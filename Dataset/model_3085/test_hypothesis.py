import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relationship,
    Property,
    Process,
    PotentialOwner,
    PartnerRole,
    PartnerEntity,
    ParticipantMultiplicity,
    ParticipantAssociation,
    Participant,
    gateways_ParallelGateway,
    OutputSet,
    Operation,
    MultiInstanceLoopCharacteristics,
    Monitoring,
    MessageFlowAssociation,
    MessageFlow,
    MessageEventDefinition,
    Message,
    ItemDefinition,
    ManualTask,
    LoopCharacteristics,
    events_LinkEventDefinition,
    LaneSet,
    Lane,
    InputSet,
    InputOutputSpecification,
    InputOutputBinding,
    events_IntermediateThrowEvent,
    events_IntermediateCatchEvent,
    Interface,
    gateways_InclusiveGateway,
    Import,
    events_ImplicitThrowEvent,
    ResourceRole,
    Performer,
    HumanPerformer,
    artifacts_Group,
    GlobalUserTask,
    GlobalTask,
    GlobalScriptTask,
    GlobalManualTask,
    GlobalConversation,
    GlobalChoreographyTask,
    GlobalBusinessRuleTask,
    gateways_Gateway,
    FormalExpression,
    gateways_EventBasedGateway,
    flows_FlowNode,
    extension_ExtensionAttributeValue,
    extension_Extension,
    Expression,
    gateways_ExclusiveGateway,
    EndPoint,
    events_Event,
    events_EscalationEventDefinition,
    Escalation,
    events_ErrorEventDefinition,
    Error,
    events_EndEvent,
    Documentation,
    Definitions,
    DataStoreReference,
    DataStore,
    DataState,
    DataAssociation,
    DataOutputAssociation,
    DataOutput,
    DataObjectReference,
    DataObject,
    DataInputAssociation,
    DataInput,
    ConversationAssociation,
    correlations_CorrelationSubscription,
    correlations_CorrelationPropertyRetrievalExpression,
    correlations_CorrelationPropertyBinding,
    correlations_CorrelationProperty,
    correlations_CorrelationKey,
    ConversationLink,
    choreographyactivities_ChoreographyActivity,
    Conversation,
    events_ConditionalEventDefinition,
    gateways_ComplexGateway,
    ComplexBehaviorDefinition,
    events_CompensateEventDefinition,
    choreographyactivities_ChoreographyTask,
    events_EventDefinition,
    Collaboration,
    Choreography,
    artifacts_CategoryValue,
    artifacts_Category,
    events_CatchEvent,
    RootElement,
    events_CancelEventDefinition,
    ConversationNode,
    CallConversation,
    choreographyactivities_CallChoreography,
    CallActivity,
    CallableElement,
    Assignment,
    BusinessRuleTask,
    events_BoundaryEvent,
    BaseElement,
    Auditing,
    artifacts_Association,
    bpmn2_EStringToStringMapEntry,
    artifacts_Artifact,
    flows_FlowElement,
    AdHocSubProcess,
    Activity,
    bpmn2_DocumentRoot,
    UserTask,
    Transaction,
    events_TimerEventDefinition,
    events_ThrowEvent,
    artifacts_TextAnnotation,
    events_TerminateEventDefinition,
    events_StartEvent,
    Task,
    SubProcess,
    SubConversation,
    choreographyactivities_SubChoreography,
    StandardLoopCharacteristics,
    events_SignalEventDefinition,
    events_Signal,
    ServiceTask,
    ResourceParameter,
    flows_SequenceFlow,
    SendTask,
    ScriptTask,
    bpmn2_EObject,
    ResourceParameterBinding,
    ReceiveTask,
    ResourceAssignmentExpression,
    Resource,
    Rendering,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_potentialowner_is_not_abstract():
    assert not inspect.isabstract(PotentialOwner)


def test_potentialowner_constructor_exists():
    assert callable(PotentialOwner.__init__)


def test_potentialowner_constructor_args():
    sig = inspect.signature(PotentialOwner.__init__)
    params = list(sig.parameters.keys())



def test_partnerrole_is_not_abstract():
    assert not inspect.isabstract(PartnerRole)


def test_partnerrole_constructor_exists():
    assert callable(PartnerRole.__init__)


def test_partnerrole_constructor_args():
    sig = inspect.signature(PartnerRole.__init__)
    params = list(sig.parameters.keys())



def test_partnerentity_is_not_abstract():
    assert not inspect.isabstract(PartnerEntity)


def test_partnerentity_constructor_exists():
    assert callable(PartnerEntity.__init__)


def test_partnerentity_constructor_args():
    sig = inspect.signature(PartnerEntity.__init__)
    params = list(sig.parameters.keys())



def test_participantmultiplicity_is_not_abstract():
    assert not inspect.isabstract(ParticipantMultiplicity)


def test_participantmultiplicity_constructor_exists():
    assert callable(ParticipantMultiplicity.__init__)


def test_participantmultiplicity_constructor_args():
    sig = inspect.signature(ParticipantMultiplicity.__init__)
    params = list(sig.parameters.keys())



def test_participantassociation_is_not_abstract():
    assert not inspect.isabstract(ParticipantAssociation)


def test_participantassociation_constructor_exists():
    assert callable(ParticipantAssociation.__init__)


