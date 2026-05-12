import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ThrowEvent,
    FlowElement,
    DataAssociation,
    ItemAwareElement,
    InteractionNode,
    Gateway,
    FlowElementsContainer,
    Collaboration,
    Event,
    EventDefinition,
    RootElement,
    ConversationNode,
    ChoreographyActivity,
    Activity,
    Task,
    CatchEvent,
    Artifact,
    BaseElement,
    BPMN2Model_FlowElementsContainer,
    BPMN2Model_ItemAwareElement,
    SubProcess,
    BPMN2Model_ThrowEvent,
    FlowNode,
    BPMN2Model_UserTask,
    BPMN2Model_Transaction,
    BPMN2Model_TimerEventDefinition,
    BPMN2Model_StartEvent,
    BPMN2Model_TextAnnotation,
    BPMN2Model_TerminateEventDefinition,
    BPMN2Model_Task,
    BPMN2Model_SubProcess,
    BPMN2Model_SubConversation,
    BPMN2Model_SubChoreography,
    BPMN2Model_EObject,
    BPMN2Model_SignalEventDefinition,
    BPMN2Model_Signal,
    BPMN2Model_ServiceTask,
    BPMN2Model_SequenceFlow,
    BPMN2Model_SendTask,
    BPMN2Model_ScriptTask,
    BPMN2Model_ResourceParameter,
    BPMN2Model_Resource,
    BPMN2Model_Rendering,
    BPMN2Model_Relationship,
    BPMN2Model_ReceiveTask,
    BPMN2Model_Property,
    BPMN2Model_PartnerRole,
    BPMN2Model_PartnerEntity,
    BPMN2Model_MessageEventDefinition,
    BPMN2Model_ParticipantAssociation,
    BPMN2Model_Participant,
    BPMN2Model_ParallelGateway,
    BPMN2Model_OutputSet,
    BPMN2Model_Operation,
    BPMN2Model_Monitoring,
    BPMN2Model_MessageFlowAssociation,
    BPMN2Model_MessageFlow,
    BPMN2Model_IntermediateCatchEvent,
    BPMN2Model_Message,
    BPMN2Model_ManualTask,
    BPMN2Model_LoopCharacteristics,
    BPMN2Model_LinkEventDefinition,
    BPMN2Model_LaneSet,
    BPMN2Model_Lane,
    BPMN2Model_ItemDefinition,
    BPMN2Model_InputOutputSpecification,
    BPMN2Model_IntermediateThrowEvent,
    BPMN2Model_Interface,
    BPMN2Model_InputSet,
    BPMN2Model_InclusiveGateway,
    BPMN2Model_ImplicitThrowEvent,
    BPMN2Model_ResourceRole,
    BPMN2Model_Group,
    BPMN2Model_ExclusiveGateway,
    BPMN2Model_GlobalConversation,
    BPMN2Model_Gateway,
    BPMN2Model_FlowNode,
    BPMN2Model_Expression,
    BPMN2Model_DataOutputAssociation,
    BPMN2Model_EventBasedGateway,
    BPMN2Model_Event,
    BPMN2Model_EscalationEventDefinition,
    BPMN2Model_ErrorEventDefinition,
    BPMN2Model_Error,
    BPMN2Model_EndPoint,
    BPMN2Model_EndEvent,
    BPMN2Model_Documentation,
    BPMN2Model_Definitions,
    BPMN2Model_DataStoreReference,
    BPMN2Model_DataStore,
    BPMN2Model_DataState,
    BPMN2Model_ConversationAssociation,
    BPMN2Model_Conversation,
    BPMN2Model_DataOutput,
    BPMN2Model_DataObjectReference,
    BPMN2Model_DataObject,
    BPMN2Model_DataInputAssociation,
    BPMN2Model_DataInput,
    BPMN2Model_DataAssociation,
    BPMN2Model_CorrelationSubscription,
    BPMN2Model_CorrelationPropertyRetrievalExpression,
    BPMN2Model_CorrelationPropertyBinding,
    BPMN2Model_CorrelationProperty,
    BPMN2Model_CorrelationKey,
    BPMN2Model_ConversationLink,
    BPMN2Model_RootElement,
    BPMN2Model_EventDefinition,
    BPMN2Model_ConditionalEventDefinition,
    BPMN2Model_ComplexGateway,
    BPMN2Model_ComplexBehaviorDefinition,
    BPMN2Model_CompensateEventDefinition,
    BPMN2Model_ChoreographyTask,
    BPMN2Model_ChoreographyActivity,
    BPMN2Model_Collaboration,
    BPMN2Model_Choreography,
    BPMN2Model_CategoryValue,
    BPMN2Model_Category,
    BPMN2Model_CatchEvent,
    BPMN2Model_FlowElement,
    BPMN2Model_AdHocSubProcess,
    BPMN2Model_CancelEventDefinition,
    BPMN2Model_ConversationNode,
    BPMN2Model_CallConversation,
    BPMN2Model_CallChoreography,
    BPMN2Model_CallActivity,
    BPMN2Model_CallableElement,
    BPMN2Model_BusinessRuleTask,
    BPMN2Model_BoundaryEvent,
    BPMN2Model_Auditing,
    BPMN2Model_Association,
    BPMN2Model_Assignment,
    BPMN2Model_Artifact,
    BPMN2Model_Activity,
    BPMN2Model_EStringToStringMapEntry,
    BPMNBase,
    BPMN2Model_InteractionNode,
    BPMN2Model_Escalation,
    BPMN2Model_ResourceAssignmentExpression,
    BPMN2Model_ExtensionDefinition,
    BPMN2Model_ResourceParameterBinding,
    BPMN2Model_ExtensionAttributeDefinition,
    BPMN2Model_ExtensionAttributeValue,
    BPMN2Model_BaseElement,
    BPMN2Model_Extension,
    BPMN2Model_InputOutputBinding,
    BPMN2Model_ParticipantMultiplicity,
    BPMN2Model_Import,
    BPMN2Model_DocumentRoot,
    EObject,
    BPMN2Model_BPMNBase,
    HumanPerformer,
    BPMN2Model_PotentialOwner,
    ResourceRole,
    BPMN2Model_Performer,
    LoopCharacteristics,
    BPMN2Model_StandardLoopCharacteristics,
    BPMN2Model_MultiInstanceLoopCharacteristics,
    Performer,
    BPMN2Model_HumanPerformer,
    CallableElement,
    BPMN2Model_Process,
    BPMN2Model_GlobalTask,
    Choreography,
    BPMN2Model_GlobalChoreographyTask,
    GlobalTask,
    BPMN2Model_GlobalScriptTask,
    BPMN2Model_GlobalBusinessRuleTask,
    BPMN2Model_GlobalUserTask,
    BPMN2Model_GlobalManualTask,
    Expression,
    BPMN2Model_FormalExpression,
    MultiInstanceBehavior,
    GatewayDirection,
    ItemKind,
    AssociationDirection,
    AdHocOrdering,
    ChoreographyLoopType,
    ProcessType,
    EventBasedGatewayType,
    RelationshipDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_throwevent_is_not_abstract():
    assert not inspect.isabstract(ThrowEvent)


def test_throwevent_constructor_exists():
    assert callable(ThrowEvent.__init__)


