import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::Modifier,
    stateMachine::DeclaredParameter,
    Type,
    stateMachine::FloatType,
    stateMachine::StringType,
    stateMachine::VarName,
    stateMachine::Condition,
    stateMachine::Transition,
    stateMachine::Test,
    stateMachine::Type,
    stateMachine::State,
    stateMachine::Command,
    stateMachine::Event,
    stateMachine::StateMachine,
    stateMachine::model,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::modifier_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Modifier)


def test_statemachine::modifier_constructor_exists():
    assert callable(stateMachine::Modifier.__init__)


def test_statemachine::modifier_constructor_args():
    sig = inspect.signature(stateMachine::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_statemachine::modifier_has_visibility():
    assert hasattr(stateMachine::Modifier, "visibility")
    descriptor = None
    for klass in stateMachine::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::declaredparameter_is_not_abstract():
    assert not inspect.isabstract(stateMachine::DeclaredParameter)


def test_statemachine::declaredparameter_constructor_exists():
    assert callable(stateMachine::DeclaredParameter.__init__)


def test_statemachine::declaredparameter_constructor_args():
    sig = inspect.signature(stateMachine::DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::floattype_is_not_abstract():
    assert not inspect.isabstract(stateMachine::FloatType)


def test_statemachine::floattype_constructor_exists():
    assert callable(stateMachine::FloatType.__init__)


def test_statemachine::floattype_constructor_args():
    sig = inspect.signature(stateMachine::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::stringtype_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StringType)


def test_statemachine::stringtype_constructor_exists():
    assert callable(stateMachine::StringType.__init__)


def test_statemachine::stringtype_constructor_args():
    sig = inspect.signature(stateMachine::StringType.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::varname_is_not_abstract():
    assert not inspect.isabstract(stateMachine::VarName)


def test_statemachine::varname_constructor_exists():
    assert callable(stateMachine::VarName.__init__)


def test_statemachine::varname_constructor_args():
    sig = inspect.signature(stateMachine::VarName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine::varname_has_value():
    assert hasattr(stateMachine::VarName, "value")
    descriptor = None
    for klass in stateMachine::VarName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::condition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Condition)


def test_statemachine::condition_constructor_exists():
    assert callable(stateMachine::Condition.__init__)


def test_statemachine::condition_constructor_args():
    sig = inspect.signature(stateMachine::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::condition_has_name():
    assert hasattr(stateMachine::Condition, "name")
    descriptor = None
    for klass in stateMachine::Condition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::test_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Test)


def test_statemachine::test_constructor_exists():
    assert callable(stateMachine::Test.__init__)


def test_statemachine::test_constructor_args():
    sig = inspect.signature(stateMachine::Test.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::type_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Type)


def test_statemachine::type_constructor_exists():
    assert callable(stateMachine::Type.__init__)


def test_statemachine::type_constructor_args():
    sig = inspect.signature(stateMachine::Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_statemachine::type_has_type():
    assert hasattr(stateMachine::Type, "type")
    descriptor = None
    for klass in stateMachine::Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(stateMachine::State, "name")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::command_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Command)


def test_statemachine::command_constructor_exists():
    assert callable(stateMachine::Command.__init__)


def test_statemachine::command_constructor_args():
    sig = inspect.signature(stateMachine::Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::command_has_name():
    assert hasattr(stateMachine::Command, "name")
    descriptor = None
    for klass in stateMachine::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(stateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(stateMachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::event_has_name():
    assert hasattr(stateMachine::Event, "name")
    descriptor = None
    for klass in stateMachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::model_is_not_abstract():
    assert not inspect.isabstract(stateMachine::model)


def test_statemachine::model_constructor_exists():
    assert callable(stateMachine::model.__init__)


def test_statemachine::model_constructor_args():
    sig = inspect.signature(stateMachine::model.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "Final",
        "Initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
stateMachine::Modifier_strategy = st.builds(
    stateMachine::Modifier,
    visibility=
        safe_text
)
stateMachine::DeclaredParameter_strategy = st.builds(
    stateMachine::DeclaredParameter,
)
Type_strategy = st.builds(
    Type,
)
stateMachine::FloatType_strategy = st.builds(
    stateMachine::FloatType,
)
stateMachine::StringType_strategy = st.builds(
    stateMachine::StringType,
)
stateMachine::VarName_strategy = st.builds(
    stateMachine::VarName,
    value=
        safe_text
)
stateMachine::Condition_strategy = st.builds(
    stateMachine::Condition,
    name=
        safe_text
)
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
)
stateMachine::Test_strategy = st.builds(
    stateMachine::Test,
)
stateMachine::Type_strategy = st.builds(
    stateMachine::Type,
    type=
        safe_text
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    name=
        safe_text
)
stateMachine::Command_strategy = st.builds(
    stateMachine::Command,
    name=
        safe_text
)
stateMachine::Event_strategy = st.builds(
    stateMachine::Event,
    name=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    name=
        safe_text
)
stateMachine::model_strategy = st.builds(
    stateMachine::model,
)

@given(instance=stateMachine::Modifier_strategy)
@settings(max_examples=50)
def test_statemachine::modifier_instantiation(instance):
    assert isinstance(instance, stateMachine::Modifier)

@given(instance=stateMachine::Modifier_strategy)
def test_statemachine::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=stateMachine::Modifier_strategy)
def test_statemachine::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=stateMachine::DeclaredParameter_strategy)
@settings(max_examples=50)
def test_statemachine::declaredparameter_instantiation(instance):
    assert isinstance(instance, stateMachine::DeclaredParameter)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=stateMachine::FloatType_strategy)
@settings(max_examples=50)
def test_statemachine::floattype_instantiation(instance):
    assert isinstance(instance, stateMachine::FloatType)

@given(instance=stateMachine::StringType_strategy)
@settings(max_examples=50)
def test_statemachine::stringtype_instantiation(instance):
    assert isinstance(instance, stateMachine::StringType)

@given(instance=stateMachine::VarName_strategy)
@settings(max_examples=50)
def test_statemachine::varname_instantiation(instance):
    assert isinstance(instance, stateMachine::VarName)

@given(instance=stateMachine::VarName_strategy)
def test_statemachine::varname_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=stateMachine::VarName_strategy)
def test_statemachine::varname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachine::Condition_strategy)
@settings(max_examples=50)
def test_statemachine::condition_instantiation(instance):
    assert isinstance(instance, stateMachine::Condition)

@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Condition_strategy)
def test_statemachine::condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)

@given(instance=stateMachine::Test_strategy)
@settings(max_examples=50)
def test_statemachine::test_instantiation(instance):
    assert isinstance(instance, stateMachine::Test)

@given(instance=stateMachine::Type_strategy)
@settings(max_examples=50)
def test_statemachine::type_instantiation(instance):
    assert isinstance(instance, stateMachine::Type)

@given(instance=stateMachine::Type_strategy)
def test_statemachine::type_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stateMachine::Type_strategy)
def test_statemachine::type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Command_strategy)
@settings(max_examples=50)
def test_statemachine::command_instantiation(instance):
    assert isinstance(instance, stateMachine::Command)

@given(instance=stateMachine::Command_strategy)
def test_statemachine::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Command_strategy)
def test_statemachine::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, stateMachine::Event)

@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::model_strategy)
@settings(max_examples=50)
def test_statemachine::model_instantiation(instance):
    assert isinstance(instance, stateMachine::model)
