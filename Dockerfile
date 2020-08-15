FROM python:3.8-alpine3.12
MAINTAINER dbgroldan

WORKDIR /usr/src/app

ENV HOST 0.0.0.0
ENV PORT_HTTP 4000
ENV DB_NAME user_db
ENV DB_USER dbgroldan
ENV DB_HOST 127.0.0.1
ENV DB_PORT 5432
ENV DB_PASSWORD dbgroldan
ENV DB_TABLES_PATH src/config/db_config.sql

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /usr/src/app/

EXPOSE 4000

CMD python /usr/src/app/src/main.py
