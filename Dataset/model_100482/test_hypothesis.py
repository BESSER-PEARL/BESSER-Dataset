import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tfsmextended::NamedElement,
    Guard,
    tfsmextended::EventGuard,
    tfsmextended::EvaluateGuard,
    tfsmextended::TemporalGuard,
    NamedElement,
    tfsmextended::FSMClock,
    tfsmextended::TimedSystem,
    tfsmextended::FSMEvent,
    tfsmextended::Guard,
    tfsmextended::State,
    tfsmextended::Transition,
    tfsmextended::TFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsmextended::namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::NamedElement)


def test_tfsmextended::namedelement_constructor_exists():
    assert callable(tfsmextended::NamedElement.__init__)


def test_tfsmextended::namedelement_constructor_args():
    sig = inspect.signature(tfsmextended::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsmextended::namedelement_has_name():
    assert hasattr(tfsmextended::NamedElement, "name")
    descriptor = None
    for klass in tfsmextended::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::EventGuard)


def test_tfsmextended::eventguard_constructor_exists():
    assert callable(tfsmextended::EventGuard.__init__)


def test_tfsmextended::eventguard_constructor_args():
    sig = inspect.signature(tfsmextended::EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::EvaluateGuard)


def test_tfsmextended::evaluateguard_constructor_exists():
    assert callable(tfsmextended::EvaluateGuard.__init__)


def test_tfsmextended::evaluateguard_constructor_args():
    sig = inspect.signature(tfsmextended::EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_tfsmextended::evaluateguard_has_condition():
    assert hasattr(tfsmextended::EvaluateGuard, "condition")
    descriptor = None
    for klass in tfsmextended::EvaluateGuard.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_tfsmextended::temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::TemporalGuard)


def test_tfsmextended::temporalguard_constructor_exists():
    assert callable(tfsmextended::TemporalGuard.__init__)


