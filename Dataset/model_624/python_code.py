from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm2_Loan:

    def __init__(self, name: str, mm2_Loan: "mm2_Library" = None, loans: "mm2_Book" = None, loans7: "mm2_Member" = None, Loan: "mm2_Member" = None, Loan10: "mm2_Book" = None):
        self.name = name
        self.mm2_Loan = mm2_Loan
        self.loans = loans
        self.loans7 = loans7
        self.Loan = Loan
        self.Loan10 = Loan10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Loan10(self):
        return self.__Loan10

    @Loan10.setter
    def Loan10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Loan__Loan10", None)
        self.__Loan10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def loans(self):
        return self.__loans

    @loans.setter
    def loans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Loan__loans", None)
        self.__loans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book"):
                opp_val = getattr(old_value, "Book", None)
                if opp_val == self:
                    setattr(old_value, "Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book"):
                opp_val = getattr(value, "Book", None)
                setattr(value, "Book", self)

    @property
    def loans7(self):
        return self.__loans7

    @loans7.setter
    def loans7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Loan__loans7", None)
        self.__loans7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member"):
                opp_val = getattr(old_value, "Member", None)
                if opp_val == self:
                    setattr(old_value, "Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member"):
                opp_val = getattr(value, "Member", None)
                setattr(value, "Member", self)

    @property
    def mm2_Loan(self):
        return self.__mm2_Loan

    @mm2_Loan.setter
    def mm2_Loan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Loan__mm2_Loan", None)
        self.__mm2_Loan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library4"):
                opp_val = getattr(old_value, "mm2_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library4"):
                opp_val = getattr(value, "mm2_Library4", None)
                if opp_val is None:
                    setattr(value, "mm2_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Loan(self):
        return self.__Loan

    @Loan.setter
    def Loan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Loan__Loan", None)
        self.__Loan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "member"):
                opp_val = getattr(old_value, "member", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "member"):
                opp_val = getattr(value, "member", None)
                if opp_val is None:
                    setattr(value, "member", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm2_Member:

    def __init__(self, name: str, mm2_Member: "mm2_Library" = None, Member: "mm2_Loan" = None, member: set["mm2_Loan"] = None):
        self.name = name
        self.mm2_Member = mm2_Member
        self.Member = Member
        self.member = member if member is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loans7"):
                opp_val = getattr(old_value, "loans7", None)
                if opp_val == self:
                    setattr(old_value, "loans7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loans7"):
                opp_val = getattr(value, "loans7", None)
                setattr(value, "loans7", self)

    @property
    def member(self):
        return self.__member

    @member.setter
    def member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__member", None)
        self.__member = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Loan"):
                    opp_val = getattr(item, "Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Loan"):
                    opp_val = getattr(item, "Loan", None)
                    
                    setattr(item, "Loan", self)
                    

    @property
    def mm2_Member(self):
        return self.__mm2_Member

    @mm2_Member.setter
    def mm2_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__mm2_Member", None)
        self.__mm2_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library"):
                opp_val = getattr(old_value, "mm2_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library"):
                opp_val = getattr(value, "mm2_Library", None)
                if opp_val is None:
                    setattr(value, "mm2_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm2_Library:

    def __init__(self, name: str, mm2_Library: set["mm2_Member"] = None, mm2_Library2: set["mm2_Book"] = None, mm2_Library4: set["mm2_Loan"] = None):
        self.name = name
        self.mm2_Library = mm2_Library if mm2_Library is not None else set()
        self.mm2_Library2 = mm2_Library2 if mm2_Library2 is not None else set()
        self.mm2_Library4 = mm2_Library4 if mm2_Library4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Library(self):
        return self.__mm2_Library

    @mm2_Library.setter
    def mm2_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library", None)
        self.__mm2_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Member"):
                    opp_val = getattr(item, "mm2_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Member"):
                    opp_val = getattr(item, "mm2_Member", None)
                    
                    setattr(item, "mm2_Member", self)
                    

    @property
    def mm2_Library2(self):
        return self.__mm2_Library2

    @mm2_Library2.setter
    def mm2_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library2", None)
        self.__mm2_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Book"):
                    opp_val = getattr(item, "mm2_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Book"):
                    opp_val = getattr(item, "mm2_Book", None)
                    
                    setattr(item, "mm2_Book", self)
                    

    @property
    def mm2_Library4(self):
        return self.__mm2_Library4

    @mm2_Library4.setter
    def mm2_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library4", None)
        self.__mm2_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Loan"):
                    opp_val = getattr(item, "mm2_Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Loan"):
                    opp_val = getattr(item, "mm2_Loan", None)
                    
                    setattr(item, "mm2_Loan", self)
                    

class mm2_Book:

    def __init__(self, name: str, mm2_Book: "mm2_Library" = None, Book: "mm2_Loan" = None, book: set["mm2_Loan"] = None):
        self.name = name
        self.mm2_Book = mm2_Book
        self.Book = Book
        self.book = book if book is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loans"):
                opp_val = getattr(old_value, "loans", None)
                if opp_val == self:
                    setattr(old_value, "loans", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loans"):
                opp_val = getattr(value, "loans", None)
                setattr(value, "loans", self)

    @property
    def mm2_Book(self):
        return self.__mm2_Book

    @mm2_Book.setter
    def mm2_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Book__mm2_Book", None)
        self.__mm2_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library2"):
                opp_val = getattr(old_value, "mm2_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library2"):
                opp_val = getattr(value, "mm2_Library2", None)
                if opp_val is None:
                    setattr(value, "mm2_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Loan10"):
                    opp_val = getattr(item, "Loan10", None)
                    
                    if opp_val == self:
                        setattr(item, "Loan10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Loan10"):
                    opp_val = getattr(item, "Loan10", None)
                    
                    setattr(item, "Loan10", self)
                    
