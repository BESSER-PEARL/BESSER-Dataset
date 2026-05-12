import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Algorithm,
    Elevator,
    Building,
    Controller,
    ElevatorBay,
    UpDownButton,
    FloorButton,
    Button,
    object,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_algorithm_is_not_abstract():
    assert not inspect.isabstract(Algorithm)


def test_algorithm_constructor_exists():
    assert callable(Algorithm.__init__)


def test_algorithm_constructor_args():
    sig = inspect.signature(Algorithm.__init__)
    params = list(sig.parameters.keys())
    assert "TimeBetweenFloors" in params, "Missing parameter 'TimeBetweenFloors'"

def test_algorithm_has_TimeBetweenFloors():
    assert hasattr(Algorithm, "TimeBetweenFloors")
    descriptor = None
    for klass in Algorithm.__mro__:
        if "TimeBetweenFloors" in klass.__dict__:
            descriptor = klass.__dict__["TimeBetweenFloors"]
            break
    assert isinstance(descriptor, property)



def test_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "CurrentFloor" in params, "Missing parameter 'CurrentFloor'"
    assert "ElevatorBayNumber" in params, "Missing parameter 'ElevatorBayNumber'"
    assert "CurrentMovement" in params, "Missing parameter 'CurrentMovement'"
    assert "FloorButtons" in params, "Missing parameter 'FloorButtons'"
    assert "ElevatorNumber" in params, "Missing parameter 'ElevatorNumber'"
    assert "ArrivedAtFloor" in params, "Missing parameter 'ArrivedAtFloor'"

