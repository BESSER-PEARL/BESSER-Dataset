import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    family::Woman,
    family::Man,
    EModelElement,
    family::Person,
    family::Family,
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



def test_family::woman_is_not_abstract():
    assert not inspect.isabstract(family::Woman)


def test_family::woman_constructor_exists():
    assert callable(family::Woman.__init__)


def test_family::woman_constructor_args():
    sig = inspect.signature(family::Woman.__init__)
    params = list(sig.parameters.keys())



def test_family::man_is_not_abstract():
    assert not inspect.isabstract(family::Man)


def test_family::man_constructor_exists():
    assert callable(family::Man.__init__)


def test_family::man_constructor_args():
    sig = inspect.signature(family::Man.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthDay" in params, "Missing parameter 'birthDay'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthMonth" in params, "Missing parameter 'birthMonth'"
    assert "birthYear" in params, "Missing parameter 'birthYear'"
    assert "birthCity" in params, "Missing parameter 'birthCity'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_family::person_has_birthDay():
    assert hasattr(family::Person, "birthDay")
    descriptor = None
    for klass in family::Person.__mro__:
        if "birthDay" in klass.__dict__:
            descriptor = klass.__dict__["birthDay"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_lastName():
    assert hasattr(family::Person, "lastName")
    descriptor = None
    for klass in family::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_birthMonth():
    assert hasattr(family::Person, "birthMonth")
    descriptor = None
    for klass in family::Person.__mro__:
        if "birthMonth" in klass.__dict__:
            descriptor = klass.__dict__["birthMonth"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_birthYear():
    assert hasattr(family::Person, "birthYear")
    descriptor = None
    for klass in family::Person.__mro__:
        if "birthYear" in klass.__dict__:
            descriptor = klass.__dict__["birthYear"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_birthCity():
    assert hasattr(family::Person, "birthCity")
    descriptor = None
    for klass in family::Person.__mro__:
        if "birthCity" in klass.__dict__:
            descriptor = klass.__dict__["birthCity"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_firstName():
    assert hasattr(family::Person, "firstName")
    descriptor = None
    for klass in family::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::family_has_name():
    assert hasattr(family::Family, "name")
    descriptor = None
    for klass in family::Family.__mro__:
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
        "April",
        "March",
        "September",
        "October",
        "November",
        "February",
        "July",
        "January",
        "May",
        "August",
        "December",
        "June",
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
family::Woman_strategy = st.builds(
    family::Woman,
)
family::Man_strategy = st.builds(
    family::Man,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
family::Person_strategy = st.builds(
    family::Person,
    birthDay=
        st.integers(),
    lastName=
        safe_text,
    birthMonth=
        safe_text,
    birthYear=
        st.integers(),
    birthCity=
        safe_text,
    firstName=
        safe_text
)
family::Family_strategy = st.builds(
    family::Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family::Woman_strategy)
@settings(max_examples=50)
def test_family::woman_instantiation(instance):
    assert isinstance(instance, family::Woman)

@given(instance=family::Man_strategy)
@settings(max_examples=50)
def test_family::man_instantiation(instance):
    assert isinstance(instance, family::Man)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_birthDay_type(instance):
    assert isinstance(instance.birthDay, int)


@given(instance=family::Person_strategy)
def test_family::person_birthDay_setter(instance):
    original = instance.birthDay
    instance.birthDay = original
    assert instance.birthDay == original

@given(instance=family::Person_strategy)
def test_family::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=family::Person_strategy)
def test_family::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=family::Person_strategy)
def test_family::person_birthMonth_type(instance):
    assert isinstance(instance.birthMonth, str)


@given(instance=family::Person_strategy)
def test_family::person_birthMonth_setter(instance):
    original = instance.birthMonth
    instance.birthMonth = original
    assert instance.birthMonth == original

@given(instance=family::Person_strategy)
def test_family::person_birthYear_type(instance):
    assert isinstance(instance.birthYear, int)


@given(instance=family::Person_strategy)
def test_family::person_birthYear_setter(instance):
    original = instance.birthYear
    instance.birthYear = original
    assert instance.birthYear == original

@given(instance=family::Person_strategy)
def test_family::person_birthCity_type(instance):
    assert isinstance(instance.birthCity, str)


@given(instance=family::Person_strategy)
def test_family::person_birthCity_setter(instance):
    original = instance.birthCity
    instance.birthCity = original
    assert instance.birthCity == original

@given(instance=family::Person_strategy)
def test_family::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=family::Person_strategy)
def test_family::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Family_strategy)
def test_family::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
