from sqlalchemy import Column, Integer, Text
from app.models.baseModel import BaseModel

class Student(BaseModel):
	__tablename__ = 'students'
	id         = Column(Integer, primary_key=True, autoincrement=True)
	name       = Column(Text)
	code       = Column(Text)
