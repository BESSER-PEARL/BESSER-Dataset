from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UseCases_LocationReference:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class LocationReference:

    pass
class ModelElement:

    pass
class UseCases_ExtensionPoint(ModelElement):

    pass
class UseCases_ModelElement(ABC):

    pass
class UseCases_BooleanExpression:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class BooleanExpression:

    pass
class UseCase:

    pass
class RelationShip:

    pass
class UseCases_Extend(RelationShip):

    pass
class UseCases_Include(RelationShip):

    pass
class UseCases_RelationShip(ABC):

    pass
class ExtensionPoint:

    pass
class Extend:

    pass
class Include:

    pass
class Classifier:

    pass
class UseCases_UseCase(Classifier):

    def __init__(self, extensionPoint: str, addition: "Include" = None, base: "Include" = None, extension: "Extend" = None, base7: "Extend" = None, useCase: set["ExtensionPoint"] = None, Classifier: "UseCases_Instance" = None):
        self.extensionPoint = extensionPoint
        self.addition = addition
        self.base = base
        self.extension = extension
        self.base7 = base7
        self.useCase = useCase if useCase is not None else set()
        
        pass
    @property
    def extensionPoint(self):
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, extensionPoint: str):
        self.__extensionPoint = extensionPoint


    @property
    def addition(self):
        return self.__addition

    @addition.setter
    def addition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCases_UseCase__addition", None)
        self.__addition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Include"):
                opp_val = getattr(old_value, "Include", None)
                if opp_val == self:
                    setattr(old_value, "Include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Include"):
                opp_val = getattr(value, "Include", None)
                setattr(value, "Include", self)

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCases_UseCase__extension", None)
        self.__extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Extend"):
                opp_val = getattr(old_value, "Extend", None)
                if opp_val == self:
                    setattr(old_value, "Extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Extend"):
                opp_val = getattr(value, "Extend", None)
                setattr(value, "Extend", self)

    @property
    def useCase(self):
        return self.__useCase

    @useCase.setter
    def useCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCases_UseCase__useCase", None)
        self.__useCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    setattr(item, "ExtensionPoint", self)
                    

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCases_UseCase__base", None)
        self.__base = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Include4"):
                opp_val = getattr(old_value, "Include4", None)
                if opp_val == self:
                    setattr(old_value, "Include4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Include4"):
                opp_val = getattr(value, "Include4", None)
                setattr(value, "Include4", self)

    @property
    def base7(self):
        return self.__base7

    @base7.setter
    def base7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCases_UseCase__base7", None)
        self.__base7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Extend8"):
                opp_val = getattr(old_value, "Extend8", None)
                if opp_val == self:
                    setattr(old_value, "Extend8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Extend8"):
                opp_val = getattr(value, "Extend8", None)
                setattr(value, "Extend8", self)

class UseCases_Actor(Classifier):

    pass
class UseCases_Instance:

    pass
class Instance:

    pass
class UseCases_UseCaseInstance(Instance):

    pass
class UseCases_Classifier:

    pass