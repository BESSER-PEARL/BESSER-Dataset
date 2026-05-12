import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    family_Child,
    family_Mother,
    family_Father,
    FNamedElement,
    family_Family,
    family_Person,
    family_FNamedElement,
    SexType,
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



def test_family_child_is_not_abstract():
    assert not inspect.isabstract(family_Child)


def test_family_child_constructor_exists():
    assert callable(family_Child.__init__)


def test_family_child_constructor_args():
    sig = inspect.signature(family_Child.__init__)
    params = list(sig.parameters.keys())



def test_family_mother_is_not_abstract():
    assert not inspect.isabstract(family_Mother)


def test_family_mother_constructor_exists():
    assert callable(family_Mother.__init__)


def test_family_mother_constructor_args():
    sig = inspect.signature(family_Mother.__init__)
    params = list(sig.parameters.keys())



def test_family_father_is_not_abstract():
    assert not inspect.isabstract(family_Father)


def test_family_father_constructor_exists():
    assert callable(family_Father.__init__)


def test_family_father_constructor_args():
    sig = inspect.signature(family_Father.__init__)
    params = list(sig.parameters.keys())



def test_fnamedelement_is_not_abstract():
    assert not inspect.isabstract(FNamedElement)


def test_fnamedelement_constructor_exists():
    assert callable(FNamedElement.__init__)


def test_fnamedelement_constructor_args():
    sig = inspect.signature(FNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "sex" in params, "Missing parameter 'sex'"
    assert "age" in params, "Missing parameter 'age'"

def test_family_person_has_sex():
    assert hasattr(family_Person, "sex")
    descriptor = None
    for klass in family_Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_age():
    assert hasattr(family_Person, "age")
    descriptor = None
    for klass in family_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_family_fnamedelement_is_not_abstract():
    assert not inspect.isabstract(family_FNamedElement)


def test_family_fnamedelement_constructor_exists():
    assert callable(family_FNamedElement.__init__)


def test_family_fnamedelement_constructor_args():
    sig = inspect.signature(family_FNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_fnamedelement_has_name():
    assert hasattr(family_FNamedElement, "name")
    descriptor = None
    for klass in family_FNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sextype_exists():
    # Check that the Enumeration exists
    assert SexType is not None

def test_sextype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SexType]
    expected_literals = [
        "male",
        "female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SexType"


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
family_Child_strategy = st.builds(
    family_Child,
)
family_Mother_strategy = st.builds(
    family_Mother,
)
family_Father_strategy = st.builds(
    family_Father,
)
FNamedElement_strategy = st.builds(
    FNamedElement,
)
family_Family_strategy = st.builds(
    family_Family,
)
family_Person_strategy = st.builds(
    family_Person,
    sex=
        safe_text,
    age=
        st.integers()
)
family_FNamedElement_strategy = st.builds(
    family_FNamedElement,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family_Child_strategy)
@settings(max_examples=50)
def test_family_child_instantiation(instance):
    assert isinstance(instance, family_Child)

@given(instance=family_Mother_strategy)
@settings(max_examples=50)
def test_family_mother_instantiation(instance):
    assert isinstance(instance, family_Mother)

@given(instance=family_Father_strategy)
@settings(max_examples=50)
def test_family_father_instantiation(instance):
    assert isinstance(instance, family_Father)

@given(instance=FNamedElement_strategy)
@settings(max_examples=50)
def test_fnamedelement_instantiation(instance):
    assert isinstance(instance, FNamedElement)

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=family_Person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family_FNamedElement_strategy)
@settings(max_examples=50)
def test_family_fnamedelement_instantiation(instance):
    assert isinstance(instance, family_FNamedElement)



@given(instance=family_FNamedElement_strategy)
def test_family_fnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
