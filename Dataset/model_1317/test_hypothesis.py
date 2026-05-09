import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::Transition,
    stateMachine::Condition,
    stateMachine::State,
    stateMachine::Event,
    stateMachine::Variable,
    stateMachine::States,
    stateMachine::Events,
    stateMachine::Variables,
    stateMachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::condition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Condition)


def test_statemachine::condition_constructor_exists():
    assert callable(stateMachine::Condition.__init__)


def test_statemachine::condition_constructor_args():
    sig = inspect.signature(stateMachine::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_statemachine::condition_has_value():
    assert hasattr(stateMachine::Condition, "value")
    descriptor = None
    for klass in stateMachine::Condition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::condition_has_op():
    assert hasattr(stateMachine::Condition, "op")
    descriptor = None
    for klass in stateMachine::Condition.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(stateMachine::State, "name")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(stateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(stateMachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::event_has_name():
    assert hasattr(stateMachine::Event, "name")
    descriptor = None
    for klass in stateMachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::variable_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Variable)


def test_statemachine::variable_constructor_exists():
    assert callable(stateMachine::Variable.__init__)


def test_statemachine::variable_constructor_args():
    sig = inspect.signature(stateMachine::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::variable_has_name():
    assert hasattr(stateMachine::Variable, "name")
    descriptor = None
    for klass in stateMachine::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::states_is_not_abstract():
    assert not inspect.isabstract(stateMachine::States)


def test_statemachine::states_constructor_exists():
    assert callable(stateMachine::States.__init__)


def test_statemachine::states_constructor_args():
    sig = inspect.signature(stateMachine::States.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::events_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Events)


def test_statemachine::events_constructor_exists():
    assert callable(stateMachine::Events.__init__)


def test_statemachine::events_constructor_args():
    sig = inspect.signature(stateMachine::Events.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::variables_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Variables)


def test_statemachine::variables_constructor_exists():
    assert callable(stateMachine::Variables.__init__)


def test_statemachine::variables_constructor_args():
    sig = inspect.signature(stateMachine::Variables.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
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
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
)
stateMachine::Condition_strategy = st.builds(
    stateMachine::Condition,
    value=
        st.integers(),
    op=
        safe_text
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    name=
        safe_text
)
stateMachine::Event_strategy = st.builds(
    stateMachine::Event,
    name=
        safe_text
)
stateMachine::Variable_strategy = st.builds(
    stateMachine::Variable,
    name=
        safe_text
)
stateMachine::States_strategy = st.builds(
    stateMachine::States,
)
stateMachine::Events_strategy = st.builds(
    stateMachine::Events,
)
stateMachine::Variables_strategy = st.builds(
    stateMachine::Variables,
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    name=
        safe_text
)

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)

@given(instance=stateMachine::Condition_strategy)
@settings(max_examples=50)
def test_statemachine::condition_instantiation(instance):
    assert isinstance(instance, stateMachine::Condition)

@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, stateMachine::Event)

@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Variable_strategy)
@settings(max_examples=50)
def test_statemachine::variable_instantiation(instance):
    assert isinstance(instance, stateMachine::Variable)

@given(instance=stateMachine::Variable_strategy)
def test_statemachine::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Variable_strategy)
def test_statemachine::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::States_strategy)
@settings(max_examples=50)
def test_statemachine::states_instantiation(instance):
    assert isinstance(instance, stateMachine::States)

@given(instance=stateMachine::Events_strategy)
@settings(max_examples=50)
def test_statemachine::events_instantiation(instance):
    assert isinstance(instance, stateMachine::Events)

@given(instance=stateMachine::Variables_strategy)
@settings(max_examples=50)
def test_statemachine::variables_instantiation(instance):
    assert isinstance(instance, stateMachine::Variables)

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
