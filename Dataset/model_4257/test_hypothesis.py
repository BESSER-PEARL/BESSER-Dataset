import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Division,
    EvoCompany_ServiceLine,
    Person,
    EvoCompany_Client,
    EvoCompany_Employee,
    EvoCompany_CompanyModel,
    EvoCompany_Division,
    EvoCompany_Organisation,
    EvoCompany_Unit,
    EvoCompany_Project,
    EvoCompany_Person,
    EvoCompany_Category,
    EvoCompany_Topic,
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



def test_evocompany_serviceline_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_ServiceLine)


def test_evocompany_serviceline_constructor_exists():
    assert callable(EvoCompany_ServiceLine.__init__)


def test_evocompany_serviceline_constructor_args():
    sig = inspect.signature(EvoCompany_ServiceLine.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_evocompany_client_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Client)


def test_evocompany_client_constructor_exists():
    assert callable(EvoCompany_Client.__init__)


def test_evocompany_client_constructor_args():
    sig = inspect.signature(EvoCompany_Client.__init__)
    params = list(sig.parameters.keys())



def test_evocompany_employee_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Employee)


def test_evocompany_employee_constructor_exists():
    assert callable(EvoCompany_Employee.__init__)


def test_evocompany_employee_constructor_args():
    sig = inspect.signature(EvoCompany_Employee.__init__)
    params = list(sig.parameters.keys())



def test_evocompany_companymodel_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_CompanyModel)


def test_evocompany_companymodel_constructor_exists():
    assert callable(EvoCompany_CompanyModel.__init__)


def test_evocompany_companymodel_constructor_args():
    sig = inspect.signature(EvoCompany_CompanyModel.__init__)
    params = list(sig.parameters.keys())



def test_evocompany_division_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Division)


def test_evocompany_division_constructor_exists():
    assert callable(EvoCompany_Division.__init__)


def test_evocompany_division_constructor_args():
    sig = inspect.signature(EvoCompany_Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evocompany_division_has_name():
    assert hasattr(EvoCompany_Division, "name")
    descriptor = None
    for klass in EvoCompany_Division.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evocompany_organisation_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Organisation)


def test_evocompany_organisation_constructor_exists():
    assert callable(EvoCompany_Organisation.__init__)


def test_evocompany_organisation_constructor_args():
    sig = inspect.signature(EvoCompany_Organisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "city" in params, "Missing parameter 'city'"
    assert "completeAddress" in params, "Missing parameter 'completeAddress'"

def test_evocompany_organisation_has_name():
    assert hasattr(EvoCompany_Organisation, "name")
    descriptor = None
    for klass in EvoCompany_Organisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_evocompany_organisation_has_city():
    assert hasattr(EvoCompany_Organisation, "city")
    descriptor = None
    for klass in EvoCompany_Organisation.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_evocompany_organisation_has_completeAddress():
    assert hasattr(EvoCompany_Organisation, "completeAddress")
    descriptor = None
    for klass in EvoCompany_Organisation.__mro__:
        if "completeAddress" in klass.__dict__:
            descriptor = klass.__dict__["completeAddress"]
            break
    assert isinstance(descriptor, property)



def test_evocompany_unit_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Unit)


def test_evocompany_unit_constructor_exists():
    assert callable(EvoCompany_Unit.__init__)


def test_evocompany_unit_constructor_args():
    sig = inspect.signature(EvoCompany_Unit.__init__)
    params = list(sig.parameters.keys())



def test_evocompany_project_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Project)


def test_evocompany_project_constructor_exists():
    assert callable(EvoCompany_Project.__init__)


def test_evocompany_project_constructor_args():
    sig = inspect.signature(EvoCompany_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_evocompany_project_has_name():
    assert hasattr(EvoCompany_Project, "name")
    descriptor = None
    for klass in EvoCompany_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_evocompany_project_has_budget():
    assert hasattr(EvoCompany_Project, "budget")
    descriptor = None
    for klass in EvoCompany_Project.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_evocompany_person_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Person)


def test_evocompany_person_constructor_exists():
    assert callable(EvoCompany_Person.__init__)


def test_evocompany_person_constructor_args():
    sig = inspect.signature(EvoCompany_Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_evocompany_person_has_fullName():
    assert hasattr(EvoCompany_Person, "fullName")
    descriptor = None
    for klass in EvoCompany_Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_evocompany_category_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Category)


def test_evocompany_category_constructor_exists():
    assert callable(EvoCompany_Category.__init__)


