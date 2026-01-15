from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FamilyRegister_Member:

    def __init__(self, name: str, FamilyRegister_Member: "FamilyRegister_Family" = None, FamilyRegister_Member5: "FamilyRegister_Family" = None, FamilyRegister_Member11: "FamilyRegister_Family" = None, FamilyRegister_Member8: "FamilyRegister_Family" = None):
        self.name = name
        self.FamilyRegister_Member = FamilyRegister_Member
        self.FamilyRegister_Member5 = FamilyRegister_Member5
        self.FamilyRegister_Member11 = FamilyRegister_Member11
        self.FamilyRegister_Member8 = FamilyRegister_Member8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FamilyRegister_Member(self):
        return self.__FamilyRegister_Member

    @FamilyRegister_Member.setter
    def FamilyRegister_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Member__FamilyRegister_Member", None)
        self.__FamilyRegister_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Family2"):
                opp_val = getattr(old_value, "FamilyRegister_Family2", None)
                if opp_val == self:
                    setattr(old_value, "FamilyRegister_Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Family2"):
                opp_val = getattr(value, "FamilyRegister_Family2", None)
                setattr(value, "FamilyRegister_Family2", self)

    @property
    def FamilyRegister_Member11(self):
        return self.__FamilyRegister_Member11

    @FamilyRegister_Member11.setter
    def FamilyRegister_Member11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Member__FamilyRegister_Member11", None)
        self.__FamilyRegister_Member11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Family10"):
                opp_val = getattr(old_value, "FamilyRegister_Family10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Family10"):
                opp_val = getattr(value, "FamilyRegister_Family10", None)
                if opp_val is None:
                    setattr(value, "FamilyRegister_Family10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FamilyRegister_Member5(self):
        return self.__FamilyRegister_Member5

    @FamilyRegister_Member5.setter
    def FamilyRegister_Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Member__FamilyRegister_Member5", None)
        self.__FamilyRegister_Member5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Family4"):
                opp_val = getattr(old_value, "FamilyRegister_Family4", None)
                if opp_val == self:
                    setattr(old_value, "FamilyRegister_Family4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Family4"):
                opp_val = getattr(value, "FamilyRegister_Family4", None)
                setattr(value, "FamilyRegister_Family4", self)

    @property
    def FamilyRegister_Member8(self):
        return self.__FamilyRegister_Member8

    @FamilyRegister_Member8.setter
    def FamilyRegister_Member8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Member__FamilyRegister_Member8", None)
        self.__FamilyRegister_Member8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Family7"):
                opp_val = getattr(old_value, "FamilyRegister_Family7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Family7"):
                opp_val = getattr(value, "FamilyRegister_Family7", None)
                if opp_val is None:
                    setattr(value, "FamilyRegister_Family7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FamilyRegister_Family:

    def __init__(self, name: str, FamilyRegister_Family2: "FamilyRegister_Member" = None, FamilyRegister_Family4: "FamilyRegister_Member" = None, FamilyRegister_Family: "FamilyRegister_FamilyRegister" = None, FamilyRegister_Family10: set["FamilyRegister_Member"] = None, FamilyRegister_Family7: set["FamilyRegister_Member"] = None):
        self.name = name
        self.FamilyRegister_Family2 = FamilyRegister_Family2
        self.FamilyRegister_Family4 = FamilyRegister_Family4
        self.FamilyRegister_Family = FamilyRegister_Family
        self.FamilyRegister_Family10 = FamilyRegister_Family10 if FamilyRegister_Family10 is not None else set()
        self.FamilyRegister_Family7 = FamilyRegister_Family7 if FamilyRegister_Family7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FamilyRegister_Family10(self):
        return self.__FamilyRegister_Family10

    @FamilyRegister_Family10.setter
    def FamilyRegister_Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Family__FamilyRegister_Family10", None)
        self.__FamilyRegister_Family10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyRegister_Member11"):
                    opp_val = getattr(item, "FamilyRegister_Member11", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyRegister_Member11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyRegister_Member11"):
                    opp_val = getattr(item, "FamilyRegister_Member11", None)
                    
                    setattr(item, "FamilyRegister_Member11", self)
                    

    @property
    def FamilyRegister_Family7(self):
        return self.__FamilyRegister_Family7

    @FamilyRegister_Family7.setter
    def FamilyRegister_Family7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Family__FamilyRegister_Family7", None)
        self.__FamilyRegister_Family7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyRegister_Member8"):
                    opp_val = getattr(item, "FamilyRegister_Member8", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyRegister_Member8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyRegister_Member8"):
                    opp_val = getattr(item, "FamilyRegister_Member8", None)
                    
                    setattr(item, "FamilyRegister_Member8", self)
                    

    @property
    def FamilyRegister_Family2(self):
        return self.__FamilyRegister_Family2

    @FamilyRegister_Family2.setter
    def FamilyRegister_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Family__FamilyRegister_Family2", None)
        self.__FamilyRegister_Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Member"):
                opp_val = getattr(old_value, "FamilyRegister_Member", None)
                if opp_val == self:
                    setattr(old_value, "FamilyRegister_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Member"):
                opp_val = getattr(value, "FamilyRegister_Member", None)
                setattr(value, "FamilyRegister_Member", self)

    @property
    def FamilyRegister_Family4(self):
        return self.__FamilyRegister_Family4

    @FamilyRegister_Family4.setter
    def FamilyRegister_Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Family__FamilyRegister_Family4", None)
        self.__FamilyRegister_Family4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_Member5"):
                opp_val = getattr(old_value, "FamilyRegister_Member5", None)
                if opp_val == self:
                    setattr(old_value, "FamilyRegister_Member5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_Member5"):
                opp_val = getattr(value, "FamilyRegister_Member5", None)
                setattr(value, "FamilyRegister_Member5", self)

    @property
    def FamilyRegister_Family(self):
        return self.__FamilyRegister_Family

    @FamilyRegister_Family.setter
    def FamilyRegister_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FamilyRegister_Family__FamilyRegister_Family", None)
        self.__FamilyRegister_Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyRegister_FamilyRegister"):
                opp_val = getattr(old_value, "FamilyRegister_FamilyRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyRegister_FamilyRegister"):
                opp_val = getattr(value, "FamilyRegister_FamilyRegister", None)
                if opp_val is None:
                    setattr(value, "FamilyRegister_FamilyRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FamilyRegister_FamilyRegister:

    pass