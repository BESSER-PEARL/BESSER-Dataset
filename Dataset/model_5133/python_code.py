from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TestMerge_B:

    pass
class TestMerge_A:

    def __init__(self, attr1: str, TestMerge_A: "TestMerge_B" = None):
        self.attr1 = attr1
        self.TestMerge_A = TestMerge_A
        
    @property
    def attr1(self) -> str:
        return self.__attr1

    @attr1.setter
    def attr1(self, attr1: str):
        self.__attr1 = attr1

    @property
    def TestMerge_A(self):
        return self.__TestMerge_A

    @TestMerge_A.setter
    def TestMerge_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestMerge_A__TestMerge_A", None)
        self.__TestMerge_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestMerge_B"):
                opp_val = getattr(old_value, "TestMerge_B", None)
                if opp_val == self:
                    setattr(old_value, "TestMerge_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestMerge_B"):
                opp_val = getattr(value, "TestMerge_B", None)
                setattr(value, "TestMerge_B", self)
