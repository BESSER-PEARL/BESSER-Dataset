import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Food,
    Order,
    Table,
    Booking,
    Report,
    RMS,
    Staff,
    Chef,
    Waiter,
    Manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "served" in params, "Missing parameter 'served'"
    assert "type" in params, "Missing parameter 'type'"
    assert "food_Id" in params, "Missing parameter 'food_Id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "prepared" in params, "Missing parameter 'prepared'"
    assert "price" in params, "Missing parameter 'price'"

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_food_has_type():
    assert hasattr(Food, "type")
    descriptor = None
    for klass in Food.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_food_has_food_Id():
    assert hasattr(Food, "food_Id")
    descriptor = None
    for klass in Food.__mro__:
        if "food_Id" in klass.__dict__:
            descriptor = klass.__dict__["food_Id"]
            break
    assert isinstance(descriptor, property)

def test_food_has_description():
    assert hasattr(Food, "description")
    descriptor = None
    for klass in Food.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

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



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "order_Id" in params, "Missing parameter 'order_Id'"
    assert "foodOrdered" in params, "Missing parameter 'foodOrdered'"

def test_order_has_order_Id():
    assert hasattr(Order, "order_Id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_Id" in klass.__dict__:
            descriptor = klass.__dict__["order_Id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodOrdered():
    assert hasattr(Order, "foodOrdered")
    descriptor = None
    for klass in Order.__mro__:
        if "foodOrdered" in klass.__dict__:
            descriptor = klass.__dict__["foodOrdered"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "specialRequest" in params, "Missing parameter 'specialRequest'"
    assert "order" in params, "Missing parameter 'order'"
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "table_Id" in params, "Missing parameter 'table_Id'"
    assert "occupied" in params, "Missing parameter 'occupied'"

def test_table_has_specialRequest():
    assert hasattr(Table, "specialRequest")
    descriptor = None
    for klass in Table.__mro__:
        if "specialRequest" in klass.__dict__:
            descriptor = klass.__dict__["specialRequest"]
            break
    assert isinstance(descriptor, property)

def test_table_has_order():
    assert hasattr(Table, "order")
    descriptor = None
    for klass in Table.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
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

def test_table_has_table_Id():
    assert hasattr(Table, "table_Id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_Id" in klass.__dict__:
            descriptor = klass.__dict__["table_Id"]
            break
    assert isinstance(descriptor, property)

def test_table_has_occupied():
    assert hasattr(Table, "occupied")
    descriptor = None
    for klass in Table.__mro__:
        if "occupied" in klass.__dict__:
            descriptor = klass.__dict__["occupied"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "contact" in params, "Missing parameter 'contact'"
    assert "booking_Id" in params, "Missing parameter 'booking_Id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_booking_has_contact():
    assert hasattr(Booking, "contact")
    descriptor = None
    for klass in Booking.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_booking_Id():
    assert hasattr(Booking, "booking_Id")
    descriptor = None
    for klass in Booking.__mro__:
        if "booking_Id" in klass.__dict__:
            descriptor = klass.__dict__["booking_Id"]
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

def test_booking_has_reservedTables():
    assert hasattr(Booking, "reservedTables")
    descriptor = None
    for klass in Booking.__mro__:
        if "reservedTables" in klass.__dict__:
            descriptor = klass.__dict__["reservedTables"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_type():
    assert hasattr(Booking, "type")
    descriptor = None
    for klass in Booking.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_name():
    assert hasattr(Booking, "name")
    descriptor = None
    for klass in Booking.__mro__:
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
    assert "orders" in params, "Missing parameter 'orders'"
    assert "totalSales" in params, "Missing parameter 'totalSales'"
    assert "profit" in params, "Missing parameter 'profit'"

def test_report_has_orders():
    assert hasattr(Report, "orders")
    descriptor = None
    for klass in Report.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)

def test_report_has_totalSales():
    assert hasattr(Report, "totalSales")
    descriptor = None
    for klass in Report.__mro__:
        if "totalSales" in klass.__dict__:
            descriptor = klass.__dict__["totalSales"]
            break
    assert isinstance(descriptor, property)

def test_report_has_profit():
    assert hasattr(Report, "profit")
    descriptor = None
    for klass in Report.__mro__:
        if "profit" in klass.__dict__:
            descriptor = klass.__dict__["profit"]
            break
    assert isinstance(descriptor, property)



def test_rms_is_not_abstract():
    assert not inspect.isabstract(RMS)


def test_rms_constructor_exists():
    assert callable(RMS.__init__)


def test_rms_constructor_args():
    sig = inspect.signature(RMS.__init__)
    params = list(sig.parameters.keys())
    assert "bookings" in params, "Missing parameter 'bookings'"

def test_rms_has_bookings():
    assert hasattr(RMS, "bookings")
    descriptor = None
    for klass in RMS.__mro__:
        if "bookings" in klass.__dict__:
            descriptor = klass.__dict__["bookings"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "jobType" in params, "Missing parameter 'jobType'"

def test_staff_has_staff_Id():
    assert hasattr(Staff, "staff_Id")
    descriptor = None
    for klass in Staff.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
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

def test_staff_has_contact():
    assert hasattr(Staff, "contact")
    descriptor = None
    for klass in Staff.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_jobType():
    assert hasattr(Staff, "jobType")
    descriptor = None
    for klass in Staff.__mro__:
        if "jobType" in klass.__dict__:
            descriptor = klass.__dict__["jobType"]
            break
    assert isinstance(descriptor, property)



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



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())


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
Food_strategy = st.builds(
    Food,
    name=
        safe_text,
    served=
        st.booleans(),
    type=
        st.integers(),
    food_Id=
        safe_text,
    description=
        safe_text,
    prepared=
        st.booleans(),
    price=
        safe_text
)
Order_strategy = st.builds(
    Order,
    order_Id=
        safe_text,
    foodOrdered=
        st.none()
)
Table_strategy = st.builds(
    Table,
    specialRequest=
        safe_text,
    order=
        safe_text,
    numSeats=
        st.integers(),
    table_Id=
        safe_text,
    occupied=
        st.booleans()
)
Booking_strategy = st.builds(
    Booking,
    contact=
        safe_text,
    booking_Id=
        safe_text,
    date=
        safe_text,
    reservedTables=
        safe_text,
    type=
        st.integers(),
    name=
        safe_text
)
Report_strategy = st.builds(
    Report,
    orders=
        safe_text,
    totalSales=
        safe_text,
    profit=
        safe_text
)
RMS_strategy = st.builds(
    RMS,
    bookings=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    staff_Id=
        safe_text,
    name=
        safe_text,
    contact=
        safe_text,
    jobType=
        st.integers()
)
Chef_strategy = st.builds(
    Chef,
)
Waiter_strategy = st.builds(
    Waiter,
)
Manager_strategy = st.builds(
    Manager,
)

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)



@given(instance=Food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Food_strategy)
def test_food_served_setter(instance):
    original = instance.served
    instance.served = original
    assert instance.served == original



@given(instance=Food_strategy)
def test_food_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Food_strategy)
def test_food_food_Id_setter(instance):
    original = instance.food_Id
    instance.food_Id = original
    assert instance.food_Id == original



@given(instance=Food_strategy)
def test_food_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



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

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_order_Id_setter(instance):
    original = instance.order_Id
    instance.order_Id = original
    assert instance.order_Id == original



@given(instance=Order_strategy)
def test_order_foodOrdered_setter(instance):
    original = instance.foodOrdered
    instance.foodOrdered = original
    assert instance.foodOrdered == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_specialRequest_setter(instance):
    original = instance.specialRequest
    instance.specialRequest = original
    assert instance.specialRequest == original



@given(instance=Table_strategy)
def test_table_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=Table_strategy)
def test_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_table_table_Id_setter(instance):
    original = instance.table_Id
    instance.table_Id = original
    assert instance.table_Id == original



@given(instance=Table_strategy)
def test_table_occupied_setter(instance):
    original = instance.occupied
    instance.occupied = original
    assert instance.occupied == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Booking_strategy)
def test_booking_booking_Id_setter(instance):
    original = instance.booking_Id
    instance.booking_Id = original
    assert instance.booking_Id == original



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
def test_booking_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Booking_strategy)
def test_booking_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_report_totalSales_setter(instance):
    original = instance.totalSales
    instance.totalSales = original
    assert instance.totalSales == original



@given(instance=Report_strategy)
def test_report_profit_setter(instance):
    original = instance.profit
    instance.profit = original
    assert instance.profit == original

@given(instance=RMS_strategy)
@settings(max_examples=50)
def test_rms_instantiation(instance):
    assert isinstance(instance, RMS)



@given(instance=RMS_strategy)
def test_rms_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_staff_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Staff_strategy)
def test_staff_jobType_setter(instance):
    original = instance.jobType
    instance.jobType = original
    assert instance.jobType == original

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)
