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
ir_Scope = Class(name="ir::Scope")
Node = Class(name="Node")
ir_Declaration = Class(name="ir::Declaration")
ir_Node = Class(name="ir::Node")
ir_Annotation = Class(name="ir::Annotation")
ir_VariableImport = Class(name="ir::VariableImport")
Declaration = Class(name="Declaration")
ir_VariableExternal = Class(name="ir::VariableExternal")
ir_Type = Class(name="ir::Type")
ir_TypeDeclarationImport = Class(name="ir::TypeDeclarationImport")
ir_Namespace = Class(name="ir::Namespace")
Scope = Class(name="Scope")
ir_AbstractActor = Class(name="ir::AbstractActor")
ir_TypeActor = Class(name="ir::TypeActor")
ir_Port = Class(name="ir::Port")
ir_Variable = Class(name="ir::Variable")
ir_ExternalActor = Class(name="ir::ExternalActor")
AbstractActor = Class(name="AbstractActor")
ir_Actor = Class(name="ir::Actor")
ir_Action = Class(name="ir::Action")
ir_Schedule = Class(name="ir::Schedule")
ir_Network = Class(name="ir::Network")
ir_Connection = Class(name="ir::Connection")
ir_ActorInstance = Class(name="ir::ActorInstance")
ir_Guard = Class(name="ir::Guard")
ir_PortWrite = Class(name="ir::PortWrite")
ir_PortRead = Class(name="ir::PortRead")
ir_Statement = Class(name="ir::Statement")
Variable = Class(name="Variable")
ir_PortInstance = Class(name="ir::PortInstance")
ir_TaggedExpression = Class(name="ir::TaggedExpression")
ir_Expression = Class(name="ir::Expression")
ir_LiteralExpression = Class(name="ir::LiteralExpression")
Expression = Class(name="Expression")
ir_IntegerLiteral = Class(name="ir::IntegerLiteral")
LiteralExpression = Class(name="LiteralExpression")
ir_FloatLiteral = Class(name="ir::FloatLiteral")
ir_BooleanLiteral = Class(name="ir::BooleanLiteral")
ir_StringLiteral = Class(name="ir::StringLiteral")
ir_VariableExpression = Class(name="ir::VariableExpression")
ir_Member = Class(name="ir::Member")
ir_ListExpression = Class(name="ir::ListExpression")
ir_Generator = Class(name="ir::Generator")
ir_BinaryExpression = Class(name="ir::BinaryExpression")
ir_UnaryExpression = Class(name="ir::UnaryExpression")
ir_ExpressionCall = Class(name="ir::ExpressionCall")
ir_FunctionCall = Class(name="ir::FunctionCall")
ExpressionCall = Class(name="ExpressionCall")
ir_TypeConstructorCall = Class(name="ir::TypeConstructorCall")
ir_Point2PointConnection = Class(name="ir::Point2PointConnection")
Connection = Class(name="Connection")
ir_FromSource = Class(name="ir::FromSource")
ir_VariableReference = Class(name="ir::VariableReference")
ir_Assign = Class(name="ir::Assign")
Statement = Class(name="Statement")
ir_ReturnValue = Class(name="ir::ReturnValue")
ir_ProcCall = Class(name="ir::ProcCall")
ir_WhileLoop = Class(name="ir::WhileLoop")
ir_Block = Class(name="ir::Block")
ir_ForEach = Class(name="ir::ForEach")
ir_IfStatement = Class(name="ir::IfStatement")
ir_ToSink = Class(name="ir::ToSink")
ir_PortAccess = Class(name="ir::PortAccess")
Block = Class(name="Block")
PortAccess = Class(name="PortAccess")
ir_PortPeek = Class(name="ir::PortPeek")
ir_ForwardDeclaration = Class(name="ir::ForwardDeclaration")
ir_LambdaExpression = Class(name="ir::LambdaExpression")
ir_ProcExpression = Class(name="ir::ProcExpression")
ir_IfExpression = Class(name="ir::IfExpression")
LambdaExpression = Class(name="LambdaExpression")
ir_TypeBool = Class(name="ir::TypeBool")
Type = Class(name="Type")
ir_TypeExternal = Class(name="ir::TypeExternal")
ir_TypeInt = Class(name="ir::TypeInt")
ir_TypeList = Class(name="ir::TypeList")
ir_TypeFloat = Class(name="ir::TypeFloat")
ir_TypeUint = Class(name="ir::TypeUint")
ir_TypeString = Class(name="ir::TypeString")
ir_TypeRecord = Class(name="ir::TypeRecord")
ir_TypeUndef = Class(name="ir::TypeUndef")
ir_TypeUser = Class(name="ir::TypeUser")
ir_TypeLambda = Class(name="ir::TypeLambda")
ir_TypeProc = Class(name="ir::TypeProc")
ir_TypeConstructor = Class(name="ir::TypeConstructor")
ir_TypeDeclaration = Class(name="ir::TypeDeclaration")
ir_State = Class(name="ir::State")
ir_AnnotationArgument = Class(name="ir::AnnotationArgument")

# ir_Scope class attributes and methods

# Node class attributes and methods

# ir_Declaration class attributes and methods
ir_Declaration_name: Property = Property(name="name", type=StringType)
ir_Declaration.attributes={ir_Declaration_name}

# ir_Node class attributes and methods
ir_Node_id: Property = Property(name="id", type=StringType)
ir_Node.attributes={ir_Node_id}

# ir_Annotation class attributes and methods
ir_Annotation_name: Property = Property(name="name", type=StringType)
ir_Annotation.attributes={ir_Annotation_name}

# ir_VariableImport class attributes and methods
ir_VariableImport_namespace: Property = Property(name="namespace", type=StringType)
ir_VariableImport.attributes={ir_VariableImport_namespace}

# Declaration class attributes and methods

# ir_VariableExternal class attributes and methods

# ir_Type class attributes and methods

