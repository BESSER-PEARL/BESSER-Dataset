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
BindingType: Enumeration = Enumeration(
    name="BindingType",
    literals={
            EnumerationLiteral(name="late"),
			EnumerationLiteral(name="early")
    }
)

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
			EnumerationLiteral(name="timerCreate"),
			EnumerationLiteral(name="subprocessCreated"),
			EnumerationLiteral(name="subprocessEnd"),
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
			EnumerationLiteral(name="superstateLeave")
    }
)

# Classes
jpdl32_ActionType = Class(name="jpdl32::ActionType")
jpdl32_AssignmentType = Class(name="jpdl32::AssignmentType")
Delegation = Class(name="Delegation")
jpdl32_CancelTimerType = Class(name="jpdl32::CancelTimerType")
jpdl32_ConditionType = Class(name="jpdl32::ConditionType")
jpdl32_ScriptType = Class(name="jpdl32::ScriptType")
jpdl32_CreateTimerType = Class(name="jpdl32::CreateTimerType")
jpdl32_Delegation = Class(name="jpdl32::Delegation")
jpdl32_EventType = Class(name="jpdl32::EventType")
jpdl32_DecisionType = Class(name="jpdl32::DecisionType")
jpdl32_ExceptionHandlerType = Class(name="jpdl32::ExceptionHandlerType")
jpdl32_TransitionType = Class(name="jpdl32::TransitionType")
jpdl32_EStringToStringMapEntry = Class(name="jpdl32::EStringToStringMapEntry")
jpdl32_DocumentRoot = Class(name="jpdl32::DocumentRoot")
jpdl32_EndStateType = Class(name="jpdl32::EndStateType")
jpdl32_MailNodeType = Class(name="jpdl32::MailNodeType")
jpdl32_NodeType = Class(name="jpdl32::NodeType")
jpdl32_ForkType = Class(name="jpdl32::ForkType")
jpdl32_JoinType = Class(name="jpdl32::JoinType")
jpdl32_MailType = Class(name="jpdl32::MailType")
jpdl32_ProcessDefinitionType = Class(name="jpdl32::ProcessDefinitionType")
jpdl32_ProcessStateType = Class(name="jpdl32::ProcessStateType")
jpdl32_SuperStateType = Class(name="jpdl32::SuperStateType")
jpdl32_StartStateType = Class(name="jpdl32::StartStateType")
jpdl32_StateType = Class(name="jpdl32::StateType")
jpdl32_TaskNodeType = Class(name="jpdl32::TaskNodeType")
jpdl32_SwimlaneType = Class(name="jpdl32::SwimlaneType")
jpdl32_TaskType = Class(name="jpdl32::TaskType")
jpdl32_TimerType = Class(name="jpdl32::TimerType")
jpdl32_VariableType = Class(name="jpdl32::VariableType")
jpdl32_SubProcessType = Class(name="jpdl32::SubProcessType")
jpdl32_ReminderType = Class(name="jpdl32::ReminderType")

# jpdl32_ActionType class attributes and methods
jpdl32_ActionType_async: Property = Property(name="async", type=StringType)
jpdl32_ActionType_class: Property = Property(name="class", type=StringType)
jpdl32_ActionType_configType: Property = Property(name="configType", type=StringType)
jpdl32_ActionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl32_ActionType_any: Property = Property(name="any", type=StringType)
jpdl32_ActionType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl32_ActionType_expression: Property = Property(name="expression", type=StringType)
jpdl32_ActionType_name: Property = Property(name="name", type=StringType)
jpdl32_ActionType_refName: Property = Property(name="refName", type=StringType)
jpdl32_ActionType.attributes={jpdl32_ActionType_configType, jpdl32_ActionType_name, jpdl32_ActionType_refName, jpdl32_ActionType_acceptPropagatedEvents, jpdl32_ActionType_expression, jpdl32_ActionType_mixed, jpdl32_ActionType_async, jpdl32_ActionType_class, jpdl32_ActionType_any}

# jpdl32_AssignmentType class attributes and methods
jpdl32_AssignmentType_pooledActors: Property = Property(name="pooledActors", type=StringType)
jpdl32_AssignmentType_actorId: Property = Property(name="actorId", type=StringType)
jpdl32_AssignmentType_expression: Property = Property(name="expression", type=StringType)
jpdl32_AssignmentType.attributes={jpdl32_AssignmentType_expression, jpdl32_AssignmentType_pooledActors, jpdl32_AssignmentType_actorId}

# Delegation class attributes and methods

# jpdl32_CancelTimerType class attributes and methods
jpdl32_CancelTimerType_name: Property = Property(name="name", type=StringType)
jpdl32_CancelTimerType.attributes={jpdl32_CancelTimerType_name}

# jpdl32_ConditionType class attributes and methods
jpdl32_ConditionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl32_ConditionType_group: Property = Property(name="group", type=StringType)
jpdl32_ConditionType_any: Property = Property(name="any", type=StringType)
jpdl32_ConditionType_expression: Property = Property(name="expression", type=StringType)
jpdl32_ConditionType.attributes={jpdl32_ConditionType_any, jpdl32_ConditionType_mixed, jpdl32_ConditionType_expression, jpdl32_ConditionType_group}

# jpdl32_ScriptType class attributes and methods
jpdl32_ScriptType_any: Property = Property(name="any", type=StringType)
jpdl32_ScriptType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl32_ScriptType_name: Property = Property(name="name", type=StringType)
jpdl32_ScriptType_mixed: Property = Property(name="mixed", type=StringType)
jpdl32_ScriptType.attributes={jpdl32_ScriptType_acceptPropagatedEvents, jpdl32_ScriptType_mixed, jpdl32_ScriptType_any, jpdl32_ScriptType_name}

