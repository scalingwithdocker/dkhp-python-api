import falcon
import falcon_jsonify
import json
import requests
from models.registration import Registration
from services import BaseResource
from falcon.util.uri import encode as uri_encode

class RegistrationColletionService(BaseResource):
    def on_get(self, req, resp):
        dbsession =self.db.session
        registration = dbsession.query(Registration)\
            .order_by(Registration.id.desc())\
            .all()

        registration = [dict(
            id=row.id,
            student_code=row.student_code,
            course_code=row.course_code,
            deltete=row.delete
        ) for row in registration]

        resp.body = (json.dumps(registration, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')

        # print(result_json['name'])
        new_registration = Registration(
            student_code=result_json['student_code'],
            course_code=result_json['course_code'],
            delete=result_json['delete']
        )

        dbsession = self.db.session
        dbsession.add(new_registration)
        dbsession.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result_json, ensure_ascii=False)
        dbsession.close()

class RegistrationSingleService(BaseResource):
    def on_get(self, req, resp, id):

        dbsession = self.db.session
        registration = dbsession.query(Registration).filter(Registration.id == id).first()
        if registration is None:
            raise falcon.HTTPNotFound()
            resp.status = falcon.HTTP_404
        registration =dict(
            student_code=registration.student_code,
            course_code=registration.course_code,
            delete=registration.delete
        )
        # print(course)
        resp.body = (json.dumps(registration, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_put(self, req, resp, id):
        dbsession=self.db.session
        registration = dbsession.query(Registration).filter(Registration.id == id).first()
        if registration is None:
            raise falcon.HTTPNotFound
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')

        registration.student_code = result_json['student_code']
        registration.course_code = result_json['course_code']
        registration.delete = result_json['delete']

        if len(dbsession.dirty) > 0:
            dbsession.commit()
        registration = dict(
            student_code=registration.student_code,
            course_code=registration.course_code,
            delete=registration.delete
        )
        # print(course)
        resp.body = (json.dumps(registration, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()