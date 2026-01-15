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
logiclanguage_Type = Class(name="logiclanguage::Type", is_abstract=True)
TypeDescriptor = Class(name="TypeDescriptor")
logiclanguage_DefinedElement = Class(name="logiclanguage::DefinedElement")
SymbolicDeclaration = Class(name="SymbolicDeclaration")
logiclanguage_TypeDefinition = Class(name="logiclanguage::TypeDefinition")
Type = Class(name="Type")
logiclanguage_TypeDeclaration = Class(name="logiclanguage::TypeDeclaration")
logiclanguage_TypeReference = Class(name="logiclanguage::TypeReference", is_abstract=True)
logiclanguage_ComplexTypeReference = Class(name="logiclanguage::ComplexTypeReference")
TypeReference = Class(name="TypeReference")
logiclanguage_PrimitiveTypeReference = Class(name="logiclanguage::PrimitiveTypeReference", is_abstract=True)
logiclanguage_IntTypeReference = Class(name="logiclanguage::IntTypeReference")
PrimitiveTypeReference = Class(name="PrimitiveTypeReference")
logiclanguage_BoolTypeReference = Class(name="logiclanguage::BoolTypeReference")
logiclanguage_RealTypeReference = Class(name="logiclanguage::RealTypeReference")
logiclanguage_Function = Class(name="logiclanguage::Function", is_abstract=True)
logiclanguage_FunctionAnnotation = Class(name="logiclanguage::FunctionAnnotation")
logiclanguage_Term = Class(name="logiclanguage::Term", is_abstract=True)
TermDescription = Class(name="TermDescription")
logiclanguage_SymbolicDeclaration = Class(name="logiclanguage::SymbolicDeclaration", is_abstract=True)
logiclanguage_SymbolicValue = Class(name="logiclanguage::SymbolicValue")
Term = Class(name="Term")
logiclanguage_AtomicTerm = Class(name="logiclanguage::AtomicTerm", is_abstract=True)
logiclanguage_IntLiteral = Class(name="logiclanguage::IntLiteral")
AtomicTerm = Class(name="AtomicTerm")
logiclanguage_BoolLiteral = Class(name="logiclanguage::BoolLiteral")
logiclanguage_RealLiteral = Class(name="logiclanguage::RealLiteral")
logiclanguage_Variable = Class(name="logiclanguage::Variable")
logiclanguage_QuantifiedExpression = Class(name="logiclanguage::QuantifiedExpression", is_abstract=True)
logiclanguage_Exists = Class(name="logiclanguage::Exists")
QuantifiedExpression = Class(name="QuantifiedExpression")
logiclanguage_Forall = Class(name="logiclanguage::Forall")
logiclanguage_BoolOperation = Class(name="logiclanguage::BoolOperation", is_abstract=True)
logiclanguage_And = Class(name="logiclanguage::And")
BoolOperation = Class(name="BoolOperation")
logiclanguage_Or = Class(name="logiclanguage::Or")
logiclanguage_Impl = Class(name="logiclanguage::Impl")
logiclanguage_Not = Class(name="logiclanguage::Not")
logiclanguage_Iff = Class(name="logiclanguage::Iff")
logiclanguage_PrimitiveRelation = Class(name="logiclanguage::PrimitiveRelation", is_abstract=True)
logiclanguage_Equals = Class(name="logiclanguage::Equals")
PrimitiveRelation = Class(name="PrimitiveRelation")
logiclanguage_TypeDescriptor = Class(name="logiclanguage::TypeDescriptor", is_abstract=True)
logiclanguage_TermDescription = Class(name="logiclanguage::TermDescription", is_abstract=True)
logiclanguage_Assertion = Class(name="logiclanguage::Assertion")
logiclanguage_LessThan = Class(name="logiclanguage::LessThan")
logiclanguage_AssertionAnnotation = Class(name="logiclanguage::AssertionAnnotation")
logiclanguage_Relation = Class(name="logiclanguage::Relation", is_abstract=True)
logiclanguage_MoreThan = Class(name="logiclanguage::MoreThan")
logiclanguage_RelationAnnotation = Class(name="logiclanguage::RelationAnnotation")
logiclanguage_Constant = Class(name="logiclanguage::Constant", is_abstract=True)
logiclanguage_LessOrEqualThan = Class(name="logiclanguage::LessOrEqualThan")
logiclanguage_MoreOrEqualThan = Class(name="logiclanguage::MoreOrEqualThan")
logiclanguage_NumericOperation = Class(name="logiclanguage::NumericOperation", is_abstract=True)
logiclanguage_Plus = Class(name="logiclanguage::Plus")
NumericOperation = Class(name="NumericOperation")
logiclanguage_Minus = Class(name="logiclanguage::Minus")
logiclanguage_Multiply = Class(name="logiclanguage::Multiply")
logiclanguage_Divison = Class(name="logiclanguage::Divison")
logiclanguage_Distinct = Class(name="logiclanguage::Distinct")
logiclanguage_Mod = Class(name="logiclanguage::Mod")
logiclanguage_FunctionDeclaration = Class(name="logiclanguage::FunctionDeclaration")
logiclanguage_IfThenElse = Class(name="logiclanguage::IfThenElse")
logiclanguage_ConstantAnnotation = Class(name="logiclanguage::ConstantAnnotation")
logiclanguage_ConstantDefinition = Class(name="logiclanguage::ConstantDefinition")
Constant = Class(name="Constant")
logiclanguage_ConstantDeclaration = Class(name="logiclanguage::ConstantDeclaration")
logiclanguage_RelationDefinition = Class(name="logiclanguage::RelationDefinition")
Relation = Class(name="Relation")
logiclanguage_RelationDeclaration = Class(name="logiclanguage::RelationDeclaration")
logiclanguage_FunctionDefinition = Class(name="logiclanguage::FunctionDefinition")
Function = Class(name="Function")
logiclanguage_Pow = Class(name="logiclanguage::Pow")
logiclanguage_AggregateExpression = Class(name="logiclanguage::AggregateExpression", is_abstract=True)
logiclanguage_AggregatedParameterSubstitution = Class(name="logiclanguage::AggregatedParameterSubstitution")
logiclanguage_Sum = Class(name="logiclanguage::Sum")
ProjectedAggregateExpression = Class(name="ProjectedAggregateExpression")
logiclanguage_Count = Class(name="logiclanguage::Count")
AggregateExpression = Class(name="AggregateExpression")
logiclanguage_Min = Class(name="logiclanguage::Min")
logiclanguage_Max = Class(name="logiclanguage::Max")
logiclanguage_ProjectedAggregateExpression = Class(name="logiclanguage::ProjectedAggregateExpression", is_abstract=True)
logiclanguage_UnknownBecauseUninterpreted = Class(name="logiclanguage::UnknownBecauseUninterpreted")
logiclanguage_InstanceOf = Class(name="logiclanguage::InstanceOf")
logiclanguage_StringTypeReference = Class(name="logiclanguage::StringTypeReference")
logiclanguage_StringLiteral = Class(name="logiclanguage::StringLiteral")
logiclanguage_TransitiveClosure = Class(name="logiclanguage::TransitiveClosure")

