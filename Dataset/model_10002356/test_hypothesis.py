import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    credit_card,
    cash,
    flights,
    admin,
    ticket,
    payement,
    customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_credit_card_is_not_abstract():
    assert not inspect.isabstract(credit_card)


def test_credit_card_constructor_exists():
    assert callable(credit_card.__init__)


def test_credit_card_constructor_args():
    sig = inspect.signature(credit_card.__init__)
    params = list(sig.parameters.keys())



def test_cash_is_not_abstract():
    assert not inspect.isabstract(cash)


def test_cash_constructor_exists():
    assert callable(cash.__init__)


def test_cash_constructor_args():
    sig = inspect.signature(cash.__init__)
    params = list(sig.parameters.keys())



def test_flights_is_not_abstract():
    assert not inspect.isabstract(flights)


def test_flights_constructor_exists():
    assert callable(flights.__init__)


def test_flights_constructor_args():
    sig = inspect.signature(flights.__init__)
    params = list(sig.parameters.keys())
    assert "dest" in params, "Missing parameter 'dest'"
    assert "depart" in params, "Missing parameter 'depart'"
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"

def test_flights_has_dest():
    assert hasattr(flights, "dest")
    descriptor = None
    for klass in flights.__mro__:
        if "dest" in klass.__dict__:
            descriptor = klass.__dict__["dest"]
            break
    assert isinstance(descriptor, property)

def test_flights_has_depart():
    assert hasattr(flights, "depart")
    descriptor = None
    for klass in flights.__mro__:
        if "depart" in klass.__dict__:
            descriptor = klass.__dict__["depart"]
            break
    assert isinstance(descriptor, property)

def test_flights_has_number():
    assert hasattr(flights, "number")
    descriptor = None
    for klass in flights.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_flights_has_name():
    assert hasattr(flights, "name")
    descriptor = None
    for klass in flights.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_flights_has_time():
    assert hasattr(flights, "time")
    descriptor = None
    for klass in flights.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_admin_constructor_exists():
    assert callable(admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())
    assert "pwd" in params, "Missing parameter 'pwd'"
    assert "name_of_flight" in params, "Missing parameter 'name_of_flight'"
    assert "seats" in params, "Missing parameter 'seats'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "username" in params, "Missing parameter 'username'"
    assert "type" in params, "Missing parameter 'type'"

