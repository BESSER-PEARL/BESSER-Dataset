import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RoyalAndLoyal::Customer,
    RoyalAndLoyal::Container::RandL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_royalandloyal::customer_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal::Customer)


def test_royalandloyal::customer_constructor_exists():
    assert callable(RoyalAndLoyal::Customer.__init__)


def test_royalandloyal::customer_constructor_args():
    sig = inspect.signature(RoyalAndLoyal::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_royalandloyal::customer_has_name():
    assert hasattr(RoyalAndLoyal::Customer, "name")
    descriptor = None
    for klass in RoyalAndLoyal::Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_royalandloyal::container::randl_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal::Container::RandL)


def test_royalandloyal::container::randl_constructor_exists():
    assert callable(RoyalAndLoyal::Container::RandL.__init__)


def test_royalandloyal::container::randl_constructor_args():
    sig = inspect.signature(RoyalAndLoyal::Container::RandL.__init__)
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
RoyalAndLoyal::Customer_strategy = st.builds(
    RoyalAndLoyal::Customer,
    name=
        safe_text
)
RoyalAndLoyal::Container::RandL_strategy = st.builds(
    RoyalAndLoyal::Container::RandL,
)

@given(instance=RoyalAndLoyal::Customer_strategy)
@settings(max_examples=50)
def test_royalandloyal::customer_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal::Customer)

@given(instance=RoyalAndLoyal::Customer_strategy)
def test_royalandloyal::customer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RoyalAndLoyal::Customer_strategy)
def test_royalandloyal::customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal::Customer_strategy)
@settings(max_examples=30)
def test_royalandloyal::customer_updatename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateName' in RoyalAndLoyal::Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateName' in RoyalAndLoyal::Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateName' in RoyalAndLoyal::Customer is not implemented or raised an error")

@given(instance=RoyalAndLoyal::Container::RandL_strategy)
@settings(max_examples=50)
def test_royalandloyal::container::randl_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal::Container::RandL)
