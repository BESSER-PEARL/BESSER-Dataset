import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yyc_Blias,
    yyc_Alias,
    yyc_RelatedTo,
    yyc_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyc_blias_is_not_abstract():
    assert not inspect.isabstract(yyc_Blias)


def test_yyc_blias_constructor_exists():
    assert callable(yyc_Blias.__init__)


def test_yyc_blias_constructor_args():
    sig = inspect.signature(yyc_Blias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc_blias_has_id():
    assert hasattr(yyc_Blias, "id")
    descriptor = None
    for klass in yyc_Blias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyc_alias_is_not_abstract():
    assert not inspect.isabstract(yyc_Alias)


def test_yyc_alias_constructor_exists():
    assert callable(yyc_Alias.__init__)


def test_yyc_alias_constructor_args():
    sig = inspect.signature(yyc_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc_alias_has_id():
    assert hasattr(yyc_Alias, "id")
    descriptor = None
    for klass in yyc_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyc_relatedto_is_not_abstract():
    assert not inspect.isabstract(yyc_RelatedTo)


def test_yyc_relatedto_constructor_exists():
    assert callable(yyc_RelatedTo.__init__)


def test_yyc_relatedto_constructor_args():
    sig = inspect.signature(yyc_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyc_relatedto_has_since():
    assert hasattr(yyc_RelatedTo, "since")
    descriptor = None
    for klass in yyc_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyc_thing_is_not_abstract():
    assert not inspect.isabstract(yyc_Thing)


def test_yyc_thing_constructor_exists():
    assert callable(yyc_Thing.__init__)


def test_yyc_thing_constructor_args():
    sig = inspect.signature(yyc_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyc_thing_has_id():
    assert hasattr(yyc_Thing, "id")
    descriptor = None
    for klass in yyc_Thing.__mro__:
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
yyc_Blias_strategy = st.builds(
    yyc_Blias,
    id=
        safe_text
)
yyc_Alias_strategy = st.builds(
    yyc_Alias,
    id=
        safe_text
)
yyc_RelatedTo_strategy = st.builds(
    yyc_RelatedTo,
    since=
        safe_text
)
yyc_Thing_strategy = st.builds(
    yyc_Thing,
    id=
        st.integers()
)

@given(instance=yyc_Blias_strategy)
@settings(max_examples=50)
def test_yyc_blias_instantiation(instance):
    assert isinstance(instance, yyc_Blias)



@given(instance=yyc_Blias_strategy)
def test_yyc_blias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyc_Alias_strategy)
@settings(max_examples=50)
def test_yyc_alias_instantiation(instance):
    assert isinstance(instance, yyc_Alias)



@given(instance=yyc_Alias_strategy)
def test_yyc_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyc_RelatedTo_strategy)
@settings(max_examples=50)
def test_yyc_relatedto_instantiation(instance):
    assert isinstance(instance, yyc_RelatedTo)



@given(instance=yyc_RelatedTo_strategy)
def test_yyc_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyc_Thing_strategy)
@settings(max_examples=50)
def test_yyc_thing_instantiation(instance):
    assert isinstance(instance, yyc_Thing)



@given(instance=yyc_Thing_strategy)
def test_yyc_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
