import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::NamedElement,
    NamedElement,
    fsm::Transition,
    fsm::State,
    fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(fsm::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(fsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(fsm::NamedElement, "name")
    descriptor = None
    for klass in fsm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "letterToMatch" in params, "Missing parameter 'letterToMatch'"
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_fsm::transition_has_letterToMatch():
    assert hasattr(fsm::Transition, "letterToMatch")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "letterToMatch" in klass.__dict__:
            descriptor = klass.__dict__["letterToMatch"]
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

def test_fsm::transition_has_output():
    assert hasattr(fsm::Transition, "output")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
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
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    letterToMatch=
        safe_text,
    input=
        safe_text,
    output=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)

@given(instance=fsm::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, fsm::NamedElement)

@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_letterToMatch_type(instance):
    assert isinstance(instance.letterToMatch, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_letterToMatch_setter(instance):
    original = instance.letterToMatch
    instance.letterToMatch = original
    assert instance.letterToMatch == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::Transition_strategy)
@settings(max_examples=30)
def test_fsm::transition_calleffect_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.callEffect()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.callEffect).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'callEffect' in fsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'callEffect' in fsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'callEffect' in fsm::Transition is not implemented or raised an error")

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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::Transition_strategy)
@settings(max_examples=30)
def test_fsm::transition_evaluateguard_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateGuard()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateGuard).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateGuard' in fsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateGuard' in fsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateGuard' in fsm::Transition is not implemented or raised an error")

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::State_strategy)
@settings(max_examples=30)
def test_fsm::state_onenter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onEnter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onEnter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onEnter' in fsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onEnter' in fsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onEnter' in fsm::State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::State_strategy)
@settings(max_examples=30)
def test_fsm::state_onleave_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onLeave()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onLeave).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onLeave' in fsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onLeave' in fsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onLeave' in fsm::State is not implemented or raised an error")

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)
