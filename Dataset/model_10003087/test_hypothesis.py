import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShoppingCart,
    Admin,
    Customer,
    Login,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "cartID" in params, "Missing parameter 'cartID'"
    assert "productID" in params, "Missing parameter 'productID'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"

def test_shoppingcart_has_quantity():
    assert hasattr(ShoppingCart, "quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_cartID():
    assert hasattr(ShoppingCart, "cartID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "cartID" in klass.__dict__:
            descriptor = klass.__dict__["cartID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_productID():
    assert hasattr(ShoppingCart, "productID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_dateAdded():
    assert hasattr(ShoppingCart, "dateAdded")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"

def test_admin_has_email():
    assert hasattr(Admin, "email")
    descriptor = None
    for klass in Admin.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"
    assert "sem" in params, "Missing parameter 'sem'"

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phone():
    assert hasattr(Customer, "phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_branch():
    assert hasattr(Customer, "branch")
    descriptor = None
    for klass in Customer.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(Customer, "password")
    descriptor = None
    for klass in Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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

def test_customer_has_sem():
    assert hasattr(Customer, "sem")
    descriptor = None
    for klass in Customer.__mro__:
        if "sem" in klass.__dict__:
            descriptor = klass.__dict__["sem"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"

def test_login_has_email():
    assert hasattr(Login, "email")
    descriptor = None
    for klass in Login.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    quantity=
        st.integers(),
    cartID=
        st.integers(),
    productID=
        st.integers(),
    dateAdded=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    email=
        safe_text,
    password=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    name=
        safe_text,
    phone=
        st.integers(),
    branch=
        safe_text,
    password=
        safe_text,
    email=
        safe_text,
    sem=
        safe_text
)
Login_strategy = st.builds(
    Login,
    email=
        safe_text,
    password=
        safe_text
)

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_cartID_setter(instance):
    original = instance.cartID
    instance.cartID = original
    assert instance.cartID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Customer_strategy)
def test_customer_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_sem_setter(instance):
    original = instance.sem
    instance.sem = original
    assert instance.sem == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
