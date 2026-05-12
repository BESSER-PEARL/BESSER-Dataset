import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ForeignKey,
    Key,
    Column,
    Schema,
    Table,
    RModelElement,
    SimpleRDBMS_Table,
    SimpleRDBMS_ForeignKey,
    SimpleRDBMS_Column,
    SimpleRDBMS_Key,
    SimpleRDBMS_Schema,
    SimpleRDBMS_RModelElement,
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



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(SimpleRDBMS_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_ForeignKey)


def test_simplerdbms_foreignkey_constructor_exists():
    assert callable(SimpleRDBMS_ForeignKey.__init__)


def test_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(SimpleRDBMS_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms_column_has_type():
    assert hasattr(SimpleRDBMS_Column, "type")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Key)


def test_simplerdbms_key_constructor_exists():
    assert callable(SimpleRDBMS_Key.__init__)


def test_simplerdbms_key_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Schema)


def test_simplerdbms_schema_constructor_exists():
    assert callable(SimpleRDBMS_Schema.__init__)


def test_simplerdbms_schema_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RModelElement)


def test_simplerdbms_rmodelelement_constructor_exists():
    assert callable(SimpleRDBMS_RModelElement.__init__)


def test_simplerdbms_rmodelelement_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_rmodelelement_has_kind():
    assert hasattr(SimpleRDBMS_RModelElement, "kind")
    descriptor = None
    for klass in SimpleRDBMS_RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_rmodelelement_has_name():
    assert hasattr(SimpleRDBMS_RModelElement, "name")
    descriptor = None
    for klass in SimpleRDBMS_RModelElement.__mro__:
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
SimpleRDBMS_Table_strategy = st.builds(
    SimpleRDBMS_Table,
)
SimpleRDBMS_ForeignKey_strategy = st.builds(
    SimpleRDBMS_ForeignKey,
)
SimpleRDBMS_Column_strategy = st.builds(
    SimpleRDBMS_Column,
    type=
        safe_text
)
SimpleRDBMS_Key_strategy = st.builds(
    SimpleRDBMS_Key,
)
SimpleRDBMS_Schema_strategy = st.builds(
    SimpleRDBMS_Schema,
)
SimpleRDBMS_RModelElement_strategy = st.builds(
    SimpleRDBMS_RModelElement,
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

@given(instance=SimpleRDBMS_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Table)

@given(instance=SimpleRDBMS_ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_ForeignKey)

@given(instance=SimpleRDBMS_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Column)



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SimpleRDBMS_Key_strategy)
@settings(max_examples=50)
def test_simplerdbms_key_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Key)

@given(instance=SimpleRDBMS_Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms_schema_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Schema)

@given(instance=SimpleRDBMS_RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms_rmodelelement_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RModelElement)



@given(instance=SimpleRDBMS_RModelElement_strategy)
def test_simplerdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=SimpleRDBMS_RModelElement_strategy)
def test_simplerdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
