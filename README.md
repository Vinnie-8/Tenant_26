Tenant Management System (Django)

Quick start

1. Create and activate a virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations and start server:

```powershell
python manage.py migrate
python manage.py runserver
```

API endpoints

- `GET /api/tenants/` - list tenants
- `POST /api/tenants/` - create tenant
- `GET /api/tenants/{id}/` - retrieve
- `PUT/PATCH /api/tenants/{id}/` - update
- `DELETE /api/tenants/{id}/` - delete

Admin

Create a superuser with `python manage.py createsuperuser` and open `/admin`.
