import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Payment,
    Discription,
    User,
    Delivery,
    Order,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Date_off" in params, "Missing parameter 'Date_off'"
    assert "Amount" in params, "Missing parameter 'Amount'"

def test_payment_has_Date_off():
    assert hasattr(Payment, "Date_off")
    descriptor = None
    for klass in Payment.__mro__:
        if "Date_off" in klass.__dict__:
            descriptor = klass.__dict__["Date_off"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Amount():
    assert hasattr(Payment, "Amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)



def test_discription_is_not_abstract():
    assert not inspect.isabstract(Discription)


def test_discription_constructor_exists():
    assert callable(Discription.__init__)


def test_discription_constructor_args():
    sig = inspect.signature(Discription.__init__)
    params = list(sig.parameters.keys())
    assert "Discription" in params, "Missing parameter 'Discription'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_discription_has_Discription():
    assert hasattr(Discription, "Discription")
    descriptor = None
    for klass in Discription.__mro__:
        if "Discription" in klass.__dict__:
            descriptor = klass.__dict__["Discription"]
            break
    assert isinstance(descriptor, property)

def test_discription_has_Email():
    assert hasattr(Discription, "Email")
    descriptor = None
    for klass in Discription.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Phone_num" in params, "Missing parameter 'Phone_num'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_user_has_Email():
    assert hasattr(User, "Email")
    descriptor = None
    for klass in User.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Phone_num():
    assert hasattr(User, "Phone_num")
    descriptor = None
    for klass in User.__mro__:
        if "Phone_num" in klass.__dict__:
            descriptor = klass.__dict__["Phone_num"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Address():
    assert hasattr(User, "Address")
    descriptor = None
    for klass in User.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_delivery_is_not_abstract():
    assert not inspect.isabstract(Delivery)


def test_delivery_constructor_exists():
    assert callable(Delivery.__init__)


def test_delivery_constructor_args():
    sig = inspect.signature(Delivery.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_delivery_has_Date():
    assert hasattr(Delivery, "Date")
    descriptor = None
    for klass in Delivery.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_delivery_has_Name():
    assert hasattr(Delivery, "Name")
    descriptor = None
    for klass in Delivery.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_delivery_has_Type():
    assert hasattr(Delivery, "Type")
    descriptor = None
    for klass in Delivery.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_order_has_Type():
    assert hasattr(Order, "Type")
    descriptor = None
    for klass in Order.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Size():
    assert hasattr(Order, "Size")
    descriptor = None
    for klass in Order.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Quantity():
    assert hasattr(Order, "Quantity")
    descriptor = None
    for klass in Order.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ID():
    assert hasattr(Order, "ID")
    descriptor = None
    for klass in Order.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
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
Payment_strategy = st.builds(
    Payment,
    Date_off=
        safe_text,
    Amount=
        st.integers()
)
Discription_strategy = st.builds(
    Discription,
    Discription=
        safe_text,
    Email=
        safe_text
)
User_strategy = st.builds(
    User,
    Email=
        safe_text,
    Phone_num=
        st.integers(),
    Address=
        safe_text,
    Name=
        safe_text
)
Delivery_strategy = st.builds(
    Delivery,
    Date=
        safe_text,
    Name=
        safe_text,
    Type=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Type=
        safe_text,
    Size=
        st.integers(),
    Quantity=
        st.integers(),
    ID=
        st.integers()
)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Date_off_setter(instance):
    original = instance.Date_off
    instance.Date_off = original
    assert instance.Date_off == original



@given(instance=Payment_strategy)
def test_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original

@given(instance=Discription_strategy)
@settings(max_examples=50)
def test_discription_instantiation(instance):
    assert isinstance(instance, Discription)



@given(instance=Discription_strategy)
def test_discription_Discription_setter(instance):
    original = instance.Discription
    instance.Discription = original
    assert instance.Discription == original



@given(instance=Discription_strategy)
def test_discription_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_user_Phone_num_setter(instance):
    original = instance.Phone_num
    instance.Phone_num = original
    assert instance.Phone_num == original



@given(instance=User_strategy)
def test_user_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Delivery_strategy)
@settings(max_examples=50)
def test_delivery_instantiation(instance):
    assert isinstance(instance, Delivery)



@given(instance=Delivery_strategy)
def test_delivery_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Delivery_strategy)
def test_delivery_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Delivery_strategy)
def test_delivery_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Order_strategy)
def test_order_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Order_strategy)
def test_order_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Order_strategy)
def test_order_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original
