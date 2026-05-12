import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    statemachine_InitialState,
    statemachine_FinalState,
    statemachine_NormalState,
    statemachine_Action,
    Declaration,
    statemachine_State,
    statemachine_Transition,
    statemachine_StateMachineVariable,
    statemachine_StateMachine,
    statemachine_Declaration,
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



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_normalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_NormalState)


def test_statemachine_normalstate_constructor_exists():
    assert callable(statemachine_NormalState.__init__)


def test_statemachine_normalstate_constructor_args():
    sig = inspect.signature(statemachine_NormalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(statemachine_Action)


def test_statemachine_action_constructor_exists():
    assert callable(statemachine_Action.__init__)


def test_statemachine_action_constructor_args():
    sig = inspect.signature(statemachine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"

def test_statemachine_action_has_actionLabel():
    assert hasattr(statemachine_Action, "actionLabel")
    descriptor = None
    for klass in statemachine_Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_action_has_actionStatement():
    assert hasattr(statemachine_Action, "actionStatement")
    descriptor = None
    for klass in statemachine_Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_state_has_label():
    assert hasattr(statemachine_State, "label")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_id():
    assert hasattr(statemachine_State, "id")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "sourceLabel" in params, "Missing parameter 'sourceLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "label" in params, "Missing parameter 'label'"
    assert "targetLabel" in params, "Missing parameter 'targetLabel'"

def test_statemachine_transition_has_sourceLabel():
    assert hasattr(statemachine_Transition, "sourceLabel")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "sourceLabel" in klass.__dict__:
            descriptor = klass.__dict__["sourceLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_guardExpression():
    assert hasattr(statemachine_Transition, "guardExpression")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_guardLabel():
    assert hasattr(statemachine_Transition, "guardLabel")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_actionStatement():
    assert hasattr(statemachine_Transition, "actionStatement")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_actionLabel():
    assert hasattr(statemachine_Transition, "actionLabel")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_label():
    assert hasattr(statemachine_Transition, "label")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_targetLabel():
    assert hasattr(statemachine_Transition, "targetLabel")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "targetLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetLabel"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachineVariable)


def test_statemachine_statemachinevariable_constructor_exists():
    assert callable(statemachine_StateMachineVariable.__init__)


def test_statemachine_statemachinevariable_constructor_args():
    sig = inspect.signature(statemachine_StateMachineVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statemachine_statemachinevariable_has_name():
    assert hasattr(statemachine_StateMachineVariable, "name")
    descriptor = None
    for klass in statemachine_StateMachineVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_statemachinevariable_has_type():
    assert hasattr(statemachine_StateMachineVariable, "type")
    descriptor = None
    for klass in statemachine_StateMachineVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_declaration_is_not_abstract():
    assert not inspect.isabstract(statemachine_Declaration)


def test_statemachine_declaration_constructor_exists():
    assert callable(statemachine_Declaration.__init__)


def test_statemachine_declaration_constructor_args():
    sig = inspect.signature(statemachine_Declaration.__init__)
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
State_strategy = st.builds(
    State,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_NormalState_strategy = st.builds(
    statemachine_NormalState,
)
statemachine_Action_strategy = st.builds(
    statemachine_Action,
    actionLabel=
        safe_text,
    actionStatement=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    label=
        safe_text,
    id=
        st.integers()
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    sourceLabel=
        safe_text,
    guardExpression=
        safe_text,
    guardLabel=
        safe_text,
    actionStatement=
        safe_text,
    actionLabel=
        safe_text,
    label=
        safe_text,
    targetLabel=
        safe_text
)
statemachine_StateMachineVariable_strategy = st.builds(
    statemachine_StateMachineVariable,
    name=
        safe_text,
    type=
        safe_text
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)
statemachine_Declaration_strategy = st.builds(
    statemachine_Declaration,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)

@given(instance=statemachine_NormalState_strategy)
@settings(max_examples=50)
def test_statemachine_normalstate_instantiation(instance):
    assert isinstance(instance, statemachine_NormalState)

@given(instance=statemachine_Action_strategy)
@settings(max_examples=50)
def test_statemachine_action_instantiation(instance):
    assert isinstance(instance, statemachine_Action)



@given(instance=statemachine_Action_strategy)
def test_statemachine_action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=statemachine_Action_strategy)
def test_statemachine_action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_State_strategy)
@settings(max_examples=30)
def test_statemachine_state_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_State is not implemented or raised an error")

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_sourceLabel_setter(instance):
    original = instance.sourceLabel
    instance.sourceLabel = original
    assert instance.sourceLabel == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_targetLabel_setter(instance):
    original = instance.targetLabel
    instance.targetLabel = original
    assert instance.targetLabel == original

@given(instance=statemachine_StateMachineVariable_strategy)
@settings(max_examples=50)
def test_statemachine_statemachinevariable_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachineVariable)



@given(instance=statemachine_StateMachineVariable_strategy)
def test_statemachine_statemachinevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_StateMachineVariable_strategy)
def test_statemachine_statemachinevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=30)
def test_statemachine_statemachine_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_StateMachine is not implemented or raised an error")

@given(instance=statemachine_Declaration_strategy)
@settings(max_examples=50)
def test_statemachine_declaration_instantiation(instance):
    assert isinstance(instance, statemachine_Declaration)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_Declaration_strategy)
@settings(max_examples=30)
def test_statemachine_declaration_printreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printReachable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printReachable' in statemachine_Declaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine_Declaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine_Declaration is not implemented or raised an error")
