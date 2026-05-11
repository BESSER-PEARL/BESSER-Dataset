import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HumanPerformer,
    ResourceRole,
    LoopCharacteristics,
    Performer,
    Choreography,
    GlobalTask,
    Expression,
    CallableElement,
    bpmn2::ExtensionAttributeDefinition,
    ThrowEvent,
    bpmn2::BPMNDiagram,
    DataAssociation,
    bpmn2::Document,
    ItemAwareElement,
    FlowElement,
    InteractionNode,
    bpmn2::InteractionNode,
    Gateway,
    FlowElementsContainer,
    Collaboration,
    Event,
    EventDefinition,
    RootElement,
    ConversationNode,
    ChoreographyActivity,
    bpmn2::ExtensionDefinition,
    Artifact,
    BaseElement,
    bpmn2::ItemAwareElement,
    bpmn2::FlowElementsContainer,
    Activity,
    Task,
    CatchEvent,
    bpmn2::Role,
    bpmn2::Position,
    bpmn2::OrganisationalUnit,
    bpmn2::Criterion,
    bpmn2::Competency,
    SubProcess,
    FlowNode,
    bpmn2::UserTask,
    bpmn2::Transaction,
    bpmn2::TimerEventDefinition,
    bpmn2::ThrowEvent,
    bpmn2::TerminateEventDefinition,
    bpmn2::Task,
    bpmn2::TextAnnotation,
    bpmn2::SubChoreography,
    bpmn2::StartEvent,
    bpmn2::StandardLoopCharacteristics,
    bpmn2::SubProcess,
    bpmn2::SubConversation,
    bpmn2::Signal,
    bpmn2::ServiceTask,
    bpmn2::SequenceFlow,
    bpmn2::SignalEventDefinition,
    bpmn2::EObject,
    bpmn2::ResourceParameterBinding,
    bpmn2::ResourceParameter,
    bpmn2::SendTask,
    bpmn2::ScriptTask,
    bpmn2::Resource,
    bpmn2::Rendering,
    bpmn2::Relationship,
    bpmn2::ResourceAssignmentExpression,
    bpmn2::Process,
    bpmn2::PotentialOwner,
    bpmn2::PartnerRole,
    bpmn2::PartnerEntity,
    bpmn2::ParticipantMultiplicity,
    bpmn2::ReceiveTask,
    bpmn2::Property,
    bpmn2::ParallelGateway,
    bpmn2::OutputSet,
    bpmn2::Operation,
    bpmn2::ParticipantAssociation,
    bpmn2::Participant,
    bpmn2::MessageFlowAssociation,
    bpmn2::MessageFlow,
    bpmn2::MessageEventDefinition,
    bpmn2::MultiInstanceLoopCharacteristics,
    bpmn2::Monitoring,
    bpmn2::ManualTask,
    bpmn2::LoopCharacteristics,
    bpmn2::LinkEventDefinition,
    bpmn2::Message,
    bpmn2::ItemDefinition,
    bpmn2::InputOutputSpecification,
    bpmn2::InputOutputBinding,
    bpmn2::LaneSet,
    bpmn2::Lane,
    bpmn2::Interface,
    bpmn2::InputSet,
    bpmn2::InclusiveGateway,
    bpmn2::IntermediateThrowEvent,
    bpmn2::IntermediateCatchEvent,
    bpmn2::ResourceRole,
    bpmn2::Performer,
    bpmn2::HumanPerformer,
    bpmn2::Import,
    bpmn2::ImplicitThrowEvent,
    bpmn2::GlobalTask,
    bpmn2::GlobalScriptTask,
    bpmn2::GlobalManualTask,
    bpmn2::Group,
    bpmn2::GlobalUserTask,
    bpmn2::GlobalBusinessRuleTask,
    bpmn2::Gateway,
    bpmn2::FormalExpression,
    bpmn2::FlowNode,
    bpmn2::GlobalConversation,
    bpmn2::GlobalChoreographyTask,
    bpmn2::ExclusiveGateway,
    bpmn2::EventBasedGateway,
    bpmn2::Event,
    bpmn2::EscalationEventDefinition,
    bpmn2::ExtensionAttributeValue,
    bpmn2::Extension,
    bpmn2::Expression,
    bpmn2::Error,
    bpmn2::EndPoint,
    bpmn2::EndEvent,
    bpmn2::Documentation,
    bpmn2::Definitions,
    bpmn2::Escalation,
    bpmn2::ErrorEventDefinition,
    bpmn2::DataState,
    bpmn2::DataOutputAssociation,
    bpmn2::DataOutput,
    bpmn2::DataStoreReference,
    bpmn2::DataStore,
    bpmn2::DataInputAssociation,
    bpmn2::DataInput,
    bpmn2::DataAssociation,
    bpmn2::CorrelationSubscription,
    bpmn2::DataObjectReference,
    bpmn2::DataObject,
    bpmn2::CorrelationKey,
    bpmn2::ConversationLink,
    bpmn2::ConversationAssociation,
    bpmn2::Conversation,
    bpmn2::ConditionalEventDefinition,
    bpmn2::CorrelationPropertyRetrievalExpression,
    bpmn2::CorrelationPropertyBinding,
    bpmn2::CorrelationProperty,
    bpmn2::CompensateEventDefinition,
    bpmn2::ChoreographyTask,
    bpmn2::ChoreographyActivity,
    bpmn2::Collaboration,
    bpmn2::Choreography,
    bpmn2::ComplexGateway,
    bpmn2::ComplexBehaviorDefinition,
    bpmn2::RootElement,
    bpmn2::EventDefinition,
    bpmn2::CancelEventDefinition,
    bpmn2::ConversationNode,
    bpmn2::CallConversation,
    bpmn2::CategoryValue,
    bpmn2::Category,
    bpmn2::CatchEvent,
    bpmn2::Activity,
    bpmn2::BusinessRuleTask,
    bpmn2::BoundaryEvent,
    bpmn2::BaseElement,
    bpmn2::Auditing,
    bpmn2::Association,
    bpmn2::CallChoreography,
    bpmn2::Assignment,
    bpmn2::Artifact,
    bpmn2::CallActivity,
    bpmn2::FlowElement,
    bpmn2::AdHocSubProcess,
    bpmn2::CallableElement,
    bpmn2::EStringToStringMapEntry,
    bpmn2::DocumentRoot,
    ChoreographyLoopType,
    AdHocOrdering,
    EventBasedGatewayType,
    ProcessType,
    ItemKind,
    MultiInstanceBehavior,
    GatewayDirection,
    AssociationDirection,
    RelationshipDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_humanperformer_is_not_abstract():
    assert not inspect.isabstract(HumanPerformer)


def test_humanperformer_constructor_exists():
    assert callable(HumanPerformer.__init__)


