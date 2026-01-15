from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Household_Member:

    def __init__(self, firstName: str, Household_Member: "Household_Family" = None, Household_Member5: "Household_Family" = None, Household_Member8: "Household_Family" = None, Household_Member11: "Household_Family" = None):
        self.firstName = firstName
        self.Household_Member = Household_Member
        self.Household_Member5 = Household_Member5
        self.Household_Member8 = Household_Member8
        self.Household_Member11 = Household_Member11
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Household_Member8(self):
        return self.__Household_Member8

    @Household_Member8.setter
    def Household_Member8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Member__Household_Member8", None)
        self.__Household_Member8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Family7"):
                opp_val = getattr(old_value, "Household_Family7", None)
                if opp_val == self:
                    setattr(old_value, "Household_Family7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Family7"):
                opp_val = getattr(value, "Household_Family7", None)
                setattr(value, "Household_Family7", self)

    @property
    def Household_Member(self):
        return self.__Household_Member

    @Household_Member.setter
    def Household_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Member__Household_Member", None)
        self.__Household_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Family2"):
                opp_val = getattr(old_value, "Household_Family2", None)
                if opp_val == self:
                    setattr(old_value, "Household_Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Family2"):
                opp_val = getattr(value, "Household_Family2", None)
                setattr(value, "Household_Family2", self)

    @property
    def Household_Member5(self):
        return self.__Household_Member5

    @Household_Member5.setter
    def Household_Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Member__Household_Member5", None)
        self.__Household_Member5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Family4"):
                opp_val = getattr(old_value, "Household_Family4", None)
                if opp_val == self:
                    setattr(old_value, "Household_Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Family4"):
                opp_val = getattr(value, "Household_Family4", None)
                setattr(value, "Household_Family4", self)

    @property
    def Household_Member11(self):
        return self.__Household_Member11

    @Household_Member11.setter
    def Household_Member11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Member__Household_Member11", None)
        self.__Household_Member11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Family10"):
                opp_val = getattr(old_value, "Household_Family10", None)
                if opp_val == self:
                    setattr(old_value, "Household_Family10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Family10"):
                opp_val = getattr(value, "Household_Family10", None)
                setattr(value, "Household_Family10", self)

class Household_Family:

    def __init__(self, lastName: str, Household_Family: "Household_HouseholdRoot" = None, Household_Family2: "Household_Member" = None, Household_Family7: "Household_Member" = None, Household_Family10: "Household_Member" = None, Household_Family4: "Household_Member" = None):
        self.lastName = lastName
        self.Household_Family = Household_Family
        self.Household_Family2 = Household_Family2
        self.Household_Family7 = Household_Family7
        self.Household_Family10 = Household_Family10
        self.Household_Family4 = Household_Family4
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Household_Family4(self):
        return self.__Household_Family4

    @Household_Family4.setter
    def Household_Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Family__Household_Family4", None)
        self.__Household_Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Member5"):
                opp_val = getattr(old_value, "Household_Member5", None)
                if opp_val == self:
                    setattr(old_value, "Household_Member5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Member5"):
                opp_val = getattr(value, "Household_Member5", None)
                setattr(value, "Household_Member5", self)

    @property
    def Household_Family7(self):
        return self.__Household_Family7

    @Household_Family7.setter
    def Household_Family7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Family__Household_Family7", None)
        self.__Household_Family7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Member8"):
                opp_val = getattr(old_value, "Household_Member8", None)
                if opp_val == self:
                    setattr(old_value, "Household_Member8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Member8"):
                opp_val = getattr(value, "Household_Member8", None)
                setattr(value, "Household_Member8", self)

    @property
    def Household_Family2(self):
        return self.__Household_Family2

    @Household_Family2.setter
    def Household_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Family__Household_Family2", None)
        self.__Household_Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Member"):
                opp_val = getattr(old_value, "Household_Member", None)
                if opp_val == self:
                    setattr(old_value, "Household_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Member"):
                opp_val = getattr(value, "Household_Member", None)
                setattr(value, "Household_Member", self)

    @property
    def Household_Family10(self):
        return self.__Household_Family10

    @Household_Family10.setter
    def Household_Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Family__Household_Family10", None)
        self.__Household_Family10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_Member11"):
                opp_val = getattr(old_value, "Household_Member11", None)
                if opp_val == self:
                    setattr(old_value, "Household_Member11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_Member11"):
                opp_val = getattr(value, "Household_Member11", None)
                setattr(value, "Household_Member11", self)

    @property
    def Household_Family(self):
        return self.__Household_Family

    @Household_Family.setter
    def Household_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Household_Family__Household_Family", None)
        self.__Household_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Household_HouseholdRoot"):
                opp_val = getattr(old_value, "Household_HouseholdRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Household_HouseholdRoot"):
                opp_val = getattr(value, "Household_HouseholdRoot", None)
                if opp_val is None:
                    setattr(value, "Household_HouseholdRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Household_HouseholdRoot:

    pass