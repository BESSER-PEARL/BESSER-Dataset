import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Product,
    Classes,
    Order,
    User,
    Account,
    ShoppingCart,
    Payment,
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



def test_classes_is_not_abstract():
    assert not inspect.isabstract(Classes)


def test_classes_constructor_exists():
    assert callable(Classes.__init__)


def test_classes_constructor_args():
    sig = inspect.signature(Classes.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_classes_has_Name():
    assert hasattr(Classes, "Name")
    descriptor = None
    for klass in Classes.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_classes_has_quantity():
    assert hasattr(Classes, "quantity")
    descriptor = None
    for klass in Classes.__mro__:
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
    assert "number" in params, "Missing parameter 'number'"
    assert "Items" in params, "Missing parameter 'Items'"

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Items():
    assert hasattr(Order, "Items")
    descriptor = None
    for klass in Order.__mro__:
        if "Items" in klass.__dict__:
            descriptor = klass.__dict__["Items"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "password" in params, "Missing parameter 'password'"

def test_user_has_login():
    assert hasattr(User, "login")
    descriptor = None
    for klass in User.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Valid_invalid" in params, "Missing parameter 'Valid_invalid'"
    assert "open" in params, "Missing parameter 'open'"

def test_account_has_Valid_invalid():
    assert hasattr(Account, "Valid_invalid")
    descriptor = None
    for klass in Account.__mro__:
        if "Valid_invalid" in klass.__dict__:
            descriptor = klass.__dict__["Valid_invalid"]
            break
    assert isinstance(descriptor, property)

def test_account_has_open():
    assert hasattr(Account, "open")
    descriptor = None
    for klass in Account.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "Update_cart" in params, "Missing parameter 'Update_cart'"

def test_shoppingcart_has_Update_cart():
    assert hasattr(ShoppingCart, "Update_cart")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Update_cart" in klass.__dict__:
            descriptor = klass.__dict__["Update_cart"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Paytment_type" in params, "Missing parameter 'Paytment_type'"

def test_payment_has_Paytment_type():
    assert hasattr(Payment, "Paytment_type")
    descriptor = None
    for klass in Payment.__mro__:
        if "Paytment_type" in klass.__dict__:
            descriptor = klass.__dict__["Paytment_type"]
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
Classes_strategy = st.builds(
    Classes,
    Name=
        safe_text,
    quantity=
        safe_text
)
Order_strategy = st.builds(
    Order,
    number=
        safe_text,
    Items=
        safe_text
)
User_strategy = st.builds(
    User,
    login=
        safe_text,
    password=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Valid_invalid=
        safe_text,
    open=
        st.dates()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    Update_cart=
        st.dates()
)
Payment_strategy = st.builds(
    Payment,
    Paytment_type=
        safe_text
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

@given(instance=Classes_strategy)
@settings(max_examples=50)
def test_classes_instantiation(instance):
    assert isinstance(instance, Classes)



@given(instance=Classes_strategy)
def test_classes_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Classes_strategy)
def test_classes_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_Items_setter(instance):
    original = instance.Items
    instance.Items = original
    assert instance.Items == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Valid_invalid_setter(instance):
    original = instance.Valid_invalid
    instance.Valid_invalid = original
    assert instance.Valid_invalid == original



@given(instance=Account_strategy)
def test_account_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Update_cart_setter(instance):
    original = instance.Update_cart
    instance.Update_cart = original
    assert instance.Update_cart == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Paytment_type_setter(instance):
    original = instance.Paytment_type
    instance.Paytment_type = original
    assert instance.Paytment_type == original
