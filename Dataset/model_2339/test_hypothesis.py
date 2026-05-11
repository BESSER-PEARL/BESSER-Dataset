import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    person::PersonType,
    person::CompanyType,
    person::EStringToStringMapEntry,
    person::DocumentRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person::persontype_is_not_abstract():
    assert not inspect.isabstract(person::PersonType)


def test_person::persontype_constructor_exists():
    assert callable(person::PersonType.__init__)


def test_person::persontype_constructor_args():
    sig = inspect.signature(person::PersonType.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "country" in params, "Missing parameter 'country'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_person::persontype_has_email():
    assert hasattr(person::PersonType, "email")
    descriptor = None
    for klass in person::PersonType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_person::persontype_has_country():
    assert hasattr(person::PersonType, "country")
    descriptor = None
    for klass in person::PersonType.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_person::persontype_has_name():
    assert hasattr(person::PersonType, "name")
    descriptor = None
    for klass in person::PersonType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person::persontype_has_age():
    assert hasattr(person::PersonType, "age")
    descriptor = None
    for klass in person::PersonType.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_person::companytype_is_not_abstract():
    assert not inspect.isabstract(person::CompanyType)


def test_person::companytype_constructor_exists():
    assert callable(person::CompanyType.__init__)


def test_person::companytype_constructor_args():
    sig = inspect.signature(person::CompanyType.__init__)
    params = list(sig.parameters.keys())



def test_person::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(person::EStringToStringMapEntry)


def test_person::estringtostringmapentry_constructor_exists():
    assert callable(person::EStringToStringMapEntry.__init__)


def test_person::estringtostringmapentry_constructor_args():
    sig = inspect.signature(person::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_person::documentroot_is_not_abstract():
    assert not inspect.isabstract(person::DocumentRoot)


def test_person::documentroot_constructor_exists():
    assert callable(person::DocumentRoot.__init__)


def test_person::documentroot_constructor_args():
    sig = inspect.signature(person::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_person::documentroot_has_mixed():
    assert hasattr(person::DocumentRoot, "mixed")
    descriptor = None
    for klass in person::DocumentRoot.__mro__:
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
person::PersonType_strategy = st.builds(
    person::PersonType,
    email=
        safe_text,
    country=
        safe_text,
    name=
        safe_text,
    age=
        safe_text
)
person::CompanyType_strategy = st.builds(
    person::CompanyType,
)
person::EStringToStringMapEntry_strategy = st.builds(
    person::EStringToStringMapEntry,
)
person::DocumentRoot_strategy = st.builds(
    person::DocumentRoot,
    mixed=
        safe_text
)

@given(instance=person::PersonType_strategy)
@settings(max_examples=50)
def test_person::persontype_instantiation(instance):
    assert isinstance(instance, person::PersonType)

@given(instance=person::PersonType_strategy)
def test_person::persontype_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=person::PersonType_strategy)
def test_person::persontype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=person::PersonType_strategy)
def test_person::persontype_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=person::PersonType_strategy)
def test_person::persontype_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=person::PersonType_strategy)
def test_person::persontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=person::PersonType_strategy)
def test_person::persontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=person::PersonType_strategy)
def test_person::persontype_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=person::PersonType_strategy)
def test_person::persontype_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=person::CompanyType_strategy)
@settings(max_examples=50)
def test_person::companytype_instantiation(instance):
    assert isinstance(instance, person::CompanyType)

@given(instance=person::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_person::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, person::EStringToStringMapEntry)

@given(instance=person::DocumentRoot_strategy)
@settings(max_examples=50)
def test_person::documentroot_instantiation(instance):
    assert isinstance(instance, person::DocumentRoot)

@given(instance=person::DocumentRoot_strategy)
def test_person::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=person::DocumentRoot_strategy)
def test_person::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
