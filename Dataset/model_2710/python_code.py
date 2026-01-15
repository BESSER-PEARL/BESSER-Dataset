from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Kasu11_ClassB:

    def __init__(self, Name: str, ClassB: "Kasu11_ClassA" = None, C_B: "Kasu11_ClassA" = None, C_B5: set["Kasu11_ClassC"] = None, ClassB11: "Kasu11_ClassC" = None):
        self.Name = Name
        self.ClassB = ClassB
        self.C_B = C_B
        self.C_B5 = C_B5 if C_B5 is not None else set()
        self.ClassB11 = ClassB11
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ClassB11(self):
        return self.__ClassB11

    @ClassB11.setter
    def ClassB11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassB__ClassB11", None)
        self.__ClassB11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_C10"):
                opp_val = getattr(old_value, "C_C10", None)
                if opp_val == self:
                    setattr(old_value, "C_C10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_C10"):
                opp_val = getattr(value, "C_C10", None)
                setattr(value, "C_C10", self)

    @property
    def C_B5(self):
        return self.__C_B5

    @C_B5.setter
    def C_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassB__C_B5", None)
        self.__C_B5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassC6"):
                    opp_val = getattr(item, "ClassC6", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassC6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassC6"):
                    opp_val = getattr(item, "ClassC6", None)
                    
                    setattr(item, "ClassC6", self)
                    

    @property
    def ClassB(self):
        return self.__ClassB

    @ClassB.setter
    def ClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassB__ClassB", None)
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

    @property
    def C_B(self):
        return self.__C_B

    @C_B.setter
    def C_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassB__C_B", None)
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

class Kasu11_ClassA:

    def __init__(self, Name: str, C_A2: set["Kasu11_ClassC"] = None, ClassA: "Kasu11_ClassB" = None, C_A: set["Kasu11_ClassB"] = None, ClassA8: "Kasu11_ClassC" = None):
        self.Name = Name
        self.C_A2 = C_A2 if C_A2 is not None else set()
        self.ClassA = ClassA
        self.C_A = C_A if C_A is not None else set()
        self.ClassA8 = ClassA8
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ClassA(self):
        return self.__ClassA

    @ClassA.setter
    def ClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassA__ClassA", None)
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

    @property
    def C_A2(self):
        return self.__C_A2

    @C_A2.setter
    def C_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassA__C_A2", None)
        self.__C_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassC"):
                    opp_val = getattr(item, "ClassC", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassC", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassC"):
                    opp_val = getattr(item, "ClassC", None)
                    
                    setattr(item, "ClassC", self)
                    

    @property
    def ClassA8(self):
        return self.__ClassA8

    @ClassA8.setter
    def ClassA8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassA__ClassA8", None)
        self.__ClassA8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_C"):
                opp_val = getattr(old_value, "C_C", None)
                if opp_val == self:
                    setattr(old_value, "C_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_C"):
                opp_val = getattr(value, "C_C", None)
                setattr(value, "C_C", self)

    @property
    def C_A(self):
        return self.__C_A

    @C_A.setter
    def C_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassA__C_A", None)
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
                    

class Kasu11_ClassC:

    def __init__(self, Name: str, ClassC: "Kasu11_ClassA" = None, ClassC6: "Kasu11_ClassB" = None, C_C: "Kasu11_ClassA" = None, C_C10: "Kasu11_ClassB" = None):
        self.Name = Name
        self.ClassC = ClassC
        self.ClassC6 = ClassC6
        self.C_C = C_C
        self.C_C10 = C_C10
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def C_C10(self):
        return self.__C_C10

    @C_C10.setter
    def C_C10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassC__C_C10", None)
        self.__C_C10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassB11"):
                opp_val = getattr(old_value, "ClassB11", None)
                if opp_val == self:
                    setattr(old_value, "ClassB11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassB11"):
                opp_val = getattr(value, "ClassB11", None)
                setattr(value, "ClassB11", self)

    @property
    def ClassC6(self):
        return self.__ClassC6

    @ClassC6.setter
    def ClassC6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassC__ClassC6", None)
        self.__ClassC6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_B5"):
                opp_val = getattr(old_value, "C_B5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_B5"):
                opp_val = getattr(value, "C_B5", None)
                if opp_val is None:
                    setattr(value, "C_B5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def C_C(self):
        return self.__C_C

    @C_C.setter
    def C_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassC__C_C", None)
        self.__C_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassA8"):
                opp_val = getattr(old_value, "ClassA8", None)
                if opp_val == self:
                    setattr(old_value, "ClassA8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassA8"):
                opp_val = getattr(value, "ClassA8", None)
                setattr(value, "ClassA8", self)

    @property
    def ClassC(self):
        return self.__ClassC

    @ClassC.setter
    def ClassC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kasu11_ClassC__ClassC", None)
        self.__ClassC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C_A2"):
                opp_val = getattr(old_value, "C_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C_A2"):
                opp_val = getattr(value, "C_A2", None)
                if opp_val is None:
                    setattr(value, "C_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
