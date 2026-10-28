from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bill Calculation Implementation.  Discount Calculation added."

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/calculate", methods=["POST"])
def calculate_bill():
    data = request.get_json() or {}
    price = data.get("price", 0.0)
    quantity = data.get("quantity", 0)
    
    total = float(price) * int(quantity)
    return jsonify(total=total), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

