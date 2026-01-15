from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Library_Book:

    def __init__(self, name: str, Library_Book: "Library_Library" = None):
        self.name = name
        self.Library_Book = Library_Book
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library_Book(self):
        return self.__Library_Book

    @Library_Book.setter
    def Library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Library_Book", None)
        self.__Library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library"):
                opp_val = getattr(old_value, "Library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library"):
                opp_val = getattr(value, "Library_Library", None)
                if opp_val is None:
                    setattr(value, "Library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Library_Library:

    pass