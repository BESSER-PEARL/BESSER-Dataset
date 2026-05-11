import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    roverml::Quantity,
    roverml::CompassTrigger,
    roverml::GpsTrigger,
    roverml::DistanceSensorTrigger,
    Actuator,
    SingleQuantity,
    roverml::RoverSystem,
    roverml::Motor,
    Component,
    roverml::Actuator,
    roverml::Sensor,
    Transition,
    roverml::TriggeredTransition,
    Quantity,
    roverml::Position,
    roverml::SingleQuantity,
    roverml::Compass,
    roverml::DistanceSensor,
    roverml::GPS,
    roverml::Time,
    roverml::Angle,
    roverml::Light,
    roverml::Length,
    roverml::Velocity,
    Command,
    roverml::Rotate,
    roverml::Terminate,
    roverml::SetLightColor,
    roverml::Wait,
    roverml::Move,
    Block,
    roverml::Repeat,
    NamedElement,
    roverml::Component,
    roverml::RoverProgram,
    roverml::NamedElement,
    roverml::Transition,
    roverml::Command,
    roverml::Rover,
    roverml::Block,
    LengthUnit,
    VelocityUnit,
    TimeUnit,
    ComparisonOperator,
    Color,
    AngleUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_roverml::quantity_is_not_abstract():
    assert not inspect.isabstract(roverml::Quantity)


def test_roverml::quantity_constructor_exists():
    assert callable(roverml::Quantity.__init__)


def test_roverml::quantity_constructor_args():
    sig = inspect.signature(roverml::Quantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::compasstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::CompassTrigger)


def test_roverml::compasstrigger_constructor_exists():
    assert callable(roverml::CompassTrigger.__init__)


def test_roverml::compasstrigger_constructor_args():
    sig = inspect.signature(roverml::CompassTrigger.__init__)
    params = list(sig.parameters.keys())



def test_roverml::gpstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::GpsTrigger)


def test_roverml::gpstrigger_constructor_exists():
    assert callable(roverml::GpsTrigger.__init__)


def test_roverml::gpstrigger_constructor_args():
    sig = inspect.signature(roverml::GpsTrigger.__init__)
    params = list(sig.parameters.keys())



def test_roverml::distancesensortrigger_is_not_abstract():
    assert not inspect.isabstract(roverml::DistanceSensorTrigger)


def test_roverml::distancesensortrigger_constructor_exists():
    assert callable(roverml::DistanceSensorTrigger.__init__)


def test_roverml::distancesensortrigger_constructor_args():
    sig = inspect.signature(roverml::DistanceSensorTrigger.__init__)
    params = list(sig.parameters.keys())



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_singlequantity_is_not_abstract():
    assert not inspect.isabstract(SingleQuantity)


def test_singlequantity_constructor_exists():
    assert callable(SingleQuantity.__init__)


