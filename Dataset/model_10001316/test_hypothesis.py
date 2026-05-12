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
    Users,
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
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_service_has_basePrice():
    assert hasattr(Service, "basePrice")
    descriptor = None
    for klass in Service.__mro__:
        if "basePrice" in klass.__dict__:
            descriptor = klass.__dict__["basePrice"]
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

def test_service_has_description():
    assert hasattr(Service, "description")
    descriptor = None
    for klass in Service.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "room_name" in params, "Missing parameter 'room_name'"
    assert "room_no_bedroom" in params, "Missing parameter 'room_no_bedroom'"
    assert "room_id" in params, "Missing parameter 'room_id'"
    assert "room_rent_night" in params, "Missing parameter 'room_rent_night'"
    assert "room_size_interior" in params, "Missing parameter 'room_size_interior'"
    assert "room_no_bathroom" in params, "Missing parameter 'room_no_bathroom'"

def test_room_has_room_name():
    assert hasattr(Room, "room_name")
    descriptor = None
    for klass in Room.__mro__:
        if "room_name" in klass.__dict__:
            descriptor = klass.__dict__["room_name"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_no_bedroom():
    assert hasattr(Room, "room_no_bedroom")
    descriptor = None
    for klass in Room.__mro__:
        if "room_no_bedroom" in klass.__dict__:
            descriptor = klass.__dict__["room_no_bedroom"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_id():
    assert hasattr(Room, "room_id")
    descriptor = None
    for klass in Room.__mro__:
        if "room_id" in klass.__dict__:
            descriptor = klass.__dict__["room_id"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_rent_night():
    assert hasattr(Room, "room_rent_night")
    descriptor = None
    for klass in Room.__mro__:
        if "room_rent_night" in klass.__dict__:
            descriptor = klass.__dict__["room_rent_night"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_size_interior():
    assert hasattr(Room, "room_size_interior")
    descriptor = None
    for klass in Room.__mro__:
        if "room_size_interior" in klass.__dict__:
            descriptor = klass.__dict__["room_size_interior"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_no_bathroom():
    assert hasattr(Room, "room_no_bathroom")
    descriptor = None
    for klass in Room.__mro__:
        if "room_no_bathroom" in klass.__dict__:
            descriptor = klass.__dict__["room_no_bathroom"]
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
    assert "coordinates" in params, "Missing parameter 'coordinates'"
    assert "name" in params, "Missing parameter 'name'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "website" in params, "Missing parameter 'website'"

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

def test_hotel_has_coordinates():
    assert hasattr(Hotel, "coordinates")
    descriptor = None
    for klass in Hotel.__mro__:
        if "coordinates" in klass.__dict__:
            descriptor = klass.__dict__["coordinates"]
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

def test_hotel_has_zip():
    assert hasattr(Hotel, "zip")
    descriptor = None
    for klass in Hotel.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
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

def test_hotel_has_website():
    assert hasattr(Hotel, "website")
    descriptor = None
    for klass in Hotel.__mro__:
        if "website" in klass.__dict__:
            descriptor = klass.__dict__["website"]
            break
    assert isinstance(descriptor, property)



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "user_phone_no" in params, "Missing parameter 'user_phone_no'"
    assert "user_addr_city" in params, "Missing parameter 'user_addr_city'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "user_mail" in params, "Missing parameter 'user_mail'"
    assert "user_role" in params, "Missing parameter 'user_role'"
    assert "user_address1" in params, "Missing parameter 'user_address1'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "user_addr_state" in params, "Missing parameter 'user_addr_state'"
    assert "user_address" in params, "Missing parameter 'user_address'"

def test_users_has_user_phone_no():
    assert hasattr(Users, "user_phone_no")
    descriptor = None
    for klass in Users.__mro__:
        if "user_phone_no" in klass.__dict__:
            descriptor = klass.__dict__["user_phone_no"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_addr_city():
    assert hasattr(Users, "user_addr_city")
    descriptor = None
    for klass in Users.__mro__:
        if "user_addr_city" in klass.__dict__:
            descriptor = klass.__dict__["user_addr_city"]
            break
    assert isinstance(descriptor, property)

def test_users_has_first_name():
    assert hasattr(Users, "first_name")
    descriptor = None
    for klass in Users.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_mail():
    assert hasattr(Users, "user_mail")
    descriptor = None
    for klass in Users.__mro__:
        if "user_mail" in klass.__dict__:
            descriptor = klass.__dict__["user_mail"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_role():
    assert hasattr(Users, "user_role")
    descriptor = None
    for klass in Users.__mro__:
        if "user_role" in klass.__dict__:
            descriptor = klass.__dict__["user_role"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_address1():
    assert hasattr(Users, "user_address1")
    descriptor = None
    for klass in Users.__mro__:
        if "user_address1" in klass.__dict__:
            descriptor = klass.__dict__["user_address1"]
            break
    assert isinstance(descriptor, property)

def test_users_has_last_name():
    assert hasattr(Users, "last_name")
    descriptor = None
    for klass in Users.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_addr_state():
    assert hasattr(Users, "user_addr_state")
    descriptor = None
    for klass in Users.__mro__:
        if "user_addr_state" in klass.__dict__:
            descriptor = klass.__dict__["user_addr_state"]
            break
    assert isinstance(descriptor, property)

def test_users_has_user_address():
    assert hasattr(Users, "user_address")
    descriptor = None
    for klass in Users.__mro__:
        if "user_address" in klass.__dict__:
            descriptor = klass.__dict__["user_address"]
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
    name=
        safe_text,
    description=
        safe_text
)
Room_strategy = st.builds(
    Room,
    room_name=
        safe_text,
    room_no_bedroom=
        st.integers(),
    room_id=
        st.integers(),
    room_rent_night=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    room_size_interior=
        st.integers(),
    room_no_bathroom=
        st.integers()
)
Hotel_strategy = st.builds(
    Hotel,
    city=
        safe_text,
    phoneNumber=
        st.integers(),
    coordinates=
        st.integers(),
    name=
        safe_text,
    zip=
        st.integers(),
    street=
        safe_text,
    website=
        safe_text
)
Users_strategy = st.builds(
    Users,
    user_phone_no=
        st.integers(),
    user_addr_city=
        safe_text,
    first_name=
        safe_text,
    user_mail=
        safe_text,
    user_role=
        safe_text,
    user_address1=
        safe_text,
    last_name=
        st.integers(),
    user_addr_state=
        safe_text,
    user_address=
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
def test_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Service_strategy)
def test_service_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_room_name_setter(instance):
    original = instance.room_name
    instance.room_name = original
    assert instance.room_name == original



@given(instance=Room_strategy)
def test_room_room_no_bedroom_setter(instance):
    original = instance.room_no_bedroom
    instance.room_no_bedroom = original
    assert instance.room_no_bedroom == original



@given(instance=Room_strategy)
def test_room_room_id_setter(instance):
    original = instance.room_id
    instance.room_id = original
    assert instance.room_id == original



@given(instance=Room_strategy)
def test_room_room_rent_night_setter(instance):
    original = instance.room_rent_night
    instance.room_rent_night = original
    assert instance.room_rent_night == original



@given(instance=Room_strategy)
def test_room_room_size_interior_setter(instance):
    original = instance.room_size_interior
    instance.room_size_interior = original
    assert instance.room_size_interior == original



@given(instance=Room_strategy)
def test_room_room_no_bathroom_setter(instance):
    original = instance.room_no_bathroom
    instance.room_no_bathroom = original
    assert instance.room_no_bathroom == original

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
def test_hotel_coordinates_setter(instance):
    original = instance.coordinates
    instance.coordinates = original
    assert instance.coordinates == original



@given(instance=Hotel_strategy)
def test_hotel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hotel_strategy)
def test_hotel_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=Hotel_strategy)
def test_hotel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=Hotel_strategy)
def test_hotel_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_user_phone_no_setter(instance):
    original = instance.user_phone_no
    instance.user_phone_no = original
    assert instance.user_phone_no == original



@given(instance=Users_strategy)
def test_users_user_addr_city_setter(instance):
    original = instance.user_addr_city
    instance.user_addr_city = original
    assert instance.user_addr_city == original



@given(instance=Users_strategy)
def test_users_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=Users_strategy)
def test_users_user_mail_setter(instance):
    original = instance.user_mail
    instance.user_mail = original
    assert instance.user_mail == original



@given(instance=Users_strategy)
def test_users_user_role_setter(instance):
    original = instance.user_role
    instance.user_role = original
    assert instance.user_role == original



@given(instance=Users_strategy)
def test_users_user_address1_setter(instance):
    original = instance.user_address1
    instance.user_address1 = original
    assert instance.user_address1 == original



@given(instance=Users_strategy)
def test_users_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=Users_strategy)
def test_users_user_addr_state_setter(instance):
    original = instance.user_addr_state
    instance.user_addr_state = original
    assert instance.user_addr_state == original



@given(instance=Users_strategy)
def test_users_user_address_setter(instance):
    original = instance.user_address
    instance.user_address = original
    assert instance.user_address == original
