import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tracelinks::TraceLink,
    tracelinks::TraceLinksModel,
    tracelinks::TraceLinkEnd,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracelinks::tracelink_is_not_abstract():
    assert not inspect.isabstract(tracelinks::TraceLink)


def test_tracelinks::tracelink_constructor_exists():
    assert callable(tracelinks::TraceLink.__init__)


def test_tracelinks::tracelink_constructor_args():
    sig = inspect.signature(tracelinks::TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_tracelinks::tracelinksmodel_is_not_abstract():
    assert not inspect.isabstract(tracelinks::TraceLinksModel)


def test_tracelinks::tracelinksmodel_constructor_exists():
    assert callable(tracelinks::TraceLinksModel.__init__)


def test_tracelinks::tracelinksmodel_constructor_args():
    sig = inspect.signature(tracelinks::TraceLinksModel.__init__)
    params = list(sig.parameters.keys())



def test_tracelinks::tracelinkend_is_not_abstract():
    assert not inspect.isabstract(tracelinks::TraceLinkEnd)


def test_tracelinks::tracelinkend_constructor_exists():
    assert callable(tracelinks::TraceLinkEnd.__init__)


def test_tracelinks::tracelinkend_constructor_args():
    sig = inspect.signature(tracelinks::TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_tracelinks::tracelinkend_has_id():
    assert hasattr(tracelinks::TraceLinkEnd, "id")
    descriptor = None
    for klass in tracelinks::TraceLinkEnd.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tracelinks::tracelinkend_has_version():
    assert hasattr(tracelinks::TraceLinkEnd, "version")
    descriptor = None
    for klass in tracelinks::TraceLinkEnd.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
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
tracelinks::TraceLink_strategy = st.builds(
    tracelinks::TraceLink,
)
tracelinks::TraceLinksModel_strategy = st.builds(
    tracelinks::TraceLinksModel,
)
tracelinks::TraceLinkEnd_strategy = st.builds(
    tracelinks::TraceLinkEnd,
    id=
        safe_text,
    version=
        safe_text
)

@given(instance=tracelinks::TraceLink_strategy)
@settings(max_examples=50)
def test_tracelinks::tracelink_instantiation(instance):
    assert isinstance(instance, tracelinks::TraceLink)

@given(instance=tracelinks::TraceLinksModel_strategy)
@settings(max_examples=50)
def test_tracelinks::tracelinksmodel_instantiation(instance):
    assert isinstance(instance, tracelinks::TraceLinksModel)

@given(instance=tracelinks::TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_tracelinks::tracelinkend_instantiation(instance):
    assert isinstance(instance, tracelinks::TraceLinkEnd)

@given(instance=tracelinks::TraceLinkEnd_strategy)
def test_tracelinks::tracelinkend_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=tracelinks::TraceLinkEnd_strategy)
def test_tracelinks::tracelinkend_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tracelinks::TraceLinkEnd_strategy)
def test_tracelinks::tracelinkend_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=tracelinks::TraceLinkEnd_strategy)
def test_tracelinks::tracelinkend_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
