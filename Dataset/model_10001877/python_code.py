from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Checked_Out_UseCase:

    pass


class Checked_In_UseCase:

    pass


class Acquired_UseCase:

    pass


class Retired_UseCase:

    pass


class Book_Actor:

    pass


class Retirement_of_Books_UseCase:

    pass


class Acquisition_of_Books_UseCase:

    pass


class Mail_2_Week_Reminders_UseCase:

    pass


class Check_In_Book_UseCase:

    pass


class Check_Out_Book_UseCase:

    pass


class Reserve_Book_UseCase:

    pass


class Librarian_Actor:

    pass


class Patron_Actor:

    pass





class Library:

    def __init__(self, id: int, librarian_id: int, librarian20: "Librarian" = None, patron26: set["Patron"] = None):
        self.id = id
        self.librarian_id = librarian_id
        self.librarian20 = librarian20
        self.patron26 = patron26 if patron26 is not None else set()
        
        pass
    @property
    def librarian_id(self):
        return self.__librarian_id
    @librarian_id.setter
    def librarian_id(self, librarian_id: int):
        self.__librarian_id = librarian_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def patron26(self):
        return self.__patron26
    @patron26.setter
    def patron26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__patron26", None)
        self.__patron26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library27"):
                    opp_val = getattr(item, "library27", None)
                    
                    if opp_val == self:
                        setattr(item, "library27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library27"):
                    opp_val = getattr(item, "library27", None)
                    
                    setattr(item, "library27", self)
                    

    @property
    def librarian20(self):
        return self.__librarian20
    @librarian20.setter
    def librarian20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__librarian20", None)
        self.__librarian20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library21"):
                opp_val = getattr(old_value, "library21", None)
                if opp_val == self:
                    setattr(old_value, "library21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library21"):
                opp_val = getattr(value, "library21", None)
                setattr(value, "library21", self)



class Book:

    def __init__(self, id: int, author: str, title: str, status: str, creation_date: str, patron19: "Patron" = None, librarian23: "Librarian" = None):
        self.id = id
        self.author = author
        self.title = title
        self.status = status
        self.creation_date = creation_date
        self.patron19 = patron19
        self.librarian23 = librarian23
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def librarian23(self):
        return self.__librarian23
    @librarian23.setter
    def librarian23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__librarian23", None)
        self.__librarian23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book22"):
                opp_val = getattr(old_value, "book22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book22"):
                opp_val = getattr(value, "book22", None)
                if opp_val is None:
                    setattr(value, "book22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patron19(self):
        return self.__patron19
    @patron19.setter
    def patron19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__patron19", None)
        self.__patron19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book18"):
                opp_val = getattr(old_value, "book18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book18"):
                opp_val = getattr(value, "book18", None)
                if opp_val is None:
                    setattr(value, "book18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Librarian:

    def __init__(self, id: int, name: str, library21: "Library" = None, book22: set["Book"] = None, patron25: set["Patron"] = None):
        self.id = id
        self.name = name
        self.library21 = library21
        self.book22 = book22 if book22 is not None else set()
        self.patron25 = patron25 if patron25 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library21(self):
        return self.__library21
    @library21.setter
    def library21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__library21", None)
        self.__library21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "librarian20"):
                opp_val = getattr(old_value, "librarian20", None)
                if opp_val == self:
                    setattr(old_value, "librarian20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "librarian20"):
                opp_val = getattr(value, "librarian20", None)
                setattr(value, "librarian20", self)

    @property
    def patron25(self):
        return self.__patron25
    @patron25.setter
    def patron25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__patron25", None)
        self.__patron25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian24"):
                    opp_val = getattr(item, "librarian24", None)
                    
                    if opp_val == self:
                        setattr(item, "librarian24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian24"):
                    opp_val = getattr(item, "librarian24", None)
                    
                    setattr(item, "librarian24", self)
                    

    @property
    def book22(self):
        return self.__book22
    @book22.setter
    def book22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__book22", None)
        self.__book22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian23"):
                    opp_val = getattr(item, "librarian23", None)
                    
                    if opp_val == self:
                        setattr(item, "librarian23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian23"):
                    opp_val = getattr(item, "librarian23", None)
                    
                    setattr(item, "librarian23", self)
                    



class Patron:

    def __init__(self, id: int, name: str, status: str, address: str, num_books_checked_out: int, book18: set["Book"] = None, librarian24: "Librarian" = None, library27: "Library" = None):
        self.id = id
        self.name = name
        self.status = status
        self.address = address
        self.num_books_checked_out = num_books_checked_out
        self.book18 = book18 if book18 is not None else set()
        self.librarian24 = librarian24
        self.library27 = library27
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def num_books_checked_out(self):
        return self.__num_books_checked_out
    @num_books_checked_out.setter
    def num_books_checked_out(self, num_books_checked_out: int):
        self.__num_books_checked_out = num_books_checked_out

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def librarian24(self):
        return self.__librarian24
    @librarian24.setter
    def librarian24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__librarian24", None)
        self.__librarian24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron25"):
                opp_val = getattr(old_value, "patron25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron25"):
                opp_val = getattr(value, "patron25", None)
                if opp_val is None:
                    setattr(value, "patron25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def book18(self):
        return self.__book18
    @book18.setter
    def book18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__book18", None)
        self.__book18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron19"):
                    opp_val = getattr(item, "patron19", None)
                    
                    if opp_val == self:
                        setattr(item, "patron19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron19"):
                    opp_val = getattr(item, "patron19", None)
                    
                    setattr(item, "patron19", self)
                    

    @property
    def library27(self):
        return self.__library27
    @library27.setter
    def library27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__library27", None)
        self.__library27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron26"):
                opp_val = getattr(old_value, "patron26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron26"):
                opp_val = getattr(value, "patron26", None)
                if opp_val is None:
                    setattr(value, "patron26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

