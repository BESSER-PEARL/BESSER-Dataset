import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdpl_RecordElement,
    rdpl_Record,
    rdpl_Column,
    rdpl_Type,
    rdpl_Table,
    rdpl_Schema,
    rdpl_ForeignKey,
    BasicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdpl_recordelement_is_not_abstract():
    assert not inspect.isabstract(rdpl_RecordElement)


def test_rdpl_recordelement_constructor_exists():
    assert callable(rdpl_RecordElement.__init__)


def test_rdpl_recordelement_constructor_args():
    sig = inspect.signature(rdpl_RecordElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rdpl_recordelement_has_value():
    assert hasattr(rdpl_RecordElement, "value")
    descriptor = None
    for klass in rdpl_RecordElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rdpl_record_is_not_abstract():
    assert not inspect.isabstract(rdpl_Record)


def test_rdpl_record_constructor_exists():
    assert callable(rdpl_Record.__init__)


def test_rdpl_record_constructor_args():
    sig = inspect.signature(rdpl_Record.__init__)
    params = list(sig.parameters.keys())



def test_rdpl_column_is_not_abstract():
    assert not inspect.isabstract(rdpl_Column)


def test_rdpl_column_constructor_exists():
    assert callable(rdpl_Column.__init__)


def test_rdpl_column_constructor_args():
    sig = inspect.signature(rdpl_Column.__init__)
    params = list(sig.parameters.keys())
    assert "ctype" in params, "Missing parameter 'ctype'"
    assert "stype" in params, "Missing parameter 'stype'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl_column_has_ctype():
    assert hasattr(rdpl_Column, "ctype")
    descriptor = None
    for klass in rdpl_Column.__mro__:
        if "ctype" in klass.__dict__:
            descriptor = klass.__dict__["ctype"]
            break
    assert isinstance(descriptor, property)

def test_rdpl_column_has_stype():
    assert hasattr(rdpl_Column, "stype")
    descriptor = None
    for klass in rdpl_Column.__mro__:
        if "stype" in klass.__dict__:
            descriptor = klass.__dict__["stype"]
            break
    assert isinstance(descriptor, property)

def test_rdpl_column_has_name():
    assert hasattr(rdpl_Column, "name")
    descriptor = None
    for klass in rdpl_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl_type_is_not_abstract():
    assert not inspect.isabstract(rdpl_Type)


def test_rdpl_type_constructor_exists():
    assert callable(rdpl_Type.__init__)


def test_rdpl_type_constructor_args():
    sig = inspect.signature(rdpl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl_type_has_name():
    assert hasattr(rdpl_Type, "name")
    descriptor = None
    for klass in rdpl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl_table_is_not_abstract():
    assert not inspect.isabstract(rdpl_Table)


def test_rdpl_table_constructor_exists():
    assert callable(rdpl_Table.__init__)


def test_rdpl_table_constructor_args():
    sig = inspect.signature(rdpl_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl_table_has_name():
    assert hasattr(rdpl_Table, "name")
    descriptor = None
    for klass in rdpl_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl_schema_is_not_abstract():
    assert not inspect.isabstract(rdpl_Schema)


def test_rdpl_schema_constructor_exists():
    assert callable(rdpl_Schema.__init__)


def test_rdpl_schema_constructor_args():
    sig = inspect.signature(rdpl_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl_schema_has_name():
    assert hasattr(rdpl_Schema, "name")
    descriptor = None
    for klass in rdpl_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdpl_ForeignKey)


def test_rdpl_foreignkey_constructor_exists():
    assert callable(rdpl_ForeignKey.__init__)


def test_rdpl_foreignkey_constructor_args():
    sig = inspect.signature(rdpl_ForeignKey.__init__)
    params = list(sig.parameters.keys())

def test_basictype_exists():
    # Check that the Enumeration exists
    assert BasicType is not None

def test_basictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicType]
    expected_literals = [
        "BOOL",
        "INT",
        "CHAR",
        "REAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicType"


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
rdpl_RecordElement_strategy = st.builds(
    rdpl_RecordElement,
    value=
        safe_text
)
rdpl_Record_strategy = st.builds(
    rdpl_Record,
)
rdpl_Column_strategy = st.builds(
    rdpl_Column,
    ctype=
        safe_text,
    stype=
        safe_text,
    name=
        safe_text
)
rdpl_Type_strategy = st.builds(
    rdpl_Type,
    name=
        safe_text
)
rdpl_Table_strategy = st.builds(
    rdpl_Table,
    name=
        safe_text
)
rdpl_Schema_strategy = st.builds(
    rdpl_Schema,
    name=
        safe_text
)
rdpl_ForeignKey_strategy = st.builds(
    rdpl_ForeignKey,
)

@given(instance=rdpl_RecordElement_strategy)
@settings(max_examples=50)
def test_rdpl_recordelement_instantiation(instance):
    assert isinstance(instance, rdpl_RecordElement)



@given(instance=rdpl_RecordElement_strategy)
def test_rdpl_recordelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rdpl_Record_strategy)
@settings(max_examples=50)
def test_rdpl_record_instantiation(instance):
    assert isinstance(instance, rdpl_Record)

@given(instance=rdpl_Column_strategy)
@settings(max_examples=50)
def test_rdpl_column_instantiation(instance):
    assert isinstance(instance, rdpl_Column)



@given(instance=rdpl_Column_strategy)
def test_rdpl_column_ctype_setter(instance):
    original = instance.ctype
    instance.ctype = original
    assert instance.ctype == original



@given(instance=rdpl_Column_strategy)
def test_rdpl_column_stype_setter(instance):
    original = instance.stype
    instance.stype = original
    assert instance.stype == original



@given(instance=rdpl_Column_strategy)
def test_rdpl_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl_Type_strategy)
@settings(max_examples=50)
def test_rdpl_type_instantiation(instance):
    assert isinstance(instance, rdpl_Type)



@given(instance=rdpl_Type_strategy)
def test_rdpl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl_Table_strategy)
@settings(max_examples=50)
def test_rdpl_table_instantiation(instance):
    assert isinstance(instance, rdpl_Table)



@given(instance=rdpl_Table_strategy)
def test_rdpl_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl_Schema_strategy)
@settings(max_examples=50)
def test_rdpl_schema_instantiation(instance):
    assert isinstance(instance, rdpl_Schema)



@given(instance=rdpl_Schema_strategy)
def test_rdpl_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdpl_foreignkey_instantiation(instance):
    assert isinstance(instance, rdpl_ForeignKey)
