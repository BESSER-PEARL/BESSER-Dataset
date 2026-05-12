from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class news:

    def __init__(self, author: str, dlnews: str):
        self.author = author
        self.dlnews = dlnews
        
        pass
    @property
    def dlnews(self):
        return self.__dlnews
    @dlnews.setter
    def dlnews(self, dlnews: str):
        self.__dlnews = dlnews

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author



class Quiz:

    def __init__(self, title: str, moduleName: str, questions__: str):
        self.title = title
        self.moduleName = moduleName
        self.questions__ = questions__
        
        pass
    @property
    def questions__(self):
        return self.__questions__
    @questions__.setter
    def questions__(self, questions__: str):
        self.__questions__ = questions__

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def moduleName(self):
        return self.__moduleName
    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName



class Task:

    pass


class Mark:

    def __init__(self, id: Student, Mark: int):
        self.id = id
        self.Mark = Mark
        
        pass
    @property
    def Mark(self):
        return self.__Mark
    @Mark.setter
    def Mark(self, Mark: int):
        self.__Mark = Mark

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: Student):
        self.__id = id



class Department:

    def __init__(self, id: int, name: str, teachers__: int, modules__: str):
        self.id = id
        self.name = name
        self.teachers__ = teachers__
        self.modules__ = modules__
        
        pass
    @property
    def modules__(self):
        return self.__modules__
    @modules__.setter
    def modules__(self, modules__: str):
        self.__modules__ = modules__

    @property
    def teachers__(self):
        return self.__teachers__
    @teachers__.setter
    def teachers__(self, teachers__: int):
        self.__teachers__ = teachers__

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



class Student:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        
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
    def id(self, id: int):
        self.__id = id



class teacher:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
        pass
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



class user:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
        pass
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

