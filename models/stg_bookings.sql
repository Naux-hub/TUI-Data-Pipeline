with source as (

    select * from read_csv_auto('C:/Users/samue/OneDrive/Skrivbord/TUI_Analytics_Project/data_raw/hotel_bookings_cleaned.csv')

),

staged as (

    select
        hotel,
        is_canceled,
        lead_time,
        country,
        adults,
        children,
        babies,
        adults + children + babies as total_guests,
        reservation_status
    from source
    where adults + children + babies > 0

)

select * from staged