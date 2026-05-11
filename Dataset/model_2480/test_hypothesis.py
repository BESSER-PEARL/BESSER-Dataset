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
    assert "ruleDescriptorId" in params, "Missing parameter 'ruleDescriptorId'"

def test_traceability::trace_has_ruleDescriptorId():
    assert hasattr(traceability::Trace, "ruleDescriptorId")
    descriptor = None
    for klass in traceability::Trace.__mro__:
        if "ruleDescriptorId" in klass.__dict__:
            descriptor = klass.__dict__["ruleDescriptorId"]
            break
    assert isinstance(descriptor, property)



def test_traceability::traceability_is_not_abstract():
    assert not inspect.isabstract(traceability::Traceability)


def test_traceability::traceability_constructor_exists():
    assert callable(traceability::Traceability.__init__)


def test_traceability::traceability_constructor_args():
    sig = inspect.signature(traceability::Traceability.__init__)
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
traceability::EObject_strategy = st.builds(
    traceability::EObject,
)
traceability::Trace_strategy = st.builds(
    traceability::Trace,
    ruleDescriptorId=
        safe_text
)
traceability::Traceability_strategy = st.builds(
    traceability::Traceability,
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
def test_traceability::trace_ruleDescriptorId_type(instance):
    assert isinstance(instance.ruleDescriptorId, str)


@given(instance=traceability::Trace_strategy)
def test_traceability::trace_ruleDescriptorId_setter(instance):
    original = instance.ruleDescriptorId
    instance.ruleDescriptorId = original
    assert instance.ruleDescriptorId == original

@given(instance=traceability::Traceability_strategy)
@settings(max_examples=50)
def test_traceability::traceability_instantiation(instance):
    assert isinstance(instance, traceability::Traceability)
