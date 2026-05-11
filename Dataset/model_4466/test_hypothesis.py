import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rover::SetLightColor,
    rover::Wait,
    rover::PositionQuantity,
    rover::SingleQuantity,
    Component,
    rover::Sensor,
    rover::Move,
    rover::Rotate,
    rover::Repeate,
    rover::Command,
    rover::Block,
    Actuator,
    rover::Light,
    rover::Motor,
    Sensor,
    rover::DistanceSensor,
    rover::directionFacing,
    rover::Compass,
    rover::GPS,
    rover::Actuator,
    rover::Tansition,
    rover::Program,
    rover::Component,
    rover::Rover,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rover::setlightcolor_is_not_abstract():
    assert not inspect.isabstract(rover::SetLightColor)


def test_rover::setlightcolor_constructor_exists():
    assert callable(rover::SetLightColor.__init__)


def test_rover::setlightcolor_constructor_args():
    sig = inspect.signature(rover::SetLightColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_rover::setlightcolor_has_color():
    assert hasattr(rover::SetLightColor, "color")
    descriptor = None
    for klass in rover::SetLightColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_rover::wait_is_not_abstract():
    assert not inspect.isabstract(rover::Wait)


def test_rover::wait_constructor_exists():
    assert callable(rover::Wait.__init__)


def test_rover::wait_constructor_args():
    sig = inspect.signature(rover::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_rover::wait_has_time():
    assert hasattr(rover::Wait, "time")
    descriptor = None
    for klass in rover::Wait.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_rover::positionquantity_is_not_abstract():
    assert not inspect.isabstract(rover::PositionQuantity)


def test_rover::positionquantity_constructor_exists():
    assert callable(rover::PositionQuantity.__init__)


def test_rover::positionquantity_constructor_args():
    sig = inspect.signature(rover::PositionQuantity.__init__)
    params = list(sig.parameters.keys())



def test_rover::singlequantity_is_not_abstract():
    assert not inspect.isabstract(rover::SingleQuantity)


def test_rover::singlequantity_constructor_exists():
    assert callable(rover::SingleQuantity.__init__)


def test_rover::singlequantity_constructor_args():
    sig = inspect.signature(rover::SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_rover::sensor_is_not_abstract():
    assert not inspect.isabstract(rover::Sensor)


def test_rover::sensor_constructor_exists():
    assert callable(rover::Sensor.__init__)


def test_rover::sensor_constructor_args():
    sig = inspect.signature(rover::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_rover::move_is_not_abstract():
    assert not inspect.isabstract(rover::Move)


def test_rover::move_constructor_exists():
    assert callable(rover::Move.__init__)


def test_rover::move_constructor_args():
    sig = inspect.signature(rover::Move.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "velocity" in params, "Missing parameter 'velocity'"

def test_rover::move_has_length():
    assert hasattr(rover::Move, "length")
    descriptor = None
    for klass in rover::Move.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rover::move_has_velocity():
    assert hasattr(rover::Move, "velocity")
    descriptor = None
    for klass in rover::Move.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)



def test_rover::rotate_is_not_abstract():
    assert not inspect.isabstract(rover::Rotate)


def test_rover::rotate_constructor_exists():
    assert callable(rover::Rotate.__init__)


def test_rover::rotate_constructor_args():
    sig = inspect.signature(rover::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angel" in params, "Missing parameter 'angel'"

def test_rover::rotate_has_angel():
    assert hasattr(rover::Rotate, "angel")
    descriptor = None
    for klass in rover::Rotate.__mro__:
        if "angel" in klass.__dict__:
            descriptor = klass.__dict__["angel"]
            break
    assert isinstance(descriptor, property)



def test_rover::repeate_is_not_abstract():
    assert not inspect.isabstract(rover::Repeate)


def test_rover::repeate_constructor_exists():
    assert callable(rover::Repeate.__init__)


def test_rover::repeate_constructor_args():
    sig = inspect.signature(rover::Repeate.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_rover::repeate_has_count():
    assert hasattr(rover::Repeate, "count")
    descriptor = None
    for klass in rover::Repeate.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_rover::command_is_not_abstract():
    assert not inspect.isabstract(rover::Command)


def test_rover::command_constructor_exists():
    assert callable(rover::Command.__init__)


def test_rover::command_constructor_args():
    sig = inspect.signature(rover::Command.__init__)
    params = list(sig.parameters.keys())



def test_rover::block_is_not_abstract():
    assert not inspect.isabstract(rover::Block)


def test_rover::block_constructor_exists():
    assert callable(rover::Block.__init__)


def test_rover::block_constructor_args():
    sig = inspect.signature(rover::Block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rover::block_has_name():
    assert hasattr(rover::Block, "name")
    descriptor = None
    for klass in rover::Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_rover::light_is_not_abstract():
    assert not inspect.isabstract(rover::Light)


def test_rover::light_constructor_exists():
    assert callable(rover::Light.__init__)


def test_rover::light_constructor_args():
    sig = inspect.signature(rover::Light.__init__)
    params = list(sig.parameters.keys())



def test_rover::motor_is_not_abstract():
    assert not inspect.isabstract(rover::Motor)


def test_rover::motor_constructor_exists():
    assert callable(rover::Motor.__init__)


def test_rover::motor_constructor_args():
    sig = inspect.signature(rover::Motor.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_rover::distancesensor_is_not_abstract():
    assert not inspect.isabstract(rover::DistanceSensor)


def test_rover::distancesensor_constructor_exists():
    assert callable(rover::DistanceSensor.__init__)


def test_rover::distancesensor_constructor_args():
    sig = inspect.signature(rover::DistanceSensor.__init__)
    params = list(sig.parameters.keys())
    assert "remainingDistance" in params, "Missing parameter 'remainingDistance'"

def test_rover::distancesensor_has_remainingDistance():
    assert hasattr(rover::DistanceSensor, "remainingDistance")
    descriptor = None
    for klass in rover::DistanceSensor.__mro__:
        if "remainingDistance" in klass.__dict__:
            descriptor = klass.__dict__["remainingDistance"]
            break
    assert isinstance(descriptor, property)



def test_rover::directionfacing_is_not_abstract():
    assert not inspect.isabstract(rover::directionFacing)


def test_rover::directionfacing_constructor_exists():
    assert callable(rover::directionFacing.__init__)


def test_rover::directionfacing_constructor_args():
    sig = inspect.signature(rover::directionFacing.__init__)
    params = list(sig.parameters.keys())
    assert "currentlyFacing" in params, "Missing parameter 'currentlyFacing'"

def test_rover::directionfacing_has_currentlyFacing():
    assert hasattr(rover::directionFacing, "currentlyFacing")
    descriptor = None
    for klass in rover::directionFacing.__mro__:
        if "currentlyFacing" in klass.__dict__:
            descriptor = klass.__dict__["currentlyFacing"]
            break
    assert isinstance(descriptor, property)



def test_rover::compass_is_not_abstract():
    assert not inspect.isabstract(rover::Compass)


def test_rover::compass_constructor_exists():
    assert callable(rover::Compass.__init__)


def test_rover::compass_constructor_args():
    sig = inspect.signature(rover::Compass.__init__)
    params = list(sig.parameters.keys())



def test_rover::gps_is_not_abstract():
    assert not inspect.isabstract(rover::GPS)


def test_rover::gps_constructor_exists():
    assert callable(rover::GPS.__init__)


def test_rover::gps_constructor_args():
    sig = inspect.signature(rover::GPS.__init__)
    params = list(sig.parameters.keys())
    assert "currentPosition" in params, "Missing parameter 'currentPosition'"

def test_rover::gps_has_currentPosition():
    assert hasattr(rover::GPS, "currentPosition")
    descriptor = None
    for klass in rover::GPS.__mro__:
        if "currentPosition" in klass.__dict__:
            descriptor = klass.__dict__["currentPosition"]
            break
    assert isinstance(descriptor, property)



def test_rover::actuator_is_not_abstract():
    assert not inspect.isabstract(rover::Actuator)


def test_rover::actuator_constructor_exists():
    assert callable(rover::Actuator.__init__)


def test_rover::actuator_constructor_args():
    sig = inspect.signature(rover::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_rover::tansition_is_not_abstract():
    assert not inspect.isabstract(rover::Tansition)


def test_rover::tansition_constructor_exists():
    assert callable(rover::Tansition.__init__)


def test_rover::tansition_constructor_args():
    sig = inspect.signature(rover::Tansition.__init__)
    params = list(sig.parameters.keys())
    assert "comparedQuantity" in params, "Missing parameter 'comparedQuantity'"
    assert "operationUsed" in params, "Missing parameter 'operationUsed'"

def test_rover::tansition_has_comparedQuantity():
    assert hasattr(rover::Tansition, "comparedQuantity")
    descriptor = None
    for klass in rover::Tansition.__mro__:
        if "comparedQuantity" in klass.__dict__:
            descriptor = klass.__dict__["comparedQuantity"]
            break
    assert isinstance(descriptor, property)

def test_rover::tansition_has_operationUsed():
    assert hasattr(rover::Tansition, "operationUsed")
    descriptor = None
    for klass in rover::Tansition.__mro__:
        if "operationUsed" in klass.__dict__:
            descriptor = klass.__dict__["operationUsed"]
            break
    assert isinstance(descriptor, property)



def test_rover::program_is_not_abstract():
    assert not inspect.isabstract(rover::Program)


def test_rover::program_constructor_exists():
    assert callable(rover::Program.__init__)


def test_rover::program_constructor_args():
    sig = inspect.signature(rover::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rover::program_has_name():
    assert hasattr(rover::Program, "name")
    descriptor = None
    for klass in rover::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rover::component_is_not_abstract():
    assert not inspect.isabstract(rover::Component)


def test_rover::component_constructor_exists():
    assert callable(rover::Component.__init__)


def test_rover::component_constructor_args():
    sig = inspect.signature(rover::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rover::component_has_name():
    assert hasattr(rover::Component, "name")
    descriptor = None
    for klass in rover::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rover::rover_is_not_abstract():
    assert not inspect.isabstract(rover::Rover)


def test_rover::rover_constructor_exists():
    assert callable(rover::Rover.__init__)


def test_rover::rover_constructor_args():
    sig = inspect.signature(rover::Rover.__init__)
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
rover::SetLightColor_strategy = st.builds(
    rover::SetLightColor,
    color=
        safe_text
)
rover::Wait_strategy = st.builds(
    rover::Wait,
    time=
        st.integers()
)
rover::PositionQuantity_strategy = st.builds(
    rover::PositionQuantity,
)
rover::SingleQuantity_strategy = st.builds(
    rover::SingleQuantity,
)
Component_strategy = st.builds(
    Component,
)
rover::Sensor_strategy = st.builds(
    rover::Sensor,
)
rover::Move_strategy = st.builds(
    rover::Move,
    length=
        st.integers(),
    velocity=
        st.integers()
)
rover::Rotate_strategy = st.builds(
    rover::Rotate,
    angel=
        st.integers()
)
rover::Repeate_strategy = st.builds(
    rover::Repeate,
    count=
        st.integers()
)
rover::Command_strategy = st.builds(
    rover::Command,
)
rover::Block_strategy = st.builds(
    rover::Block,
    name=
        safe_text
)
Actuator_strategy = st.builds(
    Actuator,
)
rover::Light_strategy = st.builds(
    rover::Light,
)
rover::Motor_strategy = st.builds(
    rover::Motor,
)
Sensor_strategy = st.builds(
    Sensor,
)
rover::DistanceSensor_strategy = st.builds(
    rover::DistanceSensor,
    remainingDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
rover::directionFacing_strategy = st.builds(
    rover::directionFacing,
    currentlyFacing=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
rover::Compass_strategy = st.builds(
    rover::Compass,
)
rover::GPS_strategy = st.builds(
    rover::GPS,
    currentPosition=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
rover::Actuator_strategy = st.builds(
    rover::Actuator,
)
rover::Tansition_strategy = st.builds(
    rover::Tansition,
    comparedQuantity=
        safe_text,
    operationUsed=
        safe_text
)
rover::Program_strategy = st.builds(
    rover::Program,
    name=
        safe_text
)
rover::Component_strategy = st.builds(
    rover::Component,
    name=
        safe_text
)
rover::Rover_strategy = st.builds(
    rover::Rover,
)

@given(instance=rover::SetLightColor_strategy)
@settings(max_examples=50)
def test_rover::setlightcolor_instantiation(instance):
    assert isinstance(instance, rover::SetLightColor)

@given(instance=rover::SetLightColor_strategy)
def test_rover::setlightcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=rover::SetLightColor_strategy)
def test_rover::setlightcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=rover::Wait_strategy)
@settings(max_examples=50)
def test_rover::wait_instantiation(instance):
    assert isinstance(instance, rover::Wait)

@given(instance=rover::Wait_strategy)
def test_rover::wait_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=rover::Wait_strategy)
def test_rover::wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=rover::PositionQuantity_strategy)
@settings(max_examples=50)
def test_rover::positionquantity_instantiation(instance):
    assert isinstance(instance, rover::PositionQuantity)

@given(instance=rover::SingleQuantity_strategy)
@settings(max_examples=50)
def test_rover::singlequantity_instantiation(instance):
    assert isinstance(instance, rover::SingleQuantity)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=rover::Sensor_strategy)
@settings(max_examples=50)
def test_rover::sensor_instantiation(instance):
    assert isinstance(instance, rover::Sensor)

@given(instance=rover::Move_strategy)
@settings(max_examples=50)
def test_rover::move_instantiation(instance):
    assert isinstance(instance, rover::Move)

@given(instance=rover::Move_strategy)
def test_rover::move_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=rover::Move_strategy)
def test_rover::move_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=rover::Move_strategy)
def test_rover::move_velocity_type(instance):
    assert isinstance(instance.velocity, int)


@given(instance=rover::Move_strategy)
def test_rover::move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=rover::Rotate_strategy)
@settings(max_examples=50)
def test_rover::rotate_instantiation(instance):
    assert isinstance(instance, rover::Rotate)

@given(instance=rover::Rotate_strategy)
def test_rover::rotate_angel_type(instance):
    assert isinstance(instance.angel, int)


@given(instance=rover::Rotate_strategy)
def test_rover::rotate_angel_setter(instance):
    original = instance.angel
    instance.angel = original
    assert instance.angel == original

@given(instance=rover::Repeate_strategy)
@settings(max_examples=50)
def test_rover::repeate_instantiation(instance):
    assert isinstance(instance, rover::Repeate)

@given(instance=rover::Repeate_strategy)
def test_rover::repeate_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=rover::Repeate_strategy)
def test_rover::repeate_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=rover::Command_strategy)
@settings(max_examples=50)
def test_rover::command_instantiation(instance):
    assert isinstance(instance, rover::Command)

@given(instance=rover::Block_strategy)
@settings(max_examples=50)
def test_rover::block_instantiation(instance):
    assert isinstance(instance, rover::Block)

@given(instance=rover::Block_strategy)
def test_rover::block_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rover::Block_strategy)
def test_rover::block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=rover::Light_strategy)
@settings(max_examples=50)
def test_rover::light_instantiation(instance):
    assert isinstance(instance, rover::Light)

@given(instance=rover::Motor_strategy)
@settings(max_examples=50)
def test_rover::motor_instantiation(instance):
    assert isinstance(instance, rover::Motor)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=rover::DistanceSensor_strategy)
@settings(max_examples=50)
def test_rover::distancesensor_instantiation(instance):
    assert isinstance(instance, rover::DistanceSensor)

@given(instance=rover::DistanceSensor_strategy)
def test_rover::distancesensor_remainingDistance_type(instance):
    assert isinstance(instance.remainingDistance, float)


@given(instance=rover::DistanceSensor_strategy)
def test_rover::distancesensor_remainingDistance_setter(instance):
    original = instance.remainingDistance
    instance.remainingDistance = original
    assert instance.remainingDistance == original

@given(instance=rover::directionFacing_strategy)
@settings(max_examples=50)
def test_rover::directionfacing_instantiation(instance):
    assert isinstance(instance, rover::directionFacing)

@given(instance=rover::directionFacing_strategy)
def test_rover::directionfacing_currentlyFacing_type(instance):
    assert isinstance(instance.currentlyFacing, float)


@given(instance=rover::directionFacing_strategy)
def test_rover::directionfacing_currentlyFacing_setter(instance):
    original = instance.currentlyFacing
    instance.currentlyFacing = original
    assert instance.currentlyFacing == original

@given(instance=rover::Compass_strategy)
@settings(max_examples=50)
def test_rover::compass_instantiation(instance):
    assert isinstance(instance, rover::Compass)

@given(instance=rover::GPS_strategy)
@settings(max_examples=50)
def test_rover::gps_instantiation(instance):
    assert isinstance(instance, rover::GPS)

@given(instance=rover::GPS_strategy)
def test_rover::gps_currentPosition_type(instance):
    assert isinstance(instance.currentPosition, float)


@given(instance=rover::GPS_strategy)
def test_rover::gps_currentPosition_setter(instance):
    original = instance.currentPosition
    instance.currentPosition = original
    assert instance.currentPosition == original

@given(instance=rover::Actuator_strategy)
@settings(max_examples=50)
def test_rover::actuator_instantiation(instance):
    assert isinstance(instance, rover::Actuator)

@given(instance=rover::Tansition_strategy)
@settings(max_examples=50)
def test_rover::tansition_instantiation(instance):
    assert isinstance(instance, rover::Tansition)

@given(instance=rover::Tansition_strategy)
def test_rover::tansition_comparedQuantity_type(instance):
    assert isinstance(instance.comparedQuantity, str)


@given(instance=rover::Tansition_strategy)
def test_rover::tansition_comparedQuantity_setter(instance):
    original = instance.comparedQuantity
    instance.comparedQuantity = original
    assert instance.comparedQuantity == original

@given(instance=rover::Tansition_strategy)
def test_rover::tansition_operationUsed_type(instance):
    assert isinstance(instance.operationUsed, str)


@given(instance=rover::Tansition_strategy)
def test_rover::tansition_operationUsed_setter(instance):
    original = instance.operationUsed
    instance.operationUsed = original
    assert instance.operationUsed == original

@given(instance=rover::Program_strategy)
@settings(max_examples=50)
def test_rover::program_instantiation(instance):
    assert isinstance(instance, rover::Program)

@given(instance=rover::Program_strategy)
def test_rover::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rover::Program_strategy)
def test_rover::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rover::Component_strategy)
@settings(max_examples=50)
def test_rover::component_instantiation(instance):
    assert isinstance(instance, rover::Component)

@given(instance=rover::Component_strategy)
def test_rover::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rover::Component_strategy)
def test_rover::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rover::Rover_strategy)
@settings(max_examples=50)
def test_rover::rover_instantiation(instance):
    assert isinstance(instance, rover::Rover)
