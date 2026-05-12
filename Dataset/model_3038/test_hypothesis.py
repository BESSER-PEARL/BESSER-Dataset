import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    conversation_Junction,
    SubscribableByOthers,
    PublishableByMe,
    PublicEvent,
    PublishableByOthers,
    SubscribableByMe,
    conversation_PubliclyPublishable,
    Event,
    conversation_PublicEvent,
    conversation_SubscribableByMe,
    conversation_ProjectionField,
    conversation_Import,
    Import,
    PubliclySubscribable,
    PubliclyPublishable,
    conversation_PublicPubSub,
    conversation_PublishableByOthers,
    conversation_PrivatePubSub,
    conversation_SubscribableByOthers,
    State,
    conversation_Join,
    conversation_Decision,
    conversation_Event,
    conversation_PublishableByMe,
    conversation_PubliclySubscribable,
    conversation_StateMachine,
    conversation_View,
    conversation_AgentImport,
    conversation_TypeImport,
    conversation_Service,
    conversation_RestService,
    conversation_Projection,
    conversation_Agent,
    conversation_Transition,
    conversation_State,
    conversation_Conversation,
    ConnectionType,
    StateMachineType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conversation_junction_is_not_abstract():
    assert not inspect.isabstract(conversation_Junction)


def test_conversation_junction_constructor_exists():
    assert callable(conversation_Junction.__init__)


def test_conversation_junction_constructor_args():
    sig = inspect.signature(conversation_Junction.__init__)
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



def test_conversation_publiclypublishable_is_not_abstract():
    assert not inspect.isabstract(conversation_PubliclyPublishable)


def test_conversation_publiclypublishable_constructor_exists():
    assert callable(conversation_PubliclyPublishable.__init__)


def test_conversation_publiclypublishable_constructor_args():
    sig = inspect.signature(conversation_PubliclyPublishable.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_conversation_publicevent_is_not_abstract():
    assert not inspect.isabstract(conversation_PublicEvent)


def test_conversation_publicevent_constructor_exists():
    assert callable(conversation_PublicEvent.__init__)


def test_conversation_publicevent_constructor_args():
    sig = inspect.signature(conversation_PublicEvent.__init__)
    params = list(sig.parameters.keys())



def test_conversation_subscribablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation_SubscribableByMe)


def test_conversation_subscribablebyme_constructor_exists():
    assert callable(conversation_SubscribableByMe.__init__)


def test_conversation_subscribablebyme_constructor_args():
    sig = inspect.signature(conversation_SubscribableByMe.__init__)
    params = list(sig.parameters.keys())



def test_conversation_projectionfield_is_not_abstract():
    assert not inspect.isabstract(conversation_ProjectionField)


def test_conversation_projectionfield_constructor_exists():
    assert callable(conversation_ProjectionField.__init__)


def test_conversation_projectionfield_constructor_args():
    sig = inspect.signature(conversation_ProjectionField.__init__)
    params = list(sig.parameters.keys())



def test_conversation_import_is_not_abstract():
    assert not inspect.isabstract(conversation_Import)


def test_conversation_import_constructor_exists():
    assert callable(conversation_Import.__init__)


def test_conversation_import_constructor_args():
    sig = inspect.signature(conversation_Import.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_conversation_import_has_alias():
    assert hasattr(conversation_Import, "alias")
    descriptor = None
    for klass in conversation_Import.__mro__:
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



def test_conversation_publicpubsub_is_not_abstract():
    assert not inspect.isabstract(conversation_PublicPubSub)


def test_conversation_publicpubsub_constructor_exists():
    assert callable(conversation_PublicPubSub.__init__)


def test_conversation_publicpubsub_constructor_args():
    sig = inspect.signature(conversation_PublicPubSub.__init__)
    params = list(sig.parameters.keys())



def test_conversation_publishablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation_PublishableByOthers)


def test_conversation_publishablebyothers_constructor_exists():
    assert callable(conversation_PublishableByOthers.__init__)


def test_conversation_publishablebyothers_constructor_args():
    sig = inspect.signature(conversation_PublishableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_conversation_privatepubsub_is_not_abstract():
    assert not inspect.isabstract(conversation_PrivatePubSub)


def test_conversation_privatepubsub_constructor_exists():
    assert callable(conversation_PrivatePubSub.__init__)


def test_conversation_privatepubsub_constructor_args():
    sig = inspect.signature(conversation_PrivatePubSub.__init__)
    params = list(sig.parameters.keys())



def test_conversation_subscribablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation_SubscribableByOthers)


