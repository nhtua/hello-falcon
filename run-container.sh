#!/bin.sh
python adduser.py --user=$API_USERNAME --password=$API_PASSWORD
gunicorn -b 0.0.0.0:8080 app:api