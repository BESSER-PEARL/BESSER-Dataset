import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    List_reservation_,
    List_re_,
    List__,
    CustomerUI,
    Management_UI,
    Restaurant_owner,
    Administrator,
    Staff,
    Reservation_status,
    Table,
    Booking,
    Restaurant_Reservation_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_list_reservation__is_not_abstract():
    assert not inspect.isabstract(List_reservation_)


def test_list_reservation__constructor_exists():
    assert callable(List_reservation_.__init__)


def test_list_reservation__constructor_args():
    sig = inspect.signature(List_reservation_.__init__)
    params = list(sig.parameters.keys())



def test_list_re__is_not_abstract():
    assert not inspect.isabstract(List_re_)


def test_list_re__constructor_exists():
    assert callable(List_re_.__init__)


def test_list_re__constructor_args():
    sig = inspect.signature(List_re_.__init__)
    params = list(sig.parameters.keys())



def test_list___is_not_abstract():
    assert not inspect.isabstract(List__)


def test_list___constructor_exists():
    assert callable(List__.__init__)


def test_list___constructor_args():
    sig = inspect.signature(List__.__init__)
    params = list(sig.parameters.keys())



def test_customerui_is_not_abstract():
    assert not inspect.isabstract(CustomerUI)


def test_customerui_constructor_exists():
    assert callable(CustomerUI.__init__)


def test_customerui_constructor_args():
    sig = inspect.signature(CustomerUI.__init__)
    params = list(sig.parameters.keys())



def test_management_ui_is_not_abstract():
    assert not inspect.isabstract(Management_UI)


def test_management_ui_constructor_exists():
    assert callable(Management_UI.__init__)


def test_management_ui_constructor_args():
    sig = inspect.signature(Management_UI.__init__)
    params = list(sig.parameters.keys())



def test_restaurant_owner_is_not_abstract():
    assert not inspect.isabstract(Restaurant_owner)


def test_restaurant_owner_constructor_exists():
    assert callable(Restaurant_owner.__init__)


