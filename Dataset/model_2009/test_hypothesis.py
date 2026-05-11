import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scribbleTraceDsl::Parameter,
    Stepdefn,
    scribbleTraceDsl::Messagetransfer,
    scribbleTraceDsl::Stepdefn,
    scribbleTraceDsl::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scribbletracedsl::parameter_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl::Parameter)


def test_scribbletracedsl::parameter_constructor_exists():
    assert callable(scribbleTraceDsl::Parameter.__init__)


def test_scribbletracedsl::parameter_constructor_args():
    sig = inspect.signature(scribbleTraceDsl::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_scribbletracedsl::parameter_has_value():
    assert hasattr(scribbleTraceDsl::Parameter, "value")
    descriptor = None
    for klass in scribbleTraceDsl::Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_scribbletracedsl::parameter_has_type():
    assert hasattr(scribbleTraceDsl::Parameter, "type")
    descriptor = None
    for klass in scribbleTraceDsl::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_stepdefn_is_not_abstract():
    assert not inspect.isabstract(Stepdefn)


def test_stepdefn_constructor_exists():
    assert callable(Stepdefn.__init__)


def test_stepdefn_constructor_args():
    sig = inspect.signature(Stepdefn.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl::messagetransfer_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl::Messagetransfer)


def test_scribbletracedsl::messagetransfer_constructor_exists():
    assert callable(scribbleTraceDsl::Messagetransfer.__init__)


def test_scribbletracedsl::messagetransfer_constructor_args():
    sig = inspect.signature(scribbleTraceDsl::Messagetransfer.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl::stepdefn_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl::Stepdefn)


def test_scribbletracedsl::stepdefn_constructor_exists():
    assert callable(scribbleTraceDsl::Stepdefn.__init__)


def test_scribbletracedsl::stepdefn_constructor_args():
    sig = inspect.signature(scribbleTraceDsl::Stepdefn.__init__)
    params = list(sig.parameters.keys())



def test_scribbletracedsl::trace_is_not_abstract():
    assert not inspect.isabstract(scribbleTraceDsl::Trace)


def test_scribbletracedsl::trace_constructor_exists():
    assert callable(scribbleTraceDsl::Trace.__init__)


def test_scribbletracedsl::trace_constructor_args():
    sig = inspect.signature(scribbleTraceDsl::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "roles" in params, "Missing parameter 'roles'"

def test_scribbletracedsl::trace_has_roles():
    assert hasattr(scribbleTraceDsl::Trace, "roles")
    descriptor = None
    for klass in scribbleTraceDsl::Trace.__mro__:
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
scribbleTraceDsl::Parameter_strategy = st.builds(
    scribbleTraceDsl::Parameter,
    value=
        safe_text,
    type=
        safe_text
)
Stepdefn_strategy = st.builds(
    Stepdefn,
)
scribbleTraceDsl::Messagetransfer_strategy = st.builds(
    scribbleTraceDsl::Messagetransfer,
)
scribbleTraceDsl::Stepdefn_strategy = st.builds(
    scribbleTraceDsl::Stepdefn,
)
scribbleTraceDsl::Trace_strategy = st.builds(
    scribbleTraceDsl::Trace,
    roles=
        safe_text
)

@given(instance=scribbleTraceDsl::Parameter_strategy)
@settings(max_examples=50)
def test_scribbletracedsl::parameter_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl::Parameter)

@given(instance=scribbleTraceDsl::Parameter_strategy)
def test_scribbletracedsl::parameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=scribbleTraceDsl::Parameter_strategy)
def test_scribbletracedsl::parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=scribbleTraceDsl::Parameter_strategy)
def test_scribbletracedsl::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scribbleTraceDsl::Parameter_strategy)
def test_scribbletracedsl::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Stepdefn_strategy)
@settings(max_examples=50)
def test_stepdefn_instantiation(instance):
    assert isinstance(instance, Stepdefn)

@given(instance=scribbleTraceDsl::Messagetransfer_strategy)
@settings(max_examples=50)
def test_scribbletracedsl::messagetransfer_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl::Messagetransfer)

@given(instance=scribbleTraceDsl::Stepdefn_strategy)
@settings(max_examples=50)
def test_scribbletracedsl::stepdefn_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl::Stepdefn)

@given(instance=scribbleTraceDsl::Trace_strategy)
@settings(max_examples=50)
def test_scribbletracedsl::trace_instantiation(instance):
    assert isinstance(instance, scribbleTraceDsl::Trace)

@given(instance=scribbleTraceDsl::Trace_strategy)
def test_scribbletracedsl::trace_roles_type(instance):
    assert isinstance(instance.roles, str)


@given(instance=scribbleTraceDsl::Trace_strategy)
def test_scribbletracedsl::trace_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original
