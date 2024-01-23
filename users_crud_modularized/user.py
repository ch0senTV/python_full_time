from mysqlconnection import connectToMySQL
class User:
    DB = "users_schema.mwb"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, db):
        query = "SELECT * FROM users;"
        results = db.query_db(query)
        users = [cls(user) for user in results]
        return users
    @classmethod
    def get_one(cls, db, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        results = db.query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def save(cls, db, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) " \
                "VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        user_id = db.query_db(query, data)
        return user_id

from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    db_connection = connectToMySQL(User.DB)
    users = User.get_all(db_connection)
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
