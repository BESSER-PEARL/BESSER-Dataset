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
AssociationDirection: Enumeration = Enumeration(
    name="AssociationDirection",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="one"),
			EnumerationLiteral(name="both")
    }
)

EventBasedGatewayType: Enumeration = Enumeration(
    name="EventBasedGatewayType",
    literals={
            EnumerationLiteral(name="exclusive"),
			EnumerationLiteral(name="parallel")
    }
)

GatewayDirection: Enumeration = Enumeration(
    name="GatewayDirection",
    literals={
            EnumerationLiteral(name="mixed"),
			EnumerationLiteral(name="unspecified"),
			EnumerationLiteral(name="converging"),
			EnumerationLiteral(name="diverging")
    }
)

RelationshipDirection: Enumeration = Enumeration(
    name="RelationshipDirection",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="forward"),
			EnumerationLiteral(name="backward"),
			EnumerationLiteral(name="both")
    }
)

ItemKind: Enumeration = Enumeration(
    name="ItemKind",
    literals={
            EnumerationLiteral(name="physical"),
			EnumerationLiteral(name="information")
    }
)

ProcessType: Enumeration = Enumeration(
    name="ProcessType",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

AdHocOrdering: Enumeration = Enumeration(
    name="AdHocOrdering",
    literals={
            EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="sequential")
    }
)

MultiInstanceBehavior: Enumeration = Enumeration(
    name="MultiInstanceBehavior",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="one"),
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="complex")
    }
)

# Classes
bpmnprof_InclusiveGateway = Class(name="bpmnprof::InclusiveGateway")
NonExclusiveGateway = Class(name="NonExclusiveGateway")
bpmnprof_ActivityNode = Class(name="bpmnprof::ActivityNode")
bpmnprof_FlowElement = Class(name="bpmnprof::FlowElement", is_abstract=True)
BaseElement = Class(name="BaseElement")
bpmnprof_Auditing = Class(name="bpmnprof::Auditing")
bpmnprof_Monitoring = Class(name="bpmnprof::Monitoring")
bpmnprof_CategoryValue = Class(name="bpmnprof::CategoryValue")
bpmnprof_FlowElementsContainer = Class(name="bpmnprof::FlowElementsContainer", is_abstract=True)
bpmnprof_BaseElement = Class(name="bpmnprof::BaseElement", is_abstract=True)
bpmnprof_SequenceFlow = Class(name="bpmnprof::SequenceFlow")
bpmnprof_NonExclusiveGateway = Class(name="bpmnprof::NonExclusiveGateway", is_abstract=True)
Gateway = Class(name="Gateway")
bpmnprof_JoinNode = Class(name="bpmnprof::JoinNode")
bpmnprof_ForkNode = Class(name="bpmnprof::ForkNode")
bpmnprof_Gateway = Class(name="bpmnprof::Gateway", is_abstract=True)
FlowNode = Class(name="FlowNode")
bpmnprof_ControlNode = Class(name="bpmnprof::ControlNode")
bpmnprof_ActivityGroup = Class(name="bpmnprof::ActivityGroup")
bpmnprof_FlowNode = Class(name="bpmnprof::FlowNode", is_abstract=True)
FlowElement = Class(name="FlowElement")
bpmnprof_Comment = Class(name="bpmnprof::Comment")
bpmnprof_Stereotype = Class(name="bpmnprof::Stereotype")
BPMNArtifact = Class(name="BPMNArtifact")
bpmnprof_ExtensionAttributeValue = Class(name="bpmnprof::ExtensionAttributeValue")
bpmnprof_Element = Class(name="bpmnprof::Element")
bpmnprof_Documentation = Class(name="bpmnprof::Documentation")
bpmnprof_ExtensionDefinition = Class(name="bpmnprof::ExtensionDefinition")
bpmnprof_BPMNAssociation = Class(name="bpmnprof::BPMNAssociation")
bpmnprof_Slot = Class(name="bpmnprof::Slot")
bpmnprof_ExtensionAttributeDefinition = Class(name="bpmnprof::ExtensionAttributeDefinition")
bpmnprof_Property = Class(name="bpmnprof::Property")
bpmnprof_EnumerationLiteral = Class(name="bpmnprof::EnumerationLiteral")
bpmnprof_LaneSet = Class(name="bpmnprof::LaneSet")
bpmnprof_Dependency = Class(name="bpmnprof::Dependency")
bpmnprof_BPMNArtifact = Class(name="bpmnprof::BPMNArtifact", is_abstract=True)
bpmnprof_Class = Class(name="bpmnprof::Class")
bpmnprof_ActivityPartition = Class(name="bpmnprof::ActivityPartition")
bpmnprof_Lane = Class(name="bpmnprof::Lane")
bpmnprof_ControlFlow = Class(name="bpmnprof::ControlFlow")
bpmnprof_ParallelGateway = Class(name="bpmnprof::ParallelGateway")
bpmnprof_ComplexGateway = Class(name="bpmnprof::ComplexGateway")
bpmnprof_BPMNExpression = Class(name="bpmnprof::BPMNExpression")
bpmnprof_OpaqueExpression = Class(name="bpmnprof::OpaqueExpression")
bpmnprof_EventBasedGateway = Class(name="bpmnprof::EventBasedGateway")
bpmnprof_StructuredActivityNode = Class(name="bpmnprof::StructuredActivityNode")
bpmnprof_InterruptibleActivityRegion = Class(name="bpmnprof::InterruptibleActivityRegion")
bpmnprof_Package = Class(name="bpmnprof::Package")
bpmnprof_BPMNExtension = Class(name="bpmnprof::BPMNExtension")
bpmnprof_Import = Class(name="bpmnprof::Import")
bpmnprof_BPMNRelationship = Class(name="bpmnprof::BPMNRelationship")
bpmnprof_ExclusiveGateway = Class(name="bpmnprof::ExclusiveGateway")
bpmnprof_DecisionNode = Class(name="bpmnprof::DecisionNode")
bpmnprof_MergeNode = Class(name="bpmnprof::MergeNode")
bpmnprof_RootElement = Class(name="bpmnprof::RootElement", is_abstract=True)
bpmnprof_PackageableElement = Class(name="bpmnprof::PackageableElement")
bpmnprof_Definitions = Class(name="bpmnprof::Definitions")
bpmnprof_BPMNProcess = Class(name="bpmnprof::BPMNProcess")
CallableElement = Class(name="CallableElement")
FlowElementsContainer = Class(name="FlowElementsContainer")
bpmnprof_PackageImport = Class(name="bpmnprof::PackageImport")
bpmnprof_Constraint = Class(name="bpmnprof::Constraint")
bpmnprof_BPMNCollaboration = Class(name="bpmnprof::BPMNCollaboration")
bpmnprof_Activity = Class(name="bpmnprof::Activity")
bpmnprof_CorrelationSubscription = Class(name="bpmnprof::CorrelationSubscription")
bpmnprof_BPMNProperty = Class(name="bpmnprof::BPMNProperty")
bpmnprof_ResourceRole = Class(name="bpmnprof::ResourceRole")
bpmnprof_Action = Class(name="bpmnprof::Action")
bpmnprof_DataInput = Class(name="bpmnprof::DataInput")
bpmnprof_DataOutput = Class(name="bpmnprof::DataOutput")
bpmnprof_InputSet = Class(name="bpmnprof::InputSet")
bpmnprof_OutputSet = Class(name="bpmnprof::OutputSet")
ItemAwareElement = Class(name="ItemAwareElement")
bpmnprof_CallableElement = Class(name="bpmnprof::CallableElement", is_abstract=True)
RootElement = Class(name="RootElement")
bpmnprof_Behavior = Class(name="bpmnprof::Behavior")
bpmnprof_InputOutputSpecification = Class(name="bpmnprof::InputOutputSpecification")
bpmnprof_BPMNInterface = Class(name="bpmnprof::BPMNInterface")
bpmnprof_InputOutputBinding = Class(name="bpmnprof::InputOutputBinding")
bpmnprof_Parameter = Class(name="bpmnprof::Parameter")
bpmnprof_ActivityParameterNode = Class(name="bpmnprof::ActivityParameterNode")
bpmnprof_ItemAwareElement = Class(name="bpmnprof::ItemAwareElement", is_abstract=True)
bpmnprof_InputPin = Class(name="bpmnprof::InputPin")
bpmnprof_DataState = Class(name="bpmnprof::DataState")
bpmnprof_TypedElement = Class(name="bpmnprof::TypedElement")
bpmnprof_ItemDefinition = Class(name="bpmnprof::ItemDefinition")
bpmnprof_State = Class(name="bpmnprof::State")
bpmnprof_OutputPin = Class(name="bpmnprof::OutputPin")
bpmnprof_ParameterSet = Class(name="bpmnprof::ParameterSet")
bpmnprof_Interface = Class(name="bpmnprof::Interface")
bpmnprof_BPMNOperation = Class(name="bpmnprof::BPMNOperation")
bpmnprof_Error = Class(name="bpmnprof::Error")
ItemDefinition = Class(name="ItemDefinition")
bpmnprof_Operation = Class(name="bpmnprof::Operation")
bpmnprof_BPMNMessage = Class(name="bpmnprof::BPMNMessage")
bpmnprof_ConversationLink = Class(name="bpmnprof::ConversationLink")
bpmnprof_MessageFlowAssociation = Class(name="bpmnprof::MessageFlowAssociation")
bpmnprof_ParticipantAssociation = Class(name="bpmnprof::ParticipantAssociation")
bpmnprof_MessageFlow = Class(name="bpmnprof::MessageFlow")
bpmnprof_Collaboration = Class(name="bpmnprof::Collaboration")
bpmnprof_ConversationNode = Class(name="bpmnprof::ConversationNode", is_abstract=True)
bpmnprof_CorrelationKey = Class(name="bpmnprof::CorrelationKey")
bpmnprof_Participant = Class(name="bpmnprof::Participant")
bpmnprof_MultiplicityElement = Class(name="bpmnprof::MultiplicityElement")
bpmnprof_ParticipantMultiplicity = Class(name="bpmnprof::ParticipantMultiplicity")
bpmnprof_PartnerEntity = Class(name="bpmnprof::PartnerEntity")
bpmnprof_PartnerRole = Class(name="bpmnprof::PartnerRole")
bpmnprof_InteractionNode = Class(name="bpmnprof::InteractionNode", is_abstract=True)
bpmnprof_InstanceSpecification = Class(name="bpmnprof::InstanceSpecification")
bpmnprof_InformationFlow = Class(name="bpmnprof::InformationFlow")
InteractionNode = Class(name="InteractionNode")
bpmnprof_CorrelationPropertyRetrievalExpression = Class(name="bpmnprof::CorrelationPropertyRetrievalExpression")
bpmnprof_CorrelationProperty = Class(name="bpmnprof::CorrelationProperty")
bpmnprof_FormalExpression = Class(name="bpmnprof::FormalExpression")
BPMNExpression = Class(name="BPMNExpression")
bpmnprof_CorrelationPropertyBinding = Class(name="bpmnprof::CorrelationPropertyBinding")
bpmnprof_DataStoreNode = Class(name="bpmnprof::DataStoreNode")
bpmnprof_ResourceAssignmentExpression = Class(name="bpmnprof::ResourceAssignmentExpression")
bpmnprof_Resource = Class(name="bpmnprof::Resource")
bpmnprof_ResourceParameterBinding = Class(name="bpmnprof::ResourceParameterBinding")
bpmnprof_ResourceParameter = Class(name="bpmnprof::ResourceParameter")
bpmnprof_GlobalTask = Class(name="bpmnprof::GlobalTask")
bpmnprof_OpaqueBehavior = Class(name="bpmnprof::OpaqueBehavior")
bpmnprof_GlobalScriptTask = Class(name="bpmnprof::GlobalScriptTask")
GlobalTask = Class(name="GlobalTask")
bpmnprof_GlobalBusinessRuleTask = Class(name="bpmnprof::GlobalBusinessRuleTask")
bpmnprof_CompensateEventDefinition = Class(name="bpmnprof::CompensateEventDefinition")
EventDefinition = Class(name="EventDefinition")
bpmnprof_BPMNActivity = Class(name="bpmnprof::BPMNActivity", is_abstract=True)
bpmnprof_CallEvent = Class(name="bpmnprof::CallEvent")
bpmnprof_EventDefinition = Class(name="bpmnprof::EventDefinition", is_abstract=True)
bpmnprof_Event = Class(name="bpmnprof::Event")
bpmnprof_DataInputAssociation = Class(name="bpmnprof::DataInputAssociation")
bpmnprof_DataOutputAssociation = Class(name="bpmnprof::DataOutputAssociation")
bpmnprof_LoopCharacteristics = Class(name="bpmnprof::LoopCharacteristics", is_abstract=True)
bpmnprof_BoundaryEvent = Class(name="bpmnprof::BoundaryEvent")
CatchEvent = Class(name="CatchEvent")
bpmnprof_CatchEvent = Class(name="bpmnprof::CatchEvent", is_abstract=True)
BPMNEvent = Class(name="BPMNEvent")
bpmnprof_AcceptEventAction = Class(name="bpmnprof::AcceptEventAction")
bpmnprof_InitialNode = Class(name="bpmnprof::InitialNode")
bpmnprof_BPMNEvent = Class(name="bpmnprof::BPMNEvent", is_abstract=True)
bpmnprof_ObjectFlow = Class(name="bpmnprof::ObjectFlow")
DataAssociation = Class(name="DataAssociation")
bpmnprof_DataAssociation = Class(name="bpmnprof::DataAssociation", is_abstract=True)
bpmnprof_EscalationEventDefinition = Class(name="bpmnprof::EscalationEventDefinition")
bpmnprof_Escalation = Class(name="bpmnprof::Escalation")
bpmnprof_Assignment = Class(name="bpmnprof::Assignment")
bpmnprof_EndEvent = Class(name="bpmnprof::EndEvent")
ThrowEvent = Class(name="ThrowEvent")
bpmnprof_FinalNode = Class(name="bpmnprof::FinalNode")
bpmnprof_ThrowEvent = Class(name="bpmnprof::ThrowEvent", is_abstract=True)
bpmnprof_TimerEventDefinition = Class(name="bpmnprof::TimerEventDefinition")
bpmnprof_ChangeEvent = Class(name="bpmnprof::ChangeEvent")
bpmnprof_SignalEventDefinition = Class(name="bpmnprof::SignalEventDefinition")
bpmnprof_BPMNSignal = Class(name="bpmnprof::BPMNSignal")
bpmnprof_ErrorEventDefinition = Class(name="bpmnprof::ErrorEventDefinition")
bpmnprof_CallOperationAction = Class(name="bpmnprof::CallOperationAction")
bpmnprof_FlowFinalNode = Class(name="bpmnprof::FlowFinalNode")
bpmnprof_MessageEventDefinition = Class(name="bpmnprof::MessageEventDefinition")
bpmnprof_StartEvent = Class(name="bpmnprof::StartEvent")
bpmnprof_ConditionalEventDefinition = Class(name="bpmnprof::ConditionalEventDefinition")
bpmnprof_LinkEventDefinition = Class(name="bpmnprof::LinkEventDefinition")
bpmnprof_Enumeration = Class(name="bpmnprof::Enumeration")
bpmnprof_Group = Class(name="bpmnprof::Group")
bpmnprof_IntermediateCatchEvent = Class(name="bpmnprof::IntermediateCatchEvent")
bpmnprof_IntermediateThrowEvent = Class(name="bpmnprof::IntermediateThrowEvent")
bpmnprof_SendObjectAction = Class(name="bpmnprof::SendObjectAction")
bpmnprof_TerminateEventDefinition = Class(name="bpmnprof::TerminateEventDefinition")
bpmnprof_ImplicitThrowEvent = Class(name="bpmnprof::ImplicitThrowEvent")
bpmnprof_CancelEventDefinition = Class(name="bpmnprof::CancelEventDefinition")
bpmnprof_TextAnnotation = Class(name="bpmnprof::TextAnnotation")
bpmnprof_Category = Class(name="bpmnprof::Category")
bpmnprof_DataStore = Class(name="bpmnprof::DataStore")
bpmnprof_DataObjectReference = Class(name="bpmnprof::DataObjectReference")
bpmnprof_DataObject = Class(name="bpmnprof::DataObject")
bpmnprof_Rendering = Class(name="bpmnprof::Rendering")
bpmnprof_Task = Class(name="bpmnprof::Task")
BPMNActivity = Class(name="BPMNActivity")
bpmnprof_DataStoreReference = Class(name="bpmnprof::DataStoreReference")
bpmnprof_UserTask = Class(name="bpmnprof::UserTask")
Task = Class(name="Task")
bpmnprof_OpaqueAction = Class(name="bpmnprof::OpaqueAction")
bpmnprof_PotentialOwner = Class(name="bpmnprof::PotentialOwner")
HumanPerformer = Class(name="HumanPerformer")
bpmnprof_SubConversation = Class(name="bpmnprof::SubConversation")
ConversationNode = Class(name="ConversationNode")
bpmnprof_Image = Class(name="bpmnprof::Image")
bpmnprof_HumanPerformer = Class(name="bpmnprof::HumanPerformer")
Performer = Class(name="Performer")
bpmnprof_Performer = Class(name="bpmnprof::Performer")
ResourceRole = Class(name="ResourceRole")
bpmnprof_GlobalUserTask = Class(name="bpmnprof::GlobalUserTask")
bpmnprof_GlobalManualTask = Class(name="bpmnprof::GlobalManualTask")
bpmnprof_ManualTask = Class(name="bpmnprof::ManualTask")
bpmnprof_GlobalConversation = Class(name="bpmnprof::GlobalConversation")
BPMNCollaboration = Class(name="BPMNCollaboration")
bpmnprof_CallConversation = Class(name="bpmnprof::CallConversation")
bpmnprof_CollaborationUse = Class(name="bpmnprof::CollaborationUse")
bpmnprof_Conversation = Class(name="bpmnprof::Conversation")
bpmnprof_SubProcess = Class(name="bpmnprof::SubProcess")
bpmnprof_ComplexBehaviorDefinition = Class(name="bpmnprof::ComplexBehaviorDefinition")
bpmnprof_CallActivity = Class(name="bpmnprof::CallActivity")
bpmnprof_CallBehaviorAction = Class(name="bpmnprof::CallBehaviorAction")
bpmnprof_BusinessRuleTask = Class(name="bpmnprof::BusinessRuleTask")
bpmnprof_Transaction = Class(name="bpmnprof::Transaction")
bpmnprof_AdHocSubProcess = Class(name="bpmnprof::AdHocSubProcess")
SubProcess = Class(name="SubProcess")
bpmnprof_ScriptTask = Class(name="bpmnprof::ScriptTask")
bpmnprof_SendTask = Class(name="bpmnprof::SendTask")
bpmnprof_ServiceTask = Class(name="bpmnprof::ServiceTask")
bpmnprof_StandardLoopCharacteristics = Class(name="bpmnprof::StandardLoopCharacteristics")
LoopCharacteristics = Class(name="LoopCharacteristics")
bpmnprof_LoopNode = Class(name="bpmnprof::LoopNode")
bpmnprof_ReceiveTask = Class(name="bpmnprof::ReceiveTask")
bpmnprof_ExpansionRegion = Class(name="bpmnprof::ExpansionRegion")
bpmnprof_MultiInstanceLoopCharacteristics = Class(name="bpmnprof::MultiInstanceLoopCharacteristics")

