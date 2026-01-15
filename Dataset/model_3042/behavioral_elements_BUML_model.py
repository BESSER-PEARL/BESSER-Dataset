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
behavioral_elements_common_behavior_Instance = Class(name="behavioral::elements::common::behavior::Instance", is_abstract=True)
ModelElement = Class(name="ModelElement")
Classifier = Class(name="Classifier")
AttributeLink = Class(name="AttributeLink")
LinkEnd = Class(name="LinkEnd")
ComponentInstance = Class(name="ComponentInstance")
Instance = Class(name="Instance")
Link = Class(name="Link")
behavioral_elements_common_behavior_Signal = Class(name="behavioral::elements::common::behavior::Signal")
Reception = Class(name="Reception")
BehavioralFeature = Class(name="BehavioralFeature")
SendAction = Class(name="SendAction")
SignalEvent = Class(name="SignalEvent")
behavioral_elements_common_behavior_Action = Class(name="behavioral::elements::common::behavior::Action", is_abstract=True)
IterationExpression = Class(name="IterationExpression")
ObjectSetExpression = Class(name="ObjectSetExpression")
ActionExpression = Class(name="ActionExpression")
Argument = Class(name="Argument")
ActionSequence = Class(name="ActionSequence")
Stimulus = Class(name="Stimulus")
Transition = Class(name="Transition")
behavioral_elements_common_behavior_CreateAction = Class(name="behavioral::elements::common::behavior::CreateAction")
Action = Class(name="Action")
behavioral_elements_common_behavior_DestroyAction = Class(name="behavioral::elements::common::behavior::DestroyAction")
behavioral_elements_common_behavior_UninterpretedAction = Class(name="behavioral::elements::common::behavior::UninterpretedAction")
behavioral_elements_common_behavior_AttributeLink = Class(name="behavioral::elements::common::behavior::AttributeLink")
Attribute = Class(name="Attribute")
behavioral_elements_common_behavior_Object = Class(name="behavioral::elements::common::behavior::Object")
behavioral_elements_common_behavior_Link = Class(name="behavioral::elements::common::behavior::Link")
behavioral_elements_common_behavior_LinkObject = Class(name="behavioral::elements::common::behavior::LinkObject")
common_behavior_Object = Class(name="common::behavior::Object")
common_behavior_Link = Class(name="common::behavior::Link")
behavioral_elements_common_behavior_DataValue = Class(name="behavioral::elements::common::behavior::DataValue")
behavioral_elements_common_behavior_CallAction = Class(name="behavioral::elements::common::behavior::CallAction")
Operation = Class(name="Operation")
Signal = Class(name="Signal")
Association = Class(name="Association")
behavioral_elements_common_behavior_ActionSequence = Class(name="behavioral::elements::common::behavior::ActionSequence")
behavioral_elements_common_behavior_Argument = Class(name="behavioral::elements::common::behavior::Argument")
Expression = Class(name="Expression")
behavioral_elements_common_behavior_Reception = Class(name="behavioral::elements::common::behavior::Reception")
behavioral_elements_common_behavior_LinkEnd = Class(name="behavioral::elements::common::behavior::LinkEnd")
AssociationEnd = Class(name="AssociationEnd")
behavioral_elements_common_behavior_ReturnAction = Class(name="behavioral::elements::common::behavior::ReturnAction")
behavioral_elements_common_behavior_TerminateAction = Class(name="behavioral::elements::common::behavior::TerminateAction")
behavioral_elements_common_behavior_Stimulus = Class(name="behavioral::elements::common::behavior::Stimulus")
behavioral_elements_common_behavior_SendAction = Class(name="behavioral::elements::common::behavior::SendAction")
Message = Class(name="Message")
InteractionInstanceSet = Class(name="InteractionInstanceSet")
behavioral_elements_common_behavior_Exception = Class(name="behavioral::elements::common::behavior::Exception")
behavioral_elements_common_behavior_ComponentInstance = Class(name="behavioral::elements::common::behavior::ComponentInstance")
NodeInstance = Class(name="NodeInstance")
behavioral_elements_common_behavior_NodeInstance = Class(name="behavioral::elements::common::behavior::NodeInstance")
behavioral_elements_common_behavior_SubsystemInstance = Class(name="behavioral::elements::common::behavior::SubsystemInstance")
behavioral_elements_use_cases_UseCase = Class(name="behavioral::elements::use::cases::UseCase")
Extend = Class(name="Extend")
Include = Class(name="Include")
ExtensionPoint = Class(name="ExtensionPoint")
behavioral_elements_use_cases_Actor = Class(name="behavioral::elements::use::cases::Actor")
behavioral_elements_use_cases_UseCaseInstance = Class(name="behavioral::elements::use::cases::UseCaseInstance")
behavioral_elements_use_cases_Extend = Class(name="behavioral::elements::use::cases::Extend")
Relationship = Class(name="Relationship")
BooleanExpression = Class(name="BooleanExpression")
UseCase = Class(name="UseCase")
behavioral_elements_use_cases_Include = Class(name="behavioral::elements::use::cases::Include")
behavioral_elements_use_cases_ExtensionPoint = Class(name="behavioral::elements::use::cases::ExtensionPoint")
behavioral_elements_state_machines_StateMachine = Class(name="behavioral::elements::state::machines::StateMachine")
State = Class(name="State")
SubmachineState = Class(name="SubmachineState")
behavioral_elements_state_machines_Event = Class(name="behavioral::elements::state::machines::Event", is_abstract=True)
Parameter_ = Class(name="Parameter")
behavioral_elements_state_machines_StateVertex = Class(name="behavioral::elements::state::machines::StateVertex", is_abstract=True)
CompositeState = Class(name="CompositeState")
behavioral_elements_state_machines_State = Class(name="behavioral::elements::state::machines::State", is_abstract=True)
StateVertex = Class(name="StateVertex")
StateMachine = Class(name="StateMachine")
Event = Class(name="Event")
behavioral_elements_state_machines_TimeEvent = Class(name="behavioral::elements::state::machines::TimeEvent")
TimeExpression = Class(name="TimeExpression")
behavioral_elements_state_machines_CallEvent = Class(name="behavioral::elements::state::machines::CallEvent")
behavioral_elements_state_machines_SignalEvent = Class(name="behavioral::elements::state::machines::SignalEvent")
behavioral_elements_state_machines_Transition = Class(name="behavioral::elements::state::machines::Transition")
Guard = Class(name="Guard")
behavioral_elements_state_machines_CompositeState = Class(name="behavioral::elements::state::machines::CompositeState")
behavioral_elements_state_machines_ChangeEvent = Class(name="behavioral::elements::state::machines::ChangeEvent")
behavioral_elements_state_machines_Guard = Class(name="behavioral::elements::state::machines::Guard")
behavioral_elements_state_machines_Pseudostate = Class(name="behavioral::elements::state::machines::Pseudostate")
behavioral_elements_state_machines_SimpleState = Class(name="behavioral::elements::state::machines::SimpleState")
behavioral_elements_state_machines_SubmachineState = Class(name="behavioral::elements::state::machines::SubmachineState")
behavioral_elements_state_machines_SynchState = Class(name="behavioral::elements::state::machines::SynchState")
behavioral_elements_state_machines_StubState = Class(name="behavioral::elements::state::machines::StubState")
behavioral_elements_state_machines_FinalState = Class(name="behavioral::elements::state::machines::FinalState")
behavioral_elements_collaborations_Collaboration = Class(name="behavioral::elements::collaborations::Collaboration")
core_GeneralizableElement = Class(name="core::GeneralizableElement")
core_Namespace = Class(name="core::Namespace")
Interaction = Class(name="Interaction")
CollaborationInstanceSet = Class(name="CollaborationInstanceSet")
Collaboration = Class(name="Collaboration")
behavioral_elements_collaborations_ClassifierRole = Class(name="behavioral::elements::collaborations::ClassifierRole")
Multiplicity = Class(name="Multiplicity")
Feature = Class(name="Feature")
behavioral_elements_collaborations_AssociationRole = Class(name="behavioral::elements::collaborations::AssociationRole")
behavioral_elements_collaborations_AssociationEndRole = Class(name="behavioral::elements::collaborations::AssociationEndRole")
behavioral_elements_collaborations_Message = Class(name="behavioral::elements::collaborations::Message")
ClassifierRole = Class(name="ClassifierRole")
AssociationRole = Class(name="AssociationRole")
behavioral_elements_collaborations_Interaction = Class(name="behavioral::elements::collaborations::Interaction")
behavioral_elements_collaborations_InteractionInstanceSet = Class(name="behavioral::elements::collaborations::InteractionInstanceSet")
behavioral_elements_collaborations_CollaborationInstanceSet = Class(name="behavioral::elements::collaborations::CollaborationInstanceSet")
behavioral_elements_activity_graphs_ActivityGraph = Class(name="behavioral::elements::activity::graphs::ActivityGraph")
Partition = Class(name="Partition")
behavioral_elements_activity_graphs_Partition = Class(name="behavioral::elements::activity::graphs::Partition")
ActivityGraph = Class(name="ActivityGraph")
behavioral_elements_activity_graphs_SubactivityState = Class(name="behavioral::elements::activity::graphs::SubactivityState")
ArgListsExpression = Class(name="ArgListsExpression")
behavioral_elements_activity_graphs_ActionState = Class(name="behavioral::elements::activity::graphs::ActionState")
SimpleState = Class(name="SimpleState")
behavioral_elements_activity_graphs_CallState = Class(name="behavioral::elements::activity::graphs::CallState")
ActionState = Class(name="ActionState")
behavioral_elements_activity_graphs_ObjectFlowState = Class(name="behavioral::elements::activity::graphs::ObjectFlowState")
behavioral_elements_activity_graphs_ClassifierInState = Class(name="behavioral::elements::activity::graphs::ClassifierInState")

