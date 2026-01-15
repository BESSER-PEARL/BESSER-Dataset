from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Fiction:

    def __init__(self, Name: str, library_Fiction9: set["library_Book"] = None, library_Fiction: "library_Library" = None):
        self.Name = Name
        self.library_Fiction9 = library_Fiction9 if library_Fiction9 is not None else set()
        self.library_Fiction = library_Fiction
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def library_Fiction9(self):
        return self.__library_Fiction9

    @library_Fiction9.setter
    def library_Fiction9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Fiction__library_Fiction9", None)
        self.__library_Fiction9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book10"):
                    opp_val = getattr(item, "library_Book10", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book10"):
                    opp_val = getattr(item, "library_Book10", None)
                    
                    setattr(item, "library_Book10", self)
                    

    @property
    def library_Fiction(self):
        return self.__library_Fiction

    @library_Fiction.setter
    def library_Fiction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Fiction__library_Fiction", None)
        self.__library_Fiction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library7"):
                opp_val = getattr(old_value, "library_Library7", None)
                if opp_val == self:
                    setattr(old_value, "library_Library7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library7"):
                opp_val = getattr(value, "library_Library7", None)
                setattr(value, "library_Library7", self)

class library_NonFiction:

    def __init__(self, Name: str, library_NonFiction5: "library_Library" = None, library_NonFiction: set["library_Book"] = None):
        self.Name = Name
        self.library_NonFiction5 = library_NonFiction5
        self.library_NonFiction = library_NonFiction if library_NonFiction is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def library_NonFiction5(self):
        return self.__library_NonFiction5

    @library_NonFiction5.setter
    def library_NonFiction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NonFiction__library_NonFiction5", None)
        self.__library_NonFiction5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library4"):
                opp_val = getattr(old_value, "library_Library4", None)
                if opp_val == self:
                    setattr(old_value, "library_Library4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library4"):
                opp_val = getattr(value, "library_Library4", None)
                setattr(value, "library_Library4", self)

    @property
    def library_NonFiction(self):
        return self.__library_NonFiction

    @library_NonFiction.setter
    def library_NonFiction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NonFiction__library_NonFiction", None)
        self.__library_NonFiction = value if value is not None else set()
        
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
                    

class library_Library:

    def __init__(self, Name: str, library_Library: set["library_Book"] = None, library_Library4: "library_NonFiction" = None, library_Library7: "library_Fiction" = None):
        self.Name = Name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library4 = library_Library4
        self.library_Library7 = library_Library7
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def library_Library4(self):
        return self.__library_Library4

    @library_Library4.setter
    def library_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library4", None)
        self.__library_Library4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NonFiction5"):
                opp_val = getattr(old_value, "library_NonFiction5", None)
                if opp_val == self:
                    setattr(old_value, "library_NonFiction5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NonFiction5"):
                opp_val = getattr(value, "library_NonFiction5", None)
                setattr(value, "library_NonFiction5", self)

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
                if hasattr(item, "library_Book2"):
                    opp_val = getattr(item, "library_Book2", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book2"):
                    opp_val = getattr(item, "library_Book2", None)
                    
                    setattr(item, "library_Book2", self)
                    

    @property
    def library_Library7(self):
        return self.__library_Library7

    @library_Library7.setter
    def library_Library7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library7", None)
        self.__library_Library7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Fiction"):
                opp_val = getattr(old_value, "library_Fiction", None)
                if opp_val == self:
                    setattr(old_value, "library_Fiction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Fiction"):
                opp_val = getattr(value, "library_Fiction", None)
                setattr(value, "library_Fiction", self)

class library_Book:

    def __init__(self, Name: str, genre: str, library_Book2: "library_Library" = None, library_Book: "library_NonFiction" = None, library_Book10: "library_Fiction" = None):
        self.Name = Name
        self.genre = genre
        self.library_Book2 = library_Book2
        self.library_Book = library_Book
        self.library_Book10 = library_Book10
        
    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
            if hasattr(old_value, "library_NonFiction"):
                opp_val = getattr(old_value, "library_NonFiction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NonFiction"):
                opp_val = getattr(value, "library_NonFiction", None)
                if opp_val is None:
                    setattr(value, "library_NonFiction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book10(self):
        return self.__library_Book10

    @library_Book10.setter
    def library_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book10", None)
        self.__library_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Fiction9"):
                opp_val = getattr(old_value, "library_Fiction9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Fiction9"):
                opp_val = getattr(value, "library_Fiction9", None)
                if opp_val is None:
                    setattr(value, "library_Fiction9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
