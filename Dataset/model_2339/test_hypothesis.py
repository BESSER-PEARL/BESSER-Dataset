import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    person_PersonType,
    person_CompanyType,
    person_EStringToStringMapEntry,
    person_DocumentRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_persontype_is_not_abstract():
    assert not inspect.isabstract(person_PersonType)


def test_person_persontype_constructor_exists():
    assert callable(person_PersonType.__init__)


def test_person_persontype_constructor_args():
    sig = inspect.signature(person_PersonType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "email" in params, "Missing parameter 'email'"
    assert "country" in params, "Missing parameter 'country'"

def test_person_persontype_has_name():
    assert hasattr(person_PersonType, "name")
    descriptor = None
    for klass in person_PersonType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person_persontype_has_age():
    assert hasattr(person_PersonType, "age")
    descriptor = None
    for klass in person_PersonType.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_person_persontype_has_email():
    assert hasattr(person_PersonType, "email")
    descriptor = None
    for klass in person_PersonType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_person_persontype_has_country():
    assert hasattr(person_PersonType, "country")
    descriptor = None
    for klass in person_PersonType.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_person_companytype_is_not_abstract():
    assert not inspect.isabstract(person_CompanyType)


def test_person_companytype_constructor_exists():
    assert callable(person_CompanyType.__init__)


def test_person_companytype_constructor_args():
    sig = inspect.signature(person_CompanyType.__init__)
    params = list(sig.parameters.keys())



def test_person_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(person_EStringToStringMapEntry)


def test_person_estringtostringmapentry_constructor_exists():
    assert callable(person_EStringToStringMapEntry.__init__)


def test_person_estringtostringmapentry_constructor_args():
    sig = inspect.signature(person_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_person_documentroot_is_not_abstract():
    assert not inspect.isabstract(person_DocumentRoot)


def test_person_documentroot_constructor_exists():
    assert callable(person_DocumentRoot.__init__)


def test_person_documentroot_constructor_args():
    sig = inspect.signature(person_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_person_documentroot_has_mixed():
    assert hasattr(person_DocumentRoot, "mixed")
    descriptor = None
    for klass in person_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
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
person_PersonType_strategy = st.builds(
    person_PersonType,
    name=
        safe_text,
    age=
        safe_text,
    email=
        safe_text,
    country=
        safe_text
)
person_CompanyType_strategy = st.builds(
    person_CompanyType,
)
person_EStringToStringMapEntry_strategy = st.builds(
    person_EStringToStringMapEntry,
)
person_DocumentRoot_strategy = st.builds(
    person_DocumentRoot,
    mixed=
        safe_text
)

@given(instance=person_PersonType_strategy)
@settings(max_examples=50)
def test_person_persontype_instantiation(instance):
    assert isinstance(instance, person_PersonType)



@given(instance=person_PersonType_strategy)
def test_person_persontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=person_PersonType_strategy)
def test_person_persontype_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=person_PersonType_strategy)
def test_person_persontype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=person_PersonType_strategy)
def test_person_persontype_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=person_CompanyType_strategy)
@settings(max_examples=50)
def test_person_companytype_instantiation(instance):
    assert isinstance(instance, person_CompanyType)

@given(instance=person_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_person_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, person_EStringToStringMapEntry)

@given(instance=person_DocumentRoot_strategy)
@settings(max_examples=50)
def test_person_documentroot_instantiation(instance):
    assert isinstance(instance, person_DocumentRoot)



@given(instance=person_DocumentRoot_strategy)
def test_person_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
