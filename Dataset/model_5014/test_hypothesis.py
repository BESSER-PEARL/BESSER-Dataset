import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    epo::GlobalLocation,
    GlobalLocation,
    Address,
    epo::GlobalAddress,
    epo::CanadianAddress,
    epo::USAddress,
    epo::PurchaseOrder,
    epo::Supplier,
    epo::Customer,
    epo::Address,
    epo::Item,
    OrderStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_epo::globallocation_is_not_abstract():
    assert not inspect.isabstract(epo::GlobalLocation)


def test_epo::globallocation_constructor_exists():
    assert callable(epo::GlobalLocation.__init__)


def test_epo::globallocation_constructor_args():
    sig = inspect.signature(epo::GlobalLocation.__init__)
    params = list(sig.parameters.keys())
    assert "countryCode" in params, "Missing parameter 'countryCode'"

def test_epo::globallocation_has_countryCode():
    assert hasattr(epo::GlobalLocation, "countryCode")
    descriptor = None
    for klass in epo::GlobalLocation.__mro__:
        if "countryCode" in klass.__dict__:
            descriptor = klass.__dict__["countryCode"]
            break
    assert isinstance(descriptor, property)



def test_globallocation_is_not_abstract():
    assert not inspect.isabstract(GlobalLocation)


def test_globallocation_constructor_exists():
    assert callable(GlobalLocation.__init__)


def test_globallocation_constructor_args():
    sig = inspect.signature(GlobalLocation.__init__)
    params = list(sig.parameters.keys())



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_epo::globaladdress_is_not_abstract():
    assert not inspect.isabstract(epo::GlobalAddress)


def test_epo::globaladdress_constructor_exists():
    assert callable(epo::GlobalAddress.__init__)


