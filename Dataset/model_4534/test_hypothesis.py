import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    robot_ExpBool,
    ExpBool,
    robot_Not,
    robot_HasTurned,
    robot_While,
    robot_If,
    robot_And,
    robot_Obstacle,
    Instruction,
    robot_Turn,
    robot_SetTurnAngle,
    robot_StopEngine,
    robot_Move,
    robot_StopProgram,
    robot_Bip,
    robot_Instruction,
    robot_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robot_expbool_is_not_abstract():
    assert not inspect.isabstract(robot_ExpBool)


def test_robot_expbool_constructor_exists():
    assert callable(robot_ExpBool.__init__)


def test_robot_expbool_constructor_args():
    sig = inspect.signature(robot_ExpBool.__init__)
    params = list(sig.parameters.keys())



def test_expbool_is_not_abstract():
    assert not inspect.isabstract(ExpBool)


def test_expbool_constructor_exists():
    assert callable(ExpBool.__init__)


def test_expbool_constructor_args():
    sig = inspect.signature(ExpBool.__init__)
    params = list(sig.parameters.keys())



def test_robot_not_is_not_abstract():
    assert not inspect.isabstract(robot_Not)


def test_robot_not_constructor_exists():
    assert callable(robot_Not.__init__)


def test_robot_not_constructor_args():
    sig = inspect.signature(robot_Not.__init__)
    params = list(sig.parameters.keys())



def test_robot_hasturned_is_not_abstract():
    assert not inspect.isabstract(robot_HasTurned)


def test_robot_hasturned_constructor_exists():
    assert callable(robot_HasTurned.__init__)


def test_robot_hasturned_constructor_args():
    sig = inspect.signature(robot_HasTurned.__init__)
    params = list(sig.parameters.keys())



def test_robot_while_is_not_abstract():
    assert not inspect.isabstract(robot_While)


def test_robot_while_constructor_exists():
    assert callable(robot_While.__init__)


def test_robot_while_constructor_args():
    sig = inspect.signature(robot_While.__init__)
    params = list(sig.parameters.keys())



def test_robot_if_is_not_abstract():
    assert not inspect.isabstract(robot_If)


def test_robot_if_constructor_exists():
    assert callable(robot_If.__init__)


def test_robot_if_constructor_args():
    sig = inspect.signature(robot_If.__init__)
    params = list(sig.parameters.keys())



def test_robot_and_is_not_abstract():
    assert not inspect.isabstract(robot_And)


def test_robot_and_constructor_exists():
    assert callable(robot_And.__init__)


def test_robot_and_constructor_args():
    sig = inspect.signature(robot_And.__init__)
    params = list(sig.parameters.keys())



def test_robot_obstacle_is_not_abstract():
    assert not inspect.isabstract(robot_Obstacle)


def test_robot_obstacle_constructor_exists():
    assert callable(robot_Obstacle.__init__)


