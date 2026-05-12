import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bill,
    payment,
    order,
    waiter,
    chef,
    menu,
    staff,
    customer,
    restaurant,
    Print_Receipt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bill_is_not_abstract():
    assert not inspect.isabstract(bill)


def test_bill_constructor_exists():
    assert callable(bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(bill.__init__)
    params = list(sig.parameters.keys())
    assert "menuid" in params, "Missing parameter 'menuid'"
    assert "orderid" in params, "Missing parameter 'orderid'"
    assert "tableno" in params, "Missing parameter 'tableno'"

def test_bill_has_menuid():
    assert hasattr(bill, "menuid")
    descriptor = None
    for klass in bill.__mro__:
        if "menuid" in klass.__dict__:
            descriptor = klass.__dict__["menuid"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_orderid():
    assert hasattr(bill, "orderid")
    descriptor = None
    for klass in bill.__mro__:
        if "orderid" in klass.__dict__:
            descriptor = klass.__dict__["orderid"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_tableno():
    assert hasattr(bill, "tableno")
    descriptor = None
    for klass in bill.__mro__:
        if "tableno" in klass.__dict__:
            descriptor = klass.__dict__["tableno"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(payment)


def test_payment_constructor_exists():
    assert callable(payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(payment.__init__)
    params = list(sig.parameters.keys())
    assert "tableno" in params, "Missing parameter 'tableno'"
    assert "name" in params, "Missing parameter 'name'"

def test_payment_has_tableno():
    assert hasattr(payment, "tableno")
    descriptor = None
    for klass in payment.__mro__:
        if "tableno" in klass.__dict__:
            descriptor = klass.__dict__["tableno"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_name():
    assert hasattr(payment, "name")
    descriptor = None
    for klass in payment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(order)


def test_order_constructor_exists():
    assert callable(order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "orderid" in params, "Missing parameter 'orderid'"
    assert "orderdate" in params, "Missing parameter 'orderdate'"

def test_order_has_price():
    assert hasattr(order, "price")
    descriptor = None
    for klass in order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderid():
    assert hasattr(order, "orderid")
    descriptor = None
    for klass in order.__mro__:
        if "orderid" in klass.__dict__:
            descriptor = klass.__dict__["orderid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderdate():
    assert hasattr(order, "orderdate")
    descriptor = None
    for klass in order.__mro__:
        if "orderdate" in klass.__dict__:
            descriptor = klass.__dict__["orderdate"]
            break
    assert isinstance(descriptor, property)



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(waiter)


def test_waiter_constructor_exists():
    assert callable(waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(waiter.__init__)
    params = list(sig.parameters.keys())
    assert "Staffid" in params, "Missing parameter 'Staffid'"
    assert "name" in params, "Missing parameter 'name'"

def test_waiter_has_Staffid():
    assert hasattr(waiter, "Staffid")
    descriptor = None
    for klass in waiter.__mro__:
        if "Staffid" in klass.__dict__:
            descriptor = klass.__dict__["Staffid"]
            break
    assert isinstance(descriptor, property)

def test_waiter_has_name():
    assert hasattr(waiter, "name")
    descriptor = None
    for klass in waiter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chef_is_not_abstract():
    assert not inspect.isabstract(chef)


def test_chef_constructor_exists():
    assert callable(chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(chef.__init__)
    params = list(sig.parameters.keys())
    assert "Staffid" in params, "Missing parameter 'Staffid'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_chef_has_Staffid():
    assert hasattr(chef, "Staffid")
    descriptor = None
    for klass in chef.__mro__:
        if "Staffid" in klass.__dict__:
            descriptor = klass.__dict__["Staffid"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_Name():
    assert hasattr(chef, "Name")
    descriptor = None
    for klass in chef.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_menu_is_not_abstract():
    assert not inspect.isabstract(menu)


def test_menu_constructor_exists():
    assert callable(menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(menu.__init__)
    params = list(sig.parameters.keys())
    assert "Menuid" in params, "Missing parameter 'Menuid'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Menuname" in params, "Missing parameter 'Menuname'"

def test_menu_has_Menuid():
    assert hasattr(menu, "Menuid")
    descriptor = None
    for klass in menu.__mro__:
        if "Menuid" in klass.__dict__:
            descriptor = klass.__dict__["Menuid"]
            break
    assert isinstance(descriptor, property)

def test_menu_has_Price():
    assert hasattr(menu, "Price")
    descriptor = None
    for klass in menu.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_menu_has_Menuname():
    assert hasattr(menu, "Menuname")
    descriptor = None
    for klass in menu.__mro__:
        if "Menuname" in klass.__dict__:
            descriptor = klass.__dict__["Menuname"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(staff)


def test_staff_constructor_exists():
    assert callable(staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(staff.__init__)
    params = list(sig.parameters.keys())
    assert "staffID" in params, "Missing parameter 'staffID'"
    assert "jobtype" in params, "Missing parameter 'jobtype'"
    assert "name" in params, "Missing parameter 'name'"

def test_staff_has_staffID():
    assert hasattr(staff, "staffID")
    descriptor = None
    for klass in staff.__mro__:
        if "staffID" in klass.__dict__:
            descriptor = klass.__dict__["staffID"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_jobtype():
    assert hasattr(staff, "jobtype")
    descriptor = None
    for klass in staff.__mro__:
        if "jobtype" in klass.__dict__:
            descriptor = klass.__dict__["jobtype"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_name():
    assert hasattr(staff, "name")
    descriptor = None
    for klass in staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())
    assert "Tableno" in params, "Missing parameter 'Tableno'"
    assert "Order" in params, "Missing parameter 'Order'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_customer_has_Tableno():
    assert hasattr(customer, "Tableno")
    descriptor = None
    for klass in customer.__mro__:
        if "Tableno" in klass.__dict__:
            descriptor = klass.__dict__["Tableno"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Order():
    assert hasattr(customer, "Order")
    descriptor = None
    for klass in customer.__mro__:
        if "Order" in klass.__dict__:
            descriptor = klass.__dict__["Order"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(customer, "Name")
    descriptor = None
    for klass in customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_restaurant_is_not_abstract():
    assert not inspect.isabstract(restaurant)


def test_restaurant_constructor_exists():
    assert callable(restaurant.__init__)


def test_restaurant_constructor_args():
    sig = inspect.signature(restaurant.__init__)
    params = list(sig.parameters.keys())
    assert "tableid" in params, "Missing parameter 'tableid'"
    assert "Menuid" in params, "Missing parameter 'Menuid'"

def test_restaurant_has_tableid():
    assert hasattr(restaurant, "tableid")
    descriptor = None
    for klass in restaurant.__mro__:
        if "tableid" in klass.__dict__:
            descriptor = klass.__dict__["tableid"]
            break
    assert isinstance(descriptor, property)

def test_restaurant_has_Menuid():
    assert hasattr(restaurant, "Menuid")
    descriptor = None
    for klass in restaurant.__mro__:
        if "Menuid" in klass.__dict__:
            descriptor = klass.__dict__["Menuid"]
            break
    assert isinstance(descriptor, property)

def test_print_receipt_exists():
    # Check that the Enumeration exists
    assert Print_Receipt is not None

def test_print_receipt_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Print_Receipt]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Print_Receipt"


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
bill_strategy = st.builds(
    bill,
    menuid=
        safe_text,
    orderid=
        st.integers(),
    tableno=
        st.integers()
)
payment_strategy = st.builds(
    payment,
    tableno=
        st.integers(),
    name=
        safe_text
)
order_strategy = st.builds(
    order,
    price=
        st.integers(),
    orderid=
        st.integers(),
    orderdate=
        safe_text
)
waiter_strategy = st.builds(
    waiter,
    Staffid=
        st.integers(),
    name=
        safe_text
)
chef_strategy = st.builds(
    chef,
    Staffid=
        st.integers(),
    Name=
        safe_text
)
menu_strategy = st.builds(
    menu,
    Menuid=
        safe_text,
    Price=
        st.integers(),
    Menuname=
        safe_text
)
staff_strategy = st.builds(
    staff,
    staffID=
        st.integers(),
    jobtype=
        safe_text,
    name=
        safe_text
)
customer_strategy = st.builds(
    customer,
    Tableno=
        st.integers(),
    Order=
        safe_text,
    Name=
        safe_text
)
restaurant_strategy = st.builds(
    restaurant,
    tableid=
        st.integers(),
    Menuid=
        safe_text
)

@given(instance=bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, bill)



@given(instance=bill_strategy)
def test_bill_menuid_setter(instance):
    original = instance.menuid
    instance.menuid = original
    assert instance.menuid == original



@given(instance=bill_strategy)
def test_bill_orderid_setter(instance):
    original = instance.orderid
    instance.orderid = original
    assert instance.orderid == original



@given(instance=bill_strategy)
def test_bill_tableno_setter(instance):
    original = instance.tableno
    instance.tableno = original
    assert instance.tableno == original

@given(instance=payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, payment)



@given(instance=payment_strategy)
def test_payment_tableno_setter(instance):
    original = instance.tableno
    instance.tableno = original
    assert instance.tableno == original



@given(instance=payment_strategy)
def test_payment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, order)



@given(instance=order_strategy)
def test_order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=order_strategy)
def test_order_orderid_setter(instance):
    original = instance.orderid
    instance.orderid = original
    assert instance.orderid == original



@given(instance=order_strategy)
def test_order_orderdate_setter(instance):
    original = instance.orderdate
    instance.orderdate = original
    assert instance.orderdate == original

@given(instance=waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, waiter)



@given(instance=waiter_strategy)
def test_waiter_Staffid_setter(instance):
    original = instance.Staffid
    instance.Staffid = original
    assert instance.Staffid == original



@given(instance=waiter_strategy)
def test_waiter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, chef)



@given(instance=chef_strategy)
def test_chef_Staffid_setter(instance):
    original = instance.Staffid
    instance.Staffid = original
    assert instance.Staffid == original



@given(instance=chef_strategy)
def test_chef_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, menu)



@given(instance=menu_strategy)
def test_menu_Menuid_setter(instance):
    original = instance.Menuid
    instance.Menuid = original
    assert instance.Menuid == original



@given(instance=menu_strategy)
def test_menu_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=menu_strategy)
def test_menu_Menuname_setter(instance):
    original = instance.Menuname
    instance.Menuname = original
    assert instance.Menuname == original

@given(instance=staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, staff)



@given(instance=staff_strategy)
def test_staff_staffID_setter(instance):
    original = instance.staffID
    instance.staffID = original
    assert instance.staffID == original



@given(instance=staff_strategy)
def test_staff_jobtype_setter(instance):
    original = instance.jobtype
    instance.jobtype = original
    assert instance.jobtype == original



@given(instance=staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)



@given(instance=customer_strategy)
def test_customer_Tableno_setter(instance):
    original = instance.Tableno
    instance.Tableno = original
    assert instance.Tableno == original



@given(instance=customer_strategy)
def test_customer_Order_setter(instance):
    original = instance.Order
    instance.Order = original
    assert instance.Order == original



@given(instance=customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=restaurant_strategy)
@settings(max_examples=50)
def test_restaurant_instantiation(instance):
    assert isinstance(instance, restaurant)



@given(instance=restaurant_strategy)
def test_restaurant_tableid_setter(instance):
    original = instance.tableid
    instance.tableid = original
    assert instance.tableid == original



@given(instance=restaurant_strategy)
def test_restaurant_Menuid_setter(instance):
    original = instance.Menuid
    instance.Menuid = original
    assert instance.Menuid == original
