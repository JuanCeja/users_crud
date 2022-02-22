
from unittest import result
from mysqlconnection import connectToMySQL

DATABASE = "users_shcema"

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fullname = f'{ self.first_name } { self.last_name }'

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Users;"

        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            table_names = []
            for user in results:
                table_names.append(cls(user))
            return table_names
        return []

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
        updated_result = connectToMySQL(DATABASE).query_db(query, data)
        return updated_result

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        person_id = connectToMySQL(DATABASE).query_db(query, data)
        return person_id

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)