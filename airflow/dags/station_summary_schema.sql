CREATE TABLE IF NOT EXISTS `station_summary` (
  `ID` double DEFAULT NULL,
  `flow_99` double DEFAULT NULL,
  `flow_max` double DEFAULT NULL,
  `flow_median` double DEFAULT NULL,
  `flow_total` double DEFAULT NULL,
  `n_obs` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;