def test_throwevent_constructor_args():
    sig = inspect.signature(ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_dataassociation_is_not_abstract():
    assert not inspect.isabstract(DataAssociation)


def test_dataassociation_constructor_exists():
    assert callable(DataAssociation.__init__)


def test_dataassociation_constructor_args():
    sig = inspect.signature(DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(ItemAwareElement)


def test_itemawareelement_constructor_exists():
    assert callable(ItemAwareElement.__init__)


def test_itemawareelement_constructor_args():
    sig = inspect.signature(ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_interactionnode_is_not_abstract():
    assert not inspect.isabstract(InteractionNode)


def test_interactionnode_constructor_exists():
    assert callable(InteractionNode.__init__)


def test_interactionnode_constructor_args():
    sig = inspect.signature(InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_gateway_is_not_abstract():
    assert not inspect.isabstract(Gateway)


def test_gateway_constructor_exists():
    assert callable(Gateway.__init__)


def test_gateway_constructor_args():
    sig = inspect.signature(Gateway.__init__)
    params = list(sig.parameters.keys())



def test_flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(FlowElementsContainer)


def test_flowelementscontainer_constructor_exists():
    assert callable(FlowElementsContainer.__init__)


def test_flowelementscontainer_constructor_args():
    sig = inspect.signature(FlowElementsContainer.__init__)
    params = list(sig.parameters.keys())



def test_collaboration_is_not_abstract():
    assert not inspect.isabstract(Collaboration)


def test_collaboration_constructor_exists():
    assert callable(Collaboration.__init__)


def test_collaboration_constructor_args():
    sig = inspect.signature(Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(EventDefinition)


def test_eventdefinition_constructor_exists():
    assert callable(EventDefinition.__init__)


def test_eventdefinition_constructor_args():
    sig = inspect.signature(EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rootelement_is_not_abstract():
    assert not inspect.isabstract(RootElement)


def test_rootelement_constructor_exists():
    assert callable(RootElement.__init__)


def test_rootelement_constructor_args():
    sig = inspect.signature(RootElement.__init__)
    params = list(sig.parameters.keys())



def test_conversationnode_is_not_abstract():
    assert not inspect.isabstract(ConversationNode)


def test_conversationnode_constructor_exists():
    assert callable(ConversationNode.__init__)


def test_conversationnode_constructor_args():
    sig = inspect.signature(ConversationNode.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(ChoreographyActivity)


def test_choreographyactivity_constructor_exists():
    assert callable(ChoreographyActivity.__init__)


def test_choreographyactivity_constructor_args():
    sig = inspect.signature(ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_catchevent_is_not_abstract():
    assert not inspect.isabstract(CatchEvent)


def test_catchevent_constructor_exists():
    assert callable(CatchEvent.__init__)


def test_catchevent_constructor_args():
    sig = inspect.signature(CatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_baseelement_is_not_abstract():
    assert not inspect.isabstract(BaseElement)


def test_baseelement_constructor_exists():
    assert callable(BaseElement.__init__)


def test_baseelement_constructor_args():
    sig = inspect.signature(BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_FlowElementsContainer)


def test_bpmn2model_flowelementscontainer_constructor_exists():
    assert callable(BPMN2Model_FlowElementsContainer.__init__)


def test_bpmn2model_flowelementscontainer_constructor_args():
    sig = inspect.signature(BPMN2Model_FlowElementsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ItemAwareElement)


def test_bpmn2model_itemawareelement_constructor_exists():
    assert callable(BPMN2Model_ItemAwareElement.__init__)


def test_bpmn2model_itemawareelement_constructor_args():
    sig = inspect.signature(BPMN2Model_ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_subprocess_is_not_abstract():
    assert not inspect.isabstract(SubProcess)


def test_subprocess_constructor_exists():
    assert callable(SubProcess.__init__)


def test_subprocess_constructor_args():
    sig = inspect.signature(SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_throwevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ThrowEvent)


def test_bpmn2model_throwevent_constructor_exists():
    assert callable(BPMN2Model_ThrowEvent.__init__)


def test_bpmn2model_throwevent_constructor_args():
    sig = inspect.signature(BPMN2Model_ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_flownode_is_not_abstract():
    assert not inspect.isabstract(FlowNode)


def test_flownode_constructor_exists():
    assert callable(FlowNode.__init__)


def test_flownode_constructor_args():
    sig = inspect.signature(FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_usertask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_UserTask)


def test_bpmn2model_usertask_constructor_exists():
    assert callable(BPMN2Model_UserTask.__init__)


def test_bpmn2model_usertask_constructor_args():
    sig = inspect.signature(BPMN2Model_UserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_usertask_has_implementation():
    assert hasattr(BPMN2Model_UserTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_UserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_transaction_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Transaction)


def test_bpmn2model_transaction_constructor_exists():
    assert callable(BPMN2Model_Transaction.__init__)


def test_bpmn2model_transaction_constructor_args():
    sig = inspect.signature(BPMN2Model_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "protocol" in params, "Missing parameter 'protocol'"

def test_bpmn2model_transaction_has_method():
    assert hasattr(BPMN2Model_Transaction, "method")
    descriptor = None
    for klass in BPMN2Model_Transaction.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_transaction_has_protocol():
    assert hasattr(BPMN2Model_Transaction, "protocol")
    descriptor = None
    for klass in BPMN2Model_Transaction.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_timereventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_TimerEventDefinition)


def test_bpmn2model_timereventdefinition_constructor_exists():
    assert callable(BPMN2Model_TimerEventDefinition.__init__)


def test_bpmn2model_timereventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_TimerEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_startevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_StartEvent)


def test_bpmn2model_startevent_constructor_exists():
    assert callable(BPMN2Model_StartEvent.__init__)


def test_bpmn2model_startevent_constructor_args():
    sig = inspect.signature(BPMN2Model_StartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isInterrupting" in params, "Missing parameter 'isInterrupting'"

def test_bpmn2model_startevent_has_isInterrupting():
    assert hasattr(BPMN2Model_StartEvent, "isInterrupting")
    descriptor = None
    for klass in BPMN2Model_StartEvent.__mro__:
        if "isInterrupting" in klass.__dict__:
            descriptor = klass.__dict__["isInterrupting"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_textannotation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_TextAnnotation)


def test_bpmn2model_textannotation_constructor_exists():
    assert callable(BPMN2Model_TextAnnotation.__init__)


def test_bpmn2model_textannotation_constructor_args():
    sig = inspect.signature(BPMN2Model_TextAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "textFormat" in params, "Missing parameter 'textFormat'"

def test_bpmn2model_textannotation_has_text():
    assert hasattr(BPMN2Model_TextAnnotation, "text")
    descriptor = None
    for klass in BPMN2Model_TextAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_textannotation_has_textFormat():
    assert hasattr(BPMN2Model_TextAnnotation, "textFormat")
    descriptor = None
    for klass in BPMN2Model_TextAnnotation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_terminateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_TerminateEventDefinition)


def test_bpmn2model_terminateeventdefinition_constructor_exists():
    assert callable(BPMN2Model_TerminateEventDefinition.__init__)


def test_bpmn2model_terminateeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_TerminateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_task_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Task)


def test_bpmn2model_task_constructor_exists():
    assert callable(BPMN2Model_Task.__init__)


def test_bpmn2model_task_constructor_args():
    sig = inspect.signature(BPMN2Model_Task.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_subprocess_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SubProcess)


def test_bpmn2model_subprocess_constructor_exists():
    assert callable(BPMN2Model_SubProcess.__init__)


def test_bpmn2model_subprocess_constructor_args():
    sig = inspect.signature(BPMN2Model_SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "triggeredByEvent" in params, "Missing parameter 'triggeredByEvent'"

def test_bpmn2model_subprocess_has_triggeredByEvent():
    assert hasattr(BPMN2Model_SubProcess, "triggeredByEvent")
    descriptor = None
    for klass in BPMN2Model_SubProcess.__mro__:
        if "triggeredByEvent" in klass.__dict__:
            descriptor = klass.__dict__["triggeredByEvent"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_subconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SubConversation)


def test_bpmn2model_subconversation_constructor_exists():
    assert callable(BPMN2Model_SubConversation.__init__)


def test_bpmn2model_subconversation_constructor_args():
    sig = inspect.signature(BPMN2Model_SubConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_subchoreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SubChoreography)


def test_bpmn2model_subchoreography_constructor_exists():
    assert callable(BPMN2Model_SubChoreography.__init__)


def test_bpmn2model_subchoreography_constructor_args():
    sig = inspect.signature(BPMN2Model_SubChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_eobject_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EObject)


def test_bpmn2model_eobject_constructor_exists():
    assert callable(BPMN2Model_EObject.__init__)


def test_bpmn2model_eobject_constructor_args():
    sig = inspect.signature(BPMN2Model_EObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_signaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SignalEventDefinition)


def test_bpmn2model_signaleventdefinition_constructor_exists():
    assert callable(BPMN2Model_SignalEventDefinition.__init__)


def test_bpmn2model_signaleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_SignalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_signal_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Signal)


def test_bpmn2model_signal_constructor_exists():
    assert callable(BPMN2Model_Signal.__init__)


def test_bpmn2model_signal_constructor_args():
    sig = inspect.signature(BPMN2Model_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_signal_has_name():
    assert hasattr(BPMN2Model_Signal, "name")
    descriptor = None
    for klass in BPMN2Model_Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_servicetask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ServiceTask)


def test_bpmn2model_servicetask_constructor_exists():
    assert callable(BPMN2Model_ServiceTask.__init__)


def test_bpmn2model_servicetask_constructor_args():
    sig = inspect.signature(BPMN2Model_ServiceTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_servicetask_has_implementation():
    assert hasattr(BPMN2Model_ServiceTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_ServiceTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_sequenceflow_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SequenceFlow)


def test_bpmn2model_sequenceflow_constructor_exists():
    assert callable(BPMN2Model_SequenceFlow.__init__)


def test_bpmn2model_sequenceflow_constructor_args():
    sig = inspect.signature(BPMN2Model_SequenceFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"

def test_bpmn2model_sequenceflow_has_isImmediate():
    assert hasattr(BPMN2Model_SequenceFlow, "isImmediate")
    descriptor = None
    for klass in BPMN2Model_SequenceFlow.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_sendtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_SendTask)


def test_bpmn2model_sendtask_constructor_exists():
    assert callable(BPMN2Model_SendTask.__init__)


def test_bpmn2model_sendtask_constructor_args():
    sig = inspect.signature(BPMN2Model_SendTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_sendtask_has_implementation():
    assert hasattr(BPMN2Model_SendTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_SendTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_scripttask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ScriptTask)


def test_bpmn2model_scripttask_constructor_exists():
    assert callable(BPMN2Model_ScriptTask.__init__)


def test_bpmn2model_scripttask_constructor_args():
    sig = inspect.signature(BPMN2Model_ScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"
    assert "scriptFormat" in params, "Missing parameter 'scriptFormat'"

def test_bpmn2model_scripttask_has_script():
    assert hasattr(BPMN2Model_ScriptTask, "script")
    descriptor = None
    for klass in BPMN2Model_ScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_scripttask_has_scriptFormat():
    assert hasattr(BPMN2Model_ScriptTask, "scriptFormat")
    descriptor = None
    for klass in BPMN2Model_ScriptTask.__mro__:
        if "scriptFormat" in klass.__dict__:
            descriptor = klass.__dict__["scriptFormat"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_resourceparameter_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ResourceParameter)


def test_bpmn2model_resourceparameter_constructor_exists():
    assert callable(BPMN2Model_ResourceParameter.__init__)


def test_bpmn2model_resourceparameter_constructor_args():
    sig = inspect.signature(BPMN2Model_ResourceParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_bpmn2model_resourceparameter_has_name():
    assert hasattr(BPMN2Model_ResourceParameter, "name")
    descriptor = None
    for klass in BPMN2Model_ResourceParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_resourceparameter_has_isRequired():
    assert hasattr(BPMN2Model_ResourceParameter, "isRequired")
    descriptor = None
    for klass in BPMN2Model_ResourceParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_resource_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Resource)


def test_bpmn2model_resource_constructor_exists():
    assert callable(BPMN2Model_Resource.__init__)


def test_bpmn2model_resource_constructor_args():
    sig = inspect.signature(BPMN2Model_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_resource_has_name():
    assert hasattr(BPMN2Model_Resource, "name")
    descriptor = None
    for klass in BPMN2Model_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_rendering_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Rendering)


def test_bpmn2model_rendering_constructor_exists():
    assert callable(BPMN2Model_Rendering.__init__)


def test_bpmn2model_rendering_constructor_args():
    sig = inspect.signature(BPMN2Model_Rendering.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_relationship_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Relationship)


def test_bpmn2model_relationship_constructor_exists():
    assert callable(BPMN2Model_Relationship.__init__)


def test_bpmn2model_relationship_constructor_args():
    sig = inspect.signature(BPMN2Model_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_bpmn2model_relationship_has_type():
    assert hasattr(BPMN2Model_Relationship, "type")
    descriptor = None
    for klass in BPMN2Model_Relationship.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_relationship_has_direction():
    assert hasattr(BPMN2Model_Relationship, "direction")
    descriptor = None
    for klass in BPMN2Model_Relationship.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_receivetask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ReceiveTask)


def test_bpmn2model_receivetask_constructor_exists():
    assert callable(BPMN2Model_ReceiveTask.__init__)


def test_bpmn2model_receivetask_constructor_args():
    sig = inspect.signature(BPMN2Model_ReceiveTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "instantiate" in params, "Missing parameter 'instantiate'"

def test_bpmn2model_receivetask_has_implementation():
    assert hasattr(BPMN2Model_ReceiveTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_ReceiveTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_receivetask_has_instantiate():
    assert hasattr(BPMN2Model_ReceiveTask, "instantiate")
    descriptor = None
    for klass in BPMN2Model_ReceiveTask.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_property_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Property)


def test_bpmn2model_property_constructor_exists():
    assert callable(BPMN2Model_Property.__init__)


def test_bpmn2model_property_constructor_args():
    sig = inspect.signature(BPMN2Model_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_property_has_name():
    assert hasattr(BPMN2Model_Property, "name")
    descriptor = None
    for klass in BPMN2Model_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_partnerrole_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_PartnerRole)


def test_bpmn2model_partnerrole_constructor_exists():
    assert callable(BPMN2Model_PartnerRole.__init__)


def test_bpmn2model_partnerrole_constructor_args():
    sig = inspect.signature(BPMN2Model_PartnerRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_partnerrole_has_name():
    assert hasattr(BPMN2Model_PartnerRole, "name")
    descriptor = None
    for klass in BPMN2Model_PartnerRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_partnerentity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_PartnerEntity)


def test_bpmn2model_partnerentity_constructor_exists():
    assert callable(BPMN2Model_PartnerEntity.__init__)


def test_bpmn2model_partnerentity_constructor_args():
    sig = inspect.signature(BPMN2Model_PartnerEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_partnerentity_has_name():
    assert hasattr(BPMN2Model_PartnerEntity, "name")
    descriptor = None
    for klass in BPMN2Model_PartnerEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_messageeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_MessageEventDefinition)


def test_bpmn2model_messageeventdefinition_constructor_exists():
    assert callable(BPMN2Model_MessageEventDefinition.__init__)


def test_bpmn2model_messageeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_MessageEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_participantassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ParticipantAssociation)


def test_bpmn2model_participantassociation_constructor_exists():
    assert callable(BPMN2Model_ParticipantAssociation.__init__)


def test_bpmn2model_participantassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_ParticipantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_participant_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Participant)


def test_bpmn2model_participant_constructor_exists():
    assert callable(BPMN2Model_Participant.__init__)


def test_bpmn2model_participant_constructor_args():
    sig = inspect.signature(BPMN2Model_Participant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_participant_has_name():
    assert hasattr(BPMN2Model_Participant, "name")
    descriptor = None
    for klass in BPMN2Model_Participant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_parallelgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ParallelGateway)


def test_bpmn2model_parallelgateway_constructor_exists():
    assert callable(BPMN2Model_ParallelGateway.__init__)


def test_bpmn2model_parallelgateway_constructor_args():
    sig = inspect.signature(BPMN2Model_ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_outputset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_OutputSet)


def test_bpmn2model_outputset_constructor_exists():
    assert callable(BPMN2Model_OutputSet.__init__)


def test_bpmn2model_outputset_constructor_args():
    sig = inspect.signature(BPMN2Model_OutputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_outputset_has_name():
    assert hasattr(BPMN2Model_OutputSet, "name")
    descriptor = None
    for klass in BPMN2Model_OutputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_operation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Operation)


def test_bpmn2model_operation_constructor_exists():
    assert callable(BPMN2Model_Operation.__init__)


def test_bpmn2model_operation_constructor_args():
    sig = inspect.signature(BPMN2Model_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_operation_has_name():
    assert hasattr(BPMN2Model_Operation, "name")
    descriptor = None
    for klass in BPMN2Model_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_monitoring_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Monitoring)


def test_bpmn2model_monitoring_constructor_exists():
    assert callable(BPMN2Model_Monitoring.__init__)


def test_bpmn2model_monitoring_constructor_args():
    sig = inspect.signature(BPMN2Model_Monitoring.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_messageflowassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_MessageFlowAssociation)


def test_bpmn2model_messageflowassociation_constructor_exists():
    assert callable(BPMN2Model_MessageFlowAssociation.__init__)


def test_bpmn2model_messageflowassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_MessageFlowAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_messageflow_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_MessageFlow)


def test_bpmn2model_messageflow_constructor_exists():
    assert callable(BPMN2Model_MessageFlow.__init__)


def test_bpmn2model_messageflow_constructor_args():
    sig = inspect.signature(BPMN2Model_MessageFlow.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_messageflow_has_name():
    assert hasattr(BPMN2Model_MessageFlow, "name")
    descriptor = None
    for klass in BPMN2Model_MessageFlow.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_intermediatecatchevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_IntermediateCatchEvent)


def test_bpmn2model_intermediatecatchevent_constructor_exists():
    assert callable(BPMN2Model_IntermediateCatchEvent.__init__)


def test_bpmn2model_intermediatecatchevent_constructor_args():
    sig = inspect.signature(BPMN2Model_IntermediateCatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_message_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Message)


def test_bpmn2model_message_constructor_exists():
    assert callable(BPMN2Model_Message.__init__)


def test_bpmn2model_message_constructor_args():
    sig = inspect.signature(BPMN2Model_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_message_has_name():
    assert hasattr(BPMN2Model_Message, "name")
    descriptor = None
    for klass in BPMN2Model_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_manualtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ManualTask)


def test_bpmn2model_manualtask_constructor_exists():
    assert callable(BPMN2Model_ManualTask.__init__)


def test_bpmn2model_manualtask_constructor_args():
    sig = inspect.signature(BPMN2Model_ManualTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_LoopCharacteristics)


def test_bpmn2model_loopcharacteristics_constructor_exists():
    assert callable(BPMN2Model_LoopCharacteristics.__init__)


def test_bpmn2model_loopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model_LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_linkeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_LinkEventDefinition)


def test_bpmn2model_linkeventdefinition_constructor_exists():
    assert callable(BPMN2Model_LinkEventDefinition.__init__)


def test_bpmn2model_linkeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_LinkEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_linkeventdefinition_has_name():
    assert hasattr(BPMN2Model_LinkEventDefinition, "name")
    descriptor = None
    for klass in BPMN2Model_LinkEventDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_laneset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_LaneSet)


def test_bpmn2model_laneset_constructor_exists():
    assert callable(BPMN2Model_LaneSet.__init__)


def test_bpmn2model_laneset_constructor_args():
    sig = inspect.signature(BPMN2Model_LaneSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_laneset_has_name():
    assert hasattr(BPMN2Model_LaneSet, "name")
    descriptor = None
    for klass in BPMN2Model_LaneSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_lane_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Lane)


def test_bpmn2model_lane_constructor_exists():
    assert callable(BPMN2Model_Lane.__init__)


def test_bpmn2model_lane_constructor_args():
    sig = inspect.signature(BPMN2Model_Lane.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_lane_has_name():
    assert hasattr(BPMN2Model_Lane, "name")
    descriptor = None
    for klass in BPMN2Model_Lane.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_itemdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ItemDefinition)


def test_bpmn2model_itemdefinition_constructor_exists():
    assert callable(BPMN2Model_ItemDefinition.__init__)


def test_bpmn2model_itemdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ItemDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "itemKind" in params, "Missing parameter 'itemKind'"
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2model_itemdefinition_has_itemKind():
    assert hasattr(BPMN2Model_ItemDefinition, "itemKind")
    descriptor = None
    for klass in BPMN2Model_ItemDefinition.__mro__:
        if "itemKind" in klass.__dict__:
            descriptor = klass.__dict__["itemKind"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_itemdefinition_has_isCollection():
    assert hasattr(BPMN2Model_ItemDefinition, "isCollection")
    descriptor = None
    for klass in BPMN2Model_ItemDefinition.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_inputoutputspecification_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_InputOutputSpecification)


def test_bpmn2model_inputoutputspecification_constructor_exists():
    assert callable(BPMN2Model_InputOutputSpecification.__init__)


def test_bpmn2model_inputoutputspecification_constructor_args():
    sig = inspect.signature(BPMN2Model_InputOutputSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_intermediatethrowevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_IntermediateThrowEvent)


def test_bpmn2model_intermediatethrowevent_constructor_exists():
    assert callable(BPMN2Model_IntermediateThrowEvent.__init__)


def test_bpmn2model_intermediatethrowevent_constructor_args():
    sig = inspect.signature(BPMN2Model_IntermediateThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_interface_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Interface)


def test_bpmn2model_interface_constructor_exists():
    assert callable(BPMN2Model_Interface.__init__)


def test_bpmn2model_interface_constructor_args():
    sig = inspect.signature(BPMN2Model_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_interface_has_name():
    assert hasattr(BPMN2Model_Interface, "name")
    descriptor = None
    for klass in BPMN2Model_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_inputset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_InputSet)


def test_bpmn2model_inputset_constructor_exists():
    assert callable(BPMN2Model_InputSet.__init__)


def test_bpmn2model_inputset_constructor_args():
    sig = inspect.signature(BPMN2Model_InputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_inputset_has_name():
    assert hasattr(BPMN2Model_InputSet, "name")
    descriptor = None
    for klass in BPMN2Model_InputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_inclusivegateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_InclusiveGateway)


def test_bpmn2model_inclusivegateway_constructor_exists():
    assert callable(BPMN2Model_InclusiveGateway.__init__)


def test_bpmn2model_inclusivegateway_constructor_args():
    sig = inspect.signature(BPMN2Model_InclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_implicitthrowevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ImplicitThrowEvent)


def test_bpmn2model_implicitthrowevent_constructor_exists():
    assert callable(BPMN2Model_ImplicitThrowEvent.__init__)


def test_bpmn2model_implicitthrowevent_constructor_args():
    sig = inspect.signature(BPMN2Model_ImplicitThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_resourcerole_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ResourceRole)


def test_bpmn2model_resourcerole_constructor_exists():
    assert callable(BPMN2Model_ResourceRole.__init__)


def test_bpmn2model_resourcerole_constructor_args():
    sig = inspect.signature(BPMN2Model_ResourceRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_resourcerole_has_name():
    assert hasattr(BPMN2Model_ResourceRole, "name")
    descriptor = None
    for klass in BPMN2Model_ResourceRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_group_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Group)


def test_bpmn2model_group_constructor_exists():
    assert callable(BPMN2Model_Group.__init__)


def test_bpmn2model_group_constructor_args():
    sig = inspect.signature(BPMN2Model_Group.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_exclusivegateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ExclusiveGateway)


def test_bpmn2model_exclusivegateway_constructor_exists():
    assert callable(BPMN2Model_ExclusiveGateway.__init__)


def test_bpmn2model_exclusivegateway_constructor_args():
    sig = inspect.signature(BPMN2Model_ExclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_globalconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalConversation)


def test_bpmn2model_globalconversation_constructor_exists():
    assert callable(BPMN2Model_GlobalConversation.__init__)


def test_bpmn2model_globalconversation_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_gateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Gateway)


def test_bpmn2model_gateway_constructor_exists():
    assert callable(BPMN2Model_Gateway.__init__)


def test_bpmn2model_gateway_constructor_args():
    sig = inspect.signature(BPMN2Model_Gateway.__init__)
    params = list(sig.parameters.keys())
    assert "gatewayDirection" in params, "Missing parameter 'gatewayDirection'"

def test_bpmn2model_gateway_has_gatewayDirection():
    assert hasattr(BPMN2Model_Gateway, "gatewayDirection")
    descriptor = None
    for klass in BPMN2Model_Gateway.__mro__:
        if "gatewayDirection" in klass.__dict__:
            descriptor = klass.__dict__["gatewayDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_flownode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_FlowNode)


def test_bpmn2model_flownode_constructor_exists():
    assert callable(BPMN2Model_FlowNode.__init__)


def test_bpmn2model_flownode_constructor_args():
    sig = inspect.signature(BPMN2Model_FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_expression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Expression)


def test_bpmn2model_expression_constructor_exists():
    assert callable(BPMN2Model_Expression.__init__)


def test_bpmn2model_expression_constructor_args():
    sig = inspect.signature(BPMN2Model_Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_dataoutputassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataOutputAssociation)


def test_bpmn2model_dataoutputassociation_constructor_exists():
    assert callable(BPMN2Model_DataOutputAssociation.__init__)


def test_bpmn2model_dataoutputassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_DataOutputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_eventbasedgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EventBasedGateway)


def test_bpmn2model_eventbasedgateway_constructor_exists():
    assert callable(BPMN2Model_EventBasedGateway.__init__)


def test_bpmn2model_eventbasedgateway_constructor_args():
    sig = inspect.signature(BPMN2Model_EventBasedGateway.__init__)
    params = list(sig.parameters.keys())
    assert "instantiate" in params, "Missing parameter 'instantiate'"
    assert "eventGatewayType" in params, "Missing parameter 'eventGatewayType'"

def test_bpmn2model_eventbasedgateway_has_instantiate():
    assert hasattr(BPMN2Model_EventBasedGateway, "instantiate")
    descriptor = None
    for klass in BPMN2Model_EventBasedGateway.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_eventbasedgateway_has_eventGatewayType():
    assert hasattr(BPMN2Model_EventBasedGateway, "eventGatewayType")
    descriptor = None
    for klass in BPMN2Model_EventBasedGateway.__mro__:
        if "eventGatewayType" in klass.__dict__:
            descriptor = klass.__dict__["eventGatewayType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_event_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Event)


def test_bpmn2model_event_constructor_exists():
    assert callable(BPMN2Model_Event.__init__)


def test_bpmn2model_event_constructor_args():
    sig = inspect.signature(BPMN2Model_Event.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_escalationeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EscalationEventDefinition)


def test_bpmn2model_escalationeventdefinition_constructor_exists():
    assert callable(BPMN2Model_EscalationEventDefinition.__init__)


def test_bpmn2model_escalationeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_EscalationEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_erroreventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ErrorEventDefinition)


def test_bpmn2model_erroreventdefinition_constructor_exists():
    assert callable(BPMN2Model_ErrorEventDefinition.__init__)


def test_bpmn2model_erroreventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ErrorEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_error_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Error)


def test_bpmn2model_error_constructor_exists():
    assert callable(BPMN2Model_Error.__init__)


def test_bpmn2model_error_constructor_args():
    sig = inspect.signature(BPMN2Model_Error.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_bpmn2model_error_has_name():
    assert hasattr(BPMN2Model_Error, "name")
    descriptor = None
    for klass in BPMN2Model_Error.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_error_has_errorCode():
    assert hasattr(BPMN2Model_Error, "errorCode")
    descriptor = None
    for klass in BPMN2Model_Error.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_endpoint_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EndPoint)


def test_bpmn2model_endpoint_constructor_exists():
    assert callable(BPMN2Model_EndPoint.__init__)


def test_bpmn2model_endpoint_constructor_args():
    sig = inspect.signature(BPMN2Model_EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_endevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EndEvent)


def test_bpmn2model_endevent_constructor_exists():
    assert callable(BPMN2Model_EndEvent.__init__)


def test_bpmn2model_endevent_constructor_args():
    sig = inspect.signature(BPMN2Model_EndEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_documentation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Documentation)


def test_bpmn2model_documentation_constructor_exists():
    assert callable(BPMN2Model_Documentation.__init__)


def test_bpmn2model_documentation_constructor_args():
    sig = inspect.signature(BPMN2Model_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "text" in params, "Missing parameter 'text'"
    assert "textFormat" in params, "Missing parameter 'textFormat'"

def test_bpmn2model_documentation_has_mixed():
    assert hasattr(BPMN2Model_Documentation, "mixed")
    descriptor = None
    for klass in BPMN2Model_Documentation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_documentation_has_text():
    assert hasattr(BPMN2Model_Documentation, "text")
    descriptor = None
    for klass in BPMN2Model_Documentation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_documentation_has_textFormat():
    assert hasattr(BPMN2Model_Documentation, "textFormat")
    descriptor = None
    for klass in BPMN2Model_Documentation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_definitions_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Definitions)


def test_bpmn2model_definitions_constructor_exists():
    assert callable(BPMN2Model_Definitions.__init__)


def test_bpmn2model_definitions_constructor_args():
    sig = inspect.signature(BPMN2Model_Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "exporterVersion" in params, "Missing parameter 'exporterVersion'"
    assert "expressionLanguage" in params, "Missing parameter 'expressionLanguage'"
    assert "exporter" in params, "Missing parameter 'exporter'"
    assert "targetNamespace" in params, "Missing parameter 'targetNamespace'"
    assert "name" in params, "Missing parameter 'name'"
    assert "typeLanguage" in params, "Missing parameter 'typeLanguage'"

def test_bpmn2model_definitions_has_exporterVersion():
    assert hasattr(BPMN2Model_Definitions, "exporterVersion")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "exporterVersion" in klass.__dict__:
            descriptor = klass.__dict__["exporterVersion"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_definitions_has_expressionLanguage():
    assert hasattr(BPMN2Model_Definitions, "expressionLanguage")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "expressionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_definitions_has_exporter():
    assert hasattr(BPMN2Model_Definitions, "exporter")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "exporter" in klass.__dict__:
            descriptor = klass.__dict__["exporter"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_definitions_has_targetNamespace():
    assert hasattr(BPMN2Model_Definitions, "targetNamespace")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "targetNamespace" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_definitions_has_name():
    assert hasattr(BPMN2Model_Definitions, "name")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_definitions_has_typeLanguage():
    assert hasattr(BPMN2Model_Definitions, "typeLanguage")
    descriptor = None
    for klass in BPMN2Model_Definitions.__mro__:
        if "typeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["typeLanguage"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_datastorereference_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataStoreReference)


def test_bpmn2model_datastorereference_constructor_exists():
    assert callable(BPMN2Model_DataStoreReference.__init__)


def test_bpmn2model_datastorereference_constructor_args():
    sig = inspect.signature(BPMN2Model_DataStoreReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_datastore_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataStore)


def test_bpmn2model_datastore_constructor_exists():
    assert callable(BPMN2Model_DataStore.__init__)


def test_bpmn2model_datastore_constructor_args():
    sig = inspect.signature(BPMN2Model_DataStore.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isUnlimited" in params, "Missing parameter 'isUnlimited'"

def test_bpmn2model_datastore_has_capacity():
    assert hasattr(BPMN2Model_DataStore, "capacity")
    descriptor = None
    for klass in BPMN2Model_DataStore.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_datastore_has_name():
    assert hasattr(BPMN2Model_DataStore, "name")
    descriptor = None
    for klass in BPMN2Model_DataStore.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_datastore_has_isUnlimited():
    assert hasattr(BPMN2Model_DataStore, "isUnlimited")
    descriptor = None
    for klass in BPMN2Model_DataStore.__mro__:
        if "isUnlimited" in klass.__dict__:
            descriptor = klass.__dict__["isUnlimited"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_datastate_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataState)


def test_bpmn2model_datastate_constructor_exists():
    assert callable(BPMN2Model_DataState.__init__)


def test_bpmn2model_datastate_constructor_args():
    sig = inspect.signature(BPMN2Model_DataState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_datastate_has_name():
    assert hasattr(BPMN2Model_DataState, "name")
    descriptor = None
    for klass in BPMN2Model_DataState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_conversationassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ConversationAssociation)


def test_bpmn2model_conversationassociation_constructor_exists():
    assert callable(BPMN2Model_ConversationAssociation.__init__)


def test_bpmn2model_conversationassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_ConversationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_conversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Conversation)


def test_bpmn2model_conversation_constructor_exists():
    assert callable(BPMN2Model_Conversation.__init__)


def test_bpmn2model_conversation_constructor_args():
    sig = inspect.signature(BPMN2Model_Conversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_dataoutput_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataOutput)


def test_bpmn2model_dataoutput_constructor_exists():
    assert callable(BPMN2Model_DataOutput.__init__)


def test_bpmn2model_dataoutput_constructor_args():
    sig = inspect.signature(BPMN2Model_DataOutput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_dataoutput_has_isCollection():
    assert hasattr(BPMN2Model_DataOutput, "isCollection")
    descriptor = None
    for klass in BPMN2Model_DataOutput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_dataoutput_has_name():
    assert hasattr(BPMN2Model_DataOutput, "name")
    descriptor = None
    for klass in BPMN2Model_DataOutput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataObjectReference)


def test_bpmn2model_dataobjectreference_constructor_exists():
    assert callable(BPMN2Model_DataObjectReference.__init__)


def test_bpmn2model_dataobjectreference_constructor_args():
    sig = inspect.signature(BPMN2Model_DataObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_dataobject_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataObject)


def test_bpmn2model_dataobject_constructor_exists():
    assert callable(BPMN2Model_DataObject.__init__)


def test_bpmn2model_dataobject_constructor_args():
    sig = inspect.signature(BPMN2Model_DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2model_dataobject_has_isCollection():
    assert hasattr(BPMN2Model_DataObject, "isCollection")
    descriptor = None
    for klass in BPMN2Model_DataObject.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_datainputassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataInputAssociation)


def test_bpmn2model_datainputassociation_constructor_exists():
    assert callable(BPMN2Model_DataInputAssociation.__init__)


def test_bpmn2model_datainputassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_DataInputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_datainput_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataInput)


def test_bpmn2model_datainput_constructor_exists():
    assert callable(BPMN2Model_DataInput.__init__)


def test_bpmn2model_datainput_constructor_args():
    sig = inspect.signature(BPMN2Model_DataInput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_datainput_has_isCollection():
    assert hasattr(BPMN2Model_DataInput, "isCollection")
    descriptor = None
    for klass in BPMN2Model_DataInput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_datainput_has_name():
    assert hasattr(BPMN2Model_DataInput, "name")
    descriptor = None
    for klass in BPMN2Model_DataInput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_dataassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DataAssociation)


def test_bpmn2model_dataassociation_constructor_exists():
    assert callable(BPMN2Model_DataAssociation.__init__)


def test_bpmn2model_dataassociation_constructor_args():
    sig = inspect.signature(BPMN2Model_DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_correlationsubscription_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CorrelationSubscription)


def test_bpmn2model_correlationsubscription_constructor_exists():
    assert callable(BPMN2Model_CorrelationSubscription.__init__)


def test_bpmn2model_correlationsubscription_constructor_args():
    sig = inspect.signature(BPMN2Model_CorrelationSubscription.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_correlationpropertyretrievalexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CorrelationPropertyRetrievalExpression)


def test_bpmn2model_correlationpropertyretrievalexpression_constructor_exists():
    assert callable(BPMN2Model_CorrelationPropertyRetrievalExpression.__init__)


def test_bpmn2model_correlationpropertyretrievalexpression_constructor_args():
    sig = inspect.signature(BPMN2Model_CorrelationPropertyRetrievalExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_correlationpropertybinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CorrelationPropertyBinding)


def test_bpmn2model_correlationpropertybinding_constructor_exists():
    assert callable(BPMN2Model_CorrelationPropertyBinding.__init__)


def test_bpmn2model_correlationpropertybinding_constructor_args():
    sig = inspect.signature(BPMN2Model_CorrelationPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_correlationproperty_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CorrelationProperty)


def test_bpmn2model_correlationproperty_constructor_exists():
    assert callable(BPMN2Model_CorrelationProperty.__init__)


def test_bpmn2model_correlationproperty_constructor_args():
    sig = inspect.signature(BPMN2Model_CorrelationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_correlationproperty_has_name():
    assert hasattr(BPMN2Model_CorrelationProperty, "name")
    descriptor = None
    for klass in BPMN2Model_CorrelationProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_correlationkey_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CorrelationKey)


def test_bpmn2model_correlationkey_constructor_exists():
    assert callable(BPMN2Model_CorrelationKey.__init__)


def test_bpmn2model_correlationkey_constructor_args():
    sig = inspect.signature(BPMN2Model_CorrelationKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_correlationkey_has_name():
    assert hasattr(BPMN2Model_CorrelationKey, "name")
    descriptor = None
    for klass in BPMN2Model_CorrelationKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_conversationlink_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ConversationLink)


def test_bpmn2model_conversationlink_constructor_exists():
    assert callable(BPMN2Model_ConversationLink.__init__)


def test_bpmn2model_conversationlink_constructor_args():
    sig = inspect.signature(BPMN2Model_ConversationLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_conversationlink_has_name():
    assert hasattr(BPMN2Model_ConversationLink, "name")
    descriptor = None
    for klass in BPMN2Model_ConversationLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_rootelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_RootElement)


def test_bpmn2model_rootelement_constructor_exists():
    assert callable(BPMN2Model_RootElement.__init__)


def test_bpmn2model_rootelement_constructor_args():
    sig = inspect.signature(BPMN2Model_RootElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EventDefinition)


def test_bpmn2model_eventdefinition_constructor_exists():
    assert callable(BPMN2Model_EventDefinition.__init__)


def test_bpmn2model_eventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_conditionaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ConditionalEventDefinition)


def test_bpmn2model_conditionaleventdefinition_constructor_exists():
    assert callable(BPMN2Model_ConditionalEventDefinition.__init__)


def test_bpmn2model_conditionaleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ConditionalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_complexgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ComplexGateway)


def test_bpmn2model_complexgateway_constructor_exists():
    assert callable(BPMN2Model_ComplexGateway.__init__)


def test_bpmn2model_complexgateway_constructor_args():
    sig = inspect.signature(BPMN2Model_ComplexGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_complexbehaviordefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ComplexBehaviorDefinition)


def test_bpmn2model_complexbehaviordefinition_constructor_exists():
    assert callable(BPMN2Model_ComplexBehaviorDefinition.__init__)


def test_bpmn2model_complexbehaviordefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ComplexBehaviorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_compensateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CompensateEventDefinition)


def test_bpmn2model_compensateeventdefinition_constructor_exists():
    assert callable(BPMN2Model_CompensateEventDefinition.__init__)


def test_bpmn2model_compensateeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_CompensateEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "waitForCompletion" in params, "Missing parameter 'waitForCompletion'"

def test_bpmn2model_compensateeventdefinition_has_waitForCompletion():
    assert hasattr(BPMN2Model_CompensateEventDefinition, "waitForCompletion")
    descriptor = None
    for klass in BPMN2Model_CompensateEventDefinition.__mro__:
        if "waitForCompletion" in klass.__dict__:
            descriptor = klass.__dict__["waitForCompletion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_choreographytask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ChoreographyTask)


def test_bpmn2model_choreographytask_constructor_exists():
    assert callable(BPMN2Model_ChoreographyTask.__init__)


def test_bpmn2model_choreographytask_constructor_args():
    sig = inspect.signature(BPMN2Model_ChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ChoreographyActivity)


def test_bpmn2model_choreographyactivity_constructor_exists():
    assert callable(BPMN2Model_ChoreographyActivity.__init__)


def test_bpmn2model_choreographyactivity_constructor_args():
    sig = inspect.signature(BPMN2Model_ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_bpmn2model_choreographyactivity_has_loopType():
    assert hasattr(BPMN2Model_ChoreographyActivity, "loopType")
    descriptor = None
    for klass in BPMN2Model_ChoreographyActivity.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_collaboration_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Collaboration)


def test_bpmn2model_collaboration_constructor_exists():
    assert callable(BPMN2Model_Collaboration.__init__)


def test_bpmn2model_collaboration_constructor_args():
    sig = inspect.signature(BPMN2Model_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_bpmn2model_collaboration_has_name():
    assert hasattr(BPMN2Model_Collaboration, "name")
    descriptor = None
    for klass in BPMN2Model_Collaboration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_collaboration_has_isClosed():
    assert hasattr(BPMN2Model_Collaboration, "isClosed")
    descriptor = None
    for klass in BPMN2Model_Collaboration.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_choreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Choreography)


def test_bpmn2model_choreography_constructor_exists():
    assert callable(BPMN2Model_Choreography.__init__)


def test_bpmn2model_choreography_constructor_args():
    sig = inspect.signature(BPMN2Model_Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_categoryvalue_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CategoryValue)


def test_bpmn2model_categoryvalue_constructor_exists():
    assert callable(BPMN2Model_CategoryValue.__init__)


def test_bpmn2model_categoryvalue_constructor_args():
    sig = inspect.signature(BPMN2Model_CategoryValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2model_categoryvalue_has_value():
    assert hasattr(BPMN2Model_CategoryValue, "value")
    descriptor = None
    for klass in BPMN2Model_CategoryValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_category_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Category)


def test_bpmn2model_category_constructor_exists():
    assert callable(BPMN2Model_Category.__init__)


def test_bpmn2model_category_constructor_args():
    sig = inspect.signature(BPMN2Model_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_category_has_name():
    assert hasattr(BPMN2Model_Category, "name")
    descriptor = None
    for klass in BPMN2Model_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_catchevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CatchEvent)


def test_bpmn2model_catchevent_constructor_exists():
    assert callable(BPMN2Model_CatchEvent.__init__)


def test_bpmn2model_catchevent_constructor_args():
    sig = inspect.signature(BPMN2Model_CatchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "parallelMultiple" in params, "Missing parameter 'parallelMultiple'"

def test_bpmn2model_catchevent_has_parallelMultiple():
    assert hasattr(BPMN2Model_CatchEvent, "parallelMultiple")
    descriptor = None
    for klass in BPMN2Model_CatchEvent.__mro__:
        if "parallelMultiple" in klass.__dict__:
            descriptor = klass.__dict__["parallelMultiple"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_flowelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_FlowElement)


def test_bpmn2model_flowelement_constructor_exists():
    assert callable(BPMN2Model_FlowElement.__init__)


def test_bpmn2model_flowelement_constructor_args():
    sig = inspect.signature(BPMN2Model_FlowElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_flowelement_has_name():
    assert hasattr(BPMN2Model_FlowElement, "name")
    descriptor = None
    for klass in BPMN2Model_FlowElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_adhocsubprocess_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_AdHocSubProcess)


def test_bpmn2model_adhocsubprocess_constructor_exists():
    assert callable(BPMN2Model_AdHocSubProcess.__init__)


def test_bpmn2model_adhocsubprocess_constructor_args():
    sig = inspect.signature(BPMN2Model_AdHocSubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "cancelRemainingInstances" in params, "Missing parameter 'cancelRemainingInstances'"

def test_bpmn2model_adhocsubprocess_has_ordering():
    assert hasattr(BPMN2Model_AdHocSubProcess, "ordering")
    descriptor = None
    for klass in BPMN2Model_AdHocSubProcess.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_adhocsubprocess_has_cancelRemainingInstances():
    assert hasattr(BPMN2Model_AdHocSubProcess, "cancelRemainingInstances")
    descriptor = None
    for klass in BPMN2Model_AdHocSubProcess.__mro__:
        if "cancelRemainingInstances" in klass.__dict__:
            descriptor = klass.__dict__["cancelRemainingInstances"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_canceleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CancelEventDefinition)


def test_bpmn2model_canceleventdefinition_constructor_exists():
    assert callable(BPMN2Model_CancelEventDefinition.__init__)


def test_bpmn2model_canceleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_CancelEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_conversationnode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ConversationNode)


def test_bpmn2model_conversationnode_constructor_exists():
    assert callable(BPMN2Model_ConversationNode.__init__)


def test_bpmn2model_conversationnode_constructor_args():
    sig = inspect.signature(BPMN2Model_ConversationNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_conversationnode_has_name():
    assert hasattr(BPMN2Model_ConversationNode, "name")
    descriptor = None
    for klass in BPMN2Model_ConversationNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_callconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CallConversation)


def test_bpmn2model_callconversation_constructor_exists():
    assert callable(BPMN2Model_CallConversation.__init__)


def test_bpmn2model_callconversation_constructor_args():
    sig = inspect.signature(BPMN2Model_CallConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_callchoreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CallChoreography)


def test_bpmn2model_callchoreography_constructor_exists():
    assert callable(BPMN2Model_CallChoreography.__init__)


def test_bpmn2model_callchoreography_constructor_args():
    sig = inspect.signature(BPMN2Model_CallChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_callactivity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CallActivity)


def test_bpmn2model_callactivity_constructor_exists():
    assert callable(BPMN2Model_CallActivity.__init__)


def test_bpmn2model_callactivity_constructor_args():
    sig = inspect.signature(BPMN2Model_CallActivity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_callableelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_CallableElement)


def test_bpmn2model_callableelement_constructor_exists():
    assert callable(BPMN2Model_CallableElement.__init__)


def test_bpmn2model_callableelement_constructor_args():
    sig = inspect.signature(BPMN2Model_CallableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_callableelement_has_name():
    assert hasattr(BPMN2Model_CallableElement, "name")
    descriptor = None
    for klass in BPMN2Model_CallableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_businessruletask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_BusinessRuleTask)


def test_bpmn2model_businessruletask_constructor_exists():
    assert callable(BPMN2Model_BusinessRuleTask.__init__)


def test_bpmn2model_businessruletask_constructor_args():
    sig = inspect.signature(BPMN2Model_BusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_businessruletask_has_implementation():
    assert hasattr(BPMN2Model_BusinessRuleTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_BusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_boundaryevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_BoundaryEvent)


def test_bpmn2model_boundaryevent_constructor_exists():
    assert callable(BPMN2Model_BoundaryEvent.__init__)


def test_bpmn2model_boundaryevent_constructor_args():
    sig = inspect.signature(BPMN2Model_BoundaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "cancelActivity" in params, "Missing parameter 'cancelActivity'"

def test_bpmn2model_boundaryevent_has_cancelActivity():
    assert hasattr(BPMN2Model_BoundaryEvent, "cancelActivity")
    descriptor = None
    for klass in BPMN2Model_BoundaryEvent.__mro__:
        if "cancelActivity" in klass.__dict__:
            descriptor = klass.__dict__["cancelActivity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_auditing_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Auditing)


def test_bpmn2model_auditing_constructor_exists():
    assert callable(BPMN2Model_Auditing.__init__)


def test_bpmn2model_auditing_constructor_args():
    sig = inspect.signature(BPMN2Model_Auditing.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_association_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Association)


def test_bpmn2model_association_constructor_exists():
    assert callable(BPMN2Model_Association.__init__)


def test_bpmn2model_association_constructor_args():
    sig = inspect.signature(BPMN2Model_Association.__init__)
    params = list(sig.parameters.keys())
    assert "associationDirection" in params, "Missing parameter 'associationDirection'"

def test_bpmn2model_association_has_associationDirection():
    assert hasattr(BPMN2Model_Association, "associationDirection")
    descriptor = None
    for klass in BPMN2Model_Association.__mro__:
        if "associationDirection" in klass.__dict__:
            descriptor = klass.__dict__["associationDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_assignment_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Assignment)


def test_bpmn2model_assignment_constructor_exists():
    assert callable(BPMN2Model_Assignment.__init__)


def test_bpmn2model_assignment_constructor_args():
    sig = inspect.signature(BPMN2Model_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_artifact_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Artifact)


def test_bpmn2model_artifact_constructor_exists():
    assert callable(BPMN2Model_Artifact.__init__)


def test_bpmn2model_artifact_constructor_args():
    sig = inspect.signature(BPMN2Model_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_activity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Activity)


def test_bpmn2model_activity_constructor_exists():
    assert callable(BPMN2Model_Activity.__init__)


def test_bpmn2model_activity_constructor_args():
    sig = inspect.signature(BPMN2Model_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isForCompensation" in params, "Missing parameter 'isForCompensation'"
    assert "startQuantity" in params, "Missing parameter 'startQuantity'"
    assert "completionQuantity" in params, "Missing parameter 'completionQuantity'"

def test_bpmn2model_activity_has_isForCompensation():
    assert hasattr(BPMN2Model_Activity, "isForCompensation")
    descriptor = None
    for klass in BPMN2Model_Activity.__mro__:
        if "isForCompensation" in klass.__dict__:
            descriptor = klass.__dict__["isForCompensation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_activity_has_startQuantity():
    assert hasattr(BPMN2Model_Activity, "startQuantity")
    descriptor = None
    for klass in BPMN2Model_Activity.__mro__:
        if "startQuantity" in klass.__dict__:
            descriptor = klass.__dict__["startQuantity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_activity_has_completionQuantity():
    assert hasattr(BPMN2Model_Activity, "completionQuantity")
    descriptor = None
    for klass in BPMN2Model_Activity.__mro__:
        if "completionQuantity" in klass.__dict__:
            descriptor = klass.__dict__["completionQuantity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_EStringToStringMapEntry)


def test_bpmn2model_estringtostringmapentry_constructor_exists():
    assert callable(BPMN2Model_EStringToStringMapEntry.__init__)


def test_bpmn2model_estringtostringmapentry_constructor_args():
    sig = inspect.signature(BPMN2Model_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_bpmnbase_is_not_abstract():
    assert not inspect.isabstract(BPMNBase)


def test_bpmnbase_constructor_exists():
    assert callable(BPMNBase.__init__)


def test_bpmnbase_constructor_args():
    sig = inspect.signature(BPMNBase.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_interactionnode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_InteractionNode)


def test_bpmn2model_interactionnode_constructor_exists():
    assert callable(BPMN2Model_InteractionNode.__init__)


def test_bpmn2model_interactionnode_constructor_args():
    sig = inspect.signature(BPMN2Model_InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_escalation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Escalation)


def test_bpmn2model_escalation_constructor_exists():
    assert callable(BPMN2Model_Escalation.__init__)


def test_bpmn2model_escalation_constructor_args():
    sig = inspect.signature(BPMN2Model_Escalation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "escalationCode" in params, "Missing parameter 'escalationCode'"

def test_bpmn2model_escalation_has_name():
    assert hasattr(BPMN2Model_Escalation, "name")
    descriptor = None
    for klass in BPMN2Model_Escalation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_escalation_has_escalationCode():
    assert hasattr(BPMN2Model_Escalation, "escalationCode")
    descriptor = None
    for klass in BPMN2Model_Escalation.__mro__:
        if "escalationCode" in klass.__dict__:
            descriptor = klass.__dict__["escalationCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_resourceassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ResourceAssignmentExpression)


def test_bpmn2model_resourceassignmentexpression_constructor_exists():
    assert callable(BPMN2Model_ResourceAssignmentExpression.__init__)


def test_bpmn2model_resourceassignmentexpression_constructor_args():
    sig = inspect.signature(BPMN2Model_ResourceAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ExtensionDefinition)


def test_bpmn2model_extensiondefinition_constructor_exists():
    assert callable(BPMN2Model_ExtensionDefinition.__init__)


def test_bpmn2model_extensiondefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model_extensiondefinition_has_name():
    assert hasattr(BPMN2Model_ExtensionDefinition, "name")
    descriptor = None
    for klass in BPMN2Model_ExtensionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_resourceparameterbinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ResourceParameterBinding)


def test_bpmn2model_resourceparameterbinding_constructor_exists():
    assert callable(BPMN2Model_ResourceParameterBinding.__init__)


def test_bpmn2model_resourceparameterbinding_constructor_args():
    sig = inspect.signature(BPMN2Model_ResourceParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_extensionattributedefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ExtensionAttributeDefinition)


def test_bpmn2model_extensionattributedefinition_constructor_exists():
    assert callable(BPMN2Model_ExtensionAttributeDefinition.__init__)


def test_bpmn2model_extensionattributedefinition_constructor_args():
    sig = inspect.signature(BPMN2Model_ExtensionAttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isReference" in params, "Missing parameter 'isReference'"

def test_bpmn2model_extensionattributedefinition_has_type():
    assert hasattr(BPMN2Model_ExtensionAttributeDefinition, "type")
    descriptor = None
    for klass in BPMN2Model_ExtensionAttributeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_extensionattributedefinition_has_name():
    assert hasattr(BPMN2Model_ExtensionAttributeDefinition, "name")
    descriptor = None
    for klass in BPMN2Model_ExtensionAttributeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_extensionattributedefinition_has_isReference():
    assert hasattr(BPMN2Model_ExtensionAttributeDefinition, "isReference")
    descriptor = None
    for klass in BPMN2Model_ExtensionAttributeDefinition.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_extensionattributevalue_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ExtensionAttributeValue)


def test_bpmn2model_extensionattributevalue_constructor_exists():
    assert callable(BPMN2Model_ExtensionAttributeValue.__init__)


def test_bpmn2model_extensionattributevalue_constructor_args():
    sig = inspect.signature(BPMN2Model_ExtensionAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2model_extensionattributevalue_has_value():
    assert hasattr(BPMN2Model_ExtensionAttributeValue, "value")
    descriptor = None
    for klass in BPMN2Model_ExtensionAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_baseelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_BaseElement)


def test_bpmn2model_baseelement_constructor_exists():
    assert callable(BPMN2Model_BaseElement.__init__)


def test_bpmn2model_baseelement_constructor_args():
    sig = inspect.signature(BPMN2Model_BaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_bpmn2model_baseelement_has_id():
    assert hasattr(BPMN2Model_BaseElement, "id")
    descriptor = None
    for klass in BPMN2Model_BaseElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_baseelement_has_anyAttribute():
    assert hasattr(BPMN2Model_BaseElement, "anyAttribute")
    descriptor = None
    for klass in BPMN2Model_BaseElement.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_extension_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Extension)


def test_bpmn2model_extension_constructor_exists():
    assert callable(BPMN2Model_Extension.__init__)


def test_bpmn2model_extension_constructor_args():
    sig = inspect.signature(BPMN2Model_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "xsdDefinition" in params, "Missing parameter 'xsdDefinition'"
    assert "mustUnderstand" in params, "Missing parameter 'mustUnderstand'"

def test_bpmn2model_extension_has_xsdDefinition():
    assert hasattr(BPMN2Model_Extension, "xsdDefinition")
    descriptor = None
    for klass in BPMN2Model_Extension.__mro__:
        if "xsdDefinition" in klass.__dict__:
            descriptor = klass.__dict__["xsdDefinition"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_extension_has_mustUnderstand():
    assert hasattr(BPMN2Model_Extension, "mustUnderstand")
    descriptor = None
    for klass in BPMN2Model_Extension.__mro__:
        if "mustUnderstand" in klass.__dict__:
            descriptor = klass.__dict__["mustUnderstand"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_inputoutputbinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_InputOutputBinding)


def test_bpmn2model_inputoutputbinding_constructor_exists():
    assert callable(BPMN2Model_InputOutputBinding.__init__)


def test_bpmn2model_inputoutputbinding_constructor_args():
    sig = inspect.signature(BPMN2Model_InputOutputBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_participantmultiplicity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_ParticipantMultiplicity)


def test_bpmn2model_participantmultiplicity_constructor_exists():
    assert callable(BPMN2Model_ParticipantMultiplicity.__init__)


def test_bpmn2model_participantmultiplicity_constructor_args():
    sig = inspect.signature(BPMN2Model_ParticipantMultiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"

def test_bpmn2model_participantmultiplicity_has_minimum():
    assert hasattr(BPMN2Model_ParticipantMultiplicity, "minimum")
    descriptor = None
    for klass in BPMN2Model_ParticipantMultiplicity.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_participantmultiplicity_has_maximum():
    assert hasattr(BPMN2Model_ParticipantMultiplicity, "maximum")
    descriptor = None
    for klass in BPMN2Model_ParticipantMultiplicity.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_import_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Import)


def test_bpmn2model_import_constructor_exists():
    assert callable(BPMN2Model_Import.__init__)


def test_bpmn2model_import_constructor_args():
    sig = inspect.signature(BPMN2Model_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importType" in params, "Missing parameter 'importType'"
    assert "location" in params, "Missing parameter 'location'"
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_bpmn2model_import_has_importType():
    assert hasattr(BPMN2Model_Import, "importType")
    descriptor = None
    for klass in BPMN2Model_Import.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_import_has_location():
    assert hasattr(BPMN2Model_Import, "location")
    descriptor = None
    for klass in BPMN2Model_Import.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_import_has_namespace():
    assert hasattr(BPMN2Model_Import, "namespace")
    descriptor = None
    for klass in BPMN2Model_Import.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_documentroot_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_DocumentRoot)


def test_bpmn2model_documentroot_constructor_exists():
    assert callable(BPMN2Model_DocumentRoot.__init__)


def test_bpmn2model_documentroot_constructor_args():
    sig = inspect.signature(BPMN2Model_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_bpmn2model_documentroot_has_mixed():
    assert hasattr(BPMN2Model_DocumentRoot, "mixed")
    descriptor = None
    for klass in BPMN2Model_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_bpmnbase_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_BPMNBase)


def test_bpmn2model_bpmnbase_constructor_exists():
    assert callable(BPMN2Model_BPMNBase.__init__)


def test_bpmn2model_bpmnbase_constructor_args():
    sig = inspect.signature(BPMN2Model_BPMNBase.__init__)
    params = list(sig.parameters.keys())



def test_humanperformer_is_not_abstract():
    assert not inspect.isabstract(HumanPerformer)


def test_humanperformer_constructor_exists():
    assert callable(HumanPerformer.__init__)


def test_humanperformer_constructor_args():
    sig = inspect.signature(HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_potentialowner_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_PotentialOwner)


def test_bpmn2model_potentialowner_constructor_exists():
    assert callable(BPMN2Model_PotentialOwner.__init__)


def test_bpmn2model_potentialowner_constructor_args():
    sig = inspect.signature(BPMN2Model_PotentialOwner.__init__)
    params = list(sig.parameters.keys())



def test_resourcerole_is_not_abstract():
    assert not inspect.isabstract(ResourceRole)


def test_resourcerole_constructor_exists():
    assert callable(ResourceRole.__init__)


def test_resourcerole_constructor_args():
    sig = inspect.signature(ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_performer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Performer)


def test_bpmn2model_performer_constructor_exists():
    assert callable(BPMN2Model_Performer.__init__)


def test_bpmn2model_performer_constructor_args():
    sig = inspect.signature(BPMN2Model_Performer.__init__)
    params = list(sig.parameters.keys())



def test_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(LoopCharacteristics)


def test_loopcharacteristics_constructor_exists():
    assert callable(LoopCharacteristics.__init__)


def test_loopcharacteristics_constructor_args():
    sig = inspect.signature(LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_standardloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_StandardLoopCharacteristics)


def test_bpmn2model_standardloopcharacteristics_constructor_exists():
    assert callable(BPMN2Model_StandardLoopCharacteristics.__init__)


def test_bpmn2model_standardloopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model_StandardLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "testBefore" in params, "Missing parameter 'testBefore'"

def test_bpmn2model_standardloopcharacteristics_has_testBefore():
    assert hasattr(BPMN2Model_StandardLoopCharacteristics, "testBefore")
    descriptor = None
    for klass in BPMN2Model_StandardLoopCharacteristics.__mro__:
        if "testBefore" in klass.__dict__:
            descriptor = klass.__dict__["testBefore"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_multiinstanceloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_MultiInstanceLoopCharacteristics)


def test_bpmn2model_multiinstanceloopcharacteristics_constructor_exists():
    assert callable(BPMN2Model_MultiInstanceLoopCharacteristics.__init__)


def test_bpmn2model_multiinstanceloopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model_MultiInstanceLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "isSequential" in params, "Missing parameter 'isSequential'"
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_bpmn2model_multiinstanceloopcharacteristics_has_isSequential():
    assert hasattr(BPMN2Model_MultiInstanceLoopCharacteristics, "isSequential")
    descriptor = None
    for klass in BPMN2Model_MultiInstanceLoopCharacteristics.__mro__:
        if "isSequential" in klass.__dict__:
            descriptor = klass.__dict__["isSequential"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_multiinstanceloopcharacteristics_has_behavior():
    assert hasattr(BPMN2Model_MultiInstanceLoopCharacteristics, "behavior")
    descriptor = None
    for klass in BPMN2Model_MultiInstanceLoopCharacteristics.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_performer_is_not_abstract():
    assert not inspect.isabstract(Performer)


def test_performer_constructor_exists():
    assert callable(Performer.__init__)


def test_performer_constructor_args():
    sig = inspect.signature(Performer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_humanperformer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_HumanPerformer)


def test_bpmn2model_humanperformer_constructor_exists():
    assert callable(BPMN2Model_HumanPerformer.__init__)


def test_bpmn2model_humanperformer_constructor_args():
    sig = inspect.signature(BPMN2Model_HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_process_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_Process)


def test_bpmn2model_process_constructor_exists():
    assert callable(BPMN2Model_Process.__init__)


def test_bpmn2model_process_constructor_args():
    sig = inspect.signature(BPMN2Model_Process.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "processType" in params, "Missing parameter 'processType'"
    assert "isExecutable" in params, "Missing parameter 'isExecutable'"

def test_bpmn2model_process_has_isClosed():
    assert hasattr(BPMN2Model_Process, "isClosed")
    descriptor = None
    for klass in BPMN2Model_Process.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_process_has_processType():
    assert hasattr(BPMN2Model_Process, "processType")
    descriptor = None
    for klass in BPMN2Model_Process.__mro__:
        if "processType" in klass.__dict__:
            descriptor = klass.__dict__["processType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_process_has_isExecutable():
    assert hasattr(BPMN2Model_Process, "isExecutable")
    descriptor = None
    for klass in BPMN2Model_Process.__mro__:
        if "isExecutable" in klass.__dict__:
            descriptor = klass.__dict__["isExecutable"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_globaltask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalTask)


def test_bpmn2model_globaltask_constructor_exists():
    assert callable(BPMN2Model_GlobalTask.__init__)


def test_bpmn2model_globaltask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_choreography_is_not_abstract():
    assert not inspect.isabstract(Choreography)


def test_choreography_constructor_exists():
    assert callable(Choreography.__init__)


def test_choreography_constructor_args():
    sig = inspect.signature(Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_globalchoreographytask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalChoreographyTask)


def test_bpmn2model_globalchoreographytask_constructor_exists():
    assert callable(BPMN2Model_GlobalChoreographyTask.__init__)


def test_bpmn2model_globalchoreographytask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_globaltask_is_not_abstract():
    assert not inspect.isabstract(GlobalTask)


def test_globaltask_constructor_exists():
    assert callable(GlobalTask.__init__)


def test_globaltask_constructor_args():
    sig = inspect.signature(GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_globalscripttask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalScriptTask)


def test_bpmn2model_globalscripttask_constructor_exists():
    assert callable(BPMN2Model_GlobalScriptTask.__init__)


def test_bpmn2model_globalscripttask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "scriptLanguage" in params, "Missing parameter 'scriptLanguage'"
    assert "script" in params, "Missing parameter 'script'"

def test_bpmn2model_globalscripttask_has_scriptLanguage():
    assert hasattr(BPMN2Model_GlobalScriptTask, "scriptLanguage")
    descriptor = None
    for klass in BPMN2Model_GlobalScriptTask.__mro__:
        if "scriptLanguage" in klass.__dict__:
            descriptor = klass.__dict__["scriptLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_globalscripttask_has_script():
    assert hasattr(BPMN2Model_GlobalScriptTask, "script")
    descriptor = None
    for klass in BPMN2Model_GlobalScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_globalbusinessruletask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalBusinessRuleTask)


def test_bpmn2model_globalbusinessruletask_constructor_exists():
    assert callable(BPMN2Model_GlobalBusinessRuleTask.__init__)


def test_bpmn2model_globalbusinessruletask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalBusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_globalbusinessruletask_has_implementation():
    assert hasattr(BPMN2Model_GlobalBusinessRuleTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_GlobalBusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_globalusertask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalUserTask)


def test_bpmn2model_globalusertask_constructor_exists():
    assert callable(BPMN2Model_GlobalUserTask.__init__)


def test_bpmn2model_globalusertask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalUserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model_globalusertask_has_implementation():
    assert hasattr(BPMN2Model_GlobalUserTask, "implementation")
    descriptor = None
    for klass in BPMN2Model_GlobalUserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model_globalmanualtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_GlobalManualTask)


def test_bpmn2model_globalmanualtask_constructor_exists():
    assert callable(BPMN2Model_GlobalManualTask.__init__)


def test_bpmn2model_globalmanualtask_constructor_args():
    sig = inspect.signature(BPMN2Model_GlobalManualTask.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model_formalexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model_FormalExpression)


def test_bpmn2model_formalexpression_constructor_exists():
    assert callable(BPMN2Model_FormalExpression.__init__)


def test_bpmn2model_formalexpression_constructor_args():
    sig = inspect.signature(BPMN2Model_FormalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_bpmn2model_formalexpression_has_mixed():
    assert hasattr(BPMN2Model_FormalExpression, "mixed")
    descriptor = None
    for klass in BPMN2Model_FormalExpression.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_formalexpression_has_language():
    assert hasattr(BPMN2Model_FormalExpression, "language")
    descriptor = None
    for klass in BPMN2Model_FormalExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model_formalexpression_has_body():
    assert hasattr(BPMN2Model_FormalExpression, "body")
    descriptor = None
    for klass in BPMN2Model_FormalExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_multiinstancebehavior_exists():
    # Check that the Enumeration exists
    assert MultiInstanceBehavior is not None

def test_multiinstancebehavior_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiInstanceBehavior]
    expected_literals = [
        "None_",
        "All",
        "One",
        "Complex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiInstanceBehavior"

def test_gatewaydirection_exists():
    # Check that the Enumeration exists
    assert GatewayDirection is not None

def test_gatewaydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GatewayDirection]
    expected_literals = [
        "Diverging",
        "Mixed",
        "Converging",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GatewayDirection"

def test_itemkind_exists():
    # Check that the Enumeration exists
    assert ItemKind is not None

def test_itemkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ItemKind]
    expected_literals = [
        "Information",
        "Physical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ItemKind"

def test_associationdirection_exists():
    # Check that the Enumeration exists
    assert AssociationDirection is not None

def test_associationdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationDirection]
    expected_literals = [
        "Both",
        "One",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationDirection"

def test_adhocordering_exists():
    # Check that the Enumeration exists
    assert AdHocOrdering is not None

def test_adhocordering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdHocOrdering]
    expected_literals = [
        "Parallel",
        "Sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdHocOrdering"

def test_choreographylooptype_exists():
    # Check that the Enumeration exists
    assert ChoreographyLoopType is not None

def test_choreographylooptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoreographyLoopType]
    expected_literals = [
        "MultiInstanceSequential",
        "None_",
        "Standard",
        "MultiInstanceParallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoreographyLoopType"

def test_processtype_exists():
    # Check that the Enumeration exists
    assert ProcessType is not None

def test_processtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcessType]
    expected_literals = [
        "Private",
        "None_",
        "Public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessType"

def test_eventbasedgatewaytype_exists():
    # Check that the Enumeration exists
    assert EventBasedGatewayType is not None

def test_eventbasedgatewaytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventBasedGatewayType]
    expected_literals = [
        "Parallel",
        "Exclusive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventBasedGatewayType"

def test_relationshipdirection_exists():
    # Check that the Enumeration exists
    assert RelationshipDirection is not None

def test_relationshipdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipDirection]
    expected_literals = [
        "None_",
        "Forward",
        "Both",
        "Backward",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipDirection"


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
ThrowEvent_strategy = st.builds(
    ThrowEvent,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
DataAssociation_strategy = st.builds(
    DataAssociation,
)
ItemAwareElement_strategy = st.builds(
    ItemAwareElement,
)
InteractionNode_strategy = st.builds(
    InteractionNode,
)
Gateway_strategy = st.builds(
    Gateway,
)
FlowElementsContainer_strategy = st.builds(
    FlowElementsContainer,
)
Collaboration_strategy = st.builds(
    Collaboration,
)
Event_strategy = st.builds(
    Event,
)
EventDefinition_strategy = st.builds(
    EventDefinition,
)
RootElement_strategy = st.builds(
    RootElement,
)
ConversationNode_strategy = st.builds(
    ConversationNode,
)
ChoreographyActivity_strategy = st.builds(
    ChoreographyActivity,
)
Activity_strategy = st.builds(
    Activity,
)
Task_strategy = st.builds(
    Task,
)
CatchEvent_strategy = st.builds(
    CatchEvent,
)
Artifact_strategy = st.builds(
    Artifact,
)
BaseElement_strategy = st.builds(
    BaseElement,
)
BPMN2Model_FlowElementsContainer_strategy = st.builds(
    BPMN2Model_FlowElementsContainer,
)
BPMN2Model_ItemAwareElement_strategy = st.builds(
    BPMN2Model_ItemAwareElement,
)
SubProcess_strategy = st.builds(
    SubProcess,
)
BPMN2Model_ThrowEvent_strategy = st.builds(
    BPMN2Model_ThrowEvent,
)
FlowNode_strategy = st.builds(
    FlowNode,
)
BPMN2Model_UserTask_strategy = st.builds(
    BPMN2Model_UserTask,
    implementation=
        safe_text
)
BPMN2Model_Transaction_strategy = st.builds(
    BPMN2Model_Transaction,
    method=
        safe_text,
    protocol=
        safe_text
)
BPMN2Model_TimerEventDefinition_strategy = st.builds(
    BPMN2Model_TimerEventDefinition,
)
BPMN2Model_StartEvent_strategy = st.builds(
    BPMN2Model_StartEvent,
    isInterrupting=
        st.booleans()
)
BPMN2Model_TextAnnotation_strategy = st.builds(
    BPMN2Model_TextAnnotation,
    text=
        safe_text,
    textFormat=
        safe_text
)
BPMN2Model_TerminateEventDefinition_strategy = st.builds(
    BPMN2Model_TerminateEventDefinition,
)
BPMN2Model_Task_strategy = st.builds(
    BPMN2Model_Task,
)
BPMN2Model_SubProcess_strategy = st.builds(
    BPMN2Model_SubProcess,
    triggeredByEvent=
        st.booleans()
)
BPMN2Model_SubConversation_strategy = st.builds(
    BPMN2Model_SubConversation,
)
BPMN2Model_SubChoreography_strategy = st.builds(
    BPMN2Model_SubChoreography,
)
BPMN2Model_EObject_strategy = st.builds(
    BPMN2Model_EObject,
)
BPMN2Model_SignalEventDefinition_strategy = st.builds(
    BPMN2Model_SignalEventDefinition,
)
BPMN2Model_Signal_strategy = st.builds(
    BPMN2Model_Signal,
    name=
        safe_text
)
BPMN2Model_ServiceTask_strategy = st.builds(
    BPMN2Model_ServiceTask,
    implementation=
        safe_text
)
BPMN2Model_SequenceFlow_strategy = st.builds(
    BPMN2Model_SequenceFlow,
    isImmediate=
        st.booleans()
)
BPMN2Model_SendTask_strategy = st.builds(
    BPMN2Model_SendTask,
    implementation=
        safe_text
)
BPMN2Model_ScriptTask_strategy = st.builds(
    BPMN2Model_ScriptTask,
    script=
        safe_text,
    scriptFormat=
        safe_text
)
BPMN2Model_ResourceParameter_strategy = st.builds(
    BPMN2Model_ResourceParameter,
    name=
        safe_text,
    isRequired=
        st.booleans()
)
BPMN2Model_Resource_strategy = st.builds(
    BPMN2Model_Resource,
    name=
        safe_text
)
BPMN2Model_Rendering_strategy = st.builds(
    BPMN2Model_Rendering,
)
BPMN2Model_Relationship_strategy = st.builds(
    BPMN2Model_Relationship,
    type=
        safe_text,
    direction=
        safe_text
)
BPMN2Model_ReceiveTask_strategy = st.builds(
    BPMN2Model_ReceiveTask,
    implementation=
        safe_text,
    instantiate=
        st.booleans()
)
BPMN2Model_Property_strategy = st.builds(
    BPMN2Model_Property,
    name=
        safe_text
)
BPMN2Model_PartnerRole_strategy = st.builds(
    BPMN2Model_PartnerRole,
    name=
        safe_text
)
BPMN2Model_PartnerEntity_strategy = st.builds(
    BPMN2Model_PartnerEntity,
    name=
        safe_text
)
BPMN2Model_MessageEventDefinition_strategy = st.builds(
    BPMN2Model_MessageEventDefinition,
)
BPMN2Model_ParticipantAssociation_strategy = st.builds(
    BPMN2Model_ParticipantAssociation,
)
BPMN2Model_Participant_strategy = st.builds(
    BPMN2Model_Participant,
    name=
        safe_text
)
BPMN2Model_ParallelGateway_strategy = st.builds(
    BPMN2Model_ParallelGateway,
)
BPMN2Model_OutputSet_strategy = st.builds(
    BPMN2Model_OutputSet,
    name=
        safe_text
)
BPMN2Model_Operation_strategy = st.builds(
    BPMN2Model_Operation,
    name=
        safe_text
)
BPMN2Model_Monitoring_strategy = st.builds(
    BPMN2Model_Monitoring,
)
BPMN2Model_MessageFlowAssociation_strategy = st.builds(
    BPMN2Model_MessageFlowAssociation,
)
BPMN2Model_MessageFlow_strategy = st.builds(
    BPMN2Model_MessageFlow,
    name=
        safe_text
)
BPMN2Model_IntermediateCatchEvent_strategy = st.builds(
    BPMN2Model_IntermediateCatchEvent,
)
BPMN2Model_Message_strategy = st.builds(
    BPMN2Model_Message,
    name=
        safe_text
)
BPMN2Model_ManualTask_strategy = st.builds(
    BPMN2Model_ManualTask,
)
BPMN2Model_LoopCharacteristics_strategy = st.builds(
    BPMN2Model_LoopCharacteristics,
)
BPMN2Model_LinkEventDefinition_strategy = st.builds(
    BPMN2Model_LinkEventDefinition,
    name=
        safe_text
)
BPMN2Model_LaneSet_strategy = st.builds(
    BPMN2Model_LaneSet,
    name=
        safe_text
)
BPMN2Model_Lane_strategy = st.builds(
    BPMN2Model_Lane,
    name=
        safe_text
)
BPMN2Model_ItemDefinition_strategy = st.builds(
    BPMN2Model_ItemDefinition,
    itemKind=
        safe_text,
    isCollection=
        st.booleans()
)
BPMN2Model_InputOutputSpecification_strategy = st.builds(
    BPMN2Model_InputOutputSpecification,
)
BPMN2Model_IntermediateThrowEvent_strategy = st.builds(
    BPMN2Model_IntermediateThrowEvent,
)
BPMN2Model_Interface_strategy = st.builds(
    BPMN2Model_Interface,
    name=
        safe_text
)
BPMN2Model_InputSet_strategy = st.builds(
    BPMN2Model_InputSet,
    name=
        safe_text
)
BPMN2Model_InclusiveGateway_strategy = st.builds(
    BPMN2Model_InclusiveGateway,
)
BPMN2Model_ImplicitThrowEvent_strategy = st.builds(
    BPMN2Model_ImplicitThrowEvent,
)
BPMN2Model_ResourceRole_strategy = st.builds(
    BPMN2Model_ResourceRole,
    name=
        safe_text
)
BPMN2Model_Group_strategy = st.builds(
    BPMN2Model_Group,
)
BPMN2Model_ExclusiveGateway_strategy = st.builds(
    BPMN2Model_ExclusiveGateway,
)
BPMN2Model_GlobalConversation_strategy = st.builds(
    BPMN2Model_GlobalConversation,
)
BPMN2Model_Gateway_strategy = st.builds(
    BPMN2Model_Gateway,
    gatewayDirection=
        safe_text
)
BPMN2Model_FlowNode_strategy = st.builds(
    BPMN2Model_FlowNode,
)
BPMN2Model_Expression_strategy = st.builds(
    BPMN2Model_Expression,
)
BPMN2Model_DataOutputAssociation_strategy = st.builds(
    BPMN2Model_DataOutputAssociation,
)
BPMN2Model_EventBasedGateway_strategy = st.builds(
    BPMN2Model_EventBasedGateway,
    instantiate=
        st.booleans(),
    eventGatewayType=
        safe_text
)
BPMN2Model_Event_strategy = st.builds(
    BPMN2Model_Event,
)
BPMN2Model_EscalationEventDefinition_strategy = st.builds(
    BPMN2Model_EscalationEventDefinition,
)
BPMN2Model_ErrorEventDefinition_strategy = st.builds(
    BPMN2Model_ErrorEventDefinition,
)
BPMN2Model_Error_strategy = st.builds(
    BPMN2Model_Error,
    name=
        safe_text,
    errorCode=
        safe_text
)
BPMN2Model_EndPoint_strategy = st.builds(
    BPMN2Model_EndPoint,
)
BPMN2Model_EndEvent_strategy = st.builds(
    BPMN2Model_EndEvent,
)
BPMN2Model_Documentation_strategy = st.builds(
    BPMN2Model_Documentation,
    mixed=
        safe_text,
    text=
        safe_text,
    textFormat=
        safe_text
)
BPMN2Model_Definitions_strategy = st.builds(
    BPMN2Model_Definitions,
    exporterVersion=
        safe_text,
    expressionLanguage=
        safe_text,
    exporter=
        safe_text,
    targetNamespace=
        safe_text,
    name=
        safe_text,
    typeLanguage=
        safe_text
)
BPMN2Model_DataStoreReference_strategy = st.builds(
    BPMN2Model_DataStoreReference,
)
BPMN2Model_DataStore_strategy = st.builds(
    BPMN2Model_DataStore,
    capacity=
        st.integers(),
    name=
        safe_text,
    isUnlimited=
        st.booleans()
)
BPMN2Model_DataState_strategy = st.builds(
    BPMN2Model_DataState,
    name=
        safe_text
)
BPMN2Model_ConversationAssociation_strategy = st.builds(
    BPMN2Model_ConversationAssociation,
)
BPMN2Model_Conversation_strategy = st.builds(
    BPMN2Model_Conversation,
)
BPMN2Model_DataOutput_strategy = st.builds(
    BPMN2Model_DataOutput,
    isCollection=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model_DataObjectReference_strategy = st.builds(
    BPMN2Model_DataObjectReference,
)
BPMN2Model_DataObject_strategy = st.builds(
    BPMN2Model_DataObject,
    isCollection=
        st.booleans()
)
BPMN2Model_DataInputAssociation_strategy = st.builds(
    BPMN2Model_DataInputAssociation,
)
BPMN2Model_DataInput_strategy = st.builds(
    BPMN2Model_DataInput,
    isCollection=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model_DataAssociation_strategy = st.builds(
    BPMN2Model_DataAssociation,
)
BPMN2Model_CorrelationSubscription_strategy = st.builds(
    BPMN2Model_CorrelationSubscription,
)
BPMN2Model_CorrelationPropertyRetrievalExpression_strategy = st.builds(
    BPMN2Model_CorrelationPropertyRetrievalExpression,
)
BPMN2Model_CorrelationPropertyBinding_strategy = st.builds(
    BPMN2Model_CorrelationPropertyBinding,
)
BPMN2Model_CorrelationProperty_strategy = st.builds(
    BPMN2Model_CorrelationProperty,
    name=
        safe_text
)
BPMN2Model_CorrelationKey_strategy = st.builds(
    BPMN2Model_CorrelationKey,
    name=
        safe_text
)
BPMN2Model_ConversationLink_strategy = st.builds(
    BPMN2Model_ConversationLink,
    name=
        safe_text
)
BPMN2Model_RootElement_strategy = st.builds(
    BPMN2Model_RootElement,
)
BPMN2Model_EventDefinition_strategy = st.builds(
    BPMN2Model_EventDefinition,
)
BPMN2Model_ConditionalEventDefinition_strategy = st.builds(
    BPMN2Model_ConditionalEventDefinition,
)
BPMN2Model_ComplexGateway_strategy = st.builds(
    BPMN2Model_ComplexGateway,
)
BPMN2Model_ComplexBehaviorDefinition_strategy = st.builds(
    BPMN2Model_ComplexBehaviorDefinition,
)
BPMN2Model_CompensateEventDefinition_strategy = st.builds(
    BPMN2Model_CompensateEventDefinition,
    waitForCompletion=
        st.booleans()
)
BPMN2Model_ChoreographyTask_strategy = st.builds(
    BPMN2Model_ChoreographyTask,
)
BPMN2Model_ChoreographyActivity_strategy = st.builds(
    BPMN2Model_ChoreographyActivity,
    loopType=
        safe_text
)
BPMN2Model_Collaboration_strategy = st.builds(
    BPMN2Model_Collaboration,
    name=
        safe_text,
    isClosed=
        st.booleans()
)
BPMN2Model_Choreography_strategy = st.builds(
    BPMN2Model_Choreography,
)
BPMN2Model_CategoryValue_strategy = st.builds(
    BPMN2Model_CategoryValue,
    value=
        safe_text
)
BPMN2Model_Category_strategy = st.builds(
    BPMN2Model_Category,
    name=
        safe_text
)
BPMN2Model_CatchEvent_strategy = st.builds(
    BPMN2Model_CatchEvent,
    parallelMultiple=
        st.booleans()
)
BPMN2Model_FlowElement_strategy = st.builds(
    BPMN2Model_FlowElement,
    name=
        safe_text
)
BPMN2Model_AdHocSubProcess_strategy = st.builds(
    BPMN2Model_AdHocSubProcess,
    ordering=
        safe_text,
    cancelRemainingInstances=
        st.booleans()
)
BPMN2Model_CancelEventDefinition_strategy = st.builds(
    BPMN2Model_CancelEventDefinition,
)
BPMN2Model_ConversationNode_strategy = st.builds(
    BPMN2Model_ConversationNode,
    name=
        safe_text
)
BPMN2Model_CallConversation_strategy = st.builds(
    BPMN2Model_CallConversation,
)
BPMN2Model_CallChoreography_strategy = st.builds(
    BPMN2Model_CallChoreography,
)
BPMN2Model_CallActivity_strategy = st.builds(
    BPMN2Model_CallActivity,
)
BPMN2Model_CallableElement_strategy = st.builds(
    BPMN2Model_CallableElement,
    name=
        safe_text
)
BPMN2Model_BusinessRuleTask_strategy = st.builds(
    BPMN2Model_BusinessRuleTask,
    implementation=
        safe_text
)
BPMN2Model_BoundaryEvent_strategy = st.builds(
    BPMN2Model_BoundaryEvent,
    cancelActivity=
        st.booleans()
)
BPMN2Model_Auditing_strategy = st.builds(
    BPMN2Model_Auditing,
)
BPMN2Model_Association_strategy = st.builds(
    BPMN2Model_Association,
    associationDirection=
        safe_text
)
BPMN2Model_Assignment_strategy = st.builds(
    BPMN2Model_Assignment,
)
BPMN2Model_Artifact_strategy = st.builds(
    BPMN2Model_Artifact,
)
BPMN2Model_Activity_strategy = st.builds(
    BPMN2Model_Activity,
    isForCompensation=
        st.booleans(),
    startQuantity=
        st.integers(),
    completionQuantity=
        st.integers()
)
BPMN2Model_EStringToStringMapEntry_strategy = st.builds(
    BPMN2Model_EStringToStringMapEntry,
)
BPMNBase_strategy = st.builds(
    BPMNBase,
)
BPMN2Model_InteractionNode_strategy = st.builds(
    BPMN2Model_InteractionNode,
)
BPMN2Model_Escalation_strategy = st.builds(
    BPMN2Model_Escalation,
    name=
        safe_text,
    escalationCode=
        safe_text
)
BPMN2Model_ResourceAssignmentExpression_strategy = st.builds(
    BPMN2Model_ResourceAssignmentExpression,
)
BPMN2Model_ExtensionDefinition_strategy = st.builds(
    BPMN2Model_ExtensionDefinition,
    name=
        safe_text
)
BPMN2Model_ResourceParameterBinding_strategy = st.builds(
    BPMN2Model_ResourceParameterBinding,
)
BPMN2Model_ExtensionAttributeDefinition_strategy = st.builds(
    BPMN2Model_ExtensionAttributeDefinition,
    type=
        safe_text,
    name=
        safe_text,
    isReference=
        st.booleans()
)
BPMN2Model_ExtensionAttributeValue_strategy = st.builds(
    BPMN2Model_ExtensionAttributeValue,
    value=
        safe_text
)
BPMN2Model_BaseElement_strategy = st.builds(
    BPMN2Model_BaseElement,
    id=
        safe_text,
    anyAttribute=
        safe_text
)
BPMN2Model_Extension_strategy = st.builds(
    BPMN2Model_Extension,
    xsdDefinition=
        safe_text,
    mustUnderstand=
        st.booleans()
)
BPMN2Model_InputOutputBinding_strategy = st.builds(
    BPMN2Model_InputOutputBinding,
)
BPMN2Model_ParticipantMultiplicity_strategy = st.builds(
    BPMN2Model_ParticipantMultiplicity,
    minimum=
        st.integers(),
    maximum=
        st.integers()
)
BPMN2Model_Import_strategy = st.builds(
    BPMN2Model_Import,
    importType=
        safe_text,
    location=
        safe_text,
    namespace=
        safe_text
)
BPMN2Model_DocumentRoot_strategy = st.builds(
    BPMN2Model_DocumentRoot,
    mixed=
        safe_text
)
EObject_strategy = st.builds(
    EObject,
)
BPMN2Model_BPMNBase_strategy = st.builds(
    BPMN2Model_BPMNBase,
)
HumanPerformer_strategy = st.builds(
    HumanPerformer,
)
BPMN2Model_PotentialOwner_strategy = st.builds(
    BPMN2Model_PotentialOwner,
)
ResourceRole_strategy = st.builds(
    ResourceRole,
)
BPMN2Model_Performer_strategy = st.builds(
    BPMN2Model_Performer,
)
LoopCharacteristics_strategy = st.builds(
    LoopCharacteristics,
)
BPMN2Model_StandardLoopCharacteristics_strategy = st.builds(
    BPMN2Model_StandardLoopCharacteristics,
    testBefore=
        st.booleans()
)
BPMN2Model_MultiInstanceLoopCharacteristics_strategy = st.builds(
    BPMN2Model_MultiInstanceLoopCharacteristics,
    isSequential=
        st.booleans(),
    behavior=
        safe_text
)
Performer_strategy = st.builds(
    Performer,
)
BPMN2Model_HumanPerformer_strategy = st.builds(
    BPMN2Model_HumanPerformer,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
BPMN2Model_Process_strategy = st.builds(
    BPMN2Model_Process,
    isClosed=
        st.booleans(),
    processType=
        safe_text,
    isExecutable=
        st.booleans()
)
BPMN2Model_GlobalTask_strategy = st.builds(
    BPMN2Model_GlobalTask,
)
Choreography_strategy = st.builds(
    Choreography,
)
BPMN2Model_GlobalChoreographyTask_strategy = st.builds(
    BPMN2Model_GlobalChoreographyTask,
)
GlobalTask_strategy = st.builds(
    GlobalTask,
)
BPMN2Model_GlobalScriptTask_strategy = st.builds(
    BPMN2Model_GlobalScriptTask,
    scriptLanguage=
        safe_text,
    script=
        safe_text
)
BPMN2Model_GlobalBusinessRuleTask_strategy = st.builds(
    BPMN2Model_GlobalBusinessRuleTask,
    implementation=
        safe_text
)
BPMN2Model_GlobalUserTask_strategy = st.builds(
    BPMN2Model_GlobalUserTask,
    implementation=
        safe_text
)
BPMN2Model_GlobalManualTask_strategy = st.builds(
    BPMN2Model_GlobalManualTask,
)
Expression_strategy = st.builds(
    Expression,
)
BPMN2Model_FormalExpression_strategy = st.builds(
    BPMN2Model_FormalExpression,
    mixed=
        safe_text,
    language=
        safe_text,
    body=
        safe_text
)

@given(instance=ThrowEvent_strategy)
@settings(max_examples=50)
def test_throwevent_instantiation(instance):
    assert isinstance(instance, ThrowEvent)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=DataAssociation_strategy)
@settings(max_examples=50)
def test_dataassociation_instantiation(instance):
    assert isinstance(instance, DataAssociation)

@given(instance=ItemAwareElement_strategy)
@settings(max_examples=50)
def test_itemawareelement_instantiation(instance):
    assert isinstance(instance, ItemAwareElement)

@given(instance=InteractionNode_strategy)
@settings(max_examples=50)
def test_interactionnode_instantiation(instance):
    assert isinstance(instance, InteractionNode)

@given(instance=Gateway_strategy)
@settings(max_examples=50)
def test_gateway_instantiation(instance):
    assert isinstance(instance, Gateway)

@given(instance=FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_flowelementscontainer_instantiation(instance):
    assert isinstance(instance, FlowElementsContainer)

@given(instance=Collaboration_strategy)
@settings(max_examples=50)
def test_collaboration_instantiation(instance):
    assert isinstance(instance, Collaboration)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=EventDefinition_strategy)
@settings(max_examples=50)
def test_eventdefinition_instantiation(instance):
    assert isinstance(instance, EventDefinition)

@given(instance=RootElement_strategy)
@settings(max_examples=50)
def test_rootelement_instantiation(instance):
    assert isinstance(instance, RootElement)

@given(instance=ConversationNode_strategy)
@settings(max_examples=50)
def test_conversationnode_instantiation(instance):
    assert isinstance(instance, ConversationNode)

@given(instance=ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_choreographyactivity_instantiation(instance):
    assert isinstance(instance, ChoreographyActivity)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=CatchEvent_strategy)
@settings(max_examples=50)
def test_catchevent_instantiation(instance):
    assert isinstance(instance, CatchEvent)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=BaseElement_strategy)
@settings(max_examples=50)
def test_baseelement_instantiation(instance):
    assert isinstance(instance, BaseElement)

@given(instance=BPMN2Model_FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_bpmn2model_flowelementscontainer_instantiation(instance):
    assert isinstance(instance, BPMN2Model_FlowElementsContainer)

@given(instance=BPMN2Model_ItemAwareElement_strategy)
@settings(max_examples=50)
def test_bpmn2model_itemawareelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ItemAwareElement)

@given(instance=SubProcess_strategy)
@settings(max_examples=50)
def test_subprocess_instantiation(instance):
    assert isinstance(instance, SubProcess)

@given(instance=BPMN2Model_ThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_throwevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ThrowEvent)

@given(instance=FlowNode_strategy)
@settings(max_examples=50)
def test_flownode_instantiation(instance):
    assert isinstance(instance, FlowNode)

@given(instance=BPMN2Model_UserTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_usertask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_UserTask)



@given(instance=BPMN2Model_UserTask_strategy)
def test_bpmn2model_usertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_Transaction_strategy)
@settings(max_examples=50)
def test_bpmn2model_transaction_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Transaction)



@given(instance=BPMN2Model_Transaction_strategy)
def test_bpmn2model_transaction_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=BPMN2Model_Transaction_strategy)
def test_bpmn2model_transaction_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=BPMN2Model_TimerEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_timereventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_TimerEventDefinition)

@given(instance=BPMN2Model_StartEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_startevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_StartEvent)



@given(instance=BPMN2Model_StartEvent_strategy)
def test_bpmn2model_startevent_isInterrupting_setter(instance):
    original = instance.isInterrupting
    instance.isInterrupting = original
    assert instance.isInterrupting == original

@given(instance=BPMN2Model_TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn2model_textannotation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_TextAnnotation)



@given(instance=BPMN2Model_TextAnnotation_strategy)
def test_bpmn2model_textannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=BPMN2Model_TextAnnotation_strategy)
def test_bpmn2model_textannotation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=BPMN2Model_TerminateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_terminateeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_TerminateEventDefinition)

@given(instance=BPMN2Model_Task_strategy)
@settings(max_examples=50)
def test_bpmn2model_task_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Task)

@given(instance=BPMN2Model_SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2model_subprocess_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SubProcess)



@given(instance=BPMN2Model_SubProcess_strategy)
def test_bpmn2model_subprocess_triggeredByEvent_setter(instance):
    original = instance.triggeredByEvent
    instance.triggeredByEvent = original
    assert instance.triggeredByEvent == original

@given(instance=BPMN2Model_SubConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model_subconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SubConversation)

@given(instance=BPMN2Model_SubChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2model_subchoreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SubChoreography)

@given(instance=BPMN2Model_EObject_strategy)
@settings(max_examples=50)
def test_bpmn2model_eobject_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EObject)

@given(instance=BPMN2Model_SignalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_signaleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SignalEventDefinition)

@given(instance=BPMN2Model_Signal_strategy)
@settings(max_examples=50)
def test_bpmn2model_signal_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Signal)



@given(instance=BPMN2Model_Signal_strategy)
def test_bpmn2model_signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ServiceTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_servicetask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ServiceTask)



@given(instance=BPMN2Model_ServiceTask_strategy)
def test_bpmn2model_servicetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_SequenceFlow_strategy)
@settings(max_examples=50)
def test_bpmn2model_sequenceflow_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SequenceFlow)



@given(instance=BPMN2Model_SequenceFlow_strategy)
def test_bpmn2model_sequenceflow_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original

@given(instance=BPMN2Model_SendTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_sendtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_SendTask)



@given(instance=BPMN2Model_SendTask_strategy)
def test_bpmn2model_sendtask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_ScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_scripttask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ScriptTask)



@given(instance=BPMN2Model_ScriptTask_strategy)
def test_bpmn2model_scripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original



@given(instance=BPMN2Model_ScriptTask_strategy)
def test_bpmn2model_scripttask_scriptFormat_setter(instance):
    original = instance.scriptFormat
    instance.scriptFormat = original
    assert instance.scriptFormat == original

@given(instance=BPMN2Model_ResourceParameter_strategy)
@settings(max_examples=50)
def test_bpmn2model_resourceparameter_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ResourceParameter)



@given(instance=BPMN2Model_ResourceParameter_strategy)
def test_bpmn2model_resourceparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_ResourceParameter_strategy)
def test_bpmn2model_resourceparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BPMN2Model_Resource_strategy)
@settings(max_examples=50)
def test_bpmn2model_resource_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Resource)



@given(instance=BPMN2Model_Resource_strategy)
def test_bpmn2model_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_Rendering_strategy)
@settings(max_examples=50)
def test_bpmn2model_rendering_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Rendering)

@given(instance=BPMN2Model_Relationship_strategy)
@settings(max_examples=50)
def test_bpmn2model_relationship_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Relationship)



@given(instance=BPMN2Model_Relationship_strategy)
def test_bpmn2model_relationship_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=BPMN2Model_Relationship_strategy)
def test_bpmn2model_relationship_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=BPMN2Model_ReceiveTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_receivetask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ReceiveTask)



@given(instance=BPMN2Model_ReceiveTask_strategy)
def test_bpmn2model_receivetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=BPMN2Model_ReceiveTask_strategy)
def test_bpmn2model_receivetask_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=BPMN2Model_Property_strategy)
@settings(max_examples=50)
def test_bpmn2model_property_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Property)



@given(instance=BPMN2Model_Property_strategy)
def test_bpmn2model_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_PartnerRole_strategy)
@settings(max_examples=50)
def test_bpmn2model_partnerrole_instantiation(instance):
    assert isinstance(instance, BPMN2Model_PartnerRole)



