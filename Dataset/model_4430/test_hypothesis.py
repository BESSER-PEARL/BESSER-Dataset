import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryOperator,
    metamodel::Less,
    metamodel::Different,
    metamodel::More,
    metamodel::Equal,
    UnaryCond,
    metamodel::Negation,
    UnaryOperator,
    metamodel::Positive,
    metamodel::Negative,
    metamodel::Sub,
    metamodel::Add,
    metamodel::MoreOrEqual,
    metamodel::LessOrEqual,
    BinaryCond,
    metamodel::And,
    metamodel::Or,
    Condition,
    metamodel::UnaryCond,
    metamodel::BinaryCond,
    metamodel::Operator,
    Operator,
    metamodel::BinaryOperator,
    metamodel::UnaryOperator,
    metamodel::Condition,
    metamodel::Value,
    metamodel::Transition,
    metamodel::State,
    metamodel::StateMachine,
    Type,
    metamodel::FloatVal,
    metamodel::IntVal,
    metamodel::BoolVal,
    metamodel::Type,
    Sensor,
    metamodel::LightSensor,
    metamodel::DistanceSensor,
    ActionWheel,
    metamodel::TurnRight,
    metamodel::Forward,
    metamodel::Stopping,
    metamodel::Backward,
    metamodel::TurnLeft,
    Action,
    metamodel::ActionWheel,
    metamodel::Behaviour,
    metamodel::Robot,
    Actuator,
    metamodel::Group,
    metamodel::DifferentialWheel,
    metamodel::Action,
    metamodel::Actuator,
    metamodel::Sensor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::less_is_not_abstract():
    assert not inspect.isabstract(metamodel::Less)


def test_metamodel::less_constructor_exists():
    assert callable(metamodel::Less.__init__)


