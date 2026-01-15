from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class ResourceTypes(Enum):
    cpu = "cpu"
    memory = "memory"
    bandwidth = "bandwidth"
    power = "power"
    port = "port"


############################################
# Definition of Classes
############################################

class profile_Constraint:

    def __init__(self, isDerivation: bool, type: str, operation: str, bound: int, Constraint: "profile_PlatformProfile" = None, constraints: "profile_PlatformProfile" = None, profile_Constraint: "profile_Resource" = None):
        self.isDerivation = isDerivation
        self.type = type
        self.operation = operation
        self.bound = bound
        self.Constraint = Constraint
        self.constraints = constraints
        self.profile_Constraint = profile_Constraint
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def isDerivation(self) -> bool:
        return self.__isDerivation

    @isDerivation.setter
    def isDerivation(self, isDerivation: bool):
        self.__isDerivation = isDerivation

    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Constraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PlatformProfile5"):
                opp_val = getattr(old_value, "PlatformProfile5", None)
                if opp_val == self:
                    setattr(old_value, "PlatformProfile5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PlatformProfile5"):
                opp_val = getattr(value, "PlatformProfile5", None)
                setattr(value, "PlatformProfile5", self)

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Constraint__Constraint", None)
        self.__Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platform2"):
                opp_val = getattr(old_value, "platform2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platform2"):
                opp_val = getattr(value, "platform2", None)
                if opp_val is None:
                    setattr(value, "platform2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "profile_Resource"):
                opp_val = getattr(old_value, "profile_Resource", None)
                if opp_val == self:
                    setattr(old_value, "profile_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Resource"):
                opp_val = getattr(value, "profile_Resource", None)
                setattr(value, "profile_Resource", self)

class profile_Resource:

    def __init__(self, name: str, type: str, Resource: "profile_PlatformProfile" = None, resources: "profile_PlatformProfile" = None, profile_Resource: "profile_Constraint" = None):
        self.name = name
        self.type = type
        self.Resource = Resource
        self.resources = resources
        self.profile_Resource = profile_Resource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Resource__Resource", None)
        self.__Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platform"):
                opp_val = getattr(old_value, "platform", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platform"):
                opp_val = getattr(value, "platform", None)
                if opp_val is None:
                    setattr(value, "platform", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_Resource__resources", None)
        self.__resources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PlatformProfile"):
                opp_val = getattr(old_value, "PlatformProfile", None)
                if opp_val == self:
                    setattr(old_value, "PlatformProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PlatformProfile"):
                opp_val = getattr(value, "PlatformProfile", None)
                setattr(value, "PlatformProfile", self)

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
            if hasattr(old_value, "profile_Constraint"):
                opp_val = getattr(old_value, "profile_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "profile_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Constraint"):
                opp_val = getattr(value, "profile_Constraint", None)
                setattr(value, "profile_Constraint", self)

class profile_PlatformProfile:

    def __init__(self, name: str, platform: set["profile_Resource"] = None, platform2: set["profile_Constraint"] = None, PlatformProfile: "profile_Resource" = None, PlatformProfile5: "profile_Constraint" = None):
        self.name = name
        self.platform = platform if platform is not None else set()
        self.platform2 = platform2 if platform2 is not None else set()
        self.PlatformProfile = PlatformProfile
        self.PlatformProfile5 = PlatformProfile5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def platform2(self):
        return self.__platform2

    @platform2.setter
    def platform2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__platform2", None)
        self.__platform2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def PlatformProfile5(self):
        return self.__PlatformProfile5

    @PlatformProfile5.setter
    def PlatformProfile5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__PlatformProfile5", None)
        self.__PlatformProfile5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraints"):
                opp_val = getattr(old_value, "constraints", None)
                if opp_val == self:
                    setattr(old_value, "constraints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraints"):
                opp_val = getattr(value, "constraints", None)
                setattr(value, "constraints", self)

    @property
    def PlatformProfile(self):
        return self.__PlatformProfile

    @PlatformProfile.setter
    def PlatformProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__PlatformProfile", None)
        self.__PlatformProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources"):
                opp_val = getattr(old_value, "resources", None)
                if opp_val == self:
                    setattr(old_value, "resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources"):
                opp_val = getattr(value, "resources", None)
                setattr(value, "resources", self)

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_PlatformProfile__platform", None)
        self.__platform = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    
