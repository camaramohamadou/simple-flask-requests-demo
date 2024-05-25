from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample customer data
customers = {
    "1": {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
    "2": {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 25},
    "3": {"name": "Emily Johnson", "email": "emily.johnson@example.com", "age": 35}
}

@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)


@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
