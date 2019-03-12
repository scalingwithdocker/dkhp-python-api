
from models.course  import Course
from models.database import DBManager
from services import BaseResource

class test1(BaseResource):
    def on_get(self):
        dbsession = self.db.session
        coo = dbsession.query(Course).all()
        print('\n###All course: ')
        for c in coo:
            print(f'{c.id} : {c.name} : {c.code}')
        print('');
        dbsession.close()

dbm  = DBManager()

t = test1(dbm)
t.on_get()