@given(instance=BPMN2Model_PartnerRole_strategy)
def test_bpmn2model_partnerrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_PartnerEntity_strategy)
@settings(max_examples=50)
def test_bpmn2model_partnerentity_instantiation(instance):
    assert isinstance(instance, BPMN2Model_PartnerEntity)



@given(instance=BPMN2Model_PartnerEntity_strategy)
def test_bpmn2model_partnerentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_MessageEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_messageeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_MessageEventDefinition)

@given(instance=BPMN2Model_ParticipantAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_participantassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ParticipantAssociation)

@given(instance=BPMN2Model_Participant_strategy)
@settings(max_examples=50)
def test_bpmn2model_participant_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Participant)



@given(instance=BPMN2Model_Participant_strategy)
def test_bpmn2model_participant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ParallelGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_parallelgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ParallelGateway)

@given(instance=BPMN2Model_OutputSet_strategy)
@settings(max_examples=50)
def test_bpmn2model_outputset_instantiation(instance):
    assert isinstance(instance, BPMN2Model_OutputSet)



@given(instance=BPMN2Model_OutputSet_strategy)
def test_bpmn2model_outputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_Operation_strategy)
@settings(max_examples=50)
def test_bpmn2model_operation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Operation)



@given(instance=BPMN2Model_Operation_strategy)
def test_bpmn2model_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_Monitoring_strategy)
@settings(max_examples=50)
def test_bpmn2model_monitoring_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Monitoring)

