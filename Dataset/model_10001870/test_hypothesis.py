import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Comparable_Patient__Interface,
    genmymodelreverse_java_lang_Object,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_C1,
    genmymodelreverse_java_lang_Comparable_Interface,
    sec05_Patient,
    sec05_Person,
    sec05_demoSec05,
    hw3test_HW3ElevatorSimulationTest,
    hw3_Passenger,
    hw3_Floor,
    hw3_ElevatorFullException,
    hw3_Elevator,
    hw3_Building,
    hw2test_HW2ElevatorSimulationTest,
    hw2_Floor,
    hw2_ElevatorFullException,
    hw2_Elevator,
    hw2_Building,
    elevatortest_Patient,
    elevatortest_Person,
    elevatortest_ElevatorTest,
    elevator_Elevator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comparable_patient__interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Patient__Interface)


def test_comparable_patient__interface_constructor_exists():
    assert callable(Comparable_Patient__Interface.__init__)


def test_comparable_patient__interface_constructor_args():
    sig = inspect.signature(Comparable_Patient__Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_object_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Object)


def test_genmymodelreverse_java_lang_object_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Object.__init__)


def test_genmymodelreverse_java_lang_object_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Object.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_exception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Exception)


def test_genmymodelreverse_java_lang_exception_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Exception.__init__)


def test_genmymodelreverse_java_lang_exception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Exception.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c1_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C1)


def test_genmymodelreverse_c1_constructor_exists():
    assert callable(genmymodelreverse_C1.__init__)


def test_genmymodelreverse_c1_constructor_args():
    sig = inspect.signature(genmymodelreverse_C1.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Comparable_Interface)


def test_genmymodelreverse_java_lang_comparable_interface_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Comparable_Interface.__init__)


def test_genmymodelreverse_java_lang_comparable_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_sec05_patient_is_not_abstract():
    assert not inspect.isabstract(sec05_Patient)


def test_sec05_patient_constructor_exists():
    assert callable(sec05_Patient.__init__)


def test_sec05_patient_constructor_args():
    sig = inspect.signature(sec05_Patient.__init__)
    params = list(sig.parameters.keys())
    assert "urgencyIndex" in params, "Missing parameter 'urgencyIndex'"

def test_sec05_patient_has_urgencyIndex():
    assert hasattr(sec05_Patient, "urgencyIndex")
    descriptor = None
    for klass in sec05_Patient.__mro__:
        if "urgencyIndex" in klass.__dict__:
            descriptor = klass.__dict__["urgencyIndex"]
            break
    assert isinstance(descriptor, property)



def test_sec05_person_is_not_abstract():
    assert not inspect.isabstract(sec05_Person)


def test_sec05_person_constructor_exists():
    assert callable(sec05_Person.__init__)


