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
behavioral_elements_common_behavior_Instance = Class(name="behavioral_elements_common_behavior_Instance", is_abstract=True)
ModelElement = Class(name="ModelElement")
SendAction = Class(name="SendAction")
SignalEvent = Class(name="SignalEvent")
behavioral_elements_common_behavior_Action = Class(name="behavioral_elements_common_behavior_Action", is_abstract=True)
IterationExpression = Class(name="IterationExpression")
ObjectSetExpression = Class(name="ObjectSetExpression")
Classifier = Class(name="Classifier")
AttributeLink = Class(name="AttributeLink")
LinkEnd = Class(name="LinkEnd")
ComponentInstance = Class(name="ComponentInstance")
Instance = Class(name="Instance")
Link = Class(name="Link")
behavioral_elements_common_behavior_Signal = Class(name="behavioral_elements_common_behavior_Signal")
Reception = Class(name="Reception")
BehavioralFeature = Class(name="BehavioralFeature")
behavioral_elements_common_behavior_Object = Class(name="behavioral_elements_common_behavior_Object")
behavioral_elements_common_behavior_Link = Class(name="behavioral_elements_common_behavior_Link")
Association = Class(name="Association")
ActionExpression = Class(name="ActionExpression")
Argument = Class(name="Argument")
ActionSequence = Class(name="ActionSequence")
Stimulus = Class(name="Stimulus")
Transition = Class(name="Transition")
behavioral_elements_common_behavior_CreateAction = Class(name="behavioral_elements_common_behavior_CreateAction")
Action = Class(name="Action")
behavioral_elements_common_behavior_DestroyAction = Class(name="behavioral_elements_common_behavior_DestroyAction")
behavioral_elements_common_behavior_UninterpretedAction = Class(name="behavioral_elements_common_behavior_UninterpretedAction")
behavioral_elements_common_behavior_AttributeLink = Class(name="behavioral_elements_common_behavior_AttributeLink")
Attribute = Class(name="Attribute")
behavioral_elements_common_behavior_SendAction = Class(name="behavioral_elements_common_behavior_SendAction")
Signal = Class(name="Signal")
behavioral_elements_common_behavior_ActionSequence = Class(name="behavioral_elements_common_behavior_ActionSequence")
behavioral_elements_common_behavior_LinkObject = Class(name="behavioral_elements_common_behavior_LinkObject")
common_behavior_Object = Class(name="common_behavior_Object")
common_behavior_Link = Class(name="common_behavior_Link")
behavioral_elements_common_behavior_DataValue = Class(name="behavioral_elements_common_behavior_DataValue")
behavioral_elements_common_behavior_CallAction = Class(name="behavioral_elements_common_behavior_CallAction")
Operation = Class(name="Operation")
behavioral_elements_common_behavior_ReturnAction = Class(name="behavioral_elements_common_behavior_ReturnAction")
behavioral_elements_common_behavior_TerminateAction = Class(name="behavioral_elements_common_behavior_TerminateAction")
behavioral_elements_common_behavior_Stimulus = Class(name="behavioral_elements_common_behavior_Stimulus")
behavioral_elements_common_behavior_Argument = Class(name="behavioral_elements_common_behavior_Argument")
Expression = Class(name="Expression")
behavioral_elements_common_behavior_Reception = Class(name="behavioral_elements_common_behavior_Reception")
behavioral_elements_common_behavior_LinkEnd = Class(name="behavioral_elements_common_behavior_LinkEnd")
AssociationEnd = Class(name="AssociationEnd")
behavioral_elements_common_behavior_SubsystemInstance = Class(name="behavioral_elements_common_behavior_SubsystemInstance")
behavioral_elements_use_cases_UseCase = Class(name="behavioral_elements_use_cases_UseCase")
Extend = Class(name="Extend")
Include = Class(name="Include")
Message = Class(name="Message")
InteractionInstanceSet = Class(name="InteractionInstanceSet")
behavioral_elements_common_behavior_Exception = Class(name="behavioral_elements_common_behavior_Exception")
behavioral_elements_common_behavior_ComponentInstance = Class(name="behavioral_elements_common_behavior_ComponentInstance")
NodeInstance = Class(name="NodeInstance")
behavioral_elements_common_behavior_NodeInstance = Class(name="behavioral_elements_common_behavior_NodeInstance")
behavioral_elements_state_machines_StateMachine = Class(name="behavioral_elements_state_machines_StateMachine")
State = Class(name="State")
ExtensionPoint = Class(name="ExtensionPoint")
behavioral_elements_use_cases_Actor = Class(name="behavioral_elements_use_cases_Actor")
behavioral_elements_use_cases_UseCaseInstance = Class(name="behavioral_elements_use_cases_UseCaseInstance")
behavioral_elements_use_cases_Extend = Class(name="behavioral_elements_use_cases_Extend")
Relationship = Class(name="Relationship")
BooleanExpression = Class(name="BooleanExpression")
UseCase = Class(name="UseCase")
behavioral_elements_use_cases_Include = Class(name="behavioral_elements_use_cases_Include")
behavioral_elements_use_cases_ExtensionPoint = Class(name="behavioral_elements_use_cases_ExtensionPoint")
Event = Class(name="Event")
behavioral_elements_state_machines_TimeEvent = Class(name="behavioral_elements_state_machines_TimeEvent")
TimeExpression = Class(name="TimeExpression")
behavioral_elements_state_machines_CallEvent = Class(name="behavioral_elements_state_machines_CallEvent")
SubmachineState = Class(name="SubmachineState")
behavioral_elements_state_machines_Event = Class(name="behavioral_elements_state_machines_Event", is_abstract=True)
Parameter_ = Class(name="Parameter")
behavioral_elements_state_machines_StateVertex = Class(name="behavioral_elements_state_machines_StateVertex", is_abstract=True)
CompositeState = Class(name="CompositeState")
behavioral_elements_state_machines_State = Class(name="behavioral_elements_state_machines_State", is_abstract=True)
StateVertex = Class(name="StateVertex")
StateMachine = Class(name="StateMachine")
behavioral_elements_state_machines_ChangeEvent = Class(name="behavioral_elements_state_machines_ChangeEvent")
behavioral_elements_state_machines_Guard = Class(name="behavioral_elements_state_machines_Guard")
behavioral_elements_state_machines_SignalEvent = Class(name="behavioral_elements_state_machines_SignalEvent")
behavioral_elements_state_machines_Transition = Class(name="behavioral_elements_state_machines_Transition")
Guard = Class(name="Guard")
behavioral_elements_state_machines_CompositeState = Class(name="behavioral_elements_state_machines_CompositeState")
CollaborationInstanceSet = Class(name="CollaborationInstanceSet")
Collaboration = Class(name="Collaboration")
behavioral_elements_collaborations_ClassifierRole = Class(name="behavioral_elements_collaborations_ClassifierRole")
Multiplicity_ = Class(name="Multiplicity_")
behavioral_elements_state_machines_Pseudostate = Class(name="behavioral_elements_state_machines_Pseudostate")
behavioral_elements_state_machines_SimpleState = Class(name="behavioral_elements_state_machines_SimpleState")
behavioral_elements_state_machines_SubmachineState = Class(name="behavioral_elements_state_machines_SubmachineState")
behavioral_elements_state_machines_SynchState = Class(name="behavioral_elements_state_machines_SynchState")
behavioral_elements_state_machines_StubState = Class(name="behavioral_elements_state_machines_StubState")
behavioral_elements_state_machines_FinalState = Class(name="behavioral_elements_state_machines_FinalState")
behavioral_elements_collaborations_Collaboration = Class(name="behavioral_elements_collaborations_Collaboration")
core_GeneralizableElement = Class(name="core_GeneralizableElement")
core_Namespace = Class(name="core_Namespace")
Interaction = Class(name="Interaction")
ClassifierRole = Class(name="ClassifierRole")
Feature = Class(name="Feature")
behavioral_elements_collaborations_AssociationRole = Class(name="behavioral_elements_collaborations_AssociationRole")
behavioral_elements_collaborations_AssociationEndRole = Class(name="behavioral_elements_collaborations_AssociationEndRole")
behavioral_elements_collaborations_Message = Class(name="behavioral_elements_collaborations_Message")
behavioral_elements_collaborations_CollaborationInstanceSet = Class(name="behavioral_elements_collaborations_CollaborationInstanceSet")
AssociationRole = Class(name="AssociationRole")
behavioral_elements_collaborations_Interaction = Class(name="behavioral_elements_collaborations_Interaction")
behavioral_elements_collaborations_InteractionInstanceSet = Class(name="behavioral_elements_collaborations_InteractionInstanceSet")
SimpleState = Class(name="SimpleState")
behavioral_elements_activity_graphs_CallState = Class(name="behavioral_elements_activity_graphs_CallState")
ActionState = Class(name="ActionState")
behavioral_elements_activity_graphs_ObjectFlowState = Class(name="behavioral_elements_activity_graphs_ObjectFlowState")
behavioral_elements_activity_graphs_ActivityGraph = Class(name="behavioral_elements_activity_graphs_ActivityGraph")
Partition = Class(name="Partition")
behavioral_elements_activity_graphs_Partition = Class(name="behavioral_elements_activity_graphs_Partition")
ActivityGraph = Class(name="ActivityGraph")
behavioral_elements_activity_graphs_SubactivityState = Class(name="behavioral_elements_activity_graphs_SubactivityState")
ArgListsExpression = Class(name="ArgListsExpression")
behavioral_elements_activity_graphs_ActionState = Class(name="behavioral_elements_activity_graphs_ActionState")
behavioral_elements_activity_graphs_ClassifierInState = Class(name="behavioral_elements_activity_graphs_ClassifierInState")

