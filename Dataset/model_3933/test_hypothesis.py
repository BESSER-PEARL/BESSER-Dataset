import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    office::NamedElement,
    OfficeElement,
    office::Office,
    office::Employee,
    NamedElement,
    office::OfficeElement,
    office::OfficeModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_office::namedelement_is_not_abstract():
    assert not inspect.isabstract(office::NamedElement)


def test_office::namedelement_constructor_exists():
    assert callable(office::NamedElement.__init__)


def test_office::namedelement_constructor_args():
    sig = inspect.signature(office::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_office::namedelement_has_name():
    assert hasattr(office::NamedElement, "name")
    descriptor = None
    for klass in office::NamedElement.__mro__:
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



def test_office::office_is_not_abstract():
    assert not inspect.isabstract(office::Office)


def test_office::office_constructor_exists():
    assert callable(office::Office.__init__)


def test_office::office_constructor_args():
    sig = inspect.signature(office::Office.__init__)
    params = list(sig.parameters.keys())



def test_office::employee_is_not_abstract():
    assert not inspect.isabstract(office::Employee)


def test_office::employee_constructor_exists():
    assert callable(office::Employee.__init__)


def test_office::employee_constructor_args():
    sig = inspect.signature(office::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_office::employee_has_title():
    assert hasattr(office::Employee, "title")
    descriptor = None
    for klass in office::Employee.__mro__:
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



def test_office::officeelement_is_not_abstract():
    assert not inspect.isabstract(office::OfficeElement)


def test_office::officeelement_constructor_exists():
    assert callable(office::OfficeElement.__init__)


def test_office::officeelement_constructor_args():
    sig = inspect.signature(office::OfficeElement.__init__)
    params = list(sig.parameters.keys())



def test_office::officemodel_is_not_abstract():
    assert not inspect.isabstract(office::OfficeModel)


def test_office::officemodel_constructor_exists():
    assert callable(office::OfficeModel.__init__)


def test_office::officemodel_constructor_args():
    sig = inspect.signature(office::OfficeModel.__init__)
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
office::NamedElement_strategy = st.builds(
    office::NamedElement,
    name=
        safe_text
)
OfficeElement_strategy = st.builds(
    OfficeElement,
)
office::Office_strategy = st.builds(
    office::Office,
)
office::Employee_strategy = st.builds(
    office::Employee,
    title=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
office::OfficeElement_strategy = st.builds(
    office::OfficeElement,
)
office::OfficeModel_strategy = st.builds(
    office::OfficeModel,
)

@given(instance=office::NamedElement_strategy)
@settings(max_examples=50)
def test_office::namedelement_instantiation(instance):
    assert isinstance(instance, office::NamedElement)

@given(instance=office::NamedElement_strategy)
def test_office::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=office::NamedElement_strategy)
def test_office::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OfficeElement_strategy)
@settings(max_examples=50)
def test_officeelement_instantiation(instance):
    assert isinstance(instance, OfficeElement)

@given(instance=office::Office_strategy)
@settings(max_examples=50)
def test_office::office_instantiation(instance):
    assert isinstance(instance, office::Office)

@given(instance=office::Employee_strategy)
@settings(max_examples=50)
def test_office::employee_instantiation(instance):
    assert isinstance(instance, office::Employee)

@given(instance=office::Employee_strategy)
def test_office::employee_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=office::Employee_strategy)
def test_office::employee_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=office::OfficeElement_strategy)
@settings(max_examples=50)
def test_office::officeelement_instantiation(instance):
    assert isinstance(instance, office::OfficeElement)

@given(instance=office::OfficeModel_strategy)
@settings(max_examples=50)
def test_office::officemodel_instantiation(instance):
    assert isinstance(instance, office::OfficeModel)
