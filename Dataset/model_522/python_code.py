from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Families_Member:

    def __init__(self, firstName: str, Families_Member: "Families_Family" = None, Families_Member3: "Families_Family" = None, Families_Member6: "Families_Family" = None, Families_Member9: "Families_Family" = None):
        self.firstName = firstName
        self.Families_Member = Families_Member
        self.Families_Member3 = Families_Member3
        self.Families_Member6 = Families_Member6
        self.Families_Member9 = Families_Member9
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Families_Member6(self):
        return self.__Families_Member6

    @Families_Member6.setter
    def Families_Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member6", None)
        self.__Families_Member6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family5"):
                opp_val = getattr(old_value, "Families_Family5", None)
                if opp_val == self:
                    setattr(old_value, "Families_Family5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family5"):
                opp_val = getattr(value, "Families_Family5", None)
                setattr(value, "Families_Family5", self)

    @property
    def Families_Member9(self):
        return self.__Families_Member9

    @Families_Member9.setter
    def Families_Member9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member9", None)
        self.__Families_Member9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family8"):
                opp_val = getattr(old_value, "Families_Family8", None)
                if opp_val == self:
                    setattr(old_value, "Families_Family8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family8"):
                opp_val = getattr(value, "Families_Family8", None)
                setattr(value, "Families_Family8", self)

    @property
    def Families_Member3(self):
        return self.__Families_Member3

    @Families_Member3.setter
    def Families_Member3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member3", None)
        self.__Families_Member3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family2"):
                opp_val = getattr(old_value, "Families_Family2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family2"):
                opp_val = getattr(value, "Families_Family2", None)
                if opp_val is None:
                    setattr(value, "Families_Family2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Families_Member(self):
        return self.__Families_Member

    @Families_Member.setter
    def Families_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member", None)
        self.__Families_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family"):
                opp_val = getattr(old_value, "Families_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family"):
                opp_val = getattr(value, "Families_Family", None)
                if opp_val is None:
                    setattr(value, "Families_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Families_Family:

    def __init__(self, lastName: str, Families_Family: set["Families_Member"] = None, Families_Family2: set["Families_Member"] = None, Families_Family5: "Families_Member" = None, Families_Family8: "Families_Member" = None):
        self.lastName = lastName
        self.Families_Family = Families_Family if Families_Family is not None else set()
        self.Families_Family2 = Families_Family2 if Families_Family2 is not None else set()
        self.Families_Family5 = Families_Family5
        self.Families_Family8 = Families_Family8
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Families_Family2(self):
        return self.__Families_Family2

    @Families_Family2.setter
    def Families_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family2", None)
        self.__Families_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Member3"):
                    opp_val = getattr(item, "Families_Member3", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Member3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Member3"):
                    opp_val = getattr(item, "Families_Member3", None)
                    
                    setattr(item, "Families_Member3", self)
                    

    @property
    def Families_Family(self):
        return self.__Families_Family

    @Families_Family.setter
    def Families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family", None)
        self.__Families_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Member"):
                    opp_val = getattr(item, "Families_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Member"):
                    opp_val = getattr(item, "Families_Member", None)
                    
                    setattr(item, "Families_Member", self)
                    

    @property
    def Families_Family8(self):
        return self.__Families_Family8

    @Families_Family8.setter
    def Families_Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family8", None)
        self.__Families_Family8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Member9"):
                opp_val = getattr(old_value, "Families_Member9", None)
                if opp_val == self:
                    setattr(old_value, "Families_Member9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Member9"):
                opp_val = getattr(value, "Families_Member9", None)
                setattr(value, "Families_Member9", self)

    @property
    def Families_Family5(self):
        return self.__Families_Family5

    @Families_Family5.setter
    def Families_Family5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family5", None)
        self.__Families_Family5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Member6"):
                opp_val = getattr(old_value, "Families_Member6", None)
                if opp_val == self:
                    setattr(old_value, "Families_Member6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Member6"):
                opp_val = getattr(value, "Families_Member6", None)
                setattr(value, "Families_Member6", self)
