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
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
class QualityMetamodel_QMM_OCL_Operation(OclFeature):

    pass
class QualityMetamodel_QMM_OCL_Attribute(OclFeature):

    pass
class NumericType:

    pass
class QualityMetamodel_QMM_OCL_RealType(NumericType):

    pass
class QualityMetamodel_QMM_OCL_IntegerType(NumericType):

    pass
class TupleType:

    pass
class OclContextDefinition:

    pass
class Primitive:

    pass
class QualityMetamodel_QMM_OCL_BooleanType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_NumericType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_StringType(Primitive):

    pass
class OclModel:

    pass
class QualityMetamodel_QMM_OCL_OclInstanceModel(OclModel):

    pass
class QualityMetamodel_QMM_OCL_OclMetamodel(OclModel):

    def __init__(self, uri: str, metamodel: set["OclInstanceModel"] = None, OclModel155: "QualityMetamodel_QMM_OCL_OclModelElement" = None, OclModel: "QualityMetamodel_QMM_OCL_OclModelElementExp" = None):
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
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class QualityMetamodel_QMM_OCL_OrderedSetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_SetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_BagType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_SequenceType(CollectionType):

    pass
class MapType:

    pass
class IterateExp:

    pass
class Iterator:

    pass
class VariableExp:

    pass
class QualityMetamodel_QMM_OCL_LambdaCallExp(VariableExp):

    pass
class MapExp:

    pass
class MapElement:

    pass
