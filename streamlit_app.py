# import streamlit as st
# import joblib
# import numpy as np

# # Load the scaler and models
# scaler = joblib.load('scaler.joblib')
# models = {
#     "processing": joblib.load('svm_model_processing.joblib'),
#     "perception": joblib.load('svm_model_perception.joblib'),
#     "input": joblib.load('svm_model_input.joblib'),
#     "understanding": joblib.load('svm_model_understanding.joblib'),
# }

# # Define the prediction function
# def predict(user_input):
#     # Ensure the input is in the same order as your model expects
#     user_input_array = np.array(user_input).reshape(1, -1)

#     # Scale the input using the saved scaler
#     user_input_scaled = scaler.transform(user_input_array)

#     # Predict outcomes for all target variables
#     predictions = {}
#     for target, model in models.items():
#         prediction = model.predict(user_input_scaled)
#         predictions[target] = prediction[0]

#     return predictions

# # Streamlit UI
# st.title("ML Prediction Application")
# st.header("Input your data for predictions")

# # Create input fields for user input
# columns = [
#     'Course Overview', 'Reading File', 'Abstract Materiale', 
#     'Concrete Material', 'Visual Materials', 'Self-Assessment', 
#     'Exercises Submit', 'Quiz Submitted', 'Playing', 'Paused', 
#     'Unstarted', 'Buffering'
# ]

# user_input = []
# for col in columns:
#     value = st.number_input(f"{col}", value=0.0)
#     user_input.append(value)

# # Button for making predictions
# if st.button("Predict"):
#     # Ensure proper input and predict
#     try:
#         predictions = predict(user_input)
#         st.subheader("Predictions")
#         st.json(predictions)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

# # Share instructions for deployment
# st.markdown("""
#     - To run the app, execute `streamlit run app.py` in your terminal.
#     - Make sure the `scaler.joblib` and model files are in the same directory as this script.
# """)


import streamlit as st
import joblib
import numpy as np

# Load the scaler and models
scaler = joblib.load('scaler.joblib')
models = {
    "processing": joblib.load('svm_model_processing.joblib'),
    "perception": joblib.load('svm_model_perception.joblib'),
    "input": joblib.load('svm_model_input.joblib'),
    "understanding": joblib.load('svm_model_understanding.joblib'),
}

def predict(user_input):
    user_input_array = np.array(user_input).reshape(1, -1)
    user_input_scaled = scaler.transform(user_input_array)
    predictions = {}
    for target, model in models.items():
        prediction = model.predict(user_input_scaled)
        predictions[target] = prediction[0]
    return predictions

st.title("Prediction API")
st.header("Provide Input via POST Request")

# Create API Endpoint Simulation
if 'user_input' in st.experimental_get_query_params():
    user_input = st.experimental_get_query_params().get('user_input', [])
    user_input = list(map(float, user_input))  # Convert to float
    output = predict(user_input)
    st.json(output)
else:
    st.write("No input provided. Pass `user_input` as query params.")
