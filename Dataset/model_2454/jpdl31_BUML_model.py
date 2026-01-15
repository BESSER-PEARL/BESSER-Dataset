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
BooleanType: Enumeration = Enumeration(
    name="BooleanType",
    literals={
            EnumerationLiteral(name="yes"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="off")
    }
)

ConfigType: Enumeration = Enumeration(
    name="ConfigType",
    literals={
            EnumerationLiteral(name="field"),
			EnumerationLiteral(name="bean"),
			EnumerationLiteral(name="constructor"),
			EnumerationLiteral(name="configurationProperty")
    }
)

ConfigTypeType: Enumeration = Enumeration(
    name="ConfigTypeType",
    literals={
            EnumerationLiteral(name="field"),
			EnumerationLiteral(name="bean"),
			EnumerationLiteral(name="constructor"),
			EnumerationLiteral(name="configurationProperty")
    }
)

ConfigTypeType1: Enumeration = Enumeration(
    name="ConfigTypeType1",
    literals={
            EnumerationLiteral(name="field"),
			EnumerationLiteral(name="bean"),
			EnumerationLiteral(name="constructor"),
			EnumerationLiteral(name="configurationProperty")
    }
)

PriorityTypeMember0: Enumeration = Enumeration(
    name="PriorityTypeMember0",
    literals={
            EnumerationLiteral(name="highest"),
			EnumerationLiteral(name="high"),
			EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="low"),
			EnumerationLiteral(name="lowest")
    }
)

SignalType: Enumeration = Enumeration(
    name="SignalType",
    literals={
            EnumerationLiteral(name="unsynchronized"),
			EnumerationLiteral(name="never"),
			EnumerationLiteral(name="first"),
			EnumerationLiteral(name="firstWait"),
			EnumerationLiteral(name="last"),
			EnumerationLiteral(name="lastWait")
    }
)

TypeTypeMember1: Enumeration = Enumeration(
    name="TypeTypeMember1",
    literals={
            EnumerationLiteral(name="nodeEnter"),
			EnumerationLiteral(name="nodeLeave"),
			EnumerationLiteral(name="processStart"),
			EnumerationLiteral(name="processEnd"),
			EnumerationLiteral(name="taskCreate"),
			EnumerationLiteral(name="taskAssign"),
			EnumerationLiteral(name="taskStart"),
			EnumerationLiteral(name="taskEnd"),
			EnumerationLiteral(name="beforeSignal"),
			EnumerationLiteral(name="afterSignal"),
			EnumerationLiteral(name="superstateEnter"),
			EnumerationLiteral(name="superstateLeave"),
			EnumerationLiteral(name="timerCreate"),
			EnumerationLiteral(name="subprocessCreated"),
			EnumerationLiteral(name="subprocessEnd")
    }
)

# Classes
jpdl31_ActionType = Class(name="jpdl31::ActionType")
jpdl31_AssignmentType = Class(name="jpdl31::AssignmentType")
Delegation = Class(name="Delegation")
jpdl31_ConditionType = Class(name="jpdl31::ConditionType")
jpdl31_CancelTimerType = Class(name="jpdl31::CancelTimerType")
jpdl31_CreateTimerType = Class(name="jpdl31::CreateTimerType")
jpdl31_ScriptType = Class(name="jpdl31::ScriptType")
jpdl31_DecisionType = Class(name="jpdl31::DecisionType")
jpdl31_Delegation = Class(name="jpdl31::Delegation")
jpdl31_ExceptionHandlerType = Class(name="jpdl31::ExceptionHandlerType")
jpdl31_TransitionType1 = Class(name="jpdl31::TransitionType1")
jpdl31_EventType = Class(name="jpdl31::EventType")
jpdl31_EStringToStringMapEntry = Class(name="jpdl31::EStringToStringMapEntry")
jpdl31_DocumentRoot = Class(name="jpdl31::DocumentRoot")
jpdl31_EndStateType = Class(name="jpdl31::EndStateType")
jpdl31_ForkType = Class(name="jpdl31::ForkType")
jpdl31_JoinType = Class(name="jpdl31::JoinType")
jpdl31_NodeType = Class(name="jpdl31::NodeType")
jpdl31_ProcessDefinitionType = Class(name="jpdl31::ProcessDefinitionType")
jpdl31_StartStateType = Class(name="jpdl31::StartStateType")
jpdl31_StateType = Class(name="jpdl31::StateType")
jpdl31_SuperStateType = Class(name="jpdl31::SuperStateType")
jpdl31_SwimlaneType = Class(name="jpdl31::SwimlaneType")
jpdl31_TaskType = Class(name="jpdl31::TaskType")
jpdl31_ProcessStateType = Class(name="jpdl31::ProcessStateType")
jpdl31_TimerType = Class(name="jpdl31::TimerType")
jpdl31_TransitionType = Class(name="jpdl31::TransitionType")
jpdl31_VariableType = Class(name="jpdl31::VariableType")
jpdl31_TaskNodeType = Class(name="jpdl31::TaskNodeType")
jpdl31_SubProcessType = Class(name="jpdl31::SubProcessType")

