import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::State,
    fsm::Machine,
    fsm::Language,
    fsm::Constraint,
    fsm::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_fsm::transition_has_event():
    assert hasattr(fsm::Transition, "event")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_final():
    assert hasattr(fsm::State, "final")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_initial():
    assert hasattr(fsm::State, "initial")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_fsm::machine_is_not_abstract():
    assert not inspect.isabstract(fsm::Machine)


def test_fsm::machine_constructor_exists():
    assert callable(fsm::Machine.__init__)


def test_fsm::machine_constructor_args():
    sig = inspect.signature(fsm::Machine.__init__)
    params = list(sig.parameters.keys())



def test_fsm::language_is_not_abstract():
    assert not inspect.isabstract(fsm::Language)


def test_fsm::language_constructor_exists():
    assert callable(fsm::Language.__init__)


def test_fsm::language_constructor_args():
    sig = inspect.signature(fsm::Language.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"

def test_fsm::language_has_name():
    assert hasattr(fsm::Language, "name")
    descriptor = None
    for klass in fsm::Language.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::language_has_target():
    assert hasattr(fsm::Language, "target")
    descriptor = None
    for klass in fsm::Language.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_fsm::constraint_is_not_abstract():
    assert not inspect.isabstract(fsm::Constraint)


def test_fsm::constraint_constructor_exists():
    assert callable(fsm::Constraint.__init__)


def test_fsm::constraint_constructor_args():
    sig = inspect.signature(fsm::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "true" in params, "Missing parameter 'true'"

def test_fsm::constraint_has_name():
    assert hasattr(fsm::Constraint, "name")
    descriptor = None
    for klass in fsm::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::constraint_has_true():
    assert hasattr(fsm::Constraint, "true")
    descriptor = None
    for klass in fsm::Constraint.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_fsm::model_is_not_abstract():
    assert not inspect.isabstract(fsm::Model)


def test_fsm::model_constructor_exists():
    assert callable(fsm::Model.__init__)


def test_fsm::model_constructor_args():
    sig = inspect.signature(fsm::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::model_has_name():
    assert hasattr(fsm::Model, "name")
    descriptor = None
    for klass in fsm::Model.__mro__:
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    event=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text,
    final=
        st.booleans(),
    initial=
        st.booleans()
)
fsm::Machine_strategy = st.builds(
    fsm::Machine,
)
fsm::Language_strategy = st.builds(
    fsm::Language,
    name=
        safe_text,
    target=
        safe_text
)
fsm::Constraint_strategy = st.builds(
    fsm::Constraint,
    name=
        safe_text,
    true=
        st.booleans()
)
fsm::Model_strategy = st.builds(
    fsm::Model,
    name=
        safe_text
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::State_strategy)
def test_fsm::state_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=fsm::State_strategy)
def test_fsm::state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=fsm::State_strategy)
def test_fsm::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=fsm::State_strategy)
def test_fsm::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=fsm::Machine_strategy)
@settings(max_examples=50)
def test_fsm::machine_instantiation(instance):
    assert isinstance(instance, fsm::Machine)

@given(instance=fsm::Language_strategy)
@settings(max_examples=50)
def test_fsm::language_instantiation(instance):
    assert isinstance(instance, fsm::Language)

@given(instance=fsm::Language_strategy)
def test_fsm::language_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Language_strategy)
def test_fsm::language_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Language_strategy)
def test_fsm::language_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=fsm::Language_strategy)
def test_fsm::language_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=50)
def test_fsm::constraint_instantiation(instance):
    assert isinstance(instance, fsm::Constraint)

@given(instance=fsm::Constraint_strategy)
def test_fsm::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Constraint_strategy)
def test_fsm::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Constraint_strategy)
def test_fsm::constraint_true_type(instance):
    assert isinstance(instance.true, bool)


@given(instance=fsm::Constraint_strategy)
def test_fsm::constraint_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=fsm::Model_strategy)
@settings(max_examples=50)
def test_fsm::model_instantiation(instance):
    assert isinstance(instance, fsm::Model)

@given(instance=fsm::Model_strategy)
def test_fsm::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Model_strategy)
def test_fsm::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
