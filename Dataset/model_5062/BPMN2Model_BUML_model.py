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
AdHocOrdering: Enumeration = Enumeration(
    name="AdHocOrdering",
    literals={
            EnumerationLiteral(name="Parallel"),
			EnumerationLiteral(name="Sequential")
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

ChoreographyLoopType: Enumeration = Enumeration(
    name="ChoreographyLoopType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Standard"),
			EnumerationLiteral(name="MultiInstanceSequential"),
			EnumerationLiteral(name="MultiInstanceParallel")
    }
)

EventBasedGatewayType: Enumeration = Enumeration(
    name="EventBasedGatewayType",
    literals={
            EnumerationLiteral(name="Parallel"),
			EnumerationLiteral(name="Exclusive")
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

ItemKind: Enumeration = Enumeration(
    name="ItemKind",
    literals={
            EnumerationLiteral(name="Physical"),
			EnumerationLiteral(name="Information")
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

ProcessType: Enumeration = Enumeration(
    name="ProcessType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Public"),
			EnumerationLiteral(name="Private")
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

# Classes
BPMN2Model_DocumentRoot = Class(name="BPMN2Model::DocumentRoot")
BPMNBase = Class(name="BPMNBase")
BPMN2Model_EStringToStringMapEntry = Class(name="BPMN2Model::EStringToStringMapEntry")
BPMN2Model_Activity = Class(name="BPMN2Model::Activity")
BPMN2Model_AdHocSubProcess = Class(name="BPMN2Model::AdHocSubProcess")
BPMN2Model_FlowElement = Class(name="BPMN2Model::FlowElement", is_abstract=True)
BPMN2Model_Artifact = Class(name="BPMN2Model::Artifact")
BPMN2Model_Assignment = Class(name="BPMN2Model::Assignment")
BPMN2Model_Association = Class(name="BPMN2Model::Association")
BPMN2Model_Auditing = Class(name="BPMN2Model::Auditing")
BPMN2Model_BaseElement = Class(name="BPMN2Model::BaseElement")
BPMN2Model_BoundaryEvent = Class(name="BPMN2Model::BoundaryEvent")
BPMN2Model_BusinessRuleTask = Class(name="BPMN2Model::BusinessRuleTask")
BPMN2Model_CallableElement = Class(name="BPMN2Model::CallableElement")
BPMN2Model_CallActivity = Class(name="BPMN2Model::CallActivity")
BPMN2Model_CallChoreography = Class(name="BPMN2Model::CallChoreography")
BPMN2Model_CallConversation = Class(name="BPMN2Model::CallConversation")
BPMN2Model_ConversationNode = Class(name="BPMN2Model::ConversationNode")
BPMN2Model_CancelEventDefinition = Class(name="BPMN2Model::CancelEventDefinition")
BPMN2Model_EventDefinition = Class(name="BPMN2Model::EventDefinition")
BPMN2Model_RootElement = Class(name="BPMN2Model::RootElement")
BPMN2Model_CatchEvent = Class(name="BPMN2Model::CatchEvent", is_abstract=True)
BPMN2Model_Category = Class(name="BPMN2Model::Category")
BPMN2Model_CategoryValue = Class(name="BPMN2Model::CategoryValue")
BPMN2Model_Choreography = Class(name="BPMN2Model::Choreography")
BPMN2Model_Collaboration = Class(name="BPMN2Model::Collaboration")
BPMN2Model_ChoreographyActivity = Class(name="BPMN2Model::ChoreographyActivity", is_abstract=True)
BPMN2Model_ChoreographyTask = Class(name="BPMN2Model::ChoreographyTask")
BPMN2Model_CompensateEventDefinition = Class(name="BPMN2Model::CompensateEventDefinition")
BPMN2Model_ComplexBehaviorDefinition = Class(name="BPMN2Model::ComplexBehaviorDefinition")
BPMN2Model_ComplexGateway = Class(name="BPMN2Model::ComplexGateway")
BPMN2Model_ConditionalEventDefinition = Class(name="BPMN2Model::ConditionalEventDefinition")
BPMN2Model_Conversation = Class(name="BPMN2Model::Conversation")
BPMN2Model_ConversationLink = Class(name="BPMN2Model::ConversationLink")
BPMN2Model_CorrelationKey = Class(name="BPMN2Model::CorrelationKey")
BPMN2Model_CorrelationProperty = Class(name="BPMN2Model::CorrelationProperty")
BPMN2Model_CorrelationPropertyBinding = Class(name="BPMN2Model::CorrelationPropertyBinding")
BPMN2Model_CorrelationPropertyRetrievalExpression = Class(name="BPMN2Model::CorrelationPropertyRetrievalExpression")
BPMN2Model_CorrelationSubscription = Class(name="BPMN2Model::CorrelationSubscription")
BPMN2Model_DataAssociation = Class(name="BPMN2Model::DataAssociation")
BPMN2Model_DataInput = Class(name="BPMN2Model::DataInput")
BPMN2Model_DataInputAssociation = Class(name="BPMN2Model::DataInputAssociation")
BPMN2Model_DataObject = Class(name="BPMN2Model::DataObject")
BPMN2Model_DataObjectReference = Class(name="BPMN2Model::DataObjectReference")
BPMN2Model_DataOutput = Class(name="BPMN2Model::DataOutput")
BPMN2Model_DataOutputAssociation = Class(name="BPMN2Model::DataOutputAssociation")
BPMN2Model_DataState = Class(name="BPMN2Model::DataState")
BPMN2Model_DataStore = Class(name="BPMN2Model::DataStore")
BPMN2Model_ConversationAssociation = Class(name="BPMN2Model::ConversationAssociation")
BPMN2Model_DataStoreReference = Class(name="BPMN2Model::DataStoreReference")
BPMN2Model_Definitions = Class(name="BPMN2Model::Definitions")
BPMN2Model_Documentation = Class(name="BPMN2Model::Documentation")
BPMN2Model_EndEvent = Class(name="BPMN2Model::EndEvent")
BPMN2Model_EndPoint = Class(name="BPMN2Model::EndPoint")
BPMN2Model_Error = Class(name="BPMN2Model::Error")
BPMN2Model_ErrorEventDefinition = Class(name="BPMN2Model::ErrorEventDefinition")
BPMN2Model_Escalation = Class(name="BPMN2Model::Escalation")
BPMN2Model_EscalationEventDefinition = Class(name="BPMN2Model::EscalationEventDefinition")
BPMN2Model_Event = Class(name="BPMN2Model::Event", is_abstract=True)
BPMN2Model_EventBasedGateway = Class(name="BPMN2Model::EventBasedGateway")
BPMN2Model_ExclusiveGateway = Class(name="BPMN2Model::ExclusiveGateway")
BPMN2Model_Expression = Class(name="BPMN2Model::Expression")
BPMN2Model_Extension = Class(name="BPMN2Model::Extension")
BPMN2Model_ExtensionAttributeValue = Class(name="BPMN2Model::ExtensionAttributeValue")
BPMN2Model_FlowNode = Class(name="BPMN2Model::FlowNode", is_abstract=True)
BPMN2Model_FormalExpression = Class(name="BPMN2Model::FormalExpression")
BPMN2Model_Gateway = Class(name="BPMN2Model::Gateway", is_abstract=True)
BPMN2Model_GlobalBusinessRuleTask = Class(name="BPMN2Model::GlobalBusinessRuleTask")
BPMN2Model_GlobalChoreographyTask = Class(name="BPMN2Model::GlobalChoreographyTask")
BPMN2Model_GlobalConversation = Class(name="BPMN2Model::GlobalConversation")
BPMN2Model_GlobalManualTask = Class(name="BPMN2Model::GlobalManualTask")
BPMN2Model_GlobalScriptTask = Class(name="BPMN2Model::GlobalScriptTask")
BPMN2Model_GlobalTask = Class(name="BPMN2Model::GlobalTask")
BPMN2Model_GlobalUserTask = Class(name="BPMN2Model::GlobalUserTask")
BPMN2Model_Group = Class(name="BPMN2Model::Group")
BPMN2Model_HumanPerformer = Class(name="BPMN2Model::HumanPerformer")
BPMN2Model_Performer = Class(name="BPMN2Model::Performer")
BPMN2Model_ResourceRole = Class(name="BPMN2Model::ResourceRole")
BPMN2Model_ImplicitThrowEvent = Class(name="BPMN2Model::ImplicitThrowEvent")
BPMN2Model_Import = Class(name="BPMN2Model::Import")
BPMN2Model_InclusiveGateway = Class(name="BPMN2Model::InclusiveGateway")
BPMN2Model_InputSet = Class(name="BPMN2Model::InputSet")
BPMN2Model_IntermediateCatchEvent = Class(name="BPMN2Model::IntermediateCatchEvent")
BPMN2Model_IntermediateThrowEvent = Class(name="BPMN2Model::IntermediateThrowEvent")
BPMN2Model_InputOutputBinding = Class(name="BPMN2Model::InputOutputBinding")
BPMN2Model_InputOutputSpecification = Class(name="BPMN2Model::InputOutputSpecification")
BPMN2Model_ItemDefinition = Class(name="BPMN2Model::ItemDefinition")
BPMN2Model_Lane = Class(name="BPMN2Model::Lane")
BPMN2Model_LaneSet = Class(name="BPMN2Model::LaneSet")
BPMN2Model_LinkEventDefinition = Class(name="BPMN2Model::LinkEventDefinition")
BPMN2Model_LoopCharacteristics = Class(name="BPMN2Model::LoopCharacteristics", is_abstract=True)
BPMN2Model_ManualTask = Class(name="BPMN2Model::ManualTask")
BPMN2Model_Interface = Class(name="BPMN2Model::Interface")
BPMN2Model_Message = Class(name="BPMN2Model::Message")
BPMN2Model_MessageEventDefinition = Class(name="BPMN2Model::MessageEventDefinition")
BPMN2Model_MessageFlow = Class(name="BPMN2Model::MessageFlow")
BPMN2Model_MessageFlowAssociation = Class(name="BPMN2Model::MessageFlowAssociation")
BPMN2Model_Monitoring = Class(name="BPMN2Model::Monitoring")
BPMN2Model_MultiInstanceLoopCharacteristics = Class(name="BPMN2Model::MultiInstanceLoopCharacteristics")
BPMN2Model_Operation = Class(name="BPMN2Model::Operation")
BPMN2Model_OutputSet = Class(name="BPMN2Model::OutputSet")
BPMN2Model_ParallelGateway = Class(name="BPMN2Model::ParallelGateway")
BPMN2Model_Participant = Class(name="BPMN2Model::Participant")
BPMN2Model_ParticipantAssociation = Class(name="BPMN2Model::ParticipantAssociation")
BPMN2Model_ParticipantMultiplicity = Class(name="BPMN2Model::ParticipantMultiplicity")
BPMN2Model_PartnerEntity = Class(name="BPMN2Model::PartnerEntity")
BPMN2Model_PartnerRole = Class(name="BPMN2Model::PartnerRole")
BPMN2Model_PotentialOwner = Class(name="BPMN2Model::PotentialOwner")
BPMN2Model_Process = Class(name="BPMN2Model::Process")
BPMN2Model_Property = Class(name="BPMN2Model::Property")
BPMN2Model_ReceiveTask = Class(name="BPMN2Model::ReceiveTask")
BPMN2Model_Relationship = Class(name="BPMN2Model::Relationship")
BPMN2Model_Rendering = Class(name="BPMN2Model::Rendering")
BPMN2Model_Resource = Class(name="BPMN2Model::Resource")
BPMN2Model_ResourceAssignmentExpression = Class(name="BPMN2Model::ResourceAssignmentExpression")
BPMN2Model_ResourceParameterBinding = Class(name="BPMN2Model::ResourceParameterBinding")
BPMN2Model_EObject = Class(name="BPMN2Model::EObject")
BPMN2Model_ScriptTask = Class(name="BPMN2Model::ScriptTask")
BPMN2Model_SendTask = Class(name="BPMN2Model::SendTask")
BPMN2Model_SequenceFlow = Class(name="BPMN2Model::SequenceFlow")
BPMN2Model_ServiceTask = Class(name="BPMN2Model::ServiceTask")
BPMN2Model_Signal = Class(name="BPMN2Model::Signal")
BPMN2Model_SignalEventDefinition = Class(name="BPMN2Model::SignalEventDefinition")
BPMN2Model_StandardLoopCharacteristics = Class(name="BPMN2Model::StandardLoopCharacteristics")
BPMN2Model_StartEvent = Class(name="BPMN2Model::StartEvent")
BPMN2Model_ResourceParameter = Class(name="BPMN2Model::ResourceParameter")
BPMN2Model_SubChoreography = Class(name="BPMN2Model::SubChoreography")
BPMN2Model_SubConversation = Class(name="BPMN2Model::SubConversation")
BPMN2Model_SubProcess = Class(name="BPMN2Model::SubProcess")
BPMN2Model_Task = Class(name="BPMN2Model::Task")
BPMN2Model_TerminateEventDefinition = Class(name="BPMN2Model::TerminateEventDefinition")
BPMN2Model_TextAnnotation = Class(name="BPMN2Model::TextAnnotation")
BPMN2Model_ThrowEvent = Class(name="BPMN2Model::ThrowEvent", is_abstract=True)
BPMN2Model_TimerEventDefinition = Class(name="BPMN2Model::TimerEventDefinition")
BPMN2Model_Transaction = Class(name="BPMN2Model::Transaction")
BPMN2Model_UserTask = Class(name="BPMN2Model::UserTask")
FlowNode = Class(name="FlowNode")
SubProcess = Class(name="SubProcess")
BaseElement = Class(name="BaseElement")
Artifact = Class(name="Artifact")
BPMN2Model_ExtensionDefinition = Class(name="BPMN2Model::ExtensionDefinition")
CatchEvent = Class(name="CatchEvent")
Task = Class(name="Task")
Activity = Class(name="Activity")
ChoreographyActivity = Class(name="ChoreographyActivity")
ConversationNode = Class(name="ConversationNode")
RootElement = Class(name="RootElement")
EventDefinition = Class(name="EventDefinition")
Event = Class(name="Event")
Collaboration = Class(name="Collaboration")
FlowElementsContainer = Class(name="FlowElementsContainer")
Gateway = Class(name="Gateway")
BPMN2Model_InteractionNode = Class(name="BPMN2Model::InteractionNode")
InteractionNode = Class(name="InteractionNode")
BPMN2Model_ItemAwareElement = Class(name="BPMN2Model::ItemAwareElement")
ItemAwareElement = Class(name="ItemAwareElement")
DataAssociation = Class(name="DataAssociation")
FlowElement = Class(name="FlowElement")
ThrowEvent = Class(name="ThrowEvent")
BPMN2Model_ExtensionAttributeDefinition = Class(name="BPMN2Model::ExtensionAttributeDefinition")
BPMN2Model_FlowElementsContainer = Class(name="BPMN2Model::FlowElementsContainer", is_abstract=True)
Expression = Class(name="Expression")
GlobalTask = Class(name="GlobalTask")
Choreography = Class(name="Choreography")
CallableElement = Class(name="CallableElement")
Performer = Class(name="Performer")
LoopCharacteristics = Class(name="LoopCharacteristics")
ResourceRole = Class(name="ResourceRole")
HumanPerformer = Class(name="HumanPerformer")
BPMN2Model_BPMNBase = Class(name="BPMN2Model::BPMNBase", is_abstract=True)
EObject = Class(name="EObject")

# BPMN2Model_DocumentRoot class attributes and methods
BPMN2Model_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
BPMN2Model_DocumentRoot.attributes={BPMN2Model_DocumentRoot_mixed}

# BPMNBase class attributes and methods

# BPMN2Model_EStringToStringMapEntry class attributes and methods

# BPMN2Model_Activity class attributes and methods
BPMN2Model_Activity_completionQuantity: Property = Property(name="completionQuantity", type=IntegerType)
BPMN2Model_Activity_isForCompensation: Property = Property(name="isForCompensation", type=BooleanType)
BPMN2Model_Activity_startQuantity: Property = Property(name="startQuantity", type=IntegerType)
BPMN2Model_Activity.attributes={BPMN2Model_Activity_completionQuantity, BPMN2Model_Activity_isForCompensation, BPMN2Model_Activity_startQuantity}

# BPMN2Model_AdHocSubProcess class attributes and methods
BPMN2Model_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=BooleanType)
BPMN2Model_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
BPMN2Model_AdHocSubProcess.attributes={BPMN2Model_AdHocSubProcess_ordering, BPMN2Model_AdHocSubProcess_cancelRemainingInstances}

# BPMN2Model_FlowElement class attributes and methods
BPMN2Model_FlowElement_name: Property = Property(name="name", type=StringType)
BPMN2Model_FlowElement.attributes={BPMN2Model_FlowElement_name}

# BPMN2Model_Artifact class attributes and methods

# BPMN2Model_Assignment class attributes and methods

# BPMN2Model_Association class attributes and methods
BPMN2Model_Association_associationDirection: Property = Property(name="associationDirection", type=StringType)
BPMN2Model_Association.attributes={BPMN2Model_Association_associationDirection}

# BPMN2Model_Auditing class attributes and methods

# BPMN2Model_BaseElement class attributes and methods
BPMN2Model_BaseElement_id: Property = Property(name="id", type=StringType)
BPMN2Model_BaseElement_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
BPMN2Model_BaseElement.attributes={BPMN2Model_BaseElement_anyAttribute, BPMN2Model_BaseElement_id}

# BPMN2Model_BoundaryEvent class attributes and methods
BPMN2Model_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=BooleanType)
BPMN2Model_BoundaryEvent.attributes={BPMN2Model_BoundaryEvent_cancelActivity}

# BPMN2Model_BusinessRuleTask class attributes and methods
BPMN2Model_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_BusinessRuleTask.attributes={BPMN2Model_BusinessRuleTask_implementation}

# BPMN2Model_CallableElement class attributes and methods
BPMN2Model_CallableElement_name: Property = Property(name="name", type=StringType)
BPMN2Model_CallableElement.attributes={BPMN2Model_CallableElement_name}

# BPMN2Model_CallActivity class attributes and methods

# BPMN2Model_CallChoreography class attributes and methods

# BPMN2Model_CallConversation class attributes and methods

# BPMN2Model_ConversationNode class attributes and methods
BPMN2Model_ConversationNode_name: Property = Property(name="name", type=StringType)
BPMN2Model_ConversationNode.attributes={BPMN2Model_ConversationNode_name}

# BPMN2Model_CancelEventDefinition class attributes and methods

# BPMN2Model_EventDefinition class attributes and methods

# BPMN2Model_RootElement class attributes and methods

# BPMN2Model_CatchEvent class attributes and methods
BPMN2Model_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=BooleanType)
BPMN2Model_CatchEvent.attributes={BPMN2Model_CatchEvent_parallelMultiple}

# BPMN2Model_Category class attributes and methods
BPMN2Model_Category_name: Property = Property(name="name", type=StringType)
BPMN2Model_Category.attributes={BPMN2Model_Category_name}

# BPMN2Model_CategoryValue class attributes and methods
BPMN2Model_CategoryValue_value: Property = Property(name="value", type=StringType)
BPMN2Model_CategoryValue.attributes={BPMN2Model_CategoryValue_value}

# BPMN2Model_Choreography class attributes and methods

# BPMN2Model_Collaboration class attributes and methods
BPMN2Model_Collaboration_isClosed: Property = Property(name="isClosed", type=BooleanType)
BPMN2Model_Collaboration_name: Property = Property(name="name", type=StringType)
BPMN2Model_Collaboration.attributes={BPMN2Model_Collaboration_name, BPMN2Model_Collaboration_isClosed}

# BPMN2Model_ChoreographyActivity class attributes and methods
BPMN2Model_ChoreographyActivity_loopType: Property = Property(name="loopType", type=StringType)
BPMN2Model_ChoreographyActivity.attributes={BPMN2Model_ChoreographyActivity_loopType}

# BPMN2Model_ChoreographyTask class attributes and methods

# BPMN2Model_CompensateEventDefinition class attributes and methods
BPMN2Model_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=BooleanType)
BPMN2Model_CompensateEventDefinition.attributes={BPMN2Model_CompensateEventDefinition_waitForCompletion}

