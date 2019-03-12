import falcon
import falcon_jsonify
import json
import requests
from models.classes import Class
from services import BaseResource
from falcon.util.uri import encode as uri_encode

class ClassColletionService(BaseResource):
    def on_get(self, req, resp):
        dbsession =self.db.session
        classs = dbsession.query(Class)\
            .order_by(Class.id.desc())\
            .all()

        classs = [dict(
            id=row.id,
            name=row.name,
            code=row.code,
        ) for row in classs]
        # resp.json = classs
        resp.body = (json.dumps(classs, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')

        # print(result_json['name'])
        new_class = Class(
            name=result_json['name'],
            code=result_json['code']
        )

        dbsession = self.db.session
        dbsession.add(new_class)
        dbsession.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result_json, ensure_ascii=False)
        dbsession.close()

class ClassSingleService(BaseResource):
    def on_get(self, req, resp, id):
        dbsession = self.db.session
        classs = dbsession.query(Class).filter(Class.id == id).first()
        if classs is None:
            raise falcon.HTTPNotFound()
            resp.status = falcon.HTTP_404
        classs =dict(
            id=classs.id,
            name=classs.name,
            code=classs.code
        )
        # print(Class)
        resp.body = (json.dumps(classs, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()

    def on_put(self, req, resp, id):
        dbsession=self.db.session
        classs = dbsession.query(Class).filter(Class.id == id).first()
        if classs is None:
            raise falcon.HTTPNotFound
        raw_json = req.stream.read()
        result_json = json.loads(raw_json, encoding='utf-8')
        classs.name = result_json['name']
        classs.code = result_json['code']
        if len(dbsession.dirty) > 0:
            dbsession.commit()
        classs = dict(
            id=classs.id,
            name=classs.name,
            code=classs.code,
        )
        # print(Class)
        resp.body = (json.dumps(classs, ensure_ascii=False))
        resp.status = falcon.HTTP_200
        dbsession.close()