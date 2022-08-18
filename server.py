from re import L
from flask import Flask, request, abort
import json
import random
from data import catalog, me


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


@app.post("/api/catalog")
def post_catalog():
    product = request.get_json()

    # validating
    if not "price" in product:
        return abort(400, "ERROR: Invalid price")
    if product["price"] < 1:
        return abort(400, "ERROR: Price Should be higher than 1")

    if not "title" in product:
        return abort(400, "ERROR: Invalid title")

    if len(product["title"]) < 5:
        return abort(400, "ERROR: title needs to be at least 5 characters long")

    # Assings a unique ID
    product["_id"] = random.randint(6, 1000)
    catalog.append(product)
    return product


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


# play rock , paper and scissors
@app.get("/api/game/<pick>")
def gamer(pick):

    number = random.randint(1, 3)
    if number == 1:
        pick2 = "rock"
    elif number == 2:
        pick2 = "paper"
    elif number == 3:
        pick2 = "scissors"

    if pick == "paper" and pick2 == "rock":
        winner = "Player"
    elif pick2 == "paper" and pick == "rock":
        winner = "PC"
    elif pick == "rock" and pick2 == "scissors":
        winner = "Player"
    elif pick2 == "rock" and pick == "scissors":
        winner = "PC"
    elif pick == "scissors" and pick2 == "paper":
        winner = "Player"
    elif pick2 == "scissors" and pick == "paper":
        winner = "PC"
    elif pick == pick2:
        winner = "Draw"
    results = {"you": pick, "PC": pick2, "Winner": winner}

    return json.dumps(results)


# app.run(debug=True)
