from fastapi import FastAPI
from db.connection import test_connection

app = FastAPI()

@app.get("/")
def read_root():
    ok, message = test_connection()
    if ok:
        return {"message": "✅ Database connection successful"}
    else:
        return {"message": "❌ Database connection failed", "error": message}