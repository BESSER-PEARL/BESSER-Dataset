import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Traces::EObject,
    Traces::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces::eobject_is_not_abstract():
    assert not inspect.isabstract(Traces::EObject)


def test_traces::eobject_constructor_exists():
    assert callable(Traces::EObject.__init__)


def test_traces::eobject_constructor_args():
    sig = inspect.signature(Traces::EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces::trace_is_not_abstract():
    assert not inspect.isabstract(Traces::Trace)


def test_traces::trace_constructor_exists():
    assert callable(Traces::Trace.__init__)


def test_traces::trace_constructor_args():
    sig = inspect.signature(Traces::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_traces::trace_has_name():
    assert hasattr(Traces::Trace, "name")
    descriptor = None
    for klass in Traces::Trace.__mro__:
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
Traces::EObject_strategy = st.builds(
    Traces::EObject,
)
Traces::Trace_strategy = st.builds(
    Traces::Trace,
    name=
        safe_text
)

@given(instance=Traces::EObject_strategy)
@settings(max_examples=50)
def test_traces::eobject_instantiation(instance):
    assert isinstance(instance, Traces::EObject)

@given(instance=Traces::Trace_strategy)
@settings(max_examples=50)
def test_traces::trace_instantiation(instance):
    assert isinstance(instance, Traces::Trace)

@given(instance=Traces::Trace_strategy)
def test_traces::trace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Traces::Trace_strategy)
def test_traces::trace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
