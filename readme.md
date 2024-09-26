# Advanced Interview Scheduling System

This project provides an advanced interview scheduling system that allows HR personnel to efficiently schedule interviews by selecting time slots. The system automatically matches candidates and interviewers based on their registered availability.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Django API](#running-the-django-api)
- [Testing the API](#testing-the-api)
- [Running the Streamlit App](#running-the-streamlit-app)
- [Conclusion](#conclusion)

---

## Features

- **Time Slot Selection**: HR can select predefined time slots for interviews.
- **Automatic Matching**: Automatically match interviewers and candidates based on availability.
- **Real-Time Suggestions**: Show potential matches based on the selected slot.
- **Streamlit Interface**: HR can manually test matches using a simple Streamlit UI.
  
---

## Project Structure

├── interview_scheduler/ # Main Django project folder │ ├── interview_scheduler/ # Django settings │ ├── api/ # Django app containing models and views │ ├── manage.py # Django management script ├── streamlit_app/ # Streamlit application folder │ ├── app.py # Streamlit app script ├── requirements.txt # Python dependencies ├── README.md # Project instructions


---

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- Streamlit 1.8+
- PostgreSQL or SQLite (default)
- Git

---

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rameeskv0/interview_scheduler.git
    cd interview_scheduler
    ```



2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Django API

1. **Navigate to the project folder**:
    ```bash
    cd interview_scheduler
    ```

2. **Apply database migrations**:
    ```bash
   python manage.py makemigrations 
   python manage.py migrate
    ```

3. **Create a superuser** (for accessing Django admin):
    ```bash
    python manage.py createsuperuser
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the Django admin panel**:
    - Navigate to `http://127.0.0.1:8000/admin/` in your browser.
    - Log in with the superuser credentials you created.

---

## Testing the API

You can test the API endpoints using tools like [Postman](https://www.postman.com/) or `curl`.

### Available Endpoints

1. **User List** (GET)
    ```bash
    GET http://127.0.0.1:8000/api/users/
    ```

2. **Create Availability** (POST)
    ```bash
    POST http://127.0.0.1:8000/api/availabilities/
    Content-Type: application/json
    Body: {
      "user": 1,
      "start_time": "2024-09-26T09:00:00Z",
      "end_time": "2024-09-26T10:00:00Z"
    }
    ```

3. **Fetch Available Candidates and Interviewers** (GET)
    ```bash
    GET http://127.0.0.1:8000/api/match/?start_time=2024-09-26T09:00:00&end_time=2024-09-26T10:00:00
    ```

4. **Create User** (POST)
    ```bash
    POST http://127.0.0.1:8000/api/users/
    Content-Type: application/json
    Body: {
      "user_type": "CANDIDATE",
      "name": "John Doe"
    }
    ```

---

## Running the Streamlit App

1. **Navigate to the Streamlit folder**:
    ```bash
    cd interview_management_system
    ```

2. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

3. **Access the app**:
    - Open your browser and go to `http://localhost:8501`.
    - You should see the Streamlit interface, where you can manually test interview scheduling.

---


## Using the Streamlit App

The Streamlit app allows HR personnel to add interviewers and candidates, register their available time slots, and check for overlapping time slots for scheduling interviews.

### Step-by-Step Guide

1. **Adding Interviewers and Candidates**:
   - Go to the **"Add User"** section in the Streamlit app.
   - Enter the name and select the user type (both **Interviewer** and **Candidate**).
   - Click **Submit** to add the user to the system.
   
2. **Registering Availability**:
   - Go to the **"Add Availability"** section.
   - Select the user (interviewer and candidate) from the dropdown.
   - Enter the available start time and end time for the selected user.
   - Click **Submit** to register the availability.
   
3. **Checking Matching Available Slots**:
   - Go to the **"Check Available Slots"** section.
   - Select a specific time range you want to check (e.g., 9:00 AM - 10:00 AM, 10:00 AM - 11:00 AM).
   - The system will automatically check both the interviewer and candidate availability, and if overlapping slots are found, they will be displayed in the output.

---

### Example Scenario

- **Interviewer Availability**: 9:00 AM - 12:00 PM
- **Candidate Availability**: 10:00 AM - 2:00 PM

#### Steps:

1. **Add Users**: 
   - Add **Interviewer** (e.g., "Jane Smith") with availability from 9:00 AM to 12:00 PM.
   - Add **Candidate** (e.g., "John Doe") with availability from 10:00 AM to 2:00 PM.
   
2. **Register Availability**:
   - For **Jane Smith** (Interviewer), register availability from 9:00 AM to 12:00 PM.
   - For **John Doe** (Candidate), register availability from 10:00 AM to 2:00 PM.
   
3. **Check Available Time Slots**:
   - Once both users are registered, you can check for **matching available slots**.
   - In this case, overlapping available slots would be displayed as:
     ```plaintext
     Available Slots: [(10:00 AM - 11:00 AM), (11:00 AM - 12:00 PM)]
     ```
   - These time slots represent the matching availability between the interviewer and the candidate where interviews can be scheduled.

---

### Additional Features:

- **Automatic Slot Suggestions**: The app will automatically suggest matching time slots between the interviewer and candidate, based on their registered availability.
- **Slot Validation**: If no overlapping slots are found, the app will notify the user that no matching time slots are available for the selected time range.



## Conclusion

This project provides a robust, user-friendly solution for interview scheduling. HR personnel can manage and schedule interviews with ease using the automated system. The Django API offers a backend for testing programmatically, while the Streamlit app provides a manual interface for HR personnel to visualize and test the scheduling system.

If you encounter any issues or have any questions, feel free to open an issue in the repository.

---



