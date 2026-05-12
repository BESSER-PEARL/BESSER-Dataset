import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ticket,
    CoachBusWithEDataType_ChildTicket,
    CoachBusWithEDataType_AdultTicket,
    Employee,
    CoachBusWithEDataType_Manager,
    CoachBusWithEDataType_VendingMachine,
    Trip,
    CoachBusWithEDataType_PrivateTrip,
    CoachBusWithEDataType_RegularTrip,
    CoachBusWithEDataType_Passenger,
    CoachBusWithEDataType_Coach,
    CoachBusWithEDataType_Trip,
    CoachBusWithEDataType_Employee,
    CoachBusWithEDataType_Ticket,
    CoachBusWithEDataType_BookingOffice,
    CoachBusWithEDataType_SecurityGuard,
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



def test_coachbuswithedatatype_childticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_ChildTicket)


def test_coachbuswithedatatype_childticket_constructor_exists():
    assert callable(CoachBusWithEDataType_ChildTicket.__init__)


def test_coachbuswithedatatype_childticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_ChildTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isSchoolTrip" in params, "Missing parameter 'isSchoolTrip'"

def test_coachbuswithedatatype_childticket_has_isSchoolTrip():
    assert hasattr(CoachBusWithEDataType_ChildTicket, "isSchoolTrip")
    descriptor = None
    for klass in CoachBusWithEDataType_ChildTicket.__mro__:
        if "isSchoolTrip" in klass.__dict__:
            descriptor = klass.__dict__["isSchoolTrip"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_adultticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_AdultTicket)


def test_coachbuswithedatatype_adultticket_constructor_exists():
    assert callable(CoachBusWithEDataType_AdultTicket.__init__)


def test_coachbuswithedatatype_adultticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_AdultTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isElderlyDiscount" in params, "Missing parameter 'isElderlyDiscount'"

def test_coachbuswithedatatype_adultticket_has_isElderlyDiscount():
    assert hasattr(CoachBusWithEDataType_AdultTicket, "isElderlyDiscount")
    descriptor = None
    for klass in CoachBusWithEDataType_AdultTicket.__mro__:
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



def test_coachbuswithedatatype_manager_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Manager)


def test_coachbuswithedatatype_manager_constructor_exists():
    assert callable(CoachBusWithEDataType_Manager.__init__)


def test_coachbuswithedatatype_manager_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "hasMBA" in params, "Missing parameter 'hasMBA'"

def test_coachbuswithedatatype_manager_has_hasMBA():
    assert hasattr(CoachBusWithEDataType_Manager, "hasMBA")
    descriptor = None
    for klass in CoachBusWithEDataType_Manager.__mro__:
        if "hasMBA" in klass.__dict__:
            descriptor = klass.__dict__["hasMBA"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_vendingmachine_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_VendingMachine)


def test_coachbuswithedatatype_vendingmachine_constructor_exists():
    assert callable(CoachBusWithEDataType_VendingMachine.__init__)


def test_coachbuswithedatatype_vendingmachine_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_VendingMachine.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_coachbuswithedatatype_vendingmachine_has_number():
    assert hasattr(CoachBusWithEDataType_VendingMachine, "number")
    descriptor = None
    for klass in CoachBusWithEDataType_VendingMachine.__mro__:
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
    assert "extras" in params, "Missing parameter 'extras'"

def test_coachbuswithedatatype_privatetrip_has_extras():
    assert hasattr(CoachBusWithEDataType_PrivateTrip, "extras")
    descriptor = None
    for klass in CoachBusWithEDataType_PrivateTrip.__mro__:
        if "extras" in klass.__dict__:
            descriptor = klass.__dict__["extras"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_regulartrip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_RegularTrip)


def test_coachbuswithedatatype_regulartrip_constructor_exists():
    assert callable(CoachBusWithEDataType_RegularTrip.__init__)


def test_coachbuswithedatatype_regulartrip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_RegularTrip.__init__)
    params = list(sig.parameters.keys())



def test_coachbuswithedatatype_passenger_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Passenger)


def test_coachbuswithedatatype_passenger_constructor_exists():
    assert callable(CoachBusWithEDataType_Passenger.__init__)


def test_coachbuswithedatatype_passenger_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "idCard" in params, "Missing parameter 'idCard'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "name" in params, "Missing parameter 'name'"