def test_elevator_has_CurrentFloor():
    assert hasattr(Elevator, "CurrentFloor")
    descriptor = None
    for klass in Elevator.__mro__:
        if "CurrentFloor" in klass.__dict__:
            descriptor = klass.__dict__["CurrentFloor"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_ElevatorBayNumber():
    assert hasattr(Elevator, "ElevatorBayNumber")
    descriptor = None
    for klass in Elevator.__mro__:
        if "ElevatorBayNumber" in klass.__dict__:
            descriptor = klass.__dict__["ElevatorBayNumber"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_CurrentMovement():
    assert hasattr(Elevator, "CurrentMovement")
    descriptor = None
    for klass in Elevator.__mro__:
        if "CurrentMovement" in klass.__dict__:
            descriptor = klass.__dict__["CurrentMovement"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_FloorButtons():
    assert hasattr(Elevator, "FloorButtons")
    descriptor = None
    for klass in Elevator.__mro__:
        if "FloorButtons" in klass.__dict__:
            descriptor = klass.__dict__["FloorButtons"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_ElevatorNumber():
    assert hasattr(Elevator, "ElevatorNumber")
    descriptor = None
    for klass in Elevator.__mro__:
        if "ElevatorNumber" in klass.__dict__:
            descriptor = klass.__dict__["ElevatorNumber"]
            break
    assert isinstance(descriptor, property)

def test_elevator_has_ArrivedAtFloor():
    assert hasattr(Elevator, "ArrivedAtFloor")
    descriptor = None
    for klass in Elevator.__mro__:
        if "ArrivedAtFloor" in klass.__dict__:
            descriptor = klass.__dict__["ArrivedAtFloor"]
            break
    assert isinstance(descriptor, property)



def test_building_is_not_abstract():
    assert not inspect.isabstract(Building)


def test_building_constructor_exists():
    assert callable(Building.__init__)


def test_building_constructor_args():
    sig = inspect.signature(Building.__init__)
    params = list(sig.parameters.keys())
    assert "Controller" in params, "Missing parameter 'Controller'"
    assert "ElevatorBays" in params, "Missing parameter 'ElevatorBays'"

def test_building_has_Controller():
    assert hasattr(Building, "Controller")
    descriptor = None
    for klass in Building.__mro__:
        if "Controller" in klass.__dict__:
            descriptor = klass.__dict__["Controller"]
            break
    assert isinstance(descriptor, property)

def test_building_has_ElevatorBays():
    assert hasattr(Building, "ElevatorBays")
    descriptor = None
    for klass in Building.__mro__:
        if "ElevatorBays" in klass.__dict__:
            descriptor = klass.__dict__["ElevatorBays"]
            break
    assert isinstance(descriptor, property)



def test_controller_is_not_abstract():
    assert not inspect.isabstract(Controller)


def test_controller_constructor_exists():
    assert callable(Controller.__init__)


def test_controller_constructor_args():
    sig = inspect.signature(Controller.__init__)
    params = list(sig.parameters.keys())



def test_elevatorbay_is_not_abstract():
    assert not inspect.isabstract(ElevatorBay)


def test_elevatorbay_constructor_exists():
    assert callable(ElevatorBay.__init__)


def test_elevatorbay_constructor_args():
    sig = inspect.signature(ElevatorBay.__init__)
    params = list(sig.parameters.keys())
    assert "BayNumber" in params, "Missing parameter 'BayNumber'"
    assert "UpDownButtons" in params, "Missing parameter 'UpDownButtons'"
    assert "Elevators" in params, "Missing parameter 'Elevators'"

def test_elevatorbay_has_BayNumber():
    assert hasattr(ElevatorBay, "BayNumber")
    descriptor = None
    for klass in ElevatorBay.__mro__:
        if "BayNumber" in klass.__dict__:
            descriptor = klass.__dict__["BayNumber"]
            break
    assert isinstance(descriptor, property)

def test_elevatorbay_has_UpDownButtons():
    assert hasattr(ElevatorBay, "UpDownButtons")
    descriptor = None
    for klass in ElevatorBay.__mro__:
        if "UpDownButtons" in klass.__dict__:
            descriptor = klass.__dict__["UpDownButtons"]
            break
    assert isinstance(descriptor, property)

def test_elevatorbay_has_Elevators():
    assert hasattr(ElevatorBay, "Elevators")
    descriptor = None
    for klass in ElevatorBay.__mro__:
        if "Elevators" in klass.__dict__:
            descriptor = klass.__dict__["Elevators"]
            break
    assert isinstance(descriptor, property)



def test_updownbutton_is_not_abstract():
    assert not inspect.isabstract(UpDownButton)


def test_updownbutton_constructor_exists():
    assert callable(UpDownButton.__init__)


def test_updownbutton_constructor_args():
    sig = inspect.signature(UpDownButton.__init__)
    params = list(sig.parameters.keys())
    assert "Direction" in params, "Missing parameter 'Direction'"
    assert "ElevatorBay" in params, "Missing parameter 'ElevatorBay'"

def test_updownbutton_has_Direction():
    assert hasattr(UpDownButton, "Direction")
    descriptor = None
    for klass in UpDownButton.__mro__:
        if "Direction" in klass.__dict__:
            descriptor = klass.__dict__["Direction"]
            break
    assert isinstance(descriptor, property)

def test_updownbutton_has_ElevatorBay():
    assert hasattr(UpDownButton, "ElevatorBay")
    descriptor = None
    for klass in UpDownButton.__mro__:
        if "ElevatorBay" in klass.__dict__:
            descriptor = klass.__dict__["ElevatorBay"]
            break
    assert isinstance(descriptor, property)



def test_floorbutton_is_not_abstract():
    assert not inspect.isabstract(FloorButton)


def test_floorbutton_constructor_exists():
    assert callable(FloorButton.__init__)


def test_floorbutton_constructor_args():
    sig = inspect.signature(FloorButton.__init__)
    params = list(sig.parameters.keys())
    assert "Elevator" in params, "Missing parameter 'Elevator'"

def test_floorbutton_has_Elevator():
    assert hasattr(FloorButton, "Elevator")
    descriptor = None
    for klass in FloorButton.__mro__:
        if "Elevator" in klass.__dict__:
            descriptor = klass.__dict__["Elevator"]
            break
    assert isinstance(descriptor, property)



def test_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_button_constructor_exists():
    assert callable(Button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())
    assert "Clicked" in params, "Missing parameter 'Clicked'"
    assert "FloorNumber" in params, "Missing parameter 'FloorNumber'"
    assert "IsOn" in params, "Missing parameter 'IsOn'"

def test_button_has_Clicked():
    assert hasattr(Button, "Clicked")
    descriptor = None
    for klass in Button.__mro__:
        if "Clicked" in klass.__dict__:
            descriptor = klass.__dict__["Clicked"]
            break
    assert isinstance(descriptor, property)

def test_button_has_FloorNumber():
    assert hasattr(Button, "FloorNumber")
    descriptor = None
    for klass in Button.__mro__:
        if "FloorNumber" in klass.__dict__:
            descriptor = klass.__dict__["FloorNumber"]
            break
    assert isinstance(descriptor, property)

def test_button_has_IsOn():
    assert hasattr(Button, "IsOn")
    descriptor = None
    for klass in Button.__mro__:
        if "IsOn" in klass.__dict__:
            descriptor = klass.__dict__["IsOn"]
            break
    assert isinstance(descriptor, property)



def test_object_is_not_abstract():
    assert not inspect.isabstract(object)


def test_object_constructor_exists():
    assert callable(object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(object.__init__)
    params = list(sig.parameters.keys())

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
Algorithm_strategy = st.builds(
    Algorithm,
    TimeBetweenFloors=
        safe_text
)
Elevator_strategy = st.builds(
    Elevator,
    CurrentFloor=
        st.integers(),
    ElevatorBayNumber=
        st.integers(),
    CurrentMovement=
        safe_text,
    FloorButtons=
        safe_text,
    ElevatorNumber=
        st.integers(),
    ArrivedAtFloor=
        safe_text
)
Building_strategy = st.builds(
    Building,
    Controller=
        st.none(),
    ElevatorBays=
        safe_text
)
Controller_strategy = st.builds(
    Controller,
)
ElevatorBay_strategy = st.builds(
    ElevatorBay,
    BayNumber=
        st.integers(),
    UpDownButtons=
        safe_text,
    Elevators=
        safe_text
)
UpDownButton_strategy = st.builds(
    UpDownButton,
    Direction=
        st.none(),
    ElevatorBay=
        st.none()
)
FloorButton_strategy = st.builds(
    FloorButton,
    Elevator=
        st.none()
)
Button_strategy = st.builds(
    Button,
    Clicked=
        safe_text,
    FloorNumber=
        st.integers(),
    IsOn=
        st.booleans()
)
object_strategy = st.builds(
    object,
)

@given(instance=Algorithm_strategy)
@settings(max_examples=50)
def test_algorithm_instantiation(instance):
    assert isinstance(instance, Algorithm)



@given(instance=Algorithm_strategy)
def test_algorithm_TimeBetweenFloors_setter(instance):
    original = instance.TimeBetweenFloors
    instance.TimeBetweenFloors = original
    assert instance.TimeBetweenFloors == original

@given(instance=Elevator_strategy)
@settings(max_examples=50)
def test_elevator_instantiation(instance):
    assert isinstance(instance, Elevator)



@given(instance=Elevator_strategy)
def test_elevator_CurrentFloor_setter(instance):
    original = instance.CurrentFloor
    instance.CurrentFloor = original
    assert instance.CurrentFloor == original



@given(instance=Elevator_strategy)
def test_elevator_ElevatorBayNumber_setter(instance):
    original = instance.ElevatorBayNumber
    instance.ElevatorBayNumber = original
    assert instance.ElevatorBayNumber == original



@given(instance=Elevator_strategy)
def test_elevator_CurrentMovement_setter(instance):
    original = instance.CurrentMovement
    instance.CurrentMovement = original
    assert instance.CurrentMovement == original



@given(instance=Elevator_strategy)
def test_elevator_FloorButtons_setter(instance):
    original = instance.FloorButtons
    instance.FloorButtons = original
    assert instance.FloorButtons == original



@given(instance=Elevator_strategy)
def test_elevator_ElevatorNumber_setter(instance):
    original = instance.ElevatorNumber
    instance.ElevatorNumber = original
    assert instance.ElevatorNumber == original



@given(instance=Elevator_strategy)
def test_elevator_ArrivedAtFloor_setter(instance):
    original = instance.ArrivedAtFloor
    instance.ArrivedAtFloor = original
    assert instance.ArrivedAtFloor == original

@given(instance=Building_strategy)
@settings(max_examples=50)
def test_building_instantiation(instance):
    assert isinstance(instance, Building)



@given(instance=Building_strategy)
def test_building_Controller_setter(instance):
    original = instance.Controller
    instance.Controller = original
    assert instance.Controller == original



@given(instance=Building_strategy)
def test_building_ElevatorBays_setter(instance):
    original = instance.ElevatorBays
    instance.ElevatorBays = original
    assert instance.ElevatorBays == original

@given(instance=Controller_strategy)
@settings(max_examples=50)
def test_controller_instantiation(instance):
    assert isinstance(instance, Controller)

@given(instance=ElevatorBay_strategy)
@settings(max_examples=50)
def test_elevatorbay_instantiation(instance):
    assert isinstance(instance, ElevatorBay)



@given(instance=ElevatorBay_strategy)
def test_elevatorbay_BayNumber_setter(instance):
    original = instance.BayNumber
    instance.BayNumber = original
    assert instance.BayNumber == original



@given(instance=ElevatorBay_strategy)
def test_elevatorbay_UpDownButtons_setter(instance):
    original = instance.UpDownButtons
    instance.UpDownButtons = original
    assert instance.UpDownButtons == original



@given(instance=ElevatorBay_strategy)
def test_elevatorbay_Elevators_setter(instance):
    original = instance.Elevators
    instance.Elevators = original
    assert instance.Elevators == original

@given(instance=UpDownButton_strategy)
@settings(max_examples=50)
def test_updownbutton_instantiation(instance):
    assert isinstance(instance, UpDownButton)



@given(instance=UpDownButton_strategy)
def test_updownbutton_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original



@given(instance=UpDownButton_strategy)
def test_updownbutton_ElevatorBay_setter(instance):
    original = instance.ElevatorBay
    instance.ElevatorBay = original
    assert instance.ElevatorBay == original

@given(instance=FloorButton_strategy)
@settings(max_examples=50)
def test_floorbutton_instantiation(instance):
    assert isinstance(instance, FloorButton)



@given(instance=FloorButton_strategy)
def test_floorbutton_Elevator_setter(instance):
    original = instance.Elevator
    instance.Elevator = original
    assert instance.Elevator == original

@given(instance=Button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, Button)



@given(instance=Button_strategy)
def test_button_Clicked_setter(instance):
    original = instance.Clicked
    instance.Clicked = original
    assert instance.Clicked == original



@given(instance=Button_strategy)
def test_button_FloorNumber_setter(instance):
    original = instance.FloorNumber
    instance.FloorNumber = original
    assert instance.FloorNumber == original



@given(instance=Button_strategy)
def test_button_IsOn_setter(instance):
    original = instance.IsOn
    instance.IsOn = original
    assert instance.IsOn == original

@given(instance=object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, object)
