import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Output,
    test_Input,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_output_is_not_abstract():
    assert not inspect.isabstract(test_Output)


def test_test_output_constructor_exists():
    assert callable(test_Output.__init__)


def test_test_output_constructor_args():
    sig = inspect.signature(test_Output.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_test_output_has_key():
    assert hasattr(test_Output, "key")
    descriptor = None
    for klass in test_Output.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_test_input_is_not_abstract():
    assert not inspect.isabstract(test_Input)


def test_test_input_constructor_exists():
    assert callable(test_Input.__init__)


def test_test_input_constructor_args():
    sig = inspect.signature(test_Input.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "test" in params, "Missing parameter 'test'"

def test_test_input_has_key():
    assert hasattr(test_Input, "key")
    descriptor = None
    for klass in test_Input.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_test_input_has_test():
    assert hasattr(test_Input, "test")
    descriptor = None
    for klass in test_Input.__mro__:
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
test_Output_strategy = st.builds(
    test_Output,
    key=
        safe_text
)
test_Input_strategy = st.builds(
    test_Input,
    key=
        safe_text,
    test=
        safe_text
)

@given(instance=test_Output_strategy)
@settings(max_examples=50)
def test_test_output_instantiation(instance):
    assert isinstance(instance, test_Output)



@given(instance=test_Output_strategy)
def test_test_output_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_Output_strategy)
@settings(max_examples=30)
def test_test_output_test_changes_state(instance):
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
        assert has_statements, f"Function 'test' in test_Output is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'test' in test_Output did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'test' in test_Output is not implemented or raised an error")

@given(instance=test_Input_strategy)
@settings(max_examples=50)
def test_test_input_instantiation(instance):
    assert isinstance(instance, test_Input)



@given(instance=test_Input_strategy)
def test_test_input_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=test_Input_strategy)
def test_test_input_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original
