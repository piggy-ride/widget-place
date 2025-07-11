# Backend

## Venv Activation

```bash
# Windows
# In cmd.exe
.venv\Scripts\activate.bat
# In PowerShell
.venv\Scripts\Activate.ps1

# Unix
$ source .venv/bin/activate
```

## Install dependencies

```bash
uv pip install
```

## Running the backend

```bash
uvicorn main:app --reload
```
