import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tracelinks_TraceLink,
    tracelinks_TraceLinksModel,
    tracelinks_TraceLinkEnd,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracelinks_tracelink_is_not_abstract():
    assert not inspect.isabstract(tracelinks_TraceLink)


def test_tracelinks_tracelink_constructor_exists():
    assert callable(tracelinks_TraceLink.__init__)


def test_tracelinks_tracelink_constructor_args():
    sig = inspect.signature(tracelinks_TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_tracelinks_tracelinksmodel_is_not_abstract():
    assert not inspect.isabstract(tracelinks_TraceLinksModel)


def test_tracelinks_tracelinksmodel_constructor_exists():
    assert callable(tracelinks_TraceLinksModel.__init__)


def test_tracelinks_tracelinksmodel_constructor_args():
    sig = inspect.signature(tracelinks_TraceLinksModel.__init__)
    params = list(sig.parameters.keys())



def test_tracelinks_tracelinkend_is_not_abstract():
    assert not inspect.isabstract(tracelinks_TraceLinkEnd)


def test_tracelinks_tracelinkend_constructor_exists():
    assert callable(tracelinks_TraceLinkEnd.__init__)


def test_tracelinks_tracelinkend_constructor_args():
    sig = inspect.signature(tracelinks_TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_tracelinks_tracelinkend_has_version():
    assert hasattr(tracelinks_TraceLinkEnd, "version")
    descriptor = None
    for klass in tracelinks_TraceLinkEnd.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_tracelinks_tracelinkend_has_id():
    assert hasattr(tracelinks_TraceLinkEnd, "id")
    descriptor = None
    for klass in tracelinks_TraceLinkEnd.__mro__:
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
tracelinks_TraceLink_strategy = st.builds(
    tracelinks_TraceLink,
)
tracelinks_TraceLinksModel_strategy = st.builds(
    tracelinks_TraceLinksModel,
)
tracelinks_TraceLinkEnd_strategy = st.builds(
    tracelinks_TraceLinkEnd,
    version=
        safe_text,
    id=
        safe_text
)

@given(instance=tracelinks_TraceLink_strategy)
@settings(max_examples=50)
def test_tracelinks_tracelink_instantiation(instance):
    assert isinstance(instance, tracelinks_TraceLink)

@given(instance=tracelinks_TraceLinksModel_strategy)
@settings(max_examples=50)
def test_tracelinks_tracelinksmodel_instantiation(instance):
    assert isinstance(instance, tracelinks_TraceLinksModel)

@given(instance=tracelinks_TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_tracelinks_tracelinkend_instantiation(instance):
    assert isinstance(instance, tracelinks_TraceLinkEnd)



@given(instance=tracelinks_TraceLinkEnd_strategy)
def test_tracelinks_tracelinkend_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=tracelinks_TraceLinkEnd_strategy)
def test_tracelinks_tracelinkend_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
