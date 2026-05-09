import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Flights::FlightContainer,
    Flights::FlightModel,
    FlightObject,
    Flights::Route,
    Flights::Plane,
    Flights::Airport,
    Flights::Gate,
    Flights::Booking,
    Flights::Travel,
    Flights::Flight,
    Flights::Person,
    Flights::FlightObject,
    Flights::TimeStamp,
    Flights::Planes,
    Flights::Airports,
    Flights::Routes,
    Flights::Persons,
    Flights::Bookings,
    TravelState,
    FlightState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flights::flightcontainer_is_not_abstract():
    assert not inspect.isabstract(Flights::FlightContainer)


def test_flights::flightcontainer_constructor_exists():
    assert callable(Flights::FlightContainer.__init__)


def test_flights::flightcontainer_constructor_args():
    sig = inspect.signature(Flights::FlightContainer.__init__)
    params = list(sig.parameters.keys())



def test_flights::flightmodel_is_not_abstract():
    assert not inspect.isabstract(Flights::FlightModel)


def test_flights::flightmodel_constructor_exists():
    assert callable(Flights::FlightModel.__init__)


def test_flights::flightmodel_constructor_args():
    sig = inspect.signature(Flights::FlightModel.__init__)
    params = list(sig.parameters.keys())



def test_flightobject_is_not_abstract():
    assert not inspect.isabstract(FlightObject)


def test_flightobject_constructor_exists():
    assert callable(FlightObject.__init__)


def test_flightobject_constructor_args():
    sig = inspect.signature(FlightObject.__init__)
    params = list(sig.parameters.keys())



def test_flights::route_is_not_abstract():
    assert not inspect.isabstract(Flights::Route)


def test_flights::route_constructor_exists():
    assert callable(Flights::Route.__init__)


