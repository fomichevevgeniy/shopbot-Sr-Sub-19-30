import sqlite3


class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('shop.db', check_same_thread=False)

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            cursor = db.cursor()
            cursor.execute(sql, args)
            if commit:
                result = db.commit()
            if fetchone:
                result = cursor.fetchone()
            if fetchall:
                result = cursor.fetchall()
            return result

    def create_users_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            full_name VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        )
        '''
        self.manager(sql, commit=True)


    def get_user_by_id(self, telegram_id):
        sql = '''
        SELECT * FROM users WHERE telegram_id = ?
        '''
        return self.manager(sql, telegram_id, fetchone=True)


    def insert_user(self, telegram_id, full_name, phone):
        sql = '''
        INSERT INTO users(telegram_id, full_name, phone) VALUES (?,?,?)
        '''
        self.manager(sql, telegram_id, full_name, phone, commit=True)


    def create_filials_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS filials(
            filial_id INTEGER PRIMARY KEY AUTOINCREMENT,
            filial_name VARCHAR(100),
            places INTEGER,
            worktime VARCHAR(100),
            address VARCHAR(100)
        )
        '''
        self.manager(sql, commit=True)

    def insert_filials(self):
        sql = '''
        INSERT INTO filials(filial_name, places, worktime, address) VALUES 
        ('Чиланзар', 50, '11:00-23:00', 'На чиланзаре'),
        ('Малика', 40, '09:00-18:00', 'На малике'),
        ('Максимка', 100, '12:00-23:00', 'На максимке'),
        ('Чорсу', 70, '10:00-23:00', 'На чорсу')
        '''
        self.manager(sql, commit=True)

    def get_filials_names(self):
        sql = '''
        SELECT filial_name FROM filials
        '''
        return self.manager(sql, fetchall=True)

    def get_filial(self, filial_name):
        sql = '''
        SELECT * FROM filials WHERE filial_name = ?
        '''
        return self.manager(sql, filial_name, fetchone=True)
