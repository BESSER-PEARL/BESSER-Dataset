from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Writer:

    def __init__(self, firstName: str, lastName: str, library_Writer4: set["library_Book"] = None, library_Writer8: "library_Book" = None, library_Writer: "library_Library" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.library_Writer4 = library_Writer4 if library_Writer4 is not None else set()
        self.library_Writer8 = library_Writer8
        self.library_Writer = library_Writer
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value
        
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

    @property
    def library_Writer8(self):
        return self.__library_Writer8

    @library_Writer8.setter
    def library_Writer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer8", None)
        self.__library_Writer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book7"):
                opp_val = getattr(old_value, "library_Book7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book7"):
                opp_val = getattr(value, "library_Book7", None)
                if opp_val is None:
                    setattr(value, "library_Book7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Writer4(self):
        return self.__library_Writer4

    @library_Writer4.setter
    def library_Writer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer4", None)
        self.__library_Writer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book5"):
                    opp_val = getattr(item, "library_Book5", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book5"):
                    opp_val = getattr(item, "library_Book5", None)
                    
                    setattr(item, "library_Book5", self)
                    

class library_Library:

    def __init__(self, name: str, library_Library2: set["library_Book"] = None, library_Library: set["library_Writer"] = None):
        self.name = name
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library2(self):
        return self.__library_Library2

    @library_Library2.setter
    def library_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library2", None)
        self.__library_Library2 = value if value is not None else set()
        
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
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    setattr(item, "library_Writer", self)
                    

class library_Book:

    def __init__(self, title: str, pages: int, library_Book: "library_Library" = None, library_Book5: "library_Writer" = None, library_Book7: set["library_Writer"] = None):
        self.title = title
        self.pages = pages
        self.library_Book = library_Book
        self.library_Book5 = library_Book5
        self.library_Book7 = library_Book7 if library_Book7 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

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
            if hasattr(old_value, "library_Library2"):
                opp_val = getattr(old_value, "library_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library2"):
                opp_val = getattr(value, "library_Library2", None)
                if opp_val is None:
                    setattr(value, "library_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book7(self):
        return self.__library_Book7

    @library_Book7.setter
    def library_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book7", None)
        self.__library_Book7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Writer8"):
                    opp_val = getattr(item, "library_Writer8", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer8"):
                    opp_val = getattr(item, "library_Writer8", None)
                    
                    setattr(item, "library_Writer8", self)
                    

    @property
    def library_Book5(self):
        return self.__library_Book5

    @library_Book5.setter
    def library_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book5", None)
        self.__library_Book5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer4"):
                opp_val = getattr(old_value, "library_Writer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer4"):
                opp_val = getattr(value, "library_Writer4", None)
                if opp_val is None:
                    setattr(value, "library_Writer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
