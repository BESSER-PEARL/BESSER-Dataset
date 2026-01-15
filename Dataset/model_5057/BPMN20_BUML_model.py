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
ItemKind: Enumeration = Enumeration(
    name="ItemKind",
    literals={
            EnumerationLiteral(name="Physical"),
			EnumerationLiteral(name="Information")
    }
)

ProcessType: Enumeration = Enumeration(
    name="ProcessType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Public"),
			EnumerationLiteral(name="Private")
    }
)

GatewayDirection: Enumeration = Enumeration(
    name="GatewayDirection",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="Converging"),
			EnumerationLiteral(name="Diverging"),
			EnumerationLiteral(name="Mixed")
    }
)

EventBasedGatewayType: Enumeration = Enumeration(
    name="EventBasedGatewayType",
    literals={
            EnumerationLiteral(name="Parallel"),
			EnumerationLiteral(name="Exclusive")
    }
)

RelationshipDirection: Enumeration = Enumeration(
    name="RelationshipDirection",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Forward"),
			EnumerationLiteral(name="Backward"),
			EnumerationLiteral(name="Both")
    }
)

ChoreographyLoopType: Enumeration = Enumeration(
    name="ChoreographyLoopType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Standard"),
			EnumerationLiteral(name="MultiInstanceSequential"),
			EnumerationLiteral(name="MultiInstanceParallel")
    }
)

AssociationDirection: Enumeration = Enumeration(
    name="AssociationDirection",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="Both")
    }
)

MultiInstanceBehavior: Enumeration = Enumeration(
    name="MultiInstanceBehavior",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Complex")
    }
)

AdHocOrdering: Enumeration = Enumeration(
    name="AdHocOrdering",
    literals={
            EnumerationLiteral(name="Parallel"),
			EnumerationLiteral(name="Sequential")
    }
)

# Classes
bpmn2_Interface = Class(name="bpmn2::Interface")
RootElement = Class(name="RootElement")
bpmn2_Operation = Class(name="bpmn2::Operation")
bpmn2_EObject = Class(name="bpmn2::EObject")
bpmn2_Message = Class(name="bpmn2::Message")
bpmn2_Error = Class(name="bpmn2::Error")
bpmn2_RootElement = Class(name="bpmn2::RootElement", is_abstract=True)
BaseElement = Class(name="BaseElement")
bpmn2_BaseElement = Class(name="bpmn2::BaseElement", is_abstract=True)
bpmn2_ExtensionDefinition = Class(name="bpmn2::ExtensionDefinition")
bpmn2_ExtensionAttributeValue = Class(name="bpmn2::ExtensionAttributeValue")
bpmn2_Documentation = Class(name="bpmn2::Documentation")
bpmn2_ExtensionAttributeDefinition = Class(name="bpmn2::ExtensionAttributeDefinition")
bpmn2_ResourceRole = Class(name="bpmn2::ResourceRole")
bpmn2_CallableElement = Class(name="bpmn2::CallableElement", is_abstract=True)
bpmn2_InputOutputSpecification = Class(name="bpmn2::InputOutputSpecification")
bpmn2_InputOutputBinding = Class(name="bpmn2::InputOutputBinding")
bpmn2_ItemDefinition = Class(name="bpmn2::ItemDefinition")
bpmn2_Import = Class(name="bpmn2::Import")
bpmn2_EndPoint = Class(name="bpmn2::EndPoint")
bpmn2_Auditing = Class(name="bpmn2::Auditing")
bpmn2_GlobalTask = Class(name="bpmn2::GlobalTask")
CallableElement = Class(name="CallableElement")
bpmn2_ItemAwareElement = Class(name="bpmn2::ItemAwareElement")
bpmn2_DataState = Class(name="bpmn2::DataState")
bpmn2_InputSet = Class(name="bpmn2::InputSet")
bpmn2_OutputSet = Class(name="bpmn2::OutputSet")
bpmn2_DataInput = Class(name="bpmn2::DataInput")
bpmn2_DataOutput = Class(name="bpmn2::DataOutput")
ItemAwareElement = Class(name="ItemAwareElement")
bpmn2_ResourceParameterBinding = Class(name="bpmn2::ResourceParameterBinding")
bpmn2_ResourceAssignmentExpression = Class(name="bpmn2::ResourceAssignmentExpression")
bpmn2_ResourceParameter = Class(name="bpmn2::ResourceParameter")
bpmn2_Resource = Class(name="bpmn2::Resource")
bpmn2_Artifact = Class(name="bpmn2::Artifact", is_abstract=True)
bpmn2_CorrelationSubscription = Class(name="bpmn2::CorrelationSubscription")
bpmn2_Expression = Class(name="bpmn2::Expression")
bpmn2_Monitoring = Class(name="bpmn2::Monitoring")
bpmn2_Performer = Class(name="bpmn2::Performer")
ResourceRole = Class(name="ResourceRole")
bpmn2_Process = Class(name="bpmn2::Process")
FlowElementsContainer = Class(name="FlowElementsContainer")
bpmn2_Property = Class(name="bpmn2::Property")
bpmn2_Collaboration = Class(name="bpmn2::Collaboration")
FlowElement = Class(name="FlowElement")
bpmn2_SequenceFlow = Class(name="bpmn2::SequenceFlow")
bpmn2_FlowElementsContainer = Class(name="bpmn2::FlowElementsContainer", is_abstract=True)
bpmn2_FlowElement = Class(name="bpmn2::FlowElement", is_abstract=True)
bpmn2_LaneSet = Class(name="bpmn2::LaneSet")
bpmn2_CategoryValue = Class(name="bpmn2::CategoryValue")
bpmn2_Lane = Class(name="bpmn2::Lane")
bpmn2_FlowNode = Class(name="bpmn2::FlowNode", is_abstract=True)
bpmn2_CorrelationKey = Class(name="bpmn2::CorrelationKey")
bpmn2_ConversationNode = Class(name="bpmn2::ConversationNode", is_abstract=True)
bpmn2_ConversationLink = Class(name="bpmn2::ConversationLink")
Collaboration = Class(name="Collaboration")
bpmn2_Choreography = Class(name="bpmn2::Choreography")
bpmn2_ParticipantAssociation = Class(name="bpmn2::ParticipantAssociation")
bpmn2_MessageFlowAssociation = Class(name="bpmn2::MessageFlowAssociation")
bpmn2_ConversationAssociation = Class(name="bpmn2::ConversationAssociation")
bpmn2_Participant = Class(name="bpmn2::Participant")
bpmn2_MessageFlow = Class(name="bpmn2::MessageFlow")
bpmn2_ParticipantMultiplicity = Class(name="bpmn2::ParticipantMultiplicity")
bpmn2_InteractionNode = Class(name="bpmn2::InteractionNode", is_abstract=True)
InteractionNode = Class(name="InteractionNode")
bpmn2_CorrelationProperty = Class(name="bpmn2::CorrelationProperty")
bpmn2_CorrelationPropertyRetrievalExpression = Class(name="bpmn2::CorrelationPropertyRetrievalExpression")
bpmn2_FormalExpression = Class(name="bpmn2::FormalExpression")
bpmn2_CorrelationPropertyBinding = Class(name="bpmn2::CorrelationPropertyBinding")
bpmn2_GlobalManualTask = Class(name="bpmn2::GlobalManualTask")
GlobalTask = Class(name="GlobalTask")
bpmn2_ManualTask = Class(name="bpmn2::ManualTask")
Task = Class(name="Task")
bpmn2_Task = Class(name="bpmn2::Task")
Activity = Class(name="Activity")
bpmn2_Activity = Class(name="bpmn2::Activity", is_abstract=True)
FlowNode = Class(name="FlowNode")
bpmn2_LoopCharacteristics = Class(name="bpmn2::LoopCharacteristics", is_abstract=True)
bpmn2_BoundaryEvent = Class(name="bpmn2::BoundaryEvent")
bpmn2_DataInputAssociation = Class(name="bpmn2::DataInputAssociation")
bpmn2_DataOutputAssociation = Class(name="bpmn2::DataOutputAssociation")
Expression = Class(name="Expression")
bpmn2_CatchEvent = Class(name="bpmn2::CatchEvent", is_abstract=True)
Event = Class(name="Event")
bpmn2_EventDefinition = Class(name="bpmn2::EventDefinition", is_abstract=True)
bpmn2_Event = Class(name="bpmn2::Event", is_abstract=True)
DataAssociation = Class(name="DataAssociation")
bpmn2_DataAssociation = Class(name="bpmn2::DataAssociation")
bpmn2_Assignment = Class(name="bpmn2::Assignment")
CatchEvent = Class(name="CatchEvent")
bpmn2_Rendering = Class(name="bpmn2::Rendering")
bpmn2_HumanPerformer = Class(name="bpmn2::HumanPerformer")
Performer = Class(name="Performer")
bpmn2_PotentialOwner = Class(name="bpmn2::PotentialOwner")
HumanPerformer = Class(name="HumanPerformer")
bpmn2_GlobalUserTask = Class(name="bpmn2::GlobalUserTask")
bpmn2_Gateway = Class(name="bpmn2::Gateway", is_abstract=True)
bpmn2_EventBasedGateway = Class(name="bpmn2::EventBasedGateway")
Gateway = Class(name="Gateway")
bpmn2_ComplexGateway = Class(name="bpmn2::ComplexGateway")
bpmn2_ExclusiveGateway = Class(name="bpmn2::ExclusiveGateway")
bpmn2_InclusiveGateway = Class(name="bpmn2::InclusiveGateway")
bpmn2_UserTask = Class(name="bpmn2::UserTask")
bpmn2_Extension = Class(name="bpmn2::Extension")
bpmn2_IntermediateCatchEvent = Class(name="bpmn2::IntermediateCatchEvent")
bpmn2_IntermediateThrowEvent = Class(name="bpmn2::IntermediateThrowEvent")
ThrowEvent = Class(name="ThrowEvent")
bpmn2_ThrowEvent = Class(name="bpmn2::ThrowEvent", is_abstract=True)
bpmn2_EndEvent = Class(name="bpmn2::EndEvent")
bpmn2_StartEvent = Class(name="bpmn2::StartEvent")
bpmn2_CancelEventDefinition = Class(name="bpmn2::CancelEventDefinition")
bpmn2_ParallelGateway = Class(name="bpmn2::ParallelGateway")
bpmn2_Relationship = Class(name="bpmn2::Relationship")
bpmn2_EscalationEventDefinition = Class(name="bpmn2::EscalationEventDefinition")
bpmn2_Escalation = Class(name="bpmn2::Escalation")
bpmn2_CompensateEventDefinition = Class(name="bpmn2::CompensateEventDefinition")
bpmn2_TimerEventDefinition = Class(name="bpmn2::TimerEventDefinition")
bpmn2_LinkEventDefinition = Class(name="bpmn2::LinkEventDefinition")
EventDefinition = Class(name="EventDefinition")
bpmn2_ErrorEventDefinition = Class(name="bpmn2::ErrorEventDefinition")
bpmn2_TerminateEventDefinition = Class(name="bpmn2::TerminateEventDefinition")
bpmn2_ConditionalEventDefinition = Class(name="bpmn2::ConditionalEventDefinition")
bpmn2_SignalEventDefinition = Class(name="bpmn2::SignalEventDefinition")
bpmn2_Signal = Class(name="bpmn2::Signal")
bpmn2_ImplicitThrowEvent = Class(name="bpmn2::ImplicitThrowEvent")
bpmn2_DataObject = Class(name="bpmn2::DataObject")
bpmn2_DataStore = Class(name="bpmn2::DataStore")
bpmn2_MessageEventDefinition = Class(name="bpmn2::MessageEventDefinition")
bpmn2_DataObjectReference = Class(name="bpmn2::DataObjectReference")
bpmn2_CallConversation = Class(name="bpmn2::CallConversation")
ConversationNode = Class(name="ConversationNode")
bpmn2_Conversation = Class(name="bpmn2::Conversation")
bpmn2_SubConversation = Class(name="bpmn2::SubConversation")
bpmn2_GlobalConversation = Class(name="bpmn2::GlobalConversation")
bpmn2_PartnerEntity = Class(name="bpmn2::PartnerEntity")
bpmn2_PartnerRole = Class(name="bpmn2::PartnerRole")
bpmn2_DataStoreReference = Class(name="bpmn2::DataStoreReference")
bpmn2_ChoreographyActivity = Class(name="bpmn2::ChoreographyActivity", is_abstract=True)
bpmn2_CallChoreography = Class(name="bpmn2::CallChoreography")
ChoreographyActivity = Class(name="ChoreographyActivity")
bpmn2_SubChoreography = Class(name="bpmn2::SubChoreography")
bpmn2_GlobalChoreographyTask = Class(name="bpmn2::GlobalChoreographyTask")
Choreography = Class(name="Choreography")
bpmn2_TextAnnotation = Class(name="bpmn2::TextAnnotation")
Artifact = Class(name="Artifact")
bpmn2_Group = Class(name="bpmn2::Group")
bpmn2_Association = Class(name="bpmn2::Association")
bpmn2_Category = Class(name="bpmn2::Category")
bpmn2_ChoreographyTask = Class(name="bpmn2::ChoreographyTask")
bpmn2_SubProcess = Class(name="bpmn2::SubProcess")
bpmn2_MultiInstanceLoopCharacteristics = Class(name="bpmn2::MultiInstanceLoopCharacteristics")
LoopCharacteristics = Class(name="LoopCharacteristics")
bpmn2_ServiceTask = Class(name="bpmn2::ServiceTask")
bpmn2_ComplexBehaviorDefinition = Class(name="bpmn2::ComplexBehaviorDefinition")
bpmn2_StandardLoopCharacteristics = Class(name="bpmn2::StandardLoopCharacteristics")
bpmn2_CallActivity = Class(name="bpmn2::CallActivity")
bpmn2_ReceiveTask = Class(name="bpmn2::ReceiveTask")
bpmn2_ScriptTask = Class(name="bpmn2::ScriptTask")
bpmn2_BusinessRuleTask = Class(name="bpmn2::BusinessRuleTask")
bpmn2_AdHocSubProcess = Class(name="bpmn2::AdHocSubProcess")
SubProcess = Class(name="SubProcess")
bpmn2_SendTask = Class(name="bpmn2::SendTask")
bpmn2_Transaction = Class(name="bpmn2::Transaction")
bpmn2_GlobalScriptTask = Class(name="bpmn2::GlobalScriptTask")
bpmn2_GlobalBusinessRuleTask = Class(name="bpmn2::GlobalBusinessRuleTask")
bpmn2_Definitions = Class(name="bpmn2::Definitions")
bpmn2_BPMNDiagram = Class(name="bpmn2::BPMNDiagram")

