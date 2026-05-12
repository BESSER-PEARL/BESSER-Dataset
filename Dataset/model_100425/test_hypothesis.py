import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Statecharts_Event,
    BooleanExpression,
    Statecharts_Guard,
    CompositeState,
    Statecharts_StateVertex,
    Guard,
    Statecharts_Transition,
    Event,
    StateMachine,
    StateVertex,
    Statecharts_State,
    State,
    Statecharts_CompositeState,
    Transition,
    Statecharts_StateMachine,
    Statecharts_BooleanExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statecharts_event_is_not_abstract():
    assert not inspect.isabstract(Statecharts_Event)


def test_statecharts_event_constructor_exists():
    assert callable(Statecharts_Event.__init__)


def test_statecharts_event_constructor_args():
    sig = inspect.signature(Statecharts_Event.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_statecharts_guard_is_not_abstract():
    assert not inspect.isabstract(Statecharts_Guard)


def test_statecharts_guard_constructor_exists():
    assert callable(Statecharts_Guard.__init__)


def test_statecharts_guard_constructor_args():
    sig = inspect.signature(Statecharts_Guard.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statecharts_statevertex_is_not_abstract():
    assert not inspect.isabstract(Statecharts_StateVertex)


def test_statecharts_statevertex_constructor_exists():
    assert callable(Statecharts_StateVertex.__init__)


def test_statecharts_statevertex_constructor_args():
    sig = inspect.signature(Statecharts_StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_statecharts_transition_is_not_abstract():
    assert not inspect.isabstract(Statecharts_Transition)


def test_statecharts_transition_constructor_exists():
    assert callable(Statecharts_Transition.__init__)


def test_statecharts_transition_constructor_args():
    sig = inspect.signature(Statecharts_Transition.__init__)
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



def test_statecharts_state_is_not_abstract():
    assert not inspect.isabstract(Statecharts_State)


def test_statecharts_state_constructor_exists():
    assert callable(Statecharts_State.__init__)


def test_statecharts_state_constructor_args():
    sig = inspect.signature(Statecharts_State.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statecharts_compositestate_is_not_abstract():
    assert not inspect.isabstract(Statecharts_CompositeState)


def test_statecharts_compositestate_constructor_exists():
    assert callable(Statecharts_CompositeState.__init__)


def test_statecharts_compositestate_constructor_args():
    sig = inspect.signature(Statecharts_CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_statecharts_compositestate_has_isConcurrent():
    assert hasattr(Statecharts_CompositeState, "isConcurrent")
    descriptor = None
    for klass in Statecharts_CompositeState.__mro__:
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



def test_statecharts_statemachine_is_not_abstract():
    assert not inspect.isabstract(Statecharts_StateMachine)


def test_statecharts_statemachine_constructor_exists():
    assert callable(Statecharts_StateMachine.__init__)


def test_statecharts_statemachine_constructor_args():
    sig = inspect.signature(Statecharts_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statecharts_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(Statecharts_BooleanExpression)


def test_statecharts_booleanexpression_constructor_exists():
    assert callable(Statecharts_BooleanExpression.__init__)


def test_statecharts_booleanexpression_constructor_args():
    sig = inspect.signature(Statecharts_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statecharts_booleanexpression_has_value():
    assert hasattr(Statecharts_BooleanExpression, "value")
    descriptor = None
    for klass in Statecharts_BooleanExpression.__mro__:
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
Statecharts_Event_strategy = st.builds(
    Statecharts_Event,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
Statecharts_Guard_strategy = st.builds(
    Statecharts_Guard,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
Statecharts_StateVertex_strategy = st.builds(
    Statecharts_StateVertex,
)
Guard_strategy = st.builds(
    Guard,
)
Statecharts_Transition_strategy = st.builds(
    Statecharts_Transition,
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
Statecharts_State_strategy = st.builds(
    Statecharts_State,
)
State_strategy = st.builds(
    State,
)
Statecharts_CompositeState_strategy = st.builds(
    Statecharts_CompositeState,
    isConcurrent=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Statecharts_StateMachine_strategy = st.builds(
    Statecharts_StateMachine,
)
Statecharts_BooleanExpression_strategy = st.builds(
    Statecharts_BooleanExpression,
    value=
        safe_text
)

@given(instance=Statecharts_Event_strategy)
@settings(max_examples=50)
def test_statecharts_event_instantiation(instance):
    assert isinstance(instance, Statecharts_Event)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=Statecharts_Guard_strategy)
@settings(max_examples=50)
def test_statecharts_guard_instantiation(instance):
    assert isinstance(instance, Statecharts_Guard)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=Statecharts_StateVertex_strategy)
@settings(max_examples=50)
def test_statecharts_statevertex_instantiation(instance):
    assert isinstance(instance, Statecharts_StateVertex)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=Statecharts_Transition_strategy)
@settings(max_examples=50)
def test_statecharts_transition_instantiation(instance):
    assert isinstance(instance, Statecharts_Transition)

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

@given(instance=Statecharts_State_strategy)
@settings(max_examples=50)
def test_statecharts_state_instantiation(instance):
    assert isinstance(instance, Statecharts_State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Statecharts_CompositeState_strategy)
@settings(max_examples=50)
def test_statecharts_compositestate_instantiation(instance):
    assert isinstance(instance, Statecharts_CompositeState)



@given(instance=Statecharts_CompositeState_strategy)
def test_statecharts_compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Statecharts_StateMachine_strategy)
@settings(max_examples=50)
def test_statecharts_statemachine_instantiation(instance):
    assert isinstance(instance, Statecharts_StateMachine)

@given(instance=Statecharts_BooleanExpression_strategy)
@settings(max_examples=50)
def test_statecharts_booleanexpression_instantiation(instance):
    assert isinstance(instance, Statecharts_BooleanExpression)



@given(instance=Statecharts_BooleanExpression_strategy)
def test_statecharts_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
