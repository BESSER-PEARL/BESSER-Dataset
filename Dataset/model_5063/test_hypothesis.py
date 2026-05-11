import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
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
    SubProcess,
    BPMN2Model::ThrowEvent,
    FlowNode,
    BPMN2Model::UserTask,
    BPMN2Model::Transaction,
    BPMN2Model::TimerEventDefinition,
    BPMN2Model::StartEvent,
    BPMN2Model::TextAnnotation,
    BPMN2Model::TerminateEventDefinition,
    BPMN2Model::SubProcess,
    BPMN2Model::SubConversation,
    BPMN2Model::SubChoreography,
    BPMN2Model::EObject,
    BPMN2Model::SignalEventDefinition,
    BPMN2Model::Signal,
    BPMN2Model::ServiceTask,
    BPMN2Model::SendTask,
    BPMN2Model::ScriptTask,
    BPMN2Model::ResourceParameter,
    BPMN2Model::Resource,
    BPMN2Model::Rendering,
    BPMN2Model::Relationship,
    BPMN2Model::ReceiveTask,
    BPMN2Model::PartnerRole,
    BPMN2Model::PartnerEntity,
    BPMN2Model::MessageEventDefinition,
    BPMN2Model::ParticipantAssociation,
    BPMN2Model::ParallelGateway,
    BPMN2Model::OutputSet,
    BPMN2Model::Operation,
    BPMN2Model::Monitoring,
    BPMN2Model::MessageFlowAssociation,
    BPMN2Model::MessageFlow,
    BPMN2Model::IntermediateCatchEvent,
    BPMN2Model::Message,
    BPMN2Model::ManualTask,
    BPMN2Model::LoopCharacteristics,
    BPMN2Model::LinkEventDefinition,
    BPMN2Model::LaneSet,
    BPMN2Model::Lane,
    BPMN2Model::ItemDefinition,
    BPMN2Model::InputOutputSpecification,
    BPMN2Model::Interface,
    BPMN2Model::InputSet,
    BPMN2Model::InclusiveGateway,
    BPMN2Model::ResourceRole,
    BPMN2Model::Group,
    BPMN2Model::ExclusiveGateway,
    BPMN2Model::GlobalConversation,
    BPMN2Model::Gateway,
    BPMN2Model::Expression,
    BPMN2Model::EventBasedGateway,
    BPMN2Model::EscalationEventDefinition,
    BPMN2Model::ErrorEventDefinition,
    BPMN2Model::Error,
    BPMN2Model::EndPoint,
    BPMN2Model::Documentation,
    BPMN2Model::Definitions,
    BPMN2Model::DataState,
    BPMN2Model::ConversationAssociation,
    BPMN2Model::Conversation,
    BPMN2Model::DataAssociation,
    BPMN2Model::CorrelationSubscription,
    BPMN2Model::CorrelationPropertyRetrievalExpression,
    BPMN2Model::CorrelationPropertyBinding,
    BPMN2Model::CorrelationProperty,
    BPMN2Model::CorrelationKey,
    BPMN2Model::ConversationLink,
    BPMN2Model::RootElement,
    BPMN2Model::EventDefinition,
    BPMN2Model::ConditionalEventDefinition,
    BPMN2Model::ComplexGateway,
    BPMN2Model::ComplexBehaviorDefinition,
    BPMN2Model::CompensateEventDefinition,
    BPMN2Model::ChoreographyTask,
    BPMN2Model::ChoreographyActivity,
    BPMN2Model::Collaboration,
    BPMN2Model::Choreography,
    BPMN2Model::CategoryValue,
    BPMN2Model::Category,
    BPMN2Model::CatchEvent,
    BPMN2Model::FlowElement,
    BPMN2Model::AdHocSubProcess,
    BPMN2Model::CancelEventDefinition,
    BPMN2Model::CallConversation,
    BPMN2Model::CallChoreography,
    BPMN2Model::CallActivity,
    BPMN2Model::CallableElement,
    BPMN2Model::BusinessRuleTask,
    BPMN2Model::BoundaryEvent,
    BPMN2Model::Auditing,
    BPMN2Model::Association,
    BPMN2Model::Assignment,
    BPMN2Model::Artifact,
    BPMN2Model::Activity,
    BPMN2Model::EStringToStringMapEntry,
    BPMNBase,
    BPMN2Model::ResourceParameterBinding,
    BPMN2Model::InteractionNode,
    BPMN2Model::BaseElement,
    BPMN2Model::ParticipantMultiplicity,
    BPMN2Model::ExtensionDefinition,
    BPMN2Model::InputOutputBinding,
    BPMN2Model::ResourceAssignmentExpression,
    BPMN2Model::Escalation,
    BPMN2Model::Import,
    BPMN2Model::ExtensionAttributeValue,
    BPMN2Model::Extension,
    BPMN2Model::DocumentRoot,
    EObject,
    BPMN2Model::BPMNBase,
    HumanPerformer,
    BPMN2Model::PotentialOwner,
    ResourceRole,
    BPMN2Model::Performer,
    LoopCharacteristics,
    BPMN2Model::MultiInstanceLoopCharacteristics,
    BPMN2Model::StandardLoopCharacteristics,
    Performer,
    BPMN2Model::HumanPerformer,
    CallableElement,
    BPMN2Model::Process,
    BPMN2Model::GlobalTask,
    Choreography,
    BPMN2Model::GlobalChoreographyTask,
    GlobalTask,
    BPMN2Model::GlobalUserTask,
    BPMN2Model::GlobalScriptTask,
    BPMN2Model::GlobalManualTask,
    BPMN2Model::GlobalBusinessRuleTask,
    Expression,
    BPMN2Model::FormalExpression,
    BPMN2Model::FlowElementsContainer,
    BPMN2Model::ExtensionAttributeDefinition,
    ThrowEvent,
    BPMN2Model::IntermediateThrowEvent,
    BPMN2Model::ImplicitThrowEvent,
    BPMN2Model::EndEvent,
    FlowElement,
    BPMN2Model::SequenceFlow,
    BPMN2Model::FlowNode,
    DataAssociation,
    BPMN2Model::DataInputAssociation,
    BPMN2Model::DataOutputAssociation,
    ItemAwareElement,
    BPMN2Model::DataInput,
    BPMN2Model::DataObjectReference,
    BPMN2Model::DataStoreReference,
    BPMN2Model::Property,
    BPMN2Model::DataStore,
    BPMN2Model::DataOutput,
    BPMN2Model::DataObject,
    BPMN2Model::ItemAwareElement,
    InteractionNode,
    BPMN2Model::Task,
    BPMN2Model::ConversationNode,
    BPMN2Model::Event,
    BPMN2Model::Participant,
    RelationshipDirection,
    AssociationDirection,
    EventBasedGatewayType,
    ProcessType,
    GatewayDirection,
    ChoreographyLoopType,
    MultiInstanceBehavior,
    AdHocOrdering,
    ItemKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_subprocess_is_not_abstract():
    assert not inspect.isabstract(SubProcess)


def test_subprocess_constructor_exists():
    assert callable(SubProcess.__init__)


def test_subprocess_constructor_args():
    sig = inspect.signature(SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::throwevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ThrowEvent)


def test_bpmn2model::throwevent_constructor_exists():
    assert callable(BPMN2Model::ThrowEvent.__init__)


def test_bpmn2model::throwevent_constructor_args():
    sig = inspect.signature(BPMN2Model::ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_flownode_is_not_abstract():
    assert not inspect.isabstract(FlowNode)


def test_flownode_constructor_exists():
    assert callable(FlowNode.__init__)


def test_flownode_constructor_args():
    sig = inspect.signature(FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::usertask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::UserTask)


def test_bpmn2model::usertask_constructor_exists():
    assert callable(BPMN2Model::UserTask.__init__)


def test_bpmn2model::usertask_constructor_args():
    sig = inspect.signature(BPMN2Model::UserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::usertask_has_implementation():
    assert hasattr(BPMN2Model::UserTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::UserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::transaction_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Transaction)


def test_bpmn2model::transaction_constructor_exists():
    assert callable(BPMN2Model::Transaction.__init__)


def test_bpmn2model::transaction_constructor_args():
    sig = inspect.signature(BPMN2Model::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "method" in params, "Missing parameter 'method'"

def test_bpmn2model::transaction_has_protocol():
    assert hasattr(BPMN2Model::Transaction, "protocol")
    descriptor = None
    for klass in BPMN2Model::Transaction.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::transaction_has_method():
    assert hasattr(BPMN2Model::Transaction, "method")
    descriptor = None
    for klass in BPMN2Model::Transaction.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::timereventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::TimerEventDefinition)


def test_bpmn2model::timereventdefinition_constructor_exists():
    assert callable(BPMN2Model::TimerEventDefinition.__init__)


def test_bpmn2model::timereventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::TimerEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::startevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::StartEvent)


def test_bpmn2model::startevent_constructor_exists():
    assert callable(BPMN2Model::StartEvent.__init__)


def test_bpmn2model::startevent_constructor_args():
    sig = inspect.signature(BPMN2Model::StartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isInterrupting" in params, "Missing parameter 'isInterrupting'"

def test_bpmn2model::startevent_has_isInterrupting():
    assert hasattr(BPMN2Model::StartEvent, "isInterrupting")
    descriptor = None
    for klass in BPMN2Model::StartEvent.__mro__:
        if "isInterrupting" in klass.__dict__:
            descriptor = klass.__dict__["isInterrupting"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::textannotation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::TextAnnotation)


def test_bpmn2model::textannotation_constructor_exists():
    assert callable(BPMN2Model::TextAnnotation.__init__)


def test_bpmn2model::textannotation_constructor_args():
    sig = inspect.signature(BPMN2Model::TextAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "textFormat" in params, "Missing parameter 'textFormat'"

def test_bpmn2model::textannotation_has_text():
    assert hasattr(BPMN2Model::TextAnnotation, "text")
    descriptor = None
    for klass in BPMN2Model::TextAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::textannotation_has_textFormat():
    assert hasattr(BPMN2Model::TextAnnotation, "textFormat")
    descriptor = None
    for klass in BPMN2Model::TextAnnotation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::terminateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::TerminateEventDefinition)


def test_bpmn2model::terminateeventdefinition_constructor_exists():
    assert callable(BPMN2Model::TerminateEventDefinition.__init__)


def test_bpmn2model::terminateeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::TerminateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::subprocess_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SubProcess)


def test_bpmn2model::subprocess_constructor_exists():
    assert callable(BPMN2Model::SubProcess.__init__)


def test_bpmn2model::subprocess_constructor_args():
    sig = inspect.signature(BPMN2Model::SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "triggeredByEvent" in params, "Missing parameter 'triggeredByEvent'"

def test_bpmn2model::subprocess_has_triggeredByEvent():
    assert hasattr(BPMN2Model::SubProcess, "triggeredByEvent")
    descriptor = None
    for klass in BPMN2Model::SubProcess.__mro__:
        if "triggeredByEvent" in klass.__dict__:
            descriptor = klass.__dict__["triggeredByEvent"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::subconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SubConversation)


def test_bpmn2model::subconversation_constructor_exists():
    assert callable(BPMN2Model::SubConversation.__init__)


def test_bpmn2model::subconversation_constructor_args():
    sig = inspect.signature(BPMN2Model::SubConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::subchoreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SubChoreography)


def test_bpmn2model::subchoreography_constructor_exists():
    assert callable(BPMN2Model::SubChoreography.__init__)


def test_bpmn2model::subchoreography_constructor_args():
    sig = inspect.signature(BPMN2Model::SubChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::eobject_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EObject)


def test_bpmn2model::eobject_constructor_exists():
    assert callable(BPMN2Model::EObject.__init__)


def test_bpmn2model::eobject_constructor_args():
    sig = inspect.signature(BPMN2Model::EObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::signaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SignalEventDefinition)


def test_bpmn2model::signaleventdefinition_constructor_exists():
    assert callable(BPMN2Model::SignalEventDefinition.__init__)


def test_bpmn2model::signaleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::SignalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::signal_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Signal)


def test_bpmn2model::signal_constructor_exists():
    assert callable(BPMN2Model::Signal.__init__)


def test_bpmn2model::signal_constructor_args():
    sig = inspect.signature(BPMN2Model::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::signal_has_name():
    assert hasattr(BPMN2Model::Signal, "name")
    descriptor = None
    for klass in BPMN2Model::Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::servicetask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ServiceTask)


def test_bpmn2model::servicetask_constructor_exists():
    assert callable(BPMN2Model::ServiceTask.__init__)


def test_bpmn2model::servicetask_constructor_args():
    sig = inspect.signature(BPMN2Model::ServiceTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::servicetask_has_implementation():
    assert hasattr(BPMN2Model::ServiceTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::ServiceTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::sendtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SendTask)


def test_bpmn2model::sendtask_constructor_exists():
    assert callable(BPMN2Model::SendTask.__init__)


def test_bpmn2model::sendtask_constructor_args():
    sig = inspect.signature(BPMN2Model::SendTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::sendtask_has_implementation():
    assert hasattr(BPMN2Model::SendTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::SendTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::scripttask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ScriptTask)


def test_bpmn2model::scripttask_constructor_exists():
    assert callable(BPMN2Model::ScriptTask.__init__)


def test_bpmn2model::scripttask_constructor_args():
    sig = inspect.signature(BPMN2Model::ScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "scriptFormat" in params, "Missing parameter 'scriptFormat'"
    assert "script" in params, "Missing parameter 'script'"

def test_bpmn2model::scripttask_has_scriptFormat():
    assert hasattr(BPMN2Model::ScriptTask, "scriptFormat")
    descriptor = None
    for klass in BPMN2Model::ScriptTask.__mro__:
        if "scriptFormat" in klass.__dict__:
            descriptor = klass.__dict__["scriptFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::scripttask_has_script():
    assert hasattr(BPMN2Model::ScriptTask, "script")
    descriptor = None
    for klass in BPMN2Model::ScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::resourceparameter_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ResourceParameter)


def test_bpmn2model::resourceparameter_constructor_exists():
    assert callable(BPMN2Model::ResourceParameter.__init__)


def test_bpmn2model::resourceparameter_constructor_args():
    sig = inspect.signature(BPMN2Model::ResourceParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::resourceparameter_has_isRequired():
    assert hasattr(BPMN2Model::ResourceParameter, "isRequired")
    descriptor = None
    for klass in BPMN2Model::ResourceParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::resourceparameter_has_name():
    assert hasattr(BPMN2Model::ResourceParameter, "name")
    descriptor = None
    for klass in BPMN2Model::ResourceParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::resource_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Resource)


def test_bpmn2model::resource_constructor_exists():
    assert callable(BPMN2Model::Resource.__init__)


def test_bpmn2model::resource_constructor_args():
    sig = inspect.signature(BPMN2Model::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::resource_has_name():
    assert hasattr(BPMN2Model::Resource, "name")
    descriptor = None
    for klass in BPMN2Model::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::rendering_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Rendering)


def test_bpmn2model::rendering_constructor_exists():
    assert callable(BPMN2Model::Rendering.__init__)


def test_bpmn2model::rendering_constructor_args():
    sig = inspect.signature(BPMN2Model::Rendering.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::relationship_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Relationship)


def test_bpmn2model::relationship_constructor_exists():
    assert callable(BPMN2Model::Relationship.__init__)


def test_bpmn2model::relationship_constructor_args():
    sig = inspect.signature(BPMN2Model::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "type" in params, "Missing parameter 'type'"

def test_bpmn2model::relationship_has_direction():
    assert hasattr(BPMN2Model::Relationship, "direction")
    descriptor = None
    for klass in BPMN2Model::Relationship.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::relationship_has_type():
    assert hasattr(BPMN2Model::Relationship, "type")
    descriptor = None
    for klass in BPMN2Model::Relationship.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::receivetask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ReceiveTask)


def test_bpmn2model::receivetask_constructor_exists():
    assert callable(BPMN2Model::ReceiveTask.__init__)


def test_bpmn2model::receivetask_constructor_args():
    sig = inspect.signature(BPMN2Model::ReceiveTask.__init__)
    params = list(sig.parameters.keys())
    assert "instantiate" in params, "Missing parameter 'instantiate'"
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::receivetask_has_instantiate():
    assert hasattr(BPMN2Model::ReceiveTask, "instantiate")
    descriptor = None
    for klass in BPMN2Model::ReceiveTask.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::receivetask_has_implementation():
    assert hasattr(BPMN2Model::ReceiveTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::ReceiveTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::partnerrole_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::PartnerRole)


def test_bpmn2model::partnerrole_constructor_exists():
    assert callable(BPMN2Model::PartnerRole.__init__)


def test_bpmn2model::partnerrole_constructor_args():
    sig = inspect.signature(BPMN2Model::PartnerRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::partnerrole_has_name():
    assert hasattr(BPMN2Model::PartnerRole, "name")
    descriptor = None
    for klass in BPMN2Model::PartnerRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::partnerentity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::PartnerEntity)


def test_bpmn2model::partnerentity_constructor_exists():
    assert callable(BPMN2Model::PartnerEntity.__init__)


def test_bpmn2model::partnerentity_constructor_args():
    sig = inspect.signature(BPMN2Model::PartnerEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::partnerentity_has_name():
    assert hasattr(BPMN2Model::PartnerEntity, "name")
    descriptor = None
    for klass in BPMN2Model::PartnerEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::messageeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::MessageEventDefinition)


def test_bpmn2model::messageeventdefinition_constructor_exists():
    assert callable(BPMN2Model::MessageEventDefinition.__init__)


def test_bpmn2model::messageeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::MessageEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::participantassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ParticipantAssociation)


def test_bpmn2model::participantassociation_constructor_exists():
    assert callable(BPMN2Model::ParticipantAssociation.__init__)


def test_bpmn2model::participantassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::ParticipantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::parallelgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ParallelGateway)


def test_bpmn2model::parallelgateway_constructor_exists():
    assert callable(BPMN2Model::ParallelGateway.__init__)


def test_bpmn2model::parallelgateway_constructor_args():
    sig = inspect.signature(BPMN2Model::ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::outputset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::OutputSet)


def test_bpmn2model::outputset_constructor_exists():
    assert callable(BPMN2Model::OutputSet.__init__)


def test_bpmn2model::outputset_constructor_args():
    sig = inspect.signature(BPMN2Model::OutputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::outputset_has_name():
    assert hasattr(BPMN2Model::OutputSet, "name")
    descriptor = None
    for klass in BPMN2Model::OutputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::operation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Operation)


def test_bpmn2model::operation_constructor_exists():
    assert callable(BPMN2Model::Operation.__init__)


def test_bpmn2model::operation_constructor_args():
    sig = inspect.signature(BPMN2Model::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::operation_has_name():
    assert hasattr(BPMN2Model::Operation, "name")
    descriptor = None
    for klass in BPMN2Model::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::monitoring_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Monitoring)


def test_bpmn2model::monitoring_constructor_exists():
    assert callable(BPMN2Model::Monitoring.__init__)


def test_bpmn2model::monitoring_constructor_args():
    sig = inspect.signature(BPMN2Model::Monitoring.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::messageflowassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::MessageFlowAssociation)


def test_bpmn2model::messageflowassociation_constructor_exists():
    assert callable(BPMN2Model::MessageFlowAssociation.__init__)


def test_bpmn2model::messageflowassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::MessageFlowAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::messageflow_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::MessageFlow)


def test_bpmn2model::messageflow_constructor_exists():
    assert callable(BPMN2Model::MessageFlow.__init__)


def test_bpmn2model::messageflow_constructor_args():
    sig = inspect.signature(BPMN2Model::MessageFlow.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::messageflow_has_name():
    assert hasattr(BPMN2Model::MessageFlow, "name")
    descriptor = None
    for klass in BPMN2Model::MessageFlow.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::intermediatecatchevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::IntermediateCatchEvent)


def test_bpmn2model::intermediatecatchevent_constructor_exists():
    assert callable(BPMN2Model::IntermediateCatchEvent.__init__)


def test_bpmn2model::intermediatecatchevent_constructor_args():
    sig = inspect.signature(BPMN2Model::IntermediateCatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::message_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Message)


def test_bpmn2model::message_constructor_exists():
    assert callable(BPMN2Model::Message.__init__)


def test_bpmn2model::message_constructor_args():
    sig = inspect.signature(BPMN2Model::Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::message_has_name():
    assert hasattr(BPMN2Model::Message, "name")
    descriptor = None
    for klass in BPMN2Model::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::manualtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ManualTask)


def test_bpmn2model::manualtask_constructor_exists():
    assert callable(BPMN2Model::ManualTask.__init__)


def test_bpmn2model::manualtask_constructor_args():
    sig = inspect.signature(BPMN2Model::ManualTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::LoopCharacteristics)


def test_bpmn2model::loopcharacteristics_constructor_exists():
    assert callable(BPMN2Model::LoopCharacteristics.__init__)


def test_bpmn2model::loopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model::LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::linkeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::LinkEventDefinition)


