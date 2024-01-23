from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database'
)

@app.route('/users')
def display_users():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    return render_template('read_all.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
        conn.commit()
        return redirect('/users')
    return render_template('create.html')

if __name__ == '__main__':
    app.run()
