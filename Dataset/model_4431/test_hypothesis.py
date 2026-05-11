import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Behavior,
    gyro::StatusChange,
    gyro::Sequential,
    gyro::Parallel,
    gyro::Priority,
    Node,
    Actuate,
    gyro::LED,
    gyro::Servo,
    gyro::Motor,
    Condition,
    gyro::Bumpers,
    gyro::Waiting,
    gyro::Distance,
    Action,
    gyro::Actuate,
    gyro::Condition,
    gyro::Action,
    gyro::Node,
    gyro::GyroSpecification,
    gyro::Behavior,
    gyro::Sibling,
    gyro::Child,
    BumperKind,
    FailureState,
    SuccessState,
    LightStatus,
    RunningState,
    DistanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_gyro::statuschange_is_not_abstract():
    assert not inspect.isabstract(gyro::StatusChange)


def test_gyro::statuschange_constructor_exists():
    assert callable(gyro::StatusChange.__init__)


def test_gyro::statuschange_constructor_args():
    sig = inspect.signature(gyro::StatusChange.__init__)
    params = list(sig.parameters.keys())
    assert "changeSuccess" in params, "Missing parameter 'changeSuccess'"
    assert "changeFailure" in params, "Missing parameter 'changeFailure'"
    assert "changeRunning" in params, "Missing parameter 'changeRunning'"

def test_gyro::statuschange_has_changeSuccess():
    assert hasattr(gyro::StatusChange, "changeSuccess")
    descriptor = None
    for klass in gyro::StatusChange.__mro__:
        if "changeSuccess" in klass.__dict__:
            descriptor = klass.__dict__["changeSuccess"]
            break
    assert isinstance(descriptor, property)

def test_gyro::statuschange_has_changeFailure():
    assert hasattr(gyro::StatusChange, "changeFailure")
    descriptor = None
    for klass in gyro::StatusChange.__mro__:
        if "changeFailure" in klass.__dict__:
            descriptor = klass.__dict__["changeFailure"]
            break
    assert isinstance(descriptor, property)

def test_gyro::statuschange_has_changeRunning():
    assert hasattr(gyro::StatusChange, "changeRunning")
    descriptor = None
    for klass in gyro::StatusChange.__mro__:
        if "changeRunning" in klass.__dict__:
            descriptor = klass.__dict__["changeRunning"]
            break
    assert isinstance(descriptor, property)



def test_gyro::sequential_is_not_abstract():
    assert not inspect.isabstract(gyro::Sequential)


def test_gyro::sequential_constructor_exists():
    assert callable(gyro::Sequential.__init__)


def test_gyro::sequential_constructor_args():
    sig = inspect.signature(gyro::Sequential.__init__)
    params = list(sig.parameters.keys())



def test_gyro::parallel_is_not_abstract():
    assert not inspect.isabstract(gyro::Parallel)


def test_gyro::parallel_constructor_exists():
    assert callable(gyro::Parallel.__init__)


def test_gyro::parallel_constructor_args():
    sig = inspect.signature(gyro::Parallel.__init__)
    params = list(sig.parameters.keys())



def test_gyro::priority_is_not_abstract():
    assert not inspect.isabstract(gyro::Priority)


def test_gyro::priority_constructor_exists():
    assert callable(gyro::Priority.__init__)


