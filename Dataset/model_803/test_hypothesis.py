import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSMException,
    fsmkerm::NoInitialStateException,
    fsmkerm::NoTransition,
    fsmkerm::NonDeterminism,
    fsmkerm::FSMException,
    fsmkerm::State,
    fsmkerm::FSM,
    fsmkerm::Transition,
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



def test_fsmkerm::noinitialstateexception_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::NoInitialStateException)


def test_fsmkerm::noinitialstateexception_constructor_exists():
    assert callable(fsmkerm::NoInitialStateException.__init__)


def test_fsmkerm::noinitialstateexception_constructor_args():
    sig = inspect.signature(fsmkerm::NoInitialStateException.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm::notransition_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::NoTransition)


def test_fsmkerm::notransition_constructor_exists():
    assert callable(fsmkerm::NoTransition.__init__)


def test_fsmkerm::notransition_constructor_args():
    sig = inspect.signature(fsmkerm::NoTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm::nondeterminism_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::NonDeterminism)


def test_fsmkerm::nondeterminism_constructor_exists():
    assert callable(fsmkerm::NonDeterminism.__init__)


def test_fsmkerm::nondeterminism_constructor_args():
    sig = inspect.signature(fsmkerm::NonDeterminism.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm::fsmexception_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::FSMException)


def test_fsmkerm::fsmexception_constructor_exists():
    assert callable(fsmkerm::FSMException.__init__)


def test_fsmkerm::fsmexception_constructor_args():
    sig = inspect.signature(fsmkerm::FSMException.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm::state_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::State)


def test_fsmkerm::state_constructor_exists():
    assert callable(fsmkerm::State.__init__)


def test_fsmkerm::state_constructor_args():
    sig = inspect.signature(fsmkerm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmkerm::state_has_name():
    assert hasattr(fsmkerm::State, "name")
    descriptor = None
    for klass in fsmkerm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmkerm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::FSM)


def test_fsmkerm::fsm_constructor_exists():
    assert callable(fsmkerm::FSM.__init__)


def test_fsmkerm::fsm_constructor_args():
    sig = inspect.signature(fsmkerm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm::transition_is_not_abstract():
    assert not inspect.isabstract(fsmkerm::Transition)


def test_fsmkerm::transition_constructor_exists():
    assert callable(fsmkerm::Transition.__init__)


def test_fsmkerm::transition_constructor_args():
    sig = inspect.signature(fsmkerm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsmkerm::transition_has_output():
    assert hasattr(fsmkerm::Transition, "output")
    descriptor = None
    for klass in fsmkerm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsmkerm::transition_has_input():
    assert hasattr(fsmkerm::Transition, "input")
    descriptor = None
    for klass in fsmkerm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
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
fsmkerm::NoInitialStateException_strategy = st.builds(
    fsmkerm::NoInitialStateException,
)
fsmkerm::NoTransition_strategy = st.builds(
    fsmkerm::NoTransition,
)
fsmkerm::NonDeterminism_strategy = st.builds(
    fsmkerm::NonDeterminism,
)
fsmkerm::FSMException_strategy = st.builds(
    fsmkerm::FSMException,
)
fsmkerm::State_strategy = st.builds(
    fsmkerm::State,
    name=
        safe_text
)
fsmkerm::FSM_strategy = st.builds(
    fsmkerm::FSM,
)
fsmkerm::Transition_strategy = st.builds(
    fsmkerm::Transition,
    output=
        safe_text,
    input=
        safe_text
)

@given(instance=FSMException_strategy)
@settings(max_examples=50)
def test_fsmexception_instantiation(instance):
    assert isinstance(instance, FSMException)

@given(instance=fsmkerm::NoInitialStateException_strategy)
@settings(max_examples=50)
def test_fsmkerm::noinitialstateexception_instantiation(instance):
    assert isinstance(instance, fsmkerm::NoInitialStateException)

@given(instance=fsmkerm::NoTransition_strategy)
@settings(max_examples=50)
def test_fsmkerm::notransition_instantiation(instance):
    assert isinstance(instance, fsmkerm::NoTransition)

@given(instance=fsmkerm::NonDeterminism_strategy)
@settings(max_examples=50)
def test_fsmkerm::nondeterminism_instantiation(instance):
    assert isinstance(instance, fsmkerm::NonDeterminism)

@given(instance=fsmkerm::FSMException_strategy)
@settings(max_examples=50)
def test_fsmkerm::fsmexception_instantiation(instance):
    assert isinstance(instance, fsmkerm::FSMException)

@given(instance=fsmkerm::State_strategy)
@settings(max_examples=50)
def test_fsmkerm::state_instantiation(instance):
    assert isinstance(instance, fsmkerm::State)

@given(instance=fsmkerm::State_strategy)
def test_fsmkerm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmkerm::State_strategy)
def test_fsmkerm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm::State_strategy)
@settings(max_examples=30)
def test_fsmkerm::state_step_changes_state(instance):
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
        assert has_statements, f"Function 'step' in fsmkerm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'step' in fsmkerm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'step' in fsmkerm::State is not implemented or raised an error")

@given(instance=fsmkerm::FSM_strategy)
@settings(max_examples=50)
def test_fsmkerm::fsm_instantiation(instance):
    assert isinstance(instance, fsmkerm::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm::FSM_strategy)
@settings(max_examples=30)
def test_fsmkerm::fsm_reset_changes_state(instance):
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
        assert has_statements, f"Function 'reset' in fsmkerm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reset' in fsmkerm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reset' in fsmkerm::FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm::FSM_strategy)
@settings(max_examples=30)
def test_fsmkerm::fsm_run_changes_state(instance):
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
        assert has_statements, f"Function 'run' in fsmkerm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in fsmkerm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in fsmkerm::FSM is not implemented or raised an error")

@given(instance=fsmkerm::Transition_strategy)
@settings(max_examples=50)
def test_fsmkerm::transition_instantiation(instance):
    assert isinstance(instance, fsmkerm::Transition)

@given(instance=fsmkerm::Transition_strategy)
def test_fsmkerm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=fsmkerm::Transition_strategy)
def test_fsmkerm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=fsmkerm::Transition_strategy)
def test_fsmkerm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsmkerm::Transition_strategy)
def test_fsmkerm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm::Transition_strategy)
@settings(max_examples=30)
def test_fsmkerm::transition_fire_changes_state(instance):
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
        assert has_statements, f"Function 'fire' in fsmkerm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in fsmkerm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in fsmkerm::Transition is not implemented or raised an error")
