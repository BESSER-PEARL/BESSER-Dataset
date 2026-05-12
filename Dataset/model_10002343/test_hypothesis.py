import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Item,
    Shopping_Cart,
    Order,
    Customer,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "colour" in params, "Missing parameter 'colour'"

def test_item_has_price():
    assert hasattr(Item, "price")
    descriptor = None
    for klass in Item.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_item_has_productId():
    assert hasattr(Item, "productId")
    descriptor = None
    for klass in Item.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_item_has_colour():
    assert hasattr(Item, "colour")
    descriptor = None
    for klass in Item.__mro__:
        if "colour" in klass.__dict__:
            descriptor = klass.__dict__["colour"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "cartId" in params, "Missing parameter 'cartId'"

def test_shopping_cart_has_cartId():
    assert hasattr(Shopping_Cart, "cartId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_order_has_price():
    assert hasattr(Order, "price")
    descriptor = None
    for klass in Order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_order_has_quantity():
    assert hasattr(Order, "quantity")
    descriptor = None
    for klass in Order.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "cellNo" in params, "Missing parameter 'cellNo'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_emailAddress():
    assert hasattr(Customer, "emailAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_cellNo():
    assert hasattr(Customer, "cellNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "cellNo" in klass.__dict__:
            descriptor = klass.__dict__["cellNo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Gender():
    assert hasattr(Customer, "Gender")
    descriptor = None
    for klass in Customer.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_DOB():
    assert hasattr(Customer, "DOB")
    descriptor = None
    for klass in Customer.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
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



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_account_has_Username():
    assert hasattr(Account, "Username")
    descriptor = None
    for klass in Account.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Password():
    assert hasattr(Account, "Password")
    descriptor = None
    for klass in Account.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
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
Item_strategy = st.builds(
    Item,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    productId=
        safe_text,
    colour=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    cartId=
        safe_text
)
Order_strategy = st.builds(
    Order,
    price=
        st.none(),
    quantity=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    emailAddress=
        safe_text,
    cellNo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Gender=
        safe_text,
    DOB=
        safe_text,
    name=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Username=
        safe_text,
    Password=
        st.integers()
)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)



@given(instance=Item_strategy)
def test_item_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Item_strategy)
def test_item_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Item_strategy)
def test_item_colour_setter(instance):
    original = instance.colour
    instance.colour = original
    assert instance.colour == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Order_strategy)
def test_order_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_customer_cellNo_setter(instance):
    original = instance.cellNo
    instance.cellNo = original
    assert instance.cellNo == original



@given(instance=Customer_strategy)
def test_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_customer_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Account_strategy)
def test_account_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original
