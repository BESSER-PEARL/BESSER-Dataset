import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Command,
    statemachine_ExecuteCommand,
    statemachine_SetCommand,
    statemachine_Expression,
    statemachine_Command,
    statemachine_Transition,
    statemachine_State,
    statemachine_Statemachine,
    Expression,
    statemachine_StatePropertyExpression,
    statemachine_VerbatimExpression,
    statemachine_PrintCommand,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_executecommand_is_not_abstract():
    assert not inspect.isabstract(statemachine_ExecuteCommand)


def test_statemachine_executecommand_constructor_exists():
    assert callable(statemachine_ExecuteCommand.__init__)


def test_statemachine_executecommand_constructor_args():
    sig = inspect.signature(statemachine_ExecuteCommand.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_statemachine_executecommand_has_operation():
    assert hasattr(statemachine_ExecuteCommand, "operation")
    descriptor = None
    for klass in statemachine_ExecuteCommand.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_setcommand_is_not_abstract():
    assert not inspect.isabstract(statemachine_SetCommand)


def test_statemachine_setcommand_constructor_exists():
    assert callable(statemachine_SetCommand.__init__)


def test_statemachine_setcommand_constructor_args():
    sig = inspect.signature(statemachine_SetCommand.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_statemachine_setcommand_has_signal():
    assert hasattr(statemachine_SetCommand, "signal")
    descriptor = None
    for klass in statemachine_SetCommand.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_expression_is_not_abstract():
    assert not inspect.isabstract(statemachine_Expression)


def test_statemachine_expression_constructor_exists():
    assert callable(statemachine_Expression.__init__)


def test_statemachine_expression_constructor_args():
    sig = inspect.signature(statemachine_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(statemachine_Command)


def test_statemachine_command_constructor_exists():
    assert callable(statemachine_Command.__init__)


def test_statemachine_command_constructor_args():
    sig = inspect.signature(statemachine_Command.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_final():
    assert hasattr(statemachine_State, "final")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_initial():
    assert hasattr(statemachine_State, "initial")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_id():
    assert hasattr(statemachine_State, "id")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statepropertyexpression_is_not_abstract():
    assert not inspect.isabstract(statemachine_StatePropertyExpression)


def test_statemachine_statepropertyexpression_constructor_exists():
    assert callable(statemachine_StatePropertyExpression.__init__)


def test_statemachine_statepropertyexpression_constructor_args():
    sig = inspect.signature(statemachine_StatePropertyExpression.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"

def test_statemachine_statepropertyexpression_has__property():
    assert hasattr(statemachine_StatePropertyExpression, "_property")
    descriptor = None
    for klass in statemachine_StatePropertyExpression.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_verbatimexpression_is_not_abstract():
    assert not inspect.isabstract(statemachine_VerbatimExpression)


def test_statemachine_verbatimexpression_constructor_exists():
    assert callable(statemachine_VerbatimExpression.__init__)


def test_statemachine_verbatimexpression_constructor_args():
    sig = inspect.signature(statemachine_VerbatimExpression.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine_verbatimexpression_has_code():
    assert hasattr(statemachine_VerbatimExpression, "code")
    descriptor = None
    for klass in statemachine_VerbatimExpression.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_printcommand_is_not_abstract():
    assert not inspect.isabstract(statemachine_PrintCommand)


def test_statemachine_printcommand_constructor_exists():
    assert callable(statemachine_PrintCommand.__init__)


def test_statemachine_printcommand_constructor_args():
    sig = inspect.signature(statemachine_PrintCommand.__init__)
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
Command_strategy = st.builds(
    Command,
)
statemachine_ExecuteCommand_strategy = st.builds(
    statemachine_ExecuteCommand,
    operation=
        safe_text
)
statemachine_SetCommand_strategy = st.builds(
    statemachine_SetCommand,
    signal=
        safe_text
)
statemachine_Expression_strategy = st.builds(
    statemachine_Expression,
)
statemachine_Command_strategy = st.builds(
    statemachine_Command,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text,
    final=
        st.booleans(),
    initial=
        st.booleans(),
    id=
        safe_text
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
)
Expression_strategy = st.builds(
    Expression,
)
statemachine_StatePropertyExpression_strategy = st.builds(
    statemachine_StatePropertyExpression,
    _property=
        safe_text
)
statemachine_VerbatimExpression_strategy = st.builds(
    statemachine_VerbatimExpression,
    code=
        safe_text
)
statemachine_PrintCommand_strategy = st.builds(
    statemachine_PrintCommand,
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=statemachine_ExecuteCommand_strategy)
@settings(max_examples=50)
def test_statemachine_executecommand_instantiation(instance):
    assert isinstance(instance, statemachine_ExecuteCommand)



@given(instance=statemachine_ExecuteCommand_strategy)
def test_statemachine_executecommand_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=statemachine_SetCommand_strategy)
@settings(max_examples=50)
def test_statemachine_setcommand_instantiation(instance):
    assert isinstance(instance, statemachine_SetCommand)



@given(instance=statemachine_SetCommand_strategy)
def test_statemachine_setcommand_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=statemachine_Expression_strategy)
@settings(max_examples=50)
def test_statemachine_expression_instantiation(instance):
    assert isinstance(instance, statemachine_Expression)

@given(instance=statemachine_Command_strategy)
@settings(max_examples=50)
def test_statemachine_command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=statemachine_StatePropertyExpression_strategy)
@settings(max_examples=50)
def test_statemachine_statepropertyexpression_instantiation(instance):
    assert isinstance(instance, statemachine_StatePropertyExpression)



@given(instance=statemachine_StatePropertyExpression_strategy)
def test_statemachine_statepropertyexpression__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=statemachine_VerbatimExpression_strategy)
@settings(max_examples=50)
def test_statemachine_verbatimexpression_instantiation(instance):
    assert isinstance(instance, statemachine_VerbatimExpression)



@given(instance=statemachine_VerbatimExpression_strategy)
def test_statemachine_verbatimexpression_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine_PrintCommand_strategy)
@settings(max_examples=50)
def test_statemachine_printcommand_instantiation(instance):
    assert isinstance(instance, statemachine_PrintCommand)
