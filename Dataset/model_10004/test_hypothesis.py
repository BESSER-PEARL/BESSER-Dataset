import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Ticket,
    CoachBusWithEDataType::ChildTicket,
    CoachBusWithEDataType::AdultTicket,
    Employee,
    CoachBusWithEDataType::Manager,
    CoachBusWithEDataType::VendingMachine,
    Trip,
    CoachBusWithEDataType::PrivateTrip,
    CoachBusWithEDataType::RegularTrip,
    CoachBusWithEDataType::Passenger,
    CoachBusWithEDataType::Coach,
    CoachBusWithEDataType::Trip,
    CoachBusWithEDataType::Employee,
    CoachBusWithEDataType::Ticket,
    CoachBusWithEDataType::BookingOffice,
    CoachBusWithEDataType::SecurityGuard,
    Sex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::childticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::ChildTicket)


def test_coachbuswithedatatype::childticket_constructor_exists():
    assert callable(CoachBusWithEDataType::ChildTicket.__init__)


def test_coachbuswithedatatype::childticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::ChildTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isSchoolTrip" in params, "Missing parameter 'isSchoolTrip'"

def test_coachbuswithedatatype::childticket_has_isSchoolTrip():
    assert hasattr(CoachBusWithEDataType::ChildTicket, "isSchoolTrip")
    descriptor = None
    for klass in CoachBusWithEDataType::ChildTicket.__mro__:
        if "isSchoolTrip" in klass.__dict__:
            descriptor = klass.__dict__["isSchoolTrip"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::adultticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::AdultTicket)


def test_coachbuswithedatatype::adultticket_constructor_exists():
    assert callable(CoachBusWithEDataType::AdultTicket.__init__)


def test_coachbuswithedatatype::adultticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::AdultTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isElderlyDiscount" in params, "Missing parameter 'isElderlyDiscount'"

def test_coachbuswithedatatype::adultticket_has_isElderlyDiscount():
    assert hasattr(CoachBusWithEDataType::AdultTicket, "isElderlyDiscount")
    descriptor = None
    for klass in CoachBusWithEDataType::AdultTicket.__mro__:
        if "isElderlyDiscount" in klass.__dict__:
            descriptor = klass.__dict__["isElderlyDiscount"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::manager_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Manager)


def test_coachbuswithedatatype::manager_constructor_exists():
    assert callable(CoachBusWithEDataType::Manager.__init__)


def test_coachbuswithedatatype::manager_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Manager.__init__)
    params = list(sig.parameters.keys())
    assert "hasMBA" in params, "Missing parameter 'hasMBA'"

def test_coachbuswithedatatype::manager_has_hasMBA():
    assert hasattr(CoachBusWithEDataType::Manager, "hasMBA")
    descriptor = None
    for klass in CoachBusWithEDataType::Manager.__mro__:
        if "hasMBA" in klass.__dict__:
            descriptor = klass.__dict__["hasMBA"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::vendingmachine_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::VendingMachine)


def test_coachbuswithedatatype::vendingmachine_constructor_exists():
    assert callable(CoachBusWithEDataType::VendingMachine.__init__)


def test_coachbuswithedatatype::vendingmachine_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::VendingMachine.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_coachbuswithedatatype::vendingmachine_has_number():
    assert hasattr(CoachBusWithEDataType::VendingMachine, "number")
    descriptor = None
    for klass in CoachBusWithEDataType::VendingMachine.__mro__:
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
    assert "extras" in params, "Missing parameter 'extras'"

def test_coachbuswithedatatype::privatetrip_has_extras():
    assert hasattr(CoachBusWithEDataType::PrivateTrip, "extras")
    descriptor = None
    for klass in CoachBusWithEDataType::PrivateTrip.__mro__:
        if "extras" in klass.__dict__:
            descriptor = klass.__dict__["extras"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::regulartrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::RegularTrip)


def test_coachbuswithedatatype::regulartrip_constructor_exists():
    assert callable(CoachBusWithEDataType::RegularTrip.__init__)


def test_coachbuswithedatatype::regulartrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::RegularTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype::passenger_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Passenger)


def test_coachbuswithedatatype::passenger_constructor_exists():
    assert callable(CoachBusWithEDataType::Passenger.__init__)


def test_coachbuswithedatatype::passenger_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "idCard" in params, "Missing parameter 'idCard'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "name" in params, "Missing parameter 'name'"

