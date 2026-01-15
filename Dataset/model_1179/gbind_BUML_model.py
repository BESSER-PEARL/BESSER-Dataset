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
gbind_simpleocl_LocatedElement = Class(name="gbind::simpleocl::LocatedElement", is_abstract=True)
gbind_simpleocl_NamedElement = Class(name="gbind::simpleocl::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
gbind_simpleocl_Module = Class(name="gbind::simpleocl::Module")
NamedElement = Class(name="NamedElement")
OclMetamodel = Class(name="OclMetamodel")
Import = Class(name="Import")
ModuleElement = Class(name="ModuleElement")
gbind_simpleocl_ModuleElement = Class(name="gbind::simpleocl::ModuleElement", is_abstract=True)
Module = Class(name="Module")
gbind_simpleocl_Import = Class(name="gbind::simpleocl::Import")
gbind_simpleocl_OclExpression = Class(name="gbind::simpleocl::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCall = Class(name="OperationCall")
LocalVariable = Class(name="LocalVariable")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OperatorCallExp = Class(name="OperatorCallExp")
gbind_simpleocl_VariableExp = Class(name="gbind::simpleocl::VariableExp")
OclExpression = Class(name="OclExpression")
VariableDeclaration = Class(name="VariableDeclaration")
gbind_simpleocl_SuperExp = Class(name="gbind::simpleocl::SuperExp")
gbind_simpleocl_SelfExp = Class(name="gbind::simpleocl::SelfExp")
gbind_simpleocl_EnvExp = Class(name="gbind::simpleocl::EnvExp")
gbind_simpleocl_PrimitiveExp = Class(name="gbind::simpleocl::PrimitiveExp", is_abstract=True)
gbind_simpleocl_StringExp = Class(name="gbind::simpleocl::StringExp")
CollectionExp = Class(name="CollectionExp")
gbind_simpleocl_BooleanExp = Class(name="gbind::simpleocl::BooleanExp")
gbind_simpleocl_NumericExp = Class(name="gbind::simpleocl::NumericExp", is_abstract=True)
gbind_simpleocl_RealExp = Class(name="gbind::simpleocl::RealExp")
NumericExp = Class(name="NumericExp")
gbind_simpleocl_IntegerExp = Class(name="gbind::simpleocl::IntegerExp")
gbind_simpleocl_CollectionExp = Class(name="gbind::simpleocl::CollectionExp", is_abstract=True)
gbind_simpleocl_BagExp = Class(name="gbind::simpleocl::BagExp")
gbind_simpleocl_OrderedSetExp = Class(name="gbind::simpleocl::OrderedSetExp")
gbind_simpleocl_SequenceExp = Class(name="gbind::simpleocl::SequenceExp")
gbind_simpleocl_SetExp = Class(name="gbind::simpleocl::SetExp")
gbind_simpleocl_TupleExp = Class(name="gbind::simpleocl::TupleExp")
TuplePart = Class(name="TuplePart")
gbind_simpleocl_TuplePart = Class(name="gbind::simpleocl::TuplePart")
TupleExp = Class(name="TupleExp")
gbind_simpleocl_MapExp = Class(name="gbind::simpleocl::MapExp")
MapElement = Class(name="MapElement")
gbind_simpleocl_MapElement = Class(name="gbind::simpleocl::MapElement")
PrimitiveExp = Class(name="PrimitiveExp")
gbind_simpleocl_EnumLiteralExp = Class(name="gbind::simpleocl::EnumLiteralExp")
gbind_simpleocl_OclUndefinedExp = Class(name="gbind::simpleocl::OclUndefinedExp")
gbind_simpleocl_StaticPropertyCallExp = Class(name="gbind::simpleocl::StaticPropertyCallExp")
StaticPropertyCall = Class(name="StaticPropertyCall")
gbind_simpleocl_StaticPropertyCall = Class(name="gbind::simpleocl::StaticPropertyCall", is_abstract=True)
StaticPropertyCallExp = Class(name="StaticPropertyCallExp")
gbind_simpleocl_StaticNavigationOrAttributeCall = Class(name="gbind::simpleocl::StaticNavigationOrAttributeCall")
gbind_simpleocl_StaticOperationCall = Class(name="gbind::simpleocl::StaticOperationCall")
gbind_simpleocl_PropertyCallExp = Class(name="gbind::simpleocl::PropertyCallExp")
PropertyCall = Class(name="PropertyCall")
MapExp = Class(name="MapExp")
gbind_simpleocl_PropertyCall = Class(name="gbind::simpleocl::PropertyCall", is_abstract=True)
gbind_simpleocl_NavigationOrAttributeCall = Class(name="gbind::simpleocl::NavigationOrAttributeCall")
gbind_simpleocl_OperationCall = Class(name="gbind::simpleocl::OperationCall")
gbind_simpleocl_OperatorCallExp = Class(name="gbind::simpleocl::OperatorCallExp")
gbind_simpleocl_NotOpCallExp = Class(name="gbind::simpleocl::NotOpCallExp")
gbind_simpleocl_RelOpCallExp = Class(name="gbind::simpleocl::RelOpCallExp")
gbind_simpleocl_EqOpCallExp = Class(name="gbind::simpleocl::EqOpCallExp")
gbind_simpleocl_AddOpCallExp = Class(name="gbind::simpleocl::AddOpCallExp")
gbind_simpleocl_IntOpCallExp = Class(name="gbind::simpleocl::IntOpCallExp")
gbind_simpleocl_MulOpCallExp = Class(name="gbind::simpleocl::MulOpCallExp")
gbind_simpleocl_LambdaCallExp = Class(name="gbind::simpleocl::LambdaCallExp")
VariableExp = Class(name="VariableExp")
gbind_simpleocl_CollectionOperationCall = Class(name="gbind::simpleocl::CollectionOperationCall")
gbind_simpleocl_LoopExp = Class(name="gbind::simpleocl::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
gbind_simpleocl_IterateExp = Class(name="gbind::simpleocl::IterateExp")
gbind_simpleocl_IteratorExp = Class(name="gbind::simpleocl::IteratorExp")
gbind_simpleocl_LetExp = Class(name="gbind::simpleocl::LetExp")
gbind_simpleocl_IfExp = Class(name="gbind::simpleocl::IfExp")
gbind_simpleocl_BraceExp = Class(name="gbind::simpleocl::BraceExp")
gbind_simpleocl_VariableDeclaration = Class(name="gbind::simpleocl::VariableDeclaration", is_abstract=True)
gbind_simpleocl_LocalVariable = Class(name="gbind::simpleocl::LocalVariable")
IterateExp = Class(name="IterateExp")
gbind_simpleocl_Iterator = Class(name="gbind::simpleocl::Iterator")
gbind_simpleocl_Parameter = Class(name="gbind::simpleocl::Parameter")
gbind_simpleocl_CollectionType = Class(name="gbind::simpleocl::CollectionType")
gbind_simpleocl_OclType = Class(name="gbind::simpleocl::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
LambdaType = Class(name="LambdaType")
gbind_simpleocl_OclModelElementExp = Class(name="gbind::simpleocl::OclModelElementExp")
OclModel = Class(name="OclModel")
gbind_simpleocl_Primitive = Class(name="gbind::simpleocl::Primitive", is_abstract=True)
gbind_simpleocl_StringType = Class(name="gbind::simpleocl::StringType")
Primitive = Class(name="Primitive")
gbind_simpleocl_BooleanType = Class(name="gbind::simpleocl::BooleanType")
gbind_simpleocl_NumericType = Class(name="gbind::simpleocl::NumericType", is_abstract=True)
gbind_simpleocl_IntegerType = Class(name="gbind::simpleocl::IntegerType")
NumericType = Class(name="NumericType")
gbind_simpleocl_RealType = Class(name="gbind::simpleocl::RealType")
gbind_simpleocl_BagType = Class(name="gbind::simpleocl::BagType")
gbind_simpleocl_OrderedSetType = Class(name="gbind::simpleocl::OrderedSetType")
gbind_simpleocl_SequenceType = Class(name="gbind::simpleocl::SequenceType")
gbind_simpleocl_SetType = Class(name="gbind::simpleocl::SetType")
gbind_simpleocl_OclAnyType = Class(name="gbind::simpleocl::OclAnyType")
gbind_simpleocl_TupleType = Class(name="gbind::simpleocl::TupleType")
gbind_simpleocl_TupleTypeAttribute = Class(name="gbind::simpleocl::TupleTypeAttribute")
TupleType = Class(name="TupleType")
gbind_simpleocl_MapType = Class(name="gbind::simpleocl::MapType")
gbind_simpleocl_LambdaType = Class(name="gbind::simpleocl::LambdaType")
gbind_simpleocl_EnvType = Class(name="gbind::simpleocl::EnvType")
gbind_simpleocl_OclFeatureDefinition = Class(name="gbind::simpleocl::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
gbind_simpleocl_OclModelElement = Class(name="gbind::simpleocl::OclModelElement")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
gbind_simpleocl_OclFeature = Class(name="gbind::simpleocl::OclFeature", is_abstract=True)
gbind_simpleocl_Attribute = Class(name="gbind::simpleocl::Attribute")
gbind_simpleocl_Operation = Class(name="gbind::simpleocl::Operation")
Parameter_ = Class(name="Parameter")
gbind_simpleocl_OclContextDefinition = Class(name="gbind::simpleocl::OclContextDefinition")
gbind_simpleocl_OclModel = Class(name="gbind::simpleocl::OclModel", is_abstract=True)
OclModelElement = Class(name="OclModelElement")
gbind_simpleocl_OclMetamodel = Class(name="gbind::simpleocl::OclMetamodel")
OclInstanceModel = Class(name="OclInstanceModel")
gbind_simpleocl_OclInstanceModel = Class(name="gbind::simpleocl::OclInstanceModel")
gbind_dsl_BindingModel = Class(name="gbind::dsl::BindingModel")
ConceptBinding = Class(name="ConceptBinding")
BaseHelper = Class(name="BaseHelper")
ConceptMetaclass = Class(name="ConceptMetaclass")
VirtualMetaclass = Class(name="VirtualMetaclass")
MetamodelDeclaration = Class(name="MetamodelDeclaration")
BindingOptions = Class(name="BindingOptions")
gbind_dsl_BindingOptions = Class(name="gbind::dsl::BindingOptions")
gbind_dsl_MetamodelDeclaration = Class(name="gbind::dsl::MetamodelDeclaration")
gbind_dsl_Metaclass = Class(name="gbind::dsl::Metaclass", is_abstract=True)
dsl_gbind_EClass = Class(name="dsl::gbind::EClass")
gbind_dsl_ConceptMetaclass = Class(name="gbind::dsl::ConceptMetaclass")
Metaclass = Class(name="Metaclass")
gbind_dsl_ConcreteMetaclass = Class(name="gbind::dsl::ConcreteMetaclass")
gbind_dsl_ConceptBinding = Class(name="gbind::dsl::ConceptBinding", is_abstract=True)
BindingModel = Class(name="BindingModel")
ConcreteMetaclass = Class(name="ConcreteMetaclass")
gbind_dsl_IntermediateClassBinding = Class(name="gbind::dsl::IntermediateClassBinding")
ConcreteReferencDeclaringVar = Class(name="ConcreteReferencDeclaringVar")
BaseFeatureBinding = Class(name="BaseFeatureBinding")
gbind_dsl_ConcreteReferencDeclaringVar = Class(name="gbind::dsl::ConcreteReferencDeclaringVar")
gbind_dsl_VirtualMetaclass = Class(name="gbind::dsl::VirtualMetaclass")
VirtualReference = Class(name="VirtualReference")
VirtualAttribute = Class(name="VirtualAttribute")
gbind_dsl_ClassBinding = Class(name="gbind::dsl::ClassBinding")
gbind_dsl_VirtualFeature = Class(name="gbind::dsl::VirtualFeature")
gbind_dsl_VirtualReference = Class(name="gbind::dsl::VirtualReference")
VirtualFeature = Class(name="VirtualFeature")
gbind_dsl_VirtualAttribute = Class(name="gbind::dsl::VirtualAttribute")
gbind_dsl_VirtualClassBinding = Class(name="gbind::dsl::VirtualClassBinding")
ConceptFeatureRef = Class(name="ConceptFeatureRef")
gbind_dsl_ConceptFeatureRef = Class(name="gbind::dsl::ConceptFeatureRef")
gbind_dsl_BaseFeatureBinding = Class(name="gbind::dsl::BaseFeatureBinding")
gbind_dsl_OclFeatureBinding = Class(name="gbind::dsl::OclFeatureBinding")
gbind_dsl_BaseHelper = Class(name="gbind::dsl::BaseHelper")
gbind_dsl_ConceptHelper = Class(name="gbind::dsl::ConceptHelper")
gbind_dsl_LocalHelper = Class(name="gbind::dsl::LocalHelper")
HelperParameter = Class(name="HelperParameter")
gbind_dsl_HelperParameter = Class(name="gbind::dsl::HelperParameter")
gbind_dsl_RenamingFeatureBinding = Class(name="gbind::dsl::RenamingFeatureBinding")

# gbind_simpleocl_LocatedElement class attributes and methods
gbind_simpleocl_LocatedElement_column: Property = Property(name="column", type=StringType)
gbind_simpleocl_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
gbind_simpleocl_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
gbind_simpleocl_LocatedElement_line: Property = Property(name="line", type=StringType)
gbind_simpleocl_LocatedElement.attributes={gbind_simpleocl_LocatedElement_column, gbind_simpleocl_LocatedElement_charEnd, gbind_simpleocl_LocatedElement_line, gbind_simpleocl_LocatedElement_charStart}

# gbind_simpleocl_NamedElement class attributes and methods
gbind_simpleocl_NamedElement_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_NamedElement.attributes={gbind_simpleocl_NamedElement_name}

# LocatedElement class attributes and methods

# gbind_simpleocl_Module class attributes and methods

# NamedElement class attributes and methods

# OclMetamodel class attributes and methods

# Import class attributes and methods

# ModuleElement class attributes and methods

# gbind_simpleocl_ModuleElement class attributes and methods

# Module class attributes and methods

# gbind_simpleocl_Import class attributes and methods

# gbind_simpleocl_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCall class attributes and methods

# LocalVariable class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OperatorCallExp class attributes and methods

# gbind_simpleocl_VariableExp class attributes and methods

# OclExpression class attributes and methods

# VariableDeclaration class attributes and methods

# gbind_simpleocl_SuperExp class attributes and methods

# gbind_simpleocl_SelfExp class attributes and methods

# gbind_simpleocl_EnvExp class attributes and methods

# gbind_simpleocl_PrimitiveExp class attributes and methods

# gbind_simpleocl_StringExp class attributes and methods
gbind_simpleocl_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
gbind_simpleocl_StringExp.attributes={gbind_simpleocl_StringExp_stringSymbol}

# CollectionExp class attributes and methods

# gbind_simpleocl_BooleanExp class attributes and methods
gbind_simpleocl_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
gbind_simpleocl_BooleanExp.attributes={gbind_simpleocl_BooleanExp_booleanSymbol}

# gbind_simpleocl_NumericExp class attributes and methods

# gbind_simpleocl_RealExp class attributes and methods
gbind_simpleocl_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
gbind_simpleocl_RealExp.attributes={gbind_simpleocl_RealExp_realSymbol}

# NumericExp class attributes and methods

# gbind_simpleocl_IntegerExp class attributes and methods
gbind_simpleocl_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
gbind_simpleocl_IntegerExp.attributes={gbind_simpleocl_IntegerExp_integerSymbol}

# gbind_simpleocl_CollectionExp class attributes and methods

# gbind_simpleocl_BagExp class attributes and methods

# gbind_simpleocl_OrderedSetExp class attributes and methods

# gbind_simpleocl_SequenceExp class attributes and methods

# gbind_simpleocl_SetExp class attributes and methods

# gbind_simpleocl_TupleExp class attributes and methods

# TuplePart class attributes and methods

# gbind_simpleocl_TuplePart class attributes and methods

# TupleExp class attributes and methods

# gbind_simpleocl_MapExp class attributes and methods

# MapElement class attributes and methods

# gbind_simpleocl_MapElement class attributes and methods

# PrimitiveExp class attributes and methods

# gbind_simpleocl_EnumLiteralExp class attributes and methods
gbind_simpleocl_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_EnumLiteralExp.attributes={gbind_simpleocl_EnumLiteralExp_name}

# gbind_simpleocl_OclUndefinedExp class attributes and methods

# gbind_simpleocl_StaticPropertyCallExp class attributes and methods

# StaticPropertyCall class attributes and methods

# gbind_simpleocl_StaticPropertyCall class attributes and methods

# StaticPropertyCallExp class attributes and methods

# gbind_simpleocl_StaticNavigationOrAttributeCall class attributes and methods
gbind_simpleocl_StaticNavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_StaticNavigationOrAttributeCall.attributes={gbind_simpleocl_StaticNavigationOrAttributeCall_name}

# gbind_simpleocl_StaticOperationCall class attributes and methods
gbind_simpleocl_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
gbind_simpleocl_StaticOperationCall.attributes={gbind_simpleocl_StaticOperationCall_operationName}

# gbind_simpleocl_PropertyCallExp class attributes and methods

# PropertyCall class attributes and methods

# MapExp class attributes and methods

# gbind_simpleocl_PropertyCall class attributes and methods

# gbind_simpleocl_NavigationOrAttributeCall class attributes and methods
gbind_simpleocl_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_NavigationOrAttributeCall.attributes={gbind_simpleocl_NavigationOrAttributeCall_name}

# gbind_simpleocl_OperationCall class attributes and methods
gbind_simpleocl_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
gbind_simpleocl_OperationCall.attributes={gbind_simpleocl_OperationCall_operationName}

# gbind_simpleocl_OperatorCallExp class attributes and methods
gbind_simpleocl_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
gbind_simpleocl_OperatorCallExp.attributes={gbind_simpleocl_OperatorCallExp_operationName}

# gbind_simpleocl_NotOpCallExp class attributes and methods

# gbind_simpleocl_RelOpCallExp class attributes and methods

# gbind_simpleocl_EqOpCallExp class attributes and methods

# gbind_simpleocl_AddOpCallExp class attributes and methods

# gbind_simpleocl_IntOpCallExp class attributes and methods

# gbind_simpleocl_MulOpCallExp class attributes and methods

# gbind_simpleocl_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# gbind_simpleocl_CollectionOperationCall class attributes and methods

# gbind_simpleocl_LoopExp class attributes and methods

# Iterator class attributes and methods

# gbind_simpleocl_IterateExp class attributes and methods

# gbind_simpleocl_IteratorExp class attributes and methods
gbind_simpleocl_IteratorExp_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_IteratorExp.attributes={gbind_simpleocl_IteratorExp_name}

# gbind_simpleocl_LetExp class attributes and methods

# gbind_simpleocl_IfExp class attributes and methods

# gbind_simpleocl_BraceExp class attributes and methods

# gbind_simpleocl_VariableDeclaration class attributes and methods
gbind_simpleocl_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
gbind_simpleocl_VariableDeclaration.attributes={gbind_simpleocl_VariableDeclaration_varName}

# gbind_simpleocl_LocalVariable class attributes and methods
gbind_simpleocl_LocalVariable_eq: Property = Property(name="eq", type=StringType)
gbind_simpleocl_LocalVariable.attributes={gbind_simpleocl_LocalVariable_eq}

# IterateExp class attributes and methods

# gbind_simpleocl_Iterator class attributes and methods

# gbind_simpleocl_Parameter class attributes and methods

# gbind_simpleocl_CollectionType class attributes and methods

# gbind_simpleocl_OclType class attributes and methods
gbind_simpleocl_OclType_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_OclType.attributes={gbind_simpleocl_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# LambdaType class attributes and methods

# gbind_simpleocl_OclModelElementExp class attributes and methods
gbind_simpleocl_OclModelElementExp_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_OclModelElementExp.attributes={gbind_simpleocl_OclModelElementExp_name}

# OclModel class attributes and methods

# gbind_simpleocl_Primitive class attributes and methods

# gbind_simpleocl_StringType class attributes and methods

# Primitive class attributes and methods

# gbind_simpleocl_BooleanType class attributes and methods

# gbind_simpleocl_NumericType class attributes and methods

# gbind_simpleocl_IntegerType class attributes and methods

# NumericType class attributes and methods

# gbind_simpleocl_RealType class attributes and methods

# gbind_simpleocl_BagType class attributes and methods

# gbind_simpleocl_OrderedSetType class attributes and methods

# gbind_simpleocl_SequenceType class attributes and methods

# gbind_simpleocl_SetType class attributes and methods

# gbind_simpleocl_OclAnyType class attributes and methods

# gbind_simpleocl_TupleType class attributes and methods

# gbind_simpleocl_TupleTypeAttribute class attributes and methods
gbind_simpleocl_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_TupleTypeAttribute.attributes={gbind_simpleocl_TupleTypeAttribute_name}

# TupleType class attributes and methods

# gbind_simpleocl_MapType class attributes and methods

# gbind_simpleocl_LambdaType class attributes and methods

# gbind_simpleocl_EnvType class attributes and methods

# gbind_simpleocl_OclFeatureDefinition class attributes and methods
gbind_simpleocl_OclFeatureDefinition_static: Property = Property(name="static", type=StringType)
gbind_simpleocl_OclFeatureDefinition.attributes={gbind_simpleocl_OclFeatureDefinition_static}

# OclFeature class attributes and methods

# gbind_simpleocl_OclModelElement class attributes and methods

# OclFeatureDefinition class attributes and methods

# gbind_simpleocl_OclFeature class attributes and methods
gbind_simpleocl_OclFeature_eq: Property = Property(name="eq", type=StringType)
gbind_simpleocl_OclFeature.attributes={gbind_simpleocl_OclFeature_eq}

# gbind_simpleocl_Attribute class attributes and methods

# gbind_simpleocl_Operation class attributes and methods

# Parameter class attributes and methods

# gbind_simpleocl_OclContextDefinition class attributes and methods

# gbind_simpleocl_OclModel class attributes and methods

# OclModelElement class attributes and methods

# gbind_simpleocl_OclMetamodel class attributes and methods
gbind_simpleocl_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
gbind_simpleocl_OclMetamodel.attributes={gbind_simpleocl_OclMetamodel_uri}

# OclInstanceModel class attributes and methods

# gbind_simpleocl_OclInstanceModel class attributes and methods

# gbind_dsl_BindingModel class attributes and methods
gbind_dsl_BindingModel_name: Property = Property(name="name", type=StringType)
gbind_dsl_BindingModel.attributes={gbind_dsl_BindingModel_name}

# ConceptBinding class attributes and methods

# BaseHelper class attributes and methods

# ConceptMetaclass class attributes and methods

# VirtualMetaclass class attributes and methods

# MetamodelDeclaration class attributes and methods

# BindingOptions class attributes and methods

# gbind_dsl_BindingOptions class attributes and methods
gbind_dsl_BindingOptions_enableClassMerge: Property = Property(name="enableClassMerge", type=BooleanType)
gbind_dsl_BindingOptions.attributes={gbind_dsl_BindingOptions_enableClassMerge}

# gbind_dsl_MetamodelDeclaration class attributes and methods
gbind_dsl_MetamodelDeclaration_metamodelURI: Property = Property(name="metamodelURI", type=StringType)
gbind_dsl_MetamodelDeclaration.attributes={gbind_dsl_MetamodelDeclaration_metamodelURI}

# gbind_dsl_Metaclass class attributes and methods
gbind_dsl_Metaclass_name: Property = Property(name="name", type=StringType)
gbind_dsl_Metaclass.attributes={gbind_dsl_Metaclass_name}

# dsl_gbind_EClass class attributes and methods

# gbind_dsl_ConceptMetaclass class attributes and methods

# Metaclass class attributes and methods

# gbind_dsl_ConcreteMetaclass class attributes and methods

# gbind_dsl_ConceptBinding class attributes and methods
gbind_dsl_ConceptBinding_debugName: Property = Property(name="debugName", type=StringType)
gbind_dsl_ConceptBinding.attributes={gbind_dsl_ConceptBinding_debugName}

# BindingModel class attributes and methods

# ConcreteMetaclass class attributes and methods

# gbind_dsl_IntermediateClassBinding class attributes and methods
gbind_dsl_IntermediateClassBinding_conceptReferenceName: Property = Property(name="conceptReferenceName", type=StringType)
gbind_dsl_IntermediateClassBinding.attributes={gbind_dsl_IntermediateClassBinding_conceptReferenceName}

# ConcreteReferencDeclaringVar class attributes and methods

# BaseFeatureBinding class attributes and methods

# gbind_dsl_ConcreteReferencDeclaringVar class attributes and methods

# gbind_dsl_VirtualMetaclass class attributes and methods

# VirtualReference class attributes and methods

# VirtualAttribute class attributes and methods

# gbind_dsl_ClassBinding class attributes and methods

# gbind_dsl_VirtualFeature class attributes and methods
gbind_dsl_VirtualFeature_name: Property = Property(name="name", type=StringType)
gbind_dsl_VirtualFeature.attributes={gbind_dsl_VirtualFeature_name}

# gbind_dsl_VirtualReference class attributes and methods

# VirtualFeature class attributes and methods

# gbind_dsl_VirtualAttribute class attributes and methods

# gbind_dsl_VirtualClassBinding class attributes and methods

# ConceptFeatureRef class attributes and methods

# gbind_dsl_ConceptFeatureRef class attributes and methods
gbind_dsl_ConceptFeatureRef_featureName: Property = Property(name="featureName", type=StringType)
gbind_dsl_ConceptFeatureRef.attributes={gbind_dsl_ConceptFeatureRef_featureName}

# gbind_dsl_BaseFeatureBinding class attributes and methods
gbind_dsl_BaseFeatureBinding_conceptFeature: Property = Property(name="conceptFeature", type=StringType)
gbind_dsl_BaseFeatureBinding.attributes={gbind_dsl_BaseFeatureBinding_conceptFeature}

# gbind_dsl_OclFeatureBinding class attributes and methods

# gbind_dsl_BaseHelper class attributes and methods
gbind_dsl_BaseHelper_feature: Property = Property(name="feature", type=StringType)
gbind_dsl_BaseHelper.attributes={gbind_dsl_BaseHelper_feature}

# gbind_dsl_ConceptHelper class attributes and methods

# gbind_dsl_LocalHelper class attributes and methods

# HelperParameter class attributes and methods

# gbind_dsl_HelperParameter class attributes and methods

# gbind_dsl_RenamingFeatureBinding class attributes and methods
gbind_dsl_RenamingFeatureBinding_concreteFeature: Property = Property(name="concreteFeature", type=StringType)
gbind_dsl_RenamingFeatureBinding.attributes={gbind_dsl_RenamingFeatureBinding_concreteFeature}

# Relationships
metamodels0: BinaryAssociation = BinaryAssociation(
    name="metamodels0",
    ends={
        Property(name="OclMetamodel", type=gbind_simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_Module", type=OclMetamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="simpleocl", type=gbind_simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="Import", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="simpleocl3", type=gbind_simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ModuleElement", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module4: BinaryAssociation = BinaryAssociation(
    name="module4",
    ends={
        Property(name="simpleocl5", type=gbind_simpleocl_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Module", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module6: BinaryAssociation = BinaryAssociation(
    name="module6",
    ends={
        Property(name="simpleocl8", type=gbind_simpleocl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="Module7", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="simpleocl10", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp311: BinaryAssociation = BinaryAssociation(
    name="ifExp311",
    ends={
        Property(name="simpleocl12", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp17: BinaryAssociation = BinaryAssociation(
    name="letExp17",
    ends={
        Property(name="simpleocl18", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp19: BinaryAssociation = BinaryAssociation(
    name="loopExp19",
    ends={
        Property(name="simpleocl20", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation21: BinaryAssociation = BinaryAssociation(
    name="parentOperation21",
    ends={
        Property(name="simpleocl22", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCall", type=OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable23: BinaryAssociation = BinaryAssociation(
    name="initializedVariable23",
    ends={
        Property(name="simpleocl24", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable", type=LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp225: BinaryAssociation = BinaryAssociation(
    name="ifExp225",
    ends={
        Property(name="simpleocl27", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp26", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation28: BinaryAssociation = BinaryAssociation(
    name="owningOperation28",
    ends={
        Property(name="simpleocl29", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp130: BinaryAssociation = BinaryAssociation(
    name="ifExp130",
    ends={
        Property(name="simpleocl32", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp31", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute33: BinaryAssociation = BinaryAssociation(
    name="owningAttribute33",
    ends={
        Property(name="simpleocl34", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
appliedOperator35: BinaryAssociation = BinaryAssociation(
    name="appliedOperator35",
    ends={
        Property(name="simpleocl36", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperatorCallExp", type=OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable37: BinaryAssociation = BinaryAssociation(
    name="referredVariable37",
    ends={
        Property(name="simpleocl38", type=gbind_simpleocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
appliedProperty13: BinaryAssociation = BinaryAssociation(
    name="appliedProperty13",
    ends={
        Property(name="simpleocl14", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection15: BinaryAssociation = BinaryAssociation(
    name="collection15",
    ends={
        Property(name="simpleocl16", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
elements39: BinaryAssociation = BinaryAssociation(
    name="elements39",
    ends={
        Property(name="simpleocl40", type=gbind_simpleocl_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart41: BinaryAssociation = BinaryAssociation(
    name="tuplePart41",
    ends={
        Property(name="simpleocl42", type=gbind_simpleocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple43: BinaryAssociation = BinaryAssociation(
    name="tuple43",
    ends={
        Property(name="simpleocl44", type=gbind_simpleocl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements45: BinaryAssociation = BinaryAssociation(
    name="elements45",
    ends={
        Property(name="simpleocl46", type=gbind_simpleocl_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key49: BinaryAssociation = BinaryAssociation(
    name="key49",
    ends={
        Property(name="OclExpression50", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="OclExpression53", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_MapElement52", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source54: BinaryAssociation = BinaryAssociation(
    name="source54",
    ends={
        Property(name="simpleocl56", type=gbind_simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType55", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall57: BinaryAssociation = BinaryAssociation(
    name="staticCall57",
    ends={
        Property(name="simpleocl58", type=gbind_simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCall", type=StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp59: BinaryAssociation = BinaryAssociation(
    name="staticCallExp59",
    ends={
        Property(name="simpleocl60", type=gbind_simpleocl_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp", type=StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments61: BinaryAssociation = BinaryAssociation(
    name="arguments61",
    ends={
        Property(name="OclExpression62", type=gbind_simpleocl_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_StaticOperationCall", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls63: BinaryAssociation = BinaryAssociation(
    name="calls63",
    ends={
        Property(name="simpleocl64", type=gbind_simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCall", type=PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
map47: BinaryAssociation = BinaryAssociation(
    name="map47",
    ends={
        Property(name="simpleocl48", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
callExp68: BinaryAssociation = BinaryAssociation(
    name="callExp68",
    ends={
        Property(name="simpleocl70", type=gbind_simpleocl_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp69", type=PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments71: BinaryAssociation = BinaryAssociation(
    name="arguments71",
    ends={
        Property(name="simpleocl73", type=gbind_simpleocl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression72", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument74: BinaryAssociation = BinaryAssociation(
    name="argument74",
    ends={
        Property(name="OclExpression75", type=gbind_simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source76: BinaryAssociation = BinaryAssociation(
    name="source76",
    ends={
        Property(name="simpleocl78", type=gbind_simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression77", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments79: BinaryAssociation = BinaryAssociation(
    name="arguments79",
    ends={
        Property(name="OclExpression80", type=gbind_simpleocl_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_LambdaCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="simpleocl67", type=gbind_simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression66", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp81: BinaryAssociation = BinaryAssociation(
    name="exp81",
    ends={
        Property(name="OclExpression82", type=gbind_simpleocl_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_BraceExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body83: BinaryAssociation = BinaryAssociation(
    name="body83",
    ends={
        Property(name="simpleocl85", type=gbind_simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression84", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators86: BinaryAssociation = BinaryAssociation(
    name="iterators86",
    ends={
        Property(name="simpleocl87", type=gbind_simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result88: BinaryAssociation = BinaryAssociation(
    name="result88",
    ends={
        Property(name="simpleocl90", type=gbind_simpleocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable89", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable91: BinaryAssociation = BinaryAssociation(
    name="variable91",
    ends={
        Property(name="simpleocl93", type=gbind_simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LocalVariable92", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_94: BinaryAssociation = BinaryAssociation(
    name="in_94",
    ends={
        Property(name="simpleocl96", type=gbind_simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression95", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression97: BinaryAssociation = BinaryAssociation(
    name="thenExpression97",
    ends={
        Property(name="simpleocl99", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression98", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition100: BinaryAssociation = BinaryAssociation(
    name="condition100",
    ends={
        Property(name="simpleocl102", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression101", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression103: BinaryAssociation = BinaryAssociation(
    name="elseExpression103",
    ends={
        Property(name="simpleocl105", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression104", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type106: BinaryAssociation = BinaryAssociation(
    name="type106",
    ends={
        Property(name="simpleocl108", type=gbind_simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType107", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp109: BinaryAssociation = BinaryAssociation(
    name="variableExp109",
    ends={
        Property(name="simpleocl110", type=gbind_simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp111: BinaryAssociation = BinaryAssociation(
    name="letExp111",
    ends={
        Property(name="simpleocl113", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp112", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp117: BinaryAssociation = BinaryAssociation(
    name="baseExp117",
    ends={
        Property(name="simpleocl118", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr119: BinaryAssociation = BinaryAssociation(
    name="loopExpr119",
    ends={
        Property(name="simpleocl121", type=gbind_simpleocl_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp120", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation122: BinaryAssociation = BinaryAssociation(
    name="operation122",
    ends={
        Property(name="simpleocl124", type=gbind_simpleocl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation123", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType125: BinaryAssociation = BinaryAssociation(
    name="elementType125",
    ends={
        Property(name="simpleocl127", type=gbind_simpleocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType126", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions128: BinaryAssociation = BinaryAssociation(
    name="definitions128",
    ends={
        Property(name="simpleocl129", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression130: BinaryAssociation = BinaryAssociation(
    name="oclExpression130",
    ends={
        Property(name="simpleocl132", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression131", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
initExpression114: BinaryAssociation = BinaryAssociation(
    name="initExpression114",
    ends={
        Property(name="simpleocl116", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression115", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapType2136: BinaryAssociation = BinaryAssociation(
    name="mapType2136",
    ends={
        Property(name="simpleocl137", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute138: BinaryAssociation = BinaryAssociation(
    name="attribute138",
    ends={
        Property(name="simpleocl140", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute139", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType141: BinaryAssociation = BinaryAssociation(
    name="mapType141",
    ends={
        Property(name="simpleocl143", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType142", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes144: BinaryAssociation = BinaryAssociation(
    name="collectionTypes144",
    ends={
        Property(name="simpleocl145", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute146: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute146",
    ends={
        Property(name="simpleocl147", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration148: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration148",
    ends={
        Property(name="simpleocl150", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration149", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lambdaReturnType151: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType151",
    ends={
        Property(name="simpleocl152", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
lambdaArgType153: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType153",
    ends={
        Property(name="simpleocl155", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="LambdaType154", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
staticPropertyCall156: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall156",
    ends={
        Property(name="simpleocl158", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="StaticPropertyCallExp157", type=StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
model159: BinaryAssociation = BinaryAssociation(
    name="model159",
    ends={
        Property(name="OclModel", type=gbind_simpleocl_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_OclModelElementExp", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
operation133: BinaryAssociation = BinaryAssociation(
    name="operation133",
    ends={
        Property(name="simpleocl135", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation134", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
attributes160: BinaryAssociation = BinaryAssociation(
    name="attributes160",
    ends={
        Property(name="simpleocl162", type=gbind_simpleocl_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute161", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type163: BinaryAssociation = BinaryAssociation(
    name="type163",
    ends={
        Property(name="simpleocl165", type=gbind_simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType164", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType166: BinaryAssociation = BinaryAssociation(
    name="tupleType166",
    ends={
        Property(name="simpleocl167", type=gbind_simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model168: BinaryAssociation = BinaryAssociation(
    name="model168",
    ends={
        Property(name="simpleocl170", type=gbind_simpleocl_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel169", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType171: BinaryAssociation = BinaryAssociation(
    name="valueType171",
    ends={
        Property(name="simpleocl173", type=gbind_simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType172", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType174: BinaryAssociation = BinaryAssociation(
    name="keyType174",
    ends={
        Property(name="simpleocl176", type=gbind_simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType175", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType177: BinaryAssociation = BinaryAssociation(
    name="returnType177",
    ends={
        Property(name="simpleocl179", type=gbind_simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType178", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes180: BinaryAssociation = BinaryAssociation(
    name="argumentTypes180",
    ends={
        Property(name="simpleocl182", type=gbind_simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType181", type=OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature183: BinaryAssociation = BinaryAssociation(
    name="feature183",
    ends={
        Property(name="simpleocl184", type=gbind_simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_185: BinaryAssociation = BinaryAssociation(
    name="context_185",
    ends={
        Property(name="simpleocl187", type=gbind_simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition186", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition188: BinaryAssociation = BinaryAssociation(
    name="definition188",
    ends={
        Property(name="simpleocl189", type=gbind_simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_190: BinaryAssociation = BinaryAssociation(
    name="context_190",
    ends={
        Property(name="simpleocl192", type=gbind_simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType191", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition193: BinaryAssociation = BinaryAssociation(
    name="definition193",
    ends={
        Property(name="simpleocl195", type=gbind_simpleocl_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition194", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression196: BinaryAssociation = BinaryAssociation(
    name="initExpression196",
    ends={
        Property(name="simpleocl198", type=gbind_simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression197", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type199: BinaryAssociation = BinaryAssociation(
    name="type199",
    ends={
        Property(name="simpleocl201", type=gbind_simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType200", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters202: BinaryAssociation = BinaryAssociation(
    name="parameters202",
    ends={
        Property(name="simpleocl203", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType204: BinaryAssociation = BinaryAssociation(
    name="returnType204",
    ends={
        Property(name="simpleocl206", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType205", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements210: BinaryAssociation = BinaryAssociation(
    name="elements210",
    ends={
        Property(name="simpleocl211", type=gbind_simpleocl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model212: BinaryAssociation = BinaryAssociation(
    name="model212",
    ends={
        Property(name="simpleocl213", type=gbind_simpleocl_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclInstanceModel", type=OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel214: BinaryAssociation = BinaryAssociation(
    name="metamodel214",
    ends={
        Property(name="simpleocl216", type=gbind_simpleocl_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclMetamodel215", type=OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)
bindings217: BinaryAssociation = BinaryAssociation(
    name="bindings217",
    ends={
        Property(name="dsl", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptBinding", type=ConceptBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers218: BinaryAssociation = BinaryAssociation(
    name="helpers218",
    ends={
        Property(name="dsl219", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseHelper", type=BaseHelper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptMetaclasses220: BinaryAssociation = BinaryAssociation(
    name="conceptMetaclasses220",
    ends={
        Property(name="ConceptMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel", type=ConceptMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body207: BinaryAssociation = BinaryAssociation(
    name="body207",
    ends={
        Property(name="simpleocl209", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression208", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
virtualMetaclasses223: BinaryAssociation = BinaryAssociation(
    name="virtualMetaclasses223",
    ends={
        Property(name="VirtualMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel224", type=VirtualMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundConcept225: BinaryAssociation = BinaryAssociation(
    name="boundConcept225",
    ends={
        Property(name="MetamodelDeclaration", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel226", type=MetamodelDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boundMetamodel227: BinaryAssociation = BinaryAssociation(
    name="boundMetamodel227",
    ends={
        Property(name="MetamodelDeclaration229", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel228", type=MetamodelDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
options230: BinaryAssociation = BinaryAssociation(
    name="options230",
    ends={
        Property(name="BindingOptions", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel231", type=BindingOptions, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eclass232: BinaryAssociation = BinaryAssociation(
    name="eclass232",
    ends={
        Property(name="dsl_gbind_EClass", type=gbind_dsl_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_Metaclass", type=dsl_gbind_EClass, multiplicity=Multiplicity(1, 1))
    }
)
model_233: BinaryAssociation = BinaryAssociation(
    name="model_233",
    ends={
        Property(name="dsl234", type=gbind_dsl_ConceptBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BindingModel", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
concreteMetaclasses221: BinaryAssociation = BinaryAssociation(
    name="concreteMetaclasses221",
    ends={
        Property(name="ConcreteMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel222", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concrete237: BinaryAssociation = BinaryAssociation(
    name="concrete237",
    ends={
        Property(name="ConcreteMetaclass239", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding238", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 9999))
    }
)
whenClause240: BinaryAssociation = BinaryAssociation(
    name="whenClause240",
    ends={
        Property(name="OclExpression242", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding241", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concept243: BinaryAssociation = BinaryAssociation(
    name="concept243",
    ends={
        Property(name="ConceptMetaclass244", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concreteClass245: BinaryAssociation = BinaryAssociation(
    name="concreteClass245",
    ends={
        Property(name="ConcreteMetaclass247", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding246", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concreteReference248: BinaryAssociation = BinaryAssociation(
    name="concreteReference248",
    ends={
        Property(name="ConcreteReferencDeclaringVar", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding249", type=ConcreteReferencDeclaringVar, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conceptContext250: BinaryAssociation = BinaryAssociation(
    name="conceptContext250",
    ends={
        Property(name="ConceptMetaclass252", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding251", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
featureBindings253: BinaryAssociation = BinaryAssociation(
    name="featureBindings253",
    ends={
        Property(name="BaseFeatureBinding", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding254", type=BaseFeatureBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references255: BinaryAssociation = BinaryAssociation(
    name="references255",
    ends={
        Property(name="VirtualReference", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass", type=VirtualReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concept235: BinaryAssociation = BinaryAssociation(
    name="concept235",
    ends={
        Property(name="ConceptMetaclass236", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
type_261: BinaryAssociation = BinaryAssociation(
    name="type_261",
    ends={
        Property(name="ConcreteMetaclass262", type=gbind_dsl_VirtualReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualReference", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
type_263: BinaryAssociation = BinaryAssociation(
    name="type_263",
    ends={
        Property(name="Primitive", type=gbind_dsl_VirtualAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualAttribute", type=Primitive, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concept264: BinaryAssociation = BinaryAssociation(
    name="concept264",
    ends={
        Property(name="ConceptMetaclass265", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
virtual266: BinaryAssociation = BinaryAssociation(
    name="virtual266",
    ends={
        Property(name="VirtualMetaclass268", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding267", type=VirtualMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
refFeatures269: BinaryAssociation = BinaryAssociation(
    name="refFeatures269",
    ends={
        Property(name="ConceptFeatureRef", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding270", type=ConceptFeatureRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptClass271: BinaryAssociation = BinaryAssociation(
    name="conceptClass271",
    ends={
        Property(name="ConceptMetaclass272", type=gbind_dsl_ConceptFeatureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptFeatureRef", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
conceptClass273: BinaryAssociation = BinaryAssociation(
    name="conceptClass273",
    ends={
        Property(name="ConceptMetaclass274", type=gbind_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseFeatureBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
attributes256: BinaryAssociation = BinaryAssociation(
    name="attributes256",
    ends={
        Property(name="VirtualAttribute", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass257", type=VirtualAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init258: BinaryAssociation = BinaryAssociation(
    name="init258",
    ends={
        Property(name="OclExpression260", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass259", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concrete278: BinaryAssociation = BinaryAssociation(
    name="concrete278",
    ends={
        Property(name="OclExpression279", type=gbind_dsl_OclFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_OclFeatureBinding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body280: BinaryAssociation = BinaryAssociation(
    name="body280",
    ends={
        Property(name="OclExpression281", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseHelper", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type282: BinaryAssociation = BinaryAssociation(
    name="type282",
    ends={
        Property(name="OclType284", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseHelper283", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model_285: BinaryAssociation = BinaryAssociation(
    name="model_285",
    ends={
        Property(name="dsl287", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="BindingModel286", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
qualifier288: BinaryAssociation = BinaryAssociation(
    name="qualifier288",
    ends={
        Property(name="ConcreteMetaclass289", type=gbind_dsl_ConceptHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptHelper", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
contextClass290: BinaryAssociation = BinaryAssociation(
    name="contextClass290",
    ends={
        Property(name="ConceptMetaclass292", type=gbind_dsl_ConceptHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptHelper291", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
context293: BinaryAssociation = BinaryAssociation(
    name="context293",
    ends={
        Property(name="ConcreteMetaclass294", type=gbind_dsl_LocalHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_LocalHelper", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
parameters295: BinaryAssociation = BinaryAssociation(
    name="parameters295",
    ends={
        Property(name="HelperParameter", type=gbind_dsl_LocalHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_LocalHelper296", type=HelperParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier275: BinaryAssociation = BinaryAssociation(
    name="qualifier275",
    ends={
        Property(name="ConcreteMetaclass277", type=gbind_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseFeatureBinding276", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gbind_simpleocl_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_NamedElement)
gen_gbind_simpleocl_Module_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_Module)
gen_gbind_simpleocl_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_ModuleElement)
gen_gbind_simpleocl_Import_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_Import)
gen_gbind_simpleocl_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclExpression)
gen_gbind_simpleocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_VariableExp)
gen_gbind_simpleocl_SuperExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_SuperExp)
gen_gbind_simpleocl_SelfExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_SelfExp)
gen_gbind_simpleocl_EnvExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_EnvExp)
gen_gbind_simpleocl_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_PrimitiveExp)
gen_gbind_simpleocl_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_BooleanExp)
gen_gbind_simpleocl_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_NumericExp)
gen_gbind_simpleocl_RealExp_NumericExp = Generalization(general=NumericExp, specific=gbind_simpleocl_RealExp)
gen_gbind_simpleocl_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=gbind_simpleocl_IntegerExp)
gen_gbind_simpleocl_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_CollectionExp)
gen_gbind_simpleocl_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=gbind_simpleocl_BagExp)
gen_gbind_simpleocl_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=gbind_simpleocl_OrderedSetExp)
gen_gbind_simpleocl_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=gbind_simpleocl_SequenceExp)
gen_gbind_simpleocl_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=gbind_simpleocl_SetExp)
gen_gbind_simpleocl_TupleExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_TupleExp)
gen_gbind_simpleocl_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=gbind_simpleocl_TuplePart)
gen_gbind_simpleocl_MapExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_MapExp)
gen_gbind_simpleocl_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_MapElement)
gen_gbind_simpleocl_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_StringExp)
gen_gbind_simpleocl_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_EnumLiteralExp)
gen_gbind_simpleocl_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OclUndefinedExp)
gen_gbind_simpleocl_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_StaticPropertyCallExp)
gen_gbind_simpleocl_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_StaticPropertyCall)
gen_gbind_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=gbind_simpleocl_StaticNavigationOrAttributeCall)
gen_gbind_simpleocl_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=gbind_simpleocl_StaticOperationCall)
gen_gbind_simpleocl_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_PropertyCallExp)
gen_gbind_simpleocl_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_PropertyCall)
gen_gbind_simpleocl_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_NavigationOrAttributeCall)
gen_gbind_simpleocl_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_OperationCall)
gen_gbind_simpleocl_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OperatorCallExp)
gen_gbind_simpleocl_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_NotOpCallExp)
gen_gbind_simpleocl_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_RelOpCallExp)
gen_gbind_simpleocl_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_EqOpCallExp)
gen_gbind_simpleocl_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_AddOpCallExp)
gen_gbind_simpleocl_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_IntOpCallExp)
gen_gbind_simpleocl_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_MulOpCallExp)
gen_gbind_simpleocl_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=gbind_simpleocl_LambdaCallExp)
gen_gbind_simpleocl_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=gbind_simpleocl_CollectionOperationCall)
gen_gbind_simpleocl_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_LoopExp)
gen_gbind_simpleocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=gbind_simpleocl_IterateExp)
gen_gbind_simpleocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=gbind_simpleocl_IteratorExp)
gen_gbind_simpleocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_LetExp)
gen_gbind_simpleocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_IfExp)
gen_gbind_simpleocl_BraceExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_BraceExp)
gen_gbind_simpleocl_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_VariableDeclaration)
gen_gbind_simpleocl_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_LocalVariable)
gen_gbind_simpleocl_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_Iterator)
gen_gbind_simpleocl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_Parameter)
gen_gbind_simpleocl_CollectionType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_CollectionType)
gen_gbind_simpleocl_OclType_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclType)
gen_gbind_simpleocl_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OclModelElementExp)
gen_gbind_simpleocl_Primitive_OclType = Generalization(general=OclType, specific=gbind_simpleocl_Primitive)
gen_gbind_simpleocl_StringType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_StringType)
gen_gbind_simpleocl_BooleanType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_BooleanType)
gen_gbind_simpleocl_NumericType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_NumericType)
gen_gbind_simpleocl_IntegerType_NumericType = Generalization(general=NumericType, specific=gbind_simpleocl_IntegerType)
gen_gbind_simpleocl_RealType_NumericType = Generalization(general=NumericType, specific=gbind_simpleocl_RealType)
gen_gbind_simpleocl_BagType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_BagType)
gen_gbind_simpleocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_OrderedSetType)
gen_gbind_simpleocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_SequenceType)
gen_gbind_simpleocl_SetType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_SetType)
gen_gbind_simpleocl_OclAnyType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_OclAnyType)
gen_gbind_simpleocl_TupleType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_TupleType)
gen_gbind_simpleocl_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_TupleTypeAttribute)
gen_gbind_simpleocl_MapType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_MapType)
gen_gbind_simpleocl_LambdaType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_LambdaType)
gen_gbind_simpleocl_EnvType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_EnvType)
gen_gbind_simpleocl_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=gbind_simpleocl_OclFeatureDefinition)
gen_gbind_simpleocl_OclModelElement_OclType = Generalization(general=OclType, specific=gbind_simpleocl_OclModelElement)
gen_gbind_simpleocl_OclFeature_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_OclFeature)
gen_gbind_simpleocl_Attribute_OclFeature = Generalization(general=OclFeature, specific=gbind_simpleocl_Attribute)
gen_gbind_simpleocl_Operation_OclFeature = Generalization(general=OclFeature, specific=gbind_simpleocl_Operation)
gen_gbind_simpleocl_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclContextDefinition)
gen_gbind_simpleocl_OclModel_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_OclModel)
gen_gbind_simpleocl_OclMetamodel_OclModel = Generalization(general=OclModel, specific=gbind_simpleocl_OclMetamodel)
gen_gbind_simpleocl_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=gbind_simpleocl_OclInstanceModel)
gen_gbind_dsl_MetamodelDeclaration_OclMetamodel = Generalization(general=OclMetamodel, specific=gbind_dsl_MetamodelDeclaration)
gen_gbind_dsl_ConceptMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_ConceptMetaclass)
gen_gbind_dsl_ConcreteMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_ConcreteMetaclass)
gen_gbind_dsl_IntermediateClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_IntermediateClassBinding)
gen_gbind_dsl_ConcreteReferencDeclaringVar_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_dsl_ConcreteReferencDeclaringVar)
gen_gbind_dsl_VirtualMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_VirtualMetaclass)
gen_gbind_dsl_ClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_ClassBinding)
gen_gbind_dsl_VirtualReference_VirtualFeature = Generalization(general=VirtualFeature, specific=gbind_dsl_VirtualReference)
gen_gbind_dsl_VirtualAttribute_VirtualFeature = Generalization(general=VirtualFeature, specific=gbind_dsl_VirtualAttribute)
gen_gbind_dsl_VirtualClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_VirtualClassBinding)
gen_gbind_dsl_BaseFeatureBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_BaseFeatureBinding)
gen_gbind_dsl_OclFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=gbind_dsl_OclFeatureBinding)
gen_gbind_dsl_ConceptHelper_BaseHelper = Generalization(general=BaseHelper, specific=gbind_dsl_ConceptHelper)
gen_gbind_dsl_LocalHelper_BaseHelper = Generalization(general=BaseHelper, specific=gbind_dsl_LocalHelper)
gen_gbind_dsl_HelperParameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_dsl_HelperParameter)
gen_gbind_dsl_RenamingFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=gbind_dsl_RenamingFeatureBinding)

# Domain Model
domain_model = DomainModel(
    name="gbind",
    types={gbind_simpleocl_LocatedElement, gbind_simpleocl_NamedElement, LocatedElement, gbind_simpleocl_Module, NamedElement, OclMetamodel, Import, ModuleElement, gbind_simpleocl_ModuleElement, Module, gbind_simpleocl_Import, gbind_simpleocl_OclExpression, OclType, IfExp, PropertyCallExp, LetExp, LoopExp, OperationCall, LocalVariable, Operation, Attribute, OperatorCallExp, gbind_simpleocl_VariableExp, OclExpression, VariableDeclaration, gbind_simpleocl_SuperExp, gbind_simpleocl_SelfExp, gbind_simpleocl_EnvExp, gbind_simpleocl_PrimitiveExp, gbind_simpleocl_StringExp, CollectionExp, gbind_simpleocl_BooleanExp, gbind_simpleocl_NumericExp, gbind_simpleocl_RealExp, NumericExp, gbind_simpleocl_IntegerExp, gbind_simpleocl_CollectionExp, gbind_simpleocl_BagExp, gbind_simpleocl_OrderedSetExp, gbind_simpleocl_SequenceExp, gbind_simpleocl_SetExp, gbind_simpleocl_TupleExp, TuplePart, gbind_simpleocl_TuplePart, TupleExp, gbind_simpleocl_MapExp, MapElement, gbind_simpleocl_MapElement, PrimitiveExp, gbind_simpleocl_EnumLiteralExp, gbind_simpleocl_OclUndefinedExp, gbind_simpleocl_StaticPropertyCallExp, StaticPropertyCall, gbind_simpleocl_StaticPropertyCall, StaticPropertyCallExp, gbind_simpleocl_StaticNavigationOrAttributeCall, gbind_simpleocl_StaticOperationCall, gbind_simpleocl_PropertyCallExp, PropertyCall, MapExp, gbind_simpleocl_PropertyCall, gbind_simpleocl_NavigationOrAttributeCall, gbind_simpleocl_OperationCall, gbind_simpleocl_OperatorCallExp, gbind_simpleocl_NotOpCallExp, gbind_simpleocl_RelOpCallExp, gbind_simpleocl_EqOpCallExp, gbind_simpleocl_AddOpCallExp, gbind_simpleocl_IntOpCallExp, gbind_simpleocl_MulOpCallExp, gbind_simpleocl_LambdaCallExp, VariableExp, gbind_simpleocl_CollectionOperationCall, gbind_simpleocl_LoopExp, Iterator, gbind_simpleocl_IterateExp, gbind_simpleocl_IteratorExp, gbind_simpleocl_LetExp, gbind_simpleocl_IfExp, gbind_simpleocl_BraceExp, gbind_simpleocl_VariableDeclaration, gbind_simpleocl_LocalVariable, IterateExp, gbind_simpleocl_Iterator, gbind_simpleocl_Parameter, gbind_simpleocl_CollectionType, gbind_simpleocl_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, LambdaType, gbind_simpleocl_OclModelElementExp, OclModel, gbind_simpleocl_Primitive, gbind_simpleocl_StringType, Primitive, gbind_simpleocl_BooleanType, gbind_simpleocl_NumericType, gbind_simpleocl_IntegerType, NumericType, gbind_simpleocl_RealType, gbind_simpleocl_BagType, gbind_simpleocl_OrderedSetType, gbind_simpleocl_SequenceType, gbind_simpleocl_SetType, gbind_simpleocl_OclAnyType, gbind_simpleocl_TupleType, gbind_simpleocl_TupleTypeAttribute, TupleType, gbind_simpleocl_MapType, gbind_simpleocl_LambdaType, gbind_simpleocl_EnvType, gbind_simpleocl_OclFeatureDefinition, OclFeature, gbind_simpleocl_OclModelElement, OclFeatureDefinition, gbind_simpleocl_OclFeature, gbind_simpleocl_Attribute, gbind_simpleocl_Operation, Parameter_, gbind_simpleocl_OclContextDefinition, gbind_simpleocl_OclModel, OclModelElement, gbind_simpleocl_OclMetamodel, OclInstanceModel, gbind_simpleocl_OclInstanceModel, gbind_dsl_BindingModel, ConceptBinding, BaseHelper, ConceptMetaclass, VirtualMetaclass, MetamodelDeclaration, BindingOptions, gbind_dsl_BindingOptions, gbind_dsl_MetamodelDeclaration, gbind_dsl_Metaclass, dsl_gbind_EClass, gbind_dsl_ConceptMetaclass, Metaclass, gbind_dsl_ConcreteMetaclass, gbind_dsl_ConceptBinding, BindingModel, ConcreteMetaclass, gbind_dsl_IntermediateClassBinding, ConcreteReferencDeclaringVar, BaseFeatureBinding, gbind_dsl_ConcreteReferencDeclaringVar, gbind_dsl_VirtualMetaclass, VirtualReference, VirtualAttribute, gbind_dsl_ClassBinding, gbind_dsl_VirtualFeature, gbind_dsl_VirtualReference, VirtualFeature, gbind_dsl_VirtualAttribute, gbind_dsl_VirtualClassBinding, ConceptFeatureRef, gbind_dsl_ConceptFeatureRef, gbind_dsl_BaseFeatureBinding, gbind_dsl_OclFeatureBinding, gbind_dsl_BaseHelper, gbind_dsl_ConceptHelper, gbind_dsl_LocalHelper, HelperParameter, gbind_dsl_HelperParameter, gbind_dsl_RenamingFeatureBinding},
    associations={metamodels0, imports1, elements2, module4, module6, type9, ifExp311, letExp17, loopExp19, parentOperation21, initializedVariable23, ifExp225, owningOperation28, ifExp130, owningAttribute33, appliedOperator35, referredVariable37, appliedProperty13, collection15, elements39, tuplePart41, tuple43, elements45, key49, value51, source54, staticCall57, staticCallExp59, arguments61, calls63, map47, callExp68, arguments71, argument74, source76, arguments79, source65, exp81, body83, iterators86, result88, variable91, in_94, thenExpression97, condition100, elseExpression103, type106, variableExp109, letExp111, baseExp117, loopExpr119, operation122, elementType125, definitions128, oclExpression130, initExpression114, mapType2136, attribute138, mapType141, collectionTypes144, tupleTypeAttribute146, variableDeclaration148, lambdaReturnType151, lambdaArgType153, staticPropertyCall156, model159, operation133, attributes160, type163, tupleType166, model168, valueType171, keyType174, returnType177, argumentTypes180, feature183, context_185, definition188, context_190, definition193, initExpression196, type199, parameters202, returnType204, elements210, model212, metamodel214, bindings217, helpers218, conceptMetaclasses220, body207, virtualMetaclasses223, boundConcept225, boundMetamodel227, options230, eclass232, model_233, concreteMetaclasses221, concrete237, whenClause240, concept243, concreteClass245, concreteReference248, conceptContext250, featureBindings253, references255, concept235, type_261, type_263, concept264, virtual266, refFeatures269, conceptClass271, conceptClass273, attributes256, init258, concrete278, body280, type282, model_285, qualifier288, contextClass290, context293, parameters295, qualifier275},
    generalizations={gen_gbind_simpleocl_NamedElement_LocatedElement, gen_gbind_simpleocl_Module_NamedElement, gen_gbind_simpleocl_ModuleElement_LocatedElement, gen_gbind_simpleocl_Import_NamedElement, gen_gbind_simpleocl_OclExpression_LocatedElement, gen_gbind_simpleocl_VariableExp_OclExpression, gen_gbind_simpleocl_SuperExp_OclExpression, gen_gbind_simpleocl_SelfExp_OclExpression, gen_gbind_simpleocl_EnvExp_OclExpression, gen_gbind_simpleocl_PrimitiveExp_OclExpression, gen_gbind_simpleocl_BooleanExp_PrimitiveExp, gen_gbind_simpleocl_NumericExp_PrimitiveExp, gen_gbind_simpleocl_RealExp_NumericExp, gen_gbind_simpleocl_IntegerExp_NumericExp, gen_gbind_simpleocl_CollectionExp_OclExpression, gen_gbind_simpleocl_BagExp_CollectionExp, gen_gbind_simpleocl_OrderedSetExp_CollectionExp, gen_gbind_simpleocl_SequenceExp_CollectionExp, gen_gbind_simpleocl_SetExp_CollectionExp, gen_gbind_simpleocl_TupleExp_OclExpression, gen_gbind_simpleocl_TuplePart_LocalVariable, gen_gbind_simpleocl_MapExp_OclExpression, gen_gbind_simpleocl_MapElement_LocatedElement, gen_gbind_simpleocl_StringExp_PrimitiveExp, gen_gbind_simpleocl_EnumLiteralExp_OclExpression, gen_gbind_simpleocl_OclUndefinedExp_OclExpression, gen_gbind_simpleocl_StaticPropertyCallExp_OclExpression, gen_gbind_simpleocl_StaticPropertyCall_LocatedElement, gen_gbind_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_gbind_simpleocl_StaticOperationCall_StaticPropertyCall, gen_gbind_simpleocl_PropertyCallExp_OclExpression, gen_gbind_simpleocl_PropertyCall_LocatedElement, gen_gbind_simpleocl_NavigationOrAttributeCall_PropertyCall, gen_gbind_simpleocl_OperationCall_PropertyCall, gen_gbind_simpleocl_OperatorCallExp_OclExpression, gen_gbind_simpleocl_NotOpCallExp_OperatorCallExp, gen_gbind_simpleocl_RelOpCallExp_OperatorCallExp, gen_gbind_simpleocl_EqOpCallExp_OperatorCallExp, gen_gbind_simpleocl_AddOpCallExp_OperatorCallExp, gen_gbind_simpleocl_IntOpCallExp_OperatorCallExp, gen_gbind_simpleocl_MulOpCallExp_OperatorCallExp, gen_gbind_simpleocl_LambdaCallExp_VariableExp, gen_gbind_simpleocl_CollectionOperationCall_OperationCall, gen_gbind_simpleocl_LoopExp_PropertyCall, gen_gbind_simpleocl_IterateExp_LoopExp, gen_gbind_simpleocl_IteratorExp_LoopExp, gen_gbind_simpleocl_LetExp_OclExpression, gen_gbind_simpleocl_IfExp_OclExpression, gen_gbind_simpleocl_BraceExp_OclExpression, gen_gbind_simpleocl_VariableDeclaration_LocatedElement, gen_gbind_simpleocl_LocalVariable_VariableDeclaration, gen_gbind_simpleocl_Iterator_VariableDeclaration, gen_gbind_simpleocl_Parameter_VariableDeclaration, gen_gbind_simpleocl_CollectionType_OclType, gen_gbind_simpleocl_OclType_LocatedElement, gen_gbind_simpleocl_OclModelElementExp_OclExpression, gen_gbind_simpleocl_Primitive_OclType, gen_gbind_simpleocl_StringType_Primitive, gen_gbind_simpleocl_BooleanType_Primitive, gen_gbind_simpleocl_NumericType_Primitive, gen_gbind_simpleocl_IntegerType_NumericType, gen_gbind_simpleocl_RealType_NumericType, gen_gbind_simpleocl_BagType_CollectionType, gen_gbind_simpleocl_OrderedSetType_CollectionType, gen_gbind_simpleocl_SequenceType_CollectionType, gen_gbind_simpleocl_SetType_CollectionType, gen_gbind_simpleocl_OclAnyType_OclType, gen_gbind_simpleocl_TupleType_OclType, gen_gbind_simpleocl_TupleTypeAttribute_LocatedElement, gen_gbind_simpleocl_MapType_OclType, gen_gbind_simpleocl_LambdaType_OclType, gen_gbind_simpleocl_EnvType_OclType, gen_gbind_simpleocl_OclFeatureDefinition_ModuleElement, gen_gbind_simpleocl_OclModelElement_OclType, gen_gbind_simpleocl_OclFeature_NamedElement, gen_gbind_simpleocl_Attribute_OclFeature, gen_gbind_simpleocl_Operation_OclFeature, gen_gbind_simpleocl_OclContextDefinition_LocatedElement, gen_gbind_simpleocl_OclModel_NamedElement, gen_gbind_simpleocl_OclMetamodel_OclModel, gen_gbind_simpleocl_OclInstanceModel_OclModel, gen_gbind_dsl_MetamodelDeclaration_OclMetamodel, gen_gbind_dsl_ConceptMetaclass_Metaclass, gen_gbind_dsl_ConcreteMetaclass_Metaclass, gen_gbind_dsl_IntermediateClassBinding_ConceptBinding, gen_gbind_dsl_ConcreteReferencDeclaringVar_VariableDeclaration, gen_gbind_dsl_VirtualMetaclass_Metaclass, gen_gbind_dsl_ClassBinding_ConceptBinding, gen_gbind_dsl_VirtualReference_VirtualFeature, gen_gbind_dsl_VirtualAttribute_VirtualFeature, gen_gbind_dsl_VirtualClassBinding_ConceptBinding, gen_gbind_dsl_BaseFeatureBinding_ConceptBinding, gen_gbind_dsl_OclFeatureBinding_BaseFeatureBinding, gen_gbind_dsl_ConceptHelper_BaseHelper, gen_gbind_dsl_LocalHelper_BaseHelper, gen_gbind_dsl_HelperParameter_VariableDeclaration, gen_gbind_dsl_RenamingFeatureBinding_BaseFeatureBinding},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)