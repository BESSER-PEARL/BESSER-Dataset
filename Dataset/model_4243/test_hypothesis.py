import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    properties_Employee,
    properties_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_properties_employee_is_not_abstract():
    assert not inspect.isabstract(properties_Employee)


def test_properties_employee_constructor_exists():
    assert callable(properties_Employee.__init__)


def test_properties_employee_constructor_args():
    sig = inspect.signature(properties_Employee.__init__)
    params = list(sig.parameters.keys())



def test_properties_department_is_not_abstract():
    assert not inspect.isabstract(properties_Department)


def test_properties_department_constructor_exists():
    assert callable(properties_Department.__init__)


def test_properties_department_constructor_args():
    sig = inspect.signature(properties_Department.__init__)
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
properties_Employee_strategy = st.builds(
    properties_Employee,
)
properties_Department_strategy = st.builds(
    properties_Department,
)

@given(instance=properties_Employee_strategy)
@settings(max_examples=50)
def test_properties_employee_instantiation(instance):
    assert isinstance(instance, properties_Employee)

@given(instance=properties_Department_strategy)
@settings(max_examples=50)
def test_properties_department_instantiation(instance):
    assert isinstance(instance, properties_Department)
