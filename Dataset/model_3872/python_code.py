from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InstantiationType(Enum):
    Depends = "Depends"
    Extends = "Extends"
class OperationType(Enum):
    Normal = "Normal"
    Constructor = "Constructor"
    Destructor = "Destructor"
class InteractionOperatorKind(Enum):
    alt = "alt"
    opt = "opt"
    loop = "loop"
    disruptable = "disruptable"
    critical = "critical"
class RAMVisibilityType(Enum):
    public = "public"
    protected = "protected"
    private = "private"
    package = "package"
class MessageSort(Enum):
    synchCall = "synchCall"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class ReferenceType(Enum):
    Composition = "Composition"
    Aggregation = "Aggregation"
    Regular = "Regular"


############################################
# Definition of Classes
############################################

class ram_TracingMap:

    pass
class ram_Traceable(ABC):

    pass
class Substitution:

    pass
class ram_TransitionSubstitution(Substitution):

    pass
class ram_Substitution:

    pass
class ram_StateMachine:

    pass
class ram_Constraint:

    pass
class ram_ParameterMapping:

    pass
class ram_AttributeMapping:

    pass
class ram_OperationMapping:

    pass
class ram_ClassifierMapping:

    pass
class ram_ContainerMap:

    pass
class RCollection:

    pass
class ram_RSequence(RCollection):

    pass
class ram_RSet(RCollection):

    pass
class ram_NewLayoutElement:

    def __init__(self, x: float, y: float, ram_NewLayoutElement: "ram_ElementMap" = None):
        self.x = x
        self.y = y
        self.ram_NewLayoutElement = ram_NewLayoutElement
        
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
    def ram_NewLayoutElement(self):
        return self.__ram_NewLayoutElement

    @ram_NewLayoutElement.setter
    def ram_NewLayoutElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_NewLayoutElement__ram_NewLayoutElement", None)
        self.__ram_NewLayoutElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_ElementMap108"):
                opp_val = getattr(old_value, "ram_ElementMap108", None)
                if opp_val == self:
                    setattr(old_value, "ram_ElementMap108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ElementMap108"):
                opp_val = getattr(value, "ram_ElementMap108", None)
                setattr(value, "ram_ElementMap108", self)

class ram_ElementMap:

    pass
class ram_EObject:

    pass
class LiteralSpecification:

    pass