def test_humanperformer_constructor_args():
    sig = inspect.signature(HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_resourcerole_is_not_abstract():
    assert not inspect.isabstract(ResourceRole)


def test_resourcerole_constructor_exists():
    assert callable(ResourceRole.__init__)


def test_resourcerole_constructor_args():
    sig = inspect.signature(ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(LoopCharacteristics)


def test_loopcharacteristics_constructor_exists():
    assert callable(LoopCharacteristics.__init__)


def test_loopcharacteristics_constructor_args():
    sig = inspect.signature(LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_performer_is_not_abstract():
    assert not inspect.isabstract(Performer)


def test_performer_constructor_exists():
    assert callable(Performer.__init__)


def test_performer_constructor_args():
    sig = inspect.signature(Performer.__init__)
    params = list(sig.parameters.keys())



def test_choreography_is_not_abstract():
    assert not inspect.isabstract(Choreography)


def test_choreography_constructor_exists():
    assert callable(Choreography.__init__)


def test_choreography_constructor_args():
    sig = inspect.signature(Choreography.__init__)
    params = list(sig.parameters.keys())



def test_globaltask_is_not_abstract():
    assert not inspect.isabstract(GlobalTask)


def test_globaltask_constructor_exists():
    assert callable(GlobalTask.__init__)


def test_globaltask_constructor_args():
    sig = inspect.signature(GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::extensionattributedefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ExtensionAttributeDefinition)


def test_bpmn2::extensionattributedefinition_constructor_exists():
    assert callable(bpmn2::ExtensionAttributeDefinition.__init__)


def test_bpmn2::extensionattributedefinition_constructor_args():
    sig = inspect.signature(bpmn2::ExtensionAttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isReference" in params, "Missing parameter 'isReference'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2::extensionattributedefinition_has_isReference():
    assert hasattr(bpmn2::ExtensionAttributeDefinition, "isReference")
    descriptor = None
    for klass in bpmn2::ExtensionAttributeDefinition.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::extensionattributedefinition_has_type():
    assert hasattr(bpmn2::ExtensionAttributeDefinition, "type")
    descriptor = None
    for klass in bpmn2::ExtensionAttributeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::extensionattributedefinition_has_name():
    assert hasattr(bpmn2::ExtensionAttributeDefinition, "name")
    descriptor = None
    for klass in bpmn2::ExtensionAttributeDefinition.__mro__:
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



def test_bpmn2::bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(bpmn2::BPMNDiagram)


def test_bpmn2::bpmndiagram_constructor_exists():
    assert callable(bpmn2::BPMNDiagram.__init__)


def test_bpmn2::bpmndiagram_constructor_args():
    sig = inspect.signature(bpmn2::BPMNDiagram.__init__)
    params = list(sig.parameters.keys())



def test_dataassociation_is_not_abstract():
    assert not inspect.isabstract(DataAssociation)


def test_dataassociation_constructor_exists():
    assert callable(DataAssociation.__init__)


def test_dataassociation_constructor_args():
    sig = inspect.signature(DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::document_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Document)


def test_bpmn2::document_constructor_exists():
    assert callable(bpmn2::Document.__init__)


def test_bpmn2::document_constructor_args():
    sig = inspect.signature(bpmn2::Document.__init__)
    params = list(sig.parameters.keys())



def test_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(ItemAwareElement)


def test_itemawareelement_constructor_exists():
    assert callable(ItemAwareElement.__init__)


def test_itemawareelement_constructor_args():
    sig = inspect.signature(ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_interactionnode_is_not_abstract():
    assert not inspect.isabstract(InteractionNode)


def test_interactionnode_constructor_exists():
    assert callable(InteractionNode.__init__)


def test_interactionnode_constructor_args():
    sig = inspect.signature(InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::interactionnode_is_not_abstract():
    assert not inspect.isabstract(bpmn2::InteractionNode)


def test_bpmn2::interactionnode_constructor_exists():
    assert callable(bpmn2::InteractionNode.__init__)


def test_bpmn2::interactionnode_constructor_args():
    sig = inspect.signature(bpmn2::InteractionNode.__init__)
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



def test_bpmn2::extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ExtensionDefinition)


def test_bpmn2::extensiondefinition_constructor_exists():
    assert callable(bpmn2::ExtensionDefinition.__init__)


def test_bpmn2::extensiondefinition_constructor_args():
    sig = inspect.signature(bpmn2::ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2::extensiondefinition_has_name():
    assert hasattr(bpmn2::ExtensionDefinition, "name")
    descriptor = None
    for klass in bpmn2::ExtensionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_bpmn2::itemawareelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ItemAwareElement)


def test_bpmn2::itemawareelement_constructor_exists():
    assert callable(bpmn2::ItemAwareElement.__init__)


def test_bpmn2::itemawareelement_constructor_args():
    sig = inspect.signature(bpmn2::ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(bpmn2::FlowElementsContainer)


def test_bpmn2::flowelementscontainer_constructor_exists():
    assert callable(bpmn2::FlowElementsContainer.__init__)


def test_bpmn2::flowelementscontainer_constructor_args():
    sig = inspect.signature(bpmn2::FlowElementsContainer.__init__)
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



def test_bpmn2::role_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Role)


def test_bpmn2::role_constructor_exists():
    assert callable(bpmn2::Role.__init__)


def test_bpmn2::role_constructor_args():
    sig = inspect.signature(bpmn2::Role.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::position_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Position)


def test_bpmn2::position_constructor_exists():
    assert callable(bpmn2::Position.__init__)


def test_bpmn2::position_constructor_args():
    sig = inspect.signature(bpmn2::Position.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::organisationalunit_is_not_abstract():
    assert not inspect.isabstract(bpmn2::OrganisationalUnit)


def test_bpmn2::organisationalunit_constructor_exists():
    assert callable(bpmn2::OrganisationalUnit.__init__)


def test_bpmn2::organisationalunit_constructor_args():
    sig = inspect.signature(bpmn2::OrganisationalUnit.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::criterion_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Criterion)


def test_bpmn2::criterion_constructor_exists():
    assert callable(bpmn2::Criterion.__init__)


def test_bpmn2::criterion_constructor_args():
    sig = inspect.signature(bpmn2::Criterion.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::competency_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Competency)


def test_bpmn2::competency_constructor_exists():
    assert callable(bpmn2::Competency.__init__)


def test_bpmn2::competency_constructor_args():
    sig = inspect.signature(bpmn2::Competency.__init__)
    params = list(sig.parameters.keys())



def test_subprocess_is_not_abstract():
    assert not inspect.isabstract(SubProcess)


def test_subprocess_constructor_exists():
    assert callable(SubProcess.__init__)


def test_subprocess_constructor_args():
    sig = inspect.signature(SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_flownode_is_not_abstract():
    assert not inspect.isabstract(FlowNode)


def test_flownode_constructor_exists():
    assert callable(FlowNode.__init__)


def test_flownode_constructor_args():
    sig = inspect.signature(FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::usertask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::UserTask)


def test_bpmn2::usertask_constructor_exists():
    assert callable(bpmn2::UserTask.__init__)


def test_bpmn2::usertask_constructor_args():
    sig = inspect.signature(bpmn2::UserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::usertask_has_implementation():
    assert hasattr(bpmn2::UserTask, "implementation")
    descriptor = None
    for klass in bpmn2::UserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::transaction_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Transaction)


def test_bpmn2::transaction_constructor_exists():
    assert callable(bpmn2::Transaction.__init__)


def test_bpmn2::transaction_constructor_args():
    sig = inspect.signature(bpmn2::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "protocol" in params, "Missing parameter 'protocol'"

def test_bpmn2::transaction_has_method():
    assert hasattr(bpmn2::Transaction, "method")
    descriptor = None
    for klass in bpmn2::Transaction.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::transaction_has_protocol():
    assert hasattr(bpmn2::Transaction, "protocol")
    descriptor = None
    for klass in bpmn2::Transaction.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::timereventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::TimerEventDefinition)


def test_bpmn2::timereventdefinition_constructor_exists():
    assert callable(bpmn2::TimerEventDefinition.__init__)


def test_bpmn2::timereventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::TimerEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::throwevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ThrowEvent)


def test_bpmn2::throwevent_constructor_exists():
    assert callable(bpmn2::ThrowEvent.__init__)


def test_bpmn2::throwevent_constructor_args():
    sig = inspect.signature(bpmn2::ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::terminateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::TerminateEventDefinition)


def test_bpmn2::terminateeventdefinition_constructor_exists():
    assert callable(bpmn2::TerminateEventDefinition.__init__)


def test_bpmn2::terminateeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::TerminateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::task_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Task)


def test_bpmn2::task_constructor_exists():
    assert callable(bpmn2::Task.__init__)


def test_bpmn2::task_constructor_args():
    sig = inspect.signature(bpmn2::Task.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::textannotation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::TextAnnotation)


def test_bpmn2::textannotation_constructor_exists():
    assert callable(bpmn2::TextAnnotation.__init__)


def test_bpmn2::textannotation_constructor_args():
    sig = inspect.signature(bpmn2::TextAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "textFormat" in params, "Missing parameter 'textFormat'"
    assert "text" in params, "Missing parameter 'text'"

def test_bpmn2::textannotation_has_textFormat():
    assert hasattr(bpmn2::TextAnnotation, "textFormat")
    descriptor = None
    for klass in bpmn2::TextAnnotation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::textannotation_has_text():
    assert hasattr(bpmn2::TextAnnotation, "text")
    descriptor = None
    for klass in bpmn2::TextAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::subchoreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SubChoreography)


def test_bpmn2::subchoreography_constructor_exists():
    assert callable(bpmn2::SubChoreography.__init__)


def test_bpmn2::subchoreography_constructor_args():
    sig = inspect.signature(bpmn2::SubChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::startevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::StartEvent)


def test_bpmn2::startevent_constructor_exists():
    assert callable(bpmn2::StartEvent.__init__)


def test_bpmn2::startevent_constructor_args():
    sig = inspect.signature(bpmn2::StartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isInterrupting" in params, "Missing parameter 'isInterrupting'"

def test_bpmn2::startevent_has_isInterrupting():
    assert hasattr(bpmn2::StartEvent, "isInterrupting")
    descriptor = None
    for klass in bpmn2::StartEvent.__mro__:
        if "isInterrupting" in klass.__dict__:
            descriptor = klass.__dict__["isInterrupting"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::standardloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2::StandardLoopCharacteristics)


def test_bpmn2::standardloopcharacteristics_constructor_exists():
    assert callable(bpmn2::StandardLoopCharacteristics.__init__)


def test_bpmn2::standardloopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2::StandardLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "testBefore" in params, "Missing parameter 'testBefore'"
    assert "loopMaximum" in params, "Missing parameter 'loopMaximum'"

def test_bpmn2::standardloopcharacteristics_has_testBefore():
    assert hasattr(bpmn2::StandardLoopCharacteristics, "testBefore")
    descriptor = None
    for klass in bpmn2::StandardLoopCharacteristics.__mro__:
        if "testBefore" in klass.__dict__:
            descriptor = klass.__dict__["testBefore"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::standardloopcharacteristics_has_loopMaximum():
    assert hasattr(bpmn2::StandardLoopCharacteristics, "loopMaximum")
    descriptor = None
    for klass in bpmn2::StandardLoopCharacteristics.__mro__:
        if "loopMaximum" in klass.__dict__:
            descriptor = klass.__dict__["loopMaximum"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::subprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SubProcess)


def test_bpmn2::subprocess_constructor_exists():
    assert callable(bpmn2::SubProcess.__init__)


def test_bpmn2::subprocess_constructor_args():
    sig = inspect.signature(bpmn2::SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "triggeredByEvent" in params, "Missing parameter 'triggeredByEvent'"

def test_bpmn2::subprocess_has_triggeredByEvent():
    assert hasattr(bpmn2::SubProcess, "triggeredByEvent")
    descriptor = None
    for klass in bpmn2::SubProcess.__mro__:
        if "triggeredByEvent" in klass.__dict__:
            descriptor = klass.__dict__["triggeredByEvent"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::subconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SubConversation)


def test_bpmn2::subconversation_constructor_exists():
    assert callable(bpmn2::SubConversation.__init__)


def test_bpmn2::subconversation_constructor_args():
    sig = inspect.signature(bpmn2::SubConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::signal_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Signal)


def test_bpmn2::signal_constructor_exists():
    assert callable(bpmn2::Signal.__init__)


def test_bpmn2::signal_constructor_args():
    sig = inspect.signature(bpmn2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::servicetask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ServiceTask)


def test_bpmn2::servicetask_constructor_exists():
    assert callable(bpmn2::ServiceTask.__init__)


def test_bpmn2::servicetask_constructor_args():
    sig = inspect.signature(bpmn2::ServiceTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::servicetask_has_implementation():
    assert hasattr(bpmn2::ServiceTask, "implementation")
    descriptor = None
    for klass in bpmn2::ServiceTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::sequenceflow_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SequenceFlow)


def test_bpmn2::sequenceflow_constructor_exists():
    assert callable(bpmn2::SequenceFlow.__init__)


def test_bpmn2::sequenceflow_constructor_args():
    sig = inspect.signature(bpmn2::SequenceFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"

def test_bpmn2::sequenceflow_has_isImmediate():
    assert hasattr(bpmn2::SequenceFlow, "isImmediate")
    descriptor = None
    for klass in bpmn2::SequenceFlow.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::signaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SignalEventDefinition)


def test_bpmn2::signaleventdefinition_constructor_exists():
    assert callable(bpmn2::SignalEventDefinition.__init__)


def test_bpmn2::signaleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::SignalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::eobject_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EObject)


def test_bpmn2::eobject_constructor_exists():
    assert callable(bpmn2::EObject.__init__)


def test_bpmn2::eobject_constructor_args():
    sig = inspect.signature(bpmn2::EObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::resourceparameterbinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ResourceParameterBinding)


def test_bpmn2::resourceparameterbinding_constructor_exists():
    assert callable(bpmn2::ResourceParameterBinding.__init__)


def test_bpmn2::resourceparameterbinding_constructor_args():
    sig = inspect.signature(bpmn2::ResourceParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::resourceparameter_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ResourceParameter)


def test_bpmn2::resourceparameter_constructor_exists():
    assert callable(bpmn2::ResourceParameter.__init__)


def test_bpmn2::resourceparameter_constructor_args():
    sig = inspect.signature(bpmn2::ResourceParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_bpmn2::resourceparameter_has_isRequired():
    assert hasattr(bpmn2::ResourceParameter, "isRequired")
    descriptor = None
    for klass in bpmn2::ResourceParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::sendtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::SendTask)


def test_bpmn2::sendtask_constructor_exists():
    assert callable(bpmn2::SendTask.__init__)


def test_bpmn2::sendtask_constructor_args():
    sig = inspect.signature(bpmn2::SendTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::sendtask_has_implementation():
    assert hasattr(bpmn2::SendTask, "implementation")
    descriptor = None
    for klass in bpmn2::SendTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::scripttask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ScriptTask)


def test_bpmn2::scripttask_constructor_exists():
    assert callable(bpmn2::ScriptTask.__init__)


def test_bpmn2::scripttask_constructor_args():
    sig = inspect.signature(bpmn2::ScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "scriptFormat" in params, "Missing parameter 'scriptFormat'"
    assert "script" in params, "Missing parameter 'script'"

def test_bpmn2::scripttask_has_scriptFormat():
    assert hasattr(bpmn2::ScriptTask, "scriptFormat")
    descriptor = None
    for klass in bpmn2::ScriptTask.__mro__:
        if "scriptFormat" in klass.__dict__:
            descriptor = klass.__dict__["scriptFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::scripttask_has_script():
    assert hasattr(bpmn2::ScriptTask, "script")
    descriptor = None
    for klass in bpmn2::ScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::resource_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Resource)


def test_bpmn2::resource_constructor_exists():
    assert callable(bpmn2::Resource.__init__)


def test_bpmn2::resource_constructor_args():
    sig = inspect.signature(bpmn2::Resource.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::rendering_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Rendering)


def test_bpmn2::rendering_constructor_exists():
    assert callable(bpmn2::Rendering.__init__)


def test_bpmn2::rendering_constructor_args():
    sig = inspect.signature(bpmn2::Rendering.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::relationship_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Relationship)


def test_bpmn2::relationship_constructor_exists():
    assert callable(bpmn2::Relationship.__init__)


def test_bpmn2::relationship_constructor_args():
    sig = inspect.signature(bpmn2::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_bpmn2::relationship_has_type():
    assert hasattr(bpmn2::Relationship, "type")
    descriptor = None
    for klass in bpmn2::Relationship.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::relationship_has_direction():
    assert hasattr(bpmn2::Relationship, "direction")
    descriptor = None
    for klass in bpmn2::Relationship.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::resourceassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ResourceAssignmentExpression)


def test_bpmn2::resourceassignmentexpression_constructor_exists():
    assert callable(bpmn2::ResourceAssignmentExpression.__init__)


def test_bpmn2::resourceassignmentexpression_constructor_args():
    sig = inspect.signature(bpmn2::ResourceAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::process_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Process)


def test_bpmn2::process_constructor_exists():
    assert callable(bpmn2::Process.__init__)


def test_bpmn2::process_constructor_args():
    sig = inspect.signature(bpmn2::Process.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "processType" in params, "Missing parameter 'processType'"
    assert "isExecutable" in params, "Missing parameter 'isExecutable'"

def test_bpmn2::process_has_isClosed():
    assert hasattr(bpmn2::Process, "isClosed")
    descriptor = None
    for klass in bpmn2::Process.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::process_has_processType():
    assert hasattr(bpmn2::Process, "processType")
    descriptor = None
    for klass in bpmn2::Process.__mro__:
        if "processType" in klass.__dict__:
            descriptor = klass.__dict__["processType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::process_has_isExecutable():
    assert hasattr(bpmn2::Process, "isExecutable")
    descriptor = None
    for klass in bpmn2::Process.__mro__:
        if "isExecutable" in klass.__dict__:
            descriptor = klass.__dict__["isExecutable"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::potentialowner_is_not_abstract():
    assert not inspect.isabstract(bpmn2::PotentialOwner)


def test_bpmn2::potentialowner_constructor_exists():
    assert callable(bpmn2::PotentialOwner.__init__)


def test_bpmn2::potentialowner_constructor_args():
    sig = inspect.signature(bpmn2::PotentialOwner.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::partnerrole_is_not_abstract():
    assert not inspect.isabstract(bpmn2::PartnerRole)


def test_bpmn2::partnerrole_constructor_exists():
    assert callable(bpmn2::PartnerRole.__init__)


def test_bpmn2::partnerrole_constructor_args():
    sig = inspect.signature(bpmn2::PartnerRole.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::partnerentity_is_not_abstract():
    assert not inspect.isabstract(bpmn2::PartnerEntity)


def test_bpmn2::partnerentity_constructor_exists():
    assert callable(bpmn2::PartnerEntity.__init__)


def test_bpmn2::partnerentity_constructor_args():
    sig = inspect.signature(bpmn2::PartnerEntity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::participantmultiplicity_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ParticipantMultiplicity)


def test_bpmn2::participantmultiplicity_constructor_exists():
    assert callable(bpmn2::ParticipantMultiplicity.__init__)


def test_bpmn2::participantmultiplicity_constructor_args():
    sig = inspect.signature(bpmn2::ParticipantMultiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"

def test_bpmn2::participantmultiplicity_has_minimum():
    assert hasattr(bpmn2::ParticipantMultiplicity, "minimum")
    descriptor = None
    for klass in bpmn2::ParticipantMultiplicity.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::participantmultiplicity_has_maximum():
    assert hasattr(bpmn2::ParticipantMultiplicity, "maximum")
    descriptor = None
    for klass in bpmn2::ParticipantMultiplicity.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::receivetask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ReceiveTask)


def test_bpmn2::receivetask_constructor_exists():
    assert callable(bpmn2::ReceiveTask.__init__)


def test_bpmn2::receivetask_constructor_args():
    sig = inspect.signature(bpmn2::ReceiveTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "instantiate" in params, "Missing parameter 'instantiate'"

def test_bpmn2::receivetask_has_implementation():
    assert hasattr(bpmn2::ReceiveTask, "implementation")
    descriptor = None
    for klass in bpmn2::ReceiveTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::receivetask_has_instantiate():
    assert hasattr(bpmn2::ReceiveTask, "instantiate")
    descriptor = None
    for klass in bpmn2::ReceiveTask.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::property_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Property)


def test_bpmn2::property_constructor_exists():
    assert callable(bpmn2::Property.__init__)


def test_bpmn2::property_constructor_args():
    sig = inspect.signature(bpmn2::Property.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::parallelgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ParallelGateway)


def test_bpmn2::parallelgateway_constructor_exists():
    assert callable(bpmn2::ParallelGateway.__init__)


def test_bpmn2::parallelgateway_constructor_args():
    sig = inspect.signature(bpmn2::ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::outputset_is_not_abstract():
    assert not inspect.isabstract(bpmn2::OutputSet)


def test_bpmn2::outputset_constructor_exists():
    assert callable(bpmn2::OutputSet.__init__)


def test_bpmn2::outputset_constructor_args():
    sig = inspect.signature(bpmn2::OutputSet.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::operation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Operation)


def test_bpmn2::operation_constructor_exists():
    assert callable(bpmn2::Operation.__init__)


def test_bpmn2::operation_constructor_args():
    sig = inspect.signature(bpmn2::Operation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::participantassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ParticipantAssociation)


def test_bpmn2::participantassociation_constructor_exists():
    assert callable(bpmn2::ParticipantAssociation.__init__)


def test_bpmn2::participantassociation_constructor_args():
    sig = inspect.signature(bpmn2::ParticipantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::participant_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Participant)


def test_bpmn2::participant_constructor_exists():
    assert callable(bpmn2::Participant.__init__)


def test_bpmn2::participant_constructor_args():
    sig = inspect.signature(bpmn2::Participant.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::messageflowassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::MessageFlowAssociation)


def test_bpmn2::messageflowassociation_constructor_exists():
    assert callable(bpmn2::MessageFlowAssociation.__init__)


def test_bpmn2::messageflowassociation_constructor_args():
    sig = inspect.signature(bpmn2::MessageFlowAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::messageflow_is_not_abstract():
    assert not inspect.isabstract(bpmn2::MessageFlow)


def test_bpmn2::messageflow_constructor_exists():
    assert callable(bpmn2::MessageFlow.__init__)


def test_bpmn2::messageflow_constructor_args():
    sig = inspect.signature(bpmn2::MessageFlow.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::messageeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::MessageEventDefinition)


def test_bpmn2::messageeventdefinition_constructor_exists():
    assert callable(bpmn2::MessageEventDefinition.__init__)


def test_bpmn2::messageeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::MessageEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::multiinstanceloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2::MultiInstanceLoopCharacteristics)


def test_bpmn2::multiinstanceloopcharacteristics_constructor_exists():
    assert callable(bpmn2::MultiInstanceLoopCharacteristics.__init__)


def test_bpmn2::multiinstanceloopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2::MultiInstanceLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"
    assert "isSequential" in params, "Missing parameter 'isSequential'"

def test_bpmn2::multiinstanceloopcharacteristics_has_behavior():
    assert hasattr(bpmn2::MultiInstanceLoopCharacteristics, "behavior")
    descriptor = None
    for klass in bpmn2::MultiInstanceLoopCharacteristics.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::multiinstanceloopcharacteristics_has_isSequential():
    assert hasattr(bpmn2::MultiInstanceLoopCharacteristics, "isSequential")
    descriptor = None
    for klass in bpmn2::MultiInstanceLoopCharacteristics.__mro__:
        if "isSequential" in klass.__dict__:
            descriptor = klass.__dict__["isSequential"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::monitoring_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Monitoring)


def test_bpmn2::monitoring_constructor_exists():
    assert callable(bpmn2::Monitoring.__init__)


def test_bpmn2::monitoring_constructor_args():
    sig = inspect.signature(bpmn2::Monitoring.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::manualtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ManualTask)


def test_bpmn2::manualtask_constructor_exists():
    assert callable(bpmn2::ManualTask.__init__)


def test_bpmn2::manualtask_constructor_args():
    sig = inspect.signature(bpmn2::ManualTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2::LoopCharacteristics)


def test_bpmn2::loopcharacteristics_constructor_exists():
    assert callable(bpmn2::LoopCharacteristics.__init__)


def test_bpmn2::loopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2::LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::linkeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::LinkEventDefinition)


def test_bpmn2::linkeventdefinition_constructor_exists():
    assert callable(bpmn2::LinkEventDefinition.__init__)


def test_bpmn2::linkeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::LinkEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::message_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Message)


def test_bpmn2::message_constructor_exists():
    assert callable(bpmn2::Message.__init__)


def test_bpmn2::message_constructor_args():
    sig = inspect.signature(bpmn2::Message.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::itemdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ItemDefinition)


def test_bpmn2::itemdefinition_constructor_exists():
    assert callable(bpmn2::ItemDefinition.__init__)


def test_bpmn2::itemdefinition_constructor_args():
    sig = inspect.signature(bpmn2::ItemDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "itemKind" in params, "Missing parameter 'itemKind'"
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2::itemdefinition_has_itemKind():
    assert hasattr(bpmn2::ItemDefinition, "itemKind")
    descriptor = None
    for klass in bpmn2::ItemDefinition.__mro__:
        if "itemKind" in klass.__dict__:
            descriptor = klass.__dict__["itemKind"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::itemdefinition_has_isCollection():
    assert hasattr(bpmn2::ItemDefinition, "isCollection")
    descriptor = None
    for klass in bpmn2::ItemDefinition.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::inputoutputspecification_is_not_abstract():
    assert not inspect.isabstract(bpmn2::InputOutputSpecification)


def test_bpmn2::inputoutputspecification_constructor_exists():
    assert callable(bpmn2::InputOutputSpecification.__init__)


def test_bpmn2::inputoutputspecification_constructor_args():
    sig = inspect.signature(bpmn2::InputOutputSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::inputoutputbinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2::InputOutputBinding)


def test_bpmn2::inputoutputbinding_constructor_exists():
    assert callable(bpmn2::InputOutputBinding.__init__)


def test_bpmn2::inputoutputbinding_constructor_args():
    sig = inspect.signature(bpmn2::InputOutputBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::laneset_is_not_abstract():
    assert not inspect.isabstract(bpmn2::LaneSet)


def test_bpmn2::laneset_constructor_exists():
    assert callable(bpmn2::LaneSet.__init__)


def test_bpmn2::laneset_constructor_args():
    sig = inspect.signature(bpmn2::LaneSet.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::lane_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Lane)


def test_bpmn2::lane_constructor_exists():
    assert callable(bpmn2::Lane.__init__)


def test_bpmn2::lane_constructor_args():
    sig = inspect.signature(bpmn2::Lane.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::interface_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Interface)


def test_bpmn2::interface_constructor_exists():
    assert callable(bpmn2::Interface.__init__)


def test_bpmn2::interface_constructor_args():
    sig = inspect.signature(bpmn2::Interface.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::inputset_is_not_abstract():
    assert not inspect.isabstract(bpmn2::InputSet)


def test_bpmn2::inputset_constructor_exists():
    assert callable(bpmn2::InputSet.__init__)


def test_bpmn2::inputset_constructor_args():
    sig = inspect.signature(bpmn2::InputSet.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::inclusivegateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::InclusiveGateway)


def test_bpmn2::inclusivegateway_constructor_exists():
    assert callable(bpmn2::InclusiveGateway.__init__)


def test_bpmn2::inclusivegateway_constructor_args():
    sig = inspect.signature(bpmn2::InclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::intermediatethrowevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::IntermediateThrowEvent)


def test_bpmn2::intermediatethrowevent_constructor_exists():
    assert callable(bpmn2::IntermediateThrowEvent.__init__)


def test_bpmn2::intermediatethrowevent_constructor_args():
    sig = inspect.signature(bpmn2::IntermediateThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::intermediatecatchevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::IntermediateCatchEvent)


def test_bpmn2::intermediatecatchevent_constructor_exists():
    assert callable(bpmn2::IntermediateCatchEvent.__init__)


def test_bpmn2::intermediatecatchevent_constructor_args():
    sig = inspect.signature(bpmn2::IntermediateCatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::resourcerole_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ResourceRole)


def test_bpmn2::resourcerole_constructor_exists():
    assert callable(bpmn2::ResourceRole.__init__)


def test_bpmn2::resourcerole_constructor_args():
    sig = inspect.signature(bpmn2::ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::performer_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Performer)


def test_bpmn2::performer_constructor_exists():
    assert callable(bpmn2::Performer.__init__)


def test_bpmn2::performer_constructor_args():
    sig = inspect.signature(bpmn2::Performer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::humanperformer_is_not_abstract():
    assert not inspect.isabstract(bpmn2::HumanPerformer)


def test_bpmn2::humanperformer_constructor_exists():
    assert callable(bpmn2::HumanPerformer.__init__)


def test_bpmn2::humanperformer_constructor_args():
    sig = inspect.signature(bpmn2::HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::import_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Import)


def test_bpmn2::import_constructor_exists():
    assert callable(bpmn2::Import.__init__)


def test_bpmn2::import_constructor_args():
    sig = inspect.signature(bpmn2::Import.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "location" in params, "Missing parameter 'location'"
    assert "importType" in params, "Missing parameter 'importType'"

def test_bpmn2::import_has_namespace():
    assert hasattr(bpmn2::Import, "namespace")
    descriptor = None
    for klass in bpmn2::Import.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::import_has_location():
    assert hasattr(bpmn2::Import, "location")
    descriptor = None
    for klass in bpmn2::Import.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::import_has_importType():
    assert hasattr(bpmn2::Import, "importType")
    descriptor = None
    for klass in bpmn2::Import.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::implicitthrowevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ImplicitThrowEvent)


def test_bpmn2::implicitthrowevent_constructor_exists():
    assert callable(bpmn2::ImplicitThrowEvent.__init__)


def test_bpmn2::implicitthrowevent_constructor_args():
    sig = inspect.signature(bpmn2::ImplicitThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::globaltask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalTask)


def test_bpmn2::globaltask_constructor_exists():
    assert callable(bpmn2::GlobalTask.__init__)


def test_bpmn2::globaltask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::globalscripttask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalScriptTask)


def test_bpmn2::globalscripttask_constructor_exists():
    assert callable(bpmn2::GlobalScriptTask.__init__)


def test_bpmn2::globalscripttask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"
    assert "scriptLanguage" in params, "Missing parameter 'scriptLanguage'"

def test_bpmn2::globalscripttask_has_script():
    assert hasattr(bpmn2::GlobalScriptTask, "script")
    descriptor = None
    for klass in bpmn2::GlobalScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::globalscripttask_has_scriptLanguage():
    assert hasattr(bpmn2::GlobalScriptTask, "scriptLanguage")
    descriptor = None
    for klass in bpmn2::GlobalScriptTask.__mro__:
        if "scriptLanguage" in klass.__dict__:
            descriptor = klass.__dict__["scriptLanguage"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::globalmanualtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalManualTask)


def test_bpmn2::globalmanualtask_constructor_exists():
    assert callable(bpmn2::GlobalManualTask.__init__)


def test_bpmn2::globalmanualtask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalManualTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::group_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Group)


def test_bpmn2::group_constructor_exists():
    assert callable(bpmn2::Group.__init__)


def test_bpmn2::group_constructor_args():
    sig = inspect.signature(bpmn2::Group.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::globalusertask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalUserTask)


def test_bpmn2::globalusertask_constructor_exists():
    assert callable(bpmn2::GlobalUserTask.__init__)


def test_bpmn2::globalusertask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalUserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::globalusertask_has_implementation():
    assert hasattr(bpmn2::GlobalUserTask, "implementation")
    descriptor = None
    for klass in bpmn2::GlobalUserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::globalbusinessruletask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalBusinessRuleTask)


def test_bpmn2::globalbusinessruletask_constructor_exists():
    assert callable(bpmn2::GlobalBusinessRuleTask.__init__)


def test_bpmn2::globalbusinessruletask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalBusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::globalbusinessruletask_has_implementation():
    assert hasattr(bpmn2::GlobalBusinessRuleTask, "implementation")
    descriptor = None
    for klass in bpmn2::GlobalBusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::gateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Gateway)


def test_bpmn2::gateway_constructor_exists():
    assert callable(bpmn2::Gateway.__init__)


def test_bpmn2::gateway_constructor_args():
    sig = inspect.signature(bpmn2::Gateway.__init__)
    params = list(sig.parameters.keys())
    assert "gatewayDirection" in params, "Missing parameter 'gatewayDirection'"

def test_bpmn2::gateway_has_gatewayDirection():
    assert hasattr(bpmn2::Gateway, "gatewayDirection")
    descriptor = None
    for klass in bpmn2::Gateway.__mro__:
        if "gatewayDirection" in klass.__dict__:
            descriptor = klass.__dict__["gatewayDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::formalexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2::FormalExpression)


def test_bpmn2::formalexpression_constructor_exists():
    assert callable(bpmn2::FormalExpression.__init__)


def test_bpmn2::formalexpression_constructor_args():
    sig = inspect.signature(bpmn2::FormalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_bpmn2::formalexpression_has_mixed():
    assert hasattr(bpmn2::FormalExpression, "mixed")
    descriptor = None
    for klass in bpmn2::FormalExpression.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::formalexpression_has_body():
    assert hasattr(bpmn2::FormalExpression, "body")
    descriptor = None
    for klass in bpmn2::FormalExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::formalexpression_has_language():
    assert hasattr(bpmn2::FormalExpression, "language")
    descriptor = None
    for klass in bpmn2::FormalExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::flownode_is_not_abstract():
    assert not inspect.isabstract(bpmn2::FlowNode)


def test_bpmn2::flownode_constructor_exists():
    assert callable(bpmn2::FlowNode.__init__)


def test_bpmn2::flownode_constructor_args():
    sig = inspect.signature(bpmn2::FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::globalconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalConversation)


def test_bpmn2::globalconversation_constructor_exists():
    assert callable(bpmn2::GlobalConversation.__init__)


def test_bpmn2::globalconversation_constructor_args():
    sig = inspect.signature(bpmn2::GlobalConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::globalchoreographytask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::GlobalChoreographyTask)


def test_bpmn2::globalchoreographytask_constructor_exists():
    assert callable(bpmn2::GlobalChoreographyTask.__init__)


def test_bpmn2::globalchoreographytask_constructor_args():
    sig = inspect.signature(bpmn2::GlobalChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::exclusivegateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ExclusiveGateway)


def test_bpmn2::exclusivegateway_constructor_exists():
    assert callable(bpmn2::ExclusiveGateway.__init__)


def test_bpmn2::exclusivegateway_constructor_args():
    sig = inspect.signature(bpmn2::ExclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::eventbasedgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EventBasedGateway)


def test_bpmn2::eventbasedgateway_constructor_exists():
    assert callable(bpmn2::EventBasedGateway.__init__)


def test_bpmn2::eventbasedgateway_constructor_args():
    sig = inspect.signature(bpmn2::EventBasedGateway.__init__)
    params = list(sig.parameters.keys())
    assert "instantiate" in params, "Missing parameter 'instantiate'"
    assert "eventGatewayType" in params, "Missing parameter 'eventGatewayType'"

def test_bpmn2::eventbasedgateway_has_instantiate():
    assert hasattr(bpmn2::EventBasedGateway, "instantiate")
    descriptor = None
    for klass in bpmn2::EventBasedGateway.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::eventbasedgateway_has_eventGatewayType():
    assert hasattr(bpmn2::EventBasedGateway, "eventGatewayType")
    descriptor = None
    for klass in bpmn2::EventBasedGateway.__mro__:
        if "eventGatewayType" in klass.__dict__:
            descriptor = klass.__dict__["eventGatewayType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::event_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Event)


def test_bpmn2::event_constructor_exists():
    assert callable(bpmn2::Event.__init__)


def test_bpmn2::event_constructor_args():
    sig = inspect.signature(bpmn2::Event.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::escalationeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EscalationEventDefinition)


def test_bpmn2::escalationeventdefinition_constructor_exists():
    assert callable(bpmn2::EscalationEventDefinition.__init__)


def test_bpmn2::escalationeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::EscalationEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::extensionattributevalue_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ExtensionAttributeValue)


def test_bpmn2::extensionattributevalue_constructor_exists():
    assert callable(bpmn2::ExtensionAttributeValue.__init__)


def test_bpmn2::extensionattributevalue_constructor_args():
    sig = inspect.signature(bpmn2::ExtensionAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2::extensionattributevalue_has_value():
    assert hasattr(bpmn2::ExtensionAttributeValue, "value")
    descriptor = None
    for klass in bpmn2::ExtensionAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::extension_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Extension)


def test_bpmn2::extension_constructor_exists():
    assert callable(bpmn2::Extension.__init__)


def test_bpmn2::extension_constructor_args():
    sig = inspect.signature(bpmn2::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "mustUnderstand" in params, "Missing parameter 'mustUnderstand'"
    assert "xsdDefinition" in params, "Missing parameter 'xsdDefinition'"

def test_bpmn2::extension_has_mustUnderstand():
    assert hasattr(bpmn2::Extension, "mustUnderstand")
    descriptor = None
    for klass in bpmn2::Extension.__mro__:
        if "mustUnderstand" in klass.__dict__:
            descriptor = klass.__dict__["mustUnderstand"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::extension_has_xsdDefinition():
    assert hasattr(bpmn2::Extension, "xsdDefinition")
    descriptor = None
    for klass in bpmn2::Extension.__mro__:
        if "xsdDefinition" in klass.__dict__:
            descriptor = klass.__dict__["xsdDefinition"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::expression_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Expression)


def test_bpmn2::expression_constructor_exists():
    assert callable(bpmn2::Expression.__init__)


def test_bpmn2::expression_constructor_args():
    sig = inspect.signature(bpmn2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::error_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Error)


def test_bpmn2::error_constructor_exists():
    assert callable(bpmn2::Error.__init__)


def test_bpmn2::error_constructor_args():
    sig = inspect.signature(bpmn2::Error.__init__)
    params = list(sig.parameters.keys())
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_bpmn2::error_has_errorCode():
    assert hasattr(bpmn2::Error, "errorCode")
    descriptor = None
    for klass in bpmn2::Error.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::endpoint_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EndPoint)


def test_bpmn2::endpoint_constructor_exists():
    assert callable(bpmn2::EndPoint.__init__)


def test_bpmn2::endpoint_constructor_args():
    sig = inspect.signature(bpmn2::EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::endevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EndEvent)


def test_bpmn2::endevent_constructor_exists():
    assert callable(bpmn2::EndEvent.__init__)


def test_bpmn2::endevent_constructor_args():
    sig = inspect.signature(bpmn2::EndEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::documentation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Documentation)


def test_bpmn2::documentation_constructor_exists():
    assert callable(bpmn2::Documentation.__init__)


def test_bpmn2::documentation_constructor_args():
    sig = inspect.signature(bpmn2::Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "textFormat" in params, "Missing parameter 'textFormat'"
    assert "text" in params, "Missing parameter 'text'"

def test_bpmn2::documentation_has_mixed():
    assert hasattr(bpmn2::Documentation, "mixed")
    descriptor = None
    for klass in bpmn2::Documentation.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::documentation_has_textFormat():
    assert hasattr(bpmn2::Documentation, "textFormat")
    descriptor = None
    for klass in bpmn2::Documentation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::documentation_has_text():
    assert hasattr(bpmn2::Documentation, "text")
    descriptor = None
    for klass in bpmn2::Documentation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::definitions_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Definitions)


def test_bpmn2::definitions_constructor_exists():
    assert callable(bpmn2::Definitions.__init__)


def test_bpmn2::definitions_constructor_args():
    sig = inspect.signature(bpmn2::Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "targetNamespace" in params, "Missing parameter 'targetNamespace'"
    assert "typeLanguage" in params, "Missing parameter 'typeLanguage'"
    assert "exporter" in params, "Missing parameter 'exporter'"
    assert "expressionLanguage" in params, "Missing parameter 'expressionLanguage'"
    assert "exporterVersion" in params, "Missing parameter 'exporterVersion'"

def test_bpmn2::definitions_has_targetNamespace():
    assert hasattr(bpmn2::Definitions, "targetNamespace")
    descriptor = None
    for klass in bpmn2::Definitions.__mro__:
        if "targetNamespace" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::definitions_has_typeLanguage():
    assert hasattr(bpmn2::Definitions, "typeLanguage")
    descriptor = None
    for klass in bpmn2::Definitions.__mro__:
        if "typeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["typeLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::definitions_has_exporter():
    assert hasattr(bpmn2::Definitions, "exporter")
    descriptor = None
    for klass in bpmn2::Definitions.__mro__:
        if "exporter" in klass.__dict__:
            descriptor = klass.__dict__["exporter"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::definitions_has_expressionLanguage():
    assert hasattr(bpmn2::Definitions, "expressionLanguage")
    descriptor = None
    for klass in bpmn2::Definitions.__mro__:
        if "expressionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::definitions_has_exporterVersion():
    assert hasattr(bpmn2::Definitions, "exporterVersion")
    descriptor = None
    for klass in bpmn2::Definitions.__mro__:
        if "exporterVersion" in klass.__dict__:
            descriptor = klass.__dict__["exporterVersion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::escalation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Escalation)


def test_bpmn2::escalation_constructor_exists():
    assert callable(bpmn2::Escalation.__init__)


def test_bpmn2::escalation_constructor_args():
    sig = inspect.signature(bpmn2::Escalation.__init__)
    params = list(sig.parameters.keys())
    assert "escalationCode" in params, "Missing parameter 'escalationCode'"

def test_bpmn2::escalation_has_escalationCode():
    assert hasattr(bpmn2::Escalation, "escalationCode")
    descriptor = None
    for klass in bpmn2::Escalation.__mro__:
        if "escalationCode" in klass.__dict__:
            descriptor = klass.__dict__["escalationCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::erroreventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ErrorEventDefinition)


def test_bpmn2::erroreventdefinition_constructor_exists():
    assert callable(bpmn2::ErrorEventDefinition.__init__)


def test_bpmn2::erroreventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::ErrorEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::datastate_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataState)


def test_bpmn2::datastate_constructor_exists():
    assert callable(bpmn2::DataState.__init__)


def test_bpmn2::datastate_constructor_args():
    sig = inspect.signature(bpmn2::DataState.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::dataoutputassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataOutputAssociation)


def test_bpmn2::dataoutputassociation_constructor_exists():
    assert callable(bpmn2::DataOutputAssociation.__init__)


def test_bpmn2::dataoutputassociation_constructor_args():
    sig = inspect.signature(bpmn2::DataOutputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::dataoutput_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataOutput)


def test_bpmn2::dataoutput_constructor_exists():
    assert callable(bpmn2::DataOutput.__init__)


def test_bpmn2::dataoutput_constructor_args():
    sig = inspect.signature(bpmn2::DataOutput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2::dataoutput_has_isCollection():
    assert hasattr(bpmn2::DataOutput, "isCollection")
    descriptor = None
    for klass in bpmn2::DataOutput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::datastorereference_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataStoreReference)


def test_bpmn2::datastorereference_constructor_exists():
    assert callable(bpmn2::DataStoreReference.__init__)


def test_bpmn2::datastorereference_constructor_args():
    sig = inspect.signature(bpmn2::DataStoreReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::datastore_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataStore)


def test_bpmn2::datastore_constructor_exists():
    assert callable(bpmn2::DataStore.__init__)


def test_bpmn2::datastore_constructor_args():
    sig = inspect.signature(bpmn2::DataStore.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "isUnlimited" in params, "Missing parameter 'isUnlimited'"

def test_bpmn2::datastore_has_capacity():
    assert hasattr(bpmn2::DataStore, "capacity")
    descriptor = None
    for klass in bpmn2::DataStore.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::datastore_has_isUnlimited():
    assert hasattr(bpmn2::DataStore, "isUnlimited")
    descriptor = None
    for klass in bpmn2::DataStore.__mro__:
        if "isUnlimited" in klass.__dict__:
            descriptor = klass.__dict__["isUnlimited"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::datainputassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataInputAssociation)


def test_bpmn2::datainputassociation_constructor_exists():
    assert callable(bpmn2::DataInputAssociation.__init__)


def test_bpmn2::datainputassociation_constructor_args():
    sig = inspect.signature(bpmn2::DataInputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::datainput_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataInput)


def test_bpmn2::datainput_constructor_exists():
    assert callable(bpmn2::DataInput.__init__)


def test_bpmn2::datainput_constructor_args():
    sig = inspect.signature(bpmn2::DataInput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2::datainput_has_isCollection():
    assert hasattr(bpmn2::DataInput, "isCollection")
    descriptor = None
    for klass in bpmn2::DataInput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::dataassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataAssociation)


def test_bpmn2::dataassociation_constructor_exists():
    assert callable(bpmn2::DataAssociation.__init__)


def test_bpmn2::dataassociation_constructor_args():
    sig = inspect.signature(bpmn2::DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::correlationsubscription_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CorrelationSubscription)


def test_bpmn2::correlationsubscription_constructor_exists():
    assert callable(bpmn2::CorrelationSubscription.__init__)


def test_bpmn2::correlationsubscription_constructor_args():
    sig = inspect.signature(bpmn2::CorrelationSubscription.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataObjectReference)


def test_bpmn2::dataobjectreference_constructor_exists():
    assert callable(bpmn2::DataObjectReference.__init__)


def test_bpmn2::dataobjectreference_constructor_args():
    sig = inspect.signature(bpmn2::DataObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::dataobject_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DataObject)


def test_bpmn2::dataobject_constructor_exists():
    assert callable(bpmn2::DataObject.__init__)


def test_bpmn2::dataobject_constructor_args():
    sig = inspect.signature(bpmn2::DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2::dataobject_has_isCollection():
    assert hasattr(bpmn2::DataObject, "isCollection")
    descriptor = None
    for klass in bpmn2::DataObject.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::correlationkey_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CorrelationKey)


def test_bpmn2::correlationkey_constructor_exists():
    assert callable(bpmn2::CorrelationKey.__init__)


def test_bpmn2::correlationkey_constructor_args():
    sig = inspect.signature(bpmn2::CorrelationKey.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::conversationlink_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ConversationLink)


def test_bpmn2::conversationlink_constructor_exists():
    assert callable(bpmn2::ConversationLink.__init__)


def test_bpmn2::conversationlink_constructor_args():
    sig = inspect.signature(bpmn2::ConversationLink.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::conversationassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ConversationAssociation)


def test_bpmn2::conversationassociation_constructor_exists():
    assert callable(bpmn2::ConversationAssociation.__init__)


def test_bpmn2::conversationassociation_constructor_args():
    sig = inspect.signature(bpmn2::ConversationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::conversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Conversation)


def test_bpmn2::conversation_constructor_exists():
    assert callable(bpmn2::Conversation.__init__)


def test_bpmn2::conversation_constructor_args():
    sig = inspect.signature(bpmn2::Conversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::conditionaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ConditionalEventDefinition)


def test_bpmn2::conditionaleventdefinition_constructor_exists():
    assert callable(bpmn2::ConditionalEventDefinition.__init__)


def test_bpmn2::conditionaleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::ConditionalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::correlationpropertyretrievalexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CorrelationPropertyRetrievalExpression)


def test_bpmn2::correlationpropertyretrievalexpression_constructor_exists():
    assert callable(bpmn2::CorrelationPropertyRetrievalExpression.__init__)


def test_bpmn2::correlationpropertyretrievalexpression_constructor_args():
    sig = inspect.signature(bpmn2::CorrelationPropertyRetrievalExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::correlationpropertybinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CorrelationPropertyBinding)


def test_bpmn2::correlationpropertybinding_constructor_exists():
    assert callable(bpmn2::CorrelationPropertyBinding.__init__)


def test_bpmn2::correlationpropertybinding_constructor_args():
    sig = inspect.signature(bpmn2::CorrelationPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::correlationproperty_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CorrelationProperty)


def test_bpmn2::correlationproperty_constructor_exists():
    assert callable(bpmn2::CorrelationProperty.__init__)


def test_bpmn2::correlationproperty_constructor_args():
    sig = inspect.signature(bpmn2::CorrelationProperty.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::compensateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CompensateEventDefinition)


def test_bpmn2::compensateeventdefinition_constructor_exists():
    assert callable(bpmn2::CompensateEventDefinition.__init__)


def test_bpmn2::compensateeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::CompensateEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "waitForCompletion" in params, "Missing parameter 'waitForCompletion'"

def test_bpmn2::compensateeventdefinition_has_waitForCompletion():
    assert hasattr(bpmn2::CompensateEventDefinition, "waitForCompletion")
    descriptor = None
    for klass in bpmn2::CompensateEventDefinition.__mro__:
        if "waitForCompletion" in klass.__dict__:
            descriptor = klass.__dict__["waitForCompletion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::choreographytask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ChoreographyTask)


def test_bpmn2::choreographytask_constructor_exists():
    assert callable(bpmn2::ChoreographyTask.__init__)


def test_bpmn2::choreographytask_constructor_args():
    sig = inspect.signature(bpmn2::ChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ChoreographyActivity)


def test_bpmn2::choreographyactivity_constructor_exists():
    assert callable(bpmn2::ChoreographyActivity.__init__)


def test_bpmn2::choreographyactivity_constructor_args():
    sig = inspect.signature(bpmn2::ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_bpmn2::choreographyactivity_has_loopType():
    assert hasattr(bpmn2::ChoreographyActivity, "loopType")
    descriptor = None
    for klass in bpmn2::ChoreographyActivity.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::collaboration_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Collaboration)


def test_bpmn2::collaboration_constructor_exists():
    assert callable(bpmn2::Collaboration.__init__)


def test_bpmn2::collaboration_constructor_args():
    sig = inspect.signature(bpmn2::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_bpmn2::collaboration_has_isClosed():
    assert hasattr(bpmn2::Collaboration, "isClosed")
    descriptor = None
    for klass in bpmn2::Collaboration.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::choreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Choreography)


def test_bpmn2::choreography_constructor_exists():
    assert callable(bpmn2::Choreography.__init__)


def test_bpmn2::choreography_constructor_args():
    sig = inspect.signature(bpmn2::Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::complexgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ComplexGateway)


def test_bpmn2::complexgateway_constructor_exists():
    assert callable(bpmn2::ComplexGateway.__init__)


def test_bpmn2::complexgateway_constructor_args():
    sig = inspect.signature(bpmn2::ComplexGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::complexbehaviordefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ComplexBehaviorDefinition)


def test_bpmn2::complexbehaviordefinition_constructor_exists():
    assert callable(bpmn2::ComplexBehaviorDefinition.__init__)


def test_bpmn2::complexbehaviordefinition_constructor_args():
    sig = inspect.signature(bpmn2::ComplexBehaviorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::rootelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2::RootElement)


def test_bpmn2::rootelement_constructor_exists():
    assert callable(bpmn2::RootElement.__init__)


def test_bpmn2::rootelement_constructor_args():
    sig = inspect.signature(bpmn2::RootElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::eventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EventDefinition)


def test_bpmn2::eventdefinition_constructor_exists():
    assert callable(bpmn2::EventDefinition.__init__)


def test_bpmn2::eventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::canceleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CancelEventDefinition)


def test_bpmn2::canceleventdefinition_constructor_exists():
    assert callable(bpmn2::CancelEventDefinition.__init__)


def test_bpmn2::canceleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2::CancelEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::conversationnode_is_not_abstract():
    assert not inspect.isabstract(bpmn2::ConversationNode)


def test_bpmn2::conversationnode_constructor_exists():
    assert callable(bpmn2::ConversationNode.__init__)


def test_bpmn2::conversationnode_constructor_args():
    sig = inspect.signature(bpmn2::ConversationNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::callconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CallConversation)


def test_bpmn2::callconversation_constructor_exists():
    assert callable(bpmn2::CallConversation.__init__)


def test_bpmn2::callconversation_constructor_args():
    sig = inspect.signature(bpmn2::CallConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::categoryvalue_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CategoryValue)


def test_bpmn2::categoryvalue_constructor_exists():
    assert callable(bpmn2::CategoryValue.__init__)


def test_bpmn2::categoryvalue_constructor_args():
    sig = inspect.signature(bpmn2::CategoryValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2::categoryvalue_has_value():
    assert hasattr(bpmn2::CategoryValue, "value")
    descriptor = None
    for klass in bpmn2::CategoryValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::category_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Category)


def test_bpmn2::category_constructor_exists():
    assert callable(bpmn2::Category.__init__)


def test_bpmn2::category_constructor_args():
    sig = inspect.signature(bpmn2::Category.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::catchevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CatchEvent)


def test_bpmn2::catchevent_constructor_exists():
    assert callable(bpmn2::CatchEvent.__init__)


def test_bpmn2::catchevent_constructor_args():
    sig = inspect.signature(bpmn2::CatchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "parallelMultiple" in params, "Missing parameter 'parallelMultiple'"

def test_bpmn2::catchevent_has_parallelMultiple():
    assert hasattr(bpmn2::CatchEvent, "parallelMultiple")
    descriptor = None
    for klass in bpmn2::CatchEvent.__mro__:
        if "parallelMultiple" in klass.__dict__:
            descriptor = klass.__dict__["parallelMultiple"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::activity_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Activity)


def test_bpmn2::activity_constructor_exists():
    assert callable(bpmn2::Activity.__init__)


def test_bpmn2::activity_constructor_args():
    sig = inspect.signature(bpmn2::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "completionQuantity" in params, "Missing parameter 'completionQuantity'"
    assert "startQuantity" in params, "Missing parameter 'startQuantity'"
    assert "isForCompensation" in params, "Missing parameter 'isForCompensation'"

def test_bpmn2::activity_has_completionQuantity():
    assert hasattr(bpmn2::Activity, "completionQuantity")
    descriptor = None
    for klass in bpmn2::Activity.__mro__:
        if "completionQuantity" in klass.__dict__:
            descriptor = klass.__dict__["completionQuantity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::activity_has_startQuantity():
    assert hasattr(bpmn2::Activity, "startQuantity")
    descriptor = None
    for klass in bpmn2::Activity.__mro__:
        if "startQuantity" in klass.__dict__:
            descriptor = klass.__dict__["startQuantity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::activity_has_isForCompensation():
    assert hasattr(bpmn2::Activity, "isForCompensation")
    descriptor = None
    for klass in bpmn2::Activity.__mro__:
        if "isForCompensation" in klass.__dict__:
            descriptor = klass.__dict__["isForCompensation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::businessruletask_is_not_abstract():
    assert not inspect.isabstract(bpmn2::BusinessRuleTask)


def test_bpmn2::businessruletask_constructor_exists():
    assert callable(bpmn2::BusinessRuleTask.__init__)


def test_bpmn2::businessruletask_constructor_args():
    sig = inspect.signature(bpmn2::BusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2::businessruletask_has_implementation():
    assert hasattr(bpmn2::BusinessRuleTask, "implementation")
    descriptor = None
    for klass in bpmn2::BusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::boundaryevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2::BoundaryEvent)


def test_bpmn2::boundaryevent_constructor_exists():
    assert callable(bpmn2::BoundaryEvent.__init__)


def test_bpmn2::boundaryevent_constructor_args():
    sig = inspect.signature(bpmn2::BoundaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "cancelActivity" in params, "Missing parameter 'cancelActivity'"

def test_bpmn2::boundaryevent_has_cancelActivity():
    assert hasattr(bpmn2::BoundaryEvent, "cancelActivity")
    descriptor = None
    for klass in bpmn2::BoundaryEvent.__mro__:
        if "cancelActivity" in klass.__dict__:
            descriptor = klass.__dict__["cancelActivity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::baseelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2::BaseElement)


def test_bpmn2::baseelement_constructor_exists():
    assert callable(bpmn2::BaseElement.__init__)


def test_bpmn2::baseelement_constructor_args():
    sig = inspect.signature(bpmn2::BaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_bpmn2::baseelement_has_id():
    assert hasattr(bpmn2::BaseElement, "id")
    descriptor = None
    for klass in bpmn2::BaseElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::baseelement_has_description():
    assert hasattr(bpmn2::BaseElement, "description")
    descriptor = None
    for klass in bpmn2::BaseElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::baseelement_has_name():
    assert hasattr(bpmn2::BaseElement, "name")
    descriptor = None
    for klass in bpmn2::BaseElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::baseelement_has_anyAttribute():
    assert hasattr(bpmn2::BaseElement, "anyAttribute")
    descriptor = None
    for klass in bpmn2::BaseElement.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::auditing_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Auditing)


def test_bpmn2::auditing_constructor_exists():
    assert callable(bpmn2::Auditing.__init__)


def test_bpmn2::auditing_constructor_args():
    sig = inspect.signature(bpmn2::Auditing.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::association_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Association)


def test_bpmn2::association_constructor_exists():
    assert callable(bpmn2::Association.__init__)


def test_bpmn2::association_constructor_args():
    sig = inspect.signature(bpmn2::Association.__init__)
    params = list(sig.parameters.keys())
    assert "associationDirection" in params, "Missing parameter 'associationDirection'"

def test_bpmn2::association_has_associationDirection():
    assert hasattr(bpmn2::Association, "associationDirection")
    descriptor = None
    for klass in bpmn2::Association.__mro__:
        if "associationDirection" in klass.__dict__:
            descriptor = klass.__dict__["associationDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::callchoreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CallChoreography)


def test_bpmn2::callchoreography_constructor_exists():
    assert callable(bpmn2::CallChoreography.__init__)


def test_bpmn2::callchoreography_constructor_args():
    sig = inspect.signature(bpmn2::CallChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::assignment_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Assignment)


def test_bpmn2::assignment_constructor_exists():
    assert callable(bpmn2::Assignment.__init__)


def test_bpmn2::assignment_constructor_args():
    sig = inspect.signature(bpmn2::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::artifact_is_not_abstract():
    assert not inspect.isabstract(bpmn2::Artifact)


def test_bpmn2::artifact_constructor_exists():
    assert callable(bpmn2::Artifact.__init__)


def test_bpmn2::artifact_constructor_args():
    sig = inspect.signature(bpmn2::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::callactivity_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CallActivity)


def test_bpmn2::callactivity_constructor_exists():
    assert callable(bpmn2::CallActivity.__init__)


def test_bpmn2::callactivity_constructor_args():
    sig = inspect.signature(bpmn2::CallActivity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::flowelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2::FlowElement)


def test_bpmn2::flowelement_constructor_exists():
    assert callable(bpmn2::FlowElement.__init__)


def test_bpmn2::flowelement_constructor_args():
    sig = inspect.signature(bpmn2::FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::adhocsubprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn2::AdHocSubProcess)


def test_bpmn2::adhocsubprocess_constructor_exists():
    assert callable(bpmn2::AdHocSubProcess.__init__)


def test_bpmn2::adhocsubprocess_constructor_args():
    sig = inspect.signature(bpmn2::AdHocSubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "cancelRemainingInstances" in params, "Missing parameter 'cancelRemainingInstances'"

def test_bpmn2::adhocsubprocess_has_ordering():
    assert hasattr(bpmn2::AdHocSubProcess, "ordering")
    descriptor = None
    for klass in bpmn2::AdHocSubProcess.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2::adhocsubprocess_has_cancelRemainingInstances():
    assert hasattr(bpmn2::AdHocSubProcess, "cancelRemainingInstances")
    descriptor = None
    for klass in bpmn2::AdHocSubProcess.__mro__:
        if "cancelRemainingInstances" in klass.__dict__:
            descriptor = klass.__dict__["cancelRemainingInstances"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2::callableelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2::CallableElement)


def test_bpmn2::callableelement_constructor_exists():
    assert callable(bpmn2::CallableElement.__init__)


def test_bpmn2::callableelement_constructor_args():
    sig = inspect.signature(bpmn2::CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(bpmn2::EStringToStringMapEntry)


def test_bpmn2::estringtostringmapentry_constructor_exists():
    assert callable(bpmn2::EStringToStringMapEntry.__init__)


def test_bpmn2::estringtostringmapentry_constructor_args():
    sig = inspect.signature(bpmn2::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2::documentroot_is_not_abstract():
    assert not inspect.isabstract(bpmn2::DocumentRoot)


def test_bpmn2::documentroot_constructor_exists():
    assert callable(bpmn2::DocumentRoot.__init__)


def test_bpmn2::documentroot_constructor_args():
    sig = inspect.signature(bpmn2::DocumentRoot.__init__)
    params = list(sig.parameters.keys())

def test_choreographylooptype_exists():
    # Check that the Enumeration exists
    assert ChoreographyLoopType is not None

def test_choreographylooptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoreographyLoopType]
    expected_literals = [
        "Standard",
        "MultiInstanceSequential",
        "None_",
        "MultiInstanceParallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoreographyLoopType"

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

def test_eventbasedgatewaytype_exists():
    # Check that the Enumeration exists
    assert EventBasedGatewayType is not None

def test_eventbasedgatewaytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventBasedGatewayType]
    expected_literals = [
        "Exclusive",
        "Parallel",
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
        "None_",
        "Public",
        "Private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessType"

def test_itemkind_exists():
    # Check that the Enumeration exists
    assert ItemKind is not None

def test_itemkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ItemKind]
    expected_literals = [
        "Physical",
        "Information",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ItemKind"

def test_multiinstancebehavior_exists():
    # Check that the Enumeration exists
    assert MultiInstanceBehavior is not None

def test_multiinstancebehavior_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiInstanceBehavior]
    expected_literals = [
        "Complex",
        "All",
        "One",
        "None_",
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
        "Unspecified",
        "Mixed",
        "Converging",
        "Diverging",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GatewayDirection"

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

def test_relationshipdirection_exists():
    # Check that the Enumeration exists
    assert RelationshipDirection is not None

def test_relationshipdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipDirection]
    expected_literals = [
        "None_",
        "Backward",
        "Both",
        "Forward",
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
HumanPerformer_strategy = st.builds(
    HumanPerformer,
)
ResourceRole_strategy = st.builds(
    ResourceRole,
)
LoopCharacteristics_strategy = st.builds(
    LoopCharacteristics,
)
Performer_strategy = st.builds(
    Performer,
)
Choreography_strategy = st.builds(
    Choreography,
)
GlobalTask_strategy = st.builds(
    GlobalTask,
)
Expression_strategy = st.builds(
    Expression,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
bpmn2::ExtensionAttributeDefinition_strategy = st.builds(
    bpmn2::ExtensionAttributeDefinition,
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
bpmn2::BPMNDiagram_strategy = st.builds(
    bpmn2::BPMNDiagram,
)
DataAssociation_strategy = st.builds(
    DataAssociation,
)
bpmn2::Document_strategy = st.builds(
    bpmn2::Document,
)
ItemAwareElement_strategy = st.builds(
    ItemAwareElement,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
InteractionNode_strategy = st.builds(
    InteractionNode,
)
bpmn2::InteractionNode_strategy = st.builds(
    bpmn2::InteractionNode,
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
bpmn2::ExtensionDefinition_strategy = st.builds(
    bpmn2::ExtensionDefinition,
    name=
        safe_text
)
Artifact_strategy = st.builds(
    Artifact,
)
BaseElement_strategy = st.builds(
    BaseElement,
)
bpmn2::ItemAwareElement_strategy = st.builds(
    bpmn2::ItemAwareElement,
)
bpmn2::FlowElementsContainer_strategy = st.builds(
    bpmn2::FlowElementsContainer,
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
bpmn2::Role_strategy = st.builds(
    bpmn2::Role,
)
bpmn2::Position_strategy = st.builds(
    bpmn2::Position,
)
bpmn2::OrganisationalUnit_strategy = st.builds(
    bpmn2::OrganisationalUnit,
)
bpmn2::Criterion_strategy = st.builds(
    bpmn2::Criterion,
)
bpmn2::Competency_strategy = st.builds(
    bpmn2::Competency,
)
SubProcess_strategy = st.builds(
    SubProcess,
)
FlowNode_strategy = st.builds(
    FlowNode,
)
bpmn2::UserTask_strategy = st.builds(
    bpmn2::UserTask,
    implementation=
        safe_text
)
bpmn2::Transaction_strategy = st.builds(
    bpmn2::Transaction,
    method=
        safe_text,
    protocol=
        safe_text
)
bpmn2::TimerEventDefinition_strategy = st.builds(
    bpmn2::TimerEventDefinition,
)
bpmn2::ThrowEvent_strategy = st.builds(
    bpmn2::ThrowEvent,
)
bpmn2::TerminateEventDefinition_strategy = st.builds(
    bpmn2::TerminateEventDefinition,
)
bpmn2::Task_strategy = st.builds(
    bpmn2::Task,
)
bpmn2::TextAnnotation_strategy = st.builds(
    bpmn2::TextAnnotation,
    textFormat=
        safe_text,
    text=
        safe_text
)
bpmn2::SubChoreography_strategy = st.builds(
    bpmn2::SubChoreography,
)
bpmn2::StartEvent_strategy = st.builds(
    bpmn2::StartEvent,
    isInterrupting=
        st.booleans()
)
bpmn2::StandardLoopCharacteristics_strategy = st.builds(
    bpmn2::StandardLoopCharacteristics,
    testBefore=
        st.booleans(),
    loopMaximum=
        safe_text
)
bpmn2::SubProcess_strategy = st.builds(
    bpmn2::SubProcess,
    triggeredByEvent=
        st.booleans()
)
bpmn2::SubConversation_strategy = st.builds(
    bpmn2::SubConversation,
)
bpmn2::Signal_strategy = st.builds(
    bpmn2::Signal,
)
bpmn2::ServiceTask_strategy = st.builds(
    bpmn2::ServiceTask,
    implementation=
        safe_text
)
bpmn2::SequenceFlow_strategy = st.builds(
    bpmn2::SequenceFlow,
    isImmediate=
        st.booleans()
)
bpmn2::SignalEventDefinition_strategy = st.builds(
    bpmn2::SignalEventDefinition,
)
bpmn2::EObject_strategy = st.builds(
    bpmn2::EObject,
)
bpmn2::ResourceParameterBinding_strategy = st.builds(
    bpmn2::ResourceParameterBinding,
)
bpmn2::ResourceParameter_strategy = st.builds(
    bpmn2::ResourceParameter,
    isRequired=
        st.booleans()
)
bpmn2::SendTask_strategy = st.builds(
    bpmn2::SendTask,
    implementation=
        safe_text
)
bpmn2::ScriptTask_strategy = st.builds(
    bpmn2::ScriptTask,
    scriptFormat=
        safe_text,
    script=
        safe_text
)
bpmn2::Resource_strategy = st.builds(
    bpmn2::Resource,
)
bpmn2::Rendering_strategy = st.builds(
    bpmn2::Rendering,
)
bpmn2::Relationship_strategy = st.builds(
    bpmn2::Relationship,
    type=
        safe_text,
    direction=
        safe_text
)
bpmn2::ResourceAssignmentExpression_strategy = st.builds(
    bpmn2::ResourceAssignmentExpression,
)
bpmn2::Process_strategy = st.builds(
    bpmn2::Process,
    isClosed=
        st.booleans(),
    processType=
        safe_text,
    isExecutable=
        st.booleans()
)
bpmn2::PotentialOwner_strategy = st.builds(
    bpmn2::PotentialOwner,
)
bpmn2::PartnerRole_strategy = st.builds(
    bpmn2::PartnerRole,
)
bpmn2::PartnerEntity_strategy = st.builds(
    bpmn2::PartnerEntity,
)
bpmn2::ParticipantMultiplicity_strategy = st.builds(
    bpmn2::ParticipantMultiplicity,
    minimum=
        st.integers(),
    maximum=
        st.integers()
)
bpmn2::ReceiveTask_strategy = st.builds(
    bpmn2::ReceiveTask,
    implementation=
        safe_text,
    instantiate=
        st.booleans()
)
bpmn2::Property_strategy = st.builds(
    bpmn2::Property,
)
bpmn2::ParallelGateway_strategy = st.builds(
    bpmn2::ParallelGateway,
)
bpmn2::OutputSet_strategy = st.builds(
    bpmn2::OutputSet,
)
bpmn2::Operation_strategy = st.builds(
    bpmn2::Operation,
)
bpmn2::ParticipantAssociation_strategy = st.builds(
    bpmn2::ParticipantAssociation,
)
bpmn2::Participant_strategy = st.builds(
    bpmn2::Participant,
)
bpmn2::MessageFlowAssociation_strategy = st.builds(
    bpmn2::MessageFlowAssociation,
)
bpmn2::MessageFlow_strategy = st.builds(
    bpmn2::MessageFlow,
)
bpmn2::MessageEventDefinition_strategy = st.builds(
    bpmn2::MessageEventDefinition,
)
bpmn2::MultiInstanceLoopCharacteristics_strategy = st.builds(
    bpmn2::MultiInstanceLoopCharacteristics,
    behavior=
        safe_text,
    isSequential=
        st.booleans()
)
bpmn2::Monitoring_strategy = st.builds(
    bpmn2::Monitoring,
)
bpmn2::ManualTask_strategy = st.builds(
    bpmn2::ManualTask,
)
bpmn2::LoopCharacteristics_strategy = st.builds(
    bpmn2::LoopCharacteristics,
)
bpmn2::LinkEventDefinition_strategy = st.builds(
    bpmn2::LinkEventDefinition,
)
bpmn2::Message_strategy = st.builds(
    bpmn2::Message,
)
bpmn2::ItemDefinition_strategy = st.builds(
    bpmn2::ItemDefinition,
    itemKind=
        safe_text,
    isCollection=
        st.booleans()
)
bpmn2::InputOutputSpecification_strategy = st.builds(
    bpmn2::InputOutputSpecification,
)
bpmn2::InputOutputBinding_strategy = st.builds(
    bpmn2::InputOutputBinding,
)
bpmn2::LaneSet_strategy = st.builds(
    bpmn2::LaneSet,
)
bpmn2::Lane_strategy = st.builds(
    bpmn2::Lane,
)
bpmn2::Interface_strategy = st.builds(
    bpmn2::Interface,
)
bpmn2::InputSet_strategy = st.builds(
    bpmn2::InputSet,
)
bpmn2::InclusiveGateway_strategy = st.builds(
    bpmn2::InclusiveGateway,
)
bpmn2::IntermediateThrowEvent_strategy = st.builds(
    bpmn2::IntermediateThrowEvent,
)
bpmn2::IntermediateCatchEvent_strategy = st.builds(
    bpmn2::IntermediateCatchEvent,
)
bpmn2::ResourceRole_strategy = st.builds(
    bpmn2::ResourceRole,
)
bpmn2::Performer_strategy = st.builds(
    bpmn2::Performer,
)
bpmn2::HumanPerformer_strategy = st.builds(
    bpmn2::HumanPerformer,
)
bpmn2::Import_strategy = st.builds(
    bpmn2::Import,
    namespace=
        safe_text,
    location=
        safe_text,
    importType=
        safe_text
)
bpmn2::ImplicitThrowEvent_strategy = st.builds(
    bpmn2::ImplicitThrowEvent,
)
bpmn2::GlobalTask_strategy = st.builds(
    bpmn2::GlobalTask,
)
bpmn2::GlobalScriptTask_strategy = st.builds(
    bpmn2::GlobalScriptTask,
    script=
        safe_text,
    scriptLanguage=
        safe_text
)
bpmn2::GlobalManualTask_strategy = st.builds(
    bpmn2::GlobalManualTask,
)
bpmn2::Group_strategy = st.builds(
    bpmn2::Group,
)
bpmn2::GlobalUserTask_strategy = st.builds(
    bpmn2::GlobalUserTask,
    implementation=
        safe_text
)
bpmn2::GlobalBusinessRuleTask_strategy = st.builds(
    bpmn2::GlobalBusinessRuleTask,
    implementation=
        safe_text
)
bpmn2::Gateway_strategy = st.builds(
    bpmn2::Gateway,
    gatewayDirection=
        safe_text
)
bpmn2::FormalExpression_strategy = st.builds(
    bpmn2::FormalExpression,
    mixed=
        safe_text,
    body=
        safe_text,
    language=
        safe_text
)
bpmn2::FlowNode_strategy = st.builds(
    bpmn2::FlowNode,
)
bpmn2::GlobalConversation_strategy = st.builds(
    bpmn2::GlobalConversation,
)
bpmn2::GlobalChoreographyTask_strategy = st.builds(
    bpmn2::GlobalChoreographyTask,
)
bpmn2::ExclusiveGateway_strategy = st.builds(
    bpmn2::ExclusiveGateway,
)
bpmn2::EventBasedGateway_strategy = st.builds(
    bpmn2::EventBasedGateway,
    instantiate=
        st.booleans(),
    eventGatewayType=
        safe_text
)
bpmn2::Event_strategy = st.builds(
    bpmn2::Event,
)
bpmn2::EscalationEventDefinition_strategy = st.builds(
    bpmn2::EscalationEventDefinition,
)
bpmn2::ExtensionAttributeValue_strategy = st.builds(
    bpmn2::ExtensionAttributeValue,
    value=
        safe_text
)
bpmn2::Extension_strategy = st.builds(
    bpmn2::Extension,
    mustUnderstand=
        st.booleans(),
    xsdDefinition=
        safe_text
)
bpmn2::Expression_strategy = st.builds(
    bpmn2::Expression,
)
bpmn2::Error_strategy = st.builds(
    bpmn2::Error,
    errorCode=
        safe_text
)
bpmn2::EndPoint_strategy = st.builds(
    bpmn2::EndPoint,
)
bpmn2::EndEvent_strategy = st.builds(
    bpmn2::EndEvent,
)
bpmn2::Documentation_strategy = st.builds(
    bpmn2::Documentation,
    mixed=
        safe_text,
    textFormat=
        safe_text,
    text=
        safe_text
)
bpmn2::Definitions_strategy = st.builds(
    bpmn2::Definitions,
    targetNamespace=
        safe_text,
    typeLanguage=
        safe_text,
    exporter=
        safe_text,
    expressionLanguage=
        safe_text,
    exporterVersion=
        safe_text
)
bpmn2::Escalation_strategy = st.builds(
    bpmn2::Escalation,
    escalationCode=
        safe_text
)
bpmn2::ErrorEventDefinition_strategy = st.builds(
    bpmn2::ErrorEventDefinition,
)
bpmn2::DataState_strategy = st.builds(
    bpmn2::DataState,
)
bpmn2::DataOutputAssociation_strategy = st.builds(
    bpmn2::DataOutputAssociation,
)
bpmn2::DataOutput_strategy = st.builds(
    bpmn2::DataOutput,
    isCollection=
        st.booleans()
)
bpmn2::DataStoreReference_strategy = st.builds(
    bpmn2::DataStoreReference,
)
bpmn2::DataStore_strategy = st.builds(
    bpmn2::DataStore,
    capacity=
        st.integers(),
    isUnlimited=
        st.booleans()
)
bpmn2::DataInputAssociation_strategy = st.builds(
    bpmn2::DataInputAssociation,
)
bpmn2::DataInput_strategy = st.builds(
    bpmn2::DataInput,
    isCollection=
        st.booleans()
)
bpmn2::DataAssociation_strategy = st.builds(
    bpmn2::DataAssociation,
)
bpmn2::CorrelationSubscription_strategy = st.builds(
    bpmn2::CorrelationSubscription,
)
bpmn2::DataObjectReference_strategy = st.builds(
    bpmn2::DataObjectReference,
)
bpmn2::DataObject_strategy = st.builds(
    bpmn2::DataObject,
    isCollection=
        st.booleans()
)
bpmn2::CorrelationKey_strategy = st.builds(
    bpmn2::CorrelationKey,
)
bpmn2::ConversationLink_strategy = st.builds(
    bpmn2::ConversationLink,
)
bpmn2::ConversationAssociation_strategy = st.builds(
    bpmn2::ConversationAssociation,
)
bpmn2::Conversation_strategy = st.builds(
    bpmn2::Conversation,
)
bpmn2::ConditionalEventDefinition_strategy = st.builds(
    bpmn2::ConditionalEventDefinition,
)
bpmn2::CorrelationPropertyRetrievalExpression_strategy = st.builds(
    bpmn2::CorrelationPropertyRetrievalExpression,
)
bpmn2::CorrelationPropertyBinding_strategy = st.builds(
    bpmn2::CorrelationPropertyBinding,
)
bpmn2::CorrelationProperty_strategy = st.builds(
    bpmn2::CorrelationProperty,
)
bpmn2::CompensateEventDefinition_strategy = st.builds(
    bpmn2::CompensateEventDefinition,
    waitForCompletion=
        st.booleans()
)
bpmn2::ChoreographyTask_strategy = st.builds(
    bpmn2::ChoreographyTask,
)
bpmn2::ChoreographyActivity_strategy = st.builds(
    bpmn2::ChoreographyActivity,
    loopType=
        safe_text
)
bpmn2::Collaboration_strategy = st.builds(
    bpmn2::Collaboration,
    isClosed=
        st.booleans()
)
bpmn2::Choreography_strategy = st.builds(
    bpmn2::Choreography,
)
bpmn2::ComplexGateway_strategy = st.builds(
    bpmn2::ComplexGateway,
)
bpmn2::ComplexBehaviorDefinition_strategy = st.builds(
    bpmn2::ComplexBehaviorDefinition,
)
bpmn2::RootElement_strategy = st.builds(
    bpmn2::RootElement,
)
bpmn2::EventDefinition_strategy = st.builds(
    bpmn2::EventDefinition,
)
bpmn2::CancelEventDefinition_strategy = st.builds(
    bpmn2::CancelEventDefinition,
)
bpmn2::ConversationNode_strategy = st.builds(
    bpmn2::ConversationNode,
)
bpmn2::CallConversation_strategy = st.builds(
    bpmn2::CallConversation,
)
bpmn2::CategoryValue_strategy = st.builds(
    bpmn2::CategoryValue,
    value=
        safe_text
)
bpmn2::Category_strategy = st.builds(
    bpmn2::Category,
)
bpmn2::CatchEvent_strategy = st.builds(
    bpmn2::CatchEvent,
    parallelMultiple=
        st.booleans()
)
bpmn2::Activity_strategy = st.builds(
    bpmn2::Activity,
    completionQuantity=
        st.integers(),
    startQuantity=
        st.integers(),
    isForCompensation=
        st.booleans()
)
bpmn2::BusinessRuleTask_strategy = st.builds(
    bpmn2::BusinessRuleTask,
    implementation=
        safe_text
)
bpmn2::BoundaryEvent_strategy = st.builds(
    bpmn2::BoundaryEvent,
    cancelActivity=
        st.booleans()
)
bpmn2::BaseElement_strategy = st.builds(
    bpmn2::BaseElement,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    anyAttribute=
        safe_text
)
bpmn2::Auditing_strategy = st.builds(
    bpmn2::Auditing,
)
bpmn2::Association_strategy = st.builds(
    bpmn2::Association,
    associationDirection=
        safe_text
)
bpmn2::CallChoreography_strategy = st.builds(
    bpmn2::CallChoreography,
)
bpmn2::Assignment_strategy = st.builds(
    bpmn2::Assignment,
)
bpmn2::Artifact_strategy = st.builds(
    bpmn2::Artifact,
)
bpmn2::CallActivity_strategy = st.builds(
    bpmn2::CallActivity,
)
bpmn2::FlowElement_strategy = st.builds(
    bpmn2::FlowElement,
)
bpmn2::AdHocSubProcess_strategy = st.builds(
    bpmn2::AdHocSubProcess,
    ordering=
        safe_text,
    cancelRemainingInstances=
        st.booleans()
)
bpmn2::CallableElement_strategy = st.builds(
    bpmn2::CallableElement,
)
bpmn2::EStringToStringMapEntry_strategy = st.builds(
    bpmn2::EStringToStringMapEntry,
)
bpmn2::DocumentRoot_strategy = st.builds(
    bpmn2::DocumentRoot,
)

@given(instance=HumanPerformer_strategy)
@settings(max_examples=50)
def test_humanperformer_instantiation(instance):
    assert isinstance(instance, HumanPerformer)

@given(instance=ResourceRole_strategy)
@settings(max_examples=50)
def test_resourcerole_instantiation(instance):
    assert isinstance(instance, ResourceRole)

@given(instance=LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, LoopCharacteristics)

@given(instance=Performer_strategy)
@settings(max_examples=50)
def test_performer_instantiation(instance):
    assert isinstance(instance, Performer)

@given(instance=Choreography_strategy)
@settings(max_examples=50)
def test_choreography_instantiation(instance):
    assert isinstance(instance, Choreography)

@given(instance=GlobalTask_strategy)
@settings(max_examples=50)
def test_globaltask_instantiation(instance):
    assert isinstance(instance, GlobalTask)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::extensionattributedefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ExtensionAttributeDefinition)

@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_isReference_type(instance):
    assert isinstance(instance.isReference, bool)


@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original

@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bpmn2::ExtensionAttributeDefinition_strategy)
def test_bpmn2::extensionattributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ThrowEvent_strategy)
@settings(max_examples=50)
def test_throwevent_instantiation(instance):
    assert isinstance(instance, ThrowEvent)

@given(instance=bpmn2::BPMNDiagram_strategy)
@settings(max_examples=50)
def test_bpmn2::bpmndiagram_instantiation(instance):
    assert isinstance(instance, bpmn2::BPMNDiagram)

@given(instance=DataAssociation_strategy)
@settings(max_examples=50)
def test_dataassociation_instantiation(instance):
    assert isinstance(instance, DataAssociation)

@given(instance=bpmn2::Document_strategy)
@settings(max_examples=50)
def test_bpmn2::document_instantiation(instance):
    assert isinstance(instance, bpmn2::Document)

@given(instance=ItemAwareElement_strategy)
@settings(max_examples=50)
def test_itemawareelement_instantiation(instance):
    assert isinstance(instance, ItemAwareElement)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=InteractionNode_strategy)
@settings(max_examples=50)
def test_interactionnode_instantiation(instance):
    assert isinstance(instance, InteractionNode)

@given(instance=bpmn2::InteractionNode_strategy)
@settings(max_examples=50)
def test_bpmn2::interactionnode_instantiation(instance):
    assert isinstance(instance, bpmn2::InteractionNode)

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

@given(instance=bpmn2::ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::extensiondefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ExtensionDefinition)

@given(instance=bpmn2::ExtensionDefinition_strategy)
def test_bpmn2::extensiondefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bpmn2::ExtensionDefinition_strategy)
def test_bpmn2::extensiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=BaseElement_strategy)
@settings(max_examples=50)
def test_baseelement_instantiation(instance):
    assert isinstance(instance, BaseElement)

@given(instance=bpmn2::ItemAwareElement_strategy)
@settings(max_examples=50)
def test_bpmn2::itemawareelement_instantiation(instance):
    assert isinstance(instance, bpmn2::ItemAwareElement)

@given(instance=bpmn2::FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_bpmn2::flowelementscontainer_instantiation(instance):
    assert isinstance(instance, bpmn2::FlowElementsContainer)

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

@given(instance=bpmn2::Role_strategy)
@settings(max_examples=50)
def test_bpmn2::role_instantiation(instance):
    assert isinstance(instance, bpmn2::Role)

@given(instance=bpmn2::Position_strategy)
@settings(max_examples=50)
def test_bpmn2::position_instantiation(instance):
    assert isinstance(instance, bpmn2::Position)

@given(instance=bpmn2::OrganisationalUnit_strategy)
@settings(max_examples=50)
def test_bpmn2::organisationalunit_instantiation(instance):
    assert isinstance(instance, bpmn2::OrganisationalUnit)

@given(instance=bpmn2::Criterion_strategy)
@settings(max_examples=50)
def test_bpmn2::criterion_instantiation(instance):
    assert isinstance(instance, bpmn2::Criterion)

@given(instance=bpmn2::Competency_strategy)
@settings(max_examples=50)
def test_bpmn2::competency_instantiation(instance):
    assert isinstance(instance, bpmn2::Competency)

@given(instance=SubProcess_strategy)
@settings(max_examples=50)
def test_subprocess_instantiation(instance):
    assert isinstance(instance, SubProcess)

@given(instance=FlowNode_strategy)
@settings(max_examples=50)
def test_flownode_instantiation(instance):
    assert isinstance(instance, FlowNode)

@given(instance=bpmn2::UserTask_strategy)
@settings(max_examples=50)
def test_bpmn2::usertask_instantiation(instance):
    assert isinstance(instance, bpmn2::UserTask)

@given(instance=bpmn2::UserTask_strategy)
def test_bpmn2::usertask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::UserTask_strategy)
def test_bpmn2::usertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::Transaction_strategy)
@settings(max_examples=50)
def test_bpmn2::transaction_instantiation(instance):
    assert isinstance(instance, bpmn2::Transaction)

@given(instance=bpmn2::Transaction_strategy)
def test_bpmn2::transaction_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=bpmn2::Transaction_strategy)
def test_bpmn2::transaction_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=bpmn2::Transaction_strategy)
def test_bpmn2::transaction_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=bpmn2::Transaction_strategy)
def test_bpmn2::transaction_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=bpmn2::TimerEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::timereventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::TimerEventDefinition)

@given(instance=bpmn2::ThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::throwevent_instantiation(instance):
    assert isinstance(instance, bpmn2::ThrowEvent)

@given(instance=bpmn2::TerminateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::terminateeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::TerminateEventDefinition)

@given(instance=bpmn2::Task_strategy)
@settings(max_examples=50)
def test_bpmn2::task_instantiation(instance):
    assert isinstance(instance, bpmn2::Task)

@given(instance=bpmn2::TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn2::textannotation_instantiation(instance):
    assert isinstance(instance, bpmn2::TextAnnotation)

@given(instance=bpmn2::TextAnnotation_strategy)
def test_bpmn2::textannotation_textFormat_type(instance):
    assert isinstance(instance.textFormat, str)


@given(instance=bpmn2::TextAnnotation_strategy)
def test_bpmn2::textannotation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=bpmn2::TextAnnotation_strategy)
def test_bpmn2::textannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=bpmn2::TextAnnotation_strategy)
def test_bpmn2::textannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=bpmn2::SubChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2::subchoreography_instantiation(instance):
    assert isinstance(instance, bpmn2::SubChoreography)

@given(instance=bpmn2::StartEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::startevent_instantiation(instance):
    assert isinstance(instance, bpmn2::StartEvent)

@given(instance=bpmn2::StartEvent_strategy)
def test_bpmn2::startevent_isInterrupting_type(instance):
    assert isinstance(instance.isInterrupting, bool)


@given(instance=bpmn2::StartEvent_strategy)
def test_bpmn2::startevent_isInterrupting_setter(instance):
    original = instance.isInterrupting
    instance.isInterrupting = original
    assert instance.isInterrupting == original

@given(instance=bpmn2::StandardLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2::standardloopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2::StandardLoopCharacteristics)

@given(instance=bpmn2::StandardLoopCharacteristics_strategy)
def test_bpmn2::standardloopcharacteristics_testBefore_type(instance):
    assert isinstance(instance.testBefore, bool)


@given(instance=bpmn2::StandardLoopCharacteristics_strategy)
def test_bpmn2::standardloopcharacteristics_testBefore_setter(instance):
    original = instance.testBefore
    instance.testBefore = original
    assert instance.testBefore == original

@given(instance=bpmn2::StandardLoopCharacteristics_strategy)
def test_bpmn2::standardloopcharacteristics_loopMaximum_type(instance):
    assert isinstance(instance.loopMaximum, str)


@given(instance=bpmn2::StandardLoopCharacteristics_strategy)
def test_bpmn2::standardloopcharacteristics_loopMaximum_setter(instance):
    original = instance.loopMaximum
    instance.loopMaximum = original
    assert instance.loopMaximum == original

@given(instance=bpmn2::SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2::subprocess_instantiation(instance):
    assert isinstance(instance, bpmn2::SubProcess)

@given(instance=bpmn2::SubProcess_strategy)
def test_bpmn2::subprocess_triggeredByEvent_type(instance):
    assert isinstance(instance.triggeredByEvent, bool)


@given(instance=bpmn2::SubProcess_strategy)
def test_bpmn2::subprocess_triggeredByEvent_setter(instance):
    original = instance.triggeredByEvent
    instance.triggeredByEvent = original
    assert instance.triggeredByEvent == original

@given(instance=bpmn2::SubConversation_strategy)
@settings(max_examples=50)
def test_bpmn2::subconversation_instantiation(instance):
    assert isinstance(instance, bpmn2::SubConversation)

@given(instance=bpmn2::Signal_strategy)
@settings(max_examples=50)
def test_bpmn2::signal_instantiation(instance):
    assert isinstance(instance, bpmn2::Signal)

@given(instance=bpmn2::ServiceTask_strategy)
@settings(max_examples=50)
def test_bpmn2::servicetask_instantiation(instance):
    assert isinstance(instance, bpmn2::ServiceTask)

@given(instance=bpmn2::ServiceTask_strategy)
def test_bpmn2::servicetask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::ServiceTask_strategy)
def test_bpmn2::servicetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::SequenceFlow_strategy)
@settings(max_examples=50)
def test_bpmn2::sequenceflow_instantiation(instance):
    assert isinstance(instance, bpmn2::SequenceFlow)

@given(instance=bpmn2::SequenceFlow_strategy)
def test_bpmn2::sequenceflow_isImmediate_type(instance):
    assert isinstance(instance.isImmediate, bool)


@given(instance=bpmn2::SequenceFlow_strategy)
def test_bpmn2::sequenceflow_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original

@given(instance=bpmn2::SignalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::signaleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::SignalEventDefinition)

@given(instance=bpmn2::EObject_strategy)
@settings(max_examples=50)
def test_bpmn2::eobject_instantiation(instance):
    assert isinstance(instance, bpmn2::EObject)

@given(instance=bpmn2::ResourceParameterBinding_strategy)
@settings(max_examples=50)
def test_bpmn2::resourceparameterbinding_instantiation(instance):
    assert isinstance(instance, bpmn2::ResourceParameterBinding)

@given(instance=bpmn2::ResourceParameter_strategy)
@settings(max_examples=50)
def test_bpmn2::resourceparameter_instantiation(instance):
    assert isinstance(instance, bpmn2::ResourceParameter)

@given(instance=bpmn2::ResourceParameter_strategy)
def test_bpmn2::resourceparameter_isRequired_type(instance):
    assert isinstance(instance.isRequired, bool)


@given(instance=bpmn2::ResourceParameter_strategy)
def test_bpmn2::resourceparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=bpmn2::SendTask_strategy)
@settings(max_examples=50)
def test_bpmn2::sendtask_instantiation(instance):
    assert isinstance(instance, bpmn2::SendTask)

@given(instance=bpmn2::SendTask_strategy)
def test_bpmn2::sendtask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::SendTask_strategy)
def test_bpmn2::sendtask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::ScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2::scripttask_instantiation(instance):
    assert isinstance(instance, bpmn2::ScriptTask)

@given(instance=bpmn2::ScriptTask_strategy)
def test_bpmn2::scripttask_scriptFormat_type(instance):
    assert isinstance(instance.scriptFormat, str)


@given(instance=bpmn2::ScriptTask_strategy)
def test_bpmn2::scripttask_scriptFormat_setter(instance):
    original = instance.scriptFormat
    instance.scriptFormat = original
    assert instance.scriptFormat == original

@given(instance=bpmn2::ScriptTask_strategy)
def test_bpmn2::scripttask_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=bpmn2::ScriptTask_strategy)
def test_bpmn2::scripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=bpmn2::Resource_strategy)
@settings(max_examples=50)
def test_bpmn2::resource_instantiation(instance):
    assert isinstance(instance, bpmn2::Resource)

@given(instance=bpmn2::Rendering_strategy)
@settings(max_examples=50)
def test_bpmn2::rendering_instantiation(instance):
    assert isinstance(instance, bpmn2::Rendering)

@given(instance=bpmn2::Relationship_strategy)
@settings(max_examples=50)
def test_bpmn2::relationship_instantiation(instance):
    assert isinstance(instance, bpmn2::Relationship)

@given(instance=bpmn2::Relationship_strategy)
def test_bpmn2::relationship_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bpmn2::Relationship_strategy)
def test_bpmn2::relationship_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bpmn2::Relationship_strategy)
def test_bpmn2::relationship_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=bpmn2::Relationship_strategy)
def test_bpmn2::relationship_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=bpmn2::ResourceAssignmentExpression_strategy)
@settings(max_examples=50)
def test_bpmn2::resourceassignmentexpression_instantiation(instance):
    assert isinstance(instance, bpmn2::ResourceAssignmentExpression)

@given(instance=bpmn2::Process_strategy)
@settings(max_examples=50)
def test_bpmn2::process_instantiation(instance):
    assert isinstance(instance, bpmn2::Process)

@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_isClosed_type(instance):
    assert isinstance(instance.isClosed, bool)


@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_processType_type(instance):
    assert isinstance(instance.processType, str)


@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_processType_setter(instance):
    original = instance.processType
    instance.processType = original
    assert instance.processType == original

@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_isExecutable_type(instance):
    assert isinstance(instance.isExecutable, bool)


@given(instance=bpmn2::Process_strategy)
def test_bpmn2::process_isExecutable_setter(instance):
    original = instance.isExecutable
    instance.isExecutable = original
    assert instance.isExecutable == original

@given(instance=bpmn2::PotentialOwner_strategy)
@settings(max_examples=50)
def test_bpmn2::potentialowner_instantiation(instance):
    assert isinstance(instance, bpmn2::PotentialOwner)

@given(instance=bpmn2::PartnerRole_strategy)
@settings(max_examples=50)
def test_bpmn2::partnerrole_instantiation(instance):
    assert isinstance(instance, bpmn2::PartnerRole)

@given(instance=bpmn2::PartnerEntity_strategy)
@settings(max_examples=50)
def test_bpmn2::partnerentity_instantiation(instance):
    assert isinstance(instance, bpmn2::PartnerEntity)

@given(instance=bpmn2::ParticipantMultiplicity_strategy)
@settings(max_examples=50)
def test_bpmn2::participantmultiplicity_instantiation(instance):
    assert isinstance(instance, bpmn2::ParticipantMultiplicity)

@given(instance=bpmn2::ParticipantMultiplicity_strategy)
def test_bpmn2::participantmultiplicity_minimum_type(instance):
    assert isinstance(instance.minimum, int)


@given(instance=bpmn2::ParticipantMultiplicity_strategy)
def test_bpmn2::participantmultiplicity_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=bpmn2::ParticipantMultiplicity_strategy)
def test_bpmn2::participantmultiplicity_maximum_type(instance):
    assert isinstance(instance.maximum, int)


@given(instance=bpmn2::ParticipantMultiplicity_strategy)
def test_bpmn2::participantmultiplicity_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=bpmn2::ReceiveTask_strategy)
@settings(max_examples=50)
def test_bpmn2::receivetask_instantiation(instance):
    assert isinstance(instance, bpmn2::ReceiveTask)

@given(instance=bpmn2::ReceiveTask_strategy)
def test_bpmn2::receivetask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::ReceiveTask_strategy)
def test_bpmn2::receivetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::ReceiveTask_strategy)
def test_bpmn2::receivetask_instantiate_type(instance):
    assert isinstance(instance.instantiate, bool)


@given(instance=bpmn2::ReceiveTask_strategy)
def test_bpmn2::receivetask_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=bpmn2::Property_strategy)
@settings(max_examples=50)
def test_bpmn2::property_instantiation(instance):
    assert isinstance(instance, bpmn2::Property)

@given(instance=bpmn2::ParallelGateway_strategy)
@settings(max_examples=50)
def test_bpmn2::parallelgateway_instantiation(instance):
    assert isinstance(instance, bpmn2::ParallelGateway)

@given(instance=bpmn2::OutputSet_strategy)
@settings(max_examples=50)
def test_bpmn2::outputset_instantiation(instance):
    assert isinstance(instance, bpmn2::OutputSet)

@given(instance=bpmn2::Operation_strategy)
@settings(max_examples=50)
def test_bpmn2::operation_instantiation(instance):
    assert isinstance(instance, bpmn2::Operation)

@given(instance=bpmn2::ParticipantAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::participantassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::ParticipantAssociation)

@given(instance=bpmn2::Participant_strategy)
@settings(max_examples=50)
def test_bpmn2::participant_instantiation(instance):
    assert isinstance(instance, bpmn2::Participant)

@given(instance=bpmn2::MessageFlowAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::messageflowassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::MessageFlowAssociation)

@given(instance=bpmn2::MessageFlow_strategy)
@settings(max_examples=50)
def test_bpmn2::messageflow_instantiation(instance):
    assert isinstance(instance, bpmn2::MessageFlow)

@given(instance=bpmn2::MessageEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::messageeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::MessageEventDefinition)

@given(instance=bpmn2::MultiInstanceLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2::multiinstanceloopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2::MultiInstanceLoopCharacteristics)

@given(instance=bpmn2::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2::multiinstanceloopcharacteristics_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=bpmn2::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2::multiinstanceloopcharacteristics_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=bpmn2::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2::multiinstanceloopcharacteristics_isSequential_type(instance):
    assert isinstance(instance.isSequential, bool)


@given(instance=bpmn2::MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2::multiinstanceloopcharacteristics_isSequential_setter(instance):
    original = instance.isSequential
    instance.isSequential = original
    assert instance.isSequential == original

@given(instance=bpmn2::Monitoring_strategy)
@settings(max_examples=50)
def test_bpmn2::monitoring_instantiation(instance):
    assert isinstance(instance, bpmn2::Monitoring)

@given(instance=bpmn2::ManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2::manualtask_instantiation(instance):
    assert isinstance(instance, bpmn2::ManualTask)

@given(instance=bpmn2::LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2::loopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2::LoopCharacteristics)

@given(instance=bpmn2::LinkEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::linkeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::LinkEventDefinition)

@given(instance=bpmn2::Message_strategy)
@settings(max_examples=50)
def test_bpmn2::message_instantiation(instance):
    assert isinstance(instance, bpmn2::Message)

@given(instance=bpmn2::ItemDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::itemdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ItemDefinition)

@given(instance=bpmn2::ItemDefinition_strategy)
def test_bpmn2::itemdefinition_itemKind_type(instance):
    assert isinstance(instance.itemKind, str)


@given(instance=bpmn2::ItemDefinition_strategy)
def test_bpmn2::itemdefinition_itemKind_setter(instance):
    original = instance.itemKind
    instance.itemKind = original
    assert instance.itemKind == original

@given(instance=bpmn2::ItemDefinition_strategy)
def test_bpmn2::itemdefinition_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=bpmn2::ItemDefinition_strategy)
def test_bpmn2::itemdefinition_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2::InputOutputSpecification_strategy)
@settings(max_examples=50)
def test_bpmn2::inputoutputspecification_instantiation(instance):
    assert isinstance(instance, bpmn2::InputOutputSpecification)

@given(instance=bpmn2::InputOutputBinding_strategy)
@settings(max_examples=50)
def test_bpmn2::inputoutputbinding_instantiation(instance):
    assert isinstance(instance, bpmn2::InputOutputBinding)

@given(instance=bpmn2::LaneSet_strategy)
@settings(max_examples=50)
def test_bpmn2::laneset_instantiation(instance):
    assert isinstance(instance, bpmn2::LaneSet)

@given(instance=bpmn2::Lane_strategy)
@settings(max_examples=50)
def test_bpmn2::lane_instantiation(instance):
    assert isinstance(instance, bpmn2::Lane)

@given(instance=bpmn2::Interface_strategy)
@settings(max_examples=50)
def test_bpmn2::interface_instantiation(instance):
    assert isinstance(instance, bpmn2::Interface)

@given(instance=bpmn2::InputSet_strategy)
@settings(max_examples=50)
def test_bpmn2::inputset_instantiation(instance):
    assert isinstance(instance, bpmn2::InputSet)

@given(instance=bpmn2::InclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2::inclusivegateway_instantiation(instance):
    assert isinstance(instance, bpmn2::InclusiveGateway)

@given(instance=bpmn2::IntermediateThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::intermediatethrowevent_instantiation(instance):
    assert isinstance(instance, bpmn2::IntermediateThrowEvent)

@given(instance=bpmn2::IntermediateCatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::intermediatecatchevent_instantiation(instance):
    assert isinstance(instance, bpmn2::IntermediateCatchEvent)

@given(instance=bpmn2::ResourceRole_strategy)
@settings(max_examples=50)
def test_bpmn2::resourcerole_instantiation(instance):
    assert isinstance(instance, bpmn2::ResourceRole)

@given(instance=bpmn2::Performer_strategy)
@settings(max_examples=50)
def test_bpmn2::performer_instantiation(instance):
    assert isinstance(instance, bpmn2::Performer)

@given(instance=bpmn2::HumanPerformer_strategy)
@settings(max_examples=50)
def test_bpmn2::humanperformer_instantiation(instance):
    assert isinstance(instance, bpmn2::HumanPerformer)

@given(instance=bpmn2::Import_strategy)
@settings(max_examples=50)
def test_bpmn2::import_instantiation(instance):
    assert isinstance(instance, bpmn2::Import)

@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_importType_type(instance):
    assert isinstance(instance.importType, str)


@given(instance=bpmn2::Import_strategy)
def test_bpmn2::import_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original

@given(instance=bpmn2::ImplicitThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::implicitthrowevent_instantiation(instance):
    assert isinstance(instance, bpmn2::ImplicitThrowEvent)

@given(instance=bpmn2::GlobalTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globaltask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalTask)

@given(instance=bpmn2::GlobalScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globalscripttask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalScriptTask)

@given(instance=bpmn2::GlobalScriptTask_strategy)
def test_bpmn2::globalscripttask_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=bpmn2::GlobalScriptTask_strategy)
def test_bpmn2::globalscripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=bpmn2::GlobalScriptTask_strategy)
def test_bpmn2::globalscripttask_scriptLanguage_type(instance):
    assert isinstance(instance.scriptLanguage, str)


@given(instance=bpmn2::GlobalScriptTask_strategy)
def test_bpmn2::globalscripttask_scriptLanguage_setter(instance):
    original = instance.scriptLanguage
    instance.scriptLanguage = original
    assert instance.scriptLanguage == original

@given(instance=bpmn2::GlobalManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globalmanualtask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalManualTask)

@given(instance=bpmn2::Group_strategy)
@settings(max_examples=50)
def test_bpmn2::group_instantiation(instance):
    assert isinstance(instance, bpmn2::Group)

@given(instance=bpmn2::GlobalUserTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globalusertask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalUserTask)

@given(instance=bpmn2::GlobalUserTask_strategy)
def test_bpmn2::globalusertask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::GlobalUserTask_strategy)
def test_bpmn2::globalusertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::GlobalBusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globalbusinessruletask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalBusinessRuleTask)

@given(instance=bpmn2::GlobalBusinessRuleTask_strategy)
def test_bpmn2::globalbusinessruletask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::GlobalBusinessRuleTask_strategy)
def test_bpmn2::globalbusinessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::Gateway_strategy)
@settings(max_examples=50)
def test_bpmn2::gateway_instantiation(instance):
    assert isinstance(instance, bpmn2::Gateway)

@given(instance=bpmn2::Gateway_strategy)
def test_bpmn2::gateway_gatewayDirection_type(instance):
    assert isinstance(instance.gatewayDirection, str)


@given(instance=bpmn2::Gateway_strategy)
def test_bpmn2::gateway_gatewayDirection_setter(instance):
    original = instance.gatewayDirection
    instance.gatewayDirection = original
    assert instance.gatewayDirection == original

@given(instance=bpmn2::FormalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2::formalexpression_instantiation(instance):
    assert isinstance(instance, bpmn2::FormalExpression)

@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=bpmn2::FormalExpression_strategy)
def test_bpmn2::formalexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=bpmn2::FlowNode_strategy)
@settings(max_examples=50)
def test_bpmn2::flownode_instantiation(instance):
    assert isinstance(instance, bpmn2::FlowNode)

@given(instance=bpmn2::GlobalConversation_strategy)
@settings(max_examples=50)
def test_bpmn2::globalconversation_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalConversation)

@given(instance=bpmn2::GlobalChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2::globalchoreographytask_instantiation(instance):
    assert isinstance(instance, bpmn2::GlobalChoreographyTask)

@given(instance=bpmn2::ExclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2::exclusivegateway_instantiation(instance):
    assert isinstance(instance, bpmn2::ExclusiveGateway)

@given(instance=bpmn2::EventBasedGateway_strategy)
@settings(max_examples=50)
def test_bpmn2::eventbasedgateway_instantiation(instance):
    assert isinstance(instance, bpmn2::EventBasedGateway)

@given(instance=bpmn2::EventBasedGateway_strategy)
def test_bpmn2::eventbasedgateway_instantiate_type(instance):
    assert isinstance(instance.instantiate, bool)


@given(instance=bpmn2::EventBasedGateway_strategy)
def test_bpmn2::eventbasedgateway_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=bpmn2::EventBasedGateway_strategy)
def test_bpmn2::eventbasedgateway_eventGatewayType_type(instance):
    assert isinstance(instance.eventGatewayType, str)


@given(instance=bpmn2::EventBasedGateway_strategy)
def test_bpmn2::eventbasedgateway_eventGatewayType_setter(instance):
    original = instance.eventGatewayType
    instance.eventGatewayType = original
    assert instance.eventGatewayType == original

@given(instance=bpmn2::Event_strategy)
@settings(max_examples=50)
def test_bpmn2::event_instantiation(instance):
    assert isinstance(instance, bpmn2::Event)

@given(instance=bpmn2::EscalationEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::escalationeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::EscalationEventDefinition)

@given(instance=bpmn2::ExtensionAttributeValue_strategy)
@settings(max_examples=50)
def test_bpmn2::extensionattributevalue_instantiation(instance):
    assert isinstance(instance, bpmn2::ExtensionAttributeValue)

@given(instance=bpmn2::ExtensionAttributeValue_strategy)
def test_bpmn2::extensionattributevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=bpmn2::ExtensionAttributeValue_strategy)
def test_bpmn2::extensionattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=bpmn2::Extension_strategy)
@settings(max_examples=50)
def test_bpmn2::extension_instantiation(instance):
    assert isinstance(instance, bpmn2::Extension)

@given(instance=bpmn2::Extension_strategy)
def test_bpmn2::extension_mustUnderstand_type(instance):
    assert isinstance(instance.mustUnderstand, bool)


@given(instance=bpmn2::Extension_strategy)
def test_bpmn2::extension_mustUnderstand_setter(instance):
    original = instance.mustUnderstand
    instance.mustUnderstand = original
    assert instance.mustUnderstand == original

@given(instance=bpmn2::Extension_strategy)
def test_bpmn2::extension_xsdDefinition_type(instance):
    assert isinstance(instance.xsdDefinition, str)


@given(instance=bpmn2::Extension_strategy)
def test_bpmn2::extension_xsdDefinition_setter(instance):
    original = instance.xsdDefinition
    instance.xsdDefinition = original
    assert instance.xsdDefinition == original

@given(instance=bpmn2::Expression_strategy)
@settings(max_examples=50)
def test_bpmn2::expression_instantiation(instance):
    assert isinstance(instance, bpmn2::Expression)

@given(instance=bpmn2::Error_strategy)
@settings(max_examples=50)
def test_bpmn2::error_instantiation(instance):
    assert isinstance(instance, bpmn2::Error)

@given(instance=bpmn2::Error_strategy)
def test_bpmn2::error_errorCode_type(instance):
    assert isinstance(instance.errorCode, str)


@given(instance=bpmn2::Error_strategy)
def test_bpmn2::error_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=bpmn2::EndPoint_strategy)
@settings(max_examples=50)
def test_bpmn2::endpoint_instantiation(instance):
    assert isinstance(instance, bpmn2::EndPoint)

@given(instance=bpmn2::EndEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::endevent_instantiation(instance):
    assert isinstance(instance, bpmn2::EndEvent)

@given(instance=bpmn2::Documentation_strategy)
@settings(max_examples=50)
def test_bpmn2::documentation_instantiation(instance):
    assert isinstance(instance, bpmn2::Documentation)

@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_textFormat_type(instance):
    assert isinstance(instance.textFormat, str)


@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=bpmn2::Documentation_strategy)
def test_bpmn2::documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=bpmn2::Definitions_strategy)
@settings(max_examples=50)
def test_bpmn2::definitions_instantiation(instance):
    assert isinstance(instance, bpmn2::Definitions)

@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_targetNamespace_type(instance):
    assert isinstance(instance.targetNamespace, str)


@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_targetNamespace_setter(instance):
    original = instance.targetNamespace
    instance.targetNamespace = original
    assert instance.targetNamespace == original

@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_typeLanguage_type(instance):
    assert isinstance(instance.typeLanguage, str)


@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_typeLanguage_setter(instance):
    original = instance.typeLanguage
    instance.typeLanguage = original
    assert instance.typeLanguage == original

@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_exporter_type(instance):
    assert isinstance(instance.exporter, str)


@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_exporter_setter(instance):
    original = instance.exporter
    instance.exporter = original
    assert instance.exporter == original

@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_expressionLanguage_type(instance):
    assert isinstance(instance.expressionLanguage, str)


@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_expressionLanguage_setter(instance):
    original = instance.expressionLanguage
    instance.expressionLanguage = original
    assert instance.expressionLanguage == original

@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_exporterVersion_type(instance):
    assert isinstance(instance.exporterVersion, str)


@given(instance=bpmn2::Definitions_strategy)
def test_bpmn2::definitions_exporterVersion_setter(instance):
    original = instance.exporterVersion
    instance.exporterVersion = original
    assert instance.exporterVersion == original

@given(instance=bpmn2::Escalation_strategy)
@settings(max_examples=50)
def test_bpmn2::escalation_instantiation(instance):
    assert isinstance(instance, bpmn2::Escalation)

@given(instance=bpmn2::Escalation_strategy)
def test_bpmn2::escalation_escalationCode_type(instance):
    assert isinstance(instance.escalationCode, str)


@given(instance=bpmn2::Escalation_strategy)
def test_bpmn2::escalation_escalationCode_setter(instance):
    original = instance.escalationCode
    instance.escalationCode = original
    assert instance.escalationCode == original

@given(instance=bpmn2::ErrorEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::erroreventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ErrorEventDefinition)

@given(instance=bpmn2::DataState_strategy)
@settings(max_examples=50)
def test_bpmn2::datastate_instantiation(instance):
    assert isinstance(instance, bpmn2::DataState)

@given(instance=bpmn2::DataOutputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::dataoutputassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::DataOutputAssociation)

@given(instance=bpmn2::DataOutput_strategy)
@settings(max_examples=50)
def test_bpmn2::dataoutput_instantiation(instance):
    assert isinstance(instance, bpmn2::DataOutput)

@given(instance=bpmn2::DataOutput_strategy)
def test_bpmn2::dataoutput_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=bpmn2::DataOutput_strategy)
def test_bpmn2::dataoutput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2::DataStoreReference_strategy)
@settings(max_examples=50)
def test_bpmn2::datastorereference_instantiation(instance):
    assert isinstance(instance, bpmn2::DataStoreReference)

@given(instance=bpmn2::DataStore_strategy)
@settings(max_examples=50)
def test_bpmn2::datastore_instantiation(instance):
    assert isinstance(instance, bpmn2::DataStore)

@given(instance=bpmn2::DataStore_strategy)
def test_bpmn2::datastore_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=bpmn2::DataStore_strategy)
def test_bpmn2::datastore_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=bpmn2::DataStore_strategy)
def test_bpmn2::datastore_isUnlimited_type(instance):
    assert isinstance(instance.isUnlimited, bool)


@given(instance=bpmn2::DataStore_strategy)
def test_bpmn2::datastore_isUnlimited_setter(instance):
    original = instance.isUnlimited
    instance.isUnlimited = original
    assert instance.isUnlimited == original

@given(instance=bpmn2::DataInputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::datainputassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::DataInputAssociation)

@given(instance=bpmn2::DataInput_strategy)
@settings(max_examples=50)
def test_bpmn2::datainput_instantiation(instance):
    assert isinstance(instance, bpmn2::DataInput)

@given(instance=bpmn2::DataInput_strategy)
def test_bpmn2::datainput_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=bpmn2::DataInput_strategy)
def test_bpmn2::datainput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2::DataAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::dataassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::DataAssociation)