@given(instance=BPMN2Model_MessageFlowAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_messageflowassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_MessageFlowAssociation)

@given(instance=BPMN2Model_MessageFlow_strategy)
@settings(max_examples=50)
def test_bpmn2model_messageflow_instantiation(instance):
    assert isinstance(instance, BPMN2Model_MessageFlow)



@given(instance=BPMN2Model_MessageFlow_strategy)
def test_bpmn2model_messageflow_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_IntermediateCatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_intermediatecatchevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_IntermediateCatchEvent)

@given(instance=BPMN2Model_Message_strategy)
@settings(max_examples=50)
def test_bpmn2model_message_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Message)



@given(instance=BPMN2Model_Message_strategy)
def test_bpmn2model_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_manualtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ManualTask)

@given(instance=BPMN2Model_LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model_LoopCharacteristics)

@given(instance=BPMN2Model_LinkEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_linkeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_LinkEventDefinition)



@given(instance=BPMN2Model_LinkEventDefinition_strategy)
def test_bpmn2model_linkeventdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_LaneSet_strategy)
@settings(max_examples=50)
def test_bpmn2model_laneset_instantiation(instance):
    assert isinstance(instance, BPMN2Model_LaneSet)



@given(instance=BPMN2Model_LaneSet_strategy)
def test_bpmn2model_laneset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_Lane_strategy)
@settings(max_examples=50)
def test_bpmn2model_lane_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Lane)