def test_coachbuswithedatatype_passenger_has_age():
    assert hasattr(CoachBusWithEDataType_Passenger, "age")
    descriptor = None
    for klass in CoachBusWithEDataType_Passenger.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_passenger_has_idCard():
    assert hasattr(CoachBusWithEDataType_Passenger, "idCard")
    descriptor = None
    for klass in CoachBusWithEDataType_Passenger.__mro__:
        if "idCard" in klass.__dict__:
            descriptor = klass.__dict__["idCard"]
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

def test_coachbuswithedatatype_passenger_has_name():
    assert hasattr(CoachBusWithEDataType_Passenger, "name")
    descriptor = None
    for klass in CoachBusWithEDataType_Passenger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Coach)


def test_coachbuswithedatatype_coach_constructor_exists():
    assert callable(CoachBusWithEDataType_Coach.__init__)


def test_coachbuswithedatatype_coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"
    assert "name" in params, "Missing parameter 'name'"
    assert "model" in params, "Missing parameter 'model'"
    assert "id" in params, "Missing parameter 'id'"

def test_coachbuswithedatatype_coach_has_noOfSeats():
    assert hasattr(CoachBusWithEDataType_Coach, "noOfSeats")
    descriptor = None
    for klass in CoachBusWithEDataType_Coach.__mro__:
        if "noOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["noOfSeats"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_coach_has_name():
    assert hasattr(CoachBusWithEDataType_Coach, "name")
    descriptor = None
    for klass in CoachBusWithEDataType_Coach.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_coach_has_model():
    assert hasattr(CoachBusWithEDataType_Coach, "model")
    descriptor = None
    for klass in CoachBusWithEDataType_Coach.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_coach_has_id():
    assert hasattr(CoachBusWithEDataType_Coach, "id")
    descriptor = None
    for klass in CoachBusWithEDataType_Coach.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_trip_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Trip)


def test_coachbuswithedatatype_trip_constructor_exists():
    assert callable(CoachBusWithEDataType_Trip.__init__)


def test_coachbuswithedatatype_trip_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Trip.__init__)
    params = list(sig.parameters.keys())
    assert "origin" in params, "Missing parameter 'origin'"
    assert "number" in params, "Missing parameter 'number'"
    assert "type" in params, "Missing parameter 'type'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "name" in params, "Missing parameter 'name'"

def test_coachbuswithedatatype_trip_has_origin():
    assert hasattr(CoachBusWithEDataType_Trip, "origin")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "origin" in klass.__dict__:
            descriptor = klass.__dict__["origin"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_trip_has_number():
    assert hasattr(CoachBusWithEDataType_Trip, "number")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_trip_has_type():
    assert hasattr(CoachBusWithEDataType_Trip, "type")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_trip_has_destination():
    assert hasattr(CoachBusWithEDataType_Trip, "destination")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_trip_has_name():
    assert hasattr(CoachBusWithEDataType_Trip, "name")
    descriptor = None
    for klass in CoachBusWithEDataType_Trip.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Employee)


def test_coachbuswithedatatype_employee_constructor_exists():
    assert callable(CoachBusWithEDataType_Employee.__init__)


def test_coachbuswithedatatype_employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "baseSalary" in params, "Missing parameter 'baseSalary'"

def test_coachbuswithedatatype_employee_has_id():
    assert hasattr(CoachBusWithEDataType_Employee, "id")
    descriptor = None
    for klass in CoachBusWithEDataType_Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_employee_has_baseSalary():
    assert hasattr(CoachBusWithEDataType_Employee, "baseSalary")
    descriptor = None
    for klass in CoachBusWithEDataType_Employee.__mro__:
        if "baseSalary" in klass.__dict__:
            descriptor = klass.__dict__["baseSalary"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_ticket_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Ticket)


def test_coachbuswithedatatype_ticket_constructor_exists():
    assert callable(CoachBusWithEDataType_Ticket.__init__)


def test_coachbuswithedatatype_ticket_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "isRoundTrip" in params, "Missing parameter 'isRoundTrip'"
    assert "number" in params, "Missing parameter 'number'"
    assert "price" in params, "Missing parameter 'price'"

