import falcon
import falcon_jsonify
import json
import requests
from models.student import Student
from services import BaseResource
from falcon.util.uri import encode as uri_encode

class StudentColletionService(BaseResource):
    def on_get(self, req, resp):
        dbsession =self.db.session
        student = dbsession.query(Student)\
            .order_by(Student.id.desc())\
            .all()

        student = [dict(
            id=row.id,
            name=row.name,
            code=row.code,
            class_code=row.class_code
        ) for row in student]

        resp.body = (json.dumps(student, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')

        # print(result_json['name'])
        new_student = Student(
            name=result_json['name'],
            code=result_json['code'],
            class_code = result_json['class_code']
        )

        dbsession = self.db.session
        dbsession.add(new_student)
        dbsession.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result_json, ensure_ascii=False)
        dbsession.close()

class StudentSingleService(BaseResource):
    def on_get(self, req, resp, id):

        dbsession = self.db.session
        student = dbsession.query(Student).filter(Student.id == id).first()
        if student is None:
            raise falcon.HTTPNotFound()
            resp.status = falcon.HTTP_404
        student =dict(
            id=Student.id,
            name=Student.name,
            code=Student.code,
            class_code=Student.class_code
        )
        # print(Student)
        resp.body = (json.dumps(Student, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_put(self, req, resp, id):
        dbsession=self.db.session
        student = dbsession.query(Student).filter(Student.id == id).first()
        if student is None:
            raise falcon.HTTPNotFound
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')
        student.name = result_json['name']
        student.code = result_json['code']
        student.class_code = result_json['class_code']

        if len(dbsession.dirty) > 0:
            dbsession.commit()
        student = dict(
            id=student.id,
            name=student.name,
            code=student.code,
            class_code=student.class_code

        )
        # print(Student)
        resp.body = (json.dumps(student, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()