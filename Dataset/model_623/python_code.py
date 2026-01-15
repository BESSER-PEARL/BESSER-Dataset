from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ocltutorial_Book:

    def __init__(self, name: str, copies: str, Book: "ocltutorial_Library" = None, books: "ocltutorial_Library" = None, ocltutorial_Book: "ocltutorial_Loans" = None):
        self.name = name
        self.copies = copies
        self.Book = Book
        self.books = books
        self.ocltutorial_Book = ocltutorial_Book
        
    @property
    def copies(self) -> str:
        return self.__copies

    @copies.setter
    def copies(self, copies: str):
        self.__copies = copies

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocltutorial_Book(self):
        return self.__ocltutorial_Book

    @ocltutorial_Book.setter
    def ocltutorial_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Book__ocltutorial_Book", None)
        self.__ocltutorial_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltutorial_Loans8"):
                opp_val = getattr(old_value, "ocltutorial_Loans8", None)
                if opp_val == self:
                    setattr(old_value, "ocltutorial_Loans8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltutorial_Loans8"):
                opp_val = getattr(value, "ocltutorial_Loans8", None)
                setattr(value, "ocltutorial_Loans8", self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Book__books", None)
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
        old_value = getattr(self, f"_ocltutorial_Book__Book", None)
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

class ocltutorial_Library:

    pass
class ocltutorial_Loans:

    def __init__(self, date: date, ocltutorial_Loans: "ocltutorial_Library" = None, ocltutorial_Loans6: "ocltutorial_Member" = None, ocltutorial_Loans8: "ocltutorial_Book" = None):
        self.date = date
        self.ocltutorial_Loans = ocltutorial_Loans
        self.ocltutorial_Loans6 = ocltutorial_Loans6
        self.ocltutorial_Loans8 = ocltutorial_Loans8
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def ocltutorial_Loans(self):
        return self.__ocltutorial_Loans

    @ocltutorial_Loans.setter
    def ocltutorial_Loans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Loans__ocltutorial_Loans", None)
        self.__ocltutorial_Loans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltutorial_Library"):
                opp_val = getattr(old_value, "ocltutorial_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltutorial_Library"):
                opp_val = getattr(value, "ocltutorial_Library", None)
                if opp_val is None:
                    setattr(value, "ocltutorial_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocltutorial_Loans6(self):
        return self.__ocltutorial_Loans6

    @ocltutorial_Loans6.setter
    def ocltutorial_Loans6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Loans__ocltutorial_Loans6", None)
        self.__ocltutorial_Loans6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltutorial_Member"):
                opp_val = getattr(old_value, "ocltutorial_Member", None)
                if opp_val == self:
                    setattr(old_value, "ocltutorial_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltutorial_Member"):
                opp_val = getattr(value, "ocltutorial_Member", None)
                setattr(value, "ocltutorial_Member", self)

    @property
    def ocltutorial_Loans8(self):
        return self.__ocltutorial_Loans8

    @ocltutorial_Loans8.setter
    def ocltutorial_Loans8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Loans__ocltutorial_Loans8", None)
        self.__ocltutorial_Loans8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltutorial_Book"):
                opp_val = getattr(old_value, "ocltutorial_Book", None)
                if opp_val == self:
                    setattr(old_value, "ocltutorial_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltutorial_Book"):
                opp_val = getattr(value, "ocltutorial_Book", None)
                setattr(value, "ocltutorial_Book", self)

class ocltutorial_Member:

    def __init__(self, name: str, Member: "ocltutorial_Library" = None, ocltutorial_Member: "ocltutorial_Loans" = None, members: "ocltutorial_Library" = None):
        self.name = name
        self.Member = Member
        self.ocltutorial_Member = ocltutorial_Member
        self.members = members
        
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
        old_value = getattr(self, f"_ocltutorial_Member__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library10"):
                opp_val = getattr(old_value, "Library10", None)
                if opp_val == self:
                    setattr(old_value, "Library10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library10"):
                opp_val = getattr(value, "Library10", None)
                setattr(value, "Library10", self)

    @property
    def ocltutorial_Member(self):
        return self.__ocltutorial_Member

    @ocltutorial_Member.setter
    def ocltutorial_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Member__ocltutorial_Member", None)
        self.__ocltutorial_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocltutorial_Loans6"):
                opp_val = getattr(old_value, "ocltutorial_Loans6", None)
                if opp_val == self:
                    setattr(old_value, "ocltutorial_Loans6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocltutorial_Loans6"):
                opp_val = getattr(value, "ocltutorial_Loans6", None)
                setattr(value, "ocltutorial_Loans6", self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocltutorial_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library2"):
                opp_val = getattr(old_value, "library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library2"):
                opp_val = getattr(value, "library2", None)
                if opp_val is None:
                    setattr(value, "library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
