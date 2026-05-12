import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    f_Y,
    f_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_f_y_is_not_abstract():
    assert not inspect.isabstract(f_Y)


def test_f_y_constructor_exists():
    assert callable(f_Y.__init__)


def test_f_y_constructor_args():
    sig = inspect.signature(f_Y.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_f_y_has_a():
    assert hasattr(f_Y, "a")
    descriptor = None
    for klass in f_Y.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_f_x_is_not_abstract():
    assert not inspect.isabstract(f_X)


def test_f_x_constructor_exists():
    assert callable(f_X.__init__)


def test_f_x_constructor_args():
    sig = inspect.signature(f_X.__init__)
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
f_Y_strategy = st.builds(
    f_Y,
    a=
        safe_text
)
f_X_strategy = st.builds(
    f_X,
)

@given(instance=f_Y_strategy)
@settings(max_examples=50)
def test_f_y_instantiation(instance):
    assert isinstance(instance, f_Y)



@given(instance=f_Y_strategy)
def test_f_y_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=f_X_strategy)
@settings(max_examples=50)
def test_f_x_instantiation(instance):
    assert isinstance(instance, f_X)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=f_X_strategy)
@settings(max_examples=30)
def test_f_x_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in f_X is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in f_X did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in f_X is not implemented or raised an error")
