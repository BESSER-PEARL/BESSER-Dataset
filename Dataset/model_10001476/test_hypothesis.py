import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin,
    Commercial_Events,
    Birthday_Parties,
    Weddings,
    Refreshment,
    Event,
    Payment,
    Volunteer,
    Eventhead,
    Client,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_admin_has_username():
    assert hasattr(Admin, "username")
    descriptor = None
    for klass in Admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_commercial_events_is_not_abstract():
    assert not inspect.isabstract(Commercial_Events)


def test_commercial_events_constructor_exists():
    assert callable(Commercial_Events.__init__)


def test_commercial_events_constructor_args():
    sig = inspect.signature(Commercial_Events.__init__)
    params = list(sig.parameters.keys())



def test_birthday_parties_is_not_abstract():
    assert not inspect.isabstract(Birthday_Parties)


def test_birthday_parties_constructor_exists():
    assert callable(Birthday_Parties.__init__)


def test_birthday_parties_constructor_args():
    sig = inspect.signature(Birthday_Parties.__init__)
    params = list(sig.parameters.keys())



def test_weddings_is_not_abstract():
    assert not inspect.isabstract(Weddings)


def test_weddings_constructor_exists():
    assert callable(Weddings.__init__)


def test_weddings_constructor_args():
    sig = inspect.signature(Weddings.__init__)
    params = list(sig.parameters.keys())



def test_refreshment_is_not_abstract():
    assert not inspect.isabstract(Refreshment)


def test_refreshment_constructor_exists():
    assert callable(Refreshment.__init__)


