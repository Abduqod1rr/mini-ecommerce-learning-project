# mini-ecommerce-learning-project

🛒 Django E-commerce Project
📌 Overview

This is a full-stack E-commerce web application built with Django.
Users can browse products, add them to cart, place orders, and manage their accounts.
Sellers can add, update, and delete products.

🚀 Features
👤 Authentication

User registration & login (with session auth)

Seller and Buyer roles

Only sellers can manage their own products

🛍️ Product Management

Add, edit, delete products (with images)

Product detail & search functionality

Category & filtering support

🛒 Cart & Orders

Add to cart

View cart

Place orders

🎨 Frontend

Django Templates with CSS styling

Responsive UI (works on desktop & mobile)

⚙️ Backend

Django Models (Product, Cart, Order, User)

Class-Based Views (CBV) + Function-Based Views (FBV)

Form handling (Django Forms & ModelForms)

🗂️ Project Structure
ecommerce/
│── store/
│   ├── models.py      # Product, Cart, Order models
│   ├── views.py       # Business logic (CRUD, cart, orders)
│   ├── urls.py        # App routes
│   ├── templates/     # HTML templates
│   ├── static/        # CSS, images, JS
│
│── ecommerce/
│   ├── settings.py    # Project settings
│   ├── urls.py        # Main routes
│
│── manage.py

🛠️ Tech Stack

Backend: Django 5+

Frontend: HTML, CSS, JS (basic)

Database: SQLite (dev) → PostgreSQL (production ready)

Deployment: Docker (Gunicorn + Nginx)

⚡ Installation

Clone repo:

git clone https://github.com/abduqod1rr/ecommerce.git
cd ecommerce


Create virtual environment & install requirements:

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt


Run migrations:

python manage.py migrate


Create superuser:

python manage.py createsuperuser


Run project:

python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

🧪 Testing

Run unit tests with:

python manage.py test

🐳 Docker (Optional)

Build and run with Docker:

docker build -t ecommerce .
docker run -p 8000:8000 ecommerce

