import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scribbleTraceDsl_Parameter,
    Stepdefn,
    scribbleTraceDsl_Messagetransfer,
    scribbleTraceDsl_Stepdefn,
    scribbleTraceDsl_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scribbletracedsl_parameter_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl_Parameter)


def test_scribbletracedsl_parameter_constructor_exists():
    assert callable(scribbleTraceDsl_Parameter.__init__)


def test_scribbletracedsl_parameter_constructor_args():
    sig = inspect.signature(scribbleTraceDsl_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_scribbletracedsl_parameter_has_type():
    assert hasattr(scribbleTraceDsl_Parameter, "type")
    descriptor = None
    for klass in scribbleTraceDsl_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scribbletracedsl_parameter_has_value():
    assert hasattr(scribbleTraceDsl_Parameter, "value")
    descriptor = None
    for klass in scribbleTraceDsl_Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stepdefn_is_not_abstract():
    assert not inspect.isabstract(Stepdefn)


def test_stepdefn_constructor_exists():
    assert callable(Stepdefn.__init__)


def test_stepdefn_constructor_args():
    sig = inspect.signature(Stepdefn.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl_messagetransfer_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl_Messagetransfer)


def test_scribbletracedsl_messagetransfer_constructor_exists():
    assert callable(scribbleTraceDsl_Messagetransfer.__init__)


def test_scribbletracedsl_messagetransfer_constructor_args():
    sig = inspect.signature(scribbleTraceDsl_Messagetransfer.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl_stepdefn_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl_Stepdefn)


def test_scribbletracedsl_stepdefn_constructor_exists():
    assert callable(scribbleTraceDsl_Stepdefn.__init__)


def test_scribbletracedsl_stepdefn_constructor_args():
    sig = inspect.signature(scribbleTraceDsl_Stepdefn.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl_trace_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl_Trace)


def test_scribbletracedsl_trace_constructor_exists():
    assert callable(scribbleTraceDsl_Trace.__init__)


def test_scribbletracedsl_trace_constructor_args():
    sig = inspect.signature(scribbleTraceDsl_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "roles" in params, "Missing parameter 'roles'"

def test_scribbletracedsl_trace_has_roles():
    assert hasattr(scribbleTraceDsl_Trace, "roles")
    descriptor = None
    for klass in scribbleTraceDsl_Trace.__mro__:
        if "roles" in klass.__dict__:
            descriptor = klass.__dict__["roles"]
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
scribbleTraceDsl_Parameter_strategy = st.builds(
    scribbleTraceDsl_Parameter,
    type=
        safe_text,
    value=
        safe_text
)
Stepdefn_strategy = st.builds(
    Stepdefn,
)
scribbleTraceDsl_Messagetransfer_strategy = st.builds(
    scribbleTraceDsl_Messagetransfer,
)
scribbleTraceDsl_Stepdefn_strategy = st.builds(
    scribbleTraceDsl_Stepdefn,
)
scribbleTraceDsl_Trace_strategy = st.builds(
    scribbleTraceDsl_Trace,
    roles=
        safe_text
)

@given(instance=scribbleTraceDsl_Parameter_strategy)
@settings(max_examples=50)
def test_scribbletracedsl_parameter_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl_Parameter)



@given(instance=scribbleTraceDsl_Parameter_strategy)
def test_scribbletracedsl_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scribbleTraceDsl_Parameter_strategy)
def test_scribbletracedsl_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Stepdefn_strategy)
@settings(max_examples=50)
def test_stepdefn_instantiation(instance):
    assert isinstance(instance, Stepdefn)

@given(instance=scribbleTraceDsl_Messagetransfer_strategy)
@settings(max_examples=50)
def test_scribbletracedsl_messagetransfer_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl_Messagetransfer)

@given(instance=scribbleTraceDsl_Stepdefn_strategy)
@settings(max_examples=50)
def test_scribbletracedsl_stepdefn_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl_Stepdefn)

@given(instance=scribbleTraceDsl_Trace_strategy)
@settings(max_examples=50)
def test_scribbletracedsl_trace_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl_Trace)



@given(instance=scribbleTraceDsl_Trace_strategy)
def test_scribbletracedsl_trace_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original
