import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    basicfamily::Woman,
    basicfamily::Man,
    basicfamily::Person,
    basicfamily::Family,
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



def test_basicfamily::woman_is_not_abstract():
    assert not inspect.isabstract(basicfamily::Woman)


def test_basicfamily::woman_constructor_exists():
    assert callable(basicfamily::Woman.__init__)


def test_basicfamily::woman_constructor_args():
    sig = inspect.signature(basicfamily::Woman.__init__)
    params = list(sig.parameters.keys())



def test_basicfamily::man_is_not_abstract():
    assert not inspect.isabstract(basicfamily::Man)


def test_basicfamily::man_constructor_exists():
    assert callable(basicfamily::Man.__init__)


def test_basicfamily::man_constructor_args():
    sig = inspect.signature(basicfamily::Man.__init__)
    params = list(sig.parameters.keys())



def test_basicfamily::person_is_not_abstract():
    assert not inspect.isabstract(basicfamily::Person)


def test_basicfamily::person_constructor_exists():
    assert callable(basicfamily::Person.__init__)


def test_basicfamily::person_constructor_args():
    sig = inspect.signature(basicfamily::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfamily::person_has_name():
    assert hasattr(basicfamily::Person, "name")
    descriptor = None
    for klass in basicfamily::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basicfamily::family_is_not_abstract():
    assert not inspect.isabstract(basicfamily::Family)


def test_basicfamily::family_constructor_exists():
    assert callable(basicfamily::Family.__init__)


def test_basicfamily::family_constructor_args():
    sig = inspect.signature(basicfamily::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfamily::family_has_name():
    assert hasattr(basicfamily::Family, "name")
    descriptor = None
    for klass in basicfamily::Family.__mro__:
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
basicfamily::Woman_strategy = st.builds(
    basicfamily::Woman,
)
basicfamily::Man_strategy = st.builds(
    basicfamily::Man,
)
basicfamily::Person_strategy = st.builds(
    basicfamily::Person,
    name=
        safe_text
)
basicfamily::Family_strategy = st.builds(
    basicfamily::Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=basicfamily::Woman_strategy)
@settings(max_examples=50)
def test_basicfamily::woman_instantiation(instance):
    assert isinstance(instance, basicfamily::Woman)

@given(instance=basicfamily::Man_strategy)
@settings(max_examples=50)
def test_basicfamily::man_instantiation(instance):
    assert isinstance(instance, basicfamily::Man)

@given(instance=basicfamily::Person_strategy)
@settings(max_examples=50)
def test_basicfamily::person_instantiation(instance):
    assert isinstance(instance, basicfamily::Person)

@given(instance=basicfamily::Person_strategy)
def test_basicfamily::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicfamily::Person_strategy)
def test_basicfamily::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicfamily::Family_strategy)
@settings(max_examples=50)
def test_basicfamily::family_instantiation(instance):
    assert isinstance(instance, basicfamily::Family)

@given(instance=basicfamily::Family_strategy)
def test_basicfamily::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicfamily::Family_strategy)
def test_basicfamily::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
