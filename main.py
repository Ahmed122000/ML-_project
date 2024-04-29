from flask import Flask,jsonify,request,render_template,redirect
from train import train
from predict import prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def start():
    return render_template('home_page.html')


@app.route("/train")
def train_data():
    return render_template('train.html')

@app.route("/evaluation")
def evaluate_model():
    df = pd.read_csv("data/normal_data.csv")
    data = request.args['data_type']
    model = request.args['model']
    k = 5
    kernel = 'rbf'
    
    if data == ' oversampled':
        df = pd.read_csv("data/oversample.csv")
    elif data == 'undersapmled':
        df = pd.read_csv('data/undersample_data.csv')

    report, tr_score, te_score = train(df,  model, k, kernel).train()

    return render_template("evaluate.html", model =model, train_score = tr_score, test_score = te_score, report = report)


@app.route('/data')
def get_data():
    return render_template("input.html")


@app.route("/predict")
def predict_answer():
    data = []
    city_development = request.args['city development']
    data.append(float(city_development))

    gender = request.args['gender']
    data.append(gender)

    relevenat_exprience = request.args['relevant experience']
    data.append(relevenat_exprience)

    university = request.args['enrolled university']
    data.append(university)

    education = request.args['education level']
    data.append(education)

    discipline = request.args['major discipline']
    data.append(discipline)

    experience = request.args['experience']
    data.append(experience)

    size = request.args['company size']
    data.append(size)

    company = request.args['company type']
    data.append(company)

    last_job = request.args['last new job']
    data.append(last_job)

    training_hours = request.args['training hours']
    data.append(training_hours)

    print("dat is :{}".format(data))
    result = prediction.pr(data)
    return render_template('result.html', message = result)

app.run(debug = True)


