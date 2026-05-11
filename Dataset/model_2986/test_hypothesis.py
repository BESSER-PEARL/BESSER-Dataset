import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    zhu::TriggersSeparated,
    zhu::StatesSeparated,
    zhu::Triggers,
    zhu::State,
    zhu::Transition,
    zhu::Region,
    zhu::States,
    zhu::TopRegion,
    zhu::StateMachine,
    zhu::Transitions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_zhu::triggersseparated_is_not_abstract():
    assert not inspect.isabstract(zhu::TriggersSeparated)


def test_zhu::triggersseparated_constructor_exists():
    assert callable(zhu::TriggersSeparated.__init__)


def test_zhu::triggersseparated_constructor_args():
    sig = inspect.signature(zhu::TriggersSeparated.__init__)
    params = list(sig.parameters.keys())
    assert "followingTriggers" in params, "Missing parameter 'followingTriggers'"
    assert "firstTrigger" in params, "Missing parameter 'firstTrigger'"

def test_zhu::triggersseparated_has_followingTriggers():
    assert hasattr(zhu::TriggersSeparated, "followingTriggers")
    descriptor = None
    for klass in zhu::TriggersSeparated.__mro__:
        if "followingTriggers" in klass.__dict__:
            descriptor = klass.__dict__["followingTriggers"]
            break
    assert isinstance(descriptor, property)

def test_zhu::triggersseparated_has_firstTrigger():
    assert hasattr(zhu::TriggersSeparated, "firstTrigger")
    descriptor = None
    for klass in zhu::TriggersSeparated.__mro__:
        if "firstTrigger" in klass.__dict__:
            descriptor = klass.__dict__["firstTrigger"]
            break
    assert isinstance(descriptor, property)



def test_zhu::statesseparated_is_not_abstract():
    assert not inspect.isabstract(zhu::StatesSeparated)


def test_zhu::statesseparated_constructor_exists():
    assert callable(zhu::StatesSeparated.__init__)


def test_zhu::statesseparated_constructor_args():
    sig = inspect.signature(zhu::StatesSeparated.__init__)
    params = list(sig.parameters.keys())



def test_zhu::triggers_is_not_abstract():
    assert not inspect.isabstract(zhu::Triggers)


def test_zhu::triggers_constructor_exists():
    assert callable(zhu::Triggers.__init__)


def test_zhu::triggers_constructor_args():
    sig = inspect.signature(zhu::Triggers.__init__)
    params = list(sig.parameters.keys())



def test_zhu::state_is_not_abstract():
    assert not inspect.isabstract(zhu::State)


def test_zhu::state_constructor_exists():
    assert callable(zhu::State.__init__)