# behavioral_elements_common_behavior_Instance class attributes and methods

# ModelElement class attributes and methods

# Classifier class attributes and methods

# AttributeLink class attributes and methods

# LinkEnd class attributes and methods

# ComponentInstance class attributes and methods

# Instance class attributes and methods

# Link class attributes and methods

# behavioral_elements_common_behavior_Signal class attributes and methods

# Reception class attributes and methods

# BehavioralFeature class attributes and methods

# SendAction class attributes and methods

# SignalEvent class attributes and methods

# behavioral_elements_common_behavior_Action class attributes and methods
behavioral_elements_common_behavior_Action_isAsynchronous: Property = Property(name="isAsynchronous", type=StringType)
behavioral_elements_common_behavior_Action.attributes={behavioral_elements_common_behavior_Action_isAsynchronous}

# IterationExpression class attributes and methods

# ObjectSetExpression class attributes and methods

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

# behavioral_elements_common_behavior_Object class attributes and methods

# behavioral_elements_common_behavior_Link class attributes and methods

# behavioral_elements_common_behavior_LinkObject class attributes and methods

# common_behavior_Object class attributes and methods

# common_behavior_Link class attributes and methods

# behavioral_elements_common_behavior_DataValue class attributes and methods

# behavioral_elements_common_behavior_CallAction class attributes and methods

# Operation class attributes and methods

# Signal class attributes and methods

# Association class attributes and methods

# behavioral_elements_common_behavior_ActionSequence class attributes and methods

# behavioral_elements_common_behavior_Argument class attributes and methods

# Expression class attributes and methods

# behavioral_elements_common_behavior_Reception class attributes and methods
behavioral_elements_common_behavior_Reception_specification: Property = Property(name="specification", type=StringType)
behavioral_elements_common_behavior_Reception_isRoot: Property = Property(name="isRoot", type=StringType)
behavioral_elements_common_behavior_Reception_isLeaf: Property = Property(name="isLeaf", type=StringType)
behavioral_elements_common_behavior_Reception_isAbstract: Property = Property(name="isAbstract", type=StringType)
behavioral_elements_common_behavior_Reception.attributes={behavioral_elements_common_behavior_Reception_isLeaf, behavioral_elements_common_behavior_Reception_isAbstract, behavioral_elements_common_behavior_Reception_specification, behavioral_elements_common_behavior_Reception_isRoot}

# behavioral_elements_common_behavior_LinkEnd class attributes and methods

# AssociationEnd class attributes and methods

# behavioral_elements_common_behavior_ReturnAction class attributes and methods

# behavioral_elements_common_behavior_TerminateAction class attributes and methods

# behavioral_elements_common_behavior_Stimulus class attributes and methods

# behavioral_elements_common_behavior_SendAction class attributes and methods

# Message class attributes and methods

# InteractionInstanceSet class attributes and methods

# behavioral_elements_common_behavior_Exception class attributes and methods

# behavioral_elements_common_behavior_ComponentInstance class attributes and methods

# NodeInstance class attributes and methods

# behavioral_elements_common_behavior_NodeInstance class attributes and methods

# behavioral_elements_common_behavior_SubsystemInstance class attributes and methods

# behavioral_elements_use_cases_UseCase class attributes and methods

# Extend class attributes and methods

# Include class attributes and methods

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

# behavioral_elements_state_machines_StateMachine class attributes and methods

# State class attributes and methods

# SubmachineState class attributes and methods

# behavioral_elements_state_machines_Event class attributes and methods

# Parameter class attributes and methods

# behavioral_elements_state_machines_StateVertex class attributes and methods

# CompositeState class attributes and methods

# behavioral_elements_state_machines_State class attributes and methods

# StateVertex class attributes and methods

# StateMachine class attributes and methods

# Event class attributes and methods

# behavioral_elements_state_machines_TimeEvent class attributes and methods

# TimeExpression class attributes and methods

# behavioral_elements_state_machines_CallEvent class attributes and methods

# behavioral_elements_state_machines_SignalEvent class attributes and methods

# behavioral_elements_state_machines_Transition class attributes and methods

# Guard class attributes and methods

# behavioral_elements_state_machines_CompositeState class attributes and methods
behavioral_elements_state_machines_CompositeState_isConcurrent: Property = Property(name="isConcurrent", type=StringType)
behavioral_elements_state_machines_CompositeState.attributes={behavioral_elements_state_machines_CompositeState_isConcurrent}

# behavioral_elements_state_machines_ChangeEvent class attributes and methods

# behavioral_elements_state_machines_Guard class attributes and methods

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

