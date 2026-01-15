from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testPackage_TestElementA:

    def __init__(self, multi: int, name: str, testPackage_TestElementA: "testPackage_Container" = None, testPackage_TestElementA2: "testPackage_TestElementB" = None):
        self.multi = multi
        self.name = name
        self.testPackage_TestElementA = testPackage_TestElementA
        self.testPackage_TestElementA2 = testPackage_TestElementA2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multi(self) -> int:
        return self.__multi

    @multi.setter
    def multi(self, multi: int):
        self.__multi = multi

    @property
    def testPackage_TestElementA(self):
        return self.__testPackage_TestElementA

    @testPackage_TestElementA.setter
    def testPackage_TestElementA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testPackage_TestElementA__testPackage_TestElementA", None)
        self.__testPackage_TestElementA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testPackage_Container"):
                opp_val = getattr(old_value, "testPackage_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testPackage_Container"):
                opp_val = getattr(value, "testPackage_Container", None)
                if opp_val is None:
                    setattr(value, "testPackage_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testPackage_TestElementA2(self):
        return self.__testPackage_TestElementA2

    @testPackage_TestElementA2.setter
    def testPackage_TestElementA2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testPackage_TestElementA__testPackage_TestElementA2", None)
        self.__testPackage_TestElementA2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testPackage_TestElementB"):
                opp_val = getattr(old_value, "testPackage_TestElementB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testPackage_TestElementB"):
                opp_val = getattr(value, "testPackage_TestElementB", None)
                if opp_val is None:
                    setattr(value, "testPackage_TestElementB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TestElementA:

    pass
class testPackage_TestElementB(TestElementA):

    pass
class testPackage_Container:

    pass