@given(instance=BPMN2Model_Lane_strategy)
def test_bpmn2model_lane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ItemDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_itemdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ItemDefinition)



@given(instance=BPMN2Model_ItemDefinition_strategy)
def test_bpmn2model_itemdefinition_itemKind_setter(instance):
    original = instance.itemKind
    instance.itemKind = original
    assert instance.itemKind == original



@given(instance=BPMN2Model_ItemDefinition_strategy)
def test_bpmn2model_itemdefinition_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model_InputOutputSpecification_strategy)
@settings(max_examples=50)
def test_bpmn2model_inputoutputspecification_instantiation(instance):
    assert isinstance(instance, BPMN2Model_InputOutputSpecification)

@given(instance=BPMN2Model_IntermediateThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_intermediatethrowevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_IntermediateThrowEvent)

@given(instance=BPMN2Model_Interface_strategy)
@settings(max_examples=50)
def test_bpmn2model_interface_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Interface)



@given(instance=BPMN2Model_Interface_strategy)
def test_bpmn2model_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_InputSet_strategy)
@settings(max_examples=50)
def test_bpmn2model_inputset_instantiation(instance):
    assert isinstance(instance, BPMN2Model_InputSet)



@given(instance=BPMN2Model_InputSet_strategy)
def test_bpmn2model_inputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_InclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_inclusivegateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_InclusiveGateway)

