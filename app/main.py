from fastapi import FastAPI

app = FastAPI(title="Microservicio DevOps", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Microservicio funcionando"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/sumar/{a}/{b}")
def sumar(a: int, b: int):
    return {"resultado": a + b}
