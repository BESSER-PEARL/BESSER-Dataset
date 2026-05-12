from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class ArrPrint:

    pass


class Print:

    pass


class Documents:

    def __init__(self, file: str, data: Provider, file_name: str, tab_counter: int):
        self.file = file
        self.data = data
        self.file_name = file_name
        self.tab_counter = tab_counter
        
        pass
    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name = file_name

    @property
    def tab_counter(self):
        return self.__tab_counter
    @tab_counter.setter
    def tab_counter(self, tab_counter: int):
        self.__tab_counter = tab_counter

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: Provider):
        self.__data = data



class Provider:

    def __init__(self, uid: str, providerId: String, email: String, displayName: String, photoURL: String):
        self.uid = uid
        self.providerId = providerId
        self.email = email
        self.displayName = displayName
        self.photoURL = photoURL
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: String):
        self.__email = email

    @property
    def displayName(self):
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName: String):
        self.__displayName = displayName

    @property
    def photoURL(self):
        return self.__photoURL
    @photoURL.setter
    def photoURL(self, photoURL: String):
        self.__photoURL = photoURL

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def providerId(self):
        return self.__providerId
    @providerId.setter
    def providerId(self, providerId: String):
        self.__providerId = providerId



class Visitor:

    pass


class Array:

    def __init__(self, data: User):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: User):
        self.__data = data



class Number:

    def __init__(self, data: int):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: int):
        self.__data = data



class Category:

    def __init__(self, id: str, section: String, name: String, parent: String):
        self.id = id
        self.section = section
        self.name = name
        self.parent = parent
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, parent: String):
        self.__parent = parent

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: String):
        self.__section = section

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: String):
        self.__name = name



class String:

    def __init__(self, data: String):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: String):
        self.__data = data



class Null:

    pass


class User(ABC):

    def __init__(self, id: str, firstName: String, lastName: String, email: String, phone: String, address: Documents, photoURL: String):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address
        self.photoURL = photoURL
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: Documents):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: String):
        self.__phone = phone

    @property
    def photoURL(self):
        return self.__photoURL
    @photoURL.setter
    def photoURL(self, photoURL: String):
        self.__photoURL = photoURL

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: String):
        self.__email = email

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: String):
        self.__lastName = lastName

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: String):
        self.__firstName = firstName