# bpmn2_Interface class attributes and methods
bpmn2_Interface_name: Property = Property(name="name", type=StringType)
bpmn2_Interface.attributes={bpmn2_Interface_name}

# RootElement class attributes and methods

# bpmn2_Operation class attributes and methods
bpmn2_Operation_name: Property = Property(name="name", type=StringType)
bpmn2_Operation.attributes={bpmn2_Operation_name}

# bpmn2_EObject class attributes and methods

# bpmn2_Message class attributes and methods
bpmn2_Message_name: Property = Property(name="name", type=StringType)
bpmn2_Message.attributes={bpmn2_Message_name}

# bpmn2_Error class attributes and methods
bpmn2_Error_name: Property = Property(name="name", type=StringType)
bpmn2_Error_errorCode: Property = Property(name="errorCode", type=StringType)
bpmn2_Error.attributes={bpmn2_Error_name, bpmn2_Error_errorCode}

# bpmn2_RootElement class attributes and methods

# BaseElement class attributes and methods

# bpmn2_BaseElement class attributes and methods
bpmn2_BaseElement_id: Property = Property(name="id", type=StringType)
bpmn2_BaseElement_description: Property = Property(name="description", type=StringType)
bpmn2_BaseElement.attributes={bpmn2_BaseElement_id, bpmn2_BaseElement_description}

# bpmn2_ExtensionDefinition class attributes and methods
bpmn2_ExtensionDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionDefinition_id: Property = Property(name="id", type=StringType)
bpmn2_ExtensionDefinition.attributes={bpmn2_ExtensionDefinition_id, bpmn2_ExtensionDefinition_name}

# bpmn2_ExtensionAttributeValue class attributes and methods
bpmn2_ExtensionAttributeValue_id: Property = Property(name="id", type=StringType)
bpmn2_ExtensionAttributeValue.attributes={bpmn2_ExtensionAttributeValue_id}

# bpmn2_Documentation class attributes and methods
bpmn2_Documentation_text: Property = Property(name="text", type=StringType)
bpmn2_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_Documentation.attributes={bpmn2_Documentation_textFormat, bpmn2_Documentation_text}

# bpmn2_ExtensionAttributeDefinition class attributes and methods
bpmn2_ExtensionAttributeDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
bpmn2_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=BooleanType)
bpmn2_ExtensionAttributeDefinition_id: Property = Property(name="id", type=StringType)
bpmn2_ExtensionAttributeDefinition.attributes={bpmn2_ExtensionAttributeDefinition_id, bpmn2_ExtensionAttributeDefinition_name, bpmn2_ExtensionAttributeDefinition_isReference, bpmn2_ExtensionAttributeDefinition_type}

# bpmn2_ResourceRole class attributes and methods
bpmn2_ResourceRole_name: Property = Property(name="name", type=StringType)
bpmn2_ResourceRole.attributes={bpmn2_ResourceRole_name}

# bpmn2_CallableElement class attributes and methods
bpmn2_CallableElement_name: Property = Property(name="name", type=StringType)
bpmn2_CallableElement.attributes={bpmn2_CallableElement_name}

# bpmn2_InputOutputSpecification class attributes and methods

# bpmn2_InputOutputBinding class attributes and methods
bpmn2_InputOutputBinding_id: Property = Property(name="id", type=StringType)
bpmn2_InputOutputBinding.attributes={bpmn2_InputOutputBinding_id}

# bpmn2_ItemDefinition class attributes and methods
bpmn2_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
bpmn2_ItemDefinition_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_ItemDefinition.attributes={bpmn2_ItemDefinition_itemKind, bpmn2_ItemDefinition_isCollection}

# bpmn2_Import class attributes and methods
bpmn2_Import_importType: Property = Property(name="importType", type=StringType)
bpmn2_Import_location: Property = Property(name="location", type=StringType)
bpmn2_Import_namespace: Property = Property(name="namespace", type=StringType)
bpmn2_Import_id: Property = Property(name="id", type=StringType)
bpmn2_Import.attributes={bpmn2_Import_location, bpmn2_Import_importType, bpmn2_Import_id, bpmn2_Import_namespace}

# bpmn2_EndPoint class attributes and methods

# bpmn2_Auditing class attributes and methods

# bpmn2_GlobalTask class attributes and methods

# CallableElement class attributes and methods

# bpmn2_ItemAwareElement class attributes and methods

# bpmn2_DataState class attributes and methods
bpmn2_DataState_name: Property = Property(name="name", type=StringType)
bpmn2_DataState.attributes={bpmn2_DataState_name}

# bpmn2_InputSet class attributes and methods
bpmn2_InputSet_name: Property = Property(name="name", type=StringType)
bpmn2_InputSet.attributes={bpmn2_InputSet_name}

# bpmn2_OutputSet class attributes and methods
bpmn2_OutputSet_name: Property = Property(name="name", type=StringType)
bpmn2_OutputSet.attributes={bpmn2_OutputSet_name}

# bpmn2_DataInput class attributes and methods
bpmn2_DataInput_name: Property = Property(name="name", type=StringType)
bpmn2_DataInput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataInput.attributes={bpmn2_DataInput_name, bpmn2_DataInput_isCollection}

# bpmn2_DataOutput class attributes and methods
bpmn2_DataOutput_name: Property = Property(name="name", type=StringType)
bpmn2_DataOutput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataOutput.attributes={bpmn2_DataOutput_isCollection, bpmn2_DataOutput_name}

# ItemAwareElement class attributes and methods

# bpmn2_ResourceParameterBinding class attributes and methods
bpmn2_ResourceParameterBinding_id: Property = Property(name="id", type=StringType)
bpmn2_ResourceParameterBinding.attributes={bpmn2_ResourceParameterBinding_id}

# bpmn2_ResourceAssignmentExpression class attributes and methods
bpmn2_ResourceAssignmentExpression_id: Property = Property(name="id", type=StringType)
bpmn2_ResourceAssignmentExpression.attributes={bpmn2_ResourceAssignmentExpression_id}

# bpmn2_ResourceParameter class attributes and methods
bpmn2_ResourceParameter_name: Property = Property(name="name", type=StringType)
bpmn2_ResourceParameter_isRequired: Property = Property(name="isRequired", type=BooleanType)
bpmn2_ResourceParameter.attributes={bpmn2_ResourceParameter_name, bpmn2_ResourceParameter_isRequired}

# bpmn2_Resource class attributes and methods
bpmn2_Resource_name: Property = Property(name="name", type=StringType)
bpmn2_Resource.attributes={bpmn2_Resource_name}

# bpmn2_Artifact class attributes and methods

# bpmn2_CorrelationSubscription class attributes and methods

# bpmn2_Expression class attributes and methods

# bpmn2_Monitoring class attributes and methods

# bpmn2_Performer class attributes and methods

# ResourceRole class attributes and methods

# bpmn2_Process class attributes and methods
bpmn2_Process_processType: Property = Property(name="processType", type=StringType)
bpmn2_Process_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Process_isExecutable: Property = Property(name="isExecutable", type=BooleanType)
bpmn2_Process.attributes={bpmn2_Process_isClosed, bpmn2_Process_processType, bpmn2_Process_isExecutable}

# FlowElementsContainer class attributes and methods

# bpmn2_Property class attributes and methods
bpmn2_Property_name: Property = Property(name="name", type=StringType)
bpmn2_Property.attributes={bpmn2_Property_name}

# bpmn2_Collaboration class attributes and methods
bpmn2_Collaboration_name: Property = Property(name="name", type=StringType)
bpmn2_Collaboration_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Collaboration.attributes={bpmn2_Collaboration_name, bpmn2_Collaboration_isClosed}

# FlowElement class attributes and methods

# bpmn2_SequenceFlow class attributes and methods
bpmn2_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=BooleanType)
bpmn2_SequenceFlow.attributes={bpmn2_SequenceFlow_isImmediate}

# bpmn2_FlowElementsContainer class attributes and methods

# bpmn2_FlowElement class attributes and methods
bpmn2_FlowElement_name: Property = Property(name="name", type=StringType)
bpmn2_FlowElement.attributes={bpmn2_FlowElement_name}

# bpmn2_LaneSet class attributes and methods
bpmn2_LaneSet_name: Property = Property(name="name", type=StringType)
bpmn2_LaneSet.attributes={bpmn2_LaneSet_name}

# bpmn2_CategoryValue class attributes and methods
bpmn2_CategoryValue_value: Property = Property(name="value", type=StringType)
bpmn2_CategoryValue.attributes={bpmn2_CategoryValue_value}

# bpmn2_Lane class attributes and methods
bpmn2_Lane_name: Property = Property(name="name", type=StringType)
bpmn2_Lane.attributes={bpmn2_Lane_name}

# bpmn2_FlowNode class attributes and methods

# bpmn2_CorrelationKey class attributes and methods
bpmn2_CorrelationKey_name: Property = Property(name="name", type=StringType)
bpmn2_CorrelationKey.attributes={bpmn2_CorrelationKey_name}

# bpmn2_ConversationNode class attributes and methods
bpmn2_ConversationNode_name: Property = Property(name="name", type=StringType)
bpmn2_ConversationNode.attributes={bpmn2_ConversationNode_name}

# bpmn2_ConversationLink class attributes and methods
bpmn2_ConversationLink_name: Property = Property(name="name", type=StringType)
bpmn2_ConversationLink.attributes={bpmn2_ConversationLink_name}

