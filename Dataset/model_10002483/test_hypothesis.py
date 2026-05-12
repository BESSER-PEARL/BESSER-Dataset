import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    occupancy,
    Booking,
    User,
    Location,
    Rooms,
    Hotels,
    Owner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_occupancy_is_not_abstract():
    assert not inspect.isabstract(occupancy)


def test_occupancy_constructor_exists():
    assert callable(occupancy.__init__)


def test_occupancy_constructor_args():
    sig = inspect.signature(occupancy.__init__)
    params = list(sig.parameters.keys())
    assert "booking_id" in params, "Missing parameter 'booking_id'"

def test_occupancy_has_booking_id():
    assert hasattr(occupancy, "booking_id")
    descriptor = None
    for klass in occupancy.__mro__:
        if "booking_id" in klass.__dict__:
            descriptor = klass.__dict__["booking_id"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "guest_adress" in params, "Missing parameter 'guest_adress'"
    assert "guest_id" in params, "Missing parameter 'guest_id'"
    assert "guest_name" in params, "Missing parameter 'guest_name'"
    assert "guestphn_no" in params, "Missing parameter 'guestphn_no'"

def test_booking_has_booking_id():
    assert hasattr(Booking, "booking_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "booking_id" in klass.__dict__:
            descriptor = klass.__dict__["booking_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_user_id():
    assert hasattr(Booking, "user_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_guest_adress():
    assert hasattr(Booking, "guest_adress")
    descriptor = None
    for klass in Booking.__mro__:
        if "guest_adress" in klass.__dict__:
            descriptor = klass.__dict__["guest_adress"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_guest_id():
    assert hasattr(Booking, "guest_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "guest_id" in klass.__dict__:
            descriptor = klass.__dict__["guest_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_guest_name():
    assert hasattr(Booking, "guest_name")
    descriptor = None
    for klass in Booking.__mro__:
        if "guest_name" in klass.__dict__:
            descriptor = klass.__dict__["guest_name"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_guestphn_no():
    assert hasattr(Booking, "guestphn_no")
    descriptor = None
    for klass in Booking.__mro__:
        if "guestphn_no" in klass.__dict__:
            descriptor = klass.__dict__["guestphn_no"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"
    assert "address" in params, "Missing parameter 'address'"
    assert "mail_id" in params, "Missing parameter 'mail_id'"
    assert "phn_no" in params, "Missing parameter 'phn_no'"

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_address():
    assert hasattr(User, "address")
    descriptor = None
    for klass in User.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_mail_id():
    assert hasattr(User, "mail_id")
    descriptor = None
    for klass in User.__mro__:
        if "mail_id" in klass.__dict__:
            descriptor = klass.__dict__["mail_id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phn_no():
    assert hasattr(User, "phn_no")
    descriptor = None
    for klass in User.__mro__:
        if "phn_no" in klass.__dict__:
            descriptor = klass.__dict__["phn_no"]
            break
    assert isinstance(descriptor, property)



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "loc_name" in params, "Missing parameter 'loc_name'"
    assert "loc_id" in params, "Missing parameter 'loc_id'"

def test_location_has_attribute():
    assert hasattr(Location, "attribute")
    descriptor = None
    for klass in Location.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_location_has_loc_name():
    assert hasattr(Location, "loc_name")
    descriptor = None
    for klass in Location.__mro__:
        if "loc_name" in klass.__dict__:
            descriptor = klass.__dict__["loc_name"]
            break
    assert isinstance(descriptor, property)

def test_location_has_loc_id():
    assert hasattr(Location, "loc_id")
    descriptor = None
    for klass in Location.__mro__:
        if "loc_id" in klass.__dict__:
            descriptor = klass.__dict__["loc_id"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "room_description" in params, "Missing parameter 'room_description'"
    assert "checkout_date" in params, "Missing parameter 'checkout_date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "price" in params, "Missing parameter 'price'"
    assert "checkin_date" in params, "Missing parameter 'checkin_date'"

def test_rooms_has_name():
    assert hasattr(Rooms, "name")
    descriptor = None
    for klass in Rooms.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_room_description():
    assert hasattr(Rooms, "room_description")
    descriptor = None
    for klass in Rooms.__mro__:
        if "room_description" in klass.__dict__:
            descriptor = klass.__dict__["room_description"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_checkout_date():
    assert hasattr(Rooms, "checkout_date")
    descriptor = None
    for klass in Rooms.__mro__:
        if "checkout_date" in klass.__dict__:
            descriptor = klass.__dict__["checkout_date"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_id():
    assert hasattr(Rooms, "id")
    descriptor = None
    for klass in Rooms.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_price():
    assert hasattr(Rooms, "price")
    descriptor = None
    for klass in Rooms.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_checkin_date():
    assert hasattr(Rooms, "checkin_date")
    descriptor = None
    for klass in Rooms.__mro__:
        if "checkin_date" in klass.__dict__:
            descriptor = klass.__dict__["checkin_date"]
            break
    assert isinstance(descriptor, property)



def test_hotels_is_not_abstract():
    assert not inspect.isabstract(Hotels)


def test_hotels_constructor_exists():
    assert callable(Hotels.__init__)


def test_hotels_constructor_args():
    sig = inspect.signature(Hotels.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hotel_description" in params, "Missing parameter 'hotel_description'"

def test_hotels_has_id():
    assert hasattr(Hotels, "id")
    descriptor = None
    for klass in Hotels.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hotels_has_name():
    assert hasattr(Hotels, "name")
    descriptor = None
    for klass in Hotels.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hotels_has_hotel_description():
    assert hasattr(Hotels, "hotel_description")
    descriptor = None
    for klass in Hotels.__mro__:
        if "hotel_description" in klass.__dict__:
            descriptor = klass.__dict__["hotel_description"]
            break
    assert isinstance(descriptor, property)



def test_owner_is_not_abstract():
    assert not inspect.isabstract(Owner)


def test_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phn_no_" in params, "Missing parameter 'Phn_no_'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "password" in params, "Missing parameter 'password'"

def test_owner_has_Address():
    assert hasattr(Owner, "Address")
    descriptor = None
    for klass in Owner.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_Phn_no_():
    assert hasattr(Owner, "Phn_no_")
    descriptor = None
    for klass in Owner.__mro__:
        if "Phn_no_" in klass.__dict__:
            descriptor = klass.__dict__["Phn_no_"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_Name():
    assert hasattr(Owner, "Name")
    descriptor = None
    for klass in Owner.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_email_id():
    assert hasattr(Owner, "email_id")
    descriptor = None
    for klass in Owner.__mro__:
        if "email_id" in klass.__dict__:
            descriptor = klass.__dict__["email_id"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_ID():
    assert hasattr(Owner, "ID")
    descriptor = None
    for klass in Owner.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_password():
    assert hasattr(Owner, "password")
    descriptor = None
    for klass in Owner.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
occupancy_strategy = st.builds(
    occupancy,
    booking_id=
        st.integers()
)
Booking_strategy = st.builds(
    Booking,
    booking_id=
        st.integers(),
    user_id=
        st.integers(),
    guest_adress=
        safe_text,
    guest_id=
        st.integers(),
    guest_name=
        st.integers(),
    guestphn_no=
        st.integers()
)
User_strategy = st.builds(
    User,
    Name=
        safe_text,
    id=
        st.integers(),
    password=
        st.integers(),
    address=
        safe_text,
    mail_id=
        safe_text,
    phn_no=
        st.integers()
)
Location_strategy = st.builds(
    Location,
    attribute=
        safe_text,
    loc_name=
        safe_text,
    loc_id=
        st.integers()
)
Rooms_strategy = st.builds(
    Rooms,
    name=
        safe_text,
    room_description=
        safe_text,
    checkout_date=
        st.integers(),
    id=
        st.integers(),
    price=
        st.integers(),
    checkin_date=
        st.integers()
)
Hotels_strategy = st.builds(
    Hotels,
    id=
        st.integers(),
    name=
        st.integers(),
    hotel_description=
        st.integers()
)
Owner_strategy = st.builds(
    Owner,
    Address=
        safe_text,
    Phn_no_=
        st.none(),
    Name=
        safe_text,
    email_id=
        st.integers(),
    ID=
        st.integers(),
    password=
        st.integers()
)

@given(instance=occupancy_strategy)
@settings(max_examples=50)
def test_occupancy_instantiation(instance):
    assert isinstance(instance, occupancy)



@given(instance=occupancy_strategy)
def test_occupancy_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_booking_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Booking_strategy)
def test_booking_guest_adress_setter(instance):
    original = instance.guest_adress
    instance.guest_adress = original
    assert instance.guest_adress == original



@given(instance=Booking_strategy)
def test_booking_guest_id_setter(instance):
    original = instance.guest_id
    instance.guest_id = original
    assert instance.guest_id == original



@given(instance=Booking_strategy)
def test_booking_guest_name_setter(instance):
    original = instance.guest_name
    instance.guest_name = original
    assert instance.guest_name == original



@given(instance=Booking_strategy)
def test_booking_guestphn_no_setter(instance):
    original = instance.guestphn_no
    instance.guestphn_no = original
    assert instance.guestphn_no == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=User_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=User_strategy)
def test_user_mail_id_setter(instance):
    original = instance.mail_id
    instance.mail_id = original
    assert instance.mail_id == original



@given(instance=User_strategy)
def test_user_phn_no_setter(instance):
    original = instance.phn_no
    instance.phn_no = original
    assert instance.phn_no == original

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)



@given(instance=Location_strategy)
def test_location_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Location_strategy)
def test_location_loc_name_setter(instance):
    original = instance.loc_name
    instance.loc_name = original
    assert instance.loc_name == original



@given(instance=Location_strategy)
def test_location_loc_id_setter(instance):
    original = instance.loc_id
    instance.loc_id = original
    assert instance.loc_id == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Rooms_strategy)
def test_rooms_room_description_setter(instance):
    original = instance.room_description
    instance.room_description = original
    assert instance.room_description == original



@given(instance=Rooms_strategy)
def test_rooms_checkout_date_setter(instance):
    original = instance.checkout_date
    instance.checkout_date = original
    assert instance.checkout_date == original



@given(instance=Rooms_strategy)
def test_rooms_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Rooms_strategy)
def test_rooms_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Rooms_strategy)
def test_rooms_checkin_date_setter(instance):
    original = instance.checkin_date
    instance.checkin_date = original
    assert instance.checkin_date == original

@given(instance=Hotels_strategy)
@settings(max_examples=50)
def test_hotels_instantiation(instance):
    assert isinstance(instance, Hotels)



@given(instance=Hotels_strategy)
def test_hotels_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Hotels_strategy)
def test_hotels_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hotels_strategy)
def test_hotels_hotel_description_setter(instance):
    original = instance.hotel_description
    instance.hotel_description = original
    assert instance.hotel_description == original

@given(instance=Owner_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, Owner)



@given(instance=Owner_strategy)
def test_owner_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Owner_strategy)
def test_owner_Phn_no__setter(instance):
    original = instance.Phn_no_
    instance.Phn_no_ = original
    assert instance.Phn_no_ == original



@given(instance=Owner_strategy)
def test_owner_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Owner_strategy)
def test_owner_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



@given(instance=Owner_strategy)
def test_owner_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Owner_strategy)
def test_owner_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
