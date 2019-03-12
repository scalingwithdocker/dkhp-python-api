from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel

class Course(BaseModel):
	__tablename__ = 'courses'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	code = Column(String, unique=True)
	number_of = Column(Integer)
	startDate = Column(Date)
	def __init__(self, name, code, number_of, startDate):
		self.name = name
		self.code = code
		self.number_of = number_of
		self.startDate = startDate