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
BPMNProfile_InclusiveGateway = Class(name="BPMNProfile::InclusiveGateway")
NonExclusiveGateway = Class(name="NonExclusiveGateway")
BPMNProfile_SequenceFlow = Class(name="BPMNProfile::SequenceFlow")
BPMNProfile_NonExclusiveGateway = Class(name="BPMNProfile::NonExclusiveGateway", is_abstract=True)
Gateway = Class(name="Gateway")
BPMNProfile_JoinNode = Class(name="BPMNProfile::JoinNode")
BPMNProfile_ForkNode = Class(name="BPMNProfile::ForkNode")
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
BPMNProfile_ExtensionDefinition = Class(name="BPMNProfile::ExtensionDefinition")
BPMNProfile_BPMNAssociation = Class(name="BPMNProfile::BPMNAssociation")
BPMNProfile_Property = Class(name="BPMNProfile::Property")
BPMNProfile_Comment = Class(name="BPMNProfile::Comment")
BPMNProfile_Stereotype = Class(name="BPMNProfile::Stereotype")
BPMNArtifact = Class(name="BPMNArtifact")
BPMNProfile_Dependency = Class(name="BPMNProfile::Dependency")
BPMNProfile_BPMNArtifact = Class(name="BPMNProfile::BPMNArtifact", is_abstract=True)
BPMNProfile_Class = Class(name="BPMNProfile::Class")
BPMNProfile_Slot = Class(name="BPMNProfile::Slot")
BPMNProfile_ExtensionAttributeDefinition = Class(name="BPMNProfile::ExtensionAttributeDefinition")
BPMNProfile_LaneSet = Class(name="BPMNProfile::LaneSet")
BPMNProfile_ActivityPartition = Class(name="BPMNProfile::ActivityPartition")
BPMNProfile_Lane = Class(name="BPMNProfile::Lane")
BPMNProfile_EnumerationLiteral = Class(name="BPMNProfile::EnumerationLiteral")
BPMNProfile_OpaqueExpression = Class(name="BPMNProfile::OpaqueExpression")
BPMNProfile_EventBasedGateway = Class(name="BPMNProfile::EventBasedGateway")
BPMNProfile_StructuredActivityNode = Class(name="BPMNProfile::StructuredActivityNode")
BPMNProfile_InterruptibleActivityRegion = Class(name="BPMNProfile::InterruptibleActivityRegion")
BPMNProfile_ParallelGateway = Class(name="BPMNProfile::ParallelGateway")
BPMNProfile_ComplexGateway = Class(name="BPMNProfile::ComplexGateway")
BPMNProfile_ControlFlow = Class(name="BPMNProfile::ControlFlow")
BPMNProfile_BPMNExpression = Class(name="BPMNProfile::BPMNExpression")
BPMNProfile_MergeNode = Class(name="BPMNProfile::MergeNode")
BPMNProfile_RootElement = Class(name="BPMNProfile::RootElement", is_abstract=True)
BPMNProfile_PackageableElement = Class(name="BPMNProfile::PackageableElement")
BPMNProfile_Definitions = Class(name="BPMNProfile::Definitions")
BPMNProfile_Package = Class(name="BPMNProfile::Package")
BPMNProfile_BPMNExtension = Class(name="BPMNProfile::BPMNExtension")
BPMNProfile_Import = Class(name="BPMNProfile::Import")
BPMNProfile_BPMNRelationship = Class(name="BPMNProfile::BPMNRelationship")
BPMNProfile_PackageImport = Class(name="BPMNProfile::PackageImport")
BPMNProfile_ExclusiveGateway = Class(name="BPMNProfile::ExclusiveGateway")
BPMNProfile_DecisionNode = Class(name="BPMNProfile::DecisionNode")
BPMNProfile_BPMNProcess = Class(name="BPMNProfile::BPMNProcess")
CallableElement = Class(name="CallableElement")
FlowElementsContainer = Class(name="FlowElementsContainer")
BPMNProfile_BPMNCollaboration = Class(name="BPMNProfile::BPMNCollaboration")
BPMNProfile_Activity = Class(name="BPMNProfile::Activity")
BPMNProfile_CorrelationSubscription = Class(name="BPMNProfile::CorrelationSubscription")
BPMNProfile_Constraint = Class(name="BPMNProfile::Constraint")
BPMNProfile_Behavior = Class(name="BPMNProfile::Behavior")
BPMNProfile_InputOutputSpecification = Class(name="BPMNProfile::InputOutputSpecification")
BPMNProfile_BPMNInterface = Class(name="BPMNProfile::BPMNInterface")
BPMNProfile_InputOutputBinding = Class(name="BPMNProfile::InputOutputBinding")
BPMNProfile_Action = Class(name="BPMNProfile::Action")
BPMNProfile_DataInput = Class(name="BPMNProfile::DataInput")
BPMNProfile_DataOutput = Class(name="BPMNProfile::DataOutput")
BPMNProfile_InputSet = Class(name="BPMNProfile::InputSet")
BPMNProfile_OutputSet = Class(name="BPMNProfile::OutputSet")
ItemAwareElement = Class(name="ItemAwareElement")
BPMNProfile_BPMNProperty = Class(name="BPMNProfile::BPMNProperty")
BPMNProfile_ResourceRole = Class(name="BPMNProfile::ResourceRole")
BPMNProfile_CallableElement = Class(name="BPMNProfile::CallableElement", is_abstract=True)
RootElement = Class(name="RootElement")
BPMNProfile_Parameter = Class(name="BPMNProfile::Parameter")
BPMNProfile_ActivityParameterNode = Class(name="BPMNProfile::ActivityParameterNode")
BPMNProfile_ItemAwareElement = Class(name="BPMNProfile::ItemAwareElement", is_abstract=True)
BPMNProfile_DataState = Class(name="BPMNProfile::DataState")
BPMNProfile_TypedElement = Class(name="BPMNProfile::TypedElement")
BPMNProfile_ItemDefinition = Class(name="BPMNProfile::ItemDefinition")
BPMNProfile_State = Class(name="BPMNProfile::State")
BPMNProfile_InputPin = Class(name="BPMNProfile::InputPin")
BPMNProfile_ParameterSet = Class(name="BPMNProfile::ParameterSet")
BPMNProfile_OutputPin = Class(name="BPMNProfile::OutputPin")
BPMNProfile_Interface = Class(name="BPMNProfile::Interface")
BPMNProfile_BPMNOperation = Class(name="BPMNProfile::BPMNOperation")
BPMNProfile_Operation = Class(name="BPMNProfile::Operation")
BPMNProfile_BPMNMessage = Class(name="BPMNProfile::BPMNMessage")
BPMNProfile_ParticipantAssociation = Class(name="BPMNProfile::ParticipantAssociation")
BPMNProfile_ConversationLink = Class(name="BPMNProfile::ConversationLink")
BPMNProfile_MessageFlowAssociation = Class(name="BPMNProfile::MessageFlowAssociation")
BPMNProfile_MessageFlow = Class(name="BPMNProfile::MessageFlow")
BPMNProfile_Collaboration = Class(name="BPMNProfile::Collaboration")
BPMNProfile_ConversationNode = Class(name="BPMNProfile::ConversationNode", is_abstract=True)
BPMNProfile_Error = Class(name="BPMNProfile::Error")
ItemDefinition = Class(name="ItemDefinition")
InteractionNode = Class(name="InteractionNode")
BPMNProfile_CorrelationKey = Class(name="BPMNProfile::CorrelationKey")
BPMNProfile_Participant = Class(name="BPMNProfile::Participant")
BPMNProfile_ParticipantMultiplicity = Class(name="BPMNProfile::ParticipantMultiplicity")
BPMNProfile_PartnerEntity = Class(name="BPMNProfile::PartnerEntity")
BPMNProfile_PartnerRole = Class(name="BPMNProfile::PartnerRole")
BPMNProfile_InteractionNode = Class(name="BPMNProfile::InteractionNode", is_abstract=True)
BPMNProfile_MultiplicityElement = Class(name="BPMNProfile::MultiplicityElement")
BPMNProfile_InstanceSpecification = Class(name="BPMNProfile::InstanceSpecification")
BPMNProfile_InformationFlow = Class(name="BPMNProfile::InformationFlow")
BPMNProfile_CorrelationProperty = Class(name="BPMNProfile::CorrelationProperty")
BPMNProfile_CorrelationPropertyRetrievalExpression = Class(name="BPMNProfile::CorrelationPropertyRetrievalExpression")
BPMNProfile_FormalExpression = Class(name="BPMNProfile::FormalExpression")
BPMNExpression = Class(name="BPMNExpression")
BPMNProfile_CorrelationPropertyBinding = Class(name="BPMNProfile::CorrelationPropertyBinding")
BPMNProfile_DataStoreNode = Class(name="BPMNProfile::DataStoreNode")
BPMNProfile_ResourceAssignmentExpression = Class(name="BPMNProfile::ResourceAssignmentExpression")
BPMNProfile_Resource = Class(name="BPMNProfile::Resource")
BPMNProfile_ResourceParameterBinding = Class(name="BPMNProfile::ResourceParameterBinding")
BPMNProfile_ResourceParameter = Class(name="BPMNProfile::ResourceParameter")
BPMNProfile_GlobalScriptTask = Class(name="BPMNProfile::GlobalScriptTask")
GlobalTask = Class(name="GlobalTask")
BPMNProfile_OpaqueBehavior = Class(name="BPMNProfile::OpaqueBehavior")
BPMNProfile_GlobalBusinessRuleTask = Class(name="BPMNProfile::GlobalBusinessRuleTask")
BPMNProfile_CompensateEventDefinition = Class(name="BPMNProfile::CompensateEventDefinition")
EventDefinition = Class(name="EventDefinition")
BPMNProfile_BPMNActivity = Class(name="BPMNProfile::BPMNActivity", is_abstract=True)
BPMNProfile_CallEvent = Class(name="BPMNProfile::CallEvent")
BPMNProfile_EventDefinition = Class(name="BPMNProfile::EventDefinition", is_abstract=True)
BPMNProfile_Event = Class(name="BPMNProfile::Event")
BPMNProfile_GlobalTask = Class(name="BPMNProfile::GlobalTask")
BPMNProfile_BoundaryEvent = Class(name="BPMNProfile::BoundaryEvent")
BPMNProfile_DataInputAssociation = Class(name="BPMNProfile::DataInputAssociation")
BPMNProfile_DataOutputAssociation = Class(name="BPMNProfile::DataOutputAssociation")
BPMNProfile_LoopCharacteristics = Class(name="BPMNProfile::LoopCharacteristics", is_abstract=True)
CatchEvent = Class(name="CatchEvent")
BPMNProfile_CatchEvent = Class(name="BPMNProfile::CatchEvent", is_abstract=True)
BPMNEvent = Class(name="BPMNEvent")
BPMNProfile_AcceptEventAction = Class(name="BPMNProfile::AcceptEventAction")
BPMNProfile_InitialNode = Class(name="BPMNProfile::InitialNode")
BPMNProfile_BPMNEvent = Class(name="BPMNProfile::BPMNEvent", is_abstract=True)
DataAssociation = Class(name="DataAssociation")
BPMNProfile_DataAssociation = Class(name="BPMNProfile::DataAssociation", is_abstract=True)
BPMNProfile_ObjectFlow = Class(name="BPMNProfile::ObjectFlow")
BPMNProfile_Assignment = Class(name="BPMNProfile::Assignment")
BPMNProfile_EscalationEventDefinition = Class(name="BPMNProfile::EscalationEventDefinition")
BPMNProfile_Escalation = Class(name="BPMNProfile::Escalation")
BPMNProfile_TimerEventDefinition = Class(name="BPMNProfile::TimerEventDefinition")
BPMNProfile_ChangeEvent = Class(name="BPMNProfile::ChangeEvent")
BPMNProfile_SignalEventDefinition = Class(name="BPMNProfile::SignalEventDefinition")
BPMNProfile_BPMNSignal = Class(name="BPMNProfile::BPMNSignal")
BPMNProfile_EndEvent = Class(name="BPMNProfile::EndEvent")
ThrowEvent = Class(name="ThrowEvent")
BPMNProfile_FinalNode = Class(name="BPMNProfile::FinalNode")
BPMNProfile_ThrowEvent = Class(name="BPMNProfile::ThrowEvent", is_abstract=True)
BPMNProfile_CallOperationAction = Class(name="BPMNProfile::CallOperationAction")
BPMNProfile_FlowFinalNode = Class(name="BPMNProfile::FlowFinalNode")
BPMNProfile_MessageEventDefinition = Class(name="BPMNProfile::MessageEventDefinition")
BPMNProfile_StartEvent = Class(name="BPMNProfile::StartEvent")
BPMNProfile_ConditionalEventDefinition = Class(name="BPMNProfile::ConditionalEventDefinition")
BPMNProfile_LinkEventDefinition = Class(name="BPMNProfile::LinkEventDefinition")
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
BPMNProfile_Group = Class(name="BPMNProfile::Group")
BPMNProfile_DataObjectReference = Class(name="BPMNProfile::DataObjectReference")
BPMNProfile_DataObject = Class(name="BPMNProfile::DataObject")
BPMNProfile_DataStore = Class(name="BPMNProfile::DataStore")
BPMNProfile_DataStoreReference = Class(name="BPMNProfile::DataStoreReference")
BPMNProfile_UserTask = Class(name="BPMNProfile::UserTask")
Task = Class(name="Task")
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
BPMNProfile_GlobalManualTask = Class(name="BPMNProfile::GlobalManualTask")
BPMNProfile_ManualTask = Class(name="BPMNProfile::ManualTask")
BPMNProfile_PotentialOwner = Class(name="BPMNProfile::PotentialOwner")
BPMNProfile_GlobalConversation = Class(name="BPMNProfile::GlobalConversation")
BPMNCollaboration = Class(name="BPMNCollaboration")
BPMNProfile_CallConversation = Class(name="BPMNProfile::CallConversation")
BPMNProfile_CollaborationUse = Class(name="BPMNProfile::CollaborationUse")
HumanPerformer = Class(name="HumanPerformer")
BPMNProfile_SubConversation = Class(name="BPMNProfile::SubConversation")
ConversationNode = Class(name="ConversationNode")
BPMNProfile_CallActivity = Class(name="BPMNProfile::CallActivity")
BPMNProfile_CallBehaviorAction = Class(name="BPMNProfile::CallBehaviorAction")
BPMNProfile_BusinessRuleTask = Class(name="BPMNProfile::BusinessRuleTask")
BPMNProfile_Conversation = Class(name="BPMNProfile::Conversation")
BPMNProfile_SubProcess = Class(name="BPMNProfile::SubProcess")
BPMNProfile_ComplexBehaviorDefinition = Class(name="BPMNProfile::ComplexBehaviorDefinition")
BPMNProfile_AdHocSubProcess = Class(name="BPMNProfile::AdHocSubProcess")
SubProcess = Class(name="SubProcess")
BPMNProfile_ScriptTask = Class(name="BPMNProfile::ScriptTask")
BPMNProfile_SendTask = Class(name="BPMNProfile::SendTask")
BPMNProfile_Transaction = Class(name="BPMNProfile::Transaction")
BPMNProfile_StandardLoopCharacteristics = Class(name="BPMNProfile::StandardLoopCharacteristics")
LoopCharacteristics = Class(name="LoopCharacteristics")
BPMNProfile_LoopNode = Class(name="BPMNProfile::LoopNode")
BPMNProfile_ReceiveTask = Class(name="BPMNProfile::ReceiveTask")
BPMNProfile_ServiceTask = Class(name="BPMNProfile::ServiceTask")
BPMNProfile_MultiInstanceLoopCharacteristics = Class(name="BPMNProfile::MultiInstanceLoopCharacteristics")
BPMNProfile_ExpansionRegion = Class(name="BPMNProfile::ExpansionRegion")

