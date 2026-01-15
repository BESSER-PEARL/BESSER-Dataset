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
atlstatic_ATL_Unit = Class(name="atlstatic::ATL::Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlstatic_ATL_Library = Class(name="atlstatic::ATL::Library")
Unit = Class(name="Unit")
atlstatic_ATL_ModuleElement = Class(name="atlstatic::ATL::ModuleElement", is_abstract=True)
atlstatic_ATL_Helper = Class(name="atlstatic::ATL::Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlstatic_ATL_Rule = Class(name="atlstatic::ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
Helper = Class(name="Helper")
atlstatic_ATL_MatchedRule = Class(name="atlstatic::ATL::MatchedRule")
Rule = Class(name="Rule")
atlstatic_ATL_Query = Class(name="atlstatic::ATL::Query")
InPattern = Class(name="InPattern")
OclExpression = Class(name="OclExpression")
MatchedRule = Class(name="MatchedRule")
atlstatic_ATL_Module = Class(name="atlstatic::ATL::Module")
OclModel = Class(name="OclModel")
atlstatic_ATL_LazyMatchedRule = Class(name="atlstatic::ATL::LazyMatchedRule")
ModuleElement = Class(name="ModuleElement")
atlstatic_ATL_InPattern = Class(name="atlstatic::ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
atlstatic_ATL_OutPattern = Class(name="atlstatic::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atlstatic_ATL_DropPattern = Class(name="atlstatic::ATL::DropPattern")
atlstatic_ATL_PatternElement = Class(name="atlstatic::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlstatic_ATL_InPatternElement = Class(name="atlstatic::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atlstatic_ATL_SimpleInPatternElement = Class(name="atlstatic::ATL::SimpleInPatternElement")
atlstatic_ATL_OutPatternElement = Class(name="atlstatic::ATL::OutPatternElement", is_abstract=True)
atlstatic_ATL_CalledRule = Class(name="atlstatic::ATL::CalledRule")
Parameter_ = Class(name="Parameter")
Binding = Class(name="Binding")
atlstatic_ATL_SimpleOutPatternElement = Class(name="atlstatic::ATL::SimpleOutPatternElement")
atlstatic_ATL_ForEachOutPatternElement = Class(name="atlstatic::ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlstatic_ATL_Binding = Class(name="atlstatic::ATL::Binding")
atlstatic_ATL_RuleVariableDeclaration = Class(name="atlstatic::ATL::RuleVariableDeclaration")
atlstatic_ATL_LibraryRef = Class(name="atlstatic::ATL::LibraryRef")
atlstatic_ATL_ActionBlock = Class(name="atlstatic::ATL::ActionBlock")
Statement = Class(name="Statement")
atlstatic_ATL_Statement = Class(name="atlstatic::ATL::Statement", is_abstract=True)
atlstatic_ATL_ExpressionStat = Class(name="atlstatic::ATL::ExpressionStat")
atlstatic_ATL_BindingStat = Class(name="atlstatic::ATL::BindingStat")
atlstatic_ATL_IfStat = Class(name="atlstatic::ATL::IfStat")
atlstatic_ATL_ForStat = Class(name="atlstatic::ATL::ForStat")
atlstatic_OCL_OclExpression = Class(name="atlstatic::OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
atlstatic_OCL_VariableExp = Class(name="atlstatic::OCL::VariableExp")
atlstatic_OCL_SuperExp = Class(name="atlstatic::OCL::SuperExp")
atlstatic_OCL_StringExp = Class(name="atlstatic::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atlstatic_OCL_BooleanExp = Class(name="atlstatic::OCL::BooleanExp")
atlstatic_OCL_NumericExp = Class(name="atlstatic::OCL::NumericExp", is_abstract=True)
atlstatic_OCL_RealExp = Class(name="atlstatic::OCL::RealExp")
NumericExp = Class(name="NumericExp")
atlstatic_OCL_IntegerExp = Class(name="atlstatic::OCL::IntegerExp")
atlstatic_OCL_CollectionExp = Class(name="atlstatic::OCL::CollectionExp", is_abstract=True)
atlstatic_OCL_BagExp = Class(name="atlstatic::OCL::BagExp")
atlstatic_OCL_OrderedSetExp = Class(name="atlstatic::OCL::OrderedSetExp")
atlstatic_OCL_SequenceExp = Class(name="atlstatic::OCL::SequenceExp")
atlstatic_OCL_SetExp = Class(name="atlstatic::OCL::SetExp")
atlstatic_OCL_TupleExp = Class(name="atlstatic::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
atlstatic_OCL_TuplePart = Class(name="atlstatic::OCL::TuplePart")
TupleExp = Class(name="TupleExp")
atlstatic_OCL_MapExp = Class(name="atlstatic::OCL::MapExp")
MapElement = Class(name="MapElement")
atlstatic_OCL_MapElement = Class(name="atlstatic::OCL::MapElement")
atlstatic_OCL_PrimitiveExp = Class(name="atlstatic::OCL::PrimitiveExp", is_abstract=True)
atlstatic_OCL_OclUndefinedExp = Class(name="atlstatic::OCL::OclUndefinedExp")
atlstatic_OCL_PropertyCallExp = Class(name="atlstatic::OCL::PropertyCallExp", is_abstract=True)
atlstatic_OCL_NavigationOrAttributeCallExp = Class(name="atlstatic::OCL::NavigationOrAttributeCallExp")
atlstatic_OCL_EnumLiteralExp = Class(name="atlstatic::OCL::EnumLiteralExp")
MapExp = Class(name="MapExp")
atlstatic_OCL_IteratorExp = Class(name="atlstatic::OCL::IteratorExp")
atlstatic_OCL_LetExp = Class(name="atlstatic::OCL::LetExp")
atlstatic_OCL_OperationCallExp = Class(name="atlstatic::OCL::OperationCallExp")
atlstatic_OCL_OperatorCallExp = Class(name="atlstatic::OCL::OperatorCallExp")
atlstatic_OCL_CollectionOperationCallExp = Class(name="atlstatic::OCL::CollectionOperationCallExp")
atlstatic_OCL_IfExp = Class(name="atlstatic::OCL::IfExp")
atlstatic_OCL_LoopExp = Class(name="atlstatic::OCL::LoopExp", is_abstract=True)
atlstatic_OCL_IterateExp = Class(name="atlstatic::OCL::IterateExp")
atlstatic_OCL_VariableDeclaration = Class(name="atlstatic::OCL::VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlstatic_OCL_Iterator = Class(name="atlstatic::OCL::Iterator")
atlstatic_OCL_Parameter = Class(name="atlstatic::OCL::Parameter")
atlstatic_OCL_CollectionType = Class(name="atlstatic::OCL::CollectionType")
atlstatic_OCL_OclType = Class(name="atlstatic::OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
atlstatic_OCL_TupleType = Class(name="atlstatic::OCL::TupleType")
MapType = Class(name="MapType")
atlstatic_OCL_TupleTypeAttribute = Class(name="atlstatic::OCL::TupleTypeAttribute")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atlstatic_OCL_Primitive = Class(name="atlstatic::OCL::Primitive", is_abstract=True)
atlstatic_OCL_StringType = Class(name="atlstatic::OCL::StringType")
Primitive = Class(name="Primitive")
atlstatic_OCL_BooleanType = Class(name="atlstatic::OCL::BooleanType")
atlstatic_OCL_NumericType = Class(name="atlstatic::OCL::NumericType", is_abstract=True)
atlstatic_OCL_IntegerType = Class(name="atlstatic::OCL::IntegerType")
NumericType = Class(name="NumericType")
atlstatic_OCL_RealType = Class(name="atlstatic::OCL::RealType")
atlstatic_OCL_BagType = Class(name="atlstatic::OCL::BagType")
atlstatic_OCL_OrderedSetType = Class(name="atlstatic::OCL::OrderedSetType")
atlstatic_OCL_SequenceType = Class(name="atlstatic::OCL::SequenceType")
atlstatic_OCL_SetType = Class(name="atlstatic::OCL::SetType")
atlstatic_OCL_OclAnyType = Class(name="atlstatic::OCL::OclAnyType")
atlstatic_OCL_OclFeature = Class(name="atlstatic::OCL::OclFeature", is_abstract=True)
TupleType = Class(name="TupleType")
atlstatic_OCL_OclModelElement = Class(name="atlstatic::OCL::OclModelElement")
atlstatic_OCL_MapType = Class(name="atlstatic::OCL::MapType")
atlstatic_OCL_OclFeatureDefinition = Class(name="atlstatic::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlstatic_OCL_OclContextDefinition = Class(name="atlstatic::OCL::OclContextDefinition")
atlstatic_OCL_Attribute = Class(name="atlstatic::OCL::Attribute")
atlstatic_OCL_Operation = Class(name="atlstatic::OCL::Operation")
atlstatic_OCL_OclModel = Class(name="atlstatic::OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# atlstatic_ATL_LocatedElement class attributes and methods
atlstatic_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlstatic_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlstatic_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlstatic_ATL_LocatedElement.attributes={atlstatic_ATL_LocatedElement_commentsAfter, atlstatic_ATL_LocatedElement_location, atlstatic_ATL_LocatedElement_commentsBefore}

# atlstatic_ATL_Unit class attributes and methods
atlstatic_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Unit.attributes={atlstatic_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# atlstatic_ATL_Library class attributes and methods

# Unit class attributes and methods

# atlstatic_ATL_ModuleElement class attributes and methods

# atlstatic_ATL_Helper class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlstatic_ATL_Rule class attributes and methods
atlstatic_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Rule.attributes={atlstatic_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# Helper class attributes and methods

# atlstatic_ATL_MatchedRule class attributes and methods
atlstatic_ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlstatic_ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlstatic_ATL_MatchedRule.attributes={atlstatic_ATL_MatchedRule_isRefining, atlstatic_ATL_MatchedRule_isNoDefault, atlstatic_ATL_MatchedRule_isAbstract}

# Rule class attributes and methods

# atlstatic_ATL_Query class attributes and methods

# InPattern class attributes and methods

# OclExpression class attributes and methods

# MatchedRule class attributes and methods

# atlstatic_ATL_Module class attributes and methods
atlstatic_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_Module.attributes={atlstatic_ATL_Module_isRefining}

# OclModel class attributes and methods

# atlstatic_ATL_LazyMatchedRule class attributes and methods
atlstatic_ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlstatic_ATL_LazyMatchedRule.attributes={atlstatic_ATL_LazyMatchedRule_isUnique}

# ModuleElement class attributes and methods

# atlstatic_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlstatic_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atlstatic_ATL_DropPattern class attributes and methods

# atlstatic_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlstatic_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atlstatic_ATL_SimpleInPatternElement class attributes and methods

# atlstatic_ATL_OutPatternElement class attributes and methods

# atlstatic_ATL_CalledRule class attributes and methods
atlstatic_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlstatic_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlstatic_ATL_CalledRule.attributes={atlstatic_ATL_CalledRule_isEntrypoint, atlstatic_ATL_CalledRule_isEndpoint}

# Parameter class attributes and methods

# Binding class attributes and methods

# atlstatic_ATL_SimpleOutPatternElement class attributes and methods

# atlstatic_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlstatic_ATL_Binding class attributes and methods
atlstatic_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_Binding.attributes={atlstatic_ATL_Binding_isAssignment, atlstatic_ATL_Binding_propertyName}

# atlstatic_ATL_RuleVariableDeclaration class attributes and methods

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

# atlstatic_ATL_IfStat class attributes and methods

# atlstatic_ATL_ForStat class attributes and methods

# atlstatic_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# atlstatic_OCL_VariableExp class attributes and methods

# atlstatic_OCL_SuperExp class attributes and methods

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

# atlstatic_OCL_BagExp class attributes and methods

# atlstatic_OCL_OrderedSetExp class attributes and methods

# atlstatic_OCL_SequenceExp class attributes and methods

# atlstatic_OCL_SetExp class attributes and methods

# atlstatic_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# atlstatic_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# atlstatic_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlstatic_OCL_MapElement class attributes and methods

# atlstatic_OCL_PrimitiveExp class attributes and methods

# atlstatic_OCL_OclUndefinedExp class attributes and methods

# atlstatic_OCL_PropertyCallExp class attributes and methods

# atlstatic_OCL_NavigationOrAttributeCallExp class attributes and methods
atlstatic_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_NavigationOrAttributeCallExp.attributes={atlstatic_OCL_NavigationOrAttributeCallExp_name}

# atlstatic_OCL_EnumLiteralExp class attributes and methods
atlstatic_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_EnumLiteralExp.attributes={atlstatic_OCL_EnumLiteralExp_name}

# MapExp class attributes and methods

# atlstatic_OCL_IteratorExp class attributes and methods
atlstatic_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_IteratorExp.attributes={atlstatic_OCL_IteratorExp_name}

# atlstatic_OCL_LetExp class attributes and methods

# atlstatic_OCL_OperationCallExp class attributes and methods
atlstatic_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlstatic_OCL_OperationCallExp.attributes={atlstatic_OCL_OperationCallExp_operationName}

# atlstatic_OCL_OperatorCallExp class attributes and methods

# atlstatic_OCL_CollectionOperationCallExp class attributes and methods

# atlstatic_OCL_IfExp class attributes and methods

# atlstatic_OCL_LoopExp class attributes and methods

# atlstatic_OCL_IterateExp class attributes and methods

# atlstatic_OCL_VariableDeclaration class attributes and methods
atlstatic_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlstatic_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlstatic_OCL_VariableDeclaration.attributes={atlstatic_OCL_VariableDeclaration_varName, atlstatic_OCL_VariableDeclaration_id}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlstatic_OCL_Iterator class attributes and methods

# atlstatic_OCL_Parameter class attributes and methods

# atlstatic_OCL_CollectionType class attributes and methods

# atlstatic_OCL_OclType class attributes and methods
atlstatic_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclType.attributes={atlstatic_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# atlstatic_OCL_TupleType class attributes and methods

# MapType class attributes and methods

# atlstatic_OCL_TupleTypeAttribute class attributes and methods
atlstatic_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_TupleTypeAttribute.attributes={atlstatic_OCL_TupleTypeAttribute_name}

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# atlstatic_OCL_Primitive class attributes and methods

# atlstatic_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlstatic_OCL_BooleanType class attributes and methods

# atlstatic_OCL_NumericType class attributes and methods

# atlstatic_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# atlstatic_OCL_RealType class attributes and methods

# atlstatic_OCL_BagType class attributes and methods

# atlstatic_OCL_OrderedSetType class attributes and methods

# atlstatic_OCL_SequenceType class attributes and methods

# atlstatic_OCL_SetType class attributes and methods

# atlstatic_OCL_OclAnyType class attributes and methods

# atlstatic_OCL_OclFeature class attributes and methods

# TupleType class attributes and methods

# atlstatic_OCL_OclModelElement class attributes and methods

# atlstatic_OCL_MapType class attributes and methods

# atlstatic_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlstatic_OCL_OclContextDefinition class attributes and methods

# atlstatic_OCL_Attribute class attributes and methods
atlstatic_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Attribute.attributes={atlstatic_OCL_Attribute_name}

# atlstatic_OCL_Operation class attributes and methods
atlstatic_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Operation.attributes={atlstatic_OCL_Operation_name}

# atlstatic_OCL_OclModel class attributes and methods
atlstatic_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclModel.attributes={atlstatic_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="ATL", type=atlstatic_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="LibraryRef", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="ATL2", type=atlstatic_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern24: BinaryAssociation = BinaryAssociation(
    name="inPattern24",
    ends={
        Property(name="ATL25", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="OclExpression", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children26: BinaryAssociation = BinaryAssociation(
    name="children26",
    ends={
        Property(name="ATL27", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
helpers4: BinaryAssociation = BinaryAssociation(
    name="helpers4",
    ends={
        Property(name="ATL6", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="Helper5", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superRule28: BinaryAssociation = BinaryAssociation(
    name="superRule28",
    ends={
        Property(name="ATL30", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule29", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
inModels7: BinaryAssociation = BinaryAssociation(
    name="inModels7",
    ends={
        Property(name="OclModel", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
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
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="atlstatic_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Parameter", type=atlstatic_ATL_CalledRule, multiplicity=Multiplicity(1, 1))
    }
)
elements32: BinaryAssociation = BinaryAssociation(
    name="elements32",
    ends={
        Property(name="ATL33", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule34: BinaryAssociation = BinaryAssociation(
    name="rule34",
    ends={
        Property(name="ATL36", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchedRule35", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter37: BinaryAssociation = BinaryAssociation(
    name="filter37",
    ends={
        Property(name="OclExpression38", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule39: BinaryAssociation = BinaryAssociation(
    name="rule39",
    ends={
        Property(name="ATL40", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern41: BinaryAssociation = BinaryAssociation(
    name="dropPattern41",
    ends={
        Property(name="ATL42", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="DropPattern", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements43: BinaryAssociation = BinaryAssociation(
    name="elements43",
    ends={
        Property(name="ATL44", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern45: BinaryAssociation = BinaryAssociation(
    name="outPattern45",
    ends={
        Property(name="ATL47", type=atlstatic_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern46", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo48: BinaryAssociation = BinaryAssociation(
    name="mapsTo48",
    ends={
        Property(name="ATL50", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement49", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern51: BinaryAssociation = BinaryAssociation(
    name="inPattern51",
    ends={
        Property(name="ATL53", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPattern52", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models54: BinaryAssociation = BinaryAssociation(
    name="models54",
    ends={
        Property(name="OclModel55", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
sourceElement59: BinaryAssociation = BinaryAssociation(
    name="sourceElement59",
    ends={
        Property(name="ATL61", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InPatternElement60", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings62: BinaryAssociation = BinaryAssociation(
    name="bindings62",
    ends={
        Property(name="ATL63", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model64: BinaryAssociation = BinaryAssociation(
    name="model64",
    ends={
        Property(name="OclModel65", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings66: BinaryAssociation = BinaryAssociation(
    name="reverseBindings66",
    ends={
        Property(name="OclExpression67", type=atlstatic_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection68: BinaryAssociation = BinaryAssociation(
    name="collection68",
    ends={
        Property(name="OclExpression69", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator70: BinaryAssociation = BinaryAssociation(
    name="iterator70",
    ends={
        Property(name="Iterator", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement71", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value72: BinaryAssociation = BinaryAssociation(
    name="value72",
    ends={
        Property(name="OclExpression73", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement74: BinaryAssociation = BinaryAssociation(
    name="outPatternElement74",
    ends={
        Property(name="ATL76", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPatternElement75", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule77: BinaryAssociation = BinaryAssociation(
    name="rule77",
    ends={
        Property(name="ATL79", type=atlstatic_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule78", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit80: BinaryAssociation = BinaryAssociation(
    name="unit80",
    ends={
        Property(name="ATL81", type=atlstatic_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Unit", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
outPattern56: BinaryAssociation = BinaryAssociation(
    name="outPattern56",
    ends={
        Property(name="ATL58", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OutPattern57", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
rule82: BinaryAssociation = BinaryAssociation(
    name="rule82",
    ends={
        Property(name="ATL84", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule83", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements85: BinaryAssociation = BinaryAssociation(
    name="statements85",
    ends={
        Property(name="Statement", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="OclExpression87", type=atlstatic_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source88: BinaryAssociation = BinaryAssociation(
    name="source88",
    ends={
        Property(name="OclExpression89", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="OclExpression92", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat91", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition93: BinaryAssociation = BinaryAssociation(
    name="condition93",
    ends={
        Property(name="OclExpression94", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements95: BinaryAssociation = BinaryAssociation(
    name="thenStatements95",
    ends={
        Property(name="Statement97", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat96", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements98: BinaryAssociation = BinaryAssociation(
    name="elseStatements98",
    ends={
        Property(name="Statement100", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat99", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator101: BinaryAssociation = BinaryAssociation(
    name="iterator101",
    ends={
        Property(name="Iterator102", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection103: BinaryAssociation = BinaryAssociation(
    name="collection103",
    ends={
        Property(name="OclExpression105", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat104", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements106: BinaryAssociation = BinaryAssociation(
    name="statements106",
    ends={
        Property(name="Statement108", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat107", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="OCL", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3110: BinaryAssociation = BinaryAssociation(
    name="ifExp3110",
    ends={
        Property(name="OCL111", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty112: BinaryAssociation = BinaryAssociation(
    name="appliedProperty112",
    ends={
        Property(name="OCL113", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyCallExp", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection114: BinaryAssociation = BinaryAssociation(
    name="collection114",
    ends={
        Property(name="OCL115", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionExp", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp116: BinaryAssociation = BinaryAssociation(
    name="letExp116",
    ends={
        Property(name="OCL117", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp118: BinaryAssociation = BinaryAssociation(
    name="loopExp118",
    ends={
        Property(name="OCL119", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation120: BinaryAssociation = BinaryAssociation(
    name="parentOperation120",
    ends={
        Property(name="OCL121", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationCallExp", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable122: BinaryAssociation = BinaryAssociation(
    name="initializedVariable122",
    ends={
        Property(name="OCL123", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2124: BinaryAssociation = BinaryAssociation(
    name="ifExp2124",
    ends={
        Property(name="OCL126", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp125", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation127: BinaryAssociation = BinaryAssociation(
    name="owningOperation127",
    ends={
        Property(name="OCL128", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1129: BinaryAssociation = BinaryAssociation(
    name="ifExp1129",
    ends={
        Property(name="OCL131", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="IfExp130", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute132: BinaryAssociation = BinaryAssociation(
    name="owningAttribute132",
    ends={
        Property(name="OCL133", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable134: BinaryAssociation = BinaryAssociation(
    name="referredVariable134",
    ends={
        Property(name="OCL136", type=atlstatic_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration135", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements137: BinaryAssociation = BinaryAssociation(
    name="elements137",
    ends={
        Property(name="OCL139", type=atlstatic_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression138", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart140: BinaryAssociation = BinaryAssociation(
    name="tuplePart140",
    ends={
        Property(name="OCL141", type=atlstatic_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TuplePart", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple142: BinaryAssociation = BinaryAssociation(
    name="tuple142",
    ends={
        Property(name="OCL143", type=atlstatic_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements144: BinaryAssociation = BinaryAssociation(
    name="elements144",
    ends={
        Property(name="OCL145", type=atlstatic_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="MapElement", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map146: BinaryAssociation = BinaryAssociation(
    name="map146",
    ends={
        Property(name="OCL147", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MapExp", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key148: BinaryAssociation = BinaryAssociation(
    name="key148",
    ends={
        Property(name="OclExpression149", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source153: BinaryAssociation = BinaryAssociation(
    name="source153",
    ends={
        Property(name="OCL155", type=atlstatic_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression154", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value150: BinaryAssociation = BinaryAssociation(
    name="value150",
    ends={
        Property(name="OclExpression152", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement151", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result165: BinaryAssociation = BinaryAssociation(
    name="result165",
    ends={
        Property(name="OCL167", type=atlstatic_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration166", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable168: BinaryAssociation = BinaryAssociation(
    name="variable168",
    ends={
        Property(name="OCL170", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration169", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments156: BinaryAssociation = BinaryAssociation(
    name="arguments156",
    ends={
        Property(name="OCL158", type=atlstatic_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression157", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_171: BinaryAssociation = BinaryAssociation(
    name="in_171",
    ends={
        Property(name="OCL173", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression172", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body159: BinaryAssociation = BinaryAssociation(
    name="body159",
    ends={
        Property(name="OCL161", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression160", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators162: BinaryAssociation = BinaryAssociation(
    name="iterators162",
    ends={
        Property(name="OCL164", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator163", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseExpression180: BinaryAssociation = BinaryAssociation(
    name="elseExpression180",
    ends={
        Property(name="OCL182", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression181", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression174: BinaryAssociation = BinaryAssociation(
    name="thenExpression174",
    ends={
        Property(name="OCL176", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression175", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition177: BinaryAssociation = BinaryAssociation(
    name="condition177",
    ends={
        Property(name="OCL179", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression178", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
letExp189: BinaryAssociation = BinaryAssociation(
    name="letExp189",
    ends={
        Property(name="OCL191", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp190", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp192: BinaryAssociation = BinaryAssociation(
    name="baseExp192",
    ends={
        Property(name="OCL193", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="IterateExp", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp194: BinaryAssociation = BinaryAssociation(
    name="variableExp194",
    ends={
        Property(name="OCL195", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableExp", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr196: BinaryAssociation = BinaryAssociation(
    name="loopExpr196",
    ends={
        Property(name="OCL198", type=atlstatic_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopExp197", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType199: BinaryAssociation = BinaryAssociation(
    name="elementType199",
    ends={
        Property(name="OCL201", type=atlstatic_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType200", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type183: BinaryAssociation = BinaryAssociation(
    name="type183",
    ends={
        Property(name="OCL185", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType184", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions202: BinaryAssociation = BinaryAssociation(
    name="definitions202",
    ends={
        Property(name="OCL203", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression204: BinaryAssociation = BinaryAssociation(
    name="oclExpression204",
    ends={
        Property(name="OCL206", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression205", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
initExpression186: BinaryAssociation = BinaryAssociation(
    name="initExpression186",
    ends={
        Property(name="OCL188", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression187", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation207: BinaryAssociation = BinaryAssociation(
    name="operation207",
    ends={
        Property(name="OCL209", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation208", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
attributes225: BinaryAssociation = BinaryAssociation(
    name="attributes225",
    ends={
        Property(name="OCL227", type=atlstatic_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute226", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapType2210: BinaryAssociation = BinaryAssociation(
    name="mapType2210",
    ends={
        Property(name="OCL211", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute212: BinaryAssociation = BinaryAssociation(
    name="attribute212",
    ends={
        Property(name="OCL214", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute213", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType215: BinaryAssociation = BinaryAssociation(
    name="mapType215",
    ends={
        Property(name="OCL217", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="MapType216", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes218: BinaryAssociation = BinaryAssociation(
    name="collectionTypes218",
    ends={
        Property(name="OCL219", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute220: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute220",
    ends={
        Property(name="OCL221", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleTypeAttribute", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration222: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration222",
    ends={
        Property(name="OCL224", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclaration223", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
definition253: BinaryAssociation = BinaryAssociation(
    name="definition253",
    ends={
        Property(name="OCL255", type=atlstatic_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition254", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
type228: BinaryAssociation = BinaryAssociation(
    name="type228",
    ends={
        Property(name="OCL230", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType229", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType231: BinaryAssociation = BinaryAssociation(
    name="tupleType231",
    ends={
        Property(name="OCL232", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleType", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model233: BinaryAssociation = BinaryAssociation(
    name="model233",
    ends={
        Property(name="OCL235", type=atlstatic_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel234", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType236: BinaryAssociation = BinaryAssociation(
    name="valueType236",
    ends={
        Property(name="OCL238", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType237", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType239: BinaryAssociation = BinaryAssociation(
    name="keyType239",
    ends={
        Property(name="OCL241", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType240", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature242: BinaryAssociation = BinaryAssociation(
    name="feature242",
    ends={
        Property(name="OCL243", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeature", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_244: BinaryAssociation = BinaryAssociation(
    name="context_244",
    ends={
        Property(name="OCL246", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclContextDefinition245", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition247: BinaryAssociation = BinaryAssociation(
    name="definition247",
    ends={
        Property(name="OCL249", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclFeatureDefinition248", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_250: BinaryAssociation = BinaryAssociation(
    name="context_250",
    ends={
        Property(name="OCL252", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType251", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression256: BinaryAssociation = BinaryAssociation(
    name="initExpression256",
    ends={
        Property(name="OCL258", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression257", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type259: BinaryAssociation = BinaryAssociation(
    name="type259",
    ends={
        Property(name="OCL261", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType260", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters262: BinaryAssociation = BinaryAssociation(
    name="parameters262",
    ends={
        Property(name="Parameter263", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType264: BinaryAssociation = BinaryAssociation(
    name="returnType264",
    ends={
        Property(name="OCL266", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclType265", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body267: BinaryAssociation = BinaryAssociation(
    name="body267",
    ends={
        Property(name="OCL269", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression268", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel270: BinaryAssociation = BinaryAssociation(
    name="metamodel270",
    ends={
        Property(name="OCL272", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel271", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements273: BinaryAssociation = BinaryAssociation(
    name="elements273",
    ends={
        Property(name="OCL274", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModelElement", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model275: BinaryAssociation = BinaryAssociation(
    name="model275",
    ends={
        Property(name="OCL277", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="OclModel276", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_atlstatic_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Unit)
gen_atlstatic_ATL_Library_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Library)
gen_atlstatic_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ModuleElement)
gen_atlstatic_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Rule)
gen_atlstatic_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=atlstatic_ATL_MatchedRule)
gen_atlstatic_ATL_Query_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Query)
gen_atlstatic_ATL_Module_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Module)
gen_atlstatic_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=atlstatic_ATL_LazyMatchedRule)
gen_atlstatic_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_InPattern)
gen_atlstatic_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_OutPattern)
gen_atlstatic_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_DropPattern)
gen_atlstatic_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_PatternElement)
gen_atlstatic_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_InPatternElement)
gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlstatic_ATL_SimpleInPatternElement)
gen_atlstatic_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_OutPatternElement)
gen_atlstatic_ATL_CalledRule_Rule = Generalization(general=Rule, specific=atlstatic_ATL_CalledRule)
gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_SimpleOutPatternElement)
gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_ForEachOutPatternElement)
gen_atlstatic_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Binding)
gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_RuleVariableDeclaration)
gen_atlstatic_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_LibraryRef)
gen_atlstatic_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ActionBlock)
gen_atlstatic_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Statement)
gen_atlstatic_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ExpressionStat)
gen_atlstatic_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_BindingStat)
gen_atlstatic_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_IfStat)
gen_atlstatic_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ForStat)
gen_atlstatic_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclExpression)
gen_atlstatic_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_VariableExp)
gen_atlstatic_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_SuperExp)
gen_atlstatic_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_StringExp)
gen_atlstatic_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_BooleanExp)
gen_atlstatic_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_NumericExp)
gen_atlstatic_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_RealExp)
gen_atlstatic_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_IntegerExp)
gen_atlstatic_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_CollectionExp)
gen_atlstatic_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_BagExp)
gen_atlstatic_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_OrderedSetExp)
gen_atlstatic_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SequenceExp)
gen_atlstatic_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SetExp)
gen_atlstatic_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_TupleExp)
gen_atlstatic_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_TuplePart)
gen_atlstatic_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_MapExp)
gen_atlstatic_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_MapElement)
gen_atlstatic_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PrimitiveExp)
gen_atlstatic_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclUndefinedExp)
gen_atlstatic_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PropertyCallExp)
gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_NavigationOrAttributeCallExp)
gen_atlstatic_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_EnumLiteralExp)
gen_atlstatic_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IteratorExp)
gen_atlstatic_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_LetExp)
gen_atlstatic_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_OperationCallExp)
gen_atlstatic_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_OperatorCallExp)
gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_CollectionOperationCallExp)
gen_atlstatic_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_IfExp)
gen_atlstatic_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_LoopExp)
gen_atlstatic_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IterateExp)
gen_atlstatic_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_VariableDeclaration)
gen_atlstatic_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Iterator)
gen_atlstatic_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Parameter)
gen_atlstatic_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_CollectionType)
gen_atlstatic_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclType)
gen_atlstatic_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_TupleType)
gen_atlstatic_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlstatic_OCL_Primitive)
gen_atlstatic_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_StringType)
gen_atlstatic_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_BooleanType)
gen_atlstatic_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_NumericType)
gen_atlstatic_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_IntegerType)
gen_atlstatic_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_RealType)
gen_atlstatic_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_BagType)
gen_atlstatic_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_OrderedSetType)
gen_atlstatic_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SequenceType)
gen_atlstatic_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SetType)
gen_atlstatic_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclAnyType)
gen_atlstatic_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeature)
gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_TupleTypeAttribute)
gen_atlstatic_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclModelElement)
gen_atlstatic_OCL_MapType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_MapType)
gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeatureDefinition)
gen_atlstatic_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclContextDefinition)
gen_atlstatic_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Attribute)
gen_atlstatic_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Operation)
gen_atlstatic_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="atlstatic",
    types={atlstatic_ATL_LocatedElement, atlstatic_ATL_Unit, LocatedElement, LibraryRef, atlstatic_ATL_Library, Unit, atlstatic_ATL_ModuleElement, atlstatic_ATL_Helper, Query, Library, OclFeatureDefinition, atlstatic_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, Helper, atlstatic_ATL_MatchedRule, Rule, atlstatic_ATL_Query, InPattern, OclExpression, MatchedRule, atlstatic_ATL_Module, OclModel, atlstatic_ATL_LazyMatchedRule, ModuleElement, atlstatic_ATL_InPattern, InPatternElement, atlstatic_ATL_OutPattern, DropPattern, OutPatternElement, atlstatic_ATL_DropPattern, atlstatic_ATL_PatternElement, VariableDeclaration, atlstatic_ATL_InPatternElement, PatternElement, atlstatic_ATL_SimpleInPatternElement, atlstatic_ATL_OutPatternElement, atlstatic_ATL_CalledRule, Parameter_, Binding, atlstatic_ATL_SimpleOutPatternElement, atlstatic_ATL_ForEachOutPatternElement, Iterator, atlstatic_ATL_Binding, atlstatic_ATL_RuleVariableDeclaration, atlstatic_ATL_LibraryRef, atlstatic_ATL_ActionBlock, Statement, atlstatic_ATL_Statement, atlstatic_ATL_ExpressionStat, atlstatic_ATL_BindingStat, atlstatic_ATL_IfStat, atlstatic_ATL_ForStat, atlstatic_OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, atlstatic_OCL_VariableExp, atlstatic_OCL_SuperExp, atlstatic_OCL_StringExp, PrimitiveExp, atlstatic_OCL_BooleanExp, atlstatic_OCL_NumericExp, atlstatic_OCL_RealExp, NumericExp, atlstatic_OCL_IntegerExp, atlstatic_OCL_CollectionExp, atlstatic_OCL_BagExp, atlstatic_OCL_OrderedSetExp, atlstatic_OCL_SequenceExp, atlstatic_OCL_SetExp, atlstatic_OCL_TupleExp, TuplePart, atlstatic_OCL_TuplePart, TupleExp, atlstatic_OCL_MapExp, MapElement, atlstatic_OCL_MapElement, atlstatic_OCL_PrimitiveExp, atlstatic_OCL_OclUndefinedExp, atlstatic_OCL_PropertyCallExp, atlstatic_OCL_NavigationOrAttributeCallExp, atlstatic_OCL_EnumLiteralExp, MapExp, atlstatic_OCL_IteratorExp, atlstatic_OCL_LetExp, atlstatic_OCL_OperationCallExp, atlstatic_OCL_OperatorCallExp, atlstatic_OCL_CollectionOperationCallExp, atlstatic_OCL_IfExp, atlstatic_OCL_LoopExp, atlstatic_OCL_IterateExp, atlstatic_OCL_VariableDeclaration, IterateExp, VariableExp, atlstatic_OCL_Iterator, atlstatic_OCL_Parameter, atlstatic_OCL_CollectionType, atlstatic_OCL_OclType, OclContextDefinition, atlstatic_OCL_TupleType, MapType, atlstatic_OCL_TupleTypeAttribute, CollectionType, TupleTypeAttribute, atlstatic_OCL_Primitive, atlstatic_OCL_StringType, Primitive, atlstatic_OCL_BooleanType, atlstatic_OCL_NumericType, atlstatic_OCL_IntegerType, NumericType, atlstatic_OCL_RealType, atlstatic_OCL_BagType, atlstatic_OCL_OrderedSetType, atlstatic_OCL_SequenceType, atlstatic_OCL_SetType, atlstatic_OCL_OclAnyType, atlstatic_OCL_OclFeature, TupleType, atlstatic_OCL_OclModelElement, atlstatic_OCL_MapType, atlstatic_OCL_OclFeatureDefinition, OclFeature, atlstatic_OCL_OclContextDefinition, atlstatic_OCL_Attribute, atlstatic_OCL_Operation, atlstatic_OCL_OclModel, OclModelElement},
    associations={libraries0, query13, library15, definition17, outPattern18, actionBlock20, variables22, helpers1, inPattern24, body3, children26, helpers4, superRule28, inModels7, outModels8, elements11, parameters31, elements32, rule34, filter37, rule39, dropPattern41, elements43, outPattern45, mapsTo48, inPattern51, models54, sourceElement59, bindings62, model64, reverseBindings66, collection68, iterator70, value72, outPatternElement74, rule77, unit80, outPattern56, rule82, statements85, expression86, source88, value90, condition93, thenStatements95, elseStatements98, iterator101, collection103, statements106, type109, ifExp3110, appliedProperty112, collection114, letExp116, loopExp118, parentOperation120, initializedVariable122, ifExp2124, owningOperation127, ifExp1129, owningAttribute132, referredVariable134, elements137, tuplePart140, tuple142, elements144, map146, key148, source153, value150, result165, variable168, arguments156, in_171, body159, iterators162, elseExpression180, thenExpression174, condition177, letExp189, baseExp192, variableExp194, loopExpr196, elementType199, type183, definitions202, oclExpression204, initExpression186, operation207, attributes225, mapType2210, attribute212, mapType215, collectionTypes218, tupleTypeAttribute220, variableDeclaration222, definition253, type228, tupleType231, model233, valueType236, keyType239, feature242, context_244, definition247, context_250, initExpression256, type259, parameters262, returnType264, body267, metamodel270, elements273, model275},
    generalizations={gen_atlstatic_ATL_Unit_LocatedElement, gen_atlstatic_ATL_Library_Unit, gen_atlstatic_ATL_ModuleElement_LocatedElement, gen_atlstatic_ATL_Helper_ModuleElement, gen_atlstatic_ATL_Rule_ModuleElement, gen_atlstatic_ATL_MatchedRule_Rule, gen_atlstatic_ATL_Query_Unit, gen_atlstatic_ATL_Module_Unit, gen_atlstatic_ATL_LazyMatchedRule_MatchedRule, gen_atlstatic_ATL_InPattern_LocatedElement, gen_atlstatic_ATL_OutPattern_LocatedElement, gen_atlstatic_ATL_DropPattern_LocatedElement, gen_atlstatic_ATL_PatternElement_VariableDeclaration, gen_atlstatic_ATL_InPatternElement_PatternElement, gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement, gen_atlstatic_ATL_OutPatternElement_PatternElement, gen_atlstatic_ATL_CalledRule_Rule, gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlstatic_ATL_Binding_LocatedElement, gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlstatic_ATL_LibraryRef_LocatedElement, gen_atlstatic_ATL_ActionBlock_LocatedElement, gen_atlstatic_ATL_Statement_LocatedElement, gen_atlstatic_ATL_ExpressionStat_Statement, gen_atlstatic_ATL_BindingStat_Statement, gen_atlstatic_ATL_IfStat_Statement, gen_atlstatic_ATL_ForStat_Statement, gen_atlstatic_OCL_OclExpression_LocatedElement, gen_atlstatic_OCL_VariableExp_OclExpression, gen_atlstatic_OCL_SuperExp_OclExpression, gen_atlstatic_OCL_StringExp_PrimitiveExp, gen_atlstatic_OCL_BooleanExp_PrimitiveExp, gen_atlstatic_OCL_NumericExp_PrimitiveExp, gen_atlstatic_OCL_RealExp_NumericExp, gen_atlstatic_OCL_IntegerExp_NumericExp, gen_atlstatic_OCL_CollectionExp_OclExpression, gen_atlstatic_OCL_BagExp_CollectionExp, gen_atlstatic_OCL_OrderedSetExp_CollectionExp, gen_atlstatic_OCL_SequenceExp_CollectionExp, gen_atlstatic_OCL_SetExp_CollectionExp, gen_atlstatic_OCL_TupleExp_OclExpression, gen_atlstatic_OCL_TuplePart_VariableDeclaration, gen_atlstatic_OCL_MapExp_OclExpression, gen_atlstatic_OCL_MapElement_LocatedElement, gen_atlstatic_OCL_PrimitiveExp_OclExpression, gen_atlstatic_OCL_OclUndefinedExp_OclExpression, gen_atlstatic_OCL_PropertyCallExp_OclExpression, gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlstatic_OCL_EnumLiteralExp_OclExpression, gen_atlstatic_OCL_IteratorExp_LoopExp, gen_atlstatic_OCL_LetExp_OclExpression, gen_atlstatic_OCL_OperationCallExp_PropertyCallExp, gen_atlstatic_OCL_OperatorCallExp_OperationCallExp, gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlstatic_OCL_IfExp_OclExpression, gen_atlstatic_OCL_LoopExp_PropertyCallExp, gen_atlstatic_OCL_IterateExp_LoopExp, gen_atlstatic_OCL_VariableDeclaration_LocatedElement, gen_atlstatic_OCL_Iterator_VariableDeclaration, gen_atlstatic_OCL_Parameter_VariableDeclaration, gen_atlstatic_OCL_CollectionType_OclType, gen_atlstatic_OCL_OclType_OclExpression, gen_atlstatic_OCL_TupleType_OclType, gen_atlstatic_OCL_Primitive_OclType, gen_atlstatic_OCL_StringType_Primitive, gen_atlstatic_OCL_BooleanType_Primitive, gen_atlstatic_OCL_NumericType_Primitive, gen_atlstatic_OCL_IntegerType_NumericType, gen_atlstatic_OCL_RealType_NumericType, gen_atlstatic_OCL_BagType_CollectionType, gen_atlstatic_OCL_OrderedSetType_CollectionType, gen_atlstatic_OCL_SequenceType_CollectionType, gen_atlstatic_OCL_SetType_CollectionType, gen_atlstatic_OCL_OclAnyType_OclType, gen_atlstatic_OCL_OclFeature_LocatedElement, gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement, gen_atlstatic_OCL_OclModelElement_OclType, gen_atlstatic_OCL_MapType_OclType, gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement, gen_atlstatic_OCL_OclContextDefinition_LocatedElement, gen_atlstatic_OCL_Attribute_OclFeature, gen_atlstatic_OCL_Operation_OclFeature, gen_atlstatic_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)