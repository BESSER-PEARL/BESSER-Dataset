import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    statemachine::StatePropertyExpression,
    statemachine::VerbatimExpression,
    statemachine::Command,
    Command,
    statemachine::PrintCommand,
    statemachine::ExecuteCommand,
    statemachine::SetCommand,
    statemachine::Expression,
    statemachine::Transition,
    statemachine::State,
    statemachine::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statepropertyexpression_is_not_abstract():
    assert not inspect.isabstract(statemachine::StatePropertyExpression)


def test_statemachine::statepropertyexpression_constructor_exists():
    assert callable(statemachine::StatePropertyExpression.__init__)


def test_statemachine::statepropertyexpression_constructor_args():
    sig = inspect.signature(statemachine::StatePropertyExpression.__init__)
    params = list(sig.parameters.keys())
    assert "property" in params, "Missing parameter 'property'"

def test_statemachine::statepropertyexpression_has_property():
    assert hasattr(statemachine::StatePropertyExpression, "property")
    descriptor = None
    for klass in statemachine::StatePropertyExpression.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::verbatimexpression_is_not_abstract():
    assert not inspect.isabstract(statemachine::VerbatimExpression)


def test_statemachine::verbatimexpression_constructor_exists():
    assert callable(statemachine::VerbatimExpression.__init__)


def test_statemachine::verbatimexpression_constructor_args():
    sig = inspect.signature(statemachine::VerbatimExpression.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine::verbatimexpression_has_code():
    assert hasattr(statemachine::VerbatimExpression, "code")
    descriptor = None
    for klass in statemachine::VerbatimExpression.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::command_is_not_abstract():
    assert not inspect.isabstract(statemachine::Command)


def test_statemachine::command_constructor_exists():
    assert callable(statemachine::Command.__init__)


def test_statemachine::command_constructor_args():
    sig = inspect.signature(statemachine::Command.__init__)
    params = list(sig.parameters.keys())



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::printcommand_is_not_abstract():
    assert not inspect.isabstract(statemachine::PrintCommand)


def test_statemachine::printcommand_constructor_exists():
    assert callable(statemachine::PrintCommand.__init__)


def test_statemachine::printcommand_constructor_args():
    sig = inspect.signature(statemachine::PrintCommand.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::executecommand_is_not_abstract():
    assert not inspect.isabstract(statemachine::ExecuteCommand)


def test_statemachine::executecommand_constructor_exists():
    assert callable(statemachine::ExecuteCommand.__init__)


def test_statemachine::executecommand_constructor_args():
    sig = inspect.signature(statemachine::ExecuteCommand.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_statemachine::executecommand_has_operation():
    assert hasattr(statemachine::ExecuteCommand, "operation")
    descriptor = None
    for klass in statemachine::ExecuteCommand.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::setcommand_is_not_abstract():
    assert not inspect.isabstract(statemachine::SetCommand)


def test_statemachine::setcommand_constructor_exists():
    assert callable(statemachine::SetCommand.__init__)


def test_statemachine::setcommand_constructor_args():
    sig = inspect.signature(statemachine::SetCommand.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_statemachine::setcommand_has_signal():
    assert hasattr(statemachine::SetCommand, "signal")
    descriptor = None
    for klass in statemachine::SetCommand.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::expression_is_not_abstract():
    assert not inspect.isabstract(statemachine::Expression)


def test_statemachine::expression_constructor_exists():
    assert callable(statemachine::Expression.__init__)


def test_statemachine::expression_constructor_args():
    sig = inspect.signature(statemachine::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_statemachine::state_has_id():
    assert hasattr(statemachine::State, "id")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_name():
    assert hasattr(statemachine::State, "name")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_final():
    assert hasattr(statemachine::State, "final")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_initial():
    assert hasattr(statemachine::State, "initial")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statemachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::Statemachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::Statemachine.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
statemachine::StatePropertyExpression_strategy = st.builds(
    statemachine::StatePropertyExpression,
    property=
        safe_text
)
statemachine::VerbatimExpression_strategy = st.builds(
    statemachine::VerbatimExpression,
    code=
        safe_text
)
statemachine::Command_strategy = st.builds(
    statemachine::Command,
)
Command_strategy = st.builds(
    Command,
)
statemachine::PrintCommand_strategy = st.builds(
    statemachine::PrintCommand,
)
statemachine::ExecuteCommand_strategy = st.builds(
    statemachine::ExecuteCommand,
    operation=
        safe_text
)
statemachine::SetCommand_strategy = st.builds(
    statemachine::SetCommand,
    signal=
        safe_text
)
statemachine::Expression_strategy = st.builds(
    statemachine::Expression,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    id=
        safe_text,
    name=
        safe_text,
    final=
        st.booleans(),
    initial=
        st.booleans()
)
statemachine::Statemachine_strategy = st.builds(
    statemachine::Statemachine,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=statemachine::StatePropertyExpression_strategy)
@settings(max_examples=50)
def test_statemachine::statepropertyexpression_instantiation(instance):
    assert isinstance(instance, statemachine::StatePropertyExpression)

@given(instance=statemachine::StatePropertyExpression_strategy)
def test_statemachine::statepropertyexpression_property_type(instance):
    assert isinstance(instance.property, str)


@given(instance=statemachine::StatePropertyExpression_strategy)
def test_statemachine::statepropertyexpression_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original

@given(instance=statemachine::VerbatimExpression_strategy)
@settings(max_examples=50)
def test_statemachine::verbatimexpression_instantiation(instance):
    assert isinstance(instance, statemachine::VerbatimExpression)

@given(instance=statemachine::VerbatimExpression_strategy)
def test_statemachine::verbatimexpression_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=statemachine::VerbatimExpression_strategy)
def test_statemachine::verbatimexpression_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine::Command_strategy)
@settings(max_examples=50)
def test_statemachine::command_instantiation(instance):
    assert isinstance(instance, statemachine::Command)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=statemachine::PrintCommand_strategy)
@settings(max_examples=50)
def test_statemachine::printcommand_instantiation(instance):
    assert isinstance(instance, statemachine::PrintCommand)

@given(instance=statemachine::ExecuteCommand_strategy)
@settings(max_examples=50)
def test_statemachine::executecommand_instantiation(instance):
    assert isinstance(instance, statemachine::ExecuteCommand)

@given(instance=statemachine::ExecuteCommand_strategy)
def test_statemachine::executecommand_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=statemachine::ExecuteCommand_strategy)
def test_statemachine::executecommand_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=statemachine::SetCommand_strategy)
@settings(max_examples=50)
def test_statemachine::setcommand_instantiation(instance):
    assert isinstance(instance, statemachine::SetCommand)

@given(instance=statemachine::SetCommand_strategy)
def test_statemachine::setcommand_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=statemachine::SetCommand_strategy)
def test_statemachine::setcommand_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=statemachine::Expression_strategy)
@settings(max_examples=50)
def test_statemachine::expression_instantiation(instance):
    assert isinstance(instance, statemachine::Expression)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=statemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::Statemachine)
