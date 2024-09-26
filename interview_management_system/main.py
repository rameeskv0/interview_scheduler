import streamlit as st

st.set_page_config(page_title="Interview Management System", layout="wide")

st.title("Interview Management System")

# Sidebar for navigation (keep only this one)
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a page to navigate:")
page = st.sidebar.radio("Go to", ("Add User", "Manage Availability", "Check Available Slots"))

# Load the corresponding page
if page == "Add User":
    from add_user import  add_user_page
    add_user_page()
elif page == "Manage Availability":
    from manage_availability import manage_availability_page
    manage_availability_page()
elif page == "Check Available Slots":
    from check_available_slots import check_available_slots_page
    check_available_slots_page()
