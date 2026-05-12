import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Items,
    Warehouse,
    Account,
    Order,
    Payment,
    Shopping_Cart,
    Products,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"

def test_items_has_Description():
    assert hasattr(Items, "Description")
    descriptor = None
    for klass in Items.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_warehouse_is_not_abstract():
    assert not inspect.isabstract(Warehouse)


def test_warehouse_constructor_exists():
    assert callable(Warehouse.__init__)


def test_warehouse_constructor_args():
    sig = inspect.signature(Warehouse.__init__)
    params = list(sig.parameters.keys())
    assert "Warehouse_branch" in params, "Missing parameter 'Warehouse_branch'"

def test_warehouse_has_Warehouse_branch():
    assert hasattr(Warehouse, "Warehouse_branch")
    descriptor = None
    for klass in Warehouse.__mro__:
        if "Warehouse_branch" in klass.__dict__:
            descriptor = klass.__dict__["Warehouse_branch"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"

def test_account_has_Address():
    assert hasattr(Account, "Address")
    descriptor = None
    for klass in Account.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Order_ID" in params, "Missing parameter 'Order_ID'"

def test_order_has_Order_ID():
    assert hasattr(Order, "Order_ID")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_ID" in klass.__dict__:
            descriptor = klass.__dict__["Order_ID"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Payment_ID" in params, "Missing parameter 'Payment_ID'"

def test_payment_has_Date():
    assert hasattr(Payment, "Date")
    descriptor = None
    for klass in Payment.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Payment_ID():
    assert hasattr(Payment, "Payment_ID")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_ID" in klass.__dict__:
            descriptor = klass.__dict__["Payment_ID"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"

def test_shopping_cart_has_Date():
    assert hasattr(Shopping_Cart, "Date")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "Product_ID" in params, "Missing parameter 'Product_ID'"

def test_products_has_Product_ID():
    assert hasattr(Products, "Product_ID")
    descriptor = None
    for klass in Products.__mro__:
        if "Product_ID" in klass.__dict__:
            descriptor = klass.__dict__["Product_ID"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Customer_ID" in params, "Missing parameter 'Customer_ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_customer_has_Customer_ID():
    assert hasattr(Customer, "Customer_ID")
    descriptor = None
    for klass in Customer.__mro__:
        if "Customer_ID" in klass.__dict__:
            descriptor = klass.__dict__["Customer_ID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Items_strategy = st.builds(
    Items,
    Description=
        safe_text
)
Warehouse_strategy = st.builds(
    Warehouse,
    Warehouse_branch=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Address=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Order_ID=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    Date=
        st.integers(),
    Payment_ID=
        st.integers()
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    Date=
        st.integers()
)
Products_strategy = st.builds(
    Products,
    Product_ID=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    Customer_ID=
        st.integers(),
    Name=
        safe_text
)

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)



@given(instance=Items_strategy)
def test_items_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Warehouse_strategy)
@settings(max_examples=50)
def test_warehouse_instantiation(instance):
    assert isinstance(instance, Warehouse)



@given(instance=Warehouse_strategy)
def test_warehouse_Warehouse_branch_setter(instance):
    original = instance.Warehouse_branch
    instance.Warehouse_branch = original
    assert instance.Warehouse_branch == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Order_ID_setter(instance):
    original = instance.Order_ID
    instance.Order_ID = original
    assert instance.Order_ID == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Payment_strategy)
def test_payment_Payment_ID_setter(instance):
    original = instance.Payment_ID
    instance.Payment_ID = original
    assert instance.Payment_ID == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_Product_ID_setter(instance):
    original = instance.Product_ID
    instance.Product_ID = original
    assert instance.Product_ID == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Customer_ID_setter(instance):
    original = instance.Customer_ID
    instance.Customer_ID = original
    assert instance.Customer_ID == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