def test_epo::globaladdress_constructor_args():
    sig = inspect.signature(epo::GlobalAddress.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_epo::globaladdress_has_location():
    assert hasattr(epo::GlobalAddress, "location")
    descriptor = None
    for klass in epo::GlobalAddress.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_epo::canadianaddress_is_not_abstract():
    assert not inspect.isabstract(epo::CanadianAddress)


def test_epo::canadianaddress_constructor_exists():
    assert callable(epo::CanadianAddress.__init__)


def test_epo::canadianaddress_constructor_args():
    sig = inspect.signature(epo::CanadianAddress.__init__)
    params = list(sig.parameters.keys())
    assert "postalCode" in params, "Missing parameter 'postalCode'"
    assert "province" in params, "Missing parameter 'province'"
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"

def test_epo::canadianaddress_has_postalCode():
    assert hasattr(epo::CanadianAddress, "postalCode")
    descriptor = None
    for klass in epo::CanadianAddress.__mro__:
        if "postalCode" in klass.__dict__:
            descriptor = klass.__dict__["postalCode"]
            break
    assert isinstance(descriptor, property)

def test_epo::canadianaddress_has_province():
    assert hasattr(epo::CanadianAddress, "province")
    descriptor = None
    for klass in epo::CanadianAddress.__mro__:
        if "province" in klass.__dict__:
            descriptor = klass.__dict__["province"]
            break
    assert isinstance(descriptor, property)

def test_epo::canadianaddress_has_city():
    assert hasattr(epo::CanadianAddress, "city")
    descriptor = None
    for klass in epo::CanadianAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_epo::canadianaddress_has_street():
    assert hasattr(epo::CanadianAddress, "street")
    descriptor = None
    for klass in epo::CanadianAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_epo::usaddress_is_not_abstract():
    assert not inspect.isabstract(epo::USAddress)


def test_epo::usaddress_constructor_exists():
    assert callable(epo::USAddress.__init__)


def test_epo::usaddress_constructor_args():
    sig = inspect.signature(epo::USAddress.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"

def test_epo::usaddress_has_street():
    assert hasattr(epo::USAddress, "street")
    descriptor = None
    for klass in epo::USAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_epo::usaddress_has_zip():
    assert hasattr(epo::USAddress, "zip")
    descriptor = None
    for klass in epo::USAddress.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_epo::usaddress_has_state():
    assert hasattr(epo::USAddress, "state")
    descriptor = None
    for klass in epo::USAddress.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_epo::usaddress_has_city():
    assert hasattr(epo::USAddress, "city")
    descriptor = None
    for klass in epo::USAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_epo::purchaseorder_is_not_abstract():
    assert not inspect.isabstract(epo::PurchaseOrder)


def test_epo::purchaseorder_constructor_exists():
    assert callable(epo::PurchaseOrder.__init__)


def test_epo::purchaseorder_constructor_args():
    sig = inspect.signature(epo::PurchaseOrder.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"
    assert "totalAmount" in params, "Missing parameter 'totalAmount'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_epo::purchaseorder_has_status():
    assert hasattr(epo::PurchaseOrder, "status")
    descriptor = None
    for klass in epo::PurchaseOrder.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_epo::purchaseorder_has_orderDate():
    assert hasattr(epo::PurchaseOrder, "orderDate")
    descriptor = None
    for klass in epo::PurchaseOrder.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
            break
    assert isinstance(descriptor, property)

def test_epo::purchaseorder_has_totalAmount():
    assert hasattr(epo::PurchaseOrder, "totalAmount")
    descriptor = None
    for klass in epo::PurchaseOrder.__mro__:
        if "totalAmount" in klass.__dict__:
            descriptor = klass.__dict__["totalAmount"]
            break
    assert isinstance(descriptor, property)

def test_epo::purchaseorder_has_comment():
    assert hasattr(epo::PurchaseOrder, "comment")
    descriptor = None
    for klass in epo::PurchaseOrder.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_epo::supplier_is_not_abstract():
    assert not inspect.isabstract(epo::Supplier)


def test_epo::supplier_constructor_exists():
    assert callable(epo::Supplier.__init__)


def test_epo::supplier_constructor_args():
    sig = inspect.signature(epo::Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_epo::supplier_has_name():
    assert hasattr(epo::Supplier, "name")
    descriptor = None
    for klass in epo::Supplier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_epo::customer_is_not_abstract():
    assert not inspect.isabstract(epo::Customer)


def test_epo::customer_constructor_exists():
    assert callable(epo::Customer.__init__)


def test_epo::customer_constructor_args():
    sig = inspect.signature(epo::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "customerID" in params, "Missing parameter 'customerID'"

def test_epo::customer_has_customerID():
    assert hasattr(epo::Customer, "customerID")
    descriptor = None
    for klass in epo::Customer.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)



def test_epo::address_is_not_abstract():
    assert not inspect.isabstract(epo::Address)


def test_epo::address_constructor_exists():
    assert callable(epo::Address.__init__)


def test_epo::address_constructor_args():
    sig = inspect.signature(epo::Address.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "country" in params, "Missing parameter 'country'"

def test_epo::address_has_name():
    assert hasattr(epo::Address, "name")
    descriptor = None
    for klass in epo::Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_epo::address_has_country():
    assert hasattr(epo::Address, "country")
    descriptor = None
    for klass in epo::Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)



def test_epo::item_is_not_abstract():
    assert not inspect.isabstract(epo::Item)


def test_epo::item_constructor_exists():
    assert callable(epo::Item.__init__)


def test_epo::item_constructor_args():
    sig = inspect.signature(epo::Item.__init__)
    params = list(sig.parameters.keys())
    assert "productName" in params, "Missing parameter 'productName'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "USPrice" in params, "Missing parameter 'USPrice'"
    assert "shipDate" in params, "Missing parameter 'shipDate'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "partNum" in params, "Missing parameter 'partNum'"

def test_epo::item_has_productName():
    assert hasattr(epo::Item, "productName")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_epo::item_has_quantity():
    assert hasattr(epo::Item, "quantity")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_epo::item_has_USPrice():
    assert hasattr(epo::Item, "USPrice")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "USPrice" in klass.__dict__:
            descriptor = klass.__dict__["USPrice"]
            break
    assert isinstance(descriptor, property)

def test_epo::item_has_shipDate():
    assert hasattr(epo::Item, "shipDate")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "shipDate" in klass.__dict__:
            descriptor = klass.__dict__["shipDate"]
            break
    assert isinstance(descriptor, property)

def test_epo::item_has_comment():
    assert hasattr(epo::Item, "comment")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_epo::item_has_partNum():
    assert hasattr(epo::Item, "partNum")
    descriptor = None
    for klass in epo::Item.__mro__:
        if "partNum" in klass.__dict__:
            descriptor = klass.__dict__["partNum"]
            break
    assert isinstance(descriptor, property)

def test_orderstatus_exists():
    # Check that the Enumeration exists
    assert OrderStatus is not None

def test_orderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderStatus]
    expected_literals = [
        "BackOrder",
        "Complete",
        "Pending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderStatus"


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
epo::GlobalLocation_strategy = st.builds(
    epo::GlobalLocation,
    countryCode=
        st.integers()
)
GlobalLocation_strategy = st.builds(
    GlobalLocation,
)
Address_strategy = st.builds(
    Address,
)
epo::GlobalAddress_strategy = st.builds(
    epo::GlobalAddress,
    location=
        safe_text
)
epo::CanadianAddress_strategy = st.builds(
    epo::CanadianAddress,
    postalCode=
        safe_text,
    province=
        safe_text,
    city=
        safe_text,
    street=
        safe_text
)
epo::USAddress_strategy = st.builds(
    epo::USAddress,
    street=
        safe_text,
    zip=
        st.integers(),
    state=
        safe_text,
    city=
        safe_text
)
epo::PurchaseOrder_strategy = st.builds(
    epo::PurchaseOrder,
    status=
        safe_text,
    orderDate=
        safe_text,
    totalAmount=
        st.integers(),
    comment=
        safe_text
)
epo::Supplier_strategy = st.builds(
    epo::Supplier,
    name=
        safe_text
)
epo::Customer_strategy = st.builds(
    epo::Customer,
    customerID=
        st.integers()
)
epo::Address_strategy = st.builds(
    epo::Address,
    name=
        safe_text,
    country=
        safe_text
)
epo::Item_strategy = st.builds(
    epo::Item,
    productName=
        safe_text,
    quantity=
        st.integers(),
    USPrice=
        st.integers(),
    shipDate=
        safe_text,
    comment=
        safe_text,
    partNum=
        safe_text
)

@given(instance=epo::GlobalLocation_strategy)
@settings(max_examples=50)
def test_epo::globallocation_instantiation(instance):
    assert isinstance(instance, epo::GlobalLocation)

@given(instance=epo::GlobalLocation_strategy)
def test_epo::globallocation_countryCode_type(instance):
    assert isinstance(instance.countryCode, int)


@given(instance=epo::GlobalLocation_strategy)
def test_epo::globallocation_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original

@given(instance=GlobalLocation_strategy)
@settings(max_examples=50)
def test_globallocation_instantiation(instance):
    assert isinstance(instance, GlobalLocation)

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=epo::GlobalAddress_strategy)
@settings(max_examples=50)
def test_epo::globaladdress_instantiation(instance):
    assert isinstance(instance, epo::GlobalAddress)

@given(instance=epo::GlobalAddress_strategy)
def test_epo::globaladdress_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=epo::GlobalAddress_strategy)
def test_epo::globaladdress_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=epo::CanadianAddress_strategy)
@settings(max_examples=50)
def test_epo::canadianaddress_instantiation(instance):
    assert isinstance(instance, epo::CanadianAddress)

@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_postalCode_type(instance):
    assert isinstance(instance.postalCode, str)


@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_postalCode_setter(instance):
    original = instance.postalCode
    instance.postalCode = original
    assert instance.postalCode == original

@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_province_type(instance):
    assert isinstance(instance.province, str)


@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_province_setter(instance):
    original = instance.province
    instance.province = original
    assert instance.province == original

@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=epo::CanadianAddress_strategy)
def test_epo::canadianaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=epo::USAddress_strategy)
@settings(max_examples=50)
def test_epo::usaddress_instantiation(instance):
    assert isinstance(instance, epo::USAddress)

