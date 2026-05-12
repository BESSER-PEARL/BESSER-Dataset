import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Pseudostate,
    finitestatemachines_Join2,
    finitestatemachines_Fork,
    Transition2,
    finitestatemachines_TimedTransition,
    NamedElement,
    finitestatemachines_State2,
    finitestatemachines_Transition2,
    finitestatemachines_StateMachine,
    finitestatemachines_NamedElement,
    finitestatemachines_Trigger2,
    State2,
    finitestatemachines_Pseudostate,
    finitestatemachines_InitialState,
    finitestatemachines_FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_join2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_Join2)


def test_finitestatemachines_join2_constructor_exists():
    assert callable(finitestatemachines_Join2.__init__)


def test_finitestatemachines_join2_constructor_args():
    sig = inspect.signature(finitestatemachines_Join2.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_fork_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_Fork)


def test_finitestatemachines_fork_constructor_exists():
    assert callable(finitestatemachines_Fork.__init__)


def test_finitestatemachines_fork_constructor_args():
    sig = inspect.signature(finitestatemachines_Fork.__init__)
    params = list(sig.parameters.keys())



def test_transition2_is_not_abstract():
    assert not inspect.isabstract(Transition2)


def test_transition2_constructor_exists():
    assert callable(Transition2.__init__)


def test_transition2_constructor_args():
    sig = inspect.signature(Transition2.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_timedtransition_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_TimedTransition)


def test_finitestatemachines_timedtransition_constructor_exists():
    assert callable(finitestatemachines_TimedTransition.__init__)


def test_finitestatemachines_timedtransition_constructor_args():
    sig = inspect.signature(finitestatemachines_TimedTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_finitestatemachines_timedtransition_has_duration():
    assert hasattr(finitestatemachines_TimedTransition, "duration")
    descriptor = None
    for klass in finitestatemachines_TimedTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_state2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_State2)


def test_finitestatemachines_state2_constructor_exists():
    assert callable(finitestatemachines_State2.__init__)


def test_finitestatemachines_state2_constructor_args():
    sig = inspect.signature(finitestatemachines_State2.__init__)
    params = list(sig.parameters.keys())
    assert "initialTime2" in params, "Missing parameter 'initialTime2'"
    assert "finalTime" in params, "Missing parameter 'finalTime'"

def test_finitestatemachines_state2_has_initialTime2():
    assert hasattr(finitestatemachines_State2, "initialTime2")
    descriptor = None
    for klass in finitestatemachines_State2.__mro__:
        if "initialTime2" in klass.__dict__:
            descriptor = klass.__dict__["initialTime2"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines_state2_has_finalTime():
    assert hasattr(finitestatemachines_State2, "finalTime")
    descriptor = None
    for klass in finitestatemachines_State2.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines_transition2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_Transition2)


def test_finitestatemachines_transition2_constructor_exists():
    assert callable(finitestatemachines_Transition2.__init__)


