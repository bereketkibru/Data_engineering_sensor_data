CREATE TABLE IF NOT EXISTS `richards` (
  `timestamp` text,
  `flow1` double DEFAULT NULL,
  `occupancy1` double DEFAULT NULL,
  `flow2` double DEFAULT NULL,
  `occupancy2` double DEFAULT NULL,
  `flow3` double DEFAULT NULL,
  `occupancy3` double DEFAULT NULL,
  `totalflow` double DEFAULT NULL,
  `weekday` double DEFAULT NULL,
  `hour` double DEFAULT NULL,
  `minute` double DEFAULT NULL,
  `second` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;