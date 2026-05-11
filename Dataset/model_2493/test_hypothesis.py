import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FExpression,
    fsmWithMethods::MethodCall,
    fsmWithMethods::Event,
    fsmWithMethods::Transition,
    fsmWithMethods::Method,
    fsmWithMethods::Referentiable,
    Referentiable,
    fsmWithMethods::FExpression,
    fsmWithMethods::State,
    fsmWithMethods::Fsm,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fexpression_is_not_abstract():
    assert not inspect.isabstract(FExpression)


def test_fexpression_constructor_exists():
    assert callable(FExpression.__init__)


def test_fexpression_constructor_args():
    sig = inspect.signature(FExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::methodcall_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::MethodCall)


def test_fsmwithmethods::methodcall_constructor_exists():
    assert callable(fsmWithMethods::MethodCall.__init__)


def test_fsmwithmethods::methodcall_constructor_args():
    sig = inspect.signature(fsmWithMethods::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::event_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::Event)


def test_fsmwithmethods::event_constructor_exists():
    assert callable(fsmWithMethods::Event.__init__)


def test_fsmwithmethods::event_constructor_args():
    sig = inspect.signature(fsmWithMethods::Event.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::transition_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::Transition)


def test_fsmwithmethods::transition_constructor_exists():
    assert callable(fsmWithMethods::Transition.__init__)


def test_fsmwithmethods::transition_constructor_args():
    sig = inspect.signature(fsmWithMethods::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::method_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::Method)


def test_fsmwithmethods::method_constructor_exists():
    assert callable(fsmWithMethods::Method.__init__)


def test_fsmwithmethods::method_constructor_args():
    sig = inspect.signature(fsmWithMethods::Method.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::referentiable_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::Referentiable)


def test_fsmwithmethods::referentiable_constructor_exists():
    assert callable(fsmWithMethods::Referentiable.__init__)


def test_fsmwithmethods::referentiable_constructor_args():
    sig = inspect.signature(fsmWithMethods::Referentiable.__init__)
    params = list(sig.parameters.keys())



def test_referentiable_is_not_abstract():
    assert not inspect.isabstract(Referentiable)


def test_referentiable_constructor_exists():
    assert callable(Referentiable.__init__)


def test_referentiable_constructor_args():
    sig = inspect.signature(Referentiable.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::fexpression_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::FExpression)


def test_fsmwithmethods::fexpression_constructor_exists():
    assert callable(fsmWithMethods::FExpression.__init__)


def test_fsmwithmethods::fexpression_constructor_args():
    sig = inspect.signature(fsmWithMethods::FExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmwithmethods::fexpression_has_name():
    assert hasattr(fsmWithMethods::FExpression, "name")
    descriptor = None
    for klass in fsmWithMethods::FExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmwithmethods::state_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::State)


def test_fsmwithmethods::state_constructor_exists():
    assert callable(fsmWithMethods::State.__init__)


def test_fsmwithmethods::state_constructor_args():
    sig = inspect.signature(fsmWithMethods::State.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods::fsm_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods::Fsm)


def test_fsmwithmethods::fsm_constructor_exists():
    assert callable(fsmWithMethods::Fsm.__init__)


def test_fsmwithmethods::fsm_constructor_args():
    sig = inspect.signature(fsmWithMethods::Fsm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmwithmethods::fsm_has_name():
    assert hasattr(fsmWithMethods::Fsm, "name")
    descriptor = None
    for klass in fsmWithMethods::Fsm.__mro__:
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
FExpression_strategy = st.builds(
    FExpression,
)
fsmWithMethods::MethodCall_strategy = st.builds(
    fsmWithMethods::MethodCall,
)
fsmWithMethods::Event_strategy = st.builds(
    fsmWithMethods::Event,
)
fsmWithMethods::Transition_strategy = st.builds(
    fsmWithMethods::Transition,
)
fsmWithMethods::Method_strategy = st.builds(
    fsmWithMethods::Method,
)
fsmWithMethods::Referentiable_strategy = st.builds(
    fsmWithMethods::Referentiable,
)
Referentiable_strategy = st.builds(
    Referentiable,
)
fsmWithMethods::FExpression_strategy = st.builds(
    fsmWithMethods::FExpression,
    name=
        safe_text
)
fsmWithMethods::State_strategy = st.builds(
    fsmWithMethods::State,
)
fsmWithMethods::Fsm_strategy = st.builds(
    fsmWithMethods::Fsm,
    name=
        safe_text
)

@given(instance=FExpression_strategy)
@settings(max_examples=50)
def test_fexpression_instantiation(instance):
    assert isinstance(instance, FExpression)

@given(instance=fsmWithMethods::MethodCall_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::methodcall_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::MethodCall)

@given(instance=fsmWithMethods::Event_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::event_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::Event)

@given(instance=fsmWithMethods::Transition_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::transition_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::Transition)

@given(instance=fsmWithMethods::Method_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::method_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::Method)

@given(instance=fsmWithMethods::Referentiable_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::referentiable_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::Referentiable)

@given(instance=Referentiable_strategy)
@settings(max_examples=50)
def test_referentiable_instantiation(instance):
    assert isinstance(instance, Referentiable)

@given(instance=fsmWithMethods::FExpression_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::fexpression_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::FExpression)

@given(instance=fsmWithMethods::FExpression_strategy)
def test_fsmwithmethods::fexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmWithMethods::FExpression_strategy)
def test_fsmwithmethods::fexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmWithMethods::State_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::state_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::State)

@given(instance=fsmWithMethods::Fsm_strategy)
@settings(max_examples=50)
def test_fsmwithmethods::fsm_instantiation(instance):
    assert isinstance(instance, fsmWithMethods::Fsm)

@given(instance=fsmWithMethods::Fsm_strategy)
def test_fsmwithmethods::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmWithMethods::Fsm_strategy)
def test_fsmwithmethods::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
