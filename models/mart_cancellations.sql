with bookings as (
    select * from {{ ref('stg_bookings') }}
)

select
    hotel,
    count(*) as total_bookings,
    sum(is_canceled) as total_cancellations,
    round(
        cast(sum(is_canceled) as float) / count(*) * 100
    , 2) as cancellation_rate_pct
from bookings
group by hotel
order by cancellation_rate_pct desc