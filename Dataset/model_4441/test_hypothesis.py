import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SingleQuantity,
    Quantity,
    roverml::SingleQuantity,
    roverml::Quantity,
    roverml::Position,
    Triggered,
    roverml::GPSTrigger,
    roverml::CompassTrigger,
    roverml::DistanceSensorTrigger,
    Transition,
    roverml::Regular,
    roverml::Triggered,
    roverml::Angle,
    roverml::Length,
    roverml::Time,
    Command,
    roverml::Repeat,
    roverml::Wait,
    roverml::Rotate,
    roverml::Terminate,
    roverml::Move,
    roverml::SetLightColor,
    roverml::Command,
    roverml::Velocity,
    roverml::Transition,
    Actuator,
    roverml::Light,
    roverml::Motor,
    Sensor,
    roverml::Compass,
    roverml::DistanceSensor,
    roverml::GPS,
    Component,
    roverml::Actuator,
    roverml::Sensor,
    roverml::NamedElement,
    roverml::Block,
    NamedElement,
    roverml::Program,
    roverml::Component,
    roverml::Rover,
    roverml::System,
    AngleUnits,
    VelocityUnits,
    LengthUnits,
    TimeUnits,
    Colours,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_singlequantity_is_not_abstract():
    assert not inspect.isabstract(SingleQuantity)


def test_singlequantity_constructor_exists():
    assert callable(SingleQuantity.__init__)


