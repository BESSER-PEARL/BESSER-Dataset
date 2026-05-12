import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Address,
    customerDsl_POBox,
    customerDsl_StreetAddress,
    customerDsl_Address,
    customerDsl_Product,
    customerDsl_Order,
    customerDsl_Customer,
    customerDsl_CustomerDb,
    OrderChannel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_customerdsl_pobox_is_not_abstract():
    assert not inspect.isabstract(customerDsl_POBox)


def test_customerdsl_pobox_constructor_exists():
    assert callable(customerDsl_POBox.__init__)


def test_customerdsl_pobox_constructor_args():
    sig = inspect.signature(customerDsl_POBox.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_customerdsl_pobox_has_number():
    assert hasattr(customerDsl_POBox, "number")
    descriptor = None
    for klass in customerDsl_POBox.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_streetaddress_is_not_abstract():
    assert not inspect.isabstract(customerDsl_StreetAddress)


def test_customerdsl_streetaddress_constructor_exists():
    assert callable(customerDsl_StreetAddress.__init__)


def test_customerdsl_streetaddress_constructor_args():
    sig = inspect.signature(customerDsl_StreetAddress.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_customerdsl_streetaddress_has_street():
    assert hasattr(customerDsl_StreetAddress, "street")
    descriptor = None
    for klass in customerDsl_StreetAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl_streetaddress_has_city():
    assert hasattr(customerDsl_StreetAddress, "city")
    descriptor = None
    for klass in customerDsl_StreetAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_address_is_not_abstract():
    assert not inspect.isabstract(customerDsl_Address)


def test_customerdsl_address_constructor_exists():
    assert callable(customerDsl_Address.__init__)


def test_customerdsl_address_constructor_args():
    sig = inspect.signature(customerDsl_Address.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "zip" in params, "Missing parameter 'zip'"

def test_customerdsl_address_has_name():
    assert hasattr(customerDsl_Address, "name")
    descriptor = None
    for klass in customerDsl_Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl_address_has_zip():
    assert hasattr(customerDsl_Address, "zip")
    descriptor = None
    for klass in customerDsl_Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_product_is_not_abstract():
    assert not inspect.isabstract(customerDsl_Product)


def test_customerdsl_product_constructor_exists():
    assert callable(customerDsl_Product.__init__)


def test_customerdsl_product_constructor_args():
    sig = inspect.signature(customerDsl_Product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"

def test_customerdsl_product_has_price():
    assert hasattr(customerDsl_Product, "price")
    descriptor = None
    for klass in customerDsl_Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl_product_has_name():
    assert hasattr(customerDsl_Product, "name")
    descriptor = None
    for klass in customerDsl_Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_order_is_not_abstract():
    assert not inspect.isabstract(customerDsl_Order)


def test_customerdsl_order_constructor_exists():
    assert callable(customerDsl_Order.__init__)


def test_customerdsl_order_constructor_args():
    sig = inspect.signature(customerDsl_Order.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "channel" in params, "Missing parameter 'channel'"

def test_customerdsl_order_has_name():
    assert hasattr(customerDsl_Order, "name")
    descriptor = None
    for klass in customerDsl_Order.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl_order_has_channel():
    assert hasattr(customerDsl_Order, "channel")
    descriptor = None
    for klass in customerDsl_Order.__mro__:
        if "channel" in klass.__dict__:
            descriptor = klass.__dict__["channel"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_customer_is_not_abstract():
    assert not inspect.isabstract(customerDsl_Customer)


def test_customerdsl_customer_constructor_exists():
    assert callable(customerDsl_Customer.__init__)


def test_customerdsl_customer_constructor_args():
    sig = inspect.signature(customerDsl_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_customerdsl_customer_has_name():
    assert hasattr(customerDsl_Customer, "name")
    descriptor = None
    for klass in customerDsl_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl_customer_has_fullName():
    assert hasattr(customerDsl_Customer, "fullName")
    descriptor = None
    for klass in customerDsl_Customer.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl_customerdb_is_not_abstract():
    assert not inspect.isabstract(customerDsl_CustomerDb)


def test_customerdsl_customerdb_constructor_exists():
    assert callable(customerDsl_CustomerDb.__init__)


def test_customerdsl_customerdb_constructor_args():
    sig = inspect.signature(customerDsl_CustomerDb.__init__)
    params = list(sig.parameters.keys())

def test_orderchannel_exists():
    # Check that the Enumeration exists
    assert OrderChannel is not None

def test_orderchannel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderChannel]
    expected_literals = [
        "MAIL",
        "PHONE",
        "WEB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderChannel"


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
Address_strategy = st.builds(
    Address,
)
customerDsl_POBox_strategy = st.builds(
    customerDsl_POBox,
    number=
        st.integers()
)
customerDsl_StreetAddress_strategy = st.builds(
    customerDsl_StreetAddress,
    street=
        safe_text,
    city=
        safe_text
)
customerDsl_Address_strategy = st.builds(
    customerDsl_Address,
    name=
        safe_text,
    zip=
        safe_text
)
customerDsl_Product_strategy = st.builds(
    customerDsl_Product,
    price=
        st.integers(),
    name=
        safe_text
)
customerDsl_Order_strategy = st.builds(
    customerDsl_Order,
    name=
        safe_text,
    channel=
        safe_text
)
customerDsl_Customer_strategy = st.builds(
    customerDsl_Customer,
    name=
        safe_text,
    fullName=
        safe_text
)
customerDsl_CustomerDb_strategy = st.builds(
    customerDsl_CustomerDb,
)

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=customerDsl_POBox_strategy)
@settings(max_examples=50)
def test_customerdsl_pobox_instantiation(instance):
    assert isinstance(instance, customerDsl_POBox)



@given(instance=customerDsl_POBox_strategy)
def test_customerdsl_pobox_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=customerDsl_StreetAddress_strategy)
@settings(max_examples=50)
def test_customerdsl_streetaddress_instantiation(instance):
    assert isinstance(instance, customerDsl_StreetAddress)



@given(instance=customerDsl_StreetAddress_strategy)
def test_customerdsl_streetaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=customerDsl_StreetAddress_strategy)
def test_customerdsl_streetaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=customerDsl_Address_strategy)
@settings(max_examples=50)
def test_customerdsl_address_instantiation(instance):
    assert isinstance(instance, customerDsl_Address)



@given(instance=customerDsl_Address_strategy)
def test_customerdsl_address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=customerDsl_Address_strategy)
def test_customerdsl_address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=customerDsl_Product_strategy)
@settings(max_examples=50)
def test_customerdsl_product_instantiation(instance):
    assert isinstance(instance, customerDsl_Product)



@given(instance=customerDsl_Product_strategy)
def test_customerdsl_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=customerDsl_Product_strategy)
def test_customerdsl_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customerDsl_Order_strategy)
@settings(max_examples=50)
def test_customerdsl_order_instantiation(instance):
    assert isinstance(instance, customerDsl_Order)



@given(instance=customerDsl_Order_strategy)
def test_customerdsl_order_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=customerDsl_Order_strategy)
def test_customerdsl_order_channel_setter(instance):
    original = instance.channel
    instance.channel = original
    assert instance.channel == original

@given(instance=customerDsl_Customer_strategy)
@settings(max_examples=50)
def test_customerdsl_customer_instantiation(instance):
    assert isinstance(instance, customerDsl_Customer)



@given(instance=customerDsl_Customer_strategy)
def test_customerdsl_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=customerDsl_Customer_strategy)
def test_customerdsl_customer_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=customerDsl_CustomerDb_strategy)
@settings(max_examples=50)
def test_customerdsl_customerdb_instantiation(instance):
    assert isinstance(instance, customerDsl_CustomerDb)
