from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Parameter:

    pass
class OclInstanceModel:

    pass
class OclModelElement:

    pass
class TupleType:

    pass
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
class QualityMetamodel_QMM_OCL_Operation(OclFeature):

    pass
class QualityMetamodel_QMM_OCL_Attribute(OclFeature):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class MapType:

    pass
class QualityMetamodel_QMM_OCL_SetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_SequenceType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_OrderedSetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_BagType(CollectionType):

    pass
class NumericType:

    pass
class QualityMetamodel_QMM_OCL_RealType(NumericType):

    pass
class QualityMetamodel_QMM_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class QualityMetamodel_QMM_OCL_NumericType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_BooleanType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_StringType(Primitive):

    pass
class OclModel:

    pass
class QualityMetamodel_QMM_OCL_OclInstanceModel(OclModel):

    pass
class QualityMetamodel_QMM_OCL_OclMetamodel(OclModel):

    def __init__(self, uri: str, metamodel: set["OclInstanceModel"] = None, OclModel: "QualityMetamodel_QMM_OCL_OclModelElementExp" = None, OclModel157: "QualityMetamodel_QMM_OCL_OclModelElement" = None):
        self.uri = uri
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclMetamodel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclInstanceModel"):
                    opp_val = getattr(item, "OclInstanceModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclInstanceModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclInstanceModel"):
                    opp_val = getattr(item, "OclInstanceModel", None)
                    
                    setattr(item, "OclInstanceModel", self)
                    

class LambdaType:

    pass
class OclContextDefinition:

    pass
class IterateExp:

    pass
class Iterator:

    pass
class PropertyCall:

    pass
class QualityMetamodel_QMM_OCL_LoopExp(PropertyCall):

    pass
class VariableExp:

    pass
class QualityMetamodel_QMM_OCL_LambdaCallExp(VariableExp):

    pass
