import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ElevatorControl,
    ElevatorComponent,
    Button,
    Elevator,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elevatorcontrol_is_not_abstract():
    assert not inspect.isabstract(ElevatorControl)


def test_elevatorcontrol_constructor_exists():
    assert callable(ElevatorControl.__init__)


def test_elevatorcontrol_constructor_args():
    sig = inspect.signature(ElevatorControl.__init__)
    params = list(sig.parameters.keys())



def test_elevatorcomponent_is_not_abstract():
    assert not inspect.isabstract(ElevatorComponent)


def test_elevatorcomponent_constructor_exists():
    assert callable(ElevatorComponent.__init__)


def test_elevatorcomponent_constructor_args():
    sig = inspect.signature(ElevatorComponent.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_elevatorcomponent_has_direction():
    assert hasattr(ElevatorComponent, "direction")
    descriptor = None
    for klass in ElevatorComponent.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_button_constructor_exists():
    assert callable(Button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())
    assert "floor" in params, "Missing parameter 'floor'"
    assert "pressed" in params, "Missing parameter 'pressed'"

def test_button_has_floor():
    assert hasattr(Button, "floor")
    descriptor = None
    for klass in Button.__mro__:
        if "floor" in klass.__dict__:
            descriptor = klass.__dict__["floor"]
            break
    assert isinstance(descriptor, property)

def test_button_has_pressed():
    assert hasattr(Button, "pressed")
    descriptor = None
    for klass in Button.__mro__:
        if "pressed" in klass.__dict__:
            descriptor = klass.__dict__["pressed"]
            break
    assert isinstance(descriptor, property)



def test_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "destinationFloor" in params, "Missing parameter 'destinationFloor'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"

def test_elevator_has_number():
    assert hasattr(Elevator, "number")
    descriptor = None
    for klass in Elevator.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_destinationFloor():
    assert hasattr(Elevator, "destinationFloor")
    descriptor = None
    for klass in Elevator.__mro__:
        if "destinationFloor" in klass.__dict__:
            descriptor = klass.__dict__["destinationFloor"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_currentFloor():
    assert hasattr(Elevator, "currentFloor")
    descriptor = None
    for klass in Elevator.__mro__:
        if "currentFloor" in klass.__dict__:
            descriptor = klass.__dict__["currentFloor"]
            break
    assert isinstance(descriptor, property)

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
ElevatorControl_strategy = st.builds(
    ElevatorControl,
)
ElevatorComponent_strategy = st.builds(
    ElevatorComponent,
    direction=
        st.none()
)
Button_strategy = st.builds(
    Button,
    floor=
        st.integers(),
    pressed=
        st.booleans()
)
Elevator_strategy = st.builds(
    Elevator,
    number=
        st.integers(),
    destinationFloor=
        st.integers(),
    currentFloor=
        st.integers()
)

@given(instance=ElevatorControl_strategy)
@settings(max_examples=50)
def test_elevatorcontrol_instantiation(instance):
    assert isinstance(instance, ElevatorControl)

@given(instance=ElevatorComponent_strategy)
@settings(max_examples=50)
def test_elevatorcomponent_instantiation(instance):
    assert isinstance(instance, ElevatorComponent)



@given(instance=ElevatorComponent_strategy)
def test_elevatorcomponent_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, Button)



@given(instance=Button_strategy)
def test_button_floor_setter(instance):
    original = instance.floor
    instance.floor = original
    assert instance.floor == original



@given(instance=Button_strategy)
def test_button_pressed_setter(instance):
    original = instance.pressed
    instance.pressed = original
    assert instance.pressed == original

@given(instance=Elevator_strategy)
@settings(max_examples=50)
def test_elevator_instantiation(instance):
    assert isinstance(instance, Elevator)



@given(instance=Elevator_strategy)
def test_elevator_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Elevator_strategy)
def test_elevator_destinationFloor_setter(instance):
    original = instance.destinationFloor
    instance.destinationFloor = original
    assert instance.destinationFloor == original



@given(instance=Elevator_strategy)
def test_elevator_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original
