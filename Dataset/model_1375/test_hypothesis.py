import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Pseudostate,
    finitestatemachines::Join2,
    finitestatemachines::Fork,
    Transition2,
    finitestatemachines::TimedTransition,
    NamedElement,
    finitestatemachines::Transition2,
    finitestatemachines::State2,
    finitestatemachines::StateMachine,
    finitestatemachines::NamedElement,
    finitestatemachines::Trigger2,
    State2,
    finitestatemachines::Pseudostate,
    finitestatemachines::InitialState,
    finitestatemachines::FinalState,
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



def test_finitestatemachines::join2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::Join2)


def test_finitestatemachines::join2_constructor_exists():
    assert callable(finitestatemachines::Join2.__init__)


def test_finitestatemachines::join2_constructor_args():
    sig = inspect.signature(finitestatemachines::Join2.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines::fork_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::Fork)


def test_finitestatemachines::fork_constructor_exists():
    assert callable(finitestatemachines::Fork.__init__)


def test_finitestatemachines::fork_constructor_args():
    sig = inspect.signature(finitestatemachines::Fork.__init__)
    params = list(sig.parameters.keys())



def test_transition2_is_not_abstract():
    assert not inspect.isabstract(Transition2)


def test_transition2_constructor_exists():
    assert callable(Transition2.__init__)


def test_transition2_constructor_args():
    sig = inspect.signature(Transition2.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines::timedtransition_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::TimedTransition)


def test_finitestatemachines::timedtransition_constructor_exists():
    assert callable(finitestatemachines::TimedTransition.__init__)


def test_finitestatemachines::timedtransition_constructor_args():
    sig = inspect.signature(finitestatemachines::TimedTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_finitestatemachines::timedtransition_has_duration():
    assert hasattr(finitestatemachines::TimedTransition, "duration")
    descriptor = None
    for klass in finitestatemachines::TimedTransition.__mro__:
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



def test_finitestatemachines::transition2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::Transition2)


def test_finitestatemachines::transition2_constructor_exists():
    assert callable(finitestatemachines::Transition2.__init__)


def test_finitestatemachines::transition2_constructor_args():
    sig = inspect.signature(finitestatemachines::Transition2.__init__)
    params = list(sig.parameters.keys())
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "finalTime2" in params, "Missing parameter 'finalTime2'"

def test_finitestatemachines::transition2_has_initialTime():
    assert hasattr(finitestatemachines::Transition2, "initialTime")
    descriptor = None
    for klass in finitestatemachines::Transition2.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines::transition2_has_finalTime2():
    assert hasattr(finitestatemachines::Transition2, "finalTime2")
    descriptor = None
    for klass in finitestatemachines::Transition2.__mro__:
        if "finalTime2" in klass.__dict__:
            descriptor = klass.__dict__["finalTime2"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines::state2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::State2)


def test_finitestatemachines::state2_constructor_exists():
    assert callable(finitestatemachines::State2.__init__)


def test_finitestatemachines::state2_constructor_args():
    sig = inspect.signature(finitestatemachines::State2.__init__)
    params = list(sig.parameters.keys())
    assert "finalTime" in params, "Missing parameter 'finalTime'"
    assert "initialTime2" in params, "Missing parameter 'initialTime2'"