def test_bpmn2model::linkeventdefinition_constructor_exists():
    assert callable(BPMN2Model::LinkEventDefinition.__init__)


def test_bpmn2model::linkeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::LinkEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::linkeventdefinition_has_name():
    assert hasattr(BPMN2Model::LinkEventDefinition, "name")
    descriptor = None
    for klass in BPMN2Model::LinkEventDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::laneset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::LaneSet)


def test_bpmn2model::laneset_constructor_exists():
    assert callable(BPMN2Model::LaneSet.__init__)


def test_bpmn2model::laneset_constructor_args():
    sig = inspect.signature(BPMN2Model::LaneSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::laneset_has_name():
    assert hasattr(BPMN2Model::LaneSet, "name")
    descriptor = None
    for klass in BPMN2Model::LaneSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::lane_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Lane)


def test_bpmn2model::lane_constructor_exists():
    assert callable(BPMN2Model::Lane.__init__)


def test_bpmn2model::lane_constructor_args():
    sig = inspect.signature(BPMN2Model::Lane.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::lane_has_name():
    assert hasattr(BPMN2Model::Lane, "name")
    descriptor = None
    for klass in BPMN2Model::Lane.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::itemdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ItemDefinition)


def test_bpmn2model::itemdefinition_constructor_exists():
    assert callable(BPMN2Model::ItemDefinition.__init__)


def test_bpmn2model::itemdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ItemDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "itemKind" in params, "Missing parameter 'itemKind'"

def test_bpmn2model::itemdefinition_has_isCollection():
    assert hasattr(BPMN2Model::ItemDefinition, "isCollection")
    descriptor = None
    for klass in BPMN2Model::ItemDefinition.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::itemdefinition_has_itemKind():
    assert hasattr(BPMN2Model::ItemDefinition, "itemKind")
    descriptor = None
    for klass in BPMN2Model::ItemDefinition.__mro__:
        if "itemKind" in klass.__dict__:
            descriptor = klass.__dict__["itemKind"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::inputoutputspecification_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::InputOutputSpecification)


def test_bpmn2model::inputoutputspecification_constructor_exists():
    assert callable(BPMN2Model::InputOutputSpecification.__init__)


def test_bpmn2model::inputoutputspecification_constructor_args():
    sig = inspect.signature(BPMN2Model::InputOutputSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::interface_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Interface)


def test_bpmn2model::interface_constructor_exists():
    assert callable(BPMN2Model::Interface.__init__)


def test_bpmn2model::interface_constructor_args():
    sig = inspect.signature(BPMN2Model::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::interface_has_name():
    assert hasattr(BPMN2Model::Interface, "name")
    descriptor = None
    for klass in BPMN2Model::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::inputset_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::InputSet)


def test_bpmn2model::inputset_constructor_exists():
    assert callable(BPMN2Model::InputSet.__init__)


def test_bpmn2model::inputset_constructor_args():
    sig = inspect.signature(BPMN2Model::InputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::inputset_has_name():
    assert hasattr(BPMN2Model::InputSet, "name")
    descriptor = None
    for klass in BPMN2Model::InputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::inclusivegateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::InclusiveGateway)


def test_bpmn2model::inclusivegateway_constructor_exists():
    assert callable(BPMN2Model::InclusiveGateway.__init__)


def test_bpmn2model::inclusivegateway_constructor_args():
    sig = inspect.signature(BPMN2Model::InclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::resourcerole_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ResourceRole)


def test_bpmn2model::resourcerole_constructor_exists():
    assert callable(BPMN2Model::ResourceRole.__init__)


def test_bpmn2model::resourcerole_constructor_args():
    sig = inspect.signature(BPMN2Model::ResourceRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::resourcerole_has_name():
    assert hasattr(BPMN2Model::ResourceRole, "name")
    descriptor = None
    for klass in BPMN2Model::ResourceRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::group_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Group)


def test_bpmn2model::group_constructor_exists():
    assert callable(BPMN2Model::Group.__init__)


def test_bpmn2model::group_constructor_args():
    sig = inspect.signature(BPMN2Model::Group.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::exclusivegateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ExclusiveGateway)


def test_bpmn2model::exclusivegateway_constructor_exists():
    assert callable(BPMN2Model::ExclusiveGateway.__init__)


def test_bpmn2model::exclusivegateway_constructor_args():
    sig = inspect.signature(BPMN2Model::ExclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::globalconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalConversation)


def test_bpmn2model::globalconversation_constructor_exists():
    assert callable(BPMN2Model::GlobalConversation.__init__)


def test_bpmn2model::globalconversation_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::gateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Gateway)


def test_bpmn2model::gateway_constructor_exists():
    assert callable(BPMN2Model::Gateway.__init__)


def test_bpmn2model::gateway_constructor_args():
    sig = inspect.signature(BPMN2Model::Gateway.__init__)
    params = list(sig.parameters.keys())
    assert "gatewayDirection" in params, "Missing parameter 'gatewayDirection'"

def test_bpmn2model::gateway_has_gatewayDirection():
    assert hasattr(BPMN2Model::Gateway, "gatewayDirection")
    descriptor = None
    for klass in BPMN2Model::Gateway.__mro__:
        if "gatewayDirection" in klass.__dict__:
            descriptor = klass.__dict__["gatewayDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::expression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Expression)


def test_bpmn2model::expression_constructor_exists():
    assert callable(BPMN2Model::Expression.__init__)


def test_bpmn2model::expression_constructor_args():
    sig = inspect.signature(BPMN2Model::Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::eventbasedgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EventBasedGateway)


def test_bpmn2model::eventbasedgateway_constructor_exists():
    assert callable(BPMN2Model::EventBasedGateway.__init__)


def test_bpmn2model::eventbasedgateway_constructor_args():
    sig = inspect.signature(BPMN2Model::EventBasedGateway.__init__)
    params = list(sig.parameters.keys())
    assert "eventGatewayType" in params, "Missing parameter 'eventGatewayType'"
    assert "instantiate" in params, "Missing parameter 'instantiate'"

def test_bpmn2model::eventbasedgateway_has_eventGatewayType():
    assert hasattr(BPMN2Model::EventBasedGateway, "eventGatewayType")
    descriptor = None
    for klass in BPMN2Model::EventBasedGateway.__mro__:
        if "eventGatewayType" in klass.__dict__:
            descriptor = klass.__dict__["eventGatewayType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::eventbasedgateway_has_instantiate():
    assert hasattr(BPMN2Model::EventBasedGateway, "instantiate")
    descriptor = None
    for klass in BPMN2Model::EventBasedGateway.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::escalationeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EscalationEventDefinition)


def test_bpmn2model::escalationeventdefinition_constructor_exists():
    assert callable(BPMN2Model::EscalationEventDefinition.__init__)


def test_bpmn2model::escalationeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::EscalationEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::erroreventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ErrorEventDefinition)


def test_bpmn2model::erroreventdefinition_constructor_exists():
    assert callable(BPMN2Model::ErrorEventDefinition.__init__)


def test_bpmn2model::erroreventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ErrorEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::error_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Error)


def test_bpmn2model::error_constructor_exists():
    assert callable(BPMN2Model::Error.__init__)


def test_bpmn2model::error_constructor_args():
    sig = inspect.signature(BPMN2Model::Error.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_bpmn2model::error_has_name():
    assert hasattr(BPMN2Model::Error, "name")
    descriptor = None
    for klass in BPMN2Model::Error.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::error_has_errorCode():
    assert hasattr(BPMN2Model::Error, "errorCode")
    descriptor = None
    for klass in BPMN2Model::Error.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::endpoint_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EndPoint)


def test_bpmn2model::endpoint_constructor_exists():
    assert callable(BPMN2Model::EndPoint.__init__)


def test_bpmn2model::endpoint_constructor_args():
    sig = inspect.signature(BPMN2Model::EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::documentation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Documentation)


def test_bpmn2model::documentation_constructor_exists():
    assert callable(BPMN2Model::Documentation.__init__)


def test_bpmn2model::documentation_constructor_args():
    sig = inspect.signature(BPMN2Model::Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "textFormat" in params, "Missing parameter 'textFormat'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "text" in params, "Missing parameter 'text'"

def test_bpmn2model::documentation_has_textFormat():
    assert hasattr(BPMN2Model::Documentation, "textFormat")
    descriptor = None
    for klass in BPMN2Model::Documentation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::documentation_has_mixed():
    assert hasattr(BPMN2Model::Documentation, "mixed")
    descriptor = None
    for klass in BPMN2Model::Documentation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::documentation_has_text():
    assert hasattr(BPMN2Model::Documentation, "text")
    descriptor = None
    for klass in BPMN2Model::Documentation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::definitions_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Definitions)


def test_bpmn2model::definitions_constructor_exists():
    assert callable(BPMN2Model::Definitions.__init__)


def test_bpmn2model::definitions_constructor_args():
    sig = inspect.signature(BPMN2Model::Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "typeLanguage" in params, "Missing parameter 'typeLanguage'"
    assert "expressionLanguage" in params, "Missing parameter 'expressionLanguage'"
    assert "name" in params, "Missing parameter 'name'"
    assert "exporter" in params, "Missing parameter 'exporter'"
    assert "targetNamespace" in params, "Missing parameter 'targetNamespace'"
    assert "exporterVersion" in params, "Missing parameter 'exporterVersion'"

def test_bpmn2model::definitions_has_typeLanguage():
    assert hasattr(BPMN2Model::Definitions, "typeLanguage")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "typeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["typeLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::definitions_has_expressionLanguage():
    assert hasattr(BPMN2Model::Definitions, "expressionLanguage")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "expressionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::definitions_has_name():
    assert hasattr(BPMN2Model::Definitions, "name")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::definitions_has_exporter():
    assert hasattr(BPMN2Model::Definitions, "exporter")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "exporter" in klass.__dict__:
            descriptor = klass.__dict__["exporter"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::definitions_has_targetNamespace():
    assert hasattr(BPMN2Model::Definitions, "targetNamespace")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "targetNamespace" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::definitions_has_exporterVersion():
    assert hasattr(BPMN2Model::Definitions, "exporterVersion")
    descriptor = None
    for klass in BPMN2Model::Definitions.__mro__:
        if "exporterVersion" in klass.__dict__:
            descriptor = klass.__dict__["exporterVersion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::datastate_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataState)


def test_bpmn2model::datastate_constructor_exists():
    assert callable(BPMN2Model::DataState.__init__)


def test_bpmn2model::datastate_constructor_args():
    sig = inspect.signature(BPMN2Model::DataState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::datastate_has_name():
    assert hasattr(BPMN2Model::DataState, "name")
    descriptor = None
    for klass in BPMN2Model::DataState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::conversationassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ConversationAssociation)


def test_bpmn2model::conversationassociation_constructor_exists():
    assert callable(BPMN2Model::ConversationAssociation.__init__)


def test_bpmn2model::conversationassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::ConversationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::conversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Conversation)


def test_bpmn2model::conversation_constructor_exists():
    assert callable(BPMN2Model::Conversation.__init__)


def test_bpmn2model::conversation_constructor_args():
    sig = inspect.signature(BPMN2Model::Conversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::dataassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataAssociation)


def test_bpmn2model::dataassociation_constructor_exists():
    assert callable(BPMN2Model::DataAssociation.__init__)


def test_bpmn2model::dataassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::correlationsubscription_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CorrelationSubscription)


def test_bpmn2model::correlationsubscription_constructor_exists():
    assert callable(BPMN2Model::CorrelationSubscription.__init__)


def test_bpmn2model::correlationsubscription_constructor_args():
    sig = inspect.signature(BPMN2Model::CorrelationSubscription.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::correlationpropertyretrievalexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CorrelationPropertyRetrievalExpression)


def test_bpmn2model::correlationpropertyretrievalexpression_constructor_exists():
    assert callable(BPMN2Model::CorrelationPropertyRetrievalExpression.__init__)


def test_bpmn2model::correlationpropertyretrievalexpression_constructor_args():
    sig = inspect.signature(BPMN2Model::CorrelationPropertyRetrievalExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::correlationpropertybinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CorrelationPropertyBinding)


def test_bpmn2model::correlationpropertybinding_constructor_exists():
    assert callable(BPMN2Model::CorrelationPropertyBinding.__init__)


def test_bpmn2model::correlationpropertybinding_constructor_args():
    sig = inspect.signature(BPMN2Model::CorrelationPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::correlationproperty_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CorrelationProperty)


def test_bpmn2model::correlationproperty_constructor_exists():
    assert callable(BPMN2Model::CorrelationProperty.__init__)


def test_bpmn2model::correlationproperty_constructor_args():
    sig = inspect.signature(BPMN2Model::CorrelationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::correlationproperty_has_name():
    assert hasattr(BPMN2Model::CorrelationProperty, "name")
    descriptor = None
    for klass in BPMN2Model::CorrelationProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::correlationkey_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CorrelationKey)


def test_bpmn2model::correlationkey_constructor_exists():
    assert callable(BPMN2Model::CorrelationKey.__init__)


def test_bpmn2model::correlationkey_constructor_args():
    sig = inspect.signature(BPMN2Model::CorrelationKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::correlationkey_has_name():
    assert hasattr(BPMN2Model::CorrelationKey, "name")
    descriptor = None
    for klass in BPMN2Model::CorrelationKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::conversationlink_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ConversationLink)


def test_bpmn2model::conversationlink_constructor_exists():
    assert callable(BPMN2Model::ConversationLink.__init__)


def test_bpmn2model::conversationlink_constructor_args():
    sig = inspect.signature(BPMN2Model::ConversationLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::conversationlink_has_name():
    assert hasattr(BPMN2Model::ConversationLink, "name")
    descriptor = None
    for klass in BPMN2Model::ConversationLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::rootelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::RootElement)


def test_bpmn2model::rootelement_constructor_exists():
    assert callable(BPMN2Model::RootElement.__init__)


def test_bpmn2model::rootelement_constructor_args():
    sig = inspect.signature(BPMN2Model::RootElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::eventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EventDefinition)


def test_bpmn2model::eventdefinition_constructor_exists():
    assert callable(BPMN2Model::EventDefinition.__init__)


def test_bpmn2model::eventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::conditionaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ConditionalEventDefinition)


