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
bpmn2_DocumentRoot = Class(name="bpmn2::DocumentRoot")
bpmn2_EStringToStringMapEntry = Class(name="bpmn2::EStringToStringMapEntry")
Activity = Class(name="Activity")
AdHocSubProcess = Class(name="AdHocSubProcess")
flows_FlowElement = Class(name="flows::FlowElement")
artifacts_Artifact = Class(name="artifacts::Artifact")
Assignment = Class(name="Assignment")
artifacts_Association = Class(name="artifacts::Association")
Auditing = Class(name="Auditing")
BaseElement = Class(name="BaseElement")
events_BoundaryEvent = Class(name="events::BoundaryEvent")
BusinessRuleTask = Class(name="BusinessRuleTask")
CallableElement = Class(name="CallableElement")
CallActivity = Class(name="CallActivity")
choreographyactivities_CallChoreography = Class(name="choreographyactivities::CallChoreography")
CallConversation = Class(name="CallConversation")
ConversationNode = Class(name="ConversationNode")
events_CancelEventDefinition = Class(name="events::CancelEventDefinition")
events_EventDefinition = Class(name="events::EventDefinition")
RootElement = Class(name="RootElement")
events_CatchEvent = Class(name="events::CatchEvent")
artifacts_Category = Class(name="artifacts::Category")
artifacts_CategoryValue = Class(name="artifacts::CategoryValue")
Choreography = Class(name="Choreography")
Collaboration = Class(name="Collaboration")
choreographyactivities_ChoreographyActivity = Class(name="choreographyactivities::ChoreographyActivity")
choreographyactivities_ChoreographyTask = Class(name="choreographyactivities::ChoreographyTask")
events_CompensateEventDefinition = Class(name="events::CompensateEventDefinition")
ComplexBehaviorDefinition = Class(name="ComplexBehaviorDefinition")
events_ConditionalEventDefinition = Class(name="events::ConditionalEventDefinition")
Conversation = Class(name="Conversation")
ConversationAssociation = Class(name="ConversationAssociation")
ConversationLink = Class(name="ConversationLink")
gateways_ComplexGateway = Class(name="gateways::ComplexGateway")
correlations_CorrelationProperty = Class(name="correlations::CorrelationProperty")
correlations_CorrelationPropertyBinding = Class(name="correlations::CorrelationPropertyBinding")
correlations_CorrelationPropertyRetrievalExpression = Class(name="correlations::CorrelationPropertyRetrievalExpression")
correlations_CorrelationKey = Class(name="correlations::CorrelationKey")
DataAssociation = Class(name="DataAssociation")
DataInput = Class(name="DataInput")
DataInputAssociation = Class(name="DataInputAssociation")
correlations_CorrelationSubscription = Class(name="correlations::CorrelationSubscription")
DataObjectReference = Class(name="DataObjectReference")
DataOutput = Class(name="DataOutput")
DataOutputAssociation = Class(name="DataOutputAssociation")
DataState = Class(name="DataState")
DataObject = Class(name="DataObject")
DataStore = Class(name="DataStore")
DataStoreReference = Class(name="DataStoreReference")
Definitions = Class(name="Definitions")
Documentation = Class(name="Documentation")
events_EndEvent = Class(name="events::EndEvent")
EndPoint = Class(name="EndPoint")
Error = Class(name="Error")
events_ErrorEventDefinition = Class(name="events::ErrorEventDefinition")
Escalation = Class(name="Escalation")
events_EscalationEventDefinition = Class(name="events::EscalationEventDefinition")
events_Event = Class(name="events::Event")
gateways_EventBasedGateway = Class(name="gateways::EventBasedGateway")
gateways_ExclusiveGateway = Class(name="gateways::ExclusiveGateway")
Expression = Class(name="Expression")
extension_Extension = Class(name="extension::Extension")
extension_ExtensionAttributeValue = Class(name="extension::ExtensionAttributeValue")
flows_FlowNode = Class(name="flows::FlowNode")
FormalExpression = Class(name="FormalExpression")
gateways_Gateway = Class(name="gateways::Gateway")
GlobalBusinessRuleTask = Class(name="GlobalBusinessRuleTask")
GlobalChoreographyTask = Class(name="GlobalChoreographyTask")
GlobalConversation = Class(name="GlobalConversation")
GlobalManualTask = Class(name="GlobalManualTask")
GlobalScriptTask = Class(name="GlobalScriptTask")
GlobalTask = Class(name="GlobalTask")
GlobalUserTask = Class(name="GlobalUserTask")
artifacts_Group = Class(name="artifacts::Group")
HumanPerformer = Class(name="HumanPerformer")
Performer = Class(name="Performer")
ResourceRole = Class(name="ResourceRole")
events_ImplicitThrowEvent = Class(name="events::ImplicitThrowEvent")
Import = Class(name="Import")
gateways_InclusiveGateway = Class(name="gateways::InclusiveGateway")
InputSet = Class(name="InputSet")
Interface = Class(name="Interface")
events_IntermediateCatchEvent = Class(name="events::IntermediateCatchEvent")
events_IntermediateThrowEvent = Class(name="events::IntermediateThrowEvent")
InputOutputBinding = Class(name="InputOutputBinding")
InputOutputSpecification = Class(name="InputOutputSpecification")
ItemDefinition = Class(name="ItemDefinition")
Lane = Class(name="Lane")
LaneSet = Class(name="LaneSet")
events_LinkEventDefinition = Class(name="events::LinkEventDefinition")
LoopCharacteristics = Class(name="LoopCharacteristics")
ManualTask = Class(name="ManualTask")
Message = Class(name="Message")
MessageEventDefinition = Class(name="MessageEventDefinition")
MessageFlow = Class(name="MessageFlow")
MessageFlowAssociation = Class(name="MessageFlowAssociation")
Monitoring = Class(name="Monitoring")
MultiInstanceLoopCharacteristics = Class(name="MultiInstanceLoopCharacteristics")
Operation = Class(name="Operation")
OutputSet = Class(name="OutputSet")
gateways_ParallelGateway = Class(name="gateways::ParallelGateway")
Participant = Class(name="Participant")
ParticipantAssociation = Class(name="ParticipantAssociation")
ParticipantMultiplicity = Class(name="ParticipantMultiplicity")
PartnerEntity = Class(name="PartnerEntity")
PartnerRole = Class(name="PartnerRole")
PotentialOwner = Class(name="PotentialOwner")
Process = Class(name="Process")
Property_ = Class(name="Property")
ReceiveTask = Class(name="ReceiveTask")
Relationship = Class(name="Relationship")
Rendering = Class(name="Rendering")
Resource = Class(name="Resource")
ResourceAssignmentExpression = Class(name="ResourceAssignmentExpression")
ResourceParameter = Class(name="ResourceParameter")
ResourceParameterBinding = Class(name="ResourceParameterBinding")
bpmn2_EObject = Class(name="bpmn2::EObject")
ScriptTask = Class(name="ScriptTask")
SendTask = Class(name="SendTask")
flows_SequenceFlow = Class(name="flows::SequenceFlow")
events_Signal = Class(name="events::Signal")
events_SignalEventDefinition = Class(name="events::SignalEventDefinition")
StandardLoopCharacteristics = Class(name="StandardLoopCharacteristics")
ServiceTask = Class(name="ServiceTask")
events_StartEvent = Class(name="events::StartEvent")
choreographyactivities_SubChoreography = Class(name="choreographyactivities::SubChoreography")
SubConversation = Class(name="SubConversation")
SubProcess = Class(name="SubProcess")
Task = Class(name="Task")
events_TerminateEventDefinition = Class(name="events::TerminateEventDefinition")
events_ThrowEvent = Class(name="events::ThrowEvent")
events_TimerEventDefinition = Class(name="events::TimerEventDefinition")
artifacts_TextAnnotation = Class(name="artifacts::TextAnnotation")
Transaction = Class(name="Transaction")
UserTask = Class(name="UserTask")

