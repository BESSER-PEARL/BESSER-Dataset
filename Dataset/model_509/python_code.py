from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Families_FamilyRegistry:

    pass
class Families_Member:

    def __init__(self, firstName: str, age: int, Families_Member3: "Families_Family" = None, Families_Member6: "Families_Family" = None, Families_Member9: "Families_Family" = None, Families_Member: "Families_Family" = None, Families_Member15: "Families_Member" = None, Families_Member13: "Families_Member" = None):
        self.firstName = firstName
        self.age = age
        self.Families_Member3 = Families_Member3
        self.Families_Member6 = Families_Member6
        self.Families_Member9 = Families_Member9
        self.Families_Member = Families_Member
        self.Families_Member15 = Families_Member15
        self.Families_Member13 = Families_Member13
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

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
    def Families_Member13(self):
        return self.__Families_Member13

    @Families_Member13.setter
    def Families_Member13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member13", None)
        self.__Families_Member13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Member15"):
                opp_val = getattr(old_value, "Families_Member15", None)
                if opp_val == self:
                    setattr(old_value, "Families_Member15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Member15"):
                opp_val = getattr(value, "Families_Member15", None)
                setattr(value, "Families_Member15", self)

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
    def Families_Member15(self):
        return self.__Families_Member15

    @Families_Member15.setter
    def Families_Member15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Member__Families_Member15", None)
        self.__Families_Member15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Member13"):
                opp_val = getattr(old_value, "Families_Member13", None)
                if opp_val == self:
                    setattr(old_value, "Families_Member13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Member13"):
                opp_val = getattr(value, "Families_Member13", None)
                setattr(value, "Families_Member13", self)

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

    def __init__(self, address: str, lastName: str, Families_Family2: set["Families_Member"] = None, Families_Family5: "Families_Member" = None, Families_Family8: "Families_Member" = None, Families_Family12: "Families_Family" = None, Families_Family10: set["Families_Family"] = None, Families_Family: set["Families_Member"] = None, Families_Family17: "Families_FamilyRegistry" = None):
        self.address = address
        self.lastName = lastName
        self.Families_Family2 = Families_Family2 if Families_Family2 is not None else set()
        self.Families_Family5 = Families_Family5
        self.Families_Family8 = Families_Family8
        self.Families_Family12 = Families_Family12
        self.Families_Family10 = Families_Family10 if Families_Family10 is not None else set()
        self.Families_Family = Families_Family if Families_Family is not None else set()
        self.Families_Family17 = Families_Family17
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

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
    def Families_Family10(self):
        return self.__Families_Family10

    @Families_Family10.setter
    def Families_Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family10", None)
        self.__Families_Family10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Families_Family12"):
                    opp_val = getattr(item, "Families_Family12", None)
                    
                    if opp_val == self:
                        setattr(item, "Families_Family12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Families_Family12"):
                    opp_val = getattr(item, "Families_Family12", None)
                    
                    setattr(item, "Families_Family12", self)
                    

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
    def Families_Family17(self):
        return self.__Families_Family17

    @Families_Family17.setter
    def Families_Family17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family17", None)
        self.__Families_Family17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_FamilyRegistry"):
                opp_val = getattr(old_value, "Families_FamilyRegistry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_FamilyRegistry"):
                opp_val = getattr(value, "Families_FamilyRegistry", None)
                if opp_val is None:
                    setattr(value, "Families_FamilyRegistry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Families_Family12(self):
        return self.__Families_Family12

    @Families_Family12.setter
    def Families_Family12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Families_Family__Families_Family12", None)
        self.__Families_Family12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Families_Family10"):
                opp_val = getattr(old_value, "Families_Family10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Families_Family10"):
                opp_val = getattr(value, "Families_Family10", None)
                if opp_val is None:
                    setattr(value, "Families_Family10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