@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_zip_type(instance):
    assert isinstance(instance.zip, int)


@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=epo::USAddress_strategy)
def test_epo::usaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=epo::PurchaseOrder_strategy)
@settings(max_examples=50)
def test_epo::purchaseorder_instantiation(instance):
    assert isinstance(instance, epo::PurchaseOrder)

@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_orderDate_type(instance):
    assert isinstance(instance.orderDate, str)


@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original

@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_totalAmount_type(instance):
    assert isinstance(instance.totalAmount, int)


@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_totalAmount_setter(instance):
    original = instance.totalAmount
    instance.totalAmount = original
    assert instance.totalAmount == original

@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=epo::PurchaseOrder_strategy)
def test_epo::purchaseorder_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=epo::Supplier_strategy)
@settings(max_examples=50)
def test_epo::supplier_instantiation(instance):
    assert isinstance(instance, epo::Supplier)

@given(instance=epo::Supplier_strategy)
def test_epo::supplier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=epo::Supplier_strategy)
def test_epo::supplier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=epo::Customer_strategy)
@settings(max_examples=50)
def test_epo::customer_instantiation(instance):
    assert isinstance(instance, epo::Customer)

@given(instance=epo::Customer_strategy)
def test_epo::customer_customerID_type(instance):
    assert isinstance(instance.customerID, int)


