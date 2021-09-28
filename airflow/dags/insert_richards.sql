LOAD DATA 
INFILE '/var/lib/mysql-files/richards_sample.csv' 
INTO TABLE richards 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;