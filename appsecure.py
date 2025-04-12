# Example sanitized server

from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Database connection settings
DB_CONFIG = {
    'dbname': 'test_db',
    'user': 'postgres',
    'password': 'pword', 
    'host': 'localhost',
    'port': '5432'
}

@app.route('/db-test')
def db_test():
    id_param = request.args.get('id', '1')
    try:
        # Connect to database
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Secure parameterized query
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id_param,))
        results = cursor.fetchall()

        # Format response
        response = [{'id': row[0], 'username': row[1], 'email': row[2]} for row in results]
        cursor.close()
        conn.close()
        return {'data': response}

    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)