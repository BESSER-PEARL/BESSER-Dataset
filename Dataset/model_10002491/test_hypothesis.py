import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    Restaurants,
    CustomerUI,
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



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "c_id" in params, "Missing parameter 'c_id'"
    assert "c_email" in params, "Missing parameter 'c_email'"
    assert "c_mobile" in params, "Missing parameter 'c_mobile'"
    assert "c_address" in params, "Missing parameter 'c_address'"
    assert "c_name" in params, "Missing parameter 'c_name'"

def test_customer_has_c_id():
    assert hasattr(Customer, "c_id")
    descriptor = None
    for klass in Customer.__mro__:
        if "c_id" in klass.__dict__:
            descriptor = klass.__dict__["c_id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_c_email():
    assert hasattr(Customer, "c_email")
    descriptor = None
    for klass in Customer.__mro__:
        if "c_email" in klass.__dict__:
            descriptor = klass.__dict__["c_email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_c_mobile():
    assert hasattr(Customer, "c_mobile")
    descriptor = None
    for klass in Customer.__mro__:
        if "c_mobile" in klass.__dict__:
            descriptor = klass.__dict__["c_mobile"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_c_address():
    assert hasattr(Customer, "c_address")
    descriptor = None
    for klass in Customer.__mro__:
        if "c_address" in klass.__dict__:
            descriptor = klass.__dict__["c_address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_c_name():
    assert hasattr(Customer, "c_name")
    descriptor = None
    for klass in Customer.__mro__:
        if "c_name" in klass.__dict__:
            descriptor = klass.__dict__["c_name"]
            break
    assert isinstance(descriptor, property)



def test_restaurants_is_not_abstract():
    assert not inspect.isabstract(Restaurants)


def test_restaurants_constructor_exists():
    assert callable(Restaurants.__init__)


def test_restaurants_constructor_args():
    sig = inspect.signature(Restaurants.__init__)
    params = list(sig.parameters.keys())
    assert "r_address" in params, "Missing parameter 'r_address'"
    assert "r_name" in params, "Missing parameter 'r_name'"
    assert "r_cuisine" in params, "Missing parameter 'r_cuisine'"
    assert "r_ID" in params, "Missing parameter 'r_ID'"
    assert "r_contact" in params, "Missing parameter 'r_contact'"

def test_restaurants_has_r_address():
    assert hasattr(Restaurants, "r_address")
    descriptor = None
    for klass in Restaurants.__mro__:
        if "r_address" in klass.__dict__:
            descriptor = klass.__dict__["r_address"]
            break
    assert isinstance(descriptor, property)

def test_restaurants_has_r_name():
    assert hasattr(Restaurants, "r_name")
    descriptor = None
    for klass in Restaurants.__mro__:
        if "r_name" in klass.__dict__:
            descriptor = klass.__dict__["r_name"]
            break
    assert isinstance(descriptor, property)

def test_restaurants_has_r_cuisine():
    assert hasattr(Restaurants, "r_cuisine")
    descriptor = None
    for klass in Restaurants.__mro__:
        if "r_cuisine" in klass.__dict__:
            descriptor = klass.__dict__["r_cuisine"]
            break
    assert isinstance(descriptor, property)

def test_restaurants_has_r_ID():
    assert hasattr(Restaurants, "r_ID")
    descriptor = None
    for klass in Restaurants.__mro__:
        if "r_ID" in klass.__dict__:
            descriptor = klass.__dict__["r_ID"]
            break
    assert isinstance(descriptor, property)

def test_restaurants_has_r_contact():
    assert hasattr(Restaurants, "r_contact")
    descriptor = None
    for klass in Restaurants.__mro__:
        if "r_contact" in klass.__dict__:
            descriptor = klass.__dict__["r_contact"]
            break
    assert isinstance(descriptor, property)



def test_customerui_is_not_abstract():
    assert not inspect.isabstract(CustomerUI)


def test_customerui_constructor_exists():
    assert callable(CustomerUI.__init__)


def test_customerui_constructor_args():
    sig = inspect.signature(CustomerUI.__init__)
    params = list(sig.parameters.keys())



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "price" in params, "Missing parameter 'price'"
    assert "served" in params, "Missing parameter 'served'"
    assert "prepared" in params, "Missing parameter 'prepared'"

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_food_has_price():
    assert hasattr(Food, "price")
    descriptor = None
    for klass in Food.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
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

def test_food_has_prepared():
    assert hasattr(Food, "prepared")
    descriptor = None
    for klass in Food.__mro__:
        if "prepared" in klass.__dict__:
            descriptor = klass.__dict__["prepared"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "foodList" in params, "Missing parameter 'foodList'"
    assert "order_id" in params, "Missing parameter 'order_id'"

def test_order_has_foodList():
    assert hasattr(Order, "foodList")
    descriptor = None
    for klass in Order.__mro__:
        if "foodList" in klass.__dict__:
            descriptor = klass.__dict__["foodList"]
            break
    assert isinstance(descriptor, property)

def test_order_has_order_id():
    assert hasattr(Order, "order_id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
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
    assert "avaliable" in params, "Missing parameter 'avaliable'"
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "table_id" in params, "Missing parameter 'table_id'"

def test_table_has_avaliable():
    assert hasattr(Table, "avaliable")
    descriptor = None
    for klass in Table.__mro__:
        if "avaliable" in klass.__dict__:
            descriptor = klass.__dict__["avaliable"]
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

def test_table_has_table_id():
    assert hasattr(Table, "table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_id" in klass.__dict__:
            descriptor = klass.__dict__["table_id"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "b_id" in params, "Missing parameter 'b_id'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "endTime" in params, "Missing parameter 'endTime'"

def test_booking_has_b_id():
    assert hasattr(Booking, "b_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "b_id" in klass.__dict__:
            descriptor = klass.__dict__["b_id"]
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

def test_booking_has_startTime():
    assert hasattr(Booking, "startTime")
    descriptor = None
    for klass in Booking.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
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
Customer_strategy = st.builds(
    Customer,
    c_id=
        st.integers(),
    c_email=
        safe_text,
    c_mobile=
        st.integers(),
    c_address=
        safe_text,
    c_name=
        safe_text
)
Restaurants_strategy = st.builds(
    Restaurants,
    r_address=
        safe_text,
    r_name=
        safe_text,
    r_cuisine=
        safe_text,
    r_ID=
        st.integers(),
    r_contact=
        st.integers()
)
CustomerUI_strategy = st.builds(
    CustomerUI,
)
Food_strategy = st.builds(
    Food,
    name=
        safe_text,
    food_id=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    served=
        st.booleans(),
    prepared=
        st.booleans()
)
Order_strategy = st.builds(
    Order,
    foodList=
        safe_text,
    order_id=
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
    avaliable=
        st.booleans(),
    numSeats=
        st.integers(),
    table_id=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    b_id=
        st.integers(),
    email_id=
        safe_text,
    date=
        st.dates(),
    reservedTables=
        safe_text,
    startTime=
        safe_text,
    contact_no=
        st.integers(),
    customer_name=
        safe_text,
    endTime=
        safe_text
)
ReservationManagementSystem_strategy = st.builds(
    ReservationManagementSystem,
    bookings=
        safe_text
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_c_id_setter(instance):
    original = instance.c_id
    instance.c_id = original
    assert instance.c_id == original



@given(instance=Customer_strategy)
def test_customer_c_email_setter(instance):
    original = instance.c_email
    instance.c_email = original
    assert instance.c_email == original



@given(instance=Customer_strategy)
def test_customer_c_mobile_setter(instance):
    original = instance.c_mobile
    instance.c_mobile = original
    assert instance.c_mobile == original



@given(instance=Customer_strategy)
def test_customer_c_address_setter(instance):
    original = instance.c_address
    instance.c_address = original
    assert instance.c_address == original



@given(instance=Customer_strategy)
def test_customer_c_name_setter(instance):
    original = instance.c_name
    instance.c_name = original
    assert instance.c_name == original

@given(instance=Restaurants_strategy)
@settings(max_examples=50)
def test_restaurants_instantiation(instance):
    assert isinstance(instance, Restaurants)



@given(instance=Restaurants_strategy)
def test_restaurants_r_address_setter(instance):
    original = instance.r_address
    instance.r_address = original
    assert instance.r_address == original



@given(instance=Restaurants_strategy)
def test_restaurants_r_name_setter(instance):
    original = instance.r_name
    instance.r_name = original
    assert instance.r_name == original



@given(instance=Restaurants_strategy)
def test_restaurants_r_cuisine_setter(instance):
    original = instance.r_cuisine
    instance.r_cuisine = original
    assert instance.r_cuisine == original



@given(instance=Restaurants_strategy)
def test_restaurants_r_ID_setter(instance):
    original = instance.r_ID
    instance.r_ID = original
    assert instance.r_ID == original



@given(instance=Restaurants_strategy)
def test_restaurants_r_contact_setter(instance):
    original = instance.r_contact
    instance.r_contact = original
    assert instance.r_contact == original

@given(instance=CustomerUI_strategy)
@settings(max_examples=50)
def test_customerui_instantiation(instance):
    assert isinstance(instance, CustomerUI)

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
def test_food_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Food_strategy)
def test_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Food_strategy)
def test_food_served_setter(instance):
    original = instance.served
    instance.served = original
    assert instance.served == original



@given(instance=Food_strategy)
def test_food_prepared_setter(instance):
    original = instance.prepared
    instance.prepared = original
    assert instance.prepared == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_foodList_setter(instance):
    original = instance.foodList
    instance.foodList = original
    assert instance.foodList == original



@given(instance=Order_strategy)
def test_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original

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
def test_table_avaliable_setter(instance):
    original = instance.avaliable
    instance.avaliable = original
    assert instance.avaliable == original



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

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_b_id_setter(instance):
    original = instance.b_id
    instance.b_id = original
    assert instance.b_id == original



@given(instance=Booking_strategy)
def test_booking_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



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
def test_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



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

@given(instance=ReservationManagementSystem_strategy)
@settings(max_examples=50)
def test_reservationmanagementsystem_instantiation(instance):
    assert isinstance(instance, ReservationManagementSystem)



@given(instance=ReservationManagementSystem_strategy)
def test_reservationmanagementsystem_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original
