import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Administrator,
    RegisteredUser,
    RealEstateAgent,
    House,
    Apartment,
    Listing,
    Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())



def test_registereduser_is_not_abstract():
    assert not inspect.isabstract(RegisteredUser)


def test_registereduser_constructor_exists():
    assert callable(RegisteredUser.__init__)


def test_registereduser_constructor_args():
    sig = inspect.signature(RegisteredUser.__init__)
    params = list(sig.parameters.keys())



def test_realestateagent_is_not_abstract():
    assert not inspect.isabstract(RealEstateAgent)


def test_realestateagent_constructor_exists():
    assert callable(RealEstateAgent.__init__)


def test_realestateagent_constructor_args():
    sig = inspect.signature(RealEstateAgent.__init__)
    params = list(sig.parameters.keys())
    assert "listings" in params, "Missing parameter 'listings'"

def test_realestateagent_has_listings():
    assert hasattr(RealEstateAgent, "listings")
    descriptor = None
    for klass in RealEstateAgent.__mro__:
        if "listings" in klass.__dict__:
            descriptor = klass.__dict__["listings"]
            break
    assert isinstance(descriptor, property)



def test_house_is_not_abstract():
    assert not inspect.isabstract(House)


def test_house_constructor_exists():
    assert callable(House.__init__)