# behavioral_elements_common_behavior_Instance class attributes and methods

# ModelElement class attributes and methods

# SendAction class attributes and methods

# SignalEvent class attributes and methods

# behavioral_elements_common_behavior_Action class attributes and methods
behavioral_elements_common_behavior_Action_isAsynchronous: Property = Property(name="isAsynchronous", type=StringType)
behavioral_elements_common_behavior_Action.attributes={behavioral_elements_common_behavior_Action_isAsynchronous}

# IterationExpression class attributes and methods

# ObjectSetExpression class attributes and methods

# Classifier class attributes and methods

# AttributeLink class attributes and methods

# LinkEnd class attributes and methods

# ComponentInstance class attributes and methods

# Instance class attributes and methods

# Link class attributes and methods

# behavioral_elements_common_behavior_Signal class attributes and methods

# Reception class attributes and methods

# BehavioralFeature class attributes and methods

# behavioral_elements_common_behavior_Object class attributes and methods

# behavioral_elements_common_behavior_Link class attributes and methods

# Association class attributes and methods

# ActionExpression class attributes and methods

# Argument class attributes and methods

# ActionSequence class attributes and methods

# Stimulus class attributes and methods

# Transition class attributes and methods

# behavioral_elements_common_behavior_CreateAction class attributes and methods

# Action class attributes and methods

# behavioral_elements_common_behavior_DestroyAction class attributes and methods

# behavioral_elements_common_behavior_UninterpretedAction class attributes and methods

# behavioral_elements_common_behavior_AttributeLink class attributes and methods

# Attribute class attributes and methods

# behavioral_elements_common_behavior_SendAction class attributes and methods

# Signal class attributes and methods

# behavioral_elements_common_behavior_ActionSequence class attributes and methods

# behavioral_elements_common_behavior_LinkObject class attributes and methods

# common_behavior_Object class attributes and methods

# common_behavior_Link class attributes and methods

# behavioral_elements_common_behavior_DataValue class attributes and methods

# behavioral_elements_common_behavior_CallAction class attributes and methods

# Operation class attributes and methods

# behavioral_elements_common_behavior_ReturnAction class attributes and methods

# behavioral_elements_common_behavior_TerminateAction class attributes and methods

# behavioral_elements_common_behavior_Stimulus class attributes and methods

# behavioral_elements_common_behavior_Argument class attributes and methods

# Expression class attributes and methods

# behavioral_elements_common_behavior_Reception class attributes and methods
behavioral_elements_common_behavior_Reception_specification: Property = Property(name="specification", type=StringType)
behavioral_elements_common_behavior_Reception_isRoot: Property = Property(name="isRoot", type=StringType)
behavioral_elements_common_behavior_Reception_isLeaf: Property = Property(name="isLeaf", type=StringType)
behavioral_elements_common_behavior_Reception_isAbstract: Property = Property(name="isAbstract", type=StringType)
behavioral_elements_common_behavior_Reception.attributes={behavioral_elements_common_behavior_Reception_isAbstract, behavioral_elements_common_behavior_Reception_isLeaf, behavioral_elements_common_behavior_Reception_specification, behavioral_elements_common_behavior_Reception_isRoot}

# behavioral_elements_common_behavior_LinkEnd class attributes and methods

# AssociationEnd class attributes and methods

# behavioral_elements_common_behavior_SubsystemInstance class attributes and methods

# behavioral_elements_use_cases_UseCase class attributes and methods

# Extend class attributes and methods

# Include class attributes and methods

# Message class attributes and methods

# InteractionInstanceSet class attributes and methods

# behavioral_elements_common_behavior_Exception class attributes and methods

# behavioral_elements_common_behavior_ComponentInstance class attributes and methods

# NodeInstance class attributes and methods

# behavioral_elements_common_behavior_NodeInstance class attributes and methods

# behavioral_elements_state_machines_StateMachine class attributes and methods

# State class attributes and methods

# ExtensionPoint class attributes and methods

# behavioral_elements_use_cases_Actor class attributes and methods

# behavioral_elements_use_cases_UseCaseInstance class attributes and methods

# behavioral_elements_use_cases_Extend class attributes and methods

# Relationship class attributes and methods

# BooleanExpression class attributes and methods

# UseCase class attributes and methods

# behavioral_elements_use_cases_Include class attributes and methods

# behavioral_elements_use_cases_ExtensionPoint class attributes and methods
behavioral_elements_use_cases_ExtensionPoint_location: Property = Property(name="location", type=StringType)
behavioral_elements_use_cases_ExtensionPoint.attributes={behavioral_elements_use_cases_ExtensionPoint_location}

# Event class attributes and methods

# behavioral_elements_state_machines_TimeEvent class attributes and methods

# TimeExpression class attributes and methods

# behavioral_elements_state_machines_CallEvent class attributes and methods

# SubmachineState class attributes and methods

# behavioral_elements_state_machines_Event class attributes and methods

