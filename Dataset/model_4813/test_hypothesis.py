import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trip::model::TripModel,
    trip::model::Trip,
    trip::model::location,
    trip::model::Service,
    Service,
    trip::model::TravelService,
    trip::model::OtherService,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trip::model::tripmodel_is_not_abstract():
    assert not inspect.isabstract(trip::model::TripModel)


def test_trip::model::tripmodel_constructor_exists():
    assert callable(trip::model::TripModel.__init__)


def test_trip::model::tripmodel_constructor_args():
    sig = inspect.signature(trip::model::TripModel.__init__)
    params = list(sig.parameters.keys())



def test_trip::model::trip_is_not_abstract():
    assert not inspect.isabstract(trip::model::Trip)


def test_trip::model::trip_constructor_exists():
    assert callable(trip::model::Trip.__init__)


def test_trip::model::trip_constructor_args():
    sig = inspect.signature(trip::model::Trip.__init__)
    params = list(sig.parameters.keys())
    assert "Start" in params, "Missing parameter 'Start'"
    assert "End" in params, "Missing parameter 'End'"
    assert "name" in params, "Missing parameter 'name'"

def test_trip::model::trip_has_Start():
    assert hasattr(trip::model::Trip, "Start")
    descriptor = None
    for klass in trip::model::Trip.__mro__:
        if "Start" in klass.__dict__:
            descriptor = klass.__dict__["Start"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::trip_has_End():
    assert hasattr(trip::model::Trip, "End")
    descriptor = None
    for klass in trip::model::Trip.__mro__:
        if "End" in klass.__dict__:
            descriptor = klass.__dict__["End"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::trip_has_name():
    assert hasattr(trip::model::Trip, "name")
    descriptor = None
    for klass in trip::model::Trip.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trip::model::location_is_not_abstract():
    assert not inspect.isabstract(trip::model::location)


def test_trip::model::location_constructor_exists():
    assert callable(trip::model::location.__init__)


def test_trip::model::location_constructor_args():
    sig = inspect.signature(trip::model::location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trip::model::location_has_name():
    assert hasattr(trip::model::location, "name")
    descriptor = None
    for klass in trip::model::location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trip::model::service_is_not_abstract():
    assert not inspect.isabstract(trip::model::Service)


def test_trip::model::service_constructor_exists():
    assert callable(trip::model::Service.__init__)


def test_trip::model::service_constructor_args():
    sig = inspect.signature(trip::model::Service.__init__)
    params = list(sig.parameters.keys())
    assert "Cost" in params, "Missing parameter 'Cost'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Duration" in params, "Missing parameter 'Duration'"
    assert "Rating" in params, "Missing parameter 'Rating'"

def test_trip::model::service_has_Cost():
    assert hasattr(trip::model::Service, "Cost")
    descriptor = None
    for klass in trip::model::Service.__mro__:
        if "Cost" in klass.__dict__:
            descriptor = klass.__dict__["Cost"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::service_has_Type():
    assert hasattr(trip::model::Service, "Type")
    descriptor = None
    for klass in trip::model::Service.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::service_has_name():
    assert hasattr(trip::model::Service, "name")
    descriptor = None
    for klass in trip::model::Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::service_has_Duration():
    assert hasattr(trip::model::Service, "Duration")
    descriptor = None
    for klass in trip::model::Service.__mro__:
        if "Duration" in klass.__dict__:
            descriptor = klass.__dict__["Duration"]
            break
    assert isinstance(descriptor, property)

def test_trip::model::service_has_Rating():
    assert hasattr(trip::model::Service, "Rating")
    descriptor = None
    for klass in trip::model::Service.__mro__:
        if "Rating" in klass.__dict__:
            descriptor = klass.__dict__["Rating"]
            break
    assert isinstance(descriptor, property)



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_trip::model::travelservice_is_not_abstract():
    assert not inspect.isabstract(trip::model::TravelService)


def test_trip::model::travelservice_constructor_exists():
    assert callable(trip::model::TravelService.__init__)


def test_trip::model::travelservice_constructor_args():
    sig = inspect.signature(trip::model::TravelService.__init__)
    params = list(sig.parameters.keys())



def test_trip::model::otherservice_is_not_abstract():
    assert not inspect.isabstract(trip::model::OtherService)


def test_trip::model::otherservice_constructor_exists():
    assert callable(trip::model::OtherService.__init__)


def test_trip::model::otherservice_constructor_args():
    sig = inspect.signature(trip::model::OtherService.__init__)
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
trip::model::TripModel_strategy = st.builds(
    trip::model::TripModel,
)
trip::model::Trip_strategy = st.builds(
    trip::model::Trip,
    Start=
        st.dates(),
    End=
        st.dates(),
    name=
        safe_text
)
trip::model::location_strategy = st.builds(
    trip::model::location,
    name=
        safe_text
)
trip::model::Service_strategy = st.builds(
    trip::model::Service,
    Cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Type=
        safe_text,
    name=
        safe_text,
    Duration=
        st.integers(),
    Rating=
        st.integers()
)
Service_strategy = st.builds(
    Service,
)
trip::model::TravelService_strategy = st.builds(
    trip::model::TravelService,
)
trip::model::OtherService_strategy = st.builds(
    trip::model::OtherService,
)

@given(instance=trip::model::TripModel_strategy)
@settings(max_examples=50)
def test_trip::model::tripmodel_instantiation(instance):
    assert isinstance(instance, trip::model::TripModel)

@given(instance=trip::model::Trip_strategy)
@settings(max_examples=50)
def test_trip::model::trip_instantiation(instance):
    assert isinstance(instance, trip::model::Trip)

@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_Start_type(instance):
    assert isinstance(instance.Start, date)


@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_Start_setter(instance):
    original = instance.Start
    instance.Start = original
    assert instance.Start == original

@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_End_type(instance):
    assert isinstance(instance.End, date)


@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_End_setter(instance):
    original = instance.End
    instance.End = original
    assert instance.End == original

@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trip::model::Trip_strategy)
def test_trip::model::trip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trip::model::location_strategy)
@settings(max_examples=50)
def test_trip::model::location_instantiation(instance):
    assert isinstance(instance, trip::model::location)

@given(instance=trip::model::location_strategy)
def test_trip::model::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trip::model::location_strategy)
def test_trip::model::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trip::model::Service_strategy)
@settings(max_examples=50)
def test_trip::model::service_instantiation(instance):
    assert isinstance(instance, trip::model::Service)

@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Cost_type(instance):
    assert isinstance(instance.Cost, float)


@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Cost_setter(instance):
    original = instance.Cost
    instance.Cost = original
    assert instance.Cost == original

@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=trip::model::Service_strategy)
def test_trip::model::service_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trip::model::Service_strategy)
def test_trip::model::service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Duration_type(instance):
    assert isinstance(instance.Duration, int)


@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Duration_setter(instance):
    original = instance.Duration
    instance.Duration = original
    assert instance.Duration == original

@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Rating_type(instance):
    assert isinstance(instance.Rating, int)


@given(instance=trip::model::Service_strategy)
def test_trip::model::service_Rating_setter(instance):
    original = instance.Rating
    instance.Rating = original
    assert instance.Rating == original

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)

@given(instance=trip::model::TravelService_strategy)
@settings(max_examples=50)
def test_trip::model::travelservice_instantiation(instance):
    assert isinstance(instance, trip::model::TravelService)

@given(instance=trip::model::OtherService_strategy)
@settings(max_examples=50)
def test_trip::model::otherservice_instantiation(instance):
    assert isinstance(instance, trip::model::OtherService)
