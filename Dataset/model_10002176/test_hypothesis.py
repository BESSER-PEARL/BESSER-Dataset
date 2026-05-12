import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Staff,
    Foods,
    Reservation,
    Order,
    Class,
    Order_management_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "staffid" in params, "Missing parameter 'staffid'"
    assert "name" in params, "Missing parameter 'name'"

def test_staff_has_staffid():
    assert hasattr(Staff, "staffid")
    descriptor = None
    for klass in Staff.__mro__:
        if "staffid" in klass.__dict__:
            descriptor = klass.__dict__["staffid"]
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



def test_foods_is_not_abstract():
    assert not inspect.isabstract(Foods)


def test_foods_constructor_exists():
    assert callable(Foods.__init__)


def test_foods_constructor_args():
    sig = inspect.signature(Foods.__init__)
    params = list(sig.parameters.keys())
    assert "Catogory" in params, "Missing parameter 'Catogory'"
    assert "price" in params, "Missing parameter 'price'"
    assert "Foodname" in params, "Missing parameter 'Foodname'"
    assert "Ready" in params, "Missing parameter 'Ready'"

def test_foods_has_Catogory():
    assert hasattr(Foods, "Catogory")
    descriptor = None
    for klass in Foods.__mro__:
        if "Catogory" in klass.__dict__:
            descriptor = klass.__dict__["Catogory"]
            break
    assert isinstance(descriptor, property)

def test_foods_has_price():
    assert hasattr(Foods, "price")
    descriptor = None
    for klass in Foods.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_foods_has_Foodname():
    assert hasattr(Foods, "Foodname")
    descriptor = None
    for klass in Foods.__mro__:
        if "Foodname" in klass.__dict__:
            descriptor = klass.__dict__["Foodname"]
            break
    assert isinstance(descriptor, property)

def test_foods_has_Ready():
    assert hasattr(Foods, "Ready")
    descriptor = None
    for klass in Foods.__mro__:
        if "Ready" in klass.__dict__:
            descriptor = klass.__dict__["Ready"]
            break
    assert isinstance(descriptor, property)



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(Reservation)


def test_reservation_constructor_exists():
    assert callable(Reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "seats" in params, "Missing parameter 'seats'"
    assert "table" in params, "Missing parameter 'table'"

def test_reservation_has_seats():
    assert hasattr(Reservation, "seats")
    descriptor = None
    for klass in Reservation.__mro__:
        if "seats" in klass.__dict__:
            descriptor = klass.__dict__["seats"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_table():
    assert hasattr(Reservation, "table")
    descriptor = None
    for klass in Reservation.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "customername" in params, "Missing parameter 'customername'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Orderlist" in params, "Missing parameter 'Orderlist'"
    assert "customerphone" in params, "Missing parameter 'customerphone'"
    assert "customer_email" in params, "Missing parameter 'customer_email'"
    assert "customer_address" in params, "Missing parameter 'customer_address'"

def test_order_has_customername():
    assert hasattr(Order, "customername")
    descriptor = None
    for klass in Order.__mro__:
        if "customername" in klass.__dict__:
            descriptor = klass.__dict__["customername"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Amount():
    assert hasattr(Order, "Amount")
    descriptor = None
    for klass in Order.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Orderlist():
    assert hasattr(Order, "Orderlist")
    descriptor = None
    for klass in Order.__mro__:
        if "Orderlist" in klass.__dict__:
            descriptor = klass.__dict__["Orderlist"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customerphone():
    assert hasattr(Order, "customerphone")
    descriptor = None
    for klass in Order.__mro__:
        if "customerphone" in klass.__dict__:
            descriptor = klass.__dict__["customerphone"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customer_email():
    assert hasattr(Order, "customer_email")
    descriptor = None
    for klass in Order.__mro__:
        if "customer_email" in klass.__dict__:
            descriptor = klass.__dict__["customer_email"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customer_address():
    assert hasattr(Order, "customer_address")
    descriptor = None
    for klass in Order.__mro__:
        if "customer_address" in klass.__dict__:
            descriptor = klass.__dict__["customer_address"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_order_management_system_is_not_abstract():
    assert not inspect.isabstract(Order_management_System)


def test_order_management_system_constructor_exists():
    assert callable(Order_management_System.__init__)


def test_order_management_system_constructor_args():
    sig = inspect.signature(Order_management_System.__init__)
    params = list(sig.parameters.keys())
    assert "Orderlist" in params, "Missing parameter 'Orderlist'"

def test_order_management_system_has_Orderlist():
    assert hasattr(Order_management_System, "Orderlist")
    descriptor = None
    for klass in Order_management_System.__mro__:
        if "Orderlist" in klass.__dict__:
            descriptor = klass.__dict__["Orderlist"]
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
Staff_strategy = st.builds(
    Staff,
    staffid=
        st.none(),
    name=
        st.none()
)
Foods_strategy = st.builds(
    Foods,
    Catogory=
        st.none(),
    price=
        st.none(),
    Foodname=
        st.none(),
    Ready=
        st.booleans()
)
Reservation_strategy = st.builds(
    Reservation,
    seats=
        st.none(),
    table=
        st.none()
)
Order_strategy = st.builds(
    Order,
    customername=
        st.none(),
    Amount=
        st.none(),
    Orderlist=
        st.none(),
    customerphone=
        st.none(),
    customer_email=
        st.none(),
    customer_address=
        st.none()
)
Class_strategy = st.builds(
    Class,
)
Order_management_System_strategy = st.builds(
    Order_management_System,
    Orderlist=
        st.none()
)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_staffid_setter(instance):
    original = instance.staffid
    instance.staffid = original
    assert instance.staffid == original



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Foods_strategy)
@settings(max_examples=50)
def test_foods_instantiation(instance):
    assert isinstance(instance, Foods)



@given(instance=Foods_strategy)
def test_foods_Catogory_setter(instance):
    original = instance.Catogory
    instance.Catogory = original
    assert instance.Catogory == original



@given(instance=Foods_strategy)
def test_foods_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Foods_strategy)
def test_foods_Foodname_setter(instance):
    original = instance.Foodname
    instance.Foodname = original
    assert instance.Foodname == original



@given(instance=Foods_strategy)
def test_foods_Ready_setter(instance):
    original = instance.Ready
    instance.Ready = original
    assert instance.Ready == original

@given(instance=Reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, Reservation)



@given(instance=Reservation_strategy)
def test_reservation_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original



@given(instance=Reservation_strategy)
def test_reservation_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_customername_setter(instance):
    original = instance.customername
    instance.customername = original
    assert instance.customername == original



@given(instance=Order_strategy)
def test_order_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Order_strategy)
def test_order_Orderlist_setter(instance):
    original = instance.Orderlist
    instance.Orderlist = original
    assert instance.Orderlist == original



@given(instance=Order_strategy)
def test_order_customerphone_setter(instance):
    original = instance.customerphone
    instance.customerphone = original
    assert instance.customerphone == original



@given(instance=Order_strategy)
def test_order_customer_email_setter(instance):
    original = instance.customer_email
    instance.customer_email = original
    assert instance.customer_email == original



@given(instance=Order_strategy)
def test_order_customer_address_setter(instance):
    original = instance.customer_address
    instance.customer_address = original
    assert instance.customer_address == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Order_management_System_strategy)
@settings(max_examples=50)
def test_order_management_system_instantiation(instance):
    assert isinstance(instance, Order_management_System)



@given(instance=Order_management_System_strategy)
def test_order_management_system_Orderlist_setter(instance):
    original = instance.Orderlist
    instance.Orderlist = original
    assert instance.Orderlist == original
