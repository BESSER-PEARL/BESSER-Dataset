import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wh::Output,
    wh::Commands,
    wh::Input,
    wh::Definition,
    wh::Function,
    wh::Program,
    wh::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh::output_is_not_abstract():
    assert not inspect.isabstract(wh::Output)


def test_wh::output_constructor_exists():
    assert callable(wh::Output.__init__)


def test_wh::output_constructor_args():
    sig = inspect.signature(wh::Output.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_wh::output_has_variable():
    assert hasattr(wh::Output, "variable")
    descriptor = None
    for klass in wh::Output.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_wh::commands_is_not_abstract():
    assert not inspect.isabstract(wh::Commands)


def test_wh::commands_constructor_exists():
    assert callable(wh::Commands.__init__)


def test_wh::commands_constructor_args():
    sig = inspect.signature(wh::Commands.__init__)
    params = list(sig.parameters.keys())
    assert "command" in params, "Missing parameter 'command'"

def test_wh::commands_has_command():
    assert hasattr(wh::Commands, "command")
    descriptor = None
    for klass in wh::Commands.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)



def test_wh::input_is_not_abstract():
    assert not inspect.isabstract(wh::Input)


def test_wh::input_constructor_exists():
    assert callable(wh::Input.__init__)


def test_wh::input_constructor_args():
    sig = inspect.signature(wh::Input.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_wh::input_has_variable():
    assert hasattr(wh::Input, "variable")
    descriptor = None
    for klass in wh::Input.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh::function_is_not_abstract():
    assert not inspect.isabstract(wh::Function)


def test_wh::function_constructor_exists():
    assert callable(wh::Function.__init__)


def test_wh::function_constructor_args():
    sig = inspect.signature(wh::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::function_has_name():
    assert hasattr(wh::Function, "name")
    descriptor = None
    for klass in wh::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::program_is_not_abstract():
    assert not inspect.isabstract(wh::Program)


def test_wh::program_constructor_exists():
    assert callable(wh::Program.__init__)


def test_wh::program_constructor_args():
    sig = inspect.signature(wh::Program.__init__)
    params = list(sig.parameters.keys())



def test_wh::model_is_not_abstract():
    assert not inspect.isabstract(wh::Model)


def test_wh::model_constructor_exists():
    assert callable(wh::Model.__init__)


def test_wh::model_constructor_args():
    sig = inspect.signature(wh::Model.__init__)
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
wh::Output_strategy = st.builds(
    wh::Output,
    variable=
        safe_text
)
wh::Commands_strategy = st.builds(
    wh::Commands,
    command=
        safe_text
)
wh::Input_strategy = st.builds(
    wh::Input,
    variable=
        safe_text
)
wh::Definition_strategy = st.builds(
    wh::Definition,
)
wh::Function_strategy = st.builds(
    wh::Function,
    name=
        safe_text
)
wh::Program_strategy = st.builds(
    wh::Program,
)
wh::Model_strategy = st.builds(
    wh::Model,
)

@given(instance=wh::Output_strategy)
@settings(max_examples=50)
def test_wh::output_instantiation(instance):
    assert isinstance(instance, wh::Output)

@given(instance=wh::Output_strategy)
def test_wh::output_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=wh::Output_strategy)
def test_wh::output_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh::Commands_strategy)
@settings(max_examples=50)
def test_wh::commands_instantiation(instance):
    assert isinstance(instance, wh::Commands)

@given(instance=wh::Commands_strategy)
def test_wh::commands_command_type(instance):
    assert isinstance(instance.command, str)


@given(instance=wh::Commands_strategy)
def test_wh::commands_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=wh::Input_strategy)
@settings(max_examples=50)
def test_wh::input_instantiation(instance):
    assert isinstance(instance, wh::Input)

@given(instance=wh::Input_strategy)
def test_wh::input_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=wh::Input_strategy)
def test_wh::input_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Function_strategy)
@settings(max_examples=50)
def test_wh::function_instantiation(instance):
    assert isinstance(instance, wh::Function)

@given(instance=wh::Function_strategy)
def test_wh::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Function_strategy)
def test_wh::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::Program_strategy)
@settings(max_examples=50)
def test_wh::program_instantiation(instance):
    assert isinstance(instance, wh::Program)

@given(instance=wh::Model_strategy)
@settings(max_examples=50)
def test_wh::model_instantiation(instance):
    assert isinstance(instance, wh::Model)
