import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smDsl_CommandsSection,
    smDsl_EventsSection,
    smDsl_Model,
    smDsl_EventHandlingDescription,
    smDsl_Command,
    smDsl_Event,
    smDsl_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smdsl_commandssection_is_not_abstract():
    assert not inspect.isabstract(smDsl_CommandsSection)


def test_smdsl_commandssection_constructor_exists():
    assert callable(smDsl_CommandsSection.__init__)


def test_smdsl_commandssection_constructor_args():
    sig = inspect.signature(smDsl_CommandsSection.__init__)
    params = list(sig.parameters.keys())



def test_smdsl_eventssection_is_not_abstract():
    assert not inspect.isabstract(smDsl_EventsSection)


def test_smdsl_eventssection_constructor_exists():
    assert callable(smDsl_EventsSection.__init__)


def test_smdsl_eventssection_constructor_args():
    sig = inspect.signature(smDsl_EventsSection.__init__)
    params = list(sig.parameters.keys())



def test_smdsl_model_is_not_abstract():
    assert not inspect.isabstract(smDsl_Model)


def test_smdsl_model_constructor_exists():
    assert callable(smDsl_Model.__init__)


def test_smdsl_model_constructor_args():
    sig = inspect.signature(smDsl_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl_model_has_name():
    assert hasattr(smDsl_Model, "name")
    descriptor = None
    for klass in smDsl_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl_eventhandlingdescription_is_not_abstract():
    assert not inspect.isabstract(smDsl_EventHandlingDescription)


def test_smdsl_eventhandlingdescription_constructor_exists():
    assert callable(smDsl_EventHandlingDescription.__init__)


def test_smdsl_eventhandlingdescription_constructor_args():
    sig = inspect.signature(smDsl_EventHandlingDescription.__init__)
    params = list(sig.parameters.keys())



def test_smdsl_command_is_not_abstract():
    assert not inspect.isabstract(smDsl_Command)


def test_smdsl_command_constructor_exists():
    assert callable(smDsl_Command.__init__)


def test_smdsl_command_constructor_args():
    sig = inspect.signature(smDsl_Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl_command_has_name():
    assert hasattr(smDsl_Command, "name")
    descriptor = None
    for klass in smDsl_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl_event_is_not_abstract():
    assert not inspect.isabstract(smDsl_Event)


def test_smdsl_event_constructor_exists():
    assert callable(smDsl_Event.__init__)


def test_smdsl_event_constructor_args():
    sig = inspect.signature(smDsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl_event_has_name():
    assert hasattr(smDsl_Event, "name")
    descriptor = None
    for klass in smDsl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl_state_is_not_abstract():
    assert not inspect.isabstract(smDsl_State)


def test_smdsl_state_constructor_exists():
    assert callable(smDsl_State.__init__)


def test_smdsl_state_constructor_args():
    sig = inspect.signature(smDsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_smdsl_state_has_name():
    assert hasattr(smDsl_State, "name")
    descriptor = None
    for klass in smDsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smdsl_state_has_initial():
    assert hasattr(smDsl_State, "initial")
    descriptor = None
    for klass in smDsl_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
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
smDsl_CommandsSection_strategy = st.builds(
    smDsl_CommandsSection,
)
smDsl_EventsSection_strategy = st.builds(
    smDsl_EventsSection,
)
smDsl_Model_strategy = st.builds(
    smDsl_Model,
    name=
        safe_text
)
smDsl_EventHandlingDescription_strategy = st.builds(
    smDsl_EventHandlingDescription,
)
smDsl_Command_strategy = st.builds(
    smDsl_Command,
    name=
        safe_text
)
smDsl_Event_strategy = st.builds(
    smDsl_Event,
    name=
        safe_text
)
smDsl_State_strategy = st.builds(
    smDsl_State,
    name=
        safe_text,
    initial=
        st.booleans()
)

@given(instance=smDsl_CommandsSection_strategy)
@settings(max_examples=50)
def test_smdsl_commandssection_instantiation(instance):
    assert isinstance(instance, smDsl_CommandsSection)

@given(instance=smDsl_EventsSection_strategy)
@settings(max_examples=50)
def test_smdsl_eventssection_instantiation(instance):
    assert isinstance(instance, smDsl_EventsSection)

@given(instance=smDsl_Model_strategy)
@settings(max_examples=50)
def test_smdsl_model_instantiation(instance):
    assert isinstance(instance, smDsl_Model)



@given(instance=smDsl_Model_strategy)
def test_smdsl_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl_EventHandlingDescription_strategy)
@settings(max_examples=50)
def test_smdsl_eventhandlingdescription_instantiation(instance):
    assert isinstance(instance, smDsl_EventHandlingDescription)

@given(instance=smDsl_Command_strategy)
@settings(max_examples=50)
def test_smdsl_command_instantiation(instance):
    assert isinstance(instance, smDsl_Command)



@given(instance=smDsl_Command_strategy)
def test_smdsl_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl_Event_strategy)
@settings(max_examples=50)
def test_smdsl_event_instantiation(instance):
    assert isinstance(instance, smDsl_Event)



@given(instance=smDsl_Event_strategy)
def test_smdsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl_State_strategy)
@settings(max_examples=50)
def test_smdsl_state_instantiation(instance):
    assert isinstance(instance, smDsl_State)



@given(instance=smDsl_State_strategy)
def test_smdsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smDsl_State_strategy)
def test_smdsl_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original
