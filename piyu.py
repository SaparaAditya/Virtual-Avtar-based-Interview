import streamlit as st
import pymysql.cursors
import csv
import base64

# Function to create the database if it doesn't exist
def create_database():
    connection = pymysql.connect(
        host='localhost',
        port=3307,
        user='root',
        password='Piyu#9263',
        database='haka',
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS haka")
        connection.commit()
    connection.close()

# Call the function to create the database
create_database()

# Connect to the MySQL database
connection = pymysql.connect(
    host='localhost',
        port=3307,
        user='root',
        password='Piyu#9263',
        database='haka',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to create the table if it doesn't exist
def create_table():
    with connection.cursor() as cursor:
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS question_answers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(255),
            answer VARCHAR(255)
        )
        """
        cursor.execute(create_table_sql)
        connection.commit()

# Call the function to create the table
create_table()

# Function to insert data into the MySQL database
def insert_question_answer(question, answer):
    with connection.cursor() as cursor:
        DB_table_name = 'question_answers'
        insert_sql = "INSERT INTO " + DB_table_name + " (question, answer) VALUES (%s, %s)"
        rec_values = (question, answer)
        cursor.execute(insert_sql, rec_values)
        connection.commit()

# Function to fetch data from MySQL
def fetch_data():
    with connection.cursor() as cursor:
        cursor.execute("SELECT question, answer FROM question_answers")
        data = cursor.fetchall()
    return data

# Streamlit app
def main():
    st.title('Download Question Answers CSV')
    if st.button('Download Data as CSV'):
        data = fetch_data()
        if data:
            with open('question_answers.csv', 'w', newline='') as csvfile:
                fieldnames = ['question', 'answer']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            st.success('Data downloaded successfully!')
            st.download_button(label="Download CSV", data=open('question_answers.csv', 'rb'), file_name='question_answers.csv')
        else:
            st.warning('No data available to download!')

# Inserting sample questions and answers
questions_answers = [
    ("What is your name?", "My name is ChatGPT."),
    ("What is the capital of France?", "The capital of France is Paris."),
    ("What is 2 + 2?", "2 + 2 equals 4."),
    ("What is the largest planet in our solar system?", "The largest planet in our solar system is Jupiter."),
    ("What is the boiling point of water?", "The boiling point of water is 100 degrees Celsius.")
]

for question, answer in questions_answers:
    insert_question_answer(question, answer)

if __name__ == '__main__':
    main()