def test_coachbuswithedatatype_ticket_has_isRoundTrip():
    assert hasattr(CoachBusWithEDataType_Ticket, "isRoundTrip")
    descriptor = None
    for klass in CoachBusWithEDataType_Ticket.__mro__:
        if "isRoundTrip" in klass.__dict__:
            descriptor = klass.__dict__["isRoundTrip"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_ticket_has_number():
    assert hasattr(CoachBusWithEDataType_Ticket, "number")
    descriptor = None
    for klass in CoachBusWithEDataType_Ticket.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_ticket_has_price():
    assert hasattr(CoachBusWithEDataType_Ticket, "price")
    descriptor = None
    for klass in CoachBusWithEDataType_Ticket.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_bookingoffice_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_BookingOffice)


def test_coachbuswithedatatype_bookingoffice_constructor_exists():
    assert callable(CoachBusWithEDataType_BookingOffice.__init__)


def test_coachbuswithedatatype_bookingoffice_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_BookingOffice.__init__)
    params = list(sig.parameters.keys())
    assert "officeID" in params, "Missing parameter 'officeID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"

def test_coachbuswithedatatype_bookingoffice_has_officeID():
    assert hasattr(CoachBusWithEDataType_BookingOffice, "officeID")
    descriptor = None
    for klass in CoachBusWithEDataType_BookingOffice.__mro__:
        if "officeID" in klass.__dict__:
            descriptor = klass.__dict__["officeID"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_bookingoffice_has_name():
    assert hasattr(CoachBusWithEDataType_BookingOffice, "name")
    descriptor = None
    for klass in CoachBusWithEDataType_BookingOffice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coachbuswithedatatype_bookingoffice_has_location():
    assert hasattr(CoachBusWithEDataType_BookingOffice, "location")
    descriptor = None
    for klass in CoachBusWithEDataType_BookingOffice.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_coachbuswithedatatype_securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_SecurityGuard)


def test_coachbuswithedatatype_securityguard_constructor_exists():
    assert callable(CoachBusWithEDataType_SecurityGuard.__init__)


def test_coachbuswithedatatype_securityguard_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_SecurityGuard.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"

def test_coachbuswithedatatype_securityguard_has_shift():
    assert hasattr(CoachBusWithEDataType_SecurityGuard, "shift")
    descriptor = None
    for klass in CoachBusWithEDataType_SecurityGuard.__mro__:
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
CoachBusWithEDataType_ChildTicket_strategy = st.builds(
    CoachBusWithEDataType_ChildTicket,
    isSchoolTrip=
        st.booleans()
)
CoachBusWithEDataType_AdultTicket_strategy = st.builds(
    CoachBusWithEDataType_AdultTicket,
    isElderlyDiscount=
        st.booleans()
)
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType_Manager_strategy = st.builds(
    CoachBusWithEDataType_Manager,
    hasMBA=
        st.booleans()
)
CoachBusWithEDataType_VendingMachine_strategy = st.builds(
    CoachBusWithEDataType_VendingMachine,
    number=
        st.integers()
)
Trip_strategy = st.builds(
    Trip,
)
CoachBusWithEDataType_PrivateTrip_strategy = st.builds(
    CoachBusWithEDataType_PrivateTrip,
    extras=
        safe_text
)
CoachBusWithEDataType_RegularTrip_strategy = st.builds(
    CoachBusWithEDataType_RegularTrip,
)
CoachBusWithEDataType_Passenger_strategy = st.builds(
    CoachBusWithEDataType_Passenger,
    age=
        st.integers(),
    idCard=
        safe_text,
    sex=
        safe_text,
    name=
        safe_text
)
CoachBusWithEDataType_Coach_strategy = st.builds(
    CoachBusWithEDataType_Coach,
    noOfSeats=
        st.integers(),
    name=
        safe_text,
    model=
        safe_text,
    id=
        st.integers()
)
CoachBusWithEDataType_Trip_strategy = st.builds(
    CoachBusWithEDataType_Trip,
    origin=
        safe_text,
    number=
        st.integers(),
    type=
        safe_text,
    destination=
        safe_text,
    name=
        safe_text
)
CoachBusWithEDataType_Employee_strategy = st.builds(
    CoachBusWithEDataType_Employee,
    id=
        st.integers(),
    baseSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CoachBusWithEDataType_Ticket_strategy = st.builds(
    CoachBusWithEDataType_Ticket,
    isRoundTrip=
        st.booleans(),
    number=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CoachBusWithEDataType_BookingOffice_strategy = st.builds(
    CoachBusWithEDataType_BookingOffice,
    officeID=
        st.integers(),
    name=
        safe_text,
    location=
        safe_text
)
CoachBusWithEDataType_SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType_SecurityGuard,
    shift=
        safe_text
)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)

