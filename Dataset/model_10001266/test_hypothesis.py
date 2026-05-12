import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Discription,
    Payment,
    User,
    Delivery,
    Order,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_discription_is_not_abstract():
    assert not inspect.isabstract(Discription)


def test_discription_constructor_exists():
    assert callable(Discription.__init__)


def test_discription_constructor_args():
    sig = inspect.signature(Discription.__init__)
    params = list(sig.parameters.keys())
    assert "Emil" in params, "Missing parameter 'Emil'"
    assert "Discription" in params, "Missing parameter 'Discription'"

def test_discription_has_Emil():
    assert hasattr(Discription, "Emil")
    descriptor = None
    for klass in Discription.__mro__:
        if "Emil" in klass.__dict__:
            descriptor = klass.__dict__["Emil"]
            break
    assert isinstance(descriptor, property)

def test_discription_has_Discription():
    assert hasattr(Discription, "Discription")
    descriptor = None
    for klass in Discription.__mro__:
        if "Discription" in klass.__dict__:
            descriptor = klass.__dict__["Discription"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Date_off" in params, "Missing parameter 'Date_off'"

def test_payment_has_Amount():
    assert hasattr(Payment, "Amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Date_off():
    assert hasattr(Payment, "Date_off")
    descriptor = None
    for klass in Payment.__mro__:
        if "Date_off" in klass.__dict__:
            descriptor = klass.__dict__["Date_off"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Phone_number" in params, "Missing parameter 'Phone_number'"
    assert "Phone_number1" in params, "Missing parameter 'Phone_number1'"
    assert "Email_" in params, "Missing parameter 'Email_'"
    assert "Address_" in params, "Missing parameter 'Address_'"
    assert "Name_" in params, "Missing parameter 'Name_'"

def test_user_has_Phone_number():
    assert hasattr(User, "Phone_number")
    descriptor = None
    for klass in User.__mro__:
        if "Phone_number" in klass.__dict__:
            descriptor = klass.__dict__["Phone_number"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Phone_number1():
    assert hasattr(User, "Phone_number1")
    descriptor = None
    for klass in User.__mro__:
        if "Phone_number1" in klass.__dict__:
            descriptor = klass.__dict__["Phone_number1"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Email_():
    assert hasattr(User, "Email_")
    descriptor = None
    for klass in User.__mro__:
        if "Email_" in klass.__dict__:
            descriptor = klass.__dict__["Email_"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Address_():
    assert hasattr(User, "Address_")
    descriptor = None
    for klass in User.__mro__:
        if "Address_" in klass.__dict__:
            descriptor = klass.__dict__["Address_"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Name_():
    assert hasattr(User, "Name_")
    descriptor = None
    for klass in User.__mro__:
        if "Name_" in klass.__dict__:
            descriptor = klass.__dict__["Name_"]
            break
    assert isinstance(descriptor, property)



def test_delivery_is_not_abstract():
    assert not inspect.isabstract(Delivery)


def test_delivery_constructor_exists():
    assert callable(Delivery.__init__)


def test_delivery_constructor_args():
    sig = inspect.signature(Delivery.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_delivery_has_Type():
    assert hasattr(Delivery, "Type")
    descriptor = None
    for klass in Delivery.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
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

def test_delivery_has_Date():
    assert hasattr(Delivery, "Date")
    descriptor = None
    for klass in Delivery.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Size_" in params, "Missing parameter 'Size_'"
    assert "Type_" in params, "Missing parameter 'Type_'"
    assert "ID_" in params, "Missing parameter 'ID_'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"

def test_order_has_Size_():
    assert hasattr(Order, "Size_")
    descriptor = None
    for klass in Order.__mro__:
        if "Size_" in klass.__dict__:
            descriptor = klass.__dict__["Size_"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Type_():
    assert hasattr(Order, "Type_")
    descriptor = None
    for klass in Order.__mro__:
        if "Type_" in klass.__dict__:
            descriptor = klass.__dict__["Type_"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ID_():
    assert hasattr(Order, "ID_")
    descriptor = None
    for klass in Order.__mro__:
        if "ID_" in klass.__dict__:
            descriptor = klass.__dict__["ID_"]
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
Discription_strategy = st.builds(
    Discription,
    Emil=
        safe_text,
    Discription=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Amount=
        st.integers(),
    Date_off=
        safe_text
)
User_strategy = st.builds(
    User,
    Phone_number=
        st.integers(),
    Phone_number1=
        st.integers(),
    Email_=
        safe_text,
    Address_=
        safe_text,
    Name_=
        safe_text
)
Delivery_strategy = st.builds(
    Delivery,
    Type=
        safe_text,
    Name=
        safe_text,
    Date=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Size_=
        st.integers(),
    Type_=
        safe_text,
    ID_=
        st.integers(),
    Quantity=
        st.integers()
)

@given(instance=Discription_strategy)
@settings(max_examples=50)
def test_discription_instantiation(instance):
    assert isinstance(instance, Discription)



@given(instance=Discription_strategy)
def test_discription_Emil_setter(instance):
    original = instance.Emil
    instance.Emil = original
    assert instance.Emil == original



@given(instance=Discription_strategy)
def test_discription_Discription_setter(instance):
    original = instance.Discription
    instance.Discription = original
    assert instance.Discription == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Payment_strategy)
def test_payment_Date_off_setter(instance):
    original = instance.Date_off
    instance.Date_off = original
    assert instance.Date_off == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Phone_number_setter(instance):
    original = instance.Phone_number
    instance.Phone_number = original
    assert instance.Phone_number == original



@given(instance=User_strategy)
def test_user_Phone_number1_setter(instance):
    original = instance.Phone_number1
    instance.Phone_number1 = original
    assert instance.Phone_number1 == original



@given(instance=User_strategy)
def test_user_Email__setter(instance):
    original = instance.Email_
    instance.Email_ = original
    assert instance.Email_ == original



@given(instance=User_strategy)
def test_user_Address__setter(instance):
    original = instance.Address_
    instance.Address_ = original
    assert instance.Address_ == original



@given(instance=User_strategy)
def test_user_Name__setter(instance):
    original = instance.Name_
    instance.Name_ = original
    assert instance.Name_ == original

@given(instance=Delivery_strategy)
@settings(max_examples=50)
def test_delivery_instantiation(instance):
    assert isinstance(instance, Delivery)



@given(instance=Delivery_strategy)
def test_delivery_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Delivery_strategy)
def test_delivery_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Delivery_strategy)
def test_delivery_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Size__setter(instance):
    original = instance.Size_
    instance.Size_ = original
    assert instance.Size_ == original



@given(instance=Order_strategy)
def test_order_Type__setter(instance):
    original = instance.Type_
    instance.Type_ = original
    assert instance.Type_ == original



@given(instance=Order_strategy)
def test_order_ID__setter(instance):
    original = instance.ID_
    instance.ID_ = original
    assert instance.ID_ == original



@given(instance=Order_strategy)
def test_order_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original
