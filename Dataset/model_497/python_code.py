from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class Family:

    pass
class Families_Member:

    def __init__(self, firstName: str, 011: "Family" = None, 014: "Family" = None, 017: "Family" = None, 020: "Family" = None, Families_Member: set["Person"] = None):
        self.firstName = firstName
        self.011 = 011
        self.014 = 014
        self.017 = 017
        self.020 = 020
        self.Families_Member = Families_Member if Families_Member is not None else set()
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def 014(self):
        return self.__014

    @014.setter
    def 014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__014", None)
        self.__014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#15"):
                opp_val = getattr(old_value, "#15", None)
                if opp_val == self:
                    setattr(old_value, "#15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#15"):
                opp_val = getattr(value, "#15", None)
                setattr(value, "#15", self)

    @property
    def 020(self):
        return self.__020

    @020.setter
    def 020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__020", None)
        self.__020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#21"):
                opp_val = getattr(old_value, "#21", None)
                if opp_val == self:
                    setattr(old_value, "#21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#21"):
                opp_val = getattr(value, "#21", None)
                setattr(value, "#21", self)

    @property
    def 017(self):
        return self.__017

    @017.setter
    def 017(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__017", None)
        self.__017 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#18"):
                opp_val = getattr(old_value, "#18", None)
                if opp_val == self:
                    setattr(old_value, "#18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#18"):
                opp_val = getattr(value, "#18", None)
                setattr(value, "#18", self)

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__011", None)
        self.__011 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#12"):
                opp_val = getattr(old_value, "#12", None)
                if opp_val == self:
                    setattr(old_value, "#12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#12"):
                opp_val = getattr(value, "#12", None)
                setattr(value, "#12", self)

    @property
    def Families_Member(self):
        return self.__Families_Member

    @Families_Member.setter
    def Families_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member", None)
        self.__Families_Member = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

class Member:

    pass
class Families_Family:

    def __init__(self, lastName: str, 0: "Member" = None, 02: "Member" = None, 05: set["Member"] = None, 08: set["Member"] = None):
        self.lastName = lastName
        self.0 = 0
        self.02 = 02
        self.05 = 05 if 05 is not None else set()
        self.08 = 08 if 08 is not None else set()
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__0", None)
        self.__0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#"):
                opp_val = getattr(old_value, "#", None)
                if opp_val == self:
                    setattr(old_value, "#", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#"):
                opp_val = getattr(value, "#", None)
                setattr(value, "#", self)

    @property
    def 08(self):
        return self.__08

    @08.setter
    def 08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__08", None)
        self.__08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    if opp_val == self:
                        setattr(item, "#9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    setattr(item, "#9", self)
                    

    @property
    def 02(self):
        return self.__02

    @02.setter
    def 02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__02", None)
        self.__02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#3"):
                opp_val = getattr(old_value, "#3", None)
                if opp_val == self:
                    setattr(old_value, "#3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#3"):
                opp_val = getattr(value, "#3", None)
                setattr(value, "#3", self)

    @property
    def 05(self):
        return self.__05

    @05.setter
    def 05(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__05", None)
        self.__05 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    if opp_val == self:
                        setattr(item, "#6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    setattr(item, "#6", self)
                    
