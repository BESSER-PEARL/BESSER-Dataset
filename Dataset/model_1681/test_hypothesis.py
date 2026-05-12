import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Foo,
    yyd_Alias,
    yyd_Foo,
    yyd_RelatedTo,
    yyd_Thing,
    yyd_Blias,
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



def test_yyd_alias_is_not_abstract():
    assert not inspect.isabstract(yyd_Alias)


def test_yyd_alias_constructor_exists():
    assert callable(yyd_Alias.__init__)


def test_yyd_alias_constructor_args():
    sig = inspect.signature(yyd_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd_alias_has_id():
    assert hasattr(yyd_Alias, "id")
    descriptor = None
    for klass in yyd_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyd_foo_is_not_abstract():
    assert not inspect.isabstract(yyd_Foo)


def test_yyd_foo_constructor_exists():
    assert callable(yyd_Foo.__init__)


def test_yyd_foo_constructor_args():
    sig = inspect.signature(yyd_Foo.__init__)
    params = list(sig.parameters.keys())



def test_yyd_relatedto_is_not_abstract():
    assert not inspect.isabstract(yyd_RelatedTo)


def test_yyd_relatedto_constructor_exists():
    assert callable(yyd_RelatedTo.__init__)


def test_yyd_relatedto_constructor_args():
    sig = inspect.signature(yyd_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyd_relatedto_has_since():
    assert hasattr(yyd_RelatedTo, "since")
    descriptor = None
    for klass in yyd_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyd_thing_is_not_abstract():
    assert not inspect.isabstract(yyd_Thing)


def test_yyd_thing_constructor_exists():
    assert callable(yyd_Thing.__init__)


def test_yyd_thing_constructor_args():
    sig = inspect.signature(yyd_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd_thing_has_id():
    assert hasattr(yyd_Thing, "id")
    descriptor = None
    for klass in yyd_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyd_blias_is_not_abstract():
    assert not inspect.isabstract(yyd_Blias)


def test_yyd_blias_constructor_exists():
    assert callable(yyd_Blias.__init__)


def test_yyd_blias_constructor_args():
    sig = inspect.signature(yyd_Blias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyd_blias_has_id():
    assert hasattr(yyd_Blias, "id")
    descriptor = None
    for klass in yyd_Blias.__mro__:
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
yyd_Alias_strategy = st.builds(
    yyd_Alias,
    id=
        safe_text
)
yyd_Foo_strategy = st.builds(
    yyd_Foo,
)
yyd_RelatedTo_strategy = st.builds(
    yyd_RelatedTo,
    since=
        safe_text
)
yyd_Thing_strategy = st.builds(
    yyd_Thing,
    id=
        st.integers()
)
yyd_Blias_strategy = st.builds(
    yyd_Blias,
    id=
        safe_text
)

@given(instance=Foo_strategy)
@settings(max_examples=50)
def test_foo_instantiation(instance):
    assert isinstance(instance, Foo)

@given(instance=yyd_Alias_strategy)
@settings(max_examples=50)
def test_yyd_alias_instantiation(instance):
    assert isinstance(instance, yyd_Alias)



@given(instance=yyd_Alias_strategy)
def test_yyd_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyd_Foo_strategy)
@settings(max_examples=50)
def test_yyd_foo_instantiation(instance):
    assert isinstance(instance, yyd_Foo)

@given(instance=yyd_RelatedTo_strategy)
@settings(max_examples=50)
def test_yyd_relatedto_instantiation(instance):
    assert isinstance(instance, yyd_RelatedTo)



@given(instance=yyd_RelatedTo_strategy)
def test_yyd_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyd_Thing_strategy)
@settings(max_examples=50)
def test_yyd_thing_instantiation(instance):
    assert isinstance(instance, yyd_Thing)



@given(instance=yyd_Thing_strategy)
def test_yyd_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyd_Blias_strategy)
@settings(max_examples=50)
def test_yyd_blias_instantiation(instance):
    assert isinstance(instance, yyd_Blias)



@given(instance=yyd_Blias_strategy)
def test_yyd_blias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
