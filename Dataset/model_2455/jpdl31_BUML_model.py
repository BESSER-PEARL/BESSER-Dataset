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
            EnumerationLiteral(name="taskEnd"),
			EnumerationLiteral(name="beforeSignal"),
			EnumerationLiteral(name="afterSignal"),
			EnumerationLiteral(name="superstateEnter"),
			EnumerationLiteral(name="superstateLeave"),
			EnumerationLiteral(name="timerCreate"),
			EnumerationLiteral(name="subprocessCreated"),
			EnumerationLiteral(name="subprocessEnd"),
			EnumerationLiteral(name="nodeEnter"),
			EnumerationLiteral(name="nodeLeave"),
			EnumerationLiteral(name="processStart"),
			EnumerationLiteral(name="processEnd"),
			EnumerationLiteral(name="taskCreate"),
			EnumerationLiteral(name="taskAssign"),
			EnumerationLiteral(name="taskStart")
    }
)

ArtefactType: Enumeration = Enumeration(
    name="ArtefactType",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="inoutput")
    }
)

MetricType: Enumeration = Enumeration(
    name="MetricType",
    literals={
            EnumerationLiteral(name="time"),
			EnumerationLiteral(name="collectedData"),
			EnumerationLiteral(name="quest"),
			EnumerationLiteral(name="artefact")
    }
)

RelationOperator: Enumeration = Enumeration(
    name="RelationOperator",
    literals={
            EnumerationLiteral(name="different"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="morethan"),
			EnumerationLiteral(name="lessthan"),
			EnumerationLiteral(name="moreequalthan"),
			EnumerationLiteral(name="lessequalthan")
    }
)

AnswerType: Enumeration = Enumeration(
    name="AnswerType",
    literals={
            EnumerationLiteral(name="comboBox"),
			EnumerationLiteral(name="checkBox"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="paragraphText")
    }
)

DoEType: Enumeration = Enumeration(
    name="DoEType",
    literals={
            EnumerationLiteral(name="LS"),
			EnumerationLiteral(name="CRD"),
			EnumerationLiteral(name="RCBD"),
			EnumerationLiteral(name="other")
    }
)

HypothesisType: Enumeration = Enumeration(
    name="HypothesisType",
    literals={
            EnumerationLiteral(name="null_"),
			EnumerationLiteral(name="alternative")
    }
)

QuestionnaireType: Enumeration = Enumeration(
    name="QuestionnaireType",
    literals={
            EnumerationLiteral(name="Pre"),
			EnumerationLiteral(name="Post")
    }
)

# Classes
jpdl31_ActionType = Class(name="jpdl31::ActionType")
jpdl31_AssignmentType = Class(name="jpdl31::AssignmentType")
Delegation = Class(name="Delegation")
jpdl31_CancelTimerType = Class(name="jpdl31::CancelTimerType")
jpdl31_ConditionType = Class(name="jpdl31::ConditionType")
jpdl31_CreateTimerType = Class(name="jpdl31::CreateTimerType")
jpdl31_ScriptType = Class(name="jpdl31::ScriptType")
jpdl31_DecisionType = Class(name="jpdl31::DecisionType")
jpdl31_ExceptionHandlerType = Class(name="jpdl31::ExceptionHandlerType")
jpdl31_Delegation = Class(name="jpdl31::Delegation")
jpdl31_EventType = Class(name="jpdl31::EventType")
jpdl31_TransitionType1 = Class(name="jpdl31::TransitionType1")
jpdl31_DocumentRoot = Class(name="jpdl31::DocumentRoot")
jpdl31_EStringToStringMapEntry = Class(name="jpdl31::EStringToStringMapEntry")
jpdl31_EndStateType = Class(name="jpdl31::EndStateType")
jpdl31_NodeType = Class(name="jpdl31::NodeType")
jpdl31_ForkType = Class(name="jpdl31::ForkType")
jpdl31_JoinType = Class(name="jpdl31::JoinType")
jpdl31_ProcessStateType = Class(name="jpdl31::ProcessStateType")
jpdl31_ProcessDefinitionType = Class(name="jpdl31::ProcessDefinitionType")
jpdl31_SuperStateType = Class(name="jpdl31::SuperStateType")
jpdl31_StartStateType = Class(name="jpdl31::StartStateType")
jpdl31_StateType = Class(name="jpdl31::StateType")
jpdl31_TimerType = Class(name="jpdl31::TimerType")
jpdl31_TransitionType = Class(name="jpdl31::TransitionType")
jpdl31_SwimlaneType = Class(name="jpdl31::SwimlaneType")
jpdl31_TaskType = Class(name="jpdl31::TaskType")
jpdl31_TaskNodeType = Class(name="jpdl31::TaskNodeType")
jpdl31_VariableType = Class(name="jpdl31::VariableType")
jpdl31_Questionnaire = Class(name="jpdl31::Questionnaire")
jpdl31_ExperimentalPlan = Class(name="jpdl31::ExperimentalPlan")
jpdl31_Metric = Class(name="jpdl31::Metric")
jpdl31_SubProcessType = Class(name="jpdl31::SubProcessType")
jpdl31_Artefact = Class(name="jpdl31::Artefact")
jpdl31_MetricInfo = Class(name="jpdl31::MetricInfo")
jpdl31_Model = Class(name="jpdl31::Model")
jpdl31_Hyphotesis = Class(name="jpdl31::Hyphotesis")
jpdl31_Subhypotheses = Class(name="jpdl31::Subhypotheses")
jpdl31_Level = Class(name="jpdl31::Level")
jpdl31_DependentVariable = Class(name="jpdl31::DependentVariable")
jpdl31_Goal = Class(name="jpdl31::Goal")
jpdl31_Factor = Class(name="jpdl31::Factor")
jpdl31_Question = Class(name="jpdl31::Question")
jpdl31_Alternative = Class(name="jpdl31::Alternative")
jpdl31_Parameter = Class(name="jpdl31::Parameter")
jpdl31_StatisticalTest = Class(name="jpdl31::StatisticalTest")
jpdl31_Design = Class(name="jpdl31::Design")

