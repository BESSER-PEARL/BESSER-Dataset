from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Search:

    pass
class library_ByAuthor(Search):

    pass
class library_ByYear(Search):

    def __init__(self, year: str):
        self.year = year
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class library_Author:

    def __init__(self, firstname: str, secondname: str, library_Author: "library_AddAuthor" = None, library_Author3: "library_ByAuthor" = None, library_Author5: "library_Add" = None):
        self.firstname = firstname
        self.secondname = secondname
        self.library_Author = library_Author
        self.library_Author3 = library_Author3
        self.library_Author5 = library_Author5
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def secondname(self) -> str:
        return self.__secondname

    @secondname.setter
    def secondname(self, secondname: str):
        self.__secondname = secondname

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
            if hasattr(old_value, "library_AddAuthor"):
                opp_val = getattr(old_value, "library_AddAuthor", None)
                if opp_val == self:
                    setattr(old_value, "library_AddAuthor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_AddAuthor"):
                opp_val = getattr(value, "library_AddAuthor", None)
                setattr(value, "library_AddAuthor", self)

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
            if hasattr(old_value, "library_Add"):
                opp_val = getattr(old_value, "library_Add", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Add"):
                opp_val = getattr(value, "library_Add", None)
                if opp_val is None:
                    setattr(value, "library_Add", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "library_ByAuthor"):
                opp_val = getattr(old_value, "library_ByAuthor", None)
                if opp_val == self:
                    setattr(old_value, "library_ByAuthor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ByAuthor"):
                opp_val = getattr(value, "library_ByAuthor", None)
                setattr(value, "library_ByAuthor", self)

class Command:

    pass
class library_Return(Command):

    def __init__(self, isbn: str, firstname: str, secondname: str):
        self.isbn = isbn
        self.firstname = firstname
        self.secondname = secondname
        
    @property
    def secondname(self) -> str:
        return self.__secondname

    @secondname.setter
    def secondname(self, secondname: str):
        self.__secondname = secondname

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

class library_Lend(Command):

    def __init__(self, isbn: str, firstname: str, secondname: str):
        self.isbn = isbn
        self.firstname = firstname
        self.secondname = secondname
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def secondname(self) -> str:
        return self.__secondname

    @secondname.setter
    def secondname(self, secondname: str):
        self.__secondname = secondname

class library_AddUser(Command):

    def __init__(self, firstname: str, secondname: str, age: str):
        self.firstname = firstname
        self.secondname = secondname
        self.age = age
        
    @property
    def secondname(self) -> str:
        return self.__secondname

    @secondname.setter
    def secondname(self, secondname: str):
        self.__secondname = secondname

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

class library_Show(Command):

    def __init__(self, what: str):
        self.what = what
        
    @property
    def what(self) -> str:
        return self.__what

    @what.setter
    def what(self, what: str):
        self.__what = what

class library_Add(Command):

    def __init__(self, isbn: str, title: str, year: str, library_Add: set["library_Author"] = None):
        self.isbn = isbn
        self.title = title
        self.year = year
        self.library_Add = library_Add if library_Add is not None else set()
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Add(self):
        return self.__library_Add

    @library_Add.setter
    def library_Add(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Add__library_Add", None)
        self.__library_Add = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Author5"):
                    opp_val = getattr(item, "library_Author5", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Author5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Author5"):
                    opp_val = getattr(item, "library_Author5", None)
                    
                    setattr(item, "library_Author5", self)
                    

class library_AddAuthor(Command):

    def __init__(self, isbn: str, library_AddAuthor: "library_Author" = None):
        self.isbn = isbn
        self.library_AddAuthor = library_AddAuthor
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def library_AddAuthor(self):
        return self.__library_AddAuthor

    @library_AddAuthor.setter
    def library_AddAuthor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_AddAuthor__library_AddAuthor", None)
        self.__library_AddAuthor = value
        
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

class library_Check(Command):

    def __init__(self, isbn: str):
        self.isbn = isbn
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

class library_Remove(Command):

    def __init__(self, isbn: str):
        self.isbn = isbn
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

class library_Search(Command):

    pass
class library_ShowUserAccount(Command):

    def __init__(self, firstname: str, secondname: str):
        self.firstname = firstname
        self.secondname = secondname
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def secondname(self) -> str:
        return self.__secondname

    @secondname.setter
    def secondname(self, secondname: str):
        self.__secondname = secondname

class library_Command:

    pass
class library_Model:

    pass