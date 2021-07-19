from config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos-and-ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo))
        return dojos

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos-and-ninjas').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        dojo.ninjas = ninja.get_ninjas_by_dojo_id(data)
        print("*******************************************************************************")
        print(dojo)
        print(dojo.ninjas)
        return dojo

    @classmethod
    def new(cls, data):
        query ="INSERT INTO dojos (name, created_at, updated_at) VALUES( %(name)s, NOW(), NOW())"
        returned_id = connectToMySQL('dojos-and-ninjas').query_db(query, data)
        return returned_id