def test_singlequantity_constructor_args():
    sig = inspect.signature(SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::roversystem_is_not_abstract():
    assert not inspect.isabstract(roverml::RoverSystem)


def test_roverml::roversystem_constructor_exists():
    assert callable(roverml::RoverSystem.__init__)


def test_roverml::roversystem_constructor_args():
    sig = inspect.signature(roverml::RoverSystem.__init__)
    params = list(sig.parameters.keys())



def test_roverml::motor_is_not_abstract():
    assert not inspect.isabstract(roverml::Motor)


def test_roverml::motor_constructor_exists():
    assert callable(roverml::Motor.__init__)


def test_roverml::motor_constructor_args():
    sig = inspect.signature(roverml::Motor.__init__)
    params = list(sig.parameters.keys())



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



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_roverml::triggeredtransition_is_not_abstract():
    assert not inspect.isabstract(roverml::TriggeredTransition)


def test_roverml::triggeredtransition_constructor_exists():
    assert callable(roverml::TriggeredTransition.__init__)


def test_roverml::triggeredtransition_constructor_args():
    sig = inspect.signature(roverml::TriggeredTransition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_roverml::triggeredtransition_has_operator():
    assert hasattr(roverml::TriggeredTransition, "operator")
    descriptor = None
    for klass in roverml::TriggeredTransition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_roverml::position_is_not_abstract():
    assert not inspect.isabstract(roverml::Position)


def test_roverml::position_constructor_exists():
    assert callable(roverml::Position.__init__)


def test_roverml::position_constructor_args():
    sig = inspect.signature(roverml::Position.__init__)
    params = list(sig.parameters.keys())



def test_roverml::singlequantity_is_not_abstract():
    assert not inspect.isabstract(roverml::SingleQuantity)


def test_roverml::singlequantity_constructor_exists():
    assert callable(roverml::SingleQuantity.__init__)


def test_roverml::singlequantity_constructor_args():
    sig = inspect.signature(roverml::SingleQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_roverml::singlequantity_has_value():
    assert hasattr(roverml::SingleQuantity, "value")
    descriptor = None
    for klass in roverml::SingleQuantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_roverml::compass_is_not_abstract():
    assert not inspect.isabstract(roverml::Compass)


def test_roverml::compass_constructor_exists():
    assert callable(roverml::Compass.__init__)


def test_roverml::compass_constructor_args():
    sig = inspect.signature(roverml::Compass.__init__)
    params = list(sig.parameters.keys())



def test_roverml::distancesensor_is_not_abstract():
    assert not inspect.isabstract(roverml::DistanceSensor)


def test_roverml::distancesensor_constructor_exists():
    assert callable(roverml::DistanceSensor.__init__)


def test_roverml::distancesensor_constructor_args():
    sig = inspect.signature(roverml::DistanceSensor.__init__)
    params = list(sig.parameters.keys())



def test_roverml::gps_is_not_abstract():
    assert not inspect.isabstract(roverml::GPS)


def test_roverml::gps_constructor_exists():
    assert callable(roverml::GPS.__init__)


def test_roverml::gps_constructor_args():
    sig = inspect.signature(roverml::GPS.__init__)
    params = list(sig.parameters.keys())



def test_roverml::time_is_not_abstract():
    assert not inspect.isabstract(roverml::Time)


def test_roverml::time_constructor_exists():
    assert callable(roverml::Time.__init__)


def test_roverml::time_constructor_args():
    sig = inspect.signature(roverml::Time.__init__)
    params = list(sig.parameters.keys())
    assert "timeUnit" in params, "Missing parameter 'timeUnit'"

def test_roverml::time_has_timeUnit():
    assert hasattr(roverml::Time, "timeUnit")
    descriptor = None
    for klass in roverml::Time.__mro__:
        if "timeUnit" in klass.__dict__:
            descriptor = klass.__dict__["timeUnit"]
            break
    assert isinstance(descriptor, property)



def test_roverml::angle_is_not_abstract():
    assert not inspect.isabstract(roverml::Angle)


def test_roverml::angle_constructor_exists():
    assert callable(roverml::Angle.__init__)


def test_roverml::angle_constructor_args():
    sig = inspect.signature(roverml::Angle.__init__)
    params = list(sig.parameters.keys())
    assert "angleUnit" in params, "Missing parameter 'angleUnit'"

def test_roverml::angle_has_angleUnit():
    assert hasattr(roverml::Angle, "angleUnit")
    descriptor = None
    for klass in roverml::Angle.__mro__:
        if "angleUnit" in klass.__dict__:
            descriptor = klass.__dict__["angleUnit"]
            break
    assert isinstance(descriptor, property)



def test_roverml::light_is_not_abstract():
    assert not inspect.isabstract(roverml::Light)


def test_roverml::light_constructor_exists():
    assert callable(roverml::Light.__init__)


def test_roverml::light_constructor_args():
    sig = inspect.signature(roverml::Light.__init__)
    params = list(sig.parameters.keys())



def test_roverml::length_is_not_abstract():
    assert not inspect.isabstract(roverml::Length)


def test_roverml::length_constructor_exists():
    assert callable(roverml::Length.__init__)


def test_roverml::length_constructor_args():
    sig = inspect.signature(roverml::Length.__init__)
    params = list(sig.parameters.keys())
    assert "lengthUnit" in params, "Missing parameter 'lengthUnit'"

def test_roverml::length_has_lengthUnit():
    assert hasattr(roverml::Length, "lengthUnit")
    descriptor = None
    for klass in roverml::Length.__mro__:
        if "lengthUnit" in klass.__dict__:
            descriptor = klass.__dict__["lengthUnit"]
            break
    assert isinstance(descriptor, property)



def test_roverml::velocity_is_not_abstract():
    assert not inspect.isabstract(roverml::Velocity)


def test_roverml::velocity_constructor_exists():
    assert callable(roverml::Velocity.__init__)


def test_roverml::velocity_constructor_args():
    sig = inspect.signature(roverml::Velocity.__init__)
    params = list(sig.parameters.keys())
    assert "velocityUnit" in params, "Missing parameter 'velocityUnit'"

def test_roverml::velocity_has_velocityUnit():
    assert hasattr(roverml::Velocity, "velocityUnit")
    descriptor = None
    for klass in roverml::Velocity.__mro__:
        if "velocityUnit" in klass.__dict__:
            descriptor = klass.__dict__["velocityUnit"]
            break
    assert isinstance(descriptor, property)



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_roverml::rotate_is_not_abstract():
    assert not inspect.isabstract(roverml::Rotate)


def test_roverml::rotate_constructor_exists():
    assert callable(roverml::Rotate.__init__)


def test_roverml::rotate_constructor_args():
    sig = inspect.signature(roverml::Rotate.__init__)
    params = list(sig.parameters.keys())



def test_roverml::terminate_is_not_abstract():
    assert not inspect.isabstract(roverml::Terminate)


def test_roverml::terminate_constructor_exists():
    assert callable(roverml::Terminate.__init__)


def test_roverml::terminate_constructor_args():
    sig = inspect.signature(roverml::Terminate.__init__)
    params = list(sig.parameters.keys())



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



def test_roverml::wait_is_not_abstract():
    assert not inspect.isabstract(roverml::Wait)


def test_roverml::wait_constructor_exists():
    assert callable(roverml::Wait.__init__)


def test_roverml::wait_constructor_args():
    sig = inspect.signature(roverml::Wait.__init__)
    params = list(sig.parameters.keys())



def test_roverml::move_is_not_abstract():
    assert not inspect.isabstract(roverml::Move)


def test_roverml::move_constructor_exists():
    assert callable(roverml::Move.__init__)


def test_roverml::move_constructor_args():
    sig = inspect.signature(roverml::Move.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_roverml::repeat_is_not_abstract():
    assert not inspect.isabstract(roverml::Repeat)


def test_roverml::repeat_constructor_exists():
    assert callable(roverml::Repeat.__init__)


def test_roverml::repeat_constructor_args():
    sig = inspect.signature(roverml::Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_roverml::repeat_has_count():
    assert hasattr(roverml::Repeat, "count")
    descriptor = None
    for klass in roverml::Repeat.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_roverml::component_is_not_abstract():
    assert not inspect.isabstract(roverml::Component)


def test_roverml::component_constructor_exists():
    assert callable(roverml::Component.__init__)


def test_roverml::component_constructor_args():
    sig = inspect.signature(roverml::Component.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_roverml::component_has_kind():
    assert hasattr(roverml::Component, "kind")
    descriptor = None
    for klass in roverml::Component.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_roverml::roverprogram_is_not_abstract():
    assert not inspect.isabstract(roverml::RoverProgram)


def test_roverml::roverprogram_constructor_exists():
    assert callable(roverml::RoverProgram.__init__)


def test_roverml::roverprogram_constructor_args():
    sig = inspect.signature(roverml::RoverProgram.__init__)
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



def test_roverml::transition_is_not_abstract():
    assert not inspect.isabstract(roverml::Transition)


def test_roverml::transition_constructor_exists():
    assert callable(roverml::Transition.__init__)


def test_roverml::transition_constructor_args():
    sig = inspect.signature(roverml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_roverml::command_is_not_abstract():
    assert not inspect.isabstract(roverml::Command)


def test_roverml::command_constructor_exists():
    assert callable(roverml::Command.__init__)


def test_roverml::command_constructor_args():
    sig = inspect.signature(roverml::Command.__init__)
    params = list(sig.parameters.keys())



def test_roverml::rover_is_not_abstract():
    assert not inspect.isabstract(roverml::Rover)


def test_roverml::rover_constructor_exists():
    assert callable(roverml::Rover.__init__)


def test_roverml::rover_constructor_args():
    sig = inspect.signature(roverml::Rover.__init__)
    params = list(sig.parameters.keys())



def test_roverml::block_is_not_abstract():
    assert not inspect.isabstract(roverml::Block)


def test_roverml::block_constructor_exists():
    assert callable(roverml::Block.__init__)


def test_roverml::block_constructor_args():
    sig = inspect.signature(roverml::Block.__init__)
    params = list(sig.parameters.keys())

def test_lengthunit_exists():
    # Check that the Enumeration exists
    assert LengthUnit is not None

def test_lengthunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnit]
    expected_literals = [
        "m",
        "mm",
        "cm",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnit"

def test_velocityunit_exists():
    # Check that the Enumeration exists
    assert VelocityUnit is not None

def test_velocityunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VelocityUnit]
    expected_literals = [
        "cm_per_s",
        "mm_per_s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VelocityUnit"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "h",
        "ns",
        "s",
        "min",
        "ms",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "equals",
        "unequal",
        "smaller",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "blue",
        "yellow",
        "red",
        "none",
        "green",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_angleunit_exists():
    # Check that the Enumeration exists
    assert AngleUnit is not None

def test_angleunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AngleUnit]
    expected_literals = [
        "degree",
        "radian",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AngleUnit"


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
roverml::Quantity_strategy = st.builds(
    roverml::Quantity,
)
roverml::CompassTrigger_strategy = st.builds(
    roverml::CompassTrigger,
)
roverml::GpsTrigger_strategy = st.builds(
    roverml::GpsTrigger,
)
roverml::DistanceSensorTrigger_strategy = st.builds(
    roverml::DistanceSensorTrigger,
)
Actuator_strategy = st.builds(
    Actuator,
)
SingleQuantity_strategy = st.builds(
    SingleQuantity,
)
roverml::RoverSystem_strategy = st.builds(
    roverml::RoverSystem,
)
roverml::Motor_strategy = st.builds(
    roverml::Motor,
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
Transition_strategy = st.builds(
    Transition,
)
roverml::TriggeredTransition_strategy = st.builds(
    roverml::TriggeredTransition,
    operator=
        safe_text
)
Quantity_strategy = st.builds(
    Quantity,
)
roverml::Position_strategy = st.builds(
    roverml::Position,
)
roverml::SingleQuantity_strategy = st.builds(
    roverml::SingleQuantity,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml::Compass_strategy = st.builds(
    roverml::Compass,
)
roverml::DistanceSensor_strategy = st.builds(
    roverml::DistanceSensor,
)
roverml::GPS_strategy = st.builds(
    roverml::GPS,
)
roverml::Time_strategy = st.builds(
    roverml::Time,
    timeUnit=
        safe_text
)
roverml::Angle_strategy = st.builds(
    roverml::Angle,
    angleUnit=
        safe_text
)
roverml::Light_strategy = st.builds(
    roverml::Light,
)
roverml::Length_strategy = st.builds(
    roverml::Length,
    lengthUnit=
        safe_text
)
roverml::Velocity_strategy = st.builds(
    roverml::Velocity,
    velocityUnit=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
roverml::Rotate_strategy = st.builds(
    roverml::Rotate,
)
roverml::Terminate_strategy = st.builds(
    roverml::Terminate,
)
roverml::SetLightColor_strategy = st.builds(
    roverml::SetLightColor,
    color=
        safe_text
)
roverml::Wait_strategy = st.builds(
    roverml::Wait,
)
roverml::Move_strategy = st.builds(
    roverml::Move,
)
Block_strategy = st.builds(
    Block,
)
roverml::Repeat_strategy = st.builds(
    roverml::Repeat,
    count=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
roverml::Component_strategy = st.builds(
    roverml::Component,
    kind=
        safe_text
)
roverml::RoverProgram_strategy = st.builds(
    roverml::RoverProgram,
)
roverml::NamedElement_strategy = st.builds(
    roverml::NamedElement,
    name=
        safe_text
)
roverml::Transition_strategy = st.builds(
    roverml::Transition,
)
roverml::Command_strategy = st.builds(
    roverml::Command,
)
roverml::Rover_strategy = st.builds(
    roverml::Rover,
)
roverml::Block_strategy = st.builds(
    roverml::Block,
)

@given(instance=roverml::Quantity_strategy)
@settings(max_examples=50)
def test_roverml::quantity_instantiation(instance):
    assert isinstance(instance, roverml::Quantity)

@given(instance=roverml::CompassTrigger_strategy)
@settings(max_examples=50)
def test_roverml::compasstrigger_instantiation(instance):
    assert isinstance(instance, roverml::CompassTrigger)

@given(instance=roverml::GpsTrigger_strategy)
@settings(max_examples=50)
def test_roverml::gpstrigger_instantiation(instance):
    assert isinstance(instance, roverml::GpsTrigger)

@given(instance=roverml::DistanceSensorTrigger_strategy)
@settings(max_examples=50)
def test_roverml::distancesensortrigger_instantiation(instance):
    assert isinstance(instance, roverml::DistanceSensorTrigger)

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=SingleQuantity_strategy)
@settings(max_examples=50)
def test_singlequantity_instantiation(instance):
    assert isinstance(instance, SingleQuantity)

@given(instance=roverml::RoverSystem_strategy)
@settings(max_examples=50)
def test_roverml::roversystem_instantiation(instance):
    assert isinstance(instance, roverml::RoverSystem)

@given(instance=roverml::Motor_strategy)
@settings(max_examples=50)
def test_roverml::motor_instantiation(instance):
    assert isinstance(instance, roverml::Motor)

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

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=roverml::TriggeredTransition_strategy)
@settings(max_examples=50)
def test_roverml::triggeredtransition_instantiation(instance):
    assert isinstance(instance, roverml::TriggeredTransition)

@given(instance=roverml::TriggeredTransition_strategy)
def test_roverml::triggeredtransition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=roverml::TriggeredTransition_strategy)
def test_roverml::triggeredtransition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=roverml::Position_strategy)
@settings(max_examples=50)
def test_roverml::position_instantiation(instance):
    assert isinstance(instance, roverml::Position)

@given(instance=roverml::SingleQuantity_strategy)
@settings(max_examples=50)
def test_roverml::singlequantity_instantiation(instance):
    assert isinstance(instance, roverml::SingleQuantity)

@given(instance=roverml::SingleQuantity_strategy)
def test_roverml::singlequantity_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=roverml::SingleQuantity_strategy)
def test_roverml::singlequantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=roverml::Compass_strategy)
@settings(max_examples=50)
def test_roverml::compass_instantiation(instance):
    assert isinstance(instance, roverml::Compass)

@given(instance=roverml::DistanceSensor_strategy)
@settings(max_examples=50)
def test_roverml::distancesensor_instantiation(instance):
    assert isinstance(instance, roverml::DistanceSensor)

@given(instance=roverml::GPS_strategy)
@settings(max_examples=50)
def test_roverml::gps_instantiation(instance):
    assert isinstance(instance, roverml::GPS)

@given(instance=roverml::Time_strategy)
@settings(max_examples=50)
def test_roverml::time_instantiation(instance):
    assert isinstance(instance, roverml::Time)

@given(instance=roverml::Time_strategy)
def test_roverml::time_timeUnit_type(instance):
    assert isinstance(instance.timeUnit, str)


@given(instance=roverml::Time_strategy)
def test_roverml::time_timeUnit_setter(instance):
    original = instance.timeUnit
    instance.timeUnit = original
    assert instance.timeUnit == original

@given(instance=roverml::Angle_strategy)
@settings(max_examples=50)
def test_roverml::angle_instantiation(instance):
    assert isinstance(instance, roverml::Angle)

@given(instance=roverml::Angle_strategy)
def test_roverml::angle_angleUnit_type(instance):
    assert isinstance(instance.angleUnit, str)


@given(instance=roverml::Angle_strategy)
def test_roverml::angle_angleUnit_setter(instance):
    original = instance.angleUnit
    instance.angleUnit = original
    assert instance.angleUnit == original

@given(instance=roverml::Light_strategy)
@settings(max_examples=50)
def test_roverml::light_instantiation(instance):
    assert isinstance(instance, roverml::Light)

@given(instance=roverml::Length_strategy)
@settings(max_examples=50)
def test_roverml::length_instantiation(instance):
    assert isinstance(instance, roverml::Length)

@given(instance=roverml::Length_strategy)
def test_roverml::length_lengthUnit_type(instance):
    assert isinstance(instance.lengthUnit, str)


@given(instance=roverml::Length_strategy)
def test_roverml::length_lengthUnit_setter(instance):
    original = instance.lengthUnit
    instance.lengthUnit = original
    assert instance.lengthUnit == original

@given(instance=roverml::Velocity_strategy)
@settings(max_examples=50)
def test_roverml::velocity_instantiation(instance):
    assert isinstance(instance, roverml::Velocity)

@given(instance=roverml::Velocity_strategy)
def test_roverml::velocity_velocityUnit_type(instance):
    assert isinstance(instance.velocityUnit, str)


@given(instance=roverml::Velocity_strategy)
def test_roverml::velocity_velocityUnit_setter(instance):
    original = instance.velocityUnit
    instance.velocityUnit = original
    assert instance.velocityUnit == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=roverml::Rotate_strategy)
@settings(max_examples=50)
def test_roverml::rotate_instantiation(instance):
    assert isinstance(instance, roverml::Rotate)

@given(instance=roverml::Terminate_strategy)
@settings(max_examples=50)
def test_roverml::terminate_instantiation(instance):
    assert isinstance(instance, roverml::Terminate)

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

@given(instance=roverml::Wait_strategy)
@settings(max_examples=50)
def test_roverml::wait_instantiation(instance):
    assert isinstance(instance, roverml::Wait)

@given(instance=roverml::Move_strategy)
@settings(max_examples=50)
def test_roverml::move_instantiation(instance):
    assert isinstance(instance, roverml::Move)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=roverml::Repeat_strategy)
@settings(max_examples=50)
def test_roverml::repeat_instantiation(instance):
    assert isinstance(instance, roverml::Repeat)

@given(instance=roverml::Repeat_strategy)
def test_roverml::repeat_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=roverml::Repeat_strategy)
def test_roverml::repeat_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=roverml::Component_strategy)
@settings(max_examples=50)
def test_roverml::component_instantiation(instance):
    assert isinstance(instance, roverml::Component)

@given(instance=roverml::Component_strategy)
def test_roverml::component_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=roverml::Component_strategy)
def test_roverml::component_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=roverml::RoverProgram_strategy)
@settings(max_examples=50)
def test_roverml::roverprogram_instantiation(instance):
    assert isinstance(instance, roverml::RoverProgram)

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

@given(instance=roverml::Transition_strategy)
@settings(max_examples=50)
def test_roverml::transition_instantiation(instance):
    assert isinstance(instance, roverml::Transition)

@given(instance=roverml::Command_strategy)
@settings(max_examples=50)
def test_roverml::command_instantiation(instance):
    assert isinstance(instance, roverml::Command)

@given(instance=roverml::Rover_strategy)
@settings(max_examples=50)
def test_roverml::rover_instantiation(instance):
    assert isinstance(instance, roverml::Rover)

@given(instance=roverml::Block_strategy)
@settings(max_examples=50)
def test_roverml::block_instantiation(instance):
    assert isinstance(instance, roverml::Block)
