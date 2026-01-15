from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Kasu3_ClassB:

    def __init__(self, Name: str, Kasu3_ClassB2: "Kasu3_ClassA" = None, Kasu3_ClassB: "Kasu3_ClassA" = None):
        self.Name = Name
        self.Kasu3_ClassB2 = Kasu3_ClassB2
        self.Kasu3_ClassB = Kasu3_ClassB
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu3_ClassB(self):
        return self.__Kasu3_ClassB

    @Kasu3_ClassB.setter
    def Kasu3_ClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu3_ClassB__Kasu3_ClassB", None)
        self.__Kasu3_ClassB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu3_ClassA"):
                opp_val = getattr(old_value, "Kasu3_ClassA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu3_ClassA"):
                opp_val = getattr(value, "Kasu3_ClassA", None)
                if opp_val is None:
                    setattr(value, "Kasu3_ClassA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Kasu3_ClassB2(self):
        return self.__Kasu3_ClassB2

    @Kasu3_ClassB2.setter
    def Kasu3_ClassB2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu3_ClassB__Kasu3_ClassB2", None)
        self.__Kasu3_ClassB2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu3_ClassA3"):
                opp_val = getattr(old_value, "Kasu3_ClassA3", None)
                if opp_val == self:
                    setattr(old_value, "Kasu3_ClassA3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu3_ClassA3"):
                opp_val = getattr(value, "Kasu3_ClassA3", None)
                setattr(value, "Kasu3_ClassA3", self)

class Kasu3_ClassA:

    def __init__(self, Name: str, Kasu3_ClassA3: "Kasu3_ClassB" = None, Kasu3_ClassA: set["Kasu3_ClassB"] = None):
        self.Name = Name
        self.Kasu3_ClassA3 = Kasu3_ClassA3
        self.Kasu3_ClassA = Kasu3_ClassA if Kasu3_ClassA is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu3_ClassA3(self):
        return self.__Kasu3_ClassA3

    @Kasu3_ClassA3.setter
    def Kasu3_ClassA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu3_ClassA__Kasu3_ClassA3", None)
        self.__Kasu3_ClassA3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu3_ClassB2"):
                opp_val = getattr(old_value, "Kasu3_ClassB2", None)
                if opp_val == self:
                    setattr(old_value, "Kasu3_ClassB2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu3_ClassB2"):
                opp_val = getattr(value, "Kasu3_ClassB2", None)
                setattr(value, "Kasu3_ClassB2", self)

    @property
    def Kasu3_ClassA(self):
        return self.__Kasu3_ClassA

    @Kasu3_ClassA.setter
    def Kasu3_ClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu3_ClassA__Kasu3_ClassA", None)
        self.__Kasu3_ClassA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kasu3_ClassB"):
                    opp_val = getattr(item, "Kasu3_ClassB", None)
                    
                    if opp_val == self:
                        setattr(item, "Kasu3_ClassB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kasu3_ClassB"):
                    opp_val = getattr(item, "Kasu3_ClassB", None)
                    
                    setattr(item, "Kasu3_ClassB", self)
                    

class Kasu3_ClassC:

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name
