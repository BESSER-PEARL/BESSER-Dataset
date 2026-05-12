from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class delete_record_UseCase:

    pass


class Student_Actor:

    pass


class Password_UseCase:

    pass


class Name_UseCase:

    pass


class registered_UseCase:

    pass


class check_details_UseCase:

    pass


class Admin_Actor:

    pass


class Logout_UseCase:

    pass


class update_record_UseCase:

    pass


class generate_report_UseCase:

    pass


class insert_record_UseCase:

    pass


class Login_UseCase:

    pass





class Employee:

    def __init__(self, attribute: str, attribute2: str, attribute3: str, attribute31: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute31 = attribute31
        
        pass
    @property
    def attribute31(self):
        return self.__attribute31
    @attribute31.setter
    def attribute31(self, attribute31: str):
        self.__attribute31 = attribute31

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Admin:

    def __init__(self, username: Admin, password: Admin_Actor):
        self.username = username
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: Admin_Actor):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: Admin):
        self.__username = username



class Login_UseCase1:

    pass