def test_flights::route_constructor_args():
    sig = inspect.signature(Flights::Route.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_flights::route_has_duration():
    assert hasattr(Flights::Route, "duration")
    descriptor = None
    for klass in Flights::Route.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_flights::plane_is_not_abstract():
    assert not inspect.isabstract(Flights::Plane)


def test_flights::plane_constructor_exists():
    assert callable(Flights::Plane.__init__)


def test_flights::plane_constructor_args():
    sig = inspect.signature(Flights::Plane.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_flights::plane_has_capacity():
    assert hasattr(Flights::Plane, "capacity")
    descriptor = None
    for klass in Flights::Plane.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_flights::airport_is_not_abstract():
    assert not inspect.isabstract(Flights::Airport)


def test_flights::airport_constructor_exists():
    assert callable(Flights::Airport.__init__)


def test_flights::airport_constructor_args():
    sig = inspect.signature(Flights::Airport.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_flights::airport_has_size():
    assert hasattr(Flights::Airport, "size")
    descriptor = None
    for klass in Flights::Airport.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_flights::gate_is_not_abstract():
    assert not inspect.isabstract(Flights::Gate)


def test_flights::gate_constructor_exists():
    assert callable(Flights::Gate.__init__)


def test_flights::gate_constructor_args():
    sig = inspect.signature(Flights::Gate.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_flights::gate_has_position():
    assert hasattr(Flights::Gate, "position")
    descriptor = None
    for klass in Flights::Gate.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_flights::booking_is_not_abstract():
    assert not inspect.isabstract(Flights::Booking)


def test_flights::booking_constructor_exists():
    assert callable(Flights::Booking.__init__)


def test_flights::booking_constructor_args():
    sig = inspect.signature(Flights::Booking.__init__)
    params = list(sig.parameters.keys())



def test_flights::travel_is_not_abstract():
    assert not inspect.isabstract(Flights::Travel)


def test_flights::travel_constructor_exists():
    assert callable(Flights::Travel.__init__)


def test_flights::travel_constructor_args():
    sig = inspect.signature(Flights::Travel.__init__)
    params = list(sig.parameters.keys())



def test_flights::flight_is_not_abstract():
    assert not inspect.isabstract(Flights::Flight)


def test_flights::flight_constructor_exists():
    assert callable(Flights::Flight.__init__)


def test_flights::flight_constructor_args():
    sig = inspect.signature(Flights::Flight.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_flights::flight_has_newAttribute():
    assert hasattr(Flights::Flight, "newAttribute")
    descriptor = None
    for klass in Flights::Flight.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_flights::person_is_not_abstract():
    assert not inspect.isabstract(Flights::Person)


def test_flights::person_constructor_exists():
    assert callable(Flights::Person.__init__)


def test_flights::person_constructor_args():
    sig = inspect.signature(Flights::Person.__init__)
    params = list(sig.parameters.keys())
    assert "travelState" in params, "Missing parameter 'travelState'"

def test_flights::person_has_travelState():
    assert hasattr(Flights::Person, "travelState")
    descriptor = None
    for klass in Flights::Person.__mro__:
        if "travelState" in klass.__dict__:
            descriptor = klass.__dict__["travelState"]
            break
    assert isinstance(descriptor, property)



def test_flights::flightobject_is_not_abstract():
    assert not inspect.isabstract(Flights::FlightObject)


def test_flights::flightobject_constructor_exists():
    assert callable(Flights::FlightObject.__init__)


def test_flights::flightobject_constructor_args():
    sig = inspect.signature(Flights::FlightObject.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_flights::flightobject_has_ID():
    assert hasattr(Flights::FlightObject, "ID")
    descriptor = None
    for klass in Flights::FlightObject.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_flights::timestamp_is_not_abstract():
    assert not inspect.isabstract(Flights::TimeStamp)


def test_flights::timestamp_constructor_exists():
    assert callable(Flights::TimeStamp.__init__)


def test_flights::timestamp_constructor_args():
    sig = inspect.signature(Flights::TimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_flights::timestamp_has_time():
    assert hasattr(Flights::TimeStamp, "time")
    descriptor = None
    for klass in Flights::TimeStamp.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_flights::planes_is_not_abstract():
    assert not inspect.isabstract(Flights::Planes)


def test_flights::planes_constructor_exists():
    assert callable(Flights::Planes.__init__)


def test_flights::planes_constructor_args():
    sig = inspect.signature(Flights::Planes.__init__)
    params = list(sig.parameters.keys())



def test_flights::airports_is_not_abstract():
    assert not inspect.isabstract(Flights::Airports)


def test_flights::airports_constructor_exists():
    assert callable(Flights::Airports.__init__)


def test_flights::airports_constructor_args():
    sig = inspect.signature(Flights::Airports.__init__)
    params = list(sig.parameters.keys())



def test_flights::routes_is_not_abstract():
    assert not inspect.isabstract(Flights::Routes)


def test_flights::routes_constructor_exists():
    assert callable(Flights::Routes.__init__)


def test_flights::routes_constructor_args():
    sig = inspect.signature(Flights::Routes.__init__)
    params = list(sig.parameters.keys())



def test_flights::persons_is_not_abstract():
    assert not inspect.isabstract(Flights::Persons)


def test_flights::persons_constructor_exists():
    assert callable(Flights::Persons.__init__)


def test_flights::persons_constructor_args():
    sig = inspect.signature(Flights::Persons.__init__)
    params = list(sig.parameters.keys())



def test_flights::bookings_is_not_abstract():
    assert not inspect.isabstract(Flights::Bookings)


def test_flights::bookings_constructor_exists():
    assert callable(Flights::Bookings.__init__)


def test_flights::bookings_constructor_args():
    sig = inspect.signature(Flights::Bookings.__init__)
    params = list(sig.parameters.keys())

def test_travelstate_exists():
    # Check that the Enumeration exists
    assert TravelState is not None

def test_travelstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TravelState]
    expected_literals = [
        "unknown",
        "checkedIn",
        "onBoard",
        "luggageDroppedOf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TravelState"

def test_flightstate_exists():
    # Check that the Enumeration exists
    assert FlightState is not None

def test_flightstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlightState]
    expected_literals = [
        "completed",
        "inFlight",
        "planned",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlightState"


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
Flights::FlightContainer_strategy = st.builds(
    Flights::FlightContainer,
)
Flights::FlightModel_strategy = st.builds(
    Flights::FlightModel,
)
FlightObject_strategy = st.builds(
    FlightObject,
)
Flights::Route_strategy = st.builds(
    Flights::Route,
    duration=
        st.integers()
)
Flights::Plane_strategy = st.builds(
    Flights::Plane,
    capacity=
        st.integers()
)
Flights::Airport_strategy = st.builds(
    Flights::Airport,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Flights::Gate_strategy = st.builds(
    Flights::Gate,
    position=
        st.integers()
)
Flights::Booking_strategy = st.builds(
    Flights::Booking,
)
Flights::Travel_strategy = st.builds(
    Flights::Travel,
)
Flights::Flight_strategy = st.builds(
    Flights::Flight,
    newAttribute=
        safe_text
)
Flights::Person_strategy = st.builds(
    Flights::Person,
    travelState=
        safe_text
)
Flights::FlightObject_strategy = st.builds(
    Flights::FlightObject,
    ID=
        safe_text
)
Flights::TimeStamp_strategy = st.builds(
    Flights::TimeStamp,
    time=
        safe_text
)
Flights::Planes_strategy = st.builds(
    Flights::Planes,
)
Flights::Airports_strategy = st.builds(
    Flights::Airports,
)
Flights::Routes_strategy = st.builds(
    Flights::Routes,
)
Flights::Persons_strategy = st.builds(
    Flights::Persons,
)
Flights::Bookings_strategy = st.builds(
    Flights::Bookings,
)

@given(instance=Flights::FlightContainer_strategy)
@settings(max_examples=50)
def test_flights::flightcontainer_instantiation(instance):
    assert isinstance(instance, Flights::FlightContainer)

@given(instance=Flights::FlightModel_strategy)
@settings(max_examples=50)
def test_flights::flightmodel_instantiation(instance):
    assert isinstance(instance, Flights::FlightModel)

@given(instance=FlightObject_strategy)
@settings(max_examples=50)
def test_flightobject_instantiation(instance):
    assert isinstance(instance, FlightObject)

@given(instance=Flights::Route_strategy)
@settings(max_examples=50)
def test_flights::route_instantiation(instance):
    assert isinstance(instance, Flights::Route)

@given(instance=Flights::Route_strategy)
def test_flights::route_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=Flights::Route_strategy)
def test_flights::route_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Flights::Plane_strategy)
@settings(max_examples=50)
def test_flights::plane_instantiation(instance):
    assert isinstance(instance, Flights::Plane)

@given(instance=Flights::Plane_strategy)
def test_flights::plane_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=Flights::Plane_strategy)
def test_flights::plane_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=Flights::Airport_strategy)
@settings(max_examples=50)
def test_flights::airport_instantiation(instance):
    assert isinstance(instance, Flights::Airport)

@given(instance=Flights::Airport_strategy)
def test_flights::airport_size_type(instance):
    assert isinstance(instance.size, float)


@given(instance=Flights::Airport_strategy)
def test_flights::airport_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Flights::Gate_strategy)
@settings(max_examples=50)
def test_flights::gate_instantiation(instance):
    assert isinstance(instance, Flights::Gate)

@given(instance=Flights::Gate_strategy)
def test_flights::gate_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=Flights::Gate_strategy)
def test_flights::gate_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Flights::Booking_strategy)
@settings(max_examples=50)
def test_flights::booking_instantiation(instance):
    assert isinstance(instance, Flights::Booking)

@given(instance=Flights::Travel_strategy)
@settings(max_examples=50)
def test_flights::travel_instantiation(instance):
    assert isinstance(instance, Flights::Travel)

@given(instance=Flights::Flight_strategy)
@settings(max_examples=50)
def test_flights::flight_instantiation(instance):
    assert isinstance(instance, Flights::Flight)

@given(instance=Flights::Flight_strategy)
def test_flights::flight_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=Flights::Flight_strategy)
def test_flights::flight_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=Flights::Person_strategy)
@settings(max_examples=50)
def test_flights::person_instantiation(instance):
    assert isinstance(instance, Flights::Person)

