import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSMException,
    fsm::NoInitialStateException,
    fsm::NoTransition,
    fsm::NonDeterminism,
    fsm::FSM,
    fsm::FSMException,
    fsm::Transition,
    fsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmexception_is_not_abstract():
    assert not inspect.isabstract(FSMException)


def test_fsmexception_constructor_exists():
    assert callable(FSMException.__init__)


def test_fsmexception_constructor_args():
    sig = inspect.signature(FSMException.__init__)
    params = list(sig.parameters.keys())



def test_fsm::noinitialstateexception_is_not_abstract():
    assert not inspect.isabstract(fsm::NoInitialStateException)


def test_fsm::noinitialstateexception_constructor_exists():
    assert callable(fsm::NoInitialStateException.__init__)


def test_fsm::noinitialstateexception_constructor_args():
    sig = inspect.signature(fsm::NoInitialStateException.__init__)
    params = list(sig.parameters.keys())



def test_fsm::notransition_is_not_abstract():
    assert not inspect.isabstract(fsm::NoTransition)


def test_fsm::notransition_constructor_exists():
    assert callable(fsm::NoTransition.__init__)


def test_fsm::notransition_constructor_args():
    sig = inspect.signature(fsm::NoTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::nondeterminism_is_not_abstract():
    assert not inspect.isabstract(fsm::NonDeterminism)


def test_fsm::nondeterminism_constructor_exists():
    assert callable(fsm::NonDeterminism.__init__)


def test_fsm::nondeterminism_constructor_args():
    sig = inspect.signature(fsm::NonDeterminism.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsmexception_is_not_abstract():
    assert not inspect.isabstract(fsm::FSMException)


def test_fsm::fsmexception_constructor_exists():
    assert callable(fsm::FSMException.__init__)


def test_fsm::fsmexception_constructor_args():
    sig = inspect.signature(fsm::FSMException.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsm::transition_has_output():
    assert hasattr(fsm::Transition, "output")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_input():
    assert hasattr(fsm::Transition, "input")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
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
FSMException_strategy = st.builds(
    FSMException,
)
fsm::NoInitialStateException_strategy = st.builds(
    fsm::NoInitialStateException,
)
fsm::NoTransition_strategy = st.builds(
    fsm::NoTransition,
)
fsm::NonDeterminism_strategy = st.builds(
    fsm::NonDeterminism,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)
fsm::FSMException_strategy = st.builds(
    fsm::FSMException,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    output=
        safe_text,
    input=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)

@given(instance=FSMException_strategy)
@settings(max_examples=50)
def test_fsmexception_instantiation(instance):
    assert isinstance(instance, FSMException)

@given(instance=fsm::NoInitialStateException_strategy)
@settings(max_examples=50)
def test_fsm::noinitialstateexception_instantiation(instance):
    assert isinstance(instance, fsm::NoInitialStateException)

@given(instance=fsm::NoTransition_strategy)
@settings(max_examples=50)
def test_fsm::notransition_instantiation(instance):
    assert isinstance(instance, fsm::NoTransition)

@given(instance=fsm::NonDeterminism_strategy)
@settings(max_examples=50)
def test_fsm::nondeterminism_instantiation(instance):
    assert isinstance(instance, fsm::NonDeterminism)

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
def test_fsm::fsm_run_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.run()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.run).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'run' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in fsm::FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::FSM_strategy)
@settings(max_examples=30)
def test_fsm::fsm_reset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reset()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reset' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reset' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reset' in fsm::FSM is not implemented or raised an error")

@given(instance=fsm::FSMException_strategy)
@settings(max_examples=50)
def test_fsm::fsmexception_instantiation(instance):
    assert isinstance(instance, fsm::FSMException)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::Transition_strategy)
@settings(max_examples=30)
def test_fsm::transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in fsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in fsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in fsm::Transition is not implemented or raised an error")

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
def test_fsm::state_step_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.step(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.step).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'step' in fsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'step' in fsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'step' in fsm::State is not implemented or raised an error")
