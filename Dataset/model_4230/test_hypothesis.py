import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CompanyLanguage_Company,
    CompanyLanguage_Employee,
    CompanyLanguage_CEO,
    CompanyLanguage_Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companylanguage_company_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage_Company)


def test_companylanguage_company_constructor_exists():
    assert callable(CompanyLanguage_Company.__init__)


def test_companylanguage_company_constructor_args():
    sig = inspect.signature(CompanyLanguage_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage_company_has_name():
    assert hasattr(CompanyLanguage_Company, "name")
    descriptor = None
    for klass in CompanyLanguage_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage_employee_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage_Employee)


def test_companylanguage_employee_constructor_exists():
    assert callable(CompanyLanguage_Employee.__init__)


def test_companylanguage_employee_constructor_args():
    sig = inspect.signature(CompanyLanguage_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage_employee_has_name():
    assert hasattr(CompanyLanguage_Employee, "name")
    descriptor = None
    for klass in CompanyLanguage_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage_ceo_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage_CEO)


def test_companylanguage_ceo_constructor_exists():
    assert callable(CompanyLanguage_CEO.__init__)


def test_companylanguage_ceo_constructor_args():
    sig = inspect.signature(CompanyLanguage_CEO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage_ceo_has_name():
    assert hasattr(CompanyLanguage_CEO, "name")
    descriptor = None
    for klass in CompanyLanguage_CEO.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companylanguage_admin_is_not_abstract():
    assert not inspect.isabstract(CompanyLanguage_Admin)


def test_companylanguage_admin_constructor_exists():
    assert callable(CompanyLanguage_Admin.__init__)


def test_companylanguage_admin_constructor_args():
    sig = inspect.signature(CompanyLanguage_Admin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companylanguage_admin_has_name():
    assert hasattr(CompanyLanguage_Admin, "name")
    descriptor = None
    for klass in CompanyLanguage_Admin.__mro__:
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
CompanyLanguage_Company_strategy = st.builds(
    CompanyLanguage_Company,
    name=
        safe_text
)
CompanyLanguage_Employee_strategy = st.builds(
    CompanyLanguage_Employee,
    name=
        safe_text
)
CompanyLanguage_CEO_strategy = st.builds(
    CompanyLanguage_CEO,
    name=
        safe_text
)
CompanyLanguage_Admin_strategy = st.builds(
    CompanyLanguage_Admin,
    name=
        safe_text
)

@given(instance=CompanyLanguage_Company_strategy)
@settings(max_examples=50)
def test_companylanguage_company_instantiation(instance):
    assert isinstance(instance, CompanyLanguage_Company)



@given(instance=CompanyLanguage_Company_strategy)
def test_companylanguage_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage_Employee_strategy)
@settings(max_examples=50)
def test_companylanguage_employee_instantiation(instance):
    assert isinstance(instance, CompanyLanguage_Employee)



@given(instance=CompanyLanguage_Employee_strategy)
def test_companylanguage_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage_CEO_strategy)
@settings(max_examples=50)
def test_companylanguage_ceo_instantiation(instance):
    assert isinstance(instance, CompanyLanguage_CEO)



@given(instance=CompanyLanguage_CEO_strategy)
def test_companylanguage_ceo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyLanguage_Admin_strategy)
@settings(max_examples=50)
def test_companylanguage_admin_instantiation(instance):
    assert isinstance(instance, CompanyLanguage_Admin)



@given(instance=CompanyLanguage_Admin_strategy)
def test_companylanguage_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