# bpmn2_DocumentRoot class attributes and methods
bpmn2_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
bpmn2_DocumentRoot.attributes={bpmn2_DocumentRoot_mixed}

# bpmn2_EStringToStringMapEntry class attributes and methods

# Activity class attributes and methods

# AdHocSubProcess class attributes and methods

# flows_FlowElement class attributes and methods

# artifacts_Artifact class attributes and methods

# Assignment class attributes and methods

# artifacts_Association class attributes and methods

# Auditing class attributes and methods

# BaseElement class attributes and methods

# events_BoundaryEvent class attributes and methods

# BusinessRuleTask class attributes and methods

# CallableElement class attributes and methods

# CallActivity class attributes and methods

# choreographyactivities_CallChoreography class attributes and methods

# CallConversation class attributes and methods

# ConversationNode class attributes and methods

# events_CancelEventDefinition class attributes and methods

# events_EventDefinition class attributes and methods

# RootElement class attributes and methods

# events_CatchEvent class attributes and methods

# artifacts_Category class attributes and methods

# artifacts_CategoryValue class attributes and methods

# Choreography class attributes and methods

# Collaboration class attributes and methods

# choreographyactivities_ChoreographyActivity class attributes and methods

# choreographyactivities_ChoreographyTask class attributes and methods

# events_CompensateEventDefinition class attributes and methods

# ComplexBehaviorDefinition class attributes and methods

# events_ConditionalEventDefinition class attributes and methods

# Conversation class attributes and methods

# ConversationAssociation class attributes and methods

# ConversationLink class attributes and methods

# gateways_ComplexGateway class attributes and methods

# correlations_CorrelationProperty class attributes and methods

# correlations_CorrelationPropertyBinding class attributes and methods

# correlations_CorrelationPropertyRetrievalExpression class attributes and methods

# correlations_CorrelationKey class attributes and methods

# DataAssociation class attributes and methods

# DataInput class attributes and methods

# DataInputAssociation class attributes and methods

# correlations_CorrelationSubscription class attributes and methods

# DataObjectReference class attributes and methods

# DataOutput class attributes and methods

# DataOutputAssociation class attributes and methods

# DataState class attributes and methods

# DataObject class attributes and methods

# DataStore class attributes and methods

# DataStoreReference class attributes and methods

