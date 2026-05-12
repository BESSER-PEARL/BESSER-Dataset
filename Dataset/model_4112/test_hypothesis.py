import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wh_Affect,
    wh_Nop,
    wh_EObject,
    wh_Command,
    wh_Output,
    wh_Commands,
    wh_Input,
    wh_Definition,
    wh_Program,
    wh_Wh,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh_affect_is_not_abstract():
    assert not inspect.isabstract(wh_Affect)


def test_wh_affect_constructor_exists():
    assert callable(wh_Affect.__init__)


def test_wh_affect_constructor_args():
    sig = inspect.signature(wh_Affect.__init__)
    params = list(sig.parameters.keys())
    assert "exprs" in params, "Missing parameter 'exprs'"
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_affect_has_exprs():
    assert hasattr(wh_Affect, "exprs")
    descriptor = None
    for klass in wh_Affect.__mro__:
        if "exprs" in klass.__dict__:
            descriptor = klass.__dict__["exprs"]
            break
    assert isinstance(descriptor, property)

def test_wh_affect_has_vars():
    assert hasattr(wh_Affect, "vars")
    descriptor = None
    for klass in wh_Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_nop_is_not_abstract():
    assert not inspect.isabstract(wh_Nop)


def test_wh_nop_constructor_exists():
    assert callable(wh_Nop.__init__)


def test_wh_nop_constructor_args():
    sig = inspect.signature(wh_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh_nop_has_nop():
    assert hasattr(wh_Nop, "nop")
    descriptor = None
    for klass in wh_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh_eobject_is_not_abstract():
    assert not inspect.isabstract(wh_EObject)


def test_wh_eobject_constructor_exists():
    assert callable(wh_EObject.__init__)


def test_wh_eobject_constructor_args():
    sig = inspect.signature(wh_EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh_command_is_not_abstract():
    assert not inspect.isabstract(wh_Command)


def test_wh_command_constructor_exists():
    assert callable(wh_Command.__init__)


def test_wh_command_constructor_args():
    sig = inspect.signature(wh_Command.__init__)
    params = list(sig.parameters.keys())



def test_wh_output_is_not_abstract():
    assert not inspect.isabstract(wh_Output)


def test_wh_output_constructor_exists():
    assert callable(wh_Output.__init__)


def test_wh_output_constructor_args():
    sig = inspect.signature(wh_Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_output_has_vars():
    assert hasattr(wh_Output, "vars")
    descriptor = None
    for klass in wh_Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh_input_is_not_abstract():
    assert not inspect.isabstract(wh_Input)


def test_wh_input_constructor_exists():
    assert callable(wh_Input.__init__)


def test_wh_input_constructor_args():
    sig = inspect.signature(wh_Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_input_has_vars():
    assert hasattr(wh_Input, "vars")
    descriptor = None
    for klass in wh_Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_definition_is_not_abstract():
    assert not inspect.isabstract(wh_Definition)


def test_wh_definition_constructor_exists():
    assert callable(wh_Definition.__init__)


def test_wh_definition_constructor_args():
    sig = inspect.signature(wh_Definition.__init__)
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
wh_Affect_strategy = st.builds(
    wh_Affect,
    exprs=
        safe_text,
    vars=
        safe_text
)
wh_Nop_strategy = st.builds(
    wh_Nop,
    nop=
        safe_text
)
wh_EObject_strategy = st.builds(
    wh_EObject,
)
wh_Command_strategy = st.builds(
    wh_Command,
)
wh_Output_strategy = st.builds(
    wh_Output,
    vars=
        safe_text
)
wh_Commands_strategy = st.builds(
    wh_Commands,
)
wh_Input_strategy = st.builds(
    wh_Input,
    vars=
        safe_text
)
wh_Definition_strategy = st.builds(
    wh_Definition,
)
wh_Program_strategy = st.builds(
    wh_Program,
    name=
        safe_text
)
wh_Wh_strategy = st.builds(
    wh_Wh,
)

@given(instance=wh_Affect_strategy)
@settings(max_examples=50)
def test_wh_affect_instantiation(instance):
    assert isinstance(instance, wh_Affect)



@given(instance=wh_Affect_strategy)
def test_wh_affect_exprs_setter(instance):
    original = instance.exprs
    instance.exprs = original
    assert instance.exprs == original



@given(instance=wh_Affect_strategy)
def test_wh_affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Nop_strategy)
@settings(max_examples=50)
def test_wh_nop_instantiation(instance):
    assert isinstance(instance, wh_Nop)



@given(instance=wh_Nop_strategy)
def test_wh_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh_EObject_strategy)
@settings(max_examples=50)
def test_wh_eobject_instantiation(instance):
    assert isinstance(instance, wh_EObject)

@given(instance=wh_Command_strategy)
@settings(max_examples=50)
def test_wh_command_instantiation(instance):
    assert isinstance(instance, wh_Command)

@given(instance=wh_Output_strategy)
@settings(max_examples=50)
def test_wh_output_instantiation(instance):
    assert isinstance(instance, wh_Output)



@given(instance=wh_Output_strategy)
def test_wh_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)

@given(instance=wh_Input_strategy)
@settings(max_examples=50)
def test_wh_input_instantiation(instance):
    assert isinstance(instance, wh_Input)



@given(instance=wh_Input_strategy)
def test_wh_input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Definition_strategy)
@settings(max_examples=50)
def test_wh_definition_instantiation(instance):
    assert isinstance(instance, wh_Definition)

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
