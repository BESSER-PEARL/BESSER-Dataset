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
AssignOperator: Enumeration = Enumeration(
    name="AssignOperator",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ADD_ASIGN"),
			EnumerationLiteral(name="SUB_ASSIGN"),
			EnumerationLiteral(name="DIV_ASSIGN"),
			EnumerationLiteral(name="MULT_ASSIGN"),
			EnumerationLiteral(name="MOD_ASSIGN")
    }
)

BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="LESS_THAN_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="GREATER_THAN_OR_EQUAL"),
			EnumerationLiteral(name="LOGICAL_NEGATION"),
			EnumerationLiteral(name="ADDITION"),
			EnumerationLiteral(name="SUBSTRACTION"),
			EnumerationLiteral(name="MULTIPLICATION"),
			EnumerationLiteral(name="DIVISION"),
			EnumerationLiteral(name="MODULO"),
			EnumerationLiteral(name="LEFT_BITSHIFT"),
			EnumerationLiteral(name="RIGHT_BITSHIFT"),
			EnumerationLiteral(name="MINIMUM"),
			EnumerationLiteral(name="MAXIMUM"),
			EnumerationLiteral(name="BITWISE_AND"),
			EnumerationLiteral(name="BITWISE_XOR"),
			EnumerationLiteral(name="BITWISE_OR"),
			EnumerationLiteral(name="LOGICAL_AND"),
			EnumerationLiteral(name="LOGICAL_OR"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="BITWISE_OR_ASSIGN"),
			EnumerationLiteral(name="BITWISE_AND_ASSIGN"),
			EnumerationLiteral(name="BITWISE_XOR_ASIGN"),
			EnumerationLiteral(name="LEFT_BITSHIFT_ASSIGN"),
			EnumerationLiteral(name="RIGHT_BITSHIFT_ASSIGN"),
			EnumerationLiteral(name="IMPLY")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="NOT")
    }
)

FixedExpressionType: Enumeration = Enumeration(
    name="FixedExpressionType",
    literals={
            EnumerationLiteral(name="Deadlock"),
			EnumerationLiteral(name="True"),
			EnumerationLiteral(name="False")
    }
)

PriorityOperator: Enumeration = Enumeration(
    name="PriorityOperator",
    literals={
            EnumerationLiteral(name="Seperator"),
			EnumerationLiteral(name="LessThan")
    }
)

TypeId: Enumeration = Enumeration(
    name="TypeId",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Clock"),
			EnumerationLiteral(name="Channel"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Void")
    }
)

TypePrefix: Enumeration = Enumeration(
    name="TypePrefix",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="URGENT"),
			EnumerationLiteral(name="BROADCAST"),
			EnumerationLiteral(name="META"),
			EnumerationLiteral(name="CONSTANT")
    }
)

