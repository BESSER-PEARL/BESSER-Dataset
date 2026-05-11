import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    employee::Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee::employee_is_not_abstract():
    assert not inspect.isabstract(employee::Employee)


def test_employee::employee_constructor_exists():
    assert callable(employee::Employee.__init__)


def test_employee::employee_constructor_args():
    sig = inspect.signature(employee::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accounts" in params, "Missing parameter 'accounts'"

def test_employee::employee_has_name():
    assert hasattr(employee::Employee, "name")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employee::employee_has_accounts():
    assert hasattr(employee::Employee, "accounts")
    descriptor = None
    for klass in employee::Employee.__mro__:
        if "accounts" in klass.__dict__:
            descriptor = klass.__dict__["accounts"]
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
employee::Employee_strategy = st.builds(
    employee::Employee,
    name=
        safe_text,
    accounts=
        safe_text
)

@given(instance=employee::Employee_strategy)
@settings(max_examples=50)
def test_employee::employee_instantiation(instance):
    assert isinstance(instance, employee::Employee)

@given(instance=employee::Employee_strategy)
def test_employee::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=employee::Employee_strategy)
def test_employee::employee_accounts_type(instance):
    assert isinstance(instance.accounts, str)


@given(instance=employee::Employee_strategy)
def test_employee::employee_accounts_setter(instance):
    original = instance.accounts
    instance.accounts = original
    assert instance.accounts == original
