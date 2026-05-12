import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    panamaRelational_PanamaOfficers,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_panamarelational_panamaofficers_is_not_abstract():
    assert not inspect.isabstract(panamaRelational_PanamaOfficers)


def test_panamarelational_panamaofficers_constructor_exists():
    assert callable(panamaRelational_PanamaOfficers.__init__)


def test_panamarelational_panamaofficers_constructor_args():
    sig = inspect.signature(panamaRelational_PanamaOfficers.__init__)
    params = list(sig.parameters.keys())
    assert "company" in params, "Missing parameter 'company'"
    assert "name" in params, "Missing parameter 'name'"

def test_panamarelational_panamaofficers_has_company():
    assert hasattr(panamaRelational_PanamaOfficers, "company")
    descriptor = None
    for klass in panamaRelational_PanamaOfficers.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_panamarelational_panamaofficers_has_name():
    assert hasattr(panamaRelational_PanamaOfficers, "name")
    descriptor = None
    for klass in panamaRelational_PanamaOfficers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
panamaRelational_PanamaOfficers_strategy = st.builds(
    panamaRelational_PanamaOfficers,
    company=
        safe_text,
    name=
        safe_text
)

@given(instance=panamaRelational_PanamaOfficers_strategy)
@settings(max_examples=50)
def test_panamarelational_panamaofficers_instantiation(instance):
    assert isinstance(instance, panamaRelational_PanamaOfficers)



@given(instance=panamaRelational_PanamaOfficers_strategy)
def test_panamarelational_panamaofficers_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=panamaRelational_PanamaOfficers_strategy)
def test_panamarelational_panamaofficers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
