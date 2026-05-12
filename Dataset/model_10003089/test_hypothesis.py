import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Search_Avalibility_UseCase,
    Customer,
    Inventory,
    Manager,
    HouseKeeping_Actor,
    Chef_Actor,
    Receptionist_Actor,
    Hotel_Guest_Actor,
    Room_Cleaning_UseCase,
    Menu_Preparation_UseCase,
    Food_Serving_UseCase,
    Check_Out_UseCase,
    Check_In_UseCase,
    Cancel_Reservation_UseCase,
    Book_Room_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_search_avalibility_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_Avalibility_UseCase)


def test_search_avalibility_usecase_constructor_exists():
    assert callable(Search_Avalibility_UseCase.__init__)


def test_search_avalibility_usecase_constructor_args():
    sig = inspect.signature(Search_Avalibility_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_inventory_has_Type():
    assert hasattr(Inventory, "Type")
    descriptor = None
    for klass in Inventory.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
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



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Phone_No" in params, "Missing parameter 'Phone_No'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_manager_has_Id():
    assert hasattr(Manager, "Id")
    descriptor = None
    for klass in Manager.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Phone_No():
    assert hasattr(Manager, "Phone_No")
    descriptor = None
    for klass in Manager.__mro__:
        if "Phone_No" in klass.__dict__:
            descriptor = klass.__dict__["Phone_No"]
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



def test_housekeeping_actor_is_not_abstract():
    assert not inspect.isabstract(HouseKeeping_Actor)


def test_housekeeping_actor_constructor_exists():
    assert callable(HouseKeeping_Actor.__init__)


def test_housekeeping_actor_constructor_args():
    sig = inspect.signature(HouseKeeping_Actor.__init__)
    params = list(sig.parameters.keys())



def test_chef_actor_is_not_abstract():
    assert not inspect.isabstract(Chef_Actor)


def test_chef_actor_constructor_exists():
    assert callable(Chef_Actor.__init__)


def test_chef_actor_constructor_args():
    sig = inspect.signature(Chef_Actor.__init__)
    params = list(sig.parameters.keys())



def test_receptionist_actor_is_not_abstract():
    assert not inspect.isabstract(Receptionist_Actor)


def test_receptionist_actor_constructor_exists():
    assert callable(Receptionist_Actor.__init__)


def test_receptionist_actor_constructor_args():
    sig = inspect.signature(Receptionist_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hotel_guest_actor_is_not_abstract():
    assert not inspect.isabstract(Hotel_Guest_Actor)


def test_hotel_guest_actor_constructor_exists():
    assert callable(Hotel_Guest_Actor.__init__)


def test_hotel_guest_actor_constructor_args():
    sig = inspect.signature(Hotel_Guest_Actor.__init__)
    params = list(sig.parameters.keys())



def test_room_cleaning_usecase_is_not_abstract():
    assert not inspect.isabstract(Room_Cleaning_UseCase)


def test_room_cleaning_usecase_constructor_exists():
    assert callable(Room_Cleaning_UseCase.__init__)


def test_room_cleaning_usecase_constructor_args():
    sig = inspect.signature(Room_Cleaning_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_menu_preparation_usecase_is_not_abstract():
    assert not inspect.isabstract(Menu_Preparation_UseCase)


def test_menu_preparation_usecase_constructor_exists():
    assert callable(Menu_Preparation_UseCase.__init__)


def test_menu_preparation_usecase_constructor_args():
    sig = inspect.signature(Menu_Preparation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_food_serving_usecase_is_not_abstract():
    assert not inspect.isabstract(Food_Serving_UseCase)


def test_food_serving_usecase_constructor_exists():
    assert callable(Food_Serving_UseCase.__init__)


def test_food_serving_usecase_constructor_args():
    sig = inspect.signature(Food_Serving_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_Out_UseCase)


def test_check_out_usecase_constructor_exists():
    assert callable(Check_Out_UseCase.__init__)


def test_check_out_usecase_constructor_args():
    sig = inspect.signature(Check_Out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_In_UseCase)


def test_check_in_usecase_constructor_exists():
    assert callable(Check_In_UseCase.__init__)


def test_check_in_usecase_constructor_args():
    sig = inspect.signature(Check_In_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cancel_reservation_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_Reservation_UseCase)


def test_cancel_reservation_usecase_constructor_exists():
    assert callable(Cancel_Reservation_UseCase.__init__)


def test_cancel_reservation_usecase_constructor_args():
    sig = inspect.signature(Cancel_Reservation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_book_room_usecase_is_not_abstract():
    assert not inspect.isabstract(Book_Room_UseCase)


def test_book_room_usecase_constructor_exists():
    assert callable(Book_Room_UseCase.__init__)


def test_book_room_usecase_constructor_args():
    sig = inspect.signature(Book_Room_UseCase.__init__)
    params = list(sig.parameters.keys())


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
Search_Avalibility_UseCase_strategy = st.builds(
    Search_Avalibility_UseCase,
)
Customer_strategy = st.builds(
    Customer,
)
Inventory_strategy = st.builds(
    Inventory,
    Type=
        safe_text,
    Status=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    Id=
        st.integers(),
    Phone_No=
        st.integers(),
    Name=
        safe_text
)
HouseKeeping_Actor_strategy = st.builds(
    HouseKeeping_Actor,
)
Chef_Actor_strategy = st.builds(
    Chef_Actor,
)
Receptionist_Actor_strategy = st.builds(
    Receptionist_Actor,
)
Hotel_Guest_Actor_strategy = st.builds(
    Hotel_Guest_Actor,
)
Room_Cleaning_UseCase_strategy = st.builds(
    Room_Cleaning_UseCase,
)
Menu_Preparation_UseCase_strategy = st.builds(
    Menu_Preparation_UseCase,
)
Food_Serving_UseCase_strategy = st.builds(
    Food_Serving_UseCase,
)
Check_Out_UseCase_strategy = st.builds(
    Check_Out_UseCase,
)
Check_In_UseCase_strategy = st.builds(
    Check_In_UseCase,
)
Cancel_Reservation_UseCase_strategy = st.builds(
    Cancel_Reservation_UseCase,
)
Book_Room_UseCase_strategy = st.builds(
    Book_Room_UseCase,
)

@given(instance=Search_Avalibility_UseCase_strategy)
@settings(max_examples=50)
def test_search_avalibility_usecase_instantiation(instance):
    assert isinstance(instance, Search_Avalibility_UseCase)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)



@given(instance=Inventory_strategy)
def test_inventory_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Inventory_strategy)
def test_inventory_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Manager_strategy)
def test_manager_Phone_No_setter(instance):
    original = instance.Phone_No
    instance.Phone_No = original
    assert instance.Phone_No == original



@given(instance=Manager_strategy)
def test_manager_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=HouseKeeping_Actor_strategy)
@settings(max_examples=50)
def test_housekeeping_actor_instantiation(instance):
    assert isinstance(instance, HouseKeeping_Actor)

@given(instance=Chef_Actor_strategy)
@settings(max_examples=50)
def test_chef_actor_instantiation(instance):
    assert isinstance(instance, Chef_Actor)

@given(instance=Receptionist_Actor_strategy)
@settings(max_examples=50)
def test_receptionist_actor_instantiation(instance):
    assert isinstance(instance, Receptionist_Actor)

@given(instance=Hotel_Guest_Actor_strategy)
@settings(max_examples=50)
def test_hotel_guest_actor_instantiation(instance):
    assert isinstance(instance, Hotel_Guest_Actor)

@given(instance=Room_Cleaning_UseCase_strategy)
@settings(max_examples=50)
def test_room_cleaning_usecase_instantiation(instance):
    assert isinstance(instance, Room_Cleaning_UseCase)

@given(instance=Menu_Preparation_UseCase_strategy)
@settings(max_examples=50)
def test_menu_preparation_usecase_instantiation(instance):
    assert isinstance(instance, Menu_Preparation_UseCase)

@given(instance=Food_Serving_UseCase_strategy)
@settings(max_examples=50)
def test_food_serving_usecase_instantiation(instance):
    assert isinstance(instance, Food_Serving_UseCase)

@given(instance=Check_Out_UseCase_strategy)
@settings(max_examples=50)
def test_check_out_usecase_instantiation(instance):
    assert isinstance(instance, Check_Out_UseCase)

@given(instance=Check_In_UseCase_strategy)
@settings(max_examples=50)
def test_check_in_usecase_instantiation(instance):
    assert isinstance(instance, Check_In_UseCase)

@given(instance=Cancel_Reservation_UseCase_strategy)
@settings(max_examples=50)
def test_cancel_reservation_usecase_instantiation(instance):
    assert isinstance(instance, Cancel_Reservation_UseCase)

@given(instance=Book_Room_UseCase_strategy)
@settings(max_examples=50)
def test_book_room_usecase_instantiation(instance):
    assert isinstance(instance, Book_Room_UseCase)
