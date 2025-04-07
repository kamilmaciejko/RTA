from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # First arg
    try:
        num1 = float(request.args.get('num1', 0))
    except ValueError:
        num1 = 0
    # Second arg
    try:
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        num2 = 0
    # Predicting
    value = num1 + num2
    prediction = 1 if value > 5.8 else 0

    return jsonify({"prediction": prediction, "features": {'num1': num1, 'num2': num2}})

if __name__ == '__main__':
    app.run()
