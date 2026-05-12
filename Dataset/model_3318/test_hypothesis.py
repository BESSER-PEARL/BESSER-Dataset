import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    traceability_EObject,
    traceability_Trace,
    traceability_Traceability,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceability_eobject_is_not_abstract():
    assert not inspect.isabstract(traceability_EObject)


def test_traceability_eobject_constructor_exists():
    assert callable(traceability_EObject.__init__)


def test_traceability_eobject_constructor_args():
    sig = inspect.signature(traceability_EObject.__init__)
    params = list(sig.parameters.keys())



def test_traceability_trace_is_not_abstract():
    assert not inspect.isabstract(traceability_Trace)


def test_traceability_trace_constructor_exists():
    assert callable(traceability_Trace.__init__)


def test_traceability_trace_constructor_args():
    sig = inspect.signature(traceability_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "objects" in params, "Missing parameter 'objects'"
    assert "id" in params, "Missing parameter 'id'"

def test_traceability_trace_has_objects():
    assert hasattr(traceability_Trace, "objects")
    descriptor = None
    for klass in traceability_Trace.__mro__:
        if "objects" in klass.__dict__:
            descriptor = klass.__dict__["objects"]
            break
    assert isinstance(descriptor, property)

def test_traceability_trace_has_id():
    assert hasattr(traceability_Trace, "id")
    descriptor = None
    for klass in traceability_Trace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_traceability_traceability_is_not_abstract():
    assert not inspect.isabstract(traceability_Traceability)


def test_traceability_traceability_constructor_exists():
    assert callable(traceability_Traceability.__init__)


def test_traceability_traceability_constructor_args():
    sig = inspect.signature(traceability_Traceability.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_traceability_traceability_has_id():
    assert hasattr(traceability_Traceability, "id")
    descriptor = None
    for klass in traceability_Traceability.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
traceability_EObject_strategy = st.builds(
    traceability_EObject,
)
traceability_Trace_strategy = st.builds(
    traceability_Trace,
    objects=
        safe_text,
    id=
        safe_text
)
traceability_Traceability_strategy = st.builds(
    traceability_Traceability,
    id=
        safe_text
)

@given(instance=traceability_EObject_strategy)
@settings(max_examples=50)
def test_traceability_eobject_instantiation(instance):
    assert isinstance(instance, traceability_EObject)

@given(instance=traceability_Trace_strategy)
@settings(max_examples=50)
def test_traceability_trace_instantiation(instance):
    assert isinstance(instance, traceability_Trace)



@given(instance=traceability_Trace_strategy)
def test_traceability_trace_objects_setter(instance):
    original = instance.objects
    instance.objects = original
    assert instance.objects == original



@given(instance=traceability_Trace_strategy)
def test_traceability_trace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=traceability_Traceability_strategy)
@settings(max_examples=50)
def test_traceability_traceability_instantiation(instance):
    assert isinstance(instance, traceability_Traceability)



@given(instance=traceability_Traceability_strategy)
def test_traceability_traceability_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
