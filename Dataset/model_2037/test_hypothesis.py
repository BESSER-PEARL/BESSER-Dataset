import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stm::Transition,
    stm::SelfEvent,
    stm::Parameter,
    stm::GuardCall,
    stm::State,
    stm::Guard,
    stm::Command,
    stm::Event,
    stm::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stm::transition_is_not_abstract():
    assert not inspect.isabstract(stm::Transition)


def test_stm::transition_constructor_exists():
    assert callable(stm::Transition.__init__)


def test_stm::transition_constructor_args():
    sig = inspect.signature(stm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_stm::selfevent_is_not_abstract():
    assert not inspect.isabstract(stm::SelfEvent)


def test_stm::selfevent_constructor_exists():
    assert callable(stm::SelfEvent.__init__)


def test_stm::selfevent_constructor_args():
    sig = inspect.signature(stm::SelfEvent.__init__)
    params = list(sig.parameters.keys())



def test_stm::parameter_is_not_abstract():
    assert not inspect.isabstract(stm::Parameter)


def test_stm::parameter_constructor_exists():
    assert callable(stm::Parameter.__init__)


def test_stm::parameter_constructor_args():
    sig = inspect.signature(stm::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_stm::parameter_has_type():
    assert hasattr(stm::Parameter, "type")
    descriptor = None
    for klass in stm::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stm::parameter_has_name():
    assert hasattr(stm::Parameter, "name")
    descriptor = None
    for klass in stm::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm::guardcall_is_not_abstract():
    assert not inspect.isabstract(stm::GuardCall)


def test_stm::guardcall_constructor_exists():
    assert callable(stm::GuardCall.__init__)


def test_stm::guardcall_constructor_args():
    sig = inspect.signature(stm::GuardCall.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_stm::guardcall_has_parameters():
    assert hasattr(stm::GuardCall, "parameters")
    descriptor = None
    for klass in stm::GuardCall.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_stm::state_is_not_abstract():
    assert not inspect.isabstract(stm::State)


def test_stm::state_constructor_exists():
    assert callable(stm::State.__init__)


def test_stm::state_constructor_args():
    sig = inspect.signature(stm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm::state_has_name():
    assert hasattr(stm::State, "name")
    descriptor = None
    for klass in stm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm::guard_is_not_abstract():
    assert not inspect.isabstract(stm::Guard)


def test_stm::guard_constructor_exists():
    assert callable(stm::Guard.__init__)


def test_stm::guard_constructor_args():
    sig = inspect.signature(stm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm::guard_has_name():
    assert hasattr(stm::Guard, "name")
    descriptor = None
    for klass in stm::Guard.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm::command_is_not_abstract():
    assert not inspect.isabstract(stm::Command)


def test_stm::command_constructor_exists():
    assert callable(stm::Command.__init__)


def test_stm::command_constructor_args():
    sig = inspect.signature(stm::Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm::command_has_name():
    assert hasattr(stm::Command, "name")
    descriptor = None
    for klass in stm::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm::event_is_not_abstract():
    assert not inspect.isabstract(stm::Event)


def test_stm::event_constructor_exists():
    assert callable(stm::Event.__init__)


def test_stm::event_constructor_args():
    sig = inspect.signature(stm::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm::event_has_name():
    assert hasattr(stm::Event, "name")
    descriptor = None
    for klass in stm::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm::statemachine_is_not_abstract():
    assert not inspect.isabstract(stm::Statemachine)


def test_stm::statemachine_constructor_exists():
    assert callable(stm::Statemachine.__init__)


def test_stm::statemachine_constructor_args():
    sig = inspect.signature(stm::Statemachine.__init__)
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
stm::Transition_strategy = st.builds(
    stm::Transition,
)
stm::SelfEvent_strategy = st.builds(
    stm::SelfEvent,
)
stm::Parameter_strategy = st.builds(
    stm::Parameter,
    type=
        safe_text,
    name=
        safe_text
)
stm::GuardCall_strategy = st.builds(
    stm::GuardCall,
    parameters=
        safe_text
)
stm::State_strategy = st.builds(
    stm::State,
    name=
        safe_text
)
stm::Guard_strategy = st.builds(
    stm::Guard,
    name=
        safe_text
)
stm::Command_strategy = st.builds(
    stm::Command,
    name=
        safe_text
)
stm::Event_strategy = st.builds(
    stm::Event,
    name=
        safe_text
)
stm::Statemachine_strategy = st.builds(
    stm::Statemachine,
)

@given(instance=stm::Transition_strategy)
@settings(max_examples=50)
def test_stm::transition_instantiation(instance):
    assert isinstance(instance, stm::Transition)

@given(instance=stm::SelfEvent_strategy)
@settings(max_examples=50)
def test_stm::selfevent_instantiation(instance):
    assert isinstance(instance, stm::SelfEvent)

@given(instance=stm::Parameter_strategy)
@settings(max_examples=50)
def test_stm::parameter_instantiation(instance):
    assert isinstance(instance, stm::Parameter)

@given(instance=stm::Parameter_strategy)
def test_stm::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stm::Parameter_strategy)
def test_stm::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stm::Parameter_strategy)
def test_stm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stm::Parameter_strategy)
def test_stm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm::GuardCall_strategy)
@settings(max_examples=50)
def test_stm::guardcall_instantiation(instance):
    assert isinstance(instance, stm::GuardCall)

@given(instance=stm::GuardCall_strategy)
def test_stm::guardcall_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=stm::GuardCall_strategy)
def test_stm::guardcall_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=stm::State_strategy)
@settings(max_examples=50)
def test_stm::state_instantiation(instance):
    assert isinstance(instance, stm::State)

@given(instance=stm::State_strategy)
def test_stm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stm::State_strategy)
def test_stm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm::Guard_strategy)
@settings(max_examples=50)
def test_stm::guard_instantiation(instance):
    assert isinstance(instance, stm::Guard)

@given(instance=stm::Guard_strategy)
def test_stm::guard_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stm::Guard_strategy)
def test_stm::guard_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm::Command_strategy)
@settings(max_examples=50)
def test_stm::command_instantiation(instance):
    assert isinstance(instance, stm::Command)

@given(instance=stm::Command_strategy)
def test_stm::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stm::Command_strategy)
def test_stm::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm::Event_strategy)
@settings(max_examples=50)
def test_stm::event_instantiation(instance):
    assert isinstance(instance, stm::Event)

@given(instance=stm::Event_strategy)
def test_stm::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stm::Event_strategy)
def test_stm::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm::Statemachine_strategy)
@settings(max_examples=50)
def test_stm::statemachine_instantiation(instance):
    assert isinstance(instance, stm::Statemachine)
