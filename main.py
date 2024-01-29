from fastapi import FastAPI
from json_db import JsonDB
from product import Product

app = FastAPI()

productDB = JsonDB(path='./data/products.json', db_dict={})

@app.get('/products')
def products():
    products = productDB.read()
    return { "products" : products }

@app.post('/products')
def create_product(product: Product):
    productDB.insert(product)
    return { "status" : "inserted" }
