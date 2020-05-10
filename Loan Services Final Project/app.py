# Create API of ML model using flask
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler



app = Flask(__name__)

# Loading the model 
model= pickle.load(open('./model/model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/rate', methods = ['POST'])
def rate():
    # getting the data from post request
    if request.method == "POST": 
       


        loan_amount = float(request.form['loan_amount'])
        housing_status = float(request.form['housing_status'])
        annual_income = float(request.form["annual_income"])
        avg_credit_score = float(request.form["avg_credit_score"])
        loan_terms = float(request.form["loan_terms"])
        historical = pd.read_csv("master_data.csv")
        historical.dropna(inplace=True)
        user_df = pd.DataFrame([[loan_amount, housing_status, annual_income, avg_credit_score, loan_terms]], columns=["loan_amount", "housing_status", "annual_income", "avg_credit_score", "loan_terms(months)"])
        print(historical)
        print(user_df)
       



        combined_df = pd.concat([historical,user_df], ignore_index=True)
        print(combined_df)




        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(combined_df.dropna())
        
        data = [X_train_scaled[-1]]
        
        prediction = model.predict(data)


        print("Prediction", prediction)

        interest_rate = ""
        if(prediction[0] == 1):
            interest_rate = "6%"
        elif(prediction[0] == 2):
            interest_rate = "10%"
        elif(prediction[0] == 3):
            interest_rate = "15%"
        else:
            interest_rate = "20%"
        # Make prediction using model loaded from disk as per the data.
       # rate = model.rate([[data]])


        # take the first value of rate 
        #output = rate[0] 
   
    return render_template("results.html", interest_rate=interest_rate, loan_amount=loan_amount)
if __name__ == '__main__':
    app.run(debug=True)



