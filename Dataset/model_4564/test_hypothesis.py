import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    robot::robot::ProgramUnit,
    robot::Command,
    FlotCtrl::BoolExp,
    robot::robot::HasTurnedCmd,
    robot::robot::ObstacleCmd,
    Command,
    robot::robot::StopProgramCmd,
    robot::robot::PrintCmd,
    robot::robot::Bip,
    robot::robot::SetTurnAngleCmd,
    robot::robot::StopEngineCmd,
    robot::robot::TurnCmd,
    robot::robot::MoveCmd,
    BoolExp,
    robot::FlotCtrl::NegExp,
    robot::FlotCtrl::AndExp,
    robot::FlotCtrl::Expression,
    Expression,
    robot::FlotCtrl::BoolExp,
    robot::FlotCtrl::WhileLoop,
    robot::FlotCtrl::IfBlock,
    robot::robot::Command,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robot::robot::programunit_is_not_abstract():
    assert not inspect.isabstract(robot::robot::ProgramUnit)


def test_robot::robot::programunit_constructor_exists():
    assert callable(robot::robot::ProgramUnit.__init__)


def test_robot::robot::programunit_constructor_args():
    sig = inspect.signature(robot::robot::ProgramUnit.__init__)
    params = list(sig.parameters.keys())



def test_robot::command_is_not_abstract():
    assert not inspect.isabstract(robot::Command)


def test_robot::command_constructor_exists():
    assert callable(robot::Command.__init__)


def test_robot::command_constructor_args():
    sig = inspect.signature(robot::Command.__init__)
    params = list(sig.parameters.keys())



def test_flotctrl::boolexp_is_not_abstract():
    assert not inspect.isabstract(FlotCtrl::BoolExp)


def test_flotctrl::boolexp_constructor_exists():
    assert callable(FlotCtrl::BoolExp.__init__)


def test_flotctrl::boolexp_constructor_args():
    sig = inspect.signature(FlotCtrl::BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_robot::robot::hasturnedcmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::HasTurnedCmd)


def test_robot::robot::hasturnedcmd_constructor_exists():
    assert callable(robot::robot::HasTurnedCmd.__init__)


def test_robot::robot::hasturnedcmd_constructor_args():
    sig = inspect.signature(robot::robot::HasTurnedCmd.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_robot::robot::hasturnedcmd_has_angle():
    assert hasattr(robot::robot::HasTurnedCmd, "angle")
    descriptor = None
    for klass in robot::robot::HasTurnedCmd.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_robot::robot::obstaclecmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::ObstacleCmd)


def test_robot::robot::obstaclecmd_constructor_exists():
    assert callable(robot::robot::ObstacleCmd.__init__)


def test_robot::robot::obstaclecmd_constructor_args():
    sig = inspect.signature(robot::robot::ObstacleCmd.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_robot::robot::obstaclecmd_has_distance():
    assert hasattr(robot::robot::ObstacleCmd, "distance")
    descriptor = None
    for klass in robot::robot::ObstacleCmd.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_robot::robot::stopprogramcmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::StopProgramCmd)


def test_robot::robot::stopprogramcmd_constructor_exists():
    assert callable(robot::robot::StopProgramCmd.__init__)


def test_robot::robot::stopprogramcmd_constructor_args():
    sig = inspect.signature(robot::robot::StopProgramCmd.__init__)
    params = list(sig.parameters.keys())



def test_robot::robot::printcmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::PrintCmd)


def test_robot::robot::printcmd_constructor_exists():
    assert callable(robot::robot::PrintCmd.__init__)


def test_robot::robot::printcmd_constructor_args():
    sig = inspect.signature(robot::robot::PrintCmd.__init__)
    params = list(sig.parameters.keys())
    assert "msg" in params, "Missing parameter 'msg'"
    assert "line" in params, "Missing parameter 'line'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "col" in params, "Missing parameter 'col'"

def test_robot::robot::printcmd_has_msg():
    assert hasattr(robot::robot::PrintCmd, "msg")
    descriptor = None
    for klass in robot::robot::PrintCmd.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::printcmd_has_line():
    assert hasattr(robot::robot::PrintCmd, "line")
    descriptor = None
    for klass in robot::robot::PrintCmd.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::printcmd_has_duration():
    assert hasattr(robot::robot::PrintCmd, "duration")
    descriptor = None
    for klass in robot::robot::PrintCmd.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::printcmd_has_col():
    assert hasattr(robot::robot::PrintCmd, "col")
    descriptor = None
    for klass in robot::robot::PrintCmd.__mro__:
        if "col" in klass.__dict__:
            descriptor = klass.__dict__["col"]
            break
    assert isinstance(descriptor, property)



