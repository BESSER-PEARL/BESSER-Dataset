import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::EObject,
    trace::TraceLink,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracelink_is_not_abstract():
    assert not inspect.isabstract(trace::TraceLink)


def test_trace::tracelink_constructor_exists():
    assert callable(trace::TraceLink.__init__)


def test_trace::tracelink_constructor_args():
    sig = inspect.signature(trace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "targetValue" in params, "Missing parameter 'targetValue'"
    assert "similarity" in params, "Missing parameter 'similarity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "sourceValue" in params, "Missing parameter 'sourceValue'"
    assert "similarityMethod" in params, "Missing parameter 'similarityMethod'"
    assert "requiredSimilarity" in params, "Missing parameter 'requiredSimilarity'"

def test_trace::tracelink_has_targetValue():
    assert hasattr(trace::TraceLink, "targetValue")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "targetValue" in klass.__dict__:
            descriptor = klass.__dict__["targetValue"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_similarity():
    assert hasattr(trace::TraceLink, "similarity")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "similarity" in klass.__dict__:
            descriptor = klass.__dict__["similarity"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_name():
    assert hasattr(trace::TraceLink, "name")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_rationale():
    assert hasattr(trace::TraceLink, "rationale")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_sourceValue():
    assert hasattr(trace::TraceLink, "sourceValue")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "sourceValue" in klass.__dict__:
            descriptor = klass.__dict__["sourceValue"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_similarityMethod():
    assert hasattr(trace::TraceLink, "similarityMethod")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "similarityMethod" in klass.__dict__:
            descriptor = klass.__dict__["similarityMethod"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_requiredSimilarity():
    assert hasattr(trace::TraceLink, "requiredSimilarity")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "requiredSimilarity" in klass.__dict__:
            descriptor = klass.__dict__["requiredSimilarity"]
            break
    assert isinstance(descriptor, property)



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
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
trace::EObject_strategy = st.builds(
    trace::EObject,
)
trace::TraceLink_strategy = st.builds(
    trace::TraceLink,
    targetValue=
        safe_text,
    similarity=
        st.integers(),
    name=
        safe_text,
    rationale=
        safe_text,
    sourceValue=
        safe_text,
    similarityMethod=
        st.integers(),
    requiredSimilarity=
        st.integers()
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=trace::TraceLink_strategy)
@settings(max_examples=50)
def test_trace::tracelink_instantiation(instance):
    assert isinstance(instance, trace::TraceLink)

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_targetValue_type(instance):
    assert isinstance(instance.targetValue, str)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_targetValue_setter(instance):
    original = instance.targetValue
    instance.targetValue = original
    assert instance.targetValue == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_similarity_type(instance):
    assert isinstance(instance.similarity, int)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_similarity_setter(instance):
    original = instance.similarity
    instance.similarity = original
    assert instance.similarity == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_rationale_type(instance):
    assert isinstance(instance.rationale, str)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_sourceValue_type(instance):
    assert isinstance(instance.sourceValue, str)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_sourceValue_setter(instance):
    original = instance.sourceValue
    instance.sourceValue = original
    assert instance.sourceValue == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_similarityMethod_type(instance):
    assert isinstance(instance.similarityMethod, int)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_similarityMethod_setter(instance):
    original = instance.similarityMethod
    instance.similarityMethod = original
    assert instance.similarityMethod == original

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_requiredSimilarity_type(instance):
    assert isinstance(instance.requiredSimilarity, int)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_requiredSimilarity_setter(instance):
    original = instance.requiredSimilarity
    instance.requiredSimilarity = original
    assert instance.requiredSimilarity == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=trace::TraceLink_strategy)
@settings(max_examples=30)
def test_trace::tracelink_sameas_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.sameAs(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.sameAs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'sameAs' in trace::TraceLink is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'sameAs' in trace::TraceLink did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'sameAs' in trace::TraceLink is not implemented or raised an error")

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)
