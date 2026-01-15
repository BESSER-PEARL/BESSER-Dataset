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
bpmn2_DocumentRoot = Class(name="bpmn2::DocumentRoot")
bpmn2_EStringToStringMapEntry = Class(name="bpmn2::EStringToStringMapEntry")
bpmn2_Activity = Class(name="bpmn2::Activity")
bpmn2_AdHocSubProcess = Class(name="bpmn2::AdHocSubProcess")
bpmn2_FlowElement = Class(name="bpmn2::FlowElement", is_abstract=True)
bpmn2_Artifact = Class(name="bpmn2::Artifact")
bpmn2_Assignment = Class(name="bpmn2::Assignment")
bpmn2_BoundaryEvent = Class(name="bpmn2::BoundaryEvent")
bpmn2_BusinessRuleTask = Class(name="bpmn2::BusinessRuleTask")
bpmn2_CallableElement = Class(name="bpmn2::CallableElement")
bpmn2_CallActivity = Class(name="bpmn2::CallActivity")
bpmn2_CallChoreography = Class(name="bpmn2::CallChoreography")
bpmn2_CallConversation = Class(name="bpmn2::CallConversation")
bpmn2_ConversationNode = Class(name="bpmn2::ConversationNode")
bpmn2_CancelEventDefinition = Class(name="bpmn2::CancelEventDefinition")
bpmn2_EventDefinition = Class(name="bpmn2::EventDefinition")
bpmn2_RootElement = Class(name="bpmn2::RootElement")
bpmn2_Association = Class(name="bpmn2::Association")
bpmn2_Auditing = Class(name="bpmn2::Auditing")
bpmn2_BaseElement = Class(name="bpmn2::BaseElement")
bpmn2_DataInputAssociation = Class(name="bpmn2::DataInputAssociation")
bpmn2_ChoreographyTask = Class(name="bpmn2::ChoreographyTask")
bpmn2_DataObject = Class(name="bpmn2::DataObject")
bpmn2_CompensateEventDefinition = Class(name="bpmn2::CompensateEventDefinition")
bpmn2_DataObjectReference = Class(name="bpmn2::DataObjectReference")
bpmn2_ComplexBehaviorDefinition = Class(name="bpmn2::ComplexBehaviorDefinition")
bpmn2_DataOutput = Class(name="bpmn2::DataOutput")
bpmn2_ComplexGateway = Class(name="bpmn2::ComplexGateway")
bpmn2_ConditionalEventDefinition = Class(name="bpmn2::ConditionalEventDefinition")
bpmn2_Conversation = Class(name="bpmn2::Conversation")
bpmn2_ConversationAssociation = Class(name="bpmn2::ConversationAssociation")
bpmn2_ConversationLink = Class(name="bpmn2::ConversationLink")
bpmn2_CorrelationKey = Class(name="bpmn2::CorrelationKey")
bpmn2_CorrelationProperty = Class(name="bpmn2::CorrelationProperty")
bpmn2_CorrelationPropertyBinding = Class(name="bpmn2::CorrelationPropertyBinding")
bpmn2_CatchEvent = Class(name="bpmn2::CatchEvent", is_abstract=True)
bpmn2_CorrelationPropertyRetrievalExpression = Class(name="bpmn2::CorrelationPropertyRetrievalExpression")
bpmn2_Category = Class(name="bpmn2::Category")
bpmn2_CategoryValue = Class(name="bpmn2::CategoryValue")
bpmn2_CorrelationSubscription = Class(name="bpmn2::CorrelationSubscription")
bpmn2_Choreography = Class(name="bpmn2::Choreography")
bpmn2_DataAssociation = Class(name="bpmn2::DataAssociation")
bpmn2_Collaboration = Class(name="bpmn2::Collaboration")
bpmn2_DataInput = Class(name="bpmn2::DataInput")
bpmn2_ChoreographyActivity = Class(name="bpmn2::ChoreographyActivity", is_abstract=True)
bpmn2_Error = Class(name="bpmn2::Error")
bpmn2_ErrorEventDefinition = Class(name="bpmn2::ErrorEventDefinition")
bpmn2_Escalation = Class(name="bpmn2::Escalation")
bpmn2_EscalationEventDefinition = Class(name="bpmn2::EscalationEventDefinition")
bpmn2_Event = Class(name="bpmn2::Event", is_abstract=True)
bpmn2_DataOutputAssociation = Class(name="bpmn2::DataOutputAssociation")
bpmn2_DataState = Class(name="bpmn2::DataState")
bpmn2_DataStore = Class(name="bpmn2::DataStore")
bpmn2_DataStoreReference = Class(name="bpmn2::DataStoreReference")
bpmn2_Definitions = Class(name="bpmn2::Definitions")
bpmn2_Documentation = Class(name="bpmn2::Documentation")
bpmn2_EndEvent = Class(name="bpmn2::EndEvent")
bpmn2_EndPoint = Class(name="bpmn2::EndPoint")
bpmn2_FormalExpression = Class(name="bpmn2::FormalExpression")
bpmn2_Gateway = Class(name="bpmn2::Gateway", is_abstract=True)
bpmn2_GlobalBusinessRuleTask = Class(name="bpmn2::GlobalBusinessRuleTask")
bpmn2_GlobalChoreographyTask = Class(name="bpmn2::GlobalChoreographyTask")
bpmn2_GlobalConversation = Class(name="bpmn2::GlobalConversation")
bpmn2_EventBasedGateway = Class(name="bpmn2::EventBasedGateway")
bpmn2_ExclusiveGateway = Class(name="bpmn2::ExclusiveGateway")
bpmn2_Expression = Class(name="bpmn2::Expression")
bpmn2_Extension = Class(name="bpmn2::Extension")
bpmn2_ExtensionAttributeValue = Class(name="bpmn2::ExtensionAttributeValue")
bpmn2_FlowNode = Class(name="bpmn2::FlowNode", is_abstract=True)
bpmn2_ResourceRole = Class(name="bpmn2::ResourceRole")
bpmn2_ImplicitThrowEvent = Class(name="bpmn2::ImplicitThrowEvent")
bpmn2_Import = Class(name="bpmn2::Import")
bpmn2_InclusiveGateway = Class(name="bpmn2::InclusiveGateway")
bpmn2_InputSet = Class(name="bpmn2::InputSet")
bpmn2_GlobalManualTask = Class(name="bpmn2::GlobalManualTask")
bpmn2_GlobalScriptTask = Class(name="bpmn2::GlobalScriptTask")
bpmn2_GlobalTask = Class(name="bpmn2::GlobalTask")
bpmn2_GlobalUserTask = Class(name="bpmn2::GlobalUserTask")
bpmn2_Group = Class(name="bpmn2::Group")
bpmn2_HumanPerformer = Class(name="bpmn2::HumanPerformer")
bpmn2_Performer = Class(name="bpmn2::Performer")
bpmn2_InputOutputSpecification = Class(name="bpmn2::InputOutputSpecification")
bpmn2_ItemDefinition = Class(name="bpmn2::ItemDefinition")
bpmn2_Lane = Class(name="bpmn2::Lane")
bpmn2_LaneSet = Class(name="bpmn2::LaneSet")
bpmn2_Interface = Class(name="bpmn2::Interface")
bpmn2_IntermediateCatchEvent = Class(name="bpmn2::IntermediateCatchEvent")
bpmn2_IntermediateThrowEvent = Class(name="bpmn2::IntermediateThrowEvent")
bpmn2_Monitoring = Class(name="bpmn2::Monitoring")
bpmn2_InputOutputBinding = Class(name="bpmn2::InputOutputBinding")
bpmn2_MultiInstanceLoopCharacteristics = Class(name="bpmn2::MultiInstanceLoopCharacteristics")
bpmn2_Operation = Class(name="bpmn2::Operation")
bpmn2_OutputSet = Class(name="bpmn2::OutputSet")
bpmn2_LinkEventDefinition = Class(name="bpmn2::LinkEventDefinition")
bpmn2_LoopCharacteristics = Class(name="bpmn2::LoopCharacteristics", is_abstract=True)
bpmn2_ManualTask = Class(name="bpmn2::ManualTask")
bpmn2_Message = Class(name="bpmn2::Message")
bpmn2_MessageEventDefinition = Class(name="bpmn2::MessageEventDefinition")
bpmn2_MessageFlow = Class(name="bpmn2::MessageFlow")
bpmn2_MessageFlowAssociation = Class(name="bpmn2::MessageFlowAssociation")
bpmn2_Process = Class(name="bpmn2::Process")
bpmn2_Property = Class(name="bpmn2::Property")
bpmn2_ReceiveTask = Class(name="bpmn2::ReceiveTask")
bpmn2_Relationship = Class(name="bpmn2::Relationship")
bpmn2_ParallelGateway = Class(name="bpmn2::ParallelGateway")
bpmn2_Participant = Class(name="bpmn2::Participant")
bpmn2_ParticipantAssociation = Class(name="bpmn2::ParticipantAssociation")
bpmn2_ParticipantMultiplicity = Class(name="bpmn2::ParticipantMultiplicity")
bpmn2_PartnerEntity = Class(name="bpmn2::PartnerEntity")
bpmn2_PartnerRole = Class(name="bpmn2::PartnerRole")
bpmn2_PotentialOwner = Class(name="bpmn2::PotentialOwner")
bpmn2_EObject = Class(name="bpmn2::EObject")
bpmn2_ScriptTask = Class(name="bpmn2::ScriptTask")
bpmn2_SendTask = Class(name="bpmn2::SendTask")
bpmn2_SequenceFlow = Class(name="bpmn2::SequenceFlow")
bpmn2_Rendering = Class(name="bpmn2::Rendering")
bpmn2_Resource = Class(name="bpmn2::Resource")
bpmn2_ResourceAssignmentExpression = Class(name="bpmn2::ResourceAssignmentExpression")
bpmn2_ResourceParameter = Class(name="bpmn2::ResourceParameter")
bpmn2_ResourceParameterBinding = Class(name="bpmn2::ResourceParameterBinding")
bpmn2_SubConversation = Class(name="bpmn2::SubConversation")
bpmn2_SubProcess = Class(name="bpmn2::SubProcess")
bpmn2_Task = Class(name="bpmn2::Task")
bpmn2_ServiceTask = Class(name="bpmn2::ServiceTask")
bpmn2_Signal = Class(name="bpmn2::Signal")
bpmn2_SignalEventDefinition = Class(name="bpmn2::SignalEventDefinition")
bpmn2_StandardLoopCharacteristics = Class(name="bpmn2::StandardLoopCharacteristics")
bpmn2_StartEvent = Class(name="bpmn2::StartEvent")
bpmn2_SubChoreography = Class(name="bpmn2::SubChoreography")
bpmn2_Transaction = Class(name="bpmn2::Transaction")
bpmn2_UserTask = Class(name="bpmn2::UserTask")
FlowNode = Class(name="FlowNode")
bpmn2_TerminateEventDefinition = Class(name="bpmn2::TerminateEventDefinition")
bpmn2_TextAnnotation = Class(name="bpmn2::TextAnnotation")
bpmn2_ThrowEvent = Class(name="bpmn2::ThrowEvent", is_abstract=True)
bpmn2_TimerEventDefinition = Class(name="bpmn2::TimerEventDefinition")
bpmn2_Position = Class(name="bpmn2::Position")
bpmn2_Role = Class(name="bpmn2::Role")
SubProcess = Class(name="SubProcess")
bpmn2_Competency = Class(name="bpmn2::Competency")
bpmn2_Criterion = Class(name="bpmn2::Criterion")
bpmn2_OrganisationalUnit = Class(name="bpmn2::OrganisationalUnit")
CatchEvent = Class(name="CatchEvent")
Task = Class(name="Task")
Activity = Class(name="Activity")
ChoreographyActivity = Class(name="ChoreographyActivity")
ConversationNode = Class(name="ConversationNode")
BaseElement = Class(name="BaseElement")
Artifact = Class(name="Artifact")
bpmn2_ExtensionDefinition = Class(name="bpmn2::ExtensionDefinition")
Collaboration = Class(name="Collaboration")
FlowElementsContainer = Class(name="FlowElementsContainer")
RootElement = Class(name="RootElement")
EventDefinition = Class(name="EventDefinition")
Event = Class(name="Event")
Gateway = Class(name="Gateway")
bpmn2_InteractionNode = Class(name="bpmn2::InteractionNode")
InteractionNode = Class(name="InteractionNode")
bpmn2_ItemAwareElement = Class(name="bpmn2::ItemAwareElement")
ItemAwareElement = Class(name="ItemAwareElement")
bpmn2_Document = Class(name="bpmn2::Document")
DataAssociation = Class(name="DataAssociation")
FlowElement = Class(name="FlowElement")
bpmn2_BPMNDiagram = Class(name="bpmn2::BPMNDiagram")
ThrowEvent = Class(name="ThrowEvent")
bpmn2_ExtensionAttributeDefinition = Class(name="bpmn2::ExtensionAttributeDefinition")
Expression = Class(name="Expression")
bpmn2_FlowElementsContainer = Class(name="bpmn2::FlowElementsContainer", is_abstract=True)
GlobalTask = Class(name="GlobalTask")
Choreography = Class(name="Choreography")
CallableElement = Class(name="CallableElement")
Performer = Class(name="Performer")
LoopCharacteristics = Class(name="LoopCharacteristics")
ResourceRole = Class(name="ResourceRole")
HumanPerformer = Class(name="HumanPerformer")

# bpmn2_DocumentRoot class attributes and methods

# bpmn2_EStringToStringMapEntry class attributes and methods

# bpmn2_Activity class attributes and methods
bpmn2_Activity_completionQuantity: Property = Property(name="completionQuantity", type=IntegerType)
bpmn2_Activity_isForCompensation: Property = Property(name="isForCompensation", type=BooleanType)
bpmn2_Activity_startQuantity: Property = Property(name="startQuantity", type=IntegerType)
bpmn2_Activity.attributes={bpmn2_Activity_isForCompensation, bpmn2_Activity_startQuantity, bpmn2_Activity_completionQuantity}

# bpmn2_AdHocSubProcess class attributes and methods
bpmn2_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=BooleanType)
bpmn2_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
bpmn2_AdHocSubProcess.attributes={bpmn2_AdHocSubProcess_ordering, bpmn2_AdHocSubProcess_cancelRemainingInstances}

# bpmn2_FlowElement class attributes and methods

# bpmn2_Artifact class attributes and methods

# bpmn2_Assignment class attributes and methods

# bpmn2_BoundaryEvent class attributes and methods
bpmn2_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=BooleanType)
bpmn2_BoundaryEvent.attributes={bpmn2_BoundaryEvent_cancelActivity}

# bpmn2_BusinessRuleTask class attributes and methods
bpmn2_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_BusinessRuleTask.attributes={bpmn2_BusinessRuleTask_implementation}

# bpmn2_CallableElement class attributes and methods

# bpmn2_CallActivity class attributes and methods

# bpmn2_CallChoreography class attributes and methods

# bpmn2_CallConversation class attributes and methods

# bpmn2_ConversationNode class attributes and methods

# bpmn2_CancelEventDefinition class attributes and methods

# bpmn2_EventDefinition class attributes and methods

# bpmn2_RootElement class attributes and methods

