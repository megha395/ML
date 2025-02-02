from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
import joblib

app = Flask(__name__)
app.config['']