from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Families_Family:

    def __init__(self, lastName: str, familyDaughter: set["Families_Daughter"] = None, Family: "Families_Father" = None, familyFather: "Families_Father" = None, familyMother: "Families_Mother" = None, familySon: set["Families_Son"] = None, Family6: "Families_Mother" = None, Family8: "Families_Son" = None, Family10: "Families_Daughter" = None):
        self.lastName = lastName
        self.familyDaughter = familyDaughter if familyDaughter is not None else set()
        self.Family = Family
        self.familyFather = familyFather
        self.familyMother = familyMother
        self.familySon = familySon if familySon is not None else set()
        self.Family6 = Family6
        self.Family8 = Family8
        self.Family10 = Family10
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Family10(self):
        return self.__Family10

    @Family10.setter
    def Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family10", None)
        self.__Family10 = value
        
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
    def Family8(self):
        return self.__Family8

    @Family8.setter
    def Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family8", None)
        self.__Family8 = value
        
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
    def familyDaughter(self):
        return self.__familyDaughter

    @familyDaughter.setter
    def familyDaughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyDaughter", None)
        self.__familyDaughter = value if value is not None else set()
        
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
    def familyFather(self):
        return self.__familyFather

    @familyFather.setter
    def familyFather(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyFather", None)
        self.__familyFather = value
        
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
    def familySon(self):
        return self.__familySon

    @familySon.setter
    def familySon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familySon", None)
        self.__familySon = value if value is not None else set()
        
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
    def familyMother(self):
        return self.__familyMother

    @familyMother.setter
    def familyMother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__familyMother", None)
        self.__familyMother = value
        
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
    def Family6(self):
        return self.__Family6

    @Family6.setter
    def Family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Family6", None)
        self.__Family6 = value
        
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

class Member:

    pass
class Families_Mother(Member):

    pass
class Families_Father(Member):

    pass
class Families_Son(Member):

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