import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trip::NamedElement,
    NamedElement,
    trip::TripModel,
    trip::Person,
    trip::Vehicle,
    trip::Trip,
    Vehicle,
    trip::Van,
    trip::Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trip::namedelement_is_not_abstract():
    assert not inspect.isabstract(trip::NamedElement)


def test_trip::namedelement_constructor_exists():
    assert callable(trip::NamedElement.__init__)


def test_trip::namedelement_constructor_args():
    sig = inspect.signature(trip::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trip::namedelement_has_name():
    assert hasattr(trip::NamedElement, "name")
    descriptor = None
    for klass in trip::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_trip::tripmodel_is_not_abstract():
    assert not inspect.isabstract(trip::TripModel)


def test_trip::tripmodel_constructor_exists():
    assert callable(trip::TripModel.__init__)


def test_trip::tripmodel_constructor_args():
    sig = inspect.signature(trip::TripModel.__init__)
    params = list(sig.parameters.keys())



def test_trip::person_is_not_abstract():
    assert not inspect.isabstract(trip::Person)


def test_trip::person_constructor_exists():
    assert callable(trip::Person.__init__)


def test_trip::person_constructor_args():
    sig = inspect.signature(trip::Person.__init__)
    params = list(sig.parameters.keys())



def test_trip::vehicle_is_not_abstract():
    assert not inspect.isabstract(trip::Vehicle)


def test_trip::vehicle_constructor_exists():
    assert callable(trip::Vehicle.__init__)


def test_trip::vehicle_constructor_args():
    sig = inspect.signature(trip::Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "nrOfSeats" in params, "Missing parameter 'nrOfSeats'"

def test_trip::vehicle_has_nrOfSeats():
    assert hasattr(trip::Vehicle, "nrOfSeats")
    descriptor = None
    for klass in trip::Vehicle.__mro__:
        if "nrOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["nrOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_trip::trip_is_not_abstract():
    assert not inspect.isabstract(trip::Trip)


def test_trip::trip_constructor_exists():
    assert callable(trip::Trip.__init__)


def test_trip::trip_constructor_args():
    sig = inspect.signature(trip::Trip.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_trip::van_is_not_abstract():
    assert not inspect.isabstract(trip::Van)


def test_trip::van_constructor_exists():
    assert callable(trip::Van.__init__)


def test_trip::van_constructor_args():
    sig = inspect.signature(trip::Van.__init__)
    params = list(sig.parameters.keys())



def test_trip::car_is_not_abstract():
    assert not inspect.isabstract(trip::Car)


def test_trip::car_constructor_exists():
    assert callable(trip::Car.__init__)


def test_trip::car_constructor_args():
    sig = inspect.signature(trip::Car.__init__)
    params = list(sig.parameters.keys())


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
trip::NamedElement_strategy = st.builds(
    trip::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
trip::TripModel_strategy = st.builds(
    trip::TripModel,
)
trip::Person_strategy = st.builds(
    trip::Person,
)
trip::Vehicle_strategy = st.builds(
    trip::Vehicle,
    nrOfSeats=
        st.integers()
)
trip::Trip_strategy = st.builds(
    trip::Trip,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
trip::Van_strategy = st.builds(
    trip::Van,
)
trip::Car_strategy = st.builds(
    trip::Car,
)

@given(instance=trip::NamedElement_strategy)
@settings(max_examples=50)
def test_trip::namedelement_instantiation(instance):
    assert isinstance(instance, trip::NamedElement)

@given(instance=trip::NamedElement_strategy)
def test_trip::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trip::NamedElement_strategy)
def test_trip::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=trip::TripModel_strategy)
@settings(max_examples=50)
def test_trip::tripmodel_instantiation(instance):
    assert isinstance(instance, trip::TripModel)

@given(instance=trip::Person_strategy)
@settings(max_examples=50)
def test_trip::person_instantiation(instance):
    assert isinstance(instance, trip::Person)

@given(instance=trip::Vehicle_strategy)
@settings(max_examples=50)
def test_trip::vehicle_instantiation(instance):
    assert isinstance(instance, trip::Vehicle)

@given(instance=trip::Vehicle_strategy)
def test_trip::vehicle_nrOfSeats_type(instance):
    assert isinstance(instance.nrOfSeats, int)


@given(instance=trip::Vehicle_strategy)
def test_trip::vehicle_nrOfSeats_setter(instance):
    original = instance.nrOfSeats
    instance.nrOfSeats = original
    assert instance.nrOfSeats == original

@given(instance=trip::Trip_strategy)
@settings(max_examples=50)
def test_trip::trip_instantiation(instance):
    assert isinstance(instance, trip::Trip)

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=trip::Van_strategy)
@settings(max_examples=50)
def test_trip::van_instantiation(instance):
    assert isinstance(instance, trip::Van)

@given(instance=trip::Car_strategy)
@settings(max_examples=50)
def test_trip::car_instantiation(instance):
    assert isinstance(instance, trip::Car)
