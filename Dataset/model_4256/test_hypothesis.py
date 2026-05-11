import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Division,
    Company::Unit,
    Company::CompanyModel,
    Company::Topic,
    Project,
    Company::National,
    Company::European,
    Company::Category,
    Company::Division,
    Company::Address,
    Company::Company,
    Company::ServiceLine,
    Company::Project,
    Company::Person,
    type,
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



def test_company::unit_is_not_abstract():
    assert not inspect.isabstract(Company::Unit)


def test_company::unit_constructor_exists():
    assert callable(Company::Unit.__init__)


def test_company::unit_constructor_args():
    sig = inspect.signature(Company::Unit.__init__)
    params = list(sig.parameters.keys())



def test_company::companymodel_is_not_abstract():
    assert not inspect.isabstract(Company::CompanyModel)


def test_company::companymodel_constructor_exists():
    assert callable(Company::CompanyModel.__init__)


def test_company::companymodel_constructor_args():
    sig = inspect.signature(Company::CompanyModel.__init__)
    params = list(sig.parameters.keys())



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



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_company::national_is_not_abstract():
    assert not inspect.isabstract(Company::National)


def test_company::national_constructor_exists():
    assert callable(Company::National.__init__)


def test_company::national_constructor_args():
    sig = inspect.signature(Company::National.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"

def test_company::national_has_budget():
    assert hasattr(Company::National, "budget")
    descriptor = None
    for klass in Company::National.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_company::european_is_not_abstract():
    assert not inspect.isabstract(Company::European)


def test_company::european_constructor_exists():
    assert callable(Company::European.__init__)


def test_company::european_constructor_args():
    sig = inspect.signature(Company::European.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"

def test_company::european_has_budget():
    assert hasattr(Company::European, "budget")
    descriptor = None
    for klass in Company::European.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



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



def test_company::address_is_not_abstract():
    assert not inspect.isabstract(Company::Address)


def test_company::address_constructor_exists():
    assert callable(Company::Address.__init__)


def test_company::address_constructor_args():
    sig = inspect.signature(Company::Address.__init__)
    params = list(sig.parameters.keys())
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"
    assert "city" in params, "Missing parameter 'city'"

def test_company::address_has_completeAddress():
    assert hasattr(Company::Address, "completeAddress")
    descriptor = None
    for klass in Company::Address.__mro__:
        if "completeAddress" in klass.__dict__:
            descriptor = klass.__dict__["completeAddress"]
            break
    assert isinstance(descriptor, property)

def test_company::address_has_city():
    assert hasattr(Company::Address, "city")
    descriptor = None
    for klass in Company::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(Company::Company)


def test_company::company_constructor_exists():
    assert callable(Company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(Company::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::company_has_name():
    assert hasattr(Company::Company, "name")
    descriptor = None
    for klass in Company::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::serviceline_is_not_abstract():
    assert not inspect.isabstract(Company::ServiceLine)


def test_company::serviceline_constructor_exists():
    assert callable(Company::ServiceLine.__init__)


def test_company::serviceline_constructor_args():
    sig = inspect.signature(Company::ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_company::project_is_not_abstract():
    assert not inspect.isabstract(Company::Project)


def test_company::project_constructor_exists():
    assert callable(Company::Project.__init__)


def test_company::project_constructor_args():
    sig = inspect.signature(Company::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::project_has_name():
    assert hasattr(Company::Project, "name")
    descriptor = None
    for klass in Company::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::person_is_not_abstract():
    assert not inspect.isabstract(Company::Person)


def test_company::person_constructor_exists():
    assert callable(Company::Person.__init__)


def test_company::person_constructor_args():
    sig = inspect.signature(Company::Person.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_company::person_has_position():
    assert hasattr(Company::Person, "position")
    descriptor = None
    for klass in Company::Person.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_company::person_has_fullName():
    assert hasattr(Company::Person, "fullName")
    descriptor = None
    for klass in Company::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in type]
    expected_literals = [
        "employee",
        "client",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in type"


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
Company::Unit_strategy = st.builds(
    Company::Unit,
)
Company::CompanyModel_strategy = st.builds(
    Company::CompanyModel,
)
Company::Topic_strategy = st.builds(
    Company::Topic,
    id=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
Company::National_strategy = st.builds(
    Company::National,
    budget=
        st.integers()
)
Company::European_strategy = st.builds(
    Company::European,
    budget=
        st.integers()
)
Company::Category_strategy = st.builds(
    Company::Category,
    name=
        safe_text
)
Company::Division_strategy = st.builds(
    Company::Division,
    name=
        safe_text
)
Company::Address_strategy = st.builds(
    Company::Address,
    completeAddress=
        safe_text,
    city=
        safe_text
)
Company::Company_strategy = st.builds(
    Company::Company,
    name=
        safe_text
)
Company::ServiceLine_strategy = st.builds(
    Company::ServiceLine,
)
Company::Project_strategy = st.builds(
    Company::Project,
    name=
        safe_text
)
Company::Person_strategy = st.builds(
    Company::Person,
    position=
        safe_text,
    fullName=
        safe_text
)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=Company::Unit_strategy)
@settings(max_examples=50)
def test_company::unit_instantiation(instance):
    assert isinstance(instance, Company::Unit)

@given(instance=Company::CompanyModel_strategy)
@settings(max_examples=50)
def test_company::companymodel_instantiation(instance):
    assert isinstance(instance, Company::CompanyModel)

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

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=Company::National_strategy)
@settings(max_examples=50)
def test_company::national_instantiation(instance):
    assert isinstance(instance, Company::National)

@given(instance=Company::National_strategy)
def test_company::national_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Company::National_strategy)
def test_company::national_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=Company::European_strategy)
@settings(max_examples=50)
def test_company::european_instantiation(instance):
    assert isinstance(instance, Company::European)

@given(instance=Company::European_strategy)
def test_company::european_budget_type(instance):
    assert isinstance(instance.budget, int)


@given(instance=Company::European_strategy)
def test_company::european_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

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

@given(instance=Company::Address_strategy)
@settings(max_examples=50)
def test_company::address_instantiation(instance):
    assert isinstance(instance, Company::Address)

@given(instance=Company::Address_strategy)
def test_company::address_completeAddress_type(instance):
    assert isinstance(instance.completeAddress, str)


@given(instance=Company::Address_strategy)
def test_company::address_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original

@given(instance=Company::Address_strategy)
def test_company::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=Company::Address_strategy)
def test_company::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=Company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, Company::Company)

@given(instance=Company::Company_strategy)
def test_company::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Company::Company_strategy)
def test_company::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company::ServiceLine_strategy)
@settings(max_examples=50)
def test_company::serviceline_instantiation(instance):
    assert isinstance(instance, Company::ServiceLine)

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

@given(instance=Company::Person_strategy)
@settings(max_examples=50)
def test_company::person_instantiation(instance):
    assert isinstance(instance, Company::Person)

@given(instance=Company::Person_strategy)
def test_company::person_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=Company::Person_strategy)
def test_company::person_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Company::Person_strategy)
def test_company::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=Company::Person_strategy)
def test_company::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original
