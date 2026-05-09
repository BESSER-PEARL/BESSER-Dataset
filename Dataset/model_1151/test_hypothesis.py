import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    myFirstEditorCustom::EndState,
    myFirstEditorCustom::StartState,
    myFirstEditorCustom::Transition,
    myFirstEditorCustom::State,
    myFirstEditorCustom::StateMachine,
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



def test_myfirsteditorcustom::endstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom::EndState)


def test_myfirsteditorcustom::endstate_constructor_exists():
    assert callable(myFirstEditorCustom::EndState.__init__)


def test_myfirsteditorcustom::endstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom::EndState.__init__)
    params = list(sig.parameters.keys())



def test_myfirsteditorcustom::startstate_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom::StartState)


def test_myfirsteditorcustom::startstate_constructor_exists():
    assert callable(myFirstEditorCustom::StartState.__init__)


def test_myfirsteditorcustom::startstate_constructor_args():
    sig = inspect.signature(myFirstEditorCustom::StartState.__init__)
    params = list(sig.parameters.keys())



def test_myfirsteditorcustom::transition_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom::Transition)


def test_myfirsteditorcustom::transition_constructor_exists():
    assert callable(myFirstEditorCustom::Transition.__init__)


def test_myfirsteditorcustom::transition_constructor_args():
    sig = inspect.signature(myFirstEditorCustom::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfirsteditorcustom::transition_has_name():
    assert hasattr(myFirstEditorCustom::Transition, "name")
    descriptor = None
    for klass in myFirstEditorCustom::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myfirsteditorcustom::state_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom::State)


def test_myfirsteditorcustom::state_constructor_exists():
    assert callable(myFirstEditorCustom::State.__init__)


def test_myfirsteditorcustom::state_constructor_args():
    sig = inspect.signature(myFirstEditorCustom::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_myfirsteditorcustom::state_has_name():
    assert hasattr(myFirstEditorCustom::State, "name")
    descriptor = None
    for klass in myFirstEditorCustom::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_myfirsteditorcustom::state_has_type():
    assert hasattr(myFirstEditorCustom::State, "type")
    descriptor = None
    for klass in myFirstEditorCustom::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_myfirsteditorcustom::statemachine_is_not_abstract():
    assert not inspect.isabstract(myFirstEditorCustom::StateMachine)


def test_myfirsteditorcustom::statemachine_constructor_exists():
    assert callable(myFirstEditorCustom::StateMachine.__init__)


def test_myfirsteditorcustom::statemachine_constructor_args():
    sig = inspect.signature(myFirstEditorCustom::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfirsteditorcustom::statemachine_has_name():
    assert hasattr(myFirstEditorCustom::StateMachine, "name")
    descriptor = None
    for klass in myFirstEditorCustom::StateMachine.__mro__:
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
myFirstEditorCustom::EndState_strategy = st.builds(
    myFirstEditorCustom::EndState,
)
myFirstEditorCustom::StartState_strategy = st.builds(
    myFirstEditorCustom::StartState,
)
myFirstEditorCustom::Transition_strategy = st.builds(
    myFirstEditorCustom::Transition,
    name=
        safe_text
)
myFirstEditorCustom::State_strategy = st.builds(
    myFirstEditorCustom::State,
    name=
        safe_text,
    type=
        safe_text
)
myFirstEditorCustom::StateMachine_strategy = st.builds(
    myFirstEditorCustom::StateMachine,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=myFirstEditorCustom::EndState_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom::endstate_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom::EndState)

@given(instance=myFirstEditorCustom::StartState_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom::startstate_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom::StartState)

@given(instance=myFirstEditorCustom::Transition_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom::transition_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom::Transition)

@given(instance=myFirstEditorCustom::Transition_strategy)
def test_myfirsteditorcustom::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myFirstEditorCustom::Transition_strategy)
def test_myfirsteditorcustom::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myFirstEditorCustom::State_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom::state_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom::State)

@given(instance=myFirstEditorCustom::State_strategy)
def test_myfirsteditorcustom::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myFirstEditorCustom::State_strategy)
def test_myfirsteditorcustom::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myFirstEditorCustom::State_strategy)
def test_myfirsteditorcustom::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myFirstEditorCustom::State_strategy)
def test_myfirsteditorcustom::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myFirstEditorCustom::StateMachine_strategy)
@settings(max_examples=50)
def test_myfirsteditorcustom::statemachine_instantiation(instance):
    assert isinstance(instance, myFirstEditorCustom::StateMachine)

@given(instance=myFirstEditorCustom::StateMachine_strategy)
def test_myfirsteditorcustom::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myFirstEditorCustom::StateMachine_strategy)
def test_myfirsteditorcustom::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
