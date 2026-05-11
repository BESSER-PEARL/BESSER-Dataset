from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testmerge_F:

    pass
class testmerge_E:

    pass
class testmerge_C:

    def __init__(self, dataType: str, C: "testmerge_D" = None, toC: "testmerge_D" = None, testmerge_C: set["testmerge_E"] = None, testmerge_C4: set["testmerge_F"] = None):
        self.dataType = dataType
        self.C = C
        self.toC = toC
        self.testmerge_C = testmerge_C if testmerge_C is not None else set()
        self.testmerge_C4 = testmerge_C4 if testmerge_C4 is not None else set()
        
        pass
    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


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
    def toC(self):
        return self.__toC

    @toC.setter
    def toC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__toC", None)
        self.__toC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "D"):
                opp_val = getattr(old_value, "D", None)
                if opp_val == self:
                    setattr(old_value, "D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "D"):
                opp_val = getattr(value, "D", None)
                setattr(value, "D", self)

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__C", None)
        self.__C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toD"):
                opp_val = getattr(old_value, "toD", None)
                if opp_val == self:
                    setattr(old_value, "toD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toD"):
                opp_val = getattr(value, "toD", None)
                setattr(value, "toD", self)

    @property
    def testmerge_C4(self):
        return self.__testmerge_C4

    @testmerge_C4.setter
    def testmerge_C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_C__testmerge_C4", None)
        self.__testmerge_C4 = value if value is not None else set()
        
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
                    

class testmerge_D:

    def __init__(self, emfDataType: str, toD: "testmerge_C" = None, D: "testmerge_C" = None):
        self.emfDataType = emfDataType
        self.toD = toD
        self.D = D
        
        pass
    @property
    def emfDataType(self):
        return self.__emfDataType

    @emfDataType.setter
    def emfDataType(self, emfDataType: str):
        self.__emfDataType = emfDataType


    @property
    def D(self):
        return self.__D

    @D.setter
    def D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_D__D", None)
        self.__D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toC"):
                opp_val = getattr(old_value, "toC", None)
                if opp_val == self:
                    setattr(old_value, "toC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toC"):
                opp_val = getattr(value, "toC", None)
                setattr(value, "toC", self)

    @property
    def toD(self):
        return self.__toD

    @toD.setter
    def toD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_D__toD", None)
        self.__toD = value
        
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
