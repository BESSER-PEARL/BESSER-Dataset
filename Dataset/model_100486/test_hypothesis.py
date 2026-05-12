import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UHSM::EObject,
    UHSM::TracedClass,
    StateMachine,
    UHSM::UStateMachine,
    Transition,
    UHSM::UTransition,
    TracedClass,
    UHSM::Transition,
    UHSM::State,
    UHSM::StateMachine,
    State,
    UHSM::CompositeState,
    UHSM::InitialState,
    UHSM::UState,
    UHSM::FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uhsm::eobject_is_not_abstract():
    assert not inspect.isabstract(UHSM::EObject)


def test_uhsm::eobject_constructor_exists():
    assert callable(UHSM::EObject.__init__)


def test_uhsm::eobject_constructor_args():
    sig = inspect.signature(UHSM::EObject.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::tracedclass_is_not_abstract():
    assert not inspect.isabstract(UHSM::TracedClass)


def test_uhsm::tracedclass_constructor_exists():
    assert callable(UHSM::TracedClass.__init__)


def test_uhsm::tracedclass_constructor_args():
    sig = inspect.signature(UHSM::TracedClass.__init__)
    params = list(sig.parameters.keys())
    assert "trace" in params, "Missing parameter 'trace'"

def test_uhsm::tracedclass_has_trace():
    assert hasattr(UHSM::TracedClass, "trace")
    descriptor = None
    for klass in UHSM::TracedClass.__mro__:
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



def test_uhsm::ustatemachine_is_not_abstract():
    assert not inspect.isabstract(UHSM::UStateMachine)


def test_uhsm::ustatemachine_constructor_exists():
    assert callable(UHSM::UStateMachine.__init__)


def test_uhsm::ustatemachine_constructor_args():
    sig = inspect.signature(UHSM::UStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::utransition_is_not_abstract():
    assert not inspect.isabstract(UHSM::UTransition)


def test_uhsm::utransition_constructor_exists():
    assert callable(UHSM::UTransition.__init__)


def test_uhsm::utransition_constructor_args():
    sig = inspect.signature(UHSM::UTransition.__init__)
    params = list(sig.parameters.keys())



def test_tracedclass_is_not_abstract():
    assert not inspect.isabstract(TracedClass)


def test_tracedclass_constructor_exists():
    assert callable(TracedClass.__init__)


def test_tracedclass_constructor_args():
    sig = inspect.signature(TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::transition_is_not_abstract():
    assert not inspect.isabstract(UHSM::Transition)


def test_uhsm::transition_constructor_exists():
    assert callable(UHSM::Transition.__init__)


def test_uhsm::transition_constructor_args():
    sig = inspect.signature(UHSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm::transition_has_effect():
    assert hasattr(UHSM::Transition, "effect")
    descriptor = None
    for klass in UHSM::Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uhsm::transition_has_trigger():
    assert hasattr(UHSM::Transition, "trigger")
    descriptor = None
    for klass in UHSM::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_uhsm::transition_has_name():
    assert hasattr(UHSM::Transition, "name")
    descriptor = None
    for klass in UHSM::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uhsm::state_is_not_abstract():
    assert not inspect.isabstract(UHSM::State)


def test_uhsm::state_constructor_exists():
    assert callable(UHSM::State.__init__)


def test_uhsm::state_constructor_args():
    sig = inspect.signature(UHSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm::state_has_name():
    assert hasattr(UHSM::State, "name")
    descriptor = None
    for klass in UHSM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uhsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(UHSM::StateMachine)


def test_uhsm::statemachine_constructor_exists():
    assert callable(UHSM::StateMachine.__init__)


def test_uhsm::statemachine_constructor_args():
    sig = inspect.signature(UHSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uhsm::statemachine_has_name():
    assert hasattr(UHSM::StateMachine, "name")
    descriptor = None
    for klass in UHSM::StateMachine.__mro__:
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



def test_uhsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(UHSM::CompositeState)


def test_uhsm::compositestate_constructor_exists():
    assert callable(UHSM::CompositeState.__init__)


def test_uhsm::compositestate_constructor_args():
    sig = inspect.signature(UHSM::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(UHSM::InitialState)


def test_uhsm::initialstate_constructor_exists():
    assert callable(UHSM::InitialState.__init__)


def test_uhsm::initialstate_constructor_args():
    sig = inspect.signature(UHSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::ustate_is_not_abstract():
    assert not inspect.isabstract(UHSM::UState)


def test_uhsm::ustate_constructor_exists():
    assert callable(UHSM::UState.__init__)


def test_uhsm::ustate_constructor_args():
    sig = inspect.signature(UHSM::UState.__init__)
    params = list(sig.parameters.keys())



def test_uhsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(UHSM::FinalState)


def test_uhsm::finalstate_constructor_exists():
    assert callable(UHSM::FinalState.__init__)


def test_uhsm::finalstate_constructor_args():
    sig = inspect.signature(UHSM::FinalState.__init__)
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
UHSM::EObject_strategy = st.builds(
    UHSM::EObject,
)
UHSM::TracedClass_strategy = st.builds(
    UHSM::TracedClass,
    trace=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UHSM::UStateMachine_strategy = st.builds(
    UHSM::UStateMachine,
)
Transition_strategy = st.builds(
    Transition,
)
UHSM::UTransition_strategy = st.builds(
    UHSM::UTransition,
)
TracedClass_strategy = st.builds(
    TracedClass,
)
UHSM::Transition_strategy = st.builds(
    UHSM::Transition,
    effect=
        safe_text,
    trigger=
        safe_text,
    name=
        safe_text
)
UHSM::State_strategy = st.builds(
    UHSM::State,
    name=
        safe_text
)
UHSM::StateMachine_strategy = st.builds(
    UHSM::StateMachine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
UHSM::CompositeState_strategy = st.builds(
    UHSM::CompositeState,
)
UHSM::InitialState_strategy = st.builds(
    UHSM::InitialState,
)
UHSM::UState_strategy = st.builds(
    UHSM::UState,
)
UHSM::FinalState_strategy = st.builds(
    UHSM::FinalState,
)

@given(instance=UHSM::EObject_strategy)
@settings(max_examples=50)
def test_uhsm::eobject_instantiation(instance):
    assert isinstance(instance, UHSM::EObject)

@given(instance=UHSM::TracedClass_strategy)
@settings(max_examples=50)
def test_uhsm::tracedclass_instantiation(instance):
    assert isinstance(instance, UHSM::TracedClass)

@given(instance=UHSM::TracedClass_strategy)
def test_uhsm::tracedclass_trace_type(instance):
    assert isinstance(instance.trace, str)


@given(instance=UHSM::TracedClass_strategy)
def test_uhsm::tracedclass_trace_setter(instance):
    original = instance.trace
    instance.trace = original
    assert instance.trace == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UHSM::UStateMachine_strategy)
@settings(max_examples=50)
def test_uhsm::ustatemachine_instantiation(instance):
    assert isinstance(instance, UHSM::UStateMachine)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UHSM::UTransition_strategy)
@settings(max_examples=50)
def test_uhsm::utransition_instantiation(instance):
    assert isinstance(instance, UHSM::UTransition)

@given(instance=TracedClass_strategy)
@settings(max_examples=50)
def test_tracedclass_instantiation(instance):
    assert isinstance(instance, TracedClass)

@given(instance=UHSM::Transition_strategy)
@settings(max_examples=50)
def test_uhsm::transition_instantiation(instance):
    assert isinstance(instance, UHSM::Transition)

@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UHSM::Transition_strategy)
def test_uhsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UHSM::State_strategy)
@settings(max_examples=50)
def test_uhsm::state_instantiation(instance):
    assert isinstance(instance, UHSM::State)

@given(instance=UHSM::State_strategy)
def test_uhsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UHSM::State_strategy)
def test_uhsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UHSM::StateMachine_strategy)
@settings(max_examples=50)
def test_uhsm::statemachine_instantiation(instance):
    assert isinstance(instance, UHSM::StateMachine)

@given(instance=UHSM::StateMachine_strategy)
def test_uhsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UHSM::StateMachine_strategy)
def test_uhsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UHSM::CompositeState_strategy)
@settings(max_examples=50)
def test_uhsm::compositestate_instantiation(instance):
    assert isinstance(instance, UHSM::CompositeState)

@given(instance=UHSM::InitialState_strategy)
@settings(max_examples=50)
def test_uhsm::initialstate_instantiation(instance):
    assert isinstance(instance, UHSM::InitialState)

@given(instance=UHSM::UState_strategy)
@settings(max_examples=50)
def test_uhsm::ustate_instantiation(instance):
    assert isinstance(instance, UHSM::UState)

@given(instance=UHSM::FinalState_strategy)
@settings(max_examples=50)
def test_uhsm::finalstate_instantiation(instance):
    assert isinstance(instance, UHSM::FinalState)
