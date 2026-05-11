import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mindstorms::EdgeInstruction,
    Instruction,
    mindstorms::Choreography,
    mindstorms::Block,
    Block,
    mindstorms::Action,
    Action,
    mindstorms::Grab,
    mindstorms::End,
    mindstorms::GoBackward,
    mindstorms::GoForward,
    mindstorms::NamedElement,
    NamedElement,
    mindstorms::Instruction,
    mindstorms::Release,
    mindstorms::Rotate,
    mindstorms::Begin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mindstorms::edgeinstruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms::EdgeInstruction)


def test_mindstorms::edgeinstruction_constructor_exists():
    assert callable(mindstorms::EdgeInstruction.__init__)


def test_mindstorms::edgeinstruction_constructor_args():
    sig = inspect.signature(mindstorms::EdgeInstruction.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::choreography_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Choreography)


def test_mindstorms::choreography_constructor_exists():
    assert callable(mindstorms::Choreography.__init__)


def test_mindstorms::choreography_constructor_args():
    sig = inspect.signature(mindstorms::Choreography.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::block_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Block)


def test_mindstorms::block_constructor_exists():
    assert callable(mindstorms::Block.__init__)


def test_mindstorms::block_constructor_args():
    sig = inspect.signature(mindstorms::Block.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::action_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Action)


def test_mindstorms::action_constructor_exists():
    assert callable(mindstorms::Action.__init__)


def test_mindstorms::action_constructor_args():
    sig = inspect.signature(mindstorms::Action.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Grab)


def test_mindstorms::grab_constructor_exists():
    assert callable(mindstorms::Grab.__init__)


