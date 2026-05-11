import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    esof::homework4::q2::USAddress,
    esof::homework4::q2::Item,
    esof::homework4::q2::PurchaseOrder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esof::homework4::q2::usaddress_is_not_abstract():
    assert not inspect.isabstract(esof::homework4::q2::USAddress)


def test_esof::homework4::q2::usaddress_constructor_exists():
    assert callable(esof::homework4::q2::USAddress.__init__)


def test_esof::homework4::q2::usaddress_constructor_args():
    sig = inspect.signature(esof::homework4::q2::USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "country" in params, "Missing parameter 'country'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"

def test_esof::homework4::q2::usaddress_has_name():
    assert hasattr(esof::homework4::q2::USAddress, "name")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::usaddress_has_zip():
    assert hasattr(esof::homework4::q2::USAddress, "zip")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::usaddress_has_street():
    assert hasattr(esof::homework4::q2::USAddress, "street")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::usaddress_has_country():
    assert hasattr(esof::homework4::q2::USAddress, "country")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::usaddress_has_state():
    assert hasattr(esof::homework4::q2::USAddress, "state")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::usaddress_has_city():
    assert hasattr(esof::homework4::q2::USAddress, "city")
    descriptor = None
    for klass in esof::homework4::q2::USAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_esof::homework4::q2::item_is_not_abstract():
    assert not inspect.isabstract(esof::homework4::q2::Item)


def test_esof::homework4::q2::item_constructor_exists():
    assert callable(esof::homework4::q2::Item.__init__)


def test_esof::homework4::q2::item_constructor_args():
    sig = inspect.signature(esof::homework4::q2::Item.__init__)
    params = list(sig.parameters.keys())
    assert "productName" in params, "Missing parameter 'productName'"
    assert "USPrice" in params, "Missing parameter 'USPrice'"
    assert "partNum" in params, "Missing parameter 'partNum'"
    assert "shipDate" in params, "Missing parameter 'shipDate'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_esof::homework4::q2::item_has_productName():
    assert hasattr(esof::homework4::q2::Item, "productName")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::item_has_USPrice():
    assert hasattr(esof::homework4::q2::Item, "USPrice")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "USPrice" in klass.__dict__:
            descriptor = klass.__dict__["USPrice"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::item_has_partNum():
    assert hasattr(esof::homework4::q2::Item, "partNum")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "partNum" in klass.__dict__:
            descriptor = klass.__dict__["partNum"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::item_has_shipDate():
    assert hasattr(esof::homework4::q2::Item, "shipDate")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "shipDate" in klass.__dict__:
            descriptor = klass.__dict__["shipDate"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::item_has_quantity():
    assert hasattr(esof::homework4::q2::Item, "quantity")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::item_has_comment():
    assert hasattr(esof::homework4::q2::Item, "comment")
    descriptor = None
    for klass in esof::homework4::q2::Item.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_esof::homework4::q2::purchaseorder_is_not_abstract():
    assert not inspect.isabstract(esof::homework4::q2::PurchaseOrder)


def test_esof::homework4::q2::purchaseorder_constructor_exists():
    assert callable(esof::homework4::q2::PurchaseOrder.__init__)


def test_esof::homework4::q2::purchaseorder_constructor_args():
    sig = inspect.signature(esof::homework4::q2::PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_esof::homework4::q2::purchaseorder_has_comment():
    assert hasattr(esof::homework4::q2::PurchaseOrder, "comment")
    descriptor = None
    for klass in esof::homework4::q2::PurchaseOrder.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_esof::homework4::q2::purchaseorder_has_orderDate():
    assert hasattr(esof::homework4::q2::PurchaseOrder, "orderDate")
    descriptor = None
    for klass in esof::homework4::q2::PurchaseOrder.__mro__:
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
esof::homework4::q2::USAddress_strategy = st.builds(
    esof::homework4::q2::USAddress,
    name=
        safe_text,
    zip=
        st.integers(),
    street=
        safe_text,
    country=
        safe_text,
    state=
        safe_text,
    city=
        safe_text
)
esof::homework4::q2::Item_strategy = st.builds(
    esof::homework4::q2::Item,
    productName=
        safe_text,
    USPrice=
        st.integers(),
    partNum=
        safe_text,
    shipDate=
        safe_text,
    quantity=
        st.integers(),
    comment=
        safe_text
)
esof::homework4::q2::PurchaseOrder_strategy = st.builds(
    esof::homework4::q2::PurchaseOrder,
    comment=
        safe_text,
    orderDate=
        safe_text
)

@given(instance=esof::homework4::q2::USAddress_strategy)
@settings(max_examples=50)
def test_esof::homework4::q2::usaddress_instantiation(instance):
    assert isinstance(instance, esof::homework4::q2::USAddress)

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_zip_type(instance):
    assert isinstance(instance.zip, int)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=esof::homework4::q2::USAddress_strategy)
def test_esof::homework4::q2::usaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=esof::homework4::q2::Item_strategy)
@settings(max_examples=50)
def test_esof::homework4::q2::item_instantiation(instance):
    assert isinstance(instance, esof::homework4::q2::Item)

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_productName_type(instance):
    assert isinstance(instance.productName, str)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_USPrice_type(instance):
    assert isinstance(instance.USPrice, int)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_USPrice_setter(instance):
    original = instance.USPrice
    instance.USPrice = original
    assert instance.USPrice == original

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_partNum_type(instance):
    assert isinstance(instance.partNum, str)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_partNum_setter(instance):
    original = instance.partNum
    instance.partNum = original
    assert instance.partNum == original

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_shipDate_type(instance):
    assert isinstance(instance.shipDate, str)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_shipDate_setter(instance):
    original = instance.shipDate
    instance.shipDate = original
    assert instance.shipDate == original

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=esof::homework4::q2::Item_strategy)
def test_esof::homework4::q2::item_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=esof::homework4::q2::PurchaseOrder_strategy)
@settings(max_examples=50)
def test_esof::homework4::q2::purchaseorder_instantiation(instance):
    assert isinstance(instance, esof::homework4::q2::PurchaseOrder)

@given(instance=esof::homework4::q2::PurchaseOrder_strategy)
def test_esof::homework4::q2::purchaseorder_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=esof::homework4::q2::PurchaseOrder_strategy)
def test_esof::homework4::q2::purchaseorder_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=esof::homework4::q2::PurchaseOrder_strategy)
def test_esof::homework4::q2::purchaseorder_orderDate_type(instance):
    assert isinstance(instance.orderDate, str)


@given(instance=esof::homework4::q2::PurchaseOrder_strategy)
def test_esof::homework4::q2::purchaseorder_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original
