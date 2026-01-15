from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Library:

    pass
class library_Book:

    def __init__(self, title: str, library_Book: "library_Author" = None, library_Book2: "library_Author" = None, library_Book8: "library_Library" = None):
        self.title = title
        self.library_Book = library_Book
        self.library_Book2 = library_Book2
        self.library_Book8 = library_Book8
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Author"):
                opp_val = getattr(old_value, "library_Author", None)
                if opp_val == self:
                    setattr(old_value, "library_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Author"):
                opp_val = getattr(value, "library_Author", None)
                setattr(value, "library_Author", self)

    @property
    def library_Book2(self):
        return self.__library_Book2

    @library_Book2.setter
    def library_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book2", None)
        self.__library_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Author3"):
                opp_val = getattr(old_value, "library_Author3", None)
                if opp_val == self:
                    setattr(old_value, "library_Author3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Author3"):
                opp_val = getattr(value, "library_Author3", None)
                setattr(value, "library_Author3", self)

    @property
    def library_Book8(self):
        return self.__library_Book8

    @library_Book8.setter
    def library_Book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book8", None)
        self.__library_Book8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library7"):
                opp_val = getattr(old_value, "library_Library7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library7"):
                opp_val = getattr(value, "library_Library7", None)
                if opp_val is None:
                    setattr(value, "library_Library7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Author:

    def __init__(self, name: str, surname: str, library_Author: "library_Book" = None, library_Author3: "library_Book" = None, library_Author5: "library_Library" = None):
        self.name = name
        self.surname = surname
        self.library_Author = library_Author
        self.library_Author3 = library_Author3
        self.library_Author5 = library_Author5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def library_Author3(self):
        return self.__library_Author3

    @library_Author3.setter
    def library_Author3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Author__library_Author3", None)
        self.__library_Author3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book2"):
                opp_val = getattr(old_value, "library_Book2", None)
                if opp_val == self:
                    setattr(old_value, "library_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book2"):
                opp_val = getattr(value, "library_Book2", None)
                setattr(value, "library_Book2", self)

    @property
    def library_Author5(self):
        return self.__library_Author5

    @library_Author5.setter
    def library_Author5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Author__library_Author5", None)
        self.__library_Author5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if opp_val == self:
                    setattr(old_value, "library_Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                setattr(value, "library_Library", self)

    @property
    def library_Author(self):
        return self.__library_Author

    @library_Author.setter
    def library_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Author__library_Author", None)
        self.__library_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book"):
                opp_val = getattr(old_value, "library_Book", None)
                if opp_val == self:
                    setattr(old_value, "library_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book"):
                opp_val = getattr(value, "library_Book", None)
                setattr(value, "library_Book", self)