# Collaboration class attributes and methods

# bpmn2_Choreography class attributes and methods

# bpmn2_ParticipantAssociation class attributes and methods

# bpmn2_MessageFlowAssociation class attributes and methods

# bpmn2_ConversationAssociation class attributes and methods

# bpmn2_Participant class attributes and methods
bpmn2_Participant_name: Property = Property(name="name", type=StringType)
bpmn2_Participant.attributes={bpmn2_Participant_name}

# bpmn2_MessageFlow class attributes and methods
bpmn2_MessageFlow_name: Property = Property(name="name", type=StringType)
bpmn2_MessageFlow.attributes={bpmn2_MessageFlow_name}

# bpmn2_ParticipantMultiplicity class attributes and methods
bpmn2_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=IntegerType)
bpmn2_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=IntegerType)
bpmn2_ParticipantMultiplicity_id: Property = Property(name="id", type=StringType)
bpmn2_ParticipantMultiplicity.attributes={bpmn2_ParticipantMultiplicity_id, bpmn2_ParticipantMultiplicity_minimum, bpmn2_ParticipantMultiplicity_maximum}

# bpmn2_InteractionNode class attributes and methods

# InteractionNode class attributes and methods

# bpmn2_CorrelationProperty class attributes and methods
bpmn2_CorrelationProperty_name: Property = Property(name="name", type=StringType)
bpmn2_CorrelationProperty.attributes={bpmn2_CorrelationProperty_name}

# bpmn2_CorrelationPropertyRetrievalExpression class attributes and methods

# bpmn2_FormalExpression class attributes and methods
bpmn2_FormalExpression_language: Property = Property(name="language", type=StringType)
bpmn2_FormalExpression.attributes={bpmn2_FormalExpression_language}

# bpmn2_CorrelationPropertyBinding class attributes and methods

# bpmn2_GlobalManualTask class attributes and methods

# GlobalTask class attributes and methods

# bpmn2_ManualTask class attributes and methods

# Task class attributes and methods

# bpmn2_Task class attributes and methods

# Activity class attributes and methods

# bpmn2_Activity class attributes and methods
bpmn2_Activity_isForCompensation: Property = Property(name="isForCompensation", type=BooleanType)
bpmn2_Activity_startQuantity: Property = Property(name="startQuantity", type=IntegerType)
bpmn2_Activity_completionQuantity: Property = Property(name="completionQuantity", type=IntegerType)
bpmn2_Activity.attributes={bpmn2_Activity_completionQuantity, bpmn2_Activity_isForCompensation, bpmn2_Activity_startQuantity}

# FlowNode class attributes and methods

# bpmn2_LoopCharacteristics class attributes and methods

# bpmn2_BoundaryEvent class attributes and methods
bpmn2_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=BooleanType)
bpmn2_BoundaryEvent.attributes={bpmn2_BoundaryEvent_cancelActivity}

# bpmn2_DataInputAssociation class attributes and methods

# bpmn2_DataOutputAssociation class attributes and methods

# Expression class attributes and methods

# bpmn2_CatchEvent class attributes and methods
bpmn2_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=BooleanType)
bpmn2_CatchEvent.attributes={bpmn2_CatchEvent_parallelMultiple}

# Event class attributes and methods

# bpmn2_EventDefinition class attributes and methods

# bpmn2_Event class attributes and methods

# DataAssociation class attributes and methods

# bpmn2_DataAssociation class attributes and methods

# bpmn2_Assignment class attributes and methods

# CatchEvent class attributes and methods

# bpmn2_Rendering class attributes and methods

# bpmn2_HumanPerformer class attributes and methods

# Performer class attributes and methods

# bpmn2_PotentialOwner class attributes and methods

# HumanPerformer class attributes and methods

# bpmn2_GlobalUserTask class attributes and methods
bpmn2_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalUserTask.attributes={bpmn2_GlobalUserTask_implementation}

# bpmn2_Gateway class attributes and methods
bpmn2_Gateway_gatewayDirection: Property = Property(name="gatewayDirection", type=StringType)
bpmn2_Gateway.attributes={bpmn2_Gateway_gatewayDirection}

# bpmn2_EventBasedGateway class attributes and methods
bpmn2_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
bpmn2_EventBasedGateway.attributes={bpmn2_EventBasedGateway_eventGatewayType, bpmn2_EventBasedGateway_instantiate}

# Gateway class attributes and methods

# bpmn2_ComplexGateway class attributes and methods

# bpmn2_ExclusiveGateway class attributes and methods

# bpmn2_InclusiveGateway class attributes and methods

# bpmn2_UserTask class attributes and methods
bpmn2_UserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_UserTask.attributes={bpmn2_UserTask_implementation}

# bpmn2_Extension class attributes and methods
bpmn2_Extension_mustUnderstand: Property = Property(name="mustUnderstand", type=BooleanType)
bpmn2_Extension_id: Property = Property(name="id", type=StringType)
bpmn2_Extension.attributes={bpmn2_Extension_mustUnderstand, bpmn2_Extension_id}

# bpmn2_IntermediateCatchEvent class attributes and methods

# bpmn2_IntermediateThrowEvent class attributes and methods

# ThrowEvent class attributes and methods

# bpmn2_ThrowEvent class attributes and methods

# bpmn2_EndEvent class attributes and methods

# bpmn2_StartEvent class attributes and methods
bpmn2_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=BooleanType)
bpmn2_StartEvent.attributes={bpmn2_StartEvent_isInterrupting}

# bpmn2_CancelEventDefinition class attributes and methods

# bpmn2_ParallelGateway class attributes and methods

# bpmn2_Relationship class attributes and methods
bpmn2_Relationship_direction: Property = Property(name="direction", type=StringType)
bpmn2_Relationship_type: Property = Property(name="type", type=StringType)
bpmn2_Relationship.attributes={bpmn2_Relationship_direction, bpmn2_Relationship_type}

# bpmn2_EscalationEventDefinition class attributes and methods

# bpmn2_Escalation class attributes and methods
bpmn2_Escalation_name: Property = Property(name="name", type=StringType)
bpmn2_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
bpmn2_Escalation_id: Property = Property(name="id", type=StringType)
bpmn2_Escalation.attributes={bpmn2_Escalation_id, bpmn2_Escalation_name, bpmn2_Escalation_escalationCode}

# bpmn2_CompensateEventDefinition class attributes and methods
bpmn2_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=BooleanType)
bpmn2_CompensateEventDefinition.attributes={bpmn2_CompensateEventDefinition_waitForCompletion}

# bpmn2_TimerEventDefinition class attributes and methods

# bpmn2_LinkEventDefinition class attributes and methods
bpmn2_LinkEventDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_LinkEventDefinition.attributes={bpmn2_LinkEventDefinition_name}

# EventDefinition class attributes and methods

# bpmn2_ErrorEventDefinition class attributes and methods

# bpmn2_TerminateEventDefinition class attributes and methods

# bpmn2_ConditionalEventDefinition class attributes and methods

# bpmn2_SignalEventDefinition class attributes and methods

# bpmn2_Signal class attributes and methods
bpmn2_Signal_name: Property = Property(name="name", type=StringType)
bpmn2_Signal.attributes={bpmn2_Signal_name}

# bpmn2_ImplicitThrowEvent class attributes and methods

# bpmn2_DataObject class attributes and methods
bpmn2_DataObject_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataObject.attributes={bpmn2_DataObject_isCollection}

# bpmn2_DataStore class attributes and methods
bpmn2_DataStore_name: Property = Property(name="name", type=StringType)
bpmn2_DataStore_capacity: Property = Property(name="capacity", type=IntegerType)
bpmn2_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=BooleanType)
bpmn2_DataStore.attributes={bpmn2_DataStore_isUnlimited, bpmn2_DataStore_name, bpmn2_DataStore_capacity}

# bpmn2_MessageEventDefinition class attributes and methods

# bpmn2_DataObjectReference class attributes and methods

# bpmn2_CallConversation class attributes and methods

# ConversationNode class attributes and methods

# bpmn2_Conversation class attributes and methods

# bpmn2_SubConversation class attributes and methods

# bpmn2_GlobalConversation class attributes and methods

# bpmn2_PartnerEntity class attributes and methods
bpmn2_PartnerEntity_name: Property = Property(name="name", type=StringType)
bpmn2_PartnerEntity.attributes={bpmn2_PartnerEntity_name}

# bpmn2_PartnerRole class attributes and methods
bpmn2_PartnerRole_name: Property = Property(name="name", type=StringType)
bpmn2_PartnerRole.attributes={bpmn2_PartnerRole_name}

# bpmn2_DataStoreReference class attributes and methods

# bpmn2_ChoreographyActivity class attributes and methods
bpmn2_ChoreographyActivity_loopType: Property = Property(name="loopType", type=StringType)
bpmn2_ChoreographyActivity.attributes={bpmn2_ChoreographyActivity_loopType}

# bpmn2_CallChoreography class attributes and methods

# ChoreographyActivity class attributes and methods

# bpmn2_SubChoreography class attributes and methods

# bpmn2_GlobalChoreographyTask class attributes and methods

# Choreography class attributes and methods

# bpmn2_TextAnnotation class attributes and methods
bpmn2_TextAnnotation_text: Property = Property(name="text", type=StringType)
bpmn2_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_TextAnnotation.attributes={bpmn2_TextAnnotation_text, bpmn2_TextAnnotation_textFormat}

# Artifact class attributes and methods

# bpmn2_Group class attributes and methods

# bpmn2_Association class attributes and methods
bpmn2_Association_associationDirection: Property = Property(name="associationDirection", type=StringType)
bpmn2_Association.attributes={bpmn2_Association_associationDirection}

# bpmn2_Category class attributes and methods
bpmn2_Category_name: Property = Property(name="name", type=StringType)
bpmn2_Category.attributes={bpmn2_Category_name}

# bpmn2_ChoreographyTask class attributes and methods

# bpmn2_SubProcess class attributes and methods
bpmn2_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=BooleanType)
bpmn2_SubProcess.attributes={bpmn2_SubProcess_triggeredByEvent}

# bpmn2_MultiInstanceLoopCharacteristics class attributes and methods
bpmn2_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=BooleanType)
bpmn2_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
bpmn2_MultiInstanceLoopCharacteristics.attributes={bpmn2_MultiInstanceLoopCharacteristics_behavior, bpmn2_MultiInstanceLoopCharacteristics_isSequential}

# LoopCharacteristics class attributes and methods

# bpmn2_ServiceTask class attributes and methods
bpmn2_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ServiceTask.attributes={bpmn2_ServiceTask_implementation}

# bpmn2_ComplexBehaviorDefinition class attributes and methods

# bpmn2_StandardLoopCharacteristics class attributes and methods
bpmn2_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=BooleanType)
bpmn2_StandardLoopCharacteristics.attributes={bpmn2_StandardLoopCharacteristics_testBefore}

# bpmn2_CallActivity class attributes and methods

# bpmn2_ReceiveTask class attributes and methods
bpmn2_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ReceiveTask_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_ReceiveTask.attributes={bpmn2_ReceiveTask_implementation, bpmn2_ReceiveTask_instantiate}

# bpmn2_ScriptTask class attributes and methods
bpmn2_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
bpmn2_ScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_ScriptTask.attributes={bpmn2_ScriptTask_scriptFormat, bpmn2_ScriptTask_script}

# bpmn2_BusinessRuleTask class attributes and methods
bpmn2_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_BusinessRuleTask.attributes={bpmn2_BusinessRuleTask_implementation}

# bpmn2_AdHocSubProcess class attributes and methods
bpmn2_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
bpmn2_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=BooleanType)
bpmn2_AdHocSubProcess.attributes={bpmn2_AdHocSubProcess_ordering, bpmn2_AdHocSubProcess_cancelRemainingInstances}

# SubProcess class attributes and methods

# bpmn2_SendTask class attributes and methods
bpmn2_SendTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_SendTask.attributes={bpmn2_SendTask_implementation}

