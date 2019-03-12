from models.basemodel import BaseModel
# from app.models import courses
# from app.models import student_course_resgitry
from models import course, registration, student, classes

__all__ = [
    BaseModel,
    classes,
    student,
    registration,
    course

]