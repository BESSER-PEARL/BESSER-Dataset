import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Flight,
    Answer,
    Ticket,
    Booking,
    Client,
    Problem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Origin" in params, "Missing parameter 'Origin'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Company" in params, "Missing parameter 'Company'"
    assert "Destination" in params, "Missing parameter 'Destination'"
    assert "Max_Passangers" in params, "Missing parameter 'Max_Passangers'"

def test_flight_has_Time():
    assert hasattr(Flight, "Time")
    descriptor = None
    for klass in Flight.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Origin():
    assert hasattr(Flight, "Origin")
    descriptor = None
    for klass in Flight.__mro__:
        if "Origin" in klass.__dict__:
            descriptor = klass.__dict__["Origin"]
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

def test_flight_has_Company():
    assert hasattr(Flight, "Company")
    descriptor = None
    for klass in Flight.__mro__:
        if "Company" in klass.__dict__:
            descriptor = klass.__dict__["Company"]
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

def test_flight_has_Max_Passangers():
    assert hasattr(Flight, "Max_Passangers")
    descriptor = None
    for klass in Flight.__mro__:
        if "Max_Passangers" in klass.__dict__:
            descriptor = klass.__dict__["Max_Passangers"]
            break
    assert isinstance(descriptor, property)



def test_answer_is_not_abstract():
    assert not inspect.isabstract(Answer)


def test_answer_constructor_exists():
    assert callable(Answer.__init__)


def test_answer_constructor_args():
    sig = inspect.signature(Answer.__init__)
    params = list(sig.parameters.keys())



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "Seat" in params, "Missing parameter 'Seat'"
    assert "Booking_Class" in params, "Missing parameter 'Booking_Class'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Clients" in params, "Missing parameter 'Clients'"

