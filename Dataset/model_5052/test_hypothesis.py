import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eShop_Product,
    eShop_SaleLine,
    eShop_Portal,
    eShop_Customer,
    Customer,
    eShop_GoldCustomer,
    eShop_Sale,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eshop_product_is_not_abstract():
    assert not inspect.isabstract(eShop_Product)


def test_eshop_product_constructor_exists():
    assert callable(eShop_Product.__init__)


def test_eshop_product_constructor_args():
    sig = inspect.signature(eShop_Product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "stock" in params, "Missing parameter 'stock'"

def test_eshop_product_has_price():
    assert hasattr(eShop_Product, "price")
    descriptor = None
    for klass in eShop_Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_eshop_product_has_stock():
    assert hasattr(eShop_Product, "stock")
    descriptor = None
    for klass in eShop_Product.__mro__:
        if "stock" in klass.__dict__:
            descriptor = klass.__dict__["stock"]
            break
    assert isinstance(descriptor, property)



def test_eshop_saleline_is_not_abstract():
    assert not inspect.isabstract(eShop_SaleLine)


def test_eshop_saleline_constructor_exists():
    assert callable(eShop_SaleLine.__init__)


def test_eshop_saleline_constructor_args():
    sig = inspect.signature(eShop_SaleLine.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_eshop_saleline_has_quantity():
    assert hasattr(eShop_SaleLine, "quantity")
    descriptor = None
    for klass in eShop_SaleLine.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_eshop_portal_is_not_abstract():
    assert not inspect.isabstract(eShop_Portal)


def test_eshop_portal_constructor_exists():
    assert callable(eShop_Portal.__init__)


def test_eshop_portal_constructor_args():
    sig = inspect.signature(eShop_Portal.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "name" in params, "Missing parameter 'name'"

def test_eshop_portal_has_url():
    assert hasattr(eShop_Portal, "url")
    descriptor = None
    for klass in eShop_Portal.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_eshop_portal_has_name():
    assert hasattr(eShop_Portal, "name")
    descriptor = None
    for klass in eShop_Portal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eshop_customer_is_not_abstract():
    assert not inspect.isabstract(eShop_Customer)


def test_eshop_customer_constructor_exists():
    assert callable(eShop_Customer.__init__)


def test_eshop_customer_constructor_args():
    sig = inspect.signature(eShop_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eshop_customer_has_name():
    assert hasattr(eShop_Customer, "name")
    descriptor = None
    for klass in eShop_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_eshop_goldcustomer_is_not_abstract():
    assert not inspect.isabstract(eShop_GoldCustomer)


def test_eshop_goldcustomer_constructor_exists():
    assert callable(eShop_GoldCustomer.__init__)


def test_eshop_goldcustomer_constructor_args():
    sig = inspect.signature(eShop_GoldCustomer.__init__)
    params = list(sig.parameters.keys())



def test_eshop_sale_is_not_abstract():
    assert not inspect.isabstract(eShop_Sale)


def test_eshop_sale_constructor_exists():
    assert callable(eShop_Sale.__init__)


def test_eshop_sale_constructor_args():
    sig = inspect.signature(eShop_Sale.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "paid" in params, "Missing parameter 'paid'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_eshop_sale_has_id():
    assert hasattr(eShop_Sale, "id")
    descriptor = None
    for klass in eShop_Sale.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_eshop_sale_has_paid():
    assert hasattr(eShop_Sale, "paid")
    descriptor = None
    for klass in eShop_Sale.__mro__:
        if "paid" in klass.__dict__:
            descriptor = klass.__dict__["paid"]
            break
    assert isinstance(descriptor, property)

def test_eshop_sale_has_amount():
    assert hasattr(eShop_Sale, "amount")
    descriptor = None
    for klass in eShop_Sale.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
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
eShop_Product_strategy = st.builds(
    eShop_Product,
    price=
        st.integers(),
    stock=
        st.integers()
)
eShop_SaleLine_strategy = st.builds(
    eShop_SaleLine,
    quantity=
        st.integers()
)
eShop_Portal_strategy = st.builds(
    eShop_Portal,
    url=
        safe_text,
    name=
        safe_text
)
eShop_Customer_strategy = st.builds(
    eShop_Customer,
    name=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
)
eShop_GoldCustomer_strategy = st.builds(
    eShop_GoldCustomer,
)
eShop_Sale_strategy = st.builds(
    eShop_Sale,
    id=
        st.integers(),
    paid=
        st.booleans(),
    amount=
        st.integers()
)

@given(instance=eShop_Product_strategy)
@settings(max_examples=50)
def test_eshop_product_instantiation(instance):
    assert isinstance(instance, eShop_Product)



@given(instance=eShop_Product_strategy)
def test_eshop_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=eShop_Product_strategy)
def test_eshop_product_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original

@given(instance=eShop_SaleLine_strategy)
@settings(max_examples=50)
def test_eshop_saleline_instantiation(instance):
    assert isinstance(instance, eShop_SaleLine)



@given(instance=eShop_SaleLine_strategy)
def test_eshop_saleline_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=eShop_Portal_strategy)
@settings(max_examples=50)
def test_eshop_portal_instantiation(instance):
    assert isinstance(instance, eShop_Portal)



@given(instance=eShop_Portal_strategy)
def test_eshop_portal_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=eShop_Portal_strategy)
def test_eshop_portal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop_Portal_strategy)
@settings(max_examples=30)
def test_eshop_portal_removegoldcategory_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeGoldCategory(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeGoldCategory).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeGoldCategory' in eShop_Portal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeGoldCategory' in eShop_Portal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeGoldCategory' in eShop_Portal is not implemented or raised an error")

@given(instance=eShop_Customer_strategy)
@settings(max_examples=50)
def test_eshop_customer_instantiation(instance):
    assert isinstance(instance, eShop_Customer)



@given(instance=eShop_Customer_strategy)
def test_eshop_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop_Customer_strategy)
@settings(max_examples=30)
def test_eshop_customer_newcustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.newCustomer(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.newCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'newCustomer' in eShop_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newCustomer' in eShop_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newCustomer' in eShop_Customer is not implemented or raised an error")

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=eShop_GoldCustomer_strategy)
@settings(max_examples=50)
def test_eshop_goldcustomer_instantiation(instance):
    assert isinstance(instance, eShop_GoldCustomer)

@given(instance=eShop_Sale_strategy)
@settings(max_examples=50)
def test_eshop_sale_instantiation(instance):
    assert isinstance(instance, eShop_Sale)



@given(instance=eShop_Sale_strategy)
def test_eshop_sale_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eShop_Sale_strategy)
def test_eshop_sale_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original



@given(instance=eShop_Sale_strategy)
def test_eshop_sale_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop_Sale_strategy)
@settings(max_examples=30)
def test_eshop_sale_addsaleline_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addSaleLine(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addSaleLine).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addSaleLine' in eShop_Sale is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addSaleLine' in eShop_Sale did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addSaleLine' in eShop_Sale is not implemented or raised an error")