@given(instance=BPMN2Model_ImplicitThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_implicitthrowevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ImplicitThrowEvent)

@given(instance=BPMN2Model_ResourceRole_strategy)
@settings(max_examples=50)
def test_bpmn2model_resourcerole_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ResourceRole)



@given(instance=BPMN2Model_ResourceRole_strategy)
def test_bpmn2model_resourcerole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_Group_strategy)
@settings(max_examples=50)
def test_bpmn2model_group_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Group)

@given(instance=BPMN2Model_ExclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_exclusivegateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ExclusiveGateway)

@given(instance=BPMN2Model_GlobalConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalConversation)

@given(instance=BPMN2Model_Gateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_gateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Gateway)



@given(instance=BPMN2Model_Gateway_strategy)
def test_bpmn2model_gateway_gatewayDirection_setter(instance):
    original = instance.gatewayDirection
    instance.gatewayDirection = original
    assert instance.gatewayDirection == original

@given(instance=BPMN2Model_FlowNode_strategy)
@settings(max_examples=50)
def test_bpmn2model_flownode_instantiation(instance):
    assert isinstance(instance, BPMN2Model_FlowNode)

@given(instance=BPMN2Model_Expression_strategy)
@settings(max_examples=50)
def test_bpmn2model_expression_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Expression)

