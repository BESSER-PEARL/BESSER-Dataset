import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    logo::Parameter,
    Instruction,
    logo::ProcCall,
    logo::ProcDeclaration,
    logo::Instruction,
    logo::LogoProgram,
    logo::Right,
    logo::Left,
    logo::Forward,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logo::parameter_is_not_abstract():
    assert not inspect.isabstract(logo::Parameter)


def test_logo::parameter_constructor_exists():
    assert callable(logo::Parameter.__init__)


def test_logo::parameter_constructor_args():
    sig = inspect.signature(logo::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::parameter_has_name():
    assert hasattr(logo::Parameter, "name")
    descriptor = None
    for klass in logo::Parameter.__mro__:
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



def test_logo::proccall_is_not_abstract():
    assert not inspect.isabstract(logo::ProcCall)


def test_logo::proccall_constructor_exists():
    assert callable(logo::ProcCall.__init__)


def test_logo::proccall_constructor_args():
    sig = inspect.signature(logo::ProcCall.__init__)
    params = list(sig.parameters.keys())
    assert "actualArgs" in params, "Missing parameter 'actualArgs'"

def test_logo::proccall_has_actualArgs():
    assert hasattr(logo::ProcCall, "actualArgs")
    descriptor = None
    for klass in logo::ProcCall.__mro__:
        if "actualArgs" in klass.__dict__:
            descriptor = klass.__dict__["actualArgs"]
            break
    assert isinstance(descriptor, property)



def test_logo::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(logo::ProcDeclaration)


def test_logo::procdeclaration_constructor_exists():
    assert callable(logo::ProcDeclaration.__init__)


def test_logo::procdeclaration_constructor_args():
    sig = inspect.signature(logo::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::procdeclaration_has_name():
    assert hasattr(logo::ProcDeclaration, "name")
    descriptor = None
    for klass in logo::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::instruction_is_not_abstract():
    assert not inspect.isabstract(logo::Instruction)


def test_logo::instruction_constructor_exists():
    assert callable(logo::Instruction.__init__)


def test_logo::instruction_constructor_args():
    sig = inspect.signature(logo::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(logo::LogoProgram)


def test_logo::logoprogram_constructor_exists():
    assert callable(logo::LogoProgram.__init__)


def test_logo::logoprogram_constructor_args():
    sig = inspect.signature(logo::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_logo::right_is_not_abstract():
    assert not inspect.isabstract(logo::Right)


def test_logo::right_constructor_exists():
    assert callable(logo::Right.__init__)


def test_logo::right_constructor_args():
    sig = inspect.signature(logo::Right.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo::right_has_angle():
    assert hasattr(logo::Right, "angle")
    descriptor = None
    for klass in logo::Right.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo::left_is_not_abstract():
    assert not inspect.isabstract(logo::Left)


def test_logo::left_constructor_exists():
    assert callable(logo::Left.__init__)


def test_logo::left_constructor_args():
    sig = inspect.signature(logo::Left.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo::left_has_angle():
    assert hasattr(logo::Left, "angle")
    descriptor = None
    for klass in logo::Left.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo::forward_is_not_abstract():
    assert not inspect.isabstract(logo::Forward)


def test_logo::forward_constructor_exists():
    assert callable(logo::Forward.__init__)


def test_logo::forward_constructor_args():
    sig = inspect.signature(logo::Forward.__init__)
    params = list(sig.parameters.keys())
    assert "steps" in params, "Missing parameter 'steps'"

def test_logo::forward_has_steps():
    assert hasattr(logo::Forward, "steps")
    descriptor = None
    for klass in logo::Forward.__mro__:
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
logo::Parameter_strategy = st.builds(
    logo::Parameter,
    name=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
logo::ProcCall_strategy = st.builds(
    logo::ProcCall,
    actualArgs=
        st.integers()
)
logo::ProcDeclaration_strategy = st.builds(
    logo::ProcDeclaration,
    name=
        safe_text
)
logo::Instruction_strategy = st.builds(
    logo::Instruction,
)
logo::LogoProgram_strategy = st.builds(
    logo::LogoProgram,
)
logo::Right_strategy = st.builds(
    logo::Right,
    angle=
        st.integers()
)
logo::Left_strategy = st.builds(
    logo::Left,
    angle=
        st.integers()
)
logo::Forward_strategy = st.builds(
    logo::Forward,
    steps=
        st.integers()
)

@given(instance=logo::Parameter_strategy)
@settings(max_examples=50)
def test_logo::parameter_instantiation(instance):
    assert isinstance(instance, logo::Parameter)

@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=logo::ProcCall_strategy)
@settings(max_examples=50)
def test_logo::proccall_instantiation(instance):
    assert isinstance(instance, logo::ProcCall)

@given(instance=logo::ProcCall_strategy)
def test_logo::proccall_actualArgs_type(instance):
    assert isinstance(instance.actualArgs, int)


@given(instance=logo::ProcCall_strategy)
def test_logo::proccall_actualArgs_setter(instance):
    original = instance.actualArgs
    instance.actualArgs = original
    assert instance.actualArgs == original

@given(instance=logo::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_logo::procdeclaration_instantiation(instance):
    assert isinstance(instance, logo::ProcDeclaration)

@given(instance=logo::ProcDeclaration_strategy)
def test_logo::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::ProcDeclaration_strategy)
def test_logo::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::Instruction_strategy)
@settings(max_examples=50)
def test_logo::instruction_instantiation(instance):
    assert isinstance(instance, logo::Instruction)

@given(instance=logo::LogoProgram_strategy)
@settings(max_examples=50)
def test_logo::logoprogram_instantiation(instance):
    assert isinstance(instance, logo::LogoProgram)

@given(instance=logo::Right_strategy)
@settings(max_examples=50)
def test_logo::right_instantiation(instance):
    assert isinstance(instance, logo::Right)

@given(instance=logo::Right_strategy)
def test_logo::right_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=logo::Right_strategy)
def test_logo::right_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo::Left_strategy)
@settings(max_examples=50)
def test_logo::left_instantiation(instance):
    assert isinstance(instance, logo::Left)

@given(instance=logo::Left_strategy)
def test_logo::left_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=logo::Left_strategy)
def test_logo::left_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo::Forward_strategy)
@settings(max_examples=50)
def test_logo::forward_instantiation(instance):
    assert isinstance(instance, logo::Forward)

@given(instance=logo::Forward_strategy)
def test_logo::forward_steps_type(instance):
    assert isinstance(instance.steps, int)


@given(instance=logo::Forward_strategy)
def test_logo::forward_steps_setter(instance):
    original = instance.steps
    instance.steps = original
    assert instance.steps == original
