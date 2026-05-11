import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OrderDetail,
    Order,
    model1::Product1,
    model1::OrderDetail,
    model1::SalesOrder,
    model1::PurchaseOrder,
    model1::Order,
    model1::ProductToOrder,
    model1::Address,
    model1::Category,
    Address,
    model1::Supplier,
    model1::OrderAddress,
    model1::Customer,
    model1::Company,
    VAT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_orderdetail_is_not_abstract():
    assert not inspect.isabstract(OrderDetail)


def test_orderdetail_constructor_exists():
    assert callable(OrderDetail.__init__)


def test_orderdetail_constructor_args():
    sig = inspect.signature(OrderDetail.__init__)
    params = list(sig.parameters.keys())



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())



def test_model1::product1_is_not_abstract():
    assert not inspect.isabstract(model1::Product1)


def test_model1::product1_constructor_exists():
    assert callable(model1::Product1.__init__)


def test_model1::product1_constructor_args():
    sig = inspect.signature(model1::Product1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "vat" in params, "Missing parameter 'vat'"
    assert "description" in params, "Missing parameter 'description'"

def test_model1::product1_has_name():
    assert hasattr(model1::Product1, "name")
    descriptor = None
    for klass in model1::Product1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model1::product1_has_vat():
    assert hasattr(model1::Product1, "vat")
    descriptor = None
    for klass in model1::Product1.__mro__:
        if "vat" in klass.__dict__:
            descriptor = klass.__dict__["vat"]
            break
    assert isinstance(descriptor, property)

def test_model1::product1_has_description():
    assert hasattr(model1::Product1, "description")
    descriptor = None
    for klass in model1::Product1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model1::orderdetail_is_not_abstract():
    assert not inspect.isabstract(model1::OrderDetail)


def test_model1::orderdetail_constructor_exists():
    assert callable(model1::OrderDetail.__init__)


def test_model1::orderdetail_constructor_args():
    sig = inspect.signature(model1::OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"

def test_model1::orderdetail_has_price():
    assert hasattr(model1::OrderDetail, "price")
    descriptor = None
    for klass in model1::OrderDetail.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_model1::salesorder_is_not_abstract():
    assert not inspect.isabstract(model1::SalesOrder)


def test_model1::salesorder_constructor_exists():
    assert callable(model1::SalesOrder.__init__)


def test_model1::salesorder_constructor_args():
    sig = inspect.signature(model1::SalesOrder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model1::salesorder_has_id():
    assert hasattr(model1::SalesOrder, "id")
    descriptor = None
    for klass in model1::SalesOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model1::purchaseorder_is_not_abstract():
    assert not inspect.isabstract(model1::PurchaseOrder)


def test_model1::purchaseorder_constructor_exists():
    assert callable(model1::PurchaseOrder.__init__)


def test_model1::purchaseorder_constructor_args():
    sig = inspect.signature(model1::PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_model1::purchaseorder_has_date():
    assert hasattr(model1::PurchaseOrder, "date")
    descriptor = None
    for klass in model1::PurchaseOrder.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_model1::order_is_not_abstract():
    assert not inspect.isabstract(model1::Order)


def test_model1::order_constructor_exists():
    assert callable(model1::Order.__init__)


def test_model1::order_constructor_args():
    sig = inspect.signature(model1::Order.__init__)
    params = list(sig.parameters.keys())



def test_model1::producttoorder_is_not_abstract():
    assert not inspect.isabstract(model1::ProductToOrder)


def test_model1::producttoorder_constructor_exists():
    assert callable(model1::ProductToOrder.__init__)


def test_model1::producttoorder_constructor_args():
    sig = inspect.signature(model1::ProductToOrder.__init__)
    params = list(sig.parameters.keys())



def test_model1::address_is_not_abstract():
    assert not inspect.isabstract(model1::Address)


def test_model1::address_constructor_exists():
    assert callable(model1::Address.__init__)


def test_model1::address_constructor_args():
    sig = inspect.signature(model1::Address.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_model1::address_has_name():
    assert hasattr(model1::Address, "name")
    descriptor = None
    for klass in model1::Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model1::address_has_street():
    assert hasattr(model1::Address, "street")
    descriptor = None
    for klass in model1::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_model1::address_has_city():
    assert hasattr(model1::Address, "city")
    descriptor = None
    for klass in model1::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_model1::category_is_not_abstract():
    assert not inspect.isabstract(model1::Category)


def test_model1::category_constructor_exists():
    assert callable(model1::Category.__init__)


def test_model1::category_constructor_args():
    sig = inspect.signature(model1::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model1::category_has_name():
    assert hasattr(model1::Category, "name")
    descriptor = None
    for klass in model1::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_model1::supplier_is_not_abstract():
    assert not inspect.isabstract(model1::Supplier)


def test_model1::supplier_constructor_exists():
    assert callable(model1::Supplier.__init__)


def test_model1::supplier_constructor_args():
    sig = inspect.signature(model1::Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "preferred" in params, "Missing parameter 'preferred'"

def test_model1::supplier_has_preferred():
    assert hasattr(model1::Supplier, "preferred")
    descriptor = None
    for klass in model1::Supplier.__mro__:
        if "preferred" in klass.__dict__:
            descriptor = klass.__dict__["preferred"]
            break
    assert isinstance(descriptor, property)



def test_model1::orderaddress_is_not_abstract():
    assert not inspect.isabstract(model1::OrderAddress)


def test_model1::orderaddress_constructor_exists():
    assert callable(model1::OrderAddress.__init__)


def test_model1::orderaddress_constructor_args():
    sig = inspect.signature(model1::OrderAddress.__init__)
    params = list(sig.parameters.keys())
    assert "testAttribute" in params, "Missing parameter 'testAttribute'"

def test_model1::orderaddress_has_testAttribute():
    assert hasattr(model1::OrderAddress, "testAttribute")
    descriptor = None
    for klass in model1::OrderAddress.__mro__:
        if "testAttribute" in klass.__dict__:
            descriptor = klass.__dict__["testAttribute"]
            break
    assert isinstance(descriptor, property)



def test_model1::customer_is_not_abstract():
    assert not inspect.isabstract(model1::Customer)


def test_model1::customer_constructor_exists():
    assert callable(model1::Customer.__init__)


def test_model1::customer_constructor_args():
    sig = inspect.signature(model1::Customer.__init__)
    params = list(sig.parameters.keys())



def test_model1::company_is_not_abstract():
    assert not inspect.isabstract(model1::Company)


def test_model1::company_constructor_exists():
    assert callable(model1::Company.__init__)


def test_model1::company_constructor_args():
    sig = inspect.signature(model1::Company.__init__)
    params = list(sig.parameters.keys())

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
OrderDetail_strategy = st.builds(
    OrderDetail,
)
Order_strategy = st.builds(
    Order,
)
model1::Product1_strategy = st.builds(
    model1::Product1,
    name=
        safe_text,
    vat=
        safe_text,
    description=
        safe_text
)
model1::OrderDetail_strategy = st.builds(
    model1::OrderDetail,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model1::SalesOrder_strategy = st.builds(
    model1::SalesOrder,
    id=
        st.integers()
)
model1::PurchaseOrder_strategy = st.builds(
    model1::PurchaseOrder,
    date=
        st.dates()
)
model1::Order_strategy = st.builds(
    model1::Order,
)
model1::ProductToOrder_strategy = st.builds(
    model1::ProductToOrder,
)
model1::Address_strategy = st.builds(
    model1::Address,
    name=
        safe_text,
    street=
        safe_text,
    city=
        safe_text
)
model1::Category_strategy = st.builds(
    model1::Category,
    name=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
model1::Supplier_strategy = st.builds(
    model1::Supplier,
    preferred=
        st.booleans()
)
model1::OrderAddress_strategy = st.builds(
    model1::OrderAddress,
    testAttribute=
        st.booleans()
)
model1::Customer_strategy = st.builds(
    model1::Customer,
)
model1::Company_strategy = st.builds(
    model1::Company,
)

@given(instance=OrderDetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, OrderDetail)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)

@given(instance=model1::Product1_strategy)
@settings(max_examples=50)
def test_model1::product1_instantiation(instance):
    assert isinstance(instance, model1::Product1)

@given(instance=model1::Product1_strategy)
def test_model1::product1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model1::Product1_strategy)
def test_model1::product1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model1::Product1_strategy)
def test_model1::product1_vat_type(instance):
    assert isinstance(instance.vat, str)


@given(instance=model1::Product1_strategy)
def test_model1::product1_vat_setter(instance):
    original = instance.vat
    instance.vat = original
    assert instance.vat == original

@given(instance=model1::Product1_strategy)
def test_model1::product1_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model1::Product1_strategy)
def test_model1::product1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model1::OrderDetail_strategy)
@settings(max_examples=50)
def test_model1::orderdetail_instantiation(instance):
    assert isinstance(instance, model1::OrderDetail)

@given(instance=model1::OrderDetail_strategy)
def test_model1::orderdetail_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=model1::OrderDetail_strategy)
def test_model1::orderdetail_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=model1::SalesOrder_strategy)
@settings(max_examples=50)
def test_model1::salesorder_instantiation(instance):
    assert isinstance(instance, model1::SalesOrder)

@given(instance=model1::SalesOrder_strategy)
def test_model1::salesorder_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=model1::SalesOrder_strategy)
def test_model1::salesorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model1::PurchaseOrder_strategy)
@settings(max_examples=50)
def test_model1::purchaseorder_instantiation(instance):
    assert isinstance(instance, model1::PurchaseOrder)

