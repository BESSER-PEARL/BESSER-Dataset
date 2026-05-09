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
gbind_simpleocl_LocatedElement = Class(name="gbind_simpleocl_LocatedElement", is_abstract=True)
gbind_simpleocl_Import = Class(name="gbind_simpleocl_Import")
gbind_simpleocl_OclExpression = Class(name="gbind_simpleocl_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCall = Class(name="OperationCall")
LocalVariable = Class(name="LocalVariable")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OperatorCallExp = Class(name="OperatorCallExp")
gbind_simpleocl_NamedElement = Class(name="gbind_simpleocl_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
gbind_simpleocl_Module = Class(name="gbind_simpleocl_Module")
NamedElement = Class(name="NamedElement")
OclMetamodel = Class(name="OclMetamodel")
Import = Class(name="Import")
ModuleElement = Class(name="ModuleElement")
gbind_simpleocl_ModuleElement = Class(name="gbind_simpleocl_ModuleElement", is_abstract=True)
Module = Class(name="Module")
gbind_simpleocl_IntegerExp = Class(name="gbind_simpleocl_IntegerExp")
gbind_simpleocl_CollectionExp = Class(name="gbind_simpleocl_CollectionExp", is_abstract=True)
gbind_simpleocl_BagExp = Class(name="gbind_simpleocl_BagExp")
gbind_simpleocl_OrderedSetExp = Class(name="gbind_simpleocl_OrderedSetExp")
gbind_simpleocl_SequenceExp = Class(name="gbind_simpleocl_SequenceExp")
gbind_simpleocl_SetExp = Class(name="gbind_simpleocl_SetExp")
gbind_simpleocl_TupleExp = Class(name="gbind_simpleocl_TupleExp")
TuplePart = Class(name="TuplePart")
gbind_simpleocl_TuplePart = Class(name="gbind_simpleocl_TuplePart")
TupleExp = Class(name="TupleExp")
gbind_simpleocl_MapExp = Class(name="gbind_simpleocl_MapExp")
MapElement = Class(name="MapElement")
gbind_simpleocl_MapElement = Class(name="gbind_simpleocl_MapElement")
MapExp = Class(name="MapExp")
gbind_simpleocl_EnumLiteralExp = Class(name="gbind_simpleocl_EnumLiteralExp")
gbind_simpleocl_VariableExp = Class(name="gbind_simpleocl_VariableExp")
OclExpression = Class(name="OclExpression")
VariableDeclaration = Class(name="VariableDeclaration")
gbind_simpleocl_SuperExp = Class(name="gbind_simpleocl_SuperExp")
gbind_simpleocl_SelfExp = Class(name="gbind_simpleocl_SelfExp")
gbind_simpleocl_EnvExp = Class(name="gbind_simpleocl_EnvExp")
gbind_simpleocl_PrimitiveExp = Class(name="gbind_simpleocl_PrimitiveExp", is_abstract=True)
gbind_simpleocl_StringExp = Class(name="gbind_simpleocl_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
gbind_simpleocl_BooleanExp = Class(name="gbind_simpleocl_BooleanExp")
gbind_simpleocl_NumericExp = Class(name="gbind_simpleocl_NumericExp", is_abstract=True)
gbind_simpleocl_RealExp = Class(name="gbind_simpleocl_RealExp")
NumericExp = Class(name="NumericExp")
gbind_simpleocl_PropertyCallExp = Class(name="gbind_simpleocl_PropertyCallExp")
PropertyCall = Class(name="PropertyCall")
gbind_simpleocl_PropertyCall = Class(name="gbind_simpleocl_PropertyCall", is_abstract=True)
gbind_simpleocl_NavigationOrAttributeCall = Class(name="gbind_simpleocl_NavigationOrAttributeCall")
gbind_simpleocl_OperationCall = Class(name="gbind_simpleocl_OperationCall")
gbind_simpleocl_OperatorCallExp = Class(name="gbind_simpleocl_OperatorCallExp")
gbind_simpleocl_NotOpCallExp = Class(name="gbind_simpleocl_NotOpCallExp")
gbind_simpleocl_OclUndefinedExp = Class(name="gbind_simpleocl_OclUndefinedExp")
gbind_simpleocl_StaticPropertyCallExp = Class(name="gbind_simpleocl_StaticPropertyCallExp")
StaticPropertyCall = Class(name="StaticPropertyCall")
gbind_simpleocl_StaticPropertyCall = Class(name="gbind_simpleocl_StaticPropertyCall", is_abstract=True)
StaticPropertyCallExp = Class(name="StaticPropertyCallExp")
gbind_simpleocl_StaticNavigationOrAttributeCall = Class(name="gbind_simpleocl_StaticNavigationOrAttributeCall")
gbind_simpleocl_StaticOperationCall = Class(name="gbind_simpleocl_StaticOperationCall")
Iterator = Class(name="Iterator")
gbind_simpleocl_IterateExp = Class(name="gbind_simpleocl_IterateExp")
gbind_simpleocl_IteratorExp = Class(name="gbind_simpleocl_IteratorExp")
gbind_simpleocl_LetExp = Class(name="gbind_simpleocl_LetExp")
gbind_simpleocl_IfExp = Class(name="gbind_simpleocl_IfExp")
gbind_simpleocl_VariableDeclaration = Class(name="gbind_simpleocl_VariableDeclaration", is_abstract=True)
gbind_simpleocl_RelOpCallExp = Class(name="gbind_simpleocl_RelOpCallExp")
gbind_simpleocl_EqOpCallExp = Class(name="gbind_simpleocl_EqOpCallExp")
gbind_simpleocl_AddOpCallExp = Class(name="gbind_simpleocl_AddOpCallExp")
gbind_simpleocl_IntOpCallExp = Class(name="gbind_simpleocl_IntOpCallExp")
gbind_simpleocl_MulOpCallExp = Class(name="gbind_simpleocl_MulOpCallExp")
gbind_simpleocl_LambdaCallExp = Class(name="gbind_simpleocl_LambdaCallExp")
VariableExp = Class(name="VariableExp")
gbind_simpleocl_BraceExp = Class(name="gbind_simpleocl_BraceExp")
gbind_simpleocl_CollectionOperationCall = Class(name="gbind_simpleocl_CollectionOperationCall")
gbind_simpleocl_LoopExp = Class(name="gbind_simpleocl_LoopExp", is_abstract=True)
gbind_simpleocl_Parameter = Class(name="gbind_simpleocl_Parameter")
gbind_simpleocl_CollectionType = Class(name="gbind_simpleocl_CollectionType")
gbind_simpleocl_OclType = Class(name="gbind_simpleocl_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
gbind_simpleocl_LocalVariable = Class(name="gbind_simpleocl_LocalVariable")
IterateExp = Class(name="IterateExp")
gbind_simpleocl_Iterator = Class(name="gbind_simpleocl_Iterator")
gbind_simpleocl_RealType = Class(name="gbind_simpleocl_RealType")
gbind_simpleocl_BagType = Class(name="gbind_simpleocl_BagType")
gbind_simpleocl_OrderedSetType = Class(name="gbind_simpleocl_OrderedSetType")
gbind_simpleocl_SequenceType = Class(name="gbind_simpleocl_SequenceType")
gbind_simpleocl_SetType = Class(name="gbind_simpleocl_SetType")
gbind_simpleocl_OclAnyType = Class(name="gbind_simpleocl_OclAnyType")
gbind_simpleocl_TupleType = Class(name="gbind_simpleocl_TupleType")
gbind_simpleocl_TupleTypeAttribute = Class(name="gbind_simpleocl_TupleTypeAttribute")
TupleType = Class(name="TupleType")
gbind_simpleocl_OclModelElement = Class(name="gbind_simpleocl_OclModelElement")
gbind_simpleocl_MapType = Class(name="gbind_simpleocl_MapType")
gbind_simpleocl_LambdaType = Class(name="gbind_simpleocl_LambdaType")
LambdaType = Class(name="LambdaType")
gbind_simpleocl_OclModelElementExp = Class(name="gbind_simpleocl_OclModelElementExp")
OclModel = Class(name="OclModel")
gbind_simpleocl_Primitive = Class(name="gbind_simpleocl_Primitive", is_abstract=True)
gbind_simpleocl_StringType = Class(name="gbind_simpleocl_StringType")
Primitive = Class(name="Primitive")
gbind_simpleocl_BooleanType = Class(name="gbind_simpleocl_BooleanType")
gbind_simpleocl_NumericType = Class(name="gbind_simpleocl_NumericType", is_abstract=True)
gbind_simpleocl_IntegerType = Class(name="gbind_simpleocl_IntegerType")
NumericType = Class(name="NumericType")
gbind_simpleocl_OclFeature = Class(name="gbind_simpleocl_OclFeature", is_abstract=True)
gbind_simpleocl_Attribute = Class(name="gbind_simpleocl_Attribute")
gbind_simpleocl_Operation = Class(name="gbind_simpleocl_Operation")
Parameter_ = Class(name="Parameter")
gbind_simpleocl_OclModel = Class(name="gbind_simpleocl_OclModel", is_abstract=True)
OclModelElement = Class(name="OclModelElement")
gbind_simpleocl_OclMetamodel = Class(name="gbind_simpleocl_OclMetamodel")
OclInstanceModel = Class(name="OclInstanceModel")
gbind_simpleocl_EnvType = Class(name="gbind_simpleocl_EnvType")
gbind_simpleocl_OclFeatureDefinition = Class(name="gbind_simpleocl_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
gbind_simpleocl_OclContextDefinition = Class(name="gbind_simpleocl_OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
VirtualMetaclass = Class(name="VirtualMetaclass")
MetamodelDeclaration = Class(name="MetamodelDeclaration")
BindingOptions = Class(name="BindingOptions")
gbind_dsl_BindingOptions = Class(name="gbind_dsl_BindingOptions")
gbind_dsl_MetamodelDeclaration = Class(name="gbind_dsl_MetamodelDeclaration")
gbind_dsl_Metaclass = Class(name="gbind_dsl_Metaclass", is_abstract=True)
dsl_gbind_EClass = Class(name="dsl_gbind_EClass")
gbind_dsl_ConceptMetaclass = Class(name="gbind_dsl_ConceptMetaclass")
Metaclass = Class(name="Metaclass")
gbind_dsl_ConcreteMetaclass = Class(name="gbind_dsl_ConcreteMetaclass")
gbind_dsl_ConceptBinding = Class(name="gbind_dsl_ConceptBinding", is_abstract=True)
BindingModel = Class(name="BindingModel")
gbind_dsl_ClassBinding = Class(name="gbind_dsl_ClassBinding")
gbind_simpleocl_OclInstanceModel = Class(name="gbind_simpleocl_OclInstanceModel")
gbind_dsl_BindingModel = Class(name="gbind_dsl_BindingModel")
ConceptBinding = Class(name="ConceptBinding")
BaseHelper = Class(name="BaseHelper")
ConceptMetaclass = Class(name="ConceptMetaclass")
ConcreteMetaclass = Class(name="ConcreteMetaclass")
gbind_dsl_VirtualFeature = Class(name="gbind_dsl_VirtualFeature")
gbind_dsl_VirtualReference = Class(name="gbind_dsl_VirtualReference")
VirtualFeature = Class(name="VirtualFeature")
gbind_dsl_VirtualAttribute = Class(name="gbind_dsl_VirtualAttribute")
gbind_dsl_VirtualClassBinding = Class(name="gbind_dsl_VirtualClassBinding")
ConceptFeatureRef = Class(name="ConceptFeatureRef")
gbind_dsl_ConceptFeatureRef = Class(name="gbind_dsl_ConceptFeatureRef")
gbind_dsl_BaseFeatureBinding = Class(name="gbind_dsl_BaseFeatureBinding")
gbind_dsl_RenamingFeatureBinding = Class(name="gbind_dsl_RenamingFeatureBinding")
gbind_dsl_IntermediateClassBinding = Class(name="gbind_dsl_IntermediateClassBinding")
ConcreteReferencDeclaringVar = Class(name="ConcreteReferencDeclaringVar")
BaseFeatureBinding = Class(name="BaseFeatureBinding")
gbind_dsl_ConcreteReferencDeclaringVar = Class(name="gbind_dsl_ConcreteReferencDeclaringVar")
gbind_dsl_VirtualMetaclass = Class(name="gbind_dsl_VirtualMetaclass")
VirtualReference = Class(name="VirtualReference")
VirtualAttribute = Class(name="VirtualAttribute")
gbind_dsl_LocalHelper = Class(name="gbind_dsl_LocalHelper")
HelperParameter = Class(name="HelperParameter")
gbind_dsl_HelperParameter = Class(name="gbind_dsl_HelperParameter")
gbind_dsl_OclFeatureBinding = Class(name="gbind_dsl_OclFeatureBinding")
gbind_dsl_BaseHelper = Class(name="gbind_dsl_BaseHelper")
gbind_dsl_ConceptHelper = Class(name="gbind_dsl_ConceptHelper")

# gbind_simpleocl_LocatedElement class attributes and methods
gbind_simpleocl_LocatedElement_line: Property = Property(name="line", type=StringType)
gbind_simpleocl_LocatedElement_column: Property = Property(name="column", type=StringType)
gbind_simpleocl_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
gbind_simpleocl_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
gbind_simpleocl_LocatedElement.attributes={gbind_simpleocl_LocatedElement_column, gbind_simpleocl_LocatedElement_charEnd, gbind_simpleocl_LocatedElement_charStart, gbind_simpleocl_LocatedElement_line}

# gbind_simpleocl_Import class attributes and methods

# gbind_simpleocl_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCall class attributes and methods

# LocalVariable class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OperatorCallExp class attributes and methods

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

# MapExp class attributes and methods

# gbind_simpleocl_EnumLiteralExp class attributes and methods
gbind_simpleocl_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_EnumLiteralExp.attributes={gbind_simpleocl_EnumLiteralExp_name}

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

# PrimitiveExp class attributes and methods

# gbind_simpleocl_BooleanExp class attributes and methods
gbind_simpleocl_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
gbind_simpleocl_BooleanExp.attributes={gbind_simpleocl_BooleanExp_booleanSymbol}

# gbind_simpleocl_NumericExp class attributes and methods

# gbind_simpleocl_RealExp class attributes and methods
gbind_simpleocl_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
gbind_simpleocl_RealExp.attributes={gbind_simpleocl_RealExp_realSymbol}

# NumericExp class attributes and methods

# gbind_simpleocl_PropertyCallExp class attributes and methods

# PropertyCall class attributes and methods

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

# Iterator class attributes and methods

# gbind_simpleocl_IterateExp class attributes and methods

# gbind_simpleocl_IteratorExp class attributes and methods
gbind_simpleocl_IteratorExp_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_IteratorExp.attributes={gbind_simpleocl_IteratorExp_name}

# gbind_simpleocl_LetExp class attributes and methods

# gbind_simpleocl_IfExp class attributes and methods

# gbind_simpleocl_VariableDeclaration class attributes and methods
gbind_simpleocl_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
gbind_simpleocl_VariableDeclaration.attributes={gbind_simpleocl_VariableDeclaration_varName}

# gbind_simpleocl_RelOpCallExp class attributes and methods

# gbind_simpleocl_EqOpCallExp class attributes and methods

# gbind_simpleocl_AddOpCallExp class attributes and methods

# gbind_simpleocl_IntOpCallExp class attributes and methods

# gbind_simpleocl_MulOpCallExp class attributes and methods

# gbind_simpleocl_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# gbind_simpleocl_BraceExp class attributes and methods

# gbind_simpleocl_CollectionOperationCall class attributes and methods

# gbind_simpleocl_LoopExp class attributes and methods

# gbind_simpleocl_Parameter class attributes and methods

# gbind_simpleocl_CollectionType class attributes and methods

# gbind_simpleocl_OclType class attributes and methods
gbind_simpleocl_OclType_name: Property = Property(name="name", type=StringType)
gbind_simpleocl_OclType.attributes={gbind_simpleocl_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# gbind_simpleocl_LocalVariable class attributes and methods
gbind_simpleocl_LocalVariable_eq: Property = Property(name="eq", type=StringType)
gbind_simpleocl_LocalVariable.attributes={gbind_simpleocl_LocalVariable_eq}

# IterateExp class attributes and methods

# gbind_simpleocl_Iterator class attributes and methods

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

# gbind_simpleocl_OclModelElement class attributes and methods

# gbind_simpleocl_MapType class attributes and methods

# gbind_simpleocl_LambdaType class attributes and methods

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

# gbind_simpleocl_OclFeature class attributes and methods
gbind_simpleocl_OclFeature_eq: Property = Property(name="eq", type=StringType)
gbind_simpleocl_OclFeature.attributes={gbind_simpleocl_OclFeature_eq}

# gbind_simpleocl_Attribute class attributes and methods

# gbind_simpleocl_Operation class attributes and methods

# Parameter class attributes and methods

# gbind_simpleocl_OclModel class attributes and methods

# OclModelElement class attributes and methods

# gbind_simpleocl_OclMetamodel class attributes and methods
gbind_simpleocl_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
gbind_simpleocl_OclMetamodel.attributes={gbind_simpleocl_OclMetamodel_uri}

# OclInstanceModel class attributes and methods

# gbind_simpleocl_EnvType class attributes and methods

# gbind_simpleocl_OclFeatureDefinition class attributes and methods
gbind_simpleocl_OclFeatureDefinition_static: Property = Property(name="static", type=StringType)
gbind_simpleocl_OclFeatureDefinition.attributes={gbind_simpleocl_OclFeatureDefinition_static}

# OclFeature class attributes and methods

# gbind_simpleocl_OclContextDefinition class attributes and methods

# OclFeatureDefinition class attributes and methods

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

# gbind_dsl_ClassBinding class attributes and methods

# gbind_simpleocl_OclInstanceModel class attributes and methods

# gbind_dsl_BindingModel class attributes and methods
gbind_dsl_BindingModel_name: Property = Property(name="name", type=StringType)
gbind_dsl_BindingModel.attributes={gbind_dsl_BindingModel_name}

# ConceptBinding class attributes and methods

# BaseHelper class attributes and methods

# ConceptMetaclass class attributes and methods

# ConcreteMetaclass class attributes and methods

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

# gbind_dsl_RenamingFeatureBinding class attributes and methods
gbind_dsl_RenamingFeatureBinding_concreteFeature: Property = Property(name="concreteFeature", type=StringType)
gbind_dsl_RenamingFeatureBinding.attributes={gbind_dsl_RenamingFeatureBinding_concreteFeature}

# gbind_dsl_IntermediateClassBinding class attributes and methods
gbind_dsl_IntermediateClassBinding_conceptReferenceName: Property = Property(name="conceptReferenceName", type=StringType)
gbind_dsl_IntermediateClassBinding.attributes={gbind_dsl_IntermediateClassBinding_conceptReferenceName}

# ConcreteReferencDeclaringVar class attributes and methods

# BaseFeatureBinding class attributes and methods

# gbind_dsl_ConcreteReferencDeclaringVar class attributes and methods

# gbind_dsl_VirtualMetaclass class attributes and methods

# VirtualReference class attributes and methods

# VirtualAttribute class attributes and methods

# gbind_dsl_LocalHelper class attributes and methods

# HelperParameter class attributes and methods

# gbind_dsl_HelperParameter class attributes and methods

# gbind_dsl_OclFeatureBinding class attributes and methods

# gbind_dsl_BaseHelper class attributes and methods
gbind_dsl_BaseHelper_feature: Property = Property(name="feature", type=StringType)
gbind_dsl_BaseHelper.attributes={gbind_dsl_BaseHelper_feature}

# gbind_dsl_ConceptHelper class attributes and methods

# Relationships
module5: BinaryAssociation = BinaryAssociation(
    name="module5",
    ends={
        Property(name="Module6", type=gbind_simpleocl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="imports", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="OclType", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp38: BinaryAssociation = BinaryAssociation(
    name="ifExp38",
    ends={
        Property(name="IfExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty9: BinaryAssociation = BinaryAssociation(
    name="appliedProperty9",
    ends={
        Property(name="PropertyCallExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection10: BinaryAssociation = BinaryAssociation(
    name="collection10",
    ends={
        Property(name="CollectionExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements11", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp12: BinaryAssociation = BinaryAssociation(
    name="letExp12",
    ends={
        Property(name="LetExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp13: BinaryAssociation = BinaryAssociation(
    name="loopExp13",
    ends={
        Property(name="LoopExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation14: BinaryAssociation = BinaryAssociation(
    name="parentOperation14",
    ends={
        Property(name="OperationCall", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable15: BinaryAssociation = BinaryAssociation(
    name="initializedVariable15",
    ends={
        Property(name="LocalVariable", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp216: BinaryAssociation = BinaryAssociation(
    name="ifExp216",
    ends={
        Property(name="IfExp17", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation18: BinaryAssociation = BinaryAssociation(
    name="owningOperation18",
    ends={
        Property(name="Operation", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body19", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp120: BinaryAssociation = BinaryAssociation(
    name="ifExp120",
    ends={
        Property(name="IfExp21", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute22: BinaryAssociation = BinaryAssociation(
    name="owningAttribute22",
    ends={
        Property(name="Attribute", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression23", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
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
        Property(name="Import", type=gbind_simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="ModuleElement", type=gbind_simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module3", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module4: BinaryAssociation = BinaryAssociation(
    name="module4",
    ends={
        Property(name="Module", type=gbind_simpleocl_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
elements27: BinaryAssociation = BinaryAssociation(
    name="elements27",
    ends={
        Property(name="OclExpression", type=gbind_simpleocl_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart28: BinaryAssociation = BinaryAssociation(
    name="tuplePart28",
    ends={
        Property(name="TuplePart", type=gbind_simpleocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple29: BinaryAssociation = BinaryAssociation(
    name="tuple29",
    ends={
        Property(name="TupleExp", type=gbind_simpleocl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements30: BinaryAssociation = BinaryAssociation(
    name="elements30",
    ends={
        Property(name="MapElement", type=gbind_simpleocl_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map31: BinaryAssociation = BinaryAssociation(
    name="map31",
    ends={
        Property(name="MapExp", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements32", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key33: BinaryAssociation = BinaryAssociation(
    name="key33",
    ends={
        Property(name="OclExpression34", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="OclExpression37", type=gbind_simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_MapElement36", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
appliedOperator24: BinaryAssociation = BinaryAssociation(
    name="appliedOperator24",
    ends={
        Property(name="OperatorCallExp", type=gbind_simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source25", type=OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable26: BinaryAssociation = BinaryAssociation(
    name="referredVariable26",
    ends={
        Property(name="VariableDeclaration", type=gbind_simpleocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
calls44: BinaryAssociation = BinaryAssociation(
    name="calls44",
    ends={
        Property(name="PropertyCall", type=gbind_simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="callExp", type=PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source45: BinaryAssociation = BinaryAssociation(
    name="source45",
    ends={
        Property(name="OclExpression46", type=gbind_simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callExp47: BinaryAssociation = BinaryAssociation(
    name="callExp47",
    ends={
        Property(name="PropertyCallExp48", type=gbind_simpleocl_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="calls", type=PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments49: BinaryAssociation = BinaryAssociation(
    name="arguments49",
    ends={
        Property(name="OclExpression50", type=gbind_simpleocl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument51: BinaryAssociation = BinaryAssociation(
    name="argument51",
    ends={
        Property(name="OclExpression52", type=gbind_simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_OperatorCallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source53: BinaryAssociation = BinaryAssociation(
    name="source53",
    ends={
        Property(name="OclExpression54", type=gbind_simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedOperator", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source38: BinaryAssociation = BinaryAssociation(
    name="source38",
    ends={
        Property(name="OclType39", type=gbind_simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticPropertyCall", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall40: BinaryAssociation = BinaryAssociation(
    name="staticCall40",
    ends={
        Property(name="StaticPropertyCall", type=gbind_simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCallExp", type=StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp41: BinaryAssociation = BinaryAssociation(
    name="staticCallExp41",
    ends={
        Property(name="StaticPropertyCallExp", type=gbind_simpleocl_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCall", type=StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments42: BinaryAssociation = BinaryAssociation(
    name="arguments42",
    ends={
        Property(name="OclExpression43", type=gbind_simpleocl_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_StaticOperationCall", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterators61: BinaryAssociation = BinaryAssociation(
    name="iterators61",
    ends={
        Property(name="Iterator", type=gbind_simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result62: BinaryAssociation = BinaryAssociation(
    name="result62",
    ends={
        Property(name="LocalVariable63", type=gbind_simpleocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable64: BinaryAssociation = BinaryAssociation(
    name="variable64",
    ends={
        Property(name="LocalVariable65", type=gbind_simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_66: BinaryAssociation = BinaryAssociation(
    name="in_66",
    ends={
        Property(name="OclExpression68", type=gbind_simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp67", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression69: BinaryAssociation = BinaryAssociation(
    name="thenExpression69",
    ends={
        Property(name="OclExpression70", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition71: BinaryAssociation = BinaryAssociation(
    name="condition71",
    ends={
        Property(name="OclExpression72", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression73: BinaryAssociation = BinaryAssociation(
    name="elseExpression73",
    ends={
        Property(name="OclExpression74", type=gbind_simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments55: BinaryAssociation = BinaryAssociation(
    name="arguments55",
    ends={
        Property(name="OclExpression56", type=gbind_simpleocl_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_LambdaCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp57: BinaryAssociation = BinaryAssociation(
    name="exp57",
    ends={
        Property(name="OclExpression58", type=gbind_simpleocl_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_BraceExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body59: BinaryAssociation = BinaryAssociation(
    name="body59",
    ends={
        Property(name="OclExpression60", type=gbind_simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation85: BinaryAssociation = BinaryAssociation(
    name="operation85",
    ends={
        Property(name="Operation86", type=gbind_simpleocl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType87: BinaryAssociation = BinaryAssociation(
    name="elementType87",
    ends={
        Property(name="OclType88", type=gbind_simpleocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions89: BinaryAssociation = BinaryAssociation(
    name="definitions89",
    ends={
        Property(name="OclContextDefinition", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression90: BinaryAssociation = BinaryAssociation(
    name="oclExpression90",
    ends={
        Property(name="OclExpression91", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation92: BinaryAssociation = BinaryAssociation(
    name="operation92",
    ends={
        Property(name="Operation93", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType294: BinaryAssociation = BinaryAssociation(
    name="mapType294",
    ends={
        Property(name="MapType", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute95: BinaryAssociation = BinaryAssociation(
    name="attribute95",
    ends={
        Property(name="Attribute97", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type96", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType98: BinaryAssociation = BinaryAssociation(
    name="mapType98",
    ends={
        Property(name="MapType99", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes100: BinaryAssociation = BinaryAssociation(
    name="collectionTypes100",
    ends={
        Property(name="CollectionType", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute101: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute101",
    ends={
        Property(name="TupleTypeAttribute", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type102", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration103: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration103",
    ends={
        Property(name="VariableDeclaration105", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type104", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="OclType76", type=gbind_simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp77: BinaryAssociation = BinaryAssociation(
    name="variableExp77",
    ends={
        Property(name="VariableExp", type=gbind_simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp78: BinaryAssociation = BinaryAssociation(
    name="letExp78",
    ends={
        Property(name="LetExp79", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression80: BinaryAssociation = BinaryAssociation(
    name="initExpression80",
    ends={
        Property(name="OclExpression81", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp82: BinaryAssociation = BinaryAssociation(
    name="baseExp82",
    ends={
        Property(name="IterateExp", type=gbind_simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr83: BinaryAssociation = BinaryAssociation(
    name="loopExpr83",
    ends={
        Property(name="LoopExp84", type=gbind_simpleocl_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
attributes114: BinaryAssociation = BinaryAssociation(
    name="attributes114",
    ends={
        Property(name="TupleTypeAttribute115", type=gbind_simpleocl_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type116: BinaryAssociation = BinaryAssociation(
    name="type116",
    ends={
        Property(name="OclType117", type=gbind_simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType118: BinaryAssociation = BinaryAssociation(
    name="tupleType118",
    ends={
        Property(name="TupleType", type=gbind_simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model119: BinaryAssociation = BinaryAssociation(
    name="model119",
    ends={
        Property(name="OclModel121", type=gbind_simpleocl_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements120", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType122: BinaryAssociation = BinaryAssociation(
    name="valueType122",
    ends={
        Property(name="OclType123", type=gbind_simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType124: BinaryAssociation = BinaryAssociation(
    name="keyType124",
    ends={
        Property(name="OclType125", type=gbind_simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lambdaReturnType106: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType106",
    ends={
        Property(name="LambdaType", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType107", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
lambdaArgType108: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType108",
    ends={
        Property(name="LambdaType109", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="argumentTypes", type=LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
staticPropertyCall110: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall110",
    ends={
        Property(name="StaticPropertyCallExp112", type=gbind_simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="source111", type=StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
model113: BinaryAssociation = BinaryAssociation(
    name="model113",
    ends={
        Property(name="OclModel", type=gbind_simpleocl_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_simpleocl_OclModelElementExp", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
context_136: BinaryAssociation = BinaryAssociation(
    name="context_136",
    ends={
        Property(name="OclType137", type=gbind_simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition138: BinaryAssociation = BinaryAssociation(
    name="definition138",
    ends={
        Property(name="OclFeatureDefinition139", type=gbind_simpleocl_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression140: BinaryAssociation = BinaryAssociation(
    name="initExpression140",
    ends={
        Property(name="OclExpression141", type=gbind_simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="OclType143", type=gbind_simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters144: BinaryAssociation = BinaryAssociation(
    name="parameters144",
    ends={
        Property(name="Parameter", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType145: BinaryAssociation = BinaryAssociation(
    name="returnType145",
    ends={
        Property(name="OclType147", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation146", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body148: BinaryAssociation = BinaryAssociation(
    name="body148",
    ends={
        Property(name="OclExpression149", type=gbind_simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements150: BinaryAssociation = BinaryAssociation(
    name="elements150",
    ends={
        Property(name="OclModelElement", type=gbind_simpleocl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
returnType126: BinaryAssociation = BinaryAssociation(
    name="returnType126",
    ends={
        Property(name="OclType127", type=gbind_simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaReturnType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes128: BinaryAssociation = BinaryAssociation(
    name="argumentTypes128",
    ends={
        Property(name="OclType129", type=gbind_simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaArgType", type=OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature130: BinaryAssociation = BinaryAssociation(
    name="feature130",
    ends={
        Property(name="OclFeature", type=gbind_simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_131: BinaryAssociation = BinaryAssociation(
    name="context_131",
    ends={
        Property(name="OclContextDefinition133", type=gbind_simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition132", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition134: BinaryAssociation = BinaryAssociation(
    name="definition134",
    ends={
        Property(name="OclFeatureDefinition", type=gbind_simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_135", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
virtualMetaclasses161: BinaryAssociation = BinaryAssociation(
    name="virtualMetaclasses161",
    ends={
        Property(name="VirtualMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel162", type=VirtualMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundConcept163: BinaryAssociation = BinaryAssociation(
    name="boundConcept163",
    ends={
        Property(name="MetamodelDeclaration", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel164", type=MetamodelDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boundMetamodel165: BinaryAssociation = BinaryAssociation(
    name="boundMetamodel165",
    ends={
        Property(name="MetamodelDeclaration167", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel166", type=MetamodelDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
options168: BinaryAssociation = BinaryAssociation(
    name="options168",
    ends={
        Property(name="BindingOptions", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel169", type=BindingOptions, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eclass170: BinaryAssociation = BinaryAssociation(
    name="eclass170",
    ends={
        Property(name="dsl_gbind_EClass", type=gbind_dsl_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_Metaclass", type=dsl_gbind_EClass, multiplicity=Multiplicity(1, 1))
    }
)
model_171: BinaryAssociation = BinaryAssociation(
    name="model_171",
    ends={
        Property(name="BindingModel", type=gbind_dsl_ConceptBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
concept172: BinaryAssociation = BinaryAssociation(
    name="concept172",
    ends={
        Property(name="ConceptMetaclass173", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concrete174: BinaryAssociation = BinaryAssociation(
    name="concrete174",
    ends={
        Property(name="ConcreteMetaclass176", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding175", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 9999))
    }
)
whenClause177: BinaryAssociation = BinaryAssociation(
    name="whenClause177",
    ends={
        Property(name="OclExpression179", type=gbind_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ClassBinding178", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model151: BinaryAssociation = BinaryAssociation(
    name="model151",
    ends={
        Property(name="OclInstanceModel", type=gbind_simpleocl_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel152: BinaryAssociation = BinaryAssociation(
    name="metamodel152",
    ends={
        Property(name="OclMetamodel154", type=gbind_simpleocl_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model153", type=OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)
bindings155: BinaryAssociation = BinaryAssociation(
    name="bindings155",
    ends={
        Property(name="ConceptBinding", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_", type=ConceptBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers156: BinaryAssociation = BinaryAssociation(
    name="helpers156",
    ends={
        Property(name="BaseHelper", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_157", type=BaseHelper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptMetaclasses158: BinaryAssociation = BinaryAssociation(
    name="conceptMetaclasses158",
    ends={
        Property(name="ConceptMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel", type=ConceptMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concreteMetaclasses159: BinaryAssociation = BinaryAssociation(
    name="concreteMetaclasses159",
    ends={
        Property(name="ConcreteMetaclass", type=gbind_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BindingModel160", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init195: BinaryAssociation = BinaryAssociation(
    name="init195",
    ends={
        Property(name="OclExpression197", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass196", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type_198: BinaryAssociation = BinaryAssociation(
    name="type_198",
    ends={
        Property(name="ConcreteMetaclass199", type=gbind_dsl_VirtualReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualReference", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
type_200: BinaryAssociation = BinaryAssociation(
    name="type_200",
    ends={
        Property(name="Primitive", type=gbind_dsl_VirtualAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualAttribute", type=Primitive, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concept201: BinaryAssociation = BinaryAssociation(
    name="concept201",
    ends={
        Property(name="ConceptMetaclass202", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
virtual203: BinaryAssociation = BinaryAssociation(
    name="virtual203",
    ends={
        Property(name="VirtualMetaclass205", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding204", type=VirtualMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
refFeatures206: BinaryAssociation = BinaryAssociation(
    name="refFeatures206",
    ends={
        Property(name="ConceptFeatureRef", type=gbind_dsl_VirtualClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualClassBinding207", type=ConceptFeatureRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptClass208: BinaryAssociation = BinaryAssociation(
    name="conceptClass208",
    ends={
        Property(name="ConceptMetaclass209", type=gbind_dsl_ConceptFeatureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptFeatureRef", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
conceptClass210: BinaryAssociation = BinaryAssociation(
    name="conceptClass210",
    ends={
        Property(name="ConceptMetaclass211", type=gbind_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseFeatureBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
qualifier212: BinaryAssociation = BinaryAssociation(
    name="qualifier212",
    ends={
        Property(name="ConcreteMetaclass214", type=gbind_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseFeatureBinding213", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
concept180: BinaryAssociation = BinaryAssociation(
    name="concept180",
    ends={
        Property(name="ConceptMetaclass181", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concreteClass182: BinaryAssociation = BinaryAssociation(
    name="concreteClass182",
    ends={
        Property(name="ConcreteMetaclass184", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding183", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concreteReference185: BinaryAssociation = BinaryAssociation(
    name="concreteReference185",
    ends={
        Property(name="ConcreteReferencDeclaringVar", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding186", type=ConcreteReferencDeclaringVar, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conceptContext187: BinaryAssociation = BinaryAssociation(
    name="conceptContext187",
    ends={
        Property(name="ConceptMetaclass189", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding188", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
featureBindings190: BinaryAssociation = BinaryAssociation(
    name="featureBindings190",
    ends={
        Property(name="BaseFeatureBinding", type=gbind_dsl_IntermediateClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_IntermediateClassBinding191", type=BaseFeatureBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references192: BinaryAssociation = BinaryAssociation(
    name="references192",
    ends={
        Property(name="VirtualReference", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass", type=VirtualReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes193: BinaryAssociation = BinaryAssociation(
    name="attributes193",
    ends={
        Property(name="VirtualAttribute", type=gbind_dsl_VirtualMetaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_VirtualMetaclass194", type=VirtualAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context229: BinaryAssociation = BinaryAssociation(
    name="context229",
    ends={
        Property(name="ConcreteMetaclass230", type=gbind_dsl_LocalHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_LocalHelper", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
parameters231: BinaryAssociation = BinaryAssociation(
    name="parameters231",
    ends={
        Property(name="HelperParameter", type=gbind_dsl_LocalHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_LocalHelper232", type=HelperParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concrete215: BinaryAssociation = BinaryAssociation(
    name="concrete215",
    ends={
        Property(name="OclExpression216", type=gbind_dsl_OclFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_OclFeatureBinding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body217: BinaryAssociation = BinaryAssociation(
    name="body217",
    ends={
        Property(name="OclExpression218", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseHelper", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type219: BinaryAssociation = BinaryAssociation(
    name="type219",
    ends={
        Property(name="OclType221", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_BaseHelper220", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model_222: BinaryAssociation = BinaryAssociation(
    name="model_222",
    ends={
        Property(name="BindingModel223", type=gbind_dsl_BaseHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
qualifier224: BinaryAssociation = BinaryAssociation(
    name="qualifier224",
    ends={
        Property(name="ConcreteMetaclass225", type=gbind_dsl_ConceptHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptHelper", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
contextClass226: BinaryAssociation = BinaryAssociation(
    name="contextClass226",
    ends={
        Property(name="ConceptMetaclass228", type=gbind_dsl_ConceptHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="gbind_dsl_ConceptHelper227", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_gbind_simpleocl_Import_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_Import)
gen_gbind_simpleocl_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclExpression)
gen_gbind_simpleocl_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_NamedElement)
gen_gbind_simpleocl_Module_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_Module)
gen_gbind_simpleocl_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_ModuleElement)
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
gen_gbind_simpleocl_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_EnumLiteralExp)
gen_gbind_simpleocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_VariableExp)
gen_gbind_simpleocl_SuperExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_SuperExp)
gen_gbind_simpleocl_SelfExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_SelfExp)
gen_gbind_simpleocl_EnvExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_EnvExp)
gen_gbind_simpleocl_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_PrimitiveExp)
gen_gbind_simpleocl_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_StringExp)
gen_gbind_simpleocl_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_BooleanExp)
gen_gbind_simpleocl_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=gbind_simpleocl_NumericExp)
gen_gbind_simpleocl_RealExp_NumericExp = Generalization(general=NumericExp, specific=gbind_simpleocl_RealExp)
gen_gbind_simpleocl_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_PropertyCallExp)
gen_gbind_simpleocl_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_PropertyCall)
gen_gbind_simpleocl_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_NavigationOrAttributeCall)
gen_gbind_simpleocl_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_OperationCall)
gen_gbind_simpleocl_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OperatorCallExp)
gen_gbind_simpleocl_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_NotOpCallExp)
gen_gbind_simpleocl_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OclUndefinedExp)
gen_gbind_simpleocl_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_StaticPropertyCallExp)
gen_gbind_simpleocl_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_StaticPropertyCall)
gen_gbind_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=gbind_simpleocl_StaticNavigationOrAttributeCall)
gen_gbind_simpleocl_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=gbind_simpleocl_StaticOperationCall)
gen_gbind_simpleocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=gbind_simpleocl_IterateExp)
gen_gbind_simpleocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=gbind_simpleocl_IteratorExp)
gen_gbind_simpleocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_LetExp)
gen_gbind_simpleocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_IfExp)
gen_gbind_simpleocl_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_VariableDeclaration)
gen_gbind_simpleocl_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_RelOpCallExp)
gen_gbind_simpleocl_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_EqOpCallExp)
gen_gbind_simpleocl_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_AddOpCallExp)
gen_gbind_simpleocl_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_IntOpCallExp)
gen_gbind_simpleocl_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=gbind_simpleocl_MulOpCallExp)
gen_gbind_simpleocl_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=gbind_simpleocl_LambdaCallExp)
gen_gbind_simpleocl_BraceExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_BraceExp)
gen_gbind_simpleocl_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=gbind_simpleocl_CollectionOperationCall)
gen_gbind_simpleocl_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=gbind_simpleocl_LoopExp)
gen_gbind_simpleocl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_Parameter)
gen_gbind_simpleocl_CollectionType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_CollectionType)
gen_gbind_simpleocl_OclType_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclType)
gen_gbind_simpleocl_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_LocalVariable)
gen_gbind_simpleocl_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_simpleocl_Iterator)
gen_gbind_simpleocl_IntegerType_NumericType = Generalization(general=NumericType, specific=gbind_simpleocl_IntegerType)
gen_gbind_simpleocl_RealType_NumericType = Generalization(general=NumericType, specific=gbind_simpleocl_RealType)
gen_gbind_simpleocl_BagType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_BagType)
gen_gbind_simpleocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_OrderedSetType)
gen_gbind_simpleocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_SequenceType)
gen_gbind_simpleocl_SetType_CollectionType = Generalization(general=CollectionType, specific=gbind_simpleocl_SetType)
gen_gbind_simpleocl_OclAnyType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_OclAnyType)
gen_gbind_simpleocl_TupleType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_TupleType)
gen_gbind_simpleocl_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_TupleTypeAttribute)
gen_gbind_simpleocl_OclModelElement_OclType = Generalization(general=OclType, specific=gbind_simpleocl_OclModelElement)
gen_gbind_simpleocl_MapType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_MapType)
gen_gbind_simpleocl_LambdaType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_LambdaType)
gen_gbind_simpleocl_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=gbind_simpleocl_OclModelElementExp)
gen_gbind_simpleocl_Primitive_OclType = Generalization(general=OclType, specific=gbind_simpleocl_Primitive)
gen_gbind_simpleocl_StringType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_StringType)
gen_gbind_simpleocl_BooleanType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_BooleanType)
gen_gbind_simpleocl_NumericType_Primitive = Generalization(general=Primitive, specific=gbind_simpleocl_NumericType)
gen_gbind_simpleocl_OclFeature_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_OclFeature)
gen_gbind_simpleocl_Attribute_OclFeature = Generalization(general=OclFeature, specific=gbind_simpleocl_Attribute)
gen_gbind_simpleocl_Operation_OclFeature = Generalization(general=OclFeature, specific=gbind_simpleocl_Operation)
gen_gbind_simpleocl_OclModel_NamedElement = Generalization(general=NamedElement, specific=gbind_simpleocl_OclModel)
gen_gbind_simpleocl_OclMetamodel_OclModel = Generalization(general=OclModel, specific=gbind_simpleocl_OclMetamodel)
gen_gbind_simpleocl_EnvType_OclType = Generalization(general=OclType, specific=gbind_simpleocl_EnvType)
gen_gbind_simpleocl_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=gbind_simpleocl_OclFeatureDefinition)
gen_gbind_simpleocl_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=gbind_simpleocl_OclContextDefinition)
gen_gbind_dsl_MetamodelDeclaration_OclMetamodel = Generalization(general=OclMetamodel, specific=gbind_dsl_MetamodelDeclaration)
gen_gbind_dsl_ConceptMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_ConceptMetaclass)
gen_gbind_dsl_ConcreteMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_ConcreteMetaclass)
gen_gbind_dsl_ClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_ClassBinding)
gen_gbind_simpleocl_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=gbind_simpleocl_OclInstanceModel)
gen_gbind_dsl_VirtualReference_VirtualFeature = Generalization(general=VirtualFeature, specific=gbind_dsl_VirtualReference)
gen_gbind_dsl_VirtualAttribute_VirtualFeature = Generalization(general=VirtualFeature, specific=gbind_dsl_VirtualAttribute)
gen_gbind_dsl_VirtualClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_VirtualClassBinding)
gen_gbind_dsl_BaseFeatureBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_BaseFeatureBinding)
gen_gbind_dsl_RenamingFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=gbind_dsl_RenamingFeatureBinding)
gen_gbind_dsl_IntermediateClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=gbind_dsl_IntermediateClassBinding)
gen_gbind_dsl_ConcreteReferencDeclaringVar_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_dsl_ConcreteReferencDeclaringVar)
gen_gbind_dsl_VirtualMetaclass_Metaclass = Generalization(general=Metaclass, specific=gbind_dsl_VirtualMetaclass)
gen_gbind_dsl_LocalHelper_BaseHelper = Generalization(general=BaseHelper, specific=gbind_dsl_LocalHelper)
gen_gbind_dsl_HelperParameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=gbind_dsl_HelperParameter)
gen_gbind_dsl_OclFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=gbind_dsl_OclFeatureBinding)
gen_gbind_dsl_ConceptHelper_BaseHelper = Generalization(general=BaseHelper, specific=gbind_dsl_ConceptHelper)

# Domain Model
domain_model = DomainModel(
    name="gbind",
    types={gbind_simpleocl_LocatedElement, gbind_simpleocl_Import, gbind_simpleocl_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCall, LocalVariable, Operation, Attribute, OperatorCallExp, gbind_simpleocl_NamedElement, LocatedElement, gbind_simpleocl_Module, NamedElement, OclMetamodel, Import, ModuleElement, gbind_simpleocl_ModuleElement, Module, gbind_simpleocl_IntegerExp, gbind_simpleocl_CollectionExp, gbind_simpleocl_BagExp, gbind_simpleocl_OrderedSetExp, gbind_simpleocl_SequenceExp, gbind_simpleocl_SetExp, gbind_simpleocl_TupleExp, TuplePart, gbind_simpleocl_TuplePart, TupleExp, gbind_simpleocl_MapExp, MapElement, gbind_simpleocl_MapElement, MapExp, gbind_simpleocl_EnumLiteralExp, gbind_simpleocl_VariableExp, OclExpression, VariableDeclaration, gbind_simpleocl_SuperExp, gbind_simpleocl_SelfExp, gbind_simpleocl_EnvExp, gbind_simpleocl_PrimitiveExp, gbind_simpleocl_StringExp, PrimitiveExp, gbind_simpleocl_BooleanExp, gbind_simpleocl_NumericExp, gbind_simpleocl_RealExp, NumericExp, gbind_simpleocl_PropertyCallExp, PropertyCall, gbind_simpleocl_PropertyCall, gbind_simpleocl_NavigationOrAttributeCall, gbind_simpleocl_OperationCall, gbind_simpleocl_OperatorCallExp, gbind_simpleocl_NotOpCallExp, gbind_simpleocl_OclUndefinedExp, gbind_simpleocl_StaticPropertyCallExp, StaticPropertyCall, gbind_simpleocl_StaticPropertyCall, StaticPropertyCallExp, gbind_simpleocl_StaticNavigationOrAttributeCall, gbind_simpleocl_StaticOperationCall, Iterator, gbind_simpleocl_IterateExp, gbind_simpleocl_IteratorExp, gbind_simpleocl_LetExp, gbind_simpleocl_IfExp, gbind_simpleocl_VariableDeclaration, gbind_simpleocl_RelOpCallExp, gbind_simpleocl_EqOpCallExp, gbind_simpleocl_AddOpCallExp, gbind_simpleocl_IntOpCallExp, gbind_simpleocl_MulOpCallExp, gbind_simpleocl_LambdaCallExp, VariableExp, gbind_simpleocl_BraceExp, gbind_simpleocl_CollectionOperationCall, gbind_simpleocl_LoopExp, gbind_simpleocl_Parameter, gbind_simpleocl_CollectionType, gbind_simpleocl_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, gbind_simpleocl_LocalVariable, IterateExp, gbind_simpleocl_Iterator, gbind_simpleocl_RealType, gbind_simpleocl_BagType, gbind_simpleocl_OrderedSetType, gbind_simpleocl_SequenceType, gbind_simpleocl_SetType, gbind_simpleocl_OclAnyType, gbind_simpleocl_TupleType, gbind_simpleocl_TupleTypeAttribute, TupleType, gbind_simpleocl_OclModelElement, gbind_simpleocl_MapType, gbind_simpleocl_LambdaType, LambdaType, gbind_simpleocl_OclModelElementExp, OclModel, gbind_simpleocl_Primitive, gbind_simpleocl_StringType, Primitive, gbind_simpleocl_BooleanType, gbind_simpleocl_NumericType, gbind_simpleocl_IntegerType, NumericType, gbind_simpleocl_OclFeature, gbind_simpleocl_Attribute, gbind_simpleocl_Operation, Parameter_, gbind_simpleocl_OclModel, OclModelElement, gbind_simpleocl_OclMetamodel, OclInstanceModel, gbind_simpleocl_EnvType, gbind_simpleocl_OclFeatureDefinition, OclFeature, gbind_simpleocl_OclContextDefinition, OclFeatureDefinition, VirtualMetaclass, MetamodelDeclaration, BindingOptions, gbind_dsl_BindingOptions, gbind_dsl_MetamodelDeclaration, gbind_dsl_Metaclass, dsl_gbind_EClass, gbind_dsl_ConceptMetaclass, Metaclass, gbind_dsl_ConcreteMetaclass, gbind_dsl_ConceptBinding, BindingModel, gbind_dsl_ClassBinding, gbind_simpleocl_OclInstanceModel, gbind_dsl_BindingModel, ConceptBinding, BaseHelper, ConceptMetaclass, ConcreteMetaclass, gbind_dsl_VirtualFeature, gbind_dsl_VirtualReference, VirtualFeature, gbind_dsl_VirtualAttribute, gbind_dsl_VirtualClassBinding, ConceptFeatureRef, gbind_dsl_ConceptFeatureRef, gbind_dsl_BaseFeatureBinding, gbind_dsl_RenamingFeatureBinding, gbind_dsl_IntermediateClassBinding, ConcreteReferencDeclaringVar, BaseFeatureBinding, gbind_dsl_ConcreteReferencDeclaringVar, gbind_dsl_VirtualMetaclass, VirtualReference, VirtualAttribute, gbind_dsl_LocalHelper, HelperParameter, gbind_dsl_HelperParameter, gbind_dsl_OclFeatureBinding, gbind_dsl_BaseHelper, gbind_dsl_ConceptHelper},
    associations={module5, type7, ifExp38, appliedProperty9, collection10, letExp12, loopExp13, parentOperation14, initializedVariable15, ifExp216, owningOperation18, ifExp120, owningAttribute22, metamodels0, imports1, elements2, module4, elements27, tuplePart28, tuple29, elements30, map31, key33, value35, appliedOperator24, referredVariable26, calls44, source45, callExp47, arguments49, argument51, source53, source38, staticCall40, staticCallExp41, arguments42, iterators61, result62, variable64, in_66, thenExpression69, condition71, elseExpression73, arguments55, exp57, body59, operation85, elementType87, definitions89, oclExpression90, operation92, mapType294, attribute95, mapType98, collectionTypes100, tupleTypeAttribute101, variableDeclaration103, type75, variableExp77, letExp78, initExpression80, baseExp82, loopExpr83, attributes114, type116, tupleType118, model119, valueType122, keyType124, lambdaReturnType106, lambdaArgType108, staticPropertyCall110, model113, context_136, definition138, initExpression140, type142, parameters144, returnType145, body148, elements150, returnType126, argumentTypes128, feature130, context_131, definition134, virtualMetaclasses161, boundConcept163, boundMetamodel165, options168, eclass170, model_171, concept172, concrete174, whenClause177, model151, metamodel152, bindings155, helpers156, conceptMetaclasses158, concreteMetaclasses159, init195, type_198, type_200, concept201, virtual203, refFeatures206, conceptClass208, conceptClass210, qualifier212, concept180, concreteClass182, concreteReference185, conceptContext187, featureBindings190, references192, attributes193, context229, parameters231, concrete215, body217, type219, model_222, qualifier224, contextClass226},
    generalizations={gen_gbind_simpleocl_Import_NamedElement, gen_gbind_simpleocl_OclExpression_LocatedElement, gen_gbind_simpleocl_NamedElement_LocatedElement, gen_gbind_simpleocl_Module_NamedElement, gen_gbind_simpleocl_ModuleElement_LocatedElement, gen_gbind_simpleocl_IntegerExp_NumericExp, gen_gbind_simpleocl_CollectionExp_OclExpression, gen_gbind_simpleocl_BagExp_CollectionExp, gen_gbind_simpleocl_OrderedSetExp_CollectionExp, gen_gbind_simpleocl_SequenceExp_CollectionExp, gen_gbind_simpleocl_SetExp_CollectionExp, gen_gbind_simpleocl_TupleExp_OclExpression, gen_gbind_simpleocl_TuplePart_LocalVariable, gen_gbind_simpleocl_MapExp_OclExpression, gen_gbind_simpleocl_MapElement_LocatedElement, gen_gbind_simpleocl_EnumLiteralExp_OclExpression, gen_gbind_simpleocl_VariableExp_OclExpression, gen_gbind_simpleocl_SuperExp_OclExpression, gen_gbind_simpleocl_SelfExp_OclExpression, gen_gbind_simpleocl_EnvExp_OclExpression, gen_gbind_simpleocl_PrimitiveExp_OclExpression, gen_gbind_simpleocl_StringExp_PrimitiveExp, gen_gbind_simpleocl_BooleanExp_PrimitiveExp, gen_gbind_simpleocl_NumericExp_PrimitiveExp, gen_gbind_simpleocl_RealExp_NumericExp, gen_gbind_simpleocl_PropertyCallExp_OclExpression, gen_gbind_simpleocl_PropertyCall_LocatedElement, gen_gbind_simpleocl_NavigationOrAttributeCall_PropertyCall, gen_gbind_simpleocl_OperationCall_PropertyCall, gen_gbind_simpleocl_OperatorCallExp_OclExpression, gen_gbind_simpleocl_NotOpCallExp_OperatorCallExp, gen_gbind_simpleocl_OclUndefinedExp_OclExpression, gen_gbind_simpleocl_StaticPropertyCallExp_OclExpression, gen_gbind_simpleocl_StaticPropertyCall_LocatedElement, gen_gbind_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_gbind_simpleocl_StaticOperationCall_StaticPropertyCall, gen_gbind_simpleocl_IterateExp_LoopExp, gen_gbind_simpleocl_IteratorExp_LoopExp, gen_gbind_simpleocl_LetExp_OclExpression, gen_gbind_simpleocl_IfExp_OclExpression, gen_gbind_simpleocl_VariableDeclaration_LocatedElement, gen_gbind_simpleocl_RelOpCallExp_OperatorCallExp, gen_gbind_simpleocl_EqOpCallExp_OperatorCallExp, gen_gbind_simpleocl_AddOpCallExp_OperatorCallExp, gen_gbind_simpleocl_IntOpCallExp_OperatorCallExp, gen_gbind_simpleocl_MulOpCallExp_OperatorCallExp, gen_gbind_simpleocl_LambdaCallExp_VariableExp, gen_gbind_simpleocl_BraceExp_OclExpression, gen_gbind_simpleocl_CollectionOperationCall_OperationCall, gen_gbind_simpleocl_LoopExp_PropertyCall, gen_gbind_simpleocl_Parameter_VariableDeclaration, gen_gbind_simpleocl_CollectionType_OclType, gen_gbind_simpleocl_OclType_LocatedElement, gen_gbind_simpleocl_LocalVariable_VariableDeclaration, gen_gbind_simpleocl_Iterator_VariableDeclaration, gen_gbind_simpleocl_IntegerType_NumericType, gen_gbind_simpleocl_RealType_NumericType, gen_gbind_simpleocl_BagType_CollectionType, gen_gbind_simpleocl_OrderedSetType_CollectionType, gen_gbind_simpleocl_SequenceType_CollectionType, gen_gbind_simpleocl_SetType_CollectionType, gen_gbind_simpleocl_OclAnyType_OclType, gen_gbind_simpleocl_TupleType_OclType, gen_gbind_simpleocl_TupleTypeAttribute_LocatedElement, gen_gbind_simpleocl_OclModelElement_OclType, gen_gbind_simpleocl_MapType_OclType, gen_gbind_simpleocl_LambdaType_OclType, gen_gbind_simpleocl_OclModelElementExp_OclExpression, gen_gbind_simpleocl_Primitive_OclType, gen_gbind_simpleocl_StringType_Primitive, gen_gbind_simpleocl_BooleanType_Primitive, gen_gbind_simpleocl_NumericType_Primitive, gen_gbind_simpleocl_OclFeature_NamedElement, gen_gbind_simpleocl_Attribute_OclFeature, gen_gbind_simpleocl_Operation_OclFeature, gen_gbind_simpleocl_OclModel_NamedElement, gen_gbind_simpleocl_OclMetamodel_OclModel, gen_gbind_simpleocl_EnvType_OclType, gen_gbind_simpleocl_OclFeatureDefinition_ModuleElement, gen_gbind_simpleocl_OclContextDefinition_LocatedElement, gen_gbind_dsl_MetamodelDeclaration_OclMetamodel, gen_gbind_dsl_ConceptMetaclass_Metaclass, gen_gbind_dsl_ConcreteMetaclass_Metaclass, gen_gbind_dsl_ClassBinding_ConceptBinding, gen_gbind_simpleocl_OclInstanceModel_OclModel, gen_gbind_dsl_VirtualReference_VirtualFeature, gen_gbind_dsl_VirtualAttribute_VirtualFeature, gen_gbind_dsl_VirtualClassBinding_ConceptBinding, gen_gbind_dsl_BaseFeatureBinding_ConceptBinding, gen_gbind_dsl_RenamingFeatureBinding_BaseFeatureBinding, gen_gbind_dsl_IntermediateClassBinding_ConceptBinding, gen_gbind_dsl_ConcreteReferencDeclaringVar_VariableDeclaration, gen_gbind_dsl_VirtualMetaclass_Metaclass, gen_gbind_dsl_LocalHelper_BaseHelper, gen_gbind_dsl_HelperParameter_VariableDeclaration, gen_gbind_dsl_OclFeatureBinding_BaseFeatureBinding, gen_gbind_dsl_ConceptHelper_BaseHelper},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)