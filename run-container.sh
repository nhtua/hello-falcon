#!/bin.sh
gunicorn -b 0.0.0.0:8080 app:api