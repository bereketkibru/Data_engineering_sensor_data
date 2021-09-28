with station_summary as (
    select * from {{ ref('stg_station_summary') }}
),

I80_stations as (
    select * from {{ ref('stg_I80_stations') }}
)

select
    station_summary.ID,
    I80_stations.County,
    I80_stations.City,
    I80_stations.Latitude,
    I80_stations.Longitude,
    station_summary.flow_max,
    station_summary.flow_median,
    station_summary.flow_total,
    station_summary.n_obs
from station_summary
left join I80_stations using (ID)
