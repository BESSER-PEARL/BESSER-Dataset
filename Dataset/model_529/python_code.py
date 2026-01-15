from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class household_Member:

    def __init__(self, name: str, household_Member3: "household_Family" = None, household_Member6: "household_Family" = None, household_Member: "household_Family" = None, household_Member9: "household_Family" = None):
        self.name = name
        self.household_Member3 = household_Member3
        self.household_Member6 = household_Member6
        self.household_Member = household_Member
        self.household_Member9 = household_Member9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def household_Member(self):
        return self.__household_Member

    @household_Member.setter
    def household_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member", None)
        self.__household_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family"):
                opp_val = getattr(old_value, "household_Family", None)
                if opp_val == self:
                    setattr(old_value, "household_Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family"):
                opp_val = getattr(value, "household_Family", None)
                setattr(value, "household_Family", self)

    @property
    def household_Member6(self):
        return self.__household_Member6

    @household_Member6.setter
    def household_Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member6", None)
        self.__household_Member6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family5"):
                opp_val = getattr(old_value, "household_Family5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family5"):
                opp_val = getattr(value, "household_Family5", None)
                if opp_val is None:
                    setattr(value, "household_Family5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def household_Member9(self):
        return self.__household_Member9

    @household_Member9.setter
    def household_Member9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member9", None)
        self.__household_Member9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family8"):
                opp_val = getattr(old_value, "household_Family8", None)
                if opp_val == self:
                    setattr(old_value, "household_Family8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family8"):
                opp_val = getattr(value, "household_Family8", None)
                setattr(value, "household_Family8", self)

    @property
    def household_Member3(self):
        return self.__household_Member3

    @household_Member3.setter
    def household_Member3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member3", None)
        self.__household_Member3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family2"):
                opp_val = getattr(old_value, "household_Family2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family2"):
                opp_val = getattr(value, "household_Family2", None)
                if opp_val is None:
                    setattr(value, "household_Family2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class household_Family:

    def __init__(self, name: str, household_Family2: set["household_Member"] = None, household_Family5: set["household_Member"] = None, household_Family: "household_Member" = None, household_Family8: "household_Member" = None):
        self.name = name
        self.household_Family2 = household_Family2 if household_Family2 is not None else set()
        self.household_Family5 = household_Family5 if household_Family5 is not None else set()
        self.household_Family = household_Family
        self.household_Family8 = household_Family8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def household_Family2(self):
        return self.__household_Family2

    @household_Family2.setter
    def household_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family2", None)
        self.__household_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "household_Member3"):
                    opp_val = getattr(item, "household_Member3", None)
                    
                    if opp_val == self:
                        setattr(item, "household_Member3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "household_Member3"):
                    opp_val = getattr(item, "household_Member3", None)
                    
                    setattr(item, "household_Member3", self)
                    

    @property
    def household_Family(self):
        return self.__household_Family

    @household_Family.setter
    def household_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family", None)
        self.__household_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Member"):
                opp_val = getattr(old_value, "household_Member", None)
                if opp_val == self:
                    setattr(old_value, "household_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Member"):
                opp_val = getattr(value, "household_Member", None)
                setattr(value, "household_Member", self)

    @property
    def household_Family5(self):
        return self.__household_Family5

    @household_Family5.setter
    def household_Family5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family5", None)
        self.__household_Family5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "household_Member6"):
                    opp_val = getattr(item, "household_Member6", None)
                    
                    if opp_val == self:
                        setattr(item, "household_Member6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "household_Member6"):
                    opp_val = getattr(item, "household_Member6", None)
                    
                    setattr(item, "household_Member6", self)
                    

    @property
    def household_Family8(self):
        return self.__household_Family8

    @household_Family8.setter
    def household_Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family8", None)
        self.__household_Family8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Member9"):
                opp_val = getattr(old_value, "household_Member9", None)
                if opp_val == self:
                    setattr(old_value, "household_Member9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Member9"):
                opp_val = getattr(value, "household_Member9", None)
                setattr(value, "household_Member9", self)