@given(instance=CoachBusWithEDataType_ChildTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_childticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_ChildTicket)



@given(instance=CoachBusWithEDataType_ChildTicket_strategy)
def test_coachbuswithedatatype_childticket_isSchoolTrip_setter(instance):
    original = instance.isSchoolTrip
    instance.isSchoolTrip = original
    assert instance.isSchoolTrip == original

@given(instance=CoachBusWithEDataType_AdultTicket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_adultticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_AdultTicket)



@given(instance=CoachBusWithEDataType_AdultTicket_strategy)
def test_coachbuswithedatatype_adultticket_isElderlyDiscount_setter(instance):
    original = instance.isElderlyDiscount
    instance.isElderlyDiscount = original
    assert instance.isElderlyDiscount == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=CoachBusWithEDataType_Manager_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_manager_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Manager)



@given(instance=CoachBusWithEDataType_Manager_strategy)
def test_coachbuswithedatatype_manager_hasMBA_setter(instance):
    original = instance.hasMBA
    instance.hasMBA = original
    assert instance.hasMBA == original

@given(instance=CoachBusWithEDataType_VendingMachine_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_vendingmachine_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_VendingMachine)



@given(instance=CoachBusWithEDataType_VendingMachine_strategy)
def test_coachbuswithedatatype_vendingmachine_number_setter(instance):
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



@given(instance=CoachBusWithEDataType_PrivateTrip_strategy)
def test_coachbuswithedatatype_privatetrip_extras_setter(instance):
    original = instance.extras
    instance.extras = original
    assert instance.extras == original

@given(instance=CoachBusWithEDataType_RegularTrip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_regulartrip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_RegularTrip)

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
def test_coachbuswithedatatype_passenger_idCard_setter(instance):
    original = instance.idCard
    instance.idCard = original
    assert instance.idCard == original



@given(instance=CoachBusWithEDataType_Passenger_strategy)
def test_coachbuswithedatatype_passenger_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=CoachBusWithEDataType_Passenger_strategy)
def test_coachbuswithedatatype_passenger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType_Coach_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Coach)



@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_coachbuswithedatatype_coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original



@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_coachbuswithedatatype_coach_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_coachbuswithedatatype_coach_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_coachbuswithedatatype_coach_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CoachBusWithEDataType_Trip_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_trip_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Trip)



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=CoachBusWithEDataType_Trip_strategy)
def test_coachbuswithedatatype_trip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CoachBusWithEDataType_Employee_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Employee)



@given(instance=CoachBusWithEDataType_Employee_strategy)
def test_coachbuswithedatatype_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=CoachBusWithEDataType_Employee_strategy)
def test_coachbuswithedatatype_employee_baseSalary_setter(instance):
    original = instance.baseSalary
    instance.baseSalary = original
    assert instance.baseSalary == original

@given(instance=CoachBusWithEDataType_Ticket_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_ticket_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Ticket)



@given(instance=CoachBusWithEDataType_Ticket_strategy)
def test_coachbuswithedatatype_ticket_isRoundTrip_setter(instance):
    original = instance.isRoundTrip
    instance.isRoundTrip = original
    assert instance.isRoundTrip == original



@given(instance=CoachBusWithEDataType_Ticket_strategy)
def test_coachbuswithedatatype_ticket_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=CoachBusWithEDataType_Ticket_strategy)
def test_coachbuswithedatatype_ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=CoachBusWithEDataType_BookingOffice_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_bookingoffice_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_BookingOffice)



@given(instance=CoachBusWithEDataType_BookingOffice_strategy)
def test_coachbuswithedatatype_bookingoffice_officeID_setter(instance):
    original = instance.officeID
    instance.officeID = original
    assert instance.officeID == original



@given(instance=CoachBusWithEDataType_BookingOffice_strategy)
def test_coachbuswithedatatype_bookingoffice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBusWithEDataType_BookingOffice_strategy)
def test_coachbuswithedatatype_bookingoffice_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CoachBusWithEDataType_SecurityGuard_strategy)
@settings(max_examples=50)
def test_coachbuswithedatatype_securityguard_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_SecurityGuard)



@given(instance=CoachBusWithEDataType_SecurityGuard_strategy)
def test_coachbuswithedatatype_securityguard_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original
