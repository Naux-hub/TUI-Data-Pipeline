import pandas as pd
import numpy as np

# 1. Extrahera data (Extraction)
raw_data_path = 'data_raw/hotel_bookings.csv'
df = pd.read_csv(raw_data_path)

print(f"Datasetet laddat! Antal rader: {len(df)}")

# 2. Inledande tvätt (Cleaning)
# TUI värderar att man kan hantera saknade värden och datakvalitet.
# Vi kollar vilka kolumner som har null-värden
null_counts = df.isnull().sum()
print("\nSaknade värden per kolumn:")
print(null_counts[null_counts > 0])

# Vi fyller i saknade värden för att säkerställa dataintegritet
df['children'] = df['children'].fillna(0)
df['country'] = df['country'].fillna('Unknown')
df['agent'] = df['agent'].fillna(0)

# 3. Datatransformering (Transformation)
# Skapa en kolumn för 'Total Guests' - viktigt för TUIs resursplanering
df['total_guests'] = df['adults'] + df['children'] + df['babies']

# Ta bort rader där total_guests är 0 (ogiltiga bokningar)
df = df[df['total_guests'] > 0]

# Spara den tvättade datan för nästa steg (SQL-laddning)
df.to_csv('data_raw/hotel_bookings_cleaned.csv', index=False)
print("\nTvättad data har sparats som 'hotel_bookings_cleaned.csv'!")