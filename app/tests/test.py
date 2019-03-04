from pprint import pprint
import unittest

from app.models.students import Student
from app.services.postgres import DbUtil


class Test(unittest.TestCase):

    def test_run01(self):
        with DbUtil.get_session() as session:
            allStudent = session.query(Student).all()

            for s in allStudent:
                print(f'{s.code} {s.name}')

    # def test_run02(self):
    #     users = User.find_all()
    #     pprint(users)
    #
    # def test_run03(self):
    #     u = User(**dict(
    #         email = 'some@eemail.com',
    #         name  = 'Some Name',
    #     ))
    #     pprint(u.to_dict())
    #
    # def test_run04(self):
    #     u = User(**dict(
    #         email = 'some@eemail.com',
    #         name  = 'Some Name',
    #     ))
    #     DbUtil.insert(u)
    #
    #     users = User.find_all()
    #     pprint(users)
    
