LOAD DATA 
INFILE '/var/lib/mysql-files/station_summary.csv' 
INTO TABLE station_summary 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS