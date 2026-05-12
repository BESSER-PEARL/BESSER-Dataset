import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    emf_Transition,
    emf_TransitionToStateMapEntry,
    emf_StateMachine,
    emf_State,
    emf_Action,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emf_transition_is_not_abstract():
    assert not inspect.isabstract(emf_Transition)


def test_emf_transition_constructor_exists():
    assert callable(emf_Transition.__init__)


def test_emf_transition_constructor_args():
    sig = inspect.signature(emf_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_emf_transition_has_action():
    assert hasattr(emf_Transition, "action")
    descriptor = None
    for klass in emf_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_emf_transitiontostatemapentry_is_not_abstract():
    assert not inspect.isabstract(emf_TransitionToStateMapEntry)


def test_emf_transitiontostatemapentry_constructor_exists():
    assert callable(emf_TransitionToStateMapEntry.__init__)


def test_emf_transitiontostatemapentry_constructor_args():
    sig = inspect.signature(emf_TransitionToStateMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_emf_statemachine_is_not_abstract():
    assert not inspect.isabstract(emf_StateMachine)


def test_emf_statemachine_constructor_exists():
    assert callable(emf_StateMachine.__init__)


def test_emf_statemachine_constructor_args():
    sig = inspect.signature(emf_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_emf_state_is_not_abstract():
    assert not inspect.isabstract(emf_State)


def test_emf_state_constructor_exists():
    assert callable(emf_State.__init__)


def test_emf_state_constructor_args():
    sig = inspect.signature(emf_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_emf_state_has_name():
    assert hasattr(emf_State, "name")
    descriptor = None
    for klass in emf_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emf_state_has_type():
    assert hasattr(emf_State, "type")
    descriptor = None
    for klass in emf_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emf_action_is_not_abstract():
    assert not inspect.isabstract(emf_Action)


def test_emf_action_constructor_exists():
    assert callable(emf_Action.__init__)


def test_emf_action_constructor_args():
    sig = inspect.signature(emf_Action.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_emf_action_has_event():
    assert hasattr(emf_Action, "event")
    descriptor = None
    for klass in emf_Action.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "INITIAL",
        "FINAL",
        "NONE",
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
emf_Transition_strategy = st.builds(
    emf_Transition,
    action=
        safe_text
)
emf_TransitionToStateMapEntry_strategy = st.builds(
    emf_TransitionToStateMapEntry,
)
emf_StateMachine_strategy = st.builds(
    emf_StateMachine,
)
emf_State_strategy = st.builds(
    emf_State,
    name=
        safe_text,
    type=
        safe_text
)
emf_Action_strategy = st.builds(
    emf_Action,
    event=
        safe_text
)

@given(instance=emf_Transition_strategy)
@settings(max_examples=50)
def test_emf_transition_instantiation(instance):
    assert isinstance(instance, emf_Transition)



@given(instance=emf_Transition_strategy)
def test_emf_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=emf_TransitionToStateMapEntry_strategy)
@settings(max_examples=50)
def test_emf_transitiontostatemapentry_instantiation(instance):
    assert isinstance(instance, emf_TransitionToStateMapEntry)

@given(instance=emf_StateMachine_strategy)
@settings(max_examples=50)
def test_emf_statemachine_instantiation(instance):
    assert isinstance(instance, emf_StateMachine)

@given(instance=emf_State_strategy)
@settings(max_examples=50)
def test_emf_state_instantiation(instance):
    assert isinstance(instance, emf_State)



@given(instance=emf_State_strategy)
def test_emf_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=emf_State_strategy)
def test_emf_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emf_Action_strategy)
@settings(max_examples=50)
def test_emf_action_instantiation(instance):
    assert isinstance(instance, emf_Action)



@given(instance=emf_Action_strategy)
def test_emf_action_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
