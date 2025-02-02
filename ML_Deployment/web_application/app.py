from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
import joblib

app = Flask(__name__)

def return_prediction(model, input_json):
    input_data = [[input_json[k] for k in input_json.keys()]]
    prediction = model.predict(input_data)[0]
    return prediction

model = joblib.load('abalone_predictor.joblib')

class PredictForm(FlaskForm):
    length = TextField("Shell length")
    diameter = TextField("Shell diameter")
    height = TextField("Shell height")
    whole_weight = TextField("Whole weight")
    submit = SubmitField("Predict")

#setup for home page
@app.route("/", methods = ["GET", "POST"])
def index():

    form = PredictForm()

    if form.validate_on_submit():
        session['length'] = form.length.data
        session['diameter'] = form.diameter.data
        session['height'] = form.height.data
        session['whole_weight'] = form.whole_weight.data
        return redirect(url_for("prediction"))
    
    return render_template('home.html', form = form)

# prediction route that returns model prediction based on input form
@app.route('./prediction')
def prediction():
    content = {}
    content['length'] = float(session['length'])
    content['diameter'] = float(session['diameter'])
    content['height'] = float(session['height'])
    content['whole_weight'] = float(session['whole_weight'])
    results = return_prediction(model, content)
    return render_template('prediction.html', results = results)

if __name__ == '__main__':
    app.run()