def test_coachbuswithedatatype::passenger_has_age():
    assert hasattr(CoachBusWithEDataType::Passenger, "age")
    descriptor = None
    for klass in CoachBusWithEDataType::Passenger.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::passenger_has_idCard():
    assert hasattr(CoachBusWithEDataType::Passenger, "idCard")
    descriptor = None
    for klass in CoachBusWithEDataType::Passenger.__mro__:
        if "idCard" in klass.__dict__:
            descriptor = klass.__dict__["idCard"]
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

def test_coachbuswithedatatype::passenger_has_name():
    assert hasattr(CoachBusWithEDataType::Passenger, "name")
    descriptor = None
    for klass in CoachBusWithEDataType::Passenger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Coach)


def test_coachbuswithedatatype::coach_constructor_exists():
    assert callable(CoachBusWithEDataType::Coach.__init__)


def test_coachbuswithedatatype::coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Coach.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"

def test_coachbuswithedatatype::coach_has_model():
    assert hasattr(CoachBusWithEDataType::Coach, "model")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::coach_has_id():
    assert hasattr(CoachBusWithEDataType::Coach, "id")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::coach_has_name():
    assert hasattr(CoachBusWithEDataType::Coach, "name")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::coach_has_noOfSeats():
    assert hasattr(CoachBusWithEDataType::Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBusWithEDataType::Coach.__mro__:
        if "noOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["noOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::trip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Trip)


def test_coachbuswithedatatype::trip_constructor_exists():
    assert callable(CoachBusWithEDataType::Trip.__init__)


def test_coachbuswithedatatype::trip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Trip.__init__)
    params = list(sig.parameters.keys())
    assert "origin" in params, "Missing parameter 'origin'"
    assert "type" in params, "Missing parameter 'type'"
    assert "number" in params, "Missing parameter 'number'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "name" in params, "Missing parameter 'name'"

def test_coachbuswithedatatype::trip_has_origin():
    assert hasattr(CoachBusWithEDataType::Trip, "origin")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
        if "origin" in klass.__dict__:
            descriptor = klass.__dict__["origin"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::trip_has_type():
    assert hasattr(CoachBusWithEDataType::Trip, "type")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::trip_has_number():
    assert hasattr(CoachBusWithEDataType::Trip, "number")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::trip_has_destination():
    assert hasattr(CoachBusWithEDataType::Trip, "destination")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::trip_has_name():
    assert hasattr(CoachBusWithEDataType::Trip, "name")
    descriptor = None
    for klass in CoachBusWithEDataType::Trip.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Employee)


def test_coachbuswithedatatype::employee_constructor_exists():
    assert callable(CoachBusWithEDataType::Employee.__init__)


def test_coachbuswithedatatype::employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "baseSalary" in params, "Missing parameter 'baseSalary'"
    assert "id" in params, "Missing parameter 'id'"

def test_coachbuswithedatatype::employee_has_baseSalary():
    assert hasattr(CoachBusWithEDataType::Employee, "baseSalary")
    descriptor = None
    for klass in CoachBusWithEDataType::Employee.__mro__:
        if "baseSalary" in klass.__dict__:
            descriptor = klass.__dict__["baseSalary"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::employee_has_id():
    assert hasattr(CoachBusWithEDataType::Employee, "id")
    descriptor = None
    for klass in CoachBusWithEDataType::Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::ticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::Ticket)


def test_coachbuswithedatatype::ticket_constructor_exists():
    assert callable(CoachBusWithEDataType::Ticket.__init__)


def test_coachbuswithedatatype::ticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "isRoundTrip" in params, "Missing parameter 'isRoundTrip'"
    assert "number" in params, "Missing parameter 'number'"
    assert "price" in params, "Missing parameter 'price'"

def test_coachbuswithedatatype::ticket_has_isRoundTrip():
    assert hasattr(CoachBusWithEDataType::Ticket, "isRoundTrip")
    descriptor = None
    for klass in CoachBusWithEDataType::Ticket.__mro__:
        if "isRoundTrip" in klass.__dict__:
            descriptor = klass.__dict__["isRoundTrip"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::ticket_has_number():
    assert hasattr(CoachBusWithEDataType::Ticket, "number")
    descriptor = None
    for klass in CoachBusWithEDataType::Ticket.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::ticket_has_price():
    assert hasattr(CoachBusWithEDataType::Ticket, "price")
    descriptor = None
    for klass in CoachBusWithEDataType::Ticket.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::bookingoffice_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::BookingOffice)


def test_coachbuswithedatatype::bookingoffice_constructor_exists():
    assert callable(CoachBusWithEDataType::BookingOffice.__init__)