# ir_TypeDeclarationImport class attributes and methods
ir_TypeDeclarationImport_namespace: Property = Property(name="namespace", type=StringType)
ir_TypeDeclarationImport.attributes={ir_TypeDeclarationImport_namespace}

# ir_Namespace class attributes and methods
ir_Namespace_name: Property = Property(name="name", type=StringType)
ir_Namespace.attributes={ir_Namespace_name}

# Scope class attributes and methods

# ir_AbstractActor class attributes and methods

# ir_TypeActor class attributes and methods
ir_TypeActor_namespace: Property = Property(name="namespace", type=StringType)
ir_TypeActor_name: Property = Property(name="name", type=StringType)
ir_TypeActor.attributes={ir_TypeActor_name, ir_TypeActor_namespace}

# ir_Port class attributes and methods
ir_Port_name: Property = Property(name="name", type=StringType)
ir_Port.attributes={ir_Port_name}

# ir_Variable class attributes and methods
ir_Variable_constant: Property = Property(name="constant", type=BooleanType)
ir_Variable_parameter: Property = Property(name="parameter", type=BooleanType)
ir_Variable.attributes={ir_Variable_constant, ir_Variable_parameter}

# ir_ExternalActor class attributes and methods

# AbstractActor class attributes and methods

# ir_Actor class attributes and methods

# ir_Action class attributes and methods
ir_Action_tag: Property = Property(name="tag", type=StringType)
ir_Action.attributes={ir_Action_tag}

# ir_Schedule class attributes and methods
ir_Schedule_PriorityGraph: Property = Property(name="PriorityGraph", type=StringType)
ir_Schedule.attributes={ir_Schedule_PriorityGraph}

# ir_Network class attributes and methods

# ir_Connection class attributes and methods

# ir_ActorInstance class attributes and methods

# ir_Guard class attributes and methods

# ir_PortWrite class attributes and methods

# ir_PortRead class attributes and methods

# ir_Statement class attributes and methods

# Variable class attributes and methods

# ir_PortInstance class attributes and methods
ir_PortInstance_name: Property = Property(name="name", type=StringType)
ir_PortInstance.attributes={ir_PortInstance_name}

# ir_TaggedExpression class attributes and methods
ir_TaggedExpression_tag: Property = Property(name="tag", type=StringType)
ir_TaggedExpression.attributes={ir_TaggedExpression_tag}

# ir_Expression class attributes and methods

# ir_LiteralExpression class attributes and methods

# Expression class attributes and methods

# ir_IntegerLiteral class attributes and methods
ir_IntegerLiteral_value: Property = Property(name="value", type=StringType)
ir_IntegerLiteral.attributes={ir_IntegerLiteral_value}

# LiteralExpression class attributes and methods

# ir_FloatLiteral class attributes and methods
ir_FloatLiteral_value: Property = Property(name="value", type=FloatType)
ir_FloatLiteral.attributes={ir_FloatLiteral_value}

# ir_BooleanLiteral class attributes and methods
ir_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
ir_BooleanLiteral.attributes={ir_BooleanLiteral_value}

# ir_StringLiteral class attributes and methods
ir_StringLiteral_value: Property = Property(name="value", type=StringType)
ir_StringLiteral.attributes={ir_StringLiteral_value}

# ir_VariableExpression class attributes and methods

# ir_Member class attributes and methods
ir_Member_name: Property = Property(name="name", type=StringType)
ir_Member.attributes={ir_Member_name}

# ir_ListExpression class attributes and methods

# ir_Generator class attributes and methods

# ir_BinaryExpression class attributes and methods
ir_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
ir_BinaryExpression.attributes={ir_BinaryExpression_operator}

# ir_UnaryExpression class attributes and methods
ir_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
ir_UnaryExpression.attributes={ir_UnaryExpression_operator}

# ir_ExpressionCall class attributes and methods

# ir_FunctionCall class attributes and methods

# ExpressionCall class attributes and methods

# ir_TypeConstructorCall class attributes and methods
ir_TypeConstructorCall_name: Property = Property(name="name", type=StringType)
ir_TypeConstructorCall.attributes={ir_TypeConstructorCall_name}

# ir_Point2PointConnection class attributes and methods

# Connection class attributes and methods

# ir_FromSource class attributes and methods

# ir_VariableReference class attributes and methods

# ir_Assign class attributes and methods

# Statement class attributes and methods

# ir_ReturnValue class attributes and methods

# ir_ProcCall class attributes and methods

# ir_WhileLoop class attributes and methods

# ir_Block class attributes and methods

# ir_ForEach class attributes and methods

# ir_IfStatement class attributes and methods

# ir_ToSink class attributes and methods

# ir_PortAccess class attributes and methods

# Block class attributes and methods

# PortAccess class attributes and methods

# ir_PortPeek class attributes and methods
ir_PortPeek_position: Property = Property(name="position", type=IntegerType)
ir_PortPeek.attributes={ir_PortPeek_position}

# ir_ForwardDeclaration class attributes and methods

# ir_LambdaExpression class attributes and methods

# ir_ProcExpression class attributes and methods

# ir_IfExpression class attributes and methods

# LambdaExpression class attributes and methods

# ir_TypeBool class attributes and methods

# Type class attributes and methods

# ir_TypeExternal class attributes and methods
ir_TypeExternal_name: Property = Property(name="name", type=StringType)
ir_TypeExternal_scopeName: Property = Property(name="scopeName", type=StringType)
ir_TypeExternal.attributes={ir_TypeExternal_name, ir_TypeExternal_scopeName}

# ir_TypeInt class attributes and methods

# ir_TypeList class attributes and methods

# ir_TypeFloat class attributes and methods

# ir_TypeUint class attributes and methods

# ir_TypeString class attributes and methods

# ir_TypeRecord class attributes and methods

# ir_TypeUndef class attributes and methods

# ir_TypeUser class attributes and methods

