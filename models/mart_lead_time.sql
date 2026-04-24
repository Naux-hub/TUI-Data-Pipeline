with bookings as (

    select * from {{ ref('stg_bookings') }}

)

select
    country,
    count(*) as total_bookings,
    round(avg(lead_time), 0) as avg_lead_time_days
from bookings
where is_canceled = 0
and country != 'Unknown'
group by country
order by total_bookings desc
limit 10
