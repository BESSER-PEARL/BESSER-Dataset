from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testup_G:

    pass
class G:

    pass
class E:

    pass
class testup_F(G, E):

    pass
class AUp:

    pass
class testup_E(AUp):

    def __init__(self, newAttribute: str):
        self.newAttribute = newAttribute
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

class testup_D:

    def __init__(self, newAttribute: str, testup_D: set["testup_AUp"] = None):
        self.newAttribute = newAttribute
        self.testup_D = testup_D if testup_D is not None else set()
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def testup_D(self):
        return self.__testup_D

    @testup_D.setter
    def testup_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testup_D__testup_D", None)
        self.__testup_D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testup_AUp2"):
                    opp_val = getattr(item, "testup_AUp2", None)
                    
                    if opp_val == self:
                        setattr(item, "testup_AUp2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testup_AUp2"):
                    opp_val = getattr(item, "testup_AUp2", None)
                    
                    setattr(item, "testup_AUp2", self)
                    

class testup_B:

    def __init__(self, newAttribute: str, testup_B: "testup_AUp" = None):
        self.newAttribute = newAttribute
        self.testup_B = testup_B
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def testup_B(self):
        return self.__testup_B

    @testup_B.setter
    def testup_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testup_B__testup_B", None)
        self.__testup_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testup_AUp"):
                opp_val = getattr(old_value, "testup_AUp", None)
                if opp_val == self:
                    setattr(old_value, "testup_AUp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testup_AUp"):
                opp_val = getattr(value, "testup_AUp", None)
                setattr(value, "testup_AUp", self)

class testup_AUp:

    pass