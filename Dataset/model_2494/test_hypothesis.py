import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basicFsmEnv::Machine,
    State,
    basicFsmEnv::InitialState,
    basicFsmEnv::Action,
    basicFsmEnv::Guard,
    basicFsmEnv::VarDecl,
    basicFsmEnv::Trans,
    basicFsmEnv::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicfsmenv::machine_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::Machine)


def test_basicfsmenv::machine_constructor_exists():
    assert callable(basicFsmEnv::Machine.__init__)


def test_basicfsmenv::machine_constructor_args():
    sig = inspect.signature(basicFsmEnv::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsmenv::machine_has_name():
    assert hasattr(basicFsmEnv::Machine, "name")
    descriptor = None
    for klass in basicFsmEnv::Machine.__mro__:
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



def test_basicfsmenv::initialstate_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::InitialState)


def test_basicfsmenv::initialstate_constructor_exists():
    assert callable(basicFsmEnv::InitialState.__init__)


def test_basicfsmenv::initialstate_constructor_args():
    sig = inspect.signature(basicFsmEnv::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv::action_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::Action)


def test_basicfsmenv::action_constructor_exists():
    assert callable(basicFsmEnv::Action.__init__)


def test_basicfsmenv::action_constructor_args():
    sig = inspect.signature(basicFsmEnv::Action.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv::guard_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::Guard)


def test_basicfsmenv::guard_constructor_exists():
    assert callable(basicFsmEnv::Guard.__init__)


def test_basicfsmenv::guard_constructor_args():
    sig = inspect.signature(basicFsmEnv::Guard.__init__)
    params = list(sig.parameters.keys())



def test_basicfsmenv::vardecl_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::VarDecl)


def test_basicfsmenv::vardecl_constructor_exists():
    assert callable(basicFsmEnv::VarDecl.__init__)


def test_basicfsmenv::vardecl_constructor_args():
    sig = inspect.signature(basicFsmEnv::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_basicfsmenv::vardecl_has_name():
    assert hasattr(basicFsmEnv::VarDecl, "name")
    descriptor = None
    for klass in basicFsmEnv::VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_basicfsmenv::vardecl_has_value():
    assert hasattr(basicFsmEnv::VarDecl, "value")
    descriptor = None
    for klass in basicFsmEnv::VarDecl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basicfsmenv::trans_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::Trans)


def test_basicfsmenv::trans_constructor_exists():
    assert callable(basicFsmEnv::Trans.__init__)


def test_basicfsmenv::trans_constructor_args():
    sig = inspect.signature(basicFsmEnv::Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_basicfsmenv::trans_has_event():
    assert hasattr(basicFsmEnv::Trans, "event")
    descriptor = None
    for klass in basicFsmEnv::Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_basicfsmenv::state_is_not_abstract():
    assert not inspect.isabstract(basicFsmEnv::State)


def test_basicfsmenv::state_constructor_exists():
    assert callable(basicFsmEnv::State.__init__)


def test_basicfsmenv::state_constructor_args():
    sig = inspect.signature(basicFsmEnv::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsmenv::state_has_name():
    assert hasattr(basicFsmEnv::State, "name")
    descriptor = None
    for klass in basicFsmEnv::State.__mro__:
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
basicFsmEnv::Machine_strategy = st.builds(
    basicFsmEnv::Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
basicFsmEnv::InitialState_strategy = st.builds(
    basicFsmEnv::InitialState,
)
basicFsmEnv::Action_strategy = st.builds(
    basicFsmEnv::Action,
)
basicFsmEnv::Guard_strategy = st.builds(
    basicFsmEnv::Guard,
)
basicFsmEnv::VarDecl_strategy = st.builds(
    basicFsmEnv::VarDecl,
    name=
        safe_text,
    value=
        safe_text
)
basicFsmEnv::Trans_strategy = st.builds(
    basicFsmEnv::Trans,
    event=
        safe_text
)
basicFsmEnv::State_strategy = st.builds(
    basicFsmEnv::State,
    name=
        safe_text
)

@given(instance=basicFsmEnv::Machine_strategy)
@settings(max_examples=50)
def test_basicfsmenv::machine_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::Machine)

@given(instance=basicFsmEnv::Machine_strategy)
def test_basicfsmenv::machine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicFsmEnv::Machine_strategy)
def test_basicfsmenv::machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=basicFsmEnv::InitialState_strategy)
@settings(max_examples=50)
def test_basicfsmenv::initialstate_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::InitialState)

@given(instance=basicFsmEnv::Action_strategy)
@settings(max_examples=50)
def test_basicfsmenv::action_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::Action)

@given(instance=basicFsmEnv::Guard_strategy)
@settings(max_examples=50)
def test_basicfsmenv::guard_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::Guard)

@given(instance=basicFsmEnv::VarDecl_strategy)
@settings(max_examples=50)
def test_basicfsmenv::vardecl_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::VarDecl)

@given(instance=basicFsmEnv::VarDecl_strategy)
def test_basicfsmenv::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicFsmEnv::VarDecl_strategy)
def test_basicfsmenv::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicFsmEnv::VarDecl_strategy)
def test_basicfsmenv::vardecl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=basicFsmEnv::VarDecl_strategy)
def test_basicfsmenv::vardecl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=basicFsmEnv::Trans_strategy)
@settings(max_examples=50)
def test_basicfsmenv::trans_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::Trans)

@given(instance=basicFsmEnv::Trans_strategy)
def test_basicfsmenv::trans_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=basicFsmEnv::Trans_strategy)
def test_basicfsmenv::trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=basicFsmEnv::State_strategy)
@settings(max_examples=50)
def test_basicfsmenv::state_instantiation(instance):
    assert isinstance(instance, basicFsmEnv::State)

@given(instance=basicFsmEnv::State_strategy)
def test_basicfsmenv::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicFsmEnv::State_strategy)
def test_basicfsmenv::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
