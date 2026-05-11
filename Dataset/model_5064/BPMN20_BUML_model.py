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
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="Both")
    }
)

ChoreographyLoopType: Enumeration = Enumeration(
    name="ChoreographyLoopType",
    literals={
            EnumerationLiteral(name="None_"),
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
            EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Complex"),
			EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="One")
    }
)

ProcessType: Enumeration = Enumeration(
    name="ProcessType",
    literals={
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="Public"),
			EnumerationLiteral(name="Private")
    }
)

RelationshipDirection: Enumeration = Enumeration(
    name="RelationshipDirection",
    literals={
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="Forward"),
			EnumerationLiteral(name="Backward"),
			EnumerationLiteral(name="Both")
    }
)

# Classes
bpmn2_DocumentRoot = Class(name="bpmn2_DocumentRoot")
bpmn2_EStringToStringMapEntry = Class(name="bpmn2_EStringToStringMapEntry")
bpmn2_CallableElement = Class(name="bpmn2_CallableElement")
bpmn2_AdHocSubProcess = Class(name="bpmn2_AdHocSubProcess")
bpmn2_FlowElement = Class(name="bpmn2_FlowElement", is_abstract=True)
bpmn2_CallActivity = Class(name="bpmn2_CallActivity")
bpmn2_Artifact = Class(name="bpmn2_Artifact")
bpmn2_Assignment = Class(name="bpmn2_Assignment")
bpmn2_CallChoreography = Class(name="bpmn2_CallChoreography")
bpmn2_Association = Class(name="bpmn2_Association")
bpmn2_Auditing = Class(name="bpmn2_Auditing")
bpmn2_BaseElement = Class(name="bpmn2_BaseElement")
bpmn2_BoundaryEvent = Class(name="bpmn2_BoundaryEvent")
bpmn2_BusinessRuleTask = Class(name="bpmn2_BusinessRuleTask")
bpmn2_Activity = Class(name="bpmn2_Activity")
bpmn2_CatchEvent = Class(name="bpmn2_CatchEvent", is_abstract=True)
bpmn2_Category = Class(name="bpmn2_Category")
bpmn2_CategoryValue = Class(name="bpmn2_CategoryValue")
bpmn2_CallConversation = Class(name="bpmn2_CallConversation")
bpmn2_ConversationNode = Class(name="bpmn2_ConversationNode")
bpmn2_CancelEventDefinition = Class(name="bpmn2_CancelEventDefinition")
bpmn2_EventDefinition = Class(name="bpmn2_EventDefinition")
bpmn2_RootElement = Class(name="bpmn2_RootElement")
bpmn2_ComplexBehaviorDefinition = Class(name="bpmn2_ComplexBehaviorDefinition")
bpmn2_ComplexGateway = Class(name="bpmn2_ComplexGateway")
bpmn2_Choreography = Class(name="bpmn2_Choreography")
bpmn2_Collaboration = Class(name="bpmn2_Collaboration")
bpmn2_ChoreographyActivity = Class(name="bpmn2_ChoreographyActivity", is_abstract=True)
bpmn2_ChoreographyTask = Class(name="bpmn2_ChoreographyTask")
bpmn2_CompensateEventDefinition = Class(name="bpmn2_CompensateEventDefinition")
bpmn2_CorrelationProperty = Class(name="bpmn2_CorrelationProperty")
bpmn2_CorrelationPropertyBinding = Class(name="bpmn2_CorrelationPropertyBinding")
bpmn2_CorrelationPropertyRetrievalExpression = Class(name="bpmn2_CorrelationPropertyRetrievalExpression")
bpmn2_ConditionalEventDefinition = Class(name="bpmn2_ConditionalEventDefinition")
bpmn2_Conversation = Class(name="bpmn2_Conversation")
bpmn2_ConversationAssociation = Class(name="bpmn2_ConversationAssociation")
bpmn2_ConversationLink = Class(name="bpmn2_ConversationLink")
bpmn2_CorrelationKey = Class(name="bpmn2_CorrelationKey")
bpmn2_DataObject = Class(name="bpmn2_DataObject")
bpmn2_DataObjectReference = Class(name="bpmn2_DataObjectReference")
bpmn2_CorrelationSubscription = Class(name="bpmn2_CorrelationSubscription")
bpmn2_DataAssociation = Class(name="bpmn2_DataAssociation")
bpmn2_DataInput = Class(name="bpmn2_DataInput")
bpmn2_DataInputAssociation = Class(name="bpmn2_DataInputAssociation")
bpmn2_DataStore = Class(name="bpmn2_DataStore")
bpmn2_DataStoreReference = Class(name="bpmn2_DataStoreReference")
bpmn2_DataOutput = Class(name="bpmn2_DataOutput")
bpmn2_DataOutputAssociation = Class(name="bpmn2_DataOutputAssociation")
bpmn2_DataState = Class(name="bpmn2_DataState")
bpmn2_ErrorEventDefinition = Class(name="bpmn2_ErrorEventDefinition")
bpmn2_Escalation = Class(name="bpmn2_Escalation")
bpmn2_Definitions = Class(name="bpmn2_Definitions")
bpmn2_Documentation = Class(name="bpmn2_Documentation")
bpmn2_EndEvent = Class(name="bpmn2_EndEvent")
bpmn2_EndPoint = Class(name="bpmn2_EndPoint")
bpmn2_Error = Class(name="bpmn2_Error")
bpmn2_Expression = Class(name="bpmn2_Expression")
bpmn2_Extension = Class(name="bpmn2_Extension")
bpmn2_ExtensionAttributeValue = Class(name="bpmn2_ExtensionAttributeValue")
bpmn2_EscalationEventDefinition = Class(name="bpmn2_EscalationEventDefinition")
bpmn2_Event = Class(name="bpmn2_Event", is_abstract=True)
bpmn2_EventBasedGateway = Class(name="bpmn2_EventBasedGateway")
bpmn2_ExclusiveGateway = Class(name="bpmn2_ExclusiveGateway")
bpmn2_GlobalChoreographyTask = Class(name="bpmn2_GlobalChoreographyTask")
bpmn2_GlobalConversation = Class(name="bpmn2_GlobalConversation")
bpmn2_FlowNode = Class(name="bpmn2_FlowNode", is_abstract=True)
bpmn2_FormalExpression = Class(name="bpmn2_FormalExpression")
bpmn2_Gateway = Class(name="bpmn2_Gateway", is_abstract=True)
bpmn2_GlobalBusinessRuleTask = Class(name="bpmn2_GlobalBusinessRuleTask")
bpmn2_GlobalUserTask = Class(name="bpmn2_GlobalUserTask")
bpmn2_Group = Class(name="bpmn2_Group")
bpmn2_GlobalManualTask = Class(name="bpmn2_GlobalManualTask")
bpmn2_GlobalScriptTask = Class(name="bpmn2_GlobalScriptTask")
bpmn2_GlobalTask = Class(name="bpmn2_GlobalTask")
bpmn2_ImplicitThrowEvent = Class(name="bpmn2_ImplicitThrowEvent")
bpmn2_Import = Class(name="bpmn2_Import")
bpmn2_HumanPerformer = Class(name="bpmn2_HumanPerformer")
bpmn2_Performer = Class(name="bpmn2_Performer")
bpmn2_ResourceRole = Class(name="bpmn2_ResourceRole")
bpmn2_IntermediateCatchEvent = Class(name="bpmn2_IntermediateCatchEvent")
bpmn2_IntermediateThrowEvent = Class(name="bpmn2_IntermediateThrowEvent")
bpmn2_InclusiveGateway = Class(name="bpmn2_InclusiveGateway")
bpmn2_InputSet = Class(name="bpmn2_InputSet")
bpmn2_Interface = Class(name="bpmn2_Interface")
bpmn2_Lane = Class(name="bpmn2_Lane")
bpmn2_LaneSet = Class(name="bpmn2_LaneSet")
bpmn2_InputOutputBinding = Class(name="bpmn2_InputOutputBinding")
bpmn2_InputOutputSpecification = Class(name="bpmn2_InputOutputSpecification")
bpmn2_ItemDefinition = Class(name="bpmn2_ItemDefinition")
bpmn2_Message = Class(name="bpmn2_Message")
bpmn2_LinkEventDefinition = Class(name="bpmn2_LinkEventDefinition")
bpmn2_LoopCharacteristics = Class(name="bpmn2_LoopCharacteristics", is_abstract=True)
bpmn2_ManualTask = Class(name="bpmn2_ManualTask")
bpmn2_Monitoring = Class(name="bpmn2_Monitoring")
bpmn2_MultiInstanceLoopCharacteristics = Class(name="bpmn2_MultiInstanceLoopCharacteristics")
bpmn2_MessageEventDefinition = Class(name="bpmn2_MessageEventDefinition")
bpmn2_MessageFlow = Class(name="bpmn2_MessageFlow")
bpmn2_MessageFlowAssociation = Class(name="bpmn2_MessageFlowAssociation")
bpmn2_Participant = Class(name="bpmn2_Participant")
bpmn2_ParticipantAssociation = Class(name="bpmn2_ParticipantAssociation")
bpmn2_Operation = Class(name="bpmn2_Operation")
bpmn2_OutputSet = Class(name="bpmn2_OutputSet")
bpmn2_ParallelGateway = Class(name="bpmn2_ParallelGateway")
bpmn2_Property = Class(name="bpmn2_Property")
bpmn2_ReceiveTask = Class(name="bpmn2_ReceiveTask")
bpmn2_ParticipantMultiplicity = Class(name="bpmn2_ParticipantMultiplicity")
bpmn2_PartnerEntity = Class(name="bpmn2_PartnerEntity")
bpmn2_PartnerRole = Class(name="bpmn2_PartnerRole")
bpmn2_PotentialOwner = Class(name="bpmn2_PotentialOwner")
bpmn2_Process = Class(name="bpmn2_Process")
bpmn2_ResourceAssignmentExpression = Class(name="bpmn2_ResourceAssignmentExpression")
bpmn2_Relationship = Class(name="bpmn2_Relationship")
bpmn2_Rendering = Class(name="bpmn2_Rendering")
bpmn2_Resource = Class(name="bpmn2_Resource")
bpmn2_ScriptTask = Class(name="bpmn2_ScriptTask")
bpmn2_SendTask = Class(name="bpmn2_SendTask")
bpmn2_ResourceParameter = Class(name="bpmn2_ResourceParameter")
bpmn2_ResourceParameterBinding = Class(name="bpmn2_ResourceParameterBinding")
bpmn2_EObject = Class(name="bpmn2_EObject")
bpmn2_SignalEventDefinition = Class(name="bpmn2_SignalEventDefinition")
bpmn2_SequenceFlow = Class(name="bpmn2_SequenceFlow")
bpmn2_ServiceTask = Class(name="bpmn2_ServiceTask")
bpmn2_Signal = Class(name="bpmn2_Signal")
bpmn2_SubConversation = Class(name="bpmn2_SubConversation")
bpmn2_SubProcess = Class(name="bpmn2_SubProcess")
bpmn2_StandardLoopCharacteristics = Class(name="bpmn2_StandardLoopCharacteristics")
bpmn2_StartEvent = Class(name="bpmn2_StartEvent")
bpmn2_SubChoreography = Class(name="bpmn2_SubChoreography")
bpmn2_TextAnnotation = Class(name="bpmn2_TextAnnotation")
bpmn2_Task = Class(name="bpmn2_Task")
bpmn2_TerminateEventDefinition = Class(name="bpmn2_TerminateEventDefinition")
bpmn2_ThrowEvent = Class(name="bpmn2_ThrowEvent", is_abstract=True)
bpmn2_TimerEventDefinition = Class(name="bpmn2_TimerEventDefinition")
bpmn2_Transaction = Class(name="bpmn2_Transaction")
bpmn2_UserTask = Class(name="bpmn2_UserTask")
FlowNode = Class(name="FlowNode")
SubProcess = Class(name="SubProcess")
bpmn2_Competency = Class(name="bpmn2_Competency")
bpmn2_Criterion = Class(name="bpmn2_Criterion")
bpmn2_OrganisationalUnit = Class(name="bpmn2_OrganisationalUnit")
bpmn2_Position = Class(name="bpmn2_Position")
bpmn2_Role = Class(name="bpmn2_Role")
CatchEvent = Class(name="CatchEvent")
Task = Class(name="Task")
Activity = Class(name="Activity")
BaseElement = Class(name="BaseElement")
Artifact = Class(name="Artifact")
bpmn2_ExtensionDefinition = Class(name="bpmn2_ExtensionDefinition")
ChoreographyActivity = Class(name="ChoreographyActivity")
ConversationNode = Class(name="ConversationNode")
RootElement = Class(name="RootElement")
EventDefinition = Class(name="EventDefinition")
Event = Class(name="Event")
Collaboration = Class(name="Collaboration")
FlowElementsContainer = Class(name="FlowElementsContainer")
Gateway = Class(name="Gateway")
bpmn2_InteractionNode = Class(name="bpmn2_InteractionNode")
InteractionNode = Class(name="InteractionNode")
FlowElement = Class(name="FlowElement")
bpmn2_ItemAwareElement = Class(name="bpmn2_ItemAwareElement")
ItemAwareElement = Class(name="ItemAwareElement")
bpmn2_Document = Class(name="bpmn2_Document")
DataAssociation = Class(name="DataAssociation")
bpmn2_BPMNDiagram = Class(name="bpmn2_BPMNDiagram")
ThrowEvent = Class(name="ThrowEvent")
bpmn2_FlowElementsContainer = Class(name="bpmn2_FlowElementsContainer", is_abstract=True)
bpmn2_ExtensionAttributeDefinition = Class(name="bpmn2_ExtensionAttributeDefinition")
CallableElement = Class(name="CallableElement")
Expression = Class(name="Expression")
GlobalTask = Class(name="GlobalTask")
Choreography = Class(name="Choreography")
Performer = Class(name="Performer")
LoopCharacteristics = Class(name="LoopCharacteristics")
ResourceRole = Class(name="ResourceRole")
HumanPerformer = Class(name="HumanPerformer")

