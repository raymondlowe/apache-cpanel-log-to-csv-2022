# apache-cpanel-log-to-csv-2022
Convert an apache log, as made with default cpanel settings, into csv that works in 2022

- There are other projects that do apache log -> csv but I can't find one that works in my environment so I'm creating the wheel from scratch <shrug>

## usage
  
  ```convert.py <name of whatever apache log file>```
  
 Presumes the log file name ends "log" and creates an output file name ending "log.csv" which can be read into Excel or anything else that accepts .csv
  
 ## todo
  
  - parse the date fields sensibly 
  - parse the request to split the get, page and protocol
  