def test_sec05_person_constructor_args():
    sig = inspect.signature(sec05_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sec05_person_has_name():
    assert hasattr(sec05_Person, "name")
    descriptor = None
    for klass in sec05_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sec05_demosec05_is_not_abstract():
    assert not inspect.isabstract(sec05_demoSec05)


def test_sec05_demosec05_constructor_exists():
    assert callable(sec05_demoSec05.__init__)


def test_sec05_demosec05_constructor_args():
    sig = inspect.signature(sec05_demoSec05.__init__)
    params = list(sig.parameters.keys())



def test_hw3test_hw3elevatorsimulationtest_is_not_abstract():
    assert not inspect.isabstract(hw3test_HW3ElevatorSimulationTest)


def test_hw3test_hw3elevatorsimulationtest_constructor_exists():
    assert callable(hw3test_HW3ElevatorSimulationTest.__init__)


def test_hw3test_hw3elevatorsimulationtest_constructor_args():
    sig = inspect.signature(hw3test_HW3ElevatorSimulationTest.__init__)
    params = list(sig.parameters.keys())



def test_hw3_passenger_is_not_abstract():
    assert not inspect.isabstract(hw3_Passenger)


def test_hw3_passenger_constructor_exists():
    assert callable(hw3_Passenger.__init__)


def test_hw3_passenger_constructor_args():
    sig = inspect.signature(hw3_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "UNDEFINED_FLOOR" in params, "Missing parameter 'UNDEFINED_FLOOR'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"
    assert "destinationFloor" in params, "Missing parameter 'destinationFloor'"

def test_hw3_passenger_has_id():
    assert hasattr(hw3_Passenger, "id")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hw3_passenger_has_UNDEFINED_FLOOR():
    assert hasattr(hw3_Passenger, "UNDEFINED_FLOOR")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "UNDEFINED_FLOOR" in klass.__dict__:
            descriptor = klass.__dict__["UNDEFINED_FLOOR"]
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

def test_hw3_passenger_has_destinationFloor():
    assert hasattr(hw3_Passenger, "destinationFloor")
    descriptor = None
    for klass in hw3_Passenger.__mro__:
        if "destinationFloor" in klass.__dict__:
            descriptor = klass.__dict__["destinationFloor"]
            break
    assert isinstance(descriptor, property)



def test_hw3_floor_is_not_abstract():
    assert not inspect.isabstract(hw3_Floor)


def test_hw3_floor_constructor_exists():
    assert callable(hw3_Floor.__init__)


def test_hw3_floor_constructor_args():
    sig = inspect.signature(hw3_Floor.__init__)
    params = list(sig.parameters.keys())
    assert "passengersWaiting" in params, "Missing parameter 'passengersWaiting'"
    assert "myFloorNumber" in params, "Missing parameter 'myFloorNumber'"

def test_hw3_floor_has_passengersWaiting():
    assert hasattr(hw3_Floor, "passengersWaiting")
    descriptor = None
    for klass in hw3_Floor.__mro__:
        if "passengersWaiting" in klass.__dict__:
            descriptor = klass.__dict__["passengersWaiting"]
            break
    assert isinstance(descriptor, property)

def test_hw3_floor_has_myFloorNumber():
    assert hasattr(hw3_Floor, "myFloorNumber")
    descriptor = None
    for klass in hw3_Floor.__mro__:
        if "myFloorNumber" in klass.__dict__:
            descriptor = klass.__dict__["myFloorNumber"]
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
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "currentFloorIndex" in params, "Missing parameter 'currentFloorIndex'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"
    assert "CAPACITY" in params, "Missing parameter 'CAPACITY'"

def test_hw3_elevator_has_passengersToFloor():
    assert hasattr(hw3_Elevator, "passengersToFloor")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "passengersToFloor" in klass.__dict__:
            descriptor = klass.__dict__["passengersToFloor"]
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

def test_hw3_elevator_has_CAPACITY():
    assert hasattr(hw3_Elevator, "CAPACITY")
    descriptor = None
    for klass in hw3_Elevator.__mro__:
        if "CAPACITY" in klass.__dict__:
            descriptor = klass.__dict__["CAPACITY"]
            break
    assert isinstance(descriptor, property)



def test_hw3_building_is_not_abstract():
    assert not inspect.isabstract(hw3_Building)


def test_hw3_building_constructor_exists():
    assert callable(hw3_Building.__init__)


def test_hw3_building_constructor_args():
    sig = inspect.signature(hw3_Building.__init__)
    params = list(sig.parameters.keys())
    assert "floors" in params, "Missing parameter 'floors'"
    assert "FLOORS" in params, "Missing parameter 'FLOORS'"

def test_hw3_building_has_floors():
    assert hasattr(hw3_Building, "floors")
    descriptor = None
    for klass in hw3_Building.__mro__:
        if "floors" in klass.__dict__:
            descriptor = klass.__dict__["floors"]
            break
    assert isinstance(descriptor, property)

def test_hw3_building_has_FLOORS():
    assert hasattr(hw3_Building, "FLOORS")
    descriptor = None
    for klass in hw3_Building.__mro__:
        if "FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["FLOORS"]
            break
    assert isinstance(descriptor, property)



def test_hw2test_hw2elevatorsimulationtest_is_not_abstract():
    assert not inspect.isabstract(hw2test_HW2ElevatorSimulationTest)


def test_hw2test_hw2elevatorsimulationtest_constructor_exists():
    assert callable(hw2test_HW2ElevatorSimulationTest.__init__)


def test_hw2test_hw2elevatorsimulationtest_constructor_args():
    sig = inspect.signature(hw2test_HW2ElevatorSimulationTest.__init__)
    params = list(sig.parameters.keys())



def test_hw2_floor_is_not_abstract():
    assert not inspect.isabstract(hw2_Floor)


def test_hw2_floor_constructor_exists():
    assert callable(hw2_Floor.__init__)


def test_hw2_floor_constructor_args():
    sig = inspect.signature(hw2_Floor.__init__)
    params = list(sig.parameters.keys())
    assert "passengersWaiting" in params, "Missing parameter 'passengersWaiting'"

def test_hw2_floor_has_passengersWaiting():
    assert hasattr(hw2_Floor, "passengersWaiting")
    descriptor = None
    for klass in hw2_Floor.__mro__:
        if "passengersWaiting" in klass.__dict__:
            descriptor = klass.__dict__["passengersWaiting"]
            break
    assert isinstance(descriptor, property)



def test_hw2_elevatorfullexception_is_not_abstract():
    assert not inspect.isabstract(hw2_ElevatorFullException)


def test_hw2_elevatorfullexception_constructor_exists():
    assert callable(hw2_ElevatorFullException.__init__)


def test_hw2_elevatorfullexception_constructor_args():
    sig = inspect.signature(hw2_ElevatorFullException.__init__)
    params = list(sig.parameters.keys())



def test_hw2_elevator_is_not_abstract():
    assert not inspect.isabstract(hw2_Elevator)


def test_hw2_elevator_constructor_exists():
    assert callable(hw2_Elevator.__init__)


def test_hw2_elevator_constructor_args():
    sig = inspect.signature(hw2_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "currentFloorIndex" in params, "Missing parameter 'currentFloorIndex'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "CAPACITY" in params, "Missing parameter 'CAPACITY'"

def test_hw2_elevator_has_isGoingUp():
    assert hasattr(hw2_Elevator, "isGoingUp")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "isGoingUp" in klass.__dict__:
            descriptor = klass.__dict__["isGoingUp"]
            break
    assert isinstance(descriptor, property)

def test_hw2_elevator_has_NUMBER_OF_FLOORS():
    assert hasattr(hw2_Elevator, "NUMBER_OF_FLOORS")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "NUMBER_OF_FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["NUMBER_OF_FLOORS"]
            break
    assert isinstance(descriptor, property)

def test_hw2_elevator_has_currentFloorIndex():
    assert hasattr(hw2_Elevator, "currentFloorIndex")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "currentFloorIndex" in klass.__dict__:
            descriptor = klass.__dict__["currentFloorIndex"]
            break
    assert isinstance(descriptor, property)

def test_hw2_elevator_has_numOfPassengers():
    assert hasattr(hw2_Elevator, "numOfPassengers")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "numOfPassengers" in klass.__dict__:
            descriptor = klass.__dict__["numOfPassengers"]
            break
    assert isinstance(descriptor, property)

def test_hw2_elevator_has_passengersToFloor():
    assert hasattr(hw2_Elevator, "passengersToFloor")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "passengersToFloor" in klass.__dict__:
            descriptor = klass.__dict__["passengersToFloor"]
            break
    assert isinstance(descriptor, property)

def test_hw2_elevator_has_CAPACITY():
    assert hasattr(hw2_Elevator, "CAPACITY")
    descriptor = None
    for klass in hw2_Elevator.__mro__:
        if "CAPACITY" in klass.__dict__:
            descriptor = klass.__dict__["CAPACITY"]
            break
    assert isinstance(descriptor, property)



def test_hw2_building_is_not_abstract():
    assert not inspect.isabstract(hw2_Building)


def test_hw2_building_constructor_exists():
    assert callable(hw2_Building.__init__)


def test_hw2_building_constructor_args():
    sig = inspect.signature(hw2_Building.__init__)
    params = list(sig.parameters.keys())
    assert "FLOORS" in params, "Missing parameter 'FLOORS'"
    assert "floors" in params, "Missing parameter 'floors'"

def test_hw2_building_has_FLOORS():
    assert hasattr(hw2_Building, "FLOORS")
    descriptor = None
    for klass in hw2_Building.__mro__:
        if "FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["FLOORS"]
            break
    assert isinstance(descriptor, property)

def test_hw2_building_has_floors():
    assert hasattr(hw2_Building, "floors")
    descriptor = None
    for klass in hw2_Building.__mro__:
        if "floors" in klass.__dict__:
            descriptor = klass.__dict__["floors"]
            break
    assert isinstance(descriptor, property)



def test_elevatortest_patient_is_not_abstract():
    assert not inspect.isabstract(elevatortest_Patient)


def test_elevatortest_patient_constructor_exists():
    assert callable(elevatortest_Patient.__init__)


def test_elevatortest_patient_constructor_args():
    sig = inspect.signature(elevatortest_Patient.__init__)
    params = list(sig.parameters.keys())
    assert "urgencyIndex" in params, "Missing parameter 'urgencyIndex'"

def test_elevatortest_patient_has_urgencyIndex():
    assert hasattr(elevatortest_Patient, "urgencyIndex")
    descriptor = None
    for klass in elevatortest_Patient.__mro__:
        if "urgencyIndex" in klass.__dict__:
            descriptor = klass.__dict__["urgencyIndex"]
            break
    assert isinstance(descriptor, property)



def test_elevatortest_person_is_not_abstract():
    assert not inspect.isabstract(elevatortest_Person)


def test_elevatortest_person_constructor_exists():
    assert callable(elevatortest_Person.__init__)


def test_elevatortest_person_constructor_args():
    sig = inspect.signature(elevatortest_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_elevatortest_person_has_name():
    assert hasattr(elevatortest_Person, "name")
    descriptor = None
    for klass in elevatortest_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_elevatortest_elevatortest_is_not_abstract():
    assert not inspect.isabstract(elevatortest_ElevatorTest)


def test_elevatortest_elevatortest_constructor_exists():
    assert callable(elevatortest_ElevatorTest.__init__)


def test_elevatortest_elevatortest_constructor_args():
    sig = inspect.signature(elevatortest_ElevatorTest.__init__)
    params = list(sig.parameters.keys())



def test_elevator_elevator_is_not_abstract():
    assert not inspect.isabstract(elevator_Elevator)


def test_elevator_elevator_constructor_exists():
    assert callable(elevator_Elevator.__init__)


def test_elevator_elevator_constructor_args():
    sig = inspect.signature(elevator_Elevator.__init__)
    params = list(sig.parameters.keys())
    assert "passengersToFloor" in params, "Missing parameter 'passengersToFloor'"
    assert "numOfPassengers" in params, "Missing parameter 'numOfPassengers'"
    assert "currentFloor" in params, "Missing parameter 'currentFloor'"
    assert "NUMBER_OF_FLOORS" in params, "Missing parameter 'NUMBER_OF_FLOORS'"
    assert "isGoingUp" in params, "Missing parameter 'isGoingUp'"

def test_elevator_elevator_has_passengersToFloor():
    assert hasattr(elevator_Elevator, "passengersToFloor")
    descriptor = None
    for klass in elevator_Elevator.__mro__:
        if "passengersToFloor" in klass.__dict__:
            descriptor = klass.__dict__["passengersToFloor"]
            break
    assert isinstance(descriptor, property)

def test_elevator_elevator_has_numOfPassengers():
    assert hasattr(elevator_Elevator, "numOfPassengers")
    descriptor = None
    for klass in elevator_Elevator.__mro__:
        if "numOfPassengers" in klass.__dict__:
            descriptor = klass.__dict__["numOfPassengers"]
            break
    assert isinstance(descriptor, property)

def test_elevator_elevator_has_currentFloor():
    assert hasattr(elevator_Elevator, "currentFloor")
    descriptor = None
    for klass in elevator_Elevator.__mro__:
        if "currentFloor" in klass.__dict__:
            descriptor = klass.__dict__["currentFloor"]
            break
    assert isinstance(descriptor, property)

def test_elevator_elevator_has_NUMBER_OF_FLOORS():
    assert hasattr(elevator_Elevator, "NUMBER_OF_FLOORS")
    descriptor = None
    for klass in elevator_Elevator.__mro__:
        if "NUMBER_OF_FLOORS" in klass.__dict__:
            descriptor = klass.__dict__["NUMBER_OF_FLOORS"]
            break
    assert isinstance(descriptor, property)

def test_elevator_elevator_has_isGoingUp():
    assert hasattr(elevator_Elevator, "isGoingUp")
    descriptor = None
    for klass in elevator_Elevator.__mro__:
        if "isGoingUp" in klass.__dict__:
            descriptor = klass.__dict__["isGoingUp"]
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
Comparable_Patient__Interface_strategy = st.builds(
    Comparable_Patient__Interface,
)
genmymodelreverse_java_lang_Object_strategy = st.builds(
    genmymodelreverse_java_lang_Object,
)
genmymodelreverse_java_lang_Exception_strategy = st.builds(
    genmymodelreverse_java_lang_Exception,
)
genmymodelreverse_C1_strategy = st.builds(
    genmymodelreverse_C1,
)
genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(
    genmymodelreverse_java_lang_Comparable_Interface,
)
sec05_Patient_strategy = st.builds(
    sec05_Patient,
    urgencyIndex=
        st.integers()
)
sec05_Person_strategy = st.builds(
    sec05_Person,
    name=
        safe_text
)
sec05_demoSec05_strategy = st.builds(
    sec05_demoSec05,
)
hw3test_HW3ElevatorSimulationTest_strategy = st.builds(
    hw3test_HW3ElevatorSimulationTest,
)
hw3_Passenger_strategy = st.builds(
    hw3_Passenger,
    id=
        st.integers(),
    UNDEFINED_FLOOR=
        st.integers(),
    currentFloor=
        st.integers(),
    destinationFloor=
        st.integers()
)
hw3_Floor_strategy = st.builds(
    hw3_Floor,
    passengersWaiting=
        st.integers(),
    myFloorNumber=
        st.integers()
)
hw3_ElevatorFullException_strategy = st.builds(
    hw3_ElevatorFullException,
)
hw3_Elevator_strategy = st.builds(
    hw3_Elevator,
    passengersToFloor=
        safe_text,
    numOfPassengers=
        st.integers(),
    currentFloorIndex=
        st.integers(),
    NUMBER_OF_FLOORS=
        st.integers(),
    isGoingUp=
        st.booleans(),
    CAPACITY=
        st.integers()
)
hw3_Building_strategy = st.builds(
    hw3_Building,
    floors=
        safe_text,
    FLOORS=
        st.integers()
)
hw2test_HW2ElevatorSimulationTest_strategy = st.builds(
    hw2test_HW2ElevatorSimulationTest,
)
hw2_Floor_strategy = st.builds(
    hw2_Floor,
    passengersWaiting=
        st.integers()
)
hw2_ElevatorFullException_strategy = st.builds(
    hw2_ElevatorFullException,
)
hw2_Elevator_strategy = st.builds(
    hw2_Elevator,
    isGoingUp=
        st.booleans(),
    NUMBER_OF_FLOORS=
        st.integers(),
    currentFloorIndex=
        st.integers(),
    numOfPassengers=
        st.integers(),
    passengersToFloor=
        safe_text,
    CAPACITY=
        st.integers()
)
hw2_Building_strategy = st.builds(
    hw2_Building,
    FLOORS=
        st.integers(),
    floors=
        safe_text
)
elevatortest_Patient_strategy = st.builds(
    elevatortest_Patient,
    urgencyIndex=
        st.integers()
)
elevatortest_Person_strategy = st.builds(
    elevatortest_Person,
    name=
        safe_text
)
elevatortest_ElevatorTest_strategy = st.builds(
    elevatortest_ElevatorTest,
)
elevator_Elevator_strategy = st.builds(
    elevator_Elevator,
    passengersToFloor=
        safe_text,
    numOfPassengers=
        st.integers(),
    currentFloor=
        st.integers(),
    NUMBER_OF_FLOORS=
        st.integers(),
    isGoingUp=
        st.booleans()
)

@given(instance=Comparable_Patient__Interface_strategy)
@settings(max_examples=50)
def test_comparable_patient__interface_instantiation(instance):
    assert isinstance(instance, Comparable_Patient__Interface)

@given(instance=genmymodelreverse_java_lang_Object_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_object_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Object)

@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)

@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)

@given(instance=genmymodelreverse_java_lang_Comparable_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_comparable_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Comparable_Interface)

@given(instance=sec05_Patient_strategy)
@settings(max_examples=50)
def test_sec05_patient_instantiation(instance):
    assert isinstance(instance, sec05_Patient)



@given(instance=sec05_Patient_strategy)
def test_sec05_patient_urgencyIndex_setter(instance):
    original = instance.urgencyIndex
    instance.urgencyIndex = original
    assert instance.urgencyIndex == original

@given(instance=sec05_Person_strategy)
@settings(max_examples=50)
def test_sec05_person_instantiation(instance):
    assert isinstance(instance, sec05_Person)



@given(instance=sec05_Person_strategy)
def test_sec05_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sec05_demoSec05_strategy)
@settings(max_examples=50)
def test_sec05_demosec05_instantiation(instance):
    assert isinstance(instance, sec05_demoSec05)

@given(instance=hw3test_HW3ElevatorSimulationTest_strategy)
@settings(max_examples=50)
def test_hw3test_hw3elevatorsimulationtest_instantiation(instance):
    assert isinstance(instance, hw3test_HW3ElevatorSimulationTest)

@given(instance=hw3_Passenger_strategy)
@settings(max_examples=50)
def test_hw3_passenger_instantiation(instance):
    assert isinstance(instance, hw3_Passenger)



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_UNDEFINED_FLOOR_setter(instance):
    original = instance.UNDEFINED_FLOOR
    instance.UNDEFINED_FLOOR = original
    assert instance.UNDEFINED_FLOOR == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original



@given(instance=hw3_Passenger_strategy)
def test_hw3_passenger_destinationFloor_setter(instance):
    original = instance.destinationFloor
    instance.destinationFloor = original
    assert instance.destinationFloor == original

@given(instance=hw3_Floor_strategy)
@settings(max_examples=50)
def test_hw3_floor_instantiation(instance):
    assert isinstance(instance, hw3_Floor)



@given(instance=hw3_Floor_strategy)
def test_hw3_floor_passengersWaiting_setter(instance):
    original = instance.passengersWaiting
    instance.passengersWaiting = original
    assert instance.passengersWaiting == original



@given(instance=hw3_Floor_strategy)
def test_hw3_floor_myFloorNumber_setter(instance):
    original = instance.myFloorNumber
    instance.myFloorNumber = original
    assert instance.myFloorNumber == original

@given(instance=hw3_ElevatorFullException_strategy)
@settings(max_examples=50)
def test_hw3_elevatorfullexception_instantiation(instance):
    assert isinstance(instance, hw3_ElevatorFullException)

@given(instance=hw3_Elevator_strategy)
@settings(max_examples=50)
def test_hw3_elevator_instantiation(instance):
    assert isinstance(instance, hw3_Elevator)



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=hw3_Elevator_strategy)
def test_hw3_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



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
def test_hw3_elevator_CAPACITY_setter(instance):
    original = instance.CAPACITY
    instance.CAPACITY = original
    assert instance.CAPACITY == original

