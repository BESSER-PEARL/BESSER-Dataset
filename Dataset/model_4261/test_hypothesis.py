import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    organizationchart::Location,
    organizationchart::OrganizationalStructure,
    organizationchart::Employee,
    organizationchart::Organization,
    organizationchart::Function,
    StructureType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_organizationchart::location_is_not_abstract():
    assert not inspect.isabstract(organizationchart::Location)


def test_organizationchart::location_constructor_exists():
    assert callable(organizationchart::Location.__init__)


def test_organizationchart::location_constructor_args():
    sig = inspect.signature(organizationchart::Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_organizationchart::location_has_name():
    assert hasattr(organizationchart::Location, "name")
    descriptor = None
    for klass in organizationchart::Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_organizationchart::organizationalstructure_is_not_abstract():
    assert not inspect.isabstract(organizationchart::OrganizationalStructure)


def test_organizationchart::organizationalstructure_constructor_exists():
    assert callable(organizationchart::OrganizationalStructure.__init__)


def test_organizationchart::organizationalstructure_constructor_args():
    sig = inspect.signature(organizationchart::OrganizationalStructure.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_organizationchart::organizationalstructure_has_type():
    assert hasattr(organizationchart::OrganizationalStructure, "type")
    descriptor = None
    for klass in organizationchart::OrganizationalStructure.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_organizationchart::organizationalstructure_has_name():
    assert hasattr(organizationchart::OrganizationalStructure, "name")
    descriptor = None
    for klass in organizationchart::OrganizationalStructure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_organizationchart::employee_is_not_abstract():
    assert not inspect.isabstract(organizationchart::Employee)


def test_organizationchart::employee_constructor_exists():
    assert callable(organizationchart::Employee.__init__)


def test_organizationchart::employee_constructor_args():
    sig = inspect.signature(organizationchart::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "trigraph" in params, "Missing parameter 'trigraph'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "title" in params, "Missing parameter 'title'"

def test_organizationchart::employee_has_trigraph():
    assert hasattr(organizationchart::Employee, "trigraph")
    descriptor = None
    for klass in organizationchart::Employee.__mro__:
        if "trigraph" in klass.__dict__:
            descriptor = klass.__dict__["trigraph"]
            break
    assert isinstance(descriptor, property)

def test_organizationchart::employee_has_firstname():
    assert hasattr(organizationchart::Employee, "firstname")
    descriptor = None
    for klass in organizationchart::Employee.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_organizationchart::employee_has_lastname():
    assert hasattr(organizationchart::Employee, "lastname")
    descriptor = None
    for klass in organizationchart::Employee.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_organizationchart::employee_has_title():
    assert hasattr(organizationchart::Employee, "title")
    descriptor = None
    for klass in organizationchart::Employee.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_organizationchart::organization_is_not_abstract():
    assert not inspect.isabstract(organizationchart::Organization)


def test_organizationchart::organization_constructor_exists():
    assert callable(organizationchart::Organization.__init__)


def test_organizationchart::organization_constructor_args():
    sig = inspect.signature(organizationchart::Organization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_organizationchart::organization_has_name():
    assert hasattr(organizationchart::Organization, "name")
    descriptor = None
    for klass in organizationchart::Organization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_organizationchart::function_is_not_abstract():
    assert not inspect.isabstract(organizationchart::Function)


def test_organizationchart::function_constructor_exists():
    assert callable(organizationchart::Function.__init__)


def test_organizationchart::function_constructor_args():
    sig = inspect.signature(organizationchart::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_organizationchart::function_has_name():
    assert hasattr(organizationchart::Function, "name")
    descriptor = None
    for klass in organizationchart::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_structuretype_exists():
    # Check that the Enumeration exists
    assert StructureType is not None

def test_structuretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StructureType]
    expected_literals = [
        "department",
        "businessUnit",
        "division",
        "team",
        "service",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StructureType"


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
organizationchart::Location_strategy = st.builds(
    organizationchart::Location,
    name=
        safe_text
)
organizationchart::OrganizationalStructure_strategy = st.builds(
    organizationchart::OrganizationalStructure,
    type=
        safe_text,
    name=
        safe_text
)
organizationchart::Employee_strategy = st.builds(
    organizationchart::Employee,
    trigraph=
        safe_text,
    firstname=
        safe_text,
    lastname=
        safe_text,
    title=
        safe_text
)
organizationchart::Organization_strategy = st.builds(
    organizationchart::Organization,
    name=
        safe_text
)
organizationchart::Function_strategy = st.builds(
    organizationchart::Function,
    name=
        safe_text
)

@given(instance=organizationchart::Location_strategy)
@settings(max_examples=50)
def test_organizationchart::location_instantiation(instance):
    assert isinstance(instance, organizationchart::Location)

@given(instance=organizationchart::Location_strategy)
def test_organizationchart::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organizationchart::Location_strategy)
def test_organizationchart::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=organizationchart::OrganizationalStructure_strategy)
@settings(max_examples=50)
def test_organizationchart::organizationalstructure_instantiation(instance):
    assert isinstance(instance, organizationchart::OrganizationalStructure)

@given(instance=organizationchart::OrganizationalStructure_strategy)
def test_organizationchart::organizationalstructure_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=organizationchart::OrganizationalStructure_strategy)
def test_organizationchart::organizationalstructure_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=organizationchart::OrganizationalStructure_strategy)
def test_organizationchart::organizationalstructure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organizationchart::OrganizationalStructure_strategy)
def test_organizationchart::organizationalstructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=organizationchart::Employee_strategy)
@settings(max_examples=50)
def test_organizationchart::employee_instantiation(instance):
    assert isinstance(instance, organizationchart::Employee)

@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_trigraph_type(instance):
    assert isinstance(instance.trigraph, str)


@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_trigraph_setter(instance):
    original = instance.trigraph
    instance.trigraph = original
    assert instance.trigraph == original

@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=organizationchart::Employee_strategy)
def test_organizationchart::employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=organizationchart::Organization_strategy)
@settings(max_examples=50)
def test_organizationchart::organization_instantiation(instance):
    assert isinstance(instance, organizationchart::Organization)

@given(instance=organizationchart::Organization_strategy)
def test_organizationchart::organization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organizationchart::Organization_strategy)
def test_organizationchart::organization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=organizationchart::Function_strategy)
@settings(max_examples=50)
def test_organizationchart::function_instantiation(instance):
    assert isinstance(instance, organizationchart::Function)

@given(instance=organizationchart::Function_strategy)
def test_organizationchart::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=organizationchart::Function_strategy)
def test_organizationchart::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
