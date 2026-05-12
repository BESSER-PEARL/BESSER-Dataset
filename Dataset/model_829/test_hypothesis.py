import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lts_av_PerJoinPointScope,
    lts_av_GlobalScope,
    lts_av_EObject,
    lts_av_Advice,
    lts_av_State,
    lts_av_LTS,
    lts_av_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts_av_perjoinpointscope_is_not_abstract():
    assert not inspect.isabstract(lts_av_PerJoinPointScope)


def test_lts_av_perjoinpointscope_constructor_exists():
    assert callable(lts_av_PerJoinPointScope.__init__)


def test_lts_av_perjoinpointscope_constructor_args():
    sig = inspect.signature(lts_av_PerJoinPointScope.__init__)
    params = list(sig.parameters.keys())



def test_lts_av_globalscope_is_not_abstract():
    assert not inspect.isabstract(lts_av_GlobalScope)


def test_lts_av_globalscope_constructor_exists():
    assert callable(lts_av_GlobalScope.__init__)


def test_lts_av_globalscope_constructor_args():
    sig = inspect.signature(lts_av_GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_lts_av_eobject_is_not_abstract():
    assert not inspect.isabstract(lts_av_EObject)


def test_lts_av_eobject_constructor_exists():
    assert callable(lts_av_EObject.__init__)


def test_lts_av_eobject_constructor_args():
    sig = inspect.signature(lts_av_EObject.__init__)
    params = list(sig.parameters.keys())



def test_lts_av_advice_is_not_abstract():
    assert not inspect.isabstract(lts_av_Advice)


def test_lts_av_advice_constructor_exists():
    assert callable(lts_av_Advice.__init__)


def test_lts_av_advice_constructor_args():
    sig = inspect.signature(lts_av_Advice.__init__)
    params = list(sig.parameters.keys())



def test_lts_av_state_is_not_abstract():
    assert not inspect.isabstract(lts_av_State)


def test_lts_av_state_constructor_exists():
    assert callable(lts_av_State.__init__)


def test_lts_av_state_constructor_args():
    sig = inspect.signature(lts_av_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_av_state_has_name():
    assert hasattr(lts_av_State, "name")
    descriptor = None
    for klass in lts_av_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts_av_lts_is_not_abstract():
    assert not inspect.isabstract(lts_av_LTS)


def test_lts_av_lts_constructor_exists():
    assert callable(lts_av_LTS.__init__)


def test_lts_av_lts_constructor_args():
    sig = inspect.signature(lts_av_LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_av_lts_has_name():
    assert hasattr(lts_av_LTS, "name")
    descriptor = None
    for klass in lts_av_LTS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts_av_transition_is_not_abstract():
    assert not inspect.isabstract(lts_av_Transition)


def test_lts_av_transition_constructor_exists():
    assert callable(lts_av_Transition.__init__)


def test_lts_av_transition_constructor_args():
    sig = inspect.signature(lts_av_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_lts_av_transition_has_input():
    assert hasattr(lts_av_Transition, "input")
    descriptor = None
    for klass in lts_av_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_lts_av_transition_has_output():
    assert hasattr(lts_av_Transition, "output")
    descriptor = None
    for klass in lts_av_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
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
lts_av_PerJoinPointScope_strategy = st.builds(
    lts_av_PerJoinPointScope,
)
lts_av_GlobalScope_strategy = st.builds(
    lts_av_GlobalScope,
)
lts_av_EObject_strategy = st.builds(
    lts_av_EObject,
)
lts_av_Advice_strategy = st.builds(
    lts_av_Advice,
)
lts_av_State_strategy = st.builds(
    lts_av_State,
    name=
        safe_text
)
lts_av_LTS_strategy = st.builds(
    lts_av_LTS,
    name=
        safe_text
)
lts_av_Transition_strategy = st.builds(
    lts_av_Transition,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=lts_av_PerJoinPointScope_strategy)
@settings(max_examples=50)
def test_lts_av_perjoinpointscope_instantiation(instance):
    assert isinstance(instance, lts_av_PerJoinPointScope)

@given(instance=lts_av_GlobalScope_strategy)
@settings(max_examples=50)
def test_lts_av_globalscope_instantiation(instance):
    assert isinstance(instance, lts_av_GlobalScope)

@given(instance=lts_av_EObject_strategy)
@settings(max_examples=50)
def test_lts_av_eobject_instantiation(instance):
    assert isinstance(instance, lts_av_EObject)

@given(instance=lts_av_Advice_strategy)
@settings(max_examples=50)
def test_lts_av_advice_instantiation(instance):
    assert isinstance(instance, lts_av_Advice)

@given(instance=lts_av_State_strategy)
@settings(max_examples=50)
def test_lts_av_state_instantiation(instance):
    assert isinstance(instance, lts_av_State)



@given(instance=lts_av_State_strategy)
def test_lts_av_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts_av_LTS_strategy)
@settings(max_examples=50)
def test_lts_av_lts_instantiation(instance):
    assert isinstance(instance, lts_av_LTS)



@given(instance=lts_av_LTS_strategy)
def test_lts_av_lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts_av_Transition_strategy)
@settings(max_examples=50)
def test_lts_av_transition_instantiation(instance):
    assert isinstance(instance, lts_av_Transition)



@given(instance=lts_av_Transition_strategy)
def test_lts_av_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=lts_av_Transition_strategy)
def test_lts_av_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
