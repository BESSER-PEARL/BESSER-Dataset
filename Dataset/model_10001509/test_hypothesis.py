import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    floor_s_buttons,
    elevator_s_buttons,
    button,
    door,
    elevator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_floor_s_buttons_is_not_abstract():
    assert not inspect.isabstract(floor_s_buttons)


def test_floor_s_buttons_constructor_exists():
    assert callable(floor_s_buttons.__init__)


def test_floor_s_buttons_constructor_args():
    sig = inspect.signature(floor_s_buttons.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_floor_s_buttons_has_number():
    assert hasattr(floor_s_buttons, "number")
    descriptor = None
    for klass in floor_s_buttons.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_elevator_s_buttons_is_not_abstract():
    assert not inspect.isabstract(elevator_s_buttons)


def test_elevator_s_buttons_constructor_exists():
    assert callable(elevator_s_buttons.__init__)


def test_elevator_s_buttons_constructor_args():
    sig = inspect.signature(elevator_s_buttons.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_elevator_s_buttons_has_number():
    assert hasattr(elevator_s_buttons, "number")
    descriptor = None
    for klass in elevator_s_buttons.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_button_is_not_abstract():
    assert not inspect.isabstract(button)


def test_button_constructor_exists():
    assert callable(button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(button.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_button_has_number():
    assert hasattr(button, "number")
    descriptor = None
    for klass in button.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_door_is_not_abstract():
    assert not inspect.isabstract(door)


def test_door_constructor_exists():
    assert callable(door.__init__)


def test_door_constructor_args():
    sig = inspect.signature(door.__init__)
    params = list(sig.parameters.keys())
    assert "close" in params, "Missing parameter 'close'"

def test_door_has_close():
    assert hasattr(door, "close")
    descriptor = None
    for klass in door.__mro__:
        if "close" in klass.__dict__:
            descriptor = klass.__dict__["close"]
            break
    assert isinstance(descriptor, property)



def test_elevator_is_not_abstract():
    assert not inspect.isabstract(elevator)


def test_elevator_constructor_exists():
    assert callable(elevator.__init__)


def test_elevator_constructor_args():
    sig = inspect.signature(elevator.__init__)
    params = list(sig.parameters.keys())
    assert "floor" in params, "Missing parameter 'floor'"

def test_elevator_has_floor():
    assert hasattr(elevator, "floor")
    descriptor = None
    for klass in elevator.__mro__:
        if "floor" in klass.__dict__:
            descriptor = klass.__dict__["floor"]
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
floor_s_buttons_strategy = st.builds(
    floor_s_buttons,
    number=
        st.booleans()
)
elevator_s_buttons_strategy = st.builds(
    elevator_s_buttons,
    number=
        st.integers()
)
button_strategy = st.builds(
    button,
    number=
        st.integers()
)
door_strategy = st.builds(
    door,
    close=
        st.booleans()
)
elevator_strategy = st.builds(
    elevator,
    floor=
        st.integers()
)

@given(instance=floor_s_buttons_strategy)
@settings(max_examples=50)
def test_floor_s_buttons_instantiation(instance):
    assert isinstance(instance, floor_s_buttons)



@given(instance=floor_s_buttons_strategy)
def test_floor_s_buttons_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=elevator_s_buttons_strategy)
@settings(max_examples=50)
def test_elevator_s_buttons_instantiation(instance):
    assert isinstance(instance, elevator_s_buttons)



@given(instance=elevator_s_buttons_strategy)
def test_elevator_s_buttons_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, button)



@given(instance=button_strategy)
def test_button_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=door_strategy)
@settings(max_examples=50)
def test_door_instantiation(instance):
    assert isinstance(instance, door)



@given(instance=door_strategy)
def test_door_close_setter(instance):
    original = instance.close
    instance.close = original
    assert instance.close == original

@given(instance=elevator_strategy)
@settings(max_examples=50)
def test_elevator_instantiation(instance):
    assert isinstance(instance, elevator)



@given(instance=elevator_strategy)
def test_elevator_floor_setter(instance):
    original = instance.floor
    instance.floor = original
    assert instance.floor == original
