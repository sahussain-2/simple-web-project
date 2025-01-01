from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# إعداد الاتصال بقاعدة البيانات
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'database': 'testdb'
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        result = cursor.fetchone()
        return jsonify({'message': result[0] if result else 'No data found!'})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
