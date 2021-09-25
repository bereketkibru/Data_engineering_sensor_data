
-- Use the `ref` function to select from other models

select *
from {{ ref('sensor_data') }}
where id = 1
