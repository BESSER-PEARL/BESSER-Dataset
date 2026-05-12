import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Flight,
    Customers,
    Seats,
    Reservation,
    Ticket,
    Airport,
    Plane,
    Routes,
    Enumeration,
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
    assert "Date" in params, "Missing parameter 'Date'"
    assert "FlightNumber" in params, "Missing parameter 'FlightNumber'"

def test_flight_has_Date():
    assert hasattr(Flight, "Date")
    descriptor = None
    for klass in Flight.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_FlightNumber():
    assert hasattr(Flight, "FlightNumber")
    descriptor = None
    for klass in Flight.__mro__:
        if "FlightNumber" in klass.__dict__:
            descriptor = klass.__dict__["FlightNumber"]
            break
    assert isinstance(descriptor, property)



def test_customers_is_not_abstract():
    assert not inspect.isabstract(Customers)


def test_customers_constructor_exists():
    assert callable(Customers.__init__)


def test_customers_constructor_args():
    sig = inspect.signature(Customers.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "IdCustomer" in params, "Missing parameter 'IdCustomer'"
    assert "NameCustomer" in params, "Missing parameter 'NameCustomer'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_customers_has_Password():
    assert hasattr(Customers, "Password")
    descriptor = None
    for klass in Customers.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_customers_has_IdCustomer():
    assert hasattr(Customers, "IdCustomer")
    descriptor = None
    for klass in Customers.__mro__:
        if "IdCustomer" in klass.__dict__:
            descriptor = klass.__dict__["IdCustomer"]
            break
    assert isinstance(descriptor, property)

def test_customers_has_NameCustomer():
    assert hasattr(Customers, "NameCustomer")
    descriptor = None
    for klass in Customers.__mro__:
        if "NameCustomer" in klass.__dict__:
            descriptor = klass.__dict__["NameCustomer"]
            break
    assert isinstance(descriptor, property)

def test_customers_has_Email():
    assert hasattr(Customers, "Email")
    descriptor = None
    for klass in Customers.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_seats_is_not_abstract():
    assert not inspect.isabstract(Seats)


def test_seats_constructor_exists():
    assert callable(Seats.__init__)


def test_seats_constructor_args():
    sig = inspect.signature(Seats.__init__)
    params = list(sig.parameters.keys())
    assert "Availability" in params, "Missing parameter 'Availability'"
    assert "SeatNumber" in params, "Missing parameter 'SeatNumber'"

def test_seats_has_Availability():
    assert hasattr(Seats, "Availability")
    descriptor = None
    for klass in Seats.__mro__:
        if "Availability" in klass.__dict__:
            descriptor = klass.__dict__["Availability"]
            break
    assert isinstance(descriptor, property)

def test_seats_has_SeatNumber():
    assert hasattr(Seats, "SeatNumber")
    descriptor = None
    for klass in Seats.__mro__:
        if "SeatNumber" in klass.__dict__:
            descriptor = klass.__dict__["SeatNumber"]
            break
    assert isinstance(descriptor, property)



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(Reservation)


def test_reservation_constructor_exists():
    assert callable(Reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(Reservation.__init__)
    params = list(sig.parameters.keys())



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "DateTime" in params, "Missing parameter 'DateTime'"
    assert "TicketID" in params, "Missing parameter 'TicketID'"
    assert "Gate" in params, "Missing parameter 'Gate'"
    assert "TicketType" in params, "Missing parameter 'TicketType'"

def test_ticket_has_Price():
    assert hasattr(Ticket, "Price")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_DateTime():
    assert hasattr(Ticket, "DateTime")
    descriptor = None
    for klass in Ticket.__mro__:
        if "DateTime" in klass.__dict__:
            descriptor = klass.__dict__["DateTime"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_TicketID():
    assert hasattr(Ticket, "TicketID")
    descriptor = None
    for klass in Ticket.__mro__:
        if "TicketID" in klass.__dict__:
            descriptor = klass.__dict__["TicketID"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Gate():
    assert hasattr(Ticket, "Gate")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Gate" in klass.__dict__:
            descriptor = klass.__dict__["Gate"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_TicketType():
    assert hasattr(Ticket, "TicketType")
    descriptor = None
    for klass in Ticket.__mro__:
        if "TicketType" in klass.__dict__:
            descriptor = klass.__dict__["TicketType"]
            break
    assert isinstance(descriptor, property)



def test_airport_is_not_abstract():
    assert not inspect.isabstract(Airport)


def test_airport_constructor_exists():
    assert callable(Airport.__init__)


def test_airport_constructor_args():
    sig = inspect.signature(Airport.__init__)
    params = list(sig.parameters.keys())
    assert "AirportName" in params, "Missing parameter 'AirportName'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "AirportID" in params, "Missing parameter 'AirportID'"

def test_airport_has_AirportName():
    assert hasattr(Airport, "AirportName")
    descriptor = None
    for klass in Airport.__mro__:
        if "AirportName" in klass.__dict__:
            descriptor = klass.__dict__["AirportName"]
            break
    assert isinstance(descriptor, property)

def test_airport_has_Address():
    assert hasattr(Airport, "Address")
    descriptor = None
    for klass in Airport.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_airport_has_AirportID():
    assert hasattr(Airport, "AirportID")
    descriptor = None
    for klass in Airport.__mro__:
        if "AirportID" in klass.__dict__:
            descriptor = klass.__dict__["AirportID"]
            break
    assert isinstance(descriptor, property)



def test_plane_is_not_abstract():
    assert not inspect.isabstract(Plane)


def test_plane_constructor_exists():
    assert callable(Plane.__init__)


def test_plane_constructor_args():
    sig = inspect.signature(Plane.__init__)
    params = list(sig.parameters.keys())
    assert "Capacity" in params, "Missing parameter 'Capacity'"
    assert "PlaneId" in params, "Missing parameter 'PlaneId'"
    assert "PlaneName" in params, "Missing parameter 'PlaneName'"

def test_plane_has_Capacity():
    assert hasattr(Plane, "Capacity")
    descriptor = None
    for klass in Plane.__mro__:
        if "Capacity" in klass.__dict__:
            descriptor = klass.__dict__["Capacity"]
            break
    assert isinstance(descriptor, property)

def test_plane_has_PlaneId():
    assert hasattr(Plane, "PlaneId")
    descriptor = None
    for klass in Plane.__mro__:
        if "PlaneId" in klass.__dict__:
            descriptor = klass.__dict__["PlaneId"]
            break
    assert isinstance(descriptor, property)

def test_plane_has_PlaneName():
    assert hasattr(Plane, "PlaneName")
    descriptor = None
    for klass in Plane.__mro__:
        if "PlaneName" in klass.__dict__:
            descriptor = klass.__dict__["PlaneName"]
            break
    assert isinstance(descriptor, property)



def test_routes_is_not_abstract():
    assert not inspect.isabstract(Routes)


def test_routes_constructor_exists():
    assert callable(Routes.__init__)


def test_routes_constructor_args():
    sig = inspect.signature(Routes.__init__)
    params = list(sig.parameters.keys())
    assert "RouteID" in params, "Missing parameter 'RouteID'"
    assert "DestinationAirport" in params, "Missing parameter 'DestinationAirport'"
    assert "OriginAirport" in params, "Missing parameter 'OriginAirport'"

def test_routes_has_RouteID():
    assert hasattr(Routes, "RouteID")
    descriptor = None
    for klass in Routes.__mro__:
        if "RouteID" in klass.__dict__:
            descriptor = klass.__dict__["RouteID"]
            break
    assert isinstance(descriptor, property)

def test_routes_has_DestinationAirport():
    assert hasattr(Routes, "DestinationAirport")
    descriptor = None
    for klass in Routes.__mro__:
        if "DestinationAirport" in klass.__dict__:
            descriptor = klass.__dict__["DestinationAirport"]
            break
    assert isinstance(descriptor, property)

def test_routes_has_OriginAirport():
    assert hasattr(Routes, "OriginAirport")
    descriptor = None
    for klass in Routes.__mro__:
        if "OriginAirport" in klass.__dict__:
            descriptor = klass.__dict__["OriginAirport"]
            break
    assert isinstance(descriptor, property)

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
    Date=
        safe_text,
    FlightNumber=
        safe_text
)
Customers_strategy = st.builds(
    Customers,
    Password=
        safe_text,
    IdCustomer=
        safe_text,
    NameCustomer=
        safe_text,
    Email=
        safe_text
)
Seats_strategy = st.builds(
    Seats,
    Availability=
        st.booleans(),
    SeatNumber=
        st.integers()
)
Reservation_strategy = st.builds(
    Reservation,
)
Ticket_strategy = st.builds(
    Ticket,
    Price=
        safe_text,
    DateTime=
        safe_text,
    TicketID=
        safe_text,
    Gate=
        safe_text,
    TicketType=
        safe_text
)
Airport_strategy = st.builds(
    Airport,
    AirportName=
        safe_text,
    Address=
        safe_text,
    AirportID=
        safe_text
)
Plane_strategy = st.builds(
    Plane,
    Capacity=
        st.integers(),
    PlaneId=
        safe_text,
    PlaneName=
        safe_text
)
Routes_strategy = st.builds(
    Routes,
    RouteID=
        safe_text,
    DestinationAirport=
        safe_text,
    OriginAirport=
        safe_text
)

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Flight_strategy)
def test_flight_FlightNumber_setter(instance):
    original = instance.FlightNumber
    instance.FlightNumber = original
    assert instance.FlightNumber == original

@given(instance=Customers_strategy)
@settings(max_examples=50)
def test_customers_instantiation(instance):
    assert isinstance(instance, Customers)



@given(instance=Customers_strategy)
def test_customers_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Customers_strategy)
def test_customers_IdCustomer_setter(instance):
    original = instance.IdCustomer
    instance.IdCustomer = original
    assert instance.IdCustomer == original



@given(instance=Customers_strategy)
def test_customers_NameCustomer_setter(instance):
    original = instance.NameCustomer
    instance.NameCustomer = original
    assert instance.NameCustomer == original



@given(instance=Customers_strategy)
def test_customers_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Seats_strategy)
@settings(max_examples=50)
def test_seats_instantiation(instance):
    assert isinstance(instance, Seats)



@given(instance=Seats_strategy)
def test_seats_Availability_setter(instance):
    original = instance.Availability
    instance.Availability = original
    assert instance.Availability == original



@given(instance=Seats_strategy)
def test_seats_SeatNumber_setter(instance):
    original = instance.SeatNumber
    instance.SeatNumber = original
    assert instance.SeatNumber == original

@given(instance=Reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, Reservation)

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
def test_ticket_DateTime_setter(instance):
    original = instance.DateTime
    instance.DateTime = original
    assert instance.DateTime == original



@given(instance=Ticket_strategy)
def test_ticket_TicketID_setter(instance):
    original = instance.TicketID
    instance.TicketID = original
    assert instance.TicketID == original



@given(instance=Ticket_strategy)
def test_ticket_Gate_setter(instance):
    original = instance.Gate
    instance.Gate = original
    assert instance.Gate == original



@given(instance=Ticket_strategy)
def test_ticket_TicketType_setter(instance):
    original = instance.TicketType
    instance.TicketType = original
    assert instance.TicketType == original

@given(instance=Airport_strategy)
@settings(max_examples=50)
def test_airport_instantiation(instance):
    assert isinstance(instance, Airport)



@given(instance=Airport_strategy)
def test_airport_AirportName_setter(instance):
    original = instance.AirportName
    instance.AirportName = original
    assert instance.AirportName == original



@given(instance=Airport_strategy)
def test_airport_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Airport_strategy)
def test_airport_AirportID_setter(instance):
    original = instance.AirportID
    instance.AirportID = original
    assert instance.AirportID == original