def test_participantassociation_constructor_args():
    sig = inspect.signature(ParticipantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_participant_is_not_abstract():
    assert not inspect.isabstract(Participant)


def test_participant_constructor_exists():
    assert callable(Participant.__init__)


def test_participant_constructor_args():
    sig = inspect.signature(Participant.__init__)
    params = list(sig.parameters.keys())



def test_gateways_parallelgateway_is_not_abstract():
    assert not inspect.isabstract(gateways_ParallelGateway)


def test_gateways_parallelgateway_constructor_exists():
    assert callable(gateways_ParallelGateway.__init__)


def test_gateways_parallelgateway_constructor_args():
    sig = inspect.signature(gateways_ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_outputset_is_not_abstract():
    assert not inspect.isabstract(OutputSet)


def test_outputset_constructor_exists():
    assert callable(OutputSet.__init__)


def test_outputset_constructor_args():
    sig = inspect.signature(OutputSet.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_multiinstanceloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(MultiInstanceLoopCharacteristics)


def test_multiinstanceloopcharacteristics_constructor_exists():
    assert callable(MultiInstanceLoopCharacteristics.__init__)


def test_multiinstanceloopcharacteristics_constructor_args():
    sig = inspect.signature(MultiInstanceLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_monitoring_is_not_abstract():
    assert not inspect.isabstract(Monitoring)


def test_monitoring_constructor_exists():
    assert callable(Monitoring.__init__)


def test_monitoring_constructor_args():
    sig = inspect.signature(Monitoring.__init__)
    params = list(sig.parameters.keys())



def test_messageflowassociation_is_not_abstract():
    assert not inspect.isabstract(MessageFlowAssociation)


def test_messageflowassociation_constructor_exists():
    assert callable(MessageFlowAssociation.__init__)


def test_messageflowassociation_constructor_args():
    sig = inspect.signature(MessageFlowAssociation.__init__)
    params = list(sig.parameters.keys())



def test_messageflow_is_not_abstract():
    assert not inspect.isabstract(MessageFlow)


def test_messageflow_constructor_exists():
    assert callable(MessageFlow.__init__)


def test_messageflow_constructor_args():
    sig = inspect.signature(MessageFlow.__init__)
    params = list(sig.parameters.keys())



def test_messageeventdefinition_is_not_abstract():
    assert not inspect.isabstract(MessageEventDefinition)


def test_messageeventdefinition_constructor_exists():
    assert callable(MessageEventDefinition.__init__)


def test_messageeventdefinition_constructor_args():
    sig = inspect.signature(MessageEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_itemdefinition_is_not_abstract():
    assert not inspect.isabstract(ItemDefinition)


def test_itemdefinition_constructor_exists():
    assert callable(ItemDefinition.__init__)


def test_itemdefinition_constructor_args():
    sig = inspect.signature(ItemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_manualtask_is_not_abstract():
    assert not inspect.isabstract(ManualTask)


def test_manualtask_constructor_exists():
    assert callable(ManualTask.__init__)


def test_manualtask_constructor_args():
    sig = inspect.signature(ManualTask.__init__)
    params = list(sig.parameters.keys())



def test_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(LoopCharacteristics)


def test_loopcharacteristics_constructor_exists():
    assert callable(LoopCharacteristics.__init__)


def test_loopcharacteristics_constructor_args():
    sig = inspect.signature(LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_events_linkeventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_LinkEventDefinition)


def test_events_linkeventdefinition_constructor_exists():
    assert callable(events_LinkEventDefinition.__init__)


def test_events_linkeventdefinition_constructor_args():
    sig = inspect.signature(events_LinkEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_laneset_is_not_abstract():
    assert not inspect.isabstract(LaneSet)


def test_laneset_constructor_exists():
    assert callable(LaneSet.__init__)


def test_laneset_constructor_args():
    sig = inspect.signature(LaneSet.__init__)
    params = list(sig.parameters.keys())



def test_lane_is_not_abstract():
    assert not inspect.isabstract(Lane)


def test_lane_constructor_exists():
    assert callable(Lane.__init__)


def test_lane_constructor_args():
    sig = inspect.signature(Lane.__init__)
    params = list(sig.parameters.keys())



def test_inputset_is_not_abstract():
    assert not inspect.isabstract(InputSet)


def test_inputset_constructor_exists():
    assert callable(InputSet.__init__)


def test_inputset_constructor_args():
    sig = inspect.signature(InputSet.__init__)
    params = list(sig.parameters.keys())



def test_inputoutputspecification_is_not_abstract():
    assert not inspect.isabstract(InputOutputSpecification)


def test_inputoutputspecification_constructor_exists():
    assert callable(InputOutputSpecification.__init__)


def test_inputoutputspecification_constructor_args():
    sig = inspect.signature(InputOutputSpecification.__init__)
    params = list(sig.parameters.keys())



def test_inputoutputbinding_is_not_abstract():
    assert not inspect.isabstract(InputOutputBinding)


def test_inputoutputbinding_constructor_exists():
    assert callable(InputOutputBinding.__init__)


def test_inputoutputbinding_constructor_args():
    sig = inspect.signature(InputOutputBinding.__init__)
    params = list(sig.parameters.keys())



def test_events_intermediatethrowevent_is_not_abstract():
    assert not inspect.isabstract(events_IntermediateThrowEvent)


def test_events_intermediatethrowevent_constructor_exists():
    assert callable(events_IntermediateThrowEvent.__init__)


def test_events_intermediatethrowevent_constructor_args():
    sig = inspect.signature(events_IntermediateThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_events_intermediatecatchevent_is_not_abstract():
    assert not inspect.isabstract(events_IntermediateCatchEvent)


def test_events_intermediatecatchevent_constructor_exists():
    assert callable(events_IntermediateCatchEvent.__init__)


def test_events_intermediatecatchevent_constructor_args():
    sig = inspect.signature(events_IntermediateCatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_gateways_inclusivegateway_is_not_abstract():
    assert not inspect.isabstract(gateways_InclusiveGateway)


def test_gateways_inclusivegateway_constructor_exists():
    assert callable(gateways_InclusiveGateway.__init__)


def test_gateways_inclusivegateway_constructor_args():
    sig = inspect.signature(gateways_InclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_events_implicitthrowevent_is_not_abstract():
    assert not inspect.isabstract(events_ImplicitThrowEvent)


def test_events_implicitthrowevent_constructor_exists():
    assert callable(events_ImplicitThrowEvent.__init__)


def test_events_implicitthrowevent_constructor_args():
    sig = inspect.signature(events_ImplicitThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_resourcerole_is_not_abstract():
    assert not inspect.isabstract(ResourceRole)


def test_resourcerole_constructor_exists():
    assert callable(ResourceRole.__init__)


def test_resourcerole_constructor_args():
    sig = inspect.signature(ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_performer_is_not_abstract():
    assert not inspect.isabstract(Performer)


def test_performer_constructor_exists():
    assert callable(Performer.__init__)


def test_performer_constructor_args():
    sig = inspect.signature(Performer.__init__)
    params = list(sig.parameters.keys())



def test_humanperformer_is_not_abstract():
    assert not inspect.isabstract(HumanPerformer)


def test_humanperformer_constructor_exists():
    assert callable(HumanPerformer.__init__)


def test_humanperformer_constructor_args():
    sig = inspect.signature(HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_group_is_not_abstract():
    assert not inspect.isabstract(artifacts_Group)


def test_artifacts_group_constructor_exists():
    assert callable(artifacts_Group.__init__)


def test_artifacts_group_constructor_args():
    sig = inspect.signature(artifacts_Group.__init__)
    params = list(sig.parameters.keys())



def test_globalusertask_is_not_abstract():
    assert not inspect.isabstract(GlobalUserTask)


def test_globalusertask_constructor_exists():
    assert callable(GlobalUserTask.__init__)


def test_globalusertask_constructor_args():
    sig = inspect.signature(GlobalUserTask.__init__)
    params = list(sig.parameters.keys())



def test_globaltask_is_not_abstract():
    assert not inspect.isabstract(GlobalTask)


def test_globaltask_constructor_exists():
    assert callable(GlobalTask.__init__)


def test_globaltask_constructor_args():
    sig = inspect.signature(GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_globalscripttask_is_not_abstract():
    assert not inspect.isabstract(GlobalScriptTask)


def test_globalscripttask_constructor_exists():
    assert callable(GlobalScriptTask.__init__)


def test_globalscripttask_constructor_args():
    sig = inspect.signature(GlobalScriptTask.__init__)
    params = list(sig.parameters.keys())



def test_globalmanualtask_is_not_abstract():
    assert not inspect.isabstract(GlobalManualTask)


def test_globalmanualtask_constructor_exists():
    assert callable(GlobalManualTask.__init__)


def test_globalmanualtask_constructor_args():
    sig = inspect.signature(GlobalManualTask.__init__)
    params = list(sig.parameters.keys())



def test_globalconversation_is_not_abstract():
    assert not inspect.isabstract(GlobalConversation)


def test_globalconversation_constructor_exists():
    assert callable(GlobalConversation.__init__)


def test_globalconversation_constructor_args():
    sig = inspect.signature(GlobalConversation.__init__)
    params = list(sig.parameters.keys())



def test_globalchoreographytask_is_not_abstract():
    assert not inspect.isabstract(GlobalChoreographyTask)


def test_globalchoreographytask_constructor_exists():
    assert callable(GlobalChoreographyTask.__init__)


def test_globalchoreographytask_constructor_args():
    sig = inspect.signature(GlobalChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_globalbusinessruletask_is_not_abstract():
    assert not inspect.isabstract(GlobalBusinessRuleTask)


def test_globalbusinessruletask_constructor_exists():
    assert callable(GlobalBusinessRuleTask.__init__)


def test_globalbusinessruletask_constructor_args():
    sig = inspect.signature(GlobalBusinessRuleTask.__init__)
    params = list(sig.parameters.keys())



def test_gateways_gateway_is_not_abstract():
    assert not inspect.isabstract(gateways_Gateway)


def test_gateways_gateway_constructor_exists():
    assert callable(gateways_Gateway.__init__)


def test_gateways_gateway_constructor_args():
    sig = inspect.signature(gateways_Gateway.__init__)
    params = list(sig.parameters.keys())



def test_formalexpression_is_not_abstract():
    assert not inspect.isabstract(FormalExpression)


def test_formalexpression_constructor_exists():
    assert callable(FormalExpression.__init__)


def test_formalexpression_constructor_args():
    sig = inspect.signature(FormalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gateways_eventbasedgateway_is_not_abstract():
    assert not inspect.isabstract(gateways_EventBasedGateway)


def test_gateways_eventbasedgateway_constructor_exists():
    assert callable(gateways_EventBasedGateway.__init__)


def test_gateways_eventbasedgateway_constructor_args():
    sig = inspect.signature(gateways_EventBasedGateway.__init__)
    params = list(sig.parameters.keys())



def test_flows_flownode_is_not_abstract():
    assert not inspect.isabstract(flows_FlowNode)


def test_flows_flownode_constructor_exists():
    assert callable(flows_FlowNode.__init__)


def test_flows_flownode_constructor_args():
    sig = inspect.signature(flows_FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_extension_extensionattributevalue_is_not_abstract():
    assert not inspect.isabstract(extension_ExtensionAttributeValue)


def test_extension_extensionattributevalue_constructor_exists():
    assert callable(extension_ExtensionAttributeValue.__init__)


def test_extension_extensionattributevalue_constructor_args():
    sig = inspect.signature(extension_ExtensionAttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_extension_extension_is_not_abstract():
    assert not inspect.isabstract(extension_Extension)


def test_extension_extension_constructor_exists():
    assert callable(extension_Extension.__init__)


def test_extension_extension_constructor_args():
    sig = inspect.signature(extension_Extension.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_gateways_exclusivegateway_is_not_abstract():
    assert not inspect.isabstract(gateways_ExclusiveGateway)


def test_gateways_exclusivegateway_constructor_exists():
    assert callable(gateways_ExclusiveGateway.__init__)


def test_gateways_exclusivegateway_constructor_args():
    sig = inspect.signature(gateways_ExclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_endpoint_is_not_abstract():
    assert not inspect.isabstract(EndPoint)


def test_endpoint_constructor_exists():
    assert callable(EndPoint.__init__)


def test_endpoint_constructor_args():
    sig = inspect.signature(EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_events_event_is_not_abstract():
    assert not inspect.isabstract(events_Event)


def test_events_event_constructor_exists():
    assert callable(events_Event.__init__)


def test_events_event_constructor_args():
    sig = inspect.signature(events_Event.__init__)
    params = list(sig.parameters.keys())



def test_events_escalationeventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_EscalationEventDefinition)


def test_events_escalationeventdefinition_constructor_exists():
    assert callable(events_EscalationEventDefinition.__init__)


def test_events_escalationeventdefinition_constructor_args():
    sig = inspect.signature(events_EscalationEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_escalation_is_not_abstract():
    assert not inspect.isabstract(Escalation)


def test_escalation_constructor_exists():
    assert callable(Escalation.__init__)


def test_escalation_constructor_args():
    sig = inspect.signature(Escalation.__init__)
    params = list(sig.parameters.keys())



def test_events_erroreventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_ErrorEventDefinition)


def test_events_erroreventdefinition_constructor_exists():
    assert callable(events_ErrorEventDefinition.__init__)


def test_events_erroreventdefinition_constructor_args():
    sig = inspect.signature(events_ErrorEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_error_is_not_abstract():
    assert not inspect.isabstract(Error)


def test_error_constructor_exists():
    assert callable(Error.__init__)


def test_error_constructor_args():
    sig = inspect.signature(Error.__init__)
    params = list(sig.parameters.keys())



def test_events_endevent_is_not_abstract():
    assert not inspect.isabstract(events_EndEvent)


def test_events_endevent_constructor_exists():
    assert callable(events_EndEvent.__init__)


def test_events_endevent_constructor_args():
    sig = inspect.signature(events_EndEvent.__init__)
    params = list(sig.parameters.keys())



def test_documentation_is_not_abstract():
    assert not inspect.isabstract(Documentation)


def test_documentation_constructor_exists():
    assert callable(Documentation.__init__)


def test_documentation_constructor_args():
    sig = inspect.signature(Documentation.__init__)
    params = list(sig.parameters.keys())



def test_definitions_is_not_abstract():
    assert not inspect.isabstract(Definitions)


def test_definitions_constructor_exists():
    assert callable(Definitions.__init__)


def test_definitions_constructor_args():
    sig = inspect.signature(Definitions.__init__)
    params = list(sig.parameters.keys())



def test_datastorereference_is_not_abstract():
    assert not inspect.isabstract(DataStoreReference)


def test_datastorereference_constructor_exists():
    assert callable(DataStoreReference.__init__)


def test_datastorereference_constructor_args():
    sig = inspect.signature(DataStoreReference.__init__)
    params = list(sig.parameters.keys())



def test_datastore_is_not_abstract():
    assert not inspect.isabstract(DataStore)


def test_datastore_constructor_exists():
    assert callable(DataStore.__init__)


def test_datastore_constructor_args():
    sig = inspect.signature(DataStore.__init__)
    params = list(sig.parameters.keys())



def test_datastate_is_not_abstract():
    assert not inspect.isabstract(DataState)


def test_datastate_constructor_exists():
    assert callable(DataState.__init__)


def test_datastate_constructor_args():
    sig = inspect.signature(DataState.__init__)
    params = list(sig.parameters.keys())



def test_dataassociation_is_not_abstract():
    assert not inspect.isabstract(DataAssociation)


def test_dataassociation_constructor_exists():
    assert callable(DataAssociation.__init__)


def test_dataassociation_constructor_args():
    sig = inspect.signature(DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_dataoutputassociation_is_not_abstract():
    assert not inspect.isabstract(DataOutputAssociation)


def test_dataoutputassociation_constructor_exists():
    assert callable(DataOutputAssociation.__init__)


def test_dataoutputassociation_constructor_args():
    sig = inspect.signature(DataOutputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_dataoutput_is_not_abstract():
    assert not inspect.isabstract(DataOutput)


def test_dataoutput_constructor_exists():
    assert callable(DataOutput.__init__)


def test_dataoutput_constructor_args():
    sig = inspect.signature(DataOutput.__init__)
    params = list(sig.parameters.keys())



def test_dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(DataObjectReference)


def test_dataobjectreference_constructor_exists():
    assert callable(DataObjectReference.__init__)


def test_dataobjectreference_constructor_args():
    sig = inspect.signature(DataObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_dataobject_is_not_abstract():
    assert not inspect.isabstract(DataObject)


def test_dataobject_constructor_exists():
    assert callable(DataObject.__init__)


def test_dataobject_constructor_args():
    sig = inspect.signature(DataObject.__init__)
    params = list(sig.parameters.keys())



def test_datainputassociation_is_not_abstract():
    assert not inspect.isabstract(DataInputAssociation)


def test_datainputassociation_constructor_exists():
    assert callable(DataInputAssociation.__init__)


def test_datainputassociation_constructor_args():
    sig = inspect.signature(DataInputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_datainput_is_not_abstract():
    assert not inspect.isabstract(DataInput)


def test_datainput_constructor_exists():
    assert callable(DataInput.__init__)


def test_datainput_constructor_args():
    sig = inspect.signature(DataInput.__init__)
    params = list(sig.parameters.keys())



def test_conversationassociation_is_not_abstract():
    assert not inspect.isabstract(ConversationAssociation)


def test_conversationassociation_constructor_exists():
    assert callable(ConversationAssociation.__init__)


def test_conversationassociation_constructor_args():
    sig = inspect.signature(ConversationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_correlations_correlationsubscription_is_not_abstract():
    assert not inspect.isabstract(correlations_CorrelationSubscription)


def test_correlations_correlationsubscription_constructor_exists():
    assert callable(correlations_CorrelationSubscription.__init__)


def test_correlations_correlationsubscription_constructor_args():
    sig = inspect.signature(correlations_CorrelationSubscription.__init__)
    params = list(sig.parameters.keys())



def test_correlations_correlationpropertyretrievalexpression_is_not_abstract():
    assert not inspect.isabstract(correlations_CorrelationPropertyRetrievalExpression)


def test_correlations_correlationpropertyretrievalexpression_constructor_exists():
    assert callable(correlations_CorrelationPropertyRetrievalExpression.__init__)


def test_correlations_correlationpropertyretrievalexpression_constructor_args():
    sig = inspect.signature(correlations_CorrelationPropertyRetrievalExpression.__init__)
    params = list(sig.parameters.keys())



def test_correlations_correlationpropertybinding_is_not_abstract():
    assert not inspect.isabstract(correlations_CorrelationPropertyBinding)


def test_correlations_correlationpropertybinding_constructor_exists():
    assert callable(correlations_CorrelationPropertyBinding.__init__)


def test_correlations_correlationpropertybinding_constructor_args():
    sig = inspect.signature(correlations_CorrelationPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_correlations_correlationproperty_is_not_abstract():
    assert not inspect.isabstract(correlations_CorrelationProperty)


def test_correlations_correlationproperty_constructor_exists():
    assert callable(correlations_CorrelationProperty.__init__)


def test_correlations_correlationproperty_constructor_args():
    sig = inspect.signature(correlations_CorrelationProperty.__init__)
    params = list(sig.parameters.keys())



def test_correlations_correlationkey_is_not_abstract():
    assert not inspect.isabstract(correlations_CorrelationKey)


def test_correlations_correlationkey_constructor_exists():
    assert callable(correlations_CorrelationKey.__init__)


def test_correlations_correlationkey_constructor_args():
    sig = inspect.signature(correlations_CorrelationKey.__init__)
    params = list(sig.parameters.keys())



def test_conversationlink_is_not_abstract():
    assert not inspect.isabstract(ConversationLink)


def test_conversationlink_constructor_exists():
    assert callable(ConversationLink.__init__)


def test_conversationlink_constructor_args():
    sig = inspect.signature(ConversationLink.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivities_choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(choreographyactivities_ChoreographyActivity)


def test_choreographyactivities_choreographyactivity_constructor_exists():
    assert callable(choreographyactivities_ChoreographyActivity.__init__)


def test_choreographyactivities_choreographyactivity_constructor_args():
    sig = inspect.signature(choreographyactivities_ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())



def test_conversation_is_not_abstract():
    assert not inspect.isabstract(Conversation)


def test_conversation_constructor_exists():
    assert callable(Conversation.__init__)


def test_conversation_constructor_args():
    sig = inspect.signature(Conversation.__init__)
    params = list(sig.parameters.keys())



def test_events_conditionaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_ConditionalEventDefinition)


def test_events_conditionaleventdefinition_constructor_exists():
    assert callable(events_ConditionalEventDefinition.__init__)


def test_events_conditionaleventdefinition_constructor_args():
    sig = inspect.signature(events_ConditionalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gateways_complexgateway_is_not_abstract():
    assert not inspect.isabstract(gateways_ComplexGateway)


def test_gateways_complexgateway_constructor_exists():
    assert callable(gateways_ComplexGateway.__init__)


def test_gateways_complexgateway_constructor_args():
    sig = inspect.signature(gateways_ComplexGateway.__init__)
    params = list(sig.parameters.keys())



def test_complexbehaviordefinition_is_not_abstract():
    assert not inspect.isabstract(ComplexBehaviorDefinition)


def test_complexbehaviordefinition_constructor_exists():
    assert callable(ComplexBehaviorDefinition.__init__)


def test_complexbehaviordefinition_constructor_args():
    sig = inspect.signature(ComplexBehaviorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_events_compensateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_CompensateEventDefinition)


def test_events_compensateeventdefinition_constructor_exists():
    assert callable(events_CompensateEventDefinition.__init__)


def test_events_compensateeventdefinition_constructor_args():
    sig = inspect.signature(events_CompensateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivities_choreographytask_is_not_abstract():
    assert not inspect.isabstract(choreographyactivities_ChoreographyTask)


def test_choreographyactivities_choreographytask_constructor_exists():
    assert callable(choreographyactivities_ChoreographyTask.__init__)


def test_choreographyactivities_choreographytask_constructor_args():
    sig = inspect.signature(choreographyactivities_ChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_events_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_EventDefinition)


def test_events_eventdefinition_constructor_exists():
    assert callable(events_EventDefinition.__init__)


def test_events_eventdefinition_constructor_args():
    sig = inspect.signature(events_EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_collaboration_is_not_abstract():
    assert not inspect.isabstract(Collaboration)


def test_collaboration_constructor_exists():
    assert callable(Collaboration.__init__)


def test_collaboration_constructor_args():
    sig = inspect.signature(Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_choreography_is_not_abstract():
    assert not inspect.isabstract(Choreography)


def test_choreography_constructor_exists():
    assert callable(Choreography.__init__)


def test_choreography_constructor_args():
    sig = inspect.signature(Choreography.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_categoryvalue_is_not_abstract():
    assert not inspect.isabstract(artifacts_CategoryValue)


def test_artifacts_categoryvalue_constructor_exists():
    assert callable(artifacts_CategoryValue.__init__)


def test_artifacts_categoryvalue_constructor_args():
    sig = inspect.signature(artifacts_CategoryValue.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_category_is_not_abstract():
    assert not inspect.isabstract(artifacts_Category)


def test_artifacts_category_constructor_exists():
    assert callable(artifacts_Category.__init__)


def test_artifacts_category_constructor_args():
    sig = inspect.signature(artifacts_Category.__init__)
    params = list(sig.parameters.keys())



def test_events_catchevent_is_not_abstract():
    assert not inspect.isabstract(events_CatchEvent)


def test_events_catchevent_constructor_exists():
    assert callable(events_CatchEvent.__init__)


def test_events_catchevent_constructor_args():
    sig = inspect.signature(events_CatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_rootelement_is_not_abstract():
    assert not inspect.isabstract(RootElement)


def test_rootelement_constructor_exists():
    assert callable(RootElement.__init__)


def test_rootelement_constructor_args():
    sig = inspect.signature(RootElement.__init__)
    params = list(sig.parameters.keys())



def test_events_canceleventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_CancelEventDefinition)


def test_events_canceleventdefinition_constructor_exists():
    assert callable(events_CancelEventDefinition.__init__)


def test_events_canceleventdefinition_constructor_args():
    sig = inspect.signature(events_CancelEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_conversationnode_is_not_abstract():
    assert not inspect.isabstract(ConversationNode)


def test_conversationnode_constructor_exists():
    assert callable(ConversationNode.__init__)


def test_conversationnode_constructor_args():
    sig = inspect.signature(ConversationNode.__init__)
    params = list(sig.parameters.keys())



def test_callconversation_is_not_abstract():
    assert not inspect.isabstract(CallConversation)


def test_callconversation_constructor_exists():
    assert callable(CallConversation.__init__)


def test_callconversation_constructor_args():
    sig = inspect.signature(CallConversation.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivities_callchoreography_is_not_abstract():
    assert not inspect.isabstract(choreographyactivities_CallChoreography)


def test_choreographyactivities_callchoreography_constructor_exists():
    assert callable(choreographyactivities_CallChoreography.__init__)


def test_choreographyactivities_callchoreography_constructor_args():
    sig = inspect.signature(choreographyactivities_CallChoreography.__init__)
    params = list(sig.parameters.keys())



def test_callactivity_is_not_abstract():
    assert not inspect.isabstract(CallActivity)


def test_callactivity_constructor_exists():
    assert callable(CallActivity.__init__)


def test_callactivity_constructor_args():
    sig = inspect.signature(CallActivity.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_businessruletask_is_not_abstract():
    assert not inspect.isabstract(BusinessRuleTask)


def test_businessruletask_constructor_exists():
    assert callable(BusinessRuleTask.__init__)


def test_businessruletask_constructor_args():
    sig = inspect.signature(BusinessRuleTask.__init__)
    params = list(sig.parameters.keys())



def test_events_boundaryevent_is_not_abstract():
    assert not inspect.isabstract(events_BoundaryEvent)


def test_events_boundaryevent_constructor_exists():
    assert callable(events_BoundaryEvent.__init__)


def test_events_boundaryevent_constructor_args():
    sig = inspect.signature(events_BoundaryEvent.__init__)
    params = list(sig.parameters.keys())



def test_baseelement_is_not_abstract():
    assert not inspect.isabstract(BaseElement)


def test_baseelement_constructor_exists():
    assert callable(BaseElement.__init__)


def test_baseelement_constructor_args():
    sig = inspect.signature(BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_auditing_is_not_abstract():
    assert not inspect.isabstract(Auditing)


def test_auditing_constructor_exists():
    assert callable(Auditing.__init__)


def test_auditing_constructor_args():
    sig = inspect.signature(Auditing.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_association_is_not_abstract():
    assert not inspect.isabstract(artifacts_Association)


def test_artifacts_association_constructor_exists():
    assert callable(artifacts_Association.__init__)


def test_artifacts_association_constructor_args():
    sig = inspect.signature(artifacts_Association.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EStringToStringMapEntry)


def test_bpmn2_estringtostringmapentry_constructor_exists():
    assert callable(bpmn2_EStringToStringMapEntry.__init__)


def test_bpmn2_estringtostringmapentry_constructor_args():
    sig = inspect.signature(bpmn2_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_artifact_is_not_abstract():
    assert not inspect.isabstract(artifacts_Artifact)


def test_artifacts_artifact_constructor_exists():
    assert callable(artifacts_Artifact.__init__)


def test_artifacts_artifact_constructor_args():
    sig = inspect.signature(artifacts_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_flows_flowelement_is_not_abstract():
    assert not inspect.isabstract(flows_FlowElement)


def test_flows_flowelement_constructor_exists():
    assert callable(flows_FlowElement.__init__)


def test_flows_flowelement_constructor_args():
    sig = inspect.signature(flows_FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_adhocsubprocess_is_not_abstract():
    assert not inspect.isabstract(AdHocSubProcess)


def test_adhocsubprocess_constructor_exists():
    assert callable(AdHocSubProcess.__init__)


def test_adhocsubprocess_constructor_args():
    sig = inspect.signature(AdHocSubProcess.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_documentroot_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DocumentRoot)


def test_bpmn2_documentroot_constructor_exists():
    assert callable(bpmn2_DocumentRoot.__init__)


def test_bpmn2_documentroot_constructor_args():
    sig = inspect.signature(bpmn2_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_bpmn2_documentroot_has_mixed():
    assert hasattr(bpmn2_DocumentRoot, "mixed")
    descriptor = None
    for klass in bpmn2_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_usertask_is_not_abstract():
    assert not inspect.isabstract(UserTask)


def test_usertask_constructor_exists():
    assert callable(UserTask.__init__)


def test_usertask_constructor_args():
    sig = inspect.signature(UserTask.__init__)
    params = list(sig.parameters.keys())



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())



def test_events_timereventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_TimerEventDefinition)


def test_events_timereventdefinition_constructor_exists():
    assert callable(events_TimerEventDefinition.__init__)


def test_events_timereventdefinition_constructor_args():
    sig = inspect.signature(events_TimerEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_events_throwevent_is_not_abstract():
    assert not inspect.isabstract(events_ThrowEvent)


def test_events_throwevent_constructor_exists():
    assert callable(events_ThrowEvent.__init__)


def test_events_throwevent_constructor_args():
    sig = inspect.signature(events_ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_artifacts_textannotation_is_not_abstract():
    assert not inspect.isabstract(artifacts_TextAnnotation)


def test_artifacts_textannotation_constructor_exists():
    assert callable(artifacts_TextAnnotation.__init__)


def test_artifacts_textannotation_constructor_args():
    sig = inspect.signature(artifacts_TextAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_events_terminateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_TerminateEventDefinition)


def test_events_terminateeventdefinition_constructor_exists():
    assert callable(events_TerminateEventDefinition.__init__)


def test_events_terminateeventdefinition_constructor_args():
    sig = inspect.signature(events_TerminateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_events_startevent_is_not_abstract():
    assert not inspect.isabstract(events_StartEvent)


def test_events_startevent_constructor_exists():
    assert callable(events_StartEvent.__init__)


def test_events_startevent_constructor_args():
    sig = inspect.signature(events_StartEvent.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_subprocess_is_not_abstract():
    assert not inspect.isabstract(SubProcess)


def test_subprocess_constructor_exists():
    assert callable(SubProcess.__init__)


def test_subprocess_constructor_args():
    sig = inspect.signature(SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_subconversation_is_not_abstract():
    assert not inspect.isabstract(SubConversation)


def test_subconversation_constructor_exists():
    assert callable(SubConversation.__init__)


def test_subconversation_constructor_args():
    sig = inspect.signature(SubConversation.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivities_subchoreography_is_not_abstract():
    assert not inspect.isabstract(choreographyactivities_SubChoreography)


def test_choreographyactivities_subchoreography_constructor_exists():
    assert callable(choreographyactivities_SubChoreography.__init__)


def test_choreographyactivities_subchoreography_constructor_args():
    sig = inspect.signature(choreographyactivities_SubChoreography.__init__)
    params = list(sig.parameters.keys())



def test_standardloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(StandardLoopCharacteristics)


def test_standardloopcharacteristics_constructor_exists():
    assert callable(StandardLoopCharacteristics.__init__)


def test_standardloopcharacteristics_constructor_args():
    sig = inspect.signature(StandardLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_events_signaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(events_SignalEventDefinition)


def test_events_signaleventdefinition_constructor_exists():
    assert callable(events_SignalEventDefinition.__init__)


def test_events_signaleventdefinition_constructor_args():
    sig = inspect.signature(events_SignalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_events_signal_is_not_abstract():
    assert not inspect.isabstract(events_Signal)


def test_events_signal_constructor_exists():
    assert callable(events_Signal.__init__)


def test_events_signal_constructor_args():
    sig = inspect.signature(events_Signal.__init__)
    params = list(sig.parameters.keys())



def test_servicetask_is_not_abstract():
    assert not inspect.isabstract(ServiceTask)


def test_servicetask_constructor_exists():
    assert callable(ServiceTask.__init__)


def test_servicetask_constructor_args():
    sig = inspect.signature(ServiceTask.__init__)
    params = list(sig.parameters.keys())



def test_resourceparameter_is_not_abstract():
    assert not inspect.isabstract(ResourceParameter)


def test_resourceparameter_constructor_exists():
    assert callable(ResourceParameter.__init__)


def test_resourceparameter_constructor_args():
    sig = inspect.signature(ResourceParameter.__init__)
    params = list(sig.parameters.keys())



def test_flows_sequenceflow_is_not_abstract():
    assert not inspect.isabstract(flows_SequenceFlow)


def test_flows_sequenceflow_constructor_exists():
    assert callable(flows_SequenceFlow.__init__)


def test_flows_sequenceflow_constructor_args():
    sig = inspect.signature(flows_SequenceFlow.__init__)
    params = list(sig.parameters.keys())



def test_sendtask_is_not_abstract():
    assert not inspect.isabstract(SendTask)


def test_sendtask_constructor_exists():
    assert callable(SendTask.__init__)


def test_sendtask_constructor_args():
    sig = inspect.signature(SendTask.__init__)
    params = list(sig.parameters.keys())



def test_scripttask_is_not_abstract():
    assert not inspect.isabstract(ScriptTask)


def test_scripttask_constructor_exists():
    assert callable(ScriptTask.__init__)


def test_scripttask_constructor_args():
    sig = inspect.signature(ScriptTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_eobject_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EObject)


def test_bpmn2_eobject_constructor_exists():
    assert callable(bpmn2_EObject.__init__)


def test_bpmn2_eobject_constructor_args():
    sig = inspect.signature(bpmn2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_resourceparameterbinding_is_not_abstract():
    assert not inspect.isabstract(ResourceParameterBinding)


def test_resourceparameterbinding_constructor_exists():
    assert callable(ResourceParameterBinding.__init__)


def test_resourceparameterbinding_constructor_args():
    sig = inspect.signature(ResourceParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_receivetask_is_not_abstract():
    assert not inspect.isabstract(ReceiveTask)


def test_receivetask_constructor_exists():
    assert callable(ReceiveTask.__init__)


def test_receivetask_constructor_args():
    sig = inspect.signature(ReceiveTask.__init__)
    params = list(sig.parameters.keys())



def test_resourceassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ResourceAssignmentExpression)


def test_resourceassignmentexpression_constructor_exists():
    assert callable(ResourceAssignmentExpression.__init__)


def test_resourceassignmentexpression_constructor_args():
    sig = inspect.signature(ResourceAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_rendering_is_not_abstract():
    assert not inspect.isabstract(Rendering)


def test_rendering_constructor_exists():
    assert callable(Rendering.__init__)


def test_rendering_constructor_args():
    sig = inspect.signature(Rendering.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Relationship_strategy = st.builds(
    Relationship,
)
Property_strategy = st.builds(
    Property,
)
Process_strategy = st.builds(
    Process,
)
PotentialOwner_strategy = st.builds(
    PotentialOwner,
)
PartnerRole_strategy = st.builds(
    PartnerRole,
)
PartnerEntity_strategy = st.builds(
    PartnerEntity,
)
ParticipantMultiplicity_strategy = st.builds(
    ParticipantMultiplicity,
)
ParticipantAssociation_strategy = st.builds(
    ParticipantAssociation,
)
Participant_strategy = st.builds(
    Participant,
)
gateways_ParallelGateway_strategy = st.builds(
    gateways_ParallelGateway,
)
OutputSet_strategy = st.builds(
    OutputSet,
)
Operation_strategy = st.builds(
    Operation,
)
MultiInstanceLoopCharacteristics_strategy = st.builds(
    MultiInstanceLoopCharacteristics,
)
Monitoring_strategy = st.builds(
    Monitoring,
)
MessageFlowAssociation_strategy = st.builds(
    MessageFlowAssociation,
)
MessageFlow_strategy = st.builds(
    MessageFlow,
)
MessageEventDefinition_strategy = st.builds(
    MessageEventDefinition,
)
Message_strategy = st.builds(
    Message,
)
ItemDefinition_strategy = st.builds(
    ItemDefinition,
)
ManualTask_strategy = st.builds(
    ManualTask,
)
LoopCharacteristics_strategy = st.builds(
    LoopCharacteristics,
)
events_LinkEventDefinition_strategy = st.builds(
    events_LinkEventDefinition,
)
LaneSet_strategy = st.builds(
    LaneSet,
)
Lane_strategy = st.builds(
    Lane,
)
InputSet_strategy = st.builds(
    InputSet,
)
InputOutputSpecification_strategy = st.builds(
    InputOutputSpecification,
)
InputOutputBinding_strategy = st.builds(
    InputOutputBinding,
)
events_IntermediateThrowEvent_strategy = st.builds(
    events_IntermediateThrowEvent,
)
events_IntermediateCatchEvent_strategy = st.builds(
    events_IntermediateCatchEvent,
)
Interface_strategy = st.builds(
    Interface,
)
gateways_InclusiveGateway_strategy = st.builds(
    gateways_InclusiveGateway,
)
Import_strategy = st.builds(
    Import,
)
events_ImplicitThrowEvent_strategy = st.builds(
    events_ImplicitThrowEvent,
)
ResourceRole_strategy = st.builds(
    ResourceRole,
)
Performer_strategy = st.builds(
    Performer,
)
HumanPerformer_strategy = st.builds(
    HumanPerformer,
)
artifacts_Group_strategy = st.builds(
    artifacts_Group,
)
GlobalUserTask_strategy = st.builds(
    GlobalUserTask,
)
GlobalTask_strategy = st.builds(
    GlobalTask,
)
GlobalScriptTask_strategy = st.builds(
    GlobalScriptTask,
)
GlobalManualTask_strategy = st.builds(
    GlobalManualTask,
)
GlobalConversation_strategy = st.builds(
    GlobalConversation,
)
GlobalChoreographyTask_strategy = st.builds(
    GlobalChoreographyTask,
)
GlobalBusinessRuleTask_strategy = st.builds(
    GlobalBusinessRuleTask,
)
gateways_Gateway_strategy = st.builds(
    gateways_Gateway,
)
FormalExpression_strategy = st.builds(
    FormalExpression,
)
gateways_EventBasedGateway_strategy = st.builds(
    gateways_EventBasedGateway,
)
flows_FlowNode_strategy = st.builds(
    flows_FlowNode,
)
extension_ExtensionAttributeValue_strategy = st.builds(
    extension_ExtensionAttributeValue,
)
extension_Extension_strategy = st.builds(
    extension_Extension,
)
Expression_strategy = st.builds(
    Expression,
)
gateways_ExclusiveGateway_strategy = st.builds(
    gateways_ExclusiveGateway,
)
EndPoint_strategy = st.builds(
    EndPoint,
)
events_Event_strategy = st.builds(
    events_Event,
)
events_EscalationEventDefinition_strategy = st.builds(
    events_EscalationEventDefinition,
)
Escalation_strategy = st.builds(
    Escalation,
)
events_ErrorEventDefinition_strategy = st.builds(
    events_ErrorEventDefinition,
)
Error_strategy = st.builds(
    Error,
)
events_EndEvent_strategy = st.builds(
    events_EndEvent,
)
Documentation_strategy = st.builds(
    Documentation,
)
Definitions_strategy = st.builds(
    Definitions,
)
DataStoreReference_strategy = st.builds(
    DataStoreReference,
)
DataStore_strategy = st.builds(
    DataStore,
)
DataState_strategy = st.builds(
    DataState,
)
DataAssociation_strategy = st.builds(
    DataAssociation,
)
DataOutputAssociation_strategy = st.builds(
    DataOutputAssociation,
)
DataOutput_strategy = st.builds(
    DataOutput,
)
DataObjectReference_strategy = st.builds(
    DataObjectReference,
)
DataObject_strategy = st.builds(
    DataObject,
)
DataInputAssociation_strategy = st.builds(
    DataInputAssociation,
)
DataInput_strategy = st.builds(
    DataInput,
)
ConversationAssociation_strategy = st.builds(
    ConversationAssociation,
)
correlations_CorrelationSubscription_strategy = st.builds(
    correlations_CorrelationSubscription,
)
correlations_CorrelationPropertyRetrievalExpression_strategy = st.builds(
    correlations_CorrelationPropertyRetrievalExpression,
)
correlations_CorrelationPropertyBinding_strategy = st.builds(
    correlations_CorrelationPropertyBinding,
)
correlations_CorrelationProperty_strategy = st.builds(
    correlations_CorrelationProperty,
)
correlations_CorrelationKey_strategy = st.builds(
    correlations_CorrelationKey,
)
ConversationLink_strategy = st.builds(
    ConversationLink,
)
choreographyactivities_ChoreographyActivity_strategy = st.builds(
    choreographyactivities_ChoreographyActivity,
)
Conversation_strategy = st.builds(
    Conversation,
)
events_ConditionalEventDefinition_strategy = st.builds(
    events_ConditionalEventDefinition,
)
gateways_ComplexGateway_strategy = st.builds(
    gateways_ComplexGateway,
)
ComplexBehaviorDefinition_strategy = st.builds(
    ComplexBehaviorDefinition,
)
events_CompensateEventDefinition_strategy = st.builds(
    events_CompensateEventDefinition,
)
choreographyactivities_ChoreographyTask_strategy = st.builds(
    choreographyactivities_ChoreographyTask,
)
events_EventDefinition_strategy = st.builds(
    events_EventDefinition,
)
Collaboration_strategy = st.builds(
    Collaboration,
)
Choreography_strategy = st.builds(
    Choreography,
)
artifacts_CategoryValue_strategy = st.builds(
    artifacts_CategoryValue,
)
artifacts_Category_strategy = st.builds(
    artifacts_Category,
)
events_CatchEvent_strategy = st.builds(
    events_CatchEvent,
)
RootElement_strategy = st.builds(
    RootElement,
)
events_CancelEventDefinition_strategy = st.builds(
    events_CancelEventDefinition,
)
ConversationNode_strategy = st.builds(
    ConversationNode,
)
CallConversation_strategy = st.builds(
    CallConversation,
)
choreographyactivities_CallChoreography_strategy = st.builds(
    choreographyactivities_CallChoreography,
)
CallActivity_strategy = st.builds(
    CallActivity,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
Assignment_strategy = st.builds(
    Assignment,
)
BusinessRuleTask_strategy = st.builds(
    BusinessRuleTask,
)
events_BoundaryEvent_strategy = st.builds(
    events_BoundaryEvent,
)
BaseElement_strategy = st.builds(
    BaseElement,
)
Auditing_strategy = st.builds(
    Auditing,
)
artifacts_Association_strategy = st.builds(
    artifacts_Association,
)
bpmn2_EStringToStringMapEntry_strategy = st.builds(
    bpmn2_EStringToStringMapEntry,
)
artifacts_Artifact_strategy = st.builds(
    artifacts_Artifact,
)
flows_FlowElement_strategy = st.builds(
    flows_FlowElement,
)
AdHocSubProcess_strategy = st.builds(
    AdHocSubProcess,
)
Activity_strategy = st.builds(
    Activity,
)
bpmn2_DocumentRoot_strategy = st.builds(
    bpmn2_DocumentRoot,
    mixed=
        safe_text
)
UserTask_strategy = st.builds(
    UserTask,
)
Transaction_strategy = st.builds(
    Transaction,
)
events_TimerEventDefinition_strategy = st.builds(
    events_TimerEventDefinition,
)
events_ThrowEvent_strategy = st.builds(
    events_ThrowEvent,
)
artifacts_TextAnnotation_strategy = st.builds(
    artifacts_TextAnnotation,
)
events_TerminateEventDefinition_strategy = st.builds(
    events_TerminateEventDefinition,
)
events_StartEvent_strategy = st.builds(
    events_StartEvent,
)
Task_strategy = st.builds(
    Task,
)
SubProcess_strategy = st.builds(
    SubProcess,
)
SubConversation_strategy = st.builds(
    SubConversation,
)
choreographyactivities_SubChoreography_strategy = st.builds(
    choreographyactivities_SubChoreography,
)
StandardLoopCharacteristics_strategy = st.builds(
    StandardLoopCharacteristics,
)
events_SignalEventDefinition_strategy = st.builds(
    events_SignalEventDefinition,
)
events_Signal_strategy = st.builds(
    events_Signal,
)
ServiceTask_strategy = st.builds(
    ServiceTask,
)
ResourceParameter_strategy = st.builds(
    ResourceParameter,
)
flows_SequenceFlow_strategy = st.builds(
    flows_SequenceFlow,
)
SendTask_strategy = st.builds(
    SendTask,
)
ScriptTask_strategy = st.builds(
    ScriptTask,
)
bpmn2_EObject_strategy = st.builds(
    bpmn2_EObject,
)
ResourceParameterBinding_strategy = st.builds(
    ResourceParameterBinding,
)
ReceiveTask_strategy = st.builds(
    ReceiveTask,
)
ResourceAssignmentExpression_strategy = st.builds(
    ResourceAssignmentExpression,
)
Resource_strategy = st.builds(
    Resource,
)
Rendering_strategy = st.builds(
    Rendering,
)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=PotentialOwner_strategy)
@settings(max_examples=50)
def test_potentialowner_instantiation(instance):
    assert isinstance(instance, PotentialOwner)

@given(instance=PartnerRole_strategy)
@settings(max_examples=50)
def test_partnerrole_instantiation(instance):
    assert isinstance(instance, PartnerRole)

@given(instance=PartnerEntity_strategy)
@settings(max_examples=50)
def test_partnerentity_instantiation(instance):
    assert isinstance(instance, PartnerEntity)

@given(instance=ParticipantMultiplicity_strategy)
@settings(max_examples=50)
def test_participantmultiplicity_instantiation(instance):
    assert isinstance(instance, ParticipantMultiplicity)

@given(instance=ParticipantAssociation_strategy)
@settings(max_examples=50)
def test_participantassociation_instantiation(instance):
    assert isinstance(instance, ParticipantAssociation)

@given(instance=Participant_strategy)
@settings(max_examples=50)
def test_participant_instantiation(instance):
    assert isinstance(instance, Participant)

@given(instance=gateways_ParallelGateway_strategy)
@settings(max_examples=50)
def test_gateways_parallelgateway_instantiation(instance):
    assert isinstance(instance, gateways_ParallelGateway)

@given(instance=OutputSet_strategy)
@settings(max_examples=50)
def test_outputset_instantiation(instance):
    assert isinstance(instance, OutputSet)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=MultiInstanceLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_multiinstanceloopcharacteristics_instantiation(instance):
    assert isinstance(instance, MultiInstanceLoopCharacteristics)

@given(instance=Monitoring_strategy)
@settings(max_examples=50)
def test_monitoring_instantiation(instance):
    assert isinstance(instance, Monitoring)

@given(instance=MessageFlowAssociation_strategy)
@settings(max_examples=50)
def test_messageflowassociation_instantiation(instance):
    assert isinstance(instance, MessageFlowAssociation)

@given(instance=MessageFlow_strategy)
@settings(max_examples=50)
def test_messageflow_instantiation(instance):
    assert isinstance(instance, MessageFlow)

@given(instance=MessageEventDefinition_strategy)
@settings(max_examples=50)
def test_messageeventdefinition_instantiation(instance):
    assert isinstance(instance, MessageEventDefinition)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=ItemDefinition_strategy)
@settings(max_examples=50)
def test_itemdefinition_instantiation(instance):
    assert isinstance(instance, ItemDefinition)

@given(instance=ManualTask_strategy)
@settings(max_examples=50)
def test_manualtask_instantiation(instance):
    assert isinstance(instance, ManualTask)

@given(instance=LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, LoopCharacteristics)

@given(instance=events_LinkEventDefinition_strategy)
@settings(max_examples=50)
def test_events_linkeventdefinition_instantiation(instance):
    assert isinstance(instance, events_LinkEventDefinition)

@given(instance=LaneSet_strategy)
@settings(max_examples=50)
def test_laneset_instantiation(instance):
    assert isinstance(instance, LaneSet)

@given(instance=Lane_strategy)
@settings(max_examples=50)
def test_lane_instantiation(instance):
    assert isinstance(instance, Lane)

@given(instance=InputSet_strategy)
@settings(max_examples=50)
def test_inputset_instantiation(instance):
    assert isinstance(instance, InputSet)

@given(instance=InputOutputSpecification_strategy)
@settings(max_examples=50)
def test_inputoutputspecification_instantiation(instance):
    assert isinstance(instance, InputOutputSpecification)

@given(instance=InputOutputBinding_strategy)
@settings(max_examples=50)
def test_inputoutputbinding_instantiation(instance):
    assert isinstance(instance, InputOutputBinding)

@given(instance=events_IntermediateThrowEvent_strategy)
@settings(max_examples=50)
def test_events_intermediatethrowevent_instantiation(instance):
    assert isinstance(instance, events_IntermediateThrowEvent)

@given(instance=events_IntermediateCatchEvent_strategy)
@settings(max_examples=50)
def test_events_intermediatecatchevent_instantiation(instance):
    assert isinstance(instance, events_IntermediateCatchEvent)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=gateways_InclusiveGateway_strategy)
@settings(max_examples=50)
def test_gateways_inclusivegateway_instantiation(instance):
    assert isinstance(instance, gateways_InclusiveGateway)

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=events_ImplicitThrowEvent_strategy)
@settings(max_examples=50)
def test_events_implicitthrowevent_instantiation(instance):
    assert isinstance(instance, events_ImplicitThrowEvent)

@given(instance=ResourceRole_strategy)
@settings(max_examples=50)
def test_resourcerole_instantiation(instance):
    assert isinstance(instance, ResourceRole)

@given(instance=Performer_strategy)
@settings(max_examples=50)
def test_performer_instantiation(instance):
    assert isinstance(instance, Performer)

@given(instance=HumanPerformer_strategy)
@settings(max_examples=50)
def test_humanperformer_instantiation(instance):
    assert isinstance(instance, HumanPerformer)

@given(instance=artifacts_Group_strategy)
@settings(max_examples=50)
def test_artifacts_group_instantiation(instance):
    assert isinstance(instance, artifacts_Group)

@given(instance=GlobalUserTask_strategy)
@settings(max_examples=50)
def test_globalusertask_instantiation(instance):
    assert isinstance(instance, GlobalUserTask)

@given(instance=GlobalTask_strategy)
@settings(max_examples=50)
def test_globaltask_instantiation(instance):
    assert isinstance(instance, GlobalTask)

@given(instance=GlobalScriptTask_strategy)
@settings(max_examples=50)
def test_globalscripttask_instantiation(instance):
    assert isinstance(instance, GlobalScriptTask)

@given(instance=GlobalManualTask_strategy)
@settings(max_examples=50)
def test_globalmanualtask_instantiation(instance):
    assert isinstance(instance, GlobalManualTask)

@given(instance=GlobalConversation_strategy)
@settings(max_examples=50)
def test_globalconversation_instantiation(instance):
    assert isinstance(instance, GlobalConversation)

@given(instance=GlobalChoreographyTask_strategy)
@settings(max_examples=50)
def test_globalchoreographytask_instantiation(instance):
    assert isinstance(instance, GlobalChoreographyTask)

@given(instance=GlobalBusinessRuleTask_strategy)
@settings(max_examples=50)
def test_globalbusinessruletask_instantiation(instance):
    assert isinstance(instance, GlobalBusinessRuleTask)

@given(instance=gateways_Gateway_strategy)
@settings(max_examples=50)
def test_gateways_gateway_instantiation(instance):
    assert isinstance(instance, gateways_Gateway)

@given(instance=FormalExpression_strategy)
@settings(max_examples=50)
def test_formalexpression_instantiation(instance):
    assert isinstance(instance, FormalExpression)

@given(instance=gateways_EventBasedGateway_strategy)
@settings(max_examples=50)
def test_gateways_eventbasedgateway_instantiation(instance):
    assert isinstance(instance, gateways_EventBasedGateway)

@given(instance=flows_FlowNode_strategy)
@settings(max_examples=50)
def test_flows_flownode_instantiation(instance):
    assert isinstance(instance, flows_FlowNode)

@given(instance=extension_ExtensionAttributeValue_strategy)
@settings(max_examples=50)
def test_extension_extensionattributevalue_instantiation(instance):
    assert isinstance(instance, extension_ExtensionAttributeValue)

@given(instance=extension_Extension_strategy)
@settings(max_examples=50)
def test_extension_extension_instantiation(instance):
    assert isinstance(instance, extension_Extension)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gateways_ExclusiveGateway_strategy)
@settings(max_examples=50)
def test_gateways_exclusivegateway_instantiation(instance):
    assert isinstance(instance, gateways_ExclusiveGateway)

@given(instance=EndPoint_strategy)
@settings(max_examples=50)
def test_endpoint_instantiation(instance):
    assert isinstance(instance, EndPoint)

@given(instance=events_Event_strategy)
@settings(max_examples=50)
def test_events_event_instantiation(instance):
    assert isinstance(instance, events_Event)

@given(instance=events_EscalationEventDefinition_strategy)
@settings(max_examples=50)
def test_events_escalationeventdefinition_instantiation(instance):
    assert isinstance(instance, events_EscalationEventDefinition)

@given(instance=Escalation_strategy)
@settings(max_examples=50)
def test_escalation_instantiation(instance):
    assert isinstance(instance, Escalation)

@given(instance=events_ErrorEventDefinition_strategy)
@settings(max_examples=50)
def test_events_erroreventdefinition_instantiation(instance):
    assert isinstance(instance, events_ErrorEventDefinition)

@given(instance=Error_strategy)
@settings(max_examples=50)
def test_error_instantiation(instance):
    assert isinstance(instance, Error)

@given(instance=events_EndEvent_strategy)
@settings(max_examples=50)
def test_events_endevent_instantiation(instance):
    assert isinstance(instance, events_EndEvent)

@given(instance=Documentation_strategy)
@settings(max_examples=50)
def test_documentation_instantiation(instance):
    assert isinstance(instance, Documentation)

@given(instance=Definitions_strategy)
@settings(max_examples=50)
def test_definitions_instantiation(instance):
    assert isinstance(instance, Definitions)

@given(instance=DataStoreReference_strategy)
@settings(max_examples=50)
def test_datastorereference_instantiation(instance):
    assert isinstance(instance, DataStoreReference)

@given(instance=DataStore_strategy)
@settings(max_examples=50)
def test_datastore_instantiation(instance):
    assert isinstance(instance, DataStore)

@given(instance=DataState_strategy)
@settings(max_examples=50)
def test_datastate_instantiation(instance):
    assert isinstance(instance, DataState)

@given(instance=DataAssociation_strategy)
@settings(max_examples=50)
def test_dataassociation_instantiation(instance):
    assert isinstance(instance, DataAssociation)

@given(instance=DataOutputAssociation_strategy)
@settings(max_examples=50)
def test_dataoutputassociation_instantiation(instance):
    assert isinstance(instance, DataOutputAssociation)

@given(instance=DataOutput_strategy)
@settings(max_examples=50)
def test_dataoutput_instantiation(instance):
    assert isinstance(instance, DataOutput)

@given(instance=DataObjectReference_strategy)
@settings(max_examples=50)
def test_dataobjectreference_instantiation(instance):
    assert isinstance(instance, DataObjectReference)

@given(instance=DataObject_strategy)
@settings(max_examples=50)
def test_dataobject_instantiation(instance):
    assert isinstance(instance, DataObject)

@given(instance=DataInputAssociation_strategy)
@settings(max_examples=50)
def test_datainputassociation_instantiation(instance):
    assert isinstance(instance, DataInputAssociation)

@given(instance=DataInput_strategy)
@settings(max_examples=50)
def test_datainput_instantiation(instance):
    assert isinstance(instance, DataInput)

@given(instance=ConversationAssociation_strategy)
@settings(max_examples=50)
def test_conversationassociation_instantiation(instance):
    assert isinstance(instance, ConversationAssociation)

@given(instance=correlations_CorrelationSubscription_strategy)
@settings(max_examples=50)
def test_correlations_correlationsubscription_instantiation(instance):
    assert isinstance(instance, correlations_CorrelationSubscription)

@given(instance=correlations_CorrelationPropertyRetrievalExpression_strategy)
@settings(max_examples=50)
def test_correlations_correlationpropertyretrievalexpression_instantiation(instance):
    assert isinstance(instance, correlations_CorrelationPropertyRetrievalExpression)

@given(instance=correlations_CorrelationPropertyBinding_strategy)
@settings(max_examples=50)
def test_correlations_correlationpropertybinding_instantiation(instance):
    assert isinstance(instance, correlations_CorrelationPropertyBinding)

@given(instance=correlations_CorrelationProperty_strategy)
@settings(max_examples=50)
def test_correlations_correlationproperty_instantiation(instance):
    assert isinstance(instance, correlations_CorrelationProperty)

@given(instance=correlations_CorrelationKey_strategy)
@settings(max_examples=50)
def test_correlations_correlationkey_instantiation(instance):
    assert isinstance(instance, correlations_CorrelationKey)

@given(instance=ConversationLink_strategy)
@settings(max_examples=50)
def test_conversationlink_instantiation(instance):
    assert isinstance(instance, ConversationLink)

@given(instance=choreographyactivities_ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_choreographyactivities_choreographyactivity_instantiation(instance):
    assert isinstance(instance, choreographyactivities_ChoreographyActivity)

@given(instance=Conversation_strategy)
@settings(max_examples=50)
def test_conversation_instantiation(instance):
    assert isinstance(instance, Conversation)

@given(instance=events_ConditionalEventDefinition_strategy)
@settings(max_examples=50)
def test_events_conditionaleventdefinition_instantiation(instance):
    assert isinstance(instance, events_ConditionalEventDefinition)

@given(instance=gateways_ComplexGateway_strategy)
@settings(max_examples=50)
def test_gateways_complexgateway_instantiation(instance):
    assert isinstance(instance, gateways_ComplexGateway)

@given(instance=ComplexBehaviorDefinition_strategy)
@settings(max_examples=50)
def test_complexbehaviordefinition_instantiation(instance):
    assert isinstance(instance, ComplexBehaviorDefinition)

@given(instance=events_CompensateEventDefinition_strategy)
@settings(max_examples=50)
def test_events_compensateeventdefinition_instantiation(instance):
    assert isinstance(instance, events_CompensateEventDefinition)

@given(instance=choreographyactivities_ChoreographyTask_strategy)
@settings(max_examples=50)
def test_choreographyactivities_choreographytask_instantiation(instance):
    assert isinstance(instance, choreographyactivities_ChoreographyTask)

@given(instance=events_EventDefinition_strategy)
@settings(max_examples=50)
def test_events_eventdefinition_instantiation(instance):
    assert isinstance(instance, events_EventDefinition)

@given(instance=Collaboration_strategy)
@settings(max_examples=50)
def test_collaboration_instantiation(instance):
    assert isinstance(instance, Collaboration)

@given(instance=Choreography_strategy)
@settings(max_examples=50)
def test_choreography_instantiation(instance):
    assert isinstance(instance, Choreography)

@given(instance=artifacts_CategoryValue_strategy)
@settings(max_examples=50)
def test_artifacts_categoryvalue_instantiation(instance):
    assert isinstance(instance, artifacts_CategoryValue)

@given(instance=artifacts_Category_strategy)
@settings(max_examples=50)
def test_artifacts_category_instantiation(instance):
    assert isinstance(instance, artifacts_Category)

@given(instance=events_CatchEvent_strategy)
@settings(max_examples=50)
def test_events_catchevent_instantiation(instance):
    assert isinstance(instance, events_CatchEvent)

@given(instance=RootElement_strategy)
@settings(max_examples=50)
def test_rootelement_instantiation(instance):
    assert isinstance(instance, RootElement)

@given(instance=events_CancelEventDefinition_strategy)
@settings(max_examples=50)
def test_events_canceleventdefinition_instantiation(instance):
    assert isinstance(instance, events_CancelEventDefinition)

@given(instance=ConversationNode_strategy)
@settings(max_examples=50)
def test_conversationnode_instantiation(instance):
    assert isinstance(instance, ConversationNode)

@given(instance=CallConversation_strategy)
@settings(max_examples=50)
def test_callconversation_instantiation(instance):
    assert isinstance(instance, CallConversation)

@given(instance=choreographyactivities_CallChoreography_strategy)
@settings(max_examples=50)
def test_choreographyactivities_callchoreography_instantiation(instance):
    assert isinstance(instance, choreographyactivities_CallChoreography)

@given(instance=CallActivity_strategy)
@settings(max_examples=50)
def test_callactivity_instantiation(instance):
    assert isinstance(instance, CallActivity)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=BusinessRuleTask_strategy)
@settings(max_examples=50)
def test_businessruletask_instantiation(instance):
    assert isinstance(instance, BusinessRuleTask)

@given(instance=events_BoundaryEvent_strategy)
@settings(max_examples=50)
def test_events_boundaryevent_instantiation(instance):
    assert isinstance(instance, events_BoundaryEvent)

@given(instance=BaseElement_strategy)
@settings(max_examples=50)
def test_baseelement_instantiation(instance):
    assert isinstance(instance, BaseElement)

@given(instance=Auditing_strategy)
@settings(max_examples=50)
def test_auditing_instantiation(instance):
    assert isinstance(instance, Auditing)

@given(instance=artifacts_Association_strategy)
@settings(max_examples=50)
def test_artifacts_association_instantiation(instance):
    assert isinstance(instance, artifacts_Association)

@given(instance=bpmn2_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_bpmn2_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, bpmn2_EStringToStringMapEntry)

@given(instance=artifacts_Artifact_strategy)
@settings(max_examples=50)
def test_artifacts_artifact_instantiation(instance):
    assert isinstance(instance, artifacts_Artifact)

@given(instance=flows_FlowElement_strategy)
@settings(max_examples=50)
def test_flows_flowelement_instantiation(instance):
    assert isinstance(instance, flows_FlowElement)

@given(instance=AdHocSubProcess_strategy)
@settings(max_examples=50)
def test_adhocsubprocess_instantiation(instance):
    assert isinstance(instance, AdHocSubProcess)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=bpmn2_DocumentRoot_strategy)
@settings(max_examples=50)
def test_bpmn2_documentroot_instantiation(instance):
    assert isinstance(instance, bpmn2_DocumentRoot)



@given(instance=bpmn2_DocumentRoot_strategy)
def test_bpmn2_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=UserTask_strategy)
@settings(max_examples=50)
def test_usertask_instantiation(instance):
    assert isinstance(instance, UserTask)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)

@given(instance=events_TimerEventDefinition_strategy)
@settings(max_examples=50)
def test_events_timereventdefinition_instantiation(instance):
    assert isinstance(instance, events_TimerEventDefinition)

@given(instance=events_ThrowEvent_strategy)
@settings(max_examples=50)
def test_events_throwevent_instantiation(instance):
    assert isinstance(instance, events_ThrowEvent)

@given(instance=artifacts_TextAnnotation_strategy)
@settings(max_examples=50)
def test_artifacts_textannotation_instantiation(instance):
    assert isinstance(instance, artifacts_TextAnnotation)

@given(instance=events_TerminateEventDefinition_strategy)
@settings(max_examples=50)
def test_events_terminateeventdefinition_instantiation(instance):
    assert isinstance(instance, events_TerminateEventDefinition)

@given(instance=events_StartEvent_strategy)
@settings(max_examples=50)
def test_events_startevent_instantiation(instance):
    assert isinstance(instance, events_StartEvent)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=SubProcess_strategy)
@settings(max_examples=50)
def test_subprocess_instantiation(instance):
    assert isinstance(instance, SubProcess)

@given(instance=SubConversation_strategy)
@settings(max_examples=50)
def test_subconversation_instantiation(instance):
    assert isinstance(instance, SubConversation)

@given(instance=choreographyactivities_SubChoreography_strategy)
@settings(max_examples=50)
def test_choreographyactivities_subchoreography_instantiation(instance):
    assert isinstance(instance, choreographyactivities_SubChoreography)

@given(instance=StandardLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_standardloopcharacteristics_instantiation(instance):
    assert isinstance(instance, StandardLoopCharacteristics)

@given(instance=events_SignalEventDefinition_strategy)
@settings(max_examples=50)
def test_events_signaleventdefinition_instantiation(instance):
    assert isinstance(instance, events_SignalEventDefinition)

@given(instance=events_Signal_strategy)
@settings(max_examples=50)
def test_events_signal_instantiation(instance):
    assert isinstance(instance, events_Signal)

@given(instance=ServiceTask_strategy)
@settings(max_examples=50)
def test_servicetask_instantiation(instance):
    assert isinstance(instance, ServiceTask)

@given(instance=ResourceParameter_strategy)
@settings(max_examples=50)
def test_resourceparameter_instantiation(instance):
    assert isinstance(instance, ResourceParameter)

@given(instance=flows_SequenceFlow_strategy)
@settings(max_examples=50)
def test_flows_sequenceflow_instantiation(instance):
    assert isinstance(instance, flows_SequenceFlow)

@given(instance=SendTask_strategy)
@settings(max_examples=50)
def test_sendtask_instantiation(instance):
    assert isinstance(instance, SendTask)

@given(instance=ScriptTask_strategy)
@settings(max_examples=50)
def test_scripttask_instantiation(instance):
    assert isinstance(instance, ScriptTask)

@given(instance=bpmn2_EObject_strategy)
@settings(max_examples=50)
def test_bpmn2_eobject_instantiation(instance):
    assert isinstance(instance, bpmn2_EObject)

@given(instance=ResourceParameterBinding_strategy)
@settings(max_examples=50)
def test_resourceparameterbinding_instantiation(instance):
    assert isinstance(instance, ResourceParameterBinding)

@given(instance=ReceiveTask_strategy)
@settings(max_examples=50)
def test_receivetask_instantiation(instance):
    assert isinstance(instance, ReceiveTask)

@given(instance=ResourceAssignmentExpression_strategy)
@settings(max_examples=50)
def test_resourceassignmentexpression_instantiation(instance):
    assert isinstance(instance, ResourceAssignmentExpression)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=Rendering_strategy)
@settings(max_examples=50)
def test_rendering_instantiation(instance):
    assert isinstance(instance, Rendering)
