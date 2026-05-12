import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    Table_booking_time,
    Booking,
    Payment,
    Table,
    Restaurant,
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
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "email" in params, "Missing parameter 'email'"
    assert "cust_id" in params, "Missing parameter 'cust_id'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_mobile():
    assert hasattr(Customer, "mobile")
    descriptor = None
    for klass in Customer.__mro__:
        if "mobile" in klass.__dict__:
            descriptor = klass.__dict__["mobile"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_cust_id():
    assert hasattr(Customer, "cust_id")
    descriptor = None
    for klass in Customer.__mro__:
        if "cust_id" in klass.__dict__:
            descriptor = klass.__dict__["cust_id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_table_booking_time_is_not_abstract():
    assert not inspect.isabstract(Table_booking_time)


def test_table_booking_time_constructor_exists():
    assert callable(Table_booking_time.__init__)


def test_table_booking_time_constructor_args():
    sig = inspect.signature(Table_booking_time.__init__)
    params = list(sig.parameters.keys())
    assert "end_time" in params, "Missing parameter 'end_time'"
    assert "start_time" in params, "Missing parameter 'start_time'"

def test_table_booking_time_has_end_time():
    assert hasattr(Table_booking_time, "end_time")
    descriptor = None
    for klass in Table_booking_time.__mro__:
        if "end_time" in klass.__dict__:
            descriptor = klass.__dict__["end_time"]
            break
    assert isinstance(descriptor, property)

def test_table_booking_time_has_start_time():
    assert hasattr(Table_booking_time, "start_time")
    descriptor = None
    for klass in Table_booking_time.__mro__:
        if "start_time" in klass.__dict__:
            descriptor = klass.__dict__["start_time"]
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
    assert "table_number" in params, "Missing parameter 'table_number'"
    assert "arrival_time" in params, "Missing parameter 'arrival_time'"

def test_booking_has_customer_name():
    assert hasattr(Booking, "customer_name")
    descriptor = None
    for klass in Booking.__mro__:
        if "customer_name" in klass.__dict__:
            descriptor = klass.__dict__["customer_name"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_table_number():
    assert hasattr(Booking, "table_number")
    descriptor = None
    for klass in Booking.__mro__:
        if "table_number" in klass.__dict__:
            descriptor = klass.__dict__["table_number"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_arrival_time():
    assert hasattr(Booking, "arrival_time")
    descriptor = None
    for klass in Booking.__mro__:
        if "arrival_time" in klass.__dict__:
            descriptor = klass.__dict__["arrival_time"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "pay_hotel" in params, "Missing parameter 'pay_hotel'"
    assert "credit_card" in params, "Missing parameter 'credit_card'"
    assert "debit_card" in params, "Missing parameter 'debit_card'"
    assert "paytm" in params, "Missing parameter 'paytm'"

def test_payment_has_pay_hotel():
    assert hasattr(Payment, "pay_hotel")
    descriptor = None
    for klass in Payment.__mro__:
        if "pay_hotel" in klass.__dict__:
            descriptor = klass.__dict__["pay_hotel"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_credit_card():
    assert hasattr(Payment, "credit_card")
    descriptor = None
    for klass in Payment.__mro__:
        if "credit_card" in klass.__dict__:
            descriptor = klass.__dict__["credit_card"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_debit_card():
    assert hasattr(Payment, "debit_card")
    descriptor = None
    for klass in Payment.__mro__:
        if "debit_card" in klass.__dict__:
            descriptor = klass.__dict__["debit_card"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paytm():
    assert hasattr(Payment, "paytm")
    descriptor = None
    for klass in Payment.__mro__:
        if "paytm" in klass.__dict__:
            descriptor = klass.__dict__["paytm"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "total_person" in params, "Missing parameter 'total_person'"
    assert "table_number" in params, "Missing parameter 'table_number'"

def test_table_has_total_person():
    assert hasattr(Table, "total_person")
    descriptor = None
    for klass in Table.__mro__:
        if "total_person" in klass.__dict__:
            descriptor = klass.__dict__["total_person"]
            break
    assert isinstance(descriptor, property)

def test_table_has_table_number():
    assert hasattr(Table, "table_number")
    descriptor = None
    for klass in Table.__mro__:
        if "table_number" in klass.__dict__:
            descriptor = klass.__dict__["table_number"]
            break
    assert isinstance(descriptor, property)



def test_restaurant_is_not_abstract():
    assert not inspect.isabstract(Restaurant)


def test_restaurant_constructor_exists():
    assert callable(Restaurant.__init__)


def test_restaurant_constructor_args():
    sig = inspect.signature(Restaurant.__init__)
    params = list(sig.parameters.keys())
    assert "booking" in params, "Missing parameter 'booking'"
    assert "time" in params, "Missing parameter 'time'"

def test_restaurant_has_booking():
    assert hasattr(Restaurant, "booking")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_restaurant_has_time():
    assert hasattr(Restaurant, "time")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
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
    mobile=
        st.integers(),
    email=
        safe_text,
    cust_id=
        st.integers(),
    Address=
        safe_text,
    name=
        safe_text
)
Table_booking_time_strategy = st.builds(
    Table_booking_time,
    end_time=
        st.integers(),
    start_time=
        st.integers()
)
Booking_strategy = st.builds(
    Booking,
    customer_name=
        safe_text,
    table_number=
        st.integers(),
    arrival_time=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    pay_hotel=
        st.integers(),
    credit_card=
        st.integers(),
    debit_card=
        st.integers(),
    paytm=
        st.integers()
)
Table_strategy = st.builds(
    Table,
    total_person=
        st.integers(),
    table_number=
        st.integers()
)
Restaurant_strategy = st.builds(
    Restaurant,
    booking=
        st.integers(),
    time=
        st.integers()
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_cust_id_setter(instance):
    original = instance.cust_id
    instance.cust_id = original
    assert instance.cust_id == original



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Table_booking_time_strategy)
@settings(max_examples=50)
def test_table_booking_time_instantiation(instance):
    assert isinstance(instance, Table_booking_time)



@given(instance=Table_booking_time_strategy)
def test_table_booking_time_end_time_setter(instance):
    original = instance.end_time
    instance.end_time = original
    assert instance.end_time == original



@given(instance=Table_booking_time_strategy)
def test_table_booking_time_start_time_setter(instance):
    original = instance.start_time
    instance.start_time = original
    assert instance.start_time == original

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
def test_booking_table_number_setter(instance):
    original = instance.table_number
    instance.table_number = original
    assert instance.table_number == original



@given(instance=Booking_strategy)
def test_booking_arrival_time_setter(instance):
    original = instance.arrival_time
    instance.arrival_time = original
    assert instance.arrival_time == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_pay_hotel_setter(instance):
    original = instance.pay_hotel
    instance.pay_hotel = original
    assert instance.pay_hotel == original



@given(instance=Payment_strategy)
def test_payment_credit_card_setter(instance):
    original = instance.credit_card
    instance.credit_card = original
    assert instance.credit_card == original



@given(instance=Payment_strategy)
def test_payment_debit_card_setter(instance):
    original = instance.debit_card
    instance.debit_card = original
    assert instance.debit_card == original



@given(instance=Payment_strategy)
def test_payment_paytm_setter(instance):
    original = instance.paytm
    instance.paytm = original
    assert instance.paytm == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_total_person_setter(instance):
    original = instance.total_person
    instance.total_person = original
    assert instance.total_person == original



@given(instance=Table_strategy)
def test_table_table_number_setter(instance):
    original = instance.table_number
    instance.table_number = original
    assert instance.table_number == original

@given(instance=Restaurant_strategy)
@settings(max_examples=50)
def test_restaurant_instantiation(instance):
    assert isinstance(instance, Restaurant)



@given(instance=Restaurant_strategy)
def test_restaurant_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original



@given(instance=Restaurant_strategy)
def test_restaurant_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original