# jpdl32_CreateTimerType class attributes and methods
jpdl32_CreateTimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl32_CreateTimerType_name: Property = Property(name="name", type=StringType)
jpdl32_CreateTimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl32_CreateTimerType_transition: Property = Property(name="transition", type=StringType)
jpdl32_CreateTimerType.attributes={jpdl32_CreateTimerType_duedate, jpdl32_CreateTimerType_repeat, jpdl32_CreateTimerType_name, jpdl32_CreateTimerType_transition}

# jpdl32_Delegation class attributes and methods
jpdl32_Delegation_mixed: Property = Property(name="mixed", type=StringType)
jpdl32_Delegation_any: Property = Property(name="any", type=StringType)
jpdl32_Delegation_class: Property = Property(name="class", type=StringType)
jpdl32_Delegation_configType: Property = Property(name="configType", type=StringType)
jpdl32_Delegation.attributes={jpdl32_Delegation_mixed, jpdl32_Delegation_configType, jpdl32_Delegation_class, jpdl32_Delegation_any}

# jpdl32_EventType class attributes and methods
jpdl32_EventType_actionElements: Property = Property(name="actionElements", type=StringType)
jpdl32_EventType_type: Property = Property(name="type", type=StringType)
jpdl32_EventType.attributes={jpdl32_EventType_actionElements, jpdl32_EventType_type}

# jpdl32_DecisionType class attributes and methods
jpdl32_DecisionType_group: Property = Property(name="group", type=StringType)
jpdl32_DecisionType_description: Property = Property(name="description", type=StringType)
jpdl32_DecisionType_async: Property = Property(name="async", type=StringType)
jpdl32_DecisionType_expression: Property = Property(name="expression", type=StringType)
jpdl32_DecisionType_name: Property = Property(name="name", type=StringType)
jpdl32_DecisionType.attributes={jpdl32_DecisionType_group, jpdl32_DecisionType_description, jpdl32_DecisionType_name, jpdl32_DecisionType_expression, jpdl32_DecisionType_async}

# jpdl32_ExceptionHandlerType class attributes and methods
jpdl32_ExceptionHandlerType_exceptionClass: Property = Property(name="exceptionClass", type=StringType)
jpdl32_ExceptionHandlerType_group: Property = Property(name="group", type=StringType)
jpdl32_ExceptionHandlerType.attributes={jpdl32_ExceptionHandlerType_group, jpdl32_ExceptionHandlerType_exceptionClass}

# jpdl32_TransitionType class attributes and methods
jpdl32_TransitionType_group: Property = Property(name="group", type=StringType)
jpdl32_TransitionType_description: Property = Property(name="description", type=StringType)
jpdl32_TransitionType_to: Property = Property(name="to", type=StringType)
jpdl32_TransitionType_name: Property = Property(name="name", type=StringType)
jpdl32_TransitionType.attributes={jpdl32_TransitionType_name, jpdl32_TransitionType_group, jpdl32_TransitionType_to, jpdl32_TransitionType_description}

# jpdl32_EStringToStringMapEntry class attributes and methods

# jpdl32_DocumentRoot class attributes and methods
jpdl32_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
jpdl32_DocumentRoot_description: Property = Property(name="description", type=StringType)
jpdl32_DocumentRoot_recipients: Property = Property(name="recipients", type=StringType)
jpdl32_DocumentRoot_subject: Property = Property(name="subject", type=StringType)
jpdl32_DocumentRoot_template: Property = Property(name="template", type=StringType)
jpdl32_DocumentRoot_text: Property = Property(name="text", type=StringType)
jpdl32_DocumentRoot_to: Property = Property(name="to", type=StringType)
jpdl32_DocumentRoot.attributes={jpdl32_DocumentRoot_to, jpdl32_DocumentRoot_subject, jpdl32_DocumentRoot_description, jpdl32_DocumentRoot_mixed, jpdl32_DocumentRoot_recipients, jpdl32_DocumentRoot_text, jpdl32_DocumentRoot_template}

# jpdl32_EndStateType class attributes and methods
jpdl32_EndStateType_group: Property = Property(name="group", type=StringType)
jpdl32_EndStateType_description: Property = Property(name="description", type=StringType)
jpdl32_EndStateType_endCompleteProcess: Property = Property(name="endCompleteProcess", type=StringType)
jpdl32_EndStateType_name: Property = Property(name="name", type=StringType)
jpdl32_EndStateType.attributes={jpdl32_EndStateType_name, jpdl32_EndStateType_group, jpdl32_EndStateType_description, jpdl32_EndStateType_endCompleteProcess}

# jpdl32_MailNodeType class attributes and methods
jpdl32_MailNodeType_group: Property = Property(name="group", type=StringType)
jpdl32_MailNodeType_subject: Property = Property(name="subject", type=StringType)
jpdl32_MailNodeType_text: Property = Property(name="text", type=StringType)
jpdl32_MailNodeType_description: Property = Property(name="description", type=StringType)
jpdl32_MailNodeType_actors: Property = Property(name="actors", type=StringType)
jpdl32_MailNodeType_async: Property = Property(name="async", type=StringType)
jpdl32_MailNodeType_name: Property = Property(name="name", type=StringType)
jpdl32_MailNodeType_subject1: Property = Property(name="subject1", type=StringType)
jpdl32_MailNodeType_template: Property = Property(name="template", type=StringType)
jpdl32_MailNodeType_text1: Property = Property(name="text1", type=StringType)
jpdl32_MailNodeType_to: Property = Property(name="to", type=StringType)
jpdl32_MailNodeType.attributes={jpdl32_MailNodeType_async, jpdl32_MailNodeType_name, jpdl32_MailNodeType_text, jpdl32_MailNodeType_actors, jpdl32_MailNodeType_description, jpdl32_MailNodeType_subject1, jpdl32_MailNodeType_subject, jpdl32_MailNodeType_text1, jpdl32_MailNodeType_to, jpdl32_MailNodeType_template, jpdl32_MailNodeType_group}

