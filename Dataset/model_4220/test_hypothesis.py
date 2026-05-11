import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CompanyModel::Product,
    CompanyModel::Employee,
    CompanyModel::Department,
    CompanyModel::Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companymodel::product_is_not_abstract():
    assert not inspect.isabstract(CompanyModel::Product)


def test_companymodel::product_constructor_exists():
    assert callable(CompanyModel::Product.__init__)


def test_companymodel::product_constructor_args():
    sig = inspect.signature(CompanyModel::Product.__init__)
    params = list(sig.parameters.keys())
    assert "productID" in params, "Missing parameter 'productID'"
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel::product_has_productID():
    assert hasattr(CompanyModel::Product, "productID")
    descriptor = None
    for klass in CompanyModel::Product.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_companymodel::product_has_name():
    assert hasattr(CompanyModel::Product, "name")
    descriptor = None
    for klass in CompanyModel::Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companymodel::employee_is_not_abstract():
    assert not inspect.isabstract(CompanyModel::Employee)


def test_companymodel::employee_constructor_exists():
    assert callable(CompanyModel::Employee.__init__)


def test_companymodel::employee_constructor_args():
    sig = inspect.signature(CompanyModel::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "isManager" in params, "Missing parameter 'isManager'"
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel::employee_has_isManager():
    assert hasattr(CompanyModel::Employee, "isManager")
    descriptor = None
    for klass in CompanyModel::Employee.__mro__:
        if "isManager" in klass.__dict__:
            descriptor = klass.__dict__["isManager"]
            break
    assert isinstance(descriptor, property)

def test_companymodel::employee_has_name():
    assert hasattr(CompanyModel::Employee, "name")
    descriptor = None
    for klass in CompanyModel::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companymodel::department_is_not_abstract():
    assert not inspect.isabstract(CompanyModel::Department)


def test_companymodel::department_constructor_exists():
    assert callable(CompanyModel::Department.__init__)


def test_companymodel::department_constructor_args():
    sig = inspect.signature(CompanyModel::Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_companymodel::department_has_number():
    assert hasattr(CompanyModel::Department, "number")
    descriptor = None
    for klass in CompanyModel::Department.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_companymodel::company_is_not_abstract():
    assert not inspect.isabstract(CompanyModel::Company)


def test_companymodel::company_constructor_exists():
    assert callable(CompanyModel::Company.__init__)


def test_companymodel::company_constructor_args():
    sig = inspect.signature(CompanyModel::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel::company_has_name():
    assert hasattr(CompanyModel::Company, "name")
    descriptor = None
    for klass in CompanyModel::Company.__mro__:
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
CompanyModel::Product_strategy = st.builds(
    CompanyModel::Product,
    productID=
        st.integers(),
    name=
        safe_text
)
CompanyModel::Employee_strategy = st.builds(
    CompanyModel::Employee,
    isManager=
        st.booleans(),
    name=
        safe_text
)
CompanyModel::Department_strategy = st.builds(
    CompanyModel::Department,
    number=
        st.integers()
)
CompanyModel::Company_strategy = st.builds(
    CompanyModel::Company,
    name=
        safe_text
)

@given(instance=CompanyModel::Product_strategy)
@settings(max_examples=50)
def test_companymodel::product_instantiation(instance):
    assert isinstance(instance, CompanyModel::Product)

@given(instance=CompanyModel::Product_strategy)
def test_companymodel::product_productID_type(instance):
    assert isinstance(instance.productID, int)


@given(instance=CompanyModel::Product_strategy)
def test_companymodel::product_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original

@given(instance=CompanyModel::Product_strategy)
def test_companymodel::product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyModel::Product_strategy)
def test_companymodel::product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyModel::Employee_strategy)
@settings(max_examples=50)
def test_companymodel::employee_instantiation(instance):
    assert isinstance(instance, CompanyModel::Employee)

@given(instance=CompanyModel::Employee_strategy)
def test_companymodel::employee_isManager_type(instance):
    assert isinstance(instance.isManager, bool)


@given(instance=CompanyModel::Employee_strategy)
def test_companymodel::employee_isManager_setter(instance):
    original = instance.isManager
    instance.isManager = original
    assert instance.isManager == original

@given(instance=CompanyModel::Employee_strategy)
def test_companymodel::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyModel::Employee_strategy)
def test_companymodel::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyModel::Department_strategy)
@settings(max_examples=50)
def test_companymodel::department_instantiation(instance):
    assert isinstance(instance, CompanyModel::Department)

@given(instance=CompanyModel::Department_strategy)
def test_companymodel::department_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=CompanyModel::Department_strategy)
def test_companymodel::department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=CompanyModel::Company_strategy)
@settings(max_examples=50)
def test_companymodel::company_instantiation(instance):
    assert isinstance(instance, CompanyModel::Company)

@given(instance=CompanyModel::Company_strategy)
def test_companymodel::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompanyModel::Company_strategy)
def test_companymodel::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
