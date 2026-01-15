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
SectionType: Enumeration = Enumeration(
    name="SectionType",
    literals={
            EnumerationLiteral(name="LHS"),
			EnumerationLiteral(name="RHS"),
			EnumerationLiteral(name="NAC"),
			EnumerationLiteral(name="PAC"),
			EnumerationLiteral(name="PRE"),
			EnumerationLiteral(name="POST")
    }
)

TypedModelAction: Enumeration = Enumeration(
    name="TypedModelAction",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="readOnly"),
			EnumerationLiteral(name="viewOnly"),
			EnumerationLiteral(name="createOnly"),
			EnumerationLiteral(name="transient")
    }
)

UndefinedLiteral: Enumeration = Enumeration(
    name="UndefinedLiteral",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="INVALID")
    }
)

PredefinedVariable: Enumeration = Enumeration(
    name="PredefinedVariable",
    literals={
            EnumerationLiteral(name="this"),
			EnumerationLiteral(name="id")
    }
)

OperationSeparator: Enumeration = Enumeration(
    name="OperationSeparator",
    literals={
            EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="arrow")
    }
)

IteratorType: Enumeration = Enumeration(
    name="IteratorType",
    literals={
            EnumerationLiteral(name="forAll"),
			EnumerationLiteral(name="exists"),
			EnumerationLiteral(name="select"),
			EnumerationLiteral(name="reject"),
			EnumerationLiteral(name="collect"),
			EnumerationLiteral(name="closure")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="implies")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="lessOrEq"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="greaterOrEq"),
			EnumerationLiteral(name="notEqual")
    }
)

AdditiveOperator: Enumeration = Enumeration(
    name="AdditiveOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

MultiplicativeOperator: Enumeration = Enumeration(
    name="MultiplicativeOperator",
    literals={
            EnumerationLiteral(name="multi"),
			EnumerationLiteral(name="div")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="not")
    }
)

ScopeType: Enumeration = Enumeration(
    name="ScopeType",
    literals={
            EnumerationLiteral(name="all"),
			EnumerationLiteral(name="staticRandom"),
			EnumerationLiteral(name="dynamicRandom")
    }
)

OrderType: Enumeration = Enumeration(
    name="OrderType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="parallel")
    }
)

IterationType: Enumeration = Enumeration(
    name="IterationType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="shuffle")
    }
)

RepetitionType: Enumeration = Enumeration(
    name="RepetitionType",
    literals={
            EnumerationLiteral(name="allMatches"),
			EnumerationLiteral(name="first"),
			EnumerationLiteral(name="randomOne")
    }
)