def test_bpmn2model::conditionaleventdefinition_constructor_exists():
    assert callable(BPMN2Model::ConditionalEventDefinition.__init__)


def test_bpmn2model::conditionaleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ConditionalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::complexgateway_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ComplexGateway)


def test_bpmn2model::complexgateway_constructor_exists():
    assert callable(BPMN2Model::ComplexGateway.__init__)


def test_bpmn2model::complexgateway_constructor_args():
    sig = inspect.signature(BPMN2Model::ComplexGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::complexbehaviordefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ComplexBehaviorDefinition)


def test_bpmn2model::complexbehaviordefinition_constructor_exists():
    assert callable(BPMN2Model::ComplexBehaviorDefinition.__init__)


def test_bpmn2model::complexbehaviordefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ComplexBehaviorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::compensateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CompensateEventDefinition)


def test_bpmn2model::compensateeventdefinition_constructor_exists():
    assert callable(BPMN2Model::CompensateEventDefinition.__init__)


def test_bpmn2model::compensateeventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::CompensateEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "waitForCompletion" in params, "Missing parameter 'waitForCompletion'"

def test_bpmn2model::compensateeventdefinition_has_waitForCompletion():
    assert hasattr(BPMN2Model::CompensateEventDefinition, "waitForCompletion")
    descriptor = None
    for klass in BPMN2Model::CompensateEventDefinition.__mro__:
        if "waitForCompletion" in klass.__dict__:
            descriptor = klass.__dict__["waitForCompletion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::choreographytask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ChoreographyTask)


def test_bpmn2model::choreographytask_constructor_exists():
    assert callable(BPMN2Model::ChoreographyTask.__init__)


def test_bpmn2model::choreographytask_constructor_args():
    sig = inspect.signature(BPMN2Model::ChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ChoreographyActivity)


def test_bpmn2model::choreographyactivity_constructor_exists():
    assert callable(BPMN2Model::ChoreographyActivity.__init__)


def test_bpmn2model::choreographyactivity_constructor_args():
    sig = inspect.signature(BPMN2Model::ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_bpmn2model::choreographyactivity_has_loopType():
    assert hasattr(BPMN2Model::ChoreographyActivity, "loopType")
    descriptor = None
    for klass in BPMN2Model::ChoreographyActivity.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::collaboration_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Collaboration)


def test_bpmn2model::collaboration_constructor_exists():
    assert callable(BPMN2Model::Collaboration.__init__)


def test_bpmn2model::collaboration_constructor_args():
    sig = inspect.signature(BPMN2Model::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::collaboration_has_isClosed():
    assert hasattr(BPMN2Model::Collaboration, "isClosed")
    descriptor = None
    for klass in BPMN2Model::Collaboration.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::collaboration_has_name():
    assert hasattr(BPMN2Model::Collaboration, "name")
    descriptor = None
    for klass in BPMN2Model::Collaboration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::choreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Choreography)


def test_bpmn2model::choreography_constructor_exists():
    assert callable(BPMN2Model::Choreography.__init__)


def test_bpmn2model::choreography_constructor_args():
    sig = inspect.signature(BPMN2Model::Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::categoryvalue_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CategoryValue)


def test_bpmn2model::categoryvalue_constructor_exists():
    assert callable(BPMN2Model::CategoryValue.__init__)


def test_bpmn2model::categoryvalue_constructor_args():
    sig = inspect.signature(BPMN2Model::CategoryValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2model::categoryvalue_has_value():
    assert hasattr(BPMN2Model::CategoryValue, "value")
    descriptor = None
    for klass in BPMN2Model::CategoryValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::category_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Category)


def test_bpmn2model::category_constructor_exists():
    assert callable(BPMN2Model::Category.__init__)


def test_bpmn2model::category_constructor_args():
    sig = inspect.signature(BPMN2Model::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::category_has_name():
    assert hasattr(BPMN2Model::Category, "name")
    descriptor = None
    for klass in BPMN2Model::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::catchevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CatchEvent)


def test_bpmn2model::catchevent_constructor_exists():
    assert callable(BPMN2Model::CatchEvent.__init__)


def test_bpmn2model::catchevent_constructor_args():
    sig = inspect.signature(BPMN2Model::CatchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "parallelMultiple" in params, "Missing parameter 'parallelMultiple'"

def test_bpmn2model::catchevent_has_parallelMultiple():
    assert hasattr(BPMN2Model::CatchEvent, "parallelMultiple")
    descriptor = None
    for klass in BPMN2Model::CatchEvent.__mro__:
        if "parallelMultiple" in klass.__dict__:
            descriptor = klass.__dict__["parallelMultiple"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::flowelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::FlowElement)


def test_bpmn2model::flowelement_constructor_exists():
    assert callable(BPMN2Model::FlowElement.__init__)


def test_bpmn2model::flowelement_constructor_args():
    sig = inspect.signature(BPMN2Model::FlowElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::flowelement_has_name():
    assert hasattr(BPMN2Model::FlowElement, "name")
    descriptor = None
    for klass in BPMN2Model::FlowElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::adhocsubprocess_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::AdHocSubProcess)


def test_bpmn2model::adhocsubprocess_constructor_exists():
    assert callable(BPMN2Model::AdHocSubProcess.__init__)


def test_bpmn2model::adhocsubprocess_constructor_args():
    sig = inspect.signature(BPMN2Model::AdHocSubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "cancelRemainingInstances" in params, "Missing parameter 'cancelRemainingInstances'"

def test_bpmn2model::adhocsubprocess_has_ordering():
    assert hasattr(BPMN2Model::AdHocSubProcess, "ordering")
    descriptor = None
    for klass in BPMN2Model::AdHocSubProcess.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::adhocsubprocess_has_cancelRemainingInstances():
    assert hasattr(BPMN2Model::AdHocSubProcess, "cancelRemainingInstances")
    descriptor = None
    for klass in BPMN2Model::AdHocSubProcess.__mro__:
        if "cancelRemainingInstances" in klass.__dict__:
            descriptor = klass.__dict__["cancelRemainingInstances"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::canceleventdefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CancelEventDefinition)


def test_bpmn2model::canceleventdefinition_constructor_exists():
    assert callable(BPMN2Model::CancelEventDefinition.__init__)


def test_bpmn2model::canceleventdefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::CancelEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::callconversation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CallConversation)


def test_bpmn2model::callconversation_constructor_exists():
    assert callable(BPMN2Model::CallConversation.__init__)


def test_bpmn2model::callconversation_constructor_args():
    sig = inspect.signature(BPMN2Model::CallConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::callchoreography_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CallChoreography)


def test_bpmn2model::callchoreography_constructor_exists():
    assert callable(BPMN2Model::CallChoreography.__init__)


def test_bpmn2model::callchoreography_constructor_args():
    sig = inspect.signature(BPMN2Model::CallChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::callactivity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CallActivity)


def test_bpmn2model::callactivity_constructor_exists():
    assert callable(BPMN2Model::CallActivity.__init__)


def test_bpmn2model::callactivity_constructor_args():
    sig = inspect.signature(BPMN2Model::CallActivity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::callableelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::CallableElement)


def test_bpmn2model::callableelement_constructor_exists():
    assert callable(BPMN2Model::CallableElement.__init__)


def test_bpmn2model::callableelement_constructor_args():
    sig = inspect.signature(BPMN2Model::CallableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::callableelement_has_name():
    assert hasattr(BPMN2Model::CallableElement, "name")
    descriptor = None
    for klass in BPMN2Model::CallableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::businessruletask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::BusinessRuleTask)


def test_bpmn2model::businessruletask_constructor_exists():
    assert callable(BPMN2Model::BusinessRuleTask.__init__)


def test_bpmn2model::businessruletask_constructor_args():
    sig = inspect.signature(BPMN2Model::BusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::businessruletask_has_implementation():
    assert hasattr(BPMN2Model::BusinessRuleTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::BusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::boundaryevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::BoundaryEvent)


def test_bpmn2model::boundaryevent_constructor_exists():
    assert callable(BPMN2Model::BoundaryEvent.__init__)


def test_bpmn2model::boundaryevent_constructor_args():
    sig = inspect.signature(BPMN2Model::BoundaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "cancelActivity" in params, "Missing parameter 'cancelActivity'"

def test_bpmn2model::boundaryevent_has_cancelActivity():
    assert hasattr(BPMN2Model::BoundaryEvent, "cancelActivity")
    descriptor = None
    for klass in BPMN2Model::BoundaryEvent.__mro__:
        if "cancelActivity" in klass.__dict__:
            descriptor = klass.__dict__["cancelActivity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::auditing_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Auditing)


def test_bpmn2model::auditing_constructor_exists():
    assert callable(BPMN2Model::Auditing.__init__)


def test_bpmn2model::auditing_constructor_args():
    sig = inspect.signature(BPMN2Model::Auditing.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::association_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Association)


def test_bpmn2model::association_constructor_exists():
    assert callable(BPMN2Model::Association.__init__)


def test_bpmn2model::association_constructor_args():
    sig = inspect.signature(BPMN2Model::Association.__init__)
    params = list(sig.parameters.keys())
    assert "associationDirection" in params, "Missing parameter 'associationDirection'"

def test_bpmn2model::association_has_associationDirection():
    assert hasattr(BPMN2Model::Association, "associationDirection")
    descriptor = None
    for klass in BPMN2Model::Association.__mro__:
        if "associationDirection" in klass.__dict__:
            descriptor = klass.__dict__["associationDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::assignment_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Assignment)


def test_bpmn2model::assignment_constructor_exists():
    assert callable(BPMN2Model::Assignment.__init__)


def test_bpmn2model::assignment_constructor_args():
    sig = inspect.signature(BPMN2Model::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::artifact_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Artifact)


def test_bpmn2model::artifact_constructor_exists():
    assert callable(BPMN2Model::Artifact.__init__)


def test_bpmn2model::artifact_constructor_args():
    sig = inspect.signature(BPMN2Model::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::activity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Activity)


def test_bpmn2model::activity_constructor_exists():
    assert callable(BPMN2Model::Activity.__init__)


def test_bpmn2model::activity_constructor_args():
    sig = inspect.signature(BPMN2Model::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isForCompensation" in params, "Missing parameter 'isForCompensation'"
    assert "startQuantity" in params, "Missing parameter 'startQuantity'"
    assert "completionQuantity" in params, "Missing parameter 'completionQuantity'"

def test_bpmn2model::activity_has_isForCompensation():
    assert hasattr(BPMN2Model::Activity, "isForCompensation")
    descriptor = None
    for klass in BPMN2Model::Activity.__mro__:
        if "isForCompensation" in klass.__dict__:
            descriptor = klass.__dict__["isForCompensation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::activity_has_startQuantity():
    assert hasattr(BPMN2Model::Activity, "startQuantity")
    descriptor = None
    for klass in BPMN2Model::Activity.__mro__:
        if "startQuantity" in klass.__dict__:
            descriptor = klass.__dict__["startQuantity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::activity_has_completionQuantity():
    assert hasattr(BPMN2Model::Activity, "completionQuantity")
    descriptor = None
    for klass in BPMN2Model::Activity.__mro__:
        if "completionQuantity" in klass.__dict__:
            descriptor = klass.__dict__["completionQuantity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EStringToStringMapEntry)


def test_bpmn2model::estringtostringmapentry_constructor_exists():
    assert callable(BPMN2Model::EStringToStringMapEntry.__init__)


def test_bpmn2model::estringtostringmapentry_constructor_args():
    sig = inspect.signature(BPMN2Model::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_bpmnbase_is_not_abstract():
    assert not inspect.isabstract(BPMNBase)


def test_bpmnbase_constructor_exists():
    assert callable(BPMNBase.__init__)


def test_bpmnbase_constructor_args():
    sig = inspect.signature(BPMNBase.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::resourceparameterbinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ResourceParameterBinding)


def test_bpmn2model::resourceparameterbinding_constructor_exists():
    assert callable(BPMN2Model::ResourceParameterBinding.__init__)


def test_bpmn2model::resourceparameterbinding_constructor_args():
    sig = inspect.signature(BPMN2Model::ResourceParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::interactionnode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::InteractionNode)


def test_bpmn2model::interactionnode_constructor_exists():
    assert callable(BPMN2Model::InteractionNode.__init__)


def test_bpmn2model::interactionnode_constructor_args():
    sig = inspect.signature(BPMN2Model::InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::baseelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::BaseElement)


def test_bpmn2model::baseelement_constructor_exists():
    assert callable(BPMN2Model::BaseElement.__init__)


def test_bpmn2model::baseelement_constructor_args():
    sig = inspect.signature(BPMN2Model::BaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2model::baseelement_has_anyAttribute():
    assert hasattr(BPMN2Model::BaseElement, "anyAttribute")
    descriptor = None
    for klass in BPMN2Model::BaseElement.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::baseelement_has_id():
    assert hasattr(BPMN2Model::BaseElement, "id")
    descriptor = None
    for klass in BPMN2Model::BaseElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::participantmultiplicity_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ParticipantMultiplicity)


def test_bpmn2model::participantmultiplicity_constructor_exists():
    assert callable(BPMN2Model::ParticipantMultiplicity.__init__)


def test_bpmn2model::participantmultiplicity_constructor_args():
    sig = inspect.signature(BPMN2Model::ParticipantMultiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"

def test_bpmn2model::participantmultiplicity_has_maximum():
    assert hasattr(BPMN2Model::ParticipantMultiplicity, "maximum")
    descriptor = None
    for klass in BPMN2Model::ParticipantMultiplicity.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::participantmultiplicity_has_minimum():
    assert hasattr(BPMN2Model::ParticipantMultiplicity, "minimum")
    descriptor = None
    for klass in BPMN2Model::ParticipantMultiplicity.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ExtensionDefinition)


def test_bpmn2model::extensiondefinition_constructor_exists():
    assert callable(BPMN2Model::ExtensionDefinition.__init__)


def test_bpmn2model::extensiondefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::extensiondefinition_has_name():
    assert hasattr(BPMN2Model::ExtensionDefinition, "name")
    descriptor = None
    for klass in BPMN2Model::ExtensionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::inputoutputbinding_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::InputOutputBinding)


def test_bpmn2model::inputoutputbinding_constructor_exists():
    assert callable(BPMN2Model::InputOutputBinding.__init__)


def test_bpmn2model::inputoutputbinding_constructor_args():
    sig = inspect.signature(BPMN2Model::InputOutputBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::resourceassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ResourceAssignmentExpression)


def test_bpmn2model::resourceassignmentexpression_constructor_exists():
    assert callable(BPMN2Model::ResourceAssignmentExpression.__init__)


def test_bpmn2model::resourceassignmentexpression_constructor_args():
    sig = inspect.signature(BPMN2Model::ResourceAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::escalation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Escalation)


def test_bpmn2model::escalation_constructor_exists():
    assert callable(BPMN2Model::Escalation.__init__)


def test_bpmn2model::escalation_constructor_args():
    sig = inspect.signature(BPMN2Model::Escalation.__init__)
    params = list(sig.parameters.keys())
    assert "escalationCode" in params, "Missing parameter 'escalationCode'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::escalation_has_escalationCode():
    assert hasattr(BPMN2Model::Escalation, "escalationCode")
    descriptor = None
    for klass in BPMN2Model::Escalation.__mro__:
        if "escalationCode" in klass.__dict__:
            descriptor = klass.__dict__["escalationCode"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::escalation_has_name():
    assert hasattr(BPMN2Model::Escalation, "name")
    descriptor = None
    for klass in BPMN2Model::Escalation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::import_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Import)


def test_bpmn2model::import_constructor_exists():
    assert callable(BPMN2Model::Import.__init__)


def test_bpmn2model::import_constructor_args():
    sig = inspect.signature(BPMN2Model::Import.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "location" in params, "Missing parameter 'location'"
    assert "importType" in params, "Missing parameter 'importType'"

def test_bpmn2model::import_has_namespace():
    assert hasattr(BPMN2Model::Import, "namespace")
    descriptor = None
    for klass in BPMN2Model::Import.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::import_has_location():
    assert hasattr(BPMN2Model::Import, "location")
    descriptor = None
    for klass in BPMN2Model::Import.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::import_has_importType():
    assert hasattr(BPMN2Model::Import, "importType")
    descriptor = None
    for klass in BPMN2Model::Import.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::extensionattributevalue_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ExtensionAttributeValue)


def test_bpmn2model::extensionattributevalue_constructor_exists():
    assert callable(BPMN2Model::ExtensionAttributeValue.__init__)


def test_bpmn2model::extensionattributevalue_constructor_args():
    sig = inspect.signature(BPMN2Model::ExtensionAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2model::extensionattributevalue_has_value():
    assert hasattr(BPMN2Model::ExtensionAttributeValue, "value")
    descriptor = None
    for klass in BPMN2Model::ExtensionAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::extension_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Extension)


def test_bpmn2model::extension_constructor_exists():
    assert callable(BPMN2Model::Extension.__init__)


def test_bpmn2model::extension_constructor_args():
    sig = inspect.signature(BPMN2Model::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "xsdDefinition" in params, "Missing parameter 'xsdDefinition'"
    assert "mustUnderstand" in params, "Missing parameter 'mustUnderstand'"

def test_bpmn2model::extension_has_xsdDefinition():
    assert hasattr(BPMN2Model::Extension, "xsdDefinition")
    descriptor = None
    for klass in BPMN2Model::Extension.__mro__:
        if "xsdDefinition" in klass.__dict__:
            descriptor = klass.__dict__["xsdDefinition"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::extension_has_mustUnderstand():
    assert hasattr(BPMN2Model::Extension, "mustUnderstand")
    descriptor = None
    for klass in BPMN2Model::Extension.__mro__:
        if "mustUnderstand" in klass.__dict__:
            descriptor = klass.__dict__["mustUnderstand"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::documentroot_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DocumentRoot)


def test_bpmn2model::documentroot_constructor_exists():
    assert callable(BPMN2Model::DocumentRoot.__init__)


def test_bpmn2model::documentroot_constructor_args():
    sig = inspect.signature(BPMN2Model::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_bpmn2model::documentroot_has_mixed():
    assert hasattr(BPMN2Model::DocumentRoot, "mixed")
    descriptor = None
    for klass in BPMN2Model::DocumentRoot.__mro__:
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



def test_bpmn2model::bpmnbase_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::BPMNBase)


def test_bpmn2model::bpmnbase_constructor_exists():
    assert callable(BPMN2Model::BPMNBase.__init__)


def test_bpmn2model::bpmnbase_constructor_args():
    sig = inspect.signature(BPMN2Model::BPMNBase.__init__)
    params = list(sig.parameters.keys())



def test_humanperformer_is_not_abstract():
    assert not inspect.isabstract(HumanPerformer)


def test_humanperformer_constructor_exists():
    assert callable(HumanPerformer.__init__)


def test_humanperformer_constructor_args():
    sig = inspect.signature(HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::potentialowner_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::PotentialOwner)


def test_bpmn2model::potentialowner_constructor_exists():
    assert callable(BPMN2Model::PotentialOwner.__init__)


def test_bpmn2model::potentialowner_constructor_args():
    sig = inspect.signature(BPMN2Model::PotentialOwner.__init__)
    params = list(sig.parameters.keys())



def test_resourcerole_is_not_abstract():
    assert not inspect.isabstract(ResourceRole)


def test_resourcerole_constructor_exists():
    assert callable(ResourceRole.__init__)


def test_resourcerole_constructor_args():
    sig = inspect.signature(ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::performer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Performer)


def test_bpmn2model::performer_constructor_exists():
    assert callable(BPMN2Model::Performer.__init__)


def test_bpmn2model::performer_constructor_args():
    sig = inspect.signature(BPMN2Model::Performer.__init__)
    params = list(sig.parameters.keys())



def test_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(LoopCharacteristics)


def test_loopcharacteristics_constructor_exists():
    assert callable(LoopCharacteristics.__init__)


def test_loopcharacteristics_constructor_args():
    sig = inspect.signature(LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::multiinstanceloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::MultiInstanceLoopCharacteristics)


def test_bpmn2model::multiinstanceloopcharacteristics_constructor_exists():
    assert callable(BPMN2Model::MultiInstanceLoopCharacteristics.__init__)


def test_bpmn2model::multiinstanceloopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model::MultiInstanceLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"
    assert "isSequential" in params, "Missing parameter 'isSequential'"

def test_bpmn2model::multiinstanceloopcharacteristics_has_behavior():
    assert hasattr(BPMN2Model::MultiInstanceLoopCharacteristics, "behavior")
    descriptor = None
    for klass in BPMN2Model::MultiInstanceLoopCharacteristics.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::multiinstanceloopcharacteristics_has_isSequential():
    assert hasattr(BPMN2Model::MultiInstanceLoopCharacteristics, "isSequential")
    descriptor = None
    for klass in BPMN2Model::MultiInstanceLoopCharacteristics.__mro__:
        if "isSequential" in klass.__dict__:
            descriptor = klass.__dict__["isSequential"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::standardloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::StandardLoopCharacteristics)


def test_bpmn2model::standardloopcharacteristics_constructor_exists():
    assert callable(BPMN2Model::StandardLoopCharacteristics.__init__)


def test_bpmn2model::standardloopcharacteristics_constructor_args():
    sig = inspect.signature(BPMN2Model::StandardLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "testBefore" in params, "Missing parameter 'testBefore'"

def test_bpmn2model::standardloopcharacteristics_has_testBefore():
    assert hasattr(BPMN2Model::StandardLoopCharacteristics, "testBefore")
    descriptor = None
    for klass in BPMN2Model::StandardLoopCharacteristics.__mro__:
        if "testBefore" in klass.__dict__:
            descriptor = klass.__dict__["testBefore"]
            break
    assert isinstance(descriptor, property)



def test_performer_is_not_abstract():
    assert not inspect.isabstract(Performer)


def test_performer_constructor_exists():
    assert callable(Performer.__init__)


def test_performer_constructor_args():
    sig = inspect.signature(Performer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::humanperformer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::HumanPerformer)


def test_bpmn2model::humanperformer_constructor_exists():
    assert callable(BPMN2Model::HumanPerformer.__init__)


def test_bpmn2model::humanperformer_constructor_args():
    sig = inspect.signature(BPMN2Model::HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::process_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Process)


def test_bpmn2model::process_constructor_exists():
    assert callable(BPMN2Model::Process.__init__)


def test_bpmn2model::process_constructor_args():
    sig = inspect.signature(BPMN2Model::Process.__init__)
    params = list(sig.parameters.keys())
    assert "processType" in params, "Missing parameter 'processType'"
    assert "isExecutable" in params, "Missing parameter 'isExecutable'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_bpmn2model::process_has_processType():
    assert hasattr(BPMN2Model::Process, "processType")
    descriptor = None
    for klass in BPMN2Model::Process.__mro__:
        if "processType" in klass.__dict__:
            descriptor = klass.__dict__["processType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::process_has_isExecutable():
    assert hasattr(BPMN2Model::Process, "isExecutable")
    descriptor = None
    for klass in BPMN2Model::Process.__mro__:
        if "isExecutable" in klass.__dict__:
            descriptor = klass.__dict__["isExecutable"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::process_has_isClosed():
    assert hasattr(BPMN2Model::Process, "isClosed")
    descriptor = None
    for klass in BPMN2Model::Process.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::globaltask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalTask)


def test_bpmn2model::globaltask_constructor_exists():
    assert callable(BPMN2Model::GlobalTask.__init__)


def test_bpmn2model::globaltask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_choreography_is_not_abstract():
    assert not inspect.isabstract(Choreography)


def test_choreography_constructor_exists():
    assert callable(Choreography.__init__)


def test_choreography_constructor_args():
    sig = inspect.signature(Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::globalchoreographytask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalChoreographyTask)


def test_bpmn2model::globalchoreographytask_constructor_exists():
    assert callable(BPMN2Model::GlobalChoreographyTask.__init__)


def test_bpmn2model::globalchoreographytask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_globaltask_is_not_abstract():
    assert not inspect.isabstract(GlobalTask)


def test_globaltask_constructor_exists():
    assert callable(GlobalTask.__init__)


def test_globaltask_constructor_args():
    sig = inspect.signature(GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::globalusertask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalUserTask)


def test_bpmn2model::globalusertask_constructor_exists():
    assert callable(BPMN2Model::GlobalUserTask.__init__)


def test_bpmn2model::globalusertask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalUserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::globalusertask_has_implementation():
    assert hasattr(BPMN2Model::GlobalUserTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::GlobalUserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::globalscripttask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalScriptTask)


def test_bpmn2model::globalscripttask_constructor_exists():
    assert callable(BPMN2Model::GlobalScriptTask.__init__)


def test_bpmn2model::globalscripttask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "scriptLanguage" in params, "Missing parameter 'scriptLanguage'"
    assert "script" in params, "Missing parameter 'script'"

def test_bpmn2model::globalscripttask_has_scriptLanguage():
    assert hasattr(BPMN2Model::GlobalScriptTask, "scriptLanguage")
    descriptor = None
    for klass in BPMN2Model::GlobalScriptTask.__mro__:
        if "scriptLanguage" in klass.__dict__:
            descriptor = klass.__dict__["scriptLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::globalscripttask_has_script():
    assert hasattr(BPMN2Model::GlobalScriptTask, "script")
    descriptor = None
    for klass in BPMN2Model::GlobalScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::globalmanualtask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalManualTask)


def test_bpmn2model::globalmanualtask_constructor_exists():
    assert callable(BPMN2Model::GlobalManualTask.__init__)


def test_bpmn2model::globalmanualtask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalManualTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::globalbusinessruletask_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::GlobalBusinessRuleTask)


def test_bpmn2model::globalbusinessruletask_constructor_exists():
    assert callable(BPMN2Model::GlobalBusinessRuleTask.__init__)


def test_bpmn2model::globalbusinessruletask_constructor_args():
    sig = inspect.signature(BPMN2Model::GlobalBusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2model::globalbusinessruletask_has_implementation():
    assert hasattr(BPMN2Model::GlobalBusinessRuleTask, "implementation")
    descriptor = None
    for klass in BPMN2Model::GlobalBusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::formalexpression_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::FormalExpression)


def test_bpmn2model::formalexpression_constructor_exists():
    assert callable(BPMN2Model::FormalExpression.__init__)


def test_bpmn2model::formalexpression_constructor_args():
    sig = inspect.signature(BPMN2Model::FormalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "body" in params, "Missing parameter 'body'"

def test_bpmn2model::formalexpression_has_language():
    assert hasattr(BPMN2Model::FormalExpression, "language")
    descriptor = None
    for klass in BPMN2Model::FormalExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::formalexpression_has_mixed():
    assert hasattr(BPMN2Model::FormalExpression, "mixed")
    descriptor = None
    for klass in BPMN2Model::FormalExpression.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::formalexpression_has_body():
    assert hasattr(BPMN2Model::FormalExpression, "body")
    descriptor = None
    for klass in BPMN2Model::FormalExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::FlowElementsContainer)


def test_bpmn2model::flowelementscontainer_constructor_exists():
    assert callable(BPMN2Model::FlowElementsContainer.__init__)


def test_bpmn2model::flowelementscontainer_constructor_args():
    sig = inspect.signature(BPMN2Model::FlowElementsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::extensionattributedefinition_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ExtensionAttributeDefinition)


def test_bpmn2model::extensionattributedefinition_constructor_exists():
    assert callable(BPMN2Model::ExtensionAttributeDefinition.__init__)


def test_bpmn2model::extensionattributedefinition_constructor_args():
    sig = inspect.signature(BPMN2Model::ExtensionAttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isReference" in params, "Missing parameter 'isReference'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::extensionattributedefinition_has_isReference():
    assert hasattr(BPMN2Model::ExtensionAttributeDefinition, "isReference")
    descriptor = None
    for klass in BPMN2Model::ExtensionAttributeDefinition.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::extensionattributedefinition_has_type():
    assert hasattr(BPMN2Model::ExtensionAttributeDefinition, "type")
    descriptor = None
    for klass in BPMN2Model::ExtensionAttributeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::extensionattributedefinition_has_name():
    assert hasattr(BPMN2Model::ExtensionAttributeDefinition, "name")
    descriptor = None
    for klass in BPMN2Model::ExtensionAttributeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_throwevent_is_not_abstract():
    assert not inspect.isabstract(ThrowEvent)


def test_throwevent_constructor_exists():
    assert callable(ThrowEvent.__init__)


def test_throwevent_constructor_args():
    sig = inspect.signature(ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::intermediatethrowevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::IntermediateThrowEvent)


def test_bpmn2model::intermediatethrowevent_constructor_exists():
    assert callable(BPMN2Model::IntermediateThrowEvent.__init__)


def test_bpmn2model::intermediatethrowevent_constructor_args():
    sig = inspect.signature(BPMN2Model::IntermediateThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::implicitthrowevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ImplicitThrowEvent)


def test_bpmn2model::implicitthrowevent_constructor_exists():
    assert callable(BPMN2Model::ImplicitThrowEvent.__init__)


def test_bpmn2model::implicitthrowevent_constructor_args():
    sig = inspect.signature(BPMN2Model::ImplicitThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::endevent_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::EndEvent)


def test_bpmn2model::endevent_constructor_exists():
    assert callable(BPMN2Model::EndEvent.__init__)


def test_bpmn2model::endevent_constructor_args():
    sig = inspect.signature(BPMN2Model::EndEvent.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::sequenceflow_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::SequenceFlow)


def test_bpmn2model::sequenceflow_constructor_exists():
    assert callable(BPMN2Model::SequenceFlow.__init__)


def test_bpmn2model::sequenceflow_constructor_args():
    sig = inspect.signature(BPMN2Model::SequenceFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"

def test_bpmn2model::sequenceflow_has_isImmediate():
    assert hasattr(BPMN2Model::SequenceFlow, "isImmediate")
    descriptor = None
    for klass in BPMN2Model::SequenceFlow.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::flownode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::FlowNode)


def test_bpmn2model::flownode_constructor_exists():
    assert callable(BPMN2Model::FlowNode.__init__)


def test_bpmn2model::flownode_constructor_args():
    sig = inspect.signature(BPMN2Model::FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_dataassociation_is_not_abstract():
    assert not inspect.isabstract(DataAssociation)


def test_dataassociation_constructor_exists():
    assert callable(DataAssociation.__init__)


def test_dataassociation_constructor_args():
    sig = inspect.signature(DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::datainputassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataInputAssociation)


def test_bpmn2model::datainputassociation_constructor_exists():
    assert callable(BPMN2Model::DataInputAssociation.__init__)


def test_bpmn2model::datainputassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::DataInputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::dataoutputassociation_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataOutputAssociation)


def test_bpmn2model::dataoutputassociation_constructor_exists():
    assert callable(BPMN2Model::DataOutputAssociation.__init__)


def test_bpmn2model::dataoutputassociation_constructor_args():
    sig = inspect.signature(BPMN2Model::DataOutputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(ItemAwareElement)


def test_itemawareelement_constructor_exists():
    assert callable(ItemAwareElement.__init__)


def test_itemawareelement_constructor_args():
    sig = inspect.signature(ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::datainput_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataInput)


def test_bpmn2model::datainput_constructor_exists():
    assert callable(BPMN2Model::DataInput.__init__)


def test_bpmn2model::datainput_constructor_args():
    sig = inspect.signature(BPMN2Model::DataInput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::datainput_has_isCollection():
    assert hasattr(BPMN2Model::DataInput, "isCollection")
    descriptor = None
    for klass in BPMN2Model::DataInput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::datainput_has_name():
    assert hasattr(BPMN2Model::DataInput, "name")
    descriptor = None
    for klass in BPMN2Model::DataInput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataObjectReference)


def test_bpmn2model::dataobjectreference_constructor_exists():
    assert callable(BPMN2Model::DataObjectReference.__init__)


def test_bpmn2model::dataobjectreference_constructor_args():
    sig = inspect.signature(BPMN2Model::DataObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::datastorereference_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataStoreReference)


def test_bpmn2model::datastorereference_constructor_exists():
    assert callable(BPMN2Model::DataStoreReference.__init__)


def test_bpmn2model::datastorereference_constructor_args():
    sig = inspect.signature(BPMN2Model::DataStoreReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::property_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Property)


def test_bpmn2model::property_constructor_exists():
    assert callable(BPMN2Model::Property.__init__)


def test_bpmn2model::property_constructor_args():
    sig = inspect.signature(BPMN2Model::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::property_has_name():
    assert hasattr(BPMN2Model::Property, "name")
    descriptor = None
    for klass in BPMN2Model::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::datastore_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataStore)


def test_bpmn2model::datastore_constructor_exists():
    assert callable(BPMN2Model::DataStore.__init__)


def test_bpmn2model::datastore_constructor_args():
    sig = inspect.signature(BPMN2Model::DataStore.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isUnlimited" in params, "Missing parameter 'isUnlimited'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_bpmn2model::datastore_has_name():
    assert hasattr(BPMN2Model::DataStore, "name")
    descriptor = None
    for klass in BPMN2Model::DataStore.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::datastore_has_isUnlimited():
    assert hasattr(BPMN2Model::DataStore, "isUnlimited")
    descriptor = None
    for klass in BPMN2Model::DataStore.__mro__:
        if "isUnlimited" in klass.__dict__:
            descriptor = klass.__dict__["isUnlimited"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::datastore_has_capacity():
    assert hasattr(BPMN2Model::DataStore, "capacity")
    descriptor = None
    for klass in BPMN2Model::DataStore.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::dataoutput_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataOutput)


def test_bpmn2model::dataoutput_constructor_exists():
    assert callable(BPMN2Model::DataOutput.__init__)


def test_bpmn2model::dataoutput_constructor_args():
    sig = inspect.signature(BPMN2Model::DataOutput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::dataoutput_has_isCollection():
    assert hasattr(BPMN2Model::DataOutput, "isCollection")
    descriptor = None
    for klass in BPMN2Model::DataOutput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2model::dataoutput_has_name():
    assert hasattr(BPMN2Model::DataOutput, "name")
    descriptor = None
    for klass in BPMN2Model::DataOutput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::dataobject_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::DataObject)


def test_bpmn2model::dataobject_constructor_exists():
    assert callable(BPMN2Model::DataObject.__init__)


def test_bpmn2model::dataobject_constructor_args():
    sig = inspect.signature(BPMN2Model::DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2model::dataobject_has_isCollection():
    assert hasattr(BPMN2Model::DataObject, "isCollection")
    descriptor = None
    for klass in BPMN2Model::DataObject.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::itemawareelement_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ItemAwareElement)


def test_bpmn2model::itemawareelement_constructor_exists():
    assert callable(BPMN2Model::ItemAwareElement.__init__)


def test_bpmn2model::itemawareelement_constructor_args():
    sig = inspect.signature(BPMN2Model::ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_interactionnode_is_not_abstract():
    assert not inspect.isabstract(InteractionNode)


def test_interactionnode_constructor_exists():
    assert callable(InteractionNode.__init__)


def test_interactionnode_constructor_args():
    sig = inspect.signature(InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::task_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Task)


def test_bpmn2model::task_constructor_exists():
    assert callable(BPMN2Model::Task.__init__)


def test_bpmn2model::task_constructor_args():
    sig = inspect.signature(BPMN2Model::Task.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::conversationnode_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::ConversationNode)


def test_bpmn2model::conversationnode_constructor_exists():
    assert callable(BPMN2Model::ConversationNode.__init__)


def test_bpmn2model::conversationnode_constructor_args():
    sig = inspect.signature(BPMN2Model::ConversationNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::conversationnode_has_name():
    assert hasattr(BPMN2Model::ConversationNode, "name")
    descriptor = None
    for klass in BPMN2Model::ConversationNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2model::event_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Event)


def test_bpmn2model::event_constructor_exists():
    assert callable(BPMN2Model::Event.__init__)


def test_bpmn2model::event_constructor_args():
    sig = inspect.signature(BPMN2Model::Event.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2model::participant_is_not_abstract():
    assert not inspect.isabstract(BPMN2Model::Participant)


def test_bpmn2model::participant_constructor_exists():
    assert callable(BPMN2Model::Participant.__init__)


def test_bpmn2model::participant_constructor_args():
    sig = inspect.signature(BPMN2Model::Participant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2model::participant_has_name():
    assert hasattr(BPMN2Model::Participant, "name")
    descriptor = None
    for klass in BPMN2Model::Participant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relationshipdirection_exists():
    # Check that the Enumeration exists
    assert RelationshipDirection is not None

def test_relationshipdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipDirection]
    expected_literals = [
        "Forward",
        "Both",
        "Backward",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipDirection"

def test_associationdirection_exists():
    # Check that the Enumeration exists
    assert AssociationDirection is not None

def test_associationdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationDirection]
    expected_literals = [
        "One",
        "Both",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationDirection"

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

def test_processtype_exists():
    # Check that the Enumeration exists
    assert ProcessType is not None

def test_processtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcessType]
    expected_literals = [
        "Public",
        "Private",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessType"

def test_gatewaydirection_exists():
    # Check that the Enumeration exists
    assert GatewayDirection is not None

def test_gatewaydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GatewayDirection]
    expected_literals = [
        "Unspecified",
        "Diverging",
        "Mixed",
        "Converging",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GatewayDirection"

def test_choreographylooptype_exists():
    # Check that the Enumeration exists
    assert ChoreographyLoopType is not None

def test_choreographylooptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoreographyLoopType]
    expected_literals = [
        "MultiInstanceSequential",
        "MultiInstanceParallel",
        "Standard",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoreographyLoopType"

def test_multiinstancebehavior_exists():
    # Check that the Enumeration exists
    assert MultiInstanceBehavior is not None

def test_multiinstancebehavior_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiInstanceBehavior]
    expected_literals = [
        "Complex",
        "None_",
        "One",
        "All",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiInstanceBehavior"

def test_adhocordering_exists():
    # Check that the Enumeration exists
    assert AdHocOrdering is not None

def test_adhocordering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdHocOrdering]
    expected_literals = [
        "Sequential",
        "Parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdHocOrdering"

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
SubProcess_strategy = st.builds(
    SubProcess,
)
BPMN2Model::ThrowEvent_strategy = st.builds(
    BPMN2Model::ThrowEvent,
)
FlowNode_strategy = st.builds(
    FlowNode,
)
BPMN2Model::UserTask_strategy = st.builds(
    BPMN2Model::UserTask,
    implementation=
        safe_text
)
BPMN2Model::Transaction_strategy = st.builds(
    BPMN2Model::Transaction,
    protocol=
        safe_text,
    method=
        safe_text
)
BPMN2Model::TimerEventDefinition_strategy = st.builds(
    BPMN2Model::TimerEventDefinition,
)
BPMN2Model::StartEvent_strategy = st.builds(
    BPMN2Model::StartEvent,
    isInterrupting=
        st.booleans()
)
BPMN2Model::TextAnnotation_strategy = st.builds(
    BPMN2Model::TextAnnotation,
    text=
        safe_text,
    textFormat=
        safe_text
)
BPMN2Model::TerminateEventDefinition_strategy = st.builds(
    BPMN2Model::TerminateEventDefinition,
)
BPMN2Model::SubProcess_strategy = st.builds(
    BPMN2Model::SubProcess,
    triggeredByEvent=
        st.booleans()
)
BPMN2Model::SubConversation_strategy = st.builds(
    BPMN2Model::SubConversation,
)
BPMN2Model::SubChoreography_strategy = st.builds(
    BPMN2Model::SubChoreography,
)
BPMN2Model::EObject_strategy = st.builds(
    BPMN2Model::EObject,
)
BPMN2Model::SignalEventDefinition_strategy = st.builds(
    BPMN2Model::SignalEventDefinition,
)
BPMN2Model::Signal_strategy = st.builds(
    BPMN2Model::Signal,
    name=
        safe_text
)
BPMN2Model::ServiceTask_strategy = st.builds(
    BPMN2Model::ServiceTask,
    implementation=
        safe_text
)
BPMN2Model::SendTask_strategy = st.builds(
    BPMN2Model::SendTask,
    implementation=
        safe_text
)
BPMN2Model::ScriptTask_strategy = st.builds(
    BPMN2Model::ScriptTask,
    scriptFormat=
        safe_text,
    script=
        safe_text
)
BPMN2Model::ResourceParameter_strategy = st.builds(
    BPMN2Model::ResourceParameter,
    isRequired=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model::Resource_strategy = st.builds(
    BPMN2Model::Resource,
    name=
        safe_text
)
BPMN2Model::Rendering_strategy = st.builds(
    BPMN2Model::Rendering,
)
BPMN2Model::Relationship_strategy = st.builds(
    BPMN2Model::Relationship,
    direction=
        safe_text,
    type=
        safe_text
)
BPMN2Model::ReceiveTask_strategy = st.builds(
    BPMN2Model::ReceiveTask,
    instantiate=
        st.booleans(),
    implementation=
        safe_text
)
BPMN2Model::PartnerRole_strategy = st.builds(
    BPMN2Model::PartnerRole,
    name=
        safe_text
)
BPMN2Model::PartnerEntity_strategy = st.builds(
    BPMN2Model::PartnerEntity,
    name=
        safe_text
)
BPMN2Model::MessageEventDefinition_strategy = st.builds(
    BPMN2Model::MessageEventDefinition,
)
BPMN2Model::ParticipantAssociation_strategy = st.builds(
    BPMN2Model::ParticipantAssociation,
)
BPMN2Model::ParallelGateway_strategy = st.builds(
    BPMN2Model::ParallelGateway,
)
BPMN2Model::OutputSet_strategy = st.builds(
    BPMN2Model::OutputSet,
    name=
        safe_text
)
BPMN2Model::Operation_strategy = st.builds(
    BPMN2Model::Operation,
    name=
        safe_text
)
BPMN2Model::Monitoring_strategy = st.builds(
    BPMN2Model::Monitoring,
)
BPMN2Model::MessageFlowAssociation_strategy = st.builds(
    BPMN2Model::MessageFlowAssociation,
)
BPMN2Model::MessageFlow_strategy = st.builds(
    BPMN2Model::MessageFlow,
    name=
        safe_text
)
BPMN2Model::IntermediateCatchEvent_strategy = st.builds(
    BPMN2Model::IntermediateCatchEvent,
)
BPMN2Model::Message_strategy = st.builds(
    BPMN2Model::Message,
    name=
        safe_text
)
BPMN2Model::ManualTask_strategy = st.builds(
    BPMN2Model::ManualTask,
)
BPMN2Model::LoopCharacteristics_strategy = st.builds(
    BPMN2Model::LoopCharacteristics,
)
BPMN2Model::LinkEventDefinition_strategy = st.builds(
    BPMN2Model::LinkEventDefinition,
    name=
        safe_text
)
BPMN2Model::LaneSet_strategy = st.builds(
    BPMN2Model::LaneSet,
    name=
        safe_text
)
BPMN2Model::Lane_strategy = st.builds(
    BPMN2Model::Lane,
    name=
        safe_text
)
BPMN2Model::ItemDefinition_strategy = st.builds(
    BPMN2Model::ItemDefinition,
    isCollection=
        st.booleans(),
    itemKind=
        safe_text
)
BPMN2Model::InputOutputSpecification_strategy = st.builds(
    BPMN2Model::InputOutputSpecification,
)
BPMN2Model::Interface_strategy = st.builds(
    BPMN2Model::Interface,
    name=
        safe_text
)
BPMN2Model::InputSet_strategy = st.builds(
    BPMN2Model::InputSet,
    name=
        safe_text
)
BPMN2Model::InclusiveGateway_strategy = st.builds(
    BPMN2Model::InclusiveGateway,
)
BPMN2Model::ResourceRole_strategy = st.builds(
    BPMN2Model::ResourceRole,
    name=
        safe_text
)
BPMN2Model::Group_strategy = st.builds(
    BPMN2Model::Group,
)
BPMN2Model::ExclusiveGateway_strategy = st.builds(
    BPMN2Model::ExclusiveGateway,
)
BPMN2Model::GlobalConversation_strategy = st.builds(
    BPMN2Model::GlobalConversation,
)
BPMN2Model::Gateway_strategy = st.builds(
    BPMN2Model::Gateway,
    gatewayDirection=
        safe_text
)
BPMN2Model::Expression_strategy = st.builds(
    BPMN2Model::Expression,
)
BPMN2Model::EventBasedGateway_strategy = st.builds(
    BPMN2Model::EventBasedGateway,
    eventGatewayType=
        safe_text,
    instantiate=
        st.booleans()
)
BPMN2Model::EscalationEventDefinition_strategy = st.builds(
    BPMN2Model::EscalationEventDefinition,
)
BPMN2Model::ErrorEventDefinition_strategy = st.builds(
    BPMN2Model::ErrorEventDefinition,
)
BPMN2Model::Error_strategy = st.builds(
    BPMN2Model::Error,
    name=
        safe_text,
    errorCode=
        safe_text
)
BPMN2Model::EndPoint_strategy = st.builds(
    BPMN2Model::EndPoint,
)
BPMN2Model::Documentation_strategy = st.builds(
    BPMN2Model::Documentation,
    textFormat=
        safe_text,
    mixed=
        safe_text,
    text=
        safe_text
)
BPMN2Model::Definitions_strategy = st.builds(
    BPMN2Model::Definitions,
    typeLanguage=
        safe_text,
    expressionLanguage=
        safe_text,
    name=
        safe_text,
    exporter=
        safe_text,
    targetNamespace=
        safe_text,
    exporterVersion=
        safe_text
)
BPMN2Model::DataState_strategy = st.builds(
    BPMN2Model::DataState,
    name=
        safe_text
)
BPMN2Model::ConversationAssociation_strategy = st.builds(
    BPMN2Model::ConversationAssociation,
)
BPMN2Model::Conversation_strategy = st.builds(
    BPMN2Model::Conversation,
)
BPMN2Model::DataAssociation_strategy = st.builds(
    BPMN2Model::DataAssociation,
)
BPMN2Model::CorrelationSubscription_strategy = st.builds(
    BPMN2Model::CorrelationSubscription,
)
BPMN2Model::CorrelationPropertyRetrievalExpression_strategy = st.builds(
    BPMN2Model::CorrelationPropertyRetrievalExpression,
)
BPMN2Model::CorrelationPropertyBinding_strategy = st.builds(
    BPMN2Model::CorrelationPropertyBinding,
)
BPMN2Model::CorrelationProperty_strategy = st.builds(
    BPMN2Model::CorrelationProperty,
    name=
        safe_text
)
BPMN2Model::CorrelationKey_strategy = st.builds(
    BPMN2Model::CorrelationKey,
    name=
        safe_text
)
BPMN2Model::ConversationLink_strategy = st.builds(
    BPMN2Model::ConversationLink,
    name=
        safe_text
)
BPMN2Model::RootElement_strategy = st.builds(
    BPMN2Model::RootElement,
)
BPMN2Model::EventDefinition_strategy = st.builds(
    BPMN2Model::EventDefinition,
)
BPMN2Model::ConditionalEventDefinition_strategy = st.builds(
    BPMN2Model::ConditionalEventDefinition,
)
BPMN2Model::ComplexGateway_strategy = st.builds(
    BPMN2Model::ComplexGateway,
)
BPMN2Model::ComplexBehaviorDefinition_strategy = st.builds(
    BPMN2Model::ComplexBehaviorDefinition,
)
BPMN2Model::CompensateEventDefinition_strategy = st.builds(
    BPMN2Model::CompensateEventDefinition,
    waitForCompletion=
        st.booleans()
)
BPMN2Model::ChoreographyTask_strategy = st.builds(
    BPMN2Model::ChoreographyTask,
)
BPMN2Model::ChoreographyActivity_strategy = st.builds(
    BPMN2Model::ChoreographyActivity,
    loopType=
        safe_text
)
BPMN2Model::Collaboration_strategy = st.builds(
    BPMN2Model::Collaboration,
    isClosed=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model::Choreography_strategy = st.builds(
    BPMN2Model::Choreography,
)
BPMN2Model::CategoryValue_strategy = st.builds(
    BPMN2Model::CategoryValue,
    value=
        safe_text
)
BPMN2Model::Category_strategy = st.builds(
    BPMN2Model::Category,
    name=
        safe_text
)
BPMN2Model::CatchEvent_strategy = st.builds(
    BPMN2Model::CatchEvent,
    parallelMultiple=
        st.booleans()
)
BPMN2Model::FlowElement_strategy = st.builds(
    BPMN2Model::FlowElement,
    name=
        safe_text
)
BPMN2Model::AdHocSubProcess_strategy = st.builds(
    BPMN2Model::AdHocSubProcess,
    ordering=
        safe_text,
    cancelRemainingInstances=
        st.booleans()
)
BPMN2Model::CancelEventDefinition_strategy = st.builds(
    BPMN2Model::CancelEventDefinition,
)
BPMN2Model::CallConversation_strategy = st.builds(
    BPMN2Model::CallConversation,
)
BPMN2Model::CallChoreography_strategy = st.builds(
    BPMN2Model::CallChoreography,
)
BPMN2Model::CallActivity_strategy = st.builds(
    BPMN2Model::CallActivity,
)
BPMN2Model::CallableElement_strategy = st.builds(
    BPMN2Model::CallableElement,
    name=
        safe_text
)
BPMN2Model::BusinessRuleTask_strategy = st.builds(
    BPMN2Model::BusinessRuleTask,
    implementation=
        safe_text
)
BPMN2Model::BoundaryEvent_strategy = st.builds(
    BPMN2Model::BoundaryEvent,
    cancelActivity=
        st.booleans()
)
BPMN2Model::Auditing_strategy = st.builds(
    BPMN2Model::Auditing,
)
BPMN2Model::Association_strategy = st.builds(
    BPMN2Model::Association,
    associationDirection=
        safe_text
)
BPMN2Model::Assignment_strategy = st.builds(
    BPMN2Model::Assignment,
)
BPMN2Model::Artifact_strategy = st.builds(
    BPMN2Model::Artifact,
)
BPMN2Model::Activity_strategy = st.builds(
    BPMN2Model::Activity,
    isForCompensation=
        st.booleans(),
    startQuantity=
        st.integers(),
    completionQuantity=
        st.integers()
)
BPMN2Model::EStringToStringMapEntry_strategy = st.builds(
    BPMN2Model::EStringToStringMapEntry,
)
BPMNBase_strategy = st.builds(
    BPMNBase,
)
BPMN2Model::ResourceParameterBinding_strategy = st.builds(
    BPMN2Model::ResourceParameterBinding,
)
BPMN2Model::InteractionNode_strategy = st.builds(
    BPMN2Model::InteractionNode,
)
BPMN2Model::BaseElement_strategy = st.builds(
    BPMN2Model::BaseElement,
    anyAttribute=
        safe_text,
    id=
        safe_text
)
BPMN2Model::ParticipantMultiplicity_strategy = st.builds(
    BPMN2Model::ParticipantMultiplicity,
    maximum=
        st.integers(),
    minimum=
        st.integers()
)
BPMN2Model::ExtensionDefinition_strategy = st.builds(
    BPMN2Model::ExtensionDefinition,
    name=
        safe_text
)
BPMN2Model::InputOutputBinding_strategy = st.builds(
    BPMN2Model::InputOutputBinding,
)
BPMN2Model::ResourceAssignmentExpression_strategy = st.builds(
    BPMN2Model::ResourceAssignmentExpression,
)
BPMN2Model::Escalation_strategy = st.builds(
    BPMN2Model::Escalation,
    escalationCode=
        safe_text,
    name=
        safe_text
)
BPMN2Model::Import_strategy = st.builds(
    BPMN2Model::Import,
    namespace=
        safe_text,
    location=
        safe_text,
    importType=
        safe_text
)
BPMN2Model::ExtensionAttributeValue_strategy = st.builds(
    BPMN2Model::ExtensionAttributeValue,
    value=
        safe_text
)
BPMN2Model::Extension_strategy = st.builds(
    BPMN2Model::Extension,
    xsdDefinition=
        safe_text,
    mustUnderstand=
        st.booleans()
)
BPMN2Model::DocumentRoot_strategy = st.builds(
    BPMN2Model::DocumentRoot,
    mixed=
        safe_text
)
EObject_strategy = st.builds(
    EObject,
)
BPMN2Model::BPMNBase_strategy = st.builds(
    BPMN2Model::BPMNBase,
)
HumanPerformer_strategy = st.builds(
    HumanPerformer,
)
BPMN2Model::PotentialOwner_strategy = st.builds(
    BPMN2Model::PotentialOwner,
)
ResourceRole_strategy = st.builds(
    ResourceRole,
)
BPMN2Model::Performer_strategy = st.builds(
    BPMN2Model::Performer,
)
LoopCharacteristics_strategy = st.builds(
    LoopCharacteristics,
)
BPMN2Model::MultiInstanceLoopCharacteristics_strategy = st.builds(
    BPMN2Model::MultiInstanceLoopCharacteristics,
    behavior=
        safe_text,
    isSequential=
        st.booleans()
)
BPMN2Model::StandardLoopCharacteristics_strategy = st.builds(
    BPMN2Model::StandardLoopCharacteristics,
    testBefore=
        st.booleans()
)
Performer_strategy = st.builds(
    Performer,
)
BPMN2Model::HumanPerformer_strategy = st.builds(
    BPMN2Model::HumanPerformer,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
BPMN2Model::Process_strategy = st.builds(
    BPMN2Model::Process,
    processType=
        safe_text,
    isExecutable=
        st.booleans(),
    isClosed=
        st.booleans()
)
BPMN2Model::GlobalTask_strategy = st.builds(
    BPMN2Model::GlobalTask,
)
Choreography_strategy = st.builds(
    Choreography,
)
BPMN2Model::GlobalChoreographyTask_strategy = st.builds(
    BPMN2Model::GlobalChoreographyTask,
)
GlobalTask_strategy = st.builds(
    GlobalTask,
)
BPMN2Model::GlobalUserTask_strategy = st.builds(
    BPMN2Model::GlobalUserTask,
    implementation=
        safe_text
)
BPMN2Model::GlobalScriptTask_strategy = st.builds(
    BPMN2Model::GlobalScriptTask,
    scriptLanguage=
        safe_text,
    script=
        safe_text
)
BPMN2Model::GlobalManualTask_strategy = st.builds(
    BPMN2Model::GlobalManualTask,
)
BPMN2Model::GlobalBusinessRuleTask_strategy = st.builds(
    BPMN2Model::GlobalBusinessRuleTask,
    implementation=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
BPMN2Model::FormalExpression_strategy = st.builds(
    BPMN2Model::FormalExpression,
    language=
        safe_text,
    mixed=
        safe_text,
    body=
        safe_text
)
BPMN2Model::FlowElementsContainer_strategy = st.builds(
    BPMN2Model::FlowElementsContainer,
)
BPMN2Model::ExtensionAttributeDefinition_strategy = st.builds(
    BPMN2Model::ExtensionAttributeDefinition,
    isReference=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text
)
ThrowEvent_strategy = st.builds(
    ThrowEvent,
)
BPMN2Model::IntermediateThrowEvent_strategy = st.builds(
    BPMN2Model::IntermediateThrowEvent,
)
BPMN2Model::ImplicitThrowEvent_strategy = st.builds(
    BPMN2Model::ImplicitThrowEvent,
)
BPMN2Model::EndEvent_strategy = st.builds(
    BPMN2Model::EndEvent,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
BPMN2Model::SequenceFlow_strategy = st.builds(
    BPMN2Model::SequenceFlow,
    isImmediate=
        st.booleans()
)
BPMN2Model::FlowNode_strategy = st.builds(
    BPMN2Model::FlowNode,
)
DataAssociation_strategy = st.builds(
    DataAssociation,
)
BPMN2Model::DataInputAssociation_strategy = st.builds(
    BPMN2Model::DataInputAssociation,
)
BPMN2Model::DataOutputAssociation_strategy = st.builds(
    BPMN2Model::DataOutputAssociation,
)
ItemAwareElement_strategy = st.builds(
    ItemAwareElement,
)
BPMN2Model::DataInput_strategy = st.builds(
    BPMN2Model::DataInput,
    isCollection=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model::DataObjectReference_strategy = st.builds(
    BPMN2Model::DataObjectReference,
)
BPMN2Model::DataStoreReference_strategy = st.builds(
    BPMN2Model::DataStoreReference,
)
BPMN2Model::Property_strategy = st.builds(
    BPMN2Model::Property,
    name=
        safe_text
)
BPMN2Model::DataStore_strategy = st.builds(
    BPMN2Model::DataStore,
    name=
        safe_text,
    isUnlimited=
        st.booleans(),
    capacity=
        st.integers()
)
BPMN2Model::DataOutput_strategy = st.builds(
    BPMN2Model::DataOutput,
    isCollection=
        st.booleans(),
    name=
        safe_text
)
BPMN2Model::DataObject_strategy = st.builds(
    BPMN2Model::DataObject,
    isCollection=
        st.booleans()
)
BPMN2Model::ItemAwareElement_strategy = st.builds(
    BPMN2Model::ItemAwareElement,
)
InteractionNode_strategy = st.builds(
    InteractionNode,
)
BPMN2Model::Task_strategy = st.builds(
    BPMN2Model::Task,
)
BPMN2Model::ConversationNode_strategy = st.builds(
    BPMN2Model::ConversationNode,
    name=
        safe_text
)
BPMN2Model::Event_strategy = st.builds(
    BPMN2Model::Event,
)
BPMN2Model::Participant_strategy = st.builds(
    BPMN2Model::Participant,
    name=
        safe_text
)

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

@given(instance=SubProcess_strategy)
@settings(max_examples=50)
def test_subprocess_instantiation(instance):
    assert isinstance(instance, SubProcess)

@given(instance=BPMN2Model::ThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::throwevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ThrowEvent)

@given(instance=FlowNode_strategy)
@settings(max_examples=50)
def test_flownode_instantiation(instance):
    assert isinstance(instance, FlowNode)

@given(instance=BPMN2Model::UserTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::usertask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::UserTask)

@given(instance=BPMN2Model::UserTask_strategy)
def test_bpmn2model::usertask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::UserTask_strategy)
def test_bpmn2model::usertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::Transaction_strategy)
@settings(max_examples=50)
def test_bpmn2model::transaction_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Transaction)

@given(instance=BPMN2Model::Transaction_strategy)
def test_bpmn2model::transaction_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=BPMN2Model::Transaction_strategy)
def test_bpmn2model::transaction_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=BPMN2Model::Transaction_strategy)
def test_bpmn2model::transaction_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=BPMN2Model::Transaction_strategy)
def test_bpmn2model::transaction_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=BPMN2Model::TimerEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::timereventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::TimerEventDefinition)

@given(instance=BPMN2Model::StartEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::startevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::StartEvent)

@given(instance=BPMN2Model::StartEvent_strategy)
def test_bpmn2model::startevent_isInterrupting_type(instance):
    assert isinstance(instance.isInterrupting, bool)


@given(instance=BPMN2Model::StartEvent_strategy)
def test_bpmn2model::startevent_isInterrupting_setter(instance):
    original = instance.isInterrupting
    instance.isInterrupting = original
    assert instance.isInterrupting == original

@given(instance=BPMN2Model::TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn2model::textannotation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::TextAnnotation)

@given(instance=BPMN2Model::TextAnnotation_strategy)
def test_bpmn2model::textannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=BPMN2Model::TextAnnotation_strategy)
def test_bpmn2model::textannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=BPMN2Model::TextAnnotation_strategy)
def test_bpmn2model::textannotation_textFormat_type(instance):
    assert isinstance(instance.textFormat, str)


@given(instance=BPMN2Model::TextAnnotation_strategy)
def test_bpmn2model::textannotation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=BPMN2Model::TerminateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::terminateeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::TerminateEventDefinition)

@given(instance=BPMN2Model::SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2model::subprocess_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SubProcess)

@given(instance=BPMN2Model::SubProcess_strategy)
def test_bpmn2model::subprocess_triggeredByEvent_type(instance):
    assert isinstance(instance.triggeredByEvent, bool)


@given(instance=BPMN2Model::SubProcess_strategy)
def test_bpmn2model::subprocess_triggeredByEvent_setter(instance):
    original = instance.triggeredByEvent
    instance.triggeredByEvent = original
    assert instance.triggeredByEvent == original

@given(instance=BPMN2Model::SubConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model::subconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SubConversation)

@given(instance=BPMN2Model::SubChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2model::subchoreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SubChoreography)

@given(instance=BPMN2Model::EObject_strategy)
@settings(max_examples=50)
def test_bpmn2model::eobject_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EObject)

@given(instance=BPMN2Model::SignalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::signaleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SignalEventDefinition)

@given(instance=BPMN2Model::Signal_strategy)
@settings(max_examples=50)
def test_bpmn2model::signal_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Signal)

@given(instance=BPMN2Model::Signal_strategy)
def test_bpmn2model::signal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Signal_strategy)
def test_bpmn2model::signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::ServiceTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::servicetask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ServiceTask)

@given(instance=BPMN2Model::ServiceTask_strategy)
def test_bpmn2model::servicetask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::ServiceTask_strategy)
def test_bpmn2model::servicetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::SendTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::sendtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SendTask)

@given(instance=BPMN2Model::SendTask_strategy)
def test_bpmn2model::sendtask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::SendTask_strategy)
def test_bpmn2model::sendtask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::ScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::scripttask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ScriptTask)

@given(instance=BPMN2Model::ScriptTask_strategy)
def test_bpmn2model::scripttask_scriptFormat_type(instance):
    assert isinstance(instance.scriptFormat, str)


@given(instance=BPMN2Model::ScriptTask_strategy)
def test_bpmn2model::scripttask_scriptFormat_setter(instance):
    original = instance.scriptFormat
    instance.scriptFormat = original
    assert instance.scriptFormat == original

@given(instance=BPMN2Model::ScriptTask_strategy)
def test_bpmn2model::scripttask_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=BPMN2Model::ScriptTask_strategy)
def test_bpmn2model::scripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=BPMN2Model::ResourceParameter_strategy)
@settings(max_examples=50)
def test_bpmn2model::resourceparameter_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ResourceParameter)

@given(instance=BPMN2Model::ResourceParameter_strategy)
def test_bpmn2model::resourceparameter_isRequired_type(instance):
    assert isinstance(instance.isRequired, bool)


@given(instance=BPMN2Model::ResourceParameter_strategy)
def test_bpmn2model::resourceparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BPMN2Model::ResourceParameter_strategy)
def test_bpmn2model::resourceparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ResourceParameter_strategy)
def test_bpmn2model::resourceparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Resource_strategy)
@settings(max_examples=50)
def test_bpmn2model::resource_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Resource)

