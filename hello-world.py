import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Database connection configuration
db_config = {
    "user": "dbuser",
    "password": "dbuser",
    "host": "35.223.86.138",
    "database": "orcamsiprd",
    "unix_socket":"devops-cbd3375:us-central1:devops-hub"
}

@app.route('/')
def index():
    try:
        # Connect to the Google Cloud SQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Increment the visitor count in the database
        cursor.execute("UPDATE visitor_count SET count = count + 1")
        connection.commit()

        # Retrieve the updated count
        cursor.execute("SELECT count FROM visitor_count")
        count = cursor.fetchone()[0]

        return render_template('index.html', count=count)

    except Exception as e:
        print("Error:", str(e))
        return "An error occurred"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