# ir_TypeLambda class attributes and methods

# ir_TypeProc class attributes and methods

# ir_TypeConstructor class attributes and methods

# ir_TypeDeclaration class attributes and methods

# ir_State class attributes and methods
ir_State_PriorityGraph: Property = Property(name="PriorityGraph", type=StringType)
ir_State_Action2TargetMap: Property = Property(name="Action2TargetMap", type=StringType)
ir_State_name: Property = Property(name="name", type=StringType)
ir_State.attributes={ir_State_PriorityGraph, ir_State_Action2TargetMap, ir_State_name}

# ir_AnnotationArgument class attributes and methods
ir_AnnotationArgument_id: Property = Property(name="id", type=StringType)
ir_AnnotationArgument_value: Property = Property(name="value", type=StringType)
ir_AnnotationArgument.attributes={ir_AnnotationArgument_id, ir_AnnotationArgument_value}

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="ir_Declaration", type=ir_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Scope", type=ir_Declaration, multiplicity=Multiplicity(0, 9999))
    }
)
outer2: BinaryAssociation = BinaryAssociation(
    name="outer2",
    ends={
        Property(name="ir_Scope3", type=ir_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Scope1", type=ir_Scope, multiplicity=Multiplicity(0, 1))
    }
)
annotations4: BinaryAssociation = BinaryAssociation(
    name="annotations4",
    ends={
        Property(name="ir_Annotation", type=ir_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Node", type=ir_Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="ir_Type", type=ir_VariableExternal, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableExternal", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
actors6: BinaryAssociation = BinaryAssociation(
    name="actors6",
    ends={
        Property(name="ir_AbstractActor", type=ir_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Namespace", type=ir_AbstractActor, multiplicity=Multiplicity(0, 9999))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="ir_TypeActor", type=ir_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_AbstractActor8", type=ir_TypeActor, multiplicity=Multiplicity(0, 1))
    }
)
inputPorts9: BinaryAssociation = BinaryAssociation(
    name="inputPorts9",
    ends={
        Property(name="ir_Port", type=ir_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_AbstractActor10", type=ir_Port, multiplicity=Multiplicity(0, 9999))
    }
)
outputPorts11: BinaryAssociation = BinaryAssociation(
    name="outputPorts11",
    ends={
        Property(name="ir_Port13", type=ir_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_AbstractActor12", type=ir_Port, multiplicity=Multiplicity(0, 9999))
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="ir_Variable", type=ir_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_AbstractActor15", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
actions16: BinaryAssociation = BinaryAssociation(
    name="actions16",
    ends={
        Property(name="ir_Action", type=ir_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Actor", type=ir_Action, multiplicity=Multiplicity(0, 9999))
    }
)
initializers17: BinaryAssociation = BinaryAssociation(
    name="initializers17",
    ends={
        Property(name="ir_Action19", type=ir_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Actor18", type=ir_Action, multiplicity=Multiplicity(0, 9999))
    }
)
schedule20: BinaryAssociation = BinaryAssociation(
    name="schedule20",
    ends={
        Property(name="ir_Schedule", type=ir_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Actor21", type=ir_Schedule, multiplicity=Multiplicity(0, 1))
    }
)
connections22: BinaryAssociation = BinaryAssociation(
    name="connections22",
    ends={
        Property(name="ir_Connection", type=ir_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Network", type=ir_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
actors23: BinaryAssociation = BinaryAssociation(
    name="actors23",
    ends={
        Property(name="ir_ActorInstance", type=ir_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Network24", type=ir_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
guards25: BinaryAssociation = BinaryAssociation(
    name="guards25",
    ends={
        Property(name="ir_Guard", type=ir_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Action26", type=ir_Guard, multiplicity=Multiplicity(0, 9999))
    }
)
outputs27: BinaryAssociation = BinaryAssociation(
    name="outputs27",
    ends={
        Property(name="ir_PortWrite", type=ir_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Action28", type=ir_PortWrite, multiplicity=Multiplicity(0, 9999))
    }
)
inputs29: BinaryAssociation = BinaryAssociation(
    name="inputs29",
    ends={
        Property(name="ir_PortRead", type=ir_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Action30", type=ir_PortRead, multiplicity=Multiplicity(0, 9999))
    }
)
statements31: BinaryAssociation = BinaryAssociation(
    name="statements31",
    ends={
        Property(name="ir_Statement", type=ir_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Action32", type=ir_Statement, multiplicity=Multiplicity(0, 9999))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="ir_Type35", type=ir_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Port34", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
inputs36: BinaryAssociation = BinaryAssociation(
    name="inputs36",
    ends={
        Property(name="ir_PortInstance", type=ir_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ActorInstance37", type=ir_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
outputs38: BinaryAssociation = BinaryAssociation(
    name="outputs38",
    ends={
        Property(name="ir_PortInstance40", type=ir_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ActorInstance39", type=ir_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
actualParameters41: BinaryAssociation = BinaryAssociation(
    name="actualParameters41",
    ends={
        Property(name="ir_TaggedExpression", type=ir_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ActorInstance42", type=ir_TaggedExpression, multiplicity=Multiplicity(0, 9999))
    }
)
connections43: BinaryAssociation = BinaryAssociation(
    name="connections43",
    ends={
        Property(name="ir_Connection45", type=ir_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortInstance44", type=ir_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
actor46: BinaryAssociation = BinaryAssociation(
    name="actor46",
    ends={
        Property(name="ir_ActorInstance48", type=ir_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortInstance47", type=ir_ActorInstance, multiplicity=Multiplicity(0, 1))
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="ir_Type50", type=ir_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Expression", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
context51: BinaryAssociation = BinaryAssociation(
    name="context51",
    ends={
        Property(name="ir_Scope53", type=ir_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Expression52", type=ir_Scope, multiplicity=Multiplicity(0, 1))
    }
)
expression54: BinaryAssociation = BinaryAssociation(
    name="expression54",
    ends={
        Property(name="ir_Expression56", type=ir_TaggedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TaggedExpression55", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="ir_Declaration58", type=ir_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableExpression", type=ir_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
index59: BinaryAssociation = BinaryAssociation(
    name="index59",
    ends={
        Property(name="ir_Expression61", type=ir_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableExpression60", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
member62: BinaryAssociation = BinaryAssociation(
    name="member62",
    ends={
        Property(name="ir_Member", type=ir_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableExpression63", type=ir_Member, multiplicity=Multiplicity(0, 9999))
    }
)
generators64: BinaryAssociation = BinaryAssociation(
    name="generators64",
    ends={
        Property(name="ir_Generator", type=ir_ListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ListExpression", type=ir_Generator, multiplicity=Multiplicity(0, 9999))
    }
)
expressions65: BinaryAssociation = BinaryAssociation(
    name="expressions65",
    ends={
        Property(name="ir_Expression67", type=ir_ListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ListExpression66", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
index71: BinaryAssociation = BinaryAssociation(
    name="index71",
    ends={
        Property(name="ir_Expression73", type=ir_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Member72", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
type74: BinaryAssociation = BinaryAssociation(
    name="type74",
    ends={
        Property(name="ir_Type76", type=ir_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Member75", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
operand177: BinaryAssociation = BinaryAssociation(
    name="operand177",
    ends={
        Property(name="ir_Expression78", type=ir_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BinaryExpression", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
operand279: BinaryAssociation = BinaryAssociation(
    name="operand279",
    ends={
        Property(name="ir_Expression81", type=ir_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_BinaryExpression80", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
operand82: BinaryAssociation = BinaryAssociation(
    name="operand82",
    ends={
        Property(name="ir_Expression83", type=ir_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_UnaryExpression", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
parameters84: BinaryAssociation = BinaryAssociation(
    name="parameters84",
    ends={
        Property(name="ir_Expression85", type=ir_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FunctionCall", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
function86: BinaryAssociation = BinaryAssociation(
    name="function86",
    ends={
        Property(name="ir_Expression88", type=ir_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FunctionCall87", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
parameters89: BinaryAssociation = BinaryAssociation(
    name="parameters89",
    ends={
        Property(name="ir_Expression90", type=ir_TypeConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeConstructorCall", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
typedef91: BinaryAssociation = BinaryAssociation(
    name="typedef91",
    ends={
        Property(name="ir_Declaration93", type=ir_TypeConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeConstructorCall92", type=ir_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes94: BinaryAssociation = BinaryAssociation(
    name="attributes94",
    ends={
        Property(name="ir_TaggedExpression96", type=ir_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Connection95", type=ir_TaggedExpression, multiplicity=Multiplicity(0, 9999))
    }
)
source97: BinaryAssociation = BinaryAssociation(
    name="source97",
    ends={
        Property(name="ir_PortInstance98", type=ir_Point2PointConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Point2PointConnection", type=ir_PortInstance, multiplicity=Multiplicity(0, 1))
    }
)
target99: BinaryAssociation = BinaryAssociation(
    name="target99",
    ends={
        Property(name="ir_PortInstance101", type=ir_Point2PointConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Point2PointConnection100", type=ir_PortInstance, multiplicity=Multiplicity(0, 1))
    }
)
target102: BinaryAssociation = BinaryAssociation(
    name="target102",
    ends={
        Property(name="ir_PortInstance103", type=ir_FromSource, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FromSource", type=ir_PortInstance, multiplicity=Multiplicity(0, 1))
    }
)
source104: BinaryAssociation = BinaryAssociation(
    name="source104",
    ends={
        Property(name="ir_Port106", type=ir_FromSource, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_FromSource105", type=ir_Port, multiplicity=Multiplicity(0, 1))
    }
)
source68: BinaryAssociation = BinaryAssociation(
    name="source68",
    ends={
        Property(name="ir_Expression70", type=ir_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Generator69", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
source107: BinaryAssociation = BinaryAssociation(
    name="source107",
    ends={
        Property(name="ir_PortInstance108", type=ir_ToSink, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ToSink", type=ir_PortInstance, multiplicity=Multiplicity(0, 1))
    }
)
sink109: BinaryAssociation = BinaryAssociation(
    name="sink109",
    ends={
        Property(name="ir_Port111", type=ir_ToSink, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ToSink110", type=ir_Port, multiplicity=Multiplicity(0, 1))
    }
)
declaration112: BinaryAssociation = BinaryAssociation(
    name="declaration112",
    ends={
        Property(name="ir_Variable113", type=ir_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableReference", type=ir_Variable, multiplicity=Multiplicity(0, 1))
    }
)
index114: BinaryAssociation = BinaryAssociation(
    name="index114",
    ends={
        Property(name="ir_Expression116", type=ir_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableReference115", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
member117: BinaryAssociation = BinaryAssociation(
    name="member117",
    ends={
        Property(name="ir_Member119", type=ir_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableReference118", type=ir_Member, multiplicity=Multiplicity(0, 9999))
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="ir_Type122", type=ir_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_VariableReference121", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
target123: BinaryAssociation = BinaryAssociation(
    name="target123",
    ends={
        Property(name="ir_VariableReference124", type=ir_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Assign", type=ir_VariableReference, multiplicity=Multiplicity(0, 1))
    }
)
expression125: BinaryAssociation = BinaryAssociation(
    name="expression125",
    ends={
        Property(name="ir_Expression127", type=ir_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Assign126", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
value128: BinaryAssociation = BinaryAssociation(
    name="value128",
    ends={
        Property(name="ir_Expression129", type=ir_ReturnValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ReturnValue", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
inParameters130: BinaryAssociation = BinaryAssociation(
    name="inParameters130",
    ends={
        Property(name="ir_Expression131", type=ir_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcCall", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
outParameters132: BinaryAssociation = BinaryAssociation(
    name="outParameters132",
    ends={
        Property(name="ir_VariableReference134", type=ir_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcCall133", type=ir_VariableReference, multiplicity=Multiplicity(0, 9999))
    }
)
procedure135: BinaryAssociation = BinaryAssociation(
    name="procedure135",
    ends={
        Property(name="ir_Declaration137", type=ir_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcCall136", type=ir_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
body138: BinaryAssociation = BinaryAssociation(
    name="body138",
    ends={
        Property(name="ir_Block", type=ir_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_WhileLoop", type=ir_Block, multiplicity=Multiplicity(0, 1))
    }
)
condition139: BinaryAssociation = BinaryAssociation(
    name="condition139",
    ends={
        Property(name="ir_Expression141", type=ir_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_WhileLoop140", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
body142: BinaryAssociation = BinaryAssociation(
    name="body142",
    ends={
        Property(name="ir_Block143", type=ir_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ForEach", type=ir_Block, multiplicity=Multiplicity(0, 1))
    }
)
generators144: BinaryAssociation = BinaryAssociation(
    name="generators144",
    ends={
        Property(name="ir_Generator146", type=ir_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ForEach145", type=ir_Generator, multiplicity=Multiplicity(0, 9999))
    }
)
thenBlock147: BinaryAssociation = BinaryAssociation(
    name="thenBlock147",
    ends={
        Property(name="ir_Block148", type=ir_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfStatement", type=ir_Block, multiplicity=Multiplicity(0, 1))
    }
)
condition152: BinaryAssociation = BinaryAssociation(
    name="condition152",
    ends={
        Property(name="ir_Expression154", type=ir_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfStatement153", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
statements155: BinaryAssociation = BinaryAssociation(
    name="statements155",
    ends={
        Property(name="ir_Statement157", type=ir_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Block156", type=ir_Statement, multiplicity=Multiplicity(0, 9999))
    }
)
port158: BinaryAssociation = BinaryAssociation(
    name="port158",
    ends={
        Property(name="ir_Port159", type=ir_PortAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortAccess", type=ir_Port, multiplicity=Multiplicity(0, 1))
    }
)
repeat160: BinaryAssociation = BinaryAssociation(
    name="repeat160",
    ends={
        Property(name="ir_Expression162", type=ir_PortAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortAccess161", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
expressions163: BinaryAssociation = BinaryAssociation(
    name="expressions163",
    ends={
        Property(name="ir_Expression165", type=ir_PortWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortWrite164", type=ir_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
variables166: BinaryAssociation = BinaryAssociation(
    name="variables166",
    ends={
        Property(name="ir_VariableReference168", type=ir_PortRead, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortRead167", type=ir_VariableReference, multiplicity=Multiplicity(0, 9999))
    }
)
variable169: BinaryAssociation = BinaryAssociation(
    name="variable169",
    ends={
        Property(name="ir_VariableReference170", type=ir_PortPeek, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_PortPeek", type=ir_VariableReference, multiplicity=Multiplicity(0, 1))
    }
)
scope171: BinaryAssociation = BinaryAssociation(
    name="scope171",
    ends={
        Property(name="ir_Scope173", type=ir_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Declaration172", type=ir_Scope, multiplicity=Multiplicity(0, 1))
    }
)
attributes174: BinaryAssociation = BinaryAssociation(
    name="attributes174",
    ends={
        Property(name="ir_TaggedExpression176", type=ir_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Declaration175", type=ir_TaggedExpression, multiplicity=Multiplicity(0, 9999))
    }
)
declaration177: BinaryAssociation = BinaryAssociation(
    name="declaration177",
    ends={
        Property(name="ir_Declaration178", type=ir_ForwardDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ForwardDeclaration", type=ir_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="ir_Type181", type=ir_ForwardDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ForwardDeclaration180", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
initValue182: BinaryAssociation = BinaryAssociation(
    name="initValue182",
    ends={
        Property(name="ir_Expression184", type=ir_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Variable183", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="ir_Type187", type=ir_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Variable186", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters188: BinaryAssociation = BinaryAssociation(
    name="parameters188",
    ends={
        Property(name="ir_Variable189", type=ir_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_LambdaExpression", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
elseBlock149: BinaryAssociation = BinaryAssociation(
    name="elseBlock149",
    ends={
        Property(name="ir_Block151", type=ir_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfStatement150", type=ir_Block, multiplicity=Multiplicity(0, 1))
    }
)
parameters193: BinaryAssociation = BinaryAssociation(
    name="parameters193",
    ends={
        Property(name="ir_Variable194", type=ir_ProcExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcExpression", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
outputs195: BinaryAssociation = BinaryAssociation(
    name="outputs195",
    ends={
        Property(name="ir_Variable197", type=ir_ProcExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcExpression196", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
body198: BinaryAssociation = BinaryAssociation(
    name="body198",
    ends={
        Property(name="ir_Block200", type=ir_ProcExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_ProcExpression199", type=ir_Block, multiplicity=Multiplicity(0, 1))
    }
)
thenExpression201: BinaryAssociation = BinaryAssociation(
    name="thenExpression201",
    ends={
        Property(name="ir_Expression202", type=ir_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfExpression", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
elseExpression203: BinaryAssociation = BinaryAssociation(
    name="elseExpression203",
    ends={
        Property(name="ir_Expression205", type=ir_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfExpression204", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
condition206: BinaryAssociation = BinaryAssociation(
    name="condition206",
    ends={
        Property(name="ir_Expression208", type=ir_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_IfExpression207", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
peeks209: BinaryAssociation = BinaryAssociation(
    name="peeks209",
    ends={
        Property(name="ir_PortPeek211", type=ir_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Guard210", type=ir_PortPeek, multiplicity=Multiplicity(0, 9999))
    }
)
attributes212: BinaryAssociation = BinaryAssociation(
    name="attributes212",
    ends={
        Property(name="ir_TaggedExpression213", type=ir_TypeExternal, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeExternal", type=ir_TaggedExpression, multiplicity=Multiplicity(0, 9999))
    }
)
size214: BinaryAssociation = BinaryAssociation(
    name="size214",
    ends={
        Property(name="ir_Expression215", type=ir_TypeInt, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeInt", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
size216: BinaryAssociation = BinaryAssociation(
    name="size216",
    ends={
        Property(name="ir_Expression217", type=ir_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeList", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
type218: BinaryAssociation = BinaryAssociation(
    name="type218",
    ends={
        Property(name="ir_Type220", type=ir_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeList219", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
size221: BinaryAssociation = BinaryAssociation(
    name="size221",
    ends={
        Property(name="ir_Expression222", type=ir_TypeUint, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeUint", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
body190: BinaryAssociation = BinaryAssociation(
    name="body190",
    ends={
        Property(name="ir_Expression192", type=ir_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_LambdaExpression191", type=ir_Expression, multiplicity=Multiplicity(0, 1))
    }
)
members223: BinaryAssociation = BinaryAssociation(
    name="members223",
    ends={
        Property(name="ir_Variable224", type=ir_TypeRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeRecord", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
declaration225: BinaryAssociation = BinaryAssociation(
    name="declaration225",
    ends={
        Property(name="ir_Declaration226", type=ir_TypeUser, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeUser", type=ir_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
inputTypes227: BinaryAssociation = BinaryAssociation(
    name="inputTypes227",
    ends={
        Property(name="ir_Type228", type=ir_TypeLambda, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeLambda", type=ir_Type, multiplicity=Multiplicity(0, 9999))
    }
)
outputType229: BinaryAssociation = BinaryAssociation(
    name="outputType229",
    ends={
        Property(name="ir_Type231", type=ir_TypeLambda, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeLambda230", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
inputTypes232: BinaryAssociation = BinaryAssociation(
    name="inputTypes232",
    ends={
        Property(name="ir_Type233", type=ir_TypeProc, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeProc", type=ir_Type, multiplicity=Multiplicity(0, 9999))
    }
)
outputTypes234: BinaryAssociation = BinaryAssociation(
    name="outputTypes234",
    ends={
        Property(name="ir_Type236", type=ir_TypeProc, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeProc235", type=ir_Type, multiplicity=Multiplicity(0, 9999))
    }
)
typedef237: BinaryAssociation = BinaryAssociation(
    name="typedef237",
    ends={
        Property(name="ir_TypeDeclaration", type=ir_TypeConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeConstructor", type=ir_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
parameters238: BinaryAssociation = BinaryAssociation(
    name="parameters238",
    ends={
        Property(name="ir_Variable240", type=ir_TypeConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeConstructor239", type=ir_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
type241: BinaryAssociation = BinaryAssociation(
    name="type241",
    ends={
        Property(name="ir_Type243", type=ir_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeDeclaration242", type=ir_Type, multiplicity=Multiplicity(0, 1))
    }
)
constructor244: BinaryAssociation = BinaryAssociation(
    name="constructor244",
    ends={
        Property(name="ir_TypeConstructor246", type=ir_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_TypeDeclaration245", type=ir_TypeConstructor, multiplicity=Multiplicity(0, 1))
    }
)
states247: BinaryAssociation = BinaryAssociation(
    name="states247",
    ends={
        Property(name="ir_State", type=ir_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Schedule248", type=ir_State, multiplicity=Multiplicity(0, 9999))
    }
)
freeRunners249: BinaryAssociation = BinaryAssociation(
    name="freeRunners249",
    ends={
        Property(name="ir_Action251", type=ir_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Schedule250", type=ir_Action, multiplicity=Multiplicity(0, 9999))
    }
)
initialState252: BinaryAssociation = BinaryAssociation(
    name="initialState252",
    ends={
        Property(name="ir_State254", type=ir_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Schedule253", type=ir_State, multiplicity=Multiplicity(0, 1))
    }
)
arguments255: BinaryAssociation = BinaryAssociation(
    name="arguments255",
    ends={
        Property(name="ir_AnnotationArgument", type=ir_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ir_Annotation256", type=ir_AnnotationArgument, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ir_Scope_Node = Generalization(general=Node, specific=ir_Scope)
gen_ir_VariableImport_Declaration = Generalization(general=Declaration, specific=ir_VariableImport)
gen_ir_VariableExternal_Declaration = Generalization(general=Declaration, specific=ir_VariableExternal)
gen_ir_TypeDeclarationImport_Declaration = Generalization(general=Declaration, specific=ir_TypeDeclarationImport)
gen_ir_Namespace_Scope = Generalization(general=Scope, specific=ir_Namespace)
gen_ir_AbstractActor_Scope = Generalization(general=Scope, specific=ir_AbstractActor)
gen_ir_ExternalActor_AbstractActor = Generalization(general=AbstractActor, specific=ir_ExternalActor)
gen_ir_Actor_AbstractActor = Generalization(general=AbstractActor, specific=ir_Actor)
gen_ir_Network_AbstractActor = Generalization(general=AbstractActor, specific=ir_Network)
gen_ir_Action_Scope = Generalization(general=Scope, specific=ir_Action)
gen_ir_Port_Node = Generalization(general=Node, specific=ir_Port)
gen_ir_ActorInstance_Variable = Generalization(general=Variable, specific=ir_ActorInstance)
gen_ir_PortInstance_Node = Generalization(general=Node, specific=ir_PortInstance)
gen_ir_Expression_Node = Generalization(general=Node, specific=ir_Expression)
gen_ir_LiteralExpression_Expression = Generalization(general=Expression, specific=ir_LiteralExpression)
gen_ir_IntegerLiteral_LiteralExpression = Generalization(general=LiteralExpression, specific=ir_IntegerLiteral)
gen_ir_FloatLiteral_LiteralExpression = Generalization(general=LiteralExpression, specific=ir_FloatLiteral)
gen_ir_BooleanLiteral_LiteralExpression = Generalization(general=LiteralExpression, specific=ir_BooleanLiteral)
gen_ir_StringLiteral_LiteralExpression = Generalization(general=LiteralExpression, specific=ir_StringLiteral)
gen_ir_VariableExpression_Expression = Generalization(general=Expression, specific=ir_VariableExpression)
gen_ir_ListExpression_Expression = Generalization(general=Expression, specific=ir_ListExpression)
gen_ir_Generator_Scope = Generalization(general=Scope, specific=ir_Generator)
gen_ir_Member_Node = Generalization(general=Node, specific=ir_Member)
gen_ir_BinaryExpression_Expression = Generalization(general=Expression, specific=ir_BinaryExpression)
gen_ir_UnaryExpression_Expression = Generalization(general=Expression, specific=ir_UnaryExpression)
gen_ir_ExpressionCall_Expression = Generalization(general=Expression, specific=ir_ExpressionCall)
gen_ir_FunctionCall_ExpressionCall = Generalization(general=ExpressionCall, specific=ir_FunctionCall)
gen_ir_TypeConstructorCall_ExpressionCall = Generalization(general=ExpressionCall, specific=ir_TypeConstructorCall)
gen_ir_Connection_Node = Generalization(general=Node, specific=ir_Connection)
gen_ir_Point2PointConnection_Connection = Generalization(general=Connection, specific=ir_Point2PointConnection)
gen_ir_FromSource_Connection = Generalization(general=Connection, specific=ir_FromSource)
gen_ir_Statement_Node = Generalization(general=Node, specific=ir_Statement)
gen_ir_VariableReference_Node = Generalization(general=Node, specific=ir_VariableReference)
gen_ir_Assign_Statement = Generalization(general=Statement, specific=ir_Assign)
gen_ir_ReturnValue_Statement = Generalization(general=Statement, specific=ir_ReturnValue)
gen_ir_ProcCall_Statement = Generalization(general=Statement, specific=ir_ProcCall)
gen_ir_WhileLoop_Statement = Generalization(general=Statement, specific=ir_WhileLoop)
gen_ir_ForEach_Statement = Generalization(general=Statement, specific=ir_ForEach)
gen_ir_IfStatement_Statement = Generalization(general=Statement, specific=ir_IfStatement)
gen_ir_ToSink_Connection = Generalization(general=Connection, specific=ir_ToSink)
gen_ir_Block_Scope = Generalization(general=Scope, specific=ir_Block)
gen_ir_Block_Statement = Generalization(general=Statement, specific=ir_Block)
gen_ir_PortAccess_Node = Generalization(general=Node, specific=ir_PortAccess)
gen_ir_PortWrite_Block = Generalization(general=Block, specific=ir_PortWrite)
gen_ir_PortWrite_PortAccess = Generalization(general=PortAccess, specific=ir_PortWrite)
gen_ir_PortRead_PortAccess = Generalization(general=PortAccess, specific=ir_PortRead)
gen_ir_PortPeek_PortAccess = Generalization(general=PortAccess, specific=ir_PortPeek)
gen_ir_Declaration_Node = Generalization(general=Node, specific=ir_Declaration)
gen_ir_ForwardDeclaration_Declaration = Generalization(general=Declaration, specific=ir_ForwardDeclaration)
gen_ir_Variable_Declaration = Generalization(general=Declaration, specific=ir_Variable)
gen_ir_LambdaExpression_Scope = Generalization(general=Scope, specific=ir_LambdaExpression)
gen_ir_LambdaExpression_Expression = Generalization(general=Expression, specific=ir_LambdaExpression)
gen_ir_ProcExpression_Scope = Generalization(general=Scope, specific=ir_ProcExpression)
gen_ir_ProcExpression_Expression = Generalization(general=Expression, specific=ir_ProcExpression)
gen_ir_IfExpression_Expression = Generalization(general=Expression, specific=ir_IfExpression)
gen_ir_Guard_LambdaExpression = Generalization(general=LambdaExpression, specific=ir_Guard)
gen_ir_TypeBool_Type = Generalization(general=Type, specific=ir_TypeBool)
gen_ir_TypeExternal_Type = Generalization(general=Type, specific=ir_TypeExternal)
gen_ir_TypeInt_Type = Generalization(general=Type, specific=ir_TypeInt)
gen_ir_TypeList_Type = Generalization(general=Type, specific=ir_TypeList)
gen_ir_TypeFloat_Type = Generalization(general=Type, specific=ir_TypeFloat)
gen_ir_TypeUint_Type = Generalization(general=Type, specific=ir_TypeUint)
gen_ir_TypeRecord_Type = Generalization(general=Type, specific=ir_TypeRecord)
gen_ir_TypeRecord_Node = Generalization(general=Node, specific=ir_TypeRecord)
gen_ir_TypeUndef_Type = Generalization(general=Type, specific=ir_TypeUndef)
gen_ir_TypeActor_Type = Generalization(general=Type, specific=ir_TypeActor)
gen_ir_TypeUser_Type = Generalization(general=Type, specific=ir_TypeUser)
gen_ir_TypeLambda_Type = Generalization(general=Type, specific=ir_TypeLambda)
gen_ir_TypeProc_Type = Generalization(general=Type, specific=ir_TypeProc)
gen_ir_TypeConstructor_Declaration = Generalization(general=Declaration, specific=ir_TypeConstructor)
gen_ir_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=ir_TypeDeclaration)
gen_ir_TypeString_Type = Generalization(general=Type, specific=ir_TypeString)

# Domain Model
domain_model = DomainModel(
    name="ir",
    types={ir_Scope, Node, ir_Declaration, ir_Node, ir_Annotation, ir_VariableImport, Declaration, ir_VariableExternal, ir_Type, ir_TypeDeclarationImport, ir_Namespace, Scope, ir_AbstractActor, ir_TypeActor, ir_Port, ir_Variable, ir_ExternalActor, AbstractActor, ir_Actor, ir_Action, ir_Schedule, ir_Network, ir_Connection, ir_ActorInstance, ir_Guard, ir_PortWrite, ir_PortRead, ir_Statement, Variable, ir_PortInstance, ir_TaggedExpression, ir_Expression, ir_LiteralExpression, Expression, ir_IntegerLiteral, LiteralExpression, ir_FloatLiteral, ir_BooleanLiteral, ir_StringLiteral, ir_VariableExpression, ir_Member, ir_ListExpression, ir_Generator, ir_BinaryExpression, ir_UnaryExpression, ir_ExpressionCall, ir_FunctionCall, ExpressionCall, ir_TypeConstructorCall, ir_Point2PointConnection, Connection, ir_FromSource, ir_VariableReference, ir_Assign, Statement, ir_ReturnValue, ir_ProcCall, ir_WhileLoop, ir_Block, ir_ForEach, ir_IfStatement, ir_ToSink, ir_PortAccess, Block, PortAccess, ir_PortPeek, ir_ForwardDeclaration, ir_LambdaExpression, ir_ProcExpression, ir_IfExpression, LambdaExpression, ir_TypeBool, Type, ir_TypeExternal, ir_TypeInt, ir_TypeList, ir_TypeFloat, ir_TypeUint, ir_TypeString, ir_TypeRecord, ir_TypeUndef, ir_TypeUser, ir_TypeLambda, ir_TypeProc, ir_TypeConstructor, ir_TypeDeclaration, ir_State, ir_AnnotationArgument},
    associations={declarations0, outer2, annotations4, type5, actors6, type7, inputPorts9, outputPorts11, parameters14, actions16, initializers17, schedule20, connections22, actors23, guards25, outputs27, inputs29, statements31, type33, inputs36, outputs38, actualParameters41, connections43, actor46, type49, context51, expression54, variable57, index59, member62, generators64, expressions65, index71, type74, operand177, operand279, operand82, parameters84, function86, parameters89, typedef91, attributes94, source97, target99, target102, source104, source68, source107, sink109, declaration112, index114, member117, type120, target123, expression125, value128, inParameters130, outParameters132, procedure135, body138, condition139, body142, generators144, thenBlock147, condition152, statements155, port158, repeat160, expressions163, variables166, variable169, scope171, attributes174, declaration177, type179, initValue182, type185, parameters188, elseBlock149, parameters193, outputs195, body198, thenExpression201, elseExpression203, condition206, peeks209, attributes212, size214, size216, type218, size221, body190, members223, declaration225, inputTypes227, outputType229, inputTypes232, outputTypes234, typedef237, parameters238, type241, constructor244, states247, freeRunners249, initialState252, arguments255},
    generalizations={gen_ir_Scope_Node, gen_ir_VariableImport_Declaration, gen_ir_VariableExternal_Declaration, gen_ir_TypeDeclarationImport_Declaration, gen_ir_Namespace_Scope, gen_ir_AbstractActor_Scope, gen_ir_ExternalActor_AbstractActor, gen_ir_Actor_AbstractActor, gen_ir_Network_AbstractActor, gen_ir_Action_Scope, gen_ir_Port_Node, gen_ir_ActorInstance_Variable, gen_ir_PortInstance_Node, gen_ir_Expression_Node, gen_ir_LiteralExpression_Expression, gen_ir_IntegerLiteral_LiteralExpression, gen_ir_FloatLiteral_LiteralExpression, gen_ir_BooleanLiteral_LiteralExpression, gen_ir_StringLiteral_LiteralExpression, gen_ir_VariableExpression_Expression, gen_ir_ListExpression_Expression, gen_ir_Generator_Scope, gen_ir_Member_Node, gen_ir_BinaryExpression_Expression, gen_ir_UnaryExpression_Expression, gen_ir_ExpressionCall_Expression, gen_ir_FunctionCall_ExpressionCall, gen_ir_TypeConstructorCall_ExpressionCall, gen_ir_Connection_Node, gen_ir_Point2PointConnection_Connection, gen_ir_FromSource_Connection, gen_ir_Statement_Node, gen_ir_VariableReference_Node, gen_ir_Assign_Statement, gen_ir_ReturnValue_Statement, gen_ir_ProcCall_Statement, gen_ir_WhileLoop_Statement, gen_ir_ForEach_Statement, gen_ir_IfStatement_Statement, gen_ir_ToSink_Connection, gen_ir_Block_Scope, gen_ir_Block_Statement, gen_ir_PortAccess_Node, gen_ir_PortWrite_Block, gen_ir_PortWrite_PortAccess, gen_ir_PortRead_PortAccess, gen_ir_PortPeek_PortAccess, gen_ir_Declaration_Node, gen_ir_ForwardDeclaration_Declaration, gen_ir_Variable_Declaration, gen_ir_LambdaExpression_Scope, gen_ir_LambdaExpression_Expression, gen_ir_ProcExpression_Scope, gen_ir_ProcExpression_Expression, gen_ir_IfExpression_Expression, gen_ir_Guard_LambdaExpression, gen_ir_TypeBool_Type, gen_ir_TypeExternal_Type, gen_ir_TypeInt_Type, gen_ir_TypeList_Type, gen_ir_TypeFloat_Type, gen_ir_TypeUint_Type, gen_ir_TypeRecord_Type, gen_ir_TypeRecord_Node, gen_ir_TypeUndef_Type, gen_ir_TypeActor_Type, gen_ir_TypeUser_Type, gen_ir_TypeLambda_Type, gen_ir_TypeProc_Type, gen_ir_TypeConstructor_Declaration, gen_ir_TypeDeclaration_Declaration, gen_ir_TypeString_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)