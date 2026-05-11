import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    familytree::Man,
    familytree::Woman,
    familytree::FamilyTree,
    familytree::Person,
    RelationshipStatus,
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



def test_familytree::man_is_not_abstract():
    assert not inspect.isabstract(familytree::Man)


def test_familytree::man_constructor_exists():
    assert callable(familytree::Man.__init__)


def test_familytree::man_constructor_args():
    sig = inspect.signature(familytree::Man.__init__)
    params = list(sig.parameters.keys())



def test_familytree::woman_is_not_abstract():
    assert not inspect.isabstract(familytree::Woman)


def test_familytree::woman_constructor_exists():
    assert callable(familytree::Woman.__init__)


def test_familytree::woman_constructor_args():
    sig = inspect.signature(familytree::Woman.__init__)
    params = list(sig.parameters.keys())



def test_familytree::familytree_is_not_abstract():
    assert not inspect.isabstract(familytree::FamilyTree)


def test_familytree::familytree_constructor_exists():
    assert callable(familytree::FamilyTree.__init__)


def test_familytree::familytree_constructor_args():
    sig = inspect.signature(familytree::FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_familytree::person_is_not_abstract():
    assert not inspect.isabstract(familytree::Person)


def test_familytree::person_constructor_exists():
    assert callable(familytree::Person.__init__)


def test_familytree::person_constructor_args():
    sig = inspect.signature(familytree::Person.__init__)
    params = list(sig.parameters.keys())
    assert "died" in params, "Missing parameter 'died'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "imagePaths" in params, "Missing parameter 'imagePaths'"
    assert "nameOfBirth" in params, "Missing parameter 'nameOfBirth'"
    assert "relationshipStatus" in params, "Missing parameter 'relationshipStatus'"
    assert "secondName" in params, "Missing parameter 'secondName'"
    assert "dayOfDeath" in params, "Missing parameter 'dayOfDeath'"
    assert "locationOfBirth" in params, "Missing parameter 'locationOfBirth'"
    assert "dayOfBirth" in params, "Missing parameter 'dayOfBirth'"

def test_familytree::person_has_died():
    assert hasattr(familytree::Person, "died")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "died" in klass.__dict__:
            descriptor = klass.__dict__["died"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_firstName():
    assert hasattr(familytree::Person, "firstName")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_imagePaths():
    assert hasattr(familytree::Person, "imagePaths")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "imagePaths" in klass.__dict__:
            descriptor = klass.__dict__["imagePaths"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_nameOfBirth():
    assert hasattr(familytree::Person, "nameOfBirth")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "nameOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["nameOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_relationshipStatus():
    assert hasattr(familytree::Person, "relationshipStatus")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "relationshipStatus" in klass.__dict__:
            descriptor = klass.__dict__["relationshipStatus"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_secondName():
    assert hasattr(familytree::Person, "secondName")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "secondName" in klass.__dict__:
            descriptor = klass.__dict__["secondName"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_dayOfDeath():
    assert hasattr(familytree::Person, "dayOfDeath")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "dayOfDeath" in klass.__dict__:
            descriptor = klass.__dict__["dayOfDeath"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_locationOfBirth():
    assert hasattr(familytree::Person, "locationOfBirth")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "locationOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["locationOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_familytree::person_has_dayOfBirth():
    assert hasattr(familytree::Person, "dayOfBirth")
    descriptor = None
    for klass in familytree::Person.__mro__:
        if "dayOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dayOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_relationshipstatus_exists():
    # Check that the Enumeration exists
    assert RelationshipStatus is not None

def test_relationshipstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipStatus]
    expected_literals = [
        "Married",
        "Widowed",
        "Liaised",
        "Single",
        "Divorced",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipStatus"


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
familytree::Man_strategy = st.builds(
    familytree::Man,
)
familytree::Woman_strategy = st.builds(
    familytree::Woman,
)
familytree::FamilyTree_strategy = st.builds(
    familytree::FamilyTree,
)
familytree::Person_strategy = st.builds(
    familytree::Person,
    died=
        st.booleans(),
    firstName=
        safe_text,
    imagePaths=
        safe_text,
    nameOfBirth=
        safe_text,
    relationshipStatus=
        safe_text,
    secondName=
        safe_text,
    dayOfDeath=
        st.dates(),
    locationOfBirth=
        safe_text,
    dayOfBirth=
        st.dates()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familytree::Man_strategy)
@settings(max_examples=50)
def test_familytree::man_instantiation(instance):
    assert isinstance(instance, familytree::Man)

@given(instance=familytree::Woman_strategy)
@settings(max_examples=50)
def test_familytree::woman_instantiation(instance):
    assert isinstance(instance, familytree::Woman)

@given(instance=familytree::FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree::familytree_instantiation(instance):
    assert isinstance(instance, familytree::FamilyTree)

@given(instance=familytree::Person_strategy)
@settings(max_examples=50)
def test_familytree::person_instantiation(instance):
    assert isinstance(instance, familytree::Person)

@given(instance=familytree::Person_strategy)
def test_familytree::person_died_type(instance):
    assert isinstance(instance.died, bool)


@given(instance=familytree::Person_strategy)
def test_familytree::person_died_setter(instance):
    original = instance.died
    instance.died = original
    assert instance.died == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_imagePaths_type(instance):
    assert isinstance(instance.imagePaths, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_imagePaths_setter(instance):
    original = instance.imagePaths
    instance.imagePaths = original
    assert instance.imagePaths == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_nameOfBirth_type(instance):
    assert isinstance(instance.nameOfBirth, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_nameOfBirth_setter(instance):
    original = instance.nameOfBirth
    instance.nameOfBirth = original
    assert instance.nameOfBirth == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_relationshipStatus_type(instance):
    assert isinstance(instance.relationshipStatus, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_relationshipStatus_setter(instance):
    original = instance.relationshipStatus
    instance.relationshipStatus = original
    assert instance.relationshipStatus == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_secondName_type(instance):
    assert isinstance(instance.secondName, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_secondName_setter(instance):
    original = instance.secondName
    instance.secondName = original
    assert instance.secondName == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_dayOfDeath_type(instance):
    assert isinstance(instance.dayOfDeath, date)


@given(instance=familytree::Person_strategy)
def test_familytree::person_dayOfDeath_setter(instance):
    original = instance.dayOfDeath
    instance.dayOfDeath = original
    assert instance.dayOfDeath == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_locationOfBirth_type(instance):
    assert isinstance(instance.locationOfBirth, str)


@given(instance=familytree::Person_strategy)
def test_familytree::person_locationOfBirth_setter(instance):
    original = instance.locationOfBirth
    instance.locationOfBirth = original
    assert instance.locationOfBirth == original

@given(instance=familytree::Person_strategy)
def test_familytree::person_dayOfBirth_type(instance):
    assert isinstance(instance.dayOfBirth, date)


@given(instance=familytree::Person_strategy)
def test_familytree::person_dayOfBirth_setter(instance):
    original = instance.dayOfBirth
    instance.dayOfBirth = original
    assert instance.dayOfBirth == original
