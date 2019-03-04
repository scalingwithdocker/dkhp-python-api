from sqlalchemy import Column, Integer,Text

class Class():
	__tablename__ = 'class'
	id         = Column(Integer, primary_key=True, autoincrement=True)
	name       = Column(Text)
	code        = Column(Text)
