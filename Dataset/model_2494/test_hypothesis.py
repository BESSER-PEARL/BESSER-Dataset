import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basicFsmEnv_Machine,
    State,
    basicFsmEnv_InitialState,
    basicFsmEnv_Action,
    basicFsmEnv_Guard,
    basicFsmEnv_VarDecl,
    basicFsmEnv_Trans,
    basicFsmEnv_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicfsmenv_machine_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_Machine)


def test_basicfsmenv_machine_constructor_exists():
    assert callable(basicFsmEnv_Machine.__init__)


def test_basicfsmenv_machine_constructor_args():
    sig = inspect.signature(basicFsmEnv_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsmenv_machine_has_name():
    assert hasattr(basicFsmEnv_Machine, "name")
    descriptor = None
    for klass in basicFsmEnv_Machine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv_initialstate_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_InitialState)


def test_basicfsmenv_initialstate_constructor_exists():
    assert callable(basicFsmEnv_InitialState.__init__)


def test_basicfsmenv_initialstate_constructor_args():
    sig = inspect.signature(basicFsmEnv_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv_action_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_Action)


def test_basicfsmenv_action_constructor_exists():
    assert callable(basicFsmEnv_Action.__init__)


def test_basicfsmenv_action_constructor_args():
    sig = inspect.signature(basicFsmEnv_Action.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv_guard_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_Guard)


def test_basicfsmenv_guard_constructor_exists():
    assert callable(basicFsmEnv_Guard.__init__)


def test_basicfsmenv_guard_constructor_args():
    sig = inspect.signature(basicFsmEnv_Guard.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv_vardecl_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_VarDecl)


def test_basicfsmenv_vardecl_constructor_exists():
    assert callable(basicFsmEnv_VarDecl.__init__)


def test_basicfsmenv_vardecl_constructor_args():
    sig = inspect.signature(basicFsmEnv_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsmenv_vardecl_has_value():
    assert hasattr(basicFsmEnv_VarDecl, "value")
    descriptor = None
    for klass in basicFsmEnv_VarDecl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_basicfsmenv_vardecl_has_name():
    assert hasattr(basicFsmEnv_VarDecl, "name")
    descriptor = None
    for klass in basicFsmEnv_VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basicfsmenv_trans_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_Trans)


def test_basicfsmenv_trans_constructor_exists():
    assert callable(basicFsmEnv_Trans.__init__)


def test_basicfsmenv_trans_constructor_args():
    sig = inspect.signature(basicFsmEnv_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_basicfsmenv_trans_has_event():
    assert hasattr(basicFsmEnv_Trans, "event")
    descriptor = None
    for klass in basicFsmEnv_Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_basicfsmenv_state_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv_State)


def test_basicfsmenv_state_constructor_exists():
    assert callable(basicFsmEnv_State.__init__)


def test_basicfsmenv_state_constructor_args():
    sig = inspect.signature(basicFsmEnv_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsmenv_state_has_name():
    assert hasattr(basicFsmEnv_State, "name")
    descriptor = None
    for klass in basicFsmEnv_State.__mro__:
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
basicFsmEnv_Machine_strategy = st.builds(
    basicFsmEnv_Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
basicFsmEnv_InitialState_strategy = st.builds(
    basicFsmEnv_InitialState,
)
basicFsmEnv_Action_strategy = st.builds(
    basicFsmEnv_Action,
)
basicFsmEnv_Guard_strategy = st.builds(
    basicFsmEnv_Guard,
)
basicFsmEnv_VarDecl_strategy = st.builds(
    basicFsmEnv_VarDecl,
    value=
        safe_text,
    name=
        safe_text
)
basicFsmEnv_Trans_strategy = st.builds(
    basicFsmEnv_Trans,
    event=
        safe_text
)
basicFsmEnv_State_strategy = st.builds(
    basicFsmEnv_State,
    name=
        safe_text
)

@given(instance=basicFsmEnv_Machine_strategy)
@settings(max_examples=50)
def test_basicfsmenv_machine_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_Machine)



@given(instance=basicFsmEnv_Machine_strategy)
def test_basicfsmenv_machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=basicFsmEnv_InitialState_strategy)
@settings(max_examples=50)
def test_basicfsmenv_initialstate_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_InitialState)

@given(instance=basicFsmEnv_Action_strategy)
@settings(max_examples=50)
def test_basicfsmenv_action_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_Action)

@given(instance=basicFsmEnv_Guard_strategy)
@settings(max_examples=50)
def test_basicfsmenv_guard_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_Guard)

@given(instance=basicFsmEnv_VarDecl_strategy)
@settings(max_examples=50)
def test_basicfsmenv_vardecl_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_VarDecl)



@given(instance=basicFsmEnv_VarDecl_strategy)
def test_basicfsmenv_vardecl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=basicFsmEnv_VarDecl_strategy)
def test_basicfsmenv_vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicFsmEnv_Trans_strategy)
@settings(max_examples=50)
def test_basicfsmenv_trans_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_Trans)



@given(instance=basicFsmEnv_Trans_strategy)
def test_basicfsmenv_trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=basicFsmEnv_State_strategy)
@settings(max_examples=50)
def test_basicfsmenv_state_instantiation(instance):
    assert isinstance(instance, basicFsmEnv_State)



@given(instance=basicFsmEnv_State_strategy)
def test_basicfsmenv_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
