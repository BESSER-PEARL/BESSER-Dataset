import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Captain,
    Navigator,
    CoPilot,
    Company,
    Aircraft,
    Pilot,
    Airport,
    Flight,
    Airline,
    MaintenanceState,
    FlightState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_captain_is_not_abstract():
    assert not inspect.isabstract(Captain)


def test_captain_constructor_exists():
    assert callable(Captain.__init__)


def test_captain_constructor_args():
    sig = inspect.signature(Captain.__init__)
    params = list(sig.parameters.keys())



def test_navigator_is_not_abstract():
    assert not inspect.isabstract(Navigator)


def test_navigator_constructor_exists():
    assert callable(Navigator.__init__)


def test_navigator_constructor_args():
    sig = inspect.signature(Navigator.__init__)
    params = list(sig.parameters.keys())



def test_copilot_is_not_abstract():
    assert not inspect.isabstract(CoPilot)


def test_copilot_constructor_exists():
    assert callable(CoPilot.__init__)


def test_copilot_constructor_args():
    sig = inspect.signature(CoPilot.__init__)
    params = list(sig.parameters.keys())



def test_company_is_not_abstract():
    assert not inspect.isabstract(Company)


def test_company_constructor_exists():
    assert callable(Company.__init__)


def test_company_constructor_args():
    sig = inspect.signature(Company.__init__)
    params = list(sig.parameters.keys())



def test_aircraft_is_not_abstract():
    assert not inspect.isabstract(Aircraft)


def test_aircraft_constructor_exists():
    assert callable(Aircraft.__init__)


def test_aircraft_constructor_args():
    sig = inspect.signature(Aircraft.__init__)
    params = list(sig.parameters.keys())
    assert "flightState" in params, "Missing parameter 'flightState'"
    assert "state" in params, "Missing parameter 'state'"

def test_aircraft_has_flightState():
    assert hasattr(Aircraft, "flightState")
    descriptor = None
    for klass in Aircraft.__mro__:
        if "flightState" in klass.__dict__:
            descriptor = klass.__dict__["flightState"]
            break
    assert isinstance(descriptor, property)

def test_aircraft_has_state():
    assert hasattr(Aircraft, "state")
    descriptor = None
    for klass in Aircraft.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_pilot_is_not_abstract():
    assert not inspect.isabstract(Pilot)


def test_pilot_constructor_exists():
    assert callable(Pilot.__init__)


def test_pilot_constructor_args():
    sig = inspect.signature(Pilot.__init__)
    params = list(sig.parameters.keys())



def test_airport_is_not_abstract():
    assert not inspect.isabstract(Airport)


def test_airport_constructor_exists():
    assert callable(Airport.__init__)


def test_airport_constructor_args():
    sig = inspect.signature(Airport.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_airport_has_id():
    assert hasattr(Airport, "id")
    descriptor = None
    for klass in Airport.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "departureTime" in params, "Missing parameter 'departureTime'"
    assert "arrivalTime" in params, "Missing parameter 'arrivalTime'"

def test_flight_has_id():
    assert hasattr(Flight, "id")
    descriptor = None
    for klass in Flight.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_departureTime():
    assert hasattr(Flight, "departureTime")
    descriptor = None
    for klass in Flight.__mro__:
        if "departureTime" in klass.__dict__:
            descriptor = klass.__dict__["departureTime"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_arrivalTime():
    assert hasattr(Flight, "arrivalTime")
    descriptor = None
    for klass in Flight.__mro__:
        if "arrivalTime" in klass.__dict__:
            descriptor = klass.__dict__["arrivalTime"]
            break
    assert isinstance(descriptor, property)



def test_airline_is_not_abstract():
    assert not inspect.isabstract(Airline)


def test_airline_constructor_exists():
    assert callable(Airline.__init__)


def test_airline_constructor_args():
    sig = inspect.signature(Airline.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_airline_has_id():
    assert hasattr(Airline, "id")
    descriptor = None
    for klass in Airline.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_maintenancestate_exists():
    # Check that the Enumeration exists
    assert MaintenanceState is not None

def test_maintenancestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaintenanceState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaintenanceState"

def test_flightstate_exists():
    # Check that the Enumeration exists
    assert FlightState is not None

def test_flightstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlightState]
    expected_literals = [
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
Captain_strategy = st.builds(
    Captain,
)
Navigator_strategy = st.builds(
    Navigator,
)
CoPilot_strategy = st.builds(
    CoPilot,
)
Company_strategy = st.builds(
    Company,
)
Aircraft_strategy = st.builds(
    Aircraft,
    flightState=
        st.none(),
    state=
        st.none()
)
Pilot_strategy = st.builds(
    Pilot,
)
Airport_strategy = st.builds(
    Airport,
    id=
        safe_text
)
Flight_strategy = st.builds(
    Flight,
    id=
        st.integers(),
    departureTime=
        st.dates(),
    arrivalTime=
        st.dates()
)
Airline_strategy = st.builds(
    Airline,
    id=
        safe_text
)

@given(instance=Captain_strategy)
@settings(max_examples=50)
def test_captain_instantiation(instance):
    assert isinstance(instance, Captain)

@given(instance=Navigator_strategy)
@settings(max_examples=50)
def test_navigator_instantiation(instance):
    assert isinstance(instance, Navigator)

@given(instance=CoPilot_strategy)
@settings(max_examples=50)
def test_copilot_instantiation(instance):
    assert isinstance(instance, CoPilot)

@given(instance=Company_strategy)
@settings(max_examples=50)
def test_company_instantiation(instance):
    assert isinstance(instance, Company)

@given(instance=Aircraft_strategy)
@settings(max_examples=50)
def test_aircraft_instantiation(instance):
    assert isinstance(instance, Aircraft)



@given(instance=Aircraft_strategy)
def test_aircraft_flightState_setter(instance):
    original = instance.flightState
    instance.flightState = original
    assert instance.flightState == original



@given(instance=Aircraft_strategy)
def test_aircraft_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=Pilot_strategy)
@settings(max_examples=50)
def test_pilot_instantiation(instance):
    assert isinstance(instance, Pilot)

@given(instance=Airport_strategy)
@settings(max_examples=50)
def test_airport_instantiation(instance):
    assert isinstance(instance, Airport)



@given(instance=Airport_strategy)
def test_airport_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Flight_strategy)
def test_flight_departureTime_setter(instance):
    original = instance.departureTime
    instance.departureTime = original
    assert instance.departureTime == original



@given(instance=Flight_strategy)
def test_flight_arrivalTime_setter(instance):
    original = instance.arrivalTime
    instance.arrivalTime = original
    assert instance.arrivalTime == original

@given(instance=Airline_strategy)
@settings(max_examples=50)
def test_airline_instantiation(instance):
    assert isinstance(instance, Airline)



@given(instance=Airline_strategy)
def test_airline_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
