from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class Parameter:

    pass
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
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
            if hasattr(old_value, "OclExpression115"):
                opp_val = getattr(old_value, "OclExpression115", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression115"):
                opp_val = getattr(value, "OclExpression115", None)
                setattr(value, "OclExpression115", self)

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
            if hasattr(old_value, "OclType117"):
                opp_val = getattr(old_value, "OclType117", None)
                if opp_val == self:
                    setattr(old_value, "OclType117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType117"):
                opp_val = getattr(value, "OclType117", None)
                setattr(value, "OclType117", self)

class OCL_Operation(OclFeature):

    def __init__(self, name: str, operation: set["Parameter"] = None, operation120: "OclType" = None, owningOperation: "OclExpression" = None, OclFeature: "OCL_OclFeatureDefinition" = None):
        self.name = name
        self.operation = operation if operation is not None else set()
        self.operation120 = operation120
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
    def operation120(self):
        return self.__operation120

    @operation120.setter
    def operation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__operation120", None)
        self.__operation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType121"):
                opp_val = getattr(old_value, "OclType121", None)
                if opp_val == self:
                    setattr(old_value, "OclType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType121"):
                opp_val = getattr(value, "OclType121", None)
                setattr(value, "OclType121", self)

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
            if hasattr(old_value, "OclExpression123"):
                opp_val = getattr(old_value, "OclExpression123", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression123"):
                opp_val = getattr(value, "OclExpression123", None)
                setattr(value, "OclExpression123", self)

class OclModel:

    pass
class TupleType:

    pass
class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class VariableExp:

    pass
class IterateExp:

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


class Attribute:

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IterateExp(LoopExp):

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp: "OCL_OclExpression" = None, LoopExp71: "OCL_Iterator" = None):
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
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

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
                if hasattr(item, "OclExpression45"):
                    opp_val = getattr(item, "OclExpression45", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression45"):
                    opp_val = getattr(item, "OclExpression45", None)
                    
                    setattr(item, "OclExpression45", self)
                    

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
class OCL_MapType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class ocl_constraints_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


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


class OclExpression:

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType: "MapType" = None, type83: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type89: "TupleTypeAttribute" = None, type91: "VariableDeclaration" = None, OclExpression47: "OCL_LoopExp" = None, OclExpression57: "OCL_IfExp" = None, OclExpression61: "OCL_IfExp" = None, OclExpression: "ocl_constraints_OclInvariant" = None, OclExpression55: "OCL_LetExp" = None, OclExpression123: "OCL_Operation" = None, OclExpression59: "OCL_IfExp" = None, OclExpression31: "OCL_CollectionExp" = None, OclExpression41: "OCL_MapElement" = None, OclExpression78: "OCL_OclType" = None, OclExpression38: "OCL_MapElement" = None, OclExpression10: "ocl_constraints_OclPrecondition" = None, OclExpression115: "OCL_Attribute" = None, OclExpression43: "OCL_PropertyCallExp" = None, OclExpression65: "OCL_VariableDeclaration" = None, OclExpression45: "OCL_OperationCallExp" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type83 = type83
        self.keyType = keyType
        self.elementType = elementType
        self.type89 = type89
        self.type91 = type91
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression78"):
                opp_val = getattr(old_value, "OclExpression78", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression78"):
                opp_val = getattr(value, "OclExpression78", None)
                setattr(value, "OclExpression78", self)

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
            if hasattr(old_value, "MapType86"):
                opp_val = getattr(old_value, "MapType86", None)
                if opp_val == self:
                    setattr(old_value, "MapType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType86"):
                opp_val = getattr(value, "MapType86", None)
                setattr(value, "MapType86", self)

    @property
    def type91(self):
        return self.__type91

    @type91.setter
    def type91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type91", None)
        self.__type91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration92"):
                opp_val = getattr(old_value, "VariableDeclaration92", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration92"):
                opp_val = getattr(value, "VariableDeclaration92", None)
                setattr(value, "VariableDeclaration92", self)

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

    @property
    def type89(self):
        return self.__type89

    @type89.setter
    def type89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type89", None)
        self.__type89 = value
        
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
    def type83(self):
        return self.__type83

    @type83.setter
    def type83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type83", None)
        self.__type83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute84"):
                opp_val = getattr(old_value, "Attribute84", None)
                if opp_val == self:
                    setattr(old_value, "Attribute84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute84"):
                opp_val = getattr(value, "Attribute84", None)
                setattr(value, "Attribute84", self)

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
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation80"):
                opp_val = getattr(old_value, "Operation80", None)
                if opp_val == self:
                    setattr(old_value, "Operation80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation80"):
                opp_val = getattr(value, "Operation80", None)
                setattr(value, "Operation80", self)

class OCL_LetExp(OclExpression):

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_TupleExp(OclExpression):

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression47: "OCL_LoopExp" = None, OclExpression57: "OCL_IfExp" = None, OclExpression61: "OCL_IfExp" = None, OclExpression: "ocl_constraints_OclInvariant" = None, OclExpression55: "OCL_LetExp" = None, OclExpression123: "OCL_Operation" = None, OclExpression59: "OCL_IfExp" = None, OclExpression31: "OCL_CollectionExp" = None, OclExpression41: "OCL_MapElement" = None, OclExpression78: "OCL_OclType" = None, OclExpression38: "OCL_MapElement" = None, OclExpression10: "ocl_constraints_OclPrecondition" = None, OclExpression115: "OCL_Attribute" = None, OclExpression43: "OCL_PropertyCallExp" = None, OclExpression65: "OCL_VariableDeclaration" = None, OclExpression45: "OCL_OperationCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_MapExp(OclExpression):

    pass
class OCL_CollectionExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OclPrecondition:

    pass
class OclInvariant:

    pass
class OclConstraintsModel:

    pass
class Metaclass:

    pass
class ocl_constraints_UMLClass(Metaclass):

    pass
class VariableDeclaration:

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class Context:

    pass
class LocatedElement:

    pass
class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, variableDeclaration: "OclType" = None, initializedVariable: "OclExpression" = None, variable: "LetExp" = None, result: "IterateExp" = None, referredVariable: set["VariableExp"] = None):
        self.id = id
        self.varName = varName
        self.variableDeclaration = variableDeclaration
        self.initializedVariable = initializedVariable
        self.variable = variable
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        
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
            if hasattr(old_value, "LetExp67"):
                opp_val = getattr(old_value, "LetExp67", None)
                if opp_val == self:
                    setattr(old_value, "LetExp67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp67"):
                opp_val = getattr(value, "LetExp67", None)
                setattr(value, "LetExp67", self)

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
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType63"):
                opp_val = getattr(old_value, "OclType63", None)
                if opp_val == self:
                    setattr(old_value, "OclType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType63"):
                opp_val = getattr(value, "OclType63", None)
                setattr(value, "OclType63", self)

class ocl_constraints_OclPrecondition(LocatedElement):

    def __init__(self, name: str, description: str, ocl_constraints_OclPrecondition: "OclExpression" = None):
        self.name = name
        self.description = description
        self.ocl_constraints_OclPrecondition = ocl_constraints_OclPrecondition
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ocl_constraints_OclPrecondition(self):
        return self.__ocl_constraints_OclPrecondition

    @ocl_constraints_OclPrecondition.setter
    def ocl_constraints_OclPrecondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_constraints_OclPrecondition__ocl_constraints_OclPrecondition", None)
        self.__ocl_constraints_OclPrecondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression10"):
                opp_val = getattr(old_value, "OclExpression10", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression10"):
                opp_val = getattr(value, "OclExpression10", None)
                setattr(value, "OclExpression10", self)

class ocl_constraints_OclInvariant(LocatedElement):

    def __init__(self, name: str, description: str, ocl_constraints_OclInvariant: "OclExpression" = None):
        self.name = name
        self.description = description
        self.ocl_constraints_OclInvariant = ocl_constraints_OclInvariant
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ocl_constraints_OclInvariant(self):
        return self.__ocl_constraints_OclInvariant

    @ocl_constraints_OclInvariant.setter
    def ocl_constraints_OclInvariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_constraints_OclInvariant__ocl_constraints_OclInvariant", None)
        self.__ocl_constraints_OclInvariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression"):
                opp_val = getattr(old_value, "OclExpression", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression"):
                opp_val = getattr(value, "OclExpression", None)
                setattr(value, "OclExpression", self)

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
            if hasattr(old_value, "OclType96"):
                opp_val = getattr(old_value, "OclType96", None)
                if opp_val == self:
                    setattr(old_value, "OclType96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType96"):
                opp_val = getattr(value, "OclType96", None)
                setattr(value, "OclType96", self)

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

class ocl_constraints_Context(LocatedElement):

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model: "OclModel" = None, model127: set["OclModelElement"] = None, metamodel: set["OclModel"] = None):
        self.name = name
        self.model = model
        self.model127 = model127 if model127 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model127(self):
        return self.__model127

    @model127.setter
    def model127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model127", None)
        self.__model127 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_OCL_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel125"):
                opp_val = getattr(old_value, "OclModel125", None)
                if opp_val == self:
                    setattr(old_value, "OclModel125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel125"):
                opp_val = getattr(value, "OclModel125", None)
                setattr(value, "OclModel125", self)

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
                if hasattr(item, "OclModel129"):
                    opp_val = getattr(item, "OclModel129", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel129"):
                    opp_val = getattr(item, "OclModel129", None)
                    
                    setattr(item, "OclModel129", self)
                    

class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_MapElement(LocatedElement):

    pass
class ocl_constraints_Metaclass(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_OclExpression(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class OCL_OclFeature(LocatedElement):

    pass
class ocl_constraints_OclConstraintsModel(LocatedElement):

    def __init__(self, metamodel: str, name: str, model_: set["Context"] = None, ocl_constraints_OclConstraintsModel: set["VariableDeclaration"] = None):
        self.metamodel = metamodel
        self.name = name
        self.model_ = model_ if model_ is not None else set()
        self.ocl_constraints_OclConstraintsModel = ocl_constraints_OclConstraintsModel if ocl_constraints_OclConstraintsModel is not None else set()
        
        pass
    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model_(self):
        return self.__model_

    @model_.setter
    def model_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_constraints_OclConstraintsModel__model_", None)
        self.__model_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Context"):
                    opp_val = getattr(item, "Context", None)
                    
                    if opp_val == self:
                        setattr(item, "Context", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Context"):
                    opp_val = getattr(item, "Context", None)
                    
                    setattr(item, "Context", self)
                    

    @property
    def ocl_constraints_OclConstraintsModel(self):
        return self.__ocl_constraints_OclConstraintsModel

    @ocl_constraints_OclConstraintsModel.setter
    def ocl_constraints_OclConstraintsModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_constraints_OclConstraintsModel__ocl_constraints_OclConstraintsModel", None)
        self.__ocl_constraints_OclConstraintsModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    setattr(item, "VariableDeclaration", self)
                    

class UMLClass:

    pass