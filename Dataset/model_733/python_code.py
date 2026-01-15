from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"


############################################
# Definition of Classes
############################################

class uml_RootPackage:

    pass
class ActivityEdge:

    pass
class uml_ControlFlow(ActivityEdge):

    pass
class uml_ObjectFlow(ActivityEdge):

    def __init__(self, isMultireceive: str, isMulticast: str):
        self.isMultireceive = isMultireceive
        self.isMulticast = isMulticast
        
    @property
    def isMulticast(self) -> str:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: str):
        self.__isMulticast = isMulticast

    @property
    def isMultireceive(self) -> str:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: str):
        self.__isMultireceive = isMultireceive

class FinalNode:

    pass
class uml_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class uml_FinalNode(ControlNode):

    pass
class uml_DecisionNode(ControlNode):

    pass
class uml_ForkNode(ControlNode):

    pass
class uml_InitialNode(ControlNode):

    pass
class uml_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: str):
        self.isCombineDuplicate = isCombineDuplicate
        
    @property
    def isCombineDuplicate(self) -> str:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: str):
        self.__isCombineDuplicate = isCombineDuplicate

class ObjectNode:

    pass
class uml_ActivityParameterNode(ObjectNode):

    pass
class ActivityNode:

    pass
class uml_ExecutableNode(ActivityNode):

    pass
class Action:

    pass
class uml_OpaqueAction(Action):

    pass
class uml_Element(ABC):

    pass
class ParameterableElement:

    pass
class ExecutableNode:

    pass
class uml_Action(ExecutableNode):

    pass
class uml_ControlNode(ActivityNode):

    pass
class ValueSpecification:

    pass
class uml_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class BehavioredClassifier:

    pass
class EncapsulatedClassifier:

    pass
class uml_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: str):
        self.isActive = isActive
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

class Type:

    pass
class RedefinableElement:

    pass
class Classifier:

    pass
class uml_BehavioredClassifier(Classifier):

    pass
class uml_StructuredClassifier(Classifier):

    pass
class StructuredClassifier:

    pass
class uml_EncapsulatedClassifier(StructuredClassifier):

    pass
class TypedElement:

    pass
class uml_ObjectNode(TypedElement, ActivityNode):

    def __init__(self, isControlType: str):
        self.isControlType = isControlType
        
    @property
    def isControlType(self) -> str:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: str):
        self.__isControlType = isControlType

class Element:

    pass
class uml_TemplateableElement(Element):

    pass
class uml_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class uml_ParameterableElement(Element):

    pass
class ActivityGroup:

    pass
class NamedElement:

    pass
class uml_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str):
        self.isLeaf = isLeaf
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

class uml_Namespace(NamedElement):

    pass
class uml_TypedElement(NamedElement):

    pass
class uml_ActivityPartition(NamedElement, ActivityGroup):

    pass
class uml_ActivityGroup(Element):

    pass
class uml_ActivityEdge(RedefinableElement):

    pass
class uml_ActivityNode(RedefinableElement):

    pass
class Behavior:

    pass
class Class:

    pass
class uml_Behavior(Class):

    def __init__(self, isReentrant: str):
        self.isReentrant = isReentrant
        
    @property
    def isReentrant(self) -> str:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant

class uml_PackageableElement(NamedElement, ParameterableElement):

    pass
class TemplateableElement:

    pass
class PackageableElement:

    pass
class uml_ValueSpecification(TypedElement, PackageableElement):

    pass
class uml_Type(PackageableElement):

    pass
class Namespace:

    pass
class uml_Classifier(RedefinableElement, TemplateableElement, Type, Namespace):

    def __init__(self, isAbstract: str):
        self.isAbstract = isAbstract
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

class uml_Package(PackageableElement, TemplateableElement, Namespace):

    pass
class uml_Activity(Behavior):

    pass