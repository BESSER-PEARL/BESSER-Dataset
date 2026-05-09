import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSM::AbstractState,
    FSM::Transition,
    FSM::StateMachine,
    AbstractState,
    FSM::RegularState,
    FSM::InitialState,
    FSM::CompositeState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(FSM::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(FSM::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "genBy" in params, "Missing parameter 'genBy'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::abstractstate_has_genBy():
    assert hasattr(FSM::AbstractState, "genBy")
    descriptor = None
    for klass in FSM::AbstractState.__mro__:
        if "genBy" in klass.__dict__:
            descriptor = klass.__dict__["genBy"]
            break
    assert isinstance(descriptor, property)

def test_fsm::abstractstate_has_name():
    assert hasattr(FSM::AbstractState, "name")
    descriptor = None
    for klass in FSM::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "genBy" in params, "Missing parameter 'genBy'"

def test_fsm::transition_has_label():
    assert hasattr(FSM::Transition, "label")
    descriptor = None
    for klass in FSM::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_genBy():
    assert hasattr(FSM::Transition, "genBy")
    descriptor = None
    for klass in FSM::Transition.__mro__:
        if "genBy" in klass.__dict__:
            descriptor = klass.__dict__["genBy"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(FSM::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(FSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "genBy" in params, "Missing parameter 'genBy'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::statemachine_has_genBy():
    assert hasattr(FSM::StateMachine, "genBy")
    descriptor = None
    for klass in FSM::StateMachine.__mro__:
        if "genBy" in klass.__dict__:
            descriptor = klass.__dict__["genBy"]
            break
    assert isinstance(descriptor, property)

def test_fsm::statemachine_has_name():
    assert hasattr(FSM::StateMachine, "name")
    descriptor = None
    for klass in FSM::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(FSM::RegularState)


def test_fsm::regularstate_constructor_exists():
    assert callable(FSM::RegularState.__init__)


def test_fsm::regularstate_constructor_args():
    sig = inspect.signature(FSM::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(FSM::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(FSM::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(FSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(FSM::CompositeState)


def test_fsm::compositestate_constructor_exists():
    assert callable(FSM::CompositeState.__init__)


def test_fsm::compositestate_constructor_args():
    sig = inspect.signature(FSM::CompositeState.__init__)
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
FSM::AbstractState_strategy = st.builds(
    FSM::AbstractState,
    genBy=
        safe_text,
    name=
        safe_text
)
FSM::Transition_strategy = st.builds(
    FSM::Transition,
    label=
        safe_text,
    genBy=
        safe_text
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
    genBy=
        safe_text,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
FSM::RegularState_strategy = st.builds(
    FSM::RegularState,
)
FSM::InitialState_strategy = st.builds(
    FSM::InitialState,
)
FSM::CompositeState_strategy = st.builds(
    FSM::CompositeState,
)

@given(instance=FSM::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, FSM::AbstractState)

@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_genBy_type(instance):
    assert isinstance(instance.genBy, str)


@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_genBy_setter(instance):
    original = instance.genBy
    instance.genBy = original
    assert instance.genBy == original

@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)

@given(instance=FSM::Transition_strategy)
def test_fsm::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=FSM::Transition_strategy)
def test_fsm::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=FSM::Transition_strategy)
def test_fsm::transition_genBy_type(instance):
    assert isinstance(instance.genBy, str)


@given(instance=FSM::Transition_strategy)
def test_fsm::transition_genBy_setter(instance):
    original = instance.genBy
    instance.genBy = original
    assert instance.genBy == original

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_genBy_type(instance):
    assert isinstance(instance.genBy, str)


@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_genBy_setter(instance):
    original = instance.genBy
    instance.genBy = original
    assert instance.genBy == original

@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=FSM::RegularState_strategy)
@settings(max_examples=50)
def test_fsm::regularstate_instantiation(instance):
    assert isinstance(instance, FSM::RegularState)

@given(instance=FSM::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, FSM::InitialState)

@given(instance=FSM::CompositeState_strategy)
@settings(max_examples=50)
def test_fsm::compositestate_instantiation(instance):
    assert isinstance(instance, FSM::CompositeState)
