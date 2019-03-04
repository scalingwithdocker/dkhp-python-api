from sqlalchemy import Column, Integer, Text, ForeignKey


class Student_Course_Resgitry():
    __tablename__ = 'student_course_resgitry'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    student_code       = Column(Text,  ForeignKey('student.code'))
    class_code         = Column(Text, ForeignKey('class.code'))