@given(instance=bpmn2::CorrelationSubscription_strategy)
@settings(max_examples=50)
def test_bpmn2::correlationsubscription_instantiation(instance):
    assert isinstance(instance, bpmn2::CorrelationSubscription)

@given(instance=bpmn2::DataObjectReference_strategy)
@settings(max_examples=50)
def test_bpmn2::dataobjectreference_instantiation(instance):
    assert isinstance(instance, bpmn2::DataObjectReference)

@given(instance=bpmn2::DataObject_strategy)
@settings(max_examples=50)
def test_bpmn2::dataobject_instantiation(instance):
    assert isinstance(instance, bpmn2::DataObject)

@given(instance=bpmn2::DataObject_strategy)
def test_bpmn2::dataobject_isCollection_type(instance):
    assert isinstance(instance.isCollection, bool)


@given(instance=bpmn2::DataObject_strategy)
def test_bpmn2::dataobject_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2::CorrelationKey_strategy)
@settings(max_examples=50)
def test_bpmn2::correlationkey_instantiation(instance):
    assert isinstance(instance, bpmn2::CorrelationKey)

@given(instance=bpmn2::ConversationLink_strategy)
@settings(max_examples=50)
def test_bpmn2::conversationlink_instantiation(instance):
    assert isinstance(instance, bpmn2::ConversationLink)

