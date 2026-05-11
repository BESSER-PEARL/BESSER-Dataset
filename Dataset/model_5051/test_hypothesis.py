import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Address,
    customerDsl::POBox,
    customerDsl::StreetAddress,
    customerDsl::Address,
    customerDsl::Product,
    customerDsl::Order,
    customerDsl::Customer,
    customerDsl::CustomerDb,
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



def test_customerdsl::pobox_is_not_abstract():
    assert not inspect.isabstract(customerDsl::POBox)


def test_customerdsl::pobox_constructor_exists():
    assert callable(customerDsl::POBox.__init__)


def test_customerdsl::pobox_constructor_args():
    sig = inspect.signature(customerDsl::POBox.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_customerdsl::pobox_has_number():
    assert hasattr(customerDsl::POBox, "number")
    descriptor = None
    for klass in customerDsl::POBox.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::streetaddress_is_not_abstract():
    assert not inspect.isabstract(customerDsl::StreetAddress)


def test_customerdsl::streetaddress_constructor_exists():
    assert callable(customerDsl::StreetAddress.__init__)


def test_customerdsl::streetaddress_constructor_args():
    sig = inspect.signature(customerDsl::StreetAddress.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "street" in params, "Missing parameter 'street'"

def test_customerdsl::streetaddress_has_city():
    assert hasattr(customerDsl::StreetAddress, "city")
    descriptor = None
    for klass in customerDsl::StreetAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl::streetaddress_has_street():
    assert hasattr(customerDsl::StreetAddress, "street")
    descriptor = None
    for klass in customerDsl::StreetAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::address_is_not_abstract():
    assert not inspect.isabstract(customerDsl::Address)


def test_customerdsl::address_constructor_exists():
    assert callable(customerDsl::Address.__init__)


def test_customerdsl::address_constructor_args():
    sig = inspect.signature(customerDsl::Address.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "zip" in params, "Missing parameter 'zip'"

def test_customerdsl::address_has_name():
    assert hasattr(customerDsl::Address, "name")
    descriptor = None
    for klass in customerDsl::Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl::address_has_zip():
    assert hasattr(customerDsl::Address, "zip")
    descriptor = None
    for klass in customerDsl::Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::product_is_not_abstract():
    assert not inspect.isabstract(customerDsl::Product)


def test_customerdsl::product_constructor_exists():
    assert callable(customerDsl::Product.__init__)


def test_customerdsl::product_constructor_args():
    sig = inspect.signature(customerDsl::Product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"

def test_customerdsl::product_has_price():
    assert hasattr(customerDsl::Product, "price")
    descriptor = None
    for klass in customerDsl::Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl::product_has_name():
    assert hasattr(customerDsl::Product, "name")
    descriptor = None
    for klass in customerDsl::Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::order_is_not_abstract():
    assert not inspect.isabstract(customerDsl::Order)


def test_customerdsl::order_constructor_exists():
    assert callable(customerDsl::Order.__init__)


def test_customerdsl::order_constructor_args():
    sig = inspect.signature(customerDsl::Order.__init__)
    params = list(sig.parameters.keys())
    assert "channel" in params, "Missing parameter 'channel'"
    assert "name" in params, "Missing parameter 'name'"

def test_customerdsl::order_has_channel():
    assert hasattr(customerDsl::Order, "channel")
    descriptor = None
    for klass in customerDsl::Order.__mro__:
        if "channel" in klass.__dict__:
            descriptor = klass.__dict__["channel"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl::order_has_name():
    assert hasattr(customerDsl::Order, "name")
    descriptor = None
    for klass in customerDsl::Order.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::customer_is_not_abstract():
    assert not inspect.isabstract(customerDsl::Customer)


def test_customerdsl::customer_constructor_exists():
    assert callable(customerDsl::Customer.__init__)


def test_customerdsl::customer_constructor_args():
    sig = inspect.signature(customerDsl::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "name" in params, "Missing parameter 'name'"

def test_customerdsl::customer_has_fullName():
    assert hasattr(customerDsl::Customer, "fullName")
    descriptor = None
    for klass in customerDsl::Customer.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_customerdsl::customer_has_name():
    assert hasattr(customerDsl::Customer, "name")
    descriptor = None
    for klass in customerDsl::Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customerdsl::customerdb_is_not_abstract():
    assert not inspect.isabstract(customerDsl::CustomerDb)


def test_customerdsl::customerdb_constructor_exists():
    assert callable(customerDsl::CustomerDb.__init__)


def test_customerdsl::customerdb_constructor_args():
    sig = inspect.signature(customerDsl::CustomerDb.__init__)
    params = list(sig.parameters.keys())

def test_orderchannel_exists():
    # Check that the Enumeration exists
    assert OrderChannel is not None

def test_orderchannel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderChannel]
    expected_literals = [
        "WEB",
        "PHONE",
        "MAIL",
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
customerDsl::POBox_strategy = st.builds(
    customerDsl::POBox,
    number=
        st.integers()
)
customerDsl::StreetAddress_strategy = st.builds(
    customerDsl::StreetAddress,
    city=
        safe_text,
    street=
        safe_text
)
customerDsl::Address_strategy = st.builds(
    customerDsl::Address,
    name=
        safe_text,
    zip=
        safe_text
)
customerDsl::Product_strategy = st.builds(
    customerDsl::Product,
    price=
        st.integers(),
    name=
        safe_text
)
customerDsl::Order_strategy = st.builds(
    customerDsl::Order,
    channel=
        safe_text,
    name=
        safe_text
)
customerDsl::Customer_strategy = st.builds(
    customerDsl::Customer,
    fullName=
        safe_text,
    name=
        safe_text
)
customerDsl::CustomerDb_strategy = st.builds(
    customerDsl::CustomerDb,
)

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=customerDsl::POBox_strategy)
@settings(max_examples=50)
def test_customerdsl::pobox_instantiation(instance):
    assert isinstance(instance, customerDsl::POBox)

@given(instance=customerDsl::POBox_strategy)
def test_customerdsl::pobox_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=customerDsl::POBox_strategy)
def test_customerdsl::pobox_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=customerDsl::StreetAddress_strategy)
@settings(max_examples=50)
def test_customerdsl::streetaddress_instantiation(instance):
    assert isinstance(instance, customerDsl::StreetAddress)

@given(instance=customerDsl::StreetAddress_strategy)
def test_customerdsl::streetaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=customerDsl::StreetAddress_strategy)
def test_customerdsl::streetaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=customerDsl::StreetAddress_strategy)
def test_customerdsl::streetaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=customerDsl::StreetAddress_strategy)
def test_customerdsl::streetaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=customerDsl::Address_strategy)
@settings(max_examples=50)
def test_customerdsl::address_instantiation(instance):
    assert isinstance(instance, customerDsl::Address)