# BPMNProfile_InclusiveGateway class attributes and methods
BPMNProfile_InclusiveGateway_m_inclusiveGatewaydefault: Method = Method(name="inclusiveGatewaydefault", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InclusiveGateway.methods={BPMNProfile_InclusiveGateway_m_inclusiveGatewaydefault}

# NonExclusiveGateway class attributes and methods

# BPMNProfile_SequenceFlow class attributes and methods
BPMNProfile_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=StringType)
BPMNProfile_SequenceFlow_m_SequenceFlowconditionExpression: Method = Method(name="SequenceFlowconditionExpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SequenceFlow_m_SequenceFlowsourceRef: Method = Method(name="SequenceFlowsourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SequenceFlow_m_SequenceFlowtargetRef: Method = Method(name="SequenceFlowtargetRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_SequenceFlow.attributes={BPMNProfile_SequenceFlow_isImmediate}
BPMNProfile_SequenceFlow.methods={BPMNProfile_SequenceFlow_m_SequenceFlowsourceRef, BPMNProfile_SequenceFlow_m_SequenceFlowconditionExpression, BPMNProfile_SequenceFlow_m_SequenceFlowtargetRef}

# BPMNProfile_NonExclusiveGateway class attributes and methods

# Gateway class attributes and methods

# BPMNProfile_JoinNode class attributes and methods

# BPMNProfile_ForkNode class attributes and methods

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

# BPMNProfile_ExtensionDefinition class attributes and methods

# BPMNProfile_BPMNAssociation class attributes and methods
BPMNProfile_BPMNAssociation_associationDirection: Property = Property(name="associationDirection", type=StringType)
BPMNProfile_BPMNAssociation_m_AssociationEnd: Method = Method(name="AssociationEnd", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNAssociation.attributes={BPMNProfile_BPMNAssociation_associationDirection}
BPMNProfile_BPMNAssociation.methods={BPMNProfile_BPMNAssociation_m_AssociationEnd}

# BPMNProfile_Property class attributes and methods

# BPMNProfile_Comment class attributes and methods

# BPMNProfile_Stereotype class attributes and methods

# BPMNArtifact class attributes and methods

# BPMNProfile_Dependency class attributes and methods

# BPMNProfile_BPMNArtifact class attributes and methods

# BPMNProfile_Class class attributes and methods

# BPMNProfile_Slot class attributes and methods

# BPMNProfile_ExtensionAttributeDefinition class attributes and methods
BPMNProfile_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
BPMNProfile_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=StringType)
BPMNProfile_ExtensionAttributeDefinition.attributes={BPMNProfile_ExtensionAttributeDefinition_type, BPMNProfile_ExtensionAttributeDefinition_isReference}

# BPMNProfile_LaneSet class attributes and methods
BPMNProfile_LaneSet_m_LaneSetlanes: Method = Method(name="LaneSetlanes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSetparentLane: Method = Method(name="LaneSetparentLane", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSetflowElementsContainer: Method = Method(name="LaneSetflowElementsContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet_m_LaneSet: Method = Method(name="LaneSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_LaneSet.methods={BPMNProfile_LaneSet_m_LaneSetlanes, BPMNProfile_LaneSet_m_LaneSet, BPMNProfile_LaneSet_m_LaneSetparentLane, BPMNProfile_LaneSet_m_LaneSetflowElementsContainer}

# BPMNProfile_ActivityPartition class attributes and methods

# BPMNProfile_Lane class attributes and methods
BPMNProfile_Lane_m_LanepartitionElementRef: Method = Method(name="LanepartitionElementRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Lane_m_LaneflowNodeRefs: Method = Method(name="LaneflowNodeRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Lane_m_LanelaneSet: Method = Method(name="LanelaneSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Lane_m_LanechildLaneSet: Method = Method(name="LanechildLaneSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Lane.methods={BPMNProfile_Lane_m_LanelaneSet, BPMNProfile_Lane_m_LaneflowNodeRefs, BPMNProfile_Lane_m_LanepartitionElementRef, BPMNProfile_Lane_m_LanechildLaneSet}

# BPMNProfile_EnumerationLiteral class attributes and methods

# BPMNProfile_OpaqueExpression class attributes and methods

# BPMNProfile_EventBasedGateway class attributes and methods
BPMNProfile_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=StringType)
BPMNProfile_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
BPMNProfile_EventBasedGateway.attributes={BPMNProfile_EventBasedGateway_eventGatewayType, BPMNProfile_EventBasedGateway_instantiate}

# BPMNProfile_StructuredActivityNode class attributes and methods

# BPMNProfile_InterruptibleActivityRegion class attributes and methods

# BPMNProfile_ParallelGateway class attributes and methods

# BPMNProfile_ComplexGateway class attributes and methods
BPMNProfile_ComplexGateway_m_complexGatewaydefault: Method = Method(name="complexGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ComplexGateway_m_complexGatewayactivationCondition: Method = Method(name="complexGatewayactivationCondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ComplexGateway_m_complexGatewayjoinSpec: Method = Method(name="complexGatewayjoinSpec", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ComplexGateway.methods={BPMNProfile_ComplexGateway_m_complexGatewayjoinSpec, BPMNProfile_ComplexGateway_m_complexGatewayactivationCondition, BPMNProfile_ComplexGateway_m_complexGatewaydefault}

# BPMNProfile_ControlFlow class attributes and methods

# BPMNProfile_BPMNExpression class attributes and methods

# BPMNProfile_MergeNode class attributes and methods

# BPMNProfile_RootElement class attributes and methods

# BPMNProfile_PackageableElement class attributes and methods

# BPMNProfile_Definitions class attributes and methods
BPMNProfile_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
BPMNProfile_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
BPMNProfile_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
BPMNProfile_Definitions_exporter: Property = Property(name="exporter", type=StringType)
BPMNProfile_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
BPMNProfile_Definitions.attributes={BPMNProfile_Definitions_targetNamespace, BPMNProfile_Definitions_typeLanguage, BPMNProfile_Definitions_exporter, BPMNProfile_Definitions_exporterVersion, BPMNProfile_Definitions_expressionLanguage}

# BPMNProfile_Package class attributes and methods

# BPMNProfile_BPMNExtension class attributes and methods
BPMNProfile_BPMNExtension_mustUnderstand: Property = Property(name="mustUnderstand", type=StringType)
BPMNProfile_BPMNExtension.attributes={BPMNProfile_BPMNExtension_mustUnderstand}

# BPMNProfile_Import class attributes and methods
BPMNProfile_Import_importType: Property = Property(name="importType", type=StringType)
BPMNProfile_Import_location: Property = Property(name="location", type=StringType)
BPMNProfile_Import_namespace: Property = Property(name="namespace", type=StringType)
BPMNProfile_Import.attributes={BPMNProfile_Import_namespace, BPMNProfile_Import_location, BPMNProfile_Import_importType}

# BPMNProfile_BPMNRelationship class attributes and methods
BPMNProfile_BPMNRelationship_type: Property = Property(name="type", type=StringType)
BPMNProfile_BPMNRelationship_direction: Property = Property(name="direction", type=StringType)
BPMNProfile_BPMNRelationship.attributes={BPMNProfile_BPMNRelationship_direction, BPMNProfile_BPMNRelationship_type}

# BPMNProfile_PackageImport class attributes and methods

# BPMNProfile_ExclusiveGateway class attributes and methods
BPMNProfile_ExclusiveGateway_m_exclusiveGatewaydefault: Method = Method(name="exclusiveGatewaydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ExclusiveGateway.methods={BPMNProfile_ExclusiveGateway_m_exclusiveGatewaydefault}

# BPMNProfile_DecisionNode class attributes and methods

# BPMNProfile_BPMNProcess class attributes and methods
BPMNProfile_BPMNProcess_processType: Property = Property(name="processType", type=StringType)
BPMNProfile_BPMNProcess_isClosed: Property = Property(name="isClosed", type=StringType)
BPMNProfile_BPMNProcess_isExecutable: Property = Property(name="isExecutable", type=StringType)
BPMNProfile_BPMNProcess_m_ProcesssupportedInterfaceRefs: Method = Method(name="ProcesssupportedInterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_Processsupports: Method = Method(name="Processsupports", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_Processproperties: Method = Method(name="Processproperties", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_ProcesslaneSets: Method = Method(name="ProcesslaneSets", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProcess_m_ProcessflowElements: Method = Method(name="ProcessflowElements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProcess.attributes={BPMNProfile_BPMNProcess_processType, BPMNProfile_BPMNProcess_isClosed, BPMNProfile_BPMNProcess_isExecutable}
BPMNProfile_BPMNProcess.methods={BPMNProfile_BPMNProcess_m_ProcesslaneSets, BPMNProfile_BPMNProcess_m_ProcesssupportedInterfaceRefs, BPMNProfile_BPMNProcess_m_ProcessflowElements, BPMNProfile_BPMNProcess_m_Processproperties, BPMNProfile_BPMNProcess_m_Processsupports}

# CallableElement class attributes and methods

# FlowElementsContainer class attributes and methods

# BPMNProfile_BPMNCollaboration class attributes and methods
BPMNProfile_BPMNCollaboration_isClosed: Property = Property(name="isClosed", type=StringType)
BPMNProfile_BPMNCollaboration_m_Collaborationparticipants: Method = Method(name="Collaborationparticipants", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNCollaboration.attributes={BPMNProfile_BPMNCollaboration_isClosed}
BPMNProfile_BPMNCollaboration.methods={BPMNProfile_BPMNCollaboration_m_Collaborationparticipants}

# BPMNProfile_Activity class attributes and methods

# BPMNProfile_CorrelationSubscription class attributes and methods

# BPMNProfile_Constraint class attributes and methods

# BPMNProfile_Behavior class attributes and methods

# BPMNProfile_InputOutputSpecification class attributes and methods

# BPMNProfile_BPMNInterface class attributes and methods
BPMNProfile_BPMNInterface_m_Interfaceoperationmultiplicity: Method = Method(name="Interfaceoperationmultiplicity", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_BPMNInterfaceoperations: Method = Method(name="BPMNInterfaceoperations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_InterfaceownedOperation: Method = Method(name="InterfaceownedOperation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNInterface_m_BPMNInterfacecallableElements: Method = Method(name="BPMNInterfacecallableElements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNInterface.methods={BPMNProfile_BPMNInterface_m_BPMNInterfacecallableElements, BPMNProfile_BPMNInterface_m_InterfaceownedOperation, BPMNProfile_BPMNInterface_m_Interfaceoperationmultiplicity, BPMNProfile_BPMNInterface_m_BPMNInterfaceoperations}

# BPMNProfile_InputOutputBinding class attributes and methods

# BPMNProfile_Action class attributes and methods

# BPMNProfile_DataInput class attributes and methods
BPMNProfile_DataInput_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataInput_m_DataInputAssociation: Method = Method(name="DataInputAssociation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInput_m_DataInputnotation: Method = Method(name="DataInputnotation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInput_m_DataInputitemSubjectRef: Method = Method(name="DataInputitemSubjectRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInput.attributes={BPMNProfile_DataInput_isCollection}
BPMNProfile_DataInput.methods={BPMNProfile_DataInput_m_DataInputAssociation, BPMNProfile_DataInput_m_DataInputnotation, BPMNProfile_DataInput_m_DataInputitemSubjectRef}

# BPMNProfile_DataOutput class attributes and methods
BPMNProfile_DataOutput_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataOutput_m_DataOutputnotation: Method = Method(name="DataOutputnotation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataOutput_m_DataOutputitemSubjectRef: Method = Method(name="DataOutputitemSubjectRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataOutput.attributes={BPMNProfile_DataOutput_isCollection}
BPMNProfile_DataOutput.methods={BPMNProfile_DataOutput_m_DataOutputnotation, BPMNProfile_DataOutput_m_DataOutputitemSubjectRef}

# BPMNProfile_InputSet class attributes and methods
BPMNProfile_InputSet_m_InputSetdataInputRefs: Method = Method(name="InputSetdataInputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InputSet_m_InputSetoptionalInputRefs: Method = Method(name="InputSetoptionalInputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_InputSet_m_InputSetwhileExecutingInputRefs: Method = Method(name="InputSetwhileExecutingInputRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_InputSet.methods={BPMNProfile_InputSet_m_InputSetdataInputRefs, BPMNProfile_InputSet_m_InputSetwhileExecutingInputRefs, BPMNProfile_InputSet_m_InputSetoptionalInputRefs}

# BPMNProfile_OutputSet class attributes and methods
BPMNProfile_OutputSet_m_OutputSetdataOutputRefs: Method = Method(name="OutputSetdataOutputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_OutputSet_m_OutputSetoptionalOutputRefs: Method = Method(name="OutputSetoptionalOutputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_OutputSet_m_OutputSetwhileExecutingOutputRefs: Method = Method(name="OutputSetwhileExecutingOutputRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_OutputSet.methods={BPMNProfile_OutputSet_m_OutputSetoptionalOutputRefs, BPMNProfile_OutputSet_m_OutputSetdataOutputRefs, BPMNProfile_OutputSet_m_OutputSetwhileExecutingOutputRefs}

# ItemAwareElement class attributes and methods

# BPMNProfile_BPMNProperty class attributes and methods
BPMNProfile_BPMNProperty_m_Propertynotation: Method = Method(name="Propertynotation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNProperty_m_BPMNPropertyapply: Method = Method(name="BPMNPropertyapply", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNProperty.methods={BPMNProfile_BPMNProperty_m_Propertynotation, BPMNProfile_BPMNProperty_m_BPMNPropertyapply}

# BPMNProfile_ResourceRole class attributes and methods
BPMNProfile_ResourceRole_m_ResourceRoleowner: Method = Method(name="ResourceRoleowner", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleresourceRef: Method = Method(name="ResourceRoleresourceRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleisRequired: Method = Method(name="ResourceRoleisRequired", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleprocess: Method = Method(name="ResourceRoleprocess", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceRole_m_ResourceRoleresourceParameterBindings: Method = Method(name="ResourceRoleresourceParameterBindings", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceRole.methods={BPMNProfile_ResourceRole_m_ResourceRoleprocess, BPMNProfile_ResourceRole_m_ResourceRoleresourceRef, BPMNProfile_ResourceRole_m_ResourceRoleowner, BPMNProfile_ResourceRole_m_ResourceRoleisRequired, BPMNProfile_ResourceRole_m_ResourceRoleresourceParameterBindings}

# BPMNProfile_CallableElement class attributes and methods
BPMNProfile_CallableElement_m_CallableEelementsupportedInterfaceRefs: Method = Method(name="CallableEelementsupportedInterfaceRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallableElement_m_CallableElementresources: Method = Method(name="CallableElementresources", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallableElement.methods={BPMNProfile_CallableElement_m_CallableEelementsupportedInterfaceRefs, BPMNProfile_CallableElement_m_CallableElementresources}

# RootElement class attributes and methods

# BPMNProfile_Parameter class attributes and methods

# BPMNProfile_ActivityParameterNode class attributes and methods

# BPMNProfile_ItemAwareElement class attributes and methods
BPMNProfile_ItemAwareElement_m_ItemAwareElementdataState: Method = Method(name="ItemAwareElementdataState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ItemAwareElement.methods={BPMNProfile_ItemAwareElement_m_ItemAwareElementdataState}

# BPMNProfile_DataState class attributes and methods

# BPMNProfile_TypedElement class attributes and methods

# BPMNProfile_ItemDefinition class attributes and methods
BPMNProfile_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
BPMNProfile_ItemDefinition_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_ItemDefinition_m_ItemDefinitionstructureRef: Method = Method(name="ItemDefinitionstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ItemDefinition.attributes={BPMNProfile_ItemDefinition_isCollection, BPMNProfile_ItemDefinition_itemKind}
BPMNProfile_ItemDefinition.methods={BPMNProfile_ItemDefinition_m_ItemDefinitionstructureRef}

# BPMNProfile_State class attributes and methods

# BPMNProfile_InputPin class attributes and methods

# BPMNProfile_ParameterSet class attributes and methods

# BPMNProfile_OutputPin class attributes and methods

# BPMNProfile_Interface class attributes and methods

# BPMNProfile_BPMNOperation class attributes and methods
BPMNProfile_BPMNOperation_m_BPMNOperationowner: Method = Method(name="BPMNOperationowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationinMessageRef: Method = Method(name="BPMNOperationinMessageRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationoutMessageRef: Method = Method(name="BPMNOperationoutMessageRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNOperation_m_BPMNOperationerrorRefs: Method = Method(name="BPMNOperationerrorRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNOperation.methods={BPMNProfile_BPMNOperation_m_BPMNOperationinMessageRef, BPMNProfile_BPMNOperation_m_BPMNOperationowner, BPMNProfile_BPMNOperation_m_BPMNOperationerrorRefs, BPMNProfile_BPMNOperation_m_BPMNOperationoutMessageRef}

# BPMNProfile_Operation class attributes and methods

# BPMNProfile_BPMNMessage class attributes and methods
BPMNProfile_BPMNMessage_m_MessageitemRef: Method = Method(name="MessageitemRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNMessage.methods={BPMNProfile_BPMNMessage_m_MessageitemRef}

# BPMNProfile_ParticipantAssociation class attributes and methods
BPMNProfile_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef: Method = Method(name="ParticipantAssociationouterParticipantRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef: Method = Method(name="ParticipantAssociationinnerParticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ParticipantAssociation.methods={BPMNProfile_ParticipantAssociation_m_ParticipantAssociationouterParticipantRef, BPMNProfile_ParticipantAssociation_m_ParticipantAssociationinnerParticipantRef}

# BPMNProfile_ConversationLink class attributes and methods

# BPMNProfile_MessageFlowAssociation class attributes and methods
BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef: Method = Method(name="MessageFlowAssociationinnerMessageFlowRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef: Method = Method(name="MessageFlowAssociationouterMessageFlowRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlowAssociation.methods={BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationouterMessageFlowRef, BPMNProfile_MessageFlowAssociation_m_MessageFlowAssociationinnerMessageFlowRef}

# BPMNProfile_MessageFlow class attributes and methods
BPMNProfile_MessageFlow_m_MessageFlowsourceRef: Method = Method(name="MessageFlowsourceRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_MessageFlow_m_MessageFlowtargetRef: Method = Method(name="MessageFlowtargetRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MessageFlow_m_MessageFlowmessageRef: Method = Method(name="MessageFlowmessageRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_MessageFlow.methods={BPMNProfile_MessageFlow_m_MessageFlowmessageRef, BPMNProfile_MessageFlow_m_MessageFlowsourceRef, BPMNProfile_MessageFlow_m_MessageFlowtargetRef}

# BPMNProfile_Collaboration class attributes and methods

# BPMNProfile_ConversationNode class attributes and methods
BPMNProfile_ConversationNode_m_ConversationNodeparticipantRefs: Method = Method(name="ConversationNodeparticipantRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ConversationNode.methods={BPMNProfile_ConversationNode_m_ConversationNodeparticipantRefs}

# BPMNProfile_Error class attributes and methods
BPMNProfile_Error_errorCode: Property = Property(name="errorCode", type=StringType)
BPMNProfile_Error.attributes={BPMNProfile_Error_errorCode}

# ItemDefinition class attributes and methods

# InteractionNode class attributes and methods

# BPMNProfile_CorrelationKey class attributes and methods

# BPMNProfile_Participant class attributes and methods
BPMNProfile_Participant_m_Participantownership: Method = Method(name="Participantownership", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_Participanttype: Method = Method(name="Participanttype", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantmultiplicityMinimum: Method = Method(name="ParticipantmultiplicityMinimum", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_Participantrealizationsupplier: Method = Method(name="Participantrealizationsupplier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantprocessRef: Method = Method(name="ParticipantprocessRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantmultiplicityMaximum: Method = Method(name="ParticipantmultiplicityMaximum", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_ParticipantinterfaceRefs: Method = Method(name="ParticipantinterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_Participant_m_participantpartnerEntityRef: Method = Method(name="participantpartnerEntityRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant_m_participantpartnerRoleRef: Method = Method(name="participantpartnerRoleRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Participant.methods={BPMNProfile_Participant_m_participantpartnerEntityRef, BPMNProfile_Participant_m_Participantrealizationsupplier, BPMNProfile_Participant_m_Participantownership, BPMNProfile_Participant_m_ParticipantinterfaceRefs, BPMNProfile_Participant_m_ParticipantmultiplicityMaximum, BPMNProfile_Participant_m_Participanttype, BPMNProfile_Participant_m_participantpartnerRoleRef, BPMNProfile_Participant_m_ParticipantmultiplicityMinimum, BPMNProfile_Participant_m_ParticipantprocessRef}

# BPMNProfile_ParticipantMultiplicity class attributes and methods
BPMNProfile_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=StringType)
BPMNProfile_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=StringType)
BPMNProfile_ParticipantMultiplicity.attributes={BPMNProfile_ParticipantMultiplicity_minimum, BPMNProfile_ParticipantMultiplicity_maximum}

# BPMNProfile_PartnerEntity class attributes and methods
BPMNProfile_PartnerEntity_m_PartnerEntityparticipantRef: Method = Method(name="PartnerEntityparticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_PartnerEntity.methods={BPMNProfile_PartnerEntity_m_PartnerEntityparticipantRef}

# BPMNProfile_PartnerRole class attributes and methods
BPMNProfile_PartnerRole_m_PartnerRoleparticipantRef: Method = Method(name="PartnerRoleparticipantRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_PartnerRole.methods={BPMNProfile_PartnerRole_m_PartnerRoleparticipantRef}

# BPMNProfile_InteractionNode class attributes and methods

# BPMNProfile_MultiplicityElement class attributes and methods

# BPMNProfile_InstanceSpecification class attributes and methods

# BPMNProfile_InformationFlow class attributes and methods

# BPMNProfile_CorrelationProperty class attributes and methods

# BPMNProfile_CorrelationPropertyRetrievalExpression class attributes and methods

# BPMNProfile_FormalExpression class attributes and methods
BPMNProfile_FormalExpression_m_FormalExpressionevaluatesToTypeRef: Method = Method(name="FormalExpressionevaluatesToTypeRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_FormalExpression.methods={BPMNProfile_FormalExpression_m_FormalExpressionevaluatesToTypeRef}

# BPMNExpression class attributes and methods

# BPMNProfile_CorrelationPropertyBinding class attributes and methods

# BPMNProfile_DataStoreNode class attributes and methods

# BPMNProfile_ResourceAssignmentExpression class attributes and methods
BPMNProfile_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression: Method = Method(name="ResourceAssignmentExpressionexpression", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceAssignmentExpression.methods={BPMNProfile_ResourceAssignmentExpression_m_ResourceAssignmentExpressionexpression}

# BPMNProfile_Resource class attributes and methods
BPMNProfile_Resource_m_ResourceresourceParameters: Method = Method(name="ResourceresourceParameters", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Resource.methods={BPMNProfile_Resource_m_ResourceresourceParameters}

# BPMNProfile_ResourceParameterBinding class attributes and methods
BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingexpression: Method = Method(name="ResourceParameterBindingexpression", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingparameterRef: Method = Method(name="ResourceParameterBindingparameterRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameterBinding.methods={BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingexpression, BPMNProfile_ResourceParameterBinding_m_ResourceParameterBindingparameterRef}

# BPMNProfile_ResourceParameter class attributes and methods
BPMNProfile_ResourceParameter_isRequired: Property = Property(name="isRequired", type=StringType)
BPMNProfile_ResourceParameter_m_ResourceParameterowner: Method = Method(name="ResourceParameterowner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ResourceParameter_m_ResourceParametertype: Method = Method(name="ResourceParametertype", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceParameter_m_ResourceParameterisRequired: Method = Method(name="ResourceParameterisRequired", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ResourceParameter.attributes={BPMNProfile_ResourceParameter_isRequired}
BPMNProfile_ResourceParameter.methods={BPMNProfile_ResourceParameter_m_ResourceParameterowner, BPMNProfile_ResourceParameter_m_ResourceParameterisRequired, BPMNProfile_ResourceParameter_m_ResourceParametertype}

# BPMNProfile_GlobalScriptTask class attributes and methods
BPMNProfile_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
BPMNProfile_GlobalScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscriptFormat: Method = Method(name="GlobalScriptTaskscriptFormat", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscript: Method = Method(name="GlobalScriptTaskscript", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalScriptTask.attributes={BPMNProfile_GlobalScriptTask_script, BPMNProfile_GlobalScriptTask_scriptFormat}
BPMNProfile_GlobalScriptTask.methods={BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscript, BPMNProfile_GlobalScriptTask_m_GlobalScriptTaskscriptFormat}

# GlobalTask class attributes and methods

# BPMNProfile_OpaqueBehavior class attributes and methods

# BPMNProfile_GlobalBusinessRuleTask class attributes and methods
BPMNProfile_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation: Method = Method(name="GlobalBusinessRuleTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalBusinessRuleTask.attributes={BPMNProfile_GlobalBusinessRuleTask_implementation}
BPMNProfile_GlobalBusinessRuleTask.methods={BPMNProfile_GlobalBusinessRuleTask_m_GlobalBusinessRuleTaskimplementation}

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
BPMNProfile_BPMNActivity_m_BPMNActivityproperties: Method = Method(name="BPMNActivityproperties", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivityloopCharacteristics: Method = Method(name="BPMNActivityloopCharacteristics", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivitydefault: Method = Method(name="BPMNActivitydefault", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNActivity_m_BPMNActivityboundaryEventsRefs: Method = Method(name="BPMNActivityboundaryEventsRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BPMNActivity.attributes={BPMNProfile_BPMNActivity_completionQuantity, BPMNProfile_BPMNActivity_startQuantity, BPMNProfile_BPMNActivity_isForCompensation}
BPMNProfile_BPMNActivity.methods={BPMNProfile_BPMNActivity_m_BPMNActivityloopCharacteristics, BPMNProfile_BPMNActivity_m_BPMNActivityproperties, BPMNProfile_BPMNActivity_m_BPMNActivityboundaryEventsRefs, BPMNProfile_BPMNActivity_m_BPMNActivityresources, BPMNProfile_BPMNActivity_m_BPMNActivitydefault, BPMNProfile_BPMNActivity_m_BPMNActivitycontainer}

# BPMNProfile_CallEvent class attributes and methods

# BPMNProfile_EventDefinition class attributes and methods

# BPMNProfile_Event class attributes and methods

# BPMNProfile_GlobalTask class attributes and methods
BPMNProfile_GlobalTask_m_GlobalTasksupportedInterfaceRefs: Method = Method(name="GlobalTasksupportedInterfaceRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_GlobalTask.methods={BPMNProfile_GlobalTask_m_GlobalTasksupportedInterfaceRefs}

# BPMNProfile_BoundaryEvent class attributes and methods
BPMNProfile_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=StringType)
BPMNProfile_BoundaryEvent_m_boundaryEventattachedToRef: Method = Method(name="boundaryEventattachedToRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BoundaryEvent.attributes={BPMNProfile_BoundaryEvent_cancelActivity}
BPMNProfile_BoundaryEvent.methods={BPMNProfile_BoundaryEvent_m_boundaryEventattachedToRef}

# BPMNProfile_DataInputAssociation class attributes and methods
BPMNProfile_DataInputAssociation_m_dataInputAssociationsource: Method = Method(name="dataInputAssociationsource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInputAssociation_m_dataInputAssociationtarget: Method = Method(name="dataInputAssociationtarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataInputAssociation.methods={BPMNProfile_DataInputAssociation_m_dataInputAssociationsource, BPMNProfile_DataInputAssociation_m_dataInputAssociationtarget}

# BPMNProfile_DataOutputAssociation class attributes and methods
BPMNProfile_DataOutputAssociation_m_dataOutputAssociationsource: Method = Method(name="dataOutputAssociationsource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataOutputAssociation_m_dataOutputAssociationtarget: Method = Method(name="dataOutputAssociationtarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataOutputAssociation.methods={BPMNProfile_DataOutputAssociation_m_dataOutputAssociationtarget, BPMNProfile_DataOutputAssociation_m_dataOutputAssociationsource}

# BPMNProfile_LoopCharacteristics class attributes and methods

# CatchEvent class attributes and methods

# BPMNProfile_CatchEvent class attributes and methods
BPMNProfile_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=StringType)
BPMNProfile_CatchEvent_m_catchEventeventDefinitionsRefs: Method = Method(name="catchEventeventDefinitionsRefs", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CatchEvent.attributes={BPMNProfile_CatchEvent_parallelMultiple}
BPMNProfile_CatchEvent.methods={BPMNProfile_CatchEvent_m_catchEventeventDefinitionsRefs}

# BPMNEvent class attributes and methods

# BPMNProfile_AcceptEventAction class attributes and methods

# BPMNProfile_InitialNode class attributes and methods

# BPMNProfile_BPMNEvent class attributes and methods

# DataAssociation class attributes and methods

# BPMNProfile_DataAssociation class attributes and methods
BPMNProfile_DataAssociation_m_DataAssociationsource: Method = Method(name="DataAssociationsource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataAssociation_m_DataAssociationtransformation: Method = Method(name="DataAssociationtransformation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataAssociation_m_DataAssociationtarget: Method = Method(name="DataAssociationtarget", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataAssociation.methods={BPMNProfile_DataAssociation_m_DataAssociationtarget, BPMNProfile_DataAssociation_m_DataAssociationtransformation, BPMNProfile_DataAssociation_m_DataAssociationsource}

# BPMNProfile_ObjectFlow class attributes and methods

# BPMNProfile_Assignment class attributes and methods

# BPMNProfile_EscalationEventDefinition class attributes and methods

# BPMNProfile_Escalation class attributes and methods
BPMNProfile_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
BPMNProfile_Escalation_m_EscalationstructureRef: Method = Method(name="EscalationstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_Escalation.attributes={BPMNProfile_Escalation_escalationCode}
BPMNProfile_Escalation.methods={BPMNProfile_Escalation_m_EscalationstructureRef}

# BPMNProfile_TimerEventDefinition class attributes and methods

# BPMNProfile_ChangeEvent class attributes and methods

# BPMNProfile_SignalEventDefinition class attributes and methods

# BPMNProfile_BPMNSignal class attributes and methods
BPMNProfile_BPMNSignal_m_BPMNSignalstructureRef: Method = Method(name="BPMNSignalstructureRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_BPMNSignal.methods={BPMNProfile_BPMNSignal_m_BPMNSignalstructureRef}

# BPMNProfile_EndEvent class attributes and methods

# ThrowEvent class attributes and methods

# BPMNProfile_FinalNode class attributes and methods

# BPMNProfile_ThrowEvent class attributes and methods
BPMNProfile_ThrowEvent_m_ThrowEventeventDefinitionRefs: Method = Method(name="ThrowEventeventDefinitionRefs", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ThrowEvent.methods={BPMNProfile_ThrowEvent_m_ThrowEventeventDefinitionRefs}

# BPMNProfile_CallOperationAction class attributes and methods

# BPMNProfile_FlowFinalNode class attributes and methods

# BPMNProfile_MessageEventDefinition class attributes and methods

# BPMNProfile_StartEvent class attributes and methods
BPMNProfile_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=StringType)
BPMNProfile_StartEvent.attributes={BPMNProfile_StartEvent_isInterrupting}

# BPMNProfile_ConditionalEventDefinition class attributes and methods
BPMNProfile_ConditionalEventDefinition_m_conditionalEventDefinitioncondition: Method = Method(name="conditionalEventDefinitioncondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ConditionalEventDefinition.methods={BPMNProfile_ConditionalEventDefinition_m_conditionalEventDefinitioncondition}

# BPMNProfile_LinkEventDefinition class attributes and methods

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
BPMNProfile_TextAnnotation.attributes={BPMNProfile_TextAnnotation_textFormat, BPMNProfile_TextAnnotation_text}

# BPMNProfile_Category class attributes and methods

# BPMNProfile_Enumeration class attributes and methods

# BPMNProfile_Group class attributes and methods

# BPMNProfile_DataObjectReference class attributes and methods
BPMNProfile_DataObjectReference_m_DataObjectRefsourcetarget: Method = Method(name="DataObjectRefsourcetarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataObjectReference_m_DataObjectRefdataState: Method = Method(name="DataObjectRefdataState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_DataObjectReference.methods={BPMNProfile_DataObjectReference_m_DataObjectRefdataState, BPMNProfile_DataObjectReference_m_DataObjectRefsourcetarget}

# BPMNProfile_DataObject class attributes and methods
BPMNProfile_DataObject_isCollection: Property = Property(name="isCollection", type=StringType)
BPMNProfile_DataObject_m_DataObjectdataState: Method = Method(name="DataObjectdataState", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_DataObject.attributes={BPMNProfile_DataObject_isCollection}
BPMNProfile_DataObject.methods={BPMNProfile_DataObject_m_DataObjectdataState}

# BPMNProfile_DataStore class attributes and methods
BPMNProfile_DataStore_capacity: Property = Property(name="capacity", type=StringType)
BPMNProfile_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=StringType)
BPMNProfile_DataStore.attributes={BPMNProfile_DataStore_isUnlimited, BPMNProfile_DataStore_capacity}

# BPMNProfile_DataStoreReference class attributes and methods

# BPMNProfile_UserTask class attributes and methods
BPMNProfile_UserTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_UserTask_m_UserTaskimplementation: Method = Method(name="UserTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_UserTask_m_UserTaskrenderings: Method = Method(name="UserTaskrenderings", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_UserTask.attributes={BPMNProfile_UserTask_implementation}
BPMNProfile_UserTask.methods={BPMNProfile_UserTask_m_UserTaskimplementation, BPMNProfile_UserTask_m_UserTaskrenderings}

# Task class attributes and methods

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
BPMNProfile_GlobalUserTask_m_GlobalUserTaskimplementation: Method = Method(name="GlobalUserTaskimplementation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalUserTask.attributes={BPMNProfile_GlobalUserTask_implementation}
BPMNProfile_GlobalUserTask.methods={BPMNProfile_GlobalUserTask_m_GlobalUserTaskimplementation, BPMNProfile_GlobalUserTask_m_GlobalUserTaskrenderings}

# BPMNProfile_GlobalManualTask class attributes and methods

# BPMNProfile_ManualTask class attributes and methods

# BPMNProfile_PotentialOwner class attributes and methods

# BPMNProfile_GlobalConversation class attributes and methods
BPMNProfile_GlobalConversation_m_GlobalConversationcontainedelements: Method = Method(name="GlobalConversationcontainedelements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_GlobalConversation.methods={BPMNProfile_GlobalConversation_m_GlobalConversationcontainedelements}

# BPMNCollaboration class attributes and methods

# BPMNProfile_CallConversation class attributes and methods
BPMNProfile_CallConversation_m_CallConversationcalledCollaborationRef: Method = Method(name="CallConversationcalledCollaborationRef", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallConversation_m_CallConversationparticipantAssociations: Method = Method(name="CallConversationparticipantAssociations", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallConversation.methods={BPMNProfile_CallConversation_m_CallConversationparticipantAssociations, BPMNProfile_CallConversation_m_CallConversationcalledCollaborationRef}

# BPMNProfile_CollaborationUse class attributes and methods

# HumanPerformer class attributes and methods

# BPMNProfile_SubConversation class attributes and methods
BPMNProfile_SubConversation_m_SubConversationconnectedelements: Method = Method(name="SubConversationconnectedelements", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_SubConversation.methods={BPMNProfile_SubConversation_m_SubConversationconnectedelements}

# ConversationNode class attributes and methods

# BPMNProfile_CallActivity class attributes and methods
BPMNProfile_CallActivity_m_CallActivitycalledElementRefvalues: Method = Method(name="CallActivitycalledElementRefvalues", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_CallActivity.methods={BPMNProfile_CallActivity_m_CallActivitycalledElementRefvalues}

# BPMNProfile_CallBehaviorAction class attributes and methods

# BPMNProfile_BusinessRuleTask class attributes and methods
BPMNProfile_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_BusinessRuleTask_m_BusinessRuleTaskimplementation: Method = Method(name="BusinessRuleTaskimplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_BusinessRuleTask.attributes={BPMNProfile_BusinessRuleTask_implementation}
BPMNProfile_BusinessRuleTask.methods={BPMNProfile_BusinessRuleTask_m_BusinessRuleTaskimplementation}

# BPMNProfile_Conversation class attributes and methods

# BPMNProfile_SubProcess class attributes and methods
BPMNProfile_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=StringType)
BPMNProfile_SubProcess_m_SubProcesstriggeredByEvent: Method = Method(name="SubProcesstriggeredByEvent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_SubProcess.attributes={BPMNProfile_SubProcess_triggeredByEvent}
BPMNProfile_SubProcess.methods={BPMNProfile_SubProcess_m_SubProcesstriggeredByEvent}

# BPMNProfile_ComplexBehaviorDefinition class attributes and methods

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
BPMNProfile_ScriptTask_m_ScriptTaskscript: Method = Method(name="ScriptTaskscript", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ScriptTask.attributes={BPMNProfile_ScriptTask_script, BPMNProfile_ScriptTask_scriptFormat}
BPMNProfile_ScriptTask.methods={BPMNProfile_ScriptTask_m_ScriptTaskscript, BPMNProfile_ScriptTask_m_ScriptTaskscriptFormat}

# BPMNProfile_SendTask class attributes and methods
BPMNProfile_SendTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_SendTask_m_SendTaskoperationRef: Method = Method(name="SendTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_SendTask.attributes={BPMNProfile_SendTask_implementation}
BPMNProfile_SendTask.methods={BPMNProfile_SendTask_m_SendTaskoperationRef}

# BPMNProfile_Transaction class attributes and methods
BPMNProfile_Transaction_method: Property = Property(name="method", type=StringType)
BPMNProfile_Transaction.attributes={BPMNProfile_Transaction_method}

# BPMNProfile_StandardLoopCharacteristics class attributes and methods
BPMNProfile_StandardLoopCharacteristics_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
BPMNProfile_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=StringType)
BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore: Method = Method(name="StandardLoopCharacteristicstestBefore", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition: Method = Method(name="StandardLoopCharacteristicsloopCondition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_StandardLoopCharacteristics.attributes={BPMNProfile_StandardLoopCharacteristics_loopMaximum, BPMNProfile_StandardLoopCharacteristics_testBefore}
BPMNProfile_StandardLoopCharacteristics.methods={BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicsloopCondition, BPMNProfile_StandardLoopCharacteristics_m_StandardLoopCharacteristicstestBefore}

# LoopCharacteristics class attributes and methods

# BPMNProfile_LoopNode class attributes and methods

# BPMNProfile_ReceiveTask class attributes and methods
BPMNProfile_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_ReceiveTask_instantiate: Property = Property(name="instantiate", type=StringType)
BPMNProfile_ReceiveTask_m_ReceiveTaskoperationRef: Method = Method(name="ReceiveTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ReceiveTask.attributes={BPMNProfile_ReceiveTask_instantiate, BPMNProfile_ReceiveTask_implementation}
BPMNProfile_ReceiveTask.methods={BPMNProfile_ReceiveTask_m_ReceiveTaskoperationRef}

# BPMNProfile_ServiceTask class attributes and methods
BPMNProfile_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
BPMNProfile_ServiceTask_m_ServiceTaskinputSet: Method = Method(name="ServiceTaskinputSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ServiceTask_m_ServiceTaskoutputSet: Method = Method(name="ServiceTaskoutputSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_ServiceTask_m_ServiceTaskoperationRef: Method = Method(name="ServiceTaskoperationRef", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
BPMNProfile_ServiceTask.attributes={BPMNProfile_ServiceTask_implementation}
BPMNProfile_ServiceTask.methods={BPMNProfile_ServiceTask_m_ServiceTaskinputSet, BPMNProfile_ServiceTask_m_ServiceTaskoutputSet, BPMNProfile_ServiceTask_m_ServiceTaskoperationRef}

# BPMNProfile_MultiInstanceLoopCharacteristics class attributes and methods
BPMNProfile_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
BPMNProfile_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=StringType)
BPMNProfile_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget: Method = Method(name="MultiinstanceLoopCharacteristicstarget", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
BPMNProfile_MultiInstanceLoopCharacteristics.attributes={BPMNProfile_MultiInstanceLoopCharacteristics_behavior, BPMNProfile_MultiInstanceLoopCharacteristics_isSequential}
BPMNProfile_MultiInstanceLoopCharacteristics.methods={BPMNProfile_MultiInstanceLoopCharacteristics_m_MultiinstanceLoopCharacteristicstarget}

# BPMNProfile_ExpansionRegion class attributes and methods

# Relationships
default0: BinaryAssociation = BinaryAssociation(
    name="default0",
    ends={
        Property(name="BPMNProfile_SequenceFlow", type=BPMNProfile_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InclusiveGateway", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
base_JoinNode1: BinaryAssociation = BinaryAssociation(
    name="base_JoinNode1",
    ends={
        Property(name="BPMNProfile_JoinNode", type=BPMNProfile_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_NonExclusiveGateway", type=BPMNProfile_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
base_ForkNode2: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode2",
    ends={
        Property(name="BPMNProfile_ForkNode", type=BPMNProfile_NonExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_NonExclusiveGateway3", type=BPMNProfile_ForkNode, multiplicity=Multiplicity(0, 1))
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
        Property(name="BPMNProfile_Gateway6", type=BPMNProfile_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
base_ActivityNode7: BinaryAssociation = BinaryAssociation(
    name="base_ActivityNode7",
    ends={
        Property(name="BPMNProfile_ActivityNode", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FlowNode", type=BPMNProfile_ActivityNode, multiplicity=Multiplicity(0, 1))
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
        Property(name="categorizedFlowElements", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(0, 9999))
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
        Property(name="BPMNProfile_BaseElement", type=BPMNProfile_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999))
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
        Property(name="BPMNProfile_BaseElement17", type=BPMNProfile_Documentation, multiplicity=Multiplicity(0, 9999))
    }
)
extensionDefinitions18: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions18",
    ends={
        Property(name="BPMNProfile_ExtensionDefinition", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BaseElement19", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing20: BinaryAssociation = BinaryAssociation(
    name="outgoing20",
    ends={
        Property(name="BPMNAssociation", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="BPMNAssociation22", type=BPMNProfile_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=BPMNProfile_BPMNAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property30: BinaryAssociation = BinaryAssociation(
    name="base_Property30",
    ends={
        Property(name="BPMNProfile_Property", type=BPMNProfile_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExtensionAttributeDefinition31", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment32: BinaryAssociation = BinaryAssociation(
    name="base_Comment32",
    ends={
        Property(name="BPMNProfile_Comment", type=BPMNProfile_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Documentation33", type=BPMNProfile_Comment, multiplicity=Multiplicity(1, 1))
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
        Property(name="BPMNProfile_ExtensionDefinition37", type=BPMNProfile_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 9999))
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
laneSets50: BinaryAssociation = BinaryAssociation(
    name="laneSets50",
    ends={
        Property(name="LaneSet", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="flowElementsContainer", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(0, 9999))
    }
)
flowElements51: BinaryAssociation = BinaryAssociation(
    name="flowElements51",
    ends={
        Property(name="FlowElement52", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(0, 9999))
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
        Property(name="laneSet", type=BPMNProfile_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
parentLane55: BinaryAssociation = BinaryAssociation(
    name="parentLane55",
    ends={
        Property(name="BPMNProfile_Lane", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LaneSet56", type=BPMNProfile_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
flowElementsContainer57: BinaryAssociation = BinaryAssociation(
    name="flowElementsContainer57",
    ends={
        Property(name="FlowElementsContainer58", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="laneSets", type=BPMNProfile_FlowElementsContainer, multiplicity=Multiplicity(0, 1))
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
        Property(name="_categoryValueRef", type=BPMNProfile_FlowElement, multiplicity=Multiplicity(0, 9999))
    }
)
base_ActivityPartition59: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition59",
    ends={
        Property(name="BPMNProfile_ActivityPartition61", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Lane60", type=BPMNProfile_ActivityPartition, multiplicity=Multiplicity(1, 1))
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
        Property(name="BPMNProfile_Lane66", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(0, 9999))
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
        Property(name="BPMNProfile_Lane72", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(0, 1))
    }
)
laneSet74: BinaryAssociation = BinaryAssociation(
    name="laneSet74",
    ends={
        Property(name="LaneSet75", type=BPMNProfile_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef80: BinaryAssociation = BinaryAssociation(
    name="sourceRef80",
    ends={
        Property(name="BPMNProfile_FlowNode82", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SequenceFlow81", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef83: BinaryAssociation = BinaryAssociation(
    name="targetRef83",
    ends={
        Property(name="BPMNProfile_FlowNode85", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SequenceFlow84", type=BPMNProfile_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueExpression86: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueExpression86",
    ends={
        Property(name="BPMNProfile_OpaqueExpression", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExpression87", type=BPMNProfile_OpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ForkNode88: BinaryAssociation = BinaryAssociation(
    name="base_ForkNode88",
    ends={
        Property(name="BPMNProfile_ForkNode89", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway", type=BPMNProfile_ForkNode, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode90: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode90",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway91", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
base_InterruptibleActivityRegion92: BinaryAssociation = BinaryAssociation(
    name="base_InterruptibleActivityRegion92",
    ends={
        Property(name="BPMNProfile_InterruptibleActivityRegion", type=BPMNProfile_EventBasedGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventBasedGateway93", type=BPMNProfile_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1))
    }
)
default94: BinaryAssociation = BinaryAssociation(
    name="default94",
    ends={
        Property(name="BPMNProfile_SequenceFlow95", type=BPMNProfile_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexGateway", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
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
base_MergeNode100: BinaryAssociation = BinaryAssociation(
    name="base_MergeNode100",
    ends={
        Property(name="BPMNProfile_MergeNode", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway101", type=BPMNProfile_MergeNode, multiplicity=Multiplicity(0, 1))
    }
)
default102: BinaryAssociation = BinaryAssociation(
    name="default102",
    ends={
        Property(name="BPMNProfile_SequenceFlow104", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway103", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
base_PackageableElement105: BinaryAssociation = BinaryAssociation(
    name="base_PackageableElement105",
    ends={
        Property(name="BPMNProfile_PackageableElement", type=BPMNProfile_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_RootElement", type=BPMNProfile_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
definition106: BinaryAssociation = BinaryAssociation(
    name="definition106",
    ends={
        Property(name="Definitions", type=BPMNProfile_RootElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rootElements", type=BPMNProfile_Definitions, multiplicity=Multiplicity(0, 1))
    }
)
base_Package107: BinaryAssociation = BinaryAssociation(
    name="base_Package107",
    ends={
        Property(name="BPMNProfile_Package", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions", type=BPMNProfile_Package, multiplicity=Multiplicity(1, 1))
    }
)
extensions108: BinaryAssociation = BinaryAssociation(
    name="extensions108",
    ends={
        Property(name="BPMNProfile_BPMNExtension", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions109", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(0, 9999))
    }
)
imports110: BinaryAssociation = BinaryAssociation(
    name="imports110",
    ends={
        Property(name="BPMNProfile_Import", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions111", type=BPMNProfile_Import, multiplicity=Multiplicity(0, 9999))
    }
)
relationships112: BinaryAssociation = BinaryAssociation(
    name="relationships112",
    ends={
        Property(name="BPMNProfile_BPMNRelationship", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Definitions113", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rootElements114: BinaryAssociation = BinaryAssociation(
    name="rootElements114",
    ends={
        Property(name="RootElement", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=BPMNProfile_RootElement, multiplicity=Multiplicity(0, 9999))
    }
)
base_Stereotype115: BinaryAssociation = BinaryAssociation(
    name="base_Stereotype115",
    ends={
        Property(name="BPMNProfile_Stereotype117", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExtension116", type=BPMNProfile_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
definition118: BinaryAssociation = BinaryAssociation(
    name="definition118",
    ends={
        Property(name="BPMNProfile_ExtensionDefinition120", type=BPMNProfile_BPMNExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNExtension119", type=BPMNProfile_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_PackageImport121: BinaryAssociation = BinaryAssociation(
    name="base_PackageImport121",
    ends={
        Property(name="BPMNProfile_PackageImport", type=BPMNProfile_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Import122", type=BPMNProfile_PackageImport, multiplicity=Multiplicity(1, 1))
    }
)
definitions123: BinaryAssociation = BinaryAssociation(
    name="definitions123",
    ends={
        Property(name="BPMNProfile_Definitions125", type=BPMNProfile_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Import124", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
activationCondition96: BinaryAssociation = BinaryAssociation(
    name="activationCondition96",
    ends={
        Property(name="BPMNProfile_BPMNExpression98", type=BPMNProfile_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexGateway97", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_DecisionNode99: BinaryAssociation = BinaryAssociation(
    name="base_DecisionNode99",
    ends={
        Property(name="BPMNProfile_DecisionNode", type=BPMNProfile_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ExclusiveGateway", type=BPMNProfile_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
definition134: BinaryAssociation = BinaryAssociation(
    name="definition134",
    ends={
        Property(name="BPMNProfile_Definitions136", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship135", type=BPMNProfile_Definitions, multiplicity=Multiplicity(1, 1))
    }
)
auditing137: BinaryAssociation = BinaryAssociation(
    name="auditing137",
    ends={
        Property(name="BPMNProfile_Auditing138", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess", type=BPMNProfile_Auditing, multiplicity=Multiplicity(0, 1))
    }
)
definitionalCollaborationRef139: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef139",
    ends={
        Property(name="BPMNProfile_BPMNCollaboration", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess140", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
base_Activity141: BinaryAssociation = BinaryAssociation(
    name="base_Activity141",
    ends={
        Property(name="BPMNProfile_Activity", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess142", type=BPMNProfile_Activity, multiplicity=Multiplicity(1, 1))
    }
)
correlationSubscriptions143: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions143",
    ends={
        Property(name="BPMNProfile_CorrelationSubscription", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess144", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(0, 9999))
    }
)
base_Constraint126: BinaryAssociation = BinaryAssociation(
    name="base_Constraint126",
    ends={
        Property(name="BPMNProfile_Constraint", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship127", type=BPMNProfile_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
targets128: BinaryAssociation = BinaryAssociation(
    name="targets128",
    ends={
        Property(name="BPMNProfile_Element130", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship129", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 9999))
    }
)
sources131: BinaryAssociation = BinaryAssociation(
    name="sources131",
    ends={
        Property(name="BPMNProfile_Element133", type=BPMNProfile_BPMNRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNRelationship132", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 9999))
    }
)
base_Behavior154: BinaryAssociation = BinaryAssociation(
    name="base_Behavior154",
    ends={
        Property(name="BPMNProfile_Behavior", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement", type=BPMNProfile_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
ioSpecification155: BinaryAssociation = BinaryAssociation(
    name="ioSpecification155",
    ends={
        Property(name="BPMNProfile_InputOutputSpecification", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement156", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
supportedInterfaceRefs157: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs157",
    ends={
        Property(name="BPMNProfile_BPMNInterface", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement158", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ioBinding159: BinaryAssociation = BinaryAssociation(
    name="ioBinding159",
    ends={
        Property(name="BPMNProfile_InputOutputBinding", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallableElement160", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(0, 9999))
    }
)
base_Behavior161: BinaryAssociation = BinaryAssociation(
    name="base_Behavior161",
    ends={
        Property(name="BPMNProfile_Behavior163", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification162", type=BPMNProfile_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Action164: BinaryAssociation = BinaryAssociation(
    name="base_Action164",
    ends={
        Property(name="BPMNProfile_Action", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification165", type=BPMNProfile_Action, multiplicity=Multiplicity(1, 1))
    }
)
dataInputs166: BinaryAssociation = BinaryAssociation(
    name="dataInputs166",
    ends={
        Property(name="BPMNProfile_DataInput", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification167", type=BPMNProfile_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
dataOutputs168: BinaryAssociation = BinaryAssociation(
    name="dataOutputs168",
    ends={
        Property(name="BPMNProfile_DataOutput", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification169", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSets170: BinaryAssociation = BinaryAssociation(
    name="inputSets170",
    ends={
        Property(name="BPMNProfile_InputSet", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification171", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
outputSets172: BinaryAssociation = BinaryAssociation(
    name="outputSets172",
    ends={
        Property(name="BPMNProfile_OutputSet", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputSpecification173", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
monitoring145: BinaryAssociation = BinaryAssociation(
    name="monitoring145",
    ends={
        Property(name="BPMNProfile_Monitoring147", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess146", type=BPMNProfile_Monitoring, multiplicity=Multiplicity(0, 1))
    }
)
supports149: BinaryAssociation = BinaryAssociation(
    name="supports149",
    ends={
        Property(name="BPMNProfile_BPMNProcess150", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess148", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1))
    }
)
properties151: BinaryAssociation = BinaryAssociation(
    name="properties151",
    ends={
        Property(name="BPMNProfile_BPMNProperty", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProcess152", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(0, 9999))
    }
)
resources153: BinaryAssociation = BinaryAssociation(
    name="resources153",
    ends={
        Property(name="ResourceRole", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(0, 9999))
    }
)
base_InputPin174: BinaryAssociation = BinaryAssociation(
    name="base_InputPin174",
    ends={
        Property(name="BPMNProfile_InputPin", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput175", type=BPMNProfile_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
base_Parameter176: BinaryAssociation = BinaryAssociation(
    name="base_Parameter176",
    ends={
        Property(name="BPMNProfile_Parameter", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput177", type=BPMNProfile_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
base_ActivityParameterNode178: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode178",
    ends={
        Property(name="BPMNProfile_ActivityParameterNode", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataInput179", type=BPMNProfile_ActivityParameterNode, multiplicity=Multiplicity(0, 1))
    }
)
inputSetRefs180: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs180",
    ends={
        Property(name="InputSet", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetWithOptional181: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional181",
    ends={
        Property(name="InputSet182", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetWithWhileExecuting183: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting183",
    ends={
        Property(name="InputSet184", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=BPMNProfile_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
dataState185: BinaryAssociation = BinaryAssociation(
    name="dataState185",
    ends={
        Property(name="BPMNProfile_DataState", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement", type=BPMNProfile_DataState, multiplicity=Multiplicity(0, 9999))
    }
)
base_TypedElement186: BinaryAssociation = BinaryAssociation(
    name="base_TypedElement186",
    ends={
        Property(name="BPMNProfile_TypedElement", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement187", type=BPMNProfile_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef188: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef188",
    ends={
        Property(name="BPMNProfile_ItemDefinition", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemAwareElement189", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_State190: BinaryAssociation = BinaryAssociation(
    name="base_State190",
    ends={
        Property(name="BPMNProfile_State", type=BPMNProfile_DataState, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataState191", type=BPMNProfile_State, multiplicity=Multiplicity(1, 1))
    }
)
base_Class192: BinaryAssociation = BinaryAssociation(
    name="base_Class192",
    ends={
        Property(name="BPMNProfile_Class194", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition193", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
structureRef195: BinaryAssociation = BinaryAssociation(
    name="structureRef195",
    ends={
        Property(name="BPMNProfile_Element197", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition196", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
base_ParameterSet201: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet201",
    ends={
        Property(name="BPMNProfile_ParameterSet", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputSet202", type=BPMNProfile_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
optionalInputRefs203: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs203",
    ends={
        Property(name="DataInput", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=BPMNProfile_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingInputRefs204: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs204",
    ends={
        Property(name="DataInput205", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=BPMNProfile_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputRefs206: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs206",
    ends={
        Property(name="DataInput207", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=BPMNProfile_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
import198: BinaryAssociation = BinaryAssociation(
    name="import198",
    ends={
        Property(name="BPMNProfile_Import200", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ItemDefinition199", type=BPMNProfile_Import, multiplicity=Multiplicity(0, 1))
    }
)
base_ActivityParameterNode213: BinaryAssociation = BinaryAssociation(
    name="base_ActivityParameterNode213",
    ends={
        Property(name="BPMNProfile_ActivityParameterNode215", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput214", type=BPMNProfile_ActivityParameterNode, multiplicity=Multiplicity(0, 1))
    }
)
outputSetRefs216: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs216",
    ends={
        Property(name="OutputSet", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithOptional217: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional217",
    ends={
        Property(name="BPMNProfile_OutputSet219", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput218", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithWhileExecuting220: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting220",
    ends={
        Property(name="BPMNProfile_OutputSet222", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput221", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
base_ParameterSet223: BinaryAssociation = BinaryAssociation(
    name="base_ParameterSet223",
    ends={
        Property(name="BPMNProfile_ParameterSet225", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet224", type=BPMNProfile_ParameterSet, multiplicity=Multiplicity(1, 1))
    }
)
optionalOutputRefs226: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs226",
    ends={
        Property(name="BPMNProfile_DataOutput228", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet227", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingOutputRefs229: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs229",
    ends={
        Property(name="BPMNProfile_DataOutput231", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_OutputSet230", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
dataOutputRefs232: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs232",
    ends={
        Property(name="DataOutput", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
base_OutputPin208: BinaryAssociation = BinaryAssociation(
    name="base_OutputPin208",
    ends={
        Property(name="BPMNProfile_OutputPin", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput209", type=BPMNProfile_OutputPin, multiplicity=Multiplicity(0, 1))
    }
)
base_Parameter210: BinaryAssociation = BinaryAssociation(
    name="base_Parameter210",
    ends={
        Property(name="BPMNProfile_Parameter212", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataOutput211", type=BPMNProfile_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
base_Interface233: BinaryAssociation = BinaryAssociation(
    name="base_Interface233",
    ends={
        Property(name="BPMNProfile_Interface", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface234", type=BPMNProfile_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef235: BinaryAssociation = BinaryAssociation(
    name="implementationRef235",
    ends={
        Property(name="BPMNProfile_Element237", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface236", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
operations238: BinaryAssociation = BinaryAssociation(
    name="operations238",
    ends={
        Property(name="BPMNProfile_BPMNOperation", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface239", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 9999))
    }
)
callableElements240: BinaryAssociation = BinaryAssociation(
    name="callableElements240",
    ends={
        Property(name="BPMNProfile_CallableElement242", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNInterface241", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(0, 9999))
    }
)
base_Operation243: BinaryAssociation = BinaryAssociation(
    name="base_Operation243",
    ends={
        Property(name="BPMNProfile_Operation", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation244", type=BPMNProfile_Operation, multiplicity=Multiplicity(1, 1))
    }
)
implementationRef245: BinaryAssociation = BinaryAssociation(
    name="implementationRef245",
    ends={
        Property(name="BPMNProfile_Element247", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation246", type=BPMNProfile_Element, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef248: BinaryAssociation = BinaryAssociation(
    name="inMessageRef248",
    ends={
        Property(name="BPMNProfile_BPMNMessage", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation249", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
itemRef255: BinaryAssociation = BinaryAssociation(
    name="itemRef255",
    ends={
        Property(name="BPMNProfile_ItemDefinition257", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNMessage256", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef258: BinaryAssociation = BinaryAssociation(
    name="inputDataRef258",
    ends={
        Property(name="BPMNProfile_InputSet260", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding259", type=BPMNProfile_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef261: BinaryAssociation = BinaryAssociation(
    name="outputDataRef261",
    ends={
        Property(name="BPMNProfile_OutputSet263", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding262", type=BPMNProfile_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef264: BinaryAssociation = BinaryAssociation(
    name="operationRef264",
    ends={
        Property(name="BPMNProfile_BPMNOperation266", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding265", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency267: BinaryAssociation = BinaryAssociation(
    name="base_Dependency267",
    ends={
        Property(name="BPMNProfile_Dependency269", type=BPMNProfile_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InputOutputBinding268", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
participantAssociations270: BinaryAssociation = BinaryAssociation(
    name="participantAssociations270",
    ends={
        Property(name="BPMNProfile_ParticipantAssociation", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration271", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
conversationLinks272: BinaryAssociation = BinaryAssociation(
    name="conversationLinks272",
    ends={
        Property(name="ConversationLink", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="collaboration", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
messageFlowAssociations273: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations273",
    ends={
        Property(name="BPMNProfile_MessageFlowAssociation", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration274", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
messageFlows275: BinaryAssociation = BinaryAssociation(
    name="messageFlows275",
    ends={
        Property(name="BPMNProfile_MessageFlow", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration276", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(0, 9999))
    }
)
base_Collaboration277: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration277",
    ends={
        Property(name="BPMNProfile_Collaboration", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration278", type=BPMNProfile_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef250: BinaryAssociation = BinaryAssociation(
    name="outMessageRef250",
    ends={
        Property(name="BPMNProfile_BPMNMessage252", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation251", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
errorRef253: BinaryAssociation = BinaryAssociation(
    name="errorRef253",
    ends={
        Property(name="BPMNProfile_Error", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNOperation254", type=BPMNProfile_Error, multiplicity=Multiplicity(0, 9999))
    }
)
base_Dependency285: BinaryAssociation = BinaryAssociation(
    name="base_Dependency285",
    ends={
        Property(name="BPMNProfile_Dependency287", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation286", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
innerParticipantRef288: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef288",
    ends={
        Property(name="BPMNProfile_Participant290", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation289", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef291: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef291",
    ends={
        Property(name="BPMNProfile_Participant293", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantAssociation292", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1))
    }
)
conversations279: BinaryAssociation = BinaryAssociation(
    name="conversations279",
    ends={
        Property(name="BPMNProfile_ConversationNode", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration280", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(0, 9999))
    }
)
correlationKeys281: BinaryAssociation = BinaryAssociation(
    name="correlationKeys281",
    ends={
        Property(name="BPMNProfile_CorrelationKey", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration282", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(0, 9999))
    }
)
participants283: BinaryAssociation = BinaryAssociation(
    name="participants283",
    ends={
        Property(name="BPMNProfile_Participant", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNCollaboration284", type=BPMNProfile_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property294: BinaryAssociation = BinaryAssociation(
    name="base_Property294",
    ends={
        Property(name="BPMNProfile_Property296", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant295", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
processRef297: BinaryAssociation = BinaryAssociation(
    name="processRef297",
    ends={
        Property(name="BPMNProfile_BPMNProcess299", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant298", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
participantMultiplicity300: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity300",
    ends={
        Property(name="BPMNProfile_ParticipantMultiplicity", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant301", type=BPMNProfile_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1))
    }
)
partnerEntityRef302: BinaryAssociation = BinaryAssociation(
    name="partnerEntityRef302",
    ends={
        Property(name="PartnerEntity", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(0, 9999))
    }
)
partnerRoleRef303: BinaryAssociation = BinaryAssociation(
    name="partnerRoleRef303",
    ends={
        Property(name="PartnerRole", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participantRef304", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(0, 9999))
    }
)
interfaceRefs305: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs305",
    ends={
        Property(name="BPMNProfile_BPMNInterface307", type=BPMNProfile_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Participant306", type=BPMNProfile_BPMNInterface, multiplicity=Multiplicity(0, 9999))
    }
)
base_InteractionNode_Element308: BinaryAssociation = BinaryAssociation(
    name="base_InteractionNode_Element308",
    ends={
        Property(name="BPMNProfile_Element309", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_InteractionNode", type=BPMNProfile_Element, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConversationLinks310: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks310",
    ends={
        Property(name="ConversationLink312", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef311", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConversationLinks313: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks313",
    ends={
        Property(name="ConversationLink315", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef314", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1))
    }
)
collaboration316: BinaryAssociation = BinaryAssociation(
    name="collaboration316",
    ends={
        Property(name="BPMNCollaboration", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="conversationLinks", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency317: BinaryAssociation = BinaryAssociation(
    name="base_Dependency317",
    ends={
        Property(name="BPMNProfile_Dependency318", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationLink", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
targetRef319: BinaryAssociation = BinaryAssociation(
    name="targetRef319",
    ends={
        Property(name="InteractionNode", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConversationLinks", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef320: BinaryAssociation = BinaryAssociation(
    name="sourceRef320",
    ends={
        Property(name="InteractionNode321", type=BPMNProfile_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConversationLinks", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
base_MultiplicityElement322: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement322",
    ends={
        Property(name="BPMNProfile_MultiplicityElement", type=BPMNProfile_ParticipantMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ParticipantMultiplicity323", type=BPMNProfile_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
base_InstanceSpecification324: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification324",
    ends={
        Property(name="BPMNProfile_InstanceSpecification", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_PartnerEntity", type=BPMNProfile_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
participantRef325: BinaryAssociation = BinaryAssociation(
    name="participantRef325",
    ends={
        Property(name="Participant", type=BPMNProfile_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerEntityRef", type=BPMNProfile_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
base_Class326: BinaryAssociation = BinaryAssociation(
    name="base_Class326",
    ends={
        Property(name="BPMNProfile_Class327", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_PartnerRole", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
participantRef328: BinaryAssociation = BinaryAssociation(
    name="participantRef328",
    ends={
        Property(name="Participant329", type=BPMNProfile_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="partnerRoleRef", type=BPMNProfile_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
base_Dependency330: BinaryAssociation = BinaryAssociation(
    name="base_Dependency330",
    ends={
        Property(name="BPMNProfile_Dependency332", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation331", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef333: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef333",
    ends={
        Property(name="BPMNProfile_MessageFlow335", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation334", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef336: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef336",
    ends={
        Property(name="BPMNProfile_MessageFlow338", type=BPMNProfile_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlowAssociation337", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
base_InformationFlow339: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow339",
    ends={
        Property(name="BPMNProfile_InformationFlow", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow340", type=BPMNProfile_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef341: BinaryAssociation = BinaryAssociation(
    name="sourceRef341",
    ends={
        Property(name="BPMNProfile_InteractionNode343", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow342", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef344: BinaryAssociation = BinaryAssociation(
    name="targetRef344",
    ends={
        Property(name="BPMNProfile_InteractionNode346", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow345", type=BPMNProfile_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
messageRef347: BinaryAssociation = BinaryAssociation(
    name="messageRef347",
    ends={
        Property(name="BPMNProfile_BPMNMessage349", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageFlow348", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_Class362: BinaryAssociation = BinaryAssociation(
    name="base_Class362",
    ends={
        Property(name="BPMNProfile_Class364", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationKey363", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef365: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef365",
    ends={
        Property(name="BPMNProfile_CorrelationProperty", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationKey366", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property367: BinaryAssociation = BinaryAssociation(
    name="base_Property367",
    ends={
        Property(name="BPMNProfile_Property369", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty368", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
type370: BinaryAssociation = BinaryAssociation(
    name="type370",
    ends={
        Property(name="BPMNProfile_ItemDefinition372", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty371", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
correlationPropertyRetrievalExpression373: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression373",
    ends={
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationProperty374", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999))
    }
)
base_Dependency375: BinaryAssociation = BinaryAssociation(
    name="base_Dependency375",
    ends={
        Property(name="BPMNProfile_Dependency377", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression376", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
messageRef378: BinaryAssociation = BinaryAssociation(
    name="messageRef378",
    ends={
        Property(name="BPMNProfile_BPMNMessage380", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression379", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(1, 1))
    }
)
messagePath381: BinaryAssociation = BinaryAssociation(
    name="messagePath381",
    ends={
        Property(name="BPMNProfile_FormalExpression", type=BPMNProfile_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyRetrievalExpression382", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
evaluatesToTypeRef383: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef383",
    ends={
        Property(name="BPMNProfile_ItemDefinition385", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_FormalExpression384", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
base_Class386: BinaryAssociation = BinaryAssociation(
    name="base_Class386",
    ends={
        Property(name="BPMNProfile_Class388", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription387", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
correlationKeyRef389: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef389",
    ends={
        Property(name="BPMNProfile_CorrelationKey391", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription390", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
base_InformationFlow350: BinaryAssociation = BinaryAssociation(
    name="base_InformationFlow350",
    ends={
        Property(name="BPMNProfile_InformationFlow352", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode351", type=BPMNProfile_InformationFlow, multiplicity=Multiplicity(1, 1))
    }
)
messageFlowRefs353: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs353",
    ends={
        Property(name="BPMNProfile_MessageFlow355", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode354", type=BPMNProfile_MessageFlow, multiplicity=Multiplicity(0, 9999))
    }
)
correlationKeys356: BinaryAssociation = BinaryAssociation(
    name="correlationKeys356",
    ends={
        Property(name="BPMNProfile_CorrelationKey358", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode357", type=BPMNProfile_CorrelationKey, multiplicity=Multiplicity(0, 9999))
    }
)
participantRefs359: BinaryAssociation = BinaryAssociation(
    name="participantRefs359",
    ends={
        Property(name="BPMNProfile_Participant361", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConversationNode360", type=BPMNProfile_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
base_DataStoreNode403: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode403",
    ends={
        Property(name="BPMNProfile_DataStoreNode", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProperty404", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
umlProperty405: BinaryAssociation = BinaryAssociation(
    name="umlProperty405",
    ends={
        Property(name="BPMNProfile_Property407", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNProperty406", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding392: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding392",
    ends={
        Property(name="BPMNProfile_CorrelationPropertyBinding", type=BPMNProfile_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationSubscription393", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property394: BinaryAssociation = BinaryAssociation(
    name="base_Property394",
    ends={
        Property(name="BPMNProfile_Property396", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding395", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
dataPath397: BinaryAssociation = BinaryAssociation(
    name="dataPath397",
    ends={
        Property(name="BPMNProfile_FormalExpression399", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding398", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyRef400: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef400",
    ends={
        Property(name="BPMNProfile_CorrelationProperty402", type=BPMNProfile_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CorrelationPropertyBinding401", type=BPMNProfile_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
base_Property408: BinaryAssociation = BinaryAssociation(
    name="base_Property408",
    ends={
        Property(name="BPMNProfile_ResourceRole", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Property409", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1))
    }
)
resourceAssignmentExpression410: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression410",
    ends={
        Property(name="BPMNProfile_ResourceAssignmentExpression", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole411", type=BPMNProfile_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef412: BinaryAssociation = BinaryAssociation(
    name="resourceRef412",
    ends={
        Property(name="BPMNProfile_Resource", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole413", type=BPMNProfile_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings414: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings414",
    ends={
        Property(name="BPMNProfile_ResourceParameterBinding", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceRole415", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999))
    }
)
process416: BinaryAssociation = BinaryAssociation(
    name="process416",
    ends={
        Property(name="BPMNProcess", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=BPMNProfile_BPMNProcess, multiplicity=Multiplicity(0, 1))
    }
)
expression417: BinaryAssociation = BinaryAssociation(
    name="expression417",
    ends={
        Property(name="BPMNProfile_BPMNExpression419", type=BPMNProfile_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceAssignmentExpression418", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
resourceParameters420: BinaryAssociation = BinaryAssociation(
    name="resourceParameters420",
    ends={
        Property(name="BPMNProfile_ResourceParameter", type=BPMNProfile_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Resource421", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property422: BinaryAssociation = BinaryAssociation(
    name="base_Property422",
    ends={
        Property(name="BPMNProfile_Property424", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameter423", type=BPMNProfile_Property, multiplicity=Multiplicity(1, 1))
    }
)
type425: BinaryAssociation = BinaryAssociation(
    name="type425",
    ends={
        Property(name="BPMNProfile_ItemDefinition427", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameter426", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
base_Slot428: BinaryAssociation = BinaryAssociation(
    name="base_Slot428",
    ends={
        Property(name="BPMNProfile_Slot430", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding429", type=BPMNProfile_Slot, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef431: BinaryAssociation = BinaryAssociation(
    name="parameterRef431",
    ends={
        Property(name="BPMNProfile_ResourceParameter433", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding432", type=BPMNProfile_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
expression434: BinaryAssociation = BinaryAssociation(
    name="expression434",
    ends={
        Property(name="BPMNProfile_BPMNExpression436", type=BPMNProfile_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ResourceParameterBinding435", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueBehavior437: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueBehavior437",
    ends={
        Property(name="BPMNProfile_OpaqueBehavior", type=BPMNProfile_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalTask", type=BPMNProfile_OpaqueBehavior, multiplicity=Multiplicity(1, 1))
    }
)
resources438: BinaryAssociation = BinaryAssociation(
    name="resources438",
    ends={
        Property(name="BPMNProfile_ResourceRole440", type=BPMNProfile_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalTask439", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(0, 9999))
    }
)
activityRef441: BinaryAssociation = BinaryAssociation(
    name="activityRef441",
    ends={
        Property(name="BPMNProfile_BPMNActivity", type=BPMNProfile_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CompensateEventDefinition", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent442: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent442",
    ends={
        Property(name="BPMNProfile_CallEvent", type=BPMNProfile_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CompensateEventDefinition443", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Event444: BinaryAssociation = BinaryAssociation(
    name="base_Event444",
    ends={
        Property(name="BPMNProfile_Event", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EventDefinition", type=BPMNProfile_Event, multiplicity=Multiplicity(1, 1))
    }
)
base_Action445: BinaryAssociation = BinaryAssociation(
    name="base_Action445",
    ends={
        Property(name="BPMNProfile_Action447", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity446", type=BPMNProfile_Action, multiplicity=Multiplicity(1, 1))
    }
)
activityClass448: BinaryAssociation = BinaryAssociation(
    name="activityClass448",
    ends={
        Property(name="BPMNProfile_Class450", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity449", type=BPMNProfile_Class, multiplicity=Multiplicity(0, 1))
    }
)
properties451: BinaryAssociation = BinaryAssociation(
    name="properties451",
    ends={
        Property(name="BPMNProfile_BPMNProperty453", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity452", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(0, 9999))
    }
)
default454: BinaryAssociation = BinaryAssociation(
    name="default454",
    ends={
        Property(name="BPMNProfile_SequenceFlow456", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity455", type=BPMNProfile_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
boundaryEventRefs457: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs457",
    ends={
        Property(name="BPMNProfile_BoundaryEvent", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity458", type=BPMNProfile_BoundaryEvent, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputAssociations459: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations459",
    ends={
        Property(name="BPMNProfile_DataInputAssociation", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity460", type=BPMNProfile_DataInputAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
dataOutputAssociations461: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations461",
    ends={
        Property(name="BPMNProfile_DataOutputAssociation", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity462", type=BPMNProfile_DataOutputAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
loopCharacteristics463: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics463",
    ends={
        Property(name="BPMNProfile_LoopCharacteristics", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity464", type=BPMNProfile_LoopCharacteristics, multiplicity=Multiplicity(0, 1))
    }
)
resources465: BinaryAssociation = BinaryAssociation(
    name="resources465",
    ends={
        Property(name="BPMNProfile_ResourceRole467", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNActivity466", type=BPMNProfile_ResourceRole, multiplicity=Multiplicity(0, 9999))
    }
)
attachedToRef468: BinaryAssociation = BinaryAssociation(
    name="attachedToRef468",
    ends={
        Property(name="BPMNProfile_BPMNActivity470", type=BPMNProfile_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BoundaryEvent469", type=BPMNProfile_BPMNActivity, multiplicity=Multiplicity(1, 1))
    }
)
base_AcceptEventAction471: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction471",
    ends={
        Property(name="BPMNProfile_AcceptEventAction", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent", type=BPMNProfile_AcceptEventAction, multiplicity=Multiplicity(0, 1))
    }
)
base_InitialNode472: BinaryAssociation = BinaryAssociation(
    name="base_InitialNode472",
    ends={
        Property(name="BPMNProfile_InitialNode", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent473", type=BPMNProfile_InitialNode, multiplicity=Multiplicity(0, 1))
    }
)
dataOutputAssociation474: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation474",
    ends={
        Property(name="BPMNProfile_DataOutputAssociation476", type=BPMNProfile_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CatchEvent475", type=BPMNProfile_DataOutputAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
eventClass477: BinaryAssociation = BinaryAssociation(
    name="eventClass477",
    ends={
        Property(name="BPMNProfile_Class478", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent", type=BPMNProfile_Class, multiplicity=Multiplicity(0, 1))
    }
)
_eventDefinitions479: BinaryAssociation = BinaryAssociation(
    name="_eventDefinitions479",
    ends={
        Property(name="BPMNProfile_EventDefinition481", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent480", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
properties482: BinaryAssociation = BinaryAssociation(
    name="properties482",
    ends={
        Property(name="BPMNProfile_BPMNProperty484", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent483", type=BPMNProfile_BPMNProperty, multiplicity=Multiplicity(0, 9999))
    }
)
eventDefinitionRefs485: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs485",
    ends={
        Property(name="BPMNProfile_EventDefinition487", type=BPMNProfile_BPMNEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BPMNEvent486", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
sourceRef489: BinaryAssociation = BinaryAssociation(
    name="sourceRef489",
    ends={
        Property(name="BPMNProfile_ItemAwareElement491", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation490", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
targetRef492: BinaryAssociation = BinaryAssociation(
    name="targetRef492",
    ends={
        Property(name="BPMNProfile_ItemAwareElement494", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation493", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
transformation495: BinaryAssociation = BinaryAssociation(
    name="transformation495",
    ends={
        Property(name="BPMNProfile_FormalExpression497", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation496", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignment498: BinaryAssociation = BinaryAssociation(
    name="assignment498",
    ends={
        Property(name="BPMNProfile_Assignment", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation499", type=BPMNProfile_Assignment, multiplicity=Multiplicity(0, 9999))
    }
)
base_Dependency500: BinaryAssociation = BinaryAssociation(
    name="base_Dependency500",
    ends={
        Property(name="BPMNProfile_Dependency502", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment501", type=BPMNProfile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
from503: BinaryAssociation = BinaryAssociation(
    name="from503",
    ends={
        Property(name="BPMNProfile_BPMNExpression505", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment504", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
to506: BinaryAssociation = BinaryAssociation(
    name="to506",
    ends={
        Property(name="BPMNProfile_BPMNExpression508", type=BPMNProfile_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Assignment507", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredActivityNode509: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode509",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode511", type=BPMNProfile_LoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LoopCharacteristics510", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
escalationRef512: BinaryAssociation = BinaryAssociation(
    name="escalationRef512",
    ends={
        Property(name="BPMNProfile_Escalation", type=BPMNProfile_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EscalationEventDefinition", type=BPMNProfile_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
base_ObjectFlow488: BinaryAssociation = BinaryAssociation(
    name="base_ObjectFlow488",
    ends={
        Property(name="BPMNProfile_ObjectFlow", type=BPMNProfile_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataAssociation", type=BPMNProfile_ObjectFlow, multiplicity=Multiplicity(1, 1))
    }
)
timeCycle516: BinaryAssociation = BinaryAssociation(
    name="timeCycle516",
    ends={
        Property(name="BPMNProfile_BPMNExpression517", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDate518: BinaryAssociation = BinaryAssociation(
    name="timeDate518",
    ends={
        Property(name="BPMNProfile_BPMNExpression520", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition519", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
timeDuration521: BinaryAssociation = BinaryAssociation(
    name="timeDuration521",
    ends={
        Property(name="BPMNProfile_BPMNExpression523", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition522", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ChangeEvent524: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent524",
    ends={
        Property(name="BPMNProfile_ChangeEvent", type=BPMNProfile_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TimerEventDefinition525", type=BPMNProfile_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
signalRef526: BinaryAssociation = BinaryAssociation(
    name="signalRef526",
    ends={
        Property(name="BPMNProfile_BPMNSignal", type=BPMNProfile_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SignalEventDefinition", type=BPMNProfile_BPMNSignal, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent527: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent527",
    ends={
        Property(name="BPMNProfile_CallEvent529", type=BPMNProfile_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SignalEventDefinition528", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_FinalNode530: BinaryAssociation = BinaryAssociation(
    name="base_FinalNode530",
    ends={
        Property(name="BPMNProfile_FinalNode", type=BPMNProfile_EndEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EndEvent", type=BPMNProfile_FinalNode, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent513: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent513",
    ends={
        Property(name="BPMNProfile_CallEvent515", type=BPMNProfile_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_EscalationEventDefinition514", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_CallOperationAction531: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction531",
    ends={
        Property(name="BPMNProfile_CallOperationAction", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(0, 1))
    }
)
base_FlowFinalNode532: BinaryAssociation = BinaryAssociation(
    name="base_FlowFinalNode532",
    ends={
        Property(name="BPMNProfile_FlowFinalNode", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent533", type=BPMNProfile_FlowFinalNode, multiplicity=Multiplicity(1, 1))
    }
)
dataInputAssociation534: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation534",
    ends={
        Property(name="BPMNProfile_DataInputAssociation536", type=BPMNProfile_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ThrowEvent535", type=BPMNProfile_DataInputAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
messageRef537: BinaryAssociation = BinaryAssociation(
    name="messageRef537",
    ends={
        Property(name="BPMNProfile_BPMNMessage538", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
operationRef539: BinaryAssociation = BinaryAssociation(
    name="operationRef539",
    ends={
        Property(name="BPMNProfile_BPMNOperation541", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition540", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent542: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent542",
    ends={
        Property(name="BPMNProfile_CallEvent544", type=BPMNProfile_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MessageEventDefinition543", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_ChangeEvent545: BinaryAssociation = BinaryAssociation(
    name="base_ChangeEvent545",
    ends={
        Property(name="BPMNProfile_ChangeEvent546", type=BPMNProfile_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConditionalEventDefinition", type=BPMNProfile_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
condition547: BinaryAssociation = BinaryAssociation(
    name="condition547",
    ends={
        Property(name="BPMNProfile_BPMNExpression549", type=BPMNProfile_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ConditionalEventDefinition548", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
_target551: BinaryAssociation = BinaryAssociation(
    name="_target551",
    ends={
        Property(name="LinkEventDefinition", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
source553: BinaryAssociation = BinaryAssociation(
    name="source553",
    ends={
        Property(name="LinkEventDefinition554", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="_target", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
base_CallEvent555: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent555",
    ends={
        Property(name="BPMNProfile_CallEvent556", type=BPMNProfile_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_LinkEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
errorRef557: BinaryAssociation = BinaryAssociation(
    name="errorRef557",
    ends={
        Property(name="BPMNProfile_Error558", type=BPMNProfile_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ErrorEventDefinition", type=BPMNProfile_Error, multiplicity=Multiplicity(0, 1))
    }
)
base_CallEvent559: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent559",
    ends={
        Property(name="BPMNProfile_CallEvent561", type=BPMNProfile_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ErrorEventDefinition560", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode579: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode579",
    ends={
        Property(name="BPMNProfile_DataStoreNode581", type=BPMNProfile_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObjectReference580", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_SendObjectAction562: BinaryAssociation = BinaryAssociation(
    name="base_SendObjectAction562",
    ends={
        Property(name="BPMNProfile_SendObjectAction", type=BPMNProfile_IntermediateThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_IntermediateThrowEvent", type=BPMNProfile_SendObjectAction, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent563: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent563",
    ends={
        Property(name="BPMNProfile_CallEvent564", type=BPMNProfile_TerminateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TerminateEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_CallEvent565: BinaryAssociation = BinaryAssociation(
    name="base_CallEvent565",
    ends={
        Property(name="BPMNProfile_CallEvent566", type=BPMNProfile_CancelEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CancelEventDefinition", type=BPMNProfile_CallEvent, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment567: BinaryAssociation = BinaryAssociation(
    name="base_Comment567",
    ends={
        Property(name="BPMNProfile_Comment568", type=BPMNProfile_TextAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_TextAnnotation", type=BPMNProfile_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration569: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration569",
    ends={
        Property(name="BPMNProfile_Enumeration", type=BPMNProfile_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Category", type=BPMNProfile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
categoryValue570: BinaryAssociation = BinaryAssociation(
    name="categoryValue570",
    ends={
        Property(name="BPMNProfile_CategoryValue572", type=BPMNProfile_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Category571", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(0, 9999))
    }
)
base_ActivityPartition573: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition573",
    ends={
        Property(name="BPMNProfile_ActivityPartition574", type=BPMNProfile_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Group", type=BPMNProfile_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
_categoryValueRef575: BinaryAssociation = BinaryAssociation(
    name="_categoryValueRef575",
    ends={
        Property(name="BPMNProfile_CategoryValue577", type=BPMNProfile_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Group576", type=BPMNProfile_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
dataObjectRef578: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef578",
    ends={
        Property(name="BPMNProfile_DataObject", type=BPMNProfile_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObjectReference", type=BPMNProfile_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
base_DataStoreNode582: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode582",
    ends={
        Property(name="BPMNProfile_DataStoreNode584", type=BPMNProfile_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataObject583", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_Class585: BinaryAssociation = BinaryAssociation(
    name="base_Class585",
    ends={
        Property(name="BPMNProfile_Class586", type=BPMNProfile_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStore", type=BPMNProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
itemSubjectRef587: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef587",
    ends={
        Property(name="BPMNProfile_ItemDefinition589", type=BPMNProfile_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStore588", type=BPMNProfile_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
_dataStore590: BinaryAssociation = BinaryAssociation(
    name="_dataStore590",
    ends={
        Property(name="BPMNProfile_DataStore591", type=BPMNProfile_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStoreReference", type=BPMNProfile_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
base_DataStoreNode592: BinaryAssociation = BinaryAssociation(
    name="base_DataStoreNode592",
    ends={
        Property(name="BPMNProfile_DataStoreNode594", type=BPMNProfile_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_DataStoreReference593", type=BPMNProfile_DataStoreNode, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction595: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction595",
    ends={
        Property(name="BPMNProfile_OpaqueAction", type=BPMNProfile_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_UserTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
renderings596: BinaryAssociation = BinaryAssociation(
    name="renderings596",
    ends={
        Property(name="BPMNProfile_Rendering", type=BPMNProfile_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_UserTask597", type=BPMNProfile_Rendering, multiplicity=Multiplicity(0, 9999))
    }
)
ioSpecification598: BinaryAssociation = BinaryAssociation(
    name="ioSpecification598",
    ends={
        Property(name="BPMNProfile_InputOutputSpecification599", type=BPMNProfile_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Task", type=BPMNProfile_InputOutputSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Image600: BinaryAssociation = BinaryAssociation(
    name="base_Image600",
    ends={
        Property(name="BPMNProfile_Image", type=BPMNProfile_Rendering, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_Rendering601", type=BPMNProfile_Image, multiplicity=Multiplicity(1, 1))
    }
)
renderings602: BinaryAssociation = BinaryAssociation(
    name="renderings602",
    ends={
        Property(name="BPMNProfile_Rendering603", type=BPMNProfile_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_GlobalUserTask", type=BPMNProfile_Rendering, multiplicity=Multiplicity(0, 9999))
    }
)
base_OpaqueAction604: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction604",
    ends={
        Property(name="BPMNProfile_OpaqueAction605", type=BPMNProfile_ManualTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ManualTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
conversationNodes606: BinaryAssociation = BinaryAssociation(
    name="conversationNodes606",
    ends={
        Property(name="BPMNProfile_ConversationNode607", type=BPMNProfile_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubConversation", type=BPMNProfile_ConversationNode, multiplicity=Multiplicity(0, 9999))
    }
)
_collaborationUse608: BinaryAssociation = BinaryAssociation(
    name="_collaborationUse608",
    ends={
        Property(name="BPMNProfile_CollaborationUse", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallConversation", type=BPMNProfile_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
calledCollaborationRef609: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef609",
    ends={
        Property(name="BPMNProfile_BPMNCollaboration611", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallConversation610", type=BPMNProfile_BPMNCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations612: BinaryAssociation = BinaryAssociation(
    name="participantAssociations612",
    ends={
        Property(name="BPMNProfile_ParticipantAssociation614", type=BPMNProfile_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallConversation613", type=BPMNProfile_ParticipantAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
base_StructuredActivityNode615: BinaryAssociation = BinaryAssociation(
    name="base_StructuredActivityNode615",
    ends={
        Property(name="BPMNProfile_StructuredActivityNode616", type=BPMNProfile_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubProcess", type=BPMNProfile_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
hasLaneSets617: BinaryAssociation = BinaryAssociation(
    name="hasLaneSets617",
    ends={
        Property(name="BPMNProfile_LaneSet619", type=BPMNProfile_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SubProcess618", type=BPMNProfile_LaneSet, multiplicity=Multiplicity(0, 9999))
    }
)
base_CallBehaviorAction620: BinaryAssociation = BinaryAssociation(
    name="base_CallBehaviorAction620",
    ends={
        Property(name="BPMNProfile_CallBehaviorAction", type=BPMNProfile_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallActivity", type=BPMNProfile_CallBehaviorAction, multiplicity=Multiplicity(1, 1))
    }
)
calledElementRef621: BinaryAssociation = BinaryAssociation(
    name="calledElementRef621",
    ends={
        Property(name="BPMNProfile_CallableElement623", type=BPMNProfile_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_CallActivity622", type=BPMNProfile_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
base_OpaqueAction624: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction624",
    ends={
        Property(name="BPMNProfile_OpaqueAction625", type=BPMNProfile_BusinessRuleTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_BusinessRuleTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
condition626: BinaryAssociation = BinaryAssociation(
    name="condition626",
    ends={
        Property(name="BPMNProfile_FormalExpression627", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition", type=BPMNProfile_FormalExpression, multiplicity=Multiplicity(1, 1))
    }
)
event628: BinaryAssociation = BinaryAssociation(
    name="event628",
    ends={
        Property(name="BPMNProfile_ImplicitThrowEvent", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition629", type=BPMNProfile_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1))
    }
)
base_ControlFlow630: BinaryAssociation = BinaryAssociation(
    name="base_ControlFlow630",
    ends={
        Property(name="BPMNProfile_ControlFlow632", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ComplexBehaviorDefinition631", type=BPMNProfile_ControlFlow, multiplicity=Multiplicity(1, 1))
    }
)
completionCondition633: BinaryAssociation = BinaryAssociation(
    name="completionCondition633",
    ends={
        Property(name="BPMNProfile_BPMNExpression634", type=BPMNProfile_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_AdHocSubProcess", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueAction635: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueAction635",
    ends={
        Property(name="BPMNProfile_OpaqueAction636", type=BPMNProfile_ScriptTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ScriptTask", type=BPMNProfile_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
messageRef637: BinaryAssociation = BinaryAssociation(
    name="messageRef637",
    ends={
        Property(name="BPMNProfile_BPMNMessage638", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_CallOperationAction639: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction639",
    ends={
        Property(name="BPMNProfile_CallOperationAction641", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask640", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef642: BinaryAssociation = BinaryAssociation(
    name="operationRef642",
    ends={
        Property(name="BPMNProfile_BPMNOperation644", type=BPMNProfile_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_SendTask643", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_LoopNode645: BinaryAssociation = BinaryAssociation(
    name="base_LoopNode645",
    ends={
        Property(name="BPMNProfile_LoopNode", type=BPMNProfile_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_StandardLoopCharacteristics", type=BPMNProfile_LoopNode, multiplicity=Multiplicity(1, 1))
    }
)
loopCondition646: BinaryAssociation = BinaryAssociation(
    name="loopCondition646",
    ends={
        Property(name="BPMNProfile_BPMNExpression648", type=BPMNProfile_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_StandardLoopCharacteristics647", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(1, 1))
    }
)
messageRef649: BinaryAssociation = BinaryAssociation(
    name="messageRef649",
    ends={
        Property(name="BPMNProfile_BPMNMessage650", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask", type=BPMNProfile_BPMNMessage, multiplicity=Multiplicity(0, 1))
    }
)
base_AcceptEventAction651: BinaryAssociation = BinaryAssociation(
    name="base_AcceptEventAction651",
    ends={
        Property(name="BPMNProfile_AcceptEventAction653", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask652", type=BPMNProfile_AcceptEventAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef654: BinaryAssociation = BinaryAssociation(
    name="operationRef654",
    ends={
        Property(name="BPMNProfile_BPMNOperation656", type=BPMNProfile_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ReceiveTask655", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
base_CallOperationAction657: BinaryAssociation = BinaryAssociation(
    name="base_CallOperationAction657",
    ends={
        Property(name="BPMNProfile_CallOperationAction658", type=BPMNProfile_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ServiceTask", type=BPMNProfile_CallOperationAction, multiplicity=Multiplicity(1, 1))
    }
)
operationRef659: BinaryAssociation = BinaryAssociation(
    name="operationRef659",
    ends={
        Property(name="BPMNProfile_BPMNOperation661", type=BPMNProfile_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_ServiceTask660", type=BPMNProfile_BPMNOperation, multiplicity=Multiplicity(0, 1))
    }
)
loopDataInputRef669: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef669",
    ends={
        Property(name="BPMNProfile_ItemAwareElement671", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics670", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef672: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef672",
    ends={
        Property(name="BPMNProfile_ItemAwareElement674", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics673", type=BPMNProfile_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
outputDataItem675: BinaryAssociation = BinaryAssociation(
    name="outputDataItem675",
    ends={
        Property(name="BPMNProfile_DataOutput677", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics676", type=BPMNProfile_DataOutput, multiplicity=Multiplicity(1, 1))
    }
)
inputDataItem678: BinaryAssociation = BinaryAssociation(
    name="inputDataItem678",
    ends={
        Property(name="BPMNProfile_DataInput680", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics679", type=BPMNProfile_DataInput, multiplicity=Multiplicity(1, 1))
    }
)
oneBehaviorEventRef681: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef681",
    ends={
        Property(name="BPMNProfile_EventDefinition683", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics682", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
noneBehaviorEventRef684: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef684",
    ends={
        Property(name="BPMNProfile_EventDefinition686", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics685", type=BPMNProfile_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
complexBehaviorDefinition687: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition687",
    ends={
        Property(name="BPMNProfile_ComplexBehaviorDefinition689", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics688", type=BPMNProfile_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
loopCardinality662: BinaryAssociation = BinaryAssociation(
    name="loopCardinality662",
    ends={
        Property(name="BPMNProfile_BPMNExpression663", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition664: BinaryAssociation = BinaryAssociation(
    name="completionCondition664",
    ends={
        Property(name="BPMNProfile_BPMNExpression666", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics665", type=BPMNProfile_BPMNExpression, multiplicity=Multiplicity(0, 1))
    }
)
base_ExpansionRegion667: BinaryAssociation = BinaryAssociation(
    name="base_ExpansionRegion667",
    ends={
        Property(name="BPMNProfile_ExpansionRegion", type=BPMNProfile_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMNProfile_MultiInstanceLoopCharacteristics668", type=BPMNProfile_ExpansionRegion, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_BPMNProfile_InclusiveGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_InclusiveGateway)
gen_BPMNProfile_NonExclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_NonExclusiveGateway)
gen_BPMNProfile_Gateway_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_Gateway)
gen_BPMNProfile_FlowNode_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_FlowNode)
gen_BPMNProfile_FlowElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_FlowElement)
gen_BPMNProfile_Documentation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Documentation)
gen_BPMNProfile_BPMNAssociation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_BPMNAssociation)
gen_BPMNProfile_BPMNArtifact_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNArtifact)
gen_BPMNProfile_Auditing_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Auditing)
gen_BPMNProfile_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_FlowElementsContainer)
gen_BPMNProfile_LaneSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_LaneSet)
gen_BPMNProfile_Monitoring_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Monitoring)
gen_BPMNProfile_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CategoryValue)
gen_BPMNProfile_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_SequenceFlow)
gen_BPMNProfile_Lane_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Lane)
gen_BPMNProfile_BPMNExpression_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNExpression)
gen_BPMNProfile_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_EventBasedGateway)
gen_BPMNProfile_ParallelGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_ParallelGateway)
gen_BPMNProfile_ComplexGateway_NonExclusiveGateway = Generalization(general=NonExclusiveGateway, specific=BPMNProfile_ComplexGateway)
gen_BPMNProfile_RootElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_RootElement)
gen_BPMNProfile_Definitions_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Definitions)
gen_BPMNProfile_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMNProfile_ExclusiveGateway)
gen_BPMNProfile_BPMNProcess_CallableElement = Generalization(general=CallableElement, specific=BPMNProfile_BPMNProcess)
gen_BPMNProfile_BPMNProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMNProfile_BPMNProcess)
gen_BPMNProfile_BPMNRelationship_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNRelationship)
gen_BPMNProfile_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputOutputSpecification)
gen_BPMNProfile_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataInput)
gen_BPMNProfile_CallableElement_RootElement = Generalization(general=RootElement, specific=BPMNProfile_CallableElement)
gen_BPMNProfile_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ItemAwareElement)
gen_BPMNProfile_DataState_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_DataState)
gen_BPMNProfile_ItemDefinition_RootElement = Generalization(general=RootElement, specific=BPMNProfile_ItemDefinition)
gen_BPMNProfile_InputSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputSet)
gen_BPMNProfile_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataOutput)
gen_BPMNProfile_OutputSet_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_OutputSet)
gen_BPMNProfile_BPMNInterface_RootElement = Generalization(general=RootElement, specific=BPMNProfile_BPMNInterface)
gen_BPMNProfile_BPMNOperation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_BPMNOperation)
gen_BPMNProfile_Error_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Error)
gen_BPMNProfile_InputOutputBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_InputOutputBinding)
gen_BPMNProfile_BPMNCollaboration_RootElement = Generalization(general=RootElement, specific=BPMNProfile_BPMNCollaboration)
gen_BPMNProfile_BPMNMessage_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_BPMNMessage)
gen_BPMNProfile_Participant_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Participant)
gen_BPMNProfile_Participant_InteractionNode = Generalization(general=InteractionNode, specific=BPMNProfile_Participant)
gen_BPMNProfile_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ParticipantAssociation)
gen_BPMNProfile_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ConversationLink)
gen_BPMNProfile_ParticipantMultiplicity_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ParticipantMultiplicity)
gen_BPMNProfile_PartnerEntity_RootElement = Generalization(general=RootElement, specific=BPMNProfile_PartnerEntity)
gen_BPMNProfile_PartnerRole_RootElement = Generalization(general=RootElement, specific=BPMNProfile_PartnerRole)
gen_BPMNProfile_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_MessageFlow)
gen_BPMNProfile_ConversationNode_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ConversationNode)
gen_BPMNProfile_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=BPMNProfile_ConversationNode)
gen_BPMNProfile_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_MessageFlowAssociation)
gen_BPMNProfile_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationKey)
gen_BPMNProfile_CorrelationProperty_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationProperty)
gen_BPMNProfile_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationPropertyRetrievalExpression)
gen_BPMNProfile_FormalExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=BPMNProfile_FormalExpression)
gen_BPMNProfile_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationSubscription)
gen_BPMNProfile_BPMNProperty_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_BPMNProperty)
gen_BPMNProfile_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceRole)
gen_BPMNProfile_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_CorrelationPropertyBinding)
gen_BPMNProfile_ResourceAssignmentExpression_BPMNExpression = Generalization(general=BPMNExpression, specific=BPMNProfile_ResourceAssignmentExpression)
gen_BPMNProfile_Resource_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Resource)
gen_BPMNProfile_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceParameter)
gen_BPMNProfile_ResourceParameterBinding_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ResourceParameterBinding)
gen_BPMNProfile_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalScriptTask)
gen_BPMNProfile_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalBusinessRuleTask)
gen_BPMNProfile_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_CompensateEventDefinition)
gen_BPMNProfile_EventDefinition_RootElement = Generalization(general=RootElement, specific=BPMNProfile_EventDefinition)
gen_BPMNProfile_BPMNActivity_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_BPMNActivity)
gen_BPMNProfile_BPMNActivity_InteractionNode = Generalization(general=InteractionNode, specific=BPMNProfile_BPMNActivity)
gen_BPMNProfile_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=BPMNProfile_GlobalTask)
gen_BPMNProfile_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_BoundaryEvent)
gen_BPMNProfile_CatchEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=BPMNProfile_CatchEvent)
gen_BPMNProfile_BPMNEvent_FlowNode = Generalization(general=FlowNode, specific=BPMNProfile_BPMNEvent)
gen_BPMNProfile_BPMNEvent_InteractionNode = Generalization(general=InteractionNode, specific=BPMNProfile_BPMNEvent)
gen_BPMNProfile_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMNProfile_DataOutputAssociation)
gen_BPMNProfile_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_DataAssociation)
gen_BPMNProfile_Assignment_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Assignment)
gen_BPMNProfile_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMNProfile_DataInputAssociation)
gen_BPMNProfile_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_LoopCharacteristics)
gen_BPMNProfile_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_EscalationEventDefinition)
gen_BPMNProfile_Escalation_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_Escalation)
gen_BPMNProfile_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_TimerEventDefinition)
gen_BPMNProfile_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_SignalEventDefinition)
gen_BPMNProfile_BPMNSignal_ItemDefinition = Generalization(general=ItemDefinition, specific=BPMNProfile_BPMNSignal)
gen_BPMNProfile_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_EndEvent)
gen_BPMNProfile_ThrowEvent_BPMNEvent = Generalization(general=BPMNEvent, specific=BPMNProfile_ThrowEvent)
gen_BPMNProfile_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_MessageEventDefinition)
gen_BPMNProfile_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_StartEvent)
gen_BPMNProfile_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_ConditionalEventDefinition)
gen_BPMNProfile_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_LinkEventDefinition)
gen_BPMNProfile_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_ErrorEventDefinition)
gen_BPMNProfile_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMNProfile_IntermediateCatchEvent)
gen_BPMNProfile_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_IntermediateThrowEvent)
gen_BPMNProfile_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_TerminateEventDefinition)
gen_BPMNProfile_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMNProfile_ImplicitThrowEvent)
gen_BPMNProfile_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMNProfile_CancelEventDefinition)
gen_BPMNProfile_TextAnnotation_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_TextAnnotation)
gen_BPMNProfile_Category_RootElement = Generalization(general=RootElement, specific=BPMNProfile_Category)
gen_BPMNProfile_Group_BPMNArtifact = Generalization(general=BPMNArtifact, specific=BPMNProfile_Group)
gen_BPMNProfile_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataObjectReference)
gen_BPMNProfile_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataObjectReference)
gen_BPMNProfile_Rendering_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_Rendering)
gen_BPMNProfile_DataObject_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataObject)
gen_BPMNProfile_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataObject)
gen_BPMNProfile_DataStore_RootElement = Generalization(general=RootElement, specific=BPMNProfile_DataStore)
gen_BPMNProfile_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=BPMNProfile_DataStoreReference)
gen_BPMNProfile_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMNProfile_DataStoreReference)
gen_BPMNProfile_UserTask_Task = Generalization(general=Task, specific=BPMNProfile_UserTask)
gen_BPMNProfile_Task_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_Task)
gen_BPMNProfile_HumanPerformer_Performer = Generalization(general=Performer, specific=BPMNProfile_HumanPerformer)
gen_BPMNProfile_Performer_ResourceRole = Generalization(general=ResourceRole, specific=BPMNProfile_Performer)
gen_BPMNProfile_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalUserTask)
gen_BPMNProfile_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMNProfile_GlobalManualTask)
gen_BPMNProfile_ManualTask_Task = Generalization(general=Task, specific=BPMNProfile_ManualTask)
gen_BPMNProfile_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_SubConversation)
gen_BPMNProfile_GlobalConversation_BPMNCollaboration = Generalization(general=BPMNCollaboration, specific=BPMNProfile_GlobalConversation)
gen_BPMNProfile_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_CallConversation)
gen_BPMNProfile_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=BPMNProfile_PotentialOwner)
gen_BPMNProfile_SubProcess_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_SubProcess)
gen_BPMNProfile_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMNProfile_SubProcess)
gen_BPMNProfile_CallActivity_BPMNActivity = Generalization(general=BPMNActivity, specific=BPMNProfile_CallActivity)
gen_BPMNProfile_BusinessRuleTask_Task = Generalization(general=Task, specific=BPMNProfile_BusinessRuleTask)
gen_BPMNProfile_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMNProfile_Conversation)
gen_BPMNProfile_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=BPMNProfile_ComplexBehaviorDefinition)
gen_BPMNProfile_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=BPMNProfile_AdHocSubProcess)
gen_BPMNProfile_ScriptTask_Task = Generalization(general=Task, specific=BPMNProfile_ScriptTask)
gen_BPMNProfile_SendTask_Task = Generalization(general=Task, specific=BPMNProfile_SendTask)
gen_BPMNProfile_Transaction_SubProcess = Generalization(general=SubProcess, specific=BPMNProfile_Transaction)
gen_BPMNProfile_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMNProfile_StandardLoopCharacteristics)
gen_BPMNProfile_ReceiveTask_Task = Generalization(general=Task, specific=BPMNProfile_ReceiveTask)
gen_BPMNProfile_ServiceTask_Task = Generalization(general=Task, specific=BPMNProfile_ServiceTask)
gen_BPMNProfile_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMNProfile_MultiInstanceLoopCharacteristics)

# Domain Model
domain_model = DomainModel(
    name="BPMNProfile",
    types={BPMNProfile_InclusiveGateway, NonExclusiveGateway, BPMNProfile_SequenceFlow, BPMNProfile_NonExclusiveGateway, Gateway, BPMNProfile_JoinNode, BPMNProfile_ForkNode, BPMNProfile_Gateway, FlowNode, BPMNProfile_ControlNode, BPMNProfile_ActivityGroup, BPMNProfile_FlowNode, FlowElement, BPMNProfile_ActivityNode, BPMNProfile_FlowElement, BaseElement, BPMNProfile_Auditing, BPMNProfile_Monitoring, BPMNProfile_CategoryValue, BPMNProfile_FlowElementsContainer, BPMNProfile_BaseElement, BPMNProfile_ExtensionAttributeValue, BPMNProfile_Element, BPMNProfile_Documentation, BPMNProfile_ExtensionDefinition, BPMNProfile_BPMNAssociation, BPMNProfile_Property, BPMNProfile_Comment, BPMNProfile_Stereotype, BPMNArtifact, BPMNProfile_Dependency, BPMNProfile_BPMNArtifact, BPMNProfile_Class, BPMNProfile_Slot, BPMNProfile_ExtensionAttributeDefinition, BPMNProfile_LaneSet, BPMNProfile_ActivityPartition, BPMNProfile_Lane, BPMNProfile_EnumerationLiteral, BPMNProfile_OpaqueExpression, BPMNProfile_EventBasedGateway, BPMNProfile_StructuredActivityNode, BPMNProfile_InterruptibleActivityRegion, BPMNProfile_ParallelGateway, BPMNProfile_ComplexGateway, BPMNProfile_ControlFlow, BPMNProfile_BPMNExpression, BPMNProfile_MergeNode, BPMNProfile_RootElement, BPMNProfile_PackageableElement, BPMNProfile_Definitions, BPMNProfile_Package, BPMNProfile_BPMNExtension, BPMNProfile_Import, BPMNProfile_BPMNRelationship, BPMNProfile_PackageImport, BPMNProfile_ExclusiveGateway, BPMNProfile_DecisionNode, BPMNProfile_BPMNProcess, CallableElement, FlowElementsContainer, BPMNProfile_BPMNCollaboration, BPMNProfile_Activity, BPMNProfile_CorrelationSubscription, BPMNProfile_Constraint, BPMNProfile_Behavior, BPMNProfile_InputOutputSpecification, BPMNProfile_BPMNInterface, BPMNProfile_InputOutputBinding, BPMNProfile_Action, BPMNProfile_DataInput, BPMNProfile_DataOutput, BPMNProfile_InputSet, BPMNProfile_OutputSet, ItemAwareElement, BPMNProfile_BPMNProperty, BPMNProfile_ResourceRole, BPMNProfile_CallableElement, RootElement, BPMNProfile_Parameter, BPMNProfile_ActivityParameterNode, BPMNProfile_ItemAwareElement, BPMNProfile_DataState, BPMNProfile_TypedElement, BPMNProfile_ItemDefinition, BPMNProfile_State, BPMNProfile_InputPin, BPMNProfile_ParameterSet, BPMNProfile_OutputPin, BPMNProfile_Interface, BPMNProfile_BPMNOperation, BPMNProfile_Operation, BPMNProfile_BPMNMessage, BPMNProfile_ParticipantAssociation, BPMNProfile_ConversationLink, BPMNProfile_MessageFlowAssociation, BPMNProfile_MessageFlow, BPMNProfile_Collaboration, BPMNProfile_ConversationNode, BPMNProfile_Error, ItemDefinition, InteractionNode, BPMNProfile_CorrelationKey, BPMNProfile_Participant, BPMNProfile_ParticipantMultiplicity, BPMNProfile_PartnerEntity, BPMNProfile_PartnerRole, BPMNProfile_InteractionNode, BPMNProfile_MultiplicityElement, BPMNProfile_InstanceSpecification, BPMNProfile_InformationFlow, BPMNProfile_CorrelationProperty, BPMNProfile_CorrelationPropertyRetrievalExpression, BPMNProfile_FormalExpression, BPMNExpression, BPMNProfile_CorrelationPropertyBinding, BPMNProfile_DataStoreNode, BPMNProfile_ResourceAssignmentExpression, BPMNProfile_Resource, BPMNProfile_ResourceParameterBinding, BPMNProfile_ResourceParameter, BPMNProfile_GlobalScriptTask, GlobalTask, BPMNProfile_OpaqueBehavior, BPMNProfile_GlobalBusinessRuleTask, BPMNProfile_CompensateEventDefinition, EventDefinition, BPMNProfile_BPMNActivity, BPMNProfile_CallEvent, BPMNProfile_EventDefinition, BPMNProfile_Event, BPMNProfile_GlobalTask, BPMNProfile_BoundaryEvent, BPMNProfile_DataInputAssociation, BPMNProfile_DataOutputAssociation, BPMNProfile_LoopCharacteristics, CatchEvent, BPMNProfile_CatchEvent, BPMNEvent, BPMNProfile_AcceptEventAction, BPMNProfile_InitialNode, BPMNProfile_BPMNEvent, DataAssociation, BPMNProfile_DataAssociation, BPMNProfile_ObjectFlow, BPMNProfile_Assignment, BPMNProfile_EscalationEventDefinition, BPMNProfile_Escalation, BPMNProfile_TimerEventDefinition, BPMNProfile_ChangeEvent, BPMNProfile_SignalEventDefinition, BPMNProfile_BPMNSignal, BPMNProfile_EndEvent, ThrowEvent, BPMNProfile_FinalNode, BPMNProfile_ThrowEvent, BPMNProfile_CallOperationAction, BPMNProfile_FlowFinalNode, BPMNProfile_MessageEventDefinition, BPMNProfile_StartEvent, BPMNProfile_ConditionalEventDefinition, BPMNProfile_LinkEventDefinition, BPMNProfile_ErrorEventDefinition, BPMNProfile_IntermediateCatchEvent, BPMNProfile_IntermediateThrowEvent, BPMNProfile_SendObjectAction, BPMNProfile_TerminateEventDefinition, BPMNProfile_ImplicitThrowEvent, BPMNProfile_CancelEventDefinition, BPMNProfile_TextAnnotation, BPMNProfile_Category, BPMNProfile_Enumeration, BPMNProfile_Group, BPMNProfile_DataObjectReference, BPMNProfile_DataObject, BPMNProfile_DataStore, BPMNProfile_DataStoreReference, BPMNProfile_UserTask, Task, BPMNProfile_OpaqueAction, BPMNProfile_Rendering, BPMNProfile_Task, BPMNActivity, BPMNProfile_Image, BPMNProfile_HumanPerformer, Performer, BPMNProfile_Performer, ResourceRole, BPMNProfile_GlobalUserTask, BPMNProfile_GlobalManualTask, BPMNProfile_ManualTask, BPMNProfile_PotentialOwner, BPMNProfile_GlobalConversation, BPMNCollaboration, BPMNProfile_CallConversation, BPMNProfile_CollaborationUse, HumanPerformer, BPMNProfile_SubConversation, ConversationNode, BPMNProfile_CallActivity, BPMNProfile_CallBehaviorAction, BPMNProfile_BusinessRuleTask, BPMNProfile_Conversation, BPMNProfile_SubProcess, BPMNProfile_ComplexBehaviorDefinition, BPMNProfile_AdHocSubProcess, SubProcess, BPMNProfile_ScriptTask, BPMNProfile_SendTask, BPMNProfile_Transaction, BPMNProfile_StandardLoopCharacteristics, LoopCharacteristics, BPMNProfile_LoopNode, BPMNProfile_ReceiveTask, BPMNProfile_ServiceTask, BPMNProfile_MultiInstanceLoopCharacteristics, BPMNProfile_ExpansionRegion, AssociationDirection, EventBasedGatewayType, GatewayDirection, RelationshipDirection, ItemKind, ProcessType, AdHocOrdering, MultiInstanceBehavior},
    associations={default0, base_JoinNode1, base_ForkNode2, base_ControlNode4, base_ActivityGroup5, base_ActivityNode7, auditing8, monitoring9, _categoryValueRef11, container12, extensionValues13, base_Element14, documentation16, extensionDefinitions18, outgoing20, incoming21, base_Property30, base_Comment32, base_Stereotype34, extensionAttributeDefinitions36, base_Dependency39, targetRef40, sourceRef41, base_Class43, base_Slot23, valueRef25, extensionAttributeDefinition28, laneSets50, flowElements51, base_ActivityPartition53, lanes54, parentLane55, flowElementsContainer57, base_Class45, base_EnumerationLiteral48, categorizedFlowElements49, base_ActivityPartition59, _partitionElement62, flowNodeRefs65, partitionElementRef68, childLaneSet71, laneSet74, sourceRef80, targetRef83, base_OpaqueExpression86, base_ForkNode88, base_StructuredActivityNode90, base_InterruptibleActivityRegion92, default94, base_ControlFlow76, conditionExpression78, base_MergeNode100, default102, base_PackageableElement105, definition106, base_Package107, extensions108, imports110, relationships112, rootElements114, base_Stereotype115, definition118, base_PackageImport121, definitions123, activationCondition96, base_DecisionNode99, definition134, auditing137, definitionalCollaborationRef139, base_Activity141, correlationSubscriptions143, base_Constraint126, targets128, sources131, base_Behavior154, ioSpecification155, supportedInterfaceRefs157, ioBinding159, base_Behavior161, base_Action164, dataInputs166, dataOutputs168, inputSets170, outputSets172, monitoring145, supports149, properties151, resources153, base_InputPin174, base_Parameter176, base_ActivityParameterNode178, inputSetRefs180, inputSetWithOptional181, inputSetWithWhileExecuting183, dataState185, base_TypedElement186, itemSubjectRef188, base_State190, base_Class192, structureRef195, base_ParameterSet201, optionalInputRefs203, whileExecutingInputRefs204, dataInputRefs206, import198, base_ActivityParameterNode213, outputSetRefs216, outputSetWithOptional217, outputSetWithWhileExecuting220, base_ParameterSet223, optionalOutputRefs226, whileExecutingOutputRefs229, dataOutputRefs232, base_OutputPin208, base_Parameter210, base_Interface233, implementationRef235, operations238, callableElements240, base_Operation243, implementationRef245, inMessageRef248, itemRef255, inputDataRef258, outputDataRef261, operationRef264, base_Dependency267, participantAssociations270, conversationLinks272, messageFlowAssociations273, messageFlows275, base_Collaboration277, outMessageRef250, errorRef253, base_Dependency285, innerParticipantRef288, outerParticipantRef291, conversations279, correlationKeys281, participants283, base_Property294, processRef297, participantMultiplicity300, partnerEntityRef302, partnerRoleRef303, interfaceRefs305, base_InteractionNode_Element308, outgoingConversationLinks310, incomingConversationLinks313, collaboration316, base_Dependency317, targetRef319, sourceRef320, base_MultiplicityElement322, base_InstanceSpecification324, participantRef325, base_Class326, participantRef328, base_Dependency330, innerMessageFlowRef333, outerMessageFlowRef336, base_InformationFlow339, sourceRef341, targetRef344, messageRef347, base_Class362, correlationPropertyRef365, base_Property367, type370, correlationPropertyRetrievalExpression373, base_Dependency375, messageRef378, messagePath381, evaluatesToTypeRef383, base_Class386, correlationKeyRef389, base_InformationFlow350, messageFlowRefs353, correlationKeys356, participantRefs359, base_DataStoreNode403, umlProperty405, correlationPropertyBinding392, base_Property394, dataPath397, correlationPropertyRef400, base_Property408, resourceAssignmentExpression410, resourceRef412, resourceParameterBindings414, process416, expression417, resourceParameters420, base_Property422, type425, base_Slot428, parameterRef431, expression434, base_OpaqueBehavior437, resources438, activityRef441, base_CallEvent442, base_Event444, base_Action445, activityClass448, properties451, default454, boundaryEventRefs457, dataInputAssociations459, dataOutputAssociations461, loopCharacteristics463, resources465, attachedToRef468, base_AcceptEventAction471, base_InitialNode472, dataOutputAssociation474, eventClass477, _eventDefinitions479, properties482, eventDefinitionRefs485, sourceRef489, targetRef492, transformation495, assignment498, base_Dependency500, from503, to506, base_StructuredActivityNode509, escalationRef512, base_ObjectFlow488, timeCycle516, timeDate518, timeDuration521, base_ChangeEvent524, signalRef526, base_CallEvent527, base_FinalNode530, base_CallEvent513, base_CallOperationAction531, base_FlowFinalNode532, dataInputAssociation534, messageRef537, operationRef539, base_CallEvent542, base_ChangeEvent545, condition547, _target551, source553, base_CallEvent555, errorRef557, base_CallEvent559, base_DataStoreNode579, base_SendObjectAction562, base_CallEvent563, base_CallEvent565, base_Comment567, base_Enumeration569, categoryValue570, base_ActivityPartition573, _categoryValueRef575, dataObjectRef578, base_DataStoreNode582, base_Class585, itemSubjectRef587, _dataStore590, base_DataStoreNode592, base_OpaqueAction595, renderings596, ioSpecification598, base_Image600, renderings602, base_OpaqueAction604, conversationNodes606, _collaborationUse608, calledCollaborationRef609, participantAssociations612, base_StructuredActivityNode615, hasLaneSets617, base_CallBehaviorAction620, calledElementRef621, base_OpaqueAction624, condition626, event628, base_ControlFlow630, completionCondition633, base_OpaqueAction635, messageRef637, base_CallOperationAction639, operationRef642, base_LoopNode645, loopCondition646, messageRef649, base_AcceptEventAction651, operationRef654, base_CallOperationAction657, operationRef659, loopDataInputRef669, loopDataOutputRef672, outputDataItem675, inputDataItem678, oneBehaviorEventRef681, noneBehaviorEventRef684, complexBehaviorDefinition687, loopCardinality662, completionCondition664, base_ExpansionRegion667},
    generalizations={gen_BPMNProfile_InclusiveGateway_NonExclusiveGateway, gen_BPMNProfile_NonExclusiveGateway_Gateway, gen_BPMNProfile_Gateway_FlowNode, gen_BPMNProfile_FlowNode_FlowElement, gen_BPMNProfile_FlowElement_BaseElement, gen_BPMNProfile_Documentation_BaseElement, gen_BPMNProfile_BPMNAssociation_BPMNArtifact, gen_BPMNProfile_BPMNArtifact_BaseElement, gen_BPMNProfile_Auditing_BaseElement, gen_BPMNProfile_FlowElementsContainer_BaseElement, gen_BPMNProfile_LaneSet_BaseElement, gen_BPMNProfile_Monitoring_BaseElement, gen_BPMNProfile_CategoryValue_BaseElement, gen_BPMNProfile_SequenceFlow_FlowElement, gen_BPMNProfile_Lane_BaseElement, gen_BPMNProfile_BPMNExpression_BaseElement, gen_BPMNProfile_EventBasedGateway_Gateway, gen_BPMNProfile_ParallelGateway_NonExclusiveGateway, gen_BPMNProfile_ComplexGateway_NonExclusiveGateway, gen_BPMNProfile_RootElement_BaseElement, gen_BPMNProfile_Definitions_BaseElement, gen_BPMNProfile_ExclusiveGateway_Gateway, gen_BPMNProfile_BPMNProcess_CallableElement, gen_BPMNProfile_BPMNProcess_FlowElementsContainer, gen_BPMNProfile_BPMNRelationship_BaseElement, gen_BPMNProfile_InputOutputSpecification_BaseElement, gen_BPMNProfile_DataInput_ItemAwareElement, gen_BPMNProfile_CallableElement_RootElement, gen_BPMNProfile_ItemAwareElement_BaseElement, gen_BPMNProfile_DataState_BaseElement, gen_BPMNProfile_ItemDefinition_RootElement, gen_BPMNProfile_InputSet_BaseElement, gen_BPMNProfile_DataOutput_ItemAwareElement, gen_BPMNProfile_OutputSet_BaseElement, gen_BPMNProfile_BPMNInterface_RootElement, gen_BPMNProfile_BPMNOperation_BaseElement, gen_BPMNProfile_Error_ItemDefinition, gen_BPMNProfile_InputOutputBinding_BaseElement, gen_BPMNProfile_BPMNCollaboration_RootElement, gen_BPMNProfile_BPMNMessage_ItemDefinition, gen_BPMNProfile_Participant_BaseElement, gen_BPMNProfile_Participant_InteractionNode, gen_BPMNProfile_ParticipantAssociation_BaseElement, gen_BPMNProfile_ConversationLink_BaseElement, gen_BPMNProfile_ParticipantMultiplicity_BaseElement, gen_BPMNProfile_PartnerEntity_RootElement, gen_BPMNProfile_PartnerRole_RootElement, gen_BPMNProfile_MessageFlow_BaseElement, gen_BPMNProfile_ConversationNode_BaseElement, gen_BPMNProfile_ConversationNode_InteractionNode, gen_BPMNProfile_MessageFlowAssociation_BaseElement, gen_BPMNProfile_CorrelationKey_BaseElement, gen_BPMNProfile_CorrelationProperty_BaseElement, gen_BPMNProfile_CorrelationPropertyRetrievalExpression_BaseElement, gen_BPMNProfile_FormalExpression_BPMNExpression, gen_BPMNProfile_CorrelationSubscription_BaseElement, gen_BPMNProfile_BPMNProperty_ItemAwareElement, gen_BPMNProfile_ResourceRole_BaseElement, gen_BPMNProfile_CorrelationPropertyBinding_BaseElement, gen_BPMNProfile_ResourceAssignmentExpression_BPMNExpression, gen_BPMNProfile_Resource_ItemDefinition, gen_BPMNProfile_ResourceParameter_BaseElement, gen_BPMNProfile_ResourceParameterBinding_BaseElement, gen_BPMNProfile_GlobalScriptTask_GlobalTask, gen_BPMNProfile_GlobalBusinessRuleTask_GlobalTask, gen_BPMNProfile_CompensateEventDefinition_EventDefinition, gen_BPMNProfile_EventDefinition_RootElement, gen_BPMNProfile_BPMNActivity_FlowNode, gen_BPMNProfile_BPMNActivity_InteractionNode, gen_BPMNProfile_GlobalTask_CallableElement, gen_BPMNProfile_BoundaryEvent_CatchEvent, gen_BPMNProfile_CatchEvent_BPMNEvent, gen_BPMNProfile_BPMNEvent_FlowNode, gen_BPMNProfile_BPMNEvent_InteractionNode, gen_BPMNProfile_DataOutputAssociation_DataAssociation, gen_BPMNProfile_DataAssociation_BaseElement, gen_BPMNProfile_Assignment_BaseElement, gen_BPMNProfile_DataInputAssociation_DataAssociation, gen_BPMNProfile_LoopCharacteristics_BaseElement, gen_BPMNProfile_EscalationEventDefinition_EventDefinition, gen_BPMNProfile_Escalation_ItemDefinition, gen_BPMNProfile_TimerEventDefinition_EventDefinition, gen_BPMNProfile_SignalEventDefinition_EventDefinition, gen_BPMNProfile_BPMNSignal_ItemDefinition, gen_BPMNProfile_EndEvent_ThrowEvent, gen_BPMNProfile_ThrowEvent_BPMNEvent, gen_BPMNProfile_MessageEventDefinition_EventDefinition, gen_BPMNProfile_StartEvent_CatchEvent, gen_BPMNProfile_ConditionalEventDefinition_EventDefinition, gen_BPMNProfile_LinkEventDefinition_EventDefinition, gen_BPMNProfile_ErrorEventDefinition_EventDefinition, gen_BPMNProfile_IntermediateCatchEvent_CatchEvent, gen_BPMNProfile_IntermediateThrowEvent_ThrowEvent, gen_BPMNProfile_TerminateEventDefinition_EventDefinition, gen_BPMNProfile_ImplicitThrowEvent_ThrowEvent, gen_BPMNProfile_CancelEventDefinition_EventDefinition, gen_BPMNProfile_TextAnnotation_BPMNArtifact, gen_BPMNProfile_Category_RootElement, gen_BPMNProfile_Group_BPMNArtifact, gen_BPMNProfile_DataObjectReference_FlowElement, gen_BPMNProfile_DataObjectReference_ItemAwareElement, gen_BPMNProfile_Rendering_BaseElement, gen_BPMNProfile_DataObject_FlowElement, gen_BPMNProfile_DataObject_ItemAwareElement, gen_BPMNProfile_DataStore_RootElement, gen_BPMNProfile_DataStoreReference_FlowElement, gen_BPMNProfile_DataStoreReference_ItemAwareElement, gen_BPMNProfile_UserTask_Task, gen_BPMNProfile_Task_BPMNActivity, gen_BPMNProfile_HumanPerformer_Performer, gen_BPMNProfile_Performer_ResourceRole, gen_BPMNProfile_GlobalUserTask_GlobalTask, gen_BPMNProfile_GlobalManualTask_GlobalTask, gen_BPMNProfile_ManualTask_Task, gen_BPMNProfile_SubConversation_ConversationNode, gen_BPMNProfile_GlobalConversation_BPMNCollaboration, gen_BPMNProfile_CallConversation_ConversationNode, gen_BPMNProfile_PotentialOwner_HumanPerformer, gen_BPMNProfile_SubProcess_BPMNActivity, gen_BPMNProfile_SubProcess_FlowElementsContainer, gen_BPMNProfile_CallActivity_BPMNActivity, gen_BPMNProfile_BusinessRuleTask_Task, gen_BPMNProfile_Conversation_ConversationNode, gen_BPMNProfile_ComplexBehaviorDefinition_BaseElement, gen_BPMNProfile_AdHocSubProcess_SubProcess, gen_BPMNProfile_ScriptTask_Task, gen_BPMNProfile_SendTask_Task, gen_BPMNProfile_Transaction_SubProcess, gen_BPMNProfile_StandardLoopCharacteristics_LoopCharacteristics, gen_BPMNProfile_ReceiveTask_Task, gen_BPMNProfile_ServiceTask_Task, gen_BPMNProfile_MultiInstanceLoopCharacteristics_LoopCharacteristics},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)