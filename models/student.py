from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel


class Student(BaseModel):
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	code = Column(String, unique=True)
	class_code = Column(String, ForeignKey('classes.code'))
	classs = relationship("Class", backref="students")


	def __init__(self, name, code, classs):
		self.name = name
		self.code = code
		self.classs = classs
