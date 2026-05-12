import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tracemap_TraceMap,
    tracemap_TraceEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracemap_tracemap_is_not_abstract():
    assert not inspect.isabstract(tracemap_TraceMap)


def test_tracemap_tracemap_constructor_exists():
    assert callable(tracemap_TraceMap.__init__)


def test_tracemap_tracemap_constructor_args():
    sig = inspect.signature(tracemap_TraceMap.__init__)
    params = list(sig.parameters.keys())



def test_tracemap_traceentry_is_not_abstract():
    assert not inspect.isabstract(tracemap_TraceEntry)


def test_tracemap_traceentry_constructor_exists():
    assert callable(tracemap_TraceEntry.__init__)


def test_tracemap_traceentry_constructor_args():
    sig = inspect.signature(tracemap_TraceEntry.__init__)
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
tracemap_TraceMap_strategy = st.builds(
    tracemap_TraceMap,
)
tracemap_TraceEntry_strategy = st.builds(
    tracemap_TraceEntry,
)

@given(instance=tracemap_TraceMap_strategy)
@settings(max_examples=50)
def test_tracemap_tracemap_instantiation(instance):
    assert isinstance(instance, tracemap_TraceMap)

@given(instance=tracemap_TraceEntry_strategy)
@settings(max_examples=50)
def test_tracemap_traceentry_instantiation(instance):
    assert isinstance(instance, tracemap_TraceEntry)
