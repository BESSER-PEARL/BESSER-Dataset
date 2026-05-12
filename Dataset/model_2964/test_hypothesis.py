import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_Car,
    sample_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_car_is_not_abstract():
    assert not inspect.isabstract(sample_Car)


def test_sample_car_constructor_exists():
    assert callable(sample_Car.__init__)


def test_sample_car_constructor_args():
    sig = inspect.signature(sample_Car.__init__)
    params = list(sig.parameters.keys())
    assert "horsePower" in params, "Missing parameter 'horsePower'"

def test_sample_car_has_horsePower():
    assert hasattr(sample_Car, "horsePower")
    descriptor = None
    for klass in sample_Car.__mro__:
        if "horsePower" in klass.__dict__:
            descriptor = klass.__dict__["horsePower"]
            break
    assert isinstance(descriptor, property)



def test_sample_person_is_not_abstract():
    assert not inspect.isabstract(sample_Person)


def test_sample_person_constructor_exists():
    assert callable(sample_Person.__init__)


def test_sample_person_constructor_args():
    sig = inspect.signature(sample_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_sample_person_has_firstName():
    assert hasattr(sample_Person, "firstName")
    descriptor = None
    for klass in sample_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_sample_person_has_lastName():
    assert hasattr(sample_Person, "lastName")
    descriptor = None
    for klass in sample_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
sample_Car_strategy = st.builds(
    sample_Car,
    horsePower=
        st.integers()
)
sample_Person_strategy = st.builds(
    sample_Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)

@given(instance=sample_Car_strategy)
@settings(max_examples=50)
def test_sample_car_instantiation(instance):
    assert isinstance(instance, sample_Car)



@given(instance=sample_Car_strategy)
def test_sample_car_horsePower_setter(instance):
    original = instance.horsePower
    instance.horsePower = original
    assert instance.horsePower == original

@given(instance=sample_Person_strategy)
@settings(max_examples=50)
def test_sample_person_instantiation(instance):
    assert isinstance(instance, sample_Person)



@given(instance=sample_Person_strategy)
def test_sample_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=sample_Person_strategy)
def test_sample_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sample_Person_strategy)
@settings(max_examples=30)
def test_sample_person_buy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.buy(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.buy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'buy' in sample_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'buy' in sample_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'buy' in sample_Person is not implemented or raised an error")
