import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    statemachine_StateMachineDescription,
    AbstractState,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_State,
    Behaviour,
    StateMachineDescription,
    statemachine_Region,
    statemachine_StateMachine,
    ObeoDSMObject,
    statemachine_Transition,
    statemachine_AbstractState,
    statemachine_NamedElement,
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



def test_statemachine_statemachinedescription_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachineDescription)


def test_statemachine_statemachinedescription_constructor_exists():
    assert callable(statemachine_StateMachineDescription.__init__)


def test_statemachine_statemachinedescription_constructor_args():
    sig = inspect.signature(statemachine_StateMachineDescription.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
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



def test_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(statemachine_Region)


def test_statemachine_region_constructor_exists():
    assert callable(statemachine_Region.__init__)


def test_statemachine_region_constructor_args():
    sig = inspect.signature(statemachine_Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_obeodsmobject_is_not_abstract():
    assert not inspect.isabstract(ObeoDSMObject)


def test_obeodsmobject_constructor_exists():
    assert callable(ObeoDSMObject.__init__)


def test_obeodsmobject_constructor_args():
    sig = inspect.signature(ObeoDSMObject.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_statemachine_transition_has_guard():
    assert hasattr(statemachine_Transition, "guard")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractState)


def test_statemachine_abstractstate_constructor_exists():
    assert callable(statemachine_AbstractState.__init__)


def test_statemachine_abstractstate_constructor_args():
    sig = inspect.signature(statemachine_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine_NamedElement)


def test_statemachine_namedelement_constructor_exists():
    assert callable(statemachine_NamedElement.__init__)


def test_statemachine_namedelement_constructor_args():
    sig = inspect.signature(statemachine_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_namedelement_has_name():
    assert hasattr(statemachine_NamedElement, "name")
    descriptor = None
    for klass in statemachine_NamedElement.__mro__:
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
statemachine_StateMachineDescription_strategy = st.builds(
    statemachine_StateMachineDescription,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
Behaviour_strategy = st.builds(
    Behaviour,
)
StateMachineDescription_strategy = st.builds(
    StateMachineDescription,
)
statemachine_Region_strategy = st.builds(
    statemachine_Region,
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)
ObeoDSMObject_strategy = st.builds(
    ObeoDSMObject,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    guard=
        safe_text
)
statemachine_AbstractState_strategy = st.builds(
    statemachine_AbstractState,
)
statemachine_NamedElement_strategy = st.builds(
    statemachine_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachine_StateMachineDescription_strategy)
@settings(max_examples=50)
def test_statemachine_statemachinedescription_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachineDescription)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)

@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)

@given(instance=Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_instantiation(instance):
    assert isinstance(instance, Behaviour)

@given(instance=StateMachineDescription_strategy)
@settings(max_examples=50)
def test_statemachinedescription_instantiation(instance):
    assert isinstance(instance, StateMachineDescription)

@given(instance=statemachine_Region_strategy)
@settings(max_examples=50)
def test_statemachine_region_instantiation(instance):
    assert isinstance(instance, statemachine_Region)

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)

@given(instance=ObeoDSMObject_strategy)
@settings(max_examples=50)
def test_obeodsmobject_instantiation(instance):
    assert isinstance(instance, ObeoDSMObject)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine_abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)

@given(instance=statemachine_NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine_namedelement_instantiation(instance):
    assert isinstance(instance, statemachine_NamedElement)



@given(instance=statemachine_NamedElement_strategy)
def test_statemachine_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
