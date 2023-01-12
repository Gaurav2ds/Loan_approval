from flask import Flask, render_template,request
import pickle
import numpy as np


with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():

    gender = int(request.form['Gender'])
    married= request.form['Married']
    dependents = request.form['Dependents']
    education = request.form['Education']
    Self_Employed= request.form['Self_Employed']
    ApplicantIncome = request.form['ApplicantIncome']
    CoapplicantIncome= request.form['CoapplicantIncome']
    LoanAmount = request.form['LoanAmount']
    Loan_Amount_Term = request.form['Loan_Amount_Term']
    Credit_History= request.form['Credit_History']
    Property_Area = request.form['Property_Area']
    
    
    
    
    
    res = model.predict([[gender,married,dependents,education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    print(res)
    return render_template('index.html',loan_status= res)

if __name__ == "__main__":
    app.run(debug=True)