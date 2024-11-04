from flask import Flask, render_template
from dotenv import load_dotenv
import os
import mysql.connector

app = Flask(__name__)

load_dotenv() # Load environment variables from .env file
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def get_data_from_database():
    # Connect to your MySQL database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM Locations")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

@app.route('/')
def index():
    data = get_data_from_database()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
