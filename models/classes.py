from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel

class Class(BaseModel):
	__tablename__ = 'classes'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	code = Column(String, unique=True)


	def __init__(self, name, code,):
		self.name = name
		self.code = code

