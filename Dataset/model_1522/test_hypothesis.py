import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minifsm::FSM,
    State,
    minifsm::Terminal,
    minifsm::Initial,
    minifsm::Transition,
    minifsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minifsm::fsm_is_not_abstract():
    assert not inspect.isabstract(minifsm::FSM)


def test_minifsm::fsm_constructor_exists():
    assert callable(minifsm::FSM.__init__)


def test_minifsm::fsm_constructor_args():
    sig = inspect.signature(minifsm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_minifsm::terminal_is_not_abstract():
    assert not inspect.isabstract(minifsm::Terminal)


def test_minifsm::terminal_constructor_exists():
    assert callable(minifsm::Terminal.__init__)


def test_minifsm::terminal_constructor_args():
    sig = inspect.signature(minifsm::Terminal.__init__)
    params = list(sig.parameters.keys())



def test_minifsm::initial_is_not_abstract():
    assert not inspect.isabstract(minifsm::Initial)


def test_minifsm::initial_constructor_exists():
    assert callable(minifsm::Initial.__init__)


def test_minifsm::initial_constructor_args():
    sig = inspect.signature(minifsm::Initial.__init__)
    params = list(sig.parameters.keys())



def test_minifsm::transition_is_not_abstract():
    assert not inspect.isabstract(minifsm::Transition)


def test_minifsm::transition_constructor_exists():
    assert callable(minifsm::Transition.__init__)


def test_minifsm::transition_constructor_args():
    sig = inspect.signature(minifsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_minifsm::transition_has_event():
    assert hasattr(minifsm::Transition, "event")
    descriptor = None
    for klass in minifsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_minifsm::state_is_not_abstract():
    assert not inspect.isabstract(minifsm::State)


def test_minifsm::state_constructor_exists():
    assert callable(minifsm::State.__init__)


def test_minifsm::state_constructor_args():
    sig = inspect.signature(minifsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minifsm::state_has_name():
    assert hasattr(minifsm::State, "name")
    descriptor = None
    for klass in minifsm::State.__mro__:
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
minifsm::FSM_strategy = st.builds(
    minifsm::FSM,
)
State_strategy = st.builds(
    State,
)
minifsm::Terminal_strategy = st.builds(
    minifsm::Terminal,
)
minifsm::Initial_strategy = st.builds(
    minifsm::Initial,
)
minifsm::Transition_strategy = st.builds(
    minifsm::Transition,
    event=
        safe_text
)
minifsm::State_strategy = st.builds(
    minifsm::State,
    name=
        safe_text
)

@given(instance=minifsm::FSM_strategy)
@settings(max_examples=50)
def test_minifsm::fsm_instantiation(instance):
    assert isinstance(instance, minifsm::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm::FSM_strategy)
@settings(max_examples=30)
def test_minifsm::fsm_handle_changes_state(instance):
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
        assert has_statements, f"Function 'handle' in minifsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'handle' in minifsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'handle' in minifsm::FSM is not implemented or raised an error")

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minifsm::Terminal_strategy)
@settings(max_examples=50)
def test_minifsm::terminal_instantiation(instance):
    assert isinstance(instance, minifsm::Terminal)

@given(instance=minifsm::Initial_strategy)
@settings(max_examples=50)
def test_minifsm::initial_instantiation(instance):
    assert isinstance(instance, minifsm::Initial)

@given(instance=minifsm::Transition_strategy)
@settings(max_examples=50)
def test_minifsm::transition_instantiation(instance):
    assert isinstance(instance, minifsm::Transition)

@given(instance=minifsm::Transition_strategy)
def test_minifsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=minifsm::Transition_strategy)
def test_minifsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm::Transition_strategy)
@settings(max_examples=30)
def test_minifsm::transition_isactivated_changes_state(instance):
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
        assert has_statements, f"Function 'isActivated' in minifsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isActivated' in minifsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isActivated' in minifsm::Transition is not implemented or raised an error")

@given(instance=minifsm::State_strategy)
@settings(max_examples=50)
def test_minifsm::state_instantiation(instance):
    assert isinstance(instance, minifsm::State)

@given(instance=minifsm::State_strategy)
def test_minifsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minifsm::State_strategy)
def test_minifsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=minifsm::State_strategy)
@settings(max_examples=30)
def test_minifsm::state_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in minifsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in minifsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in minifsm::State is not implemented or raised an error")
