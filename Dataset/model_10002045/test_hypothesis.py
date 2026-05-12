import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HotelBusiness,
    Contact,
    Guest_Check_out_UseCase,
    Guest_Check_in_UseCase,
    Cancel_Booking_UseCase,
    Make_Booking_UseCase,
    Manage_Rooms_UseCase,
    Manage_Room_Types_UseCase,
    Manage_Hotels_UseCase,
    Administrator_Actor,
    Manager_Actor,
    Receptionist_Actor,
    Guest_Actor,
    Hotel,
    Booking,
    RoomType,
    Room,
    Guest,
    BookingStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hotelbusiness_is_not_abstract():
    assert not inspect.isabstract(HotelBusiness)


def test_hotelbusiness_constructor_exists():
    assert callable(HotelBusiness.__init__)


def test_hotelbusiness_constructor_args():
    sig = inspect.signature(HotelBusiness.__init__)
    params = list(sig.parameters.keys())



def test_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_contact_has_address():
    assert hasattr(Contact, "address")
    descriptor = None
    for klass in Contact.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_contact_has_phone():
    assert hasattr(Contact, "phone")
    descriptor = None
    for klass in Contact.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_contact_has_email():
    assert hasattr(Contact, "email")
    descriptor = None
    for klass in Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_contact_has_name():
    assert hasattr(Contact, "name")
    descriptor = None
    for klass in Contact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_guest_check_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Guest_Check_out_UseCase)


def test_guest_check_out_usecase_constructor_exists():
    assert callable(Guest_Check_out_UseCase.__init__)


def test_guest_check_out_usecase_constructor_args():
    sig = inspect.signature(Guest_Check_out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_guest_check_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Guest_Check_in_UseCase)


def test_guest_check_in_usecase_constructor_exists():
    assert callable(Guest_Check_in_UseCase.__init__)


def test_guest_check_in_usecase_constructor_args():
    sig = inspect.signature(Guest_Check_in_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cancel_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_Booking_UseCase)


def test_cancel_booking_usecase_constructor_exists():
    assert callable(Cancel_Booking_UseCase.__init__)


