import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    statemachine::StateMachineDescription,
    AbstractState,
    statemachine::FinalState,
    statemachine::InitialState,
    statemachine::State,
    Behaviour,
    StateMachineDescription,
    statemachine::Region,
    statemachine::StateMachine,
    ObeoDSMObject,
    statemachine::AbstractState,
    statemachine::Transition,
    statemachine::NamedElement,
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



def test_statemachine::statemachinedescription_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachineDescription)


def test_statemachine::statemachinedescription_constructor_exists():
    assert callable(statemachine::StateMachineDescription.__init__)


def test_statemachine::statemachinedescription_constructor_args():
    sig = inspect.signature(statemachine::StateMachineDescription.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(statemachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(statemachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_is_not_abstract():
    assert not inspect.isabstract(Behaviour)


def test_behaviour_constructor_exists():
    assert callable(Behaviour.__init__)


def test_behaviour_constructor_args():
    sig = inspect.signature(Behaviour.__init__)
    params = list(sig.parameters.keys())



def test_statemachinedescription_is_not_abstract():
    assert not inspect.isabstract(StateMachineDescription)


def test_statemachinedescription_constructor_exists():
    assert callable(StateMachineDescription.__init__)


def test_statemachinedescription_constructor_args():
    sig = inspect.signature(StateMachineDescription.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::region_is_not_abstract():
    assert not inspect.isabstract(statemachine::Region)


def test_statemachine::region_constructor_exists():
    assert callable(statemachine::Region.__init__)


def test_statemachine::region_constructor_args():
    sig = inspect.signature(statemachine::Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_obeodsmobject_is_not_abstract():
    assert not inspect.isabstract(ObeoDSMObject)


def test_obeodsmobject_constructor_exists():
    assert callable(ObeoDSMObject.__init__)


def test_obeodsmobject_constructor_args():
    sig = inspect.signature(ObeoDSMObject.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::AbstractState)


def test_statemachine::abstractstate_constructor_exists():
    assert callable(statemachine::AbstractState.__init__)


def test_statemachine::abstractstate_constructor_args():
    sig = inspect.signature(statemachine::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_statemachine::transition_has_guard():
    assert hasattr(statemachine::Transition, "guard")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine::NamedElement)


def test_statemachine::namedelement_constructor_exists():
    assert callable(statemachine::NamedElement.__init__)


def test_statemachine::namedelement_constructor_args():
    sig = inspect.signature(statemachine::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::namedelement_has_name():
    assert hasattr(statemachine::NamedElement, "name")
    descriptor = None
    for klass in statemachine::NamedElement.__mro__:
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
statemachine::StateMachineDescription_strategy = st.builds(
    statemachine::StateMachineDescription,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
statemachine::InitialState_strategy = st.builds(
    statemachine::InitialState,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
)
Behaviour_strategy = st.builds(
    Behaviour,
)
StateMachineDescription_strategy = st.builds(
    StateMachineDescription,
)
statemachine::Region_strategy = st.builds(
    statemachine::Region,
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
)
ObeoDSMObject_strategy = st.builds(
    ObeoDSMObject,
)
statemachine::AbstractState_strategy = st.builds(
    statemachine::AbstractState,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    guard=
        safe_text
)
statemachine::NamedElement_strategy = st.builds(
    statemachine::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachine::StateMachineDescription_strategy)
@settings(max_examples=50)
def test_statemachine::statemachinedescription_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachineDescription)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=statemachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, statemachine::InitialState)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_instantiation(instance):
    assert isinstance(instance, Behaviour)

@given(instance=StateMachineDescription_strategy)
@settings(max_examples=50)
def test_statemachinedescription_instantiation(instance):
    assert isinstance(instance, StateMachineDescription)

@given(instance=statemachine::Region_strategy)
@settings(max_examples=50)
def test_statemachine::region_instantiation(instance):
    assert isinstance(instance, statemachine::Region)

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)

@given(instance=ObeoDSMObject_strategy)
@settings(max_examples=50)
def test_obeodsmobject_instantiation(instance):
    assert isinstance(instance, ObeoDSMObject)

@given(instance=statemachine::AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine::abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine::AbstractState)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=statemachine::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine::namedelement_instantiation(instance):
    assert isinstance(instance, statemachine::NamedElement)

@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
