import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Product,
    Product_View,
    Order,
    WebUser,
    ShoppingCart,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_product_view_is_not_abstract():
    assert not inspect.isabstract(Product_View)


def test_product_view_constructor_exists():
    assert callable(Product_View.__init__)


def test_product_view_constructor_args():
    sig = inspect.signature(Product_View.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_product_view_has_price():
    assert hasattr(Product_View, "price")
    descriptor = None
    for klass in Product_View.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_product_view_has_quantity():
    assert hasattr(Product_View, "quantity")
    descriptor = None
    for klass in Product_View.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "number" in params, "Missing parameter 'number'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "total" in params, "Missing parameter 'total'"

def test_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Address():
    assert hasattr(Order, "Address")
    descriptor = None
    for klass in Order.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_webuser_is_not_abstract():
    assert not inspect.isabstract(WebUser)


def test_webuser_constructor_exists():
    assert callable(WebUser.__init__)


def test_webuser_constructor_args():
    sig = inspect.signature(WebUser.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "login" in params, "Missing parameter 'login'"

def test_webuser_has_password():
    assert hasattr(WebUser, "password")
    descriptor = None
    for klass in WebUser.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_webuser_has_login():
    assert hasattr(WebUser, "login")
    descriptor = None
    for klass in WebUser.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_shoppingcart_has_creationDate():
    assert hasattr(ShoppingCart, "creationDate")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
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
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    description=
        safe_text
)
Product_View_strategy = st.builds(
    Product_View,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    status=
        safe_text,
    number=
        st.integers(),
    ordered=
        st.dates(),
    Address=
        safe_text,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
WebUser_strategy = st.builds(
    WebUser,
    password=
        safe_text,
    login=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    creationDate=
        st.dates()
)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Product_View_strategy)
@settings(max_examples=50)
def test_product_view_instantiation(instance):
    assert isinstance(instance, Product_View)



@given(instance=Product_View_strategy)
def test_product_view_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_View_strategy)
def test_product_view_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_order_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Order_strategy)
def test_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=WebUser_strategy)
@settings(max_examples=50)
def test_webuser_instantiation(instance):
    assert isinstance(instance, WebUser)



@given(instance=WebUser_strategy)
def test_webuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=WebUser_strategy)
def test_webuser_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original
