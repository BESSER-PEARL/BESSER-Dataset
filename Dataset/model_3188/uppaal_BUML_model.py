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
BuiltInType: Enumeration = Enumeration(
    name="BuiltInType",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="CLOCK"),
			EnumerationLiteral(name="CHAN"),
			EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="VOID")
    }
)

DataVariablePrefix: Enumeration = Enumeration(
    name="DataVariablePrefix",
    literals={
            EnumerationLiteral(name="CONST"),
			EnumerationLiteral(name="META")
    }
)

CallType: Enumeration = Enumeration(
    name="CallType",
    literals={
            EnumerationLiteral(name="CALL_BY_VALUE"),
			EnumerationLiteral(name="CALL_BY_REFERENCE")
    }
)

LocationKind: Enumeration = Enumeration(
    name="LocationKind",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="URGENT"),
			EnumerationLiteral(name="COMMITED")
    }
)

SynchronizationKind: Enumeration = Enumeration(
    name="SynchronizationKind",
    literals={
            EnumerationLiteral(name="RECEIVE"),
			EnumerationLiteral(name="SEND")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="PLUS_EQUAL"),
			EnumerationLiteral(name="MINUS_EQUAL"),
			EnumerationLiteral(name="TIMES_EQUAL"),
			EnumerationLiteral(name="DIVIDE_EQUAL"),
			EnumerationLiteral(name="MODULO_EQUAL"),
			EnumerationLiteral(name="BIT_AND_EQUAL"),
			EnumerationLiteral(name="BIT_OR_EQUAL"),
			EnumerationLiteral(name="BIT_LEFT_EQUAL"),
			EnumerationLiteral(name="BIT_RIGHT_EQUAL"),
			EnumerationLiteral(name="BIT_XOR_EQUAL")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBTRACT"),
			EnumerationLiteral(name="MULTIPLICATE"),
			EnumerationLiteral(name="DIVIDE"),
			EnumerationLiteral(name="MODULO")
    }
)

CompareOperator: Enumeration = Enumeration(
    name="CompareOperator",
    literals={
            EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="GREATER_OR_EQUAL"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LESS_OR_EQUAL"),
			EnumerationLiteral(name="UNEQUAL")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="IMPLY")
    }
)

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="EXISTENTIAL"),
			EnumerationLiteral(name="UNIVERSAL")
    }
)

IncrementDecrementOperator: Enumeration = Enumeration(
    name="IncrementDecrementOperator",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
    }
)

BitShiftOperator: Enumeration = Enumeration(
    name="BitShiftOperator",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

MinMaxOperator: Enumeration = Enumeration(
    name="MinMaxOperator",
    literals={
            EnumerationLiteral(name="MIN"),
			EnumerationLiteral(name="MAX")
    }
)

BitwiseOperator: Enumeration = Enumeration(
    name="BitwiseOperator",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR")
    }
)

