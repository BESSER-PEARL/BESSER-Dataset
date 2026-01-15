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
QualityMetamodel_QualityModel = Class(name="QualityMetamodel::QualityModel")
Module = Class(name="Module")
QualityMetamodel_MetricProvider = Class(name="QualityMetamodel::MetricProvider")
QualityMetamodel_ValueType = Class(name="QualityMetamodel::ValueType", is_abstract=True)
QualityMetamodel_QualityAttribute = Class(name="QualityMetamodel::QualityAttribute")
QualityMetamodel_Value = Class(name="QualityMetamodel::Value", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
QualityMetamodel_EnumerationMetric = Class(name="QualityMetamodel::EnumerationMetric")
QualityMetamodel_EnumerationItem = Class(name="QualityMetamodel::EnumerationItem")
QualityMetamodel_SingleValue = Class(name="QualityMetamodel::SingleValue")
Value = Class(name="Value")
QualityMetamodel_AggregatedValue = Class(name="QualityMetamodel::AggregatedValue")
QualityMetamodel_Operation = Class(name="QualityMetamodel::Operation")
OclExpression = Class(name="OclExpression")
QualityMetamodel_TextValueType = Class(name="QualityMetamodel::TextValueType")
ValueType = Class(name="ValueType")
QualityMetamodel_RangeValueType = Class(name="QualityMetamodel::RangeValueType")
QualityMetamodel_AggregatedValueMetric = Class(name="QualityMetamodel::AggregatedValueMetric")
QualityMetamodel_QMM_OCL_ModuleElement = Class(name="QualityMetamodel::QMM::OCL::ModuleElement", is_abstract=True)
QualityMetamodel_RealValueType = Class(name="QualityMetamodel::RealValueType")
QualityMetamodel_BooleanValueType = Class(name="QualityMetamodel::BooleanValueType")
QualityMetamodel_IntegerValueType = Class(name="QualityMetamodel::IntegerValueType")
QualityMetamodel_ListValue = Class(name="QualityMetamodel::ListValue")
QualityMetamodel_QMM_OCL_LocatedElement = Class(name="QualityMetamodel::QMM::OCL::LocatedElement", is_abstract=True)
QualityMetamodel_QMM_OCL_NamedElement = Class(name="QualityMetamodel::QMM::OCL::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
QualityMetamodel_QMM_OCL_Module = Class(name="QualityMetamodel::QMM::OCL::Module")
NamedElement = Class(name="NamedElement")
OclMetamodel = Class(name="OclMetamodel")
Import = Class(name="Import")
ModuleElement = Class(name="ModuleElement")
LocalVariable = Class(name="LocalVariable")
QualityMetamodel_QMM_OCL_Import = Class(name="QualityMetamodel::QMM::OCL::Import")
QualityMetamodel_QMM_OCL_OclExpression = Class(name="QualityMetamodel::QMM::OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCall = Class(name="OperationCall")
CollectionPart = Class(name="CollectionPart")
QualityMetamodel_QMM_OCL_CollectionPart = Class(name="QualityMetamodel::QMM::OCL::CollectionPart", is_abstract=True)
Operation = Class(name="Operation")
CollectionExp = Class(name="CollectionExp")
QualityMetamodel_QMM_OCL_CollectionRange = Class(name="QualityMetamodel::QMM::OCL::CollectionRange")
Attribute = Class(name="Attribute")
OperatorCallExp = Class(name="OperatorCallExp")
QualityMetamodel_QMM_OCL_CollectionItem = Class(name="QualityMetamodel::QMM::OCL::CollectionItem")
QualityMetamodel_QMM_OCL_VariableExp = Class(name="QualityMetamodel::QMM::OCL::VariableExp")
QualityMetamodel_QMM_OCL_BagExp = Class(name="QualityMetamodel::QMM::OCL::BagExp")
QualityMetamodel_QMM_OCL_OrderedSetExp = Class(name="QualityMetamodel::QMM::OCL::OrderedSetExp")
QualityMetamodel_QMM_OCL_SuperExp = Class(name="QualityMetamodel::QMM::OCL::SuperExp")
QualityMetamodel_QMM_OCL_SequenceExp = Class(name="QualityMetamodel::QMM::OCL::SequenceExp")
QualityMetamodel_QMM_OCL_SelfExp = Class(name="QualityMetamodel::QMM::OCL::SelfExp")
QualityMetamodel_QMM_OCL_SetExp = Class(name="QualityMetamodel::QMM::OCL::SetExp")
QualityMetamodel_QMM_OCL_EnvExp = Class(name="QualityMetamodel::QMM::OCL::EnvExp")
QualityMetamodel_QMM_OCL_PrimitiveExp = Class(name="QualityMetamodel::QMM::OCL::PrimitiveExp", is_abstract=True)
QualityMetamodel_QMM_OCL_StringExp = Class(name="QualityMetamodel::QMM::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
QualityMetamodel_QMM_OCL_BooleanExp = Class(name="QualityMetamodel::QMM::OCL::BooleanExp")
QualityMetamodel_QMM_OCL_NumericExp = Class(name="QualityMetamodel::QMM::OCL::NumericExp", is_abstract=True)
QualityMetamodel_QMM_OCL_RealExp = Class(name="QualityMetamodel::QMM::OCL::RealExp")
NumericExp = Class(name="NumericExp")
QualityMetamodel_QMM_OCL_IntegerExp = Class(name="QualityMetamodel::QMM::OCL::IntegerExp")
QualityMetamodel_QMM_OCL_CollectionExp = Class(name="QualityMetamodel::QMM::OCL::CollectionExp", is_abstract=True)
QualityMetamodel_QMM_OCL_EnumLiteralExp = Class(name="QualityMetamodel::QMM::OCL::EnumLiteralExp")
QualityMetamodel_QMM_OCL_OclUndefinedExp = Class(name="QualityMetamodel::QMM::OCL::OclUndefinedExp")
QualityMetamodel_QMM_OCL_StaticPropertyCallExp = Class(name="QualityMetamodel::QMM::OCL::StaticPropertyCallExp")
StaticPropertyCall = Class(name="StaticPropertyCall")
QualityMetamodel_QMM_OCL_StaticPropertyCall = Class(name="QualityMetamodel::QMM::OCL::StaticPropertyCall", is_abstract=True)
StaticPropertyCallExp = Class(name="StaticPropertyCallExp")
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall = Class(name="QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_TupleExp = Class(name="QualityMetamodel::QMM::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
QualityMetamodel_QMM_OCL_TuplePart = Class(name="QualityMetamodel::QMM::OCL::TuplePart")
TupleExp = Class(name="TupleExp")
QualityMetamodel_QMM_OCL_MapExp = Class(name="QualityMetamodel::QMM::OCL::MapExp")
MapElement = Class(name="MapElement")
QualityMetamodel_QMM_OCL_MapElement = Class(name="QualityMetamodel::QMM::OCL::MapElement")
MapExp = Class(name="MapExp")
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall = Class(name="QualityMetamodel::QMM::OCL::NavigationOrAttributeCall")
QualityMetamodel_QMM_OCL_OperationCall = Class(name="QualityMetamodel::QMM::OCL::OperationCall")
QualityMetamodel_QMM_OCL_OperatorCallExp = Class(name="QualityMetamodel::QMM::OCL::OperatorCallExp")
QualityMetamodel_QMM_OCL_StaticOperationCall = Class(name="QualityMetamodel::QMM::OCL::StaticOperationCall")
QualityMetamodel_QMM_OCL_PropertyCallExp = Class(name="QualityMetamodel::QMM::OCL::PropertyCallExp")
PropertyCall = Class(name="PropertyCall")
QualityMetamodel_QMM_OCL_PropertyCall = Class(name="QualityMetamodel::QMM::OCL::PropertyCall", is_abstract=True)
QualityMetamodel_QMM_OCL_CollectionOperationCall = Class(name="QualityMetamodel::QMM::OCL::CollectionOperationCall")
QualityMetamodel_QMM_OCL_LoopExp = Class(name="QualityMetamodel::QMM::OCL::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
QualityMetamodel_QMM_OCL_IterateExp = Class(name="QualityMetamodel::QMM::OCL::IterateExp")
QualityMetamodel_QMM_OCL_IteratorExp = Class(name="QualityMetamodel::QMM::OCL::IteratorExp")
QualityMetamodel_QMM_OCL_LetExp = Class(name="QualityMetamodel::QMM::OCL::LetExp")
QualityMetamodel_QMM_OCL_NotOpCallExp = Class(name="QualityMetamodel::QMM::OCL::NotOpCallExp")
QualityMetamodel_QMM_OCL_RelOpCallExp = Class(name="QualityMetamodel::QMM::OCL::RelOpCallExp")
QualityMetamodel_QMM_OCL_EqOpCallExp = Class(name="QualityMetamodel::QMM::OCL::EqOpCallExp")
QualityMetamodel_QMM_OCL_AddOpCallExp = Class(name="QualityMetamodel::QMM::OCL::AddOpCallExp")
QualityMetamodel_QMM_OCL_IntOpCallExp = Class(name="QualityMetamodel::QMM::OCL::IntOpCallExp")
QualityMetamodel_QMM_OCL_IfExp = Class(name="QualityMetamodel::QMM::OCL::IfExp")
QualityMetamodel_QMM_OCL_MulOpCallExp = Class(name="QualityMetamodel::QMM::OCL::MulOpCallExp")
QualityMetamodel_QMM_OCL_LambdaCallExp = Class(name="QualityMetamodel::QMM::OCL::LambdaCallExp")
VariableExp = Class(name="VariableExp")
QualityMetamodel_QMM_OCL_BraceExp = Class(name="QualityMetamodel::QMM::OCL::BraceExp")
OclContextDefinition = Class(name="OclContextDefinition")
QualityMetamodel_QMM_OCL_VariableDeclaration = Class(name="QualityMetamodel::QMM::OCL::VariableDeclaration", is_abstract=True)
QualityMetamodel_QMM_OCL_LocalVariable = Class(name="QualityMetamodel::QMM::OCL::LocalVariable")
IterateExp = Class(name="IterateExp")
QualityMetamodel_QMM_OCL_Iterator = Class(name="QualityMetamodel::QMM::OCL::Iterator")
QualityMetamodel_QMM_OCL_Parameter = Class(name="QualityMetamodel::QMM::OCL::Parameter")
QualityMetamodel_QMM_OCL_CollectionType = Class(name="QualityMetamodel::QMM::OCL::CollectionType")
QualityMetamodel_QMM_OCL_OclType = Class(name="QualityMetamodel::QMM::OCL::OclType")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
QualityMetamodel_QMM_OCL_BooleanType = Class(name="QualityMetamodel::QMM::OCL::BooleanType")
QualityMetamodel_QMM_OCL_NumericType = Class(name="QualityMetamodel::QMM::OCL::NumericType", is_abstract=True)
QualityMetamodel_QMM_OCL_IntegerType = Class(name="QualityMetamodel::QMM::OCL::IntegerType")
NumericType = Class(name="NumericType")
LambdaType = Class(name="LambdaType")
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
QualityMetamodel_QMM_OCL_OclModelElementExp = Class(name="QualityMetamodel::QMM::OCL::OclModelElementExp")
OclModel = Class(name="OclModel")
QualityMetamodel_QMM_OCL_Primitive = Class(name="QualityMetamodel::QMM::OCL::Primitive", is_abstract=True)
QualityMetamodel_QMM_OCL_StringType = Class(name="QualityMetamodel::QMM::OCL::StringType")
Primitive = Class(name="Primitive")
QualityMetamodel_QMM_OCL_EnvType = Class(name="QualityMetamodel::QMM::OCL::EnvType")
QualityMetamodel_QMM_OCL_OclFeatureDefinition = Class(name="QualityMetamodel::QMM::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
QualityMetamodel_QMM_OCL_OclContextDefinition = Class(name="QualityMetamodel::QMM::OCL::OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
QualityMetamodel_QMM_OCL_OclFeature = Class(name="QualityMetamodel::QMM::OCL::OclFeature", is_abstract=True)
QualityMetamodel_QMM_OCL_Attribute = Class(name="QualityMetamodel::QMM::OCL::Attribute")
QualityMetamodel_QMM_OCL_MapType = Class(name="QualityMetamodel::QMM::OCL::MapType")
QualityMetamodel_QMM_OCL_LambdaType = Class(name="QualityMetamodel::QMM::OCL::LambdaType")
QualityMetamodel_QMM_OCL_OclModel = Class(name="QualityMetamodel::QMM::OCL::OclModel", is_abstract=True)
OclModelElement = Class(name="OclModelElement")
QualityMetamodel_QMM_OCL_OclMetamodel = Class(name="QualityMetamodel::QMM::OCL::OclMetamodel")
OclInstanceModel = Class(name="OclInstanceModel")
QualityMetamodel_QMM_OCL_OclInstanceModel = Class(name="QualityMetamodel::QMM::OCL::OclInstanceModel")
QualityMetamodel_QMM_OCL_Operation = Class(name="QualityMetamodel::QMM::OCL::Operation")
Parameter_ = Class(name="Parameter")

# QualityMetamodel_QualityModel class attributes and methods

# Module class attributes and methods

# QualityMetamodel_MetricProvider class attributes and methods
QualityMetamodel_MetricProvider_name: Property = Property(name="name", type=StringType)
QualityMetamodel_MetricProvider_description: Property = Property(name="description", type=StringType)
QualityMetamodel_MetricProvider_id: Property = Property(name="id", type=StringType)
QualityMetamodel_MetricProvider.attributes={QualityMetamodel_MetricProvider_id, QualityMetamodel_MetricProvider_description, QualityMetamodel_MetricProvider_name}

# QualityMetamodel_ValueType class attributes and methods

# QualityMetamodel_QualityAttribute class attributes and methods

# QualityMetamodel_Value class attributes and methods
QualityMetamodel_Value_description: Property = Property(name="description", type=StringType)
QualityMetamodel_Value.attributes={QualityMetamodel_Value_description}

# VariableDeclaration class attributes and methods

# QualityMetamodel_EnumerationMetric class attributes and methods

# QualityMetamodel_EnumerationItem class attributes and methods
QualityMetamodel_EnumerationItem_name: Property = Property(name="name", type=StringType)
QualityMetamodel_EnumerationItem.attributes={QualityMetamodel_EnumerationItem_name}

# QualityMetamodel_SingleValue class attributes and methods

# Value class attributes and methods

# QualityMetamodel_AggregatedValue class attributes and methods

# QualityMetamodel_Operation class attributes and methods
QualityMetamodel_Operation_name: Property = Property(name="name", type=StringType)
QualityMetamodel_Operation_body: Property = Property(name="body", type=StringType)
QualityMetamodel_Operation.attributes={QualityMetamodel_Operation_body, QualityMetamodel_Operation_name}

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
QualityMetamodel_AggregatedValueMetric_standardDeviation: Property = Property(name="standardDeviation", type=StringType)
QualityMetamodel_AggregatedValueMetric_minimum: Property = Property(name="minimum", type=StringType)
QualityMetamodel_AggregatedValueMetric_maximum: Property = Property(name="maximum", type=StringType)
QualityMetamodel_AggregatedValueMetric_average: Property = Property(name="average", type=StringType)
QualityMetamodel_AggregatedValueMetric_median: Property = Property(name="median", type=StringType)
QualityMetamodel_AggregatedValueMetric.attributes={QualityMetamodel_AggregatedValueMetric_minimum, QualityMetamodel_AggregatedValueMetric_average, QualityMetamodel_AggregatedValueMetric_standardDeviation, QualityMetamodel_AggregatedValueMetric_median, QualityMetamodel_AggregatedValueMetric_maximum}

# QualityMetamodel_QMM_OCL_ModuleElement class attributes and methods

# QualityMetamodel_RealValueType class attributes and methods
QualityMetamodel_RealValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_RealValueType.attributes={QualityMetamodel_RealValueType_value}

# QualityMetamodel_BooleanValueType class attributes and methods
QualityMetamodel_BooleanValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_BooleanValueType.attributes={QualityMetamodel_BooleanValueType_value}

# QualityMetamodel_IntegerValueType class attributes and methods
QualityMetamodel_IntegerValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_IntegerValueType.attributes={QualityMetamodel_IntegerValueType_value}

# QualityMetamodel_ListValue class attributes and methods

# QualityMetamodel_QMM_OCL_LocatedElement class attributes and methods
QualityMetamodel_QMM_OCL_LocatedElement_line: Property = Property(name="line", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_column: Property = Property(name="column", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
QualityMetamodel_QMM_OCL_LocatedElement.attributes={QualityMetamodel_QMM_OCL_LocatedElement_charStart, QualityMetamodel_QMM_OCL_LocatedElement_column, QualityMetamodel_QMM_OCL_LocatedElement_line, QualityMetamodel_QMM_OCL_LocatedElement_charEnd}

# QualityMetamodel_QMM_OCL_NamedElement class attributes and methods
QualityMetamodel_QMM_OCL_NamedElement_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_NamedElement.attributes={QualityMetamodel_QMM_OCL_NamedElement_name}

# LocatedElement class attributes and methods

# QualityMetamodel_QMM_OCL_Module class attributes and methods

# NamedElement class attributes and methods

# OclMetamodel class attributes and methods

# Import class attributes and methods

# ModuleElement class attributes and methods

# LocalVariable class attributes and methods

# QualityMetamodel_QMM_OCL_Import class attributes and methods

# QualityMetamodel_QMM_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCall class attributes and methods

# CollectionPart class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionPart class attributes and methods

# Operation class attributes and methods

# CollectionExp class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionRange class attributes and methods

# Attribute class attributes and methods

# OperatorCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionItem class attributes and methods

# QualityMetamodel_QMM_OCL_VariableExp class attributes and methods

# QualityMetamodel_QMM_OCL_BagExp class attributes and methods

# QualityMetamodel_QMM_OCL_OrderedSetExp class attributes and methods

# QualityMetamodel_QMM_OCL_SuperExp class attributes and methods

# QualityMetamodel_QMM_OCL_SequenceExp class attributes and methods

# QualityMetamodel_QMM_OCL_SelfExp class attributes and methods

# QualityMetamodel_QMM_OCL_SetExp class attributes and methods

# QualityMetamodel_QMM_OCL_EnvExp class attributes and methods

# QualityMetamodel_QMM_OCL_PrimitiveExp class attributes and methods

# QualityMetamodel_QMM_OCL_StringExp class attributes and methods
QualityMetamodel_QMM_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
QualityMetamodel_QMM_OCL_StringExp.attributes={QualityMetamodel_QMM_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

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

# QualityMetamodel_QMM_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# QualityMetamodel_QMM_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# QualityMetamodel_QMM_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# QualityMetamodel_QMM_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# QualityMetamodel_QMM_OCL_NavigationOrAttributeCall class attributes and methods
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.attributes={QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_name}

# QualityMetamodel_QMM_OCL_OperationCall class attributes and methods
QualityMetamodel_QMM_OCL_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperationCall.attributes={QualityMetamodel_QMM_OCL_OperationCall_operationName}

# QualityMetamodel_QMM_OCL_OperatorCallExp class attributes and methods
QualityMetamodel_QMM_OCL_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_OperatorCallExp.attributes={QualityMetamodel_QMM_OCL_OperatorCallExp_operationName}

# QualityMetamodel_QMM_OCL_StaticOperationCall class attributes and methods
QualityMetamodel_QMM_OCL_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
QualityMetamodel_QMM_OCL_StaticOperationCall.attributes={QualityMetamodel_QMM_OCL_StaticOperationCall_operationName}

# QualityMetamodel_QMM_OCL_PropertyCallExp class attributes and methods

# PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_PropertyCall class attributes and methods

# QualityMetamodel_QMM_OCL_CollectionOperationCall class attributes and methods

# QualityMetamodel_QMM_OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# QualityMetamodel_QMM_OCL_IterateExp class attributes and methods

# QualityMetamodel_QMM_OCL_IteratorExp class attributes and methods
QualityMetamodel_QMM_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_IteratorExp.attributes={QualityMetamodel_QMM_OCL_IteratorExp_name}

# QualityMetamodel_QMM_OCL_LetExp class attributes and methods

# QualityMetamodel_QMM_OCL_NotOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_RelOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_EqOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_AddOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_IntOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_IfExp class attributes and methods

# QualityMetamodel_QMM_OCL_MulOpCallExp class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# QualityMetamodel_QMM_OCL_BraceExp class attributes and methods

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

# QualityMetamodel_QMM_OCL_OclType class attributes and methods
QualityMetamodel_QMM_OCL_OclType_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclType.attributes={QualityMetamodel_QMM_OCL_OclType_name}

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# QualityMetamodel_QMM_OCL_BooleanType class attributes and methods

# QualityMetamodel_QMM_OCL_NumericType class attributes and methods

# QualityMetamodel_QMM_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# LambdaType class attributes and methods

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

# QualityMetamodel_QMM_OCL_OclModelElementExp class attributes and methods
QualityMetamodel_QMM_OCL_OclModelElementExp_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QMM_OCL_OclModelElementExp.attributes={QualityMetamodel_QMM_OCL_OclModelElementExp_name}

# OclModel class attributes and methods

# QualityMetamodel_QMM_OCL_Primitive class attributes and methods

# QualityMetamodel_QMM_OCL_StringType class attributes and methods

# Primitive class attributes and methods

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

# QualityMetamodel_QMM_OCL_MapType class attributes and methods

# QualityMetamodel_QMM_OCL_LambdaType class attributes and methods

# QualityMetamodel_QMM_OCL_OclModel class attributes and methods

# OclModelElement class attributes and methods

# QualityMetamodel_QMM_OCL_OclMetamodel class attributes and methods
QualityMetamodel_QMM_OCL_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
QualityMetamodel_QMM_OCL_OclMetamodel.attributes={QualityMetamodel_QMM_OCL_OclMetamodel_uri}

# OclInstanceModel class attributes and methods

# QualityMetamodel_QMM_OCL_OclInstanceModel class attributes and methods

# QualityMetamodel_QMM_OCL_Operation class attributes and methods

# Parameter class attributes and methods

# Relationships
qualityAttributes11: BinaryAssociation = BinaryAssociation(
    name="qualityAttributes11",
    ends={
        Property(name="QualityMetamodel_QualityAttribute12", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityAttribute10", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(0, 9999))
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
set23: BinaryAssociation = BinaryAssociation(
    name="set23",
    ends={
        Property(name="QualityMetamodel_EnumerationItem", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="QualityMetamodel_EnumerationItem26", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric25", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(0, 1))
    }
)
elements27: BinaryAssociation = BinaryAssociation(
    name="elements27",
    ends={
        Property(name="QualityMetamodel_ValueType28", type=QualityMetamodel_ListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_ListValue", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
metamodels29: BinaryAssociation = BinaryAssociation(
    name="metamodels29",
    ends={
        Property(name="OclMetamodel", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_Module", type=OclMetamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports30: BinaryAssociation = BinaryAssociation(
    name="imports30",
    ends={
        Property(name="QMM_OCL", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="Import", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="QMM_OCL32", type=QualityMetamodel_QMM_OCL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ModuleElement", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedVariable50: BinaryAssociation = BinaryAssociation(
    name="initializedVariable50",
    ends={
        Property(name="QMM_OCL51", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp252: BinaryAssociation = BinaryAssociation(
    name="ifExp252",
    ends={
        Property(name="QMM_OCL54", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp53", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
module33: BinaryAssociation = BinaryAssociation(
    name="module33",
    ends={
        Property(name="QMM_OCL34", type=QualityMetamodel_QMM_OCL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Module", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module35: BinaryAssociation = BinaryAssociation(
    name="module35",
    ends={
        Property(name="QMM_OCL37", type=QualityMetamodel_QMM_OCL_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="Module36", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="QMM_OCL39", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp340: BinaryAssociation = BinaryAssociation(
    name="ifExp340",
    ends={
        Property(name="QMM_OCL41", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty42: BinaryAssociation = BinaryAssociation(
    name="appliedProperty42",
    ends={
        Property(name="QMM_OCL43", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp44: BinaryAssociation = BinaryAssociation(
    name="letExp44",
    ends={
        Property(name="QMM_OCL45", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp46: BinaryAssociation = BinaryAssociation(
    name="loopExp46",
    ends={
        Property(name="QMM_OCL47", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation48: BinaryAssociation = BinaryAssociation(
    name="parentOperation48",
    ends={
        Property(name="QMM_OCL49", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCall", type=OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
parts66: BinaryAssociation = BinaryAssociation(
    name="parts66",
    ends={
        Property(name="QMM_OCL67", type=QualityMetamodel_QMM_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionPart", type=CollectionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperation55: BinaryAssociation = BinaryAssociation(
    name="owningOperation55",
    ends={
        Property(name="QMM_OCL56", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
collection68: BinaryAssociation = BinaryAssociation(
    name="collection68",
    ends={
        Property(name="QMM_OCL69", type=QualityMetamodel_QMM_OCL_CollectionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
ifExp157: BinaryAssociation = BinaryAssociation(
    name="ifExp157",
    ends={
        Property(name="QMM_OCL59", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp58", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
first70: BinaryAssociation = BinaryAssociation(
    name="first70",
    ends={
        Property(name="OclExpression71", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningAttribute60: BinaryAssociation = BinaryAssociation(
    name="owningAttribute60",
    ends={
        Property(name="QMM_OCL61", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
last72: BinaryAssociation = BinaryAssociation(
    name="last72",
    ends={
        Property(name="OclExpression74", type=QualityMetamodel_QMM_OCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionRange73", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
appliedOperator62: BinaryAssociation = BinaryAssociation(
    name="appliedOperator62",
    ends={
        Property(name="QMM_OCL63", type=QualityMetamodel_QMM_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperatorCallExp", type=OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
item75: BinaryAssociation = BinaryAssociation(
    name="item75",
    ends={
        Property(name="OclExpression76", type=QualityMetamodel_QMM_OCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable64: BinaryAssociation = BinaryAssociation(
    name="referredVariable64",
    ends={
        Property(name="QMM_OCL65", type=QualityMetamodel_QMM_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
key85: BinaryAssociation = BinaryAssociation(
    name="key85",
    ends={
        Property(name="OclExpression86", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value87: BinaryAssociation = BinaryAssociation(
    name="value87",
    ends={
        Property(name="OclExpression89", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_MapElement88", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source90: BinaryAssociation = BinaryAssociation(
    name="source90",
    ends={
        Property(name="QMM_OCL92", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType91", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall93: BinaryAssociation = BinaryAssociation(
    name="staticCall93",
    ends={
        Property(name="QMM_OCL94", type=QualityMetamodel_QMM_OCL_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCall", type=StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp95: BinaryAssociation = BinaryAssociation(
    name="staticCallExp95",
    ends={
        Property(name="QMM_OCL96", type=QualityMetamodel_QMM_OCL_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp", type=StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
tuplePart77: BinaryAssociation = BinaryAssociation(
    name="tuplePart77",
    ends={
        Property(name="QMM_OCL78", type=QualityMetamodel_QMM_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple79: BinaryAssociation = BinaryAssociation(
    name="tuple79",
    ends={
        Property(name="QMM_OCL80", type=QualityMetamodel_QMM_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements81: BinaryAssociation = BinaryAssociation(
    name="elements81",
    ends={
        Property(name="QMM_OCL82", type=QualityMetamodel_QMM_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map83: BinaryAssociation = BinaryAssociation(
    name="map83",
    ends={
        Property(name="QMM_OCL84", type=QualityMetamodel_QMM_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
callExp104: BinaryAssociation = BinaryAssociation(
    name="callExp104",
    ends={
        Property(name="QMM_OCL106", type=QualityMetamodel_QMM_OCL_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp105", type=PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments107: BinaryAssociation = BinaryAssociation(
    name="arguments107",
    ends={
        Property(name="QMM_OCL109", type=QualityMetamodel_QMM_OCL_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression108", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument110: BinaryAssociation = BinaryAssociation(
    name="argument110",
    ends={
        Property(name="OclExpression111", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source112: BinaryAssociation = BinaryAssociation(
    name="source112",
    ends={
        Property(name="QMM_OCL114", type=QualityMetamodel_QMM_OCL_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression113", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments97: BinaryAssociation = BinaryAssociation(
    name="arguments97",
    ends={
        Property(name="OclExpression98", type=QualityMetamodel_QMM_OCL_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_StaticOperationCall", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls99: BinaryAssociation = BinaryAssociation(
    name="calls99",
    ends={
        Property(name="QMM_OCL100", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCall", type=PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source101: BinaryAssociation = BinaryAssociation(
    name="source101",
    ends={
        Property(name="QMM_OCL103", type=QualityMetamodel_QMM_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression102", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body119: BinaryAssociation = BinaryAssociation(
    name="body119",
    ends={
        Property(name="QMM_OCL121", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression120", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators122: BinaryAssociation = BinaryAssociation(
    name="iterators122",
    ends={
        Property(name="QMM_OCL123", type=QualityMetamodel_QMM_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result124: BinaryAssociation = BinaryAssociation(
    name="result124",
    ends={
        Property(name="QMM_OCL126", type=QualityMetamodel_QMM_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable125", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable127: BinaryAssociation = BinaryAssociation(
    name="variable127",
    ends={
        Property(name="QMM_OCL129", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable128", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_130: BinaryAssociation = BinaryAssociation(
    name="in_130",
    ends={
        Property(name="QMM_OCL132", type=QualityMetamodel_QMM_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression131", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression133: BinaryAssociation = BinaryAssociation(
    name="thenExpression133",
    ends={
        Property(name="QMM_OCL135", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression134", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments115: BinaryAssociation = BinaryAssociation(
    name="arguments115",
    ends={
        Property(name="OclExpression116", type=QualityMetamodel_QMM_OCL_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_LambdaCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition136: BinaryAssociation = BinaryAssociation(
    name="condition136",
    ends={
        Property(name="QMM_OCL138", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression137", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp117: BinaryAssociation = BinaryAssociation(
    name="exp117",
    ends={
        Property(name="OclExpression118", type=QualityMetamodel_QMM_OCL_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_BraceExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression139: BinaryAssociation = BinaryAssociation(
    name="elseExpression139",
    ends={
        Property(name="QMM_OCL141", type=QualityMetamodel_QMM_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression140", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions164: BinaryAssociation = BinaryAssociation(
    name="definitions164",
    ends={
        Property(name="QMM_OCL165", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression166: BinaryAssociation = BinaryAssociation(
    name="oclExpression166",
    ends={
        Property(name="QMM_OCL168", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression167", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="QMM_OCL144", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType143", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp145: BinaryAssociation = BinaryAssociation(
    name="variableExp145",
    ends={
        Property(name="QMM_OCL146", type=QualityMetamodel_QMM_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp147: BinaryAssociation = BinaryAssociation(
    name="letExp147",
    ends={
        Property(name="QMM_OCL149", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp148", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression150: BinaryAssociation = BinaryAssociation(
    name="initExpression150",
    ends={
        Property(name="QMM_OCL152", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression151", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp153: BinaryAssociation = BinaryAssociation(
    name="baseExp153",
    ends={
        Property(name="QMM_OCL154", type=QualityMetamodel_QMM_OCL_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr155: BinaryAssociation = BinaryAssociation(
    name="loopExpr155",
    ends={
        Property(name="QMM_OCL157", type=QualityMetamodel_QMM_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp156", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation158: BinaryAssociation = BinaryAssociation(
    name="operation158",
    ends={
        Property(name="QMM_OCL160", type=QualityMetamodel_QMM_OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation159", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType161: BinaryAssociation = BinaryAssociation(
    name="elementType161",
    ends={
        Property(name="QMM_OCL163", type=QualityMetamodel_QMM_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType162", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation169: BinaryAssociation = BinaryAssociation(
    name="operation169",
    ends={
        Property(name="QMM_OCL171", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation170", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2172: BinaryAssociation = BinaryAssociation(
    name="mapType2172",
    ends={
        Property(name="QMM_OCL173", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute174: BinaryAssociation = BinaryAssociation(
    name="attribute174",
    ends={
        Property(name="QMM_OCL176", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute175", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType177: BinaryAssociation = BinaryAssociation(
    name="mapType177",
    ends={
        Property(name="QMM_OCL179", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType178", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes180: BinaryAssociation = BinaryAssociation(
    name="collectionTypes180",
    ends={
        Property(name="QMM_OCL181", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute182: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute182",
    ends={
        Property(name="QMM_OCL183", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration184: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration184",
    ends={
        Property(name="QMM_OCL186", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration185", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lambdaReturnType187: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType187",
    ends={
        Property(name="QMM_OCL188", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
attributes196: BinaryAssociation = BinaryAssociation(
    name="attributes196",
    ends={
        Property(name="QMM_OCL198", type=QualityMetamodel_QMM_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute197", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type199: BinaryAssociation = BinaryAssociation(
    name="type199",
    ends={
        Property(name="QMM_OCL201", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType200", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType202: BinaryAssociation = BinaryAssociation(
    name="tupleType202",
    ends={
        Property(name="QMM_OCL203", type=QualityMetamodel_QMM_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model204: BinaryAssociation = BinaryAssociation(
    name="model204",
    ends={
        Property(name="QMM_OCL206", type=QualityMetamodel_QMM_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel205", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
lambdaArgType189: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType189",
    ends={
        Property(name="QMM_OCL191", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType190", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
staticPropertyCall192: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall192",
    ends={
        Property(name="QMM_OCL194", type=QualityMetamodel_QMM_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp193", type=StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
model195: BinaryAssociation = BinaryAssociation(
    name="model195",
    ends={
        Property(name="OclModel", type=QualityMetamodel_QMM_OCL_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QMM_OCL_OclModelElementExp", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
argumentTypes216: BinaryAssociation = BinaryAssociation(
    name="argumentTypes216",
    ends={
        Property(name="QMM_OCL218", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType217", type=OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature219: BinaryAssociation = BinaryAssociation(
    name="feature219",
    ends={
        Property(name="QMM_OCL220", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_221: BinaryAssociation = BinaryAssociation(
    name="context_221",
    ends={
        Property(name="QMM_OCL223", type=QualityMetamodel_QMM_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition222", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition224: BinaryAssociation = BinaryAssociation(
    name="definition224",
    ends={
        Property(name="QMM_OCL225", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_226: BinaryAssociation = BinaryAssociation(
    name="context_226",
    ends={
        Property(name="QMM_OCL228", type=QualityMetamodel_QMM_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType227", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition229: BinaryAssociation = BinaryAssociation(
    name="definition229",
    ends={
        Property(name="QMM_OCL231", type=QualityMetamodel_QMM_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition230", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
valueType207: BinaryAssociation = BinaryAssociation(
    name="valueType207",
    ends={
        Property(name="QMM_OCL209", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType208", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType210: BinaryAssociation = BinaryAssociation(
    name="keyType210",
    ends={
        Property(name="QMM_OCL212", type=QualityMetamodel_QMM_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType211", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType213: BinaryAssociation = BinaryAssociation(
    name="returnType213",
    ends={
        Property(name="QMM_OCL215", type=QualityMetamodel_QMM_OCL_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType214", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body243: BinaryAssociation = BinaryAssociation(
    name="body243",
    ends={
        Property(name="QMM_OCL245", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression244", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements246: BinaryAssociation = BinaryAssociation(
    name="elements246",
    ends={
        Property(name="QMM_OCL247", type=QualityMetamodel_QMM_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model248: BinaryAssociation = BinaryAssociation(
    name="model248",
    ends={
        Property(name="QMM_OCL249", type=QualityMetamodel_QMM_OCL_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclInstanceModel", type=OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel250: BinaryAssociation = BinaryAssociation(
    name="metamodel250",
    ends={
        Property(name="QMM_OCL252", type=QualityMetamodel_QMM_OCL_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclMetamodel251", type=OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)
initExpression232: BinaryAssociation = BinaryAssociation(
    name="initExpression232",
    ends={
        Property(name="QMM_OCL234", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression233", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type235: BinaryAssociation = BinaryAssociation(
    name="type235",
    ends={
        Property(name="QMM_OCL237", type=QualityMetamodel_QMM_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType236", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters238: BinaryAssociation = BinaryAssociation(
    name="parameters238",
    ends={
        Property(name="QMM_OCL239", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType240: BinaryAssociation = BinaryAssociation(
    name="returnType240",
    ends={
        Property(name="QMM_OCL242", type=QualityMetamodel_QMM_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType241", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_QualityMetamodel_QualityModel_Module = Generalization(general=Module, specific=QualityMetamodel_QualityModel)
gen_QualityMetamodel_QualityAttribute_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QualityAttribute)
gen_QualityMetamodel_EnumerationMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_EnumerationMetric)
gen_QualityMetamodel_Value_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_Value)
gen_QualityMetamodel_ValueType_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_ValueType)
gen_QualityMetamodel_SingleValue_Value = Generalization(general=Value, specific=QualityMetamodel_SingleValue)
gen_QualityMetamodel_AggregatedValue_Value = Generalization(general=Value, specific=QualityMetamodel_AggregatedValue)
gen_QualityMetamodel_TextValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_TextValueType)
gen_QualityMetamodel_RangeValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RangeValueType)
gen_QualityMetamodel_AggregatedValueMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_AggregatedValueMetric)
gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_ModuleElement)
gen_QualityMetamodel_RealValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RealValueType)
gen_QualityMetamodel_BooleanValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_BooleanValueType)
gen_QualityMetamodel_IntegerValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_IntegerValueType)
gen_QualityMetamodel_ListValue_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_ListValue)
gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_NamedElement)
gen_QualityMetamodel_QMM_OCL_Module_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Module)
gen_QualityMetamodel_QMM_OCL_Import_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_Import)
gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclExpression)
gen_QualityMetamodel_QMM_OCL_CollectionPart_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_CollectionPart)
gen_QualityMetamodel_QMM_OCL_CollectionRange_CollectionPart = Generalization(general=CollectionPart, specific=QualityMetamodel_QMM_OCL_CollectionRange)
gen_QualityMetamodel_QMM_OCL_CollectionItem_CollectionPart = Generalization(general=CollectionPart, specific=QualityMetamodel_QMM_OCL_CollectionItem)
gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_VariableExp)
gen_QualityMetamodel_QMM_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_BagExp)
gen_QualityMetamodel_QMM_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_OrderedSetExp)
gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SuperExp)
gen_QualityMetamodel_QMM_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_SequenceExp)
gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_SelfExp)
gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnvExp)
gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PrimitiveExp)
gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_StringExp)
gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_BooleanExp)
gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=QualityMetamodel_QMM_OCL_NumericExp)
gen_QualityMetamodel_QMM_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=QualityMetamodel_QMM_OCL_RealExp)
gen_QualityMetamodel_QMM_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=QualityMetamodel_QMM_OCL_IntegerExp)
gen_QualityMetamodel_QMM_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_CollectionExp)
gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_EnumLiteralExp)
gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclUndefinedExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_StaticPropertyCallExp)
gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_StaticPropertyCall)
gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=QualityMetamodel_QMM_OCL_SetExp)
gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_TupleExp)
gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=QualityMetamodel_QMM_OCL_TuplePart)
gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_MapExp)
gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_MapElement)
gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_NavigationOrAttributeCall)
gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_OperationCall)
gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OperatorCallExp)
gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=QualityMetamodel_QMM_OCL_StaticOperationCall)
gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_PropertyCallExp)
gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_PropertyCall)
gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=QualityMetamodel_QMM_OCL_CollectionOperationCall)
gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=QualityMetamodel_QMM_OCL_LoopExp)
gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IterateExp)
gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=QualityMetamodel_QMM_OCL_IteratorExp)
gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_LetExp)
gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_NotOpCallExp)
gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_RelOpCallExp)
gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_EqOpCallExp)
gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_AddOpCallExp)
gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_IntOpCallExp)
gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_IfExp)
gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=QualityMetamodel_QMM_OCL_MulOpCallExp)
gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=QualityMetamodel_QMM_OCL_LambdaCallExp)
gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_BraceExp)
gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_VariableDeclaration)
gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_LocalVariable)
gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Iterator)
gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=QualityMetamodel_QMM_OCL_Parameter)
gen_QualityMetamodel_QMM_OCL_CollectionType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_CollectionType)
gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclType)
gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_BooleanType)
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
gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=QualityMetamodel_QMM_OCL_OclModelElementExp)
gen_QualityMetamodel_QMM_OCL_Primitive_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_Primitive)
gen_QualityMetamodel_QMM_OCL_StringType_Primitive = Generalization(general=Primitive, specific=QualityMetamodel_QMM_OCL_StringType)
gen_QualityMetamodel_QMM_OCL_EnvType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_EnvType)
gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=QualityMetamodel_QMM_OCL_OclFeatureDefinition)
gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=QualityMetamodel_QMM_OCL_OclContextDefinition)
gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclFeature)
gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Attribute)
gen_QualityMetamodel_QMM_OCL_MapType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_MapType)
gen_QualityMetamodel_QMM_OCL_LambdaType_OclType = Generalization(general=OclType, specific=QualityMetamodel_QMM_OCL_LambdaType)
gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement = Generalization(general=NamedElement, specific=QualityMetamodel_QMM_OCL_OclModel)
gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclMetamodel)
gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=QualityMetamodel_QMM_OCL_OclInstanceModel)
gen_QualityMetamodel_QMM_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=QualityMetamodel_QMM_OCL_Operation)

# Domain Model
domain_model = DomainModel(
    name="QualityMetamodel",
    types={QualityMetamodel_QualityModel, Module, QualityMetamodel_MetricProvider, QualityMetamodel_ValueType, QualityMetamodel_QualityAttribute, QualityMetamodel_Value, VariableDeclaration, QualityMetamodel_EnumerationMetric, QualityMetamodel_EnumerationItem, QualityMetamodel_SingleValue, Value, QualityMetamodel_AggregatedValue, QualityMetamodel_Operation, OclExpression, QualityMetamodel_TextValueType, ValueType, QualityMetamodel_RangeValueType, QualityMetamodel_AggregatedValueMetric, QualityMetamodel_QMM_OCL_ModuleElement, QualityMetamodel_RealValueType, QualityMetamodel_BooleanValueType, QualityMetamodel_IntegerValueType, QualityMetamodel_ListValue, QualityMetamodel_QMM_OCL_LocatedElement, QualityMetamodel_QMM_OCL_NamedElement, LocatedElement, QualityMetamodel_QMM_OCL_Module, NamedElement, OclMetamodel, Import, ModuleElement, LocalVariable, QualityMetamodel_QMM_OCL_Import, QualityMetamodel_QMM_OCL_OclExpression, OclType, IfExp, PropertyCallExp, LetExp, LoopExp, OperationCall, CollectionPart, QualityMetamodel_QMM_OCL_CollectionPart, Operation, CollectionExp, QualityMetamodel_QMM_OCL_CollectionRange, Attribute, OperatorCallExp, QualityMetamodel_QMM_OCL_CollectionItem, QualityMetamodel_QMM_OCL_VariableExp, QualityMetamodel_QMM_OCL_BagExp, QualityMetamodel_QMM_OCL_OrderedSetExp, QualityMetamodel_QMM_OCL_SuperExp, QualityMetamodel_QMM_OCL_SequenceExp, QualityMetamodel_QMM_OCL_SelfExp, QualityMetamodel_QMM_OCL_SetExp, QualityMetamodel_QMM_OCL_EnvExp, QualityMetamodel_QMM_OCL_PrimitiveExp, QualityMetamodel_QMM_OCL_StringExp, PrimitiveExp, QualityMetamodel_QMM_OCL_BooleanExp, QualityMetamodel_QMM_OCL_NumericExp, QualityMetamodel_QMM_OCL_RealExp, NumericExp, QualityMetamodel_QMM_OCL_IntegerExp, QualityMetamodel_QMM_OCL_CollectionExp, QualityMetamodel_QMM_OCL_EnumLiteralExp, QualityMetamodel_QMM_OCL_OclUndefinedExp, QualityMetamodel_QMM_OCL_StaticPropertyCallExp, StaticPropertyCall, QualityMetamodel_QMM_OCL_StaticPropertyCall, StaticPropertyCallExp, QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall, QualityMetamodel_QMM_OCL_TupleExp, TuplePart, QualityMetamodel_QMM_OCL_TuplePart, TupleExp, QualityMetamodel_QMM_OCL_MapExp, MapElement, QualityMetamodel_QMM_OCL_MapElement, MapExp, QualityMetamodel_QMM_OCL_NavigationOrAttributeCall, QualityMetamodel_QMM_OCL_OperationCall, QualityMetamodel_QMM_OCL_OperatorCallExp, QualityMetamodel_QMM_OCL_StaticOperationCall, QualityMetamodel_QMM_OCL_PropertyCallExp, PropertyCall, QualityMetamodel_QMM_OCL_PropertyCall, QualityMetamodel_QMM_OCL_CollectionOperationCall, QualityMetamodel_QMM_OCL_LoopExp, Iterator, QualityMetamodel_QMM_OCL_IterateExp, QualityMetamodel_QMM_OCL_IteratorExp, QualityMetamodel_QMM_OCL_LetExp, QualityMetamodel_QMM_OCL_NotOpCallExp, QualityMetamodel_QMM_OCL_RelOpCallExp, QualityMetamodel_QMM_OCL_EqOpCallExp, QualityMetamodel_QMM_OCL_AddOpCallExp, QualityMetamodel_QMM_OCL_IntOpCallExp, QualityMetamodel_QMM_OCL_IfExp, QualityMetamodel_QMM_OCL_MulOpCallExp, QualityMetamodel_QMM_OCL_LambdaCallExp, VariableExp, QualityMetamodel_QMM_OCL_BraceExp, OclContextDefinition, QualityMetamodel_QMM_OCL_VariableDeclaration, QualityMetamodel_QMM_OCL_LocalVariable, IterateExp, QualityMetamodel_QMM_OCL_Iterator, QualityMetamodel_QMM_OCL_Parameter, QualityMetamodel_QMM_OCL_CollectionType, QualityMetamodel_QMM_OCL_OclType, MapType, CollectionType, TupleTypeAttribute, QualityMetamodel_QMM_OCL_BooleanType, QualityMetamodel_QMM_OCL_NumericType, QualityMetamodel_QMM_OCL_IntegerType, NumericType, LambdaType, QualityMetamodel_QMM_OCL_RealType, QualityMetamodel_QMM_OCL_BagType, QualityMetamodel_QMM_OCL_OrderedSetType, QualityMetamodel_QMM_OCL_SequenceType, QualityMetamodel_QMM_OCL_SetType, QualityMetamodel_QMM_OCL_OclAnyType, QualityMetamodel_QMM_OCL_TupleType, QualityMetamodel_QMM_OCL_TupleTypeAttribute, TupleType, QualityMetamodel_QMM_OCL_OclModelElement, QualityMetamodel_QMM_OCL_OclModelElementExp, OclModel, QualityMetamodel_QMM_OCL_Primitive, QualityMetamodel_QMM_OCL_StringType, Primitive, QualityMetamodel_QMM_OCL_EnvType, QualityMetamodel_QMM_OCL_OclFeatureDefinition, OclFeature, QualityMetamodel_QMM_OCL_OclContextDefinition, OclFeatureDefinition, QualityMetamodel_QMM_OCL_OclFeature, QualityMetamodel_QMM_OCL_Attribute, QualityMetamodel_QMM_OCL_MapType, QualityMetamodel_QMM_OCL_LambdaType, QualityMetamodel_QMM_OCL_OclModel, OclModelElement, QualityMetamodel_QMM_OCL_OclMetamodel, OclInstanceModel, QualityMetamodel_QMM_OCL_OclInstanceModel, QualityMetamodel_QMM_OCL_Operation, Parameter_},
    associations={qualityAttributes11, metricProviders0, qualityTypes1, qualityAttributes3, qualityValues5, value7, set23, valueType13, val14, measuredBy15, calculatedBy17, aggregatedValues18, ref21, value24, elements27, metamodels29, imports30, elements31, initializedVariable50, ifExp252, module33, module35, type38, ifExp340, appliedProperty42, letExp44, loopExp46, parentOperation48, parts66, owningOperation55, collection68, ifExp157, first70, owningAttribute60, last72, appliedOperator62, item75, referredVariable64, key85, value87, source90, staticCall93, staticCallExp95, tuplePart77, tuple79, elements81, map83, callExp104, arguments107, argument110, source112, arguments97, calls99, source101, body119, iterators122, result124, variable127, in_130, thenExpression133, arguments115, condition136, exp117, elseExpression139, definitions164, oclExpression166, type142, variableExp145, letExp147, initExpression150, baseExp153, loopExpr155, operation158, elementType161, operation169, mapType2172, attribute174, mapType177, collectionTypes180, tupleTypeAttribute182, variableDeclaration184, lambdaReturnType187, attributes196, type199, tupleType202, model204, lambdaArgType189, staticPropertyCall192, model195, argumentTypes216, feature219, context_221, definition224, context_226, definition229, valueType207, keyType210, returnType213, body243, elements246, model248, metamodel250, initExpression232, type235, parameters238, returnType240},
    generalizations={gen_QualityMetamodel_QualityModel_Module, gen_QualityMetamodel_QualityAttribute_VariableDeclaration, gen_QualityMetamodel_EnumerationMetric_ValueType, gen_QualityMetamodel_Value_VariableDeclaration, gen_QualityMetamodel_ValueType_VariableDeclaration, gen_QualityMetamodel_SingleValue_Value, gen_QualityMetamodel_AggregatedValue_Value, gen_QualityMetamodel_TextValueType_ValueType, gen_QualityMetamodel_RangeValueType_ValueType, gen_QualityMetamodel_AggregatedValueMetric_ValueType, gen_QualityMetamodel_QMM_OCL_ModuleElement_LocatedElement, gen_QualityMetamodel_RealValueType_ValueType, gen_QualityMetamodel_BooleanValueType_ValueType, gen_QualityMetamodel_IntegerValueType_ValueType, gen_QualityMetamodel_ListValue_ValueType, gen_QualityMetamodel_QMM_OCL_NamedElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_Module_NamedElement, gen_QualityMetamodel_QMM_OCL_Import_NamedElement, gen_QualityMetamodel_QMM_OCL_OclExpression_LocatedElement, gen_QualityMetamodel_QMM_OCL_CollectionPart_LocatedElement, gen_QualityMetamodel_QMM_OCL_CollectionRange_CollectionPart, gen_QualityMetamodel_QMM_OCL_CollectionItem_CollectionPart, gen_QualityMetamodel_QMM_OCL_VariableExp_OclExpression, gen_QualityMetamodel_QMM_OCL_BagExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_OrderedSetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SuperExp_OclExpression, gen_QualityMetamodel_QMM_OCL_SequenceExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_SelfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_EnvExp_OclExpression, gen_QualityMetamodel_QMM_OCL_PrimitiveExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StringExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_BooleanExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_NumericExp_PrimitiveExp, gen_QualityMetamodel_QMM_OCL_RealExp_NumericExp, gen_QualityMetamodel_QMM_OCL_IntegerExp_NumericExp, gen_QualityMetamodel_QMM_OCL_CollectionExp_OclExpression, gen_QualityMetamodel_QMM_OCL_EnumLiteralExp_OclExpression, gen_QualityMetamodel_QMM_OCL_OclUndefinedExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticPropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_SetExp_CollectionExp, gen_QualityMetamodel_QMM_OCL_TupleExp_OclExpression, gen_QualityMetamodel_QMM_OCL_TuplePart_LocalVariable, gen_QualityMetamodel_QMM_OCL_MapExp_OclExpression, gen_QualityMetamodel_QMM_OCL_MapElement_LocatedElement, gen_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_OperationCall_PropertyCall, gen_QualityMetamodel_QMM_OCL_OperatorCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_StaticOperationCall_StaticPropertyCall, gen_QualityMetamodel_QMM_OCL_PropertyCallExp_OclExpression, gen_QualityMetamodel_QMM_OCL_PropertyCall_LocatedElement, gen_QualityMetamodel_QMM_OCL_CollectionOperationCall_OperationCall, gen_QualityMetamodel_QMM_OCL_LoopExp_PropertyCall, gen_QualityMetamodel_QMM_OCL_IterateExp_LoopExp, gen_QualityMetamodel_QMM_OCL_IteratorExp_LoopExp, gen_QualityMetamodel_QMM_OCL_LetExp_OclExpression, gen_QualityMetamodel_QMM_OCL_NotOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_RelOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_EqOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_AddOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_IntOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_IfExp_OclExpression, gen_QualityMetamodel_QMM_OCL_MulOpCallExp_OperatorCallExp, gen_QualityMetamodel_QMM_OCL_LambdaCallExp_VariableExp, gen_QualityMetamodel_QMM_OCL_BraceExp_OclExpression, gen_QualityMetamodel_QMM_OCL_VariableDeclaration_LocatedElement, gen_QualityMetamodel_QMM_OCL_LocalVariable_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Iterator_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_Parameter_VariableDeclaration, gen_QualityMetamodel_QMM_OCL_CollectionType_OclType, gen_QualityMetamodel_QMM_OCL_OclType_LocatedElement, gen_QualityMetamodel_QMM_OCL_BooleanType_Primitive, gen_QualityMetamodel_QMM_OCL_NumericType_Primitive, gen_QualityMetamodel_QMM_OCL_IntegerType_NumericType, gen_QualityMetamodel_QMM_OCL_RealType_NumericType, gen_QualityMetamodel_QMM_OCL_BagType_CollectionType, gen_QualityMetamodel_QMM_OCL_OrderedSetType_CollectionType, gen_QualityMetamodel_QMM_OCL_SequenceType_CollectionType, gen_QualityMetamodel_QMM_OCL_SetType_CollectionType, gen_QualityMetamodel_QMM_OCL_OclAnyType_OclType, gen_QualityMetamodel_QMM_OCL_TupleType_OclType, gen_QualityMetamodel_QMM_OCL_TupleTypeAttribute_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclModelElement_OclType, gen_QualityMetamodel_QMM_OCL_OclModelElementExp_OclExpression, gen_QualityMetamodel_QMM_OCL_Primitive_OclType, gen_QualityMetamodel_QMM_OCL_StringType_Primitive, gen_QualityMetamodel_QMM_OCL_EnvType_OclType, gen_QualityMetamodel_QMM_OCL_OclFeatureDefinition_ModuleElement, gen_QualityMetamodel_QMM_OCL_OclContextDefinition_LocatedElement, gen_QualityMetamodel_QMM_OCL_OclFeature_NamedElement, gen_QualityMetamodel_QMM_OCL_Attribute_OclFeature, gen_QualityMetamodel_QMM_OCL_MapType_OclType, gen_QualityMetamodel_QMM_OCL_LambdaType_OclType, gen_QualityMetamodel_QMM_OCL_OclModel_NamedElement, gen_QualityMetamodel_QMM_OCL_OclMetamodel_OclModel, gen_QualityMetamodel_QMM_OCL_OclInstanceModel_OclModel, gen_QualityMetamodel_QMM_OCL_Operation_OclFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)