@given(instance=Flights::Person_strategy)
def test_flights::person_travelState_type(instance):
    assert isinstance(instance.travelState, str)


@given(instance=Flights::Person_strategy)
def test_flights::person_travelState_setter(instance):
    original = instance.travelState
    instance.travelState = original
    assert instance.travelState == original

@given(instance=Flights::FlightObject_strategy)
@settings(max_examples=50)
def test_flights::flightobject_instantiation(instance):
    assert isinstance(instance, Flights::FlightObject)

@given(instance=Flights::FlightObject_strategy)
def test_flights::flightobject_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=Flights::FlightObject_strategy)
def test_flights::flightobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Flights::TimeStamp_strategy)
@settings(max_examples=50)
def test_flights::timestamp_instantiation(instance):
    assert isinstance(instance, Flights::TimeStamp)

@given(instance=Flights::TimeStamp_strategy)
def test_flights::timestamp_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=Flights::TimeStamp_strategy)
def test_flights::timestamp_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=Flights::Planes_strategy)
@settings(max_examples=50)
def test_flights::planes_instantiation(instance):
    assert isinstance(instance, Flights::Planes)

@given(instance=Flights::Airports_strategy)
@settings(max_examples=50)
def test_flights::airports_instantiation(instance):
    assert isinstance(instance, Flights::Airports)

@given(instance=Flights::Routes_strategy)
@settings(max_examples=50)
def test_flights::routes_instantiation(instance):
    assert isinstance(instance, Flights::Routes)

@given(instance=Flights::Persons_strategy)
@settings(max_examples=50)
def test_flights::persons_instantiation(instance):
    assert isinstance(instance, Flights::Persons)

@given(instance=Flights::Bookings_strategy)
@settings(max_examples=50)
def test_flights::bookings_instantiation(instance):
    assert isinstance(instance, Flights::Bookings)
