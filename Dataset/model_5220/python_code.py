from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class anytype_A:

    def __init__(self, name: str, doub: str, lon: str, anytype_A: "anytype_B" = None):
        self.name = name
        self.doub = doub
        self.lon = lon
        self.anytype_A = anytype_A
        
    @property
    def lon(self) -> str:
        return self.__lon

    @lon.setter
    def lon(self, lon: str):
        self.__lon = lon

    @property
    def doub(self) -> str:
        return self.__doub

    @doub.setter
    def doub(self, doub: str):
        self.__doub = doub

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anytype_A(self):
        return self.__anytype_A

    @anytype_A.setter
    def anytype_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anytype_A__anytype_A", None)
        self.__anytype_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anytype_B"):
                opp_val = getattr(old_value, "anytype_B", None)
                if opp_val == self:
                    setattr(old_value, "anytype_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anytype_B"):
                opp_val = getattr(value, "anytype_B", None)
                setattr(value, "anytype_B", self)

class anytype_EObject:

    pass
class anytype_TestAny:

    def __init__(self, name: str, any: str, a: str, myAny: str, anytype_TestAny: "anytype_EObject" = None, anytype_TestAny3: set["anytype_EObject"] = None):
        self.name = name
        self.any = any
        self.a = a
        self.myAny = myAny
        self.anytype_TestAny = anytype_TestAny
        self.anytype_TestAny3 = anytype_TestAny3 if anytype_TestAny3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myAny(self) -> str:
        return self.__myAny

    @myAny.setter
    def myAny(self, myAny: str):
        self.__myAny = myAny

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anytype_TestAny3(self):
        return self.__anytype_TestAny3

    @anytype_TestAny3.setter
    def anytype_TestAny3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anytype_TestAny__anytype_TestAny3", None)
        self.__anytype_TestAny3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "anytype_EObject4"):
                    opp_val = getattr(item, "anytype_EObject4", None)
                    
                    if opp_val == self:
                        setattr(item, "anytype_EObject4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "anytype_EObject4"):
                    opp_val = getattr(item, "anytype_EObject4", None)
                    
                    setattr(item, "anytype_EObject4", self)
                    

    @property
    def anytype_TestAny(self):
        return self.__anytype_TestAny

    @anytype_TestAny.setter
    def anytype_TestAny(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anytype_TestAny__anytype_TestAny", None)
        self.__anytype_TestAny = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anytype_EObject"):
                opp_val = getattr(old_value, "anytype_EObject", None)
                if opp_val == self:
                    setattr(old_value, "anytype_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anytype_EObject"):
                opp_val = getattr(value, "anytype_EObject", None)
                setattr(value, "anytype_EObject", self)

class anytype_C:

    pass
class anytype_B:

    def __init__(self, name: str, anytype_B: "anytype_A" = None):
        self.name = name
        self.anytype_B = anytype_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anytype_B(self):
        return self.__anytype_B

    @anytype_B.setter
    def anytype_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anytype_B__anytype_B", None)
        self.__anytype_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anytype_A"):
                opp_val = getattr(old_value, "anytype_A", None)
                if opp_val == self:
                    setattr(old_value, "anytype_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anytype_A"):
                opp_val = getattr(value, "anytype_A", None)
                setattr(value, "anytype_A", self)
