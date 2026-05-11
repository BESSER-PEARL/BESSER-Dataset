import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ppo::Item,
    ppo::USAddress,
    ppo::PurchaseOrder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ppo::item_is_not_abstract():
    assert not inspect.isabstract(ppo::Item)


def test_ppo::item_constructor_exists():
    assert callable(ppo::Item.__init__)


def test_ppo::item_constructor_args():
    sig = inspect.signature(ppo::Item.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "USPrice" in params, "Missing parameter 'USPrice'"
    assert "partNum" in params, "Missing parameter 'partNum'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "shipDate" in params, "Missing parameter 'shipDate'"
    assert "productName" in params, "Missing parameter 'productName'"

def test_ppo::item_has_comment():
    assert hasattr(ppo::Item, "comment")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_ppo::item_has_USPrice():
    assert hasattr(ppo::Item, "USPrice")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "USPrice" in klass.__dict__:
            descriptor = klass.__dict__["USPrice"]
            break
    assert isinstance(descriptor, property)

def test_ppo::item_has_partNum():
    assert hasattr(ppo::Item, "partNum")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "partNum" in klass.__dict__:
            descriptor = klass.__dict__["partNum"]
            break
    assert isinstance(descriptor, property)

def test_ppo::item_has_quantity():
    assert hasattr(ppo::Item, "quantity")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_ppo::item_has_shipDate():
    assert hasattr(ppo::Item, "shipDate")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "shipDate" in klass.__dict__:
            descriptor = klass.__dict__["shipDate"]
            break
    assert isinstance(descriptor, property)

def test_ppo::item_has_productName():
    assert hasattr(ppo::Item, "productName")
    descriptor = None
    for klass in ppo::Item.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)



def test_ppo::usaddress_is_not_abstract():
    assert not inspect.isabstract(ppo::USAddress)


def test_ppo::usaddress_constructor_exists():
    assert callable(ppo::USAddress.__init__)


def test_ppo::usaddress_constructor_args():
    sig = inspect.signature(ppo::USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"
    assert "name" in params, "Missing parameter 'name'"

def test_ppo::usaddress_has_zip():
    assert hasattr(ppo::USAddress, "zip")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_ppo::usaddress_has_street():
    assert hasattr(ppo::USAddress, "street")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_ppo::usaddress_has_country():
    assert hasattr(ppo::USAddress, "country")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_ppo::usaddress_has_state():
    assert hasattr(ppo::USAddress, "state")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_ppo::usaddress_has_city():
    assert hasattr(ppo::USAddress, "city")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_ppo::usaddress_has_name():
    assert hasattr(ppo::USAddress, "name")
    descriptor = None
    for klass in ppo::USAddress.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ppo::purchaseorder_is_not_abstract():
    assert not inspect.isabstract(ppo::PurchaseOrder)


def test_ppo::purchaseorder_constructor_exists():
    assert callable(ppo::PurchaseOrder.__init__)


def test_ppo::purchaseorder_constructor_args():
    sig = inspect.signature(ppo::PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_ppo::purchaseorder_has_comment():
    assert hasattr(ppo::PurchaseOrder, "comment")
    descriptor = None
    for klass in ppo::PurchaseOrder.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_ppo::purchaseorder_has_orderDate():
    assert hasattr(ppo::PurchaseOrder, "orderDate")
    descriptor = None
    for klass in ppo::PurchaseOrder.__mro__:
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
ppo::Item_strategy = st.builds(
    ppo::Item,
    comment=
        safe_text,
    USPrice=
        st.integers(),
    partNum=
        safe_text,
    quantity=
        st.integers(),
    shipDate=
        safe_text,
    productName=
        safe_text
)
ppo::USAddress_strategy = st.builds(
    ppo::USAddress,
    zip=
        st.integers(),
    street=
        safe_text,
    country=
        safe_text,
    state=
        safe_text,
    city=
        safe_text,
    name=
        safe_text
)
ppo::PurchaseOrder_strategy = st.builds(
    ppo::PurchaseOrder,
    comment=
        safe_text,
    orderDate=
        safe_text
)

@given(instance=ppo::Item_strategy)
@settings(max_examples=50)
def test_ppo::item_instantiation(instance):
    assert isinstance(instance, ppo::Item)

@given(instance=ppo::Item_strategy)
def test_ppo::item_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ppo::Item_strategy)
def test_ppo::item_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ppo::Item_strategy)
def test_ppo::item_USPrice_type(instance):
    assert isinstance(instance.USPrice, int)


@given(instance=ppo::Item_strategy)
def test_ppo::item_USPrice_setter(instance):
    original = instance.USPrice
    instance.USPrice = original
    assert instance.USPrice == original

@given(instance=ppo::Item_strategy)
def test_ppo::item_partNum_type(instance):
    assert isinstance(instance.partNum, str)


@given(instance=ppo::Item_strategy)
def test_ppo::item_partNum_setter(instance):
    original = instance.partNum
    instance.partNum = original
    assert instance.partNum == original

@given(instance=ppo::Item_strategy)
def test_ppo::item_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=ppo::Item_strategy)
def test_ppo::item_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=ppo::Item_strategy)
def test_ppo::item_shipDate_type(instance):
    assert isinstance(instance.shipDate, str)


@given(instance=ppo::Item_strategy)
def test_ppo::item_shipDate_setter(instance):
    original = instance.shipDate
    instance.shipDate = original
    assert instance.shipDate == original

@given(instance=ppo::Item_strategy)
def test_ppo::item_productName_type(instance):
    assert isinstance(instance.productName, str)


@given(instance=ppo::Item_strategy)
def test_ppo::item_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original

@given(instance=ppo::USAddress_strategy)
@settings(max_examples=50)
def test_ppo::usaddress_instantiation(instance):
    assert isinstance(instance, ppo::USAddress)

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_zip_type(instance):
    assert isinstance(instance.zip, int)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ppo::USAddress_strategy)
def test_ppo::usaddress_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ppo::PurchaseOrder_strategy)
@settings(max_examples=50)
def test_ppo::purchaseorder_instantiation(instance):
    assert isinstance(instance, ppo::PurchaseOrder)

@given(instance=ppo::PurchaseOrder_strategy)
def test_ppo::purchaseorder_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ppo::PurchaseOrder_strategy)
def test_ppo::purchaseorder_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ppo::PurchaseOrder_strategy)
def test_ppo::purchaseorder_orderDate_type(instance):
    assert isinstance(instance.orderDate, str)


@given(instance=ppo::PurchaseOrder_strategy)
def test_ppo::purchaseorder_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original