# bpmn2_DocumentRoot class attributes and methods

# bpmn2_EStringToStringMapEntry class attributes and methods

# bpmn2_CallableElement class attributes and methods

# bpmn2_AdHocSubProcess class attributes and methods
bpmn2_AdHocSubProcess_cancelRemainingInstances: Property = Property(name="cancelRemainingInstances", type=BooleanType)
bpmn2_AdHocSubProcess_ordering: Property = Property(name="ordering", type=StringType)
bpmn2_AdHocSubProcess.attributes={bpmn2_AdHocSubProcess_cancelRemainingInstances, bpmn2_AdHocSubProcess_ordering}

# bpmn2_FlowElement class attributes and methods

# bpmn2_CallActivity class attributes and methods

# bpmn2_Artifact class attributes and methods

# bpmn2_Assignment class attributes and methods

# bpmn2_CallChoreography class attributes and methods

# bpmn2_Association class attributes and methods
bpmn2_Association_associationDirection: Property = Property(name="associationDirection", type=StringType)
bpmn2_Association.attributes={bpmn2_Association_associationDirection}

# bpmn2_Auditing class attributes and methods

# bpmn2_BaseElement class attributes and methods
bpmn2_BaseElement_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
bpmn2_BaseElement_name: Property = Property(name="name", type=StringType)
bpmn2_BaseElement_description: Property = Property(name="description", type=StringType)
bpmn2_BaseElement_id: Property = Property(name="id", type=StringType)
bpmn2_BaseElement.attributes={bpmn2_BaseElement_name, bpmn2_BaseElement_id, bpmn2_BaseElement_anyAttribute, bpmn2_BaseElement_description}

# bpmn2_BoundaryEvent class attributes and methods
bpmn2_BoundaryEvent_cancelActivity: Property = Property(name="cancelActivity", type=BooleanType)
bpmn2_BoundaryEvent.attributes={bpmn2_BoundaryEvent_cancelActivity}

# bpmn2_BusinessRuleTask class attributes and methods
bpmn2_BusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_BusinessRuleTask.attributes={bpmn2_BusinessRuleTask_implementation}

# bpmn2_Activity class attributes and methods
bpmn2_Activity_completionQuantity: Property = Property(name="completionQuantity", type=IntegerType)
bpmn2_Activity_isForCompensation: Property = Property(name="isForCompensation", type=BooleanType)
bpmn2_Activity_startQuantity: Property = Property(name="startQuantity", type=IntegerType)
bpmn2_Activity.attributes={bpmn2_Activity_completionQuantity, bpmn2_Activity_isForCompensation, bpmn2_Activity_startQuantity}

# bpmn2_CatchEvent class attributes and methods
bpmn2_CatchEvent_parallelMultiple: Property = Property(name="parallelMultiple", type=BooleanType)
bpmn2_CatchEvent.attributes={bpmn2_CatchEvent_parallelMultiple}

# bpmn2_Category class attributes and methods

# bpmn2_CategoryValue class attributes and methods
bpmn2_CategoryValue_value: Property = Property(name="value", type=StringType)
bpmn2_CategoryValue.attributes={bpmn2_CategoryValue_value}

# bpmn2_CallConversation class attributes and methods

# bpmn2_ConversationNode class attributes and methods

# bpmn2_CancelEventDefinition class attributes and methods

# bpmn2_EventDefinition class attributes and methods

# bpmn2_RootElement class attributes and methods

# bpmn2_ComplexBehaviorDefinition class attributes and methods

# bpmn2_ComplexGateway class attributes and methods

# bpmn2_Choreography class attributes and methods

# bpmn2_Collaboration class attributes and methods
bpmn2_Collaboration_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Collaboration.attributes={bpmn2_Collaboration_isClosed}

# bpmn2_ChoreographyActivity class attributes and methods
bpmn2_ChoreographyActivity_loopType: Property = Property(name="loopType", type=StringType)
bpmn2_ChoreographyActivity.attributes={bpmn2_ChoreographyActivity_loopType}

# bpmn2_ChoreographyTask class attributes and methods

# bpmn2_CompensateEventDefinition class attributes and methods
bpmn2_CompensateEventDefinition_waitForCompletion: Property = Property(name="waitForCompletion", type=BooleanType)
bpmn2_CompensateEventDefinition.attributes={bpmn2_CompensateEventDefinition_waitForCompletion}

# bpmn2_CorrelationProperty class attributes and methods

# bpmn2_CorrelationPropertyBinding class attributes and methods

# bpmn2_CorrelationPropertyRetrievalExpression class attributes and methods

# bpmn2_ConditionalEventDefinition class attributes and methods

# bpmn2_Conversation class attributes and methods

# bpmn2_ConversationAssociation class attributes and methods

# bpmn2_ConversationLink class attributes and methods

# bpmn2_CorrelationKey class attributes and methods

# bpmn2_DataObject class attributes and methods
bpmn2_DataObject_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataObject.attributes={bpmn2_DataObject_isCollection}

# bpmn2_DataObjectReference class attributes and methods

# bpmn2_CorrelationSubscription class attributes and methods

# bpmn2_DataAssociation class attributes and methods

# bpmn2_DataInput class attributes and methods
bpmn2_DataInput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataInput.attributes={bpmn2_DataInput_isCollection}

# bpmn2_DataInputAssociation class attributes and methods

# bpmn2_DataStore class attributes and methods
bpmn2_DataStore_capacity: Property = Property(name="capacity", type=IntegerType)
bpmn2_DataStore_isUnlimited: Property = Property(name="isUnlimited", type=BooleanType)
bpmn2_DataStore.attributes={bpmn2_DataStore_isUnlimited, bpmn2_DataStore_capacity}

# bpmn2_DataStoreReference class attributes and methods

# bpmn2_DataOutput class attributes and methods
bpmn2_DataOutput_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_DataOutput.attributes={bpmn2_DataOutput_isCollection}

# bpmn2_DataOutputAssociation class attributes and methods

# bpmn2_DataState class attributes and methods

# bpmn2_ErrorEventDefinition class attributes and methods

# bpmn2_Escalation class attributes and methods
bpmn2_Escalation_escalationCode: Property = Property(name="escalationCode", type=StringType)
bpmn2_Escalation.attributes={bpmn2_Escalation_escalationCode}

# bpmn2_Definitions class attributes and methods
bpmn2_Definitions_exporter: Property = Property(name="exporter", type=StringType)
bpmn2_Definitions_exporterVersion: Property = Property(name="exporterVersion", type=StringType)
bpmn2_Definitions_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
bpmn2_Definitions_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
bpmn2_Definitions_typeLanguage: Property = Property(name="typeLanguage", type=StringType)
bpmn2_Definitions.attributes={bpmn2_Definitions_exporter, bpmn2_Definitions_targetNamespace, bpmn2_Definitions_typeLanguage, bpmn2_Definitions_expressionLanguage, bpmn2_Definitions_exporterVersion}

# bpmn2_Documentation class attributes and methods
bpmn2_Documentation_mixed: Property = Property(name="mixed", type=StringType)
bpmn2_Documentation_text: Property = Property(name="text", type=StringType)
bpmn2_Documentation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_Documentation.attributes={bpmn2_Documentation_text, bpmn2_Documentation_mixed, bpmn2_Documentation_textFormat}

# bpmn2_EndEvent class attributes and methods

# bpmn2_EndPoint class attributes and methods

# bpmn2_Error class attributes and methods
bpmn2_Error_errorCode: Property = Property(name="errorCode", type=StringType)
bpmn2_Error.attributes={bpmn2_Error_errorCode}

# bpmn2_Expression class attributes and methods

# bpmn2_Extension class attributes and methods
bpmn2_Extension_mustUnderstand: Property = Property(name="mustUnderstand", type=BooleanType)
bpmn2_Extension_xsdDefinition: Property = Property(name="xsdDefinition", type=StringType)
bpmn2_Extension.attributes={bpmn2_Extension_xsdDefinition, bpmn2_Extension_mustUnderstand}

# bpmn2_ExtensionAttributeValue class attributes and methods
bpmn2_ExtensionAttributeValue_value: Property = Property(name="value", type=StringType)
bpmn2_ExtensionAttributeValue.attributes={bpmn2_ExtensionAttributeValue_value}

# bpmn2_EscalationEventDefinition class attributes and methods

# bpmn2_Event class attributes and methods

# bpmn2_EventBasedGateway class attributes and methods
bpmn2_EventBasedGateway_eventGatewayType: Property = Property(name="eventGatewayType", type=StringType)
bpmn2_EventBasedGateway_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_EventBasedGateway.attributes={bpmn2_EventBasedGateway_eventGatewayType, bpmn2_EventBasedGateway_instantiate}

# bpmn2_ExclusiveGateway class attributes and methods

# bpmn2_GlobalChoreographyTask class attributes and methods

# bpmn2_GlobalConversation class attributes and methods

# bpmn2_FlowNode class attributes and methods

# bpmn2_FormalExpression class attributes and methods
bpmn2_FormalExpression_mixed: Property = Property(name="mixed", type=StringType)
bpmn2_FormalExpression_body: Property = Property(name="body", type=StringType)
bpmn2_FormalExpression_language: Property = Property(name="language", type=StringType)
bpmn2_FormalExpression.attributes={bpmn2_FormalExpression_language, bpmn2_FormalExpression_mixed, bpmn2_FormalExpression_body}

# bpmn2_Gateway class attributes and methods
bpmn2_Gateway_gatewayDirection: Property = Property(name="gatewayDirection", type=StringType)
bpmn2_Gateway.attributes={bpmn2_Gateway_gatewayDirection}

# bpmn2_GlobalBusinessRuleTask class attributes and methods
bpmn2_GlobalBusinessRuleTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalBusinessRuleTask.attributes={bpmn2_GlobalBusinessRuleTask_implementation}

# bpmn2_GlobalUserTask class attributes and methods
bpmn2_GlobalUserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_GlobalUserTask.attributes={bpmn2_GlobalUserTask_implementation}

# bpmn2_Group class attributes and methods

# bpmn2_GlobalManualTask class attributes and methods

# bpmn2_GlobalScriptTask class attributes and methods
bpmn2_GlobalScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_GlobalScriptTask_scriptLanguage: Property = Property(name="scriptLanguage", type=StringType)
bpmn2_GlobalScriptTask.attributes={bpmn2_GlobalScriptTask_scriptLanguage, bpmn2_GlobalScriptTask_script}

# bpmn2_GlobalTask class attributes and methods

# bpmn2_ImplicitThrowEvent class attributes and methods

# bpmn2_Import class attributes and methods
bpmn2_Import_importType: Property = Property(name="importType", type=StringType)
bpmn2_Import_location: Property = Property(name="location", type=StringType)
bpmn2_Import_namespace: Property = Property(name="namespace", type=StringType)
bpmn2_Import.attributes={bpmn2_Import_location, bpmn2_Import_namespace, bpmn2_Import_importType}

# bpmn2_HumanPerformer class attributes and methods

# bpmn2_Performer class attributes and methods

# bpmn2_ResourceRole class attributes and methods

# bpmn2_IntermediateCatchEvent class attributes and methods

# bpmn2_IntermediateThrowEvent class attributes and methods

# bpmn2_InclusiveGateway class attributes and methods

# bpmn2_InputSet class attributes and methods

# bpmn2_Interface class attributes and methods

# bpmn2_Lane class attributes and methods

# bpmn2_LaneSet class attributes and methods

# bpmn2_InputOutputBinding class attributes and methods

# bpmn2_InputOutputSpecification class attributes and methods

# bpmn2_ItemDefinition class attributes and methods
bpmn2_ItemDefinition_isCollection: Property = Property(name="isCollection", type=BooleanType)
bpmn2_ItemDefinition_itemKind: Property = Property(name="itemKind", type=StringType)
bpmn2_ItemDefinition.attributes={bpmn2_ItemDefinition_itemKind, bpmn2_ItemDefinition_isCollection}

# bpmn2_Message class attributes and methods

# bpmn2_LinkEventDefinition class attributes and methods

# bpmn2_LoopCharacteristics class attributes and methods

# bpmn2_ManualTask class attributes and methods

# bpmn2_Monitoring class attributes and methods

