# Python 3.11 minimal image
FROM python:3.11-slim

# Ishchi katalogni yaratish va belgilash
WORKDIR /app

# requirements.txt faylini konteynerga nusxalash
COPY requirements.txt .

# kerakli kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Barcha fayllarni konteynerga nusxalash
COPY . .

# Statik fayllarni to‘plab olish
RUN python manage.py collectstatic --noinput --clear

# Gunicorn bilan Django serverni ishga tushurish
CMD ["gunicorn", "--bind", "0.0.0.0:8019", "config.wsgi:application"]
