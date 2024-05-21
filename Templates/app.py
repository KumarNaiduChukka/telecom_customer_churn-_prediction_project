from flask import Flask, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open("notebook\Tele_model_random_forest.pkl", 'rb'))

@app.route('/')
def welcome():
    return "Welcome Home To All"

@app.route('/predict', methods=['GET'])
def predict():

    """
     ['Age', 'Married', 'Number of Dependents', 'Gender', 'Tenure in Months', 'Offer',
        'Avg Monthly GB Download', 'Internet Type', 'Multiple Lines', 'Online Security',
        'Online Backup', 'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
        'Streaming Movies', 'Streaming Music', 'Unlimited Data', 'Monthly Charge',
        'Total Charges', 'Total Refunds', 'Total Extra Data Charges', 'Total Long Distance Charges',
        'Total Revenue', 'Number of Referrals', 'Contract', 'Paperless Billing', 'Payment Method']

    """
    input_cols=['Age', 'Married', 'Number of Dependents', 'Gender', 'Tenure in Months', 'Offer',
                     'Avg Monthly GB Download', 'Internet Type', 'Multiple Lines', 'Online Security',
                     'Online Backup', 'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
                     'Streaming Movies', 'Streaming Music', 'Unlimited Data', 'Monthly Charge',
                     'Total Charges', 'Total Refunds', 'Total Extra Data Charges', 'Total Long Distance Charges',
                     'Total Revenue', 'Number of Referrals', 'Contract', 'Paperless Billing', 'Payment Method']

    list1=[]
    for i in input_cols:
        val=request.args.get()
        list1.append(eval(val))


    predictioin=classifier.predict([list1])

    print(prediction)
    return "The Custmore Status is"+str(predicition)

    @app.route('/predict_file',methods=["POST"])
    def predict_file():
        df_test=pd.read_csv(request.files.get("file"))
        prediction=classifier.predict(df_test)
        return str(list(prediction))
 
if __name__ == "__main__":
    app.run(debug=True)
