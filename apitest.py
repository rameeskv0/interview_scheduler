import requests
import random
from datetime import datetime, timedelta

# Constants
API_BASE_URL = "http://localhost:8000/api"
NUM_USERS = 1


# Generate random user data
def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Isaac", "Julia"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Create users
def create_users():
    user_ids = []
    for i in range(NUM_USERS):
        user_type = random.choice([ 'INTERVIEWER'])
        name = generate_random_name()
        response = requests.post(f"{API_BASE_URL}/users/", json={"user_type": user_type, "name": name})
        if response.status_code == 201:
            user_ids.append(response.json()['id'])
        else:
            print(f"Failed to create user: {response.json()}")
    return user_ids

create_users()