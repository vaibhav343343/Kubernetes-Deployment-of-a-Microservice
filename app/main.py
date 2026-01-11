from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "K8s Microservice",
        "status": "RUNNING",
        "timestamp": datetime.utcnow()
    }

@app.get("/info")
def info():
    return {
        "version": "1.0.0",
        "deployment": "docker"
    }
