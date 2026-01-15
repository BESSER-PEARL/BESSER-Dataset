from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_C:

    pass
class test_B:

    def __init__(self, b: str, test_B: "test_A" = None):
        self.b = b
        self.test_B = test_B
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

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
            if hasattr(old_value, "test_A"):
                opp_val = getattr(old_value, "test_A", None)
                if opp_val == self:
                    setattr(old_value, "test_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_A"):
                opp_val = getattr(value, "test_A", None)
                setattr(value, "test_A", self)

class test_A:

    def __init__(self, a: str, test_A: "test_B" = None):
        self.a = a
        self.test_A = test_A
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def test_A(self):
        return self.__test_A

    @test_A.setter
    def test_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_A__test_A", None)
        self.__test_A = value
        
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
