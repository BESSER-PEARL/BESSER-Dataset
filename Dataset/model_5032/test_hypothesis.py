import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    shop::Transaction,
    shop::Order,
    shop::Customer,
    shop::PriceCategory,
    shop::ProductCategory,
    shop::Product,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shop::transaction_is_not_abstract():
    assert not inspect.isabstract(shop::Transaction)


def test_shop::transaction_constructor_exists():
    assert callable(shop::Transaction.__init__)


def test_shop::transaction_constructor_args():
    sig = inspect.signature(shop::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "number" in params, "Missing parameter 'number'"

def test_shop::transaction_has_price():
    assert hasattr(shop::Transaction, "price")
    descriptor = None
    for klass in shop::Transaction.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_shop::transaction_has_paidDate():
    assert hasattr(shop::Transaction, "paidDate")
    descriptor = None
    for klass in shop::Transaction.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
            break
    assert isinstance(descriptor, property)

def test_shop::transaction_has_endDate():
    assert hasattr(shop::Transaction, "endDate")
    descriptor = None
    for klass in shop::Transaction.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_shop::transaction_has_startDate():
    assert hasattr(shop::Transaction, "startDate")
    descriptor = None
    for klass in shop::Transaction.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_shop::transaction_has_number():
    assert hasattr(shop::Transaction, "number")
    descriptor = None
    for klass in shop::Transaction.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_shop::order_is_not_abstract():
    assert not inspect.isabstract(shop::Order)


def test_shop::order_constructor_exists():
    assert callable(shop::Order.__init__)


def test_shop::order_constructor_args():
    sig = inspect.signature(shop::Order.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "comments" in params, "Missing parameter 'comments'"

def test_shop::order_has_number():
    assert hasattr(shop::Order, "number")
    descriptor = None
    for klass in shop::Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_shop::order_has_comments():
    assert hasattr(shop::Order, "comments")
    descriptor = None
    for klass in shop::Order.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_shop::customer_is_not_abstract():
    assert not inspect.isabstract(shop::Customer)


def test_shop::customer_constructor_exists():
    assert callable(shop::Customer.__init__)


def test_shop::customer_constructor_args():
    sig = inspect.signature(shop::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "surname" in params, "Missing parameter 'surname'"
    assert "telephoneNr" in params, "Missing parameter 'telephoneNr'"
    assert "familyName" in params, "Missing parameter 'familyName'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "address" in params, "Missing parameter 'address'"
    assert "hotel" in params, "Missing parameter 'hotel'"

def test_shop::customer_has_surname():
    assert hasattr(shop::Customer, "surname")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_shop::customer_has_telephoneNr():
    assert hasattr(shop::Customer, "telephoneNr")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "telephoneNr" in klass.__dict__:
            descriptor = klass.__dict__["telephoneNr"]
            break
    assert isinstance(descriptor, property)

def test_shop::customer_has_familyName():
    assert hasattr(shop::Customer, "familyName")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "familyName" in klass.__dict__:
            descriptor = klass.__dict__["familyName"]
            break
    assert isinstance(descriptor, property)

def test_shop::customer_has_comments():
    assert hasattr(shop::Customer, "comments")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_shop::customer_has_address():
    assert hasattr(shop::Customer, "address")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_shop::customer_has_hotel():
    assert hasattr(shop::Customer, "hotel")
    descriptor = None
    for klass in shop::Customer.__mro__:
        if "hotel" in klass.__dict__:
            descriptor = klass.__dict__["hotel"]
            break
    assert isinstance(descriptor, property)



def test_shop::pricecategory_is_not_abstract():
    assert not inspect.isabstract(shop::PriceCategory)


def test_shop::pricecategory_constructor_exists():
    assert callable(shop::PriceCategory.__init__)


def test_shop::pricecategory_constructor_args():
    sig = inspect.signature(shop::PriceCategory.__init__)
    params = list(sig.parameters.keys())
    assert "prices" in params, "Missing parameter 'prices'"
    assert "name" in params, "Missing parameter 'name'"

def test_shop::pricecategory_has_prices():
    assert hasattr(shop::PriceCategory, "prices")
    descriptor = None
    for klass in shop::PriceCategory.__mro__:
        if "prices" in klass.__dict__:
            descriptor = klass.__dict__["prices"]
            break
    assert isinstance(descriptor, property)

def test_shop::pricecategory_has_name():
    assert hasattr(shop::PriceCategory, "name")
    descriptor = None
    for klass in shop::PriceCategory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shop::productcategory_is_not_abstract():
    assert not inspect.isabstract(shop::ProductCategory)


def test_shop::productcategory_constructor_exists():
    assert callable(shop::ProductCategory.__init__)


def test_shop::productcategory_constructor_args():
    sig = inspect.signature(shop::ProductCategory.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_shop::productcategory_has_name():
    assert hasattr(shop::ProductCategory, "name")
    descriptor = None
    for klass in shop::ProductCategory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shop::product_is_not_abstract():
    assert not inspect.isabstract(shop::Product)


def test_shop::product_constructor_exists():
    assert callable(shop::Product.__init__)


def test_shop::product_constructor_args():
    sig = inspect.signature(shop::Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "number" in params, "Missing parameter 'number'"
    assert "description" in params, "Missing parameter 'description'"

def test_shop::product_has_name():
    assert hasattr(shop::Product, "name")
    descriptor = None
    for klass in shop::Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_shop::product_has_number():
    assert hasattr(shop::Product, "number")
    descriptor = None
    for klass in shop::Product.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_shop::product_has_description():
    assert hasattr(shop::Product, "description")
    descriptor = None
    for klass in shop::Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
shop::Transaction_strategy = st.builds(
    shop::Transaction,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    paidDate=
        st.dates(),
    endDate=
        st.dates(),
    startDate=
        st.dates(),
    number=
        safe_text
)
shop::Order_strategy = st.builds(
    shop::Order,
    number=
        safe_text,
    comments=
        safe_text
)
shop::Customer_strategy = st.builds(
    shop::Customer,
    surname=
        safe_text,
    telephoneNr=
        safe_text,
    familyName=
        safe_text,
    comments=
        safe_text,
    address=
        safe_text,
    hotel=
        safe_text
)
shop::PriceCategory_strategy = st.builds(
    shop::PriceCategory,
    prices=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
shop::ProductCategory_strategy = st.builds(
    shop::ProductCategory,
    name=
        safe_text
)
shop::Product_strategy = st.builds(
    shop::Product,
    name=
        safe_text,
    number=
        safe_text,
    description=
        safe_text
)

@given(instance=shop::Transaction_strategy)
@settings(max_examples=50)
def test_shop::transaction_instantiation(instance):
    assert isinstance(instance, shop::Transaction)

@given(instance=shop::Transaction_strategy)
def test_shop::transaction_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=shop::Transaction_strategy)
def test_shop::transaction_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=shop::Transaction_strategy)
def test_shop::transaction_paidDate_type(instance):
    assert isinstance(instance.paidDate, date)


@given(instance=shop::Transaction_strategy)
def test_shop::transaction_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original

@given(instance=shop::Transaction_strategy)
def test_shop::transaction_endDate_type(instance):
    assert isinstance(instance.endDate, date)


@given(instance=shop::Transaction_strategy)
def test_shop::transaction_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=shop::Transaction_strategy)
def test_shop::transaction_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=shop::Transaction_strategy)
def test_shop::transaction_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=shop::Transaction_strategy)
def test_shop::transaction_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=shop::Transaction_strategy)
def test_shop::transaction_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=shop::Order_strategy)
@settings(max_examples=50)
def test_shop::order_instantiation(instance):
    assert isinstance(instance, shop::Order)

