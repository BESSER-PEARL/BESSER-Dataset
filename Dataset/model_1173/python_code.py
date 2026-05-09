from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
class atlext_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlext_OCL_Operation: set["Parameter"] = None, operation: "OclType" = None, owningOperation: "OclExpression" = None, OclFeature: "atlext_OCL_OclFeatureDefinition" = None):
        self.name = name
        self.atlext_OCL_Operation = atlext_OCL_Operation if atlext_OCL_Operation is not None else set()
        self.operation = operation
        self.owningOperation = owningOperation
        
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
            if hasattr(old_value, "OclType217"):
                opp_val = getattr(old_value, "OclType217", None)
                if opp_val == self:
                    setattr(old_value, "OclType217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType217"):
                opp_val = getattr(value, "OclType217", None)
                setattr(value, "OclType217", self)

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
                if hasattr(item, "Parameter215"):
                    opp_val = getattr(item, "Parameter215", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter215"):
                    opp_val = getattr(item, "Parameter215", None)
                    
                    setattr(item, "Parameter215", self)
                    

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
            if hasattr(old_value, "OclExpression219"):
                opp_val = getattr(old_value, "OclExpression219", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression219"):
                opp_val = getattr(value, "OclExpression219", None)
                setattr(value, "OclExpression219", self)

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
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType213"):
                opp_val = getattr(old_value, "OclType213", None)
                if opp_val == self:
                    setattr(old_value, "OclType213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType213"):
                opp_val = getattr(value, "OclType213", None)
                setattr(value, "OclType213", self)

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
            if hasattr(old_value, "OclExpression211"):
                opp_val = getattr(old_value, "OclExpression211", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression211"):
                opp_val = getattr(value, "OclExpression211", None)
                setattr(value, "OclExpression211", self)

class CollectionType:

    pass
class MapType:

    pass
class TupleType:

    pass
class atlext_OCL_SetType(CollectionType):

    pass
class atlext_OCL_SequenceType(CollectionType):

    pass
class atlext_OCL_OrderedSetType(CollectionType):

    pass
class atlext_OCL_BagType(CollectionType):

    pass
class NumericType:

    pass
class atlext_OCL_RealType(NumericType):

    pass
class atlext_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class atlext_OCL_BooleanType(Primitive):

    pass
class atlext_OCL_NumericType(Primitive):

    pass
class atlext_OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class OclContextDefinition:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class ResolveTempResolution:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class ContextHelper:

    pass
class MapExp:

    pass
class PrimitiveExp:

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


class atlext_OCL_NumericExp(PrimitiveExp):

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


class OperationCallExp:

    pass
class atlext_OCL_OperatorCallExp(OperationCallExp):

    pass
class atlext_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class atlext_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp167: "atlext_OCL_Iterator" = None, LoopExp: "atlext_OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlext_OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class atlext_OCL_BagExp(CollectionExp):

    pass
class atlext_OCL_OrderedSetExp(CollectionExp):

    pass
class atlext_OCL_SetExp(CollectionExp):

    pass
class atlext_OCL_SequenceExp(CollectionExp):

    pass
class Attribute:

    pass
class Operation:

    pass
class IfExp:

    pass
class OclType:

    pass
class atlext_OCL_Primitive(OclType):

    pass
class atlext_OCL_CollectionType(OclType):

    pass
class atlext_OCL_TupleType(OclType):

    pass
class atlext_OCL_OclAnyType(OclType):

    pass
class atlext_OCL_MapType(OclType):

    pass
class atlext_OCL_OclModelElement(OclType):

    pass
class OCL_TypedElement:

    pass
class ATL_LocatedElement:

    pass
class atlext_OCL_VariableDeclaration(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, id: str, varName: str, variable: "LetExp" = None, result: "IterateExp" = None, referredVariable: set["VariableExp"] = None, variableDeclaration: "OclType" = None, initializedVariable: "OclExpression" = None):
        self.id = id
        self.varName = varName
        self.variable = variable
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.variableDeclaration = variableDeclaration
        self.initializedVariable = initializedVariable
        
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
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp163"):
                opp_val = getattr(old_value, "LetExp163", None)
                if opp_val == self:
                    setattr(old_value, "LetExp163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp163"):
                opp_val = getattr(value, "LetExp163", None)
                setattr(value, "LetExp163", self)

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
            if hasattr(old_value, "OclType159"):
                opp_val = getattr(old_value, "OclType159", None)
                if opp_val == self:
                    setattr(old_value, "OclType159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType159"):
                opp_val = getattr(value, "OclType159", None)
                setattr(value, "OclType159", self)

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
            if hasattr(old_value, "OclExpression161"):
                opp_val = getattr(old_value, "OclExpression161", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression161"):
                opp_val = getattr(value, "OclExpression161", None)
                setattr(value, "OclExpression161", self)

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
                    

class atlext_OCL_OclExpression(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, implicitlyCasted: str, oclExpression: "OclType" = None, elseExpression: "IfExp" = None, body115: "Operation" = None, condition: "IfExp" = None, initExpression119: "Attribute" = None, source: "PropertyCallExp" = None, elements106: "CollectionExp" = None, in_: "LetExp" = None, body: "LoopExp" = None, arguments: "OperationCallExp" = None, initExpression: "VariableDeclaration" = None, thenExpression: "IfExp" = None):
        self.implicitlyCasted = implicitlyCasted
        self.oclExpression = oclExpression
        self.elseExpression = elseExpression
        self.body115 = body115
        self.condition = condition
        self.initExpression119 = initExpression119
        self.source = source
        self.elements106 = elements106
        self.in_ = in_
        self.body = body
        self.arguments = arguments
        self.initExpression = initExpression
        self.thenExpression = thenExpression
        
        pass
    @property
    def implicitlyCasted(self):
        return self.__implicitlyCasted

    @implicitlyCasted.setter
    def implicitlyCasted(self, implicitlyCasted: str):
        self.__implicitlyCasted = implicitlyCasted


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
    def body115(self):
        return self.__body115

    @body115.setter
    def body115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__body115", None)
        self.__body115 = value
        
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
    def thenExpression(self):
        return self.__thenExpression

    @thenExpression.setter
    def thenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__thenExpression", None)
        self.__thenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IfExp113"):
                opp_val = getattr(old_value, "IfExp113", None)
                if opp_val == self:
                    setattr(old_value, "IfExp113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IfExp113"):
                opp_val = getattr(value, "IfExp113", None)
                setattr(value, "IfExp113", self)

    @property
    def initExpression119(self):
        return self.__initExpression119

    @initExpression119.setter
    def initExpression119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__initExpression119", None)
        self.__initExpression119 = value
        
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
    def initExpression(self):
        return self.__initExpression

    @initExpression.setter
    def initExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__initExpression", None)
        self.__initExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration111"):
                opp_val = getattr(old_value, "VariableDeclaration111", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration111"):
                opp_val = getattr(value, "VariableDeclaration111", None)
                setattr(value, "VariableDeclaration111", self)

    @property
    def elements106(self):
        return self.__elements106

    @elements106.setter
    def elements106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__elements106", None)
        self.__elements106 = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PropertyCallExp104"):
                opp_val = getattr(old_value, "PropertyCallExp104", None)
                if opp_val == self:
                    setattr(old_value, "PropertyCallExp104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PropertyCallExp104"):
                opp_val = getattr(value, "PropertyCallExp104", None)
                setattr(value, "PropertyCallExp104", self)

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
            if hasattr(old_value, "IfExp117"):
                opp_val = getattr(old_value, "IfExp117", None)
                if opp_val == self:
                    setattr(old_value, "IfExp117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IfExp117"):
                opp_val = getattr(value, "IfExp117", None)
                setattr(value, "IfExp117", self)

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

class MatchedRule:

    pass
class atlext_ATL_RuleResolutionInfo:

    pass
class atlext_ATL_CallableParameter:

    def __init__(self, name: str, atlext_ATL_CallableParameter: "VariableDeclaration" = None):
        self.name = name
        self.atlext_ATL_CallableParameter = atlext_ATL_CallableParameter
        
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


class Iterator:

    pass
class Binding:

    pass
class Statement:

    pass
class atlext_ATL_IfStat(Statement):

    pass
class atlext_ATL_ForStat(Statement):

    pass
class atlext_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_BindingStat: "OclExpression" = None, atlext_ATL_BindingStat78: "OclExpression" = None, Statement84: "atlext_ATL_IfStat" = None, Statement: "atlext_ATL_ActionBlock" = None, Statement95: "atlext_ATL_ForStat" = None, Statement87: "atlext_ATL_IfStat" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_BindingStat = atlext_ATL_BindingStat
        self.atlext_ATL_BindingStat78 = atlext_ATL_BindingStat78
        
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
    def atlext_ATL_BindingStat78(self):
        return self.__atlext_ATL_BindingStat78

    @atlext_ATL_BindingStat78.setter
    def atlext_ATL_BindingStat78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_BindingStat__atlext_ATL_BindingStat78", None)
        self.__atlext_ATL_BindingStat78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression79"):
                opp_val = getattr(old_value, "OclExpression79", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression79"):
                opp_val = getattr(value, "OclExpression79", None)
                setattr(value, "OclExpression79", self)

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
            if hasattr(old_value, "OclExpression76"):
                opp_val = getattr(old_value, "OclExpression76", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression76"):
                opp_val = getattr(value, "OclExpression76", None)
                setattr(value, "OclExpression76", self)

class atlext_ATL_ExpressionStat(Statement):

    pass
class RuleResolutionInfo:

    pass
class atlext_OCL_ResolveTempResolution(RuleResolutionInfo):

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
                    

class PatternElement:

    pass
class atlext_ATL_OutPatternElement(PatternElement):

    pass
class atlext_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlext_OCL_TuplePart(VariableDeclaration):

    pass
class atlext_OCL_Parameter(VariableDeclaration):

    pass
class atlext_OCL_Iterator(VariableDeclaration):

    pass
class atlext_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlext_ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class atlext_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class atlext_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class atlext_ATL_SimpleInPatternElement(InPatternElement):

    pass
class ATL_ModuleCallable:

    pass
class ATL_Helper:

    pass
class atlext_ATL_StaticHelper(ATL_Helper, ATL_ModuleCallable):

    pass
class ATL_StaticRule:

    pass
class ATL_RuleWithPattern:

    pass
class atlext_ATL_LazyRule(ATL_RuleWithPattern, ATL_StaticRule):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class RuleWithPattern:

    pass
class atlext_ATL_MatchedRule(RuleWithPattern):

    pass
class InPattern:

    pass
class Rule:

    pass
class atlext_ATL_RuleWithPattern(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, atlext_ATL_RuleWithPattern: "InPattern" = None, superRule: set["RuleWithPattern"] = None, children: "RuleWithPattern" = None, Rule68: "atlext_ATL_RuleVariableDeclaration" = None, Rule71: "atlext_ATL_ActionBlock" = None, Rule: "atlext_ATL_OutPattern" = None):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.atlext_ATL_RuleWithPattern = atlext_ATL_RuleWithPattern
        self.superRule = superRule if superRule is not None else set()
        self.children = children
        
        pass
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
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


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
            if hasattr(old_value, "RuleWithPattern29"):
                opp_val = getattr(old_value, "RuleWithPattern29", None)
                if opp_val == self:
                    setattr(old_value, "RuleWithPattern29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RuleWithPattern29"):
                opp_val = getattr(value, "RuleWithPattern29", None)
                setattr(value, "RuleWithPattern29", self)

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
class atlext_ATL_Callable(ABC):

    pass
class Callable:

    pass
class atlext_ATL_ModuleCallable(Callable):

    pass
class ATL_Rule:

    pass
class atlext_ATL_StaticRule(ATL_Rule, ATL_ModuleCallable):

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class PropertyCallExp:

    pass
class atlext_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, atlext_OCL_OperationCallExp: set["ResolveTempResolution"] = None, PropertyCallExp23: "atlext_ATL_Callable" = None, PropertyCallExp: "atlext_ATL_ContextHelper" = None, PropertyCallExp104: "atlext_OCL_OclExpression" = None):
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
                if hasattr(item, "OclExpression139"):
                    opp_val = getattr(item, "OclExpression139", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression139"):
                    opp_val = getattr(item, "OclExpression139", None)
                    
                    setattr(item, "OclExpression139", self)
                    

class atlext_OCL_LoopExp(PropertyCallExp):

    pass
class atlext_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, PropertyCallExp23: "atlext_ATL_Callable" = None, PropertyCallExp: "atlext_ATL_ContextHelper" = None, PropertyCallExp104: "atlext_OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlext_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str, fileLocation: str, fileObject: str, atlext_ATL_LocatedElement: set["StringToStringMap"] = None):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.fileLocation = fileLocation
        self.fileObject = fileObject
        self.atlext_ATL_LocatedElement = atlext_ATL_LocatedElement if atlext_ATL_LocatedElement is not None else set()
        
        pass
    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


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

    def __init__(self, hasContext: bool, isAttribute: str, atlext_ATL_Helper: "OclFeatureDefinition" = None, helpers: "Query" = None, helpers14: "Library" = None):
        self.hasContext = hasContext
        self.isAttribute = isAttribute
        self.atlext_ATL_Helper = atlext_ATL_Helper
        self.helpers = helpers
        self.helpers14 = helpers14
        
        pass
    @property
    def isAttribute(self):
        return self.__isAttribute

    @isAttribute.setter
    def isAttribute(self, isAttribute: str):
        self.__isAttribute = isAttribute


    @property
    def hasContext(self):
        return self.__hasContext

    @hasContext.setter
    def hasContext(self, hasContext: bool):
        self.__hasContext = hasContext


    @property
    def helpers14(self):
        return self.__helpers14

    @helpers14.setter
    def helpers14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__helpers14", None)
        self.__helpers14 = value
        
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

class ModuleElement:

    pass
class atlext_ATL_Rule(ModuleElement):

    def __init__(self, name: str, rule: "OutPattern" = None, rule19: "ActionBlock" = None, rule21: set["RuleVariableDeclaration"] = None, ModuleElement: "atlext_ATL_Module" = None):
        self.name = name
        self.rule = rule
        self.rule19 = rule19
        self.rule21 = rule21 if rule21 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rule21(self):
        return self.__rule21

    @rule21.setter
    def rule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__rule21", None)
        self.__rule21 = value if value is not None else set()
        
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
    def rule19(self):
        return self.__rule19

    @rule19.setter
    def rule19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__rule19", None)
        self.__rule19 = value
        
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

class OclModel:

    pass
class OclExpression:

    pass
class atlext_OCL_LetExp(OclExpression):

    pass
class atlext_OCL_OclType(OclExpression):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, elementType: "CollectionType" = None, type183: "TupleTypeAttribute" = None, type185: "VariableDeclaration" = None, valueType: "MapType" = None, keyType: "MapType" = None, type177: "Attribute" = None, OclExpression139: "atlext_OCL_OperationCallExp" = None, OclExpression76: "atlext_ATL_BindingStat" = None, OclExpression133: "atlext_OCL_MapElement" = None, OclExpression135: "atlext_OCL_PropertyCallExp" = None, OclExpression56: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression123: "atlext_OCL_CollectionExp" = None, OclExpression155: "atlext_OCL_IfExp" = None, OclExpression157: "atlext_OCL_IfExp" = None, OclExpression92: "atlext_ATL_ForStat" = None, OclExpression211: "atlext_OCL_Attribute" = None, OclExpression153: "atlext_OCL_IfExp" = None, OclExpression130: "atlext_OCL_MapElement" = None, OclExpression33: "atlext_ATL_InPattern" = None, OclExpression79: "atlext_ATL_BindingStat" = None, OclExpression172: "atlext_OCL_OclType" = None, OclExpression81: "atlext_ATL_IfStat" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression219: "atlext_OCL_Operation" = None, OclExpression74: "atlext_ATL_ExpressionStat" = None, OclExpression161: "atlext_OCL_VariableDeclaration" = None, OclExpression142: "atlext_OCL_LoopExp" = None, OclExpression62: "atlext_ATL_Binding" = None, OclExpression151: "atlext_OCL_LetExp" = None, OclExpression58: "atlext_ATL_ForEachOutPatternElement" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.elementType = elementType
        self.type183 = type183
        self.type185 = type185
        self.valueType = valueType
        self.keyType = keyType
        self.type177 = type177
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type185(self):
        return self.__type185

    @type185.setter
    def type185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type185", None)
        self.__type185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration186"):
                opp_val = getattr(old_value, "VariableDeclaration186", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration186"):
                opp_val = getattr(value, "VariableDeclaration186", None)
                setattr(value, "VariableDeclaration186", self)

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
            if hasattr(old_value, "OclExpression172"):
                opp_val = getattr(old_value, "OclExpression172", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression172"):
                opp_val = getattr(value, "OclExpression172", None)
                setattr(value, "OclExpression172", self)

    @property
    def type177(self):
        return self.__type177

    @type177.setter
    def type177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type177", None)
        self.__type177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute178"):
                opp_val = getattr(old_value, "Attribute178", None)
                if opp_val == self:
                    setattr(old_value, "Attribute178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute178"):
                opp_val = getattr(value, "Attribute178", None)
                setattr(value, "Attribute178", self)

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
    def type183(self):
        return self.__type183

    @type183.setter
    def type183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__type183", None)
        self.__type183 = value
        
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
            if hasattr(old_value, "MapType180"):
                opp_val = getattr(old_value, "MapType180", None)
                if opp_val == self:
                    setattr(old_value, "MapType180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType180"):
                opp_val = getattr(value, "MapType180", None)
                setattr(value, "MapType180", self)

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
            if hasattr(old_value, "Operation174"):
                opp_val = getattr(old_value, "Operation174", None)
                if opp_val == self:
                    setattr(old_value, "Operation174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation174"):
                opp_val = getattr(value, "Operation174", None)
                setattr(value, "Operation174", self)

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

class atlext_OCL_SuperExp(OclExpression):

    pass
class atlext_OCL_VariableExp(OclExpression):

    pass
class atlext_OCL_PropertyCallExp(OclExpression):

    def __init__(self, isStaticCall: bool, appliedProperty: "OclExpression" = None, atlext_OCL_PropertyCallExp: "Callable" = None, polymorphicCalledBy: set["ContextHelper"] = None, OclExpression139: "atlext_OCL_OperationCallExp" = None, OclExpression76: "atlext_ATL_BindingStat" = None, OclExpression133: "atlext_OCL_MapElement" = None, OclExpression135: "atlext_OCL_PropertyCallExp" = None, OclExpression56: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression123: "atlext_OCL_CollectionExp" = None, OclExpression155: "atlext_OCL_IfExp" = None, OclExpression157: "atlext_OCL_IfExp" = None, OclExpression92: "atlext_ATL_ForStat" = None, OclExpression211: "atlext_OCL_Attribute" = None, OclExpression153: "atlext_OCL_IfExp" = None, OclExpression130: "atlext_OCL_MapElement" = None, OclExpression33: "atlext_ATL_InPattern" = None, OclExpression79: "atlext_ATL_BindingStat" = None, OclExpression172: "atlext_OCL_OclType" = None, OclExpression81: "atlext_ATL_IfStat" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression219: "atlext_OCL_Operation" = None, OclExpression74: "atlext_ATL_ExpressionStat" = None, OclExpression161: "atlext_OCL_VariableDeclaration" = None, OclExpression142: "atlext_OCL_LoopExp" = None, OclExpression62: "atlext_ATL_Binding" = None, OclExpression151: "atlext_OCL_LetExp" = None, OclExpression58: "atlext_ATL_ForEachOutPatternElement" = None):
        self.isStaticCall = isStaticCall
        self.appliedProperty = appliedProperty
        self.atlext_OCL_PropertyCallExp = atlext_OCL_PropertyCallExp
        self.polymorphicCalledBy = polymorphicCalledBy if polymorphicCalledBy is not None else set()
        
        pass
    @property
    def isStaticCall(self):
        return self.__isStaticCall

    @isStaticCall.setter
    def isStaticCall(self, isStaticCall: bool):
        self.__isStaticCall = isStaticCall


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
            if hasattr(old_value, "OclExpression135"):
                opp_val = getattr(old_value, "OclExpression135", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression135"):
                opp_val = getattr(value, "OclExpression135", None)
                setattr(value, "OclExpression135", self)

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
    def atlext_OCL_PropertyCallExp(self):
        return self.__atlext_OCL_PropertyCallExp

    @atlext_OCL_PropertyCallExp.setter
    def atlext_OCL_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp", None)
        self.__atlext_OCL_PropertyCallExp = value
        
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

class atlext_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression139: "atlext_OCL_OperationCallExp" = None, OclExpression76: "atlext_ATL_BindingStat" = None, OclExpression133: "atlext_OCL_MapElement" = None, OclExpression135: "atlext_OCL_PropertyCallExp" = None, OclExpression56: "atlext_ATL_SimpleOutPatternElement" = None, OclExpression123: "atlext_OCL_CollectionExp" = None, OclExpression155: "atlext_OCL_IfExp" = None, OclExpression157: "atlext_OCL_IfExp" = None, OclExpression92: "atlext_ATL_ForStat" = None, OclExpression211: "atlext_OCL_Attribute" = None, OclExpression153: "atlext_OCL_IfExp" = None, OclExpression130: "atlext_OCL_MapElement" = None, OclExpression33: "atlext_ATL_InPattern" = None, OclExpression79: "atlext_ATL_BindingStat" = None, OclExpression172: "atlext_OCL_OclType" = None, OclExpression81: "atlext_ATL_IfStat" = None, OclExpression: "atlext_ATL_Query" = None, OclExpression219: "atlext_OCL_Operation" = None, OclExpression74: "atlext_ATL_ExpressionStat" = None, OclExpression161: "atlext_OCL_VariableDeclaration" = None, OclExpression142: "atlext_OCL_LoopExp" = None, OclExpression62: "atlext_ATL_Binding" = None, OclExpression151: "atlext_OCL_LetExp" = None, OclExpression58: "atlext_ATL_ForEachOutPatternElement" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlext_OCL_JavaBody(OclExpression):

    pass
class atlext_OCL_IfExp(OclExpression):

    pass
class atlext_OCL_OclUndefinedExp(OclExpression):

    pass
class atlext_OCL_PrimitiveExp(OclExpression):

    pass
class atlext_OCL_TupleExp(OclExpression):

    pass
class atlext_OCL_MapExp(OclExpression):

    pass
class atlext_OCL_CollectionExp(OclExpression):

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

    def __init__(self, isRefining: str, atlext_ATL_Module: set["OclModel"] = None, atlext_ATL_Module8: set["OclModel"] = None, atlext_ATL_Module11: set["ModuleElement"] = None, Unit: "atlext_ATL_LibraryRef" = None):
        self.isRefining = isRefining
        self.atlext_ATL_Module = atlext_ATL_Module if atlext_ATL_Module is not None else set()
        self.atlext_ATL_Module8 = atlext_ATL_Module8 if atlext_ATL_Module8 is not None else set()
        self.atlext_ATL_Module11 = atlext_ATL_Module11 if atlext_ATL_Module11 is not None else set()
        
        pass
    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def atlext_ATL_Module8(self):
        return self.__atlext_ATL_Module8

    @atlext_ATL_Module8.setter
    def atlext_ATL_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module8", None)
        self.__atlext_ATL_Module8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel9"):
                    opp_val = getattr(item, "OclModel9", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel9"):
                    opp_val = getattr(item, "OclModel9", None)
                    
                    setattr(item, "OclModel9", self)
                    

    @property
    def atlext_ATL_Module11(self):
        return self.__atlext_ATL_Module11

    @atlext_ATL_Module11.setter
    def atlext_ATL_Module11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module11", None)
        self.__atlext_ATL_Module11 = value if value is not None else set()
        
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
                    

class atlext_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlext_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model223: set["OclModelElement"] = None, metamodel: set["OclModel"] = None, model: "OclModel" = None):
        self.name = name
        self.model223 = model223 if model223 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        self.model = model
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "OclModel221"):
                opp_val = getattr(old_value, "OclModel221", None)
                if opp_val == self:
                    setattr(old_value, "OclModel221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel221"):
                opp_val = getattr(value, "OclModel221", None)
                setattr(value, "OclModel221", self)

    @property
    def model223(self):
        return self.__model223

    @model223.setter
    def model223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__model223", None)
        self.__model223 = value if value is not None else set()
        
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
                if hasattr(item, "OclModel225"):
                    opp_val = getattr(item, "OclModel225", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel225"):
                    opp_val = getattr(item, "OclModel225", None)
                    
                    setattr(item, "OclModel225", self)
                    

class atlext_ATL_DropPattern(LocatedElement):

    pass
class atlext_ATL_ModuleElement(LocatedElement):

    pass
class atlext_ATL_InPattern(LocatedElement):

    pass
class atlext_OCL_OclContextDefinition(LocatedElement):

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
    def tupleTypeAttribute(self):
        return self.__tupleTypeAttribute

    @tupleTypeAttribute.setter
    def tupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType190"):
                opp_val = getattr(old_value, "OclType190", None)
                if opp_val == self:
                    setattr(old_value, "OclType190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType190"):
                opp_val = getattr(value, "OclType190", None)
                setattr(value, "OclType190", self)

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

class atlext_ATL_Statement(LocatedElement):

    pass
class atlext_ATL_OutPattern(LocatedElement):

    pass
class atlext_ATL_ActionBlock(LocatedElement):

    pass
class atlext_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_Binding: "OclExpression" = None, bindings: "OutPatternElement" = None, atlext_ATL_Binding66: set["RuleResolutionInfo"] = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_Binding = atlext_ATL_Binding
        self.bindings = bindings
        self.atlext_ATL_Binding66 = atlext_ATL_Binding66 if atlext_ATL_Binding66 is not None else set()
        
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
    def bindings(self):
        return self.__bindings

    @bindings.setter
    def bindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPatternElement64"):
                opp_val = getattr(old_value, "OutPatternElement64", None)
                if opp_val == self:
                    setattr(old_value, "OutPatternElement64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPatternElement64"):
                opp_val = getattr(value, "OutPatternElement64", None)
                setattr(value, "OutPatternElement64", self)

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
            if hasattr(old_value, "OclExpression62"):
                opp_val = getattr(old_value, "OclExpression62", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression62"):
                opp_val = getattr(value, "OclExpression62", None)
                setattr(value, "OclExpression62", self)

    @property
    def atlext_ATL_Binding66(self):
        return self.__atlext_ATL_Binding66

    @atlext_ATL_Binding66.setter
    def atlext_ATL_Binding66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding66", None)
        self.__atlext_ATL_Binding66 = value if value is not None else set()
        
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
                    

class atlext_OCL_OclFeature(LocatedElement):

    pass
class atlext_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlext_OCL_MapElement(LocatedElement):

    pass
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