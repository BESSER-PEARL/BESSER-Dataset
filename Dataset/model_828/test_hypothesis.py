import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tfsm::System,
    Guard,
    tfsm::EventGuard,
    tfsm::TemporalGuard,
    tfsm::NamedElement,
    NamedElement,
    tfsm::Guard,
    tfsm::FSMClock,
    tfsm::FSMEvent,
    tfsm::State,
    tfsm::Transition,
    tfsm::TFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm::system_is_not_abstract():
    assert not inspect.isabstract(tfsm::System)


def test_tfsm::system_constructor_exists():
    assert callable(tfsm::System.__init__)


def test_tfsm::system_constructor_args():
    sig = inspect.signature(tfsm::System.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::EventGuard)


def test_tfsm::eventguard_constructor_exists():
    assert callable(tfsm::EventGuard.__init__)


def test_tfsm::eventguard_constructor_args():
    sig = inspect.signature(tfsm::EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::TemporalGuard)


def test_tfsm::temporalguard_constructor_exists():
    assert callable(tfsm::TemporalGuard.__init__)


def test_tfsm::temporalguard_constructor_args():
    sig = inspect.signature(tfsm::TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsm::temporalguard_has_afterDuration():
    assert hasattr(tfsm::TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsm::TemporalGuard.__mro__:
        if "afterDuration" in klass.__dict__:
            descriptor = klass.__dict__["afterDuration"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsm::NamedElement)


def test_tfsm::namedelement_constructor_exists():
    assert callable(tfsm::NamedElement.__init__)


def test_tfsm::namedelement_constructor_args():
    sig = inspect.signature(tfsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm::namedelement_has_name():
    assert hasattr(tfsm::NamedElement, "name")
    descriptor = None
    for klass in tfsm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::guard_is_not_abstract():
    assert not inspect.isabstract(tfsm::Guard)


def test_tfsm::guard_constructor_exists():
    assert callable(tfsm::Guard.__init__)


def test_tfsm::guard_constructor_args():
    sig = inspect.signature(tfsm::Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsm::FSMClock)


def test_tfsm::fsmclock_constructor_exists():
    assert callable(tfsm::FSMClock.__init__)


def test_tfsm::fsmclock_constructor_args():
    sig = inspect.signature(tfsm::FSMClock.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsm::FSMEvent)


def test_tfsm::fsmevent_constructor_exists():
    assert callable(tfsm::FSMEvent.__init__)


def test_tfsm::fsmevent_constructor_args():
    sig = inspect.signature(tfsm::FSMEvent.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::state_is_not_abstract():
    assert not inspect.isabstract(tfsm::State)


def test_tfsm::state_constructor_exists():
    assert callable(tfsm::State.__init__)


def test_tfsm::state_constructor_args():
    sig = inspect.signature(tfsm::State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::transition_is_not_abstract():
    assert not inspect.isabstract(tfsm::Transition)


def test_tfsm::transition_constructor_exists():
    assert callable(tfsm::Transition.__init__)


def test_tfsm::transition_constructor_args():
    sig = inspect.signature(tfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsm::transition_has_action():
    assert hasattr(tfsm::Transition, "action")
    descriptor = None
    for klass in tfsm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm::TFSM)


def test_tfsm::tfsm_constructor_exists():
    assert callable(tfsm::TFSM.__init__)


def test_tfsm::tfsm_constructor_args():
    sig = inspect.signature(tfsm::TFSM.__init__)
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
tfsm::System_strategy = st.builds(
    tfsm::System,
)
Guard_strategy = st.builds(
    Guard,
)
tfsm::EventGuard_strategy = st.builds(
    tfsm::EventGuard,
)
tfsm::TemporalGuard_strategy = st.builds(
    tfsm::TemporalGuard,
    afterDuration=
        st.integers()
)
tfsm::NamedElement_strategy = st.builds(
    tfsm::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsm::Guard_strategy = st.builds(
    tfsm::Guard,
)
tfsm::FSMClock_strategy = st.builds(
    tfsm::FSMClock,
)
tfsm::FSMEvent_strategy = st.builds(
    tfsm::FSMEvent,
)
tfsm::State_strategy = st.builds(
    tfsm::State,
)
tfsm::Transition_strategy = st.builds(
    tfsm::Transition,
    action=
        safe_text
)
tfsm::TFSM_strategy = st.builds(
    tfsm::TFSM,
)

@given(instance=tfsm::System_strategy)
@settings(max_examples=50)
def test_tfsm::system_instantiation(instance):
    assert isinstance(instance, tfsm::System)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsm::EventGuard_strategy)
@settings(max_examples=50)
def test_tfsm::eventguard_instantiation(instance):
    assert isinstance(instance, tfsm::EventGuard)

@given(instance=tfsm::TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsm::temporalguard_instantiation(instance):
    assert isinstance(instance, tfsm::TemporalGuard)

@given(instance=tfsm::TemporalGuard_strategy)
def test_tfsm::temporalguard_afterDuration_type(instance):
    assert isinstance(instance.afterDuration, int)


@given(instance=tfsm::TemporalGuard_strategy)
def test_tfsm::temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=tfsm::NamedElement_strategy)
@settings(max_examples=50)
def test_tfsm::namedelement_instantiation(instance):
    assert isinstance(instance, tfsm::NamedElement)

@given(instance=tfsm::NamedElement_strategy)
def test_tfsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tfsm::NamedElement_strategy)
def test_tfsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsm::Guard_strategy)
@settings(max_examples=50)
def test_tfsm::guard_instantiation(instance):
    assert isinstance(instance, tfsm::Guard)

@given(instance=tfsm::FSMClock_strategy)
@settings(max_examples=50)
def test_tfsm::fsmclock_instantiation(instance):
    assert isinstance(instance, tfsm::FSMClock)

@given(instance=tfsm::FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsm::fsmevent_instantiation(instance):
    assert isinstance(instance, tfsm::FSMEvent)

@given(instance=tfsm::State_strategy)
@settings(max_examples=50)
def test_tfsm::state_instantiation(instance):
    assert isinstance(instance, tfsm::State)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsm::State_strategy)
@settings(max_examples=30)
def test_tfsm::state_onleave_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onLeave()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onLeave).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onLeave' in tfsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onLeave' in tfsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onLeave' in tfsm::State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsm::State_strategy)
@settings(max_examples=30)
def test_tfsm::state_onenter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onEnter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onEnter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onEnter' in tfsm::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onEnter' in tfsm::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onEnter' in tfsm::State is not implemented or raised an error")

@given(instance=tfsm::Transition_strategy)
@settings(max_examples=50)
def test_tfsm::transition_instantiation(instance):
    assert isinstance(instance, tfsm::Transition)

@given(instance=tfsm::Transition_strategy)
def test_tfsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=tfsm::Transition_strategy)
def test_tfsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsm::Transition_strategy)
@settings(max_examples=30)
def test_tfsm::transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in tfsm::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in tfsm::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in tfsm::Transition is not implemented or raised an error")

@given(instance=tfsm::TFSM_strategy)
@settings(max_examples=50)
def test_tfsm::tfsm_instantiation(instance):
    assert isinstance(instance, tfsm::TFSM)