@given(instance=hw3_Building_strategy)
@settings(max_examples=50)
def test_hw3_building_instantiation(instance):
    assert isinstance(instance, hw3_Building)



@given(instance=hw3_Building_strategy)
def test_hw3_building_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original



@given(instance=hw3_Building_strategy)
def test_hw3_building_FLOORS_setter(instance):
    original = instance.FLOORS
    instance.FLOORS = original
    assert instance.FLOORS == original

@given(instance=hw2test_HW2ElevatorSimulationTest_strategy)
@settings(max_examples=50)
def test_hw2test_hw2elevatorsimulationtest_instantiation(instance):
    assert isinstance(instance, hw2test_HW2ElevatorSimulationTest)

@given(instance=hw2_Floor_strategy)
@settings(max_examples=50)
def test_hw2_floor_instantiation(instance):
    assert isinstance(instance, hw2_Floor)



@given(instance=hw2_Floor_strategy)
def test_hw2_floor_passengersWaiting_setter(instance):
    original = instance.passengersWaiting
    instance.passengersWaiting = original
    assert instance.passengersWaiting == original

@given(instance=hw2_ElevatorFullException_strategy)
@settings(max_examples=50)
def test_hw2_elevatorfullexception_instantiation(instance):
    assert isinstance(instance, hw2_ElevatorFullException)

