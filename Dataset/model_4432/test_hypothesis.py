import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    mindstorms_Instruction,
    mindstorms_EdgeInstruction,
    Instruction,
    mindstorms_Choreography,
    mindstorms_Block,
    Block,
    mindstorms_Action,
    Action,
    mindstorms_Rotate,
    mindstorms_End,
    mindstorms_Grab,
    mindstorms_Begin,
    mindstorms_Release,
    mindstorms_GoBackward,
    mindstorms_GoForward,
    mindstorms_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Instruction)


def test_mindstorms_instruction_constructor_exists():
    assert callable(mindstorms_Instruction.__init__)


def test_mindstorms_instruction_constructor_args():
    sig = inspect.signature(mindstorms_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_edgeinstruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_EdgeInstruction)


def test_mindstorms_edgeinstruction_constructor_exists():
    assert callable(mindstorms_EdgeInstruction.__init__)


def test_mindstorms_edgeinstruction_constructor_args():
    sig = inspect.signature(mindstorms_EdgeInstruction.__init__)
    params = list(sig.parameters.keys())



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



def test_mindstorms_block_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Block)


def test_mindstorms_block_constructor_exists():
    assert callable(mindstorms_Block.__init__)


def test_mindstorms_block_constructor_args():
    sig = inspect.signature(mindstorms_Block.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_action_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Action)


def test_mindstorms_action_constructor_exists():
    assert callable(mindstorms_Action.__init__)


def test_mindstorms_action_constructor_args():
    sig = inspect.signature(mindstorms_Action.__init__)
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



def test_mindstorms_end_is_not_abstract():
    assert not inspect.isabstract(mindstorms_End)


def test_mindstorms_end_constructor_exists():
    assert callable(mindstorms_End.__init__)


def test_mindstorms_end_constructor_args():
    sig = inspect.signature(mindstorms_End.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Grab)


def test_mindstorms_grab_constructor_exists():
    assert callable(mindstorms_Grab.__init__)


def test_mindstorms_grab_constructor_args():
    sig = inspect.signature(mindstorms_Grab.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_begin_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Begin)


def test_mindstorms_begin_constructor_exists():
    assert callable(mindstorms_Begin.__init__)


def test_mindstorms_begin_constructor_args():
    sig = inspect.signature(mindstorms_Begin.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_release_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Release)


def test_mindstorms_release_constructor_exists():
    assert callable(mindstorms_Release.__init__)


def test_mindstorms_release_constructor_args():
    sig = inspect.signature(mindstorms_Release.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_gobackward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoBackward)


def test_mindstorms_gobackward_constructor_exists():
    assert callable(mindstorms_GoBackward.__init__)


def test_mindstorms_gobackward_constructor_args():
    sig = inspect.signature(mindstorms_GoBackward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"
    assert "infinite" in params, "Missing parameter 'infinite'"

def test_mindstorms_gobackward_has_cm():
    assert hasattr(mindstorms_GoBackward, "cm")
    descriptor = None
    for klass in mindstorms_GoBackward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_gobackward_has_infinite():
    assert hasattr(mindstorms_GoBackward, "infinite")
    descriptor = None
    for klass in mindstorms_GoBackward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoForward)


def test_mindstorms_goforward_constructor_exists():
    assert callable(mindstorms_GoForward.__init__)