@given(instance=BPMN2Model::Resource_strategy)
def test_bpmn2model::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Resource_strategy)
def test_bpmn2model::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Rendering_strategy)
@settings(max_examples=50)
def test_bpmn2model::rendering_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Rendering)

@given(instance=BPMN2Model::Relationship_strategy)
@settings(max_examples=50)
def test_bpmn2model::relationship_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Relationship)

@given(instance=BPMN2Model::Relationship_strategy)
def test_bpmn2model::relationship_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=BPMN2Model::Relationship_strategy)
def test_bpmn2model::relationship_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=BPMN2Model::Relationship_strategy)
def test_bpmn2model::relationship_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=BPMN2Model::Relationship_strategy)
def test_bpmn2model::relationship_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=BPMN2Model::ReceiveTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::receivetask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ReceiveTask)

@given(instance=BPMN2Model::ReceiveTask_strategy)
def test_bpmn2model::receivetask_instantiate_type(instance):
    assert isinstance(instance.instantiate, bool)


@given(instance=BPMN2Model::ReceiveTask_strategy)
def test_bpmn2model::receivetask_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=BPMN2Model::ReceiveTask_strategy)
def test_bpmn2model::receivetask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::ReceiveTask_strategy)
def test_bpmn2model::receivetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::PartnerRole_strategy)
@settings(max_examples=50)
def test_bpmn2model::partnerrole_instantiation(instance):
    assert isinstance(instance, BPMN2Model::PartnerRole)

