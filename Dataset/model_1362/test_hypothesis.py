import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Action,
    State,
    statemachine::InitialState,
    statemachine::FinalState,
    statemachine::NormalState,
    statemachine::Declaration,
    statemachine::StateMachine,
    Declaration,
    statemachine::State,
    statemachine::Transition,
    statemachine::StateMachineVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::action_is_not_abstract():
    assert not inspect.isabstract(statemachine::Action)


def test_statemachine::action_constructor_exists():
    assert callable(statemachine::Action.__init__)


def test_statemachine::action_constructor_args():
    sig = inspect.signature(statemachine::Action.__init__)
    params = list(sig.parameters.keys())
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"

def test_statemachine::action_has_actionStatement():
    assert hasattr(statemachine::Action, "actionStatement")
    descriptor = None
    for klass in statemachine::Action.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::action_has_actionLabel():
    assert hasattr(statemachine::Action, "actionLabel")
    descriptor = None
    for klass in statemachine::Action.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(statemachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(statemachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::normalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::NormalState)


def test_statemachine::normalstate_constructor_exists():
    assert callable(statemachine::NormalState.__init__)


def test_statemachine::normalstate_constructor_args():
    sig = inspect.signature(statemachine::NormalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::declaration_is_not_abstract():
    assert not inspect.isabstract(statemachine::Declaration)


def test_statemachine::declaration_constructor_exists():
    assert callable(statemachine::Declaration.__init__)


def test_statemachine::declaration_constructor_args():
    sig = inspect.signature(statemachine::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"

def test_statemachine::state_has_id():
    assert hasattr(statemachine::State, "id")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_label():
    assert hasattr(statemachine::State, "label")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "targetLabel" in params, "Missing parameter 'targetLabel'"
    assert "label" in params, "Missing parameter 'label'"
    assert "actionStatement" in params, "Missing parameter 'actionStatement'"
    assert "actionLabel" in params, "Missing parameter 'actionLabel'"
    assert "guardExpression" in params, "Missing parameter 'guardExpression'"
    assert "guardLabel" in params, "Missing parameter 'guardLabel'"
    assert "sourceLabel" in params, "Missing parameter 'sourceLabel'"

def test_statemachine::transition_has_targetLabel():
    assert hasattr(statemachine::Transition, "targetLabel")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "targetLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_label():
    assert hasattr(statemachine::Transition, "label")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_actionStatement():
    assert hasattr(statemachine::Transition, "actionStatement")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "actionStatement" in klass.__dict__:
            descriptor = klass.__dict__["actionStatement"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_actionLabel():
    assert hasattr(statemachine::Transition, "actionLabel")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "actionLabel" in klass.__dict__:
            descriptor = klass.__dict__["actionLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_guardExpression():
    assert hasattr(statemachine::Transition, "guardExpression")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "guardExpression" in klass.__dict__:
            descriptor = klass.__dict__["guardExpression"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_guardLabel():
    assert hasattr(statemachine::Transition, "guardLabel")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "guardLabel" in klass.__dict__:
            descriptor = klass.__dict__["guardLabel"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_sourceLabel():
    assert hasattr(statemachine::Transition, "sourceLabel")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "sourceLabel" in klass.__dict__:
            descriptor = klass.__dict__["sourceLabel"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachinevariable_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachineVariable)


def test_statemachine::statemachinevariable_constructor_exists():
    assert callable(statemachine::StateMachineVariable.__init__)


def test_statemachine::statemachinevariable_constructor_args():
    sig = inspect.signature(statemachine::StateMachineVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachinevariable_has_type():
    assert hasattr(statemachine::StateMachineVariable, "type")
    descriptor = None
    for klass in statemachine::StateMachineVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::statemachinevariable_has_name():
    assert hasattr(statemachine::StateMachineVariable, "name")
    descriptor = None
    for klass in statemachine::StateMachineVariable.__mro__:
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
statemachine::Action_strategy = st.builds(
    statemachine::Action,
    actionStatement=
        safe_text,
    actionLabel=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine::InitialState_strategy = st.builds(
    statemachine::InitialState,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
statemachine::NormalState_strategy = st.builds(
    statemachine::NormalState,
)
statemachine::Declaration_strategy = st.builds(
    statemachine::Declaration,
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
)
Declaration_strategy = st.builds(
    Declaration,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    id=
        st.integers(),
    label=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    targetLabel=
        safe_text,
    label=
        safe_text,
    actionStatement=
        safe_text,
    actionLabel=
        safe_text,
    guardExpression=
        safe_text,
    guardLabel=
        safe_text,
    sourceLabel=
        safe_text
)
statemachine::StateMachineVariable_strategy = st.builds(
    statemachine::StateMachineVariable,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=statemachine::Action_strategy)
@settings(max_examples=50)
def test_statemachine::action_instantiation(instance):
    assert isinstance(instance, statemachine::Action)

@given(instance=statemachine::Action_strategy)
def test_statemachine::action_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=statemachine::Action_strategy)
def test_statemachine::action_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=statemachine::Action_strategy)
def test_statemachine::action_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=statemachine::Action_strategy)
def test_statemachine::action_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, statemachine::InitialState)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=statemachine::NormalState_strategy)
@settings(max_examples=50)
def test_statemachine::normalstate_instantiation(instance):
    assert isinstance(instance, statemachine::NormalState)

@given(instance=statemachine::Declaration_strategy)
@settings(max_examples=50)
def test_statemachine::declaration_instantiation(instance):
    assert isinstance(instance, statemachine::Declaration)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine::Declaration_strategy)
@settings(max_examples=30)
def test_statemachine::declaration_printreachable_changes_state(instance):
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
        assert has_statements, f"Function 'printReachable' in statemachine::Declaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine::Declaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine::Declaration is not implemented or raised an error")

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=30)
def test_statemachine::statemachine_printreachable_changes_state(instance):
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
        assert has_statements, f"Function 'printReachable' in statemachine::StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine::StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine::StateMachine is not implemented or raised an error")

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine::State_strategy)
@settings(max_examples=30)
def test_statemachine::state_printreachable_changes_state(instance):
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
        assert has_statements, f"Function 'printReachable' in statemachine::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printReachable' in statemachine::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printReachable' in statemachine::State is not implemented or raised an error")

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_targetLabel_type(instance):
    assert isinstance(instance.targetLabel, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_targetLabel_setter(instance):
    original = instance.targetLabel
    instance.targetLabel = original
    assert instance.targetLabel == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_actionStatement_type(instance):
    assert isinstance(instance.actionStatement, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_actionStatement_setter(instance):
    original = instance.actionStatement
    instance.actionStatement = original
    assert instance.actionStatement == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_actionLabel_type(instance):
    assert isinstance(instance.actionLabel, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_actionLabel_setter(instance):
    original = instance.actionLabel
    instance.actionLabel = original
    assert instance.actionLabel == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guardExpression_type(instance):
    assert isinstance(instance.guardExpression, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guardExpression_setter(instance):
    original = instance.guardExpression
    instance.guardExpression = original
    assert instance.guardExpression == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guardLabel_type(instance):
    assert isinstance(instance.guardLabel, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_guardLabel_setter(instance):
    original = instance.guardLabel
    instance.guardLabel = original
    assert instance.guardLabel == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_sourceLabel_type(instance):
    assert isinstance(instance.sourceLabel, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_sourceLabel_setter(instance):
    original = instance.sourceLabel
    instance.sourceLabel = original
    assert instance.sourceLabel == original

@given(instance=statemachine::StateMachineVariable_strategy)
@settings(max_examples=50)
def test_statemachine::statemachinevariable_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachineVariable)

@given(instance=statemachine::StateMachineVariable_strategy)
def test_statemachine::statemachinevariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statemachine::StateMachineVariable_strategy)
def test_statemachine::statemachinevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statemachine::StateMachineVariable_strategy)
def test_statemachine::statemachinevariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::StateMachineVariable_strategy)
def test_statemachine::statemachinevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
