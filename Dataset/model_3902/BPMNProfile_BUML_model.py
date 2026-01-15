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
            EnumerationLiteral(name="unspecified"),
			EnumerationLiteral(name="converging"),
			EnumerationLiteral(name="diverging"),
			EnumerationLiteral(name="mixed")
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
            EnumerationLiteral(name="private"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="public")
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
BPMNProfile_JoinNode = Class(name="BPMNProfile::JoinNode")
BPMNProfile_ForkNode = Class(name="BPMNProfile::ForkNode")
BPMNProfile_Comment = Class(name="BPMNProfile::Comment")
BPMNProfile_Gateway = Class(name="BPMNProfile::Gateway", is_abstract=True)
FlowNode = Class(name="FlowNode")
BPMNProfile_ControlNode = Class(name="BPMNProfile::ControlNode")
BPMNProfile_ActivityGroup = Class(name="BPMNProfile::ActivityGroup")
BPMNProfile_FlowNode = Class(name="BPMNProfile::FlowNode", is_abstract=True)
FlowElement = Class(name="FlowElement")
BPMNProfile_ActivityNode = Class(name="BPMNProfile::ActivityNode")
BPMNProfile_FlowElement = Class(name="BPMNProfile::FlowElement", is_abstract=True)
BaseElement = Class(name="BaseElement")
BPMNProfile_Auditing = Class(name="BPMNProfile::Auditing")
BPMNProfile_Monitoring = Class(name="BPMNProfile::Monitoring")
BPMNProfile_CategoryValue = Class(name="BPMNProfile::CategoryValue")
BPMNProfile_FlowElementsContainer = Class(name="BPMNProfile::FlowElementsContainer", is_abstract=True)
BPMNProfile_BaseElement = Class(name="BPMNProfile::BaseElement", is_abstract=True)
BPMNProfile_ExtensionAttributeValue = Class(name="BPMNProfile::ExtensionAttributeValue")
BPMNProfile_Element = Class(name="BPMNProfile::Element")
BPMNProfile_Documentation = Class(name="BPMNProfile::Documentation")
BPMNProfile_InclusiveGateway = Class(name="BPMNProfile::InclusiveGateway")
BPMNProfile_ExtensionDefinition = Class(name="BPMNProfile::ExtensionDefinition")
NonExclusiveGateway = Class(name="NonExclusiveGateway")
BPMNProfile_BPMNAssociation = Class(name="BPMNProfile::BPMNAssociation")
BPMNProfile_Slot = Class(name="BPMNProfile::Slot")
BPMNProfile_SequenceFlow = Class(name="BPMNProfile::SequenceFlow")
BPMNProfile_ExtensionAttributeDefinition = Class(name="BPMNProfile::ExtensionAttributeDefinition")
BPMNProfile_Property = Class(name="BPMNProfile::Property")
BPMNProfile_NonExclusiveGateway = Class(name="BPMNProfile::NonExclusiveGateway", is_abstract=True)
Gateway = Class(name="Gateway")
BPMNProfile_Stereotype = Class(name="BPMNProfile::Stereotype")
BPMNArtifact = Class(name="BPMNArtifact")
BPMNProfile_Dependency = Class(name="BPMNProfile::Dependency")
BPMNProfile_BPMNArtifact = Class(name="BPMNProfile::BPMNArtifact", is_abstract=True)
BPMNProfile_Class = Class(name="BPMNProfile::Class")
BPMNProfile_EnumerationLiteral = Class(name="BPMNProfile::EnumerationLiteral")
BPMNProfile_LaneSet = Class(name="BPMNProfile::LaneSet")
BPMNProfile_ActivityPartition = Class(name="BPMNProfile::ActivityPartition")
BPMNProfile_Lane = Class(name="BPMNProfile::Lane")
BPMNProfile_OpaqueExpression = Class(name="BPMNProfile::OpaqueExpression")
BPMNProfile_EventBasedGateway = Class(name="BPMNProfile::EventBasedGateway")
BPMNProfile_ControlFlow = Class(name="BPMNProfile::ControlFlow")
BPMNProfile_BPMNExpression = Class(name="BPMNProfile::BPMNExpression")
BPMNProfile_DecisionNode = Class(name="BPMNProfile::DecisionNode")
BPMNProfile_MergeNode = Class(name="BPMNProfile::MergeNode")
BPMNProfile_RootElement = Class(name="BPMNProfile::RootElement", is_abstract=True)
BPMNProfile_PackageableElement = Class(name="BPMNProfile::PackageableElement")
BPMNProfile_StructuredActivityNode = Class(name="BPMNProfile::StructuredActivityNode")
BPMNProfile_InterruptibleActivityRegion = Class(name="BPMNProfile::InterruptibleActivityRegion")
BPMNProfile_ParallelGateway = Class(name="BPMNProfile::ParallelGateway")
BPMNProfile_ComplexGateway = Class(name="BPMNProfile::ComplexGateway")
BPMNProfile_ExclusiveGateway = Class(name="BPMNProfile::ExclusiveGateway")
BPMNProfile_Constraint = Class(name="BPMNProfile::Constraint")
BPMNProfile_Definitions = Class(name="BPMNProfile::Definitions")
BPMNProfile_Package = Class(name="BPMNProfile::Package")
BPMNProfile_BPMNExtension = Class(name="BPMNProfile::BPMNExtension")
BPMNProfile_Import = Class(name="BPMNProfile::Import")
BPMNProfile_BPMNRelationship = Class(name="BPMNProfile::BPMNRelationship")
BPMNProfile_PackageImport = Class(name="BPMNProfile::PackageImport")
BPMNProfile_BPMNCollaboration = Class(name="BPMNProfile::BPMNCollaboration")
BPMNProfile_Activity = Class(name="BPMNProfile::Activity")
BPMNProfile_CorrelationSubscription = Class(name="BPMNProfile::CorrelationSubscription")
BPMNProfile_BPMNProcess = Class(name="BPMNProfile::BPMNProcess")
CallableElement = Class(name="CallableElement")
FlowElementsContainer = Class(name="FlowElementsContainer")
BPMNProfile_DataInput = Class(name="BPMNProfile::DataInput")
BPMNProfile_DataOutput = Class(name="BPMNProfile::DataOutput")
BPMNProfile_InputSet = Class(name="BPMNProfile::InputSet")
BPMNProfile_OutputSet = Class(name="BPMNProfile::OutputSet")
BPMNProfile_BPMNProperty = Class(name="BPMNProfile::BPMNProperty")
BPMNProfile_ResourceRole = Class(name="BPMNProfile::ResourceRole")
BPMNProfile_CallableElement = Class(name="BPMNProfile::CallableElement", is_abstract=True)
RootElement = Class(name="RootElement")
BPMNProfile_Behavior = Class(name="BPMNProfile::Behavior")
BPMNProfile_InputOutputSpecification = Class(name="BPMNProfile::InputOutputSpecification")
BPMNProfile_BPMNInterface = Class(name="BPMNProfile::BPMNInterface")
BPMNProfile_InputOutputBinding = Class(name="BPMNProfile::InputOutputBinding")
BPMNProfile_Action = Class(name="BPMNProfile::Action")
ItemAwareElement = Class(name="ItemAwareElement")
BPMNProfile_InputPin = Class(name="BPMNProfile::InputPin")
BPMNProfile_Parameter = Class(name="BPMNProfile::Parameter")
BPMNProfile_ActivityParameterNode = Class(name="BPMNProfile::ActivityParameterNode")
BPMNProfile_ItemDefinition = Class(name="BPMNProfile::ItemDefinition")
BPMNProfile_State = Class(name="BPMNProfile::State")
BPMNProfile_ItemAwareElement = Class(name="BPMNProfile::ItemAwareElement", is_abstract=True)
BPMNProfile_DataState = Class(name="BPMNProfile::DataState")
BPMNProfile_TypedElement = Class(name="BPMNProfile::TypedElement")
BPMNProfile_ParameterSet = Class(name="BPMNProfile::ParameterSet")
BPMNProfile_OutputPin = Class(name="BPMNProfile::OutputPin")
BPMNProfile_Operation = Class(name="BPMNProfile::Operation")
BPMNProfile_Interface = Class(name="BPMNProfile::Interface")
BPMNProfile_BPMNOperation = Class(name="BPMNProfile::BPMNOperation")
BPMNProfile_ParticipantAssociation = Class(name="BPMNProfile::ParticipantAssociation")
BPMNProfile_BPMNMessage = Class(name="BPMNProfile::BPMNMessage")
BPMNProfile_Error = Class(name="BPMNProfile::Error")
ItemDefinition = Class(name="ItemDefinition")
BPMNProfile_ConversationLink = Class(name="BPMNProfile::ConversationLink")
BPMNProfile_MessageFlowAssociation = Class(name="BPMNProfile::MessageFlowAssociation")
BPMNProfile_MessageFlow = Class(name="BPMNProfile::MessageFlow")
BPMNProfile_Collaboration = Class(name="BPMNProfile::Collaboration")
BPMNProfile_ConversationNode = Class(name="BPMNProfile::ConversationNode", is_abstract=True)
BPMNProfile_CorrelationKey = Class(name="BPMNProfile::CorrelationKey")
BPMNProfile_Participant = Class(name="BPMNProfile::Participant")
BPMNProfile_ParticipantMultiplicity = Class(name="BPMNProfile::ParticipantMultiplicity")
BPMNProfile_InstanceSpecification = Class(name="BPMNProfile::InstanceSpecification")
BPMNProfile_PartnerEntity = Class(name="BPMNProfile::PartnerEntity")
BPMNProfile_PartnerRole = Class(name="BPMNProfile::PartnerRole")
BPMNProfile_InteractionNode = Class(name="BPMNProfile::InteractionNode", is_abstract=True)
BPMNProfile_MultiplicityElement = Class(name="BPMNProfile::MultiplicityElement")
BPMNProfile_CorrelationPropertyRetrievalExpression = Class(name="BPMNProfile::CorrelationPropertyRetrievalExpression")
BPMNProfile_InformationFlow = Class(name="BPMNProfile::InformationFlow")
InteractionNode = Class(name="InteractionNode")
BPMNProfile_CorrelationProperty = Class(name="BPMNProfile::CorrelationProperty")
BPMNProfile_DataStoreNode = Class(name="BPMNProfile::DataStoreNode")
BPMNProfile_FormalExpression = Class(name="BPMNProfile::FormalExpression")
BPMNExpression = Class(name="BPMNExpression")
BPMNProfile_CorrelationPropertyBinding = Class(name="BPMNProfile::CorrelationPropertyBinding")
BPMNProfile_ResourceAssignmentExpression = Class(name="BPMNProfile::ResourceAssignmentExpression")
BPMNProfile_Resource = Class(name="BPMNProfile::Resource")
BPMNProfile_ResourceParameterBinding = Class(name="BPMNProfile::ResourceParameterBinding")
BPMNProfile_ResourceParameter = Class(name="BPMNProfile::ResourceParameter")
BPMNProfile_GlobalBusinessRuleTask = Class(name="BPMNProfile::GlobalBusinessRuleTask")
BPMNProfile_GlobalScriptTask = Class(name="BPMNProfile::GlobalScriptTask")
GlobalTask = Class(name="GlobalTask")
BPMNProfile_GlobalTask = Class(name="BPMNProfile::GlobalTask")
BPMNProfile_OpaqueBehavior = Class(name="BPMNProfile::OpaqueBehavior")
BPMNProfile_CompensateEventDefinition = Class(name="BPMNProfile::CompensateEventDefinition")
EventDefinition = Class(name="EventDefinition")
BPMNProfile_BPMNActivity = Class(name="BPMNProfile::BPMNActivity", is_abstract=True)
BPMNProfile_CallEvent = Class(name="BPMNProfile::CallEvent")
BPMNProfile_EventDefinition = Class(name="BPMNProfile::EventDefinition", is_abstract=True)
BPMNProfile_Event = Class(name="BPMNProfile::Event")
BPMNProfile_AcceptEventAction = Class(name="BPMNProfile::AcceptEventAction")
BPMNProfile_InitialNode = Class(name="BPMNProfile::InitialNode")
BPMNProfile_BPMNEvent = Class(name="BPMNProfile::BPMNEvent", is_abstract=True)
BPMNProfile_BoundaryEvent = Class(name="BPMNProfile::BoundaryEvent")
BPMNProfile_DataInputAssociation = Class(name="BPMNProfile::DataInputAssociation")
BPMNProfile_DataOutputAssociation = Class(name="BPMNProfile::DataOutputAssociation")
BPMNProfile_LoopCharacteristics = Class(name="BPMNProfile::LoopCharacteristics", is_abstract=True)
CatchEvent = Class(name="CatchEvent")
BPMNProfile_CatchEvent = Class(name="BPMNProfile::CatchEvent", is_abstract=True)
BPMNEvent = Class(name="BPMNEvent")
DataAssociation = Class(name="DataAssociation")
BPMNProfile_DataAssociation = Class(name="BPMNProfile::DataAssociation", is_abstract=True)
BPMNProfile_ObjectFlow = Class(name="BPMNProfile::ObjectFlow")
BPMNProfile_Assignment = Class(name="BPMNProfile::Assignment")
BPMNProfile_EscalationEventDefinition = Class(name="BPMNProfile::EscalationEventDefinition")
BPMNProfile_Escalation = Class(name="BPMNProfile::Escalation")
BPMNProfile_EndEvent = Class(name="BPMNProfile::EndEvent")
ThrowEvent = Class(name="ThrowEvent")
BPMNProfile_FinalNode = Class(name="BPMNProfile::FinalNode")
BPMNProfile_ThrowEvent = Class(name="BPMNProfile::ThrowEvent", is_abstract=True)
BPMNProfile_TimerEventDefinition = Class(name="BPMNProfile::TimerEventDefinition")
BPMNProfile_ChangeEvent = Class(name="BPMNProfile::ChangeEvent")
BPMNProfile_SignalEventDefinition = Class(name="BPMNProfile::SignalEventDefinition")
BPMNProfile_BPMNSignal = Class(name="BPMNProfile::BPMNSignal")
BPMNProfile_LinkEventDefinition = Class(name="BPMNProfile::LinkEventDefinition")
BPMNProfile_CallOperationAction = Class(name="BPMNProfile::CallOperationAction")
BPMNProfile_FlowFinalNode = Class(name="BPMNProfile::FlowFinalNode")
BPMNProfile_MessageEventDefinition = Class(name="BPMNProfile::MessageEventDefinition")
BPMNProfile_StartEvent = Class(name="BPMNProfile::StartEvent")
BPMNProfile_ConditionalEventDefinition = Class(name="BPMNProfile::ConditionalEventDefinition")
BPMNProfile_Group = Class(name="BPMNProfile::Group")
BPMNProfile_ErrorEventDefinition = Class(name="BPMNProfile::ErrorEventDefinition")
BPMNProfile_IntermediateCatchEvent = Class(name="BPMNProfile::IntermediateCatchEvent")
BPMNProfile_IntermediateThrowEvent = Class(name="BPMNProfile::IntermediateThrowEvent")
BPMNProfile_SendObjectAction = Class(name="BPMNProfile::SendObjectAction")
BPMNProfile_TerminateEventDefinition = Class(name="BPMNProfile::TerminateEventDefinition")
BPMNProfile_ImplicitThrowEvent = Class(name="BPMNProfile::ImplicitThrowEvent")
BPMNProfile_CancelEventDefinition = Class(name="BPMNProfile::CancelEventDefinition")
BPMNProfile_TextAnnotation = Class(name="BPMNProfile::TextAnnotation")
BPMNProfile_Category = Class(name="BPMNProfile::Category")
BPMNProfile_Enumeration = Class(name="BPMNProfile::Enumeration")
BPMNProfile_DataStoreReference = Class(name="BPMNProfile::DataStoreReference")
BPMNProfile_UserTask = Class(name="BPMNProfile::UserTask")
Task = Class(name="Task")
BPMNProfile_DataObjectReference = Class(name="BPMNProfile::DataObjectReference")
BPMNProfile_DataObject = Class(name="BPMNProfile::DataObject")
BPMNProfile_DataStore = Class(name="BPMNProfile::DataStore")
BPMNProfile_GlobalManualTask = Class(name="BPMNProfile::GlobalManualTask")
BPMNProfile_ManualTask = Class(name="BPMNProfile::ManualTask")
BPMNProfile_PotentialOwner = Class(name="BPMNProfile::PotentialOwner")
HumanPerformer = Class(name="HumanPerformer")
BPMNProfile_SubConversation = Class(name="BPMNProfile::SubConversation")
ConversationNode = Class(name="ConversationNode")
BPMNProfile_OpaqueAction = Class(name="BPMNProfile::OpaqueAction")
BPMNProfile_Rendering = Class(name="BPMNProfile::Rendering")
BPMNProfile_Task = Class(name="BPMNProfile::Task")
BPMNActivity = Class(name="BPMNActivity")
BPMNProfile_Image = Class(name="BPMNProfile::Image")
BPMNProfile_HumanPerformer = Class(name="BPMNProfile::HumanPerformer")
Performer = Class(name="Performer")
BPMNProfile_Performer = Class(name="BPMNProfile::Performer")
ResourceRole = Class(name="ResourceRole")
BPMNProfile_GlobalUserTask = Class(name="BPMNProfile::GlobalUserTask")
BPMNProfile_Conversation = Class(name="BPMNProfile::Conversation")
BPMNProfile_SubProcess = Class(name="BPMNProfile::SubProcess")
BPMNProfile_GlobalConversation = Class(name="BPMNProfile::GlobalConversation")
BPMNCollaboration = Class(name="BPMNCollaboration")
BPMNProfile_CallConversation = Class(name="BPMNProfile::CallConversation")
BPMNProfile_CollaborationUse = Class(name="BPMNProfile::CollaborationUse")
BPMNProfile_ComplexBehaviorDefinition = Class(name="BPMNProfile::ComplexBehaviorDefinition")
BPMNProfile_CallActivity = Class(name="BPMNProfile::CallActivity")
BPMNProfile_CallBehaviorAction = Class(name="BPMNProfile::CallBehaviorAction")
BPMNProfile_BusinessRuleTask = Class(name="BPMNProfile::BusinessRuleTask")
BPMNProfile_SendTask = Class(name="BPMNProfile::SendTask")
BPMNProfile_AdHocSubProcess = Class(name="BPMNProfile::AdHocSubProcess")
SubProcess = Class(name="SubProcess")
BPMNProfile_ScriptTask = Class(name="BPMNProfile::ScriptTask")
BPMNProfile_ServiceTask = Class(name="BPMNProfile::ServiceTask")
BPMNProfile_Transaction = Class(name="BPMNProfile::Transaction")
BPMNProfile_StandardLoopCharacteristics = Class(name="BPMNProfile::StandardLoopCharacteristics")
LoopCharacteristics = Class(name="LoopCharacteristics")
BPMNProfile_LoopNode = Class(name="BPMNProfile::LoopNode")
BPMNProfile_ReceiveTask = Class(name="BPMNProfile::ReceiveTask")
BPMNProfile_MultiInstanceLoopCharacteristics = Class(name="BPMNProfile::MultiInstanceLoopCharacteristics")
BPMNProfile_ExpansionRegion = Class(name="BPMNProfile::ExpansionRegion")