def test_singlequantity_constructor_args():
    sig = inspect.signature(SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::singlequantity_is_not_abstract():
    assert not inspect.isabstract(roverml::SingleQuantity)


def test_roverml::singlequantity_constructor_exists():
    assert callable(roverml::SingleQuantity.__init__)


def test_roverml::singlequantity_constructor_args():
    sig = inspect.signature(roverml::SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::quantity_is_not_abstract():
    assert not inspect.isabstract(roverml::Quantity)


def test_roverml::quantity_constructor_exists():
    assert callable(roverml::Quantity.__init__)


def test_roverml::quantity_constructor_args():
    sig = inspect.signature(roverml::Quantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::position_is_not_abstract():
    assert not inspect.isabstract(roverml::Position)


def test_roverml::position_constructor_exists():
    assert callable(roverml::Position.__init__)


def test_roverml::position_constructor_args():
    sig = inspect.signature(roverml::Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_roverml::position_has_x():
    assert hasattr(roverml::Position, "x")
    descriptor = None
    for klass in roverml::Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_roverml::position_has_y():
    assert hasattr(roverml::Position, "y")
    descriptor = None
    for klass in roverml::Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_triggered_is_not_abstract():
    assert not inspect.isabstract(Triggered)


def test_triggered_constructor_exists():
    assert callable(Triggered.__init__)


def test_triggered_constructor_args():
    sig = inspect.signature(Triggered.__init__)
    params = list(sig.parameters.keys())



def test_roverml::gpstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::GPSTrigger)


def test_roverml::gpstrigger_constructor_exists():
    assert callable(roverml::GPSTrigger.__init__)


def test_roverml::gpstrigger_constructor_args():
    sig = inspect.signature(roverml::GPSTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_roverml::gpstrigger_has_y():
    assert hasattr(roverml::GPSTrigger, "y")
    descriptor = None
    for klass in roverml::GPSTrigger.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_roverml::gpstrigger_has_x():
    assert hasattr(roverml::GPSTrigger, "x")
    descriptor = None
    for klass in roverml::GPSTrigger.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_roverml::compasstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::CompassTrigger)


def test_roverml::compasstrigger_constructor_exists():
    assert callable(roverml::CompassTrigger.__init__)


def test_roverml::compasstrigger_constructor_args():
    sig = inspect.signature(roverml::CompassTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml::compasstrigger_has_angle():
    assert hasattr(roverml::CompassTrigger, "angle")
    descriptor = None
    for klass in roverml::CompassTrigger.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml::distancesensortrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::DistanceSensorTrigger)


def test_roverml::distancesensortrigger_constructor_exists():
    assert callable(roverml::DistanceSensorTrigger.__init__)


def test_roverml::distancesensortrigger_constructor_args():
    sig = inspect.signature(roverml::DistanceSensorTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "dist" in params, "Missing parameter 'dist'"

def test_roverml::distancesensortrigger_has_dist():
    assert hasattr(roverml::DistanceSensorTrigger, "dist")
    descriptor = None
    for klass in roverml::DistanceSensorTrigger.__mro__:
        if "dist" in klass.__dict__:
            descriptor = klass.__dict__["dist"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_roverml::regular_is_not_abstract():
    assert not inspect.isabstract(roverml::Regular)


def test_roverml::regular_constructor_exists():
    assert callable(roverml::Regular.__init__)


def test_roverml::regular_constructor_args():
    sig = inspect.signature(roverml::Regular.__init__)
    params = list(sig.parameters.keys())



def test_roverml::triggered_is_not_abstract():
    assert not inspect.isabstract(roverml::Triggered)


def test_roverml::triggered_constructor_exists():
    assert callable(roverml::Triggered.__init__)


def test_roverml::triggered_constructor_args():
    sig = inspect.signature(roverml::Triggered.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_roverml::triggered_has_operator():
    assert hasattr(roverml::Triggered, "operator")
    descriptor = None
    for klass in roverml::Triggered.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_roverml::angle_is_not_abstract():
    assert not inspect.isabstract(roverml::Angle)


def test_roverml::angle_constructor_exists():
    assert callable(roverml::Angle.__init__)


def test_roverml::angle_constructor_args():
    sig = inspect.signature(roverml::Angle.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml::angle_has_units():
    assert hasattr(roverml::Angle, "units")
    descriptor = None
    for klass in roverml::Angle.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml::length_is_not_abstract():
    assert not inspect.isabstract(roverml::Length)


def test_roverml::length_constructor_exists():
    assert callable(roverml::Length.__init__)


def test_roverml::length_constructor_args():
    sig = inspect.signature(roverml::Length.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml::length_has_units():
    assert hasattr(roverml::Length, "units")
    descriptor = None
    for klass in roverml::Length.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml::time_is_not_abstract():
    assert not inspect.isabstract(roverml::Time)


def test_roverml::time_constructor_exists():
    assert callable(roverml::Time.__init__)


def test_roverml::time_constructor_args():
    sig = inspect.signature(roverml::Time.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml::time_has_units():
    assert hasattr(roverml::Time, "units")
    descriptor = None
    for klass in roverml::Time.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_roverml::repeat_is_not_abstract():
    assert not inspect.isabstract(roverml::Repeat)


def test_roverml::repeat_constructor_exists():
    assert callable(roverml::Repeat.__init__)


def test_roverml::repeat_constructor_args():
    sig = inspect.signature(roverml::Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfReps" in params, "Missing parameter 'numberOfReps'"

def test_roverml::repeat_has_numberOfReps():
    assert hasattr(roverml::Repeat, "numberOfReps")
    descriptor = None
    for klass in roverml::Repeat.__mro__:
        if "numberOfReps" in klass.__dict__:
            descriptor = klass.__dict__["numberOfReps"]
            break
    assert isinstance(descriptor, property)



def test_roverml::wait_is_not_abstract():
    assert not inspect.isabstract(roverml::Wait)


def test_roverml::wait_constructor_exists():
    assert callable(roverml::Wait.__init__)


def test_roverml::wait_constructor_args():
    sig = inspect.signature(roverml::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_roverml::wait_has_time():
    assert hasattr(roverml::Wait, "time")
    descriptor = None
    for klass in roverml::Wait.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_roverml::rotate_is_not_abstract():
    assert not inspect.isabstract(roverml::Rotate)


def test_roverml::rotate_constructor_exists():
    assert callable(roverml::Rotate.__init__)


def test_roverml::rotate_constructor_args():
    sig = inspect.signature(roverml::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml::rotate_has_angle():
    assert hasattr(roverml::Rotate, "angle")
    descriptor = None
    for klass in roverml::Rotate.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml::terminate_is_not_abstract():
    assert not inspect.isabstract(roverml::Terminate)


def test_roverml::terminate_constructor_exists():
    assert callable(roverml::Terminate.__init__)


def test_roverml::terminate_constructor_args():
    sig = inspect.signature(roverml::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_roverml::move_is_not_abstract():
    assert not inspect.isabstract(roverml::Move)


def test_roverml::move_constructor_exists():
    assert callable(roverml::Move.__init__)


def test_roverml::move_constructor_args():
    sig = inspect.signature(roverml::Move.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "length" in params, "Missing parameter 'length'"

def test_roverml::move_has_velocity():
    assert hasattr(roverml::Move, "velocity")
    descriptor = None
    for klass in roverml::Move.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_roverml::move_has_length():
    assert hasattr(roverml::Move, "length")
    descriptor = None
    for klass in roverml::Move.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_roverml::setlightcolor_is_not_abstract():
    assert not inspect.isabstract(roverml::SetLightColor)


def test_roverml::setlightcolor_constructor_exists():
    assert callable(roverml::SetLightColor.__init__)


def test_roverml::setlightcolor_constructor_args():
    sig = inspect.signature(roverml::SetLightColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverml::setlightcolor_has_color():
    assert hasattr(roverml::SetLightColor, "color")
    descriptor = None
    for klass in roverml::SetLightColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverml::command_is_not_abstract():
    assert not inspect.isabstract(roverml::Command)


def test_roverml::command_constructor_exists():
    assert callable(roverml::Command.__init__)


def test_roverml::command_constructor_args():
    sig = inspect.signature(roverml::Command.__init__)
    params = list(sig.parameters.keys())



def test_roverml::velocity_is_not_abstract():
    assert not inspect.isabstract(roverml::Velocity)


def test_roverml::velocity_constructor_exists():
    assert callable(roverml::Velocity.__init__)


def test_roverml::velocity_constructor_args():
    sig = inspect.signature(roverml::Velocity.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml::velocity_has_units():
    assert hasattr(roverml::Velocity, "units")
    descriptor = None
    for klass in roverml::Velocity.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml::transition_is_not_abstract():
    assert not inspect.isabstract(roverml::Transition)


def test_roverml::transition_constructor_exists():
    assert callable(roverml::Transition.__init__)


def test_roverml::transition_constructor_args():
    sig = inspect.signature(roverml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_roverml::light_is_not_abstract():
    assert not inspect.isabstract(roverml::Light)


def test_roverml::light_constructor_exists():
    assert callable(roverml::Light.__init__)


def test_roverml::light_constructor_args():
    sig = inspect.signature(roverml::Light.__init__)
    params = list(sig.parameters.keys())



def test_roverml::motor_is_not_abstract():
    assert not inspect.isabstract(roverml::Motor)


def test_roverml::motor_constructor_exists():
    assert callable(roverml::Motor.__init__)


def test_roverml::motor_constructor_args():
    sig = inspect.signature(roverml::Motor.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_roverml::compass_is_not_abstract():
    assert not inspect.isabstract(roverml::Compass)


def test_roverml::compass_constructor_exists():
    assert callable(roverml::Compass.__init__)


def test_roverml::compass_constructor_args():
    sig = inspect.signature(roverml::Compass.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml::compass_has_angle():
    assert hasattr(roverml::Compass, "angle")
    descriptor = None
    for klass in roverml::Compass.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml::distancesensor_is_not_abstract():
    assert not inspect.isabstract(roverml::DistanceSensor)


def test_roverml::distancesensor_constructor_exists():
    assert callable(roverml::DistanceSensor.__init__)


def test_roverml::distancesensor_constructor_args():
    sig = inspect.signature(roverml::DistanceSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_roverml::distancesensor_has_distance():
    assert hasattr(roverml::DistanceSensor, "distance")
    descriptor = None
    for klass in roverml::DistanceSensor.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_roverml::gps_is_not_abstract():
    assert not inspect.isabstract(roverml::GPS)


def test_roverml::gps_constructor_exists():
    assert callable(roverml::GPS.__init__)


def test_roverml::gps_constructor_args():
    sig = inspect.signature(roverml::GPS.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_roverml::gps_has_y():
    assert hasattr(roverml::GPS, "y")
    descriptor = None
    for klass in roverml::GPS.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_roverml::gps_has_x():
    assert hasattr(roverml::GPS, "x")
    descriptor = None
    for klass in roverml::GPS.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_roverml::actuator_is_not_abstract():
    assert not inspect.isabstract(roverml::Actuator)


def test_roverml::actuator_constructor_exists():
    assert callable(roverml::Actuator.__init__)


def test_roverml::actuator_constructor_args():
    sig = inspect.signature(roverml::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_roverml::sensor_is_not_abstract():
    assert not inspect.isabstract(roverml::Sensor)


def test_roverml::sensor_constructor_exists():
    assert callable(roverml::Sensor.__init__)


def test_roverml::sensor_constructor_args():
    sig = inspect.signature(roverml::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_roverml::namedelement_is_not_abstract():
    assert not inspect.isabstract(roverml::NamedElement)


def test_roverml::namedelement_constructor_exists():
    assert callable(roverml::NamedElement.__init__)


def test_roverml::namedelement_constructor_args():
    sig = inspect.signature(roverml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverml::namedelement_has_name():
    assert hasattr(roverml::NamedElement, "name")
    descriptor = None
    for klass in roverml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverml::block_is_not_abstract():
    assert not inspect.isabstract(roverml::Block)


def test_roverml::block_constructor_exists():
    assert callable(roverml::Block.__init__)


def test_roverml::block_constructor_args():
    sig = inspect.signature(roverml::Block.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_roverml::program_is_not_abstract():
    assert not inspect.isabstract(roverml::Program)


def test_roverml::program_constructor_exists():
    assert callable(roverml::Program.__init__)


def test_roverml::program_constructor_args():
    sig = inspect.signature(roverml::Program.__init__)
    params = list(sig.parameters.keys())



def test_roverml::component_is_not_abstract():
    assert not inspect.isabstract(roverml::Component)


def test_roverml::component_constructor_exists():
    assert callable(roverml::Component.__init__)


def test_roverml::component_constructor_args():
    sig = inspect.signature(roverml::Component.__init__)
    params = list(sig.parameters.keys())



def test_roverml::rover_is_not_abstract():
    assert not inspect.isabstract(roverml::Rover)


def test_roverml::rover_constructor_exists():
    assert callable(roverml::Rover.__init__)


def test_roverml::rover_constructor_args():
    sig = inspect.signature(roverml::Rover.__init__)
    params = list(sig.parameters.keys())



def test_roverml::system_is_not_abstract():
    assert not inspect.isabstract(roverml::System)


def test_roverml::system_constructor_exists():
    assert callable(roverml::System.__init__)


def test_roverml::system_constructor_args():
    sig = inspect.signature(roverml::System.__init__)
    params = list(sig.parameters.keys())

def test_angleunits_exists():
    # Check that the Enumeration exists
    assert AngleUnits is not None

def test_angleunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AngleUnits]
    expected_literals = [
        "DEGREES",
        "RADIANS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AngleUnits"

def test_velocityunits_exists():
    # Check that the Enumeration exists
    assert VelocityUnits is not None

def test_velocityunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VelocityUnits]
    expected_literals = [
        "MILLIMETERS_PER_SECOND",
        "CENTIMETERS_PER_SECOND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VelocityUnits"

def test_lengthunits_exists():
    # Check that the Enumeration exists
    assert LengthUnits is not None

def test_lengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnits]
    expected_literals = [
        "MILLIMETERS",
        "METERS",
        "CENTIMETERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnits"

def test_timeunits_exists():
    # Check that the Enumeration exists
    assert TimeUnits is not None

def test_timeunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnits]
    expected_literals = [
        "SECONDS",
        "NANOSECONDS",
        "MINUTES",
        "HOURS",
        "MILLISECONDS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnits"

def test_colours_exists():
    # Check that the Enumeration exists
    assert Colours is not None

def test_colours_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colours]
    expected_literals = [
        "GREEN",
        "BLUE",
        "RED",
        "NONE",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colours"


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
SingleQuantity_strategy = st.builds(
    SingleQuantity,
)
Quantity_strategy = st.builds(
    Quantity,
)
roverml::SingleQuantity_strategy = st.builds(
    roverml::SingleQuantity,
)
roverml::Quantity_strategy = st.builds(
    roverml::Quantity,
)
roverml::Position_strategy = st.builds(
    roverml::Position,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Triggered_strategy = st.builds(
    Triggered,
)
roverml::GPSTrigger_strategy = st.builds(
    roverml::GPSTrigger,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml::CompassTrigger_strategy = st.builds(
    roverml::CompassTrigger,
    angle=
        st.integers()
)
roverml::DistanceSensorTrigger_strategy = st.builds(
    roverml::DistanceSensorTrigger,
    dist=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Transition_strategy = st.builds(
    Transition,
)
roverml::Regular_strategy = st.builds(
    roverml::Regular,
)
roverml::Triggered_strategy = st.builds(
    roverml::Triggered,
    operator=
        safe_text
)
roverml::Angle_strategy = st.builds(
    roverml::Angle,
    units=
        safe_text
)
roverml::Length_strategy = st.builds(
    roverml::Length,
    units=
        safe_text
)
roverml::Time_strategy = st.builds(
    roverml::Time,
    units=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
roverml::Repeat_strategy = st.builds(
    roverml::Repeat,
    numberOfReps=
        st.integers()
)
roverml::Wait_strategy = st.builds(
    roverml::Wait,
    time=
        st.integers()
)
roverml::Rotate_strategy = st.builds(
    roverml::Rotate,
    angle=
        st.integers()
)
roverml::Terminate_strategy = st.builds(
    roverml::Terminate,
)
roverml::Move_strategy = st.builds(
    roverml::Move,
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml::SetLightColor_strategy = st.builds(
    roverml::SetLightColor,
    color=
        safe_text
)
roverml::Command_strategy = st.builds(
    roverml::Command,
)
roverml::Velocity_strategy = st.builds(
    roverml::Velocity,
    units=
        safe_text
)
roverml::Transition_strategy = st.builds(
    roverml::Transition,
)
Actuator_strategy = st.builds(
    Actuator,
)
roverml::Light_strategy = st.builds(
    roverml::Light,
)
roverml::Motor_strategy = st.builds(
    roverml::Motor,
)
Sensor_strategy = st.builds(
    Sensor,
)
roverml::Compass_strategy = st.builds(
    roverml::Compass,
    angle=
        st.integers()
)
roverml::DistanceSensor_strategy = st.builds(
    roverml::DistanceSensor,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml::GPS_strategy = st.builds(
    roverml::GPS,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Component_strategy = st.builds(
    Component,
)
roverml::Actuator_strategy = st.builds(
    roverml::Actuator,
)
roverml::Sensor_strategy = st.builds(
    roverml::Sensor,
)
roverml::NamedElement_strategy = st.builds(
    roverml::NamedElement,
    name=
        safe_text
)
roverml::Block_strategy = st.builds(
    roverml::Block,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
roverml::Program_strategy = st.builds(
    roverml::Program,
)
roverml::Component_strategy = st.builds(
    roverml::Component,
)
roverml::Rover_strategy = st.builds(
    roverml::Rover,
)
roverml::System_strategy = st.builds(
    roverml::System,
)

@given(instance=SingleQuantity_strategy)
@settings(max_examples=50)
def test_singlequantity_instantiation(instance):
    assert isinstance(instance, SingleQuantity)

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=roverml::SingleQuantity_strategy)
@settings(max_examples=50)
def test_roverml::singlequantity_instantiation(instance):
    assert isinstance(instance, roverml::SingleQuantity)

@given(instance=roverml::Quantity_strategy)
@settings(max_examples=50)
def test_roverml::quantity_instantiation(instance):
    assert isinstance(instance, roverml::Quantity)

@given(instance=roverml::Position_strategy)
@settings(max_examples=50)
def test_roverml::position_instantiation(instance):
    assert isinstance(instance, roverml::Position)

@given(instance=roverml::Position_strategy)
def test_roverml::position_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=roverml::Position_strategy)
def test_roverml::position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=roverml::Position_strategy)
def test_roverml::position_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=roverml::Position_strategy)
def test_roverml::position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Triggered_strategy)
@settings(max_examples=50)
def test_triggered_instantiation(instance):
    assert isinstance(instance, Triggered)

@given(instance=roverml::GPSTrigger_strategy)
@settings(max_examples=50)
def test_roverml::gpstrigger_instantiation(instance):
    assert isinstance(instance, roverml::GPSTrigger)

@given(instance=roverml::GPSTrigger_strategy)
def test_roverml::gpstrigger_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=roverml::GPSTrigger_strategy)
def test_roverml::gpstrigger_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=roverml::GPSTrigger_strategy)
def test_roverml::gpstrigger_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=roverml::GPSTrigger_strategy)
def test_roverml::gpstrigger_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=roverml::CompassTrigger_strategy)
@settings(max_examples=50)
def test_roverml::compasstrigger_instantiation(instance):
    assert isinstance(instance, roverml::CompassTrigger)

@given(instance=roverml::CompassTrigger_strategy)
def test_roverml::compasstrigger_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=roverml::CompassTrigger_strategy)
def test_roverml::compasstrigger_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml::DistanceSensorTrigger_strategy)
@settings(max_examples=50)
def test_roverml::distancesensortrigger_instantiation(instance):
    assert isinstance(instance, roverml::DistanceSensorTrigger)

@given(instance=roverml::DistanceSensorTrigger_strategy)
def test_roverml::distancesensortrigger_dist_type(instance):
    assert isinstance(instance.dist, float)


@given(instance=roverml::DistanceSensorTrigger_strategy)
def test_roverml::distancesensortrigger_dist_setter(instance):
    original = instance.dist
    instance.dist = original
    assert instance.dist == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=roverml::Regular_strategy)
@settings(max_examples=50)
def test_roverml::regular_instantiation(instance):
    assert isinstance(instance, roverml::Regular)

@given(instance=roverml::Triggered_strategy)
@settings(max_examples=50)
def test_roverml::triggered_instantiation(instance):
    assert isinstance(instance, roverml::Triggered)

@given(instance=roverml::Triggered_strategy)
def test_roverml::triggered_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=roverml::Triggered_strategy)
def test_roverml::triggered_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=roverml::Angle_strategy)
@settings(max_examples=50)
def test_roverml::angle_instantiation(instance):
    assert isinstance(instance, roverml::Angle)

@given(instance=roverml::Angle_strategy)
def test_roverml::angle_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=roverml::Angle_strategy)
def test_roverml::angle_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml::Length_strategy)
@settings(max_examples=50)
def test_roverml::length_instantiation(instance):
    assert isinstance(instance, roverml::Length)

@given(instance=roverml::Length_strategy)
def test_roverml::length_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=roverml::Length_strategy)
def test_roverml::length_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml::Time_strategy)
@settings(max_examples=50)
def test_roverml::time_instantiation(instance):
    assert isinstance(instance, roverml::Time)

@given(instance=roverml::Time_strategy)
def test_roverml::time_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=roverml::Time_strategy)
def test_roverml::time_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=roverml::Repeat_strategy)
@settings(max_examples=50)
def test_roverml::repeat_instantiation(instance):
    assert isinstance(instance, roverml::Repeat)

@given(instance=roverml::Repeat_strategy)
def test_roverml::repeat_numberOfReps_type(instance):
    assert isinstance(instance.numberOfReps, int)


@given(instance=roverml::Repeat_strategy)
def test_roverml::repeat_numberOfReps_setter(instance):
    original = instance.numberOfReps
    instance.numberOfReps = original
    assert instance.numberOfReps == original

@given(instance=roverml::Wait_strategy)
@settings(max_examples=50)
def test_roverml::wait_instantiation(instance):
    assert isinstance(instance, roverml::Wait)

@given(instance=roverml::Wait_strategy)
def test_roverml::wait_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=roverml::Wait_strategy)
def test_roverml::wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=roverml::Rotate_strategy)
@settings(max_examples=50)
def test_roverml::rotate_instantiation(instance):
    assert isinstance(instance, roverml::Rotate)

@given(instance=roverml::Rotate_strategy)
def test_roverml::rotate_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=roverml::Rotate_strategy)
def test_roverml::rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml::Terminate_strategy)
@settings(max_examples=50)
def test_roverml::terminate_instantiation(instance):
    assert isinstance(instance, roverml::Terminate)

@given(instance=roverml::Move_strategy)
@settings(max_examples=50)
def test_roverml::move_instantiation(instance):
    assert isinstance(instance, roverml::Move)

@given(instance=roverml::Move_strategy)
def test_roverml::move_velocity_type(instance):
    assert isinstance(instance.velocity, float)


@given(instance=roverml::Move_strategy)
def test_roverml::move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=roverml::Move_strategy)
def test_roverml::move_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=roverml::Move_strategy)
def test_roverml::move_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=roverml::SetLightColor_strategy)
@settings(max_examples=50)
def test_roverml::setlightcolor_instantiation(instance):
    assert isinstance(instance, roverml::SetLightColor)

@given(instance=roverml::SetLightColor_strategy)
def test_roverml::setlightcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=roverml::SetLightColor_strategy)
def test_roverml::setlightcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverml::Command_strategy)
@settings(max_examples=50)
def test_roverml::command_instantiation(instance):
    assert isinstance(instance, roverml::Command)

@given(instance=roverml::Velocity_strategy)
@settings(max_examples=50)
def test_roverml::velocity_instantiation(instance):
    assert isinstance(instance, roverml::Velocity)

@given(instance=roverml::Velocity_strategy)
def test_roverml::velocity_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=roverml::Velocity_strategy)
def test_roverml::velocity_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml::Transition_strategy)
@settings(max_examples=50)
def test_roverml::transition_instantiation(instance):
    assert isinstance(instance, roverml::Transition)

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=roverml::Light_strategy)
@settings(max_examples=50)
def test_roverml::light_instantiation(instance):
    assert isinstance(instance, roverml::Light)

@given(instance=roverml::Motor_strategy)
@settings(max_examples=50)
def test_roverml::motor_instantiation(instance):
    assert isinstance(instance, roverml::Motor)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=roverml::Compass_strategy)
