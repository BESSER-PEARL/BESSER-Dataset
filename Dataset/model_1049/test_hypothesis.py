import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    efsm_Variable,
    efsm_Param,
    efsm_ContextVariable,
    AbstractState,
    efsm_State,
    efsm_Event,
    efsm_Input,
    efsm_AbstractState,
    efsm_InitialState,
    efsm_Transition,
    efsm_EFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_efsm_variable_is_not_abstract():
    assert not inspect.isabstract(efsm_Variable)


def test_efsm_variable_constructor_exists():
    assert callable(efsm_Variable.__init__)


def test_efsm_variable_constructor_args():
    sig = inspect.signature(efsm_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_efsm_variable_has_class_():
    assert hasattr(efsm_Variable, "class_")
    descriptor = None
    for klass in efsm_Variable.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_efsm_variable_has_name():
    assert hasattr(efsm_Variable, "name")
    descriptor = None
    for klass in efsm_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm_variable_has_type():
    assert hasattr(efsm_Variable, "type")
    descriptor = None
    for klass in efsm_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_efsm_param_is_not_abstract():
    assert not inspect.isabstract(efsm_Param)


def test_efsm_param_constructor_exists():
    assert callable(efsm_Param.__init__)


def test_efsm_param_constructor_args():
    sig = inspect.signature(efsm_Param.__init__)
    params = list(sig.parameters.keys())
    assert "argName" in params, "Missing parameter 'argName'"
    assert "argType" in params, "Missing parameter 'argType'"

def test_efsm_param_has_argName():
    assert hasattr(efsm_Param, "argName")
    descriptor = None
    for klass in efsm_Param.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)

def test_efsm_param_has_argType():
    assert hasattr(efsm_Param, "argType")
    descriptor = None
    for klass in efsm_Param.__mro__:
        if "argType" in klass.__dict__:
            descriptor = klass.__dict__["argType"]
            break
    assert isinstance(descriptor, property)



def test_efsm_contextvariable_is_not_abstract():
    assert not inspect.isabstract(efsm_ContextVariable)


def test_efsm_contextvariable_constructor_exists():
    assert callable(efsm_ContextVariable.__init__)