def test_mindstorms_goforward_constructor_args():
    sig = inspect.signature(mindstorms_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms_goforward_has_infinite():
    assert hasattr(mindstorms_GoForward, "infinite")
    descriptor = None
    for klass in mindstorms_GoForward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_goforward_has_cm():
    assert hasattr(mindstorms_GoForward, "cm")
    descriptor = None
    for klass in mindstorms_GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_namedelement_is_not_abstract():
    assert not inspect.isabstract(mindstorms_NamedElement)


def test_mindstorms_namedelement_constructor_exists():
    assert callable(mindstorms_NamedElement.__init__)


def test_mindstorms_namedelement_constructor_args():
    sig = inspect.signature(mindstorms_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mindstorms_namedelement_has_name():
    assert hasattr(mindstorms_NamedElement, "name")
    descriptor = None
    for klass in mindstorms_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
NamedElement_strategy = st.builds(
    NamedElement,
)
mindstorms_Instruction_strategy = st.builds(
    mindstorms_Instruction,
)
mindstorms_EdgeInstruction_strategy = st.builds(
    mindstorms_EdgeInstruction,
)
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms_Choreography_strategy = st.builds(
    mindstorms_Choreography,
)
mindstorms_Block_strategy = st.builds(
    mindstorms_Block,
)
Block_strategy = st.builds(
    Block,
)
mindstorms_Action_strategy = st.builds(
    mindstorms_Action,
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
mindstorms_End_strategy = st.builds(
    mindstorms_End,
)
mindstorms_Grab_strategy = st.builds(
    mindstorms_Grab,
)
mindstorms_Begin_strategy = st.builds(
    mindstorms_Begin,
)
mindstorms_Release_strategy = st.builds(
    mindstorms_Release,
)
mindstorms_GoBackward_strategy = st.builds(
    mindstorms_GoBackward,
    cm=
        st.integers(),
    infinite=
        st.booleans()
)
mindstorms_GoForward_strategy = st.builds(
    mindstorms_GoForward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
mindstorms_NamedElement_strategy = st.builds(
    mindstorms_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mindstorms_Instruction_strategy)
@settings(max_examples=50)
def test_mindstorms_instruction_instantiation(instance):
    assert isinstance(instance, mindstorms_Instruction)

@given(instance=mindstorms_EdgeInstruction_strategy)
@settings(max_examples=50)
def test_mindstorms_edgeinstruction_instantiation(instance):
    assert isinstance(instance, mindstorms_EdgeInstruction)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mindstorms_Choreography_strategy)
@settings(max_examples=50)
def test_mindstorms_choreography_instantiation(instance):
    assert isinstance(instance, mindstorms_Choreography)

@given(instance=mindstorms_Block_strategy)
@settings(max_examples=50)
def test_mindstorms_block_instantiation(instance):
    assert isinstance(instance, mindstorms_Block)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=mindstorms_Action_strategy)
@settings(max_examples=50)
def test_mindstorms_action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)

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

@given(instance=mindstorms_End_strategy)
@settings(max_examples=50)
def test_mindstorms_end_instantiation(instance):
    assert isinstance(instance, mindstorms_End)

@given(instance=mindstorms_Grab_strategy)
@settings(max_examples=50)
def test_mindstorms_grab_instantiation(instance):
    assert isinstance(instance, mindstorms_Grab)

@given(instance=mindstorms_Begin_strategy)
@settings(max_examples=50)
def test_mindstorms_begin_instantiation(instance):
    assert isinstance(instance, mindstorms_Begin)

@given(instance=mindstorms_Release_strategy)
@settings(max_examples=50)
def test_mindstorms_release_instantiation(instance):
    assert isinstance(instance, mindstorms_Release)

@given(instance=mindstorms_GoBackward_strategy)
@settings(max_examples=50)
def test_mindstorms_gobackward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoBackward)



@given(instance=mindstorms_GoBackward_strategy)
def test_mindstorms_gobackward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original



@given(instance=mindstorms_GoBackward_strategy)
def test_mindstorms_gobackward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=mindstorms_GoForward_strategy)
@settings(max_examples=50)
def test_mindstorms_goforward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoForward)



@given(instance=mindstorms_GoForward_strategy)
def test_mindstorms_goforward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original



@given(instance=mindstorms_GoForward_strategy)
def test_mindstorms_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms_NamedElement_strategy)
@settings(max_examples=50)
def test_mindstorms_namedelement_instantiation(instance):
    assert isinstance(instance, mindstorms_NamedElement)



@given(instance=mindstorms_NamedElement_strategy)
def test_mindstorms_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
