import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RESERVATION_SYSTEM,
    FLIGHT,
    PASSENGER,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reservation_system_is_not_abstract():
    assert not inspect.isabstract(RESERVATION_SYSTEM)


def test_reservation_system_constructor_exists():
    assert callable(RESERVATION_SYSTEM.__init__)


def test_reservation_system_constructor_args():
    sig = inspect.signature(RESERVATION_SYSTEM.__init__)
    params = list(sig.parameters.keys())
    assert "Reservation_ID" in params, "Missing parameter 'Reservation_ID'"
    assert "Reservation_Date" in params, "Missing parameter 'Reservation_Date'"

def test_reservation_system_has_Reservation_ID():
    assert hasattr(RESERVATION_SYSTEM, "Reservation_ID")
    descriptor = None
    for klass in RESERVATION_SYSTEM.__mro__:
        if "Reservation_ID" in klass.__dict__:
            descriptor = klass.__dict__["Reservation_ID"]
            break
    assert isinstance(descriptor, property)

def test_reservation_system_has_Reservation_Date():
    assert hasattr(RESERVATION_SYSTEM, "Reservation_Date")
    descriptor = None
    for klass in RESERVATION_SYSTEM.__mro__:
        if "Reservation_Date" in klass.__dict__:
            descriptor = klass.__dict__["Reservation_Date"]
            break
    assert isinstance(descriptor, property)



def test_flight_is_not_abstract():
    assert not inspect.isabstract(FLIGHT)


def test_flight_constructor_exists():
    assert callable(FLIGHT.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(FLIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "Flight_No_" in params, "Missing parameter 'Flight_No_'"
    assert "Flight_Name" in params, "Missing parameter 'Flight_Name'"

def test_flight_has_Flight_No_():
    assert hasattr(FLIGHT, "Flight_No_")
    descriptor = None
    for klass in FLIGHT.__mro__:
        if "Flight_No_" in klass.__dict__:
            descriptor = klass.__dict__["Flight_No_"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Flight_Name():
    assert hasattr(FLIGHT, "Flight_Name")
    descriptor = None
    for klass in FLIGHT.__mro__:
        if "Flight_Name" in klass.__dict__:
            descriptor = klass.__dict__["Flight_Name"]
            break
    assert isinstance(descriptor, property)



def test_passenger_is_not_abstract():
    assert not inspect.isabstract(PASSENGER)


def test_passenger_constructor_exists():
    assert callable(PASSENGER.__init__)


def test_passenger_constructor_args():
    sig = inspect.signature(PASSENGER.__init__)
    params = list(sig.parameters.keys())
    assert "Pass_Name" in params, "Missing parameter 'Pass_Name'"
    assert "Pass_Address" in params, "Missing parameter 'Pass_Address'"
    assert "Pass_ID" in params, "Missing parameter 'Pass_ID'"

def test_passenger_has_Pass_Name():
    assert hasattr(PASSENGER, "Pass_Name")
    descriptor = None
    for klass in PASSENGER.__mro__:
        if "Pass_Name" in klass.__dict__:
            descriptor = klass.__dict__["Pass_Name"]
            break
    assert isinstance(descriptor, property)

def test_passenger_has_Pass_Address():
    assert hasattr(PASSENGER, "Pass_Address")
    descriptor = None
    for klass in PASSENGER.__mro__:
        if "Pass_Address" in klass.__dict__:
            descriptor = klass.__dict__["Pass_Address"]
            break
    assert isinstance(descriptor, property)

def test_passenger_has_Pass_ID():
    assert hasattr(PASSENGER, "Pass_ID")
    descriptor = None
    for klass in PASSENGER.__mro__:
        if "Pass_ID" in klass.__dict__:
            descriptor = klass.__dict__["Pass_ID"]
            break
    assert isinstance(descriptor, property)


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
RESERVATION_SYSTEM_strategy = st.builds(
    RESERVATION_SYSTEM,
    Reservation_ID=
        st.integers(),
    Reservation_Date=
        st.integers()
)
FLIGHT_strategy = st.builds(
    FLIGHT,
    Flight_No_=
        st.integers(),
    Flight_Name=
        safe_text
)
PASSENGER_strategy = st.builds(
    PASSENGER,
    Pass_Name=
        safe_text,
    Pass_Address=
        safe_text,
    Pass_ID=
        st.integers()
)

@given(instance=RESERVATION_SYSTEM_strategy)
@settings(max_examples=50)
def test_reservation_system_instantiation(instance):
    assert isinstance(instance, RESERVATION_SYSTEM)



@given(instance=RESERVATION_SYSTEM_strategy)
def test_reservation_system_Reservation_ID_setter(instance):
    original = instance.Reservation_ID
    instance.Reservation_ID = original
    assert instance.Reservation_ID == original



@given(instance=RESERVATION_SYSTEM_strategy)
def test_reservation_system_Reservation_Date_setter(instance):
    original = instance.Reservation_Date
    instance.Reservation_Date = original
    assert instance.Reservation_Date == original

@given(instance=FLIGHT_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, FLIGHT)



@given(instance=FLIGHT_strategy)
def test_flight_Flight_No__setter(instance):
    original = instance.Flight_No_
    instance.Flight_No_ = original
    assert instance.Flight_No_ == original



@given(instance=FLIGHT_strategy)
def test_flight_Flight_Name_setter(instance):
    original = instance.Flight_Name
    instance.Flight_Name = original
    assert instance.Flight_Name == original

@given(instance=PASSENGER_strategy)
@settings(max_examples=50)
def test_passenger_instantiation(instance):
    assert isinstance(instance, PASSENGER)



@given(instance=PASSENGER_strategy)
def test_passenger_Pass_Name_setter(instance):
    original = instance.Pass_Name
    instance.Pass_Name = original
    assert instance.Pass_Name == original



@given(instance=PASSENGER_strategy)
def test_passenger_Pass_Address_setter(instance):
    original = instance.Pass_Address
    instance.Pass_Address = original
    assert instance.Pass_Address == original



@given(instance=PASSENGER_strategy)
def test_passenger_Pass_ID_setter(instance):
    original = instance.Pass_ID
    instance.Pass_ID = original
    assert instance.Pass_ID == original
