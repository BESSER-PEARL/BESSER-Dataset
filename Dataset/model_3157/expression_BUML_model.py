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
model_CommentableElement = Class(name="model::CommentableElement")
model_Comment = Class(name="model::Comment")
model_ParametricElement = Class(name="model::ParametricElement", is_abstract=True)
model_ParameterDeclaration = Class(name="model::ParameterDeclaration")
model_ArgumentedElement = Class(name="model::ArgumentedElement")
model_Expression = Class(name="model::Expression", is_abstract=True)
model_ExpressionPackage = Class(name="model::ExpressionPackage")
NamedElement = Class(name="NamedElement")
ParametricElement = Class(name="ParametricElement")
model_TypeDeclaration = Class(name="model::TypeDeclaration")
model_ConstantDeclaration = Class(name="model::ConstantDeclaration")
model_FunctionDeclaration = Class(name="model::FunctionDeclaration")
model_BasicConstraintDefinition = Class(name="model::BasicConstraintDefinition")
model_InitializableElement = Class(name="model::InitializableElement", is_abstract=True)
model_Declaration = Class(name="model::Declaration", is_abstract=True)
model_Type = Class(name="model::Type")
model_ValueDeclaration = Class(name="model::ValueDeclaration")
Declaration = Class(name="Declaration")
model_VariableDeclaration = Class(name="model::VariableDeclaration")
ValueDeclaration = Class(name="ValueDeclaration")
InitializableElement = Class(name="InitializableElement")
model_NamedElement = Class(name="model::NamedElement", is_abstract=True)
model_LambdaDeclaration = Class(name="model::LambdaDeclaration")
FunctionDeclaration = Class(name="FunctionDeclaration")
model_TypeReference = Class(name="model::TypeReference")
Type = Class(name="Type")
model_TypeDefinition = Class(name="model::TypeDefinition")
model_NumericalTypeDefinition = Class(name="model::NumericalTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
model_CompositeTypeDefinition = Class(name="model::CompositeTypeDefinition")
model_VoidTypeDefinition = Class(name="model::VoidTypeDefinition")
model_BooleanTypeDefinition = Class(name="model::BooleanTypeDefinition")
model_IntegerTypeDefinition = Class(name="model::IntegerTypeDefinition")
NumericalTypeDefinition = Class(name="NumericalTypeDefinition")
model_RationalTypeDefinition = Class(name="model::RationalTypeDefinition")
model_DecimalTypeDefinition = Class(name="model::DecimalTypeDefinition")
model_SubrangeTypeDefinition = Class(name="model::SubrangeTypeDefinition")
CompositeTypeDefinition = Class(name="CompositeTypeDefinition")
model_EnumerableTypeDefinition = Class(name="model::EnumerableTypeDefinition", is_abstract=True)
model_EnumerationTypeDefinition = Class(name="model::EnumerationTypeDefinition")
EnumerableTypeDefinition = Class(name="EnumerableTypeDefinition")
model_EnumerationLiteralDefinition = Class(name="model::EnumerationLiteralDefinition")
model_ArrayTypeDefinition = Class(name="model::ArrayTypeDefinition")
model_IntegerRangeTypeDefinition = Class(name="model::IntegerRangeTypeDefinition")
model_FunctionTypeDefinition = Class(name="model::FunctionTypeDefinition")
model_FieldDeclaration = Class(name="model::FieldDeclaration")
model_RecordTypeDefinition = Class(name="model::RecordTypeDefinition")
model_ConstraintDefinition = Class(name="model::ConstraintDefinition", is_abstract=True)
ConstraintDefinition = Class(name="ConstraintDefinition")
model_NullaryExpression = Class(name="model::NullaryExpression", is_abstract=True)
Expression = Class(name="Expression")
model_UnaryExpression = Class(name="model::UnaryExpression", is_abstract=True)
model_BinaryExpression = Class(name="model::BinaryExpression", is_abstract=True)
model_MultiaryExpression = Class(name="model::MultiaryExpression", is_abstract=True)
model_ArithmeticExpression = Class(name="model::ArithmeticExpression", is_abstract=True)
model_LogicExpression = Class(name="model::LogicExpression")
model_BooleanExpression = Class(name="model::BooleanExpression", is_abstract=True)
LogicExpression = Class(name="LogicExpression")
model_PredicateExpression = Class(name="model::PredicateExpression", is_abstract=True)
model_OpaqueExpression = Class(name="model::OpaqueExpression")
NullaryExpression = Class(name="NullaryExpression")
model_DefaultExpression = Class(name="model::DefaultExpression")
ElseExpression = Class(name="ElseExpression")
model_QuantifierExpression = Class(name="model::QuantifierExpression", is_abstract=True)
UnaryExpression = Class(name="UnaryExpression")
model_AccessExpression = Class(name="model::AccessExpression", is_abstract=True)
model_LiteralExpression = Class(name="model::LiteralExpression", is_abstract=True)
model_EnumerableExpression = Class(name="model::EnumerableExpression", is_abstract=True)
model_ArithmeticLiteralExpression = Class(name="model::ArithmeticLiteralExpression", is_abstract=True)
LiteralExpression = Class(name="LiteralExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
model_IntegerLiteralExpression = Class(name="model::IntegerLiteralExpression")
ArithmeticLiteralExpression = Class(name="ArithmeticLiteralExpression")
model_DecimalLiteralExpression = Class(name="model::DecimalLiteralExpression")
model_RationalLiteralExpression = Class(name="model::RationalLiteralExpression")
model_BooleanLiteralExpression = Class(name="model::BooleanLiteralExpression", is_abstract=True)
BooleanExpression = Class(name="BooleanExpression")
model_TrueExpression = Class(name="model::TrueExpression")
BooleanLiteralExpression = Class(name="BooleanLiteralExpression")
model_FalseExpression = Class(name="model::FalseExpression")
model_ArrayLiteralExpression = Class(name="model::ArrayLiteralExpression")
EnumerableExpression = Class(name="EnumerableExpression")
MultiaryExpression = Class(name="MultiaryExpression")
model_IntegerRangeLiteralExpression = Class(name="model::IntegerRangeLiteralExpression")
model_ElseExpression = Class(name="model::ElseExpression")
model_RecordLiteralExpression = Class(name="model::RecordLiteralExpression")
model_FieldAssignment = Class(name="model::FieldAssignment")
model_EnumerationLiteralExpression = Class(name="model::EnumerationLiteralExpression")
BinaryExpression = Class(name="BinaryExpression")
model_ReferenceExpression = Class(name="model::ReferenceExpression")
model_IfThenElseExpression = Class(name="model::IfThenElseExpression")
model_NotExpression = Class(name="model::NotExpression")
model_ForallExpression = Class(name="model::ForallExpression")
QuantifierExpression = Class(name="QuantifierExpression")
model_ExistsExpression = Class(name="model::ExistsExpression")
model_ImplyExpression = Class(name="model::ImplyExpression")
model_OrExpression = Class(name="model::OrExpression")
model_AndExpression = Class(name="model::AndExpression")
model_XorExpression = Class(name="model::XorExpression")
model_EquivalenceExpression = Class(name="model::EquivalenceExpression", is_abstract=True)
PredicateExpression = Class(name="PredicateExpression")
model_EqualityExpression = Class(name="model::EqualityExpression")
EquivalenceExpression = Class(name="EquivalenceExpression")
model_InequalityExpression = Class(name="model::InequalityExpression")
model_GreaterEqualExpression = Class(name="model::GreaterEqualExpression")
model_LessExpression = Class(name="model::LessExpression")
model_LessEqualExpression = Class(name="model::LessEqualExpression")
model_AddExpression = Class(name="model::AddExpression")
model_SubtractExpression = Class(name="model::SubtractExpression")
model_MultiplyExpression = Class(name="model::MultiplyExpression")
model_DivideExpression = Class(name="model::DivideExpression")
model_DivExpression = Class(name="model::DivExpression")
model_ModExpression = Class(name="model::ModExpression")
model_UnaryMinusExpression = Class(name="model::UnaryMinusExpression")
model_ComparisonExpression = Class(name="model::ComparisonExpression", is_abstract=True)
model_UnaryPlusExpression = Class(name="model::UnaryPlusExpression")
model_GreaterExpression = Class(name="model::GreaterExpression")
ComparisonExpression = Class(name="ComparisonExpression")
ArgumentedElement = Class(name="ArgumentedElement")
model_ArrayAccessExpression = Class(name="model::ArrayAccessExpression")
model_RecordAccessExpression = Class(name="model::RecordAccessExpression")
model_SelectExpression = Class(name="model::SelectExpression")
model_FunctionAccessExpression = Class(name="model::FunctionAccessExpression")
AccessExpression = Class(name="AccessExpression")

# model_CommentableElement class attributes and methods

# model_Comment class attributes and methods
model_Comment_comment: Property = Property(name="comment", type=StringType)
model_Comment.attributes={model_Comment_comment}

# model_ParametricElement class attributes and methods

# model_ParameterDeclaration class attributes and methods

# model_ArgumentedElement class attributes and methods

# model_Expression class attributes and methods

# model_ExpressionPackage class attributes and methods

# NamedElement class attributes and methods

# ParametricElement class attributes and methods

# model_TypeDeclaration class attributes and methods

# model_ConstantDeclaration class attributes and methods

# model_FunctionDeclaration class attributes and methods

# model_BasicConstraintDefinition class attributes and methods

# model_InitializableElement class attributes and methods

# model_Declaration class attributes and methods

# model_Type class attributes and methods

# model_ValueDeclaration class attributes and methods

# Declaration class attributes and methods

# model_VariableDeclaration class attributes and methods

# ValueDeclaration class attributes and methods

# InitializableElement class attributes and methods

# model_NamedElement class attributes and methods
model_NamedElement_name: Property = Property(name="name", type=StringType)
model_NamedElement.attributes={model_NamedElement_name}

# model_LambdaDeclaration class attributes and methods

# FunctionDeclaration class attributes and methods

# model_TypeReference class attributes and methods

# Type class attributes and methods

# model_TypeDefinition class attributes and methods

# model_NumericalTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# model_CompositeTypeDefinition class attributes and methods

# model_VoidTypeDefinition class attributes and methods

# model_BooleanTypeDefinition class attributes and methods

# model_IntegerTypeDefinition class attributes and methods

# NumericalTypeDefinition class attributes and methods

# model_RationalTypeDefinition class attributes and methods

# model_DecimalTypeDefinition class attributes and methods

# model_SubrangeTypeDefinition class attributes and methods

# CompositeTypeDefinition class attributes and methods

# model_EnumerableTypeDefinition class attributes and methods

# model_EnumerationTypeDefinition class attributes and methods

# EnumerableTypeDefinition class attributes and methods

# model_EnumerationLiteralDefinition class attributes and methods

# model_ArrayTypeDefinition class attributes and methods

# model_IntegerRangeTypeDefinition class attributes and methods

# model_FunctionTypeDefinition class attributes and methods

# model_FieldDeclaration class attributes and methods

# model_RecordTypeDefinition class attributes and methods

# model_ConstraintDefinition class attributes and methods

# ConstraintDefinition class attributes and methods

# model_NullaryExpression class attributes and methods

# Expression class attributes and methods

# model_UnaryExpression class attributes and methods

# model_BinaryExpression class attributes and methods

# model_MultiaryExpression class attributes and methods

# model_ArithmeticExpression class attributes and methods

# model_LogicExpression class attributes and methods

# model_BooleanExpression class attributes and methods

# LogicExpression class attributes and methods

# model_PredicateExpression class attributes and methods

# model_OpaqueExpression class attributes and methods
model_OpaqueExpression_expression: Property = Property(name="expression", type=StringType)
model_OpaqueExpression.attributes={model_OpaqueExpression_expression}

# NullaryExpression class attributes and methods

# model_DefaultExpression class attributes and methods

# ElseExpression class attributes and methods

# model_QuantifierExpression class attributes and methods

# UnaryExpression class attributes and methods

# model_AccessExpression class attributes and methods

# model_LiteralExpression class attributes and methods

# model_EnumerableExpression class attributes and methods

# model_ArithmeticLiteralExpression class attributes and methods

# LiteralExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# model_IntegerLiteralExpression class attributes and methods
model_IntegerLiteralExpression_value: Property = Property(name="value", type=StringType)
model_IntegerLiteralExpression.attributes={model_IntegerLiteralExpression_value}

# ArithmeticLiteralExpression class attributes and methods

# model_DecimalLiteralExpression class attributes and methods
model_DecimalLiteralExpression_value: Property = Property(name="value", type=StringType)
model_DecimalLiteralExpression.attributes={model_DecimalLiteralExpression_value}

# model_RationalLiteralExpression class attributes and methods
model_RationalLiteralExpression_numerator: Property = Property(name="numerator", type=StringType)
model_RationalLiteralExpression_denominator: Property = Property(name="denominator", type=StringType)
model_RationalLiteralExpression.attributes={model_RationalLiteralExpression_denominator, model_RationalLiteralExpression_numerator}

# model_BooleanLiteralExpression class attributes and methods

# BooleanExpression class attributes and methods

# model_TrueExpression class attributes and methods

# BooleanLiteralExpression class attributes and methods

# model_FalseExpression class attributes and methods

# model_ArrayLiteralExpression class attributes and methods

# EnumerableExpression class attributes and methods

# MultiaryExpression class attributes and methods

# model_IntegerRangeLiteralExpression class attributes and methods
model_IntegerRangeLiteralExpression_rightInclusive: Property = Property(name="rightInclusive", type=BooleanType)
model_IntegerRangeLiteralExpression_leftInclusive: Property = Property(name="leftInclusive", type=BooleanType)
model_IntegerRangeLiteralExpression.attributes={model_IntegerRangeLiteralExpression_rightInclusive, model_IntegerRangeLiteralExpression_leftInclusive}

# model_ElseExpression class attributes and methods

# model_RecordLiteralExpression class attributes and methods

# model_FieldAssignment class attributes and methods
model_FieldAssignment_reference: Property = Property(name="reference", type=StringType)
model_FieldAssignment.attributes={model_FieldAssignment_reference}

# model_EnumerationLiteralExpression class attributes and methods

# BinaryExpression class attributes and methods

# model_ReferenceExpression class attributes and methods

# model_IfThenElseExpression class attributes and methods

# model_NotExpression class attributes and methods

# model_ForallExpression class attributes and methods

# QuantifierExpression class attributes and methods

# model_ExistsExpression class attributes and methods

# model_ImplyExpression class attributes and methods

# model_OrExpression class attributes and methods

# model_AndExpression class attributes and methods

# model_XorExpression class attributes and methods

# model_EquivalenceExpression class attributes and methods

# PredicateExpression class attributes and methods

# model_EqualityExpression class attributes and methods

# EquivalenceExpression class attributes and methods

# model_InequalityExpression class attributes and methods

# model_GreaterEqualExpression class attributes and methods

# model_LessExpression class attributes and methods

# model_LessEqualExpression class attributes and methods

# model_AddExpression class attributes and methods

# model_SubtractExpression class attributes and methods

# model_MultiplyExpression class attributes and methods

# model_DivideExpression class attributes and methods

# model_DivExpression class attributes and methods

# model_ModExpression class attributes and methods

# model_UnaryMinusExpression class attributes and methods

# model_ComparisonExpression class attributes and methods

# model_UnaryPlusExpression class attributes and methods

# model_GreaterExpression class attributes and methods

# ComparisonExpression class attributes and methods

# ArgumentedElement class attributes and methods

# model_ArrayAccessExpression class attributes and methods

# model_RecordAccessExpression class attributes and methods
model_RecordAccessExpression_field: Property = Property(name="field", type=StringType)
model_RecordAccessExpression.attributes={model_RecordAccessExpression_field}

# model_SelectExpression class attributes and methods

# model_FunctionAccessExpression class attributes and methods

# AccessExpression class attributes and methods

# Relationships
comments0: BinaryAssociation = BinaryAssociation(
    name="comments0",
    ends={
        Property(name="model_Comment", type=model_CommentableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CommentableElement", type=model_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterDeclarations1: BinaryAssociation = BinaryAssociation(
    name="parameterDeclarations1",
    ends={
        Property(name="model_ParameterDeclaration", type=model_ParametricElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ParametricElement", type=model_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments2: BinaryAssociation = BinaryAssociation(
    name="arguments2",
    ends={
        Property(name="model_Expression", type=model_ArgumentedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArgumentedElement", type=model_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclarations3: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations3",
    ends={
        Property(name="model_TypeDeclaration", type=model_ExpressionPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpressionPackage", type=model_TypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantDeclarations4: BinaryAssociation = BinaryAssociation(
    name="constantDeclarations4",
    ends={
        Property(name="model_ConstantDeclaration", type=model_ExpressionPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpressionPackage5", type=model_ConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionDeclarations6: BinaryAssociation = BinaryAssociation(
    name="functionDeclarations6",
    ends={
        Property(name="model_FunctionDeclaration", type=model_ExpressionPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpressionPackage7", type=model_FunctionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicConstraintDefinitions8: BinaryAssociation = BinaryAssociation(
    name="basicConstraintDefinitions8",
    ends={
        Property(name="model_BasicConstraintDefinition", type=model_ExpressionPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpressionPackage9", type=model_BasicConstraintDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="model_Expression11", type=model_InitializableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_InitializableElement", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="model_Type", type=model_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Declaration", type=model_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference13: BinaryAssociation = BinaryAssociation(
    name="reference13",
    ends={
        Property(name="model_TypeDeclaration14", type=model_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TypeReference", type=model_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound15: BinaryAssociation = BinaryAssociation(
    name="lowerBound15",
    ends={
        Property(name="model_Expression16", type=model_SubrangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SubrangeTypeDefinition", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound17: BinaryAssociation = BinaryAssociation(
    name="upperBound17",
    ends={
        Property(name="model_Expression19", type=model_SubrangeTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SubrangeTypeDefinition18", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals20: BinaryAssociation = BinaryAssociation(
    name="literals20",
    ends={
        Property(name="model_EnumerationLiteralDefinition", type=model_EnumerationTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EnumerationTypeDefinition", type=model_EnumerationLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType21: BinaryAssociation = BinaryAssociation(
    name="elementType21",
    ends={
        Property(name="model_Type22", type=model_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArrayTypeDefinition", type=model_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size23: BinaryAssociation = BinaryAssociation(
    name="size23",
    ends={
        Property(name="model_Expression25", type=model_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArrayTypeDefinition24", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldDeclarations31: BinaryAssociation = BinaryAssociation(
    name="fieldDeclarations31",
    ends={
        Property(name="model_FieldDeclaration", type=model_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RecordTypeDefinition", type=model_FieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression32: BinaryAssociation = BinaryAssociation(
    name="expression32",
    ends={
        Property(name="model_Expression33", type=model_ConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConstraintDefinition", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand34: BinaryAssociation = BinaryAssociation(
    name="operand34",
    ends={
        Property(name="model_Expression35", type=model_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_UnaryExpression", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand36: BinaryAssociation = BinaryAssociation(
    name="leftOperand36",
    ends={
        Property(name="model_Expression37", type=model_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BinaryExpression", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand38: BinaryAssociation = BinaryAssociation(
    name="rightOperand38",
    ends={
        Property(name="model_Expression40", type=model_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BinaryExpression39", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands41: BinaryAssociation = BinaryAssociation(
    name="operands41",
    ends={
        Property(name="model_Expression42", type=model_MultiaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MultiaryExpression", type=model_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterTypes26: BinaryAssociation = BinaryAssociation(
    name="parameterTypes26",
    ends={
        Property(name="model_Type27", type=model_FunctionTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FunctionTypeDefinition", type=model_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType28: BinaryAssociation = BinaryAssociation(
    name="returnType28",
    ends={
        Property(name="model_Type30", type=model_FunctionTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FunctionTypeDefinition29", type=model_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand43: BinaryAssociation = BinaryAssociation(
    name="operand43",
    ends={
        Property(name="model_Expression44", type=model_AccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AccessExpression", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fieldAssignments45: BinaryAssociation = BinaryAssociation(
    name="fieldAssignments45",
    ends={
        Property(name="model_FieldAssignment", type=model_RecordLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RecordLiteralExpression", type=model_FieldAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference46: BinaryAssociation = BinaryAssociation(
    name="reference46",
    ends={
        Property(name="model_EnumerationLiteralDefinition47", type=model_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EnumerationLiteralExpression", type=model_EnumerationLiteralDefinition, multiplicity=Multiplicity(1, 1))
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="model_Expression50", type=model_FieldAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FieldAssignment49", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration51: BinaryAssociation = BinaryAssociation(
    name="declaration51",
    ends={
        Property(name="model_Declaration52", type=model_ReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ReferenceExpression", type=model_Declaration, multiplicity=Multiplicity(1, 1))
    }
)
condition53: BinaryAssociation = BinaryAssociation(
    name="condition53",
    ends={
        Property(name="model_Expression54", type=model_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IfThenElseExpression", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then55: BinaryAssociation = BinaryAssociation(
    name="then55",
    ends={
        Property(name="model_Expression57", type=model_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IfThenElseExpression56", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else58: BinaryAssociation = BinaryAssociation(
    name="else58",
    ends={
        Property(name="model_Expression60", type=model_IfThenElseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IfThenElseExpression59", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_model_ExpressionPackage_NamedElement = Generalization(general=NamedElement, specific=model_ExpressionPackage)
gen_model_ExpressionPackage_ParametricElement = Generalization(general=ParametricElement, specific=model_ExpressionPackage)
gen_model_InitializableElement_NamedElement = Generalization(general=NamedElement, specific=model_InitializableElement)
gen_model_Declaration_NamedElement = Generalization(general=NamedElement, specific=model_Declaration)
gen_model_ValueDeclaration_Declaration = Generalization(general=Declaration, specific=model_ValueDeclaration)
gen_model_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=model_FunctionDeclaration)
gen_model_FunctionDeclaration_ParametricElement = Generalization(general=ParametricElement, specific=model_FunctionDeclaration)
gen_model_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=model_TypeDeclaration)
gen_model_VariableDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=model_VariableDeclaration)
gen_model_VariableDeclaration_InitializableElement = Generalization(general=InitializableElement, specific=model_VariableDeclaration)
gen_model_FieldDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=model_FieldDeclaration)
gen_model_LambdaDeclaration_InitializableElement = Generalization(general=InitializableElement, specific=model_LambdaDeclaration)
gen_model_LambdaDeclaration_FunctionDeclaration = Generalization(general=FunctionDeclaration, specific=model_LambdaDeclaration)
gen_model_TypeReference_Type = Generalization(general=Type, specific=model_TypeReference)
gen_model_TypeDefinition_Type = Generalization(general=Type, specific=model_TypeDefinition)
gen_model_NumericalTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=model_NumericalTypeDefinition)
gen_model_CompositeTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=model_CompositeTypeDefinition)
gen_model_VoidTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=model_VoidTypeDefinition)
gen_model_BooleanTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=model_BooleanTypeDefinition)
gen_model_IntegerTypeDefinition_NumericalTypeDefinition = Generalization(general=NumericalTypeDefinition, specific=model_IntegerTypeDefinition)
gen_model_RationalTypeDefinition_NumericalTypeDefinition = Generalization(general=NumericalTypeDefinition, specific=model_RationalTypeDefinition)
gen_model_DecimalTypeDefinition_NumericalTypeDefinition = Generalization(general=NumericalTypeDefinition, specific=model_DecimalTypeDefinition)
gen_model_SubrangeTypeDefinition_NumericalTypeDefinition = Generalization(general=NumericalTypeDefinition, specific=model_SubrangeTypeDefinition)
gen_model_SubrangeTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=model_SubrangeTypeDefinition)
gen_model_EnumerableTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=model_EnumerableTypeDefinition)
gen_model_EnumerationTypeDefinition_EnumerableTypeDefinition = Generalization(general=EnumerableTypeDefinition, specific=model_EnumerationTypeDefinition)
gen_model_EnumerationLiteralDefinition_NamedElement = Generalization(general=NamedElement, specific=model_EnumerationLiteralDefinition)
gen_model_ArrayTypeDefinition_EnumerableTypeDefinition = Generalization(general=EnumerableTypeDefinition, specific=model_ArrayTypeDefinition)
gen_model_IntegerRangeTypeDefinition_EnumerableTypeDefinition = Generalization(general=EnumerableTypeDefinition, specific=model_IntegerRangeTypeDefinition)
gen_model_FunctionTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=model_FunctionTypeDefinition)
gen_model_ConstantDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=model_ConstantDeclaration)
gen_model_ConstantDeclaration_InitializableElement = Generalization(general=InitializableElement, specific=model_ConstantDeclaration)
gen_model_ParameterDeclaration_ValueDeclaration = Generalization(general=ValueDeclaration, specific=model_ParameterDeclaration)
gen_model_RecordTypeDefinition_CompositeTypeDefinition = Generalization(general=CompositeTypeDefinition, specific=model_RecordTypeDefinition)
gen_model_BasicConstraintDefinition_ConstraintDefinition = Generalization(general=ConstraintDefinition, specific=model_BasicConstraintDefinition)
gen_model_NullaryExpression_Expression = Generalization(general=Expression, specific=model_NullaryExpression)
gen_model_UnaryExpression_Expression = Generalization(general=Expression, specific=model_UnaryExpression)
gen_model_BinaryExpression_Expression = Generalization(general=Expression, specific=model_BinaryExpression)
gen_model_MultiaryExpression_Expression = Generalization(general=Expression, specific=model_MultiaryExpression)
gen_model_ArithmeticExpression_Expression = Generalization(general=Expression, specific=model_ArithmeticExpression)
gen_model_LogicExpression_Expression = Generalization(general=Expression, specific=model_LogicExpression)
gen_model_BooleanExpression_LogicExpression = Generalization(general=LogicExpression, specific=model_BooleanExpression)
gen_model_PredicateExpression_LogicExpression = Generalization(general=LogicExpression, specific=model_PredicateExpression)
gen_model_OpaqueExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_OpaqueExpression)
gen_model_DefaultExpression_ElseExpression = Generalization(general=ElseExpression, specific=model_DefaultExpression)
gen_model_QuantifierExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=model_QuantifierExpression)
gen_model_QuantifierExpression_ParametricElement = Generalization(general=ParametricElement, specific=model_QuantifierExpression)
gen_model_QuantifierExpression_LogicExpression = Generalization(general=LogicExpression, specific=model_QuantifierExpression)
gen_model_AccessExpression_Expression = Generalization(general=Expression, specific=model_AccessExpression)
gen_model_LiteralExpression_Expression = Generalization(general=Expression, specific=model_LiteralExpression)
gen_model_EnumerableExpression_Expression = Generalization(general=Expression, specific=model_EnumerableExpression)
gen_model_ArithmeticLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_ArithmeticLiteralExpression)
gen_model_ArithmeticLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_ArithmeticLiteralExpression)
gen_model_ArithmeticLiteralExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_ArithmeticLiteralExpression)
gen_model_IntegerLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=model_IntegerLiteralExpression)
gen_model_DecimalLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=model_DecimalLiteralExpression)
gen_model_RationalLiteralExpression_ArithmeticLiteralExpression = Generalization(general=ArithmeticLiteralExpression, specific=model_RationalLiteralExpression)
gen_model_BooleanLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_BooleanLiteralExpression)
gen_model_BooleanLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_BooleanLiteralExpression)
gen_model_BooleanLiteralExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_BooleanLiteralExpression)
gen_model_TrueExpression_BooleanLiteralExpression = Generalization(general=BooleanLiteralExpression, specific=model_TrueExpression)
gen_model_FalseExpression_BooleanLiteralExpression = Generalization(general=BooleanLiteralExpression, specific=model_FalseExpression)
gen_model_ArrayLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_ArrayLiteralExpression)
gen_model_ArrayLiteralExpression_EnumerableExpression = Generalization(general=EnumerableExpression, specific=model_ArrayLiteralExpression)
gen_model_ArrayLiteralExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_ArrayLiteralExpression)
gen_model_IntegerRangeLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_IntegerRangeLiteralExpression)
gen_model_ElseExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_ElseExpression)
gen_model_ElseExpression_LogicExpression = Generalization(general=LogicExpression, specific=model_ElseExpression)
gen_model_RecordLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_RecordLiteralExpression)
gen_model_EnumerationLiteralExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_EnumerationLiteralExpression)
gen_model_EnumerationLiteralExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=model_EnumerationLiteralExpression)
gen_model_IntegerRangeLiteralExpression_EnumerableExpression = Generalization(general=EnumerableExpression, specific=model_IntegerRangeLiteralExpression)
gen_model_IntegerRangeLiteralExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_IntegerRangeLiteralExpression)
gen_model_ReferenceExpression_NullaryExpression = Generalization(general=NullaryExpression, specific=model_ReferenceExpression)
gen_model_IfThenElseExpression_Expression = Generalization(general=Expression, specific=model_IfThenElseExpression)
gen_model_NotExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_NotExpression)
gen_model_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=model_NotExpression)
gen_model_ForallExpression_QuantifierExpression = Generalization(general=QuantifierExpression, specific=model_ForallExpression)
gen_model_ExistsExpression_QuantifierExpression = Generalization(general=QuantifierExpression, specific=model_ExistsExpression)
gen_model_ImplyExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_ImplyExpression)
gen_model_ImplyExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_ImplyExpression)
gen_model_OrExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_OrExpression)
gen_model_OrExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_OrExpression)
gen_model_AndExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_AndExpression)
gen_model_AndExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_AndExpression)
gen_model_XorExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=model_XorExpression)
gen_model_XorExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_XorExpression)
gen_model_EquivalenceExpression_PredicateExpression = Generalization(general=PredicateExpression, specific=model_EquivalenceExpression)
gen_model_EquivalenceExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_EquivalenceExpression)
gen_model_EqualityExpression_EquivalenceExpression = Generalization(general=EquivalenceExpression, specific=model_EqualityExpression)
gen_model_InequalityExpression_EquivalenceExpression = Generalization(general=EquivalenceExpression, specific=model_InequalityExpression)
gen_model_GreaterExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=model_GreaterExpression)
gen_model_GreaterEqualExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=model_GreaterEqualExpression)
gen_model_LessExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=model_LessExpression)
gen_model_LessEqualExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=model_LessEqualExpression)
gen_model_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_AddExpression)
gen_model_AddExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_AddExpression)
gen_model_SubtractExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_SubtractExpression)
gen_model_SubtractExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_SubtractExpression)
gen_model_MultiplyExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_MultiplyExpression)
gen_model_MultiplyExpression_MultiaryExpression = Generalization(general=MultiaryExpression, specific=model_MultiplyExpression)
gen_model_DivideExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_DivideExpression)
gen_model_DivideExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_DivideExpression)
gen_model_DivExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_DivExpression)
gen_model_DivExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_DivExpression)
gen_model_ModExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_ModExpression)
gen_model_ModExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_ModExpression)
gen_model_UnaryMinusExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_UnaryMinusExpression)
gen_model_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=model_UnaryMinusExpression)
gen_model_ComparisonExpression_PredicateExpression = Generalization(general=PredicateExpression, specific=model_ComparisonExpression)
gen_model_UnaryPlusExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=model_UnaryPlusExpression)
gen_model_ComparisonExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=model_ComparisonExpression)
gen_model_FunctionAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=model_FunctionAccessExpression)
gen_model_FunctionAccessExpression_ArgumentedElement = Generalization(general=ArgumentedElement, specific=model_FunctionAccessExpression)
gen_model_ArrayAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=model_ArrayAccessExpression)
gen_model_ArrayAccessExpression_ArgumentedElement = Generalization(general=ArgumentedElement, specific=model_ArrayAccessExpression)
gen_model_RecordAccessExpression_AccessExpression = Generalization(general=AccessExpression, specific=model_RecordAccessExpression)
gen_model_SelectExpression_AccessExpression = Generalization(general=AccessExpression, specific=model_SelectExpression)
gen_model_UnaryPlusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=model_UnaryPlusExpression)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_CommentableElement, model_Comment, model_ParametricElement, model_ParameterDeclaration, model_ArgumentedElement, model_Expression, model_ExpressionPackage, NamedElement, ParametricElement, model_TypeDeclaration, model_ConstantDeclaration, model_FunctionDeclaration, model_BasicConstraintDefinition, model_InitializableElement, model_Declaration, model_Type, model_ValueDeclaration, Declaration, model_VariableDeclaration, ValueDeclaration, InitializableElement, model_NamedElement, model_LambdaDeclaration, FunctionDeclaration, model_TypeReference, Type, model_TypeDefinition, model_NumericalTypeDefinition, TypeDefinition, model_CompositeTypeDefinition, model_VoidTypeDefinition, model_BooleanTypeDefinition, model_IntegerTypeDefinition, NumericalTypeDefinition, model_RationalTypeDefinition, model_DecimalTypeDefinition, model_SubrangeTypeDefinition, CompositeTypeDefinition, model_EnumerableTypeDefinition, model_EnumerationTypeDefinition, EnumerableTypeDefinition, model_EnumerationLiteralDefinition, model_ArrayTypeDefinition, model_IntegerRangeTypeDefinition, model_FunctionTypeDefinition, model_FieldDeclaration, model_RecordTypeDefinition, model_ConstraintDefinition, ConstraintDefinition, model_NullaryExpression, Expression, model_UnaryExpression, model_BinaryExpression, model_MultiaryExpression, model_ArithmeticExpression, model_LogicExpression, model_BooleanExpression, LogicExpression, model_PredicateExpression, model_OpaqueExpression, NullaryExpression, model_DefaultExpression, ElseExpression, model_QuantifierExpression, UnaryExpression, model_AccessExpression, model_LiteralExpression, model_EnumerableExpression, model_ArithmeticLiteralExpression, LiteralExpression, ArithmeticExpression, model_IntegerLiteralExpression, ArithmeticLiteralExpression, model_DecimalLiteralExpression, model_RationalLiteralExpression, model_BooleanLiteralExpression, BooleanExpression, model_TrueExpression, BooleanLiteralExpression, model_FalseExpression, model_ArrayLiteralExpression, EnumerableExpression, MultiaryExpression, model_IntegerRangeLiteralExpression, model_ElseExpression, model_RecordLiteralExpression, model_FieldAssignment, model_EnumerationLiteralExpression, BinaryExpression, model_ReferenceExpression, model_IfThenElseExpression, model_NotExpression, model_ForallExpression, QuantifierExpression, model_ExistsExpression, model_ImplyExpression, model_OrExpression, model_AndExpression, model_XorExpression, model_EquivalenceExpression, PredicateExpression, model_EqualityExpression, EquivalenceExpression, model_InequalityExpression, model_GreaterEqualExpression, model_LessExpression, model_LessEqualExpression, model_AddExpression, model_SubtractExpression, model_MultiplyExpression, model_DivideExpression, model_DivExpression, model_ModExpression, model_UnaryMinusExpression, model_ComparisonExpression, model_UnaryPlusExpression, model_GreaterExpression, ComparisonExpression, ArgumentedElement, model_ArrayAccessExpression, model_RecordAccessExpression, model_SelectExpression, model_FunctionAccessExpression, AccessExpression},
    associations={comments0, parameterDeclarations1, arguments2, typeDeclarations3, constantDeclarations4, functionDeclarations6, basicConstraintDefinitions8, expression10, type12, reference13, lowerBound15, upperBound17, literals20, elementType21, size23, fieldDeclarations31, expression32, operand34, leftOperand36, rightOperand38, operands41, parameterTypes26, returnType28, operand43, fieldAssignments45, reference46, value48, declaration51, condition53, then55, else58},
    generalizations={gen_model_ExpressionPackage_NamedElement, gen_model_ExpressionPackage_ParametricElement, gen_model_InitializableElement_NamedElement, gen_model_Declaration_NamedElement, gen_model_ValueDeclaration_Declaration, gen_model_FunctionDeclaration_Declaration, gen_model_FunctionDeclaration_ParametricElement, gen_model_TypeDeclaration_Declaration, gen_model_VariableDeclaration_ValueDeclaration, gen_model_VariableDeclaration_InitializableElement, gen_model_FieldDeclaration_ValueDeclaration, gen_model_LambdaDeclaration_InitializableElement, gen_model_LambdaDeclaration_FunctionDeclaration, gen_model_TypeReference_Type, gen_model_TypeDefinition_Type, gen_model_NumericalTypeDefinition_TypeDefinition, gen_model_CompositeTypeDefinition_TypeDefinition, gen_model_VoidTypeDefinition_TypeDefinition, gen_model_BooleanTypeDefinition_TypeDefinition, gen_model_IntegerTypeDefinition_NumericalTypeDefinition, gen_model_RationalTypeDefinition_NumericalTypeDefinition, gen_model_DecimalTypeDefinition_NumericalTypeDefinition, gen_model_SubrangeTypeDefinition_NumericalTypeDefinition, gen_model_SubrangeTypeDefinition_CompositeTypeDefinition, gen_model_EnumerableTypeDefinition_CompositeTypeDefinition, gen_model_EnumerationTypeDefinition_EnumerableTypeDefinition, gen_model_EnumerationLiteralDefinition_NamedElement, gen_model_ArrayTypeDefinition_EnumerableTypeDefinition, gen_model_IntegerRangeTypeDefinition_EnumerableTypeDefinition, gen_model_FunctionTypeDefinition_CompositeTypeDefinition, gen_model_ConstantDeclaration_ValueDeclaration, gen_model_ConstantDeclaration_InitializableElement, gen_model_ParameterDeclaration_ValueDeclaration, gen_model_RecordTypeDefinition_CompositeTypeDefinition, gen_model_BasicConstraintDefinition_ConstraintDefinition, gen_model_NullaryExpression_Expression, gen_model_UnaryExpression_Expression, gen_model_BinaryExpression_Expression, gen_model_MultiaryExpression_Expression, gen_model_ArithmeticExpression_Expression, gen_model_LogicExpression_Expression, gen_model_BooleanExpression_LogicExpression, gen_model_PredicateExpression_LogicExpression, gen_model_OpaqueExpression_NullaryExpression, gen_model_DefaultExpression_ElseExpression, gen_model_QuantifierExpression_UnaryExpression, gen_model_QuantifierExpression_ParametricElement, gen_model_QuantifierExpression_LogicExpression, gen_model_AccessExpression_Expression, gen_model_LiteralExpression_Expression, gen_model_EnumerableExpression_Expression, gen_model_ArithmeticLiteralExpression_NullaryExpression, gen_model_ArithmeticLiteralExpression_LiteralExpression, gen_model_ArithmeticLiteralExpression_ArithmeticExpression, gen_model_IntegerLiteralExpression_ArithmeticLiteralExpression, gen_model_DecimalLiteralExpression_ArithmeticLiteralExpression, gen_model_RationalLiteralExpression_ArithmeticLiteralExpression, gen_model_BooleanLiteralExpression_NullaryExpression, gen_model_BooleanLiteralExpression_LiteralExpression, gen_model_BooleanLiteralExpression_BooleanExpression, gen_model_TrueExpression_BooleanLiteralExpression, gen_model_FalseExpression_BooleanLiteralExpression, gen_model_ArrayLiteralExpression_LiteralExpression, gen_model_ArrayLiteralExpression_EnumerableExpression, gen_model_ArrayLiteralExpression_MultiaryExpression, gen_model_IntegerRangeLiteralExpression_LiteralExpression, gen_model_ElseExpression_NullaryExpression, gen_model_ElseExpression_LogicExpression, gen_model_RecordLiteralExpression_LiteralExpression, gen_model_EnumerationLiteralExpression_NullaryExpression, gen_model_EnumerationLiteralExpression_LiteralExpression, gen_model_IntegerRangeLiteralExpression_EnumerableExpression, gen_model_IntegerRangeLiteralExpression_BinaryExpression, gen_model_ReferenceExpression_NullaryExpression, gen_model_IfThenElseExpression_Expression, gen_model_NotExpression_BooleanExpression, gen_model_NotExpression_UnaryExpression, gen_model_ForallExpression_QuantifierExpression, gen_model_ExistsExpression_QuantifierExpression, gen_model_ImplyExpression_BooleanExpression, gen_model_ImplyExpression_BinaryExpression, gen_model_OrExpression_BooleanExpression, gen_model_OrExpression_MultiaryExpression, gen_model_AndExpression_BooleanExpression, gen_model_AndExpression_MultiaryExpression, gen_model_XorExpression_BooleanExpression, gen_model_XorExpression_MultiaryExpression, gen_model_EquivalenceExpression_PredicateExpression, gen_model_EquivalenceExpression_BinaryExpression, gen_model_EqualityExpression_EquivalenceExpression, gen_model_InequalityExpression_EquivalenceExpression, gen_model_GreaterExpression_ComparisonExpression, gen_model_GreaterEqualExpression_ComparisonExpression, gen_model_LessExpression_ComparisonExpression, gen_model_LessEqualExpression_ComparisonExpression, gen_model_AddExpression_ArithmeticExpression, gen_model_AddExpression_MultiaryExpression, gen_model_SubtractExpression_ArithmeticExpression, gen_model_SubtractExpression_BinaryExpression, gen_model_MultiplyExpression_ArithmeticExpression, gen_model_MultiplyExpression_MultiaryExpression, gen_model_DivideExpression_ArithmeticExpression, gen_model_DivideExpression_BinaryExpression, gen_model_DivExpression_ArithmeticExpression, gen_model_DivExpression_BinaryExpression, gen_model_ModExpression_ArithmeticExpression, gen_model_ModExpression_BinaryExpression, gen_model_UnaryMinusExpression_ArithmeticExpression, gen_model_UnaryMinusExpression_UnaryExpression, gen_model_ComparisonExpression_PredicateExpression, gen_model_UnaryPlusExpression_ArithmeticExpression, gen_model_ComparisonExpression_BinaryExpression, gen_model_FunctionAccessExpression_AccessExpression, gen_model_FunctionAccessExpression_ArgumentedElement, gen_model_ArrayAccessExpression_AccessExpression, gen_model_ArrayAccessExpression_ArgumentedElement, gen_model_RecordAccessExpression_AccessExpression, gen_model_SelectExpression_AccessExpression, gen_model_UnaryPlusExpression_UnaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)