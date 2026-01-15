from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tutorial_Book:

    def __init__(self, name: str, copies: str, Book: "tutorial_Library" = None, books: "tutorial_Library" = None, tutorial_Book: "tutorial_Member" = None, tutorial_Book13: "tutorial_Loan" = None):
        self.name = name
        self.copies = copies
        self.Book = Book
        self.books = books
        self.tutorial_Book = tutorial_Book
        self.tutorial_Book13 = tutorial_Book13
        
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
    def tutorial_Book13(self):
        return self.__tutorial_Book13

    @tutorial_Book13.setter
    def tutorial_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book13", None)
        self.__tutorial_Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan12"):
                opp_val = getattr(old_value, "tutorial_Loan12", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan12"):
                opp_val = getattr(value, "tutorial_Loan12", None)
                setattr(value, "tutorial_Loan12", self)

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
    def tutorial_Book(self):
        return self.__tutorial_Book

    @tutorial_Book.setter
    def tutorial_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book", None)
        self.__tutorial_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Member10"):
                opp_val = getattr(old_value, "tutorial_Member10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Member10"):
                opp_val = getattr(value, "tutorial_Member10", None)
                if opp_val is None:
                    setattr(value, "tutorial_Member10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isAvailable(self) -> bool:
        # TODO: Implement isAvailable method
        pass

class tutorial_Member:

    def __init__(self, name: str, Member: "tutorial_Library" = None, members: "tutorial_Library" = None, tutorial_Member10: set["tutorial_Book"] = None, tutorial_Member: set["tutorial_Loan"] = None, tutorial_Member16: "tutorial_Loan" = None):
        self.name = name
        self.Member = Member
        self.members = members
        self.tutorial_Member10 = tutorial_Member10 if tutorial_Member10 is not None else set()
        self.tutorial_Member = tutorial_Member if tutorial_Member is not None else set()
        self.tutorial_Member16 = tutorial_Member16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tutorial_Member16(self):
        return self.__tutorial_Member16

    @tutorial_Member16.setter
    def tutorial_Member16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member16", None)
        self.__tutorial_Member16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan15"):
                opp_val = getattr(old_value, "tutorial_Loan15", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan15"):
                opp_val = getattr(value, "tutorial_Loan15", None)
                setattr(value, "tutorial_Loan15", self)

    @property
    def tutorial_Member10(self):
        return self.__tutorial_Member10

    @tutorial_Member10.setter
    def tutorial_Member10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member10", None)
        self.__tutorial_Member10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tutorial_Book"):
                    opp_val = getattr(item, "tutorial_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Book"):
                    opp_val = getattr(item, "tutorial_Book", None)
                    
                    setattr(item, "tutorial_Book", self)
                    

    @property
    def tutorial_Member(self):
        return self.__tutorial_Member

    @tutorial_Member.setter
    def tutorial_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member", None)
        self.__tutorial_Member = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tutorial_Loan8"):
                    opp_val = getattr(item, "tutorial_Loan8", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Loan8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Loan8"):
                    opp_val = getattr(item, "tutorial_Loan8", None)
                    
                    setattr(item, "tutorial_Loan8", self)
                    

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
            if hasattr(old_value, "Library6"):
                opp_val = getattr(old_value, "Library6", None)
                if opp_val == self:
                    setattr(old_value, "Library6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library6"):
                opp_val = getattr(value, "Library6", None)
                setattr(value, "Library6", self)

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

class tutorial_Loan:

    def __init__(self, date: date, tutorial_Loan: "tutorial_Library" = None, tutorial_Loan12: "tutorial_Book" = None, tutorial_Loan8: "tutorial_Member" = None, tutorial_Loan15: "tutorial_Member" = None):
        self.date = date
        self.tutorial_Loan = tutorial_Loan
        self.tutorial_Loan12 = tutorial_Loan12
        self.tutorial_Loan8 = tutorial_Loan8
        self.tutorial_Loan15 = tutorial_Loan15
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def tutorial_Loan15(self):
        return self.__tutorial_Loan15

    @tutorial_Loan15.setter
    def tutorial_Loan15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan15", None)
        self.__tutorial_Loan15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Member16"):
                opp_val = getattr(old_value, "tutorial_Member16", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Member16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Member16"):
                opp_val = getattr(value, "tutorial_Member16", None)
                setattr(value, "tutorial_Member16", self)

    @property
    def tutorial_Loan12(self):
        return self.__tutorial_Loan12

    @tutorial_Loan12.setter
    def tutorial_Loan12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan12", None)
        self.__tutorial_Loan12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Book13"):
                opp_val = getattr(old_value, "tutorial_Book13", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Book13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Book13"):
                opp_val = getattr(value, "tutorial_Book13", None)
                setattr(value, "tutorial_Book13", self)

    @property
    def tutorial_Loan(self):
        return self.__tutorial_Loan

    @tutorial_Loan.setter
    def tutorial_Loan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan", None)
        self.__tutorial_Loan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Library"):
                opp_val = getattr(old_value, "tutorial_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Library"):
                opp_val = getattr(value, "tutorial_Library", None)
                if opp_val is None:
                    setattr(value, "tutorial_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tutorial_Loan8(self):
        return self.__tutorial_Loan8

    @tutorial_Loan8.setter
    def tutorial_Loan8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan8", None)
        self.__tutorial_Loan8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Member"):
                opp_val = getattr(old_value, "tutorial_Member", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Member"):
                opp_val = getattr(value, "tutorial_Member", None)
                if opp_val is None:
                    setattr(value, "tutorial_Member", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tutorial_Library:

    def __init__(self, name: str, tutorial_Library: set["tutorial_Loan"] = None, library3: set["tutorial_Member"] = None, library: set["tutorial_Book"] = None, Library: "tutorial_Book" = None, Library6: "tutorial_Member" = None):
        self.name = name
        self.tutorial_Library = tutorial_Library if tutorial_Library is not None else set()
        self.library3 = library3 if library3 is not None else set()
        self.library = library if library is not None else set()
        self.Library = Library
        self.Library6 = Library6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Library6(self):
        return self.__Library6

    @Library6.setter
    def Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__Library6", None)
        self.__Library6 = value
        
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
                    