def test_efsm_contextvariable_constructor_args():
    sig = inspect.signature(efsm_ContextVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_efsm_contextvariable_has_name():
    assert hasattr(efsm_ContextVariable, "name")
    descriptor = None
    for klass in efsm_ContextVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm_contextvariable_has_type():
    assert hasattr(efsm_ContextVariable, "type")
    descriptor = None
    for klass in efsm_ContextVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_efsm_state_is_not_abstract():
    assert not inspect.isabstract(efsm_State)


def test_efsm_state_constructor_exists():
    assert callable(efsm_State.__init__)


def test_efsm_state_constructor_args():
    sig = inspect.signature(efsm_State.__init__)
    params = list(sig.parameters.keys())



def test_efsm_event_is_not_abstract():
    assert not inspect.isabstract(efsm_Event)


def test_efsm_event_constructor_exists():
    assert callable(efsm_Event.__init__)


def test_efsm_event_constructor_args():
    sig = inspect.signature(efsm_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_efsm_event_has_name():
    assert hasattr(efsm_Event, "name")
    descriptor = None
    for klass in efsm_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm_event_has_return_():
    assert hasattr(efsm_Event, "return_")
    descriptor = None
    for klass in efsm_Event.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_efsm_event_has_class_():
    assert hasattr(efsm_Event, "class_")
    descriptor = None
    for klass in efsm_Event.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_efsm_input_is_not_abstract():
    assert not inspect.isabstract(efsm_Input)


def test_efsm_input_constructor_exists():
    assert callable(efsm_Input.__init__)


def test_efsm_input_constructor_args():
    sig = inspect.signature(efsm_Input.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_input_has_name():
    assert hasattr(efsm_Input, "name")
    descriptor = None
    for klass in efsm_Input.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(efsm_AbstractState)


def test_efsm_abstractstate_constructor_exists():
    assert callable(efsm_AbstractState.__init__)


def test_efsm_abstractstate_constructor_args():
    sig = inspect.signature(efsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_abstractstate_has_name():
    assert hasattr(efsm_AbstractState, "name")
    descriptor = None
    for klass in efsm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(efsm_InitialState)


def test_efsm_initialstate_constructor_exists():
    assert callable(efsm_InitialState.__init__)


def test_efsm_initialstate_constructor_args():
    sig = inspect.signature(efsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_efsm_transition_is_not_abstract():
    assert not inspect.isabstract(efsm_Transition)


def test_efsm_transition_constructor_exists():
    assert callable(efsm_Transition.__init__)


def test_efsm_transition_constructor_args():
    sig = inspect.signature(efsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_transition_has_output():
    assert hasattr(efsm_Transition, "output")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_guard():
    assert hasattr(efsm_Transition, "guard")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_action():
    assert hasattr(efsm_Transition, "action")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_name():
    assert hasattr(efsm_Transition, "name")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm_efsm_is_not_abstract():
    assert not inspect.isabstract(efsm_EFSM)


def test_efsm_efsm_constructor_exists():
    assert callable(efsm_EFSM.__init__)


def test_efsm_efsm_constructor_args():
    sig = inspect.signature(efsm_EFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_efsm_has_name():
    assert hasattr(efsm_EFSM, "name")
    descriptor = None
    for klass in efsm_EFSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
efsm_Variable_strategy = st.builds(
    efsm_Variable,
    class_=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
efsm_Param_strategy = st.builds(
    efsm_Param,
    argName=
        safe_text,
    argType=
        safe_text
)
efsm_ContextVariable_strategy = st.builds(
    efsm_ContextVariable,
    name=
        safe_text,
    type=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
efsm_State_strategy = st.builds(
    efsm_State,
)
efsm_Event_strategy = st.builds(
    efsm_Event,
    name=
        safe_text,
    return_=
        safe_text,
    class_=
        safe_text
)
efsm_Input_strategy = st.builds(
    efsm_Input,
    name=
        safe_text
)
efsm_AbstractState_strategy = st.builds(
    efsm_AbstractState,
    name=
        safe_text
)
efsm_InitialState_strategy = st.builds(
    efsm_InitialState,
)
efsm_Transition_strategy = st.builds(
    efsm_Transition,
    output=
        safe_text,
    guard=
        safe_text,
    action=
        safe_text,
    name=
        safe_text
)
efsm_EFSM_strategy = st.builds(
    efsm_EFSM,
    name=
        safe_text
)

@given(instance=efsm_Variable_strategy)
@settings(max_examples=50)
def test_efsm_variable_instantiation(instance):
    assert isinstance(instance, efsm_Variable)



@given(instance=efsm_Variable_strategy)
def test_efsm_variable_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=efsm_Variable_strategy)
def test_efsm_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=efsm_Variable_strategy)
def test_efsm_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=efsm_Param_strategy)
@settings(max_examples=50)
def test_efsm_param_instantiation(instance):
    assert isinstance(instance, efsm_Param)



@given(instance=efsm_Param_strategy)
def test_efsm_param_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original



@given(instance=efsm_Param_strategy)
def test_efsm_param_argType_setter(instance):
    original = instance.argType
    instance.argType = original
    assert instance.argType == original

@given(instance=efsm_ContextVariable_strategy)
@settings(max_examples=50)
def test_efsm_contextvariable_instantiation(instance):
    assert isinstance(instance, efsm_ContextVariable)



@given(instance=efsm_ContextVariable_strategy)
def test_efsm_contextvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=efsm_ContextVariable_strategy)
def test_efsm_contextvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=efsm_State_strategy)
@settings(max_examples=50)
def test_efsm_state_instantiation(instance):
    assert isinstance(instance, efsm_State)

@given(instance=efsm_Event_strategy)
@settings(max_examples=50)
def test_efsm_event_instantiation(instance):
    assert isinstance(instance, efsm_Event)



@given(instance=efsm_Event_strategy)
def test_efsm_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=efsm_Event_strategy)
def test_efsm_event_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=efsm_Event_strategy)
def test_efsm_event_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=efsm_Input_strategy)
@settings(max_examples=50)
def test_efsm_input_instantiation(instance):
    assert isinstance(instance, efsm_Input)



@given(instance=efsm_Input_strategy)
def test_efsm_input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm_AbstractState_strategy)
@settings(max_examples=50)
def test_efsm_abstractstate_instantiation(instance):
    assert isinstance(instance, efsm_AbstractState)



@given(instance=efsm_AbstractState_strategy)
def test_efsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm_InitialState_strategy)
@settings(max_examples=50)
def test_efsm_initialstate_instantiation(instance):
    assert isinstance(instance, efsm_InitialState)

@given(instance=efsm_Transition_strategy)
@settings(max_examples=50)
def test_efsm_transition_instantiation(instance):
    assert isinstance(instance, efsm_Transition)



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm_EFSM_strategy)
@settings(max_examples=50)
def test_efsm_efsm_instantiation(instance):
    assert isinstance(instance, efsm_EFSM)



@given(instance=efsm_EFSM_strategy)
def test_efsm_efsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