@given(instance=bpmn2::ConversationAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2::conversationassociation_instantiation(instance):
    assert isinstance(instance, bpmn2::ConversationAssociation)

@given(instance=bpmn2::Conversation_strategy)
@settings(max_examples=50)
def test_bpmn2::conversation_instantiation(instance):
    assert isinstance(instance, bpmn2::Conversation)

@given(instance=bpmn2::ConditionalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::conditionaleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ConditionalEventDefinition)

@given(instance=bpmn2::CorrelationPropertyRetrievalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2::correlationpropertyretrievalexpression_instantiation(instance):
    assert isinstance(instance, bpmn2::CorrelationPropertyRetrievalExpression)

@given(instance=bpmn2::CorrelationPropertyBinding_strategy)
@settings(max_examples=50)
def test_bpmn2::correlationpropertybinding_instantiation(instance):
    assert isinstance(instance, bpmn2::CorrelationPropertyBinding)

@given(instance=bpmn2::CorrelationProperty_strategy)
@settings(max_examples=50)
def test_bpmn2::correlationproperty_instantiation(instance):
    assert isinstance(instance, bpmn2::CorrelationProperty)

@given(instance=bpmn2::CompensateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::compensateeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::CompensateEventDefinition)

@given(instance=bpmn2::CompensateEventDefinition_strategy)
def test_bpmn2::compensateeventdefinition_waitForCompletion_type(instance):
    assert isinstance(instance.waitForCompletion, bool)


@given(instance=bpmn2::CompensateEventDefinition_strategy)
def test_bpmn2::compensateeventdefinition_waitForCompletion_setter(instance):
    original = instance.waitForCompletion
    instance.waitForCompletion = original
    assert instance.waitForCompletion == original

@given(instance=bpmn2::ChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2::choreographytask_instantiation(instance):
    assert isinstance(instance, bpmn2::ChoreographyTask)

@given(instance=bpmn2::ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_bpmn2::choreographyactivity_instantiation(instance):
    assert isinstance(instance, bpmn2::ChoreographyActivity)

@given(instance=bpmn2::ChoreographyActivity_strategy)
def test_bpmn2::choreographyactivity_loopType_type(instance):
    assert isinstance(instance.loopType, str)


@given(instance=bpmn2::ChoreographyActivity_strategy)
def test_bpmn2::choreographyactivity_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=bpmn2::Collaboration_strategy)
@settings(max_examples=50)
def test_bpmn2::collaboration_instantiation(instance):
    assert isinstance(instance, bpmn2::Collaboration)

@given(instance=bpmn2::Collaboration_strategy)
def test_bpmn2::collaboration_isClosed_type(instance):
    assert isinstance(instance.isClosed, bool)


@given(instance=bpmn2::Collaboration_strategy)
def test_bpmn2::collaboration_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=bpmn2::Choreography_strategy)
@settings(max_examples=50)
def test_bpmn2::choreography_instantiation(instance):
    assert isinstance(instance, bpmn2::Choreography)

@given(instance=bpmn2::ComplexGateway_strategy)
@settings(max_examples=50)
def test_bpmn2::complexgateway_instantiation(instance):
    assert isinstance(instance, bpmn2::ComplexGateway)

@given(instance=bpmn2::ComplexBehaviorDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::complexbehaviordefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::ComplexBehaviorDefinition)

@given(instance=bpmn2::RootElement_strategy)
@settings(max_examples=50)
def test_bpmn2::rootelement_instantiation(instance):
    assert isinstance(instance, bpmn2::RootElement)

@given(instance=bpmn2::EventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::eventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::EventDefinition)

@given(instance=bpmn2::CancelEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2::canceleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2::CancelEventDefinition)

@given(instance=bpmn2::ConversationNode_strategy)
@settings(max_examples=50)
def test_bpmn2::conversationnode_instantiation(instance):
    assert isinstance(instance, bpmn2::ConversationNode)

@given(instance=bpmn2::CallConversation_strategy)
@settings(max_examples=50)
def test_bpmn2::callconversation_instantiation(instance):
    assert isinstance(instance, bpmn2::CallConversation)

@given(instance=bpmn2::CategoryValue_strategy)
@settings(max_examples=50)
def test_bpmn2::categoryvalue_instantiation(instance):
    assert isinstance(instance, bpmn2::CategoryValue)

@given(instance=bpmn2::CategoryValue_strategy)
def test_bpmn2::categoryvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=bpmn2::CategoryValue_strategy)
def test_bpmn2::categoryvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=bpmn2::Category_strategy)
@settings(max_examples=50)
def test_bpmn2::category_instantiation(instance):
    assert isinstance(instance, bpmn2::Category)