# jpdl31_ActionType class attributes and methods
jpdl31_ActionType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl31_ActionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ActionType_any: Property = Property(name="any", type=StringType)
jpdl31_ActionType_async: Property = Property(name="async", type=StringType)
jpdl31_ActionType_class: Property = Property(name="class", type=StringType)
jpdl31_ActionType_configType: Property = Property(name="configType", type=StringType)
jpdl31_ActionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_ActionType_name: Property = Property(name="name", type=StringType)
jpdl31_ActionType_refName: Property = Property(name="refName", type=StringType)
jpdl31_ActionType.attributes={jpdl31_ActionType_mixed, jpdl31_ActionType_name, jpdl31_ActionType_class, jpdl31_ActionType_async, jpdl31_ActionType_any, jpdl31_ActionType_expression, jpdl31_ActionType_refName, jpdl31_ActionType_acceptPropagatedEvents, jpdl31_ActionType_configType}

# jpdl31_AssignmentType class attributes and methods
jpdl31_AssignmentType_expression: Property = Property(name="expression", type=StringType)
jpdl31_AssignmentType_actorId: Property = Property(name="actorId", type=StringType)
jpdl31_AssignmentType_pooledActors: Property = Property(name="pooledActors", type=StringType)
jpdl31_AssignmentType.attributes={jpdl31_AssignmentType_pooledActors, jpdl31_AssignmentType_expression, jpdl31_AssignmentType_actorId}

# Delegation class attributes and methods

# jpdl31_CancelTimerType class attributes and methods
jpdl31_CancelTimerType_name: Property = Property(name="name", type=StringType)
jpdl31_CancelTimerType.attributes={jpdl31_CancelTimerType_name}

# jpdl31_ConditionType class attributes and methods
jpdl31_ConditionType_group: Property = Property(name="group", type=StringType)
jpdl31_ConditionType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ConditionType_any: Property = Property(name="any", type=StringType)
jpdl31_ConditionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_ConditionType.attributes={jpdl31_ConditionType_expression, jpdl31_ConditionType_any, jpdl31_ConditionType_group, jpdl31_ConditionType_mixed}

# jpdl31_CreateTimerType class attributes and methods
jpdl31_CreateTimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl31_CreateTimerType_name: Property = Property(name="name", type=StringType)
jpdl31_CreateTimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl31_CreateTimerType_transition: Property = Property(name="transition", type=StringType)
jpdl31_CreateTimerType.attributes={jpdl31_CreateTimerType_name, jpdl31_CreateTimerType_transition, jpdl31_CreateTimerType_repeat, jpdl31_CreateTimerType_duedate}

# jpdl31_ScriptType class attributes and methods
jpdl31_ScriptType_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_ScriptType_any: Property = Property(name="any", type=StringType)
jpdl31_ScriptType_acceptPropagatedEvents: Property = Property(name="acceptPropagatedEvents", type=StringType)
jpdl31_ScriptType_name: Property = Property(name="name", type=StringType)
jpdl31_ScriptType.attributes={jpdl31_ScriptType_acceptPropagatedEvents, jpdl31_ScriptType_any, jpdl31_ScriptType_name, jpdl31_ScriptType_mixed}

# jpdl31_DecisionType class attributes and methods
jpdl31_DecisionType_group: Property = Property(name="group", type=StringType)
jpdl31_DecisionType_async: Property = Property(name="async", type=StringType)
jpdl31_DecisionType_expression: Property = Property(name="expression", type=StringType)
jpdl31_DecisionType_name: Property = Property(name="name", type=StringType)
jpdl31_DecisionType.attributes={jpdl31_DecisionType_expression, jpdl31_DecisionType_group, jpdl31_DecisionType_async, jpdl31_DecisionType_name}

# jpdl31_ExceptionHandlerType class attributes and methods
jpdl31_ExceptionHandlerType_group: Property = Property(name="group", type=StringType)
jpdl31_ExceptionHandlerType_exceptionClass: Property = Property(name="exceptionClass", type=StringType)
jpdl31_ExceptionHandlerType.attributes={jpdl31_ExceptionHandlerType_group, jpdl31_ExceptionHandlerType_exceptionClass}

# jpdl31_Delegation class attributes and methods
jpdl31_Delegation_class: Property = Property(name="class", type=StringType)
jpdl31_Delegation_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_Delegation_any: Property = Property(name="any", type=StringType)
jpdl31_Delegation_configType: Property = Property(name="configType", type=StringType)
jpdl31_Delegation.attributes={jpdl31_Delegation_mixed, jpdl31_Delegation_any, jpdl31_Delegation_class, jpdl31_Delegation_configType}

# jpdl31_EventType class attributes and methods
jpdl31_EventType_actionElements: Property = Property(name="actionElements", type=StringType)
jpdl31_EventType_type: Property = Property(name="type", type=StringType)
jpdl31_EventType.attributes={jpdl31_EventType_actionElements, jpdl31_EventType_type}

# jpdl31_TransitionType1 class attributes and methods
jpdl31_TransitionType1_group: Property = Property(name="group", type=StringType)
jpdl31_TransitionType1_name: Property = Property(name="name", type=StringType)
jpdl31_TransitionType1_to: Property = Property(name="to", type=StringType)
jpdl31_TransitionType1.attributes={jpdl31_TransitionType1_to, jpdl31_TransitionType1_name, jpdl31_TransitionType1_group}

# jpdl31_DocumentRoot class attributes and methods
jpdl31_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
jpdl31_DocumentRoot.attributes={jpdl31_DocumentRoot_mixed}

# jpdl31_EStringToStringMapEntry class attributes and methods

# jpdl31_EndStateType class attributes and methods
jpdl31_EndStateType_group: Property = Property(name="group", type=StringType)
jpdl31_EndStateType_name: Property = Property(name="name", type=StringType)
jpdl31_EndStateType.attributes={jpdl31_EndStateType_name, jpdl31_EndStateType_group}

# jpdl31_NodeType class attributes and methods
jpdl31_NodeType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_NodeType_async: Property = Property(name="async", type=StringType)
jpdl31_NodeType_name: Property = Property(name="name", type=StringType)
jpdl31_NodeType_description: Property = Property(name="description", type=StringType)
jpdl31_NodeType.attributes={jpdl31_NodeType_description, jpdl31_NodeType_name, jpdl31_NodeType_nodeContentElements, jpdl31_NodeType_async}

# jpdl31_ForkType class attributes and methods
jpdl31_ForkType_group: Property = Property(name="group", type=StringType)
jpdl31_ForkType_name: Property = Property(name="name", type=StringType)
jpdl31_ForkType_async: Property = Property(name="async", type=StringType)
jpdl31_ForkType.attributes={jpdl31_ForkType_async, jpdl31_ForkType_group, jpdl31_ForkType_name}

