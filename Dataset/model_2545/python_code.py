from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testmerge_F:

    pass
class testmerge_E:

    pass
class testmerge_C:

    def __init__(self, dataType: str, 1: "testmerge_D" = None, 3: "testmerge_D" = None, testmerge_C: set["testmerge_E"] = None, testmerge_C7: set["testmerge_F"] = None):
        self.dataType = dataType
        self.1 = 1
        self.3 = 3
        self.testmerge_C = testmerge_C if testmerge_C is not None else set()
        self.testmerge_C7 = testmerge_C7 if testmerge_C7 is not None else set()
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__3", None)
        self.__3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "4"):
                opp_val = getattr(old_value, "4", None)
                if opp_val == self:
                    setattr(old_value, "4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "4"):
                opp_val = getattr(value, "4", None)
                setattr(value, "4", self)

    @property
    def testmerge_C(self):
        return self.__testmerge_C

    @testmerge_C.setter
    def testmerge_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__testmerge_C", None)
        self.__testmerge_C = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmerge_E"):
                    opp_val = getattr(item, "testmerge_E", None)
                    
                    if opp_val == self:
                        setattr(item, "testmerge_E", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmerge_E"):
                    opp_val = getattr(item, "testmerge_E", None)
                    
                    setattr(item, "testmerge_E", self)
                    

    @property
    def testmerge_C7(self):
        return self.__testmerge_C7

    @testmerge_C7.setter
    def testmerge_C7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__testmerge_C7", None)
        self.__testmerge_C7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmerge_F"):
                    opp_val = getattr(item, "testmerge_F", None)
                    
                    if opp_val == self:
                        setattr(item, "testmerge_F", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmerge_F"):
                    opp_val = getattr(item, "testmerge_F", None)
                    
                    setattr(item, "testmerge_F", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

class testmerge_D:

    def __init__(self, emfDataType: str, : "testmerge_C" = None, 4: "testmerge_C" = None):
        self.emfDataType = emfDataType
        self. = 
        self.4 = 4
        
    @property
    def emfDataType(self) -> str:
        return self.__emfDataType

    @emfDataType.setter
    def emfDataType(self, emfDataType: str):
        self.__emfDataType = emfDataType

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_D__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "1"):
                opp_val = getattr(old_value, "1", None)
                if opp_val == self:
                    setattr(old_value, "1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "1"):
                opp_val = getattr(value, "1", None)
                setattr(value, "1", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_D__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if opp_val == self:
                    setattr(old_value, "3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                setattr(value, "3", self)
