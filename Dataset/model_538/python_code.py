from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleFamilies_Family:

    def __init__(self, name: str, SimpleFamilies_Family2: "SimpleFamilies_FamilyMember" = None, SimpleFamilies_Family: "SimpleFamilies_FamilyRegister" = None, SimpleFamilies_Family4: "SimpleFamilies_FamilyMember" = None, SimpleFamilies_Family7: set["SimpleFamilies_FamilyMember"] = None, SimpleFamilies_Family10: set["SimpleFamilies_FamilyMember"] = None):
        self.name = name
        self.SimpleFamilies_Family2 = SimpleFamilies_Family2
        self.SimpleFamilies_Family = SimpleFamilies_Family
        self.SimpleFamilies_Family4 = SimpleFamilies_Family4
        self.SimpleFamilies_Family7 = SimpleFamilies_Family7 if SimpleFamilies_Family7 is not None else set()
        self.SimpleFamilies_Family10 = SimpleFamilies_Family10 if SimpleFamilies_Family10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleFamilies_Family7(self):
        return self.__SimpleFamilies_Family7

    @SimpleFamilies_Family7.setter
    def SimpleFamilies_Family7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_Family__SimpleFamilies_Family7", None)
        self.__SimpleFamilies_Family7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleFamilies_FamilyMember8"):
                    opp_val = getattr(item, "SimpleFamilies_FamilyMember8", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleFamilies_FamilyMember8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleFamilies_FamilyMember8"):
                    opp_val = getattr(item, "SimpleFamilies_FamilyMember8", None)
                    
                    setattr(item, "SimpleFamilies_FamilyMember8", self)
                    

    @property
    def SimpleFamilies_Family4(self):
        return self.__SimpleFamilies_Family4

    @SimpleFamilies_Family4.setter
    def SimpleFamilies_Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_Family__SimpleFamilies_Family4", None)
        self.__SimpleFamilies_Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_FamilyMember5"):
                opp_val = getattr(old_value, "SimpleFamilies_FamilyMember5", None)
                if opp_val == self:
                    setattr(old_value, "SimpleFamilies_FamilyMember5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_FamilyMember5"):
                opp_val = getattr(value, "SimpleFamilies_FamilyMember5", None)
                setattr(value, "SimpleFamilies_FamilyMember5", self)

    @property
    def SimpleFamilies_Family(self):
        return self.__SimpleFamilies_Family

    @SimpleFamilies_Family.setter
    def SimpleFamilies_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_Family__SimpleFamilies_Family", None)
        self.__SimpleFamilies_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_FamilyRegister"):
                opp_val = getattr(old_value, "SimpleFamilies_FamilyRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_FamilyRegister"):
                opp_val = getattr(value, "SimpleFamilies_FamilyRegister", None)
                if opp_val is None:
                    setattr(value, "SimpleFamilies_FamilyRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleFamilies_Family2(self):
        return self.__SimpleFamilies_Family2

    @SimpleFamilies_Family2.setter
    def SimpleFamilies_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_Family__SimpleFamilies_Family2", None)
        self.__SimpleFamilies_Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_FamilyMember"):
                opp_val = getattr(old_value, "SimpleFamilies_FamilyMember", None)
                if opp_val == self:
                    setattr(old_value, "SimpleFamilies_FamilyMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_FamilyMember"):
                opp_val = getattr(value, "SimpleFamilies_FamilyMember", None)
                setattr(value, "SimpleFamilies_FamilyMember", self)

    @property
    def SimpleFamilies_Family10(self):
        return self.__SimpleFamilies_Family10

    @SimpleFamilies_Family10.setter
    def SimpleFamilies_Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_Family__SimpleFamilies_Family10", None)
        self.__SimpleFamilies_Family10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleFamilies_FamilyMember11"):
                    opp_val = getattr(item, "SimpleFamilies_FamilyMember11", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleFamilies_FamilyMember11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleFamilies_FamilyMember11"):
                    opp_val = getattr(item, "SimpleFamilies_FamilyMember11", None)
                    
                    setattr(item, "SimpleFamilies_FamilyMember11", self)
                    

class SimpleFamilies_FamilyRegister:

    pass
class SimpleFamilies_FamilyMember:

    def __init__(self, name: str, SimpleFamilies_FamilyMember: "SimpleFamilies_Family" = None, SimpleFamilies_FamilyMember5: "SimpleFamilies_Family" = None, SimpleFamilies_FamilyMember8: "SimpleFamilies_Family" = None, SimpleFamilies_FamilyMember11: "SimpleFamilies_Family" = None):
        self.name = name
        self.SimpleFamilies_FamilyMember = SimpleFamilies_FamilyMember
        self.SimpleFamilies_FamilyMember5 = SimpleFamilies_FamilyMember5
        self.SimpleFamilies_FamilyMember8 = SimpleFamilies_FamilyMember8
        self.SimpleFamilies_FamilyMember11 = SimpleFamilies_FamilyMember11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleFamilies_FamilyMember8(self):
        return self.__SimpleFamilies_FamilyMember8

    @SimpleFamilies_FamilyMember8.setter
    def SimpleFamilies_FamilyMember8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_FamilyMember__SimpleFamilies_FamilyMember8", None)
        self.__SimpleFamilies_FamilyMember8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_Family7"):
                opp_val = getattr(old_value, "SimpleFamilies_Family7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_Family7"):
                opp_val = getattr(value, "SimpleFamilies_Family7", None)
                if opp_val is None:
                    setattr(value, "SimpleFamilies_Family7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleFamilies_FamilyMember11(self):
        return self.__SimpleFamilies_FamilyMember11

    @SimpleFamilies_FamilyMember11.setter
    def SimpleFamilies_FamilyMember11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_FamilyMember__SimpleFamilies_FamilyMember11", None)
        self.__SimpleFamilies_FamilyMember11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_Family10"):
                opp_val = getattr(old_value, "SimpleFamilies_Family10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_Family10"):
                opp_val = getattr(value, "SimpleFamilies_Family10", None)
                if opp_val is None:
                    setattr(value, "SimpleFamilies_Family10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleFamilies_FamilyMember(self):
        return self.__SimpleFamilies_FamilyMember

    @SimpleFamilies_FamilyMember.setter
    def SimpleFamilies_FamilyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_FamilyMember__SimpleFamilies_FamilyMember", None)
        self.__SimpleFamilies_FamilyMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_Family2"):
                opp_val = getattr(old_value, "SimpleFamilies_Family2", None)
                if opp_val == self:
                    setattr(old_value, "SimpleFamilies_Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_Family2"):
                opp_val = getattr(value, "SimpleFamilies_Family2", None)
                setattr(value, "SimpleFamilies_Family2", self)

    @property
    def SimpleFamilies_FamilyMember5(self):
        return self.__SimpleFamilies_FamilyMember5

    @SimpleFamilies_FamilyMember5.setter
    def SimpleFamilies_FamilyMember5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleFamilies_FamilyMember__SimpleFamilies_FamilyMember5", None)
        self.__SimpleFamilies_FamilyMember5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFamilies_Family4"):
                opp_val = getattr(old_value, "SimpleFamilies_Family4", None)
                if opp_val == self:
                    setattr(old_value, "SimpleFamilies_Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFamilies_Family4"):
                opp_val = getattr(value, "SimpleFamilies_Family4", None)
                setattr(value, "SimpleFamilies_Family4", self)
