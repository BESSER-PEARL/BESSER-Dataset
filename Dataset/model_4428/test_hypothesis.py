import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Condition,
    farrusco::Distancia,
    Action,
    farrusco::Condition,
    Actuate,
    farrusco::LED,
    farrusco::Servo,
    farrusco::Motor,
    farrusco::Actuate,
    farrusco::Espera,
    farrusco::BumperEsquerdo,
    farrusco::BumperDireito,
    Behavior,
    farrusco::Paralelo,
    farrusco::Prioridade,
    farrusco::AlterarEstado,
    Node,
    farrusco::Behavior,
    farrusco::Action,
    farrusco::Robot,
    farrusco::Irmao,
    farrusco::Filho,
    farrusco::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::distancia_is_not_abstract():
    assert not inspect.isabstract(farrusco::Distancia)


def test_farrusco::distancia_constructor_exists():
    assert callable(farrusco::Distancia.__init__)


def test_farrusco::distancia_constructor_args():
    sig = inspect.signature(farrusco::Distancia.__init__)
    params = list(sig.parameters.keys())
    assert "distancia" in params, "Missing parameter 'distancia'"
    assert "how_sucess" in params, "Missing parameter 'how_sucess'"

def test_farrusco::distancia_has_distancia():
    assert hasattr(farrusco::Distancia, "distancia")
    descriptor = None
    for klass in farrusco::Distancia.__mro__:
        if "distancia" in klass.__dict__:
            descriptor = klass.__dict__["distancia"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::distancia_has_how_sucess():
    assert hasattr(farrusco::Distancia, "how_sucess")
    descriptor = None
    for klass in farrusco::Distancia.__mro__:
        if "how_sucess" in klass.__dict__:
            descriptor = klass.__dict__["how_sucess"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::condition_is_not_abstract():
    assert not inspect.isabstract(farrusco::Condition)


def test_farrusco::condition_constructor_exists():
    assert callable(farrusco::Condition.__init__)


def test_farrusco::condition_constructor_args():
    sig = inspect.signature(farrusco::Condition.__init__)
    params = list(sig.parameters.keys())



def test_actuate_is_not_abstract():
    assert not inspect.isabstract(Actuate)


def test_actuate_constructor_exists():
    assert callable(Actuate.__init__)


def test_actuate_constructor_args():
    sig = inspect.signature(Actuate.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::led_is_not_abstract():
    assert not inspect.isabstract(farrusco::LED)


def test_farrusco::led_constructor_exists():
    assert callable(farrusco::LED.__init__)


def test_farrusco::led_constructor_args():
    sig = inspect.signature(farrusco::LED.__init__)
    params = list(sig.parameters.keys())
    assert "on_off" in params, "Missing parameter 'on_off'"

def test_farrusco::led_has_on_off():
    assert hasattr(farrusco::LED, "on_off")
    descriptor = None
    for klass in farrusco::LED.__mro__:
        if "on_off" in klass.__dict__:
            descriptor = klass.__dict__["on_off"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::servo_is_not_abstract():
    assert not inspect.isabstract(farrusco::Servo)


def test_farrusco::servo_constructor_exists():
    assert callable(farrusco::Servo.__init__)


def test_farrusco::servo_constructor_args():
    sig = inspect.signature(farrusco::Servo.__init__)
    params = list(sig.parameters.keys())
    assert "inc" in params, "Missing parameter 'inc'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_farrusco::servo_has_inc():
    assert hasattr(farrusco::Servo, "inc")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "inc" in klass.__dict__:
            descriptor = klass.__dict__["inc"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::servo_has_max():
    assert hasattr(farrusco::Servo, "max")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::servo_has_min():
    assert hasattr(farrusco::Servo, "min")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::motor_is_not_abstract():
    assert not inspect.isabstract(farrusco::Motor)


def test_farrusco::motor_constructor_exists():
    assert callable(farrusco::Motor.__init__)


def test_farrusco::motor_constructor_args():
    sig = inspect.signature(farrusco::Motor.__init__)
    params = list(sig.parameters.keys())
    assert "MotorLeft" in params, "Missing parameter 'MotorLeft'"
    assert "MotorRight" in params, "Missing parameter 'MotorRight'"

def test_farrusco::motor_has_MotorLeft():
    assert hasattr(farrusco::Motor, "MotorLeft")
    descriptor = None
    for klass in farrusco::Motor.__mro__:
        if "MotorLeft" in klass.__dict__:
            descriptor = klass.__dict__["MotorLeft"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::motor_has_MotorRight():
    assert hasattr(farrusco::Motor, "MotorRight")
    descriptor = None
    for klass in farrusco::Motor.__mro__:
        if "MotorRight" in klass.__dict__:
            descriptor = klass.__dict__["MotorRight"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::actuate_is_not_abstract():
    assert not inspect.isabstract(farrusco::Actuate)


def test_farrusco::actuate_constructor_exists():
    assert callable(farrusco::Actuate.__init__)


def test_farrusco::actuate_constructor_args():
    sig = inspect.signature(farrusco::Actuate.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::espera_is_not_abstract():
    assert not inspect.isabstract(farrusco::Espera)


def test_farrusco::espera_constructor_exists():
    assert callable(farrusco::Espera.__init__)


def test_farrusco::espera_constructor_args():
    sig = inspect.signature(farrusco::Espera.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_farrusco::espera_has_time():
    assert hasattr(farrusco::Espera, "time")
    descriptor = None
    for klass in farrusco::Espera.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::bumperesquerdo_is_not_abstract():
    assert not inspect.isabstract(farrusco::BumperEsquerdo)


def test_farrusco::bumperesquerdo_constructor_exists():
    assert callable(farrusco::BumperEsquerdo.__init__)


def test_farrusco::bumperesquerdo_constructor_args():
    sig = inspect.signature(farrusco::BumperEsquerdo.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::bumperdireito_is_not_abstract():
    assert not inspect.isabstract(farrusco::BumperDireito)


def test_farrusco::bumperdireito_constructor_exists():
    assert callable(farrusco::BumperDireito.__init__)


def test_farrusco::bumperdireito_constructor_args():
    sig = inspect.signature(farrusco::BumperDireito.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::paralelo_is_not_abstract():
    assert not inspect.isabstract(farrusco::Paralelo)


def test_farrusco::paralelo_constructor_exists():
    assert callable(farrusco::Paralelo.__init__)


def test_farrusco::paralelo_constructor_args():
    sig = inspect.signature(farrusco::Paralelo.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::prioridade_is_not_abstract():
    assert not inspect.isabstract(farrusco::Prioridade)


def test_farrusco::prioridade_constructor_exists():
    assert callable(farrusco::Prioridade.__init__)


def test_farrusco::prioridade_constructor_args():
    sig = inspect.signature(farrusco::Prioridade.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::alterarestado_is_not_abstract():
    assert not inspect.isabstract(farrusco::AlterarEstado)


def test_farrusco::alterarestado_constructor_exists():
    assert callable(farrusco::AlterarEstado.__init__)


def test_farrusco::alterarestado_constructor_args():
    sig = inspect.signature(farrusco::AlterarEstado.__init__)
    params = list(sig.parameters.keys())
    assert "fail_policy" in params, "Missing parameter 'fail_policy'"
    assert "runn_policy" in params, "Missing parameter 'runn_policy'"
    assert "succ_policy" in params, "Missing parameter 'succ_policy'"

def test_farrusco::alterarestado_has_fail_policy():
    assert hasattr(farrusco::AlterarEstado, "fail_policy")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "fail_policy" in klass.__dict__:
            descriptor = klass.__dict__["fail_policy"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::alterarestado_has_runn_policy():
    assert hasattr(farrusco::AlterarEstado, "runn_policy")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "runn_policy" in klass.__dict__:
            descriptor = klass.__dict__["runn_policy"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::alterarestado_has_succ_policy():
    assert hasattr(farrusco::AlterarEstado, "succ_policy")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "succ_policy" in klass.__dict__:
            descriptor = klass.__dict__["succ_policy"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::behavior_is_not_abstract():
    assert not inspect.isabstract(farrusco::Behavior)


def test_farrusco::behavior_constructor_exists():
    assert callable(farrusco::Behavior.__init__)


def test_farrusco::behavior_constructor_args():
    sig = inspect.signature(farrusco::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_farrusco::behavior_has_Name():
    assert hasattr(farrusco::Behavior, "Name")
    descriptor = None
    for klass in farrusco::Behavior.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::action_is_not_abstract():
    assert not inspect.isabstract(farrusco::Action)


def test_farrusco::action_constructor_exists():
    assert callable(farrusco::Action.__init__)


def test_farrusco::action_constructor_args():
    sig = inspect.signature(farrusco::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_farrusco::action_has_name():
    assert hasattr(farrusco::Action, "name")
    descriptor = None
    for klass in farrusco::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::robot_is_not_abstract():
    assert not inspect.isabstract(farrusco::Robot)


def test_farrusco::robot_constructor_exists():
    assert callable(farrusco::Robot.__init__)


def test_farrusco::robot_constructor_args():
    sig = inspect.signature(farrusco::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_farrusco::robot_has_Name():
    assert hasattr(farrusco::Robot, "Name")
    descriptor = None
    for klass in farrusco::Robot.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::irmao_is_not_abstract():
    assert not inspect.isabstract(farrusco::Irmao)


def test_farrusco::irmao_constructor_exists():
    assert callable(farrusco::Irmao.__init__)


def test_farrusco::irmao_constructor_args():
    sig = inspect.signature(farrusco::Irmao.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::filho_is_not_abstract():
    assert not inspect.isabstract(farrusco::Filho)


def test_farrusco::filho_constructor_exists():
    assert callable(farrusco::Filho.__init__)


def test_farrusco::filho_constructor_args():
    sig = inspect.signature(farrusco::Filho.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::node_is_not_abstract():
    assert not inspect.isabstract(farrusco::Node)


def test_farrusco::node_constructor_exists():
    assert callable(farrusco::Node.__init__)


def test_farrusco::node_constructor_args():
    sig = inspect.signature(farrusco::Node.__init__)
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
Condition_strategy = st.builds(
    Condition,
)
farrusco::Distancia_strategy = st.builds(
    farrusco::Distancia,
    distancia=
        st.integers(),
    how_sucess=
        st.booleans()
)
Action_strategy = st.builds(
    Action,
)
farrusco::Condition_strategy = st.builds(
    farrusco::Condition,
)
Actuate_strategy = st.builds(
    Actuate,
)
farrusco::LED_strategy = st.builds(
    farrusco::LED,
    on_off=
        st.booleans()
)
farrusco::Servo_strategy = st.builds(
    farrusco::Servo,
    inc=
        st.integers(),
    max=
        st.integers(),
    min=
        st.integers()
)
farrusco::Motor_strategy = st.builds(
    farrusco::Motor,
    MotorLeft=
        st.integers(),
    MotorRight=
        st.integers()
)
farrusco::Actuate_strategy = st.builds(
    farrusco::Actuate,
)
farrusco::Espera_strategy = st.builds(
    farrusco::Espera,
    time=
        st.integers()
)
farrusco::BumperEsquerdo_strategy = st.builds(
    farrusco::BumperEsquerdo,
)
farrusco::BumperDireito_strategy = st.builds(
    farrusco::BumperDireito,
)
Behavior_strategy = st.builds(
    Behavior,
)
farrusco::Paralelo_strategy = st.builds(
    farrusco::Paralelo,
)
farrusco::Prioridade_strategy = st.builds(
    farrusco::Prioridade,
)
farrusco::AlterarEstado_strategy = st.builds(
    farrusco::AlterarEstado,
    fail_policy=
        st.integers(),
    runn_policy=
        st.integers(),
    succ_policy=
        st.integers()
)
Node_strategy = st.builds(
    Node,
)
farrusco::Behavior_strategy = st.builds(
    farrusco::Behavior,
    Name=
        safe_text
)
farrusco::Action_strategy = st.builds(
    farrusco::Action,
    name=
        safe_text
)
farrusco::Robot_strategy = st.builds(
    farrusco::Robot,
    Name=
        safe_text
)
farrusco::Irmao_strategy = st.builds(
    farrusco::Irmao,
)
farrusco::Filho_strategy = st.builds(
    farrusco::Filho,
)
farrusco::Node_strategy = st.builds(
    farrusco::Node,
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=farrusco::Distancia_strategy)
@settings(max_examples=50)
def test_farrusco::distancia_instantiation(instance):
    assert isinstance(instance, farrusco::Distancia)

@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_distancia_type(instance):
    assert isinstance(instance.distancia, int)


@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_distancia_setter(instance):
    original = instance.distancia
    instance.distancia = original
    assert instance.distancia == original

@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_how_sucess_type(instance):
    assert isinstance(instance.how_sucess, bool)


@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_how_sucess_setter(instance):
    original = instance.how_sucess
    instance.how_sucess = original
    assert instance.how_sucess == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=farrusco::Condition_strategy)
@settings(max_examples=50)
def test_farrusco::condition_instantiation(instance):
    assert isinstance(instance, farrusco::Condition)

@given(instance=Actuate_strategy)
@settings(max_examples=50)
def test_actuate_instantiation(instance):
    assert isinstance(instance, Actuate)

@given(instance=farrusco::LED_strategy)
@settings(max_examples=50)
def test_farrusco::led_instantiation(instance):
    assert isinstance(instance, farrusco::LED)

@given(instance=farrusco::LED_strategy)
def test_farrusco::led_on_off_type(instance):
    assert isinstance(instance.on_off, bool)


@given(instance=farrusco::LED_strategy)
def test_farrusco::led_on_off_setter(instance):
    original = instance.on_off
    instance.on_off = original
    assert instance.on_off == original

@given(instance=farrusco::Servo_strategy)
@settings(max_examples=50)
def test_farrusco::servo_instantiation(instance):
    assert isinstance(instance, farrusco::Servo)

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_inc_type(instance):
    assert isinstance(instance.inc, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_inc_setter(instance):
    original = instance.inc
    instance.inc = original
    assert instance.inc == original

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=farrusco::Motor_strategy)
@settings(max_examples=50)
def test_farrusco::motor_instantiation(instance):
    assert isinstance(instance, farrusco::Motor)

@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_MotorLeft_type(instance):
    assert isinstance(instance.MotorLeft, int)


@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_MotorLeft_setter(instance):
    original = instance.MotorLeft
    instance.MotorLeft = original
    assert instance.MotorLeft == original

@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_MotorRight_type(instance):
    assert isinstance(instance.MotorRight, int)


@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_MotorRight_setter(instance):
    original = instance.MotorRight
    instance.MotorRight = original
    assert instance.MotorRight == original

@given(instance=farrusco::Actuate_strategy)
@settings(max_examples=50)
def test_farrusco::actuate_instantiation(instance):
    assert isinstance(instance, farrusco::Actuate)

@given(instance=farrusco::Espera_strategy)
@settings(max_examples=50)
def test_farrusco::espera_instantiation(instance):
    assert isinstance(instance, farrusco::Espera)

@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=farrusco::BumperEsquerdo_strategy)
@settings(max_examples=50)
def test_farrusco::bumperesquerdo_instantiation(instance):
    assert isinstance(instance, farrusco::BumperEsquerdo)

@given(instance=farrusco::BumperDireito_strategy)
@settings(max_examples=50)
def test_farrusco::bumperdireito_instantiation(instance):
    assert isinstance(instance, farrusco::BumperDireito)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=farrusco::Paralelo_strategy)
@settings(max_examples=50)
def test_farrusco::paralelo_instantiation(instance):
    assert isinstance(instance, farrusco::Paralelo)

@given(instance=farrusco::Prioridade_strategy)
@settings(max_examples=50)
def test_farrusco::prioridade_instantiation(instance):
    assert isinstance(instance, farrusco::Prioridade)

@given(instance=farrusco::AlterarEstado_strategy)
@settings(max_examples=50)
def test_farrusco::alterarestado_instantiation(instance):
    assert isinstance(instance, farrusco::AlterarEstado)

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_fail_policy_type(instance):
    assert isinstance(instance.fail_policy, int)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_fail_policy_setter(instance):
    original = instance.fail_policy
    instance.fail_policy = original
    assert instance.fail_policy == original

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_runn_policy_type(instance):
    assert isinstance(instance.runn_policy, int)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_runn_policy_setter(instance):
    original = instance.runn_policy
    instance.runn_policy = original
    assert instance.runn_policy == original

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_succ_policy_type(instance):
    assert isinstance(instance.succ_policy, int)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_succ_policy_setter(instance):
    original = instance.succ_policy
    instance.succ_policy = original
    assert instance.succ_policy == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=farrusco::Behavior_strategy)
@settings(max_examples=50)
def test_farrusco::behavior_instantiation(instance):
    assert isinstance(instance, farrusco::Behavior)

@given(instance=farrusco::Behavior_strategy)
def test_farrusco::behavior_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=farrusco::Behavior_strategy)
def test_farrusco::behavior_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=farrusco::Action_strategy)
@settings(max_examples=50)
def test_farrusco::action_instantiation(instance):
    assert isinstance(instance, farrusco::Action)

@given(instance=farrusco::Action_strategy)
def test_farrusco::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=farrusco::Action_strategy)
def test_farrusco::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=farrusco::Robot_strategy)
@settings(max_examples=50)
def test_farrusco::robot_instantiation(instance):
    assert isinstance(instance, farrusco::Robot)

@given(instance=farrusco::Robot_strategy)
def test_farrusco::robot_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=farrusco::Robot_strategy)
def test_farrusco::robot_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=farrusco::Irmao_strategy)
@settings(max_examples=50)
def test_farrusco::irmao_instantiation(instance):
    assert isinstance(instance, farrusco::Irmao)

@given(instance=farrusco::Filho_strategy)
@settings(max_examples=50)
def test_farrusco::filho_instantiation(instance):
    assert isinstance(instance, farrusco::Filho)

@given(instance=farrusco::Node_strategy)
@settings(max_examples=50)
def test_farrusco::node_instantiation(instance):
    assert isinstance(instance, farrusco::Node)
