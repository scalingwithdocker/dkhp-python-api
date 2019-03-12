import falcon
import falcon_jsonify
import json
import requests
from models.course import Course
from services import BaseResource
from falcon.util.uri import encode as uri_encode

class CourseColletionService(BaseResource):
    def on_get(self, req, resp):
        dbsession =self.db.session
        courses = dbsession.query(Course)\
            .order_by(Course.id.desc())\
            .all()

        courses = [dict(
            id=row.id,
            name=row.name,
            code=row.code,
            number_of=row.number_of,
            startDate=row.startDate.strftime('%Y-%m-%d')
        ) for row in courses]
        # resp.json = courses
        resp.body = (json.dumps(courses, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')

        print(result_json['name'])
        new_course = Course(
            name=result_json['name'],
            code=result_json['code'],
            number_of = result_json['number_of'],
            startDate = result_json['startDate']
        )

        dbsession = self.db.session
        dbsession.add(new_course)
        dbsession.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result_json, ensure_ascii=False)
        dbsession.close()

class CourseSingleService(BaseResource):
    def on_get(self, req, resp, id):

        dbsession = self.db.session
        course = dbsession.query(Course).filter(Course.id == id).first()
        if course is None:
            raise falcon.HTTPNotFound()
            resp.status = falcon.HTTP_404
        course =dict(
            id=course.id,
            name=course.name,
            code=course.code,
            number_of=course.number_of,
            startDate=course.startDate.strftime('%Y-%m-%d')
        )
        # print(course)
        resp.body = (json.dumps(course, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_put(self, req, resp, id):
        dbsession=self.db.session
        course = dbsession.query(Course).filter(Course.id == id).first()
        if course is None:
            raise falcon.HTTPNotFound
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')
        course.name = result_json['name']
        course.code = result_json['code']
        course.number_of = result_json['number_of']
        course.startDate = result_json['startDate']
        if len(dbsession.dirty) > 0:
            dbsession.commit()
        course = dict(
            id=course.id,
            name=course.name,
            code=course.code,
            number_of=course.number_of,
            startDate=course.startDate.strftime('%Y-%m-%d')
        )
        # print(course)
        resp.body = (json.dumps(course, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()