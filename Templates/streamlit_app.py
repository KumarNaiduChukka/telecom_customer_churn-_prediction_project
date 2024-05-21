import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the trained model
try:
    with open("notebook/Tele_cust_model_random_forest.pkl", "rb") as file:
        classifier = pickle.load(file)
except Exception as e:
    st.error(f"Error loading the model: {e}")

def predict_note_authentication(Age, Married, Number_of_Dependents, Gender, Tenure_in_Months, Offer,
                                Avg_Monthly_GB_Download, Internet_Type, Multiple_Lines, Online_Security,
                                Online_Backup, Device_Protection_Plan, Premium_Tech_Support, Streaming_TV,
                                Streaming_Movies, Streaming_Music, Unlimited_Data, Monthly_Charge,
                                Total_Charges, Total_Refunds, Total_Extra_Data_Charges, Total_Long_Distance_Charges,
                                Total_Revenue, Number_of_Referrals, Contract, Paperless_Billing, Payment_Method):
    # Making a prediction
    try:
        prediction = classifier.predict([[Age, Married, Number_of_Dependents, Gender, Tenure_in_Months, Offer,
                                          Avg_Monthly_GB_Download, Internet_Type, Multiple_Lines, Online_Security,
                                          Online_Backup, Device_Protection_Plan, Premium_Tech_Support, Streaming_TV,
                                          Streaming_Movies, Streaming_Music, Unlimited_Data, Monthly_Charge,
                                          Total_Charges, Total_Refunds, Total_Extra_Data_Charges, Total_Long_Distance_Charges,
                                          Total_Revenue, Number_of_Referrals, Contract, Paperless_Billing, Payment_Method]])
        return prediction
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

def main():
    st.title("Telecom Customer Churn Prediction")
    html_temp = """
    <div style="background-color:orange;padding:10px; border-radius:10px;">
    <h2 style="color:white;text-align:center;">Streamlit Telecom Customer Churn ML App</h2>
    <img src="https://via.placeholder.com/10" style="display:block; margin-left:auto; margin-right:auto; width:10%; border-radius:10px;">
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Collecting user input
    Age = st.text_input("Age", "Above 18 years")
    Married = st.selectbox("Married", [0, 1])
    Number_of_Dependents = st.selectbox("Number of Dependents", [0, 1, 2, 3, 4])
    Gender = st.selectbox("Gender", [0, 1])
    Tenure_in_Months = st.text_input("Tenure in Months", "Type Here")
    Offer = st.selectbox("Offer", [0, 1, 2, 3, 4])
    Avg_Monthly_GB_Download = st.text_input("Avg Monthly GB Download", "Type Here")
    Internet_Type = st.selectbox("Internet Type", [0, 1, 2])
    Multiple_Lines = st.selectbox("Multiple Lines", [0, 1])
    Online_Security = st.selectbox("Online Security", [0, 1])
    Online_Backup = st.selectbox("Online Backup", [0, 1])
    Device_Protection_Plan = st.selectbox("Device Protection Plan", [0, 1])
    Premium_Tech_Support = st.selectbox("Premium Tech Support", [0, 1])
    Streaming_TV = st.selectbox("Streaming TV", [0, 1])
    Streaming_Movies = st.selectbox("Streaming Movies", [0, 1])
    Streaming_Music = st.selectbox("Streaming Music", [0, 1])
    Unlimited_Data = st.selectbox("Unlimited Data", [0, 1])
    Monthly_Charge = st.text_input("Monthly Charge", "Type Here")
    Total_Charges = st.text_input("Total Charges", "Type Here")
    Total_Refunds = st.text_input("Total Refunds", "Type Here")
    Total_Extra_Data_Charges = st.text_input("Total Extra Data Charges", "Type Here")
    Total_Long_Distance_Charges = st.text_input("Total Long Distance Charges", "Type Here")
    Total_Revenue = st.text_input("Total Revenue", "Type Here")
    Number_of_Referrals = st.selectbox("Number of Referrals", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Contract = st.selectbox("Contract", [0, 1, 2])
    Paperless_Billing = st.selectbox("Paperless Billing", [0, 1])
    Payment_Method = st.selectbox("Payment Method", [0, 1, 2])

    result = ""
    if st.button("Predict"):
        try:
            # Convert inputs to the appropriate data types
            Age = float(Age)
            Tenure_in_Months = float(Tenure_in_Months)
            Avg_Monthly_GB_Download = float(Avg_Monthly_GB_Download)
            Monthly_Charge = float(Monthly_Charge)
            Total_Charges = float(Total_Charges)
            Total_Refunds = float(Total_Refunds)
            Total_Extra_Data_Charges = float(Total_Extra_Data_Charges)
            Total_Long_Distance_Charges = float(Total_Long_Distance_Charges)
            Total_Revenue = float(Total_Revenue)
            
            result = predict_note_authentication(Age, Married, Number_of_Dependents, Gender, Tenure_in_Months, Offer,
                                                 Avg_Monthly_GB_Download, Internet_Type, Multiple_Lines, Online_Security,
                                                 Online_Backup, Device_Protection_Plan, Premium_Tech_Support, Streaming_TV,
                                                 Streaming_Movies, Streaming_Music, Unlimited_Data, Monthly_Charge,
                                                 Total_Charges, Total_Refunds, Total_Extra_Data_Charges, Total_Long_Distance_Charges,
                                                 Total_Revenue, Number_of_Referrals, Contract, Paperless_Billing, Payment_Method)
            if result is not None:
                st.success(f'Customer Churn Prediction: {result}')
        except ValueError:
            st.error("Please enter valid numerical values where required.")
    
    if st.button("About"):
        st.text("Learn about customer churn prediction")
        st.text("This application uses a machine learning model to predict customer churn based on various input parameters.")

if __name__ == '__main__':
    main()
