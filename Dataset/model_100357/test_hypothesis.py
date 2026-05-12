import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSM::AssociationStateState,
    FSM::RootFolder,
    Transition,
    State,
    RootFolder,
    AssociationStateState,
    StateMachine,
    MgaObject,
    FSM::State,
    FSM::StateMachine,
    FSM::Transition,
    FSM::MgaObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::associationstatestate_is_not_abstract():
    assert not inspect.isabstract(FSM::AssociationStateState)


def test_fsm::associationstatestate_constructor_exists():
    assert callable(FSM::AssociationStateState.__init__)


def test_fsm::associationstatestate_constructor_args():
    sig = inspect.signature(FSM::AssociationStateState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::rootfolder_is_not_abstract():
    assert not inspect.isabstract(FSM::RootFolder)


def test_fsm::rootfolder_constructor_exists():
    assert callable(FSM::RootFolder.__init__)


def test_fsm::rootfolder_constructor_args():
    sig = inspect.signature(FSM::RootFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::rootfolder_has_name():
    assert hasattr(FSM::RootFolder, "name")
    descriptor = None
    for klass in FSM::RootFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_rootfolder_is_not_abstract():
    assert not inspect.isabstract(RootFolder)


def test_rootfolder_constructor_exists():
    assert callable(RootFolder.__init__)


def test_rootfolder_constructor_args():
    sig = inspect.signature(RootFolder.__init__)
    params = list(sig.parameters.keys())



def test_associationstatestate_is_not_abstract():
    assert not inspect.isabstract(AssociationStateState)


def test_associationstatestate_constructor_exists():
    assert callable(AssociationStateState.__init__)


def test_associationstatestate_constructor_args():
    sig = inspect.signature(AssociationStateState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_mgaobject_is_not_abstract():
    assert not inspect.isabstract(MgaObject)


def test_mgaobject_constructor_exists():
    assert callable(MgaObject.__init__)


def test_mgaobject_constructor_args():
    sig = inspect.signature(MgaObject.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(FSM::State)


def test_fsm::state_constructor_exists():
    assert callable(FSM::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(FSM::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(FSM::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(FSM::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::mgaobject_is_not_abstract():
    assert not inspect.isabstract(FSM::MgaObject)


def test_fsm::mgaobject_constructor_exists():
    assert callable(FSM::MgaObject.__init__)


def test_fsm::mgaobject_constructor_args():
    sig = inspect.signature(FSM::MgaObject.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::mgaobject_has_position():
    assert hasattr(FSM::MgaObject, "position")
    descriptor = None
    for klass in FSM::MgaObject.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_fsm::mgaobject_has_name():
    assert hasattr(FSM::MgaObject, "name")
    descriptor = None
    for klass in FSM::MgaObject.__mro__:
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
FSM::AssociationStateState_strategy = st.builds(
    FSM::AssociationStateState,
)
FSM::RootFolder_strategy = st.builds(
    FSM::RootFolder,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
State_strategy = st.builds(
    State,
)
RootFolder_strategy = st.builds(
    RootFolder,
)
AssociationStateState_strategy = st.builds(
    AssociationStateState,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
MgaObject_strategy = st.builds(
    MgaObject,
)
FSM::State_strategy = st.builds(
    FSM::State,
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
)
FSM::Transition_strategy = st.builds(
    FSM::Transition,
)
FSM::MgaObject_strategy = st.builds(
    FSM::MgaObject,
    position=
        safe_text,
    name=
        safe_text
)

@given(instance=FSM::AssociationStateState_strategy)
@settings(max_examples=50)
def test_fsm::associationstatestate_instantiation(instance):
    assert isinstance(instance, FSM::AssociationStateState)

@given(instance=FSM::RootFolder_strategy)
@settings(max_examples=50)
def test_fsm::rootfolder_instantiation(instance):
    assert isinstance(instance, FSM::RootFolder)

@given(instance=FSM::RootFolder_strategy)
def test_fsm::rootfolder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::RootFolder_strategy)
def test_fsm::rootfolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=RootFolder_strategy)
@settings(max_examples=50)
def test_rootfolder_instantiation(instance):
    assert isinstance(instance, RootFolder)

@given(instance=AssociationStateState_strategy)
@settings(max_examples=50)
def test_associationstatestate_instantiation(instance):
    assert isinstance(instance, AssociationStateState)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=MgaObject_strategy)
@settings(max_examples=50)
def test_mgaobject_instantiation(instance):
    assert isinstance(instance, MgaObject)

@given(instance=FSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, FSM::State)

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)

@given(instance=FSM::MgaObject_strategy)
@settings(max_examples=50)
def test_fsm::mgaobject_instantiation(instance):
    assert isinstance(instance, FSM::MgaObject)

@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