def test_metamodel::less_constructor_args():
    sig = inspect.signature(metamodel::Less.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::different_is_not_abstract():
    assert not inspect.isabstract(metamodel::Different)


def test_metamodel::different_constructor_exists():
    assert callable(metamodel::Different.__init__)


def test_metamodel::different_constructor_args():
    sig = inspect.signature(metamodel::Different.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::more_is_not_abstract():
    assert not inspect.isabstract(metamodel::More)


def test_metamodel::more_constructor_exists():
    assert callable(metamodel::More.__init__)


def test_metamodel::more_constructor_args():
    sig = inspect.signature(metamodel::More.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::equal_is_not_abstract():
    assert not inspect.isabstract(metamodel::Equal)


def test_metamodel::equal_constructor_exists():
    assert callable(metamodel::Equal.__init__)


def test_metamodel::equal_constructor_args():
    sig = inspect.signature(metamodel::Equal.__init__)
    params = list(sig.parameters.keys())



def test_unarycond_is_not_abstract():
    assert not inspect.isabstract(UnaryCond)


def test_unarycond_constructor_exists():
    assert callable(UnaryCond.__init__)


def test_unarycond_constructor_args():
    sig = inspect.signature(UnaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::negation_is_not_abstract():
    assert not inspect.isabstract(metamodel::Negation)


def test_metamodel::negation_constructor_exists():
    assert callable(metamodel::Negation.__init__)


def test_metamodel::negation_constructor_args():
    sig = inspect.signature(metamodel::Negation.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::positive_is_not_abstract():
    assert not inspect.isabstract(metamodel::Positive)


def test_metamodel::positive_constructor_exists():
    assert callable(metamodel::Positive.__init__)


def test_metamodel::positive_constructor_args():
    sig = inspect.signature(metamodel::Positive.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::negative_is_not_abstract():
    assert not inspect.isabstract(metamodel::Negative)


def test_metamodel::negative_constructor_exists():
    assert callable(metamodel::Negative.__init__)


def test_metamodel::negative_constructor_args():
    sig = inspect.signature(metamodel::Negative.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::sub_is_not_abstract():
    assert not inspect.isabstract(metamodel::Sub)


def test_metamodel::sub_constructor_exists():
    assert callable(metamodel::Sub.__init__)


def test_metamodel::sub_constructor_args():
    sig = inspect.signature(metamodel::Sub.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::add_is_not_abstract():
    assert not inspect.isabstract(metamodel::Add)


def test_metamodel::add_constructor_exists():
    assert callable(metamodel::Add.__init__)


def test_metamodel::add_constructor_args():
    sig = inspect.signature(metamodel::Add.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::moreorequal_is_not_abstract():
    assert not inspect.isabstract(metamodel::MoreOrEqual)


def test_metamodel::moreorequal_constructor_exists():
    assert callable(metamodel::MoreOrEqual.__init__)


def test_metamodel::moreorequal_constructor_args():
    sig = inspect.signature(metamodel::MoreOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::lessorequal_is_not_abstract():
    assert not inspect.isabstract(metamodel::LessOrEqual)


def test_metamodel::lessorequal_constructor_exists():
    assert callable(metamodel::LessOrEqual.__init__)


def test_metamodel::lessorequal_constructor_args():
    sig = inspect.signature(metamodel::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_binarycond_is_not_abstract():
    assert not inspect.isabstract(BinaryCond)


def test_binarycond_constructor_exists():
    assert callable(BinaryCond.__init__)


def test_binarycond_constructor_args():
    sig = inspect.signature(BinaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::and_is_not_abstract():
    assert not inspect.isabstract(metamodel::And)


def test_metamodel::and_constructor_exists():
    assert callable(metamodel::And.__init__)


def test_metamodel::and_constructor_args():
    sig = inspect.signature(metamodel::And.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::or_is_not_abstract():
    assert not inspect.isabstract(metamodel::Or)


def test_metamodel::or_constructor_exists():
    assert callable(metamodel::Or.__init__)


def test_metamodel::or_constructor_args():
    sig = inspect.signature(metamodel::Or.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::unarycond_is_not_abstract():
    assert not inspect.isabstract(metamodel::UnaryCond)


def test_metamodel::unarycond_constructor_exists():
    assert callable(metamodel::UnaryCond.__init__)


def test_metamodel::unarycond_constructor_args():
    sig = inspect.signature(metamodel::UnaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::binarycond_is_not_abstract():
    assert not inspect.isabstract(metamodel::BinaryCond)


def test_metamodel::binarycond_constructor_exists():
    assert callable(metamodel::BinaryCond.__init__)


def test_metamodel::binarycond_constructor_args():
    sig = inspect.signature(metamodel::BinaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::operator_is_not_abstract():
    assert not inspect.isabstract(metamodel::Operator)


def test_metamodel::operator_constructor_exists():
    assert callable(metamodel::Operator.__init__)


def test_metamodel::operator_constructor_args():
    sig = inspect.signature(metamodel::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(metamodel::BinaryOperator)


def test_metamodel::binaryoperator_constructor_exists():
    assert callable(metamodel::BinaryOperator.__init__)


def test_metamodel::binaryoperator_constructor_args():
    sig = inspect.signature(metamodel::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(metamodel::UnaryOperator)


def test_metamodel::unaryoperator_constructor_exists():
    assert callable(metamodel::UnaryOperator.__init__)


def test_metamodel::unaryoperator_constructor_args():
    sig = inspect.signature(metamodel::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::condition_is_not_abstract():
    assert not inspect.isabstract(metamodel::Condition)


def test_metamodel::condition_constructor_exists():
    assert callable(metamodel::Condition.__init__)


def test_metamodel::condition_constructor_args():
    sig = inspect.signature(metamodel::Condition.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::value_is_not_abstract():
    assert not inspect.isabstract(metamodel::Value)


def test_metamodel::value_constructor_exists():
    assert callable(metamodel::Value.__init__)


def test_metamodel::value_constructor_args():
    sig = inspect.signature(metamodel::Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::value_has_name():
    assert hasattr(metamodel::Value, "name")
    descriptor = None
    for klass in metamodel::Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::transition_is_not_abstract():
    assert not inspect.isabstract(metamodel::Transition)


def test_metamodel::transition_constructor_exists():
    assert callable(metamodel::Transition.__init__)


def test_metamodel::transition_constructor_args():
    sig = inspect.signature(metamodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "nameIn" in params, "Missing parameter 'nameIn'"

def test_metamodel::transition_has_nameIn():
    assert hasattr(metamodel::Transition, "nameIn")
    descriptor = None
    for klass in metamodel::Transition.__mro__:
        if "nameIn" in klass.__dict__:
            descriptor = klass.__dict__["nameIn"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::state_is_not_abstract():
    assert not inspect.isabstract(metamodel::State)


def test_metamodel::state_constructor_exists():
    assert callable(metamodel::State.__init__)


def test_metamodel::state_constructor_args():
    sig = inspect.signature(metamodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_metamodel::state_has_name():
    assert hasattr(metamodel::State, "name")
    descriptor = None
    for klass in metamodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::state_has_uid():
    assert hasattr(metamodel::State, "uid")
    descriptor = None
    for klass in metamodel::State.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::state_has_isInitial():
    assert hasattr(metamodel::State, "isInitial")
    descriptor = None
    for klass in metamodel::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(metamodel::StateMachine)


def test_metamodel::statemachine_constructor_exists():
    assert callable(metamodel::StateMachine.__init__)


def test_metamodel::statemachine_constructor_args():
    sig = inspect.signature(metamodel::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::statemachine_has_name():
    assert hasattr(metamodel::StateMachine, "name")
    descriptor = None
    for klass in metamodel::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::floatval_is_not_abstract():
    assert not inspect.isabstract(metamodel::FloatVal)


def test_metamodel::floatval_constructor_exists():
    assert callable(metamodel::FloatVal.__init__)


def test_metamodel::floatval_constructor_args():
    sig = inspect.signature(metamodel::FloatVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel::floatval_has_value():
    assert hasattr(metamodel::FloatVal, "value")
    descriptor = None
    for klass in metamodel::FloatVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::intval_is_not_abstract():
    assert not inspect.isabstract(metamodel::IntVal)


def test_metamodel::intval_constructor_exists():
    assert callable(metamodel::IntVal.__init__)


def test_metamodel::intval_constructor_args():
    sig = inspect.signature(metamodel::IntVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel::intval_has_value():
    assert hasattr(metamodel::IntVal, "value")
    descriptor = None
    for klass in metamodel::IntVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::boolval_is_not_abstract():
    assert not inspect.isabstract(metamodel::BoolVal)


def test_metamodel::boolval_constructor_exists():
    assert callable(metamodel::BoolVal.__init__)


def test_metamodel::boolval_constructor_args():
    sig = inspect.signature(metamodel::BoolVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel::boolval_has_value():
    assert hasattr(metamodel::BoolVal, "value")
    descriptor = None
    for klass in metamodel::BoolVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::type_is_not_abstract():
    assert not inspect.isabstract(metamodel::Type)


def test_metamodel::type_constructor_exists():
    assert callable(metamodel::Type.__init__)


def test_metamodel::type_constructor_args():
    sig = inspect.signature(metamodel::Type.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::lightsensor_is_not_abstract():
    assert not inspect.isabstract(metamodel::LightSensor)


def test_metamodel::lightsensor_constructor_exists():
    assert callable(metamodel::LightSensor.__init__)


def test_metamodel::lightsensor_constructor_args():
    sig = inspect.signature(metamodel::LightSensor.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::distancesensor_is_not_abstract():
    assert not inspect.isabstract(metamodel::DistanceSensor)


def test_metamodel::distancesensor_constructor_exists():
    assert callable(metamodel::DistanceSensor.__init__)


def test_metamodel::distancesensor_constructor_args():
    sig = inspect.signature(metamodel::DistanceSensor.__init__)
    params = list(sig.parameters.keys())



def test_actionwheel_is_not_abstract():
    assert not inspect.isabstract(ActionWheel)


def test_actionwheel_constructor_exists():
    assert callable(ActionWheel.__init__)


def test_actionwheel_constructor_args():
    sig = inspect.signature(ActionWheel.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::turnright_is_not_abstract():
    assert not inspect.isabstract(metamodel::TurnRight)


def test_metamodel::turnright_constructor_exists():
    assert callable(metamodel::TurnRight.__init__)


def test_metamodel::turnright_constructor_args():
    sig = inspect.signature(metamodel::TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::forward_is_not_abstract():
    assert not inspect.isabstract(metamodel::Forward)


def test_metamodel::forward_constructor_exists():
    assert callable(metamodel::Forward.__init__)


def test_metamodel::forward_constructor_args():
    sig = inspect.signature(metamodel::Forward.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::stopping_is_not_abstract():
    assert not inspect.isabstract(metamodel::Stopping)


def test_metamodel::stopping_constructor_exists():
    assert callable(metamodel::Stopping.__init__)


def test_metamodel::stopping_constructor_args():
    sig = inspect.signature(metamodel::Stopping.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::backward_is_not_abstract():
    assert not inspect.isabstract(metamodel::Backward)


def test_metamodel::backward_constructor_exists():
    assert callable(metamodel::Backward.__init__)


def test_metamodel::backward_constructor_args():
    sig = inspect.signature(metamodel::Backward.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::turnleft_is_not_abstract():
    assert not inspect.isabstract(metamodel::TurnLeft)


def test_metamodel::turnleft_constructor_exists():
    assert callable(metamodel::TurnLeft.__init__)


def test_metamodel::turnleft_constructor_args():
    sig = inspect.signature(metamodel::TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::actionwheel_is_not_abstract():
    assert not inspect.isabstract(metamodel::ActionWheel)


def test_metamodel::actionwheel_constructor_exists():
    assert callable(metamodel::ActionWheel.__init__)


def test_metamodel::actionwheel_constructor_args():
    sig = inspect.signature(metamodel::ActionWheel.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_metamodel::actionwheel_has_speed():
    assert hasattr(metamodel::ActionWheel, "speed")
    descriptor = None
    for klass in metamodel::ActionWheel.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::behaviour_is_not_abstract():
    assert not inspect.isabstract(metamodel::Behaviour)


def test_metamodel::behaviour_constructor_exists():
    assert callable(metamodel::Behaviour.__init__)


def test_metamodel::behaviour_constructor_args():
    sig = inspect.signature(metamodel::Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::behaviour_has_priority():
    assert hasattr(metamodel::Behaviour, "priority")
    descriptor = None
    for klass in metamodel::Behaviour.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::behaviour_has_name():
    assert hasattr(metamodel::Behaviour, "name")
    descriptor = None
    for klass in metamodel::Behaviour.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::robot_is_not_abstract():
    assert not inspect.isabstract(metamodel::Robot)


def test_metamodel::robot_constructor_exists():
    assert callable(metamodel::Robot.__init__)


def test_metamodel::robot_constructor_args():
    sig = inspect.signature(metamodel::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::robot_has_name():
    assert hasattr(metamodel::Robot, "name")
    descriptor = None
    for klass in metamodel::Robot.__mro__:
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



def test_metamodel::group_is_not_abstract():
    assert not inspect.isabstract(metamodel::Group)


def test_metamodel::group_constructor_exists():
    assert callable(metamodel::Group.__init__)


def test_metamodel::group_constructor_args():
    sig = inspect.signature(metamodel::Group.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::differentialwheel_is_not_abstract():
    assert not inspect.isabstract(metamodel::DifferentialWheel)


def test_metamodel::differentialwheel_constructor_exists():
    assert callable(metamodel::DifferentialWheel.__init__)


def test_metamodel::differentialwheel_constructor_args():
    sig = inspect.signature(metamodel::DifferentialWheel.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "isLeft" in params, "Missing parameter 'isLeft'"

def test_metamodel::differentialwheel_has_speed():
    assert hasattr(metamodel::DifferentialWheel, "speed")
    descriptor = None
    for klass in metamodel::DifferentialWheel.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::differentialwheel_has_isLeft():
    assert hasattr(metamodel::DifferentialWheel, "isLeft")
    descriptor = None
    for klass in metamodel::DifferentialWheel.__mro__:
        if "isLeft" in klass.__dict__:
            descriptor = klass.__dict__["isLeft"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::action_is_not_abstract():
    assert not inspect.isabstract(metamodel::Action)


def test_metamodel::action_constructor_exists():
    assert callable(metamodel::Action.__init__)


def test_metamodel::action_constructor_args():
    sig = inspect.signature(metamodel::Action.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::actuator_is_not_abstract():
    assert not inspect.isabstract(metamodel::Actuator)


def test_metamodel::actuator_constructor_exists():
    assert callable(metamodel::Actuator.__init__)


def test_metamodel::actuator_constructor_args():
    sig = inspect.signature(metamodel::Actuator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::actuator_has_name():
    assert hasattr(metamodel::Actuator, "name")
    descriptor = None
    for klass in metamodel::Actuator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::sensor_is_not_abstract():
    assert not inspect.isabstract(metamodel::Sensor)


def test_metamodel::sensor_constructor_exists():
    assert callable(metamodel::Sensor.__init__)


def test_metamodel::sensor_constructor_args():
    sig = inspect.signature(metamodel::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "sensorName" in params, "Missing parameter 'sensorName'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::sensor_has_sensorName():
    assert hasattr(metamodel::Sensor, "sensorName")
    descriptor = None
    for klass in metamodel::Sensor.__mro__:
        if "sensorName" in klass.__dict__:
            descriptor = klass.__dict__["sensorName"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sensor_has_name():
    assert hasattr(metamodel::Sensor, "name")
    descriptor = None
    for klass in metamodel::Sensor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
metamodel::Less_strategy = st.builds(
    metamodel::Less,
)
metamodel::Different_strategy = st.builds(
    metamodel::Different,
)
metamodel::More_strategy = st.builds(
    metamodel::More,
)
metamodel::Equal_strategy = st.builds(
    metamodel::Equal,
)
UnaryCond_strategy = st.builds(
    UnaryCond,
)
metamodel::Negation_strategy = st.builds(
    metamodel::Negation,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
metamodel::Positive_strategy = st.builds(
    metamodel::Positive,
)
metamodel::Negative_strategy = st.builds(
    metamodel::Negative,
)
metamodel::Sub_strategy = st.builds(
    metamodel::Sub,
)
metamodel::Add_strategy = st.builds(
    metamodel::Add,
)
metamodel::MoreOrEqual_strategy = st.builds(
    metamodel::MoreOrEqual,
)
metamodel::LessOrEqual_strategy = st.builds(
    metamodel::LessOrEqual,
)
BinaryCond_strategy = st.builds(
    BinaryCond,
)
metamodel::And_strategy = st.builds(
    metamodel::And,
)
metamodel::Or_strategy = st.builds(
    metamodel::Or,
)
Condition_strategy = st.builds(
    Condition,
)
metamodel::UnaryCond_strategy = st.builds(
    metamodel::UnaryCond,
)
metamodel::BinaryCond_strategy = st.builds(
    metamodel::BinaryCond,
)
metamodel::Operator_strategy = st.builds(
    metamodel::Operator,
)
Operator_strategy = st.builds(
    Operator,
)
metamodel::BinaryOperator_strategy = st.builds(
    metamodel::BinaryOperator,
)
metamodel::UnaryOperator_strategy = st.builds(
    metamodel::UnaryOperator,
)
metamodel::Condition_strategy = st.builds(
    metamodel::Condition,
)
metamodel::Value_strategy = st.builds(
    metamodel::Value,
    name=
        safe_text
)
metamodel::Transition_strategy = st.builds(
    metamodel::Transition,
    nameIn=
        safe_text
)
metamodel::State_strategy = st.builds(
    metamodel::State,
    name=
        safe_text,
    uid=
        st.integers(),
    isInitial=
        st.booleans()
)
metamodel::StateMachine_strategy = st.builds(
    metamodel::StateMachine,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
metamodel::FloatVal_strategy = st.builds(
    metamodel::FloatVal,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
metamodel::IntVal_strategy = st.builds(
    metamodel::IntVal,
    value=
        st.integers()
)
metamodel::BoolVal_strategy = st.builds(
    metamodel::BoolVal,
    value=
        st.booleans()
)
metamodel::Type_strategy = st.builds(
    metamodel::Type,
)
Sensor_strategy = st.builds(
    Sensor,
)
metamodel::LightSensor_strategy = st.builds(
    metamodel::LightSensor,
)
metamodel::DistanceSensor_strategy = st.builds(
    metamodel::DistanceSensor,
)
ActionWheel_strategy = st.builds(
    ActionWheel,
)
metamodel::TurnRight_strategy = st.builds(
    metamodel::TurnRight,
)
metamodel::Forward_strategy = st.builds(
    metamodel::Forward,
)
metamodel::Stopping_strategy = st.builds(
    metamodel::Stopping,
)
metamodel::Backward_strategy = st.builds(
    metamodel::Backward,
)
metamodel::TurnLeft_strategy = st.builds(
    metamodel::TurnLeft,
)
Action_strategy = st.builds(
    Action,
)
metamodel::ActionWheel_strategy = st.builds(
    metamodel::ActionWheel,
    speed=
        st.integers()
)
metamodel::Behaviour_strategy = st.builds(
    metamodel::Behaviour,
    priority=
        st.integers(),
    name=
        safe_text
)
metamodel::Robot_strategy = st.builds(
    metamodel::Robot,
    name=
        safe_text
)
Actuator_strategy = st.builds(
    Actuator,
)
metamodel::Group_strategy = st.builds(
    metamodel::Group,
)
metamodel::DifferentialWheel_strategy = st.builds(
    metamodel::DifferentialWheel,
    speed=
        st.integers(),
    isLeft=
        st.booleans()
)
metamodel::Action_strategy = st.builds(
    metamodel::Action,
)
metamodel::Actuator_strategy = st.builds(
    metamodel::Actuator,
    name=
        safe_text
)
metamodel::Sensor_strategy = st.builds(
    metamodel::Sensor,
    sensorName=
        safe_text,
    name=
        safe_text
)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=metamodel::Less_strategy)
@settings(max_examples=50)
def test_metamodel::less_instantiation(instance):
    assert isinstance(instance, metamodel::Less)

@given(instance=metamodel::Different_strategy)
@settings(max_examples=50)
def test_metamodel::different_instantiation(instance):
    assert isinstance(instance, metamodel::Different)

@given(instance=metamodel::More_strategy)
@settings(max_examples=50)
def test_metamodel::more_instantiation(instance):
    assert isinstance(instance, metamodel::More)

@given(instance=metamodel::Equal_strategy)
@settings(max_examples=50)
def test_metamodel::equal_instantiation(instance):
    assert isinstance(instance, metamodel::Equal)

@given(instance=UnaryCond_strategy)
@settings(max_examples=50)
def test_unarycond_instantiation(instance):
    assert isinstance(instance, UnaryCond)

@given(instance=metamodel::Negation_strategy)
@settings(max_examples=50)
def test_metamodel::negation_instantiation(instance):
    assert isinstance(instance, metamodel::Negation)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=metamodel::Positive_strategy)
@settings(max_examples=50)
def test_metamodel::positive_instantiation(instance):
    assert isinstance(instance, metamodel::Positive)

@given(instance=metamodel::Negative_strategy)
@settings(max_examples=50)
def test_metamodel::negative_instantiation(instance):
    assert isinstance(instance, metamodel::Negative)

@given(instance=metamodel::Sub_strategy)
@settings(max_examples=50)
def test_metamodel::sub_instantiation(instance):
    assert isinstance(instance, metamodel::Sub)

@given(instance=metamodel::Add_strategy)
@settings(max_examples=50)
def test_metamodel::add_instantiation(instance):
    assert isinstance(instance, metamodel::Add)

@given(instance=metamodel::MoreOrEqual_strategy)
@settings(max_examples=50)
def test_metamodel::moreorequal_instantiation(instance):
    assert isinstance(instance, metamodel::MoreOrEqual)

@given(instance=metamodel::LessOrEqual_strategy)
@settings(max_examples=50)
def test_metamodel::lessorequal_instantiation(instance):
    assert isinstance(instance, metamodel::LessOrEqual)

@given(instance=BinaryCond_strategy)
@settings(max_examples=50)
def test_binarycond_instantiation(instance):
    assert isinstance(instance, BinaryCond)

@given(instance=metamodel::And_strategy)
@settings(max_examples=50)
def test_metamodel::and_instantiation(instance):
    assert isinstance(instance, metamodel::And)

@given(instance=metamodel::Or_strategy)
@settings(max_examples=50)
def test_metamodel::or_instantiation(instance):
    assert isinstance(instance, metamodel::Or)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=metamodel::UnaryCond_strategy)
@settings(max_examples=50)
def test_metamodel::unarycond_instantiation(instance):
    assert isinstance(instance, metamodel::UnaryCond)

@given(instance=metamodel::BinaryCond_strategy)
@settings(max_examples=50)
def test_metamodel::binarycond_instantiation(instance):
    assert isinstance(instance, metamodel::BinaryCond)

@given(instance=metamodel::Operator_strategy)
@settings(max_examples=50)
def test_metamodel::operator_instantiation(instance):
    assert isinstance(instance, metamodel::Operator)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=metamodel::BinaryOperator_strategy)
@settings(max_examples=50)
def test_metamodel::binaryoperator_instantiation(instance):
    assert isinstance(instance, metamodel::BinaryOperator)

@given(instance=metamodel::UnaryOperator_strategy)
@settings(max_examples=50)
def test_metamodel::unaryoperator_instantiation(instance):
    assert isinstance(instance, metamodel::UnaryOperator)

@given(instance=metamodel::Condition_strategy)
@settings(max_examples=50)
def test_metamodel::condition_instantiation(instance):
    assert isinstance(instance, metamodel::Condition)

@given(instance=metamodel::Value_strategy)
@settings(max_examples=50)
def test_metamodel::value_instantiation(instance):
    assert isinstance(instance, metamodel::Value)

@given(instance=metamodel::Value_strategy)
def test_metamodel::value_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Value_strategy)
def test_metamodel::value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Transition_strategy)
@settings(max_examples=50)
def test_metamodel::transition_instantiation(instance):
    assert isinstance(instance, metamodel::Transition)

@given(instance=metamodel::Transition_strategy)
def test_metamodel::transition_nameIn_type(instance):
    assert isinstance(instance.nameIn, str)


@given(instance=metamodel::Transition_strategy)
def test_metamodel::transition_nameIn_setter(instance):
    original = instance.nameIn
    instance.nameIn = original
    assert instance.nameIn == original

@given(instance=metamodel::State_strategy)
@settings(max_examples=50)
def test_metamodel::state_instantiation(instance):
    assert isinstance(instance, metamodel::State)

@given(instance=metamodel::State_strategy)
def test_metamodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::State_strategy)
def test_metamodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::State_strategy)
def test_metamodel::state_uid_type(instance):
    assert isinstance(instance.uid, int)


@given(instance=metamodel::State_strategy)
def test_metamodel::state_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=metamodel::State_strategy)
def test_metamodel::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=metamodel::State_strategy)
def test_metamodel::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=metamodel::StateMachine_strategy)
@settings(max_examples=50)
def test_metamodel::statemachine_instantiation(instance):
    assert isinstance(instance, metamodel::StateMachine)

@given(instance=metamodel::StateMachine_strategy)
def test_metamodel::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::StateMachine_strategy)
def test_metamodel::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel::FloatVal_strategy)
@settings(max_examples=50)
def test_metamodel::floatval_instantiation(instance):
    assert isinstance(instance, metamodel::FloatVal)

@given(instance=metamodel::FloatVal_strategy)
def test_metamodel::floatval_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=metamodel::FloatVal_strategy)
def test_metamodel::floatval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel::IntVal_strategy)
@settings(max_examples=50)
def test_metamodel::intval_instantiation(instance):
    assert isinstance(instance, metamodel::IntVal)

@given(instance=metamodel::IntVal_strategy)
def test_metamodel::intval_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=metamodel::IntVal_strategy)
def test_metamodel::intval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel::BoolVal_strategy)
@settings(max_examples=50)
def test_metamodel::boolval_instantiation(instance):
    assert isinstance(instance, metamodel::BoolVal)

@given(instance=metamodel::BoolVal_strategy)
def test_metamodel::boolval_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=metamodel::BoolVal_strategy)
def test_metamodel::boolval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel::Type_strategy)
@settings(max_examples=50)
def test_metamodel::type_instantiation(instance):
    assert isinstance(instance, metamodel::Type)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=metamodel::LightSensor_strategy)
@settings(max_examples=50)
def test_metamodel::lightsensor_instantiation(instance):
    assert isinstance(instance, metamodel::LightSensor)

@given(instance=metamodel::DistanceSensor_strategy)
@settings(max_examples=50)
def test_metamodel::distancesensor_instantiation(instance):
    assert isinstance(instance, metamodel::DistanceSensor)

@given(instance=ActionWheel_strategy)
@settings(max_examples=50)
def test_actionwheel_instantiation(instance):
    assert isinstance(instance, ActionWheel)

@given(instance=metamodel::TurnRight_strategy)
@settings(max_examples=50)
def test_metamodel::turnright_instantiation(instance):
    assert isinstance(instance, metamodel::TurnRight)

@given(instance=metamodel::Forward_strategy)
@settings(max_examples=50)
def test_metamodel::forward_instantiation(instance):
    assert isinstance(instance, metamodel::Forward)

@given(instance=metamodel::Stopping_strategy)
@settings(max_examples=50)
def test_metamodel::stopping_instantiation(instance):
    assert isinstance(instance, metamodel::Stopping)

@given(instance=metamodel::Backward_strategy)
@settings(max_examples=50)
def test_metamodel::backward_instantiation(instance):
    assert isinstance(instance, metamodel::Backward)

@given(instance=metamodel::TurnLeft_strategy)
@settings(max_examples=50)
def test_metamodel::turnleft_instantiation(instance):
    assert isinstance(instance, metamodel::TurnLeft)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=metamodel::ActionWheel_strategy)
@settings(max_examples=50)
def test_metamodel::actionwheel_instantiation(instance):
    assert isinstance(instance, metamodel::ActionWheel)

@given(instance=metamodel::ActionWheel_strategy)
def test_metamodel::actionwheel_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=metamodel::ActionWheel_strategy)
def test_metamodel::actionwheel_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=metamodel::Behaviour_strategy)
@settings(max_examples=50)
def test_metamodel::behaviour_instantiation(instance):
    assert isinstance(instance, metamodel::Behaviour)

@given(instance=metamodel::Behaviour_strategy)
def test_metamodel::behaviour_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=metamodel::Behaviour_strategy)
def test_metamodel::behaviour_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=metamodel::Behaviour_strategy)
def test_metamodel::behaviour_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Behaviour_strategy)
def test_metamodel::behaviour_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Robot_strategy)
@settings(max_examples=50)
def test_metamodel::robot_instantiation(instance):
    assert isinstance(instance, metamodel::Robot)

@given(instance=metamodel::Robot_strategy)
def test_metamodel::robot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Robot_strategy)
def test_metamodel::robot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=metamodel::Group_strategy)
@settings(max_examples=50)
def test_metamodel::group_instantiation(instance):
    assert isinstance(instance, metamodel::Group)

@given(instance=metamodel::DifferentialWheel_strategy)
@settings(max_examples=50)
def test_metamodel::differentialwheel_instantiation(instance):
    assert isinstance(instance, metamodel::DifferentialWheel)

@given(instance=metamodel::DifferentialWheel_strategy)
def test_metamodel::differentialwheel_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=metamodel::DifferentialWheel_strategy)
def test_metamodel::differentialwheel_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=metamodel::DifferentialWheel_strategy)
def test_metamodel::differentialwheel_isLeft_type(instance):
    assert isinstance(instance.isLeft, bool)


@given(instance=metamodel::DifferentialWheel_strategy)
def test_metamodel::differentialwheel_isLeft_setter(instance):
    original = instance.isLeft
    instance.isLeft = original
    assert instance.isLeft == original

@given(instance=metamodel::Action_strategy)
@settings(max_examples=50)
def test_metamodel::action_instantiation(instance):
    assert isinstance(instance, metamodel::Action)

@given(instance=metamodel::Actuator_strategy)
@settings(max_examples=50)
def test_metamodel::actuator_instantiation(instance):
    assert isinstance(instance, metamodel::Actuator)

@given(instance=metamodel::Actuator_strategy)
def test_metamodel::actuator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Actuator_strategy)
def test_metamodel::actuator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Sensor_strategy)
@settings(max_examples=50)
def test_metamodel::sensor_instantiation(instance):
    assert isinstance(instance, metamodel::Sensor)

@given(instance=metamodel::Sensor_strategy)
def test_metamodel::sensor_sensorName_type(instance):
    assert isinstance(instance.sensorName, str)


@given(instance=metamodel::Sensor_strategy)
def test_metamodel::sensor_sensorName_setter(instance):
    original = instance.sensorName
    instance.sensorName = original
    assert instance.sensorName == original

@given(instance=metamodel::Sensor_strategy)
def test_metamodel::sensor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Sensor_strategy)
def test_metamodel::sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
