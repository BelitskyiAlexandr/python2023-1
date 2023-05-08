import sqlite3

class ORMMapper:
   
    def __init__(self, class_name):
        self.class_name = class_name

    def convert_to_db(self):
        # отримуємо список атрибутів класу
        attributes = [attr for attr in dir(Person) if not attr.startswith('__')]


        create_table_command = "CREATE TABLE IF NOT EXISTS " + self.class_name.__name__ + " ("
        for attribute in attributes:
            create_table_command += attribute + " " + self._get_sqlite_type(attribute)+ ","
        create_table_command = create_table_command[:-1] + ");"


        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_command)

        sqlite3.connect('database.db').close()        

    def _get_sqlite_type(self, attribute_type):
        if attribute_type == int:
            return 'INTEGER'
        elif attribute_type == float:
            return 'REAL'
        elif attribute_type == str:
            return 'TEXT'
        else:
            return 'BLOB'    
        
class Person:
    id = 0
    name = ""
    age = 0
    
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

orm_mapper = ORMMapper(Person)
orm_mapper.convert_to_db()

