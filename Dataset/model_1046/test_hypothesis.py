import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FSM_AssociationStateState,
    FSM_RootFolder,
    FSM_MgaObject,
    MgaObject,
    FSM_StateMachine,
    FSM_State,
    FSM_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_associationstatestate_is_not_abstract():
    assert not inspect.isabstract(FSM_AssociationStateState)


def test_fsm_associationstatestate_constructor_exists():
    assert callable(FSM_AssociationStateState.__init__)


def test_fsm_associationstatestate_constructor_args():
    sig = inspect.signature(FSM_AssociationStateState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_rootfolder_is_not_abstract():
    assert not inspect.isabstract(FSM_RootFolder)


def test_fsm_rootfolder_constructor_exists():
    assert callable(FSM_RootFolder.__init__)


def test_fsm_rootfolder_constructor_args():
    sig = inspect.signature(FSM_RootFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_rootfolder_has_name():
    assert hasattr(FSM_RootFolder, "name")
    descriptor = None
    for klass in FSM_RootFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_mgaobject_is_not_abstract():
    assert not inspect.isabstract(FSM_MgaObject)


def test_fsm_mgaobject_constructor_exists():
    assert callable(FSM_MgaObject.__init__)


def test_fsm_mgaobject_constructor_args():
    sig = inspect.signature(FSM_MgaObject.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_mgaobject_has_position():
    assert hasattr(FSM_MgaObject, "position")
    descriptor = None
    for klass in FSM_MgaObject.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_fsm_mgaobject_has_name():
    assert hasattr(FSM_MgaObject, "name")
    descriptor = None
    for klass in FSM_MgaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mgaobject_is_not_abstract():
    assert not inspect.isabstract(MgaObject)


def test_mgaobject_constructor_exists():
    assert callable(MgaObject.__init__)


def test_mgaobject_constructor_args():
    sig = inspect.signature(MgaObject.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(FSM_State)


def test_fsm_state_constructor_exists():
    assert callable(FSM_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(FSM_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
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
FSM_AssociationStateState_strategy = st.builds(
    FSM_AssociationStateState,
)
FSM_RootFolder_strategy = st.builds(
    FSM_RootFolder,
    name=
        safe_text
)
FSM_MgaObject_strategy = st.builds(
    FSM_MgaObject,
    position=
        safe_text,
    name=
        safe_text
)
MgaObject_strategy = st.builds(
    MgaObject,
)
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
)
FSM_State_strategy = st.builds(
    FSM_State,
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
)

@given(instance=FSM_AssociationStateState_strategy)
@settings(max_examples=50)
def test_fsm_associationstatestate_instantiation(instance):
    assert isinstance(instance, FSM_AssociationStateState)

@given(instance=FSM_RootFolder_strategy)
@settings(max_examples=50)
def test_fsm_rootfolder_instantiation(instance):
    assert isinstance(instance, FSM_RootFolder)



@given(instance=FSM_RootFolder_strategy)
def test_fsm_rootfolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_MgaObject_strategy)
@settings(max_examples=50)
def test_fsm_mgaobject_instantiation(instance):
    assert isinstance(instance, FSM_MgaObject)



@given(instance=FSM_MgaObject_strategy)
def test_fsm_mgaobject_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=FSM_MgaObject_strategy)
def test_fsm_mgaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MgaObject_strategy)
@settings(max_examples=50)
def test_mgaobject_instantiation(instance):
    assert isinstance(instance, MgaObject)

@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)

@given(instance=FSM_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, FSM_State)

@given(instance=FSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)
