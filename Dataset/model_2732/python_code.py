from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testmerge_B:

    def __init__(self, anAttribute: str, 3: "testmerge_A" = None, 1: "testmerge_A" = None):
        self.anAttribute = anAttribute
        self.3 = 3
        self.1 = 1
        
    @property
    def anAttribute(self) -> str:
        return self.__anAttribute

    @anAttribute.setter
    def anAttribute(self, anAttribute: str):
        self.__anAttribute = anAttribute

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_B__3", None)
        self.__3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "4"):
                opp_val = getattr(old_value, "4", None)
                if opp_val == self:
                    setattr(old_value, "4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "4"):
                opp_val = getattr(value, "4", None)
                setattr(value, "4", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmerge_B__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    def getA(self, paramB: str) -> str:
        # TODO: Implement getA method
        pass

class B:

    pass
class testmerge_SubB(B):

    pass
class testmerge_SuperA:

    pass
class AA:

    pass
class testmerge_AAA(AA):

    pass
class A:

    pass
class testmerge_AA(A):

    pass
class testmerge_C:

    pass
class SuperA:

    pass
class testmerge_A(SuperA):

    pass