# logiclanguage_Type class attributes and methods
logiclanguage_Type_name: Property = Property(name="name", type=StringType)
logiclanguage_Type_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
logiclanguage_Type.attributes={logiclanguage_Type_isAbstract, logiclanguage_Type_name}

# TypeDescriptor class attributes and methods

# logiclanguage_DefinedElement class attributes and methods

# SymbolicDeclaration class attributes and methods

# logiclanguage_TypeDefinition class attributes and methods

# Type class attributes and methods

# logiclanguage_TypeDeclaration class attributes and methods

# logiclanguage_TypeReference class attributes and methods

# logiclanguage_ComplexTypeReference class attributes and methods

# TypeReference class attributes and methods

# logiclanguage_PrimitiveTypeReference class attributes and methods

# logiclanguage_IntTypeReference class attributes and methods

# PrimitiveTypeReference class attributes and methods

# logiclanguage_BoolTypeReference class attributes and methods

# logiclanguage_RealTypeReference class attributes and methods

# logiclanguage_Function class attributes and methods

# logiclanguage_FunctionAnnotation class attributes and methods

# logiclanguage_Term class attributes and methods

# TermDescription class attributes and methods

# logiclanguage_SymbolicDeclaration class attributes and methods
logiclanguage_SymbolicDeclaration_name: Property = Property(name="name", type=StringType)
logiclanguage_SymbolicDeclaration.attributes={logiclanguage_SymbolicDeclaration_name}

# logiclanguage_SymbolicValue class attributes and methods

# Term class attributes and methods

# logiclanguage_AtomicTerm class attributes and methods

# logiclanguage_IntLiteral class attributes and methods
logiclanguage_IntLiteral_value: Property = Property(name="value", type=IntegerType)
logiclanguage_IntLiteral.attributes={logiclanguage_IntLiteral_value}

# AtomicTerm class attributes and methods

# logiclanguage_BoolLiteral class attributes and methods
logiclanguage_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
logiclanguage_BoolLiteral.attributes={logiclanguage_BoolLiteral_value}

# logiclanguage_RealLiteral class attributes and methods
logiclanguage_RealLiteral_value: Property = Property(name="value", type=StringType)
logiclanguage_RealLiteral.attributes={logiclanguage_RealLiteral_value}

# logiclanguage_Variable class attributes and methods

# logiclanguage_QuantifiedExpression class attributes and methods

# logiclanguage_Exists class attributes and methods

# QuantifiedExpression class attributes and methods

# logiclanguage_Forall class attributes and methods

# logiclanguage_BoolOperation class attributes and methods

# logiclanguage_And class attributes and methods

# BoolOperation class attributes and methods

# logiclanguage_Or class attributes and methods

# logiclanguage_Impl class attributes and methods

# logiclanguage_Not class attributes and methods

# logiclanguage_Iff class attributes and methods

# logiclanguage_PrimitiveRelation class attributes and methods

# logiclanguage_Equals class attributes and methods

