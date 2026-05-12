import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    logo_Parameter,
    Instruction,
    logo_ProcCall,
    logo_ProcDeclaration,
    logo_Instruction,
    logo_LogoProgram,
    logo_Right,
    logo_Left,
    logo_Forward,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logo_parameter_is_not_abstract():
    assert not inspect.isabstract(logo_Parameter)


def test_logo_parameter_constructor_exists():
    assert callable(logo_Parameter.__init__)


def test_logo_parameter_constructor_args():
    sig = inspect.signature(logo_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_parameter_has_name():
    assert hasattr(logo_Parameter, "name")
    descriptor = None
    for klass in logo_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo_proccall_is_not_abstract():
    assert not inspect.isabstract(logo_ProcCall)


def test_logo_proccall_constructor_exists():
    assert callable(logo_ProcCall.__init__)


def test_logo_proccall_constructor_args():
    sig = inspect.signature(logo_ProcCall.__init__)
    params = list(sig.parameters.keys())
    assert "actualArgs" in params, "Missing parameter 'actualArgs'"

def test_logo_proccall_has_actualArgs():
    assert hasattr(logo_ProcCall, "actualArgs")
    descriptor = None
    for klass in logo_ProcCall.__mro__:
        if "actualArgs" in klass.__dict__:
            descriptor = klass.__dict__["actualArgs"]
            break
    assert isinstance(descriptor, property)



def test_logo_procdeclaration_is_not_abstract():
    assert not inspect.isabstract(logo_ProcDeclaration)


def test_logo_procdeclaration_constructor_exists():
    assert callable(logo_ProcDeclaration.__init__)


def test_logo_procdeclaration_constructor_args():
    sig = inspect.signature(logo_ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_procdeclaration_has_name():
    assert hasattr(logo_ProcDeclaration, "name")
    descriptor = None
    for klass in logo_ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_instruction_is_not_abstract():
    assert not inspect.isabstract(logo_Instruction)


def test_logo_instruction_constructor_exists():
    assert callable(logo_Instruction.__init__)


def test_logo_instruction_constructor_args():
    sig = inspect.signature(logo_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo_logoprogram_is_not_abstract():
    assert not inspect.isabstract(logo_LogoProgram)


def test_logo_logoprogram_constructor_exists():
    assert callable(logo_LogoProgram.__init__)


def test_logo_logoprogram_constructor_args():
    sig = inspect.signature(logo_LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_logo_right_is_not_abstract():
    assert not inspect.isabstract(logo_Right)


def test_logo_right_constructor_exists():
    assert callable(logo_Right.__init__)


def test_logo_right_constructor_args():
    sig = inspect.signature(logo_Right.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo_right_has_angle():
    assert hasattr(logo_Right, "angle")
    descriptor = None
    for klass in logo_Right.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo_left_is_not_abstract():
    assert not inspect.isabstract(logo_Left)


def test_logo_left_constructor_exists():
    assert callable(logo_Left.__init__)


def test_logo_left_constructor_args():
    sig = inspect.signature(logo_Left.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo_left_has_angle():
    assert hasattr(logo_Left, "angle")
    descriptor = None
    for klass in logo_Left.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo_forward_is_not_abstract():
    assert not inspect.isabstract(logo_Forward)


def test_logo_forward_constructor_exists():
    assert callable(logo_Forward.__init__)


def test_logo_forward_constructor_args():
    sig = inspect.signature(logo_Forward.__init__)
    params = list(sig.parameters.keys())
    assert "steps" in params, "Missing parameter 'steps'"

def test_logo_forward_has_steps():
    assert hasattr(logo_Forward, "steps")
    descriptor = None
    for klass in logo_Forward.__mro__:
        if "steps" in klass.__dict__:
            descriptor = klass.__dict__["steps"]
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
logo_Parameter_strategy = st.builds(
    logo_Parameter,
    name=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
logo_ProcCall_strategy = st.builds(
    logo_ProcCall,
    actualArgs=
        st.integers()
)
logo_ProcDeclaration_strategy = st.builds(
    logo_ProcDeclaration,
    name=
        safe_text
)
logo_Instruction_strategy = st.builds(
    logo_Instruction,
)
logo_LogoProgram_strategy = st.builds(
    logo_LogoProgram,
)
logo_Right_strategy = st.builds(
    logo_Right,
    angle=
        st.integers()
)
logo_Left_strategy = st.builds(
    logo_Left,
    angle=
        st.integers()
)
logo_Forward_strategy = st.builds(
    logo_Forward,
    steps=
        st.integers()
)

@given(instance=logo_Parameter_strategy)
@settings(max_examples=50)
def test_logo_parameter_instantiation(instance):
    assert isinstance(instance, logo_Parameter)



@given(instance=logo_Parameter_strategy)
def test_logo_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=logo_ProcCall_strategy)
@settings(max_examples=50)
def test_logo_proccall_instantiation(instance):
    assert isinstance(instance, logo_ProcCall)



@given(instance=logo_ProcCall_strategy)
def test_logo_proccall_actualArgs_setter(instance):
    original = instance.actualArgs
    instance.actualArgs = original
    assert instance.actualArgs == original

@given(instance=logo_ProcDeclaration_strategy)
@settings(max_examples=50)
def test_logo_procdeclaration_instantiation(instance):
    assert isinstance(instance, logo_ProcDeclaration)



@given(instance=logo_ProcDeclaration_strategy)
def test_logo_procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo_Instruction_strategy)
@settings(max_examples=50)
def test_logo_instruction_instantiation(instance):
    assert isinstance(instance, logo_Instruction)

@given(instance=logo_LogoProgram_strategy)
@settings(max_examples=50)
def test_logo_logoprogram_instantiation(instance):
    assert isinstance(instance, logo_LogoProgram)

@given(instance=logo_Right_strategy)
@settings(max_examples=50)
def test_logo_right_instantiation(instance):
    assert isinstance(instance, logo_Right)



@given(instance=logo_Right_strategy)
def test_logo_right_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo_Left_strategy)
@settings(max_examples=50)
def test_logo_left_instantiation(instance):
    assert isinstance(instance, logo_Left)



@given(instance=logo_Left_strategy)
def test_logo_left_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo_Forward_strategy)
@settings(max_examples=50)
def test_logo_forward_instantiation(instance):
    assert isinstance(instance, logo_Forward)



@given(instance=logo_Forward_strategy)
def test_logo_forward_steps_setter(instance):
    original = instance.steps
    instance.steps = original
    assert instance.steps == original
