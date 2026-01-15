from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RootEnum(Enum):
    literal = "literal"
class NoLitEnum(Enum):
    literal = "literal"


############################################
# Definition of Classes
############################################

class root_noLiterals_NoLitClass:

    def __init__(self, attribute2: str, root_noLiterals_NoLitClass: "NestedClass1" = None):
        self.attribute2 = attribute2
        self.root_noLiterals_NoLitClass = root_noLiterals_NoLitClass
        
    @property
    def attribute2(self) -> str:
        return self.__attribute2

    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def root_noLiterals_NoLitClass(self):
        return self.__root_noLiterals_NoLitClass

    @root_noLiterals_NoLitClass.setter
    def root_noLiterals_NoLitClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_root_noLiterals_NoLitClass__root_noLiterals_NoLitClass", None)
        self.__root_noLiterals_NoLitClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NestedClass12"):
                opp_val = getattr(old_value, "NestedClass12", None)
                if opp_val == self:
                    setattr(old_value, "NestedClass12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NestedClass12"):
                opp_val = getattr(value, "NestedClass12", None)
                setattr(value, "NestedClass12", self)

class root_nestedPackage1_NestedClass1:

    pass
class NestedClass1:

    pass
class root_RootClass:

    def __init__(self, attribute1: str, root_RootClass: "NestedClass1" = None):
        self.attribute1 = attribute1
        self.root_RootClass = root_RootClass
        
    @property
    def attribute1(self) -> str:
        return self.__attribute1

    @attribute1.setter
    def attribute1(self, attribute1: str):
        self.__attribute1 = attribute1

    @property
    def root_RootClass(self):
        return self.__root_RootClass

    @root_RootClass.setter
    def root_RootClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_root_RootClass__root_RootClass", None)
        self.__root_RootClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NestedClass1"):
                opp_val = getattr(old_value, "NestedClass1", None)
                if opp_val == self:
                    setattr(old_value, "NestedClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NestedClass1"):
                opp_val = getattr(value, "NestedClass1", None)
                setattr(value, "NestedClass1", self)
