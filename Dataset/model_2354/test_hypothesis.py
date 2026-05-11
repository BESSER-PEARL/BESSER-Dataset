import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleRdbms::RModelElement,
    RModelElement,
    simpleRdbms::ForeignKey,
    simpleRdbms::Key,
    simpleRdbms::Table,
    simpleRdbms::Column,
    simpleRdbms::Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms::rmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::RModelElement)


def test_simplerdbms::rmodelelement_constructor_exists():
    assert callable(simpleRdbms::RModelElement.__init__)


def test_simplerdbms::rmodelelement_constructor_args():
    sig = inspect.signature(simpleRdbms::RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_simplerdbms::rmodelelement_has_name():
    assert hasattr(simpleRdbms::RModelElement, "name")
    descriptor = None
    for klass in simpleRdbms::RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::rmodelelement_has_kind():
    assert hasattr(simpleRdbms::RModelElement, "kind")
    descriptor = None
    for klass in simpleRdbms::RModelElement.__mro__:
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



def test_simplerdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::ForeignKey)


def test_simplerdbms::foreignkey_constructor_exists():
    assert callable(simpleRdbms::ForeignKey.__init__)


def test_simplerdbms::foreignkey_constructor_args():
    sig = inspect.signature(simpleRdbms::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::key_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::Key)


def test_simplerdbms::key_constructor_exists():
    assert callable(simpleRdbms::Key.__init__)


def test_simplerdbms::key_constructor_args():
    sig = inspect.signature(simpleRdbms::Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(simpleRdbms::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(simpleRdbms::Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(simpleRdbms::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(simpleRdbms::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms::column_has_type():
    assert hasattr(simpleRdbms::Column, "type")
    descriptor = None
    for klass in simpleRdbms::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms::schema_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms::Schema)


def test_simplerdbms::schema_constructor_exists():
    assert callable(simpleRdbms::Schema.__init__)


def test_simplerdbms::schema_constructor_args():
    sig = inspect.signature(simpleRdbms::Schema.__init__)
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
simpleRdbms::RModelElement_strategy = st.builds(
    simpleRdbms::RModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simpleRdbms::ForeignKey_strategy = st.builds(
    simpleRdbms::ForeignKey,
)
simpleRdbms::Key_strategy = st.builds(
    simpleRdbms::Key,
)
simpleRdbms::Table_strategy = st.builds(
    simpleRdbms::Table,
)
simpleRdbms::Column_strategy = st.builds(
    simpleRdbms::Column,
    type=
        safe_text
)
simpleRdbms::Schema_strategy = st.builds(
    simpleRdbms::Schema,
)

@given(instance=simpleRdbms::RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms::rmodelelement_instantiation(instance):
    assert isinstance(instance, simpleRdbms::RModelElement)

@given(instance=simpleRdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleRdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleRdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simpleRdbms::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=simpleRdbms::ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, simpleRdbms::ForeignKey)

@given(instance=simpleRdbms::Key_strategy)
@settings(max_examples=50)
def test_simplerdbms::key_instantiation(instance):
    assert isinstance(instance, simpleRdbms::Key)

@given(instance=simpleRdbms::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, simpleRdbms::Table)

@given(instance=simpleRdbms::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, simpleRdbms::Column)

@given(instance=simpleRdbms::Column_strategy)
def test_simplerdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simpleRdbms::Column_strategy)
def test_simplerdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simpleRdbms::Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms::schema_instantiation(instance):
    assert isinstance(instance, simpleRdbms::Schema)
