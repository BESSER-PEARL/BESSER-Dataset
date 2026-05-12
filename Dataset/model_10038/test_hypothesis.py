import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    t2_Son,
    t2_Dad,
    t2_Person,
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



def test_t2_son_is_not_abstract():
    assert not inspect.isabstract(t2_Son)


def test_t2_son_constructor_exists():
    assert callable(t2_Son.__init__)


def test_t2_son_constructor_args():
    sig = inspect.signature(t2_Son.__init__)
    params = list(sig.parameters.keys())



def test_t2_dad_is_not_abstract():
    assert not inspect.isabstract(t2_Dad)


def test_t2_dad_constructor_exists():
    assert callable(t2_Dad.__init__)


def test_t2_dad_constructor_args():
    sig = inspect.signature(t2_Dad.__init__)
    params = list(sig.parameters.keys())



def test_t2_person_is_not_abstract():
    assert not inspect.isabstract(t2_Person)


def test_t2_person_constructor_exists():
    assert callable(t2_Person.__init__)


def test_t2_person_constructor_args():
    sig = inspect.signature(t2_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_t2_person_has_age():
    assert hasattr(t2_Person, "age")
    descriptor = None
    for klass in t2_Person.__mro__:
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
t2_Son_strategy = st.builds(
    t2_Son,
)
t2_Dad_strategy = st.builds(
    t2_Dad,
)
t2_Person_strategy = st.builds(
    t2_Person,
    age=
        st.integers()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=t2_Son_strategy)
@settings(max_examples=50)
def test_t2_son_instantiation(instance):
    assert isinstance(instance, t2_Son)

@given(instance=t2_Dad_strategy)
@settings(max_examples=50)
def test_t2_dad_instantiation(instance):
    assert isinstance(instance, t2_Dad)

@given(instance=t2_Person_strategy)
@settings(max_examples=50)
def test_t2_person_instantiation(instance):
    assert isinstance(instance, t2_Person)



@given(instance=t2_Person_strategy)
def test_t2_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
