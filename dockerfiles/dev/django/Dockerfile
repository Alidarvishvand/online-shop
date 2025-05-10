FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

# نصب ابزارهای مورد نیاز (در یک مرحله)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    netcat \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# نصب پکیج‌های پایتون
COPY ./requirements.txt .
RUN pip install --upgrade pip -i https://pypi.org/simple && pip install --default-timeout=100 -r requirements.txt -i https://pypi.org/simple

# کپی و تنظیم اسکریپت‌ها
COPY ./entrypoint.sh /entrypoint.sh
COPY ./wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /entrypoint.sh /wait-for-postgres.sh

# اجرای نهایی
ENTRYPOINT ["/wait-for-postgres.sh", "/entrypoint.sh"]
