from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tutorial_Member:

    def __init__(self, name: str, members: "tutorial_Library" = None, Member: "tutorial_Library" = None, tutorial_Member: "tutorial_Loan" = None):
        self.name = name
        self.members = members
        self.Member = Member
        self.tutorial_Member = tutorial_Member
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__members", None)
        self.__members = value
        
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

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3"):
                opp_val = getattr(old_value, "library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3"):
                opp_val = getattr(value, "library3", None)
                if opp_val is None:
                    setattr(value, "library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tutorial_Member(self):
        return self.__tutorial_Member

    @tutorial_Member.setter
    def tutorial_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member", None)
        self.__tutorial_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan13"):
                opp_val = getattr(old_value, "tutorial_Loan13", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan13"):
                opp_val = getattr(value, "tutorial_Loan13", None)
                setattr(value, "tutorial_Loan13", self)

class tutorial_Library:

    def __init__(self, name: str, library: set["tutorial_Book"] = None, tutorial_Library: set["tutorial_Loan"] = None, Library: "tutorial_Book" = None, Library8: "tutorial_Member" = None, library3: set["tutorial_Member"] = None):
        self.name = name
        self.library = library if library is not None else set()
        self.tutorial_Library = tutorial_Library if tutorial_Library is not None else set()
        self.Library = Library
        self.Library8 = Library8
        self.library3 = library3 if library3 is not None else set()
        
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
        old_value = getattr(self, f"_tutorial_Library__Library8", None)
        self.__Library8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

    @property
    def tutorial_Library(self):
        return self.__tutorial_Library

    @tutorial_Library.setter
    def tutorial_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__tutorial_Library", None)
        self.__tutorial_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tutorial_Loan"):
                    opp_val = getattr(item, "tutorial_Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Loan"):
                    opp_val = getattr(item, "tutorial_Loan", None)
                    
                    setattr(item, "tutorial_Loan", self)
                    

    @property
    def library3(self):
        return self.__library3

    @library3.setter
    def library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__library3", None)
        self.__library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if opp_val == self:
                    setattr(old_value, "books", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                setattr(value, "books", self)

class tutorial_Loan:

    pass
class tutorial_Book:

    def __init__(self, name: str, copies: str, Book: "tutorial_Library" = None, books: "tutorial_Library" = None, tutorial_Book: set["tutorial_Loan"] = None, tutorial_Book11: "tutorial_Loan" = None):
        self.name = name
        self.copies = copies
        self.Book = Book
        self.books = books
        self.tutorial_Book = tutorial_Book if tutorial_Book is not None else set()
        self.tutorial_Book11 = tutorial_Book11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def copies(self) -> str:
        return self.__copies

    @copies.setter
    def copies(self, copies: str):
        self.__copies = copies

    @property
    def tutorial_Book(self):
        return self.__tutorial_Book

    @tutorial_Book.setter
    def tutorial_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book", None)
        self.__tutorial_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tutorial_Loan5"):
                    opp_val = getattr(item, "tutorial_Loan5", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Loan5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Loan5"):
                    opp_val = getattr(item, "tutorial_Loan5", None)
                    
                    setattr(item, "tutorial_Loan5", self)
                    

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__books", None)
        self.__books = value
        
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

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__Book", None)
        self.__Book = value
        
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
    def tutorial_Book11(self):
        return self.__tutorial_Book11

    @tutorial_Book11.setter
    def tutorial_Book11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book11", None)
        self.__tutorial_Book11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan10"):
                opp_val = getattr(old_value, "tutorial_Loan10", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan10"):
                opp_val = getattr(value, "tutorial_Loan10", None)
                setattr(value, "tutorial_Loan10", self)

    def isAvailable(self) -> bool:
        # TODO: Implement isAvailable method
        pass
