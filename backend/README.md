# Backend

## Running the backend

### Prerequisites

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create Virtual Environment

```bash
uv venv
```

### Venv Activation

```bash
# Windows
# In cmd.exe
.venv\Scripts\activate.bat
# In PowerShell
.venv\Scripts\Activate.ps1

# Unix
source .venv/bin/activate
```

### Install dependencies

```bash
uv sync
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
