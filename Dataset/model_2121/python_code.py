from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testSuite_Test:

    def __init__(self, name: str, testSuite_Test: "testSuite_Model" = None):
        self.name = name
        self.testSuite_Test = testSuite_Test
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testSuite_Test(self):
        return self.__testSuite_Test

    @testSuite_Test.setter
    def testSuite_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testSuite_Test__testSuite_Test", None)
        self.__testSuite_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testSuite_Model"):
                opp_val = getattr(old_value, "testSuite_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testSuite_Model"):
                opp_val = getattr(value, "testSuite_Model", None)
                if opp_val is None:
                    setattr(value, "testSuite_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testSuite_Model:

    pass