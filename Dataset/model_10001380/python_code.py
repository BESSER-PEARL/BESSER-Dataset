from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StudyField__(Enum):
    pass
class Student__(Enum):
    pass
class Subjects__(Enum):
    pass
class Teacher__(Enum):
    pass

############################################
# Definition of Classes
############################################










class Subject:

    def __init__(self, name: str, id: int, credits: int, currentId: int):
        self.name = name
        self.id = id
        self.credits = credits
        self.currentId = currentId
        
        pass
    @property
    def credits(self):
        return self.__credits
    @credits.setter
    def credits(self, credits: int):
        self.__credits = credits

    @property
    def currentId(self):
        return self.__currentId
    @currentId.setter
    def currentId(self, currentId: int):
        self.__currentId = currentId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class StudyField:

    def __init__(self, name: str, id: int, subjects: Subjects__, subjectsCount: int, currentId: int):
        self.name = name
        self.id = id
        self.subjects = subjects
        self.subjectsCount = subjectsCount
        self.currentId = currentId
        
        pass
    @property
    def subjectsCount(self):
        return self.__subjectsCount
    @subjectsCount.setter
    def subjectsCount(self, subjectsCount: int):
        self.__subjectsCount = subjectsCount

    @property
    def subjects(self):
        return self.__subjects
    @subjects.setter
    def subjects(self, subjects: Subjects__):
        self.__subjects = subjects

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def currentId(self):
        return self.__currentId
    @currentId.setter
    def currentId(self, currentId: int):
        self.__currentId = currentId



class Headmaster:

    pass


class Exam:

    def __init__(self, name: str, id: str, points: int, subject: Subject, currentId: int):
        self.name = name
        self.id = id
        self.points = points
        self.subject = subject
        self.currentId = currentId
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: Subject):
        self.__subject = subject

    @property
    def currentId(self):
        return self.__currentId
    @currentId.setter
    def currentId(self, currentId: int):
        self.__currentId = currentId

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points



class Teacher:

    pass


class Student:

    pass


class School:

    def __init__(self, students: Student__, studentsCount: int, teachers: Teacher__, teachersCount: int, fields: StudyField__, fieldsCount: int, headmaster: Headmaster, name: int):
        self.students = students
        self.studentsCount = studentsCount
        self.teachers = teachers
        self.teachersCount = teachersCount
        self.fields = fields
        self.fieldsCount = fieldsCount
        self.headmaster = headmaster
        self.name = name
        
        pass
    @property
    def fields(self):
        return self.__fields
    @fields.setter
    def fields(self, fields: StudyField__):
        self.__fields = fields

    @property
    def teachersCount(self):
        return self.__teachersCount
    @teachersCount.setter
    def teachersCount(self, teachersCount: int):
        self.__teachersCount = teachersCount

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def students(self):
        return self.__students
    @students.setter
    def students(self, students: Student__):
        self.__students = students

    @property
    def headmaster(self):
        return self.__headmaster
    @headmaster.setter
    def headmaster(self, headmaster: Headmaster):
        self.__headmaster = headmaster

    @property
    def fieldsCount(self):
        return self.__fieldsCount
    @fieldsCount.setter
    def fieldsCount(self, fieldsCount: int):
        self.__fieldsCount = fieldsCount

    @property
    def studentsCount(self):
        return self.__studentsCount
    @studentsCount.setter
    def studentsCount(self, studentsCount: int):
        self.__studentsCount = studentsCount

    @property
    def teachers(self):
        return self.__teachers
    @teachers.setter
    def teachers(self, teachers: Teacher__):
        self.__teachers = teachers

