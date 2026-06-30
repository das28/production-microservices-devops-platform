from fastapi import FastAPI

app = FastAPI(
    title="User Service",
    description="User microservice for e-commerce platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "User Service is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user-service"}
