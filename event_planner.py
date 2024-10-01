import streamlit as st
import pandas as pd
from datetime import datetime

# Function for the home page
def home_page():
    st.title("Welcome to the Event Planner")
    st.write("""
    Plan your events with ease! Use this app to add, manage, and view your upcoming events.
    You can navigate to different sections using the dropdown on the sidebar.
    """)
    
    # Display some example event planning images
    st.image("https://www.example.com/event-planning1.jpg", caption="Event Planning Example 1", use_column_width=True)
    st.image("https://www.example.com/event-planning2.jpg", caption="Event Planning Example 2", use_column_width=True)

# Function for adding events
def add_event_page():
    st.title("Add Event")
    
    with st.form("event_form"):
        event_name = st.text_input("Event Name", "")
        event_description = st.text_area("Event Description", "")
        event_date = st.date_input("Event Date", datetime.now())
        event_time = st.time_input("Event Time", datetime.now().time())
        
        submit = st.form_submit_button("Add Event")
    
    if 'events' not in st.session_state:
        st.session_state['events'] = []
    
    if submit:
        event_data = {
            "Event Name": event_name,
            "Event Description": event_description,
            "Event Date": event_date,
            "Event Time": event_time
        }
        st.session_state['events'].append(event_data)
        st.success(f"Event '{event_name}' added successfully!")

# Function for viewing events
def view_event_page():
    st.title("View Events")
    
    if 'events' in st.session_state and st.session_state['events']:
        event_df = pd.DataFrame(st.session_state['events'])
        st.dataframe(event_df)
    else:
        st.info("No events planned yet.")

# Sidebar navigation with a non-editable selectbox (Dropdown)
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Add Event", "View Events"], key="navigation")

# Display the correct page based on the user's selection
if page == "Home":
    home_page()
elif page == "Add Event":
    add_event_page()
elif page == "View Events":
    view_event_page()
