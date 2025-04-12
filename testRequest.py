import requests
import json

# Define the API endpoint
url = "http://localhost:5000/db-test"

try:
    # Send a normal GET request
    response = requests.get(url, timeout=5)

    # Check if the request was successful
    if response.status_code == 200:
        print("✅ Success! Normal response received:")

        try:
            # Parse JSON response
            data = response.json()
            print(json.dumps(data, indent=4))

        except json.JSONDecodeError:
            print("Received non-JSON response:")
            print(response.text)

    else:
        print(f"⚠️ Error: Received status code {response.status_code}")
        print("Response content:", response.text)

    # SQL Injection Test
    print("\n🔍 Testing for SQL Injection vulnerability...")
    sql_injection_payload = "?id=1 OR 1=1"  # Updated payload for integer column
    test_url = url + sql_injection_payload

    try:
        # Send GET request with SQL injection payload
        injection_response = requests.get(test_url, timeout=5)

        if injection_response.status_code == 200:
            print("✅ SQL Injection test response received:")
            try:
                injection_data = injection_response.json()
                print(json.dumps(injection_data, indent=4))

                # Check for potential vulnerability
                if data != injection_data:
                    print("⚠️ Warning: Response differs with SQL injection payload. Potential vulnerability detected!")
                else:
                    print("🛡️ No obvious SQL injection vulnerability detected (responses are identical).")

            except json.JSONDecodeError:
                print("Received non-JSON response for SQL injection test:")
                print(injection_response.text)

        else:
            print(f"⚠️ SQL Injection test failed with status code {injection_response.status_code}")
            print("Response content:", injection_response.text)

    except requests.exceptions.RequestException as e:
        print(f"❌ SQL Injection test request failed: {e}")

except requests.exceptions.RequestException as e:
    print(f"❌ Normal request failed: {e}")