# jpdl31_JoinType class attributes and methods
jpdl31_JoinType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_JoinType_async: Property = Property(name="async", type=StringType)
jpdl31_JoinType_name: Property = Property(name="name", type=StringType)
jpdl31_JoinType.attributes={jpdl31_JoinType_nodeContentElements, jpdl31_JoinType_name, jpdl31_JoinType_async}

# jpdl31_ProcessStateType class attributes and methods
jpdl31_ProcessStateType_group: Property = Property(name="group", type=StringType)
jpdl31_ProcessStateType_async: Property = Property(name="async", type=StringType)
jpdl31_ProcessStateType_name: Property = Property(name="name", type=StringType)
jpdl31_ProcessStateType.attributes={jpdl31_ProcessStateType_async, jpdl31_ProcessStateType_group, jpdl31_ProcessStateType_name}

# jpdl31_ProcessDefinitionType class attributes and methods
jpdl31_ProcessDefinitionType_group: Property = Property(name="group", type=StringType)
jpdl31_ProcessDefinitionType_name: Property = Property(name="name", type=StringType)
jpdl31_ProcessDefinitionType_quantity: Property = Property(name="quantity", type=StringType)
jpdl31_ProcessDefinitionType.attributes={jpdl31_ProcessDefinitionType_name, jpdl31_ProcessDefinitionType_group, jpdl31_ProcessDefinitionType_quantity}

# jpdl31_SuperStateType class attributes and methods
jpdl31_SuperStateType_group: Property = Property(name="group", type=StringType)
jpdl31_SuperStateType_async: Property = Property(name="async", type=StringType)
jpdl31_SuperStateType_name: Property = Property(name="name", type=StringType)
jpdl31_SuperStateType.attributes={jpdl31_SuperStateType_name, jpdl31_SuperStateType_async, jpdl31_SuperStateType_group}

# jpdl31_StartStateType class attributes and methods
jpdl31_StartStateType_name: Property = Property(name="name", type=StringType)
jpdl31_StartStateType_group: Property = Property(name="group", type=StringType)
jpdl31_StartStateType.attributes={jpdl31_StartStateType_group, jpdl31_StartStateType_name}

# jpdl31_StateType class attributes and methods
jpdl31_StateType_nodeContentElements: Property = Property(name="nodeContentElements", type=StringType)
jpdl31_StateType_name: Property = Property(name="name", type=StringType)
jpdl31_StateType_async: Property = Property(name="async", type=StringType)
jpdl31_StateType.attributes={jpdl31_StateType_async, jpdl31_StateType_name, jpdl31_StateType_nodeContentElements}

# jpdl31_TimerType class attributes and methods
jpdl31_TimerType_name: Property = Property(name="name", type=StringType)
jpdl31_TimerType_repeat: Property = Property(name="repeat", type=StringType)
jpdl31_TimerType_transition: Property = Property(name="transition", type=StringType)
jpdl31_TimerType_duedate: Property = Property(name="duedate", type=StringType)
jpdl31_TimerType.attributes={jpdl31_TimerType_name, jpdl31_TimerType_duedate, jpdl31_TimerType_repeat, jpdl31_TimerType_transition}

# jpdl31_TransitionType class attributes and methods
jpdl31_TransitionType_group: Property = Property(name="group", type=StringType)
jpdl31_TransitionType_to: Property = Property(name="to", type=StringType)
jpdl31_TransitionType_name: Property = Property(name="name", type=StringType)
jpdl31_TransitionType.attributes={jpdl31_TransitionType_name, jpdl31_TransitionType_to, jpdl31_TransitionType_group}

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
jpdl31_TaskType.attributes={jpdl31_TaskType_priority, jpdl31_TaskType_signalling, jpdl31_TaskType_blocking, jpdl31_TaskType_swimlane, jpdl31_TaskType_group, jpdl31_TaskType_duedate, jpdl31_TaskType_description, jpdl31_TaskType_name}

# jpdl31_TaskNodeType class attributes and methods
jpdl31_TaskNodeType_group: Property = Property(name="group", type=StringType)
jpdl31_TaskNodeType_endTasks: Property = Property(name="endTasks", type=StringType)
jpdl31_TaskNodeType_name: Property = Property(name="name", type=StringType)
jpdl31_TaskNodeType_signal: Property = Property(name="signal", type=StringType)
jpdl31_TaskNodeType_async: Property = Property(name="async", type=StringType)
jpdl31_TaskNodeType_createTasks: Property = Property(name="createTasks", type=StringType)
jpdl31_TaskNodeType_description: Property = Property(name="description", type=StringType)
jpdl31_TaskNodeType.attributes={jpdl31_TaskNodeType_async, jpdl31_TaskNodeType_createTasks, jpdl31_TaskNodeType_description, jpdl31_TaskNodeType_name, jpdl31_TaskNodeType_group, jpdl31_TaskNodeType_signal, jpdl31_TaskNodeType_endTasks}

# jpdl31_VariableType class attributes and methods
jpdl31_VariableType_any: Property = Property(name="any", type=StringType)
jpdl31_VariableType_access: Property = Property(name="access", type=StringType)
jpdl31_VariableType_mappedName: Property = Property(name="mappedName", type=StringType)
jpdl31_VariableType_name: Property = Property(name="name", type=StringType)
jpdl31_VariableType.attributes={jpdl31_VariableType_name, jpdl31_VariableType_access, jpdl31_VariableType_any, jpdl31_VariableType_mappedName}

# jpdl31_Questionnaire class attributes and methods
jpdl31_Questionnaire_name: Property = Property(name="name", type=StringType)
jpdl31_Questionnaire_type: Property = Property(name="type", type=StringType)
jpdl31_Questionnaire.attributes={jpdl31_Questionnaire_type, jpdl31_Questionnaire_name}

# jpdl31_ExperimentalPlan class attributes and methods

# jpdl31_Metric class attributes and methods
jpdl31_Metric_name: Property = Property(name="name", type=StringType)
jpdl31_Metric_description: Property = Property(name="description", type=StringType)
jpdl31_Metric_type: Property = Property(name="type", type=StringType)
jpdl31_Metric_refname: Property = Property(name="refname", type=StringType)
jpdl31_Metric.attributes={jpdl31_Metric_type, jpdl31_Metric_refname, jpdl31_Metric_name, jpdl31_Metric_description}