# CollaborationInstanceSet class attributes and methods

# Collaboration class attributes and methods

# behavioral_elements_collaborations_ClassifierRole class attributes and methods

# Multiplicity class attributes and methods

# Feature class attributes and methods

# behavioral_elements_collaborations_AssociationRole class attributes and methods

# behavioral_elements_collaborations_AssociationEndRole class attributes and methods

# behavioral_elements_collaborations_Message class attributes and methods

# ClassifierRole class attributes and methods

# AssociationRole class attributes and methods

# behavioral_elements_collaborations_Interaction class attributes and methods

# behavioral_elements_collaborations_InteractionInstanceSet class attributes and methods

# behavioral_elements_collaborations_CollaborationInstanceSet class attributes and methods

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

# SimpleState class attributes and methods

# behavioral_elements_activity_graphs_CallState class attributes and methods

# ActionState class attributes and methods

# behavioral_elements_activity_graphs_ObjectFlowState class attributes and methods
behavioral_elements_activity_graphs_ObjectFlowState_isSynch: Property = Property(name="isSynch", type=StringType)
behavioral_elements_activity_graphs_ObjectFlowState.attributes={behavioral_elements_activity_graphs_ObjectFlowState_isSynch}

# behavioral_elements_activity_graphs_ClassifierInState class attributes and methods

