import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Food,
    Housekeeping,
    Bill,
    Rooms,
    Chef,
    Guest,
    Inventory,
    Receptionist,
    Manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "foodID" in params, "Missing parameter 'foodID'"

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_food_has_foodID():
    assert hasattr(Food, "foodID")
    descriptor = None
    for klass in Food.__mro__:
        if "foodID" in klass.__dict__:
            descriptor = klass.__dict__["foodID"]
            break
    assert isinstance(descriptor, property)



def test_housekeeping_is_not_abstract():
    assert not inspect.isabstract(Housekeeping)


def test_housekeeping_constructor_exists():
    assert callable(Housekeeping.__init__)


def test_housekeeping_constructor_args():
    sig = inspect.signature(Housekeeping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "hkID" in params, "Missing parameter 'hkID'"

def test_housekeeping_has_name():
    assert hasattr(Housekeeping, "name")
    descriptor = None
    for klass in Housekeeping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_housekeeping_has_branch():
    assert hasattr(Housekeeping, "branch")
    descriptor = None
    for klass in Housekeeping.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_housekeeping_has_hkID():
    assert hasattr(Housekeeping, "hkID")
    descriptor = None
    for klass in Housekeeping.__mro__:
        if "hkID" in klass.__dict__:
            descriptor = klass.__dict__["hkID"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billNo" in params, "Missing parameter 'billNo'"
    assert "guestID" in params, "Missing parameter 'guestID'"

def test_bill_has_billNo():
    assert hasattr(Bill, "billNo")
    descriptor = None
    for klass in Bill.__mro__:
        if "billNo" in klass.__dict__:
            descriptor = klass.__dict__["billNo"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_guestID():
    assert hasattr(Bill, "guestID")
    descriptor = None
    for klass in Bill.__mro__:
        if "guestID" in klass.__dict__:
            descriptor = klass.__dict__["guestID"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "roomNo" in params, "Missing parameter 'roomNo'"

def test_rooms_has_type():
    assert hasattr(Rooms, "type")
    descriptor = None
    for klass in Rooms.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_roomNo():
    assert hasattr(Rooms, "roomNo")
    descriptor = None
    for klass in Rooms.__mro__:
        if "roomNo" in klass.__dict__:
            descriptor = klass.__dict__["roomNo"]
            break
    assert isinstance(descriptor, property)



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())
    assert "branch" in params, "Missing parameter 'branch'"
    assert "name" in params, "Missing parameter 'name'"
    assert "chefID" in params, "Missing parameter 'chefID'"

def test_chef_has_branch():
    assert hasattr(Chef, "branch")
    descriptor = None
    for klass in Chef.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_name():
    assert hasattr(Chef, "name")
    descriptor = None
    for klass in Chef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_chefID():
    assert hasattr(Chef, "chefID")
    descriptor = None
    for klass in Chef.__mro__:
        if "chefID" in klass.__dict__:
            descriptor = klass.__dict__["chefID"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "roomNo" in params, "Missing parameter 'roomNo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "guestID" in params, "Missing parameter 'guestID'"
    assert "address" in params, "Missing parameter 'address'"

def test_guest_has_phoneNo():
    assert hasattr(Guest, "phoneNo")
    descriptor = None
    for klass in Guest.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_roomNo():
    assert hasattr(Guest, "roomNo")
    descriptor = None
    for klass in Guest.__mro__:
        if "roomNo" in klass.__dict__:
            descriptor = klass.__dict__["roomNo"]
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

def test_guest_has_guestID():
    assert hasattr(Guest, "guestID")
    descriptor = None
    for klass in Guest.__mro__:
        if "guestID" in klass.__dict__:
            descriptor = klass.__dict__["guestID"]
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



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "type" in params, "Missing parameter 'type'"

def test_inventory_has_status():
    assert hasattr(Inventory, "status")
    descriptor = None
    for klass in Inventory.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_type():
    assert hasattr(Inventory, "type")
    descriptor = None
    for klass in Inventory.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rID" in params, "Missing parameter 'rID'"

def test_receptionist_has_phoneNo():
    assert hasattr(Receptionist, "phoneNo")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_branch():
    assert hasattr(Receptionist, "branch")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_name():
    assert hasattr(Receptionist, "name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_rID():
    assert hasattr(Receptionist, "rID")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "rID" in klass.__dict__:
            descriptor = klass.__dict__["rID"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "managerID" in params, "Missing parameter 'managerID'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "name" in params, "Missing parameter 'name'"

def test_manager_has_managerID():
    assert hasattr(Manager, "managerID")
    descriptor = None
    for klass in Manager.__mro__:
        if "managerID" in klass.__dict__:
            descriptor = klass.__dict__["managerID"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_branch():
    assert hasattr(Manager, "branch")
    descriptor = None
    for klass in Manager.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_phoneNo():
    assert hasattr(Manager, "phoneNo")
    descriptor = None
    for klass in Manager.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
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
Food_strategy = st.builds(
    Food,
    name=
        safe_text,
    foodID=
        st.integers()
)
Housekeeping_strategy = st.builds(
    Housekeeping,
    name=
        safe_text,
    branch=
        safe_text,
    hkID=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    billNo=
        st.integers(),
    guestID=
        st.integers()
)
Rooms_strategy = st.builds(
    Rooms,
    type=
        safe_text,
    roomNo=
        st.integers()
)
Chef_strategy = st.builds(
    Chef,
    branch=
        safe_text,
    name=
        safe_text,
    chefID=
        st.integers()
)
Guest_strategy = st.builds(
    Guest,
    phoneNo=
        st.integers(),
    roomNo=
        st.integers(),
    name=
        safe_text,
    guestID=
        st.integers(),
    address=
        safe_text
)
Inventory_strategy = st.builds(
    Inventory,
    status=
        safe_text,
    type=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    phoneNo=
        st.integers(),
    branch=
        safe_text,
    name=
        safe_text,
    rID=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    managerID=
        st.integers(),
    branch=
        safe_text,
    phoneNo=
        st.integers(),
    name=
        safe_text
)

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)



@given(instance=Food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Food_strategy)
def test_food_foodID_setter(instance):
    original = instance.foodID
    instance.foodID = original
    assert instance.foodID == original

@given(instance=Housekeeping_strategy)
@settings(max_examples=50)
def test_housekeeping_instantiation(instance):
    assert isinstance(instance, Housekeeping)



@given(instance=Housekeeping_strategy)
def test_housekeeping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Housekeeping_strategy)
def test_housekeeping_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Housekeeping_strategy)
def test_housekeeping_hkID_setter(instance):
    original = instance.hkID
    instance.hkID = original
    assert instance.hkID == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_billNo_setter(instance):
    original = instance.billNo
    instance.billNo = original
    assert instance.billNo == original



@given(instance=Bill_strategy)
def test_bill_guestID_setter(instance):
    original = instance.guestID
    instance.guestID = original
    assert instance.guestID == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Rooms_strategy)
def test_rooms_roomNo_setter(instance):
    original = instance.roomNo
    instance.roomNo = original
    assert instance.roomNo == original

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)



@given(instance=Chef_strategy)
def test_chef_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Chef_strategy)
def test_chef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Chef_strategy)
def test_chef_chefID_setter(instance):
    original = instance.chefID
    instance.chefID = original
    assert instance.chefID == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)



@given(instance=Guest_strategy)
def test_guest_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Guest_strategy)
def test_guest_roomNo_setter(instance):
    original = instance.roomNo
    instance.roomNo = original
    assert instance.roomNo == original



@given(instance=Guest_strategy)
def test_guest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Guest_strategy)
def test_guest_guestID_setter(instance):
    original = instance.guestID
    instance.guestID = original
    assert instance.guestID == original



@given(instance=Guest_strategy)
def test_guest_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)



@given(instance=Inventory_strategy)
def test_inventory_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Inventory_strategy)
def test_inventory_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Receptionist_strategy)
def test_receptionist_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Receptionist_strategy)
def test_receptionist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Receptionist_strategy)
def test_receptionist_rID_setter(instance):
    original = instance.rID
    instance.rID = original
    assert instance.rID == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_managerID_setter(instance):
    original = instance.managerID
    instance.managerID = original
    assert instance.managerID == original



@given(instance=Manager_strategy)
def test_manager_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Manager_strategy)
def test_manager_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Manager_strategy)
def test_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