# bpmn2_MultiInstanceLoopCharacteristics class attributes and methods
bpmn2_MultiInstanceLoopCharacteristics_behavior: Property = Property(name="behavior", type=StringType)
bpmn2_MultiInstanceLoopCharacteristics_isSequential: Property = Property(name="isSequential", type=BooleanType)
bpmn2_MultiInstanceLoopCharacteristics.attributes={bpmn2_MultiInstanceLoopCharacteristics_isSequential, bpmn2_MultiInstanceLoopCharacteristics_behavior}

# bpmn2_MessageEventDefinition class attributes and methods

# bpmn2_MessageFlow class attributes and methods

# bpmn2_MessageFlowAssociation class attributes and methods

# bpmn2_Participant class attributes and methods

# bpmn2_ParticipantAssociation class attributes and methods

# bpmn2_Operation class attributes and methods

# bpmn2_OutputSet class attributes and methods

# bpmn2_ParallelGateway class attributes and methods

# bpmn2_Property class attributes and methods

# bpmn2_ReceiveTask class attributes and methods
bpmn2_ReceiveTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ReceiveTask_instantiate: Property = Property(name="instantiate", type=BooleanType)
bpmn2_ReceiveTask.attributes={bpmn2_ReceiveTask_implementation, bpmn2_ReceiveTask_instantiate}

# bpmn2_ParticipantMultiplicity class attributes and methods
bpmn2_ParticipantMultiplicity_maximum: Property = Property(name="maximum", type=IntegerType)
bpmn2_ParticipantMultiplicity_minimum: Property = Property(name="minimum", type=IntegerType)
bpmn2_ParticipantMultiplicity.attributes={bpmn2_ParticipantMultiplicity_minimum, bpmn2_ParticipantMultiplicity_maximum}

# bpmn2_PartnerEntity class attributes and methods

# bpmn2_PartnerRole class attributes and methods

# bpmn2_PotentialOwner class attributes and methods

# bpmn2_Process class attributes and methods
bpmn2_Process_isClosed: Property = Property(name="isClosed", type=BooleanType)
bpmn2_Process_isExecutable: Property = Property(name="isExecutable", type=BooleanType)
bpmn2_Process_processType: Property = Property(name="processType", type=StringType)
bpmn2_Process.attributes={bpmn2_Process_processType, bpmn2_Process_isClosed, bpmn2_Process_isExecutable}

# bpmn2_ResourceAssignmentExpression class attributes and methods

# bpmn2_Relationship class attributes and methods
bpmn2_Relationship_direction: Property = Property(name="direction", type=StringType)
bpmn2_Relationship_type: Property = Property(name="type", type=StringType)
bpmn2_Relationship.attributes={bpmn2_Relationship_type, bpmn2_Relationship_direction}

# bpmn2_Rendering class attributes and methods

# bpmn2_Resource class attributes and methods

# bpmn2_ScriptTask class attributes and methods
bpmn2_ScriptTask_script: Property = Property(name="script", type=StringType)
bpmn2_ScriptTask_scriptFormat: Property = Property(name="scriptFormat", type=StringType)
bpmn2_ScriptTask.attributes={bpmn2_ScriptTask_scriptFormat, bpmn2_ScriptTask_script}

# bpmn2_SendTask class attributes and methods
bpmn2_SendTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_SendTask.attributes={bpmn2_SendTask_implementation}

# bpmn2_ResourceParameter class attributes and methods
bpmn2_ResourceParameter_isRequired: Property = Property(name="isRequired", type=BooleanType)
bpmn2_ResourceParameter.attributes={bpmn2_ResourceParameter_isRequired}

# bpmn2_ResourceParameterBinding class attributes and methods

# bpmn2_EObject class attributes and methods

# bpmn2_SignalEventDefinition class attributes and methods

# bpmn2_SequenceFlow class attributes and methods
bpmn2_SequenceFlow_isImmediate: Property = Property(name="isImmediate", type=BooleanType)
bpmn2_SequenceFlow.attributes={bpmn2_SequenceFlow_isImmediate}

# bpmn2_ServiceTask class attributes and methods
bpmn2_ServiceTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_ServiceTask.attributes={bpmn2_ServiceTask_implementation}

# bpmn2_Signal class attributes and methods

# bpmn2_SubConversation class attributes and methods

# bpmn2_SubProcess class attributes and methods
bpmn2_SubProcess_triggeredByEvent: Property = Property(name="triggeredByEvent", type=BooleanType)
bpmn2_SubProcess.attributes={bpmn2_SubProcess_triggeredByEvent}

# bpmn2_StandardLoopCharacteristics class attributes and methods
bpmn2_StandardLoopCharacteristics_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
bpmn2_StandardLoopCharacteristics_testBefore: Property = Property(name="testBefore", type=BooleanType)
bpmn2_StandardLoopCharacteristics.attributes={bpmn2_StandardLoopCharacteristics_loopMaximum, bpmn2_StandardLoopCharacteristics_testBefore}

# bpmn2_StartEvent class attributes and methods
bpmn2_StartEvent_isInterrupting: Property = Property(name="isInterrupting", type=BooleanType)
bpmn2_StartEvent.attributes={bpmn2_StartEvent_isInterrupting}

# bpmn2_SubChoreography class attributes and methods

# bpmn2_TextAnnotation class attributes and methods
bpmn2_TextAnnotation_text: Property = Property(name="text", type=StringType)
bpmn2_TextAnnotation_textFormat: Property = Property(name="textFormat", type=StringType)
bpmn2_TextAnnotation.attributes={bpmn2_TextAnnotation_textFormat, bpmn2_TextAnnotation_text}

# bpmn2_Task class attributes and methods

# bpmn2_TerminateEventDefinition class attributes and methods

# bpmn2_ThrowEvent class attributes and methods

# bpmn2_TimerEventDefinition class attributes and methods

# bpmn2_Transaction class attributes and methods
bpmn2_Transaction_protocol: Property = Property(name="protocol", type=StringType)
bpmn2_Transaction_method: Property = Property(name="method", type=StringType)
bpmn2_Transaction.attributes={bpmn2_Transaction_method, bpmn2_Transaction_protocol}

# bpmn2_UserTask class attributes and methods
bpmn2_UserTask_implementation: Property = Property(name="implementation", type=StringType)
bpmn2_UserTask.attributes={bpmn2_UserTask_implementation}

# FlowNode class attributes and methods

# SubProcess class attributes and methods

# bpmn2_Competency class attributes and methods

# bpmn2_Criterion class attributes and methods

# bpmn2_OrganisationalUnit class attributes and methods

# bpmn2_Position class attributes and methods

# bpmn2_Role class attributes and methods

# CatchEvent class attributes and methods

# Task class attributes and methods

# Activity class attributes and methods

# BaseElement class attributes and methods

# Artifact class attributes and methods

# bpmn2_ExtensionDefinition class attributes and methods
bpmn2_ExtensionDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionDefinition.attributes={bpmn2_ExtensionDefinition_name}

# ChoreographyActivity class attributes and methods

# ConversationNode class attributes and methods

# RootElement class attributes and methods

# EventDefinition class attributes and methods

# Event class attributes and methods

# Collaboration class attributes and methods

# FlowElementsContainer class attributes and methods

# Gateway class attributes and methods

# bpmn2_InteractionNode class attributes and methods

# InteractionNode class attributes and methods

# FlowElement class attributes and methods

# bpmn2_ItemAwareElement class attributes and methods

# ItemAwareElement class attributes and methods

# bpmn2_Document class attributes and methods

# DataAssociation class attributes and methods

# bpmn2_BPMNDiagram class attributes and methods

# ThrowEvent class attributes and methods

# bpmn2_FlowElementsContainer class attributes and methods

# bpmn2_ExtensionAttributeDefinition class attributes and methods
bpmn2_ExtensionAttributeDefinition_name: Property = Property(name="name", type=StringType)
bpmn2_ExtensionAttributeDefinition_type: Property = Property(name="type", type=StringType)
bpmn2_ExtensionAttributeDefinition_isReference: Property = Property(name="isReference", type=BooleanType)
bpmn2_ExtensionAttributeDefinition.attributes={bpmn2_ExtensionAttributeDefinition_name, bpmn2_ExtensionAttributeDefinition_isReference, bpmn2_ExtensionAttributeDefinition_type}

# CallableElement class attributes and methods

# Expression class attributes and methods

# GlobalTask class attributes and methods

# Choreography class attributes and methods

# Performer class attributes and methods

# LoopCharacteristics class attributes and methods

# ResourceRole class attributes and methods

# HumanPerformer class attributes and methods

