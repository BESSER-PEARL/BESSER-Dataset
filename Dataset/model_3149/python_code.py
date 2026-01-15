from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DmxUnaryOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    NOT = "NOT"
class DmxBinaryOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    POWER = "POWER"
    MODULO = "MODULO"
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    GREATER = "GREATER"
    IN = "IN"
    UNTIL = "UNTIL"
    SINGLE_ARROW = "SINGLE_ARROW"
    DOUBLE_ARROW = "DOUBLE_ARROW"
class DmxBaseType(Enum):
    UNDEFINED = "UNDEFINED"
    AMBIGUOUS = "AMBIGUOUS"
    VOID = "VOID"
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"
    TEXT = "TEXT"
    IDENTIFIER = "IDENTIFIER"
    TIMEPOINT = "TIMEPOINT"
    ENUM = "ENUM"
    STATE = "STATE"
    STATE_EVENT = "STATE_EVENT"
    COMPLEX = "COMPLEX"
    AGGREGATE = "AGGREGATE"
    NOTIFICATION = "NOTIFICATION"
    SERVICE = "SERVICE"


############################################
# Definition of Classes
############################################

class dmx_DComplexType:

    pass
class DmxComplexObject:

    pass
class dmx_DmxDetail(DmxComplexObject):

    pass
class dmx_DmxEntity(DmxComplexObject):

    pass
class dmx_DFeature:

    pass
class dmx_IStaticReferenceTarget:

    pass
class dmx_DNamedElement:

    pass
class dmx_DType:

    pass
class dmx_DmxCallArguments:

    pass
class dmx_DNavigableMember:

    pass
class DExpression:

    pass
