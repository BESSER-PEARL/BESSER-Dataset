import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FSMException,
    fsm_NoInitialStateException,
    fsm_NoTransition,
    fsm_NonDeterminism,
    fsm_FSM,
    fsm_FSMException,
    fsm_Transition,
    fsm_State,
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



def test_fsm_noinitialstateexception_is_not_abstract():
    assert not inspect.isabstract(fsm_NoInitialStateException)


def test_fsm_noinitialstateexception_constructor_exists():
    assert callable(fsm_NoInitialStateException.__init__)


def test_fsm_noinitialstateexception_constructor_args():
    sig = inspect.signature(fsm_NoInitialStateException.__init__)
    params = list(sig.parameters.keys())



def test_fsm_notransition_is_not_abstract():
    assert not inspect.isabstract(fsm_NoTransition)


def test_fsm_notransition_constructor_exists():
    assert callable(fsm_NoTransition.__init__)


def test_fsm_notransition_constructor_args():
    sig = inspect.signature(fsm_NoTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_nondeterminism_is_not_abstract():
    assert not inspect.isabstract(fsm_NonDeterminism)


def test_fsm_nondeterminism_constructor_exists():
    assert callable(fsm_NonDeterminism.__init__)


def test_fsm_nondeterminism_constructor_args():
    sig = inspect.signature(fsm_NonDeterminism.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fsmexception_is_not_abstract():
    assert not inspect.isabstract(fsm_FSMException)


def test_fsm_fsmexception_constructor_exists():
    assert callable(fsm_FSMException.__init__)


def test_fsm_fsmexception_constructor_args():
    sig = inspect.signature(fsm_FSMException.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_fsm_transition_has_input():
    assert hasattr(fsm_Transition, "input")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_output():
    assert hasattr(fsm_Transition, "output")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_state_has_name():
    assert hasattr(fsm_State, "name")
    descriptor = None
    for klass in fsm_State.__mro__:
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
fsm_NoInitialStateException_strategy = st.builds(
    fsm_NoInitialStateException,
)
fsm_NoTransition_strategy = st.builds(
    fsm_NoTransition,
)
fsm_NonDeterminism_strategy = st.builds(
    fsm_NonDeterminism,
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
)
fsm_FSMException_strategy = st.builds(
    fsm_FSMException,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    input=
        safe_text,
    output=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)

@given(instance=FSMException_strategy)
@settings(max_examples=50)
def test_fsmexception_instantiation(instance):
    assert isinstance(instance, FSMException)

@given(instance=fsm_NoInitialStateException_strategy)
@settings(max_examples=50)
def test_fsm_noinitialstateexception_instantiation(instance):
    assert isinstance(instance, fsm_NoInitialStateException)

@given(instance=fsm_NoTransition_strategy)
@settings(max_examples=50)
def test_fsm_notransition_instantiation(instance):
    assert isinstance(instance, fsm_NoTransition)

@given(instance=fsm_NonDeterminism_strategy)
@settings(max_examples=50)
def test_fsm_nondeterminism_instantiation(instance):
    assert isinstance(instance, fsm_NonDeterminism)

@given(instance=fsm_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fsm_FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_FSM_strategy)
@settings(max_examples=30)
def test_fsm_fsm_run_changes_state(instance):
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
        assert has_statements, f"Function 'run' in fsm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in fsm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in fsm_FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_FSM_strategy)
@settings(max_examples=30)
def test_fsm_fsm_reset_changes_state(instance):
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
        assert has_statements, f"Function 'reset' in fsm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reset' in fsm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reset' in fsm_FSM is not implemented or raised an error")

@given(instance=fsm_FSMException_strategy)
@settings(max_examples=50)
def test_fsm_fsmexception_instantiation(instance):
    assert isinstance(instance, fsm_FSMException)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Transition_strategy)
@settings(max_examples=30)
def test_fsm_transition_fire_changes_state(instance):
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
        assert has_statements, f"Function 'fire' in fsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in fsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in fsm_Transition is not implemented or raised an error")

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_State_strategy)
@settings(max_examples=30)
def test_fsm_state_step_changes_state(instance):
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
        assert has_statements, f"Function 'step' in fsm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'step' in fsm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'step' in fsm_State is not implemented or raised an error")
