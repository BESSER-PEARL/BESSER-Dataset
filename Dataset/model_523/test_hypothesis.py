import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    family::Child,
    family::Mother,
    family::Father,
    FNamedElement,
    family::Family,
    family::Person,
    family::FNamedElement,
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



def test_family::child_is_not_abstract():
    assert not inspect.isabstract(family::Child)


def test_family::child_constructor_exists():
    assert callable(family::Child.__init__)


def test_family::child_constructor_args():
    sig = inspect.signature(family::Child.__init__)
    params = list(sig.parameters.keys())



def test_family::mother_is_not_abstract():
    assert not inspect.isabstract(family::Mother)


def test_family::mother_constructor_exists():
    assert callable(family::Mother.__init__)


def test_family::mother_constructor_args():
    sig = inspect.signature(family::Mother.__init__)
    params = list(sig.parameters.keys())



def test_family::father_is_not_abstract():
    assert not inspect.isabstract(family::Father)


def test_family::father_constructor_exists():
    assert callable(family::Father.__init__)


def test_family::father_constructor_args():
    sig = inspect.signature(family::Father.__init__)
    params = list(sig.parameters.keys())



def test_fnamedelement_is_not_abstract():
    assert not inspect.isabstract(FNamedElement)


def test_fnamedelement_constructor_exists():
    assert callable(FNamedElement.__init__)


def test_fnamedelement_constructor_args():
    sig = inspect.signature(FNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_family::person_has_age():
    assert hasattr(family::Person, "age")
    descriptor = None
    for klass in family::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_sex():
    assert hasattr(family::Person, "sex")
    descriptor = None
    for klass in family::Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_family::fnamedelement_is_not_abstract():
    assert not inspect.isabstract(family::FNamedElement)


def test_family::fnamedelement_constructor_exists():
    assert callable(family::FNamedElement.__init__)


def test_family::fnamedelement_constructor_args():
    sig = inspect.signature(family::FNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::fnamedelement_has_name():
    assert hasattr(family::FNamedElement, "name")
    descriptor = None
    for klass in family::FNamedElement.__mro__:
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
family::Child_strategy = st.builds(
    family::Child,
)
family::Mother_strategy = st.builds(
    family::Mother,
)
family::Father_strategy = st.builds(
    family::Father,
)
FNamedElement_strategy = st.builds(
    FNamedElement,
)
family::Family_strategy = st.builds(
    family::Family,
)
family::Person_strategy = st.builds(
    family::Person,
    age=
        st.integers(),
    sex=
        safe_text
)
family::FNamedElement_strategy = st.builds(
    family::FNamedElement,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family::Child_strategy)
@settings(max_examples=50)
def test_family::child_instantiation(instance):
    assert isinstance(instance, family::Child)

@given(instance=family::Mother_strategy)
@settings(max_examples=50)
def test_family::mother_instantiation(instance):
    assert isinstance(instance, family::Mother)

@given(instance=family::Father_strategy)
@settings(max_examples=50)
def test_family::father_instantiation(instance):
    assert isinstance(instance, family::Father)

@given(instance=FNamedElement_strategy)
@settings(max_examples=50)
def test_fnamedelement_instantiation(instance):
    assert isinstance(instance, FNamedElement)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::Person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::Person_strategy)
def test_family::person_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=family::Person_strategy)
def test_family::person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=family::FNamedElement_strategy)
@settings(max_examples=50)
def test_family::fnamedelement_instantiation(instance):
    assert isinstance(instance, family::FNamedElement)

@given(instance=family::FNamedElement_strategy)
def test_family::fnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::FNamedElement_strategy)
def test_family::fnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
