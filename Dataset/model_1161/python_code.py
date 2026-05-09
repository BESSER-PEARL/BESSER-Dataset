from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Parameter:

    pass
class OclModelElement:

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
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType133"):
                opp_val = getattr(old_value, "OclType133", None)
                if opp_val == self:
                    setattr(old_value, "OclType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType133"):
                opp_val = getattr(value, "OclType133", None)
                setattr(value, "OclType133", self)

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
            if hasattr(old_value, "OclExpression131"):
                opp_val = getattr(old_value, "OclExpression131", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression131"):
                opp_val = getattr(value, "OclExpression131", None)
                setattr(value, "OclExpression131", self)

class OCL_Operation(OclFeature):

    def __init__(self, name: str, operation136: "OclType" = None, owningOperation: "OclExpression" = None, operation: set["Parameter"] = None, OclFeature: "OCL_OclFeatureDefinition" = None):
        self.name = name
        self.operation136 = operation136
        self.owningOperation = owningOperation
        self.operation = operation if operation is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "OclExpression139"):
                opp_val = getattr(old_value, "OclExpression139", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression139"):
                opp_val = getattr(value, "OclExpression139", None)
                setattr(value, "OclExpression139", self)

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
    def operation136(self):
        return self.__operation136

    @operation136.setter
    def operation136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__operation136", None)
        self.__operation136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType137"):
                opp_val = getattr(old_value, "OclType137", None)
                if opp_val == self:
                    setattr(old_value, "OclType137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType137"):
                opp_val = getattr(value, "OclType137", None)
                setattr(value, "OclType137", self)

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
class OCL_BooleanType(Primitive):

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_BagType(CollectionType):

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class Iterator:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class genericity_dsl_LocatedElement(ABC):

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
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


class OclType:

    pass
class OCL_Primitive(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_MapType(OclType):

    pass
class OCL_OclModelElement(OclType):

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
class OCL_NumericExp(PrimitiveExp):

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
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IterateExp(LoopExp):

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp: "OCL_OclExpression" = None, LoopExp87: "OCL_Iterator" = None):
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
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_LoopExp(PropertyCallExp):

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
                if hasattr(item, "OclExpression61"):
                    opp_val = getattr(item, "OclExpression61", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression61"):
                    opp_val = getattr(item, "OclExpression61", None)
                    
                    setattr(item, "OclExpression61", self)
                    

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
class VariableDeclaration:

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class BaseFeatureBinding:

    pass
class genericity_dsl_OclFeatureBinding(BaseFeatureBinding):

    pass
class genericity_dsl_RenamingFeatureBinding(BaseFeatureBinding):

    def __init__(self, concreteFeature: str):
        self.concreteFeature = concreteFeature
        
        pass
    @property
    def concreteFeature(self):
        return self.__concreteFeature

    @concreteFeature.setter
    def concreteFeature(self, concreteFeature: str):
        self.__concreteFeature = concreteFeature


class OclExpression:

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, type107: "VariableDeclaration" = None, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType: "MapType" = None, type99: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type105: "TupleTypeAttribute" = None, OclExpression71: "OCL_LetExp" = None, OclExpression21: "genericity_dsl_BHelper" = None, OclExpression: "genericity_dsl_ClassBinding" = None, OclExpression59: "OCL_PropertyCallExp" = None, OclExpression54: "OCL_MapElement" = None, OclExpression77: "OCL_IfExp" = None, OclExpression131: "OCL_Attribute" = None, OclExpression73: "OCL_IfExp" = None, OclExpression47: "OCL_CollectionExp" = None, OclExpression81: "OCL_VariableDeclaration" = None, OclExpression57: "OCL_MapElement" = None, OclExpression16: "genericity_dsl_OclFeatureBinding" = None, OclExpression94: "OCL_OclType" = None, OclExpression75: "OCL_IfExp" = None, OclExpression63: "OCL_LoopExp" = None, OclExpression61: "OCL_OperationCallExp" = None, OclExpression139: "OCL_Operation" = None):
        self.name = name
        self.type107 = type107
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type99 = type99
        self.keyType = keyType
        self.elementType = elementType
        self.type105 = type105
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type99(self):
        return self.__type99

    @type99.setter
    def type99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type99", None)
        self.__type99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute100"):
                opp_val = getattr(old_value, "Attribute100", None)
                if opp_val == self:
                    setattr(old_value, "Attribute100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute100"):
                opp_val = getattr(value, "Attribute100", None)
                setattr(value, "Attribute100", self)

    @property
    def type107(self):
        return self.__type107

    @type107.setter
    def type107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type107", None)
        self.__type107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration108"):
                opp_val = getattr(old_value, "VariableDeclaration108", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration108"):
                opp_val = getattr(value, "VariableDeclaration108", None)
                setattr(value, "VariableDeclaration108", self)

    @property
    def type105(self):
        return self.__type105

    @type105.setter
    def type105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type105", None)
        self.__type105 = value
        
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
        old_value = getattr(self, f"_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation96"):
                opp_val = getattr(old_value, "Operation96", None)
                if opp_val == self:
                    setattr(old_value, "Operation96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation96"):
                opp_val = getattr(value, "Operation96", None)
                setattr(value, "Operation96", self)

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
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType102"):
                opp_val = getattr(old_value, "MapType102", None)
                if opp_val == self:
                    setattr(old_value, "MapType102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType102"):
                opp_val = getattr(value, "MapType102", None)
                setattr(value, "MapType102", self)

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
class OCL_IfExp(OclExpression):

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression71: "OCL_LetExp" = None, OclExpression21: "genericity_dsl_BHelper" = None, OclExpression: "genericity_dsl_ClassBinding" = None, OclExpression59: "OCL_PropertyCallExp" = None, OclExpression54: "OCL_MapElement" = None, OclExpression77: "OCL_IfExp" = None, OclExpression131: "OCL_Attribute" = None, OclExpression73: "OCL_IfExp" = None, OclExpression47: "OCL_CollectionExp" = None, OclExpression81: "OCL_VariableDeclaration" = None, OclExpression57: "OCL_MapElement" = None, OclExpression16: "genericity_dsl_OclFeatureBinding" = None, OclExpression94: "OCL_OclType" = None, OclExpression75: "OCL_IfExp" = None, OclExpression63: "OCL_LoopExp" = None, OclExpression61: "OCL_OperationCallExp" = None, OclExpression139: "OCL_Operation" = None):
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
class OCL_SuperExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_CollectionExp(OclExpression):

    pass
class OCL_TupleExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class ConcreteMetaclass:

    pass
class ConceptMetaclass:

    pass
class BindingModel:

    pass
class Metaclass:

    pass
class genericity_dsl_ConcreteMetaclass(Metaclass):

    pass
class genericity_dsl_ConceptMetaclass(Metaclass):

    pass
class BHelper:

    pass
class ConceptBinding:

    pass
class genericity_dsl_ClassBinding(ConceptBinding):

    pass
class genericity_dsl_BaseFeatureBinding(ConceptBinding):

    def __init__(self, conceptFeature: str, genericity_dsl_BaseFeatureBinding: "ConceptMetaclass" = None, genericity_dsl_BaseFeatureBinding13: "ConcreteMetaclass" = None, ConceptBinding: "genericity_dsl_BindingModel" = None):
        self.conceptFeature = conceptFeature
        self.genericity_dsl_BaseFeatureBinding = genericity_dsl_BaseFeatureBinding
        self.genericity_dsl_BaseFeatureBinding13 = genericity_dsl_BaseFeatureBinding13
        
        pass
    @property
    def conceptFeature(self):
        return self.__conceptFeature

    @conceptFeature.setter
    def conceptFeature(self, conceptFeature: str):
        self.__conceptFeature = conceptFeature


    @property
    def genericity_dsl_BaseFeatureBinding13(self):
        return self.__genericity_dsl_BaseFeatureBinding13

    @genericity_dsl_BaseFeatureBinding13.setter
    def genericity_dsl_BaseFeatureBinding13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BaseFeatureBinding__genericity_dsl_BaseFeatureBinding13", None)
        self.__genericity_dsl_BaseFeatureBinding13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass14"):
                opp_val = getattr(old_value, "ConcreteMetaclass14", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass14"):
                opp_val = getattr(value, "ConcreteMetaclass14", None)
                setattr(value, "ConcreteMetaclass14", self)

    @property
    def genericity_dsl_BaseFeatureBinding(self):
        return self.__genericity_dsl_BaseFeatureBinding

    @genericity_dsl_BaseFeatureBinding.setter
    def genericity_dsl_BaseFeatureBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BaseFeatureBinding__genericity_dsl_BaseFeatureBinding", None)
        self.__genericity_dsl_BaseFeatureBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass11"):
                opp_val = getattr(old_value, "ConceptMetaclass11", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass11"):
                opp_val = getattr(value, "ConceptMetaclass11", None)
                setattr(value, "ConceptMetaclass11", self)

class LocatedElement:

    pass
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
            if hasattr(old_value, "OclType112"):
                opp_val = getattr(old_value, "OclType112", None)
                if opp_val == self:
                    setattr(old_value, "OclType112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType112"):
                opp_val = getattr(value, "OclType112", None)
                setattr(value, "OclType112", self)

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

class OCL_OclFeatureDefinition(LocatedElement):

    pass
class genericity_dsl_ConceptBinding(LocatedElement):

    def __init__(self, debugName: str, bindings: "BindingModel" = None):
        self.debugName = debugName
        self.bindings = bindings
        
        pass
    @property
    def debugName(self):
        return self.__debugName

    @debugName.setter
    def debugName(self, debugName: str):
        self.__debugName = debugName


    @property
    def bindings(self):
        return self.__bindings

    @bindings.setter
    def bindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_ConceptBinding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingModel"):
                opp_val = getattr(old_value, "BindingModel", None)
                if opp_val == self:
                    setattr(old_value, "BindingModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingModel"):
                opp_val = getattr(value, "BindingModel", None)
                setattr(value, "BindingModel", self)

class genericity_dsl_Metaclass(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model: "OclModel" = None, model143: set["OclModelElement"] = None, metamodel: set["OclModel"] = None):
        self.name = name
        self.model = model
        self.model143 = model143 if model143 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model143(self):
        return self.__model143

    @model143.setter
    def model143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model143", None)
        self.__model143 = value if value is not None else set()
        
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
            if hasattr(old_value, "OclModel141"):
                opp_val = getattr(old_value, "OclModel141", None)
                if opp_val == self:
                    setattr(old_value, "OclModel141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel141"):
                opp_val = getattr(value, "OclModel141", None)
                setattr(value, "OclModel141", self)

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
                if hasattr(item, "OclModel145"):
                    opp_val = getattr(item, "OclModel145", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel145"):
                    opp_val = getattr(item, "OclModel145", None)
                    
                    setattr(item, "OclModel145", self)
                    

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
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType79"):
                opp_val = getattr(old_value, "OclType79", None)
                if opp_val == self:
                    setattr(old_value, "OclType79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType79"):
                opp_val = getattr(value, "OclType79", None)
                setattr(value, "OclType79", self)

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
            if hasattr(old_value, "LetExp83"):
                opp_val = getattr(old_value, "LetExp83", None)
                if opp_val == self:
                    setattr(old_value, "LetExp83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp83"):
                opp_val = getattr(value, "LetExp83", None)
                setattr(value, "LetExp83", self)

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
            if hasattr(old_value, "OclExpression81"):
                opp_val = getattr(old_value, "OclExpression81", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression81"):
                opp_val = getattr(value, "OclExpression81", None)
                setattr(value, "OclExpression81", self)

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

class genericity_dsl_BHelper(LocatedElement):

    def __init__(self, feature: str, genericity_dsl_BHelper: "ConceptMetaclass" = None, genericity_dsl_BHelper20: "OclExpression" = None, genericity_dsl_BHelper23: "OclType" = None, helpers: "BindingModel" = None):
        self.feature = feature
        self.genericity_dsl_BHelper = genericity_dsl_BHelper
        self.genericity_dsl_BHelper20 = genericity_dsl_BHelper20
        self.genericity_dsl_BHelper23 = genericity_dsl_BHelper23
        self.helpers = helpers
        
        pass
    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def helpers(self):
        return self.__helpers

    @helpers.setter
    def helpers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__helpers", None)
        self.__helpers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingModel25"):
                opp_val = getattr(old_value, "BindingModel25", None)
                if opp_val == self:
                    setattr(old_value, "BindingModel25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingModel25"):
                opp_val = getattr(value, "BindingModel25", None)
                setattr(value, "BindingModel25", self)

    @property
    def genericity_dsl_BHelper23(self):
        return self.__genericity_dsl_BHelper23

    @genericity_dsl_BHelper23.setter
    def genericity_dsl_BHelper23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper23", None)
        self.__genericity_dsl_BHelper23 = value
        
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
    def genericity_dsl_BHelper(self):
        return self.__genericity_dsl_BHelper

    @genericity_dsl_BHelper.setter
    def genericity_dsl_BHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper", None)
        self.__genericity_dsl_BHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass18"):
                opp_val = getattr(old_value, "ConceptMetaclass18", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass18"):
                opp_val = getattr(value, "ConceptMetaclass18", None)
                setattr(value, "ConceptMetaclass18", self)

    @property
    def genericity_dsl_BHelper20(self):
        return self.__genericity_dsl_BHelper20

    @genericity_dsl_BHelper20.setter
    def genericity_dsl_BHelper20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper20", None)
        self.__genericity_dsl_BHelper20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression21"):
                opp_val = getattr(old_value, "OclExpression21", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression21"):
                opp_val = getattr(value, "OclExpression21", None)
                setattr(value, "OclExpression21", self)

class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeature(LocatedElement):

    pass
class OCL_OclExpression(LocatedElement):

    pass
class genericity_dsl_BindingModel(LocatedElement):

    def __init__(self, metamodel: str, name: str, model_2: set["BHelper"] = None, genericity_dsl_BindingModel: set["VariableDeclaration"] = None, model_: set["ConceptBinding"] = None):
        self.metamodel = metamodel
        self.name = name
        self.model_2 = model_2 if model_2 is not None else set()
        self.genericity_dsl_BindingModel = genericity_dsl_BindingModel if genericity_dsl_BindingModel is not None else set()
        self.model_ = model_ if model_ is not None else set()
        
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
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel


    @property
    def model_2(self):
        return self.__model_2

    @model_2.setter
    def model_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__model_2", None)
        self.__model_2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BHelper"):
                    opp_val = getattr(item, "BHelper", None)
                    
                    if opp_val == self:
                        setattr(item, "BHelper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BHelper"):
                    opp_val = getattr(item, "BHelper", None)
                    
                    setattr(item, "BHelper", self)
                    

    @property
    def genericity_dsl_BindingModel(self):
        return self.__genericity_dsl_BindingModel

    @genericity_dsl_BindingModel.setter
    def genericity_dsl_BindingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__genericity_dsl_BindingModel", None)
        self.__genericity_dsl_BindingModel = value if value is not None else set()
        
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
                    

    @property
    def model_(self):
        return self.__model_

    @model_.setter
    def model_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__model_", None)
        self.__model_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConceptBinding"):
                    opp_val = getattr(item, "ConceptBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "ConceptBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConceptBinding"):
                    opp_val = getattr(item, "ConceptBinding", None)
                    
                    setattr(item, "ConceptBinding", self)
                    
