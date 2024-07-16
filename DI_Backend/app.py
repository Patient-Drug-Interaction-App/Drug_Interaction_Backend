from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import cx_Oracle

app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

# Oracle database connection settings
oracle_username = os.getenv('$DB_USER')
oracle_password = os.getenv('$DB_PASS')
oracle_dsn = os.getenv('$DB_DSN')

# Function to get a connection to the Oracle database
def get_db_connection():
    connection = cx_Oracle.connect(
        user=oracle_username,
        password=oracle_password,
        dsn=oracle_dsn
    )
    return connection

# Search endpoint
@app.route('/search', methods=['GET'])
def search():
    query_param = request.args.get('query', '')

    # Perform the database query
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        sql_query = "SELECT * FROM healthcare_data WHERE Name LIKE :search_query"
        cursor.execute(sql_query, search_query=f'%{query_param}%')
        
        # Fetch all results
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        # Convert results to a list of dictionaries
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
