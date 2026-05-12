import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UmlTrace_EClass0,
    UmlTrace_Class,
    UmlTrace_TraceElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umltrace_eclass0_is_not_abstract():
    assert not inspect.isabstract(UmlTrace_EClass0)


def test_umltrace_eclass0_constructor_exists():
    assert callable(UmlTrace_EClass0.__init__)


def test_umltrace_eclass0_constructor_args():
    sig = inspect.signature(UmlTrace_EClass0.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_class_is_not_abstract():
    assert not inspect.isabstract(UmlTrace_Class)


def test_umltrace_class_constructor_exists():
    assert callable(UmlTrace_Class.__init__)


def test_umltrace_class_constructor_args():
    sig = inspect.signature(UmlTrace_Class.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_traceelement_is_not_abstract():
    assert not inspect.isabstract(UmlTrace_TraceElement)


def test_umltrace_traceelement_constructor_exists():
    assert callable(UmlTrace_TraceElement.__init__)


def test_umltrace_traceelement_constructor_args():
    sig = inspect.signature(UmlTrace_TraceElement.__init__)
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
UmlTrace_EClass0_strategy = st.builds(
    UmlTrace_EClass0,
)
UmlTrace_Class_strategy = st.builds(
    UmlTrace_Class,
)
UmlTrace_TraceElement_strategy = st.builds(
    UmlTrace_TraceElement,
)

@given(instance=UmlTrace_EClass0_strategy)
@settings(max_examples=50)
def test_umltrace_eclass0_instantiation(instance):
    assert isinstance(instance, UmlTrace_EClass0)

@given(instance=UmlTrace_Class_strategy)
@settings(max_examples=50)
def test_umltrace_class_instantiation(instance):
    assert isinstance(instance, UmlTrace_Class)

@given(instance=UmlTrace_TraceElement_strategy)
@settings(max_examples=50)
def test_umltrace_traceelement_instantiation(instance):
    assert isinstance(instance, UmlTrace_TraceElement)
