import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    robot::ExpBool,
    ExpBool,
    robot::And,
    robot::If,
    robot::While,
    robot::HasTurned,
    robot::Not,
    robot::Obstacle,
    Instruction,
    robot::Move,
    robot::SetTurnAngle,
    robot::StopEngine,
    robot::StopProgram,
    robot::Turn,
    robot::Bip,
    robot::Instruction,
    robot::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robot::expbool_is_not_abstract():
    assert not inspect.isabstract(robot::ExpBool)


def test_robot::expbool_constructor_exists():
    assert callable(robot::ExpBool.__init__)


def test_robot::expbool_constructor_args():
    sig = inspect.signature(robot::ExpBool.__init__)
    params = list(sig.parameters.keys())



def test_expbool_is_not_abstract():
    assert not inspect.isabstract(ExpBool)


def test_expbool_constructor_exists():
    assert callable(ExpBool.__init__)


def test_expbool_constructor_args():
    sig = inspect.signature(ExpBool.__init__)
    params = list(sig.parameters.keys())



def test_robot::and_is_not_abstract():
    assert not inspect.isabstract(robot::And)


def test_robot::and_constructor_exists():
    assert callable(robot::And.__init__)


def test_robot::and_constructor_args():
    sig = inspect.signature(robot::And.__init__)
    params = list(sig.parameters.keys())



def test_robot::if_is_not_abstract():
    assert not inspect.isabstract(robot::If)


def test_robot::if_constructor_exists():
    assert callable(robot::If.__init__)


def test_robot::if_constructor_args():
    sig = inspect.signature(robot::If.__init__)
    params = list(sig.parameters.keys())



def test_robot::while_is_not_abstract():
    assert not inspect.isabstract(robot::While)


def test_robot::while_constructor_exists():
    assert callable(robot::While.__init__)


def test_robot::while_constructor_args():
    sig = inspect.signature(robot::While.__init__)
    params = list(sig.parameters.keys())



def test_robot::hasturned_is_not_abstract():
    assert not inspect.isabstract(robot::HasTurned)


def test_robot::hasturned_constructor_exists():
    assert callable(robot::HasTurned.__init__)


def test_robot::hasturned_constructor_args():
    sig = inspect.signature(robot::HasTurned.__init__)
    params = list(sig.parameters.keys())



def test_robot::not_is_not_abstract():
    assert not inspect.isabstract(robot::Not)


def test_robot::not_constructor_exists():
    assert callable(robot::Not.__init__)


def test_robot::not_constructor_args():
    sig = inspect.signature(robot::Not.__init__)
    params = list(sig.parameters.keys())



def test_robot::obstacle_is_not_abstract():
    assert not inspect.isabstract(robot::Obstacle)


def test_robot::obstacle_constructor_exists():
    assert callable(robot::Obstacle.__init__)