def test_gyro::priority_constructor_args():
    sig = inspect.signature(gyro::Priority.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_actuate_is_not_abstract():
    assert not inspect.isabstract(Actuate)


def test_actuate_constructor_exists():
    assert callable(Actuate.__init__)


def test_actuate_constructor_args():
    sig = inspect.signature(Actuate.__init__)
    params = list(sig.parameters.keys())



def test_gyro::led_is_not_abstract():
    assert not inspect.isabstract(gyro::LED)


def test_gyro::led_constructor_exists():
    assert callable(gyro::LED.__init__)


def test_gyro::led_constructor_args():
    sig = inspect.signature(gyro::LED.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_gyro::led_has_status():
    assert hasattr(gyro::LED, "status")
    descriptor = None
    for klass in gyro::LED.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_gyro::servo_is_not_abstract():
    assert not inspect.isabstract(gyro::Servo)


def test_gyro::servo_constructor_exists():
    assert callable(gyro::Servo.__init__)


def test_gyro::servo_constructor_args():
    sig = inspect.signature(gyro::Servo.__init__)
    params = list(sig.parameters.keys())
    assert "minimalPosition" in params, "Missing parameter 'minimalPosition'"
    assert "step" in params, "Missing parameter 'step'"
    assert "maximalPosition" in params, "Missing parameter 'maximalPosition'"

def test_gyro::servo_has_minimalPosition():
    assert hasattr(gyro::Servo, "minimalPosition")
    descriptor = None
    for klass in gyro::Servo.__mro__:
        if "minimalPosition" in klass.__dict__:
            descriptor = klass.__dict__["minimalPosition"]
            break
    assert isinstance(descriptor, property)

def test_gyro::servo_has_step():
    assert hasattr(gyro::Servo, "step")
    descriptor = None
    for klass in gyro::Servo.__mro__:
        if "step" in klass.__dict__:
            descriptor = klass.__dict__["step"]
            break
    assert isinstance(descriptor, property)

def test_gyro::servo_has_maximalPosition():
    assert hasattr(gyro::Servo, "maximalPosition")
    descriptor = None
    for klass in gyro::Servo.__mro__:
        if "maximalPosition" in klass.__dict__:
            descriptor = klass.__dict__["maximalPosition"]
            break
    assert isinstance(descriptor, property)



def test_gyro::motor_is_not_abstract():
    assert not inspect.isabstract(gyro::Motor)


def test_gyro::motor_constructor_exists():
    assert callable(gyro::Motor.__init__)


def test_gyro::motor_constructor_args():
    sig = inspect.signature(gyro::Motor.__init__)
    params = list(sig.parameters.keys())
    assert "rightMotor" in params, "Missing parameter 'rightMotor'"
    assert "leftMotor" in params, "Missing parameter 'leftMotor'"

def test_gyro::motor_has_rightMotor():
    assert hasattr(gyro::Motor, "rightMotor")
    descriptor = None
    for klass in gyro::Motor.__mro__:
        if "rightMotor" in klass.__dict__:
            descriptor = klass.__dict__["rightMotor"]
            break
    assert isinstance(descriptor, property)

def test_gyro::motor_has_leftMotor():
    assert hasattr(gyro::Motor, "leftMotor")
    descriptor = None
    for klass in gyro::Motor.__mro__:
        if "leftMotor" in klass.__dict__:
            descriptor = klass.__dict__["leftMotor"]
            break
    assert isinstance(descriptor, property)



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_gyro::bumpers_is_not_abstract():
    assert not inspect.isabstract(gyro::Bumpers)


def test_gyro::bumpers_constructor_exists():
    assert callable(gyro::Bumpers.__init__)


def test_gyro::bumpers_constructor_args():
    sig = inspect.signature(gyro::Bumpers.__init__)
    params = list(sig.parameters.keys())
    assert "bumperKind" in params, "Missing parameter 'bumperKind'"

def test_gyro::bumpers_has_bumperKind():
    assert hasattr(gyro::Bumpers, "bumperKind")
    descriptor = None
    for klass in gyro::Bumpers.__mro__:
        if "bumperKind" in klass.__dict__:
            descriptor = klass.__dict__["bumperKind"]
            break
    assert isinstance(descriptor, property)



def test_gyro::waiting_is_not_abstract():
    assert not inspect.isabstract(gyro::Waiting)


def test_gyro::waiting_constructor_exists():
    assert callable(gyro::Waiting.__init__)


def test_gyro::waiting_constructor_args():
    sig = inspect.signature(gyro::Waiting.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_gyro::waiting_has_time():
    assert hasattr(gyro::Waiting, "time")
    descriptor = None
    for klass in gyro::Waiting.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_gyro::distance_is_not_abstract():
    assert not inspect.isabstract(gyro::Distance)


def test_gyro::distance_constructor_exists():
    assert callable(gyro::Distance.__init__)


def test_gyro::distance_constructor_args():
    sig = inspect.signature(gyro::Distance.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "value" in params, "Missing parameter 'value'"

def test_gyro::distance_has_kind():
    assert hasattr(gyro::Distance, "kind")
    descriptor = None
    for klass in gyro::Distance.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_gyro::distance_has_value():
    assert hasattr(gyro::Distance, "value")
    descriptor = None
    for klass in gyro::Distance.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_gyro::actuate_is_not_abstract():
    assert not inspect.isabstract(gyro::Actuate)


def test_gyro::actuate_constructor_exists():
    assert callable(gyro::Actuate.__init__)


def test_gyro::actuate_constructor_args():
    sig = inspect.signature(gyro::Actuate.__init__)
    params = list(sig.parameters.keys())



def test_gyro::condition_is_not_abstract():
    assert not inspect.isabstract(gyro::Condition)


def test_gyro::condition_constructor_exists():
    assert callable(gyro::Condition.__init__)


def test_gyro::condition_constructor_args():
    sig = inspect.signature(gyro::Condition.__init__)
    params = list(sig.parameters.keys())



def test_gyro::action_is_not_abstract():
    assert not inspect.isabstract(gyro::Action)


def test_gyro::action_constructor_exists():
    assert callable(gyro::Action.__init__)


def test_gyro::action_constructor_args():
    sig = inspect.signature(gyro::Action.__init__)
    params = list(sig.parameters.keys())



def test_gyro::node_is_not_abstract():
    assert not inspect.isabstract(gyro::Node)


def test_gyro::node_constructor_exists():
    assert callable(gyro::Node.__init__)


def test_gyro::node_constructor_args():
    sig = inspect.signature(gyro::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gyro::node_has_name():
    assert hasattr(gyro::Node, "name")
    descriptor = None
    for klass in gyro::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gyro::gyrospecification_is_not_abstract():
    assert not inspect.isabstract(gyro::GyroSpecification)


def test_gyro::gyrospecification_constructor_exists():
    assert callable(gyro::GyroSpecification.__init__)


def test_gyro::gyrospecification_constructor_args():
    sig = inspect.signature(gyro::GyroSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gyro::gyrospecification_has_name():
    assert hasattr(gyro::GyroSpecification, "name")
    descriptor = None
    for klass in gyro::GyroSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gyro::behavior_is_not_abstract():
    assert not inspect.isabstract(gyro::Behavior)


def test_gyro::behavior_constructor_exists():
    assert callable(gyro::Behavior.__init__)


def test_gyro::behavior_constructor_args():
    sig = inspect.signature(gyro::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_gyro::sibling_is_not_abstract():
    assert not inspect.isabstract(gyro::Sibling)


def test_gyro::sibling_constructor_exists():
    assert callable(gyro::Sibling.__init__)


def test_gyro::sibling_constructor_args():
    sig = inspect.signature(gyro::Sibling.__init__)
    params = list(sig.parameters.keys())



def test_gyro::child_is_not_abstract():
    assert not inspect.isabstract(gyro::Child)


def test_gyro::child_constructor_exists():
    assert callable(gyro::Child.__init__)


def test_gyro::child_constructor_args():
    sig = inspect.signature(gyro::Child.__init__)
    params = list(sig.parameters.keys())

def test_bumperkind_exists():
    # Check that the Enumeration exists
    assert BumperKind is not None

def test_bumperkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BumperKind]
    expected_literals = [
        "Left",
        "Right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BumperKind"

def test_failurestate_exists():
    # Check that the Enumeration exists
    assert FailureState is not None

def test_failurestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FailureState]
    expected_literals = [
        "Success",
        "Failure",
        "Running",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FailureState"

def test_successstate_exists():
    # Check that the Enumeration exists
    assert SuccessState is not None

def test_successstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuccessState]
    expected_literals = [
        "Running",
        "Failure",
        "Success",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuccessState"

def test_lightstatus_exists():
    # Check that the Enumeration exists
    assert LightStatus is not None

def test_lightstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LightStatus]
    expected_literals = [
        "On",
        "Off",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LightStatus"

def test_runningstate_exists():
    # Check that the Enumeration exists
    assert RunningState is not None

def test_runningstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RunningState]
    expected_literals = [
        "Failure",
        "Running",
        "Success",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RunningState"

def test_distancekind_exists():
    # Check that the Enumeration exists
    assert DistanceKind is not None

def test_distancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DistanceKind]
    expected_literals = [
        "Major",
        "Minor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DistanceKind"


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
Behavior_strategy = st.builds(
    Behavior,
)
gyro::StatusChange_strategy = st.builds(
    gyro::StatusChange,
    changeSuccess=
        safe_text,
    changeFailure=
        safe_text,
    changeRunning=
        safe_text
)
gyro::Sequential_strategy = st.builds(
    gyro::Sequential,
)
gyro::Parallel_strategy = st.builds(
    gyro::Parallel,
)
gyro::Priority_strategy = st.builds(
    gyro::Priority,
)
Node_strategy = st.builds(
    Node,
)
Actuate_strategy = st.builds(
    Actuate,
)
gyro::LED_strategy = st.builds(
    gyro::LED,
    status=
        safe_text
)
gyro::Servo_strategy = st.builds(
    gyro::Servo,
    minimalPosition=
        st.integers(),
    step=
        st.integers(),
    maximalPosition=
        st.integers()
)
gyro::Motor_strategy = st.builds(
    gyro::Motor,
    rightMotor=
        st.integers(),
    leftMotor=
        st.integers()
)
Condition_strategy = st.builds(
    Condition,
)
gyro::Bumpers_strategy = st.builds(
    gyro::Bumpers,
    bumperKind=
        safe_text
)
gyro::Waiting_strategy = st.builds(
    gyro::Waiting,
    time=
        st.integers()
)
gyro::Distance_strategy = st.builds(
    gyro::Distance,
    kind=
        safe_text,
    value=
        st.integers()
)
Action_strategy = st.builds(
    Action,
)
gyro::Actuate_strategy = st.builds(
    gyro::Actuate,
)
gyro::Condition_strategy = st.builds(
    gyro::Condition,
)
gyro::Action_strategy = st.builds(
    gyro::Action,
)
gyro::Node_strategy = st.builds(
    gyro::Node,
    name=
        safe_text
)
gyro::GyroSpecification_strategy = st.builds(
    gyro::GyroSpecification,
    name=
        safe_text
)
gyro::Behavior_strategy = st.builds(
    gyro::Behavior,
)
gyro::Sibling_strategy = st.builds(
    gyro::Sibling,
)
gyro::Child_strategy = st.builds(
    gyro::Child,
)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=gyro::StatusChange_strategy)
@settings(max_examples=50)
def test_gyro::statuschange_instantiation(instance):
    assert isinstance(instance, gyro::StatusChange)

@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeSuccess_type(instance):
    assert isinstance(instance.changeSuccess, str)


@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeSuccess_setter(instance):
    original = instance.changeSuccess
    instance.changeSuccess = original
    assert instance.changeSuccess == original

@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeFailure_type(instance):
    assert isinstance(instance.changeFailure, str)


@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeFailure_setter(instance):
    original = instance.changeFailure
    instance.changeFailure = original
    assert instance.changeFailure == original

@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeRunning_type(instance):
    assert isinstance(instance.changeRunning, str)


@given(instance=gyro::StatusChange_strategy)
def test_gyro::statuschange_changeRunning_setter(instance):
    original = instance.changeRunning
    instance.changeRunning = original
    assert instance.changeRunning == original

@given(instance=gyro::Sequential_strategy)
@settings(max_examples=50)
def test_gyro::sequential_instantiation(instance):
    assert isinstance(instance, gyro::Sequential)

@given(instance=gyro::Parallel_strategy)
@settings(max_examples=50)
def test_gyro::parallel_instantiation(instance):
    assert isinstance(instance, gyro::Parallel)

@given(instance=gyro::Priority_strategy)
@settings(max_examples=50)
def test_gyro::priority_instantiation(instance):
    assert isinstance(instance, gyro::Priority)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Actuate_strategy)
@settings(max_examples=50)
def test_actuate_instantiation(instance):
    assert isinstance(instance, Actuate)

@given(instance=gyro::LED_strategy)
@settings(max_examples=50)
def test_gyro::led_instantiation(instance):
    assert isinstance(instance, gyro::LED)

@given(instance=gyro::LED_strategy)
def test_gyro::led_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=gyro::LED_strategy)
def test_gyro::led_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=gyro::Servo_strategy)
@settings(max_examples=50)
def test_gyro::servo_instantiation(instance):
    assert isinstance(instance, gyro::Servo)

@given(instance=gyro::Servo_strategy)
def test_gyro::servo_minimalPosition_type(instance):
    assert isinstance(instance.minimalPosition, int)


@given(instance=gyro::Servo_strategy)
def test_gyro::servo_minimalPosition_setter(instance):
    original = instance.minimalPosition
    instance.minimalPosition = original
    assert instance.minimalPosition == original

@given(instance=gyro::Servo_strategy)
def test_gyro::servo_step_type(instance):
    assert isinstance(instance.step, int)


@given(instance=gyro::Servo_strategy)
def test_gyro::servo_step_setter(instance):
    original = instance.step
    instance.step = original
    assert instance.step == original

@given(instance=gyro::Servo_strategy)
def test_gyro::servo_maximalPosition_type(instance):
    assert isinstance(instance.maximalPosition, int)


@given(instance=gyro::Servo_strategy)
def test_gyro::servo_maximalPosition_setter(instance):
    original = instance.maximalPosition
    instance.maximalPosition = original
    assert instance.maximalPosition == original

@given(instance=gyro::Motor_strategy)
@settings(max_examples=50)
def test_gyro::motor_instantiation(instance):
    assert isinstance(instance, gyro::Motor)

@given(instance=gyro::Motor_strategy)
def test_gyro::motor_rightMotor_type(instance):
    assert isinstance(instance.rightMotor, int)


@given(instance=gyro::Motor_strategy)
def test_gyro::motor_rightMotor_setter(instance):
    original = instance.rightMotor
    instance.rightMotor = original
    assert instance.rightMotor == original

@given(instance=gyro::Motor_strategy)
def test_gyro::motor_leftMotor_type(instance):
    assert isinstance(instance.leftMotor, int)


@given(instance=gyro::Motor_strategy)
def test_gyro::motor_leftMotor_setter(instance):
    original = instance.leftMotor
    instance.leftMotor = original
    assert instance.leftMotor == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=gyro::Bumpers_strategy)
@settings(max_examples=50)
def test_gyro::bumpers_instantiation(instance):
    assert isinstance(instance, gyro::Bumpers)

@given(instance=gyro::Bumpers_strategy)
def test_gyro::bumpers_bumperKind_type(instance):
    assert isinstance(instance.bumperKind, str)


@given(instance=gyro::Bumpers_strategy)
def test_gyro::bumpers_bumperKind_setter(instance):
    original = instance.bumperKind
    instance.bumperKind = original
    assert instance.bumperKind == original

@given(instance=gyro::Waiting_strategy)
@settings(max_examples=50)
def test_gyro::waiting_instantiation(instance):
    assert isinstance(instance, gyro::Waiting)

@given(instance=gyro::Waiting_strategy)
def test_gyro::waiting_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=gyro::Waiting_strategy)
def test_gyro::waiting_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=gyro::Distance_strategy)
@settings(max_examples=50)
def test_gyro::distance_instantiation(instance):
    assert isinstance(instance, gyro::Distance)

