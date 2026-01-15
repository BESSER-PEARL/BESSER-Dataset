from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class ReferenceType(Enum):
    Composition = "Composition"
    Aggregation = "Aggregation"
    Regular = "Regular"
class MessageSort(Enum):
    synchCall = "synchCall"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class InstantiationType(Enum):
    Depends = "Depends"
    Extends = "Extends"
class InteractionOperatorKind(Enum):
    alt = "alt"
    opt = "opt"
    loop = "loop"
    disruptable = "disruptable"
    critical = "critical"


############################################
# Definition of Classes
############################################

class ram_Substitution:

    pass
class Substitution:

    pass
class ram_TransitionSubstitution(Substitution):

    pass
class ram_Constraint:

    pass
class ram_StateMachine:

    pass
class ObjectType:

    pass
class Mapping:

    pass
class ram_AttributeMapping(Mapping):

    pass
class ram_OperationMapping(Mapping):

    pass
class ram_ParameterMapping(Mapping):

    pass
class LiteralSpecification:

    pass
class ram_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ram_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ram_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ram_LayoutElement:

    def __init__(self, x: float, y: float, ram_LayoutElement: "ram_ElementMap" = None):
        self.x = x
        self.y = y
        self.ram_LayoutElement = ram_LayoutElement
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def ram_LayoutElement(self):
        return self.__ram_LayoutElement

    @ram_LayoutElement.setter
    def ram_LayoutElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_LayoutElement__ram_LayoutElement", None)
        self.__ram_LayoutElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_ElementMap116"):
                opp_val = getattr(old_value, "ram_ElementMap116", None)
                if opp_val == self:
                    setattr(old_value, "ram_ElementMap116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ElementMap116"):
                opp_val = getattr(value, "ram_ElementMap116", None)
                setattr(value, "ram_ElementMap116", self)

class ram_ElementMap:

    pass
class ram_EObject:

    pass
class ram_ContainerMap:

    pass
class RCollection:

    pass
class ram_RSequence(RCollection):

    pass
class ram_RSet(RCollection):

    pass
class ram_FragmentContainer(ABC):

    pass
class ValueSpecification:

    pass
class ram_LiteralSpecification(ValueSpecification):

    pass
class ram_ParameterValue(ValueSpecification):

    pass
class ram_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

class ram_StructuralFeatureValue(ValueSpecification):

    pass
class ram_MessageEnd(ABC):

    pass
class MessageOccurrenceSpecification:

    pass
class ram_DestructionOccurrenceSpecification(MessageOccurrenceSpecification):

    pass
class InteractionFragment:

    pass
class ram_ExecutionStatement(InteractionFragment):

    pass
