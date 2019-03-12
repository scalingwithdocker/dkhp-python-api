import falcon
import falcon_jsonify

from services.courseService import *
from models.database import DBManager
from services.classService import *
dbm = DBManager()

api = falcon.API()

api.add_route('/courses', CourseColletionService(dbm))
api.add_route('/courses/{id:int}', CourseSingleService(dbm))

api.add_route('/class', ClassColletionService(dbm))
api.add_route('/class/{id:int}', ClassSingleService(dbm))

