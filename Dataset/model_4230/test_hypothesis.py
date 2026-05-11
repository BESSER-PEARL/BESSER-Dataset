import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CompanyLanguage::Company,
    CompanyLanguage::Employee,
    CompanyLanguage::CEO,
    CompanyLanguage::Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companylanguage::company_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage::Company)


def test_companylanguage::company_constructor_exists():
    assert callable(CompanyLanguage::Company.__init__)


def test_companylanguage::company_constructor_args():
    sig = inspect.signature(CompanyLanguage::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage::company_has_name():
    assert hasattr(CompanyLanguage::Company, "name")
    descriptor = None
    for klass in CompanyLanguage::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage::employee_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage::Employee)


def test_companylanguage::employee_constructor_exists():
    assert callable(CompanyLanguage::Employee.__init__)


def test_companylanguage::employee_constructor_args():
    sig = inspect.signature(CompanyLanguage::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage::employee_has_name():
    assert hasattr(CompanyLanguage::Employee, "name")
    descriptor = None
    for klass in CompanyLanguage::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage::ceo_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage::CEO)


def test_companylanguage::ceo_constructor_exists():
    assert callable(CompanyLanguage::CEO.__init__)


def test_companylanguage::ceo_constructor_args():
    sig = inspect.signature(CompanyLanguage::CEO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage::ceo_has_name():
    assert hasattr(CompanyLanguage::CEO, "name")
    descriptor = None
    for klass in CompanyLanguage::CEO.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage::admin_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage::Admin)


def test_companylanguage::admin_constructor_exists():
    assert callable(CompanyLanguage::Admin.__init__)


def test_companylanguage::admin_constructor_args():
    sig = inspect.signature(CompanyLanguage::Admin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage::admin_has_name():
    assert hasattr(CompanyLanguage::Admin, "name")
    descriptor = None
    for klass in CompanyLanguage::Admin.__mro__:
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
CompanyLanguage::Company_strategy = st.builds(
    CompanyLanguage::Company,
    name=
        safe_text
)
CompanyLanguage::Employee_strategy = st.builds(
    CompanyLanguage::Employee,
    name=
        safe_text
)
CompanyLanguage::CEO_strategy = st.builds(
    CompanyLanguage::CEO,
    name=
        safe_text
)
CompanyLanguage::Admin_strategy = st.builds(
    CompanyLanguage::Admin,
    name=
        safe_text
)

@given(instance=CompanyLanguage::Company_strategy)
@settings(max_examples=50)
def test_companylanguage::company_instantiation(instance):
    assert isinstance(instance, CompanyLanguage::Company)

@given(instance=CompanyLanguage::Company_strategy)
def test_companylanguage::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyLanguage::Company_strategy)
def test_companylanguage::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage::Employee_strategy)
@settings(max_examples=50)
def test_companylanguage::employee_instantiation(instance):
    assert isinstance(instance, CompanyLanguage::Employee)

@given(instance=CompanyLanguage::Employee_strategy)
def test_companylanguage::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyLanguage::Employee_strategy)
def test_companylanguage::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage::CEO_strategy)
@settings(max_examples=50)
def test_companylanguage::ceo_instantiation(instance):
    assert isinstance(instance, CompanyLanguage::CEO)

@given(instance=CompanyLanguage::CEO_strategy)
def test_companylanguage::ceo_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyLanguage::CEO_strategy)
def test_companylanguage::ceo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage::Admin_strategy)
@settings(max_examples=50)
def test_companylanguage::admin_instantiation(instance):
    assert isinstance(instance, CompanyLanguage::Admin)

@given(instance=CompanyLanguage::Admin_strategy)
def test_companylanguage::admin_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyLanguage::Admin_strategy)
def test_companylanguage::admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
