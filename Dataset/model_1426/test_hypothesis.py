import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModelElement,
    statechart::AbstractState,
    statechart::Transition,
    statechart::ModelElement,
    statechart::StateMachine,
    AbstractState,
    statechart::FinalState,
    statechart::SimpleState,
    statechart::InitialState,
    statechart::CompositeState,
    statechart::Action,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_statechart::abstractstate_is_not_abstract():
    assert not inspect.isabstract(statechart::AbstractState)


def test_statechart::abstractstate_constructor_exists():
    assert callable(statechart::AbstractState.__init__)


def test_statechart::abstractstate_constructor_args():
    sig = inspect.signature(statechart::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::transition_is_not_abstract():
    assert not inspect.isabstract(statechart::Transition)


def test_statechart::transition_constructor_exists():
    assert callable(statechart::Transition.__init__)


def test_statechart::transition_constructor_args():
    sig = inspect.signature(statechart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "event" in params, "Missing parameter 'event'"

def test_statechart::transition_has_guard():
    assert hasattr(statechart::Transition, "guard")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transition_has_event():
    assert hasattr(statechart::Transition, "event")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_statechart::modelelement_is_not_abstract():
    assert not inspect.isabstract(statechart::ModelElement)


def test_statechart::modelelement_constructor_exists():
    assert callable(statechart::ModelElement.__init__)


def test_statechart::modelelement_constructor_args():
    sig = inspect.signature(statechart::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::modelelement_has_name():
    assert hasattr(statechart::ModelElement, "name")
    descriptor = None
    for klass in statechart::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart::statemachine_is_not_abstract():
    assert not inspect.isabstract(statechart::StateMachine)


def test_statechart::statemachine_constructor_exists():
    assert callable(statechart::StateMachine.__init__)


def test_statechart::statemachine_constructor_args():
    sig = inspect.signature(statechart::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::finalstate_is_not_abstract():
    assert not inspect.isabstract(statechart::FinalState)


def test_statechart::finalstate_constructor_exists():
    assert callable(statechart::FinalState.__init__)


def test_statechart::finalstate_constructor_args():
    sig = inspect.signature(statechart::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::simplestate_is_not_abstract():
    assert not inspect.isabstract(statechart::SimpleState)


def test_statechart::simplestate_constructor_exists():
    assert callable(statechart::SimpleState.__init__)


def test_statechart::simplestate_constructor_args():
    sig = inspect.signature(statechart::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::initialstate_is_not_abstract():
    assert not inspect.isabstract(statechart::InitialState)


def test_statechart::initialstate_constructor_exists():
    assert callable(statechart::InitialState.__init__)


def test_statechart::initialstate_constructor_args():
    sig = inspect.signature(statechart::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::compositestate_is_not_abstract():
    assert not inspect.isabstract(statechart::CompositeState)


def test_statechart::compositestate_constructor_exists():
    assert callable(statechart::CompositeState.__init__)


def test_statechart::compositestate_constructor_args():
    sig = inspect.signature(statechart::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::action_is_not_abstract():
    assert not inspect.isabstract(statechart::Action)


def test_statechart::action_constructor_exists():
    assert callable(statechart::Action.__init__)


def test_statechart::action_constructor_args():
    sig = inspect.signature(statechart::Action.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statechart::action_has_kind():
    assert hasattr(statechart::Action, "kind")
    descriptor = None
    for klass in statechart::Action.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

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
ModelElement_strategy = st.builds(
    ModelElement,
)
statechart::AbstractState_strategy = st.builds(
    statechart::AbstractState,
)
statechart::Transition_strategy = st.builds(
    statechart::Transition,
    guard=
        safe_text,
    event=
        safe_text
)
statechart::ModelElement_strategy = st.builds(
    statechart::ModelElement,
    name=
        safe_text
)
statechart::StateMachine_strategy = st.builds(
    statechart::StateMachine,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statechart::FinalState_strategy = st.builds(
    statechart::FinalState,
)
statechart::SimpleState_strategy = st.builds(
    statechart::SimpleState,
)
statechart::InitialState_strategy = st.builds(
    statechart::InitialState,
)
statechart::CompositeState_strategy = st.builds(
    statechart::CompositeState,
)
statechart::Action_strategy = st.builds(
    statechart::Action,
    kind=
        safe_text
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=statechart::AbstractState_strategy)
@settings(max_examples=50)
def test_statechart::abstractstate_instantiation(instance):
    assert isinstance(instance, statechart::AbstractState)

@given(instance=statechart::Transition_strategy)
@settings(max_examples=50)
def test_statechart::transition_instantiation(instance):
    assert isinstance(instance, statechart::Transition)

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=statechart::ModelElement_strategy)
@settings(max_examples=50)
def test_statechart::modelelement_instantiation(instance):
    assert isinstance(instance, statechart::ModelElement)

@given(instance=statechart::ModelElement_strategy)
def test_statechart::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::ModelElement_strategy)
def test_statechart::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::StateMachine_strategy)
@settings(max_examples=50)
def test_statechart::statemachine_instantiation(instance):
    assert isinstance(instance, statechart::StateMachine)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statechart::FinalState_strategy)
@settings(max_examples=50)
def test_statechart::finalstate_instantiation(instance):
    assert isinstance(instance, statechart::FinalState)

@given(instance=statechart::SimpleState_strategy)
@settings(max_examples=50)
def test_statechart::simplestate_instantiation(instance):
    assert isinstance(instance, statechart::SimpleState)

@given(instance=statechart::InitialState_strategy)
@settings(max_examples=50)
def test_statechart::initialstate_instantiation(instance):
    assert isinstance(instance, statechart::InitialState)

@given(instance=statechart::CompositeState_strategy)
@settings(max_examples=50)
def test_statechart::compositestate_instantiation(instance):
    assert isinstance(instance, statechart::CompositeState)

@given(instance=statechart::Action_strategy)
@settings(max_examples=50)
def test_statechart::action_instantiation(instance):
    assert isinstance(instance, statechart::Action)

@given(instance=statechart::Action_strategy)
def test_statechart::action_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=statechart::Action_strategy)
def test_statechart::action_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
