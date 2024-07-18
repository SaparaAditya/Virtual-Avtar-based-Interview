import streamlit as st
import json
import os
import webbrowser

# Function to save user data to local storage
def save_user_data(username, password):
    if not os.path.exists("user_data.json"):
        user_data = {}
    else:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)

    # Add new user data if username and password are not empty
    if username.strip() and password.strip():
        user_data[username] = {"password": password}

        # Save updated user data to local storage
        with open("user_data.json", "w") as file:
            json.dump(user_data, file)
        return True
    return False

# Function to check if the user exists in local storage
def is_user_exists(username):
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            return username in user_data
    return False

# Function to check if the password matches with the stored user password
def is_password_matched(username, password):
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            return user_data.get(username, {}).get("password") == password
    return False

# Main function to handle login and sign-up
def main():
    st.title("Login and Sign-up Module")

    # Get session state
    session_state = st.session_state

    # Username input field
    username = st.text_input("Username")

    # If username is entered and new_password does not exist in session state
    if username.strip() and 'new_password' not in session_state:
        password = st.text_input("Password", type="password")

        # Enable or disable the login button based on whether username and password are empty
        is_empty = not (password.strip())
        login_button = st.button("Login", disabled=is_empty)

        # If button is clicked and fields are not empty
        if login_button:
            if is_user_exists(username):
                if is_password_matched(username, password):
                    st.success("Logged in successfully!")
                    # Automatically redirect to app.py after successful login
                    url = f"http://localhost:8502/?username={username}"
                    webbrowser.open_new_tab(url)
                else:
                    st.error("Invalid password. Please try again.")
            else:
                st.warning("User does not exist.")
                # Set session state to indicate that the user is signing up
                session_state['new_password'] = True

    # If new_password exists in session state or user does not exist, it indicates the user is signing up
    if 'new_password' in session_state or not is_user_exists(username):
        # Display sign-up section
        sign_up_section(username)

# Function to handle sign-up
def sign_up_section(username):
    st.subheader("Sign-up")
    new_password = st.text_input("New Password", type="password")

    # Enable or disable the sign-up button based on whether new password is empty
    is_empty = not (new_password.strip())
    sign_up_button = st.button("Sign up", disabled=is_empty)

    # If button is clicked and new password is not empty
    if sign_up_button:
        if save_user_data(username, new_password):
            st.success("Signed up successfully! You can now login.")
            # Clear session state to prevent redirection to sign-up section
            st.session_state.pop('new_password', None)
        else:
            st.error("Password cannot be empty.")

# Run the main function
if __name__ == "__main__":
    main()