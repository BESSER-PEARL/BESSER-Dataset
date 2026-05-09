import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yyc::Thing,
    yyc::Blias,
    yyc::Alias,
    yyc::RelatedTo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyc::thing_is_not_abstract():
    assert not inspect.isabstract(yyc::Thing)


def test_yyc::thing_constructor_exists():
    assert callable(yyc::Thing.__init__)


def test_yyc::thing_constructor_args():
    sig = inspect.signature(yyc::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc::thing_has_id():
    assert hasattr(yyc::Thing, "id")
    descriptor = None
    for klass in yyc::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyc::blias_is_not_abstract():
    assert not inspect.isabstract(yyc::Blias)


def test_yyc::blias_constructor_exists():
    assert callable(yyc::Blias.__init__)


def test_yyc::blias_constructor_args():
    sig = inspect.signature(yyc::Blias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc::blias_has_id():
    assert hasattr(yyc::Blias, "id")
    descriptor = None
    for klass in yyc::Blias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyc::alias_is_not_abstract():
    assert not inspect.isabstract(yyc::Alias)


def test_yyc::alias_constructor_exists():
    assert callable(yyc::Alias.__init__)


def test_yyc::alias_constructor_args():
    sig = inspect.signature(yyc::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc::alias_has_id():
    assert hasattr(yyc::Alias, "id")
    descriptor = None
    for klass in yyc::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyc::relatedto_is_not_abstract():
    assert not inspect.isabstract(yyc::RelatedTo)


def test_yyc::relatedto_constructor_exists():
    assert callable(yyc::RelatedTo.__init__)


def test_yyc::relatedto_constructor_args():
    sig = inspect.signature(yyc::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyc::relatedto_has_since():
    assert hasattr(yyc::RelatedTo, "since")
    descriptor = None
    for klass in yyc::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
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
yyc::Thing_strategy = st.builds(
    yyc::Thing,
    id=
        st.integers()
)
yyc::Blias_strategy = st.builds(
    yyc::Blias,
    id=
        safe_text
)
yyc::Alias_strategy = st.builds(
    yyc::Alias,
    id=
        safe_text
)
yyc::RelatedTo_strategy = st.builds(
    yyc::RelatedTo,
    since=
        safe_text
)

@given(instance=yyc::Thing_strategy)
@settings(max_examples=50)
def test_yyc::thing_instantiation(instance):
    assert isinstance(instance, yyc::Thing)

@given(instance=yyc::Thing_strategy)
def test_yyc::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyc::Thing_strategy)
def test_yyc::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyc::Blias_strategy)
@settings(max_examples=50)
def test_yyc::blias_instantiation(instance):
    assert isinstance(instance, yyc::Blias)

@given(instance=yyc::Blias_strategy)
def test_yyc::blias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyc::Blias_strategy)
def test_yyc::blias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyc::Alias_strategy)
@settings(max_examples=50)
def test_yyc::alias_instantiation(instance):
    assert isinstance(instance, yyc::Alias)

@given(instance=yyc::Alias_strategy)
def test_yyc::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyc::Alias_strategy)
def test_yyc::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyc::RelatedTo_strategy)
@settings(max_examples=50)
def test_yyc::relatedto_instantiation(instance):
    assert isinstance(instance, yyc::RelatedTo)

@given(instance=yyc::RelatedTo_strategy)
def test_yyc::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyc::RelatedTo_strategy)
def test_yyc::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original