@given(instance=model1::PurchaseOrder_strategy)
def test_model1::purchaseorder_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=model1::PurchaseOrder_strategy)
def test_model1::purchaseorder_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=model1::Order_strategy)
@settings(max_examples=50)
def test_model1::order_instantiation(instance):
    assert isinstance(instance, model1::Order)

@given(instance=model1::ProductToOrder_strategy)
@settings(max_examples=50)
def test_model1::producttoorder_instantiation(instance):
    assert isinstance(instance, model1::ProductToOrder)

@given(instance=model1::Address_strategy)
@settings(max_examples=50)
def test_model1::address_instantiation(instance):
    assert isinstance(instance, model1::Address)

@given(instance=model1::Address_strategy)
def test_model1::address_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model1::Address_strategy)
def test_model1::address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model1::Address_strategy)
def test_model1::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=model1::Address_strategy)
def test_model1::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=model1::Address_strategy)
def test_model1::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=model1::Address_strategy)
def test_model1::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=model1::Category_strategy)
@settings(max_examples=50)
def test_model1::category_instantiation(instance):
    assert isinstance(instance, model1::Category)

@given(instance=model1::Category_strategy)
def test_model1::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model1::Category_strategy)
def test_model1::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=model1::Supplier_strategy)
@settings(max_examples=50)
def test_model1::supplier_instantiation(instance):
    assert isinstance(instance, model1::Supplier)

@given(instance=model1::Supplier_strategy)
def test_model1::supplier_preferred_type(instance):
    assert isinstance(instance.preferred, bool)


@given(instance=model1::Supplier_strategy)
def test_model1::supplier_preferred_setter(instance):
    original = instance.preferred
    instance.preferred = original
    assert instance.preferred == original

@given(instance=model1::OrderAddress_strategy)
@settings(max_examples=50)
def test_model1::orderaddress_instantiation(instance):
    assert isinstance(instance, model1::OrderAddress)

@given(instance=model1::OrderAddress_strategy)
def test_model1::orderaddress_testAttribute_type(instance):
    assert isinstance(instance.testAttribute, bool)


@given(instance=model1::OrderAddress_strategy)
def test_model1::orderaddress_testAttribute_setter(instance):
    original = instance.testAttribute
    instance.testAttribute = original
    assert instance.testAttribute == original

@given(instance=model1::Customer_strategy)
@settings(max_examples=50)
def test_model1::customer_instantiation(instance):
    assert isinstance(instance, model1::Customer)

@given(instance=model1::Company_strategy)
@settings(max_examples=50)
def test_model1::company_instantiation(instance):
    assert isinstance(instance, model1::Company)
