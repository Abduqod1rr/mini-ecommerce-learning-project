# Python image
FROM python:3.13.5

# Ishchi papka
WORKDIR /app

# requirements.txt ni ko‘chir
COPY requirements.txt .

# Kutubxonalarni o‘rnat
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani ko‘chir
COPY . .

# Portni och
EXPOSE 8000

# Django serverni ishga tushur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