@given(instance=gyro::Distance_strategy)
def test_gyro::distance_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=gyro::Distance_strategy)
def test_gyro::distance_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=gyro::Distance_strategy)
def test_gyro::distance_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=gyro::Distance_strategy)
def test_gyro::distance_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=gyro::Actuate_strategy)
@settings(max_examples=50)
def test_gyro::actuate_instantiation(instance):
    assert isinstance(instance, gyro::Actuate)

@given(instance=gyro::Condition_strategy)
@settings(max_examples=50)
def test_gyro::condition_instantiation(instance):
    assert isinstance(instance, gyro::Condition)

@given(instance=gyro::Action_strategy)
@settings(max_examples=50)
def test_gyro::action_instantiation(instance):
    assert isinstance(instance, gyro::Action)

@given(instance=gyro::Node_strategy)
@settings(max_examples=50)
def test_gyro::node_instantiation(instance):
    assert isinstance(instance, gyro::Node)

@given(instance=gyro::Node_strategy)
def test_gyro::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gyro::Node_strategy)
def test_gyro::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gyro::GyroSpecification_strategy)
@settings(max_examples=50)
def test_gyro::gyrospecification_instantiation(instance):
    assert isinstance(instance, gyro::GyroSpecification)

@given(instance=gyro::GyroSpecification_strategy)
def test_gyro::gyrospecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gyro::GyroSpecification_strategy)
def test_gyro::gyrospecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gyro::Behavior_strategy)
@settings(max_examples=50)
def test_gyro::behavior_instantiation(instance):
    assert isinstance(instance, gyro::Behavior)

@given(instance=gyro::Sibling_strategy)
@settings(max_examples=50)
def test_gyro::sibling_instantiation(instance):
    assert isinstance(instance, gyro::Sibling)

@given(instance=gyro::Child_strategy)
@settings(max_examples=50)
def test_gyro::child_instantiation(instance):
    assert isinstance(instance, gyro::Child)
