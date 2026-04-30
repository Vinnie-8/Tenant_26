# 🏢 Tenant Management System

A comprehensive property and tenant management REST API built with **Django** and **Django REST Framework**. 
Designed to help property managers and landlords efficiently manage their properties, tenants, and lease agreements from a single platform.


---

## 📖 About the Project

The Tenant Management System is a backend API that streamlines the day-to-day operations of property management. It provides structured endpoints for tracking tenants, managing property listings, and handling lease agreements — including lease duration, rent amounts, and active/expired lease status. Whether you are managing a single building or a large portfolio of properties, this system gives you full visibility and control.

---

##  Features

-  **Tenant Management** — Store and manage complete tenant profiles including contact information and rental history
-  **Property Management** — Track property details such as address, type, number of units, and availability status
-  **Lease Management** — Create and manage lease agreements linking tenants to specific properties with start/end dates and rent amounts
-  **Filtering & Search** — Query tenants, properties, and leases with filters and search parameters
-  **Admin Panel** — Full Django Admin interface for superuser management
-  **Input Validation** — Serializer-level validation for all incoming data
-  **Browsable API** — DRF's built-in browsable API for easy testing during development

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.11+ |
| **Framework** | Django 4.x / 5.x |
| **API Layer** | Django REST Framework |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Admin** | Django Admin |

---

Getting Started

### Windows (PowerShell)

1. **Clone the repository:**

```powershell
git clone https://github.com/your-username/tenant-management-system.git
cd tenant-management-system
```

2. **Create and activate a virtual environment:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. **Apply migrations and start the server:**

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API will be running at `http://127.0.0.1:8000`

---

### macOS / Linux

```bash
git clone https://github.com/your-username/tenant-management-system.git
cd tenant-management-system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (optional — defaults to SQLite in development)
DB_NAME=tenant_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

> Never commit your `.env` file to version control.

---

## 📡 API Endpoints

All endpoints are prefixed with `/api/`.

---

### 🧑 Tenants — `/api/tenants/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tenants/` | List all tenants |
| POST | `/api/tenants/` | Create a new tenant |
| GET | `/api/tenants/{id}/` | Retrieve a tenant by ID |
| PUT | `/api/tenants/{id}/` | Fully update a tenant record |
| PATCH | `/api/tenants/{id}/` | Partially update a tenant record |
| DELETE | `/api/tenants/{id}/` | Delete a tenant |


### 🏠 Properties — `/api/properties/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/properties/` | List all properties |
| POST | `/api/properties/` | Add a new property |
| GET | `/api/properties/{id}/` | Retrieve a property by ID |
| PUT | `/api/properties/{id}/` | Fully update a property |
| PATCH | `/api/properties/{id}/` | Partially update a property |
| DELETE | `/api/properties/{id}/` | Delete a property |
| GET | `/api/properties/{id}/leases/` | List all leases for a property |


---

### 📄 Leases — `/api/leases/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/leases/` | List all lease agreements |
| POST | `/api/leases/` | Create a new lease |
| GET | `/api/leases/{id}/` | Retrieve a lease by ID |
| PUT | `/api/leases/{id}/` | Fully update a lease |
| PATCH | `/api/leases/{id}/` | Partially update a lease |
| DELETE | `/api/leases/{id}/` | Delete / terminate a lease |


## 🔧 Admin Panel

Django's built-in Admin panel gives superusers full control over all records.

1. Create a superuser:

```powershell
python manage.py createsuperuser
```

2. Open the admin panel at: `http://127.0.0.1:8000/admin`

From the admin panel you can:
- View, create, edit, and delete Tenants, Properties, and Leases
- Search and filter records by name, status, city, or date
- Manage user accounts and permissions

