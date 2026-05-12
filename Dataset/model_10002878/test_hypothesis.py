import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Service,
    Room,
    Hotel,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())
    assert "basePrice" in params, "Missing parameter 'basePrice'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_service_has_basePrice():
    assert hasattr(Service, "basePrice")
    descriptor = None
    for klass in Service.__mro__:
        if "basePrice" in klass.__dict__:
            descriptor = klass.__dict__["basePrice"]
            break
    assert isinstance(descriptor, property)

def test_service_has_description():
    assert hasattr(Service, "description")
    descriptor = None
    for klass in Service.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_service_has_name():
    assert hasattr(Service, "name")
    descriptor = None
    for klass in Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "door" in params, "Missing parameter 'door'"
    assert "price" in params, "Missing parameter 'price'"
    assert "floor" in params, "Missing parameter 'floor'"

def test_room_has_capacity():
    assert hasattr(Room, "capacity")
    descriptor = None
    for klass in Room.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_room_has_door():
    assert hasattr(Room, "door")
    descriptor = None
    for klass in Room.__mro__:
        if "door" in klass.__dict__:
            descriptor = klass.__dict__["door"]
            break
    assert isinstance(descriptor, property)

def test_room_has_price():
    assert hasattr(Room, "price")
    descriptor = None
    for klass in Room.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_room_has_floor():
    assert hasattr(Room, "floor")
    descriptor = None
    for klass in Room.__mro__:
        if "floor" in klass.__dict__:
            descriptor = klass.__dict__["floor"]
            break
    assert isinstance(descriptor, property)



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "street" in params, "Missing parameter 'street'"
    assert "name" in params, "Missing parameter 'name'"
    assert "website" in params, "Missing parameter 'website'"
    assert "coordinates" in params, "Missing parameter 'coordinates'"
    assert "zip" in params, "Missing parameter 'zip'"

def test_hotel_has_city():
    assert hasattr(Hotel, "city")
    descriptor = None
    for klass in Hotel.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_phoneNumber():
    assert hasattr(Hotel, "phoneNumber")
    descriptor = None
    for klass in Hotel.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_street():
    assert hasattr(Hotel, "street")
    descriptor = None
    for klass in Hotel.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_name():
    assert hasattr(Hotel, "name")
    descriptor = None
    for klass in Hotel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_website():
    assert hasattr(Hotel, "website")
    descriptor = None
    for klass in Hotel.__mro__:
        if "website" in klass.__dict__:
            descriptor = klass.__dict__["website"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_coordinates():
    assert hasattr(Hotel, "coordinates")
    descriptor = None
    for klass in Hotel.__mro__:
        if "coordinates" in klass.__dict__:
            descriptor = klass.__dict__["coordinates"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_zip():
    assert hasattr(Hotel, "zip")
    descriptor = None
    for klass in Hotel.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "ident" in params, "Missing parameter 'ident'"

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_surname():
    assert hasattr(Customer, "surname")
    descriptor = None
    for klass in Customer.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_ident():
    assert hasattr(Customer, "ident")
    descriptor = None
    for klass in Customer.__mro__:
        if "ident" in klass.__dict__:
            descriptor = klass.__dict__["ident"]
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
Service_strategy = st.builds(
    Service,
    basePrice=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
Room_strategy = st.builds(
    Room,
    capacity=
        safe_text,
    door=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    floor=
        st.integers()
)
Hotel_strategy = st.builds(
    Hotel,
    city=
        safe_text,
    phoneNumber=
        st.integers(),
    street=
        safe_text,
    name=
        safe_text,
    website=
        safe_text,
    coordinates=
        st.integers(),
    zip=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    phoneNumber=
        st.integers(),
    email=
        safe_text,
    name=
        safe_text,
    surname=
        safe_text,
    ident=
        safe_text
)

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)



@given(instance=Service_strategy)
def test_service_basePrice_setter(instance):
    original = instance.basePrice
    instance.basePrice = original
    assert instance.basePrice == original



@given(instance=Service_strategy)
def test_service_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Service_strategy)
def test_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=Room_strategy)
def test_room_door_setter(instance):
    original = instance.door
    instance.door = original
    assert instance.door == original



@given(instance=Room_strategy)
def test_room_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Room_strategy)
def test_room_floor_setter(instance):
    original = instance.floor
    instance.floor = original
    assert instance.floor == original

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)



@given(instance=Hotel_strategy)
def test_hotel_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Hotel_strategy)
def test_hotel_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Hotel_strategy)
def test_hotel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=Hotel_strategy)
def test_hotel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hotel_strategy)
def test_hotel_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original



@given(instance=Hotel_strategy)
def test_hotel_coordinates_setter(instance):
    original = instance.coordinates
    instance.coordinates = original
    assert instance.coordinates == original



@given(instance=Hotel_strategy)
def test_hotel_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=Customer_strategy)
def test_customer_ident_setter(instance):
    original = instance.ident
    instance.ident = original
    assert instance.ident == original
