import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine103::Action,
    StateMachineObject,
    statemachine103::State,
    statemachine103::Transition,
    State,
    statemachine103::InitialState,
    statemachine103::FinalState,
    statemachine103::NormalState,
    statemachine103::StateMachineObject,
    statemachine103::StateMachine,
    statemachine103::StateMachineVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine103::action_is_not_abstract():
    assert not inspect.isabstract(statemachine103::Action)


def test_statemachine103::action_constructor_exists():
    assert callable(statemachine103::Action.__init__)


def test_statemachine103::action_constructor_args():
    sig = inspect.signature(statemachine103::Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_statemachine103::action_has_actionLabel():
    assert hasattr(statemachine103::Action, "actionLabel")
    descriptor = None
    for klass in statemachine103::Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103::action_has_actionStatement():
    assert hasattr(statemachine103::Action, "actionStatement")
    descriptor = None
    for klass in statemachine103::Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)



def test_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(StateMachineObject)


def test_statemachineobject_constructor_exists():
    assert callable(StateMachineObject.__init__)


def test_statemachineobject_constructor_args():
    sig = inspect.signature(StateMachineObject.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103::state_is_not_abstract():
    assert not inspect.isabstract(statemachine103::State)


def test_statemachine103::state_constructor_exists():
    assert callable(statemachine103::State.__init__)


def test_statemachine103::state_constructor_args():
    sig = inspect.signature(statemachine103::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine103::state_has_id():
    assert hasattr(statemachine103::State, "id")
    descriptor = None
    for klass in statemachine103::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine103::Transition)


def test_statemachine103::transition_constructor_exists():
    assert callable(statemachine103::Transition.__init__)


def test_statemachine103::transition_constructor_args():
    sig = inspect.signature(statemachine103::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"

def test_statemachine103::transition_has_guardExpression():
    assert hasattr(statemachine103::Transition, "guardExpression")
    descriptor = None
    for klass in statemachine103::Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103::transition_has_guardLabel():
    assert hasattr(statemachine103::Transition, "guardLabel")
    descriptor = None
    for klass in statemachine103::Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103::initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103::InitialState)


def test_statemachine103::initialstate_constructor_exists():
    assert callable(statemachine103::InitialState.__init__)


def test_statemachine103::initialstate_constructor_args():
    sig = inspect.signature(statemachine103::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103::FinalState)


def test_statemachine103::finalstate_constructor_exists():
    assert callable(statemachine103::FinalState.__init__)


def test_statemachine103::finalstate_constructor_args():
    sig = inspect.signature(statemachine103::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103::normalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103::NormalState)


def test_statemachine103::normalstate_constructor_exists():
    assert callable(statemachine103::NormalState.__init__)


def test_statemachine103::normalstate_constructor_args():
    sig = inspect.signature(statemachine103::NormalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103::statemachineobject_is_not_abstract():
    assert not inspect.isabstract(statemachine103::StateMachineObject)


def test_statemachine103::statemachineobject_constructor_exists():
    assert callable(statemachine103::StateMachineObject.__init__)


def test_statemachine103::statemachineobject_constructor_args():
    sig = inspect.signature(statemachine103::StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_statemachine103::statemachineobject_has_label():
    assert hasattr(statemachine103::StateMachineObject, "label")
    descriptor = None
    for klass in statemachine103::StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine103::StateMachine)


def test_statemachine103::statemachine_constructor_exists():
    assert callable(statemachine103::StateMachine.__init__)


def test_statemachine103::statemachine_constructor_args():
    sig = inspect.signature(statemachine103::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_statemachine103::statemachine_has_label():
    assert hasattr(statemachine103::StateMachine, "label")
    descriptor = None
    for klass in statemachine103::StateMachine.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103::statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(statemachine103::StateMachineVariable)


def test_statemachine103::statemachinevariable_constructor_exists():
    assert callable(statemachine103::StateMachineVariable.__init__)


def test_statemachine103::statemachinevariable_constructor_args():
    sig = inspect.signature(statemachine103::StateMachineVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statemachine103::statemachinevariable_has_name():
    assert hasattr(statemachine103::StateMachineVariable, "name")
    descriptor = None
    for klass in statemachine103::StateMachineVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103::statemachinevariable_has_type():
    assert hasattr(statemachine103::StateMachineVariable, "type")
    descriptor = None
    for klass in statemachine103::StateMachineVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
statemachine103::Action_strategy = st.builds(
    statemachine103::Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
statemachine103::State_strategy = st.builds(
    statemachine103::State,
    id=
        st.integers()
)
statemachine103::Transition_strategy = st.builds(
    statemachine103::Transition,
    guardExpression=
        safe_text,
    guardLabel=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine103::InitialState_strategy = st.builds(
    statemachine103::InitialState,
)
statemachine103::FinalState_strategy = st.builds(
    statemachine103::FinalState,
)
statemachine103::NormalState_strategy = st.builds(
    statemachine103::NormalState,
)
statemachine103::StateMachineObject_strategy = st.builds(
    statemachine103::StateMachineObject,
    label=
        safe_text
)
statemachine103::StateMachine_strategy = st.builds(
    statemachine103::StateMachine,
    label=
        safe_text
)
statemachine103::StateMachineVariable_strategy = st.builds(
    statemachine103::StateMachineVariable,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=statemachine103::Action_strategy)
@settings(max_examples=50)
def test_statemachine103::action_instantiation(instance):
    assert isinstance(instance, statemachine103::Action)

@given(instance=statemachine103::Action_strategy)
def test_statemachine103::action_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=statemachine103::Action_strategy)
def test_statemachine103::action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=statemachine103::Action_strategy)
def test_statemachine103::action_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=statemachine103::Action_strategy)
def test_statemachine103::action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=statemachine103::State_strategy)
@settings(max_examples=50)
def test_statemachine103::state_instantiation(instance):
    assert isinstance(instance, statemachine103::State)

@given(instance=statemachine103::State_strategy)
def test_statemachine103::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=statemachine103::State_strategy)
def test_statemachine103::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine103::Transition_strategy)
@settings(max_examples=50)
def test_statemachine103::transition_instantiation(instance):
    assert isinstance(instance, statemachine103::Transition)

