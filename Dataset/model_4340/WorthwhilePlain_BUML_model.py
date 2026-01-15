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
edu_Program = Class(name="edu::Program")
ASTNode = Class(name="ASTNode")
edu_FunctionDeclaration = Class(name="edu::FunctionDeclaration")
edu_Block = Class(name="edu::Block")
edu_Axiom = Class(name="edu::Axiom")
edu_ASTNode = Class(name="edu::ASTNode", is_abstract=True)
edu_Addition = Class(name="edu::Addition")
BinaryExpression = Class(name="BinaryExpression")
edu_UnaryExpression = Class(name="edu::UnaryExpression", is_abstract=True)
edu_ArrayLiteral = Class(name="edu::ArrayLiteral")
Literal = Class(name="Literal")
edu_Literal = Class(name="edu::Literal", is_abstract=True)
edu_ArrayType = Class(name="edu::ArrayType")
Type = Class(name="Type")
edu_PrimitiveType = Class(name="edu::PrimitiveType", is_abstract=True)
edu_BinaryExpression = Class(name="edu::BinaryExpression", is_abstract=True)
Expression = Class(name="Expression")
edu_Expression = Class(name="edu::Expression", is_abstract=True)
edu_FunctionCallPreconditionAssertion = Class(name="edu::FunctionCallPreconditionAssertion")
GuardAssertion = Class(name="GuardAssertion")
edu_FunctionCall = Class(name="edu::FunctionCall")
edu_DivisorNotZeroAssertion = Class(name="edu::DivisorNotZeroAssertion")
edu_Annotation = Class(name="edu::Annotation", is_abstract=True)
Statement = Class(name="Statement")
edu_Type = Class(name="edu::Type", is_abstract=True)
edu_Assertion = Class(name="edu::Assertion")
Annotation = Class(name="Annotation")
edu_GuardAssertion = Class(name="edu::GuardAssertion")
Assertion = Class(name="Assertion")
edu_Assumption = Class(name="edu::Assumption")
edu_Statement = Class(name="edu::Statement", is_abstract=True)
edu_BooleanLiteral = Class(name="edu::BooleanLiteral")
edu_Assignment = Class(name="edu::Assignment")
edu_VariableReference = Class(name="edu::VariableReference")
edu_VariableDeclaration = Class(name="edu::VariableDeclaration")
edu_Conjunction = Class(name="edu::Conjunction")
edu_Disjunction = Class(name="edu::Disjunction")
edu_Division = Class(name="edu::Division")
edu_Equal = Class(name="edu::Equal")
edu_Equivalence = Class(name="edu::Equivalence")
edu_ExistsQuantifier = Class(name="edu::ExistsQuantifier")
QuantifiedExpression = Class(name="QuantifiedExpression")
edu_BooleanType = Class(name="edu::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
edu_Conditional = Class(name="edu::Conditional")
edu_Precondition = Class(name="edu::Precondition")
edu_Postcondition = Class(name="edu::Postcondition")
edu_QuantifiedExpression = Class(name="edu::QuantifiedExpression", is_abstract=True)
edu_ForAllQuantifier = Class(name="edu::ForAllQuantifier")
edu_GreaterOrEqual = Class(name="edu::GreaterOrEqual")
edu_Implication = Class(name="edu::Implication")
edu_IntegerLiteral = Class(name="edu::IntegerLiteral")
edu_IntegerType = Class(name="edu::IntegerType")
edu_Invariant = Class(name="edu::Invariant")
edu_Less = Class(name="edu::Less")
FunctionAnnotation = Class(name="FunctionAnnotation")
edu_Greater = Class(name="edu::Greater")
edu_Minus = Class(name="edu::Minus")
Sign = Class(name="Sign")
edu_Sign = Class(name="edu::Sign", is_abstract=True)
UnaryExpression = Class(name="UnaryExpression")
edu_Modulus = Class(name="edu::Modulus")
edu_Multiplication = Class(name="edu::Multiplication")
edu_Negation = Class(name="edu::Negation")
edu_Plus = Class(name="edu::Plus")
edu_ReturnStatement = Class(name="edu::ReturnStatement")
edu_LessOrEqual = Class(name="edu::LessOrEqual")
edu_Loop = Class(name="edu::Loop")
SymbolReference = Class(name="SymbolReference")
edu_ReturnValueReference = Class(name="edu::ReturnValueReference")
edu_SymbolReference = Class(name="edu::SymbolReference")
edu_Subtraction = Class(name="edu::Subtraction")
edu_Unequal = Class(name="edu::Unequal")
edu_ArrayAccess = Class(name="edu::ArrayAccess")
edu_ExpressionToExpressionMap = Class(name="edu::ExpressionToExpressionMap")
edu_FunctionAnnotation = Class(name="edu::FunctionAnnotation", is_abstract=True)
edu_TernaryExpression = Class(name="edu::TernaryExpression")
edu_ExpressionEvaluation = Class(name="edu::ExpressionEvaluation")
edu_ArrayFunction = Class(name="edu::ArrayFunction")
edu_visitor_IASTNodeVisitor = Class(name="edu::visitor::IASTNodeVisitor", is_abstract=True)
edu_LetExpression = Class(name="edu::LetExpression")

# edu_Program class attributes and methods
edu_Program_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Program.methods={edu_Program_m_accept}

# ASTNode class attributes and methods

# edu_FunctionDeclaration class attributes and methods
edu_FunctionDeclaration_name: Property = Property(name="name", type=StringType)
edu_FunctionDeclaration_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_FunctionDeclaration.attributes={edu_FunctionDeclaration_name}
edu_FunctionDeclaration.methods={edu_FunctionDeclaration_m_accept}

# edu_Block class attributes and methods
edu_Block_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Block.methods={edu_Block_m_accept}

# edu_Axiom class attributes and methods
edu_Axiom_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Axiom.methods={edu_Axiom_m_accept}

# edu_ASTNode class attributes and methods
edu_ASTNode_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ASTNode.methods={edu_ASTNode_m_accept}

# edu_Addition class attributes and methods
edu_Addition_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Addition.methods={edu_Addition_m_accept}

# BinaryExpression class attributes and methods

# edu_UnaryExpression class attributes and methods
edu_UnaryExpression_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_UnaryExpression.methods={edu_UnaryExpression_m_accept}

# edu_ArrayLiteral class attributes and methods
edu_ArrayLiteral_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ArrayLiteral.methods={edu_ArrayLiteral_m_accept}

# Literal class attributes and methods

# edu_Literal class attributes and methods
edu_Literal_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Literal.methods={edu_Literal_m_accept}

# edu_ArrayType class attributes and methods
edu_ArrayType_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ArrayType.methods={edu_ArrayType_m_accept}

# Type class attributes and methods

# edu_PrimitiveType class attributes and methods
edu_PrimitiveType_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_PrimitiveType.methods={edu_PrimitiveType_m_accept}

# edu_BinaryExpression class attributes and methods
edu_BinaryExpression_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_BinaryExpression.methods={edu_BinaryExpression_m_accept}

# Expression class attributes and methods

# edu_Expression class attributes and methods
edu_Expression_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Expression.methods={edu_Expression_m_accept}

# edu_FunctionCallPreconditionAssertion class attributes and methods
edu_FunctionCallPreconditionAssertion_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_FunctionCallPreconditionAssertion.methods={edu_FunctionCallPreconditionAssertion_m_accept}

# GuardAssertion class attributes and methods

# edu_FunctionCall class attributes and methods
edu_FunctionCall_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_FunctionCall.methods={edu_FunctionCall_m_accept}

# edu_DivisorNotZeroAssertion class attributes and methods
edu_DivisorNotZeroAssertion_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_DivisorNotZeroAssertion.methods={edu_DivisorNotZeroAssertion_m_accept}

# edu_Annotation class attributes and methods
edu_Annotation_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Annotation.methods={edu_Annotation_m_accept}

# Statement class attributes and methods

# edu_Type class attributes and methods
edu_Type_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Type.methods={edu_Type_m_accept}

# edu_Assertion class attributes and methods
edu_Assertion_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Assertion.methods={edu_Assertion_m_accept}

# Annotation class attributes and methods

# edu_GuardAssertion class attributes and methods
edu_GuardAssertion_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_GuardAssertion.methods={edu_GuardAssertion_m_accept}

# Assertion class attributes and methods

# edu_Assumption class attributes and methods
edu_Assumption_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Assumption.methods={edu_Assumption_m_accept}

# edu_Statement class attributes and methods
edu_Statement_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Statement.methods={edu_Statement_m_accept}

# edu_BooleanLiteral class attributes and methods
edu_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
edu_BooleanLiteral_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_BooleanLiteral_m_getValue: Method = Method(name="getValue", parameters={}, type=BooleanType)
edu_BooleanLiteral.attributes={edu_BooleanLiteral_value}
edu_BooleanLiteral.methods={edu_BooleanLiteral_m_getValue, edu_BooleanLiteral_m_accept}

# edu_Assignment class attributes and methods
edu_Assignment_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Assignment.methods={edu_Assignment_m_accept}

# edu_VariableReference class attributes and methods
edu_VariableReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_VariableReference.methods={edu_VariableReference_m_accept}

# edu_VariableDeclaration class attributes and methods
edu_VariableDeclaration_name: Property = Property(name="name", type=StringType)
edu_VariableDeclaration_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_VariableDeclaration.attributes={edu_VariableDeclaration_name}
edu_VariableDeclaration.methods={edu_VariableDeclaration_m_accept}

# edu_Conjunction class attributes and methods
edu_Conjunction_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Conjunction.methods={edu_Conjunction_m_accept}

# edu_Disjunction class attributes and methods
edu_Disjunction_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Disjunction.methods={edu_Disjunction_m_accept}

# edu_Division class attributes and methods
edu_Division_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Division.methods={edu_Division_m_accept}

# edu_Equal class attributes and methods
edu_Equal_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Equal.methods={edu_Equal_m_accept}

# edu_Equivalence class attributes and methods
edu_Equivalence_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Equivalence.methods={edu_Equivalence_m_accept}

# edu_ExistsQuantifier class attributes and methods
edu_ExistsQuantifier_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ExistsQuantifier.methods={edu_ExistsQuantifier_m_accept}

# QuantifiedExpression class attributes and methods

# edu_BooleanType class attributes and methods
edu_BooleanType_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_BooleanType.methods={edu_BooleanType_m_accept}

# PrimitiveType class attributes and methods

# edu_Conditional class attributes and methods
edu_Conditional_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Conditional.methods={edu_Conditional_m_accept}

# edu_Precondition class attributes and methods
edu_Precondition_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Precondition.methods={edu_Precondition_m_accept}

# edu_Postcondition class attributes and methods
edu_Postcondition_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Postcondition.methods={edu_Postcondition_m_accept}

# edu_QuantifiedExpression class attributes and methods
edu_QuantifiedExpression_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_QuantifiedExpression.methods={edu_QuantifiedExpression_m_accept}

# edu_ForAllQuantifier class attributes and methods
edu_ForAllQuantifier_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ForAllQuantifier.methods={edu_ForAllQuantifier_m_accept}

# edu_GreaterOrEqual class attributes and methods
edu_GreaterOrEqual_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_GreaterOrEqual.methods={edu_GreaterOrEqual_m_accept}

# edu_Implication class attributes and methods
edu_Implication_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Implication.methods={edu_Implication_m_accept}

# edu_IntegerLiteral class attributes and methods
edu_IntegerLiteral_value: Property = Property(name="value", type=StringType)
edu_IntegerLiteral_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_IntegerLiteral.attributes={edu_IntegerLiteral_value}
edu_IntegerLiteral.methods={edu_IntegerLiteral_m_accept}

# edu_IntegerType class attributes and methods
edu_IntegerType_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_IntegerType.methods={edu_IntegerType_m_accept}

# edu_Invariant class attributes and methods
edu_Invariant_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Invariant.methods={edu_Invariant_m_accept}

# edu_Less class attributes and methods
edu_Less_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Less.methods={edu_Less_m_accept}

# FunctionAnnotation class attributes and methods

# edu_Greater class attributes and methods
edu_Greater_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Greater.methods={edu_Greater_m_accept}

# edu_Minus class attributes and methods
edu_Minus_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Minus.methods={edu_Minus_m_accept}

# Sign class attributes and methods

# edu_Sign class attributes and methods
edu_Sign_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Sign.methods={edu_Sign_m_accept}

# UnaryExpression class attributes and methods

# edu_Modulus class attributes and methods
edu_Modulus_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Modulus.methods={edu_Modulus_m_accept}

# edu_Multiplication class attributes and methods
edu_Multiplication_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Multiplication.methods={edu_Multiplication_m_accept}

# edu_Negation class attributes and methods
edu_Negation_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Negation.methods={edu_Negation_m_accept}

# edu_Plus class attributes and methods
edu_Plus_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Plus.methods={edu_Plus_m_accept}

# edu_ReturnStatement class attributes and methods
edu_ReturnStatement_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ReturnStatement.methods={edu_ReturnStatement_m_accept}

# edu_LessOrEqual class attributes and methods
edu_LessOrEqual_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_LessOrEqual.methods={edu_LessOrEqual_m_accept}

# edu_Loop class attributes and methods
edu_Loop_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Loop.methods={edu_Loop_m_accept}

# SymbolReference class attributes and methods

# edu_ReturnValueReference class attributes and methods
edu_ReturnValueReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ReturnValueReference.methods={edu_ReturnValueReference_m_accept}

# edu_SymbolReference class attributes and methods
edu_SymbolReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_SymbolReference.methods={edu_SymbolReference_m_accept}

# edu_Subtraction class attributes and methods
edu_Subtraction_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Subtraction.methods={edu_Subtraction_m_accept}

# edu_Unequal class attributes and methods
edu_Unequal_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_Unequal.methods={edu_Unequal_m_accept}

# edu_ArrayAccess class attributes and methods
edu_ArrayAccess_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ArrayAccess.methods={edu_ArrayAccess_m_accept}

# edu_ExpressionToExpressionMap class attributes and methods

# edu_FunctionAnnotation class attributes and methods
edu_FunctionAnnotation_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_FunctionAnnotation.methods={edu_FunctionAnnotation_m_accept}

# edu_TernaryExpression class attributes and methods
edu_TernaryExpression_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_TernaryExpression.methods={edu_TernaryExpression_m_accept}

# edu_ExpressionEvaluation class attributes and methods

# edu_ArrayFunction class attributes and methods
edu_ArrayFunction_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
edu_ArrayFunction.methods={edu_ArrayFunction_m_accept}

# edu_visitor_IASTNodeVisitor class attributes and methods
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='node')})
edu_visitor_IASTNodeVisitor.methods={edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit, edu_visitor_IASTNodeVisitor_m_visit}