# bpmn2_Transaction class attributes and methods
bpmn2_Transaction_protocol: Property = Property(name="protocol", type=StringType)
bpmn2_Transaction_method: Property = Property(name="method", type=StringType)
bpmn2_Transaction.attributes={bpmn2_Transaction_protocol, bpmn2_Transaction_method}

# bpmn2_GlobalScriptTask class attributes and methods
bpmn2_GlobalScriptTask_scriptLanguage: Property = Property(name="scriptLanguage", type=StringType)
bpmn2_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_GlobalScriptTask.attributes={bpmn2_GlobalScriptTask_scriptLanguage, bpmn2_GlobalScriptTask_script}

# bpmn2_GlobalBusinessRuleTask class attributes and methods
bpmn2_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalBusinessRuleTask.attributes={bpmn2_GlobalBusinessRuleTask_implementation}

# bpmn2_Definitions class attributes and methods
bpmn2_Definitions_name: Property = Property(name="name", type=StringType)
bpmn2_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
bpmn2_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
bpmn2_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
bpmn2_Definitions_exporter: Property = Property(name="exporter", type=StringType)
bpmn2_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
bpmn2_Definitions.attributes={bpmn2_Definitions_expressionLanguage, bpmn2_Definitions_typeLanguage, bpmn2_Definitions_targetNamespace, bpmn2_Definitions_exporterVersion, bpmn2_Definitions_name, bpmn2_Definitions_exporter}

# bpmn2_BPMNDiagram class attributes and methods

