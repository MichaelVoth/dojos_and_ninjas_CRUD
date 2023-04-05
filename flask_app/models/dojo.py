from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = "dojos_and_ninjas"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def dojo_select_all(cls):             #Gets all info from DB
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo_dict in results:
            dojos.append(cls(dojo_dict))
        return dojos
    
    @classmethod
    def dojo_create(cls, data):     #Adds form data to DB as new row
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def dojo_and_ninja_select( cls , data ):    #Creates a table of a dojo and the ninjas within that dojo
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db( query , data )
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db['dojo_id'],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo
    
    @classmethod
    def dojo_delete(cls, id):        #Deletes one row from DB
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data) 