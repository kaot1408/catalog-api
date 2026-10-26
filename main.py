
from fastapi import FastAPI, HTTPException
import hashlib

app = FastAPI(title="Catalog Training API")

products = [
    {"id": 1, "name": "Laptop", "price": 1500},
    {"id": 2, "name": "Keyboard", "price": 100},
    {"id": 3, "name": "Mouse", "price": 50},
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/compute")
def compute(iterations: int = 10000):
    if not 1 <= iterations <= 200000:
        raise HTTPException(status_code=400)

    data = b"training"
    for _ in range(iterations):
        data = hashlib.sha256(data).digest()

    return {"iterations": iterations, "result": data.hex()}