@given(instance=BPMN2Model_DataOutputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_dataoutputassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataOutputAssociation)

@given(instance=BPMN2Model_EventBasedGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_eventbasedgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EventBasedGateway)



@given(instance=BPMN2Model_EventBasedGateway_strategy)
def test_bpmn2model_eventbasedgateway_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original



@given(instance=BPMN2Model_EventBasedGateway_strategy)
def test_bpmn2model_eventbasedgateway_eventGatewayType_setter(instance):
    original = instance.eventGatewayType
    instance.eventGatewayType = original
    assert instance.eventGatewayType == original

@given(instance=BPMN2Model_Event_strategy)
@settings(max_examples=50)
def test_bpmn2model_event_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Event)

@given(instance=BPMN2Model_EscalationEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_escalationeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EscalationEventDefinition)

@given(instance=BPMN2Model_ErrorEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_erroreventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ErrorEventDefinition)

@given(instance=BPMN2Model_Error_strategy)
@settings(max_examples=50)
def test_bpmn2model_error_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Error)



@given(instance=BPMN2Model_Error_strategy)
def test_bpmn2model_error_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_Error_strategy)
def test_bpmn2model_error_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=BPMN2Model_EndPoint_strategy)
@settings(max_examples=50)
def test_bpmn2model_endpoint_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EndPoint)

@given(instance=BPMN2Model_EndEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_endevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EndEvent)

@given(instance=BPMN2Model_Documentation_strategy)
@settings(max_examples=50)
def test_bpmn2model_documentation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Documentation)



@given(instance=BPMN2Model_Documentation_strategy)
def test_bpmn2model_documentation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=BPMN2Model_Documentation_strategy)
def test_bpmn2model_documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=BPMN2Model_Documentation_strategy)
def test_bpmn2model_documentation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=BPMN2Model_Definitions_strategy)
@settings(max_examples=50)
def test_bpmn2model_definitions_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Definitions)



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_exporterVersion_setter(instance):
    original = instance.exporterVersion
    instance.exporterVersion = original
    assert instance.exporterVersion == original



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_expressionLanguage_setter(instance):
    original = instance.expressionLanguage
    instance.expressionLanguage = original
    assert instance.expressionLanguage == original



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_exporter_setter(instance):
    original = instance.exporter
    instance.exporter = original
    assert instance.exporter == original



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_targetNamespace_setter(instance):
    original = instance.targetNamespace
    instance.targetNamespace = original
    assert instance.targetNamespace == original



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_Definitions_strategy)
def test_bpmn2model_definitions_typeLanguage_setter(instance):
    original = instance.typeLanguage
    instance.typeLanguage = original
    assert instance.typeLanguage == original

@given(instance=BPMN2Model_DataStoreReference_strategy)
@settings(max_examples=50)
def test_bpmn2model_datastorereference_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataStoreReference)

@given(instance=BPMN2Model_DataStore_strategy)
@settings(max_examples=50)
def test_bpmn2model_datastore_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataStore)



@given(instance=BPMN2Model_DataStore_strategy)
def test_bpmn2model_datastore_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=BPMN2Model_DataStore_strategy)
def test_bpmn2model_datastore_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_DataStore_strategy)
def test_bpmn2model_datastore_isUnlimited_setter(instance):
    original = instance.isUnlimited
    instance.isUnlimited = original
    assert instance.isUnlimited == original

@given(instance=BPMN2Model_DataState_strategy)
@settings(max_examples=50)
def test_bpmn2model_datastate_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataState)



@given(instance=BPMN2Model_DataState_strategy)
def test_bpmn2model_datastate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ConversationAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_conversationassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ConversationAssociation)

@given(instance=BPMN2Model_Conversation_strategy)
@settings(max_examples=50)
def test_bpmn2model_conversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Conversation)

@given(instance=BPMN2Model_DataOutput_strategy)
@settings(max_examples=50)
def test_bpmn2model_dataoutput_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataOutput)



@given(instance=BPMN2Model_DataOutput_strategy)
def test_bpmn2model_dataoutput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original



@given(instance=BPMN2Model_DataOutput_strategy)
def test_bpmn2model_dataoutput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_DataObjectReference_strategy)
@settings(max_examples=50)
def test_bpmn2model_dataobjectreference_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataObjectReference)

@given(instance=BPMN2Model_DataObject_strategy)
@settings(max_examples=50)
def test_bpmn2model_dataobject_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataObject)



@given(instance=BPMN2Model_DataObject_strategy)
def test_bpmn2model_dataobject_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model_DataInputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_datainputassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataInputAssociation)

