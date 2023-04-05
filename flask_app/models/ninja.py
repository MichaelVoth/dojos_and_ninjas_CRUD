from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def ninja_create(cls, data):     #Adds form data to DB as new row
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s,%(age)s,%(dojo_id)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def ninja_select_one(cls,data):        #Gets one row of data from DB
        query = """SELECT * FROM ninjas
                    WHERE id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def ninja_update(cls,data):      #Updates one row in DB
        query = """UPDATE ninjas
                SET first_name =%(first_name)s, last_name = %(last_name)s, age = %(age)s
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def ninja_delete(cls, id):        #Deletes one row from DB
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data) 