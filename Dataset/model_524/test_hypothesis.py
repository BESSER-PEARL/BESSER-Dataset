import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    family_Woman,
    family_Man,
    EModelElement,
    family_Person,
    family_Family,
    Month,
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



def test_family_woman_is_not_abstract():
    assert not inspect.isabstract(family_Woman)


def test_family_woman_constructor_exists():
    assert callable(family_Woman.__init__)


def test_family_woman_constructor_args():
    sig = inspect.signature(family_Woman.__init__)
    params = list(sig.parameters.keys())



def test_family_man_is_not_abstract():
    assert not inspect.isabstract(family_Man)


def test_family_man_constructor_exists():
    assert callable(family_Man.__init__)


def test_family_man_constructor_args():
    sig = inspect.signature(family_Man.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthYear" in params, "Missing parameter 'birthYear'"
    assert "birthCity" in params, "Missing parameter 'birthCity'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "birthMonth" in params, "Missing parameter 'birthMonth'"
    assert "birthDay" in params, "Missing parameter 'birthDay'"

def test_family_person_has_lastName():
    assert hasattr(family_Person, "lastName")
    descriptor = None
    for klass in family_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_birthYear():
    assert hasattr(family_Person, "birthYear")
    descriptor = None
    for klass in family_Person.__mro__:
        if "birthYear" in klass.__dict__:
            descriptor = klass.__dict__["birthYear"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_birthCity():
    assert hasattr(family_Person, "birthCity")
    descriptor = None
    for klass in family_Person.__mro__:
        if "birthCity" in klass.__dict__:
            descriptor = klass.__dict__["birthCity"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_firstName():
    assert hasattr(family_Person, "firstName")
    descriptor = None
    for klass in family_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_birthMonth():
    assert hasattr(family_Person, "birthMonth")
    descriptor = None
    for klass in family_Person.__mro__:
        if "birthMonth" in klass.__dict__:
            descriptor = klass.__dict__["birthMonth"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_birthDay():
    assert hasattr(family_Person, "birthDay")
    descriptor = None
    for klass in family_Person.__mro__:
        if "birthDay" in klass.__dict__:
            descriptor = klass.__dict__["birthDay"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_family_has_name():
    assert hasattr(family_Family, "name")
    descriptor = None
    for klass in family_Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_month_exists():
    # Check that the Enumeration exists
    assert Month is not None

def test_month_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Month]
    expected_literals = [
        "March",
        "April",
        "July",
        "October",
        "November",
        "May",
        "January",
        "September",
        "February",
        "June",
        "August",
        "December",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Month"


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
family_Woman_strategy = st.builds(
    family_Woman,
)
family_Man_strategy = st.builds(
    family_Man,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
family_Person_strategy = st.builds(
    family_Person,
    lastName=
        safe_text,
    birthYear=
        st.integers(),
    birthCity=
        safe_text,
    firstName=
        safe_text,
    birthMonth=
        safe_text,
    birthDay=
        st.integers()
)
family_Family_strategy = st.builds(
    family_Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family_Woman_strategy)
@settings(max_examples=50)
def test_family_woman_instantiation(instance):
    assert isinstance(instance, family_Woman)

@given(instance=family_Man_strategy)
@settings(max_examples=50)
def test_family_man_instantiation(instance):
    assert isinstance(instance, family_Man)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=family_Person_strategy)
def test_family_person_birthYear_setter(instance):
    original = instance.birthYear
    instance.birthYear = original
    assert instance.birthYear == original



@given(instance=family_Person_strategy)
def test_family_person_birthCity_setter(instance):
    original = instance.birthCity
    instance.birthCity = original
    assert instance.birthCity == original



@given(instance=family_Person_strategy)
def test_family_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=family_Person_strategy)
def test_family_person_birthMonth_setter(instance):
    original = instance.birthMonth
    instance.birthMonth = original
    assert instance.birthMonth == original



@given(instance=family_Person_strategy)
def test_family_person_birthDay_setter(instance):
    original = instance.birthDay
    instance.birthDay = original
    assert instance.birthDay == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
