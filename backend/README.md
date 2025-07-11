# Backend

## Running the backend

### Venv Activation

```bash
# Windows
# In cmd.exe
.venv\Scripts\activate.bat
# In PowerShell
.venv\Scripts\Activate.ps1

# Unix
$ source .venv/bin/activate
```

### Install dependencies

```bash
uv pip install
```

### Running the backend

```bash
uvicorn main:app --reload
```

## Database Migrations

### Create a migration

```bash
alembic revision --autogenerate -m "migration message"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migrations

```bash
alembic downgrade -1
```
