from sqlalchemy import Column, Integer. Text

class Course():
	__tablename__ = 'course'
	 id         = Column(Integer, primary_key=True, autoincrement=True)
	 name       = Column(Text)
	code        = Column(Text)
