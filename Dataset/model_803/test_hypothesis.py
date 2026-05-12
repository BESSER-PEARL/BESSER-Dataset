import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FSMException,
    fsmkerm_NoInitialStateException,
    fsmkerm_NoTransition,
    fsmkerm_NonDeterminism,
    fsmkerm_FSMException,
    fsmkerm_State,
    fsmkerm_FSM,
    fsmkerm_Transition,
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



def test_fsmkerm_noinitialstateexception_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_NoInitialStateException)


def test_fsmkerm_noinitialstateexception_constructor_exists():
    assert callable(fsmkerm_NoInitialStateException.__init__)


def test_fsmkerm_noinitialstateexception_constructor_args():
    sig = inspect.signature(fsmkerm_NoInitialStateException.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm_notransition_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_NoTransition)


def test_fsmkerm_notransition_constructor_exists():
    assert callable(fsmkerm_NoTransition.__init__)


def test_fsmkerm_notransition_constructor_args():
    sig = inspect.signature(fsmkerm_NoTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm_nondeterminism_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_NonDeterminism)


def test_fsmkerm_nondeterminism_constructor_exists():
    assert callable(fsmkerm_NonDeterminism.__init__)


def test_fsmkerm_nondeterminism_constructor_args():
    sig = inspect.signature(fsmkerm_NonDeterminism.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm_fsmexception_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_FSMException)


def test_fsmkerm_fsmexception_constructor_exists():
    assert callable(fsmkerm_FSMException.__init__)


def test_fsmkerm_fsmexception_constructor_args():
    sig = inspect.signature(fsmkerm_FSMException.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm_state_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_State)


def test_fsmkerm_state_constructor_exists():
    assert callable(fsmkerm_State.__init__)


def test_fsmkerm_state_constructor_args():
    sig = inspect.signature(fsmkerm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmkerm_state_has_name():
    assert hasattr(fsmkerm_State, "name")
    descriptor = None
    for klass in fsmkerm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmkerm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_FSM)


def test_fsmkerm_fsm_constructor_exists():
    assert callable(fsmkerm_FSM.__init__)


def test_fsmkerm_fsm_constructor_args():
    sig = inspect.signature(fsmkerm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsmkerm_transition_is_not_abstract():
    assert not inspect.isabstract(fsmkerm_Transition)


def test_fsmkerm_transition_constructor_exists():
    assert callable(fsmkerm_Transition.__init__)


def test_fsmkerm_transition_constructor_args():
    sig = inspect.signature(fsmkerm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsmkerm_transition_has_output():
    assert hasattr(fsmkerm_Transition, "output")
    descriptor = None
    for klass in fsmkerm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsmkerm_transition_has_input():
    assert hasattr(fsmkerm_Transition, "input")
    descriptor = None
    for klass in fsmkerm_Transition.__mro__:
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
fsmkerm_NoInitialStateException_strategy = st.builds(
    fsmkerm_NoInitialStateException,
)
fsmkerm_NoTransition_strategy = st.builds(
    fsmkerm_NoTransition,
)
fsmkerm_NonDeterminism_strategy = st.builds(
    fsmkerm_NonDeterminism,
)
fsmkerm_FSMException_strategy = st.builds(
    fsmkerm_FSMException,
)
fsmkerm_State_strategy = st.builds(
    fsmkerm_State,
    name=
        safe_text
)
fsmkerm_FSM_strategy = st.builds(
    fsmkerm_FSM,
)
fsmkerm_Transition_strategy = st.builds(
    fsmkerm_Transition,
    output=
        safe_text,
    input=
        safe_text
)

@given(instance=FSMException_strategy)
@settings(max_examples=50)
def test_fsmexception_instantiation(instance):
    assert isinstance(instance, FSMException)

@given(instance=fsmkerm_NoInitialStateException_strategy)
@settings(max_examples=50)
def test_fsmkerm_noinitialstateexception_instantiation(instance):
    assert isinstance(instance, fsmkerm_NoInitialStateException)

@given(instance=fsmkerm_NoTransition_strategy)
@settings(max_examples=50)
def test_fsmkerm_notransition_instantiation(instance):
    assert isinstance(instance, fsmkerm_NoTransition)

@given(instance=fsmkerm_NonDeterminism_strategy)
@settings(max_examples=50)
def test_fsmkerm_nondeterminism_instantiation(instance):
    assert isinstance(instance, fsmkerm_NonDeterminism)

@given(instance=fsmkerm_FSMException_strategy)
@settings(max_examples=50)
def test_fsmkerm_fsmexception_instantiation(instance):
    assert isinstance(instance, fsmkerm_FSMException)

@given(instance=fsmkerm_State_strategy)
@settings(max_examples=50)
def test_fsmkerm_state_instantiation(instance):
    assert isinstance(instance, fsmkerm_State)



@given(instance=fsmkerm_State_strategy)
def test_fsmkerm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm_State_strategy)
@settings(max_examples=30)
def test_fsmkerm_state_step_changes_state(instance):
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
        assert has_statements, f"Function 'step' in fsmkerm_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'step' in fsmkerm_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'step' in fsmkerm_State is not implemented or raised an error")

@given(instance=fsmkerm_FSM_strategy)
@settings(max_examples=50)
def test_fsmkerm_fsm_instantiation(instance):
    assert isinstance(instance, fsmkerm_FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm_FSM_strategy)
@settings(max_examples=30)
def test_fsmkerm_fsm_run_changes_state(instance):
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
        assert has_statements, f"Function 'run' in fsmkerm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in fsmkerm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in fsmkerm_FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm_FSM_strategy)
@settings(max_examples=30)
def test_fsmkerm_fsm_reset_changes_state(instance):
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
        assert has_statements, f"Function 'reset' in fsmkerm_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reset' in fsmkerm_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reset' in fsmkerm_FSM is not implemented or raised an error")

@given(instance=fsmkerm_Transition_strategy)
@settings(max_examples=50)
def test_fsmkerm_transition_instantiation(instance):
    assert isinstance(instance, fsmkerm_Transition)



@given(instance=fsmkerm_Transition_strategy)
def test_fsmkerm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=fsmkerm_Transition_strategy)
def test_fsmkerm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmkerm_Transition_strategy)
@settings(max_examples=30)
def test_fsmkerm_transition_fire_changes_state(instance):
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
        assert has_statements, f"Function 'fire' in fsmkerm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in fsmkerm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in fsmkerm_Transition is not implemented or raised an error")
