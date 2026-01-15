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

# Enumerations
RuleResolutionStatus: Enumeration = Enumeration(
    name="RuleResolutionStatus",
    literals={
            EnumerationLiteral(name="RESOLUTION_UNKNOWN"),
			EnumerationLiteral(name="RESOLUTION_CONFIRMED"),
			EnumerationLiteral(name="RESOLUTION_DISCARDED")
    }
)

# Classes
atlext_ATL_LocatedElement = Class(name="atlext::ATL::LocatedElement", is_abstract=True)
ATL_atlext_EObject = Class(name="ATL::atlext::EObject")
ModuleElement = Class(name="ModuleElement")
atlext_ATL_ModuleElement = Class(name="atlext::ATL::ModuleElement", is_abstract=True)
atlext_ATL_Helper = Class(name="atlext::ATL::Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL::ModuleElement")
ATL_Callable = Class(name="ATL::Callable")
Query = Class(name="Query")
StringToStringMap = Class(name="StringToStringMap")
atlext_ATL_Unit = Class(name="atlext::ATL::Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlext_ATL_Library = Class(name="atlext::ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
atlext_ATL_Query = Class(name="atlext::ATL::Query")
OclExpression = Class(name="OclExpression")
atlext_ATL_Module = Class(name="atlext::ATL::Module")
OclModel = Class(name="OclModel")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlext_ATL_StaticRule = Class(name="atlext::ATL::StaticRule", is_abstract=True)
ATL_Rule = Class(name="ATL::Rule")
atlext_ATL_ModuleCallable = Class(name="atlext::ATL::ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
atlext_ATL_Callable = Class(name="atlext::ATL::Callable", is_abstract=True)
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
ATL_atlext_Type = Class(name="ATL::atlext::Type")
atlext_ATL_StaticHelper = Class(name="atlext::ATL::StaticHelper")
ATL_Helper = Class(name="ATL::Helper")
ATL_ModuleCallable = Class(name="ATL::ModuleCallable")
atlext_ATL_ContextHelper = Class(name="atlext::ATL::ContextHelper")
PropertyCallExp = Class(name="PropertyCallExp")
atlext_ATL_Rule = Class(name="atlext::ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
InPatternElement = Class(name="InPatternElement")
atlext_ATL_OutPattern = Class(name="atlext::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
CallableParameter = Class(name="CallableParameter")
atlext_ATL_RuleWithPattern = Class(name="atlext::ATL::RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
RuleWithPattern = Class(name="RuleWithPattern")
atlext_ATL_MatchedRule = Class(name="atlext::ATL::MatchedRule")
atlext_ATL_LazyRule = Class(name="atlext::ATL::LazyRule")
ATL_RuleWithPattern = Class(name="ATL::RuleWithPattern")
ATL_StaticRule = Class(name="ATL::StaticRule")
atlext_ATL_CalledRule = Class(name="atlext::ATL::CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
atlext_ATL_InPattern = Class(name="atlext::ATL::InPattern")
Binding = Class(name="Binding")
atlext_ATL_SimpleOutPatternElement = Class(name="atlext::ATL::SimpleOutPatternElement")
atlext_ATL_ForEachOutPatternElement = Class(name="atlext::ATL::ForEachOutPatternElement")
atlext_ATL_DropPattern = Class(name="atlext::ATL::DropPattern")
atlext_ATL_PatternElement = Class(name="atlext::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlext_ATL_InPatternElement = Class(name="atlext::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atlext_ATL_SimpleInPatternElement = Class(name="atlext::ATL::SimpleInPatternElement")
atlext_ATL_OutPatternElement = Class(name="atlext::ATL::OutPatternElement", is_abstract=True)
atlext_ATL_ActionBlock = Class(name="atlext::ATL::ActionBlock")
Statement = Class(name="Statement")
atlext_ATL_Statement = Class(name="atlext::ATL::Statement", is_abstract=True)
atlext_ATL_ExpressionStat = Class(name="atlext::ATL::ExpressionStat")
Iterator = Class(name="Iterator")
atlext_ATL_Binding = Class(name="atlext::ATL::Binding")
RuleResolutionInfo = Class(name="RuleResolutionInfo")
atlext_ATL_RuleVariableDeclaration = Class(name="atlext::ATL::RuleVariableDeclaration")
atlext_ATL_LibraryRef = Class(name="atlext::ATL::LibraryRef")
atlext_ATL_StringToStringMap = Class(name="atlext::ATL::StringToStringMap")
atlext_ATL_CallableParameter = Class(name="atlext::ATL::CallableParameter")
atlext_ATL_RuleResolutionInfo = Class(name="atlext::ATL::RuleResolutionInfo")
MatchedRule = Class(name="MatchedRule")
atlext_ATL_BindingStat = Class(name="atlext::ATL::BindingStat")
atlext_ATL_IfStat = Class(name="atlext::ATL::IfStat")
atlext_ATL_ForStat = Class(name="atlext::ATL::ForStat")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
atlext_OCL_OclExpression = Class(name="atlext::OCL::OclExpression", is_abstract=True)
ATL_LocatedElement = Class(name="ATL::LocatedElement")
OCL_TypedElement = Class(name="OCL::TypedElement")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
atlext_OCL_IntegerExp = Class(name="atlext::OCL::IntegerExp")
atlext_OCL_CollectionExp = Class(name="atlext::OCL::CollectionExp", is_abstract=True)
atlext_OCL_BagExp = Class(name="atlext::OCL::BagExp")
atlext_OCL_OrderedSetExp = Class(name="atlext::OCL::OrderedSetExp")
atlext_OCL_SequenceExp = Class(name="atlext::OCL::SequenceExp")
atlext_OCL_SetExp = Class(name="atlext::OCL::SetExp")
atlext_OCL_TupleExp = Class(name="atlext::OCL::TupleExp")
Attribute = Class(name="Attribute")
TuplePart = Class(name="TuplePart")
atlext_OCL_TuplePart = Class(name="atlext::OCL::TuplePart")
OCL_atlext_Type = Class(name="OCL::atlext::Type")
TupleExp = Class(name="TupleExp")
atlext_OCL_VariableExp = Class(name="atlext::OCL::VariableExp")
atlext_OCL_MapExp = Class(name="atlext::OCL::MapExp")
MapElement = Class(name="MapElement")
atlext_OCL_SuperExp = Class(name="atlext::OCL::SuperExp")
atlext_OCL_PrimitiveExp = Class(name="atlext::OCL::PrimitiveExp", is_abstract=True)
atlext_OCL_MapElement = Class(name="atlext::OCL::MapElement")
atlext_OCL_StringExp = Class(name="atlext::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
MapExp = Class(name="MapExp")
atlext_OCL_BooleanExp = Class(name="atlext::OCL::BooleanExp")
atlext_OCL_NumericExp = Class(name="atlext::OCL::NumericExp", is_abstract=True)
atlext_OCL_RealExp = Class(name="atlext::OCL::RealExp")
NumericExp = Class(name="NumericExp")
atlext_OCL_EnumLiteralExp = Class(name="atlext::OCL::EnumLiteralExp")
atlext_OCL_OclUndefinedExp = Class(name="atlext::OCL::OclUndefinedExp")
atlext_OCL_PropertyCallExp = Class(name="atlext::OCL::PropertyCallExp", is_abstract=True)
OCL_atlext_EObject = Class(name="OCL::atlext::EObject")
ContextHelper = Class(name="ContextHelper")
atlext_OCL_NavigationOrAttributeCallExp = Class(name="atlext::OCL::NavigationOrAttributeCallExp")
atlext_OCL_OperationCallExp = Class(name="atlext::OCL::OperationCallExp")
ResolveTempResolution = Class(name="ResolveTempResolution")
atlext_OCL_CollectionOperationCallExp = Class(name="atlext::OCL::CollectionOperationCallExp")
atlext_OCL_LoopExp = Class(name="atlext::OCL::LoopExp", is_abstract=True)
atlext_OCL_IterateExp = Class(name="atlext::OCL::IterateExp")
atlext_OCL_IteratorExp = Class(name="atlext::OCL::IteratorExp")
atlext_OCL_LetExp = Class(name="atlext::OCL::LetExp")
atlext_OCL_OperatorCallExp = Class(name="atlext::OCL::OperatorCallExp")
atlext_OCL_IfExp = Class(name="atlext::OCL::IfExp")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlext_OCL_Iterator = Class(name="atlext::OCL::Iterator")
atlext_OCL_Parameter = Class(name="atlext::OCL::Parameter")
atlext_OCL_CollectionType = Class(name="atlext::OCL::CollectionType")
atlext_OCL_VariableDeclaration = Class(name="atlext::OCL::VariableDeclaration")
atlext_OCL_OclType = Class(name="atlext::OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atlext_OCL_Primitive = Class(name="atlext::OCL::Primitive", is_abstract=True)
atlext_OCL_StringType = Class(name="atlext::OCL::StringType")
Primitive = Class(name="Primitive")
atlext_OCL_NumericType = Class(name="atlext::OCL::NumericType", is_abstract=True)
atlext_OCL_IntegerType = Class(name="atlext::OCL::IntegerType")
NumericType = Class(name="NumericType")
atlext_OCL_RealType = Class(name="atlext::OCL::RealType")
atlext_OCL_BagType = Class(name="atlext::OCL::BagType")
atlext_OCL_OrderedSetType = Class(name="atlext::OCL::OrderedSetType")
atlext_OCL_SequenceType = Class(name="atlext::OCL::SequenceType")
atlext_OCL_SetType = Class(name="atlext::OCL::SetType")
atlext_OCL_OclAnyType = Class(name="atlext::OCL::OclAnyType")
atlext_OCL_TupleType = Class(name="atlext::OCL::TupleType")
atlext_OCL_TupleTypeAttribute = Class(name="atlext::OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
atlext_OCL_OclModelElement = Class(name="atlext::OCL::OclModelElement")
atlext_OCL_MapType = Class(name="atlext::OCL::MapType")
atlext_OCL_BooleanType = Class(name="atlext::OCL::BooleanType")
OclFeature = Class(name="OclFeature")
atlext_OCL_OclContextDefinition = Class(name="atlext::OCL::OclContextDefinition")
atlext_OCL_OclFeature = Class(name="atlext::OCL::OclFeature", is_abstract=True)
atlext_OCL_Attribute = Class(name="atlext::OCL::Attribute")
atlext_OCL_Operation = Class(name="atlext::OCL::Operation")
atlext_OCL_OclFeatureDefinition = Class(name="atlext::OCL::OclFeatureDefinition")
atlext_OCL_OclModel = Class(name="atlext::OCL::OclModel")
OclModelElement = Class(name="OclModelElement")
atlext_OCL_TypedElement = Class(name="atlext::OCL::TypedElement", is_abstract=True)
atlext_OCL_ResolveTempResolution = Class(name="atlext::OCL::ResolveTempResolution")
atlext_OCL_JavaBody = Class(name="atlext::OCL::JavaBody")
atlext_OCL_GetAppliedStereotypesBody = Class(name="atlext::OCL::GetAppliedStereotypesBody")
JavaBody = Class(name="JavaBody")
atlext_OCL2_SelectByKind = Class(name="atlext::OCL2::SelectByKind")
CollectionOperationCallExp = Class(name="CollectionOperationCallExp")

# atlext_ATL_LocatedElement class attributes and methods
atlext_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlext_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlext_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlext_ATL_LocatedElement_fileLocation: Property = Property(name="fileLocation", type=StringType)
atlext_ATL_LocatedElement_fileObject: Property = Property(name="fileObject", type=StringType)
atlext_ATL_LocatedElement.attributes={atlext_ATL_LocatedElement_fileObject, atlext_ATL_LocatedElement_fileLocation, atlext_ATL_LocatedElement_commentsAfter, atlext_ATL_LocatedElement_location, atlext_ATL_LocatedElement_commentsBefore}

# ATL_atlext_EObject class attributes and methods

# ModuleElement class attributes and methods

# atlext_ATL_ModuleElement class attributes and methods

# atlext_ATL_Helper class attributes and methods
atlext_ATL_Helper_hasContext: Property = Property(name="hasContext", type=BooleanType)
atlext_ATL_Helper_isAttribute: Property = Property(name="isAttribute", type=BooleanType)
atlext_ATL_Helper.attributes={atlext_ATL_Helper_hasContext, atlext_ATL_Helper_isAttribute}

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

# StringToStringMap class attributes and methods

# atlext_ATL_Unit class attributes and methods
atlext_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlext_ATL_Unit.attributes={atlext_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# atlext_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# atlext_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# atlext_ATL_Module class attributes and methods
atlext_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_Module.attributes={atlext_ATL_Module_isRefining}

# OclModel class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlext_ATL_StaticRule class attributes and methods

# ATL_Rule class attributes and methods

# atlext_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# atlext_ATL_Callable class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# ATL_atlext_Type class attributes and methods

# atlext_ATL_StaticHelper class attributes and methods

# ATL_Helper class attributes and methods

# ATL_ModuleCallable class attributes and methods

# atlext_ATL_ContextHelper class attributes and methods

# PropertyCallExp class attributes and methods

# atlext_ATL_Rule class attributes and methods
atlext_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlext_ATL_Rule.attributes={atlext_ATL_Rule_name}

# OutPattern class attributes and methods

# InPatternElement class attributes and methods

# atlext_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# CallableParameter class attributes and methods

# atlext_ATL_RuleWithPattern class attributes and methods
atlext_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlext_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlext_ATL_RuleWithPattern.attributes={atlext_ATL_RuleWithPattern_isAbstract, atlext_ATL_RuleWithPattern_isRefining, atlext_ATL_RuleWithPattern_isNoDefault}

# Rule class attributes and methods

# InPattern class attributes and methods

# RuleWithPattern class attributes and methods

# atlext_ATL_MatchedRule class attributes and methods

# atlext_ATL_LazyRule class attributes and methods
atlext_ATL_LazyRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlext_ATL_LazyRule.attributes={atlext_ATL_LazyRule_isUnique}

# ATL_RuleWithPattern class attributes and methods

# ATL_StaticRule class attributes and methods

# atlext_ATL_CalledRule class attributes and methods
atlext_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlext_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlext_ATL_CalledRule.attributes={atlext_ATL_CalledRule_isEntrypoint, atlext_ATL_CalledRule_isEndpoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# atlext_ATL_InPattern class attributes and methods

# Binding class attributes and methods

# atlext_ATL_SimpleOutPatternElement class attributes and methods

# atlext_ATL_ForEachOutPatternElement class attributes and methods

# atlext_ATL_DropPattern class attributes and methods

# atlext_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlext_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atlext_ATL_SimpleInPatternElement class attributes and methods

# atlext_ATL_OutPatternElement class attributes and methods

# atlext_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atlext_ATL_Statement class attributes and methods

# atlext_ATL_ExpressionStat class attributes and methods

# Iterator class attributes and methods

# atlext_ATL_Binding class attributes and methods
atlext_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_Binding.attributes={atlext_ATL_Binding_propertyName, atlext_ATL_Binding_isAssignment}

# RuleResolutionInfo class attributes and methods

# atlext_ATL_RuleVariableDeclaration class attributes and methods

# atlext_ATL_LibraryRef class attributes and methods
atlext_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlext_ATL_LibraryRef.attributes={atlext_ATL_LibraryRef_name}

# atlext_ATL_StringToStringMap class attributes and methods
atlext_ATL_StringToStringMap_key: Property = Property(name="key", type=StringType)
atlext_ATL_StringToStringMap_value: Property = Property(name="value", type=StringType)
atlext_ATL_StringToStringMap.attributes={atlext_ATL_StringToStringMap_value, atlext_ATL_StringToStringMap_key}

# atlext_ATL_CallableParameter class attributes and methods
atlext_ATL_CallableParameter_name: Property = Property(name="name", type=StringType)
atlext_ATL_CallableParameter.attributes={atlext_ATL_CallableParameter_name}

# atlext_ATL_RuleResolutionInfo class attributes and methods
atlext_ATL_RuleResolutionInfo_status: Property = Property(name="status", type=StringType)
atlext_ATL_RuleResolutionInfo.attributes={atlext_ATL_RuleResolutionInfo_status}

# MatchedRule class attributes and methods

# atlext_ATL_BindingStat class attributes and methods
atlext_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_BindingStat.attributes={atlext_ATL_BindingStat_propertyName, atlext_ATL_BindingStat_isAssignment}

# atlext_ATL_IfStat class attributes and methods

# atlext_ATL_ForStat class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# atlext_OCL_OclExpression class attributes and methods
atlext_OCL_OclExpression_implicitlyCasted: Property = Property(name="implicitlyCasted", type=BooleanType)
atlext_OCL_OclExpression.attributes={atlext_OCL_OclExpression_implicitlyCasted}

# ATL_LocatedElement class attributes and methods

# OCL_TypedElement class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# atlext_OCL_IntegerExp class attributes and methods
atlext_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlext_OCL_IntegerExp.attributes={atlext_OCL_IntegerExp_integerSymbol}

# atlext_OCL_CollectionExp class attributes and methods

# atlext_OCL_BagExp class attributes and methods

# atlext_OCL_OrderedSetExp class attributes and methods

# atlext_OCL_SequenceExp class attributes and methods

# atlext_OCL_SetExp class attributes and methods

# atlext_OCL_TupleExp class attributes and methods

# Attribute class attributes and methods

# TuplePart class attributes and methods

# atlext_OCL_TuplePart class attributes and methods

# OCL_atlext_Type class attributes and methods

# TupleExp class attributes and methods

# atlext_OCL_VariableExp class attributes and methods

# atlext_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlext_OCL_SuperExp class attributes and methods

# atlext_OCL_PrimitiveExp class attributes and methods

# atlext_OCL_MapElement class attributes and methods

# atlext_OCL_StringExp class attributes and methods
atlext_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atlext_OCL_StringExp.attributes={atlext_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# MapExp class attributes and methods

# atlext_OCL_BooleanExp class attributes and methods
atlext_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
atlext_OCL_BooleanExp.attributes={atlext_OCL_BooleanExp_booleanSymbol}

# atlext_OCL_NumericExp class attributes and methods

# atlext_OCL_RealExp class attributes and methods
atlext_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
atlext_OCL_RealExp.attributes={atlext_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atlext_OCL_EnumLiteralExp class attributes and methods
atlext_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_EnumLiteralExp.attributes={atlext_OCL_EnumLiteralExp_name}

# atlext_OCL_OclUndefinedExp class attributes and methods

# atlext_OCL_PropertyCallExp class attributes and methods
atlext_OCL_PropertyCallExp_isStaticCall: Property = Property(name="isStaticCall", type=BooleanType)
atlext_OCL_PropertyCallExp.attributes={atlext_OCL_PropertyCallExp_isStaticCall}

# OCL_atlext_EObject class attributes and methods

# ContextHelper class attributes and methods

# atlext_OCL_NavigationOrAttributeCallExp class attributes and methods
atlext_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_NavigationOrAttributeCallExp.attributes={atlext_OCL_NavigationOrAttributeCallExp_name}

# atlext_OCL_OperationCallExp class attributes and methods
atlext_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlext_OCL_OperationCallExp.attributes={atlext_OCL_OperationCallExp_operationName}

# ResolveTempResolution class attributes and methods

# atlext_OCL_CollectionOperationCallExp class attributes and methods

# atlext_OCL_LoopExp class attributes and methods

# atlext_OCL_IterateExp class attributes and methods

# atlext_OCL_IteratorExp class attributes and methods
atlext_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_IteratorExp.attributes={atlext_OCL_IteratorExp_name}

# atlext_OCL_LetExp class attributes and methods

# atlext_OCL_OperatorCallExp class attributes and methods

# atlext_OCL_IfExp class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlext_OCL_Iterator class attributes and methods

# atlext_OCL_Parameter class attributes and methods

# atlext_OCL_CollectionType class attributes and methods

# atlext_OCL_VariableDeclaration class attributes and methods
atlext_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlext_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlext_OCL_VariableDeclaration.attributes={atlext_OCL_VariableDeclaration_varName, atlext_OCL_VariableDeclaration_id}

# atlext_OCL_OclType class attributes and methods
atlext_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclType.attributes={atlext_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# atlext_OCL_Primitive class attributes and methods

# atlext_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlext_OCL_NumericType class attributes and methods

# atlext_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# atlext_OCL_RealType class attributes and methods

# atlext_OCL_BagType class attributes and methods

# atlext_OCL_OrderedSetType class attributes and methods

# atlext_OCL_SequenceType class attributes and methods

# atlext_OCL_SetType class attributes and methods

# atlext_OCL_OclAnyType class attributes and methods

# atlext_OCL_TupleType class attributes and methods

# atlext_OCL_TupleTypeAttribute class attributes and methods
atlext_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_TupleTypeAttribute.attributes={atlext_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# atlext_OCL_OclModelElement class attributes and methods

# atlext_OCL_MapType class attributes and methods

# atlext_OCL_BooleanType class attributes and methods

# OclFeature class attributes and methods

# atlext_OCL_OclContextDefinition class attributes and methods

# atlext_OCL_OclFeature class attributes and methods

# atlext_OCL_Attribute class attributes and methods
atlext_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_Attribute.attributes={atlext_OCL_Attribute_name}

# atlext_OCL_Operation class attributes and methods
atlext_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlext_OCL_Operation.attributes={atlext_OCL_Operation_name}

# atlext_OCL_OclFeatureDefinition class attributes and methods

# atlext_OCL_OclModel class attributes and methods
atlext_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclModel.attributes={atlext_OCL_OclModel_name}

# OclModelElement class attributes and methods

# atlext_OCL_TypedElement class attributes and methods

# atlext_OCL_ResolveTempResolution class attributes and methods

# atlext_OCL_JavaBody class attributes and methods

# atlext_OCL_GetAppliedStereotypesBody class attributes and methods

# JavaBody class attributes and methods

# atlext_OCL2_SelectByKind class attributes and methods
atlext_OCL2_SelectByKind_isExact: Property = Property(name="isExact", type=BooleanType)
atlext_OCL2_SelectByKind.attributes={atlext_OCL2_SelectByKind_isExact}

# CollectionOperationCallExp class attributes and methods

# Relationships
inModels10: BinaryAssociation = BinaryAssociation(
    name="inModels10",
    ends={
        Property(name="atlext_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="OclModel", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1))
    }
)
outModels11: BinaryAssociation = BinaryAssociation(
    name="outModels11",
    ends={
        Property(name="OclModel13", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module12", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="ModuleElement", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module15", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query16: BinaryAssociation = BinaryAssociation(
    name="query16",
    ends={
        Property(name="ATL17", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Query", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
problems0: BinaryAssociation = BinaryAssociation(
    name="problems0",
    ends={
        Property(name="ATL_atlext_EObject", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement", type=ATL_atlext_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="StringToStringMap", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement2", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries3: BinaryAssociation = BinaryAssociation(
    name="libraries3",
    ends={
        Property(name="ATL", type=atlext_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="LibraryRef", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="ATL5", type=atlext_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="OclExpression", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers7: BinaryAssociation = BinaryAssociation(
    name="helpers7",
    ends={
        Property(name="ATL9", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper8", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionBlock31: BinaryAssociation = BinaryAssociation(
    name="actionBlock31",
    ends={
        Property(name="ATL32", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionBlock", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables33: BinaryAssociation = BinaryAssociation(
    name="variables33",
    ends={
        Property(name="ATL34", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleVariableDeclaration", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledBy35: BinaryAssociation = BinaryAssociation(
    name="calledBy35",
    ends={
        Property(name="PropertyCallExp36", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
library18: BinaryAssociation = BinaryAssociation(
    name="library18",
    ends={
        Property(name="ATL19", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Library", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition20: BinaryAssociation = BinaryAssociation(
    name="definition20",
    ends={
        Property(name="OclFeatureDefinition", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inferredReturnType21: BinaryAssociation = BinaryAssociation(
    name="inferredReturnType21",
    ends={
        Property(name="ATL_atlext_Type", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper22", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
staticReturnType23: BinaryAssociation = BinaryAssociation(
    name="staticReturnType23",
    ends={
        Property(name="ATL_atlext_Type25", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper24", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
contextType26: BinaryAssociation = BinaryAssociation(
    name="contextType26",
    ends={
        Property(name="ATL_atlext_Type27", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ContextHelper", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
polymorphicCalledBy28: BinaryAssociation = BinaryAssociation(
    name="polymorphicCalledBy28",
    ends={
        Property(name="OCL", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern29: BinaryAssociation = BinaryAssociation(
    name="outPattern29",
    ends={
        Property(name="ATL30", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="ATL47", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter48: BinaryAssociation = BinaryAssociation(
    name="filter48",
    ends={
        Property(name="OclExpression49", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule50: BinaryAssociation = BinaryAssociation(
    name="rule50",
    ends={
        Property(name="ATL51", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern52: BinaryAssociation = BinaryAssociation(
    name="dropPattern52",
    ends={
        Property(name="ATL53", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="DropPattern", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callableParameters37: BinaryAssociation = BinaryAssociation(
    name="callableParameters37",
    ends={
        Property(name="CallableParameter", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable38", type=CallableParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern39: BinaryAssociation = BinaryAssociation(
    name="inPattern39",
    ends={
        Property(name="InPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children40: BinaryAssociation = BinaryAssociation(
    name="children40",
    ends={
        Property(name="ATL41", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleWithPattern", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
superRule42: BinaryAssociation = BinaryAssociation(
    name="superRule42",
    ends={
        Property(name="ATL44", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleWithPattern43", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="Parameter", type=atlext_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceElement70: BinaryAssociation = BinaryAssociation(
    name="sourceElement70",
    ends={
        Property(name="ATL72", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement71", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings73: BinaryAssociation = BinaryAssociation(
    name="bindings73",
    ends={
        Property(name="ATL74", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model75: BinaryAssociation = BinaryAssociation(
    name="model75",
    ends={
        Property(name="OclModel76", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings77: BinaryAssociation = BinaryAssociation(
    name="reverseBindings77",
    ends={
        Property(name="OclExpression78", type=atlext_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection79: BinaryAssociation = BinaryAssociation(
    name="collection79",
    ends={
        Property(name="OclExpression80", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements54: BinaryAssociation = BinaryAssociation(
    name="elements54",
    ends={
        Property(name="ATL55", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern56: BinaryAssociation = BinaryAssociation(
    name="outPattern56",
    ends={
        Property(name="ATL58", type=atlext_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern57", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo59: BinaryAssociation = BinaryAssociation(
    name="mapsTo59",
    ends={
        Property(name="ATL61", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement60", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern62: BinaryAssociation = BinaryAssociation(
    name="inPattern62",
    ends={
        Property(name="ATL64", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern63", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models65: BinaryAssociation = BinaryAssociation(
    name="models65",
    ends={
        Property(name="OclModel66", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern67: BinaryAssociation = BinaryAssociation(
    name="outPattern67",
    ends={
        Property(name="ATL69", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern68", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
rule101: BinaryAssociation = BinaryAssociation(
    name="rule101",
    ends={
        Property(name="ATL103", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule102", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements104: BinaryAssociation = BinaryAssociation(
    name="statements104",
    ends={
        Property(name="Statement", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression105: BinaryAssociation = BinaryAssociation(
    name="expression105",
    ends={
        Property(name="OclExpression106", type=atlext_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator81: BinaryAssociation = BinaryAssociation(
    name="iterator81",
    ends={
        Property(name="Iterator", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement82", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value83: BinaryAssociation = BinaryAssociation(
    name="value83",
    ends={
        Property(name="OclExpression84", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement85: BinaryAssociation = BinaryAssociation(
    name="outPatternElement85",
    ends={
        Property(name="ATL87", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement86", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
writtenFeature88: BinaryAssociation = BinaryAssociation(
    name="writtenFeature88",
    ends={
        Property(name="ATL_atlext_EObject90", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding89", type=ATL_atlext_EObject, multiplicity=Multiplicity(1, 1))
    }
)
leftType91: BinaryAssociation = BinaryAssociation(
    name="leftType91",
    ends={
        Property(name="ATL_atlext_Type93", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding92", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
resolvedBy94: BinaryAssociation = BinaryAssociation(
    name="resolvedBy94",
    ends={
        Property(name="RuleResolutionInfo", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding95", type=RuleResolutionInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule96: BinaryAssociation = BinaryAssociation(
    name="rule96",
    ends={
        Property(name="ATL98", type=atlext_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule97", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit99: BinaryAssociation = BinaryAssociation(
    name="unit99",
    ends={
        Property(name="ATL100", type=atlext_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Unit", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
statements125: BinaryAssociation = BinaryAssociation(
    name="statements125",
    ends={
        Property(name="Statement127", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat126", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticType128: BinaryAssociation = BinaryAssociation(
    name="staticType128",
    ends={
        Property(name="ATL_atlext_Type129", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
paramDeclaration130: BinaryAssociation = BinaryAssociation(
    name="paramDeclaration130",
    ends={
        Property(name="VariableDeclaration", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter131", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
source107: BinaryAssociation = BinaryAssociation(
    name="source107",
    ends={
        Property(name="OclExpression108", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value109: BinaryAssociation = BinaryAssociation(
    name="value109",
    ends={
        Property(name="OclExpression111", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat110", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition112: BinaryAssociation = BinaryAssociation(
    name="condition112",
    ends={
        Property(name="OclExpression113", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements114: BinaryAssociation = BinaryAssociation(
    name="thenStatements114",
    ends={
        Property(name="Statement116", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat115", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements117: BinaryAssociation = BinaryAssociation(
    name="elseStatements117",
    ends={
        Property(name="Statement119", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat118", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator120: BinaryAssociation = BinaryAssociation(
    name="iterator120",
    ends={
        Property(name="Iterator121", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection122: BinaryAssociation = BinaryAssociation(
    name="collection122",
    ends={
        Property(name="OclExpression124", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat123", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopExp147: BinaryAssociation = BinaryAssociation(
    name="loopExp147",
    ends={
        Property(name="OCL148", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation149: BinaryAssociation = BinaryAssociation(
    name="parentOperation149",
    ends={
        Property(name="OCL150", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCallExp", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable151: BinaryAssociation = BinaryAssociation(
    name="initializedVariable151",
    ends={
        Property(name="OCL153", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration152", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2154: BinaryAssociation = BinaryAssociation(
    name="ifExp2154",
    ends={
        Property(name="OCL156", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp155", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation157: BinaryAssociation = BinaryAssociation(
    name="owningOperation157",
    ends={
        Property(name="OCL158", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
rule132: BinaryAssociation = BinaryAssociation(
    name="rule132",
    ends={
        Property(name="MatchedRule", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
allInvolvedRules133: BinaryAssociation = BinaryAssociation(
    name="allInvolvedRules133",
    ends={
        Property(name="MatchedRule135", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo134", type=MatchedRule, multiplicity=Multiplicity(1, 9999))
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="OCL137", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3138: BinaryAssociation = BinaryAssociation(
    name="ifExp3138",
    ends={
        Property(name="OCL139", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty140: BinaryAssociation = BinaryAssociation(
    name="appliedProperty140",
    ends={
        Property(name="OCL142", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp141", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection143: BinaryAssociation = BinaryAssociation(
    name="collection143",
    ends={
        Property(name="OCL144", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp145: BinaryAssociation = BinaryAssociation(
    name="letExp145",
    ends={
        Property(name="OCL146", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
elements168: BinaryAssociation = BinaryAssociation(
    name="elements168",
    ends={
        Property(name="OCL170", type=atlext_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression169", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExp1159: BinaryAssociation = BinaryAssociation(
    name="ifExp1159",
    ends={
        Property(name="OCL161", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp160", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute162: BinaryAssociation = BinaryAssociation(
    name="owningAttribute162",
    ends={
        Property(name="OCL163", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
tuplePart171: BinaryAssociation = BinaryAssociation(
    name="tuplePart171",
    ends={
        Property(name="OCL172", type=atlext_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
noCastedType164: BinaryAssociation = BinaryAssociation(
    name="noCastedType164",
    ends={
        Property(name="OCL_atlext_Type", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OclExpression", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
tuple173: BinaryAssociation = BinaryAssociation(
    name="tuple173",
    ends={
        Property(name="OCL174", type=atlext_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
referredVariable165: BinaryAssociation = BinaryAssociation(
    name="referredVariable165",
    ends={
        Property(name="OCL167", type=atlext_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration166", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements175: BinaryAssociation = BinaryAssociation(
    name="elements175",
    ends={
        Property(name="OCL176", type=atlext_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map177: BinaryAssociation = BinaryAssociation(
    name="map177",
    ends={
        Property(name="OCL178", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
source184: BinaryAssociation = BinaryAssociation(
    name="source184",
    ends={
        Property(name="OCL186", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression185", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usedFeature187: BinaryAssociation = BinaryAssociation(
    name="usedFeature187",
    ends={
        Property(name="OCL_atlext_EObject", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subtypeFeatures188: BinaryAssociation = BinaryAssociation(
    name="subtypeFeatures188",
    ends={
        Property(name="OCL_atlext_EObject190", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp189", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
key179: BinaryAssociation = BinaryAssociation(
    name="key179",
    ends={
        Property(name="OclExpression180", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receptorType191: BinaryAssociation = BinaryAssociation(
    name="receptorType191",
    ends={
        Property(name="OCL_atlext_EObject193", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp192", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value181: BinaryAssociation = BinaryAssociation(
    name="value181",
    ends={
        Property(name="OclExpression183", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement182", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticResolver194: BinaryAssociation = BinaryAssociation(
    name="staticResolver194",
    ends={
        Property(name="Callable", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp195", type=Callable, multiplicity=Multiplicity(1, 1))
    }
)
dynamicResolvers196: BinaryAssociation = BinaryAssociation(
    name="dynamicResolvers196",
    ends={
        Property(name="ATL197", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ContextHelper", type=ContextHelper, multiplicity=Multiplicity(0, 9999))
    }
)
arguments198: BinaryAssociation = BinaryAssociation(
    name="arguments198",
    ends={
        Property(name="OCL200", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression199", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolveTempResolvedBy201: BinaryAssociation = BinaryAssociation(
    name="resolveTempResolvedBy201",
    ends={
        Property(name="ResolveTempResolution", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OperationCallExp", type=ResolveTempResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body202: BinaryAssociation = BinaryAssociation(
    name="body202",
    ends={
        Property(name="OCL204", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression203", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators205: BinaryAssociation = BinaryAssociation(
    name="iterators205",
    ends={
        Property(name="OCL207", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator206", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result208: BinaryAssociation = BinaryAssociation(
    name="result208",
    ends={
        Property(name="OCL210", type=atlext_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration209", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_214: BinaryAssociation = BinaryAssociation(
    name="in_214",
    ends={
        Property(name="OCL216", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression215", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression217: BinaryAssociation = BinaryAssociation(
    name="thenExpression217",
    ends={
        Property(name="OCL219", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression218", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition220: BinaryAssociation = BinaryAssociation(
    name="condition220",
    ends={
        Property(name="OCL222", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression221", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression223: BinaryAssociation = BinaryAssociation(
    name="elseExpression223",
    ends={
        Property(name="OCL225", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression224", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable211: BinaryAssociation = BinaryAssociation(
    name="variable211",
    ends={
        Property(name="OCL213", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration212", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type226: BinaryAssociation = BinaryAssociation(
    name="type226",
    ends={
        Property(name="OCL228", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType227", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression229: BinaryAssociation = BinaryAssociation(
    name="initExpression229",
    ends={
        Property(name="OCL231", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression230", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp232: BinaryAssociation = BinaryAssociation(
    name="letExp232",
    ends={
        Property(name="OCL234", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp233", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp235: BinaryAssociation = BinaryAssociation(
    name="baseExp235",
    ends={
        Property(name="OCL236", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp237: BinaryAssociation = BinaryAssociation(
    name="variableExp237",
    ends={
        Property(name="OCL238", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
staticType239: BinaryAssociation = BinaryAssociation(
    name="staticType239",
    ends={
        Property(name="OCL_atlext_Type240", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_VariableDeclaration", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr241: BinaryAssociation = BinaryAssociation(
    name="loopExpr241",
    ends={
        Property(name="OCL243", type=atlext_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp242", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
definitions247: BinaryAssociation = BinaryAssociation(
    name="definitions247",
    ends={
        Property(name="OCL248", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression249: BinaryAssociation = BinaryAssociation(
    name="oclExpression249",
    ends={
        Property(name="OCL251", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression250", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation252: BinaryAssociation = BinaryAssociation(
    name="operation252",
    ends={
        Property(name="OCL254", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation253", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2255: BinaryAssociation = BinaryAssociation(
    name="mapType2255",
    ends={
        Property(name="OCL256", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute257: BinaryAssociation = BinaryAssociation(
    name="attribute257",
    ends={
        Property(name="OCL259", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute258", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType260: BinaryAssociation = BinaryAssociation(
    name="mapType260",
    ends={
        Property(name="OCL262", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType261", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes263: BinaryAssociation = BinaryAssociation(
    name="collectionTypes263",
    ends={
        Property(name="OCL264", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute265: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute265",
    ends={
        Property(name="OCL266", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration267: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration267",
    ends={
        Property(name="OCL269", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration268", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
elementType244: BinaryAssociation = BinaryAssociation(
    name="elementType244",
    ends={
        Property(name="OCL246", type=atlext_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType245", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes270: BinaryAssociation = BinaryAssociation(
    name="attributes270",
    ends={
        Property(name="OCL272", type=atlext_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute271", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type273: BinaryAssociation = BinaryAssociation(
    name="type273",
    ends={
        Property(name="OCL275", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType274", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType276: BinaryAssociation = BinaryAssociation(
    name="tupleType276",
    ends={
        Property(name="OCL277", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model278: BinaryAssociation = BinaryAssociation(
    name="model278",
    ends={
        Property(name="OCL280", type=atlext_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel279", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType281: BinaryAssociation = BinaryAssociation(
    name="valueType281",
    ends={
        Property(name="OCL283", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType282", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType284: BinaryAssociation = BinaryAssociation(
    name="keyType284",
    ends={
        Property(name="OCL286", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType285", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature287: BinaryAssociation = BinaryAssociation(
    name="feature287",
    ends={
        Property(name="OCL288", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_289: BinaryAssociation = BinaryAssociation(
    name="context_289",
    ends={
        Property(name="OCL291", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition290", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition292: BinaryAssociation = BinaryAssociation(
    name="definition292",
    ends={
        Property(name="OCL294", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition293", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_295: BinaryAssociation = BinaryAssociation(
    name="context_295",
    ends={
        Property(name="OCL297", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType296", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition298: BinaryAssociation = BinaryAssociation(
    name="definition298",
    ends={
        Property(name="OCL300", type=atlext_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition299", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression301: BinaryAssociation = BinaryAssociation(
    name="initExpression301",
    ends={
        Property(name="OCL303", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression302", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type304: BinaryAssociation = BinaryAssociation(
    name="type304",
    ends={
        Property(name="OCL306", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType305", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters307: BinaryAssociation = BinaryAssociation(
    name="parameters307",
    ends={
        Property(name="Parameter308", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType309: BinaryAssociation = BinaryAssociation(
    name="returnType309",
    ends={
        Property(name="OCL311", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType310", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel315: BinaryAssociation = BinaryAssociation(
    name="metamodel315",
    ends={
        Property(name="OCL317", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel316", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements318: BinaryAssociation = BinaryAssociation(
    name="elements318",
    ends={
        Property(name="OCL319", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model320: BinaryAssociation = BinaryAssociation(
    name="model320",
    ends={
        Property(name="OCL322", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel321", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
inferredType323: BinaryAssociation = BinaryAssociation(
    name="inferredType323",
    ends={
        Property(name="OCL_atlext_Type324", type=atlext_OCL_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_TypedElement", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
element325: BinaryAssociation = BinaryAssociation(
    name="element325",
    ends={
        Property(name="OutPatternElement326", type=atlext_OCL_ResolveTempResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_ResolveTempResolution", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
body312: BinaryAssociation = BinaryAssociation(
    name="body312",
    ends={
        Property(name="OCL314", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression313", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_atlext_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ModuleElement)
gen_atlext_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlext_ATL_Helper)
gen_atlext_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlext_ATL_Helper)
gen_atlext_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Unit)
gen_atlext_ATL_Library_Unit = Generalization(general=Unit, specific=atlext_ATL_Library)
gen_atlext_ATL_Query_Unit = Generalization(general=Unit, specific=atlext_ATL_Query)
gen_atlext_ATL_Module_Unit = Generalization(general=Unit, specific=atlext_ATL_Module)
gen_atlext_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlext_ATL_ModuleCallable)
gen_atlext_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlext_ATL_ContextHelper)
gen_atlext_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlext_ATL_Rule)
gen_atlext_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_InPattern)
gen_atlext_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_OutPattern)
gen_atlext_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlext_ATL_RuleWithPattern)
gen_atlext_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlext_ATL_MatchedRule)
gen_atlext_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlext_ATL_CalledRule)
gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_SimpleOutPatternElement)
gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_ForEachOutPatternElement)
gen_atlext_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_DropPattern)
gen_atlext_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_PatternElement)
gen_atlext_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_InPatternElement)
gen_atlext_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlext_ATL_SimpleInPatternElement)
gen_atlext_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_OutPatternElement)
gen_atlext_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ActionBlock)
gen_atlext_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Statement)
gen_atlext_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ExpressionStat)
gen_atlext_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Binding)
gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_RuleVariableDeclaration)
gen_atlext_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_LibraryRef)
gen_atlext_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlext_ATL_BindingStat)
gen_atlext_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlext_ATL_IfStat)
gen_atlext_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ForStat)
gen_atlext_OCL_OclExpression_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_OclExpression_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_IntegerExp)
gen_atlext_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_CollectionExp)
gen_atlext_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_BagExp)
gen_atlext_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_OrderedSetExp)
gen_atlext_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SequenceExp)
gen_atlext_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SetExp)
gen_atlext_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_TupleExp)
gen_atlext_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_TuplePart)
gen_atlext_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_VariableExp)
gen_atlext_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_MapExp)
gen_atlext_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_SuperExp)
gen_atlext_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PrimitiveExp)
gen_atlext_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_MapElement)
gen_atlext_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_StringExp)
gen_atlext_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_BooleanExp)
gen_atlext_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_NumericExp)
gen_atlext_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_RealExp)
gen_atlext_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_EnumLiteralExp)
gen_atlext_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclUndefinedExp)
gen_atlext_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PropertyCallExp)
gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_NavigationOrAttributeCallExp)
gen_atlext_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_OperationCallExp)
gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_CollectionOperationCallExp)
gen_atlext_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_LoopExp)
gen_atlext_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IterateExp)
gen_atlext_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IteratorExp)
gen_atlext_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_LetExp)
gen_atlext_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_OperatorCallExp)
gen_atlext_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_IfExp)
gen_atlext_OCL_VariableDeclaration_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Iterator)
gen_atlext_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Parameter)
gen_atlext_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlext_OCL_CollectionType)
gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclType)
gen_atlext_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlext_OCL_Primitive)
gen_atlext_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_StringType)
gen_atlext_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_NumericType)
gen_atlext_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlext_OCL_IntegerType)
gen_atlext_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlext_OCL_RealType)
gen_atlext_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_BagType)
gen_atlext_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_OrderedSetType)
gen_atlext_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_SequenceType)
gen_atlext_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_SetType)
gen_atlext_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlext_OCL_OclAnyType)
gen_atlext_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlext_OCL_TupleType)
gen_atlext_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_TupleTypeAttribute)
gen_atlext_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlext_OCL_OclModelElement)
gen_atlext_OCL_MapType_OclType = Generalization(general=OclType, specific=atlext_OCL_MapType)
gen_atlext_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_BooleanType)
gen_atlext_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclContextDefinition)
gen_atlext_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeature)
gen_atlext_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Attribute)
gen_atlext_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Operation)
gen_atlext_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeatureDefinition)
gen_atlext_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclModel)
gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo = Generalization(general=RuleResolutionInfo, specific=atlext_OCL_ResolveTempResolution)
gen_atlext_OCL_JavaBody_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_JavaBody)
gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody = Generalization(general=JavaBody, specific=atlext_OCL_GetAppliedStereotypesBody)
gen_atlext_OCL2_SelectByKind_CollectionOperationCallExp = Generalization(general=CollectionOperationCallExp, specific=atlext_OCL2_SelectByKind)

# Domain Model
domain_model = DomainModel(
    name="atlext",
    types={atlext_ATL_LocatedElement, ATL_atlext_EObject, ModuleElement, atlext_ATL_ModuleElement, atlext_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, StringToStringMap, atlext_ATL_Unit, LocatedElement, LibraryRef, atlext_ATL_Library, Unit, Helper, atlext_ATL_Query, OclExpression, atlext_ATL_Module, OclModel, ActionBlock, RuleVariableDeclaration, atlext_ATL_StaticRule, ATL_Rule, atlext_ATL_ModuleCallable, Callable, atlext_ATL_Callable, Library, OclFeatureDefinition, ATL_atlext_Type, atlext_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlext_ATL_ContextHelper, PropertyCallExp, atlext_ATL_Rule, OutPattern, InPatternElement, atlext_ATL_OutPattern, DropPattern, OutPatternElement, CallableParameter, atlext_ATL_RuleWithPattern, Rule, InPattern, RuleWithPattern, atlext_ATL_MatchedRule, atlext_ATL_LazyRule, ATL_RuleWithPattern, ATL_StaticRule, atlext_ATL_CalledRule, StaticRule, Parameter_, atlext_ATL_InPattern, Binding, atlext_ATL_SimpleOutPatternElement, atlext_ATL_ForEachOutPatternElement, atlext_ATL_DropPattern, atlext_ATL_PatternElement, VariableDeclaration, atlext_ATL_InPatternElement, PatternElement, atlext_ATL_SimpleInPatternElement, atlext_ATL_OutPatternElement, atlext_ATL_ActionBlock, Statement, atlext_ATL_Statement, atlext_ATL_ExpressionStat, Iterator, atlext_ATL_Binding, RuleResolutionInfo, atlext_ATL_RuleVariableDeclaration, atlext_ATL_LibraryRef, atlext_ATL_StringToStringMap, atlext_ATL_CallableParameter, atlext_ATL_RuleResolutionInfo, MatchedRule, atlext_ATL_BindingStat, atlext_ATL_IfStat, atlext_ATL_ForStat, LoopExp, OperationCallExp, Operation, atlext_OCL_OclExpression, ATL_LocatedElement, OCL_TypedElement, OclType, IfExp, CollectionExp, LetExp, atlext_OCL_IntegerExp, atlext_OCL_CollectionExp, atlext_OCL_BagExp, atlext_OCL_OrderedSetExp, atlext_OCL_SequenceExp, atlext_OCL_SetExp, atlext_OCL_TupleExp, Attribute, TuplePart, atlext_OCL_TuplePart, OCL_atlext_Type, TupleExp, atlext_OCL_VariableExp, atlext_OCL_MapExp, MapElement, atlext_OCL_SuperExp, atlext_OCL_PrimitiveExp, atlext_OCL_MapElement, atlext_OCL_StringExp, PrimitiveExp, MapExp, atlext_OCL_BooleanExp, atlext_OCL_NumericExp, atlext_OCL_RealExp, NumericExp, atlext_OCL_EnumLiteralExp, atlext_OCL_OclUndefinedExp, atlext_OCL_PropertyCallExp, OCL_atlext_EObject, ContextHelper, atlext_OCL_NavigationOrAttributeCallExp, atlext_OCL_OperationCallExp, ResolveTempResolution, atlext_OCL_CollectionOperationCallExp, atlext_OCL_LoopExp, atlext_OCL_IterateExp, atlext_OCL_IteratorExp, atlext_OCL_LetExp, atlext_OCL_OperatorCallExp, atlext_OCL_IfExp, IterateExp, VariableExp, atlext_OCL_Iterator, atlext_OCL_Parameter, atlext_OCL_CollectionType, atlext_OCL_VariableDeclaration, atlext_OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, atlext_OCL_Primitive, atlext_OCL_StringType, Primitive, atlext_OCL_NumericType, atlext_OCL_IntegerType, NumericType, atlext_OCL_RealType, atlext_OCL_BagType, atlext_OCL_OrderedSetType, atlext_OCL_SequenceType, atlext_OCL_SetType, atlext_OCL_OclAnyType, atlext_OCL_TupleType, atlext_OCL_TupleTypeAttribute, TupleType, atlext_OCL_OclModelElement, atlext_OCL_MapType, atlext_OCL_BooleanType, OclFeature, atlext_OCL_OclContextDefinition, atlext_OCL_OclFeature, atlext_OCL_Attribute, atlext_OCL_Operation, atlext_OCL_OclFeatureDefinition, atlext_OCL_OclModel, OclModelElement, atlext_OCL_TypedElement, atlext_OCL_ResolveTempResolution, atlext_OCL_JavaBody, atlext_OCL_GetAppliedStereotypesBody, JavaBody, atlext_OCL2_SelectByKind, CollectionOperationCallExp, RuleResolutionStatus},
    associations={inModels10, outModels11, elements14, query16, problems0, annotations1, libraries3, helpers4, body6, helpers7, actionBlock31, variables33, calledBy35, library18, definition20, inferredReturnType21, staticReturnType23, contextType26, polymorphicCalledBy28, outPattern29, elements46, filter48, rule50, dropPattern52, callableParameters37, inPattern39, children40, superRule42, parameters45, sourceElement70, bindings73, model75, reverseBindings77, collection79, elements54, outPattern56, mapsTo59, inPattern62, models65, outPattern67, rule101, statements104, expression105, iterator81, value83, outPatternElement85, writtenFeature88, leftType91, resolvedBy94, rule96, unit99, statements125, staticType128, paramDeclaration130, source107, value109, condition112, thenStatements114, elseStatements117, iterator120, collection122, loopExp147, parentOperation149, initializedVariable151, ifExp2154, owningOperation157, rule132, allInvolvedRules133, type136, ifExp3138, appliedProperty140, collection143, letExp145, elements168, ifExp1159, owningAttribute162, tuplePart171, noCastedType164, tuple173, referredVariable165, elements175, map177, source184, usedFeature187, subtypeFeatures188, key179, receptorType191, value181, staticResolver194, dynamicResolvers196, arguments198, resolveTempResolvedBy201, body202, iterators205, result208, in_214, thenExpression217, condition220, elseExpression223, variable211, type226, initExpression229, letExp232, baseExp235, variableExp237, staticType239, loopExpr241, definitions247, oclExpression249, operation252, mapType2255, attribute257, mapType260, collectionTypes263, tupleTypeAttribute265, variableDeclaration267, elementType244, attributes270, type273, tupleType276, model278, valueType281, keyType284, feature287, context_289, definition292, context_295, definition298, initExpression301, type304, parameters307, returnType309, metamodel315, elements318, model320, inferredType323, element325, body312},
    generalizations={gen_atlext_ATL_ModuleElement_LocatedElement, gen_atlext_ATL_Helper_ATL_ModuleElement, gen_atlext_ATL_Helper_ATL_Callable, gen_atlext_ATL_Unit_LocatedElement, gen_atlext_ATL_Library_Unit, gen_atlext_ATL_Query_Unit, gen_atlext_ATL_Module_Unit, gen_atlext_ATL_StaticRule_ATL_ModuleCallable, gen_atlext_ATL_StaticRule_ATL_Rule, gen_atlext_ATL_ModuleCallable_Callable, gen_atlext_ATL_StaticHelper_ATL_Helper, gen_atlext_ATL_StaticHelper_ATL_ModuleCallable, gen_atlext_ATL_ContextHelper_Helper, gen_atlext_ATL_Rule_ModuleElement, gen_atlext_ATL_InPattern_LocatedElement, gen_atlext_ATL_OutPattern_LocatedElement, gen_atlext_ATL_RuleWithPattern_Rule, gen_atlext_ATL_MatchedRule_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_StaticRule, gen_atlext_ATL_CalledRule_StaticRule, gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlext_ATL_DropPattern_LocatedElement, gen_atlext_ATL_PatternElement_VariableDeclaration, gen_atlext_ATL_InPatternElement_PatternElement, gen_atlext_ATL_SimpleInPatternElement_InPatternElement, gen_atlext_ATL_OutPatternElement_PatternElement, gen_atlext_ATL_ActionBlock_LocatedElement, gen_atlext_ATL_Statement_LocatedElement, gen_atlext_ATL_ExpressionStat_Statement, gen_atlext_ATL_Binding_LocatedElement, gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlext_ATL_LibraryRef_LocatedElement, gen_atlext_ATL_BindingStat_Statement, gen_atlext_ATL_IfStat_Statement, gen_atlext_ATL_ForStat_Statement, gen_atlext_OCL_OclExpression_ATL_LocatedElement, gen_atlext_OCL_OclExpression_OCL_TypedElement, gen_atlext_OCL_IntegerExp_NumericExp, gen_atlext_OCL_CollectionExp_OclExpression, gen_atlext_OCL_BagExp_CollectionExp, gen_atlext_OCL_OrderedSetExp_CollectionExp, gen_atlext_OCL_SequenceExp_CollectionExp, gen_atlext_OCL_SetExp_CollectionExp, gen_atlext_OCL_TupleExp_OclExpression, gen_atlext_OCL_TuplePart_VariableDeclaration, gen_atlext_OCL_VariableExp_OclExpression, gen_atlext_OCL_MapExp_OclExpression, gen_atlext_OCL_SuperExp_OclExpression, gen_atlext_OCL_PrimitiveExp_OclExpression, gen_atlext_OCL_MapElement_LocatedElement, gen_atlext_OCL_StringExp_PrimitiveExp, gen_atlext_OCL_BooleanExp_PrimitiveExp, gen_atlext_OCL_NumericExp_PrimitiveExp, gen_atlext_OCL_RealExp_NumericExp, gen_atlext_OCL_EnumLiteralExp_OclExpression, gen_atlext_OCL_OclUndefinedExp_OclExpression, gen_atlext_OCL_PropertyCallExp_OclExpression, gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlext_OCL_OperationCallExp_PropertyCallExp, gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlext_OCL_LoopExp_PropertyCallExp, gen_atlext_OCL_IterateExp_LoopExp, gen_atlext_OCL_IteratorExp_LoopExp, gen_atlext_OCL_LetExp_OclExpression, gen_atlext_OCL_OperatorCallExp_OperationCallExp, gen_atlext_OCL_IfExp_OclExpression, gen_atlext_OCL_VariableDeclaration_OCL_TypedElement, gen_atlext_OCL_Iterator_VariableDeclaration, gen_atlext_OCL_Parameter_VariableDeclaration, gen_atlext_OCL_CollectionType_OclType, gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement, gen_atlext_OCL_OclType_OclExpression, gen_atlext_OCL_Primitive_OclType, gen_atlext_OCL_StringType_Primitive, gen_atlext_OCL_NumericType_Primitive, gen_atlext_OCL_IntegerType_NumericType, gen_atlext_OCL_RealType_NumericType, gen_atlext_OCL_BagType_CollectionType, gen_atlext_OCL_OrderedSetType_CollectionType, gen_atlext_OCL_SequenceType_CollectionType, gen_atlext_OCL_SetType_CollectionType, gen_atlext_OCL_OclAnyType_OclType, gen_atlext_OCL_TupleType_OclType, gen_atlext_OCL_TupleTypeAttribute_LocatedElement, gen_atlext_OCL_OclModelElement_OclType, gen_atlext_OCL_MapType_OclType, gen_atlext_OCL_BooleanType_Primitive, gen_atlext_OCL_OclContextDefinition_LocatedElement, gen_atlext_OCL_OclFeature_LocatedElement, gen_atlext_OCL_Attribute_OclFeature, gen_atlext_OCL_Operation_OclFeature, gen_atlext_OCL_OclFeatureDefinition_LocatedElement, gen_atlext_OCL_OclModel_LocatedElement, gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo, gen_atlext_OCL_JavaBody_OclExpression, gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody, gen_atlext_OCL2_SelectByKind_CollectionOperationCallExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)