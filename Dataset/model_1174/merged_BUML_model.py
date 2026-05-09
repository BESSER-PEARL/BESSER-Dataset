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
atlext_ATL_LocatedElement = Class(name="atlext_ATL_LocatedElement", is_abstract=True)
ATL_atlext_EObject = Class(name="ATL_atlext_EObject")
StringToStringMap = Class(name="StringToStringMap")
atlext_ATL_Unit = Class(name="atlext_ATL_Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlext_ATL_Library = Class(name="atlext_ATL_Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
atlext_ATL_Query = Class(name="atlext_ATL_Query")
OclExpression = Class(name="OclExpression")
atlext_ATL_ModuleElement = Class(name="atlext_ATL_ModuleElement", is_abstract=True)
atlext_ATL_Helper = Class(name="atlext_ATL_Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL_ModuleElement")
ATL_Callable = Class(name="ATL_Callable")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
ATL_atlext_Type = Class(name="ATL_atlext_Type")
atlext_ATL_StaticHelper = Class(name="atlext_ATL_StaticHelper")
ATL_Helper = Class(name="ATL_Helper")
ATL_ModuleCallable = Class(name="ATL_ModuleCallable")
atlext_ATL_ContextHelper = Class(name="atlext_ATL_ContextHelper")
PropertyCallExp = Class(name="PropertyCallExp")
atlext_ATL_Rule = Class(name="atlext_ATL_Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlext_ATL_StaticRule = Class(name="atlext_ATL_StaticRule", is_abstract=True)
atlext_ATL_Module = Class(name="atlext_ATL_Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
atlext_ATL_SimpleInPatternElement = Class(name="atlext_ATL_SimpleInPatternElement")
atlext_ATL_OutPatternElement = Class(name="atlext_ATL_OutPatternElement", is_abstract=True)
RuleWithPattern = Class(name="RuleWithPattern")
Binding = Class(name="Binding")
atlext_ATL_MatchedRule = Class(name="atlext_ATL_MatchedRule")
atlext_ATL_LazyRule = Class(name="atlext_ATL_LazyRule")
ATL_RuleWithPattern = Class(name="ATL_RuleWithPattern")
atlext_ATL_SimpleOutPatternElement = Class(name="atlext_ATL_SimpleOutPatternElement")
ATL_StaticRule = Class(name="ATL_StaticRule")
atlext_ATL_CalledRule = Class(name="atlext_ATL_CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
atlext_ATL_InPattern = Class(name="atlext_ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
atlext_ATL_OutPattern = Class(name="atlext_ATL_OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atlext_ATL_DropPattern = Class(name="atlext_ATL_DropPattern")
ATL_Rule = Class(name="ATL_Rule")
atlext_ATL_ModuleCallable = Class(name="atlext_ATL_ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
atlext_ATL_PatternElement = Class(name="atlext_ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlext_ATL_Callable = Class(name="atlext_ATL_Callable", is_abstract=True)
atlext_ATL_InPatternElement = Class(name="atlext_ATL_InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
CallableParameter = Class(name="CallableParameter")
atlext_ATL_RuleWithPattern = Class(name="atlext_ATL_RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
atlext_ATL_ForEachOutPatternElement = Class(name="atlext_ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlext_ATL_Binding = Class(name="atlext_ATL_Binding")
atlext_ATL_IfStat = Class(name="atlext_ATL_IfStat")
RuleResolutionInfo = Class(name="RuleResolutionInfo")
atlext_ATL_RuleVariableDeclaration = Class(name="atlext_ATL_RuleVariableDeclaration")
atlext_ATL_LibraryRef = Class(name="atlext_ATL_LibraryRef")
atlext_ATL_ActionBlock = Class(name="atlext_ATL_ActionBlock")
Statement = Class(name="Statement")
atlext_ATL_Statement = Class(name="atlext_ATL_Statement", is_abstract=True)
atlext_ATL_ExpressionStat = Class(name="atlext_ATL_ExpressionStat")
atlext_ATL_BindingStat = Class(name="atlext_ATL_BindingStat")
IfExp = Class(name="IfExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
atlext_ATL_ForStat = Class(name="atlext_ATL_ForStat")
atlext_ATL_StringToStringMap = Class(name="atlext_ATL_StringToStringMap")
atlext_ATL_CallableParameter = Class(name="atlext_ATL_CallableParameter")
atlext_ATL_RuleResolutionInfo = Class(name="atlext_ATL_RuleResolutionInfo")
MatchedRule = Class(name="MatchedRule")
atlext_OCL_OclExpression = Class(name="atlext_OCL_OclExpression", is_abstract=True)
ATL_LocatedElement = Class(name="ATL_LocatedElement")
OCL_TypedElement = Class(name="OCL_TypedElement")
OclType = Class(name="OclType")
atlext_OCL_RealExp = Class(name="atlext_OCL_RealExp")
NumericExp = Class(name="NumericExp")
atlext_OCL_IntegerExp = Class(name="atlext_OCL_IntegerExp")
atlext_OCL_CollectionExp = Class(name="atlext_OCL_CollectionExp", is_abstract=True)
atlext_OCL_BagExp = Class(name="atlext_OCL_BagExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_atlext_Type = Class(name="OCL_atlext_Type")
atlext_OCL_VariableExp = Class(name="atlext_OCL_VariableExp")
atlext_OCL_SuperExp = Class(name="atlext_OCL_SuperExp")
atlext_OCL_PrimitiveExp = Class(name="atlext_OCL_PrimitiveExp", is_abstract=True)
atlext_OCL_StringExp = Class(name="atlext_OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atlext_OCL_BooleanExp = Class(name="atlext_OCL_BooleanExp")
atlext_OCL_NumericExp = Class(name="atlext_OCL_NumericExp", is_abstract=True)
OCL_atlext_EObject = Class(name="OCL_atlext_EObject")
atlext_OCL_OrderedSetExp = Class(name="atlext_OCL_OrderedSetExp")
atlext_OCL_SequenceExp = Class(name="atlext_OCL_SequenceExp")
atlext_OCL_SetExp = Class(name="atlext_OCL_SetExp")
atlext_OCL_TupleExp = Class(name="atlext_OCL_TupleExp")
TuplePart = Class(name="TuplePart")
atlext_OCL_TuplePart = Class(name="atlext_OCL_TuplePart")
TupleExp = Class(name="TupleExp")
atlext_OCL_MapExp = Class(name="atlext_OCL_MapExp")
MapElement = Class(name="MapElement")
atlext_OCL_MapElement = Class(name="atlext_OCL_MapElement")
MapExp = Class(name="MapExp")
atlext_OCL_EnumLiteralExp = Class(name="atlext_OCL_EnumLiteralExp")
atlext_OCL_OclUndefinedExp = Class(name="atlext_OCL_OclUndefinedExp")
atlext_OCL_PropertyCallExp = Class(name="atlext_OCL_PropertyCallExp", is_abstract=True)
atlext_OCL_IfExp = Class(name="atlext_OCL_IfExp")
ContextHelper = Class(name="ContextHelper")
atlext_OCL_NavigationOrAttributeCallExp = Class(name="atlext_OCL_NavigationOrAttributeCallExp")
atlext_OCL_OperationCallExp = Class(name="atlext_OCL_OperationCallExp")
ResolveTempResolution = Class(name="ResolveTempResolution")
atlext_OCL_OperatorCallExp = Class(name="atlext_OCL_OperatorCallExp")
atlext_OCL_CollectionOperationCallExp = Class(name="atlext_OCL_CollectionOperationCallExp")
atlext_OCL_LoopExp = Class(name="atlext_OCL_LoopExp", is_abstract=True)
atlext_OCL_IterateExp = Class(name="atlext_OCL_IterateExp")
atlext_OCL_IteratorExp = Class(name="atlext_OCL_IteratorExp")
atlext_OCL_LetExp = Class(name="atlext_OCL_LetExp")
atlext_OCL_Parameter = Class(name="atlext_OCL_Parameter")
atlext_OCL_CollectionType = Class(name="atlext_OCL_CollectionType")
atlext_OCL_OclType = Class(name="atlext_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
atlext_OCL_VariableDeclaration = Class(name="atlext_OCL_VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlext_OCL_Iterator = Class(name="atlext_OCL_Iterator")
atlext_OCL_SetType = Class(name="atlext_OCL_SetType")
atlext_OCL_OclAnyType = Class(name="atlext_OCL_OclAnyType")
atlext_OCL_TupleType = Class(name="atlext_OCL_TupleType")
atlext_OCL_TupleTypeAttribute = Class(name="atlext_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atlext_OCL_Primitive = Class(name="atlext_OCL_Primitive", is_abstract=True)
atlext_OCL_StringType = Class(name="atlext_OCL_StringType")
Primitive = Class(name="Primitive")
atlext_OCL_BooleanType = Class(name="atlext_OCL_BooleanType")
atlext_OCL_NumericType = Class(name="atlext_OCL_NumericType", is_abstract=True)
atlext_OCL_IntegerType = Class(name="atlext_OCL_IntegerType")
NumericType = Class(name="NumericType")
atlext_OCL_RealType = Class(name="atlext_OCL_RealType")
atlext_OCL_BagType = Class(name="atlext_OCL_BagType")
atlext_OCL_OrderedSetType = Class(name="atlext_OCL_OrderedSetType")
atlext_OCL_SequenceType = Class(name="atlext_OCL_SequenceType")
atlext_OCL_Operation = Class(name="atlext_OCL_Operation")
atlext_OCL_OclModelElement = Class(name="atlext_OCL_OclModelElement")
atlext_OCL_MapType = Class(name="atlext_OCL_MapType")
atlext_OCL_OclFeatureDefinition = Class(name="atlext_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlext_OCL_OclContextDefinition = Class(name="atlext_OCL_OclContextDefinition")
atlext_OCL_OclFeature = Class(name="atlext_OCL_OclFeature", is_abstract=True)
atlext_OCL_Attribute = Class(name="atlext_OCL_Attribute")
atlext_OCL_OclModel = Class(name="atlext_OCL_OclModel")
OclModelElement = Class(name="OclModelElement")
atlext_OCL_TypedElement = Class(name="atlext_OCL_TypedElement", is_abstract=True)
atlext_OCL_ResolveTempResolution = Class(name="atlext_OCL_ResolveTempResolution")
atlext_OCL_JavaBody = Class(name="atlext_OCL_JavaBody")
atlext_OCL_GetAppliedStereotypesBody = Class(name="atlext_OCL_GetAppliedStereotypesBody")
JavaBody = Class(name="JavaBody")
atlext_OCL2_SelectByKind = Class(name="atlext_OCL2_SelectByKind")
CollectionOperationCallExp = Class(name="CollectionOperationCallExp")

# atlext_ATL_LocatedElement class attributes and methods
atlext_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlext_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlext_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlext_ATL_LocatedElement_fileLocation: Property = Property(name="fileLocation", type=StringType)
atlext_ATL_LocatedElement_fileObject: Property = Property(name="fileObject", type=StringType)
atlext_ATL_LocatedElement.attributes={atlext_ATL_LocatedElement_location, atlext_ATL_LocatedElement_fileObject, atlext_ATL_LocatedElement_commentsBefore, atlext_ATL_LocatedElement_commentsAfter, atlext_ATL_LocatedElement_fileLocation}

# ATL_atlext_EObject class attributes and methods

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

# atlext_ATL_ModuleElement class attributes and methods

# atlext_ATL_Helper class attributes and methods
atlext_ATL_Helper_hasContext: Property = Property(name="hasContext", type=BooleanType)
atlext_ATL_Helper_isAttribute: Property = Property(name="isAttribute", type=BooleanType)
atlext_ATL_Helper.attributes={atlext_ATL_Helper_isAttribute, atlext_ATL_Helper_hasContext}

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

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

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlext_ATL_StaticRule class attributes and methods

# atlext_ATL_Module class attributes and methods
atlext_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_Module.attributes={atlext_ATL_Module_isRefining}

# OclModel class attributes and methods

# ModuleElement class attributes and methods

# atlext_ATL_SimpleInPatternElement class attributes and methods

# atlext_ATL_OutPatternElement class attributes and methods

# RuleWithPattern class attributes and methods

# Binding class attributes and methods

# atlext_ATL_MatchedRule class attributes and methods

# atlext_ATL_LazyRule class attributes and methods
atlext_ATL_LazyRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlext_ATL_LazyRule.attributes={atlext_ATL_LazyRule_isUnique}

# ATL_RuleWithPattern class attributes and methods

# atlext_ATL_SimpleOutPatternElement class attributes and methods

# ATL_StaticRule class attributes and methods

# atlext_ATL_CalledRule class attributes and methods
atlext_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlext_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlext_ATL_CalledRule.attributes={atlext_ATL_CalledRule_isEndpoint, atlext_ATL_CalledRule_isEntrypoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# atlext_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlext_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atlext_ATL_DropPattern class attributes and methods

# ATL_Rule class attributes and methods

# atlext_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# atlext_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlext_ATL_Callable class attributes and methods

# atlext_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# CallableParameter class attributes and methods

# atlext_ATL_RuleWithPattern class attributes and methods
atlext_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlext_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlext_ATL_RuleWithPattern.attributes={atlext_ATL_RuleWithPattern_isRefining, atlext_ATL_RuleWithPattern_isNoDefault, atlext_ATL_RuleWithPattern_isAbstract}

# Rule class attributes and methods

# InPattern class attributes and methods

# atlext_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlext_ATL_Binding class attributes and methods
atlext_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_Binding.attributes={atlext_ATL_Binding_propertyName, atlext_ATL_Binding_isAssignment}

# atlext_ATL_IfStat class attributes and methods

# RuleResolutionInfo class attributes and methods

# atlext_ATL_RuleVariableDeclaration class attributes and methods

# atlext_ATL_LibraryRef class attributes and methods
atlext_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlext_ATL_LibraryRef.attributes={atlext_ATL_LibraryRef_name}

# atlext_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atlext_ATL_Statement class attributes and methods

# atlext_ATL_ExpressionStat class attributes and methods

# atlext_ATL_BindingStat class attributes and methods
atlext_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_BindingStat.attributes={atlext_ATL_BindingStat_isAssignment, atlext_ATL_BindingStat_propertyName}

# IfExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# atlext_ATL_ForStat class attributes and methods

# atlext_ATL_StringToStringMap class attributes and methods
atlext_ATL_StringToStringMap_key: Property = Property(name="key", type=StringType)
atlext_ATL_StringToStringMap_value: Property = Property(name="value", type=StringType)
atlext_ATL_StringToStringMap.attributes={atlext_ATL_StringToStringMap_key, atlext_ATL_StringToStringMap_value}

# atlext_ATL_CallableParameter class attributes and methods
atlext_ATL_CallableParameter_name: Property = Property(name="name", type=StringType)
atlext_ATL_CallableParameter.attributes={atlext_ATL_CallableParameter_name}

# atlext_ATL_RuleResolutionInfo class attributes and methods
atlext_ATL_RuleResolutionInfo_status: Property = Property(name="status", type=StringType)
atlext_ATL_RuleResolutionInfo.attributes={atlext_ATL_RuleResolutionInfo_status}

# MatchedRule class attributes and methods

# atlext_OCL_OclExpression class attributes and methods
atlext_OCL_OclExpression_implicitlyCasted: Property = Property(name="implicitlyCasted", type=BooleanType)
atlext_OCL_OclExpression.attributes={atlext_OCL_OclExpression_implicitlyCasted}

# ATL_LocatedElement class attributes and methods

# OCL_TypedElement class attributes and methods

# OclType class attributes and methods

# atlext_OCL_RealExp class attributes and methods
atlext_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
atlext_OCL_RealExp.attributes={atlext_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atlext_OCL_IntegerExp class attributes and methods
atlext_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlext_OCL_IntegerExp.attributes={atlext_OCL_IntegerExp_integerSymbol}

# atlext_OCL_CollectionExp class attributes and methods

# atlext_OCL_BagExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OCL_atlext_Type class attributes and methods

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

# OCL_atlext_EObject class attributes and methods

# atlext_OCL_OrderedSetExp class attributes and methods

# atlext_OCL_SequenceExp class attributes and methods

# atlext_OCL_SetExp class attributes and methods

# atlext_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# atlext_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# atlext_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlext_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# atlext_OCL_EnumLiteralExp class attributes and methods
atlext_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_EnumLiteralExp.attributes={atlext_OCL_EnumLiteralExp_name}

# atlext_OCL_OclUndefinedExp class attributes and methods

# atlext_OCL_PropertyCallExp class attributes and methods
atlext_OCL_PropertyCallExp_isStaticCall: Property = Property(name="isStaticCall", type=BooleanType)
atlext_OCL_PropertyCallExp.attributes={atlext_OCL_PropertyCallExp_isStaticCall}

# atlext_OCL_IfExp class attributes and methods

# ContextHelper class attributes and methods

# atlext_OCL_NavigationOrAttributeCallExp class attributes and methods
atlext_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_NavigationOrAttributeCallExp.attributes={atlext_OCL_NavigationOrAttributeCallExp_name}

# atlext_OCL_OperationCallExp class attributes and methods
atlext_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlext_OCL_OperationCallExp.attributes={atlext_OCL_OperationCallExp_operationName}

# ResolveTempResolution class attributes and methods

# atlext_OCL_OperatorCallExp class attributes and methods

# atlext_OCL_CollectionOperationCallExp class attributes and methods

# atlext_OCL_LoopExp class attributes and methods

# atlext_OCL_IterateExp class attributes and methods

# atlext_OCL_IteratorExp class attributes and methods
atlext_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlext_OCL_IteratorExp.attributes={atlext_OCL_IteratorExp_name}

# atlext_OCL_LetExp class attributes and methods

# atlext_OCL_Parameter class attributes and methods

# atlext_OCL_CollectionType class attributes and methods

# atlext_OCL_OclType class attributes and methods
atlext_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclType.attributes={atlext_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# atlext_OCL_VariableDeclaration class attributes and methods
atlext_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlext_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlext_OCL_VariableDeclaration.attributes={atlext_OCL_VariableDeclaration_varName, atlext_OCL_VariableDeclaration_id}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlext_OCL_Iterator class attributes and methods

# atlext_OCL_SetType class attributes and methods

# atlext_OCL_OclAnyType class attributes and methods

# atlext_OCL_TupleType class attributes and methods

# atlext_OCL_TupleTypeAttribute class attributes and methods
atlext_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_TupleTypeAttribute.attributes={atlext_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# atlext_OCL_Primitive class attributes and methods

# atlext_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlext_OCL_BooleanType class attributes and methods

# atlext_OCL_NumericType class attributes and methods

# atlext_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# atlext_OCL_RealType class attributes and methods

# atlext_OCL_BagType class attributes and methods

# atlext_OCL_OrderedSetType class attributes and methods

# atlext_OCL_SequenceType class attributes and methods

# atlext_OCL_Operation class attributes and methods
atlext_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlext_OCL_Operation.attributes={atlext_OCL_Operation_name}

# atlext_OCL_OclModelElement class attributes and methods

# atlext_OCL_MapType class attributes and methods

# atlext_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlext_OCL_OclContextDefinition class attributes and methods

# atlext_OCL_OclFeature class attributes and methods

# atlext_OCL_Attribute class attributes and methods
atlext_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_Attribute.attributes={atlext_OCL_Attribute_name}

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
        Property(name="LibraryRef", type=atlext_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="Helper", type=atlext_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="OclExpression", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
query14: BinaryAssociation = BinaryAssociation(
    name="query14",
    ends={
        Property(name="Query", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library15: BinaryAssociation = BinaryAssociation(
    name="library15",
    ends={
        Property(name="Library", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers16", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition17: BinaryAssociation = BinaryAssociation(
    name="definition17",
    ends={
        Property(name="OclFeatureDefinition", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inferredReturnType18: BinaryAssociation = BinaryAssociation(
    name="inferredReturnType18",
    ends={
        Property(name="ATL_atlext_Type", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper19", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
staticReturnType20: BinaryAssociation = BinaryAssociation(
    name="staticReturnType20",
    ends={
        Property(name="ATL_atlext_Type22", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper21", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
contextType23: BinaryAssociation = BinaryAssociation(
    name="contextType23",
    ends={
        Property(name="ATL_atlext_Type24", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ContextHelper", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
polymorphicCalledBy25: BinaryAssociation = BinaryAssociation(
    name="polymorphicCalledBy25",
    ends={
        Property(name="PropertyCallExp", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="dynamicResolvers", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern26: BinaryAssociation = BinaryAssociation(
    name="outPattern26",
    ends={
        Property(name="OutPattern", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock27: BinaryAssociation = BinaryAssociation(
    name="actionBlock27",
    ends={
        Property(name="ActionBlock", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule28", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables29: BinaryAssociation = BinaryAssociation(
    name="variables29",
    ends={
        Property(name="RuleVariableDeclaration", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule30", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers6: BinaryAssociation = BinaryAssociation(
    name="helpers6",
    ends={
        Property(name="Helper7", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels8: BinaryAssociation = BinaryAssociation(
    name="inModels8",
    ends={
        Property(name="OclModel", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels9: BinaryAssociation = BinaryAssociation(
    name="outModels9",
    ends={
        Property(name="OclModel11", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module10", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="ModuleElement", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module13", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children36: BinaryAssociation = BinaryAssociation(
    name="children36",
    ends={
        Property(name="RuleWithPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern56: BinaryAssociation = BinaryAssociation(
    name="outPattern56",
    ends={
        Property(name="OutPattern58", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements57", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
superRule37: BinaryAssociation = BinaryAssociation(
    name="superRule37",
    ends={
        Property(name="RuleWithPattern38", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
sourceElement59: BinaryAssociation = BinaryAssociation(
    name="sourceElement59",
    ends={
        Property(name="InPatternElement60", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings61: BinaryAssociation = BinaryAssociation(
    name="bindings61",
    ends={
        Property(name="Binding", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model62: BinaryAssociation = BinaryAssociation(
    name="model62",
    ends={
        Property(name="OclModel63", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
parameters39: BinaryAssociation = BinaryAssociation(
    name="parameters39",
    ends={
        Property(name="Parameter", type=atlext_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements40: BinaryAssociation = BinaryAssociation(
    name="elements40",
    ends={
        Property(name="InPatternElement", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter41: BinaryAssociation = BinaryAssociation(
    name="filter41",
    ends={
        Property(name="OclExpression42", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule43: BinaryAssociation = BinaryAssociation(
    name="rule43",
    ends={
        Property(name="Rule", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern44: BinaryAssociation = BinaryAssociation(
    name="dropPattern44",
    ends={
        Property(name="DropPattern", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern45", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="OutPatternElement", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern47", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern48: BinaryAssociation = BinaryAssociation(
    name="outPattern48",
    ends={
        Property(name="OutPattern49", type=atlext_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
calledBy31: BinaryAssociation = BinaryAssociation(
    name="calledBy31",
    ends={
        Property(name="PropertyCallExp32", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
mapsTo50: BinaryAssociation = BinaryAssociation(
    name="mapsTo50",
    ends={
        Property(name="OutPatternElement51", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
callableParameters33: BinaryAssociation = BinaryAssociation(
    name="callableParameters33",
    ends={
        Property(name="CallableParameter", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable34", type=CallableParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern52: BinaryAssociation = BinaryAssociation(
    name="inPattern52",
    ends={
        Property(name="InPattern53", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models54: BinaryAssociation = BinaryAssociation(
    name="models54",
    ends={
        Property(name="OclModel55", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
inPattern35: BinaryAssociation = BinaryAssociation(
    name="inPattern35",
    ends={
        Property(name="InPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
writtenFeature74: BinaryAssociation = BinaryAssociation(
    name="writtenFeature74",
    ends={
        Property(name="ATL_atlext_EObject76", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding75", type=ATL_atlext_EObject, multiplicity=Multiplicity(1, 1))
    }
)
leftType77: BinaryAssociation = BinaryAssociation(
    name="leftType77",
    ends={
        Property(name="ATL_atlext_Type79", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding78", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
reverseBindings64: BinaryAssociation = BinaryAssociation(
    name="reverseBindings64",
    ends={
        Property(name="OclExpression65", type=atlext_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection66: BinaryAssociation = BinaryAssociation(
    name="collection66",
    ends={
        Property(name="OclExpression67", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator68: BinaryAssociation = BinaryAssociation(
    name="iterator68",
    ends={
        Property(name="Iterator", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement69", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value70: BinaryAssociation = BinaryAssociation(
    name="value70",
    ends={
        Property(name="OclExpression71", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement72: BinaryAssociation = BinaryAssociation(
    name="outPatternElement72",
    ends={
        Property(name="OutPatternElement73", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="OclExpression94", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat93", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition95: BinaryAssociation = BinaryAssociation(
    name="condition95",
    ends={
        Property(name="OclExpression96", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements97: BinaryAssociation = BinaryAssociation(
    name="thenStatements97",
    ends={
        Property(name="Statement99", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat98", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements100: BinaryAssociation = BinaryAssociation(
    name="elseStatements100",
    ends={
        Property(name="Statement102", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat101", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedBy80: BinaryAssociation = BinaryAssociation(
    name="resolvedBy80",
    ends={
        Property(name="RuleResolutionInfo", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding81", type=RuleResolutionInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule82: BinaryAssociation = BinaryAssociation(
    name="rule82",
    ends={
        Property(name="Rule83", type=atlext_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit84: BinaryAssociation = BinaryAssociation(
    name="unit84",
    ends={
        Property(name="Unit", type=atlext_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule85: BinaryAssociation = BinaryAssociation(
    name="rule85",
    ends={
        Property(name="Rule86", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements87: BinaryAssociation = BinaryAssociation(
    name="statements87",
    ends={
        Property(name="Statement", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="OclExpression89", type=atlext_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source90: BinaryAssociation = BinaryAssociation(
    name="source90",
    ends={
        Property(name="OclExpression91", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="OclType", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
ifExp3120: BinaryAssociation = BinaryAssociation(
    name="ifExp3120",
    ends={
        Property(name="IfExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty121: BinaryAssociation = BinaryAssociation(
    name="appliedProperty121",
    ends={
        Property(name="PropertyCallExp122", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection123: BinaryAssociation = BinaryAssociation(
    name="collection123",
    ends={
        Property(name="CollectionExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements124", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp125: BinaryAssociation = BinaryAssociation(
    name="letExp125",
    ends={
        Property(name="LetExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
iterator103: BinaryAssociation = BinaryAssociation(
    name="iterator103",
    ends={
        Property(name="Iterator104", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection105: BinaryAssociation = BinaryAssociation(
    name="collection105",
    ends={
        Property(name="OclExpression107", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat106", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements108: BinaryAssociation = BinaryAssociation(
    name="statements108",
    ends={
        Property(name="Statement110", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat109", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticType111: BinaryAssociation = BinaryAssociation(
    name="staticType111",
    ends={
        Property(name="ATL_atlext_Type112", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
paramDeclaration113: BinaryAssociation = BinaryAssociation(
    name="paramDeclaration113",
    ends={
        Property(name="VariableDeclaration", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter114", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
rule115: BinaryAssociation = BinaryAssociation(
    name="rule115",
    ends={
        Property(name="MatchedRule", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
allInvolvedRules116: BinaryAssociation = BinaryAssociation(
    name="allInvolvedRules116",
    ends={
        Property(name="MatchedRule118", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo117", type=MatchedRule, multiplicity=Multiplicity(1, 9999))
    }
)
elements141: BinaryAssociation = BinaryAssociation(
    name="elements141",
    ends={
        Property(name="OclExpression142", type=atlext_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopExp126: BinaryAssociation = BinaryAssociation(
    name="loopExp126",
    ends={
        Property(name="LoopExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation127: BinaryAssociation = BinaryAssociation(
    name="parentOperation127",
    ends={
        Property(name="OperationCallExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable128: BinaryAssociation = BinaryAssociation(
    name="initializedVariable128",
    ends={
        Property(name="VariableDeclaration129", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2130: BinaryAssociation = BinaryAssociation(
    name="ifExp2130",
    ends={
        Property(name="IfExp131", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation132: BinaryAssociation = BinaryAssociation(
    name="owningOperation132",
    ends={
        Property(name="Operation", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body133", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1134: BinaryAssociation = BinaryAssociation(
    name="ifExp1134",
    ends={
        Property(name="IfExp135", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute136: BinaryAssociation = BinaryAssociation(
    name="owningAttribute136",
    ends={
        Property(name="Attribute", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression137", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
noCastedType138: BinaryAssociation = BinaryAssociation(
    name="noCastedType138",
    ends={
        Property(name="OCL_atlext_Type", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OclExpression", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable139: BinaryAssociation = BinaryAssociation(
    name="referredVariable139",
    ends={
        Property(name="VariableDeclaration140", type=atlext_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
source153: BinaryAssociation = BinaryAssociation(
    name="source153",
    ends={
        Property(name="OclExpression154", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usedFeature155: BinaryAssociation = BinaryAssociation(
    name="usedFeature155",
    ends={
        Property(name="OCL_atlext_EObject", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subtypeFeatures156: BinaryAssociation = BinaryAssociation(
    name="subtypeFeatures156",
    ends={
        Property(name="OCL_atlext_EObject158", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp157", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
receptorType159: BinaryAssociation = BinaryAssociation(
    name="receptorType159",
    ends={
        Property(name="OCL_atlext_EObject161", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp160", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
staticResolver162: BinaryAssociation = BinaryAssociation(
    name="staticResolver162",
    ends={
        Property(name="Callable", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp163", type=Callable, multiplicity=Multiplicity(1, 1))
    }
)
tuplePart143: BinaryAssociation = BinaryAssociation(
    name="tuplePart143",
    ends={
        Property(name="TuplePart", type=atlext_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple144: BinaryAssociation = BinaryAssociation(
    name="tuple144",
    ends={
        Property(name="TupleExp", type=atlext_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements145: BinaryAssociation = BinaryAssociation(
    name="elements145",
    ends={
        Property(name="MapElement", type=atlext_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map146: BinaryAssociation = BinaryAssociation(
    name="map146",
    ends={
        Property(name="MapExp", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements147", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key148: BinaryAssociation = BinaryAssociation(
    name="key148",
    ends={
        Property(name="OclExpression149", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value150: BinaryAssociation = BinaryAssociation(
    name="value150",
    ends={
        Property(name="OclExpression152", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement151", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_176: BinaryAssociation = BinaryAssociation(
    name="in_176",
    ends={
        Property(name="OclExpression178", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp177", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression179: BinaryAssociation = BinaryAssociation(
    name="thenExpression179",
    ends={
        Property(name="OclExpression180", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dynamicResolvers164: BinaryAssociation = BinaryAssociation(
    name="dynamicResolvers164",
    ends={
        Property(name="ContextHelper", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="polymorphicCalledBy", type=ContextHelper, multiplicity=Multiplicity(0, 9999))
    }
)
arguments165: BinaryAssociation = BinaryAssociation(
    name="arguments165",
    ends={
        Property(name="OclExpression166", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolveTempResolvedBy167: BinaryAssociation = BinaryAssociation(
    name="resolveTempResolvedBy167",
    ends={
        Property(name="ResolveTempResolution", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OperationCallExp", type=ResolveTempResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body168: BinaryAssociation = BinaryAssociation(
    name="body168",
    ends={
        Property(name="OclExpression169", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators170: BinaryAssociation = BinaryAssociation(
    name="iterators170",
    ends={
        Property(name="Iterator171", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result172: BinaryAssociation = BinaryAssociation(
    name="result172",
    ends={
        Property(name="VariableDeclaration173", type=atlext_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable174: BinaryAssociation = BinaryAssociation(
    name="variable174",
    ends={
        Property(name="VariableDeclaration175", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType197: BinaryAssociation = BinaryAssociation(
    name="elementType197",
    ends={
        Property(name="OclType198", type=atlext_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions199: BinaryAssociation = BinaryAssociation(
    name="definitions199",
    ends={
        Property(name="OclContextDefinition", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
condition181: BinaryAssociation = BinaryAssociation(
    name="condition181",
    ends={
        Property(name="OclExpression182", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression183: BinaryAssociation = BinaryAssociation(
    name="elseExpression183",
    ends={
        Property(name="OclExpression184", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="OclType186", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression187: BinaryAssociation = BinaryAssociation(
    name="initExpression187",
    ends={
        Property(name="OclExpression188", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp189: BinaryAssociation = BinaryAssociation(
    name="letExp189",
    ends={
        Property(name="LetExp190", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp191: BinaryAssociation = BinaryAssociation(
    name="baseExp191",
    ends={
        Property(name="IterateExp", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp192: BinaryAssociation = BinaryAssociation(
    name="variableExp192",
    ends={
        Property(name="VariableExp", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
staticType193: BinaryAssociation = BinaryAssociation(
    name="staticType193",
    ends={
        Property(name="OCL_atlext_Type194", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_VariableDeclaration", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr195: BinaryAssociation = BinaryAssociation(
    name="loopExpr195",
    ends={
        Property(name="LoopExp196", type=atlext_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
attributes216: BinaryAssociation = BinaryAssociation(
    name="attributes216",
    ends={
        Property(name="TupleTypeAttribute217", type=atlext_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type218: BinaryAssociation = BinaryAssociation(
    name="type218",
    ends={
        Property(name="OclType219", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclExpression200: BinaryAssociation = BinaryAssociation(
    name="oclExpression200",
    ends={
        Property(name="OclExpression201", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation202: BinaryAssociation = BinaryAssociation(
    name="operation202",
    ends={
        Property(name="Operation203", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2204: BinaryAssociation = BinaryAssociation(
    name="mapType2204",
    ends={
        Property(name="MapType", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute205: BinaryAssociation = BinaryAssociation(
    name="attribute205",
    ends={
        Property(name="Attribute207", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type206", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType208: BinaryAssociation = BinaryAssociation(
    name="mapType208",
    ends={
        Property(name="MapType209", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes210: BinaryAssociation = BinaryAssociation(
    name="collectionTypes210",
    ends={
        Property(name="CollectionType", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute211: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute211",
    ends={
        Property(name="TupleTypeAttribute", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type212", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration213: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration213",
    ends={
        Property(name="VariableDeclaration215", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type214", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
initExpression239: BinaryAssociation = BinaryAssociation(
    name="initExpression239",
    ends={
        Property(name="OclExpression240", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type241: BinaryAssociation = BinaryAssociation(
    name="type241",
    ends={
        Property(name="OclType242", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters243: BinaryAssociation = BinaryAssociation(
    name="parameters243",
    ends={
        Property(name="Parameter244", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tupleType220: BinaryAssociation = BinaryAssociation(
    name="tupleType220",
    ends={
        Property(name="TupleType", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model221: BinaryAssociation = BinaryAssociation(
    name="model221",
    ends={
        Property(name="OclModel223", type=atlext_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements222", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType224: BinaryAssociation = BinaryAssociation(
    name="valueType224",
    ends={
        Property(name="OclType225", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType226: BinaryAssociation = BinaryAssociation(
    name="keyType226",
    ends={
        Property(name="OclType227", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature228: BinaryAssociation = BinaryAssociation(
    name="feature228",
    ends={
        Property(name="OclFeature", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_229: BinaryAssociation = BinaryAssociation(
    name="context_229",
    ends={
        Property(name="OclContextDefinition231", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition230", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition232: BinaryAssociation = BinaryAssociation(
    name="definition232",
    ends={
        Property(name="OclFeatureDefinition234", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_233", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_235: BinaryAssociation = BinaryAssociation(
    name="context_235",
    ends={
        Property(name="OclType236", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition237: BinaryAssociation = BinaryAssociation(
    name="definition237",
    ends={
        Property(name="OclFeatureDefinition238", type=atlext_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
returnType245: BinaryAssociation = BinaryAssociation(
    name="returnType245",
    ends={
        Property(name="OclType246", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body247: BinaryAssociation = BinaryAssociation(
    name="body247",
    ends={
        Property(name="OclExpression248", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel249: BinaryAssociation = BinaryAssociation(
    name="metamodel249",
    ends={
        Property(name="OclModel250", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements251: BinaryAssociation = BinaryAssociation(
    name="elements251",
    ends={
        Property(name="OclModelElement", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model252", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model253: BinaryAssociation = BinaryAssociation(
    name="model253",
    ends={
        Property(name="OclModel254", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
inferredType255: BinaryAssociation = BinaryAssociation(
    name="inferredType255",
    ends={
        Property(name="OCL_atlext_Type256", type=atlext_OCL_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_TypedElement", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
element257: BinaryAssociation = BinaryAssociation(
    name="element257",
    ends={
        Property(name="OutPatternElement258", type=atlext_OCL_ResolveTempResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_ResolveTempResolution", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_atlext_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Unit)
gen_atlext_ATL_Library_Unit = Generalization(general=Unit, specific=atlext_ATL_Library)
gen_atlext_ATL_Query_Unit = Generalization(general=Unit, specific=atlext_ATL_Query)
gen_atlext_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ModuleElement)
gen_atlext_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlext_ATL_Helper)
gen_atlext_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlext_ATL_Helper)
gen_atlext_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlext_ATL_ContextHelper)
gen_atlext_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlext_ATL_Rule)
gen_atlext_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_Module_Unit = Generalization(general=Unit, specific=atlext_ATL_Module)
gen_atlext_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlext_ATL_SimpleInPatternElement)
gen_atlext_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_OutPatternElement)
gen_atlext_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlext_ATL_MatchedRule)
gen_atlext_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_SimpleOutPatternElement)
gen_atlext_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlext_ATL_CalledRule)
gen_atlext_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_InPattern)
gen_atlext_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_OutPattern)
gen_atlext_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_DropPattern)
gen_atlext_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlext_ATL_ModuleCallable)
gen_atlext_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_PatternElement)
gen_atlext_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_InPatternElement)
gen_atlext_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlext_ATL_RuleWithPattern)
gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_ForEachOutPatternElement)
gen_atlext_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Binding)
gen_atlext_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlext_ATL_IfStat)
gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_RuleVariableDeclaration)
gen_atlext_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_LibraryRef)
gen_atlext_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ActionBlock)
gen_atlext_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Statement)
gen_atlext_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ExpressionStat)
gen_atlext_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlext_ATL_BindingStat)
gen_atlext_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ForStat)
gen_atlext_OCL_OclExpression_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_OclExpression_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_RealExp)
gen_atlext_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_IntegerExp)
gen_atlext_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_CollectionExp)
gen_atlext_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_BagExp)
gen_atlext_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_VariableExp)
gen_atlext_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_SuperExp)
gen_atlext_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PrimitiveExp)
gen_atlext_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_StringExp)
gen_atlext_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_BooleanExp)
gen_atlext_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_NumericExp)
gen_atlext_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_OrderedSetExp)
gen_atlext_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SequenceExp)
gen_atlext_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_SetExp)
gen_atlext_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_TupleExp)
gen_atlext_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_TuplePart)
gen_atlext_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_MapExp)
gen_atlext_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_MapElement)
gen_atlext_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_EnumLiteralExp)
gen_atlext_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclUndefinedExp)
gen_atlext_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PropertyCallExp)
gen_atlext_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_IfExp)
gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_NavigationOrAttributeCallExp)
gen_atlext_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_OperationCallExp)
gen_atlext_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_OperatorCallExp)
gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_CollectionOperationCallExp)
gen_atlext_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_LoopExp)
gen_atlext_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IterateExp)
gen_atlext_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IteratorExp)
gen_atlext_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_LetExp)
gen_atlext_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Parameter)
gen_atlext_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlext_OCL_CollectionType)
gen_atlext_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclType)
gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_VariableDeclaration_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Iterator)
gen_atlext_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_SetType)
gen_atlext_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlext_OCL_OclAnyType)
gen_atlext_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlext_OCL_TupleType)
gen_atlext_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_TupleTypeAttribute)
gen_atlext_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlext_OCL_Primitive)
gen_atlext_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_StringType)
gen_atlext_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_BooleanType)
gen_atlext_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_NumericType)
gen_atlext_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlext_OCL_IntegerType)
gen_atlext_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlext_OCL_RealType)
gen_atlext_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_BagType)
gen_atlext_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_OrderedSetType)
gen_atlext_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlext_OCL_SequenceType)
gen_atlext_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Operation)
gen_atlext_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlext_OCL_OclModelElement)
gen_atlext_OCL_MapType_OclType = Generalization(general=OclType, specific=atlext_OCL_MapType)
gen_atlext_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeatureDefinition)
gen_atlext_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclContextDefinition)
gen_atlext_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeature)
gen_atlext_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Attribute)
gen_atlext_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclModel)
gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo = Generalization(general=RuleResolutionInfo, specific=atlext_OCL_ResolveTempResolution)
gen_atlext_OCL_JavaBody_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_JavaBody)
gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody = Generalization(general=JavaBody, specific=atlext_OCL_GetAppliedStereotypesBody)
gen_atlext_OCL2_SelectByKind_CollectionOperationCallExp = Generalization(general=CollectionOperationCallExp, specific=atlext_OCL2_SelectByKind)

# Domain Model
domain_model = DomainModel(
    name="atlext",
    types={atlext_ATL_LocatedElement, ATL_atlext_EObject, StringToStringMap, atlext_ATL_Unit, LocatedElement, LibraryRef, atlext_ATL_Library, Unit, Helper, atlext_ATL_Query, OclExpression, atlext_ATL_ModuleElement, atlext_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, Library, OclFeatureDefinition, ATL_atlext_Type, atlext_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlext_ATL_ContextHelper, PropertyCallExp, atlext_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, atlext_ATL_StaticRule, atlext_ATL_Module, OclModel, ModuleElement, atlext_ATL_SimpleInPatternElement, atlext_ATL_OutPatternElement, RuleWithPattern, Binding, atlext_ATL_MatchedRule, atlext_ATL_LazyRule, ATL_RuleWithPattern, atlext_ATL_SimpleOutPatternElement, ATL_StaticRule, atlext_ATL_CalledRule, StaticRule, Parameter_, atlext_ATL_InPattern, InPatternElement, atlext_ATL_OutPattern, DropPattern, OutPatternElement, atlext_ATL_DropPattern, ATL_Rule, atlext_ATL_ModuleCallable, Callable, atlext_ATL_PatternElement, VariableDeclaration, atlext_ATL_Callable, atlext_ATL_InPatternElement, PatternElement, CallableParameter, atlext_ATL_RuleWithPattern, Rule, InPattern, atlext_ATL_ForEachOutPatternElement, Iterator, atlext_ATL_Binding, atlext_ATL_IfStat, RuleResolutionInfo, atlext_ATL_RuleVariableDeclaration, atlext_ATL_LibraryRef, atlext_ATL_ActionBlock, Statement, atlext_ATL_Statement, atlext_ATL_ExpressionStat, atlext_ATL_BindingStat, IfExp, CollectionExp, LetExp, atlext_ATL_ForStat, atlext_ATL_StringToStringMap, atlext_ATL_CallableParameter, atlext_ATL_RuleResolutionInfo, MatchedRule, atlext_OCL_OclExpression, ATL_LocatedElement, OCL_TypedElement, OclType, atlext_OCL_RealExp, NumericExp, atlext_OCL_IntegerExp, atlext_OCL_CollectionExp, atlext_OCL_BagExp, LoopExp, OperationCallExp, Operation, Attribute, OCL_atlext_Type, atlext_OCL_VariableExp, atlext_OCL_SuperExp, atlext_OCL_PrimitiveExp, atlext_OCL_StringExp, PrimitiveExp, atlext_OCL_BooleanExp, atlext_OCL_NumericExp, OCL_atlext_EObject, atlext_OCL_OrderedSetExp, atlext_OCL_SequenceExp, atlext_OCL_SetExp, atlext_OCL_TupleExp, TuplePart, atlext_OCL_TuplePart, TupleExp, atlext_OCL_MapExp, MapElement, atlext_OCL_MapElement, MapExp, atlext_OCL_EnumLiteralExp, atlext_OCL_OclUndefinedExp, atlext_OCL_PropertyCallExp, atlext_OCL_IfExp, ContextHelper, atlext_OCL_NavigationOrAttributeCallExp, atlext_OCL_OperationCallExp, ResolveTempResolution, atlext_OCL_OperatorCallExp, atlext_OCL_CollectionOperationCallExp, atlext_OCL_LoopExp, atlext_OCL_IterateExp, atlext_OCL_IteratorExp, atlext_OCL_LetExp, atlext_OCL_Parameter, atlext_OCL_CollectionType, atlext_OCL_OclType, OclContextDefinition, atlext_OCL_VariableDeclaration, IterateExp, VariableExp, atlext_OCL_Iterator, atlext_OCL_SetType, atlext_OCL_OclAnyType, atlext_OCL_TupleType, atlext_OCL_TupleTypeAttribute, TupleType, MapType, CollectionType, TupleTypeAttribute, atlext_OCL_Primitive, atlext_OCL_StringType, Primitive, atlext_OCL_BooleanType, atlext_OCL_NumericType, atlext_OCL_IntegerType, NumericType, atlext_OCL_RealType, atlext_OCL_BagType, atlext_OCL_OrderedSetType, atlext_OCL_SequenceType, atlext_OCL_Operation, atlext_OCL_OclModelElement, atlext_OCL_MapType, atlext_OCL_OclFeatureDefinition, OclFeature, atlext_OCL_OclContextDefinition, atlext_OCL_OclFeature, atlext_OCL_Attribute, atlext_OCL_OclModel, OclModelElement, atlext_OCL_TypedElement, atlext_OCL_ResolveTempResolution, atlext_OCL_JavaBody, atlext_OCL_GetAppliedStereotypesBody, JavaBody, atlext_OCL2_SelectByKind, CollectionOperationCallExp, RuleResolutionStatus},
    associations={problems0, annotations1, libraries3, helpers4, body5, query14, library15, definition17, inferredReturnType18, staticReturnType20, contextType23, polymorphicCalledBy25, outPattern26, actionBlock27, variables29, helpers6, inModels8, outModels9, elements12, children36, outPattern56, superRule37, sourceElement59, bindings61, model62, parameters39, elements40, filter41, rule43, dropPattern44, elements46, outPattern48, calledBy31, mapsTo50, callableParameters33, inPattern52, models54, inPattern35, writtenFeature74, leftType77, reverseBindings64, collection66, iterator68, value70, outPatternElement72, value92, condition95, thenStatements97, elseStatements100, resolvedBy80, rule82, unit84, rule85, statements87, expression88, source90, type119, ifExp3120, appliedProperty121, collection123, letExp125, iterator103, collection105, statements108, staticType111, paramDeclaration113, rule115, allInvolvedRules116, elements141, loopExp126, parentOperation127, initializedVariable128, ifExp2130, owningOperation132, ifExp1134, owningAttribute136, noCastedType138, referredVariable139, source153, usedFeature155, subtypeFeatures156, receptorType159, staticResolver162, tuplePart143, tuple144, elements145, map146, key148, value150, in_176, thenExpression179, dynamicResolvers164, arguments165, resolveTempResolvedBy167, body168, iterators170, result172, variable174, elementType197, definitions199, condition181, elseExpression183, type185, initExpression187, letExp189, baseExp191, variableExp192, staticType193, loopExpr195, attributes216, type218, oclExpression200, operation202, mapType2204, attribute205, mapType208, collectionTypes210, tupleTypeAttribute211, variableDeclaration213, initExpression239, type241, parameters243, tupleType220, model221, valueType224, keyType226, feature228, context_229, definition232, context_235, definition237, returnType245, body247, metamodel249, elements251, model253, inferredType255, element257},
    generalizations={gen_atlext_ATL_Unit_LocatedElement, gen_atlext_ATL_Library_Unit, gen_atlext_ATL_Query_Unit, gen_atlext_ATL_ModuleElement_LocatedElement, gen_atlext_ATL_Helper_ATL_ModuleElement, gen_atlext_ATL_Helper_ATL_Callable, gen_atlext_ATL_StaticHelper_ATL_Helper, gen_atlext_ATL_StaticHelper_ATL_ModuleCallable, gen_atlext_ATL_ContextHelper_Helper, gen_atlext_ATL_Rule_ModuleElement, gen_atlext_ATL_StaticRule_ATL_ModuleCallable, gen_atlext_ATL_Module_Unit, gen_atlext_ATL_SimpleInPatternElement_InPatternElement, gen_atlext_ATL_OutPatternElement_PatternElement, gen_atlext_ATL_MatchedRule_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_RuleWithPattern, gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlext_ATL_LazyRule_ATL_StaticRule, gen_atlext_ATL_CalledRule_StaticRule, gen_atlext_ATL_InPattern_LocatedElement, gen_atlext_ATL_OutPattern_LocatedElement, gen_atlext_ATL_DropPattern_LocatedElement, gen_atlext_ATL_StaticRule_ATL_Rule, gen_atlext_ATL_ModuleCallable_Callable, gen_atlext_ATL_PatternElement_VariableDeclaration, gen_atlext_ATL_InPatternElement_PatternElement, gen_atlext_ATL_RuleWithPattern_Rule, gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlext_ATL_Binding_LocatedElement, gen_atlext_ATL_IfStat_Statement, gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlext_ATL_LibraryRef_LocatedElement, gen_atlext_ATL_ActionBlock_LocatedElement, gen_atlext_ATL_Statement_LocatedElement, gen_atlext_ATL_ExpressionStat_Statement, gen_atlext_ATL_BindingStat_Statement, gen_atlext_ATL_ForStat_Statement, gen_atlext_OCL_OclExpression_ATL_LocatedElement, gen_atlext_OCL_OclExpression_OCL_TypedElement, gen_atlext_OCL_RealExp_NumericExp, gen_atlext_OCL_IntegerExp_NumericExp, gen_atlext_OCL_CollectionExp_OclExpression, gen_atlext_OCL_BagExp_CollectionExp, gen_atlext_OCL_VariableExp_OclExpression, gen_atlext_OCL_SuperExp_OclExpression, gen_atlext_OCL_PrimitiveExp_OclExpression, gen_atlext_OCL_StringExp_PrimitiveExp, gen_atlext_OCL_BooleanExp_PrimitiveExp, gen_atlext_OCL_NumericExp_PrimitiveExp, gen_atlext_OCL_OrderedSetExp_CollectionExp, gen_atlext_OCL_SequenceExp_CollectionExp, gen_atlext_OCL_SetExp_CollectionExp, gen_atlext_OCL_TupleExp_OclExpression, gen_atlext_OCL_TuplePart_VariableDeclaration, gen_atlext_OCL_MapExp_OclExpression, gen_atlext_OCL_MapElement_LocatedElement, gen_atlext_OCL_EnumLiteralExp_OclExpression, gen_atlext_OCL_OclUndefinedExp_OclExpression, gen_atlext_OCL_PropertyCallExp_OclExpression, gen_atlext_OCL_IfExp_OclExpression, gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlext_OCL_OperationCallExp_PropertyCallExp, gen_atlext_OCL_OperatorCallExp_OperationCallExp, gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlext_OCL_LoopExp_PropertyCallExp, gen_atlext_OCL_IterateExp_LoopExp, gen_atlext_OCL_IteratorExp_LoopExp, gen_atlext_OCL_LetExp_OclExpression, gen_atlext_OCL_Parameter_VariableDeclaration, gen_atlext_OCL_CollectionType_OclType, gen_atlext_OCL_OclType_OclExpression, gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement, gen_atlext_OCL_VariableDeclaration_OCL_TypedElement, gen_atlext_OCL_Iterator_VariableDeclaration, gen_atlext_OCL_SetType_CollectionType, gen_atlext_OCL_OclAnyType_OclType, gen_atlext_OCL_TupleType_OclType, gen_atlext_OCL_TupleTypeAttribute_LocatedElement, gen_atlext_OCL_Primitive_OclType, gen_atlext_OCL_StringType_Primitive, gen_atlext_OCL_BooleanType_Primitive, gen_atlext_OCL_NumericType_Primitive, gen_atlext_OCL_IntegerType_NumericType, gen_atlext_OCL_RealType_NumericType, gen_atlext_OCL_BagType_CollectionType, gen_atlext_OCL_OrderedSetType_CollectionType, gen_atlext_OCL_SequenceType_CollectionType, gen_atlext_OCL_Operation_OclFeature, gen_atlext_OCL_OclModelElement_OclType, gen_atlext_OCL_MapType_OclType, gen_atlext_OCL_OclFeatureDefinition_LocatedElement, gen_atlext_OCL_OclContextDefinition_LocatedElement, gen_atlext_OCL_OclFeature_LocatedElement, gen_atlext_OCL_Attribute_OclFeature, gen_atlext_OCL_OclModel_LocatedElement, gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo, gen_atlext_OCL_JavaBody_OclExpression, gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody, gen_atlext_OCL2_SelectByKind_CollectionOperationCallExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)