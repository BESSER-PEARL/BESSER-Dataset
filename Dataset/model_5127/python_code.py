from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataValue:

    pass
class NamedElement:

    pass
class xunit_TestSuite(NamedElement):

    pass
class xunit_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class xunit_DataValue:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class xunit_Action:

    def __init__(self, desc: str, xunit_Action: "xunit_Assertion" = None):
        self.desc = desc
        self.xunit_Action = xunit_Action
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def xunit_Action(self):
        return self.__xunit_Action

    @xunit_Action.setter
    def xunit_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Action__xunit_Action", None)
        self.__xunit_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_Assertion9"):
                opp_val = getattr(old_value, "xunit_Assertion9", None)
                if opp_val == self:
                    setattr(old_value, "xunit_Assertion9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_Assertion9"):
                opp_val = getattr(value, "xunit_Assertion9", None)
                setattr(value, "xunit_Assertion9", self)

class xunit_ExpectedValue(DataValue):

    pass
class xunit_Assertion(NamedElement):

    def __init__(self, type: str, xunit_Assertion: "xunit_TestCase" = None, xunit_Assertion7: "xunit_ExpectedValue" = None, xunit_Assertion9: "xunit_Action" = None, xunit_Assertion11: "xunit_TestCase" = None, xunit_Assertion15: "xunit_ExpectedValue" = None):
        self.type = type
        self.xunit_Assertion = xunit_Assertion
        self.xunit_Assertion7 = xunit_Assertion7
        self.xunit_Assertion9 = xunit_Assertion9
        self.xunit_Assertion11 = xunit_Assertion11
        self.xunit_Assertion15 = xunit_Assertion15
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xunit_Assertion9(self):
        return self.__xunit_Assertion9

    @xunit_Assertion9.setter
    def xunit_Assertion9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Assertion__xunit_Assertion9", None)
        self.__xunit_Assertion9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_Action"):
                opp_val = getattr(old_value, "xunit_Action", None)
                if opp_val == self:
                    setattr(old_value, "xunit_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_Action"):
                opp_val = getattr(value, "xunit_Action", None)
                setattr(value, "xunit_Action", self)

    @property
    def xunit_Assertion15(self):
        return self.__xunit_Assertion15

    @xunit_Assertion15.setter
    def xunit_Assertion15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Assertion__xunit_Assertion15", None)
        self.__xunit_Assertion15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_ExpectedValue14"):
                opp_val = getattr(old_value, "xunit_ExpectedValue14", None)
                if opp_val == self:
                    setattr(old_value, "xunit_ExpectedValue14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_ExpectedValue14"):
                opp_val = getattr(value, "xunit_ExpectedValue14", None)
                setattr(value, "xunit_ExpectedValue14", self)

    @property
    def xunit_Assertion(self):
        return self.__xunit_Assertion

    @xunit_Assertion.setter
    def xunit_Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Assertion__xunit_Assertion", None)
        self.__xunit_Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_TestCase2"):
                opp_val = getattr(old_value, "xunit_TestCase2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_TestCase2"):
                opp_val = getattr(value, "xunit_TestCase2", None)
                if opp_val is None:
                    setattr(value, "xunit_TestCase2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xunit_Assertion7(self):
        return self.__xunit_Assertion7

    @xunit_Assertion7.setter
    def xunit_Assertion7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Assertion__xunit_Assertion7", None)
        self.__xunit_Assertion7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_ExpectedValue"):
                opp_val = getattr(old_value, "xunit_ExpectedValue", None)
                if opp_val == self:
                    setattr(old_value, "xunit_ExpectedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_ExpectedValue"):
                opp_val = getattr(value, "xunit_ExpectedValue", None)
                setattr(value, "xunit_ExpectedValue", self)

    @property
    def xunit_Assertion11(self):
        return self.__xunit_Assertion11

    @xunit_Assertion11.setter
    def xunit_Assertion11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xunit_Assertion__xunit_Assertion11", None)
        self.__xunit_Assertion11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xunit_TestCase12"):
                opp_val = getattr(old_value, "xunit_TestCase12", None)
                if opp_val == self:
                    setattr(old_value, "xunit_TestCase12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xunit_TestCase12"):
                opp_val = getattr(value, "xunit_TestCase12", None)
                setattr(value, "xunit_TestCase12", self)

class xunit_TestCase(NamedElement):

    pass