# BPMNProfile_JoinNode class attributes and methods

# BPMNProfile_ForkNode class attributes and methods

# BPMNProfile_Comment class attributes and methods

# BPMNProfile_Gateway class attributes and methods

# FlowNode class attributes and methods

# BPMNProfile_ControlNode class attributes and methods

# BPMNProfile_ActivityGroup class attributes and methods

# BPMNProfile_FlowNode class attributes and methods

# FlowElement class attributes and methods

# BPMNProfile_ActivityNode class attributes and methods

# BPMNProfile_FlowElement class attributes and methods

# BaseElement class attributes and methods

# BPMNProfile_Auditing class attributes and methods

# BPMNProfile_Monitoring class attributes and methods

# BPMNProfile_CategoryValue class attributes and methods

# BPMNProfile_FlowElementsContainer class attributes and methods

# BPMNProfile_BaseElement class attributes and methods
BPMNProfile_BaseElement_id: Property = Property(name="id", type=StringType)
BPMNProfile_BaseElement.attributes={BPMNProfile_BaseElement_id}

# BPMNProfile_ExtensionAttributeValue class attributes and methods

# BPMNProfile_Element class attributes and methods

# BPMNProfile_Documentation class attributes and methods
BPMNProfile_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
BPMNProfile_Documentation_text: Property = Property(name="text", type=StringType)
BPMNProfile_Documentation.attributes={BPMNProfile_Documentation_text, BPMNProfile_Documentation_textFormat}

