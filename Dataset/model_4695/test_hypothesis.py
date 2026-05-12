import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    basicfamily_Woman,
    basicfamily_Man,
    basicfamily_Person,
    basicfamily_Family,
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



def test_basicfamily_woman_is_not_abstract():
    assert not inspect.isabstract(basicfamily_Woman)


def test_basicfamily_woman_constructor_exists():
    assert callable(basicfamily_Woman.__init__)


def test_basicfamily_woman_constructor_args():
    sig = inspect.signature(basicfamily_Woman.__init__)
    params = list(sig.parameters.keys())



def test_basicfamily_man_is_not_abstract():
    assert not inspect.isabstract(basicfamily_Man)


def test_basicfamily_man_constructor_exists():
    assert callable(basicfamily_Man.__init__)


def test_basicfamily_man_constructor_args():
    sig = inspect.signature(basicfamily_Man.__init__)
    params = list(sig.parameters.keys())



def test_basicfamily_person_is_not_abstract():
    assert not inspect.isabstract(basicfamily_Person)


def test_basicfamily_person_constructor_exists():
    assert callable(basicfamily_Person.__init__)


def test_basicfamily_person_constructor_args():
    sig = inspect.signature(basicfamily_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfamily_person_has_name():
    assert hasattr(basicfamily_Person, "name")
    descriptor = None
    for klass in basicfamily_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basicfamily_family_is_not_abstract():
    assert not inspect.isabstract(basicfamily_Family)


def test_basicfamily_family_constructor_exists():
    assert callable(basicfamily_Family.__init__)


def test_basicfamily_family_constructor_args():
    sig = inspect.signature(basicfamily_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfamily_family_has_name():
    assert hasattr(basicfamily_Family, "name")
    descriptor = None
    for klass in basicfamily_Family.__mro__:
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
basicfamily_Woman_strategy = st.builds(
    basicfamily_Woman,
)
basicfamily_Man_strategy = st.builds(
    basicfamily_Man,
)
basicfamily_Person_strategy = st.builds(
    basicfamily_Person,
    name=
        safe_text
)
basicfamily_Family_strategy = st.builds(
    basicfamily_Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=basicfamily_Woman_strategy)
@settings(max_examples=50)
def test_basicfamily_woman_instantiation(instance):
    assert isinstance(instance, basicfamily_Woman)

@given(instance=basicfamily_Man_strategy)
@settings(max_examples=50)
def test_basicfamily_man_instantiation(instance):
    assert isinstance(instance, basicfamily_Man)

@given(instance=basicfamily_Person_strategy)
@settings(max_examples=50)
def test_basicfamily_person_instantiation(instance):
    assert isinstance(instance, basicfamily_Person)



@given(instance=basicfamily_Person_strategy)
def test_basicfamily_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicfamily_Family_strategy)
@settings(max_examples=50)
def test_basicfamily_family_instantiation(instance):
    assert isinstance(instance, basicfamily_Family)



@given(instance=basicfamily_Family_strategy)
def test_basicfamily_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
