import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TraceMetamodel_EObject,
    TraceMetamodel_TraceLinkEnd,
    TraceMetamodel_TraceLink,
    TraceMetamodel_TraceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracemetamodel_eobject_is_not_abstract():
    assert not inspect.isabstract(TraceMetamodel_EObject)


def test_tracemetamodel_eobject_constructor_exists():
    assert callable(TraceMetamodel_EObject.__init__)


def test_tracemetamodel_eobject_constructor_args():
    sig = inspect.signature(TraceMetamodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_tracemetamodel_tracelinkend_is_not_abstract():
    assert not inspect.isabstract(TraceMetamodel_TraceLinkEnd)


def test_tracemetamodel_tracelinkend_constructor_exists():
    assert callable(TraceMetamodel_TraceLinkEnd.__init__)


def test_tracemetamodel_tracelinkend_constructor_args():
    sig = inspect.signature(TraceMetamodel_TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_tracemetamodel_tracelinkend_has_type():
    assert hasattr(TraceMetamodel_TraceLinkEnd, "type")
    descriptor = None
    for klass in TraceMetamodel_TraceLinkEnd.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tracemetamodel_tracelinkend_has_name():
    assert hasattr(TraceMetamodel_TraceLinkEnd, "name")
    descriptor = None
    for klass in TraceMetamodel_TraceLinkEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tracemetamodel_tracelink_is_not_abstract():
    assert not inspect.isabstract(TraceMetamodel_TraceLink)


def test_tracemetamodel_tracelink_constructor_exists():
    assert callable(TraceMetamodel_TraceLink.__init__)


def test_tracemetamodel_tracelink_constructor_args():
    sig = inspect.signature(TraceMetamodel_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "isNonInjective" in params, "Missing parameter 'isNonInjective'"
    assert "trule" in params, "Missing parameter 'trule'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "isPartial" in params, "Missing parameter 'isPartial'"

def test_tracemetamodel_tracelink_has_isNonInjective():
    assert hasattr(TraceMetamodel_TraceLink, "isNonInjective")
    descriptor = None
    for klass in TraceMetamodel_TraceLink.__mro__:
        if "isNonInjective" in klass.__dict__:
            descriptor = klass.__dict__["isNonInjective"]
            break
    assert isinstance(descriptor, property)

def test_tracemetamodel_tracelink_has_trule():
    assert hasattr(TraceMetamodel_TraceLink, "trule")
    descriptor = None
    for klass in TraceMetamodel_TraceLink.__mro__:
        if "trule" in klass.__dict__:
            descriptor = klass.__dict__["trule"]
            break
    assert isinstance(descriptor, property)

def test_tracemetamodel_tracelink_has_name():
    assert hasattr(TraceMetamodel_TraceLink, "name")
    descriptor = None
    for klass in TraceMetamodel_TraceLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tracemetamodel_tracelink_has_id():
    assert hasattr(TraceMetamodel_TraceLink, "id")
    descriptor = None
    for klass in TraceMetamodel_TraceLink.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tracemetamodel_tracelink_has_isPartial():
    assert hasattr(TraceMetamodel_TraceLink, "isPartial")
    descriptor = None
    for klass in TraceMetamodel_TraceLink.__mro__:
        if "isPartial" in klass.__dict__:
            descriptor = klass.__dict__["isPartial"]
            break
    assert isinstance(descriptor, property)



def test_tracemetamodel_tracemodel_is_not_abstract():
    assert not inspect.isabstract(TraceMetamodel_TraceModel)


def test_tracemetamodel_tracemodel_constructor_exists():
    assert callable(TraceMetamodel_TraceModel.__init__)


def test_tracemetamodel_tracemodel_constructor_args():
    sig = inspect.signature(TraceMetamodel_TraceModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tracemetamodel_tracemodel_has_name():
    assert hasattr(TraceMetamodel_TraceModel, "name")
    descriptor = None
    for klass in TraceMetamodel_TraceModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
TraceMetamodel_EObject_strategy = st.builds(
    TraceMetamodel_EObject,
)
TraceMetamodel_TraceLinkEnd_strategy = st.builds(
    TraceMetamodel_TraceLinkEnd,
    type=
        safe_text,
    name=
        safe_text
)
TraceMetamodel_TraceLink_strategy = st.builds(
    TraceMetamodel_TraceLink,
    isNonInjective=
        st.booleans(),
    trule=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    isPartial=
        st.booleans()
)
TraceMetamodel_TraceModel_strategy = st.builds(
    TraceMetamodel_TraceModel,
    name=
        safe_text
)

@given(instance=TraceMetamodel_EObject_strategy)
@settings(max_examples=50)
def test_tracemetamodel_eobject_instantiation(instance):
    assert isinstance(instance, TraceMetamodel_EObject)

@given(instance=TraceMetamodel_TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_tracemetamodel_tracelinkend_instantiation(instance):
    assert isinstance(instance, TraceMetamodel_TraceLinkEnd)



@given(instance=TraceMetamodel_TraceLinkEnd_strategy)
def test_tracemetamodel_tracelinkend_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=TraceMetamodel_TraceLinkEnd_strategy)
def test_tracemetamodel_tracelinkend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TraceMetamodel_TraceLink_strategy)
@settings(max_examples=50)
def test_tracemetamodel_tracelink_instantiation(instance):
    assert isinstance(instance, TraceMetamodel_TraceLink)



@given(instance=TraceMetamodel_TraceLink_strategy)
def test_tracemetamodel_tracelink_isNonInjective_setter(instance):
    original = instance.isNonInjective
    instance.isNonInjective = original
    assert instance.isNonInjective == original



@given(instance=TraceMetamodel_TraceLink_strategy)
def test_tracemetamodel_tracelink_trule_setter(instance):
    original = instance.trule
    instance.trule = original
    assert instance.trule == original



@given(instance=TraceMetamodel_TraceLink_strategy)
def test_tracemetamodel_tracelink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=TraceMetamodel_TraceLink_strategy)
def test_tracemetamodel_tracelink_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TraceMetamodel_TraceLink_strategy)
def test_tracemetamodel_tracelink_isPartial_setter(instance):
    original = instance.isPartial
    instance.isPartial = original
    assert instance.isPartial == original

@given(instance=TraceMetamodel_TraceModel_strategy)
@settings(max_examples=50)
def test_tracemetamodel_tracemodel_instantiation(instance):
    assert isinstance(instance, TraceMetamodel_TraceModel)



@given(instance=TraceMetamodel_TraceModel_strategy)
def test_tracemetamodel_tracemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
