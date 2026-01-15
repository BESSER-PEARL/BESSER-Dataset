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
amethyst_Module = Class(name="amethyst::Module")
amethyst_Import = Class(name="amethyst::Import")
amethyst_Statement = Class(name="amethyst::Statement")
amethyst_Symbol = Class(name="amethyst::Symbol")
Statement = Class(name="Statement")
amethyst_TagDeclaration = Class(name="amethyst::TagDeclaration")
amethyst_ClassType = Class(name="amethyst::ClassType")
amethyst_TagLoopExpression = Class(name="amethyst::TagLoopExpression")
amethyst_TagAttribute = Class(name="amethyst::TagAttribute")
amethyst_EObject = Class(name="amethyst::EObject")
amethyst_Expression = Class(name="amethyst::Expression")
amethyst_TagExpression = Class(name="amethyst::TagExpression")
AbstractType = Class(name="AbstractType")
amethyst_PropertyDeclaration = Class(name="amethyst::PropertyDeclaration")
amethyst_SymbolReference = Class(name="amethyst::SymbolReference")
Expression = Class(name="Expression")
amethyst_Literal = Class(name="amethyst::Literal")
amethyst_CharLiteral = Class(name="amethyst::CharLiteral")
Literal = Class(name="Literal")
amethyst_StringLiteral = Class(name="amethyst::StringLiteral")
amethyst_IntLiteral = Class(name="amethyst::IntLiteral")
amethyst_FloatLiteral = Class(name="amethyst::FloatLiteral")
amethyst_BooleanLiteral = Class(name="amethyst::BooleanLiteral")
amethyst_NullLiteral = Class(name="amethyst::NullLiteral")
amethyst_RangeLiteral = Class(name="amethyst::RangeLiteral")
amethyst_AbstractType = Class(name="amethyst::AbstractType")
amethyst_Type = Class(name="amethyst::Type")
amethyst_PrimitiveType = Class(name="amethyst::PrimitiveType")
Type = Class(name="Type")
amethyst_CharType = Class(name="amethyst::CharType")
PrimitiveType = Class(name="PrimitiveType")
amethyst_StringType = Class(name="amethyst::StringType")
amethyst_IntType = Class(name="amethyst::IntType")
amethyst_FloatType = Class(name="amethyst::FloatType")
amethyst_BooleanType = Class(name="amethyst::BooleanType")
amethyst_DefinitionType = Class(name="amethyst::DefinitionType")
amethyst_AnyType = Class(name="amethyst::AnyType")
amethyst_ArrayType = Class(name="amethyst::ArrayType")
amethyst_ClassDeclaration = Class(name="amethyst::ClassDeclaration")
amethyst_VariableDeclaration = Class(name="amethyst::VariableDeclaration")
Symbol = Class(name="Symbol")
amethyst_DefinitionDeclaration = Class(name="amethyst::DefinitionDeclaration")
amethyst_ParameterDeclaration = Class(name="amethyst::ParameterDeclaration")
amethyst_TagLoopInitializerDeclaration = Class(name="amethyst::TagLoopInitializerDeclaration")
amethyst_IfStatement = Class(name="amethyst::IfStatement")
amethyst_ElseIfStatement = Class(name="amethyst::ElseIfStatement")
amethyst_ElseStatement = Class(name="amethyst::ElseStatement")
amethyst_CaseStatement = Class(name="amethyst::CaseStatement")
amethyst_CaseElseStatement = Class(name="amethyst::CaseElseStatement")
amethyst_WhenStatement = Class(name="amethyst::WhenStatement")
amethyst_WhileStatement = Class(name="amethyst::WhileStatement")
amethyst_IndexAccessExpression = Class(name="amethyst::IndexAccessExpression")
amethyst_ForStatement = Class(name="amethyst::ForStatement")
amethyst_ForInitializerDeclaration = Class(name="amethyst::ForInitializerDeclaration")
amethyst_BreakStatement = Class(name="amethyst::BreakStatement")
amethyst_NextStatement = Class(name="amethyst::NextStatement")
amethyst_ReturnStatement = Class(name="amethyst::ReturnStatement")
amethyst_JsCodeStatement = Class(name="amethyst::JsCodeStatement")
amethyst_AssignmentExpression = Class(name="amethyst::AssignmentExpression")
amethyst_ShiftExpression = Class(name="amethyst::ShiftExpression")
amethyst_CallExpression = Class(name="amethyst::CallExpression")
amethyst_MemberAccessExpression = Class(name="amethyst::MemberAccessExpression")
amethyst_OrExpression = Class(name="amethyst::OrExpression")
amethyst_AndExpression = Class(name="amethyst::AndExpression")
amethyst_RelationalExpression = Class(name="amethyst::RelationalExpression")
amethyst_EqualityExpression = Class(name="amethyst::EqualityExpression")
amethyst_AdditiveExpression = Class(name="amethyst::AdditiveExpression")
amethyst_MultiplicativeExpression = Class(name="amethyst::MultiplicativeExpression")
amethyst_MatchingExpression = Class(name="amethyst::MatchingExpression")
amethyst_InExpression = Class(name="amethyst::InExpression")
amethyst_UnaryMinusExpression = Class(name="amethyst::UnaryMinusExpression")
amethyst_NotExpression = Class(name="amethyst::NotExpression")
amethyst_TypeCastExpression = Class(name="amethyst::TypeCastExpression")
amethyst_NewExpression = Class(name="amethyst::NewExpression")
amethyst_SuperExpression = Class(name="amethyst::SuperExpression")
amethyst_ParenthisedExpression = Class(name="amethyst::ParenthisedExpression")
amethyst_NumberRangeLiteral = Class(name="amethyst::NumberRangeLiteral")
RangeLiteral = Class(name="RangeLiteral")
amethyst_CharRangeLiteral = Class(name="amethyst::CharRangeLiteral")
amethyst_SelfExpression = Class(name="amethyst::SelfExpression")

