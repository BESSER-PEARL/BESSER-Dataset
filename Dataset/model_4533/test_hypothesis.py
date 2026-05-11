import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    robotG::flow::Programme,
    OpBinaire,
    robotG::flow::Or,
    robotG::flow::And,
    robotG::flow::Expr,
    OpUnaire,
    robotG::flow::Not,
    ExprBool,
    robotG::flow::OpUnaire,
    robotG::flow::OpBinaire,
    Expr,
    robotG::flow::ExprBool,
    robotG::flow::If,
    robotG::flow::StopProgram,
    robotG::flow::While,
    robotG::robot::CommandeRobot,
    robot::CommandeRobot,
    flow::ExprBool,
    robotG::robot::Obstacle,
    robotG::robot::HasTurned,
    CommandeRobot,
    robotG::robot::StopEngine,
    robotG::robot::Bip,
    robotG::robot::Display,
    robotG::robot::SetTurnAngle,
    robotG::robot::Turn,
    robotG::robot::Move,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robotg::flow::programme_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::Programme)


def test_robotg::flow::programme_constructor_exists():
    assert callable(robotG::flow::Programme.__init__)


def test_robotg::flow::programme_constructor_args():
    sig = inspect.signature(robotG::flow::Programme.__init__)
    params = list(sig.parameters.keys())



def test_opbinaire_is_not_abstract():
    assert not inspect.isabstract(OpBinaire)


def test_opbinaire_constructor_exists():
    assert callable(OpBinaire.__init__)


def test_opbinaire_constructor_args():
    sig = inspect.signature(OpBinaire.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::or_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::Or)


def test_robotg::flow::or_constructor_exists():
    assert callable(robotG::flow::Or.__init__)


def test_robotg::flow::or_constructor_args():
    sig = inspect.signature(robotG::flow::Or.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::and_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::And)


def test_robotg::flow::and_constructor_exists():
    assert callable(robotG::flow::And.__init__)


def test_robotg::flow::and_constructor_args():
    sig = inspect.signature(robotG::flow::And.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::expr_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::Expr)


def test_robotg::flow::expr_constructor_exists():
    assert callable(robotG::flow::Expr.__init__)


def test_robotg::flow::expr_constructor_args():
    sig = inspect.signature(robotG::flow::Expr.__init__)
    params = list(sig.parameters.keys())



def test_opunaire_is_not_abstract():
    assert not inspect.isabstract(OpUnaire)


def test_opunaire_constructor_exists():
    assert callable(OpUnaire.__init__)


def test_opunaire_constructor_args():
    sig = inspect.signature(OpUnaire.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::not_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::Not)


def test_robotg::flow::not_constructor_exists():
    assert callable(robotG::flow::Not.__init__)


def test_robotg::flow::not_constructor_args():
    sig = inspect.signature(robotG::flow::Not.__init__)
    params = list(sig.parameters.keys())



def test_exprbool_is_not_abstract():
    assert not inspect.isabstract(ExprBool)


def test_exprbool_constructor_exists():
    assert callable(ExprBool.__init__)


def test_exprbool_constructor_args():
    sig = inspect.signature(ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::opunaire_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::OpUnaire)


def test_robotg::flow::opunaire_constructor_exists():
    assert callable(robotG::flow::OpUnaire.__init__)


def test_robotg::flow::opunaire_constructor_args():
    sig = inspect.signature(robotG::flow::OpUnaire.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::opbinaire_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::OpBinaire)


def test_robotg::flow::opbinaire_constructor_exists():
    assert callable(robotG::flow::OpBinaire.__init__)


def test_robotg::flow::opbinaire_constructor_args():
    sig = inspect.signature(robotG::flow::OpBinaire.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::exprbool_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::ExprBool)


def test_robotg::flow::exprbool_constructor_exists():
    assert callable(robotG::flow::ExprBool.__init__)


def test_robotg::flow::exprbool_constructor_args():
    sig = inspect.signature(robotG::flow::ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::if_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::If)


def test_robotg::flow::if_constructor_exists():
    assert callable(robotG::flow::If.__init__)


