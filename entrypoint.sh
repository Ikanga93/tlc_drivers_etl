#!/bin/sh
set -e

# Run the first script 
python /Users/jbshome/Desktop/tlc_drivers_etl/dags/extract.py

# Run the second script 
python /Users/jbshome/Desktop/tlc_drivers_etl/dags/transform.py

# Run the third script 
python /Users/jbshome/Desktop/tlc_drivers_etl/dags/load.py