# Parameter class attributes and methods

# behavioral_elements_state_machines_StateVertex class attributes and methods

# CompositeState class attributes and methods

# behavioral_elements_state_machines_State class attributes and methods

# StateVertex class attributes and methods

# StateMachine class attributes and methods

# behavioral_elements_state_machines_ChangeEvent class attributes and methods

# behavioral_elements_state_machines_Guard class attributes and methods

# behavioral_elements_state_machines_SignalEvent class attributes and methods

# behavioral_elements_state_machines_Transition class attributes and methods

# Guard class attributes and methods

# behavioral_elements_state_machines_CompositeState class attributes and methods
behavioral_elements_state_machines_CompositeState_isConcurrent: Property = Property(name="isConcurrent", type=StringType)
behavioral_elements_state_machines_CompositeState.attributes={behavioral_elements_state_machines_CompositeState_isConcurrent}

# CollaborationInstanceSet class attributes and methods

# Collaboration class attributes and methods

# behavioral_elements_collaborations_ClassifierRole class attributes and methods

# Multiplicity_ class attributes and methods

# behavioral_elements_state_machines_Pseudostate class attributes and methods
behavioral_elements_state_machines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
behavioral_elements_state_machines_Pseudostate.attributes={behavioral_elements_state_machines_Pseudostate_kind}

# behavioral_elements_state_machines_SimpleState class attributes and methods

# behavioral_elements_state_machines_SubmachineState class attributes and methods

# behavioral_elements_state_machines_SynchState class attributes and methods
behavioral_elements_state_machines_SynchState_bound: Property = Property(name="bound", type=StringType)
behavioral_elements_state_machines_SynchState.attributes={behavioral_elements_state_machines_SynchState_bound}

# behavioral_elements_state_machines_StubState class attributes and methods
behavioral_elements_state_machines_StubState_referenceState: Property = Property(name="referenceState", type=StringType)
behavioral_elements_state_machines_StubState.attributes={behavioral_elements_state_machines_StubState_referenceState}

# behavioral_elements_state_machines_FinalState class attributes and methods

# behavioral_elements_collaborations_Collaboration class attributes and methods

# core_GeneralizableElement class attributes and methods

# core_Namespace class attributes and methods

# Interaction class attributes and methods

# ClassifierRole class attributes and methods

# Feature class attributes and methods

# behavioral_elements_collaborations_AssociationRole class attributes and methods

# behavioral_elements_collaborations_AssociationEndRole class attributes and methods

# behavioral_elements_collaborations_Message class attributes and methods

# behavioral_elements_collaborations_CollaborationInstanceSet class attributes and methods

# AssociationRole class attributes and methods

# behavioral_elements_collaborations_Interaction class attributes and methods

# behavioral_elements_collaborations_InteractionInstanceSet class attributes and methods

# SimpleState class attributes and methods

# behavioral_elements_activity_graphs_CallState class attributes and methods

# ActionState class attributes and methods

# behavioral_elements_activity_graphs_ObjectFlowState class attributes and methods
behavioral_elements_activity_graphs_ObjectFlowState_isSynch: Property = Property(name="isSynch", type=StringType)
behavioral_elements_activity_graphs_ObjectFlowState.attributes={behavioral_elements_activity_graphs_ObjectFlowState_isSynch}

# behavioral_elements_activity_graphs_ActivityGraph class attributes and methods

# Partition class attributes and methods

# behavioral_elements_activity_graphs_Partition class attributes and methods

# ActivityGraph class attributes and methods

# behavioral_elements_activity_graphs_SubactivityState class attributes and methods
behavioral_elements_activity_graphs_SubactivityState_isDynamic: Property = Property(name="isDynamic", type=StringType)
behavioral_elements_activity_graphs_SubactivityState.attributes={behavioral_elements_activity_graphs_SubactivityState_isDynamic}

# ArgListsExpression class attributes and methods

# behavioral_elements_activity_graphs_ActionState class attributes and methods
behavioral_elements_activity_graphs_ActionState_isDynamic: Property = Property(name="isDynamic", type=StringType)
behavioral_elements_activity_graphs_ActionState.attributes={behavioral_elements_activity_graphs_ActionState_isDynamic}

# behavioral_elements_activity_graphs_ClassifierInState class attributes and methods

