import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trip_NamedElement,
    NamedElement,
    trip_Person,
    trip_TripModel,
    trip_Vehicle,
    trip_Trip,
    Vehicle,
    trip_Van,
    trip_Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trip_namedelement_is_not_abstract():
    assert not inspect.isabstract(trip_NamedElement)


def test_trip_namedelement_constructor_exists():
    assert callable(trip_NamedElement.__init__)


def test_trip_namedelement_constructor_args():
    sig = inspect.signature(trip_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trip_namedelement_has_name():
    assert hasattr(trip_NamedElement, "name")
    descriptor = None
    for klass in trip_NamedElement.__mro__:
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



def test_trip_person_is_not_abstract():
    assert not inspect.isabstract(trip_Person)


def test_trip_person_constructor_exists():
    assert callable(trip_Person.__init__)


def test_trip_person_constructor_args():
    sig = inspect.signature(trip_Person.__init__)
    params = list(sig.parameters.keys())



def test_trip_tripmodel_is_not_abstract():
    assert not inspect.isabstract(trip_TripModel)


def test_trip_tripmodel_constructor_exists():
    assert callable(trip_TripModel.__init__)


def test_trip_tripmodel_constructor_args():
    sig = inspect.signature(trip_TripModel.__init__)
    params = list(sig.parameters.keys())



def test_trip_vehicle_is_not_abstract():
    assert not inspect.isabstract(trip_Vehicle)


def test_trip_vehicle_constructor_exists():
    assert callable(trip_Vehicle.__init__)


def test_trip_vehicle_constructor_args():
    sig = inspect.signature(trip_Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "nrOfSeats" in params, "Missing parameter 'nrOfSeats'"

def test_trip_vehicle_has_nrOfSeats():
    assert hasattr(trip_Vehicle, "nrOfSeats")
    descriptor = None
    for klass in trip_Vehicle.__mro__:
        if "nrOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["nrOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_trip_trip_is_not_abstract():
    assert not inspect.isabstract(trip_Trip)


def test_trip_trip_constructor_exists():
    assert callable(trip_Trip.__init__)


def test_trip_trip_constructor_args():
    sig = inspect.signature(trip_Trip.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_trip_van_is_not_abstract():
    assert not inspect.isabstract(trip_Van)


def test_trip_van_constructor_exists():
    assert callable(trip_Van.__init__)


def test_trip_van_constructor_args():
    sig = inspect.signature(trip_Van.__init__)
    params = list(sig.parameters.keys())



def test_trip_car_is_not_abstract():
    assert not inspect.isabstract(trip_Car)


def test_trip_car_constructor_exists():
    assert callable(trip_Car.__init__)


def test_trip_car_constructor_args():
    sig = inspect.signature(trip_Car.__init__)
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
trip_NamedElement_strategy = st.builds(
    trip_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
trip_Person_strategy = st.builds(
    trip_Person,
)
trip_TripModel_strategy = st.builds(
    trip_TripModel,
)
trip_Vehicle_strategy = st.builds(
    trip_Vehicle,
    nrOfSeats=
        st.integers()
)
trip_Trip_strategy = st.builds(
    trip_Trip,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
trip_Van_strategy = st.builds(
    trip_Van,
)
trip_Car_strategy = st.builds(
    trip_Car,
)

@given(instance=trip_NamedElement_strategy)
@settings(max_examples=50)
def test_trip_namedelement_instantiation(instance):
    assert isinstance(instance, trip_NamedElement)



@given(instance=trip_NamedElement_strategy)
def test_trip_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=trip_Person_strategy)
@settings(max_examples=50)
def test_trip_person_instantiation(instance):
    assert isinstance(instance, trip_Person)

@given(instance=trip_TripModel_strategy)
@settings(max_examples=50)
def test_trip_tripmodel_instantiation(instance):
    assert isinstance(instance, trip_TripModel)

@given(instance=trip_Vehicle_strategy)
@settings(max_examples=50)
def test_trip_vehicle_instantiation(instance):
    assert isinstance(instance, trip_Vehicle)



@given(instance=trip_Vehicle_strategy)
def test_trip_vehicle_nrOfSeats_setter(instance):
    original = instance.nrOfSeats
    instance.nrOfSeats = original
    assert instance.nrOfSeats == original

@given(instance=trip_Trip_strategy)
@settings(max_examples=50)
def test_trip_trip_instantiation(instance):
    assert isinstance(instance, trip_Trip)

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=trip_Van_strategy)
@settings(max_examples=50)
def test_trip_van_instantiation(instance):
    assert isinstance(instance, trip_Van)

@given(instance=trip_Car_strategy)
@settings(max_examples=50)
def test_trip_car_instantiation(instance):
    assert isinstance(instance, trip_Car)
