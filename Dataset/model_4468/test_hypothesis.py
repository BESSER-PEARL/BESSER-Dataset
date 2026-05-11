import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    polybot::modelling::language::Instruction,
    Turn,
    polybot::modelling::language::TurnLeft,
    polybot::modelling::language::TurnRight,
    Instruction,
    polybot::modelling::language::Turn,
    polybot::modelling::language::Release,
    polybot::modelling::language::Catch,
    polybot::modelling::language::ComeHome,
    polybot::modelling::language::MoveStraight,
    polybot::modelling::language::Robot,
    polybot::modelling::language::Scene,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_polybot::modelling::language::instruction_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Instruction)


def test_polybot::modelling::language::instruction_constructor_exists():
    assert callable(polybot::modelling::language::Instruction.__init__)


def test_polybot::modelling::language::instruction_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Instruction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nextInstruction" in params, "Missing parameter 'nextInstruction'"
    assert "nextInstructionTrue" in params, "Missing parameter 'nextInstructionTrue'"
    assert "nextInstructionFalse" in params, "Missing parameter 'nextInstructionFalse'"

def test_polybot::modelling::language::instruction_has_name():
    assert hasattr(polybot::modelling::language::Instruction, "name")
    descriptor = None
    for klass in polybot::modelling::language::Instruction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_polybot::modelling::language::instruction_has_nextInstruction():
    assert hasattr(polybot::modelling::language::Instruction, "nextInstruction")
    descriptor = None
    for klass in polybot::modelling::language::Instruction.__mro__:
        if "nextInstruction" in klass.__dict__:
            descriptor = klass.__dict__["nextInstruction"]
            break
    assert isinstance(descriptor, property)

def test_polybot::modelling::language::instruction_has_nextInstructionTrue():
    assert hasattr(polybot::modelling::language::Instruction, "nextInstructionTrue")
    descriptor = None
    for klass in polybot::modelling::language::Instruction.__mro__:
        if "nextInstructionTrue" in klass.__dict__:
            descriptor = klass.__dict__["nextInstructionTrue"]
            break
    assert isinstance(descriptor, property)

def test_polybot::modelling::language::instruction_has_nextInstructionFalse():
    assert hasattr(polybot::modelling::language::Instruction, "nextInstructionFalse")
    descriptor = None
    for klass in polybot::modelling::language::Instruction.__mro__:
        if "nextInstructionFalse" in klass.__dict__:
            descriptor = klass.__dict__["nextInstructionFalse"]
            break
    assert isinstance(descriptor, property)



def test_turn_is_not_abstract():
    assert not inspect.isabstract(Turn)


def test_turn_constructor_exists():
    assert callable(Turn.__init__)


def test_turn_constructor_args():
    sig = inspect.signature(Turn.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::turnleft_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::TurnLeft)


def test_polybot::modelling::language::turnleft_constructor_exists():
    assert callable(polybot::modelling::language::TurnLeft.__init__)


def test_polybot::modelling::language::turnleft_constructor_args():
    sig = inspect.signature(polybot::modelling::language::TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::turnright_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::TurnRight)


def test_polybot::modelling::language::turnright_constructor_exists():
    assert callable(polybot::modelling::language::TurnRight.__init__)


def test_polybot::modelling::language::turnright_constructor_args():
    sig = inspect.signature(polybot::modelling::language::TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::turn_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Turn)


def test_polybot::modelling::language::turn_constructor_exists():
    assert callable(polybot::modelling::language::Turn.__init__)


def test_polybot::modelling::language::turn_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_polybot::modelling::language::turn_has_angle():
    assert hasattr(polybot::modelling::language::Turn, "angle")
    descriptor = None
    for klass in polybot::modelling::language::Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_polybot::modelling::language::release_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Release)


def test_polybot::modelling::language::release_constructor_exists():
    assert callable(polybot::modelling::language::Release.__init__)


def test_polybot::modelling::language::release_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Release.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::catch_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Catch)


def test_polybot::modelling::language::catch_constructor_exists():
    assert callable(polybot::modelling::language::Catch.__init__)


def test_polybot::modelling::language::catch_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Catch.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::comehome_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::ComeHome)


def test_polybot::modelling::language::comehome_constructor_exists():
    assert callable(polybot::modelling::language::ComeHome.__init__)


def test_polybot::modelling::language::comehome_constructor_args():
    sig = inspect.signature(polybot::modelling::language::ComeHome.__init__)
    params = list(sig.parameters.keys())



def test_polybot::modelling::language::movestraight_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::MoveStraight)


def test_polybot::modelling::language::movestraight_constructor_exists():
    assert callable(polybot::modelling::language::MoveStraight.__init__)


def test_polybot::modelling::language::movestraight_constructor_args():
    sig = inspect.signature(polybot::modelling::language::MoveStraight.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_polybot::modelling::language::movestraight_has_distance():
    assert hasattr(polybot::modelling::language::MoveStraight, "distance")
    descriptor = None
    for klass in polybot::modelling::language::MoveStraight.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_polybot::modelling::language::robot_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Robot)