class QualityMetamodel_QMM_OCL_OperationCall(PropertyCall):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, PropertyCall: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None):
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
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperationCall__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression85"):
                    opp_val = getattr(item, "OclExpression85", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression85"):
                    opp_val = getattr(item, "OclExpression85", None)
                    
                    setattr(item, "OclExpression85", self)
                    

class QualityMetamodel_QMM_OCL_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str, PropertyCall: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class StaticPropertyCallExp:

    pass
class StaticPropertyCall:

    pass
class QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str, StaticPropertyCall: "QualityMetamodel_QMM_OCL_StaticPropertyCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QualityMetamodel_QMM_OCL_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, QualityMetamodel_QMM_OCL_StaticOperationCall: set["OclExpression"] = None, StaticPropertyCall: "QualityMetamodel_QMM_OCL_StaticPropertyCallExp" = None):
        self.operationName = operationName
        self.QualityMetamodel_QMM_OCL_StaticOperationCall = QualityMetamodel_QMM_OCL_StaticOperationCall if QualityMetamodel_QMM_OCL_StaticOperationCall is not None else set()
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def QualityMetamodel_QMM_OCL_StaticOperationCall(self):
        return self.__QualityMetamodel_QMM_OCL_StaticOperationCall

    @QualityMetamodel_QMM_OCL_StaticOperationCall.setter
    def QualityMetamodel_QMM_OCL_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_StaticOperationCall__QualityMetamodel_QMM_OCL_StaticOperationCall", None)
        self.__QualityMetamodel_QMM_OCL_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression78"):
                    opp_val = getattr(item, "OclExpression78", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression78"):
                    opp_val = getattr(item, "OclExpression78", None)
                    
                    setattr(item, "OclExpression78", self)
                    

class NumericExp:

    pass
class QualityMetamodel_QMM_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class QualityMetamodel_QMM_OCL_RealExp(NumericExp):

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
class QualityMetamodel_QMM_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class QualityMetamodel_QMM_OCL_NumericExp(PrimitiveExp):

    pass
class QualityMetamodel_QMM_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class TuplePart:

    pass
class CollectionExp:

    pass
class QualityMetamodel_QMM_OCL_OrderedSetExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_SequenceExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_BagExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_SetExp(CollectionExp):

    pass
class CollectionPart:

    pass
class QualityMetamodel_QMM_OCL_CollectionRange(CollectionPart):

    pass
class QualityMetamodel_QMM_OCL_CollectionItem(CollectionPart):

    pass
class LocalVariable:

    pass
class QualityMetamodel_QMM_OCL_TuplePart(LocalVariable):

    pass
class OperatorCallExp:

    pass
class QualityMetamodel_QMM_OCL_NotOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_IntOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_MulOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_EqOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_RelOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_AddOpCallExp(OperatorCallExp):

    pass
class Attribute:

    pass
class Operation:

    pass
class ModuleElement:

    pass
class QualityMetamodel_QMM_OCL_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, definition: "OclFeature" = None, definition168: "OclContextDefinition" = None, ModuleElement: "QualityMetamodel_QMM_OCL_Module" = None):
        self.static = static
        self.definition = definition
        self.definition168 = definition168
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def definition(self):
        return self.__definition

    @definition.setter
    def definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeatureDefinition__definition", None)
        self.__definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeature"):
                opp_val = getattr(old_value, "OclFeature", None)
                if opp_val == self:
                    setattr(old_value, "OclFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeature"):
                opp_val = getattr(value, "OclFeature", None)
                setattr(value, "OclFeature", self)

    @property
    def definition168(self):
        return self.__definition168

    @definition168.setter
    def definition168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeatureDefinition__definition168", None)
        self.__definition168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition169"):
                opp_val = getattr(old_value, "OclContextDefinition169", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition169"):
                opp_val = getattr(value, "OclContextDefinition169", None)
                setattr(value, "OclContextDefinition169", self)

class OperationCall:

    pass
class QualityMetamodel_QMM_OCL_CollectionOperationCall(OperationCall):

    pass
class LoopExp:

    pass
class QualityMetamodel_QMM_OCL_IterateExp(LoopExp):

    pass
class QualityMetamodel_QMM_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp119: "QualityMetamodel_QMM_OCL_Iterator" = None, LoopExp: "QualityMetamodel_QMM_OCL_OclExpression" = None):
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
class PropertyCallExp:

    pass
class IfExp:

    pass
class OclType:

    pass
class QualityMetamodel_QMM_OCL_EnvType(OclType):

    pass
class QualityMetamodel_QMM_OCL_LambdaType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclAnyType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclModelElement(OclType):

    pass
class QualityMetamodel_QMM_OCL_TupleType(OclType):

    pass
class QualityMetamodel_QMM_OCL_CollectionType(OclType):

    pass
class QualityMetamodel_QMM_OCL_Primitive(OclType):

    pass
class QualityMetamodel_QMM_OCL_MapType(OclType):

    pass
class ValueType:

    pass
class QualityMetamodel_RangeValueType(ValueType):

    def __init__(self, min: str, max: str):
        self.min = min
        self.max = max
        
        pass
    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min


class QualityMetamodel_AggregatedValueMetric(ValueType):

    def __init__(self, maximum: str, average: str, median: str, standardDeviation: str, minimum: str):
        self.maximum = maximum
        self.average = average
        self.median = median
        self.standardDeviation = standardDeviation
        self.minimum = minimum
        
        pass
    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum


    @property
    def standardDeviation(self):
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: str):
        self.__standardDeviation = standardDeviation


    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum


    @property
    def average(self):
        return self.__average

    @average.setter
    def average(self, average: str):
        self.__average = average


    @property
    def median(self):
        return self.__median

    @median.setter
    def median(self, median: str):
        self.__median = median


class QualityMetamodel_TextValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Import:

    pass
class OclMetamodel:

    pass
class NamedElement:

    pass
class QualityMetamodel_QMM_OCL_Import(NamedElement):

    pass
