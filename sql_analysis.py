<<<<<<< HEAD
import pandas as pd
import sqlite3

# 1. Skapa anslutning till en lokal SQLite-databas (simulerar databasmiljö)
conn = sqlite3.connect('tui_hotel_data.db')

# 2. Ladda in den tvättade datan i databasen
df = pd.read_csv('data_raw/hotel_bookings_cleaned.csv')
df.to_sql('bookings', conn, if_exists='replace', index=False)
print("Data framgångsrikt laddad till SQL-tabellen 'bookings'.")

# 3. Analys 1: Avbokningsgrad (Cancellation Rate) per hotelltyp
# Affärsfråga för TUI: Vilka typer av boenden avbokas mest?
query1 = """
SELECT 
    hotel,
    COUNT(*) as total_bookings,
    SUM(is_canceled) as total_cancellations,
    ROUND((CAST(SUM(is_canceled) AS FLOAT) / COUNT(*)) * 100, 2) as cancellation_rate_pct
FROM bookings
GROUP BY hotel;
"""
cancellation_analysis = pd.read_sql_query(query1, conn)
print("\n--- Avbokningsgrad per Hotelltyp ---")
print(cancellation_analysis)

# 4. Analys 2: Genomsnittlig bokningsframförhållning (Lead Time) för framgångsrika bokningar
# Affärsfråga för TUI: Hur många dagar i förväg bokar våra största kundgrupper?
query2 = """
SELECT 
    country,
    COUNT(*) as total_bookings,
    ROUND(AVG(lead_time), 0) as avg_lead_time_days
FROM bookings
WHERE is_canceled = 0 AND country != 'Unknown'
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 5;
"""
lead_time_analysis = pd.read_sql_query(query2, conn)
print("\n--- Topp 5 Länder: Genomsnittlig Framförhållning (dagar) ---")
print(lead_time_analysis)

# 5. Spara ett aggregerat resultat för att bygga vår Tableau Dashboard på
cancellation_analysis.to_csv('data_raw/cancellation_summary.csv', index=False)
print("\nSQL-analys klar! Aggregerad data är sparad för Tableau.")

=======
import pandas as pd
import sqlite3

# 1. Skapa anslutning till en lokal SQLite-databas (simulerar databasmiljö)
conn = sqlite3.connect('tui_hotel_data.db')

# 2. Ladda in den tvättade datan i databasen
df = pd.read_csv('data_raw/hotel_bookings_cleaned.csv')
df.to_sql('bookings', conn, if_exists='replace', index=False)
print("Data framgångsrikt laddad till SQL-tabellen 'bookings'.")

# 3. Analys 1: Avbokningsgrad (Cancellation Rate) per hotelltyp
# Affärsfråga för TUI: Vilka typer av boenden avbokas mest?
query1 = """
SELECT 
    hotel,
    COUNT(*) as total_bookings,
    SUM(is_canceled) as total_cancellations,
    ROUND((CAST(SUM(is_canceled) AS FLOAT) / COUNT(*)) * 100, 2) as cancellation_rate_pct
FROM bookings
GROUP BY hotel;
"""
cancellation_analysis = pd.read_sql_query(query1, conn)
print("\n--- Avbokningsgrad per Hotelltyp ---")
print(cancellation_analysis)

# 4. Analys 2: Genomsnittlig bokningsframförhållning (Lead Time) för framgångsrika bokningar
# Affärsfråga för TUI: Hur många dagar i förväg bokar våra största kundgrupper?
query2 = """
SELECT 
    country,
    COUNT(*) as total_bookings,
    ROUND(AVG(lead_time), 0) as avg_lead_time_days
FROM bookings
WHERE is_canceled = 0 AND country != 'Unknown'
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 5;
"""
lead_time_analysis = pd.read_sql_query(query2, conn)
print("\n--- Topp 5 Länder: Genomsnittlig Framförhållning (dagar) ---")
print(lead_time_analysis)

# 5. Spara ett aggregerat resultat för att bygga vår Tableau Dashboard på
cancellation_analysis.to_csv('data_raw/cancellation_summary.csv', index=False)
print("\nSQL-analys klar! Aggregerad data är sparad för Tableau.")

>>>>>>> 71fcdbff89a6a1763a0b13cc8067fe157117faf1
conn.close()