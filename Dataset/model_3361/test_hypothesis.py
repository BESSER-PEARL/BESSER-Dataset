import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    nosql::Cell,
    ColumnFamily,
    nosql::Row,
    nosql::Column,
    nosql::PK,
    nosql::Options,
    nosql::ColumnFamily,
    nosql::Index,
    nosql::KeySpace,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nosql::cell_is_not_abstract():
    assert not inspect.isabstract(nosql::Cell)


def test_nosql::cell_constructor_exists():
    assert callable(nosql::Cell.__init__)


def test_nosql::cell_constructor_args():
    sig = inspect.signature(nosql::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nosql::cell_has_value():
    assert hasattr(nosql::Cell, "value")
    descriptor = None
    for klass in nosql::Cell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_columnfamily_is_not_abstract():
    assert not inspect.isabstract(ColumnFamily)


def test_columnfamily_constructor_exists():
    assert callable(ColumnFamily.__init__)


def test_columnfamily_constructor_args():
    sig = inspect.signature(ColumnFamily.__init__)
    params = list(sig.parameters.keys())



def test_nosql::row_is_not_abstract():
    assert not inspect.isabstract(nosql::Row)


def test_nosql::row_constructor_exists():
    assert callable(nosql::Row.__init__)


def test_nosql::row_constructor_args():
    sig = inspect.signature(nosql::Row.__init__)
    params = list(sig.parameters.keys())



def test_nosql::column_is_not_abstract():
    assert not inspect.isabstract(nosql::Column)


def test_nosql::column_constructor_exists():
    assert callable(nosql::Column.__init__)


def test_nosql::column_constructor_args():
    sig = inspect.signature(nosql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::column_has_size():
    assert hasattr(nosql::Column, "size")
    descriptor = None
    for klass in nosql::Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_nosql::column_has_datatype():
    assert hasattr(nosql::Column, "datatype")
    descriptor = None
    for klass in nosql::Column.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_nosql::column_has_name():
    assert hasattr(nosql::Column, "name")
    descriptor = None
    for klass in nosql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nosql::pk_is_not_abstract():
    assert not inspect.isabstract(nosql::PK)


def test_nosql::pk_constructor_exists():
    assert callable(nosql::PK.__init__)


def test_nosql::pk_constructor_args():
    sig = inspect.signature(nosql::PK.__init__)
    params = list(sig.parameters.keys())



def test_nosql::options_is_not_abstract():
    assert not inspect.isabstract(nosql::Options)


def test_nosql::options_constructor_exists():
    assert callable(nosql::Options.__init__)


def test_nosql::options_constructor_args():
    sig = inspect.signature(nosql::Options.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_nosql::options_has_name():
    assert hasattr(nosql::Options, "name")
    descriptor = None
    for klass in nosql::Options.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nosql::options_has_value():
    assert hasattr(nosql::Options, "value")
    descriptor = None
    for klass in nosql::Options.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nosql::columnfamily_is_not_abstract():
    assert not inspect.isabstract(nosql::ColumnFamily)


def test_nosql::columnfamily_constructor_exists():
    assert callable(nosql::ColumnFamily.__init__)


def test_nosql::columnfamily_constructor_args():
    sig = inspect.signature(nosql::ColumnFamily.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::columnfamily_has_comment():
    assert hasattr(nosql::ColumnFamily, "comment")
    descriptor = None
    for klass in nosql::ColumnFamily.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_nosql::columnfamily_has_name():
    assert hasattr(nosql::ColumnFamily, "name")
    descriptor = None
    for klass in nosql::ColumnFamily.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nosql::index_is_not_abstract():
    assert not inspect.isabstract(nosql::Index)


def test_nosql::index_constructor_exists():
    assert callable(nosql::Index.__init__)


def test_nosql::index_constructor_args():
    sig = inspect.signature(nosql::Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_nosql::index_has_name():
    assert hasattr(nosql::Index, "name")
    descriptor = None
    for klass in nosql::Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nosql::index_has_reference():
    assert hasattr(nosql::Index, "reference")
    descriptor = None
    for klass in nosql::Index.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_nosql::keyspace_is_not_abstract():
    assert not inspect.isabstract(nosql::KeySpace)


def test_nosql::keyspace_constructor_exists():
    assert callable(nosql::KeySpace.__init__)


def test_nosql::keyspace_constructor_args():
    sig = inspect.signature(nosql::KeySpace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::keyspace_has_name():
    assert hasattr(nosql::KeySpace, "name")
    descriptor = None
    for klass in nosql::KeySpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "varint",
        "bigint",
        "blob",
        "int",
        "uuid",
        "double",
        "ascii",
        "decimal",
        "counter",
        "text",
        "timestamp",
        "float",
        "boolean",
        "varchar",
        "timeuuid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
nosql::Cell_strategy = st.builds(
    nosql::Cell,
    value=
        safe_text
)
ColumnFamily_strategy = st.builds(
    ColumnFamily,
)
nosql::Row_strategy = st.builds(
    nosql::Row,
)
nosql::Column_strategy = st.builds(
    nosql::Column,
    size=
        safe_text,
    datatype=
        safe_text,
    name=
        safe_text
)
nosql::PK_strategy = st.builds(
    nosql::PK,
)
nosql::Options_strategy = st.builds(
    nosql::Options,
    name=
        safe_text,
    value=
        safe_text
)
nosql::ColumnFamily_strategy = st.builds(
    nosql::ColumnFamily,
    comment=
        safe_text,
    name=
        safe_text
)
nosql::Index_strategy = st.builds(
    nosql::Index,
    name=
        safe_text,
    reference=
        safe_text
)
nosql::KeySpace_strategy = st.builds(
    nosql::KeySpace,
    name=
        safe_text
)

@given(instance=nosql::Cell_strategy)
@settings(max_examples=50)
def test_nosql::cell_instantiation(instance):
    assert isinstance(instance, nosql::Cell)

@given(instance=nosql::Cell_strategy)
def test_nosql::cell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=nosql::Cell_strategy)
def test_nosql::cell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ColumnFamily_strategy)
@settings(max_examples=50)
def test_columnfamily_instantiation(instance):
    assert isinstance(instance, ColumnFamily)

@given(instance=nosql::Row_strategy)
@settings(max_examples=50)
def test_nosql::row_instantiation(instance):
    assert isinstance(instance, nosql::Row)

@given(instance=nosql::Column_strategy)
@settings(max_examples=50)
def test_nosql::column_instantiation(instance):
    assert isinstance(instance, nosql::Column)

@given(instance=nosql::Column_strategy)
def test_nosql::column_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=nosql::Column_strategy)
def test_nosql::column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=nosql::Column_strategy)
def test_nosql::column_datatype_type(instance):
    assert isinstance(instance.datatype, str)


@given(instance=nosql::Column_strategy)
def test_nosql::column_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original

@given(instance=nosql::Column_strategy)
def test_nosql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::Column_strategy)
def test_nosql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql::PK_strategy)
@settings(max_examples=50)
def test_nosql::pk_instantiation(instance):
    assert isinstance(instance, nosql::PK)

@given(instance=nosql::Options_strategy)
@settings(max_examples=50)
def test_nosql::options_instantiation(instance):
    assert isinstance(instance, nosql::Options)

@given(instance=nosql::Options_strategy)
def test_nosql::options_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::Options_strategy)
def test_nosql::options_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql::Options_strategy)
def test_nosql::options_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=nosql::Options_strategy)
def test_nosql::options_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nosql::ColumnFamily_strategy)
@settings(max_examples=50)
def test_nosql::columnfamily_instantiation(instance):
    assert isinstance(instance, nosql::ColumnFamily)

@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql::Index_strategy)
@settings(max_examples=50)
def test_nosql::index_instantiation(instance):
    assert isinstance(instance, nosql::Index)

@given(instance=nosql::Index_strategy)
def test_nosql::index_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::Index_strategy)
def test_nosql::index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql::Index_strategy)
def test_nosql::index_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=nosql::Index_strategy)
def test_nosql::index_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=nosql::KeySpace_strategy)
@settings(max_examples=50)
def test_nosql::keyspace_instantiation(instance):
    assert isinstance(instance, nosql::KeySpace)

@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
