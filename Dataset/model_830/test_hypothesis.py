import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lts_pc_EObject,
    lts_pc_Pointcut,
    lts_pc_Transition,
    lts_pc_State,
    lts_pc_LTS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts_pc_eobject_is_not_abstract():
    assert not inspect.isabstract(lts_pc_EObject)


def test_lts_pc_eobject_constructor_exists():
    assert callable(lts_pc_EObject.__init__)


def test_lts_pc_eobject_constructor_args():
    sig = inspect.signature(lts_pc_EObject.__init__)
    params = list(sig.parameters.keys())



def test_lts_pc_pointcut_is_not_abstract():
    assert not inspect.isabstract(lts_pc_Pointcut)


def test_lts_pc_pointcut_constructor_exists():
    assert callable(lts_pc_Pointcut.__init__)


def test_lts_pc_pointcut_constructor_args():
    sig = inspect.signature(lts_pc_Pointcut.__init__)
    params = list(sig.parameters.keys())



def test_lts_pc_transition_is_not_abstract():
    assert not inspect.isabstract(lts_pc_Transition)


def test_lts_pc_transition_constructor_exists():
    assert callable(lts_pc_Transition.__init__)


def test_lts_pc_transition_constructor_args():
    sig = inspect.signature(lts_pc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_lts_pc_transition_has_input():
    assert hasattr(lts_pc_Transition, "input")
    descriptor = None
    for klass in lts_pc_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_lts_pc_transition_has_output():
    assert hasattr(lts_pc_Transition, "output")
    descriptor = None
    for klass in lts_pc_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_lts_pc_state_is_not_abstract():
    assert not inspect.isabstract(lts_pc_State)


def test_lts_pc_state_constructor_exists():
    assert callable(lts_pc_State.__init__)


def test_lts_pc_state_constructor_args():
    sig = inspect.signature(lts_pc_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_pc_state_has_name():
    assert hasattr(lts_pc_State, "name")
    descriptor = None
    for klass in lts_pc_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts_pc_lts_is_not_abstract():
    assert not inspect.isabstract(lts_pc_LTS)


def test_lts_pc_lts_constructor_exists():
    assert callable(lts_pc_LTS.__init__)


def test_lts_pc_lts_constructor_args():
    sig = inspect.signature(lts_pc_LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_pc_lts_has_name():
    assert hasattr(lts_pc_LTS, "name")
    descriptor = None
    for klass in lts_pc_LTS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
lts_pc_EObject_strategy = st.builds(
    lts_pc_EObject,
)
lts_pc_Pointcut_strategy = st.builds(
    lts_pc_Pointcut,
)
lts_pc_Transition_strategy = st.builds(
    lts_pc_Transition,
    input=
        safe_text,
    output=
        safe_text
)
lts_pc_State_strategy = st.builds(
    lts_pc_State,
    name=
        safe_text
)
lts_pc_LTS_strategy = st.builds(
    lts_pc_LTS,
    name=
        safe_text
)

@given(instance=lts_pc_EObject_strategy)
@settings(max_examples=50)
def test_lts_pc_eobject_instantiation(instance):
    assert isinstance(instance, lts_pc_EObject)

@given(instance=lts_pc_Pointcut_strategy)
@settings(max_examples=50)
def test_lts_pc_pointcut_instantiation(instance):
    assert isinstance(instance, lts_pc_Pointcut)

@given(instance=lts_pc_Transition_strategy)
@settings(max_examples=50)
def test_lts_pc_transition_instantiation(instance):
    assert isinstance(instance, lts_pc_Transition)



@given(instance=lts_pc_Transition_strategy)
def test_lts_pc_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=lts_pc_Transition_strategy)
def test_lts_pc_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=lts_pc_State_strategy)
@settings(max_examples=50)
def test_lts_pc_state_instantiation(instance):
    assert isinstance(instance, lts_pc_State)



@given(instance=lts_pc_State_strategy)
def test_lts_pc_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts_pc_LTS_strategy)
@settings(max_examples=50)
def test_lts_pc_lts_instantiation(instance):
    assert isinstance(instance, lts_pc_LTS)



@given(instance=lts_pc_LTS_strategy)
def test_lts_pc_lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