def test_finitestatemachines_transition2_constructor_args():
    sig = inspect.signature(finitestatemachines_Transition2.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime2" in params, "Missing parameter 'finalTime2'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"

def test_finitestatemachines_transition2_has_finalTime2():
    assert hasattr(finitestatemachines_Transition2, "finalTime2")
    descriptor = None
    for klass in finitestatemachines_Transition2.__mro__:
        if "finalTime2" in klass.__dict__:
            descriptor = klass.__dict__["finalTime2"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines_transition2_has_initialTime():
    assert hasattr(finitestatemachines_Transition2, "initialTime")
    descriptor = None
    for klass in finitestatemachines_Transition2.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_StateMachine)


def test_finitestatemachines_statemachine_constructor_exists():
    assert callable(finitestatemachines_StateMachine.__init__)


def test_finitestatemachines_statemachine_constructor_args():
    sig = inspect.signature(finitestatemachines_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_namedelement_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_NamedElement)


def test_finitestatemachines_namedelement_constructor_exists():
    assert callable(finitestatemachines_NamedElement.__init__)


def test_finitestatemachines_namedelement_constructor_args():
    sig = inspect.signature(finitestatemachines_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finitestatemachines_namedelement_has_name():
    assert hasattr(finitestatemachines_NamedElement, "name")
    descriptor = None
    for klass in finitestatemachines_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines_trigger2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_Trigger2)


def test_finitestatemachines_trigger2_constructor_exists():
    assert callable(finitestatemachines_Trigger2.__init__)


def test_finitestatemachines_trigger2_constructor_args():
    sig = inspect.signature(finitestatemachines_Trigger2.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_finitestatemachines_trigger2_has_expression():
    assert hasattr(finitestatemachines_Trigger2, "expression")
    descriptor = None
    for klass in finitestatemachines_Trigger2.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_state2_is_not_abstract():
    assert not inspect.isabstract(State2)


def test_state2_constructor_exists():
    assert callable(State2.__init__)


def test_state2_constructor_args():
    sig = inspect.signature(State2.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_pseudostate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_Pseudostate)


def test_finitestatemachines_pseudostate_constructor_exists():
    assert callable(finitestatemachines_Pseudostate.__init__)


def test_finitestatemachines_pseudostate_constructor_args():
    sig = inspect.signature(finitestatemachines_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_initialstate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_InitialState)


def test_finitestatemachines_initialstate_constructor_exists():
    assert callable(finitestatemachines_InitialState.__init__)


def test_finitestatemachines_initialstate_constructor_args():
    sig = inspect.signature(finitestatemachines_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines_finalstate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines_FinalState)


def test_finitestatemachines_finalstate_constructor_exists():
    assert callable(finitestatemachines_FinalState.__init__)


def test_finitestatemachines_finalstate_constructor_args():
    sig = inspect.signature(finitestatemachines_FinalState.__init__)
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
Pseudostate_strategy = st.builds(
    Pseudostate,
)
finitestatemachines_Join2_strategy = st.builds(
    finitestatemachines_Join2,
)
finitestatemachines_Fork_strategy = st.builds(
    finitestatemachines_Fork,
)
Transition2_strategy = st.builds(
    Transition2,
)
finitestatemachines_TimedTransition_strategy = st.builds(
    finitestatemachines_TimedTransition,
    duration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
finitestatemachines_State2_strategy = st.builds(
    finitestatemachines_State2,
    initialTime2=
        st.integers(),
    finalTime=
        st.integers()
)
finitestatemachines_Transition2_strategy = st.builds(
    finitestatemachines_Transition2,
    finalTime2=
        st.integers(),
    initialTime=
        st.integers()
)
finitestatemachines_StateMachine_strategy = st.builds(
    finitestatemachines_StateMachine,
)
finitestatemachines_NamedElement_strategy = st.builds(
    finitestatemachines_NamedElement,
    name=
        safe_text
)
finitestatemachines_Trigger2_strategy = st.builds(
    finitestatemachines_Trigger2,
    expression=
        safe_text
)
State2_strategy = st.builds(
    State2,
)
finitestatemachines_Pseudostate_strategy = st.builds(
    finitestatemachines_Pseudostate,
)
finitestatemachines_InitialState_strategy = st.builds(
    finitestatemachines_InitialState,
)
finitestatemachines_FinalState_strategy = st.builds(
    finitestatemachines_FinalState,
)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=finitestatemachines_Join2_strategy)
@settings(max_examples=50)
def test_finitestatemachines_join2_instantiation(instance):
    assert isinstance(instance, finitestatemachines_Join2)

@given(instance=finitestatemachines_Fork_strategy)
@settings(max_examples=50)
def test_finitestatemachines_fork_instantiation(instance):
    assert isinstance(instance, finitestatemachines_Fork)

@given(instance=Transition2_strategy)
@settings(max_examples=50)
def test_transition2_instantiation(instance):
    assert isinstance(instance, Transition2)

@given(instance=finitestatemachines_TimedTransition_strategy)
@settings(max_examples=50)
def test_finitestatemachines_timedtransition_instantiation(instance):
    assert isinstance(instance, finitestatemachines_TimedTransition)



@given(instance=finitestatemachines_TimedTransition_strategy)
def test_finitestatemachines_timedtransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=finitestatemachines_State2_strategy)
@settings(max_examples=50)
def test_finitestatemachines_state2_instantiation(instance):
    assert isinstance(instance, finitestatemachines_State2)



@given(instance=finitestatemachines_State2_strategy)
def test_finitestatemachines_state2_initialTime2_setter(instance):
    original = instance.initialTime2
    instance.initialTime2 = original
    assert instance.initialTime2 == original



@given(instance=finitestatemachines_State2_strategy)
def test_finitestatemachines_state2_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=finitestatemachines_Transition2_strategy)
@settings(max_examples=50)
def test_finitestatemachines_transition2_instantiation(instance):
    assert isinstance(instance, finitestatemachines_Transition2)



@given(instance=finitestatemachines_Transition2_strategy)
def test_finitestatemachines_transition2_finalTime2_setter(instance):
    original = instance.finalTime2
    instance.finalTime2 = original
    assert instance.finalTime2 == original



@given(instance=finitestatemachines_Transition2_strategy)
def test_finitestatemachines_transition2_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=finitestatemachines_StateMachine_strategy)
@settings(max_examples=50)
def test_finitestatemachines_statemachine_instantiation(instance):
    assert isinstance(instance, finitestatemachines_StateMachine)

@given(instance=finitestatemachines_NamedElement_strategy)
@settings(max_examples=50)
def test_finitestatemachines_namedelement_instantiation(instance):
    assert isinstance(instance, finitestatemachines_NamedElement)



@given(instance=finitestatemachines_NamedElement_strategy)
def test_finitestatemachines_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finitestatemachines_Trigger2_strategy)
@settings(max_examples=50)
def test_finitestatemachines_trigger2_instantiation(instance):
    assert isinstance(instance, finitestatemachines_Trigger2)



@given(instance=finitestatemachines_Trigger2_strategy)
def test_finitestatemachines_trigger2_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=State2_strategy)
@settings(max_examples=50)
def test_state2_instantiation(instance):
    assert isinstance(instance, State2)

@given(instance=finitestatemachines_Pseudostate_strategy)
@settings(max_examples=50)
def test_finitestatemachines_pseudostate_instantiation(instance):
    assert isinstance(instance, finitestatemachines_Pseudostate)

@given(instance=finitestatemachines_InitialState_strategy)
@settings(max_examples=50)
def test_finitestatemachines_initialstate_instantiation(instance):
    assert isinstance(instance, finitestatemachines_InitialState)

@given(instance=finitestatemachines_FinalState_strategy)
@settings(max_examples=50)
def test_finitestatemachines_finalstate_instantiation(instance):
    assert isinstance(instance, finitestatemachines_FinalState)