# Definitions class attributes and methods

# Documentation class attributes and methods

# events_EndEvent class attributes and methods

# EndPoint class attributes and methods

# Error class attributes and methods

# events_ErrorEventDefinition class attributes and methods

# Escalation class attributes and methods

# events_EscalationEventDefinition class attributes and methods

# events_Event class attributes and methods

# gateways_EventBasedGateway class attributes and methods

# gateways_ExclusiveGateway class attributes and methods

# Expression class attributes and methods

# extension_Extension class attributes and methods

# extension_ExtensionAttributeValue class attributes and methods

# flows_FlowNode class attributes and methods

# FormalExpression class attributes and methods

# gateways_Gateway class attributes and methods

# GlobalBusinessRuleTask class attributes and methods

# GlobalChoreographyTask class attributes and methods

# GlobalConversation class attributes and methods

# GlobalManualTask class attributes and methods

# GlobalScriptTask class attributes and methods

# GlobalTask class attributes and methods

# GlobalUserTask class attributes and methods

# artifacts_Group class attributes and methods

# HumanPerformer class attributes and methods

# Performer class attributes and methods

# ResourceRole class attributes and methods

# events_ImplicitThrowEvent class attributes and methods

# Import class attributes and methods

# gateways_InclusiveGateway class attributes and methods

# InputSet class attributes and methods

# Interface class attributes and methods

# events_IntermediateCatchEvent class attributes and methods

# events_IntermediateThrowEvent class attributes and methods

# InputOutputBinding class attributes and methods

# InputOutputSpecification class attributes and methods

# ItemDefinition class attributes and methods

# Lane class attributes and methods

# LaneSet class attributes and methods

# events_LinkEventDefinition class attributes and methods

# LoopCharacteristics class attributes and methods

# ManualTask class attributes and methods

# Message class attributes and methods

# MessageEventDefinition class attributes and methods

# MessageFlow class attributes and methods

# MessageFlowAssociation class attributes and methods

# Monitoring class attributes and methods

# MultiInstanceLoopCharacteristics class attributes and methods

# Operation class attributes and methods

# OutputSet class attributes and methods

# gateways_ParallelGateway class attributes and methods

# Participant class attributes and methods

# ParticipantAssociation class attributes and methods

# ParticipantMultiplicity class attributes and methods

# PartnerEntity class attributes and methods

# PartnerRole class attributes and methods

# PotentialOwner class attributes and methods

# Process class attributes and methods

# Property class attributes and methods

# ReceiveTask class attributes and methods

# Relationship class attributes and methods

# Rendering class attributes and methods

# Resource class attributes and methods

# ResourceAssignmentExpression class attributes and methods

# ResourceParameter class attributes and methods

# ResourceParameterBinding class attributes and methods

# bpmn2_EObject class attributes and methods

# ScriptTask class attributes and methods

# SendTask class attributes and methods

# flows_SequenceFlow class attributes and methods

# events_Signal class attributes and methods

# events_SignalEventDefinition class attributes and methods

# StandardLoopCharacteristics class attributes and methods

# ServiceTask class attributes and methods

# events_StartEvent class attributes and methods

# choreographyactivities_SubChoreography class attributes and methods

# SubConversation class attributes and methods

# SubProcess class attributes and methods

# Task class attributes and methods

# events_TerminateEventDefinition class attributes and methods

# events_ThrowEvent class attributes and methods

# events_TimerEventDefinition class attributes and methods

# artifacts_TextAnnotation class attributes and methods

# Transaction class attributes and methods

