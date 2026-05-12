import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Family,
    family_WealthyFamily,
    family_Family,
    family_Car,
    family_Address,
    family_Person,
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



def test_family_wealthyfamily_is_not_abstract():
    assert not inspect.isabstract(family_WealthyFamily)


def test_family_wealthyfamily_constructor_exists():
    assert callable(family_WealthyFamily.__init__)


def test_family_wealthyfamily_constructor_args():
    sig = inspect.signature(family_WealthyFamily.__init__)
    params = list(sig.parameters.keys())
    assert "forbesRanking" in params, "Missing parameter 'forbesRanking'"

def test_family_wealthyfamily_has_forbesRanking():
    assert hasattr(family_WealthyFamily, "forbesRanking")
    descriptor = None
    for klass in family_WealthyFamily.__mro__:
        if "forbesRanking" in klass.__dict__:
            descriptor = klass.__dict__["forbesRanking"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "surname" in params, "Missing parameter 'surname'"
    assert "numberOfPets" in params, "Missing parameter 'numberOfPets'"
    assert "favoriteHolidayDestinations" in params, "Missing parameter 'favoriteHolidayDestinations'"
    assert "hasASwimmingPool" in params, "Missing parameter 'hasASwimmingPool'"

def test_family_family_has_surname():
    assert hasattr(family_Family, "surname")
    descriptor = None
    for klass in family_Family.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_numberOfPets():
    assert hasattr(family_Family, "numberOfPets")
    descriptor = None
    for klass in family_Family.__mro__:
        if "numberOfPets" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPets"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_favoriteHolidayDestinations():
    assert hasattr(family_Family, "favoriteHolidayDestinations")
    descriptor = None
    for klass in family_Family.__mro__:
        if "favoriteHolidayDestinations" in klass.__dict__:
            descriptor = klass.__dict__["favoriteHolidayDestinations"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_hasASwimmingPool():
    assert hasattr(family_Family, "hasASwimmingPool")
    descriptor = None
    for klass in family_Family.__mro__:
        if "hasASwimmingPool" in klass.__dict__:
            descriptor = klass.__dict__["hasASwimmingPool"]
            break
    assert isinstance(descriptor, property)



def test_family_car_is_not_abstract():
    assert not inspect.isabstract(family_Car)


def test_family_car_constructor_exists():
    assert callable(family_Car.__init__)


def test_family_car_constructor_args():
    sig = inspect.signature(family_Car.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"

def test_family_car_has_numberOfSeats():
    assert hasattr(family_Car, "numberOfSeats")
    descriptor = None
    for klass in family_Car.__mro__:
        if "numberOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_family_address_is_not_abstract():
    assert not inspect.isabstract(family_Address)


def test_family_address_constructor_exists():
    assert callable(family_Address.__init__)


def test_family_address_constructor_args():
    sig = inspect.signature(family_Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"

def test_family_address_has_street():
    assert hasattr(family_Address, "street")
    descriptor = None
    for klass in family_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "sexe" in params, "Missing parameter 'sexe'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_family_person_has_sexe():
    assert hasattr(family_Person, "sexe")
    descriptor = None
    for klass in family_Person.__mro__:
        if "sexe" in klass.__dict__:
            descriptor = klass.__dict__["sexe"]
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

def test_sexe_exists():
    # Check that the Enumeration exists
    assert Sexe is not None

def test_sexe_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sexe]
    expected_literals = [
        "MALE",
        "FEMALE",
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
family_WealthyFamily_strategy = st.builds(
    family_WealthyFamily,
    forbesRanking=
        st.integers()
)
family_Family_strategy = st.builds(
    family_Family,
    surname=
        safe_text,
    numberOfPets=
        st.integers(),
    favoriteHolidayDestinations=
        safe_text,
    hasASwimmingPool=
        st.booleans()
)
family_Car_strategy = st.builds(
    family_Car,
    numberOfSeats=
        safe_text
)
family_Address_strategy = st.builds(
    family_Address,
    street=
        safe_text
)
family_Person_strategy = st.builds(
    family_Person,
    sexe=
        safe_text,
    firstName=
        safe_text
)

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

@given(instance=family_WealthyFamily_strategy)
@settings(max_examples=50)
def test_family_wealthyfamily_instantiation(instance):
    assert isinstance(instance, family_WealthyFamily)



@given(instance=family_WealthyFamily_strategy)
def test_family_wealthyfamily_forbesRanking_setter(instance):
    original = instance.forbesRanking
    instance.forbesRanking = original
    assert instance.forbesRanking == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=family_Family_strategy)
def test_family_family_numberOfPets_setter(instance):
    original = instance.numberOfPets
    instance.numberOfPets = original
    assert instance.numberOfPets == original



@given(instance=family_Family_strategy)
def test_family_family_favoriteHolidayDestinations_setter(instance):
    original = instance.favoriteHolidayDestinations
    instance.favoriteHolidayDestinations = original
    assert instance.favoriteHolidayDestinations == original



@given(instance=family_Family_strategy)
def test_family_family_hasASwimmingPool_setter(instance):
    original = instance.hasASwimmingPool
    instance.hasASwimmingPool = original
    assert instance.hasASwimmingPool == original

@given(instance=family_Car_strategy)
@settings(max_examples=50)
def test_family_car_instantiation(instance):
    assert isinstance(instance, family_Car)



@given(instance=family_Car_strategy)
def test_family_car_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original

@given(instance=family_Address_strategy)
@settings(max_examples=50)
def test_family_address_instantiation(instance):
    assert isinstance(instance, family_Address)



@given(instance=family_Address_strategy)
def test_family_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_sexe_setter(instance):
    original = instance.sexe
    instance.sexe = original
    assert instance.sexe == original



@given(instance=family_Person_strategy)
def test_family_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
