import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_person,
    family_studyprogramme,
    family_university,
    family_Root,
    family_family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_person)


def test_family_person_constructor_exists():
    assert callable(family_person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_person.__init__)
    params = list(sig.parameters.keys())
    assert "cpr" in params, "Missing parameter 'cpr'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_family_person_has_cpr():
    assert hasattr(family_person, "cpr")
    descriptor = None
    for klass in family_person.__mro__:
        if "cpr" in klass.__dict__:
            descriptor = klass.__dict__["cpr"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_name():
    assert hasattr(family_person, "name")
    descriptor = None
    for klass in family_person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_age():
    assert hasattr(family_person, "age")
    descriptor = None
    for klass in family_person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_family_studyprogramme_is_not_abstract():
    assert not inspect.isabstract(family_studyprogramme)


def test_family_studyprogramme_constructor_exists():
    assert callable(family_studyprogramme.__init__)


def test_family_studyprogramme_constructor_args():
    sig = inspect.signature(family_studyprogramme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_studyprogramme_has_name():
    assert hasattr(family_studyprogramme, "name")
    descriptor = None
    for klass in family_studyprogramme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family_university_is_not_abstract():
    assert not inspect.isabstract(family_university)


def test_family_university_constructor_exists():
    assert callable(family_university.__init__)


def test_family_university_constructor_args():
    sig = inspect.signature(family_university.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_university_has_name():
    assert hasattr(family_university, "name")
    descriptor = None
    for klass in family_university.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family_root_is_not_abstract():
    assert not inspect.isabstract(family_Root)


def test_family_root_constructor_exists():
    assert callable(family_Root.__init__)


def test_family_root_constructor_args():
    sig = inspect.signature(family_Root.__init__)
    params = list(sig.parameters.keys())



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_family)


def test_family_family_constructor_exists():
    assert callable(family_family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_family_has_name():
    assert hasattr(family_family, "name")
    descriptor = None
    for klass in family_family.__mro__:
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
family_person_strategy = st.builds(
    family_person,
    cpr=
        safe_text,
    name=
        safe_text,
    age=
        safe_text
)
family_studyprogramme_strategy = st.builds(
    family_studyprogramme,
    name=
        safe_text
)
family_university_strategy = st.builds(
    family_university,
    name=
        safe_text
)
family_Root_strategy = st.builds(
    family_Root,
)
family_family_strategy = st.builds(
    family_family,
    name=
        safe_text
)

@given(instance=family_person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_person)



@given(instance=family_person_strategy)
def test_family_person_cpr_setter(instance):
    original = instance.cpr
    instance.cpr = original
    assert instance.cpr == original



@given(instance=family_person_strategy)
def test_family_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=family_person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family_studyprogramme_strategy)
@settings(max_examples=50)
def test_family_studyprogramme_instantiation(instance):
    assert isinstance(instance, family_studyprogramme)



@given(instance=family_studyprogramme_strategy)
def test_family_studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family_university_strategy)
@settings(max_examples=50)
def test_family_university_instantiation(instance):
    assert isinstance(instance, family_university)



@given(instance=family_university_strategy)
def test_family_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family_Root_strategy)
@settings(max_examples=50)
def test_family_root_instantiation(instance):
    assert isinstance(instance, family_Root)

@given(instance=family_family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_family)



@given(instance=family_family_strategy)
def test_family_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
