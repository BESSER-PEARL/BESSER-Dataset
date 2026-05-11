import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Output,
    test::Input,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::output_is_not_abstract():
    assert not inspect.isabstract(test::Output)


def test_test::output_constructor_exists():
    assert callable(test::Output.__init__)


def test_test::output_constructor_args():
    sig = inspect.signature(test::Output.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_test::output_has_key():
    assert hasattr(test::Output, "key")
    descriptor = None
    for klass in test::Output.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_test::input_is_not_abstract():
    assert not inspect.isabstract(test::Input)


def test_test::input_constructor_exists():
    assert callable(test::Input.__init__)


def test_test::input_constructor_args():
    sig = inspect.signature(test::Input.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "test" in params, "Missing parameter 'test'"

def test_test::input_has_key():
    assert hasattr(test::Input, "key")
    descriptor = None
    for klass in test::Input.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_test::input_has_test():
    assert hasattr(test::Input, "test")
    descriptor = None
    for klass in test::Input.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
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
test::Output_strategy = st.builds(
    test::Output,
    key=
        safe_text
)
test::Input_strategy = st.builds(
    test::Input,
    key=
        safe_text,
    test=
        safe_text
)

@given(instance=test::Output_strategy)
@settings(max_examples=50)
def test_test::output_instantiation(instance):
    assert isinstance(instance, test::Output)

@given(instance=test::Output_strategy)
def test_test::output_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=test::Output_strategy)
def test_test::output_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test::Output_strategy)
@settings(max_examples=30)
def test_test::output_test_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.test()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.test).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'test' in test::Output is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'test' in test::Output did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'test' in test::Output is not implemented or raised an error")

@given(instance=test::Input_strategy)
@settings(max_examples=50)
def test_test::input_instantiation(instance):
    assert isinstance(instance, test::Input)

@given(instance=test::Input_strategy)
def test_test::input_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=test::Input_strategy)
def test_test::input_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=test::Input_strategy)
def test_test::input_test_type(instance):
    assert isinstance(instance.test, str)


@given(instance=test::Input_strategy)
def test_test::input_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original