def test_evocompany_category_constructor_args():
    sig = inspect.signature(EvoCompany_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evocompany_category_has_name():
    assert hasattr(EvoCompany_Category, "name")
    descriptor = None
    for klass in EvoCompany_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evocompany_topic_is_not_abstract():
    assert not inspect.isabstract(EvoCompany_Topic)


def test_evocompany_topic_constructor_exists():
    assert callable(EvoCompany_Topic.__init__)


def test_evocompany_topic_constructor_args():
    sig = inspect.signature(EvoCompany_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_evocompany_topic_has_id():
    assert hasattr(EvoCompany_Topic, "id")
    descriptor = None
    for klass in EvoCompany_Topic.__mro__:
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
EvoCompany_ServiceLine_strategy = st.builds(
    EvoCompany_ServiceLine,
)
Person_strategy = st.builds(
    Person,
)
EvoCompany_Client_strategy = st.builds(
    EvoCompany_Client,
)
EvoCompany_Employee_strategy = st.builds(
    EvoCompany_Employee,
)
EvoCompany_CompanyModel_strategy = st.builds(
    EvoCompany_CompanyModel,
)
EvoCompany_Division_strategy = st.builds(
    EvoCompany_Division,
    name=
        safe_text
)
EvoCompany_Organisation_strategy = st.builds(
    EvoCompany_Organisation,
    name=
        safe_text,
    city=
        safe_text,
    completeAddress=
        safe_text
)
EvoCompany_Unit_strategy = st.builds(
    EvoCompany_Unit,
)
EvoCompany_Project_strategy = st.builds(
    EvoCompany_Project,
    name=
        safe_text,
    budget=
        st.integers()
)
EvoCompany_Person_strategy = st.builds(
    EvoCompany_Person,
    fullName=
        safe_text
)
EvoCompany_Category_strategy = st.builds(
    EvoCompany_Category,
    name=
        safe_text
)
EvoCompany_Topic_strategy = st.builds(
    EvoCompany_Topic,
    id=
        safe_text
)

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=EvoCompany_ServiceLine_strategy)
@settings(max_examples=50)
def test_evocompany_serviceline_instantiation(instance):
    assert isinstance(instance, EvoCompany_ServiceLine)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=EvoCompany_Client_strategy)
@settings(max_examples=50)
def test_evocompany_client_instantiation(instance):
    assert isinstance(instance, EvoCompany_Client)

@given(instance=EvoCompany_Employee_strategy)
@settings(max_examples=50)
def test_evocompany_employee_instantiation(instance):
    assert isinstance(instance, EvoCompany_Employee)

@given(instance=EvoCompany_CompanyModel_strategy)
@settings(max_examples=50)
def test_evocompany_companymodel_instantiation(instance):
    assert isinstance(instance, EvoCompany_CompanyModel)

@given(instance=EvoCompany_Division_strategy)
@settings(max_examples=50)
def test_evocompany_division_instantiation(instance):
    assert isinstance(instance, EvoCompany_Division)



@given(instance=EvoCompany_Division_strategy)
def test_evocompany_division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany_Organisation_strategy)
@settings(max_examples=50)
def test_evocompany_organisation_instantiation(instance):
    assert isinstance(instance, EvoCompany_Organisation)



@given(instance=EvoCompany_Organisation_strategy)
def test_evocompany_organisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=EvoCompany_Organisation_strategy)
def test_evocompany_organisation_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=EvoCompany_Organisation_strategy)
def test_evocompany_organisation_completeAddress_setter(instance):
    original = instance.completeAddress
    instance.completeAddress = original
    assert instance.completeAddress == original

@given(instance=EvoCompany_Unit_strategy)
@settings(max_examples=50)
def test_evocompany_unit_instantiation(instance):
    assert isinstance(instance, EvoCompany_Unit)

@given(instance=EvoCompany_Project_strategy)
@settings(max_examples=50)
def test_evocompany_project_instantiation(instance):
    assert isinstance(instance, EvoCompany_Project)



@given(instance=EvoCompany_Project_strategy)
def test_evocompany_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=EvoCompany_Project_strategy)
def test_evocompany_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=EvoCompany_Person_strategy)
@settings(max_examples=50)
def test_evocompany_person_instantiation(instance):
    assert isinstance(instance, EvoCompany_Person)



@given(instance=EvoCompany_Person_strategy)
def test_evocompany_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=EvoCompany_Category_strategy)
@settings(max_examples=50)
def test_evocompany_category_instantiation(instance):
    assert isinstance(instance, EvoCompany_Category)



@given(instance=EvoCompany_Category_strategy)
def test_evocompany_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EvoCompany_Topic_strategy)
@settings(max_examples=50)
def test_evocompany_topic_instantiation(instance):
    assert isinstance(instance, EvoCompany_Topic)



@given(instance=EvoCompany_Topic_strategy)
def test_evocompany_topic_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
