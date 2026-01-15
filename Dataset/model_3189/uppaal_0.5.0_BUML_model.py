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

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="IMPLY")
    }
)

CompareOperator: Enumeration = Enumeration(
    name="CompareOperator",
    literals={
            EnumerationLiteral(name="UNEQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="GREATER_OR_EQUAL"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LESS_OR_EQUAL")
    }
)

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="UNIVERSAL"),
			EnumerationLiteral(name="EXISTENTIAL")
    }
)

MinMaxOperator: Enumeration = Enumeration(
    name="MinMaxOperator",
    literals={
            EnumerationLiteral(name="MIN"),
			EnumerationLiteral(name="MAX")
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

ColorKind: Enumeration = Enumeration(
    name="ColorKind",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="LIGHTGREY"),
			EnumerationLiteral(name="DARKGREY"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PINK"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="SELF_DEFINED")
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

# Classes
uppaal_NTA = Class(name="uppaal::NTA")
core_NamedElement = Class(name="core::NamedElement")
core_CommentableElement = Class(name="core::CommentableElement")
GlobalDeclarations = Class(name="GlobalDeclarations")
uppaal_core_CommentableElement = Class(name="uppaal::core::CommentableElement", is_abstract=True)
Template = Class(name="Template")
SystemDeclarations = Class(name="SystemDeclarations")
PredefinedType = Class(name="PredefinedType")
uppaal_core_NamedElement = Class(name="uppaal::core::NamedElement", is_abstract=True)
TypeDeclaration = Class(name="TypeDeclaration")
uppaal_types_Type = Class(name="uppaal::types::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
Index = Class(name="Index")
TypeSpecification = Class(name="TypeSpecification")
uppaal_types_PredefinedType = Class(name="uppaal::types::PredefinedType")
Type = Class(name="Type")
uppaal_types_DeclaredType = Class(name="uppaal::types::DeclaredType")
uppaal_types_RangeTypeSpecification = Class(name="uppaal::types::RangeTypeSpecification")
IntegerBounds = Class(name="IntegerBounds")
TypeDefinition = Class(name="TypeDefinition")
uppaal_types_TypeDefinition = Class(name="uppaal::types::TypeDefinition", is_abstract=True)
uppaal_types_TypeReference = Class(name="uppaal::types::TypeReference")
uppaal_types_TypeSpecification = Class(name="uppaal::types::TypeSpecification", is_abstract=True)
uppaal_types_ScalarTypeSpecification = Class(name="uppaal::types::ScalarTypeSpecification")
Expression = Class(name="Expression")
uppaal_types_StructTypeSpecification = Class(name="uppaal::types::StructTypeSpecification")
DataVariableDeclaration = Class(name="DataVariableDeclaration")
uppaal_declarations_GlobalDeclarations = Class(name="uppaal::declarations::GlobalDeclarations")
Declarations = Class(name="Declarations")
uppaal_types_IntegerBounds = Class(name="uppaal::types::IntegerBounds")
uppaal_types_Library = Class(name="uppaal::types::Library")
uppaal_declarations_Declarations = Class(name="uppaal::declarations::Declarations", is_abstract=True)
Declaration = Class(name="Declaration")
uppaal_declarations_DataVariableDeclaration = Class(name="uppaal::declarations::DataVariableDeclaration")
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
uppaal_declarations_Variable = Class(name="uppaal::declarations::Variable")
uppaal_declarations_FunctionDeclaration = Class(name="uppaal::declarations::FunctionDeclaration")
Function = Class(name="Function")
uppaal_declarations_Function = Class(name="uppaal::declarations::Function")
Block = Class(name="Block")
Parameter_ = Class(name="Parameter")
uppaal_declarations_TypeDeclaration = Class(name="uppaal::declarations::TypeDeclaration")
DeclaredType = Class(name="DeclaredType")
Variable = Class(name="Variable")
uppaal_declarations_Parameter = Class(name="uppaal::declarations::Parameter")
VariableContainer = Class(name="VariableContainer")
Initializer = Class(name="Initializer")
uppaal_declarations_Index = Class(name="uppaal::declarations::Index", is_abstract=True)
uppaal_declarations_ValueIndex = Class(name="uppaal::declarations::ValueIndex")
uppaal_declarations_TypeIndex = Class(name="uppaal::declarations::TypeIndex")
uppaal_declarations_VariableContainer = Class(name="uppaal::declarations::VariableContainer", is_abstract=True)
uppaal_global_ChannelList = Class(name="uppaal::global::ChannelList")
ChannelPriorityItem = Class(name="ChannelPriorityItem")
IdentifierExpression = Class(name="IdentifierExpression")
uppaal_declarations_Initializer = Class(name="uppaal::declarations::Initializer", is_abstract=True)
uppaal_declarations_ExpressionInitializer = Class(name="uppaal::declarations::ExpressionInitializer")
uppaal_declarations_ArrayInitializer = Class(name="uppaal::declarations::ArrayInitializer")
uppaal_global_ChannelPriority = Class(name="uppaal::global::ChannelPriority")
global_ChannelPriorityItem = Class(name="global::ChannelPriorityItem")
uppaal_global_ChannelPriorityItem = Class(name="uppaal::global::ChannelPriorityItem", is_abstract=True)
uppaal_system_ProgressMeasure = Class(name="uppaal::system::ProgressMeasure")
uppaal_global_DefaultChannelPriority = Class(name="uppaal::global::DefaultChannelPriority")
uppaal_system_TemplateDeclaration = Class(name="uppaal::system::TemplateDeclaration")
RedefinedTemplate = Class(name="RedefinedTemplate")
uppaal_system_System = Class(name="uppaal::system::System")
system_InstantiationList = Class(name="system::InstantiationList")
uppaal_system_InstantiationList = Class(name="uppaal::system::InstantiationList")
AbstractTemplate = Class(name="AbstractTemplate")
uppaal_templates_RedefinedTemplate = Class(name="uppaal::templates::RedefinedTemplate")
uppaal_templates_AbstractTemplate = Class(name="uppaal::templates::AbstractTemplate", is_abstract=True)
uppaal_templates_Template = Class(name="uppaal::templates::Template")
LocalDeclarations = Class(name="LocalDeclarations")
Location = Class(name="Location")
Edge = Class(name="Edge")
system_TemplateDeclaration = Class(name="system::TemplateDeclaration")
uppaal_templates_Location = Class(name="uppaal::templates::Location")
visuals_PlanarElement = Class(name="visuals::PlanarElement")
visuals_ColoredElement = Class(name="visuals::ColoredElement")
uppaal_templates_Edge = Class(name="uppaal::templates::Edge")
visuals_LinearElement = Class(name="visuals::LinearElement")
Synchronization = Class(name="Synchronization")
Selection = Class(name="Selection")
uppaal_templates_Synchronization = Class(name="uppaal::templates::Synchronization")
uppaal_templates_Selection = Class(name="uppaal::templates::Selection")
uppaal_statements_Statement = Class(name="uppaal::statements::Statement", is_abstract=True)
uppaal_statements_Block = Class(name="uppaal::statements::Block")
Statement = Class(name="Statement")
uppaal_statements_EmptyStatement = Class(name="uppaal::statements::EmptyStatement")
uppaal_statements_ForLoop = Class(name="uppaal::statements::ForLoop")
uppaal_statements_Iteration = Class(name="uppaal::statements::Iteration")
statements_Statement = Class(name="statements::Statement")
uppaal_statements_WhileLoop = Class(name="uppaal::statements::WhileLoop")
uppaal_statements_DoWhileLoop = Class(name="uppaal::statements::DoWhileLoop")
uppaal_statements_IfStatement = Class(name="uppaal::statements::IfStatement")
uppaal_statements_ReturnStatement = Class(name="uppaal::statements::ReturnStatement")
uppaal_statements_ExpressionStatement = Class(name="uppaal::statements::ExpressionStatement")
uppaal_expressions_Expression = Class(name="uppaal::expressions::Expression", is_abstract=True)
uppaal_expressions_NegationExpression = Class(name="uppaal::expressions::NegationExpression")
uppaal_expressions_PlusExpression = Class(name="uppaal::expressions::PlusExpression")
uppaal_expressions_MinusExpression = Class(name="uppaal::expressions::MinusExpression")
uppaal_expressions_BinaryExpression = Class(name="uppaal::expressions::BinaryExpression", is_abstract=True)
uppaal_expressions_AssignmentExpression = Class(name="uppaal::expressions::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
uppaal_expressions_IdentifierExpression = Class(name="uppaal::expressions::IdentifierExpression")
uppaal_expressions_LiteralExpression = Class(name="uppaal::expressions::LiteralExpression")
uppaal_expressions_ArithmeticExpression = Class(name="uppaal::expressions::ArithmeticExpression")
uppaal_expressions_LogicalExpression = Class(name="uppaal::expressions::LogicalExpression")
uppaal_expressions_FunctionCallExpression = Class(name="uppaal::expressions::FunctionCallExpression")
uppaal_expressions_ConditionExpression = Class(name="uppaal::expressions::ConditionExpression")
uppaal_expressions_CompareExpression = Class(name="uppaal::expressions::CompareExpression")
uppaal_expressions_QuantificationExpression = Class(name="uppaal::expressions::QuantificationExpression")
expressions_Expression = Class(name="expressions::Expression")
uppaal_expressions_ScopedIdentifierExpression = Class(name="uppaal::expressions::ScopedIdentifierExpression")
uppaal_expressions_IncrementDecrementExpression = Class(name="uppaal::expressions::IncrementDecrementExpression")
uppaal_expressions_BitShiftExpression = Class(name="uppaal::expressions::BitShiftExpression")
uppaal_expressions_MinMaxExpression = Class(name="uppaal::expressions::MinMaxExpression")
uppaal_expressions_BitwiseExpression = Class(name="uppaal::expressions::BitwiseExpression")
uppaal_visuals_ColoredElement = Class(name="uppaal::visuals::ColoredElement", is_abstract=True)
uppaal_visuals_PlanarElement = Class(name="uppaal::visuals::PlanarElement", is_abstract=True)
Point = Class(name="Point")
uppaal_visuals_LinearElement = Class(name="uppaal::visuals::LinearElement", is_abstract=True)
uppaal_visuals_Point = Class(name="uppaal::visuals::Point")

# uppaal_NTA class attributes and methods

# core_NamedElement class attributes and methods

# core_CommentableElement class attributes and methods

# GlobalDeclarations class attributes and methods

# uppaal_core_CommentableElement class attributes and methods
uppaal_core_CommentableElement_comment: Property = Property(name="comment", type=StringType)
uppaal_core_CommentableElement.attributes={uppaal_core_CommentableElement_comment}

# Template class attributes and methods

# SystemDeclarations class attributes and methods

# PredefinedType class attributes and methods

# uppaal_core_NamedElement class attributes and methods
uppaal_core_NamedElement_name: Property = Property(name="name", type=StringType)
uppaal_core_NamedElement.attributes={uppaal_core_NamedElement_name}

# TypeDeclaration class attributes and methods

# uppaal_types_Type class attributes and methods
uppaal_types_Type_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_Type.attributes={uppaal_types_Type_baseType}

# NamedElement class attributes and methods

# Index class attributes and methods

# TypeSpecification class attributes and methods

# uppaal_types_PredefinedType class attributes and methods
uppaal_types_PredefinedType_type: Property = Property(name="type", type=StringType)
uppaal_types_PredefinedType.attributes={uppaal_types_PredefinedType_type}

# Type class attributes and methods

# uppaal_types_DeclaredType class attributes and methods

# uppaal_types_RangeTypeSpecification class attributes and methods

# IntegerBounds class attributes and methods

# TypeDefinition class attributes and methods

# uppaal_types_TypeDefinition class attributes and methods
uppaal_types_TypeDefinition_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_TypeDefinition.attributes={uppaal_types_TypeDefinition_baseType}

# uppaal_types_TypeReference class attributes and methods

# uppaal_types_TypeSpecification class attributes and methods

# uppaal_types_ScalarTypeSpecification class attributes and methods

# Expression class attributes and methods

# uppaal_types_StructTypeSpecification class attributes and methods

# DataVariableDeclaration class attributes and methods

# uppaal_declarations_GlobalDeclarations class attributes and methods

# Declarations class attributes and methods

# uppaal_types_IntegerBounds class attributes and methods

# uppaal_types_Library class attributes and methods

# uppaal_declarations_Declarations class attributes and methods

# Declaration class attributes and methods

# uppaal_declarations_DataVariableDeclaration class attributes and methods
uppaal_declarations_DataVariableDeclaration_prefix: Property = Property(name="prefix", type=StringType)
uppaal_declarations_DataVariableDeclaration.attributes={uppaal_declarations_DataVariableDeclaration_prefix}

# global_ChannelPriority class attributes and methods

# uppaal_declarations_LocalDeclarations class attributes and methods

# uppaal_declarations_SystemDeclarations class attributes and methods

# system_System class attributes and methods

# system_ProgressMeasure class attributes and methods

# uppaal_declarations_Declaration class attributes and methods

# uppaal_declarations_VariableDeclaration class attributes and methods

# declarations_Declaration class attributes and methods

# declarations_VariableContainer class attributes and methods

# uppaal_declarations_ChannelVariableDeclaration class attributes and methods
uppaal_declarations_ChannelVariableDeclaration_urgent: Property = Property(name="urgent", type=BooleanType)
uppaal_declarations_ChannelVariableDeclaration_broadcast: Property = Property(name="broadcast", type=BooleanType)
uppaal_declarations_ChannelVariableDeclaration.attributes={uppaal_declarations_ChannelVariableDeclaration_broadcast, uppaal_declarations_ChannelVariableDeclaration_urgent}

# VariableDeclaration class attributes and methods

# uppaal_declarations_ClockVariableDeclaration class attributes and methods

# uppaal_declarations_Variable class attributes and methods

# uppaal_declarations_FunctionDeclaration class attributes and methods

# Function class attributes and methods

# uppaal_declarations_Function class attributes and methods

# Block class attributes and methods

# Parameter class attributes and methods

# uppaal_declarations_TypeDeclaration class attributes and methods

# DeclaredType class attributes and methods

# Variable class attributes and methods

# uppaal_declarations_Parameter class attributes and methods
uppaal_declarations_Parameter_callType: Property = Property(name="callType", type=StringType)
uppaal_declarations_Parameter.attributes={uppaal_declarations_Parameter_callType}

# VariableContainer class attributes and methods

# Initializer class attributes and methods

# uppaal_declarations_Index class attributes and methods

# uppaal_declarations_ValueIndex class attributes and methods

# uppaal_declarations_TypeIndex class attributes and methods

# uppaal_declarations_VariableContainer class attributes and methods

# uppaal_global_ChannelList class attributes and methods

# ChannelPriorityItem class attributes and methods

# IdentifierExpression class attributes and methods

# uppaal_declarations_Initializer class attributes and methods

# uppaal_declarations_ExpressionInitializer class attributes and methods

# uppaal_declarations_ArrayInitializer class attributes and methods

# uppaal_global_ChannelPriority class attributes and methods

# global_ChannelPriorityItem class attributes and methods

# uppaal_global_ChannelPriorityItem class attributes and methods

# uppaal_system_ProgressMeasure class attributes and methods

# uppaal_global_DefaultChannelPriority class attributes and methods

# uppaal_system_TemplateDeclaration class attributes and methods

# RedefinedTemplate class attributes and methods

# uppaal_system_System class attributes and methods

# system_InstantiationList class attributes and methods

# uppaal_system_InstantiationList class attributes and methods

# AbstractTemplate class attributes and methods

# uppaal_templates_RedefinedTemplate class attributes and methods

# uppaal_templates_AbstractTemplate class attributes and methods

# uppaal_templates_Template class attributes and methods

# LocalDeclarations class attributes and methods

# Location class attributes and methods

# Edge class attributes and methods

# system_TemplateDeclaration class attributes and methods

# uppaal_templates_Location class attributes and methods
uppaal_templates_Location_locationTimeKind: Property = Property(name="locationTimeKind", type=StringType)
uppaal_templates_Location.attributes={uppaal_templates_Location_locationTimeKind}

# visuals_PlanarElement class attributes and methods

# visuals_ColoredElement class attributes and methods

# uppaal_templates_Edge class attributes and methods

# visuals_LinearElement class attributes and methods

# Synchronization class attributes and methods

# Selection class attributes and methods

# uppaal_templates_Synchronization class attributes and methods
uppaal_templates_Synchronization_kind: Property = Property(name="kind", type=StringType)
uppaal_templates_Synchronization.attributes={uppaal_templates_Synchronization_kind}

# uppaal_templates_Selection class attributes and methods

# uppaal_statements_Statement class attributes and methods

# uppaal_statements_Block class attributes and methods

# Statement class attributes and methods

# uppaal_statements_EmptyStatement class attributes and methods

# uppaal_statements_ForLoop class attributes and methods

# uppaal_statements_Iteration class attributes and methods

# statements_Statement class attributes and methods

# uppaal_statements_WhileLoop class attributes and methods

# uppaal_statements_DoWhileLoop class attributes and methods

# uppaal_statements_IfStatement class attributes and methods

# uppaal_statements_ReturnStatement class attributes and methods

# uppaal_statements_ExpressionStatement class attributes and methods

# uppaal_expressions_Expression class attributes and methods

# uppaal_expressions_NegationExpression class attributes and methods

# uppaal_expressions_PlusExpression class attributes and methods

# uppaal_expressions_MinusExpression class attributes and methods

# uppaal_expressions_BinaryExpression class attributes and methods

# uppaal_expressions_AssignmentExpression class attributes and methods
uppaal_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_AssignmentExpression.attributes={uppaal_expressions_AssignmentExpression_operator}

# BinaryExpression class attributes and methods

# uppaal_expressions_IdentifierExpression class attributes and methods

# uppaal_expressions_LiteralExpression class attributes and methods
uppaal_expressions_LiteralExpression_text: Property = Property(name="text", type=StringType)
uppaal_expressions_LiteralExpression.attributes={uppaal_expressions_LiteralExpression_text}

# uppaal_expressions_ArithmeticExpression class attributes and methods
uppaal_expressions_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_ArithmeticExpression.attributes={uppaal_expressions_ArithmeticExpression_operator}

# uppaal_expressions_LogicalExpression class attributes and methods
uppaal_expressions_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_LogicalExpression.attributes={uppaal_expressions_LogicalExpression_operator}

# uppaal_expressions_FunctionCallExpression class attributes and methods

# uppaal_expressions_ConditionExpression class attributes and methods

# uppaal_expressions_CompareExpression class attributes and methods
uppaal_expressions_CompareExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_CompareExpression.attributes={uppaal_expressions_CompareExpression_operator}

# uppaal_expressions_QuantificationExpression class attributes and methods
uppaal_expressions_QuantificationExpression_quantifier: Property = Property(name="quantifier", type=StringType)
uppaal_expressions_QuantificationExpression.attributes={uppaal_expressions_QuantificationExpression_quantifier}

# expressions_Expression class attributes and methods

# uppaal_expressions_ScopedIdentifierExpression class attributes and methods

# uppaal_expressions_IncrementDecrementExpression class attributes and methods
uppaal_expressions_IncrementDecrementExpression_position: Property = Property(name="position", type=StringType)
uppaal_expressions_IncrementDecrementExpression_operator: Property = Property(name="operator", type=StringType)
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
uppaal_visuals_ColoredElement.attributes={uppaal_visuals_ColoredElement_colorCode, uppaal_visuals_ColoredElement_color}

# uppaal_visuals_PlanarElement class attributes and methods

# Point class attributes and methods

# uppaal_visuals_LinearElement class attributes and methods

# uppaal_visuals_Point class attributes and methods
uppaal_visuals_Point_x: Property = Property(name="x", type=IntegerType)
uppaal_visuals_Point_y: Property = Property(name="y", type=IntegerType)
uppaal_visuals_Point.attributes={uppaal_visuals_Point_y, uppaal_visuals_Point_x}

# Relationships
globalDeclarations0: BinaryAssociation = BinaryAssociation(
    name="globalDeclarations0",
    ends={
        Property(name="uppaal_NTA", type=GlobalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="GlobalDeclarations", type=uppaal_NTA, multiplicity=Multiplicity(1, 1))
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
clock10: BinaryAssociation = BinaryAssociation(
    name="clock10",
    ends={
        Property(name="PredefinedType12", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA11", type=PredefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
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
typeDeclaration22: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration22",
    ends={
        Property(name="declarations", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeDeclaration", type=TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
index19: BinaryAssociation = BinaryAssociation(
    name="index19",
    ends={
        Property(name="Index", type=uppaal_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Type", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeSpecification20: BinaryAssociation = BinaryAssociation(
    name="typeSpecification20",
    ends={
        Property(name="TypeSpecification", type=uppaal_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Type21", type=TypeSpecification, multiplicity=Multiplicity(0, 1))
    }
)
declaration28: BinaryAssociation = BinaryAssociation(
    name="declaration28",
    ends={
        Property(name="DataVariableDeclaration", type=uppaal_types_StructTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_StructTypeSpecification", type=DataVariableDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition23: BinaryAssociation = BinaryAssociation(
    name="typeDefinition23",
    ends={
        Property(name="TypeDefinition", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_DeclaredType", type=TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
typeSpecification24: BinaryAssociation = BinaryAssociation(
    name="typeSpecification24",
    ends={
        Property(name="TypeSpecification25", type=uppaal_types_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_TypeDefinition", type=TypeSpecification, multiplicity=Multiplicity(0, 1))
    }
)
referredType26: BinaryAssociation = BinaryAssociation(
    name="referredType26",
    ends={
        Property(name="Type", type=uppaal_types_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_TypeReference", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
sizeExpression27: BinaryAssociation = BinaryAssociation(
    name="sizeExpression27",
    ends={
        Property(name="Expression", type=uppaal_types_ScalarTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_ScalarTypeSpecification", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds29: BinaryAssociation = BinaryAssociation(
    name="bounds29",
    ends={
        Property(name="IntegerBounds", type=uppaal_types_RangeTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_RangeTypeSpecification", type=IntegerBounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound30: BinaryAssociation = BinaryAssociation(
    name="lowerBound30",
    ends={
        Property(name="Expression31", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound32: BinaryAssociation = BinaryAssociation(
    name="upperBound32",
    ends={
        Property(name="Expression34", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds33", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types35: BinaryAssociation = BinaryAssociation(
    name="types35",
    ends={
        Property(name="PredefinedType36", type=uppaal_types_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Library", type=PredefinedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration37: BinaryAssociation = BinaryAssociation(
    name="declaration37",
    ends={
        Property(name="Declaration", type=uppaal_declarations_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Declarations", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelPriority38: BinaryAssociation = BinaryAssociation(
    name="channelPriority38",
    ends={
        Property(name="global_ChannelPriority", type=uppaal_declarations_GlobalDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_GlobalDeclarations", type=global_ChannelPriority, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system39: BinaryAssociation = BinaryAssociation(
    name="system39",
    ends={
        Property(name="system_System", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations", type=system_System, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
progressMeasure40: BinaryAssociation = BinaryAssociation(
    name="progressMeasure40",
    ends={
        Property(name="system_ProgressMeasure", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations41", type=system_ProgressMeasure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function42: BinaryAssociation = BinaryAssociation(
    name="function42",
    ends={
        Property(name="Function", type=uppaal_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_FunctionDeclaration", type=Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType43: BinaryAssociation = BinaryAssociation(
    name="returnType43",
    ends={
        Property(name="TypeDefinition44", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block45: BinaryAssociation = BinaryAssociation(
    name="block45",
    ends={
        Property(name="Block", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function46", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter47: BinaryAssociation = BinaryAssociation(
    name="parameter47",
    ends={
        Property(name="Parameter", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function48", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="types", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DeclaredType", type=DeclaredType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition50: BinaryAssociation = BinaryAssociation(
    name="typeDefinition50",
    ends={
        Property(name="TypeDefinition51", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeDeclaration", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable67: BinaryAssociation = BinaryAssociation(
    name="variable67",
    ends={
        Property(name="declarations68", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
index52: BinaryAssociation = BinaryAssociation(
    name="index52",
    ends={
        Property(name="Index53", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container54: BinaryAssociation = BinaryAssociation(
    name="container54",
    ends={
        Property(name="declarations55", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableContainer", type=VariableContainer, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition56: BinaryAssociation = BinaryAssociation(
    name="typeDefinition56",
    ends={
        Property(name="TypeDefinition58", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable57", type=TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
initializer59: BinaryAssociation = BinaryAssociation(
    name="initializer59",
    ends={
        Property(name="Initializer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable60", type=Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeExpression61: BinaryAssociation = BinaryAssociation(
    name="sizeExpression61",
    ends={
        Property(name="Expression62", type=uppaal_declarations_ValueIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ValueIndex", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDefinition63: BinaryAssociation = BinaryAssociation(
    name="typeDefinition63",
    ends={
        Property(name="TypeDefinition64", type=uppaal_declarations_TypeIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeIndex", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDefinition65: BinaryAssociation = BinaryAssociation(
    name="typeDefinition65",
    ends={
        Property(name="TypeDefinition66", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_VariableContainer", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
channelExpression75: BinaryAssociation = BinaryAssociation(
    name="channelExpression75",
    ends={
        Property(name="IdentifierExpression", type=uppaal_global_ChannelList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelList", type=IdentifierExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableDeclaration69: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration69",
    ends={
        Property(name="VariableDeclaration", type=uppaal_declarations_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Parameter", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="Expression71", type=uppaal_declarations_ExpressionInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ExpressionInitializer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer72: BinaryAssociation = BinaryAssociation(
    name="initializer72",
    ends={
        Property(name="Initializer73", type=uppaal_declarations_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ArrayInitializer", type=Initializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
item74: BinaryAssociation = BinaryAssociation(
    name="item74",
    ends={
        Property(name="global_ChannelPriorityItem", type=uppaal_global_ChannelPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriority", type=global_ChannelPriorityItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="Expression82", type=uppaal_system_ProgressMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_ProgressMeasure", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declaredTemplate76: BinaryAssociation = BinaryAssociation(
    name="declaredTemplate76",
    ends={
        Property(name="templates", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="RedefinedTemplate", type=RedefinedTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument77: BinaryAssociation = BinaryAssociation(
    name="argument77",
    ends={
        Property(name="Expression78", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_TemplateDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiationList79: BinaryAssociation = BinaryAssociation(
    name="instantiationList79",
    ends={
        Property(name="system_InstantiationList", type=uppaal_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_System", type=system_InstantiationList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template80: BinaryAssociation = BinaryAssociation(
    name="template80",
    ends={
        Property(name="AbstractTemplate", type=uppaal_system_InstantiationList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_InstantiationList", type=AbstractTemplate, multiplicity=Multiplicity(1, 9999))
    }
)
referredTemplate93: BinaryAssociation = BinaryAssociation(
    name="referredTemplate93",
    ends={
        Property(name="AbstractTemplate94", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_RedefinedTemplate", type=AbstractTemplate, multiplicity=Multiplicity(1, 1))
    }
)
parameter83: BinaryAssociation = BinaryAssociation(
    name="parameter83",
    ends={
        Property(name="Parameter84", type=uppaal_templates_AbstractTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_AbstractTemplate", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations85: BinaryAssociation = BinaryAssociation(
    name="declarations85",
    ends={
        Property(name="LocalDeclarations", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location86: BinaryAssociation = BinaryAssociation(
    name="location86",
    ends={
        Property(name="templates87", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Location", type=Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edge88: BinaryAssociation = BinaryAssociation(
    name="edge88",
    ends={
        Property(name="templates89", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="Edge", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init90: BinaryAssociation = BinaryAssociation(
    name="init90",
    ends={
        Property(name="Location92", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template91", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate107: BinaryAssociation = BinaryAssociation(
    name="parentTemplate107",
    ends={
        Property(name="templates109", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Template108", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
guard110: BinaryAssociation = BinaryAssociation(
    name="guard110",
    ends={
        Property(name="Expression112", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge111", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration95: BinaryAssociation = BinaryAssociation(
    name="declaration95",
    ends={
        Property(name="declarations96", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=system_TemplateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate97: BinaryAssociation = BinaryAssociation(
    name="parentTemplate97",
    ends={
        Property(name="templates99", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="Template98", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
invariant100: BinaryAssociation = BinaryAssociation(
    name="invariant100",
    ends={
        Property(name="Expression101", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Location", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source102: BinaryAssociation = BinaryAssociation(
    name="source102",
    ends={
        Property(name="Location103", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
target104: BinaryAssociation = BinaryAssociation(
    name="target104",
    ends={
        Property(name="Location106", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge105", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
declarations122: BinaryAssociation = BinaryAssociation(
    name="declarations122",
    ends={
        Property(name="LocalDeclarations123", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
update113: BinaryAssociation = BinaryAssociation(
    name="update113",
    ends={
        Property(name="Expression115", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge114", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization116: BinaryAssociation = BinaryAssociation(
    name="synchronization116",
    ends={
        Property(name="Synchronization", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge117", type=Synchronization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection118: BinaryAssociation = BinaryAssociation(
    name="selection118",
    ends={
        Property(name="Selection", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge119", type=Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelExpression120: BinaryAssociation = BinaryAssociation(
    name="channelExpression120",
    ends={
        Property(name="IdentifierExpression121", type=uppaal_templates_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Synchronization", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression139: BinaryAssociation = BinaryAssociation(
    name="expression139",
    ends={
        Property(name="Expression140", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement141: BinaryAssociation = BinaryAssociation(
    name="statement141",
    ends={
        Property(name="Statement143", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop142", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement124: BinaryAssociation = BinaryAssociation(
    name="statement124",
    ends={
        Property(name="Statement", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block125", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialization126: BinaryAssociation = BinaryAssociation(
    name="initialization126",
    ends={
        Property(name="Expression127", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition128: BinaryAssociation = BinaryAssociation(
    name="condition128",
    ends={
        Property(name="Expression130", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop129", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteration131: BinaryAssociation = BinaryAssociation(
    name="iteration131",
    ends={
        Property(name="Expression133", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop132", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement134: BinaryAssociation = BinaryAssociation(
    name="statement134",
    ends={
        Property(name="Statement136", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop135", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement137: BinaryAssociation = BinaryAssociation(
    name="statement137",
    ends={
        Property(name="Statement138", type=uppaal_statements_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Iteration", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement144: BinaryAssociation = BinaryAssociation(
    name="statement144",
    ends={
        Property(name="Statement145", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression146: BinaryAssociation = BinaryAssociation(
    name="expression146",
    ends={
        Property(name="Expression148", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop147", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression149: BinaryAssociation = BinaryAssociation(
    name="ifExpression149",
    ends={
        Property(name="Expression150", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement151: BinaryAssociation = BinaryAssociation(
    name="thenStatement151",
    ends={
        Property(name="Statement153", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement152", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement154: BinaryAssociation = BinaryAssociation(
    name="elseStatement154",
    ends={
        Property(name="Statement156", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement155", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnExpression157: BinaryAssociation = BinaryAssociation(
    name="returnExpression157",
    ends={
        Property(name="Expression158", type=uppaal_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="Expression160", type=uppaal_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negatedExpression161: BinaryAssociation = BinaryAssociation(
    name="negatedExpression161",
    ends={
        Property(name="Expression162", type=uppaal_expressions_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_NegationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
confirmedExpression163: BinaryAssociation = BinaryAssociation(
    name="confirmedExpression163",
    ends={
        Property(name="Expression164", type=uppaal_expressions_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_PlusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invertedExpression165: BinaryAssociation = BinaryAssociation(
    name="invertedExpression165",
    ends={
        Property(name="Expression166", type=uppaal_expressions_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_MinusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstExpr167: BinaryAssociation = BinaryAssociation(
    name="firstExpr167",
    ends={
        Property(name="Expression168", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
secondExpr169: BinaryAssociation = BinaryAssociation(
    name="secondExpr169",
    ends={
        Property(name="Expression171", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression170", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier172: BinaryAssociation = BinaryAssociation(
    name="identifier172",
    ends={
        Property(name="NamedElement", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
index173: BinaryAssociation = BinaryAssociation(
    name="index173",
    ends={
        Property(name="Expression175", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression174", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function176: BinaryAssociation = BinaryAssociation(
    name="function176",
    ends={
        Property(name="Function177", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
argument178: BinaryAssociation = BinaryAssociation(
    name="argument178",
    ends={
        Property(name="Expression180", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression179", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExpression181: BinaryAssociation = BinaryAssociation(
    name="ifExpression181",
    ends={
        Property(name="Expression182", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression183: BinaryAssociation = BinaryAssociation(
    name="thenExpression183",
    ends={
        Property(name="Expression185", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression184", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression186: BinaryAssociation = BinaryAssociation(
    name="elseExpression186",
    ends={
        Property(name="Expression188", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression187", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scope189: BinaryAssociation = BinaryAssociation(
    name="scope189",
    ends={
        Property(name="Expression190", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier191: BinaryAssociation = BinaryAssociation(
    name="identifier191",
    ends={
        Property(name="IdentifierExpression193", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression192", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression194: BinaryAssociation = BinaryAssociation(
    name="expression194",
    ends={
        Property(name="Expression195", type=uppaal_expressions_QuantificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_QuantificationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression196: BinaryAssociation = BinaryAssociation(
    name="expression196",
    ends={
        Property(name="Expression197", type=uppaal_expressions_IncrementDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IncrementDecrementExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position198: BinaryAssociation = BinaryAssociation(
    name="position198",
    ends={
        Property(name="Point", type=uppaal_visuals_PlanarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_PlanarElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bendPoint199: BinaryAssociation = BinaryAssociation(
    name="bendPoint199",
    ends={
        Property(name="Point200", type=uppaal_visuals_LinearElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_LinearElement", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uppaal_NTA_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_NTA)
gen_uppaal_NTA_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_NTA)
gen_uppaal_types_Type_NamedElement = Generalization(general=NamedElement, specific=uppaal_types_Type)
gen_uppaal_types_PredefinedType_Type = Generalization(general=Type, specific=uppaal_types_PredefinedType)
gen_uppaal_types_DeclaredType_Type = Generalization(general=Type, specific=uppaal_types_DeclaredType)
gen_uppaal_types_RangeTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_RangeTypeSpecification)
gen_uppaal_types_TypeReference_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeReference)
gen_uppaal_types_TypeSpecification_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeSpecification)
gen_uppaal_types_ScalarTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_ScalarTypeSpecification)
gen_uppaal_types_StructTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_StructTypeSpecification)
gen_uppaal_declarations_GlobalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_GlobalDeclarations)
gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_DataVariableDeclaration)
gen_uppaal_declarations_LocalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_LocalDeclarations)
gen_uppaal_declarations_SystemDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_SystemDeclarations)
gen_uppaal_declarations_VariableDeclaration_declarations_Declaration = Generalization(general=declarations_Declaration, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ChannelVariableDeclaration)
gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ClockVariableDeclaration)
gen_uppaal_declarations_Variable_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_FunctionDeclaration)
gen_uppaal_declarations_Function_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_TypeDeclaration)
gen_uppaal_declarations_ValueIndex_Index = Generalization(general=Index, specific=uppaal_declarations_ValueIndex)
gen_uppaal_declarations_TypeIndex_Index = Generalization(general=Index, specific=uppaal_declarations_TypeIndex)
gen_uppaal_global_ChannelList_ChannelPriorityItem = Generalization(general=ChannelPriorityItem, specific=uppaal_global_ChannelList)
gen_uppaal_declarations_ExpressionInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ExpressionInitializer)
gen_uppaal_declarations_ArrayInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ArrayInitializer)
gen_uppaal_global_DefaultChannelPriority_ChannelPriorityItem = Generalization(general=ChannelPriorityItem, specific=uppaal_global_DefaultChannelPriority)
gen_uppaal_system_TemplateDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_system_TemplateDeclaration)
gen_uppaal_templates_RedefinedTemplate_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_RedefinedTemplate)
gen_uppaal_templates_AbstractTemplate_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_AbstractTemplate_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_Template_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_Template)
gen_uppaal_templates_Location_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_PlanarElement = Generalization(general=visuals_PlanarElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Edge_visuals_LinearElement = Generalization(general=visuals_LinearElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Selection_VariableContainer = Generalization(general=VariableContainer, specific=uppaal_templates_Selection)
gen_uppaal_statements_Block_Statement = Generalization(general=Statement, specific=uppaal_statements_Block)
gen_uppaal_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_EmptyStatement)
gen_uppaal_statements_ForLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_ForLoop)
gen_uppaal_statements_Iteration_statements_Statement = Generalization(general=statements_Statement, specific=uppaal_statements_Iteration)
gen_uppaal_statements_Iteration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_statements_Iteration)
gen_uppaal_statements_WhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_WhileLoop)
gen_uppaal_statements_DoWhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_DoWhileLoop)
gen_uppaal_statements_IfStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_IfStatement)
gen_uppaal_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ReturnStatement)
gen_uppaal_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ExpressionStatement)
gen_uppaal_expressions_NegationExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_NegationExpression)
gen_uppaal_expressions_PlusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_PlusExpression)
gen_uppaal_expressions_MinusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_MinusExpression)
gen_uppaal_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_BinaryExpression)
gen_uppaal_expressions_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_AssignmentExpression)
gen_uppaal_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IdentifierExpression)
gen_uppaal_expressions_LiteralExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_LiteralExpression)
gen_uppaal_expressions_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_ArithmeticExpression)
gen_uppaal_expressions_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_LogicalExpression)
gen_uppaal_expressions_FunctionCallExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_FunctionCallExpression)
gen_uppaal_expressions_ConditionExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ConditionExpression)
gen_uppaal_expressions_CompareExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_CompareExpression)
gen_uppaal_expressions_QuantificationExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_ScopedIdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ScopedIdentifierExpression)
gen_uppaal_expressions_IncrementDecrementExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IncrementDecrementExpression)
gen_uppaal_expressions_BitShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitShiftExpression)
gen_uppaal_expressions_MinMaxExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_MinMaxExpression)
gen_uppaal_expressions_BitwiseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitwiseExpression)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={uppaal_NTA, core_NamedElement, core_CommentableElement, GlobalDeclarations, uppaal_core_CommentableElement, Template, SystemDeclarations, PredefinedType, uppaal_core_NamedElement, TypeDeclaration, uppaal_types_Type, NamedElement, Index, TypeSpecification, uppaal_types_PredefinedType, Type, uppaal_types_DeclaredType, uppaal_types_RangeTypeSpecification, IntegerBounds, TypeDefinition, uppaal_types_TypeDefinition, uppaal_types_TypeReference, uppaal_types_TypeSpecification, uppaal_types_ScalarTypeSpecification, Expression, uppaal_types_StructTypeSpecification, DataVariableDeclaration, uppaal_declarations_GlobalDeclarations, Declarations, uppaal_types_IntegerBounds, uppaal_types_Library, uppaal_declarations_Declarations, Declaration, uppaal_declarations_DataVariableDeclaration, global_ChannelPriority, uppaal_declarations_LocalDeclarations, uppaal_declarations_SystemDeclarations, system_System, system_ProgressMeasure, uppaal_declarations_Declaration, uppaal_declarations_VariableDeclaration, declarations_Declaration, declarations_VariableContainer, uppaal_declarations_ChannelVariableDeclaration, VariableDeclaration, uppaal_declarations_ClockVariableDeclaration, uppaal_declarations_Variable, uppaal_declarations_FunctionDeclaration, Function, uppaal_declarations_Function, Block, Parameter_, uppaal_declarations_TypeDeclaration, DeclaredType, Variable, uppaal_declarations_Parameter, VariableContainer, Initializer, uppaal_declarations_Index, uppaal_declarations_ValueIndex, uppaal_declarations_TypeIndex, uppaal_declarations_VariableContainer, uppaal_global_ChannelList, ChannelPriorityItem, IdentifierExpression, uppaal_declarations_Initializer, uppaal_declarations_ExpressionInitializer, uppaal_declarations_ArrayInitializer, uppaal_global_ChannelPriority, global_ChannelPriorityItem, uppaal_global_ChannelPriorityItem, uppaal_system_ProgressMeasure, uppaal_global_DefaultChannelPriority, uppaal_system_TemplateDeclaration, RedefinedTemplate, uppaal_system_System, system_InstantiationList, uppaal_system_InstantiationList, AbstractTemplate, uppaal_templates_RedefinedTemplate, uppaal_templates_AbstractTemplate, uppaal_templates_Template, LocalDeclarations, Location, Edge, system_TemplateDeclaration, uppaal_templates_Location, visuals_PlanarElement, visuals_ColoredElement, uppaal_templates_Edge, visuals_LinearElement, Synchronization, Selection, uppaal_templates_Synchronization, uppaal_templates_Selection, uppaal_statements_Statement, uppaal_statements_Block, Statement, uppaal_statements_EmptyStatement, uppaal_statements_ForLoop, uppaal_statements_Iteration, statements_Statement, uppaal_statements_WhileLoop, uppaal_statements_DoWhileLoop, uppaal_statements_IfStatement, uppaal_statements_ReturnStatement, uppaal_statements_ExpressionStatement, uppaal_expressions_Expression, uppaal_expressions_NegationExpression, uppaal_expressions_PlusExpression, uppaal_expressions_MinusExpression, uppaal_expressions_BinaryExpression, uppaal_expressions_AssignmentExpression, BinaryExpression, uppaal_expressions_IdentifierExpression, uppaal_expressions_LiteralExpression, uppaal_expressions_ArithmeticExpression, uppaal_expressions_LogicalExpression, uppaal_expressions_FunctionCallExpression, uppaal_expressions_ConditionExpression, uppaal_expressions_CompareExpression, uppaal_expressions_QuantificationExpression, expressions_Expression, uppaal_expressions_ScopedIdentifierExpression, uppaal_expressions_IncrementDecrementExpression, uppaal_expressions_BitShiftExpression, uppaal_expressions_MinMaxExpression, uppaal_expressions_BitwiseExpression, uppaal_visuals_ColoredElement, uppaal_visuals_PlanarElement, Point, uppaal_visuals_LinearElement, uppaal_visuals_Point, BuiltInType, DataVariablePrefix, CallType, LocationKind, SynchronizationKind, AssignmentOperator, ArithmeticOperator, LogicalOperator, CompareOperator, Quantifier, MinMaxOperator, IncrementDecrementOperator, IncrementDecrementPosition, BitShiftOperator, ColorKind, BitwiseOperator},
    associations={globalDeclarations0, template1, systemDeclarations3, int5, bool7, clock10, chan13, void16, typeDeclaration22, index19, typeSpecification20, declaration28, typeDefinition23, typeSpecification24, referredType26, sizeExpression27, bounds29, lowerBound30, upperBound32, types35, declaration37, channelPriority38, system39, progressMeasure40, function42, returnType43, block45, parameter47, type49, typeDefinition50, variable67, index52, container54, typeDefinition56, initializer59, sizeExpression61, typeDefinition63, typeDefinition65, channelExpression75, variableDeclaration69, expression70, initializer72, item74, expression81, declaredTemplate76, argument77, instantiationList79, template80, referredTemplate93, parameter83, declarations85, location86, edge88, init90, parentTemplate107, guard110, declaration95, parentTemplate97, invariant100, source102, target104, declarations122, update113, synchronization116, selection118, channelExpression120, expression139, statement141, statement124, initialization126, condition128, iteration131, statement134, statement137, statement144, expression146, ifExpression149, thenStatement151, elseStatement154, returnExpression157, expression159, negatedExpression161, confirmedExpression163, invertedExpression165, firstExpr167, secondExpr169, identifier172, index173, function176, argument178, ifExpression181, thenExpression183, elseExpression186, scope189, identifier191, expression194, expression196, position198, bendPoint199},
    generalizations={gen_uppaal_NTA_core_NamedElement, gen_uppaal_NTA_core_CommentableElement, gen_uppaal_types_Type_NamedElement, gen_uppaal_types_PredefinedType_Type, gen_uppaal_types_DeclaredType_Type, gen_uppaal_types_RangeTypeSpecification_TypeSpecification, gen_uppaal_types_TypeReference_TypeDefinition, gen_uppaal_types_TypeSpecification_TypeDefinition, gen_uppaal_types_ScalarTypeSpecification_TypeSpecification, gen_uppaal_types_StructTypeSpecification_TypeSpecification, gen_uppaal_declarations_GlobalDeclarations_Declarations, gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_LocalDeclarations_Declarations, gen_uppaal_declarations_SystemDeclarations_Declarations, gen_uppaal_declarations_VariableDeclaration_declarations_Declaration, gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer, gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_Variable_NamedElement, gen_uppaal_declarations_FunctionDeclaration_Declaration, gen_uppaal_declarations_Function_NamedElement, gen_uppaal_declarations_TypeDeclaration_Declaration, gen_uppaal_declarations_ValueIndex_Index, gen_uppaal_declarations_TypeIndex_Index, gen_uppaal_global_ChannelList_ChannelPriorityItem, gen_uppaal_declarations_ExpressionInitializer_Initializer, gen_uppaal_declarations_ArrayInitializer_Initializer, gen_uppaal_global_DefaultChannelPriority_ChannelPriorityItem, gen_uppaal_system_TemplateDeclaration_Declaration, gen_uppaal_templates_RedefinedTemplate_AbstractTemplate, gen_uppaal_templates_AbstractTemplate_core_NamedElement, gen_uppaal_templates_AbstractTemplate_core_CommentableElement, gen_uppaal_templates_Template_AbstractTemplate, gen_uppaal_templates_Location_core_NamedElement, gen_uppaal_templates_Location_core_CommentableElement, gen_uppaal_templates_Location_visuals_PlanarElement, gen_uppaal_templates_Location_visuals_ColoredElement, gen_uppaal_templates_Edge_visuals_LinearElement, gen_uppaal_templates_Edge_core_CommentableElement, gen_uppaal_templates_Edge_visuals_ColoredElement, gen_uppaal_templates_Selection_VariableContainer, gen_uppaal_statements_Block_Statement, gen_uppaal_statements_EmptyStatement_Statement, gen_uppaal_statements_ForLoop_Statement, gen_uppaal_statements_Iteration_statements_Statement, gen_uppaal_statements_Iteration_declarations_VariableContainer, gen_uppaal_statements_WhileLoop_Statement, gen_uppaal_statements_DoWhileLoop_Statement, gen_uppaal_statements_IfStatement_Statement, gen_uppaal_statements_ReturnStatement_Statement, gen_uppaal_statements_ExpressionStatement_Statement, gen_uppaal_expressions_NegationExpression_Expression, gen_uppaal_expressions_PlusExpression_Expression, gen_uppaal_expressions_MinusExpression_Expression, gen_uppaal_expressions_BinaryExpression_Expression, gen_uppaal_expressions_AssignmentExpression_BinaryExpression, gen_uppaal_expressions_IdentifierExpression_Expression, gen_uppaal_expressions_LiteralExpression_Expression, gen_uppaal_expressions_ArithmeticExpression_BinaryExpression, gen_uppaal_expressions_LogicalExpression_BinaryExpression, gen_uppaal_expressions_FunctionCallExpression_Expression, gen_uppaal_expressions_ConditionExpression_Expression, gen_uppaal_expressions_CompareExpression_BinaryExpression, gen_uppaal_expressions_QuantificationExpression_expressions_Expression, gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer, gen_uppaal_expressions_ScopedIdentifierExpression_Expression, gen_uppaal_expressions_IncrementDecrementExpression_Expression, gen_uppaal_expressions_BitShiftExpression_BinaryExpression, gen_uppaal_expressions_MinMaxExpression_BinaryExpression, gen_uppaal_expressions_BitwiseExpression_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)