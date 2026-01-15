from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_FatherInLove:

    def __init__(self, Age: int, Name: str, family_FatherInLove: "family_Mother" = None):
        self.Age = Age
        self.Name = Name
        self.family_FatherInLove = family_FatherInLove
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self) -> int:
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def family_FatherInLove(self):
        return self.__family_FatherInLove

    @family_FatherInLove.setter
    def family_FatherInLove(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_FatherInLove__family_FatherInLove", None)
        self.__family_FatherInLove = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Mother6"):
                opp_val = getattr(old_value, "family_Mother6", None)
                if opp_val == self:
                    setattr(old_value, "family_Mother6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Mother6"):
                opp_val = getattr(value, "family_Mother6", None)
                setattr(value, "family_Mother6", self)

class family_Daughter:

    def __init__(self, Name: str, Age: int, family_Daughter: "family_Father" = None):
        self.Name = Name
        self.Age = Age
        self.family_Daughter = family_Daughter
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self) -> int:
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def family_Daughter(self):
        return self.__family_Daughter

    @family_Daughter.setter
    def family_Daughter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Daughter__family_Daughter", None)
        self.__family_Daughter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Father4"):
                opp_val = getattr(old_value, "family_Father4", None)
                if opp_val == self:
                    setattr(old_value, "family_Father4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Father4"):
                opp_val = getattr(value, "family_Father4", None)
                setattr(value, "family_Father4", self)

class family_Family:

    pass
class family_Son:

    def __init__(self, Name: str, Age: int, family_Son: "family_Father" = None):
        self.Name = Name
        self.Age = Age
        self.family_Son = family_Son
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self) -> int:
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def family_Son(self):
        return self.__family_Son

    @family_Son.setter
    def family_Son(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Son__family_Son", None)
        self.__family_Son = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Father2"):
                opp_val = getattr(old_value, "family_Father2", None)
                if opp_val == self:
                    setattr(old_value, "family_Father2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Father2"):
                opp_val = getattr(value, "family_Father2", None)
                setattr(value, "family_Father2", self)

class family_Mother:

    def __init__(self, Name: str, Age: int, family_Mother: "family_Father" = None, family_Mother6: "family_FatherInLove" = None):
        self.Name = Name
        self.Age = Age
        self.family_Mother = family_Mother
        self.family_Mother6 = family_Mother6
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self) -> int:
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def family_Mother6(self):
        return self.__family_Mother6

    @family_Mother6.setter
    def family_Mother6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Mother__family_Mother6", None)
        self.__family_Mother6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_FatherInLove"):
                opp_val = getattr(old_value, "family_FatherInLove", None)
                if opp_val == self:
                    setattr(old_value, "family_FatherInLove", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_FatherInLove"):
                opp_val = getattr(value, "family_FatherInLove", None)
                setattr(value, "family_FatherInLove", self)

    @property
    def family_Mother(self):
        return self.__family_Mother

    @family_Mother.setter
    def family_Mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Mother__family_Mother", None)
        self.__family_Mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Father"):
                opp_val = getattr(old_value, "family_Father", None)
                if opp_val == self:
                    setattr(old_value, "family_Father", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Father"):
                opp_val = getattr(value, "family_Father", None)
                setattr(value, "family_Father", self)

class family_Father:

    def __init__(self, Name: str, Age: int, family_Father: "family_Mother" = None, family_Father8: "family_Family" = None, family_Father2: "family_Son" = None, family_Father4: "family_Daughter" = None):
        self.Name = Name
        self.Age = Age
        self.family_Father = family_Father
        self.family_Father8 = family_Father8
        self.family_Father2 = family_Father2
        self.family_Father4 = family_Father4
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self) -> int:
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def family_Father8(self):
        return self.__family_Father8

    @family_Father8.setter
    def family_Father8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Father__family_Father8", None)
        self.__family_Father8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family"):
                opp_val = getattr(old_value, "family_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family"):
                opp_val = getattr(value, "family_Family", None)
                if opp_val is None:
                    setattr(value, "family_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_Father4(self):
        return self.__family_Father4

    @family_Father4.setter
    def family_Father4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Father__family_Father4", None)
        self.__family_Father4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Daughter"):
                opp_val = getattr(old_value, "family_Daughter", None)
                if opp_val == self:
                    setattr(old_value, "family_Daughter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Daughter"):
                opp_val = getattr(value, "family_Daughter", None)
                setattr(value, "family_Daughter", self)

    @property
    def family_Father2(self):
        return self.__family_Father2

    @family_Father2.setter
    def family_Father2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Father__family_Father2", None)
        self.__family_Father2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Son"):
                opp_val = getattr(old_value, "family_Son", None)
                if opp_val == self:
                    setattr(old_value, "family_Son", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Son"):
                opp_val = getattr(value, "family_Son", None)
                setattr(value, "family_Son", self)

    @property
    def family_Father(self):
        return self.__family_Father

    @family_Father.setter
    def family_Father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Father__family_Father", None)
        self.__family_Father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Mother"):
                opp_val = getattr(old_value, "family_Mother", None)
                if opp_val == self:
                    setattr(old_value, "family_Mother", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Mother"):
                opp_val = getattr(value, "family_Mother", None)
                setattr(value, "family_Mother", self)