def test_mindstorms::grab_constructor_args():
    sig = inspect.signature(mindstorms::Grab.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::end_is_not_abstract():
    assert not inspect.isabstract(mindstorms::End)


def test_mindstorms::end_constructor_exists():
    assert callable(mindstorms::End.__init__)


def test_mindstorms::end_constructor_args():
    sig = inspect.signature(mindstorms::End.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::gobackward_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoBackward)


def test_mindstorms::gobackward_constructor_exists():
    assert callable(mindstorms::GoBackward.__init__)


def test_mindstorms::gobackward_constructor_args():
    sig = inspect.signature(mindstorms::GoBackward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms::gobackward_has_infinite():
    assert hasattr(mindstorms::GoBackward, "infinite")
    descriptor = None
    for klass in mindstorms::GoBackward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::gobackward_has_cm():
    assert hasattr(mindstorms::GoBackward, "cm")
    descriptor = None
    for klass in mindstorms::GoBackward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoForward)


def test_mindstorms::goforward_constructor_exists():
    assert callable(mindstorms::GoForward.__init__)


def test_mindstorms::goforward_constructor_args():
    sig = inspect.signature(mindstorms::GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"
    assert "infinite" in params, "Missing parameter 'infinite'"

def test_mindstorms::goforward_has_cm():
    assert hasattr(mindstorms::GoForward, "cm")
    descriptor = None
    for klass in mindstorms::GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::goforward_has_infinite():
    assert hasattr(mindstorms::GoForward, "infinite")
    descriptor = None
    for klass in mindstorms::GoForward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::namedelement_is_not_abstract():
    assert not inspect.isabstract(mindstorms::NamedElement)


def test_mindstorms::namedelement_constructor_exists():
    assert callable(mindstorms::NamedElement.__init__)


def test_mindstorms::namedelement_constructor_args():
    sig = inspect.signature(mindstorms::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mindstorms::namedelement_has_name():
    assert hasattr(mindstorms::NamedElement, "name")
    descriptor = None
    for klass in mindstorms::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Instruction)


def test_mindstorms::instruction_constructor_exists():
    assert callable(mindstorms::Instruction.__init__)


def test_mindstorms::instruction_constructor_args():
    sig = inspect.signature(mindstorms::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::release_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Release)


def test_mindstorms::release_constructor_exists():
    assert callable(mindstorms::Release.__init__)


def test_mindstorms::release_constructor_args():
    sig = inspect.signature(mindstorms::Release.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::rotate_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Rotate)


def test_mindstorms::rotate_constructor_exists():
    assert callable(mindstorms::Rotate.__init__)


def test_mindstorms::rotate_constructor_args():
    sig = inspect.signature(mindstorms::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "random" in params, "Missing parameter 'random'"
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_mindstorms::rotate_has_random():
    assert hasattr(mindstorms::Rotate, "random")
    descriptor = None
    for klass in mindstorms::Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::rotate_has_degrees():
    assert hasattr(mindstorms::Rotate, "degrees")
    descriptor = None
    for klass in mindstorms::Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::begin_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Begin)


def test_mindstorms::begin_constructor_exists():
    assert callable(mindstorms::Begin.__init__)


def test_mindstorms::begin_constructor_args():
    sig = inspect.signature(mindstorms::Begin.__init__)
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
mindstorms::EdgeInstruction_strategy = st.builds(
    mindstorms::EdgeInstruction,
)
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms::Choreography_strategy = st.builds(
    mindstorms::Choreography,
)
mindstorms::Block_strategy = st.builds(
    mindstorms::Block,
)
Block_strategy = st.builds(
    Block,
)
mindstorms::Action_strategy = st.builds(
    mindstorms::Action,
)
Action_strategy = st.builds(
    Action,
)
mindstorms::Grab_strategy = st.builds(
    mindstorms::Grab,
)
mindstorms::End_strategy = st.builds(
    mindstorms::End,
)
mindstorms::GoBackward_strategy = st.builds(
    mindstorms::GoBackward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
mindstorms::GoForward_strategy = st.builds(
    mindstorms::GoForward,
    cm=
        st.integers(),
    infinite=
        st.booleans()
)
mindstorms::NamedElement_strategy = st.builds(
    mindstorms::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mindstorms::Instruction_strategy = st.builds(
    mindstorms::Instruction,
)
mindstorms::Release_strategy = st.builds(
    mindstorms::Release,
)
mindstorms::Rotate_strategy = st.builds(
    mindstorms::Rotate,
    random=
        st.booleans(),
    degrees=
        st.integers()
)
mindstorms::Begin_strategy = st.builds(
    mindstorms::Begin,
)

@given(instance=mindstorms::EdgeInstruction_strategy)
@settings(max_examples=50)
def test_mindstorms::edgeinstruction_instantiation(instance):
    assert isinstance(instance, mindstorms::EdgeInstruction)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mindstorms::Choreography_strategy)
@settings(max_examples=50)
def test_mindstorms::choreography_instantiation(instance):
    assert isinstance(instance, mindstorms::Choreography)

@given(instance=mindstorms::Block_strategy)
@settings(max_examples=50)
def test_mindstorms::block_instantiation(instance):
    assert isinstance(instance, mindstorms::Block)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=mindstorms::Action_strategy)
@settings(max_examples=50)
def test_mindstorms::action_instantiation(instance):
    assert isinstance(instance, mindstorms::Action)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=mindstorms::Grab_strategy)
@settings(max_examples=50)
def test_mindstorms::grab_instantiation(instance):
    assert isinstance(instance, mindstorms::Grab)

@given(instance=mindstorms::End_strategy)
@settings(max_examples=50)
def test_mindstorms::end_instantiation(instance):
    assert isinstance(instance, mindstorms::End)

@given(instance=mindstorms::GoBackward_strategy)
@settings(max_examples=50)
def test_mindstorms::gobackward_instantiation(instance):
    assert isinstance(instance, mindstorms::GoBackward)

@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_infinite_type(instance):
    assert isinstance(instance.infinite, bool)


@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_cm_type(instance):
    assert isinstance(instance.cm, int)


@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms::GoForward_strategy)
@settings(max_examples=50)
def test_mindstorms::goforward_instantiation(instance):
    assert isinstance(instance, mindstorms::GoForward)

@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_cm_type(instance):
    assert isinstance(instance.cm, int)


@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_infinite_type(instance):
    assert isinstance(instance.infinite, bool)


@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=mindstorms::NamedElement_strategy)
@settings(max_examples=50)
def test_mindstorms::namedelement_instantiation(instance):
    assert isinstance(instance, mindstorms::NamedElement)

@given(instance=mindstorms::NamedElement_strategy)
def test_mindstorms::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mindstorms::NamedElement_strategy)
def test_mindstorms::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mindstorms::Instruction_strategy)
@settings(max_examples=50)
def test_mindstorms::instruction_instantiation(instance):
    assert isinstance(instance, mindstorms::Instruction)

@given(instance=mindstorms::Release_strategy)
@settings(max_examples=50)
def test_mindstorms::release_instantiation(instance):
    assert isinstance(instance, mindstorms::Release)

@given(instance=mindstorms::Rotate_strategy)
@settings(max_examples=50)
def test_mindstorms::rotate_instantiation(instance):
    assert isinstance(instance, mindstorms::Rotate)

@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_random_type(instance):
    assert isinstance(instance.random, bool)


@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=mindstorms::Begin_strategy)
@settings(max_examples=50)
def test_mindstorms::begin_instantiation(instance):
    assert isinstance(instance, mindstorms::Begin)
