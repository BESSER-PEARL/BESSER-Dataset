import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mmb::Modification,
    mmb::Transition,
    mmb::Mode,
    mmb::Automaton,
    mmb::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mmb::modification_is_not_abstract():
    assert not inspect.isabstract(mmb::Modification)


def test_mmb::modification_constructor_exists():
    assert callable(mmb::Modification.__init__)


def test_mmb::modification_constructor_args():
    sig = inspect.signature(mmb::Modification.__init__)
    params = list(sig.parameters.keys())
    assert "VarName" in params, "Missing parameter 'VarName'"
    assert "VarType" in params, "Missing parameter 'VarType'"

def test_mmb::modification_has_VarName():
    assert hasattr(mmb::Modification, "VarName")
    descriptor = None
    for klass in mmb::Modification.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)

def test_mmb::modification_has_VarType():
    assert hasattr(mmb::Modification, "VarType")
    descriptor = None
    for klass in mmb::Modification.__mro__:
        if "VarType" in klass.__dict__:
            descriptor = klass.__dict__["VarType"]
            break
    assert isinstance(descriptor, property)



def test_mmb::transition_is_not_abstract():
    assert not inspect.isabstract(mmb::Transition)


def test_mmb::transition_constructor_exists():
    assert callable(mmb::Transition.__init__)


def test_mmb::transition_constructor_args():
    sig = inspect.signature(mmb::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"

def test_mmb::transition_has_Event():
    assert hasattr(mmb::Transition, "Event")
    descriptor = None
    for klass in mmb::Transition.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)



def test_mmb::mode_is_not_abstract():
    assert not inspect.isabstract(mmb::Mode)


def test_mmb::mode_constructor_exists():
    assert callable(mmb::Mode.__init__)


def test_mmb::mode_constructor_args():
    sig = inspect.signature(mmb::Mode.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Shape" in params, "Missing parameter 'Shape'"
    assert "InitialState" in params, "Missing parameter 'InitialState'"
    assert "Dimension" in params, "Missing parameter 'Dimension'"

def test_mmb::mode_has_Name():
    assert hasattr(mmb::Mode, "Name")
    descriptor = None
    for klass in mmb::Mode.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_mmb::mode_has_Shape():
    assert hasattr(mmb::Mode, "Shape")
    descriptor = None
    for klass in mmb::Mode.__mro__:
        if "Shape" in klass.__dict__:
            descriptor = klass.__dict__["Shape"]
            break
    assert isinstance(descriptor, property)

def test_mmb::mode_has_InitialState():
    assert hasattr(mmb::Mode, "InitialState")
    descriptor = None
    for klass in mmb::Mode.__mro__:
        if "InitialState" in klass.__dict__:
            descriptor = klass.__dict__["InitialState"]
            break
    assert isinstance(descriptor, property)

def test_mmb::mode_has_Dimension():
    assert hasattr(mmb::Mode, "Dimension")
    descriptor = None
    for klass in mmb::Mode.__mro__:
        if "Dimension" in klass.__dict__:
            descriptor = klass.__dict__["Dimension"]
            break
    assert isinstance(descriptor, property)



def test_mmb::automaton_is_not_abstract():
    assert not inspect.isabstract(mmb::Automaton)


def test_mmb::automaton_constructor_exists():
    assert callable(mmb::Automaton.__init__)


def test_mmb::automaton_constructor_args():
    sig = inspect.signature(mmb::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_mmb::automaton_has_Name():
    assert hasattr(mmb::Automaton, "Name")
    descriptor = None
    for klass in mmb::Automaton.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_mmb::model_is_not_abstract():
    assert not inspect.isabstract(mmb::Model)


def test_mmb::model_constructor_exists():
    assert callable(mmb::Model.__init__)


def test_mmb::model_constructor_args():
    sig = inspect.signature(mmb::Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_mmb::model_has_Name():
    assert hasattr(mmb::Model, "Name")
    descriptor = None
    for klass in mmb::Model.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
mmb::Modification_strategy = st.builds(
    mmb::Modification,
    VarName=
        safe_text,
    VarType=
        safe_text
)
mmb::Transition_strategy = st.builds(
    mmb::Transition,
    Event=
        safe_text
)
mmb::Mode_strategy = st.builds(
    mmb::Mode,
    Name=
        safe_text,
    Shape=
        safe_text,
    InitialState=
        st.booleans(),
    Dimension=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mmb::Automaton_strategy = st.builds(
    mmb::Automaton,
    Name=
        safe_text
)
mmb::Model_strategy = st.builds(
    mmb::Model,
    Name=
        safe_text
)

@given(instance=mmb::Modification_strategy)
@settings(max_examples=50)
def test_mmb::modification_instantiation(instance):
    assert isinstance(instance, mmb::Modification)

@given(instance=mmb::Modification_strategy)
def test_mmb::modification_VarName_type(instance):
    assert isinstance(instance.VarName, str)


@given(instance=mmb::Modification_strategy)
def test_mmb::modification_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original

@given(instance=mmb::Modification_strategy)
def test_mmb::modification_VarType_type(instance):
    assert isinstance(instance.VarType, str)


@given(instance=mmb::Modification_strategy)
def test_mmb::modification_VarType_setter(instance):
    original = instance.VarType
    instance.VarType = original
    assert instance.VarType == original

@given(instance=mmb::Transition_strategy)
@settings(max_examples=50)
def test_mmb::transition_instantiation(instance):
    assert isinstance(instance, mmb::Transition)

@given(instance=mmb::Transition_strategy)
def test_mmb::transition_Event_type(instance):
    assert isinstance(instance.Event, str)


@given(instance=mmb::Transition_strategy)
def test_mmb::transition_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original

@given(instance=mmb::Mode_strategy)
@settings(max_examples=50)
def test_mmb::mode_instantiation(instance):
    assert isinstance(instance, mmb::Mode)

@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Shape_type(instance):
    assert isinstance(instance.Shape, str)


@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Shape_setter(instance):
    original = instance.Shape
    instance.Shape = original
    assert instance.Shape == original

@given(instance=mmb::Mode_strategy)
def test_mmb::mode_InitialState_type(instance):
    assert isinstance(instance.InitialState, bool)


@given(instance=mmb::Mode_strategy)
def test_mmb::mode_InitialState_setter(instance):
    original = instance.InitialState
    instance.InitialState = original
    assert instance.InitialState == original

@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Dimension_type(instance):
    assert isinstance(instance.Dimension, float)


@given(instance=mmb::Mode_strategy)
def test_mmb::mode_Dimension_setter(instance):
    original = instance.Dimension
    instance.Dimension = original
    assert instance.Dimension == original

@given(instance=mmb::Automaton_strategy)
@settings(max_examples=50)
def test_mmb::automaton_instantiation(instance):
    assert isinstance(instance, mmb::Automaton)

@given(instance=mmb::Automaton_strategy)
def test_mmb::automaton_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=mmb::Automaton_strategy)
def test_mmb::automaton_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=mmb::Model_strategy)
@settings(max_examples=50)
def test_mmb::model_instantiation(instance):
    assert isinstance(instance, mmb::Model)

@given(instance=mmb::Model_strategy)
def test_mmb::model_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=mmb::Model_strategy)
def test_mmb::model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
