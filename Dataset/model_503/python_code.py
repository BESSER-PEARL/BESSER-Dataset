from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Member:

    pass
class Families_Member(ABC):

    def __init__(self, firstName: str):
        self.firstName = firstName
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

class Families_Daughter(Member):

    pass
class Families_Son(Member):

    pass
class Families_Mother(Member):

    pass
class Families_Father(Member):

    pass
class Families_Family:

    def __init__(self, lastName: str, family: "Families_Father" = None, family2: "Families_Mother" = None, family4: set["Families_Son"] = None, family6: set["Families_Daughter"] = None, Family: "Families_Father" = None, Family9: "Families_Mother" = None, Family11: "Families_Son" = None, Family13: "Families_Daughter" = None):
        self.lastName = lastName
        self.family = family
        self.family2 = family2
        self.family4 = family4 if family4 is not None else set()
        self.family6 = family6 if family6 is not None else set()
        self.Family = Family
        self.Family9 = Family9
        self.Family11 = Family11
        self.Family13 = Family13
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__family", None)
        self.__family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Father"):
                opp_val = getattr(old_value, "Father", None)
                if opp_val == self:
                    setattr(old_value, "Father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Father"):
                opp_val = getattr(value, "Father", None)
                setattr(value, "Father", self)

    @property
    def family6(self):
        return self.__family6

    @family6.setter
    def family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__family6", None)
        self.__family6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Daughter"):
                    opp_val = getattr(item, "Daughter", None)
                    
                    if opp_val == self:
                        setattr(item, "Daughter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Daughter"):
                    opp_val = getattr(item, "Daughter", None)
                    
                    setattr(item, "Daughter", self)
                    

    @property
    def family4(self):
        return self.__family4

    @family4.setter
    def family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__family4", None)
        self.__family4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    if opp_val == self:
                        setattr(item, "Son", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    setattr(item, "Son", self)
                    

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "father"):
                opp_val = getattr(old_value, "father", None)
                if opp_val == self:
                    setattr(old_value, "father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "father"):
                opp_val = getattr(value, "father", None)
                setattr(value, "father", self)

    @property
    def Family11(self):
        return self.__Family11

    @Family11.setter
    def Family11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family11", None)
        self.__Family11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sons"):
                opp_val = getattr(old_value, "sons", None)
                if opp_val == self:
                    setattr(old_value, "sons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sons"):
                opp_val = getattr(value, "sons", None)
                setattr(value, "sons", self)

    @property
    def family2(self):
        return self.__family2

    @family2.setter
    def family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__family2", None)
        self.__family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mother"):
                opp_val = getattr(old_value, "Mother", None)
                if opp_val == self:
                    setattr(old_value, "Mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mother"):
                opp_val = getattr(value, "Mother", None)
                setattr(value, "Mother", self)

    @property
    def Family13(self):
        return self.__Family13

    @Family13.setter
    def Family13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family13", None)
        self.__Family13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daughters"):
                opp_val = getattr(old_value, "daughters", None)
                if opp_val == self:
                    setattr(old_value, "daughters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daughters"):
                opp_val = getattr(value, "daughters", None)
                setattr(value, "daughters", self)

    @property
    def Family9(self):
        return self.__Family9

    @Family9.setter
    def Family9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family9", None)
        self.__Family9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mother"):
                opp_val = getattr(old_value, "mother", None)
                if opp_val == self:
                    setattr(old_value, "mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mother"):
                opp_val = getattr(value, "mother", None)
                setattr(value, "mother", self)