def test_zhu::state_constructor_args():
    sig = inspect.signature(zhu::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_zhu::state_has_name():
    assert hasattr(zhu::State, "name")
    descriptor = None
    for klass in zhu::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_zhu::transition_is_not_abstract():
    assert not inspect.isabstract(zhu::Transition)


def test_zhu::transition_constructor_exists():
    assert callable(zhu::Transition.__init__)


def test_zhu::transition_constructor_args():
    sig = inspect.signature(zhu::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "behaviour" in params, "Missing parameter 'behaviour'"

def test_zhu::transition_has_guard():
    assert hasattr(zhu::Transition, "guard")
    descriptor = None
    for klass in zhu::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_zhu::transition_has_behaviour():
    assert hasattr(zhu::Transition, "behaviour")
    descriptor = None
    for klass in zhu::Transition.__mro__:
        if "behaviour" in klass.__dict__:
            descriptor = klass.__dict__["behaviour"]
            break
    assert isinstance(descriptor, property)



def test_zhu::region_is_not_abstract():
    assert not inspect.isabstract(zhu::Region)


def test_zhu::region_constructor_exists():
    assert callable(zhu::Region.__init__)


def test_zhu::region_constructor_args():
    sig = inspect.signature(zhu::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_zhu::region_has_name():
    assert hasattr(zhu::Region, "name")
    descriptor = None
    for klass in zhu::Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_zhu::states_is_not_abstract():
    assert not inspect.isabstract(zhu::States)


def test_zhu::states_constructor_exists():
    assert callable(zhu::States.__init__)


def test_zhu::states_constructor_args():
    sig = inspect.signature(zhu::States.__init__)
    params = list(sig.parameters.keys())



def test_zhu::topregion_is_not_abstract():
    assert not inspect.isabstract(zhu::TopRegion)


def test_zhu::topregion_constructor_exists():
    assert callable(zhu::TopRegion.__init__)


def test_zhu::topregion_constructor_args():
    sig = inspect.signature(zhu::TopRegion.__init__)
    params = list(sig.parameters.keys())



def test_zhu::statemachine_is_not_abstract():
    assert not inspect.isabstract(zhu::StateMachine)


def test_zhu::statemachine_constructor_exists():
    assert callable(zhu::StateMachine.__init__)


def test_zhu::statemachine_constructor_args():
    sig = inspect.signature(zhu::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_zhu::transitions_is_not_abstract():
    assert not inspect.isabstract(zhu::Transitions)


def test_zhu::transitions_constructor_exists():
    assert callable(zhu::Transitions.__init__)


def test_zhu::transitions_constructor_args():
    sig = inspect.signature(zhu::Transitions.__init__)
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
zhu::TriggersSeparated_strategy = st.builds(
    zhu::TriggersSeparated,
    followingTriggers=
        safe_text,
    firstTrigger=
        safe_text
)
zhu::StatesSeparated_strategy = st.builds(
    zhu::StatesSeparated,
)
zhu::Triggers_strategy = st.builds(
    zhu::Triggers,
)
zhu::State_strategy = st.builds(
    zhu::State,
    name=
        safe_text
)
zhu::Transition_strategy = st.builds(
    zhu::Transition,
    guard=
        safe_text,
    behaviour=
        safe_text
)
zhu::Region_strategy = st.builds(
    zhu::Region,
    name=
        safe_text
)
zhu::States_strategy = st.builds(
    zhu::States,
)
zhu::TopRegion_strategy = st.builds(
    zhu::TopRegion,
)
zhu::StateMachine_strategy = st.builds(
    zhu::StateMachine,
)
zhu::Transitions_strategy = st.builds(
    zhu::Transitions,
)

@given(instance=zhu::TriggersSeparated_strategy)
@settings(max_examples=50)
def test_zhu::triggersseparated_instantiation(instance):
    assert isinstance(instance, zhu::TriggersSeparated)

@given(instance=zhu::TriggersSeparated_strategy)
def test_zhu::triggersseparated_followingTriggers_type(instance):
    assert isinstance(instance.followingTriggers, str)


@given(instance=zhu::TriggersSeparated_strategy)
def test_zhu::triggersseparated_followingTriggers_setter(instance):
    original = instance.followingTriggers
    instance.followingTriggers = original
    assert instance.followingTriggers == original

@given(instance=zhu::TriggersSeparated_strategy)
def test_zhu::triggersseparated_firstTrigger_type(instance):
    assert isinstance(instance.firstTrigger, str)


@given(instance=zhu::TriggersSeparated_strategy)
def test_zhu::triggersseparated_firstTrigger_setter(instance):
    original = instance.firstTrigger
    instance.firstTrigger = original
    assert instance.firstTrigger == original

@given(instance=zhu::StatesSeparated_strategy)
@settings(max_examples=50)
def test_zhu::statesseparated_instantiation(instance):
    assert isinstance(instance, zhu::StatesSeparated)

@given(instance=zhu::Triggers_strategy)
@settings(max_examples=50)
def test_zhu::triggers_instantiation(instance):
    assert isinstance(instance, zhu::Triggers)

@given(instance=zhu::State_strategy)
@settings(max_examples=50)
def test_zhu::state_instantiation(instance):
    assert isinstance(instance, zhu::State)

@given(instance=zhu::State_strategy)
def test_zhu::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=zhu::State_strategy)
def test_zhu::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=zhu::Transition_strategy)
@settings(max_examples=50)
def test_zhu::transition_instantiation(instance):
    assert isinstance(instance, zhu::Transition)

@given(instance=zhu::Transition_strategy)
def test_zhu::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=zhu::Transition_strategy)
def test_zhu::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=zhu::Transition_strategy)
def test_zhu::transition_behaviour_type(instance):
    assert isinstance(instance.behaviour, str)


@given(instance=zhu::Transition_strategy)
def test_zhu::transition_behaviour_setter(instance):
    original = instance.behaviour
    instance.behaviour = original
    assert instance.behaviour == original

@given(instance=zhu::Region_strategy)
@settings(max_examples=50)
def test_zhu::region_instantiation(instance):
    assert isinstance(instance, zhu::Region)

@given(instance=zhu::Region_strategy)
def test_zhu::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=zhu::Region_strategy)
def test_zhu::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=zhu::States_strategy)
@settings(max_examples=50)
def test_zhu::states_instantiation(instance):
    assert isinstance(instance, zhu::States)

@given(instance=zhu::TopRegion_strategy)
@settings(max_examples=50)
def test_zhu::topregion_instantiation(instance):
    assert isinstance(instance, zhu::TopRegion)

@given(instance=zhu::StateMachine_strategy)
@settings(max_examples=50)
def test_zhu::statemachine_instantiation(instance):
    assert isinstance(instance, zhu::StateMachine)

@given(instance=zhu::Transitions_strategy)
@settings(max_examples=50)
def test_zhu::transitions_instantiation(instance):
    assert isinstance(instance, zhu::Transitions)
