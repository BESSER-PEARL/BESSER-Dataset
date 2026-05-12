import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    familytree_Man,
    familytree_Woman,
    familytree_FamilyTree,
    familytree_Person,
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



def test_familytree_man_is_not_abstract():
    assert not inspect.isabstract(familytree_Man)


def test_familytree_man_constructor_exists():
    assert callable(familytree_Man.__init__)


def test_familytree_man_constructor_args():
    sig = inspect.signature(familytree_Man.__init__)
    params = list(sig.parameters.keys())



def test_familytree_woman_is_not_abstract():
    assert not inspect.isabstract(familytree_Woman)


def test_familytree_woman_constructor_exists():
    assert callable(familytree_Woman.__init__)


def test_familytree_woman_constructor_args():
    sig = inspect.signature(familytree_Woman.__init__)
    params = list(sig.parameters.keys())



def test_familytree_familytree_is_not_abstract():
    assert not inspect.isabstract(familytree_FamilyTree)


def test_familytree_familytree_constructor_exists():
    assert callable(familytree_FamilyTree.__init__)


def test_familytree_familytree_constructor_args():
    sig = inspect.signature(familytree_FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_familytree_person_is_not_abstract():
    assert not inspect.isabstract(familytree_Person)


def test_familytree_person_constructor_exists():
    assert callable(familytree_Person.__init__)


def test_familytree_person_constructor_args():
    sig = inspect.signature(familytree_Person.__init__)
    params = list(sig.parameters.keys())
    assert "nameOfBirth" in params, "Missing parameter 'nameOfBirth'"
    assert "died" in params, "Missing parameter 'died'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "imagePaths" in params, "Missing parameter 'imagePaths'"
    assert "dayOfDeath" in params, "Missing parameter 'dayOfDeath'"
    assert "locationOfBirth" in params, "Missing parameter 'locationOfBirth'"
    assert "relationshipStatus" in params, "Missing parameter 'relationshipStatus'"
    assert "secondName" in params, "Missing parameter 'secondName'"
    assert "dayOfBirth" in params, "Missing parameter 'dayOfBirth'"

def test_familytree_person_has_nameOfBirth():
    assert hasattr(familytree_Person, "nameOfBirth")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "nameOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["nameOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_died():
    assert hasattr(familytree_Person, "died")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "died" in klass.__dict__:
            descriptor = klass.__dict__["died"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_firstName():
    assert hasattr(familytree_Person, "firstName")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_imagePaths():
    assert hasattr(familytree_Person, "imagePaths")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "imagePaths" in klass.__dict__:
            descriptor = klass.__dict__["imagePaths"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_dayOfDeath():
    assert hasattr(familytree_Person, "dayOfDeath")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "dayOfDeath" in klass.__dict__:
            descriptor = klass.__dict__["dayOfDeath"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_locationOfBirth():
    assert hasattr(familytree_Person, "locationOfBirth")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "locationOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["locationOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_relationshipStatus():
    assert hasattr(familytree_Person, "relationshipStatus")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "relationshipStatus" in klass.__dict__:
            descriptor = klass.__dict__["relationshipStatus"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_secondName():
    assert hasattr(familytree_Person, "secondName")
    descriptor = None
    for klass in familytree_Person.__mro__:
        if "secondName" in klass.__dict__:
            descriptor = klass.__dict__["secondName"]
            break
    assert isinstance(descriptor, property)

def test_familytree_person_has_dayOfBirth():
    assert hasattr(familytree_Person, "dayOfBirth")
    descriptor = None
    for klass in familytree_Person.__mro__:
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
        "Divorced",
        "Liaised",
        "Widowed",
        "Married",
        "Single",
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
familytree_Man_strategy = st.builds(
    familytree_Man,
)
familytree_Woman_strategy = st.builds(
    familytree_Woman,
)
familytree_FamilyTree_strategy = st.builds(
    familytree_FamilyTree,
)
familytree_Person_strategy = st.builds(
    familytree_Person,
    nameOfBirth=
        safe_text,
    died=
        st.booleans(),
    firstName=
        safe_text,
    imagePaths=
        safe_text,
    dayOfDeath=
        st.dates(),
    locationOfBirth=
        safe_text,
    relationshipStatus=
        safe_text,
    secondName=
        safe_text,
    dayOfBirth=
        st.dates()
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familytree_Man_strategy)
@settings(max_examples=50)
def test_familytree_man_instantiation(instance):
    assert isinstance(instance, familytree_Man)

@given(instance=familytree_Woman_strategy)
@settings(max_examples=50)
def test_familytree_woman_instantiation(instance):
    assert isinstance(instance, familytree_Woman)

@given(instance=familytree_FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree_familytree_instantiation(instance):
    assert isinstance(instance, familytree_FamilyTree)

@given(instance=familytree_Person_strategy)
@settings(max_examples=50)
def test_familytree_person_instantiation(instance):
    assert isinstance(instance, familytree_Person)



@given(instance=familytree_Person_strategy)
def test_familytree_person_nameOfBirth_setter(instance):
    original = instance.nameOfBirth
    instance.nameOfBirth = original
    assert instance.nameOfBirth == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_died_setter(instance):
    original = instance.died
    instance.died = original
    assert instance.died == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_imagePaths_setter(instance):
    original = instance.imagePaths
    instance.imagePaths = original
    assert instance.imagePaths == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_dayOfDeath_setter(instance):
    original = instance.dayOfDeath
    instance.dayOfDeath = original
    assert instance.dayOfDeath == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_locationOfBirth_setter(instance):
    original = instance.locationOfBirth
    instance.locationOfBirth = original
    assert instance.locationOfBirth == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_relationshipStatus_setter(instance):
    original = instance.relationshipStatus
    instance.relationshipStatus = original
    assert instance.relationshipStatus == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_secondName_setter(instance):
    original = instance.secondName
    instance.secondName = original
    assert instance.secondName == original



@given(instance=familytree_Person_strategy)
def test_familytree_person_dayOfBirth_setter(instance):
    original = instance.dayOfBirth
    instance.dayOfBirth = original
    assert instance.dayOfBirth == original
