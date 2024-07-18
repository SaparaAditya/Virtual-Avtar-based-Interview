from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

# Function to store arrays in MySQL
def store_arrays(connection, problems, userResponses, table_name):
    try:
        cursor = connection.cursor()
        # Create table if not exists
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, problem VARCHAR(255), user_response VARCHAR(255))")
        # Insert data into the table
        for problem, response in zip(problems, userResponses):
            sql = f"INSERT INTO {table_name} (problem, user_response) VALUES (%s, %s)"
            cursor.execute(sql, (problem, response))
        connection.commit()
        print("Arrays stored successfully in MySQL")
    except mysql.connector.Error as e:
        print("Error storing arrays in MySQL:", e)
        connection.rollback()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    problems = ["Tell me about yourself", "What was your percentage in last semester?", "What's the project you have done?"]
    userResponses = request.form.getlist('userResponse[]')
    table_name = "responses"
    connection = connect_to_mysql()
    if connection:
        store_arrays(connection, problems, userResponses, table_name)
        connection.close()
    return "Arrays stored in MySQL!"

if __name__ == '__main__':
    app.run(debug=True)