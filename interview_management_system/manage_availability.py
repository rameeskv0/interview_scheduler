import streamlit as st
import requests
import json
from datetime import datetime, timedelta, time

BASE_URL = "http://localhost:8000/api"

# Function to generate a list of time slots with absolute times like 9:00 AM, 10:00 AM, etc.
def generate_time_slots():
    start = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)  # 9:00 AM
    end = datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)   # 5:00 PM
    time_slots = []
    while start <= end:
        time_slots.append(start.time())  # Append time object
        start += timedelta(hours=1)      # Increment by 1 hour
    return time_slots

def manage_availability_page():
    st.subheader("Manage Availability")

    all_users = fetch_all_users()
    interviewers = [user for user in all_users if user['user_type'] == "INTERVIEWER"]
    candidates = [user for user in all_users if user['user_type'] == "CANDIDATE"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Add Interviewer Availability")
        add_availability_form("INTERVIEWER", interviewers)

    with col2:
        st.subheader("Add Candidate Availability")
        add_availability_form("CANDIDATE", candidates)

def add_availability_form(user_type, users):
    time_slots = generate_time_slots()  # Generate time slots for dropdown

    with st.form(f"add_{user_type.lower()}_availability"):
        user = st.selectbox(f"Select {user_type}", options=users, format_func=lambda x: f"{x['name']} (ID: {x['id']})")
        date = st.date_input("Select Date", value=datetime.now().date())
        
        # Use selectbox for pre-defined time slots instead of time_input
        start_time = st.selectbox("Start Time", options=time_slots, format_func=lambda t: t.strftime('%I:%M %p'))
        end_time = st.selectbox("End Time", options=time_slots, index=1, format_func=lambda t: t.strftime('%I:%M %p'))
        
        submit_button = st.form_submit_button(f"Add {user_type} Availability")

    if submit_button:
        # Convert time to ISO format
        start_datetime = datetime.combine(date, start_time).isoformat() + "Z"
        end_datetime = datetime.combine(date, end_time).isoformat() + "Z"
        with st.spinner("Adding availability..."):
            status_code, response = add_availability(user['id'], user_type, start_datetime, end_datetime)

        # Check for success based on HTTP status code
        if status_code == 201:
            st.success(f"{user_type} availability added successfully.")
        else:
            st.error(f"Error adding availability: {response.get('message', 'Unknown error')}")

def fetch_all_users():
    all_users = []
    url = f"{BASE_URL}/users/"

    with st.spinner("Fetching all users..."):
        while url:
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                all_users.extend(data['results'])
                url = data['next']
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching users: {str(e)}")
                break

    return all_users

def add_availability(user_id, user_type, start_time, end_time):
    url = f"{BASE_URL}/{'candidate' if user_type == 'CANDIDATE' else 'interviewer'}/{user_id}/availability/"
    payload = {
        "start_time": start_time,
        "end_time": end_time
    }
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        response.raise_for_status()  # Raises an error for bad status codes
        return response.status_code, response.json()  # Return status code and JSON response
    except requests.exceptions.RequestException as e:
        return 500, {"message": f"Error: {str(e)}"}  # Return 500 for request exceptions
#manage avaialbilty