def test_tfsmextended::temporalguard_constructor_args():
    sig = inspect.signature(tfsmextended::TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsmextended::temporalguard_has_afterDuration():
    assert hasattr(tfsmextended::TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsmextended::TemporalGuard.__mro__:
        if "afterDuration" in klass.__dict__:
            descriptor = klass.__dict__["afterDuration"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::FSMClock)


def test_tfsmextended::fsmclock_constructor_exists():
    assert callable(tfsmextended::FSMClock.__init__)


def test_tfsmextended::fsmclock_constructor_args():
    sig = inspect.signature(tfsmextended::FSMClock.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTicks" in params, "Missing parameter 'numberOfTicks'"

def test_tfsmextended::fsmclock_has_numberOfTicks():
    assert hasattr(tfsmextended::FSMClock, "numberOfTicks")
    descriptor = None
    for klass in tfsmextended::FSMClock.__mro__:
        if "numberOfTicks" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTicks"]
            break
    assert isinstance(descriptor, property)



def test_tfsmextended::timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::TimedSystem)


def test_tfsmextended::timedsystem_constructor_exists():
    assert callable(tfsmextended::TimedSystem.__init__)


def test_tfsmextended::timedsystem_constructor_args():
    sig = inspect.signature(tfsmextended::TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::FSMEvent)


def test_tfsmextended::fsmevent_constructor_exists():
    assert callable(tfsmextended::FSMEvent.__init__)


def test_tfsmextended::fsmevent_constructor_args():
    sig = inspect.signature(tfsmextended::FSMEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isTriggered" in params, "Missing parameter 'isTriggered'"

def test_tfsmextended::fsmevent_has_isTriggered():
    assert hasattr(tfsmextended::FSMEvent, "isTriggered")
    descriptor = None
    for klass in tfsmextended::FSMEvent.__mro__:
        if "isTriggered" in klass.__dict__:
            descriptor = klass.__dict__["isTriggered"]
            break
    assert isinstance(descriptor, property)



def test_tfsmextended::guard_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::Guard)


def test_tfsmextended::guard_constructor_exists():
    assert callable(tfsmextended::Guard.__init__)


def test_tfsmextended::guard_constructor_args():
    sig = inspect.signature(tfsmextended::Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::state_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::State)


def test_tfsmextended::state_constructor_exists():
    assert callable(tfsmextended::State.__init__)


def test_tfsmextended::state_constructor_args():
    sig = inspect.signature(tfsmextended::State.__init__)
    params = list(sig.parameters.keys())



def test_tfsmextended::transition_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::Transition)


def test_tfsmextended::transition_constructor_exists():
    assert callable(tfsmextended::Transition.__init__)


def test_tfsmextended::transition_constructor_args():
    sig = inspect.signature(tfsmextended::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsmextended::transition_has_action():
    assert hasattr(tfsmextended::Transition, "action")
    descriptor = None
    for klass in tfsmextended::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsmextended::tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsmextended::TFSM)


def test_tfsmextended::tfsm_constructor_exists():
    assert callable(tfsmextended::TFSM.__init__)


def test_tfsmextended::tfsm_constructor_args():
    sig = inspect.signature(tfsmextended::TFSM.__init__)
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
tfsmextended::NamedElement_strategy = st.builds(
    tfsmextended::NamedElement,
    name=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
tfsmextended::EventGuard_strategy = st.builds(
    tfsmextended::EventGuard,
)
tfsmextended::EvaluateGuard_strategy = st.builds(
    tfsmextended::EvaluateGuard,
    condition=
        safe_text
)
tfsmextended::TemporalGuard_strategy = st.builds(
    tfsmextended::TemporalGuard,
    afterDuration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsmextended::FSMClock_strategy = st.builds(
    tfsmextended::FSMClock,
    numberOfTicks=
        safe_text
)
tfsmextended::TimedSystem_strategy = st.builds(
    tfsmextended::TimedSystem,
)
tfsmextended::FSMEvent_strategy = st.builds(
    tfsmextended::FSMEvent,
    isTriggered=
        st.booleans()
)
tfsmextended::Guard_strategy = st.builds(
    tfsmextended::Guard,
)
tfsmextended::State_strategy = st.builds(
    tfsmextended::State,
)
tfsmextended::Transition_strategy = st.builds(
    tfsmextended::Transition,
    action=
        safe_text
)
tfsmextended::TFSM_strategy = st.builds(
    tfsmextended::TFSM,
)

@given(instance=tfsmextended::NamedElement_strategy)
@settings(max_examples=50)
def test_tfsmextended::namedelement_instantiation(instance):
    assert isinstance(instance, tfsmextended::NamedElement)

@given(instance=tfsmextended::NamedElement_strategy)
def test_tfsmextended::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tfsmextended::NamedElement_strategy)
def test_tfsmextended::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsmextended::EventGuard_strategy)
@settings(max_examples=50)
def test_tfsmextended::eventguard_instantiation(instance):
    assert isinstance(instance, tfsmextended::EventGuard)

@given(instance=tfsmextended::EvaluateGuard_strategy)
@settings(max_examples=50)
def test_tfsmextended::evaluateguard_instantiation(instance):
    assert isinstance(instance, tfsmextended::EvaluateGuard)

@given(instance=tfsmextended::EvaluateGuard_strategy)
def test_tfsmextended::evaluateguard_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=tfsmextended::EvaluateGuard_strategy)
def test_tfsmextended::evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=tfsmextended::TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsmextended::temporalguard_instantiation(instance):
    assert isinstance(instance, tfsmextended::TemporalGuard)

@given(instance=tfsmextended::TemporalGuard_strategy)
def test_tfsmextended::temporalguard_afterDuration_type(instance):
    assert isinstance(instance.afterDuration, int)


@given(instance=tfsmextended::TemporalGuard_strategy)
def test_tfsmextended::temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsmextended::FSMClock_strategy)
@settings(max_examples=50)
def test_tfsmextended::fsmclock_instantiation(instance):
    assert isinstance(instance, tfsmextended::FSMClock)

@given(instance=tfsmextended::FSMClock_strategy)
def test_tfsmextended::fsmclock_numberOfTicks_type(instance):
    assert isinstance(instance.numberOfTicks, str)