def test_robot_obstacle_constructor_args():
    sig = inspect.signature(robot_Obstacle.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robot_turn_is_not_abstract():
    assert not inspect.isabstract(robot_Turn)


def test_robot_turn_constructor_exists():
    assert callable(robot_Turn.__init__)


def test_robot_turn_constructor_args():
    sig = inspect.signature(robot_Turn.__init__)
    params = list(sig.parameters.keys())



def test_robot_setturnangle_is_not_abstract():
    assert not inspect.isabstract(robot_SetTurnAngle)


def test_robot_setturnangle_constructor_exists():
    assert callable(robot_SetTurnAngle.__init__)


def test_robot_setturnangle_constructor_args():
    sig = inspect.signature(robot_SetTurnAngle.__init__)
    params = list(sig.parameters.keys())



def test_robot_stopengine_is_not_abstract():
    assert not inspect.isabstract(robot_StopEngine)


def test_robot_stopengine_constructor_exists():
    assert callable(robot_StopEngine.__init__)


def test_robot_stopengine_constructor_args():
    sig = inspect.signature(robot_StopEngine.__init__)
    params = list(sig.parameters.keys())



def test_robot_move_is_not_abstract():
    assert not inspect.isabstract(robot_Move)


def test_robot_move_constructor_exists():
    assert callable(robot_Move.__init__)


def test_robot_move_constructor_args():
    sig = inspect.signature(robot_Move.__init__)
    params = list(sig.parameters.keys())



def test_robot_stopprogram_is_not_abstract():
    assert not inspect.isabstract(robot_StopProgram)


def test_robot_stopprogram_constructor_exists():
    assert callable(robot_StopProgram.__init__)


def test_robot_stopprogram_constructor_args():
    sig = inspect.signature(robot_StopProgram.__init__)
    params = list(sig.parameters.keys())



def test_robot_bip_is_not_abstract():
    assert not inspect.isabstract(robot_Bip)


def test_robot_bip_constructor_exists():
    assert callable(robot_Bip.__init__)


def test_robot_bip_constructor_args():
    sig = inspect.signature(robot_Bip.__init__)
    params = list(sig.parameters.keys())



def test_robot_instruction_is_not_abstract():
    assert not inspect.isabstract(robot_Instruction)


def test_robot_instruction_constructor_exists():
    assert callable(robot_Instruction.__init__)


def test_robot_instruction_constructor_args():
    sig = inspect.signature(robot_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robot_program_is_not_abstract():
    assert not inspect.isabstract(robot_Program)


def test_robot_program_constructor_exists():
    assert callable(robot_Program.__init__)


def test_robot_program_constructor_args():
    sig = inspect.signature(robot_Program.__init__)
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
robot_ExpBool_strategy = st.builds(
    robot_ExpBool,
)
ExpBool_strategy = st.builds(
    ExpBool,
)
robot_Not_strategy = st.builds(
    robot_Not,
)
robot_HasTurned_strategy = st.builds(
    robot_HasTurned,
)
robot_While_strategy = st.builds(
    robot_While,
)
robot_If_strategy = st.builds(
    robot_If,
)
robot_And_strategy = st.builds(
    robot_And,
)
robot_Obstacle_strategy = st.builds(
    robot_Obstacle,
)
Instruction_strategy = st.builds(
    Instruction,
)
robot_Turn_strategy = st.builds(
    robot_Turn,
)
robot_SetTurnAngle_strategy = st.builds(
    robot_SetTurnAngle,
)
robot_StopEngine_strategy = st.builds(
    robot_StopEngine,
)
robot_Move_strategy = st.builds(
    robot_Move,
)
robot_StopProgram_strategy = st.builds(
    robot_StopProgram,
)
robot_Bip_strategy = st.builds(
    robot_Bip,
)
robot_Instruction_strategy = st.builds(
    robot_Instruction,
)
robot_Program_strategy = st.builds(
    robot_Program,
)

@given(instance=robot_ExpBool_strategy)
@settings(max_examples=50)
def test_robot_expbool_instantiation(instance):
    assert isinstance(instance, robot_ExpBool)

@given(instance=ExpBool_strategy)
@settings(max_examples=50)
def test_expbool_instantiation(instance):
    assert isinstance(instance, ExpBool)

@given(instance=robot_Not_strategy)
@settings(max_examples=50)
def test_robot_not_instantiation(instance):
    assert isinstance(instance, robot_Not)

@given(instance=robot_HasTurned_strategy)
@settings(max_examples=50)
def test_robot_hasturned_instantiation(instance):
    assert isinstance(instance, robot_HasTurned)

@given(instance=robot_While_strategy)
@settings(max_examples=50)
def test_robot_while_instantiation(instance):
    assert isinstance(instance, robot_While)

@given(instance=robot_If_strategy)
@settings(max_examples=50)
def test_robot_if_instantiation(instance):
    assert isinstance(instance, robot_If)

@given(instance=robot_And_strategy)
@settings(max_examples=50)
def test_robot_and_instantiation(instance):
    assert isinstance(instance, robot_And)

@given(instance=robot_Obstacle_strategy)
@settings(max_examples=50)
def test_robot_obstacle_instantiation(instance):
    assert isinstance(instance, robot_Obstacle)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=robot_Turn_strategy)
@settings(max_examples=50)
def test_robot_turn_instantiation(instance):
    assert isinstance(instance, robot_Turn)

@given(instance=robot_SetTurnAngle_strategy)
@settings(max_examples=50)
def test_robot_setturnangle_instantiation(instance):
    assert isinstance(instance, robot_SetTurnAngle)

@given(instance=robot_StopEngine_strategy)
@settings(max_examples=50)
def test_robot_stopengine_instantiation(instance):
    assert isinstance(instance, robot_StopEngine)

@given(instance=robot_Move_strategy)
@settings(max_examples=50)
def test_robot_move_instantiation(instance):
    assert isinstance(instance, robot_Move)

@given(instance=robot_StopProgram_strategy)
@settings(max_examples=50)
def test_robot_stopprogram_instantiation(instance):
    assert isinstance(instance, robot_StopProgram)

@given(instance=robot_Bip_strategy)
@settings(max_examples=50)
def test_robot_bip_instantiation(instance):
    assert isinstance(instance, robot_Bip)

@given(instance=robot_Instruction_strategy)
@settings(max_examples=50)
def test_robot_instruction_instantiation(instance):
    assert isinstance(instance, robot_Instruction)

@given(instance=robot_Program_strategy)
@settings(max_examples=50)
def test_robot_program_instantiation(instance):
    assert isinstance(instance, robot_Program)