@given(instance=bpmn2::CatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::catchevent_instantiation(instance):
    assert isinstance(instance, bpmn2::CatchEvent)

@given(instance=bpmn2::CatchEvent_strategy)
def test_bpmn2::catchevent_parallelMultiple_type(instance):
    assert isinstance(instance.parallelMultiple, bool)


@given(instance=bpmn2::CatchEvent_strategy)
def test_bpmn2::catchevent_parallelMultiple_setter(instance):
    original = instance.parallelMultiple
    instance.parallelMultiple = original
    assert instance.parallelMultiple == original

@given(instance=bpmn2::Activity_strategy)
@settings(max_examples=50)
def test_bpmn2::activity_instantiation(instance):
    assert isinstance(instance, bpmn2::Activity)

@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_completionQuantity_type(instance):
    assert isinstance(instance.completionQuantity, int)


@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_completionQuantity_setter(instance):
    original = instance.completionQuantity
    instance.completionQuantity = original
    assert instance.completionQuantity == original

@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_startQuantity_type(instance):
    assert isinstance(instance.startQuantity, int)


@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_startQuantity_setter(instance):
    original = instance.startQuantity
    instance.startQuantity = original
    assert instance.startQuantity == original

@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_isForCompensation_type(instance):
    assert isinstance(instance.isForCompensation, bool)


@given(instance=bpmn2::Activity_strategy)
def test_bpmn2::activity_isForCompensation_setter(instance):
    original = instance.isForCompensation
    instance.isForCompensation = original
    assert instance.isForCompensation == original

@given(instance=bpmn2::BusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2::businessruletask_instantiation(instance):
    assert isinstance(instance, bpmn2::BusinessRuleTask)

@given(instance=bpmn2::BusinessRuleTask_strategy)
def test_bpmn2::businessruletask_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=bpmn2::BusinessRuleTask_strategy)
def test_bpmn2::businessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2::BoundaryEvent_strategy)
@settings(max_examples=50)
def test_bpmn2::boundaryevent_instantiation(instance):
    assert isinstance(instance, bpmn2::BoundaryEvent)

