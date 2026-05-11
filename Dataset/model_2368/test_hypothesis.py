import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    relational::obeo::ModelElement,
    ModelElement,
    relational::obeo::Column,
    relational::obeo::Table,
    relational::obeo::ForeignKey,
    relational::obeo::Schema,
    relational::obeo::Database,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::obeo::modelelement_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::ModelElement)


def test_relational::obeo::modelelement_constructor_exists():
    assert callable(relational::obeo::ModelElement.__init__)


def test_relational::obeo::modelelement_constructor_args():
    sig = inspect.signature(relational::obeo::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_relational::obeo::modelelement_has_comment():
    assert hasattr(relational::obeo::ModelElement, "comment")
    descriptor = None
    for klass in relational::obeo::ModelElement.__mro__:
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



def test_relational::obeo::column_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::Column)


def test_relational::obeo::column_constructor_exists():
    assert callable(relational::obeo::Column.__init__)


def test_relational::obeo::column_constructor_args():
    sig = inspect.signature(relational::obeo::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational::obeo::column_has_type():
    assert hasattr(relational::obeo::Column, "type")
    descriptor = None
    for klass in relational::obeo::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_relational::obeo::column_has_isPrimaryKey():
    assert hasattr(relational::obeo::Column, "isPrimaryKey")
    descriptor = None
    for klass in relational::obeo::Column.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_relational::obeo::column_has_isUnique():
    assert hasattr(relational::obeo::Column, "isUnique")
    descriptor = None
    for klass in relational::obeo::Column.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_relational::obeo::column_has_name():
    assert hasattr(relational::obeo::Column, "name")
    descriptor = None
    for klass in relational::obeo::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::obeo::table_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::Table)


def test_relational::obeo::table_constructor_exists():
    assert callable(relational::obeo::Table.__init__)


def test_relational::obeo::table_constructor_args():
    sig = inspect.signature(relational::obeo::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::obeo::table_has_name():
    assert hasattr(relational::obeo::Table, "name")
    descriptor = None
    for klass in relational::obeo::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::obeo::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::ForeignKey)


def test_relational::obeo::foreignkey_constructor_exists():
    assert callable(relational::obeo::ForeignKey.__init__)


def test_relational::obeo::foreignkey_constructor_args():
    sig = inspect.signature(relational::obeo::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::obeo::foreignkey_has_name():
    assert hasattr(relational::obeo::ForeignKey, "name")
    descriptor = None
    for klass in relational::obeo::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::obeo::schema_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::Schema)


def test_relational::obeo::schema_constructor_exists():
    assert callable(relational::obeo::Schema.__init__)


def test_relational::obeo::schema_constructor_args():
    sig = inspect.signature(relational::obeo::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::obeo::schema_has_name():
    assert hasattr(relational::obeo::Schema, "name")
    descriptor = None
    for klass in relational::obeo::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::obeo::database_is_not_abstract():
    assert not inspect.isabstract(relational::obeo::Database)


def test_relational::obeo::database_constructor_exists():
    assert callable(relational::obeo::Database.__init__)


def test_relational::obeo::database_constructor_args():
    sig = inspect.signature(relational::obeo::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_relational::obeo::database_has_name():
    assert hasattr(relational::obeo::Database, "name")
    descriptor = None
    for klass in relational::obeo::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational::obeo::database_has_url():
    assert hasattr(relational::obeo::Database, "url")
    descriptor = None
    for klass in relational::obeo::Database.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "TIME",
        "FLOAT",
        "DATE",
        "NUMERIC",
        "VARCHAR",
        "CHAR",
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
relational::obeo::ModelElement_strategy = st.builds(
    relational::obeo::ModelElement,
    comment=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
relational::obeo::Column_strategy = st.builds(
    relational::obeo::Column,
    type=
        safe_text,
    isPrimaryKey=
        st.booleans(),
    isUnique=
        st.booleans(),
    name=
        safe_text
)
relational::obeo::Table_strategy = st.builds(
    relational::obeo::Table,
    name=
        safe_text
)
relational::obeo::ForeignKey_strategy = st.builds(
    relational::obeo::ForeignKey,
    name=
        safe_text
)
relational::obeo::Schema_strategy = st.builds(
    relational::obeo::Schema,
    name=
        safe_text
)
relational::obeo::Database_strategy = st.builds(
    relational::obeo::Database,
    name=
        safe_text,
    url=
        safe_text
)

@given(instance=relational::obeo::ModelElement_strategy)
@settings(max_examples=50)
def test_relational::obeo::modelelement_instantiation(instance):
    assert isinstance(instance, relational::obeo::ModelElement)

@given(instance=relational::obeo::ModelElement_strategy)
def test_relational::obeo::modelelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=relational::obeo::ModelElement_strategy)
def test_relational::obeo::modelelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=relational::obeo::Column_strategy)
@settings(max_examples=50)
def test_relational::obeo::column_instantiation(instance):
    assert isinstance(instance, relational::obeo::Column)

@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::obeo::Column_strategy)
def test_relational::obeo::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::obeo::Table_strategy)
@settings(max_examples=50)
def test_relational::obeo::table_instantiation(instance):
    assert isinstance(instance, relational::obeo::Table)

@given(instance=relational::obeo::Table_strategy)
def test_relational::obeo::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::obeo::Table_strategy)
def test_relational::obeo::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::obeo::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::obeo::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::obeo::ForeignKey)

@given(instance=relational::obeo::ForeignKey_strategy)
def test_relational::obeo::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::obeo::ForeignKey_strategy)
def test_relational::obeo::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::obeo::Schema_strategy)
@settings(max_examples=50)
def test_relational::obeo::schema_instantiation(instance):
    assert isinstance(instance, relational::obeo::Schema)

@given(instance=relational::obeo::Schema_strategy)
def test_relational::obeo::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::obeo::Schema_strategy)
def test_relational::obeo::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::obeo::Database_strategy)
@settings(max_examples=50)
def test_relational::obeo::database_instantiation(instance):
    assert isinstance(instance, relational::obeo::Database)

@given(instance=relational::obeo::Database_strategy)
def test_relational::obeo::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::obeo::Database_strategy)
def test_relational::obeo::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::obeo::Database_strategy)
def test_relational::obeo::database_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=relational::obeo::Database_strategy)
def test_relational::obeo::database_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original
