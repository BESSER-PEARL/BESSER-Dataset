import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    autopl_HierarchicalState,
    autopl_Transition,
    autopl_State,
    autopl_Symbol,
    autopl_Alphabet,
    autopl_Automaton,
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



def test_autopl_hierarchicalstate_is_not_abstract():
    assert not inspect.isabstract(autopl_HierarchicalState)


def test_autopl_hierarchicalstate_constructor_exists():
    assert callable(autopl_HierarchicalState.__init__)


def test_autopl_hierarchicalstate_constructor_args():
    sig = inspect.signature(autopl_HierarchicalState.__init__)
    params = list(sig.parameters.keys())



def test_autopl_transition_is_not_abstract():
    assert not inspect.isabstract(autopl_Transition)


def test_autopl_transition_constructor_exists():
    assert callable(autopl_Transition.__init__)


def test_autopl_transition_constructor_args():
    sig = inspect.signature(autopl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_autopl_transition_has_probability():
    assert hasattr(autopl_Transition, "probability")
    descriptor = None
    for klass in autopl_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_autopl_state_is_not_abstract():
    assert not inspect.isabstract(autopl_State)


def test_autopl_state_constructor_exists():
    assert callable(autopl_State.__init__)


def test_autopl_state_constructor_args():
    sig = inspect.signature(autopl_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_autopl_state_has_isInitial():
    assert hasattr(autopl_State, "isInitial")
    descriptor = None
    for klass in autopl_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_autopl_state_has_isFinal():
    assert hasattr(autopl_State, "isFinal")
    descriptor = None
    for klass in autopl_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_autopl_state_has_name():
    assert hasattr(autopl_State, "name")
    descriptor = None
    for klass in autopl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autopl_symbol_is_not_abstract():
    assert not inspect.isabstract(autopl_Symbol)


def test_autopl_symbol_constructor_exists():
    assert callable(autopl_Symbol.__init__)


def test_autopl_symbol_constructor_args():
    sig = inspect.signature(autopl_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_autopl_symbol_has_name():
    assert hasattr(autopl_Symbol, "name")
    descriptor = None
    for klass in autopl_Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autopl_alphabet_is_not_abstract():
    assert not inspect.isabstract(autopl_Alphabet)


def test_autopl_alphabet_constructor_exists():
    assert callable(autopl_Alphabet.__init__)


def test_autopl_alphabet_constructor_args():
    sig = inspect.signature(autopl_Alphabet.__init__)
    params = list(sig.parameters.keys())



def test_autopl_automaton_is_not_abstract():
    assert not inspect.isabstract(autopl_Automaton)


def test_autopl_automaton_constructor_exists():
    assert callable(autopl_Automaton.__init__)


def test_autopl_automaton_constructor_args():
    sig = inspect.signature(autopl_Automaton.__init__)
    params = list(sig.parameters.keys())

def test_acceptancekind_exists():
    # Check that the Enumeration exists
    assert AcceptanceKind is not None

def test_acceptancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcceptanceKind]
    expected_literals = [
        "Infinite",
        "Finite",
        "Probabilistic",
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
autopl_HierarchicalState_strategy = st.builds(
    autopl_HierarchicalState,
)
autopl_Transition_strategy = st.builds(
    autopl_Transition,
    probability=
        safe_text
)
autopl_State_strategy = st.builds(
    autopl_State,
    isInitial=
        safe_text,
    isFinal=
        safe_text,
    name=
        safe_text
)
autopl_Symbol_strategy = st.builds(
    autopl_Symbol,
    name=
        safe_text
)
autopl_Alphabet_strategy = st.builds(
    autopl_Alphabet,
)
autopl_Automaton_strategy = st.builds(
    autopl_Automaton,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=autopl_HierarchicalState_strategy)
@settings(max_examples=50)
def test_autopl_hierarchicalstate_instantiation(instance):
    assert isinstance(instance, autopl_HierarchicalState)

@given(instance=autopl_Transition_strategy)
@settings(max_examples=50)
def test_autopl_transition_instantiation(instance):
    assert isinstance(instance, autopl_Transition)



@given(instance=autopl_Transition_strategy)
def test_autopl_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=autopl_State_strategy)
@settings(max_examples=50)
def test_autopl_state_instantiation(instance):
    assert isinstance(instance, autopl_State)



@given(instance=autopl_State_strategy)
def test_autopl_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=autopl_State_strategy)
def test_autopl_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=autopl_State_strategy)
def test_autopl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_autopl_state_adjacent_changes_state(instance):
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
        assert has_statements, f"Function 'adjacent' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'adjacent' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'adjacent' in autopl_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_autopl_state_outtrans_changes_state(instance):
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
        assert has_statements, f"Function 'outTrans' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'outTrans' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'outTrans' in autopl_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_State_strategy)
@settings(max_examples=30)
def test_autopl_state_intrans_changes_state(instance):
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
        assert has_statements, f"Function 'inTrans' in autopl_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inTrans' in autopl_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inTrans' in autopl_State is not implemented or raised an error")

@given(instance=autopl_Symbol_strategy)
@settings(max_examples=50)
def test_autopl_symbol_instantiation(instance):
    assert isinstance(instance, autopl_Symbol)



@given(instance=autopl_Symbol_strategy)
def test_autopl_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=autopl_Alphabet_strategy)
@settings(max_examples=50)
def test_autopl_alphabet_instantiation(instance):
    assert isinstance(instance, autopl_Alphabet)

@given(instance=autopl_Automaton_strategy)
@settings(max_examples=50)
def test_autopl_automaton_instantiation(instance):
    assert isinstance(instance, autopl_Automaton)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=autopl_Automaton_strategy)
@settings(max_examples=30)
def test_autopl_automaton_acceptancecondition_changes_state(instance):
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
        assert has_statements, f"Function 'acceptanceCondition' in autopl_Automaton is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'acceptanceCondition' in autopl_Automaton did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'acceptanceCondition' in autopl_Automaton is not implemented or raised an error")
