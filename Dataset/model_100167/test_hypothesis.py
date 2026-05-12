import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ForeignKey,
    Key,
    Column,
    Schema,
    Table,
    RModelElement,
    SimpleRDBMS::Table,
    SimpleRDBMS::Key,
    SimpleRDBMS::Column,
    SimpleRDBMS::ForeignKey,
    SimpleRDBMS::Schema,
    SimpleRDBMS::RModelElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ForeignKey)


def test_foreignkey_constructor_exists():
    assert callable(ForeignKey.__init__)


def test_foreignkey_constructor_args():
    sig = inspect.signature(ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(SimpleRDBMS::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::key_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Key)


def test_simplerdbms::key_constructor_exists():
    assert callable(SimpleRDBMS::Key.__init__)


def test_simplerdbms::key_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(SimpleRDBMS::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms::column_has_type():
    assert hasattr(SimpleRDBMS::Column, "type")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::ForeignKey)


def test_simplerdbms::foreignkey_constructor_exists():
    assert callable(SimpleRDBMS::ForeignKey.__init__)


def test_simplerdbms::foreignkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::schema_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Schema)


def test_simplerdbms::schema_constructor_exists():
    assert callable(SimpleRDBMS::Schema.__init__)


def test_simplerdbms::schema_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RModelElement)


def test_simplerdbms::rmodelelement_constructor_exists():
    assert callable(SimpleRDBMS::RModelElement.__init__)


def test_simplerdbms::rmodelelement_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms::rmodelelement_has_kind():
    assert hasattr(SimpleRDBMS::RModelElement, "kind")
    descriptor = None
    for klass in SimpleRDBMS::RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::rmodelelement_has_name():
    assert hasattr(SimpleRDBMS::RModelElement, "name")
    descriptor = None
    for klass in SimpleRDBMS::RModelElement.__mro__:
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
ForeignKey_strategy = st.builds(
    ForeignKey,
)
Key_strategy = st.builds(
    Key,
)
Column_strategy = st.builds(
    Column,
)
Schema_strategy = st.builds(
    Schema,
)
Table_strategy = st.builds(
    Table,
)
RModelElement_strategy = st.builds(
    RModelElement,
)
SimpleRDBMS::Table_strategy = st.builds(
    SimpleRDBMS::Table,
)
SimpleRDBMS::Key_strategy = st.builds(
    SimpleRDBMS::Key,
)
SimpleRDBMS::Column_strategy = st.builds(
    SimpleRDBMS::Column,
    type=
        safe_text
)
SimpleRDBMS::ForeignKey_strategy = st.builds(
    SimpleRDBMS::ForeignKey,
)
SimpleRDBMS::Schema_strategy = st.builds(
    SimpleRDBMS::Schema,
)
SimpleRDBMS::RModelElement_strategy = st.builds(
    SimpleRDBMS::RModelElement,
    kind=
        safe_text,
    name=
        safe_text
)

@given(instance=ForeignKey_strategy)
@settings(max_examples=50)
def test_foreignkey_instantiation(instance):
    assert isinstance(instance, ForeignKey)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=SimpleRDBMS::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Table)

@given(instance=SimpleRDBMS::Key_strategy)
@settings(max_examples=50)
def test_simplerdbms::key_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Key)

@given(instance=SimpleRDBMS::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Column)

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SimpleRDBMS::ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::ForeignKey)

@given(instance=SimpleRDBMS::Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms::schema_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Schema)

@given(instance=SimpleRDBMS::RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms::rmodelelement_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RModelElement)

@given(instance=SimpleRDBMS::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=SimpleRDBMS::RModelElement_strategy)
def test_simplerdbms::rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=SimpleRDBMS::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::RModelElement_strategy)
def test_simplerdbms::rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
