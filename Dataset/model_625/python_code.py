from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ocldriven_Dependancy:

    pass
class ocldriven_Loans:

    def __init__(self, date: date, ocldriven_Loans: "ocldriven_Library" = None, ocldriven_Loans8: "ocldriven_Member" = None, ocldriven_Loans10: "ocldriven_Media" = None):
        self.date = date
        self.ocldriven_Loans = ocldriven_Loans
        self.ocldriven_Loans8 = ocldriven_Loans8
        self.ocldriven_Loans10 = ocldriven_Loans10
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def ocldriven_Loans10(self):
        return self.__ocldriven_Loans10

    @ocldriven_Loans10.setter
    def ocldriven_Loans10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Loans__ocldriven_Loans10", None)
        self.__ocldriven_Loans10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Media"):
                opp_val = getattr(old_value, "ocldriven_Media", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Media", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Media"):
                opp_val = getattr(value, "ocldriven_Media", None)
                setattr(value, "ocldriven_Media", self)

    @property
    def ocldriven_Loans(self):
        return self.__ocldriven_Loans

    @ocldriven_Loans.setter
    def ocldriven_Loans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Loans__ocldriven_Loans", None)
        self.__ocldriven_Loans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Library"):
                opp_val = getattr(old_value, "ocldriven_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Library"):
                opp_val = getattr(value, "ocldriven_Library", None)
                if opp_val is None:
                    setattr(value, "ocldriven_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ocldriven_Loans8(self):
        return self.__ocldriven_Loans8

    @ocldriven_Loans8.setter
    def ocldriven_Loans8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Loans__ocldriven_Loans8", None)
        self.__ocldriven_Loans8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Member"):
                opp_val = getattr(old_value, "ocldriven_Member", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Member"):
                opp_val = getattr(value, "ocldriven_Member", None)
                setattr(value, "ocldriven_Member", self)

class ocldriven_Member:

    def __init__(self, name: str, Member: "ocldriven_Library" = None, ocldriven_Member: "ocldriven_Loans" = None, members: "ocldriven_Library" = None):
        self.name = name
        self.Member = Member
        self.ocldriven_Member = ocldriven_Member
        self.members = members
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocldriven_Member(self):
        return self.__ocldriven_Member

    @ocldriven_Member.setter
    def ocldriven_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Member__ocldriven_Member", None)
        self.__ocldriven_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Loans8"):
                opp_val = getattr(old_value, "ocldriven_Loans8", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Loans8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Loans8"):
                opp_val = getattr(value, "ocldriven_Loans8", None)
                setattr(value, "ocldriven_Loans8", self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Member__Member", None)
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

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Member__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library12"):
                opp_val = getattr(old_value, "Library12", None)
                if opp_val == self:
                    setattr(old_value, "Library12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library12"):
                opp_val = getattr(value, "Library12", None)
                setattr(value, "Library12", self)

class ocldriven_Media:

    def __init__(self, name: str, copies: str, Media: "ocldriven_Library" = None, medias: "ocldriven_Library" = None, ocldriven_Media: "ocldriven_Loans" = None, ocldriven_Media15: "ocldriven_Dependancy" = None, ocldriven_Media18: "ocldriven_Dependancy" = None):
        self.name = name
        self.copies = copies
        self.Media = Media
        self.medias = medias
        self.ocldriven_Media = ocldriven_Media
        self.ocldriven_Media15 = ocldriven_Media15
        self.ocldriven_Media18 = ocldriven_Media18
        
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
    def medias(self):
        return self.__medias

    @medias.setter
    def medias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Media__medias", None)
        self.__medias = value
        
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
    def Media(self):
        return self.__Media

    @Media.setter
    def Media(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Media__Media", None)
        self.__Media = value
        
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
    def ocldriven_Media(self):
        return self.__ocldriven_Media

    @ocldriven_Media.setter
    def ocldriven_Media(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Media__ocldriven_Media", None)
        self.__ocldriven_Media = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Loans10"):
                opp_val = getattr(old_value, "ocldriven_Loans10", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Loans10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Loans10"):
                opp_val = getattr(value, "ocldriven_Loans10", None)
                setattr(value, "ocldriven_Loans10", self)

    @property
    def ocldriven_Media18(self):
        return self.__ocldriven_Media18

    @ocldriven_Media18.setter
    def ocldriven_Media18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Media__ocldriven_Media18", None)
        self.__ocldriven_Media18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Dependancy17"):
                opp_val = getattr(old_value, "ocldriven_Dependancy17", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Dependancy17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Dependancy17"):
                opp_val = getattr(value, "ocldriven_Dependancy17", None)
                setattr(value, "ocldriven_Dependancy17", self)

    @property
    def ocldriven_Media15(self):
        return self.__ocldriven_Media15

    @ocldriven_Media15.setter
    def ocldriven_Media15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocldriven_Media__ocldriven_Media15", None)
        self.__ocldriven_Media15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocldriven_Dependancy14"):
                opp_val = getattr(old_value, "ocldriven_Dependancy14", None)
                if opp_val == self:
                    setattr(old_value, "ocldriven_Dependancy14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocldriven_Dependancy14"):
                opp_val = getattr(value, "ocldriven_Dependancy14", None)
                setattr(value, "ocldriven_Dependancy14", self)

class ocldriven_Library:

    pass