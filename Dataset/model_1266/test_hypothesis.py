import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    family_Woman,
    family_Man,
    family_Person,
    family_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family_woman_is_not_abstract():
    assert not inspect.isabstract(family_Woman)


def test_family_woman_constructor_exists():
    assert callable(family_Woman.__init__)


def test_family_woman_constructor_args():
    sig = inspect.signature(family_Woman.__init__)
    params = list(sig.parameters.keys())



def test_family_man_is_not_abstract():
    assert not inspect.isabstract(family_Man)


def test_family_man_constructor_exists():
    assert callable(family_Man.__init__)


def test_family_man_constructor_args():
    sig = inspect.signature(family_Man.__init__)
    params = list(sig.parameters.keys())



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_person_has_name():
    assert hasattr(family_Person, "name")
    descriptor = None
    for klass in family_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_family_has_name():
    assert hasattr(family_Family, "name")
    descriptor = None
    for klass in family_Family.__mro__:
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
Person_strategy = st.builds(
    Person,
)
family_Woman_strategy = st.builds(
    family_Woman,
)
family_Man_strategy = st.builds(
    family_Man,
)
family_Person_strategy = st.builds(
    family_Person,
    name=
        safe_text
)
family_Family_strategy = st.builds(
    family_Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family_Woman_strategy)
@settings(max_examples=50)
def test_family_woman_instantiation(instance):
    assert isinstance(instance, family_Woman)

@given(instance=family_Man_strategy)
@settings(max_examples=50)
def test_family_man_instantiation(instance):
    assert isinstance(instance, family_Man)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