@given(instance=BPMN2Model::PartnerRole_strategy)
def test_bpmn2model::partnerrole_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::PartnerRole_strategy)
def test_bpmn2model::partnerrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::PartnerEntity_strategy)
@settings(max_examples=50)
def test_bpmn2model::partnerentity_instantiation(instance):
    assert isinstance(instance, BPMN2Model::PartnerEntity)

@given(instance=BPMN2Model::PartnerEntity_strategy)
def test_bpmn2model::partnerentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::PartnerEntity_strategy)
def test_bpmn2model::partnerentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::MessageEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::messageeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::MessageEventDefinition)

@given(instance=BPMN2Model::ParticipantAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::participantassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ParticipantAssociation)

@given(instance=BPMN2Model::ParallelGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::parallelgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ParallelGateway)

@given(instance=BPMN2Model::OutputSet_strategy)
@settings(max_examples=50)
def test_bpmn2model::outputset_instantiation(instance):
    assert isinstance(instance, BPMN2Model::OutputSet)

@given(instance=BPMN2Model::OutputSet_strategy)
def test_bpmn2model::outputset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::OutputSet_strategy)
def test_bpmn2model::outputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Operation_strategy)
@settings(max_examples=50)
def test_bpmn2model::operation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Operation)

@given(instance=BPMN2Model::Operation_strategy)
def test_bpmn2model::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Operation_strategy)
def test_bpmn2model::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Monitoring_strategy)
@settings(max_examples=50)
def test_bpmn2model::monitoring_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Monitoring)