@settings(max_examples=50)
def test_roverml::compass_instantiation(instance):
    assert isinstance(instance, roverml::Compass)

@given(instance=roverml::Compass_strategy)
def test_roverml::compass_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=roverml::Compass_strategy)
def test_roverml::compass_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml::DistanceSensor_strategy)
@settings(max_examples=50)
def test_roverml::distancesensor_instantiation(instance):
    assert isinstance(instance, roverml::DistanceSensor)

@given(instance=roverml::DistanceSensor_strategy)
def test_roverml::distancesensor_distance_type(instance):
    assert isinstance(instance.distance, float)


@given(instance=roverml::DistanceSensor_strategy)
def test_roverml::distancesensor_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=roverml::GPS_strategy)
@settings(max_examples=50)
def test_roverml::gps_instantiation(instance):
    assert isinstance(instance, roverml::GPS)

@given(instance=roverml::GPS_strategy)
def test_roverml::gps_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=roverml::GPS_strategy)
def test_roverml::gps_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=roverml::GPS_strategy)
def test_roverml::gps_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=roverml::GPS_strategy)
def test_roverml::gps_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=roverml::Actuator_strategy)
@settings(max_examples=50)
def test_roverml::actuator_instantiation(instance):
    assert isinstance(instance, roverml::Actuator)

