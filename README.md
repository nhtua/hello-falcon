# Hello Falcon

This document will guide you how to run this app.

## Build docker image
Because I didn't setup a private SSL Docker registry, so you must build the docker image yourself.

Run this app on docker is the fastest way to start, so let's go step by step:

1. Install Docker CE (Docker Community Edition) - If you already have docker on the machine, skip to step 2. 
   Otherwise, please follow [this link](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

2. Build the image:
```bash
cd /path/of/this/project
docker build -t hello-falcon .
```

3. Start the container:
```bash
docker run -d --rm --name hello-falcon \
    -e APP_SECRET=your_secret_key_here \
    -e APP_EXPIRED_AFTER=86400 \
    -e DATABASE_CONNECTION_STRING=postgresql+psycopg2://postgres:tua123456789@172.22.0.2:5432/customer2 \
    -e API_USERNAME=admin \
    -e API_PASSWORD=123456 \
    -p 8080:8080 \
    --network=DB \
    hello-falcon
```

Explain the command above:
- -d detach the STDOUT, running as daemon
- --rm delete the container after shutdown
- --name name of the container 
- -e set ENV variables:
    + APP_SECRET=your_secret_key_here, the secret key for HS256 algorithm in JWT 
    + APP_EXPIRED_AFTER=86400, token is expired after 86400 seconds i.e. 01 day
    + DATABASE_CONNECTION_STRING="", the string to connect database. 
      Please note that every container has it own `localhost` - don't confuse with your real `localhost`.
    + API_USERNAME set the username to login
    + API_PASSWORD set the password to login
- -p mapping port from host to container
- --network <network name> - used when you want the container to join the docker network   

After container `hello-falcon` has been run, you can explore the API.


4. View container output (log)
```bash
docker logs hello-falcon
```


5. Create user for API login:
You can defined default user as these above ENV or create others by the command: 
```bash
docker exec -it hello-falcon /bin/sh
python adduser.py --user=User --password=Secret
```


6. Stop the container:
```bash
docker stop hello-falcon
```


## Setup for dev
This session tell you about setting up the development env:

1. Requirements: Python 3.6.2
2. Install dependencies:
```bash
cd /path/of/this/project
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
3. Run the app:
```bash
gunicorn --bind=127.0.0.1:8080 --reload app:api

#or add user
python adduser.py --user=User --password=Secret
```
--reload helps gunicorn auto-reload when python files changed.

4. Switch database connection for testing
Just place the env var: `DATABASE_CONNECTION_STRING` before run the command.
```bash
DATABASE_CONNECTION_STRING=postgresql+psycopg2://postgres:tua123456789@172.22.0.2:5432/customer2
```


## Explore API via Postman

1. Import [collection here](https://www.getpostman.com/collections/ec73f671bb847e6f2d75)
2. Create new environment with a variable `token` then leave it empty
3. Choose the first endpoint `00. Login`
4. Fill the JSON content as:
```json
{
    "username":"admin",
    "password":"123456"
}
```
5. Start to explore other endpoints
