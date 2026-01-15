from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InstantiationType(Enum):
    Depends = "Depends"
    Extends = "Extends"
class MessageSort(Enum):
    synchCall = "synchCall"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class Visibility(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
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
class Mapping:

    pass
class ram_OperationMapping(Mapping):

    pass
class ram_StateMachine:

    pass
class ram_ParameterMapping(Mapping):

    pass
class ram_AttributeMapping(Mapping):

    pass
class ram_LayoutElement:

    def __init__(self, y: float, x: float, ram_LayoutElement: "ram_ElementMap" = None):
        self.y = y
        self.x = x
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
            if hasattr(old_value, "ram_ElementMap114"):
                opp_val = getattr(old_value, "ram_ElementMap114", None)
                if opp_val == self:
                    setattr(old_value, "ram_ElementMap114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ElementMap114"):
                opp_val = getattr(value, "ram_ElementMap114", None)
                setattr(value, "ram_ElementMap114", self)

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
class ram_ParameterValueMapping:

    pass
class ram_FragmentContainer(ABC):

    pass
class MessageOccurrenceSpecification:

    pass
class ram_DestructionOccurrenceSpecification(MessageOccurrenceSpecification):

    pass
class InteractionFragment:

    pass
class ram_OriginalBehaviorExecution(InteractionFragment):

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
class ram_Message:

    def __init__(self, selfMessage: bool, messageSort: str, ram_Message: "ram_MessageEnd" = None, Message: "ram_Interaction" = None, ram_Message79: "ram_ValueSpecification" = None, ram_Message82: "ram_MessageEnd" = None, ram_Message68: "ram_MessageEnd" = None, ram_Message71: "ram_Operation" = None, ram_Message74: "ram_StructuralFeature" = None, ram_Message76: set["ram_ParameterValueMapping"] = None, messages: "ram_Interaction" = None):
        self.selfMessage = selfMessage
        self.messageSort = messageSort
        self.ram_Message = ram_Message
        self.Message = Message
        self.ram_Message79 = ram_Message79
        self.ram_Message82 = ram_Message82
        self.ram_Message68 = ram_Message68
        self.ram_Message71 = ram_Message71
        self.ram_Message74 = ram_Message74
        self.ram_Message76 = ram_Message76 if ram_Message76 is not None else set()
        self.messages = messages
        
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
    def ram_Message79(self):
        return self.__ram_Message79

    @ram_Message79.setter
    def ram_Message79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message79", None)
        self.__ram_Message79 = value
        
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
    def ram_Message68(self):
        return self.__ram_Message68

    @ram_Message68.setter
    def ram_Message68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message68", None)
        self.__ram_Message68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd69"):
                opp_val = getattr(old_value, "ram_MessageEnd69", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd69"):
                opp_val = getattr(value, "ram_MessageEnd69", None)
                setattr(value, "ram_MessageEnd69", self)

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
    def ram_Message82(self):
        return self.__ram_Message82

    @ram_Message82.setter
    def ram_Message82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message82", None)
        self.__ram_Message82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd81"):
                opp_val = getattr(old_value, "ram_MessageEnd81", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd81"):
                opp_val = getattr(value, "ram_MessageEnd81", None)
                setattr(value, "ram_MessageEnd81", self)

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
    def ram_Message71(self):
        return self.__ram_Message71

    @ram_Message71.setter
    def ram_Message71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message71", None)
        self.__ram_Message71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Operation72"):
                opp_val = getattr(old_value, "ram_Operation72", None)
                if opp_val == self:
                    setattr(old_value, "ram_Operation72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Operation72"):
                opp_val = getattr(value, "ram_Operation72", None)
                setattr(value, "ram_Operation72", self)

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
    def ram_Message76(self):
        return self.__ram_Message76

    @ram_Message76.setter
    def ram_Message76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message76", None)
        self.__ram_Message76 = value if value is not None else set()
        
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
class ram_MessageEnd(ABC):

    pass
class ram_InteractionFragment(ABC):

    pass
class ram_TemporaryProperty(ABC):

    pass
class FragmentContainer:

    pass
class ram_InteractionOperand(FragmentContainer):

    pass
class ram_Interaction(FragmentContainer):

    pass
class AbstractMessageView:

    pass
class ram_MessageViewReference(AbstractMessageView):

    pass
class ram_MessageView(AbstractMessageView):

    pass
class TypedElement:

    pass
class ram_StructuralFeature(TypedElement):

    def __init__(self, static: bool, ram_StructuralFeature: "ram_Message" = None, ram_StructuralFeature92: "ram_StructuralFeatureValue" = None):
        self.static = static
        self.ram_StructuralFeature = ram_StructuralFeature
        self.ram_StructuralFeature92 = ram_StructuralFeature92
        
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
            if hasattr(old_value, "ram_Message74"):
                opp_val = getattr(old_value, "ram_Message74", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message74"):
                opp_val = getattr(value, "ram_Message74", None)
                setattr(value, "ram_Message74", self)

    @property
    def ram_StructuralFeature92(self):
        return self.__ram_StructuralFeature92

    @ram_StructuralFeature92.setter
    def ram_StructuralFeature92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature92", None)
        self.__ram_StructuralFeature92 = value
        
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

    @property
    def referenceType(self) -> str:
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: str):
        self.__referenceType = referenceType

class PrimitiveType:

    pass
class ram_RLong(PrimitiveType):

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

class ram_RString(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RFloat(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

class ram_RArray(PrimitiveType):

    def __init__(self, size: int, ram_RArray: "ram_ObjectType" = None):
        self.size = size
        self.ram_RArray = ram_RArray
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def ram_RArray(self):
        return self.__ram_RArray

    @ram_RArray.setter
    def ram_RArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_RArray__ram_RArray", None)
        self.__ram_RArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_ObjectType192"):
                opp_val = getattr(old_value, "ram_ObjectType192", None)
                if opp_val == self:
                    setattr(old_value, "ram_ObjectType192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ObjectType192"):
                opp_val = getattr(value, "ram_ObjectType192", None)
                setattr(value, "ram_ObjectType192", self)

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

class ram_REnum(PrimitiveType):

    pass
class ram_RDouble(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RBoolean(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class Type:

    pass
class ram_TypeParameter(Type):

    pass
class ram_RVoid(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RAny(Type):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ImplementationClass:

    pass
class ram_RCollection(ImplementationClass, Type):

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

class ObjectType:

    pass
class ram_PrimitiveType(ImplementationClass, ObjectType):

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

class MappableElement:

    pass
class ram_Parameter(TypedElement, MappableElement):

    pass
class ram_ObjectType(MappableElement, Type):

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
class ram_Layout:

    pass
class ram_Instantiation:

    def __init__(self, type: str, ram_Instantiation: "ram_Aspect" = None, ram_Instantiation25: set["ram_ClassifierMapping"] = None, ram_Instantiation27: "ram_Aspect" = None):
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

class ram_AbstractMessageView(ABC):

    pass
class Property:

    pass
class ram_Reference(Property, TemporaryProperty):

    pass
class ram_AssociationEnd(Property):

    def __init__(self, navigable: bool, ends: "ram_Association" = None, associationEnds: "ram_Classifier" = None, AssociationEnd: "ram_Association" = None, AssociationEnd119: "ram_Classifier" = None):
        self.navigable = navigable
        self.ends = ends
        self.associationEnds = associationEnds
        self.AssociationEnd = AssociationEnd
        self.AssociationEnd119 = AssociationEnd119
        
    @property
    def navigable(self) -> bool:
        return self.__navigable

    @navigable.setter
    def navigable(self, navigable: bool):
        self.__navigable = navigable

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
    def AssociationEnd119(self):
        return self.__AssociationEnd119

    @AssociationEnd119.setter
    def AssociationEnd119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__AssociationEnd119", None)
        self.__AssociationEnd119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classifier"):
                opp_val = getattr(old_value, "classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classifier"):
                opp_val = getattr(value, "classifier", None)
                if opp_val is None:
                    setattr(value, "classifier", set([self]))
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
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class ram_Attribute(TemporaryProperty, MappableElement, StructuralFeature):

    pass
class Classifier:

    pass
class ram_ImplementationClass(Classifier):

    def __init__(self, instanceClassName: str, interface: bool):
        self.instanceClassName = instanceClassName
        self.interface = interface
        
    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

class ram_Class(Classifier):

    def __init__(self, partial: bool, abstract: bool, ram_Class: set["ram_Attribute"] = None, ram_Class19: set["ram_Classifier"] = None):
        self.partial = partial
        self.abstract = abstract
        self.ram_Class = ram_Class if ram_Class is not None else set()
        self.ram_Class19 = ram_Class19 if ram_Class19 is not None else set()
        
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
    def ram_Class19(self):
        return self.__ram_Class19

    @ram_Class19.setter
    def ram_Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Class__ram_Class19", None)
        self.__ram_Class19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Classifier20"):
                    opp_val = getattr(item, "ram_Classifier20", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Classifier20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Classifier20"):
                    opp_val = getattr(item, "ram_Classifier20", None)
                    
                    setattr(item, "ram_Classifier20", self)
                    

class ram_Classifier(ObjectType):

    pass
class ram_StructuralView:

    pass
class NamedElement:

    pass
class ram_AspectMessageView(NamedElement, AbstractMessageView):

    pass
class ram_Transition(NamedElement):

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
            if hasattr(old_value, "ram_Lifeline62"):
                opp_val = getattr(old_value, "ram_Lifeline62", None)
                if opp_val == self:
                    setattr(old_value, "ram_Lifeline62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Lifeline62"):
                opp_val = getattr(value, "ram_Lifeline62", None)
                setattr(value, "ram_Lifeline62", self)

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

class ram_Association(NamedElement):

    pass
class ram_REnumLiteral(NamedElement):

    pass
class ram_Operation(MappableElement, NamedElement):

    def __init__(self, abstract: bool, visibility: str, static: bool, partial: bool, ram_Operation: "ram_Type" = None, ram_Operation32: set["ram_Parameter"] = None, ram_Operation43: "ram_MessageView" = None, ram_Operation57: "ram_AspectMessageView" = None, ram_Operation72: "ram_Message" = None, ram_Operation117: "ram_Classifier" = None, ram_Operation145: "ram_OperationMapping" = None, ram_Operation148: "ram_OperationMapping" = None, ram_Operation174: "ram_Transition" = None):
        self.abstract = abstract
        self.visibility = visibility
        self.static = static
        self.partial = partial
        self.ram_Operation = ram_Operation
        self.ram_Operation32 = ram_Operation32 if ram_Operation32 is not None else set()
        self.ram_Operation43 = ram_Operation43
        self.ram_Operation57 = ram_Operation57
        self.ram_Operation72 = ram_Operation72
        self.ram_Operation117 = ram_Operation117
        self.ram_Operation145 = ram_Operation145
        self.ram_Operation148 = ram_Operation148
        self.ram_Operation174 = ram_Operation174
        
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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def ram_Operation174(self):
        return self.__ram_Operation174

    @ram_Operation174.setter
    def ram_Operation174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation174", None)
        self.__ram_Operation174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Transition173"):
                opp_val = getattr(old_value, "ram_Transition173", None)
                if opp_val == self:
                    setattr(old_value, "ram_Transition173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Transition173"):
                opp_val = getattr(value, "ram_Transition173", None)
                setattr(value, "ram_Transition173", self)

    @property
    def ram_Operation148(self):
        return self.__ram_Operation148

    @ram_Operation148.setter
    def ram_Operation148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation148", None)
        self.__ram_Operation148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_OperationMapping147"):
                opp_val = getattr(old_value, "ram_OperationMapping147", None)
                if opp_val == self:
                    setattr(old_value, "ram_OperationMapping147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_OperationMapping147"):
                opp_val = getattr(value, "ram_OperationMapping147", None)
                setattr(value, "ram_OperationMapping147", self)

    @property
    def ram_Operation72(self):
        return self.__ram_Operation72

    @ram_Operation72.setter
    def ram_Operation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation72", None)
        self.__ram_Operation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Message71"):
                opp_val = getattr(old_value, "ram_Message71", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message71"):
                opp_val = getattr(value, "ram_Message71", None)
                setattr(value, "ram_Message71", self)

    @property
    def ram_Operation145(self):
        return self.__ram_Operation145

    @ram_Operation145.setter
    def ram_Operation145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation145", None)
        self.__ram_Operation145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_OperationMapping144"):
                opp_val = getattr(old_value, "ram_OperationMapping144", None)
                if opp_val == self:
                    setattr(old_value, "ram_OperationMapping144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_OperationMapping144"):
                opp_val = getattr(value, "ram_OperationMapping144", None)
                setattr(value, "ram_OperationMapping144", self)

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
            if hasattr(old_value, "ram_Type30"):
                opp_val = getattr(old_value, "ram_Type30", None)
                if opp_val == self:
                    setattr(old_value, "ram_Type30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Type30"):
                opp_val = getattr(value, "ram_Type30", None)
                setattr(value, "ram_Type30", self)

    @property
    def ram_Operation43(self):
        return self.__ram_Operation43

    @ram_Operation43.setter
    def ram_Operation43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation43", None)
        self.__ram_Operation43 = value
        
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
    def ram_Operation32(self):
        return self.__ram_Operation32

    @ram_Operation32.setter
    def ram_Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation32", None)
        self.__ram_Operation32 = value if value is not None else set()
        
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
    def ram_Operation117(self):
        return self.__ram_Operation117

    @ram_Operation117.setter
    def ram_Operation117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation117", None)
        self.__ram_Operation117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Classifier116"):
                opp_val = getattr(old_value, "ram_Classifier116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Classifier116"):
                opp_val = getattr(value, "ram_Classifier116", None)
                if opp_val is None:
                    setattr(value, "ram_Classifier116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Operation57(self):
        return self.__ram_Operation57

    @ram_Operation57.setter
    def ram_Operation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation57", None)
        self.__ram_Operation57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_AspectMessageView56"):
                opp_val = getattr(old_value, "ram_AspectMessageView56", None)
                if opp_val == self:
                    setattr(old_value, "ram_AspectMessageView56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_AspectMessageView56"):
                opp_val = getattr(value, "ram_AspectMessageView56", None)
                setattr(value, "ram_AspectMessageView56", self)

class ram_Gate(MessageEnd, NamedElement):

    pass
class ram_Type(NamedElement):

    pass
class ram_State(NamedElement):

    pass
class ram_StateView(NamedElement):

    pass
class ram_MappableElement(NamedElement):

    pass
class ram_Aspect(NamedElement):

    pass