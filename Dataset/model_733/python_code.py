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

class FinalNode:

    pass
class uml_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class uml_DecisionNode(ControlNode):

    pass
class uml_ForkNode(ControlNode):

    pass
class uml_InitialNode(ControlNode):

    pass
class uml_FinalNode(ControlNode):

    pass
class uml_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: str):
        self.isCombineDuplicate = isCombineDuplicate
        
        pass
    @property
    def isCombineDuplicate(self):
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: str):
        self.__isCombineDuplicate = isCombineDuplicate


class ObjectNode:

    pass
class uml_ActivityParameterNode(ObjectNode):

    pass
class ExecutableNode:

    pass
class uml_Action(ExecutableNode):

    pass
class uml_RootPackage:

    pass
class ActivityEdge:

    pass
class uml_ControlFlow(ActivityEdge):

    pass
class uml_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: str, isMultireceive: str):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        
        pass
    @property
    def isMulticast(self):
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: str):
        self.__isMulticast = isMulticast


    @property
    def isMultireceive(self):
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: str):
        self.__isMultireceive = isMultireceive


class Type:

    pass
class RedefinableElement:

    pass
class Classifier:

    pass
class uml_StructuredClassifier(Classifier):

    pass
class StructuredClassifier:

    pass
class uml_EncapsulatedClassifier(StructuredClassifier):

    pass
class Class:

    pass
class uml_Behavior(Class):

    def __init__(self, isReentrant: str):
        self.isReentrant = isReentrant
        
        pass
    @property
    def isReentrant(self):
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant


class Element:

    pass
class uml_TemplateableElement(Element):

    pass
class ActivityGroup:

    pass
class NamedElement:

    pass
class uml_ActivityPartition(ActivityGroup, NamedElement):

    pass
class ActivityNode:

    pass
class uml_ControlNode(ActivityNode):

    pass
class uml_ExecutableNode(ActivityNode):

    pass
class uml_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str):
        self.isLeaf = isLeaf
        
        pass
    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


class Action:

    pass
class uml_OpaqueAction(Action):

    pass
class uml_Element(ABC):

    pass
class uml_ParameterableElement(Element):

    pass
class uml_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ParameterableElement:

    pass
class uml_TypedElement(NamedElement):

    pass
class TypedElement:

    pass
class uml_ObjectNode(ActivityNode, TypedElement):

    def __init__(self, isControlType: str):
        self.isControlType = isControlType
        
        pass
    @property
    def isControlType(self):
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: str):
        self.__isControlType = isControlType


class ValueSpecification:

    pass
class uml_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str):
        self.body = body
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class BehavioredClassifier:

    pass
class EncapsulatedClassifier:

    pass
class uml_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: str):
        self.isActive = isActive
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive


class uml_BehavioredClassifier(Classifier):

    pass
class uml_Namespace(NamedElement):

    pass
class uml_ActivityGroup(Element):

    pass
class uml_ActivityEdge(RedefinableElement):

    pass
class uml_ActivityNode(RedefinableElement):

    pass
class Behavior:

    pass
class uml_Activity(Behavior):

    pass
class uml_PackageableElement(ParameterableElement, NamedElement):

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
class uml_Classifier(TemplateableElement, Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: str):
        self.isAbstract = isAbstract
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


class uml_Package(TemplateableElement, PackageableElement, Namespace):

    pass