# jpdl32_NodeType class attributes and methods
jpdl32_NodeType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl32_NodeType_description: Property = Property(name="description", type=StringType)
jpdl32_NodeType_async: Property = Property(name="async", type=StringType)
jpdl32_NodeType_name: Property = Property(name="name", type=StringType)
jpdl32_NodeType.attributes={jpdl32_NodeType_description, jpdl32_NodeType_nodeContentElements, jpdl32_NodeType_async, jpdl32_NodeType_name}

# jpdl32_ForkType class attributes and methods
jpdl32_ForkType_group: Property = Property(name="group", type=StringType)
jpdl32_ForkType_description: Property = Property(name="description", type=StringType)
jpdl32_ForkType_async: Property = Property(name="async", type=StringType)
jpdl32_ForkType_name: Property = Property(name="name", type=StringType)
jpdl32_ForkType.attributes={jpdl32_ForkType_async, jpdl32_ForkType_name, jpdl32_ForkType_group, jpdl32_ForkType_description}

# jpdl32_JoinType class attributes and methods
jpdl32_JoinType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl32_JoinType_description: Property = Property(name="description", type=StringType)
jpdl32_JoinType_name: Property = Property(name="name", type=StringType)
jpdl32_JoinType_async: Property = Property(name="async", type=StringType)
jpdl32_JoinType.attributes={jpdl32_JoinType_name, jpdl32_JoinType_nodeContentElements, jpdl32_JoinType_async, jpdl32_JoinType_description}

# jpdl32_MailType class attributes and methods
jpdl32_MailType_group: Property = Property(name="group", type=StringType)
jpdl32_MailType_subject: Property = Property(name="subject", type=StringType)
jpdl32_MailType_subject1: Property = Property(name="subject1", type=StringType)
jpdl32_MailType_template: Property = Property(name="template", type=StringType)
jpdl32_MailType_text1: Property = Property(name="text1", type=StringType)
jpdl32_MailType_to: Property = Property(name="to", type=StringType)
jpdl32_MailType_text: Property = Property(name="text", type=StringType)
jpdl32_MailType_actors: Property = Property(name="actors", type=StringType)
jpdl32_MailType_async: Property = Property(name="async", type=StringType)
jpdl32_MailType_name: Property = Property(name="name", type=StringType)
jpdl32_MailType.attributes={jpdl32_MailType_template, jpdl32_MailType_async, jpdl32_MailType_actors, jpdl32_MailType_to, jpdl32_MailType_subject, jpdl32_MailType_subject1, jpdl32_MailType_text1, jpdl32_MailType_text, jpdl32_MailType_group, jpdl32_MailType_name}

# jpdl32_ProcessDefinitionType class attributes and methods
jpdl32_ProcessDefinitionType_group: Property = Property(name="group", type=StringType)
jpdl32_ProcessDefinitionType_description: Property = Property(name="description", type=StringType)
jpdl32_ProcessDefinitionType_name: Property = Property(name="name", type=StringType)
jpdl32_ProcessDefinitionType.attributes={jpdl32_ProcessDefinitionType_name, jpdl32_ProcessDefinitionType_group, jpdl32_ProcessDefinitionType_description}

# jpdl32_ProcessStateType class attributes and methods
jpdl32_ProcessStateType_group: Property = Property(name="group", type=StringType)
jpdl32_ProcessStateType_description: Property = Property(name="description", type=StringType)
jpdl32_ProcessStateType_async: Property = Property(name="async", type=StringType)
jpdl32_ProcessStateType_binding: Property = Property(name="binding", type=StringType)
jpdl32_ProcessStateType_name: Property = Property(name="name", type=StringType)
jpdl32_ProcessStateType.attributes={jpdl32_ProcessStateType_async, jpdl32_ProcessStateType_group, jpdl32_ProcessStateType_name, jpdl32_ProcessStateType_description, jpdl32_ProcessStateType_binding}

# jpdl32_SuperStateType class attributes and methods
jpdl32_SuperStateType_group: Property = Property(name="group", type=StringType)
jpdl32_SuperStateType_description: Property = Property(name="description", type=StringType)
jpdl32_SuperStateType_async: Property = Property(name="async", type=StringType)
jpdl32_SuperStateType_name: Property = Property(name="name", type=StringType)
jpdl32_SuperStateType.attributes={jpdl32_SuperStateType_group, jpdl32_SuperStateType_name, jpdl32_SuperStateType_async, jpdl32_SuperStateType_description}

# jpdl32_StartStateType class attributes and methods
jpdl32_StartStateType_group: Property = Property(name="group", type=StringType)
jpdl32_StartStateType_description: Property = Property(name="description", type=StringType)
jpdl32_StartStateType_name: Property = Property(name="name", type=StringType)
jpdl32_StartStateType.attributes={jpdl32_StartStateType_name, jpdl32_StartStateType_group, jpdl32_StartStateType_description}

# jpdl32_StateType class attributes and methods
jpdl32_StateType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl32_StateType_description: Property = Property(name="description", type=StringType)
jpdl32_StateType_async: Property = Property(name="async", type=StringType)
jpdl32_StateType_name: Property = Property(name="name", type=StringType)
jpdl32_StateType.attributes={jpdl32_StateType_description, jpdl32_StateType_name, jpdl32_StateType_nodeContentElements, jpdl32_StateType_async}

# jpdl32_TaskNodeType class attributes and methods
jpdl32_TaskNodeType_group: Property = Property(name="group", type=StringType)
jpdl32_TaskNodeType_description: Property = Property(name="description", type=StringType)
jpdl32_TaskNodeType_endTasks: Property = Property(name="endTasks", type=StringType)
jpdl32_TaskNodeType_name: Property = Property(name="name", type=StringType)
jpdl32_TaskNodeType_signal: Property = Property(name="signal", type=StringType)
jpdl32_TaskNodeType_async: Property = Property(name="async", type=StringType)
jpdl32_TaskNodeType_createTasks: Property = Property(name="createTasks", type=StringType)
jpdl32_TaskNodeType.attributes={jpdl32_TaskNodeType_name, jpdl32_TaskNodeType_createTasks, jpdl32_TaskNodeType_group, jpdl32_TaskNodeType_signal, jpdl32_TaskNodeType_async, jpdl32_TaskNodeType_endTasks, jpdl32_TaskNodeType_description}

