import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wh::Affect,
    wh::Nop,
    wh::EObject,
    wh::Command,
    wh::Output,
    wh::Commands,
    wh::Input,
    wh::Definition,
    wh::Program,
    wh::Wh,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh::affect_is_not_abstract():
    assert not inspect.isabstract(wh::Affect)


def test_wh::affect_constructor_exists():
    assert callable(wh::Affect.__init__)


def test_wh::affect_constructor_args():
    sig = inspect.signature(wh::Affect.__init__)
    params = list(sig.parameters.keys())
    assert "exprs" in params, "Missing parameter 'exprs'"
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::affect_has_exprs():
    assert hasattr(wh::Affect, "exprs")
    descriptor = None
    for klass in wh::Affect.__mro__:
        if "exprs" in klass.__dict__:
            descriptor = klass.__dict__["exprs"]
            break
    assert isinstance(descriptor, property)

def test_wh::affect_has_vars():
    assert hasattr(wh::Affect, "vars")
    descriptor = None
    for klass in wh::Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh::nop_is_not_abstract():
    assert not inspect.isabstract(wh::Nop)


def test_wh::nop_constructor_exists():
    assert callable(wh::Nop.__init__)


def test_wh::nop_constructor_args():
    sig = inspect.signature(wh::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh::nop_has_nop():
    assert hasattr(wh::Nop, "nop")
    descriptor = None
    for klass in wh::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh::eobject_is_not_abstract():
    assert not inspect.isabstract(wh::EObject)


def test_wh::eobject_constructor_exists():
    assert callable(wh::EObject.__init__)


def test_wh::eobject_constructor_args():
    sig = inspect.signature(wh::EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh::command_is_not_abstract():
    assert not inspect.isabstract(wh::Command)


def test_wh::command_constructor_exists():
    assert callable(wh::Command.__init__)


def test_wh::command_constructor_args():
    sig = inspect.signature(wh::Command.__init__)
    params = list(sig.parameters.keys())



def test_wh::output_is_not_abstract():
    assert not inspect.isabstract(wh::Output)


def test_wh::output_constructor_exists():
    assert callable(wh::Output.__init__)


def test_wh::output_constructor_args():
    sig = inspect.signature(wh::Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::output_has_vars():
    assert hasattr(wh::Output, "vars")
    descriptor = None
    for klass in wh::Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh::commands_is_not_abstract():
    assert not inspect.isabstract(wh::Commands)


def test_wh::commands_constructor_exists():
    assert callable(wh::Commands.__init__)


def test_wh::commands_constructor_args():
    sig = inspect.signature(wh::Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh::input_is_not_abstract():
    assert not inspect.isabstract(wh::Input)


def test_wh::input_constructor_exists():
    assert callable(wh::Input.__init__)


def test_wh::input_constructor_args():
    sig = inspect.signature(wh::Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::input_has_vars():
    assert hasattr(wh::Input, "vars")
    descriptor = None
    for klass in wh::Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh::program_is_not_abstract():
    assert not inspect.isabstract(wh::Program)


def test_wh::program_constructor_exists():
    assert callable(wh::Program.__init__)


def test_wh::program_constructor_args():
    sig = inspect.signature(wh::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::program_has_name():
    assert hasattr(wh::Program, "name")
    descriptor = None
    for klass in wh::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::wh_is_not_abstract():
    assert not inspect.isabstract(wh::Wh)


def test_wh::wh_constructor_exists():
    assert callable(wh::Wh.__init__)


def test_wh::wh_constructor_args():
    sig = inspect.signature(wh::Wh.__init__)
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
wh::Affect_strategy = st.builds(
    wh::Affect,
    exprs=
        safe_text,
    vars=
        safe_text
)
wh::Nop_strategy = st.builds(
    wh::Nop,
    nop=
        safe_text
)
wh::EObject_strategy = st.builds(
    wh::EObject,
)
wh::Command_strategy = st.builds(
    wh::Command,
)
wh::Output_strategy = st.builds(
    wh::Output,
    vars=
        safe_text
)
wh::Commands_strategy = st.builds(
    wh::Commands,
)
wh::Input_strategy = st.builds(
    wh::Input,
    vars=
        safe_text
)
wh::Definition_strategy = st.builds(
    wh::Definition,
)
wh::Program_strategy = st.builds(
    wh::Program,
    name=
        safe_text
)
wh::Wh_strategy = st.builds(
    wh::Wh,
)

@given(instance=wh::Affect_strategy)
@settings(max_examples=50)
def test_wh::affect_instantiation(instance):
    assert isinstance(instance, wh::Affect)

@given(instance=wh::Affect_strategy)
def test_wh::affect_exprs_type(instance):
    assert isinstance(instance.exprs, str)


@given(instance=wh::Affect_strategy)
def test_wh::affect_exprs_setter(instance):
    original = instance.exprs
    instance.exprs = original
    assert instance.exprs == original

@given(instance=wh::Affect_strategy)
def test_wh::affect_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Affect_strategy)
def test_wh::affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh::Nop_strategy)
@settings(max_examples=50)
def test_wh::nop_instantiation(instance):
    assert isinstance(instance, wh::Nop)

@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh::EObject_strategy)
@settings(max_examples=50)
def test_wh::eobject_instantiation(instance):
    assert isinstance(instance, wh::EObject)

@given(instance=wh::Command_strategy)
@settings(max_examples=50)
def test_wh::command_instantiation(instance):
    assert isinstance(instance, wh::Command)

@given(instance=wh::Output_strategy)
@settings(max_examples=50)
def test_wh::output_instantiation(instance):
    assert isinstance(instance, wh::Output)

@given(instance=wh::Output_strategy)
def test_wh::output_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Output_strategy)
def test_wh::output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh::Commands_strategy)
@settings(max_examples=50)
def test_wh::commands_instantiation(instance):
    assert isinstance(instance, wh::Commands)

@given(instance=wh::Input_strategy)
@settings(max_examples=50)
def test_wh::input_instantiation(instance):
    assert isinstance(instance, wh::Input)

@given(instance=wh::Input_strategy)
def test_wh::input_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Input_strategy)
def test_wh::input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Program_strategy)
@settings(max_examples=50)
def test_wh::program_instantiation(instance):
    assert isinstance(instance, wh::Program)

@given(instance=wh::Program_strategy)
def test_wh::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Program_strategy)
def test_wh::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::Wh_strategy)
@settings(max_examples=50)
def test_wh::wh_instantiation(instance):
    assert isinstance(instance, wh::Wh)
