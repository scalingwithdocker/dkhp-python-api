import falcon
middleware=[]
api = falcon.API(middleware=middleware)

api.add_route('/meta', MetaResource())