class dmx_DmxStaticReference(DExpression):

    def __init__(self, displayName: str, plural: bool, dmx_DmxStaticReference68: "dmx_DNavigableMember" = None, dmx_DmxStaticReference: "dmx_IStaticReferenceTarget" = None):
        self.displayName = displayName
        self.plural = plural
        self.dmx_DmxStaticReference68 = dmx_DmxStaticReference68
        self.dmx_DmxStaticReference = dmx_DmxStaticReference
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def plural(self) -> bool:
        return self.__plural

    @plural.setter
    def plural(self, plural: bool):
        self.__plural = plural

    @property
    def dmx_DmxStaticReference68(self):
        return self.__dmx_DmxStaticReference68

    @dmx_DmxStaticReference68.setter
    def dmx_DmxStaticReference68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxStaticReference__dmx_DmxStaticReference68", None)
        self.__dmx_DmxStaticReference68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DNavigableMember69"):
                opp_val = getattr(old_value, "dmx_DNavigableMember69", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DNavigableMember69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DNavigableMember69"):
                opp_val = getattr(value, "dmx_DNavigableMember69", None)
                setattr(value, "dmx_DNavigableMember69", self)

    @property
    def dmx_DmxStaticReference(self):
        return self.__dmx_DmxStaticReference

    @dmx_DmxStaticReference.setter
    def dmx_DmxStaticReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxStaticReference__dmx_DmxStaticReference", None)
        self.__dmx_DmxStaticReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_IStaticReferenceTarget"):
                opp_val = getattr(old_value, "dmx_IStaticReferenceTarget", None)
                if opp_val == self:
                    setattr(old_value, "dmx_IStaticReferenceTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_IStaticReferenceTarget"):
                opp_val = getattr(value, "dmx_IStaticReferenceTarget", None)
                setattr(value, "dmx_IStaticReferenceTarget", self)

class dmx_DmxDecimalLiteral(DExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dmx_DmxContextReference(DExpression):

    def __init__(self, all: bool, before: bool, dmx_DmxContextReference: "dmx_DNamedElement" = None):
        self.all = all
        self.before = before
        self.dmx_DmxContextReference = dmx_DmxContextReference
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def before(self) -> bool:
        return self.__before

    @before.setter
    def before(self, before: bool):
        self.__before = before

    @property
    def dmx_DmxContextReference(self):
        return self.__dmx_DmxContextReference

    @dmx_DmxContextReference.setter
    def dmx_DmxContextReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxContextReference__dmx_DmxContextReference", None)
        self.__dmx_DmxContextReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DNamedElement"):
                opp_val = getattr(old_value, "dmx_DNamedElement", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DNamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DNamedElement"):
                opp_val = getattr(value, "dmx_DNamedElement", None)
                setattr(value, "dmx_DNamedElement", self)

class dmx_DmxIfExpression(DExpression):

    pass
class dmx_DmxBooleanLiteral(DExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class dmx_DmxListExpression(DExpression):

    pass
class dmx_DmxUnaryOperation(DExpression):

    def __init__(self, operator: str, dmx_DmxUnaryOperation: "dmx_DExpression" = None):
        self.operator = operator
        self.dmx_DmxUnaryOperation = dmx_DmxUnaryOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dmx_DmxUnaryOperation(self):
        return self.__dmx_DmxUnaryOperation

    @dmx_DmxUnaryOperation.setter
    def dmx_DmxUnaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxUnaryOperation__dmx_DmxUnaryOperation", None)
        self.__dmx_DmxUnaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DExpression58"):
                opp_val = getattr(old_value, "dmx_DExpression58", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DExpression58"):
                opp_val = getattr(value, "dmx_DExpression58", None)
                setattr(value, "dmx_DExpression58", self)

class dmx_DmxUrlLiteral(DExpression):

    def __init__(self, value: str, display: str):
        self.value = value
        self.display = display
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def display(self) -> str:
        return self.__display

    @display.setter
    def display(self, display: str):
        self.__display = display

class dmx_DmxUndefinedLiteral(DExpression):

    pass
class dmx_DmxBinaryOperation(DExpression):

    def __init__(self, operator: str, dmx_DmxBinaryOperation: "dmx_DExpression" = None, dmx_DmxBinaryOperation51: "dmx_DExpression" = None):
        self.operator = operator
        self.dmx_DmxBinaryOperation = dmx_DmxBinaryOperation
        self.dmx_DmxBinaryOperation51 = dmx_DmxBinaryOperation51
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dmx_DmxBinaryOperation(self):
        return self.__dmx_DmxBinaryOperation

    @dmx_DmxBinaryOperation.setter
    def dmx_DmxBinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxBinaryOperation__dmx_DmxBinaryOperation", None)
        self.__dmx_DmxBinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DExpression49"):
                opp_val = getattr(old_value, "dmx_DExpression49", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DExpression49"):
                opp_val = getattr(value, "dmx_DExpression49", None)
                setattr(value, "dmx_DExpression49", self)

    @property
    def dmx_DmxBinaryOperation51(self):
        return self.__dmx_DmxBinaryOperation51

    @dmx_DmxBinaryOperation51.setter
    def dmx_DmxBinaryOperation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxBinaryOperation__dmx_DmxBinaryOperation51", None)
        self.__dmx_DmxBinaryOperation51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DExpression52"):
                opp_val = getattr(old_value, "dmx_DExpression52", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DExpression52"):
                opp_val = getattr(value, "dmx_DExpression52", None)
                setattr(value, "dmx_DExpression52", self)

class dmx_DmxDateLiteral(DExpression):

    def __init__(self, value: date):
        self.value = value
        
    @property
    def value(self) -> date:
        return self.__value

    @value.setter
    def value(self, value: date):
        self.__value = value

class dmx_DmxCastExpression(DExpression):

    pass
class dmx_DmxFunctionCall(DExpression):

    pass
class dmx_DmxNaturalLiteral(DExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class dmx_DmxStringLiteral(DExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dmx_DmxInstanceOfExpression(DExpression):

    pass
class dmx_DmxAssignment(DExpression):

    pass
class dmx_DmxMemberNavigation(DExpression):

    def __init__(self, explicitOperationCall: bool, before: bool, dmx_DmxMemberNavigation: "dmx_DNavigableMember" = None, dmx_DmxMemberNavigation36: "dmx_DExpression" = None, dmx_DmxMemberNavigation39: "dmx_DmxCallArguments" = None):
        self.explicitOperationCall = explicitOperationCall
        self.before = before
        self.dmx_DmxMemberNavigation = dmx_DmxMemberNavigation
        self.dmx_DmxMemberNavigation36 = dmx_DmxMemberNavigation36
        self.dmx_DmxMemberNavigation39 = dmx_DmxMemberNavigation39
        
    @property
    def before(self) -> bool:
        return self.__before

    @before.setter
    def before(self, before: bool):
        self.__before = before

    @property
    def explicitOperationCall(self) -> bool:
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall

    @property
    def dmx_DmxMemberNavigation39(self):
        return self.__dmx_DmxMemberNavigation39

    @dmx_DmxMemberNavigation39.setter
    def dmx_DmxMemberNavigation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxMemberNavigation__dmx_DmxMemberNavigation39", None)
        self.__dmx_DmxMemberNavigation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxCallArguments"):
                opp_val = getattr(old_value, "dmx_DmxCallArguments", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxCallArguments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxCallArguments"):
                opp_val = getattr(value, "dmx_DmxCallArguments", None)
                setattr(value, "dmx_DmxCallArguments", self)

    @property
    def dmx_DmxMemberNavigation(self):
        return self.__dmx_DmxMemberNavigation

    @dmx_DmxMemberNavigation.setter
    def dmx_DmxMemberNavigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxMemberNavigation__dmx_DmxMemberNavigation", None)
        self.__dmx_DmxMemberNavigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DNavigableMember34"):
                opp_val = getattr(old_value, "dmx_DNavigableMember34", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DNavigableMember34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DNavigableMember34"):
                opp_val = getattr(value, "dmx_DNavigableMember34", None)
                setattr(value, "dmx_DNavigableMember34", self)

    @property
    def dmx_DmxMemberNavigation36(self):
        return self.__dmx_DmxMemberNavigation36

    @dmx_DmxMemberNavigation36.setter
    def dmx_DmxMemberNavigation36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxMemberNavigation__dmx_DmxMemberNavigation36", None)
        self.__dmx_DmxMemberNavigation36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DExpression37"):
                opp_val = getattr(old_value, "dmx_DExpression37", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DExpression37"):
                opp_val = getattr(value, "dmx_DExpression37", None)
                setattr(value, "dmx_DExpression37", self)

class dmx_DmxFilterTypeDescriptor:

    def __init__(self, single: str, collection: bool, multiTyped: bool, dmx_DmxFilterTypeDescriptor: "dmx_DmxFilter" = None, dmx_DmxFilterTypeDescriptor17: "dmx_DmxBaseTypeSet" = None, dmx_DmxFilterTypeDescriptor21: "dmx_DmxFilterParameter" = None):
        self.single = single
        self.collection = collection
        self.multiTyped = multiTyped
        self.dmx_DmxFilterTypeDescriptor = dmx_DmxFilterTypeDescriptor
        self.dmx_DmxFilterTypeDescriptor17 = dmx_DmxFilterTypeDescriptor17
        self.dmx_DmxFilterTypeDescriptor21 = dmx_DmxFilterTypeDescriptor21
        
    @property
    def multiTyped(self) -> bool:
        return self.__multiTyped

    @multiTyped.setter
    def multiTyped(self, multiTyped: bool):
        self.__multiTyped = multiTyped

    @property
    def single(self) -> str:
        return self.__single

    @single.setter
    def single(self, single: str):
        self.__single = single

    @property
    def collection(self) -> bool:
        return self.__collection

    @collection.setter
    def collection(self, collection: bool):
        self.__collection = collection

    @property
    def dmx_DmxFilterTypeDescriptor17(self):
        return self.__dmx_DmxFilterTypeDescriptor17

    @dmx_DmxFilterTypeDescriptor17.setter
    def dmx_DmxFilterTypeDescriptor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxFilterTypeDescriptor__dmx_DmxFilterTypeDescriptor17", None)
        self.__dmx_DmxFilterTypeDescriptor17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxBaseTypeSet18"):
                opp_val = getattr(old_value, "dmx_DmxBaseTypeSet18", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxBaseTypeSet18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxBaseTypeSet18"):
                opp_val = getattr(value, "dmx_DmxBaseTypeSet18", None)
                setattr(value, "dmx_DmxBaseTypeSet18", self)

    @property
    def dmx_DmxFilterTypeDescriptor21(self):
        return self.__dmx_DmxFilterTypeDescriptor21

    @dmx_DmxFilterTypeDescriptor21.setter
    def dmx_DmxFilterTypeDescriptor21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxFilterTypeDescriptor__dmx_DmxFilterTypeDescriptor21", None)
        self.__dmx_DmxFilterTypeDescriptor21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilterParameter20"):
                opp_val = getattr(old_value, "dmx_DmxFilterParameter20", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxFilterParameter20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilterParameter20"):
                opp_val = getattr(value, "dmx_DmxFilterParameter20", None)
                setattr(value, "dmx_DmxFilterParameter20", self)

    @property
    def dmx_DmxFilterTypeDescriptor(self):
        return self.__dmx_DmxFilterTypeDescriptor

    @dmx_DmxFilterTypeDescriptor.setter
    def dmx_DmxFilterTypeDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxFilterTypeDescriptor__dmx_DmxFilterTypeDescriptor", None)
        self.__dmx_DmxFilterTypeDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilter13"):
                opp_val = getattr(old_value, "dmx_DmxFilter13", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxFilter13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilter13"):
                opp_val = getattr(value, "dmx_DmxFilter13", None)
                setattr(value, "dmx_DmxFilter13", self)

    def isCompatible(self, type: str) -> bool:
        # TODO: Implement isCompatible method
        pass

    def isCompatible(self, type: str, collection: bool) -> bool:
        # TODO: Implement isCompatible method
        pass

class dmx_DmxFilterParameter:

    def __init__(self, name: str, dmx_DmxFilterParameter: "dmx_DmxFilter" = None, dmx_DmxFilterParameter20: "dmx_DmxFilterTypeDescriptor" = None):
        self.name = name
        self.dmx_DmxFilterParameter = dmx_DmxFilterParameter
        self.dmx_DmxFilterParameter20 = dmx_DmxFilterParameter20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dmx_DmxFilterParameter20(self):
        return self.__dmx_DmxFilterParameter20

    @dmx_DmxFilterParameter20.setter
    def dmx_DmxFilterParameter20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxFilterParameter__dmx_DmxFilterParameter20", None)
        self.__dmx_DmxFilterParameter20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilterTypeDescriptor21"):
                opp_val = getattr(old_value, "dmx_DmxFilterTypeDescriptor21", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxFilterTypeDescriptor21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilterTypeDescriptor21"):
                opp_val = getattr(value, "dmx_DmxFilterTypeDescriptor21", None)
                setattr(value, "dmx_DmxFilterTypeDescriptor21", self)

    @property
    def dmx_DmxFilterParameter(self):
        return self.__dmx_DmxFilterParameter

    @dmx_DmxFilterParameter.setter
    def dmx_DmxFilterParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxFilterParameter__dmx_DmxFilterParameter", None)
        self.__dmx_DmxFilterParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilter11"):
                opp_val = getattr(old_value, "dmx_DmxFilter11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilter11"):
                opp_val = getattr(value, "dmx_DmxFilter11", None)
                if opp_val is None:
                    setattr(value, "dmx_DmxFilter11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DNavigableMember:

    pass
class dmx_DmxCorrelationVariable(DNavigableMember):

    pass
class dmx_DmxField(DNavigableMember):

    pass
class DPrimitive:

    pass
class dmx_DmxArchetype(DPrimitive):

    def __init__(self, baseType: str):
        self.baseType = baseType
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

class dmx_DmxBaseTypeSet:

    def __init__(self, name: str, members: str, dmx_DmxBaseTypeSet: "dmx_DmxFilter" = None, dmx_DmxBaseTypeSet18: "dmx_DmxFilterTypeDescriptor" = None):
        self.name = name
        self.members = members
        self.dmx_DmxBaseTypeSet = dmx_DmxBaseTypeSet
        self.dmx_DmxBaseTypeSet18 = dmx_DmxBaseTypeSet18
        
    @property
    def members(self) -> str:
        return self.__members

    @members.setter
    def members(self, members: str):
        self.__members = members

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dmx_DmxBaseTypeSet18(self):
        return self.__dmx_DmxBaseTypeSet18

    @dmx_DmxBaseTypeSet18.setter
    def dmx_DmxBaseTypeSet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxBaseTypeSet__dmx_DmxBaseTypeSet18", None)
        self.__dmx_DmxBaseTypeSet18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilterTypeDescriptor17"):
                opp_val = getattr(old_value, "dmx_DmxFilterTypeDescriptor17", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxFilterTypeDescriptor17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilterTypeDescriptor17"):
                opp_val = getattr(value, "dmx_DmxFilterTypeDescriptor17", None)
                setattr(value, "dmx_DmxFilterTypeDescriptor17", self)

    @property
    def dmx_DmxBaseTypeSet(self):
        return self.__dmx_DmxBaseTypeSet

    @dmx_DmxBaseTypeSet.setter
    def dmx_DmxBaseTypeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxBaseTypeSet__dmx_DmxBaseTypeSet", None)
        self.__dmx_DmxBaseTypeSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxFilter15"):
                opp_val = getattr(old_value, "dmx_DmxFilter15", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DmxFilter15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxFilter15"):
                opp_val = getattr(value, "dmx_DmxFilter15", None)
                setattr(value, "dmx_DmxFilter15", self)

class DContext:

    pass
class dmx_DExpression:

    pass
class dmx_DmxTestContext(DContext):

    pass
class INavigableMemberContainer:

    pass
class dmx_DmxPredicateWithCorrelationVariable(INavigableMemberContainer, DExpression):

    pass
class dmx_DmxComplexObject(INavigableMemberContainer, DExpression):

    pass
class dmx_DmxTest(INavigableMemberContainer):

    def __init__(self, name: str, dmx_DmxTest: "dmx_DmxModel" = None, dmx_DmxTest4: set["dmx_DmxTestContext"] = None, dmx_DmxTest6: "dmx_DExpression" = None):
        self.name = name
        self.dmx_DmxTest = dmx_DmxTest
        self.dmx_DmxTest4 = dmx_DmxTest4 if dmx_DmxTest4 is not None else set()
        self.dmx_DmxTest6 = dmx_DmxTest6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dmx_DmxTest(self):
        return self.__dmx_DmxTest

    @dmx_DmxTest.setter
    def dmx_DmxTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxTest__dmx_DmxTest", None)
        self.__dmx_DmxTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DmxModel2"):
                opp_val = getattr(old_value, "dmx_DmxModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DmxModel2"):
                opp_val = getattr(value, "dmx_DmxModel2", None)
                if opp_val is None:
                    setattr(value, "dmx_DmxModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmx_DmxTest4(self):
        return self.__dmx_DmxTest4

    @dmx_DmxTest4.setter
    def dmx_DmxTest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxTest__dmx_DmxTest4", None)
        self.__dmx_DmxTest4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dmx_DmxTestContext"):
                    opp_val = getattr(item, "dmx_DmxTestContext", None)
                    
                    if opp_val == self:
                        setattr(item, "dmx_DmxTestContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dmx_DmxTestContext"):
                    opp_val = getattr(item, "dmx_DmxTestContext", None)
                    
                    setattr(item, "dmx_DmxTestContext", self)
                    

    @property
    def dmx_DmxTest6(self):
        return self.__dmx_DmxTest6

    @dmx_DmxTest6.setter
    def dmx_DmxTest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmx_DmxTest__dmx_DmxTest6", None)
        self.__dmx_DmxTest6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmx_DExpression"):
                opp_val = getattr(old_value, "dmx_DExpression", None)
                if opp_val == self:
                    setattr(old_value, "dmx_DExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmx_DExpression"):
                opp_val = getattr(value, "dmx_DExpression", None)
                setattr(value, "dmx_DExpression", self)

class dmx_DmxFilter(DNavigableMember):

    pass
class ITypeContainer:

    pass
class DModel:

    pass
class dmx_DmxModel(ITypeContainer, DModel):

    pass