@given(instance=BPMN2Model::MessageFlowAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::messageflowassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::MessageFlowAssociation)

@given(instance=BPMN2Model::MessageFlow_strategy)
@settings(max_examples=50)
def test_bpmn2model::messageflow_instantiation(instance):
    assert isinstance(instance, BPMN2Model::MessageFlow)

@given(instance=BPMN2Model::MessageFlow_strategy)
def test_bpmn2model::messageflow_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::MessageFlow_strategy)
def test_bpmn2model::messageflow_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::IntermediateCatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::intermediatecatchevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::IntermediateCatchEvent)

@given(instance=BPMN2Model::Message_strategy)
@settings(max_examples=50)
def test_bpmn2model::message_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Message)

@given(instance=BPMN2Model::Message_strategy)
def test_bpmn2model::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Message_strategy)
def test_bpmn2model::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::ManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::manualtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ManualTask)

@given(instance=BPMN2Model::LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model::loopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model::LoopCharacteristics)

@given(instance=BPMN2Model::LinkEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::linkeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::LinkEventDefinition)

@given(instance=BPMN2Model::LinkEventDefinition_strategy)
def test_bpmn2model::linkeventdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::LinkEventDefinition_strategy)
def test_bpmn2model::linkeventdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::LaneSet_strategy)
@settings(max_examples=50)
def test_bpmn2model::laneset_instantiation(instance):
    assert isinstance(instance, BPMN2Model::LaneSet)

