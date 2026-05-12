import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine103_Action,
    StateMachineObject,
    statemachine103_State,
    statemachine103_Transition,
    State,
    statemachine103_InitialState,
    statemachine103_FinalState,
    statemachine103_NormalState,
    statemachine103_StateMachineObject,
    statemachine103_StateMachine,
    statemachine103_StateMachineVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine103_action_is_not_abstract():
    assert not inspect.isabstract(statemachine103_Action)


def test_statemachine103_action_constructor_exists():
    assert callable(statemachine103_Action.__init__)


def test_statemachine103_action_constructor_args():
    sig = inspect.signature(statemachine103_Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_statemachine103_action_has_actionLabel():
    assert hasattr(statemachine103_Action, "actionLabel")
    descriptor = None
    for klass in statemachine103_Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103_action_has_actionStatement():
    assert hasattr(statemachine103_Action, "actionStatement")
    descriptor = None
    for klass in statemachine103_Action.__mro__:
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



def test_statemachine103_state_is_not_abstract():
    assert not inspect.isabstract(statemachine103_State)


def test_statemachine103_state_constructor_exists():
    assert callable(statemachine103_State.__init__)


def test_statemachine103_state_constructor_args():
    sig = inspect.signature(statemachine103_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine103_state_has_id():
    assert hasattr(statemachine103_State, "id")
    descriptor = None
    for klass in statemachine103_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine103_Transition)


def test_statemachine103_transition_constructor_exists():
    assert callable(statemachine103_Transition.__init__)


def test_statemachine103_transition_constructor_args():
    sig = inspect.signature(statemachine103_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"

def test_statemachine103_transition_has_guardLabel():
    assert hasattr(statemachine103_Transition, "guardLabel")
    descriptor = None
    for klass in statemachine103_Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103_transition_has_guardExpression():
    assert hasattr(statemachine103_Transition, "guardExpression")
    descriptor = None
    for klass in statemachine103_Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103_InitialState)


def test_statemachine103_initialstate_constructor_exists():
    assert callable(statemachine103_InitialState.__init__)


def test_statemachine103_initialstate_constructor_args():
    sig = inspect.signature(statemachine103_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103_FinalState)


def test_statemachine103_finalstate_constructor_exists():
    assert callable(statemachine103_FinalState.__init__)


def test_statemachine103_finalstate_constructor_args():
    sig = inspect.signature(statemachine103_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103_normalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine103_NormalState)


def test_statemachine103_normalstate_constructor_exists():
    assert callable(statemachine103_NormalState.__init__)


def test_statemachine103_normalstate_constructor_args():
    sig = inspect.signature(statemachine103_NormalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine103_statemachineobject_is_not_abstract():
    assert not inspect.isabstract(statemachine103_StateMachineObject)


def test_statemachine103_statemachineobject_constructor_exists():
    assert callable(statemachine103_StateMachineObject.__init__)


def test_statemachine103_statemachineobject_constructor_args():
    sig = inspect.signature(statemachine103_StateMachineObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_statemachine103_statemachineobject_has_label():
    assert hasattr(statemachine103_StateMachineObject, "label")
    descriptor = None
    for klass in statemachine103_StateMachineObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine103_StateMachine)


def test_statemachine103_statemachine_constructor_exists():
    assert callable(statemachine103_StateMachine.__init__)


def test_statemachine103_statemachine_constructor_args():
    sig = inspect.signature(statemachine103_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_statemachine103_statemachine_has_label():
    assert hasattr(statemachine103_StateMachine, "label")
    descriptor = None
    for klass in statemachine103_StateMachine.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_statemachine103_statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(statemachine103_StateMachineVariable)


def test_statemachine103_statemachinevariable_constructor_exists():
    assert callable(statemachine103_StateMachineVariable.__init__)


def test_statemachine103_statemachinevariable_constructor_args():
    sig = inspect.signature(statemachine103_StateMachineVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine103_statemachinevariable_has_type():
    assert hasattr(statemachine103_StateMachineVariable, "type")
    descriptor = None
    for klass in statemachine103_StateMachineVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statemachine103_statemachinevariable_has_name():
    assert hasattr(statemachine103_StateMachineVariable, "name")
    descriptor = None
    for klass in statemachine103_StateMachineVariable.__mro__:
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
statemachine103_Action_strategy = st.builds(
    statemachine103_Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
StateMachineObject_strategy = st.builds(
    StateMachineObject,
)
statemachine103_State_strategy = st.builds(
    statemachine103_State,
    id=
        st.integers()
)
statemachine103_Transition_strategy = st.builds(
    statemachine103_Transition,
    guardLabel=
        safe_text,
    guardExpression=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine103_InitialState_strategy = st.builds(
    statemachine103_InitialState,
)
statemachine103_FinalState_strategy = st.builds(
    statemachine103_FinalState,
)
statemachine103_NormalState_strategy = st.builds(
    statemachine103_NormalState,
)
statemachine103_StateMachineObject_strategy = st.builds(
    statemachine103_StateMachineObject,
    label=
        safe_text
)
statemachine103_StateMachine_strategy = st.builds(
    statemachine103_StateMachine,
    label=
        safe_text
)
statemachine103_StateMachineVariable_strategy = st.builds(
    statemachine103_StateMachineVariable,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=statemachine103_Action_strategy)
@settings(max_examples=50)
def test_statemachine103_action_instantiation(instance):
    assert isinstance(instance, statemachine103_Action)



@given(instance=statemachine103_Action_strategy)
def test_statemachine103_action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=statemachine103_Action_strategy)
def test_statemachine103_action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachineobject_instantiation(instance):
    assert isinstance(instance, StateMachineObject)

@given(instance=statemachine103_State_strategy)
@settings(max_examples=50)
def test_statemachine103_state_instantiation(instance):
    assert isinstance(instance, statemachine103_State)



@given(instance=statemachine103_State_strategy)
def test_statemachine103_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine103_Transition_strategy)
@settings(max_examples=50)
def test_statemachine103_transition_instantiation(instance):
    assert isinstance(instance, statemachine103_Transition)



@given(instance=statemachine103_Transition_strategy)
def test_statemachine103_transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original



@given(instance=statemachine103_Transition_strategy)
def test_statemachine103_transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine103_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine103_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine103_InitialState)

@given(instance=statemachine103_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine103_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine103_FinalState)

@given(instance=statemachine103_NormalState_strategy)
@settings(max_examples=50)
def test_statemachine103_normalstate_instantiation(instance):
    assert isinstance(instance, statemachine103_NormalState)

@given(instance=statemachine103_StateMachineObject_strategy)
@settings(max_examples=50)
def test_statemachine103_statemachineobject_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachineObject)



@given(instance=statemachine103_StateMachineObject_strategy)
def test_statemachine103_statemachineobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statemachine103_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine103_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachine)



@given(instance=statemachine103_StateMachine_strategy)
def test_statemachine103_statemachine_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statemachine103_StateMachineVariable_strategy)
@settings(max_examples=50)
def test_statemachine103_statemachinevariable_instantiation(instance):
    assert isinstance(instance, statemachine103_StateMachineVariable)



@given(instance=statemachine103_StateMachineVariable_strategy)
def test_statemachine103_statemachinevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statemachine103_StateMachineVariable_strategy)
def test_statemachine103_statemachinevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
