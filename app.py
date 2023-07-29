from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for testing
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 5.49},
    {"id": 3, "name": "Product 3", "price": 15.0},
]


# Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404


@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "price": data['price'],
    }
    products.append(new_product)
    return jsonify(new_product), 201


@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        data = request.get_json()
        product["name"] = data['name']
        product["price"] = data['price']
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [item for item in products if item["id"] != product_id]
    return jsonify({"message": "Product deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
