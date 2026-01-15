from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class E(Enum):
    A = "A"
    B = "B"
    C = "C"


############################################
# Definition of Classes
############################################

class imported_model_Library:

    pass
class imported_model_Book:

    def __init__(self, pages: int, imported_model_Book: "imported_model_Library" = None):
        self.pages = pages
        self.imported_model_Book = imported_model_Book
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def imported_model_Book(self):
        return self.__imported_model_Book

    @imported_model_Book.setter
    def imported_model_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imported_model_Book__imported_model_Book", None)
        self.__imported_model_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imported_model_Library"):
                opp_val = getattr(old_value, "imported_model_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imported_model_Library"):
                opp_val = getattr(value, "imported_model_Library", None)
                if opp_val is None:
                    setattr(value, "imported_model_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
