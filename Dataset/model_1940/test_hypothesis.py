import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FlightObject,
    Flights_Plane,
    Flights_Airport,
    Flights_Booking,
    Flights_Route,
    Flights_Gate,
    Flights_Travel,
    Flights_Flight,
    Flights_Person,
    Flights_FlightObject,
    Flights_TimeStamp,
    Flights_Planes,
    Flights_Airports,
    Flights_Routes,
    Flights_Persons,
    Flights_Bookings,
    Flights_FlightContainer,
    Flights_FlightModel,
    TravelState,
    FlightState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flightobject_is_not_abstract():
    assert not inspect.isabstract(FlightObject)


def test_flightobject_constructor_exists():
    assert callable(FlightObject.__init__)


def test_flightobject_constructor_args():
    sig = inspect.signature(FlightObject.__init__)
    params = list(sig.parameters.keys())



def test_flights_plane_is_not_abstract():
    assert not inspect.isabstract(Flights_Plane)


def test_flights_plane_constructor_exists():
    assert callable(Flights_Plane.__init__)


def test_flights_plane_constructor_args():
    sig = inspect.signature(Flights_Plane.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_flights_plane_has_capacity():
    assert hasattr(Flights_Plane, "capacity")
    descriptor = None
    for klass in Flights_Plane.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_flights_airport_is_not_abstract():
    assert not inspect.isabstract(Flights_Airport)


def test_flights_airport_constructor_exists():
    assert callable(Flights_Airport.__init__)


def test_flights_airport_constructor_args():
    sig = inspect.signature(Flights_Airport.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_flights_airport_has_size():
    assert hasattr(Flights_Airport, "size")
    descriptor = None
    for klass in Flights_Airport.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_flights_booking_is_not_abstract():
    assert not inspect.isabstract(Flights_Booking)


def test_flights_booking_constructor_exists():
    assert callable(Flights_Booking.__init__)


def test_flights_booking_constructor_args():
    sig = inspect.signature(Flights_Booking.__init__)
    params = list(sig.parameters.keys())



def test_flights_route_is_not_abstract():
    assert not inspect.isabstract(Flights_Route)


def test_flights_route_constructor_exists():
    assert callable(Flights_Route.__init__)


def test_flights_route_constructor_args():
    sig = inspect.signature(Flights_Route.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_flights_route_has_duration():
    assert hasattr(Flights_Route, "duration")
    descriptor = None
    for klass in Flights_Route.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_flights_gate_is_not_abstract():
    assert not inspect.isabstract(Flights_Gate)


def test_flights_gate_constructor_exists():
    assert callable(Flights_Gate.__init__)


def test_flights_gate_constructor_args():
    sig = inspect.signature(Flights_Gate.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_flights_gate_has_position():
    assert hasattr(Flights_Gate, "position")
    descriptor = None
    for klass in Flights_Gate.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_flights_travel_is_not_abstract():
    assert not inspect.isabstract(Flights_Travel)


def test_flights_travel_constructor_exists():
    assert callable(Flights_Travel.__init__)


def test_flights_travel_constructor_args():
    sig = inspect.signature(Flights_Travel.__init__)
    params = list(sig.parameters.keys())



def test_flights_flight_is_not_abstract():
    assert not inspect.isabstract(Flights_Flight)


def test_flights_flight_constructor_exists():
    assert callable(Flights_Flight.__init__)


def test_flights_flight_constructor_args():
    sig = inspect.signature(Flights_Flight.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_flights_flight_has_newAttribute():
    assert hasattr(Flights_Flight, "newAttribute")
    descriptor = None
    for klass in Flights_Flight.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_flights_person_is_not_abstract():
    assert not inspect.isabstract(Flights_Person)


def test_flights_person_constructor_exists():
    assert callable(Flights_Person.__init__)


def test_flights_person_constructor_args():
    sig = inspect.signature(Flights_Person.__init__)
    params = list(sig.parameters.keys())
    assert "travelState" in params, "Missing parameter 'travelState'"

def test_flights_person_has_travelState():
    assert hasattr(Flights_Person, "travelState")
    descriptor = None
    for klass in Flights_Person.__mro__:
        if "travelState" in klass.__dict__:
            descriptor = klass.__dict__["travelState"]
            break
    assert isinstance(descriptor, property)



def test_flights_flightobject_is_not_abstract():
    assert not inspect.isabstract(Flights_FlightObject)


def test_flights_flightobject_constructor_exists():
    assert callable(Flights_FlightObject.__init__)


def test_flights_flightobject_constructor_args():
    sig = inspect.signature(Flights_FlightObject.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_flights_flightobject_has_ID():
    assert hasattr(Flights_FlightObject, "ID")
    descriptor = None
    for klass in Flights_FlightObject.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_flights_timestamp_is_not_abstract():
    assert not inspect.isabstract(Flights_TimeStamp)


def test_flights_timestamp_constructor_exists():
    assert callable(Flights_TimeStamp.__init__)


def test_flights_timestamp_constructor_args():
    sig = inspect.signature(Flights_TimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_flights_timestamp_has_time():
    assert hasattr(Flights_TimeStamp, "time")
    descriptor = None
    for klass in Flights_TimeStamp.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_flights_planes_is_not_abstract():
    assert not inspect.isabstract(Flights_Planes)


def test_flights_planes_constructor_exists():
    assert callable(Flights_Planes.__init__)


def test_flights_planes_constructor_args():
    sig = inspect.signature(Flights_Planes.__init__)
    params = list(sig.parameters.keys())



def test_flights_airports_is_not_abstract():
    assert not inspect.isabstract(Flights_Airports)


def test_flights_airports_constructor_exists():
    assert callable(Flights_Airports.__init__)


def test_flights_airports_constructor_args():
    sig = inspect.signature(Flights_Airports.__init__)
    params = list(sig.parameters.keys())



def test_flights_routes_is_not_abstract():
    assert not inspect.isabstract(Flights_Routes)


def test_flights_routes_constructor_exists():
    assert callable(Flights_Routes.__init__)


def test_flights_routes_constructor_args():
    sig = inspect.signature(Flights_Routes.__init__)
    params = list(sig.parameters.keys())



def test_flights_persons_is_not_abstract():
    assert not inspect.isabstract(Flights_Persons)


def test_flights_persons_constructor_exists():
    assert callable(Flights_Persons.__init__)


def test_flights_persons_constructor_args():
    sig = inspect.signature(Flights_Persons.__init__)
    params = list(sig.parameters.keys())



def test_flights_bookings_is_not_abstract():
    assert not inspect.isabstract(Flights_Bookings)


def test_flights_bookings_constructor_exists():
    assert callable(Flights_Bookings.__init__)


def test_flights_bookings_constructor_args():
    sig = inspect.signature(Flights_Bookings.__init__)
    params = list(sig.parameters.keys())



def test_flights_flightcontainer_is_not_abstract():
    assert not inspect.isabstract(Flights_FlightContainer)


def test_flights_flightcontainer_constructor_exists():
    assert callable(Flights_FlightContainer.__init__)


def test_flights_flightcontainer_constructor_args():
    sig = inspect.signature(Flights_FlightContainer.__init__)
    params = list(sig.parameters.keys())



def test_flights_flightmodel_is_not_abstract():
    assert not inspect.isabstract(Flights_FlightModel)


def test_flights_flightmodel_constructor_exists():
    assert callable(Flights_FlightModel.__init__)


def test_flights_flightmodel_constructor_args():
    sig = inspect.signature(Flights_FlightModel.__init__)
    params = list(sig.parameters.keys())

def test_travelstate_exists():
    # Check that the Enumeration exists
    assert TravelState is not None

def test_travelstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TravelState]
    expected_literals = [
        "checkedIn",
        "luggageDroppedOf",
        "unknown",
        "onBoard",
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
        "planned",
        "inFlight",
        "completed",
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
FlightObject_strategy = st.builds(
    FlightObject,
)
Flights_Plane_strategy = st.builds(
    Flights_Plane,
    capacity=
        st.integers()
)
Flights_Airport_strategy = st.builds(
    Flights_Airport,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Flights_Booking_strategy = st.builds(
    Flights_Booking,
)
Flights_Route_strategy = st.builds(
    Flights_Route,
    duration=
        st.integers()
)
Flights_Gate_strategy = st.builds(
    Flights_Gate,
    position=
        st.integers()
)
Flights_Travel_strategy = st.builds(
    Flights_Travel,
)
Flights_Flight_strategy = st.builds(
    Flights_Flight,
    newAttribute=
        safe_text
)
Flights_Person_strategy = st.builds(
    Flights_Person,
    travelState=
        safe_text
)
Flights_FlightObject_strategy = st.builds(
    Flights_FlightObject,
    ID=
        safe_text
)
Flights_TimeStamp_strategy = st.builds(
    Flights_TimeStamp,
    time=
        safe_text
)
Flights_Planes_strategy = st.builds(
    Flights_Planes,
)
Flights_Airports_strategy = st.builds(
    Flights_Airports,
)
Flights_Routes_strategy = st.builds(
    Flights_Routes,
)
Flights_Persons_strategy = st.builds(
    Flights_Persons,
)
Flights_Bookings_strategy = st.builds(
    Flights_Bookings,
)
Flights_FlightContainer_strategy = st.builds(
    Flights_FlightContainer,
)
Flights_FlightModel_strategy = st.builds(
    Flights_FlightModel,
)

@given(instance=FlightObject_strategy)
@settings(max_examples=50)
def test_flightobject_instantiation(instance):
    assert isinstance(instance, FlightObject)

@given(instance=Flights_Plane_strategy)
@settings(max_examples=50)
def test_flights_plane_instantiation(instance):
    assert isinstance(instance, Flights_Plane)



@given(instance=Flights_Plane_strategy)
def test_flights_plane_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=Flights_Airport_strategy)
@settings(max_examples=50)
def test_flights_airport_instantiation(instance):
    assert isinstance(instance, Flights_Airport)



@given(instance=Flights_Airport_strategy)
def test_flights_airport_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Flights_Booking_strategy)
@settings(max_examples=50)
def test_flights_booking_instantiation(instance):
    assert isinstance(instance, Flights_Booking)

@given(instance=Flights_Route_strategy)
@settings(max_examples=50)
def test_flights_route_instantiation(instance):
    assert isinstance(instance, Flights_Route)



@given(instance=Flights_Route_strategy)
def test_flights_route_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Flights_Gate_strategy)
@settings(max_examples=50)
def test_flights_gate_instantiation(instance):
    assert isinstance(instance, Flights_Gate)



@given(instance=Flights_Gate_strategy)
def test_flights_gate_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Flights_Travel_strategy)
@settings(max_examples=50)
def test_flights_travel_instantiation(instance):
    assert isinstance(instance, Flights_Travel)

@given(instance=Flights_Flight_strategy)
@settings(max_examples=50)
def test_flights_flight_instantiation(instance):
    assert isinstance(instance, Flights_Flight)



@given(instance=Flights_Flight_strategy)
def test_flights_flight_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=Flights_Person_strategy)
@settings(max_examples=50)
def test_flights_person_instantiation(instance):
    assert isinstance(instance, Flights_Person)



@given(instance=Flights_Person_strategy)
def test_flights_person_travelState_setter(instance):
    original = instance.travelState
    instance.travelState = original
    assert instance.travelState == original

@given(instance=Flights_FlightObject_strategy)
@settings(max_examples=50)
def test_flights_flightobject_instantiation(instance):
    assert isinstance(instance, Flights_FlightObject)



@given(instance=Flights_FlightObject_strategy)
def test_flights_flightobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Flights_TimeStamp_strategy)
@settings(max_examples=50)
def test_flights_timestamp_instantiation(instance):
    assert isinstance(instance, Flights_TimeStamp)



@given(instance=Flights_TimeStamp_strategy)
def test_flights_timestamp_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=Flights_Planes_strategy)
@settings(max_examples=50)
def test_flights_planes_instantiation(instance):
    assert isinstance(instance, Flights_Planes)

@given(instance=Flights_Airports_strategy)
@settings(max_examples=50)
def test_flights_airports_instantiation(instance):
    assert isinstance(instance, Flights_Airports)

@given(instance=Flights_Routes_strategy)
@settings(max_examples=50)
def test_flights_routes_instantiation(instance):
    assert isinstance(instance, Flights_Routes)

@given(instance=Flights_Persons_strategy)
@settings(max_examples=50)
def test_flights_persons_instantiation(instance):
    assert isinstance(instance, Flights_Persons)

@given(instance=Flights_Bookings_strategy)
@settings(max_examples=50)
def test_flights_bookings_instantiation(instance):
    assert isinstance(instance, Flights_Bookings)

@given(instance=Flights_FlightContainer_strategy)
@settings(max_examples=50)
def test_flights_flightcontainer_instantiation(instance):
    assert isinstance(instance, Flights_FlightContainer)

@given(instance=Flights_FlightModel_strategy)
@settings(max_examples=50)
def test_flights_flightmodel_instantiation(instance):
    assert isinstance(instance, Flights_FlightModel)
