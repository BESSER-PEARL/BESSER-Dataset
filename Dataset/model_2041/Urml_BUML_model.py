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
urml_Model = Class(name="urml::Model")
urml_Capsule = Class(name="urml::Capsule")
urml_Attribute = Class(name="urml::Attribute")
urml_Expression = Class(name="urml::Expression")
urml_Signal = Class(name="urml::Signal")
urml_Port = Class(name="urml::Port")
urml_Protocol = Class(name="urml::Protocol")
urml_LocalVar = Class(name="urml::LocalVar")
Assignable = Class(name="Assignable")
urml_CapsuleInst = Class(name="urml::CapsuleInst")
urml_Connector = Class(name="urml::Connector")
urml_Operation = Class(name="urml::Operation")
urml_StateMachine = Class(name="urml::StateMachine")
urml_OperationCode = Class(name="urml::OperationCode")
urml_TimerPort = Class(name="urml::TimerPort")
urml_LogPort = Class(name="urml::LogPort")
urml_ActionCode = Class(name="urml::ActionCode")
urml_Trigger_in = Class(name="urml::Trigger::in")
urml_State_ = Class(name="urml::State::")
urml_Transition = Class(name="urml::Transition")
urml_IncomingVariable = Class(name="urml::IncomingVariable")
Identifiable = Class(name="Identifiable")
urml_Trigger_out = Class(name="urml::Trigger::out")
urml_StatementOperation = Class(name="urml::StatementOperation")
urml_WhileLoopOperation = Class(name="urml::WhileLoopOperation")
StatementOperation = Class(name="StatementOperation")
urml_IfStatementOperation = Class(name="urml::IfStatementOperation")
urml_ReturnStatement = Class(name="urml::ReturnStatement")
urml_Statement = Class(name="urml::Statement")
urml_Variable = Class(name="urml::Variable")
Statement = Class(name="Statement")
urml_InformTimer = Class(name="urml::InformTimer")
urml_NoOp = Class(name="urml::NoOp")
urml_Invoke = Class(name="urml::Invoke")
urml_Assignment = Class(name="urml::Assignment")
urml_Assignable = Class(name="urml::Assignable")
urml_SendTrigger = Class(name="urml::SendTrigger")
urml_WhileLoop = Class(name="urml::WhileLoop")
urml_IfStatement = Class(name="urml::IfStatement")
urml_LogStatement = Class(name="urml::LogStatement")
urml_StringExpression = Class(name="urml::StringExpression")
urml_NotBooleanExpression = Class(name="urml::NotBooleanExpression")
Expression = Class(name="Expression")
urml_Literal = Class(name="urml::Literal")
urml_IntLiteral = Class(name="urml::IntLiteral")
Literal = Class(name="Literal")
urml_Identifier = Class(name="urml::Identifier")
urml_Identifiable = Class(name="urml::Identifiable")
urml_FunctionCall = Class(name="urml::FunctionCall")
urml_BoolLiteral = Class(name="urml::BoolLiteral")
urml_ConditionalOrExpression = Class(name="urml::ConditionalOrExpression")
urml_ConditionalAndExpression = Class(name="urml::ConditionalAndExpression")
urml_LessThanOrEqual = Class(name="urml::LessThanOrEqual")
urml_ConcatenateExpression = Class(name="urml::ConcatenateExpression")
StringExpression = Class(name="StringExpression")
urml_GreaterThanOrEqual = Class(name="urml::GreaterThanOrEqual")
urml_GreaterThan = Class(name="urml::GreaterThan")
urml_Equal = Class(name="urml::Equal")
urml_LessThan = Class(name="urml::LessThan")
urml_NotEqual = Class(name="urml::NotEqual")
urml_Plus = Class(name="urml::Plus")
urml_Minus = Class(name="urml::Minus")
urml_Multiply = Class(name="urml::Multiply")
urml_Divide = Class(name="urml::Divide")
urml_Modulo = Class(name="urml::Modulo")
urml_UnaryExpression = Class(name="urml::UnaryExpression")

# urml_Model class attributes and methods
urml_Model_name: Property = Property(name="name", type=StringType)
urml_Model.attributes={urml_Model_name}

# urml_Capsule class attributes and methods
urml_Capsule_root: Property = Property(name="root", type=BooleanType)
urml_Capsule_name: Property = Property(name="name", type=StringType)
urml_Capsule.attributes={urml_Capsule_name, urml_Capsule_root}

# urml_Attribute class attributes and methods

# urml_Expression class attributes and methods

# urml_Signal class attributes and methods
urml_Signal_name: Property = Property(name="name", type=StringType)
urml_Signal.attributes={urml_Signal_name}

