import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplerdbms::RModelElement,
    RModelElement,
    simplerdbms::Key,
    simplerdbms::Table,
    simplerdbms::ForeignKey,
    simplerdbms::Schema,
    simplerdbms::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms::rmodelelement_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::RModelElement)


def test_simplerdbms::rmodelelement_constructor_exists():
    assert callable(simplerdbms::RModelElement.__init__)


def test_simplerdbms::rmodelelement_constructor_args():
    sig = inspect.signature(simplerdbms::RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_simplerdbms::rmodelelement_has_name():
    assert hasattr(simplerdbms::RModelElement, "name")
    descriptor = None
    for klass in simplerdbms::RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::rmodelelement_has_kind():
    assert hasattr(simplerdbms::RModelElement, "kind")
    descriptor = None
    for klass in simplerdbms::RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::key_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::Key)


def test_simplerdbms::key_constructor_exists():
    assert callable(simplerdbms::Key.__init__)


def test_simplerdbms::key_constructor_args():
    sig = inspect.signature(simplerdbms::Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(simplerdbms::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(simplerdbms::Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::ForeignKey)


def test_simplerdbms::foreignkey_constructor_exists():
    assert callable(simplerdbms::ForeignKey.__init__)


def test_simplerdbms::foreignkey_constructor_args():
    sig = inspect.signature(simplerdbms::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::schema_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::Schema)


def test_simplerdbms::schema_constructor_exists():
    assert callable(simplerdbms::Schema.__init__)


def test_simplerdbms::schema_constructor_args():
    sig = inspect.signature(simplerdbms::Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(simplerdbms::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(simplerdbms::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(simplerdbms::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms::column_has_type():
    assert hasattr(simplerdbms::Column, "type")
    descriptor = None
    for klass in simplerdbms::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
simplerdbms::RModelElement_strategy = st.builds(
    simplerdbms::RModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simplerdbms::Key_strategy = st.builds(
    simplerdbms::Key,
)
simplerdbms::Table_strategy = st.builds(
    simplerdbms::Table,
)
simplerdbms::ForeignKey_strategy = st.builds(
    simplerdbms::ForeignKey,
)
simplerdbms::Schema_strategy = st.builds(
    simplerdbms::Schema,
)
simplerdbms::Column_strategy = st.builds(
    simplerdbms::Column,
    type=
        safe_text
)

@given(instance=simplerdbms::RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms::rmodelelement_instantiation(instance):
    assert isinstance(instance, simplerdbms::RModelElement)

@given(instance=simplerdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplerdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplerdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simplerdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=simplerdbms::Key_strategy)
@settings(max_examples=50)
def test_simplerdbms::key_instantiation(instance):
    assert isinstance(instance, simplerdbms::Key)

@given(instance=simplerdbms::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, simplerdbms::Table)

@given(instance=simplerdbms::ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, simplerdbms::ForeignKey)

@given(instance=simplerdbms::Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms::schema_instantiation(instance):
    assert isinstance(instance, simplerdbms::Schema)

@given(instance=simplerdbms::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, simplerdbms::Column)

@given(instance=simplerdbms::Column_strategy)
def test_simplerdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simplerdbms::Column_strategy)
def test_simplerdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
