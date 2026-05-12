import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryOperator,
    metamodel_Different,
    metamodel_More,
    metamodel_Less,
    metamodel_Equal,
    UnaryCond,
    metamodel_Negation,
    UnaryOperator,
    metamodel_Positive,
    metamodel_Negative,
    metamodel_Sub,
    metamodel_Add,
    metamodel_MoreOrEqual,
    metamodel_LessOrEqual,
    BinaryCond,
    metamodel_And,
    metamodel_Or,
    Condition,
    metamodel_UnaryCond,
    metamodel_BinaryCond,
    metamodel_Operator,
    Operator,
    metamodel_BinaryOperator,
    metamodel_UnaryOperator,
    metamodel_Condition,
    metamodel_Value,
    metamodel_Transition,
    metamodel_State,
    metamodel_StateMachine,
    Type,
    metamodel_FloatVal,
    metamodel_IntVal,
    metamodel_BoolVal,
    metamodel_Type,
    Sensor,
    metamodel_LightSensor,
    metamodel_DistanceSensor,
    ActionWheel,
    metamodel_Forward,
    metamodel_Backward,
    metamodel_TurnRight,
    metamodel_Stopping,
    metamodel_TurnLeft,
    Action,
    metamodel_ActionWheel,
    metamodel_Behaviour,
    metamodel_Robot,
    Actuator,
    metamodel_Group,
    metamodel_DifferentialWheel,
    metamodel_Action,
    metamodel_Actuator,
    metamodel_Sensor,
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



def test_metamodel_different_is_not_abstract():
    assert not inspect.isabstract(metamodel_Different)


def test_metamodel_different_constructor_exists():
    assert callable(metamodel_Different.__init__)


