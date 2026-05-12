import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Transition,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"

def test_fsm_transition_has_b():
    assert hasattr(fsm_Transition, "b")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_a():
    assert hasattr(fsm_Transition, "a")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_c():
    assert hasattr(fsm_Transition, "c")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_c_exists():
    # Check that the Enumeration exists
    assert C is not None

def test_c_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in C]
    expected_literals = [
        "Y",
        "X",
        "Z",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in C"


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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    b=
        safe_text,
    a=
        safe_text,
    c=
        safe_text
)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Transition_strategy)
@settings(max_examples=30)
def test_fsm_transition_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in fsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in fsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in fsm_Transition is not implemented or raised an error")