# BPMN2Model_ComplexBehaviorDefinition class attributes and methods

# BPMN2Model_ComplexGateway class attributes and methods

# BPMN2Model_ConditionalEventDefinition class attributes and methods

# BPMN2Model_Conversation class attributes and methods

# BPMN2Model_ConversationLink class attributes and methods
BPMN2Model_ConversationLink_name: Property = Property(name="name", type=StringType)
BPMN2Model_ConversationLink.attributes={BPMN2Model_ConversationLink_name}

# BPMN2Model_CorrelationKey class attributes and methods
BPMN2Model_CorrelationKey_name: Property = Property(name="name", type=StringType)
BPMN2Model_CorrelationKey.attributes={BPMN2Model_CorrelationKey_name}

# BPMN2Model_CorrelationProperty class attributes and methods
BPMN2Model_CorrelationProperty_name: Property = Property(name="name", type=StringType)
BPMN2Model_CorrelationProperty.attributes={BPMN2Model_CorrelationProperty_name}

# BPMN2Model_CorrelationPropertyBinding class attributes and methods

# BPMN2Model_CorrelationPropertyRetrievalExpression class attributes and methods

# BPMN2Model_CorrelationSubscription class attributes and methods

# BPMN2Model_DataAssociation class attributes and methods

# BPMN2Model_DataInput class attributes and methods
BPMN2Model_DataInput_isCollection: Property = Property(name="isCollection", type=BooleanType)
BPMN2Model_DataInput_name: Property = Property(name="name", type=StringType)
BPMN2Model_DataInput.attributes={BPMN2Model_DataInput_name, BPMN2Model_DataInput_isCollection}

# BPMN2Model_DataInputAssociation class attributes and methods

# BPMN2Model_DataObject class attributes and methods
BPMN2Model_DataObject_isCollection: Property = Property(name="isCollection", type=BooleanType)
BPMN2Model_DataObject.attributes={BPMN2Model_DataObject_isCollection}

# BPMN2Model_DataObjectReference class attributes and methods

# BPMN2Model_DataOutput class attributes and methods
BPMN2Model_DataOutput_isCollection: Property = Property(name="isCollection", type=BooleanType)
BPMN2Model_DataOutput_name: Property = Property(name="name", type=StringType)
BPMN2Model_DataOutput.attributes={BPMN2Model_DataOutput_isCollection, BPMN2Model_DataOutput_name}

# BPMN2Model_DataOutputAssociation class attributes and methods

# BPMN2Model_DataState class attributes and methods
BPMN2Model_DataState_name: Property = Property(name="name", type=StringType)
BPMN2Model_DataState.attributes={BPMN2Model_DataState_name}

# BPMN2Model_DataStore class attributes and methods
BPMN2Model_DataStore_capacity: Property = Property(name="capacity", type=IntegerType)
BPMN2Model_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=BooleanType)
BPMN2Model_DataStore_name: Property = Property(name="name", type=StringType)
BPMN2Model_DataStore.attributes={BPMN2Model_DataStore_name, BPMN2Model_DataStore_capacity, BPMN2Model_DataStore_isUnlimited}

# BPMN2Model_ConversationAssociation class attributes and methods

# BPMN2Model_DataStoreReference class attributes and methods

# BPMN2Model_Definitions class attributes and methods
BPMN2Model_Definitions_exporter: Property = Property(name="exporter", type=StringType)
BPMN2Model_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
BPMN2Model_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
BPMN2Model_Definitions_name: Property = Property(name="name", type=StringType)
BPMN2Model_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
BPMN2Model_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
BPMN2Model_Definitions.attributes={BPMN2Model_Definitions_targetNamespace, BPMN2Model_Definitions_exporter, BPMN2Model_Definitions_exporterVersion, BPMN2Model_Definitions_expressionLanguage, BPMN2Model_Definitions_name, BPMN2Model_Definitions_typeLanguage}

# BPMN2Model_Documentation class attributes and methods
BPMN2Model_Documentation_mixed: Property = Property(name="mixed", type=StringType)
BPMN2Model_Documentation_text: Property = Property(name="text", type=StringType)
BPMN2Model_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
BPMN2Model_Documentation.attributes={BPMN2Model_Documentation_text, BPMN2Model_Documentation_textFormat, BPMN2Model_Documentation_mixed}

# BPMN2Model_EndEvent class attributes and methods

# BPMN2Model_EndPoint class attributes and methods

# BPMN2Model_Error class attributes and methods
BPMN2Model_Error_errorCode: Property = Property(name="errorCode", type=StringType)
BPMN2Model_Error_name: Property = Property(name="name", type=StringType)
BPMN2Model_Error.attributes={BPMN2Model_Error_errorCode, BPMN2Model_Error_name}

# BPMN2Model_ErrorEventDefinition class attributes and methods

# BPMN2Model_Escalation class attributes and methods
BPMN2Model_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
BPMN2Model_Escalation_name: Property = Property(name="name", type=StringType)
BPMN2Model_Escalation.attributes={BPMN2Model_Escalation_escalationCode, BPMN2Model_Escalation_name}

# BPMN2Model_EscalationEventDefinition class attributes and methods

# BPMN2Model_Event class attributes and methods

# BPMN2Model_EventBasedGateway class attributes and methods
BPMN2Model_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
BPMN2Model_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=BooleanType)
BPMN2Model_EventBasedGateway.attributes={BPMN2Model_EventBasedGateway_instantiate, BPMN2Model_EventBasedGateway_eventGatewayType}

# BPMN2Model_ExclusiveGateway class attributes and methods

# BPMN2Model_Expression class attributes and methods

# BPMN2Model_Extension class attributes and methods
BPMN2Model_Extension_mustUnderstand: Property = Property(name="mustUnderstand", type=BooleanType)
BPMN2Model_Extension_xsdDefinition: Property = Property(name="xsdDefinition", type=StringType)
BPMN2Model_Extension.attributes={BPMN2Model_Extension_mustUnderstand, BPMN2Model_Extension_xsdDefinition}

# BPMN2Model_ExtensionAttributeValue class attributes and methods
BPMN2Model_ExtensionAttributeValue_value: Property = Property(name="value", type=StringType)
BPMN2Model_ExtensionAttributeValue.attributes={BPMN2Model_ExtensionAttributeValue_value}

# BPMN2Model_FlowNode class attributes and methods

# BPMN2Model_FormalExpression class attributes and methods
BPMN2Model_FormalExpression_mixed: Property = Property(name="mixed", type=StringType)
BPMN2Model_FormalExpression_body: Property = Property(name="body", type=StringType)
BPMN2Model_FormalExpression_language: Property = Property(name="language", type=StringType)
BPMN2Model_FormalExpression.attributes={BPMN2Model_FormalExpression_mixed, BPMN2Model_FormalExpression_language, BPMN2Model_FormalExpression_body}

# BPMN2Model_Gateway class attributes and methods
BPMN2Model_Gateway_gatewayDirection: Property = Property(name="gatewayDirection", type=StringType)
BPMN2Model_Gateway.attributes={BPMN2Model_Gateway_gatewayDirection}

# BPMN2Model_GlobalBusinessRuleTask class attributes and methods
BPMN2Model_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_GlobalBusinessRuleTask.attributes={BPMN2Model_GlobalBusinessRuleTask_implementation}

# BPMN2Model_GlobalChoreographyTask class attributes and methods

# BPMN2Model_GlobalConversation class attributes and methods

# BPMN2Model_GlobalManualTask class attributes and methods

# BPMN2Model_GlobalScriptTask class attributes and methods
BPMN2Model_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
BPMN2Model_GlobalScriptTask_scriptLanguage: Property = Property(name="scriptLanguage", type=StringType)
BPMN2Model_GlobalScriptTask.attributes={BPMN2Model_GlobalScriptTask_script, BPMN2Model_GlobalScriptTask_scriptLanguage}

# BPMN2Model_GlobalTask class attributes and methods

# BPMN2Model_GlobalUserTask class attributes and methods
BPMN2Model_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_GlobalUserTask.attributes={BPMN2Model_GlobalUserTask_implementation}

# BPMN2Model_Group class attributes and methods

# BPMN2Model_HumanPerformer class attributes and methods

# BPMN2Model_Performer class attributes and methods

# BPMN2Model_ResourceRole class attributes and methods
BPMN2Model_ResourceRole_name: Property = Property(name="name", type=StringType)
BPMN2Model_ResourceRole.attributes={BPMN2Model_ResourceRole_name}

# BPMN2Model_ImplicitThrowEvent class attributes and methods

# BPMN2Model_Import class attributes and methods
BPMN2Model_Import_importType: Property = Property(name="importType", type=StringType)
BPMN2Model_Import_location: Property = Property(name="location", type=StringType)
BPMN2Model_Import_namespace: Property = Property(name="namespace", type=StringType)
BPMN2Model_Import.attributes={BPMN2Model_Import_importType, BPMN2Model_Import_namespace, BPMN2Model_Import_location}

# BPMN2Model_InclusiveGateway class attributes and methods

# BPMN2Model_InputSet class attributes and methods
BPMN2Model_InputSet_name: Property = Property(name="name", type=StringType)
BPMN2Model_InputSet.attributes={BPMN2Model_InputSet_name}

# BPMN2Model_IntermediateCatchEvent class attributes and methods

# BPMN2Model_IntermediateThrowEvent class attributes and methods

# BPMN2Model_InputOutputBinding class attributes and methods

# BPMN2Model_InputOutputSpecification class attributes and methods

# BPMN2Model_ItemDefinition class attributes and methods
BPMN2Model_ItemDefinition_isCollection: Property = Property(name="isCollection", type=BooleanType)
BPMN2Model_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
BPMN2Model_ItemDefinition.attributes={BPMN2Model_ItemDefinition_isCollection, BPMN2Model_ItemDefinition_itemKind}

# BPMN2Model_Lane class attributes and methods
BPMN2Model_Lane_name: Property = Property(name="name", type=StringType)
BPMN2Model_Lane.attributes={BPMN2Model_Lane_name}

# BPMN2Model_LaneSet class attributes and methods
BPMN2Model_LaneSet_name: Property = Property(name="name", type=StringType)
BPMN2Model_LaneSet.attributes={BPMN2Model_LaneSet_name}

# BPMN2Model_LinkEventDefinition class attributes and methods
BPMN2Model_LinkEventDefinition_name: Property = Property(name="name", type=StringType)
BPMN2Model_LinkEventDefinition.attributes={BPMN2Model_LinkEventDefinition_name}

# BPMN2Model_LoopCharacteristics class attributes and methods

# BPMN2Model_ManualTask class attributes and methods

# BPMN2Model_Interface class attributes and methods
BPMN2Model_Interface_name: Property = Property(name="name", type=StringType)
BPMN2Model_Interface.attributes={BPMN2Model_Interface_name}

# BPMN2Model_Message class attributes and methods
BPMN2Model_Message_name: Property = Property(name="name", type=StringType)
BPMN2Model_Message.attributes={BPMN2Model_Message_name}

# BPMN2Model_MessageEventDefinition class attributes and methods

# BPMN2Model_MessageFlow class attributes and methods
BPMN2Model_MessageFlow_name: Property = Property(name="name", type=StringType)
BPMN2Model_MessageFlow.attributes={BPMN2Model_MessageFlow_name}

# BPMN2Model_MessageFlowAssociation class attributes and methods

# BPMN2Model_Monitoring class attributes and methods

# BPMN2Model_MultiInstanceLoopCharacteristics class attributes and methods
BPMN2Model_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
BPMN2Model_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=BooleanType)
BPMN2Model_MultiInstanceLoopCharacteristics.attributes={BPMN2Model_MultiInstanceLoopCharacteristics_behavior, BPMN2Model_MultiInstanceLoopCharacteristics_isSequential}

# BPMN2Model_Operation class attributes and methods
BPMN2Model_Operation_name: Property = Property(name="name", type=StringType)
BPMN2Model_Operation.attributes={BPMN2Model_Operation_name}

# BPMN2Model_OutputSet class attributes and methods
BPMN2Model_OutputSet_name: Property = Property(name="name", type=StringType)
BPMN2Model_OutputSet.attributes={BPMN2Model_OutputSet_name}

# BPMN2Model_ParallelGateway class attributes and methods

# BPMN2Model_Participant class attributes and methods
BPMN2Model_Participant_name: Property = Property(name="name", type=StringType)
BPMN2Model_Participant.attributes={BPMN2Model_Participant_name}

# BPMN2Model_ParticipantAssociation class attributes and methods

# BPMN2Model_ParticipantMultiplicity class attributes and methods
BPMN2Model_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=IntegerType)
BPMN2Model_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=IntegerType)
BPMN2Model_ParticipantMultiplicity.attributes={BPMN2Model_ParticipantMultiplicity_maximum, BPMN2Model_ParticipantMultiplicity_minimum}

# BPMN2Model_PartnerEntity class attributes and methods
BPMN2Model_PartnerEntity_name: Property = Property(name="name", type=StringType)
BPMN2Model_PartnerEntity.attributes={BPMN2Model_PartnerEntity_name}

# BPMN2Model_PartnerRole class attributes and methods
BPMN2Model_PartnerRole_name: Property = Property(name="name", type=StringType)
BPMN2Model_PartnerRole.attributes={BPMN2Model_PartnerRole_name}

# BPMN2Model_PotentialOwner class attributes and methods

# BPMN2Model_Process class attributes and methods
BPMN2Model_Process_isClosed: Property = Property(name="isClosed", type=BooleanType)
BPMN2Model_Process_isExecutable: Property = Property(name="isExecutable", type=BooleanType)
BPMN2Model_Process_processType: Property = Property(name="processType", type=StringType)
BPMN2Model_Process.attributes={BPMN2Model_Process_isExecutable, BPMN2Model_Process_processType, BPMN2Model_Process_isClosed}

# BPMN2Model_Property class attributes and methods
BPMN2Model_Property_name: Property = Property(name="name", type=StringType)
BPMN2Model_Property.attributes={BPMN2Model_Property_name}

# BPMN2Model_ReceiveTask class attributes and methods
BPMN2Model_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_ReceiveTask_instantiate: Property = Property(name="instantiate", type=BooleanType)
BPMN2Model_ReceiveTask.attributes={BPMN2Model_ReceiveTask_instantiate, BPMN2Model_ReceiveTask_implementation}

# BPMN2Model_Relationship class attributes and methods
BPMN2Model_Relationship_direction: Property = Property(name="direction", type=StringType)
BPMN2Model_Relationship_type: Property = Property(name="type", type=StringType)
BPMN2Model_Relationship.attributes={BPMN2Model_Relationship_type, BPMN2Model_Relationship_direction}

# BPMN2Model_Rendering class attributes and methods

# BPMN2Model_Resource class attributes and methods
BPMN2Model_Resource_name: Property = Property(name="name", type=StringType)
BPMN2Model_Resource.attributes={BPMN2Model_Resource_name}

