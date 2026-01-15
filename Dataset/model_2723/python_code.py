from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Kasu2_Root:

    pass
class Kasu2_ClassB:

    def __init__(self, Name: str, ClassB: "Kasu2_ClassA" = None, C_B: "Kasu2_ClassA" = None):
        self.Name = Name
        self.ClassB = ClassB
        self.C_B = C_B
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def C_B(self):
        return self.__C_B

    @C_B.setter
    def C_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassB__C_B", None)
        self.__C_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassA"):
                opp_val = getattr(old_value, "ClassA", None)
                if opp_val == self:
                    setattr(old_value, "ClassA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassA"):
                opp_val = getattr(value, "ClassA", None)
                setattr(value, "ClassA", self)

    @property
    def ClassB(self):
        return self.__ClassB

    @ClassB.setter
    def ClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassB__ClassB", None)
        self.__ClassB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_A"):
                opp_val = getattr(old_value, "C_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_A"):
                opp_val = getattr(value, "C_A", None)
                if opp_val is None:
                    setattr(value, "C_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Kasu2_ClassA:

    def __init__(self, Name: str, C_A: set["Kasu2_ClassB"] = None, C_A2: "Kasu2_Root" = None, ClassA: "Kasu2_ClassB" = None, ClassA5: "Kasu2_Root" = None):
        self.Name = Name
        self.C_A = C_A if C_A is not None else set()
        self.C_A2 = C_A2
        self.ClassA = ClassA
        self.ClassA5 = ClassA5
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def C_A(self):
        return self.__C_A

    @C_A.setter
    def C_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassA__C_A", None)
        self.__C_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassB"):
                    opp_val = getattr(item, "ClassB", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassB"):
                    opp_val = getattr(item, "ClassB", None)
                    
                    setattr(item, "ClassB", self)
                    

    @property
    def C_A2(self):
        return self.__C_A2

    @C_A2.setter
    def C_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassA__C_A2", None)
        self.__C_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

    @property
    def ClassA5(self):
        return self.__ClassA5

    @ClassA5.setter
    def ClassA5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassA__ClassA5", None)
        self.__ClassA5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_R"):
                opp_val = getattr(old_value, "C_R", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_R"):
                opp_val = getattr(value, "C_R", None)
                if opp_val is None:
                    setattr(value, "C_R", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassA(self):
        return self.__ClassA

    @ClassA.setter
    def ClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu2_ClassA__ClassA", None)
        self.__ClassA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_B"):
                opp_val = getattr(old_value, "C_B", None)
                if opp_val == self:
                    setattr(old_value, "C_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_B"):
                opp_val = getattr(value, "C_B", None)
                setattr(value, "C_B", self)
