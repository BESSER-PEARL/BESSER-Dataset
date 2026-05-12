import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nosql_Cell,
    ColumnFamily,
    nosql_Row,
    nosql_Column,
    nosql_PK,
    nosql_Options,
    nosql_ColumnFamily,
    nosql_Index,
    nosql_KeySpace,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nosql_cell_is_not_abstract():
    assert not inspect.isabstract(nosql_Cell)


def test_nosql_cell_constructor_exists():
    assert callable(nosql_Cell.__init__)


def test_nosql_cell_constructor_args():
    sig = inspect.signature(nosql_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nosql_cell_has_value():
    assert hasattr(nosql_Cell, "value")
    descriptor = None
    for klass in nosql_Cell.__mro__:
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



def test_nosql_row_is_not_abstract():
    assert not inspect.isabstract(nosql_Row)


def test_nosql_row_constructor_exists():
    assert callable(nosql_Row.__init__)


def test_nosql_row_constructor_args():
    sig = inspect.signature(nosql_Row.__init__)
    params = list(sig.parameters.keys())



def test_nosql_column_is_not_abstract():
    assert not inspect.isabstract(nosql_Column)


def test_nosql_column_constructor_exists():
    assert callable(nosql_Column.__init__)


def test_nosql_column_constructor_args():
    sig = inspect.signature(nosql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "name" in params, "Missing parameter 'name'"

def test_nosql_column_has_size():
    assert hasattr(nosql_Column, "size")
    descriptor = None
    for klass in nosql_Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_nosql_column_has_datatype():
    assert hasattr(nosql_Column, "datatype")
    descriptor = None
    for klass in nosql_Column.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_nosql_column_has_name():
    assert hasattr(nosql_Column, "name")
    descriptor = None
    for klass in nosql_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nosql_pk_is_not_abstract():
    assert not inspect.isabstract(nosql_PK)


def test_nosql_pk_constructor_exists():
    assert callable(nosql_PK.__init__)


def test_nosql_pk_constructor_args():
    sig = inspect.signature(nosql_PK.__init__)
    params = list(sig.parameters.keys())



def test_nosql_options_is_not_abstract():
    assert not inspect.isabstract(nosql_Options)


def test_nosql_options_constructor_exists():
    assert callable(nosql_Options.__init__)


def test_nosql_options_constructor_args():
    sig = inspect.signature(nosql_Options.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_nosql_options_has_name():
    assert hasattr(nosql_Options, "name")
    descriptor = None
    for klass in nosql_Options.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nosql_options_has_value():
    assert hasattr(nosql_Options, "value")
    descriptor = None
    for klass in nosql_Options.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nosql_columnfamily_is_not_abstract():
    assert not inspect.isabstract(nosql_ColumnFamily)


def test_nosql_columnfamily_constructor_exists():
    assert callable(nosql_ColumnFamily.__init__)


def test_nosql_columnfamily_constructor_args():
    sig = inspect.signature(nosql_ColumnFamily.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_nosql_columnfamily_has_comment():
    assert hasattr(nosql_ColumnFamily, "comment")
    descriptor = None
    for klass in nosql_ColumnFamily.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_nosql_columnfamily_has_name():
    assert hasattr(nosql_ColumnFamily, "name")
    descriptor = None
    for klass in nosql_ColumnFamily.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nosql_index_is_not_abstract():
    assert not inspect.isabstract(nosql_Index)


def test_nosql_index_constructor_exists():
    assert callable(nosql_Index.__init__)


def test_nosql_index_constructor_args():
    sig = inspect.signature(nosql_Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_nosql_index_has_name():
    assert hasattr(nosql_Index, "name")
    descriptor = None
    for klass in nosql_Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nosql_index_has_reference():
    assert hasattr(nosql_Index, "reference")
    descriptor = None
    for klass in nosql_Index.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_nosql_keyspace_is_not_abstract():
    assert not inspect.isabstract(nosql_KeySpace)


def test_nosql_keyspace_constructor_exists():
    assert callable(nosql_KeySpace.__init__)


def test_nosql_keyspace_constructor_args():
    sig = inspect.signature(nosql_KeySpace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nosql_keyspace_has_name():
    assert hasattr(nosql_KeySpace, "name")
    descriptor = None
    for klass in nosql_KeySpace.__mro__:
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
        "float",
        "timestamp",
        "text",
        "ascii",
        "double",
        "timeuuid",
        "varint",
        "blob",
        "bigint",
        "varchar",
        "decimal",
        "int",
        "boolean",
        "uuid",
        "counter",
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
nosql_Cell_strategy = st.builds(
    nosql_Cell,
    value=
        safe_text
)
ColumnFamily_strategy = st.builds(
    ColumnFamily,
)
nosql_Row_strategy = st.builds(
    nosql_Row,
)
nosql_Column_strategy = st.builds(
    nosql_Column,
    size=
        safe_text,
    datatype=
        safe_text,
    name=
        safe_text
)
nosql_PK_strategy = st.builds(
    nosql_PK,
)
nosql_Options_strategy = st.builds(
    nosql_Options,
    name=
        safe_text,
    value=
        safe_text
)
nosql_ColumnFamily_strategy = st.builds(
    nosql_ColumnFamily,
    comment=
        safe_text,
    name=
        safe_text
)
nosql_Index_strategy = st.builds(
    nosql_Index,
    name=
        safe_text,
    reference=
        safe_text
)
nosql_KeySpace_strategy = st.builds(
    nosql_KeySpace,
    name=
        safe_text
)

@given(instance=nosql_Cell_strategy)
@settings(max_examples=50)
def test_nosql_cell_instantiation(instance):
    assert isinstance(instance, nosql_Cell)



@given(instance=nosql_Cell_strategy)
def test_nosql_cell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ColumnFamily_strategy)
@settings(max_examples=50)
def test_columnfamily_instantiation(instance):
    assert isinstance(instance, ColumnFamily)

@given(instance=nosql_Row_strategy)
@settings(max_examples=50)
def test_nosql_row_instantiation(instance):
    assert isinstance(instance, nosql_Row)

@given(instance=nosql_Column_strategy)
@settings(max_examples=50)
def test_nosql_column_instantiation(instance):
    assert isinstance(instance, nosql_Column)



@given(instance=nosql_Column_strategy)
def test_nosql_column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=nosql_Column_strategy)
def test_nosql_column_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original



@given(instance=nosql_Column_strategy)
def test_nosql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql_PK_strategy)
@settings(max_examples=50)
def test_nosql_pk_instantiation(instance):
    assert isinstance(instance, nosql_PK)

@given(instance=nosql_Options_strategy)
@settings(max_examples=50)
def test_nosql_options_instantiation(instance):
    assert isinstance(instance, nosql_Options)



@given(instance=nosql_Options_strategy)
def test_nosql_options_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nosql_Options_strategy)
def test_nosql_options_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nosql_ColumnFamily_strategy)
@settings(max_examples=50)
def test_nosql_columnfamily_instantiation(instance):
    assert isinstance(instance, nosql_ColumnFamily)



@given(instance=nosql_ColumnFamily_strategy)
def test_nosql_columnfamily_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=nosql_ColumnFamily_strategy)
def test_nosql_columnfamily_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql_Index_strategy)
@settings(max_examples=50)
def test_nosql_index_instantiation(instance):
    assert isinstance(instance, nosql_Index)



@given(instance=nosql_Index_strategy)
def test_nosql_index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nosql_Index_strategy)
def test_nosql_index_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=nosql_KeySpace_strategy)
@settings(max_examples=50)
def test_nosql_keyspace_instantiation(instance):
    assert isinstance(instance, nosql_KeySpace)



@given(instance=nosql_KeySpace_strategy)
def test_nosql_keyspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
