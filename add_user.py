import requests

# Replace with your desired user name
user_name = input("Enter name to add: ")

# API endpoint
url = "http://localhost:5000/users"

# POST request with JSON body
response = requests.post(url, json={"name": user_name})

# Show response
if response.status_code == 201:
    print("✅ User added successfully:", response.json())
else:
    print("❌ Failed to add user:", response.text)