@given(instance=bpmn2::BoundaryEvent_strategy)
def test_bpmn2::boundaryevent_cancelActivity_type(instance):
    assert isinstance(instance.cancelActivity, bool)


@given(instance=bpmn2::BoundaryEvent_strategy)
def test_bpmn2::boundaryevent_cancelActivity_setter(instance):
    original = instance.cancelActivity
    instance.cancelActivity = original
    assert instance.cancelActivity == original

@given(instance=bpmn2::BaseElement_strategy)
@settings(max_examples=50)
def test_bpmn2::baseelement_instantiation(instance):
    assert isinstance(instance, bpmn2::BaseElement)

@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=bpmn2::BaseElement_strategy)
def test_bpmn2::baseelement_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=bpmn2::Auditing_strategy)
@settings(max_examples=50)
def test_bpmn2::auditing_instantiation(instance):
    assert isinstance(instance, bpmn2::Auditing)

@given(instance=bpmn2::Association_strategy)
@settings(max_examples=50)
def test_bpmn2::association_instantiation(instance):
    assert isinstance(instance, bpmn2::Association)

@given(instance=bpmn2::Association_strategy)
def test_bpmn2::association_associationDirection_type(instance):
    assert isinstance(instance.associationDirection, str)


@given(instance=bpmn2::Association_strategy)
def test_bpmn2::association_associationDirection_setter(instance):
    original = instance.associationDirection
    instance.associationDirection = original
    assert instance.associationDirection == original

