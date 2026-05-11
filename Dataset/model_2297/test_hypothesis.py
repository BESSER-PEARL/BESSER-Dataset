import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    emf::StateMachine,
    emf::State,
    emf::Action,
    emf::Transition,
    emf::TransitionToStateMapEntry,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emf::statemachine_is_not_abstract():
    assert not inspect.isabstract(emf::StateMachine)


def test_emf::statemachine_constructor_exists():
    assert callable(emf::StateMachine.__init__)


def test_emf::statemachine_constructor_args():
    sig = inspect.signature(emf::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_emf::state_is_not_abstract():
    assert not inspect.isabstract(emf::State)


def test_emf::state_constructor_exists():
    assert callable(emf::State.__init__)


def test_emf::state_constructor_args():
    sig = inspect.signature(emf::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_emf::state_has_name():
    assert hasattr(emf::State, "name")
    descriptor = None
    for klass in emf::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emf::state_has_type():
    assert hasattr(emf::State, "type")
    descriptor = None
    for klass in emf::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emf::action_is_not_abstract():
    assert not inspect.isabstract(emf::Action)


def test_emf::action_constructor_exists():
    assert callable(emf::Action.__init__)


def test_emf::action_constructor_args():
    sig = inspect.signature(emf::Action.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_emf::action_has_event():
    assert hasattr(emf::Action, "event")
    descriptor = None
    for klass in emf::Action.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_emf::transition_is_not_abstract():
    assert not inspect.isabstract(emf::Transition)


def test_emf::transition_constructor_exists():
    assert callable(emf::Transition.__init__)


def test_emf::transition_constructor_args():
    sig = inspect.signature(emf::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_emf::transition_has_action():
    assert hasattr(emf::Transition, "action")
    descriptor = None
    for klass in emf::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_emf::transitiontostatemapentry_is_not_abstract():
    assert not inspect.isabstract(emf::TransitionToStateMapEntry)


def test_emf::transitiontostatemapentry_constructor_exists():
    assert callable(emf::TransitionToStateMapEntry.__init__)


def test_emf::transitiontostatemapentry_constructor_args():
    sig = inspect.signature(emf::TransitionToStateMapEntry.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "FINAL",
        "NONE",
        "INITIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"


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
emf::StateMachine_strategy = st.builds(
    emf::StateMachine,
)
emf::State_strategy = st.builds(
    emf::State,
    name=
        safe_text,
    type=
        safe_text
)
emf::Action_strategy = st.builds(
    emf::Action,
    event=
        safe_text
)
emf::Transition_strategy = st.builds(
    emf::Transition,
    action=
        safe_text
)
emf::TransitionToStateMapEntry_strategy = st.builds(
    emf::TransitionToStateMapEntry,
)

@given(instance=emf::StateMachine_strategy)
@settings(max_examples=50)
def test_emf::statemachine_instantiation(instance):
    assert isinstance(instance, emf::StateMachine)

@given(instance=emf::State_strategy)
@settings(max_examples=50)
def test_emf::state_instantiation(instance):
    assert isinstance(instance, emf::State)

@given(instance=emf::State_strategy)
def test_emf::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emf::State_strategy)
def test_emf::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emf::State_strategy)
def test_emf::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=emf::State_strategy)
def test_emf::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emf::Action_strategy)
@settings(max_examples=50)
def test_emf::action_instantiation(instance):
    assert isinstance(instance, emf::Action)

@given(instance=emf::Action_strategy)
def test_emf::action_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=emf::Action_strategy)
def test_emf::action_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=emf::Transition_strategy)
@settings(max_examples=50)
def test_emf::transition_instantiation(instance):
    assert isinstance(instance, emf::Transition)

@given(instance=emf::Transition_strategy)
def test_emf::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=emf::Transition_strategy)
def test_emf::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=emf::TransitionToStateMapEntry_strategy)
@settings(max_examples=50)
def test_emf::transitiontostatemapentry_instantiation(instance):
    assert isinstance(instance, emf::TransitionToStateMapEntry)
