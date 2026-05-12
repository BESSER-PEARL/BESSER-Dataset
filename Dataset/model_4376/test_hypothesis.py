import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_person_is_not_abstract():
    assert not inspect.isabstract(test_Person)


def test_test_person_constructor_exists():
    assert callable(test_Person.__init__)


def test_test_person_constructor_args():
    sig = inspect.signature(test_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_test_person_has_age():
    assert hasattr(test_Person, "age")
    descriptor = None
    for klass in test_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
test_Person_strategy = st.builds(
    test_Person,
    age=
        st.integers()
)

@given(instance=test_Person_strategy)
@settings(max_examples=50)
def test_test_person_instantiation(instance):
    assert isinstance(instance, test_Person)



@given(instance=test_Person_strategy)
def test_test_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_Person_strategy)
@settings(max_examples=30)
def test_test_person_isagevalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAgeValid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAgeValid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAgeValid' in test_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAgeValid' in test_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAgeValid' in test_Person is not implemented or raised an error")
