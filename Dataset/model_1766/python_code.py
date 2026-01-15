from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Mystery = "Mystery"
    ScienceFiction = "ScienceFiction"
    Biography = "Biography"
    IT = "IT"


############################################
# Definition of Classes
############################################

class elements_EObject:

    pass
class Person:

    pass
class elements_Writer(Person):

    pass
class elements_Book:

    def __init__(self, title: str, pages: str, category: str, uuid: str, elements_Book: "elements_EObject" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.uuid = uuid
        self.elements_Book = elements_Book
        
    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def elements_Book(self):
        return self.__elements_Book

    @elements_Book.setter
    def elements_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_elements_Book__elements_Book", None)
        self.__elements_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements_EObject"):
                opp_val = getattr(old_value, "elements_EObject", None)
                if opp_val == self:
                    setattr(old_value, "elements_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements_EObject"):
                opp_val = getattr(value, "elements_EObject", None)
                setattr(value, "elements_EObject", self)
