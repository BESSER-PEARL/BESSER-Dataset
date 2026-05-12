import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Buyer,
    User,
    Category,
    Offer,
    Product,
    Order,
    Store,
    Address,
    Position,
    Basket,
    Seller,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_buyer_is_not_abstract():
    assert not inspect.isabstract(Buyer)


def test_buyer_constructor_exists():
    assert callable(Buyer.__init__)


def test_buyer_constructor_args():
    sig = inspect.signature(Buyer.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"

def test_buyer_has_email():
    assert hasattr(Buyer, "email")
    descriptor = None
    for klass in Buyer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "username" in params, "Missing parameter 'username'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_user_has_attribute():
    assert hasattr(User, "attribute")
    descriptor = None
    for klass in User.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_firstname():
    assert hasattr(User, "firstname")
    descriptor = None
    for klass in User.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_lastname():
    assert hasattr(User, "lastname")
    descriptor = None
    for klass in User.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id():
    assert hasattr(User, "id")
    descriptor = None
    for klass in User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "photoPath" in params, "Missing parameter 'photoPath'"

def test_category_has_id():
    assert hasattr(Category, "id")
    descriptor = None
    for klass in Category.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_category_has_name():
    assert hasattr(Category, "name")
    descriptor = None
    for klass in Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_category_has_photoPath():
    assert hasattr(Category, "photoPath")
    descriptor = None
    for klass in Category.__mro__:
        if "photoPath" in klass.__dict__:
            descriptor = klass.__dict__["photoPath"]
            break
    assert isinstance(descriptor, property)



def test_offer_is_not_abstract():
    assert not inspect.isabstract(Offer)


def test_offer_constructor_exists():
    assert callable(Offer.__init__)


def test_offer_constructor_args():
    sig = inspect.signature(Offer.__init__)
    params = list(sig.parameters.keys())
    assert "beginDate" in params, "Missing parameter 'beginDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "discount" in params, "Missing parameter 'discount'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_offer_has_beginDate():
    assert hasattr(Offer, "beginDate")
    descriptor = None
    for klass in Offer.__mro__:
        if "beginDate" in klass.__dict__:
            descriptor = klass.__dict__["beginDate"]
            break
    assert isinstance(descriptor, property)

def test_offer_has_id():
    assert hasattr(Offer, "id")
    descriptor = None
    for klass in Offer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_offer_has_discount():
    assert hasattr(Offer, "discount")
    descriptor = None
    for klass in Offer.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
            break
    assert isinstance(descriptor, property)

def test_offer_has_endDate():
    assert hasattr(Offer, "endDate")
    descriptor = None
    for klass in Offer.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "photoPath" in params, "Missing parameter 'photoPath'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_photoPath():
    assert hasattr(Product, "photoPath")
    descriptor = None
    for klass in Product.__mro__:
        if "photoPath" in klass.__dict__:
            descriptor = klass.__dict__["photoPath"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(Product, "price")
    descriptor = None
    for klass in Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_product_has_id():
    assert hasattr(Product, "id")
    descriptor = None
    for klass in Product.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "id" in params, "Missing parameter 'id'"

def test_order_has_amount():
    assert hasattr(Order, "amount")
    descriptor = None
    for klass in Order.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_order_has_createdAt():
    assert hasattr(Order, "createdAt")
    descriptor = None
    for klass in Order.__mro__:
        if "createdAt" in klass.__dict__:
            descriptor = klass.__dict__["createdAt"]
            break
    assert isinstance(descriptor, property)

def test_order_has_id():
    assert hasattr(Order, "id")
    descriptor = None
    for klass in Order.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_store_constructor_exists():
    assert callable(Store.__init__)


def test_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "photoPath" in params, "Missing parameter 'photoPath'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_store_has_photoPath():
    assert hasattr(Store, "photoPath")
    descriptor = None
    for klass in Store.__mro__:
        if "photoPath" in klass.__dict__:
            descriptor = klass.__dict__["photoPath"]
            break
    assert isinstance(descriptor, property)

def test_store_has_name():
    assert hasattr(Store, "name")
    descriptor = None
    for klass in Store.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_store_has_id():
    assert hasattr(Store, "id")
    descriptor = None
    for klass in Store.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"
    assert "id" in params, "Missing parameter 'id'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"

def test_address_has_country():
    assert hasattr(Address, "country")
    descriptor = None
    for klass in Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_address_has_street():
    assert hasattr(Address, "street")
    descriptor = None
    for klass in Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_address_has_city():
    assert hasattr(Address, "city")
    descriptor = None
    for klass in Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_address_has_id():
    assert hasattr(Address, "id")
    descriptor = None
    for klass in Address.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_address_has_zipCode():
    assert hasattr(Address, "zipCode")
    descriptor = None
    for klass in Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "latitude" in params, "Missing parameter 'latitude'"

def test_position_has_id():
    assert hasattr(Position, "id")
    descriptor = None
    for klass in Position.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_position_has_createdAt():
    assert hasattr(Position, "createdAt")
    descriptor = None
    for klass in Position.__mro__:
        if "createdAt" in klass.__dict__:
            descriptor = klass.__dict__["createdAt"]
            break
    assert isinstance(descriptor, property)

def test_position_has_longitude():
    assert hasattr(Position, "longitude")
    descriptor = None
    for klass in Position.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_position_has_latitude():
    assert hasattr(Position, "latitude")
    descriptor = None
    for klass in Position.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)



def test_basket_is_not_abstract():
    assert not inspect.isabstract(Basket)


def test_basket_constructor_exists():
    assert callable(Basket.__init__)


def test_basket_constructor_args():
    sig = inspect.signature(Basket.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "updatedAt" in params, "Missing parameter 'updatedAt'"

def test_basket_has_id():
    assert hasattr(Basket, "id")
    descriptor = None
    for klass in Basket.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_basket_has_updatedAt():
    assert hasattr(Basket, "updatedAt")
    descriptor = None
    for klass in Basket.__mro__:
        if "updatedAt" in klass.__dict__:
            descriptor = klass.__dict__["updatedAt"]
            break
    assert isinstance(descriptor, property)



def test_seller_is_not_abstract():
    assert not inspect.isabstract(Seller)


def test_seller_constructor_exists():
    assert callable(Seller.__init__)


def test_seller_constructor_args():
    sig = inspect.signature(Seller.__init__)
    params = list(sig.parameters.keys())
    assert "registerNumber" in params, "Missing parameter 'registerNumber'"

def test_seller_has_registerNumber():
    assert hasattr(Seller, "registerNumber")
    descriptor = None
    for klass in Seller.__mro__:
        if "registerNumber" in klass.__dict__:
            descriptor = klass.__dict__["registerNumber"]
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
Buyer_strategy = st.builds(
    Buyer,
    email=
        safe_text
)
User_strategy = st.builds(
    User,
    attribute=
        safe_text,
    username=
        safe_text,
    firstname=
        safe_text,
    lastname=
        safe_text,
    password=
        safe_text,
    id=
        safe_text
)
Category_strategy = st.builds(
    Category,
    id=
        st.integers(),
    name=
        safe_text,
    photoPath=
        safe_text
)
Offer_strategy = st.builds(
    Offer,
    beginDate=
        safe_text,
    id=
        st.integers(),
    discount=
        st.integers(),
    endDate=
        safe_text
)
Product_strategy = st.builds(
    Product,
    description=
        safe_text,
    name=
        safe_text,
    photoPath=
        safe_text,
    price=
        st.integers(),
    id=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    amount=
        st.integers(),
    createdAt=
        safe_text,
    id=
        st.integers()
)
Store_strategy = st.builds(
    Store,
    photoPath=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)
Address_strategy = st.builds(
    Address,
    country=
        safe_text,
    street=
        safe_text,
    city=
        safe_text,
    id=
        st.integers(),
    zipCode=
        safe_text
)
Position_strategy = st.builds(
    Position,
    id=
        st.integers(),
    createdAt=
        safe_text,
    longitude=
        safe_text,
    latitude=
        safe_text
)
Basket_strategy = st.builds(
    Basket,
    id=
        st.integers(),
    updatedAt=
        safe_text
)
Seller_strategy = st.builds(
    Seller,
    registerNumber=
        safe_text
)

@given(instance=Buyer_strategy)
@settings(max_examples=50)
def test_buyer_instantiation(instance):
    assert isinstance(instance, Buyer)



@given(instance=Buyer_strategy)
def test_buyer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_user_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=User_strategy)
def test_user_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_category_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Category_strategy)
def test_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Category_strategy)
def test_category_photoPath_setter(instance):
    original = instance.photoPath
    instance.photoPath = original
    assert instance.photoPath == original

