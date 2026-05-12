import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Division,
    Company_Unit,
    Company_Division,
    Company_Address,
    Company_Company,
    Company_ServiceLine,
    Company_CompanyModel,
    Company_Topic,
    Company_Category,
    Company_Project,
    Company_Person,
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



def test_company_unit_is_not_abstract():
    assert not inspect.isabstract(Company_Unit)


def test_company_unit_constructor_exists():
    assert callable(Company_Unit.__init__)


def test_company_unit_constructor_args():
    sig = inspect.signature(Company_Unit.__init__)
    params = list(sig.parameters.keys())



def test_company_division_is_not_abstract():
    assert not inspect.isabstract(Company_Division)


def test_company_division_constructor_exists():
    assert callable(Company_Division.__init__)


def test_company_division_constructor_args():
    sig = inspect.signature(Company_Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_division_has_name():
    assert hasattr(Company_Division, "name")
    descriptor = None
    for klass in Company_Division.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_address_is_not_abstract():
    assert not inspect.isabstract(Company_Address)


def test_company_address_constructor_exists():
    assert callable(Company_Address.__init__)


def test_company_address_constructor_args():
    sig = inspect.signature(Company_Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"

def test_company_address_has_city():
    assert hasattr(Company_Address, "city")
    descriptor = None
    for klass in Company_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_company_address_has_completeAddress():
    assert hasattr(Company_Address, "completeAddress")
    descriptor = None
    for klass in Company_Address.__mro__:
        if "completeAddress" in klass.__dict__:
            descriptor = klass.__dict__["completeAddress"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(Company_Company)


def test_company_company_constructor_exists():
    assert callable(Company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(Company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_company_has_name():
    assert hasattr(Company_Company, "name")
    descriptor = None
    for klass in Company_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_serviceline_is_not_abstract():
    assert not inspect.isabstract(Company_ServiceLine)


def test_company_serviceline_constructor_exists():
    assert callable(Company_ServiceLine.__init__)


def test_company_serviceline_constructor_args():
    sig = inspect.signature(Company_ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_company_companymodel_is_not_abstract():
    assert not inspect.isabstract(Company_CompanyModel)


def test_company_companymodel_constructor_exists():
    assert callable(Company_CompanyModel.__init__)


def test_company_companymodel_constructor_args():
    sig = inspect.signature(Company_CompanyModel.__init__)
    params = list(sig.parameters.keys())



def test_company_topic_is_not_abstract():
    assert not inspect.isabstract(Company_Topic)


def test_company_topic_constructor_exists():
    assert callable(Company_Topic.__init__)


def test_company_topic_constructor_args():
    sig = inspect.signature(Company_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_company_topic_has_id():
    assert hasattr(Company_Topic, "id")
    descriptor = None
    for klass in Company_Topic.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_company_category_is_not_abstract():
    assert not inspect.isabstract(Company_Category)


def test_company_category_constructor_exists():
    assert callable(Company_Category.__init__)


def test_company_category_constructor_args():
    sig = inspect.signature(Company_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_category_has_name():
    assert hasattr(Company_Category, "name")
    descriptor = None
    for klass in Company_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_project_is_not_abstract():
    assert not inspect.isabstract(Company_Project)


def test_company_project_constructor_exists():
    assert callable(Company_Project.__init__)


def test_company_project_constructor_args():
    sig = inspect.signature(Company_Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_project_has_budget():
    assert hasattr(Company_Project, "budget")
    descriptor = None
    for klass in Company_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company_project_has_name():
    assert hasattr(Company_Project, "name")
    descriptor = None
    for klass in Company_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company_person_is_not_abstract():
    assert not inspect.isabstract(Company_Person)


def test_company_person_constructor_exists():
    assert callable(Company_Person.__init__)


def test_company_person_constructor_args():
    sig = inspect.signature(Company_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "position" in params, "Missing parameter 'position'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_company_person_has_firstname():
    assert hasattr(Company_Person, "firstname")
    descriptor = None
    for klass in Company_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_position():
    assert hasattr(Company_Person, "position")
    descriptor = None
    for klass in Company_Person.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_company_person_has_lastname():
    assert hasattr(Company_Person, "lastname")
    descriptor = None
    for klass in Company_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in type]
    expected_literals = [
        "client",
        "employee",
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
Company_Unit_strategy = st.builds(
    Company_Unit,
)
Company_Division_strategy = st.builds(
    Company_Division,
    name=
        safe_text
)
Company_Address_strategy = st.builds(
    Company_Address,
    city=
        safe_text,
    completeAddress=
        safe_text
)
Company_Company_strategy = st.builds(
    Company_Company,
    name=
        safe_text
)
Company_ServiceLine_strategy = st.builds(
    Company_ServiceLine,
)
Company_CompanyModel_strategy = st.builds(
    Company_CompanyModel,
)
Company_Topic_strategy = st.builds(
    Company_Topic,
    id=
        safe_text
)
Company_Category_strategy = st.builds(
    Company_Category,
    name=
        safe_text
)
Company_Project_strategy = st.builds(
    Company_Project,
    budget=
        st.integers(),
    name=
        safe_text
)
Company_Person_strategy = st.builds(
    Company_Person,
    firstname=
        safe_text,
    position=
        safe_text,
    lastname=
        safe_text
)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=Company_Unit_strategy)
@settings(max_examples=50)
def test_company_unit_instantiation(instance):
    assert isinstance(instance, Company_Unit)

@given(instance=Company_Division_strategy)
@settings(max_examples=50)
def test_company_division_instantiation(instance):
    assert isinstance(instance, Company_Division)



@given(instance=Company_Division_strategy)
def test_company_division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company_Address_strategy)
@settings(max_examples=50)
def test_company_address_instantiation(instance):
    assert isinstance(instance, Company_Address)



@given(instance=Company_Address_strategy)
def test_company_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Company_Address_strategy)
def test_company_address_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original

@given(instance=Company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, Company_Company)



@given(instance=Company_Company_strategy)
def test_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company_ServiceLine_strategy)
@settings(max_examples=50)
def test_company_serviceline_instantiation(instance):
    assert isinstance(instance, Company_ServiceLine)

@given(instance=Company_CompanyModel_strategy)
@settings(max_examples=50)
def test_company_companymodel_instantiation(instance):
    assert isinstance(instance, Company_CompanyModel)

@given(instance=Company_Topic_strategy)
@settings(max_examples=50)
def test_company_topic_instantiation(instance):
    assert isinstance(instance, Company_Topic)



@given(instance=Company_Topic_strategy)
def test_company_topic_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Company_Category_strategy)
@settings(max_examples=50)
def test_company_category_instantiation(instance):
    assert isinstance(instance, Company_Category)



@given(instance=Company_Category_strategy)
def test_company_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company_Project_strategy)
@settings(max_examples=50)
def test_company_project_instantiation(instance):
    assert isinstance(instance, Company_Project)



@given(instance=Company_Project_strategy)
def test_company_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=Company_Project_strategy)
def test_company_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Company_Person_strategy)
@settings(max_examples=50)
def test_company_person_instantiation(instance):
    assert isinstance(instance, Company_Person)



@given(instance=Company_Person_strategy)
def test_company_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Company_Person_strategy)
def test_company_person_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Company_Person_strategy)
def test_company_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original