# urml_Port class attributes and methods
urml_Port_conjugated: Property = Property(name="conjugated", type=BooleanType)
urml_Port_name: Property = Property(name="name", type=StringType)
urml_Port.attributes={urml_Port_conjugated, urml_Port_name}

# urml_Protocol class attributes and methods
urml_Protocol_name: Property = Property(name="name", type=StringType)
urml_Protocol.attributes={urml_Protocol_name}

# urml_LocalVar class attributes and methods

# Assignable class attributes and methods

# urml_CapsuleInst class attributes and methods
urml_CapsuleInst_name: Property = Property(name="name", type=StringType)
urml_CapsuleInst.attributes={urml_CapsuleInst_name}

# urml_Connector class attributes and methods

# urml_Operation class attributes and methods
urml_Operation_isBool: Property = Property(name="isBool", type=BooleanType)
urml_Operation_isInt: Property = Property(name="isInt", type=BooleanType)
urml_Operation_isVoid: Property = Property(name="isVoid", type=BooleanType)
urml_Operation_name: Property = Property(name="name", type=StringType)
urml_Operation.attributes={urml_Operation_isBool, urml_Operation_isVoid, urml_Operation_name, urml_Operation_isInt}

# urml_StateMachine class attributes and methods

# urml_OperationCode class attributes and methods

# urml_TimerPort class attributes and methods
urml_TimerPort_name: Property = Property(name="name", type=StringType)
urml_TimerPort.attributes={urml_TimerPort_name}

# urml_LogPort class attributes and methods
urml_LogPort_name: Property = Property(name="name", type=StringType)
urml_LogPort.attributes={urml_LogPort_name}

# urml_ActionCode class attributes and methods

# urml_Trigger_in class attributes and methods

# urml_State_ class attributes and methods
urml_State__final: Property = Property(name="final", type=BooleanType)
urml_State__name: Property = Property(name="name", type=StringType)
urml_State_.attributes={urml_State__final, urml_State__name}

# urml_Transition class attributes and methods
urml_Transition_name: Property = Property(name="name", type=StringType)
urml_Transition_init: Property = Property(name="init", type=BooleanType)
urml_Transition_universal: Property = Property(name="universal", type=BooleanType)
urml_Transition.attributes={urml_Transition_universal, urml_Transition_name, urml_Transition_init}

# urml_IncomingVariable class attributes and methods

# Identifiable class attributes and methods

# urml_Trigger_out class attributes and methods

# urml_StatementOperation class attributes and methods

# urml_WhileLoopOperation class attributes and methods

# StatementOperation class attributes and methods

# urml_IfStatementOperation class attributes and methods

# urml_ReturnStatement class attributes and methods

# urml_Statement class attributes and methods

# urml_Variable class attributes and methods
urml_Variable_assign: Property = Property(name="assign", type=BooleanType)
urml_Variable.attributes={urml_Variable_assign}

# Statement class attributes and methods

# urml_InformTimer class attributes and methods

# urml_NoOp class attributes and methods

# urml_Invoke class attributes and methods

# urml_Assignment class attributes and methods

# urml_Assignable class attributes and methods

# urml_SendTrigger class attributes and methods

# urml_WhileLoop class attributes and methods

# urml_IfStatement class attributes and methods

# urml_LogStatement class attributes and methods

# urml_StringExpression class attributes and methods
urml_StringExpression_str: Property = Property(name="str", type=StringType)
urml_StringExpression.attributes={urml_StringExpression_str}

# urml_NotBooleanExpression class attributes and methods

# Expression class attributes and methods

# urml_Literal class attributes and methods

# urml_IntLiteral class attributes and methods
urml_IntLiteral_int: Property = Property(name="int", type=IntegerType)
urml_IntLiteral.attributes={urml_IntLiteral_int}

# Literal class attributes and methods

# urml_Identifier class attributes and methods

# urml_Identifiable class attributes and methods
urml_Identifiable_isBool: Property = Property(name="isBool", type=BooleanType)
urml_Identifiable_isInt: Property = Property(name="isInt", type=BooleanType)
urml_Identifiable_name: Property = Property(name="name", type=StringType)
urml_Identifiable.attributes={urml_Identifiable_name, urml_Identifiable_isInt, urml_Identifiable_isBool}

# urml_FunctionCall class attributes and methods

# urml_BoolLiteral class attributes and methods
urml_BoolLiteral_true: Property = Property(name="true", type=BooleanType)
urml_BoolLiteral.attributes={urml_BoolLiteral_true}

# urml_ConditionalOrExpression class attributes and methods

# urml_ConditionalAndExpression class attributes and methods

# urml_LessThanOrEqual class attributes and methods

