import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FExpression,
    fsmWithMethods_Event,
    fsmWithMethods_Transition,
    fsmWithMethods_MethodCall,
    fsmWithMethods_Method,
    fsmWithMethods_Referentiable,
    Referentiable,
    fsmWithMethods_FExpression,
    fsmWithMethods_State,
    fsmWithMethods_Fsm,
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



def test_fsmwithmethods_event_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_Event)


def test_fsmwithmethods_event_constructor_exists():
    assert callable(fsmWithMethods_Event.__init__)


def test_fsmwithmethods_event_constructor_args():
    sig = inspect.signature(fsmWithMethods_Event.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_transition_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_Transition)


def test_fsmwithmethods_transition_constructor_exists():
    assert callable(fsmWithMethods_Transition.__init__)


def test_fsmwithmethods_transition_constructor_args():
    sig = inspect.signature(fsmWithMethods_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_methodcall_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_MethodCall)


def test_fsmwithmethods_methodcall_constructor_exists():
    assert callable(fsmWithMethods_MethodCall.__init__)


def test_fsmwithmethods_methodcall_constructor_args():
    sig = inspect.signature(fsmWithMethods_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_method_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_Method)


def test_fsmwithmethods_method_constructor_exists():
    assert callable(fsmWithMethods_Method.__init__)


def test_fsmwithmethods_method_constructor_args():
    sig = inspect.signature(fsmWithMethods_Method.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_referentiable_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_Referentiable)


def test_fsmwithmethods_referentiable_constructor_exists():
    assert callable(fsmWithMethods_Referentiable.__init__)


def test_fsmwithmethods_referentiable_constructor_args():
    sig = inspect.signature(fsmWithMethods_Referentiable.__init__)
    params = list(sig.parameters.keys())



def test_referentiable_is_not_abstract():
    assert not inspect.isabstract(Referentiable)


def test_referentiable_constructor_exists():
    assert callable(Referentiable.__init__)


def test_referentiable_constructor_args():
    sig = inspect.signature(Referentiable.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_fexpression_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_FExpression)


def test_fsmwithmethods_fexpression_constructor_exists():
    assert callable(fsmWithMethods_FExpression.__init__)


def test_fsmwithmethods_fexpression_constructor_args():
    sig = inspect.signature(fsmWithMethods_FExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmwithmethods_fexpression_has_name():
    assert hasattr(fsmWithMethods_FExpression, "name")
    descriptor = None
    for klass in fsmWithMethods_FExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmwithmethods_state_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_State)


def test_fsmwithmethods_state_constructor_exists():
    assert callable(fsmWithMethods_State.__init__)


def test_fsmwithmethods_state_constructor_args():
    sig = inspect.signature(fsmWithMethods_State.__init__)
    params = list(sig.parameters.keys())



def test_fsmwithmethods_fsm_is_not_abstract():
    assert not inspect.isabstract(fsmWithMethods_Fsm)


def test_fsmwithmethods_fsm_constructor_exists():
    assert callable(fsmWithMethods_Fsm.__init__)


def test_fsmwithmethods_fsm_constructor_args():
    sig = inspect.signature(fsmWithMethods_Fsm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmwithmethods_fsm_has_name():
    assert hasattr(fsmWithMethods_Fsm, "name")
    descriptor = None
    for klass in fsmWithMethods_Fsm.__mro__:
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
fsmWithMethods_Event_strategy = st.builds(
    fsmWithMethods_Event,
)
fsmWithMethods_Transition_strategy = st.builds(
    fsmWithMethods_Transition,
)
fsmWithMethods_MethodCall_strategy = st.builds(
    fsmWithMethods_MethodCall,
)
fsmWithMethods_Method_strategy = st.builds(
    fsmWithMethods_Method,
)
fsmWithMethods_Referentiable_strategy = st.builds(
    fsmWithMethods_Referentiable,
)
Referentiable_strategy = st.builds(
    Referentiable,
)
fsmWithMethods_FExpression_strategy = st.builds(
    fsmWithMethods_FExpression,
    name=
        safe_text
)
fsmWithMethods_State_strategy = st.builds(
    fsmWithMethods_State,
)
fsmWithMethods_Fsm_strategy = st.builds(
    fsmWithMethods_Fsm,
    name=
        safe_text
)

@given(instance=FExpression_strategy)
@settings(max_examples=50)
def test_fexpression_instantiation(instance):
    assert isinstance(instance, FExpression)

@given(instance=fsmWithMethods_Event_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_event_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_Event)

@given(instance=fsmWithMethods_Transition_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_transition_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_Transition)

@given(instance=fsmWithMethods_MethodCall_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_methodcall_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_MethodCall)

@given(instance=fsmWithMethods_Method_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_method_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_Method)

@given(instance=fsmWithMethods_Referentiable_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_referentiable_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_Referentiable)

@given(instance=Referentiable_strategy)
@settings(max_examples=50)
def test_referentiable_instantiation(instance):
    assert isinstance(instance, Referentiable)

@given(instance=fsmWithMethods_FExpression_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_fexpression_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_FExpression)



@given(instance=fsmWithMethods_FExpression_strategy)
def test_fsmwithmethods_fexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmWithMethods_State_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_state_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_State)

@given(instance=fsmWithMethods_Fsm_strategy)
@settings(max_examples=50)
def test_fsmwithmethods_fsm_instantiation(instance):
    assert isinstance(instance, fsmWithMethods_Fsm)



@given(instance=fsmWithMethods_Fsm_strategy)
def test_fsmwithmethods_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