@given(instance=hw2_Elevator_strategy)
@settings(max_examples=50)
def test_hw2_elevator_instantiation(instance):
    assert isinstance(instance, hw2_Elevator)



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_currentFloorIndex_setter(instance):
    original = instance.currentFloorIndex
    instance.currentFloorIndex = original
    assert instance.currentFloorIndex == original



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=hw2_Elevator_strategy)
def test_hw2_elevator_CAPACITY_setter(instance):
    original = instance.CAPACITY
    instance.CAPACITY = original
    assert instance.CAPACITY == original

@given(instance=hw2_Building_strategy)
@settings(max_examples=50)
def test_hw2_building_instantiation(instance):
    assert isinstance(instance, hw2_Building)



@given(instance=hw2_Building_strategy)
def test_hw2_building_FLOORS_setter(instance):
    original = instance.FLOORS
    instance.FLOORS = original
    assert instance.FLOORS == original



@given(instance=hw2_Building_strategy)
def test_hw2_building_floors_setter(instance):
    original = instance.floors
    instance.floors = original
    assert instance.floors == original

@given(instance=elevatortest_Patient_strategy)
@settings(max_examples=50)
def test_elevatortest_patient_instantiation(instance):
    assert isinstance(instance, elevatortest_Patient)



@given(instance=elevatortest_Patient_strategy)
def test_elevatortest_patient_urgencyIndex_setter(instance):
    original = instance.urgencyIndex
    instance.urgencyIndex = original
    assert instance.urgencyIndex == original