# bpmn2_Association class attributes and methods
bpmn2_Association_associationDirection: Property = Property(name="associationDirection", type=StringType)
bpmn2_Association.attributes={bpmn2_Association_associationDirection}

# bpmn2_Auditing class attributes and methods

# bpmn2_BaseElement class attributes and methods
bpmn2_BaseElement_description: Property = Property(name="description", type=StringType)
bpmn2_BaseElement_id: Property = Property(name="id", type=StringType)
bpmn2_BaseElement_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
bpmn2_BaseElement_name: Property = Property(name="name", type=StringType)
bpmn2_BaseElement.attributes={bpmn2_BaseElement_anyAttribute, bpmn2_BaseElement_description, bpmn2_BaseElement_name, bpmn2_BaseElement_id}

# bpmn2_DataInputAssociation class attributes and methods

# bpmn2_ChoreographyTask class attributes and methods

# bpmn2_DataObject class attributes and methods
bpmn2_DataObject_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataObject.attributes={bpmn2_DataObject_isCollection}

# bpmn2_CompensateEventDefinition class attributes and methods
bpmn2_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=BooleanType)
bpmn2_CompensateEventDefinition.attributes={bpmn2_CompensateEventDefinition_waitForCompletion}

# bpmn2_DataObjectReference class attributes and methods

# bpmn2_ComplexBehaviorDefinition class attributes and methods

# bpmn2_DataOutput class attributes and methods
bpmn2_DataOutput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataOutput.attributes={bpmn2_DataOutput_isCollection}

# bpmn2_ComplexGateway class attributes and methods

# bpmn2_ConditionalEventDefinition class attributes and methods

# bpmn2_Conversation class attributes and methods

# bpmn2_ConversationAssociation class attributes and methods

# bpmn2_ConversationLink class attributes and methods

# bpmn2_CorrelationKey class attributes and methods

# bpmn2_CorrelationProperty class attributes and methods

# bpmn2_CorrelationPropertyBinding class attributes and methods

# bpmn2_CatchEvent class attributes and methods
bpmn2_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=BooleanType)
bpmn2_CatchEvent.attributes={bpmn2_CatchEvent_parallelMultiple}

# bpmn2_CorrelationPropertyRetrievalExpression class attributes and methods

# bpmn2_Category class attributes and methods

# bpmn2_CategoryValue class attributes and methods
bpmn2_CategoryValue_value: Property = Property(name="value", type=StringType)
bpmn2_CategoryValue.attributes={bpmn2_CategoryValue_value}

# bpmn2_CorrelationSubscription class attributes and methods

# bpmn2_Choreography class attributes and methods

# bpmn2_DataAssociation class attributes and methods

# bpmn2_Collaboration class attributes and methods
bpmn2_Collaboration_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Collaboration.attributes={bpmn2_Collaboration_isClosed}

# bpmn2_DataInput class attributes and methods
bpmn2_DataInput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataInput.attributes={bpmn2_DataInput_isCollection}

# bpmn2_ChoreographyActivity class attributes and methods
bpmn2_ChoreographyActivity_loopType: Property = Property(name="loopType", type=StringType)
bpmn2_ChoreographyActivity.attributes={bpmn2_ChoreographyActivity_loopType}

# bpmn2_Error class attributes and methods
bpmn2_Error_errorCode: Property = Property(name="errorCode", type=StringType)
bpmn2_Error.attributes={bpmn2_Error_errorCode}

# bpmn2_ErrorEventDefinition class attributes and methods

# bpmn2_Escalation class attributes and methods
bpmn2_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
bpmn2_Escalation.attributes={bpmn2_Escalation_escalationCode}

# bpmn2_EscalationEventDefinition class attributes and methods

# bpmn2_Event class attributes and methods

# bpmn2_DataOutputAssociation class attributes and methods

# bpmn2_DataState class attributes and methods

# bpmn2_DataStore class attributes and methods
bpmn2_DataStore_capacity: Property = Property(name="capacity", type=IntegerType)
bpmn2_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=BooleanType)
bpmn2_DataStore.attributes={bpmn2_DataStore_capacity, bpmn2_DataStore_isUnlimited}

# bpmn2_DataStoreReference class attributes and methods

# bpmn2_Definitions class attributes and methods
bpmn2_Definitions_exporter: Property = Property(name="exporter", type=StringType)
bpmn2_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
bpmn2_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
bpmn2_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
bpmn2_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
bpmn2_Definitions.attributes={bpmn2_Definitions_targetNamespace, bpmn2_Definitions_exporterVersion, bpmn2_Definitions_typeLanguage, bpmn2_Definitions_expressionLanguage, bpmn2_Definitions_exporter}

# bpmn2_Documentation class attributes and methods
bpmn2_Documentation_mixed: Property = Property(name="mixed", type=StringType)
bpmn2_Documentation_text: Property = Property(name="text", type=StringType)
bpmn2_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_Documentation.attributes={bpmn2_Documentation_textFormat, bpmn2_Documentation_text, bpmn2_Documentation_mixed}

# bpmn2_EndEvent class attributes and methods

# bpmn2_EndPoint class attributes and methods

# bpmn2_FormalExpression class attributes and methods
bpmn2_FormalExpression_mixed: Property = Property(name="mixed", type=StringType)
bpmn2_FormalExpression_body: Property = Property(name="body", type=StringType)
bpmn2_FormalExpression_language: Property = Property(name="language", type=StringType)
bpmn2_FormalExpression.attributes={bpmn2_FormalExpression_body, bpmn2_FormalExpression_language, bpmn2_FormalExpression_mixed}

# bpmn2_Gateway class attributes and methods
bpmn2_Gateway_gatewayDirection: Property = Property(name="gatewayDirection", type=StringType)
bpmn2_Gateway.attributes={bpmn2_Gateway_gatewayDirection}

# bpmn2_GlobalBusinessRuleTask class attributes and methods
bpmn2_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalBusinessRuleTask.attributes={bpmn2_GlobalBusinessRuleTask_implementation}

# bpmn2_GlobalChoreographyTask class attributes and methods

# bpmn2_GlobalConversation class attributes and methods

# bpmn2_EventBasedGateway class attributes and methods
bpmn2_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
bpmn2_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_EventBasedGateway.attributes={bpmn2_EventBasedGateway_eventGatewayType, bpmn2_EventBasedGateway_instantiate}

# bpmn2_ExclusiveGateway class attributes and methods

# bpmn2_Expression class attributes and methods

# bpmn2_Extension class attributes and methods
bpmn2_Extension_mustUnderstand: Property = Property(name="mustUnderstand", type=BooleanType)
bpmn2_Extension_xsdDefinition: Property = Property(name="xsdDefinition", type=StringType)
bpmn2_Extension.attributes={bpmn2_Extension_mustUnderstand, bpmn2_Extension_xsdDefinition}

# bpmn2_ExtensionAttributeValue class attributes and methods
bpmn2_ExtensionAttributeValue_value: Property = Property(name="value", type=StringType)
bpmn2_ExtensionAttributeValue.attributes={bpmn2_ExtensionAttributeValue_value}

# bpmn2_FlowNode class attributes and methods

# bpmn2_ResourceRole class attributes and methods

# bpmn2_ImplicitThrowEvent class attributes and methods

# bpmn2_Import class attributes and methods
bpmn2_Import_importType: Property = Property(name="importType", type=StringType)
bpmn2_Import_location: Property = Property(name="location", type=StringType)
bpmn2_Import_namespace: Property = Property(name="namespace", type=StringType)
bpmn2_Import.attributes={bpmn2_Import_location, bpmn2_Import_importType, bpmn2_Import_namespace}

# bpmn2_InclusiveGateway class attributes and methods

# bpmn2_InputSet class attributes and methods

# bpmn2_GlobalManualTask class attributes and methods

# bpmn2_GlobalScriptTask class attributes and methods
bpmn2_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_GlobalScriptTask_scriptLanguage: Property = Property(name="scriptLanguage", type=StringType)
bpmn2_GlobalScriptTask.attributes={bpmn2_GlobalScriptTask_script, bpmn2_GlobalScriptTask_scriptLanguage}

# bpmn2_GlobalTask class attributes and methods

# bpmn2_GlobalUserTask class attributes and methods
bpmn2_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalUserTask.attributes={bpmn2_GlobalUserTask_implementation}

# bpmn2_Group class attributes and methods

# bpmn2_HumanPerformer class attributes and methods

# bpmn2_Performer class attributes and methods

# bpmn2_InputOutputSpecification class attributes and methods

# bpmn2_ItemDefinition class attributes and methods
bpmn2_ItemDefinition_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
bpmn2_ItemDefinition.attributes={bpmn2_ItemDefinition_itemKind, bpmn2_ItemDefinition_isCollection}

# bpmn2_Lane class attributes and methods

# bpmn2_LaneSet class attributes and methods

# bpmn2_Interface class attributes and methods

# bpmn2_IntermediateCatchEvent class attributes and methods

# bpmn2_IntermediateThrowEvent class attributes and methods

# bpmn2_Monitoring class attributes and methods

# bpmn2_InputOutputBinding class attributes and methods

# bpmn2_MultiInstanceLoopCharacteristics class attributes and methods
bpmn2_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
bpmn2_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=BooleanType)
bpmn2_MultiInstanceLoopCharacteristics.attributes={bpmn2_MultiInstanceLoopCharacteristics_behavior, bpmn2_MultiInstanceLoopCharacteristics_isSequential}

# bpmn2_Operation class attributes and methods

# bpmn2_OutputSet class attributes and methods

# bpmn2_LinkEventDefinition class attributes and methods

# bpmn2_LoopCharacteristics class attributes and methods

# bpmn2_ManualTask class attributes and methods

# bpmn2_Message class attributes and methods

# bpmn2_MessageEventDefinition class attributes and methods

# bpmn2_MessageFlow class attributes and methods

# bpmn2_MessageFlowAssociation class attributes and methods

# bpmn2_Process class attributes and methods
bpmn2_Process_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Process_isExecutable: Property = Property(name="isExecutable", type=BooleanType)
bpmn2_Process_processType: Property = Property(name="processType", type=StringType)
bpmn2_Process.attributes={bpmn2_Process_processType, bpmn2_Process_isExecutable, bpmn2_Process_isClosed}

# bpmn2_Property class attributes and methods

# bpmn2_ReceiveTask class attributes and methods
bpmn2_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ReceiveTask_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_ReceiveTask.attributes={bpmn2_ReceiveTask_implementation, bpmn2_ReceiveTask_instantiate}

# bpmn2_Relationship class attributes and methods
bpmn2_Relationship_direction: Property = Property(name="direction", type=StringType)
bpmn2_Relationship_type: Property = Property(name="type", type=StringType)
bpmn2_Relationship.attributes={bpmn2_Relationship_direction, bpmn2_Relationship_type}

# bpmn2_ParallelGateway class attributes and methods

# bpmn2_Participant class attributes and methods

# bpmn2_ParticipantAssociation class attributes and methods

# bpmn2_ParticipantMultiplicity class attributes and methods
bpmn2_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=IntegerType)
bpmn2_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=IntegerType)
bpmn2_ParticipantMultiplicity.attributes={bpmn2_ParticipantMultiplicity_maximum, bpmn2_ParticipantMultiplicity_minimum}

# bpmn2_PartnerEntity class attributes and methods

# bpmn2_PartnerRole class attributes and methods

# bpmn2_PotentialOwner class attributes and methods

# bpmn2_EObject class attributes and methods

# bpmn2_ScriptTask class attributes and methods
bpmn2_ScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
bpmn2_ScriptTask.attributes={bpmn2_ScriptTask_script, bpmn2_ScriptTask_scriptFormat}

# bpmn2_SendTask class attributes and methods
bpmn2_SendTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_SendTask.attributes={bpmn2_SendTask_implementation}

# bpmn2_SequenceFlow class attributes and methods
bpmn2_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=BooleanType)
bpmn2_SequenceFlow.attributes={bpmn2_SequenceFlow_isImmediate}

# bpmn2_Rendering class attributes and methods

# bpmn2_Resource class attributes and methods

# bpmn2_ResourceAssignmentExpression class attributes and methods

# bpmn2_ResourceParameter class attributes and methods
bpmn2_ResourceParameter_isRequired: Property = Property(name="isRequired", type=BooleanType)
bpmn2_ResourceParameter.attributes={bpmn2_ResourceParameter_isRequired}

# bpmn2_ResourceParameterBinding class attributes and methods

# bpmn2_SubConversation class attributes and methods

# bpmn2_SubProcess class attributes and methods
bpmn2_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=BooleanType)
bpmn2_SubProcess.attributes={bpmn2_SubProcess_triggeredByEvent}

# bpmn2_Task class attributes and methods

# bpmn2_ServiceTask class attributes and methods
bpmn2_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ServiceTask.attributes={bpmn2_ServiceTask_implementation}

# bpmn2_Signal class attributes and methods

# bpmn2_SignalEventDefinition class attributes and methods

# bpmn2_StandardLoopCharacteristics class attributes and methods
bpmn2_StandardLoopCharacteristics_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
bpmn2_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=BooleanType)
bpmn2_StandardLoopCharacteristics.attributes={bpmn2_StandardLoopCharacteristics_loopMaximum, bpmn2_StandardLoopCharacteristics_testBefore}

# bpmn2_StartEvent class attributes and methods
bpmn2_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=BooleanType)
bpmn2_StartEvent.attributes={bpmn2_StartEvent_isInterrupting}

# bpmn2_SubChoreography class attributes and methods

# bpmn2_Transaction class attributes and methods
bpmn2_Transaction_protocol: Property = Property(name="protocol", type=StringType)
bpmn2_Transaction_method: Property = Property(name="method", type=StringType)
bpmn2_Transaction.attributes={bpmn2_Transaction_protocol, bpmn2_Transaction_method}

# bpmn2_UserTask class attributes and methods
bpmn2_UserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_UserTask.attributes={bpmn2_UserTask_implementation}

# FlowNode class attributes and methods

# bpmn2_TerminateEventDefinition class attributes and methods

# bpmn2_TextAnnotation class attributes and methods
bpmn2_TextAnnotation_text: Property = Property(name="text", type=StringType)
bpmn2_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_TextAnnotation.attributes={bpmn2_TextAnnotation_text, bpmn2_TextAnnotation_textFormat}

# bpmn2_ThrowEvent class attributes and methods

# bpmn2_TimerEventDefinition class attributes and methods

# bpmn2_Position class attributes and methods

# bpmn2_Role class attributes and methods

# SubProcess class attributes and methods

# bpmn2_Competency class attributes and methods

# bpmn2_Criterion class attributes and methods

# bpmn2_OrganisationalUnit class attributes and methods

# CatchEvent class attributes and methods

# Task class attributes and methods

# Activity class attributes and methods

# ChoreographyActivity class attributes and methods

# ConversationNode class attributes and methods

# BaseElement class attributes and methods

# Artifact class attributes and methods

# bpmn2_ExtensionDefinition class attributes and methods
bpmn2_ExtensionDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionDefinition.attributes={bpmn2_ExtensionDefinition_name}

# Collaboration class attributes and methods

# FlowElementsContainer class attributes and methods

# RootElement class attributes and methods

# EventDefinition class attributes and methods

# Event class attributes and methods

