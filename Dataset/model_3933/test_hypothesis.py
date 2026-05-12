import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    office_NamedElement,
    OfficeElement,
    office_Office,
    office_Employee,
    NamedElement,
    office_OfficeElement,
    office_OfficeModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_office_namedelement_is_not_abstract():
    assert not inspect.isabstract(office_NamedElement)


def test_office_namedelement_constructor_exists():
    assert callable(office_NamedElement.__init__)


def test_office_namedelement_constructor_args():
    sig = inspect.signature(office_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_office_namedelement_has_name():
    assert hasattr(office_NamedElement, "name")
    descriptor = None
    for klass in office_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_officeelement_is_not_abstract():
    assert not inspect.isabstract(OfficeElement)


def test_officeelement_constructor_exists():
    assert callable(OfficeElement.__init__)


def test_officeelement_constructor_args():
    sig = inspect.signature(OfficeElement.__init__)
    params = list(sig.parameters.keys())



def test_office_office_is_not_abstract():
    assert not inspect.isabstract(office_Office)


def test_office_office_constructor_exists():
    assert callable(office_Office.__init__)


def test_office_office_constructor_args():
    sig = inspect.signature(office_Office.__init__)
    params = list(sig.parameters.keys())



def test_office_employee_is_not_abstract():
    assert not inspect.isabstract(office_Employee)


def test_office_employee_constructor_exists():
    assert callable(office_Employee.__init__)


def test_office_employee_constructor_args():
    sig = inspect.signature(office_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_office_employee_has_title():
    assert hasattr(office_Employee, "title")
    descriptor = None
    for klass in office_Employee.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_office_officeelement_is_not_abstract():
    assert not inspect.isabstract(office_OfficeElement)


def test_office_officeelement_constructor_exists():
    assert callable(office_OfficeElement.__init__)


def test_office_officeelement_constructor_args():
    sig = inspect.signature(office_OfficeElement.__init__)
    params = list(sig.parameters.keys())



def test_office_officemodel_is_not_abstract():
    assert not inspect.isabstract(office_OfficeModel)


def test_office_officemodel_constructor_exists():
    assert callable(office_OfficeModel.__init__)


def test_office_officemodel_constructor_args():
    sig = inspect.signature(office_OfficeModel.__init__)
    params = list(sig.parameters.keys())


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
office_NamedElement_strategy = st.builds(
    office_NamedElement,
    name=
        safe_text
)
OfficeElement_strategy = st.builds(
    OfficeElement,
)
office_Office_strategy = st.builds(
    office_Office,
)
office_Employee_strategy = st.builds(
    office_Employee,
    title=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
office_OfficeElement_strategy = st.builds(
    office_OfficeElement,
)
office_OfficeModel_strategy = st.builds(
    office_OfficeModel,
)

@given(instance=office_NamedElement_strategy)
@settings(max_examples=50)
def test_office_namedelement_instantiation(instance):
    assert isinstance(instance, office_NamedElement)



@given(instance=office_NamedElement_strategy)
def test_office_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OfficeElement_strategy)
@settings(max_examples=50)
def test_officeelement_instantiation(instance):
    assert isinstance(instance, OfficeElement)

@given(instance=office_Office_strategy)
@settings(max_examples=50)
def test_office_office_instantiation(instance):
    assert isinstance(instance, office_Office)

@given(instance=office_Employee_strategy)
@settings(max_examples=50)
def test_office_employee_instantiation(instance):
    assert isinstance(instance, office_Employee)



@given(instance=office_Employee_strategy)
def test_office_employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=office_OfficeElement_strategy)
@settings(max_examples=50)
def test_office_officeelement_instantiation(instance):
    assert isinstance(instance, office_OfficeElement)

@given(instance=office_OfficeModel_strategy)
@settings(max_examples=50)
def test_office_officemodel_instantiation(instance):
    assert isinstance(instance, office_OfficeModel)
