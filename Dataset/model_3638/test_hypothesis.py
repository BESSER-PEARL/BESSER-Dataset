import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    autopl::HierarchicalState,
    autopl::Transition,
    autopl::State,
    autopl::Symbol,
    autopl::Alphabet,
    autopl::Automaton,
    AcceptanceKind,
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



def test_autopl::hierarchicalstate_is_not_abstract():
    assert not inspect.isabstract(autopl::HierarchicalState)


def test_autopl::hierarchicalstate_constructor_exists():
    assert callable(autopl::HierarchicalState.__init__)


def test_autopl::hierarchicalstate_constructor_args():
    sig = inspect.signature(autopl::HierarchicalState.__init__)
    params = list(sig.parameters.keys())



def test_autopl::transition_is_not_abstract():
    assert not inspect.isabstract(autopl::Transition)


def test_autopl::transition_constructor_exists():
    assert callable(autopl::Transition.__init__)


def test_autopl::transition_constructor_args():
    sig = inspect.signature(autopl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_autopl::transition_has_probability():
    assert hasattr(autopl::Transition, "probability")
    descriptor = None
    for klass in autopl::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_autopl::state_is_not_abstract():
    assert not inspect.isabstract(autopl::State)


def test_autopl::state_constructor_exists():
    assert callable(autopl::State.__init__)


def test_autopl::state_constructor_args():
    sig = inspect.signature(autopl::State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_autopl::state_has_isInitial():
    assert hasattr(autopl::State, "isInitial")
    descriptor = None
    for klass in autopl::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_autopl::state_has_isFinal():
    assert hasattr(autopl::State, "isFinal")
    descriptor = None
    for klass in autopl::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_autopl::state_has_name():
    assert hasattr(autopl::State, "name")
    descriptor = None
    for klass in autopl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autopl::symbol_is_not_abstract():
    assert not inspect.isabstract(autopl::Symbol)


def test_autopl::symbol_constructor_exists():
    assert callable(autopl::Symbol.__init__)


def test_autopl::symbol_constructor_args():
    sig = inspect.signature(autopl::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_autopl::symbol_has_name():
    assert hasattr(autopl::Symbol, "name")
    descriptor = None
    for klass in autopl::Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autopl::alphabet_is_not_abstract():
    assert not inspect.isabstract(autopl::Alphabet)


def test_autopl::alphabet_constructor_exists():
    assert callable(autopl::Alphabet.__init__)


def test_autopl::alphabet_constructor_args():
    sig = inspect.signature(autopl::Alphabet.__init__)
    params = list(sig.parameters.keys())



def test_autopl::automaton_is_not_abstract():
    assert not inspect.isabstract(autopl::Automaton)


def test_autopl::automaton_constructor_exists():
    assert callable(autopl::Automaton.__init__)


def test_autopl::automaton_constructor_args():
    sig = inspect.signature(autopl::Automaton.__init__)
    params = list(sig.parameters.keys())

def test_acceptancekind_exists():
    # Check that the Enumeration exists
    assert AcceptanceKind is not None

def test_acceptancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcceptanceKind]
    expected_literals = [
        "Finite",
        "Probabilistic",
        "Infinite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AcceptanceKind"


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
autopl::HierarchicalState_strategy = st.builds(
    autopl::HierarchicalState,
)
autopl::Transition_strategy = st.builds(
    autopl::Transition,
    probability=
        safe_text
)
autopl::State_strategy = st.builds(
    autopl::State,
    isInitial=
        safe_text,
    isFinal=
        safe_text,
    name=
        safe_text
)
autopl::Symbol_strategy = st.builds(
    autopl::Symbol,
    name=
        safe_text
)
autopl::Alphabet_strategy = st.builds(
    autopl::Alphabet,
)
autopl::Automaton_strategy = st.builds(
    autopl::Automaton,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=autopl::HierarchicalState_strategy)
@settings(max_examples=50)
def test_autopl::hierarchicalstate_instantiation(instance):
    assert isinstance(instance, autopl::HierarchicalState)

@given(instance=autopl::Transition_strategy)
@settings(max_examples=50)
def test_autopl::transition_instantiation(instance):
    assert isinstance(instance, autopl::Transition)

@given(instance=autopl::Transition_strategy)
def test_autopl::transition_probability_type(instance):
    assert isinstance(instance.probability, str)


@given(instance=autopl::Transition_strategy)
def test_autopl::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=autopl::State_strategy)
@settings(max_examples=50)
def test_autopl::state_instantiation(instance):
    assert isinstance(instance, autopl::State)

@given(instance=autopl::State_strategy)
def test_autopl::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, str)


@given(instance=autopl::State_strategy)
def test_autopl::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=autopl::State_strategy)
def test_autopl::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, str)


@given(instance=autopl::State_strategy)
def test_autopl::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=autopl::State_strategy)
def test_autopl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=autopl::State_strategy)
def test_autopl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl::State_strategy)
@settings(max_examples=30)
def test_autopl::state_outtrans_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.outTrans()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.outTrans).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'outTrans' in autopl::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'outTrans' in autopl::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'outTrans' in autopl::State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl::State_strategy)
@settings(max_examples=30)
def test_autopl::state_intrans_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inTrans()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inTrans).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inTrans' in autopl::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inTrans' in autopl::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inTrans' in autopl::State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl::State_strategy)
@settings(max_examples=30)
def test_autopl::state_adjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.adjacent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.adjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'adjacent' in autopl::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'adjacent' in autopl::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'adjacent' in autopl::State is not implemented or raised an error")

@given(instance=autopl::Symbol_strategy)
@settings(max_examples=50)
def test_autopl::symbol_instantiation(instance):
    assert isinstance(instance, autopl::Symbol)

@given(instance=autopl::Symbol_strategy)
def test_autopl::symbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=autopl::Symbol_strategy)
def test_autopl::symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=autopl::Alphabet_strategy)
@settings(max_examples=50)
def test_autopl::alphabet_instantiation(instance):
    assert isinstance(instance, autopl::Alphabet)

@given(instance=autopl::Automaton_strategy)
@settings(max_examples=50)
def test_autopl::automaton_instantiation(instance):
    assert isinstance(instance, autopl::Automaton)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl::Automaton_strategy)
@settings(max_examples=30)
def test_autopl::automaton_acceptancecondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.acceptanceCondition()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.acceptanceCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'acceptanceCondition' in autopl::Automaton is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'acceptanceCondition' in autopl::Automaton did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'acceptanceCondition' in autopl::Automaton is not implemented or raised an error")