# Classes
TypedElementContainer = Class(name="TypedElementContainer")
uppaal_NTA = Class(name="uppaal::NTA")
core_NamedElement = Class(name="core::NamedElement")
core_CommentableElement = Class(name="core::CommentableElement")
GlobalDeclarations = Class(name="GlobalDeclarations")
Template = Class(name="Template")
SystemDeclarations = Class(name="SystemDeclarations")
uppaal_core_NamedElement = Class(name="uppaal::core::NamedElement", is_abstract=True)
uppaal_core_CommentableElement = Class(name="uppaal::core::CommentableElement", is_abstract=True)
uppaal_core_TypedElement = Class(name="uppaal::core::TypedElement", is_abstract=True)
Expression = Class(name="Expression")
uppaal_types_Type = Class(name="uppaal::types::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
uppaal_types_PredefinedType = Class(name="uppaal::types::PredefinedType")
Type = Class(name="Type")
uppaal_types_DeclaredType = Class(name="uppaal::types::DeclaredType")
TypeDeclaration = Class(name="TypeDeclaration")
uppaal_types_TypeExpression = Class(name="uppaal::types::TypeExpression", is_abstract=True)
uppaal_types_ScalarTypeSpecification = Class(name="uppaal::types::ScalarTypeSpecification")
TypeExpression = Class(name="TypeExpression")
uppaal_types_StructTypeSpecification = Class(name="uppaal::types::StructTypeSpecification")
TypedDeclaration = Class(name="TypedDeclaration")
uppaal_types_RangeTypeSpecification = Class(name="uppaal::types::RangeTypeSpecification")
IntegerBounds = Class(name="IntegerBounds")
uppaal_types_IntegerBounds = Class(name="uppaal::types::IntegerBounds")
uppaal_types_Library = Class(name="uppaal::types::Library")
PredefinedType = Class(name="PredefinedType")
uppaal_declarations_Declarations = Class(name="uppaal::declarations::Declarations", is_abstract=True)
Declaration = Class(name="Declaration")
uppaal_declarations_GlobalDeclarations = Class(name="uppaal::declarations::GlobalDeclarations")
Declarations = Class(name="Declarations")
global_ChannelPriorityDeclaration = Class(name="global::ChannelPriorityDeclaration")
uppaal_declarations_LocalDeclarations = Class(name="uppaal::declarations::LocalDeclarations")
uppaal_declarations_SystemDeclarations = Class(name="uppaal::declarations::SystemDeclarations")
system_System = Class(name="system::System")
system_ProgressMeasure = Class(name="system::ProgressMeasure")
uppaal_declarations_Declaration = Class(name="uppaal::declarations::Declaration", is_abstract=True)
uppaal_declarations_Function = Class(name="uppaal::declarations::Function")
core_TypedElement = Class(name="core::TypedElement")
Block = Class(name="Block")
ParameterContainer = Class(name="ParameterContainer")
uppaal_declarations_TypeDeclaration = Class(name="uppaal::declarations::TypeDeclaration")
DeclaredType = Class(name="DeclaredType")
uppaal_declarations_Variable = Class(name="uppaal::declarations::Variable")
Initializer = Class(name="Initializer")
uppaal_declarations_TypedElementContainer = Class(name="uppaal::declarations::TypedElementContainer", is_abstract=True)
TypedElement = Class(name="TypedElement")
uppaal_declarations_Parameter = Class(name="uppaal::declarations::Parameter")
Variable = Class(name="Variable")
uppaal_declarations_Initializer = Class(name="uppaal::declarations::Initializer", is_abstract=True)
uppaal_declarations_ExpressionInitializer = Class(name="uppaal::declarations::ExpressionInitializer")
uppaal_declarations_ArrayInitializer = Class(name="uppaal::declarations::ArrayInitializer")
uppaal_declarations_TypedDeclaration = Class(name="uppaal::declarations::TypedDeclaration")
declarations_Declaration = Class(name="declarations::Declaration")
declarations_TypedElementContainer = Class(name="declarations::TypedElementContainer")
uppaal_global_ChannelPriorityDeclaration = Class(name="uppaal::global::ChannelPriorityDeclaration")
uppaal_declarations_ParameterContainer = Class(name="uppaal::declarations::ParameterContainer")
global_ChannelPriorityGroup = Class(name="global::ChannelPriorityGroup")
uppaal_global_ChannelPriorityGroup = Class(name="uppaal::global::ChannelPriorityGroup")
global_PriorityItem = Class(name="global::PriorityItem")
IdentifierExpression = Class(name="IdentifierExpression")
uppaal_global_DefaultItem = Class(name="uppaal::global::DefaultItem")
uppaal_system_TemplateDeclaration = Class(name="uppaal::system::TemplateDeclaration")
RedefinedTemplate = Class(name="RedefinedTemplate")
uppaal_global_PriorityItem = Class(name="uppaal::global::PriorityItem", is_abstract=True)
uppaal_global_ChannelItem = Class(name="uppaal::global::ChannelItem")
PriorityItem = Class(name="PriorityItem")
system_InstantiationList = Class(name="system::InstantiationList")
uppaal_system_InstantiationList = Class(name="uppaal::system::InstantiationList")
AbstractTemplate = Class(name="AbstractTemplate")
uppaal_system_ProgressMeasure = Class(name="uppaal::system::ProgressMeasure")
uppaal_system_System = Class(name="uppaal::system::System")
uppaal_templates_Template = Class(name="uppaal::templates::Template")
LocalDeclarations = Class(name="LocalDeclarations")
uppaal_templates_AbstractTemplate = Class(name="uppaal::templates::AbstractTemplate", is_abstract=True)
uppaal_templates_RedefinedTemplate = Class(name="uppaal::templates::RedefinedTemplate")
system_TemplateDeclaration = Class(name="system::TemplateDeclaration")
Location = Class(name="Location")
Edge = Class(name="Edge")
uppaal_templates_Location = Class(name="uppaal::templates::Location")
visuals_PlanarElement = Class(name="visuals::PlanarElement")
visuals_ColoredElement = Class(name="visuals::ColoredElement")
uppaal_templates_Edge = Class(name="uppaal::templates::Edge")
visuals_LinearElement = Class(name="visuals::LinearElement")
uppaal_templates_Synchronization = Class(name="uppaal::templates::Synchronization")
Synchronization = Class(name="Synchronization")
Selection = Class(name="Selection")
uppaal_statements_Block = Class(name="uppaal::statements::Block")
Statement = Class(name="Statement")
uppaal_statements_EmptyStatement = Class(name="uppaal::statements::EmptyStatement")
uppaal_statements_ForLoop = Class(name="uppaal::statements::ForLoop")
uppaal_templates_Selection = Class(name="uppaal::templates::Selection")
uppaal_statements_Statement = Class(name="uppaal::statements::Statement", is_abstract=True)
uppaal_statements_Iteration = Class(name="uppaal::statements::Iteration")
statements_Statement = Class(name="statements::Statement")
uppaal_statements_WhileLoop = Class(name="uppaal::statements::WhileLoop")
uppaal_statements_IfStatement = Class(name="uppaal::statements::IfStatement")
uppaal_statements_DoWhileLoop = Class(name="uppaal::statements::DoWhileLoop")
uppaal_statements_ExpressionStatement = Class(name="uppaal::statements::ExpressionStatement")
uppaal_statements_ReturnStatement = Class(name="uppaal::statements::ReturnStatement")
uppaal_expressions_PlusExpression = Class(name="uppaal::expressions::PlusExpression")
uppaal_expressions_MinusExpression = Class(name="uppaal::expressions::MinusExpression")
uppaal_expressions_BinaryExpression = Class(name="uppaal::expressions::BinaryExpression", is_abstract=True)
uppaal_expressions_Expression = Class(name="uppaal::expressions::Expression", is_abstract=True)
uppaal_expressions_NegationExpression = Class(name="uppaal::expressions::NegationExpression")
uppaal_expressions_AssignmentExpression = Class(name="uppaal::expressions::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
uppaal_expressions_IdentifierExpression = Class(name="uppaal::expressions::IdentifierExpression")
uppaal_expressions_LogicalExpression = Class(name="uppaal::expressions::LogicalExpression")
uppaal_expressions_ScopedIdentifierExpression = Class(name="uppaal::expressions::ScopedIdentifierExpression")
uppaal_expressions_LiteralExpression = Class(name="uppaal::expressions::LiteralExpression")
uppaal_expressions_ArithmeticExpression = Class(name="uppaal::expressions::ArithmeticExpression")
uppaal_expressions_FunctionCallExpression = Class(name="uppaal::expressions::FunctionCallExpression")
Function = Class(name="Function")
uppaal_expressions_CompareExpression = Class(name="uppaal::expressions::CompareExpression")
uppaal_expressions_IncrementDecrementExpression = Class(name="uppaal::expressions::IncrementDecrementExpression", is_abstract=True)
uppaal_expressions_ConditionExpression = Class(name="uppaal::expressions::ConditionExpression")
uppaal_expressions_QuantificationExpression = Class(name="uppaal::expressions::QuantificationExpression")
expressions_Expression = Class(name="expressions::Expression")
uppaal_expressions_ChannelPrefixExpression = Class(name="uppaal::expressions::ChannelPrefixExpression")
uppaal_expressions_PreIncrementDecrementExpression = Class(name="uppaal::expressions::PreIncrementDecrementExpression")
IncrementDecrementExpression = Class(name="IncrementDecrementExpression")
uppaal_expressions_PostIncrementDecrementExpression = Class(name="uppaal::expressions::PostIncrementDecrementExpression")
uppaal_expressions_BitShiftExpression = Class(name="uppaal::expressions::BitShiftExpression")
uppaal_expressions_MinMaxExpression = Class(name="uppaal::expressions::MinMaxExpression")
uppaal_expressions_BitwiseExpression = Class(name="uppaal::expressions::BitwiseExpression")
uppaal_visuals_LinearElement = Class(name="uppaal::visuals::LinearElement", is_abstract=True)
uppaal_visuals_Point = Class(name="uppaal::visuals::Point")
uppaal_expressions_DataPrefixExpression = Class(name="uppaal::expressions::DataPrefixExpression")
uppaal_visuals_ColoredElement = Class(name="uppaal::visuals::ColoredElement", is_abstract=True)
uppaal_visuals_PlanarElement = Class(name="uppaal::visuals::PlanarElement", is_abstract=True)
Point = Class(name="Point")

# TypedElementContainer class attributes and methods

# uppaal_NTA class attributes and methods

# core_NamedElement class attributes and methods

# core_CommentableElement class attributes and methods

# GlobalDeclarations class attributes and methods

# Template class attributes and methods

# SystemDeclarations class attributes and methods

# uppaal_core_NamedElement class attributes and methods
uppaal_core_NamedElement_name: Property = Property(name="name", type=StringType)
uppaal_core_NamedElement.attributes={uppaal_core_NamedElement_name}

# uppaal_core_CommentableElement class attributes and methods
uppaal_core_CommentableElement_comment: Property = Property(name="comment", type=StringType)
uppaal_core_CommentableElement.attributes={uppaal_core_CommentableElement_comment}

# uppaal_core_TypedElement class attributes and methods

# Expression class attributes and methods

# uppaal_types_Type class attributes and methods
uppaal_types_Type_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_Type.attributes={uppaal_types_Type_baseType}

# NamedElement class attributes and methods

# uppaal_types_PredefinedType class attributes and methods
uppaal_types_PredefinedType_type: Property = Property(name="type", type=StringType)
uppaal_types_PredefinedType.attributes={uppaal_types_PredefinedType_type}

# Type class attributes and methods

# uppaal_types_DeclaredType class attributes and methods

# TypeDeclaration class attributes and methods

# uppaal_types_TypeExpression class attributes and methods

# uppaal_types_ScalarTypeSpecification class attributes and methods

# TypeExpression class attributes and methods

# uppaal_types_StructTypeSpecification class attributes and methods

# TypedDeclaration class attributes and methods

# uppaal_types_RangeTypeSpecification class attributes and methods

# IntegerBounds class attributes and methods

# uppaal_types_IntegerBounds class attributes and methods

# uppaal_types_Library class attributes and methods

# PredefinedType class attributes and methods

# uppaal_declarations_Declarations class attributes and methods

# Declaration class attributes and methods

# uppaal_declarations_GlobalDeclarations class attributes and methods

# Declarations class attributes and methods

# global_ChannelPriorityDeclaration class attributes and methods

# uppaal_declarations_LocalDeclarations class attributes and methods

# uppaal_declarations_SystemDeclarations class attributes and methods

# system_System class attributes and methods

# system_ProgressMeasure class attributes and methods

# uppaal_declarations_Declaration class attributes and methods

# uppaal_declarations_Function class attributes and methods

# core_TypedElement class attributes and methods

# Block class attributes and methods

# ParameterContainer class attributes and methods

# uppaal_declarations_TypeDeclaration class attributes and methods

# DeclaredType class attributes and methods

# uppaal_declarations_Variable class attributes and methods

# Initializer class attributes and methods

# uppaal_declarations_TypedElementContainer class attributes and methods

# TypedElement class attributes and methods

# uppaal_declarations_Parameter class attributes and methods
uppaal_declarations_Parameter_callType: Property = Property(name="callType", type=StringType)
uppaal_declarations_Parameter.attributes={uppaal_declarations_Parameter_callType}

# Variable class attributes and methods

# uppaal_declarations_Initializer class attributes and methods

# uppaal_declarations_ExpressionInitializer class attributes and methods

# uppaal_declarations_ArrayInitializer class attributes and methods

# uppaal_declarations_TypedDeclaration class attributes and methods

# declarations_Declaration class attributes and methods

# declarations_TypedElementContainer class attributes and methods

# uppaal_global_ChannelPriorityDeclaration class attributes and methods

# uppaal_declarations_ParameterContainer class attributes and methods

# global_ChannelPriorityGroup class attributes and methods

# uppaal_global_ChannelPriorityGroup class attributes and methods

# global_PriorityItem class attributes and methods

# IdentifierExpression class attributes and methods

# uppaal_global_DefaultItem class attributes and methods

# uppaal_system_TemplateDeclaration class attributes and methods

# RedefinedTemplate class attributes and methods

# uppaal_global_PriorityItem class attributes and methods

# uppaal_global_ChannelItem class attributes and methods

# PriorityItem class attributes and methods

# system_InstantiationList class attributes and methods

# uppaal_system_InstantiationList class attributes and methods

# AbstractTemplate class attributes and methods

# uppaal_system_ProgressMeasure class attributes and methods

# uppaal_system_System class attributes and methods

# uppaal_templates_Template class attributes and methods

# LocalDeclarations class attributes and methods

# uppaal_templates_AbstractTemplate class attributes and methods

# uppaal_templates_RedefinedTemplate class attributes and methods

# system_TemplateDeclaration class attributes and methods

# Location class attributes and methods

# Edge class attributes and methods

# uppaal_templates_Location class attributes and methods
uppaal_templates_Location_locationTimeKind: Property = Property(name="locationTimeKind", type=StringType)
uppaal_templates_Location.attributes={uppaal_templates_Location_locationTimeKind}

# visuals_PlanarElement class attributes and methods

# visuals_ColoredElement class attributes and methods

# uppaal_templates_Edge class attributes and methods

# visuals_LinearElement class attributes and methods

# uppaal_templates_Synchronization class attributes and methods
uppaal_templates_Synchronization_kind: Property = Property(name="kind", type=StringType)
uppaal_templates_Synchronization.attributes={uppaal_templates_Synchronization_kind}

# Synchronization class attributes and methods

# Selection class attributes and methods

# uppaal_statements_Block class attributes and methods

# Statement class attributes and methods

# uppaal_statements_EmptyStatement class attributes and methods

# uppaal_statements_ForLoop class attributes and methods

# uppaal_templates_Selection class attributes and methods

# uppaal_statements_Statement class attributes and methods

# uppaal_statements_Iteration class attributes and methods

# statements_Statement class attributes and methods

# uppaal_statements_WhileLoop class attributes and methods

# uppaal_statements_IfStatement class attributes and methods

# uppaal_statements_DoWhileLoop class attributes and methods

# uppaal_statements_ExpressionStatement class attributes and methods

# uppaal_statements_ReturnStatement class attributes and methods

# uppaal_expressions_PlusExpression class attributes and methods

# uppaal_expressions_MinusExpression class attributes and methods

# uppaal_expressions_BinaryExpression class attributes and methods

# uppaal_expressions_Expression class attributes and methods

# uppaal_expressions_NegationExpression class attributes and methods

# uppaal_expressions_AssignmentExpression class attributes and methods
uppaal_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_AssignmentExpression.attributes={uppaal_expressions_AssignmentExpression_operator}

# BinaryExpression class attributes and methods

# uppaal_expressions_IdentifierExpression class attributes and methods

# uppaal_expressions_LogicalExpression class attributes and methods
uppaal_expressions_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_LogicalExpression.attributes={uppaal_expressions_LogicalExpression_operator}

# uppaal_expressions_ScopedIdentifierExpression class attributes and methods

# uppaal_expressions_LiteralExpression class attributes and methods
uppaal_expressions_LiteralExpression_text: Property = Property(name="text", type=StringType)
uppaal_expressions_LiteralExpression.attributes={uppaal_expressions_LiteralExpression_text}

# uppaal_expressions_ArithmeticExpression class attributes and methods
uppaal_expressions_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_ArithmeticExpression.attributes={uppaal_expressions_ArithmeticExpression_operator}

# uppaal_expressions_FunctionCallExpression class attributes and methods

# Function class attributes and methods

# uppaal_expressions_CompareExpression class attributes and methods
uppaal_expressions_CompareExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_CompareExpression.attributes={uppaal_expressions_CompareExpression_operator}

# uppaal_expressions_IncrementDecrementExpression class attributes and methods
uppaal_expressions_IncrementDecrementExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_IncrementDecrementExpression.attributes={uppaal_expressions_IncrementDecrementExpression_operator}

# uppaal_expressions_ConditionExpression class attributes and methods

# uppaal_expressions_QuantificationExpression class attributes and methods
uppaal_expressions_QuantificationExpression_quantifier: Property = Property(name="quantifier", type=StringType)
uppaal_expressions_QuantificationExpression.attributes={uppaal_expressions_QuantificationExpression_quantifier}

# expressions_Expression class attributes and methods

# uppaal_expressions_ChannelPrefixExpression class attributes and methods
uppaal_expressions_ChannelPrefixExpression_urgent: Property = Property(name="urgent", type=BooleanType)
uppaal_expressions_ChannelPrefixExpression_broadcast: Property = Property(name="broadcast", type=BooleanType)
uppaal_expressions_ChannelPrefixExpression.attributes={uppaal_expressions_ChannelPrefixExpression_urgent, uppaal_expressions_ChannelPrefixExpression_broadcast}

# uppaal_expressions_PreIncrementDecrementExpression class attributes and methods

# IncrementDecrementExpression class attributes and methods

# uppaal_expressions_PostIncrementDecrementExpression class attributes and methods

# uppaal_expressions_BitShiftExpression class attributes and methods
uppaal_expressions_BitShiftExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitShiftExpression.attributes={uppaal_expressions_BitShiftExpression_operator}

# uppaal_expressions_MinMaxExpression class attributes and methods
uppaal_expressions_MinMaxExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_MinMaxExpression.attributes={uppaal_expressions_MinMaxExpression_operator}

# uppaal_expressions_BitwiseExpression class attributes and methods
uppaal_expressions_BitwiseExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitwiseExpression.attributes={uppaal_expressions_BitwiseExpression_operator}

# uppaal_visuals_LinearElement class attributes and methods

# uppaal_visuals_Point class attributes and methods
uppaal_visuals_Point_x: Property = Property(name="x", type=IntegerType)
uppaal_visuals_Point_y: Property = Property(name="y", type=IntegerType)
uppaal_visuals_Point.attributes={uppaal_visuals_Point_y, uppaal_visuals_Point_x}

# uppaal_expressions_DataPrefixExpression class attributes and methods
uppaal_expressions_DataPrefixExpression_prefix: Property = Property(name="prefix", type=StringType)
uppaal_expressions_DataPrefixExpression.attributes={uppaal_expressions_DataPrefixExpression_prefix}

# uppaal_visuals_ColoredElement class attributes and methods
uppaal_visuals_ColoredElement_colorCode: Property = Property(name="colorCode", type=StringType)
uppaal_visuals_ColoredElement.attributes={uppaal_visuals_ColoredElement_colorCode}

# uppaal_visuals_PlanarElement class attributes and methods

# Point class attributes and methods

# Relationships
globalDeclarations0: BinaryAssociation = BinaryAssociation(
    name="globalDeclarations0",
    ends={
        Property(name="GlobalDeclarations", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA", type=GlobalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
template1: BinaryAssociation = BinaryAssociation(
    name="template1",
    ends={
        Property(name="Template", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA2", type=Template, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
systemDeclarations3: BinaryAssociation = BinaryAssociation(
    name="systemDeclarations3",
    ends={
        Property(name="SystemDeclarations", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA4", type=SystemDeclarations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container5: BinaryAssociation = BinaryAssociation(
    name="container5",
    ends={
        Property(name="declarations", type=uppaal_core_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypedElementContainer", type=TypedElementContainer, multiplicity=Multiplicity(0, 1))
    }
)
typeDefinition6: BinaryAssociation = BinaryAssociation(
    name="typeDefinition6",
    ends={
        Property(name="Expression", type=uppaal_core_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_core_TypedElement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
typeDeclaration7: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration7",
    ends={
        Property(name="declarations8", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeDeclaration", type=TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition9: BinaryAssociation = BinaryAssociation(
    name="typeDefinition9",
    ends={
        Property(name="Expression10", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_DeclaredType", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
declaration21: BinaryAssociation = BinaryAssociation(
    name="declaration21",
    ends={
        Property(name="uppaal_declarations_Declarations", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Declaration", type=uppaal_declarations_Declarations, multiplicity=Multiplicity(1, 1))
    }
)
sizeExpression11: BinaryAssociation = BinaryAssociation(
    name="sizeExpression11",
    ends={
        Property(name="Expression12", type=uppaal_types_ScalarTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_ScalarTypeSpecification", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration13: BinaryAssociation = BinaryAssociation(
    name="declaration13",
    ends={
        Property(name="TypedDeclaration", type=uppaal_types_StructTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_StructTypeSpecification", type=TypedDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bounds14: BinaryAssociation = BinaryAssociation(
    name="bounds14",
    ends={
        Property(name="IntegerBounds", type=uppaal_types_RangeTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_RangeTypeSpecification", type=IntegerBounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound15: BinaryAssociation = BinaryAssociation(
    name="lowerBound15",
    ends={
        Property(name="Expression16", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound17: BinaryAssociation = BinaryAssociation(
    name="upperBound17",
    ends={
        Property(name="Expression19", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds18", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types20: BinaryAssociation = BinaryAssociation(
    name="types20",
    ends={
        Property(name="PredefinedType", type=uppaal_types_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Library", type=PredefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelPriority22: BinaryAssociation = BinaryAssociation(
    name="channelPriority22",
    ends={
        Property(name="global_ChannelPriorityDeclaration", type=uppaal_declarations_GlobalDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_GlobalDeclarations", type=global_ChannelPriorityDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system23: BinaryAssociation = BinaryAssociation(
    name="system23",
    ends={
        Property(name="system_System", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations", type=system_System, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
progressMeasure24: BinaryAssociation = BinaryAssociation(
    name="progressMeasure24",
    ends={
        Property(name="system_ProgressMeasure", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations25", type=system_ProgressMeasure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block26: BinaryAssociation = BinaryAssociation(
    name="block26",
    ends={
        Property(name="Block", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter27: BinaryAssociation = BinaryAssociation(
    name="parameter27",
    ends={
        Property(name="ParameterContainer", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function28", type=ParameterContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="types", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclaredType", type=DeclaredType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition30: BinaryAssociation = BinaryAssociation(
    name="typeDefinition30",
    ends={
        Property(name="Expression31", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index32: BinaryAssociation = BinaryAssociation(
    name="index32",
    ends={
        Property(name="Expression33", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer34: BinaryAssociation = BinaryAssociation(
    name="initializer34",
    ends={
        Property(name="Initializer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable35", type=Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition36: BinaryAssociation = BinaryAssociation(
    name="typeDefinition36",
    ends={
        Property(name="Expression37", type=uppaal_declarations_TypedElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypedElementContainer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="core", type=uppaal_declarations_TypedElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="TypedElement", type=TypedElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression39: BinaryAssociation = BinaryAssociation(
    name="expression39",
    ends={
        Property(name="Expression40", type=uppaal_declarations_ExpressionInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ExpressionInitializer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer41: BinaryAssociation = BinaryAssociation(
    name="initializer41",
    ends={
        Property(name="Initializer42", type=uppaal_declarations_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ArrayInitializer", type=Initializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
groups43: BinaryAssociation = BinaryAssociation(
    name="groups43",
    ends={
        Property(name="global_ChannelPriorityGroup", type=uppaal_global_ChannelPriorityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriorityDeclaration", type=global_ChannelPriorityGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
items44: BinaryAssociation = BinaryAssociation(
    name="items44",
    ends={
        Property(name="global_PriorityItem", type=uppaal_global_ChannelPriorityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriorityGroup", type=global_PriorityItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
channelExpression45: BinaryAssociation = BinaryAssociation(
    name="channelExpression45",
    ends={
        Property(name="IdentifierExpression", type=uppaal_global_ChannelItem, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelItem", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiationList49: BinaryAssociation = BinaryAssociation(
    name="instantiationList49",
    ends={
        Property(name="system_InstantiationList", type=uppaal_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_System", type=system_InstantiationList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template50: BinaryAssociation = BinaryAssociation(
    name="template50",
    ends={
        Property(name="AbstractTemplate", type=uppaal_system_InstantiationList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_InstantiationList", type=AbstractTemplate, multiplicity=Multiplicity(1, 9999))
    }
)
expression51: BinaryAssociation = BinaryAssociation(
    name="expression51",
    ends={
        Property(name="Expression52", type=uppaal_system_ProgressMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_ProgressMeasure", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declaredTemplate46: BinaryAssociation = BinaryAssociation(
    name="declaredTemplate46",
    ends={
        Property(name="templates", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="RedefinedTemplate", type=RedefinedTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument47: BinaryAssociation = BinaryAssociation(
    name="argument47",
    ends={
        Property(name="Expression48", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_TemplateDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter53: BinaryAssociation = BinaryAssociation(
    name="parameter53",
    ends={
        Property(name="ParameterContainer54", type=uppaal_templates_AbstractTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_AbstractTemplate", type=ParameterContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations55: BinaryAssociation = BinaryAssociation(
    name="declarations55",
    ends={
        Property(name="LocalDeclarations", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init60: BinaryAssociation = BinaryAssociation(
    name="init60",
    ends={
        Property(name="Location62", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template61", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
referredTemplate63: BinaryAssociation = BinaryAssociation(
    name="referredTemplate63",
    ends={
        Property(name="AbstractTemplate64", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_RedefinedTemplate", type=AbstractTemplate, multiplicity=Multiplicity(1, 1))
    }
)
declaration65: BinaryAssociation = BinaryAssociation(
    name="declaration65",
    ends={
        Property(name="declarations66", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=system_TemplateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
location56: BinaryAssociation = BinaryAssociation(
    name="location56",
    ends={
        Property(name="templates57", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Location", type=Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edge58: BinaryAssociation = BinaryAssociation(
    name="edge58",
    ends={
        Property(name="templates59", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Edge", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariant70: BinaryAssociation = BinaryAssociation(
    name="invariant70",
    ends={
        Property(name="Expression71", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Location", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingEdges72: BinaryAssociation = BinaryAssociation(
    name="incomingEdges72",
    ends={
        Property(name="templates74", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="Edge73", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges75: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges75",
    ends={
        Property(name="templates77", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="Edge76", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
parentTemplate67: BinaryAssociation = BinaryAssociation(
    name="parentTemplate67",
    ends={
        Property(name="templates69", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="Template68", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
source78: BinaryAssociation = BinaryAssociation(
    name="source78",
    ends={
        Property(name="templates80", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Location79", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="templates83", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Location82", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate84: BinaryAssociation = BinaryAssociation(
    name="parentTemplate84",
    ends={
        Property(name="templates86", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Template85", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
guard87: BinaryAssociation = BinaryAssociation(
    name="guard87",
    ends={
        Property(name="Expression88", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
channelExpression96: BinaryAssociation = BinaryAssociation(
    name="channelExpression96",
    ends={
        Property(name="IdentifierExpression97", type=uppaal_templates_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Synchronization", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
update89: BinaryAssociation = BinaryAssociation(
    name="update89",
    ends={
        Property(name="Expression91", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge90", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization92: BinaryAssociation = BinaryAssociation(
    name="synchronization92",
    ends={
        Property(name="Synchronization", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge93", type=Synchronization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection94: BinaryAssociation = BinaryAssociation(
    name="selection94",
    ends={
        Property(name="Selection", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge95", type=Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations98: BinaryAssociation = BinaryAssociation(
    name="declarations98",
    ends={
        Property(name="LocalDeclarations99", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement100: BinaryAssociation = BinaryAssociation(
    name="statement100",
    ends={
        Property(name="Statement", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block101", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statement110: BinaryAssociation = BinaryAssociation(
    name="statement110",
    ends={
        Property(name="Statement112", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop111", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement113: BinaryAssociation = BinaryAssociation(
    name="statement113",
    ends={
        Property(name="Statement114", type=uppaal_statements_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Iteration", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization102: BinaryAssociation = BinaryAssociation(
    name="initialization102",
    ends={
        Property(name="Expression103", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition104: BinaryAssociation = BinaryAssociation(
    name="condition104",
    ends={
        Property(name="Expression106", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop105", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteration107: BinaryAssociation = BinaryAssociation(
    name="iteration107",
    ends={
        Property(name="Expression109", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop108", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement120: BinaryAssociation = BinaryAssociation(
    name="statement120",
    ends={
        Property(name="Statement121", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression122: BinaryAssociation = BinaryAssociation(
    name="expression122",
    ends={
        Property(name="Expression124", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop123", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression125: BinaryAssociation = BinaryAssociation(
    name="ifExpression125",
    ends={
        Property(name="Expression126", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression115: BinaryAssociation = BinaryAssociation(
    name="expression115",
    ends={
        Property(name="Expression116", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement117: BinaryAssociation = BinaryAssociation(
    name="statement117",
    ends={
        Property(name="Statement119", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop118", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnExpression133: BinaryAssociation = BinaryAssociation(
    name="returnExpression133",
    ends={
        Property(name="Expression134", type=uppaal_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression135: BinaryAssociation = BinaryAssociation(
    name="expression135",
    ends={
        Property(name="Expression136", type=uppaal_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement127: BinaryAssociation = BinaryAssociation(
    name="thenStatement127",
    ends={
        Property(name="Statement129", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement128", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement130: BinaryAssociation = BinaryAssociation(
    name="elseStatement130",
    ends={
        Property(name="Statement132", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement131", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
confirmedExpression139: BinaryAssociation = BinaryAssociation(
    name="confirmedExpression139",
    ends={
        Property(name="Expression140", type=uppaal_expressions_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_PlusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invertedExpression141: BinaryAssociation = BinaryAssociation(
    name="invertedExpression141",
    ends={
        Property(name="Expression142", type=uppaal_expressions_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_MinusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negatedExpression137: BinaryAssociation = BinaryAssociation(
    name="negatedExpression137",
    ends={
        Property(name="Expression138", type=uppaal_expressions_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_NegationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index149: BinaryAssociation = BinaryAssociation(
    name="index149",
    ends={
        Property(name="Expression151", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression150", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
secondExpr145: BinaryAssociation = BinaryAssociation(
    name="secondExpr145",
    ends={
        Property(name="Expression147", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression146", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstExpr143: BinaryAssociation = BinaryAssociation(
    name="firstExpr143",
    ends={
        Property(name="Expression144", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier148: BinaryAssociation = BinaryAssociation(
    name="identifier148",
    ends={
        Property(name="NamedElement", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
scope152: BinaryAssociation = BinaryAssociation(
    name="scope152",
    ends={
        Property(name="Expression153", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier154: BinaryAssociation = BinaryAssociation(
    name="identifier154",
    ends={
        Property(name="IdentifierExpression156", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression155", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function157: BinaryAssociation = BinaryAssociation(
    name="function157",
    ends={
        Property(name="Function", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
argument158: BinaryAssociation = BinaryAssociation(
    name="argument158",
    ends={
        Property(name="Expression160", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression159", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression171: BinaryAssociation = BinaryAssociation(
    name="expression171",
    ends={
        Property(name="Expression172", type=uppaal_expressions_IncrementDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IncrementDecrementExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression161: BinaryAssociation = BinaryAssociation(
    name="ifExpression161",
    ends={
        Property(name="Expression162", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression163: BinaryAssociation = BinaryAssociation(
    name="thenExpression163",
    ends={
        Property(name="Expression165", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression164", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression166: BinaryAssociation = BinaryAssociation(
    name="elseExpression166",
    ends={
        Property(name="Expression168", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression167", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression169: BinaryAssociation = BinaryAssociation(
    name="expression169",
    ends={
        Property(name="Expression170", type=uppaal_expressions_QuantificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_QuantificationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bendPoint177: BinaryAssociation = BinaryAssociation(
    name="bendPoint177",
    ends={
        Property(name="Point178", type=uppaal_visuals_LinearElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_LinearElement", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelType173: BinaryAssociation = BinaryAssociation(
    name="channelType173",
    ends={
        Property(name="Type", type=uppaal_expressions_ChannelPrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ChannelPrefixExpression", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
dataTypeExpression174: BinaryAssociation = BinaryAssociation(
    name="dataTypeExpression174",
    ends={
        Property(name="Expression175", type=uppaal_expressions_DataPrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_DataPrefixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position176: BinaryAssociation = BinaryAssociation(
    name="position176",
    ends={
        Property(name="Point", type=uppaal_visuals_PlanarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_PlanarElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_uppaal_NTA_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_NTA)
gen_uppaal_NTA_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_NTA)
gen_uppaal_types_ScalarTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_ScalarTypeSpecification)
gen_uppaal_types_Type_NamedElement = Generalization(general=NamedElement, specific=uppaal_types_Type)
gen_uppaal_types_PredefinedType_Type = Generalization(general=Type, specific=uppaal_types_PredefinedType)
gen_uppaal_types_DeclaredType_Type = Generalization(general=Type, specific=uppaal_types_DeclaredType)
gen_uppaal_types_TypeExpression_Expression = Generalization(general=Expression, specific=uppaal_types_TypeExpression)
gen_uppaal_types_StructTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_StructTypeSpecification)
gen_uppaal_types_RangeTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_RangeTypeSpecification)
gen_uppaal_declarations_GlobalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_GlobalDeclarations)
gen_uppaal_declarations_LocalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_LocalDeclarations)
gen_uppaal_declarations_SystemDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_SystemDeclarations)
gen_uppaal_declarations_Function_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_Function_core_TypedElement = Generalization(general=core_TypedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_TypeDeclaration)
gen_uppaal_declarations_Variable_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_Variable_core_TypedElement = Generalization(general=core_TypedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_Parameter_Variable = Generalization(general=Variable, specific=uppaal_declarations_Parameter)
gen_uppaal_declarations_ExpressionInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ExpressionInitializer)
gen_uppaal_declarations_ArrayInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ArrayInitializer)
gen_uppaal_declarations_TypedDeclaration_declarations_Declaration = Generalization(general=declarations_Declaration, specific=uppaal_declarations_TypedDeclaration)
gen_uppaal_declarations_TypedDeclaration_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_declarations_TypedDeclaration)
gen_uppaal_global_ChannelPriorityDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_global_ChannelPriorityDeclaration)
gen_uppaal_declarations_ParameterContainer_TypedElementContainer = Generalization(general=TypedElementContainer, specific=uppaal_declarations_ParameterContainer)
gen_uppaal_global_DefaultItem_PriorityItem = Generalization(general=PriorityItem, specific=uppaal_global_DefaultItem)
gen_uppaal_system_TemplateDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_system_TemplateDeclaration)
gen_uppaal_global_ChannelItem_PriorityItem = Generalization(general=PriorityItem, specific=uppaal_global_ChannelItem)
gen_uppaal_templates_Template_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_Template)
gen_uppaal_templates_AbstractTemplate_NamedElement = Generalization(general=NamedElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_RedefinedTemplate_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_RedefinedTemplate)
gen_uppaal_templates_Location_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_PlanarElement = Generalization(general=visuals_PlanarElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Edge_visuals_LinearElement = Generalization(general=visuals_LinearElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Edge)
gen_uppaal_statements_Block_Statement = Generalization(general=Statement, specific=uppaal_statements_Block)
gen_uppaal_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_EmptyStatement)
gen_uppaal_statements_ForLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_ForLoop)
gen_uppaal_templates_Selection_TypedElementContainer = Generalization(general=TypedElementContainer, specific=uppaal_templates_Selection)
gen_uppaal_statements_Iteration_statements_Statement = Generalization(general=statements_Statement, specific=uppaal_statements_Iteration)
gen_uppaal_statements_Iteration_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_statements_Iteration)
gen_uppaal_statements_WhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_WhileLoop)
gen_uppaal_statements_IfStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_IfStatement)
gen_uppaal_statements_DoWhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_DoWhileLoop)
gen_uppaal_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ReturnStatement)
gen_uppaal_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ExpressionStatement)
gen_uppaal_expressions_PlusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_PlusExpression)
gen_uppaal_expressions_MinusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_MinusExpression)
gen_uppaal_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_BinaryExpression)
gen_uppaal_expressions_NegationExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_NegationExpression)
gen_uppaal_expressions_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_AssignmentExpression)
gen_uppaal_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IdentifierExpression)
gen_uppaal_expressions_ScopedIdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ScopedIdentifierExpression)
gen_uppaal_expressions_LiteralExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_LiteralExpression)
gen_uppaal_expressions_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_ArithmeticExpression)
gen_uppaal_expressions_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_LogicalExpression)
gen_uppaal_expressions_FunctionCallExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_FunctionCallExpression)
gen_uppaal_expressions_CompareExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_CompareExpression)
gen_uppaal_expressions_IncrementDecrementExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IncrementDecrementExpression)
gen_uppaal_expressions_ConditionExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ConditionExpression)
gen_uppaal_expressions_QuantificationExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_QuantificationExpression_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_ChannelPrefixExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ChannelPrefixExpression)
gen_uppaal_expressions_PreIncrementDecrementExpression_IncrementDecrementExpression = Generalization(general=IncrementDecrementExpression, specific=uppaal_expressions_PreIncrementDecrementExpression)
gen_uppaal_expressions_PostIncrementDecrementExpression_IncrementDecrementExpression = Generalization(general=IncrementDecrementExpression, specific=uppaal_expressions_PostIncrementDecrementExpression)
gen_uppaal_expressions_BitShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitShiftExpression)
gen_uppaal_expressions_MinMaxExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_MinMaxExpression)
gen_uppaal_expressions_BitwiseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitwiseExpression)
gen_uppaal_expressions_DataPrefixExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_DataPrefixExpression)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={TypedElementContainer, uppaal_NTA, core_NamedElement, core_CommentableElement, GlobalDeclarations, Template, SystemDeclarations, uppaal_core_NamedElement, uppaal_core_CommentableElement, uppaal_core_TypedElement, Expression, uppaal_types_Type, NamedElement, uppaal_types_PredefinedType, Type, uppaal_types_DeclaredType, TypeDeclaration, uppaal_types_TypeExpression, uppaal_types_ScalarTypeSpecification, TypeExpression, uppaal_types_StructTypeSpecification, TypedDeclaration, uppaal_types_RangeTypeSpecification, IntegerBounds, uppaal_types_IntegerBounds, uppaal_types_Library, PredefinedType, uppaal_declarations_Declarations, Declaration, uppaal_declarations_GlobalDeclarations, Declarations, global_ChannelPriorityDeclaration, uppaal_declarations_LocalDeclarations, uppaal_declarations_SystemDeclarations, system_System, system_ProgressMeasure, uppaal_declarations_Declaration, uppaal_declarations_Function, core_TypedElement, Block, ParameterContainer, uppaal_declarations_TypeDeclaration, DeclaredType, uppaal_declarations_Variable, Initializer, uppaal_declarations_TypedElementContainer, TypedElement, uppaal_declarations_Parameter, Variable, uppaal_declarations_Initializer, uppaal_declarations_ExpressionInitializer, uppaal_declarations_ArrayInitializer, uppaal_declarations_TypedDeclaration, declarations_Declaration, declarations_TypedElementContainer, uppaal_global_ChannelPriorityDeclaration, uppaal_declarations_ParameterContainer, global_ChannelPriorityGroup, uppaal_global_ChannelPriorityGroup, global_PriorityItem, IdentifierExpression, uppaal_global_DefaultItem, uppaal_system_TemplateDeclaration, RedefinedTemplate, uppaal_global_PriorityItem, uppaal_global_ChannelItem, PriorityItem, system_InstantiationList, uppaal_system_InstantiationList, AbstractTemplate, uppaal_system_ProgressMeasure, uppaal_system_System, uppaal_templates_Template, LocalDeclarations, uppaal_templates_AbstractTemplate, uppaal_templates_RedefinedTemplate, system_TemplateDeclaration, Location, Edge, uppaal_templates_Location, visuals_PlanarElement, visuals_ColoredElement, uppaal_templates_Edge, visuals_LinearElement, uppaal_templates_Synchronization, Synchronization, Selection, uppaal_statements_Block, Statement, uppaal_statements_EmptyStatement, uppaal_statements_ForLoop, uppaal_templates_Selection, uppaal_statements_Statement, uppaal_statements_Iteration, statements_Statement, uppaal_statements_WhileLoop, uppaal_statements_IfStatement, uppaal_statements_DoWhileLoop, uppaal_statements_ExpressionStatement, uppaal_statements_ReturnStatement, uppaal_expressions_PlusExpression, uppaal_expressions_MinusExpression, uppaal_expressions_BinaryExpression, uppaal_expressions_Expression, uppaal_expressions_NegationExpression, uppaal_expressions_AssignmentExpression, BinaryExpression, uppaal_expressions_IdentifierExpression, uppaal_expressions_LogicalExpression, uppaal_expressions_ScopedIdentifierExpression, uppaal_expressions_LiteralExpression, uppaal_expressions_ArithmeticExpression, uppaal_expressions_FunctionCallExpression, Function, uppaal_expressions_CompareExpression, uppaal_expressions_IncrementDecrementExpression, uppaal_expressions_ConditionExpression, uppaal_expressions_QuantificationExpression, expressions_Expression, uppaal_expressions_ChannelPrefixExpression, uppaal_expressions_PreIncrementDecrementExpression, IncrementDecrementExpression, uppaal_expressions_PostIncrementDecrementExpression, uppaal_expressions_BitShiftExpression, uppaal_expressions_MinMaxExpression, uppaal_expressions_BitwiseExpression, uppaal_visuals_LinearElement, uppaal_visuals_Point, uppaal_expressions_DataPrefixExpression, uppaal_visuals_ColoredElement, uppaal_visuals_PlanarElement, Point, BuiltInType, DataVariablePrefix, CallType, LocationKind, SynchronizationKind, AssignmentOperator, ArithmeticOperator, CompareOperator, LogicalOperator, Quantifier, IncrementDecrementOperator, BitShiftOperator, MinMaxOperator, BitwiseOperator},
    associations={globalDeclarations0, template1, systemDeclarations3, container5, typeDefinition6, typeDeclaration7, typeDefinition9, declaration21, sizeExpression11, declaration13, bounds14, lowerBound15, upperBound17, types20, channelPriority22, system23, progressMeasure24, block26, parameter27, type29, typeDefinition30, index32, initializer34, typeDefinition36, elements38, expression39, initializer41, groups43, items44, channelExpression45, instantiationList49, template50, expression51, declaredTemplate46, argument47, parameter53, declarations55, init60, referredTemplate63, declaration65, location56, edge58, invariant70, incomingEdges72, outgoingEdges75, parentTemplate67, source78, target81, parentTemplate84, guard87, channelExpression96, update89, synchronization92, selection94, declarations98, statement100, statement110, statement113, initialization102, condition104, iteration107, statement120, expression122, ifExpression125, expression115, statement117, returnExpression133, expression135, thenStatement127, elseStatement130, confirmedExpression139, invertedExpression141, negatedExpression137, index149, secondExpr145, firstExpr143, identifier148, scope152, identifier154, function157, argument158, expression171, ifExpression161, thenExpression163, elseExpression166, expression169, bendPoint177, channelType173, dataTypeExpression174, position176},
    generalizations={gen_uppaal_NTA_core_NamedElement, gen_uppaal_NTA_core_CommentableElement, gen_uppaal_types_ScalarTypeSpecification_TypeExpression, gen_uppaal_types_Type_NamedElement, gen_uppaal_types_PredefinedType_Type, gen_uppaal_types_DeclaredType_Type, gen_uppaal_types_TypeExpression_Expression, gen_uppaal_types_StructTypeSpecification_TypeExpression, gen_uppaal_types_RangeTypeSpecification_TypeExpression, gen_uppaal_declarations_GlobalDeclarations_Declarations, gen_uppaal_declarations_LocalDeclarations_Declarations, gen_uppaal_declarations_SystemDeclarations_Declarations, gen_uppaal_declarations_Function_core_NamedElement, gen_uppaal_declarations_Function_core_TypedElement, gen_uppaal_declarations_TypeDeclaration_Declaration, gen_uppaal_declarations_Variable_core_NamedElement, gen_uppaal_declarations_Variable_core_TypedElement, gen_uppaal_declarations_Parameter_Variable, gen_uppaal_declarations_ExpressionInitializer_Initializer, gen_uppaal_declarations_ArrayInitializer_Initializer, gen_uppaal_declarations_TypedDeclaration_declarations_Declaration, gen_uppaal_declarations_TypedDeclaration_declarations_TypedElementContainer, gen_uppaal_global_ChannelPriorityDeclaration_Declaration, gen_uppaal_declarations_ParameterContainer_TypedElementContainer, gen_uppaal_global_DefaultItem_PriorityItem, gen_uppaal_system_TemplateDeclaration_Declaration, gen_uppaal_global_ChannelItem_PriorityItem, gen_uppaal_templates_Template_AbstractTemplate, gen_uppaal_templates_AbstractTemplate_NamedElement, gen_uppaal_templates_RedefinedTemplate_AbstractTemplate, gen_uppaal_templates_Location_core_NamedElement, gen_uppaal_templates_Location_core_CommentableElement, gen_uppaal_templates_Location_visuals_PlanarElement, gen_uppaal_templates_Location_visuals_ColoredElement, gen_uppaal_templates_Edge_visuals_LinearElement, gen_uppaal_templates_Edge_core_CommentableElement, gen_uppaal_templates_Edge_visuals_ColoredElement, gen_uppaal_statements_Block_Statement, gen_uppaal_statements_EmptyStatement_Statement, gen_uppaal_statements_ForLoop_Statement, gen_uppaal_templates_Selection_TypedElementContainer, gen_uppaal_statements_Iteration_statements_Statement, gen_uppaal_statements_Iteration_declarations_TypedElementContainer, gen_uppaal_statements_WhileLoop_Statement, gen_uppaal_statements_IfStatement_Statement, gen_uppaal_statements_DoWhileLoop_Statement, gen_uppaal_statements_ReturnStatement_Statement, gen_uppaal_statements_ExpressionStatement_Statement, gen_uppaal_expressions_PlusExpression_Expression, gen_uppaal_expressions_MinusExpression_Expression, gen_uppaal_expressions_BinaryExpression_Expression, gen_uppaal_expressions_NegationExpression_Expression, gen_uppaal_expressions_AssignmentExpression_BinaryExpression, gen_uppaal_expressions_IdentifierExpression_Expression, gen_uppaal_expressions_ScopedIdentifierExpression_Expression, gen_uppaal_expressions_LiteralExpression_Expression, gen_uppaal_expressions_ArithmeticExpression_BinaryExpression, gen_uppaal_expressions_LogicalExpression_BinaryExpression, gen_uppaal_expressions_FunctionCallExpression_Expression, gen_uppaal_expressions_CompareExpression_BinaryExpression, gen_uppaal_expressions_IncrementDecrementExpression_Expression, gen_uppaal_expressions_ConditionExpression_Expression, gen_uppaal_expressions_QuantificationExpression_expressions_Expression, gen_uppaal_expressions_QuantificationExpression_declarations_TypedElementContainer, gen_uppaal_expressions_ChannelPrefixExpression_Expression, gen_uppaal_expressions_PreIncrementDecrementExpression_IncrementDecrementExpression, gen_uppaal_expressions_PostIncrementDecrementExpression_IncrementDecrementExpression, gen_uppaal_expressions_BitShiftExpression_BinaryExpression, gen_uppaal_expressions_MinMaxExpression_BinaryExpression, gen_uppaal_expressions_BitwiseExpression_BinaryExpression, gen_uppaal_expressions_DataPrefixExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)