def test_robot::obstacle_constructor_args():
    sig = inspect.signature(robot::Obstacle.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robot::move_is_not_abstract():
    assert not inspect.isabstract(robot::Move)


def test_robot::move_constructor_exists():
    assert callable(robot::Move.__init__)


def test_robot::move_constructor_args():
    sig = inspect.signature(robot::Move.__init__)
    params = list(sig.parameters.keys())



def test_robot::setturnangle_is_not_abstract():
    assert not inspect.isabstract(robot::SetTurnAngle)


def test_robot::setturnangle_constructor_exists():
    assert callable(robot::SetTurnAngle.__init__)


def test_robot::setturnangle_constructor_args():
    sig = inspect.signature(robot::SetTurnAngle.__init__)
    params = list(sig.parameters.keys())



def test_robot::stopengine_is_not_abstract():
    assert not inspect.isabstract(robot::StopEngine)


def test_robot::stopengine_constructor_exists():
    assert callable(robot::StopEngine.__init__)


def test_robot::stopengine_constructor_args():
    sig = inspect.signature(robot::StopEngine.__init__)
    params = list(sig.parameters.keys())



def test_robot::stopprogram_is_not_abstract():
    assert not inspect.isabstract(robot::StopProgram)


def test_robot::stopprogram_constructor_exists():
    assert callable(robot::StopProgram.__init__)


def test_robot::stopprogram_constructor_args():
    sig = inspect.signature(robot::StopProgram.__init__)
    params = list(sig.parameters.keys())



def test_robot::turn_is_not_abstract():
    assert not inspect.isabstract(robot::Turn)


def test_robot::turn_constructor_exists():
    assert callable(robot::Turn.__init__)


def test_robot::turn_constructor_args():
    sig = inspect.signature(robot::Turn.__init__)
    params = list(sig.parameters.keys())



def test_robot::bip_is_not_abstract():
    assert not inspect.isabstract(robot::Bip)


def test_robot::bip_constructor_exists():
    assert callable(robot::Bip.__init__)


def test_robot::bip_constructor_args():
    sig = inspect.signature(robot::Bip.__init__)
    params = list(sig.parameters.keys())



def test_robot::instruction_is_not_abstract():
    assert not inspect.isabstract(robot::Instruction)


def test_robot::instruction_constructor_exists():
    assert callable(robot::Instruction.__init__)


def test_robot::instruction_constructor_args():
    sig = inspect.signature(robot::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robot::program_is_not_abstract():
    assert not inspect.isabstract(robot::Program)


def test_robot::program_constructor_exists():
    assert callable(robot::Program.__init__)


def test_robot::program_constructor_args():
    sig = inspect.signature(robot::Program.__init__)
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
robot::ExpBool_strategy = st.builds(
    robot::ExpBool,
)
ExpBool_strategy = st.builds(
    ExpBool,
)
robot::And_strategy = st.builds(
    robot::And,
)
robot::If_strategy = st.builds(
    robot::If,
)
robot::While_strategy = st.builds(
    robot::While,
)
robot::HasTurned_strategy = st.builds(
    robot::HasTurned,
)
robot::Not_strategy = st.builds(
    robot::Not,
)
robot::Obstacle_strategy = st.builds(
    robot::Obstacle,
)
Instruction_strategy = st.builds(
    Instruction,
)
robot::Move_strategy = st.builds(
    robot::Move,
)
robot::SetTurnAngle_strategy = st.builds(
    robot::SetTurnAngle,
)
robot::StopEngine_strategy = st.builds(
    robot::StopEngine,
)
robot::StopProgram_strategy = st.builds(
    robot::StopProgram,
)
robot::Turn_strategy = st.builds(
    robot::Turn,
)
robot::Bip_strategy = st.builds(
    robot::Bip,
)
robot::Instruction_strategy = st.builds(
    robot::Instruction,
)
robot::Program_strategy = st.builds(
    robot::Program,
)

@given(instance=robot::ExpBool_strategy)
@settings(max_examples=50)
def test_robot::expbool_instantiation(instance):
    assert isinstance(instance, robot::ExpBool)

@given(instance=ExpBool_strategy)
@settings(max_examples=50)
def test_expbool_instantiation(instance):
    assert isinstance(instance, ExpBool)

@given(instance=robot::And_strategy)
@settings(max_examples=50)
def test_robot::and_instantiation(instance):
    assert isinstance(instance, robot::And)

@given(instance=robot::If_strategy)
@settings(max_examples=50)
def test_robot::if_instantiation(instance):
    assert isinstance(instance, robot::If)

@given(instance=robot::While_strategy)
@settings(max_examples=50)
def test_robot::while_instantiation(instance):
    assert isinstance(instance, robot::While)

@given(instance=robot::HasTurned_strategy)
@settings(max_examples=50)
def test_robot::hasturned_instantiation(instance):
    assert isinstance(instance, robot::HasTurned)

@given(instance=robot::Not_strategy)
@settings(max_examples=50)
def test_robot::not_instantiation(instance):
    assert isinstance(instance, robot::Not)

@given(instance=robot::Obstacle_strategy)
@settings(max_examples=50)
def test_robot::obstacle_instantiation(instance):
    assert isinstance(instance, robot::Obstacle)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=robot::Move_strategy)
@settings(max_examples=50)
def test_robot::move_instantiation(instance):
    assert isinstance(instance, robot::Move)

@given(instance=robot::SetTurnAngle_strategy)
@settings(max_examples=50)
def test_robot::setturnangle_instantiation(instance):
    assert isinstance(instance, robot::SetTurnAngle)

@given(instance=robot::StopEngine_strategy)
@settings(max_examples=50)
def test_robot::stopengine_instantiation(instance):
    assert isinstance(instance, robot::StopEngine)

@given(instance=robot::StopProgram_strategy)
@settings(max_examples=50)
def test_robot::stopprogram_instantiation(instance):
    assert isinstance(instance, robot::StopProgram)

@given(instance=robot::Turn_strategy)
@settings(max_examples=50)
def test_robot::turn_instantiation(instance):
    assert isinstance(instance, robot::Turn)

@given(instance=robot::Bip_strategy)
@settings(max_examples=50)
def test_robot::bip_instantiation(instance):
    assert isinstance(instance, robot::Bip)

@given(instance=robot::Instruction_strategy)
@settings(max_examples=50)
def test_robot::instruction_instantiation(instance):
    assert isinstance(instance, robot::Instruction)

@given(instance=robot::Program_strategy)
@settings(max_examples=50)
def test_robot::program_instantiation(instance):
    assert isinstance(instance, robot::Program)