# jpdl32_SwimlaneType class attributes and methods
jpdl32_SwimlaneType_name: Property = Property(name="name", type=StringType)
jpdl32_SwimlaneType.attributes={jpdl32_SwimlaneType_name}

# jpdl32_TaskType class attributes and methods
jpdl32_TaskType_group: Property = Property(name="group", type=StringType)
jpdl32_TaskType_description: Property = Property(name="description", type=StringType)
jpdl32_TaskType_duedate: Property = Property(name="duedate", type=StringType)
jpdl32_TaskType_name: Property = Property(name="name", type=StringType)
jpdl32_TaskType_notify: Property = Property(name="notify", type=StringType)
jpdl32_TaskType_priority: Property = Property(name="priority", type=StringType)
jpdl32_TaskType_blocking: Property = Property(name="blocking", type=StringType)
jpdl32_TaskType_description1: Property = Property(name="description1", type=StringType)
jpdl32_TaskType_signalling: Property = Property(name="signalling", type=StringType)
jpdl32_TaskType_swimlane: Property = Property(name="swimlane", type=StringType)
jpdl32_TaskType.attributes={jpdl32_TaskType_signalling, jpdl32_TaskType_description, jpdl32_TaskType_swimlane, jpdl32_TaskType_blocking, jpdl32_TaskType_name, jpdl32_TaskType_description1, jpdl32_TaskType_group, jpdl32_TaskType_notify, jpdl32_TaskType_priority, jpdl32_TaskType_duedate}

# jpdl32_TimerType class attributes and methods
jpdl32_TimerType_name: Property = Property(name="name", type=StringType)
jpdl32_TimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl32_TimerType_transition: Property = Property(name="transition", type=StringType)
jpdl32_TimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl32_TimerType.attributes={jpdl32_TimerType_name, jpdl32_TimerType_transition, jpdl32_TimerType_duedate, jpdl32_TimerType_repeat}

# jpdl32_VariableType class attributes and methods
jpdl32_VariableType_any: Property = Property(name="any", type=StringType)
jpdl32_VariableType_access: Property = Property(name="access", type=StringType)
jpdl32_VariableType_mappedName: Property = Property(name="mappedName", type=StringType)
jpdl32_VariableType_name: Property = Property(name="name", type=StringType)
jpdl32_VariableType.attributes={jpdl32_VariableType_access, jpdl32_VariableType_any, jpdl32_VariableType_name, jpdl32_VariableType_mappedName}

# jpdl32_SubProcessType class attributes and methods
jpdl32_SubProcessType_binding: Property = Property(name="binding", type=StringType)
jpdl32_SubProcessType_name: Property = Property(name="name", type=StringType)
jpdl32_SubProcessType_version: Property = Property(name="version", type=StringType)
jpdl32_SubProcessType.attributes={jpdl32_SubProcessType_name, jpdl32_SubProcessType_binding, jpdl32_SubProcessType_version}

# jpdl32_ReminderType class attributes and methods
jpdl32_ReminderType_duedate: Property = Property(name="duedate", type=StringType)
jpdl32_ReminderType_repeat: Property = Property(name="repeat", type=StringType)
jpdl32_ReminderType.attributes={jpdl32_ReminderType_repeat, jpdl32_ReminderType_duedate}

