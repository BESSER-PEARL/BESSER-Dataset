import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ddl_DataElement,
    DataElement,
    ddl_DataType,
    ddl_Table,
    ddl_Column,
    ddl_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ddl_dataelement_is_not_abstract():
    assert not inspect.isabstract(ddl_DataElement)


def test_ddl_dataelement_constructor_exists():
    assert callable(ddl_DataElement.__init__)


def test_ddl_dataelement_constructor_args():
    sig = inspect.signature(ddl_DataElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddl_dataelement_has_name():
    assert hasattr(ddl_DataElement, "name")
    descriptor = None
    for klass in ddl_DataElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataelement_is_not_abstract():
    assert not inspect.isabstract(DataElement)


def test_dataelement_constructor_exists():
    assert callable(DataElement.__init__)


def test_dataelement_constructor_args():
    sig = inspect.signature(DataElement.__init__)
    params = list(sig.parameters.keys())



def test_ddl_datatype_is_not_abstract():
    assert not inspect.isabstract(ddl_DataType)


def test_ddl_datatype_constructor_exists():
    assert callable(ddl_DataType.__init__)


def test_ddl_datatype_constructor_args():
    sig = inspect.signature(ddl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_table_is_not_abstract():
    assert not inspect.isabstract(ddl_Table)


def test_ddl_table_constructor_exists():
    assert callable(ddl_Table.__init__)


def test_ddl_table_constructor_args():
    sig = inspect.signature(ddl_Table.__init__)
    params = list(sig.parameters.keys())



def test_ddl_column_is_not_abstract():
    assert not inspect.isabstract(ddl_Column)


def test_ddl_column_constructor_exists():
    assert callable(ddl_Column.__init__)


def test_ddl_column_constructor_args():
    sig = inspect.signature(ddl_Column.__init__)
    params = list(sig.parameters.keys())



def test_ddl_schema_is_not_abstract():
    assert not inspect.isabstract(ddl_Schema)


def test_ddl_schema_constructor_exists():
    assert callable(ddl_Schema.__init__)


def test_ddl_schema_constructor_args():
    sig = inspect.signature(ddl_Schema.__init__)
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
ddl_DataElement_strategy = st.builds(
    ddl_DataElement,
    name=
        safe_text
)
DataElement_strategy = st.builds(
    DataElement,
)
ddl_DataType_strategy = st.builds(
    ddl_DataType,
)
ddl_Table_strategy = st.builds(
    ddl_Table,
)
ddl_Column_strategy = st.builds(
    ddl_Column,
)
ddl_Schema_strategy = st.builds(
    ddl_Schema,
)

@given(instance=ddl_DataElement_strategy)
@settings(max_examples=50)
def test_ddl_dataelement_instantiation(instance):
    assert isinstance(instance, ddl_DataElement)



@given(instance=ddl_DataElement_strategy)
def test_ddl_dataelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataElement_strategy)
@settings(max_examples=50)
def test_dataelement_instantiation(instance):
    assert isinstance(instance, DataElement)

@given(instance=ddl_DataType_strategy)
@settings(max_examples=50)
def test_ddl_datatype_instantiation(instance):
    assert isinstance(instance, ddl_DataType)

@given(instance=ddl_Table_strategy)
@settings(max_examples=50)
def test_ddl_table_instantiation(instance):
    assert isinstance(instance, ddl_Table)

@given(instance=ddl_Column_strategy)
@settings(max_examples=50)
def test_ddl_column_instantiation(instance):
    assert isinstance(instance, ddl_Column)

@given(instance=ddl_Schema_strategy)
@settings(max_examples=50)
def test_ddl_schema_instantiation(instance):
    assert isinstance(instance, ddl_Schema)
