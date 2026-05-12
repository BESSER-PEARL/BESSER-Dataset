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
    assert "ruleDescriptorId" in params, "Missing parameter 'ruleDescriptorId'"

def test_traceability_trace_has_ruleDescriptorId():
    assert hasattr(traceability_Trace, "ruleDescriptorId")
    descriptor = None
    for klass in traceability_Trace.__mro__:
        if "ruleDescriptorId" in klass.__dict__:
            descriptor = klass.__dict__["ruleDescriptorId"]
            break
    assert isinstance(descriptor, property)



def test_traceability_traceability_is_not_abstract():
    assert not inspect.isabstract(traceability_Traceability)


def test_traceability_traceability_constructor_exists():
    assert callable(traceability_Traceability.__init__)


def test_traceability_traceability_constructor_args():
    sig = inspect.signature(traceability_Traceability.__init__)
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
traceability_EObject_strategy = st.builds(
    traceability_EObject,
)
traceability_Trace_strategy = st.builds(
    traceability_Trace,
    ruleDescriptorId=
        safe_text
)
traceability_Traceability_strategy = st.builds(
    traceability_Traceability,
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
def test_traceability_trace_ruleDescriptorId_setter(instance):
    original = instance.ruleDescriptorId
    instance.ruleDescriptorId = original
    assert instance.ruleDescriptorId == original

@given(instance=traceability_Traceability_strategy)
@settings(max_examples=50)
def test_traceability_traceability_instantiation(instance):
    assert isinstance(instance, traceability_Traceability)
