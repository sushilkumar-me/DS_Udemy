### Put and Delete-HTTP Verbs
### Working with API's-- Json 

from flask import Flask, jsonify, request 

app = Flask(__name__) 

## Intial data in my to-do list 
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"}, 
    {"id": 2, "name": "item 2", "description":"This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to the sample to-do list app."

## Get: Retrive all the items 

@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retrive specific item by ID
@app.route("/items/<int:item_id", methods=['GET'])
def get_items(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None: 
        return jsonify({"error":"Item not found"}) 
    return item 

## Post: Create a new task 
@app.route("/items", methods=['POST'])
def create_item(): 
    if not request.json or not 'name' in request.json: 
        return jsonify({"error": "item not found"})
    new_item = {
        "id": items[-1]["id"] +1 if items else 1
    }


if __name__ == "__main__": 
    app.run(debug=True)