import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the saved model and scaler from pickle
with open('best_model.pkl', 'rb') as model_file:
    best_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit app
st.title('Math Score Prediction')

# Input fields for the user to provide data
gender = st.selectbox('Gender', ['Male', 'Female'])
# Map Gender to 0 and 1 (Male=0, Female=1)
gender_mapping = {'Male': 0, 'Female': 1}
gender = gender_mapping[gender]

lunch = st.selectbox('Lunch Type', ['Standard', 'Free/Reduced'])
# Map Lunch to 0 and 1 (Standard=1, Free/Reduced=0)
lunch_mapping = {'Standard': 1, 'Free/Reduced': 0}
lunch = lunch_mapping[lunch]

test_preparation = st.selectbox('Test Preparation Course', ['Completed', 'Not Completed'])
# Map Test Preparation Course to 0 and 1 (Not Completed=0, Completed=1)
test_preparation_mapping = {'Not Completed': 0, 'Completed': 1}
test_preparation = test_preparation_mapping[test_preparation]

# Input numerical columns (reading and writing scores)
reading_score = st.number_input('Reading Score', min_value=0.0, max_value=100.0)
writing_score = st.number_input('Writing Score', min_value=0.0, max_value=100.0)

# Prepare the input data (same format as during training)
input_data = pd.DataFrame([[gender, lunch, test_preparation, reading_score, writing_score]],
                          columns=['gender', 'lunch', 'test preparation course', 'reading score', 'writing score'])

# Scale the numerical columns using the saved scaler
input_numerical = scaler.transform(input_data[['reading score', 'writing score']])

# Combine the categorical features (gender, lunch, test preparation) with the scaled features
input_processed = np.concatenate([input_data[['gender', 'lunch', 'test preparation course']].values, input_numerical], axis=1)

# Prediction
if st.button('Predict'):
    predicted_math_score = best_model.predict(input_processed)
    st.write(f'Predicted Math Score: {predicted_math_score[0]}')
