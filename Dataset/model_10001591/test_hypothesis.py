import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Database,
    Inventory,
    Bill,
    Room,
    Manager,
    Receptionist,
    Guest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())
    assert "Details" in params, "Missing parameter 'Details'"
    assert "service" in params, "Missing parameter 'service'"
    assert "income" in params, "Missing parameter 'income'"

def test_database_has_Details():
    assert hasattr(Database, "Details")
    descriptor = None
    for klass in Database.__mro__:
        if "Details" in klass.__dict__:
            descriptor = klass.__dict__["Details"]
            break
    assert isinstance(descriptor, property)

def test_database_has_service():
    assert hasattr(Database, "service")
    descriptor = None
    for klass in Database.__mro__:
        if "service" in klass.__dict__:
            descriptor = klass.__dict__["service"]
            break
    assert isinstance(descriptor, property)

def test_database_has_income():
    assert hasattr(Database, "income")
    descriptor = None
    for klass in Database.__mro__:
        if "income" in klass.__dict__:
            descriptor = klass.__dict__["income"]
            break
    assert isinstance(descriptor, property)



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_inventory_has_type():
    assert hasattr(Inventory, "type")
    descriptor = None
    for klass in Inventory.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_Status():
    assert hasattr(Inventory, "Status")
    descriptor = None
    for klass in Inventory.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "GuestName" in params, "Missing parameter 'GuestName'"
    assert "bill_No" in params, "Missing parameter 'bill_No'"

def test_bill_has_GuestName():
    assert hasattr(Bill, "GuestName")
    descriptor = None
    for klass in Bill.__mro__:
        if "GuestName" in klass.__dict__:
            descriptor = klass.__dict__["GuestName"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_bill_No():
    assert hasattr(Bill, "bill_No")
    descriptor = None
    for klass in Bill.__mro__:
        if "bill_No" in klass.__dict__:
            descriptor = klass.__dict__["bill_No"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "RatesofRoom" in params, "Missing parameter 'RatesofRoom'"
    assert "typeOfRoom" in params, "Missing parameter 'typeOfRoom'"
    assert "roomNo" in params, "Missing parameter 'roomNo'"

def test_room_has_RatesofRoom():
    assert hasattr(Room, "RatesofRoom")
    descriptor = None
    for klass in Room.__mro__:
        if "RatesofRoom" in klass.__dict__:
            descriptor = klass.__dict__["RatesofRoom"]
            break
    assert isinstance(descriptor, property)

def test_room_has_typeOfRoom():
    assert hasattr(Room, "typeOfRoom")
    descriptor = None
    for klass in Room.__mro__:
        if "typeOfRoom" in klass.__dict__:
            descriptor = klass.__dict__["typeOfRoom"]
            break
    assert isinstance(descriptor, property)

def test_room_has_roomNo():
    assert hasattr(Room, "roomNo")
    descriptor = None
    for klass in Room.__mro__:
        if "roomNo" in klass.__dict__:
            descriptor = klass.__dict__["roomNo"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_manager_has_id():
    assert hasattr(Manager, "id")
    descriptor = None
    for klass in Manager.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_name():
    assert hasattr(Manager, "name")
    descriptor = None
    for klass in Manager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_receptionist_has_name():
    assert hasattr(Receptionist, "name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Id():
    assert hasattr(Receptionist, "Id")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credit_card" in params, "Missing parameter 'credit_card'"
    assert "Room" in params, "Missing parameter 'Room'"

def test_guest_has_Address():
    assert hasattr(Guest, "Address")
    descriptor = None
    for klass in Guest.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_phoneNo():
    assert hasattr(Guest, "phoneNo")
    descriptor = None
    for klass in Guest.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_id():
    assert hasattr(Guest, "id")
    descriptor = None
    for klass in Guest.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_name():
    assert hasattr(Guest, "name")
    descriptor = None
    for klass in Guest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_credit_card():
    assert hasattr(Guest, "credit_card")
    descriptor = None
    for klass in Guest.__mro__:
        if "credit_card" in klass.__dict__:
            descriptor = klass.__dict__["credit_card"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_Room():
    assert hasattr(Guest, "Room")
    descriptor = None
    for klass in Guest.__mro__:
        if "Room" in klass.__dict__:
            descriptor = klass.__dict__["Room"]
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
Database_strategy = st.builds(
    Database,
    Details=
        safe_text,
    service=
        safe_text,
    income=
        st.integers()
)
Inventory_strategy = st.builds(
    Inventory,
    type=
        safe_text,
    Status=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    GuestName=
        safe_text,
    bill_No=
        st.integers()
)
Room_strategy = st.builds(
    Room,
    RatesofRoom=
        st.integers(),
    typeOfRoom=
        safe_text,
    roomNo=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    id=
        st.integers(),
    name=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    name=
        safe_text,
    Id=
        st.integers()
)
Guest_strategy = st.builds(
    Guest,
    Address=
        safe_text,
    phoneNo=
        st.integers(),
    id=
        st.integers(),
    name=
        safe_text,
    credit_card=
        st.integers(),
    Room=
        st.integers()
)

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)



@given(instance=Database_strategy)
def test_database_Details_setter(instance):
    original = instance.Details
    instance.Details = original
    assert instance.Details == original



@given(instance=Database_strategy)
def test_database_service_setter(instance):
    original = instance.service
    instance.service = original
    assert instance.service == original



@given(instance=Database_strategy)
def test_database_income_setter(instance):
    original = instance.income
    instance.income = original
    assert instance.income == original

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)



@given(instance=Inventory_strategy)
def test_inventory_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Inventory_strategy)
def test_inventory_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_GuestName_setter(instance):
    original = instance.GuestName
    instance.GuestName = original
    assert instance.GuestName == original



@given(instance=Bill_strategy)
def test_bill_bill_No_setter(instance):
    original = instance.bill_No
    instance.bill_No = original
    assert instance.bill_No == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_RatesofRoom_setter(instance):
    original = instance.RatesofRoom
    instance.RatesofRoom = original
    assert instance.RatesofRoom == original



@given(instance=Room_strategy)
def test_room_typeOfRoom_setter(instance):
    original = instance.typeOfRoom
    instance.typeOfRoom = original
    assert instance.typeOfRoom == original



@given(instance=Room_strategy)
def test_room_roomNo_setter(instance):
    original = instance.roomNo
    instance.roomNo = original
    assert instance.roomNo == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Manager_strategy)
def test_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Receptionist_strategy)
def test_receptionist_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)



@given(instance=Guest_strategy)
def test_guest_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Guest_strategy)
def test_guest_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Guest_strategy)
def test_guest_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Guest_strategy)
def test_guest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Guest_strategy)
def test_guest_credit_card_setter(instance):
    original = instance.credit_card
    instance.credit_card = original
    assert instance.credit_card == original



@given(instance=Guest_strategy)
def test_guest_Room_setter(instance):
    original = instance.Room
    instance.Room = original
    assert instance.Room == original
