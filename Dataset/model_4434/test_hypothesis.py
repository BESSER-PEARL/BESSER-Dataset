import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    RobotWork::Release,
    RobotWork::GoForward,
    RobotWork::Rotate,
    RobotWork::Grab,
    Instruction,
    RobotWork::Chrography,
    RobotWork::Action,
    RobotWork::Instruction,
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



def test_robotwork::release_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Release)


def test_robotwork::release_constructor_exists():
    assert callable(RobotWork::Release.__init__)


def test_robotwork::release_constructor_args():
    sig = inspect.signature(RobotWork::Release.__init__)
    params = list(sig.parameters.keys())



def test_robotwork::goforward_is_not_abstract():
    assert not inspect.isabstract(RobotWork::GoForward)


def test_robotwork::goforward_constructor_exists():
    assert callable(RobotWork::GoForward.__init__)


def test_robotwork::goforward_constructor_args():
    sig = inspect.signature(RobotWork::GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"

def test_robotwork::goforward_has_cm():
    assert hasattr(RobotWork::GoForward, "cm")
    descriptor = None
    for klass in RobotWork::GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_robotwork::rotate_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Rotate)


def test_robotwork::rotate_constructor_exists():
    assert callable(RobotWork::Rotate.__init__)


def test_robotwork::rotate_constructor_args():
    sig = inspect.signature(RobotWork::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "random" in params, "Missing parameter 'random'"

def test_robotwork::rotate_has_degrees():
    assert hasattr(RobotWork::Rotate, "degrees")
    descriptor = None
    for klass in RobotWork::Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_robotwork::rotate_has_random():
    assert hasattr(RobotWork::Rotate, "random")
    descriptor = None
    for klass in RobotWork::Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)



def test_robotwork::grab_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Grab)


def test_robotwork::grab_constructor_exists():
    assert callable(RobotWork::Grab.__init__)


def test_robotwork::grab_constructor_args():
    sig = inspect.signature(RobotWork::Grab.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_robotwork::chrography_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Chrography)


def test_robotwork::chrography_constructor_exists():
    assert callable(RobotWork::Chrography.__init__)


def test_robotwork::chrography_constructor_args():
    sig = inspect.signature(RobotWork::Chrography.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotwork::chrography_has_name():
    assert hasattr(RobotWork::Chrography, "name")
    descriptor = None
    for klass in RobotWork::Chrography.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotwork::action_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Action)


def test_robotwork::action_constructor_exists():
    assert callable(RobotWork::Action.__init__)


def test_robotwork::action_constructor_args():
    sig = inspect.signature(RobotWork::Action.__init__)
    params = list(sig.parameters.keys())



def test_robotwork::instruction_is_not_abstract():
    assert not inspect.isabstract(RobotWork::Instruction)


def test_robotwork::instruction_constructor_exists():
    assert callable(RobotWork::Instruction.__init__)


def test_robotwork::instruction_constructor_args():
    sig = inspect.signature(RobotWork::Instruction.__init__)
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
RobotWork::Release_strategy = st.builds(
    RobotWork::Release,
)
RobotWork::GoForward_strategy = st.builds(
    RobotWork::GoForward,
    cm=
        st.integers()
)
RobotWork::Rotate_strategy = st.builds(
    RobotWork::Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
RobotWork::Grab_strategy = st.builds(
    RobotWork::Grab,
)
Instruction_strategy = st.builds(
    Instruction,
)
RobotWork::Chrography_strategy = st.builds(
    RobotWork::Chrography,
    name=
        safe_text
)
RobotWork::Action_strategy = st.builds(
    RobotWork::Action,
)
RobotWork::Instruction_strategy = st.builds(
    RobotWork::Instruction,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=RobotWork::Release_strategy)
@settings(max_examples=50)
def test_robotwork::release_instantiation(instance):
    assert isinstance(instance, RobotWork::Release)

@given(instance=RobotWork::GoForward_strategy)
@settings(max_examples=50)
def test_robotwork::goforward_instantiation(instance):
    assert isinstance(instance, RobotWork::GoForward)

@given(instance=RobotWork::GoForward_strategy)
def test_robotwork::goforward_cm_type(instance):
    assert isinstance(instance.cm, int)


@given(instance=RobotWork::GoForward_strategy)
def test_robotwork::goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=RobotWork::Rotate_strategy)
@settings(max_examples=50)
def test_robotwork::rotate_instantiation(instance):
    assert isinstance(instance, RobotWork::Rotate)

@given(instance=RobotWork::Rotate_strategy)
def test_robotwork::rotate_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=RobotWork::Rotate_strategy)
def test_robotwork::rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=RobotWork::Rotate_strategy)
def test_robotwork::rotate_random_type(instance):
    assert isinstance(instance.random, bool)


@given(instance=RobotWork::Rotate_strategy)
def test_robotwork::rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=RobotWork::Grab_strategy)
@settings(max_examples=50)
def test_robotwork::grab_instantiation(instance):
    assert isinstance(instance, RobotWork::Grab)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=RobotWork::Chrography_strategy)
@settings(max_examples=50)
def test_robotwork::chrography_instantiation(instance):
    assert isinstance(instance, RobotWork::Chrography)

@given(instance=RobotWork::Chrography_strategy)
def test_robotwork::chrography_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RobotWork::Chrography_strategy)
def test_robotwork::chrography_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RobotWork::Action_strategy)
@settings(max_examples=50)
def test_robotwork::action_instantiation(instance):
    assert isinstance(instance, RobotWork::Action)

@given(instance=RobotWork::Instruction_strategy)
@settings(max_examples=50)
def test_robotwork::instruction_instantiation(instance):
    assert isinstance(instance, RobotWork::Instruction)
