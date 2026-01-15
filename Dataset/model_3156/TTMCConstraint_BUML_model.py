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
TTMCConstraint_NamedElement = Class(name="TTMCConstraint::NamedElement", is_abstract=True)
TTMCConstraint_ParametricElement = Class(name="TTMCConstraint::ParametricElement", is_abstract=True)
TTMCConstraint_ParameterDeclaration = Class(name="TTMCConstraint::ParameterDeclaration")
TTMCConstraint_ParametrizedElement = Class(name="TTMCConstraint::ParametrizedElement")
TTMCConstraint_Expression = Class(name="TTMCConstraint::Expression", is_abstract=True)
TTMCConstraint_ConstraintSpecification = Class(name="TTMCConstraint::ConstraintSpecification")
NamedElement = Class(name="NamedElement")
ParametricElement = Class(name="ParametricElement")
TTMCConstraint_TypeDeclaration = Class(name="TTMCConstraint::TypeDeclaration")
TTMCConstraint_ConstantDeclaration = Class(name="TTMCConstraint::ConstantDeclaration")
TTMCConstraint_FunctionDeclaration = Class(name="TTMCConstraint::FunctionDeclaration")
TTMCConstraint_BasicConstraintDefinition = Class(name="TTMCConstraint::BasicConstraintDefinition")
TTMCConstraint_Declaration = Class(name="TTMCConstraint::Declaration", is_abstract=True)
TTMCConstraint_Type = Class(name="TTMCConstraint::Type")
TTMCConstraint_DefinableDeclaration = Class(name="TTMCConstraint::DefinableDeclaration", is_abstract=True)
Declaration = Class(name="Declaration")
TTMCConstraint_FieldDeclaration = Class(name="TTMCConstraint::FieldDeclaration")
TTMCConstraint_LetDeclaration = Class(name="TTMCConstraint::LetDeclaration")
DefinableDeclaration = Class(name="DefinableDeclaration")
TTMCConstraint_TypeReference = Class(name="TTMCConstraint::TypeReference")
Type = Class(name="Type")
TTMCConstraint_TypeDefinition = Class(name="TTMCConstraint::TypeDefinition")
TTMCConstraint_BasicTypeDefinition = Class(name="TTMCConstraint::BasicTypeDefinition", is_abstract=True)
TypeDefinition = Class(name="TypeDefinition")
TTMCConstraint_IntegerTypeDefinition = Class(name="TTMCConstraint::IntegerTypeDefinition")
BasicTypeDefinition = Class(name="BasicTypeDefinition")
TTMCConstraint_NaturalTypeDefinition = Class(name="TTMCConstraint::NaturalTypeDefinition")
TTMCConstraint_BooleanTypeDefinition = Class(name="TTMCConstraint::BooleanTypeDefinition")
TTMCConstraint_RealTypeDefinition = Class(name="TTMCConstraint::RealTypeDefinition")
TTMCConstraint_SubrangeTypeDefinition = Class(name="TTMCConstraint::SubrangeTypeDefinition")
TTMCConstraint_RecordTypeDefinition = Class(name="TTMCConstraint::RecordTypeDefinition")
TTMCConstraint_SubTypeDefinition = Class(name="TTMCConstraint::SubTypeDefinition")
TTMCConstraint_EnumerationTypeDefinition = Class(name="TTMCConstraint::EnumerationTypeDefinition")
TTMCConstraint_EnumerationLiteralDefinition = Class(name="TTMCConstraint::EnumerationLiteralDefinition")
TTMCConstraint_FunctionTypeDefinition = Class(name="TTMCConstraint::FunctionTypeDefinition")
TTMCConstraint_ArrayTypeDefinition = Class(name="TTMCConstraint::ArrayTypeDefinition")
TTMCConstraint_TupleTypeDefinition = Class(name="TTMCConstraint::TupleTypeDefinition")
TTMCConstraint_BooleanExpression = Class(name="TTMCConstraint::BooleanExpression", is_abstract=True)
TTMCConstraint_ConstraintDefinition = Class(name="TTMCConstraint::ConstraintDefinition", is_abstract=True)
ConstraintDefinition = Class(name="ConstraintDefinition")
TTMCConstraint_NullaryExpression = Class(name="TTMCConstraint::NullaryExpression", is_abstract=True)
Expression = Class(name="Expression")
TTMCConstraint_UnaryExpression = Class(name="TTMCConstraint::UnaryExpression", is_abstract=True)
TTMCConstraint_BinaryExpression = Class(name="TTMCConstraint::BinaryExpression", is_abstract=True)
TTMCConstraint_MultiaryExpression = Class(name="TTMCConstraint::MultiaryExpression", is_abstract=True)
TTMCConstraint_PredicateExpression = Class(name="TTMCConstraint::PredicateExpression", is_abstract=True)
TTMCConstraint_ArithmeticExpression = Class(name="TTMCConstraint::ArithmeticExpression", is_abstract=True)
TTMCConstraint_AccessExpression = Class(name="TTMCConstraint::AccessExpression", is_abstract=True)
TTMCConstraint_QuantifierExpression = Class(name="TTMCConstraint::QuantifierExpression", is_abstract=True)
UnaryExpression = Class(name="UnaryExpression")
TTMCConstraint_TemporalExpression = Class(name="TTMCConstraint::TemporalExpression", is_abstract=True)
TTMCConstraint_TemporalPathExpression = Class(name="TTMCConstraint::TemporalPathExpression", is_abstract=True)
TemporalExpression = Class(name="TemporalExpression")
TTMCConstraint_TemporalStateExpression = Class(name="TTMCConstraint::TemporalStateExpression", is_abstract=True)
TTMCConstraint_LiteralExpression = Class(name="TTMCConstraint::LiteralExpression", is_abstract=True)
TTMCConstraint_ArithmeticLiteralExpression = Class(name="TTMCConstraint::ArithmeticLiteralExpression", is_abstract=True)
NullaryExpression = Class(name="NullaryExpression")
LiteralExpression = Class(name="LiteralExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
TTMCConstraint_IntegerLiteralExpression = Class(name="TTMCConstraint::IntegerLiteralExpression")
ArithmeticLiteralExpression = Class(name="ArithmeticLiteralExpression")
TTMCConstraint_DecimalLiteralExpression = Class(name="TTMCConstraint::DecimalLiteralExpression")
TTMCConstraint_RationalLiteralExpression = Class(name="TTMCConstraint::RationalLiteralExpression")
TTMCConstraint_BooleanLiteralExpression = Class(name="TTMCConstraint::BooleanLiteralExpression", is_abstract=True)
BooleanExpression = Class(name="BooleanExpression")
TTMCConstraint_TrueExpression = Class(name="TTMCConstraint::TrueExpression")
BooleanLiteralExpression = Class(name="BooleanLiteralExpression")
TTMCConstraint_FalseExpression = Class(name="TTMCConstraint::FalseExpression")
TTMCConstraint_ArrayLiteralExpression = Class(name="TTMCConstraint::ArrayLiteralExpression")
TTMCConstraint_FunctionLiteralExpression = Class(name="TTMCConstraint::FunctionLiteralExpression")
TTMCConstraint_RecordLiteralExpression = Class(name="TTMCConstraint::RecordLiteralExpression")
TTMCConstraint_FieldAssignment = Class(name="TTMCConstraint::FieldAssignment")
TTMCConstraint_EnumerationLiteralExpression = Class(name="TTMCConstraint::EnumerationLiteralExpression")
TTMCConstraint_TupleLiteralExpression = Class(name="TTMCConstraint::TupleLiteralExpression")
TTMCConstraint_ReferenceExpression = Class(name="TTMCConstraint::ReferenceExpression")
TTMCConstraint_IfThenElseExpression = Class(name="TTMCConstraint::IfThenElseExpression")
TTMCConstraint_LetExpression = Class(name="TTMCConstraint::LetExpression")
TTMCConstraint_PrimedExpression = Class(name="TTMCConstraint::PrimedExpression")
TTMCConstraint_EqualExpression = Class(name="TTMCConstraint::EqualExpression")
BinaryExpression = Class(name="BinaryExpression")
TTMCConstraint_ImplyExpression = Class(name="TTMCConstraint::ImplyExpression")
TTMCConstraint_OrExpression = Class(name="TTMCConstraint::OrExpression")
MultiaryExpression = Class(name="MultiaryExpression")
TTMCConstraint_AndExpression = Class(name="TTMCConstraint::AndExpression")
TTMCConstraint_ReleaseExpression = Class(name="TTMCConstraint::ReleaseExpression")
TemporalPathExpression = Class(name="TemporalPathExpression")
TTMCConstraint_UntilExpression = Class(name="TTMCConstraint::UntilExpression")
TTMCConstraint_NotExpression = Class(name="TTMCConstraint::NotExpression")
TTMCConstraint_ForallExpression = Class(name="TTMCConstraint::ForallExpression")
QuantifierExpression = Class(name="QuantifierExpression")
TTMCConstraint_ExistsExpression = Class(name="TTMCConstraint::ExistsExpression")
TTMCConstraint_GloballyExpression = Class(name="TTMCConstraint::GloballyExpression")
TTMCConstraint_FinallyExpression = Class(name="TTMCConstraint::FinallyExpression")
TTMCConstraint_NextExpression = Class(name="TTMCConstraint::NextExpression")
TTMCConstraint_TemporalForallExpression = Class(name="TTMCConstraint::TemporalForallExpression")
TemporalStateExpression = Class(name="TemporalStateExpression")
TTMCConstraint_TemporalExistsExpression = Class(name="TTMCConstraint::TemporalExistsExpression")
TTMCConstraint_InExpression = Class(name="TTMCConstraint::InExpression")
PredicateExpression = Class(name="PredicateExpression")
TTMCConstraint_RecordAccessExpression = Class(name="TTMCConstraint::RecordAccessExpression")
TTMCConstraint_EquivalenceExpression = Class(name="TTMCConstraint::EquivalenceExpression", is_abstract=True)
TTMCConstraint_EqualityExpression = Class(name="TTMCConstraint::EqualityExpression")
EquivalenceExpression = Class(name="EquivalenceExpression")
TTMCConstraint_InequalityExpression = Class(name="TTMCConstraint::InequalityExpression")
TTMCConstraint_ComparisionExpression = Class(name="TTMCConstraint::ComparisionExpression", is_abstract=True)
TTMCConstraint_GreaterExpression = Class(name="TTMCConstraint::GreaterExpression")
ComparisionExpression = Class(name="ComparisionExpression")
TTMCConstraint_GreaterEqualExpression = Class(name="TTMCConstraint::GreaterEqualExpression")
TTMCConstraint_LessExpression = Class(name="TTMCConstraint::LessExpression")
TTMCConstraint_LessEqualExpression = Class(name="TTMCConstraint::LessEqualExpression")
TTMCConstraint_AddExpression = Class(name="TTMCConstraint::AddExpression")
TTMCConstraint_SubtractExpression = Class(name="TTMCConstraint::SubtractExpression")
TTMCConstraint_MultiplyExpression = Class(name="TTMCConstraint::MultiplyExpression")
TTMCConstraint_DivideExpression = Class(name="TTMCConstraint::DivideExpression")
TTMCConstraint_DivExpression = Class(name="TTMCConstraint::DivExpression")
TTMCConstraint_ModExpression = Class(name="TTMCConstraint::ModExpression")
TTMCConstraint_UnaryMinusExpression = Class(name="TTMCConstraint::UnaryMinusExpression")
TTMCConstraint_UnaryPlusExpression = Class(name="TTMCConstraint::UnaryPlusExpression")
TTMCConstraint_FunctionAccessExpression = Class(name="TTMCConstraint::FunctionAccessExpression")
AccessExpression = Class(name="AccessExpression")
ParametrizedElement = Class(name="ParametrizedElement")
TTMCConstraint_ArrayAccessExpression = Class(name="TTMCConstraint::ArrayAccessExpression")
TTMCConstraint_TupleAccessExpression = Class(name="TTMCConstraint::TupleAccessExpression")

# TTMCConstraint_NamedElement class attributes and methods
TTMCConstraint_NamedElement_name: Property = Property(name="name", type=StringType)
TTMCConstraint_NamedElement.attributes={TTMCConstraint_NamedElement_name}

# TTMCConstraint_ParametricElement class attributes and methods

# TTMCConstraint_ParameterDeclaration class attributes and methods

# TTMCConstraint_ParametrizedElement class attributes and methods

# TTMCConstraint_Expression class attributes and methods

# TTMCConstraint_ConstraintSpecification class attributes and methods

# NamedElement class attributes and methods

# ParametricElement class attributes and methods

# TTMCConstraint_TypeDeclaration class attributes and methods

# TTMCConstraint_ConstantDeclaration class attributes and methods

# TTMCConstraint_FunctionDeclaration class attributes and methods

# TTMCConstraint_BasicConstraintDefinition class attributes and methods

# TTMCConstraint_Declaration class attributes and methods

# TTMCConstraint_Type class attributes and methods

# TTMCConstraint_DefinableDeclaration class attributes and methods

# Declaration class attributes and methods

# TTMCConstraint_FieldDeclaration class attributes and methods

# TTMCConstraint_LetDeclaration class attributes and methods

# DefinableDeclaration class attributes and methods

# TTMCConstraint_TypeReference class attributes and methods

# Type class attributes and methods

# TTMCConstraint_TypeDefinition class attributes and methods

# TTMCConstraint_BasicTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# TTMCConstraint_IntegerTypeDefinition class attributes and methods

# BasicTypeDefinition class attributes and methods

# TTMCConstraint_NaturalTypeDefinition class attributes and methods

# TTMCConstraint_BooleanTypeDefinition class attributes and methods

# TTMCConstraint_RealTypeDefinition class attributes and methods

# TTMCConstraint_SubrangeTypeDefinition class attributes and methods

# TTMCConstraint_RecordTypeDefinition class attributes and methods

# TTMCConstraint_SubTypeDefinition class attributes and methods

# TTMCConstraint_EnumerationTypeDefinition class attributes and methods

# TTMCConstraint_EnumerationLiteralDefinition class attributes and methods

# TTMCConstraint_FunctionTypeDefinition class attributes and methods

# TTMCConstraint_ArrayTypeDefinition class attributes and methods

# TTMCConstraint_TupleTypeDefinition class attributes and methods

# TTMCConstraint_BooleanExpression class attributes and methods

# TTMCConstraint_ConstraintDefinition class attributes and methods

# ConstraintDefinition class attributes and methods

# TTMCConstraint_NullaryExpression class attributes and methods

# Expression class attributes and methods

# TTMCConstraint_UnaryExpression class attributes and methods

# TTMCConstraint_BinaryExpression class attributes and methods

# TTMCConstraint_MultiaryExpression class attributes and methods

# TTMCConstraint_PredicateExpression class attributes and methods

# TTMCConstraint_ArithmeticExpression class attributes and methods

# TTMCConstraint_AccessExpression class attributes and methods

# TTMCConstraint_QuantifierExpression class attributes and methods

# UnaryExpression class attributes and methods

# TTMCConstraint_TemporalExpression class attributes and methods

# TTMCConstraint_TemporalPathExpression class attributes and methods

# TemporalExpression class attributes and methods

# TTMCConstraint_TemporalStateExpression class attributes and methods

# TTMCConstraint_LiteralExpression class attributes and methods

# TTMCConstraint_ArithmeticLiteralExpression class attributes and methods

# NullaryExpression class attributes and methods

# LiteralExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# TTMCConstraint_IntegerLiteralExpression class attributes and methods
TTMCConstraint_IntegerLiteralExpression_value: Property = Property(name="value", type=StringType)
TTMCConstraint_IntegerLiteralExpression.attributes={TTMCConstraint_IntegerLiteralExpression_value}

# ArithmeticLiteralExpression class attributes and methods

# TTMCConstraint_DecimalLiteralExpression class attributes and methods
TTMCConstraint_DecimalLiteralExpression_value: Property = Property(name="value", type=StringType)
TTMCConstraint_DecimalLiteralExpression.attributes={TTMCConstraint_DecimalLiteralExpression_value}

# TTMCConstraint_RationalLiteralExpression class attributes and methods
TTMCConstraint_RationalLiteralExpression_numerator: Property = Property(name="numerator", type=StringType)
TTMCConstraint_RationalLiteralExpression_denominator: Property = Property(name="denominator", type=StringType)
TTMCConstraint_RationalLiteralExpression.attributes={TTMCConstraint_RationalLiteralExpression_numerator, TTMCConstraint_RationalLiteralExpression_denominator}

# TTMCConstraint_BooleanLiteralExpression class attributes and methods

# BooleanExpression class attributes and methods

# TTMCConstraint_TrueExpression class attributes and methods

# BooleanLiteralExpression class attributes and methods

# TTMCConstraint_FalseExpression class attributes and methods

# TTMCConstraint_ArrayLiteralExpression class attributes and methods

# TTMCConstraint_FunctionLiteralExpression class attributes and methods

# TTMCConstraint_RecordLiteralExpression class attributes and methods

# TTMCConstraint_FieldAssignment class attributes and methods
TTMCConstraint_FieldAssignment_reference: Property = Property(name="reference", type=StringType)
TTMCConstraint_FieldAssignment.attributes={TTMCConstraint_FieldAssignment_reference}

# TTMCConstraint_EnumerationLiteralExpression class attributes and methods

# TTMCConstraint_TupleLiteralExpression class attributes and methods

# TTMCConstraint_ReferenceExpression class attributes and methods

# TTMCConstraint_IfThenElseExpression class attributes and methods

# TTMCConstraint_LetExpression class attributes and methods

# TTMCConstraint_PrimedExpression class attributes and methods

# TTMCConstraint_EqualExpression class attributes and methods

# BinaryExpression class attributes and methods

# TTMCConstraint_ImplyExpression class attributes and methods

# TTMCConstraint_OrExpression class attributes and methods

# MultiaryExpression class attributes and methods

# TTMCConstraint_AndExpression class attributes and methods

# TTMCConstraint_ReleaseExpression class attributes and methods

# TemporalPathExpression class attributes and methods

# TTMCConstraint_UntilExpression class attributes and methods

# TTMCConstraint_NotExpression class attributes and methods

# TTMCConstraint_ForallExpression class attributes and methods

# QuantifierExpression class attributes and methods

# TTMCConstraint_ExistsExpression class attributes and methods

# TTMCConstraint_GloballyExpression class attributes and methods

# TTMCConstraint_FinallyExpression class attributes and methods

# TTMCConstraint_NextExpression class attributes and methods

# TTMCConstraint_TemporalForallExpression class attributes and methods

# TemporalStateExpression class attributes and methods

# TTMCConstraint_TemporalExistsExpression class attributes and methods

# TTMCConstraint_InExpression class attributes and methods

# PredicateExpression class attributes and methods

# TTMCConstraint_RecordAccessExpression class attributes and methods
TTMCConstraint_RecordAccessExpression_field: Property = Property(name="field", type=StringType)
TTMCConstraint_RecordAccessExpression.attributes={TTMCConstraint_RecordAccessExpression_field}

# TTMCConstraint_EquivalenceExpression class attributes and methods

# TTMCConstraint_EqualityExpression class attributes and methods

# EquivalenceExpression class attributes and methods

# TTMCConstraint_InequalityExpression class attributes and methods

# TTMCConstraint_ComparisionExpression class attributes and methods

# TTMCConstraint_GreaterExpression class attributes and methods

# ComparisionExpression class attributes and methods

# TTMCConstraint_GreaterEqualExpression class attributes and methods

# TTMCConstraint_LessExpression class attributes and methods

# TTMCConstraint_LessEqualExpression class attributes and methods

# TTMCConstraint_AddExpression class attributes and methods

# TTMCConstraint_SubtractExpression class attributes and methods

# TTMCConstraint_MultiplyExpression class attributes and methods

# TTMCConstraint_DivideExpression class attributes and methods

# TTMCConstraint_DivExpression class attributes and methods

# TTMCConstraint_ModExpression class attributes and methods

# TTMCConstraint_UnaryMinusExpression class attributes and methods

# TTMCConstraint_UnaryPlusExpression class attributes and methods

# TTMCConstraint_FunctionAccessExpression class attributes and methods

# AccessExpression class attributes and methods

# ParametrizedElement class attributes and methods

# TTMCConstraint_ArrayAccessExpression class attributes and methods

# TTMCConstraint_TupleAccessExpression class attributes and methods
TTMCConstraint_TupleAccessExpression_index: Property = Property(name="index", type=StringType)
TTMCConstraint_TupleAccessExpression.attributes={TTMCConstraint_TupleAccessExpression_index}

# Relationships
parameterDeclarations0: BinaryAssociation = BinaryAssociation(
    name="parameterDeclarations0",
    ends={
        Property(name="TTMCConstraint_ParameterDeclaration", type=TTMCConstraint_ParametricElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ParametricElement", type=TTMCConstraint_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="TTMCConstraint_Expression", type=TTMCConstraint_ParametrizedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ParametrizedElement", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclarations2: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations2",
    ends={
        Property(name="TTMCConstraint_TypeDeclaration", type=TTMCConstraint_ConstraintSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ConstraintSpecification", type=TTMCConstraint_TypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantDeclarations3: BinaryAssociation = BinaryAssociation(
    name="constantDeclarations3",
    ends={
        Property(name="TTMCConstraint_ConstantDeclaration", type=TTMCConstraint_ConstraintSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ConstraintSpecification4", type=TTMCConstraint_ConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionDeclarations5: BinaryAssociation = BinaryAssociation(
    name="functionDeclarations5",
    ends={
        Property(name="TTMCConstraint_FunctionDeclaration", type=TTMCConstraint_ConstraintSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ConstraintSpecification6", type=TTMCConstraint_FunctionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicConstraintDefinitions7: BinaryAssociation = BinaryAssociation(
    name="basicConstraintDefinitions7",
    ends={
        Property(name="TTMCConstraint_BasicConstraintDefinition", type=TTMCConstraint_ConstraintSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ConstraintSpecification8", type=TTMCConstraint_BasicConstraintDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="TTMCConstraint_Type", type=TTMCConstraint_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_Declaration", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="TTMCConstraint_Expression11", type=TTMCConstraint_DefinableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_DefinableDeclaration", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="TTMCConstraint_Type14", type=TTMCConstraint_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_TypeDeclaration13", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference15: BinaryAssociation = BinaryAssociation(
    name="reference15",
    ends={
        Property(name="TTMCConstraint_TypeDeclaration16", type=TTMCConstraint_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_TypeReference", type=TTMCConstraint_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound17: BinaryAssociation = BinaryAssociation(
    name="lowerBound17",
    ends={
        Property(name="TTMCConstraint_Expression18", type=TTMCConstraint_SubrangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_SubrangeTypeDefinition", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound19: BinaryAssociation = BinaryAssociation(
    name="upperBound19",
    ends={
        Property(name="TTMCConstraint_Expression21", type=TTMCConstraint_SubrangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_SubrangeTypeDefinition20", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterDeclaration22: BinaryAssociation = BinaryAssociation(
    name="parameterDeclaration22",
    ends={
        Property(name="TTMCConstraint_ParameterDeclaration23", type=TTMCConstraint_SubTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_SubTypeDefinition", type=TTMCConstraint_ParameterDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression24: BinaryAssociation = BinaryAssociation(
    name="expression24",
    ends={
        Property(name="TTMCConstraint_Expression26", type=TTMCConstraint_SubTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_SubTypeDefinition25", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literals27: BinaryAssociation = BinaryAssociation(
    name="literals27",
    ends={
        Property(name="TTMCConstraint_EnumerationLiteralDefinition", type=TTMCConstraint_EnumerationTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_EnumerationTypeDefinition", type=TTMCConstraint_EnumerationLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterTypes28: BinaryAssociation = BinaryAssociation(
    name="parameterTypes28",
    ends={
        Property(name="TTMCConstraint_Type29", type=TTMCConstraint_FunctionTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_FunctionTypeDefinition", type=TTMCConstraint_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType30: BinaryAssociation = BinaryAssociation(
    name="returnType30",
    ends={
        Property(name="TTMCConstraint_Type32", type=TTMCConstraint_FunctionTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_FunctionTypeDefinition31", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indexTypes33: BinaryAssociation = BinaryAssociation(
    name="indexTypes33",
    ends={
        Property(name="TTMCConstraint_Type34", type=TTMCConstraint_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ArrayTypeDefinition", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementType35: BinaryAssociation = BinaryAssociation(
    name="elementType35",
    ends={
        Property(name="TTMCConstraint_Type37", type=TTMCConstraint_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ArrayTypeDefinition36", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types38: BinaryAssociation = BinaryAssociation(
    name="types38",
    ends={
        Property(name="TTMCConstraint_Type39", type=TTMCConstraint_TupleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_TupleTypeDefinition", type=TTMCConstraint_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldDeclarations40: BinaryAssociation = BinaryAssociation(
    name="fieldDeclarations40",
    ends={
        Property(name="TTMCConstraint_FieldDeclaration", type=TTMCConstraint_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_RecordTypeDefinition", type=TTMCConstraint_FieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="TTMCConstraint_Expression42", type=TTMCConstraint_ConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ConstraintDefinition", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand43: BinaryAssociation = BinaryAssociation(
    name="operand43",
    ends={
        Property(name="TTMCConstraint_Expression44", type=TTMCConstraint_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_UnaryExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand45: BinaryAssociation = BinaryAssociation(
    name="leftOperand45",
    ends={
        Property(name="TTMCConstraint_Expression46", type=TTMCConstraint_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_BinaryExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand47: BinaryAssociation = BinaryAssociation(
    name="rightOperand47",
    ends={
        Property(name="TTMCConstraint_Expression49", type=TTMCConstraint_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_BinaryExpression48", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands50: BinaryAssociation = BinaryAssociation(
    name="operands50",
    ends={
        Property(name="TTMCConstraint_Expression51", type=TTMCConstraint_MultiaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_MultiaryExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand52: BinaryAssociation = BinaryAssociation(
    name="operand52",
    ends={
        Property(name="TTMCConstraint_Expression53", type=TTMCConstraint_AccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_AccessExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType54: BinaryAssociation = BinaryAssociation(
    name="returnType54",
    ends={
        Property(name="TTMCConstraint_Type55", type=TTMCConstraint_FunctionLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_FunctionLiteralExpression", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fieldAssignments56: BinaryAssociation = BinaryAssociation(
    name="fieldAssignments56",
    ends={
        Property(name="TTMCConstraint_FieldAssignment", type=TTMCConstraint_RecordLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_RecordLiteralExpression", type=TTMCConstraint_FieldAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value57: BinaryAssociation = BinaryAssociation(
    name="value57",
    ends={
        Property(name="TTMCConstraint_Expression59", type=TTMCConstraint_FieldAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_FieldAssignment58", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference60: BinaryAssociation = BinaryAssociation(
    name="reference60",
    ends={
        Property(name="TTMCConstraint_EnumerationLiteralDefinition61", type=TTMCConstraint_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_EnumerationLiteralExpression", type=TTMCConstraint_EnumerationLiteralDefinition, multiplicity=Multiplicity(1, 1))
    }
)
expressions62: BinaryAssociation = BinaryAssociation(
    name="expressions62",
    ends={
        Property(name="TTMCConstraint_Expression63", type=TTMCConstraint_TupleLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_TupleLiteralExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration64: BinaryAssociation = BinaryAssociation(
    name="declaration64",
    ends={
        Property(name="TTMCConstraint_Declaration65", type=TTMCConstraint_ReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_ReferenceExpression", type=TTMCConstraint_Declaration, multiplicity=Multiplicity(1, 1))
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="TTMCConstraint_Expression67", type=TTMCConstraint_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_IfThenElseExpression", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then68: BinaryAssociation = BinaryAssociation(
    name="then68",
    ends={
        Property(name="TTMCConstraint_Expression70", type=TTMCConstraint_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_IfThenElseExpression69", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else71: BinaryAssociation = BinaryAssociation(
    name="else71",
    ends={
        Property(name="TTMCConstraint_Expression73", type=TTMCConstraint_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_IfThenElseExpression72", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
letDeclarations74: BinaryAssociation = BinaryAssociation(
    name="letDeclarations74",
    ends={
        Property(name="TTMCConstraint_LetDeclaration", type=TTMCConstraint_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_LetExpression", type=TTMCConstraint_LetDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="TTMCConstraint_Expression77", type=TTMCConstraint_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_LetExpression76", type=TTMCConstraint_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="TTMCConstraint_Type79", type=TTMCConstraint_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TTMCConstraint_InExpression", type=TTMCConstraint_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_TTMCConstraint_ConstraintSpecification_NamedElement = Generalization(general=NamedElement, specific=TTMCConstraint_ConstraintSpecification)
gen_TTMCConstraint_ConstraintSpecification_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_ConstraintSpecification)
gen_TTMCConstraint_Declaration_NamedElement = Generalization(general=NamedElement, specific=TTMCConstraint_Declaration)
gen_TTMCConstraint_DefinableDeclaration_Declaration = Generalization(general=Declaration, specific=TTMCConstraint_DefinableDeclaration)
gen_TTMCConstraint_ParameterDeclaration_Declaration = Generalization(general=Declaration, specific=TTMCConstraint_ParameterDeclaration)
gen_TTMCConstraint_FieldDeclaration_Declaration = Generalization(general=Declaration, specific=TTMCConstraint_FieldDeclaration)
gen_TTMCConstraint_LetDeclaration_DefinableDeclaration = Generalization(general=DefinableDeclaration, specific=TTMCConstraint_LetDeclaration)
gen_TTMCConstraint_ConstantDeclaration_DefinableDeclaration = Generalization(general=DefinableDeclaration, specific=TTMCConstraint_ConstantDeclaration)
gen_TTMCConstraint_FunctionDeclaration_DefinableDeclaration = Generalization(general=DefinableDeclaration, specific=TTMCConstraint_FunctionDeclaration)
gen_TTMCConstraint_FunctionDeclaration_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_FunctionDeclaration)
gen_TTMCConstraint_TypeDeclaration_NamedElement = Generalization(general=NamedElement, specific=TTMCConstraint_TypeDeclaration)
gen_TTMCConstraint_TypeReference_Type = Generalization(general=Type, specific=TTMCConstraint_TypeReference)
gen_TTMCConstraint_TypeDefinition_Type = Generalization(general=Type, specific=TTMCConstraint_TypeDefinition)
gen_TTMCConstraint_BasicTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_BasicTypeDefinition)
gen_TTMCConstraint_IntegerTypeDefinition_BasicTypeDefinition = Generalization(general=BasicTypeDefinition, specific=TTMCConstraint_IntegerTypeDefinition)
gen_TTMCConstraint_NaturalTypeDefinition_BasicTypeDefinition = Generalization(general=BasicTypeDefinition, specific=TTMCConstraint_NaturalTypeDefinition)
gen_TTMCConstraint_BooleanTypeDefinition_BasicTypeDefinition = Generalization(general=BasicTypeDefinition, specific=TTMCConstraint_BooleanTypeDefinition)
gen_TTMCConstraint_RealTypeDefinition_BasicTypeDefinition = Generalization(general=BasicTypeDefinition, specific=TTMCConstraint_RealTypeDefinition)
gen_TTMCConstraint_SubrangeTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_SubrangeTypeDefinition)
gen_TTMCConstraint_RecordTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_RecordTypeDefinition)
gen_TTMCConstraint_SubTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_SubTypeDefinition)
gen_TTMCConstraint_SubTypeDefinition_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_SubTypeDefinition)
gen_TTMCConstraint_EnumerationTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_EnumerationTypeDefinition)
gen_TTMCConstraint_EnumerationLiteralDefinition_NamedElement = Generalization(general=NamedElement, specific=TTMCConstraint_EnumerationLiteralDefinition)
gen_TTMCConstraint_FunctionTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_FunctionTypeDefinition)
gen_TTMCConstraint_ArrayTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_ArrayTypeDefinition)
gen_TTMCConstraint_TupleTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=TTMCConstraint_TupleTypeDefinition)
gen_TTMCConstraint_BooleanExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_BooleanExpression)
gen_TTMCConstraint_BasicConstraintDefinition_ConstraintDefinition = Generalization(general=ConstraintDefinition, specific=TTMCConstraint_BasicConstraintDefinition)
gen_TTMCConstraint_NullaryExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_NullaryExpression)
gen_TTMCConstraint_UnaryExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_UnaryExpression)
gen_TTMCConstraint_BinaryExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_BinaryExpression)
gen_TTMCConstraint_MultiaryExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_MultiaryExpression)
gen_TTMCConstraint_PredicateExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_PredicateExpression)
gen_TTMCConstraint_ArithmeticExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_ArithmeticExpression)
gen_TTMCConstraint_AccessExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_AccessExpression)
gen_TTMCConstraint_RecordLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_RecordLiteralExpression)
gen_TTMCConstraint_QuantifierExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_QuantifierExpression)
gen_TTMCConstraint_QuantifierExpression_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_QuantifierExpression)
gen_TTMCConstraint_TemporalExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_TemporalExpression)
gen_TTMCConstraint_TemporalPathExpression_TemporalExpression = Generalization(general=TemporalExpression, specific=TTMCConstraint_TemporalPathExpression)
gen_TTMCConstraint_TemporalStateExpression_TemporalExpression = Generalization(general=TemporalExpression, specific=TTMCConstraint_TemporalStateExpression)
gen_TTMCConstraint_LiteralExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_LiteralExpression)
gen_TTMCConstraint_ArithmeticLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=TTMCConstraint_ArithmeticLiteralExpression)
gen_TTMCConstraint_ArithmeticLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_ArithmeticLiteralExpression)
gen_TTMCConstraint_ArithmeticLiteralExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_ArithmeticLiteralExpression)
gen_TTMCConstraint_IntegerLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=TTMCConstraint_IntegerLiteralExpression)
gen_TTMCConstraint_DecimalLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=TTMCConstraint_DecimalLiteralExpression)
gen_TTMCConstraint_RationalLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=TTMCConstraint_RationalLiteralExpression)
gen_TTMCConstraint_BooleanLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=TTMCConstraint_BooleanLiteralExpression)
gen_TTMCConstraint_BooleanLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_BooleanLiteralExpression)
gen_TTMCConstraint_BooleanLiteralExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_BooleanLiteralExpression)
gen_TTMCConstraint_TrueExpression_BooleanLiteralExpression = Generalization(general=BooleanLiteralExpression, specific=TTMCConstraint_TrueExpression)
gen_TTMCConstraint_FalseExpression_BooleanLiteralExpression = Generalization(general=BooleanLiteralExpression, specific=TTMCConstraint_FalseExpression)
gen_TTMCConstraint_ArrayLiteralExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_ArrayLiteralExpression)
gen_TTMCConstraint_ArrayLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_ArrayLiteralExpression)
gen_TTMCConstraint_ArrayLiteralExpression_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_ArrayLiteralExpression)
gen_TTMCConstraint_FunctionLiteralExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_FunctionLiteralExpression)
gen_TTMCConstraint_FunctionLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_FunctionLiteralExpression)
gen_TTMCConstraint_FunctionLiteralExpression_ParametricElement = Generalization(general=ParametricElement, specific=TTMCConstraint_FunctionLiteralExpression)
gen_TTMCConstraint_EnumerationLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=TTMCConstraint_EnumerationLiteralExpression)
gen_TTMCConstraint_EnumerationLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_EnumerationLiteralExpression)
gen_TTMCConstraint_TupleLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=TTMCConstraint_TupleLiteralExpression)
gen_TTMCConstraint_ReferenceExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=TTMCConstraint_ReferenceExpression)
gen_TTMCConstraint_IfThenElseExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_IfThenElseExpression)
gen_TTMCConstraint_LetExpression_Expression = Generalization(general=Expression, specific=TTMCConstraint_LetExpression)
gen_TTMCConstraint_EqualExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_EqualExpression)
gen_TTMCConstraint_EqualExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_EqualExpression)
gen_TTMCConstraint_ImplyExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_ImplyExpression)
gen_TTMCConstraint_ImplyExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_ImplyExpression)
gen_TTMCConstraint_OrExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_OrExpression)
gen_TTMCConstraint_OrExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=TTMCConstraint_OrExpression)
gen_TTMCConstraint_AndExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_AndExpression)
gen_TTMCConstraint_AndExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=TTMCConstraint_AndExpression)
gen_TTMCConstraint_ReleaseExpression_TemporalPathExpression = Generalization(general=TemporalPathExpression, specific=TTMCConstraint_ReleaseExpression)
gen_TTMCConstraint_ReleaseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_ReleaseExpression)
gen_TTMCConstraint_UntilExpression_TemporalPathExpression = Generalization(general=TemporalPathExpression, specific=TTMCConstraint_UntilExpression)
gen_TTMCConstraint_UntilExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_UntilExpression)
gen_TTMCConstraint_NotExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=TTMCConstraint_NotExpression)
gen_TTMCConstraint_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_NotExpression)
gen_TTMCConstraint_ForallExpression_QuantifierExpression = Generalization(general=QuantifierExpression, specific=TTMCConstraint_ForallExpression)
gen_TTMCConstraint_ExistsExpression_QuantifierExpression = Generalization(general=QuantifierExpression, specific=TTMCConstraint_ExistsExpression)
gen_TTMCConstraint_GloballyExpression_TemporalPathExpression = Generalization(general=TemporalPathExpression, specific=TTMCConstraint_GloballyExpression)
gen_TTMCConstraint_GloballyExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_GloballyExpression)
gen_TTMCConstraint_FinallyExpression_TemporalPathExpression = Generalization(general=TemporalPathExpression, specific=TTMCConstraint_FinallyExpression)
gen_TTMCConstraint_FinallyExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_FinallyExpression)
gen_TTMCConstraint_NextExpression_TemporalPathExpression = Generalization(general=TemporalPathExpression, specific=TTMCConstraint_NextExpression)
gen_TTMCConstraint_NextExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_NextExpression)
gen_TTMCConstraint_TemporalForallExpression_TemporalStateExpression = Generalization(general=TemporalStateExpression, specific=TTMCConstraint_TemporalForallExpression)
gen_TTMCConstraint_TemporalForallExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_TemporalForallExpression)
gen_TTMCConstraint_TemporalExistsExpression_TemporalStateExpression = Generalization(general=TemporalStateExpression, specific=TTMCConstraint_TemporalExistsExpression)
gen_TTMCConstraint_TemporalExistsExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_TemporalExistsExpression)
gen_TTMCConstraint_InExpression_PredicateExpression = Generalization(general=PredicateExpression, specific=TTMCConstraint_InExpression)
gen_TTMCConstraint_InExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_InExpression)
gen_TTMCConstraint_RecordAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=TTMCConstraint_RecordAccessExpression)
gen_TTMCConstraint_PrimedExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_PrimedExpression)
gen_TTMCConstraint_EquivalenceExpression_PredicateExpression = Generalization(general=PredicateExpression, specific=TTMCConstraint_EquivalenceExpression)
gen_TTMCConstraint_EquivalenceExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_EquivalenceExpression)
gen_TTMCConstraint_EqualityExpression_EquivalenceExpression = Generalization(general=EquivalenceExpression, specific=TTMCConstraint_EqualityExpression)
gen_TTMCConstraint_InequalityExpression_EquivalenceExpression = Generalization(general=EquivalenceExpression, specific=TTMCConstraint_InequalityExpression)
gen_TTMCConstraint_ComparisionExpression_PredicateExpression = Generalization(general=PredicateExpression, specific=TTMCConstraint_ComparisionExpression)
gen_TTMCConstraint_ComparisionExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_ComparisionExpression)
gen_TTMCConstraint_GreaterExpression_ComparisionExpression = Generalization(general=ComparisionExpression, specific=TTMCConstraint_GreaterExpression)
gen_TTMCConstraint_GreaterEqualExpression_ComparisionExpression = Generalization(general=ComparisionExpression, specific=TTMCConstraint_GreaterEqualExpression)
gen_TTMCConstraint_LessExpression_ComparisionExpression = Generalization(general=ComparisionExpression, specific=TTMCConstraint_LessExpression)
gen_TTMCConstraint_LessEqualExpression_ComparisionExpression = Generalization(general=ComparisionExpression, specific=TTMCConstraint_LessEqualExpression)
gen_TTMCConstraint_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_AddExpression)
gen_TTMCConstraint_AddExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=TTMCConstraint_AddExpression)
gen_TTMCConstraint_SubtractExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_SubtractExpression)
gen_TTMCConstraint_SubtractExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_SubtractExpression)
gen_TTMCConstraint_MultiplyExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_MultiplyExpression)
gen_TTMCConstraint_MultiplyExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=TTMCConstraint_MultiplyExpression)
gen_TTMCConstraint_DivideExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_DivideExpression)
gen_TTMCConstraint_DivideExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_DivideExpression)
gen_TTMCConstraint_DivExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_DivExpression)
gen_TTMCConstraint_DivExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_DivExpression)
gen_TTMCConstraint_ModExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_ModExpression)
gen_TTMCConstraint_ModExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=TTMCConstraint_ModExpression)
gen_TTMCConstraint_UnaryMinusExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_UnaryMinusExpression)
gen_TTMCConstraint_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_UnaryMinusExpression)
gen_TTMCConstraint_UnaryPlusExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=TTMCConstraint_UnaryPlusExpression)
gen_TTMCConstraint_UnaryPlusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=TTMCConstraint_UnaryPlusExpression)
gen_TTMCConstraint_FunctionAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=TTMCConstraint_FunctionAccessExpression)
gen_TTMCConstraint_FunctionAccessExpression_ParametrizedElement = Generalization(general=ParametrizedElement, specific=TTMCConstraint_FunctionAccessExpression)
gen_TTMCConstraint_ArrayAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=TTMCConstraint_ArrayAccessExpression)
gen_TTMCConstraint_ArrayAccessExpression_ParametrizedElement = Generalization(general=ParametrizedElement, specific=TTMCConstraint_ArrayAccessExpression)
gen_TTMCConstraint_TupleAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=TTMCConstraint_TupleAccessExpression)

