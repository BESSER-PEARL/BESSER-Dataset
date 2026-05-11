import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Order,
    company::Product,
    company::OrderDetail,
    company::Order,
    company::SalesOrder,
    company::PurchaseOrder,
    company::Category,
    Addressable,
    company::Customer,
    company::Supplier,
    company::Company,
    company::Addressable,
    VAT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())



def test_company::product_is_not_abstract():
    assert not inspect.isabstract(company::Product)


def test_company::product_constructor_exists():
    assert callable(company::Product.__init__)


def test_company::product_constructor_args():
    sig = inspect.signature(company::Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "price" in params, "Missing parameter 'price'"
    assert "vat" in params, "Missing parameter 'vat'"

def test_company::product_has_name():
    assert hasattr(company::Product, "name")
    descriptor = None
    for klass in company::Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::product_has_description():
    assert hasattr(company::Product, "description")
    descriptor = None
    for klass in company::Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_company::product_has_price():
    assert hasattr(company::Product, "price")
    descriptor = None
    for klass in company::Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_company::product_has_vat():
    assert hasattr(company::Product, "vat")
    descriptor = None
    for klass in company::Product.__mro__:
        if "vat" in klass.__dict__:
            descriptor = klass.__dict__["vat"]
            break
    assert isinstance(descriptor, property)



def test_company::orderdetail_is_not_abstract():
    assert not inspect.isabstract(company::OrderDetail)


def test_company::orderdetail_constructor_exists():
    assert callable(company::OrderDetail.__init__)


def test_company::orderdetail_constructor_args():
    sig = inspect.signature(company::OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"

def test_company::orderdetail_has_price():
    assert hasattr(company::OrderDetail, "price")
    descriptor = None
    for klass in company::OrderDetail.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_company::order_is_not_abstract():
    assert not inspect.isabstract(company::Order)


def test_company::order_constructor_exists():
    assert callable(company::Order.__init__)


def test_company::order_constructor_args():
    sig = inspect.signature(company::Order.__init__)
    params = list(sig.parameters.keys())



def test_company::salesorder_is_not_abstract():
    assert not inspect.isabstract(company::SalesOrder)


def test_company::salesorder_constructor_exists():
    assert callable(company::SalesOrder.__init__)


def test_company::salesorder_constructor_args():
    sig = inspect.signature(company::SalesOrder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_company::salesorder_has_id():
    assert hasattr(company::SalesOrder, "id")
    descriptor = None
    for klass in company::SalesOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_company::purchaseorder_is_not_abstract():
    assert not inspect.isabstract(company::PurchaseOrder)


def test_company::purchaseorder_constructor_exists():
    assert callable(company::PurchaseOrder.__init__)


def test_company::purchaseorder_constructor_args():
    sig = inspect.signature(company::PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_company::purchaseorder_has_date():
    assert hasattr(company::PurchaseOrder, "date")
    descriptor = None
    for klass in company::PurchaseOrder.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_company::category_is_not_abstract():
    assert not inspect.isabstract(company::Category)


def test_company::category_constructor_exists():
    assert callable(company::Category.__init__)


def test_company::category_constructor_args():
    sig = inspect.signature(company::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company::category_has_name():
    assert hasattr(company::Category, "name")
    descriptor = None
    for klass in company::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_addressable_is_not_abstract():
    assert not inspect.isabstract(Addressable)


def test_addressable_constructor_exists():
    assert callable(Addressable.__init__)


def test_addressable_constructor_args():
    sig = inspect.signature(Addressable.__init__)
    params = list(sig.parameters.keys())



def test_company::customer_is_not_abstract():
    assert not inspect.isabstract(company::Customer)


def test_company::customer_constructor_exists():
    assert callable(company::Customer.__init__)


def test_company::customer_constructor_args():
    sig = inspect.signature(company::Customer.__init__)
    params = list(sig.parameters.keys())



def test_company::supplier_is_not_abstract():
    assert not inspect.isabstract(company::Supplier)


def test_company::supplier_constructor_exists():
    assert callable(company::Supplier.__init__)


def test_company::supplier_constructor_args():
    sig = inspect.signature(company::Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "preferred" in params, "Missing parameter 'preferred'"

def test_company::supplier_has_preferred():
    assert hasattr(company::Supplier, "preferred")
    descriptor = None
    for klass in company::Supplier.__mro__:
        if "preferred" in klass.__dict__:
            descriptor = klass.__dict__["preferred"]
            break
    assert isinstance(descriptor, property)



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
    params = list(sig.parameters.keys())



def test_company::addressable_is_not_abstract():
    assert not inspect.isabstract(company::Addressable)


def test_company::addressable_constructor_exists():
    assert callable(company::Addressable.__init__)


def test_company::addressable_constructor_args():
    sig = inspect.signature(company::Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::addressable_has_city():
    assert hasattr(company::Addressable, "city")
    descriptor = None
    for klass in company::Addressable.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_company::addressable_has_street():
    assert hasattr(company::Addressable, "street")
    descriptor = None
    for klass in company::Addressable.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_company::addressable_has_name():
    assert hasattr(company::Addressable, "name")
    descriptor = None
    for klass in company::Addressable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vat_exists():
    # Check that the Enumeration exists
    assert VAT is not None

def test_vat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VAT]
    expected_literals = [
        "vat0",
        "vat15",
        "vat7",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VAT"


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
Order_strategy = st.builds(
    Order,
)
company::Product_strategy = st.builds(
    company::Product,
    name=
        safe_text,
    description=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    vat=
        safe_text
)
company::OrderDetail_strategy = st.builds(
    company::OrderDetail,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company::Order_strategy = st.builds(
    company::Order,
)
company::SalesOrder_strategy = st.builds(
    company::SalesOrder,
    id=
        st.integers()
)
company::PurchaseOrder_strategy = st.builds(
    company::PurchaseOrder,
    date=
        st.dates()
)
company::Category_strategy = st.builds(
    company::Category,
    name=
        safe_text
)
Addressable_strategy = st.builds(
    Addressable,
)
company::Customer_strategy = st.builds(
    company::Customer,
)
company::Supplier_strategy = st.builds(
    company::Supplier,
    preferred=
        st.booleans()
)
company::Company_strategy = st.builds(
    company::Company,
)
company::Addressable_strategy = st.builds(
    company::Addressable,
    city=
        safe_text,
    street=
        safe_text,
    name=
        safe_text
)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)

@given(instance=company::Product_strategy)
@settings(max_examples=50)
def test_company::product_instantiation(instance):
    assert isinstance(instance, company::Product)

@given(instance=company::Product_strategy)
def test_company::product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Product_strategy)
def test_company::product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Product_strategy)
def test_company::product_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=company::Product_strategy)
def test_company::product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=company::Product_strategy)
def test_company::product_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=company::Product_strategy)
def test_company::product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=company::Product_strategy)
def test_company::product_vat_type(instance):
    assert isinstance(instance.vat, str)


@given(instance=company::Product_strategy)
def test_company::product_vat_setter(instance):
    original = instance.vat
    instance.vat = original
    assert instance.vat == original

@given(instance=company::OrderDetail_strategy)
@settings(max_examples=50)
def test_company::orderdetail_instantiation(instance):
    assert isinstance(instance, company::OrderDetail)

@given(instance=company::OrderDetail_strategy)
def test_company::orderdetail_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=company::OrderDetail_strategy)
def test_company::orderdetail_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=company::Order_strategy)
@settings(max_examples=50)
def test_company::order_instantiation(instance):
    assert isinstance(instance, company::Order)

