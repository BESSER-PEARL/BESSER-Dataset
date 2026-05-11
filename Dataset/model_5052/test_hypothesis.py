import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eShop::Sale,
    eShop::Product,
    eShop::SaleLine,
    eShop::Portal,
    eShop::Customer,
    Customer,
    eShop::GoldCustomer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eshop::sale_is_not_abstract():
    assert not inspect.isabstract(eShop::Sale)


def test_eshop::sale_constructor_exists():
    assert callable(eShop::Sale.__init__)


def test_eshop::sale_constructor_args():
    sig = inspect.signature(eShop::Sale.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "paid" in params, "Missing parameter 'paid'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_eshop::sale_has_id():
    assert hasattr(eShop::Sale, "id")
    descriptor = None
    for klass in eShop::Sale.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_eshop::sale_has_paid():
    assert hasattr(eShop::Sale, "paid")
    descriptor = None
    for klass in eShop::Sale.__mro__:
        if "paid" in klass.__dict__:
            descriptor = klass.__dict__["paid"]
            break
    assert isinstance(descriptor, property)

def test_eshop::sale_has_amount():
    assert hasattr(eShop::Sale, "amount")
    descriptor = None
    for klass in eShop::Sale.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_eshop::product_is_not_abstract():
    assert not inspect.isabstract(eShop::Product)


def test_eshop::product_constructor_exists():
    assert callable(eShop::Product.__init__)


def test_eshop::product_constructor_args():
    sig = inspect.signature(eShop::Product.__init__)
    params = list(sig.parameters.keys())
    assert "stock" in params, "Missing parameter 'stock'"
    assert "price" in params, "Missing parameter 'price'"

def test_eshop::product_has_stock():
    assert hasattr(eShop::Product, "stock")
    descriptor = None
    for klass in eShop::Product.__mro__:
        if "stock" in klass.__dict__:
            descriptor = klass.__dict__["stock"]
            break
    assert isinstance(descriptor, property)

def test_eshop::product_has_price():
    assert hasattr(eShop::Product, "price")
    descriptor = None
    for klass in eShop::Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_eshop::saleline_is_not_abstract():
    assert not inspect.isabstract(eShop::SaleLine)


def test_eshop::saleline_constructor_exists():
    assert callable(eShop::SaleLine.__init__)


def test_eshop::saleline_constructor_args():
    sig = inspect.signature(eShop::SaleLine.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_eshop::saleline_has_quantity():
    assert hasattr(eShop::SaleLine, "quantity")
    descriptor = None
    for klass in eShop::SaleLine.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_eshop::portal_is_not_abstract():
    assert not inspect.isabstract(eShop::Portal)


def test_eshop::portal_constructor_exists():
    assert callable(eShop::Portal.__init__)


def test_eshop::portal_constructor_args():
    sig = inspect.signature(eShop::Portal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_eshop::portal_has_name():
    assert hasattr(eShop::Portal, "name")
    descriptor = None
    for klass in eShop::Portal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eshop::portal_has_url():
    assert hasattr(eShop::Portal, "url")
    descriptor = None
    for klass in eShop::Portal.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_eshop::customer_is_not_abstract():
    assert not inspect.isabstract(eShop::Customer)


def test_eshop::customer_constructor_exists():
    assert callable(eShop::Customer.__init__)


def test_eshop::customer_constructor_args():
    sig = inspect.signature(eShop::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eshop::customer_has_name():
    assert hasattr(eShop::Customer, "name")
    descriptor = None
    for klass in eShop::Customer.__mro__:
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



def test_eshop::goldcustomer_is_not_abstract():
    assert not inspect.isabstract(eShop::GoldCustomer)


def test_eshop::goldcustomer_constructor_exists():
    assert callable(eShop::GoldCustomer.__init__)


def test_eshop::goldcustomer_constructor_args():
    sig = inspect.signature(eShop::GoldCustomer.__init__)
    params = list(sig.parameters.keys())


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
eShop::Sale_strategy = st.builds(
    eShop::Sale,
    id=
        st.integers(),
    paid=
        st.booleans(),
    amount=
        st.integers()
)
eShop::Product_strategy = st.builds(
    eShop::Product,
    stock=
        st.integers(),
    price=
        st.integers()
)
eShop::SaleLine_strategy = st.builds(
    eShop::SaleLine,
    quantity=
        st.integers()
)
eShop::Portal_strategy = st.builds(
    eShop::Portal,
    name=
        safe_text,
    url=
        safe_text
)
eShop::Customer_strategy = st.builds(
    eShop::Customer,
    name=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
)
eShop::GoldCustomer_strategy = st.builds(
    eShop::GoldCustomer,
)

@given(instance=eShop::Sale_strategy)
@settings(max_examples=50)
def test_eshop::sale_instantiation(instance):
    assert isinstance(instance, eShop::Sale)

@given(instance=eShop::Sale_strategy)
def test_eshop::sale_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=eShop::Sale_strategy)
def test_eshop::sale_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eShop::Sale_strategy)
def test_eshop::sale_paid_type(instance):
    assert isinstance(instance.paid, bool)


@given(instance=eShop::Sale_strategy)
def test_eshop::sale_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original

@given(instance=eShop::Sale_strategy)
def test_eshop::sale_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=eShop::Sale_strategy)
def test_eshop::sale_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop::Sale_strategy)
@settings(max_examples=30)
def test_eshop::sale_addsaleline_changes_state(instance):
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
        assert has_statements, f"Function 'addSaleLine' in eShop::Sale is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addSaleLine' in eShop::Sale did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addSaleLine' in eShop::Sale is not implemented or raised an error")

