import streamlit as st
import time
from database import get_user, create_user  # Import database functions

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_type" not in st.session_state:
    st.session_state["user_type"] = None

def log_in(email):
    """Handle user login."""
    st.session_state["logged_in"] = True
    user = get_user(email)
    st.session_state["user_type"] = user[2]  # Store the user type
    st.success("Logged in!")
    time.sleep(0.5)

    # Redirect based on user type
    if st.session_state["user_type"] == "General User":
        st.page_link("pages/.py")
    else:
        st.page_link("pages/dashboard.py")

def log_out():
    """Handle user logout."""
    st.session_state["logged_in"] = False
    st.session_state["user_type"] = None
    st.success("Logged out!")
    time.sleep(0.5)
    st.switch_page("home")

# Navigation menu
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Menu", ["Home", "Sign Up", "Login", "Helplines"])

if st.session_state["logged_in"] and st.sidebar.button("Log Out"):
    log_out()

# Sign-up Form
if menu == "Sign Up":
    st.title("Sign Up Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    user_type = st.radio("Identify yourself as:", ["General User", "Medical Professional"])
    tracking = st.multiselect("What do you want us to track?", ["Screentime", "Location", "Heart Rate", "Idleness"])
    check_in_freq = st.selectbox("How often should we check in?", ["Daily", "Weekly", "Monthly"])
    contact_method = st.radio("How should we contact you?", ["Email", "SMS", "Push Notification"])

    if st.button("Sign Up"):
        create_user(name, email, user_type, tracking, check_in_freq, contact_method)
        st.success("User registered successfully! Please log in.")
        st.switch_page("login")

# Login Page
elif menu == "Login":
    st.title("Login")
    email = st.text_input("Enter your email")
    if st.button("Log In"):
        user = get_user(email)
        if user:
            log_in(email)
        else:
            st.error("User not found. Please sign up.")

# Helplines Page
elif menu == "Helplines":
    st.title("Support Helplines")
    from helplines import helpline_list  # Import helplines

    for category, contact in helpline_list.items():
        st.write(f"**{category}:** {contact}")

# Home Page
if menu == "Home":
    st.title("Welcome to Happy to Health")
    st.write("Your well-being is our priority.")