def test_cancel_booking_usecase_constructor_args():
    sig = inspect.signature(Cancel_Booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_make_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(Make_Booking_UseCase)


def test_make_booking_usecase_constructor_exists():
    assert callable(Make_Booking_UseCase.__init__)


def test_make_booking_usecase_constructor_args():
    sig = inspect.signature(Make_Booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_manage_rooms_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_Rooms_UseCase)


def test_manage_rooms_usecase_constructor_exists():
    assert callable(Manage_Rooms_UseCase.__init__)


def test_manage_rooms_usecase_constructor_args():
    sig = inspect.signature(Manage_Rooms_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_manage_room_types_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_Room_Types_UseCase)


def test_manage_room_types_usecase_constructor_exists():
    assert callable(Manage_Room_Types_UseCase.__init__)


def test_manage_room_types_usecase_constructor_args():
    sig = inspect.signature(Manage_Room_Types_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_manage_hotels_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_Hotels_UseCase)


def test_manage_hotels_usecase_constructor_exists():
    assert callable(Manage_Hotels_UseCase.__init__)


def test_manage_hotels_usecase_constructor_args():
    sig = inspect.signature(Manage_Hotels_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_receptionist_actor_is_not_abstract():
    assert not inspect.isabstract(Receptionist_Actor)


def test_receptionist_actor_constructor_exists():
    assert callable(Receptionist_Actor.__init__)


def test_receptionist_actor_constructor_args():
    sig = inspect.signature(Receptionist_Actor.__init__)
    params = list(sig.parameters.keys())



def test_guest_actor_is_not_abstract():
    assert not inspect.isabstract(Guest_Actor)


def test_guest_actor_constructor_exists():
    assert callable(Guest_Actor.__init__)


def test_guest_actor_constructor_args():
    sig = inspect.signature(Guest_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hotel_has_name():
    assert hasattr(Hotel, "name")
    descriptor = None
    for klass in Hotel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "bookingDate" in params, "Missing parameter 'bookingDate'"
    assert "checkInDate" in params, "Missing parameter 'checkInDate'"
    assert "checkOutDate" in params, "Missing parameter 'checkOutDate'"
    assert "_numberOfNights" in params, "Missing parameter '_numberOfNights'"

def test_booking_has_bookingDate():
    assert hasattr(Booking, "bookingDate")
    descriptor = None
    for klass in Booking.__mro__:
        if "bookingDate" in klass.__dict__:
            descriptor = klass.__dict__["bookingDate"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_checkInDate():
    assert hasattr(Booking, "checkInDate")
    descriptor = None
    for klass in Booking.__mro__:
        if "checkInDate" in klass.__dict__:
            descriptor = klass.__dict__["checkInDate"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_checkOutDate():
    assert hasattr(Booking, "checkOutDate")
    descriptor = None
    for klass in Booking.__mro__:
        if "checkOutDate" in klass.__dict__:
            descriptor = klass.__dict__["checkOutDate"]
            break
    assert isinstance(descriptor, property)

def test_booking_has__numberOfNights():
    assert hasattr(Booking, "_numberOfNights")
    descriptor = None
    for klass in Booking.__mro__:
        if "_numberOfNights" in klass.__dict__:
            descriptor = klass.__dict__["_numberOfNights"]
            break
    assert isinstance(descriptor, property)



def test_roomtype_is_not_abstract():
    assert not inspect.isabstract(RoomType)


def test_roomtype_constructor_exists():
    assert callable(RoomType.__init__)


def test_roomtype_constructor_args():
    sig = inspect.signature(RoomType.__init__)
    params = list(sig.parameters.keys())
    assert "pricePerNight" in params, "Missing parameter 'pricePerNight'"
    assert "name" in params, "Missing parameter 'name'"

def test_roomtype_has_pricePerNight():
    assert hasattr(RoomType, "pricePerNight")
    descriptor = None
    for klass in RoomType.__mro__:
        if "pricePerNight" in klass.__dict__:
            descriptor = klass.__dict__["pricePerNight"]
            break
    assert isinstance(descriptor, property)

def test_roomtype_has_name():
    assert hasattr(RoomType, "name")
    descriptor = None
    for klass in RoomType.__mro__:
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
    assert "name" in params, "Missing parameter 'name'"

def test_room_has_name():
    assert hasattr(Room, "name")
    descriptor = None
    for klass in Room.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())

def test_bookingstatus_exists():
    # Check that the Enumeration exists
    assert BookingStatus is not None

def test_bookingstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookingStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookingStatus"


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
HotelBusiness_strategy = st.builds(
    HotelBusiness,
)
Contact_strategy = st.builds(
    Contact,
    address=
        safe_text,
    phone=
        safe_text,
    email=
        safe_text,
    name=
        safe_text
)
Guest_Check_out_UseCase_strategy = st.builds(
    Guest_Check_out_UseCase,
)
Guest_Check_in_UseCase_strategy = st.builds(
    Guest_Check_in_UseCase,
)
Cancel_Booking_UseCase_strategy = st.builds(
    Cancel_Booking_UseCase,
)
Make_Booking_UseCase_strategy = st.builds(
    Make_Booking_UseCase,
)
Manage_Rooms_UseCase_strategy = st.builds(
    Manage_Rooms_UseCase,
)
Manage_Room_Types_UseCase_strategy = st.builds(
    Manage_Room_Types_UseCase,
)
Manage_Hotels_UseCase_strategy = st.builds(
    Manage_Hotels_UseCase,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
Receptionist_Actor_strategy = st.builds(
    Receptionist_Actor,
)
Guest_Actor_strategy = st.builds(
    Guest_Actor,
)
Hotel_strategy = st.builds(
    Hotel,
    name=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    bookingDate=
        safe_text,
    checkInDate=
        safe_text,
    checkOutDate=
        safe_text,
    _numberOfNights=
        st.integers()
)
RoomType_strategy = st.builds(
    RoomType,
    pricePerNight=
        safe_text,
    name=
        safe_text
)
Room_strategy = st.builds(
    Room,
    name=
        safe_text
)
Guest_strategy = st.builds(
    Guest,
)

@given(instance=HotelBusiness_strategy)
@settings(max_examples=50)
def test_hotelbusiness_instantiation(instance):
    assert isinstance(instance, HotelBusiness)

@given(instance=Contact_strategy)
@settings(max_examples=50)
def test_contact_instantiation(instance):
    assert isinstance(instance, Contact)



@given(instance=Contact_strategy)
def test_contact_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Contact_strategy)
def test_contact_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Contact_strategy)
def test_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Contact_strategy)
def test_contact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Guest_Check_out_UseCase_strategy)
@settings(max_examples=50)
def test_guest_check_out_usecase_instantiation(instance):
    assert isinstance(instance, Guest_Check_out_UseCase)

@given(instance=Guest_Check_in_UseCase_strategy)
@settings(max_examples=50)
def test_guest_check_in_usecase_instantiation(instance):
    assert isinstance(instance, Guest_Check_in_UseCase)

@given(instance=Cancel_Booking_UseCase_strategy)
@settings(max_examples=50)
def test_cancel_booking_usecase_instantiation(instance):
    assert isinstance(instance, Cancel_Booking_UseCase)

@given(instance=Make_Booking_UseCase_strategy)
@settings(max_examples=50)
def test_make_booking_usecase_instantiation(instance):
    assert isinstance(instance, Make_Booking_UseCase)

@given(instance=Manage_Rooms_UseCase_strategy)
@settings(max_examples=50)
def test_manage_rooms_usecase_instantiation(instance):
    assert isinstance(instance, Manage_Rooms_UseCase)

@given(instance=Manage_Room_Types_UseCase_strategy)
@settings(max_examples=50)
def test_manage_room_types_usecase_instantiation(instance):
    assert isinstance(instance, Manage_Room_Types_UseCase)

@given(instance=Manage_Hotels_UseCase_strategy)
@settings(max_examples=50)
def test_manage_hotels_usecase_instantiation(instance):
    assert isinstance(instance, Manage_Hotels_UseCase)

@given(instance=Administrator_Actor_strategy)
@settings(max_examples=50)
def test_administrator_actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)