# Classes
morel_NamedElement = Class(name="morel::NamedElement", is_abstract=True)
morel_Section = Class(name="morel::Section", is_abstract=True)
morel_Pattern = Class(name="morel::Pattern")
Section = Class(name="Section")
morel_ObjectVariable = Class(name="morel::ObjectVariable")
morel_LinkConstraint = Class(name="morel::LinkConstraint", is_abstract=True)
morel_Statement = Class(name="morel::Statement", is_abstract=True)
morel_AdditionalConstraint = Class(name="morel::AdditionalConstraint", is_abstract=True)
morel_Clause = Class(name="morel::Clause")
morel_Variable = Class(name="morel::Variable", is_abstract=True)
NamedElement = Class(name="NamedElement")
Variable = Class(name="Variable")
morel_EClass = Class(name="morel::EClass")
morel_TypedModel = Class(name="morel::TypedModel")
morel_PrimitiveVariable = Class(name="morel::PrimitiveVariable")
morel_EDataType = Class(name="morel::EDataType")
morel_SimpleLinkConstraint = Class(name="morel::SimpleLinkConstraint")
LinkConstraint = Class(name="LinkConstraint")
morel_Expression = Class(name="morel::Expression", is_abstract=True)
morel_EReference = Class(name="morel::EReference")
morel_EnclosureLinkConstraint = Class(name="morel::EnclosureLinkConstraint")
morel_PathConstraint = Class(name="morel::PathConstraint")
morel_LiteralExp = Class(name="morel::LiteralExp", is_abstract=True)
AtomicExp = Class(name="AtomicExp")
morel_QueryModel = Class(name="morel::QueryModel")
Unit = Class(name="Unit")
morel_Query = Class(name="morel::Query")
morel_EPackage = Class(name="morel::EPackage")
Pattern = Class(name="Pattern")
Executable = Class(name="Executable")
morel_Unit = Class(name="morel::Unit", is_abstract=True)
morel_AtomicExp = Class(name="morel::AtomicExp", is_abstract=True)
UnaryExpChild = Class(name="UnaryExpChild")
morel_CallPathExp = Class(name="morel::CallPathExp", is_abstract=True)
morel_NestedExp = Class(name="morel::NestedExp")
morel_StringLiteralExp = Class(name="morel::StringLiteralExp")
LiteralExp = Class(name="LiteralExp")
morel_IntegerLiteralExp = Class(name="morel::IntegerLiteralExp")
morel_RealLiteralExp = Class(name="morel::RealLiteralExp")
morel_BooleanLiteralExp = Class(name="morel::BooleanLiteralExp")
morel_UndefinedLiteralExp = Class(name="morel::UndefinedLiteralExp")
morel_CollectionLiteralExp = Class(name="morel::CollectionLiteralExp")
morel_EnumLiteralExp = Class(name="morel::EnumLiteralExp")
morel_EEnum = Class(name="morel::EEnum")
morel_EEnumLiteral = Class(name="morel::EEnumLiteral")
morel_TypeLiteralExp = Class(name="morel::TypeLiteralExp")
morel_EClassifier = Class(name="morel::EClassifier")
morel_VariableExp = Class(name="morel::VariableExp")
morel_PredefinedVariableExp = Class(name="morel::PredefinedVariableExp")
morel_FeaturePathExp = Class(name="morel::FeaturePathExp")
CallPathExp = Class(name="CallPathExp")
morel_OperationPathExp = Class(name="morel::OperationPathExp")
morel_LoopPathExp = Class(name="morel::LoopPathExp", is_abstract=True)
morel_IteratorPathExp = Class(name="morel::IteratorPathExp")
LoopPathExp = Class(name="LoopPathExp")
morel_LetExp = Class(name="morel::LetExp")
Expression = Class(name="Expression")
ImperativeExp = Class(name="ImperativeExp")
morel_VariableWithInit = Class(name="morel::VariableWithInit", is_abstract=True)
morel_ObjectVariableWithInit = Class(name="morel::ObjectVariableWithInit")
ObjectVariable = Class(name="ObjectVariable")
VariableWithInit = Class(name="VariableWithInit")
morel_PrimitiveVariableWithInit = Class(name="morel::PrimitiveVariableWithInit")
PrimitiveVariable = Class(name="PrimitiveVariable")
morel_ConditionExp = Class(name="morel::ConditionExp")
morel_BooleanImpliesExp = Class(name="morel::BooleanImpliesExp")
morel_BooleanImpliesExpChild = Class(name="morel::BooleanImpliesExpChild", is_abstract=True)
morel_BooleanOrExp = Class(name="morel::BooleanOrExp")
BooleanImpliesExpChild = Class(name="BooleanImpliesExpChild")
morel_BooleanOrExpChild = Class(name="morel::BooleanOrExpChild", is_abstract=True)
morel_BooleanAndExp = Class(name="morel::BooleanAndExp")
BooleanOrExpChild = Class(name="BooleanOrExpChild")
morel_BooleanAndExpChild = Class(name="morel::BooleanAndExpChild", is_abstract=True)
morel_RelationalExp = Class(name="morel::RelationalExp")
BooleanAndExpChild = Class(name="BooleanAndExpChild")
morel_RelationalExpChild = Class(name="morel::RelationalExpChild", is_abstract=True)
morel_AdditiveExp = Class(name="morel::AdditiveExp")
RelationalExpChild = Class(name="RelationalExpChild")
morel_AdditiveExpChild = Class(name="morel::AdditiveExpChild", is_abstract=True)
morel_MultiplicativeExp = Class(name="morel::MultiplicativeExp")
AdditiveExpChild = Class(name="AdditiveExpChild")
morel_MultiplicativeExpChild = Class(name="morel::MultiplicativeExpChild", is_abstract=True)
morel_UnaryExp = Class(name="morel::UnaryExp")
MultiplicativeExpChild = Class(name="MultiplicativeExpChild")
morel_UnaryExpChild = Class(name="morel::UnaryExpChild", is_abstract=True)
morel_CollectionType = Class(name="morel::CollectionType", is_abstract=True)
EDataType = Class(name="EDataType")
morel_OrderedSetType = Class(name="morel::OrderedSetType")
CollectionType = Class(name="CollectionType")
morel_SequenceType = Class(name="morel::SequenceType")
morel_SetType = Class(name="morel::SetType")
morel_BagType = Class(name="morel::BagType")
morel_ImperativeExp = Class(name="morel::ImperativeExp", is_abstract=True)
morel_BindExp = Class(name="morel::BindExp")
morel_PredefinedBindExp = Class(name="morel::PredefinedBindExp")
morel_IfStatement = Class(name="morel::IfStatement")
ImperativeStatement = Class(name="ImperativeStatement")
morel_ImperativeStatement = Class(name="morel::ImperativeStatement", is_abstract=True)
morel_ForStatement = Class(name="morel::ForStatement")
morel_BlockStatement = Class(name="morel::BlockStatement")
morel_TransformationModel = Class(name="morel::TransformationModel")
morel_RuleElement = Class(name="morel::RuleElement", is_abstract=True)
morel_Rule = Class(name="morel::Rule")
RuleElement = Class(name="RuleElement")
morel_RuleGroup = Class(name="morel::RuleGroup")
morel_DeclarativeStatement = Class(name="morel::DeclarativeStatement")
Statement = Class(name="Statement")
morel_ReflectiveVariableExp = Class(name="morel::ReflectiveVariableExp")
morel_ArrayLiteralExp = Class(name="morel::ArrayLiteralExp")
morel_Executable = Class(name="morel::Executable", is_abstract=True)
morel_OrderConstraint = Class(name="morel::OrderConstraint")
AdditionalConstraint = Class(name="AdditionalConstraint")
morel_AllDifferentConstraint = Class(name="morel::AllDifferentConstraint")
morel_PrimitiveConstraint = Class(name="morel::PrimitiveConstraint", is_abstract=True)
morel_MultiValueConstraint = Class(name="morel::MultiValueConstraint")
PrimitiveConstraint = Class(name="PrimitiveConstraint")
morel_EAttribute = Class(name="morel::EAttribute")
morel_ValueRangeConstraint = Class(name="morel::ValueRangeConstraint")

# morel_NamedElement class attributes and methods
morel_NamedElement_name: Property = Property(name="name", type=StringType)
morel_NamedElement.attributes={morel_NamedElement_name}

# morel_Section class attributes and methods
morel_Section_type: Property = Property(name="type", type=StringType)
morel_Section.attributes={morel_Section_type}

# morel_Pattern class attributes and methods

# Section class attributes and methods

# morel_ObjectVariable class attributes and methods

# morel_LinkConstraint class attributes and methods

# morel_Statement class attributes and methods

# morel_AdditionalConstraint class attributes and methods

# morel_Clause class attributes and methods

# morel_Variable class attributes and methods

# NamedElement class attributes and methods

# Variable class attributes and methods

# morel_EClass class attributes and methods

# morel_TypedModel class attributes and methods
morel_TypedModel_type: Property = Property(name="type", type=StringType)
morel_TypedModel.attributes={morel_TypedModel_type}

# morel_PrimitiveVariable class attributes and methods

# morel_EDataType class attributes and methods

# morel_SimpleLinkConstraint class attributes and methods

# LinkConstraint class attributes and methods

# morel_Expression class attributes and methods

# morel_EReference class attributes and methods

# morel_EnclosureLinkConstraint class attributes and methods

# morel_PathConstraint class attributes and methods
morel_PathConstraint_minLength: Property = Property(name="minLength", type=IntegerType)
morel_PathConstraint_maxLength: Property = Property(name="maxLength", type=IntegerType)
morel_PathConstraint.attributes={morel_PathConstraint_maxLength, morel_PathConstraint_minLength}

# morel_LiteralExp class attributes and methods

# AtomicExp class attributes and methods

# morel_QueryModel class attributes and methods

# Unit class attributes and methods

# morel_Query class attributes and methods

# morel_EPackage class attributes and methods

# Pattern class attributes and methods

# Executable class attributes and methods

# morel_Unit class attributes and methods
morel_Unit_m_getTypedModel: Method = Method(name="getTypedModel", parameters={Parameter(name='name')}, type=StringType)
morel_Unit.methods={morel_Unit_m_getTypedModel}

# morel_AtomicExp class attributes and methods

# UnaryExpChild class attributes and methods

# morel_CallPathExp class attributes and methods

# morel_NestedExp class attributes and methods

# morel_StringLiteralExp class attributes and methods
morel_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
morel_StringLiteralExp.attributes={morel_StringLiteralExp_stringSymbol}

