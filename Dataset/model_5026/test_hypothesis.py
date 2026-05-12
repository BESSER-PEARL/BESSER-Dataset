import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Order,
    company_SalesOrder,
    company_PurchaseOrder,
    company_Product,
    company_OrderDetail,
    company_Order,
    company_Category,
    Addressable,
    company_Customer,
    company_Supplier,
    company_Company,
    company_Addressable,
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



def test_company_salesorder_is_not_abstract():
    assert not inspect.isabstract(company_SalesOrder)


def test_company_salesorder_constructor_exists():
    assert callable(company_SalesOrder.__init__)


def test_company_salesorder_constructor_args():
    sig = inspect.signature(company_SalesOrder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_company_salesorder_has_id():
    assert hasattr(company_SalesOrder, "id")
    descriptor = None
    for klass in company_SalesOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_company_purchaseorder_is_not_abstract():
    assert not inspect.isabstract(company_PurchaseOrder)


def test_company_purchaseorder_constructor_exists():
    assert callable(company_PurchaseOrder.__init__)


def test_company_purchaseorder_constructor_args():
    sig = inspect.signature(company_PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_company_purchaseorder_has_date():
    assert hasattr(company_PurchaseOrder, "date")
    descriptor = None
    for klass in company_PurchaseOrder.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_company_product_is_not_abstract():
    assert not inspect.isabstract(company_Product)


def test_company_product_constructor_exists():
    assert callable(company_Product.__init__)


def test_company_product_constructor_args():
    sig = inspect.signature(company_Product.__init__)
    params = list(sig.parameters.keys())
    assert "vat" in params, "Missing parameter 'vat'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_company_product_has_vat():
    assert hasattr(company_Product, "vat")
    descriptor = None
    for klass in company_Product.__mro__:
        if "vat" in klass.__dict__:
            descriptor = klass.__dict__["vat"]
            break
    assert isinstance(descriptor, property)

def test_company_product_has_description():
    assert hasattr(company_Product, "description")
    descriptor = None
    for klass in company_Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_company_product_has_name():
    assert hasattr(company_Product, "name")
    descriptor = None
    for klass in company_Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_product_has_price():
    assert hasattr(company_Product, "price")
    descriptor = None
    for klass in company_Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_company_orderdetail_is_not_abstract():
    assert not inspect.isabstract(company_OrderDetail)


def test_company_orderdetail_constructor_exists():
    assert callable(company_OrderDetail.__init__)


def test_company_orderdetail_constructor_args():
    sig = inspect.signature(company_OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"

def test_company_orderdetail_has_price():
    assert hasattr(company_OrderDetail, "price")
    descriptor = None
    for klass in company_OrderDetail.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_company_order_is_not_abstract():
    assert not inspect.isabstract(company_Order)


def test_company_order_constructor_exists():
    assert callable(company_Order.__init__)


def test_company_order_constructor_args():
    sig = inspect.signature(company_Order.__init__)
    params = list(sig.parameters.keys())



def test_company_category_is_not_abstract():
    assert not inspect.isabstract(company_Category)


def test_company_category_constructor_exists():
    assert callable(company_Category.__init__)


def test_company_category_constructor_args():
    sig = inspect.signature(company_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_company_category_has_name():
    assert hasattr(company_Category, "name")
    descriptor = None
    for klass in company_Category.__mro__:
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



def test_company_customer_is_not_abstract():
    assert not inspect.isabstract(company_Customer)


def test_company_customer_constructor_exists():
    assert callable(company_Customer.__init__)


def test_company_customer_constructor_args():
    sig = inspect.signature(company_Customer.__init__)
    params = list(sig.parameters.keys())



def test_company_supplier_is_not_abstract():
    assert not inspect.isabstract(company_Supplier)


def test_company_supplier_constructor_exists():
    assert callable(company_Supplier.__init__)


def test_company_supplier_constructor_args():
    sig = inspect.signature(company_Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "preferred" in params, "Missing parameter 'preferred'"

def test_company_supplier_has_preferred():
    assert hasattr(company_Supplier, "preferred")
    descriptor = None
    for klass in company_Supplier.__mro__:
        if "preferred" in klass.__dict__:
            descriptor = klass.__dict__["preferred"]
            break
    assert isinstance(descriptor, property)



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())



def test_company_addressable_is_not_abstract():
    assert not inspect.isabstract(company_Addressable)


def test_company_addressable_constructor_exists():
    assert callable(company_Addressable.__init__)


def test_company_addressable_constructor_args():
    sig = inspect.signature(company_Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_addressable_has_city():
    assert hasattr(company_Addressable, "city")
    descriptor = None
    for klass in company_Addressable.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_company_addressable_has_street():
    assert hasattr(company_Addressable, "street")
    descriptor = None
    for klass in company_Addressable.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_company_addressable_has_name():
    assert hasattr(company_Addressable, "name")
    descriptor = None
    for klass in company_Addressable.__mro__:
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
        "vat15",
        "vat7",
        "vat0",
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
company_SalesOrder_strategy = st.builds(
    company_SalesOrder,
    id=
        st.integers()
)
company_PurchaseOrder_strategy = st.builds(
    company_PurchaseOrder,
    date=
        st.dates()
)
company_Product_strategy = st.builds(
    company_Product,
    vat=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company_OrderDetail_strategy = st.builds(
    company_OrderDetail,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
company_Order_strategy = st.builds(
    company_Order,
)
company_Category_strategy = st.builds(
    company_Category,
    name=
        safe_text
)
Addressable_strategy = st.builds(
    Addressable,
)
company_Customer_strategy = st.builds(
    company_Customer,
)
company_Supplier_strategy = st.builds(
    company_Supplier,
    preferred=
        st.booleans()
)
company_Company_strategy = st.builds(
    company_Company,
)
company_Addressable_strategy = st.builds(
    company_Addressable,
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

@given(instance=company_SalesOrder_strategy)
@settings(max_examples=50)
def test_company_salesorder_instantiation(instance):
    assert isinstance(instance, company_SalesOrder)



@given(instance=company_SalesOrder_strategy)
def test_company_salesorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=company_PurchaseOrder_strategy)
@settings(max_examples=50)
def test_company_purchaseorder_instantiation(instance):
    assert isinstance(instance, company_PurchaseOrder)



@given(instance=company_PurchaseOrder_strategy)
def test_company_purchaseorder_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=company_Product_strategy)
@settings(max_examples=50)
def test_company_product_instantiation(instance):
    assert isinstance(instance, company_Product)



@given(instance=company_Product_strategy)
def test_company_product_vat_setter(instance):
    original = instance.vat
    instance.vat = original
    assert instance.vat == original



@given(instance=company_Product_strategy)
def test_company_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=company_Product_strategy)
def test_company_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Product_strategy)
def test_company_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=company_OrderDetail_strategy)
@settings(max_examples=50)
def test_company_orderdetail_instantiation(instance):
    assert isinstance(instance, company_OrderDetail)



@given(instance=company_OrderDetail_strategy)
def test_company_orderdetail_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=company_Order_strategy)
@settings(max_examples=50)
def test_company_order_instantiation(instance):
    assert isinstance(instance, company_Order)

@given(instance=company_Category_strategy)
@settings(max_examples=50)
def test_company_category_instantiation(instance):
    assert isinstance(instance, company_Category)



@given(instance=company_Category_strategy)
def test_company_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=company_Customer_strategy)
@settings(max_examples=50)
def test_company_customer_instantiation(instance):
    assert isinstance(instance, company_Customer)

@given(instance=company_Supplier_strategy)
@settings(max_examples=50)
def test_company_supplier_instantiation(instance):
    assert isinstance(instance, company_Supplier)



@given(instance=company_Supplier_strategy)
def test_company_supplier_preferred_setter(instance):
    original = instance.preferred
    instance.preferred = original
    assert instance.preferred == original

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)

@given(instance=company_Addressable_strategy)
@settings(max_examples=50)
def test_company_addressable_instantiation(instance):
    assert isinstance(instance, company_Addressable)



@given(instance=company_Addressable_strategy)
def test_company_addressable_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=company_Addressable_strategy)
def test_company_addressable_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=company_Addressable_strategy)
def test_company_addressable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