@given(instance=shop::Order_strategy)
def test_shop::order_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=shop::Order_strategy)
def test_shop::order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=shop::Order_strategy)
def test_shop::order_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=shop::Order_strategy)
def test_shop::order_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=shop::Customer_strategy)
@settings(max_examples=50)
def test_shop::customer_instantiation(instance):
    assert isinstance(instance, shop::Customer)

@given(instance=shop::Customer_strategy)
def test_shop::customer_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=shop::Customer_strategy)
def test_shop::customer_telephoneNr_type(instance):
    assert isinstance(instance.telephoneNr, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_telephoneNr_setter(instance):
    original = instance.telephoneNr
    instance.telephoneNr = original
    assert instance.telephoneNr == original

@given(instance=shop::Customer_strategy)
def test_shop::customer_familyName_type(instance):
    assert isinstance(instance.familyName, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_familyName_setter(instance):
    original = instance.familyName
    instance.familyName = original
    assert instance.familyName == original

@given(instance=shop::Customer_strategy)
def test_shop::customer_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=shop::Customer_strategy)
def test_shop::customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=shop::Customer_strategy)
def test_shop::customer_hotel_type(instance):
    assert isinstance(instance.hotel, str)


@given(instance=shop::Customer_strategy)
def test_shop::customer_hotel_setter(instance):
    original = instance.hotel
    instance.hotel = original
    assert instance.hotel == original

@given(instance=shop::PriceCategory_strategy)
@settings(max_examples=50)
def test_shop::pricecategory_instantiation(instance):
    assert isinstance(instance, shop::PriceCategory)

@given(instance=shop::PriceCategory_strategy)
def test_shop::pricecategory_prices_type(instance):
    assert isinstance(instance.prices, float)


@given(instance=shop::PriceCategory_strategy)
def test_shop::pricecategory_prices_setter(instance):
    original = instance.prices
    instance.prices = original
    assert instance.prices == original

@given(instance=shop::PriceCategory_strategy)
def test_shop::pricecategory_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shop::PriceCategory_strategy)
def test_shop::pricecategory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shop::ProductCategory_strategy)
@settings(max_examples=50)
def test_shop::productcategory_instantiation(instance):
    assert isinstance(instance, shop::ProductCategory)

@given(instance=shop::ProductCategory_strategy)
def test_shop::productcategory_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shop::ProductCategory_strategy)
def test_shop::productcategory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shop::Product_strategy)
@settings(max_examples=50)
def test_shop::product_instantiation(instance):
    assert isinstance(instance, shop::Product)

@given(instance=shop::Product_strategy)
def test_shop::product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=shop::Product_strategy)
def test_shop::product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=shop::Product_strategy)
def test_shop::product_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=shop::Product_strategy)
def test_shop::product_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=shop::Product_strategy)
def test_shop::product_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=shop::Product_strategy)
def test_shop::product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
