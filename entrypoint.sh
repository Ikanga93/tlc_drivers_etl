#!/bin/sh
set -e

# Run the first script 
pyhton extract.py

# Run the second script 
pyhton transform.py

# Run the third script 
pyhton load.py