@given(instance=statemachine103::Transition_strategy)
def test_statemachine103::transition_guardExpression_type(instance):
    assert isinstance(instance.guardExpression, str)


@given(instance=statemachine103::Transition_strategy)
def test_statemachine103::transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=statemachine103::Transition_strategy)
def test_statemachine103::transition_guardLabel_type(instance):
    assert isinstance(instance.guardLabel, str)


@given(instance=statemachine103::Transition_strategy)
def test_statemachine103::transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine103::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine103::initialstate_instantiation(instance):
    assert isinstance(instance, statemachine103::InitialState)

@given(instance=statemachine103::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine103::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine103::FinalState)

@given(instance=statemachine103::NormalState_strategy)
@settings(max_examples=50)
def test_statemachine103::normalstate_instantiation(instance):
    assert isinstance(instance, statemachine103::NormalState)

@given(instance=statemachine103::StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachine103::statemachineobject_instantiation(instance):
    assert isinstance(instance, statemachine103::StateMachineObject)

@given(instance=statemachine103::StateMachineObject_strategy)
def test_statemachine103::statemachineobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statemachine103::StateMachineObject_strategy)
def test_statemachine103::statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statemachine103::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine103::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine103::StateMachine)

@given(instance=statemachine103::StateMachine_strategy)
def test_statemachine103::statemachine_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statemachine103::StateMachine_strategy)
def test_statemachine103::statemachine_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statemachine103::StateMachineVariable_strategy)
@settings(max_examples=50)
def test_statemachine103::statemachinevariable_instantiation(instance):
    assert isinstance(instance, statemachine103::StateMachineVariable)

@given(instance=statemachine103::StateMachineVariable_strategy)
def test_statemachine103::statemachinevariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine103::StateMachineVariable_strategy)
def test_statemachine103::statemachinevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine103::StateMachineVariable_strategy)
def test_statemachine103::statemachinevariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statemachine103::StateMachineVariable_strategy)
def test_statemachine103::statemachinevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
