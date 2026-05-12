import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    states_Trace,
    states_Transition,
    states_State,
    states_StateSystem,
    states_ActionExecution,
    states_Event,
    states_EObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_states_trace_is_not_abstract():
    assert not inspect.isabstract(states_Trace)


def test_states_trace_constructor_exists():
    assert callable(states_Trace.__init__)


def test_states_trace_constructor_args():
    sig = inspect.signature(states_Trace.__init__)
    params = list(sig.parameters.keys())



def test_states_transition_is_not_abstract():
    assert not inspect.isabstract(states_Transition)


def test_states_transition_constructor_exists():
    assert callable(states_Transition.__init__)


def test_states_transition_constructor_args():
    sig = inspect.signature(states_Transition.__init__)
    params = list(sig.parameters.keys())



def test_states_state_is_not_abstract():
    assert not inspect.isabstract(states_State)


def test_states_state_constructor_exists():
    assert callable(states_State.__init__)


def test_states_state_constructor_args():
    sig = inspect.signature(states_State.__init__)
    params = list(sig.parameters.keys())



def test_states_statesystem_is_not_abstract():
    assert not inspect.isabstract(states_StateSystem)


def test_states_statesystem_constructor_exists():
    assert callable(states_StateSystem.__init__)


def test_states_statesystem_constructor_args():
    sig = inspect.signature(states_StateSystem.__init__)
    params = list(sig.parameters.keys())



def test_states_actionexecution_is_not_abstract():
    assert not inspect.isabstract(states_ActionExecution)


def test_states_actionexecution_constructor_exists():
    assert callable(states_ActionExecution.__init__)


def test_states_actionexecution_constructor_args():
    sig = inspect.signature(states_ActionExecution.__init__)
    params = list(sig.parameters.keys())



def test_states_event_is_not_abstract():
    assert not inspect.isabstract(states_Event)


def test_states_event_constructor_exists():
    assert callable(states_Event.__init__)


def test_states_event_constructor_args():
    sig = inspect.signature(states_Event.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_states_event_has_qualifiedName():
    assert hasattr(states_Event, "qualifiedName")
    descriptor = None
    for klass in states_Event.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_states_eobject_is_not_abstract():
    assert not inspect.isabstract(states_EObject)


def test_states_eobject_constructor_exists():
    assert callable(states_EObject.__init__)


def test_states_eobject_constructor_args():
    sig = inspect.signature(states_EObject.__init__)
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
states_Trace_strategy = st.builds(
    states_Trace,
)
states_Transition_strategy = st.builds(
    states_Transition,
)
states_State_strategy = st.builds(
    states_State,
)
states_StateSystem_strategy = st.builds(
    states_StateSystem,
)
states_ActionExecution_strategy = st.builds(
    states_ActionExecution,
)
states_Event_strategy = st.builds(
    states_Event,
    qualifiedName=
        safe_text
)
states_EObject_strategy = st.builds(
    states_EObject,
)

@given(instance=states_Trace_strategy)
@settings(max_examples=50)
def test_states_trace_instantiation(instance):
    assert isinstance(instance, states_Trace)

@given(instance=states_Transition_strategy)
@settings(max_examples=50)
def test_states_transition_instantiation(instance):
    assert isinstance(instance, states_Transition)

@given(instance=states_State_strategy)
@settings(max_examples=50)
def test_states_state_instantiation(instance):
    assert isinstance(instance, states_State)

@given(instance=states_StateSystem_strategy)
@settings(max_examples=50)
def test_states_statesystem_instantiation(instance):
    assert isinstance(instance, states_StateSystem)

@given(instance=states_ActionExecution_strategy)
@settings(max_examples=50)
def test_states_actionexecution_instantiation(instance):
    assert isinstance(instance, states_ActionExecution)

@given(instance=states_Event_strategy)
@settings(max_examples=50)
def test_states_event_instantiation(instance):
    assert isinstance(instance, states_Event)



@given(instance=states_Event_strategy)
def test_states_event_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=states_EObject_strategy)
@settings(max_examples=50)
def test_states_eobject_instantiation(instance):
    assert isinstance(instance, states_EObject)