# jpdl31_SubProcessType class attributes and methods
jpdl31_SubProcessType_name: Property = Property(name="name", type=StringType)
jpdl31_SubProcessType_version: Property = Property(name="version", type=StringType)
jpdl31_SubProcessType.attributes={jpdl31_SubProcessType_name, jpdl31_SubProcessType_version}

# jpdl31_Artefact class attributes and methods
jpdl31_Artefact_name: Property = Property(name="name", type=StringType)
jpdl31_Artefact_type: Property = Property(name="type", type=StringType)
jpdl31_Artefact_description: Property = Property(name="description", type=StringType)
jpdl31_Artefact.attributes={jpdl31_Artefact_name, jpdl31_Artefact_description, jpdl31_Artefact_type}

# jpdl31_MetricInfo class attributes and methods
jpdl31_MetricInfo_name: Property = Property(name="name", type=StringType)
jpdl31_MetricInfo.attributes={jpdl31_MetricInfo_name}

# jpdl31_Model class attributes and methods

# jpdl31_Hyphotesis class attributes and methods
jpdl31_Hyphotesis_relationOp: Property = Property(name="relationOp", type=StringType)
jpdl31_Hyphotesis_description: Property = Property(name="description", type=StringType)
jpdl31_Hyphotesis_type: Property = Property(name="type", type=StringType)
jpdl31_Hyphotesis_id: Property = Property(name="id", type=StringType)
jpdl31_Hyphotesis.attributes={jpdl31_Hyphotesis_type, jpdl31_Hyphotesis_relationOp, jpdl31_Hyphotesis_description, jpdl31_Hyphotesis_id}

# jpdl31_Subhypotheses class attributes and methods
jpdl31_Subhypotheses_relationOp: Property = Property(name="relationOp", type=StringType)
jpdl31_Subhypotheses.attributes={jpdl31_Subhypotheses_relationOp}

# jpdl31_Level class attributes and methods
jpdl31_Level_name: Property = Property(name="name", type=StringType)
jpdl31_Level.attributes={jpdl31_Level_name}

# jpdl31_DependentVariable class attributes and methods
jpdl31_DependentVariable_name: Property = Property(name="name", type=StringType)
jpdl31_DependentVariable_description: Property = Property(name="description", type=StringType)
jpdl31_DependentVariable.attributes={jpdl31_DependentVariable_description, jpdl31_DependentVariable_name}

# jpdl31_Goal class attributes and methods
jpdl31_Goal_description: Property = Property(name="description", type=StringType)
jpdl31_Goal_id: Property = Property(name="id", type=StringType)
jpdl31_Goal.attributes={jpdl31_Goal_id, jpdl31_Goal_description}

# jpdl31_Factor class attributes and methods
jpdl31_Factor_name: Property = Property(name="name", type=StringType)
jpdl31_Factor_isTreament: Property = Property(name="isTreament", type=StringType)
jpdl31_Factor.attributes={jpdl31_Factor_isTreament, jpdl31_Factor_name}

# jpdl31_Question class attributes and methods
jpdl31_Question_description: Property = Property(name="description", type=StringType)
jpdl31_Question_type: Property = Property(name="type", type=StringType)
jpdl31_Question_required: Property = Property(name="required", type=StringType)
jpdl31_Question.attributes={jpdl31_Question_description, jpdl31_Question_required, jpdl31_Question_type}

# jpdl31_Alternative class attributes and methods
jpdl31_Alternative_description: Property = Property(name="description", type=StringType)
jpdl31_Alternative.attributes={jpdl31_Alternative_description}

# jpdl31_Parameter class attributes and methods
jpdl31_Parameter_key: Property = Property(name="key", type=StringType)
jpdl31_Parameter_value: Property = Property(name="value", type=StringType)
jpdl31_Parameter.attributes={jpdl31_Parameter_key, jpdl31_Parameter_value}

# jpdl31_StatisticalTest class attributes and methods

