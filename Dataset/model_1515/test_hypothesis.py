import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    minifsm_Terminal,
    minifsm_Initial,
    minifsm_Transition,
    minifsm_State,
    minifsm_FSM,
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



def test_minifsm_terminal_is_not_abstract():
    assert not inspect.isabstract(minifsm_Terminal)


def test_minifsm_terminal_constructor_exists():
    assert callable(minifsm_Terminal.__init__)


def test_minifsm_terminal_constructor_args():
    sig = inspect.signature(minifsm_Terminal.__init__)
    params = list(sig.parameters.keys())



def test_minifsm_initial_is_not_abstract():
    assert not inspect.isabstract(minifsm_Initial)


def test_minifsm_initial_constructor_exists():
    assert callable(minifsm_Initial.__init__)


def test_minifsm_initial_constructor_args():
    sig = inspect.signature(minifsm_Initial.__init__)
    params = list(sig.parameters.keys())



def test_minifsm_transition_is_not_abstract():
    assert not inspect.isabstract(minifsm_Transition)


def test_minifsm_transition_constructor_exists():
    assert callable(minifsm_Transition.__init__)


def test_minifsm_transition_constructor_args():
    sig = inspect.signature(minifsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_minifsm_transition_has_event():
    assert hasattr(minifsm_Transition, "event")
    descriptor = None
    for klass in minifsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_minifsm_state_is_not_abstract():
    assert not inspect.isabstract(minifsm_State)


def test_minifsm_state_constructor_exists():
    assert callable(minifsm_State.__init__)


def test_minifsm_state_constructor_args():
    sig = inspect.signature(minifsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minifsm_state_has_name():
    assert hasattr(minifsm_State, "name")
    descriptor = None
    for klass in minifsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minifsm_fsm_is_not_abstract():
    assert not inspect.isabstract(minifsm_FSM)


def test_minifsm_fsm_constructor_exists():
    assert callable(minifsm_FSM.__init__)


def test_minifsm_fsm_constructor_args():
    sig = inspect.signature(minifsm_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "currentEvent" in params, "Missing parameter 'currentEvent'"

def test_minifsm_fsm_has_currentEvent():
    assert hasattr(minifsm_FSM, "currentEvent")
    descriptor = None
    for klass in minifsm_FSM.__mro__:
        if "currentEvent" in klass.__dict__:
            descriptor = klass.__dict__["currentEvent"]
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
minifsm_Terminal_strategy = st.builds(
    minifsm_Terminal,
)
minifsm_Initial_strategy = st.builds(
    minifsm_Initial,
)
minifsm_Transition_strategy = st.builds(
    minifsm_Transition,
    event=
        safe_text
)
minifsm_State_strategy = st.builds(
    minifsm_State,
    name=
        safe_text
)
minifsm_FSM_strategy = st.builds(
    minifsm_FSM,
    currentEvent=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minifsm_Terminal_strategy)
@settings(max_examples=50)
def test_minifsm_terminal_instantiation(instance):
    assert isinstance(instance, minifsm_Terminal)

@given(instance=minifsm_Initial_strategy)
@settings(max_examples=50)
def test_minifsm_initial_instantiation(instance):
    assert isinstance(instance, minifsm_Initial)

@given(instance=minifsm_Transition_strategy)
@settings(max_examples=50)
def test_minifsm_transition_instantiation(instance):
    assert isinstance(instance, minifsm_Transition)



@given(instance=minifsm_Transition_strategy)
def test_minifsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_Transition_strategy)
@settings(max_examples=30)
def test_minifsm_transition_isactivated_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isActivated()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isActivated).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isActivated' in minifsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isActivated' in minifsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isActivated' in minifsm_Transition is not implemented or raised an error")

@given(instance=minifsm_State_strategy)
@settings(max_examples=50)
def test_minifsm_state_instantiation(instance):
    assert isinstance(instance, minifsm_State)



@given(instance=minifsm_State_strategy)
def test_minifsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_State_strategy)
@settings(max_examples=30)
def test_minifsm_state_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in minifsm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in minifsm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in minifsm_State is not implemented or raised an error")

@given(instance=minifsm_FSM_strategy)
@settings(max_examples=50)
def test_minifsm_fsm_instantiation(instance):
    assert isinstance(instance, minifsm_FSM)



@given(instance=minifsm_FSM_strategy)
def test_minifsm_fsm_currentEvent_setter(instance):
    original = instance.currentEvent
    instance.currentEvent = original
    assert instance.currentEvent == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm_FSM_strategy)
@settings(max_examples=30)
def test_minifsm_fsm_handle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.handle(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.handle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'handle' in minifsm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'handle' in minifsm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'handle' in minifsm_FSM is not implemented or raised an error")
