import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wh::Command,
    wh::Commands,
    wh::Program,
    wh::Wh,
    wh::Definition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh::command_is_not_abstract():
    assert not inspect.isabstract(wh::Command)


def test_wh::command_constructor_exists():
    assert callable(wh::Command.__init__)


def test_wh::command_constructor_args():
    sig = inspect.signature(wh::Command.__init__)
    params = list(sig.parameters.keys())
    assert "cmd" in params, "Missing parameter 'cmd'"

def test_wh::command_has_cmd():
    assert hasattr(wh::Command, "cmd")
    descriptor = None
    for klass in wh::Command.__mro__:
        if "cmd" in klass.__dict__:
            descriptor = klass.__dict__["cmd"]
            break
    assert isinstance(descriptor, property)



def test_wh::commands_is_not_abstract():
    assert not inspect.isabstract(wh::Commands)


def test_wh::commands_constructor_exists():
    assert callable(wh::Commands.__init__)


def test_wh::commands_constructor_args():
    sig = inspect.signature(wh::Commands.__init__)
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



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_wh::definition_has_input():
    assert hasattr(wh::Definition, "input")
    descriptor = None
    for klass in wh::Definition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_wh::definition_has_output():
    assert hasattr(wh::Definition, "output")
    descriptor = None
    for klass in wh::Definition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
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
wh::Command_strategy = st.builds(
    wh::Command,
    cmd=
        safe_text
)
wh::Commands_strategy = st.builds(
    wh::Commands,
)
wh::Program_strategy = st.builds(
    wh::Program,
    name=
        safe_text
)
wh::Wh_strategy = st.builds(
    wh::Wh,
)
wh::Definition_strategy = st.builds(
    wh::Definition,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=wh::Command_strategy)
@settings(max_examples=50)
def test_wh::command_instantiation(instance):
    assert isinstance(instance, wh::Command)

@given(instance=wh::Command_strategy)
def test_wh::command_cmd_type(instance):
    assert isinstance(instance.cmd, str)


@given(instance=wh::Command_strategy)
def test_wh::command_cmd_setter(instance):
    original = instance.cmd
    instance.cmd = original
    assert instance.cmd == original

@given(instance=wh::Commands_strategy)
@settings(max_examples=50)
def test_wh::commands_instantiation(instance):
    assert isinstance(instance, wh::Commands)

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

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Definition_strategy)
def test_wh::definition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=wh::Definition_strategy)
def test_wh::definition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=wh::Definition_strategy)
def test_wh::definition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=wh::Definition_strategy)
def test_wh::definition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