class ram_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, ram_CombinedFragment: set["ram_InteractionOperand"] = None):
        self.interactionOperator = interactionOperator
        self.ram_CombinedFragment = ram_CombinedFragment if ram_CombinedFragment is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def ram_CombinedFragment(self):
        return self.__ram_CombinedFragment

    @ram_CombinedFragment.setter
    def ram_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_CombinedFragment__ram_CombinedFragment", None)
        self.__ram_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_InteractionOperand"):
                    opp_val = getattr(item, "ram_InteractionOperand", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_InteractionOperand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_InteractionOperand"):
                    opp_val = getattr(item, "ram_InteractionOperand", None)
                    
                    setattr(item, "ram_InteractionOperand", self)
                    

class ram_OriginalBehaviorExecution(InteractionFragment):

    pass
class ram_OccurrenceSpecification(InteractionFragment):

    pass
class MessageEnd:

    pass
class OccurrenceSpecification:

    pass
class ram_MessageOccurrenceSpecification(OccurrenceSpecification, MessageEnd):

    pass
class ram_ValueSpecification(ABC):

    pass
class ram_ParameterValueMapping:

    pass
class ram_Message:

    def __init__(self, messageSort: str, selfMessage: bool, Message: "ram_Interaction" = None, ram_Message76: "ram_StructuralFeature" = None, ram_Message78: set["ram_ParameterValueMapping"] = None, messages: "ram_Interaction" = None, ram_Message81: "ram_ValueSpecification" = None, ram_Message84: "ram_MessageEnd" = None, ram_Message: "ram_MessageEnd" = None, ram_Message70: "ram_MessageEnd" = None, ram_Message73: "ram_Operation" = None):
        self.messageSort = messageSort
        self.selfMessage = selfMessage
        self.Message = Message
        self.ram_Message76 = ram_Message76
        self.ram_Message78 = ram_Message78 if ram_Message78 is not None else set()
        self.messages = messages
        self.ram_Message81 = ram_Message81
        self.ram_Message84 = ram_Message84
        self.ram_Message = ram_Message
        self.ram_Message70 = ram_Message70
        self.ram_Message73 = ram_Message73
        
    @property
    def selfMessage(self) -> bool:
        return self.__selfMessage

    @selfMessage.setter
    def selfMessage(self, selfMessage: bool):
        self.__selfMessage = selfMessage

    @property
    def messageSort(self) -> str:
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort

    @property
    def ram_Message81(self):
        return self.__ram_Message81

    @ram_Message81.setter
    def ram_Message81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message81", None)
        self.__ram_Message81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_ValueSpecification"):
                opp_val = getattr(old_value, "ram_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ram_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ValueSpecification"):
                opp_val = getattr(value, "ram_ValueSpecification", None)
                setattr(value, "ram_ValueSpecification", self)

    @property
    def messages(self):
        return self.__messages

    @messages.setter
    def messages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__messages", None)
        self.__messages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interaction"):
                opp_val = getattr(old_value, "Interaction", None)
                if opp_val == self:
                    setattr(old_value, "Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interaction"):
                opp_val = getattr(value, "Interaction", None)
                setattr(value, "Interaction", self)

    @property
    def ram_Message78(self):
        return self.__ram_Message78

    @ram_Message78.setter
    def ram_Message78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message78", None)
        self.__ram_Message78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_ParameterValueMapping"):
                    opp_val = getattr(item, "ram_ParameterValueMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_ParameterValueMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_ParameterValueMapping"):
                    opp_val = getattr(item, "ram_ParameterValueMapping", None)
                    
                    setattr(item, "ram_ParameterValueMapping", self)
                    

    @property
    def ram_Message84(self):
        return self.__ram_Message84

    @ram_Message84.setter
    def ram_Message84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message84", None)
        self.__ram_Message84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd83"):
                opp_val = getattr(old_value, "ram_MessageEnd83", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd83"):
                opp_val = getattr(value, "ram_MessageEnd83", None)
                setattr(value, "ram_MessageEnd83", self)

    @property
    def ram_Message70(self):
        return self.__ram_Message70

    @ram_Message70.setter
    def ram_Message70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message70", None)
        self.__ram_Message70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd71"):
                opp_val = getattr(old_value, "ram_MessageEnd71", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd71"):
                opp_val = getattr(value, "ram_MessageEnd71", None)
                setattr(value, "ram_MessageEnd71", self)

    @property
    def ram_Message73(self):
        return self.__ram_Message73

    @ram_Message73.setter
    def ram_Message73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message73", None)
        self.__ram_Message73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Operation74"):
                opp_val = getattr(old_value, "ram_Operation74", None)
                if opp_val == self:
                    setattr(old_value, "ram_Operation74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Operation74"):
                opp_val = getattr(value, "ram_Operation74", None)
                setattr(value, "ram_Operation74", self)

    @property
    def ram_Message(self):
        return self.__ram_Message

    @ram_Message.setter
    def ram_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message", None)
        self.__ram_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd"):
                opp_val = getattr(old_value, "ram_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd"):
                opp_val = getattr(value, "ram_MessageEnd", None)
                setattr(value, "ram_MessageEnd", self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__Message", None)
        self.__Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction"):
                opp_val = getattr(old_value, "interaction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction"):
                opp_val = getattr(value, "interaction", None)
                if opp_val is None:
                    setattr(value, "interaction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Message76(self):
        return self.__ram_Message76

    @ram_Message76.setter
    def ram_Message76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message76", None)
        self.__ram_Message76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_StructuralFeature"):
                opp_val = getattr(old_value, "ram_StructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "ram_StructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_StructuralFeature"):
                opp_val = getattr(value, "ram_StructuralFeature", None)
                setattr(value, "ram_StructuralFeature", self)

class ram_Lifeline:

    pass
class FragmentContainer:

    pass
class ram_InteractionOperand(FragmentContainer):

    pass
class ram_InteractionFragment(ABC):

    pass
class ram_TemporaryProperty(ABC):

    pass
class ram_Interaction(FragmentContainer):

    pass
class AbstractMessageView:

    pass
class ram_MessageViewReference(AbstractMessageView):

    pass
class ram_MessageView(AbstractMessageView):

    pass
class MappableElement:

    pass
class PrimitiveType:

    pass
class ram_REnum(PrimitiveType):

    pass
class ram_RFloat(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_RString(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RDouble(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RChar(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_RInt(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_RBoolean(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ImplementationClass:

    pass
class Type:

    pass
class ram_RAny(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RVoid(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_ObjectType(MappableElement, Type):

    pass
class ram_RCollection(Type, ImplementationClass):

    def __init__(self, ram_RCollection: "ram_ObjectType" = None):
        self.ram_RCollection = ram_RCollection
        
    @property
    def ram_RCollection(self):
        return self.__ram_RCollection

    @ram_RCollection.setter
    def ram_RCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_RCollection__ram_RCollection", None)
        self.__ram_RCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_ObjectType"):
                opp_val = getattr(old_value, "ram_ObjectType", None)
                if opp_val == self:
                    setattr(old_value, "ram_ObjectType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ObjectType"):
                opp_val = getattr(value, "ram_ObjectType", None)
                setattr(value, "ram_ObjectType", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class TypedElement:

    pass
class ram_Parameter(MappableElement, TypedElement):

    pass
class ram_StructuralFeature(TypedElement):

    def __init__(self, static: bool, ram_StructuralFeature: "ram_Message" = None, ram_StructuralFeature94: "ram_StructuralFeatureValue" = None):
        self.static = static
        self.ram_StructuralFeature = ram_StructuralFeature
        self.ram_StructuralFeature94 = ram_StructuralFeature94
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def ram_StructuralFeature94(self):
        return self.__ram_StructuralFeature94

    @ram_StructuralFeature94.setter
    def ram_StructuralFeature94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature94", None)
        self.__ram_StructuralFeature94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_StructuralFeatureValue"):
                opp_val = getattr(old_value, "ram_StructuralFeatureValue", None)
                if opp_val == self:
                    setattr(old_value, "ram_StructuralFeatureValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_StructuralFeatureValue"):
                opp_val = getattr(value, "ram_StructuralFeatureValue", None)
                setattr(value, "ram_StructuralFeatureValue", self)

    @property
    def ram_StructuralFeature(self):
        return self.__ram_StructuralFeature

    @ram_StructuralFeature.setter
    def ram_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature", None)
        self.__ram_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Message76"):
                opp_val = getattr(old_value, "ram_Message76", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message76"):
                opp_val = getattr(value, "ram_Message76", None)
                setattr(value, "ram_Message76", self)

class ram_PrimitiveType(Type, ImplementationClass):

    pass
class TemporaryProperty:

    pass
class StructuralFeature:

    pass
class ram_Property(StructuralFeature):

    def __init__(self, lowerBound: int, upperBound: int, referenceType: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.referenceType = referenceType
        
    @property
    def referenceType(self) -> str:
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: str):
        self.__referenceType = referenceType

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

class Property:

    pass
class ram_Reference(Property, TemporaryProperty):

    pass
class ram_Mapping(ABC):

    def __init__(self):
        
    def getFromElement(self) -> str:
        # TODO: Implement getFromElement method
        pass

    def getToElement(self) -> str:
        # TODO: Implement getToElement method
        pass

class ram_ClassifierMapping(Mapping):

    pass
class ram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ram_AbstractMessageView(ABC):

    pass
class ram_StructuralView:

    pass
class ram_Attribute(MappableElement, StructuralFeature, TemporaryProperty):

    pass
class ram_AssociationEnd(Property):

    def __init__(self, navigable: bool, AssociationEnd: "ram_Class" = None, ends: "ram_Association" = None, associationEnds: "ram_Class" = None, AssociationEnd25: "ram_Association" = None):
        self.navigable = navigable
        self.AssociationEnd = AssociationEnd
        self.ends = ends
        self.associationEnds = associationEnds
        self.AssociationEnd25 = AssociationEnd25
        
    @property
    def navigable(self) -> bool:
        return self.__navigable

    @navigable.setter
    def navigable(self, navigable: bool):
        self.__navigable = navigable

    @property
    def AssociationEnd(self):
        return self.__AssociationEnd

    @AssociationEnd.setter
    def AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__AssociationEnd", None)
        self.__AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass"):
                opp_val = getattr(old_value, "myClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass"):
                opp_val = getattr(value, "myClass", None)
                if opp_val is None:
                    setattr(value, "myClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def associationEnds(self):
        return self.__associationEnds

    @associationEnds.setter
    def associationEnds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__associationEnds", None)
        self.__associationEnds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def AssociationEnd25(self):
        return self.__AssociationEnd25

    @AssociationEnd25.setter
    def AssociationEnd25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__AssociationEnd25", None)
        self.__AssociationEnd25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc"):
                opp_val = getattr(old_value, "assoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc"):
                opp_val = getattr(value, "assoc", None)
                if opp_val is None:
                    setattr(value, "assoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ends(self):
        return self.__ends

    @ends.setter
    def ends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__ends", None)
        self.__ends = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class Classifier:

    pass
class ram_ImplementationClass(Classifier):

    def __init__(self, instanceClassName: str):
        self.instanceClassName = instanceClassName
        
    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

class ram_Class(Classifier):

    def __init__(self, partial: bool, abstract: bool, myClass: set["ram_AssociationEnd"] = None, ram_Class: set["ram_Attribute"] = None, Class: "ram_AssociationEnd" = None, ram_Class20: set["ram_Classifier"] = None):
        self.partial = partial
        self.abstract = abstract
        self.myClass = myClass if myClass is not None else set()
        self.ram_Class = ram_Class if ram_Class is not None else set()
        self.Class = Class
        self.ram_Class20 = ram_Class20 if ram_Class20 is not None else set()
        
    @property
    def partial(self) -> bool:
        return self.__partial

    @partial.setter
    def partial(self, partial: bool):
        self.__partial = partial

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def myClass(self):
        return self.__myClass

    @myClass.setter
    def myClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__myClass", None)
        self.__myClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationEnd"):
                    opp_val = getattr(item, "AssociationEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationEnd"):
                    opp_val = getattr(item, "AssociationEnd", None)
                    
                    setattr(item, "AssociationEnd", self)
                    

    @property
    def ram_Class20(self):
        return self.__ram_Class20

    @ram_Class20.setter
    def ram_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__ram_Class20", None)
        self.__ram_Class20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Classifier21"):
                    opp_val = getattr(item, "ram_Classifier21", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Classifier21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Classifier21"):
                    opp_val = getattr(item, "ram_Classifier21", None)
                    
                    setattr(item, "ram_Classifier21", self)
                    

    @property
    def ram_Class(self):
        return self.__ram_Class

    @ram_Class.setter
    def ram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__ram_Class", None)
        self.__ram_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Attribute"):
                    opp_val = getattr(item, "ram_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Attribute"):
                    opp_val = getattr(item, "ram_Attribute", None)
                    
                    setattr(item, "ram_Attribute", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnds"):
                opp_val = getattr(old_value, "associationEnds", None)
                if opp_val == self:
                    setattr(old_value, "associationEnds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnds"):
                opp_val = getattr(value, "associationEnds", None)
                setattr(value, "associationEnds", self)

class ram_Classifier(ObjectType):

    pass
class ram_Layout:

    pass
class ram_Instantiation:

    def __init__(self, type: str, ram_Instantiation: "ram_Aspect" = None, ram_Instantiation27: set["ram_ClassifierMapping"] = None, ram_Instantiation29: "ram_Aspect" = None):
        self.type = type
        self.ram_Instantiation = ram_Instantiation
        self.ram_Instantiation27 = ram_Instantiation27 if ram_Instantiation27 is not None else set()
        self.ram_Instantiation29 = ram_Instantiation29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ram_Instantiation(self):
        return self.__ram_Instantiation

    @ram_Instantiation.setter
    def ram_Instantiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Instantiation__ram_Instantiation", None)
        self.__ram_Instantiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Aspect6"):
                opp_val = getattr(old_value, "ram_Aspect6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Aspect6"):
                opp_val = getattr(value, "ram_Aspect6", None)
                if opp_val is None:
                    setattr(value, "ram_Aspect6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Instantiation29(self):
        return self.__ram_Instantiation29

    @ram_Instantiation29.setter
    def ram_Instantiation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Instantiation__ram_Instantiation29", None)
        self.__ram_Instantiation29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Aspect30"):
                opp_val = getattr(old_value, "ram_Aspect30", None)
                if opp_val == self:
                    setattr(old_value, "ram_Aspect30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Aspect30"):
                opp_val = getattr(value, "ram_Aspect30", None)
                setattr(value, "ram_Aspect30", self)

    @property
    def ram_Instantiation27(self):
        return self.__ram_Instantiation27

    @ram_Instantiation27.setter
    def ram_Instantiation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Instantiation__ram_Instantiation27", None)
        self.__ram_Instantiation27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_ClassifierMapping"):
                    opp_val = getattr(item, "ram_ClassifierMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_ClassifierMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_ClassifierMapping"):
                    opp_val = getattr(item, "ram_ClassifierMapping", None)
                    
                    setattr(item, "ram_ClassifierMapping", self)
                    

class NamedElement:

    pass
class ram_Gate(NamedElement, MessageEnd):

    pass
class ram_StateView(NamedElement):

    pass
class ram_MappableElement(NamedElement):

    pass
class ram_REnumLiteral(NamedElement):

    pass
class ram_State(NamedElement):

    pass
class ram_Association(NamedElement):

    pass
class ram_Type(NamedElement):

    pass
class ram_TypedElement(NamedElement):

    def __init__(self, ram_TypedElement: "ram_Lifeline" = None):
        self.ram_TypedElement = ram_TypedElement
        
    @property
    def ram_TypedElement(self):
        return self.__ram_TypedElement

    @ram_TypedElement.setter
    def ram_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_TypedElement__ram_TypedElement", None)
        self.__ram_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Lifeline64"):
                opp_val = getattr(old_value, "ram_Lifeline64", None)
                if opp_val == self:
                    setattr(old_value, "ram_Lifeline64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Lifeline64"):
                opp_val = getattr(value, "ram_Lifeline64", None)
                setattr(value, "ram_Lifeline64", self)

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

class ram_Transition(NamedElement):

    pass
class ram_AspectMessageView(NamedElement, AbstractMessageView):

    pass
class ram_Operation(MappableElement, NamedElement):

    def __init__(self, static: bool, partial: bool, abstract: bool, visibility: str, ram_Operation: "ram_Type" = None, ram_Operation34: set["ram_Parameter"] = None, ram_Operation45: "ram_MessageView" = None, ram_Operation59: "ram_AspectMessageView" = None, ram_Operation74: "ram_Message" = None, ram_Operation119: "ram_Classifier" = None, ram_Operation143: "ram_OperationMapping" = None, ram_Operation146: "ram_OperationMapping" = None, ram_Operation172: "ram_Transition" = None):
        self.static = static
        self.partial = partial
        self.abstract = abstract
        self.visibility = visibility
        self.ram_Operation = ram_Operation
        self.ram_Operation34 = ram_Operation34 if ram_Operation34 is not None else set()
        self.ram_Operation45 = ram_Operation45
        self.ram_Operation59 = ram_Operation59
        self.ram_Operation74 = ram_Operation74
        self.ram_Operation119 = ram_Operation119
        self.ram_Operation143 = ram_Operation143
        self.ram_Operation146 = ram_Operation146
        self.ram_Operation172 = ram_Operation172
        
    @property
    def partial(self) -> bool:
        return self.__partial

    @partial.setter
    def partial(self, partial: bool):
        self.__partial = partial

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def ram_Operation172(self):
        return self.__ram_Operation172

    @ram_Operation172.setter
    def ram_Operation172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation172", None)
        self.__ram_Operation172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Transition171"):
                opp_val = getattr(old_value, "ram_Transition171", None)
                if opp_val == self:
                    setattr(old_value, "ram_Transition171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Transition171"):
                opp_val = getattr(value, "ram_Transition171", None)
                setattr(value, "ram_Transition171", self)

    @property
    def ram_Operation59(self):
        return self.__ram_Operation59

    @ram_Operation59.setter
    def ram_Operation59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation59", None)
        self.__ram_Operation59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_AspectMessageView58"):
                opp_val = getattr(old_value, "ram_AspectMessageView58", None)
                if opp_val == self:
                    setattr(old_value, "ram_AspectMessageView58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_AspectMessageView58"):
                opp_val = getattr(value, "ram_AspectMessageView58", None)
                setattr(value, "ram_AspectMessageView58", self)

    @property
    def ram_Operation(self):
        return self.__ram_Operation

    @ram_Operation.setter
    def ram_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation", None)
        self.__ram_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Type32"):
                opp_val = getattr(old_value, "ram_Type32", None)
                if opp_val == self:
                    setattr(old_value, "ram_Type32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Type32"):
                opp_val = getattr(value, "ram_Type32", None)
                setattr(value, "ram_Type32", self)

    @property
    def ram_Operation45(self):
        return self.__ram_Operation45

    @ram_Operation45.setter
    def ram_Operation45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation45", None)
        self.__ram_Operation45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageView"):
                opp_val = getattr(old_value, "ram_MessageView", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageView"):
                opp_val = getattr(value, "ram_MessageView", None)
                setattr(value, "ram_MessageView", self)

    @property
    def ram_Operation119(self):
        return self.__ram_Operation119

    @ram_Operation119.setter
    def ram_Operation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation119", None)
        self.__ram_Operation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Classifier118"):
                opp_val = getattr(old_value, "ram_Classifier118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Classifier118"):
                opp_val = getattr(value, "ram_Classifier118", None)
                if opp_val is None:
                    setattr(value, "ram_Classifier118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Operation34(self):
        return self.__ram_Operation34

    @ram_Operation34.setter
    def ram_Operation34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation34", None)
        self.__ram_Operation34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Parameter"):
                    opp_val = getattr(item, "ram_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Parameter"):
                    opp_val = getattr(item, "ram_Parameter", None)
                    
                    setattr(item, "ram_Parameter", self)
                    

    @property
    def ram_Operation74(self):
        return self.__ram_Operation74

    @ram_Operation74.setter
    def ram_Operation74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation74", None)
        self.__ram_Operation74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Message73"):
                opp_val = getattr(old_value, "ram_Message73", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message73"):
                opp_val = getattr(value, "ram_Message73", None)
                setattr(value, "ram_Message73", self)

    @property
    def ram_Operation143(self):
        return self.__ram_Operation143

    @ram_Operation143.setter
    def ram_Operation143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation143", None)
        self.__ram_Operation143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_OperationMapping142"):
                opp_val = getattr(old_value, "ram_OperationMapping142", None)
                if opp_val == self:
                    setattr(old_value, "ram_OperationMapping142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_OperationMapping142"):
                opp_val = getattr(value, "ram_OperationMapping142", None)
                setattr(value, "ram_OperationMapping142", self)

    @property
    def ram_Operation146(self):
        return self.__ram_Operation146

    @ram_Operation146.setter
    def ram_Operation146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation146", None)
        self.__ram_Operation146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_OperationMapping145"):
                opp_val = getattr(old_value, "ram_OperationMapping145", None)
                if opp_val == self:
                    setattr(old_value, "ram_OperationMapping145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_OperationMapping145"):
                opp_val = getattr(value, "ram_OperationMapping145", None)
                setattr(value, "ram_OperationMapping145", self)

class ram_Aspect(NamedElement):

    pass