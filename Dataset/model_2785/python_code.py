from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testModel_EObject:

    pass
class BClass:

    pass
class testModel_CClass(BClass):

    def __init__(self, CClassAttr1: bool, CClassAttr2: str, testModel_CClass: "testModel_BClass" = None, testModel_CClass4: "testModel_EObject" = None):
        self.CClassAttr1 = CClassAttr1
        self.CClassAttr2 = CClassAttr2
        self.testModel_CClass = testModel_CClass
        self.testModel_CClass4 = testModel_CClass4
        
    @property
    def CClassAttr2(self) -> str:
        return self.__CClassAttr2

    @CClassAttr2.setter
    def CClassAttr2(self, CClassAttr2: str):
        self.__CClassAttr2 = CClassAttr2

    @property
    def CClassAttr1(self) -> bool:
        return self.__CClassAttr1

    @CClassAttr1.setter
    def CClassAttr1(self, CClassAttr1: bool):
        self.__CClassAttr1 = CClassAttr1

    @property
    def testModel_CClass4(self):
        return self.__testModel_CClass4

    @testModel_CClass4.setter
    def testModel_CClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_CClass__testModel_CClass4", None)
        self.__testModel_CClass4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_EObject"):
                opp_val = getattr(old_value, "testModel_EObject", None)
                if opp_val == self:
                    setattr(old_value, "testModel_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_EObject"):
                opp_val = getattr(value, "testModel_EObject", None)
                setattr(value, "testModel_EObject", self)

    @property
    def testModel_CClass(self):
        return self.__testModel_CClass

    @testModel_CClass.setter
    def testModel_CClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_CClass__testModel_CClass", None)
        self.__testModel_CClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_BClass2"):
                opp_val = getattr(old_value, "testModel_BClass2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_BClass2"):
                opp_val = getattr(value, "testModel_BClass2", None)
                if opp_val is None:
                    setattr(value, "testModel_BClass2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AClass:

    pass
class testModel_BClass(AClass):

    def __init__(self, BClassAttr1: bool, BClassAttr2: str, testModel_BClass: "testModel_AClass" = None, testModel_BClass2: set["testModel_CClass"] = None):
        self.BClassAttr1 = BClassAttr1
        self.BClassAttr2 = BClassAttr2
        self.testModel_BClass = testModel_BClass
        self.testModel_BClass2 = testModel_BClass2 if testModel_BClass2 is not None else set()
        
    @property
    def BClassAttr2(self) -> str:
        return self.__BClassAttr2

    @BClassAttr2.setter
    def BClassAttr2(self, BClassAttr2: str):
        self.__BClassAttr2 = BClassAttr2

    @property
    def BClassAttr1(self) -> bool:
        return self.__BClassAttr1

    @BClassAttr1.setter
    def BClassAttr1(self, BClassAttr1: bool):
        self.__BClassAttr1 = BClassAttr1

    @property
    def testModel_BClass2(self):
        return self.__testModel_BClass2

    @testModel_BClass2.setter
    def testModel_BClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_BClass__testModel_BClass2", None)
        self.__testModel_BClass2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_CClass"):
                    opp_val = getattr(item, "testModel_CClass", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_CClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_CClass"):
                    opp_val = getattr(item, "testModel_CClass", None)
                    
                    setattr(item, "testModel_CClass", self)
                    

    @property
    def testModel_BClass(self):
        return self.__testModel_BClass

    @testModel_BClass.setter
    def testModel_BClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_BClass__testModel_BClass", None)
        self.__testModel_BClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_AClass"):
                opp_val = getattr(old_value, "testModel_AClass", None)
                if opp_val == self:
                    setattr(old_value, "testModel_AClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_AClass"):
                opp_val = getattr(value, "testModel_AClass", None)
                setattr(value, "testModel_AClass", self)

class testModel_AClass:

    def __init__(self, AClassAttr1: bool, AClassAttr2: str, testModel_AClass: "testModel_BClass" = None):
        self.AClassAttr1 = AClassAttr1
        self.AClassAttr2 = AClassAttr2
        self.testModel_AClass = testModel_AClass
        
    @property
    def AClassAttr1(self) -> bool:
        return self.__AClassAttr1

    @AClassAttr1.setter
    def AClassAttr1(self, AClassAttr1: bool):
        self.__AClassAttr1 = AClassAttr1

    @property
    def AClassAttr2(self) -> str:
        return self.__AClassAttr2

    @AClassAttr2.setter
    def AClassAttr2(self, AClassAttr2: str):
        self.__AClassAttr2 = AClassAttr2

    @property
    def testModel_AClass(self):
        return self.__testModel_AClass

    @testModel_AClass.setter
    def testModel_AClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_AClass__testModel_AClass", None)
        self.__testModel_AClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_BClass"):
                opp_val = getattr(old_value, "testModel_BClass", None)
                if opp_val == self:
                    setattr(old_value, "testModel_BClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_BClass"):
                opp_val = getattr(value, "testModel_BClass", None)
                setattr(value, "testModel_BClass", self)