class PropertyCall:

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
                if hasattr(item, "OclExpression83"):
                    opp_val = getattr(item, "OclExpression83", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression83"):
                    opp_val = getattr(item, "OclExpression83", None)
                    
                    setattr(item, "OclExpression83", self)
                    

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


class QualityMetamodel_QMM_OCL_LoopExp(PropertyCall):

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
                if hasattr(item, "OclExpression76"):
                    opp_val = getattr(item, "OclExpression76", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression76"):
                    opp_val = getattr(item, "OclExpression76", None)
                    
                    setattr(item, "OclExpression76", self)
                    

class PrimitiveExp:

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


class TupleExp:

    pass
class TuplePart:

    pass
class CollectionExp:

    pass
class QualityMetamodel_QMM_OCL_SequenceExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_SetExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_BagExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_OrderedSetExp(CollectionExp):

    pass
class CollectionPart:

    pass
class QualityMetamodel_QMM_OCL_CollectionItem(CollectionPart):

    pass
class QualityMetamodel_QMM_OCL_CollectionRange(CollectionPart):

    pass
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


class QualityMetamodel_QMM_OCL_NumericExp(PrimitiveExp):

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


class IfExp:

    pass
class OclType:

    pass
class QualityMetamodel_QMM_OCL_MapType(OclType):

    pass
class QualityMetamodel_QMM_OCL_CollectionType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclModelElement(OclType):

    pass
class QualityMetamodel_QMM_OCL_Primitive(OclType):

    pass
class QualityMetamodel_QMM_OCL_TupleType(OclType):

    pass
class QualityMetamodel_QMM_OCL_EnvType(OclType):

    pass
class QualityMetamodel_QMM_OCL_LambdaType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclAnyType(OclType):

    pass
class OperatorCallExp:

    pass
class QualityMetamodel_QMM_OCL_RelOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_IntOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_NotOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_EqOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_AddOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_MulOpCallExp(OperatorCallExp):

    pass
class Attribute:

    pass
class Operation:

    pass
class LocalVariable:

    pass
class QualityMetamodel_QMM_OCL_TuplePart(LocalVariable):

    pass
class OperationCall:

    pass
class QualityMetamodel_QMM_OCL_CollectionOperationCall(OperationCall):

    pass
class LoopExp:

    pass
class QualityMetamodel_QMM_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp: "QualityMetamodel_QMM_OCL_OclExpression" = None, LoopExp117: "QualityMetamodel_QMM_OCL_Iterator" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QualityMetamodel_QMM_OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class PropertyCallExp:

    pass
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

class ModuleElement:

    pass
class QualityMetamodel_QMM_OCL_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, definition: "OclFeature" = None, definition166: "OclContextDefinition" = None, ModuleElement: "QualityMetamodel_QMM_OCL_Module" = None):
        self.static = static
        self.definition = definition
        self.definition166 = definition166
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def definition166(self):
        return self.__definition166

    @definition166.setter
    def definition166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeatureDefinition__definition166", None)
        self.__definition166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition167"):
                opp_val = getattr(old_value, "OclContextDefinition167", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition167"):
                opp_val = getattr(value, "OclContextDefinition167", None)
                setattr(value, "OclContextDefinition167", self)

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

class Import:

    pass
class OclMetamodel:

    pass
class NamedElement:

    pass
class QualityMetamodel_QMM_OCL_Import(NamedElement):

    pass
class QualityMetamodel_QMM_OCL_OclModel(NamedElement):

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
            if hasattr(old_value, "OclFeatureDefinition173"):
                opp_val = getattr(old_value, "OclFeatureDefinition173", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition173"):
                opp_val = getattr(value, "OclFeatureDefinition173", None)
                setattr(value, "OclFeatureDefinition173", self)

class QualityMetamodel_QMM_OCL_Module(NamedElement):

    pass
class LocatedElement:

    pass
class QualityMetamodel_QMM_OCL_PropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_MapElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_ModuleElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclExpression(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_CollectionPart(LocatedElement):

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
            if hasattr(old_value, "OclType151"):
                opp_val = getattr(old_value, "OclType151", None)
                if opp_val == self:
                    setattr(old_value, "OclType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType151"):
                opp_val = getattr(value, "OclType151", None)
                setattr(value, "OclType151", self)

class QualityMetamodel_QMM_OCL_StaticPropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclContextDefinition(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclType(LocatedElement):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType128: "MapType" = None, type130: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type136: "TupleTypeAttribute" = None, type138: "VariableDeclaration" = None, returnType141: "LambdaType" = None, argumentTypes: "LambdaType" = None, source145: "StaticPropertyCallExp" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType128 = valueType128
        self.type130 = type130
        self.keyType = keyType
        self.elementType = elementType
        self.type136 = type136
        self.type138 = type138
        self.returnType141 = returnType141
        self.argumentTypes = argumentTypes
        self.source145 = source145
        
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
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression124"):
                opp_val = getattr(old_value, "OclExpression124", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression124"):
                opp_val = getattr(value, "OclExpression124", None)
                setattr(value, "OclExpression124", self)

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
    def type130(self):
        return self.__type130

    @type130.setter
    def type130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type130", None)
        self.__type130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute131"):
                opp_val = getattr(old_value, "Attribute131", None)
                if opp_val == self:
                    setattr(old_value, "Attribute131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute131"):
                opp_val = getattr(value, "Attribute131", None)
                setattr(value, "Attribute131", self)

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
            if hasattr(old_value, "MapType133"):
                opp_val = getattr(old_value, "MapType133", None)
                if opp_val == self:
                    setattr(old_value, "MapType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType133"):
                opp_val = getattr(value, "MapType133", None)
                setattr(value, "MapType133", self)

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
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation126"):
                opp_val = getattr(old_value, "Operation126", None)
                if opp_val == self:
                    setattr(old_value, "Operation126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation126"):
                opp_val = getattr(value, "Operation126", None)
                setattr(value, "Operation126", self)

    @property
    def type136(self):
        return self.__type136

    @type136.setter
    def type136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__type136", None)
        self.__type136 = value
        
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
    def valueType128(self):
        return self.__valueType128

    @valueType128.setter
    def valueType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__valueType128", None)
        self.__valueType128 = value
        
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
    def argumentTypes(self):
        return self.__argumentTypes

    @argumentTypes.setter
    def argumentTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__argumentTypes", None)
        self.__argumentTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType143"):
                opp_val = getattr(old_value, "LambdaType143", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType143"):
                opp_val = getattr(value, "LambdaType143", None)
                setattr(value, "LambdaType143", self)

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
            if hasattr(old_value, "VariableDeclaration139"):
                opp_val = getattr(old_value, "VariableDeclaration139", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration139"):
                opp_val = getattr(value, "VariableDeclaration139", None)
                setattr(value, "VariableDeclaration139", self)

    @property
    def returnType141(self):
        return self.__returnType141

    @returnType141.setter
    def returnType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__returnType141", None)
        self.__returnType141 = value
        
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
    def source145(self):
        return self.__source145

    @source145.setter
    def source145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__source145", None)
        self.__source145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticPropertyCallExp146"):
                opp_val = getattr(old_value, "StaticPropertyCallExp146", None)
                if opp_val == self:
                    setattr(old_value, "StaticPropertyCallExp146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticPropertyCallExp146"):
                opp_val = getattr(value, "StaticPropertyCallExp146", None)
                setattr(value, "StaticPropertyCallExp146", self)

class QualityMetamodel_QMM_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, variableDeclaration: "OclType" = None, referredVariable: set["VariableExp"] = None):
        self.varName = varName
        self.variableDeclaration = variableDeclaration
        self.referredVariable = referredVariable if referredVariable is not None else set()
        
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
            if hasattr(old_value, "OclType109"):
                opp_val = getattr(old_value, "OclType109", None)
                if opp_val == self:
                    setattr(old_value, "OclType109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType109"):
                opp_val = getattr(value, "OclType109", None)
                setattr(value, "OclType109", self)

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
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column


    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line


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


class VariableDeclaration:

    pass
class QualityMetamodel_QMM_OCL_Iterator(VariableDeclaration):

    pass
class QualityMetamodel_QMM_OCL_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, variable: "LetExp" = None, initializedVariable: "OclExpression" = None, result: "IterateExp" = None, VariableDeclaration139: "QualityMetamodel_QMM_OCL_OclType" = None, VariableDeclaration: "QualityMetamodel_QMM_OCL_VariableExp" = None):
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
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp112"):
                opp_val = getattr(old_value, "LetExp112", None)
                if opp_val == self:
                    setattr(old_value, "LetExp112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp112"):
                opp_val = getattr(value, "LetExp112", None)
                setattr(value, "LetExp112", self)

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
            if hasattr(old_value, "OclExpression114"):
                opp_val = getattr(old_value, "OclExpression114", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression114"):
                opp_val = getattr(value, "OclExpression114", None)
                setattr(value, "OclExpression114", self)

class QualityMetamodel_QMM_OCL_Parameter(VariableDeclaration):

    pass
class QualityMetamodel_Value(VariableDeclaration):

    def __init__(self, description: str, val: "QualityMetamodel_ValueType" = None, Value: "QualityMetamodel_ValueType" = None, QualityMetamodel_Value20: "QualityMetamodel_Operation" = None, QualityMetamodel_Value: "QualityMetamodel_QualityModel" = None, QualityMetamodel_Value9: "QualityMetamodel_QualityAttribute" = None, VariableDeclaration139: "QualityMetamodel_QMM_OCL_OclType" = None, VariableDeclaration: "QualityMetamodel_QMM_OCL_VariableExp" = None):
        self.description = description
        self.val = val
        self.Value = Value
        self.QualityMetamodel_Value20 = QualityMetamodel_Value20
        self.QualityMetamodel_Value = QualityMetamodel_Value
        self.QualityMetamodel_Value9 = QualityMetamodel_Value9
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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


class QualityMetamodel_EnumerationMetric(ValueType):

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


class QualityMetamodel_AggregatedValueMetric(ValueType):

    def __init__(self, minimum: str, maximum: str, average: str, median: str, standardDeviation: str):
        self.minimum = minimum
        self.maximum = maximum
        self.average = average
        self.median = median
        self.standardDeviation = standardDeviation
        
        pass
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


    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum


    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum


    @property
    def standardDeviation(self):
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: str):
        self.__standardDeviation = standardDeviation


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


class OclExpression:

    pass
class QualityMetamodel_QMM_OCL_VariableExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_TupleExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OclUndefinedExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_IfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OclModelElementExp(OclExpression):

    def __init__(self, name: str, QualityMetamodel_QMM_OCL_OclModelElementExp: "OclModel" = None, OclExpression103: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression124: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression175: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression183: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression91: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression83: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression70: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression89: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression58: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression114: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression101: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression67: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression76: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression55: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression79: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None):
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
class QualityMetamodel_QMM_OCL_PrimitiveExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_SuperExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnvExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_CollectionExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression103: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression124: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression175: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression183: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression91: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression83: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression70: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression89: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression58: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression114: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression101: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression67: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression76: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression55: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression79: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QualityMetamodel_QMM_OCL_SelfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_LetExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_PropertyCallExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, QualityMetamodel_QMM_OCL_OperatorCallExp: "OclExpression" = None, appliedOperator: "OclExpression" = None, OclExpression103: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression124: "QualityMetamodel_QMM_OCL_OclType" = None, OclExpression175: "QualityMetamodel_QMM_OCL_Attribute" = None, OclExpression183: "QualityMetamodel_QMM_OCL_Operation" = None, OclExpression105: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression107: "QualityMetamodel_QMM_OCL_IfExp" = None, OclExpression93: "QualityMetamodel_QMM_OCL_LoopExp" = None, OclExpression87: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression91: "QualityMetamodel_QMM_OCL_BraceExp" = None, OclExpression83: "QualityMetamodel_QMM_OCL_OperationCall" = None, OclExpression60: "QualityMetamodel_QMM_OCL_CollectionItem" = None, OclExpression70: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression89: "QualityMetamodel_QMM_OCL_LambdaCallExp" = None, OclExpression58: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression114: "QualityMetamodel_QMM_OCL_LocalVariable" = None, OclExpression101: "QualityMetamodel_QMM_OCL_LetExp" = None, OclExpression67: "QualityMetamodel_QMM_OCL_MapElement" = None, OclExpression85: "QualityMetamodel_QMM_OCL_OperatorCallExp" = None, OclExpression: "QualityMetamodel_Operation" = None, OclExpression76: "QualityMetamodel_QMM_OCL_StaticOperationCall" = None, OclExpression55: "QualityMetamodel_QMM_OCL_CollectionRange" = None, OclExpression79: "QualityMetamodel_QMM_OCL_PropertyCallExp" = None):
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
            if hasattr(old_value, "OclExpression85"):
                opp_val = getattr(old_value, "OclExpression85", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression85"):
                opp_val = getattr(value, "OclExpression85", None)
                setattr(value, "OclExpression85", self)

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
            if hasattr(old_value, "OclExpression87"):
                opp_val = getattr(old_value, "OclExpression87", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression87"):
                opp_val = getattr(value, "OclExpression87", None)
                setattr(value, "OclExpression87", self)

class QualityMetamodel_QMM_OCL_BraceExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_StaticPropertyCallExp(OclExpression):

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
class QualityMetamodel_QualityAttribute(VariableDeclaration):

    pass
class QualityMetamodel_ValueType(VariableDeclaration):

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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