@given(instance=customerDsl::Address_strategy)
def test_customerdsl::address_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=customerDsl::Address_strategy)
def test_customerdsl::address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customerDsl::Address_strategy)
def test_customerdsl::address_zip_type(instance):
    assert isinstance(instance.zip, str)


@given(instance=customerDsl::Address_strategy)
def test_customerdsl::address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=customerDsl::Product_strategy)
@settings(max_examples=50)
def test_customerdsl::product_instantiation(instance):
    assert isinstance(instance, customerDsl::Product)

@given(instance=customerDsl::Product_strategy)
def test_customerdsl::product_price_type(instance):
    assert isinstance(instance.price, int)


@given(instance=customerDsl::Product_strategy)
def test_customerdsl::product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=customerDsl::Product_strategy)
def test_customerdsl::product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=customerDsl::Product_strategy)
def test_customerdsl::product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customerDsl::Order_strategy)
@settings(max_examples=50)
def test_customerdsl::order_instantiation(instance):
    assert isinstance(instance, customerDsl::Order)

@given(instance=customerDsl::Order_strategy)
def test_customerdsl::order_channel_type(instance):
    assert isinstance(instance.channel, str)


@given(instance=customerDsl::Order_strategy)
def test_customerdsl::order_channel_setter(instance):
    original = instance.channel
    instance.channel = original
    assert instance.channel == original

@given(instance=customerDsl::Order_strategy)
def test_customerdsl::order_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=customerDsl::Order_strategy)
def test_customerdsl::order_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customerDsl::Customer_strategy)
@settings(max_examples=50)
def test_customerdsl::customer_instantiation(instance):
    assert isinstance(instance, customerDsl::Customer)

@given(instance=customerDsl::Customer_strategy)
def test_customerdsl::customer_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=customerDsl::Customer_strategy)
def test_customerdsl::customer_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=customerDsl::Customer_strategy)
def test_customerdsl::customer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=customerDsl::Customer_strategy)
def test_customerdsl::customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=customerDsl::CustomerDb_strategy)
@settings(max_examples=50)
def test_customerdsl::customerdb_instantiation(instance):
    assert isinstance(instance, customerDsl::CustomerDb)
