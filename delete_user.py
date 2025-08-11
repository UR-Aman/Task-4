import requests

user_id = input("Enter user ID to delete: ")
url = f"http://localhost:5000/users/{user_id}"

response = requests.delete(url)

if response.status_code == 200:
    print("🗑️", response.json()["message"])
else:
    print("❌ Failed to delete user:", response.text)