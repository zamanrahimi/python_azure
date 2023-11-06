import requests
import json

# Define the NetBox API URL and your API token
api_url = "https://demo.netbox.dev/api/"
api_token = "b1c3507e0f204a16fdd6798deec06ca6a106b8d4"

# Define the site data
site_data = {
    "name": "Zaman",
    "slug": "Zaman",
    "status": "active",  # You can specify other status values like "planned" or "retired"

}

# Define the API endpoint for creating a site
api_endpoint = api_url + "dcim/sites/"

# Prepare the headers for the API request, including the API token
headers = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json",
}

# Send a POST request to create the site
response = requests.post(api_endpoint, headers=headers, data=json.dumps(site_data))

# Check the response
if response.status_code == 201:
    print("Site created successfully!")
else:
    print(f"Failed to create the site. Status code: {response.status_code}")
    print(response.text)
