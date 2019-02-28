class MetaResource(object):
	def on_get(self, req, resp):
		meke_response(resp,{'toi':'hau'})