# jpdl31_ActionType class attributes and methods
jpdl31_ActionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ActionType_any: Property = Property(name="any", type=StringType)
jpdl31_ActionType_class: Property = Property(name="class", type=StringType)
jpdl31_ActionType_configType: Property = Property(name="configType", type=StringType)
jpdl31_ActionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_ActionType_name: Property = Property(name="name", type=StringType)
jpdl31_ActionType_refName: Property = Property(name="refName", type=StringType)
jpdl31_ActionType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl31_ActionType_async: Property = Property(name="async", type=StringType)
jpdl31_ActionType.attributes={jpdl31_ActionType_name, jpdl31_ActionType_mixed, jpdl31_ActionType_acceptPropagatedEvents, jpdl31_ActionType_configType, jpdl31_ActionType_expression, jpdl31_ActionType_async, jpdl31_ActionType_class, jpdl31_ActionType_refName, jpdl31_ActionType_any}

# jpdl31_AssignmentType class attributes and methods
jpdl31_AssignmentType_actorId: Property = Property(name="actorId", type=StringType)
jpdl31_AssignmentType_expression: Property = Property(name="expression", type=StringType)
jpdl31_AssignmentType_pooledActors: Property = Property(name="pooledActors", type=StringType)
jpdl31_AssignmentType.attributes={jpdl31_AssignmentType_actorId, jpdl31_AssignmentType_pooledActors, jpdl31_AssignmentType_expression}

# Delegation class attributes and methods

# jpdl31_ConditionType class attributes and methods
jpdl31_ConditionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ConditionType_group: Property = Property(name="group", type=StringType)
jpdl31_ConditionType_any: Property = Property(name="any", type=StringType)
jpdl31_ConditionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_ConditionType.attributes={jpdl31_ConditionType_group, jpdl31_ConditionType_mixed, jpdl31_ConditionType_expression, jpdl31_ConditionType_any}

# jpdl31_CancelTimerType class attributes and methods
jpdl31_CancelTimerType_name: Property = Property(name="name", type=StringType)
jpdl31_CancelTimerType.attributes={jpdl31_CancelTimerType_name}

# jpdl31_CreateTimerType class attributes and methods
jpdl31_CreateTimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl31_CreateTimerType_name: Property = Property(name="name", type=StringType)
jpdl31_CreateTimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl31_CreateTimerType_transition: Property = Property(name="transition", type=StringType)
jpdl31_CreateTimerType.attributes={jpdl31_CreateTimerType_name, jpdl31_CreateTimerType_duedate, jpdl31_CreateTimerType_transition, jpdl31_CreateTimerType_repeat}

# jpdl31_ScriptType class attributes and methods
jpdl31_ScriptType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl31_ScriptType_name: Property = Property(name="name", type=StringType)
jpdl31_ScriptType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ScriptType_any: Property = Property(name="any", type=StringType)
jpdl31_ScriptType.attributes={jpdl31_ScriptType_acceptPropagatedEvents, jpdl31_ScriptType_any, jpdl31_ScriptType_name, jpdl31_ScriptType_mixed}

# jpdl31_DecisionType class attributes and methods
jpdl31_DecisionType_group: Property = Property(name="group", type=StringType)
jpdl31_DecisionType_async: Property = Property(name="async", type=StringType)
jpdl31_DecisionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_DecisionType_name: Property = Property(name="name", type=StringType)
jpdl31_DecisionType.attributes={jpdl31_DecisionType_async, jpdl31_DecisionType_group, jpdl31_DecisionType_name, jpdl31_DecisionType_expression}

# jpdl31_Delegation class attributes and methods
jpdl31_Delegation_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_Delegation_any: Property = Property(name="any", type=StringType)
jpdl31_Delegation_class: Property = Property(name="class", type=StringType)
jpdl31_Delegation_configType: Property = Property(name="configType", type=StringType)
jpdl31_Delegation.attributes={jpdl31_Delegation_any, jpdl31_Delegation_configType, jpdl31_Delegation_class, jpdl31_Delegation_mixed}

# jpdl31_ExceptionHandlerType class attributes and methods
jpdl31_ExceptionHandlerType_exceptionClass: Property = Property(name="exceptionClass", type=StringType)
jpdl31_ExceptionHandlerType_group: Property = Property(name="group", type=StringType)
jpdl31_ExceptionHandlerType.attributes={jpdl31_ExceptionHandlerType_group, jpdl31_ExceptionHandlerType_exceptionClass}

# jpdl31_TransitionType1 class attributes and methods
jpdl31_TransitionType1_group: Property = Property(name="group", type=StringType)
jpdl31_TransitionType1_name: Property = Property(name="name", type=StringType)
jpdl31_TransitionType1_to: Property = Property(name="to", type=StringType)
jpdl31_TransitionType1.attributes={jpdl31_TransitionType1_to, jpdl31_TransitionType1_name, jpdl31_TransitionType1_group}