# Relationships
callableElement27: BinaryAssociation = BinaryAssociation(
    name="callableElement27",
    ends={
        Property(name="bpmn2_CallableElement", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot28", type=bpmn2_CallableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
callActivity29: BinaryAssociation = BinaryAssociation(
    name="callActivity29",
    ends={
        Property(name="bpmn2_CallActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot30", type=bpmn2_CallActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifact10: BinaryAssociation = BinaryAssociation(
    name="artifact10",
    ends={
        Property(name="bpmn2_Artifact", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot11", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment12: BinaryAssociation = BinaryAssociation(
    name="assignment12",
    ends={
        Property(name="bpmn2_Assignment", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot13", type=bpmn2_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callChoreography31: BinaryAssociation = BinaryAssociation(
    name="callChoreography31",
    ends={
        Property(name="bpmn2_CallChoreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot32", type=bpmn2_CallChoreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
businessRuleTask25: BinaryAssociation = BinaryAssociation(
    name="businessRuleTask25",
    ends={
        Property(name="bpmn2_BusinessRuleTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot26", type=bpmn2_BusinessRuleTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity4: BinaryAssociation = BinaryAssociation(
    name="activity4",
    ends={
        Property(name="bpmn2_Activity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot5", type=bpmn2_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
compensateEventDefinition57: BinaryAssociation = BinaryAssociation(
    name="compensateEventDefinition57",
    ends={
        Property(name="bpmn2_CompensateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot58", type=bpmn2_CompensateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexBehaviorDefinition59: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition59",
    ends={
        Property(name="bpmn2_ComplexBehaviorDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot60", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexGateway61: BinaryAssociation = BinaryAssociation(
    name="complexGateway61",
    ends={
        Property(name="bpmn2_ComplexGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot62", type=bpmn2_ComplexGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValue47: BinaryAssociation = BinaryAssociation(
    name="categoryValue47",
    ends={
        Property(name="bpmn2_CategoryValue", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot48", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreography49: BinaryAssociation = BinaryAssociation(
    name="choreography49",
    ends={
        Property(name="bpmn2_Choreography", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot50", type=bpmn2_Choreography, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaboration51: BinaryAssociation = BinaryAssociation(
    name="collaboration51",
    ends={
        Property(name="bpmn2_Collaboration", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot52", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyActivity53: BinaryAssociation = BinaryAssociation(
    name="choreographyActivity53",
    ends={
        Property(name="bpmn2_ChoreographyActivity", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot54", type=bpmn2_ChoreographyActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choreographyTask55: BinaryAssociation = BinaryAssociation(
    name="choreographyTask55",
    ends={
        Property(name="bpmn2_ChoreographyTask", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot56", type=bpmn2_ChoreographyTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
dataObject87: BinaryAssociation = BinaryAssociation(
    name="dataObject87",
    ends={
        Property(name="bpmn2_DataObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot88", type=bpmn2_DataObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjectReference89: BinaryAssociation = BinaryAssociation(
    name="dataObjectReference89",
    ends={
        Property(name="bpmn2_DataObjectReference", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot90", type=bpmn2_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationPropertyRetrievalExpression77: BinaryAssociation = BinaryAssociation(
    name="correlationPropertyRetrievalExpression77",
    ends={
        Property(name="bpmn2_CorrelationPropertyRetrievalExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot78", type=bpmn2_CorrelationPropertyRetrievalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscription79: BinaryAssociation = BinaryAssociation(
    name="correlationSubscription79",
    ends={
        Property(name="bpmn2_CorrelationSubscription", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot80", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataAssociation81: BinaryAssociation = BinaryAssociation(
    name="dataAssociation81",
    ends={
        Property(name="bpmn2_DataAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot82", type=bpmn2_DataAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInput83: BinaryAssociation = BinaryAssociation(
    name="dataInput83",
    ends={
        Property(name="bpmn2_DataInput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot84", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation85: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation85",
    ends={
        Property(name="bpmn2_DataInputAssociation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot86", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
dataOutput91: BinaryAssociation = BinaryAssociation(
    name="dataOutput91",
    ends={
        Property(name="bpmn2_DataOutput", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot92", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
error109: BinaryAssociation = BinaryAssociation(
    name="error109",
    ends={
        Property(name="bpmn2_Error", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot110", type=bpmn2_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
escalationEventDefinition115: BinaryAssociation = BinaryAssociation(
    name="escalationEventDefinition115",
    ends={
        Property(name="bpmn2_EscalationEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot116", type=bpmn2_EscalationEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
flowNode129: BinaryAssociation = BinaryAssociation(
    name="flowNode129",
    ends={
        Property(name="bpmn2_FlowNode", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot130", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
implicitThrowEvent157: BinaryAssociation = BinaryAssociation(
    name="implicitThrowEvent157",
    ends={
        Property(name="bpmn2_ImplicitThrowEvent", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot158", type=bpmn2_ImplicitThrowEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import_159: BinaryAssociation = BinaryAssociation(
    name="import_159",
    ends={
        Property(name="bpmn2_Import", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot160", type=bpmn2_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
resourceRole155: BinaryAssociation = BinaryAssociation(
    name="resourceRole155",
    ends={
        Property(name="bpmn2_ResourceRole", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot156", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
inclusiveGateway161: BinaryAssociation = BinaryAssociation(
    name="inclusiveGateway161",
    ends={
        Property(name="bpmn2_InclusiveGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot162", type=bpmn2_InclusiveGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
lane177: BinaryAssociation = BinaryAssociation(
    name="lane177",
    ends={
        Property(name="bpmn2_Lane", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot178", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ioBinding171: BinaryAssociation = BinaryAssociation(
    name="ioBinding171",
    ends={
        Property(name="bpmn2_InputOutputBinding", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot172", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
message187: BinaryAssociation = BinaryAssociation(
    name="message187",
    ends={
        Property(name="bpmn2_Message", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot188", type=bpmn2_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laneSet179: BinaryAssociation = BinaryAssociation(
    name="laneSet179",
    ends={
        Property(name="bpmn2_LaneSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot180", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
monitoring195: BinaryAssociation = BinaryAssociation(
    name="monitoring195",
    ends={
        Property(name="bpmn2_Monitoring", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot196", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
outputSet201: BinaryAssociation = BinaryAssociation(
    name="outputSet201",
    ends={
        Property(name="bpmn2_OutputSet", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot202", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallelGateway203: BinaryAssociation = BinaryAssociation(
    name="parallelGateway203",
    ends={
        Property(name="bpmn2_ParallelGateway", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot204", type=bpmn2_ParallelGateway, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
process217: BinaryAssociation = BinaryAssociation(
    name="process217",
    ends={
        Property(name="bpmn2_Process", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot218", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression229: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression229",
    ends={
        Property(name="bpmn2_ResourceAssignmentExpression", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot230", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship223: BinaryAssociation = BinaryAssociation(
    name="relationship223",
    ends={
        Property(name="bpmn2_Relationship", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot224", type=bpmn2_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
script235: BinaryAssociation = BinaryAssociation(
    name="script235",
    ends={
        Property(name="bpmn2_EObject", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot236", type=bpmn2_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalEventDefinition247: BinaryAssociation = BinaryAssociation(
    name="signalEventDefinition247",
    ends={
        Property(name="bpmn2_SignalEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot248", type=bpmn2_SignalEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceFlow241: BinaryAssociation = BinaryAssociation(
    name="sequenceFlow241",
    ends={
        Property(name="bpmn2_SequenceFlow", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot242", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
subConversation255: BinaryAssociation = BinaryAssociation(
    name="subConversation255",
    ends={
        Property(name="bpmn2_SubConversation", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot256", type=bpmn2_SubConversation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
terminateEventDefinition261: BinaryAssociation = BinaryAssociation(
    name="terminateEventDefinition261",
    ends={
        Property(name="bpmn2_TerminateEventDefinition", type=bpmn2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DocumentRoot262", type=bpmn2_TerminateEventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
attachedToRef340: BinaryAssociation = BinaryAssociation(
    name="attachedToRef340",
    ends={
        Property(name="Activity", type=bpmn2_BoundaryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="boundaryEventRefs", type=bpmn2_Activity, multiplicity=Multiplicity(1, 1))
    }
)
from_320: BinaryAssociation = BinaryAssociation(
    name="from_320",
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
categoryValue380: BinaryAssociation = BinaryAssociation(
    name="categoryValue380",
    ends={
        Property(name="bpmn2_CategoryValue382", type=bpmn2_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Category381", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
messageFlowRef395: BinaryAssociation = BinaryAssociation(
    name="messageFlowRef395",
    ends={
        Property(name="bpmn2_MessageFlow397", type=bpmn2_ChoreographyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ChoreographyTask396", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 2))
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
correlationKeys419: BinaryAssociation = BinaryAssociation(
    name="correlationKeys419",
    ends={
        Property(name="bpmn2_CorrelationKey421", type=bpmn2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Collaboration420", type=bpmn2_CorrelationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
participantRefs457: BinaryAssociation = BinaryAssociation(
    name="participantRefs457",
    ends={
        Property(name="bpmn2_Participant459", type=bpmn2_ConversationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ConversationNode458", type=bpmn2_Participant, multiplicity=Multiplicity(2, 9999))
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
dataPath475: BinaryAssociation = BinaryAssociation(
    name="dataPath475",
    ends={
        Property(name="bpmn2_FormalExpression477", type=bpmn2_CorrelationPropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_CorrelationPropertyBinding476", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="DocumentAndKnowledge.ecoreDocument", type=bpmn2_DataInput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInput", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams532: BinaryAssociation = BinaryAssociation(
    name="diagrams532",
    ends={
        Property(name="bpmn2_BPMNDiagram", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions533", type=bpmn2_BPMNDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships534: BinaryAssociation = BinaryAssociation(
    name="relationships534",
    ends={
        Property(name="bpmn2_Relationship536", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions535", type=bpmn2_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
referencesDocument518: BinaryAssociation = BinaryAssociation(
    name="referencesDocument518",
    ends={
        Property(name="DocumentAndKnowledge.ecoreDocument519", type=bpmn2_DataOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="dataOutput", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
dataStoreRef520: BinaryAssociation = BinaryAssociation(
    name="dataStoreRef520",
    ends={
        Property(name="bpmn2_DataStore522", type=bpmn2_DataStoreReference, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_DataStoreReference521", type=bpmn2_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
imports523: BinaryAssociation = BinaryAssociation(
    name="imports523",
    ends={
        Property(name="bpmn2_Import525", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions524", type=bpmn2_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions526: BinaryAssociation = BinaryAssociation(
    name="extensions526",
    ends={
        Property(name="bpmn2_Extension528", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions527", type=bpmn2_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootElements529: BinaryAssociation = BinaryAssociation(
    name="rootElements529",
    ends={
        Property(name="bpmn2_RootElement531", type=bpmn2_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Definitions530", type=bpmn2_RootElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default552: BinaryAssociation = BinaryAssociation(
    name="default552",
    ends={
        Property(name="bpmn2_SequenceFlow554", type=bpmn2_ExclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExclusiveGateway553", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
definition555: BinaryAssociation = BinaryAssociation(
    name="definition555",
    ends={
        Property(name="bpmn2_ExtensionDefinition557", type=bpmn2_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Extension556", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structureRef537: BinaryAssociation = BinaryAssociation(
    name="structureRef537",
    ends={
        Property(name="bpmn2_ItemDefinition539", type=bpmn2_Error, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Error538", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
errorRef540: BinaryAssociation = BinaryAssociation(
    name="errorRef540",
    ends={
        Property(name="bpmn2_Error542", type=bpmn2_ErrorEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ErrorEventDefinition541", type=bpmn2_Error, multiplicity=Multiplicity(0, 1))
    }
)
structureRef543: BinaryAssociation = BinaryAssociation(
    name="structureRef543",
    ends={
        Property(name="bpmn2_ItemDefinition545", type=bpmn2_Escalation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Escalation544", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
escalationRef546: BinaryAssociation = BinaryAssociation(
    name="escalationRef546",
    ends={
        Property(name="bpmn2_Escalation548", type=bpmn2_EscalationEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_EscalationEventDefinition547", type=bpmn2_Escalation, multiplicity=Multiplicity(0, 1))
    }
)
properties549: BinaryAssociation = BinaryAssociation(
    name="properties549",
    ends={
        Property(name="bpmn2_Property551", type=bpmn2_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Event550", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValueRef571: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef571",
    ends={
        Property(name="bpmn2_CategoryValue573", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement572", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 9999))
    }
)
laneSets574: BinaryAssociation = BinaryAssociation(
    name="laneSets574",
    ends={
        Property(name="bpmn2_LaneSet575", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElements576: BinaryAssociation = BinaryAssociation(
    name="flowElements576",
    ends={
        Property(name="bpmn2_FlowElement578", type=bpmn2_FlowElementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElementsContainer577", type=bpmn2_FlowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefinition558: BinaryAssociation = BinaryAssociation(
    name="extensionDefinition558",
    ends={
        Property(name="ExtensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionAttributeDefinitions", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
valueRef559: BinaryAssociation = BinaryAssociation(
    name="valueRef559",
    ends={
        Property(name="bpmn2_EObject561", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue560", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
extensionAttributeDefinition562: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinition562",
    ends={
        Property(name="bpmn2_ExtensionAttributeDefinition", type=bpmn2_ExtensionAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ExtensionAttributeValue563", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
extensionAttributeDefinitions564: BinaryAssociation = BinaryAssociation(
    name="extensionAttributeDefinitions564",
    ends={
        Property(name="ExtensionAttributeDefinition", type=bpmn2_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionDefinition", type=bpmn2_ExtensionAttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auditing565: BinaryAssociation = BinaryAssociation(
    name="auditing565",
    ends={
        Property(name="bpmn2_Auditing567", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement566", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring568: BinaryAssociation = BinaryAssociation(
    name="monitoring568",
    ends={
        Property(name="bpmn2_Monitoring570", type=bpmn2_FlowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FlowElement569", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initiatingParticipantRef586: BinaryAssociation = BinaryAssociation(
    name="initiatingParticipantRef586",
    ends={
        Property(name="bpmn2_GlobalChoreographyTask587", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant588", type=bpmn2_GlobalChoreographyTask, multiplicity=Multiplicity(1, 1))
    }
)
resources589: BinaryAssociation = BinaryAssociation(
    name="resources589",
    ends={
        Property(name="bpmn2_ResourceRole591", type=bpmn2_GlobalTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalTask590", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming579: BinaryAssociation = BinaryAssociation(
    name="incoming579",
    ends={
        Property(name="SequenceFlow", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
lanes580: BinaryAssociation = BinaryAssociation(
    name="lanes580",
    ends={
        Property(name="Lane", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="flowNodeRefs", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing581: BinaryAssociation = BinaryAssociation(
    name="outgoing581",
    ends={
        Property(name="SequenceFlow582", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceRef", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 9999))
    }
)
evaluatesToTypeRef583: BinaryAssociation = BinaryAssociation(
    name="evaluatesToTypeRef583",
    ends={
        Property(name="bpmn2_ItemDefinition585", type=bpmn2_FormalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_FormalExpression584", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1))
    }
)
dataInputs610: BinaryAssociation = BinaryAssociation(
    name="dataInputs610",
    ends={
        Property(name="bpmn2_DataInput612", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification611", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputs613: BinaryAssociation = BinaryAssociation(
    name="dataOutputs613",
    ends={
        Property(name="bpmn2_DataOutput615", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification614", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSets616: BinaryAssociation = BinaryAssociation(
    name="inputSets616",
    ends={
        Property(name="bpmn2_InputSet618", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification617", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputSets619: BinaryAssociation = BinaryAssociation(
    name="outputSets619",
    ends={
        Property(name="bpmn2_OutputSet621", type=bpmn2_InputOutputSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputSpecification620", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
renderings592: BinaryAssociation = BinaryAssociation(
    name="renderings592",
    ends={
        Property(name="bpmn2_Rendering594", type=bpmn2_GlobalUserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_GlobalUserTask593", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryValueRef595: BinaryAssociation = BinaryAssociation(
    name="categoryValueRef595",
    ends={
        Property(name="bpmn2_CategoryValue597", type=bpmn2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Group596", type=bpmn2_CategoryValue, multiplicity=Multiplicity(0, 1))
    }
)
default598: BinaryAssociation = BinaryAssociation(
    name="default598",
    ends={
        Property(name="bpmn2_SequenceFlow600", type=bpmn2_InclusiveGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InclusiveGateway599", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(0, 1))
    }
)
inputDataRef601: BinaryAssociation = BinaryAssociation(
    name="inputDataRef601",
    ends={
        Property(name="bpmn2_InputSet603", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding602", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1))
    }
)
operationRef604: BinaryAssociation = BinaryAssociation(
    name="operationRef604",
    ends={
        Property(name="bpmn2_Operation606", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding605", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1))
    }
)
outputDataRef607: BinaryAssociation = BinaryAssociation(
    name="outputDataRef607",
    ends={
        Property(name="bpmn2_OutputSet609", type=bpmn2_InputOutputBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InputOutputBinding608", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConversationLinks633: BinaryAssociation = BinaryAssociation(
    name="outgoingConversationLinks633",
    ends={
        Property(name="bpmn2_ConversationLink635", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InteractionNode634", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
operations636: BinaryAssociation = BinaryAssociation(
    name="operations636",
    ends={
        Property(name="bpmn2_Operation638", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface637", type=bpmn2_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implementationRef639: BinaryAssociation = BinaryAssociation(
    name="implementationRef639",
    ends={
        Property(name="bpmn2_EObject641", type=bpmn2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Interface640", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
dataInputRefs622: BinaryAssociation = BinaryAssociation(
    name="dataInputRefs622",
    ends={
        Property(name="DataInput", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInputRefs623: BinaryAssociation = BinaryAssociation(
    name="optionalInputRefs623",
    ends={
        Property(name="DataInput624", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithOptional", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingInputRefs625: BinaryAssociation = BinaryAssociation(
    name="whileExecutingInputRefs625",
    ends={
        Property(name="DataInput626", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetWithWhileExecuting", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999))
    }
)
outputSetRefs627: BinaryAssociation = BinaryAssociation(
    name="outputSetRefs627",
    ends={
        Property(name="OutputSet629", type=bpmn2_InputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="inputSetRefs628", type=bpmn2_OutputSet, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConversationLinks630: BinaryAssociation = BinaryAssociation(
    name="incomingConversationLinks630",
    ends={
        Property(name="bpmn2_ConversationLink632", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_InteractionNode631", type=bpmn2_ConversationLink, multiplicity=Multiplicity(0, 9999))
    }
)
flowNodeRefs657: BinaryAssociation = BinaryAssociation(
    name="flowNodeRefs657",
    ends={
        Property(name="FlowNode", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmn2_FlowNode, multiplicity=Multiplicity(0, 9999))
    }
)
childLaneSet658: BinaryAssociation = BinaryAssociation(
    name="childLaneSet658",
    ends={
        Property(name="bpmn2_LaneSet660", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane659", type=bpmn2_LaneSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partitionElementRef661: BinaryAssociation = BinaryAssociation(
    name="partitionElementRef661",
    ends={
        Property(name="bpmn2_BaseElement663", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane662", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
representsPerformer664: BinaryAssociation = BinaryAssociation(
    name="representsPerformer664",
    ends={
        Property(name="bpmn2_Performer666", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane665", type=bpmn2_Performer, multiplicity=Multiplicity(0, 9999))
    }
)
representsRole667: BinaryAssociation = BinaryAssociation(
    name="representsRole667",
    ends={
        Property(name="bpmn2_Role669", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane668", type=bpmn2_Role, multiplicity=Multiplicity(0, 9999))
    }
)
dataState642: BinaryAssociation = BinaryAssociation(
    name="dataState642",
    ends={
        Property(name="bpmn2_DataState644", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement643", type=bpmn2_DataState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemSubjectRef645: BinaryAssociation = BinaryAssociation(
    name="itemSubjectRef645",
    ends={
        Property(name="bpmn2_ItemDefinition647", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemAwareElement646", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
import_648: BinaryAssociation = BinaryAssociation(
    name="import_648",
    ends={
        Property(name="bpmn2_Import650", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition649", type=bpmn2_Import, multiplicity=Multiplicity(0, 1))
    }
)
structureRef651: BinaryAssociation = BinaryAssociation(
    name="structureRef651",
    ends={
        Property(name="bpmn2_EObject653", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ItemDefinition652", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
partitionElement654: BinaryAssociation = BinaryAssociation(
    name="partitionElement654",
    ends={
        Property(name="bpmn2_BaseElement656", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane655", type=bpmn2_BaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source683: BinaryAssociation = BinaryAssociation(
    name="source683",
    ends={
        Property(name="LinkEventDefinition", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
target685: BinaryAssociation = BinaryAssociation(
    name="target685",
    ends={
        Property(name="LinkEventDefinition686", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmn2_LinkEventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
itemRef687: BinaryAssociation = BinaryAssociation(
    name="itemRef687",
    ends={
        Property(name="bpmn2_ItemDefinition689", type=bpmn2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Message688", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
representsOrganisationalUnit670: BinaryAssociation = BinaryAssociation(
    name="representsOrganisationalUnit670",
    ends={
        Property(name="bpmn2_OrganisationalUnit672", type=bpmn2_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Lane671", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
messages673: BinaryAssociation = BinaryAssociation(
    name="messages673",
    ends={
        Property(name="bpmn2_MessageFlow675", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet674", type=bpmn2_MessageFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lanes676: BinaryAssociation = BinaryAssociation(
    name="lanes676",
    ends={
        Property(name="bpmn2_Lane678", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet677", type=bpmn2_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representsOrganisationalUnit679: BinaryAssociation = BinaryAssociation(
    name="representsOrganisationalUnit679",
    ends={
        Property(name="bpmn2_OrganisationalUnit681", type=bpmn2_LaneSet, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_LaneSet680", type=bpmn2_OrganisationalUnit, multiplicity=Multiplicity(0, 9999))
    }
)
loopCardinality711: BinaryAssociation = BinaryAssociation(
    name="loopCardinality711",
    ends={
        Property(name="bpmn2_Expression713", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics712", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopDataInputRef714: BinaryAssociation = BinaryAssociation(
    name="loopDataInputRef714",
    ends={
        Property(name="bpmn2_ItemAwareElement716", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics715", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
loopDataOutputRef717: BinaryAssociation = BinaryAssociation(
    name="loopDataOutputRef717",
    ends={
        Property(name="bpmn2_ItemAwareElement719", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics718", type=bpmn2_ItemAwareElement, multiplicity=Multiplicity(0, 1))
    }
)
inputDataItem720: BinaryAssociation = BinaryAssociation(
    name="inputDataItem720",
    ends={
        Property(name="bpmn2_DataInput722", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics721", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationRef690: BinaryAssociation = BinaryAssociation(
    name="operationRef690",
    ends={
        Property(name="bpmn2_Operation692", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition691", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
messageRef693: BinaryAssociation = BinaryAssociation(
    name="messageRef693",
    ends={
        Property(name="bpmn2_Message695", type=bpmn2_MessageEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageEventDefinition694", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
messageRef696: BinaryAssociation = BinaryAssociation(
    name="messageRef696",
    ends={
        Property(name="bpmn2_Message698", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow697", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
sourceRef699: BinaryAssociation = BinaryAssociation(
    name="sourceRef699",
    ends={
        Property(name="bpmn2_InteractionNode701", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow700", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
targetRef702: BinaryAssociation = BinaryAssociation(
    name="targetRef702",
    ends={
        Property(name="bpmn2_InteractionNode704", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlow703", type=bpmn2_InteractionNode, multiplicity=Multiplicity(1, 1))
    }
)
innerMessageFlowRef705: BinaryAssociation = BinaryAssociation(
    name="innerMessageFlowRef705",
    ends={
        Property(name="bpmn2_MessageFlow707", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation706", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outerMessageFlowRef708: BinaryAssociation = BinaryAssociation(
    name="outerMessageFlowRef708",
    ends={
        Property(name="bpmn2_MessageFlow710", type=bpmn2_MessageFlowAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MessageFlowAssociation709", type=bpmn2_MessageFlow, multiplicity=Multiplicity(1, 1))
    }
)
outMessageRef741: BinaryAssociation = BinaryAssociation(
    name="outMessageRef741",
    ends={
        Property(name="bpmn2_Message743", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation742", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
errorRefs744: BinaryAssociation = BinaryAssociation(
    name="errorRefs744",
    ends={
        Property(name="bpmn2_Error746", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation745", type=bpmn2_Error, multiplicity=Multiplicity(0, 9999))
    }
)
implementationRef747: BinaryAssociation = BinaryAssociation(
    name="implementationRef747",
    ends={
        Property(name="bpmn2_EObject749", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation748", type=bpmn2_EObject, multiplicity=Multiplicity(0, 1))
    }
)
dataOutputRefs750: BinaryAssociation = BinaryAssociation(
    name="dataOutputRefs750",
    ends={
        Property(name="DataOutput", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
outputDataItem723: BinaryAssociation = BinaryAssociation(
    name="outputDataItem723",
    ends={
        Property(name="bpmn2_DataOutput725", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics724", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complexBehaviorDefinition726: BinaryAssociation = BinaryAssociation(
    name="complexBehaviorDefinition726",
    ends={
        Property(name="bpmn2_ComplexBehaviorDefinition728", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics727", type=bpmn2_ComplexBehaviorDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completionCondition729: BinaryAssociation = BinaryAssociation(
    name="completionCondition729",
    ends={
        Property(name="bpmn2_Expression731", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics730", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noneBehaviorEventRef732: BinaryAssociation = BinaryAssociation(
    name="noneBehaviorEventRef732",
    ends={
        Property(name="bpmn2_EventDefinition734", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics733", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oneBehaviorEventRef735: BinaryAssociation = BinaryAssociation(
    name="oneBehaviorEventRef735",
    ends={
        Property(name="bpmn2_EventDefinition737", type=bpmn2_MultiInstanceLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_MultiInstanceLoopCharacteristics736", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 1))
    }
)
inMessageRef738: BinaryAssociation = BinaryAssociation(
    name="inMessageRef738",
    ends={
        Property(name="bpmn2_Message740", type=bpmn2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Operation739", type=bpmn2_Message, multiplicity=Multiplicity(1, 1))
    }
)
outerParticipantRef773: BinaryAssociation = BinaryAssociation(
    name="outerParticipantRef773",
    ends={
        Property(name="bpmn2_Participant775", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation774", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
participantRef776: BinaryAssociation = BinaryAssociation(
    name="participantRef776",
    ends={
        Property(name="bpmn2_Participant778", type=bpmn2_PartnerEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerEntity777", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
optionalOutputRefs751: BinaryAssociation = BinaryAssociation(
    name="optionalOutputRefs751",
    ends={
        Property(name="DataOutput752", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithOptional", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
whileExecutingOutputRefs753: BinaryAssociation = BinaryAssociation(
    name="whileExecutingOutputRefs753",
    ends={
        Property(name="DataOutput754", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetWithWhileExecuting", type=bpmn2_DataOutput, multiplicity=Multiplicity(0, 9999))
    }
)
inputSetRefs755: BinaryAssociation = BinaryAssociation(
    name="inputSetRefs755",
    ends={
        Property(name="InputSet757", type=bpmn2_OutputSet, multiplicity=Multiplicity(1, 1)),
        Property(name="outputSetRefs756", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 9999))
    }
)
interfaceRefs758: BinaryAssociation = BinaryAssociation(
    name="interfaceRefs758",
    ends={
        Property(name="bpmn2_Interface760", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant759", type=bpmn2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
endPointRefs761: BinaryAssociation = BinaryAssociation(
    name="endPointRefs761",
    ends={
        Property(name="bpmn2_EndPoint763", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant762", type=bpmn2_EndPoint, multiplicity=Multiplicity(0, 9999))
    }
)
participantMultiplicity764: BinaryAssociation = BinaryAssociation(
    name="participantMultiplicity764",
    ends={
        Property(name="bpmn2_ParticipantMultiplicity766", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant765", type=bpmn2_ParticipantMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processRef767: BinaryAssociation = BinaryAssociation(
    name="processRef767",
    ends={
        Property(name="bpmn2_Process769", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Participant768", type=bpmn2_Process, multiplicity=Multiplicity(0, 1))
    }
)
innerParticipantRef770: BinaryAssociation = BinaryAssociation(
    name="innerParticipantRef770",
    ends={
        Property(name="bpmn2_Participant772", type=bpmn2_ParticipantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ParticipantAssociation771", type=bpmn2_Participant, multiplicity=Multiplicity(1, 1))
    }
)
participantRef779: BinaryAssociation = BinaryAssociation(
    name="participantRef779",
    ends={
        Property(name="bpmn2_Participant781", type=bpmn2_PartnerRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_PartnerRole780", type=bpmn2_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
auditing782: BinaryAssociation = BinaryAssociation(
    name="auditing782",
    ends={
        Property(name="bpmn2_Auditing784", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process783", type=bpmn2_Auditing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
monitoring785: BinaryAssociation = BinaryAssociation(
    name="monitoring785",
    ends={
        Property(name="bpmn2_Monitoring787", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process786", type=bpmn2_Monitoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties788: BinaryAssociation = BinaryAssociation(
    name="properties788",
    ends={
        Property(name="bpmn2_Property790", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process789", type=bpmn2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts791: BinaryAssociation = BinaryAssociation(
    name="artifacts791",
    ends={
        Property(name="bpmn2_Artifact793", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process792", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources794: BinaryAssociation = BinaryAssociation(
    name="resources794",
    ends={
        Property(name="bpmn2_ResourceRole796", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process795", type=bpmn2_ResourceRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correlationSubscriptions797: BinaryAssociation = BinaryAssociation(
    name="correlationSubscriptions797",
    ends={
        Property(name="bpmn2_CorrelationSubscription799", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process798", type=bpmn2_CorrelationSubscription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supports801: BinaryAssociation = BinaryAssociation(
    name="supports801",
    ends={
        Property(name="bpmn2_Process802", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process800", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999))
    }
)
definitionalCollaborationRef803: BinaryAssociation = BinaryAssociation(
    name="definitionalCollaborationRef803",
    ends={
        Property(name="bpmn2_Collaboration805", type=bpmn2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Process804", type=bpmn2_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
type824: BinaryAssociation = BinaryAssociation(
    name="type824",
    ends={
        Property(name="bpmn2_ItemDefinition826", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameter825", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expression827: BinaryAssociation = BinaryAssociation(
    name="expression827",
    ends={
        Property(name="bpmn2_Expression829", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding828", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterRef830: BinaryAssociation = BinaryAssociation(
    name="parameterRef830",
    ends={
        Property(name="bpmn2_ResourceParameter832", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceParameterBinding831", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(1, 1))
    }
)
messageRef806: BinaryAssociation = BinaryAssociation(
    name="messageRef806",
    ends={
        Property(name="bpmn2_Message808", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask807", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef809: BinaryAssociation = BinaryAssociation(
    name="operationRef809",
    ends={
        Property(name="bpmn2_Operation811", type=bpmn2_ReceiveTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ReceiveTask810", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
sources812: BinaryAssociation = BinaryAssociation(
    name="sources812",
    ends={
        Property(name="bpmn2_EObject814", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship813", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
targets815: BinaryAssociation = BinaryAssociation(
    name="targets815",
    ends={
        Property(name="bpmn2_EObject817", type=bpmn2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Relationship816", type=bpmn2_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
resourceParameters818: BinaryAssociation = BinaryAssociation(
    name="resourceParameters818",
    ends={
        Property(name="bpmn2_ResourceParameter820", type=bpmn2_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Resource819", type=bpmn2_ResourceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression821: BinaryAssociation = BinaryAssociation(
    name="expression821",
    ends={
        Property(name="bpmn2_Expression823", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceAssignmentExpression822", type=bpmn2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceRef851: BinaryAssociation = BinaryAssociation(
    name="sourceRef851",
    ends={
        Property(name="outgoing", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowNode852", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1))
    }
)
targetRef853: BinaryAssociation = BinaryAssociation(
    name="targetRef853",
    ends={
        Property(name="FlowNode854", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=bpmn2_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
operationRef855: BinaryAssociation = BinaryAssociation(
    name="operationRef855",
    ends={
        Property(name="bpmn2_Operation857", type=bpmn2_ServiceTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ServiceTask856", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
structureRef858: BinaryAssociation = BinaryAssociation(
    name="structureRef858",
    ends={
        Property(name="bpmn2_ItemDefinition860", type=bpmn2_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Signal859", type=bpmn2_ItemDefinition, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef833: BinaryAssociation = BinaryAssociation(
    name="resourceRef833",
    ends={
        Property(name="bpmn2_Resource835", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole834", type=bpmn2_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resourceParameterBindings836: BinaryAssociation = BinaryAssociation(
    name="resourceParameterBindings836",
    ends={
        Property(name="bpmn2_ResourceParameterBinding838", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole837", type=bpmn2_ResourceParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceAssignmentExpression839: BinaryAssociation = BinaryAssociation(
    name="resourceAssignmentExpression839",
    ends={
        Property(name="bpmn2_ResourceAssignmentExpression841", type=bpmn2_ResourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ResourceRole840", type=bpmn2_ResourceAssignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageRef842: BinaryAssociation = BinaryAssociation(
    name="messageRef842",
    ends={
        Property(name="bpmn2_Message844", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask843", type=bpmn2_Message, multiplicity=Multiplicity(0, 1))
    }
)
operationRef845: BinaryAssociation = BinaryAssociation(
    name="operationRef845",
    ends={
        Property(name="bpmn2_Operation847", type=bpmn2_SendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SendTask846", type=bpmn2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression848: BinaryAssociation = BinaryAssociation(
    name="conditionExpression848",
    ends={
        Property(name="bpmn2_Expression850", type=bpmn2_SequenceFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SequenceFlow849", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conversationNodes870: BinaryAssociation = BinaryAssociation(
    name="conversationNodes870",
    ends={
        Property(name="bpmn2_ConversationNode872", type=bpmn2_SubConversation, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubConversation871", type=bpmn2_ConversationNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalRef861: BinaryAssociation = BinaryAssociation(
    name="signalRef861",
    ends={
        Property(name="bpmn2_Signal863", type=bpmn2_SignalEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SignalEventDefinition862", type=bpmn2_Signal, multiplicity=Multiplicity(0, 1))
    }
)
loopCondition864: BinaryAssociation = BinaryAssociation(
    name="loopCondition864",
    ends={
        Property(name="bpmn2_Expression866", type=bpmn2_StandardLoopCharacteristics, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_StandardLoopCharacteristics865", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
artifacts867: BinaryAssociation = BinaryAssociation(
    name="artifacts867",
    ends={
        Property(name="bpmn2_Artifact869", type=bpmn2_SubChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubChoreography868", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputAssociation884: BinaryAssociation = BinaryAssociation(
    name="dataInputAssociation884",
    ends={
        Property(name="bpmn2_DataInputAssociation886", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent885", type=bpmn2_DataInputAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet887: BinaryAssociation = BinaryAssociation(
    name="inputSet887",
    ends={
        Property(name="bpmn2_InputSet889", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent888", type=bpmn2_InputSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDefinitions890: BinaryAssociation = BinaryAssociation(
    name="eventDefinitions890",
    ends={
        Property(name="bpmn2_EventDefinition892", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent891", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventDefinitionRefs893: BinaryAssociation = BinaryAssociation(
    name="eventDefinitionRefs893",
    ends={
        Property(name="bpmn2_EventDefinition895", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent894", type=bpmn2_EventDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
artifacts873: BinaryAssociation = BinaryAssociation(
    name="artifacts873",
    ends={
        Property(name="bpmn2_Artifact875", type=bpmn2_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubProcess874", type=bpmn2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedSubProcess876: BinaryAssociation = BinaryAssociation(
    name="referencedSubProcess876",
    ends={
        Property(name="bpmn2_Process878", type=bpmn2_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_SubProcess877", type=bpmn2_Process, multiplicity=Multiplicity(0, 9999))
    }
)
documentsAndResources879: BinaryAssociation = BinaryAssociation(
    name="documentsAndResources879",
    ends={
        Property(name="bpmn2_Document", type=bpmn2_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_Task880", type=bpmn2_Document, multiplicity=Multiplicity(0, 9999))
    }
)
dataInputs881: BinaryAssociation = BinaryAssociation(
    name="dataInputs881",
    ends={
        Property(name="bpmn2_DataInput883", type=bpmn2_ThrowEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_ThrowEvent882", type=bpmn2_DataInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeDate896: BinaryAssociation = BinaryAssociation(
    name="timeDate896",
    ends={
        Property(name="bpmn2_Expression898", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition897", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeDuration899: BinaryAssociation = BinaryAssociation(
    name="timeDuration899",
    ends={
        Property(name="bpmn2_Expression901", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition900", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCycle902: BinaryAssociation = BinaryAssociation(
    name="timeCycle902",
    ends={
        Property(name="bpmn2_Expression904", type=bpmn2_TimerEventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_TimerEventDefinition903", type=bpmn2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
renderings905: BinaryAssociation = BinaryAssociation(
    name="renderings905",
    ends={
        Property(name="bpmn2_Rendering907", type=bpmn2_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmn2_UserTask906", type=bpmn2_Rendering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bpmn2_Activity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Activity)
gen_bpmn2_AdHocSubProcess_SubProcess = Generalization(general=SubProcess, specific=bpmn2_AdHocSubProcess)
gen_bpmn2_BoundaryEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_BoundaryEvent)
gen_bpmn2_BusinessRuleTask_Task = Generalization(general=Task, specific=bpmn2_BusinessRuleTask)
gen_bpmn2_CallActivity_Activity = Generalization(general=Activity, specific=bpmn2_CallActivity)
gen_bpmn2_Artifact_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Artifact)
gen_bpmn2_Assignment_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Assignment)
gen_bpmn2_Association_Artifact = Generalization(general=Artifact, specific=bpmn2_Association)
gen_bpmn2_Auditing_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Auditing)
gen_bpmn2_Category_RootElement = Generalization(general=RootElement, specific=bpmn2_Category)
gen_bpmn2_CallChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_CallChoreography)
gen_bpmn2_CallConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_CallConversation)
gen_bpmn2_CallableElement_RootElement = Generalization(general=RootElement, specific=bpmn2_CallableElement)
gen_bpmn2_CancelEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CancelEventDefinition)
gen_bpmn2_CatchEvent_Event = Generalization(general=Event, specific=bpmn2_CatchEvent)
gen_bpmn2_CategoryValue_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CategoryValue)
gen_bpmn2_Choreography_Collaboration = Generalization(general=Collaboration, specific=bpmn2_Choreography)
gen_bpmn2_Choreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Choreography)
gen_bpmn2_ChoreographyActivity_FlowNode = Generalization(general=FlowNode, specific=bpmn2_ChoreographyActivity)
gen_bpmn2_ChoreographyTask_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_ChoreographyTask)
gen_bpmn2_Collaboration_RootElement = Generalization(general=RootElement, specific=bpmn2_Collaboration)
gen_bpmn2_ConditionalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ConditionalEventDefinition)
gen_bpmn2_Conversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_Conversation)
gen_bpmn2_ConversationAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationAssociation)
gen_bpmn2_ConversationLink_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationLink)
gen_bpmn2_CompensateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_CompensateEventDefinition)
gen_bpmn2_ComplexBehaviorDefinition_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ComplexBehaviorDefinition)
gen_bpmn2_ComplexGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ComplexGateway)
gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyRetrievalExpression)
gen_bpmn2_CorrelationSubscription_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationSubscription)
gen_bpmn2_ConversationNode_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ConversationNode)
gen_bpmn2_ConversationNode_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_ConversationNode)
gen_bpmn2_CorrelationKey_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationKey)
gen_bpmn2_CorrelationProperty_RootElement = Generalization(general=RootElement, specific=bpmn2_CorrelationProperty)
gen_bpmn2_CorrelationPropertyBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_CorrelationPropertyBinding)
gen_bpmn2_DataObject_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObject)
gen_bpmn2_DataObject_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObject)
gen_bpmn2_DataObjectReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_DataObjectReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataObjectReference)
gen_bpmn2_DataOutput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataOutput)
gen_bpmn2_DataAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataAssociation)
gen_bpmn2_DataInput_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataInput)
gen_bpmn2_DataInputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataInputAssociation)
gen_bpmn2_Documentation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Documentation)
gen_bpmn2_DataOutputAssociation_DataAssociation = Generalization(general=DataAssociation, specific=bpmn2_DataOutputAssociation)
gen_bpmn2_DataState_BaseElement = Generalization(general=BaseElement, specific=bpmn2_DataState)
gen_bpmn2_DataStore_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStore)
gen_bpmn2_DataStore_RootElement = Generalization(general=RootElement, specific=bpmn2_DataStore)
gen_bpmn2_DataStoreReference_FlowElement = Generalization(general=FlowElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_DataStoreReference_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_DataStoreReference)
gen_bpmn2_Definitions_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Definitions)
gen_bpmn2_EventDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_EventDefinition)
gen_bpmn2_ExclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ExclusiveGateway)
gen_bpmn2_Expression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Expression)
gen_bpmn2_EndEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_EndEvent)
gen_bpmn2_EndPoint_RootElement = Generalization(general=RootElement, specific=bpmn2_EndPoint)
gen_bpmn2_Error_RootElement = Generalization(general=RootElement, specific=bpmn2_Error)
gen_bpmn2_ErrorEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_ErrorEventDefinition)
gen_bpmn2_Escalation_RootElement = Generalization(general=RootElement, specific=bpmn2_Escalation)
gen_bpmn2_EscalationEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_EscalationEventDefinition)
gen_bpmn2_Event_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Event)
gen_bpmn2_Event_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Event)
gen_bpmn2_EventBasedGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_EventBasedGateway)
gen_bpmn2_FlowElementsContainer_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElementsContainer)
gen_bpmn2_FlowNode_FlowElement = Generalization(general=FlowElement, specific=bpmn2_FlowNode)
gen_bpmn2_FlowElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_FlowElement)
gen_bpmn2_GlobalConversation_Collaboration = Generalization(general=Collaboration, specific=bpmn2_GlobalConversation)
gen_bpmn2_GlobalManualTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalManualTask)
gen_bpmn2_GlobalScriptTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalScriptTask)
gen_bpmn2_GlobalTask_CallableElement = Generalization(general=CallableElement, specific=bpmn2_GlobalTask)
gen_bpmn2_GlobalUserTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalUserTask)
gen_bpmn2_FormalExpression_Expression = Generalization(general=Expression, specific=bpmn2_FormalExpression)
gen_bpmn2_Gateway_FlowNode = Generalization(general=FlowNode, specific=bpmn2_Gateway)
gen_bpmn2_GlobalBusinessRuleTask_GlobalTask = Generalization(general=GlobalTask, specific=bpmn2_GlobalBusinessRuleTask)
gen_bpmn2_GlobalChoreographyTask_Choreography = Generalization(general=Choreography, specific=bpmn2_GlobalChoreographyTask)
gen_bpmn2_Group_Artifact = Generalization(general=Artifact, specific=bpmn2_Group)
gen_bpmn2_HumanPerformer_Performer = Generalization(general=Performer, specific=bpmn2_HumanPerformer)
gen_bpmn2_ImplicitThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_ImplicitThrowEvent)
gen_bpmn2_InclusiveGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_InclusiveGateway)
gen_bpmn2_InputOutputBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputOutputBinding)
gen_bpmn2_InputOutputSpecification_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputOutputSpecification)
gen_bpmn2_Interface_RootElement = Generalization(general=RootElement, specific=bpmn2_Interface)
gen_bpmn2_InputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_InputSet)
gen_bpmn2_IntermediateCatchEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_IntermediateCatchEvent)
gen_bpmn2_IntermediateThrowEvent_ThrowEvent = Generalization(general=ThrowEvent, specific=bpmn2_IntermediateThrowEvent)
gen_bpmn2_ItemAwareElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ItemAwareElement)
gen_bpmn2_ItemDefinition_RootElement = Generalization(general=RootElement, specific=bpmn2_ItemDefinition)
gen_bpmn2_Lane_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Lane)
gen_bpmn2_Lane_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Lane)
gen_bpmn2_LoopCharacteristics_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LoopCharacteristics)
gen_bpmn2_ManualTask_Task = Generalization(general=Task, specific=bpmn2_ManualTask)
gen_bpmn2_Message_RootElement = Generalization(general=RootElement, specific=bpmn2_Message)
gen_bpmn2_LaneSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_LaneSet)
gen_bpmn2_LaneSet_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_LaneSet)
gen_bpmn2_LinkEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_LinkEventDefinition)
gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_MultiInstanceLoopCharacteristics)
gen_bpmn2_MessageEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_MessageEventDefinition)
gen_bpmn2_MessageFlow_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlow)
gen_bpmn2_MessageFlowAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_MessageFlowAssociation)
gen_bpmn2_Monitoring_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Monitoring)
gen_bpmn2_OutputSet_BaseElement = Generalization(general=BaseElement, specific=bpmn2_OutputSet)
gen_bpmn2_Operation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Operation)
gen_bpmn2_ParticipantMultiplicity_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ParticipantMultiplicity)
gen_bpmn2_PartnerEntity_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerEntity)
gen_bpmn2_ParallelGateway_Gateway = Generalization(general=Gateway, specific=bpmn2_ParallelGateway)
gen_bpmn2_Participant_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Participant)
gen_bpmn2_Participant_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Participant)
gen_bpmn2_ParticipantAssociation_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ParticipantAssociation)
gen_bpmn2_Property_ItemAwareElement = Generalization(general=ItemAwareElement, specific=bpmn2_Property)
gen_bpmn2_ReceiveTask_Task = Generalization(general=Task, specific=bpmn2_ReceiveTask)
gen_bpmn2_PartnerRole_RootElement = Generalization(general=RootElement, specific=bpmn2_PartnerRole)
gen_bpmn2_Performer_ResourceRole = Generalization(general=ResourceRole, specific=bpmn2_Performer)
gen_bpmn2_PotentialOwner_HumanPerformer = Generalization(general=HumanPerformer, specific=bpmn2_PotentialOwner)
gen_bpmn2_Process_CallableElement = Generalization(general=CallableElement, specific=bpmn2_Process)
gen_bpmn2_Process_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_Process)
gen_bpmn2_ResourceParameter_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceParameter)
gen_bpmn2_ResourceParameterBinding_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceParameterBinding)
gen_bpmn2_ResourceRole_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceRole)
gen_bpmn2_Relationship_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Relationship)
gen_bpmn2_Rendering_BaseElement = Generalization(general=BaseElement, specific=bpmn2_Rendering)
gen_bpmn2_Resource_RootElement = Generalization(general=RootElement, specific=bpmn2_Resource)
gen_bpmn2_ResourceAssignmentExpression_BaseElement = Generalization(general=BaseElement, specific=bpmn2_ResourceAssignmentExpression)
gen_bpmn2_ServiceTask_Task = Generalization(general=Task, specific=bpmn2_ServiceTask)
gen_bpmn2_Signal_RootElement = Generalization(general=RootElement, specific=bpmn2_Signal)
gen_bpmn2_RootElement_BaseElement = Generalization(general=BaseElement, specific=bpmn2_RootElement)
gen_bpmn2_ScriptTask_Task = Generalization(general=Task, specific=bpmn2_ScriptTask)
gen_bpmn2_SendTask_Task = Generalization(general=Task, specific=bpmn2_SendTask)
gen_bpmn2_SequenceFlow_FlowElement = Generalization(general=FlowElement, specific=bpmn2_SequenceFlow)
gen_bpmn2_SignalEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_SignalEventDefinition)
gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics = Generalization(general=LoopCharacteristics, specific=bpmn2_StandardLoopCharacteristics)
gen_bpmn2_StartEvent_CatchEvent = Generalization(general=CatchEvent, specific=bpmn2_StartEvent)
gen_bpmn2_SubChoreography_ChoreographyActivity = Generalization(general=ChoreographyActivity, specific=bpmn2_SubChoreography)
gen_bpmn2_SubChoreography_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubChoreography)
gen_bpmn2_SubConversation_ConversationNode = Generalization(general=ConversationNode, specific=bpmn2_SubConversation)
gen_bpmn2_SubProcess_Activity = Generalization(general=Activity, specific=bpmn2_SubProcess)
gen_bpmn2_SubProcess_FlowElementsContainer = Generalization(general=FlowElementsContainer, specific=bpmn2_SubProcess)
gen_bpmn2_Task_Activity = Generalization(general=Activity, specific=bpmn2_Task)
gen_bpmn2_Task_InteractionNode = Generalization(general=InteractionNode, specific=bpmn2_Task)
gen_bpmn2_TerminateEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TerminateEventDefinition)
gen_bpmn2_TextAnnotation_Artifact = Generalization(general=Artifact, specific=bpmn2_TextAnnotation)
gen_bpmn2_ThrowEvent_Event = Generalization(general=Event, specific=bpmn2_ThrowEvent)
gen_bpmn2_TimerEventDefinition_EventDefinition = Generalization(general=EventDefinition, specific=bpmn2_TimerEventDefinition)
gen_bpmn2_Transaction_SubProcess = Generalization(general=SubProcess, specific=bpmn2_Transaction)
gen_bpmn2_UserTask_Task = Generalization(general=Task, specific=bpmn2_UserTask)

# Domain Model
domain_model = DomainModel(
    name="bpmn2",
    types={bpmn2_DocumentRoot, bpmn2_EStringToStringMapEntry, bpmn2_CallableElement, bpmn2_AdHocSubProcess, bpmn2_FlowElement, bpmn2_CallActivity, bpmn2_Artifact, bpmn2_Assignment, bpmn2_CallChoreography, bpmn2_Association, bpmn2_Auditing, bpmn2_BaseElement, bpmn2_BoundaryEvent, bpmn2_BusinessRuleTask, bpmn2_Activity, bpmn2_CatchEvent, bpmn2_Category, bpmn2_CategoryValue, bpmn2_CallConversation, bpmn2_ConversationNode, bpmn2_CancelEventDefinition, bpmn2_EventDefinition, bpmn2_RootElement, bpmn2_ComplexBehaviorDefinition, bpmn2_ComplexGateway, bpmn2_Choreography, bpmn2_Collaboration, bpmn2_ChoreographyActivity, bpmn2_ChoreographyTask, bpmn2_CompensateEventDefinition, bpmn2_CorrelationProperty, bpmn2_CorrelationPropertyBinding, bpmn2_CorrelationPropertyRetrievalExpression, bpmn2_ConditionalEventDefinition, bpmn2_Conversation, bpmn2_ConversationAssociation, bpmn2_ConversationLink, bpmn2_CorrelationKey, bpmn2_DataObject, bpmn2_DataObjectReference, bpmn2_CorrelationSubscription, bpmn2_DataAssociation, bpmn2_DataInput, bpmn2_DataInputAssociation, bpmn2_DataStore, bpmn2_DataStoreReference, bpmn2_DataOutput, bpmn2_DataOutputAssociation, bpmn2_DataState, bpmn2_ErrorEventDefinition, bpmn2_Escalation, bpmn2_Definitions, bpmn2_Documentation, bpmn2_EndEvent, bpmn2_EndPoint, bpmn2_Error, bpmn2_Expression, bpmn2_Extension, bpmn2_ExtensionAttributeValue, bpmn2_EscalationEventDefinition, bpmn2_Event, bpmn2_EventBasedGateway, bpmn2_ExclusiveGateway, bpmn2_GlobalChoreographyTask, bpmn2_GlobalConversation, bpmn2_FlowNode, bpmn2_FormalExpression, bpmn2_Gateway, bpmn2_GlobalBusinessRuleTask, bpmn2_GlobalUserTask, bpmn2_Group, bpmn2_GlobalManualTask, bpmn2_GlobalScriptTask, bpmn2_GlobalTask, bpmn2_ImplicitThrowEvent, bpmn2_Import, bpmn2_HumanPerformer, bpmn2_Performer, bpmn2_ResourceRole, bpmn2_IntermediateCatchEvent, bpmn2_IntermediateThrowEvent, bpmn2_InclusiveGateway, bpmn2_InputSet, bpmn2_Interface, bpmn2_Lane, bpmn2_LaneSet, bpmn2_InputOutputBinding, bpmn2_InputOutputSpecification, bpmn2_ItemDefinition, bpmn2_Message, bpmn2_LinkEventDefinition, bpmn2_LoopCharacteristics, bpmn2_ManualTask, bpmn2_Monitoring, bpmn2_MultiInstanceLoopCharacteristics, bpmn2_MessageEventDefinition, bpmn2_MessageFlow, bpmn2_MessageFlowAssociation, bpmn2_Participant, bpmn2_ParticipantAssociation, bpmn2_Operation, bpmn2_OutputSet, bpmn2_ParallelGateway, bpmn2_Property, bpmn2_ReceiveTask, bpmn2_ParticipantMultiplicity, bpmn2_PartnerEntity, bpmn2_PartnerRole, bpmn2_PotentialOwner, bpmn2_Process, bpmn2_ResourceAssignmentExpression, bpmn2_Relationship, bpmn2_Rendering, bpmn2_Resource, bpmn2_ScriptTask, bpmn2_SendTask, bpmn2_ResourceParameter, bpmn2_ResourceParameterBinding, bpmn2_EObject, bpmn2_SignalEventDefinition, bpmn2_SequenceFlow, bpmn2_ServiceTask, bpmn2_Signal, bpmn2_SubConversation, bpmn2_SubProcess, bpmn2_StandardLoopCharacteristics, bpmn2_StartEvent, bpmn2_SubChoreography, bpmn2_TextAnnotation, bpmn2_Task, bpmn2_TerminateEventDefinition, bpmn2_ThrowEvent, bpmn2_TimerEventDefinition, bpmn2_Transaction, bpmn2_UserTask, FlowNode, SubProcess, bpmn2_Competency, bpmn2_Criterion, bpmn2_OrganisationalUnit, bpmn2_Position, bpmn2_Role, CatchEvent, Task, Activity, BaseElement, Artifact, bpmn2_ExtensionDefinition, ChoreographyActivity, ConversationNode, RootElement, EventDefinition, Event, Collaboration, FlowElementsContainer, Gateway, bpmn2_InteractionNode, InteractionNode, FlowElement, bpmn2_ItemAwareElement, ItemAwareElement, bpmn2_Document, DataAssociation, bpmn2_BPMNDiagram, ThrowEvent, bpmn2_FlowElementsContainer, bpmn2_ExtensionAttributeDefinition, CallableElement, Expression, GlobalTask, Choreography, Performer, LoopCharacteristics, ResourceRole, HumanPerformer, AdHocOrdering, AssociationDirection, ChoreographyLoopType, EventBasedGatewayType, GatewayDirection, ItemKind, MultiInstanceBehavior, ProcessType, RelationshipDirection},
    associations={callableElement27, adHocSubProcess6, flowElement8, callActivity29, artifact10, assignment12, callChoreography31, association14, auditing16, baseElement18, baseElementWithMixedContent20, boundaryEvent23, xMLNSPrefixMap0, xSISchemaLocation1, businessRuleTask25, activity4, catchEvent43, category45, callConversation33, conversationNode35, cancelEventDefinition37, eventDefinition39, rootElement41, compensateEventDefinition57, complexBehaviorDefinition59, complexGateway61, categoryValue47, choreography49, collaboration51, choreographyActivity53, choreographyTask55, correlationProperty73, correlationPropertyBinding75, conditionalEventDefinition63, conversation65, conversationAssociation67, conversationLink69, correlationKey71, dataObject87, dataObjectReference89, correlationPropertyRetrievalExpression77, correlationSubscription79, dataAssociation81, dataInput83, dataInputAssociation85, dataStore97, dataStoreReference99, dataOutput91, dataOutputAssociation93, dataState95, errorEventDefinition111, escalation113, definitions101, documentation103, endEvent105, endPoint107, error109, expression123, extension125, extensionElements127, escalationEventDefinition115, event117, eventBasedGateway119, exclusiveGateway121, globalChoreographyTask137, globalConversation139, flowNode129, formalExpression131, gateway133, globalBusinessRuleTask135, globalUserTask147, group149, globalManualTask141, globalScriptTask143, globalTask145, implicitThrowEvent157, import_159, humanPerformer151, performer153, resourceRole155, intermediateCatchEvent167, intermediateThrowEvent169, inclusiveGateway161, inputSet163, interface165, lane177, ioBinding171, ioSpecification173, itemDefinition175, message187, laneSet179, linkEventDefinition181, loopCharacteristics183, manualTask185, monitoring195, messageEventDefinition189, messageFlow191, messageFlowAssociation193, participant205, participantAssociation207, multiInstanceLoopCharacteristics197, operation199, outputSet201, parallelGateway203, property219, receiveTask221, participantMultiplicity209, partnerEntity211, partnerRole213, potentialOwner215, process217, resourceAssignmentExpression229, relationship223, rendering225, resource227, scriptTask237, sendTask239, resourceParameter231, resourceParameterBinding233, script235, signalEventDefinition247, sequenceFlow241, serviceTask243, signal245, subConversation255, standardLoopCharacteristics249, startEvent251, subChoreography253, text263, textAnnotation266, subProcess257, task259, terminateEventDefinition261, ioSpecification276, boundaryEventRefs279, properties280, dataInputAssociations283, dataOutputAssociations286, throwEvent268, timerEventDefinition270, transaction272, userTask274, competency314, completionCondition317, resources289, loopCharacteristics292, default295, requiresCompetency298, isMeasuredByCriterion300, isPerformedByOrganisationalUnit302, isResponsibleByOrganisationalUnit304, isPerformedBy307, isPerformedByPosition310, isPerformedByRole312, attachedToRef340, from_320, to323, sourceRef326, targetRef329, extensionValues332, documentation335, extensionDefinitions338, dataOutputAssociation368, outputSet371, eventDefinitions374, eventDefinitionRefs377, categoryValue380, calledElementRef341, participantAssociations344, calledChoreographyRef347, participantAssociations350, calledCollaborationRef353, supportedInterfaceRefs356, ioSpecification359, ioBinding362, dataOutputs365, participants398, messageFlows401, artifacts404, conversations407, conversationAssociations410, categorizedFlowElements383, participantRefs386, correlationKeys389, initiatingParticipantRef392, messageFlowRef395, default440, condition443, innerConversationNodeRef446, outerConversationNodeRef449, participantAssociations413, messageFlowAssociations416, correlationKeys419, choreographyRef422, conversationLinks425, activityRef428, condition431, event434, activationCondition437, correlationPropertyRef478, messagePath481, messageRef484, correlationPropertyBinding487, sourceRef452, targetRef454, participantRefs457, messageFlowRefs460, correlationKeys463, correlationPropertyRef466, correlationPropertyRetrievalExpression469, type472, dataPath475, dataObjectRef510, outputSetWithOptional513, correlationKeyRef490, sourceRef493, targetRef495, transformation498, assignment501, inputSetWithOptional504, inputSetWithWhileExecuting505, inputSetRefs507, referencesDocument509, diagrams532, relationships534, outputSetWithWhileExecuting514, outputSetRefs516, referencesDocument518, dataStoreRef520, imports523, extensions526, rootElements529, default552, definition555, structureRef537, errorRef540, structureRef543, escalationRef546, properties549, categoryValueRef571, laneSets574, flowElements576, extensionDefinition558, valueRef559, extensionAttributeDefinition562, extensionAttributeDefinitions564, auditing565, monitoring568, initiatingParticipantRef586, resources589, incoming579, lanes580, outgoing581, evaluatesToTypeRef583, dataInputs610, dataOutputs613, inputSets616, outputSets619, renderings592, categoryValueRef595, default598, inputDataRef601, operationRef604, outputDataRef607, outgoingConversationLinks633, operations636, implementationRef639, dataInputRefs622, optionalInputRefs623, whileExecutingInputRefs625, outputSetRefs627, incomingConversationLinks630, flowNodeRefs657, childLaneSet658, partitionElementRef661, representsPerformer664, representsRole667, dataState642, itemSubjectRef645, import_648, structureRef651, partitionElement654, source683, target685, itemRef687, representsOrganisationalUnit670, messages673, lanes676, representsOrganisationalUnit679, loopCardinality711, loopDataInputRef714, loopDataOutputRef717, inputDataItem720, operationRef690, messageRef693, messageRef696, sourceRef699, targetRef702, innerMessageFlowRef705, outerMessageFlowRef708, outMessageRef741, errorRefs744, implementationRef747, dataOutputRefs750, outputDataItem723, complexBehaviorDefinition726, completionCondition729, noneBehaviorEventRef732, oneBehaviorEventRef735, inMessageRef738, outerParticipantRef773, participantRef776, optionalOutputRefs751, whileExecutingOutputRefs753, inputSetRefs755, interfaceRefs758, endPointRefs761, participantMultiplicity764, processRef767, innerParticipantRef770, participantRef779, auditing782, monitoring785, properties788, artifacts791, resources794, correlationSubscriptions797, supports801, definitionalCollaborationRef803, type824, expression827, parameterRef830, messageRef806, operationRef809, sources812, targets815, resourceParameters818, expression821, sourceRef851, targetRef853, operationRef855, structureRef858, resourceRef833, resourceParameterBindings836, resourceAssignmentExpression839, messageRef842, operationRef845, conditionExpression848, conversationNodes870, signalRef861, loopCondition864, artifacts867, dataInputAssociation884, inputSet887, eventDefinitions890, eventDefinitionRefs893, artifacts873, referencedSubProcess876, documentsAndResources879, dataInputs881, timeDate896, timeDuration899, timeCycle902, renderings905},
    generalizations={gen_bpmn2_Activity_FlowNode, gen_bpmn2_AdHocSubProcess_SubProcess, gen_bpmn2_BoundaryEvent_CatchEvent, gen_bpmn2_BusinessRuleTask_Task, gen_bpmn2_CallActivity_Activity, gen_bpmn2_Artifact_BaseElement, gen_bpmn2_Assignment_BaseElement, gen_bpmn2_Association_Artifact, gen_bpmn2_Auditing_BaseElement, gen_bpmn2_Category_RootElement, gen_bpmn2_CallChoreography_ChoreographyActivity, gen_bpmn2_CallConversation_ConversationNode, gen_bpmn2_CallableElement_RootElement, gen_bpmn2_CancelEventDefinition_EventDefinition, gen_bpmn2_CatchEvent_Event, gen_bpmn2_CategoryValue_BaseElement, gen_bpmn2_Choreography_Collaboration, gen_bpmn2_Choreography_FlowElementsContainer, gen_bpmn2_ChoreographyActivity_FlowNode, gen_bpmn2_ChoreographyTask_ChoreographyActivity, gen_bpmn2_Collaboration_RootElement, gen_bpmn2_ConditionalEventDefinition_EventDefinition, gen_bpmn2_Conversation_ConversationNode, gen_bpmn2_ConversationAssociation_BaseElement, gen_bpmn2_ConversationLink_BaseElement, gen_bpmn2_CompensateEventDefinition_EventDefinition, gen_bpmn2_ComplexBehaviorDefinition_BaseElement, gen_bpmn2_ComplexGateway_Gateway, gen_bpmn2_CorrelationPropertyRetrievalExpression_BaseElement, gen_bpmn2_CorrelationSubscription_BaseElement, gen_bpmn2_ConversationNode_BaseElement, gen_bpmn2_ConversationNode_InteractionNode, gen_bpmn2_CorrelationKey_BaseElement, gen_bpmn2_CorrelationProperty_RootElement, gen_bpmn2_CorrelationPropertyBinding_BaseElement, gen_bpmn2_DataObject_FlowElement, gen_bpmn2_DataObject_ItemAwareElement, gen_bpmn2_DataObjectReference_FlowElement, gen_bpmn2_DataObjectReference_ItemAwareElement, gen_bpmn2_DataOutput_ItemAwareElement, gen_bpmn2_DataAssociation_BaseElement, gen_bpmn2_DataInput_ItemAwareElement, gen_bpmn2_DataInputAssociation_DataAssociation, gen_bpmn2_Documentation_BaseElement, gen_bpmn2_DataOutputAssociation_DataAssociation, gen_bpmn2_DataState_BaseElement, gen_bpmn2_DataStore_ItemAwareElement, gen_bpmn2_DataStore_RootElement, gen_bpmn2_DataStoreReference_FlowElement, gen_bpmn2_DataStoreReference_ItemAwareElement, gen_bpmn2_Definitions_BaseElement, gen_bpmn2_EventDefinition_RootElement, gen_bpmn2_ExclusiveGateway_Gateway, gen_bpmn2_Expression_BaseElement, gen_bpmn2_EndEvent_ThrowEvent, gen_bpmn2_EndPoint_RootElement, gen_bpmn2_Error_RootElement, gen_bpmn2_ErrorEventDefinition_EventDefinition, gen_bpmn2_Escalation_RootElement, gen_bpmn2_EscalationEventDefinition_EventDefinition, gen_bpmn2_Event_FlowNode, gen_bpmn2_Event_InteractionNode, gen_bpmn2_EventBasedGateway_Gateway, gen_bpmn2_FlowElementsContainer_BaseElement, gen_bpmn2_FlowNode_FlowElement, gen_bpmn2_FlowElement_BaseElement, gen_bpmn2_GlobalConversation_Collaboration, gen_bpmn2_GlobalManualTask_GlobalTask, gen_bpmn2_GlobalScriptTask_GlobalTask, gen_bpmn2_GlobalTask_CallableElement, gen_bpmn2_GlobalUserTask_GlobalTask, gen_bpmn2_FormalExpression_Expression, gen_bpmn2_Gateway_FlowNode, gen_bpmn2_GlobalBusinessRuleTask_GlobalTask, gen_bpmn2_GlobalChoreographyTask_Choreography, gen_bpmn2_Group_Artifact, gen_bpmn2_HumanPerformer_Performer, gen_bpmn2_ImplicitThrowEvent_ThrowEvent, gen_bpmn2_InclusiveGateway_Gateway, gen_bpmn2_InputOutputBinding_BaseElement, gen_bpmn2_InputOutputSpecification_BaseElement, gen_bpmn2_Interface_RootElement, gen_bpmn2_InputSet_BaseElement, gen_bpmn2_IntermediateCatchEvent_CatchEvent, gen_bpmn2_IntermediateThrowEvent_ThrowEvent, gen_bpmn2_ItemAwareElement_BaseElement, gen_bpmn2_ItemDefinition_RootElement, gen_bpmn2_Lane_BaseElement, gen_bpmn2_Lane_InteractionNode, gen_bpmn2_LoopCharacteristics_BaseElement, gen_bpmn2_ManualTask_Task, gen_bpmn2_Message_RootElement, gen_bpmn2_LaneSet_BaseElement, gen_bpmn2_LaneSet_InteractionNode, gen_bpmn2_LinkEventDefinition_EventDefinition, gen_bpmn2_MultiInstanceLoopCharacteristics_LoopCharacteristics, gen_bpmn2_MessageEventDefinition_EventDefinition, gen_bpmn2_MessageFlow_BaseElement, gen_bpmn2_MessageFlowAssociation_BaseElement, gen_bpmn2_Monitoring_BaseElement, gen_bpmn2_OutputSet_BaseElement, gen_bpmn2_Operation_BaseElement, gen_bpmn2_ParticipantMultiplicity_BaseElement, gen_bpmn2_PartnerEntity_RootElement, gen_bpmn2_ParallelGateway_Gateway, gen_bpmn2_Participant_BaseElement, gen_bpmn2_Participant_InteractionNode, gen_bpmn2_ParticipantAssociation_BaseElement, gen_bpmn2_Property_ItemAwareElement, gen_bpmn2_ReceiveTask_Task, gen_bpmn2_PartnerRole_RootElement, gen_bpmn2_Performer_ResourceRole, gen_bpmn2_PotentialOwner_HumanPerformer, gen_bpmn2_Process_CallableElement, gen_bpmn2_Process_FlowElementsContainer, gen_bpmn2_ResourceParameter_BaseElement, gen_bpmn2_ResourceParameterBinding_BaseElement, gen_bpmn2_ResourceRole_BaseElement, gen_bpmn2_Relationship_BaseElement, gen_bpmn2_Rendering_BaseElement, gen_bpmn2_Resource_RootElement, gen_bpmn2_ResourceAssignmentExpression_BaseElement, gen_bpmn2_ServiceTask_Task, gen_bpmn2_Signal_RootElement, gen_bpmn2_RootElement_BaseElement, gen_bpmn2_ScriptTask_Task, gen_bpmn2_SendTask_Task, gen_bpmn2_SequenceFlow_FlowElement, gen_bpmn2_SignalEventDefinition_EventDefinition, gen_bpmn2_StandardLoopCharacteristics_LoopCharacteristics, gen_bpmn2_StartEvent_CatchEvent, gen_bpmn2_SubChoreography_ChoreographyActivity, gen_bpmn2_SubChoreography_FlowElementsContainer, gen_bpmn2_SubConversation_ConversationNode, gen_bpmn2_SubProcess_Activity, gen_bpmn2_SubProcess_FlowElementsContainer, gen_bpmn2_Task_Activity, gen_bpmn2_Task_InteractionNode, gen_bpmn2_TerminateEventDefinition_EventDefinition, gen_bpmn2_TextAnnotation_Artifact, gen_bpmn2_ThrowEvent_Event, gen_bpmn2_TimerEventDefinition_EventDefinition, gen_bpmn2_Transaction_SubProcess, gen_bpmn2_UserTask_Task},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)