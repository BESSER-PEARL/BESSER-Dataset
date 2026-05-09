import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::State,
    State,
    fsm::Final,
    fsm::Initial,
    fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_fsm::transition_has_event():
    assert hasattr(fsm::Transition, "event")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::final_is_not_abstract():
    assert not inspect.isabstract(fsm::Final)


def test_fsm::final_constructor_exists():
    assert callable(fsm::Final.__init__)


def test_fsm::final_constructor_args():
    sig = inspect.signature(fsm::Final.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initial_is_not_abstract():
    assert not inspect.isabstract(fsm::Initial)


def test_fsm::initial_constructor_exists():
    assert callable(fsm::Initial.__init__)


def test_fsm::initial_constructor_args():
    sig = inspect.signature(fsm::Initial.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    event=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::Final_strategy = st.builds(
    fsm::Final,
)
fsm::Initial_strategy = st.builds(
    fsm::Initial,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::Transition_strategy)
@settings(max_examples=30)
def test_fsm::transition_isactivated_changes_state(instance):
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
        assert has_statements, f"Function 'isActivated' in fsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isActivated' in fsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isActivated' in fsm::Transition is not implemented or raised an error")

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::State_strategy)
@settings(max_examples=30)
def test_fsm::state_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in fsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in fsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in fsm::State is not implemented or raised an error")

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::Final_strategy)
@settings(max_examples=50)
def test_fsm::final_instantiation(instance):
    assert isinstance(instance, fsm::Final)

@given(instance=fsm::Initial_strategy)
@settings(max_examples=50)
def test_fsm::initial_instantiation(instance):
    assert isinstance(instance, fsm::Initial)

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::FSM_strategy)
@settings(max_examples=30)
def test_fsm::fsm_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in fsm::FSM is not implemented or raised an error")
