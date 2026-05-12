import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OrderDetail,
    Order,
    model1_Product1,
    model1_OrderDetail,
    model1_SalesOrder,
    model1_PurchaseOrder,
    model1_Order,
    model1_ProductToOrder,
    model1_Address,
    model1_Category,
    Address,
    model1_Customer,
    model1_Supplier,
    model1_OrderAddress,
    model1_Company,
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



def test_model1_product1_is_not_abstract():
    assert not inspect.isabstract(model1_Product1)


def test_model1_product1_constructor_exists():
    assert callable(model1_Product1.__init__)


def test_model1_product1_constructor_args():
    sig = inspect.signature(model1_Product1.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "vat" in params, "Missing parameter 'vat'"
    assert "name" in params, "Missing parameter 'name'"

def test_model1_product1_has_description():
    assert hasattr(model1_Product1, "description")
    descriptor = None
    for klass in model1_Product1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model1_product1_has_vat():
    assert hasattr(model1_Product1, "vat")
    descriptor = None
    for klass in model1_Product1.__mro__:
        if "vat" in klass.__dict__:
            descriptor = klass.__dict__["vat"]
            break
    assert isinstance(descriptor, property)

def test_model1_product1_has_name():
    assert hasattr(model1_Product1, "name")
    descriptor = None
    for klass in model1_Product1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model1_orderdetail_is_not_abstract():
    assert not inspect.isabstract(model1_OrderDetail)


def test_model1_orderdetail_constructor_exists():
    assert callable(model1_OrderDetail.__init__)


def test_model1_orderdetail_constructor_args():
    sig = inspect.signature(model1_OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"

def test_model1_orderdetail_has_price():
    assert hasattr(model1_OrderDetail, "price")
    descriptor = None
    for klass in model1_OrderDetail.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_model1_salesorder_is_not_abstract():
    assert not inspect.isabstract(model1_SalesOrder)


def test_model1_salesorder_constructor_exists():
    assert callable(model1_SalesOrder.__init__)


def test_model1_salesorder_constructor_args():
    sig = inspect.signature(model1_SalesOrder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model1_salesorder_has_id():
    assert hasattr(model1_SalesOrder, "id")
    descriptor = None
    for klass in model1_SalesOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model1_purchaseorder_is_not_abstract():
    assert not inspect.isabstract(model1_PurchaseOrder)


def test_model1_purchaseorder_constructor_exists():
    assert callable(model1_PurchaseOrder.__init__)


def test_model1_purchaseorder_constructor_args():
    sig = inspect.signature(model1_PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_model1_purchaseorder_has_date():
    assert hasattr(model1_PurchaseOrder, "date")
    descriptor = None
    for klass in model1_PurchaseOrder.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_model1_order_is_not_abstract():
    assert not inspect.isabstract(model1_Order)


def test_model1_order_constructor_exists():
    assert callable(model1_Order.__init__)


def test_model1_order_constructor_args():
    sig = inspect.signature(model1_Order.__init__)
    params = list(sig.parameters.keys())



def test_model1_producttoorder_is_not_abstract():
    assert not inspect.isabstract(model1_ProductToOrder)


def test_model1_producttoorder_constructor_exists():
    assert callable(model1_ProductToOrder.__init__)


def test_model1_producttoorder_constructor_args():
    sig = inspect.signature(model1_ProductToOrder.__init__)
    params = list(sig.parameters.keys())



def test_model1_address_is_not_abstract():
    assert not inspect.isabstract(model1_Address)


def test_model1_address_constructor_exists():
    assert callable(model1_Address.__init__)


def test_model1_address_constructor_args():
    sig = inspect.signature(model1_Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "name" in params, "Missing parameter 'name'"

def test_model1_address_has_street():
    assert hasattr(model1_Address, "street")
    descriptor = None
    for klass in model1_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_model1_address_has_city():
    assert hasattr(model1_Address, "city")
    descriptor = None
    for klass in model1_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_model1_address_has_name():
    assert hasattr(model1_Address, "name")
    descriptor = None
    for klass in model1_Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model1_category_is_not_abstract():
    assert not inspect.isabstract(model1_Category)


def test_model1_category_constructor_exists():
    assert callable(model1_Category.__init__)


def test_model1_category_constructor_args():
    sig = inspect.signature(model1_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model1_category_has_name():
    assert hasattr(model1_Category, "name")
    descriptor = None
    for klass in model1_Category.__mro__:
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



def test_model1_customer_is_not_abstract():
    assert not inspect.isabstract(model1_Customer)


def test_model1_customer_constructor_exists():
    assert callable(model1_Customer.__init__)


def test_model1_customer_constructor_args():
    sig = inspect.signature(model1_Customer.__init__)
    params = list(sig.parameters.keys())



def test_model1_supplier_is_not_abstract():
    assert not inspect.isabstract(model1_Supplier)


def test_model1_supplier_constructor_exists():
    assert callable(model1_Supplier.__init__)


def test_model1_supplier_constructor_args():
    sig = inspect.signature(model1_Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "preferred" in params, "Missing parameter 'preferred'"

def test_model1_supplier_has_preferred():
    assert hasattr(model1_Supplier, "preferred")
    descriptor = None
    for klass in model1_Supplier.__mro__:
        if "preferred" in klass.__dict__:
            descriptor = klass.__dict__["preferred"]
            break
    assert isinstance(descriptor, property)



def test_model1_orderaddress_is_not_abstract():
    assert not inspect.isabstract(model1_OrderAddress)


def test_model1_orderaddress_constructor_exists():
    assert callable(model1_OrderAddress.__init__)


def test_model1_orderaddress_constructor_args():
    sig = inspect.signature(model1_OrderAddress.__init__)
    params = list(sig.parameters.keys())
    assert "testAttribute" in params, "Missing parameter 'testAttribute'"

def test_model1_orderaddress_has_testAttribute():
    assert hasattr(model1_OrderAddress, "testAttribute")
    descriptor = None
    for klass in model1_OrderAddress.__mro__:
        if "testAttribute" in klass.__dict__:
            descriptor = klass.__dict__["testAttribute"]
            break
    assert isinstance(descriptor, property)



def test_model1_company_is_not_abstract():
    assert not inspect.isabstract(model1_Company)


def test_model1_company_constructor_exists():
    assert callable(model1_Company.__init__)


def test_model1_company_constructor_args():
    sig = inspect.signature(model1_Company.__init__)
    params = list(sig.parameters.keys())

def test_vat_exists():
    # Check that the Enumeration exists
    assert VAT is not None

def test_vat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VAT]
    expected_literals = [
        "vat15",
        "vat0",
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
model1_Product1_strategy = st.builds(
    model1_Product1,
    description=
        safe_text,
    vat=
        safe_text,
    name=
        safe_text
)
model1_OrderDetail_strategy = st.builds(
    model1_OrderDetail,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model1_SalesOrder_strategy = st.builds(
    model1_SalesOrder,
    id=
        st.integers()
)
model1_PurchaseOrder_strategy = st.builds(
    model1_PurchaseOrder,
    date=
        st.dates()
)
model1_Order_strategy = st.builds(
    model1_Order,
)
model1_ProductToOrder_strategy = st.builds(
    model1_ProductToOrder,
)
model1_Address_strategy = st.builds(
    model1_Address,
    street=
        safe_text,
    city=
        safe_text,
    name=
        safe_text
)
model1_Category_strategy = st.builds(
    model1_Category,
    name=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
model1_Customer_strategy = st.builds(
    model1_Customer,
)
model1_Supplier_strategy = st.builds(
    model1_Supplier,
    preferred=
        st.booleans()
)
model1_OrderAddress_strategy = st.builds(
    model1_OrderAddress,
    testAttribute=
        st.booleans()
)
model1_Company_strategy = st.builds(
    model1_Company,
)

@given(instance=OrderDetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, OrderDetail)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)

@given(instance=model1_Product1_strategy)
@settings(max_examples=50)
def test_model1_product1_instantiation(instance):
    assert isinstance(instance, model1_Product1)



@given(instance=model1_Product1_strategy)
def test_model1_product1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model1_Product1_strategy)
def test_model1_product1_vat_setter(instance):
    original = instance.vat
    instance.vat = original
    assert instance.vat == original



@given(instance=model1_Product1_strategy)
def test_model1_product1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model1_OrderDetail_strategy)
@settings(max_examples=50)
def test_model1_orderdetail_instantiation(instance):
    assert isinstance(instance, model1_OrderDetail)



@given(instance=model1_OrderDetail_strategy)
def test_model1_orderdetail_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=model1_SalesOrder_strategy)
@settings(max_examples=50)
def test_model1_salesorder_instantiation(instance):
    assert isinstance(instance, model1_SalesOrder)



@given(instance=model1_SalesOrder_strategy)
def test_model1_salesorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model1_PurchaseOrder_strategy)
@settings(max_examples=50)
def test_model1_purchaseorder_instantiation(instance):
    assert isinstance(instance, model1_PurchaseOrder)



@given(instance=model1_PurchaseOrder_strategy)
def test_model1_purchaseorder_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=model1_Order_strategy)
@settings(max_examples=50)
def test_model1_order_instantiation(instance):
    assert isinstance(instance, model1_Order)

@given(instance=model1_ProductToOrder_strategy)
@settings(max_examples=50)
def test_model1_producttoorder_instantiation(instance):
    assert isinstance(instance, model1_ProductToOrder)

@given(instance=model1_Address_strategy)
@settings(max_examples=50)
def test_model1_address_instantiation(instance):
    assert isinstance(instance, model1_Address)



@given(instance=model1_Address_strategy)
def test_model1_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=model1_Address_strategy)
def test_model1_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=model1_Address_strategy)
def test_model1_address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model1_Category_strategy)
@settings(max_examples=50)
def test_model1_category_instantiation(instance):
    assert isinstance(instance, model1_Category)



@given(instance=model1_Category_strategy)
def test_model1_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=model1_Customer_strategy)
@settings(max_examples=50)
def test_model1_customer_instantiation(instance):
    assert isinstance(instance, model1_Customer)

@given(instance=model1_Supplier_strategy)
@settings(max_examples=50)
def test_model1_supplier_instantiation(instance):
    assert isinstance(instance, model1_Supplier)



@given(instance=model1_Supplier_strategy)
def test_model1_supplier_preferred_setter(instance):
    original = instance.preferred
    instance.preferred = original
    assert instance.preferred == original

@given(instance=model1_OrderAddress_strategy)
@settings(max_examples=50)
def test_model1_orderaddress_instantiation(instance):
    assert isinstance(instance, model1_OrderAddress)



@given(instance=model1_OrderAddress_strategy)
def test_model1_orderaddress_testAttribute_setter(instance):
    original = instance.testAttribute
    instance.testAttribute = original
    assert instance.testAttribute == original

@given(instance=model1_Company_strategy)
@settings(max_examples=50)
def test_model1_company_instantiation(instance):
    assert isinstance(instance, model1_Company)
