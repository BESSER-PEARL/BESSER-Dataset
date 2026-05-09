import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractState,
    efsm::AbstractState,
    efsm::ContextVariable,
    efsm::State,
    efsm::InitialState,
    efsm::Transition,
    efsm::EFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_efsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(efsm::AbstractState)


def test_efsm::abstractstate_constructor_exists():
    assert callable(efsm::AbstractState.__init__)


def test_efsm::abstractstate_constructor_args():
    sig = inspect.signature(efsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::abstractstate_has_name():
    assert hasattr(efsm::AbstractState, "name")
    descriptor = None
    for klass in efsm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm::contextvariable_is_not_abstract():
    assert not inspect.isabstract(efsm::ContextVariable)


def test_efsm::contextvariable_constructor_exists():
    assert callable(efsm::ContextVariable.__init__)


def test_efsm::contextvariable_constructor_args():
    sig = inspect.signature(efsm::ContextVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::contextvariable_has_type():
    assert hasattr(efsm::ContextVariable, "type")
    descriptor = None
    for klass in efsm::ContextVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_efsm::contextvariable_has_name():
    assert hasattr(efsm::ContextVariable, "name")
    descriptor = None
    for klass in efsm::ContextVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm::state_is_not_abstract():
    assert not inspect.isabstract(efsm::State)


def test_efsm::state_constructor_exists():
    assert callable(efsm::State.__init__)


def test_efsm::state_constructor_args():
    sig = inspect.signature(efsm::State.__init__)
    params = list(sig.parameters.keys())



def test_efsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(efsm::InitialState)


def test_efsm::initialstate_constructor_exists():
    assert callable(efsm::InitialState.__init__)


def test_efsm::initialstate_constructor_args():
    sig = inspect.signature(efsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_efsm::transition_is_not_abstract():
    assert not inspect.isabstract(efsm::Transition)


def test_efsm::transition_constructor_exists():
    assert callable(efsm::Transition.__init__)


def test_efsm::transition_constructor_args():
    sig = inspect.signature(efsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"
    assert "event" in params, "Missing parameter 'event'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::transition_has_input():
    assert hasattr(efsm::Transition, "input")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_output():
    assert hasattr(efsm::Transition, "output")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_event():
    assert hasattr(efsm::Transition, "event")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_guard():
    assert hasattr(efsm::Transition, "guard")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_action():
    assert hasattr(efsm::Transition, "action")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_name():
    assert hasattr(efsm::Transition, "name")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm::efsm_is_not_abstract():
    assert not inspect.isabstract(efsm::EFSM)


def test_efsm::efsm_constructor_exists():
    assert callable(efsm::EFSM.__init__)


def test_efsm::efsm_constructor_args():
    sig = inspect.signature(efsm::EFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::efsm_has_name():
    assert hasattr(efsm::EFSM, "name")
    descriptor = None
    for klass in efsm::EFSM.__mro__:
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
AbstractState_strategy = st.builds(
    AbstractState,
)
efsm::AbstractState_strategy = st.builds(
    efsm::AbstractState,
    name=
        safe_text
)
efsm::ContextVariable_strategy = st.builds(
    efsm::ContextVariable,
    type=
        safe_text,
    name=
        safe_text
)
efsm::State_strategy = st.builds(
    efsm::State,
)
efsm::InitialState_strategy = st.builds(
    efsm::InitialState,
)
efsm::Transition_strategy = st.builds(
    efsm::Transition,
    input=
        safe_text,
    output=
        safe_text,
    event=
        safe_text,
    guard=
        safe_text,
    action=
        safe_text,
    name=
        safe_text
)
efsm::EFSM_strategy = st.builds(
    efsm::EFSM,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=efsm::AbstractState_strategy)
@settings(max_examples=50)
def test_efsm::abstractstate_instantiation(instance):
    assert isinstance(instance, efsm::AbstractState)

@given(instance=efsm::AbstractState_strategy)
def test_efsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::AbstractState_strategy)
def test_efsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::ContextVariable_strategy)
@settings(max_examples=50)
def test_efsm::contextvariable_instantiation(instance):
    assert isinstance(instance, efsm::ContextVariable)

@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::State_strategy)
@settings(max_examples=50)
def test_efsm::state_instantiation(instance):
    assert isinstance(instance, efsm::State)

@given(instance=efsm::InitialState_strategy)
@settings(max_examples=50)
def test_efsm::initialstate_instantiation(instance):
    assert isinstance(instance, efsm::InitialState)

@given(instance=efsm::Transition_strategy)
@settings(max_examples=50)
def test_efsm::transition_instantiation(instance):
    assert isinstance(instance, efsm::Transition)

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::EFSM_strategy)
@settings(max_examples=50)
def test_efsm::efsm_instantiation(instance):
    assert isinstance(instance, efsm::EFSM)

@given(instance=efsm::EFSM_strategy)
def test_efsm::efsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::EFSM_strategy)
def test_efsm::efsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
