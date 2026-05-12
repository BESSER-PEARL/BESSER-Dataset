import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    ExtendedFamilies_Female,
    ExtendedFamilies_Male,
    ExtendedFamilies_Person,
    ExtendedFamilies_Family,
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



def test_extendedfamilies_female_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies_Female)


def test_extendedfamilies_female_constructor_exists():
    assert callable(ExtendedFamilies_Female.__init__)


def test_extendedfamilies_female_constructor_args():
    sig = inspect.signature(ExtendedFamilies_Female.__init__)
    params = list(sig.parameters.keys())



def test_extendedfamilies_male_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies_Male)


def test_extendedfamilies_male_constructor_exists():
    assert callable(ExtendedFamilies_Male.__init__)


def test_extendedfamilies_male_constructor_args():
    sig = inspect.signature(ExtendedFamilies_Male.__init__)
    params = list(sig.parameters.keys())



def test_extendedfamilies_person_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies_Person)


def test_extendedfamilies_person_constructor_exists():
    assert callable(ExtendedFamilies_Person.__init__)


def test_extendedfamilies_person_constructor_args():
    sig = inspect.signature(ExtendedFamilies_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_extendedfamilies_person_has_firstName():
    assert hasattr(ExtendedFamilies_Person, "firstName")
    descriptor = None
    for klass in ExtendedFamilies_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_extendedfamilies_family_is_not_abstract():
    assert not inspect.isabstract(ExtendedFamilies_Family)


def test_extendedfamilies_family_constructor_exists():
    assert callable(ExtendedFamilies_Family.__init__)


def test_extendedfamilies_family_constructor_args():
    sig = inspect.signature(ExtendedFamilies_Family.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleParent" in params, "Missing parameter 'isSingleParent'"
    assert "noOfChildren" in params, "Missing parameter 'noOfChildren'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_extendedfamilies_family_has_isSingleParent():
    assert hasattr(ExtendedFamilies_Family, "isSingleParent")
    descriptor = None
    for klass in ExtendedFamilies_Family.__mro__:
        if "isSingleParent" in klass.__dict__:
            descriptor = klass.__dict__["isSingleParent"]
            break
    assert isinstance(descriptor, property)

def test_extendedfamilies_family_has_noOfChildren():
    assert hasattr(ExtendedFamilies_Family, "noOfChildren")
    descriptor = None
    for klass in ExtendedFamilies_Family.__mro__:
        if "noOfChildren" in klass.__dict__:
            descriptor = klass.__dict__["noOfChildren"]
            break
    assert isinstance(descriptor, property)

def test_extendedfamilies_family_has_lastName():
    assert hasattr(ExtendedFamilies_Family, "lastName")
    descriptor = None
    for klass in ExtendedFamilies_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
ExtendedFamilies_Female_strategy = st.builds(
    ExtendedFamilies_Female,
)
ExtendedFamilies_Male_strategy = st.builds(
    ExtendedFamilies_Male,
)
ExtendedFamilies_Person_strategy = st.builds(
    ExtendedFamilies_Person,
    firstName=
        safe_text
)
ExtendedFamilies_Family_strategy = st.builds(
    ExtendedFamilies_Family,
    isSingleParent=
        st.booleans(),
    noOfChildren=
        st.integers(),
    lastName=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=ExtendedFamilies_Female_strategy)
@settings(max_examples=50)
def test_extendedfamilies_female_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies_Female)

@given(instance=ExtendedFamilies_Male_strategy)
@settings(max_examples=50)
def test_extendedfamilies_male_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies_Male)

@given(instance=ExtendedFamilies_Person_strategy)
@settings(max_examples=50)
def test_extendedfamilies_person_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies_Person)



@given(instance=ExtendedFamilies_Person_strategy)
def test_extendedfamilies_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=ExtendedFamilies_Family_strategy)
@settings(max_examples=50)
def test_extendedfamilies_family_instantiation(instance):
    assert isinstance(instance, ExtendedFamilies_Family)



@given(instance=ExtendedFamilies_Family_strategy)
def test_extendedfamilies_family_isSingleParent_setter(instance):
    original = instance.isSingleParent
    instance.isSingleParent = original
    assert instance.isSingleParent == original



@given(instance=ExtendedFamilies_Family_strategy)
def test_extendedfamilies_family_noOfChildren_setter(instance):
    original = instance.noOfChildren
    instance.noOfChildren = original
    assert instance.noOfChildren == original



@given(instance=ExtendedFamilies_Family_strategy)
def test_extendedfamilies_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