# amethyst_Module class attributes and methods
amethyst_Module_name: Property = Property(name="name", type=StringType)
amethyst_Module.attributes={amethyst_Module_name}

# amethyst_Import class attributes and methods
amethyst_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
amethyst_Import.attributes={amethyst_Import_importedNamespace}

# amethyst_Statement class attributes and methods

# amethyst_Symbol class attributes and methods
amethyst_Symbol_name: Property = Property(name="name", type=StringType)
amethyst_Symbol.attributes={amethyst_Symbol_name}

# Statement class attributes and methods

# amethyst_TagDeclaration class attributes and methods

# amethyst_ClassType class attributes and methods

# amethyst_TagLoopExpression class attributes and methods

# amethyst_TagAttribute class attributes and methods

# amethyst_EObject class attributes and methods

# amethyst_Expression class attributes and methods

# amethyst_TagExpression class attributes and methods

# AbstractType class attributes and methods

# amethyst_PropertyDeclaration class attributes and methods

# amethyst_SymbolReference class attributes and methods

# Expression class attributes and methods

# amethyst_Literal class attributes and methods

# amethyst_CharLiteral class attributes and methods
amethyst_CharLiteral_value: Property = Property(name="value", type=StringType)
amethyst_CharLiteral.attributes={amethyst_CharLiteral_value}

# Literal class attributes and methods

# amethyst_StringLiteral class attributes and methods
amethyst_StringLiteral_value: Property = Property(name="value", type=StringType)
amethyst_StringLiteral.attributes={amethyst_StringLiteral_value}

# amethyst_IntLiteral class attributes and methods
amethyst_IntLiteral_value: Property = Property(name="value", type=IntegerType)
amethyst_IntLiteral.attributes={amethyst_IntLiteral_value}

# amethyst_FloatLiteral class attributes and methods
amethyst_FloatLiteral_value: Property = Property(name="value", type=FloatType)
amethyst_FloatLiteral.attributes={amethyst_FloatLiteral_value}

# amethyst_BooleanLiteral class attributes and methods
amethyst_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
amethyst_BooleanLiteral.attributes={amethyst_BooleanLiteral_value}

# amethyst_NullLiteral class attributes and methods

# amethyst_RangeLiteral class attributes and methods

# amethyst_AbstractType class attributes and methods

# amethyst_Type class attributes and methods

# amethyst_PrimitiveType class attributes and methods

# Type class attributes and methods

# amethyst_CharType class attributes and methods

# PrimitiveType class attributes and methods

# amethyst_StringType class attributes and methods

# amethyst_IntType class attributes and methods

# amethyst_FloatType class attributes and methods

# amethyst_BooleanType class attributes and methods

# amethyst_DefinitionType class attributes and methods

# amethyst_AnyType class attributes and methods

# amethyst_ArrayType class attributes and methods

# amethyst_ClassDeclaration class attributes and methods

# amethyst_VariableDeclaration class attributes and methods

# Symbol class attributes and methods

# amethyst_DefinitionDeclaration class attributes and methods
amethyst_DefinitionDeclaration_static: Property = Property(name="static", type=BooleanType)
amethyst_DefinitionDeclaration.attributes={amethyst_DefinitionDeclaration_static}

# amethyst_ParameterDeclaration class attributes and methods

