import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsml_FSMTransition,
    fsml_FSMState,
    fsml_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsml_fsmtransition_is_not_abstract():
    assert not inspect.isabstract(fsml_FSMTransition)


def test_fsml_fsmtransition_constructor_exists():
    assert callable(fsml_FSMTransition.__init__)


def test_fsml_fsmtransition_constructor_args():
    sig = inspect.signature(fsml_FSMTransition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "action" in params, "Missing parameter 'action'"

def test_fsml_fsmtransition_has_input():
    assert hasattr(fsml_FSMTransition, "input")
    descriptor = None
    for klass in fsml_FSMTransition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_fsml_fsmtransition_has_action():
    assert hasattr(fsml_FSMTransition, "action")
    descriptor = None
    for klass in fsml_FSMTransition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_fsml_fsmstate_is_not_abstract():
    assert not inspect.isabstract(fsml_FSMState)


def test_fsml_fsmstate_constructor_exists():
    assert callable(fsml_FSMState.__init__)


def test_fsml_fsmstate_constructor_args():
    sig = inspect.signature(fsml_FSMState.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsml_fsmstate_has_initial():
    assert hasattr(fsml_FSMState, "initial")
    descriptor = None
    for klass in fsml_FSMState.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_fsml_fsmstate_has_name():
    assert hasattr(fsml_FSMState, "name")
    descriptor = None
    for klass in fsml_FSMState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsml_fsm_is_not_abstract():
    assert not inspect.isabstract(fsml_FSM)


def test_fsml_fsm_constructor_exists():
    assert callable(fsml_FSM.__init__)


def test_fsml_fsm_constructor_args():
    sig = inspect.signature(fsml_FSM.__init__)
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
fsml_FSMTransition_strategy = st.builds(
    fsml_FSMTransition,
    input=
        safe_text,
    action=
        safe_text
)
fsml_FSMState_strategy = st.builds(
    fsml_FSMState,
    initial=
        st.booleans(),
    name=
        safe_text
)
fsml_FSM_strategy = st.builds(
    fsml_FSM,
)

@given(instance=fsml_FSMTransition_strategy)
@settings(max_examples=50)
def test_fsml_fsmtransition_instantiation(instance):
    assert isinstance(instance, fsml_FSMTransition)



@given(instance=fsml_FSMTransition_strategy)
def test_fsml_fsmtransition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=fsml_FSMTransition_strategy)
def test_fsml_fsmtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=fsml_FSMState_strategy)
@settings(max_examples=50)
def test_fsml_fsmstate_instantiation(instance):
    assert isinstance(instance, fsml_FSMState)



@given(instance=fsml_FSMState_strategy)
def test_fsml_fsmstate_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=fsml_FSMState_strategy)
def test_fsml_fsmstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsml_FSM_strategy)
@settings(max_examples=50)
def test_fsml_fsm_instantiation(instance):
    assert isinstance(instance, fsml_FSM)