def test_finitestatemachines::state2_has_finalTime():
    assert hasattr(finitestatemachines::State2, "finalTime")
    descriptor = None
    for klass in finitestatemachines::State2.__mro__:
        if "finalTime" in klass.__dict__:
            descriptor = klass.__dict__["finalTime"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines::state2_has_initialTime2():
    assert hasattr(finitestatemachines::State2, "initialTime2")
    descriptor = None
    for klass in finitestatemachines::State2.__mro__:
        if "initialTime2" in klass.__dict__:
            descriptor = klass.__dict__["initialTime2"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::StateMachine)


def test_finitestatemachines::statemachine_constructor_exists():
    assert callable(finitestatemachines::StateMachine.__init__)


def test_finitestatemachines::statemachine_constructor_args():
    sig = inspect.signature(finitestatemachines::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines::namedelement_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::NamedElement)


def test_finitestatemachines::namedelement_constructor_exists():
    assert callable(finitestatemachines::NamedElement.__init__)


def test_finitestatemachines::namedelement_constructor_args():
    sig = inspect.signature(finitestatemachines::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finitestatemachines::namedelement_has_name():
    assert hasattr(finitestatemachines::NamedElement, "name")
    descriptor = None
    for klass in finitestatemachines::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines::trigger2_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::Trigger2)


def test_finitestatemachines::trigger2_constructor_exists():
    assert callable(finitestatemachines::Trigger2.__init__)


def test_finitestatemachines::trigger2_constructor_args():
    sig = inspect.signature(finitestatemachines::Trigger2.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_finitestatemachines::trigger2_has_expression():
    assert hasattr(finitestatemachines::Trigger2, "expression")
    descriptor = None
    for klass in finitestatemachines::Trigger2.__mro__:
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



def test_finitestatemachines::pseudostate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::Pseudostate)


def test_finitestatemachines::pseudostate_constructor_exists():
    assert callable(finitestatemachines::Pseudostate.__init__)


def test_finitestatemachines::pseudostate_constructor_args():
    sig = inspect.signature(finitestatemachines::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines::initialstate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::InitialState)


def test_finitestatemachines::initialstate_constructor_exists():
    assert callable(finitestatemachines::InitialState.__init__)


def test_finitestatemachines::initialstate_constructor_args():
    sig = inspect.signature(finitestatemachines::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_finitestatemachines::finalstate_is_not_abstract():
    assert not inspect.isabstract(finitestatemachines::FinalState)


def test_finitestatemachines::finalstate_constructor_exists():
    assert callable(finitestatemachines::FinalState.__init__)


def test_finitestatemachines::finalstate_constructor_args():
    sig = inspect.signature(finitestatemachines::FinalState.__init__)
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
finitestatemachines::Join2_strategy = st.builds(
    finitestatemachines::Join2,
)
finitestatemachines::Fork_strategy = st.builds(
    finitestatemachines::Fork,
)
Transition2_strategy = st.builds(
    Transition2,
)
finitestatemachines::TimedTransition_strategy = st.builds(
    finitestatemachines::TimedTransition,
    duration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
finitestatemachines::Transition2_strategy = st.builds(
    finitestatemachines::Transition2,
    initialTime=
        st.integers(),
    finalTime2=
        st.integers()
)
finitestatemachines::State2_strategy = st.builds(
    finitestatemachines::State2,
    finalTime=
        st.integers(),
    initialTime2=
        st.integers()
)
finitestatemachines::StateMachine_strategy = st.builds(
    finitestatemachines::StateMachine,
)
finitestatemachines::NamedElement_strategy = st.builds(
    finitestatemachines::NamedElement,
    name=
        safe_text
)
finitestatemachines::Trigger2_strategy = st.builds(
    finitestatemachines::Trigger2,
    expression=
        safe_text
)
State2_strategy = st.builds(
    State2,
)
finitestatemachines::Pseudostate_strategy = st.builds(
    finitestatemachines::Pseudostate,
)
finitestatemachines::InitialState_strategy = st.builds(
    finitestatemachines::InitialState,
)
finitestatemachines::FinalState_strategy = st.builds(
    finitestatemachines::FinalState,
)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=finitestatemachines::Join2_strategy)
@settings(max_examples=50)
def test_finitestatemachines::join2_instantiation(instance):
    assert isinstance(instance, finitestatemachines::Join2)

@given(instance=finitestatemachines::Fork_strategy)
@settings(max_examples=50)
def test_finitestatemachines::fork_instantiation(instance):
    assert isinstance(instance, finitestatemachines::Fork)

@given(instance=Transition2_strategy)
@settings(max_examples=50)
def test_transition2_instantiation(instance):
    assert isinstance(instance, Transition2)

@given(instance=finitestatemachines::TimedTransition_strategy)
@settings(max_examples=50)
def test_finitestatemachines::timedtransition_instantiation(instance):
    assert isinstance(instance, finitestatemachines::TimedTransition)

@given(instance=finitestatemachines::TimedTransition_strategy)
def test_finitestatemachines::timedtransition_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=finitestatemachines::TimedTransition_strategy)
def test_finitestatemachines::timedtransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=finitestatemachines::Transition2_strategy)
@settings(max_examples=50)
def test_finitestatemachines::transition2_instantiation(instance):
    assert isinstance(instance, finitestatemachines::Transition2)