def test_coachbuswithedatatype::bookingoffice_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::BookingOffice.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "officeID" in params, "Missing parameter 'officeID'"

def test_coachbuswithedatatype::bookingoffice_has_location():
    assert hasattr(CoachBusWithEDataType::BookingOffice, "location")
    descriptor = None
    for klass in CoachBusWithEDataType::BookingOffice.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::bookingoffice_has_name():
    assert hasattr(CoachBusWithEDataType::BookingOffice, "name")
    descriptor = None
    for klass in CoachBusWithEDataType::BookingOffice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype::bookingoffice_has_officeID():
    assert hasattr(CoachBusWithEDataType::BookingOffice, "officeID")
    descriptor = None
    for klass in CoachBusWithEDataType::BookingOffice.__mro__:
        if "officeID" in klass.__dict__:
            descriptor = klass.__dict__["officeID"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype::securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType::SecurityGuard)


def test_coachbuswithedatatype::securityguard_constructor_exists():
    assert callable(CoachBusWithEDataType::SecurityGuard.__init__)


def test_coachbuswithedatatype::securityguard_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType::SecurityGuard.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"

def test_coachbuswithedatatype::securityguard_has_shift():
    assert hasattr(CoachBusWithEDataType::SecurityGuard, "shift")
    descriptor = None
    for klass in CoachBusWithEDataType::SecurityGuard.__mro__:
        if "shift" in klass.__dict__:
            descriptor = klass.__dict__["shift"]
            break
    assert isinstance(descriptor, property)

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "female",
        "male",
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
Ticket_strategy = st.builds(
    Ticket,
)
CoachBusWithEDataType::ChildTicket_strategy = st.builds(
    CoachBusWithEDataType::ChildTicket,
    isSchoolTrip=
        st.booleans()
)
CoachBusWithEDataType::AdultTicket_strategy = st.builds(
    CoachBusWithEDataType::AdultTicket,
    isElderlyDiscount=
        st.booleans()
)
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType::Manager_strategy = st.builds(
    CoachBusWithEDataType::Manager,
    hasMBA=
        st.booleans()
)
CoachBusWithEDataType::VendingMachine_strategy = st.builds(
    CoachBusWithEDataType::VendingMachine,
    number=
        st.integers()
)
Trip_strategy = st.builds(
    Trip,
)
CoachBusWithEDataType::PrivateTrip_strategy = st.builds(
    CoachBusWithEDataType::PrivateTrip,
    extras=
        safe_text
)
CoachBusWithEDataType::RegularTrip_strategy = st.builds(
    CoachBusWithEDataType::RegularTrip,
)
CoachBusWithEDataType::Passenger_strategy = st.builds(
    CoachBusWithEDataType::Passenger,
    age=
        st.integers(),
    idCard=
        safe_text,
    sex=
        safe_text,
    name=
        safe_text
)
CoachBusWithEDataType::Coach_strategy = st.builds(
    CoachBusWithEDataType::Coach,
    model=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text,
    noOfSeats=
        st.integers()
)
CoachBusWithEDataType::Trip_strategy = st.builds(
    CoachBusWithEDataType::Trip,
    origin=
        safe_text,
    type=
        safe_text,
    number=
        st.integers(),
    destination=
        safe_text,
    name=
        safe_text
)
CoachBusWithEDataType::Employee_strategy = st.builds(
    CoachBusWithEDataType::Employee,
    baseSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    id=
        st.integers()
)
CoachBusWithEDataType::Ticket_strategy = st.builds(
    CoachBusWithEDataType::Ticket,
    isRoundTrip=
        st.booleans(),
    number=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CoachBusWithEDataType::BookingOffice_strategy = st.builds(
    CoachBusWithEDataType::BookingOffice,
    location=
        safe_text,
    name=
        safe_text,
    officeID=
        st.integers()
)
CoachBusWithEDataType::SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType::SecurityGuard,
    shift=
        safe_text
)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)

@given(instance=CoachBusWithEDataType::ChildTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::childticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::ChildTicket)

@given(instance=CoachBusWithEDataType::ChildTicket_strategy)
def test_coachbuswithedatatype::childticket_isSchoolTrip_type(instance):
    assert isinstance(instance.isSchoolTrip, bool)


@given(instance=CoachBusWithEDataType::ChildTicket_strategy)
def test_coachbuswithedatatype::childticket_isSchoolTrip_setter(instance):
    original = instance.isSchoolTrip
    instance.isSchoolTrip = original
    assert instance.isSchoolTrip == original

