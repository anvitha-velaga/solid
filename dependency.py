class Database:
    def connect(self):
        pass
class MYSQL(Database):
    def connect(self):
        print("connected to db")
class App:
    def __init__(self,db):
        self.db=db
    def run(self):
        self.db.connect()
db=MYSQL()
app=App(db)
app.run()
