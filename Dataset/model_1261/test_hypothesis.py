import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Family,
    family::WealthyFamily,
    family::Family,
    family::Car,
    family::Address,
    family::Person,
    Sexe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_is_not_abstract():
    assert not inspect.isabstract(Family)


def test_family_constructor_exists():
    assert callable(Family.__init__)


def test_family_constructor_args():
    sig = inspect.signature(Family.__init__)
    params = list(sig.parameters.keys())



def test_family::wealthyfamily_is_not_abstract():
    assert not inspect.isabstract(family::WealthyFamily)


def test_family::wealthyfamily_constructor_exists():
    assert callable(family::WealthyFamily.__init__)


def test_family::wealthyfamily_constructor_args():
    sig = inspect.signature(family::WealthyFamily.__init__)
    params = list(sig.parameters.keys())
    assert "forbesRanking" in params, "Missing parameter 'forbesRanking'"

def test_family::wealthyfamily_has_forbesRanking():
    assert hasattr(family::WealthyFamily, "forbesRanking")
    descriptor = None
    for klass in family::WealthyFamily.__mro__:
        if "forbesRanking" in klass.__dict__:
            descriptor = klass.__dict__["forbesRanking"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "favoriteHolidayDestinations" in params, "Missing parameter 'favoriteHolidayDestinations'"
    assert "hasASwimmingPool" in params, "Missing parameter 'hasASwimmingPool'"
    assert "numberOfPets" in params, "Missing parameter 'numberOfPets'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_family::family_has_favoriteHolidayDestinations():
    assert hasattr(family::Family, "favoriteHolidayDestinations")
    descriptor = None
    for klass in family::Family.__mro__:
        if "favoriteHolidayDestinations" in klass.__dict__:
            descriptor = klass.__dict__["favoriteHolidayDestinations"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_hasASwimmingPool():
    assert hasattr(family::Family, "hasASwimmingPool")
    descriptor = None
    for klass in family::Family.__mro__:
        if "hasASwimmingPool" in klass.__dict__:
            descriptor = klass.__dict__["hasASwimmingPool"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_numberOfPets():
    assert hasattr(family::Family, "numberOfPets")
    descriptor = None
    for klass in family::Family.__mro__:
        if "numberOfPets" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPets"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_surname():
    assert hasattr(family::Family, "surname")
    descriptor = None
    for klass in family::Family.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_family::car_is_not_abstract():
    assert not inspect.isabstract(family::Car)


def test_family::car_constructor_exists():
    assert callable(family::Car.__init__)


def test_family::car_constructor_args():
    sig = inspect.signature(family::Car.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"

def test_family::car_has_numberOfSeats():
    assert hasattr(family::Car, "numberOfSeats")
    descriptor = None
    for klass in family::Car.__mro__:
        if "numberOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_family::address_is_not_abstract():
    assert not inspect.isabstract(family::Address)


def test_family::address_constructor_exists():
    assert callable(family::Address.__init__)


def test_family::address_constructor_args():
    sig = inspect.signature(family::Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"

def test_family::address_has_street():
    assert hasattr(family::Address, "street")
    descriptor = None
    for klass in family::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "sexe" in params, "Missing parameter 'sexe'"

def test_family::person_has_firstName():
    assert hasattr(family::Person, "firstName")
    descriptor = None
    for klass in family::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_sexe():
    assert hasattr(family::Person, "sexe")
    descriptor = None
    for klass in family::Person.__mro__:
        if "sexe" in klass.__dict__:
            descriptor = klass.__dict__["sexe"]
            break
    assert isinstance(descriptor, property)

def test_sexe_exists():
    # Check that the Enumeration exists
    assert Sexe is not None

def test_sexe_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sexe]
    expected_literals = [
        "FEMALE",
        "MALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sexe"


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
Family_strategy = st.builds(
    Family,
)
family::WealthyFamily_strategy = st.builds(
    family::WealthyFamily,
    forbesRanking=
        st.integers()
)
family::Family_strategy = st.builds(
    family::Family,
    favoriteHolidayDestinations=
        safe_text,
    hasASwimmingPool=
        st.booleans(),
    numberOfPets=
        st.integers(),
    surname=
        safe_text
)
family::Car_strategy = st.builds(
    family::Car,
    numberOfSeats=
        safe_text
)
family::Address_strategy = st.builds(
    family::Address,
    street=
        safe_text
)
family::Person_strategy = st.builds(
    family::Person,
    firstName=
        safe_text,
    sexe=
        safe_text
)

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

@given(instance=family::WealthyFamily_strategy)
@settings(max_examples=50)
def test_family::wealthyfamily_instantiation(instance):
    assert isinstance(instance, family::WealthyFamily)

@given(instance=family::WealthyFamily_strategy)
def test_family::wealthyfamily_forbesRanking_type(instance):
    assert isinstance(instance.forbesRanking, int)


@given(instance=family::WealthyFamily_strategy)
def test_family::wealthyfamily_forbesRanking_setter(instance):
    original = instance.forbesRanking
    instance.forbesRanking = original
    assert instance.forbesRanking == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_favoriteHolidayDestinations_type(instance):
    assert isinstance(instance.favoriteHolidayDestinations, str)


@given(instance=family::Family_strategy)
def test_family::family_favoriteHolidayDestinations_setter(instance):
    original = instance.favoriteHolidayDestinations
    instance.favoriteHolidayDestinations = original
    assert instance.favoriteHolidayDestinations == original

@given(instance=family::Family_strategy)
def test_family::family_hasASwimmingPool_type(instance):
    assert isinstance(instance.hasASwimmingPool, bool)


@given(instance=family::Family_strategy)
def test_family::family_hasASwimmingPool_setter(instance):
    original = instance.hasASwimmingPool
    instance.hasASwimmingPool = original
    assert instance.hasASwimmingPool == original

@given(instance=family::Family_strategy)
def test_family::family_numberOfPets_type(instance):
    assert isinstance(instance.numberOfPets, int)


@given(instance=family::Family_strategy)
def test_family::family_numberOfPets_setter(instance):
    original = instance.numberOfPets
    instance.numberOfPets = original
    assert instance.numberOfPets == original

@given(instance=family::Family_strategy)
def test_family::family_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=family::Family_strategy)
def test_family::family_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=family::Car_strategy)
@settings(max_examples=50)
def test_family::car_instantiation(instance):
    assert isinstance(instance, family::Car)

@given(instance=family::Car_strategy)
def test_family::car_numberOfSeats_type(instance):
    assert isinstance(instance.numberOfSeats, str)


@given(instance=family::Car_strategy)
def test_family::car_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original

@given(instance=family::Address_strategy)
@settings(max_examples=50)
def test_family::address_instantiation(instance):
    assert isinstance(instance, family::Address)

@given(instance=family::Address_strategy)
def test_family::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=family::Address_strategy)
def test_family::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=family::Person_strategy)
def test_family::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=family::Person_strategy)
def test_family::person_sexe_type(instance):
    assert isinstance(instance.sexe, str)


@given(instance=family::Person_strategy)
def test_family::person_sexe_setter(instance):
    original = instance.sexe
    instance.sexe = original
    assert instance.sexe == original