# Classes
timedAutomata_base_Commentable = Class(name="timedAutomata::base::Commentable", is_abstract=True)
timedAutomata_base_Identifyable = Class(name="timedAutomata::base::Identifyable")
timedAutomata_base_Nameable = Class(name="timedAutomata::base::Nameable")
timedAutomata_bnf_Identifier = Class(name="timedAutomata::bnf::Identifier")
timedAutomata_bnf_Synchronisation = Class(name="timedAutomata::bnf::Synchronisation", is_abstract=True)
Position = Class(name="Position")
expressions_Expression = Class(name="expressions::Expression")
timedAutomata_bnf_SendSynchronisation = Class(name="timedAutomata::bnf::SendSynchronisation")
Synchronisation = Class(name="Synchronisation")
timedAutomata_bnf_ReceiveSynchronisation = Class(name="timedAutomata::bnf::ReceiveSynchronisation")
timedAutomata_expressions_VariableExpression = Class(name="timedAutomata::expressions::VariableExpression")
timedAutomata_expressions_Expression = Class(name="timedAutomata::expressions::Expression", is_abstract=True)
Commentable = Class(name="Commentable")
timedAutomata_expressions_ConstantExpression = Class(name="timedAutomata::expressions::ConstantExpression")
Expression = Class(name="Expression")
Identifier = Class(name="Identifier")
timedAutomata_expressions_ArrayVariableExpression = Class(name="timedAutomata::expressions::ArrayVariableExpression")
timedAutomata_expressions_IncDecExpression = Class(name="timedAutomata::expressions::IncDecExpression")
timedAutomata_expressions_GroupingExpression = Class(name="timedAutomata::expressions::GroupingExpression")
timedAutomata_expressions_BinaryExpression = Class(name="timedAutomata::expressions::BinaryExpression")
timedAutomata_expressions_AssignmentExpression = Class(name="timedAutomata::expressions::AssignmentExpression")
timedAutomata_expressions_UnaryExpression = Class(name="timedAutomata::expressions::UnaryExpression")
timedAutomata_expressions_SimpleIfExpression = Class(name="timedAutomata::expressions::SimpleIfExpression")
timedAutomata_expressions_IdentifierExpression = Class(name="timedAutomata::expressions::IdentifierExpression")
timedAutomata_expressions_WithArgumentsExpression = Class(name="timedAutomata::expressions::WithArgumentsExpression")
timedAutomata_expressions_PointExpression = Class(name="timedAutomata::expressions::PointExpression")
timedAutomata_expressions_ForallExpression = Class(name="timedAutomata::expressions::ForallExpression")
types_Type = Class(name="types::Type")
timedAutomata_expressions_ExistsExpression = Class(name="timedAutomata::expressions::ExistsExpression")
timedAutomata_expressions_FixedExpression = Class(name="timedAutomata::expressions::FixedExpression")
timedAutomata_expressions_Selection = Class(name="timedAutomata::expressions::Selection")
timedAutomata_declarations_Declaration = Class(name="timedAutomata::declarations::Declaration", is_abstract=True)
timedAutomata_declarations_VariableDeclaration = Class(name="timedAutomata::declarations::VariableDeclaration")
Declaration = Class(name="Declaration")
declarations_VariableIdentifier = Class(name="declarations::VariableIdentifier")
timedAutomata_declarations_VariableIdentifier = Class(name="timedAutomata::declarations::VariableIdentifier")
declarations_ArrayDeclarationType = Class(name="declarations::ArrayDeclarationType")
declarations_Initialiser = Class(name="declarations::Initialiser")
declarations_ArrayDeclaration = Class(name="declarations::ArrayDeclaration")
timedAutomata_declarations_FunctionDeclaration = Class(name="timedAutomata::declarations::FunctionDeclaration")
declarations_TAParameter = Class(name="declarations::TAParameter")
declarations_Block = Class(name="declarations::Block")
timedAutomata_declarations_ChannelPriorityDeclaration = Class(name="timedAutomata::declarations::ChannelPriorityDeclaration")
declarations_ChannelPriority = Class(name="declarations::ChannelPriority")
timedAutomata_declarations_FieldDeclaration = Class(name="timedAutomata::declarations::FieldDeclaration")
timedAutomata_declarations_ArrayDeclaration = Class(name="timedAutomata::declarations::ArrayDeclaration")
timedAutomata_declarations_TypeDeclaration = Class(name="timedAutomata::declarations::TypeDeclaration")
timedAutomata_declarations_ArrayDeclarationType = Class(name="timedAutomata::declarations::ArrayDeclarationType")
timedAutomata_declarations_ArrayExpressionType = Class(name="timedAutomata::declarations::ArrayExpressionType")
ArrayDeclarationType = Class(name="ArrayDeclarationType")
timedAutomata_declarations_ArrayTypeType = Class(name="timedAutomata::declarations::ArrayTypeType")
timedAutomata_declarations_Initialiser = Class(name="timedAutomata::declarations::Initialiser", is_abstract=True)
timedAutomata_declarations_ExpressionInitialiser = Class(name="timedAutomata::declarations::ExpressionInitialiser")
Initialiser = Class(name="Initialiser")
timedAutomata_declarations_ArrayInitialiser = Class(name="timedAutomata::declarations::ArrayInitialiser")
timedAutomata_declarations_TAParameter = Class(name="timedAutomata::declarations::TAParameter", is_abstract=True)
timedAutomata_declarations_CallByValueParameter = Class(name="timedAutomata::declarations::CallByValueParameter")
TAParameter = Class(name="TAParameter")
timedAutomata_declarations_CallByReferenceParameter = Class(name="timedAutomata::declarations::CallByReferenceParameter")
timedAutomata_declarations_Block = Class(name="timedAutomata::declarations::Block")
declarations_Declaration = Class(name="declarations::Declaration")
declarations_Statement = Class(name="declarations::Statement")
timedAutomata_declarations_Statement = Class(name="timedAutomata::declarations::Statement", is_abstract=True)
timedAutomata_declarations_BlockStatement = Class(name="timedAutomata::declarations::BlockStatement")
timedAutomata_declarations_ExpressionStatement = Class(name="timedAutomata::declarations::ExpressionStatement")
Statement = Class(name="Statement")
timedAutomata_declarations_ForLoopStatement = Class(name="timedAutomata::declarations::ForLoopStatement")
timedAutomata_declarations_IterationStatement = Class(name="timedAutomata::declarations::IterationStatement")
timedAutomata_declarations_WhileLoopStatement = Class(name="timedAutomata::declarations::WhileLoopStatement")
timedAutomata_declarations_DoWhileLoopStatement = Class(name="timedAutomata::declarations::DoWhileLoopStatement")
timedAutomata_declarations_IfStatement = Class(name="timedAutomata::declarations::IfStatement")
timedAutomata_declarations_ReturnStatement = Class(name="timedAutomata::declarations::ReturnStatement")
timedAutomata_declarations_ChannelPriority = Class(name="timedAutomata::declarations::ChannelPriority", is_abstract=True)
timedAutomata_declarations_DefaultChannelPriority = Class(name="timedAutomata::declarations::DefaultChannelPriority")
ChannelPriority = Class(name="ChannelPriority")
timedAutomata_declarations_SimpleChannelPriority = Class(name="timedAutomata::declarations::SimpleChannelPriority")
declarations_ChannelExpression = Class(name="declarations::ChannelExpression")
timedAutomata_declarations_ComplexChannelPriority = Class(name="timedAutomata::declarations::ComplexChannelPriority")
timedAutomata_declarations_ChannelExpression = Class(name="timedAutomata::declarations::ChannelExpression", is_abstract=True)
timedAutomata_declarations_IdentifierChannelExpression = Class(name="timedAutomata::declarations::IdentifierChannelExpression")
ChannelExpression = Class(name="ChannelExpression")
timedAutomata_declarations_ExpressionChannelExpression = Class(name="timedAutomata::declarations::ExpressionChannelExpression")
timedAutomata_types_Type = Class(name="timedAutomata::types::Type", is_abstract=True)
timedAutomata_types_IdentifierType = Class(name="timedAutomata::types::IdentifierType")
Type = Class(name="Type")
timedAutomata_types_SimpleType = Class(name="timedAutomata::types::SimpleType")
timedAutomata_types_IntegerRange = Class(name="timedAutomata::types::IntegerRange")
timedAutomata_core_Project = Class(name="timedAutomata::core::Project")
TAElement = Class(name="TAElement")
Template = Class(name="Template")
timedAutomata_types_Scalar = Class(name="timedAutomata::types::Scalar")
SystemDefinition = Class(name="SystemDefinition")
timedAutomata_core_Template = Class(name="timedAutomata::core::Template")
timedAutomata_types_Struct = Class(name="timedAutomata::types::Struct")
declarations_FieldDeclaration = Class(name="declarations::FieldDeclaration")
Guards = Class(name="Guards")
Selections = Class(name="Selections")
core_TAElement = Class(name="core::TAElement")
base_Nameable = Class(name="base::Nameable")
base_Identifyable = Class(name="base::Identifyable")
Location = Class(name="Location")
core_timedAutomata_Parameter = Class(name="core::timedAutomata::Parameter")
Edge = Class(name="Edge")
timedAutomata_core_Edge = Class(name="timedAutomata::core::Edge")
timedAutomata_core_SystemDefinition = Class(name="timedAutomata::core::SystemDefinition")
TemplateInstantiation = Class(name="TemplateInstantiation")
System = Class(name="System")
timedAutomata_core_System = Class(name="timedAutomata::core::System", is_abstract=True)
timedAutomata_core_SimpleSystem = Class(name="timedAutomata::core::SimpleSystem")
Updates = Class(name="Updates")
core_timedAutomata_Nail = Class(name="core::timedAutomata::Nail")
timedAutomata_core_TAElement = Class(name="timedAutomata::core::TAElement", is_abstract=True)
base_Commentable = Class(name="base::Commentable")
timedAutomata_core_Location = Class(name="timedAutomata::core::Location")
core_timedAutomata_Label = Class(name="core::timedAutomata::Label")
timedAutomata_core_TemplateInstantiation = Class(name="timedAutomata::core::TemplateInstantiation")
timedAutomata_core_ComplexSystem = Class(name="timedAutomata::core::ComplexSystem")
timedAutomata_core_Selections = Class(name="timedAutomata::core::Selections")
expressions_Selection = Class(name="expressions::Selection")
timedAutomata_core_Updates = Class(name="timedAutomata::core::Updates")
timedAutomata_core_Guards = Class(name="timedAutomata::core::Guards")

# timedAutomata_base_Commentable class attributes and methods
timedAutomata_base_Commentable_comment: Property = Property(name="comment", type=StringType)
timedAutomata_base_Commentable.attributes={timedAutomata_base_Commentable_comment}

# timedAutomata_base_Identifyable class attributes and methods
timedAutomata_base_Identifyable_id: Property = Property(name="id", type=IntegerType)
timedAutomata_base_Identifyable.attributes={timedAutomata_base_Identifyable_id}

# timedAutomata_base_Nameable class attributes and methods
timedAutomata_base_Nameable_name: Property = Property(name="name", type=StringType)
timedAutomata_base_Nameable.attributes={timedAutomata_base_Nameable_name}

# timedAutomata_bnf_Identifier class attributes and methods
timedAutomata_bnf_Identifier_name: Property = Property(name="name", type=StringType)
timedAutomata_bnf_Identifier.attributes={timedAutomata_bnf_Identifier_name}

# timedAutomata_bnf_Synchronisation class attributes and methods

# Position class attributes and methods

# expressions_Expression class attributes and methods

# timedAutomata_bnf_SendSynchronisation class attributes and methods

# Synchronisation class attributes and methods

# timedAutomata_bnf_ReceiveSynchronisation class attributes and methods

# timedAutomata_expressions_VariableExpression class attributes and methods

# timedAutomata_expressions_Expression class attributes and methods

# Commentable class attributes and methods

# timedAutomata_expressions_ConstantExpression class attributes and methods
timedAutomata_expressions_ConstantExpression_value: Property = Property(name="value", type=IntegerType)
timedAutomata_expressions_ConstantExpression.attributes={timedAutomata_expressions_ConstantExpression_value}

# Expression class attributes and methods

# Identifier class attributes and methods

# timedAutomata_expressions_ArrayVariableExpression class attributes and methods

# timedAutomata_expressions_IncDecExpression class attributes and methods
timedAutomata_expressions_IncDecExpression_beforeExpression: Property = Property(name="beforeExpression", type=BooleanType)
timedAutomata_expressions_IncDecExpression_increment: Property = Property(name="increment", type=BooleanType)
timedAutomata_expressions_IncDecExpression.attributes={timedAutomata_expressions_IncDecExpression_beforeExpression, timedAutomata_expressions_IncDecExpression_increment}

# timedAutomata_expressions_GroupingExpression class attributes and methods