# BPMN2Model_ResourceAssignmentExpression class attributes and methods

# BPMN2Model_ResourceParameterBinding class attributes and methods

# BPMN2Model_EObject class attributes and methods

# BPMN2Model_ScriptTask class attributes and methods
BPMN2Model_ScriptTask_script: Property = Property(name="script", type=StringType)
BPMN2Model_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
BPMN2Model_ScriptTask.attributes={BPMN2Model_ScriptTask_script, BPMN2Model_ScriptTask_scriptFormat}

# BPMN2Model_SendTask class attributes and methods
BPMN2Model_SendTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_SendTask.attributes={BPMN2Model_SendTask_implementation}

# BPMN2Model_SequenceFlow class attributes and methods
BPMN2Model_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=BooleanType)
BPMN2Model_SequenceFlow.attributes={BPMN2Model_SequenceFlow_isImmediate}

# BPMN2Model_ServiceTask class attributes and methods
BPMN2Model_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_ServiceTask.attributes={BPMN2Model_ServiceTask_implementation}

# BPMN2Model_Signal class attributes and methods
BPMN2Model_Signal_name: Property = Property(name="name", type=StringType)
BPMN2Model_Signal.attributes={BPMN2Model_Signal_name}

# BPMN2Model_SignalEventDefinition class attributes and methods

# BPMN2Model_StandardLoopCharacteristics class attributes and methods
BPMN2Model_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=BooleanType)
BPMN2Model_StandardLoopCharacteristics.attributes={BPMN2Model_StandardLoopCharacteristics_testBefore}

# BPMN2Model_StartEvent class attributes and methods
BPMN2Model_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=BooleanType)
BPMN2Model_StartEvent.attributes={BPMN2Model_StartEvent_isInterrupting}

# BPMN2Model_ResourceParameter class attributes and methods
BPMN2Model_ResourceParameter_isRequired: Property = Property(name="isRequired", type=BooleanType)
BPMN2Model_ResourceParameter_name: Property = Property(name="name", type=StringType)
BPMN2Model_ResourceParameter.attributes={BPMN2Model_ResourceParameter_name, BPMN2Model_ResourceParameter_isRequired}

# BPMN2Model_SubChoreography class attributes and methods

# BPMN2Model_SubConversation class attributes and methods

# BPMN2Model_SubProcess class attributes and methods
BPMN2Model_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=BooleanType)
BPMN2Model_SubProcess.attributes={BPMN2Model_SubProcess_triggeredByEvent}

# BPMN2Model_Task class attributes and methods

# BPMN2Model_TerminateEventDefinition class attributes and methods

# BPMN2Model_TextAnnotation class attributes and methods
BPMN2Model_TextAnnotation_text: Property = Property(name="text", type=StringType)
BPMN2Model_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
BPMN2Model_TextAnnotation.attributes={BPMN2Model_TextAnnotation_text, BPMN2Model_TextAnnotation_textFormat}

# BPMN2Model_ThrowEvent class attributes and methods

# BPMN2Model_TimerEventDefinition class attributes and methods

# BPMN2Model_Transaction class attributes and methods
BPMN2Model_Transaction_protocol: Property = Property(name="protocol", type=StringType)
BPMN2Model_Transaction_method: Property = Property(name="method", type=StringType)
BPMN2Model_Transaction.attributes={BPMN2Model_Transaction_method, BPMN2Model_Transaction_protocol}

# BPMN2Model_UserTask class attributes and methods
BPMN2Model_UserTask_implementation: Property = Property(name="implementation", type=StringType)
BPMN2Model_UserTask.attributes={BPMN2Model_UserTask_implementation}

# FlowNode class attributes and methods

# SubProcess class attributes and methods

# BaseElement class attributes and methods

# Artifact class attributes and methods

# BPMN2Model_ExtensionDefinition class attributes and methods
BPMN2Model_ExtensionDefinition_name: Property = Property(name="name", type=StringType)
BPMN2Model_ExtensionDefinition.attributes={BPMN2Model_ExtensionDefinition_name}

# CatchEvent class attributes and methods

# Task class attributes and methods

# Activity class attributes and methods

# ChoreographyActivity class attributes and methods

# ConversationNode class attributes and methods

# RootElement class attributes and methods

# EventDefinition class attributes and methods

# Event class attributes and methods

# Collaboration class attributes and methods

# FlowElementsContainer class attributes and methods

# Gateway class attributes and methods

# BPMN2Model_InteractionNode class attributes and methods

# InteractionNode class attributes and methods

# BPMN2Model_ItemAwareElement class attributes and methods

# ItemAwareElement class attributes and methods

# DataAssociation class attributes and methods

# FlowElement class attributes and methods

# ThrowEvent class attributes and methods

# BPMN2Model_ExtensionAttributeDefinition class attributes and methods
BPMN2Model_ExtensionAttributeDefinition_name: Property = Property(name="name", type=StringType)
BPMN2Model_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
BPMN2Model_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=BooleanType)
BPMN2Model_ExtensionAttributeDefinition.attributes={BPMN2Model_ExtensionAttributeDefinition_type, BPMN2Model_ExtensionAttributeDefinition_isReference, BPMN2Model_ExtensionAttributeDefinition_name}

# BPMN2Model_FlowElementsContainer class attributes and methods

# Expression class attributes and methods

# GlobalTask class attributes and methods

# Choreography class attributes and methods

# CallableElement class attributes and methods

# Performer class attributes and methods

# LoopCharacteristics class attributes and methods

# ResourceRole class attributes and methods

# HumanPerformer class attributes and methods

# BPMN2Model_BPMNBase class attributes and methods

# EObject class attributes and methods