def test_robotg::flow::if_constructor_args():
    sig = inspect.signature(robotG::flow::If.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::stopprogram_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::StopProgram)


def test_robotg::flow::stopprogram_constructor_exists():
    assert callable(robotG::flow::StopProgram.__init__)


def test_robotg::flow::stopprogram_constructor_args():
    sig = inspect.signature(robotG::flow::StopProgram.__init__)
    params = list(sig.parameters.keys())



def test_robotg::flow::while_is_not_abstract():
    assert not inspect.isabstract(robotG::flow::While)


def test_robotg::flow::while_constructor_exists():
    assert callable(robotG::flow::While.__init__)


def test_robotg::flow::while_constructor_args():
    sig = inspect.signature(robotG::flow::While.__init__)
    params = list(sig.parameters.keys())



def test_robotg::robot::commanderobot_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::CommandeRobot)


def test_robotg::robot::commanderobot_constructor_exists():
    assert callable(robotG::robot::CommandeRobot.__init__)


def test_robotg::robot::commanderobot_constructor_args():
    sig = inspect.signature(robotG::robot::CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_robot::commanderobot_is_not_abstract():
    assert not inspect.isabstract(robot::CommandeRobot)


def test_robot::commanderobot_constructor_exists():
    assert callable(robot::CommandeRobot.__init__)


def test_robot::commanderobot_constructor_args():
    sig = inspect.signature(robot::CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_flow::exprbool_is_not_abstract():
    assert not inspect.isabstract(flow::ExprBool)


def test_flow::exprbool_constructor_exists():
    assert callable(flow::ExprBool.__init__)


def test_flow::exprbool_constructor_args():
    sig = inspect.signature(flow::ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_robotg::robot::obstacle_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::Obstacle)


def test_robotg::robot::obstacle_constructor_exists():
    assert callable(robotG::robot::Obstacle.__init__)


def test_robotg::robot::obstacle_constructor_args():
    sig = inspect.signature(robotG::robot::Obstacle.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_robotg::robot::obstacle_has_distance():
    assert hasattr(robotG::robot::Obstacle, "distance")
    descriptor = None
    for klass in robotG::robot::Obstacle.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_robotg::robot::hasturned_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::HasTurned)


def test_robotg::robot::hasturned_constructor_exists():
    assert callable(robotG::robot::HasTurned.__init__)


def test_robotg::robot::hasturned_constructor_args():
    sig = inspect.signature(robotG::robot::HasTurned.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_robotg::robot::hasturned_has_angle():
    assert hasattr(robotG::robot::HasTurned, "angle")
    descriptor = None
    for klass in robotG::robot::HasTurned.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_commanderobot_is_not_abstract():
    assert not inspect.isabstract(CommandeRobot)


def test_commanderobot_constructor_exists():
    assert callable(CommandeRobot.__init__)


def test_commanderobot_constructor_args():
    sig = inspect.signature(CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_robotg::robot::stopengine_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::StopEngine)


def test_robotg::robot::stopengine_constructor_exists():
    assert callable(robotG::robot::StopEngine.__init__)


def test_robotg::robot::stopengine_constructor_args():
    sig = inspect.signature(robotG::robot::StopEngine.__init__)
    params = list(sig.parameters.keys())



def test_robotg::robot::bip_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::Bip)


def test_robotg::robot::bip_constructor_exists():
    assert callable(robotG::robot::Bip.__init__)


def test_robotg::robot::bip_constructor_args():
    sig = inspect.signature(robotG::robot::Bip.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_robotg::robot::bip_has_power():
    assert hasattr(robotG::robot::Bip, "power")
    descriptor = None
    for klass in robotG::robot::Bip.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::bip_has_repeat():
    assert hasattr(robotG::robot::Bip, "repeat")
    descriptor = None
    for klass in robotG::robot::Bip.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::bip_has_duration():
    assert hasattr(robotG::robot::Bip, "duration")
    descriptor = None
    for klass in robotG::robot::Bip.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_robotg::robot::display_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::Display)


def test_robotg::robot::display_constructor_exists():
    assert callable(robotG::robot::Display.__init__)


def test_robotg::robot::display_constructor_args():
    sig = inspect.signature(robotG::robot::Display.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "line" in params, "Missing parameter 'line'"
    assert "col" in params, "Missing parameter 'col'"
    assert "msg" in params, "Missing parameter 'msg'"

def test_robotg::robot::display_has_duration():
    assert hasattr(robotG::robot::Display, "duration")
    descriptor = None
    for klass in robotG::robot::Display.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::display_has_line():
    assert hasattr(robotG::robot::Display, "line")
    descriptor = None
    for klass in robotG::robot::Display.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::display_has_col():
    assert hasattr(robotG::robot::Display, "col")
    descriptor = None
    for klass in robotG::robot::Display.__mro__:
        if "col" in klass.__dict__:
            descriptor = klass.__dict__["col"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::display_has_msg():
    assert hasattr(robotG::robot::Display, "msg")
    descriptor = None
    for klass in robotG::robot::Display.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)



def test_robotg::robot::setturnangle_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::SetTurnAngle)


def test_robotg::robot::setturnangle_constructor_exists():
    assert callable(robotG::robot::SetTurnAngle.__init__)


def test_robotg::robot::setturnangle_constructor_args():
    sig = inspect.signature(robotG::robot::SetTurnAngle.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_robotg::robot::setturnangle_has_angle():
    assert hasattr(robotG::robot::SetTurnAngle, "angle")
    descriptor = None
    for klass in robotG::robot::SetTurnAngle.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_robotg::robot::turn_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::Turn)


def test_robotg::robot::turn_constructor_exists():
    assert callable(robotG::robot::Turn.__init__)


def test_robotg::robot::turn_constructor_args():
    sig = inspect.signature(robotG::robot::Turn.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_robotg::robot::turn_has_power():
    assert hasattr(robotG::robot::Turn, "power")
    descriptor = None
    for klass in robotG::robot::Turn.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_robotg::robot::turn_has_angle():
    assert hasattr(robotG::robot::Turn, "angle")
    descriptor = None
    for klass in robotG::robot::Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_robotg::robot::move_is_not_abstract():
    assert not inspect.isabstract(robotG::robot::Move)


def test_robotg::robot::move_constructor_exists():
    assert callable(robotG::robot::Move.__init__)


def test_robotg::robot::move_constructor_args():
    sig = inspect.signature(robotG::robot::Move.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_robotg::robot::move_has_power():
    assert hasattr(robotG::robot::Move, "power")
    descriptor = None
    for klass in robotG::robot::Move.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
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
robotG::flow::Programme_strategy = st.builds(
    robotG::flow::Programme,
)
OpBinaire_strategy = st.builds(
    OpBinaire,
)
robotG::flow::Or_strategy = st.builds(
    robotG::flow::Or,
)
robotG::flow::And_strategy = st.builds(
    robotG::flow::And,
)
robotG::flow::Expr_strategy = st.builds(
    robotG::flow::Expr,
)
OpUnaire_strategy = st.builds(
    OpUnaire,
)
robotG::flow::Not_strategy = st.builds(
    robotG::flow::Not,
)
ExprBool_strategy = st.builds(
    ExprBool,
)
robotG::flow::OpUnaire_strategy = st.builds(
    robotG::flow::OpUnaire,
)
robotG::flow::OpBinaire_strategy = st.builds(
    robotG::flow::OpBinaire,
)
Expr_strategy = st.builds(
    Expr,
)
robotG::flow::ExprBool_strategy = st.builds(
    robotG::flow::ExprBool,
)
robotG::flow::If_strategy = st.builds(
    robotG::flow::If,
)
robotG::flow::StopProgram_strategy = st.builds(
    robotG::flow::StopProgram,
)
robotG::flow::While_strategy = st.builds(
    robotG::flow::While,
)
robotG::robot::CommandeRobot_strategy = st.builds(
    robotG::robot::CommandeRobot,
)
robot::CommandeRobot_strategy = st.builds(
    robot::CommandeRobot,
)
flow::ExprBool_strategy = st.builds(
    flow::ExprBool,
)
robotG::robot::Obstacle_strategy = st.builds(
    robotG::robot::Obstacle,
    distance=
        st.integers()
)
robotG::robot::HasTurned_strategy = st.builds(
    robotG::robot::HasTurned,
    angle=
        st.integers()
)
CommandeRobot_strategy = st.builds(
    CommandeRobot,
)
robotG::robot::StopEngine_strategy = st.builds(
    robotG::robot::StopEngine,
)
robotG::robot::Bip_strategy = st.builds(
    robotG::robot::Bip,
    power=
        st.integers(),
    repeat=
        st.booleans(),
    duration=
        st.integers()
)
robotG::robot::Display_strategy = st.builds(
    robotG::robot::Display,
    duration=
        st.integers(),
    line=
        st.integers(),
    col=
        st.integers(),
    msg=
        safe_text
)
robotG::robot::SetTurnAngle_strategy = st.builds(
    robotG::robot::SetTurnAngle,
    angle=
        st.integers()
)
robotG::robot::Turn_strategy = st.builds(
    robotG::robot::Turn,
    power=
        st.integers(),
    angle=
        st.integers()
)
robotG::robot::Move_strategy = st.builds(
    robotG::robot::Move,
    power=
        st.integers()
)

@given(instance=robotG::flow::Programme_strategy)
@settings(max_examples=50)
def test_robotg::flow::programme_instantiation(instance):
    assert isinstance(instance, robotG::flow::Programme)

@given(instance=OpBinaire_strategy)
@settings(max_examples=50)
def test_opbinaire_instantiation(instance):
    assert isinstance(instance, OpBinaire)

@given(instance=robotG::flow::Or_strategy)
@settings(max_examples=50)
def test_robotg::flow::or_instantiation(instance):
    assert isinstance(instance, robotG::flow::Or)

@given(instance=robotG::flow::And_strategy)
@settings(max_examples=50)
def test_robotg::flow::and_instantiation(instance):
    assert isinstance(instance, robotG::flow::And)

@given(instance=robotG::flow::Expr_strategy)
@settings(max_examples=50)
def test_robotg::flow::expr_instantiation(instance):
    assert isinstance(instance, robotG::flow::Expr)

@given(instance=OpUnaire_strategy)
@settings(max_examples=50)
def test_opunaire_instantiation(instance):
    assert isinstance(instance, OpUnaire)

@given(instance=robotG::flow::Not_strategy)
@settings(max_examples=50)
def test_robotg::flow::not_instantiation(instance):
    assert isinstance(instance, robotG::flow::Not)

@given(instance=ExprBool_strategy)
@settings(max_examples=50)
def test_exprbool_instantiation(instance):
    assert isinstance(instance, ExprBool)

@given(instance=robotG::flow::OpUnaire_strategy)
@settings(max_examples=50)
def test_robotg::flow::opunaire_instantiation(instance):
    assert isinstance(instance, robotG::flow::OpUnaire)

@given(instance=robotG::flow::OpBinaire_strategy)
@settings(max_examples=50)
def test_robotg::flow::opbinaire_instantiation(instance):
    assert isinstance(instance, robotG::flow::OpBinaire)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=robotG::flow::ExprBool_strategy)
@settings(max_examples=50)
def test_robotg::flow::exprbool_instantiation(instance):
    assert isinstance(instance, robotG::flow::ExprBool)

@given(instance=robotG::flow::If_strategy)
@settings(max_examples=50)
def test_robotg::flow::if_instantiation(instance):
    assert isinstance(instance, robotG::flow::If)

@given(instance=robotG::flow::StopProgram_strategy)
@settings(max_examples=50)
def test_robotg::flow::stopprogram_instantiation(instance):
    assert isinstance(instance, robotG::flow::StopProgram)

@given(instance=robotG::flow::While_strategy)
@settings(max_examples=50)
def test_robotg::flow::while_instantiation(instance):
    assert isinstance(instance, robotG::flow::While)

@given(instance=robotG::robot::CommandeRobot_strategy)
@settings(max_examples=50)
def test_robotg::robot::commanderobot_instantiation(instance):
    assert isinstance(instance, robotG::robot::CommandeRobot)

@given(instance=robot::CommandeRobot_strategy)
@settings(max_examples=50)
def test_robot::commanderobot_instantiation(instance):
    assert isinstance(instance, robot::CommandeRobot)

@given(instance=flow::ExprBool_strategy)
@settings(max_examples=50)
def test_flow::exprbool_instantiation(instance):
    assert isinstance(instance, flow::ExprBool)

@given(instance=robotG::robot::Obstacle_strategy)
@settings(max_examples=50)
def test_robotg::robot::obstacle_instantiation(instance):
    assert isinstance(instance, robotG::robot::Obstacle)

@given(instance=robotG::robot::Obstacle_strategy)
def test_robotg::robot::obstacle_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=robotG::robot::Obstacle_strategy)
def test_robotg::robot::obstacle_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=robotG::robot::HasTurned_strategy)
@settings(max_examples=50)
def test_robotg::robot::hasturned_instantiation(instance):
    assert isinstance(instance, robotG::robot::HasTurned)

@given(instance=robotG::robot::HasTurned_strategy)
def test_robotg::robot::hasturned_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=robotG::robot::HasTurned_strategy)
def test_robotg::robot::hasturned_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=CommandeRobot_strategy)
@settings(max_examples=50)
def test_commanderobot_instantiation(instance):
    assert isinstance(instance, CommandeRobot)

