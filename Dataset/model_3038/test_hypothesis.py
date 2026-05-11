import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    conversation::Junction,
    SubscribableByOthers,
    PublishableByMe,
    PublicEvent,
    PublishableByOthers,
    SubscribableByMe,
    conversation::PubliclyPublishable,
    Event,
    conversation::SubscribableByMe,
    conversation::PublicEvent,
    conversation::ProjectionField,
    conversation::Import,
    Import,
    PubliclySubscribable,
    PubliclyPublishable,
    conversation::PublicPubSub,
    conversation::PublishableByOthers,
    conversation::PrivatePubSub,
    conversation::SubscribableByOthers,
    State,
    conversation::Join,
    conversation::Decision,
    conversation::Event,
    conversation::PublishableByMe,
    conversation::PubliclySubscribable,
    conversation::StateMachine,
    conversation::View,
    conversation::AgentImport,
    conversation::TypeImport,
    conversation::Service,
    conversation::RestService,
    conversation::Projection,
    conversation::Agent,
    conversation::Transition,
    conversation::State,
    conversation::Conversation,
    StateMachineType,
    ConnectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conversation::junction_is_not_abstract():
    assert not inspect.isabstract(conversation::Junction)


def test_conversation::junction_constructor_exists():
    assert callable(conversation::Junction.__init__)


def test_conversation::junction_constructor_args():
    sig = inspect.signature(conversation::Junction.__init__)
    params = list(sig.parameters.keys())



def test_subscribablebyothers_is_not_abstract():
    assert not inspect.isabstract(SubscribableByOthers)


def test_subscribablebyothers_constructor_exists():
    assert callable(SubscribableByOthers.__init__)


