import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Pet,
    family::Person,
    family::Family,
    family::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::pet_is_not_abstract():
    assert not inspect.isabstract(family::Pet)


def test_family::pet_constructor_exists():
    assert callable(family::Pet.__init__)


def test_family::pet_constructor_args():
    sig = inspect.signature(family::Pet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::pet_has_name():
    assert hasattr(family::Pet, "name")
    descriptor = None
    for klass in family::Pet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::person_has_name():
    assert hasattr(family::Person, "name")
    descriptor = None
    for klass in family::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())



def test_family::model_is_not_abstract():
    assert not inspect.isabstract(family::Model)


def test_family::model_constructor_exists():
    assert callable(family::Model.__init__)


def test_family::model_constructor_args():
    sig = inspect.signature(family::Model.__init__)
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
family::Pet_strategy = st.builds(
    family::Pet,
    name=
        safe_text
)
family::Person_strategy = st.builds(
    family::Person,
    name=
        safe_text
)
family::Family_strategy = st.builds(
    family::Family,
)
family::Model_strategy = st.builds(
    family::Model,
)

@given(instance=family::Pet_strategy)
@settings(max_examples=50)
def test_family::pet_instantiation(instance):
    assert isinstance(instance, family::Pet)

@given(instance=family::Pet_strategy)
def test_family::pet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Pet_strategy)
def test_family::pet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Model_strategy)
@settings(max_examples=50)
def test_family::model_instantiation(instance):
    assert isinstance(instance, family::Model)
