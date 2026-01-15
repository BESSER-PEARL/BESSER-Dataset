from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_F:

    pass
class test_E:

    def __init__(self, newAttribute2: str):
        self.newAttribute2 = newAttribute2
        
    @property
    def newAttribute2(self) -> str:
        return self.__newAttribute2

    @newAttribute2.setter
    def newAttribute2(self, newAttribute2: str):
        self.__newAttribute2 = newAttribute2

class test_D:

    def __init__(self, newAttribute: str, test_D: "test_Adown" = None):
        self.newAttribute = newAttribute
        self.test_D = test_D
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def test_D(self):
        return self.__test_D

    @test_D.setter
    def test_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_D__test_D", None)
        self.__test_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Adown3"):
                opp_val = getattr(old_value, "test_Adown3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Adown3"):
                opp_val = getattr(value, "test_Adown3", None)
                if opp_val is None:
                    setattr(value, "test_Adown3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_C:

    def __init__(self, newAttribute: str, c: "test_Adown" = None, C: "test_Adown" = None):
        self.newAttribute = newAttribute
        self.c = c
        self.C = C
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_C__C", None)
        self.__C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a"):
                opp_val = getattr(old_value, "a", None)
                if opp_val == self:
                    setattr(old_value, "a", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a"):
                opp_val = getattr(value, "a", None)
                setattr(value, "a", self)

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_C__c", None)
        self.__c = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Adown"):
                opp_val = getattr(old_value, "Adown", None)
                if opp_val == self:
                    setattr(old_value, "Adown", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Adown"):
                opp_val = getattr(value, "Adown", None)
                setattr(value, "Adown", self)

class test_B:

    def __init__(self, newAttribute: str, test_B: "test_Adown" = None):
        self.newAttribute = newAttribute
        self.test_B = test_B
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def test_B(self):
        return self.__test_B

    @test_B.setter
    def test_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_B__test_B", None)
        self.__test_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Adown"):
                opp_val = getattr(old_value, "test_Adown", None)
                if opp_val == self:
                    setattr(old_value, "test_Adown", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Adown"):
                opp_val = getattr(value, "test_Adown", None)
                setattr(value, "test_Adown", self)

class E:

    pass
class test_Adown(E):

    def __init__(self, newAttribute: str, Adown: "test_C" = None, test_Adown: "test_B" = None, a: "test_C" = None, test_Adown3: set["test_D"] = None):
        self.newAttribute = newAttribute
        self.Adown = Adown
        self.test_Adown = test_Adown
        self.a = a
        self.test_Adown3 = test_Adown3 if test_Adown3 is not None else set()
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Adown__a", None)
        self.__a = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C"):
                opp_val = getattr(old_value, "C", None)
                if opp_val == self:
                    setattr(old_value, "C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C"):
                opp_val = getattr(value, "C", None)
                setattr(value, "C", self)

    @property
    def Adown(self):
        return self.__Adown

    @Adown.setter
    def Adown(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Adown__Adown", None)
        self.__Adown = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c"):
                opp_val = getattr(old_value, "c", None)
                if opp_val == self:
                    setattr(old_value, "c", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c"):
                opp_val = getattr(value, "c", None)
                setattr(value, "c", self)

    @property
    def test_Adown(self):
        return self.__test_Adown

    @test_Adown.setter
    def test_Adown(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Adown__test_Adown", None)
        self.__test_Adown = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_B"):
                opp_val = getattr(old_value, "test_B", None)
                if opp_val == self:
                    setattr(old_value, "test_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_B"):
                opp_val = getattr(value, "test_B", None)
                setattr(value, "test_B", self)

    @property
    def test_Adown3(self):
        return self.__test_Adown3

    @test_Adown3.setter
    def test_Adown3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Adown__test_Adown3", None)
        self.__test_Adown3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_D"):
                    opp_val = getattr(item, "test_D", None)
                    
                    if opp_val == self:
                        setattr(item, "test_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_D"):
                    opp_val = getattr(item, "test_D", None)
                    
                    setattr(item, "test_D", self)
                    
