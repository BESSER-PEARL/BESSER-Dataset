from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tutorial_Member:

    def __init__(self, name: str, 12: "tutorial_Library" = None, 5: "tutorial_Library" = None, tutorial_Member24: "tutorial_Loan" = None, tutorial_Member: set["tutorial_Loan"] = None, tutorial_Member17: set["tutorial_Book"] = None):
        self.name = name
        self.12 = 12
        self.5 = 5
        self.tutorial_Member24 = tutorial_Member24
        self.tutorial_Member = tutorial_Member if tutorial_Member is not None else set()
        self.tutorial_Member17 = tutorial_Member17 if tutorial_Member17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tutorial_Member17(self):
        return self.__tutorial_Member17

    @tutorial_Member17.setter
    def tutorial_Member17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member17", None)
        self.__tutorial_Member17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tutorial_Book18"):
                    opp_val = getattr(item, "tutorial_Book18", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Book18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Book18"):
                    opp_val = getattr(item, "tutorial_Book18", None)
                    
                    setattr(item, "tutorial_Book18", self)
                    

    @property
    def tutorial_Member24(self):
        return self.__tutorial_Member24

    @tutorial_Member24.setter
    def tutorial_Member24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__tutorial_Member24", None)
        self.__tutorial_Member24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan23"):
                opp_val = getattr(old_value, "tutorial_Loan23", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan23"):
                opp_val = getattr(value, "tutorial_Loan23", None)
                setattr(value, "tutorial_Loan23", self)

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Member__5", None)
        self.__5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "4"):
                opp_val = getattr(old_value, "4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "4"):
                opp_val = getattr(value, "4", None)
                if opp_val is None:
                    setattr(value, "4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "tutorial_Loan15"):
                    opp_val = getattr(item, "tutorial_Loan15", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Loan15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Loan15"):
                    opp_val = getattr(item, "tutorial_Loan15", None)
                    
                    setattr(item, "tutorial_Loan15", self)
                    

class tutorial_Loan:

    def __init__(self, date: date, tutorial_Loan10: "tutorial_Book" = None, tutorial_Loan: "tutorial_Library" = None, tutorial_Loan23: "tutorial_Member" = None, tutorial_Loan15: "tutorial_Member" = None, tutorial_Loan20: "tutorial_Book" = None):
        self.date = date
        self.tutorial_Loan10 = tutorial_Loan10
        self.tutorial_Loan = tutorial_Loan
        self.tutorial_Loan23 = tutorial_Loan23
        self.tutorial_Loan15 = tutorial_Loan15
        self.tutorial_Loan20 = tutorial_Loan20
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def tutorial_Loan23(self):
        return self.__tutorial_Loan23

    @tutorial_Loan23.setter
    def tutorial_Loan23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan23", None)
        self.__tutorial_Loan23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Member24"):
                opp_val = getattr(old_value, "tutorial_Member24", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Member24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Member24"):
                opp_val = getattr(value, "tutorial_Member24", None)
                setattr(value, "tutorial_Member24", self)

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

    @property
    def tutorial_Loan20(self):
        return self.__tutorial_Loan20

    @tutorial_Loan20.setter
    def tutorial_Loan20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan20", None)
        self.__tutorial_Loan20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Book21"):
                opp_val = getattr(old_value, "tutorial_Book21", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Book21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Book21"):
                opp_val = getattr(value, "tutorial_Book21", None)
                setattr(value, "tutorial_Book21", self)

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
    def tutorial_Loan10(self):
        return self.__tutorial_Loan10

    @tutorial_Loan10.setter
    def tutorial_Loan10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Loan__tutorial_Loan10", None)
        self.__tutorial_Loan10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Book"):
                opp_val = getattr(old_value, "tutorial_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Book"):
                opp_val = getattr(value, "tutorial_Book", None)
                if opp_val is None:
                    setattr(value, "tutorial_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tutorial_Book:

    def __init__(self, name: str, copies: str, 7: "tutorial_Library" = None, tutorial_Book: set["tutorial_Loan"] = None, 1: "tutorial_Library" = None, tutorial_Book18: "tutorial_Member" = None, tutorial_Book21: "tutorial_Loan" = None):
        self.name = name
        self.copies = copies
        self.7 = 7
        self.tutorial_Book = tutorial_Book if tutorial_Book is not None else set()
        self.1 = 1
        self.tutorial_Book18 = tutorial_Book18
        self.tutorial_Book21 = tutorial_Book21
        
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
    def tutorial_Book18(self):
        return self.__tutorial_Book18

    @tutorial_Book18.setter
    def tutorial_Book18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book18", None)
        self.__tutorial_Book18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Member17"):
                opp_val = getattr(old_value, "tutorial_Member17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Member17"):
                opp_val = getattr(value, "tutorial_Member17", None)
                if opp_val is None:
                    setattr(value, "tutorial_Member17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tutorial_Book21(self):
        return self.__tutorial_Book21

    @tutorial_Book21.setter
    def tutorial_Book21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__tutorial_Book21", None)
        self.__tutorial_Book21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutorial_Loan20"):
                opp_val = getattr(old_value, "tutorial_Loan20", None)
                if opp_val == self:
                    setattr(old_value, "tutorial_Loan20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutorial_Loan20"):
                opp_val = getattr(value, "tutorial_Loan20", None)
                setattr(value, "tutorial_Loan20", self)

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
                if hasattr(item, "tutorial_Loan10"):
                    opp_val = getattr(item, "tutorial_Loan10", None)
                    
                    if opp_val == self:
                        setattr(item, "tutorial_Loan10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tutorial_Loan10"):
                    opp_val = getattr(item, "tutorial_Loan10", None)
                    
                    setattr(item, "tutorial_Loan10", self)
                    

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Book__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "8"):
                opp_val = getattr(old_value, "8", None)
                if opp_val == self:
                    setattr(old_value, "8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "8"):
                opp_val = getattr(value, "8", None)
                setattr(value, "8", self)

    def isAvailable(self):
        # TODO: Implement isAvailable method
        pass

class tutorial_Library:

    def __init__(self, name: bool, 8: "tutorial_Book" = None, 13: "tutorial_Member" = None, : set["tutorial_Book"] = None, tutorial_Library: set["tutorial_Loan"] = None, 4: set["tutorial_Member"] = None):
        self.name = name
        self.8 = 8
        self.13 = 13
        self. =  if  is not None else set()
        self.tutorial_Library = tutorial_Library if tutorial_Library is not None else set()
        self.4 = 4 if 4 is not None else set()
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if opp_val == self:
                    setattr(old_value, "12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                setattr(value, "12", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__4", None)
        self.__4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "5"):
                    opp_val = getattr(item, "5", None)
                    
                    if opp_val == self:
                        setattr(item, "5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "5"):
                    opp_val = getattr(item, "5", None)
                    
                    setattr(item, "5", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tutorial_Library__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

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
                    
