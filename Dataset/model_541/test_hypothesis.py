import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Mother,
    family::Family,
    family::FatherInLove,
    family::Daughter,
    family::Son,
    family::Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::mother_is_not_abstract():
    assert not inspect.isabstract(family::Mother)


def test_family::mother_constructor_exists():
    assert callable(family::Mother.__init__)


def test_family::mother_constructor_args():
    sig = inspect.signature(family::Mother.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_family::mother_has_Age():
    assert hasattr(family::Mother, "Age")
    descriptor = None
    for klass in family::Mother.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_family::mother_has_Name():
    assert hasattr(family::Mother, "Name")
    descriptor = None
    for klass in family::Mother.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())



def test_family::fatherinlove_is_not_abstract():
    assert not inspect.isabstract(family::FatherInLove)


def test_family::fatherinlove_constructor_exists():
    assert callable(family::FatherInLove.__init__)


def test_family::fatherinlove_constructor_args():
    sig = inspect.signature(family::FatherInLove.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_family::fatherinlove_has_Name():
    assert hasattr(family::FatherInLove, "Name")
    descriptor = None
    for klass in family::FatherInLove.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_family::fatherinlove_has_Age():
    assert hasattr(family::FatherInLove, "Age")
    descriptor = None
    for klass in family::FatherInLove.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)



def test_family::daughter_is_not_abstract():
    assert not inspect.isabstract(family::Daughter)


def test_family::daughter_constructor_exists():
    assert callable(family::Daughter.__init__)


def test_family::daughter_constructor_args():
    sig = inspect.signature(family::Daughter.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_family::daughter_has_Age():
    assert hasattr(family::Daughter, "Age")
    descriptor = None
    for klass in family::Daughter.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_family::daughter_has_Name():
    assert hasattr(family::Daughter, "Name")
    descriptor = None
    for klass in family::Daughter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_family::son_is_not_abstract():
    assert not inspect.isabstract(family::Son)


def test_family::son_constructor_exists():
    assert callable(family::Son.__init__)


def test_family::son_constructor_args():
    sig = inspect.signature(family::Son.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_family::son_has_Name():
    assert hasattr(family::Son, "Name")
    descriptor = None
    for klass in family::Son.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_family::son_has_Age():
    assert hasattr(family::Son, "Age")
    descriptor = None
    for klass in family::Son.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)



def test_family::father_is_not_abstract():
    assert not inspect.isabstract(family::Father)


def test_family::father_constructor_exists():
    assert callable(family::Father.__init__)


def test_family::father_constructor_args():
    sig = inspect.signature(family::Father.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_family::father_has_Name():
    assert hasattr(family::Father, "Name")
    descriptor = None
    for klass in family::Father.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_family::father_has_Age():
    assert hasattr(family::Father, "Age")
    descriptor = None
    for klass in family::Father.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
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
family::Mother_strategy = st.builds(
    family::Mother,
    Age=
        st.integers(),
    Name=
        safe_text
)
family::Family_strategy = st.builds(
    family::Family,
)
family::FatherInLove_strategy = st.builds(
    family::FatherInLove,
    Name=
        safe_text,
    Age=
        st.integers()
)
family::Daughter_strategy = st.builds(
    family::Daughter,
    Age=
        st.integers(),
    Name=
        safe_text
)
family::Son_strategy = st.builds(
    family::Son,
    Name=
        safe_text,
    Age=
        st.integers()
)
family::Father_strategy = st.builds(
    family::Father,
    Name=
        safe_text,
    Age=
        st.integers()
)

@given(instance=family::Mother_strategy)
@settings(max_examples=50)
def test_family::mother_instantiation(instance):
    assert isinstance(instance, family::Mother)

@given(instance=family::Mother_strategy)
def test_family::mother_Age_type(instance):
    assert isinstance(instance.Age, int)


@given(instance=family::Mother_strategy)
def test_family::mother_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family::Mother_strategy)
def test_family::mother_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=family::Mother_strategy)
def test_family::mother_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::FatherInLove_strategy)
@settings(max_examples=50)
def test_family::fatherinlove_instantiation(instance):
    assert isinstance(instance, family::FatherInLove)

@given(instance=family::FatherInLove_strategy)
def test_family::fatherinlove_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=family::FatherInLove_strategy)
def test_family::fatherinlove_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family::FatherInLove_strategy)
def test_family::fatherinlove_Age_type(instance):
    assert isinstance(instance.Age, int)


@given(instance=family::FatherInLove_strategy)
def test_family::fatherinlove_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family::Daughter_strategy)
@settings(max_examples=50)
def test_family::daughter_instantiation(instance):
    assert isinstance(instance, family::Daughter)

@given(instance=family::Daughter_strategy)
def test_family::daughter_Age_type(instance):
    assert isinstance(instance.Age, int)


@given(instance=family::Daughter_strategy)
def test_family::daughter_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family::Daughter_strategy)
def test_family::daughter_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=family::Daughter_strategy)
def test_family::daughter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family::Son_strategy)
@settings(max_examples=50)
def test_family::son_instantiation(instance):
    assert isinstance(instance, family::Son)

@given(instance=family::Son_strategy)
def test_family::son_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=family::Son_strategy)
def test_family::son_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family::Son_strategy)
def test_family::son_Age_type(instance):
    assert isinstance(instance.Age, int)


@given(instance=family::Son_strategy)
def test_family::son_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family::Father_strategy)
@settings(max_examples=50)
def test_family::father_instantiation(instance):
    assert isinstance(instance, family::Father)

@given(instance=family::Father_strategy)
def test_family::father_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=family::Father_strategy)
def test_family::father_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family::Father_strategy)
def test_family::father_Age_type(instance):
    assert isinstance(instance.Age, int)


@given(instance=family::Father_strategy)
def test_family::father_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original