def test_metamodel_different_constructor_args():
    sig = inspect.signature(metamodel_Different.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_more_is_not_abstract():
    assert not inspect.isabstract(metamodel_More)


def test_metamodel_more_constructor_exists():
    assert callable(metamodel_More.__init__)


def test_metamodel_more_constructor_args():
    sig = inspect.signature(metamodel_More.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_less_is_not_abstract():
    assert not inspect.isabstract(metamodel_Less)


def test_metamodel_less_constructor_exists():
    assert callable(metamodel_Less.__init__)


def test_metamodel_less_constructor_args():
    sig = inspect.signature(metamodel_Less.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_equal_is_not_abstract():
    assert not inspect.isabstract(metamodel_Equal)


def test_metamodel_equal_constructor_exists():
    assert callable(metamodel_Equal.__init__)


def test_metamodel_equal_constructor_args():
    sig = inspect.signature(metamodel_Equal.__init__)
    params = list(sig.parameters.keys())



def test_unarycond_is_not_abstract():
    assert not inspect.isabstract(UnaryCond)


def test_unarycond_constructor_exists():
    assert callable(UnaryCond.__init__)


def test_unarycond_constructor_args():
    sig = inspect.signature(UnaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_negation_is_not_abstract():
    assert not inspect.isabstract(metamodel_Negation)


def test_metamodel_negation_constructor_exists():
    assert callable(metamodel_Negation.__init__)


def test_metamodel_negation_constructor_args():
    sig = inspect.signature(metamodel_Negation.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_positive_is_not_abstract():
    assert not inspect.isabstract(metamodel_Positive)


def test_metamodel_positive_constructor_exists():
    assert callable(metamodel_Positive.__init__)


def test_metamodel_positive_constructor_args():
    sig = inspect.signature(metamodel_Positive.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_negative_is_not_abstract():
    assert not inspect.isabstract(metamodel_Negative)


def test_metamodel_negative_constructor_exists():
    assert callable(metamodel_Negative.__init__)


def test_metamodel_negative_constructor_args():
    sig = inspect.signature(metamodel_Negative.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_sub_is_not_abstract():
    assert not inspect.isabstract(metamodel_Sub)


def test_metamodel_sub_constructor_exists():
    assert callable(metamodel_Sub.__init__)


def test_metamodel_sub_constructor_args():
    sig = inspect.signature(metamodel_Sub.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_add_is_not_abstract():
    assert not inspect.isabstract(metamodel_Add)


def test_metamodel_add_constructor_exists():
    assert callable(metamodel_Add.__init__)


def test_metamodel_add_constructor_args():
    sig = inspect.signature(metamodel_Add.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_moreorequal_is_not_abstract():
    assert not inspect.isabstract(metamodel_MoreOrEqual)


def test_metamodel_moreorequal_constructor_exists():
    assert callable(metamodel_MoreOrEqual.__init__)


def test_metamodel_moreorequal_constructor_args():
    sig = inspect.signature(metamodel_MoreOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_lessorequal_is_not_abstract():
    assert not inspect.isabstract(metamodel_LessOrEqual)


def test_metamodel_lessorequal_constructor_exists():
    assert callable(metamodel_LessOrEqual.__init__)


def test_metamodel_lessorequal_constructor_args():
    sig = inspect.signature(metamodel_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_binarycond_is_not_abstract():
    assert not inspect.isabstract(BinaryCond)


def test_binarycond_constructor_exists():
    assert callable(BinaryCond.__init__)


def test_binarycond_constructor_args():
    sig = inspect.signature(BinaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_and_is_not_abstract():
    assert not inspect.isabstract(metamodel_And)


def test_metamodel_and_constructor_exists():
    assert callable(metamodel_And.__init__)


def test_metamodel_and_constructor_args():
    sig = inspect.signature(metamodel_And.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_or_is_not_abstract():
    assert not inspect.isabstract(metamodel_Or)


def test_metamodel_or_constructor_exists():
    assert callable(metamodel_Or.__init__)


def test_metamodel_or_constructor_args():
    sig = inspect.signature(metamodel_Or.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_unarycond_is_not_abstract():
    assert not inspect.isabstract(metamodel_UnaryCond)


def test_metamodel_unarycond_constructor_exists():
    assert callable(metamodel_UnaryCond.__init__)


def test_metamodel_unarycond_constructor_args():
    sig = inspect.signature(metamodel_UnaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_binarycond_is_not_abstract():
    assert not inspect.isabstract(metamodel_BinaryCond)


def test_metamodel_binarycond_constructor_exists():
    assert callable(metamodel_BinaryCond.__init__)


def test_metamodel_binarycond_constructor_args():
    sig = inspect.signature(metamodel_BinaryCond.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_operator_is_not_abstract():
    assert not inspect.isabstract(metamodel_Operator)


def test_metamodel_operator_constructor_exists():
    assert callable(metamodel_Operator.__init__)


def test_metamodel_operator_constructor_args():
    sig = inspect.signature(metamodel_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(metamodel_BinaryOperator)


def test_metamodel_binaryoperator_constructor_exists():
    assert callable(metamodel_BinaryOperator.__init__)


def test_metamodel_binaryoperator_constructor_args():
    sig = inspect.signature(metamodel_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(metamodel_UnaryOperator)


def test_metamodel_unaryoperator_constructor_exists():
    assert callable(metamodel_UnaryOperator.__init__)


def test_metamodel_unaryoperator_constructor_args():
    sig = inspect.signature(metamodel_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_condition_is_not_abstract():
    assert not inspect.isabstract(metamodel_Condition)


def test_metamodel_condition_constructor_exists():
    assert callable(metamodel_Condition.__init__)


def test_metamodel_condition_constructor_args():
    sig = inspect.signature(metamodel_Condition.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_value_is_not_abstract():
    assert not inspect.isabstract(metamodel_Value)


def test_metamodel_value_constructor_exists():
    assert callable(metamodel_Value.__init__)


def test_metamodel_value_constructor_args():
    sig = inspect.signature(metamodel_Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_value_has_name():
    assert hasattr(metamodel_Value, "name")
    descriptor = None
    for klass in metamodel_Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_transition_is_not_abstract():
    assert not inspect.isabstract(metamodel_Transition)


def test_metamodel_transition_constructor_exists():
    assert callable(metamodel_Transition.__init__)


def test_metamodel_transition_constructor_args():
    sig = inspect.signature(metamodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "nameIn" in params, "Missing parameter 'nameIn'"

def test_metamodel_transition_has_nameIn():
    assert hasattr(metamodel_Transition, "nameIn")
    descriptor = None
    for klass in metamodel_Transition.__mro__:
        if "nameIn" in klass.__dict__:
            descriptor = klass.__dict__["nameIn"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_state_is_not_abstract():
    assert not inspect.isabstract(metamodel_State)


def test_metamodel_state_constructor_exists():
    assert callable(metamodel_State.__init__)


def test_metamodel_state_constructor_args():
    sig = inspect.signature(metamodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_metamodel_state_has_name():
    assert hasattr(metamodel_State, "name")
    descriptor = None
    for klass in metamodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_state_has_isInitial():
    assert hasattr(metamodel_State, "isInitial")
    descriptor = None
    for klass in metamodel_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_state_has_uid():
    assert hasattr(metamodel_State, "uid")
    descriptor = None
    for klass in metamodel_State.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(metamodel_StateMachine)


def test_metamodel_statemachine_constructor_exists():
    assert callable(metamodel_StateMachine.__init__)


def test_metamodel_statemachine_constructor_args():
    sig = inspect.signature(metamodel_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_statemachine_has_name():
    assert hasattr(metamodel_StateMachine, "name")
    descriptor = None
    for klass in metamodel_StateMachine.__mro__:
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



def test_metamodel_floatval_is_not_abstract():
    assert not inspect.isabstract(metamodel_FloatVal)


def test_metamodel_floatval_constructor_exists():
    assert callable(metamodel_FloatVal.__init__)


def test_metamodel_floatval_constructor_args():
    sig = inspect.signature(metamodel_FloatVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel_floatval_has_value():
    assert hasattr(metamodel_FloatVal, "value")
    descriptor = None
    for klass in metamodel_FloatVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_intval_is_not_abstract():
    assert not inspect.isabstract(metamodel_IntVal)


def test_metamodel_intval_constructor_exists():
    assert callable(metamodel_IntVal.__init__)


def test_metamodel_intval_constructor_args():
    sig = inspect.signature(metamodel_IntVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel_intval_has_value():
    assert hasattr(metamodel_IntVal, "value")
    descriptor = None
    for klass in metamodel_IntVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_boolval_is_not_abstract():
    assert not inspect.isabstract(metamodel_BoolVal)


def test_metamodel_boolval_constructor_exists():
    assert callable(metamodel_BoolVal.__init__)


def test_metamodel_boolval_constructor_args():
    sig = inspect.signature(metamodel_BoolVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel_boolval_has_value():
    assert hasattr(metamodel_BoolVal, "value")
    descriptor = None
    for klass in metamodel_BoolVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_type_is_not_abstract():
    assert not inspect.isabstract(metamodel_Type)


def test_metamodel_type_constructor_exists():
    assert callable(metamodel_Type.__init__)


def test_metamodel_type_constructor_args():
    sig = inspect.signature(metamodel_Type.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_lightsensor_is_not_abstract():
    assert not inspect.isabstract(metamodel_LightSensor)


def test_metamodel_lightsensor_constructor_exists():
    assert callable(metamodel_LightSensor.__init__)


def test_metamodel_lightsensor_constructor_args():
    sig = inspect.signature(metamodel_LightSensor.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_distancesensor_is_not_abstract():
    assert not inspect.isabstract(metamodel_DistanceSensor)


def test_metamodel_distancesensor_constructor_exists():
    assert callable(metamodel_DistanceSensor.__init__)


def test_metamodel_distancesensor_constructor_args():
    sig = inspect.signature(metamodel_DistanceSensor.__init__)
    params = list(sig.parameters.keys())



def test_actionwheel_is_not_abstract():
    assert not inspect.isabstract(ActionWheel)


def test_actionwheel_constructor_exists():
    assert callable(ActionWheel.__init__)


def test_actionwheel_constructor_args():
    sig = inspect.signature(ActionWheel.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_forward_is_not_abstract():
    assert not inspect.isabstract(metamodel_Forward)


def test_metamodel_forward_constructor_exists():
    assert callable(metamodel_Forward.__init__)


def test_metamodel_forward_constructor_args():
    sig = inspect.signature(metamodel_Forward.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_backward_is_not_abstract():
    assert not inspect.isabstract(metamodel_Backward)


def test_metamodel_backward_constructor_exists():
    assert callable(metamodel_Backward.__init__)


def test_metamodel_backward_constructor_args():
    sig = inspect.signature(metamodel_Backward.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_turnright_is_not_abstract():
    assert not inspect.isabstract(metamodel_TurnRight)


def test_metamodel_turnright_constructor_exists():
    assert callable(metamodel_TurnRight.__init__)


def test_metamodel_turnright_constructor_args():
    sig = inspect.signature(metamodel_TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_stopping_is_not_abstract():
    assert not inspect.isabstract(metamodel_Stopping)


def test_metamodel_stopping_constructor_exists():
    assert callable(metamodel_Stopping.__init__)


def test_metamodel_stopping_constructor_args():
    sig = inspect.signature(metamodel_Stopping.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_turnleft_is_not_abstract():
    assert not inspect.isabstract(metamodel_TurnLeft)


def test_metamodel_turnleft_constructor_exists():
    assert callable(metamodel_TurnLeft.__init__)


def test_metamodel_turnleft_constructor_args():
    sig = inspect.signature(metamodel_TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_actionwheel_is_not_abstract():
    assert not inspect.isabstract(metamodel_ActionWheel)


def test_metamodel_actionwheel_constructor_exists():
    assert callable(metamodel_ActionWheel.__init__)


def test_metamodel_actionwheel_constructor_args():
    sig = inspect.signature(metamodel_ActionWheel.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_metamodel_actionwheel_has_speed():
    assert hasattr(metamodel_ActionWheel, "speed")
    descriptor = None
    for klass in metamodel_ActionWheel.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_behaviour_is_not_abstract():
    assert not inspect.isabstract(metamodel_Behaviour)


def test_metamodel_behaviour_constructor_exists():
    assert callable(metamodel_Behaviour.__init__)


def test_metamodel_behaviour_constructor_args():
    sig = inspect.signature(metamodel_Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_behaviour_has_priority():
    assert hasattr(metamodel_Behaviour, "priority")
    descriptor = None
    for klass in metamodel_Behaviour.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_behaviour_has_name():
    assert hasattr(metamodel_Behaviour, "name")
    descriptor = None
    for klass in metamodel_Behaviour.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_robot_is_not_abstract():
    assert not inspect.isabstract(metamodel_Robot)


def test_metamodel_robot_constructor_exists():
    assert callable(metamodel_Robot.__init__)


def test_metamodel_robot_constructor_args():
    sig = inspect.signature(metamodel_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_robot_has_name():
    assert hasattr(metamodel_Robot, "name")
    descriptor = None
    for klass in metamodel_Robot.__mro__:
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



def test_metamodel_group_is_not_abstract():
    assert not inspect.isabstract(metamodel_Group)


def test_metamodel_group_constructor_exists():
    assert callable(metamodel_Group.__init__)


def test_metamodel_group_constructor_args():
    sig = inspect.signature(metamodel_Group.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_differentialwheel_is_not_abstract():
    assert not inspect.isabstract(metamodel_DifferentialWheel)


def test_metamodel_differentialwheel_constructor_exists():
    assert callable(metamodel_DifferentialWheel.__init__)


def test_metamodel_differentialwheel_constructor_args():
    sig = inspect.signature(metamodel_DifferentialWheel.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "isLeft" in params, "Missing parameter 'isLeft'"

def test_metamodel_differentialwheel_has_speed():
    assert hasattr(metamodel_DifferentialWheel, "speed")
    descriptor = None
    for klass in metamodel_DifferentialWheel.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_differentialwheel_has_isLeft():
    assert hasattr(metamodel_DifferentialWheel, "isLeft")
    descriptor = None
    for klass in metamodel_DifferentialWheel.__mro__:
        if "isLeft" in klass.__dict__:
            descriptor = klass.__dict__["isLeft"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_action_is_not_abstract():
    assert not inspect.isabstract(metamodel_Action)


def test_metamodel_action_constructor_exists():
    assert callable(metamodel_Action.__init__)


def test_metamodel_action_constructor_args():
    sig = inspect.signature(metamodel_Action.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_actuator_is_not_abstract():
    assert not inspect.isabstract(metamodel_Actuator)


def test_metamodel_actuator_constructor_exists():
    assert callable(metamodel_Actuator.__init__)


def test_metamodel_actuator_constructor_args():
    sig = inspect.signature(metamodel_Actuator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_actuator_has_name():
    assert hasattr(metamodel_Actuator, "name")
    descriptor = None
    for klass in metamodel_Actuator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_sensor_is_not_abstract():
    assert not inspect.isabstract(metamodel_Sensor)


def test_metamodel_sensor_constructor_exists():
    assert callable(metamodel_Sensor.__init__)


def test_metamodel_sensor_constructor_args():
    sig = inspect.signature(metamodel_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sensorName" in params, "Missing parameter 'sensorName'"

def test_metamodel_sensor_has_name():
    assert hasattr(metamodel_Sensor, "name")
    descriptor = None
    for klass in metamodel_Sensor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sensor_has_sensorName():
    assert hasattr(metamodel_Sensor, "sensorName")
    descriptor = None
    for klass in metamodel_Sensor.__mro__:
        if "sensorName" in klass.__dict__:
            descriptor = klass.__dict__["sensorName"]
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
metamodel_Different_strategy = st.builds(
    metamodel_Different,
)
metamodel_More_strategy = st.builds(
    metamodel_More,
)
metamodel_Less_strategy = st.builds(
    metamodel_Less,
)
metamodel_Equal_strategy = st.builds(
    metamodel_Equal,
)
UnaryCond_strategy = st.builds(
    UnaryCond,
)
metamodel_Negation_strategy = st.builds(
    metamodel_Negation,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
metamodel_Positive_strategy = st.builds(
    metamodel_Positive,
)
metamodel_Negative_strategy = st.builds(
    metamodel_Negative,
)
metamodel_Sub_strategy = st.builds(
    metamodel_Sub,
)
metamodel_Add_strategy = st.builds(
    metamodel_Add,
)
metamodel_MoreOrEqual_strategy = st.builds(
    metamodel_MoreOrEqual,
)
metamodel_LessOrEqual_strategy = st.builds(
    metamodel_LessOrEqual,
)
BinaryCond_strategy = st.builds(
    BinaryCond,
)
metamodel_And_strategy = st.builds(
    metamodel_And,
)
metamodel_Or_strategy = st.builds(
    metamodel_Or,
)
Condition_strategy = st.builds(
    Condition,
)
metamodel_UnaryCond_strategy = st.builds(
    metamodel_UnaryCond,
)
metamodel_BinaryCond_strategy = st.builds(
    metamodel_BinaryCond,
)
metamodel_Operator_strategy = st.builds(
    metamodel_Operator,
)
Operator_strategy = st.builds(
    Operator,
)
metamodel_BinaryOperator_strategy = st.builds(
    metamodel_BinaryOperator,
)
metamodel_UnaryOperator_strategy = st.builds(
    metamodel_UnaryOperator,
)
metamodel_Condition_strategy = st.builds(
    metamodel_Condition,
)
metamodel_Value_strategy = st.builds(
    metamodel_Value,
    name=
        safe_text
)
metamodel_Transition_strategy = st.builds(
    metamodel_Transition,
    nameIn=
        safe_text
)
metamodel_State_strategy = st.builds(
    metamodel_State,
    name=
        safe_text,
    isInitial=
        st.booleans(),
    uid=
        st.integers()
)
metamodel_StateMachine_strategy = st.builds(
    metamodel_StateMachine,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
metamodel_FloatVal_strategy = st.builds(
    metamodel_FloatVal,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
metamodel_IntVal_strategy = st.builds(
    metamodel_IntVal,
    value=
        st.integers()
)
metamodel_BoolVal_strategy = st.builds(
    metamodel_BoolVal,
    value=
        st.booleans()
)
metamodel_Type_strategy = st.builds(
    metamodel_Type,
)
Sensor_strategy = st.builds(
    Sensor,
)
metamodel_LightSensor_strategy = st.builds(
    metamodel_LightSensor,
)
metamodel_DistanceSensor_strategy = st.builds(
    metamodel_DistanceSensor,
)
ActionWheel_strategy = st.builds(
    ActionWheel,
)
metamodel_Forward_strategy = st.builds(
    metamodel_Forward,
)
metamodel_Backward_strategy = st.builds(
    metamodel_Backward,
)
metamodel_TurnRight_strategy = st.builds(
    metamodel_TurnRight,
)
metamodel_Stopping_strategy = st.builds(
    metamodel_Stopping,
)
metamodel_TurnLeft_strategy = st.builds(
    metamodel_TurnLeft,
)
Action_strategy = st.builds(
    Action,
)
metamodel_ActionWheel_strategy = st.builds(
    metamodel_ActionWheel,
    speed=
        st.integers()
)
metamodel_Behaviour_strategy = st.builds(
    metamodel_Behaviour,
    priority=
        st.integers(),
    name=
        safe_text
)
metamodel_Robot_strategy = st.builds(
    metamodel_Robot,
    name=
        safe_text
)
Actuator_strategy = st.builds(
    Actuator,
)
metamodel_Group_strategy = st.builds(
    metamodel_Group,
)
metamodel_DifferentialWheel_strategy = st.builds(
    metamodel_DifferentialWheel,
    speed=
        st.integers(),
    isLeft=
        st.booleans()
)
metamodel_Action_strategy = st.builds(
    metamodel_Action,
)
metamodel_Actuator_strategy = st.builds(
    metamodel_Actuator,
    name=
        safe_text
)
metamodel_Sensor_strategy = st.builds(
    metamodel_Sensor,
    name=
        safe_text,
    sensorName=
        safe_text
)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=metamodel_Different_strategy)
@settings(max_examples=50)
def test_metamodel_different_instantiation(instance):
    assert isinstance(instance, metamodel_Different)

@given(instance=metamodel_More_strategy)
@settings(max_examples=50)
def test_metamodel_more_instantiation(instance):
    assert isinstance(instance, metamodel_More)

@given(instance=metamodel_Less_strategy)
@settings(max_examples=50)
def test_metamodel_less_instantiation(instance):
    assert isinstance(instance, metamodel_Less)

@given(instance=metamodel_Equal_strategy)
@settings(max_examples=50)
def test_metamodel_equal_instantiation(instance):
    assert isinstance(instance, metamodel_Equal)

@given(instance=UnaryCond_strategy)
@settings(max_examples=50)
def test_unarycond_instantiation(instance):
    assert isinstance(instance, UnaryCond)

@given(instance=metamodel_Negation_strategy)
@settings(max_examples=50)
def test_metamodel_negation_instantiation(instance):
    assert isinstance(instance, metamodel_Negation)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=metamodel_Positive_strategy)
@settings(max_examples=50)
def test_metamodel_positive_instantiation(instance):
    assert isinstance(instance, metamodel_Positive)

@given(instance=metamodel_Negative_strategy)
@settings(max_examples=50)
def test_metamodel_negative_instantiation(instance):
    assert isinstance(instance, metamodel_Negative)

@given(instance=metamodel_Sub_strategy)
@settings(max_examples=50)
def test_metamodel_sub_instantiation(instance):
    assert isinstance(instance, metamodel_Sub)

@given(instance=metamodel_Add_strategy)
@settings(max_examples=50)
def test_metamodel_add_instantiation(instance):
    assert isinstance(instance, metamodel_Add)

@given(instance=metamodel_MoreOrEqual_strategy)
@settings(max_examples=50)
def test_metamodel_moreorequal_instantiation(instance):
    assert isinstance(instance, metamodel_MoreOrEqual)

@given(instance=metamodel_LessOrEqual_strategy)
@settings(max_examples=50)
def test_metamodel_lessorequal_instantiation(instance):
    assert isinstance(instance, metamodel_LessOrEqual)

@given(instance=BinaryCond_strategy)
@settings(max_examples=50)
def test_binarycond_instantiation(instance):
    assert isinstance(instance, BinaryCond)

@given(instance=metamodel_And_strategy)
@settings(max_examples=50)
def test_metamodel_and_instantiation(instance):
    assert isinstance(instance, metamodel_And)

@given(instance=metamodel_Or_strategy)
@settings(max_examples=50)
def test_metamodel_or_instantiation(instance):
    assert isinstance(instance, metamodel_Or)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=metamodel_UnaryCond_strategy)
@settings(max_examples=50)
def test_metamodel_unarycond_instantiation(instance):
    assert isinstance(instance, metamodel_UnaryCond)

@given(instance=metamodel_BinaryCond_strategy)
@settings(max_examples=50)
def test_metamodel_binarycond_instantiation(instance):
    assert isinstance(instance, metamodel_BinaryCond)

@given(instance=metamodel_Operator_strategy)
@settings(max_examples=50)
def test_metamodel_operator_instantiation(instance):
    assert isinstance(instance, metamodel_Operator)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=metamodel_BinaryOperator_strategy)
@settings(max_examples=50)
def test_metamodel_binaryoperator_instantiation(instance):
    assert isinstance(instance, metamodel_BinaryOperator)

@given(instance=metamodel_UnaryOperator_strategy)
@settings(max_examples=50)
def test_metamodel_unaryoperator_instantiation(instance):
    assert isinstance(instance, metamodel_UnaryOperator)

@given(instance=metamodel_Condition_strategy)
@settings(max_examples=50)
def test_metamodel_condition_instantiation(instance):
    assert isinstance(instance, metamodel_Condition)

@given(instance=metamodel_Value_strategy)
@settings(max_examples=50)
def test_metamodel_value_instantiation(instance):
    assert isinstance(instance, metamodel_Value)



@given(instance=metamodel_Value_strategy)
def test_metamodel_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Transition_strategy)
@settings(max_examples=50)
def test_metamodel_transition_instantiation(instance):
    assert isinstance(instance, metamodel_Transition)



@given(instance=metamodel_Transition_strategy)
def test_metamodel_transition_nameIn_setter(instance):
    original = instance.nameIn
    instance.nameIn = original
    assert instance.nameIn == original

@given(instance=metamodel_State_strategy)
@settings(max_examples=50)
def test_metamodel_state_instantiation(instance):
    assert isinstance(instance, metamodel_State)



@given(instance=metamodel_State_strategy)
def test_metamodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metamodel_State_strategy)
def test_metamodel_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=metamodel_State_strategy)
def test_metamodel_state_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=metamodel_StateMachine_strategy)
@settings(max_examples=50)
def test_metamodel_statemachine_instantiation(instance):
    assert isinstance(instance, metamodel_StateMachine)



@given(instance=metamodel_StateMachine_strategy)
def test_metamodel_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel_FloatVal_strategy)
@settings(max_examples=50)
def test_metamodel_floatval_instantiation(instance):
    assert isinstance(instance, metamodel_FloatVal)



@given(instance=metamodel_FloatVal_strategy)
def test_metamodel_floatval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel_IntVal_strategy)
@settings(max_examples=50)
def test_metamodel_intval_instantiation(instance):
    assert isinstance(instance, metamodel_IntVal)



@given(instance=metamodel_IntVal_strategy)
def test_metamodel_intval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel_BoolVal_strategy)
@settings(max_examples=50)
def test_metamodel_boolval_instantiation(instance):
    assert isinstance(instance, metamodel_BoolVal)



@given(instance=metamodel_BoolVal_strategy)
def test_metamodel_boolval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel_Type_strategy)
@settings(max_examples=50)
def test_metamodel_type_instantiation(instance):
    assert isinstance(instance, metamodel_Type)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=metamodel_LightSensor_strategy)
@settings(max_examples=50)
def test_metamodel_lightsensor_instantiation(instance):
    assert isinstance(instance, metamodel_LightSensor)

@given(instance=metamodel_DistanceSensor_strategy)
@settings(max_examples=50)
def test_metamodel_distancesensor_instantiation(instance):
    assert isinstance(instance, metamodel_DistanceSensor)

@given(instance=ActionWheel_strategy)
@settings(max_examples=50)
def test_actionwheel_instantiation(instance):
    assert isinstance(instance, ActionWheel)

@given(instance=metamodel_Forward_strategy)
@settings(max_examples=50)
def test_metamodel_forward_instantiation(instance):
    assert isinstance(instance, metamodel_Forward)

@given(instance=metamodel_Backward_strategy)
@settings(max_examples=50)
def test_metamodel_backward_instantiation(instance):
    assert isinstance(instance, metamodel_Backward)

@given(instance=metamodel_TurnRight_strategy)
@settings(max_examples=50)
def test_metamodel_turnright_instantiation(instance):
    assert isinstance(instance, metamodel_TurnRight)

@given(instance=metamodel_Stopping_strategy)
@settings(max_examples=50)
def test_metamodel_stopping_instantiation(instance):
    assert isinstance(instance, metamodel_Stopping)

@given(instance=metamodel_TurnLeft_strategy)
@settings(max_examples=50)
def test_metamodel_turnleft_instantiation(instance):
    assert isinstance(instance, metamodel_TurnLeft)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=metamodel_ActionWheel_strategy)
@settings(max_examples=50)
def test_metamodel_actionwheel_instantiation(instance):
    assert isinstance(instance, metamodel_ActionWheel)



@given(instance=metamodel_ActionWheel_strategy)
def test_metamodel_actionwheel_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=metamodel_Behaviour_strategy)
@settings(max_examples=50)
def test_metamodel_behaviour_instantiation(instance):
    assert isinstance(instance, metamodel_Behaviour)



@given(instance=metamodel_Behaviour_strategy)
def test_metamodel_behaviour_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=metamodel_Behaviour_strategy)
def test_metamodel_behaviour_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Robot_strategy)
@settings(max_examples=50)
def test_metamodel_robot_instantiation(instance):
    assert isinstance(instance, metamodel_Robot)



@given(instance=metamodel_Robot_strategy)
def test_metamodel_robot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=metamodel_Group_strategy)
@settings(max_examples=50)
def test_metamodel_group_instantiation(instance):
    assert isinstance(instance, metamodel_Group)

@given(instance=metamodel_DifferentialWheel_strategy)
@settings(max_examples=50)
def test_metamodel_differentialwheel_instantiation(instance):
    assert isinstance(instance, metamodel_DifferentialWheel)



@given(instance=metamodel_DifferentialWheel_strategy)
def test_metamodel_differentialwheel_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=metamodel_DifferentialWheel_strategy)
def test_metamodel_differentialwheel_isLeft_setter(instance):
    original = instance.isLeft
    instance.isLeft = original
    assert instance.isLeft == original

@given(instance=metamodel_Action_strategy)
@settings(max_examples=50)
def test_metamodel_action_instantiation(instance):
    assert isinstance(instance, metamodel_Action)

@given(instance=metamodel_Actuator_strategy)
@settings(max_examples=50)
def test_metamodel_actuator_instantiation(instance):
    assert isinstance(instance, metamodel_Actuator)



@given(instance=metamodel_Actuator_strategy)
def test_metamodel_actuator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Sensor_strategy)
@settings(max_examples=50)
def test_metamodel_sensor_instantiation(instance):
    assert isinstance(instance, metamodel_Sensor)



@given(instance=metamodel_Sensor_strategy)
def test_metamodel_sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metamodel_Sensor_strategy)
def test_metamodel_sensor_sensorName_setter(instance):
    original = instance.sensorName
    instance.sensorName = original
    assert instance.sensorName == original
