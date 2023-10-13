FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libxml2-dev libxslt-dev libssl-dev make ffmpeg \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt
COPY ./start.sh /usr/src/app/
COPY ./edit_dockerrun.sh /usr/src/app/

EXPOSE 80
RUN chmod 777 start.sh
ENTRYPOINT ["/usr/src/app/start.sh"]