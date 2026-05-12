from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Faculty_Actor:

    pass


class Staff_Actor:

    pass


class Patron_Actor:

    pass


class Student_Actor:

    pass





class Fees_for_overdue_books_external:

    pass


class Acquiring_Retiring_Books_external:

    pass


class Periodicals_external:

    pass


class Multimedia_external:

    pass


class Books_external:

    pass


class Reserved_or_reference_books_external:

    pass


class Aid_Patrons_external:

    pass


class Computers_external:

    pass


class StaffMember:

    pass


class MultiMedia:

    pass


class Books:

    def __init__(self, title: str):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title



class Patron:

    pass


class Staff_Actor1:

    pass


class Resources_Component:

    pass
