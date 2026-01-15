from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_Bar:

    def __init__(self, barA: str, test_Bar: "test_Container" = None, test_Bar4: "test_Foo" = None):
        self.barA = barA
        self.test_Bar = test_Bar
        self.test_Bar4 = test_Bar4
        
    @property
    def barA(self) -> str:
        return self.__barA

    @barA.setter
    def barA(self, barA: str):
        self.__barA = barA

    @property
    def test_Bar4(self):
        return self.__test_Bar4

    @test_Bar4.setter
    def test_Bar4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Bar__test_Bar4", None)
        self.__test_Bar4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Foo5"):
                opp_val = getattr(old_value, "test_Foo5", None)
                if opp_val == self:
                    setattr(old_value, "test_Foo5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Foo5"):
                opp_val = getattr(value, "test_Foo5", None)
                setattr(value, "test_Foo5", self)

    @property
    def test_Bar(self):
        return self.__test_Bar

    @test_Bar.setter
    def test_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Bar__test_Bar", None)
        self.__test_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Container2"):
                opp_val = getattr(old_value, "test_Container2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Container2"):
                opp_val = getattr(value, "test_Container2", None)
                if opp_val is None:
                    setattr(value, "test_Container2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Foo:

    def __init__(self, fooA: str, test_Foo: "test_Container" = None, test_Foo5: "test_Bar" = None):
        self.fooA = fooA
        self.test_Foo = test_Foo
        self.test_Foo5 = test_Foo5
        
    @property
    def fooA(self) -> str:
        return self.__fooA

    @fooA.setter
    def fooA(self, fooA: str):
        self.__fooA = fooA

    @property
    def test_Foo5(self):
        return self.__test_Foo5

    @test_Foo5.setter
    def test_Foo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Foo__test_Foo5", None)
        self.__test_Foo5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Bar4"):
                opp_val = getattr(old_value, "test_Bar4", None)
                if opp_val == self:
                    setattr(old_value, "test_Bar4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Bar4"):
                opp_val = getattr(value, "test_Bar4", None)
                setattr(value, "test_Bar4", self)

    @property
    def test_Foo(self):
        return self.__test_Foo

    @test_Foo.setter
    def test_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Foo__test_Foo", None)
        self.__test_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Container"):
                opp_val = getattr(old_value, "test_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Container"):
                opp_val = getattr(value, "test_Container", None)
                if opp_val is None:
                    setattr(value, "test_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Container:

    pass