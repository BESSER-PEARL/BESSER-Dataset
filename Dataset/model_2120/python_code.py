from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bug287941TestModel_Test2:

    pass
class bug287941TestModel_Test:

    def __init__(self, testAttr: str, bug287941TestModel_Test: "bug287941TestModel_Test2" = None):
        self.testAttr = testAttr
        self.bug287941TestModel_Test = bug287941TestModel_Test
        
    @property
    def testAttr(self) -> str:
        return self.__testAttr

    @testAttr.setter
    def testAttr(self, testAttr: str):
        self.__testAttr = testAttr

    @property
    def bug287941TestModel_Test(self):
        return self.__bug287941TestModel_Test

    @bug287941TestModel_Test.setter
    def bug287941TestModel_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bug287941TestModel_Test__bug287941TestModel_Test", None)
        self.__bug287941TestModel_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bug287941TestModel_Test2"):
                opp_val = getattr(old_value, "bug287941TestModel_Test2", None)
                if opp_val == self:
                    setattr(old_value, "bug287941TestModel_Test2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bug287941TestModel_Test2"):
                opp_val = getattr(value, "bug287941TestModel_Test2", None)
                setattr(value, "bug287941TestModel_Test2", self)
