import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSM::AssociationStateState,
    FSM::RootFolder,
    FSM::MgaObject,
    MgaObject,
    FSM::StateMachine,
    FSM::State,
    FSM::Transition,
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



def test_fsm::mgaobject_is_not_abstract():
    assert not inspect.isabstract(FSM::MgaObject)


def test_fsm::mgaobject_constructor_exists():
    assert callable(FSM::MgaObject.__init__)


def test_fsm::mgaobject_constructor_args():
    sig = inspect.signature(FSM::MgaObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "position" in params, "Missing parameter 'position'"

def test_fsm::mgaobject_has_name():
    assert hasattr(FSM::MgaObject, "name")
    descriptor = None
    for klass in FSM::MgaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::mgaobject_has_position():
    assert hasattr(FSM::MgaObject, "position")
    descriptor = None
    for klass in FSM::MgaObject.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_mgaobject_is_not_abstract():
    assert not inspect.isabstract(MgaObject)


def test_mgaobject_constructor_exists():
    assert callable(MgaObject.__init__)


def test_mgaobject_constructor_args():
    sig = inspect.signature(MgaObject.__init__)
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



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
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
FSM::AssociationStateState_strategy = st.builds(
    FSM::AssociationStateState,
)
FSM::RootFolder_strategy = st.builds(
    FSM::RootFolder,
    name=
        safe_text
)
FSM::MgaObject_strategy = st.builds(
    FSM::MgaObject,
    name=
        safe_text,
    position=
        safe_text
)
MgaObject_strategy = st.builds(
    MgaObject,
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
)
FSM::State_strategy = st.builds(
    FSM::State,
)
FSM::Transition_strategy = st.builds(
    FSM::Transition,
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

@given(instance=FSM::MgaObject_strategy)
@settings(max_examples=50)
def test_fsm::mgaobject_instantiation(instance):
    assert isinstance(instance, FSM::MgaObject)

@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=FSM::MgaObject_strategy)
def test_fsm::mgaobject_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=MgaObject_strategy)
@settings(max_examples=50)
def test_mgaobject_instantiation(instance):
    assert isinstance(instance, MgaObject)

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, FSM::State)

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)
