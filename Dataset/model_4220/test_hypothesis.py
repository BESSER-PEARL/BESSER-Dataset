import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CompanyModel_Product,
    CompanyModel_Employee,
    CompanyModel_Department,
    CompanyModel_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_companymodel_product_is_not_abstract():
    assert not inspect.isabstract(CompanyModel_Product)


def test_companymodel_product_constructor_exists():
    assert callable(CompanyModel_Product.__init__)


def test_companymodel_product_constructor_args():
    sig = inspect.signature(CompanyModel_Product.__init__)
    params = list(sig.parameters.keys())
    assert "productID" in params, "Missing parameter 'productID'"
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel_product_has_productID():
    assert hasattr(CompanyModel_Product, "productID")
    descriptor = None
    for klass in CompanyModel_Product.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_companymodel_product_has_name():
    assert hasattr(CompanyModel_Product, "name")
    descriptor = None
    for klass in CompanyModel_Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companymodel_employee_is_not_abstract():
    assert not inspect.isabstract(CompanyModel_Employee)


def test_companymodel_employee_constructor_exists():
    assert callable(CompanyModel_Employee.__init__)


def test_companymodel_employee_constructor_args():
    sig = inspect.signature(CompanyModel_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "isManager" in params, "Missing parameter 'isManager'"
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel_employee_has_isManager():
    assert hasattr(CompanyModel_Employee, "isManager")
    descriptor = None
    for klass in CompanyModel_Employee.__mro__:
        if "isManager" in klass.__dict__:
            descriptor = klass.__dict__["isManager"]
            break
    assert isinstance(descriptor, property)

def test_companymodel_employee_has_name():
    assert hasattr(CompanyModel_Employee, "name")
    descriptor = None
    for klass in CompanyModel_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_companymodel_department_is_not_abstract():
    assert not inspect.isabstract(CompanyModel_Department)


def test_companymodel_department_constructor_exists():
    assert callable(CompanyModel_Department.__init__)


def test_companymodel_department_constructor_args():
    sig = inspect.signature(CompanyModel_Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_companymodel_department_has_number():
    assert hasattr(CompanyModel_Department, "number")
    descriptor = None
    for klass in CompanyModel_Department.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_companymodel_company_is_not_abstract():
    assert not inspect.isabstract(CompanyModel_Company)


def test_companymodel_company_constructor_exists():
    assert callable(CompanyModel_Company.__init__)


def test_companymodel_company_constructor_args():
    sig = inspect.signature(CompanyModel_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_companymodel_company_has_name():
    assert hasattr(CompanyModel_Company, "name")
    descriptor = None
    for klass in CompanyModel_Company.__mro__:
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
CompanyModel_Product_strategy = st.builds(
    CompanyModel_Product,
    productID=
        st.integers(),
    name=
        safe_text
)
CompanyModel_Employee_strategy = st.builds(
    CompanyModel_Employee,
    isManager=
        st.booleans(),
    name=
        safe_text
)
CompanyModel_Department_strategy = st.builds(
    CompanyModel_Department,
    number=
        st.integers()
)
CompanyModel_Company_strategy = st.builds(
    CompanyModel_Company,
    name=
        safe_text
)

@given(instance=CompanyModel_Product_strategy)
@settings(max_examples=50)
def test_companymodel_product_instantiation(instance):
    assert isinstance(instance, CompanyModel_Product)



@given(instance=CompanyModel_Product_strategy)
def test_companymodel_product_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=CompanyModel_Product_strategy)
def test_companymodel_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyModel_Employee_strategy)
@settings(max_examples=50)
def test_companymodel_employee_instantiation(instance):
    assert isinstance(instance, CompanyModel_Employee)



@given(instance=CompanyModel_Employee_strategy)
def test_companymodel_employee_isManager_setter(instance):
    original = instance.isManager
    instance.isManager = original
    assert instance.isManager == original



@given(instance=CompanyModel_Employee_strategy)
def test_companymodel_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompanyModel_Department_strategy)
@settings(max_examples=50)
def test_companymodel_department_instantiation(instance):
    assert isinstance(instance, CompanyModel_Department)



@given(instance=CompanyModel_Department_strategy)
def test_companymodel_department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=CompanyModel_Company_strategy)
@settings(max_examples=50)
def test_companymodel_company_instantiation(instance):
    assert isinstance(instance, CompanyModel_Company)



@given(instance=CompanyModel_Company_strategy)
def test_companymodel_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
