from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ReferenceType(Enum):
    Composition = "Composition"
    Aggregation = "Aggregation"
    Regular = "Regular"
class InteractionOperatorKind(Enum):
    alt = "alt"
    opt = "opt"
    loop = "loop"
    disruptable = "disruptable"
    critical = "critical"
class Visibility(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class InstantiationType(Enum):
    Depends = "Depends"
    Extends = "Extends"
class MessageSort(Enum):
    synchCall = "synchCall"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"


############################################
# Definition of Classes
############################################

class ram_ContainerMap:

    pass
class RCollection:

    pass
class ram_RList(RCollection):

    pass
class ram_RSet(RCollection):

    pass
class ObjectType:

    pass
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
            if hasattr(old_value, "ram_ElementMap120"):
                opp_val = getattr(old_value, "ram_ElementMap120", None)
                if opp_val == self:
                    setattr(old_value, "ram_ElementMap120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ElementMap120"):
                opp_val = getattr(value, "ram_ElementMap120", None)
                setattr(value, "ram_ElementMap120", self)

class ram_ElementMap:

    pass
class ram_EObject:

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

class ValueSpecification:

    pass
class ram_ParameterValue(ValueSpecification):

    pass
class ram_LiteralSpecification(ValueSpecification):

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
class MessageOccurrenceSpecification:

    pass
class ram_DestructionOccurrenceSpecification(MessageOccurrenceSpecification):

    pass
class InteractionFragment:

    pass
class ram_ExecutionStatement(InteractionFragment):

    pass
class ram_OriginalBehaviorExecution(InteractionFragment):

    pass
class ram_OccurrenceSpecification(InteractionFragment):

    pass
class MessageEnd:

    pass
class OccurrenceSpecification:

    pass
class ram_MessageOccurrenceSpecification(MessageEnd, OccurrenceSpecification):

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
                    

class ram_FragmentContainer(ABC):

    pass
class ram_ParameterValueMapping:

    pass
class ram_ValueSpecification(ABC):

    pass
class ram_InteractionFragment(ABC):

    pass
class ram_TemporaryProperty(ABC):

    pass
class ram_MessageEnd(ABC):

    pass
class ram_Message:

    def __init__(self, selfMessage: bool, messageSort: str, Message: "ram_Interaction" = None, ram_Message: "ram_MessageEnd" = None, ram_Message74: "ram_MessageEnd" = None, ram_Message77: "ram_Operation" = None, messages: "ram_Interaction" = None, ram_Message85: "ram_ValueSpecification" = None, ram_Message88: "ram_MessageEnd" = None, ram_Message80: "ram_StructuralFeature" = None, ram_Message82: set["ram_ParameterValueMapping"] = None):
        self.selfMessage = selfMessage
        self.messageSort = messageSort
        self.Message = Message
        self.ram_Message = ram_Message
        self.ram_Message74 = ram_Message74
        self.ram_Message77 = ram_Message77
        self.messages = messages
        self.ram_Message85 = ram_Message85
        self.ram_Message88 = ram_Message88
        self.ram_Message80 = ram_Message80
        self.ram_Message82 = ram_Message82 if ram_Message82 is not None else set()
        
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
    def ram_Message88(self):
        return self.__ram_Message88

    @ram_Message88.setter
    def ram_Message88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message88", None)
        self.__ram_Message88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd87"):
                opp_val = getattr(old_value, "ram_MessageEnd87", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd87"):
                opp_val = getattr(value, "ram_MessageEnd87", None)
                setattr(value, "ram_MessageEnd87", self)

    @property
    def ram_Message80(self):
        return self.__ram_Message80

    @ram_Message80.setter
    def ram_Message80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message80", None)
        self.__ram_Message80 = value
        
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

    @property
    def ram_Message85(self):
        return self.__ram_Message85

    @ram_Message85.setter
    def ram_Message85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message85", None)
        self.__ram_Message85 = value
        
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
    def ram_Message74(self):
        return self.__ram_Message74

    @ram_Message74.setter
    def ram_Message74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message74", None)
        self.__ram_Message74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd75"):
                opp_val = getattr(old_value, "ram_MessageEnd75", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd75"):
                opp_val = getattr(value, "ram_MessageEnd75", None)
                setattr(value, "ram_MessageEnd75", self)

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
    def ram_Message77(self):
        return self.__ram_Message77

    @ram_Message77.setter
    def ram_Message77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message77", None)
        self.__ram_Message77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Operation78"):
                opp_val = getattr(old_value, "ram_Operation78", None)
                if opp_val == self:
                    setattr(old_value, "ram_Operation78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Operation78"):
                opp_val = getattr(value, "ram_Operation78", None)
                setattr(value, "ram_Operation78", self)

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
    def ram_Message82(self):
        return self.__ram_Message82

    @ram_Message82.setter
    def ram_Message82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message82", None)
        self.__ram_Message82 = value if value is not None else set()
        
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
                    

class ram_Lifeline:

    pass
class AbstractMessageView:

    pass
class ram_MessageView(AbstractMessageView):

    pass
class FragmentContainer:

    pass
class ram_InteractionOperand(FragmentContainer):

    pass
class ram_MessageViewReference(AbstractMessageView):

    pass
class ram_Interaction(FragmentContainer):

    pass
class PrimitiveType:

    pass
class ram_RBoolean(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_REnum(PrimitiveType):

    pass
class ram_RString(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_RChar(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RInt(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class MappableElement:

    pass
class ImplementationClass:

    pass
class Type:

    pass
class ram_RVoid(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
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

class ram_ObjectType(Type, MappableElement):

    pass
class ram_RAny(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class TypedElement:

    pass
class ram_StructuralFeature(TypedElement):

    def __init__(self, static: bool, ram_StructuralFeature: "ram_Message" = None, ram_StructuralFeature98: "ram_StructuralFeatureValue" = None):
        self.static = static
        self.ram_StructuralFeature = ram_StructuralFeature
        self.ram_StructuralFeature98 = ram_StructuralFeature98
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

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
            if hasattr(old_value, "ram_Message80"):
                opp_val = getattr(old_value, "ram_Message80", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message80"):
                opp_val = getattr(value, "ram_Message80", None)
                setattr(value, "ram_Message80", self)

    @property
    def ram_StructuralFeature98(self):
        return self.__ram_StructuralFeature98

    @ram_StructuralFeature98.setter
    def ram_StructuralFeature98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature98", None)
        self.__ram_StructuralFeature98 = value
        
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
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

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

class ram_Parameter(TypedElement):

    pass
class Property:

    pass
class ram_Reference(Property, TemporaryProperty):

    pass
class ram_Attribute(TemporaryProperty, StructuralFeature):

    pass
class ram_AssociationEnd(Property):

    def __init__(self, navigable: bool, ends: "ram_Association" = None, associationEnds: "ram_Class" = None, AssociationEnd23: "ram_Association" = None, AssociationEnd: "ram_Class" = None):
        self.navigable = navigable
        self.ends = ends
        self.associationEnds = associationEnds
        self.AssociationEnd23 = AssociationEnd23
        self.AssociationEnd = AssociationEnd
        
    @property
    def navigable(self) -> bool:
        return self.__navigable

    @navigable.setter
    def navigable(self, navigable: bool):
        self.__navigable = navigable

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
    def AssociationEnd23(self):
        return self.__AssociationEnd23

    @AssociationEnd23.setter
    def AssociationEnd23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__AssociationEnd23", None)
        self.__AssociationEnd23 = value
        
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

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class ram_Mapping:

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

class ram_StructuralView:

    pass
class NamedElement:

    pass
class ram_AspectMessageView(AbstractMessageView, NamedElement):

    pass
class ram_Gate(MessageEnd, NamedElement):

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
            if hasattr(old_value, "ram_Lifeline68"):
                opp_val = getattr(old_value, "ram_Lifeline68", None)
                if opp_val == self:
                    setattr(old_value, "ram_Lifeline68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Lifeline68"):
                opp_val = getattr(value, "ram_Lifeline68", None)
                setattr(value, "ram_Lifeline68", self)

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

class ram_Operation(NamedElement, MappableElement):

    def __init__(self, abstract: bool, visibility: str, static: bool, partial: bool, ram_Operation: "ram_Type" = None, ram_Operation38: set["ram_Parameter"] = None, ram_Operation49: "ram_MessageView" = None, ram_Operation63: "ram_AspectMessageView" = None, ram_Operation78: "ram_Message" = None, ram_Operation123: "ram_Classifier" = None):
        self.abstract = abstract
        self.visibility = visibility
        self.static = static
        self.partial = partial
        self.ram_Operation = ram_Operation
        self.ram_Operation38 = ram_Operation38 if ram_Operation38 is not None else set()
        self.ram_Operation49 = ram_Operation49
        self.ram_Operation63 = ram_Operation63
        self.ram_Operation78 = ram_Operation78
        self.ram_Operation123 = ram_Operation123
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

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
    def ram_Operation49(self):
        return self.__ram_Operation49

    @ram_Operation49.setter
    def ram_Operation49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation49", None)
        self.__ram_Operation49 = value
        
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
    def ram_Operation38(self):
        return self.__ram_Operation38

    @ram_Operation38.setter
    def ram_Operation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation38", None)
        self.__ram_Operation38 = value if value is not None else set()
        
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
    def ram_Operation63(self):
        return self.__ram_Operation63

    @ram_Operation63.setter
    def ram_Operation63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation63", None)
        self.__ram_Operation63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_AspectMessageView62"):
                opp_val = getattr(old_value, "ram_AspectMessageView62", None)
                if opp_val == self:
                    setattr(old_value, "ram_AspectMessageView62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_AspectMessageView62"):
                opp_val = getattr(value, "ram_AspectMessageView62", None)
                setattr(value, "ram_AspectMessageView62", self)

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
            if hasattr(old_value, "ram_Type36"):
                opp_val = getattr(old_value, "ram_Type36", None)
                if opp_val == self:
                    setattr(old_value, "ram_Type36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Type36"):
                opp_val = getattr(value, "ram_Type36", None)
                setattr(value, "ram_Type36", self)

    @property
    def ram_Operation78(self):
        return self.__ram_Operation78

    @ram_Operation78.setter
    def ram_Operation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation78", None)
        self.__ram_Operation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Message77"):
                opp_val = getattr(old_value, "ram_Message77", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message77"):
                opp_val = getattr(value, "ram_Message77", None)
                setattr(value, "ram_Message77", self)

    @property
    def ram_Operation123(self):
        return self.__ram_Operation123

    @ram_Operation123.setter
    def ram_Operation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation123", None)
        self.__ram_Operation123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Classifier122"):
                opp_val = getattr(old_value, "ram_Classifier122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Classifier122"):
                opp_val = getattr(value, "ram_Classifier122", None)
                if opp_val is None:
                    setattr(value, "ram_Classifier122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ram_REnumLiteral(NamedElement):

    pass
class ram_Aspect(NamedElement):

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

    def __init__(self, partial: bool, abstract: bool, Class: "ram_AssociationEnd" = None, myClass: set["ram_AssociationEnd"] = None, ram_Class: set["ram_Attribute"] = None, ram_Class18: set["ram_Classifier"] = None):
        self.partial = partial
        self.abstract = abstract
        self.Class = Class
        self.myClass = myClass if myClass is not None else set()
        self.ram_Class = ram_Class if ram_Class is not None else set()
        self.ram_Class18 = ram_Class18 if ram_Class18 is not None else set()
        
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

    @property
    def ram_Class18(self):
        return self.__ram_Class18

    @ram_Class18.setter
    def ram_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__ram_Class18", None)
        self.__ram_Class18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Classifier19"):
                    opp_val = getattr(item, "ram_Classifier19", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Classifier19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Classifier19"):
                    opp_val = getattr(item, "ram_Classifier19", None)
                    
                    setattr(item, "ram_Classifier19", self)
                    

class ram_Type(NamedElement):

    pass
class ram_Association(NamedElement):

    pass
class ram_Classifier(ObjectType):

    pass
class ram_Layout:

    pass
class ram_Instantiation:

    def __init__(self, type: str, ram_Instantiation: "ram_Aspect" = None, ram_Instantiation25: set["ram_Mapping"] = None, ram_Instantiation27: "ram_Aspect" = None):
        self.type = type
        self.ram_Instantiation = ram_Instantiation
        self.ram_Instantiation25 = ram_Instantiation25 if ram_Instantiation25 is not None else set()
        self.ram_Instantiation27 = ram_Instantiation27
        
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
    def ram_Instantiation25(self):
        return self.__ram_Instantiation25

    @ram_Instantiation25.setter
    def ram_Instantiation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Instantiation__ram_Instantiation25", None)
        self.__ram_Instantiation25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Mapping"):
                    opp_val = getattr(item, "ram_Mapping", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Mapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Mapping"):
                    opp_val = getattr(item, "ram_Mapping", None)
                    
                    setattr(item, "ram_Mapping", self)
                    

    @property
    def ram_Instantiation27(self):
        return self.__ram_Instantiation27

    @ram_Instantiation27.setter
    def ram_Instantiation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Instantiation__ram_Instantiation27", None)
        self.__ram_Instantiation27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Aspect28"):
                opp_val = getattr(old_value, "ram_Aspect28", None)
                if opp_val == self:
                    setattr(old_value, "ram_Aspect28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Aspect28"):
                opp_val = getattr(value, "ram_Aspect28", None)
                setattr(value, "ram_Aspect28", self)

class ram_AbstractMessageView(ABC):

    pass
class ram_MappableElement(NamedElement):

    pass