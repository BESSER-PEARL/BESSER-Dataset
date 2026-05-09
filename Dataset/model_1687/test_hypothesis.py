import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yye::Foo,
    NamedElement,
    yye::Relation,
    yye::Base,
    yye::Alias,
    yye::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yye::foo_is_not_abstract():
    assert not inspect.isabstract(yye::Foo)


def test_yye::foo_constructor_exists():
    assert callable(yye::Foo.__init__)


def test_yye::foo_constructor_args():
    sig = inspect.signature(yye::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye::foo_has_id():
    assert hasattr(yye::Foo, "id")
    descriptor = None
    for klass in yye::Foo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_yye::relation_is_not_abstract():
    assert not inspect.isabstract(yye::Relation)


def test_yye::relation_constructor_exists():
    assert callable(yye::Relation.__init__)


def test_yye::relation_constructor_args():
    sig = inspect.signature(yye::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yye::relation_has_since():
    assert hasattr(yye::Relation, "since")
    descriptor = None
    for klass in yye::Relation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yye::base_is_not_abstract():
    assert not inspect.isabstract(yye::Base)


def test_yye::base_constructor_exists():
    assert callable(yye::Base.__init__)


def test_yye::base_constructor_args():
    sig = inspect.signature(yye::Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye::base_has_id():
    assert hasattr(yye::Base, "id")
    descriptor = None
    for klass in yye::Base.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yye::alias_is_not_abstract():
    assert not inspect.isabstract(yye::Alias)


def test_yye::alias_constructor_exists():
    assert callable(yye::Alias.__init__)


def test_yye::alias_constructor_args():
    sig = inspect.signature(yye::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye::alias_has_id():
    assert hasattr(yye::Alias, "id")
    descriptor = None
    for klass in yye::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yye::namedelement_is_not_abstract():
    assert not inspect.isabstract(yye::NamedElement)


def test_yye::namedelement_constructor_exists():
    assert callable(yye::NamedElement.__init__)


def test_yye::namedelement_constructor_args():
    sig = inspect.signature(yye::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yye::namedelement_has_name():
    assert hasattr(yye::NamedElement, "name")
    descriptor = None
    for klass in yye::NamedElement.__mro__:
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
yye::Foo_strategy = st.builds(
    yye::Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yye::Relation_strategy = st.builds(
    yye::Relation,
    since=
        safe_text
)
yye::Base_strategy = st.builds(
    yye::Base,
    id=
        st.integers()
)
yye::Alias_strategy = st.builds(
    yye::Alias,
    id=
        safe_text
)
yye::NamedElement_strategy = st.builds(
    yye::NamedElement,
    name=
        safe_text
)

@given(instance=yye::Foo_strategy)
@settings(max_examples=50)
def test_yye::foo_instantiation(instance):
    assert isinstance(instance, yye::Foo)

@given(instance=yye::Foo_strategy)
def test_yye::foo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yye::Foo_strategy)
def test_yye::foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yye::Relation_strategy)
@settings(max_examples=50)
def test_yye::relation_instantiation(instance):
    assert isinstance(instance, yye::Relation)

@given(instance=yye::Relation_strategy)
def test_yye::relation_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yye::Relation_strategy)
def test_yye::relation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yye::Base_strategy)
@settings(max_examples=50)
def test_yye::base_instantiation(instance):
    assert isinstance(instance, yye::Base)

@given(instance=yye::Base_strategy)
def test_yye::base_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yye::Base_strategy)
def test_yye::base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yye::Alias_strategy)
@settings(max_examples=50)
def test_yye::alias_instantiation(instance):
    assert isinstance(instance, yye::Alias)

@given(instance=yye::Alias_strategy)
def test_yye::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yye::Alias_strategy)
def test_yye::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yye::NamedElement_strategy)
@settings(max_examples=50)
def test_yye::namedelement_instantiation(instance):
    assert isinstance(instance, yye::NamedElement)

@given(instance=yye::NamedElement_strategy)
def test_yye::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yye::NamedElement_strategy)
def test_yye::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
