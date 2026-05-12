import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Actor2_Actor,
    Actor_Actor,
    Manager,
    Class,
    Customer,
    Waiter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Contact" in params, "Missing parameter 'Contact'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Personalnformation" in params, "Missing parameter 'Personalnformation'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_manager_has_Name():
    assert hasattr(Manager, "Name")
    descriptor = None
    for klass in Manager.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Contact():
    assert hasattr(Manager, "Contact")
    descriptor = None
    for klass in Manager.__mro__:
        if "Contact" in klass.__dict__:
            descriptor = klass.__dict__["Contact"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Address():
    assert hasattr(Manager, "Address")
    descriptor = None
    for klass in Manager.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Personalnformation():
    assert hasattr(Manager, "Personalnformation")
    descriptor = None
    for klass in Manager.__mro__:
        if "Personalnformation" in klass.__dict__:
            descriptor = klass.__dict__["Personalnformation"]
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



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "Dishes_Ordered" in params, "Missing parameter 'Dishes_Ordered'"
    assert "Contact_Number" in params, "Missing parameter 'Contact_Number'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "date" in params, "Missing parameter 'date'"
    assert "Reservation" in params, "Missing parameter 'Reservation'"

def test_customer_has_reservedTables():
    assert hasattr(Customer, "reservedTables")
    descriptor = None
    for klass in Customer.__mro__:
        if "reservedTables" in klass.__dict__:
            descriptor = klass.__dict__["reservedTables"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Dishes_Ordered():
    assert hasattr(Customer, "Dishes_Ordered")
    descriptor = None
    for klass in Customer.__mro__:
        if "Dishes_Ordered" in klass.__dict__:
            descriptor = klass.__dict__["Dishes_Ordered"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Contact_Number():
    assert hasattr(Customer, "Contact_Number")
    descriptor = None
    for klass in Customer.__mro__:
        if "Contact_Number" in klass.__dict__:
            descriptor = klass.__dict__["Contact_Number"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_date():
    assert hasattr(Customer, "date")
    descriptor = None
    for klass in Customer.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Reservation():
    assert hasattr(Customer, "Reservation")
    descriptor = None
    for klass in Customer.__mro__:
        if "Reservation" in klass.__dict__:
            descriptor = klass.__dict__["Reservation"]
            break
    assert isinstance(descriptor, property)



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Contact" in params, "Missing parameter 'Contact'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Personal_Information" in params, "Missing parameter 'Personal_Information'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_waiter_has_ID():
    assert hasattr(Waiter, "ID")
    descriptor = None
    for klass in Waiter.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_waiter_has_Contact():
    assert hasattr(Waiter, "Contact")
    descriptor = None
    for klass in Waiter.__mro__:
        if "Contact" in klass.__dict__:
            descriptor = klass.__dict__["Contact"]
            break
    assert isinstance(descriptor, property)

def test_waiter_has_Address():
    assert hasattr(Waiter, "Address")
    descriptor = None
    for klass in Waiter.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_waiter_has_Personal_Information():
    assert hasattr(Waiter, "Personal_Information")
    descriptor = None
    for klass in Waiter.__mro__:
        if "Personal_Information" in klass.__dict__:
            descriptor = klass.__dict__["Personal_Information"]
            break
    assert isinstance(descriptor, property)

def test_waiter_has_Name():
    assert hasattr(Waiter, "Name")
    descriptor = None
    for klass in Waiter.__mro__:
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
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Manager_strategy = st.builds(
    Manager,
    Name=
        safe_text,
    Contact=
        st.integers(),
    Address=
        safe_text,
    Personalnformation=
        safe_text,
    ID=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
Customer_strategy = st.builds(
    Customer,
    reservedTables=
        safe_text,
    Dishes_Ordered=
        safe_text,
    Contact_Number=
        st.integers(),
    Name=
        safe_text,
    date=
        safe_text,
    Reservation=
        st.booleans()
)
Waiter_strategy = st.builds(
    Waiter,
    ID=
        safe_text,
    Contact=
        st.integers(),
    Address=
        safe_text,
    Personal_Information=
        safe_text,
    Name=
        safe_text
)

@given(instance=Actor2_Actor_strategy)
@settings(max_examples=50)
def test_actor2_actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Manager_strategy)
def test_manager_Contact_setter(instance):
    original = instance.Contact
    instance.Contact = original
    assert instance.Contact == original



@given(instance=Manager_strategy)
def test_manager_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Manager_strategy)
def test_manager_Personalnformation_setter(instance):
    original = instance.Personalnformation
    instance.Personalnformation = original
    assert instance.Personalnformation == original



@given(instance=Manager_strategy)
def test_manager_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Customer_strategy)
def test_customer_Dishes_Ordered_setter(instance):
    original = instance.Dishes_Ordered
    instance.Dishes_Ordered = original
    assert instance.Dishes_Ordered == original



@given(instance=Customer_strategy)
def test_customer_Contact_Number_setter(instance):
    original = instance.Contact_Number
    instance.Contact_Number = original
    assert instance.Contact_Number == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_strategy)
def test_customer_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Customer_strategy)
def test_customer_Reservation_setter(instance):
    original = instance.Reservation
    instance.Reservation = original
    assert instance.Reservation == original

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)



@given(instance=Waiter_strategy)
def test_waiter_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Waiter_strategy)
def test_waiter_Contact_setter(instance):
    original = instance.Contact
    instance.Contact = original
    assert instance.Contact == original



@given(instance=Waiter_strategy)
def test_waiter_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Waiter_strategy)
def test_waiter_Personal_Information_setter(instance):
    original = instance.Personal_Information
    instance.Personal_Information = original
    assert instance.Personal_Information == original



@given(instance=Waiter_strategy)
def test_waiter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