@given(instance=elevatortest_Person_strategy)
@settings(max_examples=50)
def test_elevatortest_person_instantiation(instance):
    assert isinstance(instance, elevatortest_Person)



@given(instance=elevatortest_Person_strategy)
def test_elevatortest_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=elevatortest_ElevatorTest_strategy)
@settings(max_examples=50)
def test_elevatortest_elevatortest_instantiation(instance):
    assert isinstance(instance, elevatortest_ElevatorTest)

@given(instance=elevator_Elevator_strategy)
@settings(max_examples=50)
def test_elevator_elevator_instantiation(instance):
    assert isinstance(instance, elevator_Elevator)



@given(instance=elevator_Elevator_strategy)
def test_elevator_elevator_passengersToFloor_setter(instance):
    original = instance.passengersToFloor
    instance.passengersToFloor = original
    assert instance.passengersToFloor == original



@given(instance=elevator_Elevator_strategy)
def test_elevator_elevator_numOfPassengers_setter(instance):
    original = instance.numOfPassengers
    instance.numOfPassengers = original
    assert instance.numOfPassengers == original



@given(instance=elevator_Elevator_strategy)
def test_elevator_elevator_currentFloor_setter(instance):
    original = instance.currentFloor
    instance.currentFloor = original
    assert instance.currentFloor == original



@given(instance=elevator_Elevator_strategy)
def test_elevator_elevator_NUMBER_OF_FLOORS_setter(instance):
    original = instance.NUMBER_OF_FLOORS
    instance.NUMBER_OF_FLOORS = original
    assert instance.NUMBER_OF_FLOORS == original



@given(instance=elevator_Elevator_strategy)
def test_elevator_elevator_isGoingUp_setter(instance):
    original = instance.isGoingUp
    instance.isGoingUp = original
    assert instance.isGoingUp == original
