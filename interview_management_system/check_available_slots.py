import streamlit as st
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api"

def check_available_slots_page():
    st.subheader("Check Available Slots")

    all_users = fetch_all_users()
    interviewers = [user for user in all_users if user['user_type'] == "INTERVIEWER"]
    candidates = [user for user in all_users if user['user_type'] == "CANDIDATE"]

    with st.form("check_available_slots"):
        interviewer = st.selectbox("Select Interviewer", options=interviewers, format_func=lambda x: f"{x['name']} (ID: {x['id']})")
        candidate = st.selectbox("Select Candidate", options=candidates, format_func=lambda x: f"{x['name']} (ID: {x['id']})")
        submit_button = st.form_submit_button("Check Available Slots")

    if submit_button:
        with st.spinner("Fetching available slots..."):
            available_slots = get_available_slots(candidate['id'], interviewer['id'])
        
        if isinstance(available_slots, list) and available_slots:
            st.success("Available slots found!")
            
            # Sort available slots by start time
            available_slots = sorted(available_slots, key=lambda slot: datetime.strptime(slot[0], "%Y-%m-%d %H:%M"))
            
            # Display sorted slots
            for slot in available_slots:
                start = datetime.strptime(slot[0], "%Y-%m-%d %H:%M")
                end = datetime.strptime(slot[1], "%Y-%m-%d %H:%M")
                # Display the times in 12-hour format with AM/PM
                st.write(f"Date: {start.strftime('%B %d, %Y')} - Time: {start.strftime('%I:%M %p')} to {end.strftime('%I:%M %p')}")
        elif isinstance(available_slots, list) and not available_slots:
            st.warning("No available slots found for the selected interviewer and candidate.")
        else:
            st.error("Could not fetch available slots. Please try again later.")

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

def get_available_slots(candidate_id, interviewer_id):
    payload = {
        "candidate_id": candidate_id,
        "interviewer_id": interviewer_id
    }
    try:
        response = requests.post(f"{BASE_URL}/get_available_slots/", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"message": f"Error: {str(e)}"}