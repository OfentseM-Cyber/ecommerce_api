# E-commerce Product API (Django + DRF)

This repository contains a Django REST Framework backend for an e-commerce product API. It supports product CRUD, categories, user management, search, filtering, pagination, and JWT authentication.

Getting started (local development)

1. Create and activate a virtual environment

	# Windows (PowerShell)
	python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install dependencies

	pip install -r requirements.txt

3. Run migrations and create a superuser

	python manage.py migrate
	python manage.py createsuperuser

4. Run the development server

	python manage.py runserver

API endpoints (examples)

- List products: GET /api/products/
- Retrieve product: GET /api/products/{id}/
- Create product: POST /api/products/ (authenticated)
- Update product: PUT /api/products/{id}/ (authenticated)
- Delete product: DELETE /api/products/{id}/ (authenticated)
- Search: GET /api/products/?search=phone
- Filter by category: GET /api/products/?category__name=Electronics
- Price range: GET /api/products/?price__gte=10&price__lte=100
- Pagination: GET /api/products/?page=2
- Obtain token: POST /api/auth/token/ with username and password

Notes

- This project uses SQLite for local development. For production, configure PostgreSQL and secure SECRET_KEY and DEBUG via environment variables.
- The stock deduction on order placement is a future enhancement.
ecommerce api
