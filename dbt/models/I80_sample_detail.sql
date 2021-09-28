with I80_sample as (
    select * from {{ ref('stg_I80_sample') }}
),

I80_stations as (
    select * from {{ ref('stg_I80_stations') }}
)

select
    I80_sample.*,
    I80_stations.County,
    I80_stations.City,
    I80_stations.Latitude,
    I80_stations.Longitude
from I80_sample
left join I80_stations
on I80_sample.station_id = I80_stations.ID
