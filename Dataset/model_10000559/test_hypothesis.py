import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_java_lang_Exception,
    hw3_Passenger,
    hw3_Floor,
    hw3_ElevatorFullException,
    hw3_Elevator,
    hw3_Building,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_java_lang_exception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Exception)


def test_genmymodelreverse_java_lang_exception_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Exception.__init__)


def test_genmymodelreverse_java_lang_exception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Exception.__init__)
    params = list(sig.parameters.keys())



def test_hw3_passenger_is_not_abstract():
    assert not inspect.isabstract(hw3_Passenger)


def test_hw3_passenger_constructor_exists():
    assert callable(hw3_Passenger.__init__)


def test_hw3_passenger_constructor_args():
    sig = inspect.signature(hw3_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "UNDEFINED_FLOOR" in params, "Missing parameter 'UNDEFINED_FLOOR'"
    assert "id" in params, "Missing parameter 'id'"
    assert "destinationFloor" in params, "Missing parameter 'destinationFloor'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"

def test_hw3_passenger_has_UNDEFINED_FLOOR():
    assert hasattr(hw3_Passenger, "UNDEFINED_FLOOR")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "UNDEFINED_FLOOR" in klass.__dict__:
            descriptor = klass.__dict__["UNDEFINED_FLOOR"]
            break
    assert isinstance(descriptor, property)

def test_hw3_passenger_has_id():
    assert hasattr(hw3_Passenger, "id")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hw3_passenger_has_destinationFloor():
    assert hasattr(hw3_Passenger, "destinationFloor")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "destinationFloor" in klass.__dict__:
            descriptor = klass.__dict__["destinationFloor"]
            break
    assert isinstance(descriptor, property)

def test_hw3_passenger_has_currentFloor():
    assert hasattr(hw3_Passenger, "currentFloor")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "currentFloor" in klass.__dict__:
            descriptor = klass.__dict__["currentFloor"]
            break
    assert isinstance(descriptor, property)



def test_hw3_floor_is_not_abstract():
    assert not inspect.isabstract(hw3_Floor)


def test_hw3_floor_constructor_exists():
    assert callable(hw3_Floor.__init__)


def test_hw3_floor_constructor_args():
    sig = inspect.signature(hw3_Floor.__init__)
    params = list(sig.parameters.keys())
    assert "myFloorNumber" in params, "Missing parameter 'myFloorNumber'"
    assert "passengersWaiting" in params, "Missing parameter 'passengersWaiting'"

def test_hw3_floor_has_myFloorNumber():
    assert hasattr(hw3_Floor, "myFloorNumber")
    descriptor = None
    for klass in hw3_Floor.__mro__:
        if "myFloorNumber" in klass.__dict__:
            descriptor = klass.__dict__["myFloorNumber"]
            break
    assert isinstance(descriptor, property)

def test_hw3_floor_has_passengersWaiting():
    assert hasattr(hw3_Floor, "passengersWaiting")
    descriptor = None
    for klass in hw3_Floor.__mro__:
        if "passengersWaiting" in klass.__dict__:
            descriptor = klass.__dict__["passengersWaiting"]
            break
    assert isinstance(descriptor, property)



def test_hw3_elevatorfullexception_is_not_abstract():
    assert not inspect.isabstract(hw3_ElevatorFullException)


def test_hw3_elevatorfullexception_constructor_exists():
    assert callable(hw3_ElevatorFullException.__init__)


def test_hw3_elevatorfullexception_constructor_args():
    sig = inspect.signature(hw3_ElevatorFullException.__init__)
    params = list(sig.parameters.keys())



def test_hw3_elevator_is_not_abstract():
    assert not inspect.isabstract(hw3_Elevator)


def test_hw3_elevator_constructor_exists():
    assert callable(hw3_Elevator.__init__)


def test_hw3_elevator_constructor_args():
    sig = inspect.signature(hw3_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "currentFloorIndex" in params, "Missing parameter 'currentFloorIndex'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "CAPACITY" in params, "Missing parameter 'CAPACITY'"
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"

def test_hw3_elevator_has_currentFloorIndex():
    assert hasattr(hw3_Elevator, "currentFloorIndex")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "currentFloorIndex" in klass.__dict__:
            descriptor = klass.__dict__["currentFloorIndex"]
            break
    assert isinstance(descriptor, property)

def test_hw3_elevator_has_NUMBER_OF_FLOORS():
    assert hasattr(hw3_Elevator, "NUMBER_OF_FLOORS")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "NUMBER_OF_FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["NUMBER_OF_FLOORS"]
            break
    assert isinstance(descriptor, property)

def test_hw3_elevator_has_isGoingUp():
    assert hasattr(hw3_Elevator, "isGoingUp")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "isGoingUp" in klass.__dict__:
            descriptor = klass.__dict__["isGoingUp"]
            break
    assert isinstance(descriptor, property)

def test_hw3_elevator_has_numOfPassengers():
    assert hasattr(hw3_Elevator, "numOfPassengers")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "numOfPassengers" in klass.__dict__:
            descriptor = klass.__dict__["numOfPassengers"]
            break
    assert isinstance(descriptor, property)

def test_hw3_elevator_has_CAPACITY():
    assert hasattr(hw3_Elevator, "CAPACITY")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "CAPACITY" in klass.__dict__:
            descriptor = klass.__dict__["CAPACITY"]
            break
    assert isinstance(descriptor, property)

def test_hw3_elevator_has_passengersToFloor():
    assert hasattr(hw3_Elevator, "passengersToFloor")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "passengersToFloor" in klass.__dict__:
            descriptor = klass.__dict__["passengersToFloor"]
            break
    assert isinstance(descriptor, property)



def test_hw3_building_is_not_abstract():
    assert not inspect.isabstract(hw3_Building)


def test_hw3_building_constructor_exists():
    assert callable(hw3_Building.__init__)


def test_hw3_building_constructor_args():
    sig = inspect.signature(hw3_Building.__init__)
    params = list(sig.parameters.keys())
    assert "FLOORS" in params, "Missing parameter 'FLOORS'"
    assert "floors" in params, "Missing parameter 'floors'"

def test_hw3_building_has_FLOORS():
    assert hasattr(hw3_Building, "FLOORS")
    descriptor = None
    for klass in hw3_Building.__mro__:
        if "FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["FLOORS"]
            break
    assert isinstance(descriptor, property)

def test_hw3_building_has_floors():
    assert hasattr(hw3_Building, "floors")
    descriptor = None
    for klass in hw3_Building.__mro__:
        if "floors" in klass.__dict__:
            descriptor = klass.__dict__["floors"]
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
genmymodelreverse_java_lang_Exception_strategy = st.builds(
    genmymodelreverse_java_lang_Exception,
)
hw3_Passenger_strategy = st.builds(
    hw3_Passenger,
    UNDEFINED_FLOOR=
        st.integers(),
    id=
        st.integers(),
    destinationFloor=
        st.integers(),
    currentFloor=
        st.integers()
)
hw3_Floor_strategy = st.builds(
    hw3_Floor,
    myFloorNumber=
        st.integers(),
    passengersWaiting=
        st.integers()
)
hw3_ElevatorFullException_strategy = st.builds(
    hw3_ElevatorFullException,
)
hw3_Elevator_strategy = st.builds(
    hw3_Elevator,
    currentFloorIndex=
        st.integers(),
    NUMBER_OF_FLOORS=
        st.integers(),
    isGoingUp=
        st.booleans(),
    numOfPassengers=
        st.integers(),
    CAPACITY=
        st.integers(),
    passengersToFloor=
        safe_text
)
hw3_Building_strategy = st.builds(
    hw3_Building,
    FLOORS=
        st.integers(),
    floors=
        safe_text
)

@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)

@given(instance=hw3_Passenger_strategy)
@settings(max_examples=50)
def test_hw3_passenger_instantiation(instance):
    assert isinstance(instance, hw3_Passenger)



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_UNDEFINED_FLOOR_setter(instance):
    original = instance.UNDEFINED_FLOOR
    instance.UNDEFINED_FLOOR = original
    assert instance.UNDEFINED_FLOOR == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_destinationFloor_setter(instance):
    original = instance.destinationFloor
    instance.destinationFloor = original
    assert instance.destinationFloor == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original

@given(instance=hw3_Floor_strategy)
@settings(max_examples=50)
def test_hw3_floor_instantiation(instance):
    assert isinstance(instance, hw3_Floor)



@given(instance=hw3_Floor_strategy)
def test_hw3_floor_myFloorNumber_setter(instance):
    original = instance.myFloorNumber
    instance.myFloorNumber = original
    assert instance.myFloorNumber == original



@given(instance=hw3_Floor_strategy)
def test_hw3_floor_passengersWaiting_setter(instance):
    original = instance.passengersWaiting
    instance.passengersWaiting = original
    assert instance.passengersWaiting == original

@given(instance=hw3_ElevatorFullException_strategy)
@settings(max_examples=50)
def test_hw3_elevatorfullexception_instantiation(instance):
    assert isinstance(instance, hw3_ElevatorFullException)

@given(instance=hw3_Elevator_strategy)
@settings(max_examples=50)
def test_hw3_elevator_instantiation(instance):
    assert isinstance(instance, hw3_Elevator)



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_currentFloorIndex_setter(instance):
    original = instance.currentFloorIndex
    instance.currentFloorIndex = original
    assert instance.currentFloorIndex == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_CAPACITY_setter(instance):
    original = instance.CAPACITY
    instance.CAPACITY = original
    assert instance.CAPACITY == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original

@given(instance=hw3_Building_strategy)
@settings(max_examples=50)
def test_hw3_building_instantiation(instance):
    assert isinstance(instance, hw3_Building)



@given(instance=hw3_Building_strategy)
def test_hw3_building_FLOORS_setter(instance):
    original = instance.FLOORS
    instance.FLOORS = original
    assert instance.FLOORS == original



@given(instance=hw3_Building_strategy)
def test_hw3_building_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original
