import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Division,
    Company::ServiceLine,
    Person,
    Company::Client,
    Company::Employee,
    Company::Organisation,
    Company::Unit,
    Company::Project,
    Company::Person,
    Company::CompanyModel,
    Company::Category,
    Company::Topic,
    Company::Division,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_division_is_not_abstract():
    assert not inspect.isabstract(Division)


def test_division_constructor_exists():
    assert callable(Division.__init__)


def test_division_constructor_args():
    sig = inspect.signature(Division.__init__)
    params = list(sig.parameters.keys())



def test_company::serviceline_is_not_abstract():
    assert not inspect.isabstract(Company::ServiceLine)


def test_company::serviceline_constructor_exists():
    assert callable(Company::ServiceLine.__init__)


def test_company::serviceline_constructor_args():
    sig = inspect.signature(Company::ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_company::client_is_not_abstract():
    assert not inspect.isabstract(Company::Client)


def test_company::client_constructor_exists():
    assert callable(Company::Client.__init__)


def test_company::client_constructor_args():
    sig = inspect.signature(Company::Client.__init__)
    params = list(sig.parameters.keys())



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(Company::Employee)


def test_company::employee_constructor_exists():
    assert callable(Company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(Company::Employee.__init__)
    params = list(sig.parameters.keys())



def test_company::organisation_is_not_abstract():
    assert not inspect.isabstract(Company::Organisation)


def test_company::organisation_constructor_exists():
    assert callable(Company::Organisation.__init__)


def test_company::organisation_constructor_args():
    sig = inspect.signature(Company::Organisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"
    assert "city" in params, "Missing parameter 'city'"

def test_company::organisation_has_name():
    assert hasattr(Company::Organisation, "name")
    descriptor = None
    for klass in Company::Organisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::organisation_has_completeAddress():
    assert hasattr(Company::Organisation, "completeAddress")
    descriptor = None
    for klass in Company::Organisation.__mro__:
        if "completeAddress" in klass.__dict__:
            descriptor = klass.__dict__["completeAddress"]
            break
    assert isinstance(descriptor, property)

def test_company::organisation_has_city():
    assert hasattr(Company::Organisation, "city")
    descriptor = None
    for klass in Company::Organisation.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_company::unit_is_not_abstract():
    assert not inspect.isabstract(Company::Unit)


def test_company::unit_constructor_exists():
    assert callable(Company::Unit.__init__)


def test_company::unit_constructor_args():
    sig = inspect.signature(Company::Unit.__init__)
    params = list(sig.parameters.keys())



def test_company::project_is_not_abstract():
    assert not inspect.isabstract(Company::Project)


def test_company::project_constructor_exists():
    assert callable(Company::Project.__init__)


def test_company::project_constructor_args():
    sig = inspect.signature(Company::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_company::project_has_name():
    assert hasattr(Company::Project, "name")
    descriptor = None
    for klass in Company::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::project_has_budget():
    assert hasattr(Company::Project, "budget")
    descriptor = None
    for klass in Company::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_company::person_is_not_abstract():
    assert not inspect.isabstract(Company::Person)


def test_company::person_constructor_exists():
    assert callable(Company::Person.__init__)


def test_company::person_constructor_args():
    sig = inspect.signature(Company::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_company::person_has_fullName():
    assert hasattr(Company::Person, "fullName")
    descriptor = None
    for klass in Company::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_company::companymodel_is_not_abstract():
    assert not inspect.isabstract(Company::CompanyModel)


def test_company::companymodel_constructor_exists():
    assert callable(Company::CompanyModel.__init__)


def test_company::companymodel_constructor_args():
    sig = inspect.signature(Company::CompanyModel.__init__)
    params = list(sig.parameters.keys())



def test_company::category_is_not_abstract():
    assert not inspect.isabstract(Company::Category)


def test_company::category_constructor_exists():
    assert callable(Company::Category.__init__)


def test_company::category_constructor_args():
    sig = inspect.signature(Company::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::category_has_name():
    assert hasattr(Company::Category, "name")
    descriptor = None
    for klass in Company::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::topic_is_not_abstract():
    assert not inspect.isabstract(Company::Topic)


def test_company::topic_constructor_exists():
    assert callable(Company::Topic.__init__)


def test_company::topic_constructor_args():
    sig = inspect.signature(Company::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_company::topic_has_id():
    assert hasattr(Company::Topic, "id")
    descriptor = None
    for klass in Company::Topic.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_company::division_is_not_abstract():
    assert not inspect.isabstract(Company::Division)


def test_company::division_constructor_exists():
    assert callable(Company::Division.__init__)


def test_company::division_constructor_args():
    sig = inspect.signature(Company::Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::division_has_name():
    assert hasattr(Company::Division, "name")
    descriptor = None
    for klass in Company::Division.__mro__:
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
Division_strategy = st.builds(
    Division,
)
Company::ServiceLine_strategy = st.builds(
    Company::ServiceLine,
)
Person_strategy = st.builds(
    Person,
)
Company::Client_strategy = st.builds(
    Company::Client,
)
Company::Employee_strategy = st.builds(
    Company::Employee,
)
Company::Organisation_strategy = st.builds(
    Company::Organisation,
    name=
        safe_text,
    completeAddress=
        safe_text,
    city=
        safe_text
)
Company::Unit_strategy = st.builds(
    Company::Unit,
)
Company::Project_strategy = st.builds(
    Company::Project,
    name=
        safe_text,
    budget=
        st.integers()
)
Company::Person_strategy = st.builds(
    Company::Person,
    fullName=
        safe_text
)
Company::CompanyModel_strategy = st.builds(
    Company::CompanyModel,
)
Company::Category_strategy = st.builds(
    Company::Category,
    name=
        safe_text
)
Company::Topic_strategy = st.builds(
    Company::Topic,
    id=
        safe_text
)
Company::Division_strategy = st.builds(
    Company::Division,
    name=
        safe_text
)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=Company::ServiceLine_strategy)
@settings(max_examples=50)
def test_company::serviceline_instantiation(instance):
    assert isinstance(instance, Company::ServiceLine)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Company::Client_strategy)
@settings(max_examples=50)
def test_company::client_instantiation(instance):
    assert isinstance(instance, Company::Client)

@given(instance=Company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, Company::Employee)

@given(instance=Company::Organisation_strategy)
@settings(max_examples=50)
def test_company::organisation_instantiation(instance):
    assert isinstance(instance, Company::Organisation)

@given(instance=Company::Organisation_strategy)
def test_company::organisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Organisation_strategy)
def test_company::organisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Organisation_strategy)
def test_company::organisation_completeAddress_type(instance):
    assert isinstance(instance.completeAddress, str)


@given(instance=Company::Organisation_strategy)
def test_company::organisation_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original

@given(instance=Company::Organisation_strategy)
def test_company::organisation_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=Company::Organisation_strategy)
def test_company::organisation_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=Company::Unit_strategy)
@settings(max_examples=50)
def test_company::unit_instantiation(instance):
    assert isinstance(instance, Company::Unit)

@given(instance=Company::Project_strategy)
@settings(max_examples=50)
def test_company::project_instantiation(instance):
    assert isinstance(instance, Company::Project)

@given(instance=Company::Project_strategy)
def test_company::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Project_strategy)
def test_company::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Project_strategy)
def test_company::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Company::Project_strategy)
def test_company::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Company::Person_strategy)
@settings(max_examples=50)
def test_company::person_instantiation(instance):
    assert isinstance(instance, Company::Person)

@given(instance=Company::Person_strategy)
def test_company::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=Company::Person_strategy)
def test_company::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=Company::CompanyModel_strategy)
@settings(max_examples=50)
def test_company::companymodel_instantiation(instance):
    assert isinstance(instance, Company::CompanyModel)

@given(instance=Company::Category_strategy)
@settings(max_examples=50)
def test_company::category_instantiation(instance):
    assert isinstance(instance, Company::Category)

@given(instance=Company::Category_strategy)
def test_company::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Category_strategy)
def test_company::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::Topic_strategy)
@settings(max_examples=50)
def test_company::topic_instantiation(instance):
    assert isinstance(instance, Company::Topic)

@given(instance=Company::Topic_strategy)
def test_company::topic_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Company::Topic_strategy)
def test_company::topic_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Company::Division_strategy)
@settings(max_examples=50)
def test_company::division_instantiation(instance):
    assert isinstance(instance, Company::Division)

@given(instance=Company::Division_strategy)
def test_company::division_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Division_strategy)
def test_company::division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
