import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    company_TestClass,
    company_Company,
    company_Employee,
    company_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_testclass_is_not_abstract():
    assert not inspect.isabstract(company_TestClass)


def test_company_testclass_constructor_exists():
    assert callable(company_TestClass.__init__)


def test_company_testclass_constructor_args():
    sig = inspect.signature(company_TestClass.__init__)
    params = list(sig.parameters.keys())
    assert "stringAttribute2" in params, "Missing parameter 'stringAttribute2'"
    assert "intAttribute1" in params, "Missing parameter 'intAttribute1'"
    assert "stringAttribute1" in params, "Missing parameter 'stringAttribute1'"
    assert "intAttribute2" in params, "Missing parameter 'intAttribute2'"

def test_company_testclass_has_stringAttribute2():
    assert hasattr(company_TestClass, "stringAttribute2")
    descriptor = None
    for klass in company_TestClass.__mro__:
        if "stringAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["stringAttribute2"]
            break
    assert isinstance(descriptor, property)

def test_company_testclass_has_intAttribute1():
    assert hasattr(company_TestClass, "intAttribute1")
    descriptor = None
    for klass in company_TestClass.__mro__:
        if "intAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["intAttribute1"]
            break
    assert isinstance(descriptor, property)

def test_company_testclass_has_stringAttribute1():
    assert hasattr(company_TestClass, "stringAttribute1")
    descriptor = None
    for klass in company_TestClass.__mro__:
        if "stringAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["stringAttribute1"]
            break
    assert isinstance(descriptor, property)

def test_company_testclass_has_intAttribute2():
    assert hasattr(company_TestClass, "intAttribute2")
    descriptor = None
    for klass in company_TestClass.__mro__:
        if "intAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["intAttribute2"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_company_has_name():
    assert hasattr(company_Company, "name")
    descriptor = None
    for klass in company_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "age" in params, "Missing parameter 'age'"

def test_company_employee_has_lastName():
    assert hasattr(company_Employee, "lastName")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_firstName():
    assert hasattr(company_Employee, "firstName")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_age():
    assert hasattr(company_Employee, "age")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_company_department_has_number():
    assert hasattr(company_Department, "number")
    descriptor = None
    for klass in company_Department.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
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
company_TestClass_strategy = st.builds(
    company_TestClass,
    stringAttribute2=
        safe_text,
    intAttribute1=
        st.integers(),
    stringAttribute1=
        safe_text,
    intAttribute2=
        st.integers()
)
company_Company_strategy = st.builds(
    company_Company,
    name=
        safe_text
)
company_Employee_strategy = st.builds(
    company_Employee,
    lastName=
        safe_text,
    firstName=
        safe_text,
    age=
        st.integers()
)
company_Department_strategy = st.builds(
    company_Department,
    number=
        st.integers()
)

@given(instance=company_TestClass_strategy)
@settings(max_examples=50)
def test_company_testclass_instantiation(instance):
    assert isinstance(instance, company_TestClass)



@given(instance=company_TestClass_strategy)
def test_company_testclass_stringAttribute2_setter(instance):
    original = instance.stringAttribute2
    instance.stringAttribute2 = original
    assert instance.stringAttribute2 == original



@given(instance=company_TestClass_strategy)
def test_company_testclass_intAttribute1_setter(instance):
    original = instance.intAttribute1
    instance.intAttribute1 = original
    assert instance.intAttribute1 == original



@given(instance=company_TestClass_strategy)
def test_company_testclass_stringAttribute1_setter(instance):
    original = instance.stringAttribute1
    instance.stringAttribute1 = original
    assert instance.stringAttribute1 == original



@given(instance=company_TestClass_strategy)
def test_company_testclass_intAttribute2_setter(instance):
    original = instance.intAttribute2
    instance.intAttribute2 = original
    assert instance.intAttribute2 == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)



@given(instance=company_Company_strategy)
def test_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, company_Employee)



@given(instance=company_Employee_strategy)
def test_company_employee_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=company_Employee_strategy)
def test_company_employee_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=company_Employee_strategy)
def test_company_employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, company_Department)



@given(instance=company_Department_strategy)
def test_company_department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original
