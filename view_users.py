import requests

url = "http://localhost:5000/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    if users:
        print("📋 Users List:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}")
    else:
        print("🚫 No users found.")
else:
    print("❌ Failed to fetch users:", response.text)