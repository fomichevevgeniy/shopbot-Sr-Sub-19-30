from database.database import DataBase

db = DataBase()

# db.create_users_table()
db.create_filials_table()
db.insert_filials()