@given(instance=finitestatemachines::Transition2_strategy)
def test_finitestatemachines::transition2_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=finitestatemachines::Transition2_strategy)
def test_finitestatemachines::transition2_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=finitestatemachines::Transition2_strategy)
def test_finitestatemachines::transition2_finalTime2_type(instance):
    assert isinstance(instance.finalTime2, int)


@given(instance=finitestatemachines::Transition2_strategy)
def test_finitestatemachines::transition2_finalTime2_setter(instance):
    original = instance.finalTime2
    instance.finalTime2 = original
    assert instance.finalTime2 == original

@given(instance=finitestatemachines::State2_strategy)
@settings(max_examples=50)
def test_finitestatemachines::state2_instantiation(instance):
    assert isinstance(instance, finitestatemachines::State2)

@given(instance=finitestatemachines::State2_strategy)
def test_finitestatemachines::state2_finalTime_type(instance):
    assert isinstance(instance.finalTime, int)


@given(instance=finitestatemachines::State2_strategy)
def test_finitestatemachines::state2_finalTime_setter(instance):
    original = instance.finalTime
    instance.finalTime = original
    assert instance.finalTime == original

@given(instance=finitestatemachines::State2_strategy)
def test_finitestatemachines::state2_initialTime2_type(instance):
    assert isinstance(instance.initialTime2, int)


@given(instance=finitestatemachines::State2_strategy)
def test_finitestatemachines::state2_initialTime2_setter(instance):
    original = instance.initialTime2
    instance.initialTime2 = original
    assert instance.initialTime2 == original

@given(instance=finitestatemachines::StateMachine_strategy)
@settings(max_examples=50)
def test_finitestatemachines::statemachine_instantiation(instance):
    assert isinstance(instance, finitestatemachines::StateMachine)

@given(instance=finitestatemachines::NamedElement_strategy)
@settings(max_examples=50)
def test_finitestatemachines::namedelement_instantiation(instance):
    assert isinstance(instance, finitestatemachines::NamedElement)

@given(instance=finitestatemachines::NamedElement_strategy)
def test_finitestatemachines::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=finitestatemachines::NamedElement_strategy)
def test_finitestatemachines::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finitestatemachines::Trigger2_strategy)
@settings(max_examples=50)
def test_finitestatemachines::trigger2_instantiation(instance):
    assert isinstance(instance, finitestatemachines::Trigger2)

@given(instance=finitestatemachines::Trigger2_strategy)
def test_finitestatemachines::trigger2_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=finitestatemachines::Trigger2_strategy)
def test_finitestatemachines::trigger2_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=State2_strategy)
@settings(max_examples=50)
def test_state2_instantiation(instance):
    assert isinstance(instance, State2)

@given(instance=finitestatemachines::Pseudostate_strategy)
@settings(max_examples=50)
def test_finitestatemachines::pseudostate_instantiation(instance):
    assert isinstance(instance, finitestatemachines::Pseudostate)

@given(instance=finitestatemachines::InitialState_strategy)
@settings(max_examples=50)
def test_finitestatemachines::initialstate_instantiation(instance):
    assert isinstance(instance, finitestatemachines::InitialState)

@given(instance=finitestatemachines::FinalState_strategy)
@settings(max_examples=50)
def test_finitestatemachines::finalstate_instantiation(instance):
    assert isinstance(instance, finitestatemachines::FinalState)