@given(instance=BPMN2Model::LaneSet_strategy)
def test_bpmn2model::laneset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::LaneSet_strategy)
def test_bpmn2model::laneset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Lane_strategy)
@settings(max_examples=50)
def test_bpmn2model::lane_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Lane)

@given(instance=BPMN2Model::Lane_strategy)
def test_bpmn2model::lane_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Lane_strategy)
def test_bpmn2model::lane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::ItemDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::itemdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ItemDefinition)

@given(instance=BPMN2Model::ItemDefinition_strategy)
def test_bpmn2model::itemdefinition_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=BPMN2Model::ItemDefinition_strategy)
def test_bpmn2model::itemdefinition_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model::ItemDefinition_strategy)
def test_bpmn2model::itemdefinition_itemKind_type(instance):
    assert isinstance(instance.itemKind, str)


@given(instance=BPMN2Model::ItemDefinition_strategy)
def test_bpmn2model::itemdefinition_itemKind_setter(instance):
    original = instance.itemKind
    instance.itemKind = original
    assert instance.itemKind == original

@given(instance=BPMN2Model::InputOutputSpecification_strategy)
@settings(max_examples=50)
def test_bpmn2model::inputoutputspecification_instantiation(instance):
    assert isinstance(instance, BPMN2Model::InputOutputSpecification)

@given(instance=BPMN2Model::Interface_strategy)
@settings(max_examples=50)
def test_bpmn2model::interface_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Interface)

@given(instance=BPMN2Model::Interface_strategy)
def test_bpmn2model::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Interface_strategy)
def test_bpmn2model::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::InputSet_strategy)
@settings(max_examples=50)
def test_bpmn2model::inputset_instantiation(instance):
    assert isinstance(instance, BPMN2Model::InputSet)

@given(instance=BPMN2Model::InputSet_strategy)
def test_bpmn2model::inputset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::InputSet_strategy)
def test_bpmn2model::inputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::InclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::inclusivegateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::InclusiveGateway)

@given(instance=BPMN2Model::ResourceRole_strategy)
@settings(max_examples=50)
def test_bpmn2model::resourcerole_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ResourceRole)

@given(instance=BPMN2Model::ResourceRole_strategy)
def test_bpmn2model::resourcerole_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ResourceRole_strategy)
def test_bpmn2model::resourcerole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Group_strategy)
@settings(max_examples=50)
def test_bpmn2model::group_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Group)

@given(instance=BPMN2Model::ExclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::exclusivegateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ExclusiveGateway)

@given(instance=BPMN2Model::GlobalConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalConversation)

@given(instance=BPMN2Model::Gateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::gateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Gateway)

@given(instance=BPMN2Model::Gateway_strategy)
def test_bpmn2model::gateway_gatewayDirection_type(instance):
    assert isinstance(instance.gatewayDirection, str)


@given(instance=BPMN2Model::Gateway_strategy)
def test_bpmn2model::gateway_gatewayDirection_setter(instance):
    original = instance.gatewayDirection
    instance.gatewayDirection = original
    assert instance.gatewayDirection == original

@given(instance=BPMN2Model::Expression_strategy)
@settings(max_examples=50)
def test_bpmn2model::expression_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Expression)

@given(instance=BPMN2Model::EventBasedGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::eventbasedgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EventBasedGateway)

@given(instance=BPMN2Model::EventBasedGateway_strategy)
def test_bpmn2model::eventbasedgateway_eventGatewayType_type(instance):
    assert isinstance(instance.eventGatewayType, str)


@given(instance=BPMN2Model::EventBasedGateway_strategy)
def test_bpmn2model::eventbasedgateway_eventGatewayType_setter(instance):
    original = instance.eventGatewayType
    instance.eventGatewayType = original
    assert instance.eventGatewayType == original

@given(instance=BPMN2Model::EventBasedGateway_strategy)
def test_bpmn2model::eventbasedgateway_instantiate_type(instance):
    assert isinstance(instance.instantiate, bool)


@given(instance=BPMN2Model::EventBasedGateway_strategy)
def test_bpmn2model::eventbasedgateway_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=BPMN2Model::EscalationEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::escalationeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EscalationEventDefinition)

@given(instance=BPMN2Model::ErrorEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::erroreventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ErrorEventDefinition)

@given(instance=BPMN2Model::Error_strategy)
@settings(max_examples=50)
def test_bpmn2model::error_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Error)

@given(instance=BPMN2Model::Error_strategy)
def test_bpmn2model::error_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Error_strategy)
def test_bpmn2model::error_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Error_strategy)
def test_bpmn2model::error_errorCode_type(instance):
    assert isinstance(instance.errorCode, str)


@given(instance=BPMN2Model::Error_strategy)
def test_bpmn2model::error_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=BPMN2Model::EndPoint_strategy)
@settings(max_examples=50)
def test_bpmn2model::endpoint_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EndPoint)

@given(instance=BPMN2Model::Documentation_strategy)
@settings(max_examples=50)
def test_bpmn2model::documentation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Documentation)

@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_textFormat_type(instance):
    assert isinstance(instance.textFormat, str)


@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=BPMN2Model::Documentation_strategy)
def test_bpmn2model::documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=BPMN2Model::Definitions_strategy)
@settings(max_examples=50)
def test_bpmn2model::definitions_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Definitions)

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_typeLanguage_type(instance):
    assert isinstance(instance.typeLanguage, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_typeLanguage_setter(instance):
    original = instance.typeLanguage
    instance.typeLanguage = original
    assert instance.typeLanguage == original

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_expressionLanguage_type(instance):
    assert isinstance(instance.expressionLanguage, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_expressionLanguage_setter(instance):
    original = instance.expressionLanguage
    instance.expressionLanguage = original
    assert instance.expressionLanguage == original

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_exporter_type(instance):
    assert isinstance(instance.exporter, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_exporter_setter(instance):
    original = instance.exporter
    instance.exporter = original
    assert instance.exporter == original

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_targetNamespace_type(instance):
    assert isinstance(instance.targetNamespace, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_targetNamespace_setter(instance):
    original = instance.targetNamespace
    instance.targetNamespace = original
    assert instance.targetNamespace == original

@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_exporterVersion_type(instance):
    assert isinstance(instance.exporterVersion, str)


@given(instance=BPMN2Model::Definitions_strategy)
def test_bpmn2model::definitions_exporterVersion_setter(instance):
    original = instance.exporterVersion
    instance.exporterVersion = original
    assert instance.exporterVersion == original

@given(instance=BPMN2Model::DataState_strategy)
@settings(max_examples=50)
def test_bpmn2model::datastate_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataState)

@given(instance=BPMN2Model::DataState_strategy)
def test_bpmn2model::datastate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::DataState_strategy)
def test_bpmn2model::datastate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::ConversationAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::conversationassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ConversationAssociation)

@given(instance=BPMN2Model::Conversation_strategy)
@settings(max_examples=50)
def test_bpmn2model::conversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Conversation)

@given(instance=BPMN2Model::DataAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::dataassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataAssociation)

@given(instance=BPMN2Model::CorrelationSubscription_strategy)
@settings(max_examples=50)
def test_bpmn2model::correlationsubscription_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CorrelationSubscription)

@given(instance=BPMN2Model::CorrelationPropertyRetrievalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model::correlationpropertyretrievalexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CorrelationPropertyRetrievalExpression)

@given(instance=BPMN2Model::CorrelationPropertyBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model::correlationpropertybinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CorrelationPropertyBinding)

@given(instance=BPMN2Model::CorrelationProperty_strategy)
@settings(max_examples=50)
def test_bpmn2model::correlationproperty_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CorrelationProperty)

@given(instance=BPMN2Model::CorrelationProperty_strategy)
def test_bpmn2model::correlationproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::CorrelationProperty_strategy)
def test_bpmn2model::correlationproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::CorrelationKey_strategy)
@settings(max_examples=50)
def test_bpmn2model::correlationkey_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CorrelationKey)

@given(instance=BPMN2Model::CorrelationKey_strategy)
def test_bpmn2model::correlationkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::CorrelationKey_strategy)
def test_bpmn2model::correlationkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::ConversationLink_strategy)
@settings(max_examples=50)
def test_bpmn2model::conversationlink_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ConversationLink)

@given(instance=BPMN2Model::ConversationLink_strategy)
def test_bpmn2model::conversationlink_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ConversationLink_strategy)
def test_bpmn2model::conversationlink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::RootElement_strategy)
@settings(max_examples=50)
def test_bpmn2model::rootelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model::RootElement)

@given(instance=BPMN2Model::EventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::eventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EventDefinition)

@given(instance=BPMN2Model::ConditionalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::conditionaleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ConditionalEventDefinition)

@given(instance=BPMN2Model::ComplexGateway_strategy)
@settings(max_examples=50)
def test_bpmn2model::complexgateway_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ComplexGateway)

@given(instance=BPMN2Model::ComplexBehaviorDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::complexbehaviordefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ComplexBehaviorDefinition)

@given(instance=BPMN2Model::CompensateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::compensateeventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CompensateEventDefinition)

@given(instance=BPMN2Model::CompensateEventDefinition_strategy)
def test_bpmn2model::compensateeventdefinition_waitForCompletion_type(instance):
    assert isinstance(instance.waitForCompletion, bool)


@given(instance=BPMN2Model::CompensateEventDefinition_strategy)
def test_bpmn2model::compensateeventdefinition_waitForCompletion_setter(instance):
    original = instance.waitForCompletion
    instance.waitForCompletion = original
    assert instance.waitForCompletion == original

@given(instance=BPMN2Model::ChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::choreographytask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ChoreographyTask)

@given(instance=BPMN2Model::ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_bpmn2model::choreographyactivity_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ChoreographyActivity)

@given(instance=BPMN2Model::ChoreographyActivity_strategy)
def test_bpmn2model::choreographyactivity_loopType_type(instance):
    assert isinstance(instance.loopType, str)


@given(instance=BPMN2Model::ChoreographyActivity_strategy)
def test_bpmn2model::choreographyactivity_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=BPMN2Model::Collaboration_strategy)
@settings(max_examples=50)
def test_bpmn2model::collaboration_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Collaboration)

@given(instance=BPMN2Model::Collaboration_strategy)
def test_bpmn2model::collaboration_isClosed_type(instance):
    assert isinstance(instance.isClosed, bool)


@given(instance=BPMN2Model::Collaboration_strategy)
def test_bpmn2model::collaboration_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=BPMN2Model::Collaboration_strategy)
def test_bpmn2model::collaboration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Collaboration_strategy)
def test_bpmn2model::collaboration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Choreography_strategy)
@settings(max_examples=50)
def test_bpmn2model::choreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Choreography)

@given(instance=BPMN2Model::CategoryValue_strategy)
@settings(max_examples=50)
def test_bpmn2model::categoryvalue_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CategoryValue)

@given(instance=BPMN2Model::CategoryValue_strategy)
def test_bpmn2model::categoryvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=BPMN2Model::CategoryValue_strategy)
def test_bpmn2model::categoryvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BPMN2Model::Category_strategy)
@settings(max_examples=50)
def test_bpmn2model::category_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Category)

@given(instance=BPMN2Model::Category_strategy)
def test_bpmn2model::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Category_strategy)
def test_bpmn2model::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::CatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::catchevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CatchEvent)

@given(instance=BPMN2Model::CatchEvent_strategy)
def test_bpmn2model::catchevent_parallelMultiple_type(instance):
    assert isinstance(instance.parallelMultiple, bool)


@given(instance=BPMN2Model::CatchEvent_strategy)
def test_bpmn2model::catchevent_parallelMultiple_setter(instance):
    original = instance.parallelMultiple
    instance.parallelMultiple = original
    assert instance.parallelMultiple == original

@given(instance=BPMN2Model::FlowElement_strategy)
@settings(max_examples=50)
def test_bpmn2model::flowelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model::FlowElement)

@given(instance=BPMN2Model::FlowElement_strategy)
def test_bpmn2model::flowelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::FlowElement_strategy)
def test_bpmn2model::flowelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::AdHocSubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2model::adhocsubprocess_instantiation(instance):
    assert isinstance(instance, BPMN2Model::AdHocSubProcess)

@given(instance=BPMN2Model::AdHocSubProcess_strategy)
def test_bpmn2model::adhocsubprocess_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=BPMN2Model::AdHocSubProcess_strategy)
def test_bpmn2model::adhocsubprocess_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=BPMN2Model::AdHocSubProcess_strategy)
def test_bpmn2model::adhocsubprocess_cancelRemainingInstances_type(instance):
    assert isinstance(instance.cancelRemainingInstances, bool)


@given(instance=BPMN2Model::AdHocSubProcess_strategy)
def test_bpmn2model::adhocsubprocess_cancelRemainingInstances_setter(instance):
    original = instance.cancelRemainingInstances
    instance.cancelRemainingInstances = original
    assert instance.cancelRemainingInstances == original

@given(instance=BPMN2Model::CancelEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::canceleventdefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CancelEventDefinition)

@given(instance=BPMN2Model::CallConversation_strategy)
@settings(max_examples=50)
def test_bpmn2model::callconversation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CallConversation)

@given(instance=BPMN2Model::CallChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2model::callchoreography_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CallChoreography)

@given(instance=BPMN2Model::CallActivity_strategy)
@settings(max_examples=50)
def test_bpmn2model::callactivity_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CallActivity)

@given(instance=BPMN2Model::CallableElement_strategy)
@settings(max_examples=50)
def test_bpmn2model::callableelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model::CallableElement)

@given(instance=BPMN2Model::CallableElement_strategy)
def test_bpmn2model::callableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::CallableElement_strategy)
def test_bpmn2model::callableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::BusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::businessruletask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::BusinessRuleTask)

@given(instance=BPMN2Model::BusinessRuleTask_strategy)
def test_bpmn2model::businessruletask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::BusinessRuleTask_strategy)
def test_bpmn2model::businessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::BoundaryEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::boundaryevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::BoundaryEvent)

@given(instance=BPMN2Model::BoundaryEvent_strategy)
def test_bpmn2model::boundaryevent_cancelActivity_type(instance):
    assert isinstance(instance.cancelActivity, bool)


@given(instance=BPMN2Model::BoundaryEvent_strategy)
def test_bpmn2model::boundaryevent_cancelActivity_setter(instance):
    original = instance.cancelActivity
    instance.cancelActivity = original
    assert instance.cancelActivity == original

@given(instance=BPMN2Model::Auditing_strategy)
@settings(max_examples=50)
def test_bpmn2model::auditing_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Auditing)

@given(instance=BPMN2Model::Association_strategy)
@settings(max_examples=50)
def test_bpmn2model::association_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Association)

@given(instance=BPMN2Model::Association_strategy)
def test_bpmn2model::association_associationDirection_type(instance):
    assert isinstance(instance.associationDirection, str)


@given(instance=BPMN2Model::Association_strategy)
def test_bpmn2model::association_associationDirection_setter(instance):
    original = instance.associationDirection
    instance.associationDirection = original
    assert instance.associationDirection == original

@given(instance=BPMN2Model::Assignment_strategy)
@settings(max_examples=50)
def test_bpmn2model::assignment_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Assignment)

@given(instance=BPMN2Model::Artifact_strategy)
@settings(max_examples=50)
def test_bpmn2model::artifact_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Artifact)

@given(instance=BPMN2Model::Activity_strategy)
@settings(max_examples=50)
def test_bpmn2model::activity_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Activity)

@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_isForCompensation_type(instance):
    assert isinstance(instance.isForCompensation, bool)


@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_isForCompensation_setter(instance):
    original = instance.isForCompensation
    instance.isForCompensation = original
    assert instance.isForCompensation == original