class ram_LiteralChar(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ram_LiteralFloat(LiteralSpecification):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class ram_LiteralLong(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ram_LiteralNull(LiteralSpecification):

    pass
class ram_LiteralDouble(LiteralSpecification):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
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

class ram_LiteralByte(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ram_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
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
class ram_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class ram_LiteralSpecification(ValueSpecification):

    pass
class ram_EnumLiteralValue(ValueSpecification):

    pass
class ram_ParameterValue(ValueSpecification):

    pass
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
                    

class ram_AssignmentStatement(InteractionFragment):

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
class ram_TemporaryProperty(ABC):

    pass
class ram_ValueSpecification(ABC):

    pass
class ram_Message:

    def __init__(self, selfMessage: bool, messageSort: str, Message: "ram_Interaction" = None, ram_Message70: "ram_ValueSpecification" = None, ram_Message72: set["ram_TemporaryProperty"] = None, ram_Message75: "ram_MessageEnd" = None, ram_Message: "ram_MessageEnd" = None, ram_Message59: "ram_MessageEnd" = None, ram_Message62: "ram_Operation" = None, ram_Message65: "ram_StructuralFeature" = None, ram_Message67: set["ram_ParameterValueMapping"] = None, messages: "ram_Interaction" = None):
        self.selfMessage = selfMessage
        self.messageSort = messageSort
        self.Message = Message
        self.ram_Message70 = ram_Message70
        self.ram_Message72 = ram_Message72 if ram_Message72 is not None else set()
        self.ram_Message75 = ram_Message75
        self.ram_Message = ram_Message
        self.ram_Message59 = ram_Message59
        self.ram_Message62 = ram_Message62
        self.ram_Message65 = ram_Message65
        self.ram_Message67 = ram_Message67 if ram_Message67 is not None else set()
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
    def ram_Message59(self):
        return self.__ram_Message59

    @ram_Message59.setter
    def ram_Message59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message59", None)
        self.__ram_Message59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd60"):
                opp_val = getattr(old_value, "ram_MessageEnd60", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd60"):
                opp_val = getattr(value, "ram_MessageEnd60", None)
                setattr(value, "ram_MessageEnd60", self)

    @property
    def ram_Message62(self):
        return self.__ram_Message62

    @ram_Message62.setter
    def ram_Message62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message62", None)
        self.__ram_Message62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Operation63"):
                opp_val = getattr(old_value, "ram_Operation63", None)
                if opp_val == self:
                    setattr(old_value, "ram_Operation63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Operation63"):
                opp_val = getattr(value, "ram_Operation63", None)
                setattr(value, "ram_Operation63", self)

    @property
    def ram_Message65(self):
        return self.__ram_Message65

    @ram_Message65.setter
    def ram_Message65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message65", None)
        self.__ram_Message65 = value
        
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
    def ram_Message67(self):
        return self.__ram_Message67

    @ram_Message67.setter
    def ram_Message67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message67", None)
        self.__ram_Message67 = value if value is not None else set()
        
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
    def ram_Message72(self):
        return self.__ram_Message72

    @ram_Message72.setter
    def ram_Message72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message72", None)
        self.__ram_Message72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_TemporaryProperty"):
                    opp_val = getattr(item, "ram_TemporaryProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_TemporaryProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_TemporaryProperty"):
                    opp_val = getattr(item, "ram_TemporaryProperty", None)
                    
                    setattr(item, "ram_TemporaryProperty", self)
                    

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
    def ram_Message75(self):
        return self.__ram_Message75

    @ram_Message75.setter
    def ram_Message75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Message__ram_Message75", None)
        self.__ram_Message75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_MessageEnd74"):
                opp_val = getattr(old_value, "ram_MessageEnd74", None)
                if opp_val == self:
                    setattr(old_value, "ram_MessageEnd74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_MessageEnd74"):
                opp_val = getattr(value, "ram_MessageEnd74", None)
                setattr(value, "ram_MessageEnd74", self)

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
            if hasattr(old_value, "ram_ValueSpecification"):
                opp_val = getattr(old_value, "ram_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ram_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ValueSpecification"):
                opp_val = getattr(value, "ram_ValueSpecification", None)
                setattr(value, "ram_ValueSpecification", self)

class ram_Lifeline:

    pass
class FragmentContainer:

    pass
class ram_InteractionOperand(FragmentContainer):

    pass
class ram_MessageEnd(ABC):

    pass
class ram_InteractionFragment(ABC):

    pass
class ram_Interaction(FragmentContainer):

    pass
class AbstractMessageView:

    pass
class ram_MessageViewReference(AbstractMessageView):

    pass
class ram_MessageView(AbstractMessageView):

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
            if hasattr(old_value, "ram_ObjectType164"):
                opp_val = getattr(old_value, "ram_ObjectType164", None)
                if opp_val == self:
                    setattr(old_value, "ram_ObjectType164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ObjectType164"):
                opp_val = getattr(value, "ram_ObjectType164", None)
                setattr(value, "ram_ObjectType164", self)

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RChar(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RDouble(PrimitiveType):

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
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RLong(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RFloat(PrimitiveType):

    def __init__(self):
        
    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ram_RByte(PrimitiveType):

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

class ram_RBoolean(PrimitiveType):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getInstanceClassName(self) -> str:
        # TODO: Implement getInstanceClassName method
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
            if hasattr(old_value, "ram_ObjectType97"):
                opp_val = getattr(old_value, "ram_ObjectType97", None)
                if opp_val == self:
                    setattr(old_value, "ram_ObjectType97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_ObjectType97"):
                opp_val = getattr(value, "ram_ObjectType97", None)
                setattr(value, "ram_ObjectType97", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ObjectType:

    pass
class ram_PrimitiveType(ImplementationClass, ObjectType):

    pass
class TypedElement:

    pass
class ram_StructuralFeature(TypedElement):

    def __init__(self, static: bool, ram_StructuralFeature: "ram_Message" = None, ram_StructuralFeature85: "ram_StructuralFeatureValue" = None, ram_StructuralFeature175: "ram_AssignmentStatement" = None):
        self.static = static
        self.ram_StructuralFeature = ram_StructuralFeature
        self.ram_StructuralFeature85 = ram_StructuralFeature85
        self.ram_StructuralFeature175 = ram_StructuralFeature175
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def ram_StructuralFeature85(self):
        return self.__ram_StructuralFeature85

    @ram_StructuralFeature85.setter
    def ram_StructuralFeature85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature85", None)
        self.__ram_StructuralFeature85 = value
        
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
    def ram_StructuralFeature175(self):
        return self.__ram_StructuralFeature175

    @ram_StructuralFeature175.setter
    def ram_StructuralFeature175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_StructuralFeature__ram_StructuralFeature175", None)
        self.__ram_StructuralFeature175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_AssignmentStatement"):
                opp_val = getattr(old_value, "ram_AssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "ram_AssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_AssignmentStatement"):
                opp_val = getattr(value, "ram_AssignmentStatement", None)
                setattr(value, "ram_AssignmentStatement", self)

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
            if hasattr(old_value, "ram_Message65"):
                opp_val = getattr(old_value, "ram_Message65", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message65"):
                opp_val = getattr(value, "ram_Message65", None)
                setattr(value, "ram_Message65", self)

class Property:

    pass
class ram_Reference(TemporaryProperty, Property):

    pass
class ram_AssociationEnd(Property):

    def __init__(self, navigable: bool, ends: "ram_Association" = None, associationEnds: "ram_Classifier" = None, ram_AssociationEnd: "ram_COREModelReuse" = None, AssociationEnd: "ram_Association" = None, AssociationEnd113: "ram_Classifier" = None):
        self.navigable = navigable
        self.ends = ends
        self.associationEnds = associationEnds
        self.ram_AssociationEnd = ram_AssociationEnd
        self.AssociationEnd = AssociationEnd
        self.AssociationEnd113 = AssociationEnd113
        
    @property
    def navigable(self) -> bool:
        return self.__navigable

    @navigable.setter
    def navigable(self, navigable: bool):
        self.__navigable = navigable

    @property
    def ram_AssociationEnd(self):
        return self.__ram_AssociationEnd

    @ram_AssociationEnd.setter
    def ram_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__ram_AssociationEnd", None)
        self.__ram_AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_COREModelReuse"):
                opp_val = getattr(old_value, "ram_COREModelReuse", None)
                if opp_val == self:
                    setattr(old_value, "ram_COREModelReuse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_COREModelReuse"):
                opp_val = getattr(value, "ram_COREModelReuse", None)
                setattr(value, "ram_COREModelReuse", self)

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
    def AssociationEnd113(self):
        return self.__AssociationEnd113

    @AssociationEnd113.setter
    def AssociationEnd113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_AssociationEnd__AssociationEnd113", None)
        self.__AssociationEnd113 = value
        
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

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getOppositeEnd(self) -> str:
        # TODO: Implement getOppositeEnd method
        pass

class Classifier:

    pass
class ram_ImplementationClass(Classifier):

    def __init__(self, instanceClassName: str, interface: bool):
        self.instanceClassName = instanceClassName
        self.interface = interface
        
    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

class ram_Class(Classifier):

    def __init__(self, abstract: bool, ram_Class: set["ram_Attribute"] = None):
        self.abstract = abstract
        self.ram_Class = ram_Class if ram_Class is not None else set()
        
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
                    

class Traceable:

    pass
class MappableElement:

    pass
class ram_ObjectType(Type, MappableElement):

    pass
class ram_Attribute(Traceable, StructuralFeature, TemporaryProperty, MappableElement):

    pass
class ram_Parameter(TypedElement, MappableElement):

    pass
class CORENamedElement:

    pass
class ram_NamedElement(CORENamedElement):

    pass
class ram_COREModelReuse:

    pass
class ram_AbstractMessageView(ABC):

    pass
class ram_StructuralView:

    pass
class COREModel:

    pass
class NamedElement:

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
            if hasattr(old_value, "ram_Lifeline55"):
                opp_val = getattr(old_value, "ram_Lifeline55", None)
                if opp_val == self:
                    setattr(old_value, "ram_Lifeline55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Lifeline55"):
                opp_val = getattr(value, "ram_Lifeline55", None)
                setattr(value, "ram_Lifeline55", self)

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

class ram_Operation(NamedElement, Traceable, MappableElement):

    def __init__(self, abstract: bool, extendedVisibility: str, static: bool, operationType: str, ram_Operation: "ram_Type" = None, ram_Operation25: set["ram_Parameter"] = None, ram_Operation36: "ram_MessageView" = None, ram_Operation50: "ram_AspectMessageView" = None, ram_Operation63: "ram_Message" = None, ram_Operation111: "ram_Classifier" = None, ram_Operation146: "ram_Transition" = None):
        self.abstract = abstract
        self.extendedVisibility = extendedVisibility
        self.static = static
        self.operationType = operationType
        self.ram_Operation = ram_Operation
        self.ram_Operation25 = ram_Operation25 if ram_Operation25 is not None else set()
        self.ram_Operation36 = ram_Operation36
        self.ram_Operation50 = ram_Operation50
        self.ram_Operation63 = ram_Operation63
        self.ram_Operation111 = ram_Operation111
        self.ram_Operation146 = ram_Operation146
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def extendedVisibility(self) -> str:
        return self.__extendedVisibility

    @extendedVisibility.setter
    def extendedVisibility(self, extendedVisibility: str):
        self.__extendedVisibility = extendedVisibility

    @property
    def operationType(self) -> str:
        return self.__operationType

    @operationType.setter
    def operationType(self, operationType: str):
        self.__operationType = operationType

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

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
            if hasattr(old_value, "ram_Message62"):
                opp_val = getattr(old_value, "ram_Message62", None)
                if opp_val == self:
                    setattr(old_value, "ram_Message62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Message62"):
                opp_val = getattr(value, "ram_Message62", None)
                setattr(value, "ram_Message62", self)

    @property
    def ram_Operation111(self):
        return self.__ram_Operation111

    @ram_Operation111.setter
    def ram_Operation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation111", None)
        self.__ram_Operation111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Classifier110"):
                opp_val = getattr(old_value, "ram_Classifier110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Classifier110"):
                opp_val = getattr(value, "ram_Classifier110", None)
                if opp_val is None:
                    setattr(value, "ram_Classifier110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Operation25(self):
        return self.__ram_Operation25

    @ram_Operation25.setter
    def ram_Operation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation25", None)
        self.__ram_Operation25 = value if value is not None else set()
        
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
    def ram_Operation(self):
        return self.__ram_Operation

    @ram_Operation.setter
    def ram_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation", None)
        self.__ram_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Type23"):
                opp_val = getattr(old_value, "ram_Type23", None)
                if opp_val == self:
                    setattr(old_value, "ram_Type23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Type23"):
                opp_val = getattr(value, "ram_Type23", None)
                setattr(value, "ram_Type23", self)

    @property
    def ram_Operation50(self):
        return self.__ram_Operation50

    @ram_Operation50.setter
    def ram_Operation50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation50", None)
        self.__ram_Operation50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_AspectMessageView49"):
                opp_val = getattr(old_value, "ram_AspectMessageView49", None)
                if opp_val == self:
                    setattr(old_value, "ram_AspectMessageView49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_AspectMessageView49"):
                opp_val = getattr(value, "ram_AspectMessageView49", None)
                setattr(value, "ram_AspectMessageView49", self)

    @property
    def ram_Operation36(self):
        return self.__ram_Operation36

    @ram_Operation36.setter
    def ram_Operation36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation36", None)
        self.__ram_Operation36 = value
        
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
    def ram_Operation146(self):
        return self.__ram_Operation146

    @ram_Operation146.setter
    def ram_Operation146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Operation__ram_Operation146", None)
        self.__ram_Operation146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_Transition145"):
                opp_val = getattr(old_value, "ram_Transition145", None)
                if opp_val == self:
                    setattr(old_value, "ram_Transition145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Transition145"):
                opp_val = getattr(value, "ram_Transition145", None)
                setattr(value, "ram_Transition145", self)

class ram_CheckState(NamedElement):

    pass
class ram_Transition(NamedElement):

    pass
class ram_Gate(MessageEnd, NamedElement):

    pass
class ram_AspectMessageView(NamedElement, AbstractMessageView):

    pass
class ram_REnumLiteral(NamedElement):

    pass
class ram_Aspect(NamedElement, COREModel):

    pass
class ram_Type(NamedElement):

    pass
class ram_Association(NamedElement):

    pass
class ram_Classifier(Traceable, ObjectType):

    def __init__(self, dataType: bool, ram_Classifier: "ram_StructuralView" = None, Classifier: "ram_AssociationEnd" = None, ram_Classifier110: set["ram_Operation"] = None, classifier: set["ram_AssociationEnd"] = None, ram_Classifier115: set["ram_TypeParameter"] = None, ram_Classifier118: "ram_Classifier" = None, ram_Classifier116: set["ram_Classifier"] = None, ram_Classifier131: "ram_StateView" = None):
        self.dataType = dataType
        self.ram_Classifier = ram_Classifier
        self.Classifier = Classifier
        self.ram_Classifier110 = ram_Classifier110 if ram_Classifier110 is not None else set()
        self.classifier = classifier if classifier is not None else set()
        self.ram_Classifier115 = ram_Classifier115 if ram_Classifier115 is not None else set()
        self.ram_Classifier118 = ram_Classifier118
        self.ram_Classifier116 = ram_Classifier116 if ram_Classifier116 is not None else set()
        self.ram_Classifier131 = ram_Classifier131
        
    @property
    def dataType(self) -> bool:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: bool):
        self.__dataType = dataType

    @property
    def ram_Classifier110(self):
        return self.__ram_Classifier110

    @ram_Classifier110.setter
    def ram_Classifier110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier110", None)
        self.__ram_Classifier110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Operation111"):
                    opp_val = getattr(item, "ram_Operation111", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Operation111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Operation111"):
                    opp_val = getattr(item, "ram_Operation111", None)
                    
                    setattr(item, "ram_Operation111", self)
                    

    @property
    def classifier(self):
        return self.__classifier

    @classifier.setter
    def classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__classifier", None)
        self.__classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationEnd113"):
                    opp_val = getattr(item, "AssociationEnd113", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationEnd113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationEnd113"):
                    opp_val = getattr(item, "AssociationEnd113", None)
                    
                    setattr(item, "AssociationEnd113", self)
                    

    @property
    def ram_Classifier(self):
        return self.__ram_Classifier

    @ram_Classifier.setter
    def ram_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier", None)
        self.__ram_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_StructuralView12"):
                opp_val = getattr(old_value, "ram_StructuralView12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_StructuralView12"):
                opp_val = getattr(value, "ram_StructuralView12", None)
                if opp_val is None:
                    setattr(value, "ram_StructuralView12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ram_Classifier118(self):
        return self.__ram_Classifier118

    @ram_Classifier118.setter
    def ram_Classifier118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier118", None)
        self.__ram_Classifier118 = value
        
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
    def ram_Classifier116(self):
        return self.__ram_Classifier116

    @ram_Classifier116.setter
    def ram_Classifier116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier116", None)
        self.__ram_Classifier116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_Classifier118"):
                    opp_val = getattr(item, "ram_Classifier118", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_Classifier118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_Classifier118"):
                    opp_val = getattr(item, "ram_Classifier118", None)
                    
                    setattr(item, "ram_Classifier118", self)
                    

    @property
    def ram_Classifier115(self):
        return self.__ram_Classifier115

    @ram_Classifier115.setter
    def ram_Classifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier115", None)
        self.__ram_Classifier115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ram_TypeParameter"):
                    opp_val = getattr(item, "ram_TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ram_TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ram_TypeParameter"):
                    opp_val = getattr(item, "ram_TypeParameter", None)
                    
                    setattr(item, "ram_TypeParameter", self)
                    

    @property
    def ram_Classifier131(self):
        return self.__ram_Classifier131

    @ram_Classifier131.setter
    def ram_Classifier131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__ram_Classifier131", None)
        self.__ram_Classifier131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ram_StateView130"):
                opp_val = getattr(old_value, "ram_StateView130", None)
                if opp_val == self:
                    setattr(old_value, "ram_StateView130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_StateView130"):
                opp_val = getattr(value, "ram_StateView130", None)
                setattr(value, "ram_StateView130", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ram_Classifier__Classifier", None)
        self.__Classifier = value
        
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

class COREModelElement:

    pass
class ram_MappableElement(NamedElement, COREModelElement):

    pass
class ram_WovenAspect(NamedElement):

    pass
class ram_StateView(NamedElement):

    pass
class ram_Layout:

    pass
class ram_Instantiation:

    def __init__(self, type: str, ram_Instantiation: "ram_Aspect" = None):
        self.type = type
        self.ram_Instantiation = ram_Instantiation
        
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
            if hasattr(old_value, "ram_Aspect4"):
                opp_val = getattr(old_value, "ram_Aspect4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ram_Aspect4"):
                opp_val = getattr(value, "ram_Aspect4", None)
                if opp_val is None:
                    setattr(value, "ram_Aspect4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
