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



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_delivery_is_not_abstract():
    assert not inspect.isabstract(Delivery)


def test_delivery_constructor_exists():
    assert callable(Delivery.__init__)


def test_delivery_constructor_args():
    sig = inspect.signature(Delivery.__init__)
    params = list(sig.parameters.keys())



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Size_" in params, "Missing parameter 'Size_'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "ID_" in params, "Missing parameter 'ID_'"
    assert "Type_" in params, "Missing parameter 'Type_'"

def test_order_has_Size_():
    assert hasattr(Order, "Size_")
    descriptor = None
    for klass in Order.__mro__:
        if "Size_" in klass.__dict__:
            descriptor = klass.__dict__["Size_"]
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

def test_order_has_ID_():
    assert hasattr(Order, "ID_")
    descriptor = None
    for klass in Order.__mro__:
        if "ID_" in klass.__dict__:
            descriptor = klass.__dict__["ID_"]
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
)
Payment_strategy = st.builds(
    Payment,
)
User_strategy = st.builds(
    User,
)
Delivery_strategy = st.builds(
    Delivery,
)
Order_strategy = st.builds(
    Order,
    Size_=
        st.integers(),
    Quantity=
        st.integers(),
    ID_=
        st.integers(),
    Type_=
        safe_text
)

@given(instance=Discription_strategy)
@settings(max_examples=50)
def test_discription_instantiation(instance):
    assert isinstance(instance, Discription)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Delivery_strategy)
@settings(max_examples=50)
def test_delivery_instantiation(instance):
    assert isinstance(instance, Delivery)

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
def test_order_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Order_strategy)
def test_order_ID__setter(instance):
    original = instance.ID_
    instance.ID_ = original
    assert instance.ID_ == original



@given(instance=Order_strategy)
def test_order_Type__setter(instance):
    original = instance.Type_
    instance.Type_ = original
    assert instance.Type_ == original
