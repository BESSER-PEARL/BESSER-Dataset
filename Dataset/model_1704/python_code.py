from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Library_Book:

    def __init__(self, title: str, pages: int, Library_Book: "Library_Writer" = None):
        self.title = title
        self.pages = pages
        self.Library_Book = Library_Book
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
            if hasattr(old_value, "Library_Writer"):
                opp_val = getattr(old_value, "Library_Writer", None)
                if opp_val == self:
                    setattr(old_value, "Library_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Writer"):
                opp_val = getattr(value, "Library_Writer", None)
                setattr(value, "Library_Writer", self)

class Library_Writer:

    def __init__(self, name: str, Library_Writer: "Library_Book" = None):
        self.name = name
        self.Library_Writer = Library_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library_Writer(self):
        return self.__Library_Writer

    @Library_Writer.setter
    def Library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Library_Writer", None)
        self.__Library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Book"):
                opp_val = getattr(old_value, "Library_Book", None)
                if opp_val == self:
                    setattr(old_value, "Library_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Book"):
                opp_val = getattr(value, "Library_Book", None)
                setattr(value, "Library_Book", self)