def test_subscribablebyothers_constructor_args():
    sig = inspect.signature(SubscribableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_publishablebyme_is_not_abstract():
    assert not inspect.isabstract(PublishableByMe)


def test_publishablebyme_constructor_exists():
    assert callable(PublishableByMe.__init__)


def test_publishablebyme_constructor_args():
    sig = inspect.signature(PublishableByMe.__init__)
    params = list(sig.parameters.keys())



def test_publicevent_is_not_abstract():
    assert not inspect.isabstract(PublicEvent)


def test_publicevent_constructor_exists():
    assert callable(PublicEvent.__init__)


def test_publicevent_constructor_args():
    sig = inspect.signature(PublicEvent.__init__)
    params = list(sig.parameters.keys())



def test_publishablebyothers_is_not_abstract():
    assert not inspect.isabstract(PublishableByOthers)


def test_publishablebyothers_constructor_exists():
    assert callable(PublishableByOthers.__init__)


def test_publishablebyothers_constructor_args():
    sig = inspect.signature(PublishableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_subscribablebyme_is_not_abstract():
    assert not inspect.isabstract(SubscribableByMe)


def test_subscribablebyme_constructor_exists():
    assert callable(SubscribableByMe.__init__)


def test_subscribablebyme_constructor_args():
    sig = inspect.signature(SubscribableByMe.__init__)
    params = list(sig.parameters.keys())



def test_conversation::publiclypublishable_is_not_abstract():
    assert not inspect.isabstract(conversation::PubliclyPublishable)


def test_conversation::publiclypublishable_constructor_exists():
    assert callable(conversation::PubliclyPublishable.__init__)


def test_conversation::publiclypublishable_constructor_args():
    sig = inspect.signature(conversation::PubliclyPublishable.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_conversation::subscribablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation::SubscribableByMe)


def test_conversation::subscribablebyme_constructor_exists():
    assert callable(conversation::SubscribableByMe.__init__)


def test_conversation::subscribablebyme_constructor_args():
    sig = inspect.signature(conversation::SubscribableByMe.__init__)
    params = list(sig.parameters.keys())



def test_conversation::publicevent_is_not_abstract():
    assert not inspect.isabstract(conversation::PublicEvent)


def test_conversation::publicevent_constructor_exists():
    assert callable(conversation::PublicEvent.__init__)


def test_conversation::publicevent_constructor_args():
    sig = inspect.signature(conversation::PublicEvent.__init__)
    params = list(sig.parameters.keys())



def test_conversation::projectionfield_is_not_abstract():
    assert not inspect.isabstract(conversation::ProjectionField)


def test_conversation::projectionfield_constructor_exists():
    assert callable(conversation::ProjectionField.__init__)


def test_conversation::projectionfield_constructor_args():
    sig = inspect.signature(conversation::ProjectionField.__init__)
    params = list(sig.parameters.keys())



def test_conversation::import_is_not_abstract():
    assert not inspect.isabstract(conversation::Import)


def test_conversation::import_constructor_exists():
    assert callable(conversation::Import.__init__)


def test_conversation::import_constructor_args():
    sig = inspect.signature(conversation::Import.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_conversation::import_has_alias():
    assert hasattr(conversation::Import, "alias")
    descriptor = None
    for klass in conversation::Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_publiclysubscribable_is_not_abstract():
    assert not inspect.isabstract(PubliclySubscribable)


def test_publiclysubscribable_constructor_exists():
    assert callable(PubliclySubscribable.__init__)


def test_publiclysubscribable_constructor_args():
    sig = inspect.signature(PubliclySubscribable.__init__)
    params = list(sig.parameters.keys())



def test_publiclypublishable_is_not_abstract():
    assert not inspect.isabstract(PubliclyPublishable)


def test_publiclypublishable_constructor_exists():
    assert callable(PubliclyPublishable.__init__)


def test_publiclypublishable_constructor_args():
    sig = inspect.signature(PubliclyPublishable.__init__)
    params = list(sig.parameters.keys())



def test_conversation::publicpubsub_is_not_abstract():
    assert not inspect.isabstract(conversation::PublicPubSub)


def test_conversation::publicpubsub_constructor_exists():
    assert callable(conversation::PublicPubSub.__init__)


def test_conversation::publicpubsub_constructor_args():
    sig = inspect.signature(conversation::PublicPubSub.__init__)
    params = list(sig.parameters.keys())



def test_conversation::publishablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation::PublishableByOthers)


def test_conversation::publishablebyothers_constructor_exists():
    assert callable(conversation::PublishableByOthers.__init__)


def test_conversation::publishablebyothers_constructor_args():
    sig = inspect.signature(conversation::PublishableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_conversation::privatepubsub_is_not_abstract():
    assert not inspect.isabstract(conversation::PrivatePubSub)


def test_conversation::privatepubsub_constructor_exists():
    assert callable(conversation::PrivatePubSub.__init__)


def test_conversation::privatepubsub_constructor_args():
    sig = inspect.signature(conversation::PrivatePubSub.__init__)
    params = list(sig.parameters.keys())



def test_conversation::subscribablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation::SubscribableByOthers)


def test_conversation::subscribablebyothers_constructor_exists():
    assert callable(conversation::SubscribableByOthers.__init__)


def test_conversation::subscribablebyothers_constructor_args():
    sig = inspect.signature(conversation::SubscribableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_conversation::join_is_not_abstract():
    assert not inspect.isabstract(conversation::Join)


def test_conversation::join_constructor_exists():
    assert callable(conversation::Join.__init__)


def test_conversation::join_constructor_args():
    sig = inspect.signature(conversation::Join.__init__)
    params = list(sig.parameters.keys())



def test_conversation::decision_is_not_abstract():
    assert not inspect.isabstract(conversation::Decision)


def test_conversation::decision_constructor_exists():
    assert callable(conversation::Decision.__init__)


def test_conversation::decision_constructor_args():
    sig = inspect.signature(conversation::Decision.__init__)
    params = list(sig.parameters.keys())



def test_conversation::event_is_not_abstract():
    assert not inspect.isabstract(conversation::Event)


def test_conversation::event_constructor_exists():
    assert callable(conversation::Event.__init__)


def test_conversation::event_constructor_args():
    sig = inspect.signature(conversation::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conversation::event_has_name():
    assert hasattr(conversation::Event, "name")
    descriptor = None
    for klass in conversation::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conversation::publishablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation::PublishableByMe)


def test_conversation::publishablebyme_constructor_exists():
    assert callable(conversation::PublishableByMe.__init__)


def test_conversation::publishablebyme_constructor_args():
    sig = inspect.signature(conversation::PublishableByMe.__init__)
    params = list(sig.parameters.keys())



def test_conversation::publiclysubscribable_is_not_abstract():
    assert not inspect.isabstract(conversation::PubliclySubscribable)


def test_conversation::publiclysubscribable_constructor_exists():
    assert callable(conversation::PubliclySubscribable.__init__)


def test_conversation::publiclysubscribable_constructor_args():
    sig = inspect.signature(conversation::PubliclySubscribable.__init__)
    params = list(sig.parameters.keys())



def test_conversation::statemachine_is_not_abstract():
    assert not inspect.isabstract(conversation::StateMachine)


def test_conversation::statemachine_constructor_exists():
    assert callable(conversation::StateMachine.__init__)


def test_conversation::statemachine_constructor_args():
    sig = inspect.signature(conversation::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_conversation::view_is_not_abstract():
    assert not inspect.isabstract(conversation::View)


def test_conversation::view_constructor_exists():
    assert callable(conversation::View.__init__)


def test_conversation::view_constructor_args():
    sig = inspect.signature(conversation::View.__init__)
    params = list(sig.parameters.keys())



def test_conversation::agentimport_is_not_abstract():
    assert not inspect.isabstract(conversation::AgentImport)


def test_conversation::agentimport_constructor_exists():
    assert callable(conversation::AgentImport.__init__)


def test_conversation::agentimport_constructor_args():
    sig = inspect.signature(conversation::AgentImport.__init__)
    params = list(sig.parameters.keys())



def test_conversation::typeimport_is_not_abstract():
    assert not inspect.isabstract(conversation::TypeImport)


def test_conversation::typeimport_constructor_exists():
    assert callable(conversation::TypeImport.__init__)


def test_conversation::typeimport_constructor_args():
    sig = inspect.signature(conversation::TypeImport.__init__)
    params = list(sig.parameters.keys())



def test_conversation::service_is_not_abstract():
    assert not inspect.isabstract(conversation::Service)


def test_conversation::service_constructor_exists():
    assert callable(conversation::Service.__init__)


def test_conversation::service_constructor_args():
    sig = inspect.signature(conversation::Service.__init__)
    params = list(sig.parameters.keys())



def test_conversation::restservice_is_not_abstract():
    assert not inspect.isabstract(conversation::RestService)


def test_conversation::restservice_constructor_exists():
    assert callable(conversation::RestService.__init__)


def test_conversation::restservice_constructor_args():
    sig = inspect.signature(conversation::RestService.__init__)
    params = list(sig.parameters.keys())



def test_conversation::projection_is_not_abstract():
    assert not inspect.isabstract(conversation::Projection)


def test_conversation::projection_constructor_exists():
    assert callable(conversation::Projection.__init__)


def test_conversation::projection_constructor_args():
    sig = inspect.signature(conversation::Projection.__init__)
    params = list(sig.parameters.keys())



def test_conversation::agent_is_not_abstract():
    assert not inspect.isabstract(conversation::Agent)


def test_conversation::agent_constructor_exists():
    assert callable(conversation::Agent.__init__)


def test_conversation::agent_constructor_args():
    sig = inspect.signature(conversation::Agent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "connectionType" in params, "Missing parameter 'connectionType'"
    assert "stateMachineType" in params, "Missing parameter 'stateMachineType'"
    assert "accessRequirement" in params, "Missing parameter 'accessRequirement'"

def test_conversation::agent_has_name():
    assert hasattr(conversation::Agent, "name")
    descriptor = None
    for klass in conversation::Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_conversation::agent_has_connectionType():
    assert hasattr(conversation::Agent, "connectionType")
    descriptor = None
    for klass in conversation::Agent.__mro__:
        if "connectionType" in klass.__dict__:
            descriptor = klass.__dict__["connectionType"]
            break
    assert isinstance(descriptor, property)

def test_conversation::agent_has_stateMachineType():
    assert hasattr(conversation::Agent, "stateMachineType")
    descriptor = None
    for klass in conversation::Agent.__mro__:
        if "stateMachineType" in klass.__dict__:
            descriptor = klass.__dict__["stateMachineType"]
            break
    assert isinstance(descriptor, property)

def test_conversation::agent_has_accessRequirement():
    assert hasattr(conversation::Agent, "accessRequirement")
    descriptor = None
    for klass in conversation::Agent.__mro__:
        if "accessRequirement" in klass.__dict__:
            descriptor = klass.__dict__["accessRequirement"]
            break
    assert isinstance(descriptor, property)



def test_conversation::transition_is_not_abstract():
    assert not inspect.isabstract(conversation::Transition)


def test_conversation::transition_constructor_exists():
    assert callable(conversation::Transition.__init__)


def test_conversation::transition_constructor_args():
    sig = inspect.signature(conversation::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"

def test_conversation::transition_has_requiresExecution():
    assert hasattr(conversation::Transition, "requiresExecution")
    descriptor = None
    for klass in conversation::Transition.__mro__:
        if "requiresExecution" in klass.__dict__:
            descriptor = klass.__dict__["requiresExecution"]
            break
    assert isinstance(descriptor, property)



def test_conversation::state_is_not_abstract():
    assert not inspect.isabstract(conversation::State)


def test_conversation::state_constructor_exists():
    assert callable(conversation::State.__init__)


def test_conversation::state_constructor_args():
    sig = inspect.signature(conversation::State.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"
    assert "name" in params, "Missing parameter 'name'"

def test_conversation::state_has_join():
    assert hasattr(conversation::State, "join")
    descriptor = None
    for klass in conversation::State.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_conversation::state_has_requiresExecution():
    assert hasattr(conversation::State, "requiresExecution")
    descriptor = None
    for klass in conversation::State.__mro__:
        if "requiresExecution" in klass.__dict__:
            descriptor = klass.__dict__["requiresExecution"]
            break
    assert isinstance(descriptor, property)

def test_conversation::state_has_name():
    assert hasattr(conversation::State, "name")
    descriptor = None
    for klass in conversation::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conversation::conversation_is_not_abstract():
    assert not inspect.isabstract(conversation::Conversation)


def test_conversation::conversation_constructor_exists():
    assert callable(conversation::Conversation.__init__)


def test_conversation::conversation_constructor_args():
    sig = inspect.signature(conversation::Conversation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conversation::conversation_has_name():
    assert hasattr(conversation::Conversation, "name")
    descriptor = None
    for klass in conversation::Conversation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachinetype_exists():
    # Check that the Enumeration exists
    assert StateMachineType is not None

def test_statemachinetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateMachineType]
    expected_literals = [
        "finite",
        "infinite",
        "stateless",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateMachineType"

def test_connectiontype_exists():
    # Check that the Enumeration exists
    assert ConnectionType is not None

def test_connectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionType]
    expected_literals = [
        "dependent",
        "independent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionType"


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
conversation::Junction_strategy = st.builds(
    conversation::Junction,
)
SubscribableByOthers_strategy = st.builds(
    SubscribableByOthers,
)
PublishableByMe_strategy = st.builds(
    PublishableByMe,
)
PublicEvent_strategy = st.builds(
    PublicEvent,
)
PublishableByOthers_strategy = st.builds(
    PublishableByOthers,
)
SubscribableByMe_strategy = st.builds(
    SubscribableByMe,
)
conversation::PubliclyPublishable_strategy = st.builds(
    conversation::PubliclyPublishable,
)
Event_strategy = st.builds(
    Event,
)
conversation::SubscribableByMe_strategy = st.builds(
    conversation::SubscribableByMe,
)
conversation::PublicEvent_strategy = st.builds(
    conversation::PublicEvent,
)
conversation::ProjectionField_strategy = st.builds(
    conversation::ProjectionField,
)
conversation::Import_strategy = st.builds(
    conversation::Import,
    alias=
        safe_text
)
Import_strategy = st.builds(
    Import,
)
PubliclySubscribable_strategy = st.builds(
    PubliclySubscribable,
)
PubliclyPublishable_strategy = st.builds(
    PubliclyPublishable,
)
conversation::PublicPubSub_strategy = st.builds(
    conversation::PublicPubSub,
)
conversation::PublishableByOthers_strategy = st.builds(
    conversation::PublishableByOthers,
)
conversation::PrivatePubSub_strategy = st.builds(
    conversation::PrivatePubSub,
)
conversation::SubscribableByOthers_strategy = st.builds(
    conversation::SubscribableByOthers,
)
State_strategy = st.builds(
    State,
)
conversation::Join_strategy = st.builds(
    conversation::Join,
)
conversation::Decision_strategy = st.builds(
    conversation::Decision,
)
conversation::Event_strategy = st.builds(
    conversation::Event,
    name=
        safe_text
)
conversation::PublishableByMe_strategy = st.builds(
    conversation::PublishableByMe,
)
conversation::PubliclySubscribable_strategy = st.builds(
    conversation::PubliclySubscribable,
)
conversation::StateMachine_strategy = st.builds(
    conversation::StateMachine,
)
conversation::View_strategy = st.builds(
    conversation::View,
)
conversation::AgentImport_strategy = st.builds(
    conversation::AgentImport,
)
conversation::TypeImport_strategy = st.builds(
    conversation::TypeImport,
)
conversation::Service_strategy = st.builds(
    conversation::Service,
)
conversation::RestService_strategy = st.builds(
    conversation::RestService,
)
conversation::Projection_strategy = st.builds(
    conversation::Projection,
)
conversation::Agent_strategy = st.builds(
    conversation::Agent,
    name=
        safe_text,
    connectionType=
        safe_text,
    stateMachineType=
        safe_text,
    accessRequirement=
        safe_text
)
conversation::Transition_strategy = st.builds(
    conversation::Transition,
    requiresExecution=
        st.booleans()
)
conversation::State_strategy = st.builds(
    conversation::State,
    join=
        st.booleans(),
    requiresExecution=
        st.booleans(),
    name=
        safe_text
)
conversation::Conversation_strategy = st.builds(
    conversation::Conversation,
    name=
        safe_text
)

@given(instance=conversation::Junction_strategy)
@settings(max_examples=50)
def test_conversation::junction_instantiation(instance):
    assert isinstance(instance, conversation::Junction)

@given(instance=SubscribableByOthers_strategy)
@settings(max_examples=50)
def test_subscribablebyothers_instantiation(instance):
    assert isinstance(instance, SubscribableByOthers)

@given(instance=PublishableByMe_strategy)
@settings(max_examples=50)
def test_publishablebyme_instantiation(instance):
    assert isinstance(instance, PublishableByMe)

@given(instance=PublicEvent_strategy)
@settings(max_examples=50)
def test_publicevent_instantiation(instance):
    assert isinstance(instance, PublicEvent)

@given(instance=PublishableByOthers_strategy)
@settings(max_examples=50)
def test_publishablebyothers_instantiation(instance):
    assert isinstance(instance, PublishableByOthers)

@given(instance=SubscribableByMe_strategy)
@settings(max_examples=50)
def test_subscribablebyme_instantiation(instance):
    assert isinstance(instance, SubscribableByMe)

@given(instance=conversation::PubliclyPublishable_strategy)
@settings(max_examples=50)
def test_conversation::publiclypublishable_instantiation(instance):
    assert isinstance(instance, conversation::PubliclyPublishable)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=conversation::SubscribableByMe_strategy)
@settings(max_examples=50)
def test_conversation::subscribablebyme_instantiation(instance):
    assert isinstance(instance, conversation::SubscribableByMe)

@given(instance=conversation::PublicEvent_strategy)
@settings(max_examples=50)
def test_conversation::publicevent_instantiation(instance):
    assert isinstance(instance, conversation::PublicEvent)

@given(instance=conversation::ProjectionField_strategy)
@settings(max_examples=50)
def test_conversation::projectionfield_instantiation(instance):
    assert isinstance(instance, conversation::ProjectionField)

@given(instance=conversation::Import_strategy)
@settings(max_examples=50)
def test_conversation::import_instantiation(instance):
    assert isinstance(instance, conversation::Import)

@given(instance=conversation::Import_strategy)
def test_conversation::import_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=conversation::Import_strategy)
def test_conversation::import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=PubliclySubscribable_strategy)
@settings(max_examples=50)
def test_publiclysubscribable_instantiation(instance):
    assert isinstance(instance, PubliclySubscribable)

@given(instance=PubliclyPublishable_strategy)
@settings(max_examples=50)
def test_publiclypublishable_instantiation(instance):
    assert isinstance(instance, PubliclyPublishable)

@given(instance=conversation::PublicPubSub_strategy)
@settings(max_examples=50)
def test_conversation::publicpubsub_instantiation(instance):
    assert isinstance(instance, conversation::PublicPubSub)

@given(instance=conversation::PublishableByOthers_strategy)
@settings(max_examples=50)
def test_conversation::publishablebyothers_instantiation(instance):
    assert isinstance(instance, conversation::PublishableByOthers)

@given(instance=conversation::PrivatePubSub_strategy)
@settings(max_examples=50)
def test_conversation::privatepubsub_instantiation(instance):
    assert isinstance(instance, conversation::PrivatePubSub)

@given(instance=conversation::SubscribableByOthers_strategy)
@settings(max_examples=50)
def test_conversation::subscribablebyothers_instantiation(instance):
    assert isinstance(instance, conversation::SubscribableByOthers)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=conversation::Join_strategy)
@settings(max_examples=50)
def test_conversation::join_instantiation(instance):
    assert isinstance(instance, conversation::Join)

@given(instance=conversation::Decision_strategy)
@settings(max_examples=50)
def test_conversation::decision_instantiation(instance):
    assert isinstance(instance, conversation::Decision)

@given(instance=conversation::Event_strategy)
@settings(max_examples=50)
def test_conversation::event_instantiation(instance):
    assert isinstance(instance, conversation::Event)

@given(instance=conversation::Event_strategy)
def test_conversation::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conversation::Event_strategy)
def test_conversation::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conversation::PublishableByMe_strategy)
@settings(max_examples=50)
def test_conversation::publishablebyme_instantiation(instance):
    assert isinstance(instance, conversation::PublishableByMe)

@given(instance=conversation::PubliclySubscribable_strategy)
@settings(max_examples=50)
def test_conversation::publiclysubscribable_instantiation(instance):
    assert isinstance(instance, conversation::PubliclySubscribable)

@given(instance=conversation::StateMachine_strategy)
@settings(max_examples=50)
def test_conversation::statemachine_instantiation(instance):
    assert isinstance(instance, conversation::StateMachine)

@given(instance=conversation::View_strategy)
@settings(max_examples=50)
def test_conversation::view_instantiation(instance):
    assert isinstance(instance, conversation::View)

@given(instance=conversation::AgentImport_strategy)
@settings(max_examples=50)
def test_conversation::agentimport_instantiation(instance):
    assert isinstance(instance, conversation::AgentImport)

@given(instance=conversation::TypeImport_strategy)
@settings(max_examples=50)
def test_conversation::typeimport_instantiation(instance):
    assert isinstance(instance, conversation::TypeImport)

@given(instance=conversation::Service_strategy)
@settings(max_examples=50)
def test_conversation::service_instantiation(instance):
    assert isinstance(instance, conversation::Service)

@given(instance=conversation::RestService_strategy)
@settings(max_examples=50)
def test_conversation::restservice_instantiation(instance):
    assert isinstance(instance, conversation::RestService)

@given(instance=conversation::Projection_strategy)
@settings(max_examples=50)
def test_conversation::projection_instantiation(instance):
    assert isinstance(instance, conversation::Projection)

@given(instance=conversation::Agent_strategy)
@settings(max_examples=50)
def test_conversation::agent_instantiation(instance):
    assert isinstance(instance, conversation::Agent)

@given(instance=conversation::Agent_strategy)
def test_conversation::agent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conversation::Agent_strategy)
def test_conversation::agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conversation::Agent_strategy)
def test_conversation::agent_connectionType_type(instance):
    assert isinstance(instance.connectionType, str)


