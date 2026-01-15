from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Kasu4_ClassA:

    def __init__(self, Name: str, Kasu4_ClassA: set["Kasu4_ClassB"] = None, Kasu4_ClassA3: "Kasu4_ClassB" = None):
        self.Name = Name
        self.Kasu4_ClassA = Kasu4_ClassA if Kasu4_ClassA is not None else set()
        self.Kasu4_ClassA3 = Kasu4_ClassA3
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu4_ClassA(self):
        return self.__Kasu4_ClassA

    @Kasu4_ClassA.setter
    def Kasu4_ClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu4_ClassA__Kasu4_ClassA", None)
        self.__Kasu4_ClassA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kasu4_ClassB"):
                    opp_val = getattr(item, "Kasu4_ClassB", None)
                    
                    if opp_val == self:
                        setattr(item, "Kasu4_ClassB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kasu4_ClassB"):
                    opp_val = getattr(item, "Kasu4_ClassB", None)
                    
                    setattr(item, "Kasu4_ClassB", self)
                    

    @property
    def Kasu4_ClassA3(self):
        return self.__Kasu4_ClassA3

    @Kasu4_ClassA3.setter
    def Kasu4_ClassA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu4_ClassA__Kasu4_ClassA3", None)
        self.__Kasu4_ClassA3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu4_ClassB2"):
                opp_val = getattr(old_value, "Kasu4_ClassB2", None)
                if opp_val == self:
                    setattr(old_value, "Kasu4_ClassB2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu4_ClassB2"):
                opp_val = getattr(value, "Kasu4_ClassB2", None)
                setattr(value, "Kasu4_ClassB2", self)

class Kasu4_ClassB:

    def __init__(self, Name: str, Kasu4_ClassB: "Kasu4_ClassA" = None, Kasu4_ClassB2: "Kasu4_ClassA" = None):
        self.Name = Name
        self.Kasu4_ClassB = Kasu4_ClassB
        self.Kasu4_ClassB2 = Kasu4_ClassB2
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Kasu4_ClassB(self):
        return self.__Kasu4_ClassB

    @Kasu4_ClassB.setter
    def Kasu4_ClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu4_ClassB__Kasu4_ClassB", None)
        self.__Kasu4_ClassB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu4_ClassA"):
                opp_val = getattr(old_value, "Kasu4_ClassA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu4_ClassA"):
                opp_val = getattr(value, "Kasu4_ClassA", None)
                if opp_val is None:
                    setattr(value, "Kasu4_ClassA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Kasu4_ClassB2(self):
        return self.__Kasu4_ClassB2

    @Kasu4_ClassB2.setter
    def Kasu4_ClassB2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu4_ClassB__Kasu4_ClassB2", None)
        self.__Kasu4_ClassB2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kasu4_ClassA3"):
                opp_val = getattr(old_value, "Kasu4_ClassA3", None)
                if opp_val == self:
                    setattr(old_value, "Kasu4_ClassA3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kasu4_ClassA3"):
                opp_val = getattr(value, "Kasu4_ClassA3", None)
                setattr(value, "Kasu4_ClassA3", self)