@given(instance=Manager_Actor_strategy)
@settings(max_examples=50)
def test_manager_actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)

@given(instance=Receptionist_Actor_strategy)
@settings(max_examples=50)
def test_receptionist_actor_instantiation(instance):
    assert isinstance(instance, Receptionist_Actor)

@given(instance=Guest_Actor_strategy)
@settings(max_examples=50)
def test_guest_actor_instantiation(instance):
    assert isinstance(instance, Guest_Actor)

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)



@given(instance=Hotel_strategy)
def test_hotel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_bookingDate_setter(instance):
    original = instance.bookingDate
    instance.bookingDate = original
    assert instance.bookingDate == original



@given(instance=Booking_strategy)
def test_booking_checkInDate_setter(instance):
    original = instance.checkInDate
    instance.checkInDate = original
    assert instance.checkInDate == original



@given(instance=Booking_strategy)
def test_booking_checkOutDate_setter(instance):
    original = instance.checkOutDate
    instance.checkOutDate = original
    assert instance.checkOutDate == original



@given(instance=Booking_strategy)
def test_booking__numberOfNights_setter(instance):
    original = instance._numberOfNights
    instance._numberOfNights = original
    assert instance._numberOfNights == original

@given(instance=RoomType_strategy)
@settings(max_examples=50)
def test_roomtype_instantiation(instance):
    assert isinstance(instance, RoomType)



@given(instance=RoomType_strategy)
def test_roomtype_pricePerNight_setter(instance):
    original = instance.pricePerNight
    instance.pricePerNight = original
    assert instance.pricePerNight == original



@given(instance=RoomType_strategy)
def test_roomtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)