# UserTask class attributes and methods

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="bpmn2_EStringToStringMapEntry", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot", type=bpmn2_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="bpmn2_EStringToStringMapEntry3", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot2", type=bpmn2_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity4: BinaryAssociation = BinaryAssociation(
    name="activity4",
    ends={
        Property(name="Activity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot5", type=Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adHocSubProcess6: BinaryAssociation = BinaryAssociation(
    name="adHocSubProcess6",
    ends={
        Property(name="AdHocSubProcess", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot7", type=AdHocSubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElement8: BinaryAssociation = BinaryAssociation(
    name="flowElement8",
    ends={
        Property(name="flows_FlowElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot9", type=flows_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifact10: BinaryAssociation = BinaryAssociation(
    name="artifact10",
    ends={
        Property(name="artifacts_Artifact", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot11", type=artifacts_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment12: BinaryAssociation = BinaryAssociation(
    name="assignment12",
    ends={
        Property(name="Assignment", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot13", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association14: BinaryAssociation = BinaryAssociation(
    name="association14",
    ends={
        Property(name="artifacts_Association", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot15", type=artifacts_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing16: BinaryAssociation = BinaryAssociation(
    name="auditing16",
    ends={
        Property(name="Auditing", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot17", type=Auditing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElement18: BinaryAssociation = BinaryAssociation(
    name="baseElement18",
    ends={
        Property(name="BaseElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot19", type=BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElementWithMixedContent20: BinaryAssociation = BinaryAssociation(
    name="baseElementWithMixedContent20",
    ends={
        Property(name="BaseElement22", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot21", type=BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundaryEvent23: BinaryAssociation = BinaryAssociation(
    name="boundaryEvent23",
    ends={
        Property(name="events_BoundaryEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot24", type=events_BoundaryEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessRuleTask25: BinaryAssociation = BinaryAssociation(
    name="businessRuleTask25",
    ends={
        Property(name="BusinessRuleTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot26", type=BusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callableElement27: BinaryAssociation = BinaryAssociation(
    name="callableElement27",
    ends={
        Property(name="CallableElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot28", type=CallableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callActivity29: BinaryAssociation = BinaryAssociation(
    name="callActivity29",
    ends={
        Property(name="CallActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot30", type=CallActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callChoreography31: BinaryAssociation = BinaryAssociation(
    name="callChoreography31",
    ends={
        Property(name="choreographyactivities_CallChoreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot32", type=choreographyactivities_CallChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callConversation33: BinaryAssociation = BinaryAssociation(
    name="callConversation33",
    ends={
        Property(name="CallConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot34", type=CallConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNode35: BinaryAssociation = BinaryAssociation(
    name="conversationNode35",
    ends={
        Property(name="ConversationNode", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot36", type=ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelEventDefinition37: BinaryAssociation = BinaryAssociation(
    name="cancelEventDefinition37",
    ends={
        Property(name="events_CancelEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot38", type=events_CancelEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinition39: BinaryAssociation = BinaryAssociation(
    name="eventDefinition39",
    ends={
        Property(name="events_EventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot40", type=events_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElement41: BinaryAssociation = BinaryAssociation(
    name="rootElement41",
    ends={
        Property(name="RootElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot42", type=RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category45: BinaryAssociation = BinaryAssociation(
    name="category45",
    ends={
        Property(name="artifacts_Category", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot46", type=artifacts_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValue47: BinaryAssociation = BinaryAssociation(
    name="categoryValue47",
    ends={
        Property(name="artifacts_CategoryValue", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot48", type=artifacts_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreography49: BinaryAssociation = BinaryAssociation(
    name="choreography49",
    ends={
        Property(name="Choreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot50", type=Choreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchEvent43: BinaryAssociation = BinaryAssociation(
    name="catchEvent43",
    ends={
        Property(name="events_CatchEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot44", type=events_CatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyActivity53: BinaryAssociation = BinaryAssociation(
    name="choreographyActivity53",
    ends={
        Property(name="choreographyactivities_ChoreographyActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot54", type=choreographyactivities_ChoreographyActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyTask55: BinaryAssociation = BinaryAssociation(
    name="choreographyTask55",
    ends={
        Property(name="choreographyactivities_ChoreographyTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot56", type=choreographyactivities_ChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compensateEventDefinition57: BinaryAssociation = BinaryAssociation(
    name="compensateEventDefinition57",
    ends={
        Property(name="events_CompensateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot58", type=events_CompensateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexBehaviorDefinition59: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition59",
    ends={
        Property(name="ComplexBehaviorDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot60", type=ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration51: BinaryAssociation = BinaryAssociation(
    name="collaboration51",
    ends={
        Property(name="Collaboration", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot52", type=Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalEventDefinition63: BinaryAssociation = BinaryAssociation(
    name="conditionalEventDefinition63",
    ends={
        Property(name="events_ConditionalEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot64", type=events_ConditionalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversation65: BinaryAssociation = BinaryAssociation(
    name="conversation65",
    ends={
        Property(name="Conversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot66", type=Conversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociation67: BinaryAssociation = BinaryAssociation(
    name="conversationAssociation67",
    ends={
        Property(name="ConversationAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot68", type=ConversationAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationLink69: BinaryAssociation = BinaryAssociation(
    name="conversationLink69",
    ends={
        Property(name="ConversationLink", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot70", type=ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexGateway61: BinaryAssociation = BinaryAssociation(
    name="complexGateway61",
    ends={
        Property(name="gateways_ComplexGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot62", type=gateways_ComplexGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationProperty73: BinaryAssociation = BinaryAssociation(
    name="correlationProperty73",
    ends={
        Property(name="correlations_CorrelationProperty", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot74", type=correlations_CorrelationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyBinding75: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding75",
    ends={
        Property(name="correlations_CorrelationPropertyBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot76", type=correlations_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRetrievalExpression77: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression77",
    ends={
        Property(name="correlations_CorrelationPropertyRetrievalExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot78", type=correlations_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationKey71: BinaryAssociation = BinaryAssociation(
    name="correlationKey71",
    ends={
        Property(name="correlations_CorrelationKey", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot72", type=correlations_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataAssociation81: BinaryAssociation = BinaryAssociation(
    name="dataAssociation81",
    ends={
        Property(name="DataAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot82", type=DataAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInput83: BinaryAssociation = BinaryAssociation(
    name="dataInput83",
    ends={
        Property(name="DataInput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot84", type=DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation85: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation85",
    ends={
        Property(name="DataInputAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot86", type=DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscription79: BinaryAssociation = BinaryAssociation(
    name="correlationSubscription79",
    ends={
        Property(name="correlations_CorrelationSubscription", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot80", type=correlations_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObject87: BinaryAssociation = BinaryAssociation(
    name="dataObject87",
    ends={
        Property(name="DataObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot88", type=DataObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjectReference89: BinaryAssociation = BinaryAssociation(
    name="dataObjectReference89",
    ends={
        Property(name="DataObjectReference", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot90", type=DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutput91: BinaryAssociation = BinaryAssociation(
    name="dataOutput91",
    ends={
        Property(name="DataOutput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot92", type=DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociation93: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation93",
    ends={
        Property(name="DataOutputAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot94", type=DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataState95: BinaryAssociation = BinaryAssociation(
    name="dataState95",
    ends={
        Property(name="DataState", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot96", type=DataState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStore97: BinaryAssociation = BinaryAssociation(
    name="dataStore97",
    ends={
        Property(name="DataStore", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot98", type=DataStore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStoreReference99: BinaryAssociation = BinaryAssociation(
    name="dataStoreReference99",
    ends={
        Property(name="DataStoreReference", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot100", type=DataStoreReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions101: BinaryAssociation = BinaryAssociation(
    name="definitions101",
    ends={
        Property(name="Definitions", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot102", type=Definitions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation103: BinaryAssociation = BinaryAssociation(
    name="documentation103",
    ends={
        Property(name="Documentation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot104", type=Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endEvent105: BinaryAssociation = BinaryAssociation(
    name="endEvent105",
    ends={
        Property(name="events_EndEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot106", type=events_EndEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoint107: BinaryAssociation = BinaryAssociation(
    name="endPoint107",
    ends={
        Property(name="EndPoint", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot108", type=EndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error109: BinaryAssociation = BinaryAssociation(
    name="error109",
    ends={
        Property(name="Error", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot110", type=Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
errorEventDefinition111: BinaryAssociation = BinaryAssociation(
    name="errorEventDefinition111",
    ends={
        Property(name="events_ErrorEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot112", type=events_ErrorEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalation113: BinaryAssociation = BinaryAssociation(
    name="escalation113",
    ends={
        Property(name="Escalation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot114", type=Escalation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalationEventDefinition115: BinaryAssociation = BinaryAssociation(
    name="escalationEventDefinition115",
    ends={
        Property(name="events_EscalationEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot116", type=events_EscalationEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event117: BinaryAssociation = BinaryAssociation(
    name="event117",
    ends={
        Property(name="events_Event", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot118", type=events_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventBasedGateway119: BinaryAssociation = BinaryAssociation(
    name="eventBasedGateway119",
    ends={
        Property(name="gateways_EventBasedGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot120", type=gateways_EventBasedGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclusiveGateway121: BinaryAssociation = BinaryAssociation(
    name="exclusiveGateway121",
    ends={
        Property(name="gateways_ExclusiveGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot122", type=gateways_ExclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="Expression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot124", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension125: BinaryAssociation = BinaryAssociation(
    name="extension125",
    ends={
        Property(name="extension_Extension", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot126", type=extension_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionElements127: BinaryAssociation = BinaryAssociation(
    name="extensionElements127",
    ends={
        Property(name="extension_ExtensionAttributeValue", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot128", type=extension_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowNode129: BinaryAssociation = BinaryAssociation(
    name="flowNode129",
    ends={
        Property(name="flows_FlowNode", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot130", type=flows_FlowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalExpression131: BinaryAssociation = BinaryAssociation(
    name="formalExpression131",
    ends={
        Property(name="FormalExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot132", type=FormalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gateway133: BinaryAssociation = BinaryAssociation(
    name="gateway133",
    ends={
        Property(name="gateways_Gateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot134", type=gateways_Gateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalBusinessRuleTask135: BinaryAssociation = BinaryAssociation(
    name="globalBusinessRuleTask135",
    ends={
        Property(name="GlobalBusinessRuleTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot136", type=GlobalBusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalChoreographyTask137: BinaryAssociation = BinaryAssociation(
    name="globalChoreographyTask137",
    ends={
        Property(name="GlobalChoreographyTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot138", type=GlobalChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalConversation139: BinaryAssociation = BinaryAssociation(
    name="globalConversation139",
    ends={
        Property(name="GlobalConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot140", type=GlobalConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalManualTask141: BinaryAssociation = BinaryAssociation(
    name="globalManualTask141",
    ends={
        Property(name="GlobalManualTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot142", type=GlobalManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalScriptTask143: BinaryAssociation = BinaryAssociation(
    name="globalScriptTask143",
    ends={
        Property(name="GlobalScriptTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot144", type=GlobalScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalTask145: BinaryAssociation = BinaryAssociation(
    name="globalTask145",
    ends={
        Property(name="GlobalTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot146", type=GlobalTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalUserTask147: BinaryAssociation = BinaryAssociation(
    name="globalUserTask147",
    ends={
        Property(name="GlobalUserTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot148", type=GlobalUserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group149: BinaryAssociation = BinaryAssociation(
    name="group149",
    ends={
        Property(name="artifacts_Group", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot150", type=artifacts_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
humanPerformer151: BinaryAssociation = BinaryAssociation(
    name="humanPerformer151",
    ends={
        Property(name="HumanPerformer", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot152", type=HumanPerformer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performer153: BinaryAssociation = BinaryAssociation(
    name="performer153",
    ends={
        Property(name="Performer", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot154", type=Performer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRole155: BinaryAssociation = BinaryAssociation(
    name="resourceRole155",
    ends={
        Property(name="ResourceRole", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot156", type=ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitThrowEvent157: BinaryAssociation = BinaryAssociation(
    name="implicitThrowEvent157",
    ends={
        Property(name="events_ImplicitThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot158", type=events_ImplicitThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import159: BinaryAssociation = BinaryAssociation(
    name="import159",
    ends={
        Property(name="Import", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot160", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inclusiveGateway161: BinaryAssociation = BinaryAssociation(
    name="inclusiveGateway161",
    ends={
        Property(name="gateways_InclusiveGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot162", type=gateways_InclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet163: BinaryAssociation = BinaryAssociation(
    name="inputSet163",
    ends={
        Property(name="InputSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot164", type=InputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface165: BinaryAssociation = BinaryAssociation(
    name="interface165",
    ends={
        Property(name="Interface", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot166", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateCatchEvent167: BinaryAssociation = BinaryAssociation(
    name="intermediateCatchEvent167",
    ends={
        Property(name="events_IntermediateCatchEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot168", type=events_IntermediateCatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateThrowEvent169: BinaryAssociation = BinaryAssociation(
    name="intermediateThrowEvent169",
    ends={
        Property(name="events_IntermediateThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot170", type=events_IntermediateThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioBinding171: BinaryAssociation = BinaryAssociation(
    name="ioBinding171",
    ends={
        Property(name="InputOutputBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot172", type=InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification173: BinaryAssociation = BinaryAssociation(
    name="ioSpecification173",
    ends={
        Property(name="InputOutputSpecification", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot174", type=InputOutputSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemDefinition175: BinaryAssociation = BinaryAssociation(
    name="itemDefinition175",
    ends={
        Property(name="ItemDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot176", type=ItemDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lane177: BinaryAssociation = BinaryAssociation(
    name="lane177",
    ends={
        Property(name="Lane", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot178", type=Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laneSet179: BinaryAssociation = BinaryAssociation(
    name="laneSet179",
    ends={
        Property(name="LaneSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot180", type=LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkEventDefinition181: BinaryAssociation = BinaryAssociation(
    name="linkEventDefinition181",
    ends={
        Property(name="events_LinkEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot182", type=events_LinkEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCharacteristics183: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics183",
    ends={
        Property(name="LoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot184", type=LoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manualTask185: BinaryAssociation = BinaryAssociation(
    name="manualTask185",
    ends={
        Property(name="ManualTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot186", type=ManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message187: BinaryAssociation = BinaryAssociation(
    name="message187",
    ends={
        Property(name="Message", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot188", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageEventDefinition189: BinaryAssociation = BinaryAssociation(
    name="messageEventDefinition189",
    ends={
        Property(name="MessageEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot190", type=MessageEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlow191: BinaryAssociation = BinaryAssociation(
    name="messageFlow191",
    ends={
        Property(name="MessageFlow", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot192", type=MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociation193: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociation193",
    ends={
        Property(name="MessageFlowAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot194", type=MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monitoring195: BinaryAssociation = BinaryAssociation(
    name="monitoring195",
    ends={
        Property(name="Monitoring", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot196", type=Monitoring, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiInstanceLoopCharacteristics197: BinaryAssociation = BinaryAssociation(
    name="multiInstanceLoopCharacteristics197",
    ends={
        Property(name="MultiInstanceLoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot198", type=MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation199: BinaryAssociation = BinaryAssociation(
    name="operation199",
    ends={
        Property(name="Operation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot200", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSet201: BinaryAssociation = BinaryAssociation(
    name="outputSet201",
    ends={
        Property(name="OutputSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot202", type=OutputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallelGateway203: BinaryAssociation = BinaryAssociation(
    name="parallelGateway203",
    ends={
        Property(name="gateways_ParallelGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot204", type=gateways_ParallelGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant205: BinaryAssociation = BinaryAssociation(
    name="participant205",
    ends={
        Property(name="Participant", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot206", type=Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantAssociation207: BinaryAssociation = BinaryAssociation(
    name="participantAssociation207",
    ends={
        Property(name="ParticipantAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot208", type=ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantMultiplicity209: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity209",
    ends={
        Property(name="ParticipantMultiplicity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot210", type=ParticipantMultiplicity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerEntity211: BinaryAssociation = BinaryAssociation(
    name="partnerEntity211",
    ends={
        Property(name="PartnerEntity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot212", type=PartnerEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerRole213: BinaryAssociation = BinaryAssociation(
    name="partnerRole213",
    ends={
        Property(name="PartnerRole", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot214", type=PartnerRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
potentialOwner215: BinaryAssociation = BinaryAssociation(
    name="potentialOwner215",
    ends={
        Property(name="PotentialOwner", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot216", type=PotentialOwner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process217: BinaryAssociation = BinaryAssociation(
    name="process217",
    ends={
        Property(name="Process", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot218", type=Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property219: BinaryAssociation = BinaryAssociation(
    name="property219",
    ends={
        Property(name="Property", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot220", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiveTask221: BinaryAssociation = BinaryAssociation(
    name="receiveTask221",
    ends={
        Property(name="ReceiveTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot222", type=ReceiveTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship223: BinaryAssociation = BinaryAssociation(
    name="relationship223",
    ends={
        Property(name="Relationship", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot224", type=Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rendering225: BinaryAssociation = BinaryAssociation(
    name="rendering225",
    ends={
        Property(name="Rendering", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot226", type=Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource227: BinaryAssociation = BinaryAssociation(
    name="resource227",
    ends={
        Property(name="Resource", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot228", type=Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression229: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression229",
    ends={
        Property(name="ResourceAssignmentExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot230", type=ResourceAssignmentExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameter231: BinaryAssociation = BinaryAssociation(
    name="resourceParameter231",
    ends={
        Property(name="ResourceParameter", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot232", type=ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameterBinding233: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBinding233",
    ends={
        Property(name="ResourceParameterBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot234", type=ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script235: BinaryAssociation = BinaryAssociation(
    name="script235",
    ends={
        Property(name="bpmn2_EObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot236", type=bpmn2_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sendTask239: BinaryAssociation = BinaryAssociation(
    name="sendTask239",
    ends={
        Property(name="SendTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot240", type=SendTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceFlow241: BinaryAssociation = BinaryAssociation(
    name="sequenceFlow241",
    ends={
        Property(name="flows_SequenceFlow", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot242", type=flows_SequenceFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptTask237: BinaryAssociation = BinaryAssociation(
    name="scriptTask237",
    ends={
        Property(name="ScriptTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot238", type=ScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceTask243: BinaryAssociation = BinaryAssociation(
    name="serviceTask243",
    ends={
        Property(name="bpmn2_DocumentRoot244", type=ServiceTask, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ServiceTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
signal245: BinaryAssociation = BinaryAssociation(
    name="signal245",
    ends={
        Property(name="events_Signal", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot246", type=events_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalEventDefinition247: BinaryAssociation = BinaryAssociation(
    name="signalEventDefinition247",
    ends={
        Property(name="events_SignalEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot248", type=events_SignalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
standardLoopCharacteristics249: BinaryAssociation = BinaryAssociation(
    name="standardLoopCharacteristics249",
    ends={
        Property(name="StandardLoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot250", type=StandardLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startEvent251: BinaryAssociation = BinaryAssociation(
    name="startEvent251",
    ends={
        Property(name="events_StartEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot252", type=events_StartEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subChoreography253: BinaryAssociation = BinaryAssociation(
    name="subChoreography253",
    ends={
        Property(name="choreographyactivities_SubChoreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot254", type=choreographyactivities_SubChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subConversation255: BinaryAssociation = BinaryAssociation(
    name="subConversation255",
    ends={
        Property(name="SubConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot256", type=SubConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess257: BinaryAssociation = BinaryAssociation(
    name="subProcess257",
    ends={
        Property(name="SubProcess", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot258", type=SubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task259: BinaryAssociation = BinaryAssociation(
    name="task259",
    ends={
        Property(name="Task", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot260", type=Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminateEventDefinition261: BinaryAssociation = BinaryAssociation(
    name="terminateEventDefinition261",
    ends={
        Property(name="events_TerminateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot262", type=events_TerminateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text263: BinaryAssociation = BinaryAssociation(
    name="text263",
    ends={
        Property(name="bpmn2_EObject265", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot264", type=bpmn2_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textAnnotation266: BinaryAssociation = BinaryAssociation(
    name="textAnnotation266",
    ends={
        Property(name="artifacts_TextAnnotation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot267", type=artifacts_TextAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throwEvent268: BinaryAssociation = BinaryAssociation(
    name="throwEvent268",
    ends={
        Property(name="events_ThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot269", type=events_ThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transaction272: BinaryAssociation = BinaryAssociation(
    name="transaction272",
    ends={
        Property(name="Transaction", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot273", type=Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userTask274: BinaryAssociation = BinaryAssociation(
    name="userTask274",
    ends={
        Property(name="UserTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot275", type=UserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerEventDefinition270: BinaryAssociation = BinaryAssociation(
    name="timerEventDefinition270",
    ends={
        Property(name="events_TimerEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot271", type=events_TimerEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bpmn2",
    types={bpmn2_DocumentRoot, bpmn2_EStringToStringMapEntry, Activity, AdHocSubProcess, flows_FlowElement, artifacts_Artifact, Assignment, artifacts_Association, Auditing, BaseElement, events_BoundaryEvent, BusinessRuleTask, CallableElement, CallActivity, choreographyactivities_CallChoreography, CallConversation, ConversationNode, events_CancelEventDefinition, events_EventDefinition, RootElement, events_CatchEvent, artifacts_Category, artifacts_CategoryValue, Choreography, Collaboration, choreographyactivities_ChoreographyActivity, choreographyactivities_ChoreographyTask, events_CompensateEventDefinition, ComplexBehaviorDefinition, events_ConditionalEventDefinition, Conversation, ConversationAssociation, ConversationLink, gateways_ComplexGateway, correlations_CorrelationProperty, correlations_CorrelationPropertyBinding, correlations_CorrelationPropertyRetrievalExpression, correlations_CorrelationKey, DataAssociation, DataInput, DataInputAssociation, correlations_CorrelationSubscription, DataObjectReference, DataOutput, DataOutputAssociation, DataState, DataObject, DataStore, DataStoreReference, Definitions, Documentation, events_EndEvent, EndPoint, Error, events_ErrorEventDefinition, Escalation, events_EscalationEventDefinition, events_Event, gateways_EventBasedGateway, gateways_ExclusiveGateway, Expression, extension_Extension, extension_ExtensionAttributeValue, flows_FlowNode, FormalExpression, gateways_Gateway, GlobalBusinessRuleTask, GlobalChoreographyTask, GlobalConversation, GlobalManualTask, GlobalScriptTask, GlobalTask, GlobalUserTask, artifacts_Group, HumanPerformer, Performer, ResourceRole, events_ImplicitThrowEvent, Import, gateways_InclusiveGateway, InputSet, Interface, events_IntermediateCatchEvent, events_IntermediateThrowEvent, InputOutputBinding, InputOutputSpecification, ItemDefinition, Lane, LaneSet, events_LinkEventDefinition, LoopCharacteristics, ManualTask, Message, MessageEventDefinition, MessageFlow, MessageFlowAssociation, Monitoring, MultiInstanceLoopCharacteristics, Operation, OutputSet, gateways_ParallelGateway, Participant, ParticipantAssociation, ParticipantMultiplicity, PartnerEntity, PartnerRole, PotentialOwner, Process, Property_, ReceiveTask, Relationship, Rendering, Resource, ResourceAssignmentExpression, ResourceParameter, ResourceParameterBinding, bpmn2_EObject, ScriptTask, SendTask, flows_SequenceFlow, events_Signal, events_SignalEventDefinition, StandardLoopCharacteristics, ServiceTask, events_StartEvent, choreographyactivities_SubChoreography, SubConversation, SubProcess, Task, events_TerminateEventDefinition, events_ThrowEvent, events_TimerEventDefinition, artifacts_TextAnnotation, Transaction, UserTask},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, activity4, adHocSubProcess6, flowElement8, artifact10, assignment12, association14, auditing16, baseElement18, baseElementWithMixedContent20, boundaryEvent23, businessRuleTask25, callableElement27, callActivity29, callChoreography31, callConversation33, conversationNode35, cancelEventDefinition37, eventDefinition39, rootElement41, category45, categoryValue47, choreography49, catchEvent43, choreographyActivity53, choreographyTask55, compensateEventDefinition57, complexBehaviorDefinition59, collaboration51, conditionalEventDefinition63, conversation65, conversationAssociation67, conversationLink69, complexGateway61, correlationProperty73, correlationPropertyBinding75, correlationPropertyRetrievalExpression77, correlationKey71, dataAssociation81, dataInput83, dataInputAssociation85, correlationSubscription79, dataObject87, dataObjectReference89, dataOutput91, dataOutputAssociation93, dataState95, dataStore97, dataStoreReference99, definitions101, documentation103, endEvent105, endPoint107, error109, errorEventDefinition111, escalation113, escalationEventDefinition115, event117, eventBasedGateway119, exclusiveGateway121, expression123, extension125, extensionElements127, flowNode129, formalExpression131, gateway133, globalBusinessRuleTask135, globalChoreographyTask137, globalConversation139, globalManualTask141, globalScriptTask143, globalTask145, globalUserTask147, group149, humanPerformer151, performer153, resourceRole155, implicitThrowEvent157, import159, inclusiveGateway161, inputSet163, interface165, intermediateCatchEvent167, intermediateThrowEvent169, ioBinding171, ioSpecification173, itemDefinition175, lane177, laneSet179, linkEventDefinition181, loopCharacteristics183, manualTask185, message187, messageEventDefinition189, messageFlow191, messageFlowAssociation193, monitoring195, multiInstanceLoopCharacteristics197, operation199, outputSet201, parallelGateway203, participant205, participantAssociation207, participantMultiplicity209, partnerEntity211, partnerRole213, potentialOwner215, process217, property219, receiveTask221, relationship223, rendering225, resource227, resourceAssignmentExpression229, resourceParameter231, resourceParameterBinding233, script235, sendTask239, sequenceFlow241, scriptTask237, serviceTask243, signal245, signalEventDefinition247, standardLoopCharacteristics249, startEvent251, subChoreography253, subConversation255, subProcess257, task259, terminateEventDefinition261, text263, textAnnotation266, throwEvent268, transaction272, userTask274, timerEventDefinition270},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)