import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Division,
    EvoCompany::ServiceLine,
    Person,
    EvoCompany::Client,
    EvoCompany::Employee,
    EvoCompany::CompanyModel,
    EvoCompany::Division,
    EvoCompany::Organisation,
    EvoCompany::Unit,
    EvoCompany::Project,
    EvoCompany::Person,
    EvoCompany::Category,
    EvoCompany::Topic,
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



def test_evocompany::serviceline_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::ServiceLine)


def test_evocompany::serviceline_constructor_exists():
    assert callable(EvoCompany::ServiceLine.__init__)


def test_evocompany::serviceline_constructor_args():
    sig = inspect.signature(EvoCompany::ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_evocompany::client_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Client)


def test_evocompany::client_constructor_exists():
    assert callable(EvoCompany::Client.__init__)


def test_evocompany::client_constructor_args():
    sig = inspect.signature(EvoCompany::Client.__init__)
    params = list(sig.parameters.keys())



def test_evocompany::employee_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Employee)


def test_evocompany::employee_constructor_exists():
    assert callable(EvoCompany::Employee.__init__)


def test_evocompany::employee_constructor_args():
    sig = inspect.signature(EvoCompany::Employee.__init__)
    params = list(sig.parameters.keys())



def test_evocompany::companymodel_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::CompanyModel)


def test_evocompany::companymodel_constructor_exists():
    assert callable(EvoCompany::CompanyModel.__init__)


def test_evocompany::companymodel_constructor_args():
    sig = inspect.signature(EvoCompany::CompanyModel.__init__)
    params = list(sig.parameters.keys())



def test_evocompany::division_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Division)


def test_evocompany::division_constructor_exists():
    assert callable(EvoCompany::Division.__init__)


def test_evocompany::division_constructor_args():
    sig = inspect.signature(EvoCompany::Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evocompany::division_has_name():
    assert hasattr(EvoCompany::Division, "name")
    descriptor = None
    for klass in EvoCompany::Division.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evocompany::organisation_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Organisation)


def test_evocompany::organisation_constructor_exists():
    assert callable(EvoCompany::Organisation.__init__)


def test_evocompany::organisation_constructor_args():
    sig = inspect.signature(EvoCompany::Organisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "city" in params, "Missing parameter 'city'"
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"

def test_evocompany::organisation_has_name():
    assert hasattr(EvoCompany::Organisation, "name")
    descriptor = None
    for klass in EvoCompany::Organisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_evocompany::organisation_has_city():
    assert hasattr(EvoCompany::Organisation, "city")
    descriptor = None
    for klass in EvoCompany::Organisation.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_evocompany::organisation_has_completeAddress():
    assert hasattr(EvoCompany::Organisation, "completeAddress")
    descriptor = None
    for klass in EvoCompany::Organisation.__mro__:
        if "completeAddress" in klass.__dict__:
            descriptor = klass.__dict__["completeAddress"]
            break
    assert isinstance(descriptor, property)



def test_evocompany::unit_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Unit)


def test_evocompany::unit_constructor_exists():
    assert callable(EvoCompany::Unit.__init__)


def test_evocompany::unit_constructor_args():
    sig = inspect.signature(EvoCompany::Unit.__init__)
    params = list(sig.parameters.keys())



def test_evocompany::project_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Project)


def test_evocompany::project_constructor_exists():
    assert callable(EvoCompany::Project.__init__)


def test_evocompany::project_constructor_args():
    sig = inspect.signature(EvoCompany::Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_evocompany::project_has_budget():
    assert hasattr(EvoCompany::Project, "budget")
    descriptor = None
    for klass in EvoCompany::Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_evocompany::project_has_name():
    assert hasattr(EvoCompany::Project, "name")
    descriptor = None
    for klass in EvoCompany::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evocompany::person_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Person)


def test_evocompany::person_constructor_exists():
    assert callable(EvoCompany::Person.__init__)


def test_evocompany::person_constructor_args():
    sig = inspect.signature(EvoCompany::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_evocompany::person_has_fullName():
    assert hasattr(EvoCompany::Person, "fullName")
    descriptor = None
    for klass in EvoCompany::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_evocompany::category_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Category)


def test_evocompany::category_constructor_exists():
    assert callable(EvoCompany::Category.__init__)