@given(instance=epo::Customer_strategy)
def test_epo::customer_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original

@given(instance=epo::Address_strategy)
@settings(max_examples=50)
def test_epo::address_instantiation(instance):
    assert isinstance(instance, epo::Address)

@given(instance=epo::Address_strategy)
def test_epo::address_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=epo::Address_strategy)
def test_epo::address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=epo::Address_strategy)
def test_epo::address_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=epo::Address_strategy)
def test_epo::address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=epo::Item_strategy)
@settings(max_examples=50)
def test_epo::item_instantiation(instance):
    assert isinstance(instance, epo::Item)

@given(instance=epo::Item_strategy)
def test_epo::item_productName_type(instance):
    assert isinstance(instance.productName, str)


@given(instance=epo::Item_strategy)
def test_epo::item_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original

@given(instance=epo::Item_strategy)
def test_epo::item_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=epo::Item_strategy)
def test_epo::item_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=epo::Item_strategy)
def test_epo::item_USPrice_type(instance):
    assert isinstance(instance.USPrice, int)


@given(instance=epo::Item_strategy)
def test_epo::item_USPrice_setter(instance):
    original = instance.USPrice
    instance.USPrice = original
    assert instance.USPrice == original

@given(instance=epo::Item_strategy)
def test_epo::item_shipDate_type(instance):
    assert isinstance(instance.shipDate, str)


@given(instance=epo::Item_strategy)
def test_epo::item_shipDate_setter(instance):
    original = instance.shipDate
    instance.shipDate = original
    assert instance.shipDate == original

@given(instance=epo::Item_strategy)
def test_epo::item_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=epo::Item_strategy)
def test_epo::item_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=epo::Item_strategy)
def test_epo::item_partNum_type(instance):
    assert isinstance(instance.partNum, str)


@given(instance=epo::Item_strategy)
def test_epo::item_partNum_setter(instance):
    original = instance.partNum
    instance.partNum = original
    assert instance.partNum == original