def test_refreshment_constructor_args():
    sig = inspect.signature(Refreshment.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "eventid" in params, "Missing parameter 'eventid'"
    assert "eventype" in params, "Missing parameter 'eventype'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "date" in params, "Missing parameter 'date'"
    assert "eventname" in params, "Missing parameter 'eventname'"
    assert "eventhead" in params, "Missing parameter 'eventhead'"

def test_event_has_eventid():
    assert hasattr(Event, "eventid")
    descriptor = None
    for klass in Event.__mro__:
        if "eventid" in klass.__dict__:
            descriptor = klass.__dict__["eventid"]
            break
    assert isinstance(descriptor, property)

def test_event_has_eventype():
    assert hasattr(Event, "eventype")
    descriptor = None
    for klass in Event.__mro__:
        if "eventype" in klass.__dict__:
            descriptor = klass.__dict__["eventype"]
            break
    assert isinstance(descriptor, property)

def test_event_has_amount():
    assert hasattr(Event, "amount")
    descriptor = None
    for klass in Event.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_event_has_date():
    assert hasattr(Event, "date")
    descriptor = None
    for klass in Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_event_has_eventname():
    assert hasattr(Event, "eventname")
    descriptor = None
    for klass in Event.__mro__:
        if "eventname" in klass.__dict__:
            descriptor = klass.__dict__["eventname"]
            break
    assert isinstance(descriptor, property)

def test_event_has_eventhead():
    assert hasattr(Event, "eventhead")
    descriptor = None
    for klass in Event.__mro__:
        if "eventhead" in klass.__dict__:
            descriptor = klass.__dict__["eventhead"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "amout" in params, "Missing parameter 'amout'"
    assert "status" in params, "Missing parameter 'status'"
    assert "paytype" in params, "Missing parameter 'paytype'"

def test_payment_has_amout():
    assert hasattr(Payment, "amout")
    descriptor = None
    for klass in Payment.__mro__:
        if "amout" in klass.__dict__:
            descriptor = klass.__dict__["amout"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_status():
    assert hasattr(Payment, "status")
    descriptor = None
    for klass in Payment.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paytype():
    assert hasattr(Payment, "paytype")
    descriptor = None
    for klass in Payment.__mro__:
        if "paytype" in klass.__dict__:
            descriptor = klass.__dict__["paytype"]
            break
    assert isinstance(descriptor, property)



def test_volunteer_is_not_abstract():
    assert not inspect.isabstract(Volunteer)


def test_volunteer_constructor_exists():
    assert callable(Volunteer.__init__)


def test_volunteer_constructor_args():
    sig = inspect.signature(Volunteer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_volunteer_has_id():
    assert hasattr(Volunteer, "id")
    descriptor = None
    for klass in Volunteer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_eventhead_is_not_abstract():
    assert not inspect.isabstract(Eventhead)


def test_eventhead_constructor_exists():
    assert callable(Eventhead.__init__)


def test_eventhead_constructor_args():
    sig = inspect.signature(Eventhead.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_eventhead_has_id():
    assert hasattr(Eventhead, "id")
    descriptor = None
    for klass in Eventhead.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_client_has_id():
    assert hasattr(Client, "id")
    descriptor = None
    for klass in Client.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "lname" in params, "Missing parameter 'lname'"

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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

def test_user_has_fname():
    assert hasattr(User, "fname")
    descriptor = None
    for klass in User.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_lname():
    assert hasattr(User, "lname")
    descriptor = None
    for klass in User.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
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
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    password=
        safe_text
)
Commercial_Events_strategy = st.builds(
    Commercial_Events,
)
Birthday_Parties_strategy = st.builds(
    Birthday_Parties,
)
Weddings_strategy = st.builds(
    Weddings,
)
Refreshment_strategy = st.builds(
    Refreshment,
)
Event_strategy = st.builds(
    Event,
    eventid=
        st.integers(),
    eventype=
        safe_text,
    amount=
        st.integers(),
    date=
        st.integers(),
    eventname=
        safe_text,
    eventhead=
        st.none()
)
Payment_strategy = st.builds(
    Payment,
    amout=
        st.integers(),
    status=
        safe_text,
    paytype=
        safe_text
)
Volunteer_strategy = st.builds(
    Volunteer,
    id=
        st.integers()
)
Eventhead_strategy = st.builds(
    Eventhead,
    id=
        st.integers()
)
Client_strategy = st.builds(
    Client,
    id=
        st.integers()
)
User_strategy = st.builds(
    User,
    username=
        safe_text,
    password=
        safe_text,
    fname=
        safe_text,
    lname=
        safe_text
)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Commercial_Events_strategy)
@settings(max_examples=50)
def test_commercial_events_instantiation(instance):
    assert isinstance(instance, Commercial_Events)

@given(instance=Birthday_Parties_strategy)
@settings(max_examples=50)
def test_birthday_parties_instantiation(instance):
    assert isinstance(instance, Birthday_Parties)

@given(instance=Weddings_strategy)
@settings(max_examples=50)
def test_weddings_instantiation(instance):
    assert isinstance(instance, Weddings)

@given(instance=Refreshment_strategy)
@settings(max_examples=50)
def test_refreshment_instantiation(instance):
    assert isinstance(instance, Refreshment)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_eventid_setter(instance):
    original = instance.eventid
    instance.eventid = original
    assert instance.eventid == original



@given(instance=Event_strategy)
def test_event_eventype_setter(instance):
    original = instance.eventype
    instance.eventype = original
    assert instance.eventype == original



@given(instance=Event_strategy)
def test_event_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Event_strategy)
def test_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Event_strategy)
def test_event_eventname_setter(instance):
    original = instance.eventname
    instance.eventname = original
    assert instance.eventname == original



@given(instance=Event_strategy)
def test_event_eventhead_setter(instance):
    original = instance.eventhead
    instance.eventhead = original
    assert instance.eventhead == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_amout_setter(instance):
    original = instance.amout
    instance.amout = original
    assert instance.amout == original



@given(instance=Payment_strategy)
def test_payment_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Payment_strategy)
def test_payment_paytype_setter(instance):
    original = instance.paytype
    instance.paytype = original
    assert instance.paytype == original

@given(instance=Volunteer_strategy)
@settings(max_examples=50)
def test_volunteer_instantiation(instance):
    assert isinstance(instance, Volunteer)



@given(instance=Volunteer_strategy)
def test_volunteer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Eventhead_strategy)
@settings(max_examples=50)
def test_eventhead_instantiation(instance):
    assert isinstance(instance, Eventhead)



@given(instance=Eventhead_strategy)
def test_eventhead_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)



@given(instance=Client_strategy)
def test_client_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=User_strategy)
def test_user_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original
