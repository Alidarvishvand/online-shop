#!/bin/sh

# اگه manage.py وجود نداشت، پروژه رو بساز
if [ ! -f "manage.py" ]; then
  echo "🔧 No Django project found, creating one..."
  django-admin startproject core .
fi

# اجرای سرور
echo "🚀 Starting Django server on port 8000..."
python manage.py runserver 0.0.0.0:8000
