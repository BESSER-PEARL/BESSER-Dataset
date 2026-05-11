import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    properties::Employee,
    properties::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_properties::employee_is_not_abstract():
    assert not inspect.isabstract(properties::Employee)


def test_properties::employee_constructor_exists():
    assert callable(properties::Employee.__init__)


def test_properties::employee_constructor_args():
    sig = inspect.signature(properties::Employee.__init__)
    params = list(sig.parameters.keys())



def test_properties::department_is_not_abstract():
    assert not inspect.isabstract(properties::Department)


def test_properties::department_constructor_exists():
    assert callable(properties::Department.__init__)


def test_properties::department_constructor_args():
    sig = inspect.signature(properties::Department.__init__)
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
properties::Employee_strategy = st.builds(
    properties::Employee,
)
properties::Department_strategy = st.builds(
    properties::Department,
)

@given(instance=properties::Employee_strategy)
@settings(max_examples=50)
def test_properties::employee_instantiation(instance):
    assert isinstance(instance, properties::Employee)

@given(instance=properties::Department_strategy)
@settings(max_examples=50)
def test_properties::department_instantiation(instance):
    assert isinstance(instance, properties::Department)
