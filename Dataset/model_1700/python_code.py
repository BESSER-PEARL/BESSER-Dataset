from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Writer:

    def __init__(self, name: str, library_Writer: "library_Library" = None, library_Writer5: "library_Book" = None):
        self.name = name
        self.library_Writer = library_Writer
        self.library_Writer5 = library_Writer5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Writer5(self):
        return self.__library_Writer5

    @library_Writer5.setter
    def library_Writer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer5", None)
        self.__library_Writer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book4"):
                opp_val = getattr(old_value, "library_Book4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book4"):
                opp_val = getattr(value, "library_Book4", None)
                if opp_val is None:
                    setattr(value, "library_Book4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class library_Book:

    def __init__(self, title: str, library_Book: "library_Library" = None, library_Book4: set["library_Writer"] = None, library_Book8: "library_Book" = None, library_Book6: set["library_Book"] = None):
        self.title = title
        self.library_Book = library_Book
        self.library_Book4 = library_Book4 if library_Book4 is not None else set()
        self.library_Book8 = library_Book8
        self.library_Book6 = library_Book6 if library_Book6 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Book4(self):
        return self.__library_Book4

    @library_Book4.setter
    def library_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book4", None)
        self.__library_Book4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Writer5"):
                    opp_val = getattr(item, "library_Writer5", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer5"):
                    opp_val = getattr(item, "library_Writer5", None)
                    
                    setattr(item, "library_Writer5", self)
                    

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
            if hasattr(old_value, "library_Book6"):
                opp_val = getattr(old_value, "library_Book6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book6"):
                opp_val = getattr(value, "library_Book6", None)
                if opp_val is None:
                    setattr(value, "library_Book6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book6(self):
        return self.__library_Book6

    @library_Book6.setter
    def library_Book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book6", None)
        self.__library_Book6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book8"):
                    opp_val = getattr(item, "library_Book8", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book8"):
                    opp_val = getattr(item, "library_Book8", None)
                    
                    setattr(item, "library_Book8", self)
                    

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

    pass