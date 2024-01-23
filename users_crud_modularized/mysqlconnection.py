# mysqlconnection.py

import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )

    def query_db(self, query: str, data: dict = None):
        try:
            with self.connection.cursor() as cursor:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)

                if query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                #i remembered elif!!
                elif query.lower().startswith("select"):
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
        except Exception as e:
            print("Something went wrong", e)
            return False

    def close(self):
        self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)
