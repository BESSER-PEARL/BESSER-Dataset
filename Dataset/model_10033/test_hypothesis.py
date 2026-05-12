import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CoachBusWithEDataType_Passenger,
    CoachBusWithEDataType_Ticket,
    Trip,
    CoachBusWithEDataType_PrivateTrip,
    CoachBusWithEDataType_RegularTrip,
    CoachBusWithEDataType_Trip,
    Ticket,
    CoachBusWithEDataType_AdultTicket,
    CoachBusWithEDataType_ChildTicket,
    CoachBusWithEDataType_Coach,
    Sex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbuswithedatatype_passenger_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Passenger)


def test_coachbuswithedatatype_passenger_constructor_exists():
    assert callable(CoachBusWithEDataType_Passenger.__init__)


def test_coachbuswithedatatype_passenger_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_coachbuswithedatatype_passenger_has_age():
    assert hasattr(CoachBusWithEDataType_Passenger, "age")
    descriptor = None
    for klass in CoachBusWithEDataType_Passenger.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_passenger_has_sex():
    assert hasattr(CoachBusWithEDataType_Passenger, "sex")
    descriptor = None
    for klass in CoachBusWithEDataType_Passenger.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_ticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Ticket)


def test_coachbuswithedatatype_ticket_constructor_exists():
    assert callable(CoachBusWithEDataType_Ticket.__init__)


def test_coachbuswithedatatype_ticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_coachbuswithedatatype_ticket_has_number():
    assert hasattr(CoachBusWithEDataType_Ticket, "number")
    descriptor = None
    for klass in CoachBusWithEDataType_Ticket.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_trip_is_not_abstract():
    assert not inspect.isabstract(Trip)


def test_trip_constructor_exists():
    assert callable(Trip.__init__)


def test_trip_constructor_args():
    sig = inspect.signature(Trip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_privatetrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_PrivateTrip)


def test_coachbuswithedatatype_privatetrip_constructor_exists():
    assert callable(CoachBusWithEDataType_PrivateTrip.__init__)


def test_coachbuswithedatatype_privatetrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_PrivateTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_regulartrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_RegularTrip)


def test_coachbuswithedatatype_regulartrip_constructor_exists():
    assert callable(CoachBusWithEDataType_RegularTrip.__init__)


def test_coachbuswithedatatype_regulartrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_RegularTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_trip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Trip)


def test_coachbuswithedatatype_trip_constructor_exists():
    assert callable(CoachBusWithEDataType_Trip.__init__)


def test_coachbuswithedatatype_trip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Trip.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_coachbuswithedatatype_trip_has_type():
    assert hasattr(CoachBusWithEDataType_Trip, "type")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_adultticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_AdultTicket)


def test_coachbuswithedatatype_adultticket_constructor_exists():
    assert callable(CoachBusWithEDataType_AdultTicket.__init__)


def test_coachbuswithedatatype_adultticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_AdultTicket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_childticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_ChildTicket)


def test_coachbuswithedatatype_childticket_constructor_exists():
    assert callable(CoachBusWithEDataType_ChildTicket.__init__)


def test_coachbuswithedatatype_childticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_ChildTicket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Coach)


def test_coachbuswithedatatype_coach_constructor_exists():
    assert callable(CoachBusWithEDataType_Coach.__init__)


def test_coachbuswithedatatype_coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"

def test_coachbuswithedatatype_coach_has_noOfSeats():
    assert hasattr(CoachBusWithEDataType_Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBusWithEDataType_Coach.__mro__:
        if "noOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["noOfSeats"]
            break
    assert isinstance(descriptor, property)

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "male",
        "female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"


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
CoachBusWithEDataType_Passenger_strategy = st.builds(
    CoachBusWithEDataType_Passenger,
    age=
        st.integers(),
    sex=
        safe_text
)
CoachBusWithEDataType_Ticket_strategy = st.builds(
    CoachBusWithEDataType_Ticket,
    number=
        st.integers()
)
Trip_strategy = st.builds(
    Trip,
)
CoachBusWithEDataType_PrivateTrip_strategy = st.builds(
    CoachBusWithEDataType_PrivateTrip,
)
CoachBusWithEDataType_RegularTrip_strategy = st.builds(
    CoachBusWithEDataType_RegularTrip,
)
CoachBusWithEDataType_Trip_strategy = st.builds(
    CoachBusWithEDataType_Trip,
    type=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
)
CoachBusWithEDataType_AdultTicket_strategy = st.builds(
    CoachBusWithEDataType_AdultTicket,
)
CoachBusWithEDataType_ChildTicket_strategy = st.builds(
    CoachBusWithEDataType_ChildTicket,
)
CoachBusWithEDataType_Coach_strategy = st.builds(
    CoachBusWithEDataType_Coach,
    noOfSeats=
        st.integers()
)

@given(instance=CoachBusWithEDataType_Passenger_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_passenger_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Passenger)



@given(instance=CoachBusWithEDataType_Passenger_strategy)
def test_coachbuswithedatatype_passenger_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=CoachBusWithEDataType_Passenger_strategy)
def test_coachbuswithedatatype_passenger_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=CoachBusWithEDataType_Ticket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_ticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Ticket)



@given(instance=CoachBusWithEDataType_Ticket_strategy)
def test_coachbuswithedatatype_ticket_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Trip_strategy)
@settings(max_examples=50)
def test_trip_instantiation(instance):
    assert isinstance(instance, Trip)

@given(instance=CoachBusWithEDataType_PrivateTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_privatetrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_PrivateTrip)

@given(instance=CoachBusWithEDataType_RegularTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_regulartrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_RegularTrip)

@given(instance=CoachBusWithEDataType_Trip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_trip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Trip)



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)

@given(instance=CoachBusWithEDataType_AdultTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_adultticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_AdultTicket)

@given(instance=CoachBusWithEDataType_ChildTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_childticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_ChildTicket)

@given(instance=CoachBusWithEDataType_Coach_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Coach)



@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_coachbuswithedatatype_coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original