@given(instance=Offer_strategy)
@settings(max_examples=50)
def test_offer_instantiation(instance):
    assert isinstance(instance, Offer)



@given(instance=Offer_strategy)
def test_offer_beginDate_setter(instance):
    original = instance.beginDate
    instance.beginDate = original
    assert instance.beginDate == original



@given(instance=Offer_strategy)
def test_offer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Offer_strategy)
def test_offer_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original



@given(instance=Offer_strategy)
def test_offer_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_photoPath_setter(instance):
    original = instance.photoPath
    instance.photoPath = original
    assert instance.photoPath == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_product_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Order_strategy)
def test_order_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=Order_strategy)
def test_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Store_strategy)
@settings(max_examples=50)
def test_store_instantiation(instance):
    assert isinstance(instance, Store)



@given(instance=Store_strategy)
def test_store_photoPath_setter(instance):
    original = instance.photoPath
    instance.photoPath = original
    assert instance.photoPath == original



@given(instance=Store_strategy)
def test_store_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Store_strategy)
def test_store_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)



@given(instance=Address_strategy)
def test_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Address_strategy)
def test_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=Address_strategy)
def test_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Address_strategy)
def test_address_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Address_strategy)
def test_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)



@given(instance=Position_strategy)
def test_position_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Position_strategy)
def test_position_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=Position_strategy)
def test_position_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original



@given(instance=Position_strategy)
def test_position_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original

@given(instance=Basket_strategy)
@settings(max_examples=50)
def test_basket_instantiation(instance):
    assert isinstance(instance, Basket)



@given(instance=Basket_strategy)
def test_basket_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Basket_strategy)
def test_basket_updatedAt_setter(instance):
    original = instance.updatedAt
    instance.updatedAt = original
    assert instance.updatedAt == original

@given(instance=Seller_strategy)
@settings(max_examples=50)
def test_seller_instantiation(instance):
    assert isinstance(instance, Seller)



@given(instance=Seller_strategy)
def test_seller_registerNumber_setter(instance):
    original = instance.registerNumber
    instance.registerNumber = original
    assert instance.registerNumber == original