def test_restaurant_owner_constructor_args():
    sig = inspect.signature(Restaurant_owner.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "username" in params, "Missing parameter 'username'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_restaurant_owner_has_email():
    assert hasattr(Restaurant_owner, "email")
    descriptor = None
    for klass in Restaurant_owner.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_restaurant_owner_has_username():
    assert hasattr(Restaurant_owner, "username")
    descriptor = None
    for klass in Restaurant_owner.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_restaurant_owner_has_user_id():
    assert hasattr(Restaurant_owner, "user_id")
    descriptor = None
    for klass in Restaurant_owner.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "user_name" in params, "Missing parameter 'user_name'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_administrator_has_email():
    assert hasattr(Administrator, "email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_user_name():
    assert hasattr(Administrator, "user_name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "user_name" in klass.__dict__:
            descriptor = klass.__dict__["user_name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_user_id():
    assert hasattr(Administrator, "user_id")
    descriptor = None
    for klass in Administrator.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_staff_has_name():
    assert hasattr(Staff, "name")
    descriptor = None
    for klass in Staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_type():
    assert hasattr(Staff, "type")
    descriptor = None
    for klass in Staff.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_user_id():
    assert hasattr(Staff, "user_id")
    descriptor = None
    for klass in Staff.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_reservation_status_is_not_abstract():
    assert not inspect.isabstract(Reservation_status)


def test_reservation_status_constructor_exists():
    assert callable(Reservation_status.__init__)


def test_reservation_status_constructor_args():
    sig = inspect.signature(Reservation_status.__init__)
    params = list(sig.parameters.keys())
    assert "reservation" in params, "Missing parameter 'reservation'"
    assert "report_id" in params, "Missing parameter 'report_id'"

def test_reservation_status_has_reservation():
    assert hasattr(Reservation_status, "reservation")
    descriptor = None
    for klass in Reservation_status.__mro__:
        if "reservation" in klass.__dict__:
            descriptor = klass.__dict__["reservation"]
            break
    assert isinstance(descriptor, property)

def test_reservation_status_has_report_id():
    assert hasattr(Reservation_status, "report_id")
    descriptor = None
    for klass in Reservation_status.__mro__:
        if "report_id" in klass.__dict__:
            descriptor = klass.__dict__["report_id"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "table_id" in params, "Missing parameter 'table_id'"
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_table_has_table_id():
    assert hasattr(Table, "table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_id" in klass.__dict__:
            descriptor = klass.__dict__["table_id"]
            break
    assert isinstance(descriptor, property)

def test_table_has_numSeats():
    assert hasattr(Table, "numSeats")
    descriptor = None
    for klass in Table.__mro__:
        if "numSeats" in klass.__dict__:
            descriptor = klass.__dict__["numSeats"]
            break
    assert isinstance(descriptor, property)

def test_table_has_quantity():
    assert hasattr(Table, "quantity")
    descriptor = None
    for klass in Table.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "person" in params, "Missing parameter 'person'"
    assert "customer_id" in params, "Missing parameter 'customer_id'"
    assert "Restaurant_id" in params, "Missing parameter 'Restaurant_id'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"

def test_booking_has_date():
    assert hasattr(Booking, "date")
    descriptor = None
    for klass in Booking.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
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

def test_booking_has_person():
    assert hasattr(Booking, "person")
    descriptor = None
    for klass in Booking.__mro__:
        if "person" in klass.__dict__:
            descriptor = klass.__dict__["person"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_customer_id():
    assert hasattr(Booking, "customer_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "customer_id" in klass.__dict__:
            descriptor = klass.__dict__["customer_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Restaurant_id():
    assert hasattr(Booking, "Restaurant_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "Restaurant_id" in klass.__dict__:
            descriptor = klass.__dict__["Restaurant_id"]
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



def test_restaurant_reservation_system_is_not_abstract():
    assert not inspect.isabstract(Restaurant_Reservation_System)


def test_restaurant_reservation_system_constructor_exists():
    assert callable(Restaurant_Reservation_System.__init__)


def test_restaurant_reservation_system_constructor_args():
    sig = inspect.signature(Restaurant_Reservation_System.__init__)
    params = list(sig.parameters.keys())
    assert "Menu" in params, "Missing parameter 'Menu'"
    assert "bookings" in params, "Missing parameter 'bookings'"

def test_restaurant_reservation_system_has_Menu():
    assert hasattr(Restaurant_Reservation_System, "Menu")
    descriptor = None
    for klass in Restaurant_Reservation_System.__mro__:
        if "Menu" in klass.__dict__:
            descriptor = klass.__dict__["Menu"]
            break
    assert isinstance(descriptor, property)

def test_restaurant_reservation_system_has_bookings():
    assert hasattr(Restaurant_Reservation_System, "bookings")
    descriptor = None
    for klass in Restaurant_Reservation_System.__mro__:
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
List_reservation__strategy = st.builds(
    List_reservation_,
)
List_re__strategy = st.builds(
    List_re_,
)
List___strategy = st.builds(
    List__,
)
CustomerUI_strategy = st.builds(
    CustomerUI,
)
Management_UI_strategy = st.builds(
    Management_UI,
)
Restaurant_owner_strategy = st.builds(
    Restaurant_owner,
    email=
        safe_text,
    username=
        safe_text,
    user_id=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    email=
        safe_text,
    user_name=
        safe_text,
    user_id=
        st.integers()
)
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    type=
        safe_text,
    user_id=
        safe_text
)
Reservation_status_strategy = st.builds(
    Reservation_status,
    reservation=
        st.none(),
    report_id=
        safe_text
)
Table_strategy = st.builds(
    Table,
    table_id=
        safe_text,
    numSeats=
        st.integers(),
    quantity=
        st.integers()
)
Booking_strategy = st.builds(
    Booking,
    date=
        st.dates(),
    reservedTables=
        safe_text,
    person=
        st.integers(),
    customer_id=
        safe_text,
    Restaurant_id=
        safe_text,
    booking_id=
        st.integers(),
    endTime=
        safe_text,
    startTime=
        safe_text
)
Restaurant_Reservation_System_strategy = st.builds(
    Restaurant_Reservation_System,
    Menu=
        safe_text,
    bookings=
        safe_text
)

@given(instance=List_reservation__strategy)
@settings(max_examples=50)
def test_list_reservation__instantiation(instance):
    assert isinstance(instance, List_reservation_)

@given(instance=List_re__strategy)
@settings(max_examples=50)
def test_list_re__instantiation(instance):
    assert isinstance(instance, List_re_)

@given(instance=List___strategy)
@settings(max_examples=50)
def test_list___instantiation(instance):
    assert isinstance(instance, List__)

@given(instance=CustomerUI_strategy)
@settings(max_examples=50)
def test_customerui_instantiation(instance):
    assert isinstance(instance, CustomerUI)

@given(instance=Management_UI_strategy)
@settings(max_examples=50)
def test_management_ui_instantiation(instance):
    assert isinstance(instance, Management_UI)

@given(instance=Restaurant_owner_strategy)
@settings(max_examples=50)
def test_restaurant_owner_instantiation(instance):
    assert isinstance(instance, Restaurant_owner)



@given(instance=Restaurant_owner_strategy)
def test_restaurant_owner_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Restaurant_owner_strategy)
def test_restaurant_owner_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Restaurant_owner_strategy)
def test_restaurant_owner_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_administrator_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original



@given(instance=Administrator_strategy)
def test_administrator_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_staff_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Staff_strategy)
def test_staff_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Reservation_status_strategy)
@settings(max_examples=50)
def test_reservation_status_instantiation(instance):
    assert isinstance(instance, Reservation_status)



@given(instance=Reservation_status_strategy)
def test_reservation_status_reservation_setter(instance):
    original = instance.reservation
    instance.reservation = original
    assert instance.reservation == original



@given(instance=Reservation_status_strategy)
def test_reservation_status_report_id_setter(instance):
    original = instance.report_id
    instance.report_id = original
    assert instance.report_id == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original



@given(instance=Table_strategy)
def test_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_table_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Booking_strategy)
def test_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_booking_person_setter(instance):
    original = instance.person
    instance.person = original
    assert instance.person == original



@given(instance=Booking_strategy)
def test_booking_customer_id_setter(instance):
    original = instance.customer_id
    instance.customer_id = original
    assert instance.customer_id == original



@given(instance=Booking_strategy)
def test_booking_Restaurant_id_setter(instance):
    original = instance.Restaurant_id
    instance.Restaurant_id = original
    assert instance.Restaurant_id == original



@given(instance=Booking_strategy)
def test_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



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

@given(instance=Restaurant_Reservation_System_strategy)
@settings(max_examples=50)
def test_restaurant_reservation_system_instantiation(instance):
    assert isinstance(instance, Restaurant_Reservation_System)



@given(instance=Restaurant_Reservation_System_strategy)
def test_restaurant_reservation_system_Menu_setter(instance):
    original = instance.Menu
    instance.Menu = original
    assert instance.Menu == original



@given(instance=Restaurant_Reservation_System_strategy)
def test_restaurant_reservation_system_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original
