import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ddl::DataElement,
    DataElement,
    ddl::Table,
    ddl::DataType,
    ddl::Schema,
    ddl::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ddl::dataelement_is_not_abstract():
    assert not inspect.isabstract(ddl::DataElement)


def test_ddl::dataelement_constructor_exists():
    assert callable(ddl::DataElement.__init__)


def test_ddl::dataelement_constructor_args():
    sig = inspect.signature(ddl::DataElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddl::dataelement_has_name():
    assert hasattr(ddl::DataElement, "name")
    descriptor = None
    for klass in ddl::DataElement.__mro__:
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



def test_ddl::table_is_not_abstract():
    assert not inspect.isabstract(ddl::Table)


def test_ddl::table_constructor_exists():
    assert callable(ddl::Table.__init__)


def test_ddl::table_constructor_args():
    sig = inspect.signature(ddl::Table.__init__)
    params = list(sig.parameters.keys())



def test_ddl::datatype_is_not_abstract():
    assert not inspect.isabstract(ddl::DataType)


def test_ddl::datatype_constructor_exists():
    assert callable(ddl::DataType.__init__)


def test_ddl::datatype_constructor_args():
    sig = inspect.signature(ddl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_ddl::schema_is_not_abstract():
    assert not inspect.isabstract(ddl::Schema)


def test_ddl::schema_constructor_exists():
    assert callable(ddl::Schema.__init__)


def test_ddl::schema_constructor_args():
    sig = inspect.signature(ddl::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "conformite" in params, "Missing parameter 'conformite'"
    assert "prix" in params, "Missing parameter 'prix'"

def test_ddl::schema_has_version():
    assert hasattr(ddl::Schema, "version")
    descriptor = None
    for klass in ddl::Schema.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ddl::schema_has_conformite():
    assert hasattr(ddl::Schema, "conformite")
    descriptor = None
    for klass in ddl::Schema.__mro__:
        if "conformite" in klass.__dict__:
            descriptor = klass.__dict__["conformite"]
            break
    assert isinstance(descriptor, property)

def test_ddl::schema_has_prix():
    assert hasattr(ddl::Schema, "prix")
    descriptor = None
    for klass in ddl::Schema.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)



def test_ddl::column_is_not_abstract():
    assert not inspect.isabstract(ddl::Column)


def test_ddl::column_constructor_exists():
    assert callable(ddl::Column.__init__)


def test_ddl::column_constructor_args():
    sig = inspect.signature(ddl::Column.__init__)
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
ddl::DataElement_strategy = st.builds(
    ddl::DataElement,
    name=
        safe_text
)
DataElement_strategy = st.builds(
    DataElement,
)
ddl::Table_strategy = st.builds(
    ddl::Table,
)
ddl::DataType_strategy = st.builds(
    ddl::DataType,
)
ddl::Schema_strategy = st.builds(
    ddl::Schema,
    version=
        st.integers(),
    conformite=
        st.booleans(),
    prix=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ddl::Column_strategy = st.builds(
    ddl::Column,
)

@given(instance=ddl::DataElement_strategy)
@settings(max_examples=50)
def test_ddl::dataelement_instantiation(instance):
    assert isinstance(instance, ddl::DataElement)

@given(instance=ddl::DataElement_strategy)
def test_ddl::dataelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddl::DataElement_strategy)
def test_ddl::dataelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataElement_strategy)
@settings(max_examples=50)
def test_dataelement_instantiation(instance):
    assert isinstance(instance, DataElement)

@given(instance=ddl::Table_strategy)
@settings(max_examples=50)
def test_ddl::table_instantiation(instance):
    assert isinstance(instance, ddl::Table)

@given(instance=ddl::DataType_strategy)
@settings(max_examples=50)
def test_ddl::datatype_instantiation(instance):
    assert isinstance(instance, ddl::DataType)

@given(instance=ddl::Schema_strategy)
@settings(max_examples=50)
def test_ddl::schema_instantiation(instance):
    assert isinstance(instance, ddl::Schema)

@given(instance=ddl::Schema_strategy)
def test_ddl::schema_version_type(instance):
    assert isinstance(instance.version, int)


@given(instance=ddl::Schema_strategy)
def test_ddl::schema_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=ddl::Schema_strategy)
def test_ddl::schema_conformite_type(instance):
    assert isinstance(instance.conformite, bool)


@given(instance=ddl::Schema_strategy)
def test_ddl::schema_conformite_setter(instance):
    original = instance.conformite
    instance.conformite = original
    assert instance.conformite == original

@given(instance=ddl::Schema_strategy)
def test_ddl::schema_prix_type(instance):
    assert isinstance(instance.prix, float)


@given(instance=ddl::Schema_strategy)
def test_ddl::schema_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original

@given(instance=ddl::Column_strategy)
@settings(max_examples=50)
def test_ddl::column_instantiation(instance):
    assert isinstance(instance, ddl::Column)
