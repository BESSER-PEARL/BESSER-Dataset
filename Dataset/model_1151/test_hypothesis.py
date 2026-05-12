import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    myFirstEditorCustom_EndState,
    myFirstEditorCustom_StartState,
    myFirstEditorCustom_Transition,
    myFirstEditorCustom_State,
    myFirstEditorCustom_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_myfirsteditorcustom_endstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_EndState)


def test_myfirsteditorcustom_endstate_constructor_exists():
    assert callable(myFirstEditorCustom_EndState.__init__)


def test_myfirsteditorcustom_endstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_EndState.__init__)
    params = list(sig.parameters.keys())



def test_myfirsteditorcustom_startstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_StartState)


def test_myfirsteditorcustom_startstate_constructor_exists():
    assert callable(myFirstEditorCustom_StartState.__init__)


def test_myfirsteditorcustom_startstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_StartState.__init__)
    params = list(sig.parameters.keys())



def test_myfirsteditorcustom_transition_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_Transition)


def test_myfirsteditorcustom_transition_constructor_exists():
    assert callable(myFirstEditorCustom_Transition.__init__)


def test_myfirsteditorcustom_transition_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfirsteditorcustom_transition_has_name():
    assert hasattr(myFirstEditorCustom_Transition, "name")
    descriptor = None
    for klass in myFirstEditorCustom_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myfirsteditorcustom_state_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_State)


def test_myfirsteditorcustom_state_constructor_exists():
    assert callable(myFirstEditorCustom_State.__init__)


def test_myfirsteditorcustom_state_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_myfirsteditorcustom_state_has_name():
    assert hasattr(myFirstEditorCustom_State, "name")
    descriptor = None
    for klass in myFirstEditorCustom_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_myfirsteditorcustom_state_has_type():
    assert hasattr(myFirstEditorCustom_State, "type")
    descriptor = None
    for klass in myFirstEditorCustom_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_myfirsteditorcustom_statemachine_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom_StateMachine)


def test_myfirsteditorcustom_statemachine_constructor_exists():
    assert callable(myFirstEditorCustom_StateMachine.__init__)


def test_myfirsteditorcustom_statemachine_constructor_args():
    sig = inspect.signature(myFirstEditorCustom_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfirsteditorcustom_statemachine_has_name():
    assert hasattr(myFirstEditorCustom_StateMachine, "name")
    descriptor = None
    for klass in myFirstEditorCustom_StateMachine.__mro__:
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
State_strategy = st.builds(
    State,
)
myFirstEditorCustom_EndState_strategy = st.builds(
    myFirstEditorCustom_EndState,
)
myFirstEditorCustom_StartState_strategy = st.builds(
    myFirstEditorCustom_StartState,
)
myFirstEditorCustom_Transition_strategy = st.builds(
    myFirstEditorCustom_Transition,
    name=
        safe_text
)
myFirstEditorCustom_State_strategy = st.builds(
    myFirstEditorCustom_State,
    name=
        safe_text,
    type=
        safe_text
)
myFirstEditorCustom_StateMachine_strategy = st.builds(
    myFirstEditorCustom_StateMachine,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=myFirstEditorCustom_EndState_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom_endstate_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_EndState)

@given(instance=myFirstEditorCustom_StartState_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom_startstate_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_StartState)

@given(instance=myFirstEditorCustom_Transition_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom_transition_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_Transition)



@given(instance=myFirstEditorCustom_Transition_strategy)
def test_myfirsteditorcustom_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myFirstEditorCustom_State_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom_state_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_State)



@given(instance=myFirstEditorCustom_State_strategy)
def test_myfirsteditorcustom_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myFirstEditorCustom_State_strategy)
def test_myfirsteditorcustom_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myFirstEditorCustom_StateMachine_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom_statemachine_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom_StateMachine)



@given(instance=myFirstEditorCustom_StateMachine_strategy)
def test_myfirsteditorcustom_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
