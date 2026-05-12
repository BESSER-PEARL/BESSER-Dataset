import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    esm_Transition,
    esm_State,
    esm_Machine,
    esm_EObject,
    State,
    esm_EndState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esm_transition_is_not_abstract():
    assert not inspect.isabstract(esm_Transition)


def test_esm_transition_constructor_exists():
    assert callable(esm_Transition.__init__)


def test_esm_transition_constructor_args():
    sig = inspect.signature(esm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_esm_transition_has_action():
    assert hasattr(esm_Transition, "action")
    descriptor = None
    for klass in esm_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_esm_state_is_not_abstract():
    assert not inspect.isabstract(esm_State)


def test_esm_state_constructor_exists():
    assert callable(esm_State.__init__)


def test_esm_state_constructor_args():
    sig = inspect.signature(esm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esm_state_has_name():
    assert hasattr(esm_State, "name")
    descriptor = None
    for klass in esm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esm_machine_is_not_abstract():
    assert not inspect.isabstract(esm_Machine)


def test_esm_machine_constructor_exists():
    assert callable(esm_Machine.__init__)


def test_esm_machine_constructor_args():
    sig = inspect.signature(esm_Machine.__init__)
    params = list(sig.parameters.keys())



def test_esm_eobject_is_not_abstract():
    assert not inspect.isabstract(esm_EObject)


def test_esm_eobject_constructor_exists():
    assert callable(esm_EObject.__init__)


def test_esm_eobject_constructor_args():
    sig = inspect.signature(esm_EObject.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_esm_endstate_is_not_abstract():
    assert not inspect.isabstract(esm_EndState)


def test_esm_endstate_constructor_exists():
    assert callable(esm_EndState.__init__)


def test_esm_endstate_constructor_args():
    sig = inspect.signature(esm_EndState.__init__)
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
esm_Transition_strategy = st.builds(
    esm_Transition,
    action=
        safe_text
)
esm_State_strategy = st.builds(
    esm_State,
    name=
        safe_text
)
esm_Machine_strategy = st.builds(
    esm_Machine,
)
esm_EObject_strategy = st.builds(
    esm_EObject,
)
State_strategy = st.builds(
    State,
)
esm_EndState_strategy = st.builds(
    esm_EndState,
)

@given(instance=esm_Transition_strategy)
@settings(max_examples=50)
def test_esm_transition_instantiation(instance):
    assert isinstance(instance, esm_Transition)



@given(instance=esm_Transition_strategy)
def test_esm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=esm_State_strategy)
@settings(max_examples=50)
def test_esm_state_instantiation(instance):
    assert isinstance(instance, esm_State)



@given(instance=esm_State_strategy)
def test_esm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esm_Machine_strategy)
@settings(max_examples=50)
def test_esm_machine_instantiation(instance):
    assert isinstance(instance, esm_Machine)

@given(instance=esm_EObject_strategy)
@settings(max_examples=50)
def test_esm_eobject_instantiation(instance):
    assert isinstance(instance, esm_EObject)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=esm_EndState_strategy)
@settings(max_examples=50)
def test_esm_endstate_instantiation(instance):
    assert isinstance(instance, esm_EndState)
