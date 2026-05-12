import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    UHSM_EObject,
    UHSM_TracedClass,
    StateMachine,
    UHSM_UStateMachine,
    UHSM_UState,
    UHSM_FinalState,
    UHSM_InitialState,
    Transition,
    UHSM_UTransition,
    UHSM_CompositeState,
    TracedClass,
    UHSM_Transition,
    UHSM_State,
    UHSM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_eobject_is_not_abstract():
    assert not inspect.isabstract(UHSM_EObject)


def test_uhsm_eobject_constructor_exists():
    assert callable(UHSM_EObject.__init__)


def test_uhsm_eobject_constructor_args():
    sig = inspect.signature(UHSM_EObject.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_tracedclass_is_not_abstract():
    assert not inspect.isabstract(UHSM_TracedClass)


def test_uhsm_tracedclass_constructor_exists():
    assert callable(UHSM_TracedClass.__init__)


def test_uhsm_tracedclass_constructor_args():
    sig = inspect.signature(UHSM_TracedClass.__init__)
    params = list(sig.parameters.keys())
    assert "trace" in params, "Missing parameter 'trace'"

def test_uhsm_tracedclass_has_trace():
    assert hasattr(UHSM_TracedClass, "trace")
    descriptor = None
    for klass in UHSM_TracedClass.__mro__:
        if "trace" in klass.__dict__:
            descriptor = klass.__dict__["trace"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_ustatemachine_is_not_abstract():
    assert not inspect.isabstract(UHSM_UStateMachine)


def test_uhsm_ustatemachine_constructor_exists():
    assert callable(UHSM_UStateMachine.__init__)


def test_uhsm_ustatemachine_constructor_args():
    sig = inspect.signature(UHSM_UStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_ustate_is_not_abstract():
    assert not inspect.isabstract(UHSM_UState)


def test_uhsm_ustate_constructor_exists():
    assert callable(UHSM_UState.__init__)


def test_uhsm_ustate_constructor_args():
    sig = inspect.signature(UHSM_UState.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(UHSM_FinalState)


def test_uhsm_finalstate_constructor_exists():
    assert callable(UHSM_FinalState.__init__)


def test_uhsm_finalstate_constructor_args():
    sig = inspect.signature(UHSM_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(UHSM_InitialState)


def test_uhsm_initialstate_constructor_exists():
    assert callable(UHSM_InitialState.__init__)


def test_uhsm_initialstate_constructor_args():
    sig = inspect.signature(UHSM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_utransition_is_not_abstract():
    assert not inspect.isabstract(UHSM_UTransition)


def test_uhsm_utransition_constructor_exists():
    assert callable(UHSM_UTransition.__init__)


def test_uhsm_utransition_constructor_args():
    sig = inspect.signature(UHSM_UTransition.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(UHSM_CompositeState)


def test_uhsm_compositestate_constructor_exists():
    assert callable(UHSM_CompositeState.__init__)


def test_uhsm_compositestate_constructor_args():
    sig = inspect.signature(UHSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_tracedclass_is_not_abstract():
    assert not inspect.isabstract(TracedClass)


def test_tracedclass_constructor_exists():
    assert callable(TracedClass.__init__)


def test_tracedclass_constructor_args():
    sig = inspect.signature(TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_uhsm_transition_is_not_abstract():
    assert not inspect.isabstract(UHSM_Transition)


def test_uhsm_transition_constructor_exists():
    assert callable(UHSM_Transition.__init__)


def test_uhsm_transition_constructor_args():
    sig = inspect.signature(UHSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm_transition_has_trigger():
    assert hasattr(UHSM_Transition, "trigger")
    descriptor = None
    for klass in UHSM_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_uhsm_transition_has_effect():
    assert hasattr(UHSM_Transition, "effect")
    descriptor = None
    for klass in UHSM_Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uhsm_transition_has_name():
    assert hasattr(UHSM_Transition, "name")
    descriptor = None
    for klass in UHSM_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uhsm_state_is_not_abstract():
    assert not inspect.isabstract(UHSM_State)


def test_uhsm_state_constructor_exists():
    assert callable(UHSM_State.__init__)


def test_uhsm_state_constructor_args():
    sig = inspect.signature(UHSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm_state_has_name():
    assert hasattr(UHSM_State, "name")
    descriptor = None
    for klass in UHSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uhsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(UHSM_StateMachine)


def test_uhsm_statemachine_constructor_exists():
    assert callable(UHSM_StateMachine.__init__)


def test_uhsm_statemachine_constructor_args():
    sig = inspect.signature(UHSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm_statemachine_has_name():
    assert hasattr(UHSM_StateMachine, "name")
    descriptor = None
    for klass in UHSM_StateMachine.__mro__:
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
State_strategy = st.builds(
    State,
)
UHSM_EObject_strategy = st.builds(
    UHSM_EObject,
)
UHSM_TracedClass_strategy = st.builds(
    UHSM_TracedClass,
    trace=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UHSM_UStateMachine_strategy = st.builds(
    UHSM_UStateMachine,
)
UHSM_UState_strategy = st.builds(
    UHSM_UState,
)
UHSM_FinalState_strategy = st.builds(
    UHSM_FinalState,
)
UHSM_InitialState_strategy = st.builds(
    UHSM_InitialState,
)
Transition_strategy = st.builds(
    Transition,
)
UHSM_UTransition_strategy = st.builds(
    UHSM_UTransition,
)
UHSM_CompositeState_strategy = st.builds(
    UHSM_CompositeState,
)
TracedClass_strategy = st.builds(
    TracedClass,
)
UHSM_Transition_strategy = st.builds(
    UHSM_Transition,
    trigger=
        safe_text,
    effect=
        safe_text,
    name=
        safe_text
)
UHSM_State_strategy = st.builds(
    UHSM_State,
    name=
        safe_text
)
UHSM_StateMachine_strategy = st.builds(
    UHSM_StateMachine,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UHSM_EObject_strategy)
@settings(max_examples=50)
def test_uhsm_eobject_instantiation(instance):
    assert isinstance(instance, UHSM_EObject)

@given(instance=UHSM_TracedClass_strategy)
@settings(max_examples=50)
def test_uhsm_tracedclass_instantiation(instance):
    assert isinstance(instance, UHSM_TracedClass)



@given(instance=UHSM_TracedClass_strategy)
def test_uhsm_tracedclass_trace_setter(instance):
    original = instance.trace
    instance.trace = original
    assert instance.trace == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UHSM_UStateMachine_strategy)
@settings(max_examples=50)
def test_uhsm_ustatemachine_instantiation(instance):
    assert isinstance(instance, UHSM_UStateMachine)

@given(instance=UHSM_UState_strategy)
@settings(max_examples=50)
def test_uhsm_ustate_instantiation(instance):
    assert isinstance(instance, UHSM_UState)

@given(instance=UHSM_FinalState_strategy)
@settings(max_examples=50)
def test_uhsm_finalstate_instantiation(instance):
    assert isinstance(instance, UHSM_FinalState)

@given(instance=UHSM_InitialState_strategy)
@settings(max_examples=50)
def test_uhsm_initialstate_instantiation(instance):
    assert isinstance(instance, UHSM_InitialState)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UHSM_UTransition_strategy)
@settings(max_examples=50)
def test_uhsm_utransition_instantiation(instance):
    assert isinstance(instance, UHSM_UTransition)

@given(instance=UHSM_CompositeState_strategy)
@settings(max_examples=50)
def test_uhsm_compositestate_instantiation(instance):
    assert isinstance(instance, UHSM_CompositeState)

@given(instance=TracedClass_strategy)
@settings(max_examples=50)
def test_tracedclass_instantiation(instance):
    assert isinstance(instance, TracedClass)

@given(instance=UHSM_Transition_strategy)
@settings(max_examples=50)
def test_uhsm_transition_instantiation(instance):
    assert isinstance(instance, UHSM_Transition)



@given(instance=UHSM_Transition_strategy)
def test_uhsm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=UHSM_Transition_strategy)
def test_uhsm_transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=UHSM_Transition_strategy)
def test_uhsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UHSM_State_strategy)
@settings(max_examples=50)
def test_uhsm_state_instantiation(instance):
    assert isinstance(instance, UHSM_State)



@given(instance=UHSM_State_strategy)
def test_uhsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UHSM_StateMachine_strategy)
@settings(max_examples=50)
def test_uhsm_statemachine_instantiation(instance):
    assert isinstance(instance, UHSM_StateMachine)



@given(instance=UHSM_StateMachine_strategy)
def test_uhsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
