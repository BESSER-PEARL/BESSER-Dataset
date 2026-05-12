import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    Friends_Woman,
    Friends_Man,
    Friends_Classroom,
    Friends_Person,
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



def test_friends_woman_is_not_abstract():
    assert not inspect.isabstract(Friends_Woman)


def test_friends_woman_constructor_exists():
    assert callable(Friends_Woman.__init__)


def test_friends_woman_constructor_args():
    sig = inspect.signature(Friends_Woman.__init__)
    params = list(sig.parameters.keys())



def test_friends_man_is_not_abstract():
    assert not inspect.isabstract(Friends_Man)


def test_friends_man_constructor_exists():
    assert callable(Friends_Man.__init__)


def test_friends_man_constructor_args():
    sig = inspect.signature(Friends_Man.__init__)
    params = list(sig.parameters.keys())



def test_friends_classroom_is_not_abstract():
    assert not inspect.isabstract(Friends_Classroom)


def test_friends_classroom_constructor_exists():
    assert callable(Friends_Classroom.__init__)


def test_friends_classroom_constructor_args():
    sig = inspect.signature(Friends_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_friends_classroom_has_id():
    assert hasattr(Friends_Classroom, "id")
    descriptor = None
    for klass in Friends_Classroom.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_friends_person_is_not_abstract():
    assert not inspect.isabstract(Friends_Person)


def test_friends_person_constructor_exists():
    assert callable(Friends_Person.__init__)


def test_friends_person_constructor_args():
    sig = inspect.signature(Friends_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_friends_person_has_name():
    assert hasattr(Friends_Person, "name")
    descriptor = None
    for klass in Friends_Person.__mro__:
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
Friends_Woman_strategy = st.builds(
    Friends_Woman,
)
Friends_Man_strategy = st.builds(
    Friends_Man,
)
Friends_Classroom_strategy = st.builds(
    Friends_Classroom,
    id=
        st.integers()
)
Friends_Person_strategy = st.builds(
    Friends_Person,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Friends_Woman_strategy)
@settings(max_examples=50)
def test_friends_woman_instantiation(instance):
    assert isinstance(instance, Friends_Woman)

@given(instance=Friends_Man_strategy)
@settings(max_examples=50)
def test_friends_man_instantiation(instance):
    assert isinstance(instance, Friends_Man)

@given(instance=Friends_Classroom_strategy)
@settings(max_examples=50)
def test_friends_classroom_instantiation(instance):
    assert isinstance(instance, Friends_Classroom)



@given(instance=Friends_Classroom_strategy)
def test_friends_classroom_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Friends_Person_strategy)
@settings(max_examples=50)
def test_friends_person_instantiation(instance):
    assert isinstance(instance, Friends_Person)



@given(instance=Friends_Person_strategy)
def test_friends_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
