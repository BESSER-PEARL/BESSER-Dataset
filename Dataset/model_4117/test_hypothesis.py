import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wh_Output,
    wh_Commands,
    wh_Input,
    wh_Definition,
    wh_Function,
    wh_Program,
    wh_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh_output_is_not_abstract():
    assert not inspect.isabstract(wh_Output)


def test_wh_output_constructor_exists():
    assert callable(wh_Output.__init__)


def test_wh_output_constructor_args():
    sig = inspect.signature(wh_Output.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_wh_output_has_variable():
    assert hasattr(wh_Output, "variable")
    descriptor = None
    for klass in wh_Output.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
    params = list(sig.parameters.keys())
    assert "command" in params, "Missing parameter 'command'"

def test_wh_commands_has_command():
    assert hasattr(wh_Commands, "command")
    descriptor = None
    for klass in wh_Commands.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)



def test_wh_input_is_not_abstract():
    assert not inspect.isabstract(wh_Input)


def test_wh_input_constructor_exists():
    assert callable(wh_Input.__init__)


def test_wh_input_constructor_args():
    sig = inspect.signature(wh_Input.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_wh_input_has_variable():
    assert hasattr(wh_Input, "variable")
    descriptor = None
    for klass in wh_Input.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_wh_definition_is_not_abstract():
    assert not inspect.isabstract(wh_Definition)


def test_wh_definition_constructor_exists():
    assert callable(wh_Definition.__init__)


def test_wh_definition_constructor_args():
    sig = inspect.signature(wh_Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh_function_is_not_abstract():
    assert not inspect.isabstract(wh_Function)


def test_wh_function_constructor_exists():
    assert callable(wh_Function.__init__)


def test_wh_function_constructor_args():
    sig = inspect.signature(wh_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_function_has_name():
    assert hasattr(wh_Function, "name")
    descriptor = None
    for klass in wh_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_program_is_not_abstract():
    assert not inspect.isabstract(wh_Program)


def test_wh_program_constructor_exists():
    assert callable(wh_Program.__init__)


def test_wh_program_constructor_args():
    sig = inspect.signature(wh_Program.__init__)
    params = list(sig.parameters.keys())



def test_wh_model_is_not_abstract():
    assert not inspect.isabstract(wh_Model)


def test_wh_model_constructor_exists():
    assert callable(wh_Model.__init__)


def test_wh_model_constructor_args():
    sig = inspect.signature(wh_Model.__init__)
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
wh_Output_strategy = st.builds(
    wh_Output,
    variable=
        safe_text
)
wh_Commands_strategy = st.builds(
    wh_Commands,
    command=
        safe_text
)
wh_Input_strategy = st.builds(
    wh_Input,
    variable=
        safe_text
)
wh_Definition_strategy = st.builds(
    wh_Definition,
)
wh_Function_strategy = st.builds(
    wh_Function,
    name=
        safe_text
)
wh_Program_strategy = st.builds(
    wh_Program,
)
wh_Model_strategy = st.builds(
    wh_Model,
)

@given(instance=wh_Output_strategy)
@settings(max_examples=50)
def test_wh_output_instantiation(instance):
    assert isinstance(instance, wh_Output)



@given(instance=wh_Output_strategy)
def test_wh_output_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)



@given(instance=wh_Commands_strategy)
def test_wh_commands_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=wh_Input_strategy)
@settings(max_examples=50)
def test_wh_input_instantiation(instance):
    assert isinstance(instance, wh_Input)



@given(instance=wh_Input_strategy)
def test_wh_input_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=wh_Definition_strategy)
@settings(max_examples=50)
def test_wh_definition_instantiation(instance):
    assert isinstance(instance, wh_Definition)

@given(instance=wh_Function_strategy)
@settings(max_examples=50)
def test_wh_function_instantiation(instance):
    assert isinstance(instance, wh_Function)



@given(instance=wh_Function_strategy)
def test_wh_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_Program_strategy)
@settings(max_examples=50)
def test_wh_program_instantiation(instance):
    assert isinstance(instance, wh_Program)

@given(instance=wh_Model_strategy)
@settings(max_examples=50)
def test_wh_model_instantiation(instance):
    assert isinstance(instance, wh_Model)