@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_startQuantity_type(instance):
    assert isinstance(instance.startQuantity, int)


@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_startQuantity_setter(instance):
    original = instance.startQuantity
    instance.startQuantity = original
    assert instance.startQuantity == original

@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_completionQuantity_type(instance):
    assert isinstance(instance.completionQuantity, int)


@given(instance=BPMN2Model::Activity_strategy)
def test_bpmn2model::activity_completionQuantity_setter(instance):
    original = instance.completionQuantity
    instance.completionQuantity = original
    assert instance.completionQuantity == original

@given(instance=BPMN2Model::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_bpmn2model::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EStringToStringMapEntry)

@given(instance=BPMNBase_strategy)
@settings(max_examples=50)
def test_bpmnbase_instantiation(instance):
    assert isinstance(instance, BPMNBase)

@given(instance=BPMN2Model::ResourceParameterBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model::resourceparameterbinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ResourceParameterBinding)

@given(instance=BPMN2Model::InteractionNode_strategy)
@settings(max_examples=50)
def test_bpmn2model::interactionnode_instantiation(instance):
    assert isinstance(instance, BPMN2Model::InteractionNode)

@given(instance=BPMN2Model::BaseElement_strategy)
@settings(max_examples=50)
def test_bpmn2model::baseelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model::BaseElement)

@given(instance=BPMN2Model::BaseElement_strategy)
def test_bpmn2model::baseelement_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=BPMN2Model::BaseElement_strategy)
def test_bpmn2model::baseelement_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=BPMN2Model::BaseElement_strategy)
def test_bpmn2model::baseelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=BPMN2Model::BaseElement_strategy)
def test_bpmn2model::baseelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=BPMN2Model::ParticipantMultiplicity_strategy)
@settings(max_examples=50)
def test_bpmn2model::participantmultiplicity_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ParticipantMultiplicity)

@given(instance=BPMN2Model::ParticipantMultiplicity_strategy)
def test_bpmn2model::participantmultiplicity_maximum_type(instance):
    assert isinstance(instance.maximum, int)


@given(instance=BPMN2Model::ParticipantMultiplicity_strategy)
def test_bpmn2model::participantmultiplicity_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=BPMN2Model::ParticipantMultiplicity_strategy)
def test_bpmn2model::participantmultiplicity_minimum_type(instance):
    assert isinstance(instance.minimum, int)


@given(instance=BPMN2Model::ParticipantMultiplicity_strategy)
def test_bpmn2model::participantmultiplicity_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=BPMN2Model::ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::extensiondefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ExtensionDefinition)

@given(instance=BPMN2Model::ExtensionDefinition_strategy)
def test_bpmn2model::extensiondefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ExtensionDefinition_strategy)
def test_bpmn2model::extensiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::InputOutputBinding_strategy)
@settings(max_examples=50)
def test_bpmn2model::inputoutputbinding_instantiation(instance):
    assert isinstance(instance, BPMN2Model::InputOutputBinding)

@given(instance=BPMN2Model::ResourceAssignmentExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model::resourceassignmentexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ResourceAssignmentExpression)

@given(instance=BPMN2Model::Escalation_strategy)
@settings(max_examples=50)
def test_bpmn2model::escalation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Escalation)

@given(instance=BPMN2Model::Escalation_strategy)
def test_bpmn2model::escalation_escalationCode_type(instance):
    assert isinstance(instance.escalationCode, str)


@given(instance=BPMN2Model::Escalation_strategy)
def test_bpmn2model::escalation_escalationCode_setter(instance):
    original = instance.escalationCode
    instance.escalationCode = original
    assert instance.escalationCode == original

@given(instance=BPMN2Model::Escalation_strategy)
def test_bpmn2model::escalation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Escalation_strategy)
def test_bpmn2model::escalation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Import_strategy)
@settings(max_examples=50)
def test_bpmn2model::import_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Import)

@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_importType_type(instance):
    assert isinstance(instance.importType, str)


@given(instance=BPMN2Model::Import_strategy)
def test_bpmn2model::import_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original

@given(instance=BPMN2Model::ExtensionAttributeValue_strategy)
@settings(max_examples=50)
def test_bpmn2model::extensionattributevalue_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ExtensionAttributeValue)

@given(instance=BPMN2Model::ExtensionAttributeValue_strategy)
def test_bpmn2model::extensionattributevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=BPMN2Model::ExtensionAttributeValue_strategy)
def test_bpmn2model::extensionattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BPMN2Model::Extension_strategy)
@settings(max_examples=50)
def test_bpmn2model::extension_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Extension)

@given(instance=BPMN2Model::Extension_strategy)
def test_bpmn2model::extension_xsdDefinition_type(instance):
    assert isinstance(instance.xsdDefinition, str)


@given(instance=BPMN2Model::Extension_strategy)
def test_bpmn2model::extension_xsdDefinition_setter(instance):
    original = instance.xsdDefinition
    instance.xsdDefinition = original
    assert instance.xsdDefinition == original

@given(instance=BPMN2Model::Extension_strategy)
def test_bpmn2model::extension_mustUnderstand_type(instance):
    assert isinstance(instance.mustUnderstand, bool)


@given(instance=BPMN2Model::Extension_strategy)
def test_bpmn2model::extension_mustUnderstand_setter(instance):
    original = instance.mustUnderstand
    instance.mustUnderstand = original
    assert instance.mustUnderstand == original

@given(instance=BPMN2Model::DocumentRoot_strategy)
@settings(max_examples=50)
def test_bpmn2model::documentroot_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DocumentRoot)

@given(instance=BPMN2Model::DocumentRoot_strategy)
def test_bpmn2model::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=BPMN2Model::DocumentRoot_strategy)
def test_bpmn2model::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=BPMN2Model::BPMNBase_strategy)
@settings(max_examples=50)
def test_bpmn2model::bpmnbase_instantiation(instance):
    assert isinstance(instance, BPMN2Model::BPMNBase)

@given(instance=HumanPerformer_strategy)
@settings(max_examples=50)
def test_humanperformer_instantiation(instance):
    assert isinstance(instance, HumanPerformer)

@given(instance=BPMN2Model::PotentialOwner_strategy)
@settings(max_examples=50)
def test_bpmn2model::potentialowner_instantiation(instance):
    assert isinstance(instance, BPMN2Model::PotentialOwner)

@given(instance=ResourceRole_strategy)
@settings(max_examples=50)
def test_resourcerole_instantiation(instance):
    assert isinstance(instance, ResourceRole)

@given(instance=BPMN2Model::Performer_strategy)
@settings(max_examples=50)
def test_bpmn2model::performer_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Performer)

@given(instance=LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, LoopCharacteristics)

@given(instance=BPMN2Model::MultiInstanceLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model::multiinstanceloopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model::MultiInstanceLoopCharacteristics)

@given(instance=BPMN2Model::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model::multiinstanceloopcharacteristics_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=BPMN2Model::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model::multiinstanceloopcharacteristics_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=BPMN2Model::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model::multiinstanceloopcharacteristics_isSequential_type(instance):
    assert isinstance(instance.isSequential, bool)


@given(instance=BPMN2Model::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2model::multiinstanceloopcharacteristics_isSequential_setter(instance):
    original = instance.isSequential
    instance.isSequential = original
    assert instance.isSequential == original

@given(instance=BPMN2Model::StandardLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2model::standardloopcharacteristics_instantiation(instance):
    assert isinstance(instance, BPMN2Model::StandardLoopCharacteristics)

@given(instance=BPMN2Model::StandardLoopCharacteristics_strategy)
def test_bpmn2model::standardloopcharacteristics_testBefore_type(instance):
    assert isinstance(instance.testBefore, bool)


@given(instance=BPMN2Model::StandardLoopCharacteristics_strategy)
def test_bpmn2model::standardloopcharacteristics_testBefore_setter(instance):
    original = instance.testBefore
    instance.testBefore = original
    assert instance.testBefore == original

@given(instance=Performer_strategy)
@settings(max_examples=50)
def test_performer_instantiation(instance):
    assert isinstance(instance, Performer)

@given(instance=BPMN2Model::HumanPerformer_strategy)
@settings(max_examples=50)
def test_bpmn2model::humanperformer_instantiation(instance):
    assert isinstance(instance, BPMN2Model::HumanPerformer)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=BPMN2Model::Process_strategy)
@settings(max_examples=50)
def test_bpmn2model::process_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Process)

@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_processType_type(instance):
    assert isinstance(instance.processType, str)


@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_processType_setter(instance):
    original = instance.processType
    instance.processType = original
    assert instance.processType == original

@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_isExecutable_type(instance):
    assert isinstance(instance.isExecutable, bool)


@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_isExecutable_setter(instance):
    original = instance.isExecutable
    instance.isExecutable = original
    assert instance.isExecutable == original

@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_isClosed_type(instance):
    assert isinstance(instance.isClosed, bool)


@given(instance=BPMN2Model::Process_strategy)
def test_bpmn2model::process_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=BPMN2Model::GlobalTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globaltask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalTask)

@given(instance=Choreography_strategy)
@settings(max_examples=50)
def test_choreography_instantiation(instance):
    assert isinstance(instance, Choreography)

@given(instance=BPMN2Model::GlobalChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalchoreographytask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalChoreographyTask)

@given(instance=GlobalTask_strategy)
@settings(max_examples=50)
def test_globaltask_instantiation(instance):
    assert isinstance(instance, GlobalTask)

@given(instance=BPMN2Model::GlobalUserTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalusertask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalUserTask)

@given(instance=BPMN2Model::GlobalUserTask_strategy)
def test_bpmn2model::globalusertask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::GlobalUserTask_strategy)
def test_bpmn2model::globalusertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=BPMN2Model::GlobalScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalscripttask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalScriptTask)

@given(instance=BPMN2Model::GlobalScriptTask_strategy)
def test_bpmn2model::globalscripttask_scriptLanguage_type(instance):
    assert isinstance(instance.scriptLanguage, str)


@given(instance=BPMN2Model::GlobalScriptTask_strategy)
def test_bpmn2model::globalscripttask_scriptLanguage_setter(instance):
    original = instance.scriptLanguage
    instance.scriptLanguage = original
    assert instance.scriptLanguage == original

@given(instance=BPMN2Model::GlobalScriptTask_strategy)
def test_bpmn2model::globalscripttask_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=BPMN2Model::GlobalScriptTask_strategy)
def test_bpmn2model::globalscripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=BPMN2Model::GlobalManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalmanualtask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalManualTask)

@given(instance=BPMN2Model::GlobalBusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2model::globalbusinessruletask_instantiation(instance):
    assert isinstance(instance, BPMN2Model::GlobalBusinessRuleTask)

@given(instance=BPMN2Model::GlobalBusinessRuleTask_strategy)
def test_bpmn2model::globalbusinessruletask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=BPMN2Model::GlobalBusinessRuleTask_strategy)
def test_bpmn2model::globalbusinessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=BPMN2Model::FormalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2model::formalexpression_instantiation(instance):
    assert isinstance(instance, BPMN2Model::FormalExpression)

@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=BPMN2Model::FormalExpression_strategy)
def test_bpmn2model::formalexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=BPMN2Model::FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_bpmn2model::flowelementscontainer_instantiation(instance):
    assert isinstance(instance, BPMN2Model::FlowElementsContainer)

@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2model::extensionattributedefinition_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ExtensionAttributeDefinition)

@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_isReference_type(instance):
    assert isinstance(instance.isReference, bool)


@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original

@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ExtensionAttributeDefinition_strategy)
def test_bpmn2model::extensionattributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ThrowEvent_strategy)
@settings(max_examples=50)
def test_throwevent_instantiation(instance):
    assert isinstance(instance, ThrowEvent)

@given(instance=BPMN2Model::IntermediateThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::intermediatethrowevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::IntermediateThrowEvent)

@given(instance=BPMN2Model::ImplicitThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::implicitthrowevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ImplicitThrowEvent)

@given(instance=BPMN2Model::EndEvent_strategy)
@settings(max_examples=50)
def test_bpmn2model::endevent_instantiation(instance):
    assert isinstance(instance, BPMN2Model::EndEvent)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=BPMN2Model::SequenceFlow_strategy)
@settings(max_examples=50)
def test_bpmn2model::sequenceflow_instantiation(instance):
    assert isinstance(instance, BPMN2Model::SequenceFlow)

@given(instance=BPMN2Model::SequenceFlow_strategy)
def test_bpmn2model::sequenceflow_isImmediate_type(instance):
    assert isinstance(instance.isImmediate, bool)


@given(instance=BPMN2Model::SequenceFlow_strategy)
def test_bpmn2model::sequenceflow_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original

@given(instance=BPMN2Model::FlowNode_strategy)
@settings(max_examples=50)
def test_bpmn2model::flownode_instantiation(instance):
    assert isinstance(instance, BPMN2Model::FlowNode)

@given(instance=DataAssociation_strategy)
@settings(max_examples=50)
def test_dataassociation_instantiation(instance):
    assert isinstance(instance, DataAssociation)

@given(instance=BPMN2Model::DataInputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::datainputassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataInputAssociation)

@given(instance=BPMN2Model::DataOutputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2model::dataoutputassociation_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataOutputAssociation)

@given(instance=ItemAwareElement_strategy)
@settings(max_examples=50)
def test_itemawareelement_instantiation(instance):
    assert isinstance(instance, ItemAwareElement)

@given(instance=BPMN2Model::DataInput_strategy)
@settings(max_examples=50)
def test_bpmn2model::datainput_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataInput)

@given(instance=BPMN2Model::DataInput_strategy)
def test_bpmn2model::datainput_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=BPMN2Model::DataInput_strategy)
def test_bpmn2model::datainput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model::DataInput_strategy)
def test_bpmn2model::datainput_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::DataInput_strategy)
def test_bpmn2model::datainput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::DataObjectReference_strategy)
@settings(max_examples=50)
def test_bpmn2model::dataobjectreference_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataObjectReference)

@given(instance=BPMN2Model::DataStoreReference_strategy)
@settings(max_examples=50)
def test_bpmn2model::datastorereference_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataStoreReference)

@given(instance=BPMN2Model::Property_strategy)
@settings(max_examples=50)
def test_bpmn2model::property_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Property)

@given(instance=BPMN2Model::Property_strategy)
def test_bpmn2model::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Property_strategy)
def test_bpmn2model::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::DataStore_strategy)
@settings(max_examples=50)
def test_bpmn2model::datastore_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataStore)

@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_isUnlimited_type(instance):
    assert isinstance(instance.isUnlimited, bool)


@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_isUnlimited_setter(instance):
    original = instance.isUnlimited
    instance.isUnlimited = original
    assert instance.isUnlimited == original

@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=BPMN2Model::DataStore_strategy)
def test_bpmn2model::datastore_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=BPMN2Model::DataOutput_strategy)
@settings(max_examples=50)
def test_bpmn2model::dataoutput_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataOutput)

@given(instance=BPMN2Model::DataOutput_strategy)
def test_bpmn2model::dataoutput_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=BPMN2Model::DataOutput_strategy)
def test_bpmn2model::dataoutput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model::DataOutput_strategy)
def test_bpmn2model::dataoutput_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::DataOutput_strategy)
def test_bpmn2model::dataoutput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::DataObject_strategy)
@settings(max_examples=50)
def test_bpmn2model::dataobject_instantiation(instance):
    assert isinstance(instance, BPMN2Model::DataObject)

@given(instance=BPMN2Model::DataObject_strategy)
def test_bpmn2model::dataobject_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=BPMN2Model::DataObject_strategy)
def test_bpmn2model::dataobject_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=BPMN2Model::ItemAwareElement_strategy)
@settings(max_examples=50)
def test_bpmn2model::itemawareelement_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ItemAwareElement)

@given(instance=InteractionNode_strategy)
@settings(max_examples=50)
def test_interactionnode_instantiation(instance):
    assert isinstance(instance, InteractionNode)

@given(instance=BPMN2Model::Task_strategy)
@settings(max_examples=50)
def test_bpmn2model::task_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Task)

@given(instance=BPMN2Model::ConversationNode_strategy)
@settings(max_examples=50)
def test_bpmn2model::conversationnode_instantiation(instance):
    assert isinstance(instance, BPMN2Model::ConversationNode)

@given(instance=BPMN2Model::ConversationNode_strategy)
def test_bpmn2model::conversationnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::ConversationNode_strategy)
def test_bpmn2model::conversationnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BPMN2Model::Event_strategy)
@settings(max_examples=50)
def test_bpmn2model::event_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Event)

@given(instance=BPMN2Model::Participant_strategy)
@settings(max_examples=50)
def test_bpmn2model::participant_instantiation(instance):
    assert isinstance(instance, BPMN2Model::Participant)

@given(instance=BPMN2Model::Participant_strategy)
def test_bpmn2model::participant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BPMN2Model::Participant_strategy)
def test_bpmn2model::participant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
