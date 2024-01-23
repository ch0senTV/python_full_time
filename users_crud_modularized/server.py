from flask import Flask, render_template, request, redirect
from user import User
from mysqlconnection import connectToMySQL
from datetime import datetime

app = Flask(__name__)

db_connection = connectToMySQL("users_schema")

@app.route('/')
def index():
    all_users = User.get_all(db_connection)
    return render_template("index.html", users=all_users)

@app.route('/user/show/<int:user_id>')
def show(user_id):
    user = User.get_one(db_connection, user_id)
    return render_template("show_user.html", user=user)

@app.route('/add_user', methods=["POST"])
def add_user():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(db_connection, data)
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form['name']
    email = request.form['email']

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    User.update(db_connection, user_id, name, email, current_time)

    user = User.get_one(db_connection, user_id)
    return render_template('read_one_user.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)