def test_admin_has_pwd():
    assert hasattr(admin, "pwd")
    descriptor = None
    for klass in admin.__mro__:
        if "pwd" in klass.__dict__:
            descriptor = klass.__dict__["pwd"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_name_of_flight():
    assert hasattr(admin, "name_of_flight")
    descriptor = None
    for klass in admin.__mro__:
        if "name_of_flight" in klass.__dict__:
            descriptor = klass.__dict__["name_of_flight"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_seats():
    assert hasattr(admin, "seats")
    descriptor = None
    for klass in admin.__mro__:
        if "seats" in klass.__dict__:
            descriptor = klass.__dict__["seats"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_cost():
    assert hasattr(admin, "cost")
    descriptor = None
    for klass in admin.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_username():
    assert hasattr(admin, "username")
    descriptor = None
    for klass in admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_type():
    assert hasattr(admin, "type")
    descriptor = None
    for klass in admin.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(ticket)


def test_ticket_constructor_exists():
    assert callable(ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(ticket.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "custid" in params, "Missing parameter 'custid'"
    assert "tiketno_" in params, "Missing parameter 'tiketno_'"
    assert "dest" in params, "Missing parameter 'dest'"

def test_ticket_has_source():
    assert hasattr(ticket, "source")
    descriptor = None
    for klass in ticket.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_attribute():
    assert hasattr(ticket, "attribute")
    descriptor = None
    for klass in ticket.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_custid():
    assert hasattr(ticket, "custid")
    descriptor = None
    for klass in ticket.__mro__:
        if "custid" in klass.__dict__:
            descriptor = klass.__dict__["custid"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_tiketno_():
    assert hasattr(ticket, "tiketno_")
    descriptor = None
    for klass in ticket.__mro__:
        if "tiketno_" in klass.__dict__:
            descriptor = klass.__dict__["tiketno_"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_dest():
    assert hasattr(ticket, "dest")
    descriptor = None
    for klass in ticket.__mro__:
        if "dest" in klass.__dict__:
            descriptor = klass.__dict__["dest"]
            break
    assert isinstance(descriptor, property)



def test_payement_is_not_abstract():
    assert not inspect.isabstract(payement)


def test_payement_constructor_exists():
    assert callable(payement.__init__)


def test_payement_constructor_args():
    sig = inspect.signature(payement.__init__)
    params = list(sig.parameters.keys())
    assert "customer_info" in params, "Missing parameter 'customer_info'"
    assert "pay_amt" in params, "Missing parameter 'pay_amt'"
    assert "transc_id" in params, "Missing parameter 'transc_id'"
    assert "pay_date" in params, "Missing parameter 'pay_date'"
    assert "paymethod" in params, "Missing parameter 'paymethod'"

def test_payement_has_customer_info():
    assert hasattr(payement, "customer_info")
    descriptor = None
    for klass in payement.__mro__:
        if "customer_info" in klass.__dict__:
            descriptor = klass.__dict__["customer_info"]
            break
    assert isinstance(descriptor, property)

def test_payement_has_pay_amt():
    assert hasattr(payement, "pay_amt")
    descriptor = None
    for klass in payement.__mro__:
        if "pay_amt" in klass.__dict__:
            descriptor = klass.__dict__["pay_amt"]
            break
    assert isinstance(descriptor, property)

def test_payement_has_transc_id():
    assert hasattr(payement, "transc_id")
    descriptor = None
    for klass in payement.__mro__:
        if "transc_id" in klass.__dict__:
            descriptor = klass.__dict__["transc_id"]
            break
    assert isinstance(descriptor, property)

def test_payement_has_pay_date():
    assert hasattr(payement, "pay_date")
    descriptor = None
    for klass in payement.__mro__:
        if "pay_date" in klass.__dict__:
            descriptor = klass.__dict__["pay_date"]
            break
    assert isinstance(descriptor, property)

def test_payement_has_paymethod():
    assert hasattr(payement, "paymethod")
    descriptor = None
    for klass in payement.__mro__:
        if "paymethod" in klass.__dict__:
            descriptor = klass.__dict__["paymethod"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_source():
    assert hasattr(customer, "source")
    descriptor = None
    for klass in customer.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_age():
    assert hasattr(customer, "age")
    descriptor = None
    for klass in customer.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(customer, "address")
    descriptor = None
    for klass in customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(customer, "name")
    descriptor = None
    for klass in customer.__mro__:
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
credit_card_strategy = st.builds(
    credit_card,
)
cash_strategy = st.builds(
    cash,
)
flights_strategy = st.builds(
    flights,
    dest=
        safe_text,
    depart=
        safe_text,
    number=
        st.integers(),
    name=
        safe_text,
    time=
        st.integers()
)
admin_strategy = st.builds(
    admin,
    pwd=
        safe_text,
    name_of_flight=
        safe_text,
    seats=
        st.integers(),
    cost=
        st.integers(),
    username=
        safe_text,
    type=
        safe_text
)
ticket_strategy = st.builds(
    ticket,
    source=
        safe_text,
    attribute=
        safe_text,
    custid=
        st.integers(),
    tiketno_=
        st.integers(),
    dest=
        safe_text
)
payement_strategy = st.builds(
    payement,
    customer_info=
        safe_text,
    pay_amt=
        st.integers(),
    transc_id=
        st.integers(),
    pay_date=
        st.integers(),
    paymethod=
        safe_text
)
customer_strategy = st.builds(
    customer,
    source=
        safe_text,
    age=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)

@given(instance=credit_card_strategy)
@settings(max_examples=50)
def test_credit_card_instantiation(instance):
    assert isinstance(instance, credit_card)

@given(instance=cash_strategy)
@settings(max_examples=50)
def test_cash_instantiation(instance):
    assert isinstance(instance, cash)

@given(instance=flights_strategy)
@settings(max_examples=50)
def test_flights_instantiation(instance):
    assert isinstance(instance, flights)



@given(instance=flights_strategy)
def test_flights_dest_setter(instance):
    original = instance.dest
    instance.dest = original
    assert instance.dest == original



@given(instance=flights_strategy)
def test_flights_depart_setter(instance):
    original = instance.depart
    instance.depart = original
    assert instance.depart == original



@given(instance=flights_strategy)
def test_flights_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=flights_strategy)
def test_flights_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=flights_strategy)
def test_flights_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)



@given(instance=admin_strategy)
def test_admin_pwd_setter(instance):
    original = instance.pwd
    instance.pwd = original
    assert instance.pwd == original



@given(instance=admin_strategy)
def test_admin_name_of_flight_setter(instance):
    original = instance.name_of_flight
    instance.name_of_flight = original
    assert instance.name_of_flight == original



@given(instance=admin_strategy)
def test_admin_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original



@given(instance=admin_strategy)
def test_admin_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=admin_strategy)
def test_admin_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, ticket)



@given(instance=ticket_strategy)
def test_ticket_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=ticket_strategy)
def test_ticket_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ticket_strategy)
def test_ticket_custid_setter(instance):
    original = instance.custid
    instance.custid = original
    assert instance.custid == original



@given(instance=ticket_strategy)
def test_ticket_tiketno__setter(instance):
    original = instance.tiketno_
    instance.tiketno_ = original
    assert instance.tiketno_ == original



@given(instance=ticket_strategy)
def test_ticket_dest_setter(instance):
    original = instance.dest
    instance.dest = original
    assert instance.dest == original

@given(instance=payement_strategy)
@settings(max_examples=50)
def test_payement_instantiation(instance):
    assert isinstance(instance, payement)



@given(instance=payement_strategy)
def test_payement_customer_info_setter(instance):
    original = instance.customer_info
    instance.customer_info = original
    assert instance.customer_info == original



@given(instance=payement_strategy)
def test_payement_pay_amt_setter(instance):
    original = instance.pay_amt
    instance.pay_amt = original
    assert instance.pay_amt == original



@given(instance=payement_strategy)
def test_payement_transc_id_setter(instance):
    original = instance.transc_id
    instance.transc_id = original
    assert instance.transc_id == original



@given(instance=payement_strategy)
def test_payement_pay_date_setter(instance):
    original = instance.pay_date
    instance.pay_date = original
    assert instance.pay_date == original



@given(instance=payement_strategy)
def test_payement_paymethod_setter(instance):
    original = instance.paymethod
    instance.paymethod = original
    assert instance.paymethod == original

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)



@given(instance=customer_strategy)
def test_customer_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=customer_strategy)
def test_customer_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
