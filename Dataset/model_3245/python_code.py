from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResourceType(Enum):
    cpu = "cpu"
    memory = "memory"
    bandwidth = "bandwidth"
    power = "power"
    port = "port"
class ConstraintOperation(Enum):
    Less = "Less"
    LessOrEqual = "LessOrEqual"
    Equal = "Equal"
    GreaterOrEqual = "GreaterOrEqual"
    Greater = "Greater"
class ConstraintType(Enum):
    Minimum = "Minimum"
    Maximum = "Maximum"
    Average = "Average"


############################################
# Definition of Classes
############################################

class profile_Constraint:

    def __init__(self, type: str, isDerivation: bool, operation: str, bound: int, profile_Constraint4: "profile_Resource" = None, profile_Constraint: "profile_PlatformProfile" = None):
        self.type = type
        self.isDerivation = isDerivation
        self.operation = operation
        self.bound = bound
        self.profile_Constraint4 = profile_Constraint4
        self.profile_Constraint = profile_Constraint
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def isDerivation(self) -> bool:
        return self.__isDerivation

    @isDerivation.setter
    def isDerivation(self, isDerivation: bool):
        self.__isDerivation = isDerivation

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def profile_Constraint(self):
        return self.__profile_Constraint

    @profile_Constraint.setter
    def profile_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Constraint__profile_Constraint", None)
        self.__profile_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_PlatformProfile2"):
                opp_val = getattr(old_value, "profile_PlatformProfile2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_PlatformProfile2"):
                opp_val = getattr(value, "profile_PlatformProfile2", None)
                if opp_val is None:
                    setattr(value, "profile_PlatformProfile2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def profile_Constraint4(self):
        return self.__profile_Constraint4

    @profile_Constraint4.setter
    def profile_Constraint4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Constraint__profile_Constraint4", None)
        self.__profile_Constraint4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Resource5"):
                opp_val = getattr(old_value, "profile_Resource5", None)
                if opp_val == self:
                    setattr(old_value, "profile_Resource5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Resource5"):
                opp_val = getattr(value, "profile_Resource5", None)
                setattr(value, "profile_Resource5", self)

class profile_Resource:

    def __init__(self, name: str, type: str, weight: int, profile_Resource5: "profile_Constraint" = None, profile_Resource: "profile_PlatformProfile" = None):
        self.name = name
        self.type = type
        self.weight = weight
        self.profile_Resource5 = profile_Resource5
        self.profile_Resource = profile_Resource
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def profile_Resource5(self):
        return self.__profile_Resource5

    @profile_Resource5.setter
    def profile_Resource5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Resource__profile_Resource5", None)
        self.__profile_Resource5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Constraint4"):
                opp_val = getattr(old_value, "profile_Constraint4", None)
                if opp_val == self:
                    setattr(old_value, "profile_Constraint4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Constraint4"):
                opp_val = getattr(value, "profile_Constraint4", None)
                setattr(value, "profile_Constraint4", self)

    @property
    def profile_Resource(self):
        return self.__profile_Resource

    @profile_Resource.setter
    def profile_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Resource__profile_Resource", None)
        self.__profile_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_PlatformProfile"):
                opp_val = getattr(old_value, "profile_PlatformProfile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_PlatformProfile"):
                opp_val = getattr(value, "profile_PlatformProfile", None)
                if opp_val is None:
                    setattr(value, "profile_PlatformProfile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class profile_PlatformProfile:

    def __init__(self, name: str, profile_PlatformProfile: set["profile_Resource"] = None, profile_PlatformProfile2: set["profile_Constraint"] = None):
        self.name = name
        self.profile_PlatformProfile = profile_PlatformProfile if profile_PlatformProfile is not None else set()
        self.profile_PlatformProfile2 = profile_PlatformProfile2 if profile_PlatformProfile2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def profile_PlatformProfile2(self):
        return self.__profile_PlatformProfile2

    @profile_PlatformProfile2.setter
    def profile_PlatformProfile2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__profile_PlatformProfile2", None)
        self.__profile_PlatformProfile2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile_Constraint"):
                    opp_val = getattr(item, "profile_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "profile_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile_Constraint"):
                    opp_val = getattr(item, "profile_Constraint", None)
                    
                    setattr(item, "profile_Constraint", self)
                    

    @property
    def profile_PlatformProfile(self):
        return self.__profile_PlatformProfile

    @profile_PlatformProfile.setter
    def profile_PlatformProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__profile_PlatformProfile", None)
        self.__profile_PlatformProfile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile_Resource"):
                    opp_val = getattr(item, "profile_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "profile_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile_Resource"):
                    opp_val = getattr(item, "profile_Resource", None)
                    
                    setattr(item, "profile_Resource", self)
                    