# urml_ConcatenateExpression class attributes and methods

# StringExpression class attributes and methods

# urml_GreaterThanOrEqual class attributes and methods

# urml_GreaterThan class attributes and methods

# urml_Equal class attributes and methods

# urml_LessThan class attributes and methods

# urml_NotEqual class attributes and methods

# urml_Plus class attributes and methods

# urml_Minus class attributes and methods

# urml_Multiply class attributes and methods

# urml_Divide class attributes and methods

# urml_Modulo class attributes and methods

# urml_UnaryExpression class attributes and methods

# Relationships
capsules0: BinaryAssociation = BinaryAssociation(
    name="capsules0",
    ends={
        Property(name="urml_Capsule", type=urml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Model", type=urml_Capsule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue3: BinaryAssociation = BinaryAssociation(
    name="defaultValue3",
    ends={
        Property(name="urml_Expression", type=urml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Attribute", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingMessages4: BinaryAssociation = BinaryAssociation(
    name="incomingMessages4",
    ends={
        Property(name="urml_Signal", type=urml_Protocol, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Protocol5", type=urml_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingMessages6: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages6",
    ends={
        Property(name="urml_Signal8", type=urml_Protocol, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Protocol7", type=urml_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LocalVars9: BinaryAssociation = BinaryAssociation(
    name="LocalVars9",
    ends={
        Property(name="urml_LocalVar", type=urml_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Signal10", type=urml_LocalVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfacePorts11: BinaryAssociation = BinaryAssociation(
    name="interfacePorts11",
    ends={
        Property(name="urml_Port", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule12", type=urml_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalPorts13: BinaryAssociation = BinaryAssociation(
    name="internalPorts13",
    ends={
        Property(name="urml_Port15", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule14", type=urml_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols1: BinaryAssociation = BinaryAssociation(
    name="protocols1",
    ends={
        Property(name="urml_Protocol", type=urml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Model2", type=urml_Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logPorts18: BinaryAssociation = BinaryAssociation(
    name="logPorts18",
    ends={
        Property(name="urml_LogPort", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule19", type=urml_LogPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes20: BinaryAssociation = BinaryAssociation(
    name="attributes20",
    ends={
        Property(name="urml_Attribute22", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule21", type=urml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capsuleInsts23: BinaryAssociation = BinaryAssociation(
    name="capsuleInsts23",
    ends={
        Property(name="urml_CapsuleInst", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule24", type=urml_CapsuleInst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors25: BinaryAssociation = BinaryAssociation(
    name="connectors25",
    ends={
        Property(name="urml_Connector", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule26", type=urml_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations27: BinaryAssociation = BinaryAssociation(
    name="operations27",
    ends={
        Property(name="urml_Operation", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule28", type=urml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachines29: BinaryAssociation = BinaryAssociation(
    name="statemachines29",
    ends={
        Property(name="urml_StateMachine", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule30", type=urml_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LocalVars31: BinaryAssociation = BinaryAssociation(
    name="LocalVars31",
    ends={
        Property(name="urml_LocalVar33", type=urml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Operation32", type=urml_LocalVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerPorts16: BinaryAssociation = BinaryAssociation(
    name="timerPorts16",
    ends={
        Property(name="urml_TimerPort", type=urml_Capsule, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Capsule17", type=urml_TimerPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol36: BinaryAssociation = BinaryAssociation(
    name="protocol36",
    ends={
        Property(name="urml_Protocol38", type=urml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Port37", type=urml_Protocol, multiplicity=Multiplicity(0, 1))
    }
)
capsuleInst139: BinaryAssociation = BinaryAssociation(
    name="capsuleInst139",
    ends={
        Property(name="urml_CapsuleInst41", type=urml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Connector40", type=urml_CapsuleInst, multiplicity=Multiplicity(0, 1))
    }
)
port142: BinaryAssociation = BinaryAssociation(
    name="port142",
    ends={
        Property(name="urml_Port44", type=urml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Connector43", type=urml_Port, multiplicity=Multiplicity(0, 1))
    }
)
capsuleInst245: BinaryAssociation = BinaryAssociation(
    name="capsuleInst245",
    ends={
        Property(name="urml_CapsuleInst47", type=urml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Connector46", type=urml_CapsuleInst, multiplicity=Multiplicity(0, 1))
    }
)
port248: BinaryAssociation = BinaryAssociation(
    name="port248",
    ends={
        Property(name="urml_Port50", type=urml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Connector49", type=urml_Port, multiplicity=Multiplicity(0, 1))
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="urml_Capsule53", type=urml_CapsuleInst, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_CapsuleInst52", type=urml_Capsule, multiplicity=Multiplicity(0, 1))
    }
)
operationCode34: BinaryAssociation = BinaryAssociation(
    name="operationCode34",
    ends={
        Property(name="urml_OperationCode", type=urml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Operation35", type=urml_OperationCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryCode58: BinaryAssociation = BinaryAssociation(
    name="entryCode58",
    ends={
        Property(name="urml_ActionCode", type=urml_State_, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_State_59", type=urml_ActionCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitCode60: BinaryAssociation = BinaryAssociation(
    name="exitCode60",
    ends={
        Property(name="urml_ActionCode62", type=urml_State_, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_State_61", type=urml_ActionCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substatemachine63: BinaryAssociation = BinaryAssociation(
    name="substatemachine63",
    ends={
        Property(name="urml_StateMachine65", type=urml_State_, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_State_64", type=urml_StateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from66: BinaryAssociation = BinaryAssociation(
    name="from66",
    ends={
        Property(name="urml_State_68", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition67", type=urml_State_, multiplicity=Multiplicity(0, 1))
    }
)
to69: BinaryAssociation = BinaryAssociation(
    name="to69",
    ends={
        Property(name="urml_State_71", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition70", type=urml_State_, multiplicity=Multiplicity(0, 1))
    }
)
guard72: BinaryAssociation = BinaryAssociation(
    name="guard72",
    ends={
        Property(name="urml_Expression74", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition73", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers75: BinaryAssociation = BinaryAssociation(
    name="triggers75",
    ends={
        Property(name="urml_Trigger_in", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition76", type=urml_Trigger_in, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states54: BinaryAssociation = BinaryAssociation(
    name="states54",
    ends={
        Property(name="urml_State_", type=urml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_StateMachine55", type=urml_State_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions56: BinaryAssociation = BinaryAssociation(
    name="transitions56",
    ends={
        Property(name="urml_Transition", type=urml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_StateMachine57", type=urml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from83: BinaryAssociation = BinaryAssociation(
    name="from83",
    ends={
        Property(name="urml_Port85", type=urml_Trigger_in, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_in84", type=urml_Port, multiplicity=Multiplicity(0, 1))
    }
)
signal86: BinaryAssociation = BinaryAssociation(
    name="signal86",
    ends={
        Property(name="urml_Signal88", type=urml_Trigger_in, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_in87", type=urml_Signal, multiplicity=Multiplicity(0, 1))
    }
)
parameters89: BinaryAssociation = BinaryAssociation(
    name="parameters89",
    ends={
        Property(name="urml_IncomingVariable", type=urml_Trigger_in, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_in90", type=urml_IncomingVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to91: BinaryAssociation = BinaryAssociation(
    name="to91",
    ends={
        Property(name="urml_Port92", type=urml_Trigger_out, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_out", type=urml_Port, multiplicity=Multiplicity(0, 1))
    }
)
signal93: BinaryAssociation = BinaryAssociation(
    name="signal93",
    ends={
        Property(name="urml_Signal95", type=urml_Trigger_out, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_out94", type=urml_Signal, multiplicity=Multiplicity(0, 1))
    }
)
parameters96: BinaryAssociation = BinaryAssociation(
    name="parameters96",
    ends={
        Property(name="urml_Expression98", type=urml_Trigger_out, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Trigger_out97", type=urml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements99: BinaryAssociation = BinaryAssociation(
    name="statements99",
    ends={
        Property(name="urml_StatementOperation", type=urml_OperationCode, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_OperationCode100", type=urml_StatementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerPort77: BinaryAssociation = BinaryAssociation(
    name="timerPort77",
    ends={
        Property(name="urml_TimerPort79", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition78", type=urml_TimerPort, multiplicity=Multiplicity(0, 1))
    }
)
action80: BinaryAssociation = BinaryAssociation(
    name="action80",
    ends={
        Property(name="urml_ActionCode82", type=urml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Transition81", type=urml_ActionCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition106: BinaryAssociation = BinaryAssociation(
    name="condition106",
    ends={
        Property(name="urml_Expression107", type=urml_IfStatementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatementOperation", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatements108: BinaryAssociation = BinaryAssociation(
    name="thenStatements108",
    ends={
        Property(name="urml_StatementOperation110", type=urml_IfStatementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatementOperation109", type=urml_StatementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements111: BinaryAssociation = BinaryAssociation(
    name="elseStatements111",
    ends={
        Property(name="urml_StatementOperation113", type=urml_IfStatementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatementOperation112", type=urml_StatementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue114: BinaryAssociation = BinaryAssociation(
    name="returnValue114",
    ends={
        Property(name="urml_Expression115", type=urml_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ReturnStatement", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements116: BinaryAssociation = BinaryAssociation(
    name="statements116",
    ends={
        Property(name="urml_Statement", type=urml_ActionCode, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ActionCode117", type=urml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var118: BinaryAssociation = BinaryAssociation(
    name="var118",
    ends={
        Property(name="urml_LocalVar119", type=urml_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Variable", type=urml_LocalVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition101: BinaryAssociation = BinaryAssociation(
    name="condition101",
    ends={
        Property(name="urml_Expression102", type=urml_WhileLoopOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_WhileLoopOperation", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements103: BinaryAssociation = BinaryAssociation(
    name="statements103",
    ends={
        Property(name="urml_StatementOperation105", type=urml_WhileLoopOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_WhileLoopOperation104", type=urml_StatementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers123: BinaryAssociation = BinaryAssociation(
    name="triggers123",
    ends={
        Property(name="urml_Trigger_out124", type=urml_SendTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_SendTrigger", type=urml_Trigger_out, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerPort125: BinaryAssociation = BinaryAssociation(
    name="timerPort125",
    ends={
        Property(name="urml_TimerPort126", type=urml_InformTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_InformTimer", type=urml_TimerPort, multiplicity=Multiplicity(0, 1))
    }
)
time127: BinaryAssociation = BinaryAssociation(
    name="time127",
    ends={
        Property(name="urml_Expression129", type=urml_InformTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_InformTimer128", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation130: BinaryAssociation = BinaryAssociation(
    name="operation130",
    ends={
        Property(name="urml_Operation131", type=urml_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Invoke", type=urml_Operation, multiplicity=Multiplicity(0, 1))
    }
)
parameters132: BinaryAssociation = BinaryAssociation(
    name="parameters132",
    ends={
        Property(name="urml_Expression134", type=urml_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Invoke133", type=urml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lvalue135: BinaryAssociation = BinaryAssociation(
    name="lvalue135",
    ends={
        Property(name="urml_Assignable", type=urml_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Assignment", type=urml_Assignable, multiplicity=Multiplicity(0, 1))
    }
)
exp120: BinaryAssociation = BinaryAssociation(
    name="exp120",
    ends={
        Property(name="urml_Expression122", type=urml_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Variable121", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp136: BinaryAssociation = BinaryAssociation(
    name="exp136",
    ends={
        Property(name="urml_Expression138", type=urml_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Assignment137", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition139: BinaryAssociation = BinaryAssociation(
    name="condition139",
    ends={
        Property(name="urml_Expression140", type=urml_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_WhileLoop", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements141: BinaryAssociation = BinaryAssociation(
    name="statements141",
    ends={
        Property(name="urml_Statement143", type=urml_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_WhileLoop142", type=urml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition144: BinaryAssociation = BinaryAssociation(
    name="condition144",
    ends={
        Property(name="urml_Expression145", type=urml_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatement", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatements146: BinaryAssociation = BinaryAssociation(
    name="thenStatements146",
    ends={
        Property(name="urml_Statement148", type=urml_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatement147", type=urml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements149: BinaryAssociation = BinaryAssociation(
    name="elseStatements149",
    ends={
        Property(name="urml_Statement151", type=urml_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_IfStatement150", type=urml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logPort152: BinaryAssociation = BinaryAssociation(
    name="logPort152",
    ends={
        Property(name="urml_LogPort153", type=urml_LogStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LogStatement", type=urml_LogPort, multiplicity=Multiplicity(0, 1))
    }
)
left154: BinaryAssociation = BinaryAssociation(
    name="left154",
    ends={
        Property(name="urml_StringExpression", type=urml_LogStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LogStatement155", type=urml_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr156: BinaryAssociation = BinaryAssociation(
    name="expr156",
    ends={
        Property(name="urml_Expression158", type=urml_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_StringExpression157", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp159: BinaryAssociation = BinaryAssociation(
    name="exp159",
    ends={
        Property(name="urml_Expression160", type=urml_NotBooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_NotBooleanExpression", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id161: BinaryAssociation = BinaryAssociation(
    name="id161",
    ends={
        Property(name="urml_Identifiable", type=urml_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Identifier", type=urml_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
call162: BinaryAssociation = BinaryAssociation(
    name="call162",
    ends={
        Property(name="urml_Operation163", type=urml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_FunctionCall", type=urml_Operation, multiplicity=Multiplicity(0, 1))
    }
)
params164: BinaryAssociation = BinaryAssociation(
    name="params164",
    ends={
        Property(name="urml_Expression166", type=urml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_FunctionCall165", type=urml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left167: BinaryAssociation = BinaryAssociation(
    name="left167",
    ends={
        Property(name="urml_StringExpression168", type=urml_ConcatenateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConcatenateExpression", type=urml_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest169: BinaryAssociation = BinaryAssociation(
    name="rest169",
    ends={
        Property(name="urml_StringExpression171", type=urml_ConcatenateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConcatenateExpression170", type=urml_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left172: BinaryAssociation = BinaryAssociation(
    name="left172",
    ends={
        Property(name="urml_Expression173", type=urml_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConditionalOrExpression", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest174: BinaryAssociation = BinaryAssociation(
    name="rest174",
    ends={
        Property(name="urml_Expression176", type=urml_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConditionalOrExpression175", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left177: BinaryAssociation = BinaryAssociation(
    name="left177",
    ends={
        Property(name="urml_Expression178", type=urml_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConditionalAndExpression", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest179: BinaryAssociation = BinaryAssociation(
    name="rest179",
    ends={
        Property(name="urml_Expression181", type=urml_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_ConditionalAndExpression180", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left182: BinaryAssociation = BinaryAssociation(
    name="left182",
    ends={
        Property(name="urml_Expression183", type=urml_LessThanOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LessThanOrEqual", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest184: BinaryAssociation = BinaryAssociation(
    name="rest184",
    ends={
        Property(name="urml_Expression186", type=urml_LessThanOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LessThanOrEqual185", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left187: BinaryAssociation = BinaryAssociation(
    name="left187",
    ends={
        Property(name="urml_Expression188", type=urml_LessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LessThan", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest189: BinaryAssociation = BinaryAssociation(
    name="rest189",
    ends={
        Property(name="urml_Expression191", type=urml_LessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_LessThan190", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left192: BinaryAssociation = BinaryAssociation(
    name="left192",
    ends={
        Property(name="urml_Expression193", type=urml_GreaterThanOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_GreaterThanOrEqual", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest194: BinaryAssociation = BinaryAssociation(
    name="rest194",
    ends={
        Property(name="urml_Expression196", type=urml_GreaterThanOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_GreaterThanOrEqual195", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left197: BinaryAssociation = BinaryAssociation(
    name="left197",
    ends={
        Property(name="urml_Expression198", type=urml_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_GreaterThan", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest199: BinaryAssociation = BinaryAssociation(
    name="rest199",
    ends={
        Property(name="urml_Expression201", type=urml_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_GreaterThan200", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left202: BinaryAssociation = BinaryAssociation(
    name="left202",
    ends={
        Property(name="urml_Expression203", type=urml_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Equal", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left207: BinaryAssociation = BinaryAssociation(
    name="left207",
    ends={
        Property(name="urml_Expression208", type=urml_NotEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_NotEqual", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest209: BinaryAssociation = BinaryAssociation(
    name="rest209",
    ends={
        Property(name="urml_Expression211", type=urml_NotEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_NotEqual210", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left212: BinaryAssociation = BinaryAssociation(
    name="left212",
    ends={
        Property(name="urml_Expression213", type=urml_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Plus", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest214: BinaryAssociation = BinaryAssociation(
    name="rest214",
    ends={
        Property(name="urml_Expression216", type=urml_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Plus215", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left217: BinaryAssociation = BinaryAssociation(
    name="left217",
    ends={
        Property(name="urml_Expression218", type=urml_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Minus", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest219: BinaryAssociation = BinaryAssociation(
    name="rest219",
    ends={
        Property(name="urml_Expression221", type=urml_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Minus220", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest204: BinaryAssociation = BinaryAssociation(
    name="rest204",
    ends={
        Property(name="urml_Expression206", type=urml_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Equal205", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest224: BinaryAssociation = BinaryAssociation(
    name="rest224",
    ends={
        Property(name="urml_Expression226", type=urml_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Multiply225", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left227: BinaryAssociation = BinaryAssociation(
    name="left227",
    ends={
        Property(name="urml_Expression228", type=urml_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Divide", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest229: BinaryAssociation = BinaryAssociation(
    name="rest229",
    ends={
        Property(name="urml_Expression231", type=urml_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Divide230", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left232: BinaryAssociation = BinaryAssociation(
    name="left232",
    ends={
        Property(name="urml_Expression233", type=urml_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Modulo", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest234: BinaryAssociation = BinaryAssociation(
    name="rest234",
    ends={
        Property(name="urml_Expression236", type=urml_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Modulo235", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left222: BinaryAssociation = BinaryAssociation(
    name="left222",
    ends={
        Property(name="urml_Expression223", type=urml_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Multiply", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp237: BinaryAssociation = BinaryAssociation(
    name="exp237",
    ends={
        Property(name="urml_Expression238", type=urml_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_UnaryExpression", type=urml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_urml_Attribute_Assignable = Generalization(general=Assignable, specific=urml_Attribute)
gen_urml_LocalVar_Assignable = Generalization(general=Assignable, specific=urml_LocalVar)
gen_urml_IncomingVariable_Identifiable = Generalization(general=Identifiable, specific=urml_IncomingVariable)
gen_urml_WhileLoopOperation_StatementOperation = Generalization(general=StatementOperation, specific=urml_WhileLoopOperation)
gen_urml_IfStatementOperation_StatementOperation = Generalization(general=StatementOperation, specific=urml_IfStatementOperation)
gen_urml_ReturnStatement_StatementOperation = Generalization(general=StatementOperation, specific=urml_ReturnStatement)
gen_urml_Variable_StatementOperation = Generalization(general=StatementOperation, specific=urml_Variable)
gen_urml_Variable_Statement = Generalization(general=Statement, specific=urml_Variable)
gen_urml_InformTimer_StatementOperation = Generalization(general=StatementOperation, specific=urml_InformTimer)
gen_urml_InformTimer_Statement = Generalization(general=Statement, specific=urml_InformTimer)
gen_urml_NoOp_StatementOperation = Generalization(general=StatementOperation, specific=urml_NoOp)
gen_urml_NoOp_Statement = Generalization(general=Statement, specific=urml_NoOp)
gen_urml_Invoke_StatementOperation = Generalization(general=StatementOperation, specific=urml_Invoke)
gen_urml_Invoke_Statement = Generalization(general=Statement, specific=urml_Invoke)
gen_urml_Assignment_StatementOperation = Generalization(general=StatementOperation, specific=urml_Assignment)
gen_urml_Assignment_Statement = Generalization(general=Statement, specific=urml_Assignment)
gen_urml_SendTrigger_StatementOperation = Generalization(general=StatementOperation, specific=urml_SendTrigger)
gen_urml_SendTrigger_Statement = Generalization(general=Statement, specific=urml_SendTrigger)
gen_urml_WhileLoop_Statement = Generalization(general=Statement, specific=urml_WhileLoop)
gen_urml_IfStatement_Statement = Generalization(general=Statement, specific=urml_IfStatement)
gen_urml_LogStatement_StatementOperation = Generalization(general=StatementOperation, specific=urml_LogStatement)
gen_urml_LogStatement_Statement = Generalization(general=Statement, specific=urml_LogStatement)
gen_urml_Assignable_Identifiable = Generalization(general=Identifiable, specific=urml_Assignable)
gen_urml_NotBooleanExpression_Expression = Generalization(general=Expression, specific=urml_NotBooleanExpression)
gen_urml_Literal_Expression = Generalization(general=Expression, specific=urml_Literal)
gen_urml_IntLiteral_Literal = Generalization(general=Literal, specific=urml_IntLiteral)
gen_urml_Identifier_Expression = Generalization(general=Expression, specific=urml_Identifier)
gen_urml_FunctionCall_Literal = Generalization(general=Literal, specific=urml_FunctionCall)
gen_urml_BoolLiteral_Literal = Generalization(general=Literal, specific=urml_BoolLiteral)
gen_urml_ConditionalOrExpression_Expression = Generalization(general=Expression, specific=urml_ConditionalOrExpression)
gen_urml_ConditionalAndExpression_Expression = Generalization(general=Expression, specific=urml_ConditionalAndExpression)
gen_urml_LessThanOrEqual_Expression = Generalization(general=Expression, specific=urml_LessThanOrEqual)
gen_urml_ConcatenateExpression_StringExpression = Generalization(general=StringExpression, specific=urml_ConcatenateExpression)
gen_urml_GreaterThanOrEqual_Expression = Generalization(general=Expression, specific=urml_GreaterThanOrEqual)
gen_urml_GreaterThan_Expression = Generalization(general=Expression, specific=urml_GreaterThan)
gen_urml_Equal_Expression = Generalization(general=Expression, specific=urml_Equal)
gen_urml_LessThan_Expression = Generalization(general=Expression, specific=urml_LessThan)
gen_urml_NotEqual_Expression = Generalization(general=Expression, specific=urml_NotEqual)
gen_urml_Plus_Expression = Generalization(general=Expression, specific=urml_Plus)
gen_urml_Minus_Expression = Generalization(general=Expression, specific=urml_Minus)
gen_urml_Multiply_Expression = Generalization(general=Expression, specific=urml_Multiply)
gen_urml_Divide_Expression = Generalization(general=Expression, specific=urml_Divide)
gen_urml_Modulo_Expression = Generalization(general=Expression, specific=urml_Modulo)
gen_urml_UnaryExpression_Expression = Generalization(general=Expression, specific=urml_UnaryExpression)

# Domain Model
domain_model = DomainModel(
    name="urml",
    types={urml_Model, urml_Capsule, urml_Attribute, urml_Expression, urml_Signal, urml_Port, urml_Protocol, urml_LocalVar, Assignable, urml_CapsuleInst, urml_Connector, urml_Operation, urml_StateMachine, urml_OperationCode, urml_TimerPort, urml_LogPort, urml_ActionCode, urml_Trigger_in, urml_State_, urml_Transition, urml_IncomingVariable, Identifiable, urml_Trigger_out, urml_StatementOperation, urml_WhileLoopOperation, StatementOperation, urml_IfStatementOperation, urml_ReturnStatement, urml_Statement, urml_Variable, Statement, urml_InformTimer, urml_NoOp, urml_Invoke, urml_Assignment, urml_Assignable, urml_SendTrigger, urml_WhileLoop, urml_IfStatement, urml_LogStatement, urml_StringExpression, urml_NotBooleanExpression, Expression, urml_Literal, urml_IntLiteral, Literal, urml_Identifier, urml_Identifiable, urml_FunctionCall, urml_BoolLiteral, urml_ConditionalOrExpression, urml_ConditionalAndExpression, urml_LessThanOrEqual, urml_ConcatenateExpression, StringExpression, urml_GreaterThanOrEqual, urml_GreaterThan, urml_Equal, urml_LessThan, urml_NotEqual, urml_Plus, urml_Minus, urml_Multiply, urml_Divide, urml_Modulo, urml_UnaryExpression},
    associations={capsules0, defaultValue3, incomingMessages4, outgoingMessages6, LocalVars9, interfacePorts11, internalPorts13, protocols1, logPorts18, attributes20, capsuleInsts23, connectors25, operations27, statemachines29, LocalVars31, timerPorts16, protocol36, capsuleInst139, port142, capsuleInst245, port248, type51, operationCode34, entryCode58, exitCode60, substatemachine63, from66, to69, guard72, triggers75, states54, transitions56, from83, signal86, parameters89, to91, signal93, parameters96, statements99, timerPort77, action80, condition106, thenStatements108, elseStatements111, returnValue114, statements116, var118, condition101, statements103, triggers123, timerPort125, time127, operation130, parameters132, lvalue135, exp120, exp136, condition139, statements141, condition144, thenStatements146, elseStatements149, logPort152, left154, expr156, exp159, id161, call162, params164, left167, rest169, left172, rest174, left177, rest179, left182, rest184, left187, rest189, left192, rest194, left197, rest199, left202, left207, rest209, left212, rest214, left217, rest219, rest204, rest224, left227, rest229, left232, rest234, left222, exp237},
    generalizations={gen_urml_Attribute_Assignable, gen_urml_LocalVar_Assignable, gen_urml_IncomingVariable_Identifiable, gen_urml_WhileLoopOperation_StatementOperation, gen_urml_IfStatementOperation_StatementOperation, gen_urml_ReturnStatement_StatementOperation, gen_urml_Variable_StatementOperation, gen_urml_Variable_Statement, gen_urml_InformTimer_StatementOperation, gen_urml_InformTimer_Statement, gen_urml_NoOp_StatementOperation, gen_urml_NoOp_Statement, gen_urml_Invoke_StatementOperation, gen_urml_Invoke_Statement, gen_urml_Assignment_StatementOperation, gen_urml_Assignment_Statement, gen_urml_SendTrigger_StatementOperation, gen_urml_SendTrigger_Statement, gen_urml_WhileLoop_Statement, gen_urml_IfStatement_Statement, gen_urml_LogStatement_StatementOperation, gen_urml_LogStatement_Statement, gen_urml_Assignable_Identifiable, gen_urml_NotBooleanExpression_Expression, gen_urml_Literal_Expression, gen_urml_IntLiteral_Literal, gen_urml_Identifier_Expression, gen_urml_FunctionCall_Literal, gen_urml_BoolLiteral_Literal, gen_urml_ConditionalOrExpression_Expression, gen_urml_ConditionalAndExpression_Expression, gen_urml_LessThanOrEqual_Expression, gen_urml_ConcatenateExpression_StringExpression, gen_urml_GreaterThanOrEqual_Expression, gen_urml_GreaterThan_Expression, gen_urml_Equal_Expression, gen_urml_LessThan_Expression, gen_urml_NotEqual_Expression, gen_urml_Plus_Expression, gen_urml_Minus_Expression, gen_urml_Multiply_Expression, gen_urml_Divide_Expression, gen_urml_Modulo_Expression, gen_urml_UnaryExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)