def test_house_constructor_args():
    sig = inspect.signature(House.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "fees" in params, "Missing parameter 'fees'"
    assert "sizeOfProperty" in params, "Missing parameter 'sizeOfProperty'"
    assert "numberOfFloors" in params, "Missing parameter 'numberOfFloors'"

def test_house_has_price():
    assert hasattr(House, "price")
    descriptor = None
    for klass in House.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_house_has_fees():
    assert hasattr(House, "fees")
    descriptor = None
    for klass in House.__mro__:
        if "fees" in klass.__dict__:
            descriptor = klass.__dict__["fees"]
            break
    assert isinstance(descriptor, property)

def test_house_has_sizeOfProperty():
    assert hasattr(House, "sizeOfProperty")
    descriptor = None
    for klass in House.__mro__:
        if "sizeOfProperty" in klass.__dict__:
            descriptor = klass.__dict__["sizeOfProperty"]
            break
    assert isinstance(descriptor, property)

def test_house_has_numberOfFloors():
    assert hasattr(House, "numberOfFloors")
    descriptor = None
    for klass in House.__mro__:
        if "numberOfFloors" in klass.__dict__:
            descriptor = klass.__dict__["numberOfFloors"]
            break
    assert isinstance(descriptor, property)



def test_apartment_is_not_abstract():
    assert not inspect.isabstract(Apartment)


def test_apartment_constructor_exists():
    assert callable(Apartment.__init__)


def test_apartment_constructor_args():
    sig = inspect.signature(Apartment.__init__)
    params = list(sig.parameters.keys())
    assert "lease" in params, "Missing parameter 'lease'"
    assert "securityDeposit" in params, "Missing parameter 'securityDeposit'"
    assert "size" in params, "Missing parameter 'size'"
    assert "monthlyRent" in params, "Missing parameter 'monthlyRent'"

def test_apartment_has_lease():
    assert hasattr(Apartment, "lease")
    descriptor = None
    for klass in Apartment.__mro__:
        if "lease" in klass.__dict__:
            descriptor = klass.__dict__["lease"]
            break
    assert isinstance(descriptor, property)

def test_apartment_has_securityDeposit():
    assert hasattr(Apartment, "securityDeposit")
    descriptor = None
    for klass in Apartment.__mro__:
        if "securityDeposit" in klass.__dict__:
            descriptor = klass.__dict__["securityDeposit"]
            break
    assert isinstance(descriptor, property)

def test_apartment_has_size():
    assert hasattr(Apartment, "size")
    descriptor = None
    for klass in Apartment.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_apartment_has_monthlyRent():
    assert hasattr(Apartment, "monthlyRent")
    descriptor = None
    for klass in Apartment.__mro__:
        if "monthlyRent" in klass.__dict__:
            descriptor = klass.__dict__["monthlyRent"]
            break
    assert isinstance(descriptor, property)



def test_listing_is_not_abstract():
    assert not inspect.isabstract(Listing)


def test_listing_constructor_exists():
    assert callable(Listing.__init__)


def test_listing_constructor_args():
    sig = inspect.signature(Listing.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfBathrooms" in params, "Missing parameter 'numberOfBathrooms'"
    assert "numberOfBedroms" in params, "Missing parameter 'numberOfBedroms'"
    assert "furnished" in params, "Missing parameter 'furnished'"
    assert "image" in params, "Missing parameter 'image'"
    assert "video" in params, "Missing parameter 'video'"
    assert "kitchen" in params, "Missing parameter 'kitchen'"
    assert "parkingPossibilities" in params, "Missing parameter 'parkingPossibilities'"
    assert "address" in params, "Missing parameter 'address'"
    assert "livingRooom" in params, "Missing parameter 'livingRooom'"

def test_listing_has_numberOfBathrooms():
    assert hasattr(Listing, "numberOfBathrooms")
    descriptor = None
    for klass in Listing.__mro__:
        if "numberOfBathrooms" in klass.__dict__:
            descriptor = klass.__dict__["numberOfBathrooms"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_numberOfBedroms():
    assert hasattr(Listing, "numberOfBedroms")
    descriptor = None
    for klass in Listing.__mro__:
        if "numberOfBedroms" in klass.__dict__:
            descriptor = klass.__dict__["numberOfBedroms"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_furnished():
    assert hasattr(Listing, "furnished")
    descriptor = None
    for klass in Listing.__mro__:
        if "furnished" in klass.__dict__:
            descriptor = klass.__dict__["furnished"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_image():
    assert hasattr(Listing, "image")
    descriptor = None
    for klass in Listing.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_video():
    assert hasattr(Listing, "video")
    descriptor = None
    for klass in Listing.__mro__:
        if "video" in klass.__dict__:
            descriptor = klass.__dict__["video"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_kitchen():
    assert hasattr(Listing, "kitchen")
    descriptor = None
    for klass in Listing.__mro__:
        if "kitchen" in klass.__dict__:
            descriptor = klass.__dict__["kitchen"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_parkingPossibilities():
    assert hasattr(Listing, "parkingPossibilities")
    descriptor = None
    for klass in Listing.__mro__:
        if "parkingPossibilities" in klass.__dict__:
            descriptor = klass.__dict__["parkingPossibilities"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_address():
    assert hasattr(Listing, "address")
    descriptor = None
    for klass in Listing.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_listing_has_livingRooom():
    assert hasattr(Listing, "livingRooom")
    descriptor = None
    for klass in Listing.__mro__:
        if "livingRooom" in klass.__dict__:
            descriptor = klass.__dict__["livingRooom"]
            break
    assert isinstance(descriptor, property)



def test_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_actor_has_name():
    assert hasattr(Actor, "name")
    descriptor = None
    for klass in Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_actor_has_password():
    assert hasattr(Actor, "password")
    descriptor = None
    for klass in Actor.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_actor_has_username():
    assert hasattr(Actor, "username")
    descriptor = None
    for klass in Actor.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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
Administrator_strategy = st.builds(
    Administrator,
)
RegisteredUser_strategy = st.builds(
    RegisteredUser,
)
RealEstateAgent_strategy = st.builds(
    RealEstateAgent,
    listings=
        safe_text
)
House_strategy = st.builds(
    House,
    price=
        st.integers(),
    fees=
        st.integers(),
    sizeOfProperty=
        st.integers(),
    numberOfFloors=
        st.integers()
)
Apartment_strategy = st.builds(
    Apartment,
    lease=
        st.integers(),
    securityDeposit=
        st.integers(),
    size=
        st.integers(),
    monthlyRent=
        st.integers()
)
Listing_strategy = st.builds(
    Listing,
    numberOfBathrooms=
        st.integers(),
    numberOfBedroms=
        st.integers(),
    furnished=
        st.booleans(),
    image=
        safe_text,
    video=
        safe_text,
    kitchen=
        st.integers(),
    parkingPossibilities=
        st.integers(),
    address=
        safe_text,
    livingRooom=
        st.integers()
)
Actor_strategy = st.builds(
    Actor,
    name=
        safe_text,
    password=
        safe_text,
    username=
        safe_text
)

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)

@given(instance=RegisteredUser_strategy)
@settings(max_examples=50)
def test_registereduser_instantiation(instance):
    assert isinstance(instance, RegisteredUser)

@given(instance=RealEstateAgent_strategy)
@settings(max_examples=50)
def test_realestateagent_instantiation(instance):
    assert isinstance(instance, RealEstateAgent)



@given(instance=RealEstateAgent_strategy)
def test_realestateagent_listings_setter(instance):
    original = instance.listings
    instance.listings = original
    assert instance.listings == original

@given(instance=House_strategy)
@settings(max_examples=50)
def test_house_instantiation(instance):
    assert isinstance(instance, House)



@given(instance=House_strategy)
def test_house_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=House_strategy)
def test_house_fees_setter(instance):
    original = instance.fees
    instance.fees = original
    assert instance.fees == original



@given(instance=House_strategy)
def test_house_sizeOfProperty_setter(instance):
    original = instance.sizeOfProperty
    instance.sizeOfProperty = original
    assert instance.sizeOfProperty == original



@given(instance=House_strategy)
def test_house_numberOfFloors_setter(instance):
    original = instance.numberOfFloors
    instance.numberOfFloors = original
    assert instance.numberOfFloors == original

@given(instance=Apartment_strategy)
@settings(max_examples=50)
def test_apartment_instantiation(instance):
    assert isinstance(instance, Apartment)



@given(instance=Apartment_strategy)
def test_apartment_lease_setter(instance):
    original = instance.lease
    instance.lease = original
    assert instance.lease == original



@given(instance=Apartment_strategy)
def test_apartment_securityDeposit_setter(instance):
    original = instance.securityDeposit
    instance.securityDeposit = original
    assert instance.securityDeposit == original



@given(instance=Apartment_strategy)
def test_apartment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Apartment_strategy)
def test_apartment_monthlyRent_setter(instance):
    original = instance.monthlyRent
    instance.monthlyRent = original
    assert instance.monthlyRent == original

@given(instance=Listing_strategy)
@settings(max_examples=50)
def test_listing_instantiation(instance):
    assert isinstance(instance, Listing)



@given(instance=Listing_strategy)
def test_listing_numberOfBathrooms_setter(instance):
    original = instance.numberOfBathrooms
    instance.numberOfBathrooms = original
    assert instance.numberOfBathrooms == original



@given(instance=Listing_strategy)
def test_listing_numberOfBedroms_setter(instance):
    original = instance.numberOfBedroms
    instance.numberOfBedroms = original
    assert instance.numberOfBedroms == original



@given(instance=Listing_strategy)
def test_listing_furnished_setter(instance):
    original = instance.furnished
    instance.furnished = original
    assert instance.furnished == original



@given(instance=Listing_strategy)
def test_listing_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Listing_strategy)
def test_listing_video_setter(instance):
    original = instance.video
    instance.video = original
    assert instance.video == original



@given(instance=Listing_strategy)
def test_listing_kitchen_setter(instance):
    original = instance.kitchen
    instance.kitchen = original
    assert instance.kitchen == original



@given(instance=Listing_strategy)
def test_listing_parkingPossibilities_setter(instance):
    original = instance.parkingPossibilities
    instance.parkingPossibilities = original
    assert instance.parkingPossibilities == original



@given(instance=Listing_strategy)
def test_listing_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Listing_strategy)
def test_listing_livingRooom_setter(instance):
    original = instance.livingRooom
    instance.livingRooom = original
    assert instance.livingRooom == original

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)



@given(instance=Actor_strategy)
def test_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Actor_strategy)
def test_actor_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Actor_strategy)
def test_actor_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original
