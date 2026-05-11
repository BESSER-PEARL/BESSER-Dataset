import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    Friends::Woman,
    Friends::Man,
    Friends::Classroom,
    Friends::Person,
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



def test_friends::woman_is_not_abstract():
    assert not inspect.isabstract(Friends::Woman)


def test_friends::woman_constructor_exists():
    assert callable(Friends::Woman.__init__)


def test_friends::woman_constructor_args():
    sig = inspect.signature(Friends::Woman.__init__)
    params = list(sig.parameters.keys())



def test_friends::man_is_not_abstract():
    assert not inspect.isabstract(Friends::Man)


def test_friends::man_constructor_exists():
    assert callable(Friends::Man.__init__)


def test_friends::man_constructor_args():
    sig = inspect.signature(Friends::Man.__init__)
    params = list(sig.parameters.keys())



def test_friends::classroom_is_not_abstract():
    assert not inspect.isabstract(Friends::Classroom)


def test_friends::classroom_constructor_exists():
    assert callable(Friends::Classroom.__init__)


def test_friends::classroom_constructor_args():
    sig = inspect.signature(Friends::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_friends::classroom_has_id():
    assert hasattr(Friends::Classroom, "id")
    descriptor = None
    for klass in Friends::Classroom.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_friends::person_is_not_abstract():
    assert not inspect.isabstract(Friends::Person)


def test_friends::person_constructor_exists():
    assert callable(Friends::Person.__init__)


def test_friends::person_constructor_args():
    sig = inspect.signature(Friends::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_friends::person_has_name():
    assert hasattr(Friends::Person, "name")
    descriptor = None
    for klass in Friends::Person.__mro__:
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
Friends::Woman_strategy = st.builds(
    Friends::Woman,
)
Friends::Man_strategy = st.builds(
    Friends::Man,
)
Friends::Classroom_strategy = st.builds(
    Friends::Classroom,
    id=
        st.integers()
)
Friends::Person_strategy = st.builds(
    Friends::Person,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Friends::Woman_strategy)
@settings(max_examples=50)
def test_friends::woman_instantiation(instance):
    assert isinstance(instance, Friends::Woman)

@given(instance=Friends::Man_strategy)
@settings(max_examples=50)
def test_friends::man_instantiation(instance):
    assert isinstance(instance, Friends::Man)

@given(instance=Friends::Classroom_strategy)
@settings(max_examples=50)
def test_friends::classroom_instantiation(instance):
    assert isinstance(instance, Friends::Classroom)

@given(instance=Friends::Classroom_strategy)
def test_friends::classroom_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Friends::Classroom_strategy)
def test_friends::classroom_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Friends::Person_strategy)
@settings(max_examples=50)
def test_friends::person_instantiation(instance):
    assert isinstance(instance, Friends::Person)

@given(instance=Friends::Person_strategy)
def test_friends::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Friends::Person_strategy)
def test_friends::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
