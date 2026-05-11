import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::TestClass,
    company::Company,
    company::Employee,
    company::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::testclass_is_not_abstract():
    assert not inspect.isabstract(company::TestClass)


def test_company::testclass_constructor_exists():
    assert callable(company::TestClass.__init__)


def test_company::testclass_constructor_args():
    sig = inspect.signature(company::TestClass.__init__)
    params = list(sig.parameters.keys())
    assert "stringAttribute2" in params, "Missing parameter 'stringAttribute2'"
    assert "stringAttribute1" in params, "Missing parameter 'stringAttribute1'"
    assert "intAttribute2" in params, "Missing parameter 'intAttribute2'"
    assert "intAttribute1" in params, "Missing parameter 'intAttribute1'"

def test_company::testclass_has_stringAttribute2():
    assert hasattr(company::TestClass, "stringAttribute2")
    descriptor = None
    for klass in company::TestClass.__mro__:
        if "stringAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["stringAttribute2"]
            break
    assert isinstance(descriptor, property)

def test_company::testclass_has_stringAttribute1():
    assert hasattr(company::TestClass, "stringAttribute1")
    descriptor = None
    for klass in company::TestClass.__mro__:
        if "stringAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["stringAttribute1"]
            break
    assert isinstance(descriptor, property)

def test_company::testclass_has_intAttribute2():
    assert hasattr(company::TestClass, "intAttribute2")
    descriptor = None
    for klass in company::TestClass.__mro__:
        if "intAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["intAttribute2"]
            break
    assert isinstance(descriptor, property)

def test_company::testclass_has_intAttribute1():
    assert hasattr(company::TestClass, "intAttribute1")
    descriptor = None
    for klass in company::TestClass.__mro__:
        if "intAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["intAttribute1"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::company_has_name():
    assert hasattr(company::Company, "name")
    descriptor = None
    for klass in company::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(company::Employee)


def test_company::employee_constructor_exists():
    assert callable(company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_company::employee_has_age():
    assert hasattr(company::Employee, "age")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_lastName():
    assert hasattr(company::Employee, "lastName")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_firstName():
    assert hasattr(company::Employee, "firstName")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(company::Department)


def test_company::department_constructor_exists():
    assert callable(company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_company::department_has_number():
    assert hasattr(company::Department, "number")
    descriptor = None
    for klass in company::Department.__mro__:
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
company::TestClass_strategy = st.builds(
    company::TestClass,
    stringAttribute2=
        safe_text,
    stringAttribute1=
        safe_text,
    intAttribute2=
        st.integers(),
    intAttribute1=
        st.integers()
)
company::Company_strategy = st.builds(
    company::Company,
    name=
        safe_text
)
company::Employee_strategy = st.builds(
    company::Employee,
    age=
        st.integers(),
    lastName=
        safe_text,
    firstName=
        safe_text
)
company::Department_strategy = st.builds(
    company::Department,
    number=
        st.integers()
)

@given(instance=company::TestClass_strategy)
@settings(max_examples=50)
def test_company::testclass_instantiation(instance):
    assert isinstance(instance, company::TestClass)

@given(instance=company::TestClass_strategy)
def test_company::testclass_stringAttribute2_type(instance):
    assert isinstance(instance.stringAttribute2, str)


@given(instance=company::TestClass_strategy)
def test_company::testclass_stringAttribute2_setter(instance):
    original = instance.stringAttribute2
    instance.stringAttribute2 = original
    assert instance.stringAttribute2 == original

@given(instance=company::TestClass_strategy)
def test_company::testclass_stringAttribute1_type(instance):
    assert isinstance(instance.stringAttribute1, str)


@given(instance=company::TestClass_strategy)
def test_company::testclass_stringAttribute1_setter(instance):
    original = instance.stringAttribute1
    instance.stringAttribute1 = original
    assert instance.stringAttribute1 == original

@given(instance=company::TestClass_strategy)
def test_company::testclass_intAttribute2_type(instance):
    assert isinstance(instance.intAttribute2, int)


@given(instance=company::TestClass_strategy)
def test_company::testclass_intAttribute2_setter(instance):
    original = instance.intAttribute2
    instance.intAttribute2 = original
    assert instance.intAttribute2 == original

@given(instance=company::TestClass_strategy)
def test_company::testclass_intAttribute1_type(instance):
    assert isinstance(instance.intAttribute1, int)


@given(instance=company::TestClass_strategy)
def test_company::testclass_intAttribute1_setter(instance):
    original = instance.intAttribute1
    instance.intAttribute1 = original
    assert instance.intAttribute1 == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)

@given(instance=company::Company_strategy)
def test_company::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Company_strategy)
def test_company::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, company::Employee)

@given(instance=company::Employee_strategy)
def test_company::employee_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=company::Employee_strategy)
def test_company::employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company::Employee_strategy)
def test_company::employee_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=company::Employee_strategy)
def test_company::employee_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=company::Employee_strategy)
def test_company::employee_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=company::Employee_strategy)
def test_company::employee_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, company::Department)

@given(instance=company::Department_strategy)
def test_company::department_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=company::Department_strategy)
def test_company::department_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original
