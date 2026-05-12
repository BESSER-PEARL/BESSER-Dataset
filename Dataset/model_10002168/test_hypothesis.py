import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Payment,
    Airport,
    Ticket,
    Flight,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "price" in params, "Missing parameter 'price'"
    assert "Ticketnumber" in params, "Missing parameter 'Ticketnumber'"
    assert "Method" in params, "Missing parameter 'Method'"
    assert "username" in params, "Missing parameter 'username'"

def test_payment_has_date():
    assert hasattr(Payment, "date")
    descriptor = None
    for klass in Payment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_price():
    assert hasattr(Payment, "price")
    descriptor = None
    for klass in Payment.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Ticketnumber():
    assert hasattr(Payment, "Ticketnumber")
    descriptor = None
    for klass in Payment.__mro__:
        if "Ticketnumber" in klass.__dict__:
            descriptor = klass.__dict__["Ticketnumber"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Method():
    assert hasattr(Payment, "Method")
    descriptor = None
    for klass in Payment.__mro__:
        if "Method" in klass.__dict__:
            descriptor = klass.__dict__["Method"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_username():
    assert hasattr(Payment, "username")
    descriptor = None
    for klass in Payment.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_airport_is_not_abstract():
    assert not inspect.isabstract(Airport)


def test_airport_constructor_exists():
    assert callable(Airport.__init__)


def test_airport_constructor_args():
    sig = inspect.signature(Airport.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_airport_has_location():
    assert hasattr(Airport, "location")
    descriptor = None
    for klass in Airport.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_airport_has_code():
    assert hasattr(Airport, "code")
    descriptor = None
    for klass in Airport.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_airport_has_name():
    assert hasattr(Airport, "name")
    descriptor = None
    for klass in Airport.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "Flightnumber" in params, "Missing parameter 'Flightnumber'"
    assert "class" in params, "Missing parameter 'class'"
    assert "username" in params, "Missing parameter 'username'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "age" in params, "Missing parameter 'age'"
    assert "arrival" in params, "Missing parameter 'arrival'"
    assert "Ticketnumber" in params, "Missing parameter 'Ticketnumber'"
    assert "date" in params, "Missing parameter 'date'"
    assert "price" in params, "Missing parameter 'price'"

def test_ticket_has_Flightnumber():
    assert hasattr(Ticket, "Flightnumber")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Flightnumber" in klass.__dict__:
            descriptor = klass.__dict__["Flightnumber"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_class():
    assert hasattr(Ticket, "class")
    descriptor = None
    for klass in Ticket.__mro__:
        if "class" in klass.__dict__:
            descriptor = klass.__dict__["class"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_username():
    assert hasattr(Ticket, "username")
    descriptor = None
    for klass in Ticket.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_destination():
    assert hasattr(Ticket, "destination")
    descriptor = None
    for klass in Ticket.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_age():
    assert hasattr(Ticket, "age")
    descriptor = None
    for klass in Ticket.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_arrival():
    assert hasattr(Ticket, "arrival")
    descriptor = None
    for klass in Ticket.__mro__:
        if "arrival" in klass.__dict__:
            descriptor = klass.__dict__["arrival"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_Ticketnumber():
    assert hasattr(Ticket, "Ticketnumber")
    descriptor = None
    for klass in Ticket.__mro__:
        if "Ticketnumber" in klass.__dict__:
            descriptor = klass.__dict__["Ticketnumber"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_date():
    assert hasattr(Ticket, "date")
    descriptor = None
    for klass in Ticket.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_price():
    assert hasattr(Ticket, "price")
    descriptor = None
    for klass in Ticket.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "destination" in params, "Missing parameter 'destination'"
    assert "Flightname" in params, "Missing parameter 'Flightname'"
    assert "Flightnumber" in params, "Missing parameter 'Flightnumber'"
    assert "price" in params, "Missing parameter 'price'"
    assert "time" in params, "Missing parameter 'time'"
    assert "date" in params, "Missing parameter 'date'"
    assert "arrival" in params, "Missing parameter 'arrival'"

def test_flight_has_destination():
    assert hasattr(Flight, "destination")
    descriptor = None
    for klass in Flight.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Flightname():
    assert hasattr(Flight, "Flightname")
    descriptor = None
    for klass in Flight.__mro__:
        if "Flightname" in klass.__dict__:
            descriptor = klass.__dict__["Flightname"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_Flightnumber():
    assert hasattr(Flight, "Flightnumber")
    descriptor = None
    for klass in Flight.__mro__:
        if "Flightnumber" in klass.__dict__:
            descriptor = klass.__dict__["Flightnumber"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_price():
    assert hasattr(Flight, "price")
    descriptor = None
    for klass in Flight.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_time():
    assert hasattr(Flight, "time")
    descriptor = None
    for klass in Flight.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_date():
    assert hasattr(Flight, "date")
    descriptor = None
    for klass in Flight.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_flight_has_arrival():
    assert hasattr(Flight, "arrival")
    descriptor = None
    for klass in Flight.__mro__:
        if "arrival" in klass.__dict__:
            descriptor = klass.__dict__["arrival"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_user_has_gender():
    assert hasattr(User, "gender")
    descriptor = None
    for klass in User.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_user_has_age():
    assert hasattr(User, "age")
    descriptor = None
    for klass in User.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phone():
    assert hasattr(User, "phone")
    descriptor = None
    for klass in User.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
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
Payment_strategy = st.builds(
    Payment,
    date=
        st.none(),
    price=
        st.none(),
    Ticketnumber=
        st.none(),
    Method=
        safe_text,
    username=
        st.none()
)
Airport_strategy = st.builds(
    Airport,
    location=
        safe_text,
    code=
        st.integers(),
    name=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    Flightnumber=
        st.none(),
    class=
        safe_text,
    username=
        st.none(),
    destination=
        st.none(),
    age=
        st.none(),
    arrival=
        st.none(),
    Ticketnumber=
        st.integers(),
    date=
        st.integers(),
    price=
        st.integers()
)
Flight_strategy = st.builds(
    Flight,
    destination=
        safe_text,
    Flightname=
        safe_text,
    Flightnumber=
        st.integers(),
    price=
        st.integers(),
    time=
        st.integers(),
    date=
        st.integers(),
    arrival=
        safe_text
)
User_strategy = st.builds(
    User,
    gender=
        safe_text,
    age=
        st.integers(),
    name=
        safe_text,
    email=
        safe_text,
    phone=
        st.integers(),
    password=
        safe_text,
    username=
        safe_text
)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Payment_strategy)
def test_payment_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Payment_strategy)
def test_payment_Ticketnumber_setter(instance):
    original = instance.Ticketnumber
    instance.Ticketnumber = original
    assert instance.Ticketnumber == original



@given(instance=Payment_strategy)
def test_payment_Method_setter(instance):
    original = instance.Method
    instance.Method = original
    assert instance.Method == original



@given(instance=Payment_strategy)
def test_payment_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Airport_strategy)
@settings(max_examples=50)
def test_airport_instantiation(instance):
    assert isinstance(instance, Airport)



@given(instance=Airport_strategy)
def test_airport_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Airport_strategy)
def test_airport_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Airport_strategy)
def test_airport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_Flightnumber_setter(instance):
    original = instance.Flightnumber
    instance.Flightnumber = original
    assert instance.Flightnumber == original



@given(instance=Ticket_strategy)
def test_ticket_class_setter(instance):
    original = instance.class
    instance.class = original
    assert instance.class == original



@given(instance=Ticket_strategy)
def test_ticket_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Ticket_strategy)
def test_ticket_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Ticket_strategy)
def test_ticket_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Ticket_strategy)
def test_ticket_arrival_setter(instance):
    original = instance.arrival
    instance.arrival = original
    assert instance.arrival == original



@given(instance=Ticket_strategy)
def test_ticket_Ticketnumber_setter(instance):
    original = instance.Ticketnumber
    instance.Ticketnumber = original
    assert instance.Ticketnumber == original



@given(instance=Ticket_strategy)
def test_ticket_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Ticket_strategy)
def test_ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Flight_strategy)
def test_flight_Flightname_setter(instance):
    original = instance.Flightname
    instance.Flightname = original
    assert instance.Flightname == original



@given(instance=Flight_strategy)
def test_flight_Flightnumber_setter(instance):
    original = instance.Flightnumber
    instance.Flightnumber = original
    assert instance.Flightnumber == original



@given(instance=Flight_strategy)
def test_flight_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Flight_strategy)
def test_flight_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Flight_strategy)
def test_flight_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Flight_strategy)
def test_flight_arrival_setter(instance):
    original = instance.arrival
    instance.arrival = original
    assert instance.arrival == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=User_strategy)
def test_user_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_user_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original
