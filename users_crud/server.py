from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='jay',
    password='password',
    database='database'
)

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form['name']
    email = request.form['email']

    cursor = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('UPDATE users SET name = %s, email = %s, updated_at = %s WHERE id = %s', (name, email, current_time, user_id))
    conn.commit()

    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    return render_template('read_one_user.html', user=user)

if __name__ == '__main__':
    app.run()
