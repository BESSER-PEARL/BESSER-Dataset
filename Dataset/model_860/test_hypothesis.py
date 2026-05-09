import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::NamedElement,
    Pseudostate,
    fsm::Join,
    fsm::Fork,
    Transition,
    fsm::TimedTransition,
    fsm::Trigger,
    State,
    fsm::InitialState,
    fsm::Pseudostate,
    fsm::FinalState,
    NamedElement,
    fsm::Transition,
    fsm::State,
    fsm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(fsm::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(fsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(fsm::NamedElement, "name")
    descriptor = None
    for klass in fsm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::join_is_not_abstract():
    assert not inspect.isabstract(fsm::Join)


def test_fsm::join_constructor_exists():
    assert callable(fsm::Join.__init__)


def test_fsm::join_constructor_args():
    sig = inspect.signature(fsm::Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fork_is_not_abstract():
    assert not inspect.isabstract(fsm::Fork)


def test_fsm::fork_constructor_exists():
    assert callable(fsm::Fork.__init__)


def test_fsm::fork_constructor_args():
    sig = inspect.signature(fsm::Fork.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::timedtransition_is_not_abstract():
    assert not inspect.isabstract(fsm::TimedTransition)


def test_fsm::timedtransition_constructor_exists():
    assert callable(fsm::TimedTransition.__init__)


def test_fsm::timedtransition_constructor_args():
    sig = inspect.signature(fsm::TimedTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_fsm::timedtransition_has_duration():
    assert hasattr(fsm::TimedTransition, "duration")
    descriptor = None
    for klass in fsm::TimedTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_fsm::trigger_is_not_abstract():
    assert not inspect.isabstract(fsm::Trigger)


def test_fsm::trigger_constructor_exists():
    assert callable(fsm::Trigger.__init__)


def test_fsm::trigger_constructor_args():
    sig = inspect.signature(fsm::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm::trigger_has_expression():
    assert hasattr(fsm::Trigger, "expression")
    descriptor = None
    for klass in fsm::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime" in params, "Missing parameter 'finalTime'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "time" in params, "Missing parameter 'time'"

def test_fsm::transition_has_finalTime():
    assert hasattr(fsm::Transition, "finalTime")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_initialTime():
    assert hasattr(fsm::Transition, "initialTime")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_time():
    assert hasattr(fsm::Transition, "time")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime" in params, "Missing parameter 'finalTime'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"

def test_fsm::state_has_finalTime():
    assert hasattr(fsm::State, "finalTime")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_initialTime():
    assert hasattr(fsm::State, "initialTime")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
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
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm::Join_strategy = st.builds(
    fsm::Join,
)
fsm::Fork_strategy = st.builds(
    fsm::Fork,
)
Transition_strategy = st.builds(
    Transition,
)
fsm::TimedTransition_strategy = st.builds(
    fsm::TimedTransition,
    duration=
        st.integers()
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    finalTime=
        st.integers(),
    initialTime=
        st.integers(),
    time=
        st.integers()
)
fsm::State_strategy = st.builds(
    fsm::State,
    finalTime=
        st.integers(),
    initialTime=
        st.integers()
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)

@given(instance=fsm::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, fsm::NamedElement)

@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm::Join_strategy)
@settings(max_examples=50)
def test_fsm::join_instantiation(instance):
    assert isinstance(instance, fsm::Join)

@given(instance=fsm::Fork_strategy)
@settings(max_examples=50)
def test_fsm::fork_instantiation(instance):
    assert isinstance(instance, fsm::Fork)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=fsm::TimedTransition_strategy)
@settings(max_examples=50)
def test_fsm::timedtransition_instantiation(instance):
    assert isinstance(instance, fsm::TimedTransition)

@given(instance=fsm::TimedTransition_strategy)
def test_fsm::timedtransition_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=fsm::TimedTransition_strategy)
def test_fsm::timedtransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=fsm::Trigger_strategy)
@settings(max_examples=50)
def test_fsm::trigger_instantiation(instance):
    assert isinstance(instance, fsm::Trigger)

@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_finalTime_type(instance):
    assert isinstance(instance.finalTime, int)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_finalTime_type(instance):
    assert isinstance(instance.finalTime, int)


@given(instance=fsm::State_strategy)
def test_fsm::state_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=fsm::State_strategy)
def test_fsm::state_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=fsm::State_strategy)
def test_fsm::state_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)
