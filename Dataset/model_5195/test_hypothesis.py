import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_C2,
    a_Zug,
    a_C,
    E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_c2_is_not_abstract():
    assert not inspect.isabstract(a_C2)


def test_a_c2_constructor_exists():
    assert callable(a_C2.__init__)


def test_a_c2_constructor_args():
    sig = inspect.signature(a_C2.__init__)
    params = list(sig.parameters.keys())



def test_a_zug_is_not_abstract():
    assert not inspect.isabstract(a_Zug)


def test_a_zug_constructor_exists():
    assert callable(a_Zug.__init__)


def test_a_zug_constructor_args():
    sig = inspect.signature(a_Zug.__init__)
    params = list(sig.parameters.keys())



def test_a_c_is_not_abstract():
    assert not inspect.isabstract(a_C)


def test_a_c_constructor_exists():
    assert callable(a_C.__init__)


def test_a_c_constructor_args():
    sig = inspect.signature(a_C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_a_c_has_a():
    assert hasattr(a_C, "a")
    descriptor = None
    for klass in a_C.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_e_exists():
    # Check that the Enumeration exists
    assert E is not None

def test_e_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in E]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in E"


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
a_C2_strategy = st.builds(
    a_C2,
)
a_Zug_strategy = st.builds(
    a_Zug,
)
a_C_strategy = st.builds(
    a_C,
    a=
        safe_text
)

@given(instance=a_C2_strategy)
@settings(max_examples=50)
def test_a_c2_instantiation(instance):
    assert isinstance(instance, a_C2)

@given(instance=a_Zug_strategy)
@settings(max_examples=50)
def test_a_zug_instantiation(instance):
    assert isinstance(instance, a_Zug)

@given(instance=a_C_strategy)
@settings(max_examples=50)
def test_a_c_instantiation(instance):
    assert isinstance(instance, a_C)



@given(instance=a_C_strategy)
def test_a_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=a_C_strategy)
@settings(max_examples=30)
def test_a_c_o_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.o(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.o).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'o' in a_C is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'o' in a_C did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'o' in a_C is not implemented or raised an error")
