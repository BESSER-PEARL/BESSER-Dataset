import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    fsm_TimedTransition,
    fsm_Trigger,
    fsm_Region,
    Pseudostate,
    fsm_Join,
    fsm_Fork,
    NamedElement,
    fsm_State,
    fsm_StateMachine,
    fsm_NamedElement,
    State,
    fsm_InitialState,
    fsm_Pseudostate,
    fsm_FinalState,
    fsm_CompositeState,
    fsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_timedtransition_is_not_abstract():
    assert not inspect.isabstract(fsm_TimedTransition)


def test_fsm_timedtransition_constructor_exists():
    assert callable(fsm_TimedTransition.__init__)


def test_fsm_timedtransition_constructor_args():
    sig = inspect.signature(fsm_TimedTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_fsm_timedtransition_has_duration():
    assert hasattr(fsm_TimedTransition, "duration")
    descriptor = None
    for klass in fsm_TimedTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm_trigger_has_expression():
    assert hasattr(fsm_Trigger, "expression")
    descriptor = None
    for klass in fsm_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsm_region_is_not_abstract():
    assert not inspect.isabstract(fsm_Region)


def test_fsm_region_constructor_exists():
    assert callable(fsm_Region.__init__)


def test_fsm_region_constructor_args():
    sig = inspect.signature(fsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_join_is_not_abstract():
    assert not inspect.isabstract(fsm_Join)


def test_fsm_join_constructor_exists():
    assert callable(fsm_Join.__init__)


def test_fsm_join_constructor_args():
    sig = inspect.signature(fsm_Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fork_is_not_abstract():
    assert not inspect.isabstract(fsm_Fork)


def test_fsm_fork_constructor_exists():
    assert callable(fsm_Fork.__init__)


def test_fsm_fork_constructor_args():
    sig = inspect.signature(fsm_Fork.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime" in params, "Missing parameter 'finalTime'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"

def test_fsm_state_has_finalTime():
    assert hasattr(fsm_State, "finalTime")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_initialTime():
    assert hasattr(fsm_State, "initialTime")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_namedelement_has_name():
    assert hasattr(fsm_NamedElement, "name")
    descriptor = None
    for klass in fsm_NamedElement.__mro__:
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



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(fsm_CompositeState)


def test_fsm_compositestate_constructor_exists():
    assert callable(fsm_CompositeState.__init__)


def test_fsm_compositestate_constructor_args():
    sig = inspect.signature(fsm_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime" in params, "Missing parameter 'finalTime'"
    assert "time" in params, "Missing parameter 'time'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"

def test_fsm_transition_has_finalTime():
    assert hasattr(fsm_Transition, "finalTime")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_time():
    assert hasattr(fsm_Transition, "time")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_initialTime():
    assert hasattr(fsm_Transition, "initialTime")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
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
Transition_strategy = st.builds(
    Transition,
)
fsm_TimedTransition_strategy = st.builds(
    fsm_TimedTransition,
    duration=
        st.integers()
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
fsm_Region_strategy = st.builds(
    fsm_Region,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm_Join_strategy = st.builds(
    fsm_Join,
)
fsm_Fork_strategy = st.builds(
    fsm_Fork,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_State_strategy = st.builds(
    fsm_State,
    finalTime=
        st.integers(),
    initialTime=
        st.integers()
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
fsm_CompositeState_strategy = st.builds(
    fsm_CompositeState,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    finalTime=
        st.integers(),
    time=
        st.integers(),
    initialTime=
        st.integers()
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=fsm_TimedTransition_strategy)
@settings(max_examples=50)
def test_fsm_timedtransition_instantiation(instance):
    assert isinstance(instance, fsm_TimedTransition)



@given(instance=fsm_TimedTransition_strategy)
def test_fsm_timedtransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=fsm_Trigger_strategy)
@settings(max_examples=50)
def test_fsm_trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)



@given(instance=fsm_Trigger_strategy)
def test_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsm_Region_strategy)
@settings(max_examples=50)
def test_fsm_region_instantiation(instance):
    assert isinstance(instance, fsm_Region)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm_Join_strategy)
@settings(max_examples=50)
def test_fsm_join_instantiation(instance):
    assert isinstance(instance, fsm_Join)

@given(instance=fsm_Fork_strategy)
@settings(max_examples=50)
def test_fsm_fork_instantiation(instance):
    assert isinstance(instance, fsm_Fork)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original



@given(instance=fsm_State_strategy)
def test_fsm_state_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)

@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=50)
def test_fsm_namedelement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)



@given(instance=fsm_NamedElement_strategy)
def test_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)

@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm_pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)

@given(instance=fsm_FinalState_strategy)
@settings(max_examples=50)
def test_fsm_finalstate_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)

@given(instance=fsm_CompositeState_strategy)
@settings(max_examples=50)
def test_fsm_compositestate_instantiation(instance):
    assert isinstance(instance, fsm_CompositeState)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original
