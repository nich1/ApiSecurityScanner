import requests
import json

# Define the API endpoint
url = "https://test-server-beta-lovat.vercel.app/db-test"

try:
    # Send a GET request
    response = requests.get(url, timeout=5)

    # Check if the request was successful
    if response.status_code == 200:
        print("✅ Success! Response received:")

        try:
            # Try parsing JSON response
            data = response.json()
            print(json.dumps(data, indent=4))  # Pretty-print JSON response

        except json.JSONDecodeError:
            # If response is not JSON, print raw text
            print("Received non-JSON response:")
            print(response.text)

    else:
        print(f"⚠️ Error: Received status code {response.status_code}")
        print("Response content:", response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
