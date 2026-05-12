import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    stateMachine_FloatType,
    stateMachine_StringType,
    stateMachine_VarName,
    stateMachine_Condition,
    stateMachine_Transition,
    stateMachine_Test,
    stateMachine_Type,
    stateMachine_State,
    stateMachine_Command,
    stateMachine_Event,
    stateMachine_StateMachine,
    stateMachine_model,
    stateMachine_Modifier,
    stateMachine_DeclaredParameter,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_floattype_is_not_abstract():
    assert not inspect.isabstract(stateMachine_FloatType)


def test_statemachine_floattype_constructor_exists():
    assert callable(stateMachine_FloatType.__init__)


def test_statemachine_floattype_constructor_args():
    sig = inspect.signature(stateMachine_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_stringtype_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StringType)


def test_statemachine_stringtype_constructor_exists():
    assert callable(stateMachine_StringType.__init__)


def test_statemachine_stringtype_constructor_args():
    sig = inspect.signature(stateMachine_StringType.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_varname_is_not_abstract():
    assert not inspect.isabstract(stateMachine_VarName)


def test_statemachine_varname_constructor_exists():
    assert callable(stateMachine_VarName.__init__)


def test_statemachine_varname_constructor_args():
    sig = inspect.signature(stateMachine_VarName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine_varname_has_value():
    assert hasattr(stateMachine_VarName, "value")
    descriptor = None
    for klass in stateMachine_VarName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_condition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Condition)


def test_statemachine_condition_constructor_exists():
    assert callable(stateMachine_Condition.__init__)


def test_statemachine_condition_constructor_args():
    sig = inspect.signature(stateMachine_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_condition_has_name():
    assert hasattr(stateMachine_Condition, "name")
    descriptor = None
    for klass in stateMachine_Condition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(stateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(stateMachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_test_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Test)


def test_statemachine_test_constructor_exists():
    assert callable(stateMachine_Test.__init__)


def test_statemachine_test_constructor_args():
    sig = inspect.signature(stateMachine_Test.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_type_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Type)


def test_statemachine_type_constructor_exists():
    assert callable(stateMachine_Type.__init__)


def test_statemachine_type_constructor_args():
    sig = inspect.signature(stateMachine_Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_statemachine_type_has_type():
    assert hasattr(stateMachine_Type, "type")
    descriptor = None
    for klass in stateMachine_Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(stateMachine_State, "name")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Command)


def test_statemachine_command_constructor_exists():
    assert callable(stateMachine_Command.__init__)


def test_statemachine_command_constructor_args():
    sig = inspect.signature(stateMachine_Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_command_has_name():
    assert hasattr(stateMachine_Command, "name")
    descriptor = None
    for klass in stateMachine_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(stateMachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(stateMachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_event_has_name():
    assert hasattr(stateMachine_Event, "name")
    descriptor = None
    for klass in stateMachine_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(stateMachine_StateMachine, "name")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_model_is_not_abstract():
    assert not inspect.isabstract(stateMachine_model)


def test_statemachine_model_constructor_exists():
    assert callable(stateMachine_model.__init__)


def test_statemachine_model_constructor_args():
    sig = inspect.signature(stateMachine_model.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_modifier_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Modifier)


def test_statemachine_modifier_constructor_exists():
    assert callable(stateMachine_Modifier.__init__)


def test_statemachine_modifier_constructor_args():
    sig = inspect.signature(stateMachine_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_statemachine_modifier_has_visibility():
    assert hasattr(stateMachine_Modifier, "visibility")
    descriptor = None
    for klass in stateMachine_Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_declaredparameter_is_not_abstract():
    assert not inspect.isabstract(stateMachine_DeclaredParameter)


def test_statemachine_declaredparameter_constructor_exists():
    assert callable(stateMachine_DeclaredParameter.__init__)


def test_statemachine_declaredparameter_constructor_args():
    sig = inspect.signature(stateMachine_DeclaredParameter.__init__)
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
Type_strategy = st.builds(
    Type,
)
stateMachine_FloatType_strategy = st.builds(
    stateMachine_FloatType,
)
stateMachine_StringType_strategy = st.builds(
    stateMachine_StringType,
)
stateMachine_VarName_strategy = st.builds(
    stateMachine_VarName,
    value=
        safe_text
)
stateMachine_Condition_strategy = st.builds(
    stateMachine_Condition,
    name=
        safe_text
)
stateMachine_Transition_strategy = st.builds(
    stateMachine_Transition,
)
stateMachine_Test_strategy = st.builds(
    stateMachine_Test,
)
stateMachine_Type_strategy = st.builds(
    stateMachine_Type,
    type=
        safe_text
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    name=
        safe_text
)
stateMachine_Command_strategy = st.builds(
    stateMachine_Command,
    name=
        safe_text
)
stateMachine_Event_strategy = st.builds(
    stateMachine_Event,
    name=
        safe_text
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    name=
        safe_text
)
stateMachine_model_strategy = st.builds(
    stateMachine_model,
)
stateMachine_Modifier_strategy = st.builds(
    stateMachine_Modifier,
    visibility=
        safe_text
)
stateMachine_DeclaredParameter_strategy = st.builds(
    stateMachine_DeclaredParameter,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=stateMachine_FloatType_strategy)
@settings(max_examples=50)
def test_statemachine_floattype_instantiation(instance):
    assert isinstance(instance, stateMachine_FloatType)

@given(instance=stateMachine_StringType_strategy)
@settings(max_examples=50)
def test_statemachine_stringtype_instantiation(instance):
    assert isinstance(instance, stateMachine_StringType)

@given(instance=stateMachine_VarName_strategy)
@settings(max_examples=50)
def test_statemachine_varname_instantiation(instance):
    assert isinstance(instance, stateMachine_VarName)



@given(instance=stateMachine_VarName_strategy)
def test_statemachine_varname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stateMachine_Condition_strategy)
@settings(max_examples=50)
def test_statemachine_condition_instantiation(instance):
    assert isinstance(instance, stateMachine_Condition)



@given(instance=stateMachine_Condition_strategy)
def test_statemachine_condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)

@given(instance=stateMachine_Test_strategy)
@settings(max_examples=50)
def test_statemachine_test_instantiation(instance):
    assert isinstance(instance, stateMachine_Test)

@given(instance=stateMachine_Type_strategy)
@settings(max_examples=50)
def test_statemachine_type_instantiation(instance):
    assert isinstance(instance, stateMachine_Type)



@given(instance=stateMachine_Type_strategy)
def test_statemachine_type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Command_strategy)
@settings(max_examples=50)
def test_statemachine_command_instantiation(instance):
    assert isinstance(instance, stateMachine_Command)



@given(instance=stateMachine_Command_strategy)
def test_statemachine_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, stateMachine_Event)



@given(instance=stateMachine_Event_strategy)
def test_statemachine_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_model_strategy)
@settings(max_examples=50)
def test_statemachine_model_instantiation(instance):
    assert isinstance(instance, stateMachine_model)

@given(instance=stateMachine_Modifier_strategy)
@settings(max_examples=50)
def test_statemachine_modifier_instantiation(instance):
    assert isinstance(instance, stateMachine_Modifier)



@given(instance=stateMachine_Modifier_strategy)
def test_statemachine_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=stateMachine_DeclaredParameter_strategy)
@settings(max_examples=50)
def test_statemachine_declaredparameter_instantiation(instance):
    assert isinstance(instance, stateMachine_DeclaredParameter)