@given(instance=CoachBusWithEDataType::AdultTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::adultticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::AdultTicket)

@given(instance=CoachBusWithEDataType::AdultTicket_strategy)
def test_coachbuswithedatatype::adultticket_isElderlyDiscount_type(instance):
    assert isinstance(instance.isElderlyDiscount, bool)


@given(instance=CoachBusWithEDataType::AdultTicket_strategy)
def test_coachbuswithedatatype::adultticket_isElderlyDiscount_setter(instance):
    original = instance.isElderlyDiscount
    instance.isElderlyDiscount = original
    assert instance.isElderlyDiscount == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=CoachBusWithEDataType::Manager_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::manager_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Manager)

@given(instance=CoachBusWithEDataType::Manager_strategy)
def test_coachbuswithedatatype::manager_hasMBA_type(instance):
    assert isinstance(instance.hasMBA, bool)


@given(instance=CoachBusWithEDataType::Manager_strategy)
def test_coachbuswithedatatype::manager_hasMBA_setter(instance):
    original = instance.hasMBA
    instance.hasMBA = original
    assert instance.hasMBA == original

@given(instance=CoachBusWithEDataType::VendingMachine_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::vendingmachine_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::VendingMachine)

@given(instance=CoachBusWithEDataType::VendingMachine_strategy)
def test_coachbuswithedatatype::vendingmachine_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=CoachBusWithEDataType::VendingMachine_strategy)
def test_coachbuswithedatatype::vendingmachine_number_setter(instance):
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

@given(instance=CoachBusWithEDataType::PrivateTrip_strategy)
def test_coachbuswithedatatype::privatetrip_extras_type(instance):
    assert isinstance(instance.extras, str)


@given(instance=CoachBusWithEDataType::PrivateTrip_strategy)
def test_coachbuswithedatatype::privatetrip_extras_setter(instance):
    original = instance.extras
    instance.extras = original
    assert instance.extras == original

@given(instance=CoachBusWithEDataType::RegularTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::regulartrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::RegularTrip)

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
def test_coachbuswithedatatype::passenger_idCard_type(instance):
    assert isinstance(instance.idCard, str)


@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_idCard_setter(instance):
    original = instance.idCard
    instance.idCard = original
    assert instance.idCard == original

@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CoachBusWithEDataType::Passenger_strategy)
def test_coachbuswithedatatype::passenger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType::Coach_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Coach)

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_type(instance):
    assert isinstance(instance.noOfSeats, int)


@given(instance=CoachBusWithEDataType::Coach_strategy)
def test_coachbuswithedatatype::coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original

@given(instance=CoachBusWithEDataType::Trip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::trip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Trip)

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_origin_type(instance):
    assert isinstance(instance.origin, str)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_destination_type(instance):
    assert isinstance(instance.destination, str)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original

@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CoachBusWithEDataType::Trip_strategy)
def test_coachbuswithedatatype::trip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType::Employee_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Employee)

@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_baseSalary_type(instance):
    assert isinstance(instance.baseSalary, float)


@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_baseSalary_setter(instance):
    original = instance.baseSalary
    instance.baseSalary = original
    assert instance.baseSalary == original

@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=CoachBusWithEDataType::Employee_strategy)
def test_coachbuswithedatatype::employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CoachBusWithEDataType::Ticket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::ticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::Ticket)

@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_isRoundTrip_type(instance):
    assert isinstance(instance.isRoundTrip, bool)


@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_isRoundTrip_setter(instance):
    original = instance.isRoundTrip
    instance.isRoundTrip = original
    assert instance.isRoundTrip == original

@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=CoachBusWithEDataType::Ticket_strategy)
def test_coachbuswithedatatype::ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::bookingoffice_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::BookingOffice)

@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_officeID_type(instance):
    assert isinstance(instance.officeID, int)


@given(instance=CoachBusWithEDataType::BookingOffice_strategy)
def test_coachbuswithedatatype::bookingoffice_officeID_setter(instance):
    original = instance.officeID
    instance.officeID = original
    assert instance.officeID == original

@given(instance=CoachBusWithEDataType::SecurityGuard_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype::securityguard_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType::SecurityGuard)

@given(instance=CoachBusWithEDataType::SecurityGuard_strategy)
def test_coachbuswithedatatype::securityguard_shift_type(instance):
    assert isinstance(instance.shift, str)


@given(instance=CoachBusWithEDataType::SecurityGuard_strategy)
def test_coachbuswithedatatype::securityguard_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original
