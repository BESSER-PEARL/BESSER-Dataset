import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    User,
    Payment,
    City,
    Guest,
    Rooms,
    Hotels,
    Manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "mail_id" in params, "Missing parameter 'mail_id'"
    assert "phn_no" in params, "Missing parameter 'phn_no'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

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

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "cvv" in params, "Missing parameter 'cvv'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "password" in params, "Missing parameter 'password'"
    assert "card_no" in params, "Missing parameter 'card_no'"
    assert "card_type" in params, "Missing parameter 'card_type'"

def test_payment_has_cvv():
    assert hasattr(Payment, "cvv")
    descriptor = None
    for klass in Payment.__mro__:
        if "cvv" in klass.__dict__:
            descriptor = klass.__dict__["cvv"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_amount():
    assert hasattr(Payment, "amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_password():
    assert hasattr(Payment, "password")
    descriptor = None
    for klass in Payment.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_card_no():
    assert hasattr(Payment, "card_no")
    descriptor = None
    for klass in Payment.__mro__:
        if "card_no" in klass.__dict__:
            descriptor = klass.__dict__["card_no"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_card_type():
    assert hasattr(Payment, "card_type")
    descriptor = None
    for klass in Payment.__mro__:
        if "card_type" in klass.__dict__:
            descriptor = klass.__dict__["card_type"]
            break
    assert isinstance(descriptor, property)



def test_city_is_not_abstract():
    assert not inspect.isabstract(City)


def test_city_constructor_exists():
    assert callable(City.__init__)


def test_city_constructor_args():
    sig = inspect.signature(City.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "id" in params, "Missing parameter 'id'"

def test_city_has_city():
    assert hasattr(City, "city")
    descriptor = None
    for klass in City.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_city_has_id():
    assert hasattr(City, "id")
    descriptor = None
    for klass in City.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Nmae" in params, "Missing parameter 'Nmae'"
    assert "Phone_no_" in params, "Missing parameter 'Phone_no_'"
    assert "address" in params, "Missing parameter 'address'"

def test_guest_has_id():
    assert hasattr(Guest, "id")
    descriptor = None
    for klass in Guest.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_Nmae():
    assert hasattr(Guest, "Nmae")
    descriptor = None
    for klass in Guest.__mro__:
        if "Nmae" in klass.__dict__:
            descriptor = klass.__dict__["Nmae"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_Phone_no_():
    assert hasattr(Guest, "Phone_no_")
    descriptor = None
    for klass in Guest.__mro__:
        if "Phone_no_" in klass.__dict__:
            descriptor = klass.__dict__["Phone_no_"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_address():
    assert hasattr(Guest, "address")
    descriptor = None
    for klass in Guest.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "room_description" in params, "Missing parameter 'room_description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"

def test_rooms_has_room_description():
    assert hasattr(Rooms, "room_description")
    descriptor = None
    for klass in Rooms.__mro__:
        if "room_description" in klass.__dict__:
            descriptor = klass.__dict__["room_description"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_name():
    assert hasattr(Rooms, "name")
    descriptor = None
    for klass in Rooms.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_rooms_has_id():
    assert hasattr(Rooms, "id")
    descriptor = None
    for klass in Rooms.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"

def test_hotels_has_id():
    assert hasattr(Hotels, "id")
    descriptor = None
    for klass in Hotels.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hotels_has_location():
    assert hasattr(Hotels, "location")
    descriptor = None
    for klass in Hotels.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phn_no_" in params, "Missing parameter 'Phn_no_'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_manager_has_Address():
    assert hasattr(Manager, "Address")
    descriptor = None
    for klass in Manager.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Phn_no_():
    assert hasattr(Manager, "Phn_no_")
    descriptor = None
    for klass in Manager.__mro__:
        if "Phn_no_" in klass.__dict__:
            descriptor = klass.__dict__["Phn_no_"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_ID():
    assert hasattr(Manager, "ID")
    descriptor = None
    for klass in Manager.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Name():
    assert hasattr(Manager, "Name")
    descriptor = None
    for klass in Manager.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
User_strategy = st.builds(
    User,
    address=
        safe_text,
    mail_id=
        safe_text,
    phn_no=
        st.integers(),
    Name=
        safe_text,
    password=
        st.integers(),
    id=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    cvv=
        st.integers(),
    amount=
        st.integers(),
    password=
        st.integers(),
    card_no=
        st.integers(),
    card_type=
        safe_text
)
City_strategy = st.builds(
    City,
    city=
        safe_text,
    id=
        st.integers()
)
Guest_strategy = st.builds(
    Guest,
    id=
        st.integers(),
    Nmae=
        safe_text,
    Phone_no_=
        st.integers(),
    address=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    room_description=
        safe_text,
    name=
        safe_text,
    price=
        st.integers(),
    id=
        st.integers()
)
Hotels_strategy = st.builds(
    Hotels,
    id=
        st.integers(),
    location=
        st.integers(),
    name=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    Address=
        safe_text,
    Phn_no_=
        st.none(),
    ID=
        st.integers(),
    Name=
        safe_text
)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



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



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



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

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_cvv_setter(instance):
    original = instance.cvv
    instance.cvv = original
    assert instance.cvv == original



@given(instance=Payment_strategy)
def test_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Payment_strategy)
def test_payment_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Payment_strategy)
def test_payment_card_no_setter(instance):
    original = instance.card_no
    instance.card_no = original
    assert instance.card_no == original



@given(instance=Payment_strategy)
def test_payment_card_type_setter(instance):
    original = instance.card_type
    instance.card_type = original
    assert instance.card_type == original

@given(instance=City_strategy)
@settings(max_examples=50)
def test_city_instantiation(instance):
    assert isinstance(instance, City)



@given(instance=City_strategy)
def test_city_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=City_strategy)
def test_city_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)



@given(instance=Guest_strategy)
def test_guest_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Guest_strategy)
def test_guest_Nmae_setter(instance):
    original = instance.Nmae
    instance.Nmae = original
    assert instance.Nmae == original



@given(instance=Guest_strategy)
def test_guest_Phone_no__setter(instance):
    original = instance.Phone_no_
    instance.Phone_no_ = original
    assert instance.Phone_no_ == original



@given(instance=Guest_strategy)
def test_guest_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_room_description_setter(instance):
    original = instance.room_description
    instance.room_description = original
    assert instance.room_description == original



@given(instance=Rooms_strategy)
def test_rooms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Rooms_strategy)
def test_rooms_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Rooms_strategy)
def test_rooms_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

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
def test_hotels_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Hotels_strategy)
def test_hotels_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Manager_strategy)
def test_manager_Phn_no__setter(instance):
    original = instance.Phn_no_
    instance.Phn_no_ = original
    assert instance.Phn_no_ == original



@given(instance=Manager_strategy)
def test_manager_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Manager_strategy)
def test_manager_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
