import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsml::FSMState,
    fsml::FSM,
    fsml::FSMTransition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsml::fsmstate_is_not_abstract():
    assert not inspect.isabstract(fsml::FSMState)


def test_fsml::fsmstate_constructor_exists():
    assert callable(fsml::FSMState.__init__)


def test_fsml::fsmstate_constructor_args():
    sig = inspect.signature(fsml::FSMState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_fsml::fsmstate_has_name():
    assert hasattr(fsml::FSMState, "name")
    descriptor = None
    for klass in fsml::FSMState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsml::fsmstate_has_initial():
    assert hasattr(fsml::FSMState, "initial")
    descriptor = None
    for klass in fsml::FSMState.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_fsml::fsm_is_not_abstract():
    assert not inspect.isabstract(fsml::FSM)


def test_fsml::fsm_constructor_exists():
    assert callable(fsml::FSM.__init__)


def test_fsml::fsm_constructor_args():
    sig = inspect.signature(fsml::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsml::fsmtransition_is_not_abstract():
    assert not inspect.isabstract(fsml::FSMTransition)


def test_fsml::fsmtransition_constructor_exists():
    assert callable(fsml::FSMTransition.__init__)


def test_fsml::fsmtransition_constructor_args():
    sig = inspect.signature(fsml::FSMTransition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsml::fsmtransition_has_action():
    assert hasattr(fsml::FSMTransition, "action")
    descriptor = None
    for klass in fsml::FSMTransition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_fsml::fsmtransition_has_input():
    assert hasattr(fsml::FSMTransition, "input")
    descriptor = None
    for klass in fsml::FSMTransition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)


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
fsml::FSMState_strategy = st.builds(
    fsml::FSMState,
    name=
        safe_text,
    initial=
        st.booleans()
)
fsml::FSM_strategy = st.builds(
    fsml::FSM,
)
fsml::FSMTransition_strategy = st.builds(
    fsml::FSMTransition,
    action=
        safe_text,
    input=
        safe_text
)

@given(instance=fsml::FSMState_strategy)
@settings(max_examples=50)
def test_fsml::fsmstate_instantiation(instance):
    assert isinstance(instance, fsml::FSMState)

@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=fsml::FSM_strategy)
@settings(max_examples=50)
def test_fsml::fsm_instantiation(instance):
    assert isinstance(instance, fsml::FSM)

@given(instance=fsml::FSMTransition_strategy)
@settings(max_examples=50)
def test_fsml::fsmtransition_instantiation(instance):
    assert isinstance(instance, fsml::FSMTransition)

@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original
