import falcon
from app.api.v0.meta_resource import MetaResource

middleware=[]
api = falcon.API(middleware=middleware)

api.add_route('/meta', MetaResource())
