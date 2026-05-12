import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_Mother,
    family_Family,
    family_FatherInLove,
    family_Daughter,
    family_Son,
    family_Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_mother_is_not_abstract():
    assert not inspect.isabstract(family_Mother)


def test_family_mother_constructor_exists():
    assert callable(family_Mother.__init__)


def test_family_mother_constructor_args():
    sig = inspect.signature(family_Mother.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_family_mother_has_Age():
    assert hasattr(family_Mother, "Age")
    descriptor = None
    for klass in family_Mother.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_family_mother_has_Name():
    assert hasattr(family_Mother, "Name")
    descriptor = None
    for klass in family_Mother.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())



def test_family_fatherinlove_is_not_abstract():
    assert not inspect.isabstract(family_FatherInLove)


def test_family_fatherinlove_constructor_exists():
    assert callable(family_FatherInLove.__init__)


def test_family_fatherinlove_constructor_args():
    sig = inspect.signature(family_FatherInLove.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_family_fatherinlove_has_Name():
    assert hasattr(family_FatherInLove, "Name")
    descriptor = None
    for klass in family_FatherInLove.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_family_fatherinlove_has_Age():
    assert hasattr(family_FatherInLove, "Age")
    descriptor = None
    for klass in family_FatherInLove.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)



def test_family_daughter_is_not_abstract():
    assert not inspect.isabstract(family_Daughter)


def test_family_daughter_constructor_exists():
    assert callable(family_Daughter.__init__)


def test_family_daughter_constructor_args():
    sig = inspect.signature(family_Daughter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_family_daughter_has_Name():
    assert hasattr(family_Daughter, "Name")
    descriptor = None
    for klass in family_Daughter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_family_daughter_has_Age():
    assert hasattr(family_Daughter, "Age")
    descriptor = None
    for klass in family_Daughter.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)



def test_family_son_is_not_abstract():
    assert not inspect.isabstract(family_Son)


def test_family_son_constructor_exists():
    assert callable(family_Son.__init__)


def test_family_son_constructor_args():
    sig = inspect.signature(family_Son.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_family_son_has_Age():
    assert hasattr(family_Son, "Age")
    descriptor = None
    for klass in family_Son.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_family_son_has_Name():
    assert hasattr(family_Son, "Name")
    descriptor = None
    for klass in family_Son.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_family_father_is_not_abstract():
    assert not inspect.isabstract(family_Father)


def test_family_father_constructor_exists():
    assert callable(family_Father.__init__)


def test_family_father_constructor_args():
    sig = inspect.signature(family_Father.__init__)
    params = list(sig.parameters.keys())
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_family_father_has_Age():
    assert hasattr(family_Father, "Age")
    descriptor = None
    for klass in family_Father.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_family_father_has_Name():
    assert hasattr(family_Father, "Name")
    descriptor = None
    for klass in family_Father.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
family_Mother_strategy = st.builds(
    family_Mother,
    Age=
        st.integers(),
    Name=
        safe_text
)
family_Family_strategy = st.builds(
    family_Family,
)
family_FatherInLove_strategy = st.builds(
    family_FatherInLove,
    Name=
        safe_text,
    Age=
        st.integers()
)
family_Daughter_strategy = st.builds(
    family_Daughter,
    Name=
        safe_text,
    Age=
        st.integers()
)
family_Son_strategy = st.builds(
    family_Son,
    Age=
        st.integers(),
    Name=
        safe_text
)
family_Father_strategy = st.builds(
    family_Father,
    Age=
        st.integers(),
    Name=
        safe_text
)

@given(instance=family_Mother_strategy)
@settings(max_examples=50)
def test_family_mother_instantiation(instance):
    assert isinstance(instance, family_Mother)



@given(instance=family_Mother_strategy)
def test_family_mother_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=family_Mother_strategy)
def test_family_mother_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)

@given(instance=family_FatherInLove_strategy)
@settings(max_examples=50)
def test_family_fatherinlove_instantiation(instance):
    assert isinstance(instance, family_FatherInLove)



@given(instance=family_FatherInLove_strategy)
def test_family_fatherinlove_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=family_FatherInLove_strategy)
def test_family_fatherinlove_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family_Daughter_strategy)
@settings(max_examples=50)
def test_family_daughter_instantiation(instance):
    assert isinstance(instance, family_Daughter)



@given(instance=family_Daughter_strategy)
def test_family_daughter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=family_Daughter_strategy)
def test_family_daughter_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=family_Son_strategy)
@settings(max_examples=50)
def test_family_son_instantiation(instance):
    assert isinstance(instance, family_Son)



@given(instance=family_Son_strategy)
def test_family_son_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=family_Son_strategy)
def test_family_son_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=family_Father_strategy)
@settings(max_examples=50)
def test_family_father_instantiation(instance):
    assert isinstance(instance, family_Father)



@given(instance=family_Father_strategy)
def test_family_father_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=family_Father_strategy)
def test_family_father_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
