import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdpl::RecordElement,
    rdpl::Record,
    rdpl::Column,
    rdpl::Type,
    rdpl::Table,
    rdpl::Schema,
    rdpl::ForeignKey,
    BasicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdpl::recordelement_is_not_abstract():
    assert not inspect.isabstract(rdpl::RecordElement)


def test_rdpl::recordelement_constructor_exists():
    assert callable(rdpl::RecordElement.__init__)


def test_rdpl::recordelement_constructor_args():
    sig = inspect.signature(rdpl::RecordElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rdpl::recordelement_has_value():
    assert hasattr(rdpl::RecordElement, "value")
    descriptor = None
    for klass in rdpl::RecordElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rdpl::record_is_not_abstract():
    assert not inspect.isabstract(rdpl::Record)


def test_rdpl::record_constructor_exists():
    assert callable(rdpl::Record.__init__)


def test_rdpl::record_constructor_args():
    sig = inspect.signature(rdpl::Record.__init__)
    params = list(sig.parameters.keys())



def test_rdpl::column_is_not_abstract():
    assert not inspect.isabstract(rdpl::Column)


def test_rdpl::column_constructor_exists():
    assert callable(rdpl::Column.__init__)


def test_rdpl::column_constructor_args():
    sig = inspect.signature(rdpl::Column.__init__)
    params = list(sig.parameters.keys())
    assert "stype" in params, "Missing parameter 'stype'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ctype" in params, "Missing parameter 'ctype'"

def test_rdpl::column_has_stype():
    assert hasattr(rdpl::Column, "stype")
    descriptor = None
    for klass in rdpl::Column.__mro__:
        if "stype" in klass.__dict__:
            descriptor = klass.__dict__["stype"]
            break
    assert isinstance(descriptor, property)

def test_rdpl::column_has_name():
    assert hasattr(rdpl::Column, "name")
    descriptor = None
    for klass in rdpl::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdpl::column_has_ctype():
    assert hasattr(rdpl::Column, "ctype")
    descriptor = None
    for klass in rdpl::Column.__mro__:
        if "ctype" in klass.__dict__:
            descriptor = klass.__dict__["ctype"]
            break
    assert isinstance(descriptor, property)



def test_rdpl::type_is_not_abstract():
    assert not inspect.isabstract(rdpl::Type)


def test_rdpl::type_constructor_exists():
    assert callable(rdpl::Type.__init__)


def test_rdpl::type_constructor_args():
    sig = inspect.signature(rdpl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl::type_has_name():
    assert hasattr(rdpl::Type, "name")
    descriptor = None
    for klass in rdpl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl::table_is_not_abstract():
    assert not inspect.isabstract(rdpl::Table)


def test_rdpl::table_constructor_exists():
    assert callable(rdpl::Table.__init__)


def test_rdpl::table_constructor_args():
    sig = inspect.signature(rdpl::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl::table_has_name():
    assert hasattr(rdpl::Table, "name")
    descriptor = None
    for klass in rdpl::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl::schema_is_not_abstract():
    assert not inspect.isabstract(rdpl::Schema)


def test_rdpl::schema_constructor_exists():
    assert callable(rdpl::Schema.__init__)


def test_rdpl::schema_constructor_args():
    sig = inspect.signature(rdpl::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdpl::schema_has_name():
    assert hasattr(rdpl::Schema, "name")
    descriptor = None
    for klass in rdpl::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdpl::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdpl::ForeignKey)


def test_rdpl::foreignkey_constructor_exists():
    assert callable(rdpl::ForeignKey.__init__)


def test_rdpl::foreignkey_constructor_args():
    sig = inspect.signature(rdpl::ForeignKey.__init__)
    params = list(sig.parameters.keys())

def test_basictype_exists():
    # Check that the Enumeration exists
    assert BasicType is not None

def test_basictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicType]
    expected_literals = [
        "INT",
        "CHAR",
        "REAL",
        "BOOL",
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
rdpl::RecordElement_strategy = st.builds(
    rdpl::RecordElement,
    value=
        safe_text
)
rdpl::Record_strategy = st.builds(
    rdpl::Record,
)
rdpl::Column_strategy = st.builds(
    rdpl::Column,
    stype=
        safe_text,
    name=
        safe_text,
    ctype=
        safe_text
)
rdpl::Type_strategy = st.builds(
    rdpl::Type,
    name=
        safe_text
)
rdpl::Table_strategy = st.builds(
    rdpl::Table,
    name=
        safe_text
)
rdpl::Schema_strategy = st.builds(
    rdpl::Schema,
    name=
        safe_text
)
rdpl::ForeignKey_strategy = st.builds(
    rdpl::ForeignKey,
)

@given(instance=rdpl::RecordElement_strategy)
@settings(max_examples=50)
def test_rdpl::recordelement_instantiation(instance):
    assert isinstance(instance, rdpl::RecordElement)

@given(instance=rdpl::RecordElement_strategy)
def test_rdpl::recordelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=rdpl::RecordElement_strategy)
def test_rdpl::recordelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rdpl::Record_strategy)
@settings(max_examples=50)
def test_rdpl::record_instantiation(instance):
    assert isinstance(instance, rdpl::Record)

@given(instance=rdpl::Column_strategy)
@settings(max_examples=50)
def test_rdpl::column_instantiation(instance):
    assert isinstance(instance, rdpl::Column)

@given(instance=rdpl::Column_strategy)
def test_rdpl::column_stype_type(instance):
    assert isinstance(instance.stype, str)


@given(instance=rdpl::Column_strategy)
def test_rdpl::column_stype_setter(instance):
    original = instance.stype
    instance.stype = original
    assert instance.stype == original

@given(instance=rdpl::Column_strategy)
def test_rdpl::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdpl::Column_strategy)
def test_rdpl::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl::Column_strategy)
def test_rdpl::column_ctype_type(instance):
    assert isinstance(instance.ctype, str)


@given(instance=rdpl::Column_strategy)
def test_rdpl::column_ctype_setter(instance):
    original = instance.ctype
    instance.ctype = original
    assert instance.ctype == original

@given(instance=rdpl::Type_strategy)
@settings(max_examples=50)
def test_rdpl::type_instantiation(instance):
    assert isinstance(instance, rdpl::Type)

@given(instance=rdpl::Type_strategy)
def test_rdpl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdpl::Type_strategy)
def test_rdpl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl::Table_strategy)
@settings(max_examples=50)
def test_rdpl::table_instantiation(instance):
    assert isinstance(instance, rdpl::Table)

@given(instance=rdpl::Table_strategy)
def test_rdpl::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdpl::Table_strategy)
def test_rdpl::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl::Schema_strategy)
@settings(max_examples=50)
def test_rdpl::schema_instantiation(instance):
    assert isinstance(instance, rdpl::Schema)

@given(instance=rdpl::Schema_strategy)
def test_rdpl::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdpl::Schema_strategy)
def test_rdpl::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdpl::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdpl::foreignkey_instantiation(instance):
    assert isinstance(instance, rdpl::ForeignKey)