class QualityMetamodel_QMM_OCL_OclFeature(NamedElement):

    def __init__(self, eq: str, feature: "OclFeatureDefinition" = None):
        self.eq = eq
        self.feature = feature
        
        pass
    @property
    def eq(self):
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition175"):
                opp_val = getattr(old_value, "OclFeatureDefinition175", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition175"):
                opp_val = getattr(value, "OclFeatureDefinition175", None)
                setattr(value, "OclFeatureDefinition175", self)

class QualityMetamodel_QMM_OCL_OclModel(NamedElement):

    pass
class QualityMetamodel_QMM_OCL_Module(NamedElement):

    pass
class LocatedElement:

    pass
class QualityMetamodel_QMM_OCL_StaticPropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_MapElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_CollectionPart(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclExpression(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_PropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_TupleTypeAttribute(LocatedElement):

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
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_TupleTypeAttribute__attributes", None)
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
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType153"):
                opp_val = getattr(old_value, "OclType153", None)
                if opp_val == self:
                    setattr(old_value, "OclType153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType153"):
                opp_val = getattr(value, "OclType153", None)
                setattr(value, "OclType153", self)

class QualityMetamodel_QMM_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, referredVariable: set["VariableExp"] = None, variableDeclaration: "OclType" = None):
        self.varName = varName
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.variableDeclaration = variableDeclaration
        
        pass
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
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType111"):
                opp_val = getattr(old_value, "OclType111", None)
                if opp_val == self:
                    setattr(old_value, "OclType111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType111"):
                opp_val = getattr(value, "OclType111", None)
                setattr(value, "OclType111", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_VariableDeclaration__referredVariable", None)
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
                    

class QualityMetamodel_QMM_OCL_ModuleElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclType(LocatedElement):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, type140: "VariableDeclaration" = None, returnType143: "LambdaType" = None, argumentTypes: "LambdaType" = None, source147: "StaticPropertyCallExp" = None, returnType: "Operation" = None, valueType130: "MapType" = None, type132: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type138: "TupleTypeAttribute" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.type140 = type140
        self.returnType143 = returnType143
        self.argumentTypes = argumentTypes
        self.source147 = source147
        self.returnType = returnType
        self.valueType130 = valueType130
        self.type132 = type132
        self.keyType = keyType
        self.elementType = elementType
        self.type138 = type138
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type138(self):
        return self.__type138

    @type138.setter
    def type138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type138", None)
        self.__type138 = value
        
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
    def argumentTypes(self):
        return self.__argumentTypes

    @argumentTypes.setter
    def argumentTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__argumentTypes", None)
        self.__argumentTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType145"):
                opp_val = getattr(old_value, "LambdaType145", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType145"):
                opp_val = getattr(value, "LambdaType145", None)
                setattr(value, "LambdaType145", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__context_", None)
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
    def source147(self):
        return self.__source147

    @source147.setter
    def source147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__source147", None)
        self.__source147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticPropertyCallExp148"):
                opp_val = getattr(old_value, "StaticPropertyCallExp148", None)
                if opp_val == self:
                    setattr(old_value, "StaticPropertyCallExp148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticPropertyCallExp148"):
                opp_val = getattr(value, "StaticPropertyCallExp148", None)
                setattr(value, "StaticPropertyCallExp148", self)

    @property
    def type140(self):
        return self.__type140

    @type140.setter
    def type140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type140", None)
        self.__type140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration141"):
                opp_val = getattr(old_value, "VariableDeclaration141", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration141"):
                opp_val = getattr(value, "VariableDeclaration141", None)
                setattr(value, "VariableDeclaration141", self)

    @property
    def returnType143(self):
        return self.__returnType143

    @returnType143.setter
    def returnType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__returnType143", None)
        self.__returnType143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType"):
                opp_val = getattr(old_value, "LambdaType", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType"):
                opp_val = getattr(value, "LambdaType", None)
                setattr(value, "LambdaType", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__elementType", None)
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
    def type132(self):
        return self.__type132

    @type132.setter
    def type132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type132", None)
        self.__type132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute133"):
                opp_val = getattr(old_value, "Attribute133", None)
                if opp_val == self:
                    setattr(old_value, "Attribute133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute133"):
                opp_val = getattr(value, "Attribute133", None)
                setattr(value, "Attribute133", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation128"):
                opp_val = getattr(old_value, "Operation128", None)
                if opp_val == self:
                    setattr(old_value, "Operation128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation128"):
                opp_val = getattr(value, "Operation128", None)
                setattr(value, "Operation128", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression126"):
                opp_val = getattr(old_value, "OclExpression126", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression126"):
                opp_val = getattr(value, "OclExpression126", None)
                setattr(value, "OclExpression126", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType135"):
                opp_val = getattr(old_value, "MapType135", None)
                if opp_val == self:
                    setattr(old_value, "MapType135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType135"):
                opp_val = getattr(value, "MapType135", None)
                setattr(value, "MapType135", self)

    @property
    def valueType130(self):
        return self.__valueType130

    @valueType130.setter
    def valueType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__valueType130", None)
        self.__valueType130 = value
        
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

class QualityMetamodel_QMM_OCL_OclContextDefinition(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QualityMetamodel_QMM_OCL_LocatedElement(ABC):

    def __init__(self, line: str, column: str, charStart: str, charEnd: str):
        self.line = line
        self.column = column
        self.charStart = charStart
        self.charEnd = charEnd
        
        pass
    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line


    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column


    @property
    def charStart(self):
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart


    @property
    def charEnd(self):
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd


class QualityMetamodel_ListValue(ValueType):

    pass
class QualityMetamodel_IntegerValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class QualityMetamodel_BooleanValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class QualityMetamodel_RealValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class QualityMetamodel_EnumerationItem:

    def __init__(self, name: str, QualityMetamodel_EnumerationItem: "QualityMetamodel_EnumerationMetric" = None, QualityMetamodel_EnumerationItem26: "QualityMetamodel_EnumerationMetric" = None):
        self.name = name
        self.QualityMetamodel_EnumerationItem = QualityMetamodel_EnumerationItem
        self.QualityMetamodel_EnumerationItem26 = QualityMetamodel_EnumerationItem26
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def QualityMetamodel_EnumerationItem(self):
        return self.__QualityMetamodel_EnumerationItem

    @QualityMetamodel_EnumerationItem.setter
    def QualityMetamodel_EnumerationItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem", None)
        self.__QualityMetamodel_EnumerationItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_EnumerationMetric", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QualityMetamodel_EnumerationItem26(self):
        return self.__QualityMetamodel_EnumerationItem26

    @QualityMetamodel_EnumerationItem26.setter
    def QualityMetamodel_EnumerationItem26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem26", None)
        self.__QualityMetamodel_EnumerationItem26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric25"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric25", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_EnumerationMetric25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric25"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric25", None)
                setattr(value, "QualityMetamodel_EnumerationMetric25", self)

class QualityMetamodel_EnumerationMetric(ValueType):

    pass
class QualityMetamodel_MetricProvider:

    def __init__(self, name: str, description: str, id: str, QualityMetamodel_MetricProvider: "QualityMetamodel_QualityModel" = None, QualityMetamodel_MetricProvider16: "QualityMetamodel_SingleValue" = None):
        self.name = name
        self.description = description
        self.id = id
        self.QualityMetamodel_MetricProvider = QualityMetamodel_MetricProvider
        self.QualityMetamodel_MetricProvider16 = QualityMetamodel_MetricProvider16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def QualityMetamodel_MetricProvider(self):
        return self.__QualityMetamodel_MetricProvider

    @QualityMetamodel_MetricProvider.setter
    def QualityMetamodel_MetricProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider", None)
        self.__QualityMetamodel_MetricProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QualityMetamodel_MetricProvider16(self):
        return self.__QualityMetamodel_MetricProvider16

    @QualityMetamodel_MetricProvider16.setter
    def QualityMetamodel_MetricProvider16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider16", None)
        self.__QualityMetamodel_MetricProvider16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(old_value, "QualityMetamodel_SingleValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_SingleValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(value, "QualityMetamodel_SingleValue", None)
                setattr(value, "QualityMetamodel_SingleValue", self)

class Module:

    pass
class QualityMetamodel_QualityModel(Module):

    pass
class OclExpression:

    pass
class QualityMetamodel_QMM_OCL_PropertyCallExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_LetExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_SuperExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_StaticPropertyCallExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_SelfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnvExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_PrimitiveExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_TupleExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OclModelElementExp(OclExpression):

    def __init__(self, name: str, QualityMetamodel_QMM_OCL_OclModelElementExp: "OclModel" = None, OclExpression177: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression57: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression69: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression185: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression81: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None, OclExpression89: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression78: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression95: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression103: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression72: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression62: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression126: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression109: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression116: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression91: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionRange" = None):
        self.name = name
        self.QualityMetamodel_QMM_OCL_OclModelElementExp = QualityMetamodel_QMM_OCL_OclModelElementExp
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def QualityMetamodel_QMM_OCL_OclModelElementExp(self):
        return self.__QualityMetamodel_QMM_OCL_OclModelElementExp

    @QualityMetamodel_QMM_OCL_OclModelElementExp.setter
    def QualityMetamodel_QMM_OCL_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclModelElementExp__QualityMetamodel_QMM_OCL_OclModelElementExp", None)
        self.__QualityMetamodel_QMM_OCL_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel"):
                opp_val = getattr(old_value, "OclModel", None)
                if opp_val == self:
                    setattr(old_value, "OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel"):
                opp_val = getattr(value, "OclModel", None)
                setattr(value, "OclModel", self)

class QualityMetamodel_QMM_OCL_MapExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression177: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression57: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression69: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression185: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression81: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None, OclExpression89: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression78: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression95: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression103: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression72: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression62: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression126: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression109: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression116: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression91: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionRange" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QualityMetamodel_QMM_OCL_BraceExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OclUndefinedExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_CollectionExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_IfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, QualityMetamodel_QMM_OCL_OperatorCallExp: "OclExpression" = None, appliedOperator: "OclExpression" = None, OclExpression177: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression57: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression69: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression185: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression81: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None, OclExpression89: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression78: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression95: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression103: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression72: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression62: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression126: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression109: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression116: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression91: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionRange" = None):
        self.operationName = operationName
        self.QualityMetamodel_QMM_OCL_OperatorCallExp = QualityMetamodel_QMM_OCL_OperatorCallExp
        self.appliedOperator = appliedOperator
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def QualityMetamodel_QMM_OCL_OperatorCallExp(self):
        return self.__QualityMetamodel_QMM_OCL_OperatorCallExp

    @QualityMetamodel_QMM_OCL_OperatorCallExp.setter
    def QualityMetamodel_QMM_OCL_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperatorCallExp__QualityMetamodel_QMM_OCL_OperatorCallExp", None)
        self.__QualityMetamodel_QMM_OCL_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression87"):
                opp_val = getattr(old_value, "OclExpression87", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression87"):
                opp_val = getattr(value, "OclExpression87", None)
                setattr(value, "OclExpression87", self)

    @property
    def appliedOperator(self):
        return self.__appliedOperator

    @appliedOperator.setter
    def appliedOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperatorCallExp__appliedOperator", None)
        self.__appliedOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression89"):
                opp_val = getattr(old_value, "OclExpression89", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression89"):
                opp_val = getattr(value, "OclExpression89", None)
                setattr(value, "OclExpression89", self)

class QualityMetamodel_QMM_OCL_VariableExp(OclExpression):

    pass
class QualityMetamodel_Operation:

    def __init__(self, name: str, body: str, QualityMetamodel_Operation: "QualityMetamodel_AggregatedValue" = None, QualityMetamodel_Operation19: set["QualityMetamodel_Value"] = None, QualityMetamodel_Operation22: "OclExpression" = None):
        self.name = name
        self.body = body
        self.QualityMetamodel_Operation = QualityMetamodel_Operation
        self.QualityMetamodel_Operation19 = QualityMetamodel_Operation19 if QualityMetamodel_Operation19 is not None else set()
        self.QualityMetamodel_Operation22 = QualityMetamodel_Operation22
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def QualityMetamodel_Operation22(self):
        return self.__QualityMetamodel_Operation22

    @QualityMetamodel_Operation22.setter
    def QualityMetamodel_Operation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation22", None)
        self.__QualityMetamodel_Operation22 = value
        
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

    @property
    def QualityMetamodel_Operation19(self):
        return self.__QualityMetamodel_Operation19

    @QualityMetamodel_Operation19.setter
    def QualityMetamodel_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation19", None)
        self.__QualityMetamodel_Operation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_Value20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    setattr(item, "QualityMetamodel_Value20", self)
                    

    @property
    def QualityMetamodel_Operation(self):
        return self.__QualityMetamodel_Operation

    @QualityMetamodel_Operation.setter
    def QualityMetamodel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation", None)
        self.__QualityMetamodel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(old_value, "QualityMetamodel_AggregatedValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_AggregatedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(value, "QualityMetamodel_AggregatedValue", None)
                setattr(value, "QualityMetamodel_AggregatedValue", self)

class Value:

    pass
class QualityMetamodel_AggregatedValue(Value):

    pass
class QualityMetamodel_SingleValue(Value):

    pass
class VariableDeclaration:

    pass
class QualityMetamodel_QMM_OCL_Parameter(VariableDeclaration):

    pass
class QualityMetamodel_QMM_OCL_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, variable: "LetExp" = None, initializedVariable: "OclExpression" = None, result: "IterateExp" = None, VariableDeclaration141: "QualityMetamodel_QMM_OCL_OclType" = None, VariableDeclaration: "QualityMetamodel_QMM_OCL_VariableExp" = None):
        self.eq = eq
        self.variable = variable
        self.initializedVariable = initializedVariable
        self.result = result
        
        pass
    @property
    def eq(self):
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp114"):
                opp_val = getattr(old_value, "LetExp114", None)
                if opp_val == self:
                    setattr(old_value, "LetExp114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp114"):
                opp_val = getattr(value, "LetExp114", None)
                setattr(value, "LetExp114", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__result", None)
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
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression116"):
                opp_val = getattr(old_value, "OclExpression116", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression116"):
                opp_val = getattr(value, "OclExpression116", None)
                setattr(value, "OclExpression116", self)

class QualityMetamodel_QMM_OCL_Iterator(VariableDeclaration):

    pass
class QualityMetamodel_Value(VariableDeclaration):

    def __init__(self, description: str, QualityMetamodel_Value: "QualityMetamodel_QualityModel" = None, QualityMetamodel_Value9: "QualityMetamodel_QualityAttribute" = None, val: "QualityMetamodel_ValueType" = None, Value: "QualityMetamodel_ValueType" = None, QualityMetamodel_Value20: "QualityMetamodel_Operation" = None, VariableDeclaration141: "QualityMetamodel_QMM_OCL_OclType" = None, VariableDeclaration: "QualityMetamodel_QMM_OCL_VariableExp" = None):
        self.description = description
        self.QualityMetamodel_Value = QualityMetamodel_Value
        self.QualityMetamodel_Value9 = QualityMetamodel_Value9
        self.val = val
        self.Value = Value
        self.QualityMetamodel_Value20 = QualityMetamodel_Value20
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__val", None)
        self.__val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType"):
                opp_val = getattr(old_value, "ValueType", None)
                if opp_val == self:
                    setattr(old_value, "ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType"):
                opp_val = getattr(value, "ValueType", None)
                setattr(value, "ValueType", self)

    @property
    def QualityMetamodel_Value(self):
        return self.__QualityMetamodel_Value

    @QualityMetamodel_Value.setter
    def QualityMetamodel_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value", None)
        self.__QualityMetamodel_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel6", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QualityMetamodel_Value9(self):
        return self.__QualityMetamodel_Value9

    @QualityMetamodel_Value9.setter
    def QualityMetamodel_Value9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value9", None)
        self.__QualityMetamodel_Value9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(value, "QualityMetamodel_QualityAttribute8", None)
                setattr(value, "QualityMetamodel_QualityAttribute8", self)

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__Value", None)
        self.__Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueType"):
                opp_val = getattr(old_value, "valueType", None)
                if opp_val == self:
                    setattr(old_value, "valueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueType"):
                opp_val = getattr(value, "valueType", None)
                setattr(value, "valueType", self)

    @property
    def QualityMetamodel_Value20(self):
        return self.__QualityMetamodel_Value20

    @QualityMetamodel_Value20.setter
    def QualityMetamodel_Value20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value20", None)
        self.__QualityMetamodel_Value20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_Operation19"):
                opp_val = getattr(old_value, "QualityMetamodel_Operation19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_Operation19"):
                opp_val = getattr(value, "QualityMetamodel_Operation19", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_Operation19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetamodel_QualityAttribute(VariableDeclaration):

    pass
class QualityMetamodel_ValueType(VariableDeclaration):

    pass