# Gateway class attributes and methods

# bpmn2_InteractionNode class attributes and methods

# InteractionNode class attributes and methods

# bpmn2_ItemAwareElement class attributes and methods

# ItemAwareElement class attributes and methods

# bpmn2_Document class attributes and methods

# DataAssociation class attributes and methods

# FlowElement class attributes and methods

# bpmn2_BPMNDiagram class attributes and methods

# ThrowEvent class attributes and methods

# bpmn2_ExtensionAttributeDefinition class attributes and methods
bpmn2_ExtensionAttributeDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
bpmn2_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=BooleanType)
bpmn2_ExtensionAttributeDefinition.attributes={bpmn2_ExtensionAttributeDefinition_type, bpmn2_ExtensionAttributeDefinition_isReference, bpmn2_ExtensionAttributeDefinition_name}

# Expression class attributes and methods

# bpmn2_FlowElementsContainer class attributes and methods

# GlobalTask class attributes and methods

# Choreography class attributes and methods

# CallableElement class attributes and methods

# Performer class attributes and methods

# LoopCharacteristics class attributes and methods

# ResourceRole class attributes and methods

# HumanPerformer class attributes and methods

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
        Property(name="bpmn2_Activity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot5", type=bpmn2_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adHocSubProcess6: BinaryAssociation = BinaryAssociation(
    name="adHocSubProcess6",
    ends={
        Property(name="bpmn2_AdHocSubProcess", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot7", type=bpmn2_AdHocSubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElement8: BinaryAssociation = BinaryAssociation(
    name="flowElement8",
    ends={
        Property(name="bpmn2_FlowElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot9", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifact10: BinaryAssociation = BinaryAssociation(
    name="artifact10",
    ends={
        Property(name="bpmn2_Artifact", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot11", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElementWithMixedContent20: BinaryAssociation = BinaryAssociation(
    name="baseElementWithMixedContent20",
    ends={
        Property(name="bpmn2_BaseElement22", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot21", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundaryEvent23: BinaryAssociation = BinaryAssociation(
    name="boundaryEvent23",
    ends={
        Property(name="bpmn2_BoundaryEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot24", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessRuleTask25: BinaryAssociation = BinaryAssociation(
    name="businessRuleTask25",
    ends={
        Property(name="bpmn2_BusinessRuleTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot26", type=bpmn2_BusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callableElement27: BinaryAssociation = BinaryAssociation(
    name="callableElement27",
    ends={
        Property(name="bpmn2_CallableElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot28", type=bpmn2_CallableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callActivity29: BinaryAssociation = BinaryAssociation(
    name="callActivity29",
    ends={
        Property(name="bpmn2_CallActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot30", type=bpmn2_CallActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callChoreography31: BinaryAssociation = BinaryAssociation(
    name="callChoreography31",
    ends={
        Property(name="bpmn2_CallChoreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot32", type=bpmn2_CallChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callConversation33: BinaryAssociation = BinaryAssociation(
    name="callConversation33",
    ends={
        Property(name="bpmn2_CallConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot34", type=bpmn2_CallConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNode35: BinaryAssociation = BinaryAssociation(
    name="conversationNode35",
    ends={
        Property(name="bpmn2_ConversationNode", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot36", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancelEventDefinition37: BinaryAssociation = BinaryAssociation(
    name="cancelEventDefinition37",
    ends={
        Property(name="bpmn2_CancelEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot38", type=bpmn2_CancelEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinition39: BinaryAssociation = BinaryAssociation(
    name="eventDefinition39",
    ends={
        Property(name="bpmn2_EventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot40", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElement41: BinaryAssociation = BinaryAssociation(
    name="rootElement41",
    ends={
        Property(name="bpmn2_RootElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot42", type=bpmn2_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment12: BinaryAssociation = BinaryAssociation(
    name="assignment12",
    ends={
        Property(name="bpmn2_Assignment", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot13", type=bpmn2_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association14: BinaryAssociation = BinaryAssociation(
    name="association14",
    ends={
        Property(name="bpmn2_Association", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot15", type=bpmn2_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing16: BinaryAssociation = BinaryAssociation(
    name="auditing16",
    ends={
        Property(name="bpmn2_Auditing", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot17", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseElement18: BinaryAssociation = BinaryAssociation(
    name="baseElement18",
    ends={
        Property(name="bpmn2_BaseElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot19", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyActivity53: BinaryAssociation = BinaryAssociation(
    name="choreographyActivity53",
    ends={
        Property(name="bpmn2_DocumentRoot54", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="bpmn2_ChoreographyActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
dataInputAssociation85: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation85",
    ends={
        Property(name="bpmn2_DataInputAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot86", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyTask55: BinaryAssociation = BinaryAssociation(
    name="choreographyTask55",
    ends={
        Property(name="bpmn2_ChoreographyTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot56", type=bpmn2_ChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObject87: BinaryAssociation = BinaryAssociation(
    name="dataObject87",
    ends={
        Property(name="bpmn2_DataObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot88", type=bpmn2_DataObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compensateEventDefinition57: BinaryAssociation = BinaryAssociation(
    name="compensateEventDefinition57",
    ends={
        Property(name="bpmn2_CompensateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot58", type=bpmn2_CompensateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjectReference89: BinaryAssociation = BinaryAssociation(
    name="dataObjectReference89",
    ends={
        Property(name="bpmn2_DataObjectReference", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot90", type=bpmn2_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexBehaviorDefinition59: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition59",
    ends={
        Property(name="bpmn2_ComplexBehaviorDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot60", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutput91: BinaryAssociation = BinaryAssociation(
    name="dataOutput91",
    ends={
        Property(name="bpmn2_DataOutput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot92", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexGateway61: BinaryAssociation = BinaryAssociation(
    name="complexGateway61",
    ends={
        Property(name="bpmn2_ComplexGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot62", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalEventDefinition63: BinaryAssociation = BinaryAssociation(
    name="conditionalEventDefinition63",
    ends={
        Property(name="bpmn2_ConditionalEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot64", type=bpmn2_ConditionalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversation65: BinaryAssociation = BinaryAssociation(
    name="conversation65",
    ends={
        Property(name="bpmn2_Conversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot66", type=bpmn2_Conversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociation67: BinaryAssociation = BinaryAssociation(
    name="conversationAssociation67",
    ends={
        Property(name="bpmn2_ConversationAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot68", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationLink69: BinaryAssociation = BinaryAssociation(
    name="conversationLink69",
    ends={
        Property(name="bpmn2_ConversationLink", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot70", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationKey71: BinaryAssociation = BinaryAssociation(
    name="correlationKey71",
    ends={
        Property(name="bpmn2_CorrelationKey", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot72", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationProperty73: BinaryAssociation = BinaryAssociation(
    name="correlationProperty73",
    ends={
        Property(name="bpmn2_CorrelationProperty", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot74", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyBinding75: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding75",
    ends={
        Property(name="bpmn2_CorrelationPropertyBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot76", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchEvent43: BinaryAssociation = BinaryAssociation(
    name="catchEvent43",
    ends={
        Property(name="bpmn2_CatchEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot44", type=bpmn2_CatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category45: BinaryAssociation = BinaryAssociation(
    name="category45",
    ends={
        Property(name="bpmn2_Category", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot46", type=bpmn2_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRetrievalExpression77: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression77",
    ends={
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot78", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValue47: BinaryAssociation = BinaryAssociation(
    name="categoryValue47",
    ends={
        Property(name="bpmn2_CategoryValue", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot48", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscription79: BinaryAssociation = BinaryAssociation(
    name="correlationSubscription79",
    ends={
        Property(name="bpmn2_CorrelationSubscription", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot80", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreography49: BinaryAssociation = BinaryAssociation(
    name="choreography49",
    ends={
        Property(name="bpmn2_Choreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot50", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataAssociation81: BinaryAssociation = BinaryAssociation(
    name="dataAssociation81",
    ends={
        Property(name="bpmn2_DataAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot82", type=bpmn2_DataAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration51: BinaryAssociation = BinaryAssociation(
    name="collaboration51",
    ends={
        Property(name="bpmn2_Collaboration", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot52", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInput83: BinaryAssociation = BinaryAssociation(
    name="dataInput83",
    ends={
        Property(name="bpmn2_DataInput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot84", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error109: BinaryAssociation = BinaryAssociation(
    name="error109",
    ends={
        Property(name="bpmn2_Error", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot110", type=bpmn2_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
errorEventDefinition111: BinaryAssociation = BinaryAssociation(
    name="errorEventDefinition111",
    ends={
        Property(name="bpmn2_ErrorEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot112", type=bpmn2_ErrorEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalation113: BinaryAssociation = BinaryAssociation(
    name="escalation113",
    ends={
        Property(name="bpmn2_Escalation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot114", type=bpmn2_Escalation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
escalationEventDefinition115: BinaryAssociation = BinaryAssociation(
    name="escalationEventDefinition115",
    ends={
        Property(name="bpmn2_EscalationEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot116", type=bpmn2_EscalationEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociation93: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation93",
    ends={
        Property(name="bpmn2_DataOutputAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot94", type=bpmn2_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataState95: BinaryAssociation = BinaryAssociation(
    name="dataState95",
    ends={
        Property(name="bpmn2_DataState", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot96", type=bpmn2_DataState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStore97: BinaryAssociation = BinaryAssociation(
    name="dataStore97",
    ends={
        Property(name="bpmn2_DataStore", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot98", type=bpmn2_DataStore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStoreReference99: BinaryAssociation = BinaryAssociation(
    name="dataStoreReference99",
    ends={
        Property(name="bpmn2_DataStoreReference", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot100", type=bpmn2_DataStoreReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions101: BinaryAssociation = BinaryAssociation(
    name="definitions101",
    ends={
        Property(name="bpmn2_Definitions", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot102", type=bpmn2_Definitions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation103: BinaryAssociation = BinaryAssociation(
    name="documentation103",
    ends={
        Property(name="bpmn2_Documentation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot104", type=bpmn2_Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endEvent105: BinaryAssociation = BinaryAssociation(
    name="endEvent105",
    ends={
        Property(name="bpmn2_EndEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot106", type=bpmn2_EndEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoint107: BinaryAssociation = BinaryAssociation(
    name="endPoint107",
    ends={
        Property(name="bpmn2_EndPoint", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot108", type=bpmn2_EndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalExpression131: BinaryAssociation = BinaryAssociation(
    name="formalExpression131",
    ends={
        Property(name="bpmn2_FormalExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot132", type=bpmn2_FormalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gateway133: BinaryAssociation = BinaryAssociation(
    name="gateway133",
    ends={
        Property(name="bpmn2_Gateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot134", type=bpmn2_Gateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalBusinessRuleTask135: BinaryAssociation = BinaryAssociation(
    name="globalBusinessRuleTask135",
    ends={
        Property(name="bpmn2_GlobalBusinessRuleTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot136", type=bpmn2_GlobalBusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalChoreographyTask137: BinaryAssociation = BinaryAssociation(
    name="globalChoreographyTask137",
    ends={
        Property(name="bpmn2_GlobalChoreographyTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot138", type=bpmn2_GlobalChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalConversation139: BinaryAssociation = BinaryAssociation(
    name="globalConversation139",
    ends={
        Property(name="bpmn2_GlobalConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot140", type=bpmn2_GlobalConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event117: BinaryAssociation = BinaryAssociation(
    name="event117",
    ends={
        Property(name="bpmn2_Event", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot118", type=bpmn2_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventBasedGateway119: BinaryAssociation = BinaryAssociation(
    name="eventBasedGateway119",
    ends={
        Property(name="bpmn2_EventBasedGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot120", type=bpmn2_EventBasedGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclusiveGateway121: BinaryAssociation = BinaryAssociation(
    name="exclusiveGateway121",
    ends={
        Property(name="bpmn2_ExclusiveGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot122", type=bpmn2_ExclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="bpmn2_Expression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot124", type=bpmn2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension125: BinaryAssociation = BinaryAssociation(
    name="extension125",
    ends={
        Property(name="bpmn2_Extension", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot126", type=bpmn2_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionElements127: BinaryAssociation = BinaryAssociation(
    name="extensionElements127",
    ends={
        Property(name="bpmn2_ExtensionAttributeValue", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot128", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowNode129: BinaryAssociation = BinaryAssociation(
    name="flowNode129",
    ends={
        Property(name="bpmn2_FlowNode", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot130", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRole155: BinaryAssociation = BinaryAssociation(
    name="resourceRole155",
    ends={
        Property(name="bpmn2_ResourceRole", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot156", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitThrowEvent157: BinaryAssociation = BinaryAssociation(
    name="implicitThrowEvent157",
    ends={
        Property(name="bpmn2_ImplicitThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot158", type=bpmn2_ImplicitThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import159: BinaryAssociation = BinaryAssociation(
    name="import159",
    ends={
        Property(name="bpmn2_Import", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot160", type=bpmn2_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inclusiveGateway161: BinaryAssociation = BinaryAssociation(
    name="inclusiveGateway161",
    ends={
        Property(name="bpmn2_InclusiveGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot162", type=bpmn2_InclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalManualTask141: BinaryAssociation = BinaryAssociation(
    name="globalManualTask141",
    ends={
        Property(name="bpmn2_GlobalManualTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot142", type=bpmn2_GlobalManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalScriptTask143: BinaryAssociation = BinaryAssociation(
    name="globalScriptTask143",
    ends={
        Property(name="bpmn2_GlobalScriptTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot144", type=bpmn2_GlobalScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalTask145: BinaryAssociation = BinaryAssociation(
    name="globalTask145",
    ends={
        Property(name="bpmn2_GlobalTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot146", type=bpmn2_GlobalTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalUserTask147: BinaryAssociation = BinaryAssociation(
    name="globalUserTask147",
    ends={
        Property(name="bpmn2_GlobalUserTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot148", type=bpmn2_GlobalUserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group149: BinaryAssociation = BinaryAssociation(
    name="group149",
    ends={
        Property(name="bpmn2_Group", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot150", type=bpmn2_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
humanPerformer151: BinaryAssociation = BinaryAssociation(
    name="humanPerformer151",
    ends={
        Property(name="bpmn2_HumanPerformer", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot152", type=bpmn2_HumanPerformer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performer153: BinaryAssociation = BinaryAssociation(
    name="performer153",
    ends={
        Property(name="bpmn2_Performer", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot154", type=bpmn2_Performer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification173: BinaryAssociation = BinaryAssociation(
    name="ioSpecification173",
    ends={
        Property(name="bpmn2_InputOutputSpecification", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot174", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemDefinition175: BinaryAssociation = BinaryAssociation(
    name="itemDefinition175",
    ends={
        Property(name="bpmn2_ItemDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot176", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lane177: BinaryAssociation = BinaryAssociation(
    name="lane177",
    ends={
        Property(name="bpmn2_Lane", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot178", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet163: BinaryAssociation = BinaryAssociation(
    name="inputSet163",
    ends={
        Property(name="bpmn2_InputSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot164", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface165: BinaryAssociation = BinaryAssociation(
    name="interface165",
    ends={
        Property(name="bpmn2_Interface", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot166", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateCatchEvent167: BinaryAssociation = BinaryAssociation(
    name="intermediateCatchEvent167",
    ends={
        Property(name="bpmn2_IntermediateCatchEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot168", type=bpmn2_IntermediateCatchEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateThrowEvent169: BinaryAssociation = BinaryAssociation(
    name="intermediateThrowEvent169",
    ends={
        Property(name="bpmn2_IntermediateThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot170", type=bpmn2_IntermediateThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monitoring195: BinaryAssociation = BinaryAssociation(
    name="monitoring195",
    ends={
        Property(name="bpmn2_Monitoring", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot196", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioBinding171: BinaryAssociation = BinaryAssociation(
    name="ioBinding171",
    ends={
        Property(name="bpmn2_InputOutputBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot172", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiInstanceLoopCharacteristics197: BinaryAssociation = BinaryAssociation(
    name="multiInstanceLoopCharacteristics197",
    ends={
        Property(name="bpmn2_MultiInstanceLoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot198", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation199: BinaryAssociation = BinaryAssociation(
    name="operation199",
    ends={
        Property(name="bpmn2_Operation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot200", type=bpmn2_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laneSet179: BinaryAssociation = BinaryAssociation(
    name="laneSet179",
    ends={
        Property(name="bpmn2_LaneSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot180", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSet201: BinaryAssociation = BinaryAssociation(
    name="outputSet201",
    ends={
        Property(name="bpmn2_OutputSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot202", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkEventDefinition181: BinaryAssociation = BinaryAssociation(
    name="linkEventDefinition181",
    ends={
        Property(name="bpmn2_LinkEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot182", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCharacteristics183: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics183",
    ends={
        Property(name="bpmn2_LoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot184", type=bpmn2_LoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manualTask185: BinaryAssociation = BinaryAssociation(
    name="manualTask185",
    ends={
        Property(name="bpmn2_ManualTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot186", type=bpmn2_ManualTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message187: BinaryAssociation = BinaryAssociation(
    name="message187",
    ends={
        Property(name="bpmn2_Message", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot188", type=bpmn2_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageEventDefinition189: BinaryAssociation = BinaryAssociation(
    name="messageEventDefinition189",
    ends={
        Property(name="bpmn2_MessageEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot190", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlow191: BinaryAssociation = BinaryAssociation(
    name="messageFlow191",
    ends={
        Property(name="bpmn2_MessageFlow", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot192", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociation193: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociation193",
    ends={
        Property(name="bpmn2_MessageFlowAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot194", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process217: BinaryAssociation = BinaryAssociation(
    name="process217",
    ends={
        Property(name="bpmn2_Process", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot218", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property219: BinaryAssociation = BinaryAssociation(
    name="property219",
    ends={
        Property(name="bpmn2_Property", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot220", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiveTask221: BinaryAssociation = BinaryAssociation(
    name="receiveTask221",
    ends={
        Property(name="bpmn2_ReceiveTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot222", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship223: BinaryAssociation = BinaryAssociation(
    name="relationship223",
    ends={
        Property(name="bpmn2_Relationship", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot224", type=bpmn2_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallelGateway203: BinaryAssociation = BinaryAssociation(
    name="parallelGateway203",
    ends={
        Property(name="bpmn2_ParallelGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot204", type=bpmn2_ParallelGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant205: BinaryAssociation = BinaryAssociation(
    name="participant205",
    ends={
        Property(name="bpmn2_Participant", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot206", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantAssociation207: BinaryAssociation = BinaryAssociation(
    name="participantAssociation207",
    ends={
        Property(name="bpmn2_ParticipantAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot208", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantMultiplicity209: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity209",
    ends={
        Property(name="bpmn2_ParticipantMultiplicity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot210", type=bpmn2_ParticipantMultiplicity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerEntity211: BinaryAssociation = BinaryAssociation(
    name="partnerEntity211",
    ends={
        Property(name="bpmn2_PartnerEntity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot212", type=bpmn2_PartnerEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerRole213: BinaryAssociation = BinaryAssociation(
    name="partnerRole213",
    ends={
        Property(name="bpmn2_PartnerRole", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot214", type=bpmn2_PartnerRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
potentialOwner215: BinaryAssociation = BinaryAssociation(
    name="potentialOwner215",
    ends={
        Property(name="bpmn2_PotentialOwner", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot216", type=bpmn2_PotentialOwner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script235: BinaryAssociation = BinaryAssociation(
    name="script235",
    ends={
        Property(name="bpmn2_EObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot236", type=bpmn2_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptTask237: BinaryAssociation = BinaryAssociation(
    name="scriptTask237",
    ends={
        Property(name="bpmn2_ScriptTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot238", type=bpmn2_ScriptTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sendTask239: BinaryAssociation = BinaryAssociation(
    name="sendTask239",
    ends={
        Property(name="bpmn2_SendTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot240", type=bpmn2_SendTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceFlow241: BinaryAssociation = BinaryAssociation(
    name="sequenceFlow241",
    ends={
        Property(name="bpmn2_SequenceFlow", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot242", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rendering225: BinaryAssociation = BinaryAssociation(
    name="rendering225",
    ends={
        Property(name="bpmn2_Rendering", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot226", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource227: BinaryAssociation = BinaryAssociation(
    name="resource227",
    ends={
        Property(name="bpmn2_Resource", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot228", type=bpmn2_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression229: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression229",
    ends={
        Property(name="bpmn2_ResourceAssignmentExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot230", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameter231: BinaryAssociation = BinaryAssociation(
    name="resourceParameter231",
    ends={
        Property(name="bpmn2_ResourceParameter", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot232", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceParameterBinding233: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBinding233",
    ends={
        Property(name="bpmn2_ResourceParameterBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot234", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subConversation255: BinaryAssociation = BinaryAssociation(
    name="subConversation255",
    ends={
        Property(name="bpmn2_SubConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot256", type=bpmn2_SubConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcess257: BinaryAssociation = BinaryAssociation(
    name="subProcess257",
    ends={
        Property(name="bpmn2_SubProcess", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot258", type=bpmn2_SubProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task259: BinaryAssociation = BinaryAssociation(
    name="task259",
    ends={
        Property(name="bpmn2_Task", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot260", type=bpmn2_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceTask243: BinaryAssociation = BinaryAssociation(
    name="serviceTask243",
    ends={
        Property(name="bpmn2_ServiceTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot244", type=bpmn2_ServiceTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal245: BinaryAssociation = BinaryAssociation(
    name="signal245",
    ends={
        Property(name="bpmn2_Signal", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot246", type=bpmn2_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalEventDefinition247: BinaryAssociation = BinaryAssociation(
    name="signalEventDefinition247",
    ends={
        Property(name="bpmn2_SignalEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot248", type=bpmn2_SignalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
standardLoopCharacteristics249: BinaryAssociation = BinaryAssociation(
    name="standardLoopCharacteristics249",
    ends={
        Property(name="bpmn2_StandardLoopCharacteristics", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot250", type=bpmn2_StandardLoopCharacteristics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startEvent251: BinaryAssociation = BinaryAssociation(
    name="startEvent251",
    ends={
        Property(name="bpmn2_StartEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot252", type=bpmn2_StartEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subChoreography253: BinaryAssociation = BinaryAssociation(
    name="subChoreography253",
    ends={
        Property(name="bpmn2_SubChoreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot254", type=bpmn2_SubChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transaction272: BinaryAssociation = BinaryAssociation(
    name="transaction272",
    ends={
        Property(name="bpmn2_Transaction", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot273", type=bpmn2_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userTask274: BinaryAssociation = BinaryAssociation(
    name="userTask274",
    ends={
        Property(name="bpmn2_UserTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot275", type=bpmn2_UserTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioSpecification276: BinaryAssociation = BinaryAssociation(
    name="ioSpecification276",
    ends={
        Property(name="bpmn2_InputOutputSpecification278", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity277", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundaryEventRefs279: BinaryAssociation = BinaryAssociation(
    name="boundaryEventRefs279",
    ends={
        Property(name="BoundaryEvent", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="attachedToRef", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(0, 9999))
    }
)
terminateEventDefinition261: BinaryAssociation = BinaryAssociation(
    name="terminateEventDefinition261",
    ends={
        Property(name="bpmn2_TerminateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot262", type=bpmn2_TerminateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="bpmn2_TextAnnotation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot267", type=bpmn2_TextAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throwEvent268: BinaryAssociation = BinaryAssociation(
    name="throwEvent268",
    ends={
        Property(name="bpmn2_ThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot269", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timerEventDefinition270: BinaryAssociation = BinaryAssociation(
    name="timerEventDefinition270",
    ends={
        Property(name="bpmn2_TimerEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot271", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isPerformedBy307: BinaryAssociation = BinaryAssociation(
    name="isPerformedBy307",
    ends={
        Property(name="bpmn2_Performer309", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity308", type=bpmn2_Performer, multiplicity=Multiplicity(0, 9999))
    }
)
isPerformedByPosition310: BinaryAssociation = BinaryAssociation(
    name="isPerformedByPosition310",
    ends={
        Property(name="bpmn2_Position", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity311", type=bpmn2_Position, multiplicity=Multiplicity(0, 9999))
    }
)
isPerformedByRole312: BinaryAssociation = BinaryAssociation(
    name="isPerformedByRole312",
    ends={
        Property(name="bpmn2_Role", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity313", type=bpmn2_Role, multiplicity=Multiplicity(0, 9999))
    }
)
competency314: BinaryAssociation = BinaryAssociation(
    name="competency314",
    ends={
        Property(name="bpmn2_Competency316", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity315", type=bpmn2_Competency, multiplicity=Multiplicity(0, 9999))
    }
)
completionCondition317: BinaryAssociation = BinaryAssociation(
    name="completionCondition317",
    ends={
        Property(name="bpmn2_Expression319", type=bpmn2_AdHocSubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_AdHocSubProcess318", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
properties280: BinaryAssociation = BinaryAssociation(
    name="properties280",
    ends={
        Property(name="bpmn2_Property282", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity281", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociations283: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociations283",
    ends={
        Property(name="bpmn2_DataInputAssociation285", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity284", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociations286: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociations286",
    ends={
        Property(name="bpmn2_DataOutputAssociation288", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity287", type=bpmn2_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources289: BinaryAssociation = BinaryAssociation(
    name="resources289",
    ends={
        Property(name="bpmn2_ResourceRole291", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity290", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopCharacteristics292: BinaryAssociation = BinaryAssociation(
    name="loopCharacteristics292",
    ends={
        Property(name="bpmn2_LoopCharacteristics294", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity293", type=bpmn2_LoopCharacteristics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default295: BinaryAssociation = BinaryAssociation(
    name="default295",
    ends={
        Property(name="bpmn2_SequenceFlow297", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity296", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
requiresCompetency298: BinaryAssociation = BinaryAssociation(
    name="requiresCompetency298",
    ends={
        Property(name="bpmn2_Competency", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity299", type=bpmn2_Competency, multiplicity=Multiplicity(0, 9999))
    }
)
isMeasuredByCriterion300: BinaryAssociation = BinaryAssociation(
    name="isMeasuredByCriterion300",
    ends={
        Property(name="bpmn2_Criterion", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity301", type=bpmn2_Criterion, multiplicity=Multiplicity(0, 9999))
    }
)
isPerformedByOrganisationalUnit302: BinaryAssociation = BinaryAssociation(
    name="isPerformedByOrganisationalUnit302",
    ends={
        Property(name="bpmn2_OrganisationalUnit", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity303", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isResponsibleByOrganisationalUnit304: BinaryAssociation = BinaryAssociation(
    name="isResponsibleByOrganisationalUnit304",
    ends={
        Property(name="bpmn2_OrganisationalUnit306", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Activity305", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
attachedToRef340: BinaryAssociation = BinaryAssociation(
    name="attachedToRef340",
    ends={
        Property(name="Activity", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="boundaryEventRefs", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1))
    }
)
calledElementRef341: BinaryAssociation = BinaryAssociation(
    name="calledElementRef341",
    ends={
        Property(name="bpmn2_CallableElement343", type=bpmn2_CallActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallActivity342", type=bpmn2_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
participantAssociations344: BinaryAssociation = BinaryAssociation(
    name="participantAssociations344",
    ends={
        Property(name="bpmn2_ParticipantAssociation346", type=bpmn2_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallChoreography345", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledChoreographyRef347: BinaryAssociation = BinaryAssociation(
    name="calledChoreographyRef347",
    ends={
        Property(name="bpmn2_Choreography349", type=bpmn2_CallChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallChoreography348", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 1))
    }
)
from320: BinaryAssociation = BinaryAssociation(
    name="from320",
    ends={
        Property(name="bpmn2_Expression322", type=bpmn2_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Assignment321", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to323: BinaryAssociation = BinaryAssociation(
    name="to323",
    ends={
        Property(name="bpmn2_Expression325", type=bpmn2_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Assignment324", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceRef326: BinaryAssociation = BinaryAssociation(
    name="sourceRef326",
    ends={
        Property(name="bpmn2_BaseElement328", type=bpmn2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Association327", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
targetRef329: BinaryAssociation = BinaryAssociation(
    name="targetRef329",
    ends={
        Property(name="bpmn2_BaseElement331", type=bpmn2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Association330", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1))
    }
)
extensionValues332: BinaryAssociation = BinaryAssociation(
    name="extensionValues332",
    ends={
        Property(name="bpmn2_ExtensionAttributeValue334", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement333", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation335: BinaryAssociation = BinaryAssociation(
    name="documentation335",
    ends={
        Property(name="bpmn2_Documentation337", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement336", type=bpmn2_Documentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefinitions338: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions338",
    ends={
        Property(name="bpmn2_ExtensionDefinition", type=bpmn2_BaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_BaseElement339", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
categoryValue380: BinaryAssociation = BinaryAssociation(
    name="categoryValue380",
    ends={
        Property(name="bpmn2_CategoryValue382", type=bpmn2_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Category381", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categorizedFlowElements383: BinaryAssociation = BinaryAssociation(
    name="categorizedFlowElements383",
    ends={
        Property(name="bpmn2_FlowElement385", type=bpmn2_CategoryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CategoryValue384", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999))
    }
)
participantRefs386: BinaryAssociation = BinaryAssociation(
    name="participantRefs386",
    ends={
        Property(name="bpmn2_Participant388", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity387", type=bpmn2_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
correlationKeys389: BinaryAssociation = BinaryAssociation(
    name="correlationKeys389",
    ends={
        Property(name="bpmn2_CorrelationKey391", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity390", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initiatingParticipantRef392: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef392",
    ends={
        Property(name="bpmn2_Participant394", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyActivity393", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
participantAssociations350: BinaryAssociation = BinaryAssociation(
    name="participantAssociations350",
    ends={
        Property(name="bpmn2_ParticipantAssociation352", type=bpmn2_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallConversation351", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledCollaborationRef353: BinaryAssociation = BinaryAssociation(
    name="calledCollaborationRef353",
    ends={
        Property(name="bpmn2_Collaboration355", type=bpmn2_CallConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallConversation354", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
supportedInterfaceRefs356: BinaryAssociation = BinaryAssociation(
    name="supportedInterfaceRefs356",
    ends={
        Property(name="bpmn2_Interface358", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement357", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ioSpecification359: BinaryAssociation = BinaryAssociation(
    name="ioSpecification359",
    ends={
        Property(name="bpmn2_InputOutputSpecification361", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement360", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ioBinding362: BinaryAssociation = BinaryAssociation(
    name="ioBinding362",
    ends={
        Property(name="bpmn2_InputOutputBinding364", type=bpmn2_CallableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CallableElement363", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs365: BinaryAssociation = BinaryAssociation(
    name="dataOutputs365",
    ends={
        Property(name="bpmn2_DataOutput367", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent366", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputAssociation368: BinaryAssociation = BinaryAssociation(
    name="dataOutputAssociation368",
    ends={
        Property(name="bpmn2_DataOutputAssociation370", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent369", type=bpmn2_DataOutputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputSet371: BinaryAssociation = BinaryAssociation(
    name="outputSet371",
    ends={
        Property(name="bpmn2_OutputSet373", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent372", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitions374: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions374",
    ends={
        Property(name="bpmn2_EventDefinition376", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent375", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitionRefs377: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs377",
    ends={
        Property(name="bpmn2_EventDefinition379", type=bpmn2_CatchEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CatchEvent378", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
choreographyRef422: BinaryAssociation = BinaryAssociation(
    name="choreographyRef422",
    ends={
        Property(name="bpmn2_Choreography424", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration423", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 9999))
    }
)
conversationLinks425: BinaryAssociation = BinaryAssociation(
    name="conversationLinks425",
    ends={
        Property(name="bpmn2_ConversationLink427", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration426", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityRef428: BinaryAssociation = BinaryAssociation(
    name="activityRef428",
    ends={
        Property(name="bpmn2_Activity430", type=bpmn2_CompensateEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CompensateEventDefinition429", type=bpmn2_Activity, multiplicity=Multiplicity(0, 1))
    }
)
messageFlowRef395: BinaryAssociation = BinaryAssociation(
    name="messageFlowRef395",
    ends={
        Property(name="bpmn2_MessageFlow397", type=bpmn2_ChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyTask396", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 2))
    }
)
participants398: BinaryAssociation = BinaryAssociation(
    name="participants398",
    ends={
        Property(name="bpmn2_Participant400", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration399", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlows401: BinaryAssociation = BinaryAssociation(
    name="messageFlows401",
    ends={
        Property(name="bpmn2_MessageFlow403", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration402", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts404: BinaryAssociation = BinaryAssociation(
    name="artifacts404",
    ends={
        Property(name="bpmn2_Artifact406", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration405", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversations407: BinaryAssociation = BinaryAssociation(
    name="conversations407",
    ends={
        Property(name="bpmn2_ConversationNode409", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration408", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationAssociations410: BinaryAssociation = BinaryAssociation(
    name="conversationAssociations410",
    ends={
        Property(name="bpmn2_ConversationAssociation412", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration411", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantAssociations413: BinaryAssociation = BinaryAssociation(
    name="participantAssociations413",
    ends={
        Property(name="bpmn2_ParticipantAssociation415", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration414", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowAssociations416: BinaryAssociation = BinaryAssociation(
    name="messageFlowAssociations416",
    ends={
        Property(name="bpmn2_MessageFlowAssociation418", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration417", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantRefs457: BinaryAssociation = BinaryAssociation(
    name="participantRefs457",
    ends={
        Property(name="bpmn2_Participant459", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode458", type=bpmn2_Participant, multiplicity=Multiplicity(2, 9999))
    }
)
correlationKeys419: BinaryAssociation = BinaryAssociation(
    name="correlationKeys419",
    ends={
        Property(name="bpmn2_CorrelationKey421", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration420", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageFlowRefs460: BinaryAssociation = BinaryAssociation(
    name="messageFlowRefs460",
    ends={
        Property(name="bpmn2_MessageFlow462", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode461", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999))
    }
)
correlationKeys463: BinaryAssociation = BinaryAssociation(
    name="correlationKeys463",
    ends={
        Property(name="bpmn2_CorrelationKey465", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode464", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRef466: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef466",
    ends={
        Property(name="bpmn2_CorrelationProperty468", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationKey467", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(0, 9999))
    }
)
correlationPropertyRetrievalExpression469: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression469",
    ends={
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression471", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationProperty470", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type472: BinaryAssociation = BinaryAssociation(
    name="type472",
    ends={
        Property(name="bpmn2_ItemDefinition474", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationProperty473", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
condition431: BinaryAssociation = BinaryAssociation(
    name="condition431",
    ends={
        Property(name="bpmn2_FormalExpression433", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexBehaviorDefinition432", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event434: BinaryAssociation = BinaryAssociation(
    name="event434",
    ends={
        Property(name="bpmn2_ImplicitThrowEvent436", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexBehaviorDefinition435", type=bpmn2_ImplicitThrowEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activationCondition437: BinaryAssociation = BinaryAssociation(
    name="activationCondition437",
    ends={
        Property(name="bpmn2_Expression439", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexGateway438", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default440: BinaryAssociation = BinaryAssociation(
    name="default440",
    ends={
        Property(name="bpmn2_SequenceFlow442", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ComplexGateway441", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
condition443: BinaryAssociation = BinaryAssociation(
    name="condition443",
    ends={
        Property(name="bpmn2_Expression445", type=bpmn2_ConditionalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConditionalEventDefinition444", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
innerConversationNodeRef446: BinaryAssociation = BinaryAssociation(
    name="innerConversationNodeRef446",
    ends={
        Property(name="bpmn2_ConversationNode448", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationAssociation447", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
outerConversationNodeRef449: BinaryAssociation = BinaryAssociation(
    name="outerConversationNodeRef449",
    ends={
        Property(name="bpmn2_ConversationNode451", type=bpmn2_ConversationAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationAssociation450", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef452: BinaryAssociation = BinaryAssociation(
    name="sourceRef452",
    ends={
        Property(name="bpmn2_InteractionNode", type=bpmn2_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationLink453", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef454: BinaryAssociation = BinaryAssociation(
    name="targetRef454",
    ends={
        Property(name="bpmn2_InteractionNode456", type=bpmn2_ConversationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationLink455", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
correlationKeyRef490: BinaryAssociation = BinaryAssociation(
    name="correlationKeyRef490",
    ends={
        Property(name="bpmn2_CorrelationKey492", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationSubscription491", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(1, 1))
    }
)
sourceRef493: BinaryAssociation = BinaryAssociation(
    name="sourceRef493",
    ends={
        Property(name="bpmn2_ItemAwareElement", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation494", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 9999))
    }
)
targetRef495: BinaryAssociation = BinaryAssociation(
    name="targetRef495",
    ends={
        Property(name="bpmn2_ItemAwareElement497", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation496", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1))
    }
)
transformation498: BinaryAssociation = BinaryAssociation(
    name="transformation498",
    ends={
        Property(name="bpmn2_FormalExpression500", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation499", type=bpmn2_FormalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment501: BinaryAssociation = BinaryAssociation(
    name="assignment501",
    ends={
        Property(name="bpmn2_Assignment503", type=bpmn2_DataAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataAssociation502", type=bpmn2_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSetWithOptional504: BinaryAssociation = BinaryAssociation(
    name="inputSetWithOptional504",
    ends={
        Property(name="InputSet", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
dataPath475: BinaryAssociation = BinaryAssociation(
    name="dataPath475",
    ends={
        Property(name="bpmn2_FormalExpression477", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyBinding476", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
correlationPropertyRef478: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRef478",
    ends={
        Property(name="bpmn2_CorrelationProperty480", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyBinding479", type=bpmn2_CorrelationProperty, multiplicity=Multiplicity(1, 1))
    }
)
messagePath481: BinaryAssociation = BinaryAssociation(
    name="messagePath481",
    ends={
        Property(name="bpmn2_FormalExpression483", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression482", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageRef484: BinaryAssociation = BinaryAssociation(
    name="messageRef484",
    ends={
        Property(name="bpmn2_Message486", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression485", type=bpmn2_Message, multiplicity=Multiplicity(1, 1))
    }
)
correlationPropertyBinding487: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyBinding487",
    ends={
        Property(name="bpmn2_CorrelationPropertyBinding489", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationSubscription488", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencesDocument518: BinaryAssociation = BinaryAssociation(
    name="referencesDocument518",
    ends={
        Property(name="..520", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="documentAndKnowledge519", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
dataStoreRef521: BinaryAssociation = BinaryAssociation(
    name="dataStoreRef521",
    ends={
        Property(name="bpmn2_DataStore523", type=bpmn2_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataStoreReference522", type=bpmn2_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
imports524: BinaryAssociation = BinaryAssociation(
    name="imports524",
    ends={
        Property(name="bpmn2_Import526", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions525", type=bpmn2_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions527: BinaryAssociation = BinaryAssociation(
    name="extensions527",
    ends={
        Property(name="bpmn2_Extension529", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions528", type=bpmn2_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSetWithWhileExecuting505: BinaryAssociation = BinaryAssociation(
    name="inputSetWithWhileExecuting505",
    ends={
        Property(name="InputSet506", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs507: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs507",
    ends={
        Property(name="InputSet508", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInputRefs", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 9999))
    }
)
referencesDocument509: BinaryAssociation = BinaryAssociation(
    name="referencesDocument509",
    ends={
        Property(name="..", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="documentAndKnowledge", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
dataObjectRef510: BinaryAssociation = BinaryAssociation(
    name="dataObjectRef510",
    ends={
        Property(name="bpmn2_DataObject512", type=bpmn2_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataObjectReference511", type=bpmn2_DataObject, multiplicity=Multiplicity(1, 1))
    }
)
outputSetWithOptional513: BinaryAssociation = BinaryAssociation(
    name="outputSetWithOptional513",
    ends={
        Property(name="OutputSet", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetWithWhileExecuting514: BinaryAssociation = BinaryAssociation(
    name="outputSetWithWhileExecuting514",
    ends={
        Property(name="OutputSet515", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="whileExecutingOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs516: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs516",
    ends={
        Property(name="OutputSet517", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutputRefs", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 9999))
    }
)
structureRef544: BinaryAssociation = BinaryAssociation(
    name="structureRef544",
    ends={
        Property(name="bpmn2_ItemDefinition546", type=bpmn2_Escalation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Escalation545", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
escalationRef547: BinaryAssociation = BinaryAssociation(
    name="escalationRef547",
    ends={
        Property(name="bpmn2_Escalation549", type=bpmn2_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_EscalationEventDefinition548", type=bpmn2_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
properties550: BinaryAssociation = BinaryAssociation(
    name="properties550",
    ends={
        Property(name="bpmn2_Property552", type=bpmn2_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Event551", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElements530: BinaryAssociation = BinaryAssociation(
    name="rootElements530",
    ends={
        Property(name="bpmn2_RootElement532", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions531", type=bpmn2_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams533: BinaryAssociation = BinaryAssociation(
    name="diagrams533",
    ends={
        Property(name="bpmn2_BPMNDiagram", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions534", type=bpmn2_BPMNDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships535: BinaryAssociation = BinaryAssociation(
    name="relationships535",
    ends={
        Property(name="bpmn2_Relationship537", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions536", type=bpmn2_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structureRef538: BinaryAssociation = BinaryAssociation(
    name="structureRef538",
    ends={
        Property(name="bpmn2_ItemDefinition540", type=bpmn2_Error, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Error539", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
errorRef541: BinaryAssociation = BinaryAssociation(
    name="errorRef541",
    ends={
        Property(name="bpmn2_Error543", type=bpmn2_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ErrorEventDefinition542", type=bpmn2_Error, multiplicity=Multiplicity(0, 1))
    }
)
extensionDefinition559: BinaryAssociation = BinaryAssociation(
    name="extensionDefinition559",
    ends={
        Property(name="ExtensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionAttributeDefinitions", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
valueRef560: BinaryAssociation = BinaryAssociation(
    name="valueRef560",
    ends={
        Property(name="bpmn2_EObject562", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue561", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
extensionAttributeDefinition563: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition563",
    ends={
        Property(name="bpmn2_ExtensionAttributeDefinition", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue564", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
default553: BinaryAssociation = BinaryAssociation(
    name="default553",
    ends={
        Property(name="bpmn2_SequenceFlow555", type=bpmn2_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExclusiveGateway554", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
definition556: BinaryAssociation = BinaryAssociation(
    name="definition556",
    ends={
        Property(name="bpmn2_ExtensionDefinition558", type=bpmn2_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Extension557", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outgoing582: BinaryAssociation = BinaryAssociation(
    name="outgoing582",
    ends={
        Property(name="SequenceFlow583", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
evaluatesToTypeRef584: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef584",
    ends={
        Property(name="bpmn2_ItemDefinition586", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FormalExpression585", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
extensionAttributeDefinitions565: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions565",
    ends={
        Property(name="ExtensionAttributeDefinition", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing566: BinaryAssociation = BinaryAssociation(
    name="auditing566",
    ends={
        Property(name="bpmn2_Auditing568", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement567", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring569: BinaryAssociation = BinaryAssociation(
    name="monitoring569",
    ends={
        Property(name="bpmn2_Monitoring571", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement570", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
categoryValueRef572: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef572",
    ends={
        Property(name="bpmn2_CategoryValue574", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement573", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999))
    }
)
laneSets575: BinaryAssociation = BinaryAssociation(
    name="laneSets575",
    ends={
        Property(name="bpmn2_LaneSet576", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElements577: BinaryAssociation = BinaryAssociation(
    name="flowElements577",
    ends={
        Property(name="bpmn2_FlowElement579", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer578", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming580: BinaryAssociation = BinaryAssociation(
    name="incoming580",
    ends={
        Property(name="SequenceFlow", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
lanes581: BinaryAssociation = BinaryAssociation(
    name="lanes581",
    ends={
        Property(name="Lane", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="flowNodeRefs", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputs611: BinaryAssociation = BinaryAssociation(
    name="dataInputs611",
    ends={
        Property(name="bpmn2_DataInput613", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification612", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initiatingParticipantRef587: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef587",
    ends={
        Property(name="bpmn2_Participant589", type=bpmn2_GlobalChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalChoreographyTask588", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
dataOutputs614: BinaryAssociation = BinaryAssociation(
    name="dataOutputs614",
    ends={
        Property(name="bpmn2_DataOutput616", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification615", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSets617: BinaryAssociation = BinaryAssociation(
    name="inputSets617",
    ends={
        Property(name="bpmn2_InputSet619", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification618", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputSets620: BinaryAssociation = BinaryAssociation(
    name="outputSets620",
    ends={
        Property(name="bpmn2_OutputSet622", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification621", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataInputRefs623: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs623",
    ends={
        Property(name="DataInput", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
resources590: BinaryAssociation = BinaryAssociation(
    name="resources590",
    ends={
        Property(name="bpmn2_ResourceRole592", type=bpmn2_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalTask591", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renderings593: BinaryAssociation = BinaryAssociation(
    name="renderings593",
    ends={
        Property(name="bpmn2_Rendering595", type=bpmn2_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalUserTask594", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValueRef596: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef596",
    ends={
        Property(name="bpmn2_CategoryValue598", type=bpmn2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Group597", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
default599: BinaryAssociation = BinaryAssociation(
    name="default599",
    ends={
        Property(name="bpmn2_SequenceFlow601", type=bpmn2_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InclusiveGateway600", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef602: BinaryAssociation = BinaryAssociation(
    name="inputDataRef602",
    ends={
        Property(name="bpmn2_InputSet604", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding603", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef605: BinaryAssociation = BinaryAssociation(
    name="operationRef605",
    ends={
        Property(name="bpmn2_Operation607", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding606", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef608: BinaryAssociation = BinaryAssociation(
    name="outputDataRef608",
    ends={
        Property(name="bpmn2_OutputSet610", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding609", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
dataState643: BinaryAssociation = BinaryAssociation(
    name="dataState643",
    ends={
        Property(name="bpmn2_DataState645", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement644", type=bpmn2_DataState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemSubjectRef646: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef646",
    ends={
        Property(name="bpmn2_ItemDefinition648", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement647", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
import649: BinaryAssociation = BinaryAssociation(
    name="import649",
    ends={
        Property(name="bpmn2_Import651", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition650", type=bpmn2_Import, multiplicity=Multiplicity(0, 1))
    }
)
structureRef652: BinaryAssociation = BinaryAssociation(
    name="structureRef652",
    ends={
        Property(name="bpmn2_EObject654", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition653", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
optionalInputRefs624: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs624",
    ends={
        Property(name="DataInput625", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingInputRefs626: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs626",
    ends={
        Property(name="DataInput627", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs628: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs628",
    ends={
        Property(name="OutputSet630", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs629", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConversationLinks631: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks631",
    ends={
        Property(name="bpmn2_ConversationLink633", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InteractionNode632", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingConversationLinks634: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks634",
    ends={
        Property(name="bpmn2_ConversationLink636", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InteractionNode635", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
operations637: BinaryAssociation = BinaryAssociation(
    name="operations637",
    ends={
        Property(name="bpmn2_Operation639", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface638", type=bpmn2_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implementationRef640: BinaryAssociation = BinaryAssociation(
    name="implementationRef640",
    ends={
        Property(name="bpmn2_EObject642", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface641", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
partitionElementRef662: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef662",
    ends={
        Property(name="bpmn2_BaseElement664", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane663", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
representsPerformer665: BinaryAssociation = BinaryAssociation(
    name="representsPerformer665",
    ends={
        Property(name="bpmn2_Performer667", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane666", type=bpmn2_Performer, multiplicity=Multiplicity(0, 9999))
    }
)
representsRole668: BinaryAssociation = BinaryAssociation(
    name="representsRole668",
    ends={
        Property(name="bpmn2_Role670", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane669", type=bpmn2_Role, multiplicity=Multiplicity(0, 9999))
    }
)
representsOrganisationalUnit671: BinaryAssociation = BinaryAssociation(
    name="representsOrganisationalUnit671",
    ends={
        Property(name="bpmn2_OrganisationalUnit673", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane672", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
messages674: BinaryAssociation = BinaryAssociation(
    name="messages674",
    ends={
        Property(name="bpmn2_MessageFlow676", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet675", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lanes677: BinaryAssociation = BinaryAssociation(
    name="lanes677",
    ends={
        Property(name="bpmn2_Lane679", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet678", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partitionElement655: BinaryAssociation = BinaryAssociation(
    name="partitionElement655",
    ends={
        Property(name="bpmn2_BaseElement657", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane656", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowNodeRefs658: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs658",
    ends={
        Property(name="FlowNode", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 9999))
    }
)
childLaneSet659: BinaryAssociation = BinaryAssociation(
    name="childLaneSet659",
    ends={
        Property(name="bpmn2_LaneSet661", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane660", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetRef703: BinaryAssociation = BinaryAssociation(
    name="targetRef703",
    ends={
        Property(name="bpmn2_InteractionNode705", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow704", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef706: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef706",
    ends={
        Property(name="bpmn2_MessageFlow708", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation707", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef709: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef709",
    ends={
        Property(name="bpmn2_MessageFlow711", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation710", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
representsOrganisationalUnit680: BinaryAssociation = BinaryAssociation(
    name="representsOrganisationalUnit680",
    ends={
        Property(name="bpmn2_OrganisationalUnit682", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet681", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
source684: BinaryAssociation = BinaryAssociation(
    name="source684",
    ends={
        Property(name="LinkEventDefinition", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
target686: BinaryAssociation = BinaryAssociation(
    name="target686",
    ends={
        Property(name="LinkEventDefinition687", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
itemRef688: BinaryAssociation = BinaryAssociation(
    name="itemRef688",
    ends={
        Property(name="bpmn2_ItemDefinition690", type=bpmn2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Message689", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operationRef691: BinaryAssociation = BinaryAssociation(
    name="operationRef691",
    ends={
        Property(name="bpmn2_Operation693", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition692", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef694: BinaryAssociation = BinaryAssociation(
    name="messageRef694",
    ends={
        Property(name="bpmn2_Message696", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition695", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
errorRefs745: BinaryAssociation = BinaryAssociation(
    name="errorRefs745",
    ends={
        Property(name="bpmn2_Error747", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation746", type=bpmn2_Error, multiplicity=Multiplicity(0, 9999))
    }
)
messageRef697: BinaryAssociation = BinaryAssociation(
    name="messageRef697",
    ends={
        Property(name="bpmn2_Message699", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow698", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
implementationRef748: BinaryAssociation = BinaryAssociation(
    name="implementationRef748",
    ends={
        Property(name="bpmn2_EObject750", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation749", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef700: BinaryAssociation = BinaryAssociation(
    name="sourceRef700",
    ends={
        Property(name="bpmn2_InteractionNode702", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow701", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
dataOutputRefs751: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs751",
    ends={
        Property(name="DataOutput", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
optionalOutputRefs752: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs752",
    ends={
        Property(name="DataOutput753", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithOptional", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingOutputRefs754: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs754",
    ends={
        Property(name="DataOutput755", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithWhileExecuting", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs756: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs756",
    ends={
        Property(name="InputSet758", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs757", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
loopCardinality712: BinaryAssociation = BinaryAssociation(
    name="loopCardinality712",
    ends={
        Property(name="bpmn2_Expression714", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics713", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopDataInputRef715: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef715",
    ends={
        Property(name="bpmn2_ItemAwareElement717", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics716", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef718: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef718",
    ends={
        Property(name="bpmn2_ItemAwareElement720", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics719", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
inputDataItem721: BinaryAssociation = BinaryAssociation(
    name="inputDataItem721",
    ends={
        Property(name="bpmn2_DataInput723", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics722", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputDataItem724: BinaryAssociation = BinaryAssociation(
    name="outputDataItem724",
    ends={
        Property(name="bpmn2_DataOutput726", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics725", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complexBehaviorDefinition727: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition727",
    ends={
        Property(name="bpmn2_ComplexBehaviorDefinition729", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics728", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completionCondition730: BinaryAssociation = BinaryAssociation(
    name="completionCondition730",
    ends={
        Property(name="bpmn2_Expression732", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics731", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noneBehaviorEventRef733: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef733",
    ends={
        Property(name="bpmn2_EventDefinition735", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics734", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oneBehaviorEventRef736: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef736",
    ends={
        Property(name="bpmn2_EventDefinition738", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics737", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef739: BinaryAssociation = BinaryAssociation(
    name="inMessageRef739",
    ends={
        Property(name="bpmn2_Message741", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation740", type=bpmn2_Message, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef742: BinaryAssociation = BinaryAssociation(
    name="outMessageRef742",
    ends={
        Property(name="bpmn2_Message744", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation743", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
participantMultiplicity765: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity765",
    ends={
        Property(name="bpmn2_ParticipantMultiplicity767", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant766", type=bpmn2_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processRef768: BinaryAssociation = BinaryAssociation(
    name="processRef768",
    ends={
        Property(name="bpmn2_Process770", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant769", type=bpmn2_Process, multiplicity=Multiplicity(0, 1))
    }
)
innerParticipantRef771: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef771",
    ends={
        Property(name="bpmn2_Participant773", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation772", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef774: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef774",
    ends={
        Property(name="bpmn2_Participant776", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation775", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRefs759: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs759",
    ends={
        Property(name="bpmn2_Interface761", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant760", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
endPointRefs762: BinaryAssociation = BinaryAssociation(
    name="endPointRefs762",
    ends={
        Property(name="bpmn2_EndPoint764", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant763", type=bpmn2_EndPoint, multiplicity=Multiplicity(0, 9999))
    }
)
messageRef807: BinaryAssociation = BinaryAssociation(
    name="messageRef807",
    ends={
        Property(name="bpmn2_Message809", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask808", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef810: BinaryAssociation = BinaryAssociation(
    name="operationRef810",
    ends={
        Property(name="bpmn2_Operation812", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask811", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
participantRef777: BinaryAssociation = BinaryAssociation(
    name="participantRef777",
    ends={
        Property(name="bpmn2_Participant779", type=bpmn2_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerEntity778", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
participantRef780: BinaryAssociation = BinaryAssociation(
    name="participantRef780",
    ends={
        Property(name="bpmn2_Participant782", type=bpmn2_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerRole781", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
auditing783: BinaryAssociation = BinaryAssociation(
    name="auditing783",
    ends={
        Property(name="bpmn2_Auditing785", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process784", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring786: BinaryAssociation = BinaryAssociation(
    name="monitoring786",
    ends={
        Property(name="bpmn2_Monitoring788", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process787", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties789: BinaryAssociation = BinaryAssociation(
    name="properties789",
    ends={
        Property(name="bpmn2_Property791", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process790", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts792: BinaryAssociation = BinaryAssociation(
    name="artifacts792",
    ends={
        Property(name="bpmn2_Artifact794", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process793", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources795: BinaryAssociation = BinaryAssociation(
    name="resources795",
    ends={
        Property(name="bpmn2_ResourceRole797", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process796", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscriptions798: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions798",
    ends={
        Property(name="bpmn2_CorrelationSubscription800", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process799", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports802: BinaryAssociation = BinaryAssociation(
    name="supports802",
    ends={
        Property(name="bpmn2_Process803", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process801", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999))
    }
)
definitionalCollaborationRef804: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef804",
    ends={
        Property(name="bpmn2_Collaboration806", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process805", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
parameterRef831: BinaryAssociation = BinaryAssociation(
    name="parameterRef831",
    ends={
        Property(name="bpmn2_ResourceParameter833", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding832", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
resourceRef834: BinaryAssociation = BinaryAssociation(
    name="resourceRef834",
    ends={
        Property(name="bpmn2_Resource836", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole835", type=bpmn2_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings837: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings837",
    ends={
        Property(name="bpmn2_ResourceParameterBinding839", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole838", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression840: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression840",
    ends={
        Property(name="bpmn2_ResourceAssignmentExpression842", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole841", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageRef843: BinaryAssociation = BinaryAssociation(
    name="messageRef843",
    ends={
        Property(name="bpmn2_Message845", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask844", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
sources813: BinaryAssociation = BinaryAssociation(
    name="sources813",
    ends={
        Property(name="bpmn2_EObject815", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship814", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
targets816: BinaryAssociation = BinaryAssociation(
    name="targets816",
    ends={
        Property(name="bpmn2_EObject818", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship817", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
resourceParameters819: BinaryAssociation = BinaryAssociation(
    name="resourceParameters819",
    ends={
        Property(name="bpmn2_ResourceParameter821", type=bpmn2_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Resource820", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression822: BinaryAssociation = BinaryAssociation(
    name="expression822",
    ends={
        Property(name="bpmn2_Expression824", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceAssignmentExpression823", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type825: BinaryAssociation = BinaryAssociation(
    name="type825",
    ends={
        Property(name="bpmn2_ItemDefinition827", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameter826", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expression828: BinaryAssociation = BinaryAssociation(
    name="expression828",
    ends={
        Property(name="bpmn2_Expression830", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding829", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
artifacts868: BinaryAssociation = BinaryAssociation(
    name="artifacts868",
    ends={
        Property(name="bpmn2_Artifact870", type=bpmn2_SubChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubChoreography869", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversationNodes871: BinaryAssociation = BinaryAssociation(
    name="conversationNodes871",
    ends={
        Property(name="bpmn2_ConversationNode873", type=bpmn2_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubConversation872", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts874: BinaryAssociation = BinaryAssociation(
    name="artifacts874",
    ends={
        Property(name="bpmn2_Artifact876", type=bpmn2_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubProcess875", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationRef846: BinaryAssociation = BinaryAssociation(
    name="operationRef846",
    ends={
        Property(name="bpmn2_Operation848", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask847", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression849: BinaryAssociation = BinaryAssociation(
    name="conditionExpression849",
    ends={
        Property(name="bpmn2_Expression851", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SequenceFlow850", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceRef852: BinaryAssociation = BinaryAssociation(
    name="sourceRef852",
    ends={
        Property(name="FlowNode853", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef854: BinaryAssociation = BinaryAssociation(
    name="targetRef854",
    ends={
        Property(name="FlowNode855", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
operationRef856: BinaryAssociation = BinaryAssociation(
    name="operationRef856",
    ends={
        Property(name="bpmn2_Operation858", type=bpmn2_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ServiceTask857", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
structureRef859: BinaryAssociation = BinaryAssociation(
    name="structureRef859",
    ends={
        Property(name="bpmn2_ItemDefinition861", type=bpmn2_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Signal860", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
signalRef862: BinaryAssociation = BinaryAssociation(
    name="signalRef862",
    ends={
        Property(name="bpmn2_Signal864", type=bpmn2_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SignalEventDefinition863", type=bpmn2_Signal, multiplicity=Multiplicity(0, 1))
    }
)
loopCondition865: BinaryAssociation = BinaryAssociation(
    name="loopCondition865",
    ends={
        Property(name="bpmn2_Expression867", type=bpmn2_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_StandardLoopCharacteristics866", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCycle903: BinaryAssociation = BinaryAssociation(
    name="timeCycle903",
    ends={
        Property(name="bpmn2_Expression905", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition904", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
renderings906: BinaryAssociation = BinaryAssociation(
    name="renderings906",
    ends={
        Property(name="bpmn2_Rendering908", type=bpmn2_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_UserTask907", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedSubProcess877: BinaryAssociation = BinaryAssociation(
    name="referencedSubProcess877",
    ends={
        Property(name="bpmn2_Process879", type=bpmn2_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubProcess878", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999))
    }
)
documentsAndResources880: BinaryAssociation = BinaryAssociation(
    name="documentsAndResources880",
    ends={
        Property(name="bpmn2_Document", type=bpmn2_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Task881", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputs882: BinaryAssociation = BinaryAssociation(
    name="dataInputs882",
    ends={
        Property(name="bpmn2_DataInput884", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent883", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation885: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation885",
    ends={
        Property(name="bpmn2_DataInputAssociation887", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent886", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet888: BinaryAssociation = BinaryAssociation(
    name="inputSet888",
    ends={
        Property(name="bpmn2_InputSet890", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent889", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitions891: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions891",
    ends={
        Property(name="bpmn2_EventDefinition893", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent892", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitionRefs894: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs894",
    ends={
        Property(name="bpmn2_EventDefinition896", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent895", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
timeDate897: BinaryAssociation = BinaryAssociation(
    name="timeDate897",
    ends={
        Property(name="bpmn2_Expression899", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition898", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeDuration900: BinaryAssociation = BinaryAssociation(
    name="timeDuration900",
    ends={
        Property(name="bpmn2_Expression902", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition901", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_bpmn2_Activity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Activity)
gen_bpmn2_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=bpmn2_AdHocSubProcess)
gen_bpmn2_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_BoundaryEvent)
gen_bpmn2_BusinessRuleTask_Task = Generalization(general=Task, specific=bpmn2_BusinessRuleTask)
gen_bpmn2_CallActivity_Activity = Generalization(general=Activity, specific=bpmn2_CallActivity)
gen_bpmn2_CallChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_CallChoreography)
gen_bpmn2_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_CallConversation)
gen_bpmn2_Artifact_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Artifact)
gen_bpmn2_Assignment_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Assignment)
gen_bpmn2_Association_Artifact = Generalization(general=Artifact, specific=bpmn2_Association)
gen_bpmn2_Auditing_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Auditing)
gen_bpmn2_Category_RootElement = Generalization(general=RootElement, specific=bpmn2_Category)
gen_bpmn2_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CategoryValue)
gen_bpmn2_Choreography_Collaboration = Generalization(general=Collaboration, specific=bpmn2_Choreography)
gen_bpmn2_Choreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Choreography)
gen_bpmn2_ChoreographyActivity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_ChoreographyActivity)
gen_bpmn2_CallableElement_RootElement = Generalization(general=RootElement, specific=bpmn2_CallableElement)
gen_bpmn2_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CancelEventDefinition)
gen_bpmn2_CatchEvent_Event = Generalization(general=Event, specific=bpmn2_CatchEvent)
gen_bpmn2_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CompensateEventDefinition)
gen_bpmn2_ChoreographyTask_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_ChoreographyTask)
gen_bpmn2_Collaboration_RootElement = Generalization(general=RootElement, specific=bpmn2_Collaboration)
gen_bpmn2_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationKey)
gen_bpmn2_CorrelationProperty_RootElement = Generalization(general=RootElement, specific=bpmn2_CorrelationProperty)
gen_bpmn2_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ComplexBehaviorDefinition)
gen_bpmn2_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyBinding)
gen_bpmn2_ComplexGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ComplexGateway)
gen_bpmn2_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ConditionalEventDefinition)
gen_bpmn2_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_Conversation)
gen_bpmn2_ConversationAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationAssociation)
gen_bpmn2_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationLink)
gen_bpmn2_ConversationNode_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationNode)
gen_bpmn2_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_ConversationNode)
gen_bpmn2_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataAssociation)
gen_bpmn2_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataInput)
gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyRetrievalExpression)
gen_bpmn2_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationSubscription)
gen_bpmn2_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataOutputAssociation)
gen_bpmn2_DataState_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataState)
gen_bpmn2_DataStore_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStore)
gen_bpmn2_DataStore_RootElement = Generalization(general=RootElement, specific=bpmn2_DataStore)
gen_bpmn2_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_Definitions_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Definitions)
gen_bpmn2_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataInputAssociation)
gen_bpmn2_DataObject_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObject)
gen_bpmn2_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObject)
gen_bpmn2_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataOutput)
gen_bpmn2_Escalation_RootElement = Generalization(general=RootElement, specific=bpmn2_Escalation)
gen_bpmn2_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_EscalationEventDefinition)
gen_bpmn2_Event_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Event)
gen_bpmn2_Event_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Event)
gen_bpmn2_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_EventBasedGateway)
gen_bpmn2_Documentation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Documentation)
gen_bpmn2_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_EndEvent)
gen_bpmn2_EndPoint_RootElement = Generalization(general=RootElement, specific=bpmn2_EndPoint)
gen_bpmn2_Error_RootElement = Generalization(general=RootElement, specific=bpmn2_Error)
gen_bpmn2_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ErrorEventDefinition)
gen_bpmn2_EventDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_EventDefinition)
gen_bpmn2_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ExclusiveGateway)
gen_bpmn2_Expression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Expression)
gen_bpmn2_FormalExpression_Expression = Generalization(general=Expression, specific=bpmn2_FormalExpression)
gen_bpmn2_Gateway_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Gateway)
gen_bpmn2_FlowElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElement)
gen_bpmn2_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElementsContainer)
gen_bpmn2_FlowNode_FlowElement = Generalization(general=FlowElement, specific=bpmn2_FlowNode)
gen_bpmn2_GlobalConversation_Collaboration = Generalization(general=Collaboration, specific=bpmn2_GlobalConversation)
gen_bpmn2_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalManualTask)
gen_bpmn2_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalBusinessRuleTask)
gen_bpmn2_GlobalChoreographyTask_Choreography = Generalization(general=Choreography, specific=bpmn2_GlobalChoreographyTask)
gen_bpmn2_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputOutputSpecification)
gen_bpmn2_InputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputSet)
gen_bpmn2_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalScriptTask)
gen_bpmn2_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=bpmn2_GlobalTask)
gen_bpmn2_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalUserTask)
gen_bpmn2_Group_Artifact = Generalization(general=Artifact, specific=bpmn2_Group)
gen_bpmn2_HumanPerformer_Performer = Generalization(general=Performer, specific=bpmn2_HumanPerformer)
gen_bpmn2_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_ImplicitThrowEvent)
gen_bpmn2_InclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_InclusiveGateway)
gen_bpmn2_InputOutputBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputOutputBinding)
gen_bpmn2_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ItemAwareElement)
gen_bpmn2_ItemDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_ItemDefinition)
gen_bpmn2_Interface_RootElement = Generalization(general=RootElement, specific=bpmn2_Interface)
gen_bpmn2_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_IntermediateCatchEvent)
gen_bpmn2_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_IntermediateThrowEvent)
gen_bpmn2_LaneSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LaneSet)
gen_bpmn2_LaneSet_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_LaneSet)
gen_bpmn2_Lane_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Lane)
gen_bpmn2_Lane_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Lane)
gen_bpmn2_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlowAssociation)
gen_bpmn2_Monitoring_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Monitoring)
gen_bpmn2_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_LinkEventDefinition)
gen_bpmn2_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LoopCharacteristics)
gen_bpmn2_ManualTask_Task = Generalization(general=Task, specific=bpmn2_ManualTask)
gen_bpmn2_Message_RootElement = Generalization(general=RootElement, specific=bpmn2_Message)
gen_bpmn2_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_MessageEventDefinition)
gen_bpmn2_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlow)
gen_bpmn2_OutputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_OutputSet)
gen_bpmn2_ParallelGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ParallelGateway)
gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_MultiInstanceLoopCharacteristics)
gen_bpmn2_Participant_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Participant)
gen_bpmn2_Operation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Operation)
gen_bpmn2_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ParticipantAssociation)
gen_bpmn2_ParticipantMultiplicity_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ParticipantMultiplicity)
gen_bpmn2_PartnerEntity_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerEntity)
gen_bpmn2_Participant_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Participant)
gen_bpmn2_Property_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_Property)
gen_bpmn2_ReceiveTask_Task = Generalization(general=Task, specific=bpmn2_ReceiveTask)
gen_bpmn2_Relationship_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Relationship)
gen_bpmn2_PartnerRole_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerRole)
gen_bpmn2_Performer_ResourceRole = Generalization(general=ResourceRole, specific=bpmn2_Performer)
gen_bpmn2_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=bpmn2_PotentialOwner)
gen_bpmn2_Process_CallableElement = Generalization(general=CallableElement, specific=bpmn2_Process)
gen_bpmn2_Process_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Process)
gen_bpmn2_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceRole)
gen_bpmn2_RootElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_RootElement)
gen_bpmn2_ScriptTask_Task = Generalization(general=Task, specific=bpmn2_ScriptTask)
gen_bpmn2_SendTask_Task = Generalization(general=Task, specific=bpmn2_SendTask)
gen_bpmn2_Rendering_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Rendering)
gen_bpmn2_Resource_RootElement = Generalization(general=RootElement, specific=bpmn2_Resource)
gen_bpmn2_ResourceAssignmentExpression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceAssignmentExpression)
gen_bpmn2_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceParameter)
gen_bpmn2_ResourceParameterBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceParameterBinding)
gen_bpmn2_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_StartEvent)
gen_bpmn2_SubChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_SubChoreography)
gen_bpmn2_SubChoreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubChoreography)
gen_bpmn2_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_SubConversation)
gen_bpmn2_SubProcess_Activity = Generalization(general=Activity, specific=bpmn2_SubProcess)
gen_bpmn2_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubProcess)
gen_bpmn2_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=bpmn2_SequenceFlow)
gen_bpmn2_ServiceTask_Task = Generalization(general=Task, specific=bpmn2_ServiceTask)
gen_bpmn2_Signal_RootElement = Generalization(general=RootElement, specific=bpmn2_Signal)
gen_bpmn2_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_SignalEventDefinition)
gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_StandardLoopCharacteristics)
gen_bpmn2_Transaction_SubProcess = Generalization(general=SubProcess, specific=bpmn2_Transaction)
gen_bpmn2_UserTask_Task = Generalization(general=Task, specific=bpmn2_UserTask)
gen_bpmn2_Task_Activity = Generalization(general=Activity, specific=bpmn2_Task)
gen_bpmn2_Task_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Task)
gen_bpmn2_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TerminateEventDefinition)
gen_bpmn2_TextAnnotation_Artifact = Generalization(general=Artifact, specific=bpmn2_TextAnnotation)
gen_bpmn2_ThrowEvent_Event = Generalization(general=Event, specific=bpmn2_ThrowEvent)
gen_bpmn2_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TimerEventDefinition)

# Domain Model
domain_model = DomainModel(
    name="bpmn2",
    types={bpmn2_DocumentRoot, bpmn2_EStringToStringMapEntry, bpmn2_Activity, bpmn2_AdHocSubProcess, bpmn2_FlowElement, bpmn2_Artifact, bpmn2_Assignment, bpmn2_BoundaryEvent, bpmn2_BusinessRuleTask, bpmn2_CallableElement, bpmn2_CallActivity, bpmn2_CallChoreography, bpmn2_CallConversation, bpmn2_ConversationNode, bpmn2_CancelEventDefinition, bpmn2_EventDefinition, bpmn2_RootElement, bpmn2_Association, bpmn2_Auditing, bpmn2_BaseElement, bpmn2_DataInputAssociation, bpmn2_ChoreographyTask, bpmn2_DataObject, bpmn2_CompensateEventDefinition, bpmn2_DataObjectReference, bpmn2_ComplexBehaviorDefinition, bpmn2_DataOutput, bpmn2_ComplexGateway, bpmn2_ConditionalEventDefinition, bpmn2_Conversation, bpmn2_ConversationAssociation, bpmn2_ConversationLink, bpmn2_CorrelationKey, bpmn2_CorrelationProperty, bpmn2_CorrelationPropertyBinding, bpmn2_CatchEvent, bpmn2_CorrelationPropertyRetrievalExpression, bpmn2_Category, bpmn2_CategoryValue, bpmn2_CorrelationSubscription, bpmn2_Choreography, bpmn2_DataAssociation, bpmn2_Collaboration, bpmn2_DataInput, bpmn2_ChoreographyActivity, bpmn2_Error, bpmn2_ErrorEventDefinition, bpmn2_Escalation, bpmn2_EscalationEventDefinition, bpmn2_Event, bpmn2_DataOutputAssociation, bpmn2_DataState, bpmn2_DataStore, bpmn2_DataStoreReference, bpmn2_Definitions, bpmn2_Documentation, bpmn2_EndEvent, bpmn2_EndPoint, bpmn2_FormalExpression, bpmn2_Gateway, bpmn2_GlobalBusinessRuleTask, bpmn2_GlobalChoreographyTask, bpmn2_GlobalConversation, bpmn2_EventBasedGateway, bpmn2_ExclusiveGateway, bpmn2_Expression, bpmn2_Extension, bpmn2_ExtensionAttributeValue, bpmn2_FlowNode, bpmn2_ResourceRole, bpmn2_ImplicitThrowEvent, bpmn2_Import, bpmn2_InclusiveGateway, bpmn2_InputSet, bpmn2_GlobalManualTask, bpmn2_GlobalScriptTask, bpmn2_GlobalTask, bpmn2_GlobalUserTask, bpmn2_Group, bpmn2_HumanPerformer, bpmn2_Performer, bpmn2_InputOutputSpecification, bpmn2_ItemDefinition, bpmn2_Lane, bpmn2_LaneSet, bpmn2_Interface, bpmn2_IntermediateCatchEvent, bpmn2_IntermediateThrowEvent, bpmn2_Monitoring, bpmn2_InputOutputBinding, bpmn2_MultiInstanceLoopCharacteristics, bpmn2_Operation, bpmn2_OutputSet, bpmn2_LinkEventDefinition, bpmn2_LoopCharacteristics, bpmn2_ManualTask, bpmn2_Message, bpmn2_MessageEventDefinition, bpmn2_MessageFlow, bpmn2_MessageFlowAssociation, bpmn2_Process, bpmn2_Property, bpmn2_ReceiveTask, bpmn2_Relationship, bpmn2_ParallelGateway, bpmn2_Participant, bpmn2_ParticipantAssociation, bpmn2_ParticipantMultiplicity, bpmn2_PartnerEntity, bpmn2_PartnerRole, bpmn2_PotentialOwner, bpmn2_EObject, bpmn2_ScriptTask, bpmn2_SendTask, bpmn2_SequenceFlow, bpmn2_Rendering, bpmn2_Resource, bpmn2_ResourceAssignmentExpression, bpmn2_ResourceParameter, bpmn2_ResourceParameterBinding, bpmn2_SubConversation, bpmn2_SubProcess, bpmn2_Task, bpmn2_ServiceTask, bpmn2_Signal, bpmn2_SignalEventDefinition, bpmn2_StandardLoopCharacteristics, bpmn2_StartEvent, bpmn2_SubChoreography, bpmn2_Transaction, bpmn2_UserTask, FlowNode, bpmn2_TerminateEventDefinition, bpmn2_TextAnnotation, bpmn2_ThrowEvent, bpmn2_TimerEventDefinition, bpmn2_Position, bpmn2_Role, SubProcess, bpmn2_Competency, bpmn2_Criterion, bpmn2_OrganisationalUnit, CatchEvent, Task, Activity, ChoreographyActivity, ConversationNode, BaseElement, Artifact, bpmn2_ExtensionDefinition, Collaboration, FlowElementsContainer, RootElement, EventDefinition, Event, Gateway, bpmn2_InteractionNode, InteractionNode, bpmn2_ItemAwareElement, ItemAwareElement, bpmn2_Document, DataAssociation, FlowElement, bpmn2_BPMNDiagram, ThrowEvent, bpmn2_ExtensionAttributeDefinition, Expression, bpmn2_FlowElementsContainer, GlobalTask, Choreography, CallableElement, Performer, LoopCharacteristics, ResourceRole, HumanPerformer, AdHocOrdering, AssociationDirection, ChoreographyLoopType, EventBasedGatewayType, GatewayDirection, ItemKind, MultiInstanceBehavior, ProcessType, RelationshipDirection},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, activity4, adHocSubProcess6, flowElement8, artifact10, baseElementWithMixedContent20, boundaryEvent23, businessRuleTask25, callableElement27, callActivity29, callChoreography31, callConversation33, conversationNode35, cancelEventDefinition37, eventDefinition39, rootElement41, assignment12, association14, auditing16, baseElement18, choreographyActivity53, dataInputAssociation85, choreographyTask55, dataObject87, compensateEventDefinition57, dataObjectReference89, complexBehaviorDefinition59, dataOutput91, complexGateway61, conditionalEventDefinition63, conversation65, conversationAssociation67, conversationLink69, correlationKey71, correlationProperty73, correlationPropertyBinding75, catchEvent43, category45, correlationPropertyRetrievalExpression77, categoryValue47, correlationSubscription79, choreography49, dataAssociation81, collaboration51, dataInput83, error109, errorEventDefinition111, escalation113, escalationEventDefinition115, dataOutputAssociation93, dataState95, dataStore97, dataStoreReference99, definitions101, documentation103, endEvent105, endPoint107, formalExpression131, gateway133, globalBusinessRuleTask135, globalChoreographyTask137, globalConversation139, event117, eventBasedGateway119, exclusiveGateway121, expression123, extension125, extensionElements127, flowNode129, resourceRole155, implicitThrowEvent157, import159, inclusiveGateway161, globalManualTask141, globalScriptTask143, globalTask145, globalUserTask147, group149, humanPerformer151, performer153, ioSpecification173, itemDefinition175, lane177, inputSet163, interface165, intermediateCatchEvent167, intermediateThrowEvent169, monitoring195, ioBinding171, multiInstanceLoopCharacteristics197, operation199, laneSet179, outputSet201, linkEventDefinition181, loopCharacteristics183, manualTask185, message187, messageEventDefinition189, messageFlow191, messageFlowAssociation193, process217, property219, receiveTask221, relationship223, parallelGateway203, participant205, participantAssociation207, participantMultiplicity209, partnerEntity211, partnerRole213, potentialOwner215, script235, scriptTask237, sendTask239, sequenceFlow241, rendering225, resource227, resourceAssignmentExpression229, resourceParameter231, resourceParameterBinding233, subConversation255, subProcess257, task259, serviceTask243, signal245, signalEventDefinition247, standardLoopCharacteristics249, startEvent251, subChoreography253, transaction272, userTask274, ioSpecification276, boundaryEventRefs279, terminateEventDefinition261, text263, textAnnotation266, throwEvent268, timerEventDefinition270, isPerformedBy307, isPerformedByPosition310, isPerformedByRole312, competency314, completionCondition317, properties280, dataInputAssociations283, dataOutputAssociations286, resources289, loopCharacteristics292, default295, requiresCompetency298, isMeasuredByCriterion300, isPerformedByOrganisationalUnit302, isResponsibleByOrganisationalUnit304, attachedToRef340, calledElementRef341, participantAssociations344, calledChoreographyRef347, from320, to323, sourceRef326, targetRef329, extensionValues332, documentation335, extensionDefinitions338, categoryValue380, categorizedFlowElements383, participantRefs386, correlationKeys389, initiatingParticipantRef392, participantAssociations350, calledCollaborationRef353, supportedInterfaceRefs356, ioSpecification359, ioBinding362, dataOutputs365, dataOutputAssociation368, outputSet371, eventDefinitions374, eventDefinitionRefs377, choreographyRef422, conversationLinks425, activityRef428, messageFlowRef395, participants398, messageFlows401, artifacts404, conversations407, conversationAssociations410, participantAssociations413, messageFlowAssociations416, participantRefs457, correlationKeys419, messageFlowRefs460, correlationKeys463, correlationPropertyRef466, correlationPropertyRetrievalExpression469, type472, condition431, event434, activationCondition437, default440, condition443, innerConversationNodeRef446, outerConversationNodeRef449, sourceRef452, targetRef454, correlationKeyRef490, sourceRef493, targetRef495, transformation498, assignment501, inputSetWithOptional504, dataPath475, correlationPropertyRef478, messagePath481, messageRef484, correlationPropertyBinding487, referencesDocument518, dataStoreRef521, imports524, extensions527, inputSetWithWhileExecuting505, inputSetRefs507, referencesDocument509, dataObjectRef510, outputSetWithOptional513, outputSetWithWhileExecuting514, outputSetRefs516, structureRef544, escalationRef547, properties550, rootElements530, diagrams533, relationships535, structureRef538, errorRef541, extensionDefinition559, valueRef560, extensionAttributeDefinition563, default553, definition556, outgoing582, evaluatesToTypeRef584, extensionAttributeDefinitions565, auditing566, monitoring569, categoryValueRef572, laneSets575, flowElements577, incoming580, lanes581, dataInputs611, initiatingParticipantRef587, dataOutputs614, inputSets617, outputSets620, dataInputRefs623, resources590, renderings593, categoryValueRef596, default599, inputDataRef602, operationRef605, outputDataRef608, dataState643, itemSubjectRef646, import649, structureRef652, optionalInputRefs624, whileExecutingInputRefs626, outputSetRefs628, incomingConversationLinks631, outgoingConversationLinks634, operations637, implementationRef640, partitionElementRef662, representsPerformer665, representsRole668, representsOrganisationalUnit671, messages674, lanes677, partitionElement655, flowNodeRefs658, childLaneSet659, targetRef703, innerMessageFlowRef706, outerMessageFlowRef709, representsOrganisationalUnit680, source684, target686, itemRef688, operationRef691, messageRef694, errorRefs745, messageRef697, implementationRef748, sourceRef700, dataOutputRefs751, optionalOutputRefs752, whileExecutingOutputRefs754, inputSetRefs756, loopCardinality712, loopDataInputRef715, loopDataOutputRef718, inputDataItem721, outputDataItem724, complexBehaviorDefinition727, completionCondition730, noneBehaviorEventRef733, oneBehaviorEventRef736, inMessageRef739, outMessageRef742, participantMultiplicity765, processRef768, innerParticipantRef771, outerParticipantRef774, interfaceRefs759, endPointRefs762, messageRef807, operationRef810, participantRef777, participantRef780, auditing783, monitoring786, properties789, artifacts792, resources795, correlationSubscriptions798, supports802, definitionalCollaborationRef804, parameterRef831, resourceRef834, resourceParameterBindings837, resourceAssignmentExpression840, messageRef843, sources813, targets816, resourceParameters819, expression822, type825, expression828, artifacts868, conversationNodes871, artifacts874, operationRef846, conditionExpression849, sourceRef852, targetRef854, operationRef856, structureRef859, signalRef862, loopCondition865, timeCycle903, renderings906, referencedSubProcess877, documentsAndResources880, dataInputs882, dataInputAssociation885, inputSet888, eventDefinitions891, eventDefinitionRefs894, timeDate897, timeDuration900},
    generalizations={gen_bpmn2_Activity_FlowNode, gen_bpmn2_AdHocSubProcess_SubProcess, gen_bpmn2_BoundaryEvent_CatchEvent, gen_bpmn2_BusinessRuleTask_Task, gen_bpmn2_CallActivity_Activity, gen_bpmn2_CallChoreography_ChoreographyActivity, gen_bpmn2_CallConversation_ConversationNode, gen_bpmn2_Artifact_BaseElement, gen_bpmn2_Assignment_BaseElement, gen_bpmn2_Association_Artifact, gen_bpmn2_Auditing_BaseElement, gen_bpmn2_Category_RootElement, gen_bpmn2_CategoryValue_BaseElement, gen_bpmn2_Choreography_Collaboration, gen_bpmn2_Choreography_FlowElementsContainer, gen_bpmn2_ChoreographyActivity_FlowNode, gen_bpmn2_CallableElement_RootElement, gen_bpmn2_CancelEventDefinition_EventDefinition, gen_bpmn2_CatchEvent_Event, gen_bpmn2_CompensateEventDefinition_EventDefinition, gen_bpmn2_ChoreographyTask_ChoreographyActivity, gen_bpmn2_Collaboration_RootElement, gen_bpmn2_CorrelationKey_BaseElement, gen_bpmn2_CorrelationProperty_RootElement, gen_bpmn2_ComplexBehaviorDefinition_BaseElement, gen_bpmn2_CorrelationPropertyBinding_BaseElement, gen_bpmn2_ComplexGateway_Gateway, gen_bpmn2_ConditionalEventDefinition_EventDefinition, gen_bpmn2_Conversation_ConversationNode, gen_bpmn2_ConversationAssociation_BaseElement, gen_bpmn2_ConversationLink_BaseElement, gen_bpmn2_ConversationNode_BaseElement, gen_bpmn2_ConversationNode_InteractionNode, gen_bpmn2_DataAssociation_BaseElement, gen_bpmn2_DataInput_ItemAwareElement, gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement, gen_bpmn2_CorrelationSubscription_BaseElement, gen_bpmn2_DataOutputAssociation_DataAssociation, gen_bpmn2_DataState_BaseElement, gen_bpmn2_DataStore_ItemAwareElement, gen_bpmn2_DataStore_RootElement, gen_bpmn2_DataStoreReference_FlowElement, gen_bpmn2_DataStoreReference_ItemAwareElement, gen_bpmn2_Definitions_BaseElement, gen_bpmn2_DataInputAssociation_DataAssociation, gen_bpmn2_DataObject_FlowElement, gen_bpmn2_DataObject_ItemAwareElement, gen_bpmn2_DataObjectReference_FlowElement, gen_bpmn2_DataObjectReference_ItemAwareElement, gen_bpmn2_DataOutput_ItemAwareElement, gen_bpmn2_Escalation_RootElement, gen_bpmn2_EscalationEventDefinition_EventDefinition, gen_bpmn2_Event_FlowNode, gen_bpmn2_Event_InteractionNode, gen_bpmn2_EventBasedGateway_Gateway, gen_bpmn2_Documentation_BaseElement, gen_bpmn2_EndEvent_ThrowEvent, gen_bpmn2_EndPoint_RootElement, gen_bpmn2_Error_RootElement, gen_bpmn2_ErrorEventDefinition_EventDefinition, gen_bpmn2_EventDefinition_RootElement, gen_bpmn2_ExclusiveGateway_Gateway, gen_bpmn2_Expression_BaseElement, gen_bpmn2_FormalExpression_Expression, gen_bpmn2_Gateway_FlowNode, gen_bpmn2_FlowElement_BaseElement, gen_bpmn2_FlowElementsContainer_BaseElement, gen_bpmn2_FlowNode_FlowElement, gen_bpmn2_GlobalConversation_Collaboration, gen_bpmn2_GlobalManualTask_GlobalTask, gen_bpmn2_GlobalBusinessRuleTask_GlobalTask, gen_bpmn2_GlobalChoreographyTask_Choreography, gen_bpmn2_InputOutputSpecification_BaseElement, gen_bpmn2_InputSet_BaseElement, gen_bpmn2_GlobalScriptTask_GlobalTask, gen_bpmn2_GlobalTask_CallableElement, gen_bpmn2_GlobalUserTask_GlobalTask, gen_bpmn2_Group_Artifact, gen_bpmn2_HumanPerformer_Performer, gen_bpmn2_ImplicitThrowEvent_ThrowEvent, gen_bpmn2_InclusiveGateway_Gateway, gen_bpmn2_InputOutputBinding_BaseElement, gen_bpmn2_ItemAwareElement_BaseElement, gen_bpmn2_ItemDefinition_RootElement, gen_bpmn2_Interface_RootElement, gen_bpmn2_IntermediateCatchEvent_CatchEvent, gen_bpmn2_IntermediateThrowEvent_ThrowEvent, gen_bpmn2_LaneSet_BaseElement, gen_bpmn2_LaneSet_InteractionNode, gen_bpmn2_Lane_BaseElement, gen_bpmn2_Lane_InteractionNode, gen_bpmn2_MessageFlowAssociation_BaseElement, gen_bpmn2_Monitoring_BaseElement, gen_bpmn2_LinkEventDefinition_EventDefinition, gen_bpmn2_LoopCharacteristics_BaseElement, gen_bpmn2_ManualTask_Task, gen_bpmn2_Message_RootElement, gen_bpmn2_MessageEventDefinition_EventDefinition, gen_bpmn2_MessageFlow_BaseElement, gen_bpmn2_OutputSet_BaseElement, gen_bpmn2_ParallelGateway_Gateway, gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics, gen_bpmn2_Participant_BaseElement, gen_bpmn2_Operation_BaseElement, gen_bpmn2_ParticipantAssociation_BaseElement, gen_bpmn2_ParticipantMultiplicity_BaseElement, gen_bpmn2_PartnerEntity_RootElement, gen_bpmn2_Participant_InteractionNode, gen_bpmn2_Property_ItemAwareElement, gen_bpmn2_ReceiveTask_Task, gen_bpmn2_Relationship_BaseElement, gen_bpmn2_PartnerRole_RootElement, gen_bpmn2_Performer_ResourceRole, gen_bpmn2_PotentialOwner_HumanPerformer, gen_bpmn2_Process_CallableElement, gen_bpmn2_Process_FlowElementsContainer, gen_bpmn2_ResourceRole_BaseElement, gen_bpmn2_RootElement_BaseElement, gen_bpmn2_ScriptTask_Task, gen_bpmn2_SendTask_Task, gen_bpmn2_Rendering_BaseElement, gen_bpmn2_Resource_RootElement, gen_bpmn2_ResourceAssignmentExpression_BaseElement, gen_bpmn2_ResourceParameter_BaseElement, gen_bpmn2_ResourceParameterBinding_BaseElement, gen_bpmn2_StartEvent_CatchEvent, gen_bpmn2_SubChoreography_ChoreographyActivity, gen_bpmn2_SubChoreography_FlowElementsContainer, gen_bpmn2_SubConversation_ConversationNode, gen_bpmn2_SubProcess_Activity, gen_bpmn2_SubProcess_FlowElementsContainer, gen_bpmn2_SequenceFlow_FlowElement, gen_bpmn2_ServiceTask_Task, gen_bpmn2_Signal_RootElement, gen_bpmn2_SignalEventDefinition_EventDefinition, gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics, gen_bpmn2_Transaction_SubProcess, gen_bpmn2_UserTask_Task, gen_bpmn2_Task_Activity, gen_bpmn2_Task_InteractionNode, gen_bpmn2_TerminateEventDefinition_EventDefinition, gen_bpmn2_TextAnnotation_Artifact, gen_bpmn2_ThrowEvent_Event, gen_bpmn2_TimerEventDefinition_EventDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)