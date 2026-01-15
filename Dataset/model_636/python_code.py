from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lib_Address:

    def __init__(self, postalCode: str, lib_Address: "lib_Library" = None):
        self.postalCode = postalCode
        self.lib_Address = lib_Address
        
    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def lib_Address(self):
        return self.__lib_Address

    @lib_Address.setter
    def lib_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Address__lib_Address", None)
        self.__lib_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Library2"):
                opp_val = getattr(old_value, "lib_Library2", None)
                if opp_val == self:
                    setattr(old_value, "lib_Library2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Library2"):
                opp_val = getattr(value, "lib_Library2", None)
                setattr(value, "lib_Library2", self)

class lib_Book:

    def __init__(self, title: str, lib_Book: "lib_Library" = None):
        self.title = title
        self.lib_Book = lib_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lib_Book(self):
        return self.__lib_Book

    @lib_Book.setter
    def lib_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Book__lib_Book", None)
        self.__lib_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Library"):
                opp_val = getattr(old_value, "lib_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Library"):
                opp_val = getattr(value, "lib_Library", None)
                if opp_val is None:
                    setattr(value, "lib_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lib_Library:

    def __init__(self, name: str, library: set["lib_Person"] = None, library5: "lib_Cafeteria" = None, lib_Library: set["lib_Book"] = None, lib_Library2: "lib_Address" = None, Library8: "lib_Cafeteria" = None, Library: "lib_Person" = None):
        self.name = name
        self.library = library if library is not None else set()
        self.library5 = library5
        self.lib_Library = lib_Library if lib_Library is not None else set()
        self.lib_Library2 = lib_Library2
        self.Library8 = Library8
        self.Library = Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library8(self):
        return self.__Library8

    @Library8.setter
    def Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__Library8", None)
        self.__Library8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cafeteria"):
                opp_val = getattr(old_value, "cafeteria", None)
                if opp_val == self:
                    setattr(old_value, "cafeteria", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cafeteria"):
                opp_val = getattr(value, "cafeteria", None)
                setattr(value, "cafeteria", self)

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if opp_val == self:
                    setattr(old_value, "writers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                setattr(value, "writers", self)

    @property
    def library5(self):
        return self.__library5

    @library5.setter
    def library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__library5", None)
        self.__library5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cafeteria"):
                opp_val = getattr(old_value, "Cafeteria", None)
                if opp_val == self:
                    setattr(old_value, "Cafeteria", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cafeteria"):
                opp_val = getattr(value, "Cafeteria", None)
                setattr(value, "Cafeteria", self)

    @property
    def lib_Library(self):
        return self.__lib_Library

    @lib_Library.setter
    def lib_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__lib_Library", None)
        self.__lib_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lib_Book"):
                    opp_val = getattr(item, "lib_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "lib_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lib_Book"):
                    opp_val = getattr(item, "lib_Book", None)
                    
                    setattr(item, "lib_Book", self)
                    

    @property
    def lib_Library2(self):
        return self.__lib_Library2

    @lib_Library2.setter
    def lib_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__lib_Library2", None)
        self.__lib_Library2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Address"):
                opp_val = getattr(old_value, "lib_Address", None)
                if opp_val == self:
                    setattr(old_value, "lib_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Address"):
                opp_val = getattr(value, "lib_Address", None)
                setattr(value, "lib_Address", self)

class lib_Cafeteria:

    def __init__(self, name: str, Cafeteria: "lib_Library" = None, cafeteria: "lib_Library" = None):
        self.name = name
        self.Cafeteria = Cafeteria
        self.cafeteria = cafeteria
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Cafeteria(self):
        return self.__Cafeteria

    @Cafeteria.setter
    def Cafeteria(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Cafeteria__Cafeteria", None)
        self.__Cafeteria = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library5"):
                opp_val = getattr(old_value, "library5", None)
                if opp_val == self:
                    setattr(old_value, "library5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library5"):
                opp_val = getattr(value, "library5", None)
                setattr(value, "library5", self)

    @property
    def cafeteria(self):
        return self.__cafeteria

    @cafeteria.setter
    def cafeteria(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Cafeteria__cafeteria", None)
        self.__cafeteria = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library8"):
                opp_val = getattr(old_value, "Library8", None)
                if opp_val == self:
                    setattr(old_value, "Library8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library8"):
                opp_val = getattr(value, "Library8", None)
                setattr(value, "Library8", self)

class lib_Person:

    def __init__(self, name: str, Person: "lib_Library" = None, writers: "lib_Library" = None):
        self.name = name
        self.Person = Person
        self.writers = writers
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library"):
                opp_val = getattr(old_value, "library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library"):
                opp_val = getattr(value, "library", None)
                if opp_val is None:
                    setattr(value, "library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Person__writers", None)
        self.__writers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)
