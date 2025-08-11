# 🧑‍💻 Flask REST API – User Management

This is a simple RESTful API built using **Flask** that performs **CRUD operations** on in-memory user data. It demonstrates basic **GET**, **POST**, **PUT**, and **DELETE** functionality, and includes **Python scripts** for interacting with the API.

---

## 🚀 Features

- 🔍 View all users
- ➕ Add a user
- ✏️ Update a user
- ❌ Delete a user
- 🧪 Test with Postman or Python scripts

---

## 🛠 Tech Stack

- Python 3
- Flask
- Requests (for client scripts)
- Postman or Curl (optional testing tools)

---

## 📁 Project Structure

```
📁 flask-api/
│
├── app.py             # Flask API server
├── add_user.py        # Script to add a new user (POST)
├── view_users.py      # Script to view all users (GET)
├── update_user.py     # Script to update a user (PUT)
├── delete_user.py     # Script to delete a user (DELETE)
└── README.md          # Project documentation
```

---

## ▶️ How to Run

### 1. Install Flask and Requests
```bash
pip install flask requests
```

### 2. Run the Flask API server
```bash
python app.py
```

The server will run on: `http://localhost:5000`

---

## 🧪 How to Use Client Scripts

### ➕ Add a user
```bash
python add_user.py
```
Enter name when prompted.

### 🔍 View all users
```bash
python view_users.py
```

### ✏️ Update a user
```bash
python update_user.py
```
Enter user ID and new name when prompted.

### ❌ Delete a user
```bash
python delete_user.py
```
Enter user ID when prompted.

---

## 🧪 Optional: Test Using Postman

- `GET` http://localhost:5000/users
- `POST` http://localhost:5000/users
  ```json
  {
    "name": "Aman"
  }
  ```
- `PUT` http://localhost:5000/users/1
  ```json
  {
    "name": "Updated Name"
  }
  ```
- `DELETE` http://localhost:5000/users/1

---


## 👨‍💻 Author

**Aman Kumar**  
Python Intern | Flask REST API Task
