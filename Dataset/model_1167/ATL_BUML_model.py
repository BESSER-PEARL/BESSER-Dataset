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
top_ATL_Query = Class(name="top::ATL::Query")
OclExpression = Class(name="OclExpression")
top_ATL_Module = Class(name="top::ATL::Module")
OclModel = Class(name="OclModel")
top_ATL_LocatedElement = Class(name="top::ATL::LocatedElement", is_abstract=True)
top_ATL_Unit = Class(name="top::ATL::Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
top_ATL_Library = Class(name="top::ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
top_ATL_MatchedRule = Class(name="top::ATL::MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
top_ATL_LazyMatchedRule = Class(name="top::ATL::LazyMatchedRule")
ModuleElement = Class(name="ModuleElement")
top_ATL_ModuleElement = Class(name="top::ATL::ModuleElement", is_abstract=True)
Module = Class(name="Module")
top_ATL_Helper = Class(name="top::ATL::Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
top_ATL_Rule = Class(name="top::ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
top_ATL_DropPattern = Class(name="top::ATL::DropPattern")
top_ATL_PatternElement = Class(name="top::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
top_ATL_InPatternElement = Class(name="top::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
top_ATL_CalledRule = Class(name="top::ATL::CalledRule")
Parameter_ = Class(name="Parameter")
top_ATL_InPattern = Class(name="top::ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
top_ATL_OutPattern = Class(name="top::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
top_ATL_RuleVariableDeclaration = Class(name="top::ATL::RuleVariableDeclaration")
top_ATL_LibraryRef = Class(name="top::ATL::LibraryRef")
top_ATL_SimpleInPatternElement = Class(name="top::ATL::SimpleInPatternElement")
top_ATL_OutPatternElement = Class(name="top::ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
top_ATL_SimpleOutPatternElement = Class(name="top::ATL::SimpleOutPatternElement")
top_ATL_ForEachOutPatternElement = Class(name="top::ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
top_ATL_Binding = Class(name="top::ATL::Binding")
top_ATL_BindingStat = Class(name="top::ATL::BindingStat")
top_ATL_IfStat = Class(name="top::ATL::IfStat")
top_ATL_ActionBlock = Class(name="top::ATL::ActionBlock")
Statement = Class(name="Statement")
top_ATL_Statement = Class(name="top::ATL::Statement", is_abstract=True)
top_ATL_ExpressionStat = Class(name="top::ATL::ExpressionStat")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
top_ATL_ForStat = Class(name="top::ATL::ForStat")
top_OCL_OclExpression = Class(name="top::OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
top_OCL_NumericExp = Class(name="top::OCL::NumericExp", is_abstract=True)
top_OCL_RealExp = Class(name="top::OCL::RealExp")
NumericExp = Class(name="NumericExp")
top_OCL_IntegerExp = Class(name="top::OCL::IntegerExp")
top_OCL_CollectionExp = Class(name="top::OCL::CollectionExp", is_abstract=True)
top_OCL_BagExp = Class(name="top::OCL::BagExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
top_OCL_VariableExp = Class(name="top::OCL::VariableExp")
top_OCL_SuperExp = Class(name="top::OCL::SuperExp")
top_OCL_PrimitiveExp = Class(name="top::OCL::PrimitiveExp", is_abstract=True)
top_OCL_StringExp = Class(name="top::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
top_OCL_BooleanExp = Class(name="top::OCL::BooleanExp")
top_OCL_EnumLiteralExp = Class(name="top::OCL::EnumLiteralExp")
top_OCL_OclUndefinedExp = Class(name="top::OCL::OclUndefinedExp")
top_OCL_PropertyCallExp = Class(name="top::OCL::PropertyCallExp", is_abstract=True)
top_OCL_OrderedSetExp = Class(name="top::OCL::OrderedSetExp")
top_OCL_SequenceExp = Class(name="top::OCL::SequenceExp")
top_OCL_SetExp = Class(name="top::OCL::SetExp")
top_OCL_TupleExp = Class(name="top::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
top_OCL_TuplePart = Class(name="top::OCL::TuplePart")
TupleExp = Class(name="TupleExp")
top_OCL_MapExp = Class(name="top::OCL::MapExp")
MapElement = Class(name="MapElement")
top_OCL_MapElement = Class(name="top::OCL::MapElement")
MapExp = Class(name="MapExp")
top_OCL_IteratorExp = Class(name="top::OCL::IteratorExp")
top_OCL_LetExp = Class(name="top::OCL::LetExp")
top_OCL_IfExp = Class(name="top::OCL::IfExp")
top_OCL_NavigationOrAttributeCallExp = Class(name="top::OCL::NavigationOrAttributeCallExp")
top_OCL_OperationCallExp = Class(name="top::OCL::OperationCallExp")
top_OCL_OperatorCallExp = Class(name="top::OCL::OperatorCallExp")
top_OCL_CollectionOperationCallExp = Class(name="top::OCL::CollectionOperationCallExp")
top_OCL_LoopExp = Class(name="top::OCL::LoopExp", is_abstract=True)
top_OCL_IterateExp = Class(name="top::OCL::IterateExp")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
top_OCL_Iterator = Class(name="top::OCL::Iterator")
top_OCL_Parameter = Class(name="top::OCL::Parameter")
top_OCL_CollectionType = Class(name="top::OCL::CollectionType")
top_OCL_VariableDeclaration = Class(name="top::OCL::VariableDeclaration")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
top_OCL_OclType = Class(name="top::OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
TupleType = Class(name="TupleType")
top_OCL_OclModelElement = Class(name="top::OCL::OclModelElement")
top_OCL_MapType = Class(name="top::OCL::MapType")
top_OCL_Primitive = Class(name="top::OCL::Primitive", is_abstract=True)
top_OCL_StringType = Class(name="top::OCL::StringType")
Primitive = Class(name="Primitive")
top_OCL_BooleanType = Class(name="top::OCL::BooleanType")
top_OCL_NumericType = Class(name="top::OCL::NumericType", is_abstract=True)
top_OCL_IntegerType = Class(name="top::OCL::IntegerType")
NumericType = Class(name="NumericType")
top_OCL_RealType = Class(name="top::OCL::RealType")
top_OCL_BagType = Class(name="top::OCL::BagType")
top_OCL_OrderedSetType = Class(name="top::OCL::OrderedSetType")
top_OCL_SequenceType = Class(name="top::OCL::SequenceType")
top_OCL_SetType = Class(name="top::OCL::SetType")
top_OCL_OclAnyType = Class(name="top::OCL::OclAnyType")
top_OCL_TupleType = Class(name="top::OCL::TupleType")
top_OCL_TupleTypeAttribute = Class(name="top::OCL::TupleTypeAttribute")
top_OCL_Operation = Class(name="top::OCL::Operation")
top_OCL_OclFeatureDefinition = Class(name="top::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
top_OCL_OclContextDefinition = Class(name="top::OCL::OclContextDefinition")
top_OCL_OclFeature = Class(name="top::OCL::OclFeature", is_abstract=True)
top_OCL_Attribute = Class(name="top::OCL::Attribute")
top_OCL_OclModel = Class(name="top::OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# top_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# top_ATL_Module class attributes and methods
top_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
top_ATL_Module.attributes={top_ATL_Module_isRefining}

# OclModel class attributes and methods

# top_ATL_LocatedElement class attributes and methods
top_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
top_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
top_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
top_ATL_LocatedElement.attributes={top_ATL_LocatedElement_commentsAfter, top_ATL_LocatedElement_commentsBefore, top_ATL_LocatedElement_location}

# top_ATL_Unit class attributes and methods
top_ATL_Unit_name: Property = Property(name="name", type=StringType)
top_ATL_Unit.attributes={top_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# top_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# top_ATL_MatchedRule class attributes and methods
top_ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
top_ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
top_ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
top_ATL_MatchedRule.attributes={top_ATL_MatchedRule_isAbstract, top_ATL_MatchedRule_isRefining, top_ATL_MatchedRule_isNoDefault}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# top_ATL_LazyMatchedRule class attributes and methods
top_ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
top_ATL_LazyMatchedRule.attributes={top_ATL_LazyMatchedRule_isUnique}

# ModuleElement class attributes and methods

# top_ATL_ModuleElement class attributes and methods

# Module class attributes and methods

# top_ATL_Helper class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# top_ATL_Rule class attributes and methods
top_ATL_Rule_name: Property = Property(name="name", type=StringType)
top_ATL_Rule.attributes={top_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# top_ATL_DropPattern class attributes and methods

# top_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# top_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# top_ATL_CalledRule class attributes and methods
top_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
top_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
top_ATL_CalledRule.attributes={top_ATL_CalledRule_isEntrypoint, top_ATL_CalledRule_isEndpoint}

# Parameter class attributes and methods

# top_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# top_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# top_ATL_RuleVariableDeclaration class attributes and methods

# top_ATL_LibraryRef class attributes and methods
top_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
top_ATL_LibraryRef.attributes={top_ATL_LibraryRef_name}

# top_ATL_SimpleInPatternElement class attributes and methods

# top_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# top_ATL_SimpleOutPatternElement class attributes and methods

# top_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# top_ATL_Binding class attributes and methods
top_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
top_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
top_ATL_Binding.attributes={top_ATL_Binding_isAssignment, top_ATL_Binding_propertyName}

# top_ATL_BindingStat class attributes and methods
top_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
top_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
top_ATL_BindingStat.attributes={top_ATL_BindingStat_isAssignment, top_ATL_BindingStat_propertyName}

# top_ATL_IfStat class attributes and methods

# top_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# top_ATL_Statement class attributes and methods

# top_ATL_ExpressionStat class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# top_ATL_ForStat class attributes and methods

# top_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# top_OCL_NumericExp class attributes and methods

# top_OCL_RealExp class attributes and methods
top_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
top_OCL_RealExp.attributes={top_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# top_OCL_IntegerExp class attributes and methods
top_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
top_OCL_IntegerExp.attributes={top_OCL_IntegerExp_integerSymbol}

# top_OCL_CollectionExp class attributes and methods

# top_OCL_BagExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# top_OCL_VariableExp class attributes and methods

# top_OCL_SuperExp class attributes and methods

# top_OCL_PrimitiveExp class attributes and methods

# top_OCL_StringExp class attributes and methods
top_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
top_OCL_StringExp.attributes={top_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# top_OCL_BooleanExp class attributes and methods
top_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
top_OCL_BooleanExp.attributes={top_OCL_BooleanExp_booleanSymbol}

# top_OCL_EnumLiteralExp class attributes and methods
top_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
top_OCL_EnumLiteralExp.attributes={top_OCL_EnumLiteralExp_name}

# top_OCL_OclUndefinedExp class attributes and methods

# top_OCL_PropertyCallExp class attributes and methods

# top_OCL_OrderedSetExp class attributes and methods

# top_OCL_SequenceExp class attributes and methods

# top_OCL_SetExp class attributes and methods

# top_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# top_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# top_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# top_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# top_OCL_IteratorExp class attributes and methods
top_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
top_OCL_IteratorExp.attributes={top_OCL_IteratorExp_name}

# top_OCL_LetExp class attributes and methods

# top_OCL_IfExp class attributes and methods

# top_OCL_NavigationOrAttributeCallExp class attributes and methods
top_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
top_OCL_NavigationOrAttributeCallExp.attributes={top_OCL_NavigationOrAttributeCallExp_name}

# top_OCL_OperationCallExp class attributes and methods
top_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
top_OCL_OperationCallExp.attributes={top_OCL_OperationCallExp_operationName}

# top_OCL_OperatorCallExp class attributes and methods

# top_OCL_CollectionOperationCallExp class attributes and methods

# top_OCL_LoopExp class attributes and methods

# top_OCL_IterateExp class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# top_OCL_Iterator class attributes and methods

# top_OCL_Parameter class attributes and methods

# top_OCL_CollectionType class attributes and methods

# top_OCL_VariableDeclaration class attributes and methods
top_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
top_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
top_OCL_VariableDeclaration.attributes={top_OCL_VariableDeclaration_varName, top_OCL_VariableDeclaration_id}

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# top_OCL_OclType class attributes and methods
top_OCL_OclType_name: Property = Property(name="name", type=StringType)
top_OCL_OclType.attributes={top_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# TupleType class attributes and methods

# top_OCL_OclModelElement class attributes and methods

# top_OCL_MapType class attributes and methods

# top_OCL_Primitive class attributes and methods

# top_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# top_OCL_BooleanType class attributes and methods

# top_OCL_NumericType class attributes and methods

# top_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# top_OCL_RealType class attributes and methods

# top_OCL_BagType class attributes and methods

# top_OCL_OrderedSetType class attributes and methods

# top_OCL_SequenceType class attributes and methods

# top_OCL_SetType class attributes and methods

# top_OCL_OclAnyType class attributes and methods

# top_OCL_TupleType class attributes and methods

# top_OCL_TupleTypeAttribute class attributes and methods
top_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
top_OCL_TupleTypeAttribute.attributes={top_OCL_TupleTypeAttribute_name}

# top_OCL_Operation class attributes and methods
top_OCL_Operation_name: Property = Property(name="name", type=StringType)
top_OCL_Operation.attributes={top_OCL_Operation_name}

# top_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# top_OCL_OclContextDefinition class attributes and methods

# top_OCL_OclFeature class attributes and methods

# top_OCL_Attribute class attributes and methods
top_OCL_Attribute_name: Property = Property(name="name", type=StringType)
top_OCL_Attribute.attributes={top_OCL_Attribute_name}

# top_OCL_OclModel class attributes and methods
top_OCL_OclModel_name: Property = Property(name="name", type=StringType)
top_OCL_OclModel.attributes={top_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="ATL2", type=top_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="OclExpression", type=top_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="ATL6", type=top_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper5", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels7: BinaryAssociation = BinaryAssociation(
    name="inModels7",
    ends={
        Property(name="OclModel", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels8: BinaryAssociation = BinaryAssociation(
    name="outModels8",
    ends={
        Property(name="OclModel10", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Module9", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="ATL", type=top_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="LibraryRef", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern26: BinaryAssociation = BinaryAssociation(
    name="inPattern26",
    ends={
        Property(name="ATL27", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children28: BinaryAssociation = BinaryAssociation(
    name="children28",
    ends={
        Property(name="ATL29", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
superRule30: BinaryAssociation = BinaryAssociation(
    name="superRule30",
    ends={
        Property(name="ATL32", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule31", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
elements11: BinaryAssociation = BinaryAssociation(
    name="elements11",
    ends={
        Property(name="ATL12", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ModuleElement", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module13: BinaryAssociation = BinaryAssociation(
    name="module13",
    ends={
        Property(name="ATL14", type=top_ATL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Module", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
query15: BinaryAssociation = BinaryAssociation(
    name="query15",
    ends={
        Property(name="ATL16", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Query", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library17: BinaryAssociation = BinaryAssociation(
    name="library17",
    ends={
        Property(name="ATL18", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="Library", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition19: BinaryAssociation = BinaryAssociation(
    name="definition19",
    ends={
        Property(name="OclFeatureDefinition", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPattern20: BinaryAssociation = BinaryAssociation(
    name="outPattern20",
    ends={
        Property(name="ATL21", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock22: BinaryAssociation = BinaryAssociation(
    name="actionBlock22",
    ends={
        Property(name="ATL23", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionBlock", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables24: BinaryAssociation = BinaryAssociation(
    name="variables24",
    ends={
        Property(name="ATL25", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="RuleVariableDeclaration", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements45: BinaryAssociation = BinaryAssociation(
    name="elements45",
    ends={
        Property(name="OutPatternElement", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="ATL46", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
outPattern47: BinaryAssociation = BinaryAssociation(
    name="outPattern47",
    ends={
        Property(name="ATL49", type=top_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern48", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo50: BinaryAssociation = BinaryAssociation(
    name="mapsTo50",
    ends={
        Property(name="ATL52", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement51", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern53: BinaryAssociation = BinaryAssociation(
    name="inPattern53",
    ends={
        Property(name="ATL55", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern54", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models56: BinaryAssociation = BinaryAssociation(
    name="models56",
    ends={
        Property(name="OclModel57", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
parameters33: BinaryAssociation = BinaryAssociation(
    name="parameters33",
    ends={
        Property(name="Parameter", type=top_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements34: BinaryAssociation = BinaryAssociation(
    name="elements34",
    ends={
        Property(name="ATL35", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule36: BinaryAssociation = BinaryAssociation(
    name="rule36",
    ends={
        Property(name="ATL38", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule37", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter39: BinaryAssociation = BinaryAssociation(
    name="filter39",
    ends={
        Property(name="OclExpression40", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule41: BinaryAssociation = BinaryAssociation(
    name="rule41",
    ends={
        Property(name="ATL42", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern43: BinaryAssociation = BinaryAssociation(
    name="dropPattern43",
    ends={
        Property(name="ATL44", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="DropPattern", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outPatternElement76: BinaryAssociation = BinaryAssociation(
    name="outPatternElement76",
    ends={
        Property(name="ATL78", type=top_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement77", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule79: BinaryAssociation = BinaryAssociation(
    name="rule79",
    ends={
        Property(name="ATL81", type=top_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule80", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit82: BinaryAssociation = BinaryAssociation(
    name="unit82",
    ends={
        Property(name="ATL83", type=top_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Unit", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
outPattern58: BinaryAssociation = BinaryAssociation(
    name="outPattern58",
    ends={
        Property(name="ATL60", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern59", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement61: BinaryAssociation = BinaryAssociation(
    name="sourceElement61",
    ends={
        Property(name="ATL63", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement62", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings64: BinaryAssociation = BinaryAssociation(
    name="bindings64",
    ends={
        Property(name="ATL65", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model66: BinaryAssociation = BinaryAssociation(
    name="model66",
    ends={
        Property(name="OclModel67", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings68: BinaryAssociation = BinaryAssociation(
    name="reverseBindings68",
    ends={
        Property(name="OclExpression69", type=top_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection70: BinaryAssociation = BinaryAssociation(
    name="collection70",
    ends={
        Property(name="OclExpression71", type=top_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator72: BinaryAssociation = BinaryAssociation(
    name="iterator72",
    ends={
        Property(name="Iterator", type=top_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForEachOutPatternElement73", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="OclExpression75", type=top_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source90: BinaryAssociation = BinaryAssociation(
    name="source90",
    ends={
        Property(name="OclExpression91", type=top_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="OclExpression94", type=top_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_BindingStat93", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule84: BinaryAssociation = BinaryAssociation(
    name="rule84",
    ends={
        Property(name="ATL86", type=top_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule85", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements87: BinaryAssociation = BinaryAssociation(
    name="statements87",
    ends={
        Property(name="Statement", type=top_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="OclExpression89", type=top_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExp3112: BinaryAssociation = BinaryAssociation(
    name="ifExp3112",
    ends={
        Property(name="OCL113", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty114: BinaryAssociation = BinaryAssociation(
    name="appliedProperty114",
    ends={
        Property(name="OCL115", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection116: BinaryAssociation = BinaryAssociation(
    name="collection116",
    ends={
        Property(name="OCL117", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp118: BinaryAssociation = BinaryAssociation(
    name="letExp118",
    ends={
        Property(name="OCL119", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp120: BinaryAssociation = BinaryAssociation(
    name="loopExp120",
    ends={
        Property(name="OCL121", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation122: BinaryAssociation = BinaryAssociation(
    name="parentOperation122",
    ends={
        Property(name="OCL123", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCallExp", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
condition95: BinaryAssociation = BinaryAssociation(
    name="condition95",
    ends={
        Property(name="OclExpression96", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements97: BinaryAssociation = BinaryAssociation(
    name="thenStatements97",
    ends={
        Property(name="Statement99", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat98", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements100: BinaryAssociation = BinaryAssociation(
    name="elseStatements100",
    ends={
        Property(name="Statement102", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat101", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator103: BinaryAssociation = BinaryAssociation(
    name="iterator103",
    ends={
        Property(name="Iterator104", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection105: BinaryAssociation = BinaryAssociation(
    name="collection105",
    ends={
        Property(name="OclExpression107", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat106", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements108: BinaryAssociation = BinaryAssociation(
    name="statements108",
    ends={
        Property(name="Statement110", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat109", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="OCL", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements139: BinaryAssociation = BinaryAssociation(
    name="elements139",
    ends={
        Property(name="OCL141", type=top_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression140", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedVariable124: BinaryAssociation = BinaryAssociation(
    name="initializedVariable124",
    ends={
        Property(name="OCL125", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2126: BinaryAssociation = BinaryAssociation(
    name="ifExp2126",
    ends={
        Property(name="OCL128", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp127", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation129: BinaryAssociation = BinaryAssociation(
    name="owningOperation129",
    ends={
        Property(name="OCL130", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1131: BinaryAssociation = BinaryAssociation(
    name="ifExp1131",
    ends={
        Property(name="OCL133", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp132", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute134: BinaryAssociation = BinaryAssociation(
    name="owningAttribute134",
    ends={
        Property(name="OCL135", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable136: BinaryAssociation = BinaryAssociation(
    name="referredVariable136",
    ends={
        Property(name="OCL138", type=top_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration137", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
value152: BinaryAssociation = BinaryAssociation(
    name="value152",
    ends={
        Property(name="OclExpression154", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_OCL_MapElement153", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source155: BinaryAssociation = BinaryAssociation(
    name="source155",
    ends={
        Property(name="OCL157", type=top_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression156", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuplePart142: BinaryAssociation = BinaryAssociation(
    name="tuplePart142",
    ends={
        Property(name="OCL143", type=top_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple144: BinaryAssociation = BinaryAssociation(
    name="tuple144",
    ends={
        Property(name="OCL145", type=top_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements146: BinaryAssociation = BinaryAssociation(
    name="elements146",
    ends={
        Property(name="OCL147", type=top_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map148: BinaryAssociation = BinaryAssociation(
    name="map148",
    ends={
        Property(name="OCL149", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key150: BinaryAssociation = BinaryAssociation(
    name="key150",
    ends={
        Property(name="OclExpression151", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable170: BinaryAssociation = BinaryAssociation(
    name="variable170",
    ends={
        Property(name="OCL172", type=top_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration171", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_173: BinaryAssociation = BinaryAssociation(
    name="in_173",
    ends={
        Property(name="OCL175", type=top_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression174", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments158: BinaryAssociation = BinaryAssociation(
    name="arguments158",
    ends={
        Property(name="OCL160", type=top_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression159", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body161: BinaryAssociation = BinaryAssociation(
    name="body161",
    ends={
        Property(name="OCL163", type=top_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression162", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators164: BinaryAssociation = BinaryAssociation(
    name="iterators164",
    ends={
        Property(name="OCL166", type=top_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator165", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result167: BinaryAssociation = BinaryAssociation(
    name="result167",
    ends={
        Property(name="OCL169", type=top_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration168", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp194: BinaryAssociation = BinaryAssociation(
    name="baseExp194",
    ends={
        Property(name="OCL195", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp196: BinaryAssociation = BinaryAssociation(
    name="variableExp196",
    ends={
        Property(name="OCL197", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr198: BinaryAssociation = BinaryAssociation(
    name="loopExpr198",
    ends={
        Property(name="OCL200", type=top_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp199", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation201: BinaryAssociation = BinaryAssociation(
    name="operation201",
    ends={
        Property(name="OCL203", type=top_OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation202", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
thenExpression176: BinaryAssociation = BinaryAssociation(
    name="thenExpression176",
    ends={
        Property(name="OCL178", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression177", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition179: BinaryAssociation = BinaryAssociation(
    name="condition179",
    ends={
        Property(name="OCL181", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression180", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression182: BinaryAssociation = BinaryAssociation(
    name="elseExpression182",
    ends={
        Property(name="OCL184", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression183", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="OCL187", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType186", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression188: BinaryAssociation = BinaryAssociation(
    name="initExpression188",
    ends={
        Property(name="OCL190", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression189", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp191: BinaryAssociation = BinaryAssociation(
    name="letExp191",
    ends={
        Property(name="OCL193", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp192", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes223: BinaryAssociation = BinaryAssociation(
    name="collectionTypes223",
    ends={
        Property(name="OCL224", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute225: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute225",
    ends={
        Property(name="OCL226", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration227: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration227",
    ends={
        Property(name="OCL229", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration228", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
elementType204: BinaryAssociation = BinaryAssociation(
    name="elementType204",
    ends={
        Property(name="OCL206", type=top_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType205", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions207: BinaryAssociation = BinaryAssociation(
    name="definitions207",
    ends={
        Property(name="OCL208", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression209: BinaryAssociation = BinaryAssociation(
    name="oclExpression209",
    ends={
        Property(name="OCL211", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression210", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation212: BinaryAssociation = BinaryAssociation(
    name="operation212",
    ends={
        Property(name="OCL214", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation213", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2215: BinaryAssociation = BinaryAssociation(
    name="mapType2215",
    ends={
        Property(name="OCL216", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute217: BinaryAssociation = BinaryAssociation(
    name="attribute217",
    ends={
        Property(name="OCL219", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute218", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType220: BinaryAssociation = BinaryAssociation(
    name="mapType220",
    ends={
        Property(name="OCL222", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType221", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
tupleType236: BinaryAssociation = BinaryAssociation(
    name="tupleType236",
    ends={
        Property(name="OCL237", type=top_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model238: BinaryAssociation = BinaryAssociation(
    name="model238",
    ends={
        Property(name="OCL240", type=top_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel239", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType241: BinaryAssociation = BinaryAssociation(
    name="valueType241",
    ends={
        Property(name="OCL243", type=top_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType242", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType244: BinaryAssociation = BinaryAssociation(
    name="keyType244",
    ends={
        Property(name="OCL246", type=top_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType245", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes230: BinaryAssociation = BinaryAssociation(
    name="attributes230",
    ends={
        Property(name="OCL232", type=top_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute231", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type233: BinaryAssociation = BinaryAssociation(
    name="type233",
    ends={
        Property(name="OCL235", type=top_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType234", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type264: BinaryAssociation = BinaryAssociation(
    name="type264",
    ends={
        Property(name="OCL266", type=top_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType265", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters267: BinaryAssociation = BinaryAssociation(
    name="parameters267",
    ends={
        Property(name="OCL269", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter268", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType270: BinaryAssociation = BinaryAssociation(
    name="returnType270",
    ends={
        Property(name="OCL272", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType271", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body273: BinaryAssociation = BinaryAssociation(
    name="body273",
    ends={
        Property(name="OCL275", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression274", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature247: BinaryAssociation = BinaryAssociation(
    name="feature247",
    ends={
        Property(name="OCL248", type=top_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_249: BinaryAssociation = BinaryAssociation(
    name="context_249",
    ends={
        Property(name="OCL251", type=top_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition250", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition252: BinaryAssociation = BinaryAssociation(
    name="definition252",
    ends={
        Property(name="OCL254", type=top_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition253", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_255: BinaryAssociation = BinaryAssociation(
    name="context_255",
    ends={
        Property(name="OCL257", type=top_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType256", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition258: BinaryAssociation = BinaryAssociation(
    name="definition258",
    ends={
        Property(name="OCL260", type=top_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition259", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression261: BinaryAssociation = BinaryAssociation(
    name="initExpression261",
    ends={
        Property(name="OCL263", type=top_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression262", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel276: BinaryAssociation = BinaryAssociation(
    name="metamodel276",
    ends={
        Property(name="OCL278", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel277", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements279: BinaryAssociation = BinaryAssociation(
    name="elements279",
    ends={
        Property(name="OCL280", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model281: BinaryAssociation = BinaryAssociation(
    name="model281",
    ends={
        Property(name="OCL283", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel282", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_top_ATL_Query_Unit = Generalization(general=Unit, specific=top_ATL_Query)
gen_top_ATL_Module_Unit = Generalization(general=Unit, specific=top_ATL_Module)
gen_top_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Unit)
gen_top_ATL_Library_Unit = Generalization(general=Unit, specific=top_ATL_Library)
gen_top_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=top_ATL_MatchedRule)
gen_top_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=top_ATL_LazyMatchedRule)
gen_top_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_ModuleElement)
gen_top_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=top_ATL_Helper)
gen_top_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=top_ATL_Rule)
gen_top_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_DropPattern)
gen_top_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_ATL_PatternElement)
gen_top_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=top_ATL_InPatternElement)
gen_top_ATL_CalledRule_Rule = Generalization(general=Rule, specific=top_ATL_CalledRule)
gen_top_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_InPattern)
gen_top_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_OutPattern)
gen_top_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_ATL_RuleVariableDeclaration)
gen_top_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_LibraryRef)
gen_top_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=top_ATL_SimpleInPatternElement)
gen_top_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=top_ATL_OutPatternElement)
gen_top_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=top_ATL_SimpleOutPatternElement)
gen_top_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=top_ATL_ForEachOutPatternElement)
gen_top_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Binding)
gen_top_ATL_BindingStat_Statement = Generalization(general=Statement, specific=top_ATL_BindingStat)
gen_top_ATL_IfStat_Statement = Generalization(general=Statement, specific=top_ATL_IfStat)
gen_top_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_ActionBlock)
gen_top_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Statement)
gen_top_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=top_ATL_ExpressionStat)
gen_top_ATL_ForStat_Statement = Generalization(general=Statement, specific=top_ATL_ForStat)
gen_top_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclExpression)
gen_top_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_NumericExp)
gen_top_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=top_OCL_RealExp)
gen_top_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=top_OCL_IntegerExp)
gen_top_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_CollectionExp)
gen_top_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_BagExp)
gen_top_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_VariableExp)
gen_top_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_SuperExp)
gen_top_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_PrimitiveExp)
gen_top_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_StringExp)
gen_top_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_BooleanExp)
gen_top_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_EnumLiteralExp)
gen_top_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_OclUndefinedExp)
gen_top_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_PropertyCallExp)
gen_top_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_OrderedSetExp)
gen_top_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_SequenceExp)
gen_top_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_SetExp)
gen_top_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_TupleExp)
gen_top_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_TuplePart)
gen_top_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_MapExp)
gen_top_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_MapElement)
gen_top_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=top_OCL_IteratorExp)
gen_top_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_LetExp)
gen_top_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_IfExp)
gen_top_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_NavigationOrAttributeCallExp)
gen_top_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_OperationCallExp)
gen_top_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=top_OCL_OperatorCallExp)
gen_top_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=top_OCL_CollectionOperationCallExp)
gen_top_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_LoopExp)
gen_top_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=top_OCL_IterateExp)
gen_top_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_Iterator)
gen_top_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_Parameter)
gen_top_OCL_CollectionType_OclType = Generalization(general=OclType, specific=top_OCL_CollectionType)
gen_top_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_VariableDeclaration)
gen_top_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=top_OCL_OclType)
gen_top_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=top_OCL_OclModelElement)
gen_top_OCL_MapType_OclType = Generalization(general=OclType, specific=top_OCL_MapType)
gen_top_OCL_Primitive_OclType = Generalization(general=OclType, specific=top_OCL_Primitive)
gen_top_OCL_StringType_Primitive = Generalization(general=Primitive, specific=top_OCL_StringType)
gen_top_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=top_OCL_BooleanType)
gen_top_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=top_OCL_NumericType)
gen_top_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=top_OCL_IntegerType)
gen_top_OCL_RealType_NumericType = Generalization(general=NumericType, specific=top_OCL_RealType)
gen_top_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_BagType)
gen_top_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_OrderedSetType)
gen_top_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_SequenceType)
gen_top_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_SetType)
gen_top_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=top_OCL_OclAnyType)
gen_top_OCL_TupleType_OclType = Generalization(general=OclType, specific=top_OCL_TupleType)
gen_top_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_TupleTypeAttribute)
gen_top_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=top_OCL_Operation)
gen_top_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclFeatureDefinition)
gen_top_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclContextDefinition)
gen_top_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclFeature)
gen_top_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=top_OCL_Attribute)
gen_top_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="top",
    types={top_ATL_Query, OclExpression, top_ATL_Module, OclModel, top_ATL_LocatedElement, top_ATL_Unit, LocatedElement, LibraryRef, top_ATL_Library, Unit, Helper, top_ATL_MatchedRule, Rule, InPattern, MatchedRule, top_ATL_LazyMatchedRule, ModuleElement, top_ATL_ModuleElement, Module, top_ATL_Helper, Query, Library, OclFeatureDefinition, top_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, top_ATL_DropPattern, top_ATL_PatternElement, VariableDeclaration, top_ATL_InPatternElement, PatternElement, top_ATL_CalledRule, Parameter_, top_ATL_InPattern, InPatternElement, top_ATL_OutPattern, DropPattern, OutPatternElement, top_ATL_RuleVariableDeclaration, top_ATL_LibraryRef, top_ATL_SimpleInPatternElement, top_ATL_OutPatternElement, Binding, top_ATL_SimpleOutPatternElement, top_ATL_ForEachOutPatternElement, Iterator, top_ATL_Binding, top_ATL_BindingStat, top_ATL_IfStat, top_ATL_ActionBlock, Statement, top_ATL_Statement, top_ATL_ExpressionStat, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, top_ATL_ForStat, top_OCL_OclExpression, OclType, top_OCL_NumericExp, top_OCL_RealExp, NumericExp, top_OCL_IntegerExp, top_OCL_CollectionExp, top_OCL_BagExp, Operation, Attribute, top_OCL_VariableExp, top_OCL_SuperExp, top_OCL_PrimitiveExp, top_OCL_StringExp, PrimitiveExp, top_OCL_BooleanExp, top_OCL_EnumLiteralExp, top_OCL_OclUndefinedExp, top_OCL_PropertyCallExp, top_OCL_OrderedSetExp, top_OCL_SequenceExp, top_OCL_SetExp, top_OCL_TupleExp, TuplePart, top_OCL_TuplePart, TupleExp, top_OCL_MapExp, MapElement, top_OCL_MapElement, MapExp, top_OCL_IteratorExp, top_OCL_LetExp, top_OCL_IfExp, top_OCL_NavigationOrAttributeCallExp, top_OCL_OperationCallExp, top_OCL_OperatorCallExp, top_OCL_CollectionOperationCallExp, top_OCL_LoopExp, top_OCL_IterateExp, IterateExp, VariableExp, top_OCL_Iterator, top_OCL_Parameter, top_OCL_CollectionType, top_OCL_VariableDeclaration, CollectionType, TupleTypeAttribute, top_OCL_OclType, OclContextDefinition, MapType, TupleType, top_OCL_OclModelElement, top_OCL_MapType, top_OCL_Primitive, top_OCL_StringType, Primitive, top_OCL_BooleanType, top_OCL_NumericType, top_OCL_IntegerType, NumericType, top_OCL_RealType, top_OCL_BagType, top_OCL_OrderedSetType, top_OCL_SequenceType, top_OCL_SetType, top_OCL_OclAnyType, top_OCL_TupleType, top_OCL_TupleTypeAttribute, top_OCL_Operation, top_OCL_OclFeatureDefinition, OclFeature, top_OCL_OclContextDefinition, top_OCL_OclFeature, top_OCL_Attribute, top_OCL_OclModel, OclModelElement},
    associations={helpers1, body3, helpers4, inModels7, outModels8, libraries0, inPattern26, children28, superRule30, elements11, module13, query15, library17, definition19, outPattern20, actionBlock22, variables24, elements45, outPattern47, mapsTo50, inPattern53, models56, parameters33, elements34, rule36, filter39, rule41, dropPattern43, outPatternElement76, rule79, unit82, outPattern58, sourceElement61, bindings64, model66, reverseBindings68, collection70, iterator72, value74, source90, value92, rule84, statements87, expression88, ifExp3112, appliedProperty114, collection116, letExp118, loopExp120, parentOperation122, condition95, thenStatements97, elseStatements100, iterator103, collection105, statements108, type111, elements139, initializedVariable124, ifExp2126, owningOperation129, ifExp1131, owningAttribute134, referredVariable136, value152, source155, tuplePart142, tuple144, elements146, map148, key150, variable170, in_173, arguments158, body161, iterators164, result167, baseExp194, variableExp196, loopExpr198, operation201, thenExpression176, condition179, elseExpression182, type185, initExpression188, letExp191, collectionTypes223, tupleTypeAttribute225, variableDeclaration227, elementType204, definitions207, oclExpression209, operation212, mapType2215, attribute217, mapType220, tupleType236, model238, valueType241, keyType244, attributes230, type233, type264, parameters267, returnType270, body273, feature247, context_249, definition252, context_255, definition258, initExpression261, metamodel276, elements279, model281},
    generalizations={gen_top_ATL_Query_Unit, gen_top_ATL_Module_Unit, gen_top_ATL_Unit_LocatedElement, gen_top_ATL_Library_Unit, gen_top_ATL_MatchedRule_Rule, gen_top_ATL_LazyMatchedRule_MatchedRule, gen_top_ATL_ModuleElement_LocatedElement, gen_top_ATL_Helper_ModuleElement, gen_top_ATL_Rule_ModuleElement, gen_top_ATL_DropPattern_LocatedElement, gen_top_ATL_PatternElement_VariableDeclaration, gen_top_ATL_InPatternElement_PatternElement, gen_top_ATL_CalledRule_Rule, gen_top_ATL_InPattern_LocatedElement, gen_top_ATL_OutPattern_LocatedElement, gen_top_ATL_RuleVariableDeclaration_VariableDeclaration, gen_top_ATL_LibraryRef_LocatedElement, gen_top_ATL_SimpleInPatternElement_InPatternElement, gen_top_ATL_OutPatternElement_PatternElement, gen_top_ATL_SimpleOutPatternElement_OutPatternElement, gen_top_ATL_ForEachOutPatternElement_OutPatternElement, gen_top_ATL_Binding_LocatedElement, gen_top_ATL_BindingStat_Statement, gen_top_ATL_IfStat_Statement, gen_top_ATL_ActionBlock_LocatedElement, gen_top_ATL_Statement_LocatedElement, gen_top_ATL_ExpressionStat_Statement, gen_top_ATL_ForStat_Statement, gen_top_OCL_OclExpression_LocatedElement, gen_top_OCL_NumericExp_PrimitiveExp, gen_top_OCL_RealExp_NumericExp, gen_top_OCL_IntegerExp_NumericExp, gen_top_OCL_CollectionExp_OclExpression, gen_top_OCL_BagExp_CollectionExp, gen_top_OCL_VariableExp_OclExpression, gen_top_OCL_SuperExp_OclExpression, gen_top_OCL_PrimitiveExp_OclExpression, gen_top_OCL_StringExp_PrimitiveExp, gen_top_OCL_BooleanExp_PrimitiveExp, gen_top_OCL_EnumLiteralExp_OclExpression, gen_top_OCL_OclUndefinedExp_OclExpression, gen_top_OCL_PropertyCallExp_OclExpression, gen_top_OCL_OrderedSetExp_CollectionExp, gen_top_OCL_SequenceExp_CollectionExp, gen_top_OCL_SetExp_CollectionExp, gen_top_OCL_TupleExp_OclExpression, gen_top_OCL_TuplePart_VariableDeclaration, gen_top_OCL_MapExp_OclExpression, gen_top_OCL_MapElement_LocatedElement, gen_top_OCL_IteratorExp_LoopExp, gen_top_OCL_LetExp_OclExpression, gen_top_OCL_IfExp_OclExpression, gen_top_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_top_OCL_OperationCallExp_PropertyCallExp, gen_top_OCL_OperatorCallExp_OperationCallExp, gen_top_OCL_CollectionOperationCallExp_OperationCallExp, gen_top_OCL_LoopExp_PropertyCallExp, gen_top_OCL_IterateExp_LoopExp, gen_top_OCL_Iterator_VariableDeclaration, gen_top_OCL_Parameter_VariableDeclaration, gen_top_OCL_CollectionType_OclType, gen_top_OCL_VariableDeclaration_LocatedElement, gen_top_OCL_OclType_OclExpression, gen_top_OCL_OclModelElement_OclType, gen_top_OCL_MapType_OclType, gen_top_OCL_Primitive_OclType, gen_top_OCL_StringType_Primitive, gen_top_OCL_BooleanType_Primitive, gen_top_OCL_NumericType_Primitive, gen_top_OCL_IntegerType_NumericType, gen_top_OCL_RealType_NumericType, gen_top_OCL_BagType_CollectionType, gen_top_OCL_OrderedSetType_CollectionType, gen_top_OCL_SequenceType_CollectionType, gen_top_OCL_SetType_CollectionType, gen_top_OCL_OclAnyType_OclType, gen_top_OCL_TupleType_OclType, gen_top_OCL_TupleTypeAttribute_LocatedElement, gen_top_OCL_Operation_OclFeature, gen_top_OCL_OclFeatureDefinition_LocatedElement, gen_top_OCL_OclContextDefinition_LocatedElement, gen_top_OCL_OclFeature_LocatedElement, gen_top_OCL_Attribute_OclFeature, gen_top_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)