# Relationships
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="bpmn2_Operation", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface", type=bpmn2_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implementationRef1: BinaryAssociation = BinaryAssociation(
    name="implementationRef1",
    ends={
        Property(name="bpmn2_EObject", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface2", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef18: BinaryAssociation = BinaryAssociation(
    name="inMessageRef18",
    ends={
        Property(name="bpmn2_Message", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation19", type=bpmn2_Message, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef20: BinaryAssociation = BinaryAssociation(
    name="outMessageRef20",
    ends={
        Property(name="bpmn2_Message22", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation21", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
errorRefs23: BinaryAssociation = BinaryAssociation(
    name="errorRefs23",
    ends={
        Property(name="bpmn2_Error", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation24", type=bpmn2_Error, multiplicity=Multiplicity(0, 9999))
    }
)
implementationRef25: BinaryAssociation = BinaryAssociation(
    name="implementationRef25",
    ends={
        Property(name="bpmn2_EObject27", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation26", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
extensionDefinitions3: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions3",
    ends={
        Property(name="bpmn2_ExtensionDefinition", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
extensionValues4: BinaryAssociation = BinaryAssociation(
    name="extensionValues4",
    ends={
        Property(name="bpmn2_ExtensionAttributeValue", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement5", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation6: BinaryAssociation = BinaryAssociation(
    name="documentation6",
    ends={
        Property(name="bpmn2_Documentation", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement7", type=bpmn2_Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionAttributeDefinitions8: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions8",
    ends={
        Property(name="ExtensionAttributeDefinition", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefinition9: BinaryAssociation = BinaryAssociation(
    name="extensionDefinition9",
    ends={
        Property(name="ExtensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionAttributeDefinitions", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
valueRef10: BinaryAssociation = BinaryAssociation(
    name="valueRef10",
    ends={
        Property(name="bpmn2_EObject12", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue11", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="bpmn2_EObject15", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue14", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionAttributeDefinition16: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition16",
    ends={
        Property(name="bpmn2_ExtensionAttributeDefinition", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue17", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
resources38: BinaryAssociation = BinaryAssociation(
    name="resources38",
    ends={
        Property(name="bpmn2_ResourceRole", type=bpmn2_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalTask", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification39: BinaryAssociation = BinaryAssociation(
    name="ioSpecification39",
    ends={
        Property(name="bpmn2_InputOutputSpecification", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supportedInterfaceRefs40: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs40",
    ends={
        Property(name="bpmn2_Interface42", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement41", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ioBinding43: BinaryAssociation = BinaryAssociation(
    name="ioBinding43",
    ends={
        Property(name="bpmn2_InputOutputBinding", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement44", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemRef28: BinaryAssociation = BinaryAssociation(
    name="itemRef28",
    ends={
        Property(name="bpmn2_ItemDefinition", type=bpmn2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Message29", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
structureRef30: BinaryAssociation = BinaryAssociation(
    name="structureRef30",
    ends={
        Property(name="bpmn2_EObject32", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition31", type=bpmn2_EObject, multiplicity=Multiplicity(1, 1))
    }
)
import33: BinaryAssociation = BinaryAssociation(
    name="import33",
    ends={
        Property(name="bpmn2_Import", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition34", type=bpmn2_Import, multiplicity=Multiplicity(0, 1))
    }
)
structureRef35: BinaryAssociation = BinaryAssociation(
    name="structureRef35",
    ends={
        Property(name="bpmn2_ItemDefinition37", type=bpmn2_Error, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Error36", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
itemSubjectRef65: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef65",
    ends={
        Property(name="bpmn2_ItemDefinition66", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataState67: BinaryAssociation = BinaryAssociation(
    name="dataState67",
    ends={
        Property(name="bpmn2_DataState", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement68", type=bpmn2_DataState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataOutputRefs69: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs69",
    ends={
        Property(name="DataOutput", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSets45: BinaryAssociation = BinaryAssociation(
    name="inputSets45",
    ends={
        Property(name="bpmn2_InputSet", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification46", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSets47: BinaryAssociation = BinaryAssociation(
    name="outputSets47",
    ends={
        Property(name="bpmn2_OutputSet", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification48", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputs49: BinaryAssociation = BinaryAssociation(
    name="dataInputs49",
    ends={
        Property(name="bpmn2_DataInput", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification50", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs51: BinaryAssociation = BinaryAssociation(
    name="dataOutputs51",
    ends={
        Property(name="bpmn2_DataOutput", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification52", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputRefs53: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs53",
    ends={
        Property(name="DataInput", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInputRefs54: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs54",
    ends={
        Property(name="DataInput55", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingInputRefs56: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs56",
    ends={
        Property(name="DataInput57", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs58: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs58",
    ends={
        Property(name="OutputSet", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs59", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetWithOptional60: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional60",
    ends={
        Property(name="InputSet", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetWithWhileExecuting61: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting61",
    ends={
        Property(name="InputSet62", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs63: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs63",
    ends={
        Property(name="InputSet64", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
resourceParameterBindings94: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings94",
    ends={
        Property(name="bpmn2_ResourceParameterBinding", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole95", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression96: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression96",
    ends={
        Property(name="bpmn2_ResourceAssignmentExpression", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole97", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceParameters98: BinaryAssociation = BinaryAssociation(
    name="resourceParameters98",
    ends={
        Property(name="bpmn2_ResourceParameter", type=bpmn2_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Resource99", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalOutputRefs70: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs70",
    ends={
        Property(name="DataOutput71", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithOptional", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingOutputRefs72: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs72",
    ends={
        Property(name="DataOutput73", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithWhileExecuting", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs74: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs74",
    ends={
        Property(name="InputSet76", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs75", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithOptional77: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional77",
    ends={
        Property(name="OutputSet78", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithWhileExecuting79: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting79",
    ends={
        Property(name="OutputSet80", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs81: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs81",
    ends={
        Property(name="OutputSet82", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputDataRef83: BinaryAssociation = BinaryAssociation(
    name="inputDataRef83",
    ends={
        Property(name="bpmn2_InputSet85", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding84", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef86: BinaryAssociation = BinaryAssociation(
    name="outputDataRef86",
    ends={
        Property(name="bpmn2_OutputSet88", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding87", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef89: BinaryAssociation = BinaryAssociation(
    name="operationRef89",
    ends={
        Property(name="bpmn2_Operation91", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding90", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1))
    }
)
resourceRef92: BinaryAssociation = BinaryAssociation(
    name="resourceRef92",
    ends={
        Property(name="bpmn2_Resource", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole93", type=bpmn2_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resources121: BinaryAssociation = BinaryAssociation(
    name="resources121",
    ends={
        Property(name="bpmn2_ResourceRole123", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process122", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts124: BinaryAssociation = BinaryAssociation(
    name="artifacts124",
    ends={
        Property(name="bpmn2_Artifact", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process125", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscriptions126: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions126",
    ends={
        Property(name="bpmn2_CorrelationSubscription", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process127", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decomposedBy129: BinaryAssociation = BinaryAssociation(
    name="decomposedBy129",
    ends={
        Property(name="Process", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposes", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decomposes131: BinaryAssociation = BinaryAssociation(
    name="decomposes131",
    ends={
        Property(name="Process132", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposedBy", type=bpmn2_Process, multiplicity=Multiplicity(0, 1))
    }
)
type100: BinaryAssociation = BinaryAssociation(
    name="type100",
    ends={
        Property(name="bpmn2_ItemDefinition102", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameter101", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="bpmn2_Expression", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding104", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterRef105: BinaryAssociation = BinaryAssociation(
    name="parameterRef105",
    ends={
        Property(name="bpmn2_ResourceParameter107", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding106", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
expression108: BinaryAssociation = BinaryAssociation(
    name="expression108",
    ends={
        Property(name="bpmn2_Expression110", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceAssignmentExpression109", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
auditing111: BinaryAssociation = BinaryAssociation(
    name="auditing111",
    ends={
        Property(name="bpmn2_Auditing", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring112: BinaryAssociation = BinaryAssociation(
    name="monitoring112",
    ends={
        Property(name="bpmn2_Monitoring", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process113", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties114: BinaryAssociation = BinaryAssociation(
    name="properties114",
    ends={
        Property(name="bpmn2_Property", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process115", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports117: BinaryAssociation = BinaryAssociation(
    name="supports117",
    ends={
        Property(name="bpmn2_Process118", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process116", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999))
    }
)
definitionalCollaborationRef119: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef119",
    ends={
        Property(name="bpmn2_Collaboration", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process120", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
flowNodeRefs152: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs152",
    ends={
        Property(name="FlowNode", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 9999))
    }
)
partitionElement153: BinaryAssociation = BinaryAssociation(
    name="partitionElement153",
    ends={
        Property(name="bpmn2_BaseElement155", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane154", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing156: BinaryAssociation = BinaryAssociation(
    name="outgoing156",
    ends={
        Property(name="SequenceFlow", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
incoming157: BinaryAssociation = BinaryAssociation(
    name="incoming157",
    ends={
        Property(name="SequenceFlow158", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
lanes159: BinaryAssociation = BinaryAssociation(
    name="lanes159",
    ends={
        Property(name="Lane", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="flowNodeRefs", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
flowElements133: BinaryAssociation = BinaryAssociation(
    name="flowElements133",
    ends={
        Property(name="bpmn2_FlowElement", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laneSets134: BinaryAssociation = BinaryAssociation(
    name="laneSets134",
    ends={
        Property(name="bpmn2_LaneSet", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer135", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing136: BinaryAssociation = BinaryAssociation(
    name="auditing136",
    ends={
        Property(name="bpmn2_Auditing138", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement137", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring139: BinaryAssociation = BinaryAssociation(
    name="monitoring139",
    ends={
        Property(name="bpmn2_Monitoring141", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement140", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
categoryValueRef142: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef142",
    ends={
        Property(name="CategoryValue", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="categorizedFlowElements", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999))
    }
)
categorizedFlowElements143: BinaryAssociation = BinaryAssociation(
    name="categorizedFlowElements143",
    ends={
        Property(name="FlowElement", type=bpmn2_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryValueRef", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999))
    }
)
lanes144: BinaryAssociation = BinaryAssociation(
    name="lanes144",
    ends={
        Property(name="bpmn2_Lane", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet145", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childLaneSet146: BinaryAssociation = BinaryAssociation(
    name="childLaneSet146",
    ends={
        Property(name="bpmn2_LaneSet148", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane147", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partitionElementRef149: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef149",
    ends={
        Property(name="bpmn2_BaseElement151", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane150", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
correlationKeys181: BinaryAssociation = BinaryAssociation(
    name="correlationKeys181",
    ends={
        Property(name="bpmn2_CorrelationKey", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration182", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversations183: BinaryAssociation = BinaryAssociation(
    name="conversations183",
    ends={
        Property(name="bpmn2_ConversationNode", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration184", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationLinks185: BinaryAssociation = BinaryAssociation(
    name="conversationLinks185",
    ends={
        Property(name="bpmn2_ConversationLink", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration186", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression160: BinaryAssociation = BinaryAssociation(
    name="conditionExpression160",
    ends={
        Property(name="bpmn2_Expression161", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SequenceFlow", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetRef162: BinaryAssociation = BinaryAssociation(
    name="targetRef162",
    ends={
        Property(name="FlowNode163", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef164: BinaryAssociation = BinaryAssociation(
    name="sourceRef164",
    ends={
        Property(name="FlowNode165", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
choreographyRef166: BinaryAssociation = BinaryAssociation(
    name="choreographyRef166",
    ends={
        Property(name="bpmn2_Choreography", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration167", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 9999))
    }
)
artifacts168: BinaryAssociation = BinaryAssociation(
    name="artifacts168",
    ends={
        Property(name="bpmn2_Artifact170", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration169", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantAssociations171: BinaryAssociation = BinaryAssociation(
    name="participantAssociations171",
    ends={
        Property(name="bpmn2_ParticipantAssociation", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration172", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociations173: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations173",
    ends={
        Property(name="bpmn2_MessageFlowAssociation", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration174", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociations175: BinaryAssociation = BinaryAssociation(
    name="conversationAssociations175",
    ends={
        Property(name="bpmn2_ConversationAssociation", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration176", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
participants177: BinaryAssociation = BinaryAssociation(
    name="participants177",
    ends={
        Property(name="bpmn2_Participant", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration178", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlows179: BinaryAssociation = BinaryAssociation(
    name="messageFlows179",
    ends={
        Property(name="bpmn2_MessageFlow", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration180", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantMultiplicity196: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity196",
    ends={
        Property(name="bpmn2_ParticipantMultiplicity", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant197", type=bpmn2_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endPointRefs198: BinaryAssociation = BinaryAssociation(
    name="endPointRefs198",
    ends={
        Property(name="bpmn2_EndPoint", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant199", type=bpmn2_EndPoint, multiplicity=Multiplicity(0, 9999))
    }
)
processRef200: BinaryAssociation = BinaryAssociation(
    name="processRef200",
    ends={
        Property(name="bpmn2_Process202", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant201", type=bpmn2_Process, multiplicity=Multiplicity(0, 1))
    }
)
incomingConversationLinks203: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks203",
    ends={
        Property(name="ConversationLink", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef204", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingConversationLinks205: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks205",
    ends={
        Property(name="ConversationLink207", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef206", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
sourceRef208: BinaryAssociation = BinaryAssociation(
    name="sourceRef208",
    ends={
        Property(name="InteractionNode", type=bpmn2_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConversationLinks", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
innerParticipantRef187: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef187",
    ends={
        Property(name="bpmn2_Participant189", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation188", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
targetRef209: BinaryAssociation = BinaryAssociation(
    name="targetRef209",
    ends={
        Property(name="InteractionNode210", type=bpmn2_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConversationLinks", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef190: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef190",
    ends={
        Property(name="bpmn2_Participant192", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation191", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRefs193: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs193",
    ends={
        Property(name="bpmn2_Interface195", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant194", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
targetRef219: BinaryAssociation = BinaryAssociation(
    name="targetRef219",
    ends={
        Property(name="bpmn2_InteractionNode221", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow220", type=bpmn2_InteractionNode, multiplicity=Multiplicity(0, 1))
    }
)
messageRef222: BinaryAssociation = BinaryAssociation(
    name="messageRef222",
    ends={
        Property(name="bpmn2_Message224", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow223", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
innerConversationNodeRef225: BinaryAssociation = BinaryAssociation(
    name="innerConversationNodeRef225",
    ends={
        Property(name="bpmn2_ConversationNode227", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationAssociation226", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
outerConversationNodeRef228: BinaryAssociation = BinaryAssociation(
    name="outerConversationNodeRef228",
    ends={
        Property(name="bpmn2_ConversationNode230", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationAssociation229", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
participantRefs231: BinaryAssociation = BinaryAssociation(
    name="participantRefs231",
    ends={
        Property(name="bpmn2_Participant233", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode232", type=bpmn2_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
messageFlowRefs234: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs234",
    ends={
        Property(name="bpmn2_MessageFlow236", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode235", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999))
    }
)
correlationKeys237: BinaryAssociation = BinaryAssociation(
    name="correlationKeys237",
    ends={
        Property(name="bpmn2_CorrelationKey239", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode238", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRef240: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef240",
    ends={
        Property(name="bpmn2_CorrelationProperty", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationKey241", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(0, 9999))
    }
)
correlationPropertyRetrievalExpression242: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression242",
    ends={
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationProperty243", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type244: BinaryAssociation = BinaryAssociation(
    name="type244",
    ends={
        Property(name="bpmn2_ItemDefinition246", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationProperty245", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
messagePath247: BinaryAssociation = BinaryAssociation(
    name="messagePath247",
    ends={
        Property(name="bpmn2_FormalExpression", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression248", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageRef249: BinaryAssociation = BinaryAssociation(
    name="messageRef249",
    ends={
        Property(name="bpmn2_Message251", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression250", type=bpmn2_Message, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef211: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef211",
    ends={
        Property(name="bpmn2_MessageFlow213", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation212", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef214: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef214",
    ends={
        Property(name="bpmn2_MessageFlow216", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation215", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef217: BinaryAssociation = BinaryAssociation(
    name="sourceRef217",
    ends={
        Property(name="bpmn2_InteractionNode", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow218", type=bpmn2_InteractionNode, multiplicity=Multiplicity(0, 1))
    }
)
evaluatesToTypeRef255: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef255",
    ends={
        Property(name="bpmn2_ItemDefinition257", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FormalExpression256", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
correlationKeyRef258: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef258",
    ends={
        Property(name="bpmn2_CorrelationKey260", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationSubscription259", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding261: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding261",
    ends={
        Property(name="bpmn2_CorrelationPropertyBinding", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationSubscription262", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataPath263: BinaryAssociation = BinaryAssociation(
    name="dataPath263",
    ends={
        Property(name="bpmn2_FormalExpression265", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyBinding264", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
correlationPropertyRef266: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef266",
    ends={
        Property(name="bpmn2_CorrelationProperty268", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyBinding267", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
loopCharacteristics269: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics269",
    ends={
        Property(name="bpmn2_LoopCharacteristics", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity", type=bpmn2_LoopCharacteristics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources270: BinaryAssociation = BinaryAssociation(
    name="resources270",
    ends={
        Property(name="bpmn2_ResourceRole272", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity271", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default273: BinaryAssociation = BinaryAssociation(
    name="default273",
    ends={
        Property(name="bpmn2_SequenceFlow275", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity274", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
properties276: BinaryAssociation = BinaryAssociation(
    name="properties276",
    ends={
        Property(name="bpmn2_Property278", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity277", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification279: BinaryAssociation = BinaryAssociation(
    name="ioSpecification279",
    ends={
        Property(name="bpmn2_InputOutputSpecification281", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity280", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundaryEventRefs282: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs282",
    ends={
        Property(name="BoundaryEvent", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="attachedToRef", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputAssociations283: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations283",
    ends={
        Property(name="bpmn2_DataInputAssociation", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity284", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociations285: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations285",
    ends={
        Property(name="bpmn2_DataOutputAssociation", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity286", type=bpmn2_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body252: BinaryAssociation = BinaryAssociation(
    name="body252",
    ends={
        Property(name="bpmn2_EObject254", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FormalExpression253", type=bpmn2_EObject, multiplicity=Multiplicity(1, 1))
    }
)
attachedToRef287: BinaryAssociation = BinaryAssociation(
    name="attachedToRef287",
    ends={
        Property(name="Activity", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="boundaryEventRefs", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1))
    }
)
outputSet288: BinaryAssociation = BinaryAssociation(
    name="outputSet288",
    ends={
        Property(name="bpmn2_OutputSet289", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitionRefs290: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs290",
    ends={
        Property(name="bpmn2_EventDefinition", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent291", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
dataOutputAssociation292: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation292",
    ends={
        Property(name="bpmn2_DataOutputAssociation294", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent293", type=bpmn2_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs295: BinaryAssociation = BinaryAssociation(
    name="dataOutputs295",
    ends={
        Property(name="bpmn2_DataOutput297", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent296", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitions298: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions298",
    ends={
        Property(name="bpmn2_EventDefinition300", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent299", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties301: BinaryAssociation = BinaryAssociation(
    name="properties301",
    ends={
        Property(name="bpmn2_Property302", type=bpmn2_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Event", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation303: BinaryAssociation = BinaryAssociation(
    name="transformation303",
    ends={
        Property(name="bpmn2_FormalExpression304", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation", type=bpmn2_FormalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment305: BinaryAssociation = BinaryAssociation(
    name="assignment305",
    ends={
        Property(name="bpmn2_Assignment", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation306", type=bpmn2_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetRef307: BinaryAssociation = BinaryAssociation(
    name="targetRef307",
    ends={
        Property(name="bpmn2_ItemAwareElement309", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation308", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef310: BinaryAssociation = BinaryAssociation(
    name="sourceRef310",
    ends={
        Property(name="bpmn2_ItemAwareElement312", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation311", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 9999))
    }
)
from313: BinaryAssociation = BinaryAssociation(
    name="from313",
    ends={
        Property(name="bpmn2_Expression315", type=bpmn2_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Assignment314", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
renderings319: BinaryAssociation = BinaryAssociation(
    name="renderings319",
    ends={
        Property(name="bpmn2_Rendering", type=bpmn2_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_UserTask", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renderings320: BinaryAssociation = BinaryAssociation(
    name="renderings320",
    ends={
        Property(name="bpmn2_Rendering321", type=bpmn2_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalUserTask", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activationCondition322: BinaryAssociation = BinaryAssociation(
    name="activationCondition322",
    ends={
        Property(name="bpmn2_Expression323", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexGateway", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default324: BinaryAssociation = BinaryAssociation(
    name="default324",
    ends={
        Property(name="bpmn2_SequenceFlow326", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexGateway325", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
default327: BinaryAssociation = BinaryAssociation(
    name="default327",
    ends={
        Property(name="bpmn2_SequenceFlow328", type=bpmn2_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExclusiveGateway", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
default329: BinaryAssociation = BinaryAssociation(
    name="default329",
    ends={
        Property(name="bpmn2_SequenceFlow330", type=bpmn2_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InclusiveGateway", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
to316: BinaryAssociation = BinaryAssociation(
    name="to316",
    ends={
        Property(name="bpmn2_Expression318", type=bpmn2_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Assignment317", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sources331: BinaryAssociation = BinaryAssociation(
    name="sources331",
    ends={
        Property(name="bpmn2_EObject332", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
targets333: BinaryAssociation = BinaryAssociation(
    name="targets333",
    ends={
        Property(name="bpmn2_EObject335", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship334", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
definition336: BinaryAssociation = BinaryAssociation(
    name="definition336",
    ends={
        Property(name="bpmn2_ExtensionDefinition337", type=bpmn2_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Extension", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputSet338: BinaryAssociation = BinaryAssociation(
    name="inputSet338",
    ends={
        Property(name="bpmn2_InputSet339", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitionRefs340: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs340",
    ends={
        Property(name="bpmn2_EventDefinition342", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent341", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputAssociation343: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation343",
    ends={
        Property(name="bpmn2_DataInputAssociation345", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent344", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputs346: BinaryAssociation = BinaryAssociation(
    name="dataInputs346",
    ends={
        Property(name="bpmn2_DataInput348", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent347", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitions349: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions349",
    ends={
        Property(name="bpmn2_EventDefinition351", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent350", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalationRef354: BinaryAssociation = BinaryAssociation(
    name="escalationRef354",
    ends={
        Property(name="bpmn2_Escalation", type=bpmn2_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_EscalationEventDefinition", type=bpmn2_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
structureRef355: BinaryAssociation = BinaryAssociation(
    name="structureRef355",
    ends={
        Property(name="bpmn2_ItemDefinition357", type=bpmn2_Escalation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Escalation356", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
activityRef358: BinaryAssociation = BinaryAssociation(
    name="activityRef358",
    ends={
        Property(name="bpmn2_Activity359", type=bpmn2_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CompensateEventDefinition", type=bpmn2_Activity, multiplicity=Multiplicity(0, 1))
    }
)
timeDate360: BinaryAssociation = BinaryAssociation(
    name="timeDate360",
    ends={
        Property(name="bpmn2_Expression361", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCycle362: BinaryAssociation = BinaryAssociation(
    name="timeCycle362",
    ends={
        Property(name="bpmn2_Expression364", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition363", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeDuration365: BinaryAssociation = BinaryAssociation(
    name="timeDuration365",
    ends={
        Property(name="bpmn2_Expression367", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition366", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
errorRef352: BinaryAssociation = BinaryAssociation(
    name="errorRef352",
    ends={
        Property(name="bpmn2_Error353", type=bpmn2_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ErrorEventDefinition", type=bpmn2_Error, multiplicity=Multiplicity(0, 1))
    }
)
operationRef375: BinaryAssociation = BinaryAssociation(
    name="operationRef375",
    ends={
        Property(name="bpmn2_Operation377", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition376", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
condition378: BinaryAssociation = BinaryAssociation(
    name="condition378",
    ends={
        Property(name="bpmn2_Expression379", type=bpmn2_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConditionalEventDefinition", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signalRef380: BinaryAssociation = BinaryAssociation(
    name="signalRef380",
    ends={
        Property(name="bpmn2_Signal", type=bpmn2_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SignalEventDefinition", type=bpmn2_Signal, multiplicity=Multiplicity(0, 1))
    }
)
structureRef381: BinaryAssociation = BinaryAssociation(
    name="structureRef381",
    ends={
        Property(name="bpmn2_ItemDefinition383", type=bpmn2_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Signal382", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
target369: BinaryAssociation = BinaryAssociation(
    name="target369",
    ends={
        Property(name="LinkEventDefinition", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
source371: BinaryAssociation = BinaryAssociation(
    name="source371",
    ends={
        Property(name="LinkEventDefinition372", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
messageRef373: BinaryAssociation = BinaryAssociation(
    name="messageRef373",
    ends={
        Property(name="bpmn2_Message374", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
dataStoreRef384: BinaryAssociation = BinaryAssociation(
    name="dataStoreRef384",
    ends={
        Property(name="bpmn2_DataStore", type=bpmn2_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataStoreReference", type=bpmn2_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
dataObjectRef385: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef385",
    ends={
        Property(name="bpmn2_DataObject", type=bpmn2_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataObjectReference", type=bpmn2_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
calledCollaborationRef386: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef386",
    ends={
        Property(name="bpmn2_Collaboration387", type=bpmn2_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallConversation", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations388: BinaryAssociation = BinaryAssociation(
    name="participantAssociations388",
    ends={
        Property(name="bpmn2_ParticipantAssociation390", type=bpmn2_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallConversation389", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNodes391: BinaryAssociation = BinaryAssociation(
    name="conversationNodes391",
    ends={
        Property(name="bpmn2_ConversationNode392", type=bpmn2_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubConversation", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantRef393: BinaryAssociation = BinaryAssociation(
    name="participantRef393",
    ends={
        Property(name="bpmn2_Participant394", type=bpmn2_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerEntity", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
participantRefs397: BinaryAssociation = BinaryAssociation(
    name="participantRefs397",
    ends={
        Property(name="bpmn2_Participant398", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingParticipantRef399: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef399",
    ends={
        Property(name="bpmn2_Participant401", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity400", type=bpmn2_Participant, multiplicity=Multiplicity(0, 1))
    }
)
correlationKeys402: BinaryAssociation = BinaryAssociation(
    name="correlationKeys402",
    ends={
        Property(name="bpmn2_CorrelationKey404", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity403", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledChoreographyRef405: BinaryAssociation = BinaryAssociation(
    name="calledChoreographyRef405",
    ends={
        Property(name="bpmn2_Choreography406", type=bpmn2_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallChoreography", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations407: BinaryAssociation = BinaryAssociation(
    name="participantAssociations407",
    ends={
        Property(name="bpmn2_ParticipantAssociation409", type=bpmn2_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallChoreography408", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts410: BinaryAssociation = BinaryAssociation(
    name="artifacts410",
    ends={
        Property(name="bpmn2_Artifact411", type=bpmn2_SubChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubChoreography", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantRef395: BinaryAssociation = BinaryAssociation(
    name="participantRef395",
    ends={
        Property(name="bpmn2_Participant396", type=bpmn2_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerRole", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingParticipantRef414: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef414",
    ends={
        Property(name="bpmn2_Participant415", type=bpmn2_GlobalChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalChoreographyTask", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
categoryValueRef416: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef416",
    ends={
        Property(name="bpmn2_CategoryValue", type=bpmn2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Group", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef417: BinaryAssociation = BinaryAssociation(
    name="sourceRef417",
    ends={
        Property(name="bpmn2_BaseElement418", type=bpmn2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Association", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
targetRef419: BinaryAssociation = BinaryAssociation(
    name="targetRef419",
    ends={
        Property(name="bpmn2_BaseElement421", type=bpmn2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Association420", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
categoryValue422: BinaryAssociation = BinaryAssociation(
    name="categoryValue422",
    ends={
        Property(name="bpmn2_CategoryValue423", type=bpmn2_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Category", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowRef412: BinaryAssociation = BinaryAssociation(
    name="messageFlowRef412",
    ends={
        Property(name="bpmn2_MessageFlow413", type=bpmn2_ChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyTask", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 2))
    }
)
operationRef424: BinaryAssociation = BinaryAssociation(
    name="operationRef424",
    ends={
        Property(name="bpmn2_Operation425", type=bpmn2_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ServiceTask", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
artifacts426: BinaryAssociation = BinaryAssociation(
    name="artifacts426",
    ends={
        Property(name="bpmn2_Artifact427", type=bpmn2_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubProcess", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCardinality428: BinaryAssociation = BinaryAssociation(
    name="loopCardinality428",
    ends={
        Property(name="bpmn2_Expression429", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopDataInputRef430: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef430",
    ends={
        Property(name="bpmn2_ItemAwareElement432", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics431", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef433: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef433",
    ends={
        Property(name="bpmn2_ItemAwareElement435", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics434", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
inputDataItem436: BinaryAssociation = BinaryAssociation(
    name="inputDataItem436",
    ends={
        Property(name="bpmn2_DataInput438", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics437", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completionCondition442: BinaryAssociation = BinaryAssociation(
    name="completionCondition442",
    ends={
        Property(name="bpmn2_Expression444", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics443", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complexBehaviorDefinition445: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition445",
    ends={
        Property(name="bpmn2_ComplexBehaviorDefinition", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics446", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oneBehaviorEventRef447: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef447",
    ends={
        Property(name="bpmn2_EventDefinition449", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics448", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
noneBehaviorEventRef450: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef450",
    ends={
        Property(name="bpmn2_EventDefinition452", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics451", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
condition453: BinaryAssociation = BinaryAssociation(
    name="condition453",
    ends={
        Property(name="bpmn2_FormalExpression455", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexBehaviorDefinition454", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event456: BinaryAssociation = BinaryAssociation(
    name="event456",
    ends={
        Property(name="bpmn2_ImplicitThrowEvent", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexBehaviorDefinition457", type=bpmn2_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopCondition458: BinaryAssociation = BinaryAssociation(
    name="loopCondition458",
    ends={
        Property(name="bpmn2_Expression459", type=bpmn2_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_StandardLoopCharacteristics", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopMaximum460: BinaryAssociation = BinaryAssociation(
    name="loopMaximum460",
    ends={
        Property(name="bpmn2_Expression462", type=bpmn2_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_StandardLoopCharacteristics461", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputDataItem439: BinaryAssociation = BinaryAssociation(
    name="outputDataItem439",
    ends={
        Property(name="bpmn2_DataOutput441", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics440", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationRef465: BinaryAssociation = BinaryAssociation(
    name="operationRef465",
    ends={
        Property(name="bpmn2_Operation466", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef467: BinaryAssociation = BinaryAssociation(
    name="messageRef467",
    ends={
        Property(name="bpmn2_Message469", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask468", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef470: BinaryAssociation = BinaryAssociation(
    name="operationRef470",
    ends={
        Property(name="bpmn2_Operation471", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef472: BinaryAssociation = BinaryAssociation(
    name="messageRef472",
    ends={
        Property(name="bpmn2_Message474", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask473", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition475: BinaryAssociation = BinaryAssociation(
    name="completionCondition475",
    ends={
        Property(name="bpmn2_Expression476", type=bpmn2_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_AdHocSubProcess", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
calledElementRef463: BinaryAssociation = BinaryAssociation(
    name="calledElementRef463",
    ends={
        Property(name="bpmn2_CallableElement464", type=bpmn2_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallActivity", type=bpmn2_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
imports477: BinaryAssociation = BinaryAssociation(
    name="imports477",
    ends={
        Property(name="bpmn2_Import478", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions", type=bpmn2_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions479: BinaryAssociation = BinaryAssociation(
    name="extensions479",
    ends={
        Property(name="bpmn2_Extension481", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions480", type=bpmn2_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams487: BinaryAssociation = BinaryAssociation(
    name="diagrams487",
    ends={
        Property(name="bpmn2_BPMNDiagram", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions488", type=bpmn2_BPMNDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships482: BinaryAssociation = BinaryAssociation(
    name="relationships482",
    ends={
        Property(name="bpmn2_Relationship484", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions483", type=bpmn2_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElements485: BinaryAssociation = BinaryAssociation(
    name="rootElements485",
    ends={
        Property(name="bpmn2_RootElement", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions486", type=bpmn2_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bpmn2_Interface_RootElement = Generalization(general=RootElement, specific=bpmn2_Interface)
gen_bpmn2_Operation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Operation)
gen_bpmn2_RootElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_RootElement)
gen_bpmn2_Documentation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Documentation)
gen_bpmn2_CallableElement_RootElement = Generalization(general=RootElement, specific=bpmn2_CallableElement)
gen_bpmn2_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputOutputSpecification)
gen_bpmn2_Message_RootElement = Generalization(general=RootElement, specific=bpmn2_Message)
gen_bpmn2_ItemDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_ItemDefinition)
gen_bpmn2_Error_RootElement = Generalization(general=RootElement, specific=bpmn2_Error)
gen_bpmn2_EndPoint_RootElement = Generalization(general=RootElement, specific=bpmn2_EndPoint)
gen_bpmn2_Auditing_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Auditing)
gen_bpmn2_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=bpmn2_GlobalTask)
gen_bpmn2_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ItemAwareElement)
gen_bpmn2_DataState_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataState)
gen_bpmn2_OutputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_OutputSet)
gen_bpmn2_InputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputSet)
gen_bpmn2_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataInput)
gen_bpmn2_Resource_RootElement = Generalization(general=RootElement, specific=bpmn2_Resource)
gen_bpmn2_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceParameter)
gen_bpmn2_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataOutput)
gen_bpmn2_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceRole)
gen_bpmn2_Expression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Expression)
gen_bpmn2_Monitoring_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Monitoring)
gen_bpmn2_Performer_ResourceRole = Generalization(general=ResourceRole, specific=bpmn2_Performer)
gen_bpmn2_Process_CallableElement = Generalization(general=CallableElement, specific=bpmn2_Process)
gen_bpmn2_Process_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Process)
gen_bpmn2_FlowNode_FlowElement = Generalization(general=FlowElement, specific=bpmn2_FlowNode)
gen_bpmn2_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElementsContainer)
gen_bpmn2_FlowElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElement)
gen_bpmn2_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CategoryValue)
gen_bpmn2_LaneSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LaneSet)
gen_bpmn2_Lane_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Lane)
gen_bpmn2_Choreography_Collaboration = Generalization(general=Collaboration, specific=bpmn2_Choreography)
gen_bpmn2_Choreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Choreography)
gen_bpmn2_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=bpmn2_SequenceFlow)
gen_bpmn2_Property_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_Property)
gen_bpmn2_Collaboration_RootElement = Generalization(general=RootElement, specific=bpmn2_Collaboration)
gen_bpmn2_Artifact_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Artifact)
gen_bpmn2_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ParticipantAssociation)
gen_bpmn2_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationLink)
gen_bpmn2_Participant_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Participant)
gen_bpmn2_Participant_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Participant)
gen_bpmn2_ConversationAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationAssociation)
gen_bpmn2_ConversationNode_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationNode)
gen_bpmn2_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_ConversationNode)
gen_bpmn2_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationKey)
gen_bpmn2_CorrelationProperty_RootElement = Generalization(general=RootElement, specific=bpmn2_CorrelationProperty)
gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyRetrievalExpression)
gen_bpmn2_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlowAssociation)
gen_bpmn2_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlow)
gen_bpmn2_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationSubscription)
gen_bpmn2_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyBinding)
gen_bpmn2_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalManualTask)
gen_bpmn2_ManualTask_Task = Generalization(general=Task, specific=bpmn2_ManualTask)
gen_bpmn2_Task_Activity = Generalization(general=Activity, specific=bpmn2_Task)
gen_bpmn2_Activity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Activity)
gen_bpmn2_Activity_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Activity)
gen_bpmn2_FormalExpression_Expression = Generalization(general=Expression, specific=bpmn2_FormalExpression)
gen_bpmn2_CatchEvent_Event = Generalization(general=Event, specific=bpmn2_CatchEvent)
gen_bpmn2_Event_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Event)
gen_bpmn2_Event_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Event)
gen_bpmn2_EventDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_EventDefinition)
gen_bpmn2_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataOutputAssociation)
gen_bpmn2_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataAssociation)
gen_bpmn2_Assignment_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Assignment)
gen_bpmn2_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LoopCharacteristics)
gen_bpmn2_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_BoundaryEvent)
gen_bpmn2_Rendering_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Rendering)
gen_bpmn2_HumanPerformer_Performer = Generalization(general=Performer, specific=bpmn2_HumanPerformer)
gen_bpmn2_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=bpmn2_PotentialOwner)
gen_bpmn2_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalUserTask)
gen_bpmn2_Gateway_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Gateway)
gen_bpmn2_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_EventBasedGateway)
gen_bpmn2_ComplexGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ComplexGateway)
gen_bpmn2_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ExclusiveGateway)
gen_bpmn2_InclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_InclusiveGateway)
gen_bpmn2_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataInputAssociation)
gen_bpmn2_UserTask_Task = Generalization(general=Task, specific=bpmn2_UserTask)
gen_bpmn2_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_IntermediateCatchEvent)
gen_bpmn2_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_IntermediateThrowEvent)
gen_bpmn2_ThrowEvent_Event = Generalization(general=Event, specific=bpmn2_ThrowEvent)
gen_bpmn2_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_EndEvent)
gen_bpmn2_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_StartEvent)
gen_bpmn2_ParallelGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ParallelGateway)
gen_bpmn2_Relationship_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Relationship)
gen_bpmn2_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_EscalationEventDefinition)
gen_bpmn2_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CompensateEventDefinition)
gen_bpmn2_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TimerEventDefinition)
gen_bpmn2_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_LinkEventDefinition)
gen_bpmn2_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CancelEventDefinition)
gen_bpmn2_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ErrorEventDefinition)
gen_bpmn2_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TerminateEventDefinition)
gen_bpmn2_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ConditionalEventDefinition)
gen_bpmn2_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_SignalEventDefinition)
gen_bpmn2_Signal_RootElement = Generalization(general=RootElement, specific=bpmn2_Signal)
gen_bpmn2_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_ImplicitThrowEvent)
gen_bpmn2_DataObject_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObject)
gen_bpmn2_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObject)
gen_bpmn2_DataStore_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStore)
gen_bpmn2_DataStore_RootElement = Generalization(general=RootElement, specific=bpmn2_DataStore)
gen_bpmn2_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_MessageEventDefinition)
gen_bpmn2_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_CallConversation)
gen_bpmn2_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_Conversation)
gen_bpmn2_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_SubConversation)
gen_bpmn2_GlobalConversation_Collaboration = Generalization(general=Collaboration, specific=bpmn2_GlobalConversation)
gen_bpmn2_PartnerEntity_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerEntity)
gen_bpmn2_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_ChoreographyActivity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_ChoreographyActivity)
gen_bpmn2_CallChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_CallChoreography)
gen_bpmn2_SubChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_SubChoreography)
gen_bpmn2_SubChoreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubChoreography)
gen_bpmn2_PartnerRole_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerRole)
gen_bpmn2_GlobalChoreographyTask_Choreography = Generalization(general=Choreography, specific=bpmn2_GlobalChoreographyTask)
gen_bpmn2_TextAnnotation_Artifact = Generalization(general=Artifact, specific=bpmn2_TextAnnotation)
gen_bpmn2_Group_Artifact = Generalization(general=Artifact, specific=bpmn2_Group)
gen_bpmn2_Association_Artifact = Generalization(general=Artifact, specific=bpmn2_Association)
gen_bpmn2_Category_RootElement = Generalization(general=RootElement, specific=bpmn2_Category)
gen_bpmn2_ChoreographyTask_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_ChoreographyTask)
gen_bpmn2_SubProcess_Activity = Generalization(general=Activity, specific=bpmn2_SubProcess)
gen_bpmn2_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubProcess)
gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_MultiInstanceLoopCharacteristics)
gen_bpmn2_ServiceTask_Task = Generalization(general=Task, specific=bpmn2_ServiceTask)
gen_bpmn2_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ComplexBehaviorDefinition)
gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_StandardLoopCharacteristics)
gen_bpmn2_CallActivity_Activity = Generalization(general=Activity, specific=bpmn2_CallActivity)
gen_bpmn2_ReceiveTask_Task = Generalization(general=Task, specific=bpmn2_ReceiveTask)
gen_bpmn2_ScriptTask_Task = Generalization(general=Task, specific=bpmn2_ScriptTask)
gen_bpmn2_BusinessRuleTask_Task = Generalization(general=Task, specific=bpmn2_BusinessRuleTask)
gen_bpmn2_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=bpmn2_AdHocSubProcess)
gen_bpmn2_SendTask_Task = Generalization(general=Task, specific=bpmn2_SendTask)
gen_bpmn2_Transaction_SubProcess = Generalization(general=SubProcess, specific=bpmn2_Transaction)
gen_bpmn2_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalScriptTask)
gen_bpmn2_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalBusinessRuleTask)
gen_bpmn2_Definitions_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Definitions)

# Domain Model
domain_model = DomainModel(
    name="bpmn2",
    types={bpmn2_Interface, RootElement, bpmn2_Operation, bpmn2_EObject, bpmn2_Message, bpmn2_Error, bpmn2_RootElement, BaseElement, bpmn2_BaseElement, bpmn2_ExtensionDefinition, bpmn2_ExtensionAttributeValue, bpmn2_Documentation, bpmn2_ExtensionAttributeDefinition, bpmn2_ResourceRole, bpmn2_CallableElement, bpmn2_InputOutputSpecification, bpmn2_InputOutputBinding, bpmn2_ItemDefinition, bpmn2_Import, bpmn2_EndPoint, bpmn2_Auditing, bpmn2_GlobalTask, CallableElement, bpmn2_ItemAwareElement, bpmn2_DataState, bpmn2_InputSet, bpmn2_OutputSet, bpmn2_DataInput, bpmn2_DataOutput, ItemAwareElement, bpmn2_ResourceParameterBinding, bpmn2_ResourceAssignmentExpression, bpmn2_ResourceParameter, bpmn2_Resource, bpmn2_Artifact, bpmn2_CorrelationSubscription, bpmn2_Expression, bpmn2_Monitoring, bpmn2_Performer, ResourceRole, bpmn2_Process, FlowElementsContainer, bpmn2_Property, bpmn2_Collaboration, FlowElement, bpmn2_SequenceFlow, bpmn2_FlowElementsContainer, bpmn2_FlowElement, bpmn2_LaneSet, bpmn2_CategoryValue, bpmn2_Lane, bpmn2_FlowNode, bpmn2_CorrelationKey, bpmn2_ConversationNode, bpmn2_ConversationLink, Collaboration, bpmn2_Choreography, bpmn2_ParticipantAssociation, bpmn2_MessageFlowAssociation, bpmn2_ConversationAssociation, bpmn2_Participant, bpmn2_MessageFlow, bpmn2_ParticipantMultiplicity, bpmn2_InteractionNode, InteractionNode, bpmn2_CorrelationProperty, bpmn2_CorrelationPropertyRetrievalExpression, bpmn2_FormalExpression, bpmn2_CorrelationPropertyBinding, bpmn2_GlobalManualTask, GlobalTask, bpmn2_ManualTask, Task, bpmn2_Task, Activity, bpmn2_Activity, FlowNode, bpmn2_LoopCharacteristics, bpmn2_BoundaryEvent, bpmn2_DataInputAssociation, bpmn2_DataOutputAssociation, Expression, bpmn2_CatchEvent, Event, bpmn2_EventDefinition, bpmn2_Event, DataAssociation, bpmn2_DataAssociation, bpmn2_Assignment, CatchEvent, bpmn2_Rendering, bpmn2_HumanPerformer, Performer, bpmn2_PotentialOwner, HumanPerformer, bpmn2_GlobalUserTask, bpmn2_Gateway, bpmn2_EventBasedGateway, Gateway, bpmn2_ComplexGateway, bpmn2_ExclusiveGateway, bpmn2_InclusiveGateway, bpmn2_UserTask, bpmn2_Extension, bpmn2_IntermediateCatchEvent, bpmn2_IntermediateThrowEvent, ThrowEvent, bpmn2_ThrowEvent, bpmn2_EndEvent, bpmn2_StartEvent, bpmn2_CancelEventDefinition, bpmn2_ParallelGateway, bpmn2_Relationship, bpmn2_EscalationEventDefinition, bpmn2_Escalation, bpmn2_CompensateEventDefinition, bpmn2_TimerEventDefinition, bpmn2_LinkEventDefinition, EventDefinition, bpmn2_ErrorEventDefinition, bpmn2_TerminateEventDefinition, bpmn2_ConditionalEventDefinition, bpmn2_SignalEventDefinition, bpmn2_Signal, bpmn2_ImplicitThrowEvent, bpmn2_DataObject, bpmn2_DataStore, bpmn2_MessageEventDefinition, bpmn2_DataObjectReference, bpmn2_CallConversation, ConversationNode, bpmn2_Conversation, bpmn2_SubConversation, bpmn2_GlobalConversation, bpmn2_PartnerEntity, bpmn2_PartnerRole, bpmn2_DataStoreReference, bpmn2_ChoreographyActivity, bpmn2_CallChoreography, ChoreographyActivity, bpmn2_SubChoreography, bpmn2_GlobalChoreographyTask, Choreography, bpmn2_TextAnnotation, Artifact, bpmn2_Group, bpmn2_Association, bpmn2_Category, bpmn2_ChoreographyTask, bpmn2_SubProcess, bpmn2_MultiInstanceLoopCharacteristics, LoopCharacteristics, bpmn2_ServiceTask, bpmn2_ComplexBehaviorDefinition, bpmn2_StandardLoopCharacteristics, bpmn2_CallActivity, bpmn2_ReceiveTask, bpmn2_ScriptTask, bpmn2_BusinessRuleTask, bpmn2_AdHocSubProcess, SubProcess, bpmn2_SendTask, bpmn2_Transaction, bpmn2_GlobalScriptTask, bpmn2_GlobalBusinessRuleTask, bpmn2_Definitions, bpmn2_BPMNDiagram, ItemKind, ProcessType, GatewayDirection, EventBasedGatewayType, RelationshipDirection, ChoreographyLoopType, AssociationDirection, MultiInstanceBehavior, AdHocOrdering},
    associations={operations0, implementationRef1, inMessageRef18, outMessageRef20, errorRefs23, implementationRef25, extensionDefinitions3, extensionValues4, documentation6, extensionAttributeDefinitions8, extensionDefinition9, valueRef10, value13, extensionAttributeDefinition16, resources38, ioSpecification39, supportedInterfaceRefs40, ioBinding43, itemRef28, structureRef30, import33, structureRef35, itemSubjectRef65, dataState67, dataOutputRefs69, inputSets45, outputSets47, dataInputs49, dataOutputs51, dataInputRefs53, optionalInputRefs54, whileExecutingInputRefs56, outputSetRefs58, inputSetWithOptional60, inputSetWithWhileExecuting61, inputSetRefs63, resourceParameterBindings94, resourceAssignmentExpression96, resourceParameters98, optionalOutputRefs70, whileExecutingOutputRefs72, inputSetRefs74, outputSetWithOptional77, outputSetWithWhileExecuting79, outputSetRefs81, inputDataRef83, outputDataRef86, operationRef89, resourceRef92, resources121, artifacts124, correlationSubscriptions126, decomposedBy129, decomposes131, type100, expression103, parameterRef105, expression108, auditing111, monitoring112, properties114, supports117, definitionalCollaborationRef119, flowNodeRefs152, partitionElement153, outgoing156, incoming157, lanes159, flowElements133, laneSets134, auditing136, monitoring139, categoryValueRef142, categorizedFlowElements143, lanes144, childLaneSet146, partitionElementRef149, correlationKeys181, conversations183, conversationLinks185, conditionExpression160, targetRef162, sourceRef164, choreographyRef166, artifacts168, participantAssociations171, messageFlowAssociations173, conversationAssociations175, participants177, messageFlows179, participantMultiplicity196, endPointRefs198, processRef200, incomingConversationLinks203, outgoingConversationLinks205, sourceRef208, innerParticipantRef187, targetRef209, outerParticipantRef190, interfaceRefs193, targetRef219, messageRef222, innerConversationNodeRef225, outerConversationNodeRef228, participantRefs231, messageFlowRefs234, correlationKeys237, correlationPropertyRef240, correlationPropertyRetrievalExpression242, type244, messagePath247, messageRef249, innerMessageFlowRef211, outerMessageFlowRef214, sourceRef217, evaluatesToTypeRef255, correlationKeyRef258, correlationPropertyBinding261, dataPath263, correlationPropertyRef266, loopCharacteristics269, resources270, default273, properties276, ioSpecification279, boundaryEventRefs282, dataInputAssociations283, dataOutputAssociations285, body252, attachedToRef287, outputSet288, eventDefinitionRefs290, dataOutputAssociation292, dataOutputs295, eventDefinitions298, properties301, transformation303, assignment305, targetRef307, sourceRef310, from313, renderings319, renderings320, activationCondition322, default324, default327, default329, to316, sources331, targets333, definition336, inputSet338, eventDefinitionRefs340, dataInputAssociation343, dataInputs346, eventDefinitions349, escalationRef354, structureRef355, activityRef358, timeDate360, timeCycle362, timeDuration365, errorRef352, operationRef375, condition378, signalRef380, structureRef381, target369, source371, messageRef373, dataStoreRef384, dataObjectRef385, calledCollaborationRef386, participantAssociations388, conversationNodes391, participantRef393, participantRefs397, initiatingParticipantRef399, correlationKeys402, calledChoreographyRef405, participantAssociations407, artifacts410, participantRef395, initiatingParticipantRef414, categoryValueRef416, sourceRef417, targetRef419, categoryValue422, messageFlowRef412, operationRef424, artifacts426, loopCardinality428, loopDataInputRef430, loopDataOutputRef433, inputDataItem436, completionCondition442, complexBehaviorDefinition445, oneBehaviorEventRef447, noneBehaviorEventRef450, condition453, event456, loopCondition458, loopMaximum460, outputDataItem439, operationRef465, messageRef467, operationRef470, messageRef472, completionCondition475, calledElementRef463, imports477, extensions479, diagrams487, relationships482, rootElements485},
    generalizations={gen_bpmn2_Interface_RootElement, gen_bpmn2_Operation_BaseElement, gen_bpmn2_RootElement_BaseElement, gen_bpmn2_Documentation_BaseElement, gen_bpmn2_CallableElement_RootElement, gen_bpmn2_InputOutputSpecification_BaseElement, gen_bpmn2_Message_RootElement, gen_bpmn2_ItemDefinition_RootElement, gen_bpmn2_Error_RootElement, gen_bpmn2_EndPoint_RootElement, gen_bpmn2_Auditing_BaseElement, gen_bpmn2_GlobalTask_CallableElement, gen_bpmn2_ItemAwareElement_BaseElement, gen_bpmn2_DataState_BaseElement, gen_bpmn2_OutputSet_BaseElement, gen_bpmn2_InputSet_BaseElement, gen_bpmn2_DataInput_ItemAwareElement, gen_bpmn2_Resource_RootElement, gen_bpmn2_ResourceParameter_BaseElement, gen_bpmn2_DataOutput_ItemAwareElement, gen_bpmn2_ResourceRole_BaseElement, gen_bpmn2_Expression_BaseElement, gen_bpmn2_Monitoring_BaseElement, gen_bpmn2_Performer_ResourceRole, gen_bpmn2_Process_CallableElement, gen_bpmn2_Process_FlowElementsContainer, gen_bpmn2_FlowNode_FlowElement, gen_bpmn2_FlowElementsContainer_BaseElement, gen_bpmn2_FlowElement_BaseElement, gen_bpmn2_CategoryValue_BaseElement, gen_bpmn2_LaneSet_BaseElement, gen_bpmn2_Lane_BaseElement, gen_bpmn2_Choreography_Collaboration, gen_bpmn2_Choreography_FlowElementsContainer, gen_bpmn2_SequenceFlow_FlowElement, gen_bpmn2_Property_ItemAwareElement, gen_bpmn2_Collaboration_RootElement, gen_bpmn2_Artifact_BaseElement, gen_bpmn2_ParticipantAssociation_BaseElement, gen_bpmn2_ConversationLink_BaseElement, gen_bpmn2_Participant_BaseElement, gen_bpmn2_Participant_InteractionNode, gen_bpmn2_ConversationAssociation_BaseElement, gen_bpmn2_ConversationNode_BaseElement, gen_bpmn2_ConversationNode_InteractionNode, gen_bpmn2_CorrelationKey_BaseElement, gen_bpmn2_CorrelationProperty_RootElement, gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement, gen_bpmn2_MessageFlowAssociation_BaseElement, gen_bpmn2_MessageFlow_BaseElement, gen_bpmn2_CorrelationSubscription_BaseElement, gen_bpmn2_CorrelationPropertyBinding_BaseElement, gen_bpmn2_GlobalManualTask_GlobalTask, gen_bpmn2_ManualTask_Task, gen_bpmn2_Task_Activity, gen_bpmn2_Activity_FlowNode, gen_bpmn2_Activity_InteractionNode, gen_bpmn2_FormalExpression_Expression, gen_bpmn2_CatchEvent_Event, gen_bpmn2_Event_FlowNode, gen_bpmn2_Event_InteractionNode, gen_bpmn2_EventDefinition_RootElement, gen_bpmn2_DataOutputAssociation_DataAssociation, gen_bpmn2_DataAssociation_BaseElement, gen_bpmn2_Assignment_BaseElement, gen_bpmn2_LoopCharacteristics_BaseElement, gen_bpmn2_BoundaryEvent_CatchEvent, gen_bpmn2_Rendering_BaseElement, gen_bpmn2_HumanPerformer_Performer, gen_bpmn2_PotentialOwner_HumanPerformer, gen_bpmn2_GlobalUserTask_GlobalTask, gen_bpmn2_Gateway_FlowNode, gen_bpmn2_EventBasedGateway_Gateway, gen_bpmn2_ComplexGateway_Gateway, gen_bpmn2_ExclusiveGateway_Gateway, gen_bpmn2_InclusiveGateway_Gateway, gen_bpmn2_DataInputAssociation_DataAssociation, gen_bpmn2_UserTask_Task, gen_bpmn2_IntermediateCatchEvent_CatchEvent, gen_bpmn2_IntermediateThrowEvent_ThrowEvent, gen_bpmn2_ThrowEvent_Event, gen_bpmn2_EndEvent_ThrowEvent, gen_bpmn2_StartEvent_CatchEvent, gen_bpmn2_ParallelGateway_Gateway, gen_bpmn2_Relationship_BaseElement, gen_bpmn2_EscalationEventDefinition_EventDefinition, gen_bpmn2_CompensateEventDefinition_EventDefinition, gen_bpmn2_TimerEventDefinition_EventDefinition, gen_bpmn2_LinkEventDefinition_EventDefinition, gen_bpmn2_CancelEventDefinition_EventDefinition, gen_bpmn2_ErrorEventDefinition_EventDefinition, gen_bpmn2_TerminateEventDefinition_EventDefinition, gen_bpmn2_ConditionalEventDefinition_EventDefinition, gen_bpmn2_SignalEventDefinition_EventDefinition, gen_bpmn2_Signal_RootElement, gen_bpmn2_ImplicitThrowEvent_ThrowEvent, gen_bpmn2_DataObject_FlowElement, gen_bpmn2_DataObject_ItemAwareElement, gen_bpmn2_DataStore_ItemAwareElement, gen_bpmn2_DataStore_RootElement, gen_bpmn2_MessageEventDefinition_EventDefinition, gen_bpmn2_DataObjectReference_FlowElement, gen_bpmn2_DataObjectReference_ItemAwareElement, gen_bpmn2_CallConversation_ConversationNode, gen_bpmn2_Conversation_ConversationNode, gen_bpmn2_SubConversation_ConversationNode, gen_bpmn2_GlobalConversation_Collaboration, gen_bpmn2_PartnerEntity_RootElement, gen_bpmn2_DataStoreReference_FlowElement, gen_bpmn2_DataStoreReference_ItemAwareElement, gen_bpmn2_ChoreographyActivity_FlowNode, gen_bpmn2_CallChoreography_ChoreographyActivity, gen_bpmn2_SubChoreography_ChoreographyActivity, gen_bpmn2_SubChoreography_FlowElementsContainer, gen_bpmn2_PartnerRole_RootElement, gen_bpmn2_GlobalChoreographyTask_Choreography, gen_bpmn2_TextAnnotation_Artifact, gen_bpmn2_Group_Artifact, gen_bpmn2_Association_Artifact, gen_bpmn2_Category_RootElement, gen_bpmn2_ChoreographyTask_ChoreographyActivity, gen_bpmn2_SubProcess_Activity, gen_bpmn2_SubProcess_FlowElementsContainer, gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics, gen_bpmn2_ServiceTask_Task, gen_bpmn2_ComplexBehaviorDefinition_BaseElement, gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics, gen_bpmn2_CallActivity_Activity, gen_bpmn2_ReceiveTask_Task, gen_bpmn2_ScriptTask_Task, gen_bpmn2_BusinessRuleTask_Task, gen_bpmn2_AdHocSubProcess_SubProcess, gen_bpmn2_SendTask_Task, gen_bpmn2_Transaction_SubProcess, gen_bpmn2_GlobalScriptTask_GlobalTask, gen_bpmn2_GlobalBusinessRuleTask_GlobalTask, gen_bpmn2_Definitions_BaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)