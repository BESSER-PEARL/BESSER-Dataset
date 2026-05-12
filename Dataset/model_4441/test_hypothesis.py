import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SingleQuantity,
    Quantity,
    roverml_SingleQuantity,
    roverml_Quantity,
    roverml_Position,
    Triggered,
    roverml_CompassTrigger,
    roverml_GPSTrigger,
    roverml_DistanceSensorTrigger,
    Transition,
    roverml_Regular,
    roverml_Triggered,
    roverml_Angle,
    roverml_Length,
    roverml_Time,
    Command,
    roverml_Terminate,
    roverml_Rotate,
    roverml_Repeat,
    roverml_Wait,
    roverml_Move,
    roverml_SetLightColor,
    roverml_Command,
    roverml_Velocity,
    roverml_Transition,
    Actuator,
    roverml_Light,
    roverml_Motor,
    Sensor,
    roverml_DistanceSensor,
    roverml_Compass,
    roverml_GPS,
    Component,
    roverml_Actuator,
    roverml_Sensor,
    roverml_NamedElement,
    roverml_Block,
    NamedElement,
    roverml_Program,
    roverml_Component,
    roverml_Rover,
    roverml_System,
    LengthUnits,
    AngleUnits,
    Colours,
    TimeUnits,
    VelocityUnits,
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



def test_roverml_singlequantity_is_not_abstract():
    assert not inspect.isabstract(roverml_SingleQuantity)


def test_roverml_singlequantity_constructor_exists():
    assert callable(roverml_SingleQuantity.__init__)


