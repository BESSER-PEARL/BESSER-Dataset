import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Instruction,
    mindstorms_Choreography,
    mindstorms_Instruction,
    Action,
    mindstorms_Rotate,
    mindstorms_GoForward,
    mindstorms_Release,
    mindstorms_Grab,
    mindstorms_Action,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_choreography_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Choreography)


def test_mindstorms_choreography_constructor_exists():
    assert callable(mindstorms_Choreography.__init__)


def test_mindstorms_choreography_constructor_args():
    sig = inspect.signature(mindstorms_Choreography.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mindstorms_choreography_has_name():
    assert hasattr(mindstorms_Choreography, "name")
    descriptor = None
    for klass in mindstorms_Choreography.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Instruction)


def test_mindstorms_instruction_constructor_exists():
    assert callable(mindstorms_Instruction.__init__)


def test_mindstorms_instruction_constructor_args():
    sig = inspect.signature(mindstorms_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_rotate_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Rotate)


def test_mindstorms_rotate_constructor_exists():
    assert callable(mindstorms_Rotate.__init__)


def test_mindstorms_rotate_constructor_args():
    sig = inspect.signature(mindstorms_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "random" in params, "Missing parameter 'random'"

def test_mindstorms_rotate_has_degrees():
    assert hasattr(mindstorms_Rotate, "degrees")
    descriptor = None
    for klass in mindstorms_Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_rotate_has_random():
    assert hasattr(mindstorms_Rotate, "random")
    descriptor = None
    for klass in mindstorms_Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoForward)


def test_mindstorms_goforward_constructor_exists():
    assert callable(mindstorms_GoForward.__init__)


def test_mindstorms_goforward_constructor_args():
    sig = inspect.signature(mindstorms_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms_goforward_has_cm():
    assert hasattr(mindstorms_GoForward, "cm")
    descriptor = None
    for klass in mindstorms_GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_release_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Release)


def test_mindstorms_release_constructor_exists():
    assert callable(mindstorms_Release.__init__)


def test_mindstorms_release_constructor_args():
    sig = inspect.signature(mindstorms_Release.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Grab)


def test_mindstorms_grab_constructor_exists():
    assert callable(mindstorms_Grab.__init__)


def test_mindstorms_grab_constructor_args():
    sig = inspect.signature(mindstorms_Grab.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_action_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Action)


def test_mindstorms_action_constructor_exists():
    assert callable(mindstorms_Action.__init__)


def test_mindstorms_action_constructor_args():
    sig = inspect.signature(mindstorms_Action.__init__)
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
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms_Choreography_strategy = st.builds(
    mindstorms_Choreography,
    name=
        safe_text
)
mindstorms_Instruction_strategy = st.builds(
    mindstorms_Instruction,
)
Action_strategy = st.builds(
    Action,
)
mindstorms_Rotate_strategy = st.builds(
    mindstorms_Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
mindstorms_GoForward_strategy = st.builds(
    mindstorms_GoForward,
    cm=
        st.integers()
)
mindstorms_Release_strategy = st.builds(
    mindstorms_Release,
)
mindstorms_Grab_strategy = st.builds(
    mindstorms_Grab,
)
mindstorms_Action_strategy = st.builds(
    mindstorms_Action,
)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mindstorms_Choreography_strategy)
@settings(max_examples=50)
def test_mindstorms_choreography_instantiation(instance):
    assert isinstance(instance, mindstorms_Choreography)



@given(instance=mindstorms_Choreography_strategy)
def test_mindstorms_choreography_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mindstorms_Instruction_strategy)
@settings(max_examples=50)
def test_mindstorms_instruction_instantiation(instance):
    assert isinstance(instance, mindstorms_Instruction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=mindstorms_Rotate_strategy)
@settings(max_examples=50)
def test_mindstorms_rotate_instantiation(instance):
    assert isinstance(instance, mindstorms_Rotate)



@given(instance=mindstorms_Rotate_strategy)
def test_mindstorms_rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original



@given(instance=mindstorms_Rotate_strategy)
def test_mindstorms_rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=mindstorms_GoForward_strategy)
@settings(max_examples=50)
def test_mindstorms_goforward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoForward)



@given(instance=mindstorms_GoForward_strategy)
def test_mindstorms_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms_Release_strategy)
@settings(max_examples=50)
def test_mindstorms_release_instantiation(instance):
    assert isinstance(instance, mindstorms_Release)

@given(instance=mindstorms_Grab_strategy)
@settings(max_examples=50)
def test_mindstorms_grab_instantiation(instance):
    assert isinstance(instance, mindstorms_Grab)

@given(instance=mindstorms_Action_strategy)
@settings(max_examples=50)
def test_mindstorms_action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)