# amethyst_TagLoopInitializerDeclaration class attributes and methods

# amethyst_IfStatement class attributes and methods

# amethyst_ElseIfStatement class attributes and methods

# amethyst_ElseStatement class attributes and methods

# amethyst_CaseStatement class attributes and methods

# amethyst_CaseElseStatement class attributes and methods

# amethyst_WhenStatement class attributes and methods

# amethyst_WhileStatement class attributes and methods

# amethyst_IndexAccessExpression class attributes and methods

# amethyst_ForStatement class attributes and methods

# amethyst_ForInitializerDeclaration class attributes and methods

# amethyst_BreakStatement class attributes and methods

# amethyst_NextStatement class attributes and methods

# amethyst_ReturnStatement class attributes and methods

# amethyst_JsCodeStatement class attributes and methods
amethyst_JsCodeStatement_value: Property = Property(name="value", type=StringType)
amethyst_JsCodeStatement.attributes={amethyst_JsCodeStatement_value}

# amethyst_AssignmentExpression class attributes and methods

# amethyst_ShiftExpression class attributes and methods
amethyst_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_ShiftExpression.attributes={amethyst_ShiftExpression_operator}

# amethyst_CallExpression class attributes and methods

# amethyst_MemberAccessExpression class attributes and methods

# amethyst_OrExpression class attributes and methods

# amethyst_AndExpression class attributes and methods

# amethyst_RelationalExpression class attributes and methods
amethyst_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_RelationalExpression.attributes={amethyst_RelationalExpression_operator}

# amethyst_EqualityExpression class attributes and methods
amethyst_EqualityExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_EqualityExpression.attributes={amethyst_EqualityExpression_operator}

# amethyst_AdditiveExpression class attributes and methods
amethyst_AdditiveExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_AdditiveExpression.attributes={amethyst_AdditiveExpression_operator}

# amethyst_MultiplicativeExpression class attributes and methods
amethyst_MultiplicativeExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_MultiplicativeExpression.attributes={amethyst_MultiplicativeExpression_operator}

# amethyst_MatchingExpression class attributes and methods
amethyst_MatchingExpression_operator: Property = Property(name="operator", type=StringType)
amethyst_MatchingExpression.attributes={amethyst_MatchingExpression_operator}

# amethyst_InExpression class attributes and methods

# amethyst_UnaryMinusExpression class attributes and methods

# amethyst_NotExpression class attributes and methods

# amethyst_TypeCastExpression class attributes and methods

# amethyst_NewExpression class attributes and methods

# amethyst_SuperExpression class attributes and methods

# amethyst_ParenthisedExpression class attributes and methods

# amethyst_NumberRangeLiteral class attributes and methods

# RangeLiteral class attributes and methods

# amethyst_CharRangeLiteral class attributes and methods