# timedAutomata_expressions_BinaryExpression class attributes and methods
timedAutomata_expressions_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
timedAutomata_expressions_BinaryExpression.attributes={timedAutomata_expressions_BinaryExpression_operator}

# timedAutomata_expressions_AssignmentExpression class attributes and methods
timedAutomata_expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
timedAutomata_expressions_AssignmentExpression.attributes={timedAutomata_expressions_AssignmentExpression_operator}

# timedAutomata_expressions_UnaryExpression class attributes and methods
timedAutomata_expressions_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
timedAutomata_expressions_UnaryExpression.attributes={timedAutomata_expressions_UnaryExpression_operator}

# timedAutomata_expressions_SimpleIfExpression class attributes and methods

# timedAutomata_expressions_IdentifierExpression class attributes and methods

# timedAutomata_expressions_WithArgumentsExpression class attributes and methods

# timedAutomata_expressions_PointExpression class attributes and methods

# timedAutomata_expressions_ForallExpression class attributes and methods

# types_Type class attributes and methods

# timedAutomata_expressions_ExistsExpression class attributes and methods

# timedAutomata_expressions_FixedExpression class attributes and methods
timedAutomata_expressions_FixedExpression_type: Property = Property(name="type", type=StringType)
timedAutomata_expressions_FixedExpression.attributes={timedAutomata_expressions_FixedExpression_type}

# timedAutomata_expressions_Selection class attributes and methods

# timedAutomata_declarations_Declaration class attributes and methods

# timedAutomata_declarations_VariableDeclaration class attributes and methods

# Declaration class attributes and methods

# declarations_VariableIdentifier class attributes and methods

# timedAutomata_declarations_VariableIdentifier class attributes and methods

# declarations_ArrayDeclarationType class attributes and methods

# declarations_Initialiser class attributes and methods

# declarations_ArrayDeclaration class attributes and methods

# timedAutomata_declarations_FunctionDeclaration class attributes and methods

# declarations_TAParameter class attributes and methods

# declarations_Block class attributes and methods

# timedAutomata_declarations_ChannelPriorityDeclaration class attributes and methods

# declarations_ChannelPriority class attributes and methods

# timedAutomata_declarations_FieldDeclaration class attributes and methods

# timedAutomata_declarations_ArrayDeclaration class attributes and methods

# timedAutomata_declarations_TypeDeclaration class attributes and methods

# timedAutomata_declarations_ArrayDeclarationType class attributes and methods

# timedAutomata_declarations_ArrayExpressionType class attributes and methods

# ArrayDeclarationType class attributes and methods

# timedAutomata_declarations_ArrayTypeType class attributes and methods

# timedAutomata_declarations_Initialiser class attributes and methods

# timedAutomata_declarations_ExpressionInitialiser class attributes and methods

# Initialiser class attributes and methods

# timedAutomata_declarations_ArrayInitialiser class attributes and methods

# timedAutomata_declarations_TAParameter class attributes and methods

# timedAutomata_declarations_CallByValueParameter class attributes and methods

# TAParameter class attributes and methods

# timedAutomata_declarations_CallByReferenceParameter class attributes and methods

# timedAutomata_declarations_Block class attributes and methods

# declarations_Declaration class attributes and methods

# declarations_Statement class attributes and methods

# timedAutomata_declarations_Statement class attributes and methods

# timedAutomata_declarations_BlockStatement class attributes and methods

# timedAutomata_declarations_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# timedAutomata_declarations_ForLoopStatement class attributes and methods

# timedAutomata_declarations_IterationStatement class attributes and methods

# timedAutomata_declarations_WhileLoopStatement class attributes and methods

# timedAutomata_declarations_DoWhileLoopStatement class attributes and methods

# timedAutomata_declarations_IfStatement class attributes and methods

# timedAutomata_declarations_ReturnStatement class attributes and methods

# timedAutomata_declarations_ChannelPriority class attributes and methods

# timedAutomata_declarations_DefaultChannelPriority class attributes and methods

# ChannelPriority class attributes and methods

# timedAutomata_declarations_SimpleChannelPriority class attributes and methods

# declarations_ChannelExpression class attributes and methods

# timedAutomata_declarations_ComplexChannelPriority class attributes and methods
timedAutomata_declarations_ComplexChannelPriority_channelOperator: Property = Property(name="channelOperator", type=StringType)
timedAutomata_declarations_ComplexChannelPriority.attributes={timedAutomata_declarations_ComplexChannelPriority_channelOperator}

# timedAutomata_declarations_ChannelExpression class attributes and methods

# timedAutomata_declarations_IdentifierChannelExpression class attributes and methods

# ChannelExpression class attributes and methods

# timedAutomata_declarations_ExpressionChannelExpression class attributes and methods

# timedAutomata_types_Type class attributes and methods
timedAutomata_types_Type_prefix: Property = Property(name="prefix", type=StringType)
timedAutomata_types_Type.attributes={timedAutomata_types_Type_prefix}

# timedAutomata_types_IdentifierType class attributes and methods

# Type class attributes and methods

# timedAutomata_types_SimpleType class attributes and methods
timedAutomata_types_SimpleType_type: Property = Property(name="type", type=StringType)
timedAutomata_types_SimpleType.attributes={timedAutomata_types_SimpleType_type}

# timedAutomata_types_IntegerRange class attributes and methods

# timedAutomata_core_Project class attributes and methods
timedAutomata_core_Project_id: Property = Property(name="id", type=StringType)
timedAutomata_core_Project.attributes={timedAutomata_core_Project_id}

# TAElement class attributes and methods

# Template class attributes and methods

# timedAutomata_types_Scalar class attributes and methods

# SystemDefinition class attributes and methods

# timedAutomata_core_Template class attributes and methods

# timedAutomata_types_Struct class attributes and methods

# declarations_FieldDeclaration class attributes and methods

# Guards class attributes and methods

# Selections class attributes and methods

# core_TAElement class attributes and methods

# base_Nameable class attributes and methods

# base_Identifyable class attributes and methods

# Location class attributes and methods

# core_timedAutomata_Parameter class attributes and methods

# Edge class attributes and methods

# timedAutomata_core_Edge class attributes and methods

# timedAutomata_core_SystemDefinition class attributes and methods

# TemplateInstantiation class attributes and methods

# System class attributes and methods

# timedAutomata_core_System class attributes and methods

# timedAutomata_core_SimpleSystem class attributes and methods

# Updates class attributes and methods

# core_timedAutomata_Nail class attributes and methods

# timedAutomata_core_TAElement class attributes and methods

# base_Commentable class attributes and methods

# timedAutomata_core_Location class attributes and methods
timedAutomata_core_Location_urgent: Property = Property(name="urgent", type=StringType)
timedAutomata_core_Location_committed: Property = Property(name="committed", type=StringType)
timedAutomata_core_Location.attributes={timedAutomata_core_Location_committed, timedAutomata_core_Location_urgent}

# core_timedAutomata_Label class attributes and methods

# timedAutomata_core_TemplateInstantiation class attributes and methods

# timedAutomata_core_ComplexSystem class attributes and methods
timedAutomata_core_ComplexSystem_operator: Property = Property(name="operator", type=StringType)
timedAutomata_core_ComplexSystem.attributes={timedAutomata_core_ComplexSystem_operator}

# timedAutomata_core_Selections class attributes and methods

# expressions_Selection class attributes and methods

# timedAutomata_core_Updates class attributes and methods

# timedAutomata_core_Guards class attributes and methods