# Relationships
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="BPMN2Model_EStringToStringMapEntry3", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot2", type=BPMN2Model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity4: BinaryAssociation = BinaryAssociation(
    name="activity4",
    ends={
        Property(name="BPMN2Model_Activity", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot5", type=BPMN2Model_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adHocSubProcess6: BinaryAssociation = BinaryAssociation(
    name="adHocSubProcess6",
    ends={
        Property(name="BPMN2Model_AdHocSubProcess", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot7", type=BPMN2Model_AdHocSubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElement8: BinaryAssociation = BinaryAssociation(
    name="flowElement8",
    ends={
        Property(name="BPMN2Model_FlowElement", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot9", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifact10: BinaryAssociation = BinaryAssociation(
    name="artifact10",
    ends={
        Property(name="BPMN2Model_Artifact", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot11", type=BPMN2Model_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment12: BinaryAssociation = BinaryAssociation(
    name="assignment12",
    ends={
        Property(name="BPMN2Model_Assignment", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot13", type=BPMN2Model_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association14: BinaryAssociation = BinaryAssociation(
    name="association14",
    ends={
        Property(name="BPMN2Model_Association", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot15", type=BPMN2Model_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing16: BinaryAssociation = BinaryAssociation(
    name="auditing16",
    ends={
        Property(name="BPMN2Model_Auditing", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot17", type=BPMN2Model_Auditing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElement18: BinaryAssociation = BinaryAssociation(
    name="baseElement18",
    ends={
        Property(name="BPMN2Model_BaseElement", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot19", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElementWithMixedContent20: BinaryAssociation = BinaryAssociation(
    name="baseElementWithMixedContent20",
    ends={
        Property(name="BPMN2Model_BaseElement22", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot21", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundaryEvent23: BinaryAssociation = BinaryAssociation(
    name="boundaryEvent23",
    ends={
        Property(name="BPMN2Model_BoundaryEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot24", type=BPMN2Model_BoundaryEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessRuleTask25: BinaryAssociation = BinaryAssociation(
    name="businessRuleTask25",
    ends={
        Property(name="BPMN2Model_BusinessRuleTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot26", type=BPMN2Model_BusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callableElement27: BinaryAssociation = BinaryAssociation(
    name="callableElement27",
    ends={
        Property(name="BPMN2Model_CallableElement", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot28", type=BPMN2Model_CallableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callActivity29: BinaryAssociation = BinaryAssociation(
    name="callActivity29",
    ends={
        Property(name="BPMN2Model_CallActivity", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot30", type=BPMN2Model_CallActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callChoreography31: BinaryAssociation = BinaryAssociation(
    name="callChoreography31",
    ends={
        Property(name="BPMN2Model_CallChoreography", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot32", type=BPMN2Model_CallChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callConversation33: BinaryAssociation = BinaryAssociation(
    name="callConversation33",
    ends={
        Property(name="BPMN2Model_CallConversation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot34", type=BPMN2Model_CallConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="BPMN2Model_EStringToStringMapEntry", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot", type=BPMN2Model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelEventDefinition37: BinaryAssociation = BinaryAssociation(
    name="cancelEventDefinition37",
    ends={
        Property(name="BPMN2Model_CancelEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot38", type=BPMN2Model_CancelEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinition39: BinaryAssociation = BinaryAssociation(
    name="eventDefinition39",
    ends={
        Property(name="BPMN2Model_EventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot40", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElement41: BinaryAssociation = BinaryAssociation(
    name="rootElement41",
    ends={
        Property(name="BPMN2Model_RootElement", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot42", type=BPMN2Model_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchEvent43: BinaryAssociation = BinaryAssociation(
    name="catchEvent43",
    ends={
        Property(name="BPMN2Model_CatchEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot44", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category45: BinaryAssociation = BinaryAssociation(
    name="category45",
    ends={
        Property(name="BPMN2Model_Category", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot46", type=BPMN2Model_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValue47: BinaryAssociation = BinaryAssociation(
    name="categoryValue47",
    ends={
        Property(name="BPMN2Model_CategoryValue", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot48", type=BPMN2Model_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreography49: BinaryAssociation = BinaryAssociation(
    name="choreography49",
    ends={
        Property(name="BPMN2Model_Choreography", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot50", type=BPMN2Model_Choreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration51: BinaryAssociation = BinaryAssociation(
    name="collaboration51",
    ends={
        Property(name="BPMN2Model_Collaboration", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot52", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyActivity53: BinaryAssociation = BinaryAssociation(
    name="choreographyActivity53",
    ends={
        Property(name="BPMN2Model_ChoreographyActivity", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot54", type=BPMN2Model_ChoreographyActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyTask55: BinaryAssociation = BinaryAssociation(
    name="choreographyTask55",
    ends={
        Property(name="BPMN2Model_ChoreographyTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot56", type=BPMN2Model_ChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compensateEventDefinition57: BinaryAssociation = BinaryAssociation(
    name="compensateEventDefinition57",
    ends={
        Property(name="BPMN2Model_CompensateEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot58", type=BPMN2Model_CompensateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexBehaviorDefinition59: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition59",
    ends={
        Property(name="BPMN2Model_ComplexBehaviorDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot60", type=BPMN2Model_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexGateway61: BinaryAssociation = BinaryAssociation(
    name="complexGateway61",
    ends={
        Property(name="BPMN2Model_ComplexGateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot62", type=BPMN2Model_ComplexGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalEventDefinition63: BinaryAssociation = BinaryAssociation(
    name="conditionalEventDefinition63",
    ends={
        Property(name="BPMN2Model_ConditionalEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot64", type=BPMN2Model_ConditionalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversation65: BinaryAssociation = BinaryAssociation(
    name="conversation65",
    ends={
        Property(name="BPMN2Model_Conversation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot66", type=BPMN2Model_Conversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNode35: BinaryAssociation = BinaryAssociation(
    name="conversationNode35",
    ends={
        Property(name="BPMN2Model_ConversationNode", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot36", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociation67: BinaryAssociation = BinaryAssociation(
    name="conversationAssociation67",
    ends={
        Property(name="BPMN2Model_ConversationAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot68", type=BPMN2Model_ConversationAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationLink69: BinaryAssociation = BinaryAssociation(
    name="conversationLink69",
    ends={
        Property(name="BPMN2Model_ConversationLink", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot70", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationKey71: BinaryAssociation = BinaryAssociation(
    name="correlationKey71",
    ends={
        Property(name="BPMN2Model_CorrelationKey", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot72", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationProperty73: BinaryAssociation = BinaryAssociation(
    name="correlationProperty73",
    ends={
        Property(name="BPMN2Model_CorrelationProperty", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot74", type=BPMN2Model_CorrelationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyBinding75: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding75",
    ends={
        Property(name="BPMN2Model_CorrelationPropertyBinding", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot76", type=BPMN2Model_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRetrievalExpression77: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression77",
    ends={
        Property(name="BPMN2Model_CorrelationPropertyRetrievalExpression", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot78", type=BPMN2Model_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscription79: BinaryAssociation = BinaryAssociation(
    name="correlationSubscription79",
    ends={
        Property(name="BPMN2Model_CorrelationSubscription", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot80", type=BPMN2Model_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataAssociation81: BinaryAssociation = BinaryAssociation(
    name="dataAssociation81",
    ends={
        Property(name="BPMN2Model_DataAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot82", type=BPMN2Model_DataAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInput83: BinaryAssociation = BinaryAssociation(
    name="dataInput83",
    ends={
        Property(name="BPMN2Model_DataInput", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot84", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation85: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation85",
    ends={
        Property(name="BPMN2Model_DataInputAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot86", type=BPMN2Model_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObject87: BinaryAssociation = BinaryAssociation(
    name="dataObject87",
    ends={
        Property(name="BPMN2Model_DataObject", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot88", type=BPMN2Model_DataObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjectReference89: BinaryAssociation = BinaryAssociation(
    name="dataObjectReference89",
    ends={
        Property(name="BPMN2Model_DataObjectReference", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot90", type=BPMN2Model_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutput91: BinaryAssociation = BinaryAssociation(
    name="dataOutput91",
    ends={
        Property(name="BPMN2Model_DataOutput", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot92", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociation93: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation93",
    ends={
        Property(name="BPMN2Model_DataOutputAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot94", type=BPMN2Model_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataState95: BinaryAssociation = BinaryAssociation(
    name="dataState95",
    ends={
        Property(name="BPMN2Model_DataState", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot96", type=BPMN2Model_DataState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStoreReference99: BinaryAssociation = BinaryAssociation(
    name="dataStoreReference99",
    ends={
        Property(name="BPMN2Model_DataStoreReference", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot100", type=BPMN2Model_DataStoreReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions101: BinaryAssociation = BinaryAssociation(
    name="definitions101",
    ends={
        Property(name="BPMN2Model_Definitions", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot102", type=BPMN2Model_Definitions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation103: BinaryAssociation = BinaryAssociation(
    name="documentation103",
    ends={
        Property(name="BPMN2Model_Documentation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot104", type=BPMN2Model_Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endEvent105: BinaryAssociation = BinaryAssociation(
    name="endEvent105",
    ends={
        Property(name="BPMN2Model_EndEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot106", type=BPMN2Model_EndEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoint107: BinaryAssociation = BinaryAssociation(
    name="endPoint107",
    ends={
        Property(name="BPMN2Model_EndPoint", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot108", type=BPMN2Model_EndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error109: BinaryAssociation = BinaryAssociation(
    name="error109",
    ends={
        Property(name="BPMN2Model_Error", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot110", type=BPMN2Model_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
errorEventDefinition111: BinaryAssociation = BinaryAssociation(
    name="errorEventDefinition111",
    ends={
        Property(name="BPMN2Model_ErrorEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot112", type=BPMN2Model_ErrorEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalation113: BinaryAssociation = BinaryAssociation(
    name="escalation113",
    ends={
        Property(name="BPMN2Model_Escalation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot114", type=BPMN2Model_Escalation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalationEventDefinition115: BinaryAssociation = BinaryAssociation(
    name="escalationEventDefinition115",
    ends={
        Property(name="BPMN2Model_EscalationEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot116", type=BPMN2Model_EscalationEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event117: BinaryAssociation = BinaryAssociation(
    name="event117",
    ends={
        Property(name="BPMN2Model_Event", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot118", type=BPMN2Model_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventBasedGateway119: BinaryAssociation = BinaryAssociation(
    name="eventBasedGateway119",
    ends={
        Property(name="BPMN2Model_EventBasedGateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot120", type=BPMN2Model_EventBasedGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclusiveGateway121: BinaryAssociation = BinaryAssociation(
    name="exclusiveGateway121",
    ends={
        Property(name="BPMN2Model_ExclusiveGateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot122", type=BPMN2Model_ExclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="BPMN2Model_Expression", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot124", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension125: BinaryAssociation = BinaryAssociation(
    name="extension125",
    ends={
        Property(name="BPMN2Model_Extension", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot126", type=BPMN2Model_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStore97: BinaryAssociation = BinaryAssociation(
    name="dataStore97",
    ends={
        Property(name="BPMN2Model_DataStore", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot98", type=BPMN2Model_DataStore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionElements127: BinaryAssociation = BinaryAssociation(
    name="extensionElements127",
    ends={
        Property(name="BPMN2Model_ExtensionAttributeValue", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot128", type=BPMN2Model_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowNode129: BinaryAssociation = BinaryAssociation(
    name="flowNode129",
    ends={
        Property(name="BPMN2Model_FlowNode", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot130", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalExpression131: BinaryAssociation = BinaryAssociation(
    name="formalExpression131",
    ends={
        Property(name="BPMN2Model_FormalExpression", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot132", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gateway133: BinaryAssociation = BinaryAssociation(
    name="gateway133",
    ends={
        Property(name="BPMN2Model_Gateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot134", type=BPMN2Model_Gateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalBusinessRuleTask135: BinaryAssociation = BinaryAssociation(
    name="globalBusinessRuleTask135",
    ends={
        Property(name="BPMN2Model_GlobalBusinessRuleTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot136", type=BPMN2Model_GlobalBusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalChoreographyTask137: BinaryAssociation = BinaryAssociation(
    name="globalChoreographyTask137",
    ends={
        Property(name="BPMN2Model_GlobalChoreographyTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot138", type=BPMN2Model_GlobalChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalConversation139: BinaryAssociation = BinaryAssociation(
    name="globalConversation139",
    ends={
        Property(name="BPMN2Model_GlobalConversation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot140", type=BPMN2Model_GlobalConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalManualTask141: BinaryAssociation = BinaryAssociation(
    name="globalManualTask141",
    ends={
        Property(name="BPMN2Model_GlobalManualTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot142", type=BPMN2Model_GlobalManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalScriptTask143: BinaryAssociation = BinaryAssociation(
    name="globalScriptTask143",
    ends={
        Property(name="BPMN2Model_GlobalScriptTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot144", type=BPMN2Model_GlobalScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalTask145: BinaryAssociation = BinaryAssociation(
    name="globalTask145",
    ends={
        Property(name="BPMN2Model_GlobalTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot146", type=BPMN2Model_GlobalTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalUserTask147: BinaryAssociation = BinaryAssociation(
    name="globalUserTask147",
    ends={
        Property(name="BPMN2Model_GlobalUserTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot148", type=BPMN2Model_GlobalUserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group149: BinaryAssociation = BinaryAssociation(
    name="group149",
    ends={
        Property(name="BPMN2Model_Group", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot150", type=BPMN2Model_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
humanPerformer151: BinaryAssociation = BinaryAssociation(
    name="humanPerformer151",
    ends={
        Property(name="BPMN2Model_HumanPerformer", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot152", type=BPMN2Model_HumanPerformer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performer153: BinaryAssociation = BinaryAssociation(
    name="performer153",
    ends={
        Property(name="BPMN2Model_Performer", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot154", type=BPMN2Model_Performer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRole155: BinaryAssociation = BinaryAssociation(
    name="resourceRole155",
    ends={
        Property(name="BPMN2Model_ResourceRole", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot156", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitThrowEvent157: BinaryAssociation = BinaryAssociation(
    name="implicitThrowEvent157",
    ends={
        Property(name="BPMN2Model_ImplicitThrowEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot158", type=BPMN2Model_ImplicitThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import159: BinaryAssociation = BinaryAssociation(
    name="import159",
    ends={
        Property(name="BPMN2Model_Import", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot160", type=BPMN2Model_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inclusiveGateway161: BinaryAssociation = BinaryAssociation(
    name="inclusiveGateway161",
    ends={
        Property(name="BPMN2Model_InclusiveGateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot162", type=BPMN2Model_InclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet163: BinaryAssociation = BinaryAssociation(
    name="inputSet163",
    ends={
        Property(name="BPMN2Model_InputSet", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot164", type=BPMN2Model_InputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface165: BinaryAssociation = BinaryAssociation(
    name="interface165",
    ends={
        Property(name="BPMN2Model_Interface", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot166", type=BPMN2Model_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateCatchEvent167: BinaryAssociation = BinaryAssociation(
    name="intermediateCatchEvent167",
    ends={
        Property(name="BPMN2Model_IntermediateCatchEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot168", type=BPMN2Model_IntermediateCatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateThrowEvent169: BinaryAssociation = BinaryAssociation(
    name="intermediateThrowEvent169",
    ends={
        Property(name="BPMN2Model_IntermediateThrowEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot170", type=BPMN2Model_IntermediateThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioBinding171: BinaryAssociation = BinaryAssociation(
    name="ioBinding171",
    ends={
        Property(name="BPMN2Model_InputOutputBinding", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot172", type=BPMN2Model_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification173: BinaryAssociation = BinaryAssociation(
    name="ioSpecification173",
    ends={
        Property(name="BPMN2Model_InputOutputSpecification", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot174", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemDefinition175: BinaryAssociation = BinaryAssociation(
    name="itemDefinition175",
    ends={
        Property(name="BPMN2Model_ItemDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot176", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lane177: BinaryAssociation = BinaryAssociation(
    name="lane177",
    ends={
        Property(name="BPMN2Model_Lane", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot178", type=BPMN2Model_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laneSet179: BinaryAssociation = BinaryAssociation(
    name="laneSet179",
    ends={
        Property(name="BPMN2Model_LaneSet", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot180", type=BPMN2Model_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkEventDefinition181: BinaryAssociation = BinaryAssociation(
    name="linkEventDefinition181",
    ends={
        Property(name="BPMN2Model_LinkEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot182", type=BPMN2Model_LinkEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCharacteristics183: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics183",
    ends={
        Property(name="BPMN2Model_LoopCharacteristics", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot184", type=BPMN2Model_LoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manualTask185: BinaryAssociation = BinaryAssociation(
    name="manualTask185",
    ends={
        Property(name="BPMN2Model_ManualTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot186", type=BPMN2Model_ManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message187: BinaryAssociation = BinaryAssociation(
    name="message187",
    ends={
        Property(name="BPMN2Model_Message", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot188", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageEventDefinition189: BinaryAssociation = BinaryAssociation(
    name="messageEventDefinition189",
    ends={
        Property(name="BPMN2Model_MessageEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot190", type=BPMN2Model_MessageEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlow191: BinaryAssociation = BinaryAssociation(
    name="messageFlow191",
    ends={
        Property(name="BPMN2Model_MessageFlow", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot192", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociation193: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociation193",
    ends={
        Property(name="BPMN2Model_MessageFlowAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot194", type=BPMN2Model_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monitoring195: BinaryAssociation = BinaryAssociation(
    name="monitoring195",
    ends={
        Property(name="BPMN2Model_Monitoring", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot196", type=BPMN2Model_Monitoring, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiInstanceLoopCharacteristics197: BinaryAssociation = BinaryAssociation(
    name="multiInstanceLoopCharacteristics197",
    ends={
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot198", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation199: BinaryAssociation = BinaryAssociation(
    name="operation199",
    ends={
        Property(name="BPMN2Model_Operation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot200", type=BPMN2Model_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSet201: BinaryAssociation = BinaryAssociation(
    name="outputSet201",
    ends={
        Property(name="BPMN2Model_OutputSet", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot202", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallelGateway203: BinaryAssociation = BinaryAssociation(
    name="parallelGateway203",
    ends={
        Property(name="BPMN2Model_ParallelGateway", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot204", type=BPMN2Model_ParallelGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant205: BinaryAssociation = BinaryAssociation(
    name="participant205",
    ends={
        Property(name="BPMN2Model_Participant", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot206", type=BPMN2Model_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantAssociation207: BinaryAssociation = BinaryAssociation(
    name="participantAssociation207",
    ends={
        Property(name="BPMN2Model_ParticipantAssociation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot208", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerEntity211: BinaryAssociation = BinaryAssociation(
    name="partnerEntity211",
    ends={
        Property(name="BPMN2Model_PartnerEntity", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot212", type=BPMN2Model_PartnerEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerRole213: BinaryAssociation = BinaryAssociation(
    name="partnerRole213",
    ends={
        Property(name="BPMN2Model_PartnerRole", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot214", type=BPMN2Model_PartnerRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
potentialOwner215: BinaryAssociation = BinaryAssociation(
    name="potentialOwner215",
    ends={
        Property(name="BPMN2Model_PotentialOwner", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot216", type=BPMN2Model_PotentialOwner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process217: BinaryAssociation = BinaryAssociation(
    name="process217",
    ends={
        Property(name="BPMN2Model_Process", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot218", type=BPMN2Model_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property219: BinaryAssociation = BinaryAssociation(
    name="property219",
    ends={
        Property(name="BPMN2Model_Property", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot220", type=BPMN2Model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiveTask221: BinaryAssociation = BinaryAssociation(
    name="receiveTask221",
    ends={
        Property(name="BPMN2Model_ReceiveTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot222", type=BPMN2Model_ReceiveTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship223: BinaryAssociation = BinaryAssociation(
    name="relationship223",
    ends={
        Property(name="BPMN2Model_Relationship", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot224", type=BPMN2Model_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rendering225: BinaryAssociation = BinaryAssociation(
    name="rendering225",
    ends={
        Property(name="BPMN2Model_Rendering", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot226", type=BPMN2Model_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource227: BinaryAssociation = BinaryAssociation(
    name="resource227",
    ends={
        Property(name="BPMN2Model_Resource", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot228", type=BPMN2Model_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression229: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression229",
    ends={
        Property(name="BPMN2Model_ResourceAssignmentExpression", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot230", type=BPMN2Model_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantMultiplicity209: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity209",
    ends={
        Property(name="BPMN2Model_ParticipantMultiplicity", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot210", type=BPMN2Model_ParticipantMultiplicity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameter231: BinaryAssociation = BinaryAssociation(
    name="resourceParameter231",
    ends={
        Property(name="BPMN2Model_ResourceParameter", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot232", type=BPMN2Model_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameterBinding233: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBinding233",
    ends={
        Property(name="BPMN2Model_ResourceParameterBinding", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot234", type=BPMN2Model_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script235: BinaryAssociation = BinaryAssociation(
    name="script235",
    ends={
        Property(name="BPMN2Model_EObject", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot236", type=BPMN2Model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptTask237: BinaryAssociation = BinaryAssociation(
    name="scriptTask237",
    ends={
        Property(name="BPMN2Model_ScriptTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot238", type=BPMN2Model_ScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sendTask239: BinaryAssociation = BinaryAssociation(
    name="sendTask239",
    ends={
        Property(name="BPMN2Model_SendTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot240", type=BPMN2Model_SendTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceFlow241: BinaryAssociation = BinaryAssociation(
    name="sequenceFlow241",
    ends={
        Property(name="BPMN2Model_SequenceFlow", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot242", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceTask243: BinaryAssociation = BinaryAssociation(
    name="serviceTask243",
    ends={
        Property(name="BPMN2Model_ServiceTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot244", type=BPMN2Model_ServiceTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal245: BinaryAssociation = BinaryAssociation(
    name="signal245",
    ends={
        Property(name="BPMN2Model_Signal", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot246", type=BPMN2Model_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalEventDefinition247: BinaryAssociation = BinaryAssociation(
    name="signalEventDefinition247",
    ends={
        Property(name="BPMN2Model_SignalEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot248", type=BPMN2Model_SignalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
standardLoopCharacteristics249: BinaryAssociation = BinaryAssociation(
    name="standardLoopCharacteristics249",
    ends={
        Property(name="BPMN2Model_StandardLoopCharacteristics", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot250", type=BPMN2Model_StandardLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startEvent251: BinaryAssociation = BinaryAssociation(
    name="startEvent251",
    ends={
        Property(name="BPMN2Model_StartEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot252", type=BPMN2Model_StartEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subChoreography253: BinaryAssociation = BinaryAssociation(
    name="subChoreography253",
    ends={
        Property(name="BPMN2Model_SubChoreography", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot254", type=BPMN2Model_SubChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subConversation255: BinaryAssociation = BinaryAssociation(
    name="subConversation255",
    ends={
        Property(name="BPMN2Model_SubConversation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot256", type=BPMN2Model_SubConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess257: BinaryAssociation = BinaryAssociation(
    name="subProcess257",
    ends={
        Property(name="BPMN2Model_SubProcess", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot258", type=BPMN2Model_SubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task259: BinaryAssociation = BinaryAssociation(
    name="task259",
    ends={
        Property(name="BPMN2Model_Task", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot260", type=BPMN2Model_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminateEventDefinition261: BinaryAssociation = BinaryAssociation(
    name="terminateEventDefinition261",
    ends={
        Property(name="BPMN2Model_TerminateEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot262", type=BPMN2Model_TerminateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text263: BinaryAssociation = BinaryAssociation(
    name="text263",
    ends={
        Property(name="BPMN2Model_EObject265", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot264", type=BPMN2Model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textAnnotation266: BinaryAssociation = BinaryAssociation(
    name="textAnnotation266",
    ends={
        Property(name="BPMN2Model_TextAnnotation", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot267", type=BPMN2Model_TextAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throwEvent268: BinaryAssociation = BinaryAssociation(
    name="throwEvent268",
    ends={
        Property(name="BPMN2Model_ThrowEvent", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot269", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerEventDefinition270: BinaryAssociation = BinaryAssociation(
    name="timerEventDefinition270",
    ends={
        Property(name="BPMN2Model_TimerEventDefinition", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot271", type=BPMN2Model_TimerEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transaction272: BinaryAssociation = BinaryAssociation(
    name="transaction272",
    ends={
        Property(name="BPMN2Model_Transaction", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot273", type=BPMN2Model_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userTask274: BinaryAssociation = BinaryAssociation(
    name="userTask274",
    ends={
        Property(name="BPMN2Model_UserTask", type=BPMN2Model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DocumentRoot275", type=BPMN2Model_UserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification276: BinaryAssociation = BinaryAssociation(
    name="ioSpecification276",
    ends={
        Property(name="BPMN2Model_InputOutputSpecification278", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity277", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundaryEventRefs279: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs279",
    ends={
        Property(name="BoundaryEvent", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="attachedToRef", type=BPMN2Model_BoundaryEvent, multiplicity=Multiplicity(0, 9999))
    }
)
properties280: BinaryAssociation = BinaryAssociation(
    name="properties280",
    ends={
        Property(name="BPMN2Model_Property282", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity281", type=BPMN2Model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociations283: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations283",
    ends={
        Property(name="BPMN2Model_DataInputAssociation285", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity284", type=BPMN2Model_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociations286: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations286",
    ends={
        Property(name="BPMN2Model_DataOutputAssociation288", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity287", type=BPMN2Model_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources289: BinaryAssociation = BinaryAssociation(
    name="resources289",
    ends={
        Property(name="BPMN2Model_ResourceRole291", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity290", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCharacteristics292: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics292",
    ends={
        Property(name="BPMN2Model_LoopCharacteristics294", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity293", type=BPMN2Model_LoopCharacteristics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default295: BinaryAssociation = BinaryAssociation(
    name="default295",
    ends={
        Property(name="BPMN2Model_SequenceFlow297", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Activity296", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
completionCondition298: BinaryAssociation = BinaryAssociation(
    name="completionCondition298",
    ends={
        Property(name="BPMN2Model_Expression300", type=BPMN2Model_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_AdHocSubProcess299", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from301: BinaryAssociation = BinaryAssociation(
    name="from301",
    ends={
        Property(name="BPMN2Model_Expression303", type=BPMN2Model_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Assignment302", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to304: BinaryAssociation = BinaryAssociation(
    name="to304",
    ends={
        Property(name="BPMN2Model_Expression306", type=BPMN2Model_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Assignment305", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceRef307: BinaryAssociation = BinaryAssociation(
    name="sourceRef307",
    ends={
        Property(name="BPMN2Model_BaseElement309", type=BPMN2Model_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Association308", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
targetRef310: BinaryAssociation = BinaryAssociation(
    name="targetRef310",
    ends={
        Property(name="BPMN2Model_BaseElement312", type=BPMN2Model_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Association311", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
extensionValues313: BinaryAssociation = BinaryAssociation(
    name="extensionValues313",
    ends={
        Property(name="BPMN2Model_ExtensionAttributeValue315", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_BaseElement314", type=BPMN2Model_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation316: BinaryAssociation = BinaryAssociation(
    name="documentation316",
    ends={
        Property(name="BPMN2Model_Documentation318", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_BaseElement317", type=BPMN2Model_Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefinitions319: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions319",
    ends={
        Property(name="BPMN2Model_ExtensionDefinition", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_BaseElement320", type=BPMN2Model_ExtensionDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
attachedToRef321: BinaryAssociation = BinaryAssociation(
    name="attachedToRef321",
    ends={
        Property(name="Activity", type=BPMN2Model_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="boundaryEventRefs", type=BPMN2Model_Activity, multiplicity=Multiplicity(1, 1))
    }
)
calledElementRef322: BinaryAssociation = BinaryAssociation(
    name="calledElementRef322",
    ends={
        Property(name="BPMN2Model_CallableElement324", type=BPMN2Model_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallActivity323", type=BPMN2Model_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations325: BinaryAssociation = BinaryAssociation(
    name="participantAssociations325",
    ends={
        Property(name="BPMN2Model_ParticipantAssociation327", type=BPMN2Model_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallChoreography326", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledChoreographyRef328: BinaryAssociation = BinaryAssociation(
    name="calledChoreographyRef328",
    ends={
        Property(name="BPMN2Model_Choreography330", type=BPMN2Model_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallChoreography329", type=BPMN2Model_Choreography, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations331: BinaryAssociation = BinaryAssociation(
    name="participantAssociations331",
    ends={
        Property(name="BPMN2Model_ParticipantAssociation333", type=BPMN2Model_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallConversation332", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledCollaborationRef334: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef334",
    ends={
        Property(name="BPMN2Model_Collaboration336", type=BPMN2Model_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallConversation335", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
supportedInterfaceRefs337: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs337",
    ends={
        Property(name="BPMN2Model_Interface339", type=BPMN2Model_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallableElement338", type=BPMN2Model_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ioSpecification340: BinaryAssociation = BinaryAssociation(
    name="ioSpecification340",
    ends={
        Property(name="BPMN2Model_InputOutputSpecification342", type=BPMN2Model_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallableElement341", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ioBinding343: BinaryAssociation = BinaryAssociation(
    name="ioBinding343",
    ends={
        Property(name="BPMN2Model_InputOutputBinding345", type=BPMN2Model_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CallableElement344", type=BPMN2Model_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs346: BinaryAssociation = BinaryAssociation(
    name="dataOutputs346",
    ends={
        Property(name="BPMN2Model_DataOutput348", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CatchEvent347", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociation349: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation349",
    ends={
        Property(name="BPMN2Model_DataOutputAssociation351", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CatchEvent350", type=BPMN2Model_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSet352: BinaryAssociation = BinaryAssociation(
    name="outputSet352",
    ends={
        Property(name="BPMN2Model_OutputSet354", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CatchEvent353", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitions355: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions355",
    ends={
        Property(name="BPMN2Model_EventDefinition357", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CatchEvent356", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitionRefs358: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs358",
    ends={
        Property(name="BPMN2Model_EventDefinition360", type=BPMN2Model_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CatchEvent359", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
categoryValue361: BinaryAssociation = BinaryAssociation(
    name="categoryValue361",
    ends={
        Property(name="BPMN2Model_CategoryValue363", type=BPMN2Model_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Category362", type=BPMN2Model_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categorizedFlowElements364: BinaryAssociation = BinaryAssociation(
    name="categorizedFlowElements364",
    ends={
        Property(name="BPMN2Model_FlowElement366", type=BPMN2Model_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CategoryValue365", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(0, 9999))
    }
)
participantRefs367: BinaryAssociation = BinaryAssociation(
    name="participantRefs367",
    ends={
        Property(name="BPMN2Model_Participant369", type=BPMN2Model_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ChoreographyActivity368", type=BPMN2Model_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
correlationKeys370: BinaryAssociation = BinaryAssociation(
    name="correlationKeys370",
    ends={
        Property(name="BPMN2Model_CorrelationKey372", type=BPMN2Model_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ChoreographyActivity371", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initiatingParticipantRef373: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef373",
    ends={
        Property(name="BPMN2Model_Participant375", type=BPMN2Model_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ChoreographyActivity374", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1))
    }
)
messageFlowRef376: BinaryAssociation = BinaryAssociation(
    name="messageFlowRef376",
    ends={
        Property(name="BPMN2Model_MessageFlow378", type=BPMN2Model_ChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ChoreographyTask377", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 2))
    }
)
participants379: BinaryAssociation = BinaryAssociation(
    name="participants379",
    ends={
        Property(name="BPMN2Model_Participant381", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration380", type=BPMN2Model_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlows382: BinaryAssociation = BinaryAssociation(
    name="messageFlows382",
    ends={
        Property(name="BPMN2Model_MessageFlow384", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration383", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts385: BinaryAssociation = BinaryAssociation(
    name="artifacts385",
    ends={
        Property(name="BPMN2Model_Artifact387", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration386", type=BPMN2Model_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversations388: BinaryAssociation = BinaryAssociation(
    name="conversations388",
    ends={
        Property(name="BPMN2Model_ConversationNode390", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration389", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociations391: BinaryAssociation = BinaryAssociation(
    name="conversationAssociations391",
    ends={
        Property(name="BPMN2Model_ConversationAssociation393", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration392", type=BPMN2Model_ConversationAssociation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
participantAssociations394: BinaryAssociation = BinaryAssociation(
    name="participantAssociations394",
    ends={
        Property(name="BPMN2Model_ParticipantAssociation396", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration395", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociations397: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations397",
    ends={
        Property(name="BPMN2Model_MessageFlowAssociation399", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration398", type=BPMN2Model_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationKeys400: BinaryAssociation = BinaryAssociation(
    name="correlationKeys400",
    ends={
        Property(name="BPMN2Model_CorrelationKey402", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration401", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyRef403: BinaryAssociation = BinaryAssociation(
    name="choreographyRef403",
    ends={
        Property(name="BPMN2Model_Choreography405", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration404", type=BPMN2Model_Choreography, multiplicity=Multiplicity(0, 9999))
    }
)
conversationLinks406: BinaryAssociation = BinaryAssociation(
    name="conversationLinks406",
    ends={
        Property(name="BPMN2Model_ConversationLink408", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Collaboration407", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityRef409: BinaryAssociation = BinaryAssociation(
    name="activityRef409",
    ends={
        Property(name="BPMN2Model_Activity411", type=BPMN2Model_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CompensateEventDefinition410", type=BPMN2Model_Activity, multiplicity=Multiplicity(0, 1))
    }
)
condition412: BinaryAssociation = BinaryAssociation(
    name="condition412",
    ends={
        Property(name="BPMN2Model_FormalExpression414", type=BPMN2Model_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ComplexBehaviorDefinition413", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event415: BinaryAssociation = BinaryAssociation(
    name="event415",
    ends={
        Property(name="BPMN2Model_ImplicitThrowEvent417", type=BPMN2Model_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ComplexBehaviorDefinition416", type=BPMN2Model_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activationCondition418: BinaryAssociation = BinaryAssociation(
    name="activationCondition418",
    ends={
        Property(name="BPMN2Model_Expression420", type=BPMN2Model_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ComplexGateway419", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default421: BinaryAssociation = BinaryAssociation(
    name="default421",
    ends={
        Property(name="BPMN2Model_SequenceFlow423", type=BPMN2Model_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ComplexGateway422", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
condition424: BinaryAssociation = BinaryAssociation(
    name="condition424",
    ends={
        Property(name="BPMN2Model_Expression426", type=BPMN2Model_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConditionalEventDefinition425", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
innerConversationNodeRef427: BinaryAssociation = BinaryAssociation(
    name="innerConversationNodeRef427",
    ends={
        Property(name="BPMN2Model_ConversationNode429", type=BPMN2Model_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationAssociation428", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
outerConversationNodeRef430: BinaryAssociation = BinaryAssociation(
    name="outerConversationNodeRef430",
    ends={
        Property(name="BPMN2Model_ConversationNode432", type=BPMN2Model_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationAssociation431", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef433: BinaryAssociation = BinaryAssociation(
    name="sourceRef433",
    ends={
        Property(name="BPMN2Model_InteractionNode", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationLink434", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef435: BinaryAssociation = BinaryAssociation(
    name="targetRef435",
    ends={
        Property(name="BPMN2Model_InteractionNode437", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationLink436", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
participantRefs438: BinaryAssociation = BinaryAssociation(
    name="participantRefs438",
    ends={
        Property(name="BPMN2Model_Participant440", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationNode439", type=BPMN2Model_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
messageFlowRefs441: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs441",
    ends={
        Property(name="BPMN2Model_MessageFlow443", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationNode442", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(0, 9999))
    }
)
correlationKeys444: BinaryAssociation = BinaryAssociation(
    name="correlationKeys444",
    ends={
        Property(name="BPMN2Model_CorrelationKey446", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ConversationNode445", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRef447: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef447",
    ends={
        Property(name="BPMN2Model_CorrelationProperty449", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationKey448", type=BPMN2Model_CorrelationProperty, multiplicity=Multiplicity(0, 9999))
    }
)
correlationPropertyRetrievalExpression450: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression450",
    ends={
        Property(name="BPMN2Model_CorrelationPropertyRetrievalExpression452", type=BPMN2Model_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationProperty451", type=BPMN2Model_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type453: BinaryAssociation = BinaryAssociation(
    name="type453",
    ends={
        Property(name="BPMN2Model_ItemDefinition455", type=BPMN2Model_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationProperty454", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataPath456: BinaryAssociation = BinaryAssociation(
    name="dataPath456",
    ends={
        Property(name="BPMN2Model_FormalExpression458", type=BPMN2Model_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationPropertyBinding457", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
correlationPropertyRef459: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef459",
    ends={
        Property(name="BPMN2Model_CorrelationProperty461", type=BPMN2Model_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationPropertyBinding460", type=BPMN2Model_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
messagePath462: BinaryAssociation = BinaryAssociation(
    name="messagePath462",
    ends={
        Property(name="BPMN2Model_FormalExpression464", type=BPMN2Model_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationPropertyRetrievalExpression463", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageRef465: BinaryAssociation = BinaryAssociation(
    name="messageRef465",
    ends={
        Property(name="BPMN2Model_Message467", type=BPMN2Model_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationPropertyRetrievalExpression466", type=BPMN2Model_Message, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding468: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding468",
    ends={
        Property(name="BPMN2Model_CorrelationPropertyBinding470", type=BPMN2Model_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationSubscription469", type=BPMN2Model_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationKeyRef471: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef471",
    ends={
        Property(name="BPMN2Model_CorrelationKey473", type=BPMN2Model_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_CorrelationSubscription472", type=BPMN2Model_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef474: BinaryAssociation = BinaryAssociation(
    name="sourceRef474",
    ends={
        Property(name="BPMN2Model_ItemAwareElement", type=BPMN2Model_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataAssociation475", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(0, 9999))
    }
)
targetRef476: BinaryAssociation = BinaryAssociation(
    name="targetRef476",
    ends={
        Property(name="BPMN2Model_ItemAwareElement478", type=BPMN2Model_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataAssociation477", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
transformation479: BinaryAssociation = BinaryAssociation(
    name="transformation479",
    ends={
        Property(name="BPMN2Model_FormalExpression481", type=BPMN2Model_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataAssociation480", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment482: BinaryAssociation = BinaryAssociation(
    name="assignment482",
    ends={
        Property(name="BPMN2Model_Assignment484", type=BPMN2Model_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataAssociation483", type=BPMN2Model_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSetWithOptional485: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional485",
    ends={
        Property(name="InputSet", type=BPMN2Model_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=BPMN2Model_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetWithWhileExecuting486: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting486",
    ends={
        Property(name="InputSet487", type=BPMN2Model_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=BPMN2Model_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs488: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs488",
    ends={
        Property(name="InputSet489", type=BPMN2Model_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
dataObjectRef490: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef490",
    ends={
        Property(name="BPMN2Model_DataObject492", type=BPMN2Model_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataObjectReference491", type=BPMN2Model_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
outputSetWithOptional493: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional493",
    ends={
        Property(name="OutputSet", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalOutputRefs", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithWhileExecuting494: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting494",
    ends={
        Property(name="OutputSet495", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingOutputRefs", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs496: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs496",
    ends={
        Property(name="OutputSet497", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
dataStoreRef498: BinaryAssociation = BinaryAssociation(
    name="dataStoreRef498",
    ends={
        Property(name="BPMN2Model_DataStore500", type=BPMN2Model_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_DataStoreReference499", type=BPMN2Model_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
imports501: BinaryAssociation = BinaryAssociation(
    name="imports501",
    ends={
        Property(name="BPMN2Model_Import503", type=BPMN2Model_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Definitions502", type=BPMN2Model_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions504: BinaryAssociation = BinaryAssociation(
    name="extensions504",
    ends={
        Property(name="BPMN2Model_Extension506", type=BPMN2Model_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Definitions505", type=BPMN2Model_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElements507: BinaryAssociation = BinaryAssociation(
    name="rootElements507",
    ends={
        Property(name="BPMN2Model_RootElement509", type=BPMN2Model_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Definitions508", type=BPMN2Model_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships510: BinaryAssociation = BinaryAssociation(
    name="relationships510",
    ends={
        Property(name="BPMN2Model_Relationship512", type=BPMN2Model_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Definitions511", type=BPMN2Model_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structureRef513: BinaryAssociation = BinaryAssociation(
    name="structureRef513",
    ends={
        Property(name="BPMN2Model_ItemDefinition515", type=BPMN2Model_Error, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Error514", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
errorRef516: BinaryAssociation = BinaryAssociation(
    name="errorRef516",
    ends={
        Property(name="BPMN2Model_Error518", type=BPMN2Model_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ErrorEventDefinition517", type=BPMN2Model_Error, multiplicity=Multiplicity(0, 1))
    }
)
structureRef519: BinaryAssociation = BinaryAssociation(
    name="structureRef519",
    ends={
        Property(name="BPMN2Model_ItemDefinition521", type=BPMN2Model_Escalation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Escalation520", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
escalationRef522: BinaryAssociation = BinaryAssociation(
    name="escalationRef522",
    ends={
        Property(name="BPMN2Model_Escalation524", type=BPMN2Model_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_EscalationEventDefinition523", type=BPMN2Model_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
properties525: BinaryAssociation = BinaryAssociation(
    name="properties525",
    ends={
        Property(name="BPMN2Model_Property527", type=BPMN2Model_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Event526", type=BPMN2Model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default528: BinaryAssociation = BinaryAssociation(
    name="default528",
    ends={
        Property(name="BPMN2Model_SequenceFlow530", type=BPMN2Model_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ExclusiveGateway529", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
definition531: BinaryAssociation = BinaryAssociation(
    name="definition531",
    ends={
        Property(name="BPMN2Model_ExtensionDefinition533", type=BPMN2Model_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Extension532", type=BPMN2Model_ExtensionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extensionDefinition534: BinaryAssociation = BinaryAssociation(
    name="extensionDefinition534",
    ends={
        Property(name="ExtensionDefinition", type=BPMN2Model_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionAttributeDefinitions", type=BPMN2Model_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
valueRef535: BinaryAssociation = BinaryAssociation(
    name="valueRef535",
    ends={
        Property(name="BPMN2Model_EObject537", type=BPMN2Model_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ExtensionAttributeValue536", type=BPMN2Model_EObject, multiplicity=Multiplicity(0, 1))
    }
)
extensionAttributeDefinition538: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition538",
    ends={
        Property(name="BPMN2Model_ExtensionAttributeDefinition", type=BPMN2Model_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ExtensionAttributeValue539", type=BPMN2Model_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
extensionAttributeDefinitions540: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions540",
    ends={
        Property(name="ExtensionAttributeDefinition", type=BPMN2Model_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionDefinition", type=BPMN2Model_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing541: BinaryAssociation = BinaryAssociation(
    name="auditing541",
    ends={
        Property(name="BPMN2Model_Auditing543", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FlowElement542", type=BPMN2Model_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring544: BinaryAssociation = BinaryAssociation(
    name="monitoring544",
    ends={
        Property(name="BPMN2Model_Monitoring546", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FlowElement545", type=BPMN2Model_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
categoryValueRef547: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef547",
    ends={
        Property(name="BPMN2Model_CategoryValue549", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FlowElement548", type=BPMN2Model_CategoryValue, multiplicity=Multiplicity(0, 9999))
    }
)
laneSets550: BinaryAssociation = BinaryAssociation(
    name="laneSets550",
    ends={
        Property(name="BPMN2Model_LaneSet551", type=BPMN2Model_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FlowElementsContainer", type=BPMN2Model_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElements552: BinaryAssociation = BinaryAssociation(
    name="flowElements552",
    ends={
        Property(name="BPMN2Model_FlowElement554", type=BPMN2Model_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FlowElementsContainer553", type=BPMN2Model_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming555: BinaryAssociation = BinaryAssociation(
    name="incoming555",
    ends={
        Property(name="SequenceFlow", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
lanes556: BinaryAssociation = BinaryAssociation(
    name="lanes556",
    ends={
        Property(name="Lane", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="flowNodeRefs", type=BPMN2Model_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing557: BinaryAssociation = BinaryAssociation(
    name="outgoing557",
    ends={
        Property(name="SequenceFlow558", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
evaluatesToTypeRef559: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef559",
    ends={
        Property(name="BPMN2Model_ItemDefinition561", type=BPMN2Model_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_FormalExpression560", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
initiatingParticipantRef562: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef562",
    ends={
        Property(name="BPMN2Model_Participant564", type=BPMN2Model_GlobalChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_GlobalChoreographyTask563", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1))
    }
)
resources565: BinaryAssociation = BinaryAssociation(
    name="resources565",
    ends={
        Property(name="BPMN2Model_ResourceRole567", type=BPMN2Model_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_GlobalTask566", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renderings568: BinaryAssociation = BinaryAssociation(
    name="renderings568",
    ends={
        Property(name="BPMN2Model_Rendering570", type=BPMN2Model_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_GlobalUserTask569", type=BPMN2Model_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValueRef571: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef571",
    ends={
        Property(name="BPMN2Model_CategoryValue573", type=BPMN2Model_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Group572", type=BPMN2Model_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
default574: BinaryAssociation = BinaryAssociation(
    name="default574",
    ends={
        Property(name="BPMN2Model_SequenceFlow576", type=BPMN2Model_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InclusiveGateway575", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef577: BinaryAssociation = BinaryAssociation(
    name="inputDataRef577",
    ends={
        Property(name="BPMN2Model_InputSet579", type=BPMN2Model_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputBinding578", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef580: BinaryAssociation = BinaryAssociation(
    name="operationRef580",
    ends={
        Property(name="BPMN2Model_Operation582", type=BPMN2Model_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputBinding581", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef583: BinaryAssociation = BinaryAssociation(
    name="outputDataRef583",
    ends={
        Property(name="BPMN2Model_OutputSet585", type=BPMN2Model_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputBinding584", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
dataInputs586: BinaryAssociation = BinaryAssociation(
    name="dataInputs586",
    ends={
        Property(name="BPMN2Model_DataInput588", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputSpecification587", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs589: BinaryAssociation = BinaryAssociation(
    name="dataOutputs589",
    ends={
        Property(name="BPMN2Model_DataOutput591", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputSpecification590", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSets592: BinaryAssociation = BinaryAssociation(
    name="inputSets592",
    ends={
        Property(name="BPMN2Model_InputSet594", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputSpecification593", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputSets595: BinaryAssociation = BinaryAssociation(
    name="outputSets595",
    ends={
        Property(name="BPMN2Model_OutputSet597", type=BPMN2Model_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InputOutputSpecification596", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataInputRefs598: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs598",
    ends={
        Property(name="DataInput", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInputRefs599: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs599",
    ends={
        Property(name="DataInput600", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingInputRefs601: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs601",
    ends={
        Property(name="DataInput602", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs603: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs603",
    ends={
        Property(name="OutputSet605", type=BPMN2Model_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs604", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConversationLinks606: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks606",
    ends={
        Property(name="BPMN2Model_ConversationLink608", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InteractionNode607", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingConversationLinks609: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks609",
    ends={
        Property(name="BPMN2Model_ConversationLink611", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_InteractionNode610", type=BPMN2Model_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
operations612: BinaryAssociation = BinaryAssociation(
    name="operations612",
    ends={
        Property(name="BPMN2Model_Operation614", type=BPMN2Model_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Interface613", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implementationRef615: BinaryAssociation = BinaryAssociation(
    name="implementationRef615",
    ends={
        Property(name="BPMN2Model_EObject617", type=BPMN2Model_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Interface616", type=BPMN2Model_EObject, multiplicity=Multiplicity(0, 1))
    }
)
dataState618: BinaryAssociation = BinaryAssociation(
    name="dataState618",
    ends={
        Property(name="BPMN2Model_DataState620", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ItemAwareElement619", type=BPMN2Model_DataState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemSubjectRef621: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef621",
    ends={
        Property(name="BPMN2Model_ItemDefinition623", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ItemAwareElement622", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
import624: BinaryAssociation = BinaryAssociation(
    name="import624",
    ends={
        Property(name="BPMN2Model_Import626", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ItemDefinition625", type=BPMN2Model_Import, multiplicity=Multiplicity(0, 1))
    }
)
structureRef627: BinaryAssociation = BinaryAssociation(
    name="structureRef627",
    ends={
        Property(name="BPMN2Model_EObject629", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ItemDefinition628", type=BPMN2Model_EObject, multiplicity=Multiplicity(1, 1))
    }
)
partitionElement630: BinaryAssociation = BinaryAssociation(
    name="partitionElement630",
    ends={
        Property(name="BPMN2Model_BaseElement632", type=BPMN2Model_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Lane631", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flowNodeRefs633: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs633",
    ends={
        Property(name="FlowNode", type=BPMN2Model_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(0, 9999))
    }
)
childLaneSet634: BinaryAssociation = BinaryAssociation(
    name="childLaneSet634",
    ends={
        Property(name="BPMN2Model_LaneSet636", type=BPMN2Model_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Lane635", type=BPMN2Model_LaneSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partitionElementRef637: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef637",
    ends={
        Property(name="BPMN2Model_BaseElement639", type=BPMN2Model_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Lane638", type=BPMN2Model_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
lanes640: BinaryAssociation = BinaryAssociation(
    name="lanes640",
    ends={
        Property(name="BPMN2Model_Lane642", type=BPMN2Model_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_LaneSet641", type=BPMN2Model_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source644: BinaryAssociation = BinaryAssociation(
    name="source644",
    ends={
        Property(name="LinkEventDefinition", type=BPMN2Model_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=BPMN2Model_LinkEventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
target646: BinaryAssociation = BinaryAssociation(
    name="target646",
    ends={
        Property(name="LinkEventDefinition647", type=BPMN2Model_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=BPMN2Model_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
itemRef648: BinaryAssociation = BinaryAssociation(
    name="itemRef648",
    ends={
        Property(name="BPMN2Model_ItemDefinition650", type=BPMN2Model_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Message649", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operationRef651: BinaryAssociation = BinaryAssociation(
    name="operationRef651",
    ends={
        Property(name="BPMN2Model_Operation653", type=BPMN2Model_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageEventDefinition652", type=BPMN2Model_Operation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef654: BinaryAssociation = BinaryAssociation(
    name="messageRef654",
    ends={
        Property(name="BPMN2Model_Message656", type=BPMN2Model_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageEventDefinition655", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 1))
    }
)
messageRef657: BinaryAssociation = BinaryAssociation(
    name="messageRef657",
    ends={
        Property(name="BPMN2Model_Message659", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageFlow658", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef660: BinaryAssociation = BinaryAssociation(
    name="sourceRef660",
    ends={
        Property(name="BPMN2Model_InteractionNode662", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageFlow661", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef663: BinaryAssociation = BinaryAssociation(
    name="targetRef663",
    ends={
        Property(name="BPMN2Model_InteractionNode665", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageFlow664", type=BPMN2Model_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef666: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef666",
    ends={
        Property(name="BPMN2Model_MessageFlow668", type=BPMN2Model_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageFlowAssociation667", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef669: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef669",
    ends={
        Property(name="BPMN2Model_MessageFlow671", type=BPMN2Model_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MessageFlowAssociation670", type=BPMN2Model_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
loopCardinality672: BinaryAssociation = BinaryAssociation(
    name="loopCardinality672",
    ends={
        Property(name="BPMN2Model_Expression674", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics673", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopDataInputRef675: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef675",
    ends={
        Property(name="BPMN2Model_ItemAwareElement677", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics676", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef678: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef678",
    ends={
        Property(name="BPMN2Model_ItemAwareElement680", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics679", type=BPMN2Model_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
inputDataItem681: BinaryAssociation = BinaryAssociation(
    name="inputDataItem681",
    ends={
        Property(name="BPMN2Model_DataInput683", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics682", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputDataItem684: BinaryAssociation = BinaryAssociation(
    name="outputDataItem684",
    ends={
        Property(name="BPMN2Model_DataOutput686", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics685", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complexBehaviorDefinition687: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition687",
    ends={
        Property(name="BPMN2Model_ComplexBehaviorDefinition689", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics688", type=BPMN2Model_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completionCondition690: BinaryAssociation = BinaryAssociation(
    name="completionCondition690",
    ends={
        Property(name="BPMN2Model_Expression692", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics691", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noneBehaviorEventRef693: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef693",
    ends={
        Property(name="BPMN2Model_EventDefinition695", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics694", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oneBehaviorEventRef696: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef696",
    ends={
        Property(name="BPMN2Model_EventDefinition698", type=BPMN2Model_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_MultiInstanceLoopCharacteristics697", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef699: BinaryAssociation = BinaryAssociation(
    name="inMessageRef699",
    ends={
        Property(name="BPMN2Model_Message701", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Operation700", type=BPMN2Model_Message, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef702: BinaryAssociation = BinaryAssociation(
    name="outMessageRef702",
    ends={
        Property(name="BPMN2Model_Message704", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Operation703", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 1))
    }
)
errorRefs705: BinaryAssociation = BinaryAssociation(
    name="errorRefs705",
    ends={
        Property(name="BPMN2Model_Error707", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Operation706", type=BPMN2Model_Error, multiplicity=Multiplicity(0, 9999))
    }
)
implementationRef708: BinaryAssociation = BinaryAssociation(
    name="implementationRef708",
    ends={
        Property(name="BPMN2Model_EObject710", type=BPMN2Model_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Operation709", type=BPMN2Model_EObject, multiplicity=Multiplicity(0, 1))
    }
)
dataOutputRefs711: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs711",
    ends={
        Property(name="DataOutput", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
optionalOutputRefs712: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs712",
    ends={
        Property(name="DataOutput713", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithOptional", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingOutputRefs714: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs714",
    ends={
        Property(name="DataOutput715", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithWhileExecuting", type=BPMN2Model_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs716: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs716",
    ends={
        Property(name="InputSet718", type=BPMN2Model_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs717", type=BPMN2Model_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
interfaceRefs719: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs719",
    ends={
        Property(name="BPMN2Model_Interface721", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Participant720", type=BPMN2Model_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
endPointRefs722: BinaryAssociation = BinaryAssociation(
    name="endPointRefs722",
    ends={
        Property(name="BPMN2Model_EndPoint724", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Participant723", type=BPMN2Model_EndPoint, multiplicity=Multiplicity(0, 9999))
    }
)
participantMultiplicity725: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity725",
    ends={
        Property(name="BPMN2Model_ParticipantMultiplicity727", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Participant726", type=BPMN2Model_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processRef728: BinaryAssociation = BinaryAssociation(
    name="processRef728",
    ends={
        Property(name="BPMN2Model_Process730", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Participant729", type=BPMN2Model_Process, multiplicity=Multiplicity(0, 1))
    }
)
innerParticipantRef731: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef731",
    ends={
        Property(name="BPMN2Model_Participant733", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ParticipantAssociation732", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef734: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef734",
    ends={
        Property(name="BPMN2Model_Participant736", type=BPMN2Model_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ParticipantAssociation735", type=BPMN2Model_Participant, multiplicity=Multiplicity(1, 1))
    }
)
participantRef737: BinaryAssociation = BinaryAssociation(
    name="participantRef737",
    ends={
        Property(name="BPMN2Model_Participant739", type=BPMN2Model_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_PartnerEntity738", type=BPMN2Model_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
participantRef740: BinaryAssociation = BinaryAssociation(
    name="participantRef740",
    ends={
        Property(name="BPMN2Model_Participant742", type=BPMN2Model_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_PartnerRole741", type=BPMN2Model_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
auditing743: BinaryAssociation = BinaryAssociation(
    name="auditing743",
    ends={
        Property(name="BPMN2Model_Auditing745", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process744", type=BPMN2Model_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring746: BinaryAssociation = BinaryAssociation(
    name="monitoring746",
    ends={
        Property(name="BPMN2Model_Monitoring748", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process747", type=BPMN2Model_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties749: BinaryAssociation = BinaryAssociation(
    name="properties749",
    ends={
        Property(name="BPMN2Model_Property751", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process750", type=BPMN2Model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts752: BinaryAssociation = BinaryAssociation(
    name="artifacts752",
    ends={
        Property(name="BPMN2Model_Artifact754", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process753", type=BPMN2Model_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources755: BinaryAssociation = BinaryAssociation(
    name="resources755",
    ends={
        Property(name="BPMN2Model_ResourceRole757", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process756", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscriptions758: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions758",
    ends={
        Property(name="BPMN2Model_CorrelationSubscription760", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process759", type=BPMN2Model_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports762: BinaryAssociation = BinaryAssociation(
    name="supports762",
    ends={
        Property(name="BPMN2Model_Process763", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process761", type=BPMN2Model_Process, multiplicity=Multiplicity(0, 9999))
    }
)
definitionalCollaborationRef764: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef764",
    ends={
        Property(name="BPMN2Model_Collaboration766", type=BPMN2Model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Process765", type=BPMN2Model_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
messageRef767: BinaryAssociation = BinaryAssociation(
    name="messageRef767",
    ends={
        Property(name="BPMN2Model_Message769", type=BPMN2Model_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ReceiveTask768", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef770: BinaryAssociation = BinaryAssociation(
    name="operationRef770",
    ends={
        Property(name="BPMN2Model_ReceiveTask771", type=BPMN2Model_Operation, multiplicity=Multiplicity(0, 1)),
        Property(name="BPMN2Model_Operation772", type=BPMN2Model_ReceiveTask, multiplicity=Multiplicity(1, 1))
    }
)
sources773: BinaryAssociation = BinaryAssociation(
    name="sources773",
    ends={
        Property(name="BPMN2Model_EObject775", type=BPMN2Model_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Relationship774", type=BPMN2Model_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
targets776: BinaryAssociation = BinaryAssociation(
    name="targets776",
    ends={
        Property(name="BPMN2Model_EObject778", type=BPMN2Model_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Relationship777", type=BPMN2Model_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
resourceParameters779: BinaryAssociation = BinaryAssociation(
    name="resourceParameters779",
    ends={
        Property(name="BPMN2Model_ResourceParameter781", type=BPMN2Model_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Resource780", type=BPMN2Model_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression782: BinaryAssociation = BinaryAssociation(
    name="expression782",
    ends={
        Property(name="BPMN2Model_Expression784", type=BPMN2Model_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceAssignmentExpression783", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type785: BinaryAssociation = BinaryAssociation(
    name="type785",
    ends={
        Property(name="BPMN2Model_ItemDefinition787", type=BPMN2Model_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceParameter786", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expression788: BinaryAssociation = BinaryAssociation(
    name="expression788",
    ends={
        Property(name="BPMN2Model_Expression790", type=BPMN2Model_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceParameterBinding789", type=BPMN2Model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterRef791: BinaryAssociation = BinaryAssociation(
    name="parameterRef791",
    ends={
        Property(name="BPMN2Model_ResourceParameter793", type=BPMN2Model_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceParameterBinding792", type=BPMN2Model_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
resourceRef794: BinaryAssociation = BinaryAssociation(
    name="resourceRef794",
    ends={
        Property(name="BPMN2Model_Resource796", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceRole795", type=BPMN2Model_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings797: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings797",
    ends={
        Property(name="BPMN2Model_ResourceParameterBinding799", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceRole798", type=BPMN2Model_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression800: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression800",
    ends={
        Property(name="BPMN2Model_ResourceAssignmentExpression802", type=BPMN2Model_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ResourceRole801", type=BPMN2Model_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageRef803: BinaryAssociation = BinaryAssociation(
    name="messageRef803",
    ends={
        Property(name="BPMN2Model_Message805", type=BPMN2Model_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SendTask804", type=BPMN2Model_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef806: BinaryAssociation = BinaryAssociation(
    name="operationRef806",
    ends={
        Property(name="BPMN2Model_Operation808", type=BPMN2Model_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SendTask807", type=BPMN2Model_Operation, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression809: BinaryAssociation = BinaryAssociation(
    name="conditionExpression809",
    ends={
        Property(name="BPMN2Model_Expression811", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SequenceFlow810", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceRef812: BinaryAssociation = BinaryAssociation(
    name="sourceRef812",
    ends={
        Property(name="FlowNode813", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef814: BinaryAssociation = BinaryAssociation(
    name="targetRef814",
    ends={
        Property(name="FlowNode815", type=BPMN2Model_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=BPMN2Model_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
operationRef816: BinaryAssociation = BinaryAssociation(
    name="operationRef816",
    ends={
        Property(name="BPMN2Model_Operation818", type=BPMN2Model_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ServiceTask817", type=BPMN2Model_Operation, multiplicity=Multiplicity(0, 1))
    }
)
structureRef819: BinaryAssociation = BinaryAssociation(
    name="structureRef819",
    ends={
        Property(name="BPMN2Model_ItemDefinition821", type=BPMN2Model_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_Signal820", type=BPMN2Model_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
signalRef822: BinaryAssociation = BinaryAssociation(
    name="signalRef822",
    ends={
        Property(name="BPMN2Model_Signal824", type=BPMN2Model_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SignalEventDefinition823", type=BPMN2Model_Signal, multiplicity=Multiplicity(0, 1))
    }
)
loopCondition825: BinaryAssociation = BinaryAssociation(
    name="loopCondition825",
    ends={
        Property(name="BPMN2Model_Expression827", type=BPMN2Model_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_StandardLoopCharacteristics826", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopMaximum828: BinaryAssociation = BinaryAssociation(
    name="loopMaximum828",
    ends={
        Property(name="BPMN2Model_Expression830", type=BPMN2Model_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_StandardLoopCharacteristics829", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
artifacts831: BinaryAssociation = BinaryAssociation(
    name="artifacts831",
    ends={
        Property(name="BPMN2Model_Artifact833", type=BPMN2Model_SubChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SubChoreography832", type=BPMN2Model_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNodes834: BinaryAssociation = BinaryAssociation(
    name="conversationNodes834",
    ends={
        Property(name="BPMN2Model_ConversationNode836", type=BPMN2Model_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SubConversation835", type=BPMN2Model_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts837: BinaryAssociation = BinaryAssociation(
    name="artifacts837",
    ends={
        Property(name="BPMN2Model_Artifact839", type=BPMN2Model_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_SubProcess838", type=BPMN2Model_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputs840: BinaryAssociation = BinaryAssociation(
    name="dataInputs840",
    ends={
        Property(name="BPMN2Model_DataInput842", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ThrowEvent841", type=BPMN2Model_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation843: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation843",
    ends={
        Property(name="BPMN2Model_DataInputAssociation845", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ThrowEvent844", type=BPMN2Model_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet846: BinaryAssociation = BinaryAssociation(
    name="inputSet846",
    ends={
        Property(name="BPMN2Model_InputSet848", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ThrowEvent847", type=BPMN2Model_InputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitions849: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions849",
    ends={
        Property(name="BPMN2Model_EventDefinition851", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ThrowEvent850", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitionRefs852: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs852",
    ends={
        Property(name="BPMN2Model_EventDefinition854", type=BPMN2Model_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_ThrowEvent853", type=BPMN2Model_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
timeDate855: BinaryAssociation = BinaryAssociation(
    name="timeDate855",
    ends={
        Property(name="BPMN2Model_Expression857", type=BPMN2Model_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_TimerEventDefinition856", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeDuration858: BinaryAssociation = BinaryAssociation(
    name="timeDuration858",
    ends={
        Property(name="BPMN2Model_Expression860", type=BPMN2Model_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_TimerEventDefinition859", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCycle861: BinaryAssociation = BinaryAssociation(
    name="timeCycle861",
    ends={
        Property(name="BPMN2Model_Expression863", type=BPMN2Model_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_TimerEventDefinition862", type=BPMN2Model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
renderings864: BinaryAssociation = BinaryAssociation(
    name="renderings864",
    ends={
        Property(name="BPMN2Model_Rendering866", type=BPMN2Model_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="BPMN2Model_UserTask865", type=BPMN2Model_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_BPMN2Model_DocumentRoot_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_DocumentRoot)
gen_BPMN2Model_Activity_FlowNode = Generalization(general=FlowNode, specific=BPMN2Model_Activity)
gen_BPMN2Model_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=BPMN2Model_AdHocSubProcess)
gen_BPMN2Model_Artifact_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Artifact)
gen_BPMN2Model_Assignment_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Assignment)
gen_BPMN2Model_Association_Artifact = Generalization(general=Artifact, specific=BPMN2Model_Association)
gen_BPMN2Model_Auditing_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Auditing)
gen_BPMN2Model_BaseElement_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_BaseElement)
gen_BPMN2Model_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMN2Model_BoundaryEvent)
gen_BPMN2Model_BusinessRuleTask_Task = Generalization(general=Task, specific=BPMN2Model_BusinessRuleTask)
gen_BPMN2Model_CallActivity_Activity = Generalization(general=Activity, specific=BPMN2Model_CallActivity)
gen_BPMN2Model_CallChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=BPMN2Model_CallChoreography)
gen_BPMN2Model_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMN2Model_CallConversation)
gen_BPMN2Model_CallableElement_RootElement = Generalization(general=RootElement, specific=BPMN2Model_CallableElement)
gen_BPMN2Model_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_CancelEventDefinition)
gen_BPMN2Model_CatchEvent_Event = Generalization(general=Event, specific=BPMN2Model_CatchEvent)
gen_BPMN2Model_Category_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Category)
gen_BPMN2Model_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_CategoryValue)
gen_BPMN2Model_Choreography_Collaboration = Generalization(general=Collaboration, specific=BPMN2Model_Choreography)
gen_BPMN2Model_Choreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMN2Model_Choreography)
gen_BPMN2Model_ChoreographyActivity_FlowNode = Generalization(general=FlowNode, specific=BPMN2Model_ChoreographyActivity)
gen_BPMN2Model_ChoreographyTask_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=BPMN2Model_ChoreographyTask)
gen_BPMN2Model_Collaboration_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Collaboration)
gen_BPMN2Model_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_CompensateEventDefinition)
gen_BPMN2Model_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ComplexBehaviorDefinition)
gen_BPMN2Model_ComplexGateway_Gateway = Generalization(general=Gateway, specific=BPMN2Model_ComplexGateway)
gen_BPMN2Model_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_ConditionalEventDefinition)
gen_BPMN2Model_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMN2Model_Conversation)
gen_BPMN2Model_ConversationAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ConversationAssociation)
gen_BPMN2Model_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ConversationLink)
gen_BPMN2Model_ConversationNode_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ConversationNode)
gen_BPMN2Model_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=BPMN2Model_ConversationNode)
gen_BPMN2Model_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_CorrelationKey)
gen_BPMN2Model_CorrelationProperty_RootElement = Generalization(general=RootElement, specific=BPMN2Model_CorrelationProperty)
gen_BPMN2Model_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_CorrelationPropertyBinding)
gen_BPMN2Model_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_CorrelationPropertyRetrievalExpression)
gen_BPMN2Model_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_CorrelationSubscription)
gen_BPMN2Model_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_DataAssociation)
gen_BPMN2Model_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataInput)
gen_BPMN2Model_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMN2Model_DataInputAssociation)
gen_BPMN2Model_DataObject_FlowElement = Generalization(general=FlowElement, specific=BPMN2Model_DataObject)
gen_BPMN2Model_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataObject)
gen_BPMN2Model_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=BPMN2Model_DataObjectReference)
gen_BPMN2Model_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataObjectReference)
gen_BPMN2Model_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataOutput)
gen_BPMN2Model_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=BPMN2Model_DataOutputAssociation)
gen_BPMN2Model_DataState_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_DataState)
gen_BPMN2Model_DataStore_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataStore)
gen_BPMN2Model_DataStore_RootElement = Generalization(general=RootElement, specific=BPMN2Model_DataStore)
gen_BPMN2Model_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=BPMN2Model_DataStoreReference)
gen_BPMN2Model_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_DataStoreReference)
gen_BPMN2Model_Definitions_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Definitions)
gen_BPMN2Model_Documentation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Documentation)
gen_BPMN2Model_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMN2Model_EndEvent)
gen_BPMN2Model_EndPoint_RootElement = Generalization(general=RootElement, specific=BPMN2Model_EndPoint)
gen_BPMN2Model_Error_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Error)
gen_BPMN2Model_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_ErrorEventDefinition)
gen_BPMN2Model_Escalation_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_Escalation)
gen_BPMN2Model_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_EscalationEventDefinition)
gen_BPMN2Model_Event_FlowNode = Generalization(general=FlowNode, specific=BPMN2Model_Event)
gen_BPMN2Model_Event_InteractionNode = Generalization(general=InteractionNode, specific=BPMN2Model_Event)
gen_BPMN2Model_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=BPMN2Model_EventBasedGateway)
gen_BPMN2Model_EventDefinition_RootElement = Generalization(general=RootElement, specific=BPMN2Model_EventDefinition)
gen_BPMN2Model_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMN2Model_ExclusiveGateway)
gen_BPMN2Model_Extension_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_Extension)
gen_BPMN2Model_ExtensionAttributeDefinition_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ExtensionAttributeDefinition)
gen_BPMN2Model_ExtensionAttributeValue_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ExtensionAttributeValue)
gen_BPMN2Model_ExtensionDefinition_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ExtensionDefinition)
gen_BPMN2Model_FlowElement_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_FlowElement)
gen_BPMN2Model_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_FlowElementsContainer)
gen_BPMN2Model_FlowNode_FlowElement = Generalization(general=FlowElement, specific=BPMN2Model_FlowNode)
gen_BPMN2Model_Expression_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Expression)
gen_BPMN2Model_FormalExpression_Expression = Generalization(general=Expression, specific=BPMN2Model_FormalExpression)
gen_BPMN2Model_Gateway_FlowNode = Generalization(general=FlowNode, specific=BPMN2Model_Gateway)
gen_BPMN2Model_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMN2Model_GlobalBusinessRuleTask)
gen_BPMN2Model_GlobalChoreographyTask_Choreography = Generalization(general=Choreography, specific=BPMN2Model_GlobalChoreographyTask)
gen_BPMN2Model_GlobalConversation_Collaboration = Generalization(general=Collaboration, specific=BPMN2Model_GlobalConversation)
gen_BPMN2Model_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMN2Model_GlobalManualTask)
gen_BPMN2Model_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMN2Model_GlobalScriptTask)
gen_BPMN2Model_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=BPMN2Model_GlobalTask)
gen_BPMN2Model_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=BPMN2Model_GlobalUserTask)
gen_BPMN2Model_Group_Artifact = Generalization(general=Artifact, specific=BPMN2Model_Group)
gen_BPMN2Model_HumanPerformer_Performer = Generalization(general=Performer, specific=BPMN2Model_HumanPerformer)
gen_BPMN2Model_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMN2Model_ImplicitThrowEvent)
gen_BPMN2Model_Import_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_Import)
gen_BPMN2Model_InclusiveGateway_Gateway = Generalization(general=Gateway, specific=BPMN2Model_InclusiveGateway)
gen_BPMN2Model_InputOutputBinding_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_InputOutputBinding)
gen_BPMN2Model_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_InputOutputSpecification)
gen_BPMN2Model_InputSet_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_InputSet)
gen_BPMN2Model_InteractionNode_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_InteractionNode)
gen_BPMN2Model_Interface_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Interface)
gen_BPMN2Model_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMN2Model_IntermediateCatchEvent)
gen_BPMN2Model_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=BPMN2Model_IntermediateThrowEvent)
gen_BPMN2Model_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ItemAwareElement)
gen_BPMN2Model_ItemDefinition_RootElement = Generalization(general=RootElement, specific=BPMN2Model_ItemDefinition)
gen_BPMN2Model_Lane_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Lane)
gen_BPMN2Model_LaneSet_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_LaneSet)
gen_BPMN2Model_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_LinkEventDefinition)
gen_BPMN2Model_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_LoopCharacteristics)
gen_BPMN2Model_ManualTask_Task = Generalization(general=Task, specific=BPMN2Model_ManualTask)
gen_BPMN2Model_Message_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Message)
gen_BPMN2Model_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_MessageEventDefinition)
gen_BPMN2Model_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_MessageFlow)
gen_BPMN2Model_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_MessageFlowAssociation)
gen_BPMN2Model_Monitoring_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Monitoring)
gen_BPMN2Model_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMN2Model_MultiInstanceLoopCharacteristics)
gen_BPMN2Model_Operation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Operation)
gen_BPMN2Model_OutputSet_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_OutputSet)
gen_BPMN2Model_ParallelGateway_Gateway = Generalization(general=Gateway, specific=BPMN2Model_ParallelGateway)
gen_BPMN2Model_Participant_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Participant)
gen_BPMN2Model_Participant_InteractionNode = Generalization(general=InteractionNode, specific=BPMN2Model_Participant)
gen_BPMN2Model_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ParticipantAssociation)
gen_BPMN2Model_ParticipantMultiplicity_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ParticipantMultiplicity)
gen_BPMN2Model_PartnerEntity_RootElement = Generalization(general=RootElement, specific=BPMN2Model_PartnerEntity)
gen_BPMN2Model_PartnerRole_RootElement = Generalization(general=RootElement, specific=BPMN2Model_PartnerRole)
gen_BPMN2Model_Performer_ResourceRole = Generalization(general=ResourceRole, specific=BPMN2Model_Performer)
gen_BPMN2Model_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=BPMN2Model_PotentialOwner)
gen_BPMN2Model_Process_CallableElement = Generalization(general=CallableElement, specific=BPMN2Model_Process)
gen_BPMN2Model_Process_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMN2Model_Process)
gen_BPMN2Model_Property_ItemAwareElement = Generalization(general=ItemAwareElement, specific=BPMN2Model_Property)
gen_BPMN2Model_ReceiveTask_Task = Generalization(general=Task, specific=BPMN2Model_ReceiveTask)
gen_BPMN2Model_Relationship_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Relationship)
gen_BPMN2Model_Rendering_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_Rendering)
gen_BPMN2Model_Resource_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Resource)
gen_BPMN2Model_ResourceAssignmentExpression_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ResourceAssignmentExpression)
gen_BPMN2Model_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ResourceParameter)
gen_BPMN2Model_ResourceParameterBinding_BPMNBase = Generalization(general=BPMNBase, specific=BPMN2Model_ResourceParameterBinding)
gen_BPMN2Model_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_ResourceRole)
gen_BPMN2Model_RootElement_BaseElement = Generalization(general=BaseElement, specific=BPMN2Model_RootElement)
gen_BPMN2Model_ScriptTask_Task = Generalization(general=Task, specific=BPMN2Model_ScriptTask)
gen_BPMN2Model_SendTask_Task = Generalization(general=Task, specific=BPMN2Model_SendTask)
gen_BPMN2Model_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=BPMN2Model_SequenceFlow)
gen_BPMN2Model_ServiceTask_Task = Generalization(general=Task, specific=BPMN2Model_ServiceTask)
gen_BPMN2Model_Signal_RootElement = Generalization(general=RootElement, specific=BPMN2Model_Signal)
gen_BPMN2Model_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_SignalEventDefinition)
gen_BPMN2Model_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=BPMN2Model_StandardLoopCharacteristics)
gen_BPMN2Model_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=BPMN2Model_StartEvent)
gen_BPMN2Model_SubChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=BPMN2Model_SubChoreography)
gen_BPMN2Model_SubChoreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMN2Model_SubChoreography)
gen_BPMN2Model_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=BPMN2Model_SubConversation)
gen_BPMN2Model_SubProcess_Activity = Generalization(general=Activity, specific=BPMN2Model_SubProcess)
gen_BPMN2Model_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=BPMN2Model_SubProcess)
gen_BPMN2Model_Task_Activity = Generalization(general=Activity, specific=BPMN2Model_Task)
gen_BPMN2Model_Task_InteractionNode = Generalization(general=InteractionNode, specific=BPMN2Model_Task)
gen_BPMN2Model_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_TerminateEventDefinition)
gen_BPMN2Model_TextAnnotation_Artifact = Generalization(general=Artifact, specific=BPMN2Model_TextAnnotation)
gen_BPMN2Model_ThrowEvent_Event = Generalization(general=Event, specific=BPMN2Model_ThrowEvent)
gen_BPMN2Model_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=BPMN2Model_TimerEventDefinition)
gen_BPMN2Model_Transaction_SubProcess = Generalization(general=SubProcess, specific=BPMN2Model_Transaction)
gen_BPMN2Model_UserTask_Task = Generalization(general=Task, specific=BPMN2Model_UserTask)
gen_BPMN2Model_BPMNBase_EObject = Generalization(general=EObject, specific=BPMN2Model_BPMNBase)

# Domain Model
domain_model = DomainModel(
    name="BPMN2Model",
    types={BPMN2Model_DocumentRoot, BPMNBase, BPMN2Model_EStringToStringMapEntry, BPMN2Model_Activity, BPMN2Model_AdHocSubProcess, BPMN2Model_FlowElement, BPMN2Model_Artifact, BPMN2Model_Assignment, BPMN2Model_Association, BPMN2Model_Auditing, BPMN2Model_BaseElement, BPMN2Model_BoundaryEvent, BPMN2Model_BusinessRuleTask, BPMN2Model_CallableElement, BPMN2Model_CallActivity, BPMN2Model_CallChoreography, BPMN2Model_CallConversation, BPMN2Model_ConversationNode, BPMN2Model_CancelEventDefinition, BPMN2Model_EventDefinition, BPMN2Model_RootElement, BPMN2Model_CatchEvent, BPMN2Model_Category, BPMN2Model_CategoryValue, BPMN2Model_Choreography, BPMN2Model_Collaboration, BPMN2Model_ChoreographyActivity, BPMN2Model_ChoreographyTask, BPMN2Model_CompensateEventDefinition, BPMN2Model_ComplexBehaviorDefinition, BPMN2Model_ComplexGateway, BPMN2Model_ConditionalEventDefinition, BPMN2Model_Conversation, BPMN2Model_ConversationLink, BPMN2Model_CorrelationKey, BPMN2Model_CorrelationProperty, BPMN2Model_CorrelationPropertyBinding, BPMN2Model_CorrelationPropertyRetrievalExpression, BPMN2Model_CorrelationSubscription, BPMN2Model_DataAssociation, BPMN2Model_DataInput, BPMN2Model_DataInputAssociation, BPMN2Model_DataObject, BPMN2Model_DataObjectReference, BPMN2Model_DataOutput, BPMN2Model_DataOutputAssociation, BPMN2Model_DataState, BPMN2Model_DataStore, BPMN2Model_ConversationAssociation, BPMN2Model_DataStoreReference, BPMN2Model_Definitions, BPMN2Model_Documentation, BPMN2Model_EndEvent, BPMN2Model_EndPoint, BPMN2Model_Error, BPMN2Model_ErrorEventDefinition, BPMN2Model_Escalation, BPMN2Model_EscalationEventDefinition, BPMN2Model_Event, BPMN2Model_EventBasedGateway, BPMN2Model_ExclusiveGateway, BPMN2Model_Expression, BPMN2Model_Extension, BPMN2Model_ExtensionAttributeValue, BPMN2Model_FlowNode, BPMN2Model_FormalExpression, BPMN2Model_Gateway, BPMN2Model_GlobalBusinessRuleTask, BPMN2Model_GlobalChoreographyTask, BPMN2Model_GlobalConversation, BPMN2Model_GlobalManualTask, BPMN2Model_GlobalScriptTask, BPMN2Model_GlobalTask, BPMN2Model_GlobalUserTask, BPMN2Model_Group, BPMN2Model_HumanPerformer, BPMN2Model_Performer, BPMN2Model_ResourceRole, BPMN2Model_ImplicitThrowEvent, BPMN2Model_Import, BPMN2Model_InclusiveGateway, BPMN2Model_InputSet, BPMN2Model_IntermediateCatchEvent, BPMN2Model_IntermediateThrowEvent, BPMN2Model_InputOutputBinding, BPMN2Model_InputOutputSpecification, BPMN2Model_ItemDefinition, BPMN2Model_Lane, BPMN2Model_LaneSet, BPMN2Model_LinkEventDefinition, BPMN2Model_LoopCharacteristics, BPMN2Model_ManualTask, BPMN2Model_Interface, BPMN2Model_Message, BPMN2Model_MessageEventDefinition, BPMN2Model_MessageFlow, BPMN2Model_MessageFlowAssociation, BPMN2Model_Monitoring, BPMN2Model_MultiInstanceLoopCharacteristics, BPMN2Model_Operation, BPMN2Model_OutputSet, BPMN2Model_ParallelGateway, BPMN2Model_Participant, BPMN2Model_ParticipantAssociation, BPMN2Model_ParticipantMultiplicity, BPMN2Model_PartnerEntity, BPMN2Model_PartnerRole, BPMN2Model_PotentialOwner, BPMN2Model_Process, BPMN2Model_Property, BPMN2Model_ReceiveTask, BPMN2Model_Relationship, BPMN2Model_Rendering, BPMN2Model_Resource, BPMN2Model_ResourceAssignmentExpression, BPMN2Model_ResourceParameterBinding, BPMN2Model_EObject, BPMN2Model_ScriptTask, BPMN2Model_SendTask, BPMN2Model_SequenceFlow, BPMN2Model_ServiceTask, BPMN2Model_Signal, BPMN2Model_SignalEventDefinition, BPMN2Model_StandardLoopCharacteristics, BPMN2Model_StartEvent, BPMN2Model_ResourceParameter, BPMN2Model_SubChoreography, BPMN2Model_SubConversation, BPMN2Model_SubProcess, BPMN2Model_Task, BPMN2Model_TerminateEventDefinition, BPMN2Model_TextAnnotation, BPMN2Model_ThrowEvent, BPMN2Model_TimerEventDefinition, BPMN2Model_Transaction, BPMN2Model_UserTask, FlowNode, SubProcess, BaseElement, Artifact, BPMN2Model_ExtensionDefinition, CatchEvent, Task, Activity, ChoreographyActivity, ConversationNode, RootElement, EventDefinition, Event, Collaboration, FlowElementsContainer, Gateway, BPMN2Model_InteractionNode, InteractionNode, BPMN2Model_ItemAwareElement, ItemAwareElement, DataAssociation, FlowElement, ThrowEvent, BPMN2Model_ExtensionAttributeDefinition, BPMN2Model_FlowElementsContainer, Expression, GlobalTask, Choreography, CallableElement, Performer, LoopCharacteristics, ResourceRole, HumanPerformer, BPMN2Model_BPMNBase, EObject, AdHocOrdering, AssociationDirection, ChoreographyLoopType, EventBasedGatewayType, GatewayDirection, ItemKind, MultiInstanceBehavior, ProcessType, RelationshipDirection},
    associations={xSISchemaLocation1, activity4, adHocSubProcess6, flowElement8, artifact10, assignment12, association14, auditing16, baseElement18, baseElementWithMixedContent20, boundaryEvent23, businessRuleTask25, callableElement27, callActivity29, callChoreography31, callConversation33, xMLNSPrefixMap0, cancelEventDefinition37, eventDefinition39, rootElement41, catchEvent43, category45, categoryValue47, choreography49, collaboration51, choreographyActivity53, choreographyTask55, compensateEventDefinition57, complexBehaviorDefinition59, complexGateway61, conditionalEventDefinition63, conversation65, conversationNode35, conversationAssociation67, conversationLink69, correlationKey71, correlationProperty73, correlationPropertyBinding75, correlationPropertyRetrievalExpression77, correlationSubscription79, dataAssociation81, dataInput83, dataInputAssociation85, dataObject87, dataObjectReference89, dataOutput91, dataOutputAssociation93, dataState95, dataStoreReference99, definitions101, documentation103, endEvent105, endPoint107, error109, errorEventDefinition111, escalation113, escalationEventDefinition115, event117, eventBasedGateway119, exclusiveGateway121, expression123, extension125, dataStore97, extensionElements127, flowNode129, formalExpression131, gateway133, globalBusinessRuleTask135, globalChoreographyTask137, globalConversation139, globalManualTask141, globalScriptTask143, globalTask145, globalUserTask147, group149, humanPerformer151, performer153, resourceRole155, implicitThrowEvent157, import159, inclusiveGateway161, inputSet163, interface165, intermediateCatchEvent167, intermediateThrowEvent169, ioBinding171, ioSpecification173, itemDefinition175, lane177, laneSet179, linkEventDefinition181, loopCharacteristics183, manualTask185, message187, messageEventDefinition189, messageFlow191, messageFlowAssociation193, monitoring195, multiInstanceLoopCharacteristics197, operation199, outputSet201, parallelGateway203, participant205, participantAssociation207, partnerEntity211, partnerRole213, potentialOwner215, process217, property219, receiveTask221, relationship223, rendering225, resource227, resourceAssignmentExpression229, participantMultiplicity209, resourceParameter231, resourceParameterBinding233, script235, scriptTask237, sendTask239, sequenceFlow241, serviceTask243, signal245, signalEventDefinition247, standardLoopCharacteristics249, startEvent251, subChoreography253, subConversation255, subProcess257, task259, terminateEventDefinition261, text263, textAnnotation266, throwEvent268, timerEventDefinition270, transaction272, userTask274, ioSpecification276, boundaryEventRefs279, properties280, dataInputAssociations283, dataOutputAssociations286, resources289, loopCharacteristics292, default295, completionCondition298, from301, to304, sourceRef307, targetRef310, extensionValues313, documentation316, extensionDefinitions319, attachedToRef321, calledElementRef322, participantAssociations325, calledChoreographyRef328, participantAssociations331, calledCollaborationRef334, supportedInterfaceRefs337, ioSpecification340, ioBinding343, dataOutputs346, dataOutputAssociation349, outputSet352, eventDefinitions355, eventDefinitionRefs358, categoryValue361, categorizedFlowElements364, participantRefs367, correlationKeys370, initiatingParticipantRef373, messageFlowRef376, participants379, messageFlows382, artifacts385, conversations388, conversationAssociations391, participantAssociations394, messageFlowAssociations397, correlationKeys400, choreographyRef403, conversationLinks406, activityRef409, condition412, event415, activationCondition418, default421, condition424, innerConversationNodeRef427, outerConversationNodeRef430, sourceRef433, targetRef435, participantRefs438, messageFlowRefs441, correlationKeys444, correlationPropertyRef447, correlationPropertyRetrievalExpression450, type453, dataPath456, correlationPropertyRef459, messagePath462, messageRef465, correlationPropertyBinding468, correlationKeyRef471, sourceRef474, targetRef476, transformation479, assignment482, inputSetWithOptional485, inputSetWithWhileExecuting486, inputSetRefs488, dataObjectRef490, outputSetWithOptional493, outputSetWithWhileExecuting494, outputSetRefs496, dataStoreRef498, imports501, extensions504, rootElements507, relationships510, structureRef513, errorRef516, structureRef519, escalationRef522, properties525, default528, definition531, extensionDefinition534, valueRef535, extensionAttributeDefinition538, extensionAttributeDefinitions540, auditing541, monitoring544, categoryValueRef547, laneSets550, flowElements552, incoming555, lanes556, outgoing557, evaluatesToTypeRef559, initiatingParticipantRef562, resources565, renderings568, categoryValueRef571, default574, inputDataRef577, operationRef580, outputDataRef583, dataInputs586, dataOutputs589, inputSets592, outputSets595, dataInputRefs598, optionalInputRefs599, whileExecutingInputRefs601, outputSetRefs603, incomingConversationLinks606, outgoingConversationLinks609, operations612, implementationRef615, dataState618, itemSubjectRef621, import624, structureRef627, partitionElement630, flowNodeRefs633, childLaneSet634, partitionElementRef637, lanes640, source644, target646, itemRef648, operationRef651, messageRef654, messageRef657, sourceRef660, targetRef663, innerMessageFlowRef666, outerMessageFlowRef669, loopCardinality672, loopDataInputRef675, loopDataOutputRef678, inputDataItem681, outputDataItem684, complexBehaviorDefinition687, completionCondition690, noneBehaviorEventRef693, oneBehaviorEventRef696, inMessageRef699, outMessageRef702, errorRefs705, implementationRef708, dataOutputRefs711, optionalOutputRefs712, whileExecutingOutputRefs714, inputSetRefs716, interfaceRefs719, endPointRefs722, participantMultiplicity725, processRef728, innerParticipantRef731, outerParticipantRef734, participantRef737, participantRef740, auditing743, monitoring746, properties749, artifacts752, resources755, correlationSubscriptions758, supports762, definitionalCollaborationRef764, messageRef767, operationRef770, sources773, targets776, resourceParameters779, expression782, type785, expression788, parameterRef791, resourceRef794, resourceParameterBindings797, resourceAssignmentExpression800, messageRef803, operationRef806, conditionExpression809, sourceRef812, targetRef814, operationRef816, structureRef819, signalRef822, loopCondition825, loopMaximum828, artifacts831, conversationNodes834, artifacts837, dataInputs840, dataInputAssociation843, inputSet846, eventDefinitions849, eventDefinitionRefs852, timeDate855, timeDuration858, timeCycle861, renderings864},
    generalizations={gen_BPMN2Model_DocumentRoot_BPMNBase, gen_BPMN2Model_Activity_FlowNode, gen_BPMN2Model_AdHocSubProcess_SubProcess, gen_BPMN2Model_Artifact_BaseElement, gen_BPMN2Model_Assignment_BaseElement, gen_BPMN2Model_Association_Artifact, gen_BPMN2Model_Auditing_BaseElement, gen_BPMN2Model_BaseElement_BPMNBase, gen_BPMN2Model_BoundaryEvent_CatchEvent, gen_BPMN2Model_BusinessRuleTask_Task, gen_BPMN2Model_CallActivity_Activity, gen_BPMN2Model_CallChoreography_ChoreographyActivity, gen_BPMN2Model_CallConversation_ConversationNode, gen_BPMN2Model_CallableElement_RootElement, gen_BPMN2Model_CancelEventDefinition_EventDefinition, gen_BPMN2Model_CatchEvent_Event, gen_BPMN2Model_Category_RootElement, gen_BPMN2Model_CategoryValue_BaseElement, gen_BPMN2Model_Choreography_Collaboration, gen_BPMN2Model_Choreography_FlowElementsContainer, gen_BPMN2Model_ChoreographyActivity_FlowNode, gen_BPMN2Model_ChoreographyTask_ChoreographyActivity, gen_BPMN2Model_Collaboration_RootElement, gen_BPMN2Model_CompensateEventDefinition_EventDefinition, gen_BPMN2Model_ComplexBehaviorDefinition_BaseElement, gen_BPMN2Model_ComplexGateway_Gateway, gen_BPMN2Model_ConditionalEventDefinition_EventDefinition, gen_BPMN2Model_Conversation_ConversationNode, gen_BPMN2Model_ConversationAssociation_BaseElement, gen_BPMN2Model_ConversationLink_BaseElement, gen_BPMN2Model_ConversationNode_BaseElement, gen_BPMN2Model_ConversationNode_InteractionNode, gen_BPMN2Model_CorrelationKey_BaseElement, gen_BPMN2Model_CorrelationProperty_RootElement, gen_BPMN2Model_CorrelationPropertyBinding_BaseElement, gen_BPMN2Model_CorrelationPropertyRetrievalExpression_BaseElement, gen_BPMN2Model_CorrelationSubscription_BaseElement, gen_BPMN2Model_DataAssociation_BaseElement, gen_BPMN2Model_DataInput_ItemAwareElement, gen_BPMN2Model_DataInputAssociation_DataAssociation, gen_BPMN2Model_DataObject_FlowElement, gen_BPMN2Model_DataObject_ItemAwareElement, gen_BPMN2Model_DataObjectReference_FlowElement, gen_BPMN2Model_DataObjectReference_ItemAwareElement, gen_BPMN2Model_DataOutput_ItemAwareElement, gen_BPMN2Model_DataOutputAssociation_DataAssociation, gen_BPMN2Model_DataState_BaseElement, gen_BPMN2Model_DataStore_ItemAwareElement, gen_BPMN2Model_DataStore_RootElement, gen_BPMN2Model_DataStoreReference_FlowElement, gen_BPMN2Model_DataStoreReference_ItemAwareElement, gen_BPMN2Model_Definitions_BaseElement, gen_BPMN2Model_Documentation_BaseElement, gen_BPMN2Model_EndEvent_ThrowEvent, gen_BPMN2Model_EndPoint_RootElement, gen_BPMN2Model_Error_RootElement, gen_BPMN2Model_ErrorEventDefinition_EventDefinition, gen_BPMN2Model_Escalation_BPMNBase, gen_BPMN2Model_EscalationEventDefinition_EventDefinition, gen_BPMN2Model_Event_FlowNode, gen_BPMN2Model_Event_InteractionNode, gen_BPMN2Model_EventBasedGateway_Gateway, gen_BPMN2Model_EventDefinition_RootElement, gen_BPMN2Model_ExclusiveGateway_Gateway, gen_BPMN2Model_Extension_BPMNBase, gen_BPMN2Model_ExtensionAttributeDefinition_BPMNBase, gen_BPMN2Model_ExtensionAttributeValue_BPMNBase, gen_BPMN2Model_ExtensionDefinition_BPMNBase, gen_BPMN2Model_FlowElement_BaseElement, gen_BPMN2Model_FlowElementsContainer_BaseElement, gen_BPMN2Model_FlowNode_FlowElement, gen_BPMN2Model_Expression_BaseElement, gen_BPMN2Model_FormalExpression_Expression, gen_BPMN2Model_Gateway_FlowNode, gen_BPMN2Model_GlobalBusinessRuleTask_GlobalTask, gen_BPMN2Model_GlobalChoreographyTask_Choreography, gen_BPMN2Model_GlobalConversation_Collaboration, gen_BPMN2Model_GlobalManualTask_GlobalTask, gen_BPMN2Model_GlobalScriptTask_GlobalTask, gen_BPMN2Model_GlobalTask_CallableElement, gen_BPMN2Model_GlobalUserTask_GlobalTask, gen_BPMN2Model_Group_Artifact, gen_BPMN2Model_HumanPerformer_Performer, gen_BPMN2Model_ImplicitThrowEvent_ThrowEvent, gen_BPMN2Model_Import_BPMNBase, gen_BPMN2Model_InclusiveGateway_Gateway, gen_BPMN2Model_InputOutputBinding_BPMNBase, gen_BPMN2Model_InputOutputSpecification_BaseElement, gen_BPMN2Model_InputSet_BaseElement, gen_BPMN2Model_InteractionNode_BPMNBase, gen_BPMN2Model_Interface_RootElement, gen_BPMN2Model_IntermediateCatchEvent_CatchEvent, gen_BPMN2Model_IntermediateThrowEvent_ThrowEvent, gen_BPMN2Model_ItemAwareElement_BaseElement, gen_BPMN2Model_ItemDefinition_RootElement, gen_BPMN2Model_Lane_BaseElement, gen_BPMN2Model_LaneSet_BaseElement, gen_BPMN2Model_LinkEventDefinition_EventDefinition, gen_BPMN2Model_LoopCharacteristics_BaseElement, gen_BPMN2Model_ManualTask_Task, gen_BPMN2Model_Message_RootElement, gen_BPMN2Model_MessageEventDefinition_EventDefinition, gen_BPMN2Model_MessageFlow_BaseElement, gen_BPMN2Model_MessageFlowAssociation_BaseElement, gen_BPMN2Model_Monitoring_BaseElement, gen_BPMN2Model_MultiInstanceLoopCharacteristics_LoopCharacteristics, gen_BPMN2Model_Operation_BaseElement, gen_BPMN2Model_OutputSet_BaseElement, gen_BPMN2Model_ParallelGateway_Gateway, gen_BPMN2Model_Participant_BaseElement, gen_BPMN2Model_Participant_InteractionNode, gen_BPMN2Model_ParticipantAssociation_BaseElement, gen_BPMN2Model_ParticipantMultiplicity_BPMNBase, gen_BPMN2Model_PartnerEntity_RootElement, gen_BPMN2Model_PartnerRole_RootElement, gen_BPMN2Model_Performer_ResourceRole, gen_BPMN2Model_PotentialOwner_HumanPerformer, gen_BPMN2Model_Process_CallableElement, gen_BPMN2Model_Process_FlowElementsContainer, gen_BPMN2Model_Property_ItemAwareElement, gen_BPMN2Model_ReceiveTask_Task, gen_BPMN2Model_Relationship_BaseElement, gen_BPMN2Model_Rendering_BaseElement, gen_BPMN2Model_Resource_RootElement, gen_BPMN2Model_ResourceAssignmentExpression_BPMNBase, gen_BPMN2Model_ResourceParameter_BaseElement, gen_BPMN2Model_ResourceParameterBinding_BPMNBase, gen_BPMN2Model_ResourceRole_BaseElement, gen_BPMN2Model_RootElement_BaseElement, gen_BPMN2Model_ScriptTask_Task, gen_BPMN2Model_SendTask_Task, gen_BPMN2Model_SequenceFlow_FlowElement, gen_BPMN2Model_ServiceTask_Task, gen_BPMN2Model_Signal_RootElement, gen_BPMN2Model_SignalEventDefinition_EventDefinition, gen_BPMN2Model_StandardLoopCharacteristics_LoopCharacteristics, gen_BPMN2Model_StartEvent_CatchEvent, gen_BPMN2Model_SubChoreography_ChoreographyActivity, gen_BPMN2Model_SubChoreography_FlowElementsContainer, gen_BPMN2Model_SubConversation_ConversationNode, gen_BPMN2Model_SubProcess_Activity, gen_BPMN2Model_SubProcess_FlowElementsContainer, gen_BPMN2Model_Task_Activity, gen_BPMN2Model_Task_InteractionNode, gen_BPMN2Model_TerminateEventDefinition_EventDefinition, gen_BPMN2Model_TextAnnotation_Artifact, gen_BPMN2Model_ThrowEvent_Event, gen_BPMN2Model_TimerEventDefinition_EventDefinition, gen_BPMN2Model_Transaction_SubProcess, gen_BPMN2Model_UserTask_Task, gen_BPMN2Model_BPMNBase_EObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)