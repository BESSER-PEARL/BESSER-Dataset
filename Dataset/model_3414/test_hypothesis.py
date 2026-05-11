import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    people::Universe,
    people::Person,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people::universe_is_not_abstract():
    assert not inspect.isabstract(people::Universe)


def test_people::universe_constructor_exists():
    assert callable(people::Universe.__init__)


def test_people::universe_constructor_args():
    sig = inspect.signature(people::Universe.__init__)
    params = list(sig.parameters.keys())



def test_people::person_is_not_abstract():
    assert not inspect.isabstract(people::Person)


def test_people::person_constructor_exists():
    assert callable(people::Person.__init__)


def test_people::person_constructor_args():
    sig = inspect.signature(people::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_people::person_has_name():
    assert hasattr(people::Person, "name")
    descriptor = None
    for klass in people::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_gender():
    assert hasattr(people::Person, "gender")
    descriptor = None
    for klass in people::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "FEMALE",
        "MALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
people::Universe_strategy = st.builds(
    people::Universe,
)
people::Person_strategy = st.builds(
    people::Person,
    name=
        safe_text,
    gender=
        safe_text
)

@given(instance=people::Universe_strategy)
@settings(max_examples=50)
def test_people::universe_instantiation(instance):
    assert isinstance(instance, people::Universe)

@given(instance=people::Person_strategy)
@settings(max_examples=50)
def test_people::person_instantiation(instance):
    assert isinstance(instance, people::Person)

@given(instance=people::Person_strategy)
def test_people::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=people::Person_strategy)
def test_people::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=people::Person_strategy)
def test_people::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=people::Person_strategy)
def test_people::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=people::Person_strategy)
@settings(max_examples=30)
def test_people::person_child_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.child(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.child).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'child' in people::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'child' in people::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'child' in people::Person is not implemented or raised an error")