# bpmnprof_InclusiveGateway class attributes and methods
bpmnprof_InclusiveGateway_m_inclusiveGatewaydefault: Method = Method(name="inclusiveGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_InclusiveGateway.methods={bpmnprof_InclusiveGateway_m_inclusiveGatewaydefault}

# NonExclusiveGateway class attributes and methods

# bpmnprof_ActivityNode class attributes and methods

# bpmnprof_FlowElement class attributes and methods

# BaseElement class attributes and methods

# bpmnprof_Auditing class attributes and methods

# bpmnprof_Monitoring class attributes and methods

# bpmnprof_CategoryValue class attributes and methods

# bpmnprof_FlowElementsContainer class attributes and methods

# bpmnprof_BaseElement class attributes and methods
bpmnprof_BaseElement_id: Property = Property(name="id", type=StringType)
bpmnprof_BaseElement.attributes={bpmnprof_BaseElement_id}

# bpmnprof_SequenceFlow class attributes and methods
bpmnprof_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=StringType)
bpmnprof_SequenceFlow_m_SequenceFlowsourceRef: Method = Method(name="SequenceFlowsourceRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_SequenceFlow_m_SequenceFlowtargetRef: Method = Method(name="SequenceFlowtargetRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_SequenceFlow_m_SequenceFlowconditionExpression: Method = Method(name="SequenceFlowconditionExpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_SequenceFlow.attributes={bpmnprof_SequenceFlow_isImmediate}
bpmnprof_SequenceFlow.methods={bpmnprof_SequenceFlow_m_SequenceFlowsourceRef, bpmnprof_SequenceFlow_m_SequenceFlowconditionExpression, bpmnprof_SequenceFlow_m_SequenceFlowtargetRef}

# bpmnprof_NonExclusiveGateway class attributes and methods

# Gateway class attributes and methods

# bpmnprof_JoinNode class attributes and methods

# bpmnprof_ForkNode class attributes and methods

# bpmnprof_Gateway class attributes and methods

# FlowNode class attributes and methods

# bpmnprof_ControlNode class attributes and methods

# bpmnprof_ActivityGroup class attributes and methods

# bpmnprof_FlowNode class attributes and methods

# FlowElement class attributes and methods

# bpmnprof_Comment class attributes and methods

# bpmnprof_Stereotype class attributes and methods

# BPMNArtifact class attributes and methods

# bpmnprof_ExtensionAttributeValue class attributes and methods

# bpmnprof_Element class attributes and methods

# bpmnprof_Documentation class attributes and methods
bpmnprof_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmnprof_Documentation_text: Property = Property(name="text", type=StringType)
bpmnprof_Documentation.attributes={bpmnprof_Documentation_text, bpmnprof_Documentation_textFormat}

# bpmnprof_ExtensionDefinition class attributes and methods

# bpmnprof_BPMNAssociation class attributes and methods
bpmnprof_BPMNAssociation_associationDirection: Property = Property(name="associationDirection", type=StringType)
bpmnprof_BPMNAssociation_m_AssociationEnd: Method = Method(name="AssociationEnd", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNAssociation.attributes={bpmnprof_BPMNAssociation_associationDirection}
bpmnprof_BPMNAssociation.methods={bpmnprof_BPMNAssociation_m_AssociationEnd}

# bpmnprof_Slot class attributes and methods

# bpmnprof_ExtensionAttributeDefinition class attributes and methods
bpmnprof_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
bpmnprof_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=StringType)
bpmnprof_ExtensionAttributeDefinition.attributes={bpmnprof_ExtensionAttributeDefinition_type, bpmnprof_ExtensionAttributeDefinition_isReference}

# bpmnprof_Property class attributes and methods

# bpmnprof_EnumerationLiteral class attributes and methods

# bpmnprof_LaneSet class attributes and methods
bpmnprof_LaneSet_m_LaneSetlanes: Method = Method(name="LaneSetlanes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_LaneSet_m_LaneSetparentLane: Method = Method(name="LaneSetparentLane", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_LaneSet_m_LaneSetflowElementsContainer: Method = Method(name="LaneSetflowElementsContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_LaneSet_m_LaneSet: Method = Method(name="LaneSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_LaneSet.methods={bpmnprof_LaneSet_m_LaneSetlanes, bpmnprof_LaneSet_m_LaneSetparentLane, bpmnprof_LaneSet_m_LaneSetflowElementsContainer, bpmnprof_LaneSet_m_LaneSet}

# bpmnprof_Dependency class attributes and methods

# bpmnprof_BPMNArtifact class attributes and methods

# bpmnprof_Class class attributes and methods

# bpmnprof_ActivityPartition class attributes and methods

# bpmnprof_Lane class attributes and methods
bpmnprof_Lane_m_LanelaneSet: Method = Method(name="LanelaneSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Lane_m_LanechildLaneSet: Method = Method(name="LanechildLaneSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_Lane_m_LanepartitionElementRef: Method = Method(name="LanepartitionElementRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Lane_m_LaneflowNodeRefs: Method = Method(name="LaneflowNodeRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Lane.methods={bpmnprof_Lane_m_LanelaneSet, bpmnprof_Lane_m_LaneflowNodeRefs, bpmnprof_Lane_m_LanechildLaneSet, bpmnprof_Lane_m_LanepartitionElementRef}

# bpmnprof_ControlFlow class attributes and methods

# bpmnprof_ParallelGateway class attributes and methods

# bpmnprof_ComplexGateway class attributes and methods
bpmnprof_ComplexGateway_m_complexGatewaydefault: Method = Method(name="complexGatewaydefault", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ComplexGateway_m_complexGatewayactivationCondition: Method = Method(name="complexGatewayactivationCondition", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ComplexGateway_m_complexGatewayjoinSpec: Method = Method(name="complexGatewayjoinSpec", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ComplexGateway.methods={bpmnprof_ComplexGateway_m_complexGatewayactivationCondition, bpmnprof_ComplexGateway_m_complexGatewaydefault, bpmnprof_ComplexGateway_m_complexGatewayjoinSpec}

# bpmnprof_BPMNExpression class attributes and methods

# bpmnprof_OpaqueExpression class attributes and methods

# bpmnprof_EventBasedGateway class attributes and methods
bpmnprof_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=StringType)
bpmnprof_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
bpmnprof_EventBasedGateway.attributes={bpmnprof_EventBasedGateway_eventGatewayType, bpmnprof_EventBasedGateway_instantiate}

# bpmnprof_StructuredActivityNode class attributes and methods

# bpmnprof_InterruptibleActivityRegion class attributes and methods

# bpmnprof_Package class attributes and methods

# bpmnprof_BPMNExtension class attributes and methods
bpmnprof_BPMNExtension_mustUnderstand: Property = Property(name="mustUnderstand", type=StringType)
bpmnprof_BPMNExtension.attributes={bpmnprof_BPMNExtension_mustUnderstand}

# bpmnprof_Import class attributes and methods
bpmnprof_Import_importType: Property = Property(name="importType", type=StringType)
bpmnprof_Import_location: Property = Property(name="location", type=StringType)
bpmnprof_Import_namespace: Property = Property(name="namespace", type=StringType)
bpmnprof_Import.attributes={bpmnprof_Import_importType, bpmnprof_Import_namespace, bpmnprof_Import_location}

# bpmnprof_BPMNRelationship class attributes and methods
bpmnprof_BPMNRelationship_type: Property = Property(name="type", type=StringType)
bpmnprof_BPMNRelationship_direction: Property = Property(name="direction", type=StringType)
bpmnprof_BPMNRelationship.attributes={bpmnprof_BPMNRelationship_direction, bpmnprof_BPMNRelationship_type}

# bpmnprof_ExclusiveGateway class attributes and methods
bpmnprof_ExclusiveGateway_m_exclusiveGatewaydefault: Method = Method(name="exclusiveGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ExclusiveGateway.methods={bpmnprof_ExclusiveGateway_m_exclusiveGatewaydefault}

# bpmnprof_DecisionNode class attributes and methods

# bpmnprof_MergeNode class attributes and methods

# bpmnprof_RootElement class attributes and methods

# bpmnprof_PackageableElement class attributes and methods

# bpmnprof_Definitions class attributes and methods
bpmnprof_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
bpmnprof_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
bpmnprof_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
bpmnprof_Definitions_exporter: Property = Property(name="exporter", type=StringType)
bpmnprof_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
bpmnprof_Definitions.attributes={bpmnprof_Definitions_exporter, bpmnprof_Definitions_targetNamespace, bpmnprof_Definitions_expressionLanguage, bpmnprof_Definitions_exporterVersion, bpmnprof_Definitions_typeLanguage}

# bpmnprof_BPMNProcess class attributes and methods
bpmnprof_BPMNProcess_isExecutable: Property = Property(name="isExecutable", type=StringType)
bpmnprof_BPMNProcess_processType: Property = Property(name="processType", type=StringType)
bpmnprof_BPMNProcess_isClosed: Property = Property(name="isClosed", type=StringType)
bpmnprof_BPMNProcess_m_ProcesssupportedInterfaceRefs: Method = Method(name="ProcesssupportedInterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNProcess_m_Processsupports: Method = Method(name="Processsupports", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNProcess_m_Processproperties: Method = Method(name="Processproperties", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNProcess_m_ProcesslaneSets: Method = Method(name="ProcesslaneSets", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNProcess_m_ProcessflowElements: Method = Method(name="ProcessflowElements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNProcess.attributes={bpmnprof_BPMNProcess_isClosed, bpmnprof_BPMNProcess_processType, bpmnprof_BPMNProcess_isExecutable}
bpmnprof_BPMNProcess.methods={bpmnprof_BPMNProcess_m_ProcesssupportedInterfaceRefs, bpmnprof_BPMNProcess_m_Processproperties, bpmnprof_BPMNProcess_m_Processsupports, bpmnprof_BPMNProcess_m_ProcessflowElements, bpmnprof_BPMNProcess_m_ProcesslaneSets}

# CallableElement class attributes and methods

# FlowElementsContainer class attributes and methods

# bpmnprof_PackageImport class attributes and methods

# bpmnprof_Constraint class attributes and methods

# bpmnprof_BPMNCollaboration class attributes and methods
bpmnprof_BPMNCollaboration_isClosed: Property = Property(name="isClosed", type=StringType)
bpmnprof_BPMNCollaboration_m_Collaborationparticipants: Method = Method(name="Collaborationparticipants", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNCollaboration.attributes={bpmnprof_BPMNCollaboration_isClosed}
bpmnprof_BPMNCollaboration.methods={bpmnprof_BPMNCollaboration_m_Collaborationparticipants}

# bpmnprof_Activity class attributes and methods

# bpmnprof_CorrelationSubscription class attributes and methods

# bpmnprof_BPMNProperty class attributes and methods
bpmnprof_BPMNProperty_m_Propertynotation: Method = Method(name="Propertynotation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNProperty_m_BPMNPropertyapply: Method = Method(name="BPMNPropertyapply", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNProperty.methods={bpmnprof_BPMNProperty_m_Propertynotation, bpmnprof_BPMNProperty_m_BPMNPropertyapply}

# bpmnprof_ResourceRole class attributes and methods
bpmnprof_ResourceRole_m_ResourceRoleowner: Method = Method(name="ResourceRoleowner", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ResourceRole_m_ResourceRoleresourceRef: Method = Method(name="ResourceRoleresourceRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ResourceRole_m_ResourceRoleresourceParameterBindings: Method = Method(name="ResourceRoleresourceParameterBindings", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ResourceRole_m_ResourceRoleisRequired: Method = Method(name="ResourceRoleisRequired", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceRole_m_ResourceRoleprocess: Method = Method(name="ResourceRoleprocess", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ResourceRole.methods={bpmnprof_ResourceRole_m_ResourceRoleowner, bpmnprof_ResourceRole_m_ResourceRoleresourceParameterBindings, bpmnprof_ResourceRole_m_ResourceRoleprocess, bpmnprof_ResourceRole_m_ResourceRoleisRequired, bpmnprof_ResourceRole_m_ResourceRoleresourceRef}

# bpmnprof_Action class attributes and methods

# bpmnprof_DataInput class attributes and methods
bpmnprof_DataInput_isCollection: Property = Property(name="isCollection", type=StringType)
bpmnprof_DataInput_m_DataInputAssociation: Method = Method(name="DataInputAssociation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataInput_m_DataInputnotation: Method = Method(name="DataInputnotation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataInput_m_DataInputitemSubjectRef: Method = Method(name="DataInputitemSubjectRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataInput.attributes={bpmnprof_DataInput_isCollection}
bpmnprof_DataInput.methods={bpmnprof_DataInput_m_DataInputAssociation, bpmnprof_DataInput_m_DataInputnotation, bpmnprof_DataInput_m_DataInputitemSubjectRef}

# bpmnprof_DataOutput class attributes and methods
bpmnprof_DataOutput_isCollection: Property = Property(name="isCollection", type=StringType)
bpmnprof_DataOutput_m_DataOutputnotation: Method = Method(name="DataOutputnotation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataOutput_m_DataOutputitemSubjectRef: Method = Method(name="DataOutputitemSubjectRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataOutput.attributes={bpmnprof_DataOutput_isCollection}
bpmnprof_DataOutput.methods={bpmnprof_DataOutput_m_DataOutputitemSubjectRef, bpmnprof_DataOutput_m_DataOutputnotation}

# bpmnprof_InputSet class attributes and methods
bpmnprof_InputSet_m_InputSetdataInputRefs: Method = Method(name="InputSetdataInputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_InputSet_m_InputSetoptionalInputRefs: Method = Method(name="InputSetoptionalInputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_InputSet_m_InputSetwhileExecutingInputRefs: Method = Method(name="InputSetwhileExecutingInputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_InputSet.methods={bpmnprof_InputSet_m_InputSetoptionalInputRefs, bpmnprof_InputSet_m_InputSetdataInputRefs, bpmnprof_InputSet_m_InputSetwhileExecutingInputRefs}

# bpmnprof_OutputSet class attributes and methods
bpmnprof_OutputSet_m_OutputSetwhileExecutingOutputRefs: Method = Method(name="OutputSetwhileExecutingOutputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_OutputSet_m_OutputSetdataOutputRefs: Method = Method(name="OutputSetdataOutputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_OutputSet_m_OutputSetoptionalOutputRefs: Method = Method(name="OutputSetoptionalOutputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_OutputSet.methods={bpmnprof_OutputSet_m_OutputSetoptionalOutputRefs, bpmnprof_OutputSet_m_OutputSetdataOutputRefs, bpmnprof_OutputSet_m_OutputSetwhileExecutingOutputRefs}

# ItemAwareElement class attributes and methods

# bpmnprof_CallableElement class attributes and methods
bpmnprof_CallableElement_m_CallableEelementsupportedInterfaceRefs: Method = Method(name="CallableEelementsupportedInterfaceRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_CallableElement_m_CallableElementresources: Method = Method(name="CallableElementresources", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_CallableElement.methods={bpmnprof_CallableElement_m_CallableEelementsupportedInterfaceRefs, bpmnprof_CallableElement_m_CallableElementresources}

# RootElement class attributes and methods

# bpmnprof_Behavior class attributes and methods

# bpmnprof_InputOutputSpecification class attributes and methods

# bpmnprof_BPMNInterface class attributes and methods
bpmnprof_BPMNInterface_m_Interfaceoperationmultiplicity: Method = Method(name="Interfaceoperationmultiplicity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNInterface_m_InterfaceownedOperation: Method = Method(name="InterfaceownedOperation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNInterface_m_BPMNInterfacecallableElements: Method = Method(name="BPMNInterfacecallableElements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNInterface_m_BPMNInterfaceoperations: Method = Method(name="BPMNInterfaceoperations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNInterface.methods={bpmnprof_BPMNInterface_m_Interfaceoperationmultiplicity, bpmnprof_BPMNInterface_m_BPMNInterfaceoperations, bpmnprof_BPMNInterface_m_InterfaceownedOperation, bpmnprof_BPMNInterface_m_BPMNInterfacecallableElements}

# bpmnprof_InputOutputBinding class attributes and methods

# bpmnprof_Parameter class attributes and methods

# bpmnprof_ActivityParameterNode class attributes and methods

# bpmnprof_ItemAwareElement class attributes and methods
bpmnprof_ItemAwareElement_m_ItemAwareElementdataState: Method = Method(name="ItemAwareElementdataState", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ItemAwareElement.methods={bpmnprof_ItemAwareElement_m_ItemAwareElementdataState}

# bpmnprof_InputPin class attributes and methods

# bpmnprof_DataState class attributes and methods

# bpmnprof_TypedElement class attributes and methods

# bpmnprof_ItemDefinition class attributes and methods
bpmnprof_ItemDefinition_isCollection: Property = Property(name="isCollection", type=StringType)
bpmnprof_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
bpmnprof_ItemDefinition_m_ItemDefinitionstructureRef: Method = Method(name="ItemDefinitionstructureRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ItemDefinition.attributes={bpmnprof_ItemDefinition_itemKind, bpmnprof_ItemDefinition_isCollection}
bpmnprof_ItemDefinition.methods={bpmnprof_ItemDefinition_m_ItemDefinitionstructureRef}

# bpmnprof_State class attributes and methods

# bpmnprof_OutputPin class attributes and methods

# bpmnprof_ParameterSet class attributes and methods

# bpmnprof_Interface class attributes and methods

# bpmnprof_BPMNOperation class attributes and methods
bpmnprof_BPMNOperation_m_BPMNOperationowner: Method = Method(name="BPMNOperationowner", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNOperation_m_BPMNOperationinMessageRef: Method = Method(name="BPMNOperationinMessageRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNOperation_m_BPMNOperationoutMessageRef: Method = Method(name="BPMNOperationoutMessageRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNOperation_m_BPMNOperationerrorRefs: Method = Method(name="BPMNOperationerrorRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNOperation.methods={bpmnprof_BPMNOperation_m_BPMNOperationinMessageRef, bpmnprof_BPMNOperation_m_BPMNOperationoutMessageRef, bpmnprof_BPMNOperation_m_BPMNOperationowner, bpmnprof_BPMNOperation_m_BPMNOperationerrorRefs}

# bpmnprof_Error class attributes and methods
bpmnprof_Error_errorCode: Property = Property(name="errorCode", type=StringType)
bpmnprof_Error.attributes={bpmnprof_Error_errorCode}

# ItemDefinition class attributes and methods

# bpmnprof_Operation class attributes and methods

# bpmnprof_BPMNMessage class attributes and methods
bpmnprof_BPMNMessage_m_MessageitemRef: Method = Method(name="MessageitemRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNMessage.methods={bpmnprof_BPMNMessage_m_MessageitemRef}

# bpmnprof_ConversationLink class attributes and methods

# bpmnprof_MessageFlowAssociation class attributes and methods
bpmnprof_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef: Method = Method(name="MessageFlowAssociationinnerMessageFlowRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef: Method = Method(name="MessageFlowAssociationouterMessageFlowRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_MessageFlowAssociation.methods={bpmnprof_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef, bpmnprof_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef}

# bpmnprof_ParticipantAssociation class attributes and methods
bpmnprof_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef: Method = Method(name="ParticipantAssociationinnerParticipantRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef: Method = Method(name="ParticipantAssociationouterParticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ParticipantAssociation.methods={bpmnprof_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef, bpmnprof_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef}

# bpmnprof_MessageFlow class attributes and methods
bpmnprof_MessageFlow_m_MessageFlowsourceRef: Method = Method(name="MessageFlowsourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_MessageFlow_m_MessageFlowtargetRef: Method = Method(name="MessageFlowtargetRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_MessageFlow_m_MessageFlowmessageRef: Method = Method(name="MessageFlowmessageRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_MessageFlow.methods={bpmnprof_MessageFlow_m_MessageFlowsourceRef, bpmnprof_MessageFlow_m_MessageFlowtargetRef, bpmnprof_MessageFlow_m_MessageFlowmessageRef}

# bpmnprof_Collaboration class attributes and methods

# bpmnprof_ConversationNode class attributes and methods
bpmnprof_ConversationNode_m_ConversationNodeparticipantRefs: Method = Method(name="ConversationNodeparticipantRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ConversationNode.methods={bpmnprof_ConversationNode_m_ConversationNodeparticipantRefs}

# bpmnprof_CorrelationKey class attributes and methods

# bpmnprof_Participant class attributes and methods
bpmnprof_Participant_m_Participantownership: Method = Method(name="Participantownership", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant_m_ParticipantmultiplicityMaximum: Method = Method(name="ParticipantmultiplicityMaximum", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_Participant_m_participantpartnerEntityRef: Method = Method(name="participantpartnerEntityRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_Participant_m_participantpartnerRoleRef: Method = Method(name="participantpartnerRoleRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant_m_ParticipantinterfaceRefs: Method = Method(name="ParticipantinterfaceRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant_m_Participanttype: Method = Method(name="Participanttype", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_Participant_m_ParticipantmultiplicityMinimum: Method = Method(name="ParticipantmultiplicityMinimum", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant_m_Participantrealizationsupplier: Method = Method(name="Participantrealizationsupplier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant_m_ParticipantprocessRef: Method = Method(name="ParticipantprocessRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Participant.methods={bpmnprof_Participant_m_participantpartnerEntityRef, bpmnprof_Participant_m_Participantownership, bpmnprof_Participant_m_Participantrealizationsupplier, bpmnprof_Participant_m_ParticipantinterfaceRefs, bpmnprof_Participant_m_ParticipantmultiplicityMinimum, bpmnprof_Participant_m_ParticipantprocessRef, bpmnprof_Participant_m_ParticipantmultiplicityMaximum, bpmnprof_Participant_m_Participanttype, bpmnprof_Participant_m_participantpartnerRoleRef}

# bpmnprof_MultiplicityElement class attributes and methods

# bpmnprof_ParticipantMultiplicity class attributes and methods
bpmnprof_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=StringType)
bpmnprof_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=StringType)
bpmnprof_ParticipantMultiplicity.attributes={bpmnprof_ParticipantMultiplicity_minimum, bpmnprof_ParticipantMultiplicity_maximum}

# bpmnprof_PartnerEntity class attributes and methods
bpmnprof_PartnerEntity_m_PartnerEntityparticipantRef: Method = Method(name="PartnerEntityparticipantRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_PartnerEntity.methods={bpmnprof_PartnerEntity_m_PartnerEntityparticipantRef}

# bpmnprof_PartnerRole class attributes and methods
bpmnprof_PartnerRole_m_PartnerRoleparticipantRef: Method = Method(name="PartnerRoleparticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_PartnerRole.methods={bpmnprof_PartnerRole_m_PartnerRoleparticipantRef}

# bpmnprof_InteractionNode class attributes and methods

# bpmnprof_InstanceSpecification class attributes and methods

# bpmnprof_InformationFlow class attributes and methods

# InteractionNode class attributes and methods

# bpmnprof_CorrelationPropertyRetrievalExpression class attributes and methods

# bpmnprof_CorrelationProperty class attributes and methods

# bpmnprof_FormalExpression class attributes and methods
bpmnprof_FormalExpression_m_FormalExpressionevaluatesToTypeRef: Method = Method(name="FormalExpressionevaluatesToTypeRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_FormalExpression.methods={bpmnprof_FormalExpression_m_FormalExpressionevaluatesToTypeRef}

# BPMNExpression class attributes and methods

# bpmnprof_CorrelationPropertyBinding class attributes and methods

# bpmnprof_DataStoreNode class attributes and methods

# bpmnprof_ResourceAssignmentExpression class attributes and methods
bpmnprof_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression: Method = Method(name="ResourceAssignmentExpressionexpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceAssignmentExpression.methods={bpmnprof_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression}

# bpmnprof_Resource class attributes and methods
bpmnprof_Resource_m_ResourceresourceParameters: Method = Method(name="ResourceresourceParameters", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_Resource.methods={bpmnprof_Resource_m_ResourceresourceParameters}

# bpmnprof_ResourceParameterBinding class attributes and methods
bpmnprof_ResourceParameterBinding_m_ResourceParameterBindingexpression: Method = Method(name="ResourceParameterBindingexpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceParameterBinding_m_ResourceParameterBindingparameterRef: Method = Method(name="ResourceParameterBindingparameterRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceParameterBinding.methods={bpmnprof_ResourceParameterBinding_m_ResourceParameterBindingexpression, bpmnprof_ResourceParameterBinding_m_ResourceParameterBindingparameterRef}

# bpmnprof_ResourceParameter class attributes and methods
bpmnprof_ResourceParameter_isRequired: Property = Property(name="isRequired", type=StringType)
bpmnprof_ResourceParameter_m_ResourceParameterowner: Method = Method(name="ResourceParameterowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceParameter_m_ResourceParametertype: Method = Method(name="ResourceParametertype", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceParameter_m_ResourceParameterisRequired: Method = Method(name="ResourceParameterisRequired", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ResourceParameter.attributes={bpmnprof_ResourceParameter_isRequired}
bpmnprof_ResourceParameter.methods={bpmnprof_ResourceParameter_m_ResourceParameterisRequired, bpmnprof_ResourceParameter_m_ResourceParametertype, bpmnprof_ResourceParameter_m_ResourceParameterowner}

# bpmnprof_GlobalTask class attributes and methods
bpmnprof_GlobalTask_m_GlobalTasksupportedInterfaceRefs: Method = Method(name="GlobalTasksupportedInterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_GlobalTask.methods={bpmnprof_GlobalTask_m_GlobalTasksupportedInterfaceRefs}

# bpmnprof_OpaqueBehavior class attributes and methods

# bpmnprof_GlobalScriptTask class attributes and methods
bpmnprof_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
bpmnprof_GlobalScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
bpmnprof_GlobalScriptTask_m_GlobalScriptTaskscriptFormat: Method = Method(name="GlobalScriptTaskscriptFormat", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_GlobalScriptTask_m_GlobalScriptTaskscript: Method = Method(name="GlobalScriptTaskscript", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_GlobalScriptTask.attributes={bpmnprof_GlobalScriptTask_script, bpmnprof_GlobalScriptTask_scriptFormat}
bpmnprof_GlobalScriptTask.methods={bpmnprof_GlobalScriptTask_m_GlobalScriptTaskscriptFormat, bpmnprof_GlobalScriptTask_m_GlobalScriptTaskscript}

# GlobalTask class attributes and methods

# bpmnprof_GlobalBusinessRuleTask class attributes and methods
bpmnprof_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation: Method = Method(name="GlobalBusinessRuleTaskimplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_GlobalBusinessRuleTask.attributes={bpmnprof_GlobalBusinessRuleTask_implementation}
bpmnprof_GlobalBusinessRuleTask.methods={bpmnprof_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation}

# bpmnprof_CompensateEventDefinition class attributes and methods
bpmnprof_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=StringType)
bpmnprof_CompensateEventDefinition.attributes={bpmnprof_CompensateEventDefinition_waitForCompletion}

# EventDefinition class attributes and methods

# bpmnprof_BPMNActivity class attributes and methods
bpmnprof_BPMNActivity_isForCompensation: Property = Property(name="isForCompensation", type=StringType)
bpmnprof_BPMNActivity_startQuantity: Property = Property(name="startQuantity", type=StringType)
bpmnprof_BPMNActivity_completionQuantity: Property = Property(name="completionQuantity", type=StringType)
bpmnprof_BPMNActivity_m_BPMNActivitycontainer: Method = Method(name="BPMNActivitycontainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNActivity_m_BPMNActivityproperties: Method = Method(name="BPMNActivityproperties", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNActivity_m_BPMNActivityresources: Method = Method(name="BPMNActivityresources", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNActivity_m_BPMNActivitydefault: Method = Method(name="BPMNActivitydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNActivity_m_BPMNActivityboundaryEventsRefs: Method = Method(name="BPMNActivityboundaryEventsRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_BPMNActivity_m_BPMNActivityloopCharacteristics: Method = Method(name="BPMNActivityloopCharacteristics", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNActivity.attributes={bpmnprof_BPMNActivity_completionQuantity, bpmnprof_BPMNActivity_startQuantity, bpmnprof_BPMNActivity_isForCompensation}
bpmnprof_BPMNActivity.methods={bpmnprof_BPMNActivity_m_BPMNActivityproperties, bpmnprof_BPMNActivity_m_BPMNActivitycontainer, bpmnprof_BPMNActivity_m_BPMNActivityloopCharacteristics, bpmnprof_BPMNActivity_m_BPMNActivityboundaryEventsRefs, bpmnprof_BPMNActivity_m_BPMNActivityresources, bpmnprof_BPMNActivity_m_BPMNActivitydefault}

# bpmnprof_CallEvent class attributes and methods

# bpmnprof_EventDefinition class attributes and methods

# bpmnprof_Event class attributes and methods

# bpmnprof_DataInputAssociation class attributes and methods
bpmnprof_DataInputAssociation_m_dataInputAssociationsource: Method = Method(name="dataInputAssociationsource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataInputAssociation_m_dataInputAssociationtarget: Method = Method(name="dataInputAssociationtarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataInputAssociation.methods={bpmnprof_DataInputAssociation_m_dataInputAssociationtarget, bpmnprof_DataInputAssociation_m_dataInputAssociationsource}

# bpmnprof_DataOutputAssociation class attributes and methods
bpmnprof_DataOutputAssociation_m_dataOutputAssociationsource: Method = Method(name="dataOutputAssociationsource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataOutputAssociation_m_dataOutputAssociationtarget: Method = Method(name="dataOutputAssociationtarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataOutputAssociation.methods={bpmnprof_DataOutputAssociation_m_dataOutputAssociationtarget, bpmnprof_DataOutputAssociation_m_dataOutputAssociationsource}

# bpmnprof_LoopCharacteristics class attributes and methods

# bpmnprof_BoundaryEvent class attributes and methods
bpmnprof_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=StringType)
bpmnprof_BoundaryEvent_m_boundaryEventattachedToRef: Method = Method(name="boundaryEventattachedToRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BoundaryEvent.attributes={bpmnprof_BoundaryEvent_cancelActivity}
bpmnprof_BoundaryEvent.methods={bpmnprof_BoundaryEvent_m_boundaryEventattachedToRef}

# CatchEvent class attributes and methods

# bpmnprof_CatchEvent class attributes and methods
bpmnprof_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=StringType)
bpmnprof_CatchEvent_m_catchEventeventDefinitionsRefs: Method = Method(name="catchEventeventDefinitionsRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_CatchEvent.attributes={bpmnprof_CatchEvent_parallelMultiple}
bpmnprof_CatchEvent.methods={bpmnprof_CatchEvent_m_catchEventeventDefinitionsRefs}

# BPMNEvent class attributes and methods

# bpmnprof_AcceptEventAction class attributes and methods

# bpmnprof_InitialNode class attributes and methods

# bpmnprof_BPMNEvent class attributes and methods

# bpmnprof_ObjectFlow class attributes and methods

# DataAssociation class attributes and methods

# bpmnprof_DataAssociation class attributes and methods
bpmnprof_DataAssociation_m_DataAssociationsource: Method = Method(name="DataAssociationsource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataAssociation_m_DataAssociationtransformation: Method = Method(name="DataAssociationtransformation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataAssociation_m_DataAssociationtarget: Method = Method(name="DataAssociationtarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataAssociation.methods={bpmnprof_DataAssociation_m_DataAssociationtransformation, bpmnprof_DataAssociation_m_DataAssociationtarget, bpmnprof_DataAssociation_m_DataAssociationsource}

# bpmnprof_EscalationEventDefinition class attributes and methods

# bpmnprof_Escalation class attributes and methods
bpmnprof_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
bpmnprof_Escalation_m_EscalationstructureRef: Method = Method(name="EscalationstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_Escalation.attributes={bpmnprof_Escalation_escalationCode}
bpmnprof_Escalation.methods={bpmnprof_Escalation_m_EscalationstructureRef}

# bpmnprof_Assignment class attributes and methods

# bpmnprof_EndEvent class attributes and methods

# ThrowEvent class attributes and methods

# bpmnprof_FinalNode class attributes and methods

# bpmnprof_ThrowEvent class attributes and methods
bpmnprof_ThrowEvent_m_ThrowEventeventDefinitionRefs: Method = Method(name="ThrowEventeventDefinitionRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ThrowEvent.methods={bpmnprof_ThrowEvent_m_ThrowEventeventDefinitionRefs}

# bpmnprof_TimerEventDefinition class attributes and methods

# bpmnprof_ChangeEvent class attributes and methods

# bpmnprof_SignalEventDefinition class attributes and methods

# bpmnprof_BPMNSignal class attributes and methods
bpmnprof_BPMNSignal_m_BPMNSignalstructureRef: Method = Method(name="BPMNSignalstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BPMNSignal.methods={bpmnprof_BPMNSignal_m_BPMNSignalstructureRef}

# bpmnprof_ErrorEventDefinition class attributes and methods

# bpmnprof_CallOperationAction class attributes and methods

# bpmnprof_FlowFinalNode class attributes and methods

# bpmnprof_MessageEventDefinition class attributes and methods

# bpmnprof_StartEvent class attributes and methods
bpmnprof_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=StringType)
bpmnprof_StartEvent.attributes={bpmnprof_StartEvent_isInterrupting}

# bpmnprof_ConditionalEventDefinition class attributes and methods
bpmnprof_ConditionalEventDefinition_m_conditionalEventDefinitioncondition: Method = Method(name="conditionalEventDefinitioncondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ConditionalEventDefinition.methods={bpmnprof_ConditionalEventDefinition_m_conditionalEventDefinitioncondition}

# bpmnprof_LinkEventDefinition class attributes and methods

# bpmnprof_Enumeration class attributes and methods

# bpmnprof_Group class attributes and methods

# bpmnprof_IntermediateCatchEvent class attributes and methods

# bpmnprof_IntermediateThrowEvent class attributes and methods

# bpmnprof_SendObjectAction class attributes and methods

# bpmnprof_TerminateEventDefinition class attributes and methods

# bpmnprof_ImplicitThrowEvent class attributes and methods

# bpmnprof_CancelEventDefinition class attributes and methods

# bpmnprof_TextAnnotation class attributes and methods
bpmnprof_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmnprof_TextAnnotation_text: Property = Property(name="text", type=StringType)
bpmnprof_TextAnnotation.attributes={bpmnprof_TextAnnotation_text, bpmnprof_TextAnnotation_textFormat}

# bpmnprof_Category class attributes and methods

# bpmnprof_DataStore class attributes and methods
bpmnprof_DataStore_capacity: Property = Property(name="capacity", type=StringType)
bpmnprof_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=StringType)
bpmnprof_DataStore.attributes={bpmnprof_DataStore_capacity, bpmnprof_DataStore_isUnlimited}

# bpmnprof_DataObjectReference class attributes and methods
bpmnprof_DataObjectReference_m_DataObjectRefsourcetarget: Method = Method(name="DataObjectRefsourcetarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataObjectReference_m_DataObjectRefdataState: Method = Method(name="DataObjectRefdataState", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_DataObjectReference.methods={bpmnprof_DataObjectReference_m_DataObjectRefdataState, bpmnprof_DataObjectReference_m_DataObjectRefsourcetarget}

# bpmnprof_DataObject class attributes and methods
bpmnprof_DataObject_isCollection: Property = Property(name="isCollection", type=StringType)
bpmnprof_DataObject_m_DataObjectdataState: Method = Method(name="DataObjectdataState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_DataObject.attributes={bpmnprof_DataObject_isCollection}
bpmnprof_DataObject.methods={bpmnprof_DataObject_m_DataObjectdataState}

# bpmnprof_Rendering class attributes and methods

# bpmnprof_Task class attributes and methods

# BPMNActivity class attributes and methods

# bpmnprof_DataStoreReference class attributes and methods

# bpmnprof_UserTask class attributes and methods
bpmnprof_UserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_UserTask_m_UserTaskimplementation: Method = Method(name="UserTaskimplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_UserTask_m_UserTaskrenderings: Method = Method(name="UserTaskrenderings", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_UserTask.attributes={bpmnprof_UserTask_implementation}
bpmnprof_UserTask.methods={bpmnprof_UserTask_m_UserTaskrenderings, bpmnprof_UserTask_m_UserTaskimplementation}

# Task class attributes and methods

# bpmnprof_OpaqueAction class attributes and methods

# bpmnprof_PotentialOwner class attributes and methods

# HumanPerformer class attributes and methods

# bpmnprof_SubConversation class attributes and methods
bpmnprof_SubConversation_m_SubConversationconnectedelements: Method = Method(name="SubConversationconnectedelements", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_SubConversation.methods={bpmnprof_SubConversation_m_SubConversationconnectedelements}

# ConversationNode class attributes and methods

# bpmnprof_Image class attributes and methods

# bpmnprof_HumanPerformer class attributes and methods

# Performer class attributes and methods

# bpmnprof_Performer class attributes and methods

# ResourceRole class attributes and methods

# bpmnprof_GlobalUserTask class attributes and methods
bpmnprof_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_GlobalUserTask_m_GlobalUserTaskrenderings: Method = Method(name="GlobalUserTaskrenderings", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_GlobalUserTask_m_GlobalUserTaskimplementation: Method = Method(name="GlobalUserTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_GlobalUserTask.attributes={bpmnprof_GlobalUserTask_implementation}
bpmnprof_GlobalUserTask.methods={bpmnprof_GlobalUserTask_m_GlobalUserTaskrenderings, bpmnprof_GlobalUserTask_m_GlobalUserTaskimplementation}

# bpmnprof_GlobalManualTask class attributes and methods

# bpmnprof_ManualTask class attributes and methods

# bpmnprof_GlobalConversation class attributes and methods
bpmnprof_GlobalConversation_m_GlobalConversationcontainedelements: Method = Method(name="GlobalConversationcontainedelements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_GlobalConversation.methods={bpmnprof_GlobalConversation_m_GlobalConversationcontainedelements}

# BPMNCollaboration class attributes and methods

# bpmnprof_CallConversation class attributes and methods
bpmnprof_CallConversation_m_CallConversationcalledCollaborationRef: Method = Method(name="CallConversationcalledCollaborationRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_CallConversation_m_CallConversationparticipantAssociations: Method = Method(name="CallConversationparticipantAssociations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_CallConversation.methods={bpmnprof_CallConversation_m_CallConversationparticipantAssociations, bpmnprof_CallConversation_m_CallConversationcalledCollaborationRef}

# bpmnprof_CollaborationUse class attributes and methods

# bpmnprof_Conversation class attributes and methods

# bpmnprof_SubProcess class attributes and methods
bpmnprof_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=StringType)
bpmnprof_SubProcess_m_SubProcesstriggeredByEvent: Method = Method(name="SubProcesstriggeredByEvent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_SubProcess.attributes={bpmnprof_SubProcess_triggeredByEvent}
bpmnprof_SubProcess.methods={bpmnprof_SubProcess_m_SubProcesstriggeredByEvent}

# bpmnprof_ComplexBehaviorDefinition class attributes and methods

# bpmnprof_CallActivity class attributes and methods
bpmnprof_CallActivity_m_CallActivitycalledElementRefvalues: Method = Method(name="CallActivitycalledElementRefvalues", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_CallActivity.methods={bpmnprof_CallActivity_m_CallActivitycalledElementRefvalues}

# bpmnprof_CallBehaviorAction class attributes and methods

# bpmnprof_BusinessRuleTask class attributes and methods
bpmnprof_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_BusinessRuleTask_m_BusinessRuleTaskimplementation: Method = Method(name="BusinessRuleTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_BusinessRuleTask.attributes={bpmnprof_BusinessRuleTask_implementation}
bpmnprof_BusinessRuleTask.methods={bpmnprof_BusinessRuleTask_m_BusinessRuleTaskimplementation}

# bpmnprof_Transaction class attributes and methods
bpmnprof_Transaction_method: Property = Property(name="method", type=StringType)
bpmnprof_Transaction.attributes={bpmnprof_Transaction_method}

# bpmnprof_AdHocSubProcess class attributes and methods
bpmnprof_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
bpmnprof_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=StringType)
bpmnprof_AdHocSubProcess_m_AdHocSubProcesscancelRemainingInstances: Method = Method(name="AdHocSubProcesscancelRemainingInstances", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_AdHocSubProcess.attributes={bpmnprof_AdHocSubProcess_ordering, bpmnprof_AdHocSubProcess_cancelRemainingInstances}
bpmnprof_AdHocSubProcess.methods={bpmnprof_AdHocSubProcess_m_AdHocSubProcesscancelRemainingInstances}

# SubProcess class attributes and methods

# bpmnprof_ScriptTask class attributes and methods
bpmnprof_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
bpmnprof_ScriptTask_script: Property = Property(name="script", type=StringType)
bpmnprof_ScriptTask_m_ScriptTaskscriptFormat: Method = Method(name="ScriptTaskscriptFormat", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ScriptTask_m_ScriptTaskscript: Method = Method(name="ScriptTaskscript", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ScriptTask.attributes={bpmnprof_ScriptTask_scriptFormat, bpmnprof_ScriptTask_script}
bpmnprof_ScriptTask.methods={bpmnprof_ScriptTask_m_ScriptTaskscript, bpmnprof_ScriptTask_m_ScriptTaskscriptFormat}

# bpmnprof_SendTask class attributes and methods
bpmnprof_SendTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_SendTask_m_SendTaskoperationRef: Method = Method(name="SendTaskoperationRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_SendTask.attributes={bpmnprof_SendTask_implementation}
bpmnprof_SendTask.methods={bpmnprof_SendTask_m_SendTaskoperationRef}

# bpmnprof_ServiceTask class attributes and methods
bpmnprof_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_ServiceTask_m_ServiceTaskinputSet: Method = Method(name="ServiceTaskinputSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ServiceTask_m_ServiceTaskoutputSet: Method = Method(name="ServiceTaskoutputSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ServiceTask_m_ServiceTaskoperationRef: Method = Method(name="ServiceTaskoperationRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_ServiceTask.attributes={bpmnprof_ServiceTask_implementation}
bpmnprof_ServiceTask.methods={bpmnprof_ServiceTask_m_ServiceTaskinputSet, bpmnprof_ServiceTask_m_ServiceTaskoperationRef, bpmnprof_ServiceTask_m_ServiceTaskoutputSet}

# bpmnprof_StandardLoopCharacteristics class attributes and methods
bpmnprof_StandardLoopCharacteristics_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
bpmnprof_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=StringType)
bpmnprof_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore: Method = Method(name="StandardLoopCharacteristicstestBefore", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition: Method = Method(name="StandardLoopCharacteristicsloopCondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
bpmnprof_StandardLoopCharacteristics.attributes={bpmnprof_StandardLoopCharacteristics_loopMaximum, bpmnprof_StandardLoopCharacteristics_testBefore}
bpmnprof_StandardLoopCharacteristics.methods={bpmnprof_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore, bpmnprof_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition}

# LoopCharacteristics class attributes and methods

# bpmnprof_LoopNode class attributes and methods

# bpmnprof_ReceiveTask class attributes and methods
bpmnprof_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
bpmnprof_ReceiveTask_instantiate: Property = Property(name="instantiate", type=StringType)
bpmnprof_ReceiveTask_m_ReceiveTaskoperationRef: Method = Method(name="ReceiveTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_ReceiveTask.attributes={bpmnprof_ReceiveTask_instantiate, bpmnprof_ReceiveTask_implementation}
bpmnprof_ReceiveTask.methods={bpmnprof_ReceiveTask_m_ReceiveTaskoperationRef}

# bpmnprof_ExpansionRegion class attributes and methods

# bpmnprof_MultiInstanceLoopCharacteristics class attributes and methods
bpmnprof_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=StringType)
bpmnprof_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
bpmnprof_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget: Method = Method(name="MultiinstanceLoopCharacteristicstarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
bpmnprof_MultiInstanceLoopCharacteristics.attributes={bpmnprof_MultiInstanceLoopCharacteristics_behavior, bpmnprof_MultiInstanceLoopCharacteristics_isSequential}
bpmnprof_MultiInstanceLoopCharacteristics.methods={bpmnprof_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget}

# Relationships
base_ActivityNode7: BinaryAssociation = BinaryAssociation(
    name="base_ActivityNode7",
    ends={
        Property(name="bpmnprof_ActivityNode", type=bpmnprof_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_FlowNode", type=bpmnprof_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
auditing8: BinaryAssociation = BinaryAssociation(
    name="auditing8",
    ends={
        Property(name="bpmnprof_Auditing", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_FlowElement", type=bpmnprof_Auditing, multiplicity=Multiplicity(0, 1))
    }
)
monitoring9: BinaryAssociation = BinaryAssociation(
    name="monitoring9",
    ends={
        Property(name="bpmnprof_Monitoring", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_FlowElement10", type=bpmnprof_Monitoring, multiplicity=Multiplicity(0, 1))
    }
)
_categoryValueRef11: BinaryAssociation = BinaryAssociation(
    name="_categoryValueRef11",
    ends={
        Property(name="CategoryValue", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="categorizedFlowElements", type=bpmnprof_CategoryValue, multiplicity=Multiplicity(1, 9999))
    }
)
container12: BinaryAssociation = BinaryAssociation(
    name="container12",
    ends={
        Property(name="FlowElementsContainer", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="flowElements", type=bpmnprof_FlowElementsContainer, multiplicity=Multiplicity(1, 1))
    }
)
default0: BinaryAssociation = BinaryAssociation(
    name="default0",
    ends={
        Property(name="bpmnprof_SequenceFlow", type=bpmnprof_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InclusiveGateway", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
base_JoinNode1: BinaryAssociation = BinaryAssociation(
    name="base_JoinNode1",
    ends={
        Property(name="bpmnprof_JoinNode", type=bpmnprof_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_NonExclusiveGateway", type=bpmnprof_JoinNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ForkNode2: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode2",
    ends={
        Property(name="bpmnprof_ForkNode", type=bpmnprof_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_NonExclusiveGateway3", type=bpmnprof_ForkNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ControlNode4: BinaryAssociation = BinaryAssociation(
    name="base_ControlNode4",
    ends={
        Property(name="bpmnprof_ControlNode", type=bpmnprof_Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Gateway", type=bpmnprof_ControlNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityGroup5: BinaryAssociation = BinaryAssociation(
    name="base_ActivityGroup5",
    ends={
        Property(name="bpmnprof_ActivityGroup", type=bpmnprof_Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Gateway6", type=bpmnprof_ActivityGroup, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment32: BinaryAssociation = BinaryAssociation(
    name="base_Comment32",
    ends={
        Property(name="bpmnprof_Comment", type=bpmnprof_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Documentation33", type=bpmnprof_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_Stereotype34: BinaryAssociation = BinaryAssociation(
    name="base_Stereotype34",
    ends={
        Property(name="bpmnprof_Stereotype", type=bpmnprof_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionDefinition35", type=bpmnprof_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
extensionAttributeDefinitions36: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions36",
    ends={
        Property(name="bpmnprof_ExtensionAttributeDefinition38", type=bpmnprof_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionDefinition37", type=bpmnprof_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
extensionValues13: BinaryAssociation = BinaryAssociation(
    name="extensionValues13",
    ends={
        Property(name="bpmnprof_ExtensionAttributeValue", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BaseElement", type=bpmnprof_ExtensionAttributeValue, multiplicity=Multiplicity(1, 9999))
    }
)
base_Element14: BinaryAssociation = BinaryAssociation(
    name="base_Element14",
    ends={
        Property(name="bpmnprof_Element", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BaseElement15", type=bpmnprof_Element, multiplicity=Multiplicity(1, 1))
    }
)
documentation16: BinaryAssociation = BinaryAssociation(
    name="documentation16",
    ends={
        Property(name="bpmnprof_Documentation", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BaseElement17", type=bpmnprof_Documentation, multiplicity=Multiplicity(1, 9999))
    }
)
extensionDefinitions18: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions18",
    ends={
        Property(name="bpmnprof_ExtensionDefinition", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BaseElement19", type=bpmnprof_ExtensionDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing20: BinaryAssociation = BinaryAssociation(
    name="outgoing20",
    ends={
        Property(name="BPMNAssociation", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=bpmnprof_BPMNAssociation, multiplicity=Multiplicity(1, 1))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="BPMNAssociation22", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=bpmnprof_BPMNAssociation, multiplicity=Multiplicity(1, 1))
    }
)
base_Slot23: BinaryAssociation = BinaryAssociation(
    name="base_Slot23",
    ends={
        Property(name="bpmnprof_Slot", type=bpmnprof_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionAttributeValue24", type=bpmnprof_Slot, multiplicity=Multiplicity(1, 1))
    }
)
valueRef25: BinaryAssociation = BinaryAssociation(
    name="valueRef25",
    ends={
        Property(name="bpmnprof_Element27", type=bpmnprof_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionAttributeValue26", type=bpmnprof_Element, multiplicity=Multiplicity(0, 1))
    }
)
extensionAttributeDefinition28: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition28",
    ends={
        Property(name="bpmnprof_ExtensionAttributeDefinition", type=bpmnprof_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionAttributeValue29", type=bpmnprof_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_Property30: BinaryAssociation = BinaryAssociation(
    name="base_Property30",
    ends={
        Property(name="bpmnprof_Property", type=bpmnprof_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExtensionAttributeDefinition31", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_EnumerationLiteral48: BinaryAssociation = BinaryAssociation(
    name="base_EnumerationLiteral48",
    ends={
        Property(name="bpmnprof_EnumerationLiteral", type=bpmnprof_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CategoryValue", type=bpmnprof_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
categorizedFlowElements49: BinaryAssociation = BinaryAssociation(
    name="categorizedFlowElements49",
    ends={
        Property(name="FlowElement", type=bpmnprof_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="_categoryValueRef", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 9999))
    }
)
laneSets50: BinaryAssociation = BinaryAssociation(
    name="laneSets50",
    ends={
        Property(name="LaneSet", type=bpmnprof_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="flowElementsContainer", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 9999))
    }
)
flowElements51: BinaryAssociation = BinaryAssociation(
    name="flowElements51",
    ends={
        Property(name="FlowElement52", type=bpmnprof_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=bpmnprof_FlowElement, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency39: BinaryAssociation = BinaryAssociation(
    name="base_Dependency39",
    ends={
        Property(name="bpmnprof_Dependency", type=bpmnprof_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNAssociation", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
targetRef40: BinaryAssociation = BinaryAssociation(
    name="targetRef40",
    ends={
        Property(name="BaseElement", type=bpmnprof_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef41: BinaryAssociation = BinaryAssociation(
    name="sourceRef41",
    ends={
        Property(name="BaseElement42", type=bpmnprof_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=bpmnprof_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="bpmnprof_Class", type=bpmnprof_Auditing, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Auditing44", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="bpmnprof_Class47", type=bpmnprof_Monitoring, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Monitoring46", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
flowElementsContainer57: BinaryAssociation = BinaryAssociation(
    name="flowElementsContainer57",
    ends={
        Property(name="FlowElementsContainer58", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="laneSets", type=bpmnprof_FlowElementsContainer, multiplicity=Multiplicity(0, 1))
    }
)
base_ActivityPartition53: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition53",
    ends={
        Property(name="bpmnprof_ActivityPartition", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_LaneSet", type=bpmnprof_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
lanes54: BinaryAssociation = BinaryAssociation(
    name="lanes54",
    ends={
        Property(name="Lane", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="laneSet", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 9999))
    }
)
parentLane55: BinaryAssociation = BinaryAssociation(
    name="parentLane55",
    ends={
        Property(name="bpmnprof_Lane", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_LaneSet56", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 9999))
    }
)
base_ControlFlow76: BinaryAssociation = BinaryAssociation(
    name="base_ControlFlow76",
    ends={
        Property(name="bpmnprof_ControlFlow", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SequenceFlow77", type=bpmnprof_ControlFlow, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityPartition59: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition59",
    ends={
        Property(name="bpmnprof_ActivityPartition61", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Lane60", type=bpmnprof_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
_partitionElement62: BinaryAssociation = BinaryAssociation(
    name="_partitionElement62",
    ends={
        Property(name="bpmnprof_Element64", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Lane63", type=bpmnprof_Element, multiplicity=Multiplicity(0, 1))
    }
)
flowNodeRefs65: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs65",
    ends={
        Property(name="bpmnprof_FlowNode67", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Lane66", type=bpmnprof_FlowNode, multiplicity=Multiplicity(1, 9999))
    }
)
partitionElementRef68: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef68",
    ends={
        Property(name="bpmnprof_BaseElement70", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Lane69", type=bpmnprof_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
childLaneSet71: BinaryAssociation = BinaryAssociation(
    name="childLaneSet71",
    ends={
        Property(name="bpmnprof_LaneSet73", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Lane72", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1))
    }
)
laneSet74: BinaryAssociation = BinaryAssociation(
    name="laneSet74",
    ends={
        Property(name="LaneSet75", type=bpmnprof_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression78: BinaryAssociation = BinaryAssociation(
    name="conditionExpression78",
    ends={
        Property(name="bpmnprof_BPMNExpression", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SequenceFlow79", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueExpression80: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueExpression80",
    ends={
        Property(name="bpmnprof_OpaqueExpression", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNExpression81", type=bpmnprof_OpaqueExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_ForkNode82: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode82",
    ends={
        Property(name="bpmnprof_ForkNode83", type=bpmnprof_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EventBasedGateway", type=bpmnprof_ForkNode, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode84: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode84",
    ends={
        Property(name="bpmnprof_StructuredActivityNode", type=bpmnprof_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EventBasedGateway85", type=bpmnprof_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
base_InterruptibleActivityRegion86: BinaryAssociation = BinaryAssociation(
    name="base_InterruptibleActivityRegion86",
    ends={
        Property(name="bpmnprof_InterruptibleActivityRegion", type=bpmnprof_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EventBasedGateway87", type=bpmnprof_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1))
    }
)
base_Package101: BinaryAssociation = BinaryAssociation(
    name="base_Package101",
    ends={
        Property(name="bpmnprof_Package", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Definitions", type=bpmnprof_Package, multiplicity=Multiplicity(1, 1))
    }
)
extensions102: BinaryAssociation = BinaryAssociation(
    name="extensions102",
    ends={
        Property(name="bpmnprof_BPMNExtension", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Definitions103", type=bpmnprof_BPMNExtension, multiplicity=Multiplicity(1, 9999))
    }
)
imports104: BinaryAssociation = BinaryAssociation(
    name="imports104",
    ends={
        Property(name="bpmnprof_Import", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Definitions105", type=bpmnprof_Import, multiplicity=Multiplicity(1, 9999))
    }
)
relationships106: BinaryAssociation = BinaryAssociation(
    name="relationships106",
    ends={
        Property(name="bpmnprof_BPMNRelationship", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Definitions107", type=bpmnprof_BPMNRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
default88: BinaryAssociation = BinaryAssociation(
    name="default88",
    ends={
        Property(name="bpmnprof_SequenceFlow89", type=bpmnprof_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ComplexGateway", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
activationCondition90: BinaryAssociation = BinaryAssociation(
    name="activationCondition90",
    ends={
        Property(name="bpmnprof_BPMNExpression92", type=bpmnprof_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ComplexGateway91", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_DecisionNode93: BinaryAssociation = BinaryAssociation(
    name="base_DecisionNode93",
    ends={
        Property(name="bpmnprof_DecisionNode", type=bpmnprof_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExclusiveGateway", type=bpmnprof_DecisionNode, multiplicity=Multiplicity(1, 1))
    }
)
base_MergeNode94: BinaryAssociation = BinaryAssociation(
    name="base_MergeNode94",
    ends={
        Property(name="bpmnprof_MergeNode", type=bpmnprof_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExclusiveGateway95", type=bpmnprof_MergeNode, multiplicity=Multiplicity(1, 1))
    }
)
default96: BinaryAssociation = BinaryAssociation(
    name="default96",
    ends={
        Property(name="bpmnprof_SequenceFlow98", type=bpmnprof_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ExclusiveGateway97", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
base_PackageableElement99: BinaryAssociation = BinaryAssociation(
    name="base_PackageableElement99",
    ends={
        Property(name="bpmnprof_PackageableElement", type=bpmnprof_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_RootElement", type=bpmnprof_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
definition100: BinaryAssociation = BinaryAssociation(
    name="definition100",
    ends={
        Property(name="Definitions", type=bpmnprof_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rootElements", type=bpmnprof_Definitions, multiplicity=Multiplicity(0, 1))
    }
)
targets122: BinaryAssociation = BinaryAssociation(
    name="targets122",
    ends={
        Property(name="bpmnprof_Element124", type=bpmnprof_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNRelationship123", type=bpmnprof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
sources125: BinaryAssociation = BinaryAssociation(
    name="sources125",
    ends={
        Property(name="bpmnprof_Element127", type=bpmnprof_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNRelationship126", type=bpmnprof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
definition128: BinaryAssociation = BinaryAssociation(
    name="definition128",
    ends={
        Property(name="bpmnprof_Definitions130", type=bpmnprof_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNRelationship129", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
rootElements108: BinaryAssociation = BinaryAssociation(
    name="rootElements108",
    ends={
        Property(name="RootElement", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=bpmnprof_RootElement, multiplicity=Multiplicity(1, 9999))
    }
)
base_Stereotype109: BinaryAssociation = BinaryAssociation(
    name="base_Stereotype109",
    ends={
        Property(name="bpmnprof_Stereotype111", type=bpmnprof_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNExtension110", type=bpmnprof_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
definition112: BinaryAssociation = BinaryAssociation(
    name="definition112",
    ends={
        Property(name="bpmnprof_ExtensionDefinition114", type=bpmnprof_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNExtension113", type=bpmnprof_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_PackageImport115: BinaryAssociation = BinaryAssociation(
    name="base_PackageImport115",
    ends={
        Property(name="bpmnprof_PackageImport", type=bpmnprof_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Import116", type=bpmnprof_PackageImport, multiplicity=Multiplicity(1, 1))
    }
)
definitions117: BinaryAssociation = BinaryAssociation(
    name="definitions117",
    ends={
        Property(name="bpmnprof_Definitions119", type=bpmnprof_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Import118", type=bpmnprof_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
base_Constraint120: BinaryAssociation = BinaryAssociation(
    name="base_Constraint120",
    ends={
        Property(name="bpmnprof_Constraint", type=bpmnprof_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNRelationship121", type=bpmnprof_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
definitionalCollaborationRef133: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef133",
    ends={
        Property(name="bpmnprof_BPMNCollaboration", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess134", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
base_Activity135: BinaryAssociation = BinaryAssociation(
    name="base_Activity135",
    ends={
        Property(name="bpmnprof_Activity", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess136", type=bpmnprof_Activity, multiplicity=Multiplicity(1, 1))
    }
)
correlationSubscriptions137: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions137",
    ends={
        Property(name="bpmnprof_CorrelationSubscription", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess138", type=bpmnprof_CorrelationSubscription, multiplicity=Multiplicity(1, 9999))
    }
)
monitoring139: BinaryAssociation = BinaryAssociation(
    name="monitoring139",
    ends={
        Property(name="bpmnprof_Monitoring141", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess140", type=bpmnprof_Monitoring, multiplicity=Multiplicity(0, 1))
    }
)
supports143: BinaryAssociation = BinaryAssociation(
    name="supports143",
    ends={
        Property(name="bpmnprof_BPMNProcess144", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess142", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1))
    }
)
properties145: BinaryAssociation = BinaryAssociation(
    name="properties145",
    ends={
        Property(name="bpmnprof_BPMNProperty", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess146", type=bpmnprof_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
auditing131: BinaryAssociation = BinaryAssociation(
    name="auditing131",
    ends={
        Property(name="bpmnprof_Auditing132", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProcess", type=bpmnprof_Auditing, multiplicity=Multiplicity(0, 1))
    }
)
base_Behavior155: BinaryAssociation = BinaryAssociation(
    name="base_Behavior155",
    ends={
        Property(name="bpmnprof_Behavior157", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification156", type=bpmnprof_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Action158: BinaryAssociation = BinaryAssociation(
    name="base_Action158",
    ends={
        Property(name="bpmnprof_Action", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification159", type=bpmnprof_Action, multiplicity=Multiplicity(1, 1))
    }
)
dataInputs160: BinaryAssociation = BinaryAssociation(
    name="dataInputs160",
    ends={
        Property(name="bpmnprof_DataInput", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification161", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputs162: BinaryAssociation = BinaryAssociation(
    name="dataOutputs162",
    ends={
        Property(name="bpmnprof_DataOutput", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification163", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
inputSets164: BinaryAssociation = BinaryAssociation(
    name="inputSets164",
    ends={
        Property(name="bpmnprof_InputSet", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification165", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSets166: BinaryAssociation = BinaryAssociation(
    name="outputSets166",
    ends={
        Property(name="bpmnprof_OutputSet", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputSpecification167", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
resources147: BinaryAssociation = BinaryAssociation(
    name="resources147",
    ends={
        Property(name="ResourceRole", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
base_Behavior148: BinaryAssociation = BinaryAssociation(
    name="base_Behavior148",
    ends={
        Property(name="bpmnprof_Behavior", type=bpmnprof_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallableElement", type=bpmnprof_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
ioSpecification149: BinaryAssociation = BinaryAssociation(
    name="ioSpecification149",
    ends={
        Property(name="bpmnprof_InputOutputSpecification", type=bpmnprof_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallableElement150", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
supportedInterfaceRefs151: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs151",
    ends={
        Property(name="bpmnprof_BPMNInterface", type=bpmnprof_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallableElement152", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 9999))
    }
)
ioBinding153: BinaryAssociation = BinaryAssociation(
    name="ioBinding153",
    ends={
        Property(name="bpmnprof_InputOutputBinding", type=bpmnprof_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallableElement154", type=bpmnprof_InputOutputBinding, multiplicity=Multiplicity(1, 9999))
    }
)
base_Parameter170: BinaryAssociation = BinaryAssociation(
    name="base_Parameter170",
    ends={
        Property(name="bpmnprof_Parameter", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataInput171", type=bpmnprof_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityParameterNode172: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode172",
    ends={
        Property(name="bpmnprof_ActivityParameterNode", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataInput173", type=bpmnprof_ActivityParameterNode, multiplicity=Multiplicity(1, 1))
    }
)
inputSetRefs174: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs174",
    ends={
        Property(name="InputSet", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
inputSetWithOptional175: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional175",
    ends={
        Property(name="InputSet176", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
inputSetWithWhileExecuting177: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting177",
    ends={
        Property(name="InputSet178", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_InputPin168: BinaryAssociation = BinaryAssociation(
    name="base_InputPin168",
    ends={
        Property(name="bpmnprof_InputPin", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataInput169", type=bpmnprof_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
base_Class186: BinaryAssociation = BinaryAssociation(
    name="base_Class186",
    ends={
        Property(name="bpmnprof_Class188", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemDefinition187", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
structureRef189: BinaryAssociation = BinaryAssociation(
    name="structureRef189",
    ends={
        Property(name="bpmnprof_Element191", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemDefinition190", type=bpmnprof_Element, multiplicity=Multiplicity(0, 1))
    }
)
import192: BinaryAssociation = BinaryAssociation(
    name="import192",
    ends={
        Property(name="bpmnprof_Import194", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemDefinition193", type=bpmnprof_Import, multiplicity=Multiplicity(0, 1))
    }
)
dataState179: BinaryAssociation = BinaryAssociation(
    name="dataState179",
    ends={
        Property(name="bpmnprof_DataState", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemAwareElement", type=bpmnprof_DataState, multiplicity=Multiplicity(1, 9999))
    }
)
base_TypedElement180: BinaryAssociation = BinaryAssociation(
    name="base_TypedElement180",
    ends={
        Property(name="bpmnprof_TypedElement", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemAwareElement181", type=bpmnprof_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef182: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef182",
    ends={
        Property(name="bpmnprof_ItemDefinition", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ItemAwareElement183", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_State184: BinaryAssociation = BinaryAssociation(
    name="base_State184",
    ends={
        Property(name="bpmnprof_State", type=bpmnprof_DataState, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataState185", type=bpmnprof_State, multiplicity=Multiplicity(1, 1))
    }
)
base_OutputPin202: BinaryAssociation = BinaryAssociation(
    name="base_OutputPin202",
    ends={
        Property(name="bpmnprof_OutputPin", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataOutput203", type=bpmnprof_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
base_Parameter204: BinaryAssociation = BinaryAssociation(
    name="base_Parameter204",
    ends={
        Property(name="bpmnprof_Parameter206", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataOutput205", type=bpmnprof_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityParameterNode207: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode207",
    ends={
        Property(name="bpmnprof_ActivityParameterNode209", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataOutput208", type=bpmnprof_ActivityParameterNode, multiplicity=Multiplicity(1, 1))
    }
)
outputSetRefs210: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs210",
    ends={
        Property(name="OutputSet", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_ParameterSet195: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet195",
    ends={
        Property(name="bpmnprof_ParameterSet", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputSet196", type=bpmnprof_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
optionalInputRefs197: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs197",
    ends={
        Property(name="DataInput", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
whileExecutingInputRefs198: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs198",
    ends={
        Property(name="DataInput199", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
dataInputRefs200: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs200",
    ends={
        Property(name="DataInput201", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
base_ParameterSet217: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet217",
    ends={
        Property(name="bpmnprof_ParameterSet219", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_OutputSet218", type=bpmnprof_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
optionalOutputRefs220: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs220",
    ends={
        Property(name="bpmnprof_DataOutput222", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_OutputSet221", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
whileExecutingOutputRefs223: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs223",
    ends={
        Property(name="bpmnprof_DataOutput225", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_OutputSet224", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputRefs226: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs226",
    ends={
        Property(name="DataOutput", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
outputSetWithOptional211: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional211",
    ends={
        Property(name="bpmnprof_OutputSet213", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataOutput212", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSetWithWhileExecuting214: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting214",
    ends={
        Property(name="bpmnprof_OutputSet216", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataOutput215", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_Interface227: BinaryAssociation = BinaryAssociation(
    name="base_Interface227",
    ends={
        Property(name="bpmnprof_Interface", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNInterface228", type=bpmnprof_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef229: BinaryAssociation = BinaryAssociation(
    name="implementationRef229",
    ends={
        Property(name="bpmnprof_Element231", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNInterface230", type=bpmnprof_Element, multiplicity=Multiplicity(0, 1))
    }
)
operations232: BinaryAssociation = BinaryAssociation(
    name="operations232",
    ends={
        Property(name="bpmnprof_BPMNOperation", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNInterface233", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 9999))
    }
)
callableElements234: BinaryAssociation = BinaryAssociation(
    name="callableElements234",
    ends={
        Property(name="bpmnprof_CallableElement236", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNInterface235", type=bpmnprof_CallableElement, multiplicity=Multiplicity(1, 9999))
    }
)
inMessageRef242: BinaryAssociation = BinaryAssociation(
    name="inMessageRef242",
    ends={
        Property(name="bpmnprof_BPMNMessage", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNOperation243", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef244: BinaryAssociation = BinaryAssociation(
    name="outMessageRef244",
    ends={
        Property(name="bpmnprof_BPMNMessage246", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNOperation245", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
errorRef247: BinaryAssociation = BinaryAssociation(
    name="errorRef247",
    ends={
        Property(name="bpmnprof_Error", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNOperation248", type=bpmnprof_Error, multiplicity=Multiplicity(1, 9999))
    }
)
itemRef249: BinaryAssociation = BinaryAssociation(
    name="itemRef249",
    ends={
        Property(name="bpmnprof_ItemDefinition251", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNMessage250", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef252: BinaryAssociation = BinaryAssociation(
    name="inputDataRef252",
    ends={
        Property(name="bpmnprof_InputSet254", type=bpmnprof_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputBinding253", type=bpmnprof_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
base_Operation237: BinaryAssociation = BinaryAssociation(
    name="base_Operation237",
    ends={
        Property(name="bpmnprof_Operation", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNOperation238", type=bpmnprof_Operation, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef239: BinaryAssociation = BinaryAssociation(
    name="implementationRef239",
    ends={
        Property(name="bpmnprof_Element241", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNOperation240", type=bpmnprof_Element, multiplicity=Multiplicity(0, 1))
    }
)
conversationLinks266: BinaryAssociation = BinaryAssociation(
    name="conversationLinks266",
    ends={
        Property(name="ConversationLink", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 9999))
    }
)
messageFlowAssociations267: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations267",
    ends={
        Property(name="bpmnprof_MessageFlowAssociation", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration268", type=bpmnprof_MessageFlowAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
outputDataRef255: BinaryAssociation = BinaryAssociation(
    name="outputDataRef255",
    ends={
        Property(name="bpmnprof_OutputSet257", type=bpmnprof_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputBinding256", type=bpmnprof_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef258: BinaryAssociation = BinaryAssociation(
    name="operationRef258",
    ends={
        Property(name="bpmnprof_BPMNOperation260", type=bpmnprof_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputBinding259", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency261: BinaryAssociation = BinaryAssociation(
    name="base_Dependency261",
    ends={
        Property(name="bpmnprof_Dependency263", type=bpmnprof_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InputOutputBinding262", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
participantAssociations264: BinaryAssociation = BinaryAssociation(
    name="participantAssociations264",
    ends={
        Property(name="bpmnprof_ParticipantAssociation", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration265", type=bpmnprof_ParticipantAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency279: BinaryAssociation = BinaryAssociation(
    name="base_Dependency279",
    ends={
        Property(name="bpmnprof_Dependency281", type=bpmnprof_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ParticipantAssociation280", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
innerParticipantRef282: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef282",
    ends={
        Property(name="bpmnprof_Participant284", type=bpmnprof_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ParticipantAssociation283", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef285: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef285",
    ends={
        Property(name="bpmnprof_Participant287", type=bpmnprof_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ParticipantAssociation286", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1))
    }
)
messageFlows269: BinaryAssociation = BinaryAssociation(
    name="messageFlows269",
    ends={
        Property(name="bpmnprof_MessageFlow", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration270", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 9999))
    }
)
base_Collaboration271: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration271",
    ends={
        Property(name="bpmnprof_Collaboration", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration272", type=bpmnprof_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
conversations273: BinaryAssociation = BinaryAssociation(
    name="conversations273",
    ends={
        Property(name="bpmnprof_ConversationNode", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration274", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 9999))
    }
)
correlationKeys275: BinaryAssociation = BinaryAssociation(
    name="correlationKeys275",
    ends={
        Property(name="bpmnprof_CorrelationKey", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration276", type=bpmnprof_CorrelationKey, multiplicity=Multiplicity(1, 9999))
    }
)
participants277: BinaryAssociation = BinaryAssociation(
    name="participants277",
    ends={
        Property(name="bpmnprof_Participant", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNCollaboration278", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
base_Property288: BinaryAssociation = BinaryAssociation(
    name="base_Property288",
    ends={
        Property(name="bpmnprof_Property290", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Participant289", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConversationLinks304: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks304",
    ends={
        Property(name="ConversationLink306", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef305", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 9999))
    }
)
incomingConversationLinks307: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks307",
    ends={
        Property(name="ConversationLink309", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef308", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 1))
    }
)
collaboration310: BinaryAssociation = BinaryAssociation(
    name="collaboration310",
    ends={
        Property(name="BPMNCollaboration", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="conversationLinks", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency311: BinaryAssociation = BinaryAssociation(
    name="base_Dependency311",
    ends={
        Property(name="bpmnprof_Dependency312", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConversationLink", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
targetRef313: BinaryAssociation = BinaryAssociation(
    name="targetRef313",
    ends={
        Property(name="InteractionNode", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConversationLinks", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef314: BinaryAssociation = BinaryAssociation(
    name="sourceRef314",
    ends={
        Property(name="InteractionNode315", type=bpmnprof_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConversationLinks", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
base_MultiplicityElement316: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement316",
    ends={
        Property(name="bpmnprof_MultiplicityElement", type=bpmnprof_ParticipantMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ParticipantMultiplicity317", type=bpmnprof_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
processRef291: BinaryAssociation = BinaryAssociation(
    name="processRef291",
    ends={
        Property(name="bpmnprof_BPMNProcess293", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Participant292", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
participantMultiplicity294: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity294",
    ends={
        Property(name="bpmnprof_ParticipantMultiplicity", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Participant295", type=bpmnprof_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1))
    }
)
partnerEntityRef296: BinaryAssociation = BinaryAssociation(
    name="partnerEntityRef296",
    ends={
        Property(name="PartnerEntity", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef", type=bpmnprof_PartnerEntity, multiplicity=Multiplicity(1, 9999))
    }
)
partnerRoleRef297: BinaryAssociation = BinaryAssociation(
    name="partnerRoleRef297",
    ends={
        Property(name="PartnerRole", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef298", type=bpmnprof_PartnerRole, multiplicity=Multiplicity(1, 9999))
    }
)
interfaceRefs299: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs299",
    ends={
        Property(name="bpmnprof_BPMNInterface301", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Participant300", type=bpmnprof_BPMNInterface, multiplicity=Multiplicity(1, 9999))
    }
)
base_Element302: BinaryAssociation = BinaryAssociation(
    name="base_Element302",
    ends={
        Property(name="bpmnprof_Element303", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_InteractionNode", type=bpmnprof_Element, multiplicity=Multiplicity(1, 1))
    }
)
base_Class320: BinaryAssociation = BinaryAssociation(
    name="base_Class320",
    ends={
        Property(name="bpmnprof_Class321", type=bpmnprof_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_PartnerRole", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
participantRef322: BinaryAssociation = BinaryAssociation(
    name="participantRef322",
    ends={
        Property(name="Participant323", type=bpmnprof_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerRoleRef", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency324: BinaryAssociation = BinaryAssociation(
    name="base_Dependency324",
    ends={
        Property(name="bpmnprof_Dependency326", type=bpmnprof_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlowAssociation325", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
base_InstanceSpecification318: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification318",
    ends={
        Property(name="bpmnprof_InstanceSpecification", type=bpmnprof_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_PartnerEntity", type=bpmnprof_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
participantRef319: BinaryAssociation = BinaryAssociation(
    name="participantRef319",
    ends={
        Property(name="Participant", type=bpmnprof_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerEntityRef", type=bpmnprof_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
base_InformationFlow333: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow333",
    ends={
        Property(name="bpmnprof_InformationFlow", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlow334", type=bpmnprof_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef335: BinaryAssociation = BinaryAssociation(
    name="sourceRef335",
    ends={
        Property(name="bpmnprof_InteractionNode337", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlow336", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef338: BinaryAssociation = BinaryAssociation(
    name="targetRef338",
    ends={
        Property(name="bpmnprof_InteractionNode340", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlow339", type=bpmnprof_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
messageRef341: BinaryAssociation = BinaryAssociation(
    name="messageRef341",
    ends={
        Property(name="bpmnprof_BPMNMessage343", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlow342", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
innerMessageFlowRef327: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef327",
    ends={
        Property(name="bpmnprof_MessageFlow329", type=bpmnprof_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlowAssociation328", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef330: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef330",
    ends={
        Property(name="bpmnprof_MessageFlow332", type=bpmnprof_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageFlowAssociation331", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
base_Property361: BinaryAssociation = BinaryAssociation(
    name="base_Property361",
    ends={
        Property(name="bpmnprof_Property363", type=bpmnprof_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationProperty362", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
type364: BinaryAssociation = BinaryAssociation(
    name="type364",
    ends={
        Property(name="bpmnprof_ItemDefinition366", type=bpmnprof_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationProperty365", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
correlationPropertyRetrievalExpression367: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression367",
    ends={
        Property(name="bpmnprof_CorrelationPropertyRetrievalExpression", type=bpmnprof_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationProperty368", type=bpmnprof_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999))
    }
)
base_InformationFlow344: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow344",
    ends={
        Property(name="bpmnprof_InformationFlow346", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConversationNode345", type=bpmnprof_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
messageFlowRefs347: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs347",
    ends={
        Property(name="bpmnprof_MessageFlow349", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConversationNode348", type=bpmnprof_MessageFlow, multiplicity=Multiplicity(1, 9999))
    }
)
correlationKeys350: BinaryAssociation = BinaryAssociation(
    name="correlationKeys350",
    ends={
        Property(name="bpmnprof_CorrelationKey352", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConversationNode351", type=bpmnprof_CorrelationKey, multiplicity=Multiplicity(1, 9999))
    }
)
participantRefs353: BinaryAssociation = BinaryAssociation(
    name="participantRefs353",
    ends={
        Property(name="bpmnprof_Participant355", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConversationNode354", type=bpmnprof_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
base_Class356: BinaryAssociation = BinaryAssociation(
    name="base_Class356",
    ends={
        Property(name="bpmnprof_Class358", type=bpmnprof_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationKey357", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef359: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef359",
    ends={
        Property(name="bpmnprof_CorrelationProperty", type=bpmnprof_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationKey360", type=bpmnprof_CorrelationProperty, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency369: BinaryAssociation = BinaryAssociation(
    name="base_Dependency369",
    ends={
        Property(name="bpmnprof_Dependency371", type=bpmnprof_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyRetrievalExpression370", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
messageRef372: BinaryAssociation = BinaryAssociation(
    name="messageRef372",
    ends={
        Property(name="bpmnprof_BPMNMessage374", type=bpmnprof_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyRetrievalExpression373", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
messagePath375: BinaryAssociation = BinaryAssociation(
    name="messagePath375",
    ends={
        Property(name="bpmnprof_FormalExpression", type=bpmnprof_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyRetrievalExpression376", type=bpmnprof_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_Property388: BinaryAssociation = BinaryAssociation(
    name="base_Property388",
    ends={
        Property(name="bpmnprof_Property390", type=bpmnprof_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyBinding389", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
dataPath391: BinaryAssociation = BinaryAssociation(
    name="dataPath391",
    ends={
        Property(name="bpmnprof_FormalExpression393", type=bpmnprof_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyBinding392", type=bpmnprof_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef394: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef394",
    ends={
        Property(name="bpmnprof_CorrelationProperty396", type=bpmnprof_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationPropertyBinding395", type=bpmnprof_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
evaluatesToTypeRef377: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef377",
    ends={
        Property(name="bpmnprof_ItemDefinition379", type=bpmnprof_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_FormalExpression378", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_Class380: BinaryAssociation = BinaryAssociation(
    name="base_Class380",
    ends={
        Property(name="bpmnprof_Class382", type=bpmnprof_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationSubscription381", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationKeyRef383: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef383",
    ends={
        Property(name="bpmnprof_CorrelationKey385", type=bpmnprof_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationSubscription384", type=bpmnprof_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding386: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding386",
    ends={
        Property(name="bpmnprof_CorrelationPropertyBinding", type=bpmnprof_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CorrelationSubscription387", type=bpmnprof_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 9999))
    }
)
base_DataStoreNode397: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode397",
    ends={
        Property(name="bpmnprof_DataStoreNode", type=bpmnprof_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProperty398", type=bpmnprof_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
umlProperty399: BinaryAssociation = BinaryAssociation(
    name="umlProperty399",
    ends={
        Property(name="bpmnprof_Property401", type=bpmnprof_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNProperty400", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Property402: BinaryAssociation = BinaryAssociation(
    name="base_Property402",
    ends={
        Property(name="bpmnprof_Property403", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceRole", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
resourceAssignmentExpression404: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression404",
    ends={
        Property(name="bpmnprof_ResourceAssignmentExpression", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceRole405", type=bpmnprof_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef406: BinaryAssociation = BinaryAssociation(
    name="resourceRef406",
    ends={
        Property(name="bpmnprof_Resource", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceRole407", type=bpmnprof_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings408: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings408",
    ends={
        Property(name="bpmnprof_ResourceParameterBinding", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceRole409", type=bpmnprof_ResourceParameterBinding, multiplicity=Multiplicity(1, 9999))
    }
)
expression411: BinaryAssociation = BinaryAssociation(
    name="expression411",
    ends={
        Property(name="bpmnprof_BPMNExpression413", type=bpmnprof_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceAssignmentExpression412", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
process410: BinaryAssociation = BinaryAssociation(
    name="process410",
    ends={
        Property(name="BPMNProcess", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=bpmnprof_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameters414: BinaryAssociation = BinaryAssociation(
    name="resourceParameters414",
    ends={
        Property(name="bpmnprof_ResourceParameter", type=bpmnprof_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Resource415", type=bpmnprof_ResourceParameter, multiplicity=Multiplicity(1, 9999))
    }
)
base_Property416: BinaryAssociation = BinaryAssociation(
    name="base_Property416",
    ends={
        Property(name="bpmnprof_Property418", type=bpmnprof_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceParameter417", type=bpmnprof_Property, multiplicity=Multiplicity(1, 1))
    }
)
type419: BinaryAssociation = BinaryAssociation(
    name="type419",
    ends={
        Property(name="bpmnprof_ItemDefinition421", type=bpmnprof_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceParameter420", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueBehavior431: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueBehavior431",
    ends={
        Property(name="bpmnprof_OpaqueBehavior", type=bpmnprof_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_GlobalTask", type=bpmnprof_OpaqueBehavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Slot422: BinaryAssociation = BinaryAssociation(
    name="base_Slot422",
    ends={
        Property(name="bpmnprof_Slot424", type=bpmnprof_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceParameterBinding423", type=bpmnprof_Slot, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef425: BinaryAssociation = BinaryAssociation(
    name="parameterRef425",
    ends={
        Property(name="bpmnprof_ResourceParameter427", type=bpmnprof_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceParameterBinding426", type=bpmnprof_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
expression428: BinaryAssociation = BinaryAssociation(
    name="expression428",
    ends={
        Property(name="bpmnprof_BPMNExpression430", type=bpmnprof_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ResourceParameterBinding429", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
resources432: BinaryAssociation = BinaryAssociation(
    name="resources432",
    ends={
        Property(name="bpmnprof_ResourceRole434", type=bpmnprof_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_GlobalTask433", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
activityRef435: BinaryAssociation = BinaryAssociation(
    name="activityRef435",
    ends={
        Property(name="bpmnprof_BPMNActivity", type=bpmnprof_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CompensateEventDefinition", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent436: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent436",
    ends={
        Property(name="bpmnprof_CallEvent", type=bpmnprof_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CompensateEventDefinition437", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Event438: BinaryAssociation = BinaryAssociation(
    name="base_Event438",
    ends={
        Property(name="bpmnprof_Event", type=bpmnprof_EventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EventDefinition", type=bpmnprof_Event, multiplicity=Multiplicity(1, 1))
    }
)
dataInputAssociations453: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations453",
    ends={
        Property(name="bpmnprof_DataInputAssociation", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity454", type=bpmnprof_DataInputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputAssociations455: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations455",
    ends={
        Property(name="bpmnprof_DataOutputAssociation", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity456", type=bpmnprof_DataOutputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
loopCharacteristics457: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics457",
    ends={
        Property(name="bpmnprof_LoopCharacteristics", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity458", type=bpmnprof_LoopCharacteristics, multiplicity=Multiplicity(0, 1))
    }
)
base_Action439: BinaryAssociation = BinaryAssociation(
    name="base_Action439",
    ends={
        Property(name="bpmnprof_Action441", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity440", type=bpmnprof_Action, multiplicity=Multiplicity(1, 1))
    }
)
activityClass442: BinaryAssociation = BinaryAssociation(
    name="activityClass442",
    ends={
        Property(name="bpmnprof_Class444", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity443", type=bpmnprof_Class, multiplicity=Multiplicity(0, 1))
    }
)
properties445: BinaryAssociation = BinaryAssociation(
    name="properties445",
    ends={
        Property(name="bpmnprof_BPMNProperty447", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity446", type=bpmnprof_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
default448: BinaryAssociation = BinaryAssociation(
    name="default448",
    ends={
        Property(name="bpmnprof_SequenceFlow450", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity449", type=bpmnprof_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
boundaryEventRefs451: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs451",
    ends={
        Property(name="bpmnprof_BoundaryEvent", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity452", type=bpmnprof_BoundaryEvent, multiplicity=Multiplicity(1, 9999))
    }
)
_eventDefinitions473: BinaryAssociation = BinaryAssociation(
    name="_eventDefinitions473",
    ends={
        Property(name="bpmnprof_EventDefinition475", type=bpmnprof_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNEvent474", type=bpmnprof_EventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
properties476: BinaryAssociation = BinaryAssociation(
    name="properties476",
    ends={
        Property(name="bpmnprof_BPMNProperty478", type=bpmnprof_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNEvent477", type=bpmnprof_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
eventDefinitionRefs479: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs479",
    ends={
        Property(name="bpmnprof_EventDefinition481", type=bpmnprof_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNEvent480", type=bpmnprof_EventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
resources459: BinaryAssociation = BinaryAssociation(
    name="resources459",
    ends={
        Property(name="bpmnprof_ResourceRole461", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNActivity460", type=bpmnprof_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
attachedToRef462: BinaryAssociation = BinaryAssociation(
    name="attachedToRef462",
    ends={
        Property(name="bpmnprof_BPMNActivity464", type=bpmnprof_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BoundaryEvent463", type=bpmnprof_BPMNActivity, multiplicity=Multiplicity(1, 1))
    }
)
base_AcceptEventAction465: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction465",
    ends={
        Property(name="bpmnprof_AcceptEventAction", type=bpmnprof_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CatchEvent", type=bpmnprof_AcceptEventAction, multiplicity=Multiplicity(1, 1))
    }
)
base_InitialNode466: BinaryAssociation = BinaryAssociation(
    name="base_InitialNode466",
    ends={
        Property(name="bpmnprof_InitialNode", type=bpmnprof_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CatchEvent467", type=bpmnprof_InitialNode, multiplicity=Multiplicity(1, 1))
    }
)
dataOutputAssociation468: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation468",
    ends={
        Property(name="bpmnprof_DataOutputAssociation470", type=bpmnprof_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CatchEvent469", type=bpmnprof_DataOutputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
eventClass471: BinaryAssociation = BinaryAssociation(
    name="eventClass471",
    ends={
        Property(name="bpmnprof_Class472", type=bpmnprof_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BPMNEvent", type=bpmnprof_Class, multiplicity=Multiplicity(0, 1))
    }
)
base_ObjectFlow482: BinaryAssociation = BinaryAssociation(
    name="base_ObjectFlow482",
    ends={
        Property(name="bpmnprof_ObjectFlow", type=bpmnprof_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataAssociation", type=bpmnprof_ObjectFlow, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode503: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode503",
    ends={
        Property(name="bpmnprof_StructuredActivityNode505", type=bpmnprof_LoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_LoopCharacteristics504", type=bpmnprof_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
escalationRef506: BinaryAssociation = BinaryAssociation(
    name="escalationRef506",
    ends={
        Property(name="bpmnprof_Escalation", type=bpmnprof_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EscalationEventDefinition", type=bpmnprof_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef483: BinaryAssociation = BinaryAssociation(
    name="sourceRef483",
    ends={
        Property(name="bpmnprof_ItemAwareElement485", type=bpmnprof_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataAssociation484", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent507: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent507",
    ends={
        Property(name="bpmnprof_CallEvent509", type=bpmnprof_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EscalationEventDefinition508", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
targetRef486: BinaryAssociation = BinaryAssociation(
    name="targetRef486",
    ends={
        Property(name="bpmnprof_ItemAwareElement488", type=bpmnprof_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataAssociation487", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
transformation489: BinaryAssociation = BinaryAssociation(
    name="transformation489",
    ends={
        Property(name="bpmnprof_FormalExpression491", type=bpmnprof_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataAssociation490", type=bpmnprof_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignment492: BinaryAssociation = BinaryAssociation(
    name="assignment492",
    ends={
        Property(name="bpmnprof_Assignment", type=bpmnprof_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataAssociation493", type=bpmnprof_Assignment, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency494: BinaryAssociation = BinaryAssociation(
    name="base_Dependency494",
    ends={
        Property(name="bpmnprof_Dependency496", type=bpmnprof_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Assignment495", type=bpmnprof_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
from497: BinaryAssociation = BinaryAssociation(
    name="from497",
    ends={
        Property(name="bpmnprof_BPMNExpression499", type=bpmnprof_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Assignment498", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
to500: BinaryAssociation = BinaryAssociation(
    name="to500",
    ends={
        Property(name="bpmnprof_BPMNExpression502", type=bpmnprof_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Assignment501", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_FinalNode524: BinaryAssociation = BinaryAssociation(
    name="base_FinalNode524",
    ends={
        Property(name="bpmnprof_FinalNode", type=bpmnprof_EndEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_EndEvent", type=bpmnprof_FinalNode, multiplicity=Multiplicity(1, 1))
    }
)
timeCycle510: BinaryAssociation = BinaryAssociation(
    name="timeCycle510",
    ends={
        Property(name="bpmnprof_BPMNExpression511", type=bpmnprof_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TimerEventDefinition", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDate512: BinaryAssociation = BinaryAssociation(
    name="timeDate512",
    ends={
        Property(name="bpmnprof_BPMNExpression514", type=bpmnprof_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TimerEventDefinition513", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDuration515: BinaryAssociation = BinaryAssociation(
    name="timeDuration515",
    ends={
        Property(name="bpmnprof_BPMNExpression517", type=bpmnprof_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TimerEventDefinition516", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ChangeEvent518: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent518",
    ends={
        Property(name="bpmnprof_ChangeEvent", type=bpmnprof_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TimerEventDefinition519", type=bpmnprof_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
signalRef520: BinaryAssociation = BinaryAssociation(
    name="signalRef520",
    ends={
        Property(name="bpmnprof_BPMNSignal", type=bpmnprof_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SignalEventDefinition", type=bpmnprof_BPMNSignal, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent521: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent521",
    ends={
        Property(name="bpmnprof_CallEvent523", type=bpmnprof_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SignalEventDefinition522", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
_target545: BinaryAssociation = BinaryAssociation(
    name="_target545",
    ends={
        Property(name="LinkEventDefinition", type=bpmnprof_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmnprof_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
source547: BinaryAssociation = BinaryAssociation(
    name="source547",
    ends={
        Property(name="LinkEventDefinition548", type=bpmnprof_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="_target", type=bpmnprof_LinkEventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
base_CallEvent549: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent549",
    ends={
        Property(name="bpmnprof_CallEvent550", type=bpmnprof_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_LinkEventDefinition", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_CallOperationAction525: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction525",
    ends={
        Property(name="bpmnprof_CallOperationAction", type=bpmnprof_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ThrowEvent", type=bpmnprof_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
base_FlowFinalNode526: BinaryAssociation = BinaryAssociation(
    name="base_FlowFinalNode526",
    ends={
        Property(name="bpmnprof_FlowFinalNode", type=bpmnprof_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ThrowEvent527", type=bpmnprof_FlowFinalNode, multiplicity=Multiplicity(1, 1))
    }
)
dataInputAssociation528: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation528",
    ends={
        Property(name="bpmnprof_DataInputAssociation530", type=bpmnprof_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ThrowEvent529", type=bpmnprof_DataInputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
messageRef531: BinaryAssociation = BinaryAssociation(
    name="messageRef531",
    ends={
        Property(name="bpmnprof_BPMNMessage532", type=bpmnprof_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageEventDefinition", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
operationRef533: BinaryAssociation = BinaryAssociation(
    name="operationRef533",
    ends={
        Property(name="bpmnprof_BPMNOperation535", type=bpmnprof_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageEventDefinition534", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent536: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent536",
    ends={
        Property(name="bpmnprof_CallEvent538", type=bpmnprof_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MessageEventDefinition537", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_ChangeEvent539: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent539",
    ends={
        Property(name="bpmnprof_ChangeEvent540", type=bpmnprof_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConditionalEventDefinition", type=bpmnprof_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
condition541: BinaryAssociation = BinaryAssociation(
    name="condition541",
    ends={
        Property(name="bpmnprof_BPMNExpression543", type=bpmnprof_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ConditionalEventDefinition542", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration563: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration563",
    ends={
        Property(name="bpmnprof_Enumeration", type=bpmnprof_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Category", type=bpmnprof_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
categoryValue564: BinaryAssociation = BinaryAssociation(
    name="categoryValue564",
    ends={
        Property(name="bpmnprof_CategoryValue566", type=bpmnprof_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Category565", type=bpmnprof_CategoryValue, multiplicity=Multiplicity(1, 9999))
    }
)
errorRef551: BinaryAssociation = BinaryAssociation(
    name="errorRef551",
    ends={
        Property(name="bpmnprof_Error552", type=bpmnprof_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ErrorEventDefinition", type=bpmnprof_Error, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent553: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent553",
    ends={
        Property(name="bpmnprof_CallEvent555", type=bpmnprof_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ErrorEventDefinition554", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_SendObjectAction556: BinaryAssociation = BinaryAssociation(
    name="base_SendObjectAction556",
    ends={
        Property(name="bpmnprof_SendObjectAction", type=bpmnprof_IntermediateThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_IntermediateThrowEvent", type=bpmnprof_SendObjectAction, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent557: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent557",
    ends={
        Property(name="bpmnprof_CallEvent558", type=bpmnprof_TerminateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TerminateEventDefinition", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent559: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent559",
    ends={
        Property(name="bpmnprof_CallEvent560", type=bpmnprof_CancelEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CancelEventDefinition", type=bpmnprof_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment561: BinaryAssociation = BinaryAssociation(
    name="base_Comment561",
    ends={
        Property(name="bpmnprof_Comment562", type=bpmnprof_TextAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_TextAnnotation", type=bpmnprof_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode576: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode576",
    ends={
        Property(name="bpmnprof_DataStoreNode578", type=bpmnprof_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataObject577", type=bpmnprof_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityPartition567: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition567",
    ends={
        Property(name="bpmnprof_ActivityPartition568", type=bpmnprof_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Group", type=bpmnprof_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
_categoryValueRef569: BinaryAssociation = BinaryAssociation(
    name="_categoryValueRef569",
    ends={
        Property(name="bpmnprof_CategoryValue571", type=bpmnprof_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Group570", type=bpmnprof_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
dataObjectRef572: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef572",
    ends={
        Property(name="bpmnprof_DataObject", type=bpmnprof_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataObjectReference", type=bpmnprof_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode573: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode573",
    ends={
        Property(name="bpmnprof_DataStoreNode575", type=bpmnprof_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataObjectReference574", type=bpmnprof_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
renderings590: BinaryAssociation = BinaryAssociation(
    name="renderings590",
    ends={
        Property(name="bpmnprof_Rendering", type=bpmnprof_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_UserTask591", type=bpmnprof_Rendering, multiplicity=Multiplicity(1, 9999))
    }
)
ioSpecification592: BinaryAssociation = BinaryAssociation(
    name="ioSpecification592",
    ends={
        Property(name="bpmnprof_InputOutputSpecification593", type=bpmnprof_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Task", type=bpmnprof_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Class579: BinaryAssociation = BinaryAssociation(
    name="base_Class579",
    ends={
        Property(name="bpmnprof_Class580", type=bpmnprof_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataStore", type=bpmnprof_Class, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef581: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef581",
    ends={
        Property(name="bpmnprof_ItemDefinition583", type=bpmnprof_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataStore582", type=bpmnprof_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
_dataStore584: BinaryAssociation = BinaryAssociation(
    name="_dataStore584",
    ends={
        Property(name="bpmnprof_DataStore585", type=bpmnprof_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataStoreReference", type=bpmnprof_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
base_DataStoreNode586: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode586",
    ends={
        Property(name="bpmnprof_DataStoreNode588", type=bpmnprof_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_DataStoreReference587", type=bpmnprof_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction589: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction589",
    ends={
        Property(name="bpmnprof_OpaqueAction", type=bpmnprof_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_UserTask", type=bpmnprof_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction598: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction598",
    ends={
        Property(name="bpmnprof_OpaqueAction599", type=bpmnprof_ManualTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ManualTask", type=bpmnprof_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
base_Image594: BinaryAssociation = BinaryAssociation(
    name="base_Image594",
    ends={
        Property(name="bpmnprof_Image", type=bpmnprof_Rendering, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_Rendering595", type=bpmnprof_Image, multiplicity=Multiplicity(1, 1))
    }
)
renderings596: BinaryAssociation = BinaryAssociation(
    name="renderings596",
    ends={
        Property(name="bpmnprof_Rendering597", type=bpmnprof_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_GlobalUserTask", type=bpmnprof_Rendering, multiplicity=Multiplicity(1, 9999))
    }
)
base_StructuredActivityNode609: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode609",
    ends={
        Property(name="bpmnprof_StructuredActivityNode610", type=bpmnprof_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SubProcess", type=bpmnprof_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
conversationNodes600: BinaryAssociation = BinaryAssociation(
    name="conversationNodes600",
    ends={
        Property(name="bpmnprof_ConversationNode601", type=bpmnprof_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SubConversation", type=bpmnprof_ConversationNode, multiplicity=Multiplicity(1, 9999))
    }
)
_collaborationUse602: BinaryAssociation = BinaryAssociation(
    name="_collaborationUse602",
    ends={
        Property(name="bpmnprof_CollaborationUse", type=bpmnprof_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallConversation", type=bpmnprof_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
calledCollaborationRef603: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef603",
    ends={
        Property(name="bpmnprof_BPMNCollaboration605", type=bpmnprof_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallConversation604", type=bpmnprof_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations606: BinaryAssociation = BinaryAssociation(
    name="participantAssociations606",
    ends={
        Property(name="bpmnprof_ParticipantAssociation608", type=bpmnprof_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallConversation607", type=bpmnprof_ParticipantAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
condition620: BinaryAssociation = BinaryAssociation(
    name="condition620",
    ends={
        Property(name="bpmnprof_FormalExpression621", type=bpmnprof_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ComplexBehaviorDefinition", type=bpmnprof_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
event622: BinaryAssociation = BinaryAssociation(
    name="event622",
    ends={
        Property(name="bpmnprof_ImplicitThrowEvent", type=bpmnprof_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ComplexBehaviorDefinition623", type=bpmnprof_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1))
    }
)
base_ControlFlow624: BinaryAssociation = BinaryAssociation(
    name="base_ControlFlow624",
    ends={
        Property(name="bpmnprof_ControlFlow626", type=bpmnprof_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ComplexBehaviorDefinition625", type=bpmnprof_ControlFlow, multiplicity=Multiplicity(1, 1))
    }
)
hasLaneSets611: BinaryAssociation = BinaryAssociation(
    name="hasLaneSets611",
    ends={
        Property(name="bpmnprof_LaneSet613", type=bpmnprof_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SubProcess612", type=bpmnprof_LaneSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_CallBehaviorAction614: BinaryAssociation = BinaryAssociation(
    name="base_CallBehaviorAction614",
    ends={
        Property(name="bpmnprof_CallBehaviorAction", type=bpmnprof_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallActivity", type=bpmnprof_CallBehaviorAction, multiplicity=Multiplicity(1, 1))
    }
)
calledElementRef615: BinaryAssociation = BinaryAssociation(
    name="calledElementRef615",
    ends={
        Property(name="bpmnprof_CallableElement617", type=bpmnprof_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_CallActivity616", type=bpmnprof_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueAction618: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction618",
    ends={
        Property(name="bpmnprof_OpaqueAction619", type=bpmnprof_BusinessRuleTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_BusinessRuleTask", type=bpmnprof_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
messageRef631: BinaryAssociation = BinaryAssociation(
    name="messageRef631",
    ends={
        Property(name="bpmnprof_BPMNMessage632", type=bpmnprof_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SendTask", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_CallOperationAction633: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction633",
    ends={
        Property(name="bpmnprof_CallOperationAction635", type=bpmnprof_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SendTask634", type=bpmnprof_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef636: BinaryAssociation = BinaryAssociation(
    name="operationRef636",
    ends={
        Property(name="bpmnprof_BPMNOperation638", type=bpmnprof_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_SendTask637", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition627: BinaryAssociation = BinaryAssociation(
    name="completionCondition627",
    ends={
        Property(name="bpmnprof_BPMNExpression628", type=bpmnprof_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_AdHocSubProcess", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction629: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction629",
    ends={
        Property(name="bpmnprof_OpaqueAction630", type=bpmnprof_ScriptTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ScriptTask", type=bpmnprof_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
base_AcceptEventAction645: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction645",
    ends={
        Property(name="bpmnprof_AcceptEventAction647", type=bpmnprof_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ReceiveTask646", type=bpmnprof_AcceptEventAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef648: BinaryAssociation = BinaryAssociation(
    name="operationRef648",
    ends={
        Property(name="bpmnprof_BPMNOperation650", type=bpmnprof_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ReceiveTask649", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_LoopNode639: BinaryAssociation = BinaryAssociation(
    name="base_LoopNode639",
    ends={
        Property(name="bpmnprof_LoopNode", type=bpmnprof_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_StandardLoopCharacteristics", type=bpmnprof_LoopNode, multiplicity=Multiplicity(1, 1))
    }
)
loopCondition640: BinaryAssociation = BinaryAssociation(
    name="loopCondition640",
    ends={
        Property(name="bpmnprof_BPMNExpression642", type=bpmnprof_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_StandardLoopCharacteristics641", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
messageRef643: BinaryAssociation = BinaryAssociation(
    name="messageRef643",
    ends={
        Property(name="bpmnprof_BPMNMessage644", type=bpmnprof_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ReceiveTask", type=bpmnprof_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_ExpansionRegion661: BinaryAssociation = BinaryAssociation(
    name="base_ExpansionRegion661",
    ends={
        Property(name="bpmnprof_ExpansionRegion", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics662", type=bpmnprof_ExpansionRegion, multiplicity=Multiplicity(1, 1))
    }
)
loopDataInputRef663: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef663",
    ends={
        Property(name="bpmnprof_ItemAwareElement665", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics664", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef666: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef666",
    ends={
        Property(name="bpmnprof_ItemAwareElement668", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics667", type=bpmnprof_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
base_CallOperationAction651: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction651",
    ends={
        Property(name="bpmnprof_CallOperationAction652", type=bpmnprof_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ServiceTask", type=bpmnprof_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef653: BinaryAssociation = BinaryAssociation(
    name="operationRef653",
    ends={
        Property(name="bpmnprof_BPMNOperation655", type=bpmnprof_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_ServiceTask654", type=bpmnprof_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
loopCardinality656: BinaryAssociation = BinaryAssociation(
    name="loopCardinality656",
    ends={
        Property(name="bpmnprof_BPMNExpression657", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition658: BinaryAssociation = BinaryAssociation(
    name="completionCondition658",
    ends={
        Property(name="bpmnprof_BPMNExpression660", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics659", type=bpmnprof_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
outputDataItem669: BinaryAssociation = BinaryAssociation(
    name="outputDataItem669",
    ends={
        Property(name="bpmnprof_DataOutput671", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics670", type=bpmnprof_DataOutput, multiplicity=Multiplicity(1, 1))
    }
)
inputDataItem672: BinaryAssociation = BinaryAssociation(
    name="inputDataItem672",
    ends={
        Property(name="bpmnprof_DataInput674", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics673", type=bpmnprof_DataInput, multiplicity=Multiplicity(1, 1))
    }
)
oneBehaviorEventRef675: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef675",
    ends={
        Property(name="bpmnprof_EventDefinition677", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics676", type=bpmnprof_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
noneBehaviorEventRef678: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef678",
    ends={
        Property(name="bpmnprof_EventDefinition680", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics679", type=bpmnprof_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
complexBehaviorDefinition681: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition681",
    ends={
        Property(name="bpmnprof_ComplexBehaviorDefinition683", type=bpmnprof_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnprof_MultiInstanceLoopCharacteristics682", type=bpmnprof_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_bpmnprof_InclusiveGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=bpmnprof_InclusiveGateway)
gen_bpmnprof_FlowElement_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_FlowElement)
gen_bpmnprof_NonExclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmnprof_NonExclusiveGateway)
gen_bpmnprof_Gateway_FlowNode = Generalization(general=FlowNode, specific=bpmnprof_Gateway)
gen_bpmnprof_FlowNode_FlowElement = Generalization(general=FlowElement, specific=bpmnprof_FlowNode)
gen_bpmnprof_Documentation_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Documentation)
gen_bpmnprof_BPMNAssociation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=bpmnprof_BPMNAssociation)
gen_bpmnprof_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CategoryValue)
gen_bpmnprof_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_FlowElementsContainer)
gen_bpmnprof_LaneSet_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_LaneSet)
gen_bpmnprof_BPMNArtifact_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_BPMNArtifact)
gen_bpmnprof_Auditing_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Auditing)
gen_bpmnprof_Monitoring_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Monitoring)
gen_bpmnprof_Lane_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Lane)
gen_bpmnprof_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=bpmnprof_SequenceFlow)
gen_bpmnprof_ParallelGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=bpmnprof_ParallelGateway)
gen_bpmnprof_ComplexGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=bpmnprof_ComplexGateway)
gen_bpmnprof_BPMNExpression_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_BPMNExpression)
gen_bpmnprof_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=bpmnprof_EventBasedGateway)
gen_bpmnprof_Definitions_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Definitions)
gen_bpmnprof_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmnprof_ExclusiveGateway)
gen_bpmnprof_RootElement_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_RootElement)
gen_bpmnprof_BPMNProcess_CallableElement = Generalization(general=CallableElement, specific=bpmnprof_BPMNProcess)
gen_bpmnprof_BPMNProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmnprof_BPMNProcess)
gen_bpmnprof_BPMNRelationship_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_BPMNRelationship)
gen_bpmnprof_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_InputOutputSpecification)
gen_bpmnprof_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_DataInput)
gen_bpmnprof_CallableElement_RootElement = Generalization(general=RootElement, specific=bpmnprof_CallableElement)
gen_bpmnprof_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ItemAwareElement)
gen_bpmnprof_InputSet_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_InputSet)
gen_bpmnprof_DataState_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_DataState)
gen_bpmnprof_ItemDefinition_RootElement = Generalization(general=RootElement, specific=bpmnprof_ItemDefinition)
gen_bpmnprof_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_DataOutput)
gen_bpmnprof_BPMNInterface_RootElement = Generalization(general=RootElement, specific=bpmnprof_BPMNInterface)
gen_bpmnprof_OutputSet_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_OutputSet)
gen_bpmnprof_BPMNOperation_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_BPMNOperation)
gen_bpmnprof_BPMNMessage_ItemDefinition = Generalization(general=ItemDefinition, specific=bpmnprof_BPMNMessage)
gen_bpmnprof_Error_ItemDefinition = Generalization(general=ItemDefinition, specific=bpmnprof_Error)
gen_bpmnprof_InputOutputBinding_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_InputOutputBinding)
gen_bpmnprof_BPMNCollaboration_RootElement = Generalization(general=RootElement, specific=bpmnprof_BPMNCollaboration)
gen_bpmnprof_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ParticipantAssociation)
gen_bpmnprof_Participant_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Participant)
gen_bpmnprof_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ConversationLink)
gen_bpmnprof_ParticipantMultiplicity_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ParticipantMultiplicity)
gen_bpmnprof_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_MessageFlowAssociation)
gen_bpmnprof_PartnerEntity_RootElement = Generalization(general=RootElement, specific=bpmnprof_PartnerEntity)
gen_bpmnprof_PartnerRole_RootElement = Generalization(general=RootElement, specific=bpmnprof_PartnerRole)
gen_bpmnprof_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=bpmnprof_ConversationNode)
gen_bpmnprof_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_MessageFlow)
gen_bpmnprof_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CorrelationKey)
gen_bpmnprof_CorrelationProperty_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CorrelationProperty)
gen_bpmnprof_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CorrelationPropertyRetrievalExpression)
gen_bpmnprof_FormalExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=bpmnprof_FormalExpression)
gen_bpmnprof_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CorrelationPropertyBinding)
gen_bpmnprof_BPMNProperty_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_BPMNProperty)
gen_bpmnprof_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_CorrelationSubscription)
gen_bpmnprof_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ResourceRole)
gen_bpmnprof_ResourceParameterBinding_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ResourceParameterBinding)
gen_bpmnprof_Resource_ItemDefinition = Generalization(general=ItemDefinition, specific=bpmnprof_Resource)
gen_bpmnprof_ResourceAssignmentExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=bpmnprof_ResourceAssignmentExpression)
gen_bpmnprof_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ResourceParameter)
gen_bpmnprof_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=bpmnprof_GlobalTask)
gen_bpmnprof_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmnprof_GlobalScriptTask)
gen_bpmnprof_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmnprof_GlobalBusinessRuleTask)
gen_bpmnprof_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_CompensateEventDefinition)
gen_bpmnprof_EventDefinition_RootElement = Generalization(general=RootElement, specific=bpmnprof_EventDefinition)
gen_bpmnprof_BPMNActivity_FlowNode = Generalization(general=FlowNode, specific=bpmnprof_BPMNActivity)
gen_bpmnprof_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmnprof_BoundaryEvent)
gen_bpmnprof_CatchEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=bpmnprof_CatchEvent)
gen_bpmnprof_BPMNEvent_FlowNode = Generalization(general=FlowNode, specific=bpmnprof_BPMNEvent)
gen_bpmnprof_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmnprof_DataOutputAssociation)
gen_bpmnprof_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_DataAssociation)
gen_bpmnprof_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_EscalationEventDefinition)
gen_bpmnprof_Escalation_ItemDefinition = Generalization(general=ItemDefinition, specific=bpmnprof_Escalation)
gen_bpmnprof_Assignment_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Assignment)
gen_bpmnprof_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmnprof_DataInputAssociation)
gen_bpmnprof_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_LoopCharacteristics)
gen_bpmnprof_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmnprof_EndEvent)
gen_bpmnprof_ThrowEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=bpmnprof_ThrowEvent)
gen_bpmnprof_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_TimerEventDefinition)
gen_bpmnprof_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_SignalEventDefinition)
gen_bpmnprof_BPMNSignal_ItemDefinition = Generalization(general=ItemDefinition, specific=bpmnprof_BPMNSignal)
gen_bpmnprof_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_LinkEventDefinition)
gen_bpmnprof_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_MessageEventDefinition)
gen_bpmnprof_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmnprof_StartEvent)
gen_bpmnprof_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_ConditionalEventDefinition)
gen_bpmnprof_Group_BPMNArtifact = Generalization(general=BPMNArtifact, specific=bpmnprof_Group)
gen_bpmnprof_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_ErrorEventDefinition)
gen_bpmnprof_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmnprof_IntermediateCatchEvent)
gen_bpmnprof_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmnprof_IntermediateThrowEvent)
gen_bpmnprof_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_TerminateEventDefinition)
gen_bpmnprof_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmnprof_ImplicitThrowEvent)
gen_bpmnprof_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmnprof_CancelEventDefinition)
gen_bpmnprof_TextAnnotation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=bpmnprof_TextAnnotation)
gen_bpmnprof_Category_RootElement = Generalization(general=RootElement, specific=bpmnprof_Category)
gen_bpmnprof_DataStore_RootElement = Generalization(general=RootElement, specific=bpmnprof_DataStore)
gen_bpmnprof_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=bpmnprof_DataObjectReference)
gen_bpmnprof_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_DataObjectReference)
gen_bpmnprof_DataObject_FlowElement = Generalization(general=FlowElement, specific=bpmnprof_DataObject)
gen_bpmnprof_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_DataObject)
gen_bpmnprof_Task_BPMNActivity = Generalization(general=BPMNActivity, specific=bpmnprof_Task)
gen_bpmnprof_Rendering_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_Rendering)
gen_bpmnprof_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=bpmnprof_DataStoreReference)
gen_bpmnprof_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmnprof_DataStoreReference)
gen_bpmnprof_UserTask_Task = Generalization(general=Task, specific=bpmnprof_UserTask)
gen_bpmnprof_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=bpmnprof_PotentialOwner)
gen_bpmnprof_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmnprof_SubConversation)
gen_bpmnprof_HumanPerformer_Performer = Generalization(general=Performer, specific=bpmnprof_HumanPerformer)
gen_bpmnprof_Performer_ResourceRole = Generalization(general=ResourceRole, specific=bpmnprof_Performer)
gen_bpmnprof_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmnprof_GlobalUserTask)
gen_bpmnprof_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmnprof_GlobalManualTask)
gen_bpmnprof_ManualTask_Task = Generalization(general=Task, specific=bpmnprof_ManualTask)
gen_bpmnprof_GlobalConversation_BPMNCollaboration = Generalization(general=BPMNCollaboration, specific=bpmnprof_GlobalConversation)
gen_bpmnprof_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmnprof_CallConversation)
gen_bpmnprof_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmnprof_Conversation)
gen_bpmnprof_SubProcess_BPMNActivity = Generalization(general=BPMNActivity, specific=bpmnprof_SubProcess)
gen_bpmnprof_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmnprof_SubProcess)
gen_bpmnprof_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=bpmnprof_ComplexBehaviorDefinition)
gen_bpmnprof_CallActivity_BPMNActivity = Generalization(general=BPMNActivity, specific=bpmnprof_CallActivity)
gen_bpmnprof_BusinessRuleTask_Task = Generalization(general=Task, specific=bpmnprof_BusinessRuleTask)
gen_bpmnprof_Transaction_SubProcess = Generalization(general=SubProcess, specific=bpmnprof_Transaction)
gen_bpmnprof_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=bpmnprof_AdHocSubProcess)
gen_bpmnprof_ScriptTask_Task = Generalization(general=Task, specific=bpmnprof_ScriptTask)
gen_bpmnprof_SendTask_Task = Generalization(general=Task, specific=bpmnprof_SendTask)
gen_bpmnprof_ServiceTask_Task = Generalization(general=Task, specific=bpmnprof_ServiceTask)
gen_bpmnprof_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmnprof_StandardLoopCharacteristics)
gen_bpmnprof_ReceiveTask_Task = Generalization(general=Task, specific=bpmnprof_ReceiveTask)
gen_bpmnprof_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmnprof_MultiInstanceLoopCharacteristics)

# Domain Model
domain_model = DomainModel(
    name="bpmnprof",
    types={bpmnprof_InclusiveGateway, NonExclusiveGateway, bpmnprof_ActivityNode, bpmnprof_FlowElement, BaseElement, bpmnprof_Auditing, bpmnprof_Monitoring, bpmnprof_CategoryValue, bpmnprof_FlowElementsContainer, bpmnprof_BaseElement, bpmnprof_SequenceFlow, bpmnprof_NonExclusiveGateway, Gateway, bpmnprof_JoinNode, bpmnprof_ForkNode, bpmnprof_Gateway, FlowNode, bpmnprof_ControlNode, bpmnprof_ActivityGroup, bpmnprof_FlowNode, FlowElement, bpmnprof_Comment, bpmnprof_Stereotype, BPMNArtifact, bpmnprof_ExtensionAttributeValue, bpmnprof_Element, bpmnprof_Documentation, bpmnprof_ExtensionDefinition, bpmnprof_BPMNAssociation, bpmnprof_Slot, bpmnprof_ExtensionAttributeDefinition, bpmnprof_Property, bpmnprof_EnumerationLiteral, bpmnprof_LaneSet, bpmnprof_Dependency, bpmnprof_BPMNArtifact, bpmnprof_Class, bpmnprof_ActivityPartition, bpmnprof_Lane, bpmnprof_ControlFlow, bpmnprof_ParallelGateway, bpmnprof_ComplexGateway, bpmnprof_BPMNExpression, bpmnprof_OpaqueExpression, bpmnprof_EventBasedGateway, bpmnprof_StructuredActivityNode, bpmnprof_InterruptibleActivityRegion, bpmnprof_Package, bpmnprof_BPMNExtension, bpmnprof_Import, bpmnprof_BPMNRelationship, bpmnprof_ExclusiveGateway, bpmnprof_DecisionNode, bpmnprof_MergeNode, bpmnprof_RootElement, bpmnprof_PackageableElement, bpmnprof_Definitions, bpmnprof_BPMNProcess, CallableElement, FlowElementsContainer, bpmnprof_PackageImport, bpmnprof_Constraint, bpmnprof_BPMNCollaboration, bpmnprof_Activity, bpmnprof_CorrelationSubscription, bpmnprof_BPMNProperty, bpmnprof_ResourceRole, bpmnprof_Action, bpmnprof_DataInput, bpmnprof_DataOutput, bpmnprof_InputSet, bpmnprof_OutputSet, ItemAwareElement, bpmnprof_CallableElement, RootElement, bpmnprof_Behavior, bpmnprof_InputOutputSpecification, bpmnprof_BPMNInterface, bpmnprof_InputOutputBinding, bpmnprof_Parameter, bpmnprof_ActivityParameterNode, bpmnprof_ItemAwareElement, bpmnprof_InputPin, bpmnprof_DataState, bpmnprof_TypedElement, bpmnprof_ItemDefinition, bpmnprof_State, bpmnprof_OutputPin, bpmnprof_ParameterSet, bpmnprof_Interface, bpmnprof_BPMNOperation, bpmnprof_Error, ItemDefinition, bpmnprof_Operation, bpmnprof_BPMNMessage, bpmnprof_ConversationLink, bpmnprof_MessageFlowAssociation, bpmnprof_ParticipantAssociation, bpmnprof_MessageFlow, bpmnprof_Collaboration, bpmnprof_ConversationNode, bpmnprof_CorrelationKey, bpmnprof_Participant, bpmnprof_MultiplicityElement, bpmnprof_ParticipantMultiplicity, bpmnprof_PartnerEntity, bpmnprof_PartnerRole, bpmnprof_InteractionNode, bpmnprof_InstanceSpecification, bpmnprof_InformationFlow, InteractionNode, bpmnprof_CorrelationPropertyRetrievalExpression, bpmnprof_CorrelationProperty, bpmnprof_FormalExpression, BPMNExpression, bpmnprof_CorrelationPropertyBinding, bpmnprof_DataStoreNode, bpmnprof_ResourceAssignmentExpression, bpmnprof_Resource, bpmnprof_ResourceParameterBinding, bpmnprof_ResourceParameter, bpmnprof_GlobalTask, bpmnprof_OpaqueBehavior, bpmnprof_GlobalScriptTask, GlobalTask, bpmnprof_GlobalBusinessRuleTask, bpmnprof_CompensateEventDefinition, EventDefinition, bpmnprof_BPMNActivity, bpmnprof_CallEvent, bpmnprof_EventDefinition, bpmnprof_Event, bpmnprof_DataInputAssociation, bpmnprof_DataOutputAssociation, bpmnprof_LoopCharacteristics, bpmnprof_BoundaryEvent, CatchEvent, bpmnprof_CatchEvent, BPMNEvent, bpmnprof_AcceptEventAction, bpmnprof_InitialNode, bpmnprof_BPMNEvent, bpmnprof_ObjectFlow, DataAssociation, bpmnprof_DataAssociation, bpmnprof_EscalationEventDefinition, bpmnprof_Escalation, bpmnprof_Assignment, bpmnprof_EndEvent, ThrowEvent, bpmnprof_FinalNode, bpmnprof_ThrowEvent, bpmnprof_TimerEventDefinition, bpmnprof_ChangeEvent, bpmnprof_SignalEventDefinition, bpmnprof_BPMNSignal, bpmnprof_ErrorEventDefinition, bpmnprof_CallOperationAction, bpmnprof_FlowFinalNode, bpmnprof_MessageEventDefinition, bpmnprof_StartEvent, bpmnprof_ConditionalEventDefinition, bpmnprof_LinkEventDefinition, bpmnprof_Enumeration, bpmnprof_Group, bpmnprof_IntermediateCatchEvent, bpmnprof_IntermediateThrowEvent, bpmnprof_SendObjectAction, bpmnprof_TerminateEventDefinition, bpmnprof_ImplicitThrowEvent, bpmnprof_CancelEventDefinition, bpmnprof_TextAnnotation, bpmnprof_Category, bpmnprof_DataStore, bpmnprof_DataObjectReference, bpmnprof_DataObject, bpmnprof_Rendering, bpmnprof_Task, BPMNActivity, bpmnprof_DataStoreReference, bpmnprof_UserTask, Task, bpmnprof_OpaqueAction, bpmnprof_PotentialOwner, HumanPerformer, bpmnprof_SubConversation, ConversationNode, bpmnprof_Image, bpmnprof_HumanPerformer, Performer, bpmnprof_Performer, ResourceRole, bpmnprof_GlobalUserTask, bpmnprof_GlobalManualTask, bpmnprof_ManualTask, bpmnprof_GlobalConversation, BPMNCollaboration, bpmnprof_CallConversation, bpmnprof_CollaborationUse, bpmnprof_Conversation, bpmnprof_SubProcess, bpmnprof_ComplexBehaviorDefinition, bpmnprof_CallActivity, bpmnprof_CallBehaviorAction, bpmnprof_BusinessRuleTask, bpmnprof_Transaction, bpmnprof_AdHocSubProcess, SubProcess, bpmnprof_ScriptTask, bpmnprof_SendTask, bpmnprof_ServiceTask, bpmnprof_StandardLoopCharacteristics, LoopCharacteristics, bpmnprof_LoopNode, bpmnprof_ReceiveTask, bpmnprof_ExpansionRegion, bpmnprof_MultiInstanceLoopCharacteristics, AssociationDirection, EventBasedGatewayType, GatewayDirection, RelationshipDirection, ItemKind, ProcessType, AdHocOrdering, MultiInstanceBehavior},
    associations={base_ActivityNode7, auditing8, monitoring9, _categoryValueRef11, container12, default0, base_JoinNode1, base_ForkNode2, base_ControlNode4, base_ActivityGroup5, base_Comment32, base_Stereotype34, extensionAttributeDefinitions36, extensionValues13, base_Element14, documentation16, extensionDefinitions18, outgoing20, incoming21, base_Slot23, valueRef25, extensionAttributeDefinition28, base_Property30, base_EnumerationLiteral48, categorizedFlowElements49, laneSets50, flowElements51, base_Dependency39, targetRef40, sourceRef41, base_Class43, base_Class45, flowElementsContainer57, base_ActivityPartition53, lanes54, parentLane55, base_ControlFlow76, base_ActivityPartition59, _partitionElement62, flowNodeRefs65, partitionElementRef68, childLaneSet71, laneSet74, conditionExpression78, base_OpaqueExpression80, base_ForkNode82, base_StructuredActivityNode84, base_InterruptibleActivityRegion86, base_Package101, extensions102, imports104, relationships106, default88, activationCondition90, base_DecisionNode93, base_MergeNode94, default96, base_PackageableElement99, definition100, targets122, sources125, definition128, rootElements108, base_Stereotype109, definition112, base_PackageImport115, definitions117, base_Constraint120, definitionalCollaborationRef133, base_Activity135, correlationSubscriptions137, monitoring139, supports143, properties145, auditing131, base_Behavior155, base_Action158, dataInputs160, dataOutputs162, inputSets164, outputSets166, resources147, base_Behavior148, ioSpecification149, supportedInterfaceRefs151, ioBinding153, base_Parameter170, base_ActivityParameterNode172, inputSetRefs174, inputSetWithOptional175, inputSetWithWhileExecuting177, base_InputPin168, base_Class186, structureRef189, import192, dataState179, base_TypedElement180, itemSubjectRef182, base_State184, base_OutputPin202, base_Parameter204, base_ActivityParameterNode207, outputSetRefs210, base_ParameterSet195, optionalInputRefs197, whileExecutingInputRefs198, dataInputRefs200, base_ParameterSet217, optionalOutputRefs220, whileExecutingOutputRefs223, dataOutputRefs226, outputSetWithOptional211, outputSetWithWhileExecuting214, base_Interface227, implementationRef229, operations232, callableElements234, inMessageRef242, outMessageRef244, errorRef247, itemRef249, inputDataRef252, base_Operation237, implementationRef239, conversationLinks266, messageFlowAssociations267, outputDataRef255, operationRef258, base_Dependency261, participantAssociations264, base_Dependency279, innerParticipantRef282, outerParticipantRef285, messageFlows269, base_Collaboration271, conversations273, correlationKeys275, participants277, base_Property288, outgoingConversationLinks304, incomingConversationLinks307, collaboration310, base_Dependency311, targetRef313, sourceRef314, base_MultiplicityElement316, processRef291, participantMultiplicity294, partnerEntityRef296, partnerRoleRef297, interfaceRefs299, base_Element302, base_Class320, participantRef322, base_Dependency324, base_InstanceSpecification318, participantRef319, base_InformationFlow333, sourceRef335, targetRef338, messageRef341, innerMessageFlowRef327, outerMessageFlowRef330, base_Property361, type364, correlationPropertyRetrievalExpression367, base_InformationFlow344, messageFlowRefs347, correlationKeys350, participantRefs353, base_Class356, correlationPropertyRef359, base_Dependency369, messageRef372, messagePath375, base_Property388, dataPath391, correlationPropertyRef394, evaluatesToTypeRef377, base_Class380, correlationKeyRef383, correlationPropertyBinding386, base_DataStoreNode397, umlProperty399, base_Property402, resourceAssignmentExpression404, resourceRef406, resourceParameterBindings408, expression411, process410, resourceParameters414, base_Property416, type419, base_OpaqueBehavior431, base_Slot422, parameterRef425, expression428, resources432, activityRef435, base_CallEvent436, base_Event438, dataInputAssociations453, dataOutputAssociations455, loopCharacteristics457, base_Action439, activityClass442, properties445, default448, boundaryEventRefs451, _eventDefinitions473, properties476, eventDefinitionRefs479, resources459, attachedToRef462, base_AcceptEventAction465, base_InitialNode466, dataOutputAssociation468, eventClass471, base_ObjectFlow482, base_StructuredActivityNode503, escalationRef506, sourceRef483, base_CallEvent507, targetRef486, transformation489, assignment492, base_Dependency494, from497, to500, base_FinalNode524, timeCycle510, timeDate512, timeDuration515, base_ChangeEvent518, signalRef520, base_CallEvent521, _target545, source547, base_CallEvent549, base_CallOperationAction525, base_FlowFinalNode526, dataInputAssociation528, messageRef531, operationRef533, base_CallEvent536, base_ChangeEvent539, condition541, base_Enumeration563, categoryValue564, errorRef551, base_CallEvent553, base_SendObjectAction556, base_CallEvent557, base_CallEvent559, base_Comment561, base_DataStoreNode576, base_ActivityPartition567, _categoryValueRef569, dataObjectRef572, base_DataStoreNode573, renderings590, ioSpecification592, base_Class579, itemSubjectRef581, _dataStore584, base_DataStoreNode586, base_OpaqueAction589, base_OpaqueAction598, base_Image594, renderings596, base_StructuredActivityNode609, conversationNodes600, _collaborationUse602, calledCollaborationRef603, participantAssociations606, condition620, event622, base_ControlFlow624, hasLaneSets611, base_CallBehaviorAction614, calledElementRef615, base_OpaqueAction618, messageRef631, base_CallOperationAction633, operationRef636, completionCondition627, base_OpaqueAction629, base_AcceptEventAction645, operationRef648, base_LoopNode639, loopCondition640, messageRef643, base_ExpansionRegion661, loopDataInputRef663, loopDataOutputRef666, base_CallOperationAction651, operationRef653, loopCardinality656, completionCondition658, outputDataItem669, inputDataItem672, oneBehaviorEventRef675, noneBehaviorEventRef678, complexBehaviorDefinition681},
    generalizations={gen_bpmnprof_InclusiveGateway_NonExclusiveGateway, gen_bpmnprof_FlowElement_BaseElement, gen_bpmnprof_NonExclusiveGateway_Gateway, gen_bpmnprof_Gateway_FlowNode, gen_bpmnprof_FlowNode_FlowElement, gen_bpmnprof_Documentation_BaseElement, gen_bpmnprof_BPMNAssociation_BPMNArtifact, gen_bpmnprof_CategoryValue_BaseElement, gen_bpmnprof_FlowElementsContainer_BaseElement, gen_bpmnprof_LaneSet_BaseElement, gen_bpmnprof_BPMNArtifact_BaseElement, gen_bpmnprof_Auditing_BaseElement, gen_bpmnprof_Monitoring_BaseElement, gen_bpmnprof_Lane_BaseElement, gen_bpmnprof_SequenceFlow_FlowElement, gen_bpmnprof_ParallelGateway_NonExclusiveGateway, gen_bpmnprof_ComplexGateway_NonExclusiveGateway, gen_bpmnprof_BPMNExpression_BaseElement, gen_bpmnprof_EventBasedGateway_Gateway, gen_bpmnprof_Definitions_BaseElement, gen_bpmnprof_ExclusiveGateway_Gateway, gen_bpmnprof_RootElement_BaseElement, gen_bpmnprof_BPMNProcess_CallableElement, gen_bpmnprof_BPMNProcess_FlowElementsContainer, gen_bpmnprof_BPMNRelationship_BaseElement, gen_bpmnprof_InputOutputSpecification_BaseElement, gen_bpmnprof_DataInput_ItemAwareElement, gen_bpmnprof_CallableElement_RootElement, gen_bpmnprof_ItemAwareElement_BaseElement, gen_bpmnprof_InputSet_BaseElement, gen_bpmnprof_DataState_BaseElement, gen_bpmnprof_ItemDefinition_RootElement, gen_bpmnprof_DataOutput_ItemAwareElement, gen_bpmnprof_BPMNInterface_RootElement, gen_bpmnprof_OutputSet_BaseElement, gen_bpmnprof_BPMNOperation_BaseElement, gen_bpmnprof_BPMNMessage_ItemDefinition, gen_bpmnprof_Error_ItemDefinition, gen_bpmnprof_InputOutputBinding_BaseElement, gen_bpmnprof_BPMNCollaboration_RootElement, gen_bpmnprof_ParticipantAssociation_BaseElement, gen_bpmnprof_Participant_BaseElement, gen_bpmnprof_ConversationLink_BaseElement, gen_bpmnprof_ParticipantMultiplicity_BaseElement, gen_bpmnprof_MessageFlowAssociation_BaseElement, gen_bpmnprof_PartnerEntity_RootElement, gen_bpmnprof_PartnerRole_RootElement, gen_bpmnprof_ConversationNode_InteractionNode, gen_bpmnprof_MessageFlow_BaseElement, gen_bpmnprof_CorrelationKey_BaseElement, gen_bpmnprof_CorrelationProperty_BaseElement, gen_bpmnprof_CorrelationPropertyRetrievalExpression_BaseElement, gen_bpmnprof_FormalExpression_BPMNExpression, gen_bpmnprof_CorrelationPropertyBinding_BaseElement, gen_bpmnprof_BPMNProperty_ItemAwareElement, gen_bpmnprof_CorrelationSubscription_BaseElement, gen_bpmnprof_ResourceRole_BaseElement, gen_bpmnprof_ResourceParameterBinding_BaseElement, gen_bpmnprof_Resource_ItemDefinition, gen_bpmnprof_ResourceAssignmentExpression_BPMNExpression, gen_bpmnprof_ResourceParameter_BaseElement, gen_bpmnprof_GlobalTask_CallableElement, gen_bpmnprof_GlobalScriptTask_GlobalTask, gen_bpmnprof_GlobalBusinessRuleTask_GlobalTask, gen_bpmnprof_CompensateEventDefinition_EventDefinition, gen_bpmnprof_EventDefinition_RootElement, gen_bpmnprof_BPMNActivity_FlowNode, gen_bpmnprof_BoundaryEvent_CatchEvent, gen_bpmnprof_CatchEvent_BPMNEvent, gen_bpmnprof_BPMNEvent_FlowNode, gen_bpmnprof_DataOutputAssociation_DataAssociation, gen_bpmnprof_DataAssociation_BaseElement, gen_bpmnprof_EscalationEventDefinition_EventDefinition, gen_bpmnprof_Escalation_ItemDefinition, gen_bpmnprof_Assignment_BaseElement, gen_bpmnprof_DataInputAssociation_DataAssociation, gen_bpmnprof_LoopCharacteristics_BaseElement, gen_bpmnprof_EndEvent_ThrowEvent, gen_bpmnprof_ThrowEvent_BPMNEvent, gen_bpmnprof_TimerEventDefinition_EventDefinition, gen_bpmnprof_SignalEventDefinition_EventDefinition, gen_bpmnprof_BPMNSignal_ItemDefinition, gen_bpmnprof_LinkEventDefinition_EventDefinition, gen_bpmnprof_MessageEventDefinition_EventDefinition, gen_bpmnprof_StartEvent_CatchEvent, gen_bpmnprof_ConditionalEventDefinition_EventDefinition, gen_bpmnprof_Group_BPMNArtifact, gen_bpmnprof_ErrorEventDefinition_EventDefinition, gen_bpmnprof_IntermediateCatchEvent_CatchEvent, gen_bpmnprof_IntermediateThrowEvent_ThrowEvent, gen_bpmnprof_TerminateEventDefinition_EventDefinition, gen_bpmnprof_ImplicitThrowEvent_ThrowEvent, gen_bpmnprof_CancelEventDefinition_EventDefinition, gen_bpmnprof_TextAnnotation_BPMNArtifact, gen_bpmnprof_Category_RootElement, gen_bpmnprof_DataStore_RootElement, gen_bpmnprof_DataObjectReference_FlowElement, gen_bpmnprof_DataObjectReference_ItemAwareElement, gen_bpmnprof_DataObject_FlowElement, gen_bpmnprof_DataObject_ItemAwareElement, gen_bpmnprof_Task_BPMNActivity, gen_bpmnprof_Rendering_BaseElement, gen_bpmnprof_DataStoreReference_FlowElement, gen_bpmnprof_DataStoreReference_ItemAwareElement, gen_bpmnprof_UserTask_Task, gen_bpmnprof_PotentialOwner_HumanPerformer, gen_bpmnprof_SubConversation_ConversationNode, gen_bpmnprof_HumanPerformer_Performer, gen_bpmnprof_Performer_ResourceRole, gen_bpmnprof_GlobalUserTask_GlobalTask, gen_bpmnprof_GlobalManualTask_GlobalTask, gen_bpmnprof_ManualTask_Task, gen_bpmnprof_GlobalConversation_BPMNCollaboration, gen_bpmnprof_CallConversation_ConversationNode, gen_bpmnprof_Conversation_ConversationNode, gen_bpmnprof_SubProcess_BPMNActivity, gen_bpmnprof_SubProcess_FlowElementsContainer, gen_bpmnprof_ComplexBehaviorDefinition_BaseElement, gen_bpmnprof_CallActivity_BPMNActivity, gen_bpmnprof_BusinessRuleTask_Task, gen_bpmnprof_Transaction_SubProcess, gen_bpmnprof_AdHocSubProcess_SubProcess, gen_bpmnprof_ScriptTask_Task, gen_bpmnprof_SendTask_Task, gen_bpmnprof_ServiceTask_Task, gen_bpmnprof_StandardLoopCharacteristics_LoopCharacteristics, gen_bpmnprof_ReceiveTask_Task, gen_bpmnprof_MultiInstanceLoopCharacteristics_LoopCharacteristics},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)