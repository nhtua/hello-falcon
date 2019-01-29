FROM python:3.6-alpine

ENV APP_SECRET ""
ENV APP_GREETING ""
ENV APP_EXPIRED_AFTER ""
ENV DATABASE_CONNECTION_STRING ""

WORKDIR /app
COPY ./ /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev &&\
    pip install --upgrade setuptools pip wheel &&\
    pip install -r requirements.txt &&\
    cp config.example.ini config.ini


COPY ./run-container.sh /app

EXPOSE 8080
CMD ["/bin/sh", "run-container.sh"]