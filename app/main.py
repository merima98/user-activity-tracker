from fastapi import FastAPI
from app import user_routes

app = FastAPI(title="User Management API")

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "API is running!"}