@given(instance=robotG::robot::StopEngine_strategy)
@settings(max_examples=50)
def test_robotg::robot::stopengine_instantiation(instance):
    assert isinstance(instance, robotG::robot::StopEngine)

@given(instance=robotG::robot::Bip_strategy)
@settings(max_examples=50)
def test_robotg::robot::bip_instantiation(instance):
    assert isinstance(instance, robotG::robot::Bip)

@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_power_type(instance):
    assert isinstance(instance.power, int)


@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_repeat_type(instance):
    assert isinstance(instance.repeat, bool)


@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=robotG::robot::Bip_strategy)
def test_robotg::robot::bip_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=robotG::robot::Display_strategy)
@settings(max_examples=50)
def test_robotg::robot::display_instantiation(instance):
    assert isinstance(instance, robotG::robot::Display)

@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_col_type(instance):
    assert isinstance(instance.col, int)


@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_col_setter(instance):
    original = instance.col
    instance.col = original
    assert instance.col == original

@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_msg_type(instance):
    assert isinstance(instance.msg, str)


@given(instance=robotG::robot::Display_strategy)
def test_robotg::robot::display_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=robotG::robot::SetTurnAngle_strategy)
@settings(max_examples=50)
def test_robotg::robot::setturnangle_instantiation(instance):
    assert isinstance(instance, robotG::robot::SetTurnAngle)

@given(instance=robotG::robot::SetTurnAngle_strategy)
def test_robotg::robot::setturnangle_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=robotG::robot::SetTurnAngle_strategy)
def test_robotg::robot::setturnangle_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=robotG::robot::Turn_strategy)
@settings(max_examples=50)
def test_robotg::robot::turn_instantiation(instance):
    assert isinstance(instance, robotG::robot::Turn)

@given(instance=robotG::robot::Turn_strategy)
def test_robotg::robot::turn_power_type(instance):
    assert isinstance(instance.power, int)


@given(instance=robotG::robot::Turn_strategy)
def test_robotg::robot::turn_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=robotG::robot::Turn_strategy)
def test_robotg::robot::turn_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=robotG::robot::Turn_strategy)
def test_robotg::robot::turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=robotG::robot::Move_strategy)
@settings(max_examples=50)
def test_robotg::robot::move_instantiation(instance):
    assert isinstance(instance, robotG::robot::Move)

@given(instance=robotG::robot::Move_strategy)
def test_robotg::robot::move_power_type(instance):
    assert isinstance(instance.power, int)


@given(instance=robotG::robot::Move_strategy)
def test_robotg::robot::move_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original
