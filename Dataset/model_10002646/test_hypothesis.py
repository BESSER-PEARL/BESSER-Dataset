import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Manager,
    FrontOfHouse,
    CustomerUI,
    StaffUI,
    Waiter,
    Staff,
    Report,
    Table,
    Booking,
    ReservationManagementSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())



def test_frontofhouse_is_not_abstract():
    assert not inspect.isabstract(FrontOfHouse)


def test_frontofhouse_constructor_exists():
    assert callable(FrontOfHouse.__init__)


def test_frontofhouse_constructor_args():
    sig = inspect.signature(FrontOfHouse.__init__)
    params = list(sig.parameters.keys())



def test_customerui_is_not_abstract():
    assert not inspect.isabstract(CustomerUI)


def test_customerui_constructor_exists():
    assert callable(CustomerUI.__init__)


def test_customerui_constructor_args():
    sig = inspect.signature(CustomerUI.__init__)
    params = list(sig.parameters.keys())



def test_staffui_is_not_abstract():
    assert not inspect.isabstract(StaffUI)


def test_staffui_constructor_exists():
    assert callable(StaffUI.__init__)


def test_staffui_constructor_args():
    sig = inspect.signature(StaffUI.__init__)
    params = list(sig.parameters.keys())



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "staffId" in params, "Missing parameter 'staffId'"
    assert "name" in params, "Missing parameter 'name'"

def test_staff_has_type():
    assert hasattr(Staff, "type")
    descriptor = None
    for klass in Staff.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_staffId():
    assert hasattr(Staff, "staffId")
    descriptor = None
    for klass in Staff.__mro__:
        if "staffId" in klass.__dict__:
            descriptor = klass.__dict__["staffId"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_name():
    assert hasattr(Staff, "name")
    descriptor = None
    for klass in Staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())
    assert "report_id" in params, "Missing parameter 'report_id'"
    assert "orders" in params, "Missing parameter 'orders'"

def test_report_has_report_id():
    assert hasattr(Report, "report_id")
    descriptor = None
    for klass in Report.__mro__:
        if "report_id" in klass.__dict__:
            descriptor = klass.__dict__["report_id"]
            break
    assert isinstance(descriptor, property)

def test_report_has_orders():
    assert hasattr(Report, "orders")
    descriptor = None
    for klass in Report.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "table_id" in params, "Missing parameter 'table_id'"
    assert "avaliable" in params, "Missing parameter 'avaliable'"

def test_table_has_numSeats():
    assert hasattr(Table, "numSeats")
    descriptor = None
    for klass in Table.__mro__:
        if "numSeats" in klass.__dict__:
            descriptor = klass.__dict__["numSeats"]
            break
    assert isinstance(descriptor, property)

