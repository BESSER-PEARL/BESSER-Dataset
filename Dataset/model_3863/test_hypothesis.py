import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tracemap::TraceMap,
    tracemap::TraceEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracemap::tracemap_is_not_abstract():
    assert not inspect.isabstract(tracemap::TraceMap)


def test_tracemap::tracemap_constructor_exists():
    assert callable(tracemap::TraceMap.__init__)


def test_tracemap::tracemap_constructor_args():
    sig = inspect.signature(tracemap::TraceMap.__init__)
    params = list(sig.parameters.keys())



def test_tracemap::traceentry_is_not_abstract():
    assert not inspect.isabstract(tracemap::TraceEntry)


def test_tracemap::traceentry_constructor_exists():
    assert callable(tracemap::TraceEntry.__init__)


def test_tracemap::traceentry_constructor_args():
    sig = inspect.signature(tracemap::TraceEntry.__init__)
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
tracemap::TraceMap_strategy = st.builds(
    tracemap::TraceMap,
)
tracemap::TraceEntry_strategy = st.builds(
    tracemap::TraceEntry,
)

@given(instance=tracemap::TraceMap_strategy)
@settings(max_examples=50)
def test_tracemap::tracemap_instantiation(instance):
    assert isinstance(instance, tracemap::TraceMap)

@given(instance=tracemap::TraceEntry_strategy)
@settings(max_examples=50)
def test_tracemap::traceentry_instantiation(instance):
    assert isinstance(instance, tracemap::TraceEntry)
