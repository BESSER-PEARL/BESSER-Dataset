from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Kasu1_ClassB:

    def __init__(self, Name: str, Kasu1_ClassB: "Kasu1_ClassA" = None, Kasu1_ClassB2: "Kasu1_ClassA" = None):
        self.Name = Name
        self.Kasu1_ClassB = Kasu1_ClassB
        self.Kasu1_ClassB2 = Kasu1_ClassB2
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu1_ClassB(self):
        return self.__Kasu1_ClassB

    @Kasu1_ClassB.setter
    def Kasu1_ClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu1_ClassB__Kasu1_ClassB", None)
        self.__Kasu1_ClassB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu1_ClassA"):
                opp_val = getattr(old_value, "Kasu1_ClassA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu1_ClassA"):
                opp_val = getattr(value, "Kasu1_ClassA", None)
                if opp_val is None:
                    setattr(value, "Kasu1_ClassA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Kasu1_ClassB2(self):
        return self.__Kasu1_ClassB2

    @Kasu1_ClassB2.setter
    def Kasu1_ClassB2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu1_ClassB__Kasu1_ClassB2", None)
        self.__Kasu1_ClassB2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu1_ClassA3"):
                opp_val = getattr(old_value, "Kasu1_ClassA3", None)
                if opp_val == self:
                    setattr(old_value, "Kasu1_ClassA3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu1_ClassA3"):
                opp_val = getattr(value, "Kasu1_ClassA3", None)
                setattr(value, "Kasu1_ClassA3", self)

class Kasu1_ClassA:

    def __init__(self, Name: str, Kasu1_ClassA: set["Kasu1_ClassB"] = None, Kasu1_ClassA3: "Kasu1_ClassB" = None):
        self.Name = Name
        self.Kasu1_ClassA = Kasu1_ClassA if Kasu1_ClassA is not None else set()
        self.Kasu1_ClassA3 = Kasu1_ClassA3
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu1_ClassA(self):
        return self.__Kasu1_ClassA

    @Kasu1_ClassA.setter
    def Kasu1_ClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu1_ClassA__Kasu1_ClassA", None)
        self.__Kasu1_ClassA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kasu1_ClassB"):
                    opp_val = getattr(item, "Kasu1_ClassB", None)
                    
                    if opp_val == self:
                        setattr(item, "Kasu1_ClassB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kasu1_ClassB"):
                    opp_val = getattr(item, "Kasu1_ClassB", None)
                    
                    setattr(item, "Kasu1_ClassB", self)
                    

    @property
    def Kasu1_ClassA3(self):
        return self.__Kasu1_ClassA3

    @Kasu1_ClassA3.setter
    def Kasu1_ClassA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu1_ClassA__Kasu1_ClassA3", None)
        self.__Kasu1_ClassA3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu1_ClassB2"):
                opp_val = getattr(old_value, "Kasu1_ClassB2", None)
                if opp_val == self:
                    setattr(old_value, "Kasu1_ClassB2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu1_ClassB2"):
                opp_val = getattr(value, "Kasu1_ClassB2", None)
                setattr(value, "Kasu1_ClassB2", self)
