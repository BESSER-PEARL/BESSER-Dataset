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
QualityMetamodel_SingleValue = Class(name="QualityMetamodel::SingleValue")
Value = Class(name="Value")
QualityMetamodel_AggregatedValue = Class(name="QualityMetamodel::AggregatedValue")
QualityMetamodel_Operation = Class(name="QualityMetamodel::Operation")
QualityMetamodel_QualityModel = Class(name="QualityMetamodel::QualityModel")
Module = Class(name="Module")
QualityMetamodel_MetricProvider = Class(name="QualityMetamodel::MetricProvider")
QualityMetamodel_ValueType = Class(name="QualityMetamodel::ValueType", is_abstract=True)
QualityMetamodel_QualityAttribute = Class(name="QualityMetamodel::QualityAttribute")
QualityMetamodel_Value = Class(name="QualityMetamodel::Value", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
QualityMetamodel_RealValueType = Class(name="QualityMetamodel::RealValueType")
QualityMetamodel_BooleanValueType = Class(name="QualityMetamodel::BooleanValueType")
QualityMetamodel_IntegerValueType = Class(name="QualityMetamodel::IntegerValueType")
OclExpression = Class(name="OclExpression")
QualityMetamodel_TextValueType = Class(name="QualityMetamodel::TextValueType")
ValueType = Class(name="ValueType")
QualityMetamodel_RangeValueType = Class(name="QualityMetamodel::RangeValueType")
QualityMetamodel_AggregatedValueMetric = Class(name="QualityMetamodel::AggregatedValueMetric")
QualityMetamodel_EnumerationMetric = Class(name="QualityMetamodel::EnumerationMetric")
QualityMetamodel_EnumerationItem = Class(name="QualityMetamodel::EnumerationItem")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
QualityMetamodel_QMM_OCL_LocatedElement = Class(name="QualityMetamodel::QMM::OCL::LocatedElement", is_abstract=True)
QualityMetamodel_QMM_OCL_NamedElement = Class(name="QualityMetamodel::QMM::OCL::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
QualityMetamodel_QMM_OCL_Module = Class(name="QualityMetamodel::QMM::OCL::Module")
NamedElement = Class(name="NamedElement")
OclMetamodel = Class(name="OclMetamodel")
Import = Class(name="Import")
ModuleElement = Class(name="ModuleElement")
QualityMetamodel_QMM_OCL_ModuleElement = Class(name="QualityMetamodel::QMM::OCL::ModuleElement", is_abstract=True)
QualityMetamodel_QMM_OCL_Import = Class(name="QualityMetamodel::QMM::OCL::Import")
QualityMetamodel_QMM_OCL_OclExpression = Class(name="QualityMetamodel::QMM::OCL::OclExpression", is_abstract=True)
QualityMetamodel_QMM_OCL_StringExp = Class(name="QualityMetamodel::QMM::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
QualityMetamodel_QMM_OCL_BooleanExp = Class(name="QualityMetamodel::QMM::OCL::BooleanExp")
QualityMetamodel_QMM_OCL_NumericExp = Class(name="QualityMetamodel::QMM::OCL::NumericExp", is_abstract=True)
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCall = Class(name="OperationCall")
LocalVariable = Class(name="LocalVariable")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OperatorCallExp = Class(name="OperatorCallExp")
QualityMetamodel_QMM_OCL_VariableExp = Class(name="QualityMetamodel::QMM::OCL::VariableExp")
QualityMetamodel_QMM_OCL_SuperExp = Class(name="QualityMetamodel::QMM::OCL::SuperExp")
QualityMetamodel_QMM_OCL_SelfExp = Class(name="QualityMetamodel::QMM::OCL::SelfExp")
QualityMetamodel_QMM_OCL_EnvExp = Class(name="QualityMetamodel::QMM::OCL::EnvExp")
QualityMetamodel_QMM_OCL_PrimitiveExp = Class(name="QualityMetamodel::QMM::OCL::PrimitiveExp", is_abstract=True)
QualityMetamodel_QMM_OCL_TupleExp = Class(name="QualityMetamodel::QMM::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
QualityMetamodel_QMM_OCL_TuplePart = Class(name="QualityMetamodel::QMM::OCL::TuplePart")
TupleExp = Class(name="TupleExp")
QualityMetamodel_QMM_OCL_RealExp = Class(name="QualityMetamodel::QMM::OCL::RealExp")
NumericExp = Class(name="NumericExp")
QualityMetamodel_QMM_OCL_IntegerExp = Class(name="QualityMetamodel::QMM::OCL::IntegerExp")
QualityMetamodel_QMM_OCL_CollectionExp = Class(name="QualityMetamodel::QMM::OCL::CollectionExp", is_abstract=True)
CollectionPart = Class(name="CollectionPart")
QualityMetamodel_QMM_OCL_CollectionPart = Class(name="QualityMetamodel::QMM::OCL::CollectionPart", is_abstract=True)
CollectionExp = Class(name="CollectionExp")
QualityMetamodel_QMM_OCL_CollectionRange = Class(name="QualityMetamodel::QMM::OCL::CollectionRange")
QualityMetamodel_QMM_OCL_CollectionItem = Class(name="QualityMetamodel::QMM::OCL::CollectionItem")
QualityMetamodel_QMM_OCL_BagExp = Class(name="QualityMetamodel::QMM::OCL::BagExp")
QualityMetamodel_QMM_OCL_OrderedSetExp = Class(name="QualityMetamodel::QMM::OCL::OrderedSetExp")
QualityMetamodel_QMM_OCL_SequenceExp = Class(name="QualityMetamodel::QMM::OCL::SequenceExp")
QualityMetamodel_QMM_OCL_SetExp = Class(name="QualityMetamodel::QMM::OCL::SetExp")
QualityMetamodel_QMM_OCL_StaticOperationCall = Class(name="QualityMetamodel::QMM::OCL::StaticOperationCall")
QualityMetamodel_QMM_OCL_MapExp = Class(name="QualityMetamodel::QMM::OCL::MapExp")
MapElement = Class(name="MapElement")
QualityMetamodel_QMM_OCL_MapElement = Class(name="QualityMetamodel::QMM::OCL::MapElement")
MapExp = Class(name="MapExp")
QualityMetamodel_QMM_OCL_EnumLiteralExp = Class(name="QualityMetamodel::QMM::OCL::EnumLiteralExp")
QualityMetamodel_QMM_OCL_OclUndefinedExp = Class(name="QualityMetamodel::QMM::OCL::OclUndefinedExp")
QualityMetamodel_QMM_OCL_StaticPropertyCallExp = Class(name="QualityMetamodel::QMM::OCL::StaticPropertyCallExp")
StaticPropertyCall = Class(name="StaticPropertyCall")
QualityMetamodel_QMM_OCL_StaticPropertyCall = Class(name="QualityMetamodel::QMM::OCL::StaticPropertyCall", is_abstract=True)
StaticPropertyCallExp = Class(name="StaticPropertyCallExp")
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall = Class(name="QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_PropertyCallExp = Class(name="QualityMetamodel::QMM::OCL::PropertyCallExp")
PropertyCall = Class(name="PropertyCall")
QualityMetamodel_QMM_OCL_PropertyCall = Class(name="QualityMetamodel::QMM::OCL::PropertyCall", is_abstract=True)
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall = Class(name="QualityMetamodel::QMM::OCL::NavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_OperationCall = Class(name="QualityMetamodel::QMM::OCL::OperationCall")
QualityMetamodel_QMM_OCL_OperatorCallExp = Class(name="QualityMetamodel::QMM::OCL::OperatorCallExp")
QualityMetamodel_QMM_OCL_BraceExp = Class(name="QualityMetamodel::QMM::OCL::BraceExp")
QualityMetamodel_QMM_OCL_CollectionOperationCall = Class(name="QualityMetamodel::QMM::OCL::CollectionOperationCall")
QualityMetamodel_QMM_OCL_NotOpCallExp = Class(name="QualityMetamodel::QMM::OCL::NotOpCallExp")
QualityMetamodel_QMM_OCL_RelOpCallExp = Class(name="QualityMetamodel::QMM::OCL::RelOpCallExp")
QualityMetamodel_QMM_OCL_EqOpCallExp = Class(name="QualityMetamodel::QMM::OCL::EqOpCallExp")
QualityMetamodel_QMM_OCL_AddOpCallExp = Class(name="QualityMetamodel::QMM::OCL::AddOpCallExp")
QualityMetamodel_QMM_OCL_IntOpCallExp = Class(name="QualityMetamodel::QMM::OCL::IntOpCallExp")
QualityMetamodel_QMM_OCL_MulOpCallExp = Class(name="QualityMetamodel::QMM::OCL::MulOpCallExp")
QualityMetamodel_QMM_OCL_LambdaCallExp = Class(name="QualityMetamodel::QMM::OCL::LambdaCallExp")
VariableExp = Class(name="VariableExp")
QualityMetamodel_QMM_OCL_LoopExp = Class(name="QualityMetamodel::QMM::OCL::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
QualityMetamodel_QMM_OCL_IterateExp = Class(name="QualityMetamodel::QMM::OCL::IterateExp")
QualityMetamodel_QMM_OCL_IteratorExp = Class(name="QualityMetamodel::QMM::OCL::IteratorExp")
QualityMetamodel_QMM_OCL_LetExp = Class(name="QualityMetamodel::QMM::OCL::LetExp")
QualityMetamodel_QMM_OCL_IfExp = Class(name="QualityMetamodel::QMM::OCL::IfExp")
QualityMetamodel_QMM_OCL_OclType = Class(name="QualityMetamodel::QMM::OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
QualityMetamodel_QMM_OCL_VariableDeclaration = Class(name="QualityMetamodel::QMM::OCL::VariableDeclaration", is_abstract=True)
QualityMetamodel_QMM_OCL_LocalVariable = Class(name="QualityMetamodel::QMM::OCL::LocalVariable")
IterateExp = Class(name="IterateExp")
QualityMetamodel_QMM_OCL_Iterator = Class(name="QualityMetamodel::QMM::OCL::Iterator")
QualityMetamodel_QMM_OCL_Parameter = Class(name="QualityMetamodel::QMM::OCL::Parameter")
QualityMetamodel_QMM_OCL_CollectionType = Class(name="QualityMetamodel::QMM::OCL::CollectionType")
QualityMetamodel_QMM_OCL_Primitive = Class(name="QualityMetamodel::QMM::OCL::Primitive", is_abstract=True)
QualityMetamodel_QMM_OCL_StringType = Class(name="QualityMetamodel::QMM::OCL::StringType")
Primitive = Class(name="Primitive")
QualityMetamodel_QMM_OCL_BooleanType = Class(name="QualityMetamodel::QMM::OCL::BooleanType")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
LambdaType = Class(name="LambdaType")
QualityMetamodel_QMM_OCL_OclModelElementExp = Class(name="QualityMetamodel::QMM::OCL::OclModelElementExp")
OclModel = Class(name="OclModel")
QualityMetamodel_QMM_OCL_LambdaType = Class(name="QualityMetamodel::QMM::OCL::LambdaType")
QualityMetamodel_QMM_OCL_NumericType = Class(name="QualityMetamodel::QMM::OCL::NumericType", is_abstract=True)
QualityMetamodel_QMM_OCL_IntegerType = Class(name="QualityMetamodel::QMM::OCL::IntegerType")
NumericType = Class(name="NumericType")
QualityMetamodel_QMM_OCL_RealType = Class(name="QualityMetamodel::QMM::OCL::RealType")
QualityMetamodel_QMM_OCL_BagType = Class(name="QualityMetamodel::QMM::OCL::BagType")
QualityMetamodel_QMM_OCL_OrderedSetType = Class(name="QualityMetamodel::QMM::OCL::OrderedSetType")
QualityMetamodel_QMM_OCL_SequenceType = Class(name="QualityMetamodel::QMM::OCL::SequenceType")
QualityMetamodel_QMM_OCL_SetType = Class(name="QualityMetamodel::QMM::OCL::SetType")
QualityMetamodel_QMM_OCL_OclAnyType = Class(name="QualityMetamodel::QMM::OCL::OclAnyType")
QualityMetamodel_QMM_OCL_TupleType = Class(name="QualityMetamodel::QMM::OCL::TupleType")
QualityMetamodel_QMM_OCL_TupleTypeAttribute = Class(name="QualityMetamodel::QMM::OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
QualityMetamodel_QMM_OCL_OclModelElement = Class(name="QualityMetamodel::QMM::OCL::OclModelElement")
QualityMetamodel_QMM_OCL_MapType = Class(name="QualityMetamodel::QMM::OCL::MapType")
QualityMetamodel_QMM_OCL_Operation = Class(name="QualityMetamodel::QMM::OCL::Operation")
Parameter_ = Class(name="Parameter")
QualityMetamodel_QMM_OCL_EnvType = Class(name="QualityMetamodel::QMM::OCL::EnvType")
QualityMetamodel_QMM_OCL_OclFeatureDefinition = Class(name="QualityMetamodel::QMM::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
QualityMetamodel_QMM_OCL_OclContextDefinition = Class(name="QualityMetamodel::QMM::OCL::OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
QualityMetamodel_QMM_OCL_OclFeature = Class(name="QualityMetamodel::QMM::OCL::OclFeature", is_abstract=True)
QualityMetamodel_QMM_OCL_Attribute = Class(name="QualityMetamodel::QMM::OCL::Attribute")
QualityMetamodel_QMM_OCL_OclModel = Class(name="QualityMetamodel::QMM::OCL::OclModel", is_abstract=True)
OclModelElement = Class(name="OclModelElement")
QualityMetamodel_QMM_OCL_OclMetamodel = Class(name="QualityMetamodel::QMM::OCL::OclMetamodel")
OclInstanceModel = Class(name="OclInstanceModel")
QualityMetamodel_QMM_OCL_OclInstanceModel = Class(name="QualityMetamodel::QMM::OCL::OclInstanceModel")

# QualityMetamodel_SingleValue class attributes and methods

# Value class attributes and methods

# QualityMetamodel_AggregatedValue class attributes and methods

# QualityMetamodel_Operation class attributes and methods
QualityMetamodel_Operation_name: Property = Property(name="name", type=StringType)
QualityMetamodel_Operation_body: Property = Property(name="body", type=StringType)
QualityMetamodel_Operation.attributes={QualityMetamodel_Operation_body, QualityMetamodel_Operation_name}

# QualityMetamodel_QualityModel class attributes and methods

# Module class attributes and methods

# QualityMetamodel_MetricProvider class attributes and methods
QualityMetamodel_MetricProvider_name: Property = Property(name="name", type=StringType)
QualityMetamodel_MetricProvider_description: Property = Property(name="description", type=StringType)
QualityMetamodel_MetricProvider_id: Property = Property(name="id", type=StringType)
QualityMetamodel_MetricProvider.attributes={QualityMetamodel_MetricProvider_name, QualityMetamodel_MetricProvider_id, QualityMetamodel_MetricProvider_description}

# QualityMetamodel_ValueType class attributes and methods

# QualityMetamodel_QualityAttribute class attributes and methods

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

# OclExpression class attributes and methods

# QualityMetamodel_TextValueType class attributes and methods
QualityMetamodel_TextValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_TextValueType.attributes={QualityMetamodel_TextValueType_value}

# ValueType class attributes and methods

# QualityMetamodel_RangeValueType class attributes and methods
QualityMetamodel_RangeValueType_min: Property = Property(name="min", type=StringType)
QualityMetamodel_RangeValueType_max: Property = Property(name="max", type=StringType)
QualityMetamodel_RangeValueType.attributes={QualityMetamodel_RangeValueType_max, QualityMetamodel_RangeValueType_min}

# QualityMetamodel_AggregatedValueMetric class attributes and methods
QualityMetamodel_AggregatedValueMetric_minimum: Property = Property(name="minimum", type=StringType)
QualityMetamodel_AggregatedValueMetric_maximum: Property = Property(name="maximum", type=StringType)
QualityMetamodel_AggregatedValueMetric_average: Property = Property(name="average", type=StringType)
QualityMetamodel_AggregatedValueMetric_median: Property = Property(name="median", type=StringType)
QualityMetamodel_AggregatedValueMetric_standardDeviation: Property = Property(name="standardDeviation", type=StringType)
QualityMetamodel_AggregatedValueMetric.attributes={QualityMetamodel_AggregatedValueMetric_minimum, QualityMetamodel_AggregatedValueMetric_maximum, QualityMetamodel_AggregatedValueMetric_median, QualityMetamodel_AggregatedValueMetric_average, QualityMetamodel_AggregatedValueMetric_standardDeviation}

# QualityMetamodel_EnumerationMetric class attributes and methods

# QualityMetamodel_EnumerationItem class attributes and methods
QualityMetamodel_EnumerationItem_name: Property = Property(name="name", type=StringType)
QualityMetamodel_EnumerationItem.attributes={QualityMetamodel_EnumerationItem_name}

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_LocatedElement class attributes and methods
QualityMetamodel_QMM_OCL_LocatedElement_line: Property = Property(name="line", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_column: Property = Property(name="column", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement.attributes={QualityMetamodel_QMM_OCL_LocatedElement_line, QualityMetamodel_QMM_OCL_LocatedElement_column, QualityMetamodel_QMM_OCL_LocatedElement_charStart, QualityMetamodel_QMM_OCL_LocatedElement_charEnd}

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

# QualityMetamodel_QMM_OCL_StringExp class attributes and methods
QualityMetamodel_QMM_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
QualityMetamodel_QMM_OCL_StringExp.attributes={QualityMetamodel_QMM_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# QualityMetamodel_QMM_OCL_BooleanExp class attributes and methods
QualityMetamodel_QMM_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
QualityMetamodel_QMM_OCL_BooleanExp.attributes={QualityMetamodel_QMM_OCL_BooleanExp_booleanSymbol}

# QualityMetamodel_QMM_OCL_NumericExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCall class attributes and methods

# LocalVariable class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OperatorCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_VariableExp class attributes and methods

# QualityMetamodel_QMM_OCL_SuperExp class attributes and methods

# QualityMetamodel_QMM_OCL_SelfExp class attributes and methods

# QualityMetamodel_QMM_OCL_EnvExp class attributes and methods

# QualityMetamodel_QMM_OCL_PrimitiveExp class attributes and methods

# QualityMetamodel_QMM_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# QualityMetamodel_QMM_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

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

# QualityMetamodel_QMM_OCL_StaticOperationCall class attributes and methods
QualityMetamodel_QMM_OCL_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_StaticOperationCall.attributes={QualityMetamodel_QMM_OCL_StaticOperationCall_operationName}

# QualityMetamodel_QMM_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# QualityMetamodel_QMM_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

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

# QualityMetamodel_QMM_OCL_PropertyCallExp class attributes and methods

# PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_NavigationOrAttributeCall class attributes and methods
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.attributes={QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name}

# QualityMetamodel_QMM_OCL_OperationCall class attributes and methods
QualityMetamodel_QMM_OCL_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperationCall.attributes={QualityMetamodel_QMM_OCL_OperationCall_operationName}

# QualityMetamodel_QMM_OCL_OperatorCallExp class attributes and methods
QualityMetamodel_QMM_OCL_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperatorCallExp.attributes={QualityMetamodel_QMM_OCL_OperatorCallExp_operationName}

# QualityMetamodel_QMM_OCL_BraceExp class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionOperationCall class attributes and methods

# QualityMetamodel_QMM_OCL_NotOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_RelOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_EqOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_AddOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_IntOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_MulOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# QualityMetamodel_QMM_OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# QualityMetamodel_QMM_OCL_IterateExp class attributes and methods

# QualityMetamodel_QMM_OCL_IteratorExp class attributes and methods
QualityMetamodel_QMM_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_IteratorExp.attributes={QualityMetamodel_QMM_OCL_IteratorExp_name}

# QualityMetamodel_QMM_OCL_LetExp class attributes and methods

# QualityMetamodel_QMM_OCL_IfExp class attributes and methods

# QualityMetamodel_QMM_OCL_OclType class attributes and methods
QualityMetamodel_QMM_OCL_OclType_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclType.attributes={QualityMetamodel_QMM_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# QualityMetamodel_QMM_OCL_VariableDeclaration class attributes and methods
QualityMetamodel_QMM_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
QualityMetamodel_QMM_OCL_VariableDeclaration.attributes={QualityMetamodel_QMM_OCL_VariableDeclaration_varName}

# QualityMetamodel_QMM_OCL_LocalVariable class attributes and methods
QualityMetamodel_QMM_OCL_LocalVariable_eq: Property = Property(name="eq", type=StringType)
QualityMetamodel_QMM_OCL_LocalVariable.attributes={QualityMetamodel_QMM_OCL_LocalVariable_eq}

# IterateExp class attributes and methods

# QualityMetamodel_QMM_OCL_Iterator class attributes and methods

# QualityMetamodel_QMM_OCL_Parameter class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionType class attributes and methods

# QualityMetamodel_QMM_OCL_Primitive class attributes and methods

# QualityMetamodel_QMM_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# QualityMetamodel_QMM_OCL_BooleanType class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# LambdaType class attributes and methods

# QualityMetamodel_QMM_OCL_OclModelElementExp class attributes and methods
QualityMetamodel_QMM_OCL_OclModelElementExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclModelElementExp.attributes={QualityMetamodel_QMM_OCL_OclModelElementExp_name}

# OclModel class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaType class attributes and methods

# QualityMetamodel_QMM_OCL_NumericType class attributes and methods

# QualityMetamodel_QMM_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# QualityMetamodel_QMM_OCL_RealType class attributes and methods

# QualityMetamodel_QMM_OCL_BagType class attributes and methods

# QualityMetamodel_QMM_OCL_OrderedSetType class attributes and methods

# QualityMetamodel_QMM_OCL_SequenceType class attributes and methods

# QualityMetamodel_QMM_OCL_SetType class attributes and methods

# QualityMetamodel_QMM_OCL_OclAnyType class attributes and methods

# QualityMetamodel_QMM_OCL_TupleType class attributes and methods

# QualityMetamodel_QMM_OCL_TupleTypeAttribute class attributes and methods
QualityMetamodel_QMM_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_TupleTypeAttribute.attributes={QualityMetamodel_QMM_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# QualityMetamodel_QMM_OCL_OclModelElement class attributes and methods

# QualityMetamodel_QMM_OCL_MapType class attributes and methods

# QualityMetamodel_QMM_OCL_Operation class attributes and methods

# Parameter class attributes and methods

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

# QualityMetamodel_QMM_OCL_OclModel class attributes and methods

# OclModelElement class attributes and methods

# QualityMetamodel_QMM_OCL_OclMetamodel class attributes and methods
QualityMetamodel_QMM_OCL_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
QualityMetamodel_QMM_OCL_OclMetamodel.attributes={QualityMetamodel_QMM_OCL_OclMetamodel_uri}

# OclInstanceModel class attributes and methods

# QualityMetamodel_QMM_OCL_OclInstanceModel class attributes and methods

# Relationships
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
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="QMM_OCL37", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp338: BinaryAssociation = BinaryAssociation(
    name="ifExp338",
    ends={
        Property(name="QMM_OCL39", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty40: BinaryAssociation = BinaryAssociation(
    name="appliedProperty40",
    ends={
        Property(name="QMM_OCL41", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
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
        Property(name="QMM_OCL", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="Import", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements29: BinaryAssociation = BinaryAssociation(
    name="elements29",
    ends={
        Property(name="QMM_OCL30", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ModuleElement", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module31: BinaryAssociation = BinaryAssociation(
    name="module31",
    ends={
        Property(name="QMM_OCL32", type=QualityMetamodel_QMM_OCL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Module", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module33: BinaryAssociation = BinaryAssociation(
    name="module33",
    ends={
        Property(name="QMM_OCL35", type=QualityMetamodel_QMM_OCL_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="Module34", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
letExp42: BinaryAssociation = BinaryAssociation(
    name="letExp42",
    ends={
        Property(name="QMM_OCL43", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp44: BinaryAssociation = BinaryAssociation(
    name="loopExp44",
    ends={
        Property(name="QMM_OCL45", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation46: BinaryAssociation = BinaryAssociation(
    name="parentOperation46",
    ends={
        Property(name="QMM_OCL47", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCall", type=OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable48: BinaryAssociation = BinaryAssociation(
    name="initializedVariable48",
    ends={
        Property(name="QMM_OCL49", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp250: BinaryAssociation = BinaryAssociation(
    name="ifExp250",
    ends={
        Property(name="QMM_OCL52", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp51", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation53: BinaryAssociation = BinaryAssociation(
    name="owningOperation53",
    ends={
        Property(name="QMM_OCL54", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp155: BinaryAssociation = BinaryAssociation(
    name="ifExp155",
    ends={
        Property(name="QMM_OCL57", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp56", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute58: BinaryAssociation = BinaryAssociation(
    name="owningAttribute58",
    ends={
        Property(name="QMM_OCL59", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
appliedOperator60: BinaryAssociation = BinaryAssociation(
    name="appliedOperator60",
    ends={
        Property(name="QMM_OCL61", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperatorCallExp", type=OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable62: BinaryAssociation = BinaryAssociation(
    name="referredVariable62",
    ends={
        Property(name="QMM_OCL63", type=QualityMetamodel_QMM_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
tuplePart75: BinaryAssociation = BinaryAssociation(
    name="tuplePart75",
    ends={
        Property(name="QMM_OCL76", type=QualityMetamodel_QMM_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple77: BinaryAssociation = BinaryAssociation(
    name="tuple77",
    ends={
        Property(name="QMM_OCL78", type=QualityMetamodel_QMM_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
parts64: BinaryAssociation = BinaryAssociation(
    name="parts64",
    ends={
        Property(name="QMM_OCL65", type=QualityMetamodel_QMM_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionPart", type=CollectionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection66: BinaryAssociation = BinaryAssociation(
    name="collection66",
    ends={
        Property(name="QMM_OCL67", type=QualityMetamodel_QMM_OCL_CollectionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
first68: BinaryAssociation = BinaryAssociation(
    name="first68",
    ends={
        Property(name="OclExpression69", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last70: BinaryAssociation = BinaryAssociation(
    name="last70",
    ends={
        Property(name="OclExpression72", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange71", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item73: BinaryAssociation = BinaryAssociation(
    name="item73",
    ends={
        Property(name="OclExpression74", type=QualityMetamodel_QMM_OCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments95: BinaryAssociation = BinaryAssociation(
    name="arguments95",
    ends={
        Property(name="OclExpression96", type=QualityMetamodel_QMM_OCL_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_StaticOperationCall", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements79: BinaryAssociation = BinaryAssociation(
    name="elements79",
    ends={
        Property(name="QMM_OCL80", type=QualityMetamodel_QMM_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map81: BinaryAssociation = BinaryAssociation(
    name="map81",
    ends={
        Property(name="QMM_OCL82", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key83: BinaryAssociation = BinaryAssociation(
    name="key83",
    ends={
        Property(name="OclExpression84", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="OclExpression87", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement86", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source88: BinaryAssociation = BinaryAssociation(
    name="source88",
    ends={
        Property(name="QMM_OCL90", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType89", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall91: BinaryAssociation = BinaryAssociation(
    name="staticCall91",
    ends={
        Property(name="QMM_OCL92", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCall", type=StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp93: BinaryAssociation = BinaryAssociation(
    name="staticCallExp93",
    ends={
        Property(name="QMM_OCL94", type=QualityMetamodel_QMM_OCL_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp", type=StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
calls97: BinaryAssociation = BinaryAssociation(
    name="calls97",
    ends={
        Property(name="QMM_OCL98", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCall", type=PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source99: BinaryAssociation = BinaryAssociation(
    name="source99",
    ends={
        Property(name="QMM_OCL101", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression100", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callExp102: BinaryAssociation = BinaryAssociation(
    name="callExp102",
    ends={
        Property(name="QMM_OCL104", type=QualityMetamodel_QMM_OCL_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp103", type=PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments105: BinaryAssociation = BinaryAssociation(
    name="arguments105",
    ends={
        Property(name="QMM_OCL107", type=QualityMetamodel_QMM_OCL_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression106", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument108: BinaryAssociation = BinaryAssociation(
    name="argument108",
    ends={
        Property(name="OclExpression109", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp115: BinaryAssociation = BinaryAssociation(
    name="exp115",
    ends={
        Property(name="OclExpression116", type=QualityMetamodel_QMM_OCL_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_BraceExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source110: BinaryAssociation = BinaryAssociation(
    name="source110",
    ends={
        Property(name="QMM_OCL112", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression111", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments113: BinaryAssociation = BinaryAssociation(
    name="arguments113",
    ends={
        Property(name="OclExpression114", type=QualityMetamodel_QMM_OCL_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_LambdaCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition134: BinaryAssociation = BinaryAssociation(
    name="condition134",
    ends={
        Property(name="QMM_OCL136", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression135", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression137: BinaryAssociation = BinaryAssociation(
    name="elseExpression137",
    ends={
        Property(name="QMM_OCL139", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression138", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body117: BinaryAssociation = BinaryAssociation(
    name="body117",
    ends={
        Property(name="QMM_OCL119", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression118", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators120: BinaryAssociation = BinaryAssociation(
    name="iterators120",
    ends={
        Property(name="QMM_OCL121", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result122: BinaryAssociation = BinaryAssociation(
    name="result122",
    ends={
        Property(name="QMM_OCL124", type=QualityMetamodel_QMM_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable123", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable125: BinaryAssociation = BinaryAssociation(
    name="variable125",
    ends={
        Property(name="QMM_OCL127", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable126", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_128: BinaryAssociation = BinaryAssociation(
    name="in_128",
    ends={
        Property(name="QMM_OCL130", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression129", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression131: BinaryAssociation = BinaryAssociation(
    name="thenExpression131",
    ends={
        Property(name="QMM_OCL133", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression132", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType159: BinaryAssociation = BinaryAssociation(
    name="elementType159",
    ends={
        Property(name="QMM_OCL161", type=QualityMetamodel_QMM_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType160", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions162: BinaryAssociation = BinaryAssociation(
    name="definitions162",
    ends={
        Property(name="QMM_OCL163", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="QMM_OCL142", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType141", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp143: BinaryAssociation = BinaryAssociation(
    name="variableExp143",
    ends={
        Property(name="QMM_OCL144", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp145: BinaryAssociation = BinaryAssociation(
    name="letExp145",
    ends={
        Property(name="QMM_OCL147", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp146", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression148: BinaryAssociation = BinaryAssociation(
    name="initExpression148",
    ends={
        Property(name="QMM_OCL150", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression149", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp151: BinaryAssociation = BinaryAssociation(
    name="baseExp151",
    ends={
        Property(name="QMM_OCL152", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr153: BinaryAssociation = BinaryAssociation(
    name="loopExpr153",
    ends={
        Property(name="QMM_OCL155", type=QualityMetamodel_QMM_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp154", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation156: BinaryAssociation = BinaryAssociation(
    name="operation156",
    ends={
        Property(name="QMM_OCL158", type=QualityMetamodel_QMM_OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation157", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
oclExpression164: BinaryAssociation = BinaryAssociation(
    name="oclExpression164",
    ends={
        Property(name="QMM_OCL166", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression165", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation167: BinaryAssociation = BinaryAssociation(
    name="operation167",
    ends={
        Property(name="QMM_OCL169", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation168", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2170: BinaryAssociation = BinaryAssociation(
    name="mapType2170",
    ends={
        Property(name="QMM_OCL171", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute172: BinaryAssociation = BinaryAssociation(
    name="attribute172",
    ends={
        Property(name="QMM_OCL174", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute173", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType175: BinaryAssociation = BinaryAssociation(
    name="mapType175",
    ends={
        Property(name="QMM_OCL177", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType176", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes178: BinaryAssociation = BinaryAssociation(
    name="collectionTypes178",
    ends={
        Property(name="QMM_OCL179", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute180: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute180",
    ends={
        Property(name="QMM_OCL181", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration182: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration182",
    ends={
        Property(name="QMM_OCL184", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration183", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lambdaReturnType185: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType185",
    ends={
        Property(name="QMM_OCL186", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
lambdaArgType187: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType187",
    ends={
        Property(name="QMM_OCL189", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType188", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
staticPropertyCall190: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall190",
    ends={
        Property(name="QMM_OCL192", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp191", type=StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
keyType208: BinaryAssociation = BinaryAssociation(
    name="keyType208",
    ends={
        Property(name="OclType209", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="QMM_OCL210", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1))
    }
)
model193: BinaryAssociation = BinaryAssociation(
    name="model193",
    ends={
        Property(name="OclModel", type=QualityMetamodel_QMM_OCL_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OclModelElementExp", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
returnType211: BinaryAssociation = BinaryAssociation(
    name="returnType211",
    ends={
        Property(name="QMM_OCL213", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType212", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes214: BinaryAssociation = BinaryAssociation(
    name="argumentTypes214",
    ends={
        Property(name="QMM_OCL216", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType215", type=OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes194: BinaryAssociation = BinaryAssociation(
    name="attributes194",
    ends={
        Property(name="QMM_OCL196", type=QualityMetamodel_QMM_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute195", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="QMM_OCL199", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType198", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType200: BinaryAssociation = BinaryAssociation(
    name="tupleType200",
    ends={
        Property(name="QMM_OCL201", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model202: BinaryAssociation = BinaryAssociation(
    name="model202",
    ends={
        Property(name="QMM_OCL204", type=QualityMetamodel_QMM_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel203", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType205: BinaryAssociation = BinaryAssociation(
    name="valueType205",
    ends={
        Property(name="QMM_OCL207", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType206", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters236: BinaryAssociation = BinaryAssociation(
    name="parameters236",
    ends={
        Property(name="QMM_OCL237", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType238: BinaryAssociation = BinaryAssociation(
    name="returnType238",
    ends={
        Property(name="QMM_OCL240", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType239", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature217: BinaryAssociation = BinaryAssociation(
    name="feature217",
    ends={
        Property(name="QMM_OCL218", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_219: BinaryAssociation = BinaryAssociation(
    name="context_219",
    ends={
        Property(name="QMM_OCL221", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition220", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition222: BinaryAssociation = BinaryAssociation(
    name="definition222",
    ends={
        Property(name="QMM_OCL223", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_224: BinaryAssociation = BinaryAssociation(
    name="context_224",
    ends={
        Property(name="QMM_OCL226", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType225", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition227: BinaryAssociation = BinaryAssociation(
    name="definition227",
    ends={
        Property(name="QMM_OCL229", type=QualityMetamodel_QMM_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition228", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression230: BinaryAssociation = BinaryAssociation(
    name="initExpression230",
    ends={
        Property(name="QMM_OCL232", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression231", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type233: BinaryAssociation = BinaryAssociation(
    name="type233",
    ends={
        Property(name="QMM_OCL235", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType234", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body241: BinaryAssociation = BinaryAssociation(
    name="body241",
    ends={
        Property(name="QMM_OCL243", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression242", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements244: BinaryAssociation = BinaryAssociation(
    name="elements244",
    ends={
        Property(name="QMM_OCL245", type=QualityMetamodel_QMM_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model246: BinaryAssociation = BinaryAssociation(
    name="model246",
    ends={
        Property(name="QMM_OCL247", type=QualityMetamodel_QMM_OCL_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclInstanceModel", type=OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel248: BinaryAssociation = BinaryAssociation(
    name="metamodel248",
    ends={
        Property(name="QMM_OCL250", type=QualityMetamodel_QMM_OCL_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclMetamodel249", type=OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_QualityMetamodel_SingleValue_Value = Generalization(general=Value, specific=QualityMetamodel_SingleValue)
gen_QualityMetamodel_AggregatedValue_Value = Generalization(general=Value, specific=QualityMetamodel_AggregatedValue)
gen_QualityMetamodel_QualityModel_Module = Generalization(general=Module, specific=QualityMetamodel_QualityModel)
gen_QualityMetamodel_QualityAttribute_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QualityAttribute)
gen_QualityMetamodel_Value_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_Value)
gen_QualityMetamodel_ValueType_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_ValueType)
gen_QualityMetamodel_RealValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RealValueType)
gen_QualityMetamodel_BooleanValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_BooleanValueType)
gen_QualityMetamodel_IntegerValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_IntegerValueType)
gen_QualityMetamodel_TextValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_TextValueType)
gen_QualityMetamodel_RangeValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RangeValueType)
gen_QualityMetamodel_AggregatedValueMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_AggregatedValueMetric)
gen_QualityMetamodel_EnumerationMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_EnumerationMetric)
gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclExpression)
gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_NamedElement)
gen_QualityMetamodel_QMM_OCL_Module_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Module)
gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_ModuleElement)
gen_QualityMetamodel_QMM_OCL_Import_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Import)
gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PrimitiveExp)
gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_StringExp)
gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_BooleanExp)
gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_NumericExp)
gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_VariableExp)
gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SuperExp)
gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SelfExp)
gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnvExp)
gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_TupleExp)
gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=QualityMetamodel_QMM_OCL_TuplePart)
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
gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticOperationCall)
gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_MapExp)
gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_MapElement)
gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnumLiteralExp)
gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclUndefinedExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_StaticPropertyCallExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_StaticPropertyCall)
gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PropertyCallExp)
gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_PropertyCall)
gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_NavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_OperationCall)
gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OperatorCallExp)
gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_BraceExp)
gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=QualityMetamodel_QMM_OCL_CollectionOperationCall)
gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_NotOpCallExp)
gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_RelOpCallExp)
gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_EqOpCallExp)
gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_AddOpCallExp)
gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_IntOpCallExp)
gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_MulOpCallExp)
gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=QualityMetamodel_QMM_OCL_LambdaCallExp)
gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_LoopExp)
gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IterateExp)
gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IteratorExp)
gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_LetExp)
gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_IfExp)
gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclType)
gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_VariableDeclaration)
gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_LocalVariable)
gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Iterator)
gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Parameter)
gen_QualityMetamodel_QMM_OCL_CollectionType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_CollectionType)
gen_QualityMetamodel_QMM_OCL_Primitive_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_Primitive)
gen_QualityMetamodel_QMM_OCL_StringType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_StringType)
gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_BooleanType)
gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclModelElementExp)
gen_QualityMetamodel_QMM_OCL_LambdaType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_LambdaType)
gen_QualityMetamodel_QMM_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_NumericType)
gen_QualityMetamodel_QMM_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=QualityMetamodel_QMM_OCL_IntegerType)
gen_QualityMetamodel_QMM_OCL_RealType_NumericType = Generalization(general=NumericType, specific=QualityMetamodel_QMM_OCL_RealType)
gen_QualityMetamodel_QMM_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_BagType)
gen_QualityMetamodel_QMM_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_OrderedSetType)
gen_QualityMetamodel_QMM_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_SequenceType)
gen_QualityMetamodel_QMM_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=QualityMetamodel_QMM_OCL_SetType)
gen_QualityMetamodel_QMM_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_OclAnyType)
gen_QualityMetamodel_QMM_OCL_TupleType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_TupleType)
gen_QualityMetamodel_QMM_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_TupleTypeAttribute)
gen_QualityMetamodel_QMM_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_OclModelElement)
gen_QualityMetamodel_QMM_OCL_MapType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_MapType)
gen_QualityMetamodel_QMM_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Operation)
gen_QualityMetamodel_QMM_OCL_EnvType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_EnvType)
gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=QualityMetamodel_QMM_OCL_OclFeatureDefinition)
gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclContextDefinition)
gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclFeature)
gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Attribute)
gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclModel)
gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclMetamodel)
gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclInstanceModel)

# Domain Model
domain_model = DomainModel(
    name="QualityMetamodel",
    types={QualityMetamodel_SingleValue, Value, QualityMetamodel_AggregatedValue, QualityMetamodel_Operation, QualityMetamodel_QualityModel, Module, QualityMetamodel_MetricProvider, QualityMetamodel_ValueType, QualityMetamodel_QualityAttribute, QualityMetamodel_Value, VariableDeclaration, QualityMetamodel_RealValueType, QualityMetamodel_BooleanValueType, QualityMetamodel_IntegerValueType, OclExpression, QualityMetamodel_TextValueType, ValueType, QualityMetamodel_RangeValueType, QualityMetamodel_AggregatedValueMetric, QualityMetamodel_EnumerationMetric, QualityMetamodel_EnumerationItem, OclType, IfExp, PropertyCallExp, QualityMetamodel_QMM_OCL_LocatedElement, QualityMetamodel_QMM_OCL_NamedElement, LocatedElement, QualityMetamodel_QMM_OCL_Module, NamedElement, OclMetamodel, Import, ModuleElement, QualityMetamodel_QMM_OCL_ModuleElement, QualityMetamodel_QMM_OCL_Import, QualityMetamodel_QMM_OCL_OclExpression, QualityMetamodel_QMM_OCL_StringExp, PrimitiveExp, QualityMetamodel_QMM_OCL_BooleanExp, QualityMetamodel_QMM_OCL_NumericExp, LetExp, LoopExp, OperationCall, LocalVariable, Operation, Attribute, OperatorCallExp, QualityMetamodel_QMM_OCL_VariableExp, QualityMetamodel_QMM_OCL_SuperExp, QualityMetamodel_QMM_OCL_SelfExp, QualityMetamodel_QMM_OCL_EnvExp, QualityMetamodel_QMM_OCL_PrimitiveExp, QualityMetamodel_QMM_OCL_TupleExp, TuplePart, QualityMetamodel_QMM_OCL_TuplePart, TupleExp, QualityMetamodel_QMM_OCL_RealExp, NumericExp, QualityMetamodel_QMM_OCL_IntegerExp, QualityMetamodel_QMM_OCL_CollectionExp, CollectionPart, QualityMetamodel_QMM_OCL_CollectionPart, CollectionExp, QualityMetamodel_QMM_OCL_CollectionRange, QualityMetamodel_QMM_OCL_CollectionItem, QualityMetamodel_QMM_OCL_BagExp, QualityMetamodel_QMM_OCL_OrderedSetExp, QualityMetamodel_QMM_OCL_SequenceExp, QualityMetamodel_QMM_OCL_SetExp, QualityMetamodel_QMM_OCL_StaticOperationCall, QualityMetamodel_QMM_OCL_MapExp, MapElement, QualityMetamodel_QMM_OCL_MapElement, MapExp, QualityMetamodel_QMM_OCL_EnumLiteralExp, QualityMetamodel_QMM_OCL_OclUndefinedExp, QualityMetamodel_QMM_OCL_StaticPropertyCallExp, StaticPropertyCall, QualityMetamodel_QMM_OCL_StaticPropertyCall, StaticPropertyCallExp, QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall, QualityMetamodel_QMM_OCL_PropertyCallExp, PropertyCall, QualityMetamodel_QMM_OCL_PropertyCall, QualityMetamodel_QMM_OCL_NavigationOrAttributeCall, QualityMetamodel_QMM_OCL_OperationCall, QualityMetamodel_QMM_OCL_OperatorCallExp, QualityMetamodel_QMM_OCL_BraceExp, QualityMetamodel_QMM_OCL_CollectionOperationCall, QualityMetamodel_QMM_OCL_NotOpCallExp, QualityMetamodel_QMM_OCL_RelOpCallExp, QualityMetamodel_QMM_OCL_EqOpCallExp, QualityMetamodel_QMM_OCL_AddOpCallExp, QualityMetamodel_QMM_OCL_IntOpCallExp, QualityMetamodel_QMM_OCL_MulOpCallExp, QualityMetamodel_QMM_OCL_LambdaCallExp, VariableExp, QualityMetamodel_QMM_OCL_LoopExp, Iterator, QualityMetamodel_QMM_OCL_IterateExp, QualityMetamodel_QMM_OCL_IteratorExp, QualityMetamodel_QMM_OCL_LetExp, QualityMetamodel_QMM_OCL_IfExp, QualityMetamodel_QMM_OCL_OclType, OclContextDefinition, QualityMetamodel_QMM_OCL_VariableDeclaration, QualityMetamodel_QMM_OCL_LocalVariable, IterateExp, QualityMetamodel_QMM_OCL_Iterator, QualityMetamodel_QMM_OCL_Parameter, QualityMetamodel_QMM_OCL_CollectionType, QualityMetamodel_QMM_OCL_Primitive, QualityMetamodel_QMM_OCL_StringType, Primitive, QualityMetamodel_QMM_OCL_BooleanType, MapType, CollectionType, TupleTypeAttribute, LambdaType, QualityMetamodel_QMM_OCL_OclModelElementExp, OclModel, QualityMetamodel_QMM_OCL_LambdaType, QualityMetamodel_QMM_OCL_NumericType, QualityMetamodel_QMM_OCL_IntegerType, NumericType, QualityMetamodel_QMM_OCL_RealType, QualityMetamodel_QMM_OCL_BagType, QualityMetamodel_QMM_OCL_OrderedSetType, QualityMetamodel_QMM_OCL_SequenceType, QualityMetamodel_QMM_OCL_SetType, QualityMetamodel_QMM_OCL_OclAnyType, QualityMetamodel_QMM_OCL_TupleType, QualityMetamodel_QMM_OCL_TupleTypeAttribute, TupleType, QualityMetamodel_QMM_OCL_OclModelElement, QualityMetamodel_QMM_OCL_MapType, QualityMetamodel_QMM_OCL_Operation, Parameter_, QualityMetamodel_QMM_OCL_EnvType, QualityMetamodel_QMM_OCL_OclFeatureDefinition, OclFeature, QualityMetamodel_QMM_OCL_OclContextDefinition, OclFeatureDefinition, QualityMetamodel_QMM_OCL_OclFeature, QualityMetamodel_QMM_OCL_Attribute, QualityMetamodel_QMM_OCL_OclModel, OclModelElement, QualityMetamodel_QMM_OCL_OclMetamodel, OclInstanceModel, QualityMetamodel_QMM_OCL_OclInstanceModel},
    associations={measuredBy15, calculatedBy17, metricProviders0, qualityTypes1, qualityAttributes3, qualityValues5, value7, qualityAttributes11, valueType13, val14, aggregatedValues18, ref21, set23, value24, type36, ifExp338, appliedProperty40, metamodels27, imports28, elements29, module31, module33, letExp42, loopExp44, parentOperation46, initializedVariable48, ifExp250, owningOperation53, ifExp155, owningAttribute58, appliedOperator60, referredVariable62, tuplePart75, tuple77, parts64, collection66, first68, last70, item73, arguments95, elements79, map81, key83, value85, source88, staticCall91, staticCallExp93, calls97, source99, callExp102, arguments105, argument108, exp115, source110, arguments113, condition134, elseExpression137, body117, iterators120, result122, variable125, in_128, thenExpression131, elementType159, definitions162, type140, variableExp143, letExp145, initExpression148, baseExp151, loopExpr153, operation156, oclExpression164, operation167, mapType2170, attribute172, mapType175, collectionTypes178, tupleTypeAttribute180, variableDeclaration182, lambdaReturnType185, lambdaArgType187, staticPropertyCall190, keyType208, model193, returnType211, argumentTypes214, attributes194, type197, tupleType200, model202, valueType205, parameters236, returnType238, feature217, context_219, definition222, context_224, definition227, initExpression230, type233, body241, elements244, model246, metamodel248},
    generalizations={gen_QualityMetamodel_SingleValue_Value, gen_QualityMetamodel_AggregatedValue_Value, gen_QualityMetamodel_QualityModel_Module, gen_QualityMetamodel_QualityAttribute_VariableDeclaration, gen_QualityMetamodel_Value_VariableDeclaration, gen_QualityMetamodel_ValueType_VariableDeclaration, gen_QualityMetamodel_RealValueType_ValueType, gen_QualityMetamodel_BooleanValueType_ValueType, gen_QualityMetamodel_IntegerValueType_ValueType, gen_QualityMetamodel_TextValueType_ValueType, gen_QualityMetamodel_RangeValueType_ValueType, gen_QualityMetamodel_AggregatedValueMetric_ValueType, gen_QualityMetamodel_EnumerationMetric_ValueType, gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement, gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_Module_NamedElement, gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_Import_NamedElement, gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression, gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression, gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression, gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression, gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable, gen_QualityMetamodel_QMM_OCL_RealExp_NumericExp, gen_QualityMetamodel_QMM_OCL_IntegerExp_NumericExp, gen_QualityMetamodel_QMM_OCL_CollectionExp_OclExpression, gen_QualityMetamodel_QMM_OCL_CollectionPart_LocatedElement, gen_QualityMetamodel_QMM_OCL_CollectionRange_CollectionPart, gen_QualityMetamodel_QMM_OCL_CollectionItem_CollectionPart, gen_QualityMetamodel_QMM_OCL_BagExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_OrderedSetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SequenceExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression, gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression, gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression, gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall, gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp, gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall, gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp, gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp, gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression, gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement, gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement, gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_CollectionType_OclType, gen_QualityMetamodel_QMM_OCL_Primitive_OclType, gen_QualityMetamodel_QMM_OCL_StringType_Primitive, gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive, gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression, gen_QualityMetamodel_QMM_OCL_LambdaType_OclType, gen_QualityMetamodel_QMM_OCL_NumericType_Primitive, gen_QualityMetamodel_QMM_OCL_IntegerType_NumericType, gen_QualityMetamodel_QMM_OCL_RealType_NumericType, gen_QualityMetamodel_QMM_OCL_BagType_CollectionType, gen_QualityMetamodel_QMM_OCL_OrderedSetType_CollectionType, gen_QualityMetamodel_QMM_OCL_SequenceType_CollectionType, gen_QualityMetamodel_QMM_OCL_SetType_CollectionType, gen_QualityMetamodel_QMM_OCL_OclAnyType_OclType, gen_QualityMetamodel_QMM_OCL_TupleType_OclType, gen_QualityMetamodel_QMM_OCL_TupleTypeAttribute_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclModelElement_OclType, gen_QualityMetamodel_QMM_OCL_MapType_OclType, gen_QualityMetamodel_QMM_OCL_Operation_OclFeature, gen_QualityMetamodel_QMM_OCL_EnvType_OclType, gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement, gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement, gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature, gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement, gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel, gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)