# Relationships
context12: BinaryAssociation = BinaryAssociation(
    name="context12",
    ends={
        Property(name="BehavioralFeature", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="raisedSignal", type=BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
sendAction13: BinaryAssociation = BinaryAssociation(
    name="sendAction13",
    ends={
        Property(name="SendAction", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="signal14", type=SendAction, multiplicity=Multiplicity(0, 9999))
    }
)
occurrence15: BinaryAssociation = BinaryAssociation(
    name="occurrence15",
    ends={
        Property(name="SignalEvent", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="signal16", type=SignalEvent, multiplicity=Multiplicity(0, 9999))
    }
)
recurrence17: BinaryAssociation = BinaryAssociation(
    name="recurrence17",
    ends={
        Property(name="IterationExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action", type=IterationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="ObjectSetExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action19", type=ObjectSetExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier0: BinaryAssociation = BinaryAssociation(
    name="classifier0",
    ends={
        Property(name="Classifier", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Instance", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
attributeLink1: BinaryAssociation = BinaryAssociation(
    name="attributeLink1",
    ends={
        Property(name="AttributeLink", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=AttributeLink, multiplicity=Multiplicity(0, 9999))
    }
)
linkEnd2: BinaryAssociation = BinaryAssociation(
    name="linkEnd2",
    ends={
        Property(name="LinkEnd", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=LinkEnd, multiplicity=Multiplicity(0, 9999))
    }
)
slot3: BinaryAssociation = BinaryAssociation(
    name="slot3",
    ends={
        Property(name="AttributeLink5", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance4", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentInstance6: BinaryAssociation = BinaryAssociation(
    name="componentInstance6",
    ends={
        Property(name="ComponentInstance", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="resident", type=ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)
ownedInstance7: BinaryAssociation = BinaryAssociation(
    name="ownedInstance7",
    ends={
        Property(name="Instance", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Instance8", type=Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLink9: BinaryAssociation = BinaryAssociation(
    name="ownedLink9",
    ends={
        Property(name="Link", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Instance10", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reception11: BinaryAssociation = BinaryAssociation(
    name="reception11",
    ends={
        Property(name="Reception", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="signal", type=Reception, multiplicity=Multiplicity(0, 9999))
    }
)
instance32: BinaryAssociation = BinaryAssociation(
    name="instance32",
    ends={
        Property(name="Instance33", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
linkEnd34: BinaryAssociation = BinaryAssociation(
    name="linkEnd34",
    ends={
        Property(name="LinkEnd35", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiedValue", type=LinkEnd, multiplicity=Multiplicity(0, 1))
    }
)
association36: BinaryAssociation = BinaryAssociation(
    name="association36",
    ends={
        Property(name="Association", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Link", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
connection37: BinaryAssociation = BinaryAssociation(
    name="connection37",
    ends={
        Property(name="LinkEnd38", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=LinkEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
script20: BinaryAssociation = BinaryAssociation(
    name="script20",
    ends={
        Property(name="ActionExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action21", type=ActionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualArgument22: BinaryAssociation = BinaryAssociation(
    name="actualArgument22",
    ends={
        Property(name="Argument", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="action", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionSequence23: BinaryAssociation = BinaryAssociation(
    name="actionSequence23",
    ends={
        Property(name="ActionSequence", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="action24", type=ActionSequence, multiplicity=Multiplicity(0, 1))
    }
)
stimulus25: BinaryAssociation = BinaryAssociation(
    name="stimulus25",
    ends={
        Property(name="Stimulus", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dispatchAction", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
transition26: BinaryAssociation = BinaryAssociation(
    name="transition26",
    ends={
        Property(name="Transition", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="effect", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
instantiation27: BinaryAssociation = BinaryAssociation(
    name="instantiation27",
    ends={
        Property(name="Classifier28", type=behavioral_elements_common_behavior_CreateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="createAction", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
attribute29: BinaryAssociation = BinaryAssociation(
    name="attribute29",
    ends={
        Property(name="Attribute", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_AttributeLink", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
value30: BinaryAssociation = BinaryAssociation(
    name="value30",
    ends={
        Property(name="Instance31", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeLink", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
operation41: BinaryAssociation = BinaryAssociation(
    name="operation41",
    ends={
        Property(name="callAction", type=Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=behavioral_elements_common_behavior_CallAction, multiplicity=Multiplicity(1, 1))
    }
)
signal42: BinaryAssociation = BinaryAssociation(
    name="signal42",
    ends={
        Property(name="Signal", type=behavioral_elements_common_behavior_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sendAction", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
stimulus39: BinaryAssociation = BinaryAssociation(
    name="stimulus39",
    ends={
        Property(name="Stimulus40", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLink", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiedValue54: BinaryAssociation = BinaryAssociation(
    name="qualifiedValue54",
    ends={
        Property(name="AttributeLink56", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="linkEnd55", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument57: BinaryAssociation = BinaryAssociation(
    name="argument57",
    ends={
        Property(name="Instance58", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
action43: BinaryAssociation = BinaryAssociation(
    name="action43",
    ends={
        Property(name="Action", type=behavioral_elements_common_behavior_ActionSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="actionSequence", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="Expression", type=behavioral_elements_common_behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Argument", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action45: BinaryAssociation = BinaryAssociation(
    name="action45",
    ends={
        Property(name="Action46", type=behavioral_elements_common_behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="actualArgument", type=Action, multiplicity=Multiplicity(0, 1))
    }
)
signal47: BinaryAssociation = BinaryAssociation(
    name="signal47",
    ends={
        Property(name="Signal48", type=behavioral_elements_common_behavior_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="reception", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
instance49: BinaryAssociation = BinaryAssociation(
    name="instance49",
    ends={
        Property(name="Instance50", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="linkEnd", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
link51: BinaryAssociation = BinaryAssociation(
    name="link51",
    ends={
        Property(name="Link52", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=Link, multiplicity=Multiplicity(1, 1))
    }
)
associationEnd53: BinaryAssociation = BinaryAssociation(
    name="associationEnd53",
    ends={
        Property(name="AssociationEnd", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_LinkEnd", type=AssociationEnd, multiplicity=Multiplicity(1, 1))
    }
)
extender78: BinaryAssociation = BinaryAssociation(
    name="extender78",
    ends={
        Property(name="Extend", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
extend79: BinaryAssociation = BinaryAssociation(
    name="extend79",
    ends={
        Property(name="Extend80", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
includer81: BinaryAssociation = BinaryAssociation(
    name="includer81",
    ends={
        Property(name="Include", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="addition", type=Include, multiplicity=Multiplicity(0, 9999))
    }
)
sender59: BinaryAssociation = BinaryAssociation(
    name="sender59",
    ends={
        Property(name="Instance61", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus60", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
receiver62: BinaryAssociation = BinaryAssociation(
    name="receiver62",
    ends={
        Property(name="Instance64", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus63", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
communicationLink65: BinaryAssociation = BinaryAssociation(
    name="communicationLink65",
    ends={
        Property(name="Link66", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="stimulus", type=Link, multiplicity=Multiplicity(0, 1))
    }
)
dispatchAction67: BinaryAssociation = BinaryAssociation(
    name="dispatchAction67",
    ends={
        Property(name="Action69", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="stimulus68", type=Action, multiplicity=Multiplicity(1, 1))
    }
)
playedRole70: BinaryAssociation = BinaryAssociation(
    name="playedRole70",
    ends={
        Property(name="Message", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="conformingStimulus", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
interactionInstanceSet71: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet71",
    ends={
        Property(name="InteractionInstanceSet", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingStimulus", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
nodeInstance72: BinaryAssociation = BinaryAssociation(
    name="nodeInstance72",
    ends={
        Property(name="NodeInstance", type=behavioral_elements_common_behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="resident73", type=NodeInstance, multiplicity=Multiplicity(0, 1))
    }
)
resident74: BinaryAssociation = BinaryAssociation(
    name="resident74",
    ends={
        Property(name="Instance75", type=behavioral_elements_common_behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="componentInstance", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
resident76: BinaryAssociation = BinaryAssociation(
    name="resident76",
    ends={
        Property(name="ComponentInstance77", type=behavioral_elements_common_behavior_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="nodeInstance", type=ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
extend99: BinaryAssociation = BinaryAssociation(
    name="extend99",
    ends={
        Property(name="Extend101", type=behavioral_elements_use_cases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint100", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
context102: BinaryAssociation = BinaryAssociation(
    name="context102",
    ends={
        Property(name="ModelElement", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
top103: BinaryAssociation = BinaryAssociation(
    name="top103",
    ends={
        Property(name="State", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions104: BinaryAssociation = BinaryAssociation(
    name="transitions104",
    ends={
        Property(name="Transition106", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine105", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include82: BinaryAssociation = BinaryAssociation(
    name="include82",
    ends={
        Property(name="Include84", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base83", type=Include, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint85: BinaryAssociation = BinaryAssociation(
    name="extensionPoint85",
    ends={
        Property(name="ExtensionPoint", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition86: BinaryAssociation = BinaryAssociation(
    name="condition86",
    ends={
        Property(name="BooleanExpression", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_use_cases_Extend", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base87: BinaryAssociation = BinaryAssociation(
    name="base87",
    ends={
        Property(name="UseCase", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extender", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension88: BinaryAssociation = BinaryAssociation(
    name="extension88",
    ends={
        Property(name="UseCase89", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoint90: BinaryAssociation = BinaryAssociation(
    name="extensionPoint90",
    ends={
        Property(name="ExtensionPoint92", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend91", type=ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
addition93: BinaryAssociation = BinaryAssociation(
    name="addition93",
    ends={
        Property(name="UseCase94", type=behavioral_elements_use_cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includer", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base95: BinaryAssociation = BinaryAssociation(
    name="base95",
    ends={
        Property(name="UseCase96", type=behavioral_elements_use_cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase97: BinaryAssociation = BinaryAssociation(
    name="useCase97",
    ends={
        Property(name="UseCase98", type=behavioral_elements_use_cases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
deferrableEvent122: BinaryAssociation = BinaryAssociation(
    name="deferrableEvent122",
    ends={
        Property(name="Event", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State123", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
internalTransition124: BinaryAssociation = BinaryAssociation(
    name="internalTransition124",
    ends={
        Property(name="Transition125", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity126: BinaryAssociation = BinaryAssociation(
    name="doActivity126",
    ends={
        Property(name="Action128", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State127", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when129: BinaryAssociation = BinaryAssociation(
    name="when129",
    ends={
        Property(name="TimeExpression", type=behavioral_elements_state_machines_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_TimeEvent", type=TimeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachineState107: BinaryAssociation = BinaryAssociation(
    name="submachineState107",
    ends={
        Property(name="SubmachineState", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=SubmachineState, multiplicity=Multiplicity(0, 9999))
    }
)
parameter108: BinaryAssociation = BinaryAssociation(
    name="parameter108",
    ends={
        Property(name="Parameter", type=behavioral_elements_state_machines_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_Event", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition109: BinaryAssociation = BinaryAssociation(
    name="transition109",
    ends={
        Property(name="Transition110", type=behavioral_elements_state_machines_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container111: BinaryAssociation = BinaryAssociation(
    name="container111",
    ends={
        Property(name="CompositeState", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
outgoing112: BinaryAssociation = BinaryAssociation(
    name="outgoing112",
    ends={
        Property(name="Transition113", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming114: BinaryAssociation = BinaryAssociation(
    name="incoming114",
    ends={
        Property(name="Transition115", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry116: BinaryAssociation = BinaryAssociation(
    name="entry116",
    ends={
        Property(name="Action117", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit118: BinaryAssociation = BinaryAssociation(
    name="exit118",
    ends={
        Property(name="Action120", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State119", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine121: BinaryAssociation = BinaryAssociation(
    name="stateMachine121",
    ends={
        Property(name="StateMachine", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="top", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
subvertex149: BinaryAssociation = BinaryAssociation(
    name="subvertex149",
    ends={
        Property(name="StateVertex150", type=behavioral_elements_state_machines_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeExpression151: BinaryAssociation = BinaryAssociation(
    name="changeExpression151",
    ends={
        Property(name="BooleanExpression152", type=behavioral_elements_state_machines_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_ChangeEvent", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression153: BinaryAssociation = BinaryAssociation(
    name="expression153",
    ends={
        Property(name="BooleanExpression154", type=behavioral_elements_state_machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_Guard", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition155: BinaryAssociation = BinaryAssociation(
    name="transition155",
    ends={
        Property(name="Transition156", type=behavioral_elements_state_machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
operation130: BinaryAssociation = BinaryAssociation(
    name="operation130",
    ends={
        Property(name="Operation131", type=behavioral_elements_state_machines_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="occurrence", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal132: BinaryAssociation = BinaryAssociation(
    name="signal132",
    ends={
        Property(name="Signal134", type=behavioral_elements_state_machines_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="occurrence133", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
guard135: BinaryAssociation = BinaryAssociation(
    name="guard135",
    ends={
        Property(name="Guard", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect136: BinaryAssociation = BinaryAssociation(
    name="effect136",
    ends={
        Property(name="Action138", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition137", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state139: BinaryAssociation = BinaryAssociation(
    name="state139",
    ends={
        Property(name="State140", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="internalTransition", type=State, multiplicity=Multiplicity(0, 1))
    }
)
trigger141: BinaryAssociation = BinaryAssociation(
    name="trigger141",
    ends={
        Property(name="Event143", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition142", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine144: BinaryAssociation = BinaryAssociation(
    name="stateMachine144",
    ends={
        Property(name="StateMachine145", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source146: BinaryAssociation = BinaryAssociation(
    name="source146",
    ends={
        Property(name="StateVertex", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target147: BinaryAssociation = BinaryAssociation(
    name="target147",
    ends={
        Property(name="StateVertex148", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
collaborationInstanceSet164: BinaryAssociation = BinaryAssociation(
    name="collaborationInstanceSet164",
    ends={
        Property(name="CollaborationInstanceSet", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration165", type=CollaborationInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
usedCollaboration166: BinaryAssociation = BinaryAssociation(
    name="usedCollaboration166",
    ends={
        Property(name="Collaboration", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Collaboration167", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
representedClassifier168: BinaryAssociation = BinaryAssociation(
    name="representedClassifier168",
    ends={
        Property(name="Classifier170", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration169", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity171: BinaryAssociation = BinaryAssociation(
    name="multiplicity171",
    ends={
        Property(name="Multiplicity", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base172: BinaryAssociation = BinaryAssociation(
    name="base172",
    ends={
        Property(name="Classifier174", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole173", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
submachine157: BinaryAssociation = BinaryAssociation(
    name="submachine157",
    ends={
        Property(name="StateMachine158", type=behavioral_elements_state_machines_SubmachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
interaction159: BinaryAssociation = BinaryAssociation(
    name="interaction159",
    ends={
        Property(name="Interaction", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representedOperation160: BinaryAssociation = BinaryAssociation(
    name="representedOperation160",
    ends={
        Property(name="Operation161", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
constrainingElement162: BinaryAssociation = BinaryAssociation(
    name="constrainingElement162",
    ends={
        Property(name="ModelElement163", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Collaboration", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
interaction200: BinaryAssociation = BinaryAssociation(
    name="interaction200",
    ends={
        Property(name="Interaction201", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=Interaction, multiplicity=Multiplicity(1, 1))
    }
)
activator202: BinaryAssociation = BinaryAssociation(
    name="activator202",
    ends={
        Property(name="Message203", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
sender204: BinaryAssociation = BinaryAssociation(
    name="sender204",
    ends={
        Property(name="ClassifierRole", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message205", type=ClassifierRole, multiplicity=Multiplicity(1, 1))
    }
)
receiver206: BinaryAssociation = BinaryAssociation(
    name="receiver206",
    ends={
        Property(name="ClassifierRole208", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message207", type=ClassifierRole, multiplicity=Multiplicity(1, 1))
    }
)
predecessor209: BinaryAssociation = BinaryAssociation(
    name="predecessor209",
    ends={
        Property(name="Message210", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
successor211: BinaryAssociation = BinaryAssociation(
    name="successor211",
    ends={
        Property(name="Message212", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
availableFeature175: BinaryAssociation = BinaryAssociation(
    name="availableFeature175",
    ends={
        Property(name="Feature", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole176", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
availableContents177: BinaryAssociation = BinaryAssociation(
    name="availableContents177",
    ends={
        Property(name="ModelElement179", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole178", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
conformingInstance180: BinaryAssociation = BinaryAssociation(
    name="conformingInstance180",
    ends={
        Property(name="Instance182", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole181", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity183: BinaryAssociation = BinaryAssociation(
    name="multiplicity183",
    ends={
        Property(name="Multiplicity184", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base185: BinaryAssociation = BinaryAssociation(
    name="base185",
    ends={
        Property(name="Association187", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole186", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
message188: BinaryAssociation = BinaryAssociation(
    name="message188",
    ends={
        Property(name="Message189", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationConnection", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
conformingLink190: BinaryAssociation = BinaryAssociation(
    name="conformingLink190",
    ends={
        Property(name="Link192", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole191", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationMultiplicity193: BinaryAssociation = BinaryAssociation(
    name="collaborationMultiplicity193",
    ends={
        Property(name="Multiplicity194", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationEndRole", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base195: BinaryAssociation = BinaryAssociation(
    name="base195",
    ends={
        Property(name="AssociationEnd197", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationEndRole196", type=AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
availableQualifier198: BinaryAssociation = BinaryAssociation(
    name="availableQualifier198",
    ends={
        Property(name="Attribute199", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEndRole", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
interactionInstanceSet236: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet236",
    ends={
        Property(name="InteractionInstanceSet238", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="context237", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration239: BinaryAssociation = BinaryAssociation(
    name="collaboration239",
    ends={
        Property(name="Collaboration240", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="collaborationInstanceSet", type=Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
participatingInstance241: BinaryAssociation = BinaryAssociation(
    name="participatingInstance241",
    ends={
        Property(name="Instance242", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet", type=Instance, multiplicity=Multiplicity(1, 9999))
    }
)
participatingLink243: BinaryAssociation = BinaryAssociation(
    name="participatingLink243",
    ends={
        Property(name="Link245", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet244", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingElement246: BinaryAssociation = BinaryAssociation(
    name="constrainingElement246",
    ends={
        Property(name="ModelElement248", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet247", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
communicationConnection213: BinaryAssociation = BinaryAssociation(
    name="communicationConnection213",
    ends={
        Property(name="AssociationRole", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message214", type=AssociationRole, multiplicity=Multiplicity(0, 1))
    }
)
action215: BinaryAssociation = BinaryAssociation(
    name="action215",
    ends={
        Property(name="Action217", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message216", type=Action, multiplicity=Multiplicity(1, 1))
    }
)
conformingStimulus218: BinaryAssociation = BinaryAssociation(
    name="conformingStimulus218",
    ends={
        Property(name="Stimulus219", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="playedRole", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
message220: BinaryAssociation = BinaryAssociation(
    name="message220",
    ends={
        Property(name="Message221", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
context222: BinaryAssociation = BinaryAssociation(
    name="context222",
    ends={
        Property(name="Collaboration224", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction223", type=Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
interactionInstanceSet225: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet225",
    ends={
        Property(name="InteractionInstanceSet227", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction226", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
context228: BinaryAssociation = BinaryAssociation(
    name="context228",
    ends={
        Property(name="CollaborationInstanceSet229", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="interactionInstanceSet", type=CollaborationInstanceSet, multiplicity=Multiplicity(1, 1))
    }
)
interaction230: BinaryAssociation = BinaryAssociation(
    name="interaction230",
    ends={
        Property(name="Interaction232", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="interactionInstanceSet231", type=Interaction, multiplicity=Multiplicity(0, 1))
    }
)
participatingStimulus233: BinaryAssociation = BinaryAssociation(
    name="participatingStimulus233",
    ends={
        Property(name="Stimulus235", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="interactionInstanceSet234", type=Stimulus, multiplicity=Multiplicity(1, 9999))
    }
)
dynamicArguments257: BinaryAssociation = BinaryAssociation(
    name="dynamicArguments257",
    ends={
        Property(name="ArgListsExpression258", type=behavioral_elements_activity_graphs_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ActionState", type=ArgListsExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicMultiplicity259: BinaryAssociation = BinaryAssociation(
    name="dynamicMultiplicity259",
    ends={
        Property(name="Multiplicity261", type=behavioral_elements_activity_graphs_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ActionState260", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter262: BinaryAssociation = BinaryAssociation(
    name="parameter262",
    ends={
        Property(name="Parameter263", type=behavioral_elements_activity_graphs_ObjectFlowState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ObjectFlowState", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
partition249: BinaryAssociation = BinaryAssociation(
    name="partition249",
    ends={
        Property(name="Partition", type=behavioral_elements_activity_graphs_ActivityGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="activityGraph", type=Partition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents250: BinaryAssociation = BinaryAssociation(
    name="contents250",
    ends={
        Property(name="ModelElement251", type=behavioral_elements_activity_graphs_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_Partition", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
activityGraph252: BinaryAssociation = BinaryAssociation(
    name="activityGraph252",
    ends={
        Property(name="ActivityGraph", type=behavioral_elements_activity_graphs_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="partition", type=ActivityGraph, multiplicity=Multiplicity(1, 1))
    }
)
dynamicArguments253: BinaryAssociation = BinaryAssociation(
    name="dynamicArguments253",
    ends={
        Property(name="ArgListsExpression", type=behavioral_elements_activity_graphs_SubactivityState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_SubactivityState", type=ArgListsExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicMultiplicity254: BinaryAssociation = BinaryAssociation(
    name="dynamicMultiplicity254",
    ends={
        Property(name="Multiplicity256", type=behavioral_elements_activity_graphs_SubactivityState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_SubactivityState255", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type264: BinaryAssociation = BinaryAssociation(
    name="type264",
    ends={
        Property(name="Classifier266", type=behavioral_elements_activity_graphs_ObjectFlowState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ObjectFlowState265", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
type267: BinaryAssociation = BinaryAssociation(
    name="type267",
    ends={
        Property(name="Classifier268", type=behavioral_elements_activity_graphs_ClassifierInState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ClassifierInState", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
inState269: BinaryAssociation = BinaryAssociation(
    name="inState269",
    ends={
        Property(name="State271", type=behavioral_elements_activity_graphs_ClassifierInState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ClassifierInState270", type=State, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_behavioral_elements_common_behavior_Instance_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Instance)
gen_behavioral_elements_common_behavior_Action_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Action)
gen_behavioral_elements_common_behavior_Signal_Classifier = Generalization(general=Classifier, specific=behavioral_elements_common_behavior_Signal)
gen_behavioral_elements_common_behavior_Object_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_Object)
gen_behavioral_elements_common_behavior_Link_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Link)
gen_behavioral_elements_common_behavior_CreateAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_CreateAction)
gen_behavioral_elements_common_behavior_DestroyAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_DestroyAction)
gen_behavioral_elements_common_behavior_UninterpretedAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_UninterpretedAction)
gen_behavioral_elements_common_behavior_AttributeLink_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_AttributeLink)
gen_behavioral_elements_common_behavior_SendAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_SendAction)
gen_behavioral_elements_common_behavior_ActionSequence_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_ActionSequence)
gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Object = Generalization(general=common_behavior_Object, specific=behavioral_elements_common_behavior_LinkObject)
gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Link = Generalization(general=common_behavior_Link, specific=behavioral_elements_common_behavior_LinkObject)
gen_behavioral_elements_common_behavior_DataValue_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_DataValue)
gen_behavioral_elements_common_behavior_CallAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_CallAction)
gen_behavioral_elements_common_behavior_ReturnAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_ReturnAction)
gen_behavioral_elements_common_behavior_TerminateAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_TerminateAction)
gen_behavioral_elements_common_behavior_Stimulus_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Stimulus)
gen_behavioral_elements_common_behavior_Argument_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Argument)
gen_behavioral_elements_common_behavior_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=behavioral_elements_common_behavior_Reception)
gen_behavioral_elements_common_behavior_LinkEnd_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_LinkEnd)
gen_behavioral_elements_common_behavior_SubsystemInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_SubsystemInstance)
gen_behavioral_elements_use_cases_UseCase_Classifier = Generalization(general=Classifier, specific=behavioral_elements_use_cases_UseCase)
gen_behavioral_elements_common_behavior_Exception_Signal = Generalization(general=Signal, specific=behavioral_elements_common_behavior_Exception)
gen_behavioral_elements_common_behavior_ComponentInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_ComponentInstance)
gen_behavioral_elements_common_behavior_NodeInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_NodeInstance)
gen_behavioral_elements_state_machines_StateMachine_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_StateMachine)
gen_behavioral_elements_use_cases_Actor_Classifier = Generalization(general=Classifier, specific=behavioral_elements_use_cases_Actor)
gen_behavioral_elements_use_cases_UseCaseInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_use_cases_UseCaseInstance)
gen_behavioral_elements_use_cases_Extend_Relationship = Generalization(general=Relationship, specific=behavioral_elements_use_cases_Extend)
gen_behavioral_elements_use_cases_Include_Relationship = Generalization(general=Relationship, specific=behavioral_elements_use_cases_Include)
gen_behavioral_elements_use_cases_ExtensionPoint_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_use_cases_ExtensionPoint)
gen_behavioral_elements_state_machines_TimeEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_TimeEvent)
gen_behavioral_elements_state_machines_CallEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_CallEvent)
gen_behavioral_elements_state_machines_Event_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Event)
gen_behavioral_elements_state_machines_StateVertex_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_StateVertex)
gen_behavioral_elements_state_machines_State_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_State)
gen_behavioral_elements_state_machines_ChangeEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_ChangeEvent)
gen_behavioral_elements_state_machines_Guard_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Guard)
gen_behavioral_elements_state_machines_SignalEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_SignalEvent)
gen_behavioral_elements_state_machines_Transition_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Transition)
gen_behavioral_elements_state_machines_CompositeState_State = Generalization(general=State, specific=behavioral_elements_state_machines_CompositeState)
gen_behavioral_elements_collaborations_ClassifierRole_Classifier = Generalization(general=Classifier, specific=behavioral_elements_collaborations_ClassifierRole)
gen_behavioral_elements_state_machines_Pseudostate_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_Pseudostate)
gen_behavioral_elements_state_machines_SimpleState_State = Generalization(general=State, specific=behavioral_elements_state_machines_SimpleState)
gen_behavioral_elements_state_machines_SubmachineState_CompositeState = Generalization(general=CompositeState, specific=behavioral_elements_state_machines_SubmachineState)
gen_behavioral_elements_state_machines_SynchState_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_SynchState)
gen_behavioral_elements_state_machines_StubState_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_StubState)
gen_behavioral_elements_state_machines_FinalState_State = Generalization(general=State, specific=behavioral_elements_state_machines_FinalState)
gen_behavioral_elements_collaborations_Collaboration_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=behavioral_elements_collaborations_Collaboration)
gen_behavioral_elements_collaborations_Collaboration_core_Namespace = Generalization(general=core_Namespace, specific=behavioral_elements_collaborations_Collaboration)
gen_behavioral_elements_collaborations_Message_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_Message)
gen_behavioral_elements_collaborations_AssociationRole_Association = Generalization(general=Association, specific=behavioral_elements_collaborations_AssociationRole)
gen_behavioral_elements_collaborations_AssociationEndRole_AssociationEnd = Generalization(general=AssociationEnd, specific=behavioral_elements_collaborations_AssociationEndRole)
gen_behavioral_elements_collaborations_CollaborationInstanceSet_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_CollaborationInstanceSet)
gen_behavioral_elements_collaborations_Interaction_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_Interaction)
gen_behavioral_elements_collaborations_InteractionInstanceSet_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_InteractionInstanceSet)
gen_behavioral_elements_activity_graphs_ActionState_SimpleState = Generalization(general=SimpleState, specific=behavioral_elements_activity_graphs_ActionState)
gen_behavioral_elements_activity_graphs_CallState_ActionState = Generalization(general=ActionState, specific=behavioral_elements_activity_graphs_CallState)
gen_behavioral_elements_activity_graphs_ObjectFlowState_SimpleState = Generalization(general=SimpleState, specific=behavioral_elements_activity_graphs_ObjectFlowState)
gen_behavioral_elements_activity_graphs_ActivityGraph_StateMachine = Generalization(general=StateMachine, specific=behavioral_elements_activity_graphs_ActivityGraph)
gen_behavioral_elements_activity_graphs_Partition_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_activity_graphs_Partition)
gen_behavioral_elements_activity_graphs_SubactivityState_SubmachineState = Generalization(general=SubmachineState, specific=behavioral_elements_activity_graphs_SubactivityState)
gen_behavioral_elements_activity_graphs_ClassifierInState_Classifier = Generalization(general=Classifier, specific=behavioral_elements_activity_graphs_ClassifierInState)

# Domain Model
domain_model = DomainModel(
    name="behavioral_elements",
    types={behavioral_elements_common_behavior_Instance, ModelElement, SendAction, SignalEvent, behavioral_elements_common_behavior_Action, IterationExpression, ObjectSetExpression, Classifier, AttributeLink, LinkEnd, ComponentInstance, Instance, Link, behavioral_elements_common_behavior_Signal, Reception, BehavioralFeature, behavioral_elements_common_behavior_Object, behavioral_elements_common_behavior_Link, Association, ActionExpression, Argument, ActionSequence, Stimulus, Transition, behavioral_elements_common_behavior_CreateAction, Action, behavioral_elements_common_behavior_DestroyAction, behavioral_elements_common_behavior_UninterpretedAction, behavioral_elements_common_behavior_AttributeLink, Attribute, behavioral_elements_common_behavior_SendAction, Signal, behavioral_elements_common_behavior_ActionSequence, behavioral_elements_common_behavior_LinkObject, common_behavior_Object, common_behavior_Link, behavioral_elements_common_behavior_DataValue, behavioral_elements_common_behavior_CallAction, Operation, behavioral_elements_common_behavior_ReturnAction, behavioral_elements_common_behavior_TerminateAction, behavioral_elements_common_behavior_Stimulus, behavioral_elements_common_behavior_Argument, Expression, behavioral_elements_common_behavior_Reception, behavioral_elements_common_behavior_LinkEnd, AssociationEnd, behavioral_elements_common_behavior_SubsystemInstance, behavioral_elements_use_cases_UseCase, Extend, Include, Message, InteractionInstanceSet, behavioral_elements_common_behavior_Exception, behavioral_elements_common_behavior_ComponentInstance, NodeInstance, behavioral_elements_common_behavior_NodeInstance, behavioral_elements_state_machines_StateMachine, State, ExtensionPoint, behavioral_elements_use_cases_Actor, behavioral_elements_use_cases_UseCaseInstance, behavioral_elements_use_cases_Extend, Relationship, BooleanExpression, UseCase, behavioral_elements_use_cases_Include, behavioral_elements_use_cases_ExtensionPoint, Event, behavioral_elements_state_machines_TimeEvent, TimeExpression, behavioral_elements_state_machines_CallEvent, SubmachineState, behavioral_elements_state_machines_Event, Parameter_, behavioral_elements_state_machines_StateVertex, CompositeState, behavioral_elements_state_machines_State, StateVertex, StateMachine, behavioral_elements_state_machines_ChangeEvent, behavioral_elements_state_machines_Guard, behavioral_elements_state_machines_SignalEvent, behavioral_elements_state_machines_Transition, Guard, behavioral_elements_state_machines_CompositeState, CollaborationInstanceSet, Collaboration, behavioral_elements_collaborations_ClassifierRole, Multiplicity_, behavioral_elements_state_machines_Pseudostate, behavioral_elements_state_machines_SimpleState, behavioral_elements_state_machines_SubmachineState, behavioral_elements_state_machines_SynchState, behavioral_elements_state_machines_StubState, behavioral_elements_state_machines_FinalState, behavioral_elements_collaborations_Collaboration, core_GeneralizableElement, core_Namespace, Interaction, ClassifierRole, Feature, behavioral_elements_collaborations_AssociationRole, behavioral_elements_collaborations_AssociationEndRole, behavioral_elements_collaborations_Message, behavioral_elements_collaborations_CollaborationInstanceSet, AssociationRole, behavioral_elements_collaborations_Interaction, behavioral_elements_collaborations_InteractionInstanceSet, SimpleState, behavioral_elements_activity_graphs_CallState, ActionState, behavioral_elements_activity_graphs_ObjectFlowState, behavioral_elements_activity_graphs_ActivityGraph, Partition, behavioral_elements_activity_graphs_Partition, ActivityGraph, behavioral_elements_activity_graphs_SubactivityState, ArgListsExpression, behavioral_elements_activity_graphs_ActionState, behavioral_elements_activity_graphs_ClassifierInState},
    associations={context12, sendAction13, occurrence15, recurrence17, target18, classifier0, attributeLink1, linkEnd2, slot3, componentInstance6, ownedInstance7, ownedLink9, reception11, instance32, linkEnd34, association36, connection37, script20, actualArgument22, actionSequence23, stimulus25, transition26, instantiation27, attribute29, value30, operation41, signal42, stimulus39, qualifiedValue54, argument57, action43, value44, action45, signal47, instance49, link51, associationEnd53, extender78, extend79, includer81, sender59, receiver62, communicationLink65, dispatchAction67, playedRole70, interactionInstanceSet71, nodeInstance72, resident74, resident76, extend99, context102, top103, transitions104, include82, extensionPoint85, condition86, base87, extension88, extensionPoint90, addition93, base95, useCase97, deferrableEvent122, internalTransition124, doActivity126, when129, submachineState107, parameter108, transition109, container111, outgoing112, incoming114, entry116, exit118, stateMachine121, subvertex149, changeExpression151, expression153, transition155, operation130, signal132, guard135, effect136, state139, trigger141, stateMachine144, source146, target147, collaborationInstanceSet164, usedCollaboration166, representedClassifier168, multiplicity171, base172, submachine157, interaction159, representedOperation160, constrainingElement162, interaction200, activator202, sender204, receiver206, predecessor209, successor211, availableFeature175, availableContents177, conformingInstance180, multiplicity183, base185, message188, conformingLink190, collaborationMultiplicity193, base195, availableQualifier198, interactionInstanceSet236, collaboration239, participatingInstance241, participatingLink243, constrainingElement246, communicationConnection213, action215, conformingStimulus218, message220, context222, interactionInstanceSet225, context228, interaction230, participatingStimulus233, dynamicArguments257, dynamicMultiplicity259, parameter262, partition249, contents250, activityGraph252, dynamicArguments253, dynamicMultiplicity254, type264, type267, inState269},
    generalizations={gen_behavioral_elements_common_behavior_Instance_ModelElement, gen_behavioral_elements_common_behavior_Action_ModelElement, gen_behavioral_elements_common_behavior_Signal_Classifier, gen_behavioral_elements_common_behavior_Object_Instance, gen_behavioral_elements_common_behavior_Link_ModelElement, gen_behavioral_elements_common_behavior_CreateAction_Action, gen_behavioral_elements_common_behavior_DestroyAction_Action, gen_behavioral_elements_common_behavior_UninterpretedAction_Action, gen_behavioral_elements_common_behavior_AttributeLink_ModelElement, gen_behavioral_elements_common_behavior_SendAction_Action, gen_behavioral_elements_common_behavior_ActionSequence_Action, gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Object, gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Link, gen_behavioral_elements_common_behavior_DataValue_Instance, gen_behavioral_elements_common_behavior_CallAction_Action, gen_behavioral_elements_common_behavior_ReturnAction_Action, gen_behavioral_elements_common_behavior_TerminateAction_Action, gen_behavioral_elements_common_behavior_Stimulus_ModelElement, gen_behavioral_elements_common_behavior_Argument_ModelElement, gen_behavioral_elements_common_behavior_Reception_BehavioralFeature, gen_behavioral_elements_common_behavior_LinkEnd_ModelElement, gen_behavioral_elements_common_behavior_SubsystemInstance_Instance, gen_behavioral_elements_use_cases_UseCase_Classifier, gen_behavioral_elements_common_behavior_Exception_Signal, gen_behavioral_elements_common_behavior_ComponentInstance_Instance, gen_behavioral_elements_common_behavior_NodeInstance_Instance, gen_behavioral_elements_state_machines_StateMachine_ModelElement, gen_behavioral_elements_use_cases_Actor_Classifier, gen_behavioral_elements_use_cases_UseCaseInstance_Instance, gen_behavioral_elements_use_cases_Extend_Relationship, gen_behavioral_elements_use_cases_Include_Relationship, gen_behavioral_elements_use_cases_ExtensionPoint_ModelElement, gen_behavioral_elements_state_machines_TimeEvent_Event, gen_behavioral_elements_state_machines_CallEvent_Event, gen_behavioral_elements_state_machines_Event_ModelElement, gen_behavioral_elements_state_machines_StateVertex_ModelElement, gen_behavioral_elements_state_machines_State_StateVertex, gen_behavioral_elements_state_machines_ChangeEvent_Event, gen_behavioral_elements_state_machines_Guard_ModelElement, gen_behavioral_elements_state_machines_SignalEvent_Event, gen_behavioral_elements_state_machines_Transition_ModelElement, gen_behavioral_elements_state_machines_CompositeState_State, gen_behavioral_elements_collaborations_ClassifierRole_Classifier, gen_behavioral_elements_state_machines_Pseudostate_StateVertex, gen_behavioral_elements_state_machines_SimpleState_State, gen_behavioral_elements_state_machines_SubmachineState_CompositeState, gen_behavioral_elements_state_machines_SynchState_StateVertex, gen_behavioral_elements_state_machines_StubState_StateVertex, gen_behavioral_elements_state_machines_FinalState_State, gen_behavioral_elements_collaborations_Collaboration_core_GeneralizableElement, gen_behavioral_elements_collaborations_Collaboration_core_Namespace, gen_behavioral_elements_collaborations_Message_ModelElement, gen_behavioral_elements_collaborations_AssociationRole_Association, gen_behavioral_elements_collaborations_AssociationEndRole_AssociationEnd, gen_behavioral_elements_collaborations_CollaborationInstanceSet_ModelElement, gen_behavioral_elements_collaborations_Interaction_ModelElement, gen_behavioral_elements_collaborations_InteractionInstanceSet_ModelElement, gen_behavioral_elements_activity_graphs_ActionState_SimpleState, gen_behavioral_elements_activity_graphs_CallState_ActionState, gen_behavioral_elements_activity_graphs_ObjectFlowState_SimpleState, gen_behavioral_elements_activity_graphs_ActivityGraph_StateMachine, gen_behavioral_elements_activity_graphs_Partition_ModelElement, gen_behavioral_elements_activity_graphs_SubactivityState_SubmachineState, gen_behavioral_elements_activity_graphs_ClassifierInState_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)