def test_table_has_table_id():
    assert hasattr(Table, "table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_id" in klass.__dict__:
            descriptor = klass.__dict__["table_id"]
            break
    assert isinstance(descriptor, property)

def test_table_has_avaliable():
    assert hasattr(Table, "avaliable")
    descriptor = None
    for klass in Table.__mro__:
        if "avaliable" in klass.__dict__:
            descriptor = klass.__dict__["avaliable"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"

def test_booking_has_contact_no():
    assert hasattr(Booking, "contact_no")
    descriptor = None
    for klass in Booking.__mro__:
        if "contact_no" in klass.__dict__:
            descriptor = klass.__dict__["contact_no"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_customer_name():
    assert hasattr(Booking, "customer_name")
    descriptor = None
    for klass in Booking.__mro__:
        if "customer_name" in klass.__dict__:
            descriptor = klass.__dict__["customer_name"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_endTime():
    assert hasattr(Booking, "endTime")
    descriptor = None
    for klass in Booking.__mro__:
        if "endTime" in klass.__dict__:
            descriptor = klass.__dict__["endTime"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_startTime():
    assert hasattr(Booking, "startTime")
    descriptor = None
    for klass in Booking.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_booking_id():
    assert hasattr(Booking, "booking_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "booking_id" in klass.__dict__:
            descriptor = klass.__dict__["booking_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_date():
    assert hasattr(Booking, "date")
    descriptor = None
    for klass in Booking.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_email_id():
    assert hasattr(Booking, "email_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "email_id" in klass.__dict__:
            descriptor = klass.__dict__["email_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_reservedTables():
    assert hasattr(Booking, "reservedTables")
    descriptor = None
    for klass in Booking.__mro__:
        if "reservedTables" in klass.__dict__:
            descriptor = klass.__dict__["reservedTables"]
            break
    assert isinstance(descriptor, property)



def test_reservationmanagementsystem_is_not_abstract():
    assert not inspect.isabstract(ReservationManagementSystem)


def test_reservationmanagementsystem_constructor_exists():
    assert callable(ReservationManagementSystem.__init__)


def test_reservationmanagementsystem_constructor_args():
    sig = inspect.signature(ReservationManagementSystem.__init__)
    params = list(sig.parameters.keys())
    assert "bookings" in params, "Missing parameter 'bookings'"

def test_reservationmanagementsystem_has_bookings():
    assert hasattr(ReservationManagementSystem, "bookings")
    descriptor = None
    for klass in ReservationManagementSystem.__mro__:
        if "bookings" in klass.__dict__:
            descriptor = klass.__dict__["bookings"]
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
Manager_strategy = st.builds(
    Manager,
)
FrontOfHouse_strategy = st.builds(
    FrontOfHouse,
)
CustomerUI_strategy = st.builds(
    CustomerUI,
)
StaffUI_strategy = st.builds(
    StaffUI,
)
Waiter_strategy = st.builds(
    Waiter,
)
Staff_strategy = st.builds(
    Staff,
    type=
        safe_text,
    staffId=
        safe_text,
    name=
        safe_text
)
Report_strategy = st.builds(
    Report,
    report_id=
        safe_text,
    orders=
        safe_text
)
Table_strategy = st.builds(
    Table,
    numSeats=
        st.integers(),
    table_id=
        safe_text,
    avaliable=
        st.booleans()
)
Booking_strategy = st.builds(
    Booking,
    contact_no=
        st.integers(),
    customer_name=
        safe_text,
    endTime=
        safe_text,
    startTime=
        safe_text,
    booking_id=
        st.integers(),
    date=
        st.dates(),
    email_id=
        safe_text,
    reservedTables=
        safe_text
)
ReservationManagementSystem_strategy = st.builds(
    ReservationManagementSystem,
    bookings=
        safe_text
)

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)

@given(instance=FrontOfHouse_strategy)
@settings(max_examples=50)
def test_frontofhouse_instantiation(instance):
    assert isinstance(instance, FrontOfHouse)

@given(instance=CustomerUI_strategy)
@settings(max_examples=50)
def test_customerui_instantiation(instance):
    assert isinstance(instance, CustomerUI)

@given(instance=StaffUI_strategy)
@settings(max_examples=50)
def test_staffui_instantiation(instance):
    assert isinstance(instance, StaffUI)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Staff_strategy)
def test_staff_staffId_setter(instance):
    original = instance.staffId
    instance.staffId = original
    assert instance.staffId == original



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)



@given(instance=Report_strategy)
def test_report_report_id_setter(instance):
    original = instance.report_id
    instance.report_id = original
    assert instance.report_id == original



@given(instance=Report_strategy)
def test_report_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original



@given(instance=Table_strategy)
def test_table_avaliable_setter(instance):
    original = instance.avaliable
    instance.avaliable = original
    assert instance.avaliable == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=Booking_strategy)
def test_booking_customer_name_setter(instance):
    original = instance.customer_name
    instance.customer_name = original
    assert instance.customer_name == original



@given(instance=Booking_strategy)
def test_booking_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Booking_strategy)
def test_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Booking_strategy)
def test_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Booking_strategy)
def test_booking_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



@given(instance=Booking_strategy)
def test_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original

@given(instance=ReservationManagementSystem_strategy)
@settings(max_examples=50)
def test_reservationmanagementsystem_instantiation(instance):
    assert isinstance(instance, ReservationManagementSystem)



@given(instance=ReservationManagementSystem_strategy)
def test_reservationmanagementsystem_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original