@given(instance=company::SalesOrder_strategy)
@settings(max_examples=50)
def test_company::salesorder_instantiation(instance):
    assert isinstance(instance, company::SalesOrder)

@given(instance=company::SalesOrder_strategy)
def test_company::salesorder_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=company::SalesOrder_strategy)
def test_company::salesorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=company::PurchaseOrder_strategy)
@settings(max_examples=50)
def test_company::purchaseorder_instantiation(instance):
    assert isinstance(instance, company::PurchaseOrder)

@given(instance=company::PurchaseOrder_strategy)
def test_company::purchaseorder_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=company::PurchaseOrder_strategy)
def test_company::purchaseorder_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=company::Category_strategy)
@settings(max_examples=50)
def test_company::category_instantiation(instance):
    assert isinstance(instance, company::Category)

@given(instance=company::Category_strategy)
def test_company::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Category_strategy)
def test_company::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=company::Customer_strategy)
@settings(max_examples=50)
def test_company::customer_instantiation(instance):
    assert isinstance(instance, company::Customer)

@given(instance=company::Supplier_strategy)
@settings(max_examples=50)
def test_company::supplier_instantiation(instance):
    assert isinstance(instance, company::Supplier)

@given(instance=company::Supplier_strategy)
def test_company::supplier_preferred_type(instance):
    assert isinstance(instance.preferred, bool)


@given(instance=company::Supplier_strategy)
def test_company::supplier_preferred_setter(instance):
    original = instance.preferred
    instance.preferred = original
    assert instance.preferred == original

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)

@given(instance=company::Addressable_strategy)
@settings(max_examples=50)
def test_company::addressable_instantiation(instance):
    assert isinstance(instance, company::Addressable)

@given(instance=company::Addressable_strategy)
def test_company::addressable_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=company::Addressable_strategy)
def test_company::addressable_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=company::Addressable_strategy)
def test_company::addressable_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=company::Addressable_strategy)
def test_company::addressable_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=company::Addressable_strategy)
def test_company::addressable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Addressable_strategy)
def test_company::addressable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