@given(instance=bpmn2::CallChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2::callchoreography_instantiation(instance):
    assert isinstance(instance, bpmn2::CallChoreography)

@given(instance=bpmn2::Assignment_strategy)
@settings(max_examples=50)
def test_bpmn2::assignment_instantiation(instance):
    assert isinstance(instance, bpmn2::Assignment)

@given(instance=bpmn2::Artifact_strategy)
@settings(max_examples=50)
def test_bpmn2::artifact_instantiation(instance):
    assert isinstance(instance, bpmn2::Artifact)

@given(instance=bpmn2::CallActivity_strategy)
@settings(max_examples=50)
def test_bpmn2::callactivity_instantiation(instance):
    assert isinstance(instance, bpmn2::CallActivity)

@given(instance=bpmn2::FlowElement_strategy)
@settings(max_examples=50)
def test_bpmn2::flowelement_instantiation(instance):
    assert isinstance(instance, bpmn2::FlowElement)

@given(instance=bpmn2::AdHocSubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2::adhocsubprocess_instantiation(instance):
    assert isinstance(instance, bpmn2::AdHocSubProcess)

@given(instance=bpmn2::AdHocSubProcess_strategy)
def test_bpmn2::adhocsubprocess_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=bpmn2::AdHocSubProcess_strategy)
def test_bpmn2::adhocsubprocess_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=bpmn2::AdHocSubProcess_strategy)
def test_bpmn2::adhocsubprocess_cancelRemainingInstances_type(instance):
    assert isinstance(instance.cancelRemainingInstances, bool)


@given(instance=bpmn2::AdHocSubProcess_strategy)
def test_bpmn2::adhocsubprocess_cancelRemainingInstances_setter(instance):
    original = instance.cancelRemainingInstances
    instance.cancelRemainingInstances = original
    assert instance.cancelRemainingInstances == original

@given(instance=bpmn2::CallableElement_strategy)
@settings(max_examples=50)
def test_bpmn2::callableelement_instantiation(instance):
    assert isinstance(instance, bpmn2::CallableElement)

@given(instance=bpmn2::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_bpmn2::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, bpmn2::EStringToStringMapEntry)

@given(instance=bpmn2::DocumentRoot_strategy)
@settings(max_examples=50)
def test_bpmn2::documentroot_instantiation(instance):
    assert isinstance(instance, bpmn2::DocumentRoot)
