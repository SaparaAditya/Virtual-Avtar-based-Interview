import streamlit as st
import pandas as pd
import pymysql.cursors

# Function to establish a connection to the MySQL database
def get_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,  # Change port if necessary
        user='your_username',
        password='your_password',
        database='your_database',
        cursorclass=pymysql.cursors.DictCursor
    )

# Function to create the table in the database if it doesn't exist
def create_table():
    connection = get_connection()
    with connection.cursor() as cursor:
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS question_responses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(255),
            user_response VARCHAR(255)
        )
        """
        cursor.execute(create_table_sql)
        connection.commit()
    connection.close()

# Function to insert data into the MySQL database
def insert_question_response(question, user_response):
    connection = get_connection()
    with connection.cursor() as cursor:
        insert_sql = "INSERT INTO question_responses (question, user_response) VALUES (%s, %s)"
        rec_values = (question, user_response)
        cursor.execute(insert_sql, rec_values)
        connection.commit()
    connection.close()

# Render HTML content with Streamlit
st.title("Speech Recognition App")

# Display placeholders for HTML content
video_placeholder = st.empty()
chat_placeholder = st.empty()

# Render the HTML content using Streamlit components
video_html = """
<div id="videoPlaceholder"></div>
<div id="chatPlaceholder"></div>
<div id="question"></div>
<div id="answer"></div>
"""

st.components.v1.html(video_html, height=400)

# Execute the JavaScript code to interact with the HTML content
js_code = """
<script>
    // Your JavaScript code here
</script>
"""

st.components.v1.html(js_code)

# Run Streamlit app
if __name__ == "__main__":
    create_table()  # Ensure the table exists in the database