def test_polybot::modelling::language::robot_constructor_exists():
    assert callable(polybot::modelling::language::Robot.__init__)


def test_polybot::modelling::language::robot_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"

def test_polybot::modelling::language::robot_has_debug():
    assert hasattr(polybot::modelling::language::Robot, "debug")
    descriptor = None
    for klass in polybot::modelling::language::Robot.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_polybot::modelling::language::scene_is_not_abstract():
    assert not inspect.isabstract(polybot::modelling::language::Scene)


def test_polybot::modelling::language::scene_constructor_exists():
    assert callable(polybot::modelling::language::Scene.__init__)


def test_polybot::modelling::language::scene_constructor_args():
    sig = inspect.signature(polybot::modelling::language::Scene.__init__)
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
polybot::modelling::language::Instruction_strategy = st.builds(
    polybot::modelling::language::Instruction,
    name=
        safe_text,
    nextInstruction=
        safe_text,
    nextInstructionTrue=
        safe_text,
    nextInstructionFalse=
        safe_text
)
Turn_strategy = st.builds(
    Turn,
)
polybot::modelling::language::TurnLeft_strategy = st.builds(
    polybot::modelling::language::TurnLeft,
)
polybot::modelling::language::TurnRight_strategy = st.builds(
    polybot::modelling::language::TurnRight,
)
Instruction_strategy = st.builds(
    Instruction,
)
polybot::modelling::language::Turn_strategy = st.builds(
    polybot::modelling::language::Turn,
    angle=
        st.integers()
)
polybot::modelling::language::Release_strategy = st.builds(
    polybot::modelling::language::Release,
)
polybot::modelling::language::Catch_strategy = st.builds(
    polybot::modelling::language::Catch,
)
polybot::modelling::language::ComeHome_strategy = st.builds(
    polybot::modelling::language::ComeHome,
)
polybot::modelling::language::MoveStraight_strategy = st.builds(
    polybot::modelling::language::MoveStraight,
    distance=
        st.integers()
)
polybot::modelling::language::Robot_strategy = st.builds(
    polybot::modelling::language::Robot,
    debug=
        st.booleans()
)
polybot::modelling::language::Scene_strategy = st.builds(
    polybot::modelling::language::Scene,
)

@given(instance=polybot::modelling::language::Instruction_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::instruction_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Instruction)

@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstruction_type(instance):
    assert isinstance(instance.nextInstruction, str)


@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstruction_setter(instance):
    original = instance.nextInstruction
    instance.nextInstruction = original
    assert instance.nextInstruction == original

@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstructionTrue_type(instance):
    assert isinstance(instance.nextInstructionTrue, str)


@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstructionTrue_setter(instance):
    original = instance.nextInstructionTrue
    instance.nextInstructionTrue = original
    assert instance.nextInstructionTrue == original

@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstructionFalse_type(instance):
    assert isinstance(instance.nextInstructionFalse, str)


@given(instance=polybot::modelling::language::Instruction_strategy)
def test_polybot::modelling::language::instruction_nextInstructionFalse_setter(instance):
    original = instance.nextInstructionFalse
    instance.nextInstructionFalse = original
    assert instance.nextInstructionFalse == original

@given(instance=Turn_strategy)
@settings(max_examples=50)
def test_turn_instantiation(instance):
    assert isinstance(instance, Turn)

@given(instance=polybot::modelling::language::TurnLeft_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::turnleft_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::TurnLeft)

@given(instance=polybot::modelling::language::TurnRight_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::turnright_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::TurnRight)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=polybot::modelling::language::Turn_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::turn_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Turn)

@given(instance=polybot::modelling::language::Turn_strategy)
def test_polybot::modelling::language::turn_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=polybot::modelling::language::Turn_strategy)
def test_polybot::modelling::language::turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=polybot::modelling::language::Release_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::release_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Release)

@given(instance=polybot::modelling::language::Catch_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::catch_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Catch)

@given(instance=polybot::modelling::language::ComeHome_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::comehome_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::ComeHome)

@given(instance=polybot::modelling::language::MoveStraight_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::movestraight_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::MoveStraight)

@given(instance=polybot::modelling::language::MoveStraight_strategy)
def test_polybot::modelling::language::movestraight_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=polybot::modelling::language::MoveStraight_strategy)
def test_polybot::modelling::language::movestraight_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=polybot::modelling::language::Robot_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::robot_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Robot)

@given(instance=polybot::modelling::language::Robot_strategy)
def test_polybot::modelling::language::robot_debug_type(instance):
    assert isinstance(instance.debug, bool)


@given(instance=polybot::modelling::language::Robot_strategy)
def test_polybot::modelling::language::robot_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=polybot::modelling::language::Scene_strategy)
@settings(max_examples=50)
def test_polybot::modelling::language::scene_instantiation(instance):
    assert isinstance(instance, polybot::modelling::language::Scene)