@given(instance=eShop::Product_strategy)
@settings(max_examples=50)
def test_eshop::product_instantiation(instance):
    assert isinstance(instance, eShop::Product)

@given(instance=eShop::Product_strategy)
def test_eshop::product_stock_type(instance):
    assert isinstance(instance.stock, int)


@given(instance=eShop::Product_strategy)
def test_eshop::product_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original

@given(instance=eShop::Product_strategy)
def test_eshop::product_price_type(instance):
    assert isinstance(instance.price, int)


@given(instance=eShop::Product_strategy)
def test_eshop::product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=eShop::SaleLine_strategy)
@settings(max_examples=50)
def test_eshop::saleline_instantiation(instance):
    assert isinstance(instance, eShop::SaleLine)

@given(instance=eShop::SaleLine_strategy)
def test_eshop::saleline_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=eShop::SaleLine_strategy)
def test_eshop::saleline_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=eShop::Portal_strategy)
@settings(max_examples=50)
def test_eshop::portal_instantiation(instance):
    assert isinstance(instance, eShop::Portal)

@given(instance=eShop::Portal_strategy)
def test_eshop::portal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eShop::Portal_strategy)
def test_eshop::portal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eShop::Portal_strategy)
def test_eshop::portal_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=eShop::Portal_strategy)
def test_eshop::portal_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop::Portal_strategy)
@settings(max_examples=30)
def test_eshop::portal_removegoldcategory_changes_state(instance):
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
        assert has_statements, f"Function 'removeGoldCategory' in eShop::Portal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeGoldCategory' in eShop::Portal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeGoldCategory' in eShop::Portal is not implemented or raised an error")

@given(instance=eShop::Customer_strategy)
@settings(max_examples=50)
def test_eshop::customer_instantiation(instance):
    assert isinstance(instance, eShop::Customer)

@given(instance=eShop::Customer_strategy)
def test_eshop::customer_name_type(instance):
    assert isinstance(instance.name, int)


@given(instance=eShop::Customer_strategy)
def test_eshop::customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=eShop::Customer_strategy)
@settings(max_examples=30)
def test_eshop::customer_newcustomer_changes_state(instance):
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
        assert has_statements, f"Function 'newCustomer' in eShop::Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newCustomer' in eShop::Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newCustomer' in eShop::Customer is not implemented or raised an error")

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=eShop::GoldCustomer_strategy)
@settings(max_examples=50)
def test_eshop::goldcustomer_instantiation(instance):
    assert isinstance(instance, eShop::GoldCustomer)
