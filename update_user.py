import requests

user_id = input("Enter user ID to update: ")
new_name = input("Enter new name: ")

url = f"http://localhost:5000/users/{user_id}"
response = requests.put(url, json={"name": new_name})

if response.status_code == 200:
    print("✅ User updated successfully:", response.json())
else:
    print("❌ Failed to update user:", response.text)