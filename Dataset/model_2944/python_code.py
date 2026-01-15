from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class jointPackage_UML2ER_TrgElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TrgFeature:

    pass
class jointPackage_UML2ER_TrgAttribute(TrgFeature):

    def __init__(self, type: str, TrgFeature: "jointPackage_UML2ER_TrgEntityType"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class jointPackage_UML2ER_TrgReference(TrgFeature):

    pass
class TrgReference:

    pass
class jointPackage_UML2ER_TrgStrongReference(TrgReference):

    pass
class jointPackage_UML2ER_TrgWeakReference(TrgReference):

    pass
class TrgEntityType:

    pass
class TrgElement:

    pass
class jointPackage_UML2ER_TrgFeature(TrgElement):

    pass
class jointPackage_UML2ER_TrgEntityType(TrgElement):

    pass
class jointPackage_UML2ER_TrgERModel(TrgElement):

    pass
class jointPackage_UML2ER_SrcNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SrcProperty:

    pass
class SrcClass:

    pass
class SrcNamedElement:

    pass
class jointPackage_UML2ER_SrcClass(SrcNamedElement):

    pass
class jointPackage_UML2ER_SrcProperty(SrcNamedElement):

    def __init__(self, primitiveType: str, isContainment: bool, jointPackage_UML2ER_SrcProperty: "SrcClass" = None):
        self.primitiveType = primitiveType
        self.isContainment = isContainment
        self.jointPackage_UML2ER_SrcProperty = jointPackage_UML2ER_SrcProperty
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def isContainment(self) -> bool:
        return self.__isContainment

    @isContainment.setter
    def isContainment(self, isContainment: bool):
        self.__isContainment = isContainment

    @property
    def jointPackage_UML2ER_SrcProperty(self):
        return self.__jointPackage_UML2ER_SrcProperty

    @jointPackage_UML2ER_SrcProperty.setter
    def jointPackage_UML2ER_SrcProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_UML2ER_SrcProperty__jointPackage_UML2ER_SrcProperty", None)
        self.__jointPackage_UML2ER_SrcProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcClass9"):
                opp_val = getattr(old_value, "SrcClass9", None)
                if opp_val == self:
                    setattr(old_value, "SrcClass9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcClass9"):
                opp_val = getattr(value, "SrcClass9", None)
                setattr(value, "SrcClass9", self)

class jointPackage_UML2ER_SrcPackage(SrcNamedElement):

    pass
class TrgStrongReference:

    pass
class SrcPackage:

    pass
class jointPackage_UML2ER_JointMM:

    pass