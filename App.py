from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = []

@app.route('/')
def home():
    return "👋 Welcome to the User API!"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    new_user = {
        'id': len(users) + 1,
        'name': data['name']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == user_id), None)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'name' in data:
        user['name'] = data['name']
    return jsonify(user), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': f'User {user_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