# amethyst_SelfExpression class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="amethyst_Import", type=amethyst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_Module", type=amethyst_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="amethyst_Statement", type=amethyst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_Module2", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="amethyst_ClassType", type=amethyst_TagDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagDeclaration", type=amethyst_ClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopExpression4: BinaryAssociation = BinaryAssociation(
    name="loopExpression4",
    ends={
        Property(name="amethyst_TagLoopExpression", type=amethyst_TagDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagDeclaration5", type=amethyst_TagLoopExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="amethyst_TagAttribute", type=amethyst_TagDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagDeclaration7", type=amethyst_TagAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="amethyst_EObject", type=amethyst_TagDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagDeclaration9", type=amethyst_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer10: BinaryAssociation = BinaryAssociation(
    name="initializer10",
    ends={
        Property(name="amethyst_Symbol", type=amethyst_TagLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagLoopExpression11", type=amethyst_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterable12: BinaryAssociation = BinaryAssociation(
    name="iterable12",
    ends={
        Property(name="amethyst_Expression", type=amethyst_TagLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagLoopExpression13", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp14: BinaryAssociation = BinaryAssociation(
    name="exp14",
    ends={
        Property(name="amethyst_Expression15", type=amethyst_TagExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyRef16: BinaryAssociation = BinaryAssociation(
    name="propertyRef16",
    ends={
        Property(name="amethyst_PropertyDeclaration", type=amethyst_TagAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagAttribute17", type=amethyst_PropertyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="amethyst_Expression20", type=amethyst_TagAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TagAttribute19", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolRef21: BinaryAssociation = BinaryAssociation(
    name="symbolRef21",
    ends={
        Property(name="amethyst_Symbol22", type=amethyst_SymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_SymbolReference", type=amethyst_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
statements35: BinaryAssociation = BinaryAssociation(
    name="statements35",
    ends={
        Property(name="amethyst_Statement37", type=amethyst_DefinitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_DefinitionDeclaration36", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="amethyst_Type", type=amethyst_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ArrayType", type=amethyst_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef24: BinaryAssociation = BinaryAssociation(
    name="typeRef24",
    ends={
        Property(name="amethyst_ClassDeclaration", type=amethyst_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ClassType25", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="amethyst_AbstractType", type=amethyst_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_VariableDeclaration", type=amethyst_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="amethyst_Expression29", type=amethyst_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_VariableDeclaration28", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params30: BinaryAssociation = BinaryAssociation(
    name="params30",
    ends={
        Property(name="amethyst_Symbol31", type=amethyst_DefinitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_DefinitionDeclaration", type=amethyst_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="amethyst_AbstractType34", type=amethyst_DefinitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_DefinitionDeclaration33", type=amethyst_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="amethyst_Expression67", type=amethyst_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ElseIfStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="amethyst_AbstractType39", type=amethyst_ParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ParameterDeclaration", type=amethyst_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType41: BinaryAssociation = BinaryAssociation(
    name="superType41",
    ends={
        Property(name="amethyst_ClassDeclaration42", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ClassDeclaration40", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
methods43: BinaryAssociation = BinaryAssociation(
    name="methods43",
    ends={
        Property(name="amethyst_Symbol45", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ClassDeclaration44", type=amethyst_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties46: BinaryAssociation = BinaryAssociation(
    name="properties46",
    ends={
        Property(name="amethyst_Symbol48", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ClassDeclaration47", type=amethyst_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag49: BinaryAssociation = BinaryAssociation(
    name="tag49",
    ends={
        Property(name="amethyst_TagDeclaration51", type=amethyst_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ClassDeclaration50", type=amethyst_TagDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="amethyst_AbstractType54", type=amethyst_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_PropertyDeclaration53", type=amethyst_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="amethyst_Expression57", type=amethyst_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_PropertyDeclaration56", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition58: BinaryAssociation = BinaryAssociation(
    name="condition58",
    ends={
        Property(name="amethyst_Expression59", type=amethyst_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_IfStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements60: BinaryAssociation = BinaryAssociation(
    name="statements60",
    ends={
        Property(name="amethyst_Statement62", type=amethyst_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_IfStatement61", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement63: BinaryAssociation = BinaryAssociation(
    name="elseStatement63",
    ends={
        Property(name="amethyst_Statement65", type=amethyst_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_IfStatement64", type=amethyst_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition91: BinaryAssociation = BinaryAssociation(
    name="condition91",
    ends={
        Property(name="amethyst_Expression92", type=amethyst_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_WhileStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements68: BinaryAssociation = BinaryAssociation(
    name="statements68",
    ends={
        Property(name="amethyst_Statement70", type=amethyst_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ElseIfStatement69", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement71: BinaryAssociation = BinaryAssociation(
    name="elseStatement71",
    ends={
        Property(name="amethyst_Statement73", type=amethyst_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ElseIfStatement72", type=amethyst_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements74: BinaryAssociation = BinaryAssociation(
    name="statements74",
    ends={
        Property(name="amethyst_Statement75", type=amethyst_ElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ElseStatement", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value76: BinaryAssociation = BinaryAssociation(
    name="value76",
    ends={
        Property(name="amethyst_Expression77", type=amethyst_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CaseStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenStatements78: BinaryAssociation = BinaryAssociation(
    name="whenStatements78",
    ends={
        Property(name="amethyst_Statement80", type=amethyst_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CaseStatement79", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement81: BinaryAssociation = BinaryAssociation(
    name="elseStatement81",
    ends={
        Property(name="amethyst_Statement83", type=amethyst_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CaseStatement82", type=amethyst_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements84: BinaryAssociation = BinaryAssociation(
    name="statements84",
    ends={
        Property(name="amethyst_Statement85", type=amethyst_CaseElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CaseElseStatement", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition86: BinaryAssociation = BinaryAssociation(
    name="condition86",
    ends={
        Property(name="amethyst_Expression87", type=amethyst_WhenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_WhenStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements88: BinaryAssociation = BinaryAssociation(
    name="statements88",
    ends={
        Property(name="amethyst_Statement90", type=amethyst_WhenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_WhenStatement89", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements93: BinaryAssociation = BinaryAssociation(
    name="statements93",
    ends={
        Property(name="amethyst_Statement95", type=amethyst_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_WhileStatement94", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer96: BinaryAssociation = BinaryAssociation(
    name="initializer96",
    ends={
        Property(name="amethyst_Symbol97", type=amethyst_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ForStatement", type=amethyst_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterable98: BinaryAssociation = BinaryAssociation(
    name="iterable98",
    ends={
        Property(name="amethyst_Expression100", type=amethyst_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ForStatement99", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements101: BinaryAssociation = BinaryAssociation(
    name="statements101",
    ends={
        Property(name="amethyst_Statement103", type=amethyst_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ForStatement102", type=amethyst_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="amethyst_Expression105", type=amethyst_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ReturnStatement", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="amethyst_Expression107", type=amethyst_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AssignmentExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="amethyst_Expression110", type=amethyst_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AssignmentExpression109", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="amethyst_Expression145", type=amethyst_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_EqualityExpression144", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="amethyst_Expression112", type=amethyst_IndexAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_IndexAccessExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index113: BinaryAssociation = BinaryAssociation(
    name="index113",
    ends={
        Property(name="amethyst_Expression115", type=amethyst_IndexAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_IndexAccessExpression114", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="amethyst_Expression117", type=amethyst_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CallExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args118: BinaryAssociation = BinaryAssociation(
    name="args118",
    ends={
        Property(name="amethyst_Expression120", type=amethyst_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CallExpression119", type=amethyst_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="amethyst_Expression122", type=amethyst_MemberAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MemberAccessExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="amethyst_Symbol125", type=amethyst_MemberAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MemberAccessExpression124", type=amethyst_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="amethyst_Expression127", type=amethyst_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_OrExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="amethyst_Expression130", type=amethyst_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_OrExpression129", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="amethyst_Expression132", type=amethyst_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AndExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="amethyst_Expression135", type=amethyst_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AndExpression134", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="amethyst_Expression137", type=amethyst_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_RelationalExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="amethyst_Expression140", type=amethyst_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_RelationalExpression139", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="amethyst_Expression142", type=amethyst_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_EqualityExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="amethyst_Expression147", type=amethyst_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ShiftExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="amethyst_Expression150", type=amethyst_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ShiftExpression149", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="amethyst_Expression152", type=amethyst_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AdditiveExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="amethyst_Expression155", type=amethyst_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_AdditiveExpression154", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left156: BinaryAssociation = BinaryAssociation(
    name="left156",
    ends={
        Property(name="amethyst_Expression157", type=amethyst_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MultiplicativeExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right158: BinaryAssociation = BinaryAssociation(
    name="right158",
    ends={
        Property(name="amethyst_Expression160", type=amethyst_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MultiplicativeExpression159", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="amethyst_Expression162", type=amethyst_MatchingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MatchingExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="amethyst_Expression165", type=amethyst_MatchingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_MatchingExpression164", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="amethyst_Expression167", type=amethyst_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_InExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right168: BinaryAssociation = BinaryAssociation(
    name="right168",
    ends={
        Property(name="amethyst_Expression170", type=amethyst_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_InExpression169", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression171: BinaryAssociation = BinaryAssociation(
    name="expression171",
    ends={
        Property(name="amethyst_Expression172", type=amethyst_UnaryMinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_UnaryMinusExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression173: BinaryAssociation = BinaryAssociation(
    name="expression173",
    ends={
        Property(name="amethyst_Expression174", type=amethyst_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_NotExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression175: BinaryAssociation = BinaryAssociation(
    name="expression175",
    ends={
        Property(name="amethyst_Expression176", type=amethyst_TypeCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TypeCastExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef177: BinaryAssociation = BinaryAssociation(
    name="typeRef177",
    ends={
        Property(name="amethyst_AbstractType179", type=amethyst_TypeCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_TypeCastExpression178", type=amethyst_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type180: BinaryAssociation = BinaryAssociation(
    name="type180",
    ends={
        Property(name="amethyst_ClassType181", type=amethyst_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_NewExpression", type=amethyst_ClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args182: BinaryAssociation = BinaryAssociation(
    name="args182",
    ends={
        Property(name="amethyst_Expression184", type=amethyst_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_NewExpression183", type=amethyst_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression185: BinaryAssociation = BinaryAssociation(
    name="expression185",
    ends={
        Property(name="amethyst_Expression186", type=amethyst_ParenthisedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_ParenthisedExpression", type=amethyst_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start187: BinaryAssociation = BinaryAssociation(
    name="start187",
    ends={
        Property(name="amethyst_IntLiteral", type=amethyst_NumberRangeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_NumberRangeLiteral", type=amethyst_IntLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end188: BinaryAssociation = BinaryAssociation(
    name="end188",
    ends={
        Property(name="amethyst_IntLiteral190", type=amethyst_NumberRangeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_NumberRangeLiteral189", type=amethyst_IntLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start191: BinaryAssociation = BinaryAssociation(
    name="start191",
    ends={
        Property(name="amethyst_CharLiteral", type=amethyst_CharRangeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CharRangeLiteral", type=amethyst_CharLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end192: BinaryAssociation = BinaryAssociation(
    name="end192",
    ends={
        Property(name="amethyst_CharLiteral194", type=amethyst_CharRangeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="amethyst_CharRangeLiteral193", type=amethyst_CharLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_amethyst_Symbol_Statement = Generalization(general=Statement, specific=amethyst_Symbol)
gen_amethyst_Type_AbstractType = Generalization(general=AbstractType, specific=amethyst_Type)
gen_amethyst_Expression_Statement = Generalization(general=Statement, specific=amethyst_Expression)
gen_amethyst_SymbolReference_Expression = Generalization(general=Expression, specific=amethyst_SymbolReference)
gen_amethyst_Literal_Expression = Generalization(general=Expression, specific=amethyst_Literal)
gen_amethyst_CharLiteral_Literal = Generalization(general=Literal, specific=amethyst_CharLiteral)
gen_amethyst_StringLiteral_Literal = Generalization(general=Literal, specific=amethyst_StringLiteral)
gen_amethyst_IntLiteral_Literal = Generalization(general=Literal, specific=amethyst_IntLiteral)
gen_amethyst_FloatLiteral_Literal = Generalization(general=Literal, specific=amethyst_FloatLiteral)
gen_amethyst_BooleanLiteral_Literal = Generalization(general=Literal, specific=amethyst_BooleanLiteral)
gen_amethyst_NullLiteral_Literal = Generalization(general=Literal, specific=amethyst_NullLiteral)
gen_amethyst_RangeLiteral_Literal = Generalization(general=Literal, specific=amethyst_RangeLiteral)
gen_amethyst_PrimitiveType_Type = Generalization(general=Type, specific=amethyst_PrimitiveType)
gen_amethyst_CharType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_CharType)
gen_amethyst_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_StringType)
gen_amethyst_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_IntType)
gen_amethyst_FloatType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_FloatType)
gen_amethyst_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_BooleanType)
gen_amethyst_DefinitionType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_DefinitionType)
gen_amethyst_AnyType_PrimitiveType = Generalization(general=PrimitiveType, specific=amethyst_AnyType)
gen_amethyst_ArrayType_AbstractType = Generalization(general=AbstractType, specific=amethyst_ArrayType)
gen_amethyst_ClassType_Type = Generalization(general=Type, specific=amethyst_ClassType)
gen_amethyst_VariableDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_VariableDeclaration)
gen_amethyst_DefinitionDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_DefinitionDeclaration)
gen_amethyst_ParameterDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_ParameterDeclaration)
gen_amethyst_ClassDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_ClassDeclaration)
gen_amethyst_PropertyDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_PropertyDeclaration)
gen_amethyst_TagLoopInitializerDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_TagLoopInitializerDeclaration)
gen_amethyst_IfStatement_Statement = Generalization(general=Statement, specific=amethyst_IfStatement)
gen_amethyst_ElseIfStatement_Statement = Generalization(general=Statement, specific=amethyst_ElseIfStatement)
gen_amethyst_ElseStatement_Statement = Generalization(general=Statement, specific=amethyst_ElseStatement)
gen_amethyst_CaseStatement_Statement = Generalization(general=Statement, specific=amethyst_CaseStatement)
gen_amethyst_CaseElseStatement_Statement = Generalization(general=Statement, specific=amethyst_CaseElseStatement)
gen_amethyst_WhenStatement_Statement = Generalization(general=Statement, specific=amethyst_WhenStatement)
gen_amethyst_WhileStatement_Statement = Generalization(general=Statement, specific=amethyst_WhileStatement)
gen_amethyst_IndexAccessExpression_Expression = Generalization(general=Expression, specific=amethyst_IndexAccessExpression)
gen_amethyst_ForStatement_Statement = Generalization(general=Statement, specific=amethyst_ForStatement)
gen_amethyst_ForInitializerDeclaration_Symbol = Generalization(general=Symbol, specific=amethyst_ForInitializerDeclaration)
gen_amethyst_BreakStatement_Statement = Generalization(general=Statement, specific=amethyst_BreakStatement)
gen_amethyst_NextStatement_Statement = Generalization(general=Statement, specific=amethyst_NextStatement)
gen_amethyst_ReturnStatement_Statement = Generalization(general=Statement, specific=amethyst_ReturnStatement)
gen_amethyst_JsCodeStatement_Statement = Generalization(general=Statement, specific=amethyst_JsCodeStatement)
gen_amethyst_AssignmentExpression_Expression = Generalization(general=Expression, specific=amethyst_AssignmentExpression)
gen_amethyst_CallExpression_Expression = Generalization(general=Expression, specific=amethyst_CallExpression)
gen_amethyst_MemberAccessExpression_Expression = Generalization(general=Expression, specific=amethyst_MemberAccessExpression)
gen_amethyst_OrExpression_Expression = Generalization(general=Expression, specific=amethyst_OrExpression)
gen_amethyst_AndExpression_Expression = Generalization(general=Expression, specific=amethyst_AndExpression)
gen_amethyst_RelationalExpression_Expression = Generalization(general=Expression, specific=amethyst_RelationalExpression)
gen_amethyst_EqualityExpression_Expression = Generalization(general=Expression, specific=amethyst_EqualityExpression)
gen_amethyst_ShiftExpression_Expression = Generalization(general=Expression, specific=amethyst_ShiftExpression)
gen_amethyst_AdditiveExpression_Expression = Generalization(general=Expression, specific=amethyst_AdditiveExpression)
gen_amethyst_MultiplicativeExpression_Expression = Generalization(general=Expression, specific=amethyst_MultiplicativeExpression)
gen_amethyst_MatchingExpression_Expression = Generalization(general=Expression, specific=amethyst_MatchingExpression)
gen_amethyst_InExpression_Expression = Generalization(general=Expression, specific=amethyst_InExpression)
gen_amethyst_UnaryMinusExpression_Expression = Generalization(general=Expression, specific=amethyst_UnaryMinusExpression)
gen_amethyst_NotExpression_Expression = Generalization(general=Expression, specific=amethyst_NotExpression)
gen_amethyst_TypeCastExpression_Expression = Generalization(general=Expression, specific=amethyst_TypeCastExpression)
gen_amethyst_NewExpression_Expression = Generalization(general=Expression, specific=amethyst_NewExpression)
gen_amethyst_SuperExpression_Expression = Generalization(general=Expression, specific=amethyst_SuperExpression)
gen_amethyst_ParenthisedExpression_Expression = Generalization(general=Expression, specific=amethyst_ParenthisedExpression)
gen_amethyst_NumberRangeLiteral_RangeLiteral = Generalization(general=RangeLiteral, specific=amethyst_NumberRangeLiteral)
gen_amethyst_CharRangeLiteral_RangeLiteral = Generalization(general=RangeLiteral, specific=amethyst_CharRangeLiteral)
gen_amethyst_SelfExpression_Expression = Generalization(general=Expression, specific=amethyst_SelfExpression)

# Domain Model
domain_model = DomainModel(
    name="amethyst",
    types={amethyst_Module, amethyst_Import, amethyst_Statement, amethyst_Symbol, Statement, amethyst_TagDeclaration, amethyst_ClassType, amethyst_TagLoopExpression, amethyst_TagAttribute, amethyst_EObject, amethyst_Expression, amethyst_TagExpression, AbstractType, amethyst_PropertyDeclaration, amethyst_SymbolReference, Expression, amethyst_Literal, amethyst_CharLiteral, Literal, amethyst_StringLiteral, amethyst_IntLiteral, amethyst_FloatLiteral, amethyst_BooleanLiteral, amethyst_NullLiteral, amethyst_RangeLiteral, amethyst_AbstractType, amethyst_Type, amethyst_PrimitiveType, Type, amethyst_CharType, PrimitiveType, amethyst_StringType, amethyst_IntType, amethyst_FloatType, amethyst_BooleanType, amethyst_DefinitionType, amethyst_AnyType, amethyst_ArrayType, amethyst_ClassDeclaration, amethyst_VariableDeclaration, Symbol, amethyst_DefinitionDeclaration, amethyst_ParameterDeclaration, amethyst_TagLoopInitializerDeclaration, amethyst_IfStatement, amethyst_ElseIfStatement, amethyst_ElseStatement, amethyst_CaseStatement, amethyst_CaseElseStatement, amethyst_WhenStatement, amethyst_WhileStatement, amethyst_IndexAccessExpression, amethyst_ForStatement, amethyst_ForInitializerDeclaration, amethyst_BreakStatement, amethyst_NextStatement, amethyst_ReturnStatement, amethyst_JsCodeStatement, amethyst_AssignmentExpression, amethyst_ShiftExpression, amethyst_CallExpression, amethyst_MemberAccessExpression, amethyst_OrExpression, amethyst_AndExpression, amethyst_RelationalExpression, amethyst_EqualityExpression, amethyst_AdditiveExpression, amethyst_MultiplicativeExpression, amethyst_MatchingExpression, amethyst_InExpression, amethyst_UnaryMinusExpression, amethyst_NotExpression, amethyst_TypeCastExpression, amethyst_NewExpression, amethyst_SuperExpression, amethyst_ParenthisedExpression, amethyst_NumberRangeLiteral, RangeLiteral, amethyst_CharRangeLiteral, amethyst_SelfExpression},
    associations={imports0, declarations1, type3, loopExpression4, attributes6, children8, initializer10, iterable12, exp14, propertyRef16, expression18, symbolRef21, statements35, type23, typeRef24, type26, expression27, params30, type32, condition66, type38, superType41, methods43, properties46, tag49, type52, expression55, condition58, statements60, elseStatement63, condition91, statements68, elseStatement71, statements74, value76, whenStatements78, elseStatement81, statements84, condition86, statements88, statements93, initializer96, iterable98, statements101, expression104, left106, right108, right143, left111, index113, left116, args118, left121, right123, left126, right128, left131, right133, left136, right138, left141, left146, right148, left151, right153, left156, right158, left161, right163, left166, right168, expression171, expression173, expression175, typeRef177, type180, args182, expression185, start187, end188, start191, end192},
    generalizations={gen_amethyst_Symbol_Statement, gen_amethyst_Type_AbstractType, gen_amethyst_Expression_Statement, gen_amethyst_SymbolReference_Expression, gen_amethyst_Literal_Expression, gen_amethyst_CharLiteral_Literal, gen_amethyst_StringLiteral_Literal, gen_amethyst_IntLiteral_Literal, gen_amethyst_FloatLiteral_Literal, gen_amethyst_BooleanLiteral_Literal, gen_amethyst_NullLiteral_Literal, gen_amethyst_RangeLiteral_Literal, gen_amethyst_PrimitiveType_Type, gen_amethyst_CharType_PrimitiveType, gen_amethyst_StringType_PrimitiveType, gen_amethyst_IntType_PrimitiveType, gen_amethyst_FloatType_PrimitiveType, gen_amethyst_BooleanType_PrimitiveType, gen_amethyst_DefinitionType_PrimitiveType, gen_amethyst_AnyType_PrimitiveType, gen_amethyst_ArrayType_AbstractType, gen_amethyst_ClassType_Type, gen_amethyst_VariableDeclaration_Symbol, gen_amethyst_DefinitionDeclaration_Symbol, gen_amethyst_ParameterDeclaration_Symbol, gen_amethyst_ClassDeclaration_Symbol, gen_amethyst_PropertyDeclaration_Symbol, gen_amethyst_TagLoopInitializerDeclaration_Symbol, gen_amethyst_IfStatement_Statement, gen_amethyst_ElseIfStatement_Statement, gen_amethyst_ElseStatement_Statement, gen_amethyst_CaseStatement_Statement, gen_amethyst_CaseElseStatement_Statement, gen_amethyst_WhenStatement_Statement, gen_amethyst_WhileStatement_Statement, gen_amethyst_IndexAccessExpression_Expression, gen_amethyst_ForStatement_Statement, gen_amethyst_ForInitializerDeclaration_Symbol, gen_amethyst_BreakStatement_Statement, gen_amethyst_NextStatement_Statement, gen_amethyst_ReturnStatement_Statement, gen_amethyst_JsCodeStatement_Statement, gen_amethyst_AssignmentExpression_Expression, gen_amethyst_CallExpression_Expression, gen_amethyst_MemberAccessExpression_Expression, gen_amethyst_OrExpression_Expression, gen_amethyst_AndExpression_Expression, gen_amethyst_RelationalExpression_Expression, gen_amethyst_EqualityExpression_Expression, gen_amethyst_ShiftExpression_Expression, gen_amethyst_AdditiveExpression_Expression, gen_amethyst_MultiplicativeExpression_Expression, gen_amethyst_MatchingExpression_Expression, gen_amethyst_InExpression_Expression, gen_amethyst_UnaryMinusExpression_Expression, gen_amethyst_NotExpression_Expression, gen_amethyst_TypeCastExpression_Expression, gen_amethyst_NewExpression_Expression, gen_amethyst_SuperExpression_Expression, gen_amethyst_ParenthisedExpression_Expression, gen_amethyst_NumberRangeLiteral_RangeLiteral, gen_amethyst_CharRangeLiteral_RangeLiteral, gen_amethyst_SelfExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)