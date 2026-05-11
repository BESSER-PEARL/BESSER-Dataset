import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    my::FKRelation,
    NamedElement,
    my::Database,
    my::Table,
    my::Column,
    my::NamedElement,
    ColumnType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_my::fkrelation_is_not_abstract():
    assert not inspect.isabstract(my::FKRelation)


def test_my::fkrelation_constructor_exists():
    assert callable(my::FKRelation.__init__)


def test_my::fkrelation_constructor_args():
    sig = inspect.signature(my::FKRelation.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_my::fkrelation_has_label():
    assert hasattr(my::FKRelation, "label")
    descriptor = None
    for klass in my::FKRelation.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_my::database_is_not_abstract():
    assert not inspect.isabstract(my::Database)


def test_my::database_constructor_exists():
    assert callable(my::Database.__init__)


def test_my::database_constructor_args():
    sig = inspect.signature(my::Database.__init__)
    params = list(sig.parameters.keys())



def test_my::table_is_not_abstract():
    assert not inspect.isabstract(my::Table)


def test_my::table_constructor_exists():
    assert callable(my::Table.__init__)


def test_my::table_constructor_args():
    sig = inspect.signature(my::Table.__init__)
    params = list(sig.parameters.keys())



def test_my::column_is_not_abstract():
    assert not inspect.isabstract(my::Column)


def test_my::column_constructor_exists():
    assert callable(my::Column.__init__)


def test_my::column_constructor_args():
    sig = inspect.signature(my::Column.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "type" in params, "Missing parameter 'type'"
    assert "size" in params, "Missing parameter 'size'"
    assert "primary" in params, "Missing parameter 'primary'"

def test_my::column_has_unique():
    assert hasattr(my::Column, "unique")
    descriptor = None
    for klass in my::Column.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_my::column_has_type():
    assert hasattr(my::Column, "type")
    descriptor = None
    for klass in my::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_my::column_has_size():
    assert hasattr(my::Column, "size")
    descriptor = None
    for klass in my::Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_my::column_has_primary():
    assert hasattr(my::Column, "primary")
    descriptor = None
    for klass in my::Column.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)



def test_my::namedelement_is_not_abstract():
    assert not inspect.isabstract(my::NamedElement)


def test_my::namedelement_constructor_exists():
    assert callable(my::NamedElement.__init__)


def test_my::namedelement_constructor_args():
    sig = inspect.signature(my::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_my::namedelement_has_name():
    assert hasattr(my::NamedElement, "name")
    descriptor = None
    for klass in my::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "Char",
        "Date",
        "Number",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"


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
my::FKRelation_strategy = st.builds(
    my::FKRelation,
    label=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
my::Database_strategy = st.builds(
    my::Database,
)
my::Table_strategy = st.builds(
    my::Table,
)
my::Column_strategy = st.builds(
    my::Column,
    unique=
        st.booleans(),
    type=
        safe_text,
    size=
        st.integers(),
    primary=
        st.booleans()
)
my::NamedElement_strategy = st.builds(
    my::NamedElement,
    name=
        safe_text
)

@given(instance=my::FKRelation_strategy)
@settings(max_examples=50)
def test_my::fkrelation_instantiation(instance):
    assert isinstance(instance, my::FKRelation)

@given(instance=my::FKRelation_strategy)
def test_my::fkrelation_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=my::FKRelation_strategy)
def test_my::fkrelation_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=my::Database_strategy)
@settings(max_examples=50)
def test_my::database_instantiation(instance):
    assert isinstance(instance, my::Database)

@given(instance=my::Table_strategy)
@settings(max_examples=50)
def test_my::table_instantiation(instance):
    assert isinstance(instance, my::Table)

@given(instance=my::Column_strategy)
@settings(max_examples=50)
def test_my::column_instantiation(instance):
    assert isinstance(instance, my::Column)

@given(instance=my::Column_strategy)
def test_my::column_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=my::Column_strategy)
def test_my::column_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=my::Column_strategy)
def test_my::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=my::Column_strategy)
def test_my::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=my::Column_strategy)
def test_my::column_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=my::Column_strategy)
def test_my::column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=my::Column_strategy)
def test_my::column_primary_type(instance):
    assert isinstance(instance.primary, bool)


@given(instance=my::Column_strategy)
def test_my::column_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original

@given(instance=my::NamedElement_strategy)
@settings(max_examples=50)
def test_my::namedelement_instantiation(instance):
    assert isinstance(instance, my::NamedElement)

@given(instance=my::NamedElement_strategy)
def test_my::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=my::NamedElement_strategy)
def test_my::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
