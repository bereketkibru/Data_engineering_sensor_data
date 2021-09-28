-- imputing null values with 0

{{ config(materialized='table') }}

{% set cols = ["col3", "col4", "col5", "col6", "col7", "col8", "col9","col10", "col11",
    "col12", "col13", "col14", "col15", "col16", "col17", "col18", "col19", "col20",
    "col21", "col22", "col23", "col24", "col25", "col26"] %}

with stations as (

    select date, time, station_id,
        
        {% for col in cols %}
            case
                when isnull({{col}}) then 0 else {{col}}
            end as {{col}}
            {% if not loop.last %},{% endif %}
        {% endfor %}
    from foo.I80_sample

)

select *
from stations