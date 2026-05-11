import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbms::RModelElement,
    RModelElement,
    rdbms::Table,
    rdbms::ForeignKey,
    rdbms::Schema,
    rdbms::Column,
    rdbms::Key,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms::rmodelelement_is_not_abstract():
    assert not inspect.isabstract(rdbms::RModelElement)


def test_rdbms::rmodelelement_constructor_exists():
    assert callable(rdbms::RModelElement.__init__)


def test_rdbms::rmodelelement_constructor_args():
    sig = inspect.signature(rdbms::RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::rmodelelement_has_kind():
    assert hasattr(rdbms::RModelElement, "kind")
    descriptor = None
    for klass in rdbms::RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rmodelelement_has_name():
    assert hasattr(rdbms::RModelElement, "name")
    descriptor = None
    for klass in rdbms::RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::table_is_not_abstract():
    assert not inspect.isabstract(rdbms::Table)


def test_rdbms::table_constructor_exists():
    assert callable(rdbms::Table.__init__)


def test_rdbms::table_constructor_args():
    sig = inspect.signature(rdbms::Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms::ForeignKey)


def test_rdbms::foreignkey_constructor_exists():
    assert callable(rdbms::ForeignKey.__init__)


def test_rdbms::foreignkey_constructor_args():
    sig = inspect.signature(rdbms::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::schema_is_not_abstract():
    assert not inspect.isabstract(rdbms::Schema)


def test_rdbms::schema_constructor_exists():
    assert callable(rdbms::Schema.__init__)


def test_rdbms::schema_constructor_args():
    sig = inspect.signature(rdbms::Schema.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::column_is_not_abstract():
    assert not inspect.isabstract(rdbms::Column)


def test_rdbms::column_constructor_exists():
    assert callable(rdbms::Column.__init__)


def test_rdbms::column_constructor_args():
    sig = inspect.signature(rdbms::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms::column_has_type():
    assert hasattr(rdbms::Column, "type")
    descriptor = None
    for klass in rdbms::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::key_is_not_abstract():
    assert not inspect.isabstract(rdbms::Key)


def test_rdbms::key_constructor_exists():
    assert callable(rdbms::Key.__init__)


def test_rdbms::key_constructor_args():
    sig = inspect.signature(rdbms::Key.__init__)
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
rdbms::RModelElement_strategy = st.builds(
    rdbms::RModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
rdbms::Table_strategy = st.builds(
    rdbms::Table,
)
rdbms::ForeignKey_strategy = st.builds(
    rdbms::ForeignKey,
)
rdbms::Schema_strategy = st.builds(
    rdbms::Schema,
)
rdbms::Column_strategy = st.builds(
    rdbms::Column,
    type=
        safe_text
)
rdbms::Key_strategy = st.builds(
    rdbms::Key,
)

@given(instance=rdbms::RModelElement_strategy)
@settings(max_examples=50)
def test_rdbms::rmodelelement_instantiation(instance):
    assert isinstance(instance, rdbms::RModelElement)

@given(instance=rdbms::RModelElement_strategy)
def test_rdbms::rmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::RModelElement_strategy)
def test_rdbms::rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::RModelElement_strategy)
def test_rdbms::rmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::RModelElement_strategy)
def test_rdbms::rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=rdbms::Table_strategy)
@settings(max_examples=50)
def test_rdbms::table_instantiation(instance):
    assert isinstance(instance, rdbms::Table)

@given(instance=rdbms::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms::ForeignKey)

@given(instance=rdbms::Schema_strategy)
@settings(max_examples=50)
def test_rdbms::schema_instantiation(instance):
    assert isinstance(instance, rdbms::Schema)

@given(instance=rdbms::Column_strategy)
@settings(max_examples=50)
def test_rdbms::column_instantiation(instance):
    assert isinstance(instance, rdbms::Column)

@given(instance=rdbms::Column_strategy)
def test_rdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdbms::Column_strategy)
def test_rdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbms::Key_strategy)
@settings(max_examples=50)
def test_rdbms::key_instantiation(instance):
    assert isinstance(instance, rdbms::Key)
