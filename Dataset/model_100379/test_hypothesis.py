import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mmb_Modification,
    mmb_Transition,
    mmb_Mode,
    mmb_Automaton,
    mmb_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mmb_modification_is_not_abstract():
    assert not inspect.isabstract(mmb_Modification)


def test_mmb_modification_constructor_exists():
    assert callable(mmb_Modification.__init__)


def test_mmb_modification_constructor_args():
    sig = inspect.signature(mmb_Modification.__init__)
    params = list(sig.parameters.keys())
    assert "VarName" in params, "Missing parameter 'VarName'"
    assert "VarType" in params, "Missing parameter 'VarType'"

def test_mmb_modification_has_VarName():
    assert hasattr(mmb_Modification, "VarName")
    descriptor = None
    for klass in mmb_Modification.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)

def test_mmb_modification_has_VarType():
    assert hasattr(mmb_Modification, "VarType")
    descriptor = None
    for klass in mmb_Modification.__mro__:
        if "VarType" in klass.__dict__:
            descriptor = klass.__dict__["VarType"]
            break
    assert isinstance(descriptor, property)



def test_mmb_transition_is_not_abstract():
    assert not inspect.isabstract(mmb_Transition)


def test_mmb_transition_constructor_exists():
    assert callable(mmb_Transition.__init__)


def test_mmb_transition_constructor_args():
    sig = inspect.signature(mmb_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"

def test_mmb_transition_has_Event():
    assert hasattr(mmb_Transition, "Event")
    descriptor = None
    for klass in mmb_Transition.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)



def test_mmb_mode_is_not_abstract():
    assert not inspect.isabstract(mmb_Mode)


def test_mmb_mode_constructor_exists():
    assert callable(mmb_Mode.__init__)


def test_mmb_mode_constructor_args():
    sig = inspect.signature(mmb_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "InitialState" in params, "Missing parameter 'InitialState'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Dimension" in params, "Missing parameter 'Dimension'"
    assert "Shape" in params, "Missing parameter 'Shape'"

def test_mmb_mode_has_InitialState():
    assert hasattr(mmb_Mode, "InitialState")
    descriptor = None
    for klass in mmb_Mode.__mro__:
        if "InitialState" in klass.__dict__:
            descriptor = klass.__dict__["InitialState"]
            break
    assert isinstance(descriptor, property)

def test_mmb_mode_has_Name():
    assert hasattr(mmb_Mode, "Name")
    descriptor = None
    for klass in mmb_Mode.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_mmb_mode_has_Dimension():
    assert hasattr(mmb_Mode, "Dimension")
    descriptor = None
    for klass in mmb_Mode.__mro__:
        if "Dimension" in klass.__dict__:
            descriptor = klass.__dict__["Dimension"]
            break
    assert isinstance(descriptor, property)

def test_mmb_mode_has_Shape():
    assert hasattr(mmb_Mode, "Shape")
    descriptor = None
    for klass in mmb_Mode.__mro__:
        if "Shape" in klass.__dict__:
            descriptor = klass.__dict__["Shape"]
            break
    assert isinstance(descriptor, property)



def test_mmb_automaton_is_not_abstract():
    assert not inspect.isabstract(mmb_Automaton)


def test_mmb_automaton_constructor_exists():
    assert callable(mmb_Automaton.__init__)


def test_mmb_automaton_constructor_args():
    sig = inspect.signature(mmb_Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_mmb_automaton_has_Name():
    assert hasattr(mmb_Automaton, "Name")
    descriptor = None
    for klass in mmb_Automaton.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_mmb_model_is_not_abstract():
    assert not inspect.isabstract(mmb_Model)


def test_mmb_model_constructor_exists():
    assert callable(mmb_Model.__init__)


def test_mmb_model_constructor_args():
    sig = inspect.signature(mmb_Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_mmb_model_has_Name():
    assert hasattr(mmb_Model, "Name")
    descriptor = None
    for klass in mmb_Model.__mro__:
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
mmb_Modification_strategy = st.builds(
    mmb_Modification,
    VarName=
        safe_text,
    VarType=
        safe_text
)
mmb_Transition_strategy = st.builds(
    mmb_Transition,
    Event=
        safe_text
)
mmb_Mode_strategy = st.builds(
    mmb_Mode,
    InitialState=
        st.booleans(),
    Name=
        safe_text,
    Dimension=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Shape=
        safe_text
)
mmb_Automaton_strategy = st.builds(
    mmb_Automaton,
    Name=
        safe_text
)
mmb_Model_strategy = st.builds(
    mmb_Model,
    Name=
        safe_text
)

@given(instance=mmb_Modification_strategy)
@settings(max_examples=50)
def test_mmb_modification_instantiation(instance):
    assert isinstance(instance, mmb_Modification)



@given(instance=mmb_Modification_strategy)
def test_mmb_modification_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original



@given(instance=mmb_Modification_strategy)
def test_mmb_modification_VarType_setter(instance):
    original = instance.VarType
    instance.VarType = original
    assert instance.VarType == original

@given(instance=mmb_Transition_strategy)
@settings(max_examples=50)
def test_mmb_transition_instantiation(instance):
    assert isinstance(instance, mmb_Transition)



@given(instance=mmb_Transition_strategy)
def test_mmb_transition_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original

@given(instance=mmb_Mode_strategy)
@settings(max_examples=50)
def test_mmb_mode_instantiation(instance):
    assert isinstance(instance, mmb_Mode)



@given(instance=mmb_Mode_strategy)
def test_mmb_mode_InitialState_setter(instance):
    original = instance.InitialState
    instance.InitialState = original
    assert instance.InitialState == original



@given(instance=mmb_Mode_strategy)
def test_mmb_mode_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=mmb_Mode_strategy)
def test_mmb_mode_Dimension_setter(instance):
    original = instance.Dimension
    instance.Dimension = original
    assert instance.Dimension == original



@given(instance=mmb_Mode_strategy)
def test_mmb_mode_Shape_setter(instance):
    original = instance.Shape
    instance.Shape = original
    assert instance.Shape == original

@given(instance=mmb_Automaton_strategy)
@settings(max_examples=50)
def test_mmb_automaton_instantiation(instance):
    assert isinstance(instance, mmb_Automaton)



@given(instance=mmb_Automaton_strategy)
def test_mmb_automaton_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=mmb_Model_strategy)
@settings(max_examples=50)
def test_mmb_model_instantiation(instance):
    assert isinstance(instance, mmb_Model)



@given(instance=mmb_Model_strategy)
def test_mmb_model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
