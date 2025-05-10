#!/bin/sh

# اگه پروژه Django هنوز ساخته نشده، بسازش
if [ ! -f "manage.py" ]; then
  echo "🔧 No Django project found, creating one..."
  django-admin startproject core .
fi

# اعمال مهاجرت‌ها
echo "📦 Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# اجرای سرور
echo "🚀 Starting Django server on port 8000..."
python manage.py runserver 0.0.0.0:8000
