import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    FSM::StateMachine,
    FSM::State,
    FSM::FSMModel,
    FSM::Transition,
    FSM::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(FSM::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(FSM::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(FSM::State)


def test_fsm::state_constructor_exists():
    assert callable(FSM::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(FSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_fsm::state_has_isFinal():
    assert hasattr(FSM::State, "isFinal")
    descriptor = None
    for klass in FSM::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fsmmodel_is_not_abstract():
    assert not inspect.isabstract(FSM::FSMModel)


def test_fsm::fsmmodel_constructor_exists():
    assert callable(FSM::FSMModel.__init__)


def test_fsm::fsmmodel_constructor_args():
    sig = inspect.signature(FSM::FSMModel.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_fsm::transition_has_input():
    assert hasattr(FSM::Transition, "input")
    descriptor = None
    for klass in FSM::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_output():
    assert hasattr(FSM::Transition, "output")
    descriptor = None
    for klass in FSM::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(FSM::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(FSM::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(FSM::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(FSM::NamedElement, "name")
    descriptor = None
    for klass in FSM::NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
)
FSM::State_strategy = st.builds(
    FSM::State,
    isFinal=
        st.booleans()
)
FSM::FSMModel_strategy = st.builds(
    FSM::FSMModel,
)
FSM::Transition_strategy = st.builds(
    FSM::Transition,
    input=
        safe_text,
    output=
        safe_text
)
FSM::NamedElement_strategy = st.builds(
    FSM::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, FSM::State)

@given(instance=FSM::State_strategy)
def test_fsm::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=FSM::State_strategy)
def test_fsm::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=FSM::FSMModel_strategy)
@settings(max_examples=50)
def test_fsm::fsmmodel_instantiation(instance):
    assert isinstance(instance, FSM::FSMModel)

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)

@given(instance=FSM::Transition_strategy)
def test_fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=FSM::Transition_strategy)
def test_fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=FSM::Transition_strategy)
def test_fsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=FSM::Transition_strategy)
def test_fsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=FSM::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, FSM::NamedElement)

@given(instance=FSM::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
