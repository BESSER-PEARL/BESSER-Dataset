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

SynchronizationKind: Enumeration = Enumeration(
    name="SynchronizationKind",
    literals={
            EnumerationLiteral(name="RECEIVE"),
			EnumerationLiteral(name="SEND")
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

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="DIVIDE_EQUAL"),
			EnumerationLiteral(name="MODULO_EQUAL"),
			EnumerationLiteral(name="BIT_AND_EQUAL"),
			EnumerationLiteral(name="BIT_OR_EQUAL"),
			EnumerationLiteral(name="BIT_LEFT_EQUAL"),
			EnumerationLiteral(name="BIT_RIGHT_EQUAL"),
			EnumerationLiteral(name="BIT_XOR_EQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="PLUS_EQUAL"),
			EnumerationLiteral(name="MINUS_EQUAL"),
			EnumerationLiteral(name="TIMES_EQUAL")
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
			EnumerationLiteral(name="IMPLY"),
			EnumerationLiteral(name="XOR")
    }
)

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="EXISTENTIAL"),
			EnumerationLiteral(name="UNIVERSAL")
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
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="OR")
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

# Classes
uppaal_NTA = Class(name="uppaal_NTA")
core_NamedElement = Class(name="core_NamedElement")
core_CommentableElement = Class(name="core_CommentableElement")
GlobalDeclarations = Class(name="GlobalDeclarations")
uppaal_core_NamedElement = Class(name="uppaal_core_NamedElement", is_abstract=True)
Template = Class(name="Template")
SystemDeclarations = Class(name="SystemDeclarations")
PredefinedType = Class(name="PredefinedType")
uppaal_types_DeclaredType = Class(name="uppaal_types_DeclaredType")
TypeDeclaration = Class(name="TypeDeclaration")
uppaal_core_CommentableElement = Class(name="uppaal_core_CommentableElement", is_abstract=True)
uppaal_types_Type = Class(name="uppaal_types_Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
Index = Class(name="Index")
uppaal_types_PredefinedType = Class(name="uppaal_types_PredefinedType")
Type = Class(name="Type")
uppaal_types_StructTypeSpecification = Class(name="uppaal_types_StructTypeSpecification")
DataVariableDeclaration = Class(name="DataVariableDeclaration")
uppaal_types_RangeTypeSpecification = Class(name="uppaal_types_RangeTypeSpecification")
IntegerBounds = Class(name="IntegerBounds")
uppaal_types_IntegerBounds = Class(name="uppaal_types_IntegerBounds")
TypeDefinition = Class(name="TypeDefinition")
uppaal_types_TypeDefinition = Class(name="uppaal_types_TypeDefinition", is_abstract=True)
uppaal_types_TypeReference = Class(name="uppaal_types_TypeReference")
uppaal_types_TypeSpecification = Class(name="uppaal_types_TypeSpecification", is_abstract=True)
uppaal_types_ScalarTypeSpecification = Class(name="uppaal_types_ScalarTypeSpecification")
TypeSpecification = Class(name="TypeSpecification")
Expression = Class(name="Expression")
system_System = Class(name="system_System")
system_ProgressMeasure = Class(name="system_ProgressMeasure")
uppaal_declarations_Declaration = Class(name="uppaal_declarations_Declaration", is_abstract=True)
uppaal_declarations_VariableDeclaration = Class(name="uppaal_declarations_VariableDeclaration", is_abstract=True)
declarations_Declaration = Class(name="declarations_Declaration")
declarations_VariableContainer = Class(name="declarations_VariableContainer")
uppaal_declarations_ChannelVariableDeclaration = Class(name="uppaal_declarations_ChannelVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
uppaal_declarations_Declarations = Class(name="uppaal_declarations_Declarations", is_abstract=True)
Declaration = Class(name="Declaration")
uppaal_declarations_GlobalDeclarations = Class(name="uppaal_declarations_GlobalDeclarations")
Declarations = Class(name="Declarations")
global_ChannelPriority = Class(name="global_ChannelPriority")
uppaal_declarations_LocalDeclarations = Class(name="uppaal_declarations_LocalDeclarations")
uppaal_declarations_SystemDeclarations = Class(name="uppaal_declarations_SystemDeclarations")
Block = Class(name="Block")
Parameter_ = Class(name="Parameter")
uppaal_declarations_TypeDeclaration = Class(name="uppaal_declarations_TypeDeclaration")
DeclaredType = Class(name="DeclaredType")
uppaal_declarations_Variable = Class(name="uppaal_declarations_Variable")
uppaal_declarations_ClockVariableDeclaration = Class(name="uppaal_declarations_ClockVariableDeclaration")
uppaal_declarations_DataVariableDeclaration = Class(name="uppaal_declarations_DataVariableDeclaration")
uppaal_declarations_FunctionDeclaration = Class(name="uppaal_declarations_FunctionDeclaration")
Function = Class(name="Function")
uppaal_declarations_Function = Class(name="uppaal_declarations_Function")
uppaal_declarations_ValueIndex = Class(name="uppaal_declarations_ValueIndex")
uppaal_declarations_TypeIndex = Class(name="uppaal_declarations_TypeIndex")
uppaal_declarations_VariableContainer = Class(name="uppaal_declarations_VariableContainer", is_abstract=True)
VariableContainer = Class(name="VariableContainer")
Initializer = Class(name="Initializer")
uppaal_declarations_Index = Class(name="uppaal_declarations_Index", is_abstract=True)
uppaal_declarations_ExpressionInitializer = Class(name="uppaal_declarations_ExpressionInitializer")
uppaal_declarations_ArrayInitializer = Class(name="uppaal_declarations_ArrayInitializer")
uppaal_global_ChannelPriority = Class(name="uppaal_global_ChannelPriority")
global_ChannelPriorityItem = Class(name="global_ChannelPriorityItem")
uppaal_global_ChannelPriorityItem = Class(name="uppaal_global_ChannelPriorityItem", is_abstract=True)
uppaal_global_ChannelList = Class(name="uppaal_global_ChannelList")
ChannelPriorityItem = Class(name="ChannelPriorityItem")
Variable = Class(name="Variable")
uppaal_declarations_Parameter = Class(name="uppaal_declarations_Parameter")
uppaal_declarations_Initializer = Class(name="uppaal_declarations_Initializer", is_abstract=True)
uppaal_system_System = Class(name="uppaal_system_System")
system_InstantiationList = Class(name="system_InstantiationList")
uppaal_system_InstantiationList = Class(name="uppaal_system_InstantiationList")
AbstractTemplate = Class(name="AbstractTemplate")
uppaal_system_ProgressMeasure = Class(name="uppaal_system_ProgressMeasure")
IdentifierExpression = Class(name="IdentifierExpression")
uppaal_global_DefaultChannelPriority = Class(name="uppaal_global_DefaultChannelPriority")
uppaal_system_TemplateDeclaration = Class(name="uppaal_system_TemplateDeclaration")
RedefinedTemplate = Class(name="RedefinedTemplate")
Location = Class(name="Location")
Edge = Class(name="Edge")
uppaal_templates_RedefinedTemplate = Class(name="uppaal_templates_RedefinedTemplate")
uppaal_templates_AbstractTemplate = Class(name="uppaal_templates_AbstractTemplate", is_abstract=True)
uppaal_templates_Template = Class(name="uppaal_templates_Template")
LocalDeclarations = Class(name="LocalDeclarations")
uppaal_templates_Location = Class(name="uppaal_templates_Location")
visuals_PlanarElement = Class(name="visuals_PlanarElement")
visuals_ColoredElement = Class(name="visuals_ColoredElement")
system_TemplateDeclaration = Class(name="system_TemplateDeclaration")
Synchronization = Class(name="Synchronization")
Selection = Class(name="Selection")
uppaal_templates_Synchronization = Class(name="uppaal_templates_Synchronization")
uppaal_templates_Edge = Class(name="uppaal_templates_Edge")
visuals_LinearElement = Class(name="visuals_LinearElement")
uppaal_statements_EmptyStatement = Class(name="uppaal_statements_EmptyStatement")
uppaal_statements_ForLoop = Class(name="uppaal_statements_ForLoop")
uppaal_statements_Iteration = Class(name="uppaal_statements_Iteration")
statements_Statement = Class(name="statements_Statement")
uppaal_templates_Selection = Class(name="uppaal_templates_Selection")
uppaal_statements_Statement = Class(name="uppaal_statements_Statement", is_abstract=True)
uppaal_statements_Block = Class(name="uppaal_statements_Block")
Statement = Class(name="Statement")
uppaal_statements_DoWhileLoop = Class(name="uppaal_statements_DoWhileLoop")
uppaal_statements_IfStatement = Class(name="uppaal_statements_IfStatement")
uppaal_statements_WhileLoop = Class(name="uppaal_statements_WhileLoop")
uppaal_expressions_Expression = Class(name="uppaal_expressions_Expression", is_abstract=True)
uppaal_expressions_NegationExpression = Class(name="uppaal_expressions_NegationExpression")
uppaal_expressions_PlusExpression = Class(name="uppaal_expressions_PlusExpression")
uppaal_expressions_MinusExpression = Class(name="uppaal_expressions_MinusExpression")
uppaal_statements_ReturnStatement = Class(name="uppaal_statements_ReturnStatement")
uppaal_statements_ExpressionStatement = Class(name="uppaal_statements_ExpressionStatement")
uppaal_expressions_IdentifierExpression = Class(name="uppaal_expressions_IdentifierExpression")
uppaal_expressions_LiteralExpression = Class(name="uppaal_expressions_LiteralExpression")
uppaal_expressions_BinaryExpression = Class(name="uppaal_expressions_BinaryExpression", is_abstract=True)
uppaal_expressions_AssignmentExpression = Class(name="uppaal_expressions_AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
uppaal_expressions_CompareExpression = Class(name="uppaal_expressions_CompareExpression")
uppaal_expressions_ConditionExpression = Class(name="uppaal_expressions_ConditionExpression")
uppaal_expressions_ArithmeticExpression = Class(name="uppaal_expressions_ArithmeticExpression")
uppaal_expressions_LogicalExpression = Class(name="uppaal_expressions_LogicalExpression")
uppaal_expressions_FunctionCallExpression = Class(name="uppaal_expressions_FunctionCallExpression")
uppaal_expressions_QuantificationExpression = Class(name="uppaal_expressions_QuantificationExpression")
expressions_Expression = Class(name="expressions_Expression")
uppaal_expressions_IncrementDecrementExpression = Class(name="uppaal_expressions_IncrementDecrementExpression")
uppaal_expressions_ScopedIdentifierExpression = Class(name="uppaal_expressions_ScopedIdentifierExpression")
uppaal_expressions_BitwiseExpression = Class(name="uppaal_expressions_BitwiseExpression")
uppaal_visuals_ColoredElement = Class(name="uppaal_visuals_ColoredElement", is_abstract=True)
uppaal_expressions_BitShiftExpression = Class(name="uppaal_expressions_BitShiftExpression")
uppaal_expressions_MinMaxExpression = Class(name="uppaal_expressions_MinMaxExpression")
uppaal_visuals_PlanarElement = Class(name="uppaal_visuals_PlanarElement", is_abstract=True)
Point = Class(name="Point")
uppaal_visuals_LinearElement = Class(name="uppaal_visuals_LinearElement", is_abstract=True)
uppaal_visuals_Point = Class(name="uppaal_visuals_Point")

# uppaal_NTA class attributes and methods

# core_NamedElement class attributes and methods

# core_CommentableElement class attributes and methods

# GlobalDeclarations class attributes and methods

# uppaal_core_NamedElement class attributes and methods
uppaal_core_NamedElement_name: Property = Property(name="name", type=StringType)
uppaal_core_NamedElement.attributes={uppaal_core_NamedElement_name}

# Template class attributes and methods

# SystemDeclarations class attributes and methods

# PredefinedType class attributes and methods

# uppaal_types_DeclaredType class attributes and methods

# TypeDeclaration class attributes and methods

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

# uppaal_types_StructTypeSpecification class attributes and methods

# DataVariableDeclaration class attributes and methods

# uppaal_types_RangeTypeSpecification class attributes and methods

# IntegerBounds class attributes and methods

# uppaal_types_IntegerBounds class attributes and methods

# TypeDefinition class attributes and methods

# uppaal_types_TypeDefinition class attributes and methods
uppaal_types_TypeDefinition_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_TypeDefinition.attributes={uppaal_types_TypeDefinition_baseType}

# uppaal_types_TypeReference class attributes and methods

# uppaal_types_TypeSpecification class attributes and methods

# uppaal_types_ScalarTypeSpecification class attributes and methods

# TypeSpecification class attributes and methods

# Expression class attributes and methods

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

# uppaal_declarations_Declarations class attributes and methods

# Declaration class attributes and methods

# uppaal_declarations_GlobalDeclarations class attributes and methods

# Declarations class attributes and methods

# global_ChannelPriority class attributes and methods

# uppaal_declarations_LocalDeclarations class attributes and methods

# uppaal_declarations_SystemDeclarations class attributes and methods

# Block class attributes and methods

# Parameter class attributes and methods

# uppaal_declarations_TypeDeclaration class attributes and methods

# DeclaredType class attributes and methods

# uppaal_declarations_Variable class attributes and methods

# uppaal_declarations_ClockVariableDeclaration class attributes and methods

# uppaal_declarations_DataVariableDeclaration class attributes and methods
uppaal_declarations_DataVariableDeclaration_prefix: Property = Property(name="prefix", type=StringType)
uppaal_declarations_DataVariableDeclaration.attributes={uppaal_declarations_DataVariableDeclaration_prefix}

# uppaal_declarations_FunctionDeclaration class attributes and methods

# Function class attributes and methods

# uppaal_declarations_Function class attributes and methods

# uppaal_declarations_ValueIndex class attributes and methods

# uppaal_declarations_TypeIndex class attributes and methods

# uppaal_declarations_VariableContainer class attributes and methods

# VariableContainer class attributes and methods

# Initializer class attributes and methods

# uppaal_declarations_Index class attributes and methods

# uppaal_declarations_ExpressionInitializer class attributes and methods

# uppaal_declarations_ArrayInitializer class attributes and methods

# uppaal_global_ChannelPriority class attributes and methods

# global_ChannelPriorityItem class attributes and methods

# uppaal_global_ChannelPriorityItem class attributes and methods

# uppaal_global_ChannelList class attributes and methods

# ChannelPriorityItem class attributes and methods

# Variable class attributes and methods

# uppaal_declarations_Parameter class attributes and methods
uppaal_declarations_Parameter_callType: Property = Property(name="callType", type=StringType)
uppaal_declarations_Parameter.attributes={uppaal_declarations_Parameter_callType}

# uppaal_declarations_Initializer class attributes and methods

# uppaal_system_System class attributes and methods

# system_InstantiationList class attributes and methods

# uppaal_system_InstantiationList class attributes and methods

# AbstractTemplate class attributes and methods

# uppaal_system_ProgressMeasure class attributes and methods

# IdentifierExpression class attributes and methods

# uppaal_global_DefaultChannelPriority class attributes and methods

# uppaal_system_TemplateDeclaration class attributes and methods

# RedefinedTemplate class attributes and methods

# Location class attributes and methods

# Edge class attributes and methods

# uppaal_templates_RedefinedTemplate class attributes and methods

# uppaal_templates_AbstractTemplate class attributes and methods

# uppaal_templates_Template class attributes and methods

# LocalDeclarations class attributes and methods

# uppaal_templates_Location class attributes and methods
uppaal_templates_Location_locationTimeKind: Property = Property(name="locationTimeKind", type=StringType)
uppaal_templates_Location.attributes={uppaal_templates_Location_locationTimeKind}

# visuals_PlanarElement class attributes and methods

# visuals_ColoredElement class attributes and methods

# system_TemplateDeclaration class attributes and methods

# Synchronization class attributes and methods

# Selection class attributes and methods

# uppaal_templates_Synchronization class attributes and methods
uppaal_templates_Synchronization_kind: Property = Property(name="kind", type=StringType)
uppaal_templates_Synchronization.attributes={uppaal_templates_Synchronization_kind}

# uppaal_templates_Edge class attributes and methods

# visuals_LinearElement class attributes and methods

# uppaal_statements_EmptyStatement class attributes and methods

# uppaal_statements_ForLoop class attributes and methods

# uppaal_statements_Iteration class attributes and methods

# statements_Statement class attributes and methods

# uppaal_templates_Selection class attributes and methods

# uppaal_statements_Statement class attributes and methods

# uppaal_statements_Block class attributes and methods

# Statement class attributes and methods

# uppaal_statements_DoWhileLoop class attributes and methods

# uppaal_statements_IfStatement class attributes and methods

# uppaal_statements_WhileLoop class attributes and methods

# uppaal_expressions_Expression class attributes and methods

# uppaal_expressions_NegationExpression class attributes and methods

# uppaal_expressions_PlusExpression class attributes and methods

# uppaal_expressions_MinusExpression class attributes and methods

# uppaal_statements_ReturnStatement class attributes and methods

# uppaal_statements_ExpressionStatement class attributes and methods

# uppaal_expressions_IdentifierExpression class attributes and methods

# uppaal_expressions_LiteralExpression class attributes and methods
uppaal_expressions_LiteralExpression_text: Property = Property(name="text", type=StringType)
uppaal_expressions_LiteralExpression.attributes={uppaal_expressions_LiteralExpression_text}

# uppaal_expressions_BinaryExpression class attributes and methods

# uppaal_expressions_AssignmentExpression class attributes and methods
uppaal_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_AssignmentExpression.attributes={uppaal_expressions_AssignmentExpression_operator}

# BinaryExpression class attributes and methods

# uppaal_expressions_CompareExpression class attributes and methods
uppaal_expressions_CompareExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_CompareExpression.attributes={uppaal_expressions_CompareExpression_operator}

# uppaal_expressions_ConditionExpression class attributes and methods

# uppaal_expressions_ArithmeticExpression class attributes and methods
uppaal_expressions_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_ArithmeticExpression.attributes={uppaal_expressions_ArithmeticExpression_operator}

# uppaal_expressions_LogicalExpression class attributes and methods
uppaal_expressions_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_LogicalExpression.attributes={uppaal_expressions_LogicalExpression_operator}

# uppaal_expressions_FunctionCallExpression class attributes and methods

# uppaal_expressions_QuantificationExpression class attributes and methods
uppaal_expressions_QuantificationExpression_quantifier: Property = Property(name="quantifier", type=StringType)
uppaal_expressions_QuantificationExpression.attributes={uppaal_expressions_QuantificationExpression_quantifier}

# expressions_Expression class attributes and methods

# uppaal_expressions_IncrementDecrementExpression class attributes and methods
uppaal_expressions_IncrementDecrementExpression_position: Property = Property(name="position", type=StringType)
uppaal_expressions_IncrementDecrementExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_IncrementDecrementExpression.attributes={uppaal_expressions_IncrementDecrementExpression_position, uppaal_expressions_IncrementDecrementExpression_operator}

# uppaal_expressions_ScopedIdentifierExpression class attributes and methods

# uppaal_expressions_BitwiseExpression class attributes and methods
uppaal_expressions_BitwiseExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitwiseExpression.attributes={uppaal_expressions_BitwiseExpression_operator}

# uppaal_visuals_ColoredElement class attributes and methods
uppaal_visuals_ColoredElement_color: Property = Property(name="color", type=StringType)
uppaal_visuals_ColoredElement_colorCode: Property = Property(name="colorCode", type=StringType)
uppaal_visuals_ColoredElement.attributes={uppaal_visuals_ColoredElement_color, uppaal_visuals_ColoredElement_colorCode}

# uppaal_expressions_BitShiftExpression class attributes and methods
uppaal_expressions_BitShiftExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitShiftExpression.attributes={uppaal_expressions_BitShiftExpression_operator}

# uppaal_expressions_MinMaxExpression class attributes and methods
uppaal_expressions_MinMaxExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_MinMaxExpression.attributes={uppaal_expressions_MinMaxExpression_operator}

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
        Property(name="GlobalDeclarations", type=uppaal_NTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NTA", type=GlobalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
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
typeDeclaration20: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration20",
    ends={
        Property(name="TypeDeclaration", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
index19: BinaryAssociation = BinaryAssociation(
    name="index19",
    ends={
        Property(name="Index", type=uppaal_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Type", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
parameter41: BinaryAssociation = BinaryAssociation(
    name="parameter41",
    ends={
        Property(name="Parameter", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function42", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="DeclaredType", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDeclaration", type=DeclaredType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition44: BinaryAssociation = BinaryAssociation(
    name="typeDefinition44",
    ends={
        Property(name="TypeDefinition45", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeDeclaration", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function36: BinaryAssociation = BinaryAssociation(
    name="function36",
    ends={
        Property(name="Function", type=uppaal_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_FunctionDeclaration", type=Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sizeExpression54: BinaryAssociation = BinaryAssociation(
    name="sizeExpression54",
    ends={
        Property(name="Expression55", type=uppaal_declarations_ValueIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ValueIndex", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeDefinition56: BinaryAssociation = BinaryAssociation(
    name="typeDefinition56",
    ends={
        Property(name="TypeDefinition57", type=uppaal_declarations_TypeIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeIndex", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index46: BinaryAssociation = BinaryAssociation(
    name="index46",
    ends={
        Property(name="Index47", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container48: BinaryAssociation = BinaryAssociation(
    name="container48",
    ends={
        Property(name="VariableContainer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=VariableContainer, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition49: BinaryAssociation = BinaryAssociation(
    name="typeDefinition49",
    ends={
        Property(name="TypeDefinition51", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable50", type=TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
initializer52: BinaryAssociation = BinaryAssociation(
    name="initializer52",
    ends={
        Property(name="Initializer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable53", type=Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression62: BinaryAssociation = BinaryAssociation(
    name="expression62",
    ends={
        Property(name="Expression63", type=uppaal_declarations_ExpressionInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ExpressionInitializer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer64: BinaryAssociation = BinaryAssociation(
    name="initializer64",
    ends={
        Property(name="Initializer65", type=uppaal_declarations_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ArrayInitializer", type=Initializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
item66: BinaryAssociation = BinaryAssociation(
    name="item66",
    ends={
        Property(name="global_ChannelPriorityItem", type=uppaal_global_ChannelPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriority", type=global_ChannelPriorityItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition58: BinaryAssociation = BinaryAssociation(
    name="typeDefinition58",
    ends={
        Property(name="TypeDefinition59", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_VariableContainer", type=TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable60: BinaryAssociation = BinaryAssociation(
    name="variable60",
    ends={
        Property(name="Variable", type=uppaal_declarations_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableDeclaration61: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration61",
    ends={
        Property(name="VariableDeclaration", type=uppaal_declarations_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Parameter", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument69: BinaryAssociation = BinaryAssociation(
    name="argument69",
    ends={
        Property(name="Expression70", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_TemplateDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiationList71: BinaryAssociation = BinaryAssociation(
    name="instantiationList71",
    ends={
        Property(name="system_InstantiationList", type=uppaal_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_System", type=system_InstantiationList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template72: BinaryAssociation = BinaryAssociation(
    name="template72",
    ends={
        Property(name="AbstractTemplate", type=uppaal_system_InstantiationList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_InstantiationList", type=AbstractTemplate, multiplicity=Multiplicity(1, 9999))
    }
)
expression73: BinaryAssociation = BinaryAssociation(
    name="expression73",
    ends={
        Property(name="Expression74", type=uppaal_system_ProgressMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_ProgressMeasure", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
channelExpression67: BinaryAssociation = BinaryAssociation(
    name="channelExpression67",
    ends={
        Property(name="IdentifierExpression", type=uppaal_global_ChannelList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelList", type=IdentifierExpression, multiplicity=Multiplicity(1, 9999))
    }
)
declaredTemplate68: BinaryAssociation = BinaryAssociation(
    name="declaredTemplate68",
    ends={
        Property(name="RedefinedTemplate", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=RedefinedTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location78: BinaryAssociation = BinaryAssociation(
    name="location78",
    ends={
        Property(name="Location", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTemplate", type=Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edge79: BinaryAssociation = BinaryAssociation(
    name="edge79",
    ends={
        Property(name="Edge", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTemplate80", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init81: BinaryAssociation = BinaryAssociation(
    name="init81",
    ends={
        Property(name="Location83", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template82", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
referredTemplate84: BinaryAssociation = BinaryAssociation(
    name="referredTemplate84",
    ends={
        Property(name="AbstractTemplate85", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_RedefinedTemplate", type=AbstractTemplate, multiplicity=Multiplicity(1, 1))
    }
)
parameter75: BinaryAssociation = BinaryAssociation(
    name="parameter75",
    ends={
        Property(name="Parameter76", type=uppaal_templates_AbstractTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_AbstractTemplate", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations77: BinaryAssociation = BinaryAssociation(
    name="declarations77",
    ends={
        Property(name="LocalDeclarations", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentTemplate87: BinaryAssociation = BinaryAssociation(
    name="parentTemplate87",
    ends={
        Property(name="Template88", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
invariant89: BinaryAssociation = BinaryAssociation(
    name="invariant89",
    ends={
        Property(name="Expression90", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Location", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration86: BinaryAssociation = BinaryAssociation(
    name="declaration86",
    ends={
        Property(name="TemplateDeclaration", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="declaredTemplate", type=system_TemplateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
guard98: BinaryAssociation = BinaryAssociation(
    name="guard98",
    ends={
        Property(name="Expression100", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge99", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
update101: BinaryAssociation = BinaryAssociation(
    name="update101",
    ends={
        Property(name="Expression103", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge102", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization104: BinaryAssociation = BinaryAssociation(
    name="synchronization104",
    ends={
        Property(name="Synchronization", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge105", type=Synchronization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection106: BinaryAssociation = BinaryAssociation(
    name="selection106",
    ends={
        Property(name="Selection", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge107", type=Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelExpression108: BinaryAssociation = BinaryAssociation(
    name="channelExpression108",
    ends={
        Property(name="IdentifierExpression109", type=uppaal_templates_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Synchronization", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source91: BinaryAssociation = BinaryAssociation(
    name="source91",
    ends={
        Property(name="Location92", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
target93: BinaryAssociation = BinaryAssociation(
    name="target93",
    ends={
        Property(name="Location95", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge94", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate96: BinaryAssociation = BinaryAssociation(
    name="parentTemplate96",
    ends={
        Property(name="Template97", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
statement112: BinaryAssociation = BinaryAssociation(
    name="statement112",
    ends={
        Property(name="Statement", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block113", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialization114: BinaryAssociation = BinaryAssociation(
    name="initialization114",
    ends={
        Property(name="Expression115", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition116: BinaryAssociation = BinaryAssociation(
    name="condition116",
    ends={
        Property(name="Expression118", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop117", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteration119: BinaryAssociation = BinaryAssociation(
    name="iteration119",
    ends={
        Property(name="Expression121", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop120", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement122: BinaryAssociation = BinaryAssociation(
    name="statement122",
    ends={
        Property(name="Statement124", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop123", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations110: BinaryAssociation = BinaryAssociation(
    name="declarations110",
    ends={
        Property(name="LocalDeclarations111", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement132: BinaryAssociation = BinaryAssociation(
    name="statement132",
    ends={
        Property(name="Statement133", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="Expression136", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop135", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression137: BinaryAssociation = BinaryAssociation(
    name="ifExpression137",
    ends={
        Property(name="Expression138", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement139: BinaryAssociation = BinaryAssociation(
    name="thenStatement139",
    ends={
        Property(name="Statement141", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement140", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement125: BinaryAssociation = BinaryAssociation(
    name="statement125",
    ends={
        Property(name="Statement126", type=uppaal_statements_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Iteration", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression127: BinaryAssociation = BinaryAssociation(
    name="expression127",
    ends={
        Property(name="Expression128", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement129: BinaryAssociation = BinaryAssociation(
    name="statement129",
    ends={
        Property(name="Statement131", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop130", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negatedExpression149: BinaryAssociation = BinaryAssociation(
    name="negatedExpression149",
    ends={
        Property(name="Expression150", type=uppaal_expressions_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_NegationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
confirmedExpression151: BinaryAssociation = BinaryAssociation(
    name="confirmedExpression151",
    ends={
        Property(name="Expression152", type=uppaal_expressions_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_PlusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement142: BinaryAssociation = BinaryAssociation(
    name="elseStatement142",
    ends={
        Property(name="Statement144", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement143", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnExpression145: BinaryAssociation = BinaryAssociation(
    name="returnExpression145",
    ends={
        Property(name="Expression146", type=uppaal_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression147: BinaryAssociation = BinaryAssociation(
    name="expression147",
    ends={
        Property(name="Expression148", type=uppaal_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier160: BinaryAssociation = BinaryAssociation(
    name="identifier160",
    ends={
        Property(name="NamedElement", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
index161: BinaryAssociation = BinaryAssociation(
    name="index161",
    ends={
        Property(name="Expression163", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression162", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invertedExpression153: BinaryAssociation = BinaryAssociation(
    name="invertedExpression153",
    ends={
        Property(name="Expression154", type=uppaal_expressions_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_MinusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstExpr155: BinaryAssociation = BinaryAssociation(
    name="firstExpr155",
    ends={
        Property(name="Expression156", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
secondExpr157: BinaryAssociation = BinaryAssociation(
    name="secondExpr157",
    ends={
        Property(name="Expression159", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression158", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function164: BinaryAssociation = BinaryAssociation(
    name="function164",
    ends={
        Property(name="Function165", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
argument166: BinaryAssociation = BinaryAssociation(
    name="argument166",
    ends={
        Property(name="Expression168", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression167", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression182: BinaryAssociation = BinaryAssociation(
    name="expression182",
    ends={
        Property(name="Expression183", type=uppaal_expressions_QuantificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_QuantificationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression184: BinaryAssociation = BinaryAssociation(
    name="expression184",
    ends={
        Property(name="Expression185", type=uppaal_expressions_IncrementDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IncrementDecrementExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression169: BinaryAssociation = BinaryAssociation(
    name="ifExpression169",
    ends={
        Property(name="Expression170", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression171: BinaryAssociation = BinaryAssociation(
    name="thenExpression171",
    ends={
        Property(name="Expression173", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression172", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression174: BinaryAssociation = BinaryAssociation(
    name="elseExpression174",
    ends={
        Property(name="Expression176", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression175", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scope177: BinaryAssociation = BinaryAssociation(
    name="scope177",
    ends={
        Property(name="Expression178", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier179: BinaryAssociation = BinaryAssociation(
    name="identifier179",
    ends={
        Property(name="IdentifierExpression181", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression180", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position186: BinaryAssociation = BinaryAssociation(
    name="position186",
    ends={
        Property(name="Point", type=uppaal_visuals_PlanarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_PlanarElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bendPoint187: BinaryAssociation = BinaryAssociation(
    name="bendPoint187",
    ends={
        Property(name="Point188", type=uppaal_visuals_LinearElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_LinearElement", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uppaal_NTA_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_NTA)
gen_uppaal_NTA_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_NTA)
gen_uppaal_types_DeclaredType_Type = Generalization(general=Type, specific=uppaal_types_DeclaredType)
gen_uppaal_types_Type_NamedElement = Generalization(general=NamedElement, specific=uppaal_types_Type)
gen_uppaal_types_PredefinedType_Type = Generalization(general=Type, specific=uppaal_types_PredefinedType)
gen_uppaal_types_StructTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_StructTypeSpecification)
gen_uppaal_types_RangeTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_RangeTypeSpecification)
gen_uppaal_types_TypeReference_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeReference)
gen_uppaal_types_TypeSpecification_TypeDefinition = Generalization(general=TypeDefinition, specific=uppaal_types_TypeSpecification)
gen_uppaal_types_ScalarTypeSpecification_TypeSpecification = Generalization(general=TypeSpecification, specific=uppaal_types_ScalarTypeSpecification)
gen_uppaal_declarations_VariableDeclaration_declarations_Declaration = Generalization(general=declarations_Declaration, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_declarations_VariableDeclaration)
gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ChannelVariableDeclaration)
gen_uppaal_declarations_GlobalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_GlobalDeclarations)
gen_uppaal_declarations_LocalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_LocalDeclarations)
gen_uppaal_declarations_SystemDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_SystemDeclarations)
gen_uppaal_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_TypeDeclaration)
gen_uppaal_declarations_Variable_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_ClockVariableDeclaration)
gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=uppaal_declarations_DataVariableDeclaration)
gen_uppaal_declarations_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_FunctionDeclaration)
gen_uppaal_declarations_Function_NamedElement = Generalization(general=NamedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_ValueIndex_Index = Generalization(general=Index, specific=uppaal_declarations_ValueIndex)
gen_uppaal_declarations_TypeIndex_Index = Generalization(general=Index, specific=uppaal_declarations_TypeIndex)
gen_uppaal_declarations_ExpressionInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ExpressionInitializer)
gen_uppaal_declarations_ArrayInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ArrayInitializer)
gen_uppaal_global_ChannelList_ChannelPriorityItem = Generalization(general=ChannelPriorityItem, specific=uppaal_global_ChannelList)
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
gen_uppaal_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_EmptyStatement)
gen_uppaal_statements_ForLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_ForLoop)
gen_uppaal_statements_Iteration_statements_Statement = Generalization(general=statements_Statement, specific=uppaal_statements_Iteration)
gen_uppaal_statements_Iteration_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_statements_Iteration)
gen_uppaal_templates_Selection_VariableContainer = Generalization(general=VariableContainer, specific=uppaal_templates_Selection)
gen_uppaal_statements_Block_Statement = Generalization(general=Statement, specific=uppaal_statements_Block)
gen_uppaal_statements_DoWhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_DoWhileLoop)
gen_uppaal_statements_IfStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_IfStatement)
gen_uppaal_statements_WhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_WhileLoop)
gen_uppaal_expressions_NegationExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_NegationExpression)
gen_uppaal_expressions_PlusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_PlusExpression)
gen_uppaal_expressions_MinusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_MinusExpression)
gen_uppaal_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ReturnStatement)
gen_uppaal_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ExpressionStatement)
gen_uppaal_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IdentifierExpression)
gen_uppaal_expressions_LiteralExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_LiteralExpression)
gen_uppaal_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_BinaryExpression)
gen_uppaal_expressions_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_AssignmentExpression)
gen_uppaal_expressions_CompareExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_CompareExpression)
gen_uppaal_expressions_ConditionExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ConditionExpression)
gen_uppaal_expressions_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_ArithmeticExpression)
gen_uppaal_expressions_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_LogicalExpression)
gen_uppaal_expressions_FunctionCallExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_FunctionCallExpression)
gen_uppaal_expressions_QuantificationExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer = Generalization(general=declarations_VariableContainer, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_IncrementDecrementExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IncrementDecrementExpression)
gen_uppaal_expressions_ScopedIdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ScopedIdentifierExpression)
gen_uppaal_expressions_BitwiseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitwiseExpression)
gen_uppaal_expressions_BitShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitShiftExpression)
gen_uppaal_expressions_MinMaxExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_MinMaxExpression)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={uppaal_NTA, core_NamedElement, core_CommentableElement, GlobalDeclarations, uppaal_core_NamedElement, Template, SystemDeclarations, PredefinedType, uppaal_types_DeclaredType, TypeDeclaration, uppaal_core_CommentableElement, uppaal_types_Type, NamedElement, Index, uppaal_types_PredefinedType, Type, uppaal_types_StructTypeSpecification, DataVariableDeclaration, uppaal_types_RangeTypeSpecification, IntegerBounds, uppaal_types_IntegerBounds, TypeDefinition, uppaal_types_TypeDefinition, uppaal_types_TypeReference, uppaal_types_TypeSpecification, uppaal_types_ScalarTypeSpecification, TypeSpecification, Expression, system_System, system_ProgressMeasure, uppaal_declarations_Declaration, uppaal_declarations_VariableDeclaration, declarations_Declaration, declarations_VariableContainer, uppaal_declarations_ChannelVariableDeclaration, VariableDeclaration, uppaal_declarations_Declarations, Declaration, uppaal_declarations_GlobalDeclarations, Declarations, global_ChannelPriority, uppaal_declarations_LocalDeclarations, uppaal_declarations_SystemDeclarations, Block, Parameter_, uppaal_declarations_TypeDeclaration, DeclaredType, uppaal_declarations_Variable, uppaal_declarations_ClockVariableDeclaration, uppaal_declarations_DataVariableDeclaration, uppaal_declarations_FunctionDeclaration, Function, uppaal_declarations_Function, uppaal_declarations_ValueIndex, uppaal_declarations_TypeIndex, uppaal_declarations_VariableContainer, VariableContainer, Initializer, uppaal_declarations_Index, uppaal_declarations_ExpressionInitializer, uppaal_declarations_ArrayInitializer, uppaal_global_ChannelPriority, global_ChannelPriorityItem, uppaal_global_ChannelPriorityItem, uppaal_global_ChannelList, ChannelPriorityItem, Variable, uppaal_declarations_Parameter, uppaal_declarations_Initializer, uppaal_system_System, system_InstantiationList, uppaal_system_InstantiationList, AbstractTemplate, uppaal_system_ProgressMeasure, IdentifierExpression, uppaal_global_DefaultChannelPriority, uppaal_system_TemplateDeclaration, RedefinedTemplate, Location, Edge, uppaal_templates_RedefinedTemplate, uppaal_templates_AbstractTemplate, uppaal_templates_Template, LocalDeclarations, uppaal_templates_Location, visuals_PlanarElement, visuals_ColoredElement, system_TemplateDeclaration, Synchronization, Selection, uppaal_templates_Synchronization, uppaal_templates_Edge, visuals_LinearElement, uppaal_statements_EmptyStatement, uppaal_statements_ForLoop, uppaal_statements_Iteration, statements_Statement, uppaal_templates_Selection, uppaal_statements_Statement, uppaal_statements_Block, Statement, uppaal_statements_DoWhileLoop, uppaal_statements_IfStatement, uppaal_statements_WhileLoop, uppaal_expressions_Expression, uppaal_expressions_NegationExpression, uppaal_expressions_PlusExpression, uppaal_expressions_MinusExpression, uppaal_statements_ReturnStatement, uppaal_statements_ExpressionStatement, uppaal_expressions_IdentifierExpression, uppaal_expressions_LiteralExpression, uppaal_expressions_BinaryExpression, uppaal_expressions_AssignmentExpression, BinaryExpression, uppaal_expressions_CompareExpression, uppaal_expressions_ConditionExpression, uppaal_expressions_ArithmeticExpression, uppaal_expressions_LogicalExpression, uppaal_expressions_FunctionCallExpression, uppaal_expressions_QuantificationExpression, expressions_Expression, uppaal_expressions_IncrementDecrementExpression, uppaal_expressions_ScopedIdentifierExpression, uppaal_expressions_BitwiseExpression, uppaal_visuals_ColoredElement, uppaal_expressions_BitShiftExpression, uppaal_expressions_MinMaxExpression, uppaal_visuals_PlanarElement, Point, uppaal_visuals_LinearElement, uppaal_visuals_Point, BuiltInType, DataVariablePrefix, CallType, SynchronizationKind, LocationKind, AssignmentOperator, CompareOperator, ArithmeticOperator, LogicalOperator, Quantifier, MinMaxOperator, BitwiseOperator, IncrementDecrementOperator, IncrementDecrementPosition, BitShiftOperator, ColorKind},
    associations={globalDeclarations0, bool7, clock10, chan13, void16, template1, systemDeclarations3, int5, typeDeclaration20, index19, sizeExpression23, declaration24, bounds25, lowerBound26, upperBound28, typeDefinition21, referredType22, system33, progressMeasure34, declaration31, channelPriority32, returnType37, block39, parameter41, type43, typeDefinition44, function36, sizeExpression54, typeDefinition56, index46, container48, typeDefinition49, initializer52, expression62, initializer64, item66, typeDefinition58, variable60, variableDeclaration61, argument69, instantiationList71, template72, expression73, channelExpression67, declaredTemplate68, location78, edge79, init81, referredTemplate84, parameter75, declarations77, parentTemplate87, invariant89, declaration86, guard98, update101, synchronization104, selection106, channelExpression108, source91, target93, parentTemplate96, statement112, initialization114, condition116, iteration119, statement122, declarations110, statement132, expression134, ifExpression137, thenStatement139, statement125, expression127, statement129, negatedExpression149, confirmedExpression151, elseStatement142, returnExpression145, expression147, identifier160, index161, invertedExpression153, firstExpr155, secondExpr157, function164, argument166, expression182, expression184, ifExpression169, thenExpression171, elseExpression174, scope177, identifier179, position186, bendPoint187},
    generalizations={gen_uppaal_NTA_core_NamedElement, gen_uppaal_NTA_core_CommentableElement, gen_uppaal_types_DeclaredType_Type, gen_uppaal_types_Type_NamedElement, gen_uppaal_types_PredefinedType_Type, gen_uppaal_types_StructTypeSpecification_TypeSpecification, gen_uppaal_types_RangeTypeSpecification_TypeSpecification, gen_uppaal_types_TypeReference_TypeDefinition, gen_uppaal_types_TypeSpecification_TypeDefinition, gen_uppaal_types_ScalarTypeSpecification_TypeSpecification, gen_uppaal_declarations_VariableDeclaration_declarations_Declaration, gen_uppaal_declarations_VariableDeclaration_declarations_VariableContainer, gen_uppaal_declarations_ChannelVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_GlobalDeclarations_Declarations, gen_uppaal_declarations_LocalDeclarations_Declarations, gen_uppaal_declarations_SystemDeclarations_Declarations, gen_uppaal_declarations_TypeDeclaration_Declaration, gen_uppaal_declarations_Variable_NamedElement, gen_uppaal_declarations_ClockVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_DataVariableDeclaration_VariableDeclaration, gen_uppaal_declarations_FunctionDeclaration_Declaration, gen_uppaal_declarations_Function_NamedElement, gen_uppaal_declarations_ValueIndex_Index, gen_uppaal_declarations_TypeIndex_Index, gen_uppaal_declarations_ExpressionInitializer_Initializer, gen_uppaal_declarations_ArrayInitializer_Initializer, gen_uppaal_global_ChannelList_ChannelPriorityItem, gen_uppaal_global_DefaultChannelPriority_ChannelPriorityItem, gen_uppaal_system_TemplateDeclaration_Declaration, gen_uppaal_templates_RedefinedTemplate_AbstractTemplate, gen_uppaal_templates_AbstractTemplate_core_NamedElement, gen_uppaal_templates_AbstractTemplate_core_CommentableElement, gen_uppaal_templates_Template_AbstractTemplate, gen_uppaal_templates_Location_core_NamedElement, gen_uppaal_templates_Location_core_CommentableElement, gen_uppaal_templates_Location_visuals_PlanarElement, gen_uppaal_templates_Location_visuals_ColoredElement, gen_uppaal_templates_Edge_visuals_LinearElement, gen_uppaal_templates_Edge_core_CommentableElement, gen_uppaal_templates_Edge_visuals_ColoredElement, gen_uppaal_statements_EmptyStatement_Statement, gen_uppaal_statements_ForLoop_Statement, gen_uppaal_statements_Iteration_statements_Statement, gen_uppaal_statements_Iteration_declarations_VariableContainer, gen_uppaal_templates_Selection_VariableContainer, gen_uppaal_statements_Block_Statement, gen_uppaal_statements_DoWhileLoop_Statement, gen_uppaal_statements_IfStatement_Statement, gen_uppaal_statements_WhileLoop_Statement, gen_uppaal_expressions_NegationExpression_Expression, gen_uppaal_expressions_PlusExpression_Expression, gen_uppaal_expressions_MinusExpression_Expression, gen_uppaal_statements_ReturnStatement_Statement, gen_uppaal_statements_ExpressionStatement_Statement, gen_uppaal_expressions_IdentifierExpression_Expression, gen_uppaal_expressions_LiteralExpression_Expression, gen_uppaal_expressions_BinaryExpression_Expression, gen_uppaal_expressions_AssignmentExpression_BinaryExpression, gen_uppaal_expressions_CompareExpression_BinaryExpression, gen_uppaal_expressions_ConditionExpression_Expression, gen_uppaal_expressions_ArithmeticExpression_BinaryExpression, gen_uppaal_expressions_LogicalExpression_BinaryExpression, gen_uppaal_expressions_FunctionCallExpression_Expression, gen_uppaal_expressions_QuantificationExpression_expressions_Expression, gen_uppaal_expressions_QuantificationExpression_declarations_VariableContainer, gen_uppaal_expressions_IncrementDecrementExpression_Expression, gen_uppaal_expressions_ScopedIdentifierExpression_Expression, gen_uppaal_expressions_BitwiseExpression_BinaryExpression, gen_uppaal_expressions_BitShiftExpression_BinaryExpression, gen_uppaal_expressions_MinMaxExpression_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)