# jpdl31_EventType class attributes and methods
jpdl31_EventType_actionElements: Property = Property(name="actionElements", type=StringType)
jpdl31_EventType_type: Property = Property(name="type", type=StringType)
jpdl31_EventType.attributes={jpdl31_EventType_actionElements, jpdl31_EventType_type}

# jpdl31_EStringToStringMapEntry class attributes and methods

# jpdl31_DocumentRoot class attributes and methods
jpdl31_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_DocumentRoot.attributes={jpdl31_DocumentRoot_mixed}

# jpdl31_EndStateType class attributes and methods
jpdl31_EndStateType_group: Property = Property(name="group", type=StringType)
jpdl31_EndStateType_name: Property = Property(name="name", type=StringType)
jpdl31_EndStateType.attributes={jpdl31_EndStateType_name, jpdl31_EndStateType_group}

# jpdl31_ForkType class attributes and methods
jpdl31_ForkType_group: Property = Property(name="group", type=StringType)
jpdl31_ForkType_async: Property = Property(name="async", type=StringType)
jpdl31_ForkType_name: Property = Property(name="name", type=StringType)
jpdl31_ForkType.attributes={jpdl31_ForkType_name, jpdl31_ForkType_async, jpdl31_ForkType_group}

# jpdl31_JoinType class attributes and methods
jpdl31_JoinType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_JoinType_async: Property = Property(name="async", type=StringType)
jpdl31_JoinType_name: Property = Property(name="name", type=StringType)
jpdl31_JoinType.attributes={jpdl31_JoinType_name, jpdl31_JoinType_async, jpdl31_JoinType_nodeContentElements}

# jpdl31_NodeType class attributes and methods
jpdl31_NodeType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_NodeType_async: Property = Property(name="async", type=StringType)
jpdl31_NodeType_name: Property = Property(name="name", type=StringType)
jpdl31_NodeType.attributes={jpdl31_NodeType_async, jpdl31_NodeType_nodeContentElements, jpdl31_NodeType_name}

# jpdl31_ProcessDefinitionType class attributes and methods
jpdl31_ProcessDefinitionType_group: Property = Property(name="group", type=StringType)
jpdl31_ProcessDefinitionType_name: Property = Property(name="name", type=StringType)
jpdl31_ProcessDefinitionType.attributes={jpdl31_ProcessDefinitionType_name, jpdl31_ProcessDefinitionType_group}

# jpdl31_StartStateType class attributes and methods
jpdl31_StartStateType_group: Property = Property(name="group", type=StringType)
jpdl31_StartStateType_name: Property = Property(name="name", type=StringType)
jpdl31_StartStateType.attributes={jpdl31_StartStateType_group, jpdl31_StartStateType_name}

# jpdl31_StateType class attributes and methods
jpdl31_StateType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_StateType_async: Property = Property(name="async", type=StringType)
jpdl31_StateType_name: Property = Property(name="name", type=StringType)
jpdl31_StateType.attributes={jpdl31_StateType_name, jpdl31_StateType_nodeContentElements, jpdl31_StateType_async}

# jpdl31_SuperStateType class attributes and methods
jpdl31_SuperStateType_group: Property = Property(name="group", type=StringType)
jpdl31_SuperStateType_async: Property = Property(name="async", type=StringType)
jpdl31_SuperStateType_name: Property = Property(name="name", type=StringType)
jpdl31_SuperStateType.attributes={jpdl31_SuperStateType_name, jpdl31_SuperStateType_group, jpdl31_SuperStateType_async}

# jpdl31_SwimlaneType class attributes and methods
jpdl31_SwimlaneType_name: Property = Property(name="name", type=StringType)
jpdl31_SwimlaneType.attributes={jpdl31_SwimlaneType_name}

# jpdl31_TaskType class attributes and methods
jpdl31_TaskType_group: Property = Property(name="group", type=StringType)
jpdl31_TaskType_blocking: Property = Property(name="blocking", type=StringType)
jpdl31_TaskType_description: Property = Property(name="description", type=StringType)
jpdl31_TaskType_duedate: Property = Property(name="duedate", type=StringType)
jpdl31_TaskType_name: Property = Property(name="name", type=StringType)
jpdl31_TaskType_priority: Property = Property(name="priority", type=StringType)
jpdl31_TaskType_signalling: Property = Property(name="signalling", type=StringType)
jpdl31_TaskType_swimlane: Property = Property(name="swimlane", type=StringType)
jpdl31_TaskType.attributes={jpdl31_TaskType_duedate, jpdl31_TaskType_signalling, jpdl31_TaskType_blocking, jpdl31_TaskType_swimlane, jpdl31_TaskType_description, jpdl31_TaskType_group, jpdl31_TaskType_name, jpdl31_TaskType_priority}