# PrimitiveRelation class attributes and methods

# logiclanguage_TypeDescriptor class attributes and methods

# logiclanguage_TermDescription class attributes and methods

# logiclanguage_Assertion class attributes and methods
logiclanguage_Assertion_name: Property = Property(name="name", type=StringType)
logiclanguage_Assertion.attributes={logiclanguage_Assertion_name}

# logiclanguage_LessThan class attributes and methods

# logiclanguage_AssertionAnnotation class attributes and methods

# logiclanguage_Relation class attributes and methods

# logiclanguage_MoreThan class attributes and methods

# logiclanguage_RelationAnnotation class attributes and methods

# logiclanguage_Constant class attributes and methods

# logiclanguage_LessOrEqualThan class attributes and methods

# logiclanguage_MoreOrEqualThan class attributes and methods

# logiclanguage_NumericOperation class attributes and methods

# logiclanguage_Plus class attributes and methods

# NumericOperation class attributes and methods

# logiclanguage_Minus class attributes and methods

# logiclanguage_Multiply class attributes and methods

# logiclanguage_Divison class attributes and methods

# logiclanguage_Distinct class attributes and methods

# logiclanguage_Mod class attributes and methods

# logiclanguage_FunctionDeclaration class attributes and methods

# logiclanguage_IfThenElse class attributes and methods

# logiclanguage_ConstantAnnotation class attributes and methods

# logiclanguage_ConstantDefinition class attributes and methods

# Constant class attributes and methods

# logiclanguage_ConstantDeclaration class attributes and methods

# logiclanguage_RelationDefinition class attributes and methods

# Relation class attributes and methods

# logiclanguage_RelationDeclaration class attributes and methods

# logiclanguage_FunctionDefinition class attributes and methods

# Function class attributes and methods

# logiclanguage_Pow class attributes and methods

# logiclanguage_AggregateExpression class attributes and methods

# logiclanguage_AggregatedParameterSubstitution class attributes and methods

# logiclanguage_Sum class attributes and methods

# ProjectedAggregateExpression class attributes and methods

# logiclanguage_Count class attributes and methods

# AggregateExpression class attributes and methods

# logiclanguage_Min class attributes and methods

# logiclanguage_Max class attributes and methods

# logiclanguage_ProjectedAggregateExpression class attributes and methods
logiclanguage_ProjectedAggregateExpression_projectionIndex: Property = Property(name="projectionIndex", type=IntegerType)
logiclanguage_ProjectedAggregateExpression.attributes={logiclanguage_ProjectedAggregateExpression_projectionIndex}

# logiclanguage_UnknownBecauseUninterpreted class attributes and methods

# logiclanguage_InstanceOf class attributes and methods

# logiclanguage_StringTypeReference class attributes and methods

# logiclanguage_StringLiteral class attributes and methods
logiclanguage_StringLiteral_value: Property = Property(name="value", type=StringType)
logiclanguage_StringLiteral.attributes={logiclanguage_StringLiteral_value}

# logiclanguage_TransitiveClosure class attributes and methods

