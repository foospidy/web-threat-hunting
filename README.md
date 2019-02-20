# web-threat-hunting
Utility scripts to assist with threat hunting in web applications.

## Setup

run `make env` to create the Python virtual environment.
run `source .env/bin/activate` to initialize the Python virtual enviornment.

## Scripts

response_size.py - Genereate the average response size by method and by url.

response_time.py - Generate the average response time by method and by url. This script expects the access log file to contain request processing time as the last field in log entries. In Apache, add %D to the log format. In NGINX, add $request_time to the log format.
