LOAD DATA 
INFILE '/var/lib/mysql-files/I80_sample.txt' 
INTO TABLE I80Davis 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
(date_time, station_id, @vcol3, @vcol4, @vcol5, @vcol6, @vcol7, @vcol8, @vcol9, @vcol10, @vcol11, @vcol12, @vcol13, @vcol14, @vcol15, @vcol16, @vcol17, @vcol18, @vcol19, @vcol20, @vcol21, @vcol22, @vcol23, @vcol24, @vcol25, @vcol26) 
SET col3 = NULLIF( @vcol3, ''), 
    col4 = NULLIF( @vcol4, ''), 
    col5 = NULLIF( @vcol5, ''), 
    col6 = NULLIF( @vcol6, ''), 
    col7 = NULLIF( @vcol7, ''), 
    col8 = NULLIF( @vcol8, ''), 
    col9 = NULLIF( @vcol9, ''), 
    col10 = NULLIF( @vcol10, ''), 
    col11 = NULLIF( @vcol11, ''), 
    col12 = NULLIF( @vcol12, ''), 
    col13 = NULLIF( @vcol13, ''), 
    col14 = NULLIF( @vcol14, ''),
    col15 = NULLIF( @vcol15, ''), 
    col16 = NULLIF( @vcol16, ''), 
    col17 = NULLIF( @vcol17, ''), 
    col18 = NULLIF( @vcol18, ''), 
    col19 = NULLIF( @vcol19, ''), 
    col20 = NULLIF( @vcol20, ''), 
    col21 = NULLIF( @vcol21, ''), 
    col22 = NULLIF( @vcol22, ''), 
    col23 = NULLIF( @vcol23, ''), 
    col24 = NULLIF( @vcol24, ''), 
    col25 = NULLIF( @vcol25, ''), 
    col26 = NULLIF( @vcol26, '');