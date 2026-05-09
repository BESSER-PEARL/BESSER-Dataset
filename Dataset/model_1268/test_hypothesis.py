import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::person,
    family::studyprogramme,
    family::university,
    family::Root,
    family::family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::person)


def test_family::person_constructor_exists():
    assert callable(family::person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cpr" in params, "Missing parameter 'cpr'"

def test_family::person_has_age():
    assert hasattr(family::person, "age")
    descriptor = None
    for klass in family::person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_name():
    assert hasattr(family::person, "name")
    descriptor = None
    for klass in family::person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_cpr():
    assert hasattr(family::person, "cpr")
    descriptor = None
    for klass in family::person.__mro__:
        if "cpr" in klass.__dict__:
            descriptor = klass.__dict__["cpr"]
            break
    assert isinstance(descriptor, property)



def test_family::studyprogramme_is_not_abstract():
    assert not inspect.isabstract(family::studyprogramme)


def test_family::studyprogramme_constructor_exists():
    assert callable(family::studyprogramme.__init__)


def test_family::studyprogramme_constructor_args():
    sig = inspect.signature(family::studyprogramme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::studyprogramme_has_name():
    assert hasattr(family::studyprogramme, "name")
    descriptor = None
    for klass in family::studyprogramme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::university_is_not_abstract():
    assert not inspect.isabstract(family::university)


def test_family::university_constructor_exists():
    assert callable(family::university.__init__)


def test_family::university_constructor_args():
    sig = inspect.signature(family::university.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::university_has_name():
    assert hasattr(family::university, "name")
    descriptor = None
    for klass in family::university.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::root_is_not_abstract():
    assert not inspect.isabstract(family::Root)


def test_family::root_constructor_exists():
    assert callable(family::Root.__init__)


def test_family::root_constructor_args():
    sig = inspect.signature(family::Root.__init__)
    params = list(sig.parameters.keys())



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::family)


def test_family::family_constructor_exists():
    assert callable(family::family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::family_has_name():
    assert hasattr(family::family, "name")
    descriptor = None
    for klass in family::family.__mro__:
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
family::person_strategy = st.builds(
    family::person,
    age=
        safe_text,
    name=
        safe_text,
    cpr=
        safe_text
)
family::studyprogramme_strategy = st.builds(
    family::studyprogramme,
    name=
        safe_text
)
family::university_strategy = st.builds(
    family::university,
    name=
        safe_text
)
family::Root_strategy = st.builds(
    family::Root,
)
family::family_strategy = st.builds(
    family::family,
    name=
        safe_text
)

@given(instance=family::person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::person)

@given(instance=family::person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=family::person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::person_strategy)
def test_family::person_cpr_type(instance):
    assert isinstance(instance.cpr, str)


@given(instance=family::person_strategy)
def test_family::person_cpr_setter(instance):
    original = instance.cpr
    instance.cpr = original
    assert instance.cpr == original

@given(instance=family::studyprogramme_strategy)
@settings(max_examples=50)
def test_family::studyprogramme_instantiation(instance):
    assert isinstance(instance, family::studyprogramme)

@given(instance=family::studyprogramme_strategy)
def test_family::studyprogramme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::studyprogramme_strategy)
def test_family::studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::university_strategy)
@settings(max_examples=50)
def test_family::university_instantiation(instance):
    assert isinstance(instance, family::university)

@given(instance=family::university_strategy)
def test_family::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::university_strategy)
def test_family::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::Root_strategy)
@settings(max_examples=50)
def test_family::root_instantiation(instance):
    assert isinstance(instance, family::Root)

@given(instance=family::family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::family)

@given(instance=family::family_strategy)
def test_family::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::family_strategy)
def test_family::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