@given(instance=conversation::Agent_strategy)
def test_conversation::agent_connectionType_setter(instance):
    original = instance.connectionType
    instance.connectionType = original
    assert instance.connectionType == original

@given(instance=conversation::Agent_strategy)
def test_conversation::agent_stateMachineType_type(instance):
    assert isinstance(instance.stateMachineType, str)


@given(instance=conversation::Agent_strategy)
def test_conversation::agent_stateMachineType_setter(instance):
    original = instance.stateMachineType
    instance.stateMachineType = original
    assert instance.stateMachineType == original

@given(instance=conversation::Agent_strategy)
def test_conversation::agent_accessRequirement_type(instance):
    assert isinstance(instance.accessRequirement, str)


@given(instance=conversation::Agent_strategy)
def test_conversation::agent_accessRequirement_setter(instance):
    original = instance.accessRequirement
    instance.accessRequirement = original
    assert instance.accessRequirement == original

@given(instance=conversation::Transition_strategy)
@settings(max_examples=50)
def test_conversation::transition_instantiation(instance):
    assert isinstance(instance, conversation::Transition)

@given(instance=conversation::Transition_strategy)
def test_conversation::transition_requiresExecution_type(instance):
    assert isinstance(instance.requiresExecution, bool)


@given(instance=conversation::Transition_strategy)
def test_conversation::transition_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original

@given(instance=conversation::State_strategy)
@settings(max_examples=50)
def test_conversation::state_instantiation(instance):
    assert isinstance(instance, conversation::State)

@given(instance=conversation::State_strategy)
def test_conversation::state_join_type(instance):
    assert isinstance(instance.join, bool)


@given(instance=conversation::State_strategy)
def test_conversation::state_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=conversation::State_strategy)
def test_conversation::state_requiresExecution_type(instance):
    assert isinstance(instance.requiresExecution, bool)


@given(instance=conversation::State_strategy)
def test_conversation::state_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original

@given(instance=conversation::State_strategy)
def test_conversation::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conversation::State_strategy)
def test_conversation::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conversation::Conversation_strategy)
@settings(max_examples=50)
def test_conversation::conversation_instantiation(instance):
    assert isinstance(instance, conversation::Conversation)

@given(instance=conversation::Conversation_strategy)
def test_conversation::conversation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conversation::Conversation_strategy)
def test_conversation::conversation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
