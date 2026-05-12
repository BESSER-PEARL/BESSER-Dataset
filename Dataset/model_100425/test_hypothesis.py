import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statecharts::Event,
    BooleanExpression,
    Statecharts::Guard,
    CompositeState,
    Statecharts::StateVertex,
    Guard,
    Statecharts::Transition,
    Event,
    StateMachine,
    StateVertex,
    Statecharts::State,
    State,
    Statecharts::CompositeState,
    Transition,
    Statecharts::StateMachine,
    Statecharts::BooleanExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statecharts::event_is_not_abstract():
    assert not inspect.isabstract(Statecharts::Event)


def test_statecharts::event_constructor_exists():
    assert callable(Statecharts::Event.__init__)


def test_statecharts::event_constructor_args():
    sig = inspect.signature(Statecharts::Event.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::guard_is_not_abstract():
    assert not inspect.isabstract(Statecharts::Guard)


def test_statecharts::guard_constructor_exists():
    assert callable(Statecharts::Guard.__init__)


def test_statecharts::guard_constructor_args():
    sig = inspect.signature(Statecharts::Guard.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::statevertex_is_not_abstract():
    assert not inspect.isabstract(Statecharts::StateVertex)


def test_statecharts::statevertex_constructor_exists():
    assert callable(Statecharts::StateVertex.__init__)


def test_statecharts::statevertex_constructor_args():
    sig = inspect.signature(Statecharts::StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::transition_is_not_abstract():
    assert not inspect.isabstract(Statecharts::Transition)


def test_statecharts::transition_constructor_exists():
    assert callable(Statecharts::Transition.__init__)


def test_statecharts::transition_constructor_args():
    sig = inspect.signature(Statecharts::Transition.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::state_is_not_abstract():
    assert not inspect.isabstract(Statecharts::State)


def test_statecharts::state_constructor_exists():
    assert callable(Statecharts::State.__init__)


def test_statecharts::state_constructor_args():
    sig = inspect.signature(Statecharts::State.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::compositestate_is_not_abstract():
    assert not inspect.isabstract(Statecharts::CompositeState)


def test_statecharts::compositestate_constructor_exists():
    assert callable(Statecharts::CompositeState.__init__)


def test_statecharts::compositestate_constructor_args():
    sig = inspect.signature(Statecharts::CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_statecharts::compositestate_has_isConcurrent():
    assert hasattr(Statecharts::CompositeState, "isConcurrent")
    descriptor = None
    for klass in Statecharts::CompositeState.__mro__:
        if "isConcurrent" in klass.__dict__:
            descriptor = klass.__dict__["isConcurrent"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::statemachine_is_not_abstract():
    assert not inspect.isabstract(Statecharts::StateMachine)


def test_statecharts::statemachine_constructor_exists():
    assert callable(Statecharts::StateMachine.__init__)


def test_statecharts::statemachine_constructor_args():
    sig = inspect.signature(Statecharts::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statecharts::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(Statecharts::BooleanExpression)


def test_statecharts::booleanexpression_constructor_exists():
    assert callable(Statecharts::BooleanExpression.__init__)


def test_statecharts::booleanexpression_constructor_args():
    sig = inspect.signature(Statecharts::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statecharts::booleanexpression_has_value():
    assert hasattr(Statecharts::BooleanExpression, "value")
    descriptor = None
    for klass in Statecharts::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
Statecharts::Event_strategy = st.builds(
    Statecharts::Event,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
Statecharts::Guard_strategy = st.builds(
    Statecharts::Guard,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
Statecharts::StateVertex_strategy = st.builds(
    Statecharts::StateVertex,
)
Guard_strategy = st.builds(
    Guard,
)
Statecharts::Transition_strategy = st.builds(
    Statecharts::Transition,
)
Event_strategy = st.builds(
    Event,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
Statecharts::State_strategy = st.builds(
    Statecharts::State,
)
State_strategy = st.builds(
    State,
)
Statecharts::CompositeState_strategy = st.builds(
    Statecharts::CompositeState,
    isConcurrent=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Statecharts::StateMachine_strategy = st.builds(
    Statecharts::StateMachine,
)
Statecharts::BooleanExpression_strategy = st.builds(
    Statecharts::BooleanExpression,
    value=
        safe_text
)

@given(instance=Statecharts::Event_strategy)
@settings(max_examples=50)
def test_statecharts::event_instantiation(instance):
    assert isinstance(instance, Statecharts::Event)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=Statecharts::Guard_strategy)
@settings(max_examples=50)
def test_statecharts::guard_instantiation(instance):
    assert isinstance(instance, Statecharts::Guard)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=Statecharts::StateVertex_strategy)
@settings(max_examples=50)
def test_statecharts::statevertex_instantiation(instance):
    assert isinstance(instance, Statecharts::StateVertex)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=Statecharts::Transition_strategy)
@settings(max_examples=50)
def test_statecharts::transition_instantiation(instance):
    assert isinstance(instance, Statecharts::Transition)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=Statecharts::State_strategy)
@settings(max_examples=50)
def test_statecharts::state_instantiation(instance):
    assert isinstance(instance, Statecharts::State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Statecharts::CompositeState_strategy)
@settings(max_examples=50)
def test_statecharts::compositestate_instantiation(instance):
    assert isinstance(instance, Statecharts::CompositeState)

@given(instance=Statecharts::CompositeState_strategy)
def test_statecharts::compositestate_isConcurrent_type(instance):
    assert isinstance(instance.isConcurrent, str)


@given(instance=Statecharts::CompositeState_strategy)
def test_statecharts::compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Statecharts::StateMachine_strategy)
@settings(max_examples=50)
def test_statecharts::statemachine_instantiation(instance):
    assert isinstance(instance, Statecharts::StateMachine)

@given(instance=Statecharts::BooleanExpression_strategy)
@settings(max_examples=50)
def test_statecharts::booleanexpression_instantiation(instance):
    assert isinstance(instance, Statecharts::BooleanExpression)

@given(instance=Statecharts::BooleanExpression_strategy)
def test_statecharts::booleanexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Statecharts::BooleanExpression_strategy)
def test_statecharts::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
