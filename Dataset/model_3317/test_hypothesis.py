import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traceability::EObject,
    traceability::Trace,
    traceability::Traceability,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceability::eobject_is_not_abstract():
    assert not inspect.isabstract(traceability::EObject)


def test_traceability::eobject_constructor_exists():
    assert callable(traceability::EObject.__init__)


def test_traceability::eobject_constructor_args():
    sig = inspect.signature(traceability::EObject.__init__)
    params = list(sig.parameters.keys())



def test_traceability::trace_is_not_abstract():
    assert not inspect.isabstract(traceability::Trace)


def test_traceability::trace_constructor_exists():
    assert callable(traceability::Trace.__init__)


def test_traceability::trace_constructor_args():
    sig = inspect.signature(traceability::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "objects" in params, "Missing parameter 'objects'"

def test_traceability::trace_has_id():
    assert hasattr(traceability::Trace, "id")
    descriptor = None
    for klass in traceability::Trace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_traceability::trace_has_objects():
    assert hasattr(traceability::Trace, "objects")
    descriptor = None
    for klass in traceability::Trace.__mro__:
        if "objects" in klass.__dict__:
            descriptor = klass.__dict__["objects"]
            break
    assert isinstance(descriptor, property)



def test_traceability::traceability_is_not_abstract():
    assert not inspect.isabstract(traceability::Traceability)


def test_traceability::traceability_constructor_exists():
    assert callable(traceability::Traceability.__init__)


def test_traceability::traceability_constructor_args():
    sig = inspect.signature(traceability::Traceability.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_traceability::traceability_has_id():
    assert hasattr(traceability::Traceability, "id")
    descriptor = None
    for klass in traceability::Traceability.__mro__:
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
traceability::EObject_strategy = st.builds(
    traceability::EObject,
)
traceability::Trace_strategy = st.builds(
    traceability::Trace,
    id=
        safe_text,
    objects=
        safe_text
)
traceability::Traceability_strategy = st.builds(
    traceability::Traceability,
    id=
        safe_text
)

@given(instance=traceability::EObject_strategy)
@settings(max_examples=50)
def test_traceability::eobject_instantiation(instance):
    assert isinstance(instance, traceability::EObject)

@given(instance=traceability::Trace_strategy)
@settings(max_examples=50)
def test_traceability::trace_instantiation(instance):
    assert isinstance(instance, traceability::Trace)

@given(instance=traceability::Trace_strategy)
def test_traceability::trace_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=traceability::Trace_strategy)
def test_traceability::trace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=traceability::Trace_strategy)
def test_traceability::trace_objects_type(instance):
    assert isinstance(instance.objects, str)


@given(instance=traceability::Trace_strategy)
def test_traceability::trace_objects_setter(instance):
    original = instance.objects
    instance.objects = original
    assert instance.objects == original

@given(instance=traceability::Traceability_strategy)
@settings(max_examples=50)
def test_traceability::traceability_instantiation(instance):
    assert isinstance(instance, traceability::Traceability)

@given(instance=traceability::Traceability_strategy)
def test_traceability::traceability_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=traceability::Traceability_strategy)
def test_traceability::traceability_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