# jpdl31_ProcessStateType class attributes and methods
jpdl31_ProcessStateType_group: Property = Property(name="group", type=StringType)
jpdl31_ProcessStateType_async: Property = Property(name="async", type=StringType)
jpdl31_ProcessStateType_name: Property = Property(name="name", type=StringType)
jpdl31_ProcessStateType.attributes={jpdl31_ProcessStateType_group, jpdl31_ProcessStateType_async, jpdl31_ProcessStateType_name}

# jpdl31_TimerType class attributes and methods
jpdl31_TimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl31_TimerType_name: Property = Property(name="name", type=StringType)
jpdl31_TimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl31_TimerType_transition: Property = Property(name="transition", type=StringType)
jpdl31_TimerType.attributes={jpdl31_TimerType_transition, jpdl31_TimerType_duedate, jpdl31_TimerType_name, jpdl31_TimerType_repeat}

# jpdl31_TransitionType class attributes and methods
jpdl31_TransitionType_group: Property = Property(name="group", type=StringType)
jpdl31_TransitionType_name: Property = Property(name="name", type=StringType)
jpdl31_TransitionType_to: Property = Property(name="to", type=StringType)
jpdl31_TransitionType.attributes={jpdl31_TransitionType_name, jpdl31_TransitionType_group, jpdl31_TransitionType_to}

# jpdl31_VariableType class attributes and methods
jpdl31_VariableType_name: Property = Property(name="name", type=StringType)
jpdl31_VariableType_any: Property = Property(name="any", type=StringType)
jpdl31_VariableType_access: Property = Property(name="access", type=StringType)
jpdl31_VariableType_mappedName: Property = Property(name="mappedName", type=StringType)
jpdl31_VariableType.attributes={jpdl31_VariableType_mappedName, jpdl31_VariableType_any, jpdl31_VariableType_name, jpdl31_VariableType_access}

# jpdl31_TaskNodeType class attributes and methods
jpdl31_TaskNodeType_group: Property = Property(name="group", type=StringType)
jpdl31_TaskNodeType_async: Property = Property(name="async", type=StringType)
jpdl31_TaskNodeType_createTasks: Property = Property(name="createTasks", type=StringType)
jpdl31_TaskNodeType_endTasks: Property = Property(name="endTasks", type=StringType)
jpdl31_TaskNodeType_name: Property = Property(name="name", type=StringType)
jpdl31_TaskNodeType_signal: Property = Property(name="signal", type=StringType)
jpdl31_TaskNodeType.attributes={jpdl31_TaskNodeType_name, jpdl31_TaskNodeType_createTasks, jpdl31_TaskNodeType_async, jpdl31_TaskNodeType_signal, jpdl31_TaskNodeType_group, jpdl31_TaskNodeType_endTasks}

# jpdl31_SubProcessType class attributes and methods
jpdl31_SubProcessType_name: Property = Property(name="name", type=StringType)
jpdl31_SubProcessType_version: Property = Property(name="version", type=StringType)
jpdl31_SubProcessType.attributes={jpdl31_SubProcessType_version, jpdl31_SubProcessType_name}