# edu_LetExpression class attributes and methods

# Relationships
functionDeclarations0: BinaryAssociation = BinaryAssociation(
    name="functionDeclarations0",
    ends={
        Property(name="edu_FunctionDeclaration", type=edu_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Program", type=edu_FunctionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainBlock1: BinaryAssociation = BinaryAssociation(
    name="mainBlock1",
    ends={
        Property(name="edu_Block", type=edu_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Program2", type=edu_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
axioms3: BinaryAssociation = BinaryAssociation(
    name="axioms3",
    ends={
        Property(name="edu_Axiom", type=edu_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Program4", type=edu_Axiom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand9: BinaryAssociation = BinaryAssociation(
    name="operand9",
    ends={
        Property(name="edu_Expression10", type=edu_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_UnaryExpression", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values11: BinaryAssociation = BinaryAssociation(
    name="values11",
    ends={
        Property(name="edu_Expression12", type=edu_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayLiteral", type=edu_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType13: BinaryAssociation = BinaryAssociation(
    name="baseType13",
    ends={
        Property(name="edu_PrimitiveType", type=edu_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayType", type=edu_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="edu_Expression", type=edu_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_BinaryExpression", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right6: BinaryAssociation = BinaryAssociation(
    name="right6",
    ends={
        Property(name="edu_Expression8", type=edu_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_BinaryExpression7", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardedNode14: BinaryAssociation = BinaryAssociation(
    name="guardedNode14",
    ends={
        Property(name="edu_FunctionCall", type=edu_FunctionCallPreconditionAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionCallPreconditionAssertion", type=edu_FunctionCall, multiplicity=Multiplicity(1, 1))
    }
)
guardedNode15: BinaryAssociation = BinaryAssociation(
    name="guardedNode15",
    ends={
        Property(name="edu_Expression16", type=edu_DivisorNotZeroAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_DivisorNotZeroAssertion", type=edu_Expression, multiplicity=Multiplicity(1, 1))
    }
)
expression17: BinaryAssociation = BinaryAssociation(
    name="expression17",
    ends={
        Property(name="edu_Expression18", type=edu_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Annotation", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="edu_Type", type=edu_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_VariableDeclaration", type=edu_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue24: BinaryAssociation = BinaryAssociation(
    name="initialValue24",
    ends={
        Property(name="edu_Expression26", type=edu_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_VariableDeclaration25", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements27: BinaryAssociation = BinaryAssociation(
    name="statements27",
    ends={
        Property(name="edu_Statement", type=edu_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Block28", type=edu_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="edu_Expression20", type=edu_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Assignment", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable21: BinaryAssociation = BinaryAssociation(
    name="variable21",
    ends={
        Property(name="edu_VariableReference", type=edu_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Assignment22", type=edu_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseBlock34: BinaryAssociation = BinaryAssociation(
    name="falseBlock34",
    ends={
        Property(name="edu_Block36", type=edu_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Conditional35", type=edu_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="edu_Expression30", type=edu_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Conditional", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueBlock31: BinaryAssociation = BinaryAssociation(
    name="trueBlock31",
    ends={
        Property(name="edu_Block33", type=edu_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Conditional32", type=edu_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actuals45: BinaryAssociation = BinaryAssociation(
    name="actuals45",
    ends={
        Property(name="edu_Expression47", type=edu_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionCall46", type=edu_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function48: BinaryAssociation = BinaryAssociation(
    name="function48",
    ends={
        Property(name="edu_FunctionDeclaration50", type=edu_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionCall49", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
preconditions51: BinaryAssociation = BinaryAssociation(
    name="preconditions51",
    ends={
        Property(name="edu_Precondition", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionDeclaration52", type=edu_Precondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postconditions53: BinaryAssociation = BinaryAssociation(
    name="postconditions53",
    ends={
        Property(name="edu_Postcondition", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionDeclaration54", type=edu_Postcondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters55: BinaryAssociation = BinaryAssociation(
    name="parameters55",
    ends={
        Property(name="edu_VariableDeclaration57", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionDeclaration56", type=edu_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body58: BinaryAssociation = BinaryAssociation(
    name="body58",
    ends={
        Property(name="edu_Block60", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionDeclaration59", type=edu_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter37: BinaryAssociation = BinaryAssociation(
    name="parameter37",
    ends={
        Property(name="edu_VariableDeclaration38", type=edu_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_QuantifiedExpression", type=edu_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression39: BinaryAssociation = BinaryAssociation(
    name="expression39",
    ends={
        Property(name="edu_Expression41", type=edu_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_QuantifiedExpression40", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="edu_Expression44", type=edu_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_QuantifiedExpression43", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType61: BinaryAssociation = BinaryAssociation(
    name="returnType61",
    ends={
        Property(name="edu_Type63", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_FunctionDeclaration62", type=edu_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition64: BinaryAssociation = BinaryAssociation(
    name="condition64",
    ends={
        Property(name="edu_Expression65", type=edu_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Loop", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body66: BinaryAssociation = BinaryAssociation(
    name="body66",
    ends={
        Property(name="edu_Block68", type=edu_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Loop67", type=edu_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invariants69: BinaryAssociation = BinaryAssociation(
    name="invariants69",
    ends={
        Property(name="edu_Invariant", type=edu_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Loop70", type=edu_Invariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable76: BinaryAssociation = BinaryAssociation(
    name="variable76",
    ends={
        Property(name="edu_VariableDeclaration78", type=edu_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_VariableReference77", type=edu_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
function79: BinaryAssociation = BinaryAssociation(
    name="function79",
    ends={
        Property(name="edu_FunctionDeclaration80", type=edu_ReturnValueReference, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ReturnValueReference", type=edu_FunctionDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
index81: BinaryAssociation = BinaryAssociation(
    name="index81",
    ends={
        Property(name="edu_Expression82", type=edu_SymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_SymbolReference", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue71: BinaryAssociation = BinaryAssociation(
    name="returnValue71",
    ends={
        Property(name="edu_Expression72", type=edu_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ReturnStatement", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function73: BinaryAssociation = BinaryAssociation(
    name="function73",
    ends={
        Property(name="edu_FunctionDeclaration75", type=edu_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ReturnStatement74", type=edu_FunctionDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
index93: BinaryAssociation = BinaryAssociation(
    name="index93",
    ends={
        Property(name="edu_Expression94", type=edu_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayAccess", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array95: BinaryAssociation = BinaryAssociation(
    name="array95",
    ends={
        Property(name="edu_Expression97", type=edu_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayAccess96", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key98: BinaryAssociation = BinaryAssociation(
    name="key98",
    ends={
        Property(name="edu_Expression99", type=edu_ExpressionToExpressionMap, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ExpressionToExpressionMap", type=edu_Expression, multiplicity=Multiplicity(0, 1))
    }
)
value100: BinaryAssociation = BinaryAssociation(
    name="value100",
    ends={
        Property(name="edu_Expression102", type=edu_ExpressionToExpressionMap, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ExpressionToExpressionMap101", type=edu_Expression, multiplicity=Multiplicity(0, 1))
    }
)
expression83: BinaryAssociation = BinaryAssociation(
    name="expression83",
    ends={
        Property(name="edu_Expression84", type=edu_ExpressionEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ExpressionEvaluation", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
chainedFunction85: BinaryAssociation = BinaryAssociation(
    name="chainedFunction85",
    ends={
        Property(name="edu_Expression86", type=edu_ArrayFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayFunction", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index87: BinaryAssociation = BinaryAssociation(
    name="index87",
    ends={
        Property(name="edu_Expression89", type=edu_ArrayFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayFunction88", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="edu_Expression92", type=edu_ArrayFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_ArrayFunction91", type=edu_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenTrue103: BinaryAssociation = BinaryAssociation(
    name="whenTrue103",
    ends={
        Property(name="edu_Expression104", type=edu_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_TernaryExpression", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whenFalse105: BinaryAssociation = BinaryAssociation(
    name="whenFalse105",
    ends={
        Property(name="edu_Expression107", type=edu_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_TernaryExpression106", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition108: BinaryAssociation = BinaryAssociation(
    name="condition108",
    ends={
        Property(name="edu_Expression110", type=edu_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_TernaryExpression109", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters111: BinaryAssociation = BinaryAssociation(
    name="parameters111",
    ends={
        Property(name="edu_VariableDeclaration112", type=edu_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_LetExpression", type=edu_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="edu_Expression115", type=edu_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_LetExpression114", type=edu_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_edu_Program_ASTNode = Generalization(general=ASTNode, specific=edu_Program)
gen_edu_Addition_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Addition)
gen_edu_UnaryExpression_Expression = Generalization(general=Expression, specific=edu_UnaryExpression)
gen_edu_ArrayLiteral_Literal = Generalization(general=Literal, specific=edu_ArrayLiteral)
gen_edu_Literal_Expression = Generalization(general=Expression, specific=edu_Literal)
gen_edu_ArrayType_Type = Generalization(general=Type, specific=edu_ArrayType)
gen_edu_BinaryExpression_Expression = Generalization(general=Expression, specific=edu_BinaryExpression)
gen_edu_Expression_ASTNode = Generalization(general=ASTNode, specific=edu_Expression)
gen_edu_FunctionCallPreconditionAssertion_GuardAssertion = Generalization(general=GuardAssertion, specific=edu_FunctionCallPreconditionAssertion)
gen_edu_DivisorNotZeroAssertion_GuardAssertion = Generalization(general=GuardAssertion, specific=edu_DivisorNotZeroAssertion)
gen_edu_Annotation_Statement = Generalization(general=Statement, specific=edu_Annotation)
gen_edu_Type_ASTNode = Generalization(general=ASTNode, specific=edu_Type)
gen_edu_PrimitiveType_Type = Generalization(general=Type, specific=edu_PrimitiveType)
gen_edu_Assertion_Annotation = Generalization(general=Annotation, specific=edu_Assertion)
gen_edu_GuardAssertion_Assertion = Generalization(general=Assertion, specific=edu_GuardAssertion)
gen_edu_Assumption_Annotation = Generalization(general=Annotation, specific=edu_Assumption)
gen_edu_Axiom_Annotation = Generalization(general=Annotation, specific=edu_Axiom)
gen_edu_Block_Statement = Generalization(general=Statement, specific=edu_Block)
gen_edu_BooleanLiteral_Literal = Generalization(general=Literal, specific=edu_BooleanLiteral)
gen_edu_Assignment_Statement = Generalization(general=Statement, specific=edu_Assignment)
gen_edu_VariableDeclaration_Statement = Generalization(general=Statement, specific=edu_VariableDeclaration)
gen_edu_Conjunction_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Conjunction)
gen_edu_Disjunction_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Disjunction)
gen_edu_Division_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Division)
gen_edu_Equal_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Equal)
gen_edu_Equivalence_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Equivalence)
gen_edu_ExistsQuantifier_QuantifiedExpression = Generalization(general=QuantifiedExpression, specific=edu_ExistsQuantifier)
gen_edu_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=edu_BooleanType)
gen_edu_Conditional_Statement = Generalization(general=Statement, specific=edu_Conditional)
gen_edu_FunctionCall_Expression = Generalization(general=Expression, specific=edu_FunctionCall)
gen_edu_FunctionDeclaration_ASTNode = Generalization(general=ASTNode, specific=edu_FunctionDeclaration)
gen_edu_QuantifiedExpression_Expression = Generalization(general=Expression, specific=edu_QuantifiedExpression)
gen_edu_ForAllQuantifier_QuantifiedExpression = Generalization(general=QuantifiedExpression, specific=edu_ForAllQuantifier)
gen_edu_GreaterOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_GreaterOrEqual)
gen_edu_Implication_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Implication)
gen_edu_IntegerLiteral_Literal = Generalization(general=Literal, specific=edu_IntegerLiteral)
gen_edu_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=edu_IntegerType)
gen_edu_Invariant_Annotation = Generalization(general=Annotation, specific=edu_Invariant)
gen_edu_Less_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Less)
gen_edu_Precondition_FunctionAnnotation = Generalization(general=FunctionAnnotation, specific=edu_Precondition)
gen_edu_Postcondition_FunctionAnnotation = Generalization(general=FunctionAnnotation, specific=edu_Postcondition)
gen_edu_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Greater)
gen_edu_Minus_Sign = Generalization(general=Sign, specific=edu_Minus)
gen_edu_Sign_UnaryExpression = Generalization(general=UnaryExpression, specific=edu_Sign)
gen_edu_Modulus_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Modulus)
gen_edu_Multiplication_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Multiplication)
gen_edu_Negation_UnaryExpression = Generalization(general=UnaryExpression, specific=edu_Negation)
gen_edu_Plus_Sign = Generalization(general=Sign, specific=edu_Plus)
gen_edu_ReturnStatement_Statement = Generalization(general=Statement, specific=edu_ReturnStatement)
gen_edu_LessOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_LessOrEqual)
gen_edu_Loop_Statement = Generalization(general=Statement, specific=edu_Loop)
gen_edu_VariableReference_SymbolReference = Generalization(general=SymbolReference, specific=edu_VariableReference)
gen_edu_Statement_ASTNode = Generalization(general=ASTNode, specific=edu_Statement)
gen_edu_ReturnValueReference_SymbolReference = Generalization(general=SymbolReference, specific=edu_ReturnValueReference)
gen_edu_SymbolReference_Expression = Generalization(general=Expression, specific=edu_SymbolReference)
gen_edu_Subtraction_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Subtraction)
gen_edu_Unequal_BinaryExpression = Generalization(general=BinaryExpression, specific=edu_Unequal)
gen_edu_ArrayAccess_Expression = Generalization(general=Expression, specific=edu_ArrayAccess)
gen_edu_FunctionAnnotation_Annotation = Generalization(general=Annotation, specific=edu_FunctionAnnotation)
gen_edu_TernaryExpression_Expression = Generalization(general=Expression, specific=edu_TernaryExpression)
gen_edu_ExpressionEvaluation_ASTNode = Generalization(general=ASTNode, specific=edu_ExpressionEvaluation)
gen_edu_ArrayFunction_Literal = Generalization(general=Literal, specific=edu_ArrayFunction)
gen_edu_LetExpression_Expression = Generalization(general=Expression, specific=edu_LetExpression)

# Domain Model
domain_model = DomainModel(
    name="edu",
    types={edu_Program, ASTNode, edu_FunctionDeclaration, edu_Block, edu_Axiom, edu_ASTNode, edu_Addition, BinaryExpression, edu_UnaryExpression, edu_ArrayLiteral, Literal, edu_Literal, edu_ArrayType, Type, edu_PrimitiveType, edu_BinaryExpression, Expression, edu_Expression, edu_FunctionCallPreconditionAssertion, GuardAssertion, edu_FunctionCall, edu_DivisorNotZeroAssertion, edu_Annotation, Statement, edu_Type, edu_Assertion, Annotation, edu_GuardAssertion, Assertion, edu_Assumption, edu_Statement, edu_BooleanLiteral, edu_Assignment, edu_VariableReference, edu_VariableDeclaration, edu_Conjunction, edu_Disjunction, edu_Division, edu_Equal, edu_Equivalence, edu_ExistsQuantifier, QuantifiedExpression, edu_BooleanType, PrimitiveType, edu_Conditional, edu_Precondition, edu_Postcondition, edu_QuantifiedExpression, edu_ForAllQuantifier, edu_GreaterOrEqual, edu_Implication, edu_IntegerLiteral, edu_IntegerType, edu_Invariant, edu_Less, FunctionAnnotation, edu_Greater, edu_Minus, Sign, edu_Sign, UnaryExpression, edu_Modulus, edu_Multiplication, edu_Negation, edu_Plus, edu_ReturnStatement, edu_LessOrEqual, edu_Loop, SymbolReference, edu_ReturnValueReference, edu_SymbolReference, edu_Subtraction, edu_Unequal, edu_ArrayAccess, edu_ExpressionToExpressionMap, edu_FunctionAnnotation, edu_TernaryExpression, edu_ExpressionEvaluation, edu_ArrayFunction, edu_visitor_IASTNodeVisitor, edu_LetExpression},
    associations={functionDeclarations0, mainBlock1, axioms3, operand9, values11, baseType13, left5, right6, guardedNode14, guardedNode15, expression17, type23, initialValue24, statements27, value19, variable21, falseBlock34, condition29, trueBlock31, actuals45, function48, preconditions51, postconditions53, parameters55, body58, parameter37, expression39, condition42, returnType61, condition64, body66, invariants69, variable76, function79, index81, returnValue71, function73, index93, array95, key98, value100, expression83, chainedFunction85, index87, value90, whenTrue103, whenFalse105, condition108, parameters111, expression113},
    generalizations={gen_edu_Program_ASTNode, gen_edu_Addition_BinaryExpression, gen_edu_UnaryExpression_Expression, gen_edu_ArrayLiteral_Literal, gen_edu_Literal_Expression, gen_edu_ArrayType_Type, gen_edu_BinaryExpression_Expression, gen_edu_Expression_ASTNode, gen_edu_FunctionCallPreconditionAssertion_GuardAssertion, gen_edu_DivisorNotZeroAssertion_GuardAssertion, gen_edu_Annotation_Statement, gen_edu_Type_ASTNode, gen_edu_PrimitiveType_Type, gen_edu_Assertion_Annotation, gen_edu_GuardAssertion_Assertion, gen_edu_Assumption_Annotation, gen_edu_Axiom_Annotation, gen_edu_Block_Statement, gen_edu_BooleanLiteral_Literal, gen_edu_Assignment_Statement, gen_edu_VariableDeclaration_Statement, gen_edu_Conjunction_BinaryExpression, gen_edu_Disjunction_BinaryExpression, gen_edu_Division_BinaryExpression, gen_edu_Equal_BinaryExpression, gen_edu_Equivalence_BinaryExpression, gen_edu_ExistsQuantifier_QuantifiedExpression, gen_edu_BooleanType_PrimitiveType, gen_edu_Conditional_Statement, gen_edu_FunctionCall_Expression, gen_edu_FunctionDeclaration_ASTNode, gen_edu_QuantifiedExpression_Expression, gen_edu_ForAllQuantifier_QuantifiedExpression, gen_edu_GreaterOrEqual_BinaryExpression, gen_edu_Implication_BinaryExpression, gen_edu_IntegerLiteral_Literal, gen_edu_IntegerType_PrimitiveType, gen_edu_Invariant_Annotation, gen_edu_Less_BinaryExpression, gen_edu_Precondition_FunctionAnnotation, gen_edu_Postcondition_FunctionAnnotation, gen_edu_Greater_BinaryExpression, gen_edu_Minus_Sign, gen_edu_Sign_UnaryExpression, gen_edu_Modulus_BinaryExpression, gen_edu_Multiplication_BinaryExpression, gen_edu_Negation_UnaryExpression, gen_edu_Plus_Sign, gen_edu_ReturnStatement_Statement, gen_edu_LessOrEqual_BinaryExpression, gen_edu_Loop_Statement, gen_edu_VariableReference_SymbolReference, gen_edu_Statement_ASTNode, gen_edu_ReturnValueReference_SymbolReference, gen_edu_SymbolReference_Expression, gen_edu_Subtraction_BinaryExpression, gen_edu_Unequal_BinaryExpression, gen_edu_ArrayAccess_Expression, gen_edu_FunctionAnnotation_Annotation, gen_edu_TernaryExpression_Expression, gen_edu_ExpressionEvaluation_ASTNode, gen_edu_ArrayFunction_Literal, gen_edu_LetExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)