@given(instance=Plane_strategy)
@settings(max_examples=50)
def test_plane_instantiation(instance):
    assert isinstance(instance, Plane)



@given(instance=Plane_strategy)
def test_plane_Capacity_setter(instance):
    original = instance.Capacity
    instance.Capacity = original
    assert instance.Capacity == original



@given(instance=Plane_strategy)
def test_plane_PlaneId_setter(instance):
    original = instance.PlaneId
    instance.PlaneId = original
    assert instance.PlaneId == original



@given(instance=Plane_strategy)
def test_plane_PlaneName_setter(instance):
    original = instance.PlaneName
    instance.PlaneName = original
    assert instance.PlaneName == original

@given(instance=Routes_strategy)
@settings(max_examples=50)
def test_routes_instantiation(instance):
    assert isinstance(instance, Routes)



@given(instance=Routes_strategy)
def test_routes_RouteID_setter(instance):
    original = instance.RouteID
    instance.RouteID = original
    assert instance.RouteID == original



@given(instance=Routes_strategy)
def test_routes_DestinationAirport_setter(instance):
    original = instance.DestinationAirport
    instance.DestinationAirport = original
    assert instance.DestinationAirport == original



@given(instance=Routes_strategy)
def test_routes_OriginAirport_setter(instance):
    original = instance.OriginAirport
    instance.OriginAirport = original
    assert instance.OriginAirport == original
