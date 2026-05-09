####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
QualityMetamodel_QualityModel = Class(name="QualityMetamodel_QualityModel")
Module = Class(name="Module")
QualityMetamodel_MetricProvider = Class(name="QualityMetamodel_MetricProvider")
QualityMetamodel_ValueType = Class(name="QualityMetamodel_ValueType", is_abstract=True)
QualityMetamodel_QualityAttribute = Class(name="QualityMetamodel_QualityAttribute")
QualityMetamodel_SingleValue = Class(name="QualityMetamodel_SingleValue")
Value = Class(name="Value")
QualityMetamodel_AggregatedValue = Class(name="QualityMetamodel_AggregatedValue")
QualityMetamodel_Operation = Class(name="QualityMetamodel_Operation")
OclExpression = Class(name="OclExpression")
QualityMetamodel_TextValueType = Class(name="QualityMetamodel_TextValueType")
ValueType = Class(name="ValueType")
QualityMetamodel_RangeValueType = Class(name="QualityMetamodel_RangeValueType")
QualityMetamodel_AggregatedValueMetric = Class(name="QualityMetamodel_AggregatedValueMetric")
QualityMetamodel_Value = Class(name="QualityMetamodel_Value", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
QualityMetamodel_RealValueType = Class(name="QualityMetamodel_RealValueType")
QualityMetamodel_BooleanValueType = Class(name="QualityMetamodel_BooleanValueType")
QualityMetamodel_IntegerValueType = Class(name="QualityMetamodel_IntegerValueType")
QualityMetamodel_QMM_OCL_LocatedElement = Class(name="QualityMetamodel_QMM_OCL_LocatedElement", is_abstract=True)
QualityMetamodel_QMM_OCL_NamedElement = Class(name="QualityMetamodel_QMM_OCL_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
QualityMetamodel_QMM_OCL_Module = Class(name="QualityMetamodel_QMM_OCL_Module")
NamedElement = Class(name="NamedElement")
OclMetamodel = Class(name="OclMetamodel")
Import = Class(name="Import")
ModuleElement = Class(name="ModuleElement")
QualityMetamodel_QMM_OCL_ModuleElement = Class(name="QualityMetamodel_QMM_OCL_ModuleElement", is_abstract=True)
QualityMetamodel_QMM_OCL_Import = Class(name="QualityMetamodel_QMM_OCL_Import")
QualityMetamodel_QMM_OCL_OclExpression = Class(name="QualityMetamodel_QMM_OCL_OclExpression", is_abstract=True)
QualityMetamodel_EnumerationMetric = Class(name="QualityMetamodel_EnumerationMetric")
QualityMetamodel_EnumerationItem = Class(name="QualityMetamodel_EnumerationItem")
PropertyCallExp = Class(name="PropertyCallExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCall = Class(name="OperationCall")
LocalVariable = Class(name="LocalVariable")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OperatorCallExp = Class(name="OperatorCallExp")
QualityMetamodel_QMM_OCL_VariableExp = Class(name="QualityMetamodel_QMM_OCL_VariableExp")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
QualityMetamodel_QMM_OCL_BooleanExp = Class(name="QualityMetamodel_QMM_OCL_BooleanExp")
QualityMetamodel_QMM_OCL_NumericExp = Class(name="QualityMetamodel_QMM_OCL_NumericExp", is_abstract=True)
QualityMetamodel_QMM_OCL_RealExp = Class(name="QualityMetamodel_QMM_OCL_RealExp")
NumericExp = Class(name="NumericExp")
QualityMetamodel_QMM_OCL_IntegerExp = Class(name="QualityMetamodel_QMM_OCL_IntegerExp")
QualityMetamodel_QMM_OCL_CollectionExp = Class(name="QualityMetamodel_QMM_OCL_CollectionExp", is_abstract=True)
CollectionPart = Class(name="CollectionPart")
QualityMetamodel_QMM_OCL_CollectionPart = Class(name="QualityMetamodel_QMM_OCL_CollectionPart", is_abstract=True)
CollectionExp = Class(name="CollectionExp")
QualityMetamodel_QMM_OCL_CollectionRange = Class(name="QualityMetamodel_QMM_OCL_CollectionRange")
QualityMetamodel_QMM_OCL_CollectionItem = Class(name="QualityMetamodel_QMM_OCL_CollectionItem")
QualityMetamodel_QMM_OCL_BagExp = Class(name="QualityMetamodel_QMM_OCL_BagExp")
QualityMetamodel_QMM_OCL_OrderedSetExp = Class(name="QualityMetamodel_QMM_OCL_OrderedSetExp")
QualityMetamodel_QMM_OCL_SequenceExp = Class(name="QualityMetamodel_QMM_OCL_SequenceExp")
QualityMetamodel_QMM_OCL_SetExp = Class(name="QualityMetamodel_QMM_OCL_SetExp")
QualityMetamodel_QMM_OCL_TupleExp = Class(name="QualityMetamodel_QMM_OCL_TupleExp")
TuplePart = Class(name="TuplePart")
QualityMetamodel_QMM_OCL_TuplePart = Class(name="QualityMetamodel_QMM_OCL_TuplePart")
TupleExp = Class(name="TupleExp")
QualityMetamodel_QMM_OCL_SuperExp = Class(name="QualityMetamodel_QMM_OCL_SuperExp")
QualityMetamodel_QMM_OCL_SelfExp = Class(name="QualityMetamodel_QMM_OCL_SelfExp")
QualityMetamodel_QMM_OCL_EnvExp = Class(name="QualityMetamodel_QMM_OCL_EnvExp")
QualityMetamodel_QMM_OCL_PrimitiveExp = Class(name="QualityMetamodel_QMM_OCL_PrimitiveExp", is_abstract=True)
QualityMetamodel_QMM_OCL_StringExp = Class(name="QualityMetamodel_QMM_OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
QualityMetamodel_QMM_OCL_EnumLiteralExp = Class(name="QualityMetamodel_QMM_OCL_EnumLiteralExp")
QualityMetamodel_QMM_OCL_OclUndefinedExp = Class(name="QualityMetamodel_QMM_OCL_OclUndefinedExp")
QualityMetamodel_QMM_OCL_StaticPropertyCallExp = Class(name="QualityMetamodel_QMM_OCL_StaticPropertyCallExp")
StaticPropertyCall = Class(name="StaticPropertyCall")
QualityMetamodel_QMM_OCL_StaticPropertyCall = Class(name="QualityMetamodel_QMM_OCL_StaticPropertyCall", is_abstract=True)
StaticPropertyCallExp = Class(name="StaticPropertyCallExp")
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall = Class(name="QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_StaticOperationCall = Class(name="QualityMetamodel_QMM_OCL_StaticOperationCall")
QualityMetamodel_QMM_OCL_PropertyCallExp = Class(name="QualityMetamodel_QMM_OCL_PropertyCallExp")
PropertyCall = Class(name="PropertyCall")
QualityMetamodel_QMM_OCL_PropertyCall = Class(name="QualityMetamodel_QMM_OCL_PropertyCall", is_abstract=True)
QualityMetamodel_QMM_OCL_MapExp = Class(name="QualityMetamodel_QMM_OCL_MapExp")
MapElement = Class(name="MapElement")
QualityMetamodel_QMM_OCL_MapElement = Class(name="QualityMetamodel_QMM_OCL_MapElement")
MapExp = Class(name="MapExp")
QualityMetamodel_QMM_OCL_OperatorCallExp = Class(name="QualityMetamodel_QMM_OCL_OperatorCallExp")
QualityMetamodel_QMM_OCL_NotOpCallExp = Class(name="QualityMetamodel_QMM_OCL_NotOpCallExp")
QualityMetamodel_QMM_OCL_RelOpCallExp = Class(name="QualityMetamodel_QMM_OCL_RelOpCallExp")
QualityMetamodel_QMM_OCL_EqOpCallExp = Class(name="QualityMetamodel_QMM_OCL_EqOpCallExp")
QualityMetamodel_QMM_OCL_AddOpCallExp = Class(name="QualityMetamodel_QMM_OCL_AddOpCallExp")
QualityMetamodel_QMM_OCL_IntOpCallExp = Class(name="QualityMetamodel_QMM_OCL_IntOpCallExp")
QualityMetamodel_QMM_OCL_MulOpCallExp = Class(name="QualityMetamodel_QMM_OCL_MulOpCallExp")
QualityMetamodel_QMM_OCL_LambdaCallExp = Class(name="QualityMetamodel_QMM_OCL_LambdaCallExp")
VariableExp = Class(name="VariableExp")
QualityMetamodel_QMM_OCL_BraceExp = Class(name="QualityMetamodel_QMM_OCL_BraceExp")
QualityMetamodel_QMM_OCL_CollectionOperationCall = Class(name="QualityMetamodel_QMM_OCL_CollectionOperationCall")
QualityMetamodel_QMM_OCL_LoopExp = Class(name="QualityMetamodel_QMM_OCL_LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
QualityMetamodel_QMM_OCL_IterateExp = Class(name="QualityMetamodel_QMM_OCL_IterateExp")
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall = Class(name="QualityMetamodel_QMM_OCL_NavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_OperationCall = Class(name="QualityMetamodel_QMM_OCL_OperationCall")
QualityMetamodel_QMM_OCL_IfExp = Class(name="QualityMetamodel_QMM_OCL_IfExp")
QualityMetamodel_QMM_OCL_VariableDeclaration = Class(name="QualityMetamodel_QMM_OCL_VariableDeclaration", is_abstract=True)
QualityMetamodel_QMM_OCL_LocalVariable = Class(name="QualityMetamodel_QMM_OCL_LocalVariable")
IterateExp = Class(name="IterateExp")
QualityMetamodel_QMM_OCL_Iterator = Class(name="QualityMetamodel_QMM_OCL_Iterator")
QualityMetamodel_QMM_OCL_Parameter = Class(name="QualityMetamodel_QMM_OCL_Parameter")
QualityMetamodel_QMM_OCL_IteratorExp = Class(name="QualityMetamodel_QMM_OCL_IteratorExp")
QualityMetamodel_QMM_OCL_LetExp = Class(name="QualityMetamodel_QMM_OCL_LetExp")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
LambdaType = Class(name="LambdaType")
QualityMetamodel_QMM_OCL_OclModelElementExp = Class(name="QualityMetamodel_QMM_OCL_OclModelElementExp")
OclModel = Class(name="OclModel")
QualityMetamodel_QMM_OCL_Primitive = Class(name="QualityMetamodel_QMM_OCL_Primitive", is_abstract=True)
QualityMetamodel_QMM_OCL_StringType = Class(name="QualityMetamodel_QMM_OCL_StringType")
Primitive = Class(name="Primitive")
QualityMetamodel_QMM_OCL_BooleanType = Class(name="QualityMetamodel_QMM_OCL_BooleanType")
QualityMetamodel_QMM_OCL_NumericType = Class(name="QualityMetamodel_QMM_OCL_NumericType", is_abstract=True)
QualityMetamodel_QMM_OCL_CollectionType = Class(name="QualityMetamodel_QMM_OCL_CollectionType")
QualityMetamodel_QMM_OCL_OclType = Class(name="QualityMetamodel_QMM_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
QualityMetamodel_QMM_OCL_TupleTypeAttribute = Class(name="QualityMetamodel_QMM_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
QualityMetamodel_QMM_OCL_OclModelElement = Class(name="QualityMetamodel_QMM_OCL_OclModelElement")
QualityMetamodel_QMM_OCL_IntegerType = Class(name="QualityMetamodel_QMM_OCL_IntegerType")
NumericType = Class(name="NumericType")
QualityMetamodel_QMM_OCL_MapType = Class(name="QualityMetamodel_QMM_OCL_MapType")
QualityMetamodel_QMM_OCL_RealType = Class(name="QualityMetamodel_QMM_OCL_RealType")
QualityMetamodel_QMM_OCL_BagType = Class(name="QualityMetamodel_QMM_OCL_BagType")
QualityMetamodel_QMM_OCL_OrderedSetType = Class(name="QualityMetamodel_QMM_OCL_OrderedSetType")
QualityMetamodel_QMM_OCL_SequenceType = Class(name="QualityMetamodel_QMM_OCL_SequenceType")
QualityMetamodel_QMM_OCL_SetType = Class(name="QualityMetamodel_QMM_OCL_SetType")
QualityMetamodel_QMM_OCL_OclAnyType = Class(name="QualityMetamodel_QMM_OCL_OclAnyType")
QualityMetamodel_QMM_OCL_TupleType = Class(name="QualityMetamodel_QMM_OCL_TupleType")
QualityMetamodel_QMM_OCL_LambdaType = Class(name="QualityMetamodel_QMM_OCL_LambdaType")
QualityMetamodel_QMM_OCL_EnvType = Class(name="QualityMetamodel_QMM_OCL_EnvType")
QualityMetamodel_QMM_OCL_OclFeatureDefinition = Class(name="QualityMetamodel_QMM_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
QualityMetamodel_QMM_OCL_OclContextDefinition = Class(name="QualityMetamodel_QMM_OCL_OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
QualityMetamodel_QMM_OCL_OclFeature = Class(name="QualityMetamodel_QMM_OCL_OclFeature", is_abstract=True)
QualityMetamodel_QMM_OCL_Attribute = Class(name="QualityMetamodel_QMM_OCL_Attribute")
QualityMetamodel_QMM_OCL_Operation = Class(name="QualityMetamodel_QMM_OCL_Operation")
QualityMetamodel_QMM_OCL_OclModel = Class(name="QualityMetamodel_QMM_OCL_OclModel", is_abstract=True)
OclModelElement = Class(name="OclModelElement")
QualityMetamodel_QMM_OCL_OclMetamodel = Class(name="QualityMetamodel_QMM_OCL_OclMetamodel")
OclInstanceModel = Class(name="OclInstanceModel")
QualityMetamodel_QMM_OCL_OclInstanceModel = Class(name="QualityMetamodel_QMM_OCL_OclInstanceModel")
Parameter_ = Class(name="Parameter")

# QualityMetamodel_QualityModel class attributes and methods

# Module class attributes and methods

# QualityMetamodel_MetricProvider class attributes and methods
QualityMetamodel_MetricProvider_name: Property = Property(name="name", type=StringType)
QualityMetamodel_MetricProvider_description: Property = Property(name="description", type=StringType)
QualityMetamodel_MetricProvider_id: Property = Property(name="id", type=StringType)
QualityMetamodel_MetricProvider.attributes={QualityMetamodel_MetricProvider_name, QualityMetamodel_MetricProvider_id, QualityMetamodel_MetricProvider_description}

# QualityMetamodel_ValueType class attributes and methods

# QualityMetamodel_QualityAttribute class attributes and methods

# QualityMetamodel_SingleValue class attributes and methods

# Value class attributes and methods

# QualityMetamodel_AggregatedValue class attributes and methods

# QualityMetamodel_Operation class attributes and methods
QualityMetamodel_Operation_name: Property = Property(name="name", type=StringType)
QualityMetamodel_Operation_body: Property = Property(name="body", type=StringType)
QualityMetamodel_Operation.attributes={QualityMetamodel_Operation_name, QualityMetamodel_Operation_body}

# OclExpression class attributes and methods

# QualityMetamodel_TextValueType class attributes and methods
QualityMetamodel_TextValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_TextValueType.attributes={QualityMetamodel_TextValueType_value}

# ValueType class attributes and methods

# QualityMetamodel_RangeValueType class attributes and methods
QualityMetamodel_RangeValueType_min: Property = Property(name="min", type=StringType)
QualityMetamodel_RangeValueType_max: Property = Property(name="max", type=StringType)
QualityMetamodel_RangeValueType.attributes={QualityMetamodel_RangeValueType_min, QualityMetamodel_RangeValueType_max}

# QualityMetamodel_AggregatedValueMetric class attributes and methods
QualityMetamodel_AggregatedValueMetric_minimum: Property = Property(name="minimum", type=StringType)
QualityMetamodel_AggregatedValueMetric_maximum: Property = Property(name="maximum", type=StringType)
QualityMetamodel_AggregatedValueMetric_average: Property = Property(name="average", type=StringType)
QualityMetamodel_AggregatedValueMetric_median: Property = Property(name="median", type=StringType)
QualityMetamodel_AggregatedValueMetric_standardDeviation: Property = Property(name="standardDeviation", type=StringType)
QualityMetamodel_AggregatedValueMetric.attributes={QualityMetamodel_AggregatedValueMetric_average, QualityMetamodel_AggregatedValueMetric_minimum, QualityMetamodel_AggregatedValueMetric_standardDeviation, QualityMetamodel_AggregatedValueMetric_maximum, QualityMetamodel_AggregatedValueMetric_median}

# QualityMetamodel_Value class attributes and methods
QualityMetamodel_Value_description: Property = Property(name="description", type=StringType)
QualityMetamodel_Value.attributes={QualityMetamodel_Value_description}

# VariableDeclaration class attributes and methods

# QualityMetamodel_RealValueType class attributes and methods
QualityMetamodel_RealValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_RealValueType.attributes={QualityMetamodel_RealValueType_value}

# QualityMetamodel_BooleanValueType class attributes and methods
QualityMetamodel_BooleanValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_BooleanValueType.attributes={QualityMetamodel_BooleanValueType_value}

# QualityMetamodel_IntegerValueType class attributes and methods
QualityMetamodel_IntegerValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_IntegerValueType.attributes={QualityMetamodel_IntegerValueType_value}

# QualityMetamodel_QMM_OCL_LocatedElement class attributes and methods
QualityMetamodel_QMM_OCL_LocatedElement_line: Property = Property(name="line", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_column: Property = Property(name="column", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement.attributes={QualityMetamodel_QMM_OCL_LocatedElement_charStart, QualityMetamodel_QMM_OCL_LocatedElement_charEnd, QualityMetamodel_QMM_OCL_LocatedElement_line, QualityMetamodel_QMM_OCL_LocatedElement_column}

# QualityMetamodel_QMM_OCL_NamedElement class attributes and methods
QualityMetamodel_QMM_OCL_NamedElement_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_NamedElement.attributes={QualityMetamodel_QMM_OCL_NamedElement_name}

# LocatedElement class attributes and methods

# QualityMetamodel_QMM_OCL_Module class attributes and methods

# NamedElement class attributes and methods

# OclMetamodel class attributes and methods

# Import class attributes and methods

# ModuleElement class attributes and methods

# QualityMetamodel_QMM_OCL_ModuleElement class attributes and methods

# QualityMetamodel_QMM_OCL_Import class attributes and methods

# QualityMetamodel_QMM_OCL_OclExpression class attributes and methods

# QualityMetamodel_EnumerationMetric class attributes and methods

# QualityMetamodel_EnumerationItem class attributes and methods
QualityMetamodel_EnumerationItem_name: Property = Property(name="name", type=StringType)
QualityMetamodel_EnumerationItem.attributes={QualityMetamodel_EnumerationItem_name}

# PropertyCallExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCall class attributes and methods

# LocalVariable class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OperatorCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_VariableExp class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# QualityMetamodel_QMM_OCL_BooleanExp class attributes and methods
QualityMetamodel_QMM_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
QualityMetamodel_QMM_OCL_BooleanExp.attributes={QualityMetamodel_QMM_OCL_BooleanExp_booleanSymbol}

# QualityMetamodel_QMM_OCL_NumericExp class attributes and methods

# QualityMetamodel_QMM_OCL_RealExp class attributes and methods
QualityMetamodel_QMM_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
QualityMetamodel_QMM_OCL_RealExp.attributes={QualityMetamodel_QMM_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# QualityMetamodel_QMM_OCL_IntegerExp class attributes and methods
QualityMetamodel_QMM_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
QualityMetamodel_QMM_OCL_IntegerExp.attributes={QualityMetamodel_QMM_OCL_IntegerExp_integerSymbol}

# QualityMetamodel_QMM_OCL_CollectionExp class attributes and methods

# CollectionPart class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionPart class attributes and methods

# CollectionExp class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionRange class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionItem class attributes and methods

# QualityMetamodel_QMM_OCL_BagExp class attributes and methods

# QualityMetamodel_QMM_OCL_OrderedSetExp class attributes and methods

# QualityMetamodel_QMM_OCL_SequenceExp class attributes and methods

# QualityMetamodel_QMM_OCL_SetExp class attributes and methods

# QualityMetamodel_QMM_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# QualityMetamodel_QMM_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# QualityMetamodel_QMM_OCL_SuperExp class attributes and methods

# QualityMetamodel_QMM_OCL_SelfExp class attributes and methods

# QualityMetamodel_QMM_OCL_EnvExp class attributes and methods

# QualityMetamodel_QMM_OCL_PrimitiveExp class attributes and methods

# QualityMetamodel_QMM_OCL_StringExp class attributes and methods
QualityMetamodel_QMM_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
QualityMetamodel_QMM_OCL_StringExp.attributes={QualityMetamodel_QMM_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# QualityMetamodel_QMM_OCL_EnumLiteralExp class attributes and methods
QualityMetamodel_QMM_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_EnumLiteralExp.attributes={QualityMetamodel_QMM_OCL_EnumLiteralExp_name}

# QualityMetamodel_QMM_OCL_OclUndefinedExp class attributes and methods

# QualityMetamodel_QMM_OCL_StaticPropertyCallExp class attributes and methods

# StaticPropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_StaticPropertyCall class attributes and methods

# StaticPropertyCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall class attributes and methods
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall.attributes={QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_name}

# QualityMetamodel_QMM_OCL_StaticOperationCall class attributes and methods
QualityMetamodel_QMM_OCL_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_StaticOperationCall.attributes={QualityMetamodel_QMM_OCL_StaticOperationCall_operationName}

# QualityMetamodel_QMM_OCL_PropertyCallExp class attributes and methods

# PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# QualityMetamodel_QMM_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# QualityMetamodel_QMM_OCL_OperatorCallExp class attributes and methods
QualityMetamodel_QMM_OCL_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperatorCallExp.attributes={QualityMetamodel_QMM_OCL_OperatorCallExp_operationName}

# QualityMetamodel_QMM_OCL_NotOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_RelOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_EqOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_AddOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_IntOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_MulOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# QualityMetamodel_QMM_OCL_BraceExp class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionOperationCall class attributes and methods

# QualityMetamodel_QMM_OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# QualityMetamodel_QMM_OCL_IterateExp class attributes and methods

# QualityMetamodel_QMM_OCL_NavigationOrAttributeCall class attributes and methods
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.attributes={QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name}

# QualityMetamodel_QMM_OCL_OperationCall class attributes and methods
QualityMetamodel_QMM_OCL_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperationCall.attributes={QualityMetamodel_QMM_OCL_OperationCall_operationName}

# QualityMetamodel_QMM_OCL_IfExp class attributes and methods

# QualityMetamodel_QMM_OCL_VariableDeclaration class attributes and methods
QualityMetamodel_QMM_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
QualityMetamodel_QMM_OCL_VariableDeclaration.attributes={QualityMetamodel_QMM_OCL_VariableDeclaration_varName}

# QualityMetamodel_QMM_OCL_LocalVariable class attributes and methods
QualityMetamodel_QMM_OCL_LocalVariable_eq: Property = Property(name="eq", type=StringType)
QualityMetamodel_QMM_OCL_LocalVariable.attributes={QualityMetamodel_QMM_OCL_LocalVariable_eq}

# IterateExp class attributes and methods

# QualityMetamodel_QMM_OCL_Iterator class attributes and methods

# QualityMetamodel_QMM_OCL_Parameter class attributes and methods

# QualityMetamodel_QMM_OCL_IteratorExp class attributes and methods
QualityMetamodel_QMM_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_IteratorExp.attributes={QualityMetamodel_QMM_OCL_IteratorExp_name}

# QualityMetamodel_QMM_OCL_LetExp class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# LambdaType class attributes and methods

# QualityMetamodel_QMM_OCL_OclModelElementExp class attributes and methods
QualityMetamodel_QMM_OCL_OclModelElementExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclModelElementExp.attributes={QualityMetamodel_QMM_OCL_OclModelElementExp_name}

# OclModel class attributes and methods

# QualityMetamodel_QMM_OCL_Primitive class attributes and methods

# QualityMetamodel_QMM_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# QualityMetamodel_QMM_OCL_BooleanType class attributes and methods

# QualityMetamodel_QMM_OCL_NumericType class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionType class attributes and methods

# QualityMetamodel_QMM_OCL_OclType class attributes and methods
QualityMetamodel_QMM_OCL_OclType_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclType.attributes={QualityMetamodel_QMM_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# QualityMetamodel_QMM_OCL_TupleTypeAttribute class attributes and methods
QualityMetamodel_QMM_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_TupleTypeAttribute.attributes={QualityMetamodel_QMM_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# QualityMetamodel_QMM_OCL_OclModelElement class attributes and methods

# QualityMetamodel_QMM_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# QualityMetamodel_QMM_OCL_MapType class attributes and methods

# QualityMetamodel_QMM_OCL_RealType class attributes and methods

# QualityMetamodel_QMM_OCL_BagType class attributes and methods

# QualityMetamodel_QMM_OCL_OrderedSetType class attributes and methods

# QualityMetamodel_QMM_OCL_SequenceType class attributes and methods

# QualityMetamodel_QMM_OCL_SetType class attributes and methods

# QualityMetamodel_QMM_OCL_OclAnyType class attributes and methods

# QualityMetamodel_QMM_OCL_TupleType class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaType class attributes and methods

# QualityMetamodel_QMM_OCL_EnvType class attributes and methods

# QualityMetamodel_QMM_OCL_OclFeatureDefinition class attributes and methods
QualityMetamodel_QMM_OCL_OclFeatureDefinition_static: Property = Property(name="static", type=StringType)
QualityMetamodel_QMM_OCL_OclFeatureDefinition.attributes={QualityMetamodel_QMM_OCL_OclFeatureDefinition_static}

# OclFeature class attributes and methods

# QualityMetamodel_QMM_OCL_OclContextDefinition class attributes and methods

# OclFeatureDefinition class attributes and methods

# QualityMetamodel_QMM_OCL_OclFeature class attributes and methods
QualityMetamodel_QMM_OCL_OclFeature_eq: Property = Property(name="eq", type=StringType)
QualityMetamodel_QMM_OCL_OclFeature.attributes={QualityMetamodel_QMM_OCL_OclFeature_eq}

# QualityMetamodel_QMM_OCL_Attribute class attributes and methods

# QualityMetamodel_QMM_OCL_Operation class attributes and methods

# QualityMetamodel_QMM_OCL_OclModel class attributes and methods

# OclModelElement class attributes and methods

# QualityMetamodel_QMM_OCL_OclMetamodel class attributes and methods
QualityMetamodel_QMM_OCL_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
QualityMetamodel_QMM_OCL_OclMetamodel.attributes={QualityMetamodel_QMM_OCL_OclMetamodel_uri}

# OclInstanceModel class attributes and methods

# QualityMetamodel_QMM_OCL_OclInstanceModel class attributes and methods

# Parameter class attributes and methods

# Relationships
metricProviders0: BinaryAssociation = BinaryAssociation(
    name="metricProviders0",
    ends={
        Property(name="QualityMetamodel_MetricProvider", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel", type=QualityMetamodel_MetricProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityTypes1: BinaryAssociation = BinaryAssociation(
    name="qualityTypes1",
    ends={
        Property(name="QualityMetamodel_ValueType", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel2", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityAttributes3: BinaryAssociation = BinaryAssociation(
    name="qualityAttributes3",
    ends={
        Property(name="QualityMetamodel_QualityAttribute", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel4", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueType13: BinaryAssociation = BinaryAssociation(
    name="valueType13",
    ends={
        Property(name="ValueType", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="val", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(1, 1))
    }
)
val14: BinaryAssociation = BinaryAssociation(
    name="val14",
    ends={
        Property(name="Value", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1))
    }
)
measuredBy15: BinaryAssociation = BinaryAssociation(
    name="measuredBy15",
    ends={
        Property(name="QualityMetamodel_MetricProvider16", type=QualityMetamodel_SingleValue, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_SingleValue", type=QualityMetamodel_MetricProvider, multiplicity=Multiplicity(1, 1))
    }
)
calculatedBy17: BinaryAssociation = BinaryAssociation(
    name="calculatedBy17",
    ends={
        Property(name="QualityMetamodel_Operation", type=QualityMetamodel_AggregatedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_AggregatedValue", type=QualityMetamodel_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aggregatedValues18: BinaryAssociation = BinaryAssociation(
    name="aggregatedValues18",
    ends={
        Property(name="QualityMetamodel_Value20", type=QualityMetamodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_Operation19", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 9999))
    }
)
ref21: BinaryAssociation = BinaryAssociation(
    name="ref21",
    ends={
        Property(name="OclExpression", type=QualityMetamodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_Operation22", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualityValues5: BinaryAssociation = BinaryAssociation(
    name="qualityValues5",
    ends={
        Property(name="QualityMetamodel_Value", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel6", type=QualityMetamodel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="QualityMetamodel_Value9", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityAttribute8", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1))
    }
)
qualityAttributes11: BinaryAssociation = BinaryAssociation(
    name="qualityAttributes11",
    ends={
        Property(name="QualityMetamodel_QualityAttribute12", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityAttribute10", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
metamodels27: BinaryAssociation = BinaryAssociation(
    name="metamodels27",
    ends={
        Property(name="OclMetamodel", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_Module", type=OclMetamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports28: BinaryAssociation = BinaryAssociation(
    name="imports28",
    ends={
        Property(name="Import", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements29: BinaryAssociation = BinaryAssociation(
    name="elements29",
    ends={
        Property(name="ModuleElement", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module30", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module31: BinaryAssociation = BinaryAssociation(
    name="module31",
    ends={
        Property(name="Module", type=QualityMetamodel_QMM_OCL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module32: BinaryAssociation = BinaryAssociation(
    name="module32",
    ends={
        Property(name="Module33", type=QualityMetamodel_QMM_OCL_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="imports", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
set23: BinaryAssociation = BinaryAssociation(
    name="set23",
    ends={
        Property(name="QualityMetamodel_EnumerationItem", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="QualityMetamodel_EnumerationItem26", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric25", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty36: BinaryAssociation = BinaryAssociation(
    name="appliedProperty36",
    ends={
        Property(name="PropertyCallExp", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp37: BinaryAssociation = BinaryAssociation(
    name="letExp37",
    ends={
        Property(name="LetExp", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp38: BinaryAssociation = BinaryAssociation(
    name="loopExp38",
    ends={
        Property(name="LoopExp", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation39: BinaryAssociation = BinaryAssociation(
    name="parentOperation39",
    ends={
        Property(name="OperationCall", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable40: BinaryAssociation = BinaryAssociation(
    name="initializedVariable40",
    ends={
        Property(name="LocalVariable", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp241: BinaryAssociation = BinaryAssociation(
    name="ifExp241",
    ends={
        Property(name="IfExp42", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation43: BinaryAssociation = BinaryAssociation(
    name="owningOperation43",
    ends={
        Property(name="Operation", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body44", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp145: BinaryAssociation = BinaryAssociation(
    name="ifExp145",
    ends={
        Property(name="IfExp46", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute47: BinaryAssociation = BinaryAssociation(
    name="owningAttribute47",
    ends={
        Property(name="Attribute", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression48", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
appliedOperator49: BinaryAssociation = BinaryAssociation(
    name="appliedOperator49",
    ends={
        Property(name="OperatorCallExp", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source50", type=OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable51: BinaryAssociation = BinaryAssociation(
    name="referredVariable51",
    ends={
        Property(name="VariableDeclaration", type=QualityMetamodel_QMM_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="OclType", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp335: BinaryAssociation = BinaryAssociation(
    name="ifExp335",
    ends={
        Property(name="IfExp", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
parts52: BinaryAssociation = BinaryAssociation(
    name="parts52",
    ends={
        Property(name="CollectionPart", type=QualityMetamodel_QMM_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=CollectionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection53: BinaryAssociation = BinaryAssociation(
    name="collection53",
    ends={
        Property(name="CollectionExp", type=QualityMetamodel_QMM_OCL_CollectionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
first54: BinaryAssociation = BinaryAssociation(
    name="first54",
    ends={
        Property(name="OclExpression55", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last56: BinaryAssociation = BinaryAssociation(
    name="last56",
    ends={
        Property(name="OclExpression58", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange57", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item59: BinaryAssociation = BinaryAssociation(
    name="item59",
    ends={
        Property(name="OclExpression60", type=QualityMetamodel_QMM_OCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuplePart61: BinaryAssociation = BinaryAssociation(
    name="tuplePart61",
    ends={
        Property(name="TuplePart", type=QualityMetamodel_QMM_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple62: BinaryAssociation = BinaryAssociation(
    name="tuple62",
    ends={
        Property(name="TupleExp", type=QualityMetamodel_QMM_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
value68: BinaryAssociation = BinaryAssociation(
    name="value68",
    ends={
        Property(name="OclExpression70", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement69", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source71: BinaryAssociation = BinaryAssociation(
    name="source71",
    ends={
        Property(name="OclType72", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticPropertyCall", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall73: BinaryAssociation = BinaryAssociation(
    name="staticCall73",
    ends={
        Property(name="StaticPropertyCall", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCallExp", type=StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp74: BinaryAssociation = BinaryAssociation(
    name="staticCallExp74",
    ends={
        Property(name="StaticPropertyCallExp", type=QualityMetamodel_QMM_OCL_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCall", type=StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments75: BinaryAssociation = BinaryAssociation(
    name="arguments75",
    ends={
        Property(name="OclExpression76", type=QualityMetamodel_QMM_OCL_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_StaticOperationCall", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls77: BinaryAssociation = BinaryAssociation(
    name="calls77",
    ends={
        Property(name="PropertyCall", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="callExp", type=PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source78: BinaryAssociation = BinaryAssociation(
    name="source78",
    ends={
        Property(name="OclExpression79", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callExp80: BinaryAssociation = BinaryAssociation(
    name="callExp80",
    ends={
        Property(name="PropertyCallExp81", type=QualityMetamodel_QMM_OCL_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="calls", type=PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
elements63: BinaryAssociation = BinaryAssociation(
    name="elements63",
    ends={
        Property(name="MapElement", type=QualityMetamodel_QMM_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map64: BinaryAssociation = BinaryAssociation(
    name="map64",
    ends={
        Property(name="MapExp", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements65", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key66: BinaryAssociation = BinaryAssociation(
    name="key66",
    ends={
        Property(name="OclExpression67", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument84: BinaryAssociation = BinaryAssociation(
    name="argument84",
    ends={
        Property(name="OclExpression85", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source86: BinaryAssociation = BinaryAssociation(
    name="source86",
    ends={
        Property(name="OclExpression87", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedOperator", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments88: BinaryAssociation = BinaryAssociation(
    name="arguments88",
    ends={
        Property(name="OclExpression89", type=QualityMetamodel_QMM_OCL_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_LambdaCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp90: BinaryAssociation = BinaryAssociation(
    name="exp90",
    ends={
        Property(name="OclExpression91", type=QualityMetamodel_QMM_OCL_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_BraceExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="OclExpression93", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators94: BinaryAssociation = BinaryAssociation(
    name="iterators94",
    ends={
        Property(name="Iterator", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result95: BinaryAssociation = BinaryAssociation(
    name="result95",
    ends={
        Property(name="LocalVariable96", type=QualityMetamodel_QMM_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments82: BinaryAssociation = BinaryAssociation(
    name="arguments82",
    ends={
        Property(name="OclExpression83", type=QualityMetamodel_QMM_OCL_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenExpression102: BinaryAssociation = BinaryAssociation(
    name="thenExpression102",
    ends={
        Property(name="OclExpression103", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition104: BinaryAssociation = BinaryAssociation(
    name="condition104",
    ends={
        Property(name="OclExpression105", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression106: BinaryAssociation = BinaryAssociation(
    name="elseExpression106",
    ends={
        Property(name="OclExpression107", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type108: BinaryAssociation = BinaryAssociation(
    name="type108",
    ends={
        Property(name="OclType109", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp110: BinaryAssociation = BinaryAssociation(
    name="variableExp110",
    ends={
        Property(name="VariableExp", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp111: BinaryAssociation = BinaryAssociation(
    name="letExp111",
    ends={
        Property(name="LetExp112", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression113: BinaryAssociation = BinaryAssociation(
    name="initExpression113",
    ends={
        Property(name="OclExpression114", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp115: BinaryAssociation = BinaryAssociation(
    name="baseExp115",
    ends={
        Property(name="IterateExp", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr116: BinaryAssociation = BinaryAssociation(
    name="loopExpr116",
    ends={
        Property(name="LoopExp117", type=QualityMetamodel_QMM_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation118: BinaryAssociation = BinaryAssociation(
    name="operation118",
    ends={
        Property(name="Operation119", type=QualityMetamodel_QMM_OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
variable97: BinaryAssociation = BinaryAssociation(
    name="variable97",
    ends={
        Property(name="LocalVariable98", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_99: BinaryAssociation = BinaryAssociation(
    name="in_99",
    ends={
        Property(name="OclExpression101", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp100", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions122: BinaryAssociation = BinaryAssociation(
    name="definitions122",
    ends={
        Property(name="OclContextDefinition", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression123: BinaryAssociation = BinaryAssociation(
    name="oclExpression123",
    ends={
        Property(name="OclExpression124", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation125: BinaryAssociation = BinaryAssociation(
    name="operation125",
    ends={
        Property(name="Operation126", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2127: BinaryAssociation = BinaryAssociation(
    name="mapType2127",
    ends={
        Property(name="MapType", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType128", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute129: BinaryAssociation = BinaryAssociation(
    name="attribute129",
    ends={
        Property(name="Attribute131", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type130", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType132: BinaryAssociation = BinaryAssociation(
    name="mapType132",
    ends={
        Property(name="MapType133", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes134: BinaryAssociation = BinaryAssociation(
    name="collectionTypes134",
    ends={
        Property(name="CollectionType", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute135: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute135",
    ends={
        Property(name="TupleTypeAttribute", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type136", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration137: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration137",
    ends={
        Property(name="VariableDeclaration139", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type138", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lambdaReturnType140: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType140",
    ends={
        Property(name="LambdaType", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType141", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
lambdaArgType142: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType142",
    ends={
        Property(name="LambdaType143", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="argumentTypes", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
staticPropertyCall144: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall144",
    ends={
        Property(name="StaticPropertyCallExp146", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="source145", type=StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
model147: BinaryAssociation = BinaryAssociation(
    name="model147",
    ends={
        Property(name="OclModel", type=QualityMetamodel_QMM_OCL_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OclModelElementExp", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elementType120: BinaryAssociation = BinaryAssociation(
    name="elementType120",
    ends={
        Property(name="OclType121", type=QualityMetamodel_QMM_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes148: BinaryAssociation = BinaryAssociation(
    name="attributes148",
    ends={
        Property(name="TupleTypeAttribute149", type=QualityMetamodel_QMM_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type150: BinaryAssociation = BinaryAssociation(
    name="type150",
    ends={
        Property(name="OclType151", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType152: BinaryAssociation = BinaryAssociation(
    name="tupleType152",
    ends={
        Property(name="TupleType", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model153: BinaryAssociation = BinaryAssociation(
    name="model153",
    ends={
        Property(name="OclModel155", type=QualityMetamodel_QMM_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements154", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
returnType160: BinaryAssociation = BinaryAssociation(
    name="returnType160",
    ends={
        Property(name="OclType161", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaReturnType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes162: BinaryAssociation = BinaryAssociation(
    name="argumentTypes162",
    ends={
        Property(name="OclType163", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaArgType", type=OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature164: BinaryAssociation = BinaryAssociation(
    name="feature164",
    ends={
        Property(name="OclFeature", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_165: BinaryAssociation = BinaryAssociation(
    name="context_165",
    ends={
        Property(name="OclContextDefinition167", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition166", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition168: BinaryAssociation = BinaryAssociation(
    name="definition168",
    ends={
        Property(name="OclFeatureDefinition", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_169", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_170: BinaryAssociation = BinaryAssociation(
    name="context_170",
    ends={
        Property(name="OclType171", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition172: BinaryAssociation = BinaryAssociation(
    name="definition172",
    ends={
        Property(name="OclFeatureDefinition173", type=QualityMetamodel_QMM_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression174: BinaryAssociation = BinaryAssociation(
    name="initExpression174",
    ends={
        Property(name="OclExpression175", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type176: BinaryAssociation = BinaryAssociation(
    name="type176",
    ends={
        Property(name="OclType177", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueType156: BinaryAssociation = BinaryAssociation(
    name="valueType156",
    ends={
        Property(name="OclType157", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType158: BinaryAssociation = BinaryAssociation(
    name="keyType158",
    ends={
        Property(name="OclType159", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body182: BinaryAssociation = BinaryAssociation(
    name="body182",
    ends={
        Property(name="OclExpression183", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements184: BinaryAssociation = BinaryAssociation(
    name="elements184",
    ends={
        Property(name="OclModelElement", type=QualityMetamodel_QMM_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model185: BinaryAssociation = BinaryAssociation(
    name="model185",
    ends={
        Property(name="OclInstanceModel", type=QualityMetamodel_QMM_OCL_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel186: BinaryAssociation = BinaryAssociation(
    name="metamodel186",
    ends={
        Property(name="OclMetamodel188", type=QualityMetamodel_QMM_OCL_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model187", type=OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)
parameters178: BinaryAssociation = BinaryAssociation(
    name="parameters178",
    ends={
        Property(name="Parameter", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType179: BinaryAssociation = BinaryAssociation(
    name="returnType179",
    ends={
        Property(name="OclType181", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation180", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_QualityMetamodel_QualityModel_Module = Generalization(general=Module, specific=QualityMetamodel_QualityModel)
gen_QualityMetamodel_Value_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_Value)
gen_QualityMetamodel_ValueType_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_ValueType)
gen_QualityMetamodel_SingleValue_Value = Generalization(general=Value, specific=QualityMetamodel_SingleValue)
gen_QualityMetamodel_AggregatedValue_Value = Generalization(general=Value, specific=QualityMetamodel_AggregatedValue)
gen_QualityMetamodel_TextValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_TextValueType)
gen_QualityMetamodel_RangeValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RangeValueType)
gen_QualityMetamodel_AggregatedValueMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_AggregatedValueMetric)
gen_QualityMetamodel_QualityAttribute_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QualityAttribute)
gen_QualityMetamodel_RealValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RealValueType)
gen_QualityMetamodel_BooleanValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_BooleanValueType)
gen_QualityMetamodel_IntegerValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_IntegerValueType)
gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_NamedElement)
gen_QualityMetamodel_QMM_OCL_Module_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Module)
gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_ModuleElement)
gen_QualityMetamodel_QMM_OCL_Import_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Import)
gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclExpression)
gen_QualityMetamodel_EnumerationMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_EnumerationMetric)
gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_VariableExp)
gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_BooleanExp)
gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_NumericExp)
gen_QualityMetamodel_QMM_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=QualityMetamodel_QMM_OCL_RealExp)
gen_QualityMetamodel_QMM_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=QualityMetamodel_QMM_OCL_IntegerExp)
gen_QualityMetamodel_QMM_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_CollectionExp)
gen_QualityMetamodel_QMM_OCL_CollectionPart_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_CollectionPart)
gen_QualityMetamodel_QMM_OCL_CollectionRange_CollectionPart = Generalization(general=CollectionPart, specific=QualityMetamodel_QMM_OCL_CollectionRange)
gen_QualityMetamodel_QMM_OCL_CollectionItem_CollectionPart = Generalization(general=CollectionPart, specific=QualityMetamodel_QMM_OCL_CollectionItem)
gen_QualityMetamodel_QMM_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_BagExp)
gen_QualityMetamodel_QMM_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_OrderedSetExp)
gen_QualityMetamodel_QMM_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_SequenceExp)
gen_QualityMetamodel_QMM_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_SetExp)
gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_TupleExp)
gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=QualityMetamodel_QMM_OCL_TuplePart)
gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SuperExp)
gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SelfExp)
gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnvExp)
gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PrimitiveExp)
gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_StringExp)
gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnumLiteralExp)
gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclUndefinedExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_StaticPropertyCallExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_StaticPropertyCall)
gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticOperationCall)
gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PropertyCallExp)
gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_PropertyCall)
gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_MapExp)
gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_MapElement)
gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OperatorCallExp)
gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_NotOpCallExp)
gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_RelOpCallExp)
gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_EqOpCallExp)
gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_AddOpCallExp)
gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_IntOpCallExp)
gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_MulOpCallExp)
gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=QualityMetamodel_QMM_OCL_LambdaCallExp)
gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_BraceExp)
gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=QualityMetamodel_QMM_OCL_CollectionOperationCall)
gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_LoopExp)
gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IterateExp)
gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_NavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_OperationCall)
gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_IfExp)
gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_VariableDeclaration)
gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_LocalVariable)
gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Iterator)
gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Parameter)
gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IteratorExp)
gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_LetExp)
gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclModelElementExp)
gen_QualityMetamodel_QMM_OCL_Primitive_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_Primitive)
gen_QualityMetamodel_QMM_OCL_StringType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_StringType)
gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_BooleanType)
gen_QualityMetamodel_QMM_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_NumericType)
gen_QualityMetamodel_QMM_OCL_CollectionType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_CollectionType)
gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclType)
gen_QualityMetamodel_QMM_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_TupleTypeAttribute)
gen_QualityMetamodel_QMM_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_OclModelElement)
gen_QualityMetamodel_QMM_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=QualityMetamodel_QMM_OCL_IntegerType)
gen_QualityMetamodel_QMM_OCL_RealType_NumericType = Generalization(general=NumericType, specific=QualityMetamodel_QMM_OCL_RealType)
gen_QualityMetamodel_QMM_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_BagType)
gen_QualityMetamodel_QMM_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_OrderedSetType)
gen_QualityMetamodel_QMM_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_SequenceType)
gen_QualityMetamodel_QMM_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_SetType)
gen_QualityMetamodel_QMM_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_OclAnyType)
gen_QualityMetamodel_QMM_OCL_TupleType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_TupleType)
gen_QualityMetamodel_QMM_OCL_LambdaType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_LambdaType)
gen_QualityMetamodel_QMM_OCL_EnvType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_EnvType)
gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=QualityMetamodel_QMM_OCL_OclFeatureDefinition)
gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclContextDefinition)
gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclFeature)
gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Attribute)
gen_QualityMetamodel_QMM_OCL_MapType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_MapType)
gen_QualityMetamodel_QMM_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Operation)
gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclModel)
gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclMetamodel)
gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclInstanceModel)

# Domain Model
domain_model = DomainModel(
    name="QualityMetamodel",
    types={QualityMetamodel_QualityModel, Module, QualityMetamodel_MetricProvider, QualityMetamodel_ValueType, QualityMetamodel_QualityAttribute, QualityMetamodel_SingleValue, Value, QualityMetamodel_AggregatedValue, QualityMetamodel_Operation, OclExpression, QualityMetamodel_TextValueType, ValueType, QualityMetamodel_RangeValueType, QualityMetamodel_AggregatedValueMetric, QualityMetamodel_Value, VariableDeclaration, QualityMetamodel_RealValueType, QualityMetamodel_BooleanValueType, QualityMetamodel_IntegerValueType, QualityMetamodel_QMM_OCL_LocatedElement, QualityMetamodel_QMM_OCL_NamedElement, LocatedElement, QualityMetamodel_QMM_OCL_Module, NamedElement, OclMetamodel, Import, ModuleElement, QualityMetamodel_QMM_OCL_ModuleElement, QualityMetamodel_QMM_OCL_Import, QualityMetamodel_QMM_OCL_OclExpression, QualityMetamodel_EnumerationMetric, QualityMetamodel_EnumerationItem, PropertyCallExp, LetExp, LoopExp, OperationCall, LocalVariable, Operation, Attribute, OperatorCallExp, QualityMetamodel_QMM_OCL_VariableExp, OclType, IfExp, QualityMetamodel_QMM_OCL_BooleanExp, QualityMetamodel_QMM_OCL_NumericExp, QualityMetamodel_QMM_OCL_RealExp, NumericExp, QualityMetamodel_QMM_OCL_IntegerExp, QualityMetamodel_QMM_OCL_CollectionExp, CollectionPart, QualityMetamodel_QMM_OCL_CollectionPart, CollectionExp, QualityMetamodel_QMM_OCL_CollectionRange, QualityMetamodel_QMM_OCL_CollectionItem, QualityMetamodel_QMM_OCL_BagExp, QualityMetamodel_QMM_OCL_OrderedSetExp, QualityMetamodel_QMM_OCL_SequenceExp, QualityMetamodel_QMM_OCL_SetExp, QualityMetamodel_QMM_OCL_TupleExp, TuplePart, QualityMetamodel_QMM_OCL_TuplePart, TupleExp, QualityMetamodel_QMM_OCL_SuperExp, QualityMetamodel_QMM_OCL_SelfExp, QualityMetamodel_QMM_OCL_EnvExp, QualityMetamodel_QMM_OCL_PrimitiveExp, QualityMetamodel_QMM_OCL_StringExp, PrimitiveExp, QualityMetamodel_QMM_OCL_EnumLiteralExp, QualityMetamodel_QMM_OCL_OclUndefinedExp, QualityMetamodel_QMM_OCL_StaticPropertyCallExp, StaticPropertyCall, QualityMetamodel_QMM_OCL_StaticPropertyCall, StaticPropertyCallExp, QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall, QualityMetamodel_QMM_OCL_StaticOperationCall, QualityMetamodel_QMM_OCL_PropertyCallExp, PropertyCall, QualityMetamodel_QMM_OCL_PropertyCall, QualityMetamodel_QMM_OCL_MapExp, MapElement, QualityMetamodel_QMM_OCL_MapElement, MapExp, QualityMetamodel_QMM_OCL_OperatorCallExp, QualityMetamodel_QMM_OCL_NotOpCallExp, QualityMetamodel_QMM_OCL_RelOpCallExp, QualityMetamodel_QMM_OCL_EqOpCallExp, QualityMetamodel_QMM_OCL_AddOpCallExp, QualityMetamodel_QMM_OCL_IntOpCallExp, QualityMetamodel_QMM_OCL_MulOpCallExp, QualityMetamodel_QMM_OCL_LambdaCallExp, VariableExp, QualityMetamodel_QMM_OCL_BraceExp, QualityMetamodel_QMM_OCL_CollectionOperationCall, QualityMetamodel_QMM_OCL_LoopExp, Iterator, QualityMetamodel_QMM_OCL_IterateExp, QualityMetamodel_QMM_OCL_NavigationOrAttributeCall, QualityMetamodel_QMM_OCL_OperationCall, QualityMetamodel_QMM_OCL_IfExp, QualityMetamodel_QMM_OCL_VariableDeclaration, QualityMetamodel_QMM_OCL_LocalVariable, IterateExp, QualityMetamodel_QMM_OCL_Iterator, QualityMetamodel_QMM_OCL_Parameter, QualityMetamodel_QMM_OCL_IteratorExp, QualityMetamodel_QMM_OCL_LetExp, MapType, CollectionType, TupleTypeAttribute, LambdaType, QualityMetamodel_QMM_OCL_OclModelElementExp, OclModel, QualityMetamodel_QMM_OCL_Primitive, QualityMetamodel_QMM_OCL_StringType, Primitive, QualityMetamodel_QMM_OCL_BooleanType, QualityMetamodel_QMM_OCL_NumericType, QualityMetamodel_QMM_OCL_CollectionType, QualityMetamodel_QMM_OCL_OclType, OclContextDefinition, QualityMetamodel_QMM_OCL_TupleTypeAttribute, TupleType, QualityMetamodel_QMM_OCL_OclModelElement, QualityMetamodel_QMM_OCL_IntegerType, NumericType, QualityMetamodel_QMM_OCL_MapType, QualityMetamodel_QMM_OCL_RealType, QualityMetamodel_QMM_OCL_BagType, QualityMetamodel_QMM_OCL_OrderedSetType, QualityMetamodel_QMM_OCL_SequenceType, QualityMetamodel_QMM_OCL_SetType, QualityMetamodel_QMM_OCL_OclAnyType, QualityMetamodel_QMM_OCL_TupleType, QualityMetamodel_QMM_OCL_LambdaType, QualityMetamodel_QMM_OCL_EnvType, QualityMetamodel_QMM_OCL_OclFeatureDefinition, OclFeature, QualityMetamodel_QMM_OCL_OclContextDefinition, OclFeatureDefinition, QualityMetamodel_QMM_OCL_OclFeature, QualityMetamodel_QMM_OCL_Attribute, QualityMetamodel_QMM_OCL_Operation, QualityMetamodel_QMM_OCL_OclModel, OclModelElement, QualityMetamodel_QMM_OCL_OclMetamodel, OclInstanceModel, QualityMetamodel_QMM_OCL_OclInstanceModel, Parameter_},
    associations={metricProviders0, qualityTypes1, qualityAttributes3, valueType13, val14, measuredBy15, calculatedBy17, aggregatedValues18, ref21, qualityValues5, value7, qualityAttributes11, metamodels27, imports28, elements29, module31, module32, set23, value24, appliedProperty36, letExp37, loopExp38, parentOperation39, initializedVariable40, ifExp241, owningOperation43, ifExp145, owningAttribute47, appliedOperator49, referredVariable51, type34, ifExp335, parts52, collection53, first54, last56, item59, tuplePart61, tuple62, value68, source71, staticCall73, staticCallExp74, arguments75, calls77, source78, callExp80, elements63, map64, key66, argument84, source86, arguments88, exp90, body92, iterators94, result95, arguments82, thenExpression102, condition104, elseExpression106, type108, variableExp110, letExp111, initExpression113, baseExp115, loopExpr116, operation118, variable97, in_99, definitions122, oclExpression123, operation125, mapType2127, attribute129, mapType132, collectionTypes134, tupleTypeAttribute135, variableDeclaration137, lambdaReturnType140, lambdaArgType142, staticPropertyCall144, model147, elementType120, attributes148, type150, tupleType152, model153, returnType160, argumentTypes162, feature164, context_165, definition168, context_170, definition172, initExpression174, type176, valueType156, keyType158, body182, elements184, model185, metamodel186, parameters178, returnType179},
    generalizations={gen_QualityMetamodel_QualityModel_Module, gen_QualityMetamodel_Value_VariableDeclaration, gen_QualityMetamodel_ValueType_VariableDeclaration, gen_QualityMetamodel_SingleValue_Value, gen_QualityMetamodel_AggregatedValue_Value, gen_QualityMetamodel_TextValueType_ValueType, gen_QualityMetamodel_RangeValueType_ValueType, gen_QualityMetamodel_AggregatedValueMetric_ValueType, gen_QualityMetamodel_QualityAttribute_VariableDeclaration, gen_QualityMetamodel_RealValueType_ValueType, gen_QualityMetamodel_BooleanValueType_ValueType, gen_QualityMetamodel_IntegerValueType_ValueType, gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_Module_NamedElement, gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_Import_NamedElement, gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement, gen_QualityMetamodel_EnumerationMetric_ValueType, gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression, gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_RealExp_NumericExp, gen_QualityMetamodel_QMM_OCL_IntegerExp_NumericExp, gen_QualityMetamodel_QMM_OCL_CollectionExp_OclExpression, gen_QualityMetamodel_QMM_OCL_CollectionPart_LocatedElement, gen_QualityMetamodel_QMM_OCL_CollectionRange_CollectionPart, gen_QualityMetamodel_QMM_OCL_CollectionItem_CollectionPart, gen_QualityMetamodel_QMM_OCL_BagExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_OrderedSetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SequenceExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression, gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable, gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression, gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression, gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression, gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression, gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp, gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression, gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall, gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall, gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp, gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement, gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp, gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression, gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression, gen_QualityMetamodel_QMM_OCL_Primitive_OclType, gen_QualityMetamodel_QMM_OCL_StringType_Primitive, gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive, gen_QualityMetamodel_QMM_OCL_NumericType_Primitive, gen_QualityMetamodel_QMM_OCL_CollectionType_OclType, gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement, gen_QualityMetamodel_QMM_OCL_TupleTypeAttribute_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclModelElement_OclType, gen_QualityMetamodel_QMM_OCL_IntegerType_NumericType, gen_QualityMetamodel_QMM_OCL_RealType_NumericType, gen_QualityMetamodel_QMM_OCL_BagType_CollectionType, gen_QualityMetamodel_QMM_OCL_OrderedSetType_CollectionType, gen_QualityMetamodel_QMM_OCL_SequenceType_CollectionType, gen_QualityMetamodel_QMM_OCL_SetType_CollectionType, gen_QualityMetamodel_QMM_OCL_OclAnyType_OclType, gen_QualityMetamodel_QMM_OCL_TupleType_OclType, gen_QualityMetamodel_QMM_OCL_LambdaType_OclType, gen_QualityMetamodel_QMM_OCL_EnvType_OclType, gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement, gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement, gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature, gen_QualityMetamodel_QMM_OCL_MapType_OclType, gen_QualityMetamodel_QMM_OCL_Operation_OclFeature, gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement, gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel, gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)