def test_robot::robot::bip_is_not_abstract():
    assert not inspect.isabstract(robot::robot::Bip)


def test_robot::robot::bip_constructor_exists():
    assert callable(robot::robot::Bip.__init__)


def test_robot::robot::bip_constructor_args():
    sig = inspect.signature(robot::robot::Bip.__init__)
    params = list(sig.parameters.keys())
    assert "repet" in params, "Missing parameter 'repet'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "power" in params, "Missing parameter 'power'"

def test_robot::robot::bip_has_repet():
    assert hasattr(robot::robot::Bip, "repet")
    descriptor = None
    for klass in robot::robot::Bip.__mro__:
        if "repet" in klass.__dict__:
            descriptor = klass.__dict__["repet"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::bip_has_duration():
    assert hasattr(robot::robot::Bip, "duration")
    descriptor = None
    for klass in robot::robot::Bip.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::bip_has_power():
    assert hasattr(robot::robot::Bip, "power")
    descriptor = None
    for klass in robot::robot::Bip.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_robot::robot::setturnanglecmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::SetTurnAngleCmd)


def test_robot::robot::setturnanglecmd_constructor_exists():
    assert callable(robot::robot::SetTurnAngleCmd.__init__)


def test_robot::robot::setturnanglecmd_constructor_args():
    sig = inspect.signature(robot::robot::SetTurnAngleCmd.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_robot::robot::setturnanglecmd_has_angle():
    assert hasattr(robot::robot::SetTurnAngleCmd, "angle")
    descriptor = None
    for klass in robot::robot::SetTurnAngleCmd.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_robot::robot::stopenginecmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::StopEngineCmd)


def test_robot::robot::stopenginecmd_constructor_exists():
    assert callable(robot::robot::StopEngineCmd.__init__)


def test_robot::robot::stopenginecmd_constructor_args():
    sig = inspect.signature(robot::robot::StopEngineCmd.__init__)
    params = list(sig.parameters.keys())



def test_robot::robot::turncmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::TurnCmd)


def test_robot::robot::turncmd_constructor_exists():
    assert callable(robot::robot::TurnCmd.__init__)


def test_robot::robot::turncmd_constructor_args():
    sig = inspect.signature(robot::robot::TurnCmd.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_robot::robot::turncmd_has_power():
    assert hasattr(robot::robot::TurnCmd, "power")
    descriptor = None
    for klass in robot::robot::TurnCmd.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_robot::robot::turncmd_has_angle():
    assert hasattr(robot::robot::TurnCmd, "angle")
    descriptor = None
    for klass in robot::robot::TurnCmd.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_robot::robot::movecmd_is_not_abstract():
    assert not inspect.isabstract(robot::robot::MoveCmd)


def test_robot::robot::movecmd_constructor_exists():
    assert callable(robot::robot::MoveCmd.__init__)


def test_robot::robot::movecmd_constructor_args():
    sig = inspect.signature(robot::robot::MoveCmd.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_robot::robot::movecmd_has_power():
    assert hasattr(robot::robot::MoveCmd, "power")
    descriptor = None
    for klass in robot::robot::MoveCmd.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_boolexp_is_not_abstract():
    assert not inspect.isabstract(BoolExp)


def test_boolexp_constructor_exists():
    assert callable(BoolExp.__init__)


def test_boolexp_constructor_args():
    sig = inspect.signature(BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::negexp_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::NegExp)


def test_robot::flotctrl::negexp_constructor_exists():
    assert callable(robot::FlotCtrl::NegExp.__init__)


def test_robot::flotctrl::negexp_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::NegExp.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::andexp_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::AndExp)


def test_robot::flotctrl::andexp_constructor_exists():
    assert callable(robot::FlotCtrl::AndExp.__init__)


def test_robot::flotctrl::andexp_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::AndExp.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::expression_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::Expression)


def test_robot::flotctrl::expression_constructor_exists():
    assert callable(robot::FlotCtrl::Expression.__init__)


def test_robot::flotctrl::expression_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::boolexp_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::BoolExp)