# jpdl31_Design class attributes and methods
jpdl31_Design_DoE: Property = Property(name="DoE", type=StringType)
jpdl31_Design.attributes={jpdl31_Design_DoE}

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
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="jpdl31_TransitionType1", type=jpdl31_DecisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DecisionType9", type=jpdl31_TransitionType1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation11: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation11",
    ends={
        Property(name="jpdl31_EStringToStringMapEntry13", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot12", type=jpdl31_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap10: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap10",
    ends={
        Property(name="jpdl31_EStringToStringMapEntry", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot", type=jpdl31_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer19: BinaryAssociation = BinaryAssociation(
    name="cancelTimer19",
    ends={
        Property(name="jpdl31_CancelTimerType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot20", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
decision27: BinaryAssociation = BinaryAssociation(
    name="decision27",
    ends={
        Property(name="jpdl31_DecisionType29", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot28", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller21: BinaryAssociation = BinaryAssociation(
    name="controller21",
    ends={
        Property(name="jpdl31_Delegation23", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot22", type=jpdl31_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer24: BinaryAssociation = BinaryAssociation(
    name="createTimer24",
    ends={
        Property(name="jpdl31_CreateTimerType26", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot25", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
join40: BinaryAssociation = BinaryAssociation(
    name="join40",
    ends={
        Property(name="jpdl31_JoinType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot41", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
processState46: BinaryAssociation = BinaryAssociation(
    name="processState46",
    ends={
        Property(name="jpdl31_ProcessStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot47", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
superState55: BinaryAssociation = BinaryAssociation(
    name="superState55",
    ends={
        Property(name="jpdl31_SuperStateType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot56", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
taskNode61: BinaryAssociation = BinaryAssociation(
    name="taskNode61",
    ends={
        Property(name="jpdl31_TaskNodeType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot62", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event75: BinaryAssociation = BinaryAssociation(
    name="event75",
    ends={
        Property(name="jpdl31_EventType77", type=jpdl31_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EndStateType76", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable67: BinaryAssociation = BinaryAssociation(
    name="variable67",
    ends={
        Property(name="jpdl31_VariableType", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot68", type=jpdl31_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
questionnaires69: BinaryAssociation = BinaryAssociation(
    name="questionnaires69",
    ends={
        Property(name="jpdl31_Questionnaire", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot70", type=jpdl31_Questionnaire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plan71: BinaryAssociation = BinaryAssociation(
    name="plan71",
    ends={
        Property(name="jpdl31_ExperimentalPlan", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot72", type=jpdl31_ExperimentalPlan, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
metrics73: BinaryAssociation = BinaryAssociation(
    name="metrics73",
    ends={
        Property(name="jpdl31_Metric", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DocumentRoot74", type=jpdl31_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action81: BinaryAssociation = BinaryAssociation(
    name="action81",
    ends={
        Property(name="jpdl31_ActionType83", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType82", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script84: BinaryAssociation = BinaryAssociation(
    name="script84",
    ends={
        Property(name="jpdl31_ScriptType86", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType85", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler78: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler78",
    ends={
        Property(name="jpdl31_ExceptionHandlerType80", type=jpdl31_EndStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EndStateType79", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action93: BinaryAssociation = BinaryAssociation(
    name="action93",
    ends={
        Property(name="jpdl31_ActionType95", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExceptionHandlerType94", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer87: BinaryAssociation = BinaryAssociation(
    name="createTimer87",
    ends={
        Property(name="jpdl31_CreateTimerType89", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType88", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer90: BinaryAssociation = BinaryAssociation(
    name="cancelTimer90",
    ends={
        Property(name="jpdl31_CancelTimerType92", type=jpdl31_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_EventType91", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event102: BinaryAssociation = BinaryAssociation(
    name="event102",
    ends={
        Property(name="jpdl31_EventType104", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType103", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler105: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler105",
    ends={
        Property(name="jpdl31_ExceptionHandlerType107", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType106", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script96: BinaryAssociation = BinaryAssociation(
    name="script96",
    ends={
        Property(name="jpdl31_ScriptType98", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExceptionHandlerType97", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script99: BinaryAssociation = BinaryAssociation(
    name="script99",
    ends={
        Property(name="jpdl31_ScriptType101", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType100", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer108: BinaryAssociation = BinaryAssociation(
    name="timer108",
    ends={
        Property(name="jpdl31_TimerType110", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType109", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition111: BinaryAssociation = BinaryAssociation(
    name="transition111",
    ends={
        Property(name="jpdl31_TransitionType113", type=jpdl31_ForkType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ForkType112", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition123: BinaryAssociation = BinaryAssociation(
    name="transition123",
    ends={
        Property(name="jpdl31_TransitionType125", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType124", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event114: BinaryAssociation = BinaryAssociation(
    name="event114",
    ends={
        Property(name="jpdl31_EventType116", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType115", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler117: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler117",
    ends={
        Property(name="jpdl31_ExceptionHandlerType119", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType118", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer120: BinaryAssociation = BinaryAssociation(
    name="timer120",
    ends={
        Property(name="jpdl31_TimerType122", type=jpdl31_JoinType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_JoinType121", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer135: BinaryAssociation = BinaryAssociation(
    name="cancelTimer135",
    ends={
        Property(name="jpdl31_CancelTimerType137", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType136", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event138: BinaryAssociation = BinaryAssociation(
    name="event138",
    ends={
        Property(name="jpdl31_EventType140", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType139", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action126: BinaryAssociation = BinaryAssociation(
    name="action126",
    ends={
        Property(name="jpdl31_ActionType128", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType127", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script129: BinaryAssociation = BinaryAssociation(
    name="script129",
    ends={
        Property(name="jpdl31_ScriptType131", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType130", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createTimer132: BinaryAssociation = BinaryAssociation(
    name="createTimer132",
    ends={
        Property(name="jpdl31_CreateTimerType134", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType133", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition147: BinaryAssociation = BinaryAssociation(
    name="transition147",
    ends={
        Property(name="jpdl31_NodeType148", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="jpdl31_TransitionType149", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1))
    }
)
exceptionHandler141: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler141",
    ends={
        Property(name="jpdl31_ExceptionHandlerType143", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType142", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer144: BinaryAssociation = BinaryAssociation(
    name="timer144",
    ends={
        Property(name="jpdl31_TimerType146", type=jpdl31_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_NodeType145", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swimlane150: BinaryAssociation = BinaryAssociation(
    name="swimlane150",
    ends={
        Property(name="jpdl31_SwimlaneType152", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType151", type=jpdl31_SwimlaneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode162: BinaryAssociation = BinaryAssociation(
    name="taskNode162",
    ends={
        Property(name="jpdl31_TaskNodeType164", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType163", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState165: BinaryAssociation = BinaryAssociation(
    name="superState165",
    ends={
        Property(name="jpdl31_SuperStateType167", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType166", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState153: BinaryAssociation = BinaryAssociation(
    name="startState153",
    ends={
        Property(name="jpdl31_StartStateType155", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType154", type=jpdl31_StartStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node156: BinaryAssociation = BinaryAssociation(
    name="node156",
    ends={
        Property(name="jpdl31_NodeType158", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType157", type=jpdl31_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state159: BinaryAssociation = BinaryAssociation(
    name="state159",
    ends={
        Property(name="jpdl31_StateType161", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType160", type=jpdl31_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision177: BinaryAssociation = BinaryAssociation(
    name="decision177",
    ends={
        Property(name="jpdl31_DecisionType179", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType178", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState168: BinaryAssociation = BinaryAssociation(
    name="processState168",
    ends={
        Property(name="jpdl31_ProcessStateType170", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType169", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork171: BinaryAssociation = BinaryAssociation(
    name="fork171",
    ends={
        Property(name="jpdl31_ForkType173", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType172", type=jpdl31_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join174: BinaryAssociation = BinaryAssociation(
    name="join174",
    ends={
        Property(name="jpdl31_JoinType176", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType175", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer189: BinaryAssociation = BinaryAssociation(
    name="createTimer189",
    ends={
        Property(name="jpdl31_CreateTimerType191", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType190", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer192: BinaryAssociation = BinaryAssociation(
    name="cancelTimer192",
    ends={
        Property(name="jpdl31_CancelTimerType194", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType193", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState180: BinaryAssociation = BinaryAssociation(
    name="endState180",
    ends={
        Property(name="jpdl31_EndStateType182", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType181", type=jpdl31_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action183: BinaryAssociation = BinaryAssociation(
    name="action183",
    ends={
        Property(name="jpdl31_ActionType185", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType184", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script186: BinaryAssociation = BinaryAssociation(
    name="script186",
    ends={
        Property(name="jpdl31_ScriptType188", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType187", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task201: BinaryAssociation = BinaryAssociation(
    name="task201",
    ends={
        Property(name="jpdl31_TaskType203", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType202", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event195: BinaryAssociation = BinaryAssociation(
    name="event195",
    ends={
        Property(name="jpdl31_EventType197", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType196", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler198: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler198",
    ends={
        Property(name="jpdl31_ExceptionHandlerType200", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessDefinitionType199", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable206: BinaryAssociation = BinaryAssociation(
    name="variable206",
    ends={
        Property(name="jpdl31_VariableType208", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType207", type=jpdl31_VariableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event209: BinaryAssociation = BinaryAssociation(
    name="event209",
    ends={
        Property(name="jpdl31_EventType211", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType210", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess204: BinaryAssociation = BinaryAssociation(
    name="subProcess204",
    ends={
        Property(name="jpdl31_SubProcessType", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType205", type=jpdl31_SubProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler212: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler212",
    ends={
        Property(name="jpdl31_ExceptionHandlerType214", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType213", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer215: BinaryAssociation = BinaryAssociation(
    name="timer215",
    ends={
        Property(name="jpdl31_TimerType217", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType216", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition218: BinaryAssociation = BinaryAssociation(
    name="transition218",
    ends={
        Property(name="jpdl31_TransitionType220", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ProcessStateType219", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler230: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler230",
    ends={
        Property(name="jpdl31_ExceptionHandlerType232", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType231", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task221: BinaryAssociation = BinaryAssociation(
    name="task221",
    ends={
        Property(name="jpdl31_TaskType223", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType222", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition224: BinaryAssociation = BinaryAssociation(
    name="transition224",
    ends={
        Property(name="jpdl31_TransitionType226", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType225", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event227: BinaryAssociation = BinaryAssociation(
    name="event227",
    ends={
        Property(name="jpdl31_EventType229", type=jpdl31_StartStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StartStateType228", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event233: BinaryAssociation = BinaryAssociation(
    name="event233",
    ends={
        Property(name="jpdl31_EventType235", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType234", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler236: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler236",
    ends={
        Property(name="jpdl31_ExceptionHandlerType238", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType237", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer239: BinaryAssociation = BinaryAssociation(
    name="timer239",
    ends={
        Property(name="jpdl31_TimerType241", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType240", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition242: BinaryAssociation = BinaryAssociation(
    name="transition242",
    ends={
        Property(name="jpdl31_TransitionType244", type=jpdl31_StateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_StateType243", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processState257: BinaryAssociation = BinaryAssociation(
    name="processState257",
    ends={
        Property(name="jpdl31_ProcessStateType259", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType258", type=jpdl31_ProcessStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fork260: BinaryAssociation = BinaryAssociation(
    name="fork260",
    ends={
        Property(name="jpdl31_ForkType262", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType261", type=jpdl31_ForkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node245: BinaryAssociation = BinaryAssociation(
    name="node245",
    ends={
        Property(name="jpdl31_NodeType247", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType246", type=jpdl31_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state248: BinaryAssociation = BinaryAssociation(
    name="state248",
    ends={
        Property(name="jpdl31_StateType250", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType249", type=jpdl31_StateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNode251: BinaryAssociation = BinaryAssociation(
    name="taskNode251",
    ends={
        Property(name="jpdl31_TaskNodeType253", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType252", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superState255: BinaryAssociation = BinaryAssociation(
    name="superState255",
    ends={
        Property(name="jpdl31_SuperStateType256", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType254", type=jpdl31_SuperStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState269: BinaryAssociation = BinaryAssociation(
    name="endState269",
    ends={
        Property(name="jpdl31_EndStateType271", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType270", type=jpdl31_EndStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join263: BinaryAssociation = BinaryAssociation(
    name="join263",
    ends={
        Property(name="jpdl31_JoinType265", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType264", type=jpdl31_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision266: BinaryAssociation = BinaryAssociation(
    name="decision266",
    ends={
        Property(name="jpdl31_DecisionType268", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType267", type=jpdl31_DecisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition281: BinaryAssociation = BinaryAssociation(
    name="transition281",
    ends={
        Property(name="jpdl31_TransitionType283", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType282", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event272: BinaryAssociation = BinaryAssociation(
    name="event272",
    ends={
        Property(name="jpdl31_EventType274", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType273", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler275: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler275",
    ends={
        Property(name="jpdl31_ExceptionHandlerType277", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType276", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer278: BinaryAssociation = BinaryAssociation(
    name="timer278",
    ends={
        Property(name="jpdl31_TimerType280", type=jpdl31_SuperStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SuperStateType279", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task287: BinaryAssociation = BinaryAssociation(
    name="task287",
    ends={
        Property(name="jpdl31_TaskType289", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType288", type=jpdl31_TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event290: BinaryAssociation = BinaryAssociation(
    name="event290",
    ends={
        Property(name="jpdl31_EventType292", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType291", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment284: BinaryAssociation = BinaryAssociation(
    name="assignment284",
    ends={
        Property(name="jpdl31_AssignmentType286", type=jpdl31_SwimlaneType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_SwimlaneType285", type=jpdl31_AssignmentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionHandler293: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler293",
    ends={
        Property(name="jpdl31_ExceptionHandlerType295", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType294", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer296: BinaryAssociation = BinaryAssociation(
    name="timer296",
    ends={
        Property(name="jpdl31_TimerType298", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType297", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition299: BinaryAssociation = BinaryAssociation(
    name="transition299",
    ends={
        Property(name="jpdl31_TransitionType301", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType300", type=jpdl31_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment306: BinaryAssociation = BinaryAssociation(
    name="assignment306",
    ends={
        Property(name="jpdl31_AssignmentType308", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType307", type=jpdl31_AssignmentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller309: BinaryAssociation = BinaryAssociation(
    name="controller309",
    ends={
        Property(name="jpdl31_Delegation311", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType310", type=jpdl31_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefacts302: BinaryAssociation = BinaryAssociation(
    name="artefacts302",
    ends={
        Property(name="jpdl31_Artefact", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType303", type=jpdl31_Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics304: BinaryAssociation = BinaryAssociation(
    name="metrics304",
    ends={
        Property(name="jpdl31_MetricInfo", type=jpdl31_TaskNodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskNodeType305", type=jpdl31_MetricInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event312: BinaryAssociation = BinaryAssociation(
    name="event312",
    ends={
        Property(name="jpdl31_EventType314", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType313", type=jpdl31_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timer315: BinaryAssociation = BinaryAssociation(
    name="timer315",
    ends={
        Property(name="jpdl31_TimerType317", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType316", type=jpdl31_TimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefacts318: BinaryAssociation = BinaryAssociation(
    name="artefacts318",
    ends={
        Property(name="jpdl31_Artefact320", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType319", type=jpdl31_Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricInfo321: BinaryAssociation = BinaryAssociation(
    name="metricInfo321",
    ends={
        Property(name="jpdl31_MetricInfo323", type=jpdl31_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TaskType322", type=jpdl31_MetricInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action324: BinaryAssociation = BinaryAssociation(
    name="action324",
    ends={
        Property(name="jpdl31_ActionType326", type=jpdl31_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TimerType325", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script327: BinaryAssociation = BinaryAssociation(
    name="script327",
    ends={
        Property(name="jpdl31_ScriptType329", type=jpdl31_TimerType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TimerType328", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createTimer336: BinaryAssociation = BinaryAssociation(
    name="createTimer336",
    ends={
        Property(name="jpdl31_CreateTimerType338", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType337", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action330: BinaryAssociation = BinaryAssociation(
    name="action330",
    ends={
        Property(name="jpdl31_ActionType332", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType331", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script333: BinaryAssociation = BinaryAssociation(
    name="script333",
    ends={
        Property(name="jpdl31_ScriptType335", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType334", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer339: BinaryAssociation = BinaryAssociation(
    name="cancelTimer339",
    ends={
        Property(name="jpdl31_CancelTimerType341", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType340", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler342: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler342",
    ends={
        Property(name="jpdl31_ExceptionHandlerType344", type=jpdl31_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType343", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action347: BinaryAssociation = BinaryAssociation(
    name="action347",
    ends={
        Property(name="jpdl31_ActionType349", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1348", type=jpdl31_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition345: BinaryAssociation = BinaryAssociation(
    name="condition345",
    ends={
        Property(name="jpdl31_ConditionType", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1346", type=jpdl31_ConditionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelTimer356: BinaryAssociation = BinaryAssociation(
    name="cancelTimer356",
    ends={
        Property(name="jpdl31_CancelTimerType358", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1357", type=jpdl31_CancelTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script350: BinaryAssociation = BinaryAssociation(
    name="script350",
    ends={
        Property(name="jpdl31_ScriptType352", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1351", type=jpdl31_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createTimer353: BinaryAssociation = BinaryAssociation(
    name="createTimer353",
    ends={
        Property(name="jpdl31_CreateTimerType355", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1354", type=jpdl31_CreateTimerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionHandler359: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler359",
    ends={
        Property(name="jpdl31_ExceptionHandlerType361", type=jpdl31_TransitionType1, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_TransitionType1360", type=jpdl31_ExceptionHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements362: BinaryAssociation = BinaryAssociation(
    name="elements362",
    ends={
        Property(name="jpdl31_DocumentRoot363", type=jpdl31_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Model", type=jpdl31_DocumentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricReferenced364: BinaryAssociation = BinaryAssociation(
    name="metricReferenced364",
    ends={
        Property(name="jpdl31_Metric366", type=jpdl31_MetricInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_MetricInfo365", type=jpdl31_Metric, multiplicity=Multiplicity(0, 1))
    }
)
formalizes367: BinaryAssociation = BinaryAssociation(
    name="formalizes367",
    ends={
        Property(name="jpdl31_Subhypotheses", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Hyphotesis", type=jpdl31_Subhypotheses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treatment370: BinaryAssociation = BinaryAssociation(
    name="treatment370",
    ends={
        Property(name="jpdl31_Level", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Hyphotesis371", type=jpdl31_Level, multiplicity=Multiplicity(0, 9999))
    }
)
dependentVariable372: BinaryAssociation = BinaryAssociation(
    name="dependentVariable372",
    ends={
        Property(name="jpdl31_DependentVariable", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Hyphotesis373", type=jpdl31_DependentVariable, multiplicity=Multiplicity(0, 1))
    }
)
fromGoal368: BinaryAssociation = BinaryAssociation(
    name="fromGoal368",
    ends={
        Property(name="jpdl31_Goal", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Hyphotesis369", type=jpdl31_Goal, multiplicity=Multiplicity(1, 1))
    }
)
measureBy380: BinaryAssociation = BinaryAssociation(
    name="measureBy380",
    ends={
        Property(name="jpdl31_Metric382", type=jpdl31_DependentVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_DependentVariable381", type=jpdl31_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
treatment374: BinaryAssociation = BinaryAssociation(
    name="treatment374",
    ends={
        Property(name="jpdl31_Level376", type=jpdl31_Subhypotheses, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Subhypotheses375", type=jpdl31_Level, multiplicity=Multiplicity(0, 1))
    }
)
dependentVariable377: BinaryAssociation = BinaryAssociation(
    name="dependentVariable377",
    ends={
        Property(name="jpdl31_DependentVariable379", type=jpdl31_Subhypotheses, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Subhypotheses378", type=jpdl31_DependentVariable, multiplicity=Multiplicity(0, 1))
    }
)
relatesTo385: BinaryAssociation = BinaryAssociation(
    name="relatesTo385",
    ends={
        Property(name="jpdl31_ProcessDefinitionType387", type=jpdl31_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Metric386", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(0, 9999))
    }
)
levels383: BinaryAssociation = BinaryAssociation(
    name="levels383",
    ends={
        Property(name="jpdl31_Level384", type=jpdl31_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Factor", type=jpdl31_Level, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
question388: BinaryAssociation = BinaryAssociation(
    name="question388",
    ends={
        Property(name="jpdl31_Question", type=jpdl31_Questionnaire, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Questionnaire389", type=jpdl31_Question, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
option393: BinaryAssociation = BinaryAssociation(
    name="option393",
    ends={
        Property(name="jpdl31_Alternative", type=jpdl31_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Question394", type=jpdl31_Alternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference0396: BinaryAssociation = BinaryAssociation(
    name="EReference0396",
    ends={
        Property(name="jpdl31_Question397", type=jpdl31_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Question395", type=jpdl31_Question, multiplicity=Multiplicity(0, 1))
    }
)
processes390: BinaryAssociation = BinaryAssociation(
    name="processes390",
    ends={
        Property(name="jpdl31_ProcessDefinitionType392", type=jpdl31_Questionnaire, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Questionnaire391", type=jpdl31_ProcessDefinitionType, multiplicity=Multiplicity(0, 9999))
    }
)
hypotheses398: BinaryAssociation = BinaryAssociation(
    name="hypotheses398",
    ends={
        Property(name="jpdl31_Hyphotesis400", type=jpdl31_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Goal399", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals401: BinaryAssociation = BinaryAssociation(
    name="goals401",
    ends={
        Property(name="jpdl31_Goal403", type=jpdl31_ExperimentalPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExperimentalPlan402", type=jpdl31_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors409: BinaryAssociation = BinaryAssociation(
    name="factors409",
    ends={
        Property(name="jpdl31_Design410", type=jpdl31_Factor, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="jpdl31_Factor411", type=jpdl31_Design, multiplicity=Multiplicity(1, 1))
    }
)
parameters412: BinaryAssociation = BinaryAssociation(
    name="parameters412",
    ends={
        Property(name="jpdl31_Parameter", type=jpdl31_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Design413", type=jpdl31_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test414: BinaryAssociation = BinaryAssociation(
    name="test414",
    ends={
        Property(name="jpdl31_StatisticalTest", type=jpdl31_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Design415", type=jpdl31_StatisticalTest, multiplicity=Multiplicity(0, 9999))
    }
)
hypothesis404: BinaryAssociation = BinaryAssociation(
    name="hypothesis404",
    ends={
        Property(name="jpdl31_Hyphotesis406", type=jpdl31_ExperimentalPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExperimentalPlan405", type=jpdl31_Hyphotesis, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
design407: BinaryAssociation = BinaryAssociation(
    name="design407",
    ends={
        Property(name="jpdl31_Design", type=jpdl31_ExperimentalPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_ExperimentalPlan408", type=jpdl31_Design, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
depVariable416: BinaryAssociation = BinaryAssociation(
    name="depVariable416",
    ends={
        Property(name="jpdl31_DependentVariable418", type=jpdl31_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="jpdl31_Design417", type=jpdl31_DependentVariable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_jpdl31_AssignmentType_Delegation = Generalization(general=Delegation, specific=jpdl31_AssignmentType)

# Domain Model
domain_model = DomainModel(
    name="jpdl31",
    types={jpdl31_ActionType, jpdl31_AssignmentType, Delegation, jpdl31_CancelTimerType, jpdl31_ConditionType, jpdl31_CreateTimerType, jpdl31_ScriptType, jpdl31_DecisionType, jpdl31_ExceptionHandlerType, jpdl31_Delegation, jpdl31_EventType, jpdl31_TransitionType1, jpdl31_DocumentRoot, jpdl31_EStringToStringMapEntry, jpdl31_EndStateType, jpdl31_NodeType, jpdl31_ForkType, jpdl31_JoinType, jpdl31_ProcessStateType, jpdl31_ProcessDefinitionType, jpdl31_SuperStateType, jpdl31_StartStateType, jpdl31_StateType, jpdl31_TimerType, jpdl31_TransitionType, jpdl31_SwimlaneType, jpdl31_TaskType, jpdl31_TaskNodeType, jpdl31_VariableType, jpdl31_Questionnaire, jpdl31_ExperimentalPlan, jpdl31_Metric, jpdl31_SubProcessType, jpdl31_Artefact, jpdl31_MetricInfo, jpdl31_Model, jpdl31_Hyphotesis, jpdl31_Subhypotheses, jpdl31_Level, jpdl31_DependentVariable, jpdl31_Goal, jpdl31_Factor, jpdl31_Question, jpdl31_Alternative, jpdl31_Parameter, jpdl31_StatisticalTest, jpdl31_Design, BooleanType, ConfigType, ConfigTypeType, ConfigTypeType1, PriorityTypeMember0, SignalType, TypeTypeMember1, ArtefactType, MetricType, RelationOperator, AnswerType, DoEType, HypothesisType, QuestionnaireType},
    associations={action0, script1, exceptionHandler6, handler3, event4, transition8, xSISchemaLocation11, xMLNSPrefixMap10, cancelTimer19, action14, assignment17, decision27, controller21, createTimer24, endState30, event32, join40, exceptionHandler35, fork38, processState46, node42, processDefinition44, superState55, script48, startState51, state53, timer63, transition65, swimlane57, task59, taskNode61, event75, variable67, questionnaires69, plan71, metrics73, action81, script84, exceptionHandler78, action93, createTimer87, cancelTimer90, event102, exceptionHandler105, script96, script99, timer108, transition111, transition123, event114, exceptionHandler117, timer120, cancelTimer135, event138, action126, script129, createTimer132, transition147, exceptionHandler141, timer144, swimlane150, taskNode162, superState165, startState153, node156, state159, decision177, processState168, fork171, join174, createTimer189, cancelTimer192, endState180, action183, script186, task201, event195, exceptionHandler198, variable206, event209, subProcess204, exceptionHandler212, timer215, transition218, exceptionHandler230, task221, transition224, event227, event233, exceptionHandler236, timer239, transition242, processState257, fork260, node245, state248, taskNode251, superState255, endState269, join263, decision266, transition281, event272, exceptionHandler275, timer278, task287, event290, assignment284, exceptionHandler293, timer296, transition299, assignment306, controller309, artefacts302, metrics304, event312, timer315, artefacts318, metricInfo321, action324, script327, createTimer336, action330, script333, cancelTimer339, exceptionHandler342, action347, condition345, cancelTimer356, script350, createTimer353, exceptionHandler359, elements362, metricReferenced364, formalizes367, treatment370, dependentVariable372, fromGoal368, measureBy380, treatment374, dependentVariable377, relatesTo385, levels383, question388, option393, EReference0396, processes390, hypotheses398, goals401, factors409, parameters412, test414, hypothesis404, design407, depVariable416},
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