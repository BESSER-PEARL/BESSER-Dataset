import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    relational::ModelElement,
    ModelElement,
    relational::Column,
    relational::ForeignKey,
    relational::Database,
    relational::Table,
    relational::Schema,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::modelelement_is_not_abstract():
    assert not inspect.isabstract(relational::ModelElement)


def test_relational::modelelement_constructor_exists():
    assert callable(relational::ModelElement.__init__)


def test_relational::modelelement_constructor_args():
    sig = inspect.signature(relational::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_relational::modelelement_has_comment():
    assert hasattr(relational::ModelElement, "comment")
    descriptor = None
    for klass in relational::ModelElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(relational::Column)


def test_relational::column_constructor_exists():
    assert callable(relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(relational::Column.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational::column_has_isUnique():
    assert hasattr(relational::Column, "isUnique")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_isPrimaryKey():
    assert hasattr(relational::Column, "isPrimaryKey")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_type():
    assert hasattr(relational::Column, "type")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_name():
    assert hasattr(relational::Column, "name")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::foreignkey_has_name():
    assert hasattr(relational::ForeignKey, "name")
    descriptor = None
    for klass in relational::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::database_is_not_abstract():
    assert not inspect.isabstract(relational::Database)


def test_relational::database_constructor_exists():
    assert callable(relational::Database.__init__)


def test_relational::database_constructor_args():
    sig = inspect.signature(relational::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_relational::database_has_name():
    assert hasattr(relational::Database, "name")
    descriptor = None
    for klass in relational::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational::database_has_url():
    assert hasattr(relational::Database, "url")
    descriptor = None
    for klass in relational::Database.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(relational::Table)


def test_relational::table_constructor_exists():
    assert callable(relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(relational::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::table_has_name():
    assert hasattr(relational::Table, "name")
    descriptor = None
    for klass in relational::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(relational::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::schema_has_name():
    assert hasattr(relational::Schema, "name")
    descriptor = None
    for klass in relational::Schema.__mro__:
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
        "DATE",
        "CHAR",
        "FLOAT",
        "TIME",
        "VARCHAR",
        "NUMERIC",
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
relational::ModelElement_strategy = st.builds(
    relational::ModelElement,
    comment=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
relational::Column_strategy = st.builds(
    relational::Column,
    isUnique=
        st.booleans(),
    isPrimaryKey=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text
)
relational::ForeignKey_strategy = st.builds(
    relational::ForeignKey,
    name=
        safe_text
)
relational::Database_strategy = st.builds(
    relational::Database,
    name=
        safe_text,
    url=
        safe_text
)
relational::Table_strategy = st.builds(
    relational::Table,
    name=
        safe_text
)
relational::Schema_strategy = st.builds(
    relational::Schema,
    name=
        safe_text
)

@given(instance=relational::ModelElement_strategy)
@settings(max_examples=50)
def test_relational::modelelement_instantiation(instance):
    assert isinstance(instance, relational::ModelElement)

@given(instance=relational::ModelElement_strategy)
def test_relational::modelelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=relational::ModelElement_strategy)
def test_relational::modelelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Column_strategy)
def test_relational::column_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=relational::Column_strategy)
def test_relational::column_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=relational::Column_strategy)
def test_relational::column_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=relational::Column_strategy)
def test_relational::column_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=relational::Column_strategy)
def test_relational::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=relational::Column_strategy)
def test_relational::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=relational::Column_strategy)
def test_relational::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Column_strategy)
def test_relational::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::ForeignKey)

@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Database_strategy)
@settings(max_examples=50)
def test_relational::database_instantiation(instance):
    assert isinstance(instance, relational::Database)

@given(instance=relational::Database_strategy)
def test_relational::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Database_strategy)
def test_relational::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Database_strategy)
def test_relational::database_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=relational::Database_strategy)
def test_relational::database_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=relational::Table_strategy)
def test_relational::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Table_strategy)
def test_relational::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, relational::Schema)

@given(instance=relational::Schema_strategy)
def test_relational::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Schema_strategy)
def test_relational::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
