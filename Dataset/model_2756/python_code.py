from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_A:

    def __init__(self, listen: int, test_A4: set["test_B"] = None, test_A: "test_Compo" = None):
        self.listen = listen
        self.test_A4 = test_A4 if test_A4 is not None else set()
        self.test_A = test_A
        
    @property
    def listen(self) -> int:
        return self.__listen

    @listen.setter
    def listen(self, listen: int):
        self.__listen = listen

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
            if hasattr(old_value, "test_Compo2"):
                opp_val = getattr(old_value, "test_Compo2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Compo2"):
                opp_val = getattr(value, "test_Compo2", None)
                if opp_val is None:
                    setattr(value, "test_Compo2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_A4(self):
        return self.__test_A4

    @test_A4.setter
    def test_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_A__test_A4", None)
        self.__test_A4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_B5"):
                    opp_val = getattr(item, "test_B5", None)
                    
                    if opp_val == self:
                        setattr(item, "test_B5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_B5"):
                    opp_val = getattr(item, "test_B5", None)
                    
                    setattr(item, "test_B5", self)
                    

class test_B:

    def __init__(self, name: str, test_B5: "test_A" = None, test_B: "test_Compo" = None):
        self.name = name
        self.test_B5 = test_B5
        self.test_B = test_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "test_Compo"):
                opp_val = getattr(old_value, "test_Compo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Compo"):
                opp_val = getattr(value, "test_Compo", None)
                if opp_val is None:
                    setattr(value, "test_Compo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_B5(self):
        return self.__test_B5

    @test_B5.setter
    def test_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_B__test_B5", None)
        self.__test_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_A4"):
                opp_val = getattr(old_value, "test_A4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_A4"):
                opp_val = getattr(value, "test_A4", None)
                if opp_val is None:
                    setattr(value, "test_A4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Compo:

    pass