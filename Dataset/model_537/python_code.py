from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class household_Member:

    def __init__(self, name: str, household_Member: "household_Family" = None, household_Member5: "household_Family" = None, household_Member8: "household_Family" = None, household_Member11: "household_Family" = None):
        self.name = name
        self.household_Member = household_Member
        self.household_Member5 = household_Member5
        self.household_Member8 = household_Member8
        self.household_Member11 = household_Member11
        
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
            if hasattr(old_value, "household_Family2"):
                opp_val = getattr(old_value, "household_Family2", None)
                if opp_val == self:
                    setattr(old_value, "household_Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family2"):
                opp_val = getattr(value, "household_Family2", None)
                setattr(value, "household_Family2", self)

    @property
    def household_Member5(self):
        return self.__household_Member5

    @household_Member5.setter
    def household_Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member5", None)
        self.__household_Member5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family4"):
                opp_val = getattr(old_value, "household_Family4", None)
                if opp_val == self:
                    setattr(old_value, "household_Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family4"):
                opp_val = getattr(value, "household_Family4", None)
                setattr(value, "household_Family4", self)

    @property
    def household_Member8(self):
        return self.__household_Member8

    @household_Member8.setter
    def household_Member8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member8", None)
        self.__household_Member8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family7"):
                opp_val = getattr(old_value, "household_Family7", None)
                if opp_val == self:
                    setattr(old_value, "household_Family7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family7"):
                opp_val = getattr(value, "household_Family7", None)
                setattr(value, "household_Family7", self)

    @property
    def household_Member11(self):
        return self.__household_Member11

    @household_Member11.setter
    def household_Member11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Member__household_Member11", None)
        self.__household_Member11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Family10"):
                opp_val = getattr(old_value, "household_Family10", None)
                if opp_val == self:
                    setattr(old_value, "household_Family10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Family10"):
                opp_val = getattr(value, "household_Family10", None)
                setattr(value, "household_Family10", self)

class household_Family:

    def __init__(self, name: str, household_Family: "household_HouseholdRoot" = None, household_Family2: "household_Member" = None, household_Family4: "household_Member" = None, household_Family7: "household_Member" = None, household_Family10: "household_Member" = None):
        self.name = name
        self.household_Family = household_Family
        self.household_Family2 = household_Family2
        self.household_Family4 = household_Family4
        self.household_Family7 = household_Family7
        self.household_Family10 = household_Family10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def household_Family10(self):
        return self.__household_Family10

    @household_Family10.setter
    def household_Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family10", None)
        self.__household_Family10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Member11"):
                opp_val = getattr(old_value, "household_Member11", None)
                if opp_val == self:
                    setattr(old_value, "household_Member11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Member11"):
                opp_val = getattr(value, "household_Member11", None)
                setattr(value, "household_Member11", self)

    @property
    def household_Family7(self):
        return self.__household_Family7

    @household_Family7.setter
    def household_Family7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family7", None)
        self.__household_Family7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Member8"):
                opp_val = getattr(old_value, "household_Member8", None)
                if opp_val == self:
                    setattr(old_value, "household_Member8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Member8"):
                opp_val = getattr(value, "household_Member8", None)
                setattr(value, "household_Member8", self)

    @property
    def household_Family4(self):
        return self.__household_Family4

    @household_Family4.setter
    def household_Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family4", None)
        self.__household_Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "household_Member5"):
                opp_val = getattr(old_value, "household_Member5", None)
                if opp_val == self:
                    setattr(old_value, "household_Member5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_Member5"):
                opp_val = getattr(value, "household_Member5", None)
                setattr(value, "household_Member5", self)

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
            if hasattr(old_value, "household_HouseholdRoot"):
                opp_val = getattr(old_value, "household_HouseholdRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "household_HouseholdRoot"):
                opp_val = getattr(value, "household_HouseholdRoot", None)
                if opp_val is None:
                    setattr(value, "household_HouseholdRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def household_Family2(self):
        return self.__household_Family2

    @household_Family2.setter
    def household_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_household_Family__household_Family2", None)
        self.__household_Family2 = value
        
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

class household_HouseholdRoot:

    pass