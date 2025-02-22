from flask import Flask, request, jsonify
import joblib

# Create an instance of the Flask class
app = Flask(__name__)

# define prediction function
def return_prediction(model, input_json):
    input_data = [[input_json[k] for k in input_json.keys()]]
    prediction = model.predict(input_data[0])
    return prediction

model = joblib.load('abalone_predictor.joblib')
@app.route("/")
def index():
    return """
    <h1>Welcome to our abalone prediction service</h1>
    To use this service, make a JSON post request to the /predict url with the following fields:
    <ul>
    <li>length</li>
    <li>diameter</li>
    <li>height</li>
    <li>whole_weight</li>
    </ul>
    """
@app.route('/predict', methods = ['POST'])
def abalone_prediction():
    content = request.json
    results = return_prediction(model, content)
    print(results)
    return jsonify(results)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port = 8000)
    app.run(debug= True)
