from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_EClass1:

    pass
class test_EClass0:

    def __init__(self, EAttribute0: bool, test_EClass0: "test_EClass1" = None):
        self.EAttribute0 = EAttribute0
        self.test_EClass0 = test_EClass0
        
    @property
    def EAttribute0(self) -> bool:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: bool):
        self.__EAttribute0 = EAttribute0

    @property
    def test_EClass0(self):
        return self.__test_EClass0

    @test_EClass0.setter
    def test_EClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass0__test_EClass0", None)
        self.__test_EClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass1"):
                opp_val = getattr(old_value, "test_EClass1", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass1"):
                opp_val = getattr(value, "test_EClass1", None)
                setattr(value, "test_EClass1", self)
