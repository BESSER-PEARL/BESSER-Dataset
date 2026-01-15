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
atlstatic_ATL_LocatedElement = Class(name="atlstatic::ATL::LocatedElement", is_abstract=True)
ModuleElement = Class(name="ModuleElement")
atlstatic_ATL_ModuleElement = Class(name="atlstatic::ATL::ModuleElement", is_abstract=True)
atlstatic_ATL_Helper = Class(name="atlstatic::ATL::Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL::ModuleElement")
ATL_Callable = Class(name="ATL::Callable")
Query = Class(name="Query")
Library = Class(name="Library")
atlstatic_ATL_Unit = Class(name="atlstatic::ATL::Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlstatic_ATL_Library = Class(name="atlstatic::ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
atlstatic_ATL_Query = Class(name="atlstatic::ATL::Query")
OclExpression = Class(name="OclExpression")
atlstatic_ATL_Module = Class(name="atlstatic::ATL::Module")
OclModel = Class(name="OclModel")
InPattern = Class(name="InPattern")
RuleWithPattern = Class(name="RuleWithPattern")
atlstatic_ATL_MatchedRule = Class(name="atlstatic::ATL::MatchedRule")
atlstatic_ATL_LazyRule = Class(name="atlstatic::ATL::LazyRule")
ATL_RuleWithPattern = Class(name="ATL::RuleWithPattern")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlstatic_ATL_StaticHelper = Class(name="atlstatic::ATL::StaticHelper")
ATL_Helper = Class(name="ATL::Helper")
ATL_ModuleCallable = Class(name="ATL::ModuleCallable")
atlstatic_ATL_ContextHelper = Class(name="atlstatic::ATL::ContextHelper")
atlstatic_ATL_Rule = Class(name="atlstatic::ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlstatic_ATL_StaticRule = Class(name="atlstatic::ATL::StaticRule", is_abstract=True)
ATL_Rule = Class(name="ATL::Rule")
atlstatic_ATL_ModuleCallable = Class(name="atlstatic::ATL::ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
atlstatic_ATL_Callable = Class(name="atlstatic::ATL::Callable", is_abstract=True)
atlstatic_ATL_RuleWithPattern = Class(name="atlstatic::ATL::RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
OutPatternElement = Class(name="OutPatternElement")
atlstatic_ATL_DropPattern = Class(name="atlstatic::ATL::DropPattern")
atlstatic_ATL_PatternElement = Class(name="atlstatic::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlstatic_ATL_InPatternElement = Class(name="atlstatic::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
ATL_StaticRule = Class(name="ATL::StaticRule")
atlstatic_ATL_CalledRule = Class(name="atlstatic::ATL::CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
atlstatic_ATL_InPattern = Class(name="atlstatic::ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
atlstatic_ATL_OutPattern = Class(name="atlstatic::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
atlstatic_ATL_Binding = Class(name="atlstatic::ATL::Binding")
atlstatic_ATL_RuleVariableDeclaration = Class(name="atlstatic::ATL::RuleVariableDeclaration")
atlstatic_ATL_SimpleInPatternElement = Class(name="atlstatic::ATL::SimpleInPatternElement")
atlstatic_ATL_OutPatternElement = Class(name="atlstatic::ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atlstatic_ATL_SimpleOutPatternElement = Class(name="atlstatic::ATL::SimpleOutPatternElement")
atlstatic_ATL_ForEachOutPatternElement = Class(name="atlstatic::ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlstatic_ATL_IfStat = Class(name="atlstatic::ATL::IfStat")
atlstatic_ATL_ForStat = Class(name="atlstatic::ATL::ForStat")
atlstatic_ATL_LibraryRef = Class(name="atlstatic::ATL::LibraryRef")
atlstatic_ATL_ActionBlock = Class(name="atlstatic::ATL::ActionBlock")
Statement = Class(name="Statement")
atlstatic_ATL_Statement = Class(name="atlstatic::ATL::Statement", is_abstract=True)
atlstatic_ATL_ExpressionStat = Class(name="atlstatic::ATL::ExpressionStat")
atlstatic_ATL_BindingStat = Class(name="atlstatic::ATL::BindingStat")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
atlstatic_OCL_OclExpression = Class(name="atlstatic::OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
atlstatic_OCL_BagExp = Class(name="atlstatic::OCL::BagExp")
atlstatic_OCL_OrderedSetExp = Class(name="atlstatic::OCL::OrderedSetExp")
atlstatic_OCL_SequenceExp = Class(name="atlstatic::OCL::SequenceExp")
atlstatic_OCL_SetExp = Class(name="atlstatic::OCL::SetExp")
atlstatic_OCL_TupleExp = Class(name="atlstatic::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
Attribute = Class(name="Attribute")
atlstatic_OCL_TuplePart = Class(name="atlstatic::OCL::TuplePart")
atlstatic_OCL_VariableExp = Class(name="atlstatic::OCL::VariableExp")
atlstatic_OCL_SuperExp = Class(name="atlstatic::OCL::SuperExp")
atlstatic_OCL_PrimitiveExp = Class(name="atlstatic::OCL::PrimitiveExp", is_abstract=True)
atlstatic_OCL_StringExp = Class(name="atlstatic::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atlstatic_OCL_BooleanExp = Class(name="atlstatic::OCL::BooleanExp")
atlstatic_OCL_NumericExp = Class(name="atlstatic::OCL::NumericExp", is_abstract=True)
atlstatic_OCL_RealExp = Class(name="atlstatic::OCL::RealExp")
NumericExp = Class(name="NumericExp")
atlstatic_OCL_IntegerExp = Class(name="atlstatic::OCL::IntegerExp")
atlstatic_OCL_CollectionExp = Class(name="atlstatic::OCL::CollectionExp", is_abstract=True)
atlstatic_OCL_OclUndefinedExp = Class(name="atlstatic::OCL::OclUndefinedExp")
atlstatic_OCL_PropertyCallExp = Class(name="atlstatic::OCL::PropertyCallExp", is_abstract=True)
atlstatic_OCL_NavigationOrAttributeCallExp = Class(name="atlstatic::OCL::NavigationOrAttributeCallExp")
atlstatic_OCL_OperationCallExp = Class(name="atlstatic::OCL::OperationCallExp")
TupleExp = Class(name="TupleExp")
atlstatic_OCL_MapExp = Class(name="atlstatic::OCL::MapExp")
MapElement = Class(name="MapElement")
atlstatic_OCL_MapElement = Class(name="atlstatic::OCL::MapElement")
MapExp = Class(name="MapExp")
atlstatic_OCL_EnumLiteralExp = Class(name="atlstatic::OCL::EnumLiteralExp")
atlstatic_OCL_IfExp = Class(name="atlstatic::OCL::IfExp")
atlstatic_OCL_OperatorCallExp = Class(name="atlstatic::OCL::OperatorCallExp")
atlstatic_OCL_CollectionOperationCallExp = Class(name="atlstatic::OCL::CollectionOperationCallExp")
atlstatic_OCL_LoopExp = Class(name="atlstatic::OCL::LoopExp", is_abstract=True)
atlstatic_OCL_IterateExp = Class(name="atlstatic::OCL::IterateExp")
atlstatic_OCL_IteratorExp = Class(name="atlstatic::OCL::IteratorExp")
atlstatic_OCL_LetExp = Class(name="atlstatic::OCL::LetExp")
atlstatic_OCL_Iterator = Class(name="atlstatic::OCL::Iterator")
atlstatic_OCL_Parameter = Class(name="atlstatic::OCL::Parameter")
atlstatic_OCL_CollectionType = Class(name="atlstatic::OCL::CollectionType")
atlstatic_OCL_OclType = Class(name="atlstatic::OCL::OclType")
atlstatic_OCL_VariableDeclaration = Class(name="atlstatic::OCL::VariableDeclaration")
IterateExp = Class(name="IterateExp")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
VariableExp = Class(name="VariableExp")
atlstatic_OCL_Primitive = Class(name="atlstatic::OCL::Primitive", is_abstract=True)
atlstatic_OCL_StringType = Class(name="atlstatic::OCL::StringType")
Primitive = Class(name="Primitive")
atlstatic_OCL_BooleanType = Class(name="atlstatic::OCL::BooleanType")
atlstatic_OCL_NumericType = Class(name="atlstatic::OCL::NumericType", is_abstract=True)
atlstatic_OCL_IntegerType = Class(name="atlstatic::OCL::IntegerType")
NumericType = Class(name="NumericType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
atlstatic_OCL_TupleTypeAttribute = Class(name="atlstatic::OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
atlstatic_OCL_RealType = Class(name="atlstatic::OCL::RealType")
atlstatic_OCL_BagType = Class(name="atlstatic::OCL::BagType")
atlstatic_OCL_OrderedSetType = Class(name="atlstatic::OCL::OrderedSetType")
atlstatic_OCL_SequenceType = Class(name="atlstatic::OCL::SequenceType")
atlstatic_OCL_SetType = Class(name="atlstatic::OCL::SetType")
atlstatic_OCL_OclAnyType = Class(name="atlstatic::OCL::OclAnyType")
atlstatic_OCL_TupleType = Class(name="atlstatic::OCL::TupleType")
OclFeature = Class(name="OclFeature")
atlstatic_OCL_OclContextDefinition = Class(name="atlstatic::OCL::OclContextDefinition")
atlstatic_OCL_OclFeature = Class(name="atlstatic::OCL::OclFeature", is_abstract=True)
atlstatic_OCL_OclModelElement = Class(name="atlstatic::OCL::OclModelElement")
atlstatic_OCL_MapType = Class(name="atlstatic::OCL::MapType")
atlstatic_OCL_OclFeatureDefinition = Class(name="atlstatic::OCL::OclFeatureDefinition")
atlstatic_OCL_OclModel = Class(name="atlstatic::OCL::OclModel")
atlstatic_OCL_Attribute = Class(name="atlstatic::OCL::Attribute")
atlstatic_OCL_Operation = Class(name="atlstatic::OCL::Operation")
OclModelElement = Class(name="OclModelElement")

# atlstatic_ATL_LocatedElement class attributes and methods
atlstatic_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlstatic_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlstatic_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlstatic_ATL_LocatedElement.attributes={atlstatic_ATL_LocatedElement_location, atlstatic_ATL_LocatedElement_commentsBefore, atlstatic_ATL_LocatedElement_commentsAfter}

# ModuleElement class attributes and methods

# atlstatic_ATL_ModuleElement class attributes and methods

# atlstatic_ATL_Helper class attributes and methods

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# atlstatic_ATL_Unit class attributes and methods
atlstatic_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Unit.attributes={atlstatic_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# atlstatic_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# atlstatic_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# atlstatic_ATL_Module class attributes and methods
atlstatic_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_Module.attributes={atlstatic_ATL_Module_isRefining}

# OclModel class attributes and methods

# InPattern class attributes and methods

# RuleWithPattern class attributes and methods

# atlstatic_ATL_MatchedRule class attributes and methods

# atlstatic_ATL_LazyRule class attributes and methods
atlstatic_ATL_LazyRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlstatic_ATL_LazyRule.attributes={atlstatic_ATL_LazyRule_isUnique}

# ATL_RuleWithPattern class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlstatic_ATL_StaticHelper class attributes and methods

# ATL_Helper class attributes and methods

# ATL_ModuleCallable class attributes and methods

# atlstatic_ATL_ContextHelper class attributes and methods

# atlstatic_ATL_Rule class attributes and methods
atlstatic_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Rule.attributes={atlstatic_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_StaticRule class attributes and methods

# ATL_Rule class attributes and methods

# atlstatic_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# atlstatic_ATL_Callable class attributes and methods

# atlstatic_ATL_RuleWithPattern class attributes and methods
atlstatic_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlstatic_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlstatic_ATL_RuleWithPattern.attributes={atlstatic_ATL_RuleWithPattern_isAbstract, atlstatic_ATL_RuleWithPattern_isRefining, atlstatic_ATL_RuleWithPattern_isNoDefault}

# Rule class attributes and methods

# OutPatternElement class attributes and methods

# atlstatic_ATL_DropPattern class attributes and methods

# atlstatic_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlstatic_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# ATL_StaticRule class attributes and methods

# atlstatic_ATL_CalledRule class attributes and methods
atlstatic_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlstatic_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlstatic_ATL_CalledRule.attributes={atlstatic_ATL_CalledRule_isEndpoint, atlstatic_ATL_CalledRule_isEntrypoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# atlstatic_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlstatic_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# atlstatic_ATL_Binding class attributes and methods
atlstatic_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_Binding.attributes={atlstatic_ATL_Binding_propertyName, atlstatic_ATL_Binding_isAssignment}

# atlstatic_ATL_RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_SimpleInPatternElement class attributes and methods

# atlstatic_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atlstatic_ATL_SimpleOutPatternElement class attributes and methods

# atlstatic_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlstatic_ATL_IfStat class attributes and methods

# atlstatic_ATL_ForStat class attributes and methods

# atlstatic_ATL_LibraryRef class attributes and methods
atlstatic_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_LibraryRef.attributes={atlstatic_ATL_LibraryRef_name}

# atlstatic_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atlstatic_ATL_Statement class attributes and methods

# atlstatic_ATL_ExpressionStat class attributes and methods

# atlstatic_ATL_BindingStat class attributes and methods
atlstatic_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_BindingStat.attributes={atlstatic_ATL_BindingStat_isAssignment, atlstatic_ATL_BindingStat_propertyName}

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# atlstatic_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# atlstatic_OCL_BagExp class attributes and methods

# atlstatic_OCL_OrderedSetExp class attributes and methods

# atlstatic_OCL_SequenceExp class attributes and methods

# atlstatic_OCL_SetExp class attributes and methods

# atlstatic_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# Attribute class attributes and methods

# atlstatic_OCL_TuplePart class attributes and methods

# atlstatic_OCL_VariableExp class attributes and methods

# atlstatic_OCL_SuperExp class attributes and methods

# atlstatic_OCL_PrimitiveExp class attributes and methods

# atlstatic_OCL_StringExp class attributes and methods
atlstatic_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atlstatic_OCL_StringExp.attributes={atlstatic_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# atlstatic_OCL_BooleanExp class attributes and methods
atlstatic_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
atlstatic_OCL_BooleanExp.attributes={atlstatic_OCL_BooleanExp_booleanSymbol}

# atlstatic_OCL_NumericExp class attributes and methods

# atlstatic_OCL_RealExp class attributes and methods
atlstatic_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
atlstatic_OCL_RealExp.attributes={atlstatic_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atlstatic_OCL_IntegerExp class attributes and methods
atlstatic_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlstatic_OCL_IntegerExp.attributes={atlstatic_OCL_IntegerExp_integerSymbol}

# atlstatic_OCL_CollectionExp class attributes and methods

# atlstatic_OCL_OclUndefinedExp class attributes and methods

# atlstatic_OCL_PropertyCallExp class attributes and methods

# atlstatic_OCL_NavigationOrAttributeCallExp class attributes and methods
atlstatic_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_NavigationOrAttributeCallExp.attributes={atlstatic_OCL_NavigationOrAttributeCallExp_name}

# atlstatic_OCL_OperationCallExp class attributes and methods
atlstatic_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlstatic_OCL_OperationCallExp.attributes={atlstatic_OCL_OperationCallExp_operationName}

# TupleExp class attributes and methods

# atlstatic_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlstatic_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# atlstatic_OCL_EnumLiteralExp class attributes and methods
atlstatic_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_EnumLiteralExp.attributes={atlstatic_OCL_EnumLiteralExp_name}

# atlstatic_OCL_IfExp class attributes and methods

# atlstatic_OCL_OperatorCallExp class attributes and methods

# atlstatic_OCL_CollectionOperationCallExp class attributes and methods

# atlstatic_OCL_LoopExp class attributes and methods

# atlstatic_OCL_IterateExp class attributes and methods

# atlstatic_OCL_IteratorExp class attributes and methods
atlstatic_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_IteratorExp.attributes={atlstatic_OCL_IteratorExp_name}

# atlstatic_OCL_LetExp class attributes and methods

# atlstatic_OCL_Iterator class attributes and methods

# atlstatic_OCL_Parameter class attributes and methods

# atlstatic_OCL_CollectionType class attributes and methods

# atlstatic_OCL_OclType class attributes and methods
atlstatic_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclType.attributes={atlstatic_OCL_OclType_name}

# atlstatic_OCL_VariableDeclaration class attributes and methods
atlstatic_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlstatic_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlstatic_OCL_VariableDeclaration.attributes={atlstatic_OCL_VariableDeclaration_varName, atlstatic_OCL_VariableDeclaration_id}

# IterateExp class attributes and methods

# TupleTypeAttribute class attributes and methods

# VariableExp class attributes and methods

# atlstatic_OCL_Primitive class attributes and methods

# atlstatic_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlstatic_OCL_BooleanType class attributes and methods

# atlstatic_OCL_NumericType class attributes and methods

# atlstatic_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# atlstatic_OCL_TupleTypeAttribute class attributes and methods
atlstatic_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_TupleTypeAttribute.attributes={atlstatic_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# atlstatic_OCL_RealType class attributes and methods

# atlstatic_OCL_BagType class attributes and methods

# atlstatic_OCL_OrderedSetType class attributes and methods

# atlstatic_OCL_SequenceType class attributes and methods

# atlstatic_OCL_SetType class attributes and methods

# atlstatic_OCL_OclAnyType class attributes and methods

# atlstatic_OCL_TupleType class attributes and methods

# OclFeature class attributes and methods

# atlstatic_OCL_OclContextDefinition class attributes and methods

# atlstatic_OCL_OclFeature class attributes and methods

# atlstatic_OCL_OclModelElement class attributes and methods

# atlstatic_OCL_MapType class attributes and methods

# atlstatic_OCL_OclFeatureDefinition class attributes and methods

# atlstatic_OCL_OclModel class attributes and methods
atlstatic_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclModel.attributes={atlstatic_OCL_OclModel_name}

# atlstatic_OCL_Attribute class attributes and methods
atlstatic_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Attribute.attributes={atlstatic_OCL_Attribute_name}

# atlstatic_OCL_Operation class attributes and methods
atlstatic_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Operation.attributes={atlstatic_OCL_Operation_name}

# OclModelElement class attributes and methods

# Relationships
outModels8: BinaryAssociation = BinaryAssociation(
    name="outModels8",
    ends={
        Property(name="OclModel10", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module9", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements11: BinaryAssociation = BinaryAssociation(
    name="elements11",
    ends={
        Property(name="ModuleElement", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module12", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query13: BinaryAssociation = BinaryAssociation(
    name="query13",
    ends={
        Property(name="ATL14", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Query", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library15: BinaryAssociation = BinaryAssociation(
    name="library15",
    ends={
        Property(name="ATL16", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Library", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="ATL", type=atlstatic_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="LibraryRef", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="ATL2", type=atlstatic_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="OclExpression", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="ATL6", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper5", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels7: BinaryAssociation = BinaryAssociation(
    name="inModels7",
    ends={
        Property(name="OclModel", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inPattern24: BinaryAssociation = BinaryAssociation(
    name="inPattern24",
    ends={
        Property(name="InPattern", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children25: BinaryAssociation = BinaryAssociation(
    name="children25",
    ends={
        Property(name="ATL26", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleWithPattern", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
superRule27: BinaryAssociation = BinaryAssociation(
    name="superRule27",
    ends={
        Property(name="ATL29", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleWithPattern28", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
definition17: BinaryAssociation = BinaryAssociation(
    name="definition17",
    ends={
        Property(name="OclFeatureDefinition", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPattern18: BinaryAssociation = BinaryAssociation(
    name="outPattern18",
    ends={
        Property(name="ATL19", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock20: BinaryAssociation = BinaryAssociation(
    name="actionBlock20",
    ends={
        Property(name="ATL21", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionBlock", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables22: BinaryAssociation = BinaryAssociation(
    name="variables22",
    ends={
        Property(name="ATL23", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleVariableDeclaration", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements39: BinaryAssociation = BinaryAssociation(
    name="elements39",
    ends={
        Property(name="ATL40", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern41: BinaryAssociation = BinaryAssociation(
    name="outPattern41",
    ends={
        Property(name="ATL43", type=atlstatic_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern42", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo44: BinaryAssociation = BinaryAssociation(
    name="mapsTo44",
    ends={
        Property(name="ATL46", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement45", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern47: BinaryAssociation = BinaryAssociation(
    name="inPattern47",
    ends={
        Property(name="ATL49", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern48", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="Parameter", type=atlstatic_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="ATL32", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter33: BinaryAssociation = BinaryAssociation(
    name="filter33",
    ends={
        Property(name="OclExpression34", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule35: BinaryAssociation = BinaryAssociation(
    name="rule35",
    ends={
        Property(name="ATL36", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern37: BinaryAssociation = BinaryAssociation(
    name="dropPattern37",
    ends={
        Property(name="ATL38", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="DropPattern", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value68: BinaryAssociation = BinaryAssociation(
    name="value68",
    ends={
        Property(name="OclExpression69", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement70: BinaryAssociation = BinaryAssociation(
    name="outPatternElement70",
    ends={
        Property(name="ATL72", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement71", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule73: BinaryAssociation = BinaryAssociation(
    name="rule73",
    ends={
        Property(name="ATL75", type=atlstatic_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule74", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
models50: BinaryAssociation = BinaryAssociation(
    name="models50",
    ends={
        Property(name="OclModel51", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern52: BinaryAssociation = BinaryAssociation(
    name="outPattern52",
    ends={
        Property(name="ATL54", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern53", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement55: BinaryAssociation = BinaryAssociation(
    name="sourceElement55",
    ends={
        Property(name="ATL57", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement56", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings58: BinaryAssociation = BinaryAssociation(
    name="bindings58",
    ends={
        Property(name="ATL59", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model60: BinaryAssociation = BinaryAssociation(
    name="model60",
    ends={
        Property(name="OclModel61", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings62: BinaryAssociation = BinaryAssociation(
    name="reverseBindings62",
    ends={
        Property(name="OclExpression63", type=atlstatic_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection64: BinaryAssociation = BinaryAssociation(
    name="collection64",
    ends={
        Property(name="OclExpression65", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator66: BinaryAssociation = BinaryAssociation(
    name="iterator66",
    ends={
        Property(name="Iterator", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement67", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value86: BinaryAssociation = BinaryAssociation(
    name="value86",
    ends={
        Property(name="OclExpression88", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat87", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition89: BinaryAssociation = BinaryAssociation(
    name="condition89",
    ends={
        Property(name="OclExpression90", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements91: BinaryAssociation = BinaryAssociation(
    name="thenStatements91",
    ends={
        Property(name="Statement93", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat92", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements94: BinaryAssociation = BinaryAssociation(
    name="elseStatements94",
    ends={
        Property(name="Statement96", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat95", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit76: BinaryAssociation = BinaryAssociation(
    name="unit76",
    ends={
        Property(name="ATL77", type=atlstatic_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Unit", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule78: BinaryAssociation = BinaryAssociation(
    name="rule78",
    ends={
        Property(name="ATL80", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule79", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements81: BinaryAssociation = BinaryAssociation(
    name="statements81",
    ends={
        Property(name="Statement", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="OclExpression83", type=atlstatic_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="OclExpression85", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopExp114: BinaryAssociation = BinaryAssociation(
    name="loopExp114",
    ends={
        Property(name="OCL115", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation116: BinaryAssociation = BinaryAssociation(
    name="parentOperation116",
    ends={
        Property(name="OCL117", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCallExp", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable118: BinaryAssociation = BinaryAssociation(
    name="initializedVariable118",
    ends={
        Property(name="OCL119", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2120: BinaryAssociation = BinaryAssociation(
    name="ifExp2120",
    ends={
        Property(name="OCL122", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp121", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation123: BinaryAssociation = BinaryAssociation(
    name="owningOperation123",
    ends={
        Property(name="OCL124", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1125: BinaryAssociation = BinaryAssociation(
    name="ifExp1125",
    ends={
        Property(name="OCL127", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp126", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
iterator97: BinaryAssociation = BinaryAssociation(
    name="iterator97",
    ends={
        Property(name="Iterator98", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection99: BinaryAssociation = BinaryAssociation(
    name="collection99",
    ends={
        Property(name="OclExpression101", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat100", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements102: BinaryAssociation = BinaryAssociation(
    name="statements102",
    ends={
        Property(name="Statement104", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat103", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="OCL", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3106: BinaryAssociation = BinaryAssociation(
    name="ifExp3106",
    ends={
        Property(name="OCL107", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty108: BinaryAssociation = BinaryAssociation(
    name="appliedProperty108",
    ends={
        Property(name="OCL109", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection110: BinaryAssociation = BinaryAssociation(
    name="collection110",
    ends={
        Property(name="OCL111", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp112: BinaryAssociation = BinaryAssociation(
    name="letExp112",
    ends={
        Property(name="OCL113", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
elements133: BinaryAssociation = BinaryAssociation(
    name="elements133",
    ends={
        Property(name="OCL135", type=atlstatic_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression134", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart136: BinaryAssociation = BinaryAssociation(
    name="tuplePart136",
    ends={
        Property(name="OCL137", type=atlstatic_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningAttribute128: BinaryAssociation = BinaryAssociation(
    name="owningAttribute128",
    ends={
        Property(name="OCL129", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable130: BinaryAssociation = BinaryAssociation(
    name="referredVariable130",
    ends={
        Property(name="OCL132", type=atlstatic_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration131", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
source149: BinaryAssociation = BinaryAssociation(
    name="source149",
    ends={
        Property(name="OCL151", type=atlstatic_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression150", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments152: BinaryAssociation = BinaryAssociation(
    name="arguments152",
    ends={
        Property(name="OCL154", type=atlstatic_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression153", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple138: BinaryAssociation = BinaryAssociation(
    name="tuple138",
    ends={
        Property(name="OCL139", type=atlstatic_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements140: BinaryAssociation = BinaryAssociation(
    name="elements140",
    ends={
        Property(name="OCL141", type=atlstatic_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map142: BinaryAssociation = BinaryAssociation(
    name="map142",
    ends={
        Property(name="OCL143", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key144: BinaryAssociation = BinaryAssociation(
    name="key144",
    ends={
        Property(name="OclExpression145", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value146: BinaryAssociation = BinaryAssociation(
    name="value146",
    ends={
        Property(name="OclExpression148", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement147", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable164: BinaryAssociation = BinaryAssociation(
    name="variable164",
    ends={
        Property(name="OCL166", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration165", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_167: BinaryAssociation = BinaryAssociation(
    name="in_167",
    ends={
        Property(name="OCL169", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression168", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression170: BinaryAssociation = BinaryAssociation(
    name="thenExpression170",
    ends={
        Property(name="OCL172", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression171", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition173: BinaryAssociation = BinaryAssociation(
    name="condition173",
    ends={
        Property(name="OCL175", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression174", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body155: BinaryAssociation = BinaryAssociation(
    name="body155",
    ends={
        Property(name="OCL157", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression156", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators158: BinaryAssociation = BinaryAssociation(
    name="iterators158",
    ends={
        Property(name="OCL160", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator159", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result161: BinaryAssociation = BinaryAssociation(
    name="result161",
    ends={
        Property(name="OCL163", type=atlstatic_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration162", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableExp190: BinaryAssociation = BinaryAssociation(
    name="variableExp190",
    ends={
        Property(name="OCL191", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr192: BinaryAssociation = BinaryAssociation(
    name="loopExpr192",
    ends={
        Property(name="OCL194", type=atlstatic_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp193", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType195: BinaryAssociation = BinaryAssociation(
    name="elementType195",
    ends={
        Property(name="OCL197", type=atlstatic_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType196", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression176: BinaryAssociation = BinaryAssociation(
    name="elseExpression176",
    ends={
        Property(name="OCL178", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression177", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="OCL181", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType180", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression182: BinaryAssociation = BinaryAssociation(
    name="initExpression182",
    ends={
        Property(name="OCL184", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression183", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp185: BinaryAssociation = BinaryAssociation(
    name="letExp185",
    ends={
        Property(name="OCL187", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp186", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp188: BinaryAssociation = BinaryAssociation(
    name="baseExp188",
    ends={
        Property(name="OCL189", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute216: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute216",
    ends={
        Property(name="OCL217", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration218: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration218",
    ends={
        Property(name="OCL220", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration219", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
definitions198: BinaryAssociation = BinaryAssociation(
    name="definitions198",
    ends={
        Property(name="OCL199", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression200: BinaryAssociation = BinaryAssociation(
    name="oclExpression200",
    ends={
        Property(name="OCL202", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression201", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation203: BinaryAssociation = BinaryAssociation(
    name="operation203",
    ends={
        Property(name="OCL205", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation204", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2206: BinaryAssociation = BinaryAssociation(
    name="mapType2206",
    ends={
        Property(name="OCL207", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute208: BinaryAssociation = BinaryAssociation(
    name="attribute208",
    ends={
        Property(name="OCL210", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute209", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType211: BinaryAssociation = BinaryAssociation(
    name="mapType211",
    ends={
        Property(name="OCL213", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType212", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes214: BinaryAssociation = BinaryAssociation(
    name="collectionTypes214",
    ends={
        Property(name="OCL215", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
attributes221: BinaryAssociation = BinaryAssociation(
    name="attributes221",
    ends={
        Property(name="OCL223", type=atlstatic_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute222", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type224: BinaryAssociation = BinaryAssociation(
    name="type224",
    ends={
        Property(name="OCL226", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType225", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature238: BinaryAssociation = BinaryAssociation(
    name="feature238",
    ends={
        Property(name="OCL239", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_240: BinaryAssociation = BinaryAssociation(
    name="context_240",
    ends={
        Property(name="OCL242", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition241", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition243: BinaryAssociation = BinaryAssociation(
    name="definition243",
    ends={
        Property(name="OCL245", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition244", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_246: BinaryAssociation = BinaryAssociation(
    name="context_246",
    ends={
        Property(name="OCL248", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType247", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType227: BinaryAssociation = BinaryAssociation(
    name="tupleType227",
    ends={
        Property(name="OCL228", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model229: BinaryAssociation = BinaryAssociation(
    name="model229",
    ends={
        Property(name="OCL231", type=atlstatic_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel230", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType232: BinaryAssociation = BinaryAssociation(
    name="valueType232",
    ends={
        Property(name="OCL234", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType233", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType235: BinaryAssociation = BinaryAssociation(
    name="keyType235",
    ends={
        Property(name="OCL237", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType236", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters258: BinaryAssociation = BinaryAssociation(
    name="parameters258",
    ends={
        Property(name="Parameter259", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType260: BinaryAssociation = BinaryAssociation(
    name="returnType260",
    ends={
        Property(name="OCL262", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType261", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body263: BinaryAssociation = BinaryAssociation(
    name="body263",
    ends={
        Property(name="OCL265", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression264", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition249: BinaryAssociation = BinaryAssociation(
    name="definition249",
    ends={
        Property(name="OCL251", type=atlstatic_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition250", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression252: BinaryAssociation = BinaryAssociation(
    name="initExpression252",
    ends={
        Property(name="OCL254", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression253", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type255: BinaryAssociation = BinaryAssociation(
    name="type255",
    ends={
        Property(name="OCL257", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType256", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel266: BinaryAssociation = BinaryAssociation(
    name="metamodel266",
    ends={
        Property(name="OCL268", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel267", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements269: BinaryAssociation = BinaryAssociation(
    name="elements269",
    ends={
        Property(name="OCL270", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model271: BinaryAssociation = BinaryAssociation(
    name="model271",
    ends={
        Property(name="OCL273", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel272", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_atlstatic_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ModuleElement)
gen_atlstatic_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Unit)
gen_atlstatic_ATL_Library_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Library)
gen_atlstatic_ATL_Query_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Query)
gen_atlstatic_ATL_Module_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Module)
gen_atlstatic_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlstatic_ATL_MatchedRule)
gen_atlstatic_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlstatic_ATL_LazyRule)
gen_atlstatic_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlstatic_ATL_StaticHelper)
gen_atlstatic_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlstatic_ATL_StaticHelper)
gen_atlstatic_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlstatic_ATL_ContextHelper)
gen_atlstatic_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Rule)
gen_atlstatic_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlstatic_ATL_StaticRule)
gen_atlstatic_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlstatic_ATL_StaticRule)
gen_atlstatic_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlstatic_ATL_ModuleCallable)
gen_atlstatic_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlstatic_ATL_RuleWithPattern)
gen_atlstatic_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_DropPattern)
gen_atlstatic_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_PatternElement)
gen_atlstatic_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_InPatternElement)
gen_atlstatic_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlstatic_ATL_LazyRule)
gen_atlstatic_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlstatic_ATL_CalledRule)
gen_atlstatic_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_InPattern)
gen_atlstatic_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_OutPattern)
gen_atlstatic_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Binding)
gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_RuleVariableDeclaration)
gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlstatic_ATL_SimpleInPatternElement)
gen_atlstatic_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_OutPatternElement)
gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_SimpleOutPatternElement)
gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_ForEachOutPatternElement)
gen_atlstatic_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_IfStat)
gen_atlstatic_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ForStat)
gen_atlstatic_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_LibraryRef)
gen_atlstatic_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ActionBlock)
gen_atlstatic_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Statement)
gen_atlstatic_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ExpressionStat)
gen_atlstatic_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_BindingStat)
gen_atlstatic_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclExpression)
gen_atlstatic_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_CollectionExp)
gen_atlstatic_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_BagExp)
gen_atlstatic_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_OrderedSetExp)
gen_atlstatic_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SequenceExp)
gen_atlstatic_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SetExp)
gen_atlstatic_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_TupleExp)
gen_atlstatic_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_VariableExp)
gen_atlstatic_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_SuperExp)
gen_atlstatic_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PrimitiveExp)
gen_atlstatic_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_StringExp)
gen_atlstatic_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_BooleanExp)
gen_atlstatic_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_NumericExp)
gen_atlstatic_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_RealExp)
gen_atlstatic_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_IntegerExp)
gen_atlstatic_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclUndefinedExp)
gen_atlstatic_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PropertyCallExp)
gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_NavigationOrAttributeCallExp)
gen_atlstatic_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_OperationCallExp)
gen_atlstatic_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_TuplePart)
gen_atlstatic_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_MapExp)
gen_atlstatic_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_MapElement)
gen_atlstatic_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_EnumLiteralExp)
gen_atlstatic_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_IfExp)
gen_atlstatic_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_OperatorCallExp)
gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_CollectionOperationCallExp)
gen_atlstatic_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_LoopExp)
gen_atlstatic_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IterateExp)
gen_atlstatic_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IteratorExp)
gen_atlstatic_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_LetExp)
gen_atlstatic_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Iterator)
gen_atlstatic_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Parameter)
gen_atlstatic_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_CollectionType)
gen_atlstatic_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclType)
gen_atlstatic_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_VariableDeclaration)
gen_atlstatic_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlstatic_OCL_Primitive)
gen_atlstatic_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_StringType)
gen_atlstatic_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_BooleanType)
gen_atlstatic_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_NumericType)
gen_atlstatic_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_IntegerType)
gen_atlstatic_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_TupleType)
gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_TupleTypeAttribute)
gen_atlstatic_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_RealType)
gen_atlstatic_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_BagType)
gen_atlstatic_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_OrderedSetType)
gen_atlstatic_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SequenceType)
gen_atlstatic_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SetType)
gen_atlstatic_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclAnyType)
gen_atlstatic_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclContextDefinition)
gen_atlstatic_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeature)
gen_atlstatic_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclModelElement)
gen_atlstatic_OCL_MapType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_MapType)
gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeatureDefinition)
gen_atlstatic_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclModel)
gen_atlstatic_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Attribute)
gen_atlstatic_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Operation)

# Domain Model
domain_model = DomainModel(
    name="atlstatic",
    types={atlstatic_ATL_LocatedElement, ModuleElement, atlstatic_ATL_ModuleElement, atlstatic_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, Library, atlstatic_ATL_Unit, LocatedElement, LibraryRef, atlstatic_ATL_Library, Unit, Helper, atlstatic_ATL_Query, OclExpression, atlstatic_ATL_Module, OclModel, InPattern, RuleWithPattern, atlstatic_ATL_MatchedRule, atlstatic_ATL_LazyRule, ATL_RuleWithPattern, OclFeatureDefinition, atlstatic_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlstatic_ATL_ContextHelper, atlstatic_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, atlstatic_ATL_StaticRule, ATL_Rule, atlstatic_ATL_ModuleCallable, Callable, atlstatic_ATL_Callable, atlstatic_ATL_RuleWithPattern, Rule, OutPatternElement, atlstatic_ATL_DropPattern, atlstatic_ATL_PatternElement, VariableDeclaration, atlstatic_ATL_InPatternElement, PatternElement, ATL_StaticRule, atlstatic_ATL_CalledRule, StaticRule, Parameter_, atlstatic_ATL_InPattern, InPatternElement, atlstatic_ATL_OutPattern, DropPattern, atlstatic_ATL_Binding, atlstatic_ATL_RuleVariableDeclaration, atlstatic_ATL_SimpleInPatternElement, atlstatic_ATL_OutPatternElement, Binding, atlstatic_ATL_SimpleOutPatternElement, atlstatic_ATL_ForEachOutPatternElement, Iterator, atlstatic_ATL_IfStat, atlstatic_ATL_ForStat, atlstatic_ATL_LibraryRef, atlstatic_ATL_ActionBlock, Statement, atlstatic_ATL_Statement, atlstatic_ATL_ExpressionStat, atlstatic_ATL_BindingStat, OperationCallExp, Operation, atlstatic_OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, atlstatic_OCL_BagExp, atlstatic_OCL_OrderedSetExp, atlstatic_OCL_SequenceExp, atlstatic_OCL_SetExp, atlstatic_OCL_TupleExp, TuplePart, Attribute, atlstatic_OCL_TuplePart, atlstatic_OCL_VariableExp, atlstatic_OCL_SuperExp, atlstatic_OCL_PrimitiveExp, atlstatic_OCL_StringExp, PrimitiveExp, atlstatic_OCL_BooleanExp, atlstatic_OCL_NumericExp, atlstatic_OCL_RealExp, NumericExp, atlstatic_OCL_IntegerExp, atlstatic_OCL_CollectionExp, atlstatic_OCL_OclUndefinedExp, atlstatic_OCL_PropertyCallExp, atlstatic_OCL_NavigationOrAttributeCallExp, atlstatic_OCL_OperationCallExp, TupleExp, atlstatic_OCL_MapExp, MapElement, atlstatic_OCL_MapElement, MapExp, atlstatic_OCL_EnumLiteralExp, atlstatic_OCL_IfExp, atlstatic_OCL_OperatorCallExp, atlstatic_OCL_CollectionOperationCallExp, atlstatic_OCL_LoopExp, atlstatic_OCL_IterateExp, atlstatic_OCL_IteratorExp, atlstatic_OCL_LetExp, atlstatic_OCL_Iterator, atlstatic_OCL_Parameter, atlstatic_OCL_CollectionType, atlstatic_OCL_OclType, atlstatic_OCL_VariableDeclaration, IterateExp, TupleTypeAttribute, VariableExp, atlstatic_OCL_Primitive, atlstatic_OCL_StringType, Primitive, atlstatic_OCL_BooleanType, atlstatic_OCL_NumericType, atlstatic_OCL_IntegerType, NumericType, OclContextDefinition, MapType, CollectionType, atlstatic_OCL_TupleTypeAttribute, TupleType, atlstatic_OCL_RealType, atlstatic_OCL_BagType, atlstatic_OCL_OrderedSetType, atlstatic_OCL_SequenceType, atlstatic_OCL_SetType, atlstatic_OCL_OclAnyType, atlstatic_OCL_TupleType, OclFeature, atlstatic_OCL_OclContextDefinition, atlstatic_OCL_OclFeature, atlstatic_OCL_OclModelElement, atlstatic_OCL_MapType, atlstatic_OCL_OclFeatureDefinition, atlstatic_OCL_OclModel, atlstatic_OCL_Attribute, atlstatic_OCL_Operation, OclModelElement},
    associations={outModels8, elements11, query13, library15, libraries0, helpers1, body3, helpers4, inModels7, inPattern24, children25, superRule27, definition17, outPattern18, actionBlock20, variables22, elements39, outPattern41, mapsTo44, inPattern47, parameters30, elements31, filter33, rule35, dropPattern37, value68, outPatternElement70, rule73, models50, outPattern52, sourceElement55, bindings58, model60, reverseBindings62, collection64, iterator66, value86, condition89, thenStatements91, elseStatements94, unit76, rule78, statements81, expression82, source84, loopExp114, parentOperation116, initializedVariable118, ifExp2120, owningOperation123, ifExp1125, iterator97, collection99, statements102, type105, ifExp3106, appliedProperty108, collection110, letExp112, elements133, tuplePart136, owningAttribute128, referredVariable130, source149, arguments152, tuple138, elements140, map142, key144, value146, variable164, in_167, thenExpression170, condition173, body155, iterators158, result161, variableExp190, loopExpr192, elementType195, elseExpression176, type179, initExpression182, letExp185, baseExp188, tupleTypeAttribute216, variableDeclaration218, definitions198, oclExpression200, operation203, mapType2206, attribute208, mapType211, collectionTypes214, attributes221, type224, feature238, context_240, definition243, context_246, tupleType227, model229, valueType232, keyType235, parameters258, returnType260, body263, definition249, initExpression252, type255, metamodel266, elements269, model271},
    generalizations={gen_atlstatic_ATL_ModuleElement_LocatedElement, gen_atlstatic_ATL_Helper_ATL_ModuleElement, gen_atlstatic_ATL_Helper_ATL_Callable, gen_atlstatic_ATL_Unit_LocatedElement, gen_atlstatic_ATL_Library_Unit, gen_atlstatic_ATL_Query_Unit, gen_atlstatic_ATL_Module_Unit, gen_atlstatic_ATL_MatchedRule_RuleWithPattern, gen_atlstatic_ATL_LazyRule_ATL_RuleWithPattern, gen_atlstatic_ATL_StaticHelper_ATL_Helper, gen_atlstatic_ATL_StaticHelper_ATL_ModuleCallable, gen_atlstatic_ATL_ContextHelper_Helper, gen_atlstatic_ATL_Rule_ModuleElement, gen_atlstatic_ATL_StaticRule_ATL_ModuleCallable, gen_atlstatic_ATL_StaticRule_ATL_Rule, gen_atlstatic_ATL_ModuleCallable_Callable, gen_atlstatic_ATL_RuleWithPattern_Rule, gen_atlstatic_ATL_DropPattern_LocatedElement, gen_atlstatic_ATL_PatternElement_VariableDeclaration, gen_atlstatic_ATL_InPatternElement_PatternElement, gen_atlstatic_ATL_LazyRule_ATL_StaticRule, gen_atlstatic_ATL_CalledRule_StaticRule, gen_atlstatic_ATL_InPattern_LocatedElement, gen_atlstatic_ATL_OutPattern_LocatedElement, gen_atlstatic_ATL_Binding_LocatedElement, gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement, gen_atlstatic_ATL_OutPatternElement_PatternElement, gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlstatic_ATL_IfStat_Statement, gen_atlstatic_ATL_ForStat_Statement, gen_atlstatic_ATL_LibraryRef_LocatedElement, gen_atlstatic_ATL_ActionBlock_LocatedElement, gen_atlstatic_ATL_Statement_LocatedElement, gen_atlstatic_ATL_ExpressionStat_Statement, gen_atlstatic_ATL_BindingStat_Statement, gen_atlstatic_OCL_OclExpression_LocatedElement, gen_atlstatic_OCL_CollectionExp_OclExpression, gen_atlstatic_OCL_BagExp_CollectionExp, gen_atlstatic_OCL_OrderedSetExp_CollectionExp, gen_atlstatic_OCL_SequenceExp_CollectionExp, gen_atlstatic_OCL_SetExp_CollectionExp, gen_atlstatic_OCL_TupleExp_OclExpression, gen_atlstatic_OCL_VariableExp_OclExpression, gen_atlstatic_OCL_SuperExp_OclExpression, gen_atlstatic_OCL_PrimitiveExp_OclExpression, gen_atlstatic_OCL_StringExp_PrimitiveExp, gen_atlstatic_OCL_BooleanExp_PrimitiveExp, gen_atlstatic_OCL_NumericExp_PrimitiveExp, gen_atlstatic_OCL_RealExp_NumericExp, gen_atlstatic_OCL_IntegerExp_NumericExp, gen_atlstatic_OCL_OclUndefinedExp_OclExpression, gen_atlstatic_OCL_PropertyCallExp_OclExpression, gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlstatic_OCL_OperationCallExp_PropertyCallExp, gen_atlstatic_OCL_TuplePart_VariableDeclaration, gen_atlstatic_OCL_MapExp_OclExpression, gen_atlstatic_OCL_MapElement_LocatedElement, gen_atlstatic_OCL_EnumLiteralExp_OclExpression, gen_atlstatic_OCL_IfExp_OclExpression, gen_atlstatic_OCL_OperatorCallExp_OperationCallExp, gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlstatic_OCL_LoopExp_PropertyCallExp, gen_atlstatic_OCL_IterateExp_LoopExp, gen_atlstatic_OCL_IteratorExp_LoopExp, gen_atlstatic_OCL_LetExp_OclExpression, gen_atlstatic_OCL_Iterator_VariableDeclaration, gen_atlstatic_OCL_Parameter_VariableDeclaration, gen_atlstatic_OCL_CollectionType_OclType, gen_atlstatic_OCL_OclType_OclExpression, gen_atlstatic_OCL_VariableDeclaration_LocatedElement, gen_atlstatic_OCL_Primitive_OclType, gen_atlstatic_OCL_StringType_Primitive, gen_atlstatic_OCL_BooleanType_Primitive, gen_atlstatic_OCL_NumericType_Primitive, gen_atlstatic_OCL_IntegerType_NumericType, gen_atlstatic_OCL_TupleType_OclType, gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement, gen_atlstatic_OCL_RealType_NumericType, gen_atlstatic_OCL_BagType_CollectionType, gen_atlstatic_OCL_OrderedSetType_CollectionType, gen_atlstatic_OCL_SequenceType_CollectionType, gen_atlstatic_OCL_SetType_CollectionType, gen_atlstatic_OCL_OclAnyType_OclType, gen_atlstatic_OCL_OclContextDefinition_LocatedElement, gen_atlstatic_OCL_OclFeature_LocatedElement, gen_atlstatic_OCL_OclModelElement_OclType, gen_atlstatic_OCL_MapType_OclType, gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement, gen_atlstatic_OCL_OclModel_LocatedElement, gen_atlstatic_OCL_Attribute_OclFeature, gen_atlstatic_OCL_Operation_OclFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)