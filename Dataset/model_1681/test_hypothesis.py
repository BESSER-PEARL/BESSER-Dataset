import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Foo,
    yyd::Alias,
    yyd::Foo,
    yyd::RelatedTo,
    yyd::Thing,
    yyd::Blias,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foo_is_not_abstract():
    assert not inspect.isabstract(Foo)


def test_foo_constructor_exists():
    assert callable(Foo.__init__)


def test_foo_constructor_args():
    sig = inspect.signature(Foo.__init__)
    params = list(sig.parameters.keys())



def test_yyd::alias_is_not_abstract():
    assert not inspect.isabstract(yyd::Alias)


def test_yyd::alias_constructor_exists():
    assert callable(yyd::Alias.__init__)


def test_yyd::alias_constructor_args():
    sig = inspect.signature(yyd::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd::alias_has_id():
    assert hasattr(yyd::Alias, "id")
    descriptor = None
    for klass in yyd::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyd::foo_is_not_abstract():
    assert not inspect.isabstract(yyd::Foo)


def test_yyd::foo_constructor_exists():
    assert callable(yyd::Foo.__init__)


def test_yyd::foo_constructor_args():
    sig = inspect.signature(yyd::Foo.__init__)
    params = list(sig.parameters.keys())



def test_yyd::relatedto_is_not_abstract():
    assert not inspect.isabstract(yyd::RelatedTo)


def test_yyd::relatedto_constructor_exists():
    assert callable(yyd::RelatedTo.__init__)


def test_yyd::relatedto_constructor_args():
    sig = inspect.signature(yyd::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyd::relatedto_has_since():
    assert hasattr(yyd::RelatedTo, "since")
    descriptor = None
    for klass in yyd::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyd::thing_is_not_abstract():
    assert not inspect.isabstract(yyd::Thing)


def test_yyd::thing_constructor_exists():
    assert callable(yyd::Thing.__init__)


def test_yyd::thing_constructor_args():
    sig = inspect.signature(yyd::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd::thing_has_id():
    assert hasattr(yyd::Thing, "id")
    descriptor = None
    for klass in yyd::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyd::blias_is_not_abstract():
    assert not inspect.isabstract(yyd::Blias)


def test_yyd::blias_constructor_exists():
    assert callable(yyd::Blias.__init__)


def test_yyd::blias_constructor_args():
    sig = inspect.signature(yyd::Blias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd::blias_has_id():
    assert hasattr(yyd::Blias, "id")
    descriptor = None
    for klass in yyd::Blias.__mro__:
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
Foo_strategy = st.builds(
    Foo,
)
yyd::Alias_strategy = st.builds(
    yyd::Alias,
    id=
        safe_text
)
yyd::Foo_strategy = st.builds(
    yyd::Foo,
)
yyd::RelatedTo_strategy = st.builds(
    yyd::RelatedTo,
    since=
        safe_text
)
yyd::Thing_strategy = st.builds(
    yyd::Thing,
    id=
        st.integers()
)
yyd::Blias_strategy = st.builds(
    yyd::Blias,
    id=
        safe_text
)

@given(instance=Foo_strategy)
@settings(max_examples=50)
def test_foo_instantiation(instance):
    assert isinstance(instance, Foo)

@given(instance=yyd::Alias_strategy)
@settings(max_examples=50)
def test_yyd::alias_instantiation(instance):
    assert isinstance(instance, yyd::Alias)

@given(instance=yyd::Alias_strategy)
def test_yyd::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyd::Alias_strategy)
def test_yyd::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyd::Foo_strategy)
@settings(max_examples=50)
def test_yyd::foo_instantiation(instance):
    assert isinstance(instance, yyd::Foo)

@given(instance=yyd::RelatedTo_strategy)
@settings(max_examples=50)
def test_yyd::relatedto_instantiation(instance):
    assert isinstance(instance, yyd::RelatedTo)

@given(instance=yyd::RelatedTo_strategy)
def test_yyd::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyd::RelatedTo_strategy)
def test_yyd::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyd::Thing_strategy)
@settings(max_examples=50)
def test_yyd::thing_instantiation(instance):
    assert isinstance(instance, yyd::Thing)

@given(instance=yyd::Thing_strategy)
def test_yyd::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyd::Thing_strategy)
def test_yyd::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyd::Blias_strategy)
@settings(max_examples=50)
def test_yyd::blias_instantiation(instance):
    assert isinstance(instance, yyd::Blias)

@given(instance=yyd::Blias_strategy)
def test_yyd::blias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyd::Blias_strategy)
def test_yyd::blias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
