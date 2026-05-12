import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CoachBusWithEDataType::Passenger,
    CoachBusWithEDataType::Ticket,
    Trip,
    CoachBusWithEDataType::PrivateTrip,
    CoachBusWithEDataType::RegularTrip,
    CoachBusWithEDataType::Trip,
    Ticket,
    CoachBusWithEDataType::AdultTicket,
    CoachBusWithEDataType::ChildTicket,
    CoachBusWithEDataType::Coach,
    Sex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coachbuswithedatatype::passenger_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Passenger)


def test_coachbuswithedatatype::passenger_constructor_exists():
    assert callable(CoachBusWithEDataType::Passenger.__init__)


def test_coachbuswithedatatype::passenger_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_coachbuswithedatatype::passenger_has_age():
    assert hasattr(CoachBusWithEDataType::Passenger, "age")
    descriptor = None
    for klass in CoachBusWithEDataType::Passenger.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::passenger_has_sex():
    assert hasattr(CoachBusWithEDataType::Passenger, "sex")
    descriptor = None
    for klass in CoachBusWithEDataType::Passenger.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::ticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Ticket)


def test_coachbuswithedatatype::ticket_constructor_exists():
    assert callable(CoachBusWithEDataType::Ticket.__init__)


def test_coachbuswithedatatype::ticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_coachbuswithedatatype::ticket_has_number():
    assert hasattr(CoachBusWithEDataType::Ticket, "number")
    descriptor = None
    for klass in CoachBusWithEDataType::Ticket.__mro__:
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



def test_coachbuswithedatatype::privatetrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::PrivateTrip)


def test_coachbuswithedatatype::privatetrip_constructor_exists():
    assert callable(CoachBusWithEDataType::PrivateTrip.__init__)


def test_coachbuswithedatatype::privatetrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::PrivateTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::regulartrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::RegularTrip)


def test_coachbuswithedatatype::regulartrip_constructor_exists():
    assert callable(CoachBusWithEDataType::RegularTrip.__init__)


def test_coachbuswithedatatype::regulartrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::RegularTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::trip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Trip)


def test_coachbuswithedatatype::trip_constructor_exists():
    assert callable(CoachBusWithEDataType::Trip.__init__)


def test_coachbuswithedatatype::trip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Trip.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_coachbuswithedatatype::trip_has_type():
    assert hasattr(CoachBusWithEDataType::Trip, "type")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
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



def test_coachbuswithedatatype::adultticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::AdultTicket)


def test_coachbuswithedatatype::adultticket_constructor_exists():
    assert callable(CoachBusWithEDataType::AdultTicket.__init__)


def test_coachbuswithedatatype::adultticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::AdultTicket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::childticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::ChildTicket)


def test_coachbuswithedatatype::childticket_constructor_exists():
    assert callable(CoachBusWithEDataType::ChildTicket.__init__)


def test_coachbuswithedatatype::childticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::ChildTicket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Coach)


def test_coachbuswithedatatype::coach_constructor_exists():
    assert callable(CoachBusWithEDataType::Coach.__init__)


def test_coachbuswithedatatype::coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"

def test_coachbuswithedatatype::coach_has_noOfSeats():
    assert hasattr(CoachBusWithEDataType::Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
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
CoachBusWithEDataType::Passenger_strategy = st.builds(
    CoachBusWithEDataType::Passenger,
    age=
        st.integers(),
    sex=
        safe_text
)
CoachBusWithEDataType::Ticket_strategy = st.builds(
    CoachBusWithEDataType::Ticket,
    number=
        st.integers()
)
Trip_strategy = st.builds(
    Trip,
)
CoachBusWithEDataType::PrivateTrip_strategy = st.builds(
    CoachBusWithEDataType::PrivateTrip,
)
CoachBusWithEDataType::RegularTrip_strategy = st.builds(
    CoachBusWithEDataType::RegularTrip,
)
CoachBusWithEDataType::Trip_strategy = st.builds(
    CoachBusWithEDataType::Trip,
    type=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
)
CoachBusWithEDataType::AdultTicket_strategy = st.builds(
    CoachBusWithEDataType::AdultTicket,
)
CoachBusWithEDataType::ChildTicket_strategy = st.builds(
    CoachBusWithEDataType::ChildTicket,
)
CoachBusWithEDataType::Coach_strategy = st.builds(
    CoachBusWithEDataType::Coach,
    noOfSeats=
        st.integers()
)

@given(instance=CoachBusWithEDataType::Passenger_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::passenger_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Passenger)

@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=CoachBusWithEDataType::Ticket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::ticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Ticket)

@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Trip_strategy)
@settings(max_examples=50)
def test_trip_instantiation(instance):
    assert isinstance(instance, Trip)

@given(instance=CoachBusWithEDataType::PrivateTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::privatetrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::PrivateTrip)

@given(instance=CoachBusWithEDataType::RegularTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::regulartrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::RegularTrip)

@given(instance=CoachBusWithEDataType::Trip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::trip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Trip)

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)

@given(instance=CoachBusWithEDataType::AdultTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::adultticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::AdultTicket)

@given(instance=CoachBusWithEDataType::ChildTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::childticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::ChildTicket)

@given(instance=CoachBusWithEDataType::Coach_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Coach)

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_type(instance):
    assert isinstance(instance.noOfSeats, int)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original
