import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    esm::Transition,
    esm::State,
    esm::Machine,
    esm::EObject,
    State,
    esm::EndState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esm::transition_is_not_abstract():
    assert not inspect.isabstract(esm::Transition)


def test_esm::transition_constructor_exists():
    assert callable(esm::Transition.__init__)


def test_esm::transition_constructor_args():
    sig = inspect.signature(esm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_esm::transition_has_action():
    assert hasattr(esm::Transition, "action")
    descriptor = None
    for klass in esm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_esm::state_is_not_abstract():
    assert not inspect.isabstract(esm::State)


def test_esm::state_constructor_exists():
    assert callable(esm::State.__init__)


def test_esm::state_constructor_args():
    sig = inspect.signature(esm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esm::state_has_name():
    assert hasattr(esm::State, "name")
    descriptor = None
    for klass in esm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esm::machine_is_not_abstract():
    assert not inspect.isabstract(esm::Machine)


def test_esm::machine_constructor_exists():
    assert callable(esm::Machine.__init__)


def test_esm::machine_constructor_args():
    sig = inspect.signature(esm::Machine.__init__)
    params = list(sig.parameters.keys())



def test_esm::eobject_is_not_abstract():
    assert not inspect.isabstract(esm::EObject)


def test_esm::eobject_constructor_exists():
    assert callable(esm::EObject.__init__)


def test_esm::eobject_constructor_args():
    sig = inspect.signature(esm::EObject.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_esm::endstate_is_not_abstract():
    assert not inspect.isabstract(esm::EndState)


def test_esm::endstate_constructor_exists():
    assert callable(esm::EndState.__init__)


def test_esm::endstate_constructor_args():
    sig = inspect.signature(esm::EndState.__init__)
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
esm::Transition_strategy = st.builds(
    esm::Transition,
    action=
        safe_text
)
esm::State_strategy = st.builds(
    esm::State,
    name=
        safe_text
)
esm::Machine_strategy = st.builds(
    esm::Machine,
)
esm::EObject_strategy = st.builds(
    esm::EObject,
)
State_strategy = st.builds(
    State,
)
esm::EndState_strategy = st.builds(
    esm::EndState,
)

@given(instance=esm::Transition_strategy)
@settings(max_examples=50)
def test_esm::transition_instantiation(instance):
    assert isinstance(instance, esm::Transition)

@given(instance=esm::Transition_strategy)
def test_esm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=esm::Transition_strategy)
def test_esm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=esm::State_strategy)
@settings(max_examples=50)
def test_esm::state_instantiation(instance):
    assert isinstance(instance, esm::State)

@given(instance=esm::State_strategy)
def test_esm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esm::State_strategy)
def test_esm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esm::Machine_strategy)
@settings(max_examples=50)
def test_esm::machine_instantiation(instance):
    assert isinstance(instance, esm::Machine)

@given(instance=esm::EObject_strategy)
@settings(max_examples=50)
def test_esm::eobject_instantiation(instance):
    assert isinstance(instance, esm::EObject)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=esm::EndState_strategy)
@settings(max_examples=50)
def test_esm::endstate_instantiation(instance):
    assert isinstance(instance, esm::EndState)
