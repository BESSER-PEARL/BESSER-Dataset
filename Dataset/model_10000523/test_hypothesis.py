import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Timinglist,
    Flightlist,
    Admin,
    System,
    Ticket,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timinglist_is_not_abstract():
    assert not inspect.isabstract(Timinglist)


def test_timinglist_constructor_exists():
    assert callable(Timinglist.__init__)


def test_timinglist_constructor_args():
    sig = inspect.signature(Timinglist.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "source" in params, "Missing parameter 'source'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "flightname" in params, "Missing parameter 'flightname'"

def test_timinglist_has_time():
    assert hasattr(Timinglist, "time")
    descriptor = None
    for klass in Timinglist.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_timinglist_has_source():
    assert hasattr(Timinglist, "source")
    descriptor = None
    for klass in Timinglist.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_timinglist_has_destination():
    assert hasattr(Timinglist, "destination")
    descriptor = None
    for klass in Timinglist.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_timinglist_has_flightname():
    assert hasattr(Timinglist, "flightname")
    descriptor = None
    for klass in Timinglist.__mro__:
        if "flightname" in klass.__dict__:
            descriptor = klass.__dict__["flightname"]
            break
    assert isinstance(descriptor, property)



def test_flightlist_is_not_abstract():
    assert not inspect.isabstract(Flightlist)


def test_flightlist_constructor_exists():
    assert callable(Flightlist.__init__)


def test_flightlist_constructor_args():
    sig = inspect.signature(Flightlist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_flightlist_has_name():
    assert hasattr(Flightlist, "name")
    descriptor = None
    for klass in Flightlist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_flightlist_has_id():
    assert hasattr(Flightlist, "id")
    descriptor = None
    for klass in Flightlist.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "type" in params, "Missing parameter 'type'"
    assert "adminname" in params, "Missing parameter 'adminname'"
    assert "mobile" in params, "Missing parameter 'mobile'"

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_gender():
    assert hasattr(Admin, "gender")
    descriptor = None
    for klass in Admin.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_type():
    assert hasattr(Admin, "type")
    descriptor = None
    for klass in Admin.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_adminname():
    assert hasattr(Admin, "adminname")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminname" in klass.__dict__:
            descriptor = klass.__dict__["adminname"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_mobile():
    assert hasattr(Admin, "mobile")
    descriptor = None
    for klass in Admin.__mro__:
        if "mobile" in klass.__dict__:
            descriptor = klass.__dict__["mobile"]
            break
    assert isinstance(descriptor, property)



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "session" in params, "Missing parameter 'session'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_system_has_session():
    assert hasattr(System, "session")
    descriptor = None
    for klass in System.__mro__:
        if "session" in klass.__dict__:
            descriptor = klass.__dict__["session"]
            break
    assert isinstance(descriptor, property)

def test_system_has_name():
    assert hasattr(System, "name")
    descriptor = None
    for klass in System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_system_has_id():
    assert hasattr(System, "id")
    descriptor = None
    for klass in System.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "ticketid" in params, "Missing parameter 'ticketid'"
    assert "price" in params, "Missing parameter 'price'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "source" in params, "Missing parameter 'source'"
    assert "passengername" in params, "Missing parameter 'passengername'"
    assert "flightname" in params, "Missing parameter 'flightname'"

def test_ticket_has_ticketid():
    assert hasattr(Ticket, "ticketid")
    descriptor = None
    for klass in Ticket.__mro__:
        if "ticketid" in klass.__dict__:
            descriptor = klass.__dict__["ticketid"]
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

def test_ticket_has_destination():
    assert hasattr(Ticket, "destination")
    descriptor = None
    for klass in Ticket.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_source():
    assert hasattr(Ticket, "source")
    descriptor = None
    for klass in Ticket.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_passengername():
    assert hasattr(Ticket, "passengername")
    descriptor = None
    for klass in Ticket.__mro__:
        if "passengername" in klass.__dict__:
            descriptor = klass.__dict__["passengername"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_flightname():
    assert hasattr(Ticket, "flightname")
    descriptor = None
    for klass in Ticket.__mro__:
        if "flightname" in klass.__dict__:
            descriptor = klass.__dict__["flightname"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "attribute" in params, "Missing parameter 'attribute'"

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

def test_user_has_attribute():
    assert hasattr(User, "attribute")
    descriptor = None
    for klass in User.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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
Timinglist_strategy = st.builds(
    Timinglist,
    time=
        safe_text,
    source=
        safe_text,
    destination=
        safe_text,
    flightname=
        safe_text
)
Flightlist_strategy = st.builds(
    Flightlist,
    name=
        safe_text,
    id=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    password=
        safe_text,
    gender=
        safe_text,
    type=
        safe_text,
    adminname=
        safe_text,
    mobile=
        st.integers()
)
System_strategy = st.builds(
    System,
    session=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    ticketid=
        safe_text,
    price=
        st.integers(),
    destination=
        safe_text,
    source=
        safe_text,
    passengername=
        safe_text,
    flightname=
        safe_text
)
User_strategy = st.builds(
    User,
    password=
        safe_text,
    username=
        safe_text,
    attribute=
        safe_text
)

@given(instance=Timinglist_strategy)
@settings(max_examples=50)
def test_timinglist_instantiation(instance):
    assert isinstance(instance, Timinglist)



@given(instance=Timinglist_strategy)
def test_timinglist_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Timinglist_strategy)
def test_timinglist_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=Timinglist_strategy)
def test_timinglist_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Timinglist_strategy)
def test_timinglist_flightname_setter(instance):
    original = instance.flightname
    instance.flightname = original
    assert instance.flightname == original

@given(instance=Flightlist_strategy)
@settings(max_examples=50)
def test_flightlist_instantiation(instance):
    assert isinstance(instance, Flightlist)



@given(instance=Flightlist_strategy)
def test_flightlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Flightlist_strategy)
def test_flightlist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Admin_strategy)
def test_admin_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Admin_strategy)
def test_admin_adminname_setter(instance):
    original = instance.adminname
    instance.adminname = original
    assert instance.adminname == original



@given(instance=Admin_strategy)
def test_admin_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)



@given(instance=System_strategy)
def test_system_session_setter(instance):
    original = instance.session
    instance.session = original
    assert instance.session == original



@given(instance=System_strategy)
def test_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=System_strategy)
def test_system_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_ticketid_setter(instance):
    original = instance.ticketid
    instance.ticketid = original
    assert instance.ticketid == original



@given(instance=Ticket_strategy)
def test_ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Ticket_strategy)
def test_ticket_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Ticket_strategy)
def test_ticket_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=Ticket_strategy)
def test_ticket_passengername_setter(instance):
    original = instance.passengername
    instance.passengername = original
    assert instance.passengername == original



@given(instance=Ticket_strategy)
def test_ticket_flightname_setter(instance):
    original = instance.flightname
    instance.flightname = original
    assert instance.flightname == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



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



@given(instance=User_strategy)
def test_user_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original