# Relationships
script1: BinaryAssociation = BinaryAssociation(
    name="script1",
    ends={
        Property(name="jpdl32_ScriptType", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_CreateTimerType2", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action0: BinaryAssociation = BinaryAssociation(
    name="action0",
    ends={
        Property(name="jpdl32_ActionType", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_CreateTimerType", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
handler3: BinaryAssociation = BinaryAssociation(
    name="handler3",
    ends={
        Property(name="jpdl32_Delegation", type=jpdl32_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DecisionType", type=jpdl32_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event4: BinaryAssociation = BinaryAssociation(
    name="event4",
    ends={
        Property(name="jpdl32_EventType", type=jpdl32_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DecisionType5", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler6: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler6",
    ends={
        Property(name="jpdl32_ExceptionHandlerType", type=jpdl32_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DecisionType7", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="jpdl32_TransitionType", type=jpdl32_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DecisionType9", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap10: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap10",
    ends={
        Property(name="jpdl32_EStringToStringMapEntry", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot", type=jpdl32_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller21: BinaryAssociation = BinaryAssociation(
    name="controller21",
    ends={
        Property(name="jpdl32_Delegation23", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot22", type=jpdl32_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer24: BinaryAssociation = BinaryAssociation(
    name="createTimer24",
    ends={
        Property(name="jpdl32_CreateTimerType26", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot25", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation11: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation11",
    ends={
        Property(name="jpdl32_EStringToStringMapEntry13", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot12", type=jpdl32_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action14: BinaryAssociation = BinaryAssociation(
    name="action14",
    ends={
        Property(name="jpdl32_ActionType16", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot15", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment17: BinaryAssociation = BinaryAssociation(
    name="assignment17",
    ends={
        Property(name="jpdl32_AssignmentType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot18", type=jpdl32_AssignmentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer19: BinaryAssociation = BinaryAssociation(
    name="cancelTimer19",
    ends={
        Property(name="jpdl32_CancelTimerType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot20", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="jpdl32_EventType34", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot33", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler35: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler35",
    ends={
        Property(name="jpdl32_ExceptionHandlerType37", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot36", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision27: BinaryAssociation = BinaryAssociation(
    name="decision27",
    ends={
        Property(name="jpdl32_DecisionType29", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot28", type=jpdl32_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState30: BinaryAssociation = BinaryAssociation(
    name="endState30",
    ends={
        Property(name="jpdl32_EndStateType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot31", type=jpdl32_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailNode44: BinaryAssociation = BinaryAssociation(
    name="mailNode44",
    ends={
        Property(name="jpdl32_MailNodeType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot45", type=jpdl32_MailNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork38: BinaryAssociation = BinaryAssociation(
    name="fork38",
    ends={
        Property(name="jpdl32_ForkType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot39", type=jpdl32_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join40: BinaryAssociation = BinaryAssociation(
    name="join40",
    ends={
        Property(name="jpdl32_JoinType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot41", type=jpdl32_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mail42: BinaryAssociation = BinaryAssociation(
    name="mail42",
    ends={
        Property(name="jpdl32_MailType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot43", type=jpdl32_MailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script52: BinaryAssociation = BinaryAssociation(
    name="script52",
    ends={
        Property(name="jpdl32_ScriptType54", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot53", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node46: BinaryAssociation = BinaryAssociation(
    name="node46",
    ends={
        Property(name="jpdl32_NodeType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot47", type=jpdl32_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processDefinition48: BinaryAssociation = BinaryAssociation(
    name="processDefinition48",
    ends={
        Property(name="jpdl32_ProcessDefinitionType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot49", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState50: BinaryAssociation = BinaryAssociation(
    name="processState50",
    ends={
        Property(name="jpdl32_ProcessStateType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot51", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState59: BinaryAssociation = BinaryAssociation(
    name="superState59",
    ends={
        Property(name="jpdl32_SuperStateType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot60", type=jpdl32_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState55: BinaryAssociation = BinaryAssociation(
    name="startState55",
    ends={
        Property(name="jpdl32_StartStateType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot56", type=jpdl32_StartStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state57: BinaryAssociation = BinaryAssociation(
    name="state57",
    ends={
        Property(name="jpdl32_StateType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot58", type=jpdl32_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode65: BinaryAssociation = BinaryAssociation(
    name="taskNode65",
    ends={
        Property(name="jpdl32_TaskNodeType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot66", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swimlane61: BinaryAssociation = BinaryAssociation(
    name="swimlane61",
    ends={
        Property(name="jpdl32_SwimlaneType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot62", type=jpdl32_SwimlaneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task63: BinaryAssociation = BinaryAssociation(
    name="task63",
    ends={
        Property(name="jpdl32_TaskType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot64", type=jpdl32_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition69: BinaryAssociation = BinaryAssociation(
    name="transition69",
    ends={
        Property(name="jpdl32_TransitionType71", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot70", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer67: BinaryAssociation = BinaryAssociation(
    name="timer67",
    ends={
        Property(name="jpdl32_TimerType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot68", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event74: BinaryAssociation = BinaryAssociation(
    name="event74",
    ends={
        Property(name="jpdl32_EventType76", type=jpdl32_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EndStateType75", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable72: BinaryAssociation = BinaryAssociation(
    name="variable72",
    ends={
        Property(name="jpdl32_VariableType", type=jpdl32_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_DocumentRoot73", type=jpdl32_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action80: BinaryAssociation = BinaryAssociation(
    name="action80",
    ends={
        Property(name="jpdl32_ActionType82", type=jpdl32_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EventType81", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler77: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler77",
    ends={
        Property(name="jpdl32_ExceptionHandlerType79", type=jpdl32_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EndStateType78", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mail92: BinaryAssociation = BinaryAssociation(
    name="mail92",
    ends={
        Property(name="jpdl32_MailType94", type=jpdl32_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EventType93", type=jpdl32_MailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script83: BinaryAssociation = BinaryAssociation(
    name="script83",
    ends={
        Property(name="jpdl32_ScriptType85", type=jpdl32_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EventType84", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer86: BinaryAssociation = BinaryAssociation(
    name="createTimer86",
    ends={
        Property(name="jpdl32_CreateTimerType88", type=jpdl32_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EventType87", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer89: BinaryAssociation = BinaryAssociation(
    name="cancelTimer89",
    ends={
        Property(name="jpdl32_CancelTimerType91", type=jpdl32_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_EventType90", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script98: BinaryAssociation = BinaryAssociation(
    name="script98",
    ends={
        Property(name="jpdl32_ScriptType100", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ExceptionHandlerType99", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action95: BinaryAssociation = BinaryAssociation(
    name="action95",
    ends={
        Property(name="jpdl32_ActionType97", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ExceptionHandlerType96", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event104: BinaryAssociation = BinaryAssociation(
    name="event104",
    ends={
        Property(name="jpdl32_EventType106", type=jpdl32_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ForkType105", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script101: BinaryAssociation = BinaryAssociation(
    name="script101",
    ends={
        Property(name="jpdl32_ScriptType103", type=jpdl32_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ForkType102", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler107: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler107",
    ends={
        Property(name="jpdl32_ExceptionHandlerType109", type=jpdl32_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ForkType108", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer110: BinaryAssociation = BinaryAssociation(
    name="timer110",
    ends={
        Property(name="jpdl32_TimerType112", type=jpdl32_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ForkType111", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition113: BinaryAssociation = BinaryAssociation(
    name="transition113",
    ends={
        Property(name="jpdl32_TransitionType115", type=jpdl32_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ForkType114", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler119: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler119",
    ends={
        Property(name="jpdl32_ExceptionHandlerType121", type=jpdl32_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_JoinType120", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event116: BinaryAssociation = BinaryAssociation(
    name="event116",
    ends={
        Property(name="jpdl32_EventType118", type=jpdl32_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_JoinType117", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer122: BinaryAssociation = BinaryAssociation(
    name="timer122",
    ends={
        Property(name="jpdl32_TimerType124", type=jpdl32_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_JoinType123", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition125: BinaryAssociation = BinaryAssociation(
    name="transition125",
    ends={
        Property(name="jpdl32_TransitionType127", type=jpdl32_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_JoinType126", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event128: BinaryAssociation = BinaryAssociation(
    name="event128",
    ends={
        Property(name="jpdl32_EventType130", type=jpdl32_MailNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_MailNodeType129", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler131: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler131",
    ends={
        Property(name="jpdl32_ExceptionHandlerType133", type=jpdl32_MailNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_MailNodeType132", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer134: BinaryAssociation = BinaryAssociation(
    name="timer134",
    ends={
        Property(name="jpdl32_TimerType136", type=jpdl32_MailNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_MailNodeType135", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition137: BinaryAssociation = BinaryAssociation(
    name="transition137",
    ends={
        Property(name="jpdl32_TransitionType139", type=jpdl32_MailNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_MailNodeType138", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer146: BinaryAssociation = BinaryAssociation(
    name="createTimer146",
    ends={
        Property(name="jpdl32_CreateTimerType148", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType147", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cancelTimer149: BinaryAssociation = BinaryAssociation(
    name="cancelTimer149",
    ends={
        Property(name="jpdl32_CancelTimerType151", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType150", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action140: BinaryAssociation = BinaryAssociation(
    name="action140",
    ends={
        Property(name="jpdl32_ActionType142", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType141", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script143: BinaryAssociation = BinaryAssociation(
    name="script143",
    ends={
        Property(name="jpdl32_ScriptType145", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType144", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event155: BinaryAssociation = BinaryAssociation(
    name="event155",
    ends={
        Property(name="jpdl32_EventType157", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType156", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler158: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler158",
    ends={
        Property(name="jpdl32_ExceptionHandlerType160", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType159", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mail152: BinaryAssociation = BinaryAssociation(
    name="mail152",
    ends={
        Property(name="jpdl32_MailType154", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType153", type=jpdl32_MailType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timer161: BinaryAssociation = BinaryAssociation(
    name="timer161",
    ends={
        Property(name="jpdl32_TimerType163", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType162", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition164: BinaryAssociation = BinaryAssociation(
    name="transition164",
    ends={
        Property(name="jpdl32_TransitionType166", type=jpdl32_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_NodeType165", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node173: BinaryAssociation = BinaryAssociation(
    name="node173",
    ends={
        Property(name="jpdl32_NodeType175", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType174", type=jpdl32_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state176: BinaryAssociation = BinaryAssociation(
    name="state176",
    ends={
        Property(name="jpdl32_StateType178", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType177", type=jpdl32_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swimlane167: BinaryAssociation = BinaryAssociation(
    name="swimlane167",
    ends={
        Property(name="jpdl32_SwimlaneType169", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType168", type=jpdl32_SwimlaneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState170: BinaryAssociation = BinaryAssociation(
    name="startState170",
    ends={
        Property(name="jpdl32_StartStateType172", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType171", type=jpdl32_StartStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState185: BinaryAssociation = BinaryAssociation(
    name="processState185",
    ends={
        Property(name="jpdl32_ProcessStateType187", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType186", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork188: BinaryAssociation = BinaryAssociation(
    name="fork188",
    ends={
        Property(name="jpdl32_ForkType190", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType189", type=jpdl32_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode179: BinaryAssociation = BinaryAssociation(
    name="taskNode179",
    ends={
        Property(name="jpdl32_TaskNodeType181", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType180", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState182: BinaryAssociation = BinaryAssociation(
    name="superState182",
    ends={
        Property(name="jpdl32_SuperStateType184", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType183", type=jpdl32_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState197: BinaryAssociation = BinaryAssociation(
    name="endState197",
    ends={
        Property(name="jpdl32_EndStateType199", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType198", type=jpdl32_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailNode200: BinaryAssociation = BinaryAssociation(
    name="mailNode200",
    ends={
        Property(name="jpdl32_MailNodeType202", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType201", type=jpdl32_MailNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join191: BinaryAssociation = BinaryAssociation(
    name="join191",
    ends={
        Property(name="jpdl32_JoinType193", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType192", type=jpdl32_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision194: BinaryAssociation = BinaryAssociation(
    name="decision194",
    ends={
        Property(name="jpdl32_DecisionType196", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType195", type=jpdl32_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer209: BinaryAssociation = BinaryAssociation(
    name="createTimer209",
    ends={
        Property(name="jpdl32_CreateTimerType211", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType210", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action203: BinaryAssociation = BinaryAssociation(
    name="action203",
    ends={
        Property(name="jpdl32_ActionType205", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType204", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script206: BinaryAssociation = BinaryAssociation(
    name="script206",
    ends={
        Property(name="jpdl32_ScriptType208", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType207", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event218: BinaryAssociation = BinaryAssociation(
    name="event218",
    ends={
        Property(name="jpdl32_ProcessDefinitionType219", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="jpdl32_EventType220", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1))
    }
)
exceptionHandler221: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler221",
    ends={
        Property(name="jpdl32_ExceptionHandlerType223", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType222", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer212: BinaryAssociation = BinaryAssociation(
    name="cancelTimer212",
    ends={
        Property(name="jpdl32_CancelTimerType214", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType213", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mail215: BinaryAssociation = BinaryAssociation(
    name="mail215",
    ends={
        Property(name="jpdl32_MailType217", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType216", type=jpdl32_MailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess227: BinaryAssociation = BinaryAssociation(
    name="subProcess227",
    ends={
        Property(name="jpdl32_SubProcessType", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType228", type=jpdl32_SubProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task224: BinaryAssociation = BinaryAssociation(
    name="task224",
    ends={
        Property(name="jpdl32_TaskType226", type=jpdl32_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessDefinitionType225", type=jpdl32_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler235: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler235",
    ends={
        Property(name="jpdl32_ExceptionHandlerType237", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType236", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable229: BinaryAssociation = BinaryAssociation(
    name="variable229",
    ends={
        Property(name="jpdl32_VariableType231", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType230", type=jpdl32_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event232: BinaryAssociation = BinaryAssociation(
    name="event232",
    ends={
        Property(name="jpdl32_EventType234", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType233", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer238: BinaryAssociation = BinaryAssociation(
    name="timer238",
    ends={
        Property(name="jpdl32_TimerType240", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType239", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition241: BinaryAssociation = BinaryAssociation(
    name="transition241",
    ends={
        Property(name="jpdl32_TransitionType243", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_ProcessStateType242", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler253: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler253",
    ends={
        Property(name="jpdl32_ExceptionHandlerType255", type=jpdl32_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StartStateType254", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task244: BinaryAssociation = BinaryAssociation(
    name="task244",
    ends={
        Property(name="jpdl32_TaskType246", type=jpdl32_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StartStateType245", type=jpdl32_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition247: BinaryAssociation = BinaryAssociation(
    name="transition247",
    ends={
        Property(name="jpdl32_TransitionType249", type=jpdl32_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StartStateType248", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event250: BinaryAssociation = BinaryAssociation(
    name="event250",
    ends={
        Property(name="jpdl32_EventType252", type=jpdl32_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StartStateType251", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event256: BinaryAssociation = BinaryAssociation(
    name="event256",
    ends={
        Property(name="jpdl32_EventType258", type=jpdl32_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StateType257", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler259: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler259",
    ends={
        Property(name="jpdl32_ExceptionHandlerType261", type=jpdl32_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StateType260", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer262: BinaryAssociation = BinaryAssociation(
    name="timer262",
    ends={
        Property(name="jpdl32_TimerType264", type=jpdl32_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StateType263", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition265: BinaryAssociation = BinaryAssociation(
    name="transition265",
    ends={
        Property(name="jpdl32_TransitionType267", type=jpdl32_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_StateType266", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node268: BinaryAssociation = BinaryAssociation(
    name="node268",
    ends={
        Property(name="jpdl32_NodeType270", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType269", type=jpdl32_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state271: BinaryAssociation = BinaryAssociation(
    name="state271",
    ends={
        Property(name="jpdl32_StateType273", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType272", type=jpdl32_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState280: BinaryAssociation = BinaryAssociation(
    name="processState280",
    ends={
        Property(name="jpdl32_ProcessStateType282", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType281", type=jpdl32_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode274: BinaryAssociation = BinaryAssociation(
    name="taskNode274",
    ends={
        Property(name="jpdl32_TaskNodeType276", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType275", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState278: BinaryAssociation = BinaryAssociation(
    name="superState278",
    ends={
        Property(name="jpdl32_SuperStateType279", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType277", type=jpdl32_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState292: BinaryAssociation = BinaryAssociation(
    name="endState292",
    ends={
        Property(name="jpdl32_EndStateType294", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType293", type=jpdl32_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailNode295: BinaryAssociation = BinaryAssociation(
    name="mailNode295",
    ends={
        Property(name="jpdl32_MailNodeType297", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType296", type=jpdl32_MailNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork283: BinaryAssociation = BinaryAssociation(
    name="fork283",
    ends={
        Property(name="jpdl32_ForkType285", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType284", type=jpdl32_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join286: BinaryAssociation = BinaryAssociation(
    name="join286",
    ends={
        Property(name="jpdl32_JoinType288", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType287", type=jpdl32_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision289: BinaryAssociation = BinaryAssociation(
    name="decision289",
    ends={
        Property(name="jpdl32_DecisionType291", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType290", type=jpdl32_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler301: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler301",
    ends={
        Property(name="jpdl32_ExceptionHandlerType303", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType302", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer304: BinaryAssociation = BinaryAssociation(
    name="timer304",
    ends={
        Property(name="jpdl32_TimerType306", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType305", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event298: BinaryAssociation = BinaryAssociation(
    name="event298",
    ends={
        Property(name="jpdl32_EventType300", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType299", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment310: BinaryAssociation = BinaryAssociation(
    name="assignment310",
    ends={
        Property(name="jpdl32_AssignmentType312", type=jpdl32_SwimlaneType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SwimlaneType311", type=jpdl32_AssignmentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition307: BinaryAssociation = BinaryAssociation(
    name="transition307",
    ends={
        Property(name="jpdl32_TransitionType309", type=jpdl32_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_SuperStateType308", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler319: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler319",
    ends={
        Property(name="jpdl32_ExceptionHandlerType321", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskNodeType320", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer322: BinaryAssociation = BinaryAssociation(
    name="timer322",
    ends={
        Property(name="jpdl32_TimerType324", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskNodeType323", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task313: BinaryAssociation = BinaryAssociation(
    name="task313",
    ends={
        Property(name="jpdl32_TaskType315", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskNodeType314", type=jpdl32_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event316: BinaryAssociation = BinaryAssociation(
    name="event316",
    ends={
        Property(name="jpdl32_EventType318", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskNodeType317", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition325: BinaryAssociation = BinaryAssociation(
    name="transition325",
    ends={
        Property(name="jpdl32_TransitionType327", type=jpdl32_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskNodeType326", type=jpdl32_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event334: BinaryAssociation = BinaryAssociation(
    name="event334",
    ends={
        Property(name="jpdl32_EventType336", type=jpdl32_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskType335", type=jpdl32_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer337: BinaryAssociation = BinaryAssociation(
    name="timer337",
    ends={
        Property(name="jpdl32_TimerType339", type=jpdl32_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskType338", type=jpdl32_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment328: BinaryAssociation = BinaryAssociation(
    name="assignment328",
    ends={
        Property(name="jpdl32_AssignmentType330", type=jpdl32_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskType329", type=jpdl32_AssignmentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller331: BinaryAssociation = BinaryAssociation(
    name="controller331",
    ends={
        Property(name="jpdl32_Delegation333", type=jpdl32_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskType332", type=jpdl32_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reminder340: BinaryAssociation = BinaryAssociation(
    name="reminder340",
    ends={
        Property(name="jpdl32_ReminderType", type=jpdl32_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TaskType341", type=jpdl32_ReminderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer348: BinaryAssociation = BinaryAssociation(
    name="createTimer348",
    ends={
        Property(name="jpdl32_CreateTimerType350", type=jpdl32_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TimerType349", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cancelTimer351: BinaryAssociation = BinaryAssociation(
    name="cancelTimer351",
    ends={
        Property(name="jpdl32_CancelTimerType353", type=jpdl32_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TimerType352", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mail354: BinaryAssociation = BinaryAssociation(
    name="mail354",
    ends={
        Property(name="jpdl32_MailType356", type=jpdl32_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TimerType355", type=jpdl32_MailType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action342: BinaryAssociation = BinaryAssociation(
    name="action342",
    ends={
        Property(name="jpdl32_ActionType344", type=jpdl32_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TimerType343", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script345: BinaryAssociation = BinaryAssociation(
    name="script345",
    ends={
        Property(name="jpdl32_ScriptType347", type=jpdl32_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TimerType346", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition357: BinaryAssociation = BinaryAssociation(
    name="condition357",
    ends={
        Property(name="jpdl32_ConditionType", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType358", type=jpdl32_ConditionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action359: BinaryAssociation = BinaryAssociation(
    name="action359",
    ends={
        Property(name="jpdl32_ActionType361", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType360", type=jpdl32_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer368: BinaryAssociation = BinaryAssociation(
    name="cancelTimer368",
    ends={
        Property(name="jpdl32_CancelTimerType370", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType369", type=jpdl32_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mail371: BinaryAssociation = BinaryAssociation(
    name="mail371",
    ends={
        Property(name="jpdl32_MailType373", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType372", type=jpdl32_MailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script362: BinaryAssociation = BinaryAssociation(
    name="script362",
    ends={
        Property(name="jpdl32_ScriptType364", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType363", type=jpdl32_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer365: BinaryAssociation = BinaryAssociation(
    name="createTimer365",
    ends={
        Property(name="jpdl32_CreateTimerType367", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType366", type=jpdl32_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler374: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler374",
    ends={
        Property(name="jpdl32_ExceptionHandlerType376", type=jpdl32_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl32_TransitionType375", type=jpdl32_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jpdl32_AssignmentType_Delegation = Generalization(general=Delegation, specific=jpdl32_AssignmentType)

# Domain Model
domain_model = DomainModel(
    name="jpdl32",
    types={jpdl32_ActionType, jpdl32_AssignmentType, Delegation, jpdl32_CancelTimerType, jpdl32_ConditionType, jpdl32_ScriptType, jpdl32_CreateTimerType, jpdl32_Delegation, jpdl32_EventType, jpdl32_DecisionType, jpdl32_ExceptionHandlerType, jpdl32_TransitionType, jpdl32_EStringToStringMapEntry, jpdl32_DocumentRoot, jpdl32_EndStateType, jpdl32_MailNodeType, jpdl32_NodeType, jpdl32_ForkType, jpdl32_JoinType, jpdl32_MailType, jpdl32_ProcessDefinitionType, jpdl32_ProcessStateType, jpdl32_SuperStateType, jpdl32_StartStateType, jpdl32_StateType, jpdl32_TaskNodeType, jpdl32_SwimlaneType, jpdl32_TaskType, jpdl32_TimerType, jpdl32_VariableType, jpdl32_SubProcessType, jpdl32_ReminderType, BindingType, BooleanType, ConfigType, PriorityTypeMember0, SignalType, TypeTypeMember1},
    associations={script1, action0, handler3, event4, exceptionHandler6, transition8, xMLNSPrefixMap10, controller21, createTimer24, xSISchemaLocation11, action14, assignment17, cancelTimer19, event32, exceptionHandler35, decision27, endState30, mailNode44, fork38, join40, mail42, script52, node46, processDefinition48, processState50, superState59, startState55, state57, taskNode65, swimlane61, task63, transition69, timer67, event74, variable72, action80, exceptionHandler77, mail92, script83, createTimer86, cancelTimer89, script98, action95, event104, script101, exceptionHandler107, timer110, transition113, exceptionHandler119, event116, timer122, transition125, event128, exceptionHandler131, timer134, transition137, createTimer146, cancelTimer149, action140, script143, event155, exceptionHandler158, mail152, timer161, transition164, node173, state176, swimlane167, startState170, processState185, fork188, taskNode179, superState182, endState197, mailNode200, join191, decision194, createTimer209, action203, script206, event218, exceptionHandler221, cancelTimer212, mail215, subProcess227, task224, exceptionHandler235, variable229, event232, timer238, transition241, exceptionHandler253, task244, transition247, event250, event256, exceptionHandler259, timer262, transition265, node268, state271, processState280, taskNode274, superState278, endState292, mailNode295, fork283, join286, decision289, exceptionHandler301, timer304, event298, assignment310, transition307, exceptionHandler319, timer322, task313, event316, transition325, event334, timer337, assignment328, controller331, reminder340, createTimer348, cancelTimer351, mail354, action342, script345, condition357, action359, cancelTimer368, mail371, script362, createTimer365, exceptionHandler374},
    generalizations={gen_jpdl32_AssignmentType_Delegation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)