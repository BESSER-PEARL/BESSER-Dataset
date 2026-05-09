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
atlext_ATL_LocatedElement = Class(name="atlext_ATL_LocatedElement", is_abstract=True)
StringToStringMap = Class(name="StringToStringMap")
atlext_ATL_Unit = Class(name="atlext_ATL_Unit")
LocatedElement = Class(name="LocatedElement")
Helper = Class(name="Helper")
atlext_ATL_Query = Class(name="atlext_ATL_Query")
OclExpression = Class(name="OclExpression")
atlext_ATL_Module = Class(name="atlext_ATL_Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
atlext_ATL_ModuleElement = Class(name="atlext_ATL_ModuleElement", is_abstract=True)
atlext_ATL_Helper = Class(name="atlext_ATL_Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL_ModuleElement")
ATL_Callable = Class(name="ATL_Callable")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlext_ATL_StaticHelper = Class(name="atlext_ATL_StaticHelper")
ATL_Helper = Class(name="ATL_Helper")
ATL_ModuleCallable = Class(name="ATL_ModuleCallable")
atlext_ATL_ContextHelper = Class(name="atlext_ATL_ContextHelper")
PropertyCallExp = Class(name="PropertyCallExp")
atlext_ATL_Rule = Class(name="atlext_ATL_Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
LibraryRef = Class(name="LibraryRef")
atlext_ATL_Library = Class(name="atlext_ATL_Library")
Unit = Class(name="Unit")
atlext_ATL_StaticRule = Class(name="atlext_ATL_StaticRule", is_abstract=True)
ATL_Rule = Class(name="ATL_Rule")
atlext_ATL_ModuleCallable = Class(name="atlext_ATL_ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
atlext_ATL_Callable = Class(name="atlext_ATL_Callable", is_abstract=True)
CallableParameter = Class(name="CallableParameter")
atlext_ATL_RuleWithPattern = Class(name="atlext_ATL_RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
RuleWithPattern = Class(name="RuleWithPattern")
atlext_ATL_MatchedRule = Class(name="atlext_ATL_MatchedRule")
atlext_ATL_LazyRule = Class(name="atlext_ATL_LazyRule")
ATL_RuleWithPattern = Class(name="ATL_RuleWithPattern")
ATL_StaticRule = Class(name="ATL_StaticRule")
atlext_ATL_CalledRule = Class(name="atlext_ATL_CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
atlext_ATL_InPattern = Class(name="atlext_ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
atlext_ATL_OutPattern = Class(name="atlext_ATL_OutPattern")
DropPattern = Class(name="DropPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlext_ATL_PatternElement = Class(name="atlext_ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlext_ATL_InPatternElement = Class(name="atlext_ATL_InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atlext_ATL_SimpleInPatternElement = Class(name="atlext_ATL_SimpleInPatternElement")
atlext_ATL_OutPatternElement = Class(name="atlext_ATL_OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atlext_ATL_SimpleOutPatternElement = Class(name="atlext_ATL_SimpleOutPatternElement")
atlext_ATL_ForEachOutPatternElement = Class(name="atlext_ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlext_ATL_Binding = Class(name="atlext_ATL_Binding")
RuleResolutionInfo = Class(name="RuleResolutionInfo")
OutPatternElement = Class(name="OutPatternElement")
atlext_ATL_DropPattern = Class(name="atlext_ATL_DropPattern")
atlext_ATL_LibraryRef = Class(name="atlext_ATL_LibraryRef")
atlext_ATL_ActionBlock = Class(name="atlext_ATL_ActionBlock")
Statement = Class(name="Statement")
atlext_ATL_Statement = Class(name="atlext_ATL_Statement", is_abstract=True)
atlext_ATL_ExpressionStat = Class(name="atlext_ATL_ExpressionStat")
atlext_ATL_BindingStat = Class(name="atlext_ATL_BindingStat")
atlext_ATL_IfStat = Class(name="atlext_ATL_IfStat")
atlext_ATL_ForStat = Class(name="atlext_ATL_ForStat")
atlext_ATL_StringToStringMap = Class(name="atlext_ATL_StringToStringMap")
atlext_ATL_RuleVariableDeclaration = Class(name="atlext_ATL_RuleVariableDeclaration")
atlext_ATL_CallableParameter = Class(name="atlext_ATL_CallableParameter")
atlext_ATL_RuleResolutionInfo = Class(name="atlext_ATL_RuleResolutionInfo")
MatchedRule = Class(name="MatchedRule")
atlext_OCL_OclExpression = Class(name="atlext_OCL_OclExpression", is_abstract=True)
ATL_LocatedElement = Class(name="ATL_LocatedElement")
OCL_TypedElement = Class(name="OCL_TypedElement")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
atlext_OCL_VariableExp = Class(name="atlext_OCL_VariableExp")
atlext_OCL_SuperExp = Class(name="atlext_OCL_SuperExp")
atlext_OCL_PrimitiveExp = Class(name="atlext_OCL_PrimitiveExp", is_abstract=True)
atlext_OCL_StringExp = Class(name="atlext_OCL_StringExp")
atlext_OCL_BooleanExp = Class(name="atlext_OCL_BooleanExp")
atlext_OCL_NumericExp = Class(name="atlext_OCL_NumericExp", is_abstract=True)
atlext_OCL_RealExp = Class(name="atlext_OCL_RealExp")
NumericExp = Class(name="NumericExp")
atlext_OCL_IntegerExp = Class(name="atlext_OCL_IntegerExp")
atlext_OCL_CollectionExp = Class(name="atlext_OCL_CollectionExp", is_abstract=True)
atlext_OCL_BagExp = Class(name="atlext_OCL_BagExp")
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
PrimitiveExp = Class(name="PrimitiveExp")
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
atlext_OCL_IfExp = Class(name="atlext_OCL_IfExp")
atlext_OCL_VariableDeclaration = Class(name="atlext_OCL_VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlext_OCL_Iterator = Class(name="atlext_OCL_Iterator")
atlext_OCL_Parameter = Class(name="atlext_OCL_Parameter")
atlext_OCL_CollectionType = Class(name="atlext_OCL_CollectionType")
atlext_OCL_OclType = Class(name="atlext_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
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
atlext_OCL_SetType = Class(name="atlext_OCL_SetType")
atlext_OCL_OclAnyType = Class(name="atlext_OCL_OclAnyType")
atlext_OCL_TupleType = Class(name="atlext_OCL_TupleType")
atlext_OCL_TupleTypeAttribute = Class(name="atlext_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
atlext_OCL_MapType = Class(name="atlext_OCL_MapType")
atlext_OCL_OclFeatureDefinition = Class(name="atlext_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlext_OCL_OclContextDefinition = Class(name="atlext_OCL_OclContextDefinition")
atlext_OCL_OclFeature = Class(name="atlext_OCL_OclFeature", is_abstract=True)
atlext_OCL_Attribute = Class(name="atlext_OCL_Attribute")
atlext_OCL_Operation = Class(name="atlext_OCL_Operation")
atlext_OCL_OclModelElement = Class(name="atlext_OCL_OclModelElement")
OclModelElement = Class(name="OclModelElement")
atlext_OCL_TypedElement = Class(name="atlext_OCL_TypedElement", is_abstract=True)
atlext_OCL_ResolveTempResolution = Class(name="atlext_OCL_ResolveTempResolution")
atlext_OCL_JavaBody = Class(name="atlext_OCL_JavaBody")
atlext_OCL_GetAppliedStereotypesBody = Class(name="atlext_OCL_GetAppliedStereotypesBody")
JavaBody = Class(name="JavaBody")
atlext_OCL_OclModel = Class(name="atlext_OCL_OclModel")

# atlext_ATL_LocatedElement class attributes and methods
atlext_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlext_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlext_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlext_ATL_LocatedElement_fileLocation: Property = Property(name="fileLocation", type=StringType)
atlext_ATL_LocatedElement_fileObject: Property = Property(name="fileObject", type=StringType)
atlext_ATL_LocatedElement.attributes={atlext_ATL_LocatedElement_fileLocation, atlext_ATL_LocatedElement_location, atlext_ATL_LocatedElement_fileObject, atlext_ATL_LocatedElement_commentsAfter, atlext_ATL_LocatedElement_commentsBefore}

# StringToStringMap class attributes and methods

# atlext_ATL_Unit class attributes and methods
atlext_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlext_ATL_Unit.attributes={atlext_ATL_Unit_name}

# LocatedElement class attributes and methods

# Helper class attributes and methods

# atlext_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# atlext_ATL_Module class attributes and methods
atlext_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_Module.attributes={atlext_ATL_Module_isRefining}

# OclModel class attributes and methods

# ModuleElement class attributes and methods

# atlext_ATL_ModuleElement class attributes and methods

# atlext_ATL_Helper class attributes and methods
atlext_ATL_Helper_hasContext: Property = Property(name="hasContext", type=BooleanType)
atlext_ATL_Helper_isAttribute: Property = Property(name="isAttribute", type=StringType)
atlext_ATL_Helper.attributes={atlext_ATL_Helper_hasContext, atlext_ATL_Helper_isAttribute}

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlext_ATL_StaticHelper class attributes and methods

# ATL_Helper class attributes and methods

# ATL_ModuleCallable class attributes and methods

# atlext_ATL_ContextHelper class attributes and methods

# PropertyCallExp class attributes and methods

# atlext_ATL_Rule class attributes and methods
atlext_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlext_ATL_Rule.attributes={atlext_ATL_Rule_name}

# OutPattern class attributes and methods

# LibraryRef class attributes and methods

# atlext_ATL_Library class attributes and methods

# Unit class attributes and methods

# atlext_ATL_StaticRule class attributes and methods

# ATL_Rule class attributes and methods

# atlext_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# atlext_ATL_Callable class attributes and methods

# CallableParameter class attributes and methods

# atlext_ATL_RuleWithPattern class attributes and methods
atlext_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlext_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlext_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlext_ATL_RuleWithPattern.attributes={atlext_ATL_RuleWithPattern_isRefining, atlext_ATL_RuleWithPattern_isAbstract, atlext_ATL_RuleWithPattern_isNoDefault}

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
atlext_ATL_CalledRule.attributes={atlext_ATL_CalledRule_isEndpoint, atlext_ATL_CalledRule_isEntrypoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# atlext_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlext_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlext_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlext_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atlext_ATL_SimpleInPatternElement class attributes and methods

# atlext_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atlext_ATL_SimpleOutPatternElement class attributes and methods

# atlext_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlext_ATL_Binding class attributes and methods
atlext_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlext_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlext_ATL_Binding.attributes={atlext_ATL_Binding_isAssignment, atlext_ATL_Binding_propertyName}

# RuleResolutionInfo class attributes and methods

# OutPatternElement class attributes and methods

# atlext_ATL_DropPattern class attributes and methods

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

# atlext_ATL_IfStat class attributes and methods

# atlext_ATL_ForStat class attributes and methods

# atlext_ATL_StringToStringMap class attributes and methods
atlext_ATL_StringToStringMap_key: Property = Property(name="key", type=StringType)
atlext_ATL_StringToStringMap_value: Property = Property(name="value", type=StringType)
atlext_ATL_StringToStringMap.attributes={atlext_ATL_StringToStringMap_key, atlext_ATL_StringToStringMap_value}

# atlext_ATL_RuleVariableDeclaration class attributes and methods

# atlext_ATL_CallableParameter class attributes and methods
atlext_ATL_CallableParameter_name: Property = Property(name="name", type=StringType)
atlext_ATL_CallableParameter.attributes={atlext_ATL_CallableParameter_name}

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

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# atlext_OCL_VariableExp class attributes and methods

# atlext_OCL_SuperExp class attributes and methods

# atlext_OCL_PrimitiveExp class attributes and methods

# atlext_OCL_StringExp class attributes and methods
atlext_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atlext_OCL_StringExp.attributes={atlext_OCL_StringExp_stringSymbol}

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

# atlext_OCL_CollectionExp class attributes and methods

# atlext_OCL_BagExp class attributes and methods

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

# PrimitiveExp class attributes and methods

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

# atlext_OCL_IfExp class attributes and methods

# atlext_OCL_VariableDeclaration class attributes and methods
atlext_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlext_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlext_OCL_VariableDeclaration.attributes={atlext_OCL_VariableDeclaration_varName, atlext_OCL_VariableDeclaration_id}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlext_OCL_Iterator class attributes and methods

# atlext_OCL_Parameter class attributes and methods

# atlext_OCL_CollectionType class attributes and methods

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

# atlext_OCL_BooleanType class attributes and methods

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

# atlext_OCL_MapType class attributes and methods

# atlext_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlext_OCL_OclContextDefinition class attributes and methods

# atlext_OCL_OclFeature class attributes and methods

# atlext_OCL_Attribute class attributes and methods
atlext_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlext_OCL_Attribute.attributes={atlext_OCL_Attribute_name}

# atlext_OCL_Operation class attributes and methods
atlext_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlext_OCL_Operation.attributes={atlext_OCL_Operation_name}

# atlext_OCL_OclModelElement class attributes and methods

# OclModelElement class attributes and methods

# atlext_OCL_TypedElement class attributes and methods

# atlext_OCL_ResolveTempResolution class attributes and methods

# atlext_OCL_JavaBody class attributes and methods

# atlext_OCL_GetAppliedStereotypesBody class attributes and methods

# JavaBody class attributes and methods

# atlext_OCL_OclModel class attributes and methods
atlext_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlext_OCL_OclModel.attributes={atlext_OCL_OclModel_name}

# Relationships
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="StringToStringMap", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers2: BinaryAssociation = BinaryAssociation(
    name="helpers2",
    ends={
        Property(name="Helper", type=atlext_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="OclExpression", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="Helper5", type=atlext_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels6: BinaryAssociation = BinaryAssociation(
    name="inModels6",
    ends={
        Property(name="OclModel", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels7: BinaryAssociation = BinaryAssociation(
    name="outModels7",
    ends={
        Property(name="OclModel9", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module8", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="ModuleElement", type=atlext_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Module11", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query12: BinaryAssociation = BinaryAssociation(
    name="query12",
    ends={
        Property(name="Query", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library13: BinaryAssociation = BinaryAssociation(
    name="library13",
    ends={
        Property(name="Library", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers14", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition15: BinaryAssociation = BinaryAssociation(
    name="definition15",
    ends={
        Property(name="OclFeatureDefinition", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
polymorphicCalledBy16: BinaryAssociation = BinaryAssociation(
    name="polymorphicCalledBy16",
    ends={
        Property(name="PropertyCallExp", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="dynamicResolvers", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern17: BinaryAssociation = BinaryAssociation(
    name="outPattern17",
    ends={
        Property(name="OutPattern", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
libraries1: BinaryAssociation = BinaryAssociation(
    name="libraries1",
    ends={
        Property(name="LibraryRef", type=atlext_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledBy22: BinaryAssociation = BinaryAssociation(
    name="calledBy22",
    ends={
        Property(name="PropertyCallExp23", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
callableParameters24: BinaryAssociation = BinaryAssociation(
    name="callableParameters24",
    ends={
        Property(name="CallableParameter", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable25", type=CallableParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern26: BinaryAssociation = BinaryAssociation(
    name="inPattern26",
    ends={
        Property(name="InPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children27: BinaryAssociation = BinaryAssociation(
    name="children27",
    ends={
        Property(name="RuleWithPattern", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
superRule28: BinaryAssociation = BinaryAssociation(
    name="superRule28",
    ends={
        Property(name="RuleWithPattern29", type=atlext_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="Parameter", type=atlext_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="InPatternElement", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter32: BinaryAssociation = BinaryAssociation(
    name="filter32",
    ends={
        Property(name="OclExpression33", type=atlext_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule34: BinaryAssociation = BinaryAssociation(
    name="rule34",
    ends={
        Property(name="Rule", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern35: BinaryAssociation = BinaryAssociation(
    name="dropPattern35",
    ends={
        Property(name="DropPattern", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern36", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock18: BinaryAssociation = BinaryAssociation(
    name="actionBlock18",
    ends={
        Property(name="ActionBlock", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule19", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables20: BinaryAssociation = BinaryAssociation(
    name="variables20",
    ends={
        Property(name="RuleVariableDeclaration", type=atlext_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule21", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapsTo41: BinaryAssociation = BinaryAssociation(
    name="mapsTo41",
    ends={
        Property(name="OutPatternElement42", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern43: BinaryAssociation = BinaryAssociation(
    name="inPattern43",
    ends={
        Property(name="InPattern44", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models45: BinaryAssociation = BinaryAssociation(
    name="models45",
    ends={
        Property(name="OclModel46", type=atlext_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern47: BinaryAssociation = BinaryAssociation(
    name="outPattern47",
    ends={
        Property(name="OutPattern49", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements48", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement50: BinaryAssociation = BinaryAssociation(
    name="sourceElement50",
    ends={
        Property(name="InPatternElement51", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings52: BinaryAssociation = BinaryAssociation(
    name="bindings52",
    ends={
        Property(name="Binding", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model53: BinaryAssociation = BinaryAssociation(
    name="model53",
    ends={
        Property(name="OclModel54", type=atlext_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings55: BinaryAssociation = BinaryAssociation(
    name="reverseBindings55",
    ends={
        Property(name="OclExpression56", type=atlext_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection57: BinaryAssociation = BinaryAssociation(
    name="collection57",
    ends={
        Property(name="OclExpression58", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator59: BinaryAssociation = BinaryAssociation(
    name="iterator59",
    ends={
        Property(name="Iterator", type=atlext_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForEachOutPatternElement60", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="OclExpression62", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement63: BinaryAssociation = BinaryAssociation(
    name="outPatternElement63",
    ends={
        Property(name="OutPatternElement64", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
resolvedBy65: BinaryAssociation = BinaryAssociation(
    name="resolvedBy65",
    ends={
        Property(name="RuleResolutionInfo", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding66", type=RuleResolutionInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements37: BinaryAssociation = BinaryAssociation(
    name="elements37",
    ends={
        Property(name="OutPatternElement", type=atlext_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern38", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern39: BinaryAssociation = BinaryAssociation(
    name="outPattern39",
    ends={
        Property(name="OutPattern40", type=atlext_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
unit69: BinaryAssociation = BinaryAssociation(
    name="unit69",
    ends={
        Property(name="Unit", type=atlext_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule70: BinaryAssociation = BinaryAssociation(
    name="rule70",
    ends={
        Property(name="Rule71", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements72: BinaryAssociation = BinaryAssociation(
    name="statements72",
    ends={
        Property(name="Statement", type=atlext_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression73: BinaryAssociation = BinaryAssociation(
    name="expression73",
    ends={
        Property(name="OclExpression74", type=atlext_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source75: BinaryAssociation = BinaryAssociation(
    name="source75",
    ends={
        Property(name="OclExpression76", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value77: BinaryAssociation = BinaryAssociation(
    name="value77",
    ends={
        Property(name="OclExpression79", type=atlext_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_BindingStat78", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition80: BinaryAssociation = BinaryAssociation(
    name="condition80",
    ends={
        Property(name="OclExpression81", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements82: BinaryAssociation = BinaryAssociation(
    name="thenStatements82",
    ends={
        Property(name="Statement84", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat83", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements85: BinaryAssociation = BinaryAssociation(
    name="elseStatements85",
    ends={
        Property(name="Statement87", type=atlext_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_IfStat86", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator88: BinaryAssociation = BinaryAssociation(
    name="iterator88",
    ends={
        Property(name="Iterator89", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection90: BinaryAssociation = BinaryAssociation(
    name="collection90",
    ends={
        Property(name="OclExpression92", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat91", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements93: BinaryAssociation = BinaryAssociation(
    name="statements93",
    ends={
        Property(name="Statement95", type=atlext_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ForStat94", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule67: BinaryAssociation = BinaryAssociation(
    name="rule67",
    ends={
        Property(name="Rule68", type=atlext_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
paramDeclaration96: BinaryAssociation = BinaryAssociation(
    name="paramDeclaration96",
    ends={
        Property(name="VariableDeclaration", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
rule97: BinaryAssociation = BinaryAssociation(
    name="rule97",
    ends={
        Property(name="MatchedRule", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
allInvolvedRules98: BinaryAssociation = BinaryAssociation(
    name="allInvolvedRules98",
    ends={
        Property(name="MatchedRule100", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo99", type=MatchedRule, multiplicity=Multiplicity(1, 9999))
    }
)
type101: BinaryAssociation = BinaryAssociation(
    name="type101",
    ends={
        Property(name="OclType", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3102: BinaryAssociation = BinaryAssociation(
    name="ifExp3102",
    ends={
        Property(name="IfExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty103: BinaryAssociation = BinaryAssociation(
    name="appliedProperty103",
    ends={
        Property(name="PropertyCallExp104", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection105: BinaryAssociation = BinaryAssociation(
    name="collection105",
    ends={
        Property(name="CollectionExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements106", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp107: BinaryAssociation = BinaryAssociation(
    name="letExp107",
    ends={
        Property(name="LetExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp108: BinaryAssociation = BinaryAssociation(
    name="loopExp108",
    ends={
        Property(name="LoopExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation109: BinaryAssociation = BinaryAssociation(
    name="parentOperation109",
    ends={
        Property(name="OperationCallExp", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable110: BinaryAssociation = BinaryAssociation(
    name="initializedVariable110",
    ends={
        Property(name="VariableDeclaration111", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2112: BinaryAssociation = BinaryAssociation(
    name="ifExp2112",
    ends={
        Property(name="IfExp113", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation114: BinaryAssociation = BinaryAssociation(
    name="owningOperation114",
    ends={
        Property(name="Operation", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body115", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1116: BinaryAssociation = BinaryAssociation(
    name="ifExp1116",
    ends={
        Property(name="IfExp117", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute118: BinaryAssociation = BinaryAssociation(
    name="owningAttribute118",
    ends={
        Property(name="Attribute", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression119", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable120: BinaryAssociation = BinaryAssociation(
    name="referredVariable120",
    ends={
        Property(name="VariableDeclaration121", type=atlext_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements122: BinaryAssociation = BinaryAssociation(
    name="elements122",
    ends={
        Property(name="OclExpression123", type=atlext_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart124: BinaryAssociation = BinaryAssociation(
    name="tuplePart124",
    ends={
        Property(name="TuplePart", type=atlext_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple125: BinaryAssociation = BinaryAssociation(
    name="tuple125",
    ends={
        Property(name="TupleExp", type=atlext_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements126: BinaryAssociation = BinaryAssociation(
    name="elements126",
    ends={
        Property(name="MapElement", type=atlext_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map127: BinaryAssociation = BinaryAssociation(
    name="map127",
    ends={
        Property(name="MapExp", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements128", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key129: BinaryAssociation = BinaryAssociation(
    name="key129",
    ends={
        Property(name="OclExpression130", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value131: BinaryAssociation = BinaryAssociation(
    name="value131",
    ends={
        Property(name="OclExpression133", type=atlext_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_MapElement132", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source134: BinaryAssociation = BinaryAssociation(
    name="source134",
    ends={
        Property(name="OclExpression135", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticResolver136: BinaryAssociation = BinaryAssociation(
    name="staticResolver136",
    ends={
        Property(name="Callable", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp", type=Callable, multiplicity=Multiplicity(1, 1))
    }
)
dynamicResolvers137: BinaryAssociation = BinaryAssociation(
    name="dynamicResolvers137",
    ends={
        Property(name="ContextHelper", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="polymorphicCalledBy", type=ContextHelper, multiplicity=Multiplicity(0, 9999))
    }
)
arguments138: BinaryAssociation = BinaryAssociation(
    name="arguments138",
    ends={
        Property(name="OclExpression139", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolveTempResolvedBy140: BinaryAssociation = BinaryAssociation(
    name="resolveTempResolvedBy140",
    ends={
        Property(name="ResolveTempResolution", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OperationCallExp", type=ResolveTempResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body141: BinaryAssociation = BinaryAssociation(
    name="body141",
    ends={
        Property(name="OclExpression142", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators143: BinaryAssociation = BinaryAssociation(
    name="iterators143",
    ends={
        Property(name="Iterator144", type=atlext_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result145: BinaryAssociation = BinaryAssociation(
    name="result145",
    ends={
        Property(name="VariableDeclaration146", type=atlext_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable147: BinaryAssociation = BinaryAssociation(
    name="variable147",
    ends={
        Property(name="VariableDeclaration148", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_149: BinaryAssociation = BinaryAssociation(
    name="in_149",
    ends={
        Property(name="OclExpression151", type=atlext_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp150", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression152: BinaryAssociation = BinaryAssociation(
    name="thenExpression152",
    ends={
        Property(name="OclExpression153", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition154: BinaryAssociation = BinaryAssociation(
    name="condition154",
    ends={
        Property(name="OclExpression155", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type158: BinaryAssociation = BinaryAssociation(
    name="type158",
    ends={
        Property(name="OclType159", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression160: BinaryAssociation = BinaryAssociation(
    name="initExpression160",
    ends={
        Property(name="OclExpression161", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp162: BinaryAssociation = BinaryAssociation(
    name="letExp162",
    ends={
        Property(name="LetExp163", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp164: BinaryAssociation = BinaryAssociation(
    name="baseExp164",
    ends={
        Property(name="IterateExp", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp165: BinaryAssociation = BinaryAssociation(
    name="variableExp165",
    ends={
        Property(name="VariableExp", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr166: BinaryAssociation = BinaryAssociation(
    name="loopExpr166",
    ends={
        Property(name="LoopExp167", type=atlext_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType168: BinaryAssociation = BinaryAssociation(
    name="elementType168",
    ends={
        Property(name="OclType169", type=atlext_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions170: BinaryAssociation = BinaryAssociation(
    name="definitions170",
    ends={
        Property(name="OclContextDefinition", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression171: BinaryAssociation = BinaryAssociation(
    name="oclExpression171",
    ends={
        Property(name="OclExpression172", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation173: BinaryAssociation = BinaryAssociation(
    name="operation173",
    ends={
        Property(name="Operation174", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2175: BinaryAssociation = BinaryAssociation(
    name="mapType2175",
    ends={
        Property(name="MapType", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute176: BinaryAssociation = BinaryAssociation(
    name="attribute176",
    ends={
        Property(name="Attribute178", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type177", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType179: BinaryAssociation = BinaryAssociation(
    name="mapType179",
    ends={
        Property(name="MapType180", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes181: BinaryAssociation = BinaryAssociation(
    name="collectionTypes181",
    ends={
        Property(name="CollectionType", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute182: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute182",
    ends={
        Property(name="TupleTypeAttribute", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type183", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
elseExpression156: BinaryAssociation = BinaryAssociation(
    name="elseExpression156",
    ends={
        Property(name="OclExpression157", type=atlext_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclaration184: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration184",
    ends={
        Property(name="VariableDeclaration186", type=atlext_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type185", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes187: BinaryAssociation = BinaryAssociation(
    name="attributes187",
    ends={
        Property(name="TupleTypeAttribute188", type=atlext_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type189: BinaryAssociation = BinaryAssociation(
    name="type189",
    ends={
        Property(name="OclType190", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType191: BinaryAssociation = BinaryAssociation(
    name="tupleType191",
    ends={
        Property(name="TupleType", type=atlext_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model192: BinaryAssociation = BinaryAssociation(
    name="model192",
    ends={
        Property(name="OclModel194", type=atlext_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements193", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType195: BinaryAssociation = BinaryAssociation(
    name="valueType195",
    ends={
        Property(name="OclType196", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType197: BinaryAssociation = BinaryAssociation(
    name="keyType197",
    ends={
        Property(name="OclType198", type=atlext_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature199: BinaryAssociation = BinaryAssociation(
    name="feature199",
    ends={
        Property(name="OclFeature", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_200: BinaryAssociation = BinaryAssociation(
    name="context_200",
    ends={
        Property(name="OclContextDefinition202", type=atlext_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition201", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition203: BinaryAssociation = BinaryAssociation(
    name="definition203",
    ends={
        Property(name="OclFeatureDefinition205", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_204", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_206: BinaryAssociation = BinaryAssociation(
    name="context_206",
    ends={
        Property(name="OclType207", type=atlext_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition208: BinaryAssociation = BinaryAssociation(
    name="definition208",
    ends={
        Property(name="OclFeatureDefinition209", type=atlext_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression210: BinaryAssociation = BinaryAssociation(
    name="initExpression210",
    ends={
        Property(name="OclExpression211", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type212: BinaryAssociation = BinaryAssociation(
    name="type212",
    ends={
        Property(name="OclType213", type=atlext_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters214: BinaryAssociation = BinaryAssociation(
    name="parameters214",
    ends={
        Property(name="Parameter215", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType216: BinaryAssociation = BinaryAssociation(
    name="returnType216",
    ends={
        Property(name="OclType217", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body218: BinaryAssociation = BinaryAssociation(
    name="body218",
    ends={
        Property(name="OclExpression219", type=atlext_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel220: BinaryAssociation = BinaryAssociation(
    name="metamodel220",
    ends={
        Property(name="OclModel221", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements222: BinaryAssociation = BinaryAssociation(
    name="elements222",
    ends={
        Property(name="OclModelElement", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model223", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model224: BinaryAssociation = BinaryAssociation(
    name="model224",
    ends={
        Property(name="OclModel225", type=atlext_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
element226: BinaryAssociation = BinaryAssociation(
    name="element226",
    ends={
        Property(name="OutPatternElement227", type=atlext_OCL_ResolveTempResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_ResolveTempResolution", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_atlext_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Unit)
gen_atlext_ATL_Query_Unit = Generalization(general=Unit, specific=atlext_ATL_Query)
gen_atlext_ATL_Module_Unit = Generalization(general=Unit, specific=atlext_ATL_Module)
gen_atlext_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ModuleElement)
gen_atlext_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlext_ATL_Helper)
gen_atlext_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlext_ATL_Helper)
gen_atlext_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticHelper)
gen_atlext_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlext_ATL_ContextHelper)
gen_atlext_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlext_ATL_Rule)
gen_atlext_ATL_Library_Unit = Generalization(general=Unit, specific=atlext_ATL_Library)
gen_atlext_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlext_ATL_StaticRule)
gen_atlext_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlext_ATL_ModuleCallable)
gen_atlext_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlext_ATL_RuleWithPattern)
gen_atlext_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlext_ATL_MatchedRule)
gen_atlext_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlext_ATL_LazyRule)
gen_atlext_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlext_ATL_CalledRule)
gen_atlext_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_InPattern)
gen_atlext_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_OutPattern)
gen_atlext_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_PatternElement)
gen_atlext_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_InPatternElement)
gen_atlext_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlext_ATL_SimpleInPatternElement)
gen_atlext_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlext_ATL_OutPatternElement)
gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_SimpleOutPatternElement)
gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlext_ATL_ForEachOutPatternElement)
gen_atlext_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Binding)
gen_atlext_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_DropPattern)
gen_atlext_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_LibraryRef)
gen_atlext_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_ActionBlock)
gen_atlext_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlext_ATL_Statement)
gen_atlext_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ExpressionStat)
gen_atlext_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlext_ATL_BindingStat)
gen_atlext_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlext_ATL_IfStat)
gen_atlext_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlext_ATL_ForStat)
gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_ATL_RuleVariableDeclaration)
gen_atlext_OCL_OclExpression_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_OclExpression_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_VariableExp)
gen_atlext_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_SuperExp)
gen_atlext_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_PrimitiveExp)
gen_atlext_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_BooleanExp)
gen_atlext_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_NumericExp)
gen_atlext_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_RealExp)
gen_atlext_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlext_OCL_IntegerExp)
gen_atlext_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_CollectionExp)
gen_atlext_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlext_OCL_BagExp)
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
gen_atlext_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlext_OCL_StringExp)
gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_NavigationOrAttributeCallExp)
gen_atlext_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_OperationCallExp)
gen_atlext_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_OperatorCallExp)
gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlext_OCL_CollectionOperationCallExp)
gen_atlext_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlext_OCL_LoopExp)
gen_atlext_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IterateExp)
gen_atlext_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlext_OCL_IteratorExp)
gen_atlext_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_LetExp)
gen_atlext_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_IfExp)
gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement = Generalization(general=ATL_LocatedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_VariableDeclaration_OCL_TypedElement = Generalization(general=OCL_TypedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Iterator)
gen_atlext_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlext_OCL_Parameter)
gen_atlext_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlext_OCL_CollectionType)
gen_atlext_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_OclType)
gen_atlext_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlext_OCL_Primitive)
gen_atlext_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_StringType)
gen_atlext_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlext_OCL_BooleanType)
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
gen_atlext_OCL_MapType_OclType = Generalization(general=OclType, specific=atlext_OCL_MapType)
gen_atlext_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeatureDefinition)
gen_atlext_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclContextDefinition)
gen_atlext_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclFeature)
gen_atlext_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Attribute)
gen_atlext_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlext_OCL_Operation)
gen_atlext_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlext_OCL_OclModelElement)
gen_atlext_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlext_OCL_OclModel)
gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo = Generalization(general=RuleResolutionInfo, specific=atlext_OCL_ResolveTempResolution)
gen_atlext_OCL_JavaBody_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_JavaBody)
gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody = Generalization(general=JavaBody, specific=atlext_OCL_GetAppliedStereotypesBody)

# Domain Model
domain_model = DomainModel(
    name="atlext",
    types={atlext_ATL_LocatedElement, StringToStringMap, atlext_ATL_Unit, LocatedElement, Helper, atlext_ATL_Query, OclExpression, atlext_ATL_Module, OclModel, ModuleElement, atlext_ATL_ModuleElement, atlext_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, Library, OclFeatureDefinition, atlext_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlext_ATL_ContextHelper, PropertyCallExp, atlext_ATL_Rule, OutPattern, LibraryRef, atlext_ATL_Library, Unit, atlext_ATL_StaticRule, ATL_Rule, atlext_ATL_ModuleCallable, Callable, atlext_ATL_Callable, CallableParameter, atlext_ATL_RuleWithPattern, Rule, InPattern, RuleWithPattern, atlext_ATL_MatchedRule, atlext_ATL_LazyRule, ATL_RuleWithPattern, ATL_StaticRule, atlext_ATL_CalledRule, StaticRule, Parameter_, atlext_ATL_InPattern, InPatternElement, atlext_ATL_OutPattern, DropPattern, ActionBlock, RuleVariableDeclaration, atlext_ATL_PatternElement, VariableDeclaration, atlext_ATL_InPatternElement, PatternElement, atlext_ATL_SimpleInPatternElement, atlext_ATL_OutPatternElement, Binding, atlext_ATL_SimpleOutPatternElement, atlext_ATL_ForEachOutPatternElement, Iterator, atlext_ATL_Binding, RuleResolutionInfo, OutPatternElement, atlext_ATL_DropPattern, atlext_ATL_LibraryRef, atlext_ATL_ActionBlock, Statement, atlext_ATL_Statement, atlext_ATL_ExpressionStat, atlext_ATL_BindingStat, atlext_ATL_IfStat, atlext_ATL_ForStat, atlext_ATL_StringToStringMap, atlext_ATL_RuleVariableDeclaration, atlext_ATL_CallableParameter, atlext_ATL_RuleResolutionInfo, MatchedRule, atlext_OCL_OclExpression, ATL_LocatedElement, OCL_TypedElement, OclType, IfExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, atlext_OCL_VariableExp, atlext_OCL_SuperExp, atlext_OCL_PrimitiveExp, atlext_OCL_StringExp, atlext_OCL_BooleanExp, atlext_OCL_NumericExp, atlext_OCL_RealExp, NumericExp, atlext_OCL_IntegerExp, atlext_OCL_CollectionExp, atlext_OCL_BagExp, atlext_OCL_OrderedSetExp, atlext_OCL_SequenceExp, atlext_OCL_SetExp, atlext_OCL_TupleExp, TuplePart, atlext_OCL_TuplePart, TupleExp, atlext_OCL_MapExp, MapElement, atlext_OCL_MapElement, MapExp, atlext_OCL_EnumLiteralExp, atlext_OCL_OclUndefinedExp, atlext_OCL_PropertyCallExp, PrimitiveExp, ContextHelper, atlext_OCL_NavigationOrAttributeCallExp, atlext_OCL_OperationCallExp, ResolveTempResolution, atlext_OCL_OperatorCallExp, atlext_OCL_CollectionOperationCallExp, atlext_OCL_LoopExp, atlext_OCL_IterateExp, atlext_OCL_IteratorExp, atlext_OCL_LetExp, atlext_OCL_IfExp, atlext_OCL_VariableDeclaration, IterateExp, VariableExp, atlext_OCL_Iterator, atlext_OCL_Parameter, atlext_OCL_CollectionType, atlext_OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, atlext_OCL_Primitive, atlext_OCL_StringType, Primitive, atlext_OCL_BooleanType, atlext_OCL_NumericType, atlext_OCL_IntegerType, NumericType, atlext_OCL_RealType, atlext_OCL_BagType, atlext_OCL_OrderedSetType, atlext_OCL_SequenceType, atlext_OCL_SetType, atlext_OCL_OclAnyType, atlext_OCL_TupleType, atlext_OCL_TupleTypeAttribute, TupleType, atlext_OCL_MapType, atlext_OCL_OclFeatureDefinition, OclFeature, atlext_OCL_OclContextDefinition, atlext_OCL_OclFeature, atlext_OCL_Attribute, atlext_OCL_Operation, atlext_OCL_OclModelElement, OclModelElement, atlext_OCL_TypedElement, atlext_OCL_ResolveTempResolution, atlext_OCL_JavaBody, atlext_OCL_GetAppliedStereotypesBody, JavaBody, atlext_OCL_OclModel},
    associations={annotations0, helpers2, body3, helpers4, inModels6, outModels7, elements10, query12, library13, definition15, polymorphicCalledBy16, outPattern17, libraries1, calledBy22, callableParameters24, inPattern26, children27, superRule28, parameters30, elements31, filter32, rule34, dropPattern35, actionBlock18, variables20, mapsTo41, inPattern43, models45, outPattern47, sourceElement50, bindings52, model53, reverseBindings55, collection57, iterator59, value61, outPatternElement63, resolvedBy65, elements37, outPattern39, unit69, rule70, statements72, expression73, source75, value77, condition80, thenStatements82, elseStatements85, iterator88, collection90, statements93, rule67, paramDeclaration96, rule97, allInvolvedRules98, type101, ifExp3102, appliedProperty103, collection105, letExp107, loopExp108, parentOperation109, initializedVariable110, ifExp2112, owningOperation114, ifExp1116, owningAttribute118, referredVariable120, elements122, tuplePart124, tuple125, elements126, map127, key129, value131, source134, staticResolver136, dynamicResolvers137, arguments138, resolveTempResolvedBy140, body141, iterators143, result145, variable147, in_149, thenExpression152, condition154, type158, initExpression160, letExp162, baseExp164, variableExp165, loopExpr166, elementType168, definitions170, oclExpression171, operation173, mapType2175, attribute176, mapType179, collectionTypes181, tupleTypeAttribute182, elseExpression156, variableDeclaration184, attributes187, type189, tupleType191, model192, valueType195, keyType197, feature199, context_200, definition203, context_206, definition208, initExpression210, type212, parameters214, returnType216, body218, metamodel220, elements222, model224, element226},
    generalizations={gen_atlext_ATL_Unit_LocatedElement, gen_atlext_ATL_Query_Unit, gen_atlext_ATL_Module_Unit, gen_atlext_ATL_ModuleElement_LocatedElement, gen_atlext_ATL_Helper_ATL_ModuleElement, gen_atlext_ATL_Helper_ATL_Callable, gen_atlext_ATL_StaticHelper_ATL_Helper, gen_atlext_ATL_StaticHelper_ATL_ModuleCallable, gen_atlext_ATL_ContextHelper_Helper, gen_atlext_ATL_Rule_ModuleElement, gen_atlext_ATL_Library_Unit, gen_atlext_ATL_StaticRule_ATL_ModuleCallable, gen_atlext_ATL_StaticRule_ATL_Rule, gen_atlext_ATL_ModuleCallable_Callable, gen_atlext_ATL_RuleWithPattern_Rule, gen_atlext_ATL_MatchedRule_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_RuleWithPattern, gen_atlext_ATL_LazyRule_ATL_StaticRule, gen_atlext_ATL_CalledRule_StaticRule, gen_atlext_ATL_InPattern_LocatedElement, gen_atlext_ATL_OutPattern_LocatedElement, gen_atlext_ATL_PatternElement_VariableDeclaration, gen_atlext_ATL_InPatternElement_PatternElement, gen_atlext_ATL_SimpleInPatternElement_InPatternElement, gen_atlext_ATL_OutPatternElement_PatternElement, gen_atlext_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlext_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlext_ATL_Binding_LocatedElement, gen_atlext_ATL_DropPattern_LocatedElement, gen_atlext_ATL_LibraryRef_LocatedElement, gen_atlext_ATL_ActionBlock_LocatedElement, gen_atlext_ATL_Statement_LocatedElement, gen_atlext_ATL_ExpressionStat_Statement, gen_atlext_ATL_BindingStat_Statement, gen_atlext_ATL_IfStat_Statement, gen_atlext_ATL_ForStat_Statement, gen_atlext_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlext_OCL_OclExpression_ATL_LocatedElement, gen_atlext_OCL_OclExpression_OCL_TypedElement, gen_atlext_OCL_VariableExp_OclExpression, gen_atlext_OCL_SuperExp_OclExpression, gen_atlext_OCL_PrimitiveExp_OclExpression, gen_atlext_OCL_BooleanExp_PrimitiveExp, gen_atlext_OCL_NumericExp_PrimitiveExp, gen_atlext_OCL_RealExp_NumericExp, gen_atlext_OCL_IntegerExp_NumericExp, gen_atlext_OCL_CollectionExp_OclExpression, gen_atlext_OCL_BagExp_CollectionExp, gen_atlext_OCL_OrderedSetExp_CollectionExp, gen_atlext_OCL_SequenceExp_CollectionExp, gen_atlext_OCL_SetExp_CollectionExp, gen_atlext_OCL_TupleExp_OclExpression, gen_atlext_OCL_TuplePart_VariableDeclaration, gen_atlext_OCL_MapExp_OclExpression, gen_atlext_OCL_MapElement_LocatedElement, gen_atlext_OCL_EnumLiteralExp_OclExpression, gen_atlext_OCL_OclUndefinedExp_OclExpression, gen_atlext_OCL_PropertyCallExp_OclExpression, gen_atlext_OCL_StringExp_PrimitiveExp, gen_atlext_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlext_OCL_OperationCallExp_PropertyCallExp, gen_atlext_OCL_OperatorCallExp_OperationCallExp, gen_atlext_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlext_OCL_LoopExp_PropertyCallExp, gen_atlext_OCL_IterateExp_LoopExp, gen_atlext_OCL_IteratorExp_LoopExp, gen_atlext_OCL_LetExp_OclExpression, gen_atlext_OCL_IfExp_OclExpression, gen_atlext_OCL_VariableDeclaration_ATL_LocatedElement, gen_atlext_OCL_VariableDeclaration_OCL_TypedElement, gen_atlext_OCL_Iterator_VariableDeclaration, gen_atlext_OCL_Parameter_VariableDeclaration, gen_atlext_OCL_CollectionType_OclType, gen_atlext_OCL_OclType_OclExpression, gen_atlext_OCL_Primitive_OclType, gen_atlext_OCL_StringType_Primitive, gen_atlext_OCL_BooleanType_Primitive, gen_atlext_OCL_NumericType_Primitive, gen_atlext_OCL_IntegerType_NumericType, gen_atlext_OCL_RealType_NumericType, gen_atlext_OCL_BagType_CollectionType, gen_atlext_OCL_OrderedSetType_CollectionType, gen_atlext_OCL_SequenceType_CollectionType, gen_atlext_OCL_SetType_CollectionType, gen_atlext_OCL_OclAnyType_OclType, gen_atlext_OCL_TupleType_OclType, gen_atlext_OCL_TupleTypeAttribute_LocatedElement, gen_atlext_OCL_MapType_OclType, gen_atlext_OCL_OclFeatureDefinition_LocatedElement, gen_atlext_OCL_OclContextDefinition_LocatedElement, gen_atlext_OCL_OclFeature_LocatedElement, gen_atlext_OCL_Attribute_OclFeature, gen_atlext_OCL_Operation_OclFeature, gen_atlext_OCL_OclModelElement_OclType, gen_atlext_OCL_OclModel_LocatedElement, gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo, gen_atlext_OCL_JavaBody_OclExpression, gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)