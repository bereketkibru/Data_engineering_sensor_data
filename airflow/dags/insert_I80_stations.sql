LOAD DATA 
INFILE '/var/lib/mysql-files/I80_stations.csv' 
INTO TABLE I80Stations 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
<<<<<<< HEAD
=======
IGNORE 1 ROWS
>>>>>>> db28b6bf1a5d477b3ab14fd50cdc66aed4b80d43
(ID,Fwy,Dir,District,County,City,@vState_PM,Abs_PM,Latitude,Longitude,@vLength,Type,Lanes,Name,User_ID_1,User_ID_2,User_ID_3,User_ID_4) 
SET State_PM = NULLIF( @vState_PM, ''),
    Length = NULLIF( @vLength, '');