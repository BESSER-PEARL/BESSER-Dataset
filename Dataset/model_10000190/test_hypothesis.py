import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CustomerUI,
    StaffUI,
    Chef,
    Waiter,
    Staff,
    Food,
    Order,
    Report,
    Table,
    Booking,
    ReservationManagementSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
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
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "staffId" in params, "Missing parameter 'staffId'"

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

def test_staff_has_staffId():
    assert hasattr(Staff, "staffId")
    descriptor = None
    for klass in Staff.__mro__:
        if "staffId" in klass.__dict__:
            descriptor = klass.__dict__["staffId"]
            break
    assert isinstance(descriptor, property)



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "prepared" in params, "Missing parameter 'prepared'"
    assert "price" in params, "Missing parameter 'price'"
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "served" in params, "Missing parameter 'served'"
    assert "name" in params, "Missing parameter 'name'"

def test_food_has_prepared():
    assert hasattr(Food, "prepared")
    descriptor = None
    for klass in Food.__mro__:
        if "prepared" in klass.__dict__:
            descriptor = klass.__dict__["prepared"]
            break
    assert isinstance(descriptor, property)

def test_food_has_price():
    assert hasattr(Food, "price")
    descriptor = None
    for klass in Food.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_food_has_food_id():
    assert hasattr(Food, "food_id")
    descriptor = None
    for klass in Food.__mro__:
        if "food_id" in klass.__dict__:
            descriptor = klass.__dict__["food_id"]
            break
    assert isinstance(descriptor, property)

def test_food_has_served():
    assert hasattr(Food, "served")
    descriptor = None
    for klass in Food.__mro__:
        if "served" in klass.__dict__:
            descriptor = klass.__dict__["served"]
            break
    assert isinstance(descriptor, property)

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "foodList" in params, "Missing parameter 'foodList'"

def test_order_has_order_id():
    assert hasattr(Order, "order_id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodList():
    assert hasattr(Order, "foodList")
    descriptor = None
    for klass in Order.__mro__:
        if "foodList" in klass.__dict__:
            descriptor = klass.__dict__["foodList"]
            break
    assert isinstance(descriptor, property)



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())
    assert "orders" in params, "Missing parameter 'orders'"
    assert "report_id" in params, "Missing parameter 'report_id'"

def test_report_has_orders():
    assert hasattr(Report, "orders")
    descriptor = None
    for klass in Report.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)

def test_report_has_report_id():
    assert hasattr(Report, "report_id")
    descriptor = None
    for klass in Report.__mro__:
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
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "date" in params, "Missing parameter 'date'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"

def test_booking_has_customer_name():
    assert hasattr(Booking, "customer_name")
    descriptor = None
    for klass in Booking.__mro__:
        if "customer_name" in klass.__dict__:
            descriptor = klass.__dict__["customer_name"]
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

def test_booking_has_contact_no():
    assert hasattr(Booking, "contact_no")
    descriptor = None
    for klass in Booking.__mro__:
        if "contact_no" in klass.__dict__:
            descriptor = klass.__dict__["contact_no"]
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

def test_booking_has_date():
    assert hasattr(Booking, "date")
    descriptor = None
    for klass in Booking.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
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

def test_booking_has_email_id():
    assert hasattr(Booking, "email_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "email_id" in klass.__dict__:
            descriptor = klass.__dict__["email_id"]
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
CustomerUI_strategy = st.builds(
    CustomerUI,
)
StaffUI_strategy = st.builds(
    StaffUI,
)
Chef_strategy = st.builds(
    Chef,
)
Waiter_strategy = st.builds(
    Waiter,
)
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    type=
        safe_text,
    staffId=
        safe_text
)
Food_strategy = st.builds(
    Food,
    prepared=
        st.booleans(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    food_id=
        safe_text,
    served=
        st.booleans(),
    name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    order_id=
        safe_text,
    foodList=
        safe_text
)
Report_strategy = st.builds(
    Report,
    orders=
        safe_text,
    report_id=
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
    customer_name=
        safe_text,
    reservedTables=
        safe_text,
    contact_no=
        st.integers(),
    startTime=
        safe_text,
    date=
        st.dates(),
    endTime=
        safe_text,
    email_id=
        safe_text,
    booking_id=
        st.integers()
)
ReservationManagementSystem_strategy = st.builds(
    ReservationManagementSystem,
    bookings=
        safe_text
)

@given(instance=CustomerUI_strategy)
@settings(max_examples=50)
def test_customerui_instantiation(instance):
    assert isinstance(instance, CustomerUI)

@given(instance=StaffUI_strategy)
@settings(max_examples=50)
def test_staffui_instantiation(instance):
    assert isinstance(instance, StaffUI)

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

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
def test_staff_staffId_setter(instance):
    original = instance.staffId
    instance.staffId = original
    assert instance.staffId == original

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)



@given(instance=Food_strategy)
def test_food_prepared_setter(instance):
    original = instance.prepared
    instance.prepared = original
    assert instance.prepared == original



@given(instance=Food_strategy)
def test_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Food_strategy)
def test_food_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Food_strategy)
def test_food_served_setter(instance):
    original = instance.served
    instance.served = original
    assert instance.served == original



@given(instance=Food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Order_strategy)
def test_order_foodList_setter(instance):
    original = instance.foodList
    instance.foodList = original
    assert instance.foodList == original

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)



@given(instance=Report_strategy)
def test_report_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original



@given(instance=Report_strategy)
def test_report_report_id_setter(instance):
    original = instance.report_id
    instance.report_id = original
    assert instance.report_id == original

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
def test_booking_customer_name_setter(instance):
    original = instance.customer_name
    instance.customer_name = original
    assert instance.customer_name == original



@given(instance=Booking_strategy)
def test_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_booking_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=Booking_strategy)
def test_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Booking_strategy)
def test_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Booking_strategy)
def test_booking_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Booking_strategy)
def test_booking_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



@given(instance=Booking_strategy)
def test_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original

@given(instance=ReservationManagementSystem_strategy)
@settings(max_examples=50)
def test_reservationmanagementsystem_instantiation(instance):
    assert isinstance(instance, ReservationManagementSystem)



@given(instance=ReservationManagementSystem_strategy)
def test_reservationmanagementsystem_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original