def test_conversation_subscribablebyothers_constructor_exists():
    assert callable(conversation_SubscribableByOthers.__init__)


def test_conversation_subscribablebyothers_constructor_args():
    sig = inspect.signature(conversation_SubscribableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_conversation_join_is_not_abstract():
    assert not inspect.isabstract(conversation_Join)


def test_conversation_join_constructor_exists():
    assert callable(conversation_Join.__init__)


def test_conversation_join_constructor_args():
    sig = inspect.signature(conversation_Join.__init__)
    params = list(sig.parameters.keys())



def test_conversation_decision_is_not_abstract():
    assert not inspect.isabstract(conversation_Decision)


def test_conversation_decision_constructor_exists():
    assert callable(conversation_Decision.__init__)


def test_conversation_decision_constructor_args():
    sig = inspect.signature(conversation_Decision.__init__)
    params = list(sig.parameters.keys())



def test_conversation_event_is_not_abstract():
    assert not inspect.isabstract(conversation_Event)


def test_conversation_event_constructor_exists():
    assert callable(conversation_Event.__init__)


def test_conversation_event_constructor_args():
    sig = inspect.signature(conversation_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conversation_event_has_name():
    assert hasattr(conversation_Event, "name")
    descriptor = None
    for klass in conversation_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conversation_publishablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation_PublishableByMe)


def test_conversation_publishablebyme_constructor_exists():
    assert callable(conversation_PublishableByMe.__init__)


def test_conversation_publishablebyme_constructor_args():
    sig = inspect.signature(conversation_PublishableByMe.__init__)
    params = list(sig.parameters.keys())



def test_conversation_publiclysubscribable_is_not_abstract():
    assert not inspect.isabstract(conversation_PubliclySubscribable)


def test_conversation_publiclysubscribable_constructor_exists():
    assert callable(conversation_PubliclySubscribable.__init__)


def test_conversation_publiclysubscribable_constructor_args():
    sig = inspect.signature(conversation_PubliclySubscribable.__init__)
    params = list(sig.parameters.keys())



def test_conversation_statemachine_is_not_abstract():
    assert not inspect.isabstract(conversation_StateMachine)


def test_conversation_statemachine_constructor_exists():
    assert callable(conversation_StateMachine.__init__)


def test_conversation_statemachine_constructor_args():
    sig = inspect.signature(conversation_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_conversation_view_is_not_abstract():
    assert not inspect.isabstract(conversation_View)


def test_conversation_view_constructor_exists():
    assert callable(conversation_View.__init__)


def test_conversation_view_constructor_args():
    sig = inspect.signature(conversation_View.__init__)
    params = list(sig.parameters.keys())



def test_conversation_agentimport_is_not_abstract():
    assert not inspect.isabstract(conversation_AgentImport)


def test_conversation_agentimport_constructor_exists():
    assert callable(conversation_AgentImport.__init__)


def test_conversation_agentimport_constructor_args():
    sig = inspect.signature(conversation_AgentImport.__init__)
    params = list(sig.parameters.keys())



def test_conversation_typeimport_is_not_abstract():
    assert not inspect.isabstract(conversation_TypeImport)


def test_conversation_typeimport_constructor_exists():
    assert callable(conversation_TypeImport.__init__)


def test_conversation_typeimport_constructor_args():
    sig = inspect.signature(conversation_TypeImport.__init__)
    params = list(sig.parameters.keys())



def test_conversation_service_is_not_abstract():
    assert not inspect.isabstract(conversation_Service)


def test_conversation_service_constructor_exists():
    assert callable(conversation_Service.__init__)


def test_conversation_service_constructor_args():
    sig = inspect.signature(conversation_Service.__init__)
    params = list(sig.parameters.keys())



def test_conversation_restservice_is_not_abstract():
    assert not inspect.isabstract(conversation_RestService)


def test_conversation_restservice_constructor_exists():
    assert callable(conversation_RestService.__init__)


def test_conversation_restservice_constructor_args():
    sig = inspect.signature(conversation_RestService.__init__)
    params = list(sig.parameters.keys())



def test_conversation_projection_is_not_abstract():
    assert not inspect.isabstract(conversation_Projection)


def test_conversation_projection_constructor_exists():
    assert callable(conversation_Projection.__init__)


def test_conversation_projection_constructor_args():
    sig = inspect.signature(conversation_Projection.__init__)
    params = list(sig.parameters.keys())



def test_conversation_agent_is_not_abstract():
    assert not inspect.isabstract(conversation_Agent)


def test_conversation_agent_constructor_exists():
    assert callable(conversation_Agent.__init__)


def test_conversation_agent_constructor_args():
    sig = inspect.signature(conversation_Agent.__init__)
    params = list(sig.parameters.keys())
    assert "accessRequirement" in params, "Missing parameter 'accessRequirement'"
    assert "stateMachineType" in params, "Missing parameter 'stateMachineType'"
    assert "connectionType" in params, "Missing parameter 'connectionType'"
    assert "name" in params, "Missing parameter 'name'"

def test_conversation_agent_has_accessRequirement():
    assert hasattr(conversation_Agent, "accessRequirement")
    descriptor = None
    for klass in conversation_Agent.__mro__:
        if "accessRequirement" in klass.__dict__:
            descriptor = klass.__dict__["accessRequirement"]
            break
    assert isinstance(descriptor, property)

def test_conversation_agent_has_stateMachineType():
    assert hasattr(conversation_Agent, "stateMachineType")
    descriptor = None
    for klass in conversation_Agent.__mro__:
        if "stateMachineType" in klass.__dict__:
            descriptor = klass.__dict__["stateMachineType"]
            break
    assert isinstance(descriptor, property)

def test_conversation_agent_has_connectionType():
    assert hasattr(conversation_Agent, "connectionType")
    descriptor = None
    for klass in conversation_Agent.__mro__:
        if "connectionType" in klass.__dict__:
            descriptor = klass.__dict__["connectionType"]
            break
    assert isinstance(descriptor, property)

def test_conversation_agent_has_name():
    assert hasattr(conversation_Agent, "name")
    descriptor = None
    for klass in conversation_Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conversation_transition_is_not_abstract():
    assert not inspect.isabstract(conversation_Transition)


def test_conversation_transition_constructor_exists():
    assert callable(conversation_Transition.__init__)


def test_conversation_transition_constructor_args():
    sig = inspect.signature(conversation_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"

def test_conversation_transition_has_requiresExecution():
    assert hasattr(conversation_Transition, "requiresExecution")
    descriptor = None
    for klass in conversation_Transition.__mro__:
        if "requiresExecution" in klass.__dict__:
            descriptor = klass.__dict__["requiresExecution"]
            break
    assert isinstance(descriptor, property)



def test_conversation_state_is_not_abstract():
    assert not inspect.isabstract(conversation_State)


def test_conversation_state_constructor_exists():
    assert callable(conversation_State.__init__)


def test_conversation_state_constructor_args():
    sig = inspect.signature(conversation_State.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"
    assert "name" in params, "Missing parameter 'name'"
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"

def test_conversation_state_has_join():
    assert hasattr(conversation_State, "join")
    descriptor = None
    for klass in conversation_State.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_conversation_state_has_name():
    assert hasattr(conversation_State, "name")
    descriptor = None
    for klass in conversation_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_conversation_state_has_requiresExecution():
    assert hasattr(conversation_State, "requiresExecution")
    descriptor = None
    for klass in conversation_State.__mro__:
        if "requiresExecution" in klass.__dict__:
            descriptor = klass.__dict__["requiresExecution"]
            break
    assert isinstance(descriptor, property)



def test_conversation_conversation_is_not_abstract():
    assert not inspect.isabstract(conversation_Conversation)


def test_conversation_conversation_constructor_exists():
    assert callable(conversation_Conversation.__init__)


def test_conversation_conversation_constructor_args():
    sig = inspect.signature(conversation_Conversation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conversation_conversation_has_name():
    assert hasattr(conversation_Conversation, "name")
    descriptor = None
    for klass in conversation_Conversation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_connectiontype_exists():
    # Check that the Enumeration exists
    assert ConnectionType is not None

def test_connectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionType]
    expected_literals = [
        "independent",
        "dependent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionType"

def test_statemachinetype_exists():
    # Check that the Enumeration exists
    assert StateMachineType is not None

def test_statemachinetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateMachineType]
    expected_literals = [
        "infinite",
        "finite",
        "stateless",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateMachineType"


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
conversation_Junction_strategy = st.builds(
    conversation_Junction,
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
conversation_PubliclyPublishable_strategy = st.builds(
    conversation_PubliclyPublishable,
)
Event_strategy = st.builds(
    Event,
)
conversation_PublicEvent_strategy = st.builds(
    conversation_PublicEvent,
)
conversation_SubscribableByMe_strategy = st.builds(
    conversation_SubscribableByMe,
)
conversation_ProjectionField_strategy = st.builds(
    conversation_ProjectionField,
)
conversation_Import_strategy = st.builds(
    conversation_Import,
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
conversation_PublicPubSub_strategy = st.builds(
    conversation_PublicPubSub,
)
conversation_PublishableByOthers_strategy = st.builds(
    conversation_PublishableByOthers,
)
conversation_PrivatePubSub_strategy = st.builds(
    conversation_PrivatePubSub,
)
conversation_SubscribableByOthers_strategy = st.builds(
    conversation_SubscribableByOthers,
)
State_strategy = st.builds(
    State,
)
conversation_Join_strategy = st.builds(
    conversation_Join,
)
conversation_Decision_strategy = st.builds(
    conversation_Decision,
)
conversation_Event_strategy = st.builds(
    conversation_Event,
    name=
        safe_text
)
conversation_PublishableByMe_strategy = st.builds(
    conversation_PublishableByMe,
)
conversation_PubliclySubscribable_strategy = st.builds(
    conversation_PubliclySubscribable,
)
conversation_StateMachine_strategy = st.builds(
    conversation_StateMachine,
)
conversation_View_strategy = st.builds(
    conversation_View,
)
conversation_AgentImport_strategy = st.builds(
    conversation_AgentImport,
)
conversation_TypeImport_strategy = st.builds(
    conversation_TypeImport,
)
conversation_Service_strategy = st.builds(
    conversation_Service,
)
conversation_RestService_strategy = st.builds(
    conversation_RestService,
)
conversation_Projection_strategy = st.builds(
    conversation_Projection,
)
conversation_Agent_strategy = st.builds(
    conversation_Agent,
    accessRequirement=
        safe_text,
    stateMachineType=
        safe_text,
    connectionType=
        safe_text,
    name=
        safe_text
)
conversation_Transition_strategy = st.builds(
    conversation_Transition,
    requiresExecution=
        st.booleans()
)
conversation_State_strategy = st.builds(
    conversation_State,
    join=
        st.booleans(),
    name=
        safe_text,
    requiresExecution=
        st.booleans()
)
conversation_Conversation_strategy = st.builds(
    conversation_Conversation,
    name=
        safe_text
)

@given(instance=conversation_Junction_strategy)
@settings(max_examples=50)
def test_conversation_junction_instantiation(instance):
    assert isinstance(instance, conversation_Junction)

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

@given(instance=conversation_PubliclyPublishable_strategy)
@settings(max_examples=50)
def test_conversation_publiclypublishable_instantiation(instance):
    assert isinstance(instance, conversation_PubliclyPublishable)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=conversation_PublicEvent_strategy)
@settings(max_examples=50)
def test_conversation_publicevent_instantiation(instance):
    assert isinstance(instance, conversation_PublicEvent)

@given(instance=conversation_SubscribableByMe_strategy)
@settings(max_examples=50)
def test_conversation_subscribablebyme_instantiation(instance):
    assert isinstance(instance, conversation_SubscribableByMe)

@given(instance=conversation_ProjectionField_strategy)
@settings(max_examples=50)
def test_conversation_projectionfield_instantiation(instance):
    assert isinstance(instance, conversation_ProjectionField)

@given(instance=conversation_Import_strategy)
@settings(max_examples=50)
def test_conversation_import_instantiation(instance):
    assert isinstance(instance, conversation_Import)



@given(instance=conversation_Import_strategy)
def test_conversation_import_alias_setter(instance):
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

@given(instance=conversation_PublicPubSub_strategy)
@settings(max_examples=50)
def test_conversation_publicpubsub_instantiation(instance):
    assert isinstance(instance, conversation_PublicPubSub)

@given(instance=conversation_PublishableByOthers_strategy)
@settings(max_examples=50)
def test_conversation_publishablebyothers_instantiation(instance):
    assert isinstance(instance, conversation_PublishableByOthers)

@given(instance=conversation_PrivatePubSub_strategy)
@settings(max_examples=50)
def test_conversation_privatepubsub_instantiation(instance):
    assert isinstance(instance, conversation_PrivatePubSub)

@given(instance=conversation_SubscribableByOthers_strategy)
@settings(max_examples=50)
def test_conversation_subscribablebyothers_instantiation(instance):
    assert isinstance(instance, conversation_SubscribableByOthers)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=conversation_Join_strategy)
@settings(max_examples=50)
def test_conversation_join_instantiation(instance):
    assert isinstance(instance, conversation_Join)

@given(instance=conversation_Decision_strategy)
@settings(max_examples=50)
def test_conversation_decision_instantiation(instance):
    assert isinstance(instance, conversation_Decision)

@given(instance=conversation_Event_strategy)
@settings(max_examples=50)
def test_conversation_event_instantiation(instance):
    assert isinstance(instance, conversation_Event)



@given(instance=conversation_Event_strategy)
def test_conversation_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conversation_PublishableByMe_strategy)
@settings(max_examples=50)
def test_conversation_publishablebyme_instantiation(instance):
    assert isinstance(instance, conversation_PublishableByMe)

@given(instance=conversation_PubliclySubscribable_strategy)
@settings(max_examples=50)
def test_conversation_publiclysubscribable_instantiation(instance):
    assert isinstance(instance, conversation_PubliclySubscribable)

@given(instance=conversation_StateMachine_strategy)
@settings(max_examples=50)
def test_conversation_statemachine_instantiation(instance):
    assert isinstance(instance, conversation_StateMachine)

@given(instance=conversation_View_strategy)
@settings(max_examples=50)
def test_conversation_view_instantiation(instance):
    assert isinstance(instance, conversation_View)

@given(instance=conversation_AgentImport_strategy)
@settings(max_examples=50)
def test_conversation_agentimport_instantiation(instance):
    assert isinstance(instance, conversation_AgentImport)

@given(instance=conversation_TypeImport_strategy)
@settings(max_examples=50)
def test_conversation_typeimport_instantiation(instance):
    assert isinstance(instance, conversation_TypeImport)

@given(instance=conversation_Service_strategy)
@settings(max_examples=50)
def test_conversation_service_instantiation(instance):
    assert isinstance(instance, conversation_Service)

@given(instance=conversation_RestService_strategy)
@settings(max_examples=50)
def test_conversation_restservice_instantiation(instance):
    assert isinstance(instance, conversation_RestService)

@given(instance=conversation_Projection_strategy)
@settings(max_examples=50)
def test_conversation_projection_instantiation(instance):
    assert isinstance(instance, conversation_Projection)

@given(instance=conversation_Agent_strategy)
@settings(max_examples=50)
def test_conversation_agent_instantiation(instance):
    assert isinstance(instance, conversation_Agent)



@given(instance=conversation_Agent_strategy)
def test_conversation_agent_accessRequirement_setter(instance):
    original = instance.accessRequirement
    instance.accessRequirement = original
    assert instance.accessRequirement == original



@given(instance=conversation_Agent_strategy)
def test_conversation_agent_stateMachineType_setter(instance):
    original = instance.stateMachineType
    instance.stateMachineType = original
    assert instance.stateMachineType == original



@given(instance=conversation_Agent_strategy)
def test_conversation_agent_connectionType_setter(instance):
    original = instance.connectionType
    instance.connectionType = original
    assert instance.connectionType == original



@given(instance=conversation_Agent_strategy)
def test_conversation_agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conversation_Transition_strategy)
@settings(max_examples=50)
def test_conversation_transition_instantiation(instance):
    assert isinstance(instance, conversation_Transition)



@given(instance=conversation_Transition_strategy)
def test_conversation_transition_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original

@given(instance=conversation_State_strategy)
@settings(max_examples=50)
def test_conversation_state_instantiation(instance):
    assert isinstance(instance, conversation_State)



@given(instance=conversation_State_strategy)
def test_conversation_state_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original



@given(instance=conversation_State_strategy)
def test_conversation_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=conversation_State_strategy)
def test_conversation_state_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original

@given(instance=conversation_Conversation_strategy)
@settings(max_examples=50)
def test_conversation_conversation_instantiation(instance):
    assert isinstance(instance, conversation_Conversation)



@given(instance=conversation_Conversation_strategy)
def test_conversation_conversation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
