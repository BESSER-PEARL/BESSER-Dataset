from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
class Parameter:

    pass
class OCL_Operation(OclFeature):

    def __init__(self, name: str, operation: set["Parameter"] = None, operation107: "OclType" = None, owningOperation: "OclExpression" = None, OclFeature: "OCL_OclFeatureDefinition" = None):
        self.name = name
        self.operation = operation if operation is not None else set()
        self.operation107 = operation107
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
        old_value = getattr(self, f"_OCL_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
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
                    

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__owningOperation", None)
        self.__owningOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression110"):
                opp_val = getattr(old_value, "OclExpression110", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression110"):
                opp_val = getattr(value, "OclExpression110", None)
                setattr(value, "OclExpression110", self)

    @property
    def operation107(self):
        return self.__operation107

    @operation107.setter
    def operation107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__operation107", None)
        self.__operation107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType108"):
                opp_val = getattr(old_value, "OclType108", None)
                if opp_val == self:
                    setattr(old_value, "OclType108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType108"):
                opp_val = getattr(value, "OclType108", None)
                setattr(value, "OclType108", self)

class OCL_Attribute(OclFeature):

    def __init__(self, name: str, owningAttribute: "OclExpression" = None, attribute: "OclType" = None, OclFeature: "OCL_OclFeatureDefinition" = None):
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
        old_value = getattr(self, f"_OCL_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression102"):
                opp_val = getattr(old_value, "OclExpression102", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression102"):
                opp_val = getattr(value, "OclExpression102", None)
                setattr(value, "OclExpression102", self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType104"):
                opp_val = getattr(old_value, "OclType104", None)
                if opp_val == self:
                    setattr(old_value, "OclType104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType104"):
                opp_val = getattr(value, "OclType104", None)
                setattr(value, "OclType104", self)

class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class OclModel:

    pass
class TupleType:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class Iterator:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class OclExpression:

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, returnType: "Operation" = None, valueType: "MapType" = None, type70: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type76: "TupleTypeAttribute" = None, type78: "VariableDeclaration" = None, context_: "OclContextDefinition" = None, type: "OclExpression" = None, OclExpression28: "OCL_MapElement" = None, OclExpression: "OCL_CollectionExp" = None, OclExpression32: "OCL_OperationCallExp" = None, OclExpression42: "OCL_LetExp" = None, OclExpression25: "OCL_MapElement" = None, OclExpression102: "OCL_Attribute" = None, OclExpression30: "OCL_PropertyCallExp" = None, OclExpression110: "OCL_Operation" = None, OclExpression44: "OCL_IfExp" = None, OclExpression48: "OCL_IfExp" = None, OclExpression34: "OCL_LoopExp" = None, OclExpression52: "OCL_VariableDeclaration" = None, OclExpression46: "OCL_IfExp" = None, OclExpression65: "OCL_OclType" = None):
        self.name = name
        self.returnType = returnType
        self.valueType = valueType
        self.type70 = type70
        self.keyType = keyType
        self.elementType = elementType
        self.type76 = type76
        self.type78 = type78
        self.context_ = context_
        self.type = type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type78(self):
        return self.__type78

    @type78.setter
    def type78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type78", None)
        self.__type78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration79"):
                opp_val = getattr(old_value, "VariableDeclaration79", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration79"):
                opp_val = getattr(value, "VariableDeclaration79", None)
                setattr(value, "VariableDeclaration79", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression65"):
                opp_val = getattr(old_value, "OclExpression65", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression65"):
                opp_val = getattr(value, "OclExpression65", None)
                setattr(value, "OclExpression65", self)

    @property
    def type70(self):
        return self.__type70

    @type70.setter
    def type70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type70", None)
        self.__type70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute71"):
                opp_val = getattr(old_value, "Attribute71", None)
                if opp_val == self:
                    setattr(old_value, "Attribute71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute71"):
                opp_val = getattr(value, "Attribute71", None)
                setattr(value, "Attribute71", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation67"):
                opp_val = getattr(old_value, "Operation67", None)
                if opp_val == self:
                    setattr(old_value, "Operation67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation67"):
                opp_val = getattr(value, "Operation67", None)
                setattr(value, "Operation67", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__valueType", None)
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
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType73"):
                opp_val = getattr(old_value, "MapType73", None)
                if opp_val == self:
                    setattr(old_value, "MapType73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType73"):
                opp_val = getattr(value, "MapType73", None)
                setattr(value, "MapType73", self)

    @property
    def type76(self):
        return self.__type76

    @type76.setter
    def type76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type76", None)
        self.__type76 = value
        
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
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__elementType", None)
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
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__context_", None)
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

class OCL_OclUndefinedExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression28: "OCL_MapElement" = None, OclExpression: "OCL_CollectionExp" = None, OclExpression32: "OCL_OperationCallExp" = None, OclExpression42: "OCL_LetExp" = None, OclExpression25: "OCL_MapElement" = None, OclExpression102: "OCL_Attribute" = None, OclExpression30: "OCL_PropertyCallExp" = None, OclExpression110: "OCL_Operation" = None, OclExpression44: "OCL_IfExp" = None, OclExpression48: "OCL_IfExp" = None, OclExpression34: "OCL_LoopExp" = None, OclExpression52: "OCL_VariableDeclaration" = None, OclExpression46: "OCL_IfExp" = None, OclExpression65: "OCL_OclType" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_VariableExp(OclExpression):

    pass
class Attribute:

    pass
class Operation:

    pass
class VariableDeclaration:

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class OCL_TupleExp(OclExpression):

    pass
class OCL_CollectionExp(OclExpression):

    pass
class NumericExp:

    pass
class OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class PrimitiveExp:

    pass
class OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class OCL_NumericExp(PrimitiveExp):

    pass
class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class LoopExp:

    pass
class OCL_IterateExp(LoopExp):

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp58: "OCL_Iterator" = None, LoopExp: "OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class LetExp:

    pass
class CollectionExp:

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, PropertyCallExp: "OCL_OclExpression" = None):
        self.operationName = operationName
        self.parentOperation = parentOperation if parentOperation is not None else set()
        
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
        old_value = getattr(self, f"_OCL_OperationCallExp__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression32"):
                    opp_val = getattr(item, "OclExpression32", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression32"):
                    opp_val = getattr(item, "OclExpression32", None)
                    
                    setattr(item, "OclExpression32", self)
                    

class OCL_LoopExp(PropertyCallExp):

    pass
class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, PropertyCallExp: "OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class IfExp:

    pass
class OclType:

    pass
class OCL_OclModelElement(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_MapType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class LocatedElement:

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeature(LocatedElement):

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model: "OclModel" = None, model114: set["OclModelElement"] = None, metamodel: set["OclModel"] = None):
        self.name = name
        self.model = model
        self.model114 = model114 if model114 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel116"):
                    opp_val = getattr(item, "OclModel116", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel116"):
                    opp_val = getattr(item, "OclModel116", None)
                    
                    setattr(item, "OclModel116", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel112"):
                opp_val = getattr(old_value, "OclModel112", None)
                if opp_val == self:
                    setattr(old_value, "OclModel112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel112"):
                opp_val = getattr(value, "OclModel112", None)
                setattr(value, "OclModel112", self)

    @property
    def model114(self):
        return self.__model114

    @model114.setter
    def model114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model114", None)
        self.__model114 = value if value is not None else set()
        
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
                    

class OCL_TupleTypeAttribute(LocatedElement):

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
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType83"):
                opp_val = getattr(old_value, "OclType83", None)
                if opp_val == self:
                    setattr(old_value, "OclType83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType83"):
                opp_val = getattr(value, "OclType83", None)
                setattr(value, "OclType83", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__attributes", None)
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

class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_VariableDeclaration(LocatedElement):

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def varName(self):
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName


    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType50"):
                opp_val = getattr(old_value, "OclType50", None)
                if opp_val == self:
                    setattr(old_value, "OclType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType50"):
                opp_val = getattr(value, "OclType50", None)
                setattr(value, "OclType50", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp54"):
                opp_val = getattr(old_value, "LetExp54", None)
                if opp_val == self:
                    setattr(old_value, "LetExp54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp54"):
                opp_val = getattr(value, "LetExp54", None)
                setattr(value, "LetExp54", self)

    @property
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression52"):
                opp_val = getattr(old_value, "OclExpression52", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression52"):
                opp_val = getattr(value, "OclExpression52", None)
                setattr(value, "OclExpression52", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__result", None)
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
        old_value = getattr(self, f"_OCL_VariableDeclaration__referredVariable", None)
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
                    

class OCL_OclExpression(LocatedElement):

    pass
class ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

