import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    esof_homework4_q2_USAddress,
    esof_homework4_q2_Item,
    esof_homework4_q2_PurchaseOrder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esof_homework4_q2_usaddress_is_not_abstract():
    assert not inspect.isabstract(esof_homework4_q2_USAddress)


def test_esof_homework4_q2_usaddress_constructor_exists():
    assert callable(esof_homework4_q2_USAddress.__init__)


def test_esof_homework4_q2_usaddress_constructor_args():
    sig = inspect.signature(esof_homework4_q2_USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "name" in params, "Missing parameter 'name'"
    assert "state" in params, "Missing parameter 'state'"
    assert "country" in params, "Missing parameter 'country'"
    assert "zip" in params, "Missing parameter 'zip'"

def test_esof_homework4_q2_usaddress_has_street():
    assert hasattr(esof_homework4_q2_USAddress, "street")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_usaddress_has_city():
    assert hasattr(esof_homework4_q2_USAddress, "city")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_usaddress_has_name():
    assert hasattr(esof_homework4_q2_USAddress, "name")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_usaddress_has_state():
    assert hasattr(esof_homework4_q2_USAddress, "state")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_usaddress_has_country():
    assert hasattr(esof_homework4_q2_USAddress, "country")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_usaddress_has_zip():
    assert hasattr(esof_homework4_q2_USAddress, "zip")
    descriptor = None
    for klass in esof_homework4_q2_USAddress.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)



def test_esof_homework4_q2_item_is_not_abstract():
    assert not inspect.isabstract(esof_homework4_q2_Item)


def test_esof_homework4_q2_item_constructor_exists():
    assert callable(esof_homework4_q2_Item.__init__)


def test_esof_homework4_q2_item_constructor_args():
    sig = inspect.signature(esof_homework4_q2_Item.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "shipDate" in params, "Missing parameter 'shipDate'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "USPrice" in params, "Missing parameter 'USPrice'"
    assert "partNum" in params, "Missing parameter 'partNum'"

def test_esof_homework4_q2_item_has_quantity():
    assert hasattr(esof_homework4_q2_Item, "quantity")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_item_has_shipDate():
    assert hasattr(esof_homework4_q2_Item, "shipDate")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "shipDate" in klass.__dict__:
            descriptor = klass.__dict__["shipDate"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_item_has_productName():
    assert hasattr(esof_homework4_q2_Item, "productName")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_item_has_comment():
    assert hasattr(esof_homework4_q2_Item, "comment")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_item_has_USPrice():
    assert hasattr(esof_homework4_q2_Item, "USPrice")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "USPrice" in klass.__dict__:
            descriptor = klass.__dict__["USPrice"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_item_has_partNum():
    assert hasattr(esof_homework4_q2_Item, "partNum")
    descriptor = None
    for klass in esof_homework4_q2_Item.__mro__:
        if "partNum" in klass.__dict__:
            descriptor = klass.__dict__["partNum"]
            break
    assert isinstance(descriptor, property)



def test_esof_homework4_q2_purchaseorder_is_not_abstract():
    assert not inspect.isabstract(esof_homework4_q2_PurchaseOrder)


def test_esof_homework4_q2_purchaseorder_constructor_exists():
    assert callable(esof_homework4_q2_PurchaseOrder.__init__)


def test_esof_homework4_q2_purchaseorder_constructor_args():
    sig = inspect.signature(esof_homework4_q2_PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_esof_homework4_q2_purchaseorder_has_comment():
    assert hasattr(esof_homework4_q2_PurchaseOrder, "comment")
    descriptor = None
    for klass in esof_homework4_q2_PurchaseOrder.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_esof_homework4_q2_purchaseorder_has_orderDate():
    assert hasattr(esof_homework4_q2_PurchaseOrder, "orderDate")
    descriptor = None
    for klass in esof_homework4_q2_PurchaseOrder.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
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
esof_homework4_q2_USAddress_strategy = st.builds(
    esof_homework4_q2_USAddress,
    street=
        safe_text,
    city=
        safe_text,
    name=
        safe_text,
    state=
        safe_text,
    country=
        safe_text,
    zip=
        st.integers()
)
esof_homework4_q2_Item_strategy = st.builds(
    esof_homework4_q2_Item,
    quantity=
        st.integers(),
    shipDate=
        safe_text,
    productName=
        safe_text,
    comment=
        safe_text,
    USPrice=
        st.integers(),
    partNum=
        safe_text
)
esof_homework4_q2_PurchaseOrder_strategy = st.builds(
    esof_homework4_q2_PurchaseOrder,
    comment=
        safe_text,
    orderDate=
        safe_text
)

@given(instance=esof_homework4_q2_USAddress_strategy)
@settings(max_examples=50)
def test_esof_homework4_q2_usaddress_instantiation(instance):
    assert isinstance(instance, esof_homework4_q2_USAddress)



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=esof_homework4_q2_USAddress_strategy)
def test_esof_homework4_q2_usaddress_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=esof_homework4_q2_Item_strategy)
@settings(max_examples=50)
def test_esof_homework4_q2_item_instantiation(instance):
    assert isinstance(instance, esof_homework4_q2_Item)



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_shipDate_setter(instance):
    original = instance.shipDate
    instance.shipDate = original
    assert instance.shipDate == original



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_USPrice_setter(instance):
    original = instance.USPrice
    instance.USPrice = original
    assert instance.USPrice == original



@given(instance=esof_homework4_q2_Item_strategy)
def test_esof_homework4_q2_item_partNum_setter(instance):
    original = instance.partNum
    instance.partNum = original
    assert instance.partNum == original

@given(instance=esof_homework4_q2_PurchaseOrder_strategy)
@settings(max_examples=50)
def test_esof_homework4_q2_purchaseorder_instantiation(instance):
    assert isinstance(instance, esof_homework4_q2_PurchaseOrder)



@given(instance=esof_homework4_q2_PurchaseOrder_strategy)
def test_esof_homework4_q2_purchaseorder_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=esof_homework4_q2_PurchaseOrder_strategy)
def test_esof_homework4_q2_purchaseorder_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original
