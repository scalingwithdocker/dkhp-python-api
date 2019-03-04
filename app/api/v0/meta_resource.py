from app.services.misc import make_response


class MetaResource(object):
	def on_get(self, req, resp):
		make_response(resp, {'toi': 'hau'})