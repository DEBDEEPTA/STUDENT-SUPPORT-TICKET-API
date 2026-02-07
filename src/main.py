from fastapi import FastAPI
from routes import auth
app = FastAPI(title="STUDENT SUPPORT TICKET API")

@app.get("/health")
def health_check():
    return "project is live!"

app.include_router(auth.router, prefix="/login", tags=['auth'])




