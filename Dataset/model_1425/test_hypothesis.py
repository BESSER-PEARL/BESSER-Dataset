import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractState,
    errorstm::SimpleState,
    errorstm::InitialState,
    errorstm::FinalState,
    errorstm::CompositeState,
    errorstm::Action,
    errorstm::AbstractState,
    errorstm::Transition,
    errorstm::StateMachine,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm::simplestate_is_not_abstract():
    assert not inspect.isabstract(errorstm::SimpleState)


def test_errorstm::simplestate_constructor_exists():
    assert callable(errorstm::SimpleState.__init__)


def test_errorstm::simplestate_constructor_args():
    sig = inspect.signature(errorstm::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm::initialstate_is_not_abstract():
    assert not inspect.isabstract(errorstm::InitialState)


def test_errorstm::initialstate_constructor_exists():
    assert callable(errorstm::InitialState.__init__)


def test_errorstm::initialstate_constructor_args():
    sig = inspect.signature(errorstm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm::finalstate_is_not_abstract():
    assert not inspect.isabstract(errorstm::FinalState)


def test_errorstm::finalstate_constructor_exists():
    assert callable(errorstm::FinalState.__init__)


def test_errorstm::finalstate_constructor_args():
    sig = inspect.signature(errorstm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm::compositestate_is_not_abstract():
    assert not inspect.isabstract(errorstm::CompositeState)


def test_errorstm::compositestate_constructor_exists():
    assert callable(errorstm::CompositeState.__init__)


def test_errorstm::compositestate_constructor_args():
    sig = inspect.signature(errorstm::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm::action_is_not_abstract():
    assert not inspect.isabstract(errorstm::Action)


def test_errorstm::action_constructor_exists():
    assert callable(errorstm::Action.__init__)


def test_errorstm::action_constructor_args():
    sig = inspect.signature(errorstm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_errorstm::action_has_kind():
    assert hasattr(errorstm::Action, "kind")
    descriptor = None
    for klass in errorstm::Action.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_errorstm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(errorstm::AbstractState)


def test_errorstm::abstractstate_constructor_exists():
    assert callable(errorstm::AbstractState.__init__)


def test_errorstm::abstractstate_constructor_args():
    sig = inspect.signature(errorstm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_errorstm::abstractstate_has_name():
    assert hasattr(errorstm::AbstractState, "name")
    descriptor = None
    for klass in errorstm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_errorstm::transition_is_not_abstract():
    assert not inspect.isabstract(errorstm::Transition)


def test_errorstm::transition_constructor_exists():
    assert callable(errorstm::Transition.__init__)


def test_errorstm::transition_constructor_args():
    sig = inspect.signature(errorstm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "event" in params, "Missing parameter 'event'"
    assert "name" in params, "Missing parameter 'name'"

def test_errorstm::transition_has_guard():
    assert hasattr(errorstm::Transition, "guard")
    descriptor = None
    for klass in errorstm::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_errorstm::transition_has_event():
    assert hasattr(errorstm::Transition, "event")
    descriptor = None
    for klass in errorstm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_errorstm::transition_has_name():
    assert hasattr(errorstm::Transition, "name")
    descriptor = None
    for klass in errorstm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_errorstm::statemachine_is_not_abstract():
    assert not inspect.isabstract(errorstm::StateMachine)


def test_errorstm::statemachine_constructor_exists():
    assert callable(errorstm::StateMachine.__init__)


def test_errorstm::statemachine_constructor_args():
    sig = inspect.signature(errorstm::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "EXIT",
        "ENTRY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"


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
AbstractState_strategy = st.builds(
    AbstractState,
)
errorstm::SimpleState_strategy = st.builds(
    errorstm::SimpleState,
)
errorstm::InitialState_strategy = st.builds(
    errorstm::InitialState,
)
errorstm::FinalState_strategy = st.builds(
    errorstm::FinalState,
)
errorstm::CompositeState_strategy = st.builds(
    errorstm::CompositeState,
)
errorstm::Action_strategy = st.builds(
    errorstm::Action,
    kind=
        safe_text
)
errorstm::AbstractState_strategy = st.builds(
    errorstm::AbstractState,
    name=
        safe_text
)
errorstm::Transition_strategy = st.builds(
    errorstm::Transition,
    guard=
        safe_text,
    event=
        safe_text,
    name=
        safe_text
)
errorstm::StateMachine_strategy = st.builds(
    errorstm::StateMachine,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=errorstm::SimpleState_strategy)
@settings(max_examples=50)
def test_errorstm::simplestate_instantiation(instance):
    assert isinstance(instance, errorstm::SimpleState)

@given(instance=errorstm::InitialState_strategy)
@settings(max_examples=50)
def test_errorstm::initialstate_instantiation(instance):
    assert isinstance(instance, errorstm::InitialState)

@given(instance=errorstm::FinalState_strategy)
@settings(max_examples=50)
def test_errorstm::finalstate_instantiation(instance):
    assert isinstance(instance, errorstm::FinalState)

@given(instance=errorstm::CompositeState_strategy)
@settings(max_examples=50)
def test_errorstm::compositestate_instantiation(instance):
    assert isinstance(instance, errorstm::CompositeState)

@given(instance=errorstm::Action_strategy)
@settings(max_examples=50)
def test_errorstm::action_instantiation(instance):
    assert isinstance(instance, errorstm::Action)

@given(instance=errorstm::Action_strategy)
def test_errorstm::action_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=errorstm::Action_strategy)
def test_errorstm::action_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=errorstm::AbstractState_strategy)
@settings(max_examples=50)
def test_errorstm::abstractstate_instantiation(instance):
    assert isinstance(instance, errorstm::AbstractState)

@given(instance=errorstm::AbstractState_strategy)
def test_errorstm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=errorstm::AbstractState_strategy)
def test_errorstm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=errorstm::Transition_strategy)
@settings(max_examples=50)
def test_errorstm::transition_instantiation(instance):
    assert isinstance(instance, errorstm::Transition)

@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=errorstm::Transition_strategy)
def test_errorstm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=errorstm::StateMachine_strategy)
@settings(max_examples=50)
def test_errorstm::statemachine_instantiation(instance):
    assert isinstance(instance, errorstm::StateMachine)
