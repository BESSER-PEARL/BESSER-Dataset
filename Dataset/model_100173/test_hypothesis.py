import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    relational_ModelElement,
    ModelElement,
    relational_Column,
    relational_ForeignKey,
    relational_Database,
    relational_Table,
    relational_Schema,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational_modelelement_is_not_abstract():
    assert not inspect.isabstract(relational_ModelElement)


def test_relational_modelelement_constructor_exists():
    assert callable(relational_ModelElement.__init__)


def test_relational_modelelement_constructor_args():
    sig = inspect.signature(relational_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_relational_modelelement_has_comment():
    assert hasattr(relational_ModelElement, "comment")
    descriptor = None
    for klass in relational_ModelElement.__mro__:
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



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational_column_has_isUnique():
    assert hasattr(relational_Column, "isUnique")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_type():
    assert hasattr(relational_Column, "type")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_isPrimaryKey():
    assert hasattr(relational_Column, "isPrimaryKey")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_name():
    assert hasattr(relational_Column, "name")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_foreignkey_has_name():
    assert hasattr(relational_ForeignKey, "name")
    descriptor = None
    for klass in relational_ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_database_is_not_abstract():
    assert not inspect.isabstract(relational_Database)


def test_relational_database_constructor_exists():
    assert callable(relational_Database.__init__)


def test_relational_database_constructor_args():
    sig = inspect.signature(relational_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_relational_database_has_name():
    assert hasattr(relational_Database, "name")
    descriptor = None
    for klass in relational_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational_database_has_url():
    assert hasattr(relational_Database, "url")
    descriptor = None
    for klass in relational_Database.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_table_has_name():
    assert hasattr(relational_Table, "name")
    descriptor = None
    for klass in relational_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_schema_has_name():
    assert hasattr(relational_Schema, "name")
    descriptor = None
    for klass in relational_Schema.__mro__:
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
        "FLOAT",
        "DATE",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "TIME",
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
relational_ModelElement_strategy = st.builds(
    relational_ModelElement,
    comment=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
relational_Column_strategy = st.builds(
    relational_Column,
    isUnique=
        st.booleans(),
    type=
        safe_text,
    isPrimaryKey=
        st.booleans(),
    name=
        safe_text
)
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
    name=
        safe_text
)
relational_Database_strategy = st.builds(
    relational_Database,
    name=
        safe_text,
    url=
        safe_text
)
relational_Table_strategy = st.builds(
    relational_Table,
    name=
        safe_text
)
relational_Schema_strategy = st.builds(
    relational_Schema,
    name=
        safe_text
)

@given(instance=relational_ModelElement_strategy)
@settings(max_examples=50)
def test_relational_modelelement_instantiation(instance):
    assert isinstance(instance, relational_ModelElement)



@given(instance=relational_ModelElement_strategy)
def test_relational_modelelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)



@given(instance=relational_Column_strategy)
def test_relational_column_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=relational_Column_strategy)
def test_relational_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=relational_Column_strategy)
def test_relational_column_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original



@given(instance=relational_Column_strategy)
def test_relational_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)



@given(instance=relational_ForeignKey_strategy)
def test_relational_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Database_strategy)
@settings(max_examples=50)
def test_relational_database_instantiation(instance):
    assert isinstance(instance, relational_Database)



@given(instance=relational_Database_strategy)
def test_relational_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=relational_Database_strategy)
def test_relational_database_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)



@given(instance=relational_Table_strategy)
def test_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)



@given(instance=relational_Schema_strategy)
def test_relational_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
