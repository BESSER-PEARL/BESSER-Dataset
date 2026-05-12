import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ticket,
    Administrator,
    Flight,
    Bank,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_ticket_has_Price():
    assert hasattr(Ticket, "Price")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Id():
    assert hasattr(Ticket, "Id")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Customer_Name():
    assert hasattr(Ticket, "Customer_Name")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Type():
    assert hasattr(Ticket, "Type")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Fullname" in params, "Missing parameter 'Fullname'"
    assert "Account" in params, "Missing parameter 'Account'"

def test_administrator_has_Fullname():
    assert hasattr(Administrator, "Fullname")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Fullname" in klass.__dict__:
            descriptor = klass.__dict__["Fullname"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Account():
    assert hasattr(Administrator, "Account")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Account" in klass.__dict__:
            descriptor = klass.__dict__["Account"]
            break
    assert isinstance(descriptor, property)



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "Number_of_seats" in params, "Missing parameter 'Number_of_seats'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Destination" in params, "Missing parameter 'Destination'"
    assert "Source" in params, "Missing parameter 'Source'"

def test_flight_has_Number_of_seats():
    assert hasattr(Flight, "Number_of_seats")
    descriptor = None
    for klass in Flight.__mro__:
        if "Number_of_seats" in klass.__dict__:
            descriptor = klass.__dict__["Number_of_seats"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Time():
    assert hasattr(Flight, "Time")
    descriptor = None
    for klass in Flight.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Id():
    assert hasattr(Flight, "Id")
    descriptor = None
    for klass in Flight.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Name():
    assert hasattr(Flight, "Name")
    descriptor = None
    for klass in Flight.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Destination():
    assert hasattr(Flight, "Destination")
    descriptor = None
    for klass in Flight.__mro__:
        if "Destination" in klass.__dict__:
            descriptor = klass.__dict__["Destination"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Source():
    assert hasattr(Flight, "Source")
    descriptor = None
    for klass in Flight.__mro__:
        if "Source" in klass.__dict__:
            descriptor = klass.__dict__["Source"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Account" in params, "Missing parameter 'Account'"

def test_bank_has_Name():
    assert hasattr(Bank, "Name")
    descriptor = None
    for klass in Bank.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Account():
    assert hasattr(Bank, "Account")
    descriptor = None
    for klass in Bank.__mro__:
        if "Account" in klass.__dict__:
            descriptor = klass.__dict__["Account"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Fullname" in params, "Missing parameter 'Fullname'"
    assert "Card_details" in params, "Missing parameter 'Card_details'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Location" in params, "Missing parameter 'Location'"

def test_customer_has_Fullname():
    assert hasattr(Customer, "Fullname")
    descriptor = None
    for klass in Customer.__mro__:
        if "Fullname" in klass.__dict__:
            descriptor = klass.__dict__["Fullname"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Card_details():
    assert hasattr(Customer, "Card_details")
    descriptor = None
    for klass in Customer.__mro__:
        if "Card_details" in klass.__dict__:
            descriptor = klass.__dict__["Card_details"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Gender():
    assert hasattr(Customer, "Gender")
    descriptor = None
    for klass in Customer.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Location():
    assert hasattr(Customer, "Location")
    descriptor = None
    for klass in Customer.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
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
Ticket_strategy = st.builds(
    Ticket,
    Price=
        st.booleans(),
    Id=
        st.integers(),
    Customer_Name=
        safe_text,
    Type=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Fullname=
        safe_text,
    Account=
        safe_text
)
Flight_strategy = st.builds(
    Flight,
    Number_of_seats=
        st.integers(),
    Time=
        st.integers(),
    Id=
        st.none(),
    Name=
        safe_text,
    Destination=
        safe_text,
    Source=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    Name=
        safe_text,
    Account=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    Fullname=
        safe_text,
    Card_details=
        st.integers(),
    Gender=
        safe_text,
    Location=
        safe_text
)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Ticket_strategy)
def test_ticket_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Ticket_strategy)
def test_ticket_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original



@given(instance=Ticket_strategy)
def test_ticket_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Fullname_setter(instance):
    original = instance.Fullname
    instance.Fullname = original
    assert instance.Fullname == original



@given(instance=Administrator_strategy)
def test_administrator_Account_setter(instance):
    original = instance.Account
    instance.Account = original
    assert instance.Account == original

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_Number_of_seats_setter(instance):
    original = instance.Number_of_seats
    instance.Number_of_seats = original
    assert instance.Number_of_seats == original



@given(instance=Flight_strategy)
def test_flight_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Flight_strategy)
def test_flight_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Flight_strategy)
def test_flight_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Flight_strategy)
def test_flight_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original



@given(instance=Flight_strategy)
def test_flight_Source_setter(instance):
    original = instance.Source
    instance.Source = original
    assert instance.Source == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Bank_strategy)
def test_bank_Account_setter(instance):
    original = instance.Account
    instance.Account = original
    assert instance.Account == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Fullname_setter(instance):
    original = instance.Fullname
    instance.Fullname = original
    assert instance.Fullname == original



@given(instance=Customer_strategy)
def test_customer_Card_details_setter(instance):
    original = instance.Card_details
    instance.Card_details = original
    assert instance.Card_details == original



@given(instance=Customer_strategy)
def test_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_customer_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original