# LiteralExp class attributes and methods

# morel_IntegerLiteralExp class attributes and methods
morel_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
morel_IntegerLiteralExp.attributes={morel_IntegerLiteralExp_integerSymbol}

# morel_RealLiteralExp class attributes and methods
morel_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
morel_RealLiteralExp.attributes={morel_RealLiteralExp_realSymbol}

# morel_BooleanLiteralExp class attributes and methods
morel_BooleanLiteralExp_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
morel_BooleanLiteralExp.attributes={morel_BooleanLiteralExp_boolSymbol}

# morel_UndefinedLiteralExp class attributes and methods
morel_UndefinedLiteralExp_value: Property = Property(name="value", type=StringType)
morel_UndefinedLiteralExp.attributes={morel_UndefinedLiteralExp_value}

# morel_CollectionLiteralExp class attributes and methods
morel_CollectionLiteralExp_type: Property = Property(name="type", type=StringType)
morel_CollectionLiteralExp.attributes={morel_CollectionLiteralExp_type}

# morel_EnumLiteralExp class attributes and methods

# morel_EEnum class attributes and methods

# morel_EEnumLiteral class attributes and methods

# morel_TypeLiteralExp class attributes and methods

# morel_EClassifier class attributes and methods

# morel_VariableExp class attributes and methods

# morel_PredefinedVariableExp class attributes and methods
morel_PredefinedVariableExp_variable: Property = Property(name="variable", type=StringType)
morel_PredefinedVariableExp.attributes={morel_PredefinedVariableExp_variable}

# morel_FeaturePathExp class attributes and methods
morel_FeaturePathExp_feature: Property = Property(name="feature", type=StringType)
morel_FeaturePathExp.attributes={morel_FeaturePathExp_feature}

# CallPathExp class attributes and methods

# morel_OperationPathExp class attributes and methods
morel_OperationPathExp_separator: Property = Property(name="separator", type=StringType)
morel_OperationPathExp_operation: Property = Property(name="operation", type=StringType)
morel_OperationPathExp.attributes={morel_OperationPathExp_operation, morel_OperationPathExp_separator}

# morel_LoopPathExp class attributes and methods

# morel_IteratorPathExp class attributes and methods
morel_IteratorPathExp_type: Property = Property(name="type", type=StringType)
morel_IteratorPathExp.attributes={morel_IteratorPathExp_type}

# LoopPathExp class attributes and methods

# morel_LetExp class attributes and methods

# Expression class attributes and methods

# ImperativeExp class attributes and methods

# morel_VariableWithInit class attributes and methods

# morel_ObjectVariableWithInit class attributes and methods

# ObjectVariable class attributes and methods

# VariableWithInit class attributes and methods

# morel_PrimitiveVariableWithInit class attributes and methods

# PrimitiveVariable class attributes and methods

# morel_ConditionExp class attributes and methods

# morel_BooleanImpliesExp class attributes and methods
morel_BooleanImpliesExp_operator: Property = Property(name="operator", type=StringType)
morel_BooleanImpliesExp.attributes={morel_BooleanImpliesExp_operator}

# morel_BooleanImpliesExpChild class attributes and methods

# morel_BooleanOrExp class attributes and methods
morel_BooleanOrExp_operators: Property = Property(name="operators", type=StringType)
morel_BooleanOrExp.attributes={morel_BooleanOrExp_operators}

# BooleanImpliesExpChild class attributes and methods

# morel_BooleanOrExpChild class attributes and methods

# morel_BooleanAndExp class attributes and methods
morel_BooleanAndExp_operators: Property = Property(name="operators", type=StringType)
morel_BooleanAndExp.attributes={morel_BooleanAndExp_operators}

# BooleanOrExpChild class attributes and methods

# morel_BooleanAndExpChild class attributes and methods

# morel_RelationalExp class attributes and methods
morel_RelationalExp_operator: Property = Property(name="operator", type=StringType)
morel_RelationalExp.attributes={morel_RelationalExp_operator}

# BooleanAndExpChild class attributes and methods

# morel_RelationalExpChild class attributes and methods

# morel_AdditiveExp class attributes and methods
morel_AdditiveExp_operators: Property = Property(name="operators", type=StringType)
morel_AdditiveExp.attributes={morel_AdditiveExp_operators}

# RelationalExpChild class attributes and methods

# morel_AdditiveExpChild class attributes and methods

# morel_MultiplicativeExp class attributes and methods
morel_MultiplicativeExp_operators: Property = Property(name="operators", type=StringType)
morel_MultiplicativeExp.attributes={morel_MultiplicativeExp_operators}

# AdditiveExpChild class attributes and methods

# morel_MultiplicativeExpChild class attributes and methods

# morel_UnaryExp class attributes and methods
morel_UnaryExp_operator: Property = Property(name="operator", type=StringType)
morel_UnaryExp.attributes={morel_UnaryExp_operator}

# MultiplicativeExpChild class attributes and methods

# morel_UnaryExpChild class attributes and methods

# morel_CollectionType class attributes and methods

# EDataType class attributes and methods

# morel_OrderedSetType class attributes and methods

# CollectionType class attributes and methods

# morel_SequenceType class attributes and methods

# morel_SetType class attributes and methods

# morel_BagType class attributes and methods

# morel_ImperativeExp class attributes and methods

# morel_BindExp class attributes and methods

# morel_PredefinedBindExp class attributes and methods

# morel_IfStatement class attributes and methods

# ImperativeStatement class attributes and methods

# morel_ImperativeStatement class attributes and methods

# morel_ForStatement class attributes and methods

# morel_BlockStatement class attributes and methods

# morel_TransformationModel class attributes and methods

# morel_RuleElement class attributes and methods

# morel_Rule class attributes and methods

# RuleElement class attributes and methods

# morel_RuleGroup class attributes and methods
morel_RuleGroup_scope: Property = Property(name="scope", type=StringType)
morel_RuleGroup_scopeSize: Property = Property(name="scopeSize", type=IntegerType)
morel_RuleGroup_order: Property = Property(name="order", type=StringType)
morel_RuleGroup_iteration: Property = Property(name="iteration", type=StringType)
morel_RuleGroup_maxIteration: Property = Property(name="maxIteration", type=IntegerType)
morel_RuleGroup_repetition: Property = Property(name="repetition", type=StringType)
morel_RuleGroup.attributes={morel_RuleGroup_repetition, morel_RuleGroup_order, morel_RuleGroup_maxIteration, morel_RuleGroup_scope, morel_RuleGroup_scopeSize, morel_RuleGroup_iteration}

# morel_DeclarativeStatement class attributes and methods

