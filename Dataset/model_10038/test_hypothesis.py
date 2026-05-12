import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    t2::Son,
    t2::Dad,
    t2::Person,
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



def test_t2::son_is_not_abstract():
    assert not inspect.isabstract(t2::Son)


def test_t2::son_constructor_exists():
    assert callable(t2::Son.__init__)


def test_t2::son_constructor_args():
    sig = inspect.signature(t2::Son.__init__)
    params = list(sig.parameters.keys())



def test_t2::dad_is_not_abstract():
    assert not inspect.isabstract(t2::Dad)


def test_t2::dad_constructor_exists():
    assert callable(t2::Dad.__init__)


def test_t2::dad_constructor_args():
    sig = inspect.signature(t2::Dad.__init__)
    params = list(sig.parameters.keys())



def test_t2::person_is_not_abstract():
    assert not inspect.isabstract(t2::Person)


def test_t2::person_constructor_exists():
    assert callable(t2::Person.__init__)


def test_t2::person_constructor_args():
    sig = inspect.signature(t2::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_t2::person_has_age():
    assert hasattr(t2::Person, "age")
    descriptor = None
    for klass in t2::Person.__mro__:
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
Person_strategy = st.builds(
    Person,
)
t2::Son_strategy = st.builds(
    t2::Son,
)
t2::Dad_strategy = st.builds(
    t2::Dad,
)
t2::Person_strategy = st.builds(
    t2::Person,
    age=
        st.integers()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=t2::Son_strategy)
@settings(max_examples=50)
def test_t2::son_instantiation(instance):
    assert isinstance(instance, t2::Son)

@given(instance=t2::Dad_strategy)
@settings(max_examples=50)
def test_t2::dad_instantiation(instance):
    assert isinstance(instance, t2::Dad)

@given(instance=t2::Person_strategy)
@settings(max_examples=50)
def test_t2::person_instantiation(instance):
    assert isinstance(instance, t2::Person)

@given(instance=t2::Person_strategy)
def test_t2::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=t2::Person_strategy)
def test_t2::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
