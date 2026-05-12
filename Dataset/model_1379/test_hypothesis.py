import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tsm_NamedElement,
    tsm_TimeEvent,
    NamedElement,
    tsm_Transition,
    tsm_StateMachine,
    tsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(tsm_NamedElement)


def test_tsm_namedelement_constructor_exists():
    assert callable(tsm_NamedElement.__init__)


def test_tsm_namedelement_constructor_args():
    sig = inspect.signature(tsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tsm_namedelement_has_name():
    assert hasattr(tsm_NamedElement, "name")
    descriptor = None
    for klass in tsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tsm_timeevent_is_not_abstract():
    assert not inspect.isabstract(tsm_TimeEvent)


def test_tsm_timeevent_constructor_exists():
    assert callable(tsm_TimeEvent.__init__)


def test_tsm_timeevent_constructor_args():
    sig = inspect.signature(tsm_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tsm_timeevent_has_time():
    assert hasattr(tsm_TimeEvent, "time")
    descriptor = None
    for klass in tsm_TimeEvent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tsm_transition_is_not_abstract():
    assert not inspect.isabstract(tsm_Transition)


def test_tsm_transition_constructor_exists():
    assert callable(tsm_Transition.__init__)


def test_tsm_transition_constructor_args():
    sig = inspect.signature(tsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_tsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(tsm_StateMachine)


def test_tsm_statemachine_constructor_exists():
    assert callable(tsm_StateMachine.__init__)


def test_tsm_statemachine_constructor_args():
    sig = inspect.signature(tsm_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_tsm_state_is_not_abstract():
    assert not inspect.isabstract(tsm_State)


def test_tsm_state_constructor_exists():
    assert callable(tsm_State.__init__)


def test_tsm_state_constructor_args():
    sig = inspect.signature(tsm_State.__init__)
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
tsm_NamedElement_strategy = st.builds(
    tsm_NamedElement,
    name=
        safe_text
)
tsm_TimeEvent_strategy = st.builds(
    tsm_TimeEvent,
    time=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tsm_Transition_strategy = st.builds(
    tsm_Transition,
)
tsm_StateMachine_strategy = st.builds(
    tsm_StateMachine,
)
tsm_State_strategy = st.builds(
    tsm_State,
)

@given(instance=tsm_NamedElement_strategy)
@settings(max_examples=50)
def test_tsm_namedelement_instantiation(instance):
    assert isinstance(instance, tsm_NamedElement)



@given(instance=tsm_NamedElement_strategy)
def test_tsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tsm_TimeEvent_strategy)
@settings(max_examples=50)
def test_tsm_timeevent_instantiation(instance):
    assert isinstance(instance, tsm_TimeEvent)



@given(instance=tsm_TimeEvent_strategy)
def test_tsm_timeevent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tsm_Transition_strategy)
@settings(max_examples=50)
def test_tsm_transition_instantiation(instance):
    assert isinstance(instance, tsm_Transition)

@given(instance=tsm_StateMachine_strategy)
@settings(max_examples=50)
def test_tsm_statemachine_instantiation(instance):
    assert isinstance(instance, tsm_StateMachine)

@given(instance=tsm_State_strategy)
@settings(max_examples=50)
def test_tsm_state_instantiation(instance):
    assert isinstance(instance, tsm_State)
