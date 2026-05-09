import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UmlTrace::EClass0,
    UmlTrace::Class,
    UmlTrace::TraceElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umltrace::eclass0_is_not_abstract():
    assert not inspect.isabstract(UmlTrace::EClass0)


def test_umltrace::eclass0_constructor_exists():
    assert callable(UmlTrace::EClass0.__init__)


def test_umltrace::eclass0_constructor_args():
    sig = inspect.signature(UmlTrace::EClass0.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::class_is_not_abstract():
    assert not inspect.isabstract(UmlTrace::Class)


def test_umltrace::class_constructor_exists():
    assert callable(UmlTrace::Class.__init__)


def test_umltrace::class_constructor_args():
    sig = inspect.signature(UmlTrace::Class.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::traceelement_is_not_abstract():
    assert not inspect.isabstract(UmlTrace::TraceElement)


def test_umltrace::traceelement_constructor_exists():
    assert callable(UmlTrace::TraceElement.__init__)


def test_umltrace::traceelement_constructor_args():
    sig = inspect.signature(UmlTrace::TraceElement.__init__)
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
UmlTrace::EClass0_strategy = st.builds(
    UmlTrace::EClass0,
)
UmlTrace::Class_strategy = st.builds(
    UmlTrace::Class,
)
UmlTrace::TraceElement_strategy = st.builds(
    UmlTrace::TraceElement,
)

@given(instance=UmlTrace::EClass0_strategy)
@settings(max_examples=50)
def test_umltrace::eclass0_instantiation(instance):
    assert isinstance(instance, UmlTrace::EClass0)

@given(instance=UmlTrace::Class_strategy)
@settings(max_examples=50)
def test_umltrace::class_instantiation(instance):
    assert isinstance(instance, UmlTrace::Class)

@given(instance=UmlTrace::TraceElement_strategy)
@settings(max_examples=50)
def test_umltrace::traceelement_instantiation(instance):
    assert isinstance(instance, UmlTrace::TraceElement)
