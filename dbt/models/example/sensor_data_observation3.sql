
-- Use the `ref` function to select from other models

select *
from {{ ref('sensor_data_observation2') }}
where id = 1
