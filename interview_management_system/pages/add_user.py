import streamlit as st
import requests
import json

BASE_URL = "http://localhost:8000/api"

def add_user_page():
    st.subheader("Add User")

    with st.form("add_user_form"):
        user_type = st.selectbox("Select User Type", options=["CANDIDATE", "INTERVIEWER"])
        user_name = st.text_input("Enter User Name")
        submit_button = st.form_submit_button("Add User")

    if submit_button:
        if user_name:
            with st.spinner("Adding user..."):
                response = add_user(user_type, user_name)
            if "id" in response:
                st.success(f"User added successfully. User ID: {response['id']}")
            else:
                st.error(f"Error adding user: {response.get('message', 'Unknown error')}")
        else:
            st.warning("Please enter a user name.")

def add_user(user_type, name):
    url = f"{BASE_URL}/users/"
    payload = {
        "user_type": user_type,
        "name": name
    }
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"message": f"Error: {str(e)}"}