# Statement class attributes and methods

# morel_ReflectiveVariableExp class attributes and methods

# morel_ArrayLiteralExp class attributes and methods

# morel_Executable class attributes and methods
morel_Executable_active: Property = Property(name="active", type=BooleanType)
morel_Executable_parameters: Property = Property(name="parameters", type=StringType)
morel_Executable.attributes={morel_Executable_parameters, morel_Executable_active}

# morel_OrderConstraint class attributes and methods

# AdditionalConstraint class attributes and methods

# morel_AllDifferentConstraint class attributes and methods

# morel_PrimitiveConstraint class attributes and methods

# morel_MultiValueConstraint class attributes and methods

# PrimitiveConstraint class attributes and methods

# morel_EAttribute class attributes and methods

# morel_ValueRangeConstraint class attributes and methods

# Relationships
statements7: BinaryAssociation = BinaryAssociation(
    name="statements7",
    ends={
        Property(name="morel_Statement8", type=morel_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Clause", type=morel_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="morel_ObjectVariable", type=morel_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Pattern", type=morel_ObjectVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkConstraints1: BinaryAssociation = BinaryAssociation(
    name="linkConstraints1",
    ends={
        Property(name="morel_LinkConstraint", type=morel_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Pattern2", type=morel_LinkConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="morel_Statement", type=morel_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Pattern4", type=morel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additionalConstraints5: BinaryAssociation = BinaryAssociation(
    name="additionalConstraints5",
    ends={
        Property(name="morel_AdditionalConstraint", type=morel_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Pattern6", type=morel_AdditionalConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="morel_EClass", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ObjectVariable10", type=morel_EClass, multiplicity=Multiplicity(1, 1))
    }
)
model11: BinaryAssociation = BinaryAssociation(
    name="model11",
    ends={
        Property(name="morel_TypedModel", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ObjectVariable12", type=morel_TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="morel_EDataType", type=morel_PrimitiveVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PrimitiveVariable", type=morel_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="morel_ObjectVariable16", type=morel_LinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_LinkConstraint15", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="morel_ObjectVariable19", type=morel_LinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_LinkConstraint18", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1))
    }
)
id20: BinaryAssociation = BinaryAssociation(
    name="id20",
    ends={
        Property(name="morel_Expression", type=morel_SimpleLinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_SimpleLinkConstraint", type=morel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference21: BinaryAssociation = BinaryAssociation(
    name="reference21",
    ends={
        Property(name="morel_EReference", type=morel_SimpleLinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_SimpleLinkConstraint22", type=morel_EReference, multiplicity=Multiplicity(1, 1))
    }
)
forward23: BinaryAssociation = BinaryAssociation(
    name="forward23",
    ends={
        Property(name="morel_EReference24", type=morel_EnclosureLinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_EnclosureLinkConstraint", type=morel_EReference, multiplicity=Multiplicity(1, 9999))
    }
)
types25: BinaryAssociation = BinaryAssociation(
    name="types25",
    ends={
        Property(name="morel_EClass27", type=morel_EnclosureLinkConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_EnclosureLinkConstraint26", type=morel_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
pathVariable28: BinaryAssociation = BinaryAssociation(
    name="pathVariable28",
    ends={
        Property(name="morel_Variable", type=morel_PathConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PathConstraint", type=morel_Variable, multiplicity=Multiplicity(1, 1))
    }
)
references29: BinaryAssociation = BinaryAssociation(
    name="references29",
    ends={
        Property(name="morel_EReference31", type=morel_PathConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PathConstraint30", type=morel_EReference, multiplicity=Multiplicity(1, 9999))
    }
)
types32: BinaryAssociation = BinaryAssociation(
    name="types32",
    ends={
        Property(name="morel_EClass34", type=morel_PathConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PathConstraint33", type=morel_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
queries35: BinaryAssociation = BinaryAssociation(
    name="queries35",
    ends={
        Property(name="morel_Query", type=morel_QueryModel, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_QueryModel", type=morel_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package36: BinaryAssociation = BinaryAssociation(
    name="package36",
    ends={
        Property(name="morel_EPackage", type=morel_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_TypedModel37", type=morel_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
models38: BinaryAssociation = BinaryAssociation(
    name="models38",
    ends={
        Property(name="morel_TypedModel39", type=morel_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Unit", type=morel_TypedModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataTypes40: BinaryAssociation = BinaryAssociation(
    name="dataTypes40",
    ends={
        Property(name="morel_EDataType42", type=morel_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Unit41", type=morel_EDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path43: BinaryAssociation = BinaryAssociation(
    name="path43",
    ends={
        Property(name="morel_CallPathExp", type=morel_AtomicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_AtomicExp", type=morel_CallPathExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals44: BinaryAssociation = BinaryAssociation(
    name="literals44",
    ends={
        Property(name="morel_Expression45", type=morel_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_CollectionLiteralExp", type=morel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumType46: BinaryAssociation = BinaryAssociation(
    name="enumType46",
    ends={
        Property(name="morel_EEnum", type=morel_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_EnumLiteralExp", type=morel_EEnum, multiplicity=Multiplicity(1, 1))
    }
)
enumSymbol47: BinaryAssociation = BinaryAssociation(
    name="enumSymbol47",
    ends={
        Property(name="morel_EEnumLiteral", type=morel_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_EnumLiteralExp48", type=morel_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="morel_EClassifier", type=morel_TypeLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_TypeLiteralExp", type=morel_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
referredVariable50: BinaryAssociation = BinaryAssociation(
    name="referredVariable50",
    ends={
        Property(name="morel_Variable51", type=morel_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_VariableExp", type=morel_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression52: BinaryAssociation = BinaryAssociation(
    name="expression52",
    ends={
        Property(name="morel_Expression53", type=morel_NestedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_NestedExp", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next55: BinaryAssociation = BinaryAssociation(
    name="next55",
    ends={
        Property(name="morel_CallPathExp56", type=morel_CallPathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_CallPathExp54", type=morel_CallPathExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters57: BinaryAssociation = BinaryAssociation(
    name="parameters57",
    ends={
        Property(name="morel_Expression58", type=morel_OperationPathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_OperationPathExp", type=morel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstVar59: BinaryAssociation = BinaryAssociation(
    name="firstVar59",
    ends={
        Property(name="morel_Variable60", type=morel_IteratorPathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IteratorPathExp", type=morel_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
secondVar61: BinaryAssociation = BinaryAssociation(
    name="secondVar61",
    ends={
        Property(name="morel_Variable63", type=morel_IteratorPathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IteratorPathExp62", type=morel_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExp64: BinaryAssociation = BinaryAssociation(
    name="bodyExp64",
    ends={
        Property(name="morel_Expression66", type=morel_IteratorPathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IteratorPathExp65", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables67: BinaryAssociation = BinaryAssociation(
    name="variables67",
    ends={
        Property(name="morel_VariableWithInit", type=morel_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_LetExp", type=morel_VariableWithInit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inExp68: BinaryAssociation = BinaryAssociation(
    name="inExp68",
    ends={
        Property(name="morel_Expression70", type=morel_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_LetExp69", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExp71: BinaryAssociation = BinaryAssociation(
    name="initExp71",
    ends={
        Property(name="morel_Expression73", type=morel_VariableWithInit, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_VariableWithInit72", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition74: BinaryAssociation = BinaryAssociation(
    name="condition74",
    ends={
        Property(name="morel_BooleanImpliesExp", type=morel_ConditionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ConditionExp", type=morel_BooleanImpliesExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenBranch75: BinaryAssociation = BinaryAssociation(
    name="thenBranch75",
    ends={
        Property(name="morel_Expression77", type=morel_ConditionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ConditionExp76", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBranch78: BinaryAssociation = BinaryAssociation(
    name="elseBranch78",
    ends={
        Property(name="morel_Expression80", type=morel_ConditionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ConditionExp79", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="morel_BooleanImpliesExpChild", type=morel_BooleanImpliesExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BooleanImpliesExp82", type=morel_BooleanImpliesExpChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="morel_BooleanImpliesExpChild85", type=morel_BooleanImpliesExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BooleanImpliesExp84", type=morel_BooleanImpliesExpChild, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children86: BinaryAssociation = BinaryAssociation(
    name="children86",
    ends={
        Property(name="morel_BooleanOrExpChild", type=morel_BooleanOrExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BooleanOrExp", type=morel_BooleanOrExpChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children87: BinaryAssociation = BinaryAssociation(
    name="children87",
    ends={
        Property(name="morel_BooleanAndExpChild", type=morel_BooleanAndExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BooleanAndExp", type=morel_BooleanAndExpChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="morel_RelationalExpChild", type=morel_RelationalExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_RelationalExp", type=morel_RelationalExpChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right89: BinaryAssociation = BinaryAssociation(
    name="right89",
    ends={
        Property(name="morel_RelationalExpChild91", type=morel_RelationalExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_RelationalExp90", type=morel_RelationalExpChild, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children92: BinaryAssociation = BinaryAssociation(
    name="children92",
    ends={
        Property(name="morel_AdditiveExpChild", type=morel_AdditiveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_AdditiveExp", type=morel_AdditiveExpChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children93: BinaryAssociation = BinaryAssociation(
    name="children93",
    ends={
        Property(name="morel_MultiplicativeExpChild", type=morel_MultiplicativeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_MultiplicativeExp", type=morel_MultiplicativeExpChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child94: BinaryAssociation = BinaryAssociation(
    name="child94",
    ends={
        Property(name="morel_UnaryExpChild", type=morel_UnaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_UnaryExp", type=morel_UnaryExpChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType95: BinaryAssociation = BinaryAssociation(
    name="elementType95",
    ends={
        Property(name="morel_EClassifier96", type=morel_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_CollectionType", type=morel_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
source97: BinaryAssociation = BinaryAssociation(
    name="source97",
    ends={
        Property(name="morel_VariableExp98", type=morel_BindExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BindExp", type=morel_VariableExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExp99: BinaryAssociation = BinaryAssociation(
    name="valueExp99",
    ends={
        Property(name="morel_Expression101", type=morel_BindExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BindExp100", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source102: BinaryAssociation = BinaryAssociation(
    name="source102",
    ends={
        Property(name="morel_PredefinedVariableExp", type=morel_PredefinedBindExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PredefinedBindExp", type=morel_PredefinedVariableExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExp103: BinaryAssociation = BinaryAssociation(
    name="valueExp103",
    ends={
        Property(name="morel_Expression105", type=morel_PredefinedBindExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PredefinedBindExp104", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition106: BinaryAssociation = BinaryAssociation(
    name="condition106",
    ends={
        Property(name="morel_BooleanImpliesExp107", type=morel_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IfStatement", type=morel_BooleanImpliesExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement108: BinaryAssociation = BinaryAssociation(
    name="thenStatement108",
    ends={
        Property(name="morel_ImperativeStatement", type=morel_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IfStatement109", type=morel_ImperativeStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement110: BinaryAssociation = BinaryAssociation(
    name="elseStatement110",
    ends={
        Property(name="morel_ImperativeStatement112", type=morel_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_IfStatement111", type=morel_ImperativeStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator113: BinaryAssociation = BinaryAssociation(
    name="iterator113",
    ends={
        Property(name="morel_VariableWithInit114", type=morel_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ForStatement", type=morel_VariableWithInit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
terminationExp115: BinaryAssociation = BinaryAssociation(
    name="terminationExp115",
    ends={
        Property(name="morel_BooleanImpliesExp117", type=morel_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ForStatement116", type=morel_BooleanImpliesExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stepExp118: BinaryAssociation = BinaryAssociation(
    name="stepExp118",
    ends={
        Property(name="morel_Expression120", type=morel_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ForStatement119", type=morel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyStatement121: BinaryAssociation = BinaryAssociation(
    name="bodyStatement121",
    ends={
        Property(name="morel_ImperativeStatement123", type=morel_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ForStatement122", type=morel_ImperativeStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements124: BinaryAssociation = BinaryAssociation(
    name="statements124",
    ends={
        Property(name="morel_Statement125", type=morel_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_BlockStatement", type=morel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules126: BinaryAssociation = BinaryAssociation(
    name="rules126",
    ends={
        Property(name="morel_RuleElement", type=morel_TransformationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_TransformationModel", type=morel_RuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns127: BinaryAssociation = BinaryAssociation(
    name="patterns127",
    ends={
        Property(name="morel_Pattern128", type=morel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Rule", type=morel_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules129: BinaryAssociation = BinaryAssociation(
    name="rules129",
    ends={
        Property(name="morel_Rule130", type=morel_RuleGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_RuleGroup", type=morel_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object152: BinaryAssociation = BinaryAssociation(
    name="object152",
    ends={
        Property(name="morel_MultiValueConstraint", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ObjectVariable153", type=morel_MultiValueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
expression131: BinaryAssociation = BinaryAssociation(
    name="expression131",
    ends={
        Property(name="morel_Expression132", type=morel_DeclarativeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_DeclarativeStatement", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable133: BinaryAssociation = BinaryAssociation(
    name="variable133",
    ends={
        Property(name="morel_Variable134", type=morel_ReflectiveVariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ReflectiveVariableExp", type=morel_Variable, multiplicity=Multiplicity(1, 1))
    }
)
elements135: BinaryAssociation = BinaryAssociation(
    name="elements135",
    ends={
        Property(name="morel_Expression136", type=morel_ArrayLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ArrayLiteralExp", type=morel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveVariables137: BinaryAssociation = BinaryAssociation(
    name="primitiveVariables137",
    ends={
        Property(name="morel_PrimitiveVariable138", type=morel_Executable, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_Executable", type=morel_PrimitiveVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables139: BinaryAssociation = BinaryAssociation(
    name="variables139",
    ends={
        Property(name="morel_Variable141", type=morel_AdditionalConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_AdditionalConstraint140", type=morel_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
base142: BinaryAssociation = BinaryAssociation(
    name="base142",
    ends={
        Property(name="morel_ObjectVariable143", type=morel_OrderConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_OrderConstraint", type=morel_ObjectVariable, multiplicity=Multiplicity(1, 1))
    }
)
references144: BinaryAssociation = BinaryAssociation(
    name="references144",
    ends={
        Property(name="morel_EReference146", type=morel_OrderConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_OrderConstraint145", type=morel_EReference, multiplicity=Multiplicity(1, 9999))
    }
)
types147: BinaryAssociation = BinaryAssociation(
    name="types147",
    ends={
        Property(name="morel_EClass149", type=morel_OrderConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_OrderConstraint148", type=morel_EClass, multiplicity=Multiplicity(1, 9999))
    }
)
variable150: BinaryAssociation = BinaryAssociation(
    name="variable150",
    ends={
        Property(name="morel_PrimitiveVariable151", type=morel_PrimitiveConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_PrimitiveConstraint", type=morel_PrimitiveVariable, multiplicity=Multiplicity(1, 1))
    }
)
attribute154: BinaryAssociation = BinaryAssociation(
    name="attribute154",
    ends={
        Property(name="morel_EAttribute", type=morel_MultiValueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_MultiValueConstraint155", type=morel_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
expression156: BinaryAssociation = BinaryAssociation(
    name="expression156",
    ends={
        Property(name="morel_Expression157", type=morel_ValueRangeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="morel_ValueRangeConstraint", type=morel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_morel_Pattern_Section = Generalization(general=Section, specific=morel_Pattern)
gen_morel_Clause_Section = Generalization(general=Section, specific=morel_Clause)
gen_morel_Variable_NamedElement = Generalization(general=NamedElement, specific=morel_Variable)
gen_morel_ObjectVariable_Variable = Generalization(general=Variable, specific=morel_ObjectVariable)
gen_morel_PrimitiveVariable_Variable = Generalization(general=Variable, specific=morel_PrimitiveVariable)
gen_morel_SimpleLinkConstraint_LinkConstraint = Generalization(general=LinkConstraint, specific=morel_SimpleLinkConstraint)
gen_morel_EnclosureLinkConstraint_LinkConstraint = Generalization(general=LinkConstraint, specific=morel_EnclosureLinkConstraint)
gen_morel_PathConstraint_LinkConstraint = Generalization(general=LinkConstraint, specific=morel_PathConstraint)
gen_morel_LiteralExp_AtomicExp = Generalization(general=AtomicExp, specific=morel_LiteralExp)
gen_morel_QueryModel_Unit = Generalization(general=Unit, specific=morel_QueryModel)
gen_morel_TypedModel_NamedElement = Generalization(general=NamedElement, specific=morel_TypedModel)
gen_morel_Query_Pattern = Generalization(general=Pattern, specific=morel_Query)
gen_morel_Query_NamedElement = Generalization(general=NamedElement, specific=morel_Query)
gen_morel_Query_Executable = Generalization(general=Executable, specific=morel_Query)
gen_morel_AtomicExp_UnaryExpChild = Generalization(general=UnaryExpChild, specific=morel_AtomicExp)
gen_morel_NestedExp_AtomicExp = Generalization(general=AtomicExp, specific=morel_NestedExp)
gen_morel_StringLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_StringLiteralExp)
gen_morel_IntegerLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_IntegerLiteralExp)
gen_morel_RealLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_RealLiteralExp)
gen_morel_BooleanLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_BooleanLiteralExp)
gen_morel_UndefinedLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_UndefinedLiteralExp)
gen_morel_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_CollectionLiteralExp)
gen_morel_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_EnumLiteralExp)
gen_morel_TypeLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_TypeLiteralExp)
gen_morel_VariableExp_AtomicExp = Generalization(general=AtomicExp, specific=morel_VariableExp)
gen_morel_PredefinedVariableExp_AtomicExp = Generalization(general=AtomicExp, specific=morel_PredefinedVariableExp)
gen_morel_FeaturePathExp_CallPathExp = Generalization(general=CallPathExp, specific=morel_FeaturePathExp)
gen_morel_OperationPathExp_CallPathExp = Generalization(general=CallPathExp, specific=morel_OperationPathExp)
gen_morel_LoopPathExp_CallPathExp = Generalization(general=CallPathExp, specific=morel_LoopPathExp)
gen_morel_IteratorPathExp_LoopPathExp = Generalization(general=LoopPathExp, specific=morel_IteratorPathExp)
gen_morel_LetExp_Expression = Generalization(general=Expression, specific=morel_LetExp)
gen_morel_LetExp_ImperativeExp = Generalization(general=ImperativeExp, specific=morel_LetExp)
gen_morel_VariableWithInit_Variable = Generalization(general=Variable, specific=morel_VariableWithInit)
gen_morel_ObjectVariableWithInit_ObjectVariable = Generalization(general=ObjectVariable, specific=morel_ObjectVariableWithInit)
gen_morel_ObjectVariableWithInit_VariableWithInit = Generalization(general=VariableWithInit, specific=morel_ObjectVariableWithInit)
gen_morel_PrimitiveVariableWithInit_PrimitiveVariable = Generalization(general=PrimitiveVariable, specific=morel_PrimitiveVariableWithInit)
gen_morel_PrimitiveVariableWithInit_VariableWithInit = Generalization(general=VariableWithInit, specific=morel_PrimitiveVariableWithInit)
gen_morel_ConditionExp_Expression = Generalization(general=Expression, specific=morel_ConditionExp)
gen_morel_BooleanImpliesExp_Expression = Generalization(general=Expression, specific=morel_BooleanImpliesExp)
gen_morel_BooleanImpliesExpChild_Expression = Generalization(general=Expression, specific=morel_BooleanImpliesExpChild)
gen_morel_BooleanOrExp_BooleanImpliesExpChild = Generalization(general=BooleanImpliesExpChild, specific=morel_BooleanOrExp)
gen_morel_BooleanOrExpChild_BooleanImpliesExpChild = Generalization(general=BooleanImpliesExpChild, specific=morel_BooleanOrExpChild)
gen_morel_BooleanAndExp_BooleanOrExpChild = Generalization(general=BooleanOrExpChild, specific=morel_BooleanAndExp)
gen_morel_BooleanAndExpChild_BooleanOrExpChild = Generalization(general=BooleanOrExpChild, specific=morel_BooleanAndExpChild)
gen_morel_UnaryExpChild_MultiplicativeExpChild = Generalization(general=MultiplicativeExpChild, specific=morel_UnaryExpChild)
gen_morel_RelationalExp_BooleanAndExpChild = Generalization(general=BooleanAndExpChild, specific=morel_RelationalExp)
gen_morel_RelationalExpChild_BooleanAndExpChild = Generalization(general=BooleanAndExpChild, specific=morel_RelationalExpChild)
gen_morel_AdditiveExp_RelationalExpChild = Generalization(general=RelationalExpChild, specific=morel_AdditiveExp)
gen_morel_AdditiveExpChild_RelationalExpChild = Generalization(general=RelationalExpChild, specific=morel_AdditiveExpChild)
gen_morel_MultiplicativeExp_AdditiveExpChild = Generalization(general=AdditiveExpChild, specific=morel_MultiplicativeExp)
gen_morel_MultiplicativeExpChild_AdditiveExpChild = Generalization(general=AdditiveExpChild, specific=morel_MultiplicativeExpChild)
gen_morel_UnaryExp_MultiplicativeExpChild = Generalization(general=MultiplicativeExpChild, specific=morel_UnaryExp)
gen_morel_CollectionType_EDataType = Generalization(general=EDataType, specific=morel_CollectionType)
gen_morel_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=morel_OrderedSetType)
gen_morel_SequenceType_CollectionType = Generalization(general=CollectionType, specific=morel_SequenceType)
gen_morel_SetType_CollectionType = Generalization(general=CollectionType, specific=morel_SetType)
gen_morel_BagType_CollectionType = Generalization(general=CollectionType, specific=morel_BagType)
gen_morel_ImperativeExp_Expression = Generalization(general=Expression, specific=morel_ImperativeExp)
gen_morel_BindExp_ImperativeExp = Generalization(general=ImperativeExp, specific=morel_BindExp)
gen_morel_PredefinedBindExp_ImperativeExp = Generalization(general=ImperativeExp, specific=morel_PredefinedBindExp)
gen_morel_IfStatement_ImperativeStatement = Generalization(general=ImperativeStatement, specific=morel_IfStatement)
gen_morel_ForStatement_ImperativeStatement = Generalization(general=ImperativeStatement, specific=morel_ForStatement)
gen_morel_BlockStatement_ImperativeStatement = Generalization(general=ImperativeStatement, specific=morel_BlockStatement)
gen_morel_TransformationModel_Unit = Generalization(general=Unit, specific=morel_TransformationModel)
gen_morel_TransformationModel_NamedElement = Generalization(general=NamedElement, specific=morel_TransformationModel)
gen_morel_RuleElement_NamedElement = Generalization(general=NamedElement, specific=morel_RuleElement)
gen_morel_RuleElement_Executable = Generalization(general=Executable, specific=morel_RuleElement)
gen_morel_Rule_RuleElement = Generalization(general=RuleElement, specific=morel_Rule)
gen_morel_RuleGroup_RuleElement = Generalization(general=RuleElement, specific=morel_RuleGroup)
gen_morel_DeclarativeStatement_Statement = Generalization(general=Statement, specific=morel_DeclarativeStatement)
gen_morel_ImperativeStatement_Statement = Generalization(general=Statement, specific=morel_ImperativeStatement)
gen_morel_ReflectiveVariableExp_Expression = Generalization(general=Expression, specific=morel_ReflectiveVariableExp)
gen_morel_ArrayLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=morel_ArrayLiteralExp)
gen_morel_OrderConstraint_AdditionalConstraint = Generalization(general=AdditionalConstraint, specific=morel_OrderConstraint)
gen_morel_AllDifferentConstraint_AdditionalConstraint = Generalization(general=AdditionalConstraint, specific=morel_AllDifferentConstraint)
gen_morel_MultiValueConstraint_PrimitiveConstraint = Generalization(general=PrimitiveConstraint, specific=morel_MultiValueConstraint)
gen_morel_ValueRangeConstraint_PrimitiveConstraint = Generalization(general=PrimitiveConstraint, specific=morel_ValueRangeConstraint)

# Domain Model
domain_model = DomainModel(
    name="morel",
    types={morel_NamedElement, morel_Section, morel_Pattern, Section, morel_ObjectVariable, morel_LinkConstraint, morel_Statement, morel_AdditionalConstraint, morel_Clause, morel_Variable, NamedElement, Variable, morel_EClass, morel_TypedModel, morel_PrimitiveVariable, morel_EDataType, morel_SimpleLinkConstraint, LinkConstraint, morel_Expression, morel_EReference, morel_EnclosureLinkConstraint, morel_PathConstraint, morel_LiteralExp, AtomicExp, morel_QueryModel, Unit, morel_Query, morel_EPackage, Pattern, Executable, morel_Unit, morel_AtomicExp, UnaryExpChild, morel_CallPathExp, morel_NestedExp, morel_StringLiteralExp, LiteralExp, morel_IntegerLiteralExp, morel_RealLiteralExp, morel_BooleanLiteralExp, morel_UndefinedLiteralExp, morel_CollectionLiteralExp, morel_EnumLiteralExp, morel_EEnum, morel_EEnumLiteral, morel_TypeLiteralExp, morel_EClassifier, morel_VariableExp, morel_PredefinedVariableExp, morel_FeaturePathExp, CallPathExp, morel_OperationPathExp, morel_LoopPathExp, morel_IteratorPathExp, LoopPathExp, morel_LetExp, Expression, ImperativeExp, morel_VariableWithInit, morel_ObjectVariableWithInit, ObjectVariable, VariableWithInit, morel_PrimitiveVariableWithInit, PrimitiveVariable, morel_ConditionExp, morel_BooleanImpliesExp, morel_BooleanImpliesExpChild, morel_BooleanOrExp, BooleanImpliesExpChild, morel_BooleanOrExpChild, morel_BooleanAndExp, BooleanOrExpChild, morel_BooleanAndExpChild, morel_RelationalExp, BooleanAndExpChild, morel_RelationalExpChild, morel_AdditiveExp, RelationalExpChild, morel_AdditiveExpChild, morel_MultiplicativeExp, AdditiveExpChild, morel_MultiplicativeExpChild, morel_UnaryExp, MultiplicativeExpChild, morel_UnaryExpChild, morel_CollectionType, EDataType, morel_OrderedSetType, CollectionType, morel_SequenceType, morel_SetType, morel_BagType, morel_ImperativeExp, morel_BindExp, morel_PredefinedBindExp, morel_IfStatement, ImperativeStatement, morel_ImperativeStatement, morel_ForStatement, morel_BlockStatement, morel_TransformationModel, morel_RuleElement, morel_Rule, RuleElement, morel_RuleGroup, morel_DeclarativeStatement, Statement, morel_ReflectiveVariableExp, morel_ArrayLiteralExp, morel_Executable, morel_OrderConstraint, AdditionalConstraint, morel_AllDifferentConstraint, morel_PrimitiveConstraint, morel_MultiValueConstraint, PrimitiveConstraint, morel_EAttribute, morel_ValueRangeConstraint, SectionType, TypedModelAction, UndefinedLiteral, PredefinedVariable, OperationSeparator, IteratorType, BooleanOperator, RelationalOperator, AdditiveOperator, MultiplicativeOperator, UnaryOperator, ScopeType, OrderType, IterationType, RepetitionType},
    associations={statements7, variables0, linkConstraints1, statements3, additionalConstraints5, type9, model11, type13, source14, target17, id20, reference21, forward23, types25, pathVariable28, references29, types32, queries35, package36, models38, dataTypes40, path43, literals44, enumType46, enumSymbol47, value49, referredVariable50, expression52, next55, parameters57, firstVar59, secondVar61, bodyExp64, variables67, inExp68, initExp71, condition74, thenBranch75, elseBranch78, left81, right83, children86, children87, left88, right89, children92, children93, child94, elementType95, source97, valueExp99, source102, valueExp103, condition106, thenStatement108, elseStatement110, iterator113, terminationExp115, stepExp118, bodyStatement121, statements124, rules126, patterns127, rules129, object152, expression131, variable133, elements135, primitiveVariables137, variables139, base142, references144, types147, variable150, attribute154, expression156},
    generalizations={gen_morel_Pattern_Section, gen_morel_Clause_Section, gen_morel_Variable_NamedElement, gen_morel_ObjectVariable_Variable, gen_morel_PrimitiveVariable_Variable, gen_morel_SimpleLinkConstraint_LinkConstraint, gen_morel_EnclosureLinkConstraint_LinkConstraint, gen_morel_PathConstraint_LinkConstraint, gen_morel_LiteralExp_AtomicExp, gen_morel_QueryModel_Unit, gen_morel_TypedModel_NamedElement, gen_morel_Query_Pattern, gen_morel_Query_NamedElement, gen_morel_Query_Executable, gen_morel_AtomicExp_UnaryExpChild, gen_morel_NestedExp_AtomicExp, gen_morel_StringLiteralExp_LiteralExp, gen_morel_IntegerLiteralExp_LiteralExp, gen_morel_RealLiteralExp_LiteralExp, gen_morel_BooleanLiteralExp_LiteralExp, gen_morel_UndefinedLiteralExp_LiteralExp, gen_morel_CollectionLiteralExp_LiteralExp, gen_morel_EnumLiteralExp_LiteralExp, gen_morel_TypeLiteralExp_LiteralExp, gen_morel_VariableExp_AtomicExp, gen_morel_PredefinedVariableExp_AtomicExp, gen_morel_FeaturePathExp_CallPathExp, gen_morel_OperationPathExp_CallPathExp, gen_morel_LoopPathExp_CallPathExp, gen_morel_IteratorPathExp_LoopPathExp, gen_morel_LetExp_Expression, gen_morel_LetExp_ImperativeExp, gen_morel_VariableWithInit_Variable, gen_morel_ObjectVariableWithInit_ObjectVariable, gen_morel_ObjectVariableWithInit_VariableWithInit, gen_morel_PrimitiveVariableWithInit_PrimitiveVariable, gen_morel_PrimitiveVariableWithInit_VariableWithInit, gen_morel_ConditionExp_Expression, gen_morel_BooleanImpliesExp_Expression, gen_morel_BooleanImpliesExpChild_Expression, gen_morel_BooleanOrExp_BooleanImpliesExpChild, gen_morel_BooleanOrExpChild_BooleanImpliesExpChild, gen_morel_BooleanAndExp_BooleanOrExpChild, gen_morel_BooleanAndExpChild_BooleanOrExpChild, gen_morel_UnaryExpChild_MultiplicativeExpChild, gen_morel_RelationalExp_BooleanAndExpChild, gen_morel_RelationalExpChild_BooleanAndExpChild, gen_morel_AdditiveExp_RelationalExpChild, gen_morel_AdditiveExpChild_RelationalExpChild, gen_morel_MultiplicativeExp_AdditiveExpChild, gen_morel_MultiplicativeExpChild_AdditiveExpChild, gen_morel_UnaryExp_MultiplicativeExpChild, gen_morel_CollectionType_EDataType, gen_morel_OrderedSetType_CollectionType, gen_morel_SequenceType_CollectionType, gen_morel_SetType_CollectionType, gen_morel_BagType_CollectionType, gen_morel_ImperativeExp_Expression, gen_morel_BindExp_ImperativeExp, gen_morel_PredefinedBindExp_ImperativeExp, gen_morel_IfStatement_ImperativeStatement, gen_morel_ForStatement_ImperativeStatement, gen_morel_BlockStatement_ImperativeStatement, gen_morel_TransformationModel_Unit, gen_morel_TransformationModel_NamedElement, gen_morel_RuleElement_NamedElement, gen_morel_RuleElement_Executable, gen_morel_Rule_RuleElement, gen_morel_RuleGroup_RuleElement, gen_morel_DeclarativeStatement_Statement, gen_morel_ImperativeStatement_Statement, gen_morel_ReflectiveVariableExp_Expression, gen_morel_ArrayLiteralExp_LiteralExp, gen_morel_OrderConstraint_AdditionalConstraint, gen_morel_AllDifferentConstraint_AdditionalConstraint, gen_morel_MultiValueConstraint_PrimitiveConstraint, gen_morel_ValueRangeConstraint_PrimitiveConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)