def test_ticket_has_Seat():
    assert hasattr(Ticket, "Seat")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Seat" in klass.__dict__:
            descriptor = klass.__dict__["Seat"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Booking_Class():
    assert hasattr(Ticket, "Booking_Class")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Booking_Class" in klass.__dict__:
            descriptor = klass.__dict__["Booking_Class"]
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

def test_ticket_has_Clients():
    assert hasattr(Ticket, "Clients")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Clients" in klass.__dict__:
            descriptor = klass.__dict__["Clients"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Luggage" in params, "Missing parameter 'Luggage'"
    assert "Destination" in params, "Missing parameter 'Destination'"
    assert "Origin" in params, "Missing parameter 'Origin'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Tickets" in params, "Missing parameter 'Tickets'"

def test_booking_has_Time():
    assert hasattr(Booking, "Time")
    descriptor = None
    for klass in Booking.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Luggage():
    assert hasattr(Booking, "Luggage")
    descriptor = None
    for klass in Booking.__mro__:
        if "Luggage" in klass.__dict__:
            descriptor = klass.__dict__["Luggage"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Destination():
    assert hasattr(Booking, "Destination")
    descriptor = None
    for klass in Booking.__mro__:
        if "Destination" in klass.__dict__:
            descriptor = klass.__dict__["Destination"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Origin():
    assert hasattr(Booking, "Origin")
    descriptor = None
    for klass in Booking.__mro__:
        if "Origin" in klass.__dict__:
            descriptor = klass.__dict__["Origin"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Id():
    assert hasattr(Booking, "Id")
    descriptor = None
    for klass in Booking.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Tickets():
    assert hasattr(Booking, "Tickets")
    descriptor = None
    for klass in Booking.__mro__:
        if "Tickets" in klass.__dict__:
            descriptor = klass.__dict__["Tickets"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "Bookings" in params, "Missing parameter 'Bookings'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Loyalty_card" in params, "Missing parameter 'Loyalty_card'"

def test_client_has_Bookings():
    assert hasattr(Client, "Bookings")
    descriptor = None
    for klass in Client.__mro__:
        if "Bookings" in klass.__dict__:
            descriptor = klass.__dict__["Bookings"]
            break
    assert isinstance(descriptor, property)

def test_client_has_Name():
    assert hasattr(Client, "Name")
    descriptor = None
    for klass in Client.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_client_has_Id():
    assert hasattr(Client, "Id")
    descriptor = None
    for klass in Client.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_client_has_Loyalty_card():
    assert hasattr(Client, "Loyalty_card")
    descriptor = None
    for klass in Client.__mro__:
        if "Loyalty_card" in klass.__dict__:
            descriptor = klass.__dict__["Loyalty_card"]
            break
    assert isinstance(descriptor, property)



def test_problem_is_not_abstract():
    assert not inspect.isabstract(Problem)


def test_problem_constructor_exists():
    assert callable(Problem.__init__)


def test_problem_constructor_args():
    sig = inspect.signature(Problem.__init__)
    params = list(sig.parameters.keys())
    assert "Content" in params, "Missing parameter 'Content'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_problem_has_Content():
    assert hasattr(Problem, "Content")
    descriptor = None
    for klass in Problem.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)

def test_problem_has_Id():
    assert hasattr(Problem, "Id")
    descriptor = None
    for klass in Problem.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_problem_has_Type():
    assert hasattr(Problem, "Type")
    descriptor = None
    for klass in Problem.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
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
Flight_strategy = st.builds(
    Flight,
    Time=
        safe_text,
    Origin=
        safe_text,
    Id=
        safe_text,
    Company=
        safe_text,
    Destination=
        safe_text,
    Max_Passangers=
        st.integers()
)
Answer_strategy = st.builds(
    Answer,
)
Ticket_strategy = st.builds(
    Ticket,
    Seat=
        safe_text,
    Booking_Class=
        safe_text,
    Id=
        safe_text,
    Clients=
        st.none()
)
Booking_strategy = st.builds(
    Booking,
    Time=
        safe_text,
    Luggage=
        safe_text,
    Destination=
        safe_text,
    Origin=
        safe_text,
    Id=
        safe_text,
    Tickets=
        st.none()
)
Client_strategy = st.builds(
    Client,
    Bookings=
        st.none(),
    Name=
        safe_text,
    Id=
        safe_text,
    Loyalty_card=
        safe_text
)
Problem_strategy = st.builds(
    Problem,
    Content=
        safe_text,
    Id=
        safe_text,
    Type=
        safe_text
)

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Flight_strategy)
def test_flight_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original



@given(instance=Flight_strategy)
def test_flight_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Flight_strategy)
def test_flight_Company_setter(instance):
    original = instance.Company
    instance.Company = original
    assert instance.Company == original



@given(instance=Flight_strategy)
def test_flight_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original



@given(instance=Flight_strategy)
def test_flight_Max_Passangers_setter(instance):
    original = instance.Max_Passangers
    instance.Max_Passangers = original
    assert instance.Max_Passangers == original

@given(instance=Answer_strategy)
@settings(max_examples=50)
def test_answer_instantiation(instance):
    assert isinstance(instance, Answer)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_Seat_setter(instance):
    original = instance.Seat
    instance.Seat = original
    assert instance.Seat == original



@given(instance=Ticket_strategy)
def test_ticket_Booking_Class_setter(instance):
    original = instance.Booking_Class
    instance.Booking_Class = original
    assert instance.Booking_Class == original



@given(instance=Ticket_strategy)
def test_ticket_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Ticket_strategy)
def test_ticket_Clients_setter(instance):
    original = instance.Clients
    instance.Clients = original
    assert instance.Clients == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Booking_strategy)
def test_booking_Luggage_setter(instance):
    original = instance.Luggage
    instance.Luggage = original
    assert instance.Luggage == original



@given(instance=Booking_strategy)
def test_booking_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original



@given(instance=Booking_strategy)
def test_booking_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original



@given(instance=Booking_strategy)
def test_booking_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Booking_strategy)
def test_booking_Tickets_setter(instance):
    original = instance.Tickets
    instance.Tickets = original
    assert instance.Tickets == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)



@given(instance=Client_strategy)
def test_client_Bookings_setter(instance):
    original = instance.Bookings
    instance.Bookings = original
    assert instance.Bookings == original



@given(instance=Client_strategy)
def test_client_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Client_strategy)
def test_client_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Client_strategy)
def test_client_Loyalty_card_setter(instance):
    original = instance.Loyalty_card
    instance.Loyalty_card = original
    assert instance.Loyalty_card == original

@given(instance=Problem_strategy)
@settings(max_examples=50)
def test_problem_instantiation(instance):
    assert isinstance(instance, Problem)



@given(instance=Problem_strategy)
def test_problem_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original



@given(instance=Problem_strategy)
def test_problem_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Problem_strategy)
def test_problem_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original
