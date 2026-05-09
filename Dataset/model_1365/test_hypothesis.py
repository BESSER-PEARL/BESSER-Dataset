import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BehavioralFeature,
    statemachine::Operation,
    MessageEvent,
    statemachine::CallEvent,
    Event,
    statemachine::MessageEvent,
    statemachine::Event,
    State,
    statemachine::FinalState,
    Vertex,
    statemachine::State,
    statemachine::PseudoState,
    statemachine::Trigger,
    statemachine::Constraint,
    NamedElement,
    statemachine::BehavioralFeature,
    statemachine::Transition,
    statemachine::Vertex,
    statemachine::Behavior,
    statemachine::BehavioredClassifier,
    statemachine::NamedElement,
    statemachine::Region,
    Behavior,
    statemachine::OpaqueBehavior,
    statemachine::StateMachine,
    BehavioredClassifier,
    statemachine::Class,
    PseudoStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::operation_is_not_abstract():
    assert not inspect.isabstract(statemachine::Operation)


def test_statemachine::operation_constructor_exists():
    assert callable(statemachine::Operation.__init__)


def test_statemachine::operation_constructor_args():
    sig = inspect.signature(statemachine::Operation.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::callevent_is_not_abstract():
    assert not inspect.isabstract(statemachine::CallEvent)


def test_statemachine::callevent_constructor_exists():
    assert callable(statemachine::CallEvent.__init__)


def test_statemachine::callevent_constructor_args():
    sig = inspect.signature(statemachine::CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::messageevent_is_not_abstract():
    assert not inspect.isabstract(statemachine::MessageEvent)


def test_statemachine::messageevent_constructor_exists():
    assert callable(statemachine::MessageEvent.__init__)


def test_statemachine::messageevent_constructor_args():
    sig = inspect.signature(statemachine::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine::PseudoState)


def test_statemachine::pseudostate_constructor_exists():
    assert callable(statemachine::PseudoState.__init__)


def test_statemachine::pseudostate_constructor_args():
    sig = inspect.signature(statemachine::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine::pseudostate_has_kind():
    assert hasattr(statemachine::PseudoState, "kind")
    descriptor = None
    for klass in statemachine::PseudoState.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::trigger_is_not_abstract():
    assert not inspect.isabstract(statemachine::Trigger)


def test_statemachine::trigger_constructor_exists():
    assert callable(statemachine::Trigger.__init__)


def test_statemachine::trigger_constructor_args():
    sig = inspect.signature(statemachine::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::constraint_is_not_abstract():
    assert not inspect.isabstract(statemachine::Constraint)


def test_statemachine::constraint_constructor_exists():
    assert callable(statemachine::Constraint.__init__)


def test_statemachine::constraint_constructor_args():
    sig = inspect.signature(statemachine::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(statemachine::BehavioralFeature)


def test_statemachine::behavioralfeature_constructor_exists():
    assert callable(statemachine::BehavioralFeature.__init__)


def test_statemachine::behavioralfeature_constructor_args():
    sig = inspect.signature(statemachine::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::vertex_is_not_abstract():
    assert not inspect.isabstract(statemachine::Vertex)


def test_statemachine::vertex_constructor_exists():
    assert callable(statemachine::Vertex.__init__)


def test_statemachine::vertex_constructor_args():
    sig = inspect.signature(statemachine::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::behavior_is_not_abstract():
    assert not inspect.isabstract(statemachine::Behavior)


def test_statemachine::behavior_constructor_exists():
    assert callable(statemachine::Behavior.__init__)


def test_statemachine::behavior_constructor_args():
    sig = inspect.signature(statemachine::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(statemachine::BehavioredClassifier)


def test_statemachine::behavioredclassifier_constructor_exists():
    assert callable(statemachine::BehavioredClassifier.__init__)


def test_statemachine::behavioredclassifier_constructor_args():
    sig = inspect.signature(statemachine::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine::NamedElement)


def test_statemachine::namedelement_constructor_exists():
    assert callable(statemachine::NamedElement.__init__)


def test_statemachine::namedelement_constructor_args():
    sig = inspect.signature(statemachine::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::region_is_not_abstract():
    assert not inspect.isabstract(statemachine::Region)


def test_statemachine::region_constructor_exists():
    assert callable(statemachine::Region.__init__)


def test_statemachine::region_constructor_args():
    sig = inspect.signature(statemachine::Region.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(statemachine::OpaqueBehavior)


def test_statemachine::opaquebehavior_constructor_exists():
    assert callable(statemachine::OpaqueBehavior.__init__)


def test_statemachine::opaquebehavior_constructor_args():
    sig = inspect.signature(statemachine::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_statemachine::opaquebehavior_has_body():
    assert hasattr(statemachine::OpaqueBehavior, "body")
    descriptor = None
    for klass in statemachine::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::opaquebehavior_has_language():
    assert hasattr(statemachine::OpaqueBehavior, "language")
    descriptor = None
    for klass in statemachine::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::class_is_not_abstract():
    assert not inspect.isabstract(statemachine::Class)


def test_statemachine::class_constructor_exists():
    assert callable(statemachine::Class.__init__)


def test_statemachine::class_constructor_args():
    sig = inspect.signature(statemachine::Class.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"


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
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
statemachine::Operation_strategy = st.builds(
    statemachine::Operation,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
statemachine::CallEvent_strategy = st.builds(
    statemachine::CallEvent,
)
Event_strategy = st.builds(
    Event,
)
statemachine::MessageEvent_strategy = st.builds(
    statemachine::MessageEvent,
)
statemachine::Event_strategy = st.builds(
    statemachine::Event,
)
State_strategy = st.builds(
    State,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
)
statemachine::PseudoState_strategy = st.builds(
    statemachine::PseudoState,
    kind=
        safe_text
)
statemachine::Trigger_strategy = st.builds(
    statemachine::Trigger,
)
statemachine::Constraint_strategy = st.builds(
    statemachine::Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachine::BehavioralFeature_strategy = st.builds(
    statemachine::BehavioralFeature,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::Vertex_strategy = st.builds(
    statemachine::Vertex,
)
statemachine::Behavior_strategy = st.builds(
    statemachine::Behavior,
)
statemachine::BehavioredClassifier_strategy = st.builds(
    statemachine::BehavioredClassifier,
)
statemachine::NamedElement_strategy = st.builds(
    statemachine::NamedElement,
)
statemachine::Region_strategy = st.builds(
    statemachine::Region,
)
Behavior_strategy = st.builds(
    Behavior,
)
statemachine::OpaqueBehavior_strategy = st.builds(
    statemachine::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
statemachine::Class_strategy = st.builds(
    statemachine::Class,
)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=statemachine::Operation_strategy)
@settings(max_examples=50)
def test_statemachine::operation_instantiation(instance):
    assert isinstance(instance, statemachine::Operation)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=statemachine::CallEvent_strategy)
@settings(max_examples=50)
def test_statemachine::callevent_instantiation(instance):
    assert isinstance(instance, statemachine::CallEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statemachine::MessageEvent_strategy)
@settings(max_examples=50)
def test_statemachine::messageevent_instantiation(instance):
    assert isinstance(instance, statemachine::MessageEvent)

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::PseudoState_strategy)
@settings(max_examples=50)
def test_statemachine::pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine::PseudoState)

@given(instance=statemachine::PseudoState_strategy)
def test_statemachine::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=statemachine::PseudoState_strategy)
def test_statemachine::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=statemachine::Trigger_strategy)
@settings(max_examples=50)
def test_statemachine::trigger_instantiation(instance):
    assert isinstance(instance, statemachine::Trigger)

@given(instance=statemachine::Constraint_strategy)
@settings(max_examples=50)
def test_statemachine::constraint_instantiation(instance):
    assert isinstance(instance, statemachine::Constraint)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachine::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_statemachine::behavioralfeature_instantiation(instance):
    assert isinstance(instance, statemachine::BehavioralFeature)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Vertex_strategy)
@settings(max_examples=50)
def test_statemachine::vertex_instantiation(instance):
    assert isinstance(instance, statemachine::Vertex)

@given(instance=statemachine::Behavior_strategy)
@settings(max_examples=50)
def test_statemachine::behavior_instantiation(instance):
    assert isinstance(instance, statemachine::Behavior)

@given(instance=statemachine::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_statemachine::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, statemachine::BehavioredClassifier)

@given(instance=statemachine::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine::namedelement_instantiation(instance):
    assert isinstance(instance, statemachine::NamedElement)

@given(instance=statemachine::Region_strategy)
@settings(max_examples=50)
def test_statemachine::region_instantiation(instance):
    assert isinstance(instance, statemachine::Region)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=statemachine::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_statemachine::opaquebehavior_instantiation(instance):
    assert isinstance(instance, statemachine::OpaqueBehavior)

@given(instance=statemachine::OpaqueBehavior_strategy)
def test_statemachine::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=statemachine::OpaqueBehavior_strategy)
def test_statemachine::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=statemachine::OpaqueBehavior_strategy)
def test_statemachine::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=statemachine::OpaqueBehavior_strategy)
def test_statemachine::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=statemachine::Class_strategy)
@settings(max_examples=50)
def test_statemachine::class_instantiation(instance):
    assert isinstance(instance, statemachine::Class)
