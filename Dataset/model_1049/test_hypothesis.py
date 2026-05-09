import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    efsm::Variable,
    efsm::Param,
    efsm::ContextVariable,
    AbstractState,
    efsm::State,
    efsm::Event,
    efsm::Input,
    efsm::AbstractState,
    efsm::InitialState,
    efsm::Transition,
    efsm::EFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_efsm::variable_is_not_abstract():
    assert not inspect.isabstract(efsm::Variable)


def test_efsm::variable_constructor_exists():
    assert callable(efsm::Variable.__init__)


def test_efsm::variable_constructor_args():
    sig = inspect.signature(efsm::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "type" in params, "Missing parameter 'type'"

def test_efsm::variable_has_name():
    assert hasattr(efsm::Variable, "name")
    descriptor = None
    for klass in efsm::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm::variable_has_class_():
    assert hasattr(efsm::Variable, "class_")
    descriptor = None
    for klass in efsm::Variable.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_efsm::variable_has_type():
    assert hasattr(efsm::Variable, "type")
    descriptor = None
    for klass in efsm::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_efsm::param_is_not_abstract():
    assert not inspect.isabstract(efsm::Param)


def test_efsm::param_constructor_exists():
    assert callable(efsm::Param.__init__)


def test_efsm::param_constructor_args():
    sig = inspect.signature(efsm::Param.__init__)
    params = list(sig.parameters.keys())
    assert "argType" in params, "Missing parameter 'argType'"
    assert "argName" in params, "Missing parameter 'argName'"

def test_efsm::param_has_argType():
    assert hasattr(efsm::Param, "argType")
    descriptor = None
    for klass in efsm::Param.__mro__:
        if "argType" in klass.__dict__:
            descriptor = klass.__dict__["argType"]
            break
    assert isinstance(descriptor, property)

def test_efsm::param_has_argName():
    assert hasattr(efsm::Param, "argName")
    descriptor = None
    for klass in efsm::Param.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)



def test_efsm::contextvariable_is_not_abstract():
    assert not inspect.isabstract(efsm::ContextVariable)


def test_efsm::contextvariable_constructor_exists():
    assert callable(efsm::ContextVariable.__init__)


