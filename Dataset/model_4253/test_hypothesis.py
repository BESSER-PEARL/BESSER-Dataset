import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    employee_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_employee_is_not_abstract():
    assert not inspect.isabstract(employee_Employee)


def test_employee_employee_constructor_exists():
    assert callable(employee_Employee.__init__)


def test_employee_employee_constructor_args():
    sig = inspect.signature(employee_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accounts" in params, "Missing parameter 'accounts'"

def test_employee_employee_has_name():
    assert hasattr(employee_Employee, "name")
    descriptor = None
    for klass in employee_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employee_employee_has_accounts():
    assert hasattr(employee_Employee, "accounts")
    descriptor = None
    for klass in employee_Employee.__mro__:
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
employee_Employee_strategy = st.builds(
    employee_Employee,
    name=
        safe_text,
    accounts=
        safe_text
)

@given(instance=employee_Employee_strategy)
@settings(max_examples=50)
def test_employee_employee_instantiation(instance):
    assert isinstance(instance, employee_Employee)



@given(instance=employee_Employee_strategy)
def test_employee_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=employee_Employee_strategy)
def test_employee_employee_accounts_setter(instance):
    original = instance.accounts
    instance.accounts = original
    assert instance.accounts == original