@given(instance=BPMN2Model_DataInput_strategy)
@settings(max_examples=50)
def test_bpmn2model_datainput_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataInput)



@given(instance=BPMN2Model_DataInput_strategy)
def test_bpmn2model_datainput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original



@given(instance=BPMN2Model_DataInput_strategy)
def test_bpmn2model_datainput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_DataAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model_dataassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DataAssociation)

@given(instance=BPMN2Model_CorrelationSubscription_strategy)
@settings(max_examples=50)
def test_bpmn2model_correlationsubscription_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CorrelationSubscription)

@given(instance=BPMN2Model_CorrelationPropertyRetrievalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model_correlationpropertyretrievalexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CorrelationPropertyRetrievalExpression)

@given(instance=BPMN2Model_CorrelationPropertyBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model_correlationpropertybinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CorrelationPropertyBinding)

@given(instance=BPMN2Model_CorrelationProperty_strategy)
@settings(max_examples=50)
def test_bpmn2model_correlationproperty_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CorrelationProperty)



@given(instance=BPMN2Model_CorrelationProperty_strategy)
def test_bpmn2model_correlationproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_CorrelationKey_strategy)
@settings(max_examples=50)
def test_bpmn2model_correlationkey_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CorrelationKey)



@given(instance=BPMN2Model_CorrelationKey_strategy)
def test_bpmn2model_correlationkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ConversationLink_strategy)
@settings(max_examples=50)
def test_bpmn2model_conversationlink_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ConversationLink)



@given(instance=BPMN2Model_ConversationLink_strategy)
def test_bpmn2model_conversationlink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_RootElement_strategy)
@settings(max_examples=50)
def test_bpmn2model_rootelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model_RootElement)

@given(instance=BPMN2Model_EventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_eventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EventDefinition)

@given(instance=BPMN2Model_ConditionalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_conditionaleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ConditionalEventDefinition)

@given(instance=BPMN2Model_ComplexGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model_complexgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ComplexGateway)

@given(instance=BPMN2Model_ComplexBehaviorDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_complexbehaviordefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ComplexBehaviorDefinition)

@given(instance=BPMN2Model_CompensateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_compensateeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CompensateEventDefinition)



@given(instance=BPMN2Model_CompensateEventDefinition_strategy)
def test_bpmn2model_compensateeventdefinition_waitForCompletion_setter(instance):
    original = instance.waitForCompletion
    instance.waitForCompletion = original
    assert instance.waitForCompletion == original

@given(instance=BPMN2Model_ChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_choreographytask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ChoreographyTask)

@given(instance=BPMN2Model_ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_bpmn2model_choreographyactivity_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ChoreographyActivity)



@given(instance=BPMN2Model_ChoreographyActivity_strategy)
def test_bpmn2model_choreographyactivity_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=BPMN2Model_Collaboration_strategy)
@settings(max_examples=50)
def test_bpmn2model_collaboration_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Collaboration)



@given(instance=BPMN2Model_Collaboration_strategy)
def test_bpmn2model_collaboration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_Collaboration_strategy)
def test_bpmn2model_collaboration_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=BPMN2Model_Choreography_strategy)
@settings(max_examples=50)
def test_bpmn2model_choreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Choreography)

@given(instance=BPMN2Model_CategoryValue_strategy)
@settings(max_examples=50)
def test_bpmn2model_categoryvalue_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CategoryValue)



@given(instance=BPMN2Model_CategoryValue_strategy)
def test_bpmn2model_categoryvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BPMN2Model_Category_strategy)
@settings(max_examples=50)
def test_bpmn2model_category_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Category)



@given(instance=BPMN2Model_Category_strategy)
def test_bpmn2model_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_CatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_catchevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CatchEvent)



@given(instance=BPMN2Model_CatchEvent_strategy)
def test_bpmn2model_catchevent_parallelMultiple_setter(instance):
    original = instance.parallelMultiple
    instance.parallelMultiple = original
    assert instance.parallelMultiple == original

@given(instance=BPMN2Model_FlowElement_strategy)
@settings(max_examples=50)
def test_bpmn2model_flowelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model_FlowElement)



@given(instance=BPMN2Model_FlowElement_strategy)
def test_bpmn2model_flowelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_AdHocSubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2model_adhocsubprocess_instantiation(instance):
    assert isinstance(instance, BPMN2Model_AdHocSubProcess)



@given(instance=BPMN2Model_AdHocSubProcess_strategy)
def test_bpmn2model_adhocsubprocess_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=BPMN2Model_AdHocSubProcess_strategy)
def test_bpmn2model_adhocsubprocess_cancelRemainingInstances_setter(instance):
    original = instance.cancelRemainingInstances
    instance.cancelRemainingInstances = original
    assert instance.cancelRemainingInstances == original

@given(instance=BPMN2Model_CancelEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_canceleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CancelEventDefinition)

@given(instance=BPMN2Model_ConversationNode_strategy)
@settings(max_examples=50)
def test_bpmn2model_conversationnode_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ConversationNode)



@given(instance=BPMN2Model_ConversationNode_strategy)
def test_bpmn2model_conversationnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_CallConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model_callconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CallConversation)

@given(instance=BPMN2Model_CallChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2model_callchoreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CallChoreography)

@given(instance=BPMN2Model_CallActivity_strategy)
@settings(max_examples=50)
def test_bpmn2model_callactivity_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CallActivity)

@given(instance=BPMN2Model_CallableElement_strategy)
@settings(max_examples=50)
def test_bpmn2model_callableelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model_CallableElement)



@given(instance=BPMN2Model_CallableElement_strategy)
def test_bpmn2model_callableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_BusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_businessruletask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_BusinessRuleTask)



@given(instance=BPMN2Model_BusinessRuleTask_strategy)
def test_bpmn2model_businessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_BoundaryEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model_boundaryevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model_BoundaryEvent)



@given(instance=BPMN2Model_BoundaryEvent_strategy)
def test_bpmn2model_boundaryevent_cancelActivity_setter(instance):
    original = instance.cancelActivity
    instance.cancelActivity = original
    assert instance.cancelActivity == original

@given(instance=BPMN2Model_Auditing_strategy)
@settings(max_examples=50)
def test_bpmn2model_auditing_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Auditing)

@given(instance=BPMN2Model_Association_strategy)
@settings(max_examples=50)
def test_bpmn2model_association_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Association)



@given(instance=BPMN2Model_Association_strategy)
def test_bpmn2model_association_associationDirection_setter(instance):
    original = instance.associationDirection
    instance.associationDirection = original
    assert instance.associationDirection == original

@given(instance=BPMN2Model_Assignment_strategy)
@settings(max_examples=50)
def test_bpmn2model_assignment_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Assignment)

@given(instance=BPMN2Model_Artifact_strategy)
@settings(max_examples=50)
def test_bpmn2model_artifact_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Artifact)

@given(instance=BPMN2Model_Activity_strategy)
@settings(max_examples=50)
def test_bpmn2model_activity_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Activity)



@given(instance=BPMN2Model_Activity_strategy)
def test_bpmn2model_activity_isForCompensation_setter(instance):
    original = instance.isForCompensation
    instance.isForCompensation = original
    assert instance.isForCompensation == original



@given(instance=BPMN2Model_Activity_strategy)
def test_bpmn2model_activity_startQuantity_setter(instance):
    original = instance.startQuantity
    instance.startQuantity = original
    assert instance.startQuantity == original



@given(instance=BPMN2Model_Activity_strategy)
def test_bpmn2model_activity_completionQuantity_setter(instance):
    original = instance.completionQuantity
    instance.completionQuantity = original
    assert instance.completionQuantity == original

@given(instance=BPMN2Model_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_bpmn2model_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, BPMN2Model_EStringToStringMapEntry)

@given(instance=BPMNBase_strategy)
@settings(max_examples=50)
def test_bpmnbase_instantiation(instance):
    assert isinstance(instance, BPMNBase)

@given(instance=BPMN2Model_InteractionNode_strategy)
@settings(max_examples=50)
def test_bpmn2model_interactionnode_instantiation(instance):
    assert isinstance(instance, BPMN2Model_InteractionNode)

@given(instance=BPMN2Model_Escalation_strategy)
@settings(max_examples=50)
def test_bpmn2model_escalation_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Escalation)



@given(instance=BPMN2Model_Escalation_strategy)
def test_bpmn2model_escalation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_Escalation_strategy)
def test_bpmn2model_escalation_escalationCode_setter(instance):
    original = instance.escalationCode
    instance.escalationCode = original
    assert instance.escalationCode == original

@given(instance=BPMN2Model_ResourceAssignmentExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model_resourceassignmentexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ResourceAssignmentExpression)

@given(instance=BPMN2Model_ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_extensiondefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ExtensionDefinition)



@given(instance=BPMN2Model_ExtensionDefinition_strategy)
def test_bpmn2model_extensiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model_ResourceParameterBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model_resourceparameterbinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ResourceParameterBinding)

@given(instance=BPMN2Model_ExtensionAttributeDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model_extensionattributedefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ExtensionAttributeDefinition)



@given(instance=BPMN2Model_ExtensionAttributeDefinition_strategy)
def test_bpmn2model_extensionattributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=BPMN2Model_ExtensionAttributeDefinition_strategy)
def test_bpmn2model_extensionattributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BPMN2Model_ExtensionAttributeDefinition_strategy)
def test_bpmn2model_extensionattributedefinition_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original

@given(instance=BPMN2Model_ExtensionAttributeValue_strategy)
@settings(max_examples=50)
def test_bpmn2model_extensionattributevalue_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ExtensionAttributeValue)



@given(instance=BPMN2Model_ExtensionAttributeValue_strategy)
def test_bpmn2model_extensionattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BPMN2Model_BaseElement_strategy)
@settings(max_examples=50)
def test_bpmn2model_baseelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model_BaseElement)



@given(instance=BPMN2Model_BaseElement_strategy)
def test_bpmn2model_baseelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=BPMN2Model_BaseElement_strategy)
def test_bpmn2model_baseelement_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=BPMN2Model_Extension_strategy)
@settings(max_examples=50)
def test_bpmn2model_extension_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Extension)



@given(instance=BPMN2Model_Extension_strategy)
def test_bpmn2model_extension_xsdDefinition_setter(instance):
    original = instance.xsdDefinition
    instance.xsdDefinition = original
    assert instance.xsdDefinition == original



@given(instance=BPMN2Model_Extension_strategy)
def test_bpmn2model_extension_mustUnderstand_setter(instance):
    original = instance.mustUnderstand
    instance.mustUnderstand = original
    assert instance.mustUnderstand == original

@given(instance=BPMN2Model_InputOutputBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model_inputoutputbinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model_InputOutputBinding)

@given(instance=BPMN2Model_ParticipantMultiplicity_strategy)
@settings(max_examples=50)
def test_bpmn2model_participantmultiplicity_instantiation(instance):
    assert isinstance(instance, BPMN2Model_ParticipantMultiplicity)



@given(instance=BPMN2Model_ParticipantMultiplicity_strategy)
def test_bpmn2model_participantmultiplicity_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=BPMN2Model_ParticipantMultiplicity_strategy)
def test_bpmn2model_participantmultiplicity_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=BPMN2Model_Import_strategy)
@settings(max_examples=50)
def test_bpmn2model_import_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Import)



@given(instance=BPMN2Model_Import_strategy)
def test_bpmn2model_import_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original



@given(instance=BPMN2Model_Import_strategy)
def test_bpmn2model_import_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=BPMN2Model_Import_strategy)
def test_bpmn2model_import_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=BPMN2Model_DocumentRoot_strategy)
@settings(max_examples=50)
def test_bpmn2model_documentroot_instantiation(instance):
    assert isinstance(instance, BPMN2Model_DocumentRoot)



@given(instance=BPMN2Model_DocumentRoot_strategy)
def test_bpmn2model_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=BPMN2Model_BPMNBase_strategy)
@settings(max_examples=50)
def test_bpmn2model_bpmnbase_instantiation(instance):
    assert isinstance(instance, BPMN2Model_BPMNBase)

@given(instance=HumanPerformer_strategy)
@settings(max_examples=50)
def test_humanperformer_instantiation(instance):
    assert isinstance(instance, HumanPerformer)

@given(instance=BPMN2Model_PotentialOwner_strategy)
@settings(max_examples=50)
def test_bpmn2model_potentialowner_instantiation(instance):
    assert isinstance(instance, BPMN2Model_PotentialOwner)

@given(instance=ResourceRole_strategy)
@settings(max_examples=50)
def test_resourcerole_instantiation(instance):
    assert isinstance(instance, ResourceRole)

@given(instance=BPMN2Model_Performer_strategy)
@settings(max_examples=50)
def test_bpmn2model_performer_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Performer)

@given(instance=LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, LoopCharacteristics)

@given(instance=BPMN2Model_StandardLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model_standardloopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model_StandardLoopCharacteristics)



@given(instance=BPMN2Model_StandardLoopCharacteristics_strategy)
def test_bpmn2model_standardloopcharacteristics_testBefore_setter(instance):
    original = instance.testBefore
    instance.testBefore = original
    assert instance.testBefore == original

@given(instance=BPMN2Model_MultiInstanceLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model_multiinstanceloopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model_MultiInstanceLoopCharacteristics)



@given(instance=BPMN2Model_MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model_multiinstanceloopcharacteristics_isSequential_setter(instance):
    original = instance.isSequential
    instance.isSequential = original
    assert instance.isSequential == original



@given(instance=BPMN2Model_MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model_multiinstanceloopcharacteristics_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=Performer_strategy)
@settings(max_examples=50)
def test_performer_instantiation(instance):
    assert isinstance(instance, Performer)

@given(instance=BPMN2Model_HumanPerformer_strategy)
@settings(max_examples=50)
def test_bpmn2model_humanperformer_instantiation(instance):
    assert isinstance(instance, BPMN2Model_HumanPerformer)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=BPMN2Model_Process_strategy)
@settings(max_examples=50)
def test_bpmn2model_process_instantiation(instance):
    assert isinstance(instance, BPMN2Model_Process)



@given(instance=BPMN2Model_Process_strategy)
def test_bpmn2model_process_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original



@given(instance=BPMN2Model_Process_strategy)
def test_bpmn2model_process_processType_setter(instance):
    original = instance.processType
    instance.processType = original
    assert instance.processType == original



@given(instance=BPMN2Model_Process_strategy)
def test_bpmn2model_process_isExecutable_setter(instance):
    original = instance.isExecutable
    instance.isExecutable = original
    assert instance.isExecutable == original

@given(instance=BPMN2Model_GlobalTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globaltask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalTask)

@given(instance=Choreography_strategy)
@settings(max_examples=50)
def test_choreography_instantiation(instance):
    assert isinstance(instance, Choreography)

@given(instance=BPMN2Model_GlobalChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalchoreographytask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalChoreographyTask)

@given(instance=GlobalTask_strategy)
@settings(max_examples=50)
def test_globaltask_instantiation(instance):
    assert isinstance(instance, GlobalTask)

@given(instance=BPMN2Model_GlobalScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalscripttask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalScriptTask)



@given(instance=BPMN2Model_GlobalScriptTask_strategy)
def test_bpmn2model_globalscripttask_scriptLanguage_setter(instance):
    original = instance.scriptLanguage
    instance.scriptLanguage = original
    assert instance.scriptLanguage == original



@given(instance=BPMN2Model_GlobalScriptTask_strategy)
def test_bpmn2model_globalscripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=BPMN2Model_GlobalBusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalbusinessruletask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalBusinessRuleTask)



@given(instance=BPMN2Model_GlobalBusinessRuleTask_strategy)
def test_bpmn2model_globalbusinessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_GlobalUserTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalusertask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalUserTask)



@given(instance=BPMN2Model_GlobalUserTask_strategy)
def test_bpmn2model_globalusertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model_GlobalManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2model_globalmanualtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model_GlobalManualTask)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=BPMN2Model_FormalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model_formalexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model_FormalExpression)



@given(instance=BPMN2Model_FormalExpression_strategy)
def test_bpmn2model_formalexpression_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=BPMN2Model_FormalExpression_strategy)
def test_bpmn2model_formalexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=BPMN2Model_FormalExpression_strategy)
def test_bpmn2model_formalexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original
