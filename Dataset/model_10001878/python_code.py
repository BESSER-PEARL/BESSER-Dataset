from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Library_Staff_Actor:

    pass


class Faculty_Actor:

    pass


class Student_Actor:

    pass


class Patron_Actor:

    pass





class Check_In_Item_external:

    pass


class Faculty:

    pass


class Student:

    pass


class Patron:

    def __init__(self, isMember: bool):
        self.isMember = isMember
        
        pass
    @property
    def isMember(self):
        return self.__isMember
    @isMember.setter
    def isMember(self, isMember: bool):
        self.__isMember = isMember



class Library_Management_Component:

    pass


class Manage_Computer_Terminals_external:

    pass


class Extended_Checkout_external:

    pass


class Order_New_Resources_external:

    pass


class Renew_Magazine_Subscriptions_external:

    pass


class Organize_Books_external:

    pass


class Manage_Reference_Materials_external:

    pass


class Reserve_Book_For_Semester_external:

    pass


class Check_Out_Item_external:

    pass


class Request_Book_external:

    pass
