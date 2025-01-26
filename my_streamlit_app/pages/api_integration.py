import requests

def get_health_data(symptom):
    # Example API endpoint (replace with a real health API)
    api_url = f"https://api.healthdata.org/v1/symptoms/{symptom}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def display_health_data(symptom):
    data = get_health_data(symptom)
    if "error" in data:
        return f"Error fetching data: {data['error']}"
    else:
        # Process and display the data as needed
        return data
