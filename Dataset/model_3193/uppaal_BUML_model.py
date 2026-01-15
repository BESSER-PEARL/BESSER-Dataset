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
            EnumerationLiteral(name="NONE"),
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

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="IMPLY")
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

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="UNIVERSAL"),
			EnumerationLiteral(name="EXISTENTIAL")
    }
)

IncrementDecrementOperator: Enumeration = Enumeration(
    name="IncrementDecrementOperator",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
    }
)

IncrementDecrementPosition: Enumeration = Enumeration(
    name="IncrementDecrementPosition",
    literals={
            EnumerationLiteral(name="PRE"),
			EnumerationLiteral(name="POST")
    }
)

BitShiftOperator: Enumeration = Enumeration(
    name="BitShiftOperator",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

BitwiseOperator: Enumeration = Enumeration(
    name="BitwiseOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="OR")
    }
)

MinMaxOperator: Enumeration = Enumeration(
    name="MinMaxOperator",
    literals={
            EnumerationLiteral(name="MAX"),
			EnumerationLiteral(name="MIN")
    }
)

ColorKind: Enumeration = Enumeration(
    name="ColorKind",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="LIGHTGREY"),
			EnumerationLiteral(name="DARKGREY"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="SELF_DEFINED"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PINK")
    }
)

# Classes
uppaal_NTA = Class(name="uppaal::NTA")
core_NamedElement = Class(name="core::NamedElement")
core_CommentableElement = Class(name="core::CommentableElement")
Template = Class(name="Template")
SystemDeclarations = Class(name="SystemDeclarations")
PredefinedType = Class(name="PredefinedType")
GlobalDeclarations = Class(name="GlobalDeclarations")
uppaal_core_NamedElement = Class(name="uppaal::core::NamedElement", is_abstract=True)
uppaal_core_CommentableElement = Class(name="uppaal::core::CommentableElement", is_abstract=True)
uppaal_types_Type = Class(name="uppaal::types::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
Index = Class(name="Index")
uppaal_types_PredefinedType = Class(name="uppaal::types::PredefinedType")
Type = Class(name="Type")
uppaal_types_DeclaredType = Class(name="uppaal::types::DeclaredType")
TypeDefinition = Class(name="TypeDefinition")
uppaal_types_TypeDefinition = Class(name="uppaal::types::TypeDefinition", is_abstract=True)
uppaal_types_TypeReference = Class(name="uppaal::types::TypeReference")
uppaal_types_TypeSpecification = Class(name="uppaal::types::TypeSpecification", is_abstract=True)
uppaal_types_ScalarTypeSpecification = Class(name="uppaal::types::ScalarTypeSpecification")
TypeSpecification = Class(name="TypeSpecification")
TypeDeclaration = Class(name="TypeDeclaration")
Expression = Class(name="Expression")
uppaal_types_StructTypeSpecification = Class(name="uppaal::types::StructTypeSpecification")
DataVariableDeclaration = Class(name="DataVariableDeclaration")
uppaal_types_RangeTypeSpecification = Class(name="uppaal::types::RangeTypeSpecification")
IntegerBounds = Class(name="IntegerBounds")
uppaal_types_IntegerBounds = Class(name="uppaal::types::IntegerBounds")
uppaal_declarations_Declarations = Class(name="uppaal::declarations::Declarations", is_abstract=True)
Declaration = Class(name="Declaration")
uppaal_declarations_GlobalDeclarations = Class(name="uppaal::declarations::GlobalDeclarations")
Declarations = Class(name="Declarations")
global_ChannelPriority = Class(name="global::ChannelPriority")
uppaal_declarations_LocalDeclarations = Class(name="uppaal::declarations::LocalDeclarations")
uppaal_declarations_SystemDeclarations = Class(name="uppaal::declarations::SystemDeclarations")
system_System = Class(name="system::System")
system_ProgressMeasure = Class(name="system::ProgressMeasure")
uppaal_declarations_Declaration = Class(name="uppaal::declarations::Declaration", is_abstract=True)
uppaal_declarations_VariableDeclaration = Class(name="uppaal::declarations::VariableDeclaration", is_abstract=True)
declarations_Declaration = Class(name="declarations::Declaration")
declarations_VariableContainer = Class(name="declarations::VariableContainer")
uppaal_declarations_ChannelVariableDeclaration = Class(name="uppaal::declarations::ChannelVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
uppaal_declarations_ClockVariableDeclaration = Class(name="uppaal::declarations::ClockVariableDeclaration")
uppaal_declarations_DataVariableDeclaration = Class(name="uppaal::declarations::DataVariableDeclaration")
uppaal_declarations_FunctionDeclaration = Class(name="uppaal::declarations::FunctionDeclaration")
Function = Class(name="Function")
uppaal_declarations_Function = Class(name="uppaal::declarations::Function")
Block = Class(name="Block")
Parameter_ = Class(name="Parameter")
uppaal_declarations_TypeDeclaration = Class(name="uppaal::declarations::TypeDeclaration")
DeclaredType = Class(name="DeclaredType")
uppaal_declarations_Variable = Class(name="uppaal::declarations::Variable")
Initializer = Class(name="Initializer")
uppaal_declarations_Index = Class(name="uppaal::declarations::Index", is_abstract=True)
uppaal_declarations_ValueIndex = Class(name="uppaal::declarations::ValueIndex")
uppaal_declarations_TypeIndex = Class(name="uppaal::declarations::TypeIndex")
VariableContainer = Class(name="VariableContainer")
uppaal_declarations_VariableContainer = Class(name="uppaal::declarations::VariableContainer", is_abstract=True)
Variable = Class(name="Variable")
uppaal_declarations_Parameter = Class(name="uppaal::declarations::Parameter")
uppaal_declarations_Initializer = Class(name="uppaal::declarations::Initializer", is_abstract=True)
uppaal_declarations_ExpressionInitializer = Class(name="uppaal::declarations::ExpressionInitializer")
uppaal_declarations_ArrayInitializer = Class(name="uppaal::declarations::ArrayInitializer")
uppaal_global_DefaultChannelPriority = Class(name="uppaal::global::DefaultChannelPriority")
uppaal_global_ChannelPriority = Class(name="uppaal::global::ChannelPriority")
global_ChannelPriorityItem = Class(name="global::ChannelPriorityItem")
uppaal_global_ChannelPriorityItem = Class(name="uppaal::global::ChannelPriorityItem", is_abstract=True)
uppaal_global_ChannelList = Class(name="uppaal::global::ChannelList")
ChannelPriorityItem = Class(name="ChannelPriorityItem")
IdentifierExpression = Class(name="IdentifierExpression")
system_InstantiationList = Class(name="system::InstantiationList")
uppaal_system_TemplateDeclaration = Class(name="uppaal::system::TemplateDeclaration")
RedefinedTemplate = Class(name="RedefinedTemplate")
uppaal_system_System = Class(name="uppaal::system::System")
uppaal_system_InstantiationList = Class(name="uppaal::system::InstantiationList")
AbstractTemplate = Class(name="AbstractTemplate")
uppaal_system_ProgressMeasure = Class(name="uppaal::system::ProgressMeasure")
uppaal_templates_AbstractTemplate = Class(name="uppaal::templates::AbstractTemplate", is_abstract=True)
uppaal_templates_Template = Class(name="uppaal::templates::Template")
LocalDeclarations = Class(name="LocalDeclarations")
Location = Class(name="Location")
Edge = Class(name="Edge")
uppaal_templates_RedefinedTemplate = Class(name="uppaal::templates::RedefinedTemplate")
system_TemplateDeclaration = Class(name="system::TemplateDeclaration")
uppaal_templates_Location = Class(name="uppaal::templates::Location")
visuals_PlanarElement = Class(name="visuals::PlanarElement")
visuals_ColoredElement = Class(name="visuals::ColoredElement")
uppaal_templates_Edge = Class(name="uppaal::templates::Edge")
visuals_LinearElement = Class(name="visuals::LinearElement")
Synchronization = Class(name="Synchronization")
uppaal_templates_Selection = Class(name="uppaal::templates::Selection")
Selection = Class(name="Selection")
uppaal_templates_Synchronization = Class(name="uppaal::templates::Synchronization")
uppaal_statements_EmptyStatement = Class(name="uppaal::statements::EmptyStatement")
uppaal_statements_ForLoop = Class(name="uppaal::statements::ForLoop")
uppaal_statements_Statement = Class(name="uppaal::statements::Statement", is_abstract=True)
uppaal_statements_Block = Class(name="uppaal::statements::Block")
Statement = Class(name="Statement")
uppaal_statements_Iteration = Class(name="uppaal::statements::Iteration")
statements_Statement = Class(name="statements::Statement")
uppaal_statements_WhileLoop = Class(name="uppaal::statements::WhileLoop")
uppaal_statements_IfStatement = Class(name="uppaal::statements::IfStatement")
uppaal_statements_DoWhileLoop = Class(name="uppaal::statements::DoWhileLoop")
uppaal_statements_ExpressionStatement = Class(name="uppaal::statements::ExpressionStatement")
uppaal_expressions_Expression = Class(name="uppaal::expressions::Expression", is_abstract=True)
uppaal_expressions_NegationExpression = Class(name="uppaal::expressions::NegationExpression")
uppaal_statements_ReturnStatement = Class(name="uppaal::statements::ReturnStatement")
uppaal_expressions_PlusExpression = Class(name="uppaal::expressions::PlusExpression")
uppaal_expressions_MinusExpression = Class(name="uppaal::expressions::MinusExpression")
uppaal_expressions_BinaryExpression = Class(name="uppaal::expressions::BinaryExpression", is_abstract=True)
uppaal_expressions_AssignmentExpression = Class(name="uppaal::expressions::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
uppaal_expressions_LiteralExpression = Class(name="uppaal::expressions::LiteralExpression")
uppaal_expressions_IdentifierExpression = Class(name="uppaal::expressions::IdentifierExpression")
uppaal_expressions_LogicalExpression = Class(name="uppaal::expressions::LogicalExpression")
uppaal_expressions_FunctionCallExpression = Class(name="uppaal::expressions::FunctionCallExpression")
uppaal_expressions_ArithmeticExpression = Class(name="uppaal::expressions::ArithmeticExpression")
uppaal_expressions_CompareExpression = Class(name="uppaal::expressions::CompareExpression")
uppaal_expressions_ConditionExpression = Class(name="uppaal::expressions::ConditionExpression")
uppaal_expressions_ScopedIdentifierExpression = Class(name="uppaal::expressions::ScopedIdentifierExpression")
uppaal_expressions_QuantificationExpression = Class(name="uppaal::expressions::QuantificationExpression")
expressions_Expression = Class(name="expressions::Expression")
uppaal_expressions_IncrementDecrementExpression = Class(name="uppaal::expressions::IncrementDecrementExpression")
uppaal_expressions_BitShiftExpression = Class(name="uppaal::expressions::BitShiftExpression")
uppaal_expressions_MinMaxExpression = Class(name="uppaal::expressions::MinMaxExpression")
uppaal_expressions_BitwiseExpression = Class(name="uppaal::expressions::BitwiseExpression")
uppaal_visuals_ColoredElement = Class(name="uppaal::visuals::ColoredElement", is_abstract=True)
uppaal_visuals_LinearElement = Class(name="uppaal::visuals::LinearElement", is_abstract=True)
uppaal_visuals_Point = Class(name="uppaal::visuals::Point")
uppaal_visuals_PlanarElement = Class(name="uppaal::visuals::PlanarElement", is_abstract=True)
Point = Class(name="Point")

# uppaal_NTA class attributes and methods

# core_NamedElement class attributes and methods

# core_CommentableElement class attributes and methods

# Template class attributes and methods

# SystemDeclarations class attributes and methods

# PredefinedType class attributes and methods

# GlobalDeclarations class attributes and methods

# uppaal_core_NamedElement class attributes and methods
uppaal_core_NamedElement_name: Property = Property(name="name", type=StringType)
uppaal_core_NamedElement.attributes={uppaal_core_NamedElement_name}

# uppaal_core_CommentableElement class attributes and methods
uppaal_core_CommentableElement_comment: Property = Property(name="comment", type=StringType)
uppaal_core_CommentableElement.attributes={uppaal_core_CommentableElement_comment}

# uppaal_types_Type class attributes and methods
uppaal_types_Type_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_Type.attributes={uppaal_types_Type_baseType}

# NamedElement class attributes and methods

# Index class attributes and methods

# uppaal_types_PredefinedType class attributes and methods
uppaal_types_PredefinedType_type: Property = Property(name="type", type=StringType)
uppaal_types_PredefinedType.attributes={uppaal_types_PredefinedType_type}

# Type class attributes and methods

# uppaal_types_DeclaredType class attributes and methods

# TypeDefinition class attributes and methods

# uppaal_types_TypeDefinition class attributes and methods
uppaal_types_TypeDefinition_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_TypeDefinition.attributes={uppaal_types_TypeDefinition_baseType}

# uppaal_types_TypeReference class attributes and methods

# uppaal_types_TypeSpecification class attributes and methods

# uppaal_types_ScalarTypeSpecification class attributes and methods

# TypeSpecification class attributes and methods

# TypeDeclaration class attributes and methods

# Expression class attributes and methods

# uppaal_types_StructTypeSpecification class attributes and methods

# DataVariableDeclaration class attributes and methods

# uppaal_types_RangeTypeSpecification class attributes and methods

# IntegerBounds class attributes and methods

# uppaal_types_IntegerBounds class attributes and methods

# uppaal_declarations_Declarations class attributes and methods

# Declaration class attributes and methods

# uppaal_declarations_GlobalDeclarations class attributes and methods

# Declarations class attributes and methods

# global_ChannelPriority class attributes and methods

# uppaal_declarations_LocalDeclarations class attributes and methods

# uppaal_declarations_SystemDeclarations class attributes and methods

# system_System class attributes and methods

# system_ProgressMeasure class attributes and methods

# uppaal_declarations_Declaration class attributes and methods
uppaal_declarations_Declaration_exp: Property = Property(name="exp", type=StringType)
uppaal_declarations_Declaration.attributes={uppaal_declarations_Declaration_exp}

# uppaal_declarations_VariableDeclaration class attributes and methods

# declarations_Declaration class attributes and methods

# declarations_VariableContainer class attributes and methods

# uppaal_declarations_ChannelVariableDeclaration class attributes and methods
uppaal_declarations_ChannelVariableDeclaration_urgent: Property = Property(name="urgent", type=BooleanType)
uppaal_declarations_ChannelVariableDeclaration_broadcast: Property = Property(name="broadcast", type=BooleanType)
uppaal_declarations_ChannelVariableDeclaration.attributes={uppaal_declarations_ChannelVariableDeclaration_urgent, uppaal_declarations_ChannelVariableDeclaration_broadcast}

# VariableDeclaration class attributes and methods

# uppaal_declarations_ClockVariableDeclaration class attributes and methods

# uppaal_declarations_DataVariableDeclaration class attributes and methods
uppaal_declarations_DataVariableDeclaration_prefix: Property = Property(name="prefix", type=StringType)
uppaal_declarations_DataVariableDeclaration.attributes={uppaal_declarations_DataVariableDeclaration_prefix}

# uppaal_declarations_FunctionDeclaration class attributes and methods

# Function class attributes and methods

# uppaal_declarations_Function class attributes and methods

# Block class attributes and methods

# Parameter class attributes and methods

# uppaal_declarations_TypeDeclaration class attributes and methods

# DeclaredType class attributes and methods

# uppaal_declarations_Variable class attributes and methods

# Initializer class attributes and methods

# uppaal_declarations_Index class attributes and methods

# uppaal_declarations_ValueIndex class attributes and methods

# uppaal_declarations_TypeIndex class attributes and methods

# VariableContainer class attributes and methods

# uppaal_declarations_VariableContainer class attributes and methods

# Variable class attributes and methods

# uppaal_declarations_Parameter class attributes and methods
uppaal_declarations_Parameter_callType: Property = Property(name="callType", type=StringType)
uppaal_declarations_Parameter.attributes={uppaal_declarations_Parameter_callType}

# uppaal_declarations_Initializer class attributes and methods

# uppaal_declarations_ExpressionInitializer class attributes and methods

# uppaal_declarations_ArrayInitializer class attributes and methods

# uppaal_global_DefaultChannelPriority class attributes and methods

# uppaal_global_ChannelPriority class attributes and methods

# global_ChannelPriorityItem class attributes and methods

# uppaal_global_ChannelPriorityItem class attributes and methods

# uppaal_global_ChannelList class attributes and methods

# ChannelPriorityItem class attributes and methods

# IdentifierExpression class attributes and methods

# system_InstantiationList class attributes and methods

# uppaal_system_TemplateDeclaration class attributes and methods

# RedefinedTemplate class attributes and methods

# uppaal_system_System class attributes and methods

# uppaal_system_InstantiationList class attributes and methods

# AbstractTemplate class attributes and methods

# uppaal_system_ProgressMeasure class attributes and methods

# uppaal_templates_AbstractTemplate class attributes and methods

# uppaal_templates_Template class attributes and methods

# LocalDeclarations class attributes and methods

# Location class attributes and methods

# Edge class attributes and methods

# uppaal_templates_RedefinedTemplate class attributes and methods

# system_TemplateDeclaration class attributes and methods

# uppaal_templates_Location class attributes and methods
uppaal_templates_Location_locationTimeKind: Property = Property(name="locationTimeKind", type=StringType)
uppaal_templates_Location.attributes={uppaal_templates_Location_locationTimeKind}

# visuals_PlanarElement class attributes and methods

# visuals_ColoredElement class attributes and methods

# uppaal_templates_Edge class attributes and methods

# visuals_LinearElement class attributes and methods

# Synchronization class attributes and methods

# uppaal_templates_Selection class attributes and methods

# Selection class attributes and methods

# uppaal_templates_Synchronization class attributes and methods
uppaal_templates_Synchronization_kind: Property = Property(name="kind", type=StringType)
uppaal_templates_Synchronization.attributes={uppaal_templates_Synchronization_kind}

# uppaal_statements_EmptyStatement class attributes and methods

# uppaal_statements_ForLoop class attributes and methods

# uppaal_statements_Statement class attributes and methods

# uppaal_statements_Block class attributes and methods

# Statement class attributes and methods

# uppaal_statements_Iteration class attributes and methods

# statements_Statement class attributes and methods

# uppaal_statements_WhileLoop class attributes and methods

# uppaal_statements_IfStatement class attributes and methods

# uppaal_statements_DoWhileLoop class attributes and methods

# uppaal_statements_ExpressionStatement class attributes and methods

# uppaal_expressions_Expression class attributes and methods
uppaal_expressions_Expression_exp: Property = Property(name="exp", type=StringType)
uppaal_expressions_Expression.attributes={uppaal_expressions_Expression_exp}

# uppaal_expressions_NegationExpression class attributes and methods

# uppaal_statements_ReturnStatement class attributes and methods

# uppaal_expressions_PlusExpression class attributes and methods

# uppaal_expressions_MinusExpression class attributes and methods

# uppaal_expressions_BinaryExpression class attributes and methods

# uppaal_expressions_AssignmentExpression class attributes and methods
uppaal_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_AssignmentExpression.attributes={uppaal_expressions_AssignmentExpression_operator}

# BinaryExpression class attributes and methods

# uppaal_expressions_LiteralExpression class attributes and methods
uppaal_expressions_LiteralExpression_text: Property = Property(name="text", type=StringType)
uppaal_expressions_LiteralExpression.attributes={uppaal_expressions_LiteralExpression_text}

# uppaal_expressions_IdentifierExpression class attributes and methods

# uppaal_expressions_LogicalExpression class attributes and methods
uppaal_expressions_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_LogicalExpression.attributes={uppaal_expressions_LogicalExpression_operator}

# uppaal_expressions_FunctionCallExpression class attributes and methods

# uppaal_expressions_ArithmeticExpression class attributes and methods
uppaal_expressions_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_ArithmeticExpression.attributes={uppaal_expressions_ArithmeticExpression_operator}

# uppaal_expressions_CompareExpression class attributes and methods
uppaal_expressions_CompareExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_CompareExpression.attributes={uppaal_expressions_CompareExpression_operator}

# uppaal_expressions_ConditionExpression class attributes and methods

# uppaal_expressions_ScopedIdentifierExpression class attributes and methods

# uppaal_expressions_QuantificationExpression class attributes and methods
uppaal_expressions_QuantificationExpression_quantifier: Property = Property(name="quantifier", type=StringType)
uppaal_expressions_QuantificationExpression.attributes={uppaal_expressions_QuantificationExpression_quantifier}

# expressions_Expression class attributes and methods

# uppaal_expressions_IncrementDecrementExpression class attributes and methods
uppaal_expressions_IncrementDecrementExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_IncrementDecrementExpression_position: Property = Property(name="position", type=StringType)
uppaal_expressions_IncrementDecrementExpression.attributes={uppaal_expressions_IncrementDecrementExpression_operator, uppaal_expressions_IncrementDecrementExpression_position}

# uppaal_expressions_BitShiftExpression class attributes and methods
uppaal_expressions_BitShiftExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitShiftExpression.attributes={uppaal_expressions_BitShiftExpression_operator}

# uppaal_expressions_MinMaxExpression class attributes and methods
uppaal_expressions_MinMaxExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_MinMaxExpression.attributes={uppaal_expressions_MinMaxExpression_operator}

# uppaal_expressions_BitwiseExpression class attributes and methods
uppaal_expressions_BitwiseExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitwiseExpression.attributes={uppaal_expressions_BitwiseExpression_operator}

# uppaal_visuals_ColoredElement class attributes and methods
uppaal_visuals_ColoredElement_color: Property = Property(name="color", type=StringType)
uppaal_visuals_ColoredElement_colorCode: Property = Property(name="colorCode", type=StringType)
uppaal_visuals_ColoredElement.attributes={uppaal_visuals_ColoredElement_color, uppaal_visuals_ColoredElement_colorCode}

# uppaal_visuals_LinearElement class attributes and methods

# uppaal_visuals_Point class attributes and methods
uppaal_visuals_Point_x: Property = Property(name="x", type=IntegerType)
uppaal_visuals_Point_y: Property = Property(name="y", type=IntegerType)
uppaal_visuals_Point.attributes={uppaal_visuals_Point_x, uppaal_visuals_Point_y}

# uppaal_visuals_PlanarElement class attributes and methods

# Point class attributes and methods

# Relationships
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
int5: BinaryAssociation = BinaryAssociation(
    name="int5",
    ends={
        Property(name="PredefinedType", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA6", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bool7: BinaryAssociation = BinaryAssociation(
    name="bool7",
    ends={
        Property(name="PredefinedType9", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA8", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
globalDeclarations0: BinaryAssociation = BinaryAssociation(
    name="globalDeclarations0",
    ends={
        Property(name="GlobalDeclarations", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA", type=GlobalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chan13: BinaryAssociation = BinaryAssociation(
    name="chan13",
    ends={
        Property(name="PredefinedType15", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA14", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
void16: BinaryAssociation = BinaryAssociation(
    name="void16",
    ends={
        Property(name="PredefinedType18", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA17", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
clock10: BinaryAssociation = BinaryAssociation(
    name="clock10",
    ends={
        Property(name="PredefinedType12", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA11", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index19: BinaryAssociation = BinaryAssociation(
    name="index19",
    ends={
        Property(name="Index", type=uppaal_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Type", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclaration20: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration20",
    ends={
        Property(name="declarations", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeDeclaration", type=TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition21: BinaryAssociation = BinaryAssociation(
    name="typeDefinition21",
    ends={
        Property(name="TypeDefinition", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_DeclaredType", type=TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
referredType22: BinaryAssociation = BinaryAssociation(
    name="referredType22",
    ends={
        Property(name="Type", type=uppaal_types_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_TypeReference", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
sizeExpression23: BinaryAssociation = BinaryAssociation(
    name="sizeExpression23",
    ends={
        Property(name="Expression", type=uppaal_types_ScalarTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_ScalarTypeSpecification", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration24: BinaryAssociation = BinaryAssociation(
    name="declaration24",
    ends={
        Property(name="DataVariableDeclaration", type=uppaal_types_StructTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_StructTypeSpecification", type=DataVariableDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bounds25: BinaryAssociation = BinaryAssociation(
    name="bounds25",
    ends={
        Property(name="IntegerBounds", type=uppaal_types_RangeTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_RangeTypeSpecification", type=IntegerBounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound26: BinaryAssociation = BinaryAssociation(
    name="lowerBound26",
    ends={
        Property(name="Expression27", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound28: BinaryAssociation = BinaryAssociation(
    name="upperBound28",
    ends={
        Property(name="Expression30", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds29", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration31: BinaryAssociation = BinaryAssociation(
    name="declaration31",
    ends={
        Property(name="Declaration", type=uppaal_declarations_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Declarations", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelPriority32: BinaryAssociation = BinaryAssociation(
    name="channelPriority32",
    ends={
        Property(name="global_ChannelPriority", type=uppaal_declarations_GlobalDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_GlobalDeclarations", type=global_ChannelPriority, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system33: BinaryAssociation = BinaryAssociation(
    name="system33",
    ends={
        Property(name="system_System", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations", type=system_System, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
progressMeasure34: BinaryAssociation = BinaryAssociation(
    name="progressMeasure34",
    ends={
        Property(name="system_ProgressMeasure", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations35", type=system_ProgressMeasure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function36: BinaryAssociation = BinaryAssociation(
    name="function36",
    ends={
        Property(name="Function", type=uppaal_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_FunctionDeclaration", type=Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType37: BinaryAssociation = BinaryAssociation(
    name="returnType37",
    ends={
        Property(name="TypeDefinition38", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block39: BinaryAssociation = BinaryAssociation(
    name="block39",
    ends={
        Property(name="Block", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function40", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="types", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclaredType", type=DeclaredType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition44: BinaryAssociation = BinaryAssociation(
    name="typeDefinition44",
    ends={
        Property(name="TypeDefinition45", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeDeclaration", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index46: BinaryAssociation = BinaryAssociation(
    name="index46",
    ends={
        Property(name="Index47", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter41: BinaryAssociation = BinaryAssociation(
    name="parameter41",
    ends={
        Property(name="Parameter", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function42", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container48: BinaryAssociation = BinaryAssociation(
    name="container48",
    ends={
        Property(name="declarations49", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableContainer", type=VariableContainer, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition50: BinaryAssociation = BinaryAssociation(
    name="typeDefinition50",
    ends={
        Property(name="TypeDefinition52", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable51", type=TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
initializer53: BinaryAssociation = BinaryAssociation(
    name="initializer53",
    ends={
        Property(name="Initializer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable54", type=Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeExpression55: BinaryAssociation = BinaryAssociation(
    name="sizeExpression55",
    ends={
        Property(name="Expression56", type=uppaal_declarations_ValueIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ValueIndex", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDefinition57: BinaryAssociation = BinaryAssociation(
    name="typeDefinition57",
    ends={
        Property(name="TypeDefinition58", type=uppaal_declarations_TypeIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeIndex", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDefinition59: BinaryAssociation = BinaryAssociation(
    name="typeDefinition59",
    ends={
        Property(name="TypeDefinition60", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_VariableContainer", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable61: BinaryAssociation = BinaryAssociation(
    name="variable61",
    ends={
        Property(name="declarations62", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableDeclaration63: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration63",
    ends={
        Property(name="VariableDeclaration", type=uppaal_declarations_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Parameter", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression64: BinaryAssociation = BinaryAssociation(
    name="expression64",
    ends={
        Property(name="Expression65", type=uppaal_declarations_ExpressionInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ExpressionInitializer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer66: BinaryAssociation = BinaryAssociation(
    name="initializer66",
    ends={
        Property(name="Initializer67", type=uppaal_declarations_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ArrayInitializer", type=Initializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
item68: BinaryAssociation = BinaryAssociation(
    name="item68",
    ends={
        Property(name="global_ChannelPriorityItem", type=uppaal_global_ChannelPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriority", type=global_ChannelPriorityItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
channelExpression69: BinaryAssociation = BinaryAssociation(
    name="channelExpression69",
    ends={
        Property(name="IdentifierExpression", type=uppaal_global_ChannelList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelList", type=IdentifierExpression, multiplicity=Multiplicity(1, 9999))
    }
)
declaredTemplate70: BinaryAssociation = BinaryAssociation(
    name="declaredTemplate70",
    ends={
        Property(name="templates", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="RedefinedTemplate", type=RedefinedTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument71: BinaryAssociation = BinaryAssociation(
    name="argument71",
    ends={
        Property(name="Expression72", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_TemplateDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiationList73: BinaryAssociation = BinaryAssociation(
    name="instantiationList73",
    ends={
        Property(name="system_InstantiationList", type=uppaal_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_System", type=system_InstantiationList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template74: BinaryAssociation = BinaryAssociation(
    name="template74",
    ends={
        Property(name="AbstractTemplate", type=uppaal_system_InstantiationList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_InstantiationList", type=AbstractTemplate, multiplicity=Multiplicity(1, 9999))
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="Expression76", type=uppaal_system_ProgressMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_ProgressMeasure", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter77: BinaryAssociation = BinaryAssociation(
    name="parameter77",
    ends={
        Property(name="Parameter78", type=uppaal_templates_AbstractTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_AbstractTemplate", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations79: BinaryAssociation = BinaryAssociation(
    name="declarations79",
    ends={
        Property(name="LocalDeclarations", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location80: BinaryAssociation = BinaryAssociation(
    name="location80",
    ends={
        Property(name="templates81", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Location", type=Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edge82: BinaryAssociation = BinaryAssociation(
    name="edge82",
    ends={
        Property(name="templates83", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Edge", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentTemplate91: BinaryAssociation = BinaryAssociation(
    name="parentTemplate91",
    ends={
        Property(name="Template92", type=Template, multiplicity=Multiplicity(1, 1)),
        Property(name="templates93", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1))
    }
)
init84: BinaryAssociation = BinaryAssociation(
    name="init84",
    ends={
        Property(name="Location86", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template85", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
referredTemplate87: BinaryAssociation = BinaryAssociation(
    name="referredTemplate87",
    ends={
        Property(name="AbstractTemplate88", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_RedefinedTemplate", type=AbstractTemplate, multiplicity=Multiplicity(1, 1))
    }
)
declaration89: BinaryAssociation = BinaryAssociation(
    name="declaration89",
    ends={
        Property(name="declarations90", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=system_TemplateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
invariant94: BinaryAssociation = BinaryAssociation(
    name="invariant94",
    ends={
        Property(name="Expression95", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Location", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target98: BinaryAssociation = BinaryAssociation(
    name="target98",
    ends={
        Property(name="Location100", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge99", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate101: BinaryAssociation = BinaryAssociation(
    name="parentTemplate101",
    ends={
        Property(name="templates103", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Template102", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
guard104: BinaryAssociation = BinaryAssociation(
    name="guard104",
    ends={
        Property(name="Expression106", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge105", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
update107: BinaryAssociation = BinaryAssociation(
    name="update107",
    ends={
        Property(name="Expression109", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge108", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization110: BinaryAssociation = BinaryAssociation(
    name="synchronization110",
    ends={
        Property(name="Synchronization", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge111", type=Synchronization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source96: BinaryAssociation = BinaryAssociation(
    name="source96",
    ends={
        Property(name="Location97", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
channelExpression114: BinaryAssociation = BinaryAssociation(
    name="channelExpression114",
    ends={
        Property(name="IdentifierExpression115", type=uppaal_templates_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Synchronization", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selection112: BinaryAssociation = BinaryAssociation(
    name="selection112",
    ends={
        Property(name="Selection", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge113", type=Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations116: BinaryAssociation = BinaryAssociation(
    name="declarations116",
    ends={
        Property(name="LocalDeclarations117", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement118: BinaryAssociation = BinaryAssociation(
    name="statement118",
    ends={
        Property(name="Statement", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block119", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialization120: BinaryAssociation = BinaryAssociation(
    name="initialization120",
    ends={
        Property(name="Expression121", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition122: BinaryAssociation = BinaryAssociation(
    name="condition122",
    ends={
        Property(name="Expression124", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop123", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement128: BinaryAssociation = BinaryAssociation(
    name="statement128",
    ends={
        Property(name="Statement130", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop129", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement131: BinaryAssociation = BinaryAssociation(
    name="statement131",
    ends={
        Property(name="Statement132", type=uppaal_statements_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Iteration", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression133: BinaryAssociation = BinaryAssociation(
    name="expression133",
    ends={
        Property(name="Expression134", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteration125: BinaryAssociation = BinaryAssociation(
    name="iteration125",
    ends={
        Property(name="Expression127", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop126", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement138: BinaryAssociation = BinaryAssociation(
    name="statement138",
    ends={
        Property(name="Statement139", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression140: BinaryAssociation = BinaryAssociation(
    name="expression140",
    ends={
        Property(name="Expression142", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop141", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression143: BinaryAssociation = BinaryAssociation(
    name="ifExpression143",
    ends={
        Property(name="Expression144", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement145: BinaryAssociation = BinaryAssociation(
    name="thenStatement145",
    ends={
        Property(name="Statement147", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement146", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement135: BinaryAssociation = BinaryAssociation(
    name="statement135",
    ends={
        Property(name="Statement137", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop136", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnExpression151: BinaryAssociation = BinaryAssociation(
    name="returnExpression151",
    ends={
        Property(name="Expression152", type=uppaal_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression153: BinaryAssociation = BinaryAssociation(
    name="expression153",
    ends={
        Property(name="Expression154", type=uppaal_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement148: BinaryAssociation = BinaryAssociation(
    name="elseStatement148",
    ends={
        Property(name="Statement150", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement149", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
confirmedExpression157: BinaryAssociation = BinaryAssociation(
    name="confirmedExpression157",
    ends={
        Property(name="Expression158", type=uppaal_expressions_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_PlusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invertedExpression159: BinaryAssociation = BinaryAssociation(
    name="invertedExpression159",
    ends={
        Property(name="Expression160", type=uppaal_expressions_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_MinusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negatedExpression155: BinaryAssociation = BinaryAssociation(
    name="negatedExpression155",
    ends={
        Property(name="Expression156", type=uppaal_expressions_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_NegationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
secondExpr163: BinaryAssociation = BinaryAssociation(
    name="secondExpr163",
    ends={
        Property(name="Expression165", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression164", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstExpr161: BinaryAssociation = BinaryAssociation(
    name="firstExpr161",
    ends={
        Property(name="Expression162", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier166: BinaryAssociation = BinaryAssociation(
    name="identifier166",
    ends={
        Property(name="NamedElement", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
index167: BinaryAssociation = BinaryAssociation(
    name="index167",
    ends={
        Property(name="Expression169", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression168", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function170: BinaryAssociation = BinaryAssociation(
    name="function170",
    ends={
        Property(name="Function171", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
ifExpression175: BinaryAssociation = BinaryAssociation(
    name="ifExpression175",
    ends={
        Property(name="Expression176", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument172: BinaryAssociation = BinaryAssociation(
    name="argument172",
    ends={
        Property(name="Expression174", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression173", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression180: BinaryAssociation = BinaryAssociation(
    name="elseExpression180",
    ends={
        Property(name="Expression182", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression181", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scope183: BinaryAssociation = BinaryAssociation(
    name="scope183",
    ends={
        Property(name="Expression184", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier185: BinaryAssociation = BinaryAssociation(
    name="identifier185",
    ends={
        Property(name="IdentifierExpression187", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression186", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression177: BinaryAssociation = BinaryAssociation(
    name="thenExpression177",
    ends={
        Property(name="Expression179", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression178", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression188: BinaryAssociation = BinaryAssociation(
    name="expression188",
    ends={
        Property(name="Expression189", type=uppaal_expressions_QuantificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_QuantificationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression190: BinaryAssociation = BinaryAssociation(
    name="expression190",
    ends={
        Property(name="Expression191", type=uppaal_expressions_IncrementDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IncrementDecrementExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bendPoint193: BinaryAssociation = BinaryAssociation(
    name="bendPoint193",
    ends={
        Property(name="Point194", type=uppaal_visuals_LinearElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_LinearElement", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position192: BinaryAssociation = BinaryAssociation(
    name="position192",
    ends={
        Property(name="Point", type=uppaal_visuals_PlanarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_PlanarElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_uppaal_NTA_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_NTA)
gen_uppaal_NTA_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_NTA)
gen_uppaal_types_Type_NamedElement = Generalization(general=NamedElement, specific=uppaal_types_Type)
gen_uppaal_types_PredefinedType_Type = Generalization(general=Type, specific=uppaal_types_PredefinedType)
gen_uppaal_types_DeclaredType_Type = Generalization(general=Type, specific=uppaal_types_DeclaredType)
gen_uppaal_types_TypeReference_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeReference)
gen_uppaal_types_TypeSpecification_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeSpecification)
gen_uppaal_types_ScalarTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_ScalarTypeSpecification)
gen_uppaal_types_StructTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_StructTypeSpecification)
gen_uppaal_types_RangeTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_RangeTypeSpecification)
gen_uppaal_declarations_GlobalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_GlobalDeclarations)
gen_uppaal_declarations_LocalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_LocalDeclarations)
gen_uppaal_declarations_SystemDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_SystemDeclarations)
gen_uppaal_declarations_VariableDeclaration_declarations_Declaration = Generalization(general=declarations_Declaration, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ChannelVariableDeclaration)
gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ClockVariableDeclaration)
gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_DataVariableDeclaration)
gen_uppaal_declarations_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_FunctionDeclaration)
gen_uppaal_declarations_Function_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_TypeDeclaration)
gen_uppaal_declarations_Variable_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_ValueIndex_Index = Generalization(general=Index, specific=uppaal_declarations_ValueIndex)
gen_uppaal_declarations_TypeIndex_Index = Generalization(general=Index, specific=uppaal_declarations_TypeIndex)
gen_uppaal_declarations_ExpressionInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ExpressionInitializer)
gen_uppaal_declarations_ArrayInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ArrayInitializer)
gen_uppaal_global_DefaultChannelPriority_ChannelPriorityItem = Generalization(general=ChannelPriorityItem, specific=uppaal_global_DefaultChannelPriority)
gen_uppaal_global_ChannelList_ChannelPriorityItem = Generalization(general=ChannelPriorityItem, specific=uppaal_global_ChannelList)
gen_uppaal_system_TemplateDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_system_TemplateDeclaration)
gen_uppaal_templates_AbstractTemplate_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_AbstractTemplate_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_Template_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_Template)
gen_uppaal_templates_RedefinedTemplate_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_RedefinedTemplate)
gen_uppaal_templates_Location_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_PlanarElement = Generalization(general=visuals_PlanarElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Edge_visuals_LinearElement = Generalization(general=visuals_LinearElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Selection_VariableContainer = Generalization(general=VariableContainer, specific=uppaal_templates_Selection)
gen_uppaal_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_EmptyStatement)
gen_uppaal_statements_ForLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_ForLoop)
gen_uppaal_statements_Block_Statement = Generalization(general=Statement, specific=uppaal_statements_Block)
gen_uppaal_statements_Iteration_statements_Statement = Generalization(general=statements_Statement, specific=uppaal_statements_Iteration)
gen_uppaal_statements_Iteration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_statements_Iteration)
gen_uppaal_statements_WhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_WhileLoop)
gen_uppaal_statements_IfStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_IfStatement)
gen_uppaal_statements_DoWhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_DoWhileLoop)
gen_uppaal_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ExpressionStatement)
gen_uppaal_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ReturnStatement)
gen_uppaal_expressions_PlusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_PlusExpression)
gen_uppaal_expressions_MinusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_MinusExpression)
gen_uppaal_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_BinaryExpression)
gen_uppaal_expressions_NegationExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_NegationExpression)
gen_uppaal_expressions_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_AssignmentExpression)
gen_uppaal_expressions_LiteralExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_LiteralExpression)
gen_uppaal_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IdentifierExpression)
gen_uppaal_expressions_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_LogicalExpression)
gen_uppaal_expressions_FunctionCallExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_FunctionCallExpression)
gen_uppaal_expressions_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_ArithmeticExpression)
gen_uppaal_expressions_CompareExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_CompareExpression)
gen_uppaal_expressions_ConditionExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ConditionExpression)
gen_uppaal_expressions_ScopedIdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ScopedIdentifierExpression)
gen_uppaal_expressions_QuantificationExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_IncrementDecrementExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IncrementDecrementExpression)
gen_uppaal_expressions_BitShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitShiftExpression)
gen_uppaal_expressions_MinMaxExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_MinMaxExpression)
gen_uppaal_expressions_BitwiseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitwiseExpression)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={uppaal_NTA, core_NamedElement, core_CommentableElement, Template, SystemDeclarations, PredefinedType, GlobalDeclarations, uppaal_core_NamedElement, uppaal_core_CommentableElement, uppaal_types_Type, NamedElement, Index, uppaal_types_PredefinedType, Type, uppaal_types_DeclaredType, TypeDefinition, uppaal_types_TypeDefinition, uppaal_types_TypeReference, uppaal_types_TypeSpecification, uppaal_types_ScalarTypeSpecification, TypeSpecification, TypeDeclaration, Expression, uppaal_types_StructTypeSpecification, DataVariableDeclaration, uppaal_types_RangeTypeSpecification, IntegerBounds, uppaal_types_IntegerBounds, uppaal_declarations_Declarations, Declaration, uppaal_declarations_GlobalDeclarations, Declarations, global_ChannelPriority, uppaal_declarations_LocalDeclarations, uppaal_declarations_SystemDeclarations, system_System, system_ProgressMeasure, uppaal_declarations_Declaration, uppaal_declarations_VariableDeclaration, declarations_Declaration, declarations_VariableContainer, uppaal_declarations_ChannelVariableDeclaration, VariableDeclaration, uppaal_declarations_ClockVariableDeclaration, uppaal_declarations_DataVariableDeclaration, uppaal_declarations_FunctionDeclaration, Function, uppaal_declarations_Function, Block, Parameter_, uppaal_declarations_TypeDeclaration, DeclaredType, uppaal_declarations_Variable, Initializer, uppaal_declarations_Index, uppaal_declarations_ValueIndex, uppaal_declarations_TypeIndex, VariableContainer, uppaal_declarations_VariableContainer, Variable, uppaal_declarations_Parameter, uppaal_declarations_Initializer, uppaal_declarations_ExpressionInitializer, uppaal_declarations_ArrayInitializer, uppaal_global_DefaultChannelPriority, uppaal_global_ChannelPriority, global_ChannelPriorityItem, uppaal_global_ChannelPriorityItem, uppaal_global_ChannelList, ChannelPriorityItem, IdentifierExpression, system_InstantiationList, uppaal_system_TemplateDeclaration, RedefinedTemplate, uppaal_system_System, uppaal_system_InstantiationList, AbstractTemplate, uppaal_system_ProgressMeasure, uppaal_templates_AbstractTemplate, uppaal_templates_Template, LocalDeclarations, Location, Edge, uppaal_templates_RedefinedTemplate, system_TemplateDeclaration, uppaal_templates_Location, visuals_PlanarElement, visuals_ColoredElement, uppaal_templates_Edge, visuals_LinearElement, Synchronization, uppaal_templates_Selection, Selection, uppaal_templates_Synchronization, uppaal_statements_EmptyStatement, uppaal_statements_ForLoop, uppaal_statements_Statement, uppaal_statements_Block, Statement, uppaal_statements_Iteration, statements_Statement, uppaal_statements_WhileLoop, uppaal_statements_IfStatement, uppaal_statements_DoWhileLoop, uppaal_statements_ExpressionStatement, uppaal_expressions_Expression, uppaal_expressions_NegationExpression, uppaal_statements_ReturnStatement, uppaal_expressions_PlusExpression, uppaal_expressions_MinusExpression, uppaal_expressions_BinaryExpression, uppaal_expressions_AssignmentExpression, BinaryExpression, uppaal_expressions_LiteralExpression, uppaal_expressions_IdentifierExpression, uppaal_expressions_LogicalExpression, uppaal_expressions_FunctionCallExpression, uppaal_expressions_ArithmeticExpression, uppaal_expressions_CompareExpression, uppaal_expressions_ConditionExpression, uppaal_expressions_ScopedIdentifierExpression, uppaal_expressions_QuantificationExpression, expressions_Expression, uppaal_expressions_IncrementDecrementExpression, uppaal_expressions_BitShiftExpression, uppaal_expressions_MinMaxExpression, uppaal_expressions_BitwiseExpression, uppaal_visuals_ColoredElement, uppaal_visuals_LinearElement, uppaal_visuals_Point, uppaal_visuals_PlanarElement, Point, BuiltInType, DataVariablePrefix, CallType, LocationKind, SynchronizationKind, AssignmentOperator, LogicalOperator, ArithmeticOperator, CompareOperator, Quantifier, IncrementDecrementOperator, IncrementDecrementPosition, BitShiftOperator, BitwiseOperator, MinMaxOperator, ColorKind},
    associations={template1, systemDeclarations3, int5, bool7, globalDeclarations0, chan13, void16, clock10, index19, typeDeclaration20, typeDefinition21, referredType22, sizeExpression23, declaration24, bounds25, lowerBound26, upperBound28, declaration31, channelPriority32, system33, progressMeasure34, function36, returnType37, block39, type43, typeDefinition44, index46, parameter41, container48, typeDefinition50, initializer53, sizeExpression55, typeDefinition57, typeDefinition59, variable61, variableDeclaration63, expression64, initializer66, item68, channelExpression69, declaredTemplate70, argument71, instantiationList73, template74, expression75, parameter77, declarations79, location80, edge82, parentTemplate91, init84, referredTemplate87, declaration89, invariant94, target98, parentTemplate101, guard104, update107, synchronization110, source96, channelExpression114, selection112, declarations116, statement118, initialization120, condition122, statement128, statement131, expression133, iteration125, statement138, expression140, ifExpression143, thenStatement145, statement135, returnExpression151, expression153, elseStatement148, confirmedExpression157, invertedExpression159, negatedExpression155, secondExpr163, firstExpr161, identifier166, index167, function170, ifExpression175, argument172, elseExpression180, scope183, identifier185, thenExpression177, expression188, expression190, bendPoint193, position192},
    generalizations={gen_uppaal_NTA_core_NamedElement, gen_uppaal_NTA_core_CommentableElement, gen_uppaal_types_Type_NamedElement, gen_uppaal_types_PredefinedType_Type, gen_uppaal_types_DeclaredType_Type, gen_uppaal_types_TypeReference_TypeDefinition, gen_uppaal_types_TypeSpecification_TypeDefinition, gen_uppaal_types_ScalarTypeSpecification_TypeSpecification, gen_uppaal_types_StructTypeSpecification_TypeSpecification, gen_uppaal_types_RangeTypeSpecification_TypeSpecification, gen_uppaal_declarations_GlobalDeclarations_Declarations, gen_uppaal_declarations_LocalDeclarations_Declarations, gen_uppaal_declarations_SystemDeclarations_Declarations, gen_uppaal_declarations_VariableDeclaration_declarations_Declaration, gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer, gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_FunctionDeclaration_Declaration, gen_uppaal_declarations_Function_NamedElement, gen_uppaal_declarations_TypeDeclaration_Declaration, gen_uppaal_declarations_Variable_NamedElement, gen_uppaal_declarations_ValueIndex_Index, gen_uppaal_declarations_TypeIndex_Index, gen_uppaal_declarations_ExpressionInitializer_Initializer, gen_uppaal_declarations_ArrayInitializer_Initializer, gen_uppaal_global_DefaultChannelPriority_ChannelPriorityItem, gen_uppaal_global_ChannelList_ChannelPriorityItem, gen_uppaal_system_TemplateDeclaration_Declaration, gen_uppaal_templates_AbstractTemplate_core_NamedElement, gen_uppaal_templates_AbstractTemplate_core_CommentableElement, gen_uppaal_templates_Template_AbstractTemplate, gen_uppaal_templates_RedefinedTemplate_AbstractTemplate, gen_uppaal_templates_Location_core_NamedElement, gen_uppaal_templates_Location_core_CommentableElement, gen_uppaal_templates_Location_visuals_PlanarElement, gen_uppaal_templates_Location_visuals_ColoredElement, gen_uppaal_templates_Edge_visuals_LinearElement, gen_uppaal_templates_Edge_core_CommentableElement, gen_uppaal_templates_Edge_visuals_ColoredElement, gen_uppaal_templates_Selection_VariableContainer, gen_uppaal_statements_EmptyStatement_Statement, gen_uppaal_statements_ForLoop_Statement, gen_uppaal_statements_Block_Statement, gen_uppaal_statements_Iteration_statements_Statement, gen_uppaal_statements_Iteration_declarations_VariableContainer, gen_uppaal_statements_WhileLoop_Statement, gen_uppaal_statements_IfStatement_Statement, gen_uppaal_statements_DoWhileLoop_Statement, gen_uppaal_statements_ExpressionStatement_Statement, gen_uppaal_statements_ReturnStatement_Statement, gen_uppaal_expressions_PlusExpression_Expression, gen_uppaal_expressions_MinusExpression_Expression, gen_uppaal_expressions_BinaryExpression_Expression, gen_uppaal_expressions_NegationExpression_Expression, gen_uppaal_expressions_AssignmentExpression_BinaryExpression, gen_uppaal_expressions_LiteralExpression_Expression, gen_uppaal_expressions_IdentifierExpression_Expression, gen_uppaal_expressions_LogicalExpression_BinaryExpression, gen_uppaal_expressions_FunctionCallExpression_Expression, gen_uppaal_expressions_ArithmeticExpression_BinaryExpression, gen_uppaal_expressions_CompareExpression_BinaryExpression, gen_uppaal_expressions_ConditionExpression_Expression, gen_uppaal_expressions_ScopedIdentifierExpression_Expression, gen_uppaal_expressions_QuantificationExpression_expressions_Expression, gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer, gen_uppaal_expressions_IncrementDecrementExpression_Expression, gen_uppaal_expressions_BitShiftExpression_BinaryExpression, gen_uppaal_expressions_MinMaxExpression_BinaryExpression, gen_uppaal_expressions_BitwiseExpression_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)