# Relationships
action0: BinaryAssociation = BinaryAssociation(
    name="action0",
    ends={
        Property(name="jpdl31_ActionType", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_CreateTimerType", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script1: BinaryAssociation = BinaryAssociation(
    name="script1",
    ends={
        Property(name="jpdl31_ScriptType", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_CreateTimerType2", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionHandler6: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler6",
    ends={
        Property(name="jpdl31_ExceptionHandlerType", type=jpdl31_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DecisionType7", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="jpdl31_TransitionType1", type=jpdl31_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DecisionType9", type=jpdl31_TransitionType1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler3: BinaryAssociation = BinaryAssociation(
    name="handler3",
    ends={
        Property(name="jpdl31_Delegation", type=jpdl31_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DecisionType", type=jpdl31_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event4: BinaryAssociation = BinaryAssociation(
    name="event4",
    ends={
        Property(name="jpdl31_EventType", type=jpdl31_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DecisionType5", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap10: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap10",
    ends={
        Property(name="jpdl31_EStringToStringMapEntry", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot", type=jpdl31_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation11: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation11",
    ends={
        Property(name="jpdl31_EStringToStringMapEntry13", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot12", type=jpdl31_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action14: BinaryAssociation = BinaryAssociation(
    name="action14",
    ends={
        Property(name="jpdl31_ActionType16", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot15", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment17: BinaryAssociation = BinaryAssociation(
    name="assignment17",
    ends={
        Property(name="jpdl31_AssignmentType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot18", type=jpdl31_AssignmentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer19: BinaryAssociation = BinaryAssociation(
    name="cancelTimer19",
    ends={
        Property(name="jpdl31_CancelTimerType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot20", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller21: BinaryAssociation = BinaryAssociation(
    name="controller21",
    ends={
        Property(name="jpdl31_Delegation23", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot22", type=jpdl31_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState30: BinaryAssociation = BinaryAssociation(
    name="endState30",
    ends={
        Property(name="jpdl31_EndStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot31", type=jpdl31_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="jpdl31_EventType34", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot33", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler35: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler35",
    ends={
        Property(name="jpdl31_ExceptionHandlerType37", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot36", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork38: BinaryAssociation = BinaryAssociation(
    name="fork38",
    ends={
        Property(name="jpdl31_ForkType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot39", type=jpdl31_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join40: BinaryAssociation = BinaryAssociation(
    name="join40",
    ends={
        Property(name="jpdl31_JoinType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot41", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node42: BinaryAssociation = BinaryAssociation(
    name="node42",
    ends={
        Property(name="jpdl31_NodeType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot43", type=jpdl31_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processDefinition44: BinaryAssociation = BinaryAssociation(
    name="processDefinition44",
    ends={
        Property(name="jpdl31_ProcessDefinitionType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot45", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer24: BinaryAssociation = BinaryAssociation(
    name="createTimer24",
    ends={
        Property(name="jpdl31_CreateTimerType26", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot25", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision27: BinaryAssociation = BinaryAssociation(
    name="decision27",
    ends={
        Property(name="jpdl31_DecisionType29", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot28", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script48: BinaryAssociation = BinaryAssociation(
    name="script48",
    ends={
        Property(name="jpdl31_ScriptType50", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot49", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState51: BinaryAssociation = BinaryAssociation(
    name="startState51",
    ends={
        Property(name="jpdl31_StartStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot52", type=jpdl31_StartStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state53: BinaryAssociation = BinaryAssociation(
    name="state53",
    ends={
        Property(name="jpdl31_StateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot54", type=jpdl31_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState55: BinaryAssociation = BinaryAssociation(
    name="superState55",
    ends={
        Property(name="jpdl31_SuperStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot56", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swimlane57: BinaryAssociation = BinaryAssociation(
    name="swimlane57",
    ends={
        Property(name="jpdl31_SwimlaneType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot58", type=jpdl31_SwimlaneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task59: BinaryAssociation = BinaryAssociation(
    name="task59",
    ends={
        Property(name="jpdl31_TaskType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot60", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState46: BinaryAssociation = BinaryAssociation(
    name="processState46",
    ends={
        Property(name="jpdl31_ProcessStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot47", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer63: BinaryAssociation = BinaryAssociation(
    name="timer63",
    ends={
        Property(name="jpdl31_TimerType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot64", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition65: BinaryAssociation = BinaryAssociation(
    name="transition65",
    ends={
        Property(name="jpdl31_TransitionType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot66", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable67: BinaryAssociation = BinaryAssociation(
    name="variable67",
    ends={
        Property(name="jpdl31_VariableType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot68", type=jpdl31_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event69: BinaryAssociation = BinaryAssociation(
    name="event69",
    ends={
        Property(name="jpdl31_EventType71", type=jpdl31_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EndStateType70", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode61: BinaryAssociation = BinaryAssociation(
    name="taskNode61",
    ends={
        Property(name="jpdl31_TaskNodeType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot62", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action75: BinaryAssociation = BinaryAssociation(
    name="action75",
    ends={
        Property(name="jpdl31_ActionType77", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType76", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script78: BinaryAssociation = BinaryAssociation(
    name="script78",
    ends={
        Property(name="jpdl31_ScriptType80", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType79", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer81: BinaryAssociation = BinaryAssociation(
    name="createTimer81",
    ends={
        Property(name="jpdl31_CreateTimerType83", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType82", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer84: BinaryAssociation = BinaryAssociation(
    name="cancelTimer84",
    ends={
        Property(name="jpdl31_CancelTimerType86", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType85", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler72: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler72",
    ends={
        Property(name="jpdl31_ExceptionHandlerType74", type=jpdl31_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EndStateType73", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action87: BinaryAssociation = BinaryAssociation(
    name="action87",
    ends={
        Property(name="jpdl31_ActionType89", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExceptionHandlerType88", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script90: BinaryAssociation = BinaryAssociation(
    name="script90",
    ends={
        Property(name="jpdl31_ScriptType92", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExceptionHandlerType91", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script93: BinaryAssociation = BinaryAssociation(
    name="script93",
    ends={
        Property(name="jpdl31_ScriptType95", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType94", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event96: BinaryAssociation = BinaryAssociation(
    name="event96",
    ends={
        Property(name="jpdl31_EventType98", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType97", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition105: BinaryAssociation = BinaryAssociation(
    name="transition105",
    ends={
        Property(name="jpdl31_TransitionType107", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType106", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event108: BinaryAssociation = BinaryAssociation(
    name="event108",
    ends={
        Property(name="jpdl31_EventType110", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType109", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler111: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler111",
    ends={
        Property(name="jpdl31_ExceptionHandlerType113", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType112", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler99: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler99",
    ends={
        Property(name="jpdl31_ExceptionHandlerType101", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType100", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer102: BinaryAssociation = BinaryAssociation(
    name="timer102",
    ends={
        Property(name="jpdl31_TimerType104", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType103", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition117: BinaryAssociation = BinaryAssociation(
    name="transition117",
    ends={
        Property(name="jpdl31_TransitionType119", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType118", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action120: BinaryAssociation = BinaryAssociation(
    name="action120",
    ends={
        Property(name="jpdl31_ActionType122", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType121", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timer114: BinaryAssociation = BinaryAssociation(
    name="timer114",
    ends={
        Property(name="jpdl31_TimerType116", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType115", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script123: BinaryAssociation = BinaryAssociation(
    name="script123",
    ends={
        Property(name="jpdl31_ScriptType125", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType124", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createTimer126: BinaryAssociation = BinaryAssociation(
    name="createTimer126",
    ends={
        Property(name="jpdl31_CreateTimerType128", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType127", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cancelTimer129: BinaryAssociation = BinaryAssociation(
    name="cancelTimer129",
    ends={
        Property(name="jpdl31_CancelTimerType131", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType130", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event132: BinaryAssociation = BinaryAssociation(
    name="event132",
    ends={
        Property(name="jpdl31_EventType134", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType133", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition141: BinaryAssociation = BinaryAssociation(
    name="transition141",
    ends={
        Property(name="jpdl31_TransitionType143", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType142", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler135: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler135",
    ends={
        Property(name="jpdl31_ExceptionHandlerType137", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType136", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer138: BinaryAssociation = BinaryAssociation(
    name="timer138",
    ends={
        Property(name="jpdl31_TimerType140", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType139", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node150: BinaryAssociation = BinaryAssociation(
    name="node150",
    ends={
        Property(name="jpdl31_NodeType152", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType151", type=jpdl31_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state153: BinaryAssociation = BinaryAssociation(
    name="state153",
    ends={
        Property(name="jpdl31_StateType155", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType154", type=jpdl31_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode156: BinaryAssociation = BinaryAssociation(
    name="taskNode156",
    ends={
        Property(name="jpdl31_TaskNodeType158", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType157", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState159: BinaryAssociation = BinaryAssociation(
    name="superState159",
    ends={
        Property(name="jpdl31_SuperStateType161", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType160", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState162: BinaryAssociation = BinaryAssociation(
    name="processState162",
    ends={
        Property(name="jpdl31_ProcessStateType164", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType163", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork165: BinaryAssociation = BinaryAssociation(
    name="fork165",
    ends={
        Property(name="jpdl31_ForkType167", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType166", type=jpdl31_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swimlane144: BinaryAssociation = BinaryAssociation(
    name="swimlane144",
    ends={
        Property(name="jpdl31_SwimlaneType146", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType145", type=jpdl31_SwimlaneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState147: BinaryAssociation = BinaryAssociation(
    name="startState147",
    ends={
        Property(name="jpdl31_StartStateType149", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType148", type=jpdl31_StartStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState174: BinaryAssociation = BinaryAssociation(
    name="endState174",
    ends={
        Property(name="jpdl31_EndStateType176", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType175", type=jpdl31_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action177: BinaryAssociation = BinaryAssociation(
    name="action177",
    ends={
        Property(name="jpdl31_ActionType179", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType178", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script180: BinaryAssociation = BinaryAssociation(
    name="script180",
    ends={
        Property(name="jpdl31_ScriptType182", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType181", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer183: BinaryAssociation = BinaryAssociation(
    name="createTimer183",
    ends={
        Property(name="jpdl31_CreateTimerType185", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType184", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer186: BinaryAssociation = BinaryAssociation(
    name="cancelTimer186",
    ends={
        Property(name="jpdl31_CancelTimerType188", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType187", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join168: BinaryAssociation = BinaryAssociation(
    name="join168",
    ends={
        Property(name="jpdl31_JoinType170", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType169", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision171: BinaryAssociation = BinaryAssociation(
    name="decision171",
    ends={
        Property(name="jpdl31_DecisionType173", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType172", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler192: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler192",
    ends={
        Property(name="jpdl31_ExceptionHandlerType194", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType193", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task195: BinaryAssociation = BinaryAssociation(
    name="task195",
    ends={
        Property(name="jpdl31_TaskType197", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType196", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess198: BinaryAssociation = BinaryAssociation(
    name="subProcess198",
    ends={
        Property(name="jpdl31_SubProcessType", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType199", type=jpdl31_SubProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event189: BinaryAssociation = BinaryAssociation(
    name="event189",
    ends={
        Property(name="jpdl31_EventType191", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType190", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler206: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler206",
    ends={
        Property(name="jpdl31_ExceptionHandlerType208", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType207", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer209: BinaryAssociation = BinaryAssociation(
    name="timer209",
    ends={
        Property(name="jpdl31_TimerType211", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType210", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition212: BinaryAssociation = BinaryAssociation(
    name="transition212",
    ends={
        Property(name="jpdl31_TransitionType214", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType213", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable200: BinaryAssociation = BinaryAssociation(
    name="variable200",
    ends={
        Property(name="jpdl31_VariableType202", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType201", type=jpdl31_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event203: BinaryAssociation = BinaryAssociation(
    name="event203",
    ends={
        Property(name="jpdl31_EventType205", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType204", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task215: BinaryAssociation = BinaryAssociation(
    name="task215",
    ends={
        Property(name="jpdl31_TaskType217", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType216", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition218: BinaryAssociation = BinaryAssociation(
    name="transition218",
    ends={
        Property(name="jpdl31_TransitionType220", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType219", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler224: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler224",
    ends={
        Property(name="jpdl31_ExceptionHandlerType226", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType225", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event227: BinaryAssociation = BinaryAssociation(
    name="event227",
    ends={
        Property(name="jpdl31_EventType229", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType228", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler230: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler230",
    ends={
        Property(name="jpdl31_ExceptionHandlerType232", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType231", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event221: BinaryAssociation = BinaryAssociation(
    name="event221",
    ends={
        Property(name="jpdl31_EventType223", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType222", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node239: BinaryAssociation = BinaryAssociation(
    name="node239",
    ends={
        Property(name="jpdl31_NodeType241", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType240", type=jpdl31_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer233: BinaryAssociation = BinaryAssociation(
    name="timer233",
    ends={
        Property(name="jpdl31_TimerType235", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType234", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition236: BinaryAssociation = BinaryAssociation(
    name="transition236",
    ends={
        Property(name="jpdl31_TransitionType238", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType237", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode245: BinaryAssociation = BinaryAssociation(
    name="taskNode245",
    ends={
        Property(name="jpdl31_SuperStateType246", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="jpdl31_TaskNodeType247", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1))
    }
)
superState249: BinaryAssociation = BinaryAssociation(
    name="superState249",
    ends={
        Property(name="jpdl31_SuperStateType250", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType248", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState251: BinaryAssociation = BinaryAssociation(
    name="processState251",
    ends={
        Property(name="jpdl31_ProcessStateType253", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType252", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork254: BinaryAssociation = BinaryAssociation(
    name="fork254",
    ends={
        Property(name="jpdl31_ForkType256", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType255", type=jpdl31_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join257: BinaryAssociation = BinaryAssociation(
    name="join257",
    ends={
        Property(name="jpdl31_JoinType259", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType258", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state242: BinaryAssociation = BinaryAssociation(
    name="state242",
    ends={
        Property(name="jpdl31_StateType244", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType243", type=jpdl31_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event266: BinaryAssociation = BinaryAssociation(
    name="event266",
    ends={
        Property(name="jpdl31_EventType268", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType267", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler269: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler269",
    ends={
        Property(name="jpdl31_ExceptionHandlerType271", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType270", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer272: BinaryAssociation = BinaryAssociation(
    name="timer272",
    ends={
        Property(name="jpdl31_TimerType274", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType273", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition275: BinaryAssociation = BinaryAssociation(
    name="transition275",
    ends={
        Property(name="jpdl31_TransitionType277", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType276", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision260: BinaryAssociation = BinaryAssociation(
    name="decision260",
    ends={
        Property(name="jpdl31_DecisionType262", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType261", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState263: BinaryAssociation = BinaryAssociation(
    name="endState263",
    ends={
        Property(name="jpdl31_EndStateType265", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType264", type=jpdl31_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment278: BinaryAssociation = BinaryAssociation(
    name="assignment278",
    ends={
        Property(name="jpdl31_AssignmentType280", type=jpdl31_SwimlaneType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SwimlaneType279", type=jpdl31_AssignmentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task281: BinaryAssociation = BinaryAssociation(
    name="task281",
    ends={
        Property(name="jpdl31_TaskType283", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType282", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event284: BinaryAssociation = BinaryAssociation(
    name="event284",
    ends={
        Property(name="jpdl31_EventType286", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType285", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler287: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler287",
    ends={
        Property(name="jpdl31_ExceptionHandlerType289", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType288", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition293: BinaryAssociation = BinaryAssociation(
    name="transition293",
    ends={
        Property(name="jpdl31_TransitionType295", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType294", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment296: BinaryAssociation = BinaryAssociation(
    name="assignment296",
    ends={
        Property(name="jpdl31_AssignmentType298", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType297", type=jpdl31_AssignmentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer290: BinaryAssociation = BinaryAssociation(
    name="timer290",
    ends={
        Property(name="jpdl31_TimerType292", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType291", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event302: BinaryAssociation = BinaryAssociation(
    name="event302",
    ends={
        Property(name="jpdl31_EventType304", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType303", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer305: BinaryAssociation = BinaryAssociation(
    name="timer305",
    ends={
        Property(name="jpdl31_TimerType307", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType306", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller299: BinaryAssociation = BinaryAssociation(
    name="controller299",
    ends={
        Property(name="jpdl31_Delegation301", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType300", type=jpdl31_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action308: BinaryAssociation = BinaryAssociation(
    name="action308",
    ends={
        Property(name="jpdl31_ActionType310", type=jpdl31_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TimerType309", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script311: BinaryAssociation = BinaryAssociation(
    name="script311",
    ends={
        Property(name="jpdl31_ScriptType313", type=jpdl31_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TimerType312", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action314: BinaryAssociation = BinaryAssociation(
    name="action314",
    ends={
        Property(name="jpdl31_ActionType316", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType315", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer320: BinaryAssociation = BinaryAssociation(
    name="createTimer320",
    ends={
        Property(name="jpdl31_CreateTimerType322", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType321", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer323: BinaryAssociation = BinaryAssociation(
    name="cancelTimer323",
    ends={
        Property(name="jpdl31_CancelTimerType325", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType324", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler326: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler326",
    ends={
        Property(name="jpdl31_ExceptionHandlerType328", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType327", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script317: BinaryAssociation = BinaryAssociation(
    name="script317",
    ends={
        Property(name="jpdl31_ScriptType319", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType318", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition329: BinaryAssociation = BinaryAssociation(
    name="condition329",
    ends={
        Property(name="jpdl31_ConditionType", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1330", type=jpdl31_ConditionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action331: BinaryAssociation = BinaryAssociation(
    name="action331",
    ends={
        Property(name="jpdl31_ActionType333", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1332", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script334: BinaryAssociation = BinaryAssociation(
    name="script334",
    ends={
        Property(name="jpdl31_ScriptType336", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1335", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler343: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler343",
    ends={
        Property(name="jpdl31_ExceptionHandlerType345", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1344", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer337: BinaryAssociation = BinaryAssociation(
    name="createTimer337",
    ends={
        Property(name="jpdl31_CreateTimerType339", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1338", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer340: BinaryAssociation = BinaryAssociation(
    name="cancelTimer340",
    ends={
        Property(name="jpdl31_CancelTimerType342", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1341", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jpdl31_AssignmentType_Delegation = Generalization(general=Delegation, specific=jpdl31_AssignmentType)

# Domain Model
domain_model = DomainModel(
    name="jpdl31",
    types={jpdl31_ActionType, jpdl31_AssignmentType, Delegation, jpdl31_ConditionType, jpdl31_CancelTimerType, jpdl31_CreateTimerType, jpdl31_ScriptType, jpdl31_DecisionType, jpdl31_Delegation, jpdl31_ExceptionHandlerType, jpdl31_TransitionType1, jpdl31_EventType, jpdl31_EStringToStringMapEntry, jpdl31_DocumentRoot, jpdl31_EndStateType, jpdl31_ForkType, jpdl31_JoinType, jpdl31_NodeType, jpdl31_ProcessDefinitionType, jpdl31_StartStateType, jpdl31_StateType, jpdl31_SuperStateType, jpdl31_SwimlaneType, jpdl31_TaskType, jpdl31_ProcessStateType, jpdl31_TimerType, jpdl31_TransitionType, jpdl31_VariableType, jpdl31_TaskNodeType, jpdl31_SubProcessType, BooleanType, ConfigType, ConfigTypeType, ConfigTypeType1, PriorityTypeMember0, SignalType, TypeTypeMember1},
    associations={action0, script1, exceptionHandler6, transition8, handler3, event4, xMLNSPrefixMap10, xSISchemaLocation11, action14, assignment17, cancelTimer19, controller21, endState30, event32, exceptionHandler35, fork38, join40, node42, processDefinition44, createTimer24, decision27, script48, startState51, state53, superState55, swimlane57, task59, processState46, timer63, transition65, variable67, event69, taskNode61, action75, script78, createTimer81, cancelTimer84, exceptionHandler72, action87, script90, script93, event96, transition105, event108, exceptionHandler111, exceptionHandler99, timer102, transition117, action120, timer114, script123, createTimer126, cancelTimer129, event132, transition141, exceptionHandler135, timer138, node150, state153, taskNode156, superState159, processState162, fork165, swimlane144, startState147, endState174, action177, script180, createTimer183, cancelTimer186, join168, decision171, exceptionHandler192, task195, subProcess198, event189, exceptionHandler206, timer209, transition212, variable200, event203, task215, transition218, exceptionHandler224, event227, exceptionHandler230, event221, node239, timer233, transition236, taskNode245, superState249, processState251, fork254, join257, state242, event266, exceptionHandler269, timer272, transition275, decision260, endState263, assignment278, task281, event284, exceptionHandler287, transition293, assignment296, timer290, event302, timer305, controller299, action308, script311, action314, createTimer320, cancelTimer323, exceptionHandler326, script317, condition329, action331, script334, exceptionHandler343, createTimer337, cancelTimer340},
    generalizations={gen_jpdl31_AssignmentType_Delegation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)