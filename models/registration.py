from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel

student_registry = Table(
    'student_registration', BaseModel.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('registration_id', Integer, ForeignKey('registrations.id'))
)

course_registration = Table(
    'course_registration', BaseModel.metadata,
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('registration_id', Integer, ForeignKey('registrations.id'))
)

class Registration(BaseModel):
    __tablename__ = 'registrations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    delete = Column(Boolean)
    student = relationship("Student", secondary=student_registry)
    course = relationship("Course", secondary=course_registration)

    def __init__(self, delete, student):
        self.delete = delete