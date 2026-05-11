import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smDsl::CommandsSection,
    smDsl::EventsSection,
    smDsl::Model,
    smDsl::EventHandlingDescription,
    smDsl::Command,
    smDsl::Event,
    smDsl::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smdsl::commandssection_is_not_abstract():
    assert not inspect.isabstract(smDsl::CommandsSection)


def test_smdsl::commandssection_constructor_exists():
    assert callable(smDsl::CommandsSection.__init__)


def test_smdsl::commandssection_constructor_args():
    sig = inspect.signature(smDsl::CommandsSection.__init__)
    params = list(sig.parameters.keys())



def test_smdsl::eventssection_is_not_abstract():
    assert not inspect.isabstract(smDsl::EventsSection)


def test_smdsl::eventssection_constructor_exists():
    assert callable(smDsl::EventsSection.__init__)


def test_smdsl::eventssection_constructor_args():
    sig = inspect.signature(smDsl::EventsSection.__init__)
    params = list(sig.parameters.keys())



def test_smdsl::model_is_not_abstract():
    assert not inspect.isabstract(smDsl::Model)


def test_smdsl::model_constructor_exists():
    assert callable(smDsl::Model.__init__)


def test_smdsl::model_constructor_args():
    sig = inspect.signature(smDsl::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl::model_has_name():
    assert hasattr(smDsl::Model, "name")
    descriptor = None
    for klass in smDsl::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl::eventhandlingdescription_is_not_abstract():
    assert not inspect.isabstract(smDsl::EventHandlingDescription)


def test_smdsl::eventhandlingdescription_constructor_exists():
    assert callable(smDsl::EventHandlingDescription.__init__)


def test_smdsl::eventhandlingdescription_constructor_args():
    sig = inspect.signature(smDsl::EventHandlingDescription.__init__)
    params = list(sig.parameters.keys())



def test_smdsl::command_is_not_abstract():
    assert not inspect.isabstract(smDsl::Command)


def test_smdsl::command_constructor_exists():
    assert callable(smDsl::Command.__init__)


def test_smdsl::command_constructor_args():
    sig = inspect.signature(smDsl::Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl::command_has_name():
    assert hasattr(smDsl::Command, "name")
    descriptor = None
    for klass in smDsl::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl::event_is_not_abstract():
    assert not inspect.isabstract(smDsl::Event)


def test_smdsl::event_constructor_exists():
    assert callable(smDsl::Event.__init__)


def test_smdsl::event_constructor_args():
    sig = inspect.signature(smDsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl::event_has_name():
    assert hasattr(smDsl::Event, "name")
    descriptor = None
    for klass in smDsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smdsl::state_is_not_abstract():
    assert not inspect.isabstract(smDsl::State)


def test_smdsl::state_constructor_exists():
    assert callable(smDsl::State.__init__)


def test_smdsl::state_constructor_args():
    sig = inspect.signature(smDsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_smdsl::state_has_initial():
    assert hasattr(smDsl::State, "initial")
    descriptor = None
    for klass in smDsl::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_smdsl::state_has_name():
    assert hasattr(smDsl::State, "name")
    descriptor = None
    for klass in smDsl::State.__mro__:
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
smDsl::CommandsSection_strategy = st.builds(
    smDsl::CommandsSection,
)
smDsl::EventsSection_strategy = st.builds(
    smDsl::EventsSection,
)
smDsl::Model_strategy = st.builds(
    smDsl::Model,
    name=
        safe_text
)
smDsl::EventHandlingDescription_strategy = st.builds(
    smDsl::EventHandlingDescription,
)
smDsl::Command_strategy = st.builds(
    smDsl::Command,
    name=
        safe_text
)
smDsl::Event_strategy = st.builds(
    smDsl::Event,
    name=
        safe_text
)
smDsl::State_strategy = st.builds(
    smDsl::State,
    initial=
        st.booleans(),
    name=
        safe_text
)

@given(instance=smDsl::CommandsSection_strategy)
@settings(max_examples=50)
def test_smdsl::commandssection_instantiation(instance):
    assert isinstance(instance, smDsl::CommandsSection)

@given(instance=smDsl::EventsSection_strategy)
@settings(max_examples=50)
def test_smdsl::eventssection_instantiation(instance):
    assert isinstance(instance, smDsl::EventsSection)

@given(instance=smDsl::Model_strategy)
@settings(max_examples=50)
def test_smdsl::model_instantiation(instance):
    assert isinstance(instance, smDsl::Model)

@given(instance=smDsl::Model_strategy)
def test_smdsl::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smDsl::Model_strategy)
def test_smdsl::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl::EventHandlingDescription_strategy)
@settings(max_examples=50)
def test_smdsl::eventhandlingdescription_instantiation(instance):
    assert isinstance(instance, smDsl::EventHandlingDescription)

@given(instance=smDsl::Command_strategy)
@settings(max_examples=50)
def test_smdsl::command_instantiation(instance):
    assert isinstance(instance, smDsl::Command)

@given(instance=smDsl::Command_strategy)
def test_smdsl::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smDsl::Command_strategy)
def test_smdsl::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl::Event_strategy)
@settings(max_examples=50)
def test_smdsl::event_instantiation(instance):
    assert isinstance(instance, smDsl::Event)

@given(instance=smDsl::Event_strategy)
def test_smdsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smDsl::Event_strategy)
def test_smdsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smDsl::State_strategy)
@settings(max_examples=50)
def test_smdsl::state_instantiation(instance):
    assert isinstance(instance, smDsl::State)

@given(instance=smDsl::State_strategy)
def test_smdsl::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=smDsl::State_strategy)
def test_smdsl::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=smDsl::State_strategy)
def test_smdsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smDsl::State_strategy)
def test_smdsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