def test_roverml_singlequantity_constructor_args():
    sig = inspect.signature(roverml_SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml_quantity_is_not_abstract():
    assert not inspect.isabstract(roverml_Quantity)


def test_roverml_quantity_constructor_exists():
    assert callable(roverml_Quantity.__init__)


def test_roverml_quantity_constructor_args():
    sig = inspect.signature(roverml_Quantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml_position_is_not_abstract():
    assert not inspect.isabstract(roverml_Position)


def test_roverml_position_constructor_exists():
    assert callable(roverml_Position.__init__)


def test_roverml_position_constructor_args():
    sig = inspect.signature(roverml_Position.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_roverml_position_has_y():
    assert hasattr(roverml_Position, "y")
    descriptor = None
    for klass in roverml_Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_roverml_position_has_x():
    assert hasattr(roverml_Position, "x")
    descriptor = None
    for klass in roverml_Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_triggered_is_not_abstract():
    assert not inspect.isabstract(Triggered)


def test_triggered_constructor_exists():
    assert callable(Triggered.__init__)


def test_triggered_constructor_args():
    sig = inspect.signature(Triggered.__init__)
    params = list(sig.parameters.keys())



def test_roverml_compasstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_CompassTrigger)


def test_roverml_compasstrigger_constructor_exists():
    assert callable(roverml_CompassTrigger.__init__)


def test_roverml_compasstrigger_constructor_args():
    sig = inspect.signature(roverml_CompassTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml_compasstrigger_has_angle():
    assert hasattr(roverml_CompassTrigger, "angle")
    descriptor = None
    for klass in roverml_CompassTrigger.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml_gpstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_GPSTrigger)


def test_roverml_gpstrigger_constructor_exists():
    assert callable(roverml_GPSTrigger.__init__)


def test_roverml_gpstrigger_constructor_args():
    sig = inspect.signature(roverml_GPSTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_roverml_gpstrigger_has_y():
    assert hasattr(roverml_GPSTrigger, "y")
    descriptor = None
    for klass in roverml_GPSTrigger.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_roverml_gpstrigger_has_x():
    assert hasattr(roverml_GPSTrigger, "x")
    descriptor = None
    for klass in roverml_GPSTrigger.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_roverml_distancesensortrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_DistanceSensorTrigger)


def test_roverml_distancesensortrigger_constructor_exists():
    assert callable(roverml_DistanceSensorTrigger.__init__)


def test_roverml_distancesensortrigger_constructor_args():
    sig = inspect.signature(roverml_DistanceSensorTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "dist" in params, "Missing parameter 'dist'"

def test_roverml_distancesensortrigger_has_dist():
    assert hasattr(roverml_DistanceSensorTrigger, "dist")
    descriptor = None
    for klass in roverml_DistanceSensorTrigger.__mro__:
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



def test_roverml_regular_is_not_abstract():
    assert not inspect.isabstract(roverml_Regular)


def test_roverml_regular_constructor_exists():
    assert callable(roverml_Regular.__init__)


def test_roverml_regular_constructor_args():
    sig = inspect.signature(roverml_Regular.__init__)
    params = list(sig.parameters.keys())



def test_roverml_triggered_is_not_abstract():
    assert not inspect.isabstract(roverml_Triggered)


def test_roverml_triggered_constructor_exists():
    assert callable(roverml_Triggered.__init__)


def test_roverml_triggered_constructor_args():
    sig = inspect.signature(roverml_Triggered.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_roverml_triggered_has_operator():
    assert hasattr(roverml_Triggered, "operator")
    descriptor = None
    for klass in roverml_Triggered.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_roverml_angle_is_not_abstract():
    assert not inspect.isabstract(roverml_Angle)


def test_roverml_angle_constructor_exists():
    assert callable(roverml_Angle.__init__)


def test_roverml_angle_constructor_args():
    sig = inspect.signature(roverml_Angle.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml_angle_has_units():
    assert hasattr(roverml_Angle, "units")
    descriptor = None
    for klass in roverml_Angle.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml_length_is_not_abstract():
    assert not inspect.isabstract(roverml_Length)


def test_roverml_length_constructor_exists():
    assert callable(roverml_Length.__init__)


def test_roverml_length_constructor_args():
    sig = inspect.signature(roverml_Length.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml_length_has_units():
    assert hasattr(roverml_Length, "units")
    descriptor = None
    for klass in roverml_Length.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml_time_is_not_abstract():
    assert not inspect.isabstract(roverml_Time)


def test_roverml_time_constructor_exists():
    assert callable(roverml_Time.__init__)


def test_roverml_time_constructor_args():
    sig = inspect.signature(roverml_Time.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml_time_has_units():
    assert hasattr(roverml_Time, "units")
    descriptor = None
    for klass in roverml_Time.__mro__:
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



def test_roverml_terminate_is_not_abstract():
    assert not inspect.isabstract(roverml_Terminate)


def test_roverml_terminate_constructor_exists():
    assert callable(roverml_Terminate.__init__)


def test_roverml_terminate_constructor_args():
    sig = inspect.signature(roverml_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_roverml_rotate_is_not_abstract():
    assert not inspect.isabstract(roverml_Rotate)


def test_roverml_rotate_constructor_exists():
    assert callable(roverml_Rotate.__init__)


def test_roverml_rotate_constructor_args():
    sig = inspect.signature(roverml_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml_rotate_has_angle():
    assert hasattr(roverml_Rotate, "angle")
    descriptor = None
    for klass in roverml_Rotate.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml_repeat_is_not_abstract():
    assert not inspect.isabstract(roverml_Repeat)


def test_roverml_repeat_constructor_exists():
    assert callable(roverml_Repeat.__init__)


def test_roverml_repeat_constructor_args():
    sig = inspect.signature(roverml_Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfReps" in params, "Missing parameter 'numberOfReps'"

def test_roverml_repeat_has_numberOfReps():
    assert hasattr(roverml_Repeat, "numberOfReps")
    descriptor = None
    for klass in roverml_Repeat.__mro__:
        if "numberOfReps" in klass.__dict__:
            descriptor = klass.__dict__["numberOfReps"]
            break
    assert isinstance(descriptor, property)



def test_roverml_wait_is_not_abstract():
    assert not inspect.isabstract(roverml_Wait)


def test_roverml_wait_constructor_exists():
    assert callable(roverml_Wait.__init__)


def test_roverml_wait_constructor_args():
    sig = inspect.signature(roverml_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_roverml_wait_has_time():
    assert hasattr(roverml_Wait, "time")
    descriptor = None
    for klass in roverml_Wait.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_roverml_move_is_not_abstract():
    assert not inspect.isabstract(roverml_Move)


def test_roverml_move_constructor_exists():
    assert callable(roverml_Move.__init__)


def test_roverml_move_constructor_args():
    sig = inspect.signature(roverml_Move.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "length" in params, "Missing parameter 'length'"

def test_roverml_move_has_velocity():
    assert hasattr(roverml_Move, "velocity")
    descriptor = None
    for klass in roverml_Move.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_roverml_move_has_length():
    assert hasattr(roverml_Move, "length")
    descriptor = None
    for klass in roverml_Move.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_roverml_setlightcolor_is_not_abstract():
    assert not inspect.isabstract(roverml_SetLightColor)


def test_roverml_setlightcolor_constructor_exists():
    assert callable(roverml_SetLightColor.__init__)


def test_roverml_setlightcolor_constructor_args():
    sig = inspect.signature(roverml_SetLightColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverml_setlightcolor_has_color():
    assert hasattr(roverml_SetLightColor, "color")
    descriptor = None
    for klass in roverml_SetLightColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverml_command_is_not_abstract():
    assert not inspect.isabstract(roverml_Command)


def test_roverml_command_constructor_exists():
    assert callable(roverml_Command.__init__)


def test_roverml_command_constructor_args():
    sig = inspect.signature(roverml_Command.__init__)
    params = list(sig.parameters.keys())



def test_roverml_velocity_is_not_abstract():
    assert not inspect.isabstract(roverml_Velocity)


def test_roverml_velocity_constructor_exists():
    assert callable(roverml_Velocity.__init__)


def test_roverml_velocity_constructor_args():
    sig = inspect.signature(roverml_Velocity.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"

def test_roverml_velocity_has_units():
    assert hasattr(roverml_Velocity, "units")
    descriptor = None
    for klass in roverml_Velocity.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_roverml_transition_is_not_abstract():
    assert not inspect.isabstract(roverml_Transition)


def test_roverml_transition_constructor_exists():
    assert callable(roverml_Transition.__init__)


def test_roverml_transition_constructor_args():
    sig = inspect.signature(roverml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_roverml_light_is_not_abstract():
    assert not inspect.isabstract(roverml_Light)


def test_roverml_light_constructor_exists():
    assert callable(roverml_Light.__init__)


def test_roverml_light_constructor_args():
    sig = inspect.signature(roverml_Light.__init__)
    params = list(sig.parameters.keys())



def test_roverml_motor_is_not_abstract():
    assert not inspect.isabstract(roverml_Motor)


def test_roverml_motor_constructor_exists():
    assert callable(roverml_Motor.__init__)


def test_roverml_motor_constructor_args():
    sig = inspect.signature(roverml_Motor.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_roverml_distancesensor_is_not_abstract():
    assert not inspect.isabstract(roverml_DistanceSensor)


def test_roverml_distancesensor_constructor_exists():
    assert callable(roverml_DistanceSensor.__init__)


def test_roverml_distancesensor_constructor_args():
    sig = inspect.signature(roverml_DistanceSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_roverml_distancesensor_has_distance():
    assert hasattr(roverml_DistanceSensor, "distance")
    descriptor = None
    for klass in roverml_DistanceSensor.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_roverml_compass_is_not_abstract():
    assert not inspect.isabstract(roverml_Compass)


def test_roverml_compass_constructor_exists():
    assert callable(roverml_Compass.__init__)


def test_roverml_compass_constructor_args():
    sig = inspect.signature(roverml_Compass.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_roverml_compass_has_angle():
    assert hasattr(roverml_Compass, "angle")
    descriptor = None
    for klass in roverml_Compass.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_roverml_gps_is_not_abstract():
    assert not inspect.isabstract(roverml_GPS)


def test_roverml_gps_constructor_exists():
    assert callable(roverml_GPS.__init__)


def test_roverml_gps_constructor_args():
    sig = inspect.signature(roverml_GPS.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_roverml_gps_has_x():
    assert hasattr(roverml_GPS, "x")
    descriptor = None
    for klass in roverml_GPS.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_roverml_gps_has_y():
    assert hasattr(roverml_GPS, "y")
    descriptor = None
    for klass in roverml_GPS.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_roverml_actuator_is_not_abstract():
    assert not inspect.isabstract(roverml_Actuator)


def test_roverml_actuator_constructor_exists():
    assert callable(roverml_Actuator.__init__)


def test_roverml_actuator_constructor_args():
    sig = inspect.signature(roverml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_roverml_sensor_is_not_abstract():
    assert not inspect.isabstract(roverml_Sensor)


def test_roverml_sensor_constructor_exists():
    assert callable(roverml_Sensor.__init__)


def test_roverml_sensor_constructor_args():
    sig = inspect.signature(roverml_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_roverml_namedelement_is_not_abstract():
    assert not inspect.isabstract(roverml_NamedElement)


def test_roverml_namedelement_constructor_exists():
    assert callable(roverml_NamedElement.__init__)


def test_roverml_namedelement_constructor_args():
    sig = inspect.signature(roverml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverml_namedelement_has_name():
    assert hasattr(roverml_NamedElement, "name")
    descriptor = None
    for klass in roverml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverml_block_is_not_abstract():
    assert not inspect.isabstract(roverml_Block)


def test_roverml_block_constructor_exists():
    assert callable(roverml_Block.__init__)


def test_roverml_block_constructor_args():
    sig = inspect.signature(roverml_Block.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_roverml_program_is_not_abstract():
    assert not inspect.isabstract(roverml_Program)


def test_roverml_program_constructor_exists():
    assert callable(roverml_Program.__init__)


def test_roverml_program_constructor_args():
    sig = inspect.signature(roverml_Program.__init__)
    params = list(sig.parameters.keys())



def test_roverml_component_is_not_abstract():
    assert not inspect.isabstract(roverml_Component)


def test_roverml_component_constructor_exists():
    assert callable(roverml_Component.__init__)


def test_roverml_component_constructor_args():
    sig = inspect.signature(roverml_Component.__init__)
    params = list(sig.parameters.keys())



def test_roverml_rover_is_not_abstract():
    assert not inspect.isabstract(roverml_Rover)


def test_roverml_rover_constructor_exists():
    assert callable(roverml_Rover.__init__)


def test_roverml_rover_constructor_args():
    sig = inspect.signature(roverml_Rover.__init__)
    params = list(sig.parameters.keys())



def test_roverml_system_is_not_abstract():
    assert not inspect.isabstract(roverml_System)


def test_roverml_system_constructor_exists():
    assert callable(roverml_System.__init__)


def test_roverml_system_constructor_args():
    sig = inspect.signature(roverml_System.__init__)
    params = list(sig.parameters.keys())

def test_lengthunits_exists():
    # Check that the Enumeration exists
    assert LengthUnits is not None

def test_lengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnits]
    expected_literals = [
        "MILLIMETERS",
        "CENTIMETERS",
        "METERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnits"

def test_angleunits_exists():
    # Check that the Enumeration exists
    assert AngleUnits is not None

def test_angleunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AngleUnits]
    expected_literals = [
        "RADIANS",
        "DEGREES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AngleUnits"

def test_colours_exists():
    # Check that the Enumeration exists
    assert Colours is not None

def test_colours_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colours]
    expected_literals = [
        "NONE",
        "RED",
        "GREEN",
        "BLUE",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colours"

def test_timeunits_exists():
    # Check that the Enumeration exists
    assert TimeUnits is not None

def test_timeunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnits]
    expected_literals = [
        "SECONDS",
        "HOURS",
        "MINUTES",
        "MILLISECONDS",
        "NANOSECONDS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnits"

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
roverml_SingleQuantity_strategy = st.builds(
    roverml_SingleQuantity,
)
roverml_Quantity_strategy = st.builds(
    roverml_Quantity,
)
roverml_Position_strategy = st.builds(
    roverml_Position,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Triggered_strategy = st.builds(
    Triggered,
)
roverml_CompassTrigger_strategy = st.builds(
    roverml_CompassTrigger,
    angle=
        st.integers()
)
roverml_GPSTrigger_strategy = st.builds(
    roverml_GPSTrigger,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_DistanceSensorTrigger_strategy = st.builds(
    roverml_DistanceSensorTrigger,
    dist=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Transition_strategy = st.builds(
    Transition,
)
roverml_Regular_strategy = st.builds(
    roverml_Regular,
)
roverml_Triggered_strategy = st.builds(
    roverml_Triggered,
    operator=
        safe_text
)
roverml_Angle_strategy = st.builds(
    roverml_Angle,
    units=
        safe_text
)
roverml_Length_strategy = st.builds(
    roverml_Length,
    units=
        safe_text
)
roverml_Time_strategy = st.builds(
    roverml_Time,
    units=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
roverml_Terminate_strategy = st.builds(
    roverml_Terminate,
)
roverml_Rotate_strategy = st.builds(
    roverml_Rotate,
    angle=
        st.integers()
)
roverml_Repeat_strategy = st.builds(
    roverml_Repeat,
    numberOfReps=
        st.integers()
)
roverml_Wait_strategy = st.builds(
    roverml_Wait,
    time=
        st.integers()
)
roverml_Move_strategy = st.builds(
    roverml_Move,
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_SetLightColor_strategy = st.builds(
    roverml_SetLightColor,
    color=
        safe_text
)
roverml_Command_strategy = st.builds(
    roverml_Command,
)
roverml_Velocity_strategy = st.builds(
    roverml_Velocity,
    units=
        safe_text
)
roverml_Transition_strategy = st.builds(
    roverml_Transition,
)
Actuator_strategy = st.builds(
    Actuator,
)
roverml_Light_strategy = st.builds(
    roverml_Light,
)
roverml_Motor_strategy = st.builds(
    roverml_Motor,
)
Sensor_strategy = st.builds(
    Sensor,
)
roverml_DistanceSensor_strategy = st.builds(
    roverml_DistanceSensor,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_Compass_strategy = st.builds(
    roverml_Compass,
    angle=
        st.integers()
)
roverml_GPS_strategy = st.builds(
    roverml_GPS,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Component_strategy = st.builds(
    Component,
)
roverml_Actuator_strategy = st.builds(
    roverml_Actuator,
)
roverml_Sensor_strategy = st.builds(
    roverml_Sensor,
)
roverml_NamedElement_strategy = st.builds(
    roverml_NamedElement,
    name=
        safe_text
)
roverml_Block_strategy = st.builds(
    roverml_Block,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
roverml_Program_strategy = st.builds(
    roverml_Program,
)
roverml_Component_strategy = st.builds(
    roverml_Component,
)
roverml_Rover_strategy = st.builds(
    roverml_Rover,
)
roverml_System_strategy = st.builds(
    roverml_System,
)

@given(instance=SingleQuantity_strategy)
@settings(max_examples=50)
def test_singlequantity_instantiation(instance):
    assert isinstance(instance, SingleQuantity)

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=roverml_SingleQuantity_strategy)
@settings(max_examples=50)
def test_roverml_singlequantity_instantiation(instance):
    assert isinstance(instance, roverml_SingleQuantity)

@given(instance=roverml_Quantity_strategy)
@settings(max_examples=50)
def test_roverml_quantity_instantiation(instance):
    assert isinstance(instance, roverml_Quantity)

@given(instance=roverml_Position_strategy)
@settings(max_examples=50)
def test_roverml_position_instantiation(instance):
    assert isinstance(instance, roverml_Position)



@given(instance=roverml_Position_strategy)
def test_roverml_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=roverml_Position_strategy)
def test_roverml_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Triggered_strategy)
@settings(max_examples=50)
def test_triggered_instantiation(instance):
    assert isinstance(instance, Triggered)

@given(instance=roverml_CompassTrigger_strategy)
@settings(max_examples=50)
def test_roverml_compasstrigger_instantiation(instance):
    assert isinstance(instance, roverml_CompassTrigger)



@given(instance=roverml_CompassTrigger_strategy)
def test_roverml_compasstrigger_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml_GPSTrigger_strategy)
@settings(max_examples=50)
def test_roverml_gpstrigger_instantiation(instance):
    assert isinstance(instance, roverml_GPSTrigger)



@given(instance=roverml_GPSTrigger_strategy)
def test_roverml_gpstrigger_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=roverml_GPSTrigger_strategy)
def test_roverml_gpstrigger_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=roverml_DistanceSensorTrigger_strategy)
@settings(max_examples=50)
def test_roverml_distancesensortrigger_instantiation(instance):
    assert isinstance(instance, roverml_DistanceSensorTrigger)



@given(instance=roverml_DistanceSensorTrigger_strategy)
def test_roverml_distancesensortrigger_dist_setter(instance):
    original = instance.dist
    instance.dist = original
    assert instance.dist == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=roverml_Regular_strategy)
@settings(max_examples=50)
def test_roverml_regular_instantiation(instance):
    assert isinstance(instance, roverml_Regular)

@given(instance=roverml_Triggered_strategy)
@settings(max_examples=50)
def test_roverml_triggered_instantiation(instance):
    assert isinstance(instance, roverml_Triggered)



@given(instance=roverml_Triggered_strategy)
def test_roverml_triggered_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=roverml_Angle_strategy)
@settings(max_examples=50)
def test_roverml_angle_instantiation(instance):
    assert isinstance(instance, roverml_Angle)



@given(instance=roverml_Angle_strategy)
def test_roverml_angle_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml_Length_strategy)
@settings(max_examples=50)
def test_roverml_length_instantiation(instance):
    assert isinstance(instance, roverml_Length)



@given(instance=roverml_Length_strategy)
def test_roverml_length_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml_Time_strategy)
@settings(max_examples=50)
def test_roverml_time_instantiation(instance):
    assert isinstance(instance, roverml_Time)



@given(instance=roverml_Time_strategy)
def test_roverml_time_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=roverml_Terminate_strategy)
@settings(max_examples=50)
def test_roverml_terminate_instantiation(instance):
    assert isinstance(instance, roverml_Terminate)

@given(instance=roverml_Rotate_strategy)
@settings(max_examples=50)
def test_roverml_rotate_instantiation(instance):
    assert isinstance(instance, roverml_Rotate)



@given(instance=roverml_Rotate_strategy)
def test_roverml_rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml_Repeat_strategy)
@settings(max_examples=50)
def test_roverml_repeat_instantiation(instance):
    assert isinstance(instance, roverml_Repeat)



@given(instance=roverml_Repeat_strategy)
def test_roverml_repeat_numberOfReps_setter(instance):
    original = instance.numberOfReps
    instance.numberOfReps = original
    assert instance.numberOfReps == original

@given(instance=roverml_Wait_strategy)
@settings(max_examples=50)
def test_roverml_wait_instantiation(instance):
    assert isinstance(instance, roverml_Wait)



@given(instance=roverml_Wait_strategy)
def test_roverml_wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=roverml_Move_strategy)
@settings(max_examples=50)
def test_roverml_move_instantiation(instance):
    assert isinstance(instance, roverml_Move)



@given(instance=roverml_Move_strategy)
def test_roverml_move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original



@given(instance=roverml_Move_strategy)
def test_roverml_move_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=roverml_SetLightColor_strategy)
@settings(max_examples=50)
def test_roverml_setlightcolor_instantiation(instance):
    assert isinstance(instance, roverml_SetLightColor)



@given(instance=roverml_SetLightColor_strategy)
def test_roverml_setlightcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverml_Command_strategy)
@settings(max_examples=50)
def test_roverml_command_instantiation(instance):
    assert isinstance(instance, roverml_Command)

@given(instance=roverml_Velocity_strategy)
@settings(max_examples=50)
def test_roverml_velocity_instantiation(instance):
    assert isinstance(instance, roverml_Velocity)



@given(instance=roverml_Velocity_strategy)
def test_roverml_velocity_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=roverml_Transition_strategy)
@settings(max_examples=50)
def test_roverml_transition_instantiation(instance):
    assert isinstance(instance, roverml_Transition)

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=roverml_Light_strategy)
@settings(max_examples=50)
def test_roverml_light_instantiation(instance):
    assert isinstance(instance, roverml_Light)

@given(instance=roverml_Motor_strategy)
@settings(max_examples=50)
def test_roverml_motor_instantiation(instance):
    assert isinstance(instance, roverml_Motor)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=roverml_DistanceSensor_strategy)
@settings(max_examples=50)
def test_roverml_distancesensor_instantiation(instance):
    assert isinstance(instance, roverml_DistanceSensor)



@given(instance=roverml_DistanceSensor_strategy)
def test_roverml_distancesensor_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=roverml_Compass_strategy)
@settings(max_examples=50)
def test_roverml_compass_instantiation(instance):
    assert isinstance(instance, roverml_Compass)



@given(instance=roverml_Compass_strategy)
def test_roverml_compass_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=roverml_GPS_strategy)
@settings(max_examples=50)
def test_roverml_gps_instantiation(instance):
    assert isinstance(instance, roverml_GPS)



@given(instance=roverml_GPS_strategy)
def test_roverml_gps_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=roverml_GPS_strategy)
def test_roverml_gps_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=roverml_Actuator_strategy)
@settings(max_examples=50)
def test_roverml_actuator_instantiation(instance):
    assert isinstance(instance, roverml_Actuator)

@given(instance=roverml_Sensor_strategy)
@settings(max_examples=50)
def test_roverml_sensor_instantiation(instance):
    assert isinstance(instance, roverml_Sensor)

@given(instance=roverml_NamedElement_strategy)
@settings(max_examples=50)
def test_roverml_namedelement_instantiation(instance):
    assert isinstance(instance, roverml_NamedElement)



@given(instance=roverml_NamedElement_strategy)
def test_roverml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverml_Block_strategy)
@settings(max_examples=50)
def test_roverml_block_instantiation(instance):
    assert isinstance(instance, roverml_Block)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=roverml_Program_strategy)
@settings(max_examples=50)
def test_roverml_program_instantiation(instance):
    assert isinstance(instance, roverml_Program)

@given(instance=roverml_Component_strategy)
@settings(max_examples=50)
def test_roverml_component_instantiation(instance):
    assert isinstance(instance, roverml_Component)

@given(instance=roverml_Rover_strategy)
@settings(max_examples=50)
def test_roverml_rover_instantiation(instance):
    assert isinstance(instance, roverml_Rover)

@given(instance=roverml_System_strategy)
@settings(max_examples=50)
def test_roverml_system_instantiation(instance):
    assert isinstance(instance, roverml_System)
