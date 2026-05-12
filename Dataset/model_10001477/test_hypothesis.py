import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ticket,
    ValleyParking,
    spot,
    XL,
    large,
    medium,
    small,
    Vehicle_Interface,
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
    assert "id" in params, "Missing parameter 'id'"

def test_ticket_has_id():
    assert hasattr(Ticket, "id")
    descriptor = None
    for klass in Ticket.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_valleyparking_is_not_abstract():
    assert not inspect.isabstract(ValleyParking)


def test_valleyparking_constructor_exists():
    assert callable(ValleyParking.__init__)


def test_valleyparking_constructor_args():
    sig = inspect.signature(ValleyParking.__init__)
    params = list(sig.parameters.keys())



def test_spot_is_not_abstract():
    assert not inspect.isabstract(spot)


def test_spot_constructor_exists():
    assert callable(spot.__init__)


def test_spot_constructor_args():
    sig = inspect.signature(spot.__init__)
    params = list(sig.parameters.keys())
    assert "parkedVehicle" in params, "Missing parameter 'parkedVehicle'"
    assert "id" in params, "Missing parameter 'id'"
    assert "size" in params, "Missing parameter 'size'"

def test_spot_has_parkedVehicle():
    assert hasattr(spot, "parkedVehicle")
    descriptor = None
    for klass in spot.__mro__:
        if "parkedVehicle" in klass.__dict__:
            descriptor = klass.__dict__["parkedVehicle"]
            break
    assert isinstance(descriptor, property)

def test_spot_has_id():
    assert hasattr(spot, "id")
    descriptor = None
    for klass in spot.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_spot_has_size():
    assert hasattr(spot, "size")
    descriptor = None
    for klass in spot.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_xl_is_not_abstract():
    assert not inspect.isabstract(XL)


def test_xl_constructor_exists():
    assert callable(XL.__init__)


def test_xl_constructor_args():
    sig = inspect.signature(XL.__init__)
    params = list(sig.parameters.keys())



def test_large_is_not_abstract():
    assert not inspect.isabstract(large)


def test_large_constructor_exists():
    assert callable(large.__init__)


def test_large_constructor_args():
    sig = inspect.signature(large.__init__)
    params = list(sig.parameters.keys())



def test_medium_is_not_abstract():
    assert not inspect.isabstract(medium)


def test_medium_constructor_exists():
    assert callable(medium.__init__)


def test_medium_constructor_args():
    sig = inspect.signature(medium.__init__)
    params = list(sig.parameters.keys())



def test_small_is_not_abstract():
    assert not inspect.isabstract(small)


def test_small_constructor_exists():
    assert callable(small.__init__)


def test_small_constructor_args():
    sig = inspect.signature(small.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_interface_is_not_abstract():
    assert not inspect.isabstract(Vehicle_Interface)


def test_vehicle_interface_constructor_exists():
    assert callable(Vehicle_Interface.__init__)


def test_vehicle_interface_constructor_args():
    sig = inspect.signature(Vehicle_Interface.__init__)
    params = list(sig.parameters.keys())


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
    id=
        safe_text
)
ValleyParking_strategy = st.builds(
    ValleyParking,
)
spot_strategy = st.builds(
    spot,
    parkedVehicle=
        st.none(),
    id=
        safe_text,
    size=
        st.integers()
)
XL_strategy = st.builds(
    XL,
)
large_strategy = st.builds(
    large,
)
medium_strategy = st.builds(
    medium,
)
small_strategy = st.builds(
    small,
)
Vehicle_Interface_strategy = st.builds(
    Vehicle_Interface,
)

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ValleyParking_strategy)
@settings(max_examples=50)
def test_valleyparking_instantiation(instance):
    assert isinstance(instance, ValleyParking)

@given(instance=spot_strategy)
@settings(max_examples=50)
def test_spot_instantiation(instance):
    assert isinstance(instance, spot)



@given(instance=spot_strategy)
def test_spot_parkedVehicle_setter(instance):
    original = instance.parkedVehicle
    instance.parkedVehicle = original
    assert instance.parkedVehicle == original



@given(instance=spot_strategy)
def test_spot_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=spot_strategy)
def test_spot_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=XL_strategy)
@settings(max_examples=50)
def test_xl_instantiation(instance):
    assert isinstance(instance, XL)

@given(instance=large_strategy)
@settings(max_examples=50)
def test_large_instantiation(instance):
    assert isinstance(instance, large)

@given(instance=medium_strategy)
@settings(max_examples=50)
def test_medium_instantiation(instance):
    assert isinstance(instance, medium)

@given(instance=small_strategy)
@settings(max_examples=50)
def test_small_instantiation(instance):
    assert isinstance(instance, small)

@given(instance=Vehicle_Interface_strategy)
@settings(max_examples=50)
def test_vehicle_interface_instantiation(instance):
    assert isinstance(instance, Vehicle_Interface)
