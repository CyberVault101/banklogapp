import requests

def make_api_call():
    try:
        # Specify the API endpoint URL
        api_url = "https://jsonplaceholder.typicode.com/todos/1"

        # Make the GET request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Display the retrieved data
            print("API Response:")
            print("User ID:", data['userId'])
            print("Title:", data['title'])
            print("Completed:", data['completed'])

        else:
            # Display an error message for unsuccessful requests
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the request
        print(f"Error during API call: {e}")

# Call the function to make the API request
make_api_call()