@given(instance=roverml::Sensor_strategy)
@settings(max_examples=50)
def test_roverml::sensor_instantiation(instance):
    assert isinstance(instance, roverml::Sensor)

@given(instance=roverml::NamedElement_strategy)
@settings(max_examples=50)
def test_roverml::namedelement_instantiation(instance):
    assert isinstance(instance, roverml::NamedElement)

@given(instance=roverml::NamedElement_strategy)
def test_roverml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=roverml::NamedElement_strategy)
def test_roverml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverml::Block_strategy)
@settings(max_examples=50)
def test_roverml::block_instantiation(instance):
    assert isinstance(instance, roverml::Block)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=roverml::Program_strategy)
@settings(max_examples=50)
def test_roverml::program_instantiation(instance):
    assert isinstance(instance, roverml::Program)

@given(instance=roverml::Component_strategy)
@settings(max_examples=50)
def test_roverml::component_instantiation(instance):
    assert isinstance(instance, roverml::Component)

@given(instance=roverml::Rover_strategy)
@settings(max_examples=50)
def test_roverml::rover_instantiation(instance):
    assert isinstance(instance, roverml::Rover)

@given(instance=roverml::System_strategy)
@settings(max_examples=50)
def test_roverml::system_instantiation(instance):
    assert isinstance(instance, roverml::System)