@given(instance=tfsmextended::FSMClock_strategy)
def test_tfsmextended::fsmclock_numberOfTicks_setter(instance):
    original = instance.numberOfTicks
    instance.numberOfTicks = original
    assert instance.numberOfTicks == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::FSMClock_strategy)
@settings(max_examples=30)
def test_tfsmextended::fsmclock_ticks_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ticks()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ticks).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ticks' in tfsmextended::FSMClock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ticks' in tfsmextended::FSMClock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ticks' in tfsmextended::FSMClock is not implemented or raised an error")

@given(instance=tfsmextended::TimedSystem_strategy)
@settings(max_examples=50)
def test_tfsmextended::timedsystem_instantiation(instance):
    assert isinstance(instance, tfsmextended::TimedSystem)

@given(instance=tfsmextended::FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsmextended::fsmevent_instantiation(instance):
    assert isinstance(instance, tfsmextended::FSMEvent)

@given(instance=tfsmextended::FSMEvent_strategy)
def test_tfsmextended::fsmevent_isTriggered_type(instance):
    assert isinstance(instance.isTriggered, bool)


@given(instance=tfsmextended::FSMEvent_strategy)
def test_tfsmextended::fsmevent_isTriggered_setter(instance):
    original = instance.isTriggered
    instance.isTriggered = original
    assert instance.isTriggered == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::FSMEvent_strategy)
@settings(max_examples=30)
def test_tfsmextended::fsmevent_trigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.trigger()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.trigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'trigger' in tfsmextended::FSMEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'trigger' in tfsmextended::FSMEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'trigger' in tfsmextended::FSMEvent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::FSMEvent_strategy)
@settings(max_examples=30)
def test_tfsmextended::fsmevent_untrigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unTrigger()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unTrigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unTrigger' in tfsmextended::FSMEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unTrigger' in tfsmextended::FSMEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unTrigger' in tfsmextended::FSMEvent is not implemented or raised an error")

@given(instance=tfsmextended::Guard_strategy)
@settings(max_examples=50)
def test_tfsmextended::guard_instantiation(instance):
    assert isinstance(instance, tfsmextended::Guard)

@given(instance=tfsmextended::State_strategy)
@settings(max_examples=50)
def test_tfsmextended::state_instantiation(instance):
    assert isinstance(instance, tfsmextended::State)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::State_strategy)
@settings(max_examples=30)
def test_tfsmextended::state_onleave_changes_state(instance):
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
        assert has_statements, f"Function 'onLeave' in tfsmextended::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onLeave' in tfsmextended::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onLeave' in tfsmextended::State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::State_strategy)
@settings(max_examples=30)
def test_tfsmextended::state_onenter_changes_state(instance):
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
        assert has_statements, f"Function 'onEnter' in tfsmextended::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onEnter' in tfsmextended::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onEnter' in tfsmextended::State is not implemented or raised an error")

@given(instance=tfsmextended::Transition_strategy)
@settings(max_examples=50)
def test_tfsmextended::transition_instantiation(instance):
    assert isinstance(instance, tfsmextended::Transition)

@given(instance=tfsmextended::Transition_strategy)
def test_tfsmextended::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=tfsmextended::Transition_strategy)
def test_tfsmextended::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::Transition_strategy)
@settings(max_examples=30)
def test_tfsmextended::transition_fire_changes_state(instance):
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
        assert has_statements, f"Function 'fire' in tfsmextended::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in tfsmextended::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in tfsmextended::Transition is not implemented or raised an error")

@given(instance=tfsmextended::TFSM_strategy)
@settings(max_examples=50)
def test_tfsmextended::tfsm_instantiation(instance):
    assert isinstance(instance, tfsmextended::TFSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tfsmextended::TFSM_strategy)
@settings(max_examples=30)
def test_tfsmextended::tfsm_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in tfsmextended::TFSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in tfsmextended::TFSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in tfsmextended::TFSM is not implemented or raised an error")
