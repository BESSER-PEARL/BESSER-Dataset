import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Action,
    RobotWork_Release,
    RobotWork_GoForward,
    RobotWork_Rotate,
    RobotWork_Grab,
    Instruction,
    RobotWork_Chrography,
    RobotWork_Action,
    RobotWork_Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_robotwork_release_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Release)


def test_robotwork_release_constructor_exists():
    assert callable(RobotWork_Release.__init__)


def test_robotwork_release_constructor_args():
    sig = inspect.signature(RobotWork_Release.__init__)
    params = list(sig.parameters.keys())



def test_robotwork_goforward_is_not_abstract():
    assert not inspect.isabstract(RobotWork_GoForward)


def test_robotwork_goforward_constructor_exists():
    assert callable(RobotWork_GoForward.__init__)


def test_robotwork_goforward_constructor_args():
    sig = inspect.signature(RobotWork_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"

def test_robotwork_goforward_has_cm():
    assert hasattr(RobotWork_GoForward, "cm")
    descriptor = None
    for klass in RobotWork_GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_robotwork_rotate_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Rotate)


def test_robotwork_rotate_constructor_exists():
    assert callable(RobotWork_Rotate.__init__)


def test_robotwork_rotate_constructor_args():
    sig = inspect.signature(RobotWork_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "random" in params, "Missing parameter 'random'"

def test_robotwork_rotate_has_degrees():
    assert hasattr(RobotWork_Rotate, "degrees")
    descriptor = None
    for klass in RobotWork_Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_robotwork_rotate_has_random():
    assert hasattr(RobotWork_Rotate, "random")
    descriptor = None
    for klass in RobotWork_Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)



def test_robotwork_grab_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Grab)


def test_robotwork_grab_constructor_exists():
    assert callable(RobotWork_Grab.__init__)


def test_robotwork_grab_constructor_args():
    sig = inspect.signature(RobotWork_Grab.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robotwork_chrography_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Chrography)


def test_robotwork_chrography_constructor_exists():
    assert callable(RobotWork_Chrography.__init__)


def test_robotwork_chrography_constructor_args():
    sig = inspect.signature(RobotWork_Chrography.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotwork_chrography_has_name():
    assert hasattr(RobotWork_Chrography, "name")
    descriptor = None
    for klass in RobotWork_Chrography.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotwork_action_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Action)


def test_robotwork_action_constructor_exists():
    assert callable(RobotWork_Action.__init__)


def test_robotwork_action_constructor_args():
    sig = inspect.signature(RobotWork_Action.__init__)
    params = list(sig.parameters.keys())



def test_robotwork_instruction_is_not_abstract():
    assert not inspect.isabstract(RobotWork_Instruction)


def test_robotwork_instruction_constructor_exists():
    assert callable(RobotWork_Instruction.__init__)


def test_robotwork_instruction_constructor_args():
    sig = inspect.signature(RobotWork_Instruction.__init__)
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
Action_strategy = st.builds(
    Action,
)
RobotWork_Release_strategy = st.builds(
    RobotWork_Release,
)
RobotWork_GoForward_strategy = st.builds(
    RobotWork_GoForward,
    cm=
        st.integers()
)
RobotWork_Rotate_strategy = st.builds(
    RobotWork_Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
RobotWork_Grab_strategy = st.builds(
    RobotWork_Grab,
)
Instruction_strategy = st.builds(
    Instruction,
)
RobotWork_Chrography_strategy = st.builds(
    RobotWork_Chrography,
    name=
        safe_text
)
RobotWork_Action_strategy = st.builds(
    RobotWork_Action,
)
RobotWork_Instruction_strategy = st.builds(
    RobotWork_Instruction,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=RobotWork_Release_strategy)
@settings(max_examples=50)
def test_robotwork_release_instantiation(instance):
    assert isinstance(instance, RobotWork_Release)

@given(instance=RobotWork_GoForward_strategy)
@settings(max_examples=50)
def test_robotwork_goforward_instantiation(instance):
    assert isinstance(instance, RobotWork_GoForward)



@given(instance=RobotWork_GoForward_strategy)
def test_robotwork_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=RobotWork_Rotate_strategy)
@settings(max_examples=50)
def test_robotwork_rotate_instantiation(instance):
    assert isinstance(instance, RobotWork_Rotate)



@given(instance=RobotWork_Rotate_strategy)
def test_robotwork_rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original



@given(instance=RobotWork_Rotate_strategy)
def test_robotwork_rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=RobotWork_Grab_strategy)
@settings(max_examples=50)
def test_robotwork_grab_instantiation(instance):
    assert isinstance(instance, RobotWork_Grab)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=RobotWork_Chrography_strategy)
@settings(max_examples=50)
def test_robotwork_chrography_instantiation(instance):
    assert isinstance(instance, RobotWork_Chrography)



@given(instance=RobotWork_Chrography_strategy)
def test_robotwork_chrography_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RobotWork_Action_strategy)
@settings(max_examples=50)
def test_robotwork_action_instantiation(instance):
    assert isinstance(instance, RobotWork_Action)

@given(instance=RobotWork_Instruction_strategy)
@settings(max_examples=50)
def test_robotwork_instruction_instantiation(instance):
    assert isinstance(instance, RobotWork_Instruction)