# BPMNProfile_InclusiveGateway class attributes and methods
BPMNProfile_InclusiveGateway_m_inclusiveGatewaydefault: Method = Method(name="inclusiveGatewaydefault", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InclusiveGateway.methods={BPMNProfile_InclusiveGateway_m_inclusiveGatewaydefault}

# BPMNProfile_ExtensionDefinition class attributes and methods

# NonExclusiveGateway class attributes and methods

# BPMNProfile_BPMNAssociation class attributes and methods
BPMNProfile_BPMNAssociation_associationDirection: Property = Property(name="associationDirection", type=StringType)
BPMNProfile_BPMNAssociation_m_AssociationEnd: Method = Method(name="AssociationEnd", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNAssociation.attributes={BPMNProfile_BPMNAssociation_associationDirection}
BPMNProfile_BPMNAssociation.methods={BPMNProfile_BPMNAssociation_m_AssociationEnd}

# BPMNProfile_Slot class attributes and methods

# BPMNProfile_SequenceFlow class attributes and methods
BPMNProfile_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=StringType)
BPMNProfile_SequenceFlow_m_SequenceFlowconditionExpression: Method = Method(name="SequenceFlowconditionExpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SequenceFlow_m_SequenceFlowsourceRef: Method = Method(name="SequenceFlowsourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SequenceFlow_m_SequenceFlowtargetRef: Method = Method(name="SequenceFlowtargetRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SequenceFlow.attributes={BPMNProfile_SequenceFlow_isImmediate}
BPMNProfile_SequenceFlow.methods={BPMNProfile_SequenceFlow_m_SequenceFlowtargetRef, BPMNProfile_SequenceFlow_m_SequenceFlowconditionExpression, BPMNProfile_SequenceFlow_m_SequenceFlowsourceRef}

# BPMNProfile_ExtensionAttributeDefinition class attributes and methods
BPMNProfile_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
BPMNProfile_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=StringType)
BPMNProfile_ExtensionAttributeDefinition.attributes={BPMNProfile_ExtensionAttributeDefinition_type, BPMNProfile_ExtensionAttributeDefinition_isReference}

# BPMNProfile_Property class attributes and methods

# BPMNProfile_NonExclusiveGateway class attributes and methods

# Gateway class attributes and methods

# BPMNProfile_Stereotype class attributes and methods

# BPMNArtifact class attributes and methods

# BPMNProfile_Dependency class attributes and methods

# BPMNProfile_BPMNArtifact class attributes and methods

# BPMNProfile_Class class attributes and methods

# BPMNProfile_EnumerationLiteral class attributes and methods

# BPMNProfile_LaneSet class attributes and methods
BPMNProfile_LaneSet_m_LaneSetlanes: Method = Method(name="LaneSetlanes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSetparentLane: Method = Method(name="LaneSetparentLane", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSetflowElementsContainer: Method = Method(name="LaneSetflowElementsContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSet: Method = Method(name="LaneSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_LaneSet.methods={BPMNProfile_LaneSet_m_LaneSet, BPMNProfile_LaneSet_m_LaneSetflowElementsContainer, BPMNProfile_LaneSet_m_LaneSetparentLane, BPMNProfile_LaneSet_m_LaneSetlanes}

# BPMNProfile_ActivityPartition class attributes and methods

# BPMNProfile_Lane class attributes and methods
BPMNProfile_Lane_m_LaneflowNodeRefs: Method = Method(name="LaneflowNodeRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Lane_m_LanelaneSet: Method = Method(name="LanelaneSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Lane_m_LanechildLaneSet: Method = Method(name="LanechildLaneSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Lane_m_LanepartitionElementRef: Method = Method(name="LanepartitionElementRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Lane.methods={BPMNProfile_Lane_m_LanelaneSet, BPMNProfile_Lane_m_LanechildLaneSet, BPMNProfile_Lane_m_LaneflowNodeRefs, BPMNProfile_Lane_m_LanepartitionElementRef}

# BPMNProfile_OpaqueExpression class attributes and methods

# BPMNProfile_EventBasedGateway class attributes and methods
BPMNProfile_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=StringType)
BPMNProfile_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
BPMNProfile_EventBasedGateway.attributes={BPMNProfile_EventBasedGateway_instantiate, BPMNProfile_EventBasedGateway_eventGatewayType}

# BPMNProfile_ControlFlow class attributes and methods

# BPMNProfile_BPMNExpression class attributes and methods

# BPMNProfile_DecisionNode class attributes and methods

# BPMNProfile_MergeNode class attributes and methods

# BPMNProfile_RootElement class attributes and methods

# BPMNProfile_PackageableElement class attributes and methods

# BPMNProfile_StructuredActivityNode class attributes and methods

# BPMNProfile_InterruptibleActivityRegion class attributes and methods

# BPMNProfile_ParallelGateway class attributes and methods

# BPMNProfile_ComplexGateway class attributes and methods
BPMNProfile_ComplexGateway_m_complexGatewaydefault: Method = Method(name="complexGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ComplexGateway_m_complexGatewayactivationCondition: Method = Method(name="complexGatewayactivationCondition", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ComplexGateway_m_complexGatewayjoinSpec: Method = Method(name="complexGatewayjoinSpec", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ComplexGateway.methods={BPMNProfile_ComplexGateway_m_complexGatewayjoinSpec, BPMNProfile_ComplexGateway_m_complexGatewaydefault, BPMNProfile_ComplexGateway_m_complexGatewayactivationCondition}

# BPMNProfile_ExclusiveGateway class attributes and methods
BPMNProfile_ExclusiveGateway_m_exclusiveGatewaydefault: Method = Method(name="exclusiveGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ExclusiveGateway.methods={BPMNProfile_ExclusiveGateway_m_exclusiveGatewaydefault}

# BPMNProfile_Constraint class attributes and methods

# BPMNProfile_Definitions class attributes and methods
BPMNProfile_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
BPMNProfile_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
BPMNProfile_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
BPMNProfile_Definitions_exporter: Property = Property(name="exporter", type=StringType)
BPMNProfile_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
BPMNProfile_Definitions.attributes={BPMNProfile_Definitions_exporter, BPMNProfile_Definitions_exporterVersion, BPMNProfile_Definitions_targetNamespace, BPMNProfile_Definitions_typeLanguage, BPMNProfile_Definitions_expressionLanguage}

# BPMNProfile_Package class attributes and methods

# BPMNProfile_BPMNExtension class attributes and methods
BPMNProfile_BPMNExtension_mustUnderstand: Property = Property(name="mustUnderstand", type=StringType)
BPMNProfile_BPMNExtension.attributes={BPMNProfile_BPMNExtension_mustUnderstand}

# BPMNProfile_Import class attributes and methods
BPMNProfile_Import_importType: Property = Property(name="importType", type=StringType)
BPMNProfile_Import_location: Property = Property(name="location", type=StringType)
BPMNProfile_Import_namespace: Property = Property(name="namespace", type=StringType)
BPMNProfile_Import.attributes={BPMNProfile_Import_namespace, BPMNProfile_Import_importType, BPMNProfile_Import_location}

# BPMNProfile_BPMNRelationship class attributes and methods
BPMNProfile_BPMNRelationship_type: Property = Property(name="type", type=StringType)
BPMNProfile_BPMNRelationship_direction: Property = Property(name="direction", type=StringType)
BPMNProfile_BPMNRelationship.attributes={BPMNProfile_BPMNRelationship_type, BPMNProfile_BPMNRelationship_direction}

# BPMNProfile_PackageImport class attributes and methods

# BPMNProfile_BPMNCollaboration class attributes and methods
BPMNProfile_BPMNCollaboration_isClosed: Property = Property(name="isClosed", type=StringType)
BPMNProfile_BPMNCollaboration_m_Collaborationparticipants: Method = Method(name="Collaborationparticipants", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNCollaboration.attributes={BPMNProfile_BPMNCollaboration_isClosed}
BPMNProfile_BPMNCollaboration.methods={BPMNProfile_BPMNCollaboration_m_Collaborationparticipants}

# BPMNProfile_Activity class attributes and methods

# BPMNProfile_CorrelationSubscription class attributes and methods

# BPMNProfile_BPMNProcess class attributes and methods
BPMNProfile_BPMNProcess_isExecutable: Property = Property(name="isExecutable", type=StringType)
BPMNProfile_BPMNProcess_processType: Property = Property(name="processType", type=StringType)
BPMNProfile_BPMNProcess_isClosed: Property = Property(name="isClosed", type=StringType)
BPMNProfile_BPMNProcess_m_ProcesssupportedInterfaceRefs: Method = Method(name="ProcesssupportedInterfaceRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_Processsupports: Method = Method(name="Processsupports", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_Processproperties: Method = Method(name="Processproperties", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_ProcesslaneSets: Method = Method(name="ProcesslaneSets", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_ProcessflowElements: Method = Method(name="ProcessflowElements", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProcess.attributes={BPMNProfile_BPMNProcess_isExecutable, BPMNProfile_BPMNProcess_processType, BPMNProfile_BPMNProcess_isClosed}
BPMNProfile_BPMNProcess.methods={BPMNProfile_BPMNProcess_m_ProcessflowElements, BPMNProfile_BPMNProcess_m_ProcesssupportedInterfaceRefs, BPMNProfile_BPMNProcess_m_ProcesslaneSets, BPMNProfile_BPMNProcess_m_Processproperties, BPMNProfile_BPMNProcess_m_Processsupports}

# CallableElement class attributes and methods

# FlowElementsContainer class attributes and methods

# BPMNProfile_DataInput class attributes and methods
BPMNProfile_DataInput_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataInput_m_DataInputAssociation: Method = Method(name="DataInputAssociation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInput_m_DataInputnotation: Method = Method(name="DataInputnotation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataInput_m_DataInputitemSubjectRef: Method = Method(name="DataInputitemSubjectRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInput.attributes={BPMNProfile_DataInput_isCollection}
BPMNProfile_DataInput.methods={BPMNProfile_DataInput_m_DataInputAssociation, BPMNProfile_DataInput_m_DataInputnotation, BPMNProfile_DataInput_m_DataInputitemSubjectRef}

# BPMNProfile_DataOutput class attributes and methods
BPMNProfile_DataOutput_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataOutput_m_DataOutputnotation: Method = Method(name="DataOutputnotation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataOutput_m_DataOutputitemSubjectRef: Method = Method(name="DataOutputitemSubjectRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataOutput.attributes={BPMNProfile_DataOutput_isCollection}
BPMNProfile_DataOutput.methods={BPMNProfile_DataOutput_m_DataOutputitemSubjectRef, BPMNProfile_DataOutput_m_DataOutputnotation}

# BPMNProfile_InputSet class attributes and methods
BPMNProfile_InputSet_m_InputSetdataInputRefs: Method = Method(name="InputSetdataInputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InputSet_m_InputSetoptionalInputRefs: Method = Method(name="InputSetoptionalInputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InputSet_m_InputSetwhileExecutingInputRefs: Method = Method(name="InputSetwhileExecutingInputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_InputSet.methods={BPMNProfile_InputSet_m_InputSetdataInputRefs, BPMNProfile_InputSet_m_InputSetoptionalInputRefs, BPMNProfile_InputSet_m_InputSetwhileExecutingInputRefs}

# BPMNProfile_OutputSet class attributes and methods
BPMNProfile_OutputSet_m_OutputSetdataOutputRefs: Method = Method(name="OutputSetdataOutputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_OutputSet_m_OutputSetoptionalOutputRefs: Method = Method(name="OutputSetoptionalOutputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_OutputSet_m_OutputSetwhileExecutingOutputRefs: Method = Method(name="OutputSetwhileExecutingOutputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_OutputSet.methods={BPMNProfile_OutputSet_m_OutputSetdataOutputRefs, BPMNProfile_OutputSet_m_OutputSetwhileExecutingOutputRefs, BPMNProfile_OutputSet_m_OutputSetoptionalOutputRefs}

# BPMNProfile_BPMNProperty class attributes and methods
BPMNProfile_BPMNProperty_m_Propertynotation: Method = Method(name="Propertynotation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProperty_m_BPMNPropertyapply: Method = Method(name="BPMNPropertyapply", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProperty.methods={BPMNProfile_BPMNProperty_m_BPMNPropertyapply, BPMNProfile_BPMNProperty_m_Propertynotation}

# BPMNProfile_ResourceRole class attributes and methods
BPMNProfile_ResourceRole_m_ResourceRoleowner: Method = Method(name="ResourceRoleowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleresourceRef: Method = Method(name="ResourceRoleresourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleisRequired: Method = Method(name="ResourceRoleisRequired", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleprocess: Method = Method(name="ResourceRoleprocess", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleresourceParameterBindings: Method = Method(name="ResourceRoleresourceParameterBindings", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceRole.methods={BPMNProfile_ResourceRole_m_ResourceRoleisRequired, BPMNProfile_ResourceRole_m_ResourceRoleresourceParameterBindings, BPMNProfile_ResourceRole_m_ResourceRoleresourceRef, BPMNProfile_ResourceRole_m_ResourceRoleowner, BPMNProfile_ResourceRole_m_ResourceRoleprocess}

# BPMNProfile_CallableElement class attributes and methods
BPMNProfile_CallableElement_m_CallableEelementsupportedInterfaceRefs: Method = Method(name="CallableEelementsupportedInterfaceRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallableElement_m_CallableElementresources: Method = Method(name="CallableElementresources", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallableElement.methods={BPMNProfile_CallableElement_m_CallableEelementsupportedInterfaceRefs, BPMNProfile_CallableElement_m_CallableElementresources}

# RootElement class attributes and methods

# BPMNProfile_Behavior class attributes and methods

# BPMNProfile_InputOutputSpecification class attributes and methods

# BPMNProfile_BPMNInterface class attributes and methods
BPMNProfile_BPMNInterface_m_Interfaceoperationmultiplicity: Method = Method(name="Interfaceoperationmultiplicity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_InterfaceownedOperation: Method = Method(name="InterfaceownedOperation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_BPMNInterfacecallableElements: Method = Method(name="BPMNInterfacecallableElements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_BPMNInterfaceoperations: Method = Method(name="BPMNInterfaceoperations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNInterface.methods={BPMNProfile_BPMNInterface_m_BPMNInterfacecallableElements, BPMNProfile_BPMNInterface_m_BPMNInterfaceoperations, BPMNProfile_BPMNInterface_m_Interfaceoperationmultiplicity, BPMNProfile_BPMNInterface_m_InterfaceownedOperation}

# BPMNProfile_InputOutputBinding class attributes and methods

# BPMNProfile_Action class attributes and methods

# ItemAwareElement class attributes and methods

# BPMNProfile_InputPin class attributes and methods

# BPMNProfile_Parameter class attributes and methods

# BPMNProfile_ActivityParameterNode class attributes and methods

# BPMNProfile_ItemDefinition class attributes and methods
BPMNProfile_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
BPMNProfile_ItemDefinition_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_ItemDefinition_m_ItemDefinitionstructureRef: Method = Method(name="ItemDefinitionstructureRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ItemDefinition.attributes={BPMNProfile_ItemDefinition_isCollection, BPMNProfile_ItemDefinition_itemKind}
BPMNProfile_ItemDefinition.methods={BPMNProfile_ItemDefinition_m_ItemDefinitionstructureRef}

# BPMNProfile_State class attributes and methods

# BPMNProfile_ItemAwareElement class attributes and methods
BPMNProfile_ItemAwareElement_m_ItemAwareElementdataState: Method = Method(name="ItemAwareElementdataState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ItemAwareElement.methods={BPMNProfile_ItemAwareElement_m_ItemAwareElementdataState}

# BPMNProfile_DataState class attributes and methods

# BPMNProfile_TypedElement class attributes and methods

# BPMNProfile_ParameterSet class attributes and methods

# BPMNProfile_OutputPin class attributes and methods

# BPMNProfile_Operation class attributes and methods

# BPMNProfile_Interface class attributes and methods

# BPMNProfile_BPMNOperation class attributes and methods
BPMNProfile_BPMNOperation_m_BPMNOperationerrorRefs: Method = Method(name="BPMNOperationerrorRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationowner: Method = Method(name="BPMNOperationowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationinMessageRef: Method = Method(name="BPMNOperationinMessageRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationoutMessageRef: Method = Method(name="BPMNOperationoutMessageRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation.methods={BPMNProfile_BPMNOperation_m_BPMNOperationowner, BPMNProfile_BPMNOperation_m_BPMNOperationoutMessageRef, BPMNProfile_BPMNOperation_m_BPMNOperationerrorRefs, BPMNProfile_BPMNOperation_m_BPMNOperationinMessageRef}

# BPMNProfile_ParticipantAssociation class attributes and methods
BPMNProfile_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef: Method = Method(name="ParticipantAssociationinnerParticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef: Method = Method(name="ParticipantAssociationouterParticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ParticipantAssociation.methods={BPMNProfile_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef, BPMNProfile_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef}

# BPMNProfile_BPMNMessage class attributes and methods
BPMNProfile_BPMNMessage_m_MessageitemRef: Method = Method(name="MessageitemRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNMessage.methods={BPMNProfile_BPMNMessage_m_MessageitemRef}

# BPMNProfile_Error class attributes and methods
BPMNProfile_Error_errorCode: Property = Property(name="errorCode", type=StringType)
BPMNProfile_Error.attributes={BPMNProfile_Error_errorCode}

# ItemDefinition class attributes and methods

# BPMNProfile_ConversationLink class attributes and methods

# BPMNProfile_MessageFlowAssociation class attributes and methods
BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef: Method = Method(name="MessageFlowAssociationinnerMessageFlowRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef: Method = Method(name="MessageFlowAssociationouterMessageFlowRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlowAssociation.methods={BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef, BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef}

# BPMNProfile_MessageFlow class attributes and methods
BPMNProfile_MessageFlow_m_MessageFlowtargetRef: Method = Method(name="MessageFlowtargetRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlow_m_MessageFlowmessageRef: Method = Method(name="MessageFlowmessageRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlow_m_MessageFlowsourceRef: Method = Method(name="MessageFlowsourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_MessageFlow.methods={BPMNProfile_MessageFlow_m_MessageFlowmessageRef, BPMNProfile_MessageFlow_m_MessageFlowtargetRef, BPMNProfile_MessageFlow_m_MessageFlowsourceRef}

# BPMNProfile_Collaboration class attributes and methods

# BPMNProfile_ConversationNode class attributes and methods
BPMNProfile_ConversationNode_m_ConversationNodeparticipantRefs: Method = Method(name="ConversationNodeparticipantRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ConversationNode.methods={BPMNProfile_ConversationNode_m_ConversationNodeparticipantRefs}

# BPMNProfile_CorrelationKey class attributes and methods

# BPMNProfile_Participant class attributes and methods
BPMNProfile_Participant_m_Participantownership: Method = Method(name="Participantownership", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_Participanttype: Method = Method(name="Participanttype", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantmultiplicityMinimum: Method = Method(name="ParticipantmultiplicityMinimum", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_Participantrealizationsupplier: Method = Method(name="Participantrealizationsupplier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantprocessRef: Method = Method(name="ParticipantprocessRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantmultiplicityMaximum: Method = Method(name="ParticipantmultiplicityMaximum", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_participantpartnerEntityRef: Method = Method(name="participantpartnerEntityRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_participantpartnerRoleRef: Method = Method(name="participantpartnerRoleRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantinterfaceRefs: Method = Method(name="ParticipantinterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant.methods={BPMNProfile_Participant_m_ParticipantmultiplicityMinimum, BPMNProfile_Participant_m_Participanttype, BPMNProfile_Participant_m_Participantownership, BPMNProfile_Participant_m_Participantrealizationsupplier, BPMNProfile_Participant_m_ParticipantmultiplicityMaximum, BPMNProfile_Participant_m_participantpartnerEntityRef, BPMNProfile_Participant_m_ParticipantprocessRef, BPMNProfile_Participant_m_ParticipantinterfaceRefs, BPMNProfile_Participant_m_participantpartnerRoleRef}

# BPMNProfile_ParticipantMultiplicity class attributes and methods
BPMNProfile_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=StringType)
BPMNProfile_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=StringType)
BPMNProfile_ParticipantMultiplicity.attributes={BPMNProfile_ParticipantMultiplicity_maximum, BPMNProfile_ParticipantMultiplicity_minimum}

# BPMNProfile_InstanceSpecification class attributes and methods

# BPMNProfile_PartnerEntity class attributes and methods
BPMNProfile_PartnerEntity_m_PartnerEntityparticipantRef: Method = Method(name="PartnerEntityparticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_PartnerEntity.methods={BPMNProfile_PartnerEntity_m_PartnerEntityparticipantRef}

# BPMNProfile_PartnerRole class attributes and methods
BPMNProfile_PartnerRole_m_PartnerRoleparticipantRef: Method = Method(name="PartnerRoleparticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_PartnerRole.methods={BPMNProfile_PartnerRole_m_PartnerRoleparticipantRef}

# BPMNProfile_InteractionNode class attributes and methods

# BPMNProfile_MultiplicityElement class attributes and methods

# BPMNProfile_CorrelationPropertyRetrievalExpression class attributes and methods

# BPMNProfile_InformationFlow class attributes and methods

# InteractionNode class attributes and methods

# BPMNProfile_CorrelationProperty class attributes and methods

# BPMNProfile_DataStoreNode class attributes and methods

# BPMNProfile_FormalExpression class attributes and methods
BPMNProfile_FormalExpression_m_FormalExpressionevaluatesToTypeRef: Method = Method(name="FormalExpressionevaluatesToTypeRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_FormalExpression.methods={BPMNProfile_FormalExpression_m_FormalExpressionevaluatesToTypeRef}

# BPMNExpression class attributes and methods

# BPMNProfile_CorrelationPropertyBinding class attributes and methods

# BPMNProfile_ResourceAssignmentExpression class attributes and methods
BPMNProfile_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression: Method = Method(name="ResourceAssignmentExpressionexpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceAssignmentExpression.methods={BPMNProfile_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression}

# BPMNProfile_Resource class attributes and methods
BPMNProfile_Resource_m_ResourceresourceParameters: Method = Method(name="ResourceresourceParameters", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Resource.methods={BPMNProfile_Resource_m_ResourceresourceParameters}

# BPMNProfile_ResourceParameterBinding class attributes and methods
BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingexpression: Method = Method(name="ResourceParameterBindingexpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingparameterRef: Method = Method(name="ResourceParameterBindingparameterRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameterBinding.methods={BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingparameterRef, BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingexpression}

# BPMNProfile_ResourceParameter class attributes and methods
BPMNProfile_ResourceParameter_isRequired: Property = Property(name="isRequired", type=StringType)
BPMNProfile_ResourceParameter_m_ResourceParameterowner: Method = Method(name="ResourceParameterowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameter_m_ResourceParametertype: Method = Method(name="ResourceParametertype", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceParameter_m_ResourceParameterisRequired: Method = Method(name="ResourceParameterisRequired", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameter.attributes={BPMNProfile_ResourceParameter_isRequired}
BPMNProfile_ResourceParameter.methods={BPMNProfile_ResourceParameter_m_ResourceParametertype, BPMNProfile_ResourceParameter_m_ResourceParameterowner, BPMNProfile_ResourceParameter_m_ResourceParameterisRequired}

# BPMNProfile_GlobalBusinessRuleTask class attributes and methods
BPMNProfile_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation: Method = Method(name="GlobalBusinessRuleTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalBusinessRuleTask.attributes={BPMNProfile_GlobalBusinessRuleTask_implementation}
BPMNProfile_GlobalBusinessRuleTask.methods={BPMNProfile_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation}

# BPMNProfile_GlobalScriptTask class attributes and methods
BPMNProfile_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
BPMNProfile_GlobalScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscriptFormat: Method = Method(name="GlobalScriptTaskscriptFormat", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscript: Method = Method(name="GlobalScriptTaskscript", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_GlobalScriptTask.attributes={BPMNProfile_GlobalScriptTask_scriptFormat, BPMNProfile_GlobalScriptTask_script}
BPMNProfile_GlobalScriptTask.methods={BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscript, BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscriptFormat}

# GlobalTask class attributes and methods

# BPMNProfile_GlobalTask class attributes and methods
BPMNProfile_GlobalTask_m_GlobalTasksupportedInterfaceRefs: Method = Method(name="GlobalTasksupportedInterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_GlobalTask.methods={BPMNProfile_GlobalTask_m_GlobalTasksupportedInterfaceRefs}

# BPMNProfile_OpaqueBehavior class attributes and methods

# BPMNProfile_CompensateEventDefinition class attributes and methods
BPMNProfile_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=StringType)
BPMNProfile_CompensateEventDefinition.attributes={BPMNProfile_CompensateEventDefinition_waitForCompletion}

# EventDefinition class attributes and methods

# BPMNProfile_BPMNActivity class attributes and methods
BPMNProfile_BPMNActivity_isForCompensation: Property = Property(name="isForCompensation", type=StringType)
BPMNProfile_BPMNActivity_startQuantity: Property = Property(name="startQuantity", type=StringType)
BPMNProfile_BPMNActivity_completionQuantity: Property = Property(name="completionQuantity", type=StringType)
BPMNProfile_BPMNActivity_m_BPMNActivityresources: Method = Method(name="BPMNActivityresources", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivitycontainer: Method = Method(name="BPMNActivitycontainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivityproperties: Method = Method(name="BPMNActivityproperties", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivitydefault: Method = Method(name="BPMNActivitydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivityboundaryEventsRefs: Method = Method(name="BPMNActivityboundaryEventsRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivityloopCharacteristics: Method = Method(name="BPMNActivityloopCharacteristics", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity.attributes={BPMNProfile_BPMNActivity_isForCompensation, BPMNProfile_BPMNActivity_startQuantity, BPMNProfile_BPMNActivity_completionQuantity}
BPMNProfile_BPMNActivity.methods={BPMNProfile_BPMNActivity_m_BPMNActivitycontainer, BPMNProfile_BPMNActivity_m_BPMNActivityproperties, BPMNProfile_BPMNActivity_m_BPMNActivityboundaryEventsRefs, BPMNProfile_BPMNActivity_m_BPMNActivityloopCharacteristics, BPMNProfile_BPMNActivity_m_BPMNActivitydefault, BPMNProfile_BPMNActivity_m_BPMNActivityresources}

# BPMNProfile_CallEvent class attributes and methods

# BPMNProfile_EventDefinition class attributes and methods

# BPMNProfile_Event class attributes and methods

# BPMNProfile_AcceptEventAction class attributes and methods

# BPMNProfile_InitialNode class attributes and methods

# BPMNProfile_BPMNEvent class attributes and methods

# BPMNProfile_BoundaryEvent class attributes and methods
BPMNProfile_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=StringType)
BPMNProfile_BoundaryEvent_m_boundaryEventattachedToRef: Method = Method(name="boundaryEventattachedToRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BoundaryEvent.attributes={BPMNProfile_BoundaryEvent_cancelActivity}
BPMNProfile_BoundaryEvent.methods={BPMNProfile_BoundaryEvent_m_boundaryEventattachedToRef}

# BPMNProfile_DataInputAssociation class attributes and methods
BPMNProfile_DataInputAssociation_m_dataInputAssociationsource: Method = Method(name="dataInputAssociationsource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInputAssociation_m_dataInputAssociationtarget: Method = Method(name="dataInputAssociationtarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataInputAssociation.methods={BPMNProfile_DataInputAssociation_m_dataInputAssociationtarget, BPMNProfile_DataInputAssociation_m_dataInputAssociationsource}

# BPMNProfile_DataOutputAssociation class attributes and methods
BPMNProfile_DataOutputAssociation_m_dataOutputAssociationsource: Method = Method(name="dataOutputAssociationsource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataOutputAssociation_m_dataOutputAssociationtarget: Method = Method(name="dataOutputAssociationtarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataOutputAssociation.methods={BPMNProfile_DataOutputAssociation_m_dataOutputAssociationtarget, BPMNProfile_DataOutputAssociation_m_dataOutputAssociationsource}

# BPMNProfile_LoopCharacteristics class attributes and methods

# CatchEvent class attributes and methods

# BPMNProfile_CatchEvent class attributes and methods
BPMNProfile_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=StringType)
BPMNProfile_CatchEvent_m_catchEventeventDefinitionsRefs: Method = Method(name="catchEventeventDefinitionsRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_CatchEvent.attributes={BPMNProfile_CatchEvent_parallelMultiple}
BPMNProfile_CatchEvent.methods={BPMNProfile_CatchEvent_m_catchEventeventDefinitionsRefs}

# BPMNEvent class attributes and methods

# DataAssociation class attributes and methods

# BPMNProfile_DataAssociation class attributes and methods
BPMNProfile_DataAssociation_m_DataAssociationsource: Method = Method(name="DataAssociationsource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataAssociation_m_DataAssociationtransformation: Method = Method(name="DataAssociationtransformation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataAssociation_m_DataAssociationtarget: Method = Method(name="DataAssociationtarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataAssociation.methods={BPMNProfile_DataAssociation_m_DataAssociationsource, BPMNProfile_DataAssociation_m_DataAssociationtransformation, BPMNProfile_DataAssociation_m_DataAssociationtarget}

# BPMNProfile_ObjectFlow class attributes and methods

# BPMNProfile_Assignment class attributes and methods

# BPMNProfile_EscalationEventDefinition class attributes and methods

# BPMNProfile_Escalation class attributes and methods
BPMNProfile_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
BPMNProfile_Escalation_m_EscalationstructureRef: Method = Method(name="EscalationstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Escalation.attributes={BPMNProfile_Escalation_escalationCode}
BPMNProfile_Escalation.methods={BPMNProfile_Escalation_m_EscalationstructureRef}

# BPMNProfile_EndEvent class attributes and methods

# ThrowEvent class attributes and methods

# BPMNProfile_FinalNode class attributes and methods

# BPMNProfile_ThrowEvent class attributes and methods
BPMNProfile_ThrowEvent_m_ThrowEventeventDefinitionRefs: Method = Method(name="ThrowEventeventDefinitionRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ThrowEvent.methods={BPMNProfile_ThrowEvent_m_ThrowEventeventDefinitionRefs}

# BPMNProfile_TimerEventDefinition class attributes and methods

# BPMNProfile_ChangeEvent class attributes and methods

# BPMNProfile_SignalEventDefinition class attributes and methods

# BPMNProfile_BPMNSignal class attributes and methods
BPMNProfile_BPMNSignal_m_BPMNSignalstructureRef: Method = Method(name="BPMNSignalstructureRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNSignal.methods={BPMNProfile_BPMNSignal_m_BPMNSignalstructureRef}

# BPMNProfile_LinkEventDefinition class attributes and methods

# BPMNProfile_CallOperationAction class attributes and methods

# BPMNProfile_FlowFinalNode class attributes and methods

# BPMNProfile_MessageEventDefinition class attributes and methods

# BPMNProfile_StartEvent class attributes and methods
BPMNProfile_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=StringType)
BPMNProfile_StartEvent.attributes={BPMNProfile_StartEvent_isInterrupting}

# BPMNProfile_ConditionalEventDefinition class attributes and methods
BPMNProfile_ConditionalEventDefinition_m_conditionalEventDefinitioncondition: Method = Method(name="conditionalEventDefinitioncondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ConditionalEventDefinition.methods={BPMNProfile_ConditionalEventDefinition_m_conditionalEventDefinitioncondition}

# BPMNProfile_Group class attributes and methods

# BPMNProfile_ErrorEventDefinition class attributes and methods

# BPMNProfile_IntermediateCatchEvent class attributes and methods

# BPMNProfile_IntermediateThrowEvent class attributes and methods

# BPMNProfile_SendObjectAction class attributes and methods

# BPMNProfile_TerminateEventDefinition class attributes and methods

# BPMNProfile_ImplicitThrowEvent class attributes and methods

# BPMNProfile_CancelEventDefinition class attributes and methods

# BPMNProfile_TextAnnotation class attributes and methods
BPMNProfile_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
BPMNProfile_TextAnnotation_text: Property = Property(name="text", type=StringType)
BPMNProfile_TextAnnotation.attributes={BPMNProfile_TextAnnotation_text, BPMNProfile_TextAnnotation_textFormat}

# BPMNProfile_Category class attributes and methods

# BPMNProfile_Enumeration class attributes and methods

# BPMNProfile_DataStoreReference class attributes and methods

# BPMNProfile_UserTask class attributes and methods
BPMNProfile_UserTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_UserTask_m_UserTaskimplementation: Method = Method(name="UserTaskimplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_UserTask_m_UserTaskrenderings: Method = Method(name="UserTaskrenderings", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_UserTask.attributes={BPMNProfile_UserTask_implementation}
BPMNProfile_UserTask.methods={BPMNProfile_UserTask_m_UserTaskrenderings, BPMNProfile_UserTask_m_UserTaskimplementation}

# Task class attributes and methods

# BPMNProfile_DataObjectReference class attributes and methods
BPMNProfile_DataObjectReference_m_DataObjectRefsourcetarget: Method = Method(name="DataObjectRefsourcetarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataObjectReference_m_DataObjectRefdataState: Method = Method(name="DataObjectRefdataState", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataObjectReference.methods={BPMNProfile_DataObjectReference_m_DataObjectRefdataState, BPMNProfile_DataObjectReference_m_DataObjectRefsourcetarget}

# BPMNProfile_DataObject class attributes and methods
BPMNProfile_DataObject_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataObject_m_DataObjectdataState: Method = Method(name="DataObjectdataState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataObject.attributes={BPMNProfile_DataObject_isCollection}
BPMNProfile_DataObject.methods={BPMNProfile_DataObject_m_DataObjectdataState}

# BPMNProfile_DataStore class attributes and methods
BPMNProfile_DataStore_capacity: Property = Property(name="capacity", type=StringType)
BPMNProfile_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=StringType)
BPMNProfile_DataStore.attributes={BPMNProfile_DataStore_isUnlimited, BPMNProfile_DataStore_capacity}

# BPMNProfile_GlobalManualTask class attributes and methods

# BPMNProfile_ManualTask class attributes and methods

# BPMNProfile_PotentialOwner class attributes and methods

# HumanPerformer class attributes and methods

# BPMNProfile_SubConversation class attributes and methods
BPMNProfile_SubConversation_m_SubConversationconnectedelements: Method = Method(name="SubConversationconnectedelements", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SubConversation.methods={BPMNProfile_SubConversation_m_SubConversationconnectedelements}

# ConversationNode class attributes and methods

# BPMNProfile_OpaqueAction class attributes and methods

# BPMNProfile_Rendering class attributes and methods

# BPMNProfile_Task class attributes and methods

# BPMNActivity class attributes and methods

# BPMNProfile_Image class attributes and methods

# BPMNProfile_HumanPerformer class attributes and methods

# Performer class attributes and methods

# BPMNProfile_Performer class attributes and methods

# ResourceRole class attributes and methods

# BPMNProfile_GlobalUserTask class attributes and methods
BPMNProfile_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_GlobalUserTask_m_GlobalUserTaskrenderings: Method = Method(name="GlobalUserTaskrenderings", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_GlobalUserTask_m_GlobalUserTaskimplementation: Method = Method(name="GlobalUserTaskimplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_GlobalUserTask.attributes={BPMNProfile_GlobalUserTask_implementation}
BPMNProfile_GlobalUserTask.methods={BPMNProfile_GlobalUserTask_m_GlobalUserTaskimplementation, BPMNProfile_GlobalUserTask_m_GlobalUserTaskrenderings}

# BPMNProfile_Conversation class attributes and methods

# BPMNProfile_SubProcess class attributes and methods
BPMNProfile_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=StringType)
BPMNProfile_SubProcess_m_SubProcesstriggeredByEvent: Method = Method(name="SubProcesstriggeredByEvent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SubProcess.attributes={BPMNProfile_SubProcess_triggeredByEvent}
BPMNProfile_SubProcess.methods={BPMNProfile_SubProcess_m_SubProcesstriggeredByEvent}

# BPMNProfile_GlobalConversation class attributes and methods
BPMNProfile_GlobalConversation_m_GlobalConversationcontainedelements: Method = Method(name="GlobalConversationcontainedelements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalConversation.methods={BPMNProfile_GlobalConversation_m_GlobalConversationcontainedelements}

# BPMNCollaboration class attributes and methods

# BPMNProfile_CallConversation class attributes and methods
BPMNProfile_CallConversation_m_CallConversationcalledCollaborationRef: Method = Method(name="CallConversationcalledCollaborationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_CallConversation_m_CallConversationparticipantAssociations: Method = Method(name="CallConversationparticipantAssociations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_CallConversation.methods={BPMNProfile_CallConversation_m_CallConversationparticipantAssociations, BPMNProfile_CallConversation_m_CallConversationcalledCollaborationRef}

# BPMNProfile_CollaborationUse class attributes and methods

# BPMNProfile_ComplexBehaviorDefinition class attributes and methods

# BPMNProfile_CallActivity class attributes and methods
BPMNProfile_CallActivity_m_CallActivitycalledElementRefvalues: Method = Method(name="CallActivitycalledElementRefvalues", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_CallActivity.methods={BPMNProfile_CallActivity_m_CallActivitycalledElementRefvalues}

# BPMNProfile_CallBehaviorAction class attributes and methods

# BPMNProfile_BusinessRuleTask class attributes and methods
BPMNProfile_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_BusinessRuleTask_m_BusinessRuleTaskimplementation: Method = Method(name="BusinessRuleTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BusinessRuleTask.attributes={BPMNProfile_BusinessRuleTask_implementation}
BPMNProfile_BusinessRuleTask.methods={BPMNProfile_BusinessRuleTask_m_BusinessRuleTaskimplementation}

# BPMNProfile_SendTask class attributes and methods
BPMNProfile_SendTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_SendTask_m_SendTaskoperationRef: Method = Method(name="SendTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SendTask.attributes={BPMNProfile_SendTask_implementation}
BPMNProfile_SendTask.methods={BPMNProfile_SendTask_m_SendTaskoperationRef}

# BPMNProfile_AdHocSubProcess class attributes and methods
BPMNProfile_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
BPMNProfile_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=StringType)
BPMNProfile_AdHocSubProcess_m_AdHocSubProcesscancelRemainingInstances: Method = Method(name="AdHocSubProcesscancelRemainingInstances", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_AdHocSubProcess.attributes={BPMNProfile_AdHocSubProcess_ordering, BPMNProfile_AdHocSubProcess_cancelRemainingInstances}
BPMNProfile_AdHocSubProcess.methods={BPMNProfile_AdHocSubProcess_m_AdHocSubProcesscancelRemainingInstances}

# SubProcess class attributes and methods

# BPMNProfile_ScriptTask class attributes and methods
BPMNProfile_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
BPMNProfile_ScriptTask_script: Property = Property(name="script", type=StringType)
BPMNProfile_ScriptTask_m_ScriptTaskscriptFormat: Method = Method(name="ScriptTaskscriptFormat", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ScriptTask_m_ScriptTaskscript: Method = Method(name="ScriptTaskscript", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ScriptTask.attributes={BPMNProfile_ScriptTask_script, BPMNProfile_ScriptTask_scriptFormat}
BPMNProfile_ScriptTask.methods={BPMNProfile_ScriptTask_m_ScriptTaskscript, BPMNProfile_ScriptTask_m_ScriptTaskscriptFormat}

# BPMNProfile_ServiceTask class attributes and methods
BPMNProfile_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_ServiceTask_m_ServiceTaskinputSet: Method = Method(name="ServiceTaskinputSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ServiceTask_m_ServiceTaskoutputSet: Method = Method(name="ServiceTaskoutputSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ServiceTask_m_ServiceTaskoperationRef: Method = Method(name="ServiceTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ServiceTask.attributes={BPMNProfile_ServiceTask_implementation}
BPMNProfile_ServiceTask.methods={BPMNProfile_ServiceTask_m_ServiceTaskoutputSet, BPMNProfile_ServiceTask_m_ServiceTaskoperationRef, BPMNProfile_ServiceTask_m_ServiceTaskinputSet}

# BPMNProfile_Transaction class attributes and methods
BPMNProfile_Transaction_method: Property = Property(name="method", type=StringType)
BPMNProfile_Transaction.attributes={BPMNProfile_Transaction_method}

# BPMNProfile_StandardLoopCharacteristics class attributes and methods
BPMNProfile_StandardLoopCharacteristics_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
BPMNProfile_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=StringType)
BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore: Method = Method(name="StandardLoopCharacteristicstestBefore", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition: Method = Method(name="StandardLoopCharacteristicsloopCondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_StandardLoopCharacteristics.attributes={BPMNProfile_StandardLoopCharacteristics_loopMaximum, BPMNProfile_StandardLoopCharacteristics_testBefore}
BPMNProfile_StandardLoopCharacteristics.methods={BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition, BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore}

# LoopCharacteristics class attributes and methods

# BPMNProfile_LoopNode class attributes and methods

# BPMNProfile_ReceiveTask class attributes and methods
BPMNProfile_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_ReceiveTask_instantiate: Property = Property(name="instantiate", type=StringType)
BPMNProfile_ReceiveTask_m_ReceiveTaskoperationRef: Method = Method(name="ReceiveTaskoperationRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ReceiveTask.attributes={BPMNProfile_ReceiveTask_instantiate, BPMNProfile_ReceiveTask_implementation}
BPMNProfile_ReceiveTask.methods={BPMNProfile_ReceiveTask_m_ReceiveTaskoperationRef}

# BPMNProfile_MultiInstanceLoopCharacteristics class attributes and methods
BPMNProfile_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=StringType)
BPMNProfile_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
BPMNProfile_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget: Method = Method(name="MultiinstanceLoopCharacteristicstarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_MultiInstanceLoopCharacteristics.attributes={BPMNProfile_MultiInstanceLoopCharacteristics_isSequential, BPMNProfile_MultiInstanceLoopCharacteristics_behavior}
BPMNProfile_MultiInstanceLoopCharacteristics.methods={BPMNProfile_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget}

# BPMNProfile_ExpansionRegion class attributes and methods

# Relationships
base_Property30: BinaryAssociation = BinaryAssociation(
    name="base_Property30",
    ends={
        Property(name="BPMNProfile_Property", type=BPMNProfile_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionAttributeDefinition31", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_JoinNode1: BinaryAssociation = BinaryAssociation(
    name="base_JoinNode1",
    ends={
        Property(name="BPMNProfile_JoinNode", type=BPMNProfile_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_NonExclusiveGateway", type=BPMNProfile_JoinNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ForkNode2: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode2",
    ends={
        Property(name="BPMNProfile_ForkNode", type=BPMNProfile_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_NonExclusiveGateway3", type=BPMNProfile_ForkNode, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment32: BinaryAssociation = BinaryAssociation(
    name="base_Comment32",
    ends={
        Property(name="BPMNProfile_Comment", type=BPMNProfile_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Documentation33", type=BPMNProfile_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_ControlNode4: BinaryAssociation = BinaryAssociation(
    name="base_ControlNode4",
    ends={
        Property(name="BPMNProfile_ControlNode", type=BPMNProfile_Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Gateway", type=BPMNProfile_ControlNode, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityGroup5: BinaryAssociation = BinaryAssociation(
    name="base_ActivityGroup5",
    ends={
        Property(name="BPMNProfile_ActivityGroup", type=BPMNProfile_Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Gateway6", type=BPMNProfile_ActivityGroup, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityNode7: BinaryAssociation = BinaryAssociation(
    name="base_ActivityNode7",
    ends={
        Property(name="BPMNProfile_ActivityNode", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FlowNode", type=BPMNProfile_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
auditing8: BinaryAssociation = BinaryAssociation(
    name="auditing8",
    ends={
        Property(name="BPMNProfile_Auditing", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FlowElement", type=BPMNProfile_Auditing, multiplicity=Multiplicity(0, 1))
    }
)
monitoring9: BinaryAssociation = BinaryAssociation(
    name="monitoring9",
    ends={
        Property(name="BPMNProfile_Monitoring", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FlowElement10", type=BPMNProfile_Monitoring, multiplicity=Multiplicity(0, 1))
    }
)
_categoryValueRef11: BinaryAssociation = BinaryAssociation(
    name="_categoryValueRef11",
    ends={
        Property(name="CategoryValue", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="categorizedFlowElements", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(1, 9999))
    }
)
container12: BinaryAssociation = BinaryAssociation(
    name="container12",
    ends={
        Property(name="FlowElementsContainer", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="flowElements", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(1, 1))
    }
)
extensionValues13: BinaryAssociation = BinaryAssociation(
    name="extensionValues13",
    ends={
        Property(name="BPMNProfile_ExtensionAttributeValue", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BaseElement", type=BPMNProfile_ExtensionAttributeValue, multiplicity=Multiplicity(1, 9999))
    }
)
base_Element14: BinaryAssociation = BinaryAssociation(
    name="base_Element14",
    ends={
        Property(name="BPMNProfile_Element", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BaseElement15", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 1))
    }
)
documentation16: BinaryAssociation = BinaryAssociation(
    name="documentation16",
    ends={
        Property(name="BPMNProfile_Documentation", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BaseElement17", type=BPMNProfile_Documentation, multiplicity=Multiplicity(1, 9999))
    }
)
extensionDefinitions18: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions18",
    ends={
        Property(name="BPMNProfile_ExtensionDefinition", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BaseElement19", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing20: BinaryAssociation = BinaryAssociation(
    name="outgoing20",
    ends={
        Property(name="BPMNAssociation", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="BPMNAssociation22", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
base_Slot23: BinaryAssociation = BinaryAssociation(
    name="base_Slot23",
    ends={
        Property(name="BPMNProfile_Slot", type=BPMNProfile_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionAttributeValue24", type=BPMNProfile_Slot, multiplicity=Multiplicity(1, 1))
    }
)
valueRef25: BinaryAssociation = BinaryAssociation(
    name="valueRef25",
    ends={
        Property(name="BPMNProfile_Element27", type=BPMNProfile_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionAttributeValue26", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
extensionAttributeDefinition28: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition28",
    ends={
        Property(name="BPMNProfile_ExtensionAttributeDefinition", type=BPMNProfile_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionAttributeValue29", type=BPMNProfile_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
default0: BinaryAssociation = BinaryAssociation(
    name="default0",
    ends={
        Property(name="BPMNProfile_SequenceFlow", type=BPMNProfile_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InclusiveGateway", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
flowElements51: BinaryAssociation = BinaryAssociation(
    name="flowElements51",
    ends={
        Property(name="FlowElement52", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 9999))
    }
)
base_Stereotype34: BinaryAssociation = BinaryAssociation(
    name="base_Stereotype34",
    ends={
        Property(name="BPMNProfile_Stereotype", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionDefinition35", type=BPMNProfile_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
extensionAttributeDefinitions36: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions36",
    ends={
        Property(name="BPMNProfile_ExtensionAttributeDefinition38", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionDefinition37", type=BPMNProfile_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency39: BinaryAssociation = BinaryAssociation(
    name="base_Dependency39",
    ends={
        Property(name="BPMNProfile_Dependency", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNAssociation", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
targetRef40: BinaryAssociation = BinaryAssociation(
    name="targetRef40",
    ends={
        Property(name="BaseElement", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef41: BinaryAssociation = BinaryAssociation(
    name="sourceRef41",
    ends={
        Property(name="BaseElement42", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="BPMNProfile_Class", type=BPMNProfile_Auditing, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Auditing44", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="BPMNProfile_Class47", type=BPMNProfile_Monitoring, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Monitoring46", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_EnumerationLiteral48: BinaryAssociation = BinaryAssociation(
    name="base_EnumerationLiteral48",
    ends={
        Property(name="BPMNProfile_EnumerationLiteral", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CategoryValue", type=BPMNProfile_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
categorizedFlowElements49: BinaryAssociation = BinaryAssociation(
    name="categorizedFlowElements49",
    ends={
        Property(name="FlowElement", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="_categoryValueRef", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(1, 9999))
    }
)
laneSets50: BinaryAssociation = BinaryAssociation(
    name="laneSets50",
    ends={
        Property(name="LaneSet", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="flowElementsContainer", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_ActivityPartition59: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition59",
    ends={
        Property(name="BPMNProfile_ActivityPartition61", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane60", type=BPMNProfile_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityPartition53: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition53",
    ends={
        Property(name="BPMNProfile_ActivityPartition", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LaneSet", type=BPMNProfile_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
lanes54: BinaryAssociation = BinaryAssociation(
    name="lanes54",
    ends={
        Property(name="Lane", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="laneSet", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 9999))
    }
)
parentLane55: BinaryAssociation = BinaryAssociation(
    name="parentLane55",
    ends={
        Property(name="BPMNProfile_Lane", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LaneSet56", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 9999))
    }
)
flowElementsContainer57: BinaryAssociation = BinaryAssociation(
    name="flowElementsContainer57",
    ends={
        Property(name="FlowElementsContainer58", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="laneSets", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueExpression80: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueExpression80",
    ends={
        Property(name="BPMNProfile_OpaqueExpression", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExpression81", type=BPMNProfile_OpaqueExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_ForkNode82: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode82",
    ends={
        Property(name="BPMNProfile_ForkNode83", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway", type=BPMNProfile_ForkNode, multiplicity=Multiplicity(1, 1))
    }
)
_partitionElement62: BinaryAssociation = BinaryAssociation(
    name="_partitionElement62",
    ends={
        Property(name="BPMNProfile_Element64", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane63", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
flowNodeRefs65: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs65",
    ends={
        Property(name="BPMNProfile_FlowNode67", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane66", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(1, 9999))
    }
)
partitionElementRef68: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef68",
    ends={
        Property(name="BPMNProfile_BaseElement70", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane69", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
childLaneSet71: BinaryAssociation = BinaryAssociation(
    name="childLaneSet71",
    ends={
        Property(name="BPMNProfile_LaneSet73", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane72", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1))
    }
)
laneSet74: BinaryAssociation = BinaryAssociation(
    name="laneSet74",
    ends={
        Property(name="LaneSet75", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1))
    }
)
base_ControlFlow76: BinaryAssociation = BinaryAssociation(
    name="base_ControlFlow76",
    ends={
        Property(name="BPMNProfile_ControlFlow", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SequenceFlow77", type=BPMNProfile_ControlFlow, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression78: BinaryAssociation = BinaryAssociation(
    name="conditionExpression78",
    ends={
        Property(name="BPMNProfile_BPMNExpression", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SequenceFlow79", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_DecisionNode93: BinaryAssociation = BinaryAssociation(
    name="base_DecisionNode93",
    ends={
        Property(name="BPMNProfile_DecisionNode", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway", type=BPMNProfile_DecisionNode, multiplicity=Multiplicity(1, 1))
    }
)
base_MergeNode94: BinaryAssociation = BinaryAssociation(
    name="base_MergeNode94",
    ends={
        Property(name="BPMNProfile_MergeNode", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway95", type=BPMNProfile_MergeNode, multiplicity=Multiplicity(1, 1))
    }
)
default96: BinaryAssociation = BinaryAssociation(
    name="default96",
    ends={
        Property(name="BPMNProfile_SequenceFlow98", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway97", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
base_PackageableElement99: BinaryAssociation = BinaryAssociation(
    name="base_PackageableElement99",
    ends={
        Property(name="BPMNProfile_PackageableElement", type=BPMNProfile_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_RootElement", type=BPMNProfile_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode84: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode84",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway85", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
base_InterruptibleActivityRegion86: BinaryAssociation = BinaryAssociation(
    name="base_InterruptibleActivityRegion86",
    ends={
        Property(name="BPMNProfile_InterruptibleActivityRegion", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway87", type=BPMNProfile_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1))
    }
)
default88: BinaryAssociation = BinaryAssociation(
    name="default88",
    ends={
        Property(name="BPMNProfile_SequenceFlow89", type=BPMNProfile_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexGateway", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
activationCondition90: BinaryAssociation = BinaryAssociation(
    name="activationCondition90",
    ends={
        Property(name="BPMNProfile_BPMNExpression92", type=BPMNProfile_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexGateway91", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_Constraint120: BinaryAssociation = BinaryAssociation(
    name="base_Constraint120",
    ends={
        Property(name="BPMNProfile_Constraint", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship121", type=BPMNProfile_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
targets122: BinaryAssociation = BinaryAssociation(
    name="targets122",
    ends={
        Property(name="BPMNProfile_Element124", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship123", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 9999))
    }
)
definition100: BinaryAssociation = BinaryAssociation(
    name="definition100",
    ends={
        Property(name="Definitions", type=BPMNProfile_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rootElements", type=BPMNProfile_Definitions, multiplicity=Multiplicity(0, 1))
    }
)
base_Package101: BinaryAssociation = BinaryAssociation(
    name="base_Package101",
    ends={
        Property(name="BPMNProfile_Package", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions", type=BPMNProfile_Package, multiplicity=Multiplicity(1, 1))
    }
)
extensions102: BinaryAssociation = BinaryAssociation(
    name="extensions102",
    ends={
        Property(name="BPMNProfile_BPMNExtension", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions103", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(1, 9999))
    }
)
imports104: BinaryAssociation = BinaryAssociation(
    name="imports104",
    ends={
        Property(name="BPMNProfile_Import", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions105", type=BPMNProfile_Import, multiplicity=Multiplicity(1, 9999))
    }
)
relationships106: BinaryAssociation = BinaryAssociation(
    name="relationships106",
    ends={
        Property(name="BPMNProfile_BPMNRelationship", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions107", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
rootElements108: BinaryAssociation = BinaryAssociation(
    name="rootElements108",
    ends={
        Property(name="RootElement", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=BPMNProfile_RootElement, multiplicity=Multiplicity(1, 9999))
    }
)
base_Stereotype109: BinaryAssociation = BinaryAssociation(
    name="base_Stereotype109",
    ends={
        Property(name="BPMNProfile_Stereotype111", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExtension110", type=BPMNProfile_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
definition112: BinaryAssociation = BinaryAssociation(
    name="definition112",
    ends={
        Property(name="BPMNProfile_ExtensionDefinition114", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExtension113", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_PackageImport115: BinaryAssociation = BinaryAssociation(
    name="base_PackageImport115",
    ends={
        Property(name="BPMNProfile_PackageImport", type=BPMNProfile_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Import116", type=BPMNProfile_PackageImport, multiplicity=Multiplicity(1, 1))
    }
)
definitions117: BinaryAssociation = BinaryAssociation(
    name="definitions117",
    ends={
        Property(name="BPMNProfile_Definitions119", type=BPMNProfile_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Import118", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
auditing131: BinaryAssociation = BinaryAssociation(
    name="auditing131",
    ends={
        Property(name="BPMNProfile_Auditing132", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess", type=BPMNProfile_Auditing, multiplicity=Multiplicity(0, 1))
    }
)
definitionalCollaborationRef133: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef133",
    ends={
        Property(name="BPMNProfile_BPMNCollaboration", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess134", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
base_Activity135: BinaryAssociation = BinaryAssociation(
    name="base_Activity135",
    ends={
        Property(name="BPMNProfile_Activity", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess136", type=BPMNProfile_Activity, multiplicity=Multiplicity(1, 1))
    }
)
correlationSubscriptions137: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions137",
    ends={
        Property(name="BPMNProfile_CorrelationSubscription", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess138", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 9999))
    }
)
sources125: BinaryAssociation = BinaryAssociation(
    name="sources125",
    ends={
        Property(name="BPMNProfile_Element127", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship126", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 9999))
    }
)
definition128: BinaryAssociation = BinaryAssociation(
    name="definition128",
    ends={
        Property(name="BPMNProfile_Definitions130", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship129", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
dataInputs160: BinaryAssociation = BinaryAssociation(
    name="dataInputs160",
    ends={
        Property(name="BPMNProfile_DataInput", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification161", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputs162: BinaryAssociation = BinaryAssociation(
    name="dataOutputs162",
    ends={
        Property(name="BPMNProfile_DataOutput", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification163", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
inputSets164: BinaryAssociation = BinaryAssociation(
    name="inputSets164",
    ends={
        Property(name="BPMNProfile_InputSet", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification165", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSets166: BinaryAssociation = BinaryAssociation(
    name="outputSets166",
    ends={
        Property(name="BPMNProfile_OutputSet", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification167", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
monitoring139: BinaryAssociation = BinaryAssociation(
    name="monitoring139",
    ends={
        Property(name="BPMNProfile_Monitoring141", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess140", type=BPMNProfile_Monitoring, multiplicity=Multiplicity(0, 1))
    }
)
supports143: BinaryAssociation = BinaryAssociation(
    name="supports143",
    ends={
        Property(name="BPMNProfile_BPMNProcess144", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess142", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1))
    }
)
properties145: BinaryAssociation = BinaryAssociation(
    name="properties145",
    ends={
        Property(name="BPMNProfile_BPMNProperty", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess146", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
resources147: BinaryAssociation = BinaryAssociation(
    name="resources147",
    ends={
        Property(name="ResourceRole", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
base_Behavior148: BinaryAssociation = BinaryAssociation(
    name="base_Behavior148",
    ends={
        Property(name="BPMNProfile_Behavior", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement", type=BPMNProfile_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
ioSpecification149: BinaryAssociation = BinaryAssociation(
    name="ioSpecification149",
    ends={
        Property(name="BPMNProfile_InputOutputSpecification", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement150", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
supportedInterfaceRefs151: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs151",
    ends={
        Property(name="BPMNProfile_BPMNInterface", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement152", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 9999))
    }
)
ioBinding153: BinaryAssociation = BinaryAssociation(
    name="ioBinding153",
    ends={
        Property(name="BPMNProfile_InputOutputBinding", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement154", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 9999))
    }
)
base_Behavior155: BinaryAssociation = BinaryAssociation(
    name="base_Behavior155",
    ends={
        Property(name="BPMNProfile_Behavior157", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification156", type=BPMNProfile_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Action158: BinaryAssociation = BinaryAssociation(
    name="base_Action158",
    ends={
        Property(name="BPMNProfile_Action", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification159", type=BPMNProfile_Action, multiplicity=Multiplicity(1, 1))
    }
)
base_InputPin168: BinaryAssociation = BinaryAssociation(
    name="base_InputPin168",
    ends={
        Property(name="BPMNProfile_InputPin", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput169", type=BPMNProfile_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
base_Parameter170: BinaryAssociation = BinaryAssociation(
    name="base_Parameter170",
    ends={
        Property(name="BPMNProfile_Parameter", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput171", type=BPMNProfile_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
base_ActivityParameterNode172: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode172",
    ends={
        Property(name="BPMNProfile_ActivityParameterNode", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput173", type=BPMNProfile_ActivityParameterNode, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef182: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef182",
    ends={
        Property(name="BPMNProfile_ItemDefinition", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement183", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_State184: BinaryAssociation = BinaryAssociation(
    name="base_State184",
    ends={
        Property(name="BPMNProfile_State", type=BPMNProfile_DataState, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataState185", type=BPMNProfile_State, multiplicity=Multiplicity(1, 1))
    }
)
inputSetRefs174: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs174",
    ends={
        Property(name="InputSet", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
inputSetWithOptional175: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional175",
    ends={
        Property(name="InputSet176", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
inputSetWithWhileExecuting177: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting177",
    ends={
        Property(name="InputSet178", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
dataState179: BinaryAssociation = BinaryAssociation(
    name="dataState179",
    ends={
        Property(name="BPMNProfile_DataState", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement", type=BPMNProfile_DataState, multiplicity=Multiplicity(1, 9999))
    }
)
base_TypedElement180: BinaryAssociation = BinaryAssociation(
    name="base_TypedElement180",
    ends={
        Property(name="BPMNProfile_TypedElement", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement181", type=BPMNProfile_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_ParameterSet195: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet195",
    ends={
        Property(name="BPMNProfile_ParameterSet", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputSet196", type=BPMNProfile_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
base_Class186: BinaryAssociation = BinaryAssociation(
    name="base_Class186",
    ends={
        Property(name="BPMNProfile_Class188", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition187", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
structureRef189: BinaryAssociation = BinaryAssociation(
    name="structureRef189",
    ends={
        Property(name="BPMNProfile_Element191", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition190", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
import192: BinaryAssociation = BinaryAssociation(
    name="import192",
    ends={
        Property(name="BPMNProfile_Import194", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition193", type=BPMNProfile_Import, multiplicity=Multiplicity(0, 1))
    }
)
base_OutputPin202: BinaryAssociation = BinaryAssociation(
    name="base_OutputPin202",
    ends={
        Property(name="BPMNProfile_OutputPin", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput203", type=BPMNProfile_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
base_Parameter204: BinaryAssociation = BinaryAssociation(
    name="base_Parameter204",
    ends={
        Property(name="BPMNProfile_Parameter206", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput205", type=BPMNProfile_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
optionalInputRefs197: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs197",
    ends={
        Property(name="DataInput", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
whileExecutingInputRefs198: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs198",
    ends={
        Property(name="DataInput199", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
dataInputRefs200: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs200",
    ends={
        Property(name="DataInput201", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputRefs226: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs226",
    ends={
        Property(name="DataOutput", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
base_ActivityParameterNode207: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode207",
    ends={
        Property(name="BPMNProfile_ActivityParameterNode209", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput208", type=BPMNProfile_ActivityParameterNode, multiplicity=Multiplicity(1, 1))
    }
)
outputSetRefs210: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs210",
    ends={
        Property(name="OutputSet", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSetWithOptional211: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional211",
    ends={
        Property(name="BPMNProfile_OutputSet213", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput212", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSetWithWhileExecuting214: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting214",
    ends={
        Property(name="BPMNProfile_OutputSet216", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput215", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_ParameterSet217: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet217",
    ends={
        Property(name="BPMNProfile_ParameterSet219", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet218", type=BPMNProfile_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
optionalOutputRefs220: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs220",
    ends={
        Property(name="BPMNProfile_DataOutput222", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet221", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
whileExecutingOutputRefs223: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs223",
    ends={
        Property(name="BPMNProfile_DataOutput225", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet224", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 9999))
    }
)
base_Interface227: BinaryAssociation = BinaryAssociation(
    name="base_Interface227",
    ends={
        Property(name="BPMNProfile_Interface", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface228", type=BPMNProfile_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef229: BinaryAssociation = BinaryAssociation(
    name="implementationRef229",
    ends={
        Property(name="BPMNProfile_Element231", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface230", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
operations232: BinaryAssociation = BinaryAssociation(
    name="operations232",
    ends={
        Property(name="BPMNProfile_BPMNOperation", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface233", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 9999))
    }
)
callableElements234: BinaryAssociation = BinaryAssociation(
    name="callableElements234",
    ends={
        Property(name="BPMNProfile_CallableElement236", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface235", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 9999))
    }
)
base_Operation237: BinaryAssociation = BinaryAssociation(
    name="base_Operation237",
    ends={
        Property(name="BPMNProfile_Operation", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation238", type=BPMNProfile_Operation, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef239: BinaryAssociation = BinaryAssociation(
    name="implementationRef239",
    ends={
        Property(name="BPMNProfile_Element241", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation240", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef242: BinaryAssociation = BinaryAssociation(
    name="inMessageRef242",
    ends={
        Property(name="BPMNProfile_BPMNMessage", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation243", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef244: BinaryAssociation = BinaryAssociation(
    name="outMessageRef244",
    ends={
        Property(name="BPMNProfile_BPMNMessage246", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation245", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
errorRef247: BinaryAssociation = BinaryAssociation(
    name="errorRef247",
    ends={
        Property(name="BPMNProfile_Error", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation248", type=BPMNProfile_Error, multiplicity=Multiplicity(1, 9999))
    }
)
itemRef249: BinaryAssociation = BinaryAssociation(
    name="itemRef249",
    ends={
        Property(name="BPMNProfile_ItemDefinition251", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNMessage250", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef252: BinaryAssociation = BinaryAssociation(
    name="inputDataRef252",
    ends={
        Property(name="BPMNProfile_InputSet254", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding253", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef255: BinaryAssociation = BinaryAssociation(
    name="outputDataRef255",
    ends={
        Property(name="BPMNProfile_OutputSet257", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding256", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef258: BinaryAssociation = BinaryAssociation(
    name="operationRef258",
    ends={
        Property(name="BPMNProfile_BPMNOperation260", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding259", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency261: BinaryAssociation = BinaryAssociation(
    name="base_Dependency261",
    ends={
        Property(name="BPMNProfile_Dependency263", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding262", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef285: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef285",
    ends={
        Property(name="BPMNProfile_Participant287", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation286", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1))
    }
)
participantAssociations264: BinaryAssociation = BinaryAssociation(
    name="participantAssociations264",
    ends={
        Property(name="BPMNProfile_ParticipantAssociation", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration265", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
conversationLinks266: BinaryAssociation = BinaryAssociation(
    name="conversationLinks266",
    ends={
        Property(name="ConversationLink", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 9999))
    }
)
messageFlowAssociations267: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations267",
    ends={
        Property(name="BPMNProfile_MessageFlowAssociation", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration268", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
messageFlows269: BinaryAssociation = BinaryAssociation(
    name="messageFlows269",
    ends={
        Property(name="BPMNProfile_MessageFlow", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration270", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 9999))
    }
)
base_Collaboration271: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration271",
    ends={
        Property(name="BPMNProfile_Collaboration", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration272", type=BPMNProfile_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
conversations273: BinaryAssociation = BinaryAssociation(
    name="conversations273",
    ends={
        Property(name="BPMNProfile_ConversationNode", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration274", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 9999))
    }
)
correlationKeys275: BinaryAssociation = BinaryAssociation(
    name="correlationKeys275",
    ends={
        Property(name="BPMNProfile_CorrelationKey", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration276", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 9999))
    }
)
participants277: BinaryAssociation = BinaryAssociation(
    name="participants277",
    ends={
        Property(name="BPMNProfile_Participant", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration278", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency279: BinaryAssociation = BinaryAssociation(
    name="base_Dependency279",
    ends={
        Property(name="BPMNProfile_Dependency281", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation280", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
innerParticipantRef282: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef282",
    ends={
        Property(name="BPMNProfile_Participant284", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation283", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1))
    }
)
base_Property288: BinaryAssociation = BinaryAssociation(
    name="base_Property288",
    ends={
        Property(name="BPMNProfile_Property290", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant289", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
processRef291: BinaryAssociation = BinaryAssociation(
    name="processRef291",
    ends={
        Property(name="BPMNProfile_BPMNProcess293", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant292", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
participantMultiplicity294: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity294",
    ends={
        Property(name="BPMNProfile_ParticipantMultiplicity", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant295", type=BPMNProfile_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1))
    }
)
base_InstanceSpecification318: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification318",
    ends={
        Property(name="BPMNProfile_InstanceSpecification", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_PartnerEntity", type=BPMNProfile_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
participantRef319: BinaryAssociation = BinaryAssociation(
    name="participantRef319",
    ends={
        Property(name="Participant", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerEntityRef", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
partnerEntityRef296: BinaryAssociation = BinaryAssociation(
    name="partnerEntityRef296",
    ends={
        Property(name="PartnerEntity", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(1, 9999))
    }
)
partnerRoleRef297: BinaryAssociation = BinaryAssociation(
    name="partnerRoleRef297",
    ends={
        Property(name="PartnerRole", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef298", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(1, 9999))
    }
)
interfaceRefs299: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs299",
    ends={
        Property(name="BPMNProfile_BPMNInterface301", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant300", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 9999))
    }
)
base_Element302: BinaryAssociation = BinaryAssociation(
    name="base_Element302",
    ends={
        Property(name="BPMNProfile_Element303", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InteractionNode", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConversationLinks304: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks304",
    ends={
        Property(name="ConversationLink306", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef305", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 9999))
    }
)
incomingConversationLinks307: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks307",
    ends={
        Property(name="ConversationLink309", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef308", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1))
    }
)
collaboration310: BinaryAssociation = BinaryAssociation(
    name="collaboration310",
    ends={
        Property(name="BPMNCollaboration", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="conversationLinks", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency311: BinaryAssociation = BinaryAssociation(
    name="base_Dependency311",
    ends={
        Property(name="BPMNProfile_Dependency312", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationLink", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
targetRef313: BinaryAssociation = BinaryAssociation(
    name="targetRef313",
    ends={
        Property(name="InteractionNode", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConversationLinks", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef314: BinaryAssociation = BinaryAssociation(
    name="sourceRef314",
    ends={
        Property(name="InteractionNode315", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConversationLinks", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
base_MultiplicityElement316: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement316",
    ends={
        Property(name="BPMNProfile_MultiplicityElement", type=BPMNProfile_ParticipantMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantMultiplicity317", type=BPMNProfile_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Class320: BinaryAssociation = BinaryAssociation(
    name="base_Class320",
    ends={
        Property(name="BPMNProfile_Class321", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_PartnerRole", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
participantRef322: BinaryAssociation = BinaryAssociation(
    name="participantRef322",
    ends={
        Property(name="Participant323", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerRoleRef", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency324: BinaryAssociation = BinaryAssociation(
    name="base_Dependency324",
    ends={
        Property(name="BPMNProfile_Dependency326", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation325", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef327: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef327",
    ends={
        Property(name="BPMNProfile_MessageFlow329", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation328", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef330: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef330",
    ends={
        Property(name="BPMNProfile_MessageFlow332", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation331", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRetrievalExpression367: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression367",
    ends={
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty368", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency369: BinaryAssociation = BinaryAssociation(
    name="base_Dependency369",
    ends={
        Property(name="BPMNProfile_Dependency371", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression370", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
base_InformationFlow333: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow333",
    ends={
        Property(name="BPMNProfile_InformationFlow", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow334", type=BPMNProfile_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef335: BinaryAssociation = BinaryAssociation(
    name="sourceRef335",
    ends={
        Property(name="BPMNProfile_InteractionNode337", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow336", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef338: BinaryAssociation = BinaryAssociation(
    name="targetRef338",
    ends={
        Property(name="BPMNProfile_InteractionNode340", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow339", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
messageRef341: BinaryAssociation = BinaryAssociation(
    name="messageRef341",
    ends={
        Property(name="BPMNProfile_BPMNMessage343", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow342", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_InformationFlow344: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow344",
    ends={
        Property(name="BPMNProfile_InformationFlow346", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode345", type=BPMNProfile_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
messageFlowRefs347: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs347",
    ends={
        Property(name="BPMNProfile_MessageFlow349", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode348", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 9999))
    }
)
correlationKeys350: BinaryAssociation = BinaryAssociation(
    name="correlationKeys350",
    ends={
        Property(name="BPMNProfile_CorrelationKey352", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode351", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 9999))
    }
)
participantRefs353: BinaryAssociation = BinaryAssociation(
    name="participantRefs353",
    ends={
        Property(name="BPMNProfile_Participant355", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode354", type=BPMNProfile_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
base_Class356: BinaryAssociation = BinaryAssociation(
    name="base_Class356",
    ends={
        Property(name="BPMNProfile_Class358", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationKey357", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef359: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef359",
    ends={
        Property(name="BPMNProfile_CorrelationProperty", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationKey360", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 9999))
    }
)
base_Property361: BinaryAssociation = BinaryAssociation(
    name="base_Property361",
    ends={
        Property(name="BPMNProfile_Property363", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty362", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
type364: BinaryAssociation = BinaryAssociation(
    name="type364",
    ends={
        Property(name="BPMNProfile_ItemDefinition366", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty365", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_DataStoreNode397: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode397",
    ends={
        Property(name="BPMNProfile_DataStoreNode", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProperty398", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
umlProperty399: BinaryAssociation = BinaryAssociation(
    name="umlProperty399",
    ends={
        Property(name="BPMNProfile_Property401", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProperty400", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
messageRef372: BinaryAssociation = BinaryAssociation(
    name="messageRef372",
    ends={
        Property(name="BPMNProfile_BPMNMessage374", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression373", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
messagePath375: BinaryAssociation = BinaryAssociation(
    name="messagePath375",
    ends={
        Property(name="BPMNProfile_FormalExpression", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression376", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
evaluatesToTypeRef377: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef377",
    ends={
        Property(name="BPMNProfile_ItemDefinition379", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FormalExpression378", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_Class380: BinaryAssociation = BinaryAssociation(
    name="base_Class380",
    ends={
        Property(name="BPMNProfile_Class382", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription381", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationKeyRef383: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef383",
    ends={
        Property(name="BPMNProfile_CorrelationKey385", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription384", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding386: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding386",
    ends={
        Property(name="BPMNProfile_CorrelationPropertyBinding", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription387", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 9999))
    }
)
base_Property388: BinaryAssociation = BinaryAssociation(
    name="base_Property388",
    ends={
        Property(name="BPMNProfile_Property390", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding389", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
dataPath391: BinaryAssociation = BinaryAssociation(
    name="dataPath391",
    ends={
        Property(name="BPMNProfile_FormalExpression393", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding392", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef394: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef394",
    ends={
        Property(name="BPMNProfile_CorrelationProperty396", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding395", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
process410: BinaryAssociation = BinaryAssociation(
    name="process410",
    ends={
        Property(name="BPMNProcess", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
base_Property402: BinaryAssociation = BinaryAssociation(
    name="base_Property402",
    ends={
        Property(name="BPMNProfile_Property403", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
resourceAssignmentExpression404: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression404",
    ends={
        Property(name="BPMNProfile_ResourceAssignmentExpression", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole405", type=BPMNProfile_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef406: BinaryAssociation = BinaryAssociation(
    name="resourceRef406",
    ends={
        Property(name="BPMNProfile_Resource", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole407", type=BPMNProfile_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings408: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings408",
    ends={
        Property(name="BPMNProfile_ResourceParameterBinding", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole409", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 9999))
    }
)
expression411: BinaryAssociation = BinaryAssociation(
    name="expression411",
    ends={
        Property(name="BPMNProfile_BPMNExpression413", type=BPMNProfile_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceAssignmentExpression412", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
resourceParameters414: BinaryAssociation = BinaryAssociation(
    name="resourceParameters414",
    ends={
        Property(name="BPMNProfile_ResourceParameter", type=BPMNProfile_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Resource415", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 9999))
    }
)
base_Property416: BinaryAssociation = BinaryAssociation(
    name="base_Property416",
    ends={
        Property(name="BPMNProfile_Property418", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameter417", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
type419: BinaryAssociation = BinaryAssociation(
    name="type419",
    ends={
        Property(name="BPMNProfile_ItemDefinition421", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameter420", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
resources432: BinaryAssociation = BinaryAssociation(
    name="resources432",
    ends={
        Property(name="BPMNProfile_ResourceRole434", type=BPMNProfile_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalTask433", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
base_Slot422: BinaryAssociation = BinaryAssociation(
    name="base_Slot422",
    ends={
        Property(name="BPMNProfile_Slot424", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding423", type=BPMNProfile_Slot, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef425: BinaryAssociation = BinaryAssociation(
    name="parameterRef425",
    ends={
        Property(name="BPMNProfile_ResourceParameter427", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding426", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
expression428: BinaryAssociation = BinaryAssociation(
    name="expression428",
    ends={
        Property(name="BPMNProfile_BPMNExpression430", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding429", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueBehavior431: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueBehavior431",
    ends={
        Property(name="BPMNProfile_OpaqueBehavior", type=BPMNProfile_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalTask", type=BPMNProfile_OpaqueBehavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Action439: BinaryAssociation = BinaryAssociation(
    name="base_Action439",
    ends={
        Property(name="BPMNProfile_Action441", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity440", type=BPMNProfile_Action, multiplicity=Multiplicity(1, 1))
    }
)
activityRef435: BinaryAssociation = BinaryAssociation(
    name="activityRef435",
    ends={
        Property(name="BPMNProfile_BPMNActivity", type=BPMNProfile_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CompensateEventDefinition", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent436: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent436",
    ends={
        Property(name="BPMNProfile_CallEvent", type=BPMNProfile_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CompensateEventDefinition437", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Event438: BinaryAssociation = BinaryAssociation(
    name="base_Event438",
    ends={
        Property(name="BPMNProfile_Event", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventDefinition", type=BPMNProfile_Event, multiplicity=Multiplicity(1, 1))
    }
)
base_AcceptEventAction465: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction465",
    ends={
        Property(name="BPMNProfile_AcceptEventAction", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent", type=BPMNProfile_AcceptEventAction, multiplicity=Multiplicity(1, 1))
    }
)
base_InitialNode466: BinaryAssociation = BinaryAssociation(
    name="base_InitialNode466",
    ends={
        Property(name="BPMNProfile_InitialNode", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent467", type=BPMNProfile_InitialNode, multiplicity=Multiplicity(1, 1))
    }
)
dataOutputAssociation468: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation468",
    ends={
        Property(name="BPMNProfile_DataOutputAssociation470", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent469", type=BPMNProfile_DataOutputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
activityClass442: BinaryAssociation = BinaryAssociation(
    name="activityClass442",
    ends={
        Property(name="BPMNProfile_Class444", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity443", type=BPMNProfile_Class, multiplicity=Multiplicity(0, 1))
    }
)
properties445: BinaryAssociation = BinaryAssociation(
    name="properties445",
    ends={
        Property(name="BPMNProfile_BPMNProperty447", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity446", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
default448: BinaryAssociation = BinaryAssociation(
    name="default448",
    ends={
        Property(name="BPMNProfile_SequenceFlow450", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity449", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
boundaryEventRefs451: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs451",
    ends={
        Property(name="BPMNProfile_BoundaryEvent", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity452", type=BPMNProfile_BoundaryEvent, multiplicity=Multiplicity(1, 9999))
    }
)
dataInputAssociations453: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations453",
    ends={
        Property(name="BPMNProfile_DataInputAssociation", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity454", type=BPMNProfile_DataInputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
dataOutputAssociations455: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations455",
    ends={
        Property(name="BPMNProfile_DataOutputAssociation", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity456", type=BPMNProfile_DataOutputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
loopCharacteristics457: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics457",
    ends={
        Property(name="BPMNProfile_LoopCharacteristics", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity458", type=BPMNProfile_LoopCharacteristics, multiplicity=Multiplicity(0, 1))
    }
)
resources459: BinaryAssociation = BinaryAssociation(
    name="resources459",
    ends={
        Property(name="BPMNProfile_ResourceRole461", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity460", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 9999))
    }
)
attachedToRef462: BinaryAssociation = BinaryAssociation(
    name="attachedToRef462",
    ends={
        Property(name="BPMNProfile_BPMNActivity464", type=BPMNProfile_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BoundaryEvent463", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1))
    }
)
base_ObjectFlow482: BinaryAssociation = BinaryAssociation(
    name="base_ObjectFlow482",
    ends={
        Property(name="BPMNProfile_ObjectFlow", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation", type=BPMNProfile_ObjectFlow, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef483: BinaryAssociation = BinaryAssociation(
    name="sourceRef483",
    ends={
        Property(name="BPMNProfile_ItemAwareElement485", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation484", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
eventClass471: BinaryAssociation = BinaryAssociation(
    name="eventClass471",
    ends={
        Property(name="BPMNProfile_Class472", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent", type=BPMNProfile_Class, multiplicity=Multiplicity(0, 1))
    }
)
_eventDefinitions473: BinaryAssociation = BinaryAssociation(
    name="_eventDefinitions473",
    ends={
        Property(name="BPMNProfile_EventDefinition475", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent474", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
properties476: BinaryAssociation = BinaryAssociation(
    name="properties476",
    ends={
        Property(name="BPMNProfile_BPMNProperty478", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent477", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 9999))
    }
)
eventDefinitionRefs479: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs479",
    ends={
        Property(name="BPMNProfile_EventDefinition481", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent480", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
base_CallEvent507: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent507",
    ends={
        Property(name="BPMNProfile_CallEvent509", type=BPMNProfile_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EscalationEventDefinition508", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
targetRef486: BinaryAssociation = BinaryAssociation(
    name="targetRef486",
    ends={
        Property(name="BPMNProfile_ItemAwareElement488", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation487", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
transformation489: BinaryAssociation = BinaryAssociation(
    name="transformation489",
    ends={
        Property(name="BPMNProfile_FormalExpression491", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation490", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignment492: BinaryAssociation = BinaryAssociation(
    name="assignment492",
    ends={
        Property(name="BPMNProfile_Assignment", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation493", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency494: BinaryAssociation = BinaryAssociation(
    name="base_Dependency494",
    ends={
        Property(name="BPMNProfile_Dependency496", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment495", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
from497: BinaryAssociation = BinaryAssociation(
    name="from497",
    ends={
        Property(name="BPMNProfile_BPMNExpression499", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment498", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
to500: BinaryAssociation = BinaryAssociation(
    name="to500",
    ends={
        Property(name="BPMNProfile_BPMNExpression502", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment501", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode503: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode503",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode505", type=BPMNProfile_LoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LoopCharacteristics504", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
escalationRef506: BinaryAssociation = BinaryAssociation(
    name="escalationRef506",
    ends={
        Property(name="BPMNProfile_Escalation", type=BPMNProfile_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EscalationEventDefinition", type=BPMNProfile_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
base_FinalNode524: BinaryAssociation = BinaryAssociation(
    name="base_FinalNode524",
    ends={
        Property(name="BPMNProfile_FinalNode", type=BPMNProfile_EndEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EndEvent", type=BPMNProfile_FinalNode, multiplicity=Multiplicity(1, 1))
    }
)
timeCycle510: BinaryAssociation = BinaryAssociation(
    name="timeCycle510",
    ends={
        Property(name="BPMNProfile_BPMNExpression511", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDate512: BinaryAssociation = BinaryAssociation(
    name="timeDate512",
    ends={
        Property(name="BPMNProfile_BPMNExpression514", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition513", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDuration515: BinaryAssociation = BinaryAssociation(
    name="timeDuration515",
    ends={
        Property(name="BPMNProfile_BPMNExpression517", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition516", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ChangeEvent518: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent518",
    ends={
        Property(name="BPMNProfile_ChangeEvent", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition519", type=BPMNProfile_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
signalRef520: BinaryAssociation = BinaryAssociation(
    name="signalRef520",
    ends={
        Property(name="BPMNProfile_BPMNSignal", type=BPMNProfile_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SignalEventDefinition", type=BPMNProfile_BPMNSignal, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent521: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent521",
    ends={
        Property(name="BPMNProfile_CallEvent523", type=BPMNProfile_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SignalEventDefinition522", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
_target545: BinaryAssociation = BinaryAssociation(
    name="_target545",
    ends={
        Property(name="LinkEventDefinition", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
source547: BinaryAssociation = BinaryAssociation(
    name="source547",
    ends={
        Property(name="LinkEventDefinition548", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="_target", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
base_CallOperationAction525: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction525",
    ends={
        Property(name="BPMNProfile_CallOperationAction", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
base_FlowFinalNode526: BinaryAssociation = BinaryAssociation(
    name="base_FlowFinalNode526",
    ends={
        Property(name="BPMNProfile_FlowFinalNode", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent527", type=BPMNProfile_FlowFinalNode, multiplicity=Multiplicity(1, 1))
    }
)
dataInputAssociation528: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation528",
    ends={
        Property(name="BPMNProfile_DataInputAssociation530", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent529", type=BPMNProfile_DataInputAssociation, multiplicity=Multiplicity(1, 9999))
    }
)
messageRef531: BinaryAssociation = BinaryAssociation(
    name="messageRef531",
    ends={
        Property(name="BPMNProfile_BPMNMessage532", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
operationRef533: BinaryAssociation = BinaryAssociation(
    name="operationRef533",
    ends={
        Property(name="BPMNProfile_BPMNOperation535", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition534", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent536: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent536",
    ends={
        Property(name="BPMNProfile_CallEvent538", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition537", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_ChangeEvent539: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent539",
    ends={
        Property(name="BPMNProfile_ChangeEvent540", type=BPMNProfile_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConditionalEventDefinition", type=BPMNProfile_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
condition541: BinaryAssociation = BinaryAssociation(
    name="condition541",
    ends={
        Property(name="BPMNProfile_BPMNExpression543", type=BPMNProfile_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConditionalEventDefinition542", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
categoryValue564: BinaryAssociation = BinaryAssociation(
    name="categoryValue564",
    ends={
        Property(name="BPMNProfile_CategoryValue566", type=BPMNProfile_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Category565", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(1, 9999))
    }
)
base_ActivityPartition567: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition567",
    ends={
        Property(name="BPMNProfile_ActivityPartition568", type=BPMNProfile_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Group", type=BPMNProfile_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
_categoryValueRef569: BinaryAssociation = BinaryAssociation(
    name="_categoryValueRef569",
    ends={
        Property(name="BPMNProfile_CategoryValue571", type=BPMNProfile_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Group570", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent549: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent549",
    ends={
        Property(name="BPMNProfile_CallEvent550", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LinkEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
errorRef551: BinaryAssociation = BinaryAssociation(
    name="errorRef551",
    ends={
        Property(name="BPMNProfile_Error552", type=BPMNProfile_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ErrorEventDefinition", type=BPMNProfile_Error, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent553: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent553",
    ends={
        Property(name="BPMNProfile_CallEvent555", type=BPMNProfile_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ErrorEventDefinition554", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_SendObjectAction556: BinaryAssociation = BinaryAssociation(
    name="base_SendObjectAction556",
    ends={
        Property(name="BPMNProfile_SendObjectAction", type=BPMNProfile_IntermediateThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_IntermediateThrowEvent", type=BPMNProfile_SendObjectAction, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent557: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent557",
    ends={
        Property(name="BPMNProfile_CallEvent558", type=BPMNProfile_TerminateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TerminateEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent559: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent559",
    ends={
        Property(name="BPMNProfile_CallEvent560", type=BPMNProfile_CancelEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CancelEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment561: BinaryAssociation = BinaryAssociation(
    name="base_Comment561",
    ends={
        Property(name="BPMNProfile_Comment562", type=BPMNProfile_TextAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TextAnnotation", type=BPMNProfile_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration563: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration563",
    ends={
        Property(name="BPMNProfile_Enumeration", type=BPMNProfile_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Category", type=BPMNProfile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
_dataStore584: BinaryAssociation = BinaryAssociation(
    name="_dataStore584",
    ends={
        Property(name="BPMNProfile_DataStore585", type=BPMNProfile_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStoreReference", type=BPMNProfile_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
base_DataStoreNode586: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode586",
    ends={
        Property(name="BPMNProfile_DataStoreNode588", type=BPMNProfile_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStoreReference587", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
dataObjectRef572: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef572",
    ends={
        Property(name="BPMNProfile_DataObject", type=BPMNProfile_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObjectReference", type=BPMNProfile_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode573: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode573",
    ends={
        Property(name="BPMNProfile_DataStoreNode575", type=BPMNProfile_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObjectReference574", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode576: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode576",
    ends={
        Property(name="BPMNProfile_DataStoreNode578", type=BPMNProfile_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObject577", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_Class579: BinaryAssociation = BinaryAssociation(
    name="base_Class579",
    ends={
        Property(name="BPMNProfile_Class580", type=BPMNProfile_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStore", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef581: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef581",
    ends={
        Property(name="BPMNProfile_ItemDefinition583", type=BPMNProfile_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStore582", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueAction598: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction598",
    ends={
        Property(name="BPMNProfile_OpaqueAction599", type=BPMNProfile_ManualTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ManualTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction589: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction589",
    ends={
        Property(name="BPMNProfile_OpaqueAction", type=BPMNProfile_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_UserTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
renderings590: BinaryAssociation = BinaryAssociation(
    name="renderings590",
    ends={
        Property(name="BPMNProfile_Rendering", type=BPMNProfile_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_UserTask591", type=BPMNProfile_Rendering, multiplicity=Multiplicity(1, 9999))
    }
)
ioSpecification592: BinaryAssociation = BinaryAssociation(
    name="ioSpecification592",
    ends={
        Property(name="BPMNProfile_InputOutputSpecification593", type=BPMNProfile_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Task", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Image594: BinaryAssociation = BinaryAssociation(
    name="base_Image594",
    ends={
        Property(name="BPMNProfile_Image", type=BPMNProfile_Rendering, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Rendering595", type=BPMNProfile_Image, multiplicity=Multiplicity(1, 1))
    }
)
renderings596: BinaryAssociation = BinaryAssociation(
    name="renderings596",
    ends={
        Property(name="BPMNProfile_Rendering597", type=BPMNProfile_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalUserTask", type=BPMNProfile_Rendering, multiplicity=Multiplicity(1, 9999))
    }
)
participantAssociations606: BinaryAssociation = BinaryAssociation(
    name="participantAssociations606",
    ends={
        Property(name="BPMNProfile_CallConversation607", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 9999)),
        Property(name="BPMNProfile_ParticipantAssociation608", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1))
    }
)
conversationNodes600: BinaryAssociation = BinaryAssociation(
    name="conversationNodes600",
    ends={
        Property(name="BPMNProfile_ConversationNode601", type=BPMNProfile_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubConversation", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 9999))
    }
)
_collaborationUse602: BinaryAssociation = BinaryAssociation(
    name="_collaborationUse602",
    ends={
        Property(name="BPMNProfile_CollaborationUse", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallConversation", type=BPMNProfile_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
calledCollaborationRef603: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef603",
    ends={
        Property(name="BPMNProfile_BPMNCollaboration605", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallConversation604", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueAction618: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction618",
    ends={
        Property(name="BPMNProfile_OpaqueAction619", type=BPMNProfile_BusinessRuleTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BusinessRuleTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
condition620: BinaryAssociation = BinaryAssociation(
    name="condition620",
    ends={
        Property(name="BPMNProfile_FormalExpression621", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode609: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode609",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode610", type=BPMNProfile_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubProcess", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
hasLaneSets611: BinaryAssociation = BinaryAssociation(
    name="hasLaneSets611",
    ends={
        Property(name="BPMNProfile_LaneSet613", type=BPMNProfile_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubProcess612", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 9999))
    }
)
base_CallBehaviorAction614: BinaryAssociation = BinaryAssociation(
    name="base_CallBehaviorAction614",
    ends={
        Property(name="BPMNProfile_CallBehaviorAction", type=BPMNProfile_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallActivity", type=BPMNProfile_CallBehaviorAction, multiplicity=Multiplicity(1, 1))
    }
)
calledElementRef615: BinaryAssociation = BinaryAssociation(
    name="calledElementRef615",
    ends={
        Property(name="BPMNProfile_CallableElement617", type=BPMNProfile_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallActivity616", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
event622: BinaryAssociation = BinaryAssociation(
    name="event622",
    ends={
        Property(name="BPMNProfile_ImplicitThrowEvent", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition623", type=BPMNProfile_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1))
    }
)
base_ControlFlow624: BinaryAssociation = BinaryAssociation(
    name="base_ControlFlow624",
    ends={
        Property(name="BPMNProfile_ControlFlow626", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition625", type=BPMNProfile_ControlFlow, multiplicity=Multiplicity(1, 1))
    }
)
completionCondition627: BinaryAssociation = BinaryAssociation(
    name="completionCondition627",
    ends={
        Property(name="BPMNProfile_BPMNExpression628", type=BPMNProfile_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_AdHocSubProcess", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction629: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction629",
    ends={
        Property(name="BPMNProfile_OpaqueAction630", type=BPMNProfile_ScriptTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ScriptTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
base_AcceptEventAction645: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction645",
    ends={
        Property(name="BPMNProfile_AcceptEventAction647", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask646", type=BPMNProfile_AcceptEventAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef648: BinaryAssociation = BinaryAssociation(
    name="operationRef648",
    ends={
        Property(name="BPMNProfile_BPMNOperation650", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask649", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef631: BinaryAssociation = BinaryAssociation(
    name="messageRef631",
    ends={
        Property(name="BPMNProfile_BPMNMessage632", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_CallOperationAction633: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction633",
    ends={
        Property(name="BPMNProfile_CallOperationAction635", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask634", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef636: BinaryAssociation = BinaryAssociation(
    name="operationRef636",
    ends={
        Property(name="BPMNProfile_BPMNOperation638", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask637", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_LoopNode639: BinaryAssociation = BinaryAssociation(
    name="base_LoopNode639",
    ends={
        Property(name="BPMNProfile_LoopNode", type=BPMNProfile_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_StandardLoopCharacteristics", type=BPMNProfile_LoopNode, multiplicity=Multiplicity(1, 1))
    }
)
loopCondition640: BinaryAssociation = BinaryAssociation(
    name="loopCondition640",
    ends={
        Property(name="BPMNProfile_BPMNExpression642", type=BPMNProfile_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_StandardLoopCharacteristics641", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
messageRef643: BinaryAssociation = BinaryAssociation(
    name="messageRef643",
    ends={
        Property(name="BPMNProfile_BPMNMessage644", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
loopDataInputRef663: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef663",
    ends={
        Property(name="BPMNProfile_ItemAwareElement665", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics664", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef666: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef666",
    ends={
        Property(name="BPMNProfile_ItemAwareElement668", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics667", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
outputDataItem669: BinaryAssociation = BinaryAssociation(
    name="outputDataItem669",
    ends={
        Property(name="BPMNProfile_DataOutput671", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics670", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1))
    }
)
base_CallOperationAction651: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction651",
    ends={
        Property(name="BPMNProfile_CallOperationAction652", type=BPMNProfile_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ServiceTask", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef653: BinaryAssociation = BinaryAssociation(
    name="operationRef653",
    ends={
        Property(name="BPMNProfile_BPMNOperation655", type=BPMNProfile_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ServiceTask654", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
loopCardinality656: BinaryAssociation = BinaryAssociation(
    name="loopCardinality656",
    ends={
        Property(name="BPMNProfile_BPMNExpression657", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition658: BinaryAssociation = BinaryAssociation(
    name="completionCondition658",
    ends={
        Property(name="BPMNProfile_BPMNExpression660", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics659", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ExpansionRegion661: BinaryAssociation = BinaryAssociation(
    name="base_ExpansionRegion661",
    ends={
        Property(name="BPMNProfile_ExpansionRegion", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics662", type=BPMNProfile_ExpansionRegion, multiplicity=Multiplicity(1, 1))
    }
)
inputDataItem672: BinaryAssociation = BinaryAssociation(
    name="inputDataItem672",
    ends={
        Property(name="BPMNProfile_DataInput674", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics673", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1))
    }
)
oneBehaviorEventRef675: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef675",
    ends={
        Property(name="BPMNProfile_EventDefinition677", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics676", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
noneBehaviorEventRef678: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef678",
    ends={
        Property(name="BPMNProfile_EventDefinition680", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics679", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
complexBehaviorDefinition681: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition681",
    ends={
        Property(name="BPMNProfile_ComplexBehaviorDefinition683", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics682", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_BPMNProfile_NonExclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_NonExclusiveGateway)
gen_BPMNProfile_Documentation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Documentation)
gen_BPMNProfile_Gateway_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_Gateway)
gen_BPMNProfile_FlowNode_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_FlowNode)
gen_BPMNProfile_FlowElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_FlowElement)
gen_BPMNProfile_InclusiveGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_InclusiveGateway)
gen_BPMNProfile_LaneSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_LaneSet)
gen_BPMNProfile_BPMNAssociation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_BPMNAssociation)
gen_BPMNProfile_BPMNArtifact_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNArtifact)
gen_BPMNProfile_Auditing_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Auditing)
gen_BPMNProfile_Monitoring_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Monitoring)
gen_BPMNProfile_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CategoryValue)
gen_BPMNProfile_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_FlowElementsContainer)
gen_BPMNProfile_Lane_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Lane)
gen_BPMNProfile_BPMNExpression_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNExpression)
gen_BPMNProfile_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_EventBasedGateway)
gen_BPMNProfile_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_SequenceFlow)
gen_BPMNProfile_RootElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_RootElement)
gen_BPMNProfile_ParallelGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_ParallelGateway)
gen_BPMNProfile_ComplexGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_ComplexGateway)
gen_BPMNProfile_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_ExclusiveGateway)
gen_BPMNProfile_BPMNRelationship_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNRelationship)
gen_BPMNProfile_Definitions_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Definitions)
gen_BPMNProfile_BPMNProcess_CallableElement = Generalization(general=CallableElement, specific=BPMNProfile_BPMNProcess)
gen_BPMNProfile_BPMNProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMNProfile_BPMNProcess)
gen_BPMNProfile_CallableElement_RootElement = Generalization(general=RootElement, specific=BPMNProfile_CallableElement)
gen_BPMNProfile_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputOutputSpecification)
gen_BPMNProfile_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataInput)
gen_BPMNProfile_DataState_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_DataState)
gen_BPMNProfile_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ItemAwareElement)
gen_BPMNProfile_ItemDefinition_RootElement = Generalization(general=RootElement, specific=BPMNProfile_ItemDefinition)
gen_BPMNProfile_InputSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputSet)
gen_BPMNProfile_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataOutput)
gen_BPMNProfile_BPMNInterface_RootElement = Generalization(general=RootElement, specific=BPMNProfile_BPMNInterface)
gen_BPMNProfile_OutputSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_OutputSet)
gen_BPMNProfile_BPMNOperation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNOperation)
gen_BPMNProfile_BPMNCollaboration_RootElement = Generalization(general=RootElement, specific=BPMNProfile_BPMNCollaboration)
gen_BPMNProfile_BPMNMessage_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_BPMNMessage)
gen_BPMNProfile_Error_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Error)
gen_BPMNProfile_InputOutputBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputOutputBinding)
gen_BPMNProfile_Participant_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Participant)
gen_BPMNProfile_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ParticipantAssociation)
gen_BPMNProfile_PartnerRole_RootElement = Generalization(general=RootElement, specific=BPMNProfile_PartnerRole)
gen_BPMNProfile_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ConversationLink)
gen_BPMNProfile_ParticipantMultiplicity_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ParticipantMultiplicity)
gen_BPMNProfile_PartnerEntity_RootElement = Generalization(general=RootElement, specific=BPMNProfile_PartnerEntity)
gen_BPMNProfile_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_MessageFlowAssociation)
gen_BPMNProfile_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_MessageFlow)
gen_BPMNProfile_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationPropertyRetrievalExpression)
gen_BPMNProfile_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=BPMNProfile_ConversationNode)
gen_BPMNProfile_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationKey)
gen_BPMNProfile_CorrelationProperty_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationProperty)
gen_BPMNProfile_FormalExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=BPMNProfile_FormalExpression)
gen_BPMNProfile_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationSubscription)
gen_BPMNProfile_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationPropertyBinding)
gen_BPMNProfile_BPMNProperty_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_BPMNProperty)
gen_BPMNProfile_ResourceAssignmentExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=BPMNProfile_ResourceAssignmentExpression)
gen_BPMNProfile_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceRole)
gen_BPMNProfile_ResourceParameterBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceParameterBinding)
gen_BPMNProfile_Resource_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Resource)
gen_BPMNProfile_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceParameter)
gen_BPMNProfile_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalBusinessRuleTask)
gen_BPMNProfile_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalScriptTask)
gen_BPMNProfile_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=BPMNProfile_GlobalTask)
gen_BPMNProfile_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_CompensateEventDefinition)
gen_BPMNProfile_EventDefinition_RootElement = Generalization(general=RootElement, specific=BPMNProfile_EventDefinition)
gen_BPMNProfile_BPMNActivity_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_BPMNActivity)
gen_BPMNProfile_BPMNEvent_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_BPMNEvent)
gen_BPMNProfile_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_BoundaryEvent)
gen_BPMNProfile_CatchEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=BPMNProfile_CatchEvent)
gen_BPMNProfile_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMNProfile_DataOutputAssociation)
gen_BPMNProfile_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_DataAssociation)
gen_BPMNProfile_Escalation_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Escalation)
gen_BPMNProfile_Assignment_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Assignment)
gen_BPMNProfile_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMNProfile_DataInputAssociation)
gen_BPMNProfile_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_LoopCharacteristics)
gen_BPMNProfile_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_EscalationEventDefinition)
gen_BPMNProfile_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_EndEvent)
gen_BPMNProfile_ThrowEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=BPMNProfile_ThrowEvent)
gen_BPMNProfile_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_TimerEventDefinition)
gen_BPMNProfile_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_SignalEventDefinition)
gen_BPMNProfile_BPMNSignal_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_BPMNSignal)
gen_BPMNProfile_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_LinkEventDefinition)
gen_BPMNProfile_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_MessageEventDefinition)
gen_BPMNProfile_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_StartEvent)
gen_BPMNProfile_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_ConditionalEventDefinition)
gen_BPMNProfile_Group_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_Group)
gen_BPMNProfile_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_ErrorEventDefinition)
gen_BPMNProfile_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_IntermediateCatchEvent)
gen_BPMNProfile_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_IntermediateThrowEvent)
gen_BPMNProfile_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_TerminateEventDefinition)
gen_BPMNProfile_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_ImplicitThrowEvent)
gen_BPMNProfile_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_CancelEventDefinition)
gen_BPMNProfile_TextAnnotation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_TextAnnotation)
gen_BPMNProfile_Category_RootElement = Generalization(general=RootElement, specific=BPMNProfile_Category)
gen_BPMNProfile_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataStoreReference)
gen_BPMNProfile_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataStoreReference)
gen_BPMNProfile_UserTask_Task = Generalization(general=Task, specific=BPMNProfile_UserTask)
gen_BPMNProfile_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataObjectReference)
gen_BPMNProfile_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataObjectReference)
gen_BPMNProfile_DataObject_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataObject)
gen_BPMNProfile_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataObject)
gen_BPMNProfile_DataStore_RootElement = Generalization(general=RootElement, specific=BPMNProfile_DataStore)
gen_BPMNProfile_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalManualTask)
gen_BPMNProfile_ManualTask_Task = Generalization(general=Task, specific=BPMNProfile_ManualTask)
gen_BPMNProfile_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=BPMNProfile_PotentialOwner)
gen_BPMNProfile_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_SubConversation)
gen_BPMNProfile_Task_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_Task)
gen_BPMNProfile_Rendering_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Rendering)
gen_BPMNProfile_HumanPerformer_Performer = Generalization(general=Performer, specific=BPMNProfile_HumanPerformer)
gen_BPMNProfile_Performer_ResourceRole = Generalization(general=ResourceRole, specific=BPMNProfile_Performer)
gen_BPMNProfile_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalUserTask)
gen_BPMNProfile_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_Conversation)
gen_BPMNProfile_SubProcess_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_SubProcess)
gen_BPMNProfile_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMNProfile_SubProcess)
gen_BPMNProfile_GlobalConversation_BPMNCollaboration = Generalization(general=BPMNCollaboration, specific=BPMNProfile_GlobalConversation)
gen_BPMNProfile_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_CallConversation)
gen_BPMNProfile_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ComplexBehaviorDefinition)
gen_BPMNProfile_CallActivity_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_CallActivity)
gen_BPMNProfile_BusinessRuleTask_Task = Generalization(general=Task, specific=BPMNProfile_BusinessRuleTask)
gen_BPMNProfile_SendTask_Task = Generalization(general=Task, specific=BPMNProfile_SendTask)
gen_BPMNProfile_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=BPMNProfile_AdHocSubProcess)
gen_BPMNProfile_ScriptTask_Task = Generalization(general=Task, specific=BPMNProfile_ScriptTask)
gen_BPMNProfile_ServiceTask_Task = Generalization(general=Task, specific=BPMNProfile_ServiceTask)
gen_BPMNProfile_Transaction_SubProcess = Generalization(general=SubProcess, specific=BPMNProfile_Transaction)
gen_BPMNProfile_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMNProfile_StandardLoopCharacteristics)
gen_BPMNProfile_ReceiveTask_Task = Generalization(general=Task, specific=BPMNProfile_ReceiveTask)
gen_BPMNProfile_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMNProfile_MultiInstanceLoopCharacteristics)

# Domain Model
domain_model = DomainModel(
    name="BPMNProfile",
    types={BPMNProfile_JoinNode, BPMNProfile_ForkNode, BPMNProfile_Comment, BPMNProfile_Gateway, FlowNode, BPMNProfile_ControlNode, BPMNProfile_ActivityGroup, BPMNProfile_FlowNode, FlowElement, BPMNProfile_ActivityNode, BPMNProfile_FlowElement, BaseElement, BPMNProfile_Auditing, BPMNProfile_Monitoring, BPMNProfile_CategoryValue, BPMNProfile_FlowElementsContainer, BPMNProfile_BaseElement, BPMNProfile_ExtensionAttributeValue, BPMNProfile_Element, BPMNProfile_Documentation, BPMNProfile_InclusiveGateway, BPMNProfile_ExtensionDefinition, NonExclusiveGateway, BPMNProfile_BPMNAssociation, BPMNProfile_Slot, BPMNProfile_SequenceFlow, BPMNProfile_ExtensionAttributeDefinition, BPMNProfile_Property, BPMNProfile_NonExclusiveGateway, Gateway, BPMNProfile_Stereotype, BPMNArtifact, BPMNProfile_Dependency, BPMNProfile_BPMNArtifact, BPMNProfile_Class, BPMNProfile_EnumerationLiteral, BPMNProfile_LaneSet, BPMNProfile_ActivityPartition, BPMNProfile_Lane, BPMNProfile_OpaqueExpression, BPMNProfile_EventBasedGateway, BPMNProfile_ControlFlow, BPMNProfile_BPMNExpression, BPMNProfile_DecisionNode, BPMNProfile_MergeNode, BPMNProfile_RootElement, BPMNProfile_PackageableElement, BPMNProfile_StructuredActivityNode, BPMNProfile_InterruptibleActivityRegion, BPMNProfile_ParallelGateway, BPMNProfile_ComplexGateway, BPMNProfile_ExclusiveGateway, BPMNProfile_Constraint, BPMNProfile_Definitions, BPMNProfile_Package, BPMNProfile_BPMNExtension, BPMNProfile_Import, BPMNProfile_BPMNRelationship, BPMNProfile_PackageImport, BPMNProfile_BPMNCollaboration, BPMNProfile_Activity, BPMNProfile_CorrelationSubscription, BPMNProfile_BPMNProcess, CallableElement, FlowElementsContainer, BPMNProfile_DataInput, BPMNProfile_DataOutput, BPMNProfile_InputSet, BPMNProfile_OutputSet, BPMNProfile_BPMNProperty, BPMNProfile_ResourceRole, BPMNProfile_CallableElement, RootElement, BPMNProfile_Behavior, BPMNProfile_InputOutputSpecification, BPMNProfile_BPMNInterface, BPMNProfile_InputOutputBinding, BPMNProfile_Action, ItemAwareElement, BPMNProfile_InputPin, BPMNProfile_Parameter, BPMNProfile_ActivityParameterNode, BPMNProfile_ItemDefinition, BPMNProfile_State, BPMNProfile_ItemAwareElement, BPMNProfile_DataState, BPMNProfile_TypedElement, BPMNProfile_ParameterSet, BPMNProfile_OutputPin, BPMNProfile_Operation, BPMNProfile_Interface, BPMNProfile_BPMNOperation, BPMNProfile_ParticipantAssociation, BPMNProfile_BPMNMessage, BPMNProfile_Error, ItemDefinition, BPMNProfile_ConversationLink, BPMNProfile_MessageFlowAssociation, BPMNProfile_MessageFlow, BPMNProfile_Collaboration, BPMNProfile_ConversationNode, BPMNProfile_CorrelationKey, BPMNProfile_Participant, BPMNProfile_ParticipantMultiplicity, BPMNProfile_InstanceSpecification, BPMNProfile_PartnerEntity, BPMNProfile_PartnerRole, BPMNProfile_InteractionNode, BPMNProfile_MultiplicityElement, BPMNProfile_CorrelationPropertyRetrievalExpression, BPMNProfile_InformationFlow, InteractionNode, BPMNProfile_CorrelationProperty, BPMNProfile_DataStoreNode, BPMNProfile_FormalExpression, BPMNExpression, BPMNProfile_CorrelationPropertyBinding, BPMNProfile_ResourceAssignmentExpression, BPMNProfile_Resource, BPMNProfile_ResourceParameterBinding, BPMNProfile_ResourceParameter, BPMNProfile_GlobalBusinessRuleTask, BPMNProfile_GlobalScriptTask, GlobalTask, BPMNProfile_GlobalTask, BPMNProfile_OpaqueBehavior, BPMNProfile_CompensateEventDefinition, EventDefinition, BPMNProfile_BPMNActivity, BPMNProfile_CallEvent, BPMNProfile_EventDefinition, BPMNProfile_Event, BPMNProfile_AcceptEventAction, BPMNProfile_InitialNode, BPMNProfile_BPMNEvent, BPMNProfile_BoundaryEvent, BPMNProfile_DataInputAssociation, BPMNProfile_DataOutputAssociation, BPMNProfile_LoopCharacteristics, CatchEvent, BPMNProfile_CatchEvent, BPMNEvent, DataAssociation, BPMNProfile_DataAssociation, BPMNProfile_ObjectFlow, BPMNProfile_Assignment, BPMNProfile_EscalationEventDefinition, BPMNProfile_Escalation, BPMNProfile_EndEvent, ThrowEvent, BPMNProfile_FinalNode, BPMNProfile_ThrowEvent, BPMNProfile_TimerEventDefinition, BPMNProfile_ChangeEvent, BPMNProfile_SignalEventDefinition, BPMNProfile_BPMNSignal, BPMNProfile_LinkEventDefinition, BPMNProfile_CallOperationAction, BPMNProfile_FlowFinalNode, BPMNProfile_MessageEventDefinition, BPMNProfile_StartEvent, BPMNProfile_ConditionalEventDefinition, BPMNProfile_Group, BPMNProfile_ErrorEventDefinition, BPMNProfile_IntermediateCatchEvent, BPMNProfile_IntermediateThrowEvent, BPMNProfile_SendObjectAction, BPMNProfile_TerminateEventDefinition, BPMNProfile_ImplicitThrowEvent, BPMNProfile_CancelEventDefinition, BPMNProfile_TextAnnotation, BPMNProfile_Category, BPMNProfile_Enumeration, BPMNProfile_DataStoreReference, BPMNProfile_UserTask, Task, BPMNProfile_DataObjectReference, BPMNProfile_DataObject, BPMNProfile_DataStore, BPMNProfile_GlobalManualTask, BPMNProfile_ManualTask, BPMNProfile_PotentialOwner, HumanPerformer, BPMNProfile_SubConversation, ConversationNode, BPMNProfile_OpaqueAction, BPMNProfile_Rendering, BPMNProfile_Task, BPMNActivity, BPMNProfile_Image, BPMNProfile_HumanPerformer, Performer, BPMNProfile_Performer, ResourceRole, BPMNProfile_GlobalUserTask, BPMNProfile_Conversation, BPMNProfile_SubProcess, BPMNProfile_GlobalConversation, BPMNCollaboration, BPMNProfile_CallConversation, BPMNProfile_CollaborationUse, BPMNProfile_ComplexBehaviorDefinition, BPMNProfile_CallActivity, BPMNProfile_CallBehaviorAction, BPMNProfile_BusinessRuleTask, BPMNProfile_SendTask, BPMNProfile_AdHocSubProcess, SubProcess, BPMNProfile_ScriptTask, BPMNProfile_ServiceTask, BPMNProfile_Transaction, BPMNProfile_StandardLoopCharacteristics, LoopCharacteristics, BPMNProfile_LoopNode, BPMNProfile_ReceiveTask, BPMNProfile_MultiInstanceLoopCharacteristics, BPMNProfile_ExpansionRegion, AssociationDirection, EventBasedGatewayType, GatewayDirection, RelationshipDirection, ItemKind, ProcessType, AdHocOrdering, MultiInstanceBehavior},
    associations={base_Property30, base_JoinNode1, base_ForkNode2, base_Comment32, base_ControlNode4, base_ActivityGroup5, base_ActivityNode7, auditing8, monitoring9, _categoryValueRef11, container12, extensionValues13, base_Element14, documentation16, extensionDefinitions18, outgoing20, incoming21, base_Slot23, valueRef25, extensionAttributeDefinition28, default0, flowElements51, base_Stereotype34, extensionAttributeDefinitions36, base_Dependency39, targetRef40, sourceRef41, base_Class43, base_Class45, base_EnumerationLiteral48, categorizedFlowElements49, laneSets50, base_ActivityPartition59, base_ActivityPartition53, lanes54, parentLane55, flowElementsContainer57, base_OpaqueExpression80, base_ForkNode82, _partitionElement62, flowNodeRefs65, partitionElementRef68, childLaneSet71, laneSet74, base_ControlFlow76, conditionExpression78, base_DecisionNode93, base_MergeNode94, default96, base_PackageableElement99, base_StructuredActivityNode84, base_InterruptibleActivityRegion86, default88, activationCondition90, base_Constraint120, targets122, definition100, base_Package101, extensions102, imports104, relationships106, rootElements108, base_Stereotype109, definition112, base_PackageImport115, definitions117, auditing131, definitionalCollaborationRef133, base_Activity135, correlationSubscriptions137, sources125, definition128, dataInputs160, dataOutputs162, inputSets164, outputSets166, monitoring139, supports143, properties145, resources147, base_Behavior148, ioSpecification149, supportedInterfaceRefs151, ioBinding153, base_Behavior155, base_Action158, base_InputPin168, base_Parameter170, base_ActivityParameterNode172, itemSubjectRef182, base_State184, inputSetRefs174, inputSetWithOptional175, inputSetWithWhileExecuting177, dataState179, base_TypedElement180, base_ParameterSet195, base_Class186, structureRef189, import192, base_OutputPin202, base_Parameter204, optionalInputRefs197, whileExecutingInputRefs198, dataInputRefs200, dataOutputRefs226, base_ActivityParameterNode207, outputSetRefs210, outputSetWithOptional211, outputSetWithWhileExecuting214, base_ParameterSet217, optionalOutputRefs220, whileExecutingOutputRefs223, base_Interface227, implementationRef229, operations232, callableElements234, base_Operation237, implementationRef239, inMessageRef242, outMessageRef244, errorRef247, itemRef249, inputDataRef252, outputDataRef255, operationRef258, base_Dependency261, outerParticipantRef285, participantAssociations264, conversationLinks266, messageFlowAssociations267, messageFlows269, base_Collaboration271, conversations273, correlationKeys275, participants277, base_Dependency279, innerParticipantRef282, base_Property288, processRef291, participantMultiplicity294, base_InstanceSpecification318, participantRef319, partnerEntityRef296, partnerRoleRef297, interfaceRefs299, base_Element302, outgoingConversationLinks304, incomingConversationLinks307, collaboration310, base_Dependency311, targetRef313, sourceRef314, base_MultiplicityElement316, base_Class320, participantRef322, base_Dependency324, innerMessageFlowRef327, outerMessageFlowRef330, correlationPropertyRetrievalExpression367, base_Dependency369, base_InformationFlow333, sourceRef335, targetRef338, messageRef341, base_InformationFlow344, messageFlowRefs347, correlationKeys350, participantRefs353, base_Class356, correlationPropertyRef359, base_Property361, type364, base_DataStoreNode397, umlProperty399, messageRef372, messagePath375, evaluatesToTypeRef377, base_Class380, correlationKeyRef383, correlationPropertyBinding386, base_Property388, dataPath391, correlationPropertyRef394, process410, base_Property402, resourceAssignmentExpression404, resourceRef406, resourceParameterBindings408, expression411, resourceParameters414, base_Property416, type419, resources432, base_Slot422, parameterRef425, expression428, base_OpaqueBehavior431, base_Action439, activityRef435, base_CallEvent436, base_Event438, base_AcceptEventAction465, base_InitialNode466, dataOutputAssociation468, activityClass442, properties445, default448, boundaryEventRefs451, dataInputAssociations453, dataOutputAssociations455, loopCharacteristics457, resources459, attachedToRef462, base_ObjectFlow482, sourceRef483, eventClass471, _eventDefinitions473, properties476, eventDefinitionRefs479, base_CallEvent507, targetRef486, transformation489, assignment492, base_Dependency494, from497, to500, base_StructuredActivityNode503, escalationRef506, base_FinalNode524, timeCycle510, timeDate512, timeDuration515, base_ChangeEvent518, signalRef520, base_CallEvent521, _target545, source547, base_CallOperationAction525, base_FlowFinalNode526, dataInputAssociation528, messageRef531, operationRef533, base_CallEvent536, base_ChangeEvent539, condition541, categoryValue564, base_ActivityPartition567, _categoryValueRef569, base_CallEvent549, errorRef551, base_CallEvent553, base_SendObjectAction556, base_CallEvent557, base_CallEvent559, base_Comment561, base_Enumeration563, _dataStore584, base_DataStoreNode586, dataObjectRef572, base_DataStoreNode573, base_DataStoreNode576, base_Class579, itemSubjectRef581, base_OpaqueAction598, base_OpaqueAction589, renderings590, ioSpecification592, base_Image594, renderings596, participantAssociations606, conversationNodes600, _collaborationUse602, calledCollaborationRef603, base_OpaqueAction618, condition620, base_StructuredActivityNode609, hasLaneSets611, base_CallBehaviorAction614, calledElementRef615, event622, base_ControlFlow624, completionCondition627, base_OpaqueAction629, base_AcceptEventAction645, operationRef648, messageRef631, base_CallOperationAction633, operationRef636, base_LoopNode639, loopCondition640, messageRef643, loopDataInputRef663, loopDataOutputRef666, outputDataItem669, base_CallOperationAction651, operationRef653, loopCardinality656, completionCondition658, base_ExpansionRegion661, inputDataItem672, oneBehaviorEventRef675, noneBehaviorEventRef678, complexBehaviorDefinition681},
    generalizations={gen_BPMNProfile_NonExclusiveGateway_Gateway, gen_BPMNProfile_Documentation_BaseElement, gen_BPMNProfile_Gateway_FlowNode, gen_BPMNProfile_FlowNode_FlowElement, gen_BPMNProfile_FlowElement_BaseElement, gen_BPMNProfile_InclusiveGateway_NonExclusiveGateway, gen_BPMNProfile_LaneSet_BaseElement, gen_BPMNProfile_BPMNAssociation_BPMNArtifact, gen_BPMNProfile_BPMNArtifact_BaseElement, gen_BPMNProfile_Auditing_BaseElement, gen_BPMNProfile_Monitoring_BaseElement, gen_BPMNProfile_CategoryValue_BaseElement, gen_BPMNProfile_FlowElementsContainer_BaseElement, gen_BPMNProfile_Lane_BaseElement, gen_BPMNProfile_BPMNExpression_BaseElement, gen_BPMNProfile_EventBasedGateway_Gateway, gen_BPMNProfile_SequenceFlow_FlowElement, gen_BPMNProfile_RootElement_BaseElement, gen_BPMNProfile_ParallelGateway_NonExclusiveGateway, gen_BPMNProfile_ComplexGateway_NonExclusiveGateway, gen_BPMNProfile_ExclusiveGateway_Gateway, gen_BPMNProfile_BPMNRelationship_BaseElement, gen_BPMNProfile_Definitions_BaseElement, gen_BPMNProfile_BPMNProcess_CallableElement, gen_BPMNProfile_BPMNProcess_FlowElementsContainer, gen_BPMNProfile_CallableElement_RootElement, gen_BPMNProfile_InputOutputSpecification_BaseElement, gen_BPMNProfile_DataInput_ItemAwareElement, gen_BPMNProfile_DataState_BaseElement, gen_BPMNProfile_ItemAwareElement_BaseElement, gen_BPMNProfile_ItemDefinition_RootElement, gen_BPMNProfile_InputSet_BaseElement, gen_BPMNProfile_DataOutput_ItemAwareElement, gen_BPMNProfile_BPMNInterface_RootElement, gen_BPMNProfile_OutputSet_BaseElement, gen_BPMNProfile_BPMNOperation_BaseElement, gen_BPMNProfile_BPMNCollaboration_RootElement, gen_BPMNProfile_BPMNMessage_ItemDefinition, gen_BPMNProfile_Error_ItemDefinition, gen_BPMNProfile_InputOutputBinding_BaseElement, gen_BPMNProfile_Participant_BaseElement, gen_BPMNProfile_ParticipantAssociation_BaseElement, gen_BPMNProfile_PartnerRole_RootElement, gen_BPMNProfile_ConversationLink_BaseElement, gen_BPMNProfile_ParticipantMultiplicity_BaseElement, gen_BPMNProfile_PartnerEntity_RootElement, gen_BPMNProfile_MessageFlowAssociation_BaseElement, gen_BPMNProfile_MessageFlow_BaseElement, gen_BPMNProfile_CorrelationPropertyRetrievalExpression_BaseElement, gen_BPMNProfile_ConversationNode_InteractionNode, gen_BPMNProfile_CorrelationKey_BaseElement, gen_BPMNProfile_CorrelationProperty_BaseElement, gen_BPMNProfile_FormalExpression_BPMNExpression, gen_BPMNProfile_CorrelationSubscription_BaseElement, gen_BPMNProfile_CorrelationPropertyBinding_BaseElement, gen_BPMNProfile_BPMNProperty_ItemAwareElement, gen_BPMNProfile_ResourceAssignmentExpression_BPMNExpression, gen_BPMNProfile_ResourceRole_BaseElement, gen_BPMNProfile_ResourceParameterBinding_BaseElement, gen_BPMNProfile_Resource_ItemDefinition, gen_BPMNProfile_ResourceParameter_BaseElement, gen_BPMNProfile_GlobalBusinessRuleTask_GlobalTask, gen_BPMNProfile_GlobalScriptTask_GlobalTask, gen_BPMNProfile_GlobalTask_CallableElement, gen_BPMNProfile_CompensateEventDefinition_EventDefinition, gen_BPMNProfile_EventDefinition_RootElement, gen_BPMNProfile_BPMNActivity_FlowNode, gen_BPMNProfile_BPMNEvent_FlowNode, gen_BPMNProfile_BoundaryEvent_CatchEvent, gen_BPMNProfile_CatchEvent_BPMNEvent, gen_BPMNProfile_DataOutputAssociation_DataAssociation, gen_BPMNProfile_DataAssociation_BaseElement, gen_BPMNProfile_Escalation_ItemDefinition, gen_BPMNProfile_Assignment_BaseElement, gen_BPMNProfile_DataInputAssociation_DataAssociation, gen_BPMNProfile_LoopCharacteristics_BaseElement, gen_BPMNProfile_EscalationEventDefinition_EventDefinition, gen_BPMNProfile_EndEvent_ThrowEvent, gen_BPMNProfile_ThrowEvent_BPMNEvent, gen_BPMNProfile_TimerEventDefinition_EventDefinition, gen_BPMNProfile_SignalEventDefinition_EventDefinition, gen_BPMNProfile_BPMNSignal_ItemDefinition, gen_BPMNProfile_LinkEventDefinition_EventDefinition, gen_BPMNProfile_MessageEventDefinition_EventDefinition, gen_BPMNProfile_StartEvent_CatchEvent, gen_BPMNProfile_ConditionalEventDefinition_EventDefinition, gen_BPMNProfile_Group_BPMNArtifact, gen_BPMNProfile_ErrorEventDefinition_EventDefinition, gen_BPMNProfile_IntermediateCatchEvent_CatchEvent, gen_BPMNProfile_IntermediateThrowEvent_ThrowEvent, gen_BPMNProfile_TerminateEventDefinition_EventDefinition, gen_BPMNProfile_ImplicitThrowEvent_ThrowEvent, gen_BPMNProfile_CancelEventDefinition_EventDefinition, gen_BPMNProfile_TextAnnotation_BPMNArtifact, gen_BPMNProfile_Category_RootElement, gen_BPMNProfile_DataStoreReference_FlowElement, gen_BPMNProfile_DataStoreReference_ItemAwareElement, gen_BPMNProfile_UserTask_Task, gen_BPMNProfile_DataObjectReference_FlowElement, gen_BPMNProfile_DataObjectReference_ItemAwareElement, gen_BPMNProfile_DataObject_FlowElement, gen_BPMNProfile_DataObject_ItemAwareElement, gen_BPMNProfile_DataStore_RootElement, gen_BPMNProfile_GlobalManualTask_GlobalTask, gen_BPMNProfile_ManualTask_Task, gen_BPMNProfile_PotentialOwner_HumanPerformer, gen_BPMNProfile_SubConversation_ConversationNode, gen_BPMNProfile_Task_BPMNActivity, gen_BPMNProfile_Rendering_BaseElement, gen_BPMNProfile_HumanPerformer_Performer, gen_BPMNProfile_Performer_ResourceRole, gen_BPMNProfile_GlobalUserTask_GlobalTask, gen_BPMNProfile_Conversation_ConversationNode, gen_BPMNProfile_SubProcess_BPMNActivity, gen_BPMNProfile_SubProcess_FlowElementsContainer, gen_BPMNProfile_GlobalConversation_BPMNCollaboration, gen_BPMNProfile_CallConversation_ConversationNode, gen_BPMNProfile_ComplexBehaviorDefinition_BaseElement, gen_BPMNProfile_CallActivity_BPMNActivity, gen_BPMNProfile_BusinessRuleTask_Task, gen_BPMNProfile_SendTask_Task, gen_BPMNProfile_AdHocSubProcess_SubProcess, gen_BPMNProfile_ScriptTask_Task, gen_BPMNProfile_ServiceTask_Task, gen_BPMNProfile_Transaction_SubProcess, gen_BPMNProfile_StandardLoopCharacteristics_LoopCharacteristics, gen_BPMNProfile_ReceiveTask_Task, gen_BPMNProfile_MultiInstanceLoopCharacteristics_LoopCharacteristics},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)