# Relationships
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
        Property(name="common_behavior", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="AttributeLink", type=AttributeLink, multiplicity=Multiplicity(0, 9999))
    }
)
linkEnd2: BinaryAssociation = BinaryAssociation(
    name="linkEnd2",
    ends={
        Property(name="common_behavior3", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkEnd", type=LinkEnd, multiplicity=Multiplicity(0, 9999))
    }
)
slot4: BinaryAssociation = BinaryAssociation(
    name="slot4",
    ends={
        Property(name="common_behavior6", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="AttributeLink5", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentInstance7: BinaryAssociation = BinaryAssociation(
    name="componentInstance7",
    ends={
        Property(name="common_behavior8", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentInstance", type=ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)
ownedInstance9: BinaryAssociation = BinaryAssociation(
    name="ownedInstance9",
    ends={
        Property(name="Instance", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Instance10", type=Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLink11: BinaryAssociation = BinaryAssociation(
    name="ownedLink11",
    ends={
        Property(name="Link", type=behavioral_elements_common_behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Instance12", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reception13: BinaryAssociation = BinaryAssociation(
    name="reception13",
    ends={
        Property(name="common_behavior14", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="Reception", type=Reception, multiplicity=Multiplicity(0, 9999))
    }
)
context15: BinaryAssociation = BinaryAssociation(
    name="context15",
    ends={
        Property(name="foundation.ecorecore", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="BehavioralFeature", type=BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
sendAction16: BinaryAssociation = BinaryAssociation(
    name="sendAction16",
    ends={
        Property(name="common_behavior17", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="SendAction", type=SendAction, multiplicity=Multiplicity(0, 9999))
    }
)
occurrence18: BinaryAssociation = BinaryAssociation(
    name="occurrence18",
    ends={
        Property(name="state_machines", type=behavioral_elements_common_behavior_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="SignalEvent", type=SignalEvent, multiplicity=Multiplicity(0, 9999))
    }
)
recurrence19: BinaryAssociation = BinaryAssociation(
    name="recurrence19",
    ends={
        Property(name="IterationExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action", type=IterationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script22: BinaryAssociation = BinaryAssociation(
    name="script22",
    ends={
        Property(name="ActionExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action23", type=ActionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualArgument24: BinaryAssociation = BinaryAssociation(
    name="actualArgument24",
    ends={
        Property(name="common_behavior25", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Argument", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionSequence26: BinaryAssociation = BinaryAssociation(
    name="actionSequence26",
    ends={
        Property(name="common_behavior27", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionSequence", type=ActionSequence, multiplicity=Multiplicity(0, 1))
    }
)
stimulus28: BinaryAssociation = BinaryAssociation(
    name="stimulus28",
    ends={
        Property(name="common_behavior29", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Stimulus", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="ObjectSetExpression", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Action21", type=ObjectSetExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition30: BinaryAssociation = BinaryAssociation(
    name="transition30",
    ends={
        Property(name="state_machines31", type=behavioral_elements_common_behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
instantiation32: BinaryAssociation = BinaryAssociation(
    name="instantiation32",
    ends={
        Property(name="foundation.ecorecore34", type=behavioral_elements_common_behavior_CreateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier33", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
attribute35: BinaryAssociation = BinaryAssociation(
    name="attribute35",
    ends={
        Property(name="Attribute", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_AttributeLink", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
value36: BinaryAssociation = BinaryAssociation(
    name="value36",
    ends={
        Property(name="common_behavior38", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance37", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
instance39: BinaryAssociation = BinaryAssociation(
    name="instance39",
    ends={
        Property(name="common_behavior41", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance40", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
linkEnd42: BinaryAssociation = BinaryAssociation(
    name="linkEnd42",
    ends={
        Property(name="common_behavior44", type=behavioral_elements_common_behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkEnd43", type=LinkEnd, multiplicity=Multiplicity(0, 1))
    }
)
association45: BinaryAssociation = BinaryAssociation(
    name="association45",
    ends={
        Property(name="Association", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Link", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
connection46: BinaryAssociation = BinaryAssociation(
    name="connection46",
    ends={
        Property(name="common_behavior48", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkEnd47", type=LinkEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
stimulus49: BinaryAssociation = BinaryAssociation(
    name="stimulus49",
    ends={
        Property(name="common_behavior51", type=behavioral_elements_common_behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="Stimulus50", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
signal54: BinaryAssociation = BinaryAssociation(
    name="signal54",
    ends={
        Property(name="common_behavior55", type=behavioral_elements_common_behavior_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Signal", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
action56: BinaryAssociation = BinaryAssociation(
    name="action56",
    ends={
        Property(name="common_behavior57", type=behavioral_elements_common_behavior_ActionSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="Action", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="Expression", type=behavioral_elements_common_behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Argument", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action59: BinaryAssociation = BinaryAssociation(
    name="action59",
    ends={
        Property(name="common_behavior61", type=behavioral_elements_common_behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="Action60", type=Action, multiplicity=Multiplicity(0, 1))
    }
)
signal62: BinaryAssociation = BinaryAssociation(
    name="signal62",
    ends={
        Property(name="common_behavior64", type=behavioral_elements_common_behavior_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="Signal63", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
instance65: BinaryAssociation = BinaryAssociation(
    name="instance65",
    ends={
        Property(name="common_behavior67", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance66", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
link68: BinaryAssociation = BinaryAssociation(
    name="link68",
    ends={
        Property(name="common_behavior70", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Link69", type=Link, multiplicity=Multiplicity(1, 1))
    }
)
associationEnd71: BinaryAssociation = BinaryAssociation(
    name="associationEnd71",
    ends={
        Property(name="AssociationEnd", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_LinkEnd", type=AssociationEnd, multiplicity=Multiplicity(1, 1))
    }
)
qualifiedValue72: BinaryAssociation = BinaryAssociation(
    name="qualifiedValue72",
    ends={
        Property(name="common_behavior74", type=behavioral_elements_common_behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="AttributeLink73", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument75: BinaryAssociation = BinaryAssociation(
    name="argument75",
    ends={
        Property(name="Instance76", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
sender77: BinaryAssociation = BinaryAssociation(
    name="sender77",
    ends={
        Property(name="Instance79", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus78", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
operation52: BinaryAssociation = BinaryAssociation(
    name="operation52",
    ends={
        Property(name="foundation.ecorecore53", type=behavioral_elements_common_behavior_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
receiver80: BinaryAssociation = BinaryAssociation(
    name="receiver80",
    ends={
        Property(name="Instance82", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_common_behavior_Stimulus81", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
communicationLink83: BinaryAssociation = BinaryAssociation(
    name="communicationLink83",
    ends={
        Property(name="common_behavior85", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="Link84", type=Link, multiplicity=Multiplicity(0, 1))
    }
)
dispatchAction86: BinaryAssociation = BinaryAssociation(
    name="dispatchAction86",
    ends={
        Property(name="common_behavior88", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="Action87", type=Action, multiplicity=Multiplicity(1, 1))
    }
)
playedRole89: BinaryAssociation = BinaryAssociation(
    name="playedRole89",
    ends={
        Property(name="collaborations", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="Message", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
interactionInstanceSet90: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet90",
    ends={
        Property(name="collaborations91", type=behavioral_elements_common_behavior_Stimulus, multiplicity=Multiplicity(1, 1)),
        Property(name="InteractionInstanceSet", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
nodeInstance92: BinaryAssociation = BinaryAssociation(
    name="nodeInstance92",
    ends={
        Property(name="common_behavior93", type=behavioral_elements_common_behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="NodeInstance", type=NodeInstance, multiplicity=Multiplicity(0, 1))
    }
)
resident94: BinaryAssociation = BinaryAssociation(
    name="resident94",
    ends={
        Property(name="common_behavior96", type=behavioral_elements_common_behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance95", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
resident97: BinaryAssociation = BinaryAssociation(
    name="resident97",
    ends={
        Property(name="common_behavior99", type=behavioral_elements_common_behavior_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentInstance98", type=ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
extender100: BinaryAssociation = BinaryAssociation(
    name="extender100",
    ends={
        Property(name="use_cases", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Extend", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
extend101: BinaryAssociation = BinaryAssociation(
    name="extend101",
    ends={
        Property(name="use_cases103", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Extend102", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
includer104: BinaryAssociation = BinaryAssociation(
    name="includer104",
    ends={
        Property(name="use_cases105", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Include", type=Include, multiplicity=Multiplicity(0, 9999))
    }
)
include106: BinaryAssociation = BinaryAssociation(
    name="include106",
    ends={
        Property(name="use_cases108", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Include107", type=Include, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint109: BinaryAssociation = BinaryAssociation(
    name="extensionPoint109",
    ends={
        Property(name="use_cases110", type=behavioral_elements_use_cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ExtensionPoint", type=ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition111: BinaryAssociation = BinaryAssociation(
    name="condition111",
    ends={
        Property(name="BooleanExpression", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_use_cases_Extend", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base112: BinaryAssociation = BinaryAssociation(
    name="base112",
    ends={
        Property(name="use_cases113", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension114: BinaryAssociation = BinaryAssociation(
    name="extension114",
    ends={
        Property(name="use_cases116", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase115", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoint117: BinaryAssociation = BinaryAssociation(
    name="extensionPoint117",
    ends={
        Property(name="use_cases119", type=behavioral_elements_use_cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="ExtensionPoint118", type=ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
addition120: BinaryAssociation = BinaryAssociation(
    name="addition120",
    ends={
        Property(name="use_cases122", type=behavioral_elements_use_cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase121", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base123: BinaryAssociation = BinaryAssociation(
    name="base123",
    ends={
        Property(name="use_cases125", type=behavioral_elements_use_cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase124", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase126: BinaryAssociation = BinaryAssociation(
    name="useCase126",
    ends={
        Property(name="use_cases128", type=behavioral_elements_use_cases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase127", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extend129: BinaryAssociation = BinaryAssociation(
    name="extend129",
    ends={
        Property(name="use_cases131", type=behavioral_elements_use_cases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="Extend130", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
context132: BinaryAssociation = BinaryAssociation(
    name="context132",
    ends={
        Property(name="foundation.ecorecore133", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
top134: BinaryAssociation = BinaryAssociation(
    name="top134",
    ends={
        Property(name="state_machines135", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions136: BinaryAssociation = BinaryAssociation(
    name="transitions136",
    ends={
        Property(name="state_machines138", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition137", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachineState139: BinaryAssociation = BinaryAssociation(
    name="submachineState139",
    ends={
        Property(name="state_machines140", type=behavioral_elements_state_machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SubmachineState", type=SubmachineState, multiplicity=Multiplicity(0, 9999))
    }
)
parameter141: BinaryAssociation = BinaryAssociation(
    name="parameter141",
    ends={
        Property(name="Parameter", type=behavioral_elements_state_machines_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_Event", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition142: BinaryAssociation = BinaryAssociation(
    name="transition142",
    ends={
        Property(name="state_machines144", type=behavioral_elements_state_machines_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition143", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container145: BinaryAssociation = BinaryAssociation(
    name="container145",
    ends={
        Property(name="state_machines146", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeState", type=CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
outgoing147: BinaryAssociation = BinaryAssociation(
    name="outgoing147",
    ends={
        Property(name="state_machines149", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition148", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming150: BinaryAssociation = BinaryAssociation(
    name="incoming150",
    ends={
        Property(name="state_machines152", type=behavioral_elements_state_machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition151", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry153: BinaryAssociation = BinaryAssociation(
    name="entry153",
    ends={
        Property(name="Action154", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit155: BinaryAssociation = BinaryAssociation(
    name="exit155",
    ends={
        Property(name="Action157", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State156", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine158: BinaryAssociation = BinaryAssociation(
    name="stateMachine158",
    ends={
        Property(name="state_machines159", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
deferrableEvent160: BinaryAssociation = BinaryAssociation(
    name="deferrableEvent160",
    ends={
        Property(name="Event", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State161", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
internalTransition162: BinaryAssociation = BinaryAssociation(
    name="internalTransition162",
    ends={
        Property(name="state_machines164", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition163", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity165: BinaryAssociation = BinaryAssociation(
    name="doActivity165",
    ends={
        Property(name="Action167", type=behavioral_elements_state_machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_State166", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when168: BinaryAssociation = BinaryAssociation(
    name="when168",
    ends={
        Property(name="TimeExpression", type=behavioral_elements_state_machines_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_TimeEvent", type=TimeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation169: BinaryAssociation = BinaryAssociation(
    name="operation169",
    ends={
        Property(name="foundation.ecorecore171", type=behavioral_elements_state_machines_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation170", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal172: BinaryAssociation = BinaryAssociation(
    name="signal172",
    ends={
        Property(name="common_behavior174", type=behavioral_elements_state_machines_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="Signal173", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
guard175: BinaryAssociation = BinaryAssociation(
    name="guard175",
    ends={
        Property(name="state_machines176", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Guard", type=Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect177: BinaryAssociation = BinaryAssociation(
    name="effect177",
    ends={
        Property(name="common_behavior179", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Action178", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state180: BinaryAssociation = BinaryAssociation(
    name="state180",
    ends={
        Property(name="state_machines182", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State181", type=State, multiplicity=Multiplicity(0, 1))
    }
)
trigger183: BinaryAssociation = BinaryAssociation(
    name="trigger183",
    ends={
        Property(name="state_machines185", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Event184", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine186: BinaryAssociation = BinaryAssociation(
    name="stateMachine186",
    ends={
        Property(name="state_machines188", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine187", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source189: BinaryAssociation = BinaryAssociation(
    name="source189",
    ends={
        Property(name="state_machines190", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateVertex", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target191: BinaryAssociation = BinaryAssociation(
    name="target191",
    ends={
        Property(name="state_machines193", type=behavioral_elements_state_machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateVertex192", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
subvertex194: BinaryAssociation = BinaryAssociation(
    name="subvertex194",
    ends={
        Property(name="state_machines196", type=behavioral_elements_state_machines_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="StateVertex195", type=StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeExpression197: BinaryAssociation = BinaryAssociation(
    name="changeExpression197",
    ends={
        Property(name="BooleanExpression198", type=behavioral_elements_state_machines_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_ChangeEvent", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression199: BinaryAssociation = BinaryAssociation(
    name="expression199",
    ends={
        Property(name="BooleanExpression200", type=behavioral_elements_state_machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_state_machines_Guard", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition201: BinaryAssociation = BinaryAssociation(
    name="transition201",
    ends={
        Property(name="state_machines203", type=behavioral_elements_state_machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition202", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
submachine204: BinaryAssociation = BinaryAssociation(
    name="submachine204",
    ends={
        Property(name="state_machines206", type=behavioral_elements_state_machines_SubmachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine205", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
interaction207: BinaryAssociation = BinaryAssociation(
    name="interaction207",
    ends={
        Property(name="collaborations208", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="Interaction", type=Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representedOperation209: BinaryAssociation = BinaryAssociation(
    name="representedOperation209",
    ends={
        Property(name="foundation.ecorecore211", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation210", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
constrainingElement212: BinaryAssociation = BinaryAssociation(
    name="constrainingElement212",
    ends={
        Property(name="ModelElement213", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Collaboration", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationInstanceSet214: BinaryAssociation = BinaryAssociation(
    name="collaborationInstanceSet214",
    ends={
        Property(name="collaborations215", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="CollaborationInstanceSet", type=CollaborationInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
usedCollaboration216: BinaryAssociation = BinaryAssociation(
    name="usedCollaboration216",
    ends={
        Property(name="Collaboration", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Collaboration217", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
representedClassifier218: BinaryAssociation = BinaryAssociation(
    name="representedClassifier218",
    ends={
        Property(name="foundation.ecorecore220", type=behavioral_elements_collaborations_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier219", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity221: BinaryAssociation = BinaryAssociation(
    name="multiplicity221",
    ends={
        Property(name="Multiplicity", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base222: BinaryAssociation = BinaryAssociation(
    name="base222",
    ends={
        Property(name="Classifier224", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole223", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
availableFeature225: BinaryAssociation = BinaryAssociation(
    name="availableFeature225",
    ends={
        Property(name="Feature", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole226", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
availableContents227: BinaryAssociation = BinaryAssociation(
    name="availableContents227",
    ends={
        Property(name="ModelElement229", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole228", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
conformingInstance230: BinaryAssociation = BinaryAssociation(
    name="conformingInstance230",
    ends={
        Property(name="Instance232", type=behavioral_elements_collaborations_ClassifierRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_ClassifierRole231", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity233: BinaryAssociation = BinaryAssociation(
    name="multiplicity233",
    ends={
        Property(name="Multiplicity234", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base235: BinaryAssociation = BinaryAssociation(
    name="base235",
    ends={
        Property(name="Association237", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole236", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
message238: BinaryAssociation = BinaryAssociation(
    name="message238",
    ends={
        Property(name="collaborations240", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="Message239", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
conformingLink241: BinaryAssociation = BinaryAssociation(
    name="conformingLink241",
    ends={
        Property(name="Link243", type=behavioral_elements_collaborations_AssociationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationRole242", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationMultiplicity244: BinaryAssociation = BinaryAssociation(
    name="collaborationMultiplicity244",
    ends={
        Property(name="Multiplicity245", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationEndRole", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base246: BinaryAssociation = BinaryAssociation(
    name="base246",
    ends={
        Property(name="AssociationEnd248", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_AssociationEndRole247", type=AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
availableQualifier249: BinaryAssociation = BinaryAssociation(
    name="availableQualifier249",
    ends={
        Property(name="foundation.ecorecore251", type=behavioral_elements_collaborations_AssociationEndRole, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute250", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
interaction252: BinaryAssociation = BinaryAssociation(
    name="interaction252",
    ends={
        Property(name="collaborations254", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="Interaction253", type=Interaction, multiplicity=Multiplicity(1, 1))
    }
)
activator255: BinaryAssociation = BinaryAssociation(
    name="activator255",
    ends={
        Property(name="Message256", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
sender257: BinaryAssociation = BinaryAssociation(
    name="sender257",
    ends={
        Property(name="ClassifierRole", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message258", type=ClassifierRole, multiplicity=Multiplicity(1, 1))
    }
)
receiver259: BinaryAssociation = BinaryAssociation(
    name="receiver259",
    ends={
        Property(name="ClassifierRole261", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message260", type=ClassifierRole, multiplicity=Multiplicity(1, 1))
    }
)
predecessor262: BinaryAssociation = BinaryAssociation(
    name="predecessor262",
    ends={
        Property(name="collaborations264", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="Message263", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
successor265: BinaryAssociation = BinaryAssociation(
    name="successor265",
    ends={
        Property(name="collaborations267", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="Message266", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
communicationConnection268: BinaryAssociation = BinaryAssociation(
    name="communicationConnection268",
    ends={
        Property(name="collaborations269", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationRole", type=AssociationRole, multiplicity=Multiplicity(0, 1))
    }
)
action270: BinaryAssociation = BinaryAssociation(
    name="action270",
    ends={
        Property(name="Action272", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_Message271", type=Action, multiplicity=Multiplicity(1, 1))
    }
)
conformingStimulus273: BinaryAssociation = BinaryAssociation(
    name="conformingStimulus273",
    ends={
        Property(name="common_behavior275", type=behavioral_elements_collaborations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="Stimulus274", type=Stimulus, multiplicity=Multiplicity(0, 9999))
    }
)
message276: BinaryAssociation = BinaryAssociation(
    name="message276",
    ends={
        Property(name="collaborations278", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="Message277", type=Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
context279: BinaryAssociation = BinaryAssociation(
    name="context279",
    ends={
        Property(name="collaborations281", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="Collaboration280", type=Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
interactionInstanceSet282: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet282",
    ends={
        Property(name="collaborations284", type=behavioral_elements_collaborations_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="InteractionInstanceSet283", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999))
    }
)
context285: BinaryAssociation = BinaryAssociation(
    name="context285",
    ends={
        Property(name="collaborations287", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CollaborationInstanceSet286", type=CollaborationInstanceSet, multiplicity=Multiplicity(1, 1))
    }
)
interaction288: BinaryAssociation = BinaryAssociation(
    name="interaction288",
    ends={
        Property(name="collaborations290", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Interaction289", type=Interaction, multiplicity=Multiplicity(0, 1))
    }
)
participatingStimulus291: BinaryAssociation = BinaryAssociation(
    name="participatingStimulus291",
    ends={
        Property(name="common_behavior293", type=behavioral_elements_collaborations_InteractionInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Stimulus292", type=Stimulus, multiplicity=Multiplicity(1, 9999))
    }
)
interactionInstanceSet294: BinaryAssociation = BinaryAssociation(
    name="interactionInstanceSet294",
    ends={
        Property(name="collaborations296", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="InteractionInstanceSet295", type=InteractionInstanceSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration297: BinaryAssociation = BinaryAssociation(
    name="collaboration297",
    ends={
        Property(name="collaborations299", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Collaboration298", type=Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
participatingInstance300: BinaryAssociation = BinaryAssociation(
    name="participatingInstance300",
    ends={
        Property(name="Instance301", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet", type=Instance, multiplicity=Multiplicity(1, 9999))
    }
)
participatingLink302: BinaryAssociation = BinaryAssociation(
    name="participatingLink302",
    ends={
        Property(name="Link304", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet303", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingElement305: BinaryAssociation = BinaryAssociation(
    name="constrainingElement305",
    ends={
        Property(name="ModelElement307", type=behavioral_elements_collaborations_CollaborationInstanceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_collaborations_CollaborationInstanceSet306", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
partition308: BinaryAssociation = BinaryAssociation(
    name="partition308",
    ends={
        Property(name="activity_graphs", type=behavioral_elements_activity_graphs_ActivityGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="Partition", type=Partition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents309: BinaryAssociation = BinaryAssociation(
    name="contents309",
    ends={
        Property(name="ModelElement310", type=behavioral_elements_activity_graphs_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_Partition", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
activityGraph311: BinaryAssociation = BinaryAssociation(
    name="activityGraph311",
    ends={
        Property(name="activity_graphs312", type=behavioral_elements_activity_graphs_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGraph", type=ActivityGraph, multiplicity=Multiplicity(1, 1))
    }
)
dynamicArguments313: BinaryAssociation = BinaryAssociation(
    name="dynamicArguments313",
    ends={
        Property(name="ArgListsExpression", type=behavioral_elements_activity_graphs_SubactivityState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_SubactivityState", type=ArgListsExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicMultiplicity314: BinaryAssociation = BinaryAssociation(
    name="dynamicMultiplicity314",
    ends={
        Property(name="Multiplicity316", type=behavioral_elements_activity_graphs_SubactivityState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_SubactivityState315", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicArguments317: BinaryAssociation = BinaryAssociation(
    name="dynamicArguments317",
    ends={
        Property(name="ArgListsExpression318", type=behavioral_elements_activity_graphs_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ActionState", type=ArgListsExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicMultiplicity319: BinaryAssociation = BinaryAssociation(
    name="dynamicMultiplicity319",
    ends={
        Property(name="Multiplicity321", type=behavioral_elements_activity_graphs_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ActionState320", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter322: BinaryAssociation = BinaryAssociation(
    name="parameter322",
    ends={
        Property(name="Parameter323", type=behavioral_elements_activity_graphs_ObjectFlowState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ObjectFlowState", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
type324: BinaryAssociation = BinaryAssociation(
    name="type324",
    ends={
        Property(name="Classifier326", type=behavioral_elements_activity_graphs_ObjectFlowState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ObjectFlowState325", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
type327: BinaryAssociation = BinaryAssociation(
    name="type327",
    ends={
        Property(name="Classifier328", type=behavioral_elements_activity_graphs_ClassifierInState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ClassifierInState", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
inState329: BinaryAssociation = BinaryAssociation(
    name="inState329",
    ends={
        Property(name="State331", type=behavioral_elements_activity_graphs_ClassifierInState, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_elements_activity_graphs_ClassifierInState330", type=State, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_behavioral_elements_common_behavior_Instance_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Instance)
gen_behavioral_elements_common_behavior_Signal_Classifier = Generalization(general=Classifier, specific=behavioral_elements_common_behavior_Signal)
gen_behavioral_elements_common_behavior_Action_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Action)
gen_behavioral_elements_common_behavior_CreateAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_CreateAction)
gen_behavioral_elements_common_behavior_DestroyAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_DestroyAction)
gen_behavioral_elements_common_behavior_UninterpretedAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_UninterpretedAction)
gen_behavioral_elements_common_behavior_AttributeLink_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_AttributeLink)
gen_behavioral_elements_common_behavior_Object_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_Object)
gen_behavioral_elements_common_behavior_Link_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Link)
gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Object = Generalization(general=common_behavior_Object, specific=behavioral_elements_common_behavior_LinkObject)
gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Link = Generalization(general=common_behavior_Link, specific=behavioral_elements_common_behavior_LinkObject)
gen_behavioral_elements_common_behavior_DataValue_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_DataValue)
gen_behavioral_elements_common_behavior_CallAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_CallAction)
gen_behavioral_elements_common_behavior_SendAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_SendAction)
gen_behavioral_elements_common_behavior_ActionSequence_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_ActionSequence)
gen_behavioral_elements_common_behavior_Argument_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Argument)
gen_behavioral_elements_common_behavior_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=behavioral_elements_common_behavior_Reception)
gen_behavioral_elements_common_behavior_LinkEnd_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_LinkEnd)
gen_behavioral_elements_common_behavior_ReturnAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_ReturnAction)
gen_behavioral_elements_common_behavior_TerminateAction_Action = Generalization(general=Action, specific=behavioral_elements_common_behavior_TerminateAction)
gen_behavioral_elements_common_behavior_Stimulus_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_common_behavior_Stimulus)
gen_behavioral_elements_common_behavior_Exception_Signal = Generalization(general=Signal, specific=behavioral_elements_common_behavior_Exception)
gen_behavioral_elements_common_behavior_ComponentInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_ComponentInstance)
gen_behavioral_elements_common_behavior_NodeInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_NodeInstance)
gen_behavioral_elements_common_behavior_SubsystemInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_common_behavior_SubsystemInstance)
gen_behavioral_elements_use_cases_UseCase_Classifier = Generalization(general=Classifier, specific=behavioral_elements_use_cases_UseCase)
gen_behavioral_elements_use_cases_Actor_Classifier = Generalization(general=Classifier, specific=behavioral_elements_use_cases_Actor)
gen_behavioral_elements_use_cases_UseCaseInstance_Instance = Generalization(general=Instance, specific=behavioral_elements_use_cases_UseCaseInstance)
gen_behavioral_elements_use_cases_Extend_Relationship = Generalization(general=Relationship, specific=behavioral_elements_use_cases_Extend)
gen_behavioral_elements_use_cases_Include_Relationship = Generalization(general=Relationship, specific=behavioral_elements_use_cases_Include)
gen_behavioral_elements_use_cases_ExtensionPoint_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_use_cases_ExtensionPoint)
gen_behavioral_elements_state_machines_StateMachine_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_StateMachine)
gen_behavioral_elements_state_machines_Event_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Event)
gen_behavioral_elements_state_machines_StateVertex_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_StateVertex)
gen_behavioral_elements_state_machines_State_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_State)
gen_behavioral_elements_state_machines_TimeEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_TimeEvent)
gen_behavioral_elements_state_machines_CallEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_CallEvent)
gen_behavioral_elements_state_machines_SignalEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_SignalEvent)
gen_behavioral_elements_state_machines_Transition_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Transition)
gen_behavioral_elements_state_machines_CompositeState_State = Generalization(general=State, specific=behavioral_elements_state_machines_CompositeState)
gen_behavioral_elements_state_machines_ChangeEvent_Event = Generalization(general=Event, specific=behavioral_elements_state_machines_ChangeEvent)
gen_behavioral_elements_state_machines_Guard_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_state_machines_Guard)
gen_behavioral_elements_state_machines_Pseudostate_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_Pseudostate)
gen_behavioral_elements_state_machines_SimpleState_State = Generalization(general=State, specific=behavioral_elements_state_machines_SimpleState)
gen_behavioral_elements_state_machines_SubmachineState_CompositeState = Generalization(general=CompositeState, specific=behavioral_elements_state_machines_SubmachineState)
gen_behavioral_elements_state_machines_SynchState_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_SynchState)
gen_behavioral_elements_state_machines_StubState_StateVertex = Generalization(general=StateVertex, specific=behavioral_elements_state_machines_StubState)
gen_behavioral_elements_state_machines_FinalState_State = Generalization(general=State, specific=behavioral_elements_state_machines_FinalState)
gen_behavioral_elements_collaborations_Collaboration_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=behavioral_elements_collaborations_Collaboration)
gen_behavioral_elements_collaborations_Collaboration_core_Namespace = Generalization(general=core_Namespace, specific=behavioral_elements_collaborations_Collaboration)
gen_behavioral_elements_collaborations_ClassifierRole_Classifier = Generalization(general=Classifier, specific=behavioral_elements_collaborations_ClassifierRole)
gen_behavioral_elements_collaborations_AssociationRole_Association = Generalization(general=Association, specific=behavioral_elements_collaborations_AssociationRole)
gen_behavioral_elements_collaborations_AssociationEndRole_AssociationEnd = Generalization(general=AssociationEnd, specific=behavioral_elements_collaborations_AssociationEndRole)
gen_behavioral_elements_collaborations_Message_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_Message)
gen_behavioral_elements_collaborations_Interaction_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_Interaction)
gen_behavioral_elements_collaborations_InteractionInstanceSet_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_InteractionInstanceSet)
gen_behavioral_elements_collaborations_CollaborationInstanceSet_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_collaborations_CollaborationInstanceSet)
gen_behavioral_elements_activity_graphs_ActivityGraph_StateMachine = Generalization(general=StateMachine, specific=behavioral_elements_activity_graphs_ActivityGraph)
gen_behavioral_elements_activity_graphs_Partition_ModelElement = Generalization(general=ModelElement, specific=behavioral_elements_activity_graphs_Partition)
gen_behavioral_elements_activity_graphs_SubactivityState_SubmachineState = Generalization(general=SubmachineState, specific=behavioral_elements_activity_graphs_SubactivityState)
gen_behavioral_elements_activity_graphs_ActionState_SimpleState = Generalization(general=SimpleState, specific=behavioral_elements_activity_graphs_ActionState)
gen_behavioral_elements_activity_graphs_CallState_ActionState = Generalization(general=ActionState, specific=behavioral_elements_activity_graphs_CallState)
gen_behavioral_elements_activity_graphs_ObjectFlowState_SimpleState = Generalization(general=SimpleState, specific=behavioral_elements_activity_graphs_ObjectFlowState)
gen_behavioral_elements_activity_graphs_ClassifierInState_Classifier = Generalization(general=Classifier, specific=behavioral_elements_activity_graphs_ClassifierInState)

# Domain Model
domain_model = DomainModel(
    name="behavioral_elements",
    types={behavioral_elements_common_behavior_Instance, ModelElement, Classifier, AttributeLink, LinkEnd, ComponentInstance, Instance, Link, behavioral_elements_common_behavior_Signal, Reception, BehavioralFeature, SendAction, SignalEvent, behavioral_elements_common_behavior_Action, IterationExpression, ObjectSetExpression, ActionExpression, Argument, ActionSequence, Stimulus, Transition, behavioral_elements_common_behavior_CreateAction, Action, behavioral_elements_common_behavior_DestroyAction, behavioral_elements_common_behavior_UninterpretedAction, behavioral_elements_common_behavior_AttributeLink, Attribute, behavioral_elements_common_behavior_Object, behavioral_elements_common_behavior_Link, behavioral_elements_common_behavior_LinkObject, common_behavior_Object, common_behavior_Link, behavioral_elements_common_behavior_DataValue, behavioral_elements_common_behavior_CallAction, Operation, Signal, Association, behavioral_elements_common_behavior_ActionSequence, behavioral_elements_common_behavior_Argument, Expression, behavioral_elements_common_behavior_Reception, behavioral_elements_common_behavior_LinkEnd, AssociationEnd, behavioral_elements_common_behavior_ReturnAction, behavioral_elements_common_behavior_TerminateAction, behavioral_elements_common_behavior_Stimulus, behavioral_elements_common_behavior_SendAction, Message, InteractionInstanceSet, behavioral_elements_common_behavior_Exception, behavioral_elements_common_behavior_ComponentInstance, NodeInstance, behavioral_elements_common_behavior_NodeInstance, behavioral_elements_common_behavior_SubsystemInstance, behavioral_elements_use_cases_UseCase, Extend, Include, ExtensionPoint, behavioral_elements_use_cases_Actor, behavioral_elements_use_cases_UseCaseInstance, behavioral_elements_use_cases_Extend, Relationship, BooleanExpression, UseCase, behavioral_elements_use_cases_Include, behavioral_elements_use_cases_ExtensionPoint, behavioral_elements_state_machines_StateMachine, State, SubmachineState, behavioral_elements_state_machines_Event, Parameter_, behavioral_elements_state_machines_StateVertex, CompositeState, behavioral_elements_state_machines_State, StateVertex, StateMachine, Event, behavioral_elements_state_machines_TimeEvent, TimeExpression, behavioral_elements_state_machines_CallEvent, behavioral_elements_state_machines_SignalEvent, behavioral_elements_state_machines_Transition, Guard, behavioral_elements_state_machines_CompositeState, behavioral_elements_state_machines_ChangeEvent, behavioral_elements_state_machines_Guard, behavioral_elements_state_machines_Pseudostate, behavioral_elements_state_machines_SimpleState, behavioral_elements_state_machines_SubmachineState, behavioral_elements_state_machines_SynchState, behavioral_elements_state_machines_StubState, behavioral_elements_state_machines_FinalState, behavioral_elements_collaborations_Collaboration, core_GeneralizableElement, core_Namespace, Interaction, CollaborationInstanceSet, Collaboration, behavioral_elements_collaborations_ClassifierRole, Multiplicity, Feature, behavioral_elements_collaborations_AssociationRole, behavioral_elements_collaborations_AssociationEndRole, behavioral_elements_collaborations_Message, ClassifierRole, AssociationRole, behavioral_elements_collaborations_Interaction, behavioral_elements_collaborations_InteractionInstanceSet, behavioral_elements_collaborations_CollaborationInstanceSet, behavioral_elements_activity_graphs_ActivityGraph, Partition, behavioral_elements_activity_graphs_Partition, ActivityGraph, behavioral_elements_activity_graphs_SubactivityState, ArgListsExpression, behavioral_elements_activity_graphs_ActionState, SimpleState, behavioral_elements_activity_graphs_CallState, ActionState, behavioral_elements_activity_graphs_ObjectFlowState, behavioral_elements_activity_graphs_ClassifierInState},
    associations={classifier0, attributeLink1, linkEnd2, slot4, componentInstance7, ownedInstance9, ownedLink11, reception13, context15, sendAction16, occurrence18, recurrence19, script22, actualArgument24, actionSequence26, stimulus28, target20, transition30, instantiation32, attribute35, value36, instance39, linkEnd42, association45, connection46, stimulus49, signal54, action56, value58, action59, signal62, instance65, link68, associationEnd71, qualifiedValue72, argument75, sender77, operation52, receiver80, communicationLink83, dispatchAction86, playedRole89, interactionInstanceSet90, nodeInstance92, resident94, resident97, extender100, extend101, includer104, include106, extensionPoint109, condition111, base112, extension114, extensionPoint117, addition120, base123, useCase126, extend129, context132, top134, transitions136, submachineState139, parameter141, transition142, container145, outgoing147, incoming150, entry153, exit155, stateMachine158, deferrableEvent160, internalTransition162, doActivity165, when168, operation169, signal172, guard175, effect177, state180, trigger183, stateMachine186, source189, target191, subvertex194, changeExpression197, expression199, transition201, submachine204, interaction207, representedOperation209, constrainingElement212, collaborationInstanceSet214, usedCollaboration216, representedClassifier218, multiplicity221, base222, availableFeature225, availableContents227, conformingInstance230, multiplicity233, base235, message238, conformingLink241, collaborationMultiplicity244, base246, availableQualifier249, interaction252, activator255, sender257, receiver259, predecessor262, successor265, communicationConnection268, action270, conformingStimulus273, message276, context279, interactionInstanceSet282, context285, interaction288, participatingStimulus291, interactionInstanceSet294, collaboration297, participatingInstance300, participatingLink302, constrainingElement305, partition308, contents309, activityGraph311, dynamicArguments313, dynamicMultiplicity314, dynamicArguments317, dynamicMultiplicity319, parameter322, type324, type327, inState329},
    generalizations={gen_behavioral_elements_common_behavior_Instance_ModelElement, gen_behavioral_elements_common_behavior_Signal_Classifier, gen_behavioral_elements_common_behavior_Action_ModelElement, gen_behavioral_elements_common_behavior_CreateAction_Action, gen_behavioral_elements_common_behavior_DestroyAction_Action, gen_behavioral_elements_common_behavior_UninterpretedAction_Action, gen_behavioral_elements_common_behavior_AttributeLink_ModelElement, gen_behavioral_elements_common_behavior_Object_Instance, gen_behavioral_elements_common_behavior_Link_ModelElement, gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Object, gen_behavioral_elements_common_behavior_LinkObject_common_behavior_Link, gen_behavioral_elements_common_behavior_DataValue_Instance, gen_behavioral_elements_common_behavior_CallAction_Action, gen_behavioral_elements_common_behavior_SendAction_Action, gen_behavioral_elements_common_behavior_ActionSequence_Action, gen_behavioral_elements_common_behavior_Argument_ModelElement, gen_behavioral_elements_common_behavior_Reception_BehavioralFeature, gen_behavioral_elements_common_behavior_LinkEnd_ModelElement, gen_behavioral_elements_common_behavior_ReturnAction_Action, gen_behavioral_elements_common_behavior_TerminateAction_Action, gen_behavioral_elements_common_behavior_Stimulus_ModelElement, gen_behavioral_elements_common_behavior_Exception_Signal, gen_behavioral_elements_common_behavior_ComponentInstance_Instance, gen_behavioral_elements_common_behavior_NodeInstance_Instance, gen_behavioral_elements_common_behavior_SubsystemInstance_Instance, gen_behavioral_elements_use_cases_UseCase_Classifier, gen_behavioral_elements_use_cases_Actor_Classifier, gen_behavioral_elements_use_cases_UseCaseInstance_Instance, gen_behavioral_elements_use_cases_Extend_Relationship, gen_behavioral_elements_use_cases_Include_Relationship, gen_behavioral_elements_use_cases_ExtensionPoint_ModelElement, gen_behavioral_elements_state_machines_StateMachine_ModelElement, gen_behavioral_elements_state_machines_Event_ModelElement, gen_behavioral_elements_state_machines_StateVertex_ModelElement, gen_behavioral_elements_state_machines_State_StateVertex, gen_behavioral_elements_state_machines_TimeEvent_Event, gen_behavioral_elements_state_machines_CallEvent_Event, gen_behavioral_elements_state_machines_SignalEvent_Event, gen_behavioral_elements_state_machines_Transition_ModelElement, gen_behavioral_elements_state_machines_CompositeState_State, gen_behavioral_elements_state_machines_ChangeEvent_Event, gen_behavioral_elements_state_machines_Guard_ModelElement, gen_behavioral_elements_state_machines_Pseudostate_StateVertex, gen_behavioral_elements_state_machines_SimpleState_State, gen_behavioral_elements_state_machines_SubmachineState_CompositeState, gen_behavioral_elements_state_machines_SynchState_StateVertex, gen_behavioral_elements_state_machines_StubState_StateVertex, gen_behavioral_elements_state_machines_FinalState_State, gen_behavioral_elements_collaborations_Collaboration_core_GeneralizableElement, gen_behavioral_elements_collaborations_Collaboration_core_Namespace, gen_behavioral_elements_collaborations_ClassifierRole_Classifier, gen_behavioral_elements_collaborations_AssociationRole_Association, gen_behavioral_elements_collaborations_AssociationEndRole_AssociationEnd, gen_behavioral_elements_collaborations_Message_ModelElement, gen_behavioral_elements_collaborations_Interaction_ModelElement, gen_behavioral_elements_collaborations_InteractionInstanceSet_ModelElement, gen_behavioral_elements_collaborations_CollaborationInstanceSet_ModelElement, gen_behavioral_elements_activity_graphs_ActivityGraph_StateMachine, gen_behavioral_elements_activity_graphs_Partition_ModelElement, gen_behavioral_elements_activity_graphs_SubactivityState_SubmachineState, gen_behavioral_elements_activity_graphs_ActionState_SimpleState, gen_behavioral_elements_activity_graphs_CallState_ActionState, gen_behavioral_elements_activity_graphs_ObjectFlowState_SimpleState, gen_behavioral_elements_activity_graphs_ClassifierInState_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)