FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --upgrade pip -i https://pypi.org/simple && pip install --default-timeout=100 -r requirements.txt -i https://pypi.org/simple

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