# Relationships
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="expressions_Expression", type=timedAutomata_bnf_Synchronisation, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_bnf_Synchronisation", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="expressions_Expression15", type=timedAutomata_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_BinaryExpression14", type=expressions_Expression, multiplicity=Multiplicity(1, 1))
    }
)
identifier1: BinaryAssociation = BinaryAssociation(
    name="identifier1",
    ends={
        Property(name="Identifier", type=timedAutomata_expressions_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_VariableExpression", type=Identifier, multiplicity=Multiplicity(1, 1))
    }
)
expression2: BinaryAssociation = BinaryAssociation(
    name="expression2",
    ends={
        Property(name="expressions_Expression3", type=timedAutomata_expressions_ArrayVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ArrayVariableExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
position4: BinaryAssociation = BinaryAssociation(
    name="position4",
    ends={
        Property(name="expressions_Expression6", type=timedAutomata_expressions_ArrayVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ArrayVariableExpression5", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
expression7: BinaryAssociation = BinaryAssociation(
    name="expression7",
    ends={
        Property(name="expressions_Expression8", type=timedAutomata_expressions_IncDecExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_IncDecExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
expression9: BinaryAssociation = BinaryAssociation(
    name="expression9",
    ends={
        Property(name="expressions_Expression10", type=timedAutomata_expressions_GroupingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_GroupingExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="expressions_Expression12", type=timedAutomata_expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_BinaryExpression", type=expressions_Expression, multiplicity=Multiplicity(1, 1))
    }
)
leftSide16: BinaryAssociation = BinaryAssociation(
    name="leftSide16",
    ends={
        Property(name="expressions_Expression17", type=timedAutomata_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_AssignmentExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
rightSide18: BinaryAssociation = BinaryAssociation(
    name="rightSide18",
    ends={
        Property(name="expressions_Expression20", type=timedAutomata_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_AssignmentExpression19", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="expressions_Expression22", type=timedAutomata_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_UnaryExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
if23: BinaryAssociation = BinaryAssociation(
    name="if23",
    ends={
        Property(name="expressions_Expression24", type=timedAutomata_expressions_SimpleIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_SimpleIfExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
then25: BinaryAssociation = BinaryAssociation(
    name="then25",
    ends={
        Property(name="expressions_Expression27", type=timedAutomata_expressions_SimpleIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_SimpleIfExpression26", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
else28: BinaryAssociation = BinaryAssociation(
    name="else28",
    ends={
        Property(name="expressions_Expression30", type=timedAutomata_expressions_SimpleIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_SimpleIfExpression29", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier31: BinaryAssociation = BinaryAssociation(
    name="identifier31",
    ends={
        Property(name="Identifier32", type=timedAutomata_expressions_IdentifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_IdentifierExpression", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
expression33: BinaryAssociation = BinaryAssociation(
    name="expression33",
    ends={
        Property(name="expressions_Expression34", type=timedAutomata_expressions_WithArgumentsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_WithArgumentsExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
arguments35: BinaryAssociation = BinaryAssociation(
    name="arguments35",
    ends={
        Property(name="expressions_Expression37", type=timedAutomata_expressions_WithArgumentsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_WithArgumentsExpression36", type=expressions_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="expressions_Expression39", type=timedAutomata_expressions_PointExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_PointExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier40: BinaryAssociation = BinaryAssociation(
    name="identifier40",
    ends={
        Property(name="Identifier42", type=timedAutomata_expressions_PointExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_PointExpression41", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
identifier43: BinaryAssociation = BinaryAssociation(
    name="identifier43",
    ends={
        Property(name="Identifier44", type=timedAutomata_expressions_ForallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ForallExpression", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="types_Type", type=timedAutomata_expressions_ForallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ForallExpression46", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
expression47: BinaryAssociation = BinaryAssociation(
    name="expression47",
    ends={
        Property(name="expressions_Expression49", type=timedAutomata_expressions_ForallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ForallExpression48", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier50: BinaryAssociation = BinaryAssociation(
    name="identifier50",
    ends={
        Property(name="expressions_Expression51", type=timedAutomata_expressions_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ExistsExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="types_Type54", type=timedAutomata_expressions_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ExistsExpression53", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="expressions_Expression57", type=timedAutomata_expressions_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_ExistsExpression56", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier58: BinaryAssociation = BinaryAssociation(
    name="identifier58",
    ends={
        Property(name="Identifier59", type=timedAutomata_expressions_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_expressions_Selection", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="types_Type61", type=timedAutomata_declarations_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_VariableDeclaration", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
variableIdentifiers62: BinaryAssociation = BinaryAssociation(
    name="variableIdentifiers62",
    ends={
        Property(name="declarations_VariableIdentifier", type=timedAutomata_declarations_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_VariableDeclaration63", type=declarations_VariableIdentifier, multiplicity=Multiplicity(1, 100))
    }
)
identifier64: BinaryAssociation = BinaryAssociation(
    name="identifier64",
    ends={
        Property(name="Identifier65", type=timedAutomata_declarations_VariableIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_VariableIdentifier", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
arrayDeclarationTypes66: BinaryAssociation = BinaryAssociation(
    name="arrayDeclarationTypes66",
    ends={
        Property(name="declarations_ArrayDeclarationType", type=timedAutomata_declarations_VariableIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_VariableIdentifier67", type=declarations_ArrayDeclarationType, multiplicity=Multiplicity(0, 100))
    }
)
initialiser68: BinaryAssociation = BinaryAssociation(
    name="initialiser68",
    ends={
        Property(name="declarations_Initialiser", type=timedAutomata_declarations_VariableIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_VariableIdentifier69", type=declarations_Initialiser, multiplicity=Multiplicity(0, 1))
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="types_Type71", type=timedAutomata_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_TypeDeclaration", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
arrayDeclarations72: BinaryAssociation = BinaryAssociation(
    name="arrayDeclarations72",
    ends={
        Property(name="declarations_ArrayDeclaration", type=timedAutomata_declarations_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_TypeDeclaration73", type=declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 100))
    }
)
type74: BinaryAssociation = BinaryAssociation(
    name="type74",
    ends={
        Property(name="types_Type75", type=timedAutomata_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FunctionDeclaration", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
identifier76: BinaryAssociation = BinaryAssociation(
    name="identifier76",
    ends={
        Property(name="Identifier78", type=timedAutomata_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FunctionDeclaration77", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
parameters79: BinaryAssociation = BinaryAssociation(
    name="parameters79",
    ends={
        Property(name="declarations_TAParameter", type=timedAutomata_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FunctionDeclaration80", type=declarations_TAParameter, multiplicity=Multiplicity(0, 100))
    }
)
block81: BinaryAssociation = BinaryAssociation(
    name="block81",
    ends={
        Property(name="declarations_Block", type=timedAutomata_declarations_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FunctionDeclaration82", type=declarations_Block, multiplicity=Multiplicity(0, 1))
    }
)
channelPriority83: BinaryAssociation = BinaryAssociation(
    name="channelPriority83",
    ends={
        Property(name="declarations_ChannelPriority", type=timedAutomata_declarations_ChannelPriorityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ChannelPriorityDeclaration", type=declarations_ChannelPriority, multiplicity=Multiplicity(0, 1))
    }
)
type84: BinaryAssociation = BinaryAssociation(
    name="type84",
    ends={
        Property(name="types_Type85", type=timedAutomata_declarations_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FieldDeclaration", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
arrayDeclarations86: BinaryAssociation = BinaryAssociation(
    name="arrayDeclarations86",
    ends={
        Property(name="declarations_ArrayDeclaration88", type=timedAutomata_declarations_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_FieldDeclaration87", type=declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 100))
    }
)
types91: BinaryAssociation = BinaryAssociation(
    name="types91",
    ends={
        Property(name="declarations_ArrayDeclarationType93", type=timedAutomata_declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ArrayDeclaration92", type=declarations_ArrayDeclarationType, multiplicity=Multiplicity(0, 100))
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="expressions_Expression95", type=timedAutomata_declarations_ArrayExpressionType, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ArrayExpressionType", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="types_Type97", type=timedAutomata_declarations_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ArrayTypeType", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
expression98: BinaryAssociation = BinaryAssociation(
    name="expression98",
    ends={
        Property(name="expressions_Expression99", type=timedAutomata_declarations_ExpressionInitialiser, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ExpressionInitialiser", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
initialisers100: BinaryAssociation = BinaryAssociation(
    name="initialisers100",
    ends={
        Property(name="declarations_Initialiser101", type=timedAutomata_declarations_ArrayInitialiser, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ArrayInitialiser", type=declarations_Initialiser, multiplicity=Multiplicity(1, 100))
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="types_Type103", type=timedAutomata_declarations_TAParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_TAParameter", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
arrayDeclaration104: BinaryAssociation = BinaryAssociation(
    name="arrayDeclaration104",
    ends={
        Property(name="declarations_ArrayDeclaration106", type=timedAutomata_declarations_TAParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_TAParameter105", type=declarations_ArrayDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
declarations107: BinaryAssociation = BinaryAssociation(
    name="declarations107",
    ends={
        Property(name="declarations_Declaration", type=timedAutomata_declarations_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_Block", type=declarations_Declaration, multiplicity=Multiplicity(0, 100))
    }
)
statements108: BinaryAssociation = BinaryAssociation(
    name="statements108",
    ends={
        Property(name="declarations_Statement", type=timedAutomata_declarations_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_Block109", type=declarations_Statement, multiplicity=Multiplicity(0, 100))
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="expressions_Expression111", type=timedAutomata_declarations_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ExpressionStatement", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
initExpression112: BinaryAssociation = BinaryAssociation(
    name="initExpression112",
    ends={
        Property(name="expressions_Expression113", type=timedAutomata_declarations_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ForLoopStatement", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier89: BinaryAssociation = BinaryAssociation(
    name="identifier89",
    ends={
        Property(name="Identifier90", type=timedAutomata_declarations_ArrayDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ArrayDeclaration", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
terminalExpression117: BinaryAssociation = BinaryAssociation(
    name="terminalExpression117",
    ends={
        Property(name="expressions_Expression119", type=timedAutomata_declarations_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ForLoopStatement118", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
statement120: BinaryAssociation = BinaryAssociation(
    name="statement120",
    ends={
        Property(name="declarations_Statement122", type=timedAutomata_declarations_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ForLoopStatement121", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
identifier123: BinaryAssociation = BinaryAssociation(
    name="identifier123",
    ends={
        Property(name="Identifier124", type=timedAutomata_declarations_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IterationStatement", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
type125: BinaryAssociation = BinaryAssociation(
    name="type125",
    ends={
        Property(name="types_Type127", type=timedAutomata_declarations_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IterationStatement126", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
statement128: BinaryAssociation = BinaryAssociation(
    name="statement128",
    ends={
        Property(name="declarations_Statement130", type=timedAutomata_declarations_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IterationStatement129", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
condition131: BinaryAssociation = BinaryAssociation(
    name="condition131",
    ends={
        Property(name="expressions_Expression132", type=timedAutomata_declarations_WhileLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_WhileLoopStatement", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
statement133: BinaryAssociation = BinaryAssociation(
    name="statement133",
    ends={
        Property(name="declarations_Statement135", type=timedAutomata_declarations_WhileLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_WhileLoopStatement134", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
statement136: BinaryAssociation = BinaryAssociation(
    name="statement136",
    ends={
        Property(name="declarations_Statement137", type=timedAutomata_declarations_DoWhileLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_DoWhileLoopStatement", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
condition138: BinaryAssociation = BinaryAssociation(
    name="condition138",
    ends={
        Property(name="expressions_Expression140", type=timedAutomata_declarations_DoWhileLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_DoWhileLoopStatement139", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
condition141: BinaryAssociation = BinaryAssociation(
    name="condition141",
    ends={
        Property(name="expressions_Expression142", type=timedAutomata_declarations_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IfStatement", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
if143: BinaryAssociation = BinaryAssociation(
    name="if143",
    ends={
        Property(name="declarations_Statement145", type=timedAutomata_declarations_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IfStatement144", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
else146: BinaryAssociation = BinaryAssociation(
    name="else146",
    ends={
        Property(name="declarations_Statement148", type=timedAutomata_declarations_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IfStatement147", type=declarations_Statement, multiplicity=Multiplicity(0, 1))
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="expressions_Expression150", type=timedAutomata_declarations_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ReturnStatement", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
channelExpression151: BinaryAssociation = BinaryAssociation(
    name="channelExpression151",
    ends={
        Property(name="declarations_ChannelExpression", type=timedAutomata_declarations_SimpleChannelPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_SimpleChannelPriority", type=declarations_ChannelExpression, multiplicity=Multiplicity(0, 1))
    }
)
loopConditionExpression114: BinaryAssociation = BinaryAssociation(
    name="loopConditionExpression114",
    ends={
        Property(name="expressions_Expression116", type=timedAutomata_declarations_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ForLoopStatement115", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
leftSideChannelExpression152: BinaryAssociation = BinaryAssociation(
    name="leftSideChannelExpression152",
    ends={
        Property(name="timedAutomata_declarations_ComplexChannelPriority", type=declarations_ChannelExpression, multiplicity=Multiplicity(0, 1)),
        Property(name="declarations_ChannelExpression153", type=timedAutomata_declarations_ComplexChannelPriority, multiplicity=Multiplicity(1, 1))
    }
)
rightSideChannelExpression154: BinaryAssociation = BinaryAssociation(
    name="rightSideChannelExpression154",
    ends={
        Property(name="declarations_ChannelPriority156", type=timedAutomata_declarations_ComplexChannelPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ComplexChannelPriority155", type=declarations_ChannelPriority, multiplicity=Multiplicity(0, 1))
    }
)
identifier157: BinaryAssociation = BinaryAssociation(
    name="identifier157",
    ends={
        Property(name="Identifier158", type=timedAutomata_declarations_IdentifierChannelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_IdentifierChannelExpression", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
channelExpression159: BinaryAssociation = BinaryAssociation(
    name="channelExpression159",
    ends={
        Property(name="declarations_ChannelExpression160", type=timedAutomata_declarations_ExpressionChannelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ExpressionChannelExpression", type=declarations_ChannelExpression, multiplicity=Multiplicity(0, 1))
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="expressions_Expression163", type=timedAutomata_declarations_ExpressionChannelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_declarations_ExpressionChannelExpression162", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
identifier164: BinaryAssociation = BinaryAssociation(
    name="identifier164",
    ends={
        Property(name="Identifier165", type=timedAutomata_types_IdentifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_types_IdentifierType", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
firstIndex166: BinaryAssociation = BinaryAssociation(
    name="firstIndex166",
    ends={
        Property(name="expressions_Expression167", type=timedAutomata_types_IntegerRange, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_types_IntegerRange", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
globalDeclarations174: BinaryAssociation = BinaryAssociation(
    name="globalDeclarations174",
    ends={
        Property(name="declarations_Declaration175", type=timedAutomata_core_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Project", type=declarations_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
secondIndex168: BinaryAssociation = BinaryAssociation(
    name="secondIndex168",
    ends={
        Property(name="expressions_Expression170", type=timedAutomata_types_IntegerRange, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_types_IntegerRange169", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
templates176: BinaryAssociation = BinaryAssociation(
    name="templates176",
    ends={
        Property(name="Template", type=timedAutomata_core_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Project177", type=Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scalar171: BinaryAssociation = BinaryAssociation(
    name="scalar171",
    ends={
        Property(name="expressions_Expression172", type=timedAutomata_types_Scalar, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_types_Scalar", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
systemDeclaration178: BinaryAssociation = BinaryAssociation(
    name="systemDeclaration178",
    ends={
        Property(name="SystemDefinition", type=timedAutomata_core_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Project179", type=SystemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
fieldDeclarations173: BinaryAssociation = BinaryAssociation(
    name="fieldDeclarations173",
    ends={
        Property(name="declarations_FieldDeclaration", type=timedAutomata_types_Struct, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_types_Struct", type=declarations_FieldDeclaration, multiplicity=Multiplicity(1, 100))
    }
)
source191: BinaryAssociation = BinaryAssociation(
    name="source191",
    ends={
        Property(name="Location192", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
target193: BinaryAssociation = BinaryAssociation(
    name="target193",
    ends={
        Property(name="Location195", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge194", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
guards196: BinaryAssociation = BinaryAssociation(
    name="guards196",
    ends={
        Property(name="Guards", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge197", type=Guards, multiplicity=Multiplicity(1, 1))
    }
)
synchronisation198: BinaryAssociation = BinaryAssociation(
    name="synchronisation198",
    ends={
        Property(name="Synchronisation", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge199", type=Synchronisation, multiplicity=Multiplicity(1, 1))
    }
)
selections200: BinaryAssociation = BinaryAssociation(
    name="selections200",
    ends={
        Property(name="Selections", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge201", type=Selections, multiplicity=Multiplicity(1, 1))
    }
)
declarations180: BinaryAssociation = BinaryAssociation(
    name="declarations180",
    ends={
        Property(name="declarations_Declaration181", type=timedAutomata_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Template", type=declarations_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial182: BinaryAssociation = BinaryAssociation(
    name="initial182",
    ends={
        Property(name="Location", type=timedAutomata_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Template183", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
taParameters184: BinaryAssociation = BinaryAssociation(
    name="taParameters184",
    ends={
        Property(name="core_timedAutomata_Parameter", type=timedAutomata_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Template185", type=core_timedAutomata_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
locations186: BinaryAssociation = BinaryAssociation(
    name="locations186",
    ends={
        Property(name="Location188", type=timedAutomata_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Template187", type=Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges189: BinaryAssociation = BinaryAssociation(
    name="edges189",
    ends={
        Property(name="Edge", type=timedAutomata_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Template190", type=Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label208: BinaryAssociation = BinaryAssociation(
    name="label208",
    ends={
        Property(name="core_timedAutomata_Label", type=timedAutomata_core_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Location209", type=core_timedAutomata_Label, multiplicity=Multiplicity(0, 1))
    }
)
templateInstantiations210: BinaryAssociation = BinaryAssociation(
    name="templateInstantiations210",
    ends={
        Property(name="TemplateInstantiation", type=timedAutomata_core_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_SystemDefinition", type=TemplateInstantiation, multiplicity=Multiplicity(0, 9999))
    }
)
systems211: BinaryAssociation = BinaryAssociation(
    name="systems211",
    ends={
        Property(name="System", type=timedAutomata_core_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_SystemDefinition212", type=System, multiplicity=Multiplicity(0, 1))
    }
)
updates202: BinaryAssociation = BinaryAssociation(
    name="updates202",
    ends={
        Property(name="Updates", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge203", type=Updates, multiplicity=Multiplicity(1, 1))
    }
)
nails204: BinaryAssociation = BinaryAssociation(
    name="nails204",
    ends={
        Property(name="core_timedAutomata_Nail", type=timedAutomata_core_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Edge205", type=core_timedAutomata_Nail, multiplicity=Multiplicity(0, 9999))
    }
)
invariant206: BinaryAssociation = BinaryAssociation(
    name="invariant206",
    ends={
        Property(name="expressions_Expression207", type=timedAutomata_core_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Location", type=expressions_Expression, multiplicity=Multiplicity(0, 1))
    }
)
rightSideSystem217: BinaryAssociation = BinaryAssociation(
    name="rightSideSystem217",
    ends={
        Property(name="timedAutomata_core_ComplexSystem218", type=System, multiplicity=Multiplicity(0, 1)),
        Property(name="System219", type=timedAutomata_core_ComplexSystem, multiplicity=Multiplicity(1, 1))
    }
)
processIdentifier220: BinaryAssociation = BinaryAssociation(
    name="processIdentifier220",
    ends={
        Property(name="Identifier221", type=timedAutomata_core_TemplateInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_TemplateInstantiation", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
Identifier213: BinaryAssociation = BinaryAssociation(
    name="Identifier213",
    ends={
        Property(name="Identifier214", type=timedAutomata_core_SimpleSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_SimpleSystem", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
leftSideSystem215: BinaryAssociation = BinaryAssociation(
    name="leftSideSystem215",
    ends={
        Property(name="System216", type=timedAutomata_core_ComplexSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_ComplexSystem", type=System, multiplicity=Multiplicity(0, 1))
    }
)
selections231: BinaryAssociation = BinaryAssociation(
    name="selections231",
    ends={
        Property(name="expressions_Selection", type=timedAutomata_core_Selections, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Selections", type=expressions_Selection, multiplicity=Multiplicity(0, 9999))
    }
)
expressions232: BinaryAssociation = BinaryAssociation(
    name="expressions232",
    ends={
        Property(name="expressions_Expression233", type=timedAutomata_core_Updates, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Updates", type=expressions_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
processParameters222: BinaryAssociation = BinaryAssociation(
    name="processParameters222",
    ends={
        Property(name="declarations_TAParameter224", type=timedAutomata_core_TemplateInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_TemplateInstantiation223", type=declarations_TAParameter, multiplicity=Multiplicity(0, 9999))
    }
)
templateIdentifier225: BinaryAssociation = BinaryAssociation(
    name="templateIdentifier225",
    ends={
        Property(name="Identifier227", type=timedAutomata_core_TemplateInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_TemplateInstantiation226", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
templateArguments228: BinaryAssociation = BinaryAssociation(
    name="templateArguments228",
    ends={
        Property(name="expressions_Expression230", type=timedAutomata_core_TemplateInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_TemplateInstantiation229", type=expressions_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
conditions234: BinaryAssociation = BinaryAssociation(
    name="conditions234",
    ends={
        Property(name="expressions_Expression235", type=timedAutomata_core_Guards, multiplicity=Multiplicity(1, 1)),
        Property(name="timedAutomata_core_Guards", type=expressions_Expression, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_timedAutomata_bnf_Synchronisation_Position = Generalization(general=Position, specific=timedAutomata_bnf_Synchronisation)
gen_timedAutomata_bnf_SendSynchronisation_Synchronisation = Generalization(general=Synchronisation, specific=timedAutomata_bnf_SendSynchronisation)
gen_timedAutomata_bnf_ReceiveSynchronisation_Synchronisation = Generalization(general=Synchronisation, specific=timedAutomata_bnf_ReceiveSynchronisation)
gen_timedAutomata_expressions_VariableExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_VariableExpression)
gen_timedAutomata_expressions_Expression_Commentable = Generalization(general=Commentable, specific=timedAutomata_expressions_Expression)
gen_timedAutomata_expressions_ConstantExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_ConstantExpression)
gen_timedAutomata_expressions_ArrayVariableExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_ArrayVariableExpression)
gen_timedAutomata_expressions_IncDecExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_IncDecExpression)
gen_timedAutomata_expressions_GroupingExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_GroupingExpression)
gen_timedAutomata_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_BinaryExpression)
gen_timedAutomata_expressions_WithArgumentsExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_WithArgumentsExpression)
gen_timedAutomata_expressions_AssignmentExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_AssignmentExpression)
gen_timedAutomata_expressions_UnaryExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_UnaryExpression)
gen_timedAutomata_expressions_SimpleIfExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_SimpleIfExpression)
gen_timedAutomata_expressions_IdentifierExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_IdentifierExpression)
gen_timedAutomata_expressions_PointExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_PointExpression)
gen_timedAutomata_expressions_ForallExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_ForallExpression)
gen_timedAutomata_expressions_ExistsExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_ExistsExpression)
gen_timedAutomata_expressions_FixedExpression_Expression = Generalization(general=Expression, specific=timedAutomata_expressions_FixedExpression)
gen_timedAutomata_declarations_Declaration_Commentable = Generalization(general=Commentable, specific=timedAutomata_declarations_Declaration)
gen_timedAutomata_declarations_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=timedAutomata_declarations_VariableDeclaration)
gen_timedAutomata_declarations_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=timedAutomata_declarations_FunctionDeclaration)
gen_timedAutomata_declarations_ChannelPriorityDeclaration_Declaration = Generalization(general=Declaration, specific=timedAutomata_declarations_ChannelPriorityDeclaration)
gen_timedAutomata_declarations_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=timedAutomata_declarations_TypeDeclaration)
gen_timedAutomata_declarations_ArrayExpressionType_ArrayDeclarationType = Generalization(general=ArrayDeclarationType, specific=timedAutomata_declarations_ArrayExpressionType)
gen_timedAutomata_declarations_ArrayTypeType_ArrayDeclarationType = Generalization(general=ArrayDeclarationType, specific=timedAutomata_declarations_ArrayTypeType)
gen_timedAutomata_declarations_ExpressionInitialiser_Initialiser = Generalization(general=Initialiser, specific=timedAutomata_declarations_ExpressionInitialiser)
gen_timedAutomata_declarations_ArrayInitialiser_Initialiser = Generalization(general=Initialiser, specific=timedAutomata_declarations_ArrayInitialiser)
gen_timedAutomata_declarations_CallByValueParameter_TAParameter = Generalization(general=TAParameter, specific=timedAutomata_declarations_CallByValueParameter)
gen_timedAutomata_declarations_CallByReferenceParameter_TAParameter = Generalization(general=TAParameter, specific=timedAutomata_declarations_CallByReferenceParameter)
gen_timedAutomata_declarations_BlockStatement_declarations_Statement = Generalization(general=declarations_Statement, specific=timedAutomata_declarations_BlockStatement)
gen_timedAutomata_declarations_BlockStatement_declarations_Block = Generalization(general=declarations_Block, specific=timedAutomata_declarations_BlockStatement)
gen_timedAutomata_declarations_ExpressionStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_ExpressionStatement)
gen_timedAutomata_declarations_ForLoopStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_ForLoopStatement)
gen_timedAutomata_declarations_IterationStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_IterationStatement)
gen_timedAutomata_declarations_WhileLoopStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_WhileLoopStatement)
gen_timedAutomata_declarations_DoWhileLoopStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_DoWhileLoopStatement)
gen_timedAutomata_declarations_IfStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_IfStatement)
gen_timedAutomata_declarations_ReturnStatement_Statement = Generalization(general=Statement, specific=timedAutomata_declarations_ReturnStatement)
gen_timedAutomata_declarations_DefaultChannelPriority_ChannelPriority = Generalization(general=ChannelPriority, specific=timedAutomata_declarations_DefaultChannelPriority)
gen_timedAutomata_declarations_SimpleChannelPriority_ChannelPriority = Generalization(general=ChannelPriority, specific=timedAutomata_declarations_SimpleChannelPriority)
gen_timedAutomata_declarations_ComplexChannelPriority_ChannelPriority = Generalization(general=ChannelPriority, specific=timedAutomata_declarations_ComplexChannelPriority)
gen_timedAutomata_declarations_IdentifierChannelExpression_ChannelExpression = Generalization(general=ChannelExpression, specific=timedAutomata_declarations_IdentifierChannelExpression)
gen_timedAutomata_declarations_ExpressionChannelExpression_ChannelExpression = Generalization(general=ChannelExpression, specific=timedAutomata_declarations_ExpressionChannelExpression)
gen_timedAutomata_types_IdentifierType_Type = Generalization(general=Type, specific=timedAutomata_types_IdentifierType)
gen_timedAutomata_types_SimpleType_Type = Generalization(general=Type, specific=timedAutomata_types_SimpleType)
gen_timedAutomata_types_IntegerRange_Type = Generalization(general=Type, specific=timedAutomata_types_IntegerRange)
gen_timedAutomata_core_Project_TAElement = Generalization(general=TAElement, specific=timedAutomata_core_Project)
gen_timedAutomata_types_Scalar_Type = Generalization(general=Type, specific=timedAutomata_types_Scalar)
gen_timedAutomata_types_Struct_Type = Generalization(general=Type, specific=timedAutomata_types_Struct)
gen_timedAutomata_core_Template_core_TAElement = Generalization(general=core_TAElement, specific=timedAutomata_core_Template)
gen_timedAutomata_core_Template_base_Nameable = Generalization(general=base_Nameable, specific=timedAutomata_core_Template)
gen_timedAutomata_core_Template_base_Identifyable = Generalization(general=base_Identifyable, specific=timedAutomata_core_Template)
gen_timedAutomata_core_Edge_core_TAElement = Generalization(general=core_TAElement, specific=timedAutomata_core_Edge)
gen_timedAutomata_core_Edge_Position = Generalization(general=Position, specific=timedAutomata_core_Edge)
gen_timedAutomata_core_SimpleSystem_System = Generalization(general=System, specific=timedAutomata_core_SimpleSystem)
gen_timedAutomata_core_TAElement_base_Commentable = Generalization(general=base_Commentable, specific=timedAutomata_core_TAElement)
gen_timedAutomata_core_TAElement_base_Nameable = Generalization(general=base_Nameable, specific=timedAutomata_core_TAElement)
gen_timedAutomata_core_Location_core_TAElement = Generalization(general=core_TAElement, specific=timedAutomata_core_Location)
gen_timedAutomata_core_Location_Position = Generalization(general=Position, specific=timedAutomata_core_Location)
gen_timedAutomata_core_ComplexSystem_System = Generalization(general=System, specific=timedAutomata_core_ComplexSystem)
gen_timedAutomata_core_Selections_Position = Generalization(general=Position, specific=timedAutomata_core_Selections)
gen_timedAutomata_core_Updates_Position = Generalization(general=Position, specific=timedAutomata_core_Updates)
gen_timedAutomata_core_Guards_Position = Generalization(general=Position, specific=timedAutomata_core_Guards)

# Domain Model
domain_model = DomainModel(
    name="timedAutomata",
    types={timedAutomata_base_Commentable, timedAutomata_base_Identifyable, timedAutomata_base_Nameable, timedAutomata_bnf_Identifier, timedAutomata_bnf_Synchronisation, Position, expressions_Expression, timedAutomata_bnf_SendSynchronisation, Synchronisation, timedAutomata_bnf_ReceiveSynchronisation, timedAutomata_expressions_VariableExpression, timedAutomata_expressions_Expression, Commentable, timedAutomata_expressions_ConstantExpression, Expression, Identifier, timedAutomata_expressions_ArrayVariableExpression, timedAutomata_expressions_IncDecExpression, timedAutomata_expressions_GroupingExpression, timedAutomata_expressions_BinaryExpression, timedAutomata_expressions_AssignmentExpression, timedAutomata_expressions_UnaryExpression, timedAutomata_expressions_SimpleIfExpression, timedAutomata_expressions_IdentifierExpression, timedAutomata_expressions_WithArgumentsExpression, timedAutomata_expressions_PointExpression, timedAutomata_expressions_ForallExpression, types_Type, timedAutomata_expressions_ExistsExpression, timedAutomata_expressions_FixedExpression, timedAutomata_expressions_Selection, timedAutomata_declarations_Declaration, timedAutomata_declarations_VariableDeclaration, Declaration, declarations_VariableIdentifier, timedAutomata_declarations_VariableIdentifier, declarations_ArrayDeclarationType, declarations_Initialiser, declarations_ArrayDeclaration, timedAutomata_declarations_FunctionDeclaration, declarations_TAParameter, declarations_Block, timedAutomata_declarations_ChannelPriorityDeclaration, declarations_ChannelPriority, timedAutomata_declarations_FieldDeclaration, timedAutomata_declarations_ArrayDeclaration, timedAutomata_declarations_TypeDeclaration, timedAutomata_declarations_ArrayDeclarationType, timedAutomata_declarations_ArrayExpressionType, ArrayDeclarationType, timedAutomata_declarations_ArrayTypeType, timedAutomata_declarations_Initialiser, timedAutomata_declarations_ExpressionInitialiser, Initialiser, timedAutomata_declarations_ArrayInitialiser, timedAutomata_declarations_TAParameter, timedAutomata_declarations_CallByValueParameter, TAParameter, timedAutomata_declarations_CallByReferenceParameter, timedAutomata_declarations_Block, declarations_Declaration, declarations_Statement, timedAutomata_declarations_Statement, timedAutomata_declarations_BlockStatement, timedAutomata_declarations_ExpressionStatement, Statement, timedAutomata_declarations_ForLoopStatement, timedAutomata_declarations_IterationStatement, timedAutomata_declarations_WhileLoopStatement, timedAutomata_declarations_DoWhileLoopStatement, timedAutomata_declarations_IfStatement, timedAutomata_declarations_ReturnStatement, timedAutomata_declarations_ChannelPriority, timedAutomata_declarations_DefaultChannelPriority, ChannelPriority, timedAutomata_declarations_SimpleChannelPriority, declarations_ChannelExpression, timedAutomata_declarations_ComplexChannelPriority, timedAutomata_declarations_ChannelExpression, timedAutomata_declarations_IdentifierChannelExpression, ChannelExpression, timedAutomata_declarations_ExpressionChannelExpression, timedAutomata_types_Type, timedAutomata_types_IdentifierType, Type, timedAutomata_types_SimpleType, timedAutomata_types_IntegerRange, timedAutomata_core_Project, TAElement, Template, timedAutomata_types_Scalar, SystemDefinition, timedAutomata_core_Template, timedAutomata_types_Struct, declarations_FieldDeclaration, Guards, Selections, core_TAElement, base_Nameable, base_Identifyable, Location, core_timedAutomata_Parameter, Edge, timedAutomata_core_Edge, timedAutomata_core_SystemDefinition, TemplateInstantiation, System, timedAutomata_core_System, timedAutomata_core_SimpleSystem, Updates, core_timedAutomata_Nail, timedAutomata_core_TAElement, base_Commentable, timedAutomata_core_Location, core_timedAutomata_Label, timedAutomata_core_TemplateInstantiation, timedAutomata_core_ComplexSystem, timedAutomata_core_Selections, expressions_Selection, timedAutomata_core_Updates, timedAutomata_core_Guards, AssignOperator, BinaryOperator, UnaryOperator, FixedExpressionType, PriorityOperator, TypeId, TypePrefix},
    associations={expression0, right13, identifier1, expression2, position4, expression7, expression9, left11, leftSide16, rightSide18, expression21, if23, then25, else28, identifier31, expression33, arguments35, expression38, identifier40, identifier43, type45, expression47, identifier50, type52, expression55, identifier58, type60, variableIdentifiers62, identifier64, arrayDeclarationTypes66, initialiser68, type70, arrayDeclarations72, type74, identifier76, parameters79, block81, channelPriority83, type84, arrayDeclarations86, types91, expression94, type96, expression98, initialisers100, type102, arrayDeclaration104, declarations107, statements108, expression110, initExpression112, identifier89, terminalExpression117, statement120, identifier123, type125, statement128, condition131, statement133, statement136, condition138, condition141, if143, else146, expression149, channelExpression151, loopConditionExpression114, leftSideChannelExpression152, rightSideChannelExpression154, identifier157, channelExpression159, expression161, identifier164, firstIndex166, globalDeclarations174, secondIndex168, templates176, scalar171, systemDeclaration178, fieldDeclarations173, source191, target193, guards196, synchronisation198, selections200, declarations180, initial182, taParameters184, locations186, edges189, label208, templateInstantiations210, systems211, updates202, nails204, invariant206, rightSideSystem217, processIdentifier220, Identifier213, leftSideSystem215, selections231, expressions232, processParameters222, templateIdentifier225, templateArguments228, conditions234},
    generalizations={gen_timedAutomata_bnf_Synchronisation_Position, gen_timedAutomata_bnf_SendSynchronisation_Synchronisation, gen_timedAutomata_bnf_ReceiveSynchronisation_Synchronisation, gen_timedAutomata_expressions_VariableExpression_Expression, gen_timedAutomata_expressions_Expression_Commentable, gen_timedAutomata_expressions_ConstantExpression_Expression, gen_timedAutomata_expressions_ArrayVariableExpression_Expression, gen_timedAutomata_expressions_IncDecExpression_Expression, gen_timedAutomata_expressions_GroupingExpression_Expression, gen_timedAutomata_expressions_BinaryExpression_Expression, gen_timedAutomata_expressions_WithArgumentsExpression_Expression, gen_timedAutomata_expressions_AssignmentExpression_Expression, gen_timedAutomata_expressions_UnaryExpression_Expression, gen_timedAutomata_expressions_SimpleIfExpression_Expression, gen_timedAutomata_expressions_IdentifierExpression_Expression, gen_timedAutomata_expressions_PointExpression_Expression, gen_timedAutomata_expressions_ForallExpression_Expression, gen_timedAutomata_expressions_ExistsExpression_Expression, gen_timedAutomata_expressions_FixedExpression_Expression, gen_timedAutomata_declarations_Declaration_Commentable, gen_timedAutomata_declarations_VariableDeclaration_Declaration, gen_timedAutomata_declarations_FunctionDeclaration_Declaration, gen_timedAutomata_declarations_ChannelPriorityDeclaration_Declaration, gen_timedAutomata_declarations_TypeDeclaration_Declaration, gen_timedAutomata_declarations_ArrayExpressionType_ArrayDeclarationType, gen_timedAutomata_declarations_ArrayTypeType_ArrayDeclarationType, gen_timedAutomata_declarations_ExpressionInitialiser_Initialiser, gen_timedAutomata_declarations_ArrayInitialiser_Initialiser, gen_timedAutomata_declarations_CallByValueParameter_TAParameter, gen_timedAutomata_declarations_CallByReferenceParameter_TAParameter, gen_timedAutomata_declarations_BlockStatement_declarations_Statement, gen_timedAutomata_declarations_BlockStatement_declarations_Block, gen_timedAutomata_declarations_ExpressionStatement_Statement, gen_timedAutomata_declarations_ForLoopStatement_Statement, gen_timedAutomata_declarations_IterationStatement_Statement, gen_timedAutomata_declarations_WhileLoopStatement_Statement, gen_timedAutomata_declarations_DoWhileLoopStatement_Statement, gen_timedAutomata_declarations_IfStatement_Statement, gen_timedAutomata_declarations_ReturnStatement_Statement, gen_timedAutomata_declarations_DefaultChannelPriority_ChannelPriority, gen_timedAutomata_declarations_SimpleChannelPriority_ChannelPriority, gen_timedAutomata_declarations_ComplexChannelPriority_ChannelPriority, gen_timedAutomata_declarations_IdentifierChannelExpression_ChannelExpression, gen_timedAutomata_declarations_ExpressionChannelExpression_ChannelExpression, gen_timedAutomata_types_IdentifierType_Type, gen_timedAutomata_types_SimpleType_Type, gen_timedAutomata_types_IntegerRange_Type, gen_timedAutomata_core_Project_TAElement, gen_timedAutomata_types_Scalar_Type, gen_timedAutomata_types_Struct_Type, gen_timedAutomata_core_Template_core_TAElement, gen_timedAutomata_core_Template_base_Nameable, gen_timedAutomata_core_Template_base_Identifyable, gen_timedAutomata_core_Edge_core_TAElement, gen_timedAutomata_core_Edge_Position, gen_timedAutomata_core_SimpleSystem_System, gen_timedAutomata_core_TAElement_base_Commentable, gen_timedAutomata_core_TAElement_base_Nameable, gen_timedAutomata_core_Location_core_TAElement, gen_timedAutomata_core_Location_Position, gen_timedAutomata_core_ComplexSystem_System, gen_timedAutomata_core_Selections_Position, gen_timedAutomata_core_Updates_Position, gen_timedAutomata_core_Guards_Position},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)