import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cpsml::Condition,
    cpsml::Function,
    Transition,
    cpsml::ProbTransition,
    cpsml::ComTransition,
    cpsml::ODE,
    cpsml::Transition,
    cpsml::State,
    cpsml::Variable,
    cpsml::System,
    cpsml::Fright,
    cpsml::DeVariable,
    cpsml::IndeVariable,
    cpsml::Interval,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cpsml::condition_is_not_abstract():
    assert not inspect.isabstract(cpsml::Condition)


def test_cpsml::condition_constructor_exists():
    assert callable(cpsml::Condition.__init__)


def test_cpsml::condition_constructor_args():
    sig = inspect.signature(cpsml::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::condition_has_name():
    assert hasattr(cpsml::Condition, "name")
    descriptor = None
    for klass in cpsml::Condition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::function_is_not_abstract():
    assert not inspect.isabstract(cpsml::Function)


def test_cpsml::function_constructor_exists():
    assert callable(cpsml::Function.__init__)


def test_cpsml::function_constructor_args():
    sig = inspect.signature(cpsml::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::function_has_name():
    assert hasattr(cpsml::Function, "name")
    descriptor = None
    for klass in cpsml::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_cpsml::probtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml::ProbTransition)


def test_cpsml::probtransition_constructor_exists():
    assert callable(cpsml::ProbTransition.__init__)


def test_cpsml::probtransition_constructor_args():
    sig = inspect.signature(cpsml::ProbTransition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_cpsml::probtransition_has_probability():
    assert hasattr(cpsml::ProbTransition, "probability")
    descriptor = None
    for klass in cpsml::ProbTransition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::comtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml::ComTransition)


def test_cpsml::comtransition_constructor_exists():
    assert callable(cpsml::ComTransition.__init__)


def test_cpsml::comtransition_constructor_args():
    sig = inspect.signature(cpsml::ComTransition.__init__)
    params = list(sig.parameters.keys())



def test_cpsml::ode_is_not_abstract():
    assert not inspect.isabstract(cpsml::ODE)


def test_cpsml::ode_constructor_exists():
    assert callable(cpsml::ODE.__init__)


def test_cpsml::ode_constructor_args():
    sig = inspect.signature(cpsml::ODE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::ode_has_name():
    assert hasattr(cpsml::ODE, "name")
    descriptor = None
    for klass in cpsml::ODE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::transition_is_not_abstract():
    assert not inspect.isabstract(cpsml::Transition)


def test_cpsml::transition_constructor_exists():
    assert callable(cpsml::Transition.__init__)


def test_cpsml::transition_constructor_args():
    sig = inspect.signature(cpsml::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "event" in params, "Missing parameter 'event'"

def test_cpsml::transition_has_guard():
    assert hasattr(cpsml::Transition, "guard")
    descriptor = None
    for klass in cpsml::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::transition_has_action():
    assert hasattr(cpsml::Transition, "action")
    descriptor = None
    for klass in cpsml::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::transition_has_name():
    assert hasattr(cpsml::Transition, "name")
    descriptor = None
    for klass in cpsml::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::transition_has_event():
    assert hasattr(cpsml::Transition, "event")
    descriptor = None
    for klass in cpsml::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::state_is_not_abstract():
    assert not inspect.isabstract(cpsml::State)


def test_cpsml::state_constructor_exists():
    assert callable(cpsml::State.__init__)


def test_cpsml::state_constructor_args():
    sig = inspect.signature(cpsml::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::state_has_name():
    assert hasattr(cpsml::State, "name")
    descriptor = None
    for klass in cpsml::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::variable_is_not_abstract():
    assert not inspect.isabstract(cpsml::Variable)


def test_cpsml::variable_constructor_exists():
    assert callable(cpsml::Variable.__init__)


def test_cpsml::variable_constructor_args():
    sig = inspect.signature(cpsml::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cpsml::variable_has_value():
    assert hasattr(cpsml::Variable, "value")
    descriptor = None
    for klass in cpsml::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::system_is_not_abstract():
    assert not inspect.isabstract(cpsml::System)


def test_cpsml::system_constructor_exists():
    assert callable(cpsml::System.__init__)


def test_cpsml::system_constructor_args():
    sig = inspect.signature(cpsml::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::system_has_name():
    assert hasattr(cpsml::System, "name")
    descriptor = None
    for klass in cpsml::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::fright_is_not_abstract():
    assert not inspect.isabstract(cpsml::Fright)


def test_cpsml::fright_constructor_exists():
    assert callable(cpsml::Fright.__init__)


def test_cpsml::fright_constructor_args():
    sig = inspect.signature(cpsml::Fright.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::fright_has_name():
    assert hasattr(cpsml::Fright, "name")
    descriptor = None
    for klass in cpsml::Fright.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::devariable_is_not_abstract():
    assert not inspect.isabstract(cpsml::DeVariable)


def test_cpsml::devariable_constructor_exists():
    assert callable(cpsml::DeVariable.__init__)


def test_cpsml::devariable_constructor_args():
    sig = inspect.signature(cpsml::DeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::devariable_has_name():
    assert hasattr(cpsml::DeVariable, "name")
    descriptor = None
    for klass in cpsml::DeVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::indevariable_is_not_abstract():
    assert not inspect.isabstract(cpsml::IndeVariable)


def test_cpsml::indevariable_constructor_exists():
    assert callable(cpsml::IndeVariable.__init__)


def test_cpsml::indevariable_constructor_args():
    sig = inspect.signature(cpsml::IndeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml::indevariable_has_name():
    assert hasattr(cpsml::IndeVariable, "name")
    descriptor = None
    for klass in cpsml::IndeVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml::interval_is_not_abstract():
    assert not inspect.isabstract(cpsml::Interval)


def test_cpsml::interval_constructor_exists():
    assert callable(cpsml::Interval.__init__)


def test_cpsml::interval_constructor_args():
    sig = inspect.signature(cpsml::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "subinterval" in params, "Missing parameter 'subinterval'"
    assert "name" in params, "Missing parameter 'name'"
    assert "right" in params, "Missing parameter 'right'"

def test_cpsml::interval_has_left():
    assert hasattr(cpsml::Interval, "left")
    descriptor = None
    for klass in cpsml::Interval.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::interval_has_subinterval():
    assert hasattr(cpsml::Interval, "subinterval")
    descriptor = None
    for klass in cpsml::Interval.__mro__:
        if "subinterval" in klass.__dict__:
            descriptor = klass.__dict__["subinterval"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::interval_has_name():
    assert hasattr(cpsml::Interval, "name")
    descriptor = None
    for klass in cpsml::Interval.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cpsml::interval_has_right():
    assert hasattr(cpsml::Interval, "right")
    descriptor = None
    for klass in cpsml::Interval.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
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
cpsml::Condition_strategy = st.builds(
    cpsml::Condition,
    name=
        safe_text
)
cpsml::Function_strategy = st.builds(
    cpsml::Function,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
cpsml::ProbTransition_strategy = st.builds(
    cpsml::ProbTransition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml::ComTransition_strategy = st.builds(
    cpsml::ComTransition,
)
cpsml::ODE_strategy = st.builds(
    cpsml::ODE,
    name=
        safe_text
)
cpsml::Transition_strategy = st.builds(
    cpsml::Transition,
    guard=
        safe_text,
    action=
        safe_text,
    name=
        safe_text,
    event=
        safe_text
)
cpsml::State_strategy = st.builds(
    cpsml::State,
    name=
        safe_text
)
cpsml::Variable_strategy = st.builds(
    cpsml::Variable,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml::System_strategy = st.builds(
    cpsml::System,
    name=
        safe_text
)
cpsml::Fright_strategy = st.builds(
    cpsml::Fright,
    name=
        safe_text
)
cpsml::DeVariable_strategy = st.builds(
    cpsml::DeVariable,
    name=
        safe_text
)
cpsml::IndeVariable_strategy = st.builds(
    cpsml::IndeVariable,
    name=
        safe_text
)
cpsml::Interval_strategy = st.builds(
    cpsml::Interval,
    left=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subinterval=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    right=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=cpsml::Condition_strategy)
@settings(max_examples=50)
def test_cpsml::condition_instantiation(instance):
    assert isinstance(instance, cpsml::Condition)

@given(instance=cpsml::Condition_strategy)
def test_cpsml::condition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::Condition_strategy)
def test_cpsml::condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Function_strategy)
@settings(max_examples=50)
def test_cpsml::function_instantiation(instance):
    assert isinstance(instance, cpsml::Function)

@given(instance=cpsml::Function_strategy)
def test_cpsml::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::Function_strategy)
def test_cpsml::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=cpsml::ProbTransition_strategy)
@settings(max_examples=50)
def test_cpsml::probtransition_instantiation(instance):
    assert isinstance(instance, cpsml::ProbTransition)

@given(instance=cpsml::ProbTransition_strategy)
def test_cpsml::probtransition_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=cpsml::ProbTransition_strategy)
def test_cpsml::probtransition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=cpsml::ComTransition_strategy)
@settings(max_examples=50)
def test_cpsml::comtransition_instantiation(instance):
    assert isinstance(instance, cpsml::ComTransition)

@given(instance=cpsml::ODE_strategy)
@settings(max_examples=50)
def test_cpsml::ode_instantiation(instance):
    assert isinstance(instance, cpsml::ODE)

@given(instance=cpsml::ODE_strategy)
def test_cpsml::ode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::ODE_strategy)
def test_cpsml::ode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Transition_strategy)
@settings(max_examples=50)
def test_cpsml::transition_instantiation(instance):
    assert isinstance(instance, cpsml::Transition)

@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=cpsml::Transition_strategy)
def test_cpsml::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=cpsml::State_strategy)
@settings(max_examples=50)
def test_cpsml::state_instantiation(instance):
    assert isinstance(instance, cpsml::State)

@given(instance=cpsml::State_strategy)
def test_cpsml::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::State_strategy)
def test_cpsml::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Variable_strategy)
@settings(max_examples=50)
def test_cpsml::variable_instantiation(instance):
    assert isinstance(instance, cpsml::Variable)

@given(instance=cpsml::Variable_strategy)
def test_cpsml::variable_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=cpsml::Variable_strategy)
def test_cpsml::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cpsml::System_strategy)
@settings(max_examples=50)
def test_cpsml::system_instantiation(instance):
    assert isinstance(instance, cpsml::System)

