import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Online_Customer,
    Staff,
    Payment,
    Bill,
    Party,
    Table,
    Reservation,
    Kitchen,
    Guest,
    Order,
    Host,
    Waiter,
    Date,
    ReservationType2,
    ReservationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_online_customer_is_not_abstract():
    assert not inspect.isabstract(Online_Customer)


def test_online_customer_constructor_exists():
    assert callable(Online_Customer.__init__)


def test_online_customer_constructor_args():
    sig = inspect.signature(Online_Customer.__init__)
    params = list(sig.parameters.keys())



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Staff_ID" in params, "Missing parameter 'Staff_ID'"
    assert "JobType" in params, "Missing parameter 'JobType'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Phone" in params, "Missing parameter 'Phone'"

def test_staff_has_Staff_ID():
    assert hasattr(Staff, "Staff_ID")
    descriptor = None
    for klass in Staff.__mro__:
        if "Staff_ID" in klass.__dict__:
            descriptor = klass.__dict__["Staff_ID"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_JobType():
    assert hasattr(Staff, "JobType")
    descriptor = None
    for klass in Staff.__mro__:
        if "JobType" in klass.__dict__:
            descriptor = klass.__dict__["JobType"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Name():
    assert hasattr(Staff, "Name")
    descriptor = None
    for klass in Staff.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Phone():
    assert hasattr(Staff, "Phone")
    descriptor = None
    for klass in Staff.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "TotalAmount" in params, "Missing parameter 'TotalAmount'"
    assert "Tax" in params, "Missing parameter 'Tax'"
    assert "Tip" in params, "Missing parameter 'Tip'"

def test_bill_has_TotalAmount():
    assert hasattr(Bill, "TotalAmount")
    descriptor = None
    for klass in Bill.__mro__:
        if "TotalAmount" in klass.__dict__:
            descriptor = klass.__dict__["TotalAmount"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Tax():
    assert hasattr(Bill, "Tax")
    descriptor = None
    for klass in Bill.__mro__:
        if "Tax" in klass.__dict__:
            descriptor = klass.__dict__["Tax"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Tip():
    assert hasattr(Bill, "Tip")
    descriptor = None
    for klass in Bill.__mro__:
        if "Tip" in klass.__dict__:
            descriptor = klass.__dict__["Tip"]
            break
    assert isinstance(descriptor, property)



def test_party_is_not_abstract():
    assert not inspect.isabstract(Party)


def test_party_constructor_exists():
    assert callable(Party.__init__)


def test_party_constructor_args():
    sig = inspect.signature(Party.__init__)
    params = list(sig.parameters.keys())
    assert "Number_of_Guests" in params, "Missing parameter 'Number_of_Guests'"
    assert "Number_Of_Adults" in params, "Missing parameter 'Number_Of_Adults'"
    assert "Number_Of_Children" in params, "Missing parameter 'Number_Of_Children'"

def test_party_has_Number_of_Guests():
    assert hasattr(Party, "Number_of_Guests")
    descriptor = None
    for klass in Party.__mro__:
        if "Number_of_Guests" in klass.__dict__:
            descriptor = klass.__dict__["Number_of_Guests"]
            break
    assert isinstance(descriptor, property)

def test_party_has_Number_Of_Adults():
    assert hasattr(Party, "Number_Of_Adults")
    descriptor = None
    for klass in Party.__mro__:
        if "Number_Of_Adults" in klass.__dict__:
            descriptor = klass.__dict__["Number_Of_Adults"]
            break
    assert isinstance(descriptor, property)

def test_party_has_Number_Of_Children():
    assert hasattr(Party, "Number_Of_Children")
    descriptor = None
    for klass in Party.__mro__:
        if "Number_Of_Children" in klass.__dict__:
            descriptor = klass.__dict__["Number_Of_Children"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "Capacity" in params, "Missing parameter 'Capacity'"
    assert "TableID" in params, "Missing parameter 'TableID'"

def test_table_has_Capacity():
    assert hasattr(Table, "Capacity")
    descriptor = None
    for klass in Table.__mro__:
        if "Capacity" in klass.__dict__:
            descriptor = klass.__dict__["Capacity"]
            break
    assert isinstance(descriptor, property)

def test_table_has_TableID():
    assert hasattr(Table, "TableID")
    descriptor = None
    for klass in Table.__mro__:
        if "TableID" in klass.__dict__:
            descriptor = klass.__dict__["TableID"]
            break
    assert isinstance(descriptor, property)



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(Reservation)


def test_reservation_constructor_exists():
    assert callable(Reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "ReservationID" in params, "Missing parameter 'ReservationID'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_reservation_has_ReservationID():
    assert hasattr(Reservation, "ReservationID")
    descriptor = None
    for klass in Reservation.__mro__:
        if "ReservationID" in klass.__dict__:
            descriptor = klass.__dict__["ReservationID"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_Time():
    assert hasattr(Reservation, "Time")
    descriptor = None
    for klass in Reservation.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_reservation_has_Date():
    assert hasattr(Reservation, "Date")
    descriptor = None
    for klass in Reservation.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_kitchen_is_not_abstract():
    assert not inspect.isabstract(Kitchen)


def test_kitchen_constructor_exists():
    assert callable(Kitchen.__init__)


def test_kitchen_constructor_args():
    sig = inspect.signature(Kitchen.__init__)
    params = list(sig.parameters.keys())



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Guest_ID" in params, "Missing parameter 'Guest_ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_guest_has_Phone():
    assert hasattr(Guest, "Phone")
    descriptor = None
    for klass in Guest.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_Guest_ID():
    assert hasattr(Guest, "Guest_ID")
    descriptor = None
    for klass in Guest.__mro__:
        if "Guest_ID" in klass.__dict__:
            descriptor = klass.__dict__["Guest_ID"]
            break
    assert isinstance(descriptor, property)

def test_guest_has_Name():
    assert hasattr(Guest, "Name")
    descriptor = None
    for klass in Guest.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())



def test_host_is_not_abstract():
    assert not inspect.isabstract(Host)


def test_host_constructor_exists():
    assert callable(Host.__init__)


def test_host_constructor_args():
    sig = inspect.signature(Host.__init__)
    params = list(sig.parameters.keys())



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())

def test_date_exists():
    # Check that the Enumeration exists
    assert Date is not None

def test_date_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Date]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Date"

def test_reservationtype2_exists():
    # Check that the Enumeration exists
    assert ReservationType2 is not None

def test_reservationtype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReservationType2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReservationType2"

def test_reservationtype_exists():
    # Check that the Enumeration exists
    assert ReservationType is not None

def test_reservationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReservationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReservationType"


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
Online_Customer_strategy = st.builds(
    Online_Customer,
)
Staff_strategy = st.builds(
    Staff,
    Staff_ID=
        safe_text,
    JobType=
        safe_text,
    Name=
        safe_text,
    Phone=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
)
Bill_strategy = st.builds(
    Bill,
    TotalAmount=
        st.integers(),
    Tax=
        st.integers(),
    Tip=
        st.integers()
)
Party_strategy = st.builds(
    Party,
    Number_of_Guests=
        st.integers(),
    Number_Of_Adults=
        st.integers(),
    Number_Of_Children=
        st.integers()
)
Table_strategy = st.builds(
    Table,
    Capacity=
        st.integers(),
    TableID=
        safe_text
)
Reservation_strategy = st.builds(
    Reservation,
    ReservationID=
        safe_text,
    Time=
        safe_text,
    Date=
        st.dates()
)
Kitchen_strategy = st.builds(
    Kitchen,
)
Guest_strategy = st.builds(
    Guest,
    Phone=
        safe_text,
    Guest_ID=
        safe_text,
    Name=
        safe_text
)
Order_strategy = st.builds(
    Order,
)
Host_strategy = st.builds(
    Host,
)
Waiter_strategy = st.builds(
    Waiter,
)

@given(instance=Online_Customer_strategy)
@settings(max_examples=50)
def test_online_customer_instantiation(instance):
    assert isinstance(instance, Online_Customer)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Staff_ID_setter(instance):
    original = instance.Staff_ID
    instance.Staff_ID = original
    assert instance.Staff_ID == original



@given(instance=Staff_strategy)
def test_staff_JobType_setter(instance):
    original = instance.JobType
    instance.JobType = original
    assert instance.JobType == original



@given(instance=Staff_strategy)
def test_staff_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Staff_strategy)
def test_staff_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_TotalAmount_setter(instance):
    original = instance.TotalAmount
    instance.TotalAmount = original
    assert instance.TotalAmount == original



@given(instance=Bill_strategy)
def test_bill_Tax_setter(instance):
    original = instance.Tax
    instance.Tax = original
    assert instance.Tax == original



@given(instance=Bill_strategy)
def test_bill_Tip_setter(instance):
    original = instance.Tip
    instance.Tip = original
    assert instance.Tip == original

@given(instance=Party_strategy)
@settings(max_examples=50)
def test_party_instantiation(instance):
    assert isinstance(instance, Party)



@given(instance=Party_strategy)
def test_party_Number_of_Guests_setter(instance):
    original = instance.Number_of_Guests
    instance.Number_of_Guests = original
    assert instance.Number_of_Guests == original



@given(instance=Party_strategy)
def test_party_Number_Of_Adults_setter(instance):
    original = instance.Number_Of_Adults
    instance.Number_Of_Adults = original
    assert instance.Number_Of_Adults == original



@given(instance=Party_strategy)
def test_party_Number_Of_Children_setter(instance):
    original = instance.Number_Of_Children
    instance.Number_Of_Children = original
    assert instance.Number_Of_Children == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_Capacity_setter(instance):
    original = instance.Capacity
    instance.Capacity = original
    assert instance.Capacity == original



@given(instance=Table_strategy)
def test_table_TableID_setter(instance):
    original = instance.TableID
    instance.TableID = original
    assert instance.TableID == original

@given(instance=Reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, Reservation)



@given(instance=Reservation_strategy)
def test_reservation_ReservationID_setter(instance):
    original = instance.ReservationID
    instance.ReservationID = original
    assert instance.ReservationID == original



@given(instance=Reservation_strategy)
def test_reservation_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Reservation_strategy)
def test_reservation_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Kitchen_strategy)
@settings(max_examples=50)
def test_kitchen_instantiation(instance):
    assert isinstance(instance, Kitchen)

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)



@given(instance=Guest_strategy)
def test_guest_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Guest_strategy)
def test_guest_Guest_ID_setter(instance):
    original = instance.Guest_ID
    instance.Guest_ID = original
    assert instance.Guest_ID == original



@given(instance=Guest_strategy)
def test_guest_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)

@given(instance=Host_strategy)
@settings(max_examples=50)
def test_host_instantiation(instance):
    assert isinstance(instance, Host)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)
