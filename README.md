# Hello Falcon

This document will guid you how to run this app.

## Build docker image
Because I didn't setup a private SSL Docker registry, so you must to build the docker image by yourself.

Run this app on docker is the fastest way to start, so let's go step by step:

1. Install Docker CE (Docker Community Edition) - If you already have docker on the machine, skip to step 2. Otherwise, please follow [this link](https://docs.docker.com/install/linux/docker-ce/centos/)

2. Build the image:
```bash
cd /path/of/this/project
docker build -t hello-falcon .
```

3. Run the container:
```bash
docker run -d --rm --name hello-falcon -e APP_SECRET=your_secret_key_here -e APP_EXPIRED_AFTER=86400 -e DATABASE_CONNECTION_STRING="postgresql+psycopg2://postgres:tua123456789@172.22.0.2:5432/customer2" --network=DB hello-falcon
```
Explain the command above:
- -d detach the STDOUT, running as daemon
- --rm delete the container after shutdown
- -e set ENV variables:
    + APP_SECRET=your_secret_key_here, the secret key for HS256 algorithm in JWT 
    + APP_EXPIRED_AFTER=86400, token is expired after 86400 seconds
    + DATABASE_CONNECTION_STRING="", the string to connect database. Remember, every container has it own `localhost`, don't confuse with your real `localhost`.
- -p mapping port from host to container
- --name name of the container 
- --network <network name> Use when you want the container join the docker network   
After container `hello-falcon` run, you can explore the API.

4. View container output (log)
```bash
docker logs hello-falcon
```

5. Stop the container:
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
```
--reload helps gunicorn auto reload when files change.

## Explore API via Postman

1. Import [collection here](https://www.getpostman.com/collections/ec73f671bb847e6f2d75)
2. Create new enviroment with a variable `token` then leave it empty
3. Choose the first endpoint `00. Login`
4. Fill the JSON content as:
```json
{
	"username":"admin",
	"password":"123456"
}
```
5. Start to explore other endpoints