@given(instance=cpsml::System_strategy)
def test_cpsml::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::System_strategy)
def test_cpsml::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Fright_strategy)
@settings(max_examples=50)
def test_cpsml::fright_instantiation(instance):
    assert isinstance(instance, cpsml::Fright)

@given(instance=cpsml::Fright_strategy)
def test_cpsml::fright_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::Fright_strategy)
def test_cpsml::fright_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::DeVariable_strategy)
@settings(max_examples=50)
def test_cpsml::devariable_instantiation(instance):
    assert isinstance(instance, cpsml::DeVariable)

@given(instance=cpsml::DeVariable_strategy)
def test_cpsml::devariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::DeVariable_strategy)
def test_cpsml::devariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::IndeVariable_strategy)
@settings(max_examples=50)
def test_cpsml::indevariable_instantiation(instance):
    assert isinstance(instance, cpsml::IndeVariable)

@given(instance=cpsml::IndeVariable_strategy)
def test_cpsml::indevariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::IndeVariable_strategy)
def test_cpsml::indevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Interval_strategy)
@settings(max_examples=50)
def test_cpsml::interval_instantiation(instance):
    assert isinstance(instance, cpsml::Interval)

@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_left_type(instance):
    assert isinstance(instance.left, float)


@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_subinterval_type(instance):
    assert isinstance(instance.subinterval, float)


@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_subinterval_setter(instance):
    original = instance.subinterval
    instance.subinterval = original
    assert instance.subinterval == original

@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_right_type(instance):
    assert isinstance(instance.right, float)


@given(instance=cpsml::Interval_strategy)
def test_cpsml::interval_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original
