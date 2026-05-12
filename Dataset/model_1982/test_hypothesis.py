import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Traces_EObject,
    Traces_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces_eobject_is_not_abstract():
    assert not inspect.isabstract(Traces_EObject)


def test_traces_eobject_constructor_exists():
    assert callable(Traces_EObject.__init__)


def test_traces_eobject_constructor_args():
    sig = inspect.signature(Traces_EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces_trace_is_not_abstract():
    assert not inspect.isabstract(Traces_Trace)


def test_traces_trace_constructor_exists():
    assert callable(Traces_Trace.__init__)


def test_traces_trace_constructor_args():
    sig = inspect.signature(Traces_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_traces_trace_has_name():
    assert hasattr(Traces_Trace, "name")
    descriptor = None
    for klass in Traces_Trace.__mro__:
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
Traces_EObject_strategy = st.builds(
    Traces_EObject,
)
Traces_Trace_strategy = st.builds(
    Traces_Trace,
    name=
        safe_text
)

@given(instance=Traces_EObject_strategy)
@settings(max_examples=50)
def test_traces_eobject_instantiation(instance):
    assert isinstance(instance, Traces_EObject)

@given(instance=Traces_Trace_strategy)
@settings(max_examples=50)
def test_traces_trace_instantiation(instance):
    assert isinstance(instance, Traces_Trace)



@given(instance=Traces_Trace_strategy)
def test_traces_trace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