def test_evocompany::category_constructor_args():
    sig = inspect.signature(EvoCompany::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evocompany::category_has_name():
    assert hasattr(EvoCompany::Category, "name")
    descriptor = None
    for klass in EvoCompany::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evocompany::topic_is_not_abstract():
    assert not inspect.isabstract(EvoCompany::Topic)


def test_evocompany::topic_constructor_exists():
    assert callable(EvoCompany::Topic.__init__)


def test_evocompany::topic_constructor_args():
    sig = inspect.signature(EvoCompany::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_evocompany::topic_has_id():
    assert hasattr(EvoCompany::Topic, "id")
    descriptor = None
    for klass in EvoCompany::Topic.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
EvoCompany::ServiceLine_strategy = st.builds(
    EvoCompany::ServiceLine,
)
Person_strategy = st.builds(
    Person,
)
EvoCompany::Client_strategy = st.builds(
    EvoCompany::Client,
)
EvoCompany::Employee_strategy = st.builds(
    EvoCompany::Employee,
)
EvoCompany::CompanyModel_strategy = st.builds(
    EvoCompany::CompanyModel,
)
EvoCompany::Division_strategy = st.builds(
    EvoCompany::Division,
    name=
        safe_text
)
EvoCompany::Organisation_strategy = st.builds(
    EvoCompany::Organisation,
    name=
        safe_text,
    city=
        safe_text,
    completeAddress=
        safe_text
)
EvoCompany::Unit_strategy = st.builds(
    EvoCompany::Unit,
)
EvoCompany::Project_strategy = st.builds(
    EvoCompany::Project,
    budget=
        st.integers(),
    name=
        safe_text
)
EvoCompany::Person_strategy = st.builds(
    EvoCompany::Person,
    fullName=
        safe_text
)
EvoCompany::Category_strategy = st.builds(
    EvoCompany::Category,
    name=
        safe_text
)
EvoCompany::Topic_strategy = st.builds(
    EvoCompany::Topic,
    id=
        safe_text
)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=EvoCompany::ServiceLine_strategy)
@settings(max_examples=50)
def test_evocompany::serviceline_instantiation(instance):
    assert isinstance(instance, EvoCompany::ServiceLine)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=EvoCompany::Client_strategy)
@settings(max_examples=50)
def test_evocompany::client_instantiation(instance):
    assert isinstance(instance, EvoCompany::Client)

@given(instance=EvoCompany::Employee_strategy)
@settings(max_examples=50)
def test_evocompany::employee_instantiation(instance):
    assert isinstance(instance, EvoCompany::Employee)

@given(instance=EvoCompany::CompanyModel_strategy)
@settings(max_examples=50)
def test_evocompany::companymodel_instantiation(instance):
    assert isinstance(instance, EvoCompany::CompanyModel)

@given(instance=EvoCompany::Division_strategy)
@settings(max_examples=50)
def test_evocompany::division_instantiation(instance):
    assert isinstance(instance, EvoCompany::Division)

@given(instance=EvoCompany::Division_strategy)
def test_evocompany::division_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EvoCompany::Division_strategy)
def test_evocompany::division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany::Organisation_strategy)
@settings(max_examples=50)
def test_evocompany::organisation_instantiation(instance):
    assert isinstance(instance, EvoCompany::Organisation)

@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_completeAddress_type(instance):
    assert isinstance(instance.completeAddress, str)


@given(instance=EvoCompany::Organisation_strategy)
def test_evocompany::organisation_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original

@given(instance=EvoCompany::Unit_strategy)
@settings(max_examples=50)
def test_evocompany::unit_instantiation(instance):
    assert isinstance(instance, EvoCompany::Unit)

@given(instance=EvoCompany::Project_strategy)
@settings(max_examples=50)
def test_evocompany::project_instantiation(instance):
    assert isinstance(instance, EvoCompany::Project)

@given(instance=EvoCompany::Project_strategy)
def test_evocompany::project_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=EvoCompany::Project_strategy)
def test_evocompany::project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=EvoCompany::Project_strategy)
def test_evocompany::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EvoCompany::Project_strategy)
def test_evocompany::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany::Person_strategy)
@settings(max_examples=50)
def test_evocompany::person_instantiation(instance):
    assert isinstance(instance, EvoCompany::Person)

@given(instance=EvoCompany::Person_strategy)
def test_evocompany::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=EvoCompany::Person_strategy)
def test_evocompany::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=EvoCompany::Category_strategy)
@settings(max_examples=50)
def test_evocompany::category_instantiation(instance):
    assert isinstance(instance, EvoCompany::Category)

@given(instance=EvoCompany::Category_strategy)
def test_evocompany::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EvoCompany::Category_strategy)
def test_evocompany::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany::Topic_strategy)
@settings(max_examples=50)
def test_evocompany::topic_instantiation(instance):
    assert isinstance(instance, EvoCompany::Topic)

@given(instance=EvoCompany::Topic_strategy)
def test_evocompany::topic_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=EvoCompany::Topic_strategy)
def test_evocompany::topic_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
