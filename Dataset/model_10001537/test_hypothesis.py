import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ticket,
    Passenger,
    Luggage,
    CheckStaff,
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
    assert "no" in params, "Missing parameter 'no'"

def test_ticket_has_no():
    assert hasattr(Ticket, "no")
    descriptor = None
    for klass in Ticket.__mro__:
        if "no" in klass.__dict__:
            descriptor = klass.__dict__["no"]
            break
    assert isinstance(descriptor, property)



def test_passenger_is_not_abstract():
    assert not inspect.isabstract(Passenger)


def test_passenger_constructor_exists():
    assert callable(Passenger.__init__)


def test_passenger_constructor_args():
    sig = inspect.signature(Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_passenger_has_name():
    assert hasattr(Passenger, "name")
    descriptor = None
    for klass in Passenger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luggage_is_not_abstract():
    assert not inspect.isabstract(Luggage)


def test_luggage_constructor_exists():
    assert callable(Luggage.__init__)


def test_luggage_constructor_args():
    sig = inspect.signature(Luggage.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_luggage_has_weight():
    assert hasattr(Luggage, "weight")
    descriptor = None
    for klass in Luggage.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_checkstaff_is_not_abstract():
    assert not inspect.isabstract(CheckStaff)


def test_checkstaff_constructor_exists():
    assert callable(CheckStaff.__init__)


def test_checkstaff_constructor_args():
    sig = inspect.signature(CheckStaff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_checkstaff_has_name():
    assert hasattr(CheckStaff, "name")
    descriptor = None
    for klass in CheckStaff.__mro__:
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
Ticket_strategy = st.builds(
    Ticket,
    no=
        st.integers()
)
Passenger_strategy = st.builds(
    Passenger,
    name=
        safe_text
)
Luggage_strategy = st.builds(
    Luggage,
    weight=
        st.integers()
)
CheckStaff_strategy = st.builds(
    CheckStaff,
    name=
        safe_text
)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_no_setter(instance):
    original = instance.no
    instance.no = original
    assert instance.no == original

@given(instance=Passenger_strategy)
@settings(max_examples=50)
def test_passenger_instantiation(instance):
    assert isinstance(instance, Passenger)



@given(instance=Passenger_strategy)
def test_passenger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Luggage_strategy)
@settings(max_examples=50)
def test_luggage_instantiation(instance):
    assert isinstance(instance, Luggage)



@given(instance=Luggage_strategy)
def test_luggage_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=CheckStaff_strategy)
@settings(max_examples=50)
def test_checkstaff_instantiation(instance):
    assert isinstance(instance, CheckStaff)



@given(instance=CheckStaff_strategy)
def test_checkstaff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
