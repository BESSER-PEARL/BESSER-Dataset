import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    my_FKRelation,
    NamedElement,
    my_Database,
    my_Table,
    my_Column,
    my_NamedElement,
    ColumnType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_my_fkrelation_is_not_abstract():
    assert not inspect.isabstract(my_FKRelation)


def test_my_fkrelation_constructor_exists():
    assert callable(my_FKRelation.__init__)


def test_my_fkrelation_constructor_args():
    sig = inspect.signature(my_FKRelation.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_my_fkrelation_has_label():
    assert hasattr(my_FKRelation, "label")
    descriptor = None
    for klass in my_FKRelation.__mro__:
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



def test_my_database_is_not_abstract():
    assert not inspect.isabstract(my_Database)


def test_my_database_constructor_exists():
    assert callable(my_Database.__init__)


def test_my_database_constructor_args():
    sig = inspect.signature(my_Database.__init__)
    params = list(sig.parameters.keys())



def test_my_table_is_not_abstract():
    assert not inspect.isabstract(my_Table)


def test_my_table_constructor_exists():
    assert callable(my_Table.__init__)


def test_my_table_constructor_args():
    sig = inspect.signature(my_Table.__init__)
    params = list(sig.parameters.keys())



def test_my_column_is_not_abstract():
    assert not inspect.isabstract(my_Column)


def test_my_column_constructor_exists():
    assert callable(my_Column.__init__)


def test_my_column_constructor_args():
    sig = inspect.signature(my_Column.__init__)
    params = list(sig.parameters.keys())
    assert "primary" in params, "Missing parameter 'primary'"
    assert "type" in params, "Missing parameter 'type'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "size" in params, "Missing parameter 'size'"

def test_my_column_has_primary():
    assert hasattr(my_Column, "primary")
    descriptor = None
    for klass in my_Column.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)

def test_my_column_has_type():
    assert hasattr(my_Column, "type")
    descriptor = None
    for klass in my_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_my_column_has_unique():
    assert hasattr(my_Column, "unique")
    descriptor = None
    for klass in my_Column.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_my_column_has_size():
    assert hasattr(my_Column, "size")
    descriptor = None
    for klass in my_Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_my_namedelement_is_not_abstract():
    assert not inspect.isabstract(my_NamedElement)


def test_my_namedelement_constructor_exists():
    assert callable(my_NamedElement.__init__)


def test_my_namedelement_constructor_args():
    sig = inspect.signature(my_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_my_namedelement_has_name():
    assert hasattr(my_NamedElement, "name")
    descriptor = None
    for klass in my_NamedElement.__mro__:
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
        "Number",
        "Date",
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
my_FKRelation_strategy = st.builds(
    my_FKRelation,
    label=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
my_Database_strategy = st.builds(
    my_Database,
)
my_Table_strategy = st.builds(
    my_Table,
)
my_Column_strategy = st.builds(
    my_Column,
    primary=
        st.booleans(),
    type=
        safe_text,
    unique=
        st.booleans(),
    size=
        st.integers()
)
my_NamedElement_strategy = st.builds(
    my_NamedElement,
    name=
        safe_text
)

@given(instance=my_FKRelation_strategy)
@settings(max_examples=50)
def test_my_fkrelation_instantiation(instance):
    assert isinstance(instance, my_FKRelation)



@given(instance=my_FKRelation_strategy)
def test_my_fkrelation_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=my_Database_strategy)
@settings(max_examples=50)
def test_my_database_instantiation(instance):
    assert isinstance(instance, my_Database)

@given(instance=my_Table_strategy)
@settings(max_examples=50)
def test_my_table_instantiation(instance):
    assert isinstance(instance, my_Table)

@given(instance=my_Column_strategy)
@settings(max_examples=50)
def test_my_column_instantiation(instance):
    assert isinstance(instance, my_Column)



@given(instance=my_Column_strategy)
def test_my_column_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original



@given(instance=my_Column_strategy)
def test_my_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=my_Column_strategy)
def test_my_column_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=my_Column_strategy)
def test_my_column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=my_NamedElement_strategy)
@settings(max_examples=50)
def test_my_namedelement_instantiation(instance):
    assert isinstance(instance, my_NamedElement)



@given(instance=my_NamedElement_strategy)
def test_my_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
