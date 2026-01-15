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
atlext_ATL_LocatedElement = Class(name="atlext::ATL::LocatedElement", is_abstract=True)
atlext_ATL_Library = Class(name="atlext::ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
atlext_ATL_Query = Class(name="atlext::ATL::Query")
OclExpression = Class(name="OclExpression")
atlext_ATL_Module = Class(name="atlext::ATL::Module")
StringToStringMap = Class(name="StringToStringMap")
atlext_ATL_Unit = Class(name="atlext::ATL::Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlext_ATL_Helper = Class(name="atlext::ATL::Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL::ModuleElement")
ATL_Callable = Class(name="ATL::Callable")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlext_ATL_StaticHelper = Class(name="atlext::ATL::StaticHelper")
ATL_Helper = Class(name="ATL::Helper")
ATL_ModuleCallable = Class(name="ATL::ModuleCallable")
atlext_ATL_ContextHelper = Class(name="atlext::ATL::ContextHelper")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
atlext_ATL_ModuleElement = Class(name="atlext::ATL::ModuleElement", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlext_ATL_StaticRule = Class(name="atlext::ATL::StaticRule", is_abstract=True)
ATL_Rule = Class(name="ATL::Rule")
atlext_ATL_ModuleCallable = Class(name="atlext::ATL::ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
PropertyCallExp = Class(name="PropertyCallExp")
atlext_ATL_Rule = Class(name="atlext::ATL::Rule", is_abstract=True)
RuleWithPattern = Class(name="RuleWithPattern")
atlext_ATL_MatchedRule = Class(name="atlext::ATL::MatchedRule")
atlext_ATL_LazyRule = Class(name="atlext::ATL::LazyRule")
ATL_RuleWithPattern = Class(name="ATL::RuleWithPattern")
ATL_StaticRule = Class(name="ATL::StaticRule")
atlext_ATL_Callable = Class(name="atlext::ATL::Callable", is_abstract=True)
CallableParameter = Class(name="CallableParameter")
atlext_ATL_RuleWithPattern = Class(name="atlext::ATL::RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
atlext_ATL_OutPattern = Class(name="atlext::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atlext_ATL_DropPattern = Class(name="atlext::ATL::DropPattern")
atlext_ATL_PatternElement = Class(name="atlext::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlext_ATL_InPatternElement = Class(name="atlext::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atlext_ATL_SimpleInPatternElement = Class(name="atlext::ATL::SimpleInPatternElement")
atlext_ATL_CalledRule = Class(name="atlext::ATL::CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
atlext_ATL_InPattern = Class(name="atlext::ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
atlext_ATL_ForEachOutPatternElement = Class(name="atlext::ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlext_ATL_Binding = Class(name="atlext::ATL::Binding")
RuleResolutionInfo = Class(name="RuleResolutionInfo")
atlext_ATL_RuleVariableDeclaration = Class(name="atlext::ATL::RuleVariableDeclaration")
atlext_ATL_OutPatternElement = Class(name="atlext::ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atlext_ATL_SimpleOutPatternElement = Class(name="atlext::ATL::SimpleOutPatternElement")
atlext_ATL_BindingStat = Class(name="atlext::ATL::BindingStat")
atlext_ATL_IfStat = Class(name="atlext::ATL::IfStat")
atlext_ATL_ForStat = Class(name="atlext::ATL::ForStat")
atlext_ATL_LibraryRef = Class(name="atlext::ATL::LibraryRef")
atlext_ATL_ActionBlock = Class(name="atlext::ATL::ActionBlock")
Statement = Class(name="Statement")
atlext_ATL_Statement = Class(name="atlext::ATL::Statement", is_abstract=True)
atlext_ATL_ExpressionStat = Class(name="atlext::ATL::ExpressionStat")
atlext_ATL_RuleResolutionInfo = Class(name="atlext::ATL::RuleResolutionInfo")
MatchedRule = Class(name="MatchedRule")
atlext_OCL_OclExpression = Class(name="atlext::OCL::OclExpression", is_abstract=True)
ATL_LocatedElement = Class(name="ATL::LocatedElement")
OCL_TypedElement = Class(name="OCL::TypedElement")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
atlext_ATL_StringToStringMap = Class(name="atlext::ATL::StringToStringMap")
atlext_ATL_CallableParameter = Class(name="atlext::ATL::CallableParameter")
atlext_OCL_VariableExp = Class(name="atlext::OCL::VariableExp")
atlext_OCL_SuperExp = Class(name="atlext::OCL::SuperExp")
atlext_OCL_PrimitiveExp = Class(name="atlext::OCL::PrimitiveExp", is_abstract=True)
atlext_OCL_StringExp = Class(name="atlext::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atlext_OCL_BooleanExp = Class(name="atlext::OCL::BooleanExp")
atlext_OCL_NumericExp = Class(name="atlext::OCL::NumericExp", is_abstract=True)
atlext_OCL_RealExp = Class(name="atlext::OCL::RealExp")
NumericExp = Class(name="NumericExp")
atlext_OCL_IntegerExp = Class(name="atlext::OCL::IntegerExp")
OperationCallExp = Class(name="OperationCallExp")
atlext_OCL_CollectionExp = Class(name="atlext::OCL::CollectionExp", is_abstract=True)
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
TupleExp = Class(name="TupleExp")
atlext_OCL_MapExp = Class(name="atlext::OCL::MapExp")
MapElement = Class(name="MapElement")
atlext_OCL_MapElement = Class(name="atlext::OCL::MapElement")
MapExp = Class(name="MapExp")
atlext_OCL_BagExp = Class(name="atlext::OCL::BagExp")
atlext_OCL_OrderedSetExp = Class(name="atlext::OCL::OrderedSetExp")
atlext_OCL_SequenceExp = Class(name="atlext::OCL::SequenceExp")
atlext_OCL_SetExp = Class(name="atlext::OCL::SetExp")
atlext_OCL_TupleExp = Class(name="atlext::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
atlext_OCL_PropertyCallExp = Class(name="atlext::OCL::PropertyCallExp", is_abstract=True)
atlext_OCL_TuplePart = Class(name="atlext::OCL::TuplePart")
atlext_OCL_EnumLiteralExp = Class(name="atlext::OCL::EnumLiteralExp")
atlext_OCL_OclUndefinedExp = Class(name="atlext::OCL::OclUndefinedExp")
ResolveTempResolution = Class(name="ResolveTempResolution")
atlext_OCL_OperatorCallExp = Class(name="atlext::OCL::OperatorCallExp")
atlext_OCL_CollectionOperationCallExp = Class(name="atlext::OCL::CollectionOperationCallExp")
atlext_OCL_LoopExp = Class(name="atlext::OCL::LoopExp", is_abstract=True)
atlext_OCL_IterateExp = Class(name="atlext::OCL::IterateExp")
atlext_OCL_IteratorExp = Class(name="atlext::OCL::IteratorExp")
ContextHelper = Class(name="ContextHelper")
atlext_OCL_NavigationOrAttributeCallExp = Class(name="atlext::OCL::NavigationOrAttributeCallExp")
atlext_OCL_OperationCallExp = Class(name="atlext::OCL::OperationCallExp")
atlext_OCL_VariableDeclaration = Class(name="atlext::OCL::VariableDeclaration")
atlext_OCL_LetExp = Class(name="atlext::OCL::LetExp")
atlext_OCL_IfExp = Class(name="atlext::OCL::IfExp")
atlext_OCL_OclType = Class(name="atlext::OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlext_OCL_Iterator = Class(name="atlext::OCL::Iterator")
atlext_OCL_Parameter = Class(name="atlext::OCL::Parameter")
atlext_OCL_CollectionType = Class(name="atlext::OCL::CollectionType")
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
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atlext_OCL_Primitive = Class(name="atlext::OCL::Primitive", is_abstract=True)
atlext_OCL_StringType = Class(name="atlext::OCL::StringType")
Primitive = Class(name="Primitive")
atlext_OCL_BooleanType = Class(name="atlext::OCL::BooleanType")
atlext_OCL_OclModelElement = Class(name="atlext::OCL::OclModelElement")
atlext_OCL_MapType = Class(name="atlext::OCL::MapType")
atlext_OCL_OclFeatureDefinition = Class(name="atlext::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlext_OCL_OclContextDefinition = Class(name="atlext::OCL::OclContextDefinition")
TupleType = Class(name="TupleType")
atlext_OCL_Operation = Class(name="atlext::OCL::Operation")
atlext_OCL_OclModel = Class(name="atlext::OCL::OclModel")
OclModelElement = Class(name="OclModelElement")
atlext_OCL_OclFeature = Class(name="atlext::OCL::OclFeature", is_abstract=True)
atlext_OCL_Attribute = Class(name="atlext::OCL::Attribute")
atlext_OCL_TypedElement = Class(name="atlext::OCL::TypedElement", is_abstract=True)
atlext_OCL_ResolveTempResolution = Class(name="atlext::OCL::ResolveTempResolution")
atlext_OCL_JavaBody = Class(name="atlext::OCL::JavaBody")
atlext_OCL_GetAppliedStereotypesBody = Class(name="atlext::OCL::GetAppliedStereotypesBody")
JavaBody = Class(name="JavaBody")

# atlext_ATL_LocatedElement class attributes and methods
atlext_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlext_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlext_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlext_ATL_LocatedElement_fileLocation: Property = Property(name="fileLocation", type=StringType)
atlext_ATL_LocatedElement_fileObject: Property = Property(name="fileObject", type=StringType)
atlext_ATL_LocatedElement.attributes={atlext_ATL_LocatedElement_fileObject, atlext_ATL_LocatedElement_commentsAfter, atlext_ATL_LocatedElement_commentsBefore, atlext_ATL_LocatedElement_fileLocation, atlext_ATL_LocatedElement_location}

# atlext_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# atlext_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# atlext_ATL_Module class attributes and methods
atlext_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_Module.attributes={atlext_ATL_Module_isRefining}

# StringToStringMap class attributes and methods

# atlext_ATL_Unit class attributes and methods
atlext_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlext_ATL_Unit.attributes={atlext_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# atlext_ATL_Helper class attributes and methods
atlext_ATL_Helper_hasContext: Property = Property(name="hasContext", type=BooleanType)
atlext_ATL_Helper_isAttribute: Property = Property(name="isAttribute", type=StringType)
atlext_ATL_Helper.attributes={atlext_ATL_Helper_isAttribute, atlext_ATL_Helper_hasContext}

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlext_ATL_StaticHelper class attributes and methods

# ATL_Helper class attributes and methods

# ATL_ModuleCallable class attributes and methods

# atlext_ATL_ContextHelper class attributes and methods

# OclModel class attributes and methods

# ModuleElement class attributes and methods

# atlext_ATL_ModuleElement class attributes and methods

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlext_ATL_StaticRule class attributes and methods

# ATL_Rule class attributes and methods

# atlext_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# PropertyCallExp class attributes and methods

# atlext_ATL_Rule class attributes and methods
atlext_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlext_ATL_Rule.attributes={atlext_ATL_Rule_name}

# RuleWithPattern class attributes and methods

# atlext_ATL_MatchedRule class attributes and methods

# atlext_ATL_LazyRule class attributes and methods
atlext_ATL_LazyRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlext_ATL_LazyRule.attributes={atlext_ATL_LazyRule_isUnique}

# ATL_RuleWithPattern class attributes and methods

# ATL_StaticRule class attributes and methods

# atlext_ATL_Callable class attributes and methods

# CallableParameter class attributes and methods

# atlext_ATL_RuleWithPattern class attributes and methods
atlext_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlext_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlext_ATL_RuleWithPattern.attributes={atlext_ATL_RuleWithPattern_isNoDefault, atlext_ATL_RuleWithPattern_isAbstract, atlext_ATL_RuleWithPattern_isRefining}

# Rule class attributes and methods

# InPattern class attributes and methods

# atlext_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atlext_ATL_DropPattern class attributes and methods

# atlext_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlext_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atlext_ATL_SimpleInPatternElement class attributes and methods

# atlext_ATL_CalledRule class attributes and methods
atlext_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlext_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlext_ATL_CalledRule.attributes={atlext_ATL_CalledRule_isEndpoint, atlext_ATL_CalledRule_isEntrypoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# atlext_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlext_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlext_ATL_Binding class attributes and methods
atlext_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_Binding.attributes={atlext_ATL_Binding_propertyName, atlext_ATL_Binding_isAssignment}

# RuleResolutionInfo class attributes and methods

# atlext_ATL_RuleVariableDeclaration class attributes and methods

# atlext_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atlext_ATL_SimpleOutPatternElement class attributes and methods

# atlext_ATL_BindingStat class attributes and methods
atlext_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_BindingStat.attributes={atlext_ATL_BindingStat_propertyName, atlext_ATL_BindingStat_isAssignment}

# atlext_ATL_IfStat class attributes and methods

# atlext_ATL_ForStat class attributes and methods

# atlext_ATL_LibraryRef class attributes and methods
atlext_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlext_ATL_LibraryRef.attributes={atlext_ATL_LibraryRef_name}

# atlext_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atlext_ATL_Statement class attributes and methods

# atlext_ATL_ExpressionStat class attributes and methods

# atlext_ATL_RuleResolutionInfo class attributes and methods

# MatchedRule class attributes and methods

# atlext_OCL_OclExpression class attributes and methods
atlext_OCL_OclExpression_implicitlyCasted: Property = Property(name="implicitlyCasted", type=StringType)
atlext_OCL_OclExpression.attributes={atlext_OCL_OclExpression_implicitlyCasted}

# ATL_LocatedElement class attributes and methods

# OCL_TypedElement class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# atlext_ATL_StringToStringMap class attributes and methods
atlext_ATL_StringToStringMap_key: Property = Property(name="key", type=StringType)
atlext_ATL_StringToStringMap_value: Property = Property(name="value", type=StringType)
atlext_ATL_StringToStringMap.attributes={atlext_ATL_StringToStringMap_key, atlext_ATL_StringToStringMap_value}

# atlext_ATL_CallableParameter class attributes and methods
atlext_ATL_CallableParameter_name: Property = Property(name="name", type=StringType)
atlext_ATL_CallableParameter.attributes={atlext_ATL_CallableParameter_name}

# atlext_OCL_VariableExp class attributes and methods

# atlext_OCL_SuperExp class attributes and methods

# atlext_OCL_PrimitiveExp class attributes and methods

# atlext_OCL_StringExp class attributes and methods
atlext_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atlext_OCL_StringExp.attributes={atlext_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# atlext_OCL_BooleanExp class attributes and methods
atlext_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
atlext_OCL_BooleanExp.attributes={atlext_OCL_BooleanExp_booleanSymbol}

# atlext_OCL_NumericExp class attributes and methods

# atlext_OCL_RealExp class attributes and methods
atlext_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
atlext_OCL_RealExp.attributes={atlext_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atlext_OCL_IntegerExp class attributes and methods
atlext_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlext_OCL_IntegerExp.attributes={atlext_OCL_IntegerExp_integerSymbol}

# OperationCallExp class attributes and methods

# atlext_OCL_CollectionExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# TupleExp class attributes and methods

# atlext_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlext_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# atlext_OCL_BagExp class attributes and methods

# atlext_OCL_OrderedSetExp class attributes and methods

# atlext_OCL_SequenceExp class attributes and methods

# atlext_OCL_SetExp class attributes and methods

# atlext_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# atlext_OCL_PropertyCallExp class attributes and methods
atlext_OCL_PropertyCallExp_isStaticCall: Property = Property(name="isStaticCall", type=BooleanType)
atlext_OCL_PropertyCallExp.attributes={atlext_OCL_PropertyCallExp_isStaticCall}

# atlext_OCL_TuplePart class attributes and methods

# atlext_OCL_EnumLiteralExp class attributes and methods
atlext_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_EnumLiteralExp.attributes={atlext_OCL_EnumLiteralExp_name}

# atlext_OCL_OclUndefinedExp class attributes and methods

# ResolveTempResolution class attributes and methods

# atlext_OCL_OperatorCallExp class attributes and methods

# atlext_OCL_CollectionOperationCallExp class attributes and methods

# atlext_OCL_LoopExp class attributes and methods

# atlext_OCL_IterateExp class attributes and methods

# atlext_OCL_IteratorExp class attributes and methods
atlext_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_IteratorExp.attributes={atlext_OCL_IteratorExp_name}

# ContextHelper class attributes and methods

# atlext_OCL_NavigationOrAttributeCallExp class attributes and methods
atlext_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_NavigationOrAttributeCallExp.attributes={atlext_OCL_NavigationOrAttributeCallExp_name}

# atlext_OCL_OperationCallExp class attributes and methods
atlext_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlext_OCL_OperationCallExp.attributes={atlext_OCL_OperationCallExp_operationName}

# atlext_OCL_VariableDeclaration class attributes and methods
atlext_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlext_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlext_OCL_VariableDeclaration.attributes={atlext_OCL_VariableDeclaration_varName, atlext_OCL_VariableDeclaration_id}

# atlext_OCL_LetExp class attributes and methods

# atlext_OCL_IfExp class attributes and methods

# atlext_OCL_OclType class attributes and methods
atlext_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclType.attributes={atlext_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlext_OCL_Iterator class attributes and methods

# atlext_OCL_Parameter class attributes and methods

# atlext_OCL_CollectionType class attributes and methods

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

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# atlext_OCL_Primitive class attributes and methods

# atlext_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlext_OCL_BooleanType class attributes and methods

# atlext_OCL_OclModelElement class attributes and methods

# atlext_OCL_MapType class attributes and methods

# atlext_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlext_OCL_OclContextDefinition class attributes and methods

# TupleType class attributes and methods

# atlext_OCL_Operation class attributes and methods
atlext_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlext_OCL_Operation.attributes={atlext_OCL_Operation_name}

# atlext_OCL_OclModel class attributes and methods
atlext_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclModel.attributes={atlext_OCL_OclModel_name}

# OclModelElement class attributes and methods

# atlext_OCL_OclFeature class attributes and methods

# atlext_OCL_Attribute class attributes and methods
atlext_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_Attribute.attributes={atlext_OCL_Attribute_name}

# atlext_OCL_TypedElement class attributes and methods

# atlext_OCL_ResolveTempResolution class attributes and methods

# atlext_OCL_JavaBody class attributes and methods

# atlext_OCL_GetAppliedStereotypesBody class attributes and methods

# JavaBody class attributes and methods

# Relationships
helpers3: BinaryAssociation = BinaryAssociation(
    name="helpers3",
    ends={
        Property(name="5", type=atlext_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="9", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="StringToStringMap", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries1: BinaryAssociation = BinaryAssociation(
    name="libraries1",
    ends={
        Property(name="2", type=atlext_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query16: BinaryAssociation = BinaryAssociation(
    name="query16",
    ends={
        Property(name="18", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library19: BinaryAssociation = BinaryAssociation(
    name="library19",
    ends={
        Property(name="21", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition22: BinaryAssociation = BinaryAssociation(
    name="definition22",
    ends={
        Property(name="OclFeatureDefinition", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inModels10: BinaryAssociation = BinaryAssociation(
    name="inModels10",
    ends={
        Property(name="OclModel", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
outPattern26: BinaryAssociation = BinaryAssociation(
    name="outPattern26",
    ends={
        Property(name="28", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock29: BinaryAssociation = BinaryAssociation(
    name="actionBlock29",
    ends={
        Property(name="31", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="30", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables32: BinaryAssociation = BinaryAssociation(
    name="variables32",
    ends={
        Property(name="34", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="33", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polymorphicCalledBy23: BinaryAssociation = BinaryAssociation(
    name="polymorphicCalledBy23",
    ends={
        Property(name="25", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
inPattern38: BinaryAssociation = BinaryAssociation(
    name="inPattern38",
    ends={
        Property(name="atlext_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="InPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1))
    }
)
children39: BinaryAssociation = BinaryAssociation(
    name="children39",
    ends={
        Property(name="41", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="40", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
superRule42: BinaryAssociation = BinaryAssociation(
    name="superRule42",
    ends={
        Property(name="44", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="43", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
calledBy35: BinaryAssociation = BinaryAssociation(
    name="calledBy35",
    ends={
        Property(name="PropertyCallExp", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
callableParameters36: BinaryAssociation = BinaryAssociation(
    name="callableParameters36",
    ends={
        Property(name="CallableParameter", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable37", type=CallableParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule51: BinaryAssociation = BinaryAssociation(
    name="rule51",
    ends={
        Property(name="53", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="52", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern54: BinaryAssociation = BinaryAssociation(
    name="dropPattern54",
    ends={
        Property(name="56", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="55", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements57: BinaryAssociation = BinaryAssociation(
    name="elements57",
    ends={
        Property(name="59", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="58", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern60: BinaryAssociation = BinaryAssociation(
    name="outPattern60",
    ends={
        Property(name="62", type=atlext_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="61", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo63: BinaryAssociation = BinaryAssociation(
    name="mapsTo63",
    ends={
        Property(name="65", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="64", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern66: BinaryAssociation = BinaryAssociation(
    name="inPattern66",
    ends={
        Property(name="68", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="67", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models69: BinaryAssociation = BinaryAssociation(
    name="models69",
    ends={
        Property(name="OclModel70", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="Parameter", type=atlext_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="48", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="47", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter49: BinaryAssociation = BinaryAssociation(
    name="filter49",
    ends={
        Property(name="OclExpression50", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection84: BinaryAssociation = BinaryAssociation(
    name="collection84",
    ends={
        Property(name="OclExpression85", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator86: BinaryAssociation = BinaryAssociation(
    name="iterator86",
    ends={
        Property(name="Iterator", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement87", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value88: BinaryAssociation = BinaryAssociation(
    name="value88",
    ends={
        Property(name="OclExpression89", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement90: BinaryAssociation = BinaryAssociation(
    name="outPatternElement90",
    ends={
        Property(name="92", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="91", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
resolvedBy93: BinaryAssociation = BinaryAssociation(
    name="resolvedBy93",
    ends={
        Property(name="RuleResolutionInfo", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding94", type=RuleResolutionInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outPattern71: BinaryAssociation = BinaryAssociation(
    name="outPattern71",
    ends={
        Property(name="73", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="72", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement74: BinaryAssociation = BinaryAssociation(
    name="sourceElement74",
    ends={
        Property(name="76", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="75", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings77: BinaryAssociation = BinaryAssociation(
    name="bindings77",
    ends={
        Property(name="79", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="78", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model80: BinaryAssociation = BinaryAssociation(
    name="model80",
    ends={
        Property(name="OclModel81", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings82: BinaryAssociation = BinaryAssociation(
    name="reverseBindings82",
    ends={
        Property(name="OclExpression83", type=atlext_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression105: BinaryAssociation = BinaryAssociation(
    name="expression105",
    ends={
        Property(name="OclExpression106", type=atlext_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
rule95: BinaryAssociation = BinaryAssociation(
    name="rule95",
    ends={
        Property(name="97", type=atlext_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="96", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit98: BinaryAssociation = BinaryAssociation(
    name="unit98",
    ends={
        Property(name="100", type=atlext_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="99", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule101: BinaryAssociation = BinaryAssociation(
    name="rule101",
    ends={
        Property(name="103", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="102", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements104: BinaryAssociation = BinaryAssociation(
    name="statements104",
    ends={
        Property(name="Statement", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paramDeclaration128: BinaryAssociation = BinaryAssociation(
    name="paramDeclaration128",
    ends={
        Property(name="atlext_ATL_CallableParameter", type=VariableDeclaration, multiplicity=Multiplicity(0, 1)),
        Property(name="VariableDeclaration", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1))
    }
)
rule129: BinaryAssociation = BinaryAssociation(
    name="rule129",
    ends={
        Property(name="MatchedRule", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
allInvolvedRules130: BinaryAssociation = BinaryAssociation(
    name="allInvolvedRules130",
    ends={
        Property(name="MatchedRule132", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo131", type=MatchedRule, multiplicity=Multiplicity(1, 9999))
    }
)
type133: BinaryAssociation = BinaryAssociation(
    name="type133",
    ends={
        Property(name="135", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="134", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3136: BinaryAssociation = BinaryAssociation(
    name="ifExp3136",
    ends={
        Property(name="138", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="137", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty139: BinaryAssociation = BinaryAssociation(
    name="appliedProperty139",
    ends={
        Property(name="141", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="140", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection142: BinaryAssociation = BinaryAssociation(
    name="collection142",
    ends={
        Property(name="144", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="143", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp145: BinaryAssociation = BinaryAssociation(
    name="letExp145",
    ends={
        Property(name="147", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="146", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp148: BinaryAssociation = BinaryAssociation(
    name="loopExp148",
    ends={
        Property(name="150", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="149", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
collection122: BinaryAssociation = BinaryAssociation(
    name="collection122",
    ends={
        Property(name="OclExpression124", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat123", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements125: BinaryAssociation = BinaryAssociation(
    name="statements125",
    ends={
        Property(name="Statement127", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat126", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable169: BinaryAssociation = BinaryAssociation(
    name="referredVariable169",
    ends={
        Property(name="171", type=atlext_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="170", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parentOperation151: BinaryAssociation = BinaryAssociation(
    name="parentOperation151",
    ends={
        Property(name="153", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="152", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
elements172: BinaryAssociation = BinaryAssociation(
    name="elements172",
    ends={
        Property(name="174", type=atlext_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="173", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedVariable154: BinaryAssociation = BinaryAssociation(
    name="initializedVariable154",
    ends={
        Property(name="156", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="155", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2157: BinaryAssociation = BinaryAssociation(
    name="ifExp2157",
    ends={
        Property(name="159", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="158", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation160: BinaryAssociation = BinaryAssociation(
    name="owningOperation160",
    ends={
        Property(name="162", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="161", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1163: BinaryAssociation = BinaryAssociation(
    name="ifExp1163",
    ends={
        Property(name="165", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="164", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute166: BinaryAssociation = BinaryAssociation(
    name="owningAttribute166",
    ends={
        Property(name="168", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="167", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
tuple178: BinaryAssociation = BinaryAssociation(
    name="tuple178",
    ends={
        Property(name="180", type=atlext_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="179", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements181: BinaryAssociation = BinaryAssociation(
    name="elements181",
    ends={
        Property(name="183", type=atlext_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="182", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map184: BinaryAssociation = BinaryAssociation(
    name="map184",
    ends={
        Property(name="186", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="185", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key187: BinaryAssociation = BinaryAssociation(
    name="key187",
    ends={
        Property(name="OclExpression188", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value189: BinaryAssociation = BinaryAssociation(
    name="value189",
    ends={
        Property(name="OclExpression191", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement190", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuplePart175: BinaryAssociation = BinaryAssociation(
    name="tuplePart175",
    ends={
        Property(name="177", type=atlext_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="176", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source192: BinaryAssociation = BinaryAssociation(
    name="source192",
    ends={
        Property(name="194", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="193", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolveTempResolvedBy202: BinaryAssociation = BinaryAssociation(
    name="resolveTempResolvedBy202",
    ends={
        Property(name="ResolveTempResolution", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OperationCallExp", type=ResolveTempResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body203: BinaryAssociation = BinaryAssociation(
    name="body203",
    ends={
        Property(name="205", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="204", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators206: BinaryAssociation = BinaryAssociation(
    name="iterators206",
    ends={
        Property(name="208", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="207", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result209: BinaryAssociation = BinaryAssociation(
    name="result209",
    ends={
        Property(name="211", type=atlext_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="210", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticResolver195: BinaryAssociation = BinaryAssociation(
    name="staticResolver195",
    ends={
        Property(name="Callable", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp", type=Callable, multiplicity=Multiplicity(1, 1))
    }
)
dynamicResolvers196: BinaryAssociation = BinaryAssociation(
    name="dynamicResolvers196",
    ends={
        Property(name="198", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="197", type=ContextHelper, multiplicity=Multiplicity(0, 9999))
    }
)
arguments199: BinaryAssociation = BinaryAssociation(
    name="arguments199",
    ends={
        Property(name="201", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="200", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenExpression218: BinaryAssociation = BinaryAssociation(
    name="thenExpression218",
    ends={
        Property(name="220", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="219", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition221: BinaryAssociation = BinaryAssociation(
    name="condition221",
    ends={
        Property(name="223", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="222", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression224: BinaryAssociation = BinaryAssociation(
    name="elseExpression224",
    ends={
        Property(name="226", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="225", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type227: BinaryAssociation = BinaryAssociation(
    name="type227",
    ends={
        Property(name="229", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="228", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression230: BinaryAssociation = BinaryAssociation(
    name="initExpression230",
    ends={
        Property(name="232", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="231", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable212: BinaryAssociation = BinaryAssociation(
    name="variable212",
    ends={
        Property(name="214", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="213", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_215: BinaryAssociation = BinaryAssociation(
    name="in_215",
    ends={
        Property(name="217", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="216", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType245: BinaryAssociation = BinaryAssociation(
    name="elementType245",
    ends={
        Property(name="247", type=atlext_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="246", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions248: BinaryAssociation = BinaryAssociation(
    name="definitions248",
    ends={
        Property(name="250", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="249", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression251: BinaryAssociation = BinaryAssociation(
    name="oclExpression251",
    ends={
        Property(name="253", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="252", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation254: BinaryAssociation = BinaryAssociation(
    name="operation254",
    ends={
        Property(name="256", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="255", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2257: BinaryAssociation = BinaryAssociation(
    name="mapType2257",
    ends={
        Property(name="259", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="258", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute260: BinaryAssociation = BinaryAssociation(
    name="attribute260",
    ends={
        Property(name="262", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="261", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
letExp233: BinaryAssociation = BinaryAssociation(
    name="letExp233",
    ends={
        Property(name="235", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="234", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp236: BinaryAssociation = BinaryAssociation(
    name="baseExp236",
    ends={
        Property(name="238", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="237", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp239: BinaryAssociation = BinaryAssociation(
    name="variableExp239",
    ends={
        Property(name="241", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="240", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr242: BinaryAssociation = BinaryAssociation(
    name="loopExpr242",
    ends={
        Property(name="244", type=atlext_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="243", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
attributes275: BinaryAssociation = BinaryAssociation(
    name="attributes275",
    ends={
        Property(name="277", type=atlext_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="276", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapType263: BinaryAssociation = BinaryAssociation(
    name="mapType263",
    ends={
        Property(name="265", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="264", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes266: BinaryAssociation = BinaryAssociation(
    name="collectionTypes266",
    ends={
        Property(name="268", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="267", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute269: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute269",
    ends={
        Property(name="271", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="270", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration272: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration272",
    ends={
        Property(name="274", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="273", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
model284: BinaryAssociation = BinaryAssociation(
    name="model284",
    ends={
        Property(name="286", type=atlext_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="285", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType287: BinaryAssociation = BinaryAssociation(
    name="valueType287",
    ends={
        Property(name="289", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="288", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType290: BinaryAssociation = BinaryAssociation(
    name="keyType290",
    ends={
        Property(name="292", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="291", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature293: BinaryAssociation = BinaryAssociation(
    name="feature293",
    ends={
        Property(name="295", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="294", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_296: BinaryAssociation = BinaryAssociation(
    name="context_296",
    ends={
        Property(name="298", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="297", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type278: BinaryAssociation = BinaryAssociation(
    name="type278",
    ends={
        Property(name="280", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="279", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType281: BinaryAssociation = BinaryAssociation(
    name="tupleType281",
    ends={
        Property(name="283", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="282", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
type311: BinaryAssociation = BinaryAssociation(
    name="type311",
    ends={
        Property(name="313", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="312", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters314: BinaryAssociation = BinaryAssociation(
    name="parameters314",
    ends={
        Property(name="Parameter315", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType316: BinaryAssociation = BinaryAssociation(
    name="returnType316",
    ends={
        Property(name="318", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="317", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body319: BinaryAssociation = BinaryAssociation(
    name="body319",
    ends={
        Property(name="321", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="320", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel322: BinaryAssociation = BinaryAssociation(
    name="metamodel322",
    ends={
        Property(name="324", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="323", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
definition299: BinaryAssociation = BinaryAssociation(
    name="definition299",
    ends={
        Property(name="301", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="300", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_302: BinaryAssociation = BinaryAssociation(
    name="context_302",
    ends={
        Property(name="304", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="303", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition305: BinaryAssociation = BinaryAssociation(
    name="definition305",
    ends={
        Property(name="307", type=atlext_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="306", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression308: BinaryAssociation = BinaryAssociation(
    name="initExpression308",
    ends={
        Property(name="310", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="309", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements325: BinaryAssociation = BinaryAssociation(
    name="elements325",
    ends={
        Property(name="327", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="326", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model328: BinaryAssociation = BinaryAssociation(
    name="model328",
    ends={
        Property(name="330", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="329", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
element331: BinaryAssociation = BinaryAssociation(
    name="element331",
    ends={
        Property(name="OutPatternElement", type=atlext_OCL_ResolveTempResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_ResolveTempResolution", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_atlext_ATL_Library_Unit = Generalization(general=Unit, specific=atlext_ATL_Library)
gen_atlext_ATL_Query_Unit = Generalization(general=Unit, specific=atlext_ATL_Query)
gen_atlext_ATL_Module_Unit = Generalization(general=Unit, specific=atlext_ATL_Module)
gen_atlext_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Unit)
gen_atlext_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlext_ATL_Helper)
gen_atlext_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlext_ATL_Helper)
gen_atlext_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlext_ATL_ContextHelper)
gen_atlext_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ModuleElement)
gen_atlext_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlext_ATL_ModuleCallable)
gen_atlext_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlext_ATL_Rule)
gen_atlext_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlext_ATL_MatchedRule)
gen_atlext_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlext_ATL_RuleWithPattern)
gen_atlext_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_OutPattern)
gen_atlext_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_DropPattern)
gen_atlext_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_PatternElement)
gen_atlext_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_InPatternElement)
gen_atlext_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlext_ATL_SimpleInPatternElement)
gen_atlext_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlext_ATL_CalledRule)
gen_atlext_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_InPattern)
gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_ForEachOutPatternElement)
gen_atlext_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Binding)
gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_RuleVariableDeclaration)
gen_atlext_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_OutPatternElement)
gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_SimpleOutPatternElement)
gen_atlext_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlext_ATL_BindingStat)
gen_atlext_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlext_ATL_IfStat)
gen_atlext_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ForStat)
gen_atlext_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_LibraryRef)
gen_atlext_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ActionBlock)
gen_atlext_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Statement)
gen_atlext_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ExpressionStat)
gen_atlext_OCL_OclExpression_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_OclExpression_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_VariableExp)
gen_atlext_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_SuperExp)
gen_atlext_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PrimitiveExp)
gen_atlext_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_StringExp)
gen_atlext_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_BooleanExp)
gen_atlext_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_NumericExp)
gen_atlext_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_RealExp)
gen_atlext_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_IntegerExp)
gen_atlext_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_CollectionExp)
gen_atlext_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_MapExp)
gen_atlext_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_MapElement)
gen_atlext_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_BagExp)
gen_atlext_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_OrderedSetExp)
gen_atlext_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SequenceExp)
gen_atlext_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SetExp)
gen_atlext_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_TupleExp)
gen_atlext_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PropertyCallExp)
gen_atlext_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_TuplePart)
gen_atlext_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_EnumLiteralExp)
gen_atlext_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclUndefinedExp)
gen_atlext_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_OperatorCallExp)
gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_CollectionOperationCallExp)
gen_atlext_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_LoopExp)
gen_atlext_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IterateExp)
gen_atlext_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IteratorExp)
gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_NavigationOrAttributeCallExp)
gen_atlext_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_OperationCallExp)
gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_VariableDeclaration_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_LetExp)
gen_atlext_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_IfExp)
gen_atlext_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclType)
gen_atlext_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Iterator)
gen_atlext_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Parameter)
gen_atlext_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlext_OCL_CollectionType)
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
gen_atlext_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlext_OCL_Primitive)
gen_atlext_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_StringType)
gen_atlext_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_BooleanType)
gen_atlext_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlext_OCL_OclModelElement)
gen_atlext_OCL_MapType_OclType = Generalization(general=OclType, specific=atlext_OCL_MapType)
gen_atlext_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeatureDefinition)
gen_atlext_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclContextDefinition)
gen_atlext_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Operation)
gen_atlext_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclModel)
gen_atlext_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeature)
gen_atlext_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Attribute)
gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo = Generalization(general=RuleResolutionInfo, specific=atlext_OCL_ResolveTempResolution)
gen_atlext_OCL_JavaBody_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_JavaBody)
gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody = Generalization(general=JavaBody, specific=atlext_OCL_GetAppliedStereotypesBody)

# Domain Model
domain_model = DomainModel(
    name="atlext",
    types={atlext_ATL_LocatedElement, atlext_ATL_Library, Unit, Helper, atlext_ATL_Query, OclExpression, atlext_ATL_Module, StringToStringMap, atlext_ATL_Unit, LocatedElement, LibraryRef, atlext_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, Library, OclFeatureDefinition, atlext_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlext_ATL_ContextHelper, OclModel, ModuleElement, atlext_ATL_ModuleElement, OutPattern, ActionBlock, RuleVariableDeclaration, atlext_ATL_StaticRule, ATL_Rule, atlext_ATL_ModuleCallable, Callable, PropertyCallExp, atlext_ATL_Rule, RuleWithPattern, atlext_ATL_MatchedRule, atlext_ATL_LazyRule, ATL_RuleWithPattern, ATL_StaticRule, atlext_ATL_Callable, CallableParameter, atlext_ATL_RuleWithPattern, Rule, InPattern, atlext_ATL_OutPattern, DropPattern, OutPatternElement, atlext_ATL_DropPattern, atlext_ATL_PatternElement, VariableDeclaration, atlext_ATL_InPatternElement, PatternElement, atlext_ATL_SimpleInPatternElement, atlext_ATL_CalledRule, StaticRule, Parameter_, atlext_ATL_InPattern, InPatternElement, atlext_ATL_ForEachOutPatternElement, Iterator, atlext_ATL_Binding, RuleResolutionInfo, atlext_ATL_RuleVariableDeclaration, atlext_ATL_OutPatternElement, Binding, atlext_ATL_SimpleOutPatternElement, atlext_ATL_BindingStat, atlext_ATL_IfStat, atlext_ATL_ForStat, atlext_ATL_LibraryRef, atlext_ATL_ActionBlock, Statement, atlext_ATL_Statement, atlext_ATL_ExpressionStat, atlext_ATL_RuleResolutionInfo, MatchedRule, atlext_OCL_OclExpression, ATL_LocatedElement, OCL_TypedElement, OclType, IfExp, CollectionExp, LetExp, LoopExp, atlext_ATL_StringToStringMap, atlext_ATL_CallableParameter, atlext_OCL_VariableExp, atlext_OCL_SuperExp, atlext_OCL_PrimitiveExp, atlext_OCL_StringExp, PrimitiveExp, atlext_OCL_BooleanExp, atlext_OCL_NumericExp, atlext_OCL_RealExp, NumericExp, atlext_OCL_IntegerExp, OperationCallExp, atlext_OCL_CollectionExp, Operation, Attribute, TupleExp, atlext_OCL_MapExp, MapElement, atlext_OCL_MapElement, MapExp, atlext_OCL_BagExp, atlext_OCL_OrderedSetExp, atlext_OCL_SequenceExp, atlext_OCL_SetExp, atlext_OCL_TupleExp, TuplePart, atlext_OCL_PropertyCallExp, atlext_OCL_TuplePart, atlext_OCL_EnumLiteralExp, atlext_OCL_OclUndefinedExp, ResolveTempResolution, atlext_OCL_OperatorCallExp, atlext_OCL_CollectionOperationCallExp, atlext_OCL_LoopExp, atlext_OCL_IterateExp, atlext_OCL_IteratorExp, ContextHelper, atlext_OCL_NavigationOrAttributeCallExp, atlext_OCL_OperationCallExp, atlext_OCL_VariableDeclaration, atlext_OCL_LetExp, atlext_OCL_IfExp, atlext_OCL_OclType, OclContextDefinition, MapType, IterateExp, VariableExp, atlext_OCL_Iterator, atlext_OCL_Parameter, atlext_OCL_CollectionType, atlext_OCL_NumericType, atlext_OCL_IntegerType, NumericType, atlext_OCL_RealType, atlext_OCL_BagType, atlext_OCL_OrderedSetType, atlext_OCL_SequenceType, atlext_OCL_SetType, atlext_OCL_OclAnyType, atlext_OCL_TupleType, atlext_OCL_TupleTypeAttribute, CollectionType, TupleTypeAttribute, atlext_OCL_Primitive, atlext_OCL_StringType, Primitive, atlext_OCL_BooleanType, atlext_OCL_OclModelElement, atlext_OCL_MapType, atlext_OCL_OclFeatureDefinition, OclFeature, atlext_OCL_OclContextDefinition, TupleType, atlext_OCL_Operation, atlext_OCL_OclModel, OclModelElement, atlext_OCL_OclFeature, atlext_OCL_Attribute, atlext_OCL_TypedElement, atlext_OCL_ResolveTempResolution, atlext_OCL_JavaBody, atlext_OCL_GetAppliedStereotypesBody, JavaBody},
    associations={helpers3, body6, helpers7, annotations0, libraries1, query16, library19, definition22, inModels10, outModels11, elements14, outPattern26, actionBlock29, variables32, polymorphicCalledBy23, inPattern38, children39, superRule42, calledBy35, callableParameters36, rule51, dropPattern54, elements57, outPattern60, mapsTo63, inPattern66, models69, parameters45, elements46, filter49, collection84, iterator86, value88, outPatternElement90, resolvedBy93, outPattern71, sourceElement74, bindings77, model80, reverseBindings82, expression105, source107, value109, condition112, thenStatements114, elseStatements117, iterator120, rule95, unit98, rule101, statements104, paramDeclaration128, rule129, allInvolvedRules130, type133, ifExp3136, appliedProperty139, collection142, letExp145, loopExp148, collection122, statements125, referredVariable169, parentOperation151, elements172, initializedVariable154, ifExp2157, owningOperation160, ifExp1163, owningAttribute166, tuple178, elements181, map184, key187, value189, tuplePart175, source192, resolveTempResolvedBy202, body203, iterators206, result209, staticResolver195, dynamicResolvers196, arguments199, thenExpression218, condition221, elseExpression224, type227, initExpression230, variable212, in_215, elementType245, definitions248, oclExpression251, operation254, mapType2257, attribute260, letExp233, baseExp236, variableExp239, loopExpr242, attributes275, mapType263, collectionTypes266, tupleTypeAttribute269, variableDeclaration272, model284, valueType287, keyType290, feature293, context_296, type278, tupleType281, type311, parameters314, returnType316, body319, metamodel322, definition299, context_302, definition305, initExpression308, elements325, model328, element331},
    generalizations={gen_atlext_ATL_Library_Unit, gen_atlext_ATL_Query_Unit, gen_atlext_ATL_Module_Unit, gen_atlext_ATL_Unit_LocatedElement, gen_atlext_ATL_Helper_ATL_ModuleElement, gen_atlext_ATL_Helper_ATL_Callable, gen_atlext_ATL_StaticHelper_ATL_Helper, gen_atlext_ATL_StaticHelper_ATL_ModuleCallable, gen_atlext_ATL_ContextHelper_Helper, gen_atlext_ATL_ModuleElement_LocatedElement, gen_atlext_ATL_StaticRule_ATL_ModuleCallable, gen_atlext_ATL_StaticRule_ATL_Rule, gen_atlext_ATL_ModuleCallable_Callable, gen_atlext_ATL_Rule_ModuleElement, gen_atlext_ATL_MatchedRule_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_StaticRule, gen_atlext_ATL_RuleWithPattern_Rule, gen_atlext_ATL_OutPattern_LocatedElement, gen_atlext_ATL_DropPattern_LocatedElement, gen_atlext_ATL_PatternElement_VariableDeclaration, gen_atlext_ATL_InPatternElement_PatternElement, gen_atlext_ATL_SimpleInPatternElement_InPatternElement, gen_atlext_ATL_CalledRule_StaticRule, gen_atlext_ATL_InPattern_LocatedElement, gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlext_ATL_Binding_LocatedElement, gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlext_ATL_OutPatternElement_PatternElement, gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlext_ATL_BindingStat_Statement, gen_atlext_ATL_IfStat_Statement, gen_atlext_ATL_ForStat_Statement, gen_atlext_ATL_LibraryRef_LocatedElement, gen_atlext_ATL_ActionBlock_LocatedElement, gen_atlext_ATL_Statement_LocatedElement, gen_atlext_ATL_ExpressionStat_Statement, gen_atlext_OCL_OclExpression_ATL_LocatedElement, gen_atlext_OCL_OclExpression_OCL_TypedElement, gen_atlext_OCL_VariableExp_OclExpression, gen_atlext_OCL_SuperExp_OclExpression, gen_atlext_OCL_PrimitiveExp_OclExpression, gen_atlext_OCL_StringExp_PrimitiveExp, gen_atlext_OCL_BooleanExp_PrimitiveExp, gen_atlext_OCL_NumericExp_PrimitiveExp, gen_atlext_OCL_RealExp_NumericExp, gen_atlext_OCL_IntegerExp_NumericExp, gen_atlext_OCL_CollectionExp_OclExpression, gen_atlext_OCL_MapExp_OclExpression, gen_atlext_OCL_MapElement_LocatedElement, gen_atlext_OCL_BagExp_CollectionExp, gen_atlext_OCL_OrderedSetExp_CollectionExp, gen_atlext_OCL_SequenceExp_CollectionExp, gen_atlext_OCL_SetExp_CollectionExp, gen_atlext_OCL_TupleExp_OclExpression, gen_atlext_OCL_PropertyCallExp_OclExpression, gen_atlext_OCL_TuplePart_VariableDeclaration, gen_atlext_OCL_EnumLiteralExp_OclExpression, gen_atlext_OCL_OclUndefinedExp_OclExpression, gen_atlext_OCL_OperatorCallExp_OperationCallExp, gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlext_OCL_LoopExp_PropertyCallExp, gen_atlext_OCL_IterateExp_LoopExp, gen_atlext_OCL_IteratorExp_LoopExp, gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlext_OCL_OperationCallExp_PropertyCallExp, gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement, gen_atlext_OCL_VariableDeclaration_OCL_TypedElement, gen_atlext_OCL_LetExp_OclExpression, gen_atlext_OCL_IfExp_OclExpression, gen_atlext_OCL_OclType_OclExpression, gen_atlext_OCL_Iterator_VariableDeclaration, gen_atlext_OCL_Parameter_VariableDeclaration, gen_atlext_OCL_CollectionType_OclType, gen_atlext_OCL_NumericType_Primitive, gen_atlext_OCL_IntegerType_NumericType, gen_atlext_OCL_RealType_NumericType, gen_atlext_OCL_BagType_CollectionType, gen_atlext_OCL_OrderedSetType_CollectionType, gen_atlext_OCL_SequenceType_CollectionType, gen_atlext_OCL_SetType_CollectionType, gen_atlext_OCL_OclAnyType_OclType, gen_atlext_OCL_TupleType_OclType, gen_atlext_OCL_TupleTypeAttribute_LocatedElement, gen_atlext_OCL_Primitive_OclType, gen_atlext_OCL_StringType_Primitive, gen_atlext_OCL_BooleanType_Primitive, gen_atlext_OCL_OclModelElement_OclType, gen_atlext_OCL_MapType_OclType, gen_atlext_OCL_OclFeatureDefinition_LocatedElement, gen_atlext_OCL_OclContextDefinition_LocatedElement, gen_atlext_OCL_Operation_OclFeature, gen_atlext_OCL_OclModel_LocatedElement, gen_atlext_OCL_OclFeature_LocatedElement, gen_atlext_OCL_Attribute_OclFeature, gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo, gen_atlext_OCL_JavaBody_OclExpression, gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)