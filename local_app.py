import requests

def get_predictions_from_streamlit_cloud(user_input):
    # Replace <your-streamlit-app> with your deployed Streamlit Cloud app URL
    streamlit_url = "https://<your-streamlit-app>.streamlit.app/"
    params = {"user_input": ",".join(map(str, user_input))}  # Format input as a comma-separated string

    try:
        response = requests.get(streamlit_url, params=params)
        print("Response Text:", response.text)  # Debugging: Check raw response
        if response.status_code == 200:
            return response.json()  # Parse and return JSON response
        else:
            return {"error": f"Error: {response.status_code}, {response.text}"}
    except Exception as e:
        return {"error": str(e)}

# Example input from local app
if __name__ == "__main__":
    # Example user input
    user_input = [1.0, 0.5, 2.0, 3.0, 1.2, 0.8, 1.5, 2.5, 0.0, 0.0, 1.0, 0.0]
    result = get_predictions_from_streamlit_cloud(user_input)
    print("Predictions from Streamlit Cloud:")
    print(result)
