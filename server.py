from flask import Flask
import json
from data import me
from data import catalog

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello from Flask!"


@app.get("/test")
def test():
    return "This is another endpoint"


# get /about returns  your name
@app.get("/about")
def about():
    return "This is just 'Sebastian Lopez Wells Server'"


#####################################################
######################API PRODUCTS ##################
#####################################################


@app.get("/api/test")
def test_api():
    return json.dumps("OK")


# get /api/about return the me dict json
@app.get("/api/about")
def about_api():
    return json.dumps(me)


@app.get("/api/catalog")
def get_catalog():
    # return the list of products
    return json.dumps(catalog)


@app.get("/api/product/<id>")
def get_product_by_id(id):
    for x in catalog:
        if x["_id"] == id:
            return json.dumps(x)
    return json.dumps("ERROR: ID is not valid")


@app.get("/api/products/<category>")
def get_product_by_category(category):
    result = []
    for x in catalog:
        if x["category"].lower() == category.lower():
            result.append(x)
    return json.dumps(result)


@app.get("/api/count")
def cat_count():
    count = len(catalog)
    return json.dumps(count)


@app.get("/api/catalog/total")
def cat_price():
    total = 0
    for x in catalog:
        total += x["price"]
    return json.dumps(total)


@app.get("/api/catalog/cheapest")
def cat_cheapest():
    cheapest = catalog[0]
    for x in catalog:
        if x["price"] < cheapest["price"]:
            cheapest = x
    return json.dumps(cheapest)


# app.run(debug=True)