def test_efsm::contextvariable_constructor_args():
    sig = inspect.signature(efsm::ContextVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::contextvariable_has_type():
    assert hasattr(efsm::ContextVariable, "type")
    descriptor = None
    for klass in efsm::ContextVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_efsm::contextvariable_has_name():
    assert hasattr(efsm::ContextVariable, "name")
    descriptor = None
    for klass in efsm::ContextVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_efsm::state_is_not_abstract():
    assert not inspect.isabstract(efsm::State)


def test_efsm::state_constructor_exists():
    assert callable(efsm::State.__init__)


def test_efsm::state_constructor_args():
    sig = inspect.signature(efsm::State.__init__)
    params = list(sig.parameters.keys())



def test_efsm::event_is_not_abstract():
    assert not inspect.isabstract(efsm::Event)


def test_efsm::event_constructor_exists():
    assert callable(efsm::Event.__init__)


def test_efsm::event_constructor_args():
    sig = inspect.signature(efsm::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_efsm::event_has_name():
    assert hasattr(efsm::Event, "name")
    descriptor = None
    for klass in efsm::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm::event_has_return_():
    assert hasattr(efsm::Event, "return_")
    descriptor = None
    for klass in efsm::Event.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_efsm::event_has_class_():
    assert hasattr(efsm::Event, "class_")
    descriptor = None
    for klass in efsm::Event.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_efsm::input_is_not_abstract():
    assert not inspect.isabstract(efsm::Input)


def test_efsm::input_constructor_exists():
    assert callable(efsm::Input.__init__)


def test_efsm::input_constructor_args():
    sig = inspect.signature(efsm::Input.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::input_has_name():
    assert hasattr(efsm::Input, "name")
    descriptor = None
    for klass in efsm::Input.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(efsm::AbstractState)


def test_efsm::abstractstate_constructor_exists():
    assert callable(efsm::AbstractState.__init__)


def test_efsm::abstractstate_constructor_args():
    sig = inspect.signature(efsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::abstractstate_has_name():
    assert hasattr(efsm::AbstractState, "name")
    descriptor = None
    for klass in efsm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(efsm::InitialState)


def test_efsm::initialstate_constructor_exists():
    assert callable(efsm::InitialState.__init__)


def test_efsm::initialstate_constructor_args():
    sig = inspect.signature(efsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_efsm::transition_is_not_abstract():
    assert not inspect.isabstract(efsm::Transition)


def test_efsm::transition_constructor_exists():
    assert callable(efsm::Transition.__init__)


def test_efsm::transition_constructor_args():
    sig = inspect.signature(efsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "name" in params, "Missing parameter 'name'"
    assert "output" in params, "Missing parameter 'output'"
    assert "action" in params, "Missing parameter 'action'"

def test_efsm::transition_has_guard():
    assert hasattr(efsm::Transition, "guard")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_name():
    assert hasattr(efsm::Transition, "name")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_output():
    assert hasattr(efsm::Transition, "output")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_efsm::transition_has_action():
    assert hasattr(efsm::Transition, "action")
    descriptor = None
    for klass in efsm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_efsm::efsm_is_not_abstract():
    assert not inspect.isabstract(efsm::EFSM)


def test_efsm::efsm_constructor_exists():
    assert callable(efsm::EFSM.__init__)


def test_efsm::efsm_constructor_args():
    sig = inspect.signature(efsm::EFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm::efsm_has_name():
    assert hasattr(efsm::EFSM, "name")
    descriptor = None
    for klass in efsm::EFSM.__mro__:
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
efsm::Variable_strategy = st.builds(
    efsm::Variable,
    name=
        safe_text,
    class_=
        safe_text,
    type=
        safe_text
)
efsm::Param_strategy = st.builds(
    efsm::Param,
    argType=
        safe_text,
    argName=
        safe_text
)
efsm::ContextVariable_strategy = st.builds(
    efsm::ContextVariable,
    type=
        safe_text,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
efsm::State_strategy = st.builds(
    efsm::State,
)
efsm::Event_strategy = st.builds(
    efsm::Event,
    name=
        safe_text,
    return_=
        safe_text,
    class_=
        safe_text
)
efsm::Input_strategy = st.builds(
    efsm::Input,
    name=
        safe_text
)
efsm::AbstractState_strategy = st.builds(
    efsm::AbstractState,
    name=
        safe_text
)
efsm::InitialState_strategy = st.builds(
    efsm::InitialState,
)
efsm::Transition_strategy = st.builds(
    efsm::Transition,
    guard=
        safe_text,
    name=
        safe_text,
    output=
        safe_text,
    action=
        safe_text
)
efsm::EFSM_strategy = st.builds(
    efsm::EFSM,
    name=
        safe_text
)

@given(instance=efsm::Variable_strategy)
@settings(max_examples=50)
def test_efsm::variable_instantiation(instance):
    assert isinstance(instance, efsm::Variable)

@given(instance=efsm::Variable_strategy)
def test_efsm::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::Variable_strategy)
def test_efsm::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::Variable_strategy)
def test_efsm::variable_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=efsm::Variable_strategy)
def test_efsm::variable_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=efsm::Variable_strategy)
def test_efsm::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=efsm::Variable_strategy)
def test_efsm::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=efsm::Param_strategy)
@settings(max_examples=50)
def test_efsm::param_instantiation(instance):
    assert isinstance(instance, efsm::Param)

@given(instance=efsm::Param_strategy)
def test_efsm::param_argType_type(instance):
    assert isinstance(instance.argType, str)


@given(instance=efsm::Param_strategy)
def test_efsm::param_argType_setter(instance):
    original = instance.argType
    instance.argType = original
    assert instance.argType == original

@given(instance=efsm::Param_strategy)
def test_efsm::param_argName_type(instance):
    assert isinstance(instance.argName, str)


@given(instance=efsm::Param_strategy)
def test_efsm::param_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original

@given(instance=efsm::ContextVariable_strategy)
@settings(max_examples=50)
def test_efsm::contextvariable_instantiation(instance):
    assert isinstance(instance, efsm::ContextVariable)

@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::ContextVariable_strategy)
def test_efsm::contextvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=efsm::State_strategy)
@settings(max_examples=50)
def test_efsm::state_instantiation(instance):
    assert isinstance(instance, efsm::State)

@given(instance=efsm::Event_strategy)
@settings(max_examples=50)
def test_efsm::event_instantiation(instance):
    assert isinstance(instance, efsm::Event)

@given(instance=efsm::Event_strategy)
def test_efsm::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::Event_strategy)
def test_efsm::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::Event_strategy)
def test_efsm::event_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=efsm::Event_strategy)
def test_efsm::event_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=efsm::Event_strategy)
def test_efsm::event_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=efsm::Event_strategy)
def test_efsm::event_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=efsm::Input_strategy)
@settings(max_examples=50)
def test_efsm::input_instantiation(instance):
    assert isinstance(instance, efsm::Input)

@given(instance=efsm::Input_strategy)
def test_efsm::input_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::Input_strategy)
def test_efsm::input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::AbstractState_strategy)
@settings(max_examples=50)
def test_efsm::abstractstate_instantiation(instance):
    assert isinstance(instance, efsm::AbstractState)

@given(instance=efsm::AbstractState_strategy)
def test_efsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::AbstractState_strategy)
def test_efsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::InitialState_strategy)
@settings(max_examples=50)
def test_efsm::initialstate_instantiation(instance):
    assert isinstance(instance, efsm::InitialState)

@given(instance=efsm::Transition_strategy)
@settings(max_examples=50)
def test_efsm::transition_instantiation(instance):
    assert isinstance(instance, efsm::Transition)

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=efsm::Transition_strategy)
def test_efsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=efsm::Transition_strategy)
def test_efsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=efsm::EFSM_strategy)
@settings(max_examples=50)
def test_efsm::efsm_instantiation(instance):
    assert isinstance(instance, efsm::EFSM)

@given(instance=efsm::EFSM_strategy)
def test_efsm::efsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=efsm::EFSM_strategy)
def test_efsm::efsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
