from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Image:

    pass
class library_Text:

    pass
class library_Content:

    pass
class library_Book:

    def __init__(self, name: str, library_Book2: set["library_Chapter"] = None, library_Book: "library_Library" = None):
        self.name = name
        self.library_Book2 = library_Book2 if library_Book2 is not None else set()
        self.library_Book = library_Book
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Book2(self):
        return self.__library_Book2

    @library_Book2.setter
    def library_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book2", None)
        self.__library_Book2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Chapter"):
                    opp_val = getattr(item, "library_Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Chapter"):
                    opp_val = getattr(item, "library_Chapter", None)
                    
                    setattr(item, "library_Chapter", self)
                    

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
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Book"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    setattr(item, "library_Book", self)
                    

class library_Chapter:

    def __init__(self, name: str, pages: int, library_Chapter: "library_Book" = None, library_Chapter4: "library_Content" = None):
        self.name = name
        self.pages = pages
        self.library_Chapter = library_Chapter
        self.library_Chapter4 = library_Chapter4
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Chapter4(self):
        return self.__library_Chapter4

    @library_Chapter4.setter
    def library_Chapter4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Chapter__library_Chapter4", None)
        self.__library_Chapter4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Content"):
                opp_val = getattr(old_value, "library_Content", None)
                if opp_val == self:
                    setattr(old_value, "library_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Content"):
                opp_val = getattr(value, "library_Content", None)
                setattr(value, "library_Content", self)

    @property
    def library_Chapter(self):
        return self.__library_Chapter

    @library_Chapter.setter
    def library_Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Chapter__library_Chapter", None)
        self.__library_Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book2"):
                opp_val = getattr(old_value, "library_Book2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book2"):
                opp_val = getattr(value, "library_Book2", None)
                if opp_val is None:
                    setattr(value, "library_Book2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
