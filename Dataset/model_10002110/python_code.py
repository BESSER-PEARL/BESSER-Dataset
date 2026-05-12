from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class leftOuts:

    def __init__(self, subject: subjects, classroom: classrooms, teachers: teachers, students: str):
        self.subject = subject
        self.classroom = classroom
        self.teachers = teachers
        self.students = students
        
        pass
    @property
    def teachers(self):
        return self.__teachers
    @teachers.setter
    def teachers(self, teachers: teachers):
        self.__teachers = teachers

    @property
    def students(self):
        return self.__students
    @students.setter
    def students(self, students: str):
        self.__students = students

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: subjects):
        self.__subject = subject

    @property
    def classroom(self):
        return self.__classroom
    @classroom.setter
    def classroom(self, classroom: classrooms):
        self.__classroom = classroom



class constraints:

    def __init__(self, singletons: subjects, doubletons: subjects):
        self.singletons = singletons
        self.doubletons = doubletons
        
        pass
    @property
    def doubletons(self):
        return self.__doubletons
    @doubletons.setter
    def doubletons(self, doubletons: subjects):
        self.__doubletons = doubletons

    @property
    def singletons(self):
        return self.__singletons
    @singletons.setter
    def singletons(self, singletons: subjects):
        self.__singletons = singletons



class conflictCheck:

    def __init__(self, conflict: bool, subjects: str):
        self.conflict = conflict
        self.subjects = subjects
        
        pass
    @property
    def conflict(self):
        return self.__conflict
    @conflict.setter
    def conflict(self, conflict: bool):
        self.__conflict = conflict

    @property
    def subjects(self):
        return self.__subjects
    @subjects.setter
    def subjects(self, subjects: str):
        self.__subjects = subjects



class classrooms:

    def __init__(self, number: int, teacher: str, subject: str):
        self.number = number
        self.teacher = teacher
        self.subject = subject
        
        pass
    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def teacher(self):
        return self.__teacher
    @teacher.setter
    def teacher(self, teacher: str):
        self.__teacher = teacher



class subjects:

    def __init__(self, classroom: int, teacher: str, Section: str, name: str):
        self.classroom = classroom
        self.teacher = teacher
        self.Section = Section
        self.name = name
        
        pass
    @property
    def classroom(self):
        return self.__classroom
    @classroom.setter
    def classroom(self, classroom: int):
        self.__classroom = classroom

    @property
    def teacher(self):
        return self.__teacher
    @teacher.setter
    def teacher(self, teacher: str):
        self.__teacher = teacher

    @property
    def Section(self):
        return self.__Section
    @Section.setter
    def Section(self, Section: str):
        self.__Section = Section

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class teachers:

    def __init__(self, name: str, subject: str, classroom: int, section: str):
        self.name = name
        self.subject = subject
        self.classroom = classroom
        self.section = section
        
        pass
    @property
    def classroom(self):
        return self.__classroom
    @classroom.setter
    def classroom(self, classroom: int):
        self.__classroom = classroom

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

