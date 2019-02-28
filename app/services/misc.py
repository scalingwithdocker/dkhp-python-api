import json
def to_json(argv):
	return json.dumps(argv)

def make_response(resp, dict_data):
	import falcon
	resp.status = falcon.HTTP_OK
	resp.body = to_json(dict_data)
