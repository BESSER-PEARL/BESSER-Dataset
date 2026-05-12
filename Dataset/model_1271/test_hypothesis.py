import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_ecore_Family,
    family_ecore_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_ecore_family_is_not_abstract():
    assert not inspect.isabstract(family_ecore_Family)


def test_family_ecore_family_constructor_exists():
    assert callable(family_ecore_Family.__init__)


def test_family_ecore_family_constructor_args():
    sig = inspect.signature(family_ecore_Family.__init__)
    params = list(sig.parameters.keys())



def test_family_ecore_person_is_not_abstract():
    assert not inspect.isabstract(family_ecore_Person)


def test_family_ecore_person_constructor_exists():
    assert callable(family_ecore_Person.__init__)


def test_family_ecore_person_constructor_args():
    sig = inspect.signature(family_ecore_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_family_ecore_person_has_name():
    assert hasattr(family_ecore_Person, "name")
    descriptor = None
    for klass in family_ecore_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family_ecore_person_has_age():
    assert hasattr(family_ecore_Person, "age")
    descriptor = None
    for klass in family_ecore_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
family_ecore_Family_strategy = st.builds(
    family_ecore_Family,
)
family_ecore_Person_strategy = st.builds(
    family_ecore_Person,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=family_ecore_Family_strategy)
@settings(max_examples=50)
def test_family_ecore_family_instantiation(instance):
    assert isinstance(instance, family_ecore_Family)

@given(instance=family_ecore_Person_strategy)
@settings(max_examples=50)
def test_family_ecore_person_instantiation(instance):
    assert isinstance(instance, family_ecore_Person)



@given(instance=family_ecore_Person_strategy)
def test_family_ecore_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=family_ecore_Person_strategy)
def test_family_ecore_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
