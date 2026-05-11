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

IncrementDecrementOperator: Enumeration = Enumeration(
    name="IncrementDecrementOperator",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
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
GlobalDeclarations = Class(name="GlobalDeclarations")
Template = Class(name="Template")
SystemDeclarations = Class(name="SystemDeclarations")
uppaal_NTA = Class(name="uppaal_NTA")
core_NamedElement = Class(name="core_NamedElement")
core_CommentableElement = Class(name="core_CommentableElement")
uppaal_types_PredefinedType = Class(name="uppaal_types_PredefinedType")
Type = Class(name="Type")
uppaal_types_DeclaredType = Class(name="uppaal_types_DeclaredType")
TypeDeclaration = Class(name="TypeDeclaration")
uppaal_core_NamedElement = Class(name="uppaal_core_NamedElement", is_abstract=True)
uppaal_core_CommentableElement = Class(name="uppaal_core_CommentableElement", is_abstract=True)
uppaal_core_TypedElement = Class(name="uppaal_core_TypedElement", is_abstract=True)
TypedElementContainer = Class(name="TypedElementContainer")
Expression = Class(name="Expression")
uppaal_types_Type = Class(name="uppaal_types_Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
uppaal_types_Library = Class(name="uppaal_types_Library")
PredefinedType = Class(name="PredefinedType")
uppaal_declarations_Declarations = Class(name="uppaal_declarations_Declarations", is_abstract=True)
Declaration = Class(name="Declaration")
uppaal_declarations_GlobalDeclarations = Class(name="uppaal_declarations_GlobalDeclarations")
Declarations = Class(name="Declarations")
uppaal_types_TypeExpression = Class(name="uppaal_types_TypeExpression", is_abstract=True)
uppaal_types_ScalarTypeSpecification = Class(name="uppaal_types_ScalarTypeSpecification")
TypeExpression = Class(name="TypeExpression")
uppaal_types_StructTypeSpecification = Class(name="uppaal_types_StructTypeSpecification")
TypedDeclaration = Class(name="TypedDeclaration")
uppaal_types_RangeTypeSpecification = Class(name="uppaal_types_RangeTypeSpecification")
IntegerBounds = Class(name="IntegerBounds")
uppaal_types_IntegerBounds = Class(name="uppaal_types_IntegerBounds")
uppaal_declarations_Function = Class(name="uppaal_declarations_Function")
core_TypedElement = Class(name="core_TypedElement")
Block = Class(name="Block")
ParameterContainer = Class(name="ParameterContainer")
global_ChannelPriorityDeclaration = Class(name="global_ChannelPriorityDeclaration")
uppaal_declarations_LocalDeclarations = Class(name="uppaal_declarations_LocalDeclarations")
uppaal_declarations_SystemDeclarations = Class(name="uppaal_declarations_SystemDeclarations")
system_System = Class(name="system_System")
system_ProgressMeasure = Class(name="system_ProgressMeasure")
uppaal_declarations_Declaration = Class(name="uppaal_declarations_Declaration", is_abstract=True)
uppaal_declarations_Variable = Class(name="uppaal_declarations_Variable")
uppaal_declarations_TypeDeclaration = Class(name="uppaal_declarations_TypeDeclaration")
DeclaredType = Class(name="DeclaredType")
uppaal_declarations_TypedDeclaration = Class(name="uppaal_declarations_TypedDeclaration")
declarations_Declaration = Class(name="declarations_Declaration")
declarations_TypedElementContainer = Class(name="declarations_TypedElementContainer")
uppaal_declarations_ParameterContainer = Class(name="uppaal_declarations_ParameterContainer")
uppaal_global_ChannelPriorityDeclaration = Class(name="uppaal_global_ChannelPriorityDeclaration")
Initializer = Class(name="Initializer")
global_ChannelPriorityGroup = Class(name="global_ChannelPriorityGroup")
uppaal_declarations_TypedElementContainer = Class(name="uppaal_declarations_TypedElementContainer", is_abstract=True)
TypedElement = Class(name="TypedElement")
uppaal_declarations_Parameter = Class(name="uppaal_declarations_Parameter")
Variable = Class(name="Variable")
uppaal_declarations_Initializer = Class(name="uppaal_declarations_Initializer", is_abstract=True)
uppaal_declarations_ExpressionInitializer = Class(name="uppaal_declarations_ExpressionInitializer")
uppaal_declarations_ArrayInitializer = Class(name="uppaal_declarations_ArrayInitializer")
uppaal_system_System = Class(name="uppaal_system_System")
system_InstantiationList = Class(name="system_InstantiationList")
uppaal_system_InstantiationList = Class(name="uppaal_system_InstantiationList")
AbstractTemplate = Class(name="AbstractTemplate")
uppaal_system_ProgressMeasure = Class(name="uppaal_system_ProgressMeasure")
uppaal_global_ChannelPriorityGroup = Class(name="uppaal_global_ChannelPriorityGroup")
global_PriorityItem = Class(name="global_PriorityItem")
uppaal_global_PriorityItem = Class(name="uppaal_global_PriorityItem", is_abstract=True)
uppaal_global_ChannelItem = Class(name="uppaal_global_ChannelItem")
PriorityItem = Class(name="PriorityItem")
IdentifierExpression = Class(name="IdentifierExpression")
uppaal_global_DefaultItem = Class(name="uppaal_global_DefaultItem")
uppaal_system_TemplateDeclaration = Class(name="uppaal_system_TemplateDeclaration")
RedefinedTemplate = Class(name="RedefinedTemplate")
Edge = Class(name="Edge")
uppaal_templates_RedefinedTemplate = Class(name="uppaal_templates_RedefinedTemplate")
system_TemplateDeclaration = Class(name="system_TemplateDeclaration")
uppaal_templates_Location = Class(name="uppaal_templates_Location")
visuals_PlanarElement = Class(name="visuals_PlanarElement")
visuals_ColoredElement = Class(name="visuals_ColoredElement")
uppaal_templates_AbstractTemplate = Class(name="uppaal_templates_AbstractTemplate", is_abstract=True)
uppaal_templates_Template = Class(name="uppaal_templates_Template")
LocalDeclarations = Class(name="LocalDeclarations")
Location = Class(name="Location")
Synchronization = Class(name="Synchronization")
Selection = Class(name="Selection")
uppaal_templates_Edge = Class(name="uppaal_templates_Edge")
visuals_LinearElement = Class(name="visuals_LinearElement")
uppaal_statements_Statement = Class(name="uppaal_statements_Statement", is_abstract=True)
uppaal_statements_Block = Class(name="uppaal_statements_Block")
Statement = Class(name="Statement")
uppaal_templates_Synchronization = Class(name="uppaal_templates_Synchronization")
uppaal_templates_Selection = Class(name="uppaal_templates_Selection")
uppaal_statements_Iteration = Class(name="uppaal_statements_Iteration")
statements_Statement = Class(name="statements_Statement")
uppaal_statements_EmptyStatement = Class(name="uppaal_statements_EmptyStatement")
uppaal_statements_ForLoop = Class(name="uppaal_statements_ForLoop")
uppaal_statements_DoWhileLoop = Class(name="uppaal_statements_DoWhileLoop")
uppaal_statements_WhileLoop = Class(name="uppaal_statements_WhileLoop")
uppaal_statements_ExpressionStatement = Class(name="uppaal_statements_ExpressionStatement")
uppaal_expressions_Expression = Class(name="uppaal_expressions_Expression", is_abstract=True)
uppaal_expressions_NegationExpression = Class(name="uppaal_expressions_NegationExpression")
uppaal_statements_IfStatement = Class(name="uppaal_statements_IfStatement")
uppaal_statements_ReturnStatement = Class(name="uppaal_statements_ReturnStatement")
uppaal_expressions_AssignmentExpression = Class(name="uppaal_expressions_AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
uppaal_expressions_PlusExpression = Class(name="uppaal_expressions_PlusExpression")
uppaal_expressions_MinusExpression = Class(name="uppaal_expressions_MinusExpression")
uppaal_expressions_BinaryExpression = Class(name="uppaal_expressions_BinaryExpression", is_abstract=True)
uppaal_expressions_LiteralExpression = Class(name="uppaal_expressions_LiteralExpression")
uppaal_expressions_ArithmeticExpression = Class(name="uppaal_expressions_ArithmeticExpression")
uppaal_expressions_IdentifierExpression = Class(name="uppaal_expressions_IdentifierExpression")
uppaal_expressions_ScopedIdentifierExpression = Class(name="uppaal_expressions_ScopedIdentifierExpression")
uppaal_expressions_ConditionExpression = Class(name="uppaal_expressions_ConditionExpression")
uppaal_expressions_LogicalExpression = Class(name="uppaal_expressions_LogicalExpression")
uppaal_expressions_FunctionCallExpression = Class(name="uppaal_expressions_FunctionCallExpression")
Function = Class(name="Function")
uppaal_expressions_CompareExpression = Class(name="uppaal_expressions_CompareExpression")
uppaal_expressions_IncrementDecrementExpression = Class(name="uppaal_expressions_IncrementDecrementExpression", is_abstract=True)
uppaal_expressions_QuantificationExpression = Class(name="uppaal_expressions_QuantificationExpression")
expressions_Expression = Class(name="expressions_Expression")
uppaal_expressions_MinMaxExpression = Class(name="uppaal_expressions_MinMaxExpression")
uppaal_expressions_PreIncrementDecrementExpression = Class(name="uppaal_expressions_PreIncrementDecrementExpression")
IncrementDecrementExpression = Class(name="IncrementDecrementExpression")
uppaal_expressions_PostIncrementDecrementExpression = Class(name="uppaal_expressions_PostIncrementDecrementExpression")
uppaal_expressions_BitShiftExpression = Class(name="uppaal_expressions_BitShiftExpression")
uppaal_expressions_DataPrefixExpression = Class(name="uppaal_expressions_DataPrefixExpression")
uppaal_expressions_BitwiseExpression = Class(name="uppaal_expressions_BitwiseExpression")
uppaal_expressions_ChannelPrefixExpression = Class(name="uppaal_expressions_ChannelPrefixExpression")
uppaal_visuals_ColoredElement = Class(name="uppaal_visuals_ColoredElement", is_abstract=True)
uppaal_visuals_PlanarElement = Class(name="uppaal_visuals_PlanarElement", is_abstract=True)
Point = Class(name="Point")
uppaal_visuals_LinearElement = Class(name="uppaal_visuals_LinearElement", is_abstract=True)
uppaal_visuals_Point = Class(name="uppaal_visuals_Point")

# GlobalDeclarations class attributes and methods

# Template class attributes and methods

# SystemDeclarations class attributes and methods

# uppaal_NTA class attributes and methods

# core_NamedElement class attributes and methods

# core_CommentableElement class attributes and methods

# uppaal_types_PredefinedType class attributes and methods
uppaal_types_PredefinedType_type: Property = Property(name="type", type=StringType)
uppaal_types_PredefinedType.attributes={uppaal_types_PredefinedType_type}

# Type class attributes and methods

# uppaal_types_DeclaredType class attributes and methods

# TypeDeclaration class attributes and methods

# uppaal_core_NamedElement class attributes and methods
uppaal_core_NamedElement_name: Property = Property(name="name", type=StringType)
uppaal_core_NamedElement.attributes={uppaal_core_NamedElement_name}

# uppaal_core_CommentableElement class attributes and methods
uppaal_core_CommentableElement_comment: Property = Property(name="comment", type=StringType)
uppaal_core_CommentableElement.attributes={uppaal_core_CommentableElement_comment}

# uppaal_core_TypedElement class attributes and methods

# TypedElementContainer class attributes and methods

# Expression class attributes and methods

# uppaal_types_Type class attributes and methods
uppaal_types_Type_baseType: Property = Property(name="baseType", type=StringType)
uppaal_types_Type.attributes={uppaal_types_Type_baseType}

# NamedElement class attributes and methods

# uppaal_types_Library class attributes and methods

# PredefinedType class attributes and methods

# uppaal_declarations_Declarations class attributes and methods

# Declaration class attributes and methods

# uppaal_declarations_GlobalDeclarations class attributes and methods

# Declarations class attributes and methods

# uppaal_types_TypeExpression class attributes and methods

# uppaal_types_ScalarTypeSpecification class attributes and methods

# TypeExpression class attributes and methods

# uppaal_types_StructTypeSpecification class attributes and methods

# TypedDeclaration class attributes and methods

# uppaal_types_RangeTypeSpecification class attributes and methods

# IntegerBounds class attributes and methods

# uppaal_types_IntegerBounds class attributes and methods

# uppaal_declarations_Function class attributes and methods

# core_TypedElement class attributes and methods

# Block class attributes and methods

# ParameterContainer class attributes and methods

# global_ChannelPriorityDeclaration class attributes and methods

# uppaal_declarations_LocalDeclarations class attributes and methods

# uppaal_declarations_SystemDeclarations class attributes and methods

# system_System class attributes and methods

# system_ProgressMeasure class attributes and methods

# uppaal_declarations_Declaration class attributes and methods

# uppaal_declarations_Variable class attributes and methods

# uppaal_declarations_TypeDeclaration class attributes and methods

# DeclaredType class attributes and methods

# uppaal_declarations_TypedDeclaration class attributes and methods

# declarations_Declaration class attributes and methods

# declarations_TypedElementContainer class attributes and methods

# uppaal_declarations_ParameterContainer class attributes and methods

# uppaal_global_ChannelPriorityDeclaration class attributes and methods

# Initializer class attributes and methods

# global_ChannelPriorityGroup class attributes and methods

# uppaal_declarations_TypedElementContainer class attributes and methods

# TypedElement class attributes and methods

# uppaal_declarations_Parameter class attributes and methods
uppaal_declarations_Parameter_callType: Property = Property(name="callType", type=StringType)
uppaal_declarations_Parameter.attributes={uppaal_declarations_Parameter_callType}

# Variable class attributes and methods

# uppaal_declarations_Initializer class attributes and methods

# uppaal_declarations_ExpressionInitializer class attributes and methods

# uppaal_declarations_ArrayInitializer class attributes and methods

# uppaal_system_System class attributes and methods

# system_InstantiationList class attributes and methods

# uppaal_system_InstantiationList class attributes and methods

# AbstractTemplate class attributes and methods

# uppaal_system_ProgressMeasure class attributes and methods

# uppaal_global_ChannelPriorityGroup class attributes and methods

# global_PriorityItem class attributes and methods

# uppaal_global_PriorityItem class attributes and methods

# uppaal_global_ChannelItem class attributes and methods

# PriorityItem class attributes and methods

# IdentifierExpression class attributes and methods

# uppaal_global_DefaultItem class attributes and methods

# uppaal_system_TemplateDeclaration class attributes and methods

# RedefinedTemplate class attributes and methods

# Edge class attributes and methods

# uppaal_templates_RedefinedTemplate class attributes and methods

# system_TemplateDeclaration class attributes and methods

# uppaal_templates_Location class attributes and methods
uppaal_templates_Location_locationTimeKind: Property = Property(name="locationTimeKind", type=StringType)
uppaal_templates_Location.attributes={uppaal_templates_Location_locationTimeKind}

# visuals_PlanarElement class attributes and methods

# visuals_ColoredElement class attributes and methods

# uppaal_templates_AbstractTemplate class attributes and methods

# uppaal_templates_Template class attributes and methods

# LocalDeclarations class attributes and methods

# Location class attributes and methods

# Synchronization class attributes and methods

# Selection class attributes and methods

# uppaal_templates_Edge class attributes and methods

# visuals_LinearElement class attributes and methods

# uppaal_statements_Statement class attributes and methods

# uppaal_statements_Block class attributes and methods

# Statement class attributes and methods

# uppaal_templates_Synchronization class attributes and methods
uppaal_templates_Synchronization_kind: Property = Property(name="kind", type=StringType)
uppaal_templates_Synchronization.attributes={uppaal_templates_Synchronization_kind}

# uppaal_templates_Selection class attributes and methods

# uppaal_statements_Iteration class attributes and methods

# statements_Statement class attributes and methods

# uppaal_statements_EmptyStatement class attributes and methods

# uppaal_statements_ForLoop class attributes and methods

# uppaal_statements_DoWhileLoop class attributes and methods

# uppaal_statements_WhileLoop class attributes and methods

# uppaal_statements_ExpressionStatement class attributes and methods

# uppaal_expressions_Expression class attributes and methods

# uppaal_expressions_NegationExpression class attributes and methods

# uppaal_statements_IfStatement class attributes and methods

# uppaal_statements_ReturnStatement class attributes and methods

# uppaal_expressions_AssignmentExpression class attributes and methods
uppaal_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_AssignmentExpression.attributes={uppaal_expressions_AssignmentExpression_operator}

# BinaryExpression class attributes and methods

# uppaal_expressions_PlusExpression class attributes and methods

# uppaal_expressions_MinusExpression class attributes and methods

# uppaal_expressions_BinaryExpression class attributes and methods

# uppaal_expressions_LiteralExpression class attributes and methods
uppaal_expressions_LiteralExpression_text: Property = Property(name="text", type=StringType)
uppaal_expressions_LiteralExpression.attributes={uppaal_expressions_LiteralExpression_text}

# uppaal_expressions_ArithmeticExpression class attributes and methods
uppaal_expressions_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_ArithmeticExpression.attributes={uppaal_expressions_ArithmeticExpression_operator}

# uppaal_expressions_IdentifierExpression class attributes and methods

# uppaal_expressions_ScopedIdentifierExpression class attributes and methods

# uppaal_expressions_ConditionExpression class attributes and methods

# uppaal_expressions_LogicalExpression class attributes and methods
uppaal_expressions_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_LogicalExpression.attributes={uppaal_expressions_LogicalExpression_operator}

# uppaal_expressions_FunctionCallExpression class attributes and methods

# Function class attributes and methods

# uppaal_expressions_CompareExpression class attributes and methods
uppaal_expressions_CompareExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_CompareExpression.attributes={uppaal_expressions_CompareExpression_operator}

# uppaal_expressions_IncrementDecrementExpression class attributes and methods
uppaal_expressions_IncrementDecrementExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_IncrementDecrementExpression.attributes={uppaal_expressions_IncrementDecrementExpression_operator}

# uppaal_expressions_QuantificationExpression class attributes and methods
uppaal_expressions_QuantificationExpression_quantifier: Property = Property(name="quantifier", type=StringType)
uppaal_expressions_QuantificationExpression.attributes={uppaal_expressions_QuantificationExpression_quantifier}

# expressions_Expression class attributes and methods

# uppaal_expressions_MinMaxExpression class attributes and methods
uppaal_expressions_MinMaxExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_MinMaxExpression.attributes={uppaal_expressions_MinMaxExpression_operator}

# uppaal_expressions_PreIncrementDecrementExpression class attributes and methods

# IncrementDecrementExpression class attributes and methods

# uppaal_expressions_PostIncrementDecrementExpression class attributes and methods

# uppaal_expressions_BitShiftExpression class attributes and methods
uppaal_expressions_BitShiftExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitShiftExpression.attributes={uppaal_expressions_BitShiftExpression_operator}

# uppaal_expressions_DataPrefixExpression class attributes and methods
uppaal_expressions_DataPrefixExpression_prefix: Property = Property(name="prefix", type=StringType)
uppaal_expressions_DataPrefixExpression.attributes={uppaal_expressions_DataPrefixExpression_prefix}

# uppaal_expressions_BitwiseExpression class attributes and methods
uppaal_expressions_BitwiseExpression_operator: Property = Property(name="operator", type=StringType)
uppaal_expressions_BitwiseExpression.attributes={uppaal_expressions_BitwiseExpression_operator}

# uppaal_expressions_ChannelPrefixExpression class attributes and methods
uppaal_expressions_ChannelPrefixExpression_urgent: Property = Property(name="urgent", type=BooleanType)
uppaal_expressions_ChannelPrefixExpression_broadcast: Property = Property(name="broadcast", type=BooleanType)
uppaal_expressions_ChannelPrefixExpression.attributes={uppaal_expressions_ChannelPrefixExpression_broadcast, uppaal_expressions_ChannelPrefixExpression_urgent}

# uppaal_visuals_ColoredElement class attributes and methods
uppaal_visuals_ColoredElement_colorCode: Property = Property(name="colorCode", type=StringType)
uppaal_visuals_ColoredElement.attributes={uppaal_visuals_ColoredElement_colorCode}

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
typeDeclaration7: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration7",
    ends={
        Property(name="TypeDeclaration", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
typeDefinition8: BinaryAssociation = BinaryAssociation(
    name="typeDefinition8",
    ends={
        Property(name="Expression9", type=uppaal_types_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_DeclaredType", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
container5: BinaryAssociation = BinaryAssociation(
    name="container5",
    ends={
        Property(name="TypedElementContainer", type=uppaal_core_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=TypedElementContainer, multiplicity=Multiplicity(0, 1))
    }
)
typeDefinition6: BinaryAssociation = BinaryAssociation(
    name="typeDefinition6",
    ends={
        Property(name="Expression", type=uppaal_core_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_core_TypedElement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
upperBound16: BinaryAssociation = BinaryAssociation(
    name="upperBound16",
    ends={
        Property(name="Expression18", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds17", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types19: BinaryAssociation = BinaryAssociation(
    name="types19",
    ends={
        Property(name="PredefinedType", type=uppaal_types_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_Library", type=PredefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration20: BinaryAssociation = BinaryAssociation(
    name="declaration20",
    ends={
        Property(name="Declaration", type=uppaal_declarations_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Declarations", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sizeExpression10: BinaryAssociation = BinaryAssociation(
    name="sizeExpression10",
    ends={
        Property(name="Expression11", type=uppaal_types_ScalarTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_ScalarTypeSpecification", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration12: BinaryAssociation = BinaryAssociation(
    name="declaration12",
    ends={
        Property(name="TypedDeclaration", type=uppaal_types_StructTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_StructTypeSpecification", type=TypedDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bounds13: BinaryAssociation = BinaryAssociation(
    name="bounds13",
    ends={
        Property(name="IntegerBounds", type=uppaal_types_RangeTypeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_RangeTypeSpecification", type=IntegerBounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound14: BinaryAssociation = BinaryAssociation(
    name="lowerBound14",
    ends={
        Property(name="Expression15", type=uppaal_types_IntegerBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_types_IntegerBounds", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block25: BinaryAssociation = BinaryAssociation(
    name="block25",
    ends={
        Property(name="Block", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
channelPriority21: BinaryAssociation = BinaryAssociation(
    name="channelPriority21",
    ends={
        Property(name="global_ChannelPriorityDeclaration", type=uppaal_declarations_GlobalDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_GlobalDeclarations", type=global_ChannelPriorityDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system22: BinaryAssociation = BinaryAssociation(
    name="system22",
    ends={
        Property(name="system_System", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations", type=system_System, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
progressMeasure23: BinaryAssociation = BinaryAssociation(
    name="progressMeasure23",
    ends={
        Property(name="system_ProgressMeasure", type=uppaal_declarations_SystemDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_SystemDeclarations24", type=system_ProgressMeasure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index31: BinaryAssociation = BinaryAssociation(
    name="index31",
    ends={
        Property(name="Expression32", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter26: BinaryAssociation = BinaryAssociation(
    name="parameter26",
    ends={
        Property(name="ParameterContainer", type=uppaal_declarations_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Function27", type=ParameterContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="DeclaredType", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDeclaration", type=DeclaredType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition29: BinaryAssociation = BinaryAssociation(
    name="typeDefinition29",
    ends={
        Property(name="Expression30", type=uppaal_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypeDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer40: BinaryAssociation = BinaryAssociation(
    name="initializer40",
    ends={
        Property(name="Initializer41", type=uppaal_declarations_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ArrayInitializer", type=Initializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initializer33: BinaryAssociation = BinaryAssociation(
    name="initializer33",
    ends={
        Property(name="Initializer", type=uppaal_declarations_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_Variable34", type=Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groups42: BinaryAssociation = BinaryAssociation(
    name="groups42",
    ends={
        Property(name="global_ChannelPriorityGroup", type=uppaal_global_ChannelPriorityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriorityDeclaration", type=global_ChannelPriorityGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeDefinition35: BinaryAssociation = BinaryAssociation(
    name="typeDefinition35",
    ends={
        Property(name="Expression36", type=uppaal_declarations_TypedElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_TypedElementContainer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements37: BinaryAssociation = BinaryAssociation(
    name="elements37",
    ends={
        Property(name="TypedElement", type=uppaal_declarations_TypedElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=TypedElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="Expression39", type=uppaal_declarations_ExpressionInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_declarations_ExpressionInitializer", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument46: BinaryAssociation = BinaryAssociation(
    name="argument46",
    ends={
        Property(name="Expression47", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_TemplateDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiationList48: BinaryAssociation = BinaryAssociation(
    name="instantiationList48",
    ends={
        Property(name="system_InstantiationList", type=uppaal_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_System", type=system_InstantiationList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template49: BinaryAssociation = BinaryAssociation(
    name="template49",
    ends={
        Property(name="AbstractTemplate", type=uppaal_system_InstantiationList, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_InstantiationList", type=AbstractTemplate, multiplicity=Multiplicity(1, 9999))
    }
)
expression50: BinaryAssociation = BinaryAssociation(
    name="expression50",
    ends={
        Property(name="Expression51", type=uppaal_system_ProgressMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_system_ProgressMeasure", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
items43: BinaryAssociation = BinaryAssociation(
    name="items43",
    ends={
        Property(name="global_PriorityItem", type=uppaal_global_ChannelPriorityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelPriorityGroup", type=global_PriorityItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
channelExpression44: BinaryAssociation = BinaryAssociation(
    name="channelExpression44",
    ends={
        Property(name="IdentifierExpression", type=uppaal_global_ChannelItem, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_global_ChannelItem", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaredTemplate45: BinaryAssociation = BinaryAssociation(
    name="declaredTemplate45",
    ends={
        Property(name="RedefinedTemplate", type=uppaal_system_TemplateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=RedefinedTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edge56: BinaryAssociation = BinaryAssociation(
    name="edge56",
    ends={
        Property(name="Edge", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTemplate57", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init58: BinaryAssociation = BinaryAssociation(
    name="init58",
    ends={
        Property(name="Location60", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template59", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
referredTemplate61: BinaryAssociation = BinaryAssociation(
    name="referredTemplate61",
    ends={
        Property(name="AbstractTemplate62", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_RedefinedTemplate", type=AbstractTemplate, multiplicity=Multiplicity(1, 1))
    }
)
declaration63: BinaryAssociation = BinaryAssociation(
    name="declaration63",
    ends={
        Property(name="TemplateDeclaration", type=uppaal_templates_RedefinedTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="declaredTemplate", type=system_TemplateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parameter52: BinaryAssociation = BinaryAssociation(
    name="parameter52",
    ends={
        Property(name="ParameterContainer53", type=uppaal_templates_AbstractTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_AbstractTemplate", type=ParameterContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations54: BinaryAssociation = BinaryAssociation(
    name="declarations54",
    ends={
        Property(name="LocalDeclarations", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Template", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location55: BinaryAssociation = BinaryAssociation(
    name="location55",
    ends={
        Property(name="Location", type=uppaal_templates_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTemplate", type=Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target74: BinaryAssociation = BinaryAssociation(
    name="target74",
    ends={
        Property(name="Location75", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
parentTemplate76: BinaryAssociation = BinaryAssociation(
    name="parentTemplate76",
    ends={
        Property(name="Template77", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
guard78: BinaryAssociation = BinaryAssociation(
    name="guard78",
    ends={
        Property(name="Expression79", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
update80: BinaryAssociation = BinaryAssociation(
    name="update80",
    ends={
        Property(name="Expression82", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge81", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronization83: BinaryAssociation = BinaryAssociation(
    name="synchronization83",
    ends={
        Property(name="Synchronization", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge84", type=Synchronization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentTemplate64: BinaryAssociation = BinaryAssociation(
    name="parentTemplate64",
    ends={
        Property(name="Template65", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
invariant66: BinaryAssociation = BinaryAssociation(
    name="invariant66",
    ends={
        Property(name="Expression67", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Location", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingEdges68: BinaryAssociation = BinaryAssociation(
    name="incomingEdges68",
    ends={
        Property(name="Edge69", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges70: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges70",
    ends={
        Property(name="Edge71", type=uppaal_templates_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source72: BinaryAssociation = BinaryAssociation(
    name="source72",
    ends={
        Property(name="Location73", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
declarations89: BinaryAssociation = BinaryAssociation(
    name="declarations89",
    ends={
        Property(name="LocalDeclarations90", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block", type=LocalDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection85: BinaryAssociation = BinaryAssociation(
    name="selection85",
    ends={
        Property(name="Selection", type=uppaal_templates_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Edge86", type=Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channelExpression87: BinaryAssociation = BinaryAssociation(
    name="channelExpression87",
    ends={
        Property(name="IdentifierExpression88", type=uppaal_templates_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_templates_Synchronization", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition95: BinaryAssociation = BinaryAssociation(
    name="condition95",
    ends={
        Property(name="Expression97", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop96", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteration98: BinaryAssociation = BinaryAssociation(
    name="iteration98",
    ends={
        Property(name="Expression100", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop99", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement101: BinaryAssociation = BinaryAssociation(
    name="statement101",
    ends={
        Property(name="Statement103", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop102", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement91: BinaryAssociation = BinaryAssociation(
    name="statement91",
    ends={
        Property(name="Statement", type=uppaal_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Block92", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialization93: BinaryAssociation = BinaryAssociation(
    name="initialization93",
    ends={
        Property(name="Expression94", type=uppaal_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ForLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement111: BinaryAssociation = BinaryAssociation(
    name="statement111",
    ends={
        Property(name="Statement112", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="Expression115", type=uppaal_statements_DoWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_DoWhileLoop114", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement104: BinaryAssociation = BinaryAssociation(
    name="statement104",
    ends={
        Property(name="Statement105", type=uppaal_statements_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_Iteration", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression106: BinaryAssociation = BinaryAssociation(
    name="expression106",
    ends={
        Property(name="Expression107", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement108: BinaryAssociation = BinaryAssociation(
    name="statement108",
    ends={
        Property(name="Statement110", type=uppaal_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_WhileLoop109", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="Expression127", type=uppaal_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negatedExpression128: BinaryAssociation = BinaryAssociation(
    name="negatedExpression128",
    ends={
        Property(name="Expression129", type=uppaal_expressions_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_NegationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpression116: BinaryAssociation = BinaryAssociation(
    name="ifExpression116",
    ends={
        Property(name="Expression117", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement118: BinaryAssociation = BinaryAssociation(
    name="thenStatement118",
    ends={
        Property(name="Statement120", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement119", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement121: BinaryAssociation = BinaryAssociation(
    name="elseStatement121",
    ends={
        Property(name="Statement123", type=uppaal_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_IfStatement122", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnExpression124: BinaryAssociation = BinaryAssociation(
    name="returnExpression124",
    ends={
        Property(name="Expression125", type=uppaal_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondExpr136: BinaryAssociation = BinaryAssociation(
    name="secondExpr136",
    ends={
        Property(name="Expression138", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression137", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
confirmedExpression130: BinaryAssociation = BinaryAssociation(
    name="confirmedExpression130",
    ends={
        Property(name="Expression131", type=uppaal_expressions_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_PlusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invertedExpression132: BinaryAssociation = BinaryAssociation(
    name="invertedExpression132",
    ends={
        Property(name="Expression133", type=uppaal_expressions_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_MinusExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scope143: BinaryAssociation = BinaryAssociation(
    name="scope143",
    ends={
        Property(name="Expression144", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstExpr134: BinaryAssociation = BinaryAssociation(
    name="firstExpr134",
    ends={
        Property(name="Expression135", type=uppaal_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier145: BinaryAssociation = BinaryAssociation(
    name="identifier145",
    ends={
        Property(name="IdentifierExpression147", type=uppaal_expressions_ScopedIdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ScopedIdentifierExpression146", type=IdentifierExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifier139: BinaryAssociation = BinaryAssociation(
    name="identifier139",
    ends={
        Property(name="NamedElement", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
index140: BinaryAssociation = BinaryAssociation(
    name="index140",
    ends={
        Property(name="Expression142", type=uppaal_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IdentifierExpression141", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExpression152: BinaryAssociation = BinaryAssociation(
    name="ifExpression152",
    ends={
        Property(name="Expression153", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression154: BinaryAssociation = BinaryAssociation(
    name="thenExpression154",
    ends={
        Property(name="Expression156", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression155", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function148: BinaryAssociation = BinaryAssociation(
    name="function148",
    ends={
        Property(name="Function", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
argument149: BinaryAssociation = BinaryAssociation(
    name="argument149",
    ends={
        Property(name="Expression151", type=uppaal_expressions_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_FunctionCallExpression150", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="Expression161", type=uppaal_expressions_QuantificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_QuantificationExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression162: BinaryAssociation = BinaryAssociation(
    name="expression162",
    ends={
        Property(name="Expression163", type=uppaal_expressions_IncrementDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_IncrementDecrementExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression157: BinaryAssociation = BinaryAssociation(
    name="elseExpression157",
    ends={
        Property(name="Expression159", type=uppaal_expressions_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ConditionExpression158", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataTypeExpression165: BinaryAssociation = BinaryAssociation(
    name="dataTypeExpression165",
    ends={
        Property(name="Expression166", type=uppaal_expressions_DataPrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_DataPrefixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
channelType164: BinaryAssociation = BinaryAssociation(
    name="channelType164",
    ends={
        Property(name="Type", type=uppaal_expressions_ChannelPrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_expressions_ChannelPrefixExpression", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
position167: BinaryAssociation = BinaryAssociation(
    name="position167",
    ends={
        Property(name="Point", type=uppaal_visuals_PlanarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_PlanarElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bendPoint168: BinaryAssociation = BinaryAssociation(
    name="bendPoint168",
    ends={
        Property(name="Point169", type=uppaal_visuals_LinearElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_visuals_LinearElement", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uppaal_NTA_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_NTA)
gen_uppaal_NTA_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_NTA)
gen_uppaal_types_PredefinedType_Type = Generalization(general=Type, specific=uppaal_types_PredefinedType)
gen_uppaal_types_DeclaredType_Type = Generalization(general=Type, specific=uppaal_types_DeclaredType)
gen_uppaal_types_Type_NamedElement = Generalization(general=NamedElement, specific=uppaal_types_Type)
gen_uppaal_declarations_GlobalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_GlobalDeclarations)
gen_uppaal_types_TypeExpression_Expression = Generalization(general=Expression, specific=uppaal_types_TypeExpression)
gen_uppaal_types_ScalarTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_ScalarTypeSpecification)
gen_uppaal_types_StructTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_StructTypeSpecification)
gen_uppaal_types_RangeTypeSpecification_TypeExpression = Generalization(general=TypeExpression, specific=uppaal_types_RangeTypeSpecification)
gen_uppaal_declarations_Function_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_Function_core_TypedElement = Generalization(general=core_TypedElement, specific=uppaal_declarations_Function)
gen_uppaal_declarations_LocalDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_LocalDeclarations)
gen_uppaal_declarations_SystemDeclarations_Declarations = Generalization(general=Declarations, specific=uppaal_declarations_SystemDeclarations)
gen_uppaal_declarations_Variable_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_Variable_core_TypedElement = Generalization(general=core_TypedElement, specific=uppaal_declarations_Variable)
gen_uppaal_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_declarations_TypeDeclaration)
gen_uppaal_declarations_TypedDeclaration_declarations_Declaration = Generalization(general=declarations_Declaration, specific=uppaal_declarations_TypedDeclaration)
gen_uppaal_declarations_TypedDeclaration_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_declarations_TypedDeclaration)
gen_uppaal_declarations_ParameterContainer_TypedElementContainer = Generalization(general=TypedElementContainer, specific=uppaal_declarations_ParameterContainer)
gen_uppaal_global_ChannelPriorityDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_global_ChannelPriorityDeclaration)
gen_uppaal_declarations_Parameter_Variable = Generalization(general=Variable, specific=uppaal_declarations_Parameter)
gen_uppaal_declarations_ExpressionInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ExpressionInitializer)
gen_uppaal_declarations_ArrayInitializer_Initializer = Generalization(general=Initializer, specific=uppaal_declarations_ArrayInitializer)
gen_uppaal_global_ChannelItem_PriorityItem = Generalization(general=PriorityItem, specific=uppaal_global_ChannelItem)
gen_uppaal_global_DefaultItem_PriorityItem = Generalization(general=PriorityItem, specific=uppaal_global_DefaultItem)
gen_uppaal_system_TemplateDeclaration_Declaration = Generalization(general=Declaration, specific=uppaal_system_TemplateDeclaration)
gen_uppaal_templates_RedefinedTemplate_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_RedefinedTemplate)
gen_uppaal_templates_Location_core_NamedElement = Generalization(general=core_NamedElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_PlanarElement = Generalization(general=visuals_PlanarElement, specific=uppaal_templates_Location)
gen_uppaal_templates_Location_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Location)
gen_uppaal_templates_AbstractTemplate_NamedElement = Generalization(general=NamedElement, specific=uppaal_templates_AbstractTemplate)
gen_uppaal_templates_Template_AbstractTemplate = Generalization(general=AbstractTemplate, specific=uppaal_templates_Template)
gen_uppaal_templates_Edge_visuals_LinearElement = Generalization(general=visuals_LinearElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_core_CommentableElement = Generalization(general=core_CommentableElement, specific=uppaal_templates_Edge)
gen_uppaal_templates_Edge_visuals_ColoredElement = Generalization(general=visuals_ColoredElement, specific=uppaal_templates_Edge)
gen_uppaal_statements_Block_Statement = Generalization(general=Statement, specific=uppaal_statements_Block)
gen_uppaal_templates_Selection_TypedElementContainer = Generalization(general=TypedElementContainer, specific=uppaal_templates_Selection)
gen_uppaal_statements_Iteration_statements_Statement = Generalization(general=statements_Statement, specific=uppaal_statements_Iteration)
gen_uppaal_statements_Iteration_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_statements_Iteration)
gen_uppaal_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_EmptyStatement)
gen_uppaal_statements_ForLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_ForLoop)
gen_uppaal_statements_DoWhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_DoWhileLoop)
gen_uppaal_statements_WhileLoop_Statement = Generalization(general=Statement, specific=uppaal_statements_WhileLoop)
gen_uppaal_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ExpressionStatement)
gen_uppaal_expressions_NegationExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_NegationExpression)
gen_uppaal_statements_IfStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_IfStatement)
gen_uppaal_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=uppaal_statements_ReturnStatement)
gen_uppaal_expressions_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_AssignmentExpression)
gen_uppaal_expressions_PlusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_PlusExpression)
gen_uppaal_expressions_MinusExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_MinusExpression)
gen_uppaal_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_BinaryExpression)
gen_uppaal_expressions_LiteralExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_LiteralExpression)
gen_uppaal_expressions_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_ArithmeticExpression)
gen_uppaal_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IdentifierExpression)
gen_uppaal_expressions_ScopedIdentifierExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ScopedIdentifierExpression)
gen_uppaal_expressions_ConditionExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ConditionExpression)
gen_uppaal_expressions_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_LogicalExpression)
gen_uppaal_expressions_FunctionCallExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_FunctionCallExpression)
gen_uppaal_expressions_CompareExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_CompareExpression)
gen_uppaal_expressions_IncrementDecrementExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_IncrementDecrementExpression)
gen_uppaal_expressions_QuantificationExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_QuantificationExpression_declarations_TypedElementContainer = Generalization(general=declarations_TypedElementContainer, specific=uppaal_expressions_QuantificationExpression)
gen_uppaal_expressions_MinMaxExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_MinMaxExpression)
gen_uppaal_expressions_PreIncrementDecrementExpression_IncrementDecrementExpression = Generalization(general=IncrementDecrementExpression, specific=uppaal_expressions_PreIncrementDecrementExpression)
gen_uppaal_expressions_PostIncrementDecrementExpression_IncrementDecrementExpression = Generalization(general=IncrementDecrementExpression, specific=uppaal_expressions_PostIncrementDecrementExpression)
gen_uppaal_expressions_BitShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitShiftExpression)
gen_uppaal_expressions_DataPrefixExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_DataPrefixExpression)
gen_uppaal_expressions_BitwiseExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=uppaal_expressions_BitwiseExpression)
gen_uppaal_expressions_ChannelPrefixExpression_Expression = Generalization(general=Expression, specific=uppaal_expressions_ChannelPrefixExpression)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={GlobalDeclarations, Template, SystemDeclarations, uppaal_NTA, core_NamedElement, core_CommentableElement, uppaal_types_PredefinedType, Type, uppaal_types_DeclaredType, TypeDeclaration, uppaal_core_NamedElement, uppaal_core_CommentableElement, uppaal_core_TypedElement, TypedElementContainer, Expression, uppaal_types_Type, NamedElement, uppaal_types_Library, PredefinedType, uppaal_declarations_Declarations, Declaration, uppaal_declarations_GlobalDeclarations, Declarations, uppaal_types_TypeExpression, uppaal_types_ScalarTypeSpecification, TypeExpression, uppaal_types_StructTypeSpecification, TypedDeclaration, uppaal_types_RangeTypeSpecification, IntegerBounds, uppaal_types_IntegerBounds, uppaal_declarations_Function, core_TypedElement, Block, ParameterContainer, global_ChannelPriorityDeclaration, uppaal_declarations_LocalDeclarations, uppaal_declarations_SystemDeclarations, system_System, system_ProgressMeasure, uppaal_declarations_Declaration, uppaal_declarations_Variable, uppaal_declarations_TypeDeclaration, DeclaredType, uppaal_declarations_TypedDeclaration, declarations_Declaration, declarations_TypedElementContainer, uppaal_declarations_ParameterContainer, uppaal_global_ChannelPriorityDeclaration, Initializer, global_ChannelPriorityGroup, uppaal_declarations_TypedElementContainer, TypedElement, uppaal_declarations_Parameter, Variable, uppaal_declarations_Initializer, uppaal_declarations_ExpressionInitializer, uppaal_declarations_ArrayInitializer, uppaal_system_System, system_InstantiationList, uppaal_system_InstantiationList, AbstractTemplate, uppaal_system_ProgressMeasure, uppaal_global_ChannelPriorityGroup, global_PriorityItem, uppaal_global_PriorityItem, uppaal_global_ChannelItem, PriorityItem, IdentifierExpression, uppaal_global_DefaultItem, uppaal_system_TemplateDeclaration, RedefinedTemplate, Edge, uppaal_templates_RedefinedTemplate, system_TemplateDeclaration, uppaal_templates_Location, visuals_PlanarElement, visuals_ColoredElement, uppaal_templates_AbstractTemplate, uppaal_templates_Template, LocalDeclarations, Location, Synchronization, Selection, uppaal_templates_Edge, visuals_LinearElement, uppaal_statements_Statement, uppaal_statements_Block, Statement, uppaal_templates_Synchronization, uppaal_templates_Selection, uppaal_statements_Iteration, statements_Statement, uppaal_statements_EmptyStatement, uppaal_statements_ForLoop, uppaal_statements_DoWhileLoop, uppaal_statements_WhileLoop, uppaal_statements_ExpressionStatement, uppaal_expressions_Expression, uppaal_expressions_NegationExpression, uppaal_statements_IfStatement, uppaal_statements_ReturnStatement, uppaal_expressions_AssignmentExpression, BinaryExpression, uppaal_expressions_PlusExpression, uppaal_expressions_MinusExpression, uppaal_expressions_BinaryExpression, uppaal_expressions_LiteralExpression, uppaal_expressions_ArithmeticExpression, uppaal_expressions_IdentifierExpression, uppaal_expressions_ScopedIdentifierExpression, uppaal_expressions_ConditionExpression, uppaal_expressions_LogicalExpression, uppaal_expressions_FunctionCallExpression, Function, uppaal_expressions_CompareExpression, uppaal_expressions_IncrementDecrementExpression, uppaal_expressions_QuantificationExpression, expressions_Expression, uppaal_expressions_MinMaxExpression, uppaal_expressions_PreIncrementDecrementExpression, IncrementDecrementExpression, uppaal_expressions_PostIncrementDecrementExpression, uppaal_expressions_BitShiftExpression, uppaal_expressions_DataPrefixExpression, uppaal_expressions_BitwiseExpression, uppaal_expressions_ChannelPrefixExpression, uppaal_visuals_ColoredElement, uppaal_visuals_PlanarElement, Point, uppaal_visuals_LinearElement, uppaal_visuals_Point, BuiltInType, DataVariablePrefix, CallType, LocationKind, SynchronizationKind, AssignmentOperator, ArithmeticOperator, CompareOperator, LogicalOperator, Quantifier, BitShiftOperator, MinMaxOperator, IncrementDecrementOperator, BitwiseOperator},
    associations={globalDeclarations0, template1, systemDeclarations3, typeDeclaration7, typeDefinition8, container5, typeDefinition6, upperBound16, types19, declaration20, sizeExpression10, declaration12, bounds13, lowerBound14, block25, channelPriority21, system22, progressMeasure23, index31, parameter26, type28, typeDefinition29, initializer40, initializer33, groups42, typeDefinition35, elements37, expression38, argument46, instantiationList48, template49, expression50, items43, channelExpression44, declaredTemplate45, edge56, init58, referredTemplate61, declaration63, parameter52, declarations54, location55, target74, parentTemplate76, guard78, update80, synchronization83, parentTemplate64, invariant66, incomingEdges68, outgoingEdges70, source72, declarations89, selection85, channelExpression87, condition95, iteration98, statement101, statement91, initialization93, statement111, expression113, statement104, expression106, statement108, expression126, negatedExpression128, ifExpression116, thenStatement118, elseStatement121, returnExpression124, secondExpr136, confirmedExpression130, invertedExpression132, scope143, firstExpr134, identifier145, identifier139, index140, ifExpression152, thenExpression154, function148, argument149, expression160, expression162, elseExpression157, dataTypeExpression165, channelType164, position167, bendPoint168},
    generalizations={gen_uppaal_NTA_core_NamedElement, gen_uppaal_NTA_core_CommentableElement, gen_uppaal_types_PredefinedType_Type, gen_uppaal_types_DeclaredType_Type, gen_uppaal_types_Type_NamedElement, gen_uppaal_declarations_GlobalDeclarations_Declarations, gen_uppaal_types_TypeExpression_Expression, gen_uppaal_types_ScalarTypeSpecification_TypeExpression, gen_uppaal_types_StructTypeSpecification_TypeExpression, gen_uppaal_types_RangeTypeSpecification_TypeExpression, gen_uppaal_declarations_Function_core_NamedElement, gen_uppaal_declarations_Function_core_TypedElement, gen_uppaal_declarations_LocalDeclarations_Declarations, gen_uppaal_declarations_SystemDeclarations_Declarations, gen_uppaal_declarations_Variable_core_NamedElement, gen_uppaal_declarations_Variable_core_TypedElement, gen_uppaal_declarations_TypeDeclaration_Declaration, gen_uppaal_declarations_TypedDeclaration_declarations_Declaration, gen_uppaal_declarations_TypedDeclaration_declarations_TypedElementContainer, gen_uppaal_declarations_ParameterContainer_TypedElementContainer, gen_uppaal_global_ChannelPriorityDeclaration_Declaration, gen_uppaal_declarations_Parameter_Variable, gen_uppaal_declarations_ExpressionInitializer_Initializer, gen_uppaal_declarations_ArrayInitializer_Initializer, gen_uppaal_global_ChannelItem_PriorityItem, gen_uppaal_global_DefaultItem_PriorityItem, gen_uppaal_system_TemplateDeclaration_Declaration, gen_uppaal_templates_RedefinedTemplate_AbstractTemplate, gen_uppaal_templates_Location_core_NamedElement, gen_uppaal_templates_Location_core_CommentableElement, gen_uppaal_templates_Location_visuals_PlanarElement, gen_uppaal_templates_Location_visuals_ColoredElement, gen_uppaal_templates_AbstractTemplate_NamedElement, gen_uppaal_templates_Template_AbstractTemplate, gen_uppaal_templates_Edge_visuals_LinearElement, gen_uppaal_templates_Edge_core_CommentableElement, gen_uppaal_templates_Edge_visuals_ColoredElement, gen_uppaal_statements_Block_Statement, gen_uppaal_templates_Selection_TypedElementContainer, gen_uppaal_statements_Iteration_statements_Statement, gen_uppaal_statements_Iteration_declarations_TypedElementContainer, gen_uppaal_statements_EmptyStatement_Statement, gen_uppaal_statements_ForLoop_Statement, gen_uppaal_statements_DoWhileLoop_Statement, gen_uppaal_statements_WhileLoop_Statement, gen_uppaal_statements_ExpressionStatement_Statement, gen_uppaal_expressions_NegationExpression_Expression, gen_uppaal_statements_IfStatement_Statement, gen_uppaal_statements_ReturnStatement_Statement, gen_uppaal_expressions_AssignmentExpression_BinaryExpression, gen_uppaal_expressions_PlusExpression_Expression, gen_uppaal_expressions_MinusExpression_Expression, gen_uppaal_expressions_BinaryExpression_Expression, gen_uppaal_expressions_LiteralExpression_Expression, gen_uppaal_expressions_ArithmeticExpression_BinaryExpression, gen_uppaal_expressions_IdentifierExpression_Expression, gen_uppaal_expressions_ScopedIdentifierExpression_Expression, gen_uppaal_expressions_ConditionExpression_Expression, gen_uppaal_expressions_LogicalExpression_BinaryExpression, gen_uppaal_expressions_FunctionCallExpression_Expression, gen_uppaal_expressions_CompareExpression_BinaryExpression, gen_uppaal_expressions_IncrementDecrementExpression_Expression, gen_uppaal_expressions_QuantificationExpression_expressions_Expression, gen_uppaal_expressions_QuantificationExpression_declarations_TypedElementContainer, gen_uppaal_expressions_MinMaxExpression_BinaryExpression, gen_uppaal_expressions_PreIncrementDecrementExpression_IncrementDecrementExpression, gen_uppaal_expressions_PostIncrementDecrementExpression_IncrementDecrementExpression, gen_uppaal_expressions_BitShiftExpression_BinaryExpression, gen_uppaal_expressions_DataPrefixExpression_Expression, gen_uppaal_expressions_BitwiseExpression_BinaryExpression, gen_uppaal_expressions_ChannelPrefixExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)