def test_robot::flotctrl::boolexp_constructor_exists():
    assert callable(robot::FlotCtrl::BoolExp.__init__)


def test_robot::flotctrl::boolexp_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::whileloop_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::WhileLoop)


def test_robot::flotctrl::whileloop_constructor_exists():
    assert callable(robot::FlotCtrl::WhileLoop.__init__)


def test_robot::flotctrl::whileloop_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_robot::flotctrl::ifblock_is_not_abstract():
    assert not inspect.isabstract(robot::FlotCtrl::IfBlock)


def test_robot::flotctrl::ifblock_constructor_exists():
    assert callable(robot::FlotCtrl::IfBlock.__init__)


def test_robot::flotctrl::ifblock_constructor_args():
    sig = inspect.signature(robot::FlotCtrl::IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_robot::robot::command_is_not_abstract():
    assert not inspect.isabstract(robot::robot::Command)


def test_robot::robot::command_constructor_exists():
    assert callable(robot::robot::Command.__init__)


def test_robot::robot::command_constructor_args():
    sig = inspect.signature(robot::robot::Command.__init__)
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
robot::robot::ProgramUnit_strategy = st.builds(
    robot::robot::ProgramUnit,
)
robot::Command_strategy = st.builds(
    robot::Command,
)
FlotCtrl::BoolExp_strategy = st.builds(
    FlotCtrl::BoolExp,
)
robot::robot::HasTurnedCmd_strategy = st.builds(
    robot::robot::HasTurnedCmd,
    angle=
        safe_text
)
robot::robot::ObstacleCmd_strategy = st.builds(
    robot::robot::ObstacleCmd,
    distance=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
robot::robot::StopProgramCmd_strategy = st.builds(
    robot::robot::StopProgramCmd,
)
robot::robot::PrintCmd_strategy = st.builds(
    robot::robot::PrintCmd,
    msg=
        safe_text,
    line=
        safe_text,
    duration=
        safe_text,
    col=
        safe_text
)
robot::robot::Bip_strategy = st.builds(
    robot::robot::Bip,
    repet=
        safe_text,
    duration=
        safe_text,
    power=
        safe_text
)
robot::robot::SetTurnAngleCmd_strategy = st.builds(
    robot::robot::SetTurnAngleCmd,
    angle=
        safe_text
)
robot::robot::StopEngineCmd_strategy = st.builds(
    robot::robot::StopEngineCmd,
)
robot::robot::TurnCmd_strategy = st.builds(
    robot::robot::TurnCmd,
    power=
        safe_text,
    angle=
        safe_text
)
robot::robot::MoveCmd_strategy = st.builds(
    robot::robot::MoveCmd,
    power=
        safe_text
)
BoolExp_strategy = st.builds(
    BoolExp,
)
robot::FlotCtrl::NegExp_strategy = st.builds(
    robot::FlotCtrl::NegExp,
)
robot::FlotCtrl::AndExp_strategy = st.builds(
    robot::FlotCtrl::AndExp,
)
robot::FlotCtrl::Expression_strategy = st.builds(
    robot::FlotCtrl::Expression,
)
Expression_strategy = st.builds(
    Expression,
)
robot::FlotCtrl::BoolExp_strategy = st.builds(
    robot::FlotCtrl::BoolExp,
)
robot::FlotCtrl::WhileLoop_strategy = st.builds(
    robot::FlotCtrl::WhileLoop,
)
robot::FlotCtrl::IfBlock_strategy = st.builds(
    robot::FlotCtrl::IfBlock,
)
robot::robot::Command_strategy = st.builds(
    robot::robot::Command,
)

@given(instance=robot::robot::ProgramUnit_strategy)
@settings(max_examples=50)
def test_robot::robot::programunit_instantiation(instance):
    assert isinstance(instance, robot::robot::ProgramUnit)

@given(instance=robot::Command_strategy)
@settings(max_examples=50)
def test_robot::command_instantiation(instance):
    assert isinstance(instance, robot::Command)

@given(instance=FlotCtrl::BoolExp_strategy)
@settings(max_examples=50)
def test_flotctrl::boolexp_instantiation(instance):
    assert isinstance(instance, FlotCtrl::BoolExp)

@given(instance=robot::robot::HasTurnedCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::hasturnedcmd_instantiation(instance):
    assert isinstance(instance, robot::robot::HasTurnedCmd)

@given(instance=robot::robot::HasTurnedCmd_strategy)
def test_robot::robot::hasturnedcmd_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=robot::robot::HasTurnedCmd_strategy)
def test_robot::robot::hasturnedcmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=robot::robot::ObstacleCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::obstaclecmd_instantiation(instance):
    assert isinstance(instance, robot::robot::ObstacleCmd)

@given(instance=robot::robot::ObstacleCmd_strategy)
def test_robot::robot::obstaclecmd_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=robot::robot::ObstacleCmd_strategy)
def test_robot::robot::obstaclecmd_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=robot::robot::StopProgramCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::stopprogramcmd_instantiation(instance):
    assert isinstance(instance, robot::robot::StopProgramCmd)

@given(instance=robot::robot::PrintCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::printcmd_instantiation(instance):
    assert isinstance(instance, robot::robot::PrintCmd)

@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_msg_type(instance):
    assert isinstance(instance.msg, str)


@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original

@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_col_type(instance):
    assert isinstance(instance.col, str)


@given(instance=robot::robot::PrintCmd_strategy)
def test_robot::robot::printcmd_col_setter(instance):
    original = instance.col
    instance.col = original
    assert instance.col == original

@given(instance=robot::robot::Bip_strategy)
@settings(max_examples=50)
def test_robot::robot::bip_instantiation(instance):
    assert isinstance(instance, robot::robot::Bip)

@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_repet_type(instance):
    assert isinstance(instance.repet, str)


@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_repet_setter(instance):
    original = instance.repet
    instance.repet = original
    assert instance.repet == original

@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_power_type(instance):
    assert isinstance(instance.power, str)


@given(instance=robot::robot::Bip_strategy)
def test_robot::robot::bip_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=robot::robot::SetTurnAngleCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::setturnanglecmd_instantiation(instance):
    assert isinstance(instance, robot::robot::SetTurnAngleCmd)

@given(instance=robot::robot::SetTurnAngleCmd_strategy)
def test_robot::robot::setturnanglecmd_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=robot::robot::SetTurnAngleCmd_strategy)
def test_robot::robot::setturnanglecmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=robot::robot::StopEngineCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::stopenginecmd_instantiation(instance):
    assert isinstance(instance, robot::robot::StopEngineCmd)

@given(instance=robot::robot::TurnCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::turncmd_instantiation(instance):
    assert isinstance(instance, robot::robot::TurnCmd)

@given(instance=robot::robot::TurnCmd_strategy)
def test_robot::robot::turncmd_power_type(instance):
    assert isinstance(instance.power, str)


@given(instance=robot::robot::TurnCmd_strategy)
def test_robot::robot::turncmd_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=robot::robot::TurnCmd_strategy)
def test_robot::robot::turncmd_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=robot::robot::TurnCmd_strategy)
def test_robot::robot::turncmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=robot::robot::MoveCmd_strategy)
@settings(max_examples=50)
def test_robot::robot::movecmd_instantiation(instance):
    assert isinstance(instance, robot::robot::MoveCmd)

@given(instance=robot::robot::MoveCmd_strategy)
def test_robot::robot::movecmd_power_type(instance):
    assert isinstance(instance.power, str)


@given(instance=robot::robot::MoveCmd_strategy)
def test_robot::robot::movecmd_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=BoolExp_strategy)
@settings(max_examples=50)
def test_boolexp_instantiation(instance):
    assert isinstance(instance, BoolExp)

@given(instance=robot::FlotCtrl::NegExp_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::negexp_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::NegExp)

@given(instance=robot::FlotCtrl::AndExp_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::andexp_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::AndExp)

@given(instance=robot::FlotCtrl::Expression_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::expression_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=robot::FlotCtrl::BoolExp_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::boolexp_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::BoolExp)

@given(instance=robot::FlotCtrl::WhileLoop_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::whileloop_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::WhileLoop)

@given(instance=robot::FlotCtrl::IfBlock_strategy)
@settings(max_examples=50)
def test_robot::flotctrl::ifblock_instantiation(instance):
    assert isinstance(instance, robot::FlotCtrl::IfBlock)

@given(instance=robot::robot::Command_strategy)
@settings(max_examples=50)
def test_robot::robot::command_instantiation(instance):
    assert isinstance(instance, robot::robot::Command)