# Domain Model
domain_model = DomainModel(
    name="TTMCConstraint",
    types={TTMCConstraint_NamedElement, TTMCConstraint_ParametricElement, TTMCConstraint_ParameterDeclaration, TTMCConstraint_ParametrizedElement, TTMCConstraint_Expression, TTMCConstraint_ConstraintSpecification, NamedElement, ParametricElement, TTMCConstraint_TypeDeclaration, TTMCConstraint_ConstantDeclaration, TTMCConstraint_FunctionDeclaration, TTMCConstraint_BasicConstraintDefinition, TTMCConstraint_Declaration, TTMCConstraint_Type, TTMCConstraint_DefinableDeclaration, Declaration, TTMCConstraint_FieldDeclaration, TTMCConstraint_LetDeclaration, DefinableDeclaration, TTMCConstraint_TypeReference, Type, TTMCConstraint_TypeDefinition, TTMCConstraint_BasicTypeDefinition, TypeDefinition, TTMCConstraint_IntegerTypeDefinition, BasicTypeDefinition, TTMCConstraint_NaturalTypeDefinition, TTMCConstraint_BooleanTypeDefinition, TTMCConstraint_RealTypeDefinition, TTMCConstraint_SubrangeTypeDefinition, TTMCConstraint_RecordTypeDefinition, TTMCConstraint_SubTypeDefinition, TTMCConstraint_EnumerationTypeDefinition, TTMCConstraint_EnumerationLiteralDefinition, TTMCConstraint_FunctionTypeDefinition, TTMCConstraint_ArrayTypeDefinition, TTMCConstraint_TupleTypeDefinition, TTMCConstraint_BooleanExpression, TTMCConstraint_ConstraintDefinition, ConstraintDefinition, TTMCConstraint_NullaryExpression, Expression, TTMCConstraint_UnaryExpression, TTMCConstraint_BinaryExpression, TTMCConstraint_MultiaryExpression, TTMCConstraint_PredicateExpression, TTMCConstraint_ArithmeticExpression, TTMCConstraint_AccessExpression, TTMCConstraint_QuantifierExpression, UnaryExpression, TTMCConstraint_TemporalExpression, TTMCConstraint_TemporalPathExpression, TemporalExpression, TTMCConstraint_TemporalStateExpression, TTMCConstraint_LiteralExpression, TTMCConstraint_ArithmeticLiteralExpression, NullaryExpression, LiteralExpression, ArithmeticExpression, TTMCConstraint_IntegerLiteralExpression, ArithmeticLiteralExpression, TTMCConstraint_DecimalLiteralExpression, TTMCConstraint_RationalLiteralExpression, TTMCConstraint_BooleanLiteralExpression, BooleanExpression, TTMCConstraint_TrueExpression, BooleanLiteralExpression, TTMCConstraint_FalseExpression, TTMCConstraint_ArrayLiteralExpression, TTMCConstraint_FunctionLiteralExpression, TTMCConstraint_RecordLiteralExpression, TTMCConstraint_FieldAssignment, TTMCConstraint_EnumerationLiteralExpression, TTMCConstraint_TupleLiteralExpression, TTMCConstraint_ReferenceExpression, TTMCConstraint_IfThenElseExpression, TTMCConstraint_LetExpression, TTMCConstraint_PrimedExpression, TTMCConstraint_EqualExpression, BinaryExpression, TTMCConstraint_ImplyExpression, TTMCConstraint_OrExpression, MultiaryExpression, TTMCConstraint_AndExpression, TTMCConstraint_ReleaseExpression, TemporalPathExpression, TTMCConstraint_UntilExpression, TTMCConstraint_NotExpression, TTMCConstraint_ForallExpression, QuantifierExpression, TTMCConstraint_ExistsExpression, TTMCConstraint_GloballyExpression, TTMCConstraint_FinallyExpression, TTMCConstraint_NextExpression, TTMCConstraint_TemporalForallExpression, TemporalStateExpression, TTMCConstraint_TemporalExistsExpression, TTMCConstraint_InExpression, PredicateExpression, TTMCConstraint_RecordAccessExpression, TTMCConstraint_EquivalenceExpression, TTMCConstraint_EqualityExpression, EquivalenceExpression, TTMCConstraint_InequalityExpression, TTMCConstraint_ComparisionExpression, TTMCConstraint_GreaterExpression, ComparisionExpression, TTMCConstraint_GreaterEqualExpression, TTMCConstraint_LessExpression, TTMCConstraint_LessEqualExpression, TTMCConstraint_AddExpression, TTMCConstraint_SubtractExpression, TTMCConstraint_MultiplyExpression, TTMCConstraint_DivideExpression, TTMCConstraint_DivExpression, TTMCConstraint_ModExpression, TTMCConstraint_UnaryMinusExpression, TTMCConstraint_UnaryPlusExpression, TTMCConstraint_FunctionAccessExpression, AccessExpression, ParametrizedElement, TTMCConstraint_ArrayAccessExpression, TTMCConstraint_TupleAccessExpression},
    associations={parameterDeclarations0, parameters1, typeDeclarations2, constantDeclarations3, functionDeclarations5, basicConstraintDefinitions7, type9, expression10, type12, reference15, lowerBound17, upperBound19, parameterDeclaration22, expression24, literals27, parameterTypes28, returnType30, indexTypes33, elementType35, types38, fieldDeclarations40, expression41, operand43, leftOperand45, rightOperand47, operands50, operand52, returnType54, fieldAssignments56, value57, reference60, expressions62, declaration64, condition66, then68, else71, letDeclarations74, expression75, type78},
    generalizations={gen_TTMCConstraint_ConstraintSpecification_NamedElement, gen_TTMCConstraint_ConstraintSpecification_ParametricElement, gen_TTMCConstraint_Declaration_NamedElement, gen_TTMCConstraint_DefinableDeclaration_Declaration, gen_TTMCConstraint_ParameterDeclaration_Declaration, gen_TTMCConstraint_FieldDeclaration_Declaration, gen_TTMCConstraint_LetDeclaration_DefinableDeclaration, gen_TTMCConstraint_ConstantDeclaration_DefinableDeclaration, gen_TTMCConstraint_FunctionDeclaration_DefinableDeclaration, gen_TTMCConstraint_FunctionDeclaration_ParametricElement, gen_TTMCConstraint_TypeDeclaration_NamedElement, gen_TTMCConstraint_TypeReference_Type, gen_TTMCConstraint_TypeDefinition_Type, gen_TTMCConstraint_BasicTypeDefinition_TypeDefinition, gen_TTMCConstraint_IntegerTypeDefinition_BasicTypeDefinition, gen_TTMCConstraint_NaturalTypeDefinition_BasicTypeDefinition, gen_TTMCConstraint_BooleanTypeDefinition_BasicTypeDefinition, gen_TTMCConstraint_RealTypeDefinition_BasicTypeDefinition, gen_TTMCConstraint_SubrangeTypeDefinition_TypeDefinition, gen_TTMCConstraint_RecordTypeDefinition_TypeDefinition, gen_TTMCConstraint_SubTypeDefinition_TypeDefinition, gen_TTMCConstraint_SubTypeDefinition_ParametricElement, gen_TTMCConstraint_EnumerationTypeDefinition_TypeDefinition, gen_TTMCConstraint_EnumerationLiteralDefinition_NamedElement, gen_TTMCConstraint_FunctionTypeDefinition_TypeDefinition, gen_TTMCConstraint_ArrayTypeDefinition_TypeDefinition, gen_TTMCConstraint_TupleTypeDefinition_TypeDefinition, gen_TTMCConstraint_BooleanExpression_Expression, gen_TTMCConstraint_BasicConstraintDefinition_ConstraintDefinition, gen_TTMCConstraint_NullaryExpression_Expression, gen_TTMCConstraint_UnaryExpression_Expression, gen_TTMCConstraint_BinaryExpression_Expression, gen_TTMCConstraint_MultiaryExpression_Expression, gen_TTMCConstraint_PredicateExpression_Expression, gen_TTMCConstraint_ArithmeticExpression_Expression, gen_TTMCConstraint_AccessExpression_Expression, gen_TTMCConstraint_RecordLiteralExpression_LiteralExpression, gen_TTMCConstraint_QuantifierExpression_UnaryExpression, gen_TTMCConstraint_QuantifierExpression_ParametricElement, gen_TTMCConstraint_TemporalExpression_Expression, gen_TTMCConstraint_TemporalPathExpression_TemporalExpression, gen_TTMCConstraint_TemporalStateExpression_TemporalExpression, gen_TTMCConstraint_LiteralExpression_Expression, gen_TTMCConstraint_ArithmeticLiteralExpression_NullaryExpression, gen_TTMCConstraint_ArithmeticLiteralExpression_LiteralExpression, gen_TTMCConstraint_ArithmeticLiteralExpression_ArithmeticExpression, gen_TTMCConstraint_IntegerLiteralExpression_ArithmeticLiteralExpression, gen_TTMCConstraint_DecimalLiteralExpression_ArithmeticLiteralExpression, gen_TTMCConstraint_RationalLiteralExpression_ArithmeticLiteralExpression, gen_TTMCConstraint_BooleanLiteralExpression_NullaryExpression, gen_TTMCConstraint_BooleanLiteralExpression_LiteralExpression, gen_TTMCConstraint_BooleanLiteralExpression_BooleanExpression, gen_TTMCConstraint_TrueExpression_BooleanLiteralExpression, gen_TTMCConstraint_FalseExpression_BooleanLiteralExpression, gen_TTMCConstraint_ArrayLiteralExpression_UnaryExpression, gen_TTMCConstraint_ArrayLiteralExpression_LiteralExpression, gen_TTMCConstraint_ArrayLiteralExpression_ParametricElement, gen_TTMCConstraint_FunctionLiteralExpression_UnaryExpression, gen_TTMCConstraint_FunctionLiteralExpression_LiteralExpression, gen_TTMCConstraint_FunctionLiteralExpression_ParametricElement, gen_TTMCConstraint_EnumerationLiteralExpression_NullaryExpression, gen_TTMCConstraint_EnumerationLiteralExpression_LiteralExpression, gen_TTMCConstraint_TupleLiteralExpression_LiteralExpression, gen_TTMCConstraint_ReferenceExpression_NullaryExpression, gen_TTMCConstraint_IfThenElseExpression_Expression, gen_TTMCConstraint_LetExpression_Expression, gen_TTMCConstraint_EqualExpression_BooleanExpression, gen_TTMCConstraint_EqualExpression_BinaryExpression, gen_TTMCConstraint_ImplyExpression_BooleanExpression, gen_TTMCConstraint_ImplyExpression_BinaryExpression, gen_TTMCConstraint_OrExpression_BooleanExpression, gen_TTMCConstraint_OrExpression_MultiaryExpression, gen_TTMCConstraint_AndExpression_BooleanExpression, gen_TTMCConstraint_AndExpression_MultiaryExpression, gen_TTMCConstraint_ReleaseExpression_TemporalPathExpression, gen_TTMCConstraint_ReleaseExpression_BinaryExpression, gen_TTMCConstraint_UntilExpression_TemporalPathExpression, gen_TTMCConstraint_UntilExpression_BinaryExpression, gen_TTMCConstraint_NotExpression_BooleanExpression, gen_TTMCConstraint_NotExpression_UnaryExpression, gen_TTMCConstraint_ForallExpression_QuantifierExpression, gen_TTMCConstraint_ExistsExpression_QuantifierExpression, gen_TTMCConstraint_GloballyExpression_TemporalPathExpression, gen_TTMCConstraint_GloballyExpression_UnaryExpression, gen_TTMCConstraint_FinallyExpression_TemporalPathExpression, gen_TTMCConstraint_FinallyExpression_UnaryExpression, gen_TTMCConstraint_NextExpression_TemporalPathExpression, gen_TTMCConstraint_NextExpression_UnaryExpression, gen_TTMCConstraint_TemporalForallExpression_TemporalStateExpression, gen_TTMCConstraint_TemporalForallExpression_UnaryExpression, gen_TTMCConstraint_TemporalExistsExpression_TemporalStateExpression, gen_TTMCConstraint_TemporalExistsExpression_UnaryExpression, gen_TTMCConstraint_InExpression_PredicateExpression, gen_TTMCConstraint_InExpression_UnaryExpression, gen_TTMCConstraint_RecordAccessExpression_AccessExpression, gen_TTMCConstraint_PrimedExpression_UnaryExpression, gen_TTMCConstraint_EquivalenceExpression_PredicateExpression, gen_TTMCConstraint_EquivalenceExpression_BinaryExpression, gen_TTMCConstraint_EqualityExpression_EquivalenceExpression, gen_TTMCConstraint_InequalityExpression_EquivalenceExpression, gen_TTMCConstraint_ComparisionExpression_PredicateExpression, gen_TTMCConstraint_ComparisionExpression_BinaryExpression, gen_TTMCConstraint_GreaterExpression_ComparisionExpression, gen_TTMCConstraint_GreaterEqualExpression_ComparisionExpression, gen_TTMCConstraint_LessExpression_ComparisionExpression, gen_TTMCConstraint_LessEqualExpression_ComparisionExpression, gen_TTMCConstraint_AddExpression_ArithmeticExpression, gen_TTMCConstraint_AddExpression_MultiaryExpression, gen_TTMCConstraint_SubtractExpression_ArithmeticExpression, gen_TTMCConstraint_SubtractExpression_BinaryExpression, gen_TTMCConstraint_MultiplyExpression_ArithmeticExpression, gen_TTMCConstraint_MultiplyExpression_MultiaryExpression, gen_TTMCConstraint_DivideExpression_ArithmeticExpression, gen_TTMCConstraint_DivideExpression_BinaryExpression, gen_TTMCConstraint_DivExpression_ArithmeticExpression, gen_TTMCConstraint_DivExpression_BinaryExpression, gen_TTMCConstraint_ModExpression_ArithmeticExpression, gen_TTMCConstraint_ModExpression_BinaryExpression, gen_TTMCConstraint_UnaryMinusExpression_ArithmeticExpression, gen_TTMCConstraint_UnaryMinusExpression_UnaryExpression, gen_TTMCConstraint_UnaryPlusExpression_ArithmeticExpression, gen_TTMCConstraint_UnaryPlusExpression_UnaryExpression, gen_TTMCConstraint_FunctionAccessExpression_AccessExpression, gen_TTMCConstraint_FunctionAccessExpression_ParametrizedElement, gen_TTMCConstraint_ArrayAccessExpression_AccessExpression, gen_TTMCConstraint_ArrayAccessExpression_ParametrizedElement, gen_TTMCConstraint_TupleAccessExpression_AccessExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)