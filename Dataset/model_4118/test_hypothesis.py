import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wh_Command,
    wh_Commands,
    wh_Program,
    wh_Wh,
    wh_Definition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh_command_is_not_abstract():
    assert not inspect.isabstract(wh_Command)


def test_wh_command_constructor_exists():
    assert callable(wh_Command.__init__)


def test_wh_command_constructor_args():
    sig = inspect.signature(wh_Command.__init__)
    params = list(sig.parameters.keys())
    assert "cmd" in params, "Missing parameter 'cmd'"

def test_wh_command_has_cmd():
    assert hasattr(wh_Command, "cmd")
    descriptor = None
    for klass in wh_Command.__mro__:
        if "cmd" in klass.__dict__:
            descriptor = klass.__dict__["cmd"]
            break
    assert isinstance(descriptor, property)



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh_program_is_not_abstract():
    assert not inspect.isabstract(wh_Program)


def test_wh_program_constructor_exists():
    assert callable(wh_Program.__init__)


def test_wh_program_constructor_args():
    sig = inspect.signature(wh_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_program_has_name():
    assert hasattr(wh_Program, "name")
    descriptor = None
    for klass in wh_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_wh_is_not_abstract():
    assert not inspect.isabstract(wh_Wh)


def test_wh_wh_constructor_exists():
    assert callable(wh_Wh.__init__)


def test_wh_wh_constructor_args():
    sig = inspect.signature(wh_Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh_definition_is_not_abstract():
    assert not inspect.isabstract(wh_Definition)


def test_wh_definition_constructor_exists():
    assert callable(wh_Definition.__init__)


def test_wh_definition_constructor_args():
    sig = inspect.signature(wh_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_wh_definition_has_input():
    assert hasattr(wh_Definition, "input")
    descriptor = None
    for klass in wh_Definition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_wh_definition_has_output():
    assert hasattr(wh_Definition, "output")
    descriptor = None
    for klass in wh_Definition.__mro__:
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
wh_Command_strategy = st.builds(
    wh_Command,
    cmd=
        safe_text
)
wh_Commands_strategy = st.builds(
    wh_Commands,
)
wh_Program_strategy = st.builds(
    wh_Program,
    name=
        safe_text
)
wh_Wh_strategy = st.builds(
    wh_Wh,
)
wh_Definition_strategy = st.builds(
    wh_Definition,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=wh_Command_strategy)
@settings(max_examples=50)
def test_wh_command_instantiation(instance):
    assert isinstance(instance, wh_Command)



@given(instance=wh_Command_strategy)
def test_wh_command_cmd_setter(instance):
    original = instance.cmd
    instance.cmd = original
    assert instance.cmd == original

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)

@given(instance=wh_Program_strategy)
@settings(max_examples=50)
def test_wh_program_instantiation(instance):
    assert isinstance(instance, wh_Program)



@given(instance=wh_Program_strategy)
def test_wh_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_Wh_strategy)
@settings(max_examples=50)
def test_wh_wh_instantiation(instance):
    assert isinstance(instance, wh_Wh)

@given(instance=wh_Definition_strategy)
@settings(max_examples=50)
def test_wh_definition_instantiation(instance):
    assert isinstance(instance, wh_Definition)



@given(instance=wh_Definition_strategy)
def test_wh_definition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=wh_Definition_strategy)
def test_wh_definition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
