from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RuleResolutionStatus(Enum):
    RESOLUTION_UNKNOWN = "RESOLUTION_UNKNOWN"
    RESOLUTION_CONFIRMED = "RESOLUTION_CONFIRMED"
    RESOLUTION_DISCARDED = "RESOLUTION_DISCARDED"


############################################
# Definition of Classes
############################################

class CollectionOperationCallExp:

    pass
class atlext_OCL2_SelectByKind(CollectionOperationCallExp):

    def __init__(self, isExact: bool):
        self.isExact = isExact
        
        pass
    @property
    def isExact(self):
        return self.__isExact

    @isExact.setter
    def isExact(self, isExact: bool):
        self.__isExact = isExact


class JavaBody:

    pass
class atlext_OCL_GetAppliedStereotypesBody(JavaBody):

    pass
class atlext_OCL_TypedElement(ABC):

    pass
class OclModelElement:

    pass
class OclFeature:

    pass
class atlext_OCL_Attribute(OclFeature):

    def __init__(self, name: str, owningAttribute: "OclExpression" = None, attribute: "OclType" = None, OclFeature: "atlext_OCL_OclFeatureDefinition" = None):
        self.name = name
        self.owningAttribute = owningAttribute
        self.attribute = attribute
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningAttribute(self):
        return self.__owningAttribute

    @owningAttribute.setter
    def owningAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression240"):
                opp_val = getattr(old_value, "OclExpression240", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression240"):
                opp_val = getattr(value, "OclExpression240", None)
                setattr(value, "OclExpression240", self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType242"):
                opp_val = getattr(old_value, "OclType242", None)
                if opp_val == self:
                    setattr(old_value, "OclType242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType242"):
                opp_val = getattr(value, "OclType242", None)
                setattr(value, "OclType242", self)

class atlext_OCL_Operation(OclFeature):

    def __init__(self, name: str, operation: "OclType" = None, owningOperation: "OclExpression" = None, atlext_OCL_Operation: set["Parameter"] = None, OclFeature: "atlext_OCL_OclFeatureDefinition" = None):
        self.name = name
        self.operation = operation
        self.owningOperation = owningOperation
        self.atlext_OCL_Operation = atlext_OCL_Operation if atlext_OCL_Operation is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__operation", None)
        self.__operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType246"):
                opp_val = getattr(old_value, "OclType246", None)
                if opp_val == self:
                    setattr(old_value, "OclType246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType246"):
                opp_val = getattr(value, "OclType246", None)
                setattr(value, "OclType246", self)

    @property
    def atlext_OCL_Operation(self):
        return self.__atlext_OCL_Operation

    @atlext_OCL_Operation.setter
    def atlext_OCL_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__atlext_OCL_Operation", None)
        self.__atlext_OCL_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter244"):
                    opp_val = getattr(item, "Parameter244", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter244"):
                    opp_val = getattr(item, "Parameter244", None)
                    
                    setattr(item, "Parameter244", self)
                    

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__owningOperation", None)
        self.__owningOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression248"):
                opp_val = getattr(old_value, "OclExpression248", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression248"):
                opp_val = getattr(value, "OclExpression248", None)
                setattr(value, "OclExpression248", self)

class NumericType:

    pass
class atlext_OCL_RealType(NumericType):

    pass
class atlext_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class atlext_OCL_NumericType(Primitive):

    pass
class atlext_OCL_BooleanType(Primitive):

    pass
class atlext_OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class atlext_OCL_SequenceType(CollectionType):

    pass
class atlext_OCL_BagType(CollectionType):

    pass
class atlext_OCL_OrderedSetType(CollectionType):

    pass
class MapType:

    pass
class TupleType:

    pass
class atlext_OCL_SetType(CollectionType):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class OclContextDefinition:

    pass
class ResolveTempResolution:

    pass
class ContextHelper:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class OCL_atlext_EObject:

    pass
class PrimitiveExp:

    pass
class atlext_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class atlext_OCL_NumericExp(PrimitiveExp):

    pass
class atlext_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class OCL_atlext_Type:

    pass
class Attribute:

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class atlext_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class atlext_OCL_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class atlext_OCL_IterateExp(LoopExp):

    pass
class atlext_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp: "atlext_OCL_OclExpression" = None, LoopExp196: "atlext_OCL_Iterator" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NumericExp:

    pass
class atlext_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class atlext_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class OclType:

    pass
class atlext_OCL_Primitive(OclType):

    pass
class atlext_OCL_MapType(OclType):

    pass
class atlext_OCL_OclAnyType(OclType):

    pass
class atlext_OCL_CollectionType(OclType):

    pass
class atlext_OCL_OclModelElement(OclType):

    pass
class atlext_OCL_TupleType(OclType):

    pass
class OCL_TypedElement:

    pass
class ATL_LocatedElement:

    pass
class atlext_OCL_VariableDeclaration(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, id: str, varName: str, variableDeclaration: "OclType" = None, initializedVariable: "OclExpression" = None, variable: "LetExp" = None, result: "IterateExp" = None, referredVariable: set["VariableExp"] = None, atlext_OCL_VariableDeclaration: "OCL_atlext_Type" = None):
        self.id = id
        self.varName = varName
        self.variableDeclaration = variableDeclaration
        self.initializedVariable = initializedVariable
        self.variable = variable
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.atlext_OCL_VariableDeclaration = atlext_OCL_VariableDeclaration
        
        pass
    @property
    def varName(self):
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp190"):
                opp_val = getattr(old_value, "LetExp190", None)
                if opp_val == self:
                    setattr(old_value, "LetExp190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp190"):
                opp_val = getattr(value, "LetExp190", None)
                setattr(value, "LetExp190", self)

    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType186"):
                opp_val = getattr(old_value, "OclType186", None)
                if opp_val == self:
                    setattr(old_value, "OclType186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType186"):
                opp_val = getattr(value, "OclType186", None)
                setattr(value, "OclType186", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IterateExp"):
                opp_val = getattr(old_value, "IterateExp", None)
                if opp_val == self:
                    setattr(old_value, "IterateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IterateExp"):
                opp_val = getattr(value, "IterateExp", None)
                setattr(value, "IterateExp", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__referredVariable", None)
        self.__referredVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    setattr(item, "VariableExp", self)
                    

    @property
    def atlext_OCL_VariableDeclaration(self):
        return self.__atlext_OCL_VariableDeclaration

    @atlext_OCL_VariableDeclaration.setter
    def atlext_OCL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__atlext_OCL_VariableDeclaration", None)
        self.__atlext_OCL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_Type194"):
                opp_val = getattr(old_value, "OCL_atlext_Type194", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_Type194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_Type194"):
                opp_val = getattr(value, "OCL_atlext_Type194", None)
                setattr(value, "OCL_atlext_Type194", self)

    @property
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression188"):
                opp_val = getattr(old_value, "OclExpression188", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression188"):
                opp_val = getattr(value, "OclExpression188", None)
                setattr(value, "OclExpression188", self)

class atlext_OCL_OclExpression(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, implicitlyCasted: bool, oclExpression: "OclType" = None, elseExpression: "IfExp" = None, source: "PropertyCallExp" = None, elements124: "CollectionExp" = None, in_: "LetExp" = None, body: "LoopExp" = None, arguments: "OperationCallExp" = None, initExpression: "VariableDeclaration" = None, thenExpression: "IfExp" = None, body133: "Operation" = None, condition: "IfExp" = None, initExpression137: "Attribute" = None, atlext_OCL_OclExpression: "OCL_atlext_Type" = None):
        self.implicitlyCasted = implicitlyCasted
        self.oclExpression = oclExpression
        self.elseExpression = elseExpression
        self.source = source
        self.elements124 = elements124
        self.in_ = in_
        self.body = body
        self.arguments = arguments
        self.initExpression = initExpression
        self.thenExpression = thenExpression
        self.body133 = body133
        self.condition = condition
        self.initExpression137 = initExpression137
        self.atlext_OCL_OclExpression = atlext_OCL_OclExpression
        
        pass
    @property
    def implicitlyCasted(self):
        return self.__implicitlyCasted

    @implicitlyCasted.setter
    def implicitlyCasted(self, implicitlyCasted: bool):
        self.__implicitlyCasted = implicitlyCasted


    @property
    def elseExpression(self):
        return self.__elseExpression

    @elseExpression.setter
    def elseExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__elseExpression", None)
        self.__elseExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IfExp"):
                opp_val = getattr(old_value, "IfExp", None)
                if opp_val == self:
                    setattr(old_value, "IfExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IfExp"):
                opp_val = getattr(value, "IfExp", None)
                setattr(value, "IfExp", self)

    @property
    def initExpression(self):
        return self.__initExpression

    @initExpression.setter
    def initExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__initExpression", None)
        self.__initExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration129"):
                opp_val = getattr(old_value, "VariableDeclaration129", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration129"):
                opp_val = getattr(value, "VariableDeclaration129", None)
                setattr(value, "VariableDeclaration129", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PropertyCallExp122"):
                opp_val = getattr(old_value, "PropertyCallExp122", None)
                if opp_val == self:
                    setattr(old_value, "PropertyCallExp122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PropertyCallExp122"):
                opp_val = getattr(value, "PropertyCallExp122", None)
                setattr(value, "PropertyCallExp122", self)

    @property
    def thenExpression(self):
        return self.__thenExpression

    @thenExpression.setter
    def thenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__thenExpression", None)
        self.__thenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IfExp131"):
                opp_val = getattr(old_value, "IfExp131", None)
                if opp_val == self:
                    setattr(old_value, "IfExp131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IfExp131"):
                opp_val = getattr(value, "IfExp131", None)
                setattr(value, "IfExp131", self)

    @property
    def in_(self):
        return self.__in_

    @in_.setter
    def in_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__in_", None)
        self.__in_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp"):
                opp_val = getattr(old_value, "LetExp", None)
                if opp_val == self:
                    setattr(old_value, "LetExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp"):
                opp_val = getattr(value, "LetExp", None)
                setattr(value, "LetExp", self)

    @property
    def atlext_OCL_OclExpression(self):
        return self.__atlext_OCL_OclExpression

    @atlext_OCL_OclExpression.setter
    def atlext_OCL_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__atlext_OCL_OclExpression", None)
        self.__atlext_OCL_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_Type"):
                opp_val = getattr(old_value, "OCL_atlext_Type", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_Type"):
                opp_val = getattr(value, "OCL_atlext_Type", None)
                setattr(value, "OCL_atlext_Type", self)

    @property
    def arguments(self):
        return self.__arguments

    @arguments.setter
    def arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__arguments", None)
        self.__arguments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationCallExp"):
                opp_val = getattr(old_value, "OperationCallExp", None)
                if opp_val == self:
                    setattr(old_value, "OperationCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationCallExp"):
                opp_val = getattr(value, "OperationCallExp", None)
                setattr(value, "OperationCallExp", self)

    @property
    def body133(self):
        return self.__body133

    @body133.setter
    def body133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__body133", None)
        self.__body133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation"):
                opp_val = getattr(old_value, "Operation", None)
                if opp_val == self:
                    setattr(old_value, "Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation"):
                opp_val = getattr(value, "Operation", None)
                setattr(value, "Operation", self)

    @property
    def initExpression137(self):
        return self.__initExpression137

    @initExpression137.setter
    def initExpression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__initExpression137", None)
        self.__initExpression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

    @property
    def oclExpression(self):
        return self.__oclExpression

    @oclExpression.setter
    def oclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__oclExpression", None)
        self.__oclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType"):
                opp_val = getattr(old_value, "OclType", None)
                if opp_val == self:
                    setattr(old_value, "OclType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType"):
                opp_val = getattr(value, "OclType", None)
                setattr(value, "OclType", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoopExp"):
                opp_val = getattr(old_value, "LoopExp", None)
                if opp_val == self:
                    setattr(old_value, "LoopExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoopExp"):
                opp_val = getattr(value, "LoopExp", None)
                setattr(value, "LoopExp", self)

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__condition", None)
        self.__condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IfExp135"):
                opp_val = getattr(old_value, "IfExp135", None)
                if opp_val == self:
                    setattr(old_value, "IfExp135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IfExp135"):
                opp_val = getattr(value, "IfExp135", None)
                setattr(value, "IfExp135", self)

    @property
    def elements124(self):
        return self.__elements124

    @elements124.setter
    def elements124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__elements124", None)
        self.__elements124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CollectionExp"):
                opp_val = getattr(old_value, "CollectionExp", None)
                if opp_val == self:
                    setattr(old_value, "CollectionExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CollectionExp"):
                opp_val = getattr(value, "CollectionExp", None)
                setattr(value, "CollectionExp", self)

class MatchedRule:

    pass
class atlext_ATL_RuleResolutionInfo:

    def __init__(self, status: str, atlext_ATL_RuleResolutionInfo: "MatchedRule" = None, atlext_ATL_RuleResolutionInfo117: set["MatchedRule"] = None):
        self.status = status
        self.atlext_ATL_RuleResolutionInfo = atlext_ATL_RuleResolutionInfo
        self.atlext_ATL_RuleResolutionInfo117 = atlext_ATL_RuleResolutionInfo117 if atlext_ATL_RuleResolutionInfo117 is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def atlext_ATL_RuleResolutionInfo(self):
        return self.__atlext_ATL_RuleResolutionInfo

    @atlext_ATL_RuleResolutionInfo.setter
    def atlext_ATL_RuleResolutionInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleResolutionInfo__atlext_ATL_RuleResolutionInfo", None)
        self.__atlext_ATL_RuleResolutionInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedRule"):
                opp_val = getattr(old_value, "MatchedRule", None)
                if opp_val == self:
                    setattr(old_value, "MatchedRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedRule"):
                opp_val = getattr(value, "MatchedRule", None)
                setattr(value, "MatchedRule", self)

    @property
    def atlext_ATL_RuleResolutionInfo117(self):
        return self.__atlext_ATL_RuleResolutionInfo117

    @atlext_ATL_RuleResolutionInfo117.setter
    def atlext_ATL_RuleResolutionInfo117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleResolutionInfo__atlext_ATL_RuleResolutionInfo117", None)
        self.__atlext_ATL_RuleResolutionInfo117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchedRule118"):
                    opp_val = getattr(item, "MatchedRule118", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchedRule118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchedRule118"):
                    opp_val = getattr(item, "MatchedRule118", None)
                    
                    setattr(item, "MatchedRule118", self)
                    

class atlext_ATL_CallableParameter:

    def __init__(self, name: str, atlext_ATL_CallableParameter: "ATL_atlext_Type" = None, atlext_ATL_CallableParameter114: "VariableDeclaration" = None):
        self.name = name
        self.atlext_ATL_CallableParameter = atlext_ATL_CallableParameter
        self.atlext_ATL_CallableParameter114 = atlext_ATL_CallableParameter114
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def atlext_ATL_CallableParameter(self):
        return self.__atlext_ATL_CallableParameter

    @atlext_ATL_CallableParameter.setter
    def atlext_ATL_CallableParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter", None)
        self.__atlext_ATL_CallableParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type112"):
                opp_val = getattr(old_value, "ATL_atlext_Type112", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type112"):
                opp_val = getattr(value, "ATL_atlext_Type112", None)
                setattr(value, "ATL_atlext_Type112", self)

    @property
    def atlext_ATL_CallableParameter114(self):
        return self.__atlext_ATL_CallableParameter114

    @atlext_ATL_CallableParameter114.setter
    def atlext_ATL_CallableParameter114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter114", None)
        self.__atlext_ATL_CallableParameter114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration"):
                opp_val = getattr(old_value, "VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration"):
                opp_val = getattr(value, "VariableDeclaration", None)
                setattr(value, "VariableDeclaration", self)

class atlext_ATL_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class LetExp:

    pass
class CollectionExp:

    pass
class atlext_OCL_SequenceExp(CollectionExp):

    pass
class atlext_OCL_BagExp(CollectionExp):

    pass
class atlext_OCL_OrderedSetExp(CollectionExp):

    pass
class atlext_OCL_SetExp(CollectionExp):

    pass
class IfExp:

    pass
class Statement:

    pass
class atlext_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_BindingStat: "OclExpression" = None, atlext_ATL_BindingStat93: "OclExpression" = None, Statement110: "atlext_ATL_ForStat" = None, Statement102: "atlext_ATL_IfStat" = None, Statement: "atlext_ATL_ActionBlock" = None, Statement99: "atlext_ATL_IfStat" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_BindingStat = atlext_ATL_BindingStat
        self.atlext_ATL_BindingStat93 = atlext_ATL_BindingStat93
        
        pass
    @property
    def isAssignment(self):
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment


    @property
    def propertyName(self):
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName


    @property
    def atlext_ATL_BindingStat93(self):
        return self.__atlext_ATL_BindingStat93

    @atlext_ATL_BindingStat93.setter
    def atlext_ATL_BindingStat93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_BindingStat__atlext_ATL_BindingStat93", None)
        self.__atlext_ATL_BindingStat93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression94"):
                opp_val = getattr(old_value, "OclExpression94", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression94"):
                opp_val = getattr(value, "OclExpression94", None)
                setattr(value, "OclExpression94", self)

    @property
    def atlext_ATL_BindingStat(self):
        return self.__atlext_ATL_BindingStat

    @atlext_ATL_BindingStat.setter
    def atlext_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_BindingStat__atlext_ATL_BindingStat", None)
        self.__atlext_ATL_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression91"):
                opp_val = getattr(old_value, "OclExpression91", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression91"):
                opp_val = getattr(value, "OclExpression91", None)
                setattr(value, "OclExpression91", self)

class atlext_ATL_ExpressionStat(Statement):

    pass
class atlext_ATL_ForStat(Statement):

    pass
class RuleResolutionInfo:

    pass
class atlext_OCL_ResolveTempResolution(RuleResolutionInfo):

    pass
class atlext_ATL_IfStat(Statement):

    pass
class Iterator:

    pass
class InPattern:

    pass
class Rule:

    pass
class atlext_ATL_RuleWithPattern(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, superRule: set["RuleWithPattern"] = None, children: "RuleWithPattern" = None, atlext_ATL_RuleWithPattern: "InPattern" = None, Rule83: "atlext_ATL_RuleVariableDeclaration" = None, Rule86: "atlext_ATL_ActionBlock" = None, Rule: "atlext_ATL_OutPattern" = None):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.superRule = superRule if superRule is not None else set()
        self.children = children
        self.atlext_ATL_RuleWithPattern = atlext_ATL_RuleWithPattern
        
        pass
    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def isNoDefault(self):
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RuleWithPattern38"):
                opp_val = getattr(old_value, "RuleWithPattern38", None)
                if opp_val == self:
                    setattr(old_value, "RuleWithPattern38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RuleWithPattern38"):
                opp_val = getattr(value, "RuleWithPattern38", None)
                setattr(value, "RuleWithPattern38", self)

    @property
    def atlext_ATL_RuleWithPattern(self):
        return self.__atlext_ATL_RuleWithPattern

    @atlext_ATL_RuleWithPattern.setter
    def atlext_ATL_RuleWithPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__atlext_ATL_RuleWithPattern", None)
        self.__atlext_ATL_RuleWithPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InPattern"):
                opp_val = getattr(old_value, "InPattern", None)
                if opp_val == self:
                    setattr(old_value, "InPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InPattern"):
                opp_val = getattr(value, "InPattern", None)
                setattr(value, "InPattern", self)

    @property
    def superRule(self):
        return self.__superRule

    @superRule.setter
    def superRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__superRule", None)
        self.__superRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleWithPattern"):
                    opp_val = getattr(item, "RuleWithPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleWithPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleWithPattern"):
                    opp_val = getattr(item, "RuleWithPattern", None)
                    
                    setattr(item, "RuleWithPattern", self)
                    

class CallableParameter:

    pass
class PatternElement:

    pass
class atlext_ATL_InPatternElement(PatternElement):

    pass
class atlext_ATL_Callable(ABC):

    pass
class VariableDeclaration:

    pass
class atlext_OCL_TuplePart(VariableDeclaration):

    pass
class atlext_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlext_OCL_Iterator(VariableDeclaration):

    pass
class atlext_OCL_Parameter(VariableDeclaration):

    pass
class atlext_ATL_PatternElement(VariableDeclaration):

    pass
class Callable:

    pass
class atlext_ATL_ModuleCallable(Callable):

    pass
class ATL_Rule:

    pass
class OutPatternElement:

    pass
class atlext_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class Parameter:

    pass
class StaticRule:

    pass
class atlext_ATL_CalledRule(StaticRule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, atlext_ATL_CalledRule: set["Parameter"] = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atlext_ATL_CalledRule = atlext_ATL_CalledRule if atlext_ATL_CalledRule is not None else set()
        
        pass
    @property
    def isEndpoint(self):
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint


    @property
    def isEntrypoint(self):
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint


    @property
    def atlext_ATL_CalledRule(self):
        return self.__atlext_ATL_CalledRule

    @atlext_ATL_CalledRule.setter
    def atlext_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CalledRule__atlext_ATL_CalledRule", None)
        self.__atlext_ATL_CalledRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class ATL_StaticRule:

    pass
class atlext_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class ATL_RuleWithPattern:

    pass
class atlext_ATL_LazyRule(ATL_StaticRule, ATL_RuleWithPattern):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class Binding:

    pass
class RuleWithPattern:

    pass
class atlext_ATL_MatchedRule(RuleWithPattern):

    pass
class atlext_ATL_OutPatternElement(PatternElement):

    pass
class atlext_ATL_SimpleInPatternElement(InPatternElement):

    pass
class ModuleElement:

    pass
class OclModel:

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class atlext_ATL_Rule(ModuleElement):

    def __init__(self, name: str, rule: "OutPattern" = None, rule28: "ActionBlock" = None, rule30: set["RuleVariableDeclaration"] = None, ModuleElement: "atlext_ATL_Module" = None):
        self.name = name
        self.rule = rule
        self.rule28 = rule28
        self.rule30 = rule30 if rule30 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__rule", None)
        self.__rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPattern"):
                opp_val = getattr(old_value, "OutPattern", None)
                if opp_val == self:
                    setattr(old_value, "OutPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPattern"):
                opp_val = getattr(value, "OutPattern", None)
                setattr(value, "OutPattern", self)

    @property
    def rule30(self):
        return self.__rule30

    @rule30.setter
    def rule30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__rule30", None)
        self.__rule30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    setattr(item, "RuleVariableDeclaration", self)
                    

    @property
    def rule28(self):
        return self.__rule28

    @rule28.setter
    def rule28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__rule28", None)
        self.__rule28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionBlock"):
                opp_val = getattr(old_value, "ActionBlock", None)
                if opp_val == self:
                    setattr(old_value, "ActionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionBlock"):
                opp_val = getattr(value, "ActionBlock", None)
                setattr(value, "ActionBlock", self)

class PropertyCallExp:

    pass
class atlext_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, PropertyCallExp122: "atlext_OCL_OclExpression" = None, PropertyCallExp32: "atlext_ATL_Callable" = None, PropertyCallExp: "atlext_ATL_ContextHelper" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlext_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, atlext_OCL_OperationCallExp: set["ResolveTempResolution"] = None, PropertyCallExp122: "atlext_OCL_OclExpression" = None, PropertyCallExp32: "atlext_ATL_Callable" = None, PropertyCallExp: "atlext_ATL_ContextHelper" = None):
        self.operationName = operationName
        self.parentOperation = parentOperation if parentOperation is not None else set()
        self.atlext_OCL_OperationCallExp = atlext_OCL_OperationCallExp if atlext_OCL_OperationCallExp is not None else set()
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def parentOperation(self):
        return self.__parentOperation

    @parentOperation.setter
    def parentOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OperationCallExp__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression166"):
                    opp_val = getattr(item, "OclExpression166", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression166"):
                    opp_val = getattr(item, "OclExpression166", None)
                    
                    setattr(item, "OclExpression166", self)
                    

    @property
    def atlext_OCL_OperationCallExp(self):
        return self.__atlext_OCL_OperationCallExp

    @atlext_OCL_OperationCallExp.setter
    def atlext_OCL_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OperationCallExp__atlext_OCL_OperationCallExp", None)
        self.__atlext_OCL_OperationCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResolveTempResolution"):
                    opp_val = getattr(item, "ResolveTempResolution", None)
                    
                    if opp_val == self:
                        setattr(item, "ResolveTempResolution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResolveTempResolution"):
                    opp_val = getattr(item, "ResolveTempResolution", None)
                    
                    setattr(item, "ResolveTempResolution", self)
                    

class atlext_OCL_LoopExp(PropertyCallExp):

    pass
class ATL_ModuleCallable:

    pass
class atlext_ATL_StaticRule(ATL_Rule, ATL_ModuleCallable):

    pass
class ATL_Helper:

    pass
class atlext_ATL_StaticHelper(ATL_Helper, ATL_ModuleCallable):

    pass
class ATL_atlext_Type:

    pass
class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class ATL_Callable:

    pass
class ATL_ModuleElement:

    pass
class atlext_ATL_Helper(ATL_Callable, ATL_ModuleElement):

    def __init__(self, hasContext: bool, isAttribute: bool, helpers: "Query" = None, helpers16: "Library" = None, atlext_ATL_Helper: "OclFeatureDefinition" = None, atlext_ATL_Helper19: "ATL_atlext_Type" = None, atlext_ATL_Helper21: "ATL_atlext_Type" = None):
        self.hasContext = hasContext
        self.isAttribute = isAttribute
        self.helpers = helpers
        self.helpers16 = helpers16
        self.atlext_ATL_Helper = atlext_ATL_Helper
        self.atlext_ATL_Helper19 = atlext_ATL_Helper19
        self.atlext_ATL_Helper21 = atlext_ATL_Helper21
        
        pass
    @property
    def hasContext(self):
        return self.__hasContext

    @hasContext.setter
    def hasContext(self, hasContext: bool):
        self.__hasContext = hasContext


    @property
    def isAttribute(self):
        return self.__isAttribute

    @isAttribute.setter
    def isAttribute(self, isAttribute: bool):
        self.__isAttribute = isAttribute


    @property
    def helpers16(self):
        return self.__helpers16

    @helpers16.setter
    def helpers16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__helpers16", None)
        self.__helpers16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)

    @property
    def helpers(self):
        return self.__helpers

    @helpers.setter
    def helpers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__helpers", None)
        self.__helpers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Query"):
                opp_val = getattr(old_value, "Query", None)
                if opp_val == self:
                    setattr(old_value, "Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Query"):
                opp_val = getattr(value, "Query", None)
                setattr(value, "Query", self)

    @property
    def atlext_ATL_Helper(self):
        return self.__atlext_ATL_Helper

    @atlext_ATL_Helper.setter
    def atlext_ATL_Helper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper", None)
        self.__atlext_ATL_Helper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition"):
                opp_val = getattr(old_value, "OclFeatureDefinition", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition"):
                opp_val = getattr(value, "OclFeatureDefinition", None)
                setattr(value, "OclFeatureDefinition", self)

    @property
    def atlext_ATL_Helper19(self):
        return self.__atlext_ATL_Helper19

    @atlext_ATL_Helper19.setter
    def atlext_ATL_Helper19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper19", None)
        self.__atlext_ATL_Helper19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type"):
                opp_val = getattr(old_value, "ATL_atlext_Type", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type"):
                opp_val = getattr(value, "ATL_atlext_Type", None)
                setattr(value, "ATL_atlext_Type", self)

    @property
    def atlext_ATL_Helper21(self):
        return self.__atlext_ATL_Helper21

    @atlext_ATL_Helper21.setter
    def atlext_ATL_Helper21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper21", None)
        self.__atlext_ATL_Helper21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type22"):
                opp_val = getattr(old_value, "ATL_atlext_Type22", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type22"):
                opp_val = getattr(value, "ATL_atlext_Type22", None)
                setattr(value, "ATL_atlext_Type22", self)

class OclExpression:

    pass
class atlext_OCL_LetExp(OclExpression):

    pass
class atlext_OCL_JavaBody(OclExpression):

    pass
class atlext_OCL_PropertyCallExp(OclExpression):

    def __init__(self, isStaticCall: bool, polymorphicCalledBy: set["ContextHelper"] = None, appliedProperty: "OclExpression" = None, atlext_OCL_PropertyCallExp: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp157: set["OCL_atlext_EObject"] = None, atlext_OCL_PropertyCallExp160: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp163: "Callable" = None, OclExpression42: "atlext_ATL_InPattern" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression152: "atlext_OCL_MapElement" = None, OclExpression96: "atlext_ATL_IfStat" = None, OclExpression248: "atlext_OCL_Operation" = None, OclExpression71: "atlext_ATL_Binding" = None, OclExpression67: "atlext_ATL_ForEachOutPatternElement" = None, OclExpression89: "atlext_ATL_ExpressionStat" = None, OclExpression201: "atlext_OCL_OclType" = None, OclExpression169: "atlext_OCL_LoopExp" = None, OclExpression94: "atlext_ATL_BindingStat" = None, OclExpression178: "atlext_OCL_LetExp" = None, OclExpression184: "atlext_OCL_IfExp" = None, OclExpression188: "atlext_OCL_VariableDeclaration" = None, OclExpression180: "atlext_OCL_IfExp" = None, OclExpression149: "atlext_OCL_MapElement" = None, OclExpression107: "atlext_ATL_ForStat" = None, OclExpression166: "atlext_OCL_OperationCallExp" = None, OclExpression154: "atlext_OCL_PropertyCallExp" = None, OclExpression91: "atlext_ATL_BindingStat" = None, OclExpression65: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression182: "atlext_OCL_IfExp" = None, OclExpression240: "atlext_OCL_Attribute" = None, OclExpression142: "atlext_OCL_CollectionExp" = None):
        self.isStaticCall = isStaticCall
        self.polymorphicCalledBy = polymorphicCalledBy if polymorphicCalledBy is not None else set()
        self.appliedProperty = appliedProperty
        self.atlext_OCL_PropertyCallExp = atlext_OCL_PropertyCallExp
        self.atlext_OCL_PropertyCallExp157 = atlext_OCL_PropertyCallExp157 if atlext_OCL_PropertyCallExp157 is not None else set()
        self.atlext_OCL_PropertyCallExp160 = atlext_OCL_PropertyCallExp160
        self.atlext_OCL_PropertyCallExp163 = atlext_OCL_PropertyCallExp163
        
        pass
    @property
    def isStaticCall(self):
        return self.__isStaticCall

    @isStaticCall.setter
    def isStaticCall(self, isStaticCall: bool):
        self.__isStaticCall = isStaticCall


    @property
    def polymorphicCalledBy(self):
        return self.__polymorphicCalledBy

    @polymorphicCalledBy.setter
    def polymorphicCalledBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__polymorphicCalledBy", None)
        self.__polymorphicCalledBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContextHelper"):
                    opp_val = getattr(item, "ContextHelper", None)
                    
                    if opp_val == self:
                        setattr(item, "ContextHelper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContextHelper"):
                    opp_val = getattr(item, "ContextHelper", None)
                    
                    setattr(item, "ContextHelper", self)
                    

    @property
    def atlext_OCL_PropertyCallExp160(self):
        return self.__atlext_OCL_PropertyCallExp160

    @atlext_OCL_PropertyCallExp160.setter
    def atlext_OCL_PropertyCallExp160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp160", None)
        self.__atlext_OCL_PropertyCallExp160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_EObject161"):
                opp_val = getattr(old_value, "OCL_atlext_EObject161", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject161"):
                opp_val = getattr(value, "OCL_atlext_EObject161", None)
                setattr(value, "OCL_atlext_EObject161", self)

    @property
    def atlext_OCL_PropertyCallExp157(self):
        return self.__atlext_OCL_PropertyCallExp157

    @atlext_OCL_PropertyCallExp157.setter
    def atlext_OCL_PropertyCallExp157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp157", None)
        self.__atlext_OCL_PropertyCallExp157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL_atlext_EObject158"):
                    opp_val = getattr(item, "OCL_atlext_EObject158", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL_atlext_EObject158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL_atlext_EObject158"):
                    opp_val = getattr(item, "OCL_atlext_EObject158", None)
                    
                    setattr(item, "OCL_atlext_EObject158", self)
                    

    @property
    def appliedProperty(self):
        return self.__appliedProperty

    @appliedProperty.setter
    def appliedProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__appliedProperty", None)
        self.__appliedProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression154"):
                opp_val = getattr(old_value, "OclExpression154", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression154"):
                opp_val = getattr(value, "OclExpression154", None)
                setattr(value, "OclExpression154", self)

    @property
    def atlext_OCL_PropertyCallExp(self):
        return self.__atlext_OCL_PropertyCallExp

    @atlext_OCL_PropertyCallExp.setter
    def atlext_OCL_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp", None)
        self.__atlext_OCL_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_EObject"):
                opp_val = getattr(old_value, "OCL_atlext_EObject", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject"):
                opp_val = getattr(value, "OCL_atlext_EObject", None)
                setattr(value, "OCL_atlext_EObject", self)

    @property
    def atlext_OCL_PropertyCallExp163(self):
        return self.__atlext_OCL_PropertyCallExp163

    @atlext_OCL_PropertyCallExp163.setter
    def atlext_OCL_PropertyCallExp163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp163", None)
        self.__atlext_OCL_PropertyCallExp163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Callable"):
                opp_val = getattr(old_value, "Callable", None)
                if opp_val == self:
                    setattr(old_value, "Callable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Callable"):
                opp_val = getattr(value, "Callable", None)
                setattr(value, "Callable", self)

class atlext_OCL_TupleExp(OclExpression):

    pass
class atlext_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression42: "atlext_ATL_InPattern" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression152: "atlext_OCL_MapElement" = None, OclExpression96: "atlext_ATL_IfStat" = None, OclExpression248: "atlext_OCL_Operation" = None, OclExpression71: "atlext_ATL_Binding" = None, OclExpression67: "atlext_ATL_ForEachOutPatternElement" = None, OclExpression89: "atlext_ATL_ExpressionStat" = None, OclExpression201: "atlext_OCL_OclType" = None, OclExpression169: "atlext_OCL_LoopExp" = None, OclExpression94: "atlext_ATL_BindingStat" = None, OclExpression178: "atlext_OCL_LetExp" = None, OclExpression184: "atlext_OCL_IfExp" = None, OclExpression188: "atlext_OCL_VariableDeclaration" = None, OclExpression180: "atlext_OCL_IfExp" = None, OclExpression149: "atlext_OCL_MapElement" = None, OclExpression107: "atlext_ATL_ForStat" = None, OclExpression166: "atlext_OCL_OperationCallExp" = None, OclExpression154: "atlext_OCL_PropertyCallExp" = None, OclExpression91: "atlext_ATL_BindingStat" = None, OclExpression65: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression182: "atlext_OCL_IfExp" = None, OclExpression240: "atlext_OCL_Attribute" = None, OclExpression142: "atlext_OCL_CollectionExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlext_OCL_CollectionExp(OclExpression):

    pass
class atlext_OCL_MapExp(OclExpression):

    pass
class atlext_OCL_OclType(OclExpression):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType: "MapType" = None, type206: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type212: "TupleTypeAttribute" = None, type214: "VariableDeclaration" = None, OclExpression42: "atlext_ATL_InPattern" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression152: "atlext_OCL_MapElement" = None, OclExpression96: "atlext_ATL_IfStat" = None, OclExpression248: "atlext_OCL_Operation" = None, OclExpression71: "atlext_ATL_Binding" = None, OclExpression67: "atlext_ATL_ForEachOutPatternElement" = None, OclExpression89: "atlext_ATL_ExpressionStat" = None, OclExpression201: "atlext_OCL_OclType" = None, OclExpression169: "atlext_OCL_LoopExp" = None, OclExpression94: "atlext_ATL_BindingStat" = None, OclExpression178: "atlext_OCL_LetExp" = None, OclExpression184: "atlext_OCL_IfExp" = None, OclExpression188: "atlext_OCL_VariableDeclaration" = None, OclExpression180: "atlext_OCL_IfExp" = None, OclExpression149: "atlext_OCL_MapElement" = None, OclExpression107: "atlext_ATL_ForStat" = None, OclExpression166: "atlext_OCL_OperationCallExp" = None, OclExpression154: "atlext_OCL_PropertyCallExp" = None, OclExpression91: "atlext_ATL_BindingStat" = None, OclExpression65: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression182: "atlext_OCL_IfExp" = None, OclExpression240: "atlext_OCL_Attribute" = None, OclExpression142: "atlext_OCL_CollectionExp" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type206 = type206
        self.keyType = keyType
        self.elementType = elementType
        self.type212 = type212
        self.type214 = type214
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression201"):
                opp_val = getattr(old_value, "OclExpression201", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression201"):
                opp_val = getattr(value, "OclExpression201", None)
                setattr(value, "OclExpression201", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__elementType", None)
        self.__elementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CollectionType"):
                opp_val = getattr(old_value, "CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CollectionType"):
                opp_val = getattr(value, "CollectionType", None)
                setattr(value, "CollectionType", self)

    @property
    def type214(self):
        return self.__type214

    @type214.setter
    def type214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type214", None)
        self.__type214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration215"):
                opp_val = getattr(old_value, "VariableDeclaration215", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration215"):
                opp_val = getattr(value, "VariableDeclaration215", None)
                setattr(value, "VariableDeclaration215", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__valueType", None)
        self.__valueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType"):
                opp_val = getattr(old_value, "MapType", None)
                if opp_val == self:
                    setattr(old_value, "MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType"):
                opp_val = getattr(value, "MapType", None)
                setattr(value, "MapType", self)

    @property
    def type206(self):
        return self.__type206

    @type206.setter
    def type206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type206", None)
        self.__type206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute207"):
                opp_val = getattr(old_value, "Attribute207", None)
                if opp_val == self:
                    setattr(old_value, "Attribute207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute207"):
                opp_val = getattr(value, "Attribute207", None)
                setattr(value, "Attribute207", self)

    @property
    def type212(self):
        return self.__type212

    @type212.setter
    def type212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type212", None)
        self.__type212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleTypeAttribute"):
                opp_val = getattr(old_value, "TupleTypeAttribute", None)
                if opp_val == self:
                    setattr(old_value, "TupleTypeAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleTypeAttribute"):
                opp_val = getattr(value, "TupleTypeAttribute", None)
                setattr(value, "TupleTypeAttribute", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation203"):
                opp_val = getattr(old_value, "Operation203", None)
                if opp_val == self:
                    setattr(old_value, "Operation203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation203"):
                opp_val = getattr(value, "Operation203", None)
                setattr(value, "Operation203", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__context_", None)
        self.__context_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition"):
                opp_val = getattr(old_value, "OclContextDefinition", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition"):
                opp_val = getattr(value, "OclContextDefinition", None)
                setattr(value, "OclContextDefinition", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType209"):
                opp_val = getattr(old_value, "MapType209", None)
                if opp_val == self:
                    setattr(old_value, "MapType209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType209"):
                opp_val = getattr(value, "MapType209", None)
                setattr(value, "MapType209", self)

class atlext_OCL_IfExp(OclExpression):

    pass
class atlext_OCL_OclUndefinedExp(OclExpression):

    pass
class atlext_OCL_PrimitiveExp(OclExpression):

    pass
class atlext_OCL_VariableExp(OclExpression):

    pass
class atlext_OCL_SuperExp(OclExpression):

    pass
class Helper:

    pass
class atlext_ATL_ContextHelper(Helper):

    pass
class Unit:

    pass
class atlext_ATL_Query(Unit):

    pass
class atlext_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlext_ATL_Module: set["OclModel"] = None, atlext_ATL_Module10: set["OclModel"] = None, atlext_ATL_Module13: set["ModuleElement"] = None, Unit: "atlext_ATL_LibraryRef" = None):
        self.isRefining = isRefining
        self.atlext_ATL_Module = atlext_ATL_Module if atlext_ATL_Module is not None else set()
        self.atlext_ATL_Module10 = atlext_ATL_Module10 if atlext_ATL_Module10 is not None else set()
        self.atlext_ATL_Module13 = atlext_ATL_Module13 if atlext_ATL_Module13 is not None else set()
        
        pass
    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def atlext_ATL_Module13(self):
        return self.__atlext_ATL_Module13

    @atlext_ATL_Module13.setter
    def atlext_ATL_Module13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module13", None)
        self.__atlext_ATL_Module13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    setattr(item, "ModuleElement", self)
                    

    @property
    def atlext_ATL_Module(self):
        return self.__atlext_ATL_Module

    @atlext_ATL_Module.setter
    def atlext_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module", None)
        self.__atlext_ATL_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    setattr(item, "OclModel", self)
                    

    @property
    def atlext_ATL_Module10(self):
        return self.__atlext_ATL_Module10

    @atlext_ATL_Module10.setter
    def atlext_ATL_Module10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module10", None)
        self.__atlext_ATL_Module10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel11"):
                    opp_val = getattr(item, "OclModel11", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel11"):
                    opp_val = getattr(item, "OclModel11", None)
                    
                    setattr(item, "OclModel11", self)
                    

class atlext_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlext_ATL_InPattern(LocatedElement):

    pass
class atlext_ATL_DropPattern(LocatedElement):

    pass
class atlext_ATL_ActionBlock(LocatedElement):

    pass
class atlext_ATL_OutPattern(LocatedElement):

    pass
class atlext_OCL_MapElement(LocatedElement):

    pass
class atlext_OCL_OclContextDefinition(LocatedElement):

    pass
class atlext_ATL_Binding(LocatedElement):

    def __init__(self, isAssignment: str, propertyName: str, atlext_ATL_Binding75: "ATL_atlext_EObject" = None, atlext_ATL_Binding78: "ATL_atlext_Type" = None, atlext_ATL_Binding: "OclExpression" = None, bindings: "OutPatternElement" = None, atlext_ATL_Binding81: set["RuleResolutionInfo"] = None):
        self.isAssignment = isAssignment
        self.propertyName = propertyName
        self.atlext_ATL_Binding75 = atlext_ATL_Binding75
        self.atlext_ATL_Binding78 = atlext_ATL_Binding78
        self.atlext_ATL_Binding = atlext_ATL_Binding
        self.bindings = bindings
        self.atlext_ATL_Binding81 = atlext_ATL_Binding81 if atlext_ATL_Binding81 is not None else set()
        
        pass
    @property
    def propertyName(self):
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName


    @property
    def isAssignment(self):
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment


    @property
    def atlext_ATL_Binding81(self):
        return self.__atlext_ATL_Binding81

    @atlext_ATL_Binding81.setter
    def atlext_ATL_Binding81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding81", None)
        self.__atlext_ATL_Binding81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleResolutionInfo"):
                    opp_val = getattr(item, "RuleResolutionInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleResolutionInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleResolutionInfo"):
                    opp_val = getattr(item, "RuleResolutionInfo", None)
                    
                    setattr(item, "RuleResolutionInfo", self)
                    

    @property
    def atlext_ATL_Binding(self):
        return self.__atlext_ATL_Binding

    @atlext_ATL_Binding.setter
    def atlext_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding", None)
        self.__atlext_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression71"):
                opp_val = getattr(old_value, "OclExpression71", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression71"):
                opp_val = getattr(value, "OclExpression71", None)
                setattr(value, "OclExpression71", self)

    @property
    def bindings(self):
        return self.__bindings

    @bindings.setter
    def bindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPatternElement73"):
                opp_val = getattr(old_value, "OutPatternElement73", None)
                if opp_val == self:
                    setattr(old_value, "OutPatternElement73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPatternElement73"):
                opp_val = getattr(value, "OutPatternElement73", None)
                setattr(value, "OutPatternElement73", self)

    @property
    def atlext_ATL_Binding75(self):
        return self.__atlext_ATL_Binding75

    @atlext_ATL_Binding75.setter
    def atlext_ATL_Binding75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding75", None)
        self.__atlext_ATL_Binding75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_EObject76"):
                opp_val = getattr(old_value, "ATL_atlext_EObject76", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_EObject76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_EObject76"):
                opp_val = getattr(value, "ATL_atlext_EObject76", None)
                setattr(value, "ATL_atlext_EObject76", self)

    @property
    def atlext_ATL_Binding78(self):
        return self.__atlext_ATL_Binding78

    @atlext_ATL_Binding78.setter
    def atlext_ATL_Binding78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding78", None)
        self.__atlext_ATL_Binding78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type79"):
                opp_val = getattr(old_value, "ATL_atlext_Type79", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type79"):
                opp_val = getattr(value, "ATL_atlext_Type79", None)
                setattr(value, "ATL_atlext_Type79", self)

class atlext_OCL_OclFeature(LocatedElement):

    pass
class atlext_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlext_ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, libraries: "Unit" = None):
        self.name = name
        self.libraries = libraries
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def libraries(self):
        return self.__libraries

    @libraries.setter
    def libraries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LibraryRef__libraries", None)
        self.__libraries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit"):
                opp_val = getattr(old_value, "Unit", None)
                if opp_val == self:
                    setattr(old_value, "Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit"):
                opp_val = getattr(value, "Unit", None)
                setattr(value, "Unit", self)

class atlext_ATL_ModuleElement(LocatedElement):

    pass
class atlext_ATL_Statement(LocatedElement):

    pass
class atlext_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model: "OclModel" = None, model252: set["OclModelElement"] = None, metamodel: set["OclModel"] = None):
        self.name = name
        self.model = model
        self.model252 = model252 if model252 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model252(self):
        return self.__model252

    @model252.setter
    def model252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__model252", None)
        self.__model252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    setattr(item, "OclModelElement", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel250"):
                opp_val = getattr(old_value, "OclModel250", None)
                if opp_val == self:
                    setattr(old_value, "OclModel250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel250"):
                opp_val = getattr(value, "OclModel250", None)
                setattr(value, "OclModel250", self)

    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel254"):
                    opp_val = getattr(item, "OclModel254", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel254"):
                    opp_val = getattr(item, "OclModel254", None)
                    
                    setattr(item, "OclModel254", self)
                    

class atlext_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, tupleTypeAttribute: "OclType" = None, attributes: "TupleType" = None):
        self.name = name
        self.tupleTypeAttribute = tupleTypeAttribute
        self.attributes = attributes
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleType"):
                opp_val = getattr(old_value, "TupleType", None)
                if opp_val == self:
                    setattr(old_value, "TupleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleType"):
                opp_val = getattr(value, "TupleType", None)
                setattr(value, "TupleType", self)

    @property
    def tupleTypeAttribute(self):
        return self.__tupleTypeAttribute

    @tupleTypeAttribute.setter
    def tupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType219"):
                opp_val = getattr(old_value, "OclType219", None)
                if opp_val == self:
                    setattr(old_value, "OclType219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType219"):
                opp_val = getattr(value, "OclType219", None)
                setattr(value, "OclType219", self)

class atlext_ATL_Unit(LocatedElement):

    def __init__(self, name: str, unit: set["LibraryRef"] = None):
        self.name = name
        self.unit = unit if unit is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Unit__unit", None)
        self.__unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LibraryRef"):
                    opp_val = getattr(item, "LibraryRef", None)
                    
                    if opp_val == self:
                        setattr(item, "LibraryRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LibraryRef"):
                    opp_val = getattr(item, "LibraryRef", None)
                    
                    setattr(item, "LibraryRef", self)
                    

class StringToStringMap:

    pass
class ATL_atlext_EObject:

    pass
class atlext_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str, fileLocation: str, fileObject: str, atlext_ATL_LocatedElement: set["ATL_atlext_EObject"] = None, atlext_ATL_LocatedElement2: set["StringToStringMap"] = None):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.fileLocation = fileLocation
        self.fileObject = fileObject
        self.atlext_ATL_LocatedElement = atlext_ATL_LocatedElement if atlext_ATL_LocatedElement is not None else set()
        self.atlext_ATL_LocatedElement2 = atlext_ATL_LocatedElement2 if atlext_ATL_LocatedElement2 is not None else set()
        
        pass
    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def fileLocation(self):
        return self.__fileLocation

    @fileLocation.setter
    def fileLocation(self, fileLocation: str):
        self.__fileLocation = fileLocation


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def fileObject(self):
        return self.__fileObject

    @fileObject.setter
    def fileObject(self, fileObject: str):
        self.__fileObject = fileObject


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def atlext_ATL_LocatedElement2(self):
        return self.__atlext_ATL_LocatedElement2

    @atlext_ATL_LocatedElement2.setter
    def atlext_ATL_LocatedElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement2", None)
        self.__atlext_ATL_LocatedElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    setattr(item, "StringToStringMap", self)
                    

    @property
    def atlext_ATL_LocatedElement(self):
        return self.__atlext_ATL_LocatedElement

    @atlext_ATL_LocatedElement.setter
    def atlext_ATL_LocatedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement", None)
        self.__atlext_ATL_LocatedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL_atlext_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    setattr(item, "ATL_atlext_EObject", self)
                    