# Relationships
subtypes1: BinaryAssociation = BinaryAssociation(
    name="subtypes1",
    ends={
        Property(name="Type", type=logiclanguage_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="supertypes", type=logiclanguage_Type, multiplicity=Multiplicity(0, 9999))
    }
)
supertypes3: BinaryAssociation = BinaryAssociation(
    name="supertypes3",
    ends={
        Property(name="Type4", type=logiclanguage_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="subtypes", type=logiclanguage_Type, multiplicity=Multiplicity(0, 9999))
    }
)
definedInType5: BinaryAssociation = BinaryAssociation(
    name="definedInType5",
    ends={
        Property(name="TypeDefinition", type=logiclanguage_DefinedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=logiclanguage_TypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="DefinedElement", type=logiclanguage_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definedInType", type=logiclanguage_DefinedElement, multiplicity=Multiplicity(0, 9999))
    }
)
defines7: BinaryAssociation = BinaryAssociation(
    name="defines7",
    ends={
        Property(name="logiclanguage_TypeDeclaration", type=logiclanguage_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_TypeDefinition", type=logiclanguage_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
range9: BinaryAssociation = BinaryAssociation(
    name="range9",
    ends={
        Property(name="logiclanguage_TypeReference", type=logiclanguage_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Function", type=logiclanguage_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="logiclanguage_TypeReference12", type=logiclanguage_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Function11", type=logiclanguage_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations13: BinaryAssociation = BinaryAssociation(
    name="annotations13",
    ends={
        Property(name="logicproblem.ecoreFunctionAnnotation", type=logiclanguage_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=logiclanguage_FunctionAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
symbolicReference14: BinaryAssociation = BinaryAssociation(
    name="symbolicReference14",
    ends={
        Property(name="logiclanguage_SymbolicDeclaration", type=logiclanguage_SymbolicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_SymbolicValue", type=logiclanguage_SymbolicDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
parameterSubstitutions15: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitutions15",
    ends={
        Property(name="logiclanguage_Term", type=logiclanguage_SymbolicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_SymbolicValue16", type=logiclanguage_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range17: BinaryAssociation = BinaryAssociation(
    name="range17",
    ends={
        Property(name="logiclanguage_TypeReference18", type=logiclanguage_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Variable", type=logiclanguage_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referred8: BinaryAssociation = BinaryAssociation(
    name="referred8",
    ends={
        Property(name="logiclanguage_Type", type=logiclanguage_ComplexTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_ComplexTypeReference", type=logiclanguage_Type, multiplicity=Multiplicity(0, 1))
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="logiclanguage_Term23", type=logiclanguage_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_QuantifiedExpression22", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands24: BinaryAssociation = BinaryAssociation(
    name="operands24",
    ends={
        Property(name="logiclanguage_Term25", type=logiclanguage_And, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_And", type=logiclanguage_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands26: BinaryAssociation = BinaryAssociation(
    name="operands26",
    ends={
        Property(name="logiclanguage_Term27", type=logiclanguage_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Or", type=logiclanguage_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand28: BinaryAssociation = BinaryAssociation(
    name="leftOperand28",
    ends={
        Property(name="logiclanguage_Term29", type=logiclanguage_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Impl", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand30: BinaryAssociation = BinaryAssociation(
    name="rightOperand30",
    ends={
        Property(name="logiclanguage_Term32", type=logiclanguage_Impl, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Impl31", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand33: BinaryAssociation = BinaryAssociation(
    name="operand33",
    ends={
        Property(name="logiclanguage_Term34", type=logiclanguage_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Not", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand35: BinaryAssociation = BinaryAssociation(
    name="leftOperand35",
    ends={
        Property(name="logiclanguage_Term36", type=logiclanguage_Iff, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Iff", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand37: BinaryAssociation = BinaryAssociation(
    name="rightOperand37",
    ends={
        Property(name="logiclanguage_Term39", type=logiclanguage_Iff, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Iff38", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand40: BinaryAssociation = BinaryAssociation(
    name="leftOperand40",
    ends={
        Property(name="logiclanguage_Term41", type=logiclanguage_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Equals", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand42: BinaryAssociation = BinaryAssociation(
    name="rightOperand42",
    ends={
        Property(name="logiclanguage_Term44", type=logiclanguage_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Equals43", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quantifiedVariables19: BinaryAssociation = BinaryAssociation(
    name="quantifiedVariables19",
    ends={
        Property(name="logiclanguage_Variable20", type=logiclanguage_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_QuantifiedExpression", type=logiclanguage_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands45: BinaryAssociation = BinaryAssociation(
    name="operands45",
    ends={
        Property(name="logiclanguage_Term46", type=logiclanguage_Distinct, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Distinct", type=logiclanguage_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value72: BinaryAssociation = BinaryAssociation(
    name="value72",
    ends={
        Property(name="logiclanguage_Term73", type=logiclanguage_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Assertion", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand47: BinaryAssociation = BinaryAssociation(
    name="leftOperand47",
    ends={
        Property(name="logiclanguage_Term48", type=logiclanguage_LessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_LessThan", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand49: BinaryAssociation = BinaryAssociation(
    name="rightOperand49",
    ends={
        Property(name="logiclanguage_Term51", type=logiclanguage_LessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_LessThan50", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations74: BinaryAssociation = BinaryAssociation(
    name="annotations74",
    ends={
        Property(name="logicproblem.ecoreAssertionAnnotation", type=logiclanguage_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="target75", type=logiclanguage_AssertionAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
parameters76: BinaryAssociation = BinaryAssociation(
    name="parameters76",
    ends={
        Property(name="logiclanguage_TypeReference77", type=logiclanguage_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Relation", type=logiclanguage_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand52: BinaryAssociation = BinaryAssociation(
    name="leftOperand52",
    ends={
        Property(name="logiclanguage_Term53", type=logiclanguage_MoreThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_MoreThan", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand54: BinaryAssociation = BinaryAssociation(
    name="rightOperand54",
    ends={
        Property(name="logiclanguage_Term56", type=logiclanguage_MoreThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_MoreThan55", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations78: BinaryAssociation = BinaryAssociation(
    name="annotations78",
    ends={
        Property(name="logicproblem.ecoreRelationAnnotation", type=logiclanguage_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="target79", type=logiclanguage_RelationAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="logiclanguage_TypeReference81", type=logiclanguage_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_Constant", type=logiclanguage_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand57: BinaryAssociation = BinaryAssociation(
    name="leftOperand57",
    ends={
        Property(name="logiclanguage_Term58", type=logiclanguage_LessOrEqualThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_LessOrEqualThan", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand59: BinaryAssociation = BinaryAssociation(
    name="rightOperand59",
    ends={
        Property(name="logiclanguage_Term61", type=logiclanguage_LessOrEqualThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_LessOrEqualThan60", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand62: BinaryAssociation = BinaryAssociation(
    name="leftOperand62",
    ends={
        Property(name="logiclanguage_Term63", type=logiclanguage_MoreOrEqualThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_MoreOrEqualThan", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand64: BinaryAssociation = BinaryAssociation(
    name="rightOperand64",
    ends={
        Property(name="logiclanguage_Term66", type=logiclanguage_MoreOrEqualThan, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_MoreOrEqualThan65", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand67: BinaryAssociation = BinaryAssociation(
    name="leftOperand67",
    ends={
        Property(name="logiclanguage_Term68", type=logiclanguage_NumericOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_NumericOperation", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand69: BinaryAssociation = BinaryAssociation(
    name="rightOperand69",
    ends={
        Property(name="logiclanguage_Term71", type=logiclanguage_NumericOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_NumericOperation70", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defines97: BinaryAssociation = BinaryAssociation(
    name="defines97",
    ends={
        Property(name="logiclanguage_FunctionDeclaration", type=logiclanguage_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_FunctionDefinition98", type=logiclanguage_FunctionDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="logiclanguage_Term101", type=logiclanguage_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_FunctionDefinition100", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition102: BinaryAssociation = BinaryAssociation(
    name="condition102",
    ends={
        Property(name="logiclanguage_Term103", type=logiclanguage_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_IfThenElse", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifTrue104: BinaryAssociation = BinaryAssociation(
    name="ifTrue104",
    ends={
        Property(name="logiclanguage_Term106", type=logiclanguage_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_IfThenElse105", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalse107: BinaryAssociation = BinaryAssociation(
    name="ifFalse107",
    ends={
        Property(name="logiclanguage_Term109", type=logiclanguage_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_IfThenElse108", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations82: BinaryAssociation = BinaryAssociation(
    name="annotations82",
    ends={
        Property(name="logicproblem.ecoreConstantAnnotation", type=logiclanguage_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="target83", type=logiclanguage_ConstantAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="logiclanguage_Term85", type=logiclanguage_ConstantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_ConstantDefinition", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defines86: BinaryAssociation = BinaryAssociation(
    name="defines86",
    ends={
        Property(name="logiclanguage_ConstantDeclaration", type=logiclanguage_ConstantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_ConstantDefinition87", type=logiclanguage_ConstantDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variables88: BinaryAssociation = BinaryAssociation(
    name="variables88",
    ends={
        Property(name="logiclanguage_Variable89", type=logiclanguage_RelationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_RelationDefinition", type=logiclanguage_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="logiclanguage_Term92", type=logiclanguage_RelationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_RelationDefinition91", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defines93: BinaryAssociation = BinaryAssociation(
    name="defines93",
    ends={
        Property(name="logiclanguage_RelationDeclaration", type=logiclanguage_RelationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_RelationDefinition94", type=logiclanguage_RelationDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variable95: BinaryAssociation = BinaryAssociation(
    name="variable95",
    ends={
        Property(name="logiclanguage_Variable96", type=logiclanguage_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_FunctionDefinition", type=logiclanguage_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation120: BinaryAssociation = BinaryAssociation(
    name="relation120",
    ends={
        Property(name="logiclanguage_TransitiveClosure121", type=logiclanguage_Relation, multiplicity=Multiplicity(0, 1)),
        Property(name="logiclanguage_Relation122", type=logiclanguage_TransitiveClosure, multiplicity=Multiplicity(1, 1))
    }
)
relation123: BinaryAssociation = BinaryAssociation(
    name="relation123",
    ends={
        Property(name="logiclanguage_Relation124", type=logiclanguage_AggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_AggregateExpression", type=logiclanguage_Relation, multiplicity=Multiplicity(0, 1))
    }
)
parameterSubstitution125: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution125",
    ends={
        Property(name="logiclanguage_AggregatedParameterSubstitution", type=logiclanguage_AggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_AggregateExpression126", type=logiclanguage_AggregatedParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable127: BinaryAssociation = BinaryAssociation(
    name="resultVariable127",
    ends={
        Property(name="logiclanguage_Variable129", type=logiclanguage_AggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_AggregateExpression128", type=logiclanguage_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value110: BinaryAssociation = BinaryAssociation(
    name="value110",
    ends={
        Property(name="logiclanguage_Term111", type=logiclanguage_InstanceOf, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_InstanceOf", type=logiclanguage_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range112: BinaryAssociation = BinaryAssociation(
    name="range112",
    ends={
        Property(name="logiclanguage_TypeReference114", type=logiclanguage_InstanceOf, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_InstanceOf113", type=logiclanguage_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand115: BinaryAssociation = BinaryAssociation(
    name="leftOperand115",
    ends={
        Property(name="logiclanguage_Term116", type=logiclanguage_TransitiveClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_TransitiveClosure", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand117: BinaryAssociation = BinaryAssociation(
    name="rightOperand117",
    ends={
        Property(name="logiclanguage_Term119", type=logiclanguage_TransitiveClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_TransitiveClosure118", type=logiclanguage_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable130: BinaryAssociation = BinaryAssociation(
    name="variable130",
    ends={
        Property(name="logiclanguage_Variable132", type=logiclanguage_AggregatedParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="logiclanguage_AggregatedParameterSubstitution131", type=logiclanguage_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_logiclanguage_Type_TypeDescriptor = Generalization(general=TypeDescriptor, specific=logiclanguage_Type)
gen_logiclanguage_DefinedElement_SymbolicDeclaration = Generalization(general=SymbolicDeclaration, specific=logiclanguage_DefinedElement)
gen_logiclanguage_TypeDefinition_Type = Generalization(general=Type, specific=logiclanguage_TypeDefinition)
gen_logiclanguage_TypeReference_TypeDescriptor = Generalization(general=TypeDescriptor, specific=logiclanguage_TypeReference)
gen_logiclanguage_ComplexTypeReference_TypeReference = Generalization(general=TypeReference, specific=logiclanguage_ComplexTypeReference)
gen_logiclanguage_PrimitiveTypeReference_TypeReference = Generalization(general=TypeReference, specific=logiclanguage_PrimitiveTypeReference)
gen_logiclanguage_IntTypeReference_PrimitiveTypeReference = Generalization(general=PrimitiveTypeReference, specific=logiclanguage_IntTypeReference)
gen_logiclanguage_BoolTypeReference_PrimitiveTypeReference = Generalization(general=PrimitiveTypeReference, specific=logiclanguage_BoolTypeReference)
gen_logiclanguage_RealTypeReference_PrimitiveTypeReference = Generalization(general=PrimitiveTypeReference, specific=logiclanguage_RealTypeReference)
gen_logiclanguage_Function_SymbolicDeclaration = Generalization(general=SymbolicDeclaration, specific=logiclanguage_Function)
gen_logiclanguage_Term_TermDescription = Generalization(general=TermDescription, specific=logiclanguage_Term)
gen_logiclanguage_SymbolicDeclaration_TermDescription = Generalization(general=TermDescription, specific=logiclanguage_SymbolicDeclaration)
gen_logiclanguage_SymbolicValue_Term = Generalization(general=Term, specific=logiclanguage_SymbolicValue)
gen_logiclanguage_AtomicTerm_Term = Generalization(general=Term, specific=logiclanguage_AtomicTerm)
gen_logiclanguage_IntLiteral_AtomicTerm = Generalization(general=AtomicTerm, specific=logiclanguage_IntLiteral)
gen_logiclanguage_BoolLiteral_AtomicTerm = Generalization(general=AtomicTerm, specific=logiclanguage_BoolLiteral)
gen_logiclanguage_RealLiteral_AtomicTerm = Generalization(general=AtomicTerm, specific=logiclanguage_RealLiteral)
gen_logiclanguage_Variable_SymbolicDeclaration = Generalization(general=SymbolicDeclaration, specific=logiclanguage_Variable)
gen_logiclanguage_QuantifiedExpression_Term = Generalization(general=Term, specific=logiclanguage_QuantifiedExpression)
gen_logiclanguage_Exists_QuantifiedExpression = Generalization(general=QuantifiedExpression, specific=logiclanguage_Exists)
gen_logiclanguage_Forall_QuantifiedExpression = Generalization(general=QuantifiedExpression, specific=logiclanguage_Forall)
gen_logiclanguage_BoolOperation_Term = Generalization(general=Term, specific=logiclanguage_BoolOperation)
gen_logiclanguage_And_BoolOperation = Generalization(general=BoolOperation, specific=logiclanguage_And)
gen_logiclanguage_Or_BoolOperation = Generalization(general=BoolOperation, specific=logiclanguage_Or)
gen_logiclanguage_Impl_BoolOperation = Generalization(general=BoolOperation, specific=logiclanguage_Impl)
gen_logiclanguage_Not_BoolOperation = Generalization(general=BoolOperation, specific=logiclanguage_Not)
gen_logiclanguage_Iff_BoolOperation = Generalization(general=BoolOperation, specific=logiclanguage_Iff)
gen_logiclanguage_PrimitiveRelation_Term = Generalization(general=Term, specific=logiclanguage_PrimitiveRelation)
gen_logiclanguage_Equals_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_Equals)
gen_logiclanguage_LessThan_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_LessThan)
gen_logiclanguage_Relation_SymbolicDeclaration = Generalization(general=SymbolicDeclaration, specific=logiclanguage_Relation)
gen_logiclanguage_MoreThan_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_MoreThan)
gen_logiclanguage_Constant_SymbolicDeclaration = Generalization(general=SymbolicDeclaration, specific=logiclanguage_Constant)
gen_logiclanguage_LessOrEqualThan_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_LessOrEqualThan)
gen_logiclanguage_MoreOrEqualThan_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_MoreOrEqualThan)
gen_logiclanguage_NumericOperation_Term = Generalization(general=Term, specific=logiclanguage_NumericOperation)
gen_logiclanguage_Plus_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Plus)
gen_logiclanguage_Minus_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Minus)
gen_logiclanguage_Multiply_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Multiply)
gen_logiclanguage_Divison_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Divison)
gen_logiclanguage_Mod_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Mod)
gen_logiclanguage_Distinct_PrimitiveRelation = Generalization(general=PrimitiveRelation, specific=logiclanguage_Distinct)
gen_logiclanguage_IfThenElse_Term = Generalization(general=Term, specific=logiclanguage_IfThenElse)
gen_logiclanguage_ConstantDeclaration_Constant = Generalization(general=Constant, specific=logiclanguage_ConstantDeclaration)
gen_logiclanguage_RelationDeclaration_Relation = Generalization(general=Relation, specific=logiclanguage_RelationDeclaration)
gen_logiclanguage_ConstantDefinition_Constant = Generalization(general=Constant, specific=logiclanguage_ConstantDefinition)
gen_logiclanguage_RelationDefinition_Relation = Generalization(general=Relation, specific=logiclanguage_RelationDefinition)
gen_logiclanguage_FunctionDefinition_Function = Generalization(general=Function, specific=logiclanguage_FunctionDefinition)
gen_logiclanguage_Pow_NumericOperation = Generalization(general=NumericOperation, specific=logiclanguage_Pow)
gen_logiclanguage_AggregateExpression_Term = Generalization(general=Term, specific=logiclanguage_AggregateExpression)
gen_logiclanguage_Sum_ProjectedAggregateExpression = Generalization(general=ProjectedAggregateExpression, specific=logiclanguage_Sum)
gen_logiclanguage_Count_AggregateExpression = Generalization(general=AggregateExpression, specific=logiclanguage_Count)
gen_logiclanguage_Min_ProjectedAggregateExpression = Generalization(general=ProjectedAggregateExpression, specific=logiclanguage_Min)
gen_logiclanguage_Max_ProjectedAggregateExpression = Generalization(general=ProjectedAggregateExpression, specific=logiclanguage_Max)
gen_logiclanguage_ProjectedAggregateExpression_AggregateExpression = Generalization(general=AggregateExpression, specific=logiclanguage_ProjectedAggregateExpression)
gen_logiclanguage_FunctionDeclaration_Function = Generalization(general=Function, specific=logiclanguage_FunctionDeclaration)
gen_logiclanguage_TypeDeclaration_Type = Generalization(general=Type, specific=logiclanguage_TypeDeclaration)
gen_logiclanguage_UnknownBecauseUninterpreted_Term = Generalization(general=Term, specific=logiclanguage_UnknownBecauseUninterpreted)
gen_logiclanguage_InstanceOf_Term = Generalization(general=Term, specific=logiclanguage_InstanceOf)
gen_logiclanguage_StringTypeReference_PrimitiveTypeReference = Generalization(general=PrimitiveTypeReference, specific=logiclanguage_StringTypeReference)
gen_logiclanguage_StringLiteral_AtomicTerm = Generalization(general=AtomicTerm, specific=logiclanguage_StringLiteral)
gen_logiclanguage_TransitiveClosure_Term = Generalization(general=Term, specific=logiclanguage_TransitiveClosure)

# Domain Model
domain_model = DomainModel(
    name="logiclanguage",
    types={logiclanguage_Type, TypeDescriptor, logiclanguage_DefinedElement, SymbolicDeclaration, logiclanguage_TypeDefinition, Type, logiclanguage_TypeDeclaration, logiclanguage_TypeReference, logiclanguage_ComplexTypeReference, TypeReference, logiclanguage_PrimitiveTypeReference, logiclanguage_IntTypeReference, PrimitiveTypeReference, logiclanguage_BoolTypeReference, logiclanguage_RealTypeReference, logiclanguage_Function, logiclanguage_FunctionAnnotation, logiclanguage_Term, TermDescription, logiclanguage_SymbolicDeclaration, logiclanguage_SymbolicValue, Term, logiclanguage_AtomicTerm, logiclanguage_IntLiteral, AtomicTerm, logiclanguage_BoolLiteral, logiclanguage_RealLiteral, logiclanguage_Variable, logiclanguage_QuantifiedExpression, logiclanguage_Exists, QuantifiedExpression, logiclanguage_Forall, logiclanguage_BoolOperation, logiclanguage_And, BoolOperation, logiclanguage_Or, logiclanguage_Impl, logiclanguage_Not, logiclanguage_Iff, logiclanguage_PrimitiveRelation, logiclanguage_Equals, PrimitiveRelation, logiclanguage_TypeDescriptor, logiclanguage_TermDescription, logiclanguage_Assertion, logiclanguage_LessThan, logiclanguage_AssertionAnnotation, logiclanguage_Relation, logiclanguage_MoreThan, logiclanguage_RelationAnnotation, logiclanguage_Constant, logiclanguage_LessOrEqualThan, logiclanguage_MoreOrEqualThan, logiclanguage_NumericOperation, logiclanguage_Plus, NumericOperation, logiclanguage_Minus, logiclanguage_Multiply, logiclanguage_Divison, logiclanguage_Distinct, logiclanguage_Mod, logiclanguage_FunctionDeclaration, logiclanguage_IfThenElse, logiclanguage_ConstantAnnotation, logiclanguage_ConstantDefinition, Constant, logiclanguage_ConstantDeclaration, logiclanguage_RelationDefinition, Relation, logiclanguage_RelationDeclaration, logiclanguage_FunctionDefinition, Function, logiclanguage_Pow, logiclanguage_AggregateExpression, logiclanguage_AggregatedParameterSubstitution, logiclanguage_Sum, ProjectedAggregateExpression, logiclanguage_Count, AggregateExpression, logiclanguage_Min, logiclanguage_Max, logiclanguage_ProjectedAggregateExpression, logiclanguage_UnknownBecauseUninterpreted, logiclanguage_InstanceOf, logiclanguage_StringTypeReference, logiclanguage_StringLiteral, logiclanguage_TransitiveClosure},
    associations={subtypes1, supertypes3, definedInType5, elements6, defines7, range9, parameters10, annotations13, symbolicReference14, parameterSubstitutions15, range17, referred8, expression21, operands24, operands26, leftOperand28, rightOperand30, operand33, leftOperand35, rightOperand37, leftOperand40, rightOperand42, quantifiedVariables19, operands45, value72, leftOperand47, rightOperand49, annotations74, parameters76, leftOperand52, rightOperand54, annotations78, type80, leftOperand57, rightOperand59, leftOperand62, rightOperand64, leftOperand67, rightOperand69, defines97, value99, condition102, ifTrue104, ifFalse107, annotations82, value84, defines86, variables88, value90, defines93, variable95, relation120, relation123, parameterSubstitution125, resultVariable127, value110, range112, leftOperand115, rightOperand117, variable130},
    generalizations={gen_logiclanguage_Type_TypeDescriptor, gen_logiclanguage_DefinedElement_SymbolicDeclaration, gen_logiclanguage_TypeDefinition_Type, gen_logiclanguage_TypeReference_TypeDescriptor, gen_logiclanguage_ComplexTypeReference_TypeReference, gen_logiclanguage_PrimitiveTypeReference_TypeReference, gen_logiclanguage_IntTypeReference_PrimitiveTypeReference, gen_logiclanguage_BoolTypeReference_PrimitiveTypeReference, gen_logiclanguage_RealTypeReference_PrimitiveTypeReference, gen_logiclanguage_Function_SymbolicDeclaration, gen_logiclanguage_Term_TermDescription, gen_logiclanguage_SymbolicDeclaration_TermDescription, gen_logiclanguage_SymbolicValue_Term, gen_logiclanguage_AtomicTerm_Term, gen_logiclanguage_IntLiteral_AtomicTerm, gen_logiclanguage_BoolLiteral_AtomicTerm, gen_logiclanguage_RealLiteral_AtomicTerm, gen_logiclanguage_Variable_SymbolicDeclaration, gen_logiclanguage_QuantifiedExpression_Term, gen_logiclanguage_Exists_QuantifiedExpression, gen_logiclanguage_Forall_QuantifiedExpression, gen_logiclanguage_BoolOperation_Term, gen_logiclanguage_And_BoolOperation, gen_logiclanguage_Or_BoolOperation, gen_logiclanguage_Impl_BoolOperation, gen_logiclanguage_Not_BoolOperation, gen_logiclanguage_Iff_BoolOperation, gen_logiclanguage_PrimitiveRelation_Term, gen_logiclanguage_Equals_PrimitiveRelation, gen_logiclanguage_LessThan_PrimitiveRelation, gen_logiclanguage_Relation_SymbolicDeclaration, gen_logiclanguage_MoreThan_PrimitiveRelation, gen_logiclanguage_Constant_SymbolicDeclaration, gen_logiclanguage_LessOrEqualThan_PrimitiveRelation, gen_logiclanguage_MoreOrEqualThan_PrimitiveRelation, gen_logiclanguage_NumericOperation_Term, gen_logiclanguage_Plus_NumericOperation, gen_logiclanguage_Minus_NumericOperation, gen_logiclanguage_Multiply_NumericOperation, gen_logiclanguage_Divison_NumericOperation, gen_logiclanguage_Mod_NumericOperation, gen_logiclanguage_Distinct_PrimitiveRelation, gen_logiclanguage_IfThenElse_Term, gen_logiclanguage_ConstantDeclaration_Constant, gen_logiclanguage_RelationDeclaration_Relation, gen_logiclanguage_ConstantDefinition_Constant, gen_logiclanguage_RelationDefinition_Relation, gen_logiclanguage_FunctionDefinition_Function, gen_logiclanguage_Pow_NumericOperation, gen_logiclanguage_AggregateExpression_Term, gen_logiclanguage_Sum_ProjectedAggregateExpression, gen_logiclanguage_Count_AggregateExpression, gen_logiclanguage_Min_ProjectedAggregateExpression, gen_logiclanguage_Max_ProjectedAggregateExpression, gen_logiclanguage_ProjectedAggregateExpression_AggregateExpression, gen_logiclanguage_FunctionDeclaration_Function, gen_logiclanguage_TypeDeclaration_Type, gen_logiclanguage_UnknownBecauseUninterpreted_Term, gen_logiclanguage_InstanceOf_Term, gen_logiclanguage_StringTypeReference_PrimitiveTypeReference, gen_logiclanguage_StringLiteral_AtomicTerm, gen_logiclanguage_TransitiveClosure_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)