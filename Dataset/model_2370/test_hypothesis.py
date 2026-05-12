import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbms_referencedColumns,
    rdbms_tables,
    rdbms_table,
    rdbms_schemas,
    rdbms_schema,
    rdbms_foreignKeys,
    rdbms_RDBMS,
    rdbms_oID,
    rdbms_key2,
    rdbms_key,
    rdbms_EStringToStringMapEntry,
    rdbms_foreignKey,
    rdbms_DocumentRoot,
    rdbms_columns,
    rdbms_hasForeignKeys,
    rdbms_referencedKeys,
    rdbms_column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms_referencedcolumns_is_not_abstract():
    assert not inspect.isabstract(rdbms_referencedColumns)


def test_rdbms_referencedcolumns_constructor_exists():
    assert callable(rdbms_referencedColumns.__init__)


def test_rdbms_referencedcolumns_constructor_args():
    sig = inspect.signature(rdbms_referencedColumns.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_referencedcolumns_has_group():
    assert hasattr(rdbms_referencedColumns, "group")
    descriptor = None
    for klass in rdbms_referencedColumns.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_tables_is_not_abstract():
    assert not inspect.isabstract(rdbms_tables)


def test_rdbms_tables_constructor_exists():
    assert callable(rdbms_tables.__init__)


def test_rdbms_tables_constructor_args():
    sig = inspect.signature(rdbms_tables.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_tables_has_group():
    assert hasattr(rdbms_tables, "group")
    descriptor = None
    for klass in rdbms_tables.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(rdbms_table)


def test_rdbms_table_constructor_exists():
    assert callable(rdbms_table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(rdbms_table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "oID" in params, "Missing parameter 'oID'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_rdbms_table_has_name():
    assert hasattr(rdbms_table, "name")
    descriptor = None
    for klass in rdbms_table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_table_has_oID():
    assert hasattr(rdbms_table, "oID")
    descriptor = None
    for klass in rdbms_table.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_table_has_kind():
    assert hasattr(rdbms_table, "kind")
    descriptor = None
    for klass in rdbms_table.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_schemas_is_not_abstract():
    assert not inspect.isabstract(rdbms_schemas)


def test_rdbms_schemas_constructor_exists():
    assert callable(rdbms_schemas.__init__)


def test_rdbms_schemas_constructor_args():
    sig = inspect.signature(rdbms_schemas.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_schemas_has_group():
    assert hasattr(rdbms_schemas, "group")
    descriptor = None
    for klass in rdbms_schemas.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_schema_is_not_abstract():
    assert not inspect.isabstract(rdbms_schema)


def test_rdbms_schema_constructor_exists():
    assert callable(rdbms_schema.__init__)


def test_rdbms_schema_constructor_args():
    sig = inspect.signature(rdbms_schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "oID" in params, "Missing parameter 'oID'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_rdbms_schema_has_name():
    assert hasattr(rdbms_schema, "name")
    descriptor = None
    for klass in rdbms_schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_schema_has_oID():
    assert hasattr(rdbms_schema, "oID")
    descriptor = None
    for klass in rdbms_schema.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_schema_has_kind():
    assert hasattr(rdbms_schema, "kind")
    descriptor = None
    for klass in rdbms_schema.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_foreignkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms_foreignKeys)


def test_rdbms_foreignkeys_constructor_exists():
    assert callable(rdbms_foreignKeys.__init__)


def test_rdbms_foreignkeys_constructor_args():
    sig = inspect.signature(rdbms_foreignKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_foreignkeys_has_group():
    assert hasattr(rdbms_foreignKeys, "group")
    descriptor = None
    for klass in rdbms_foreignKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbms_is_not_abstract():
    assert not inspect.isabstract(rdbms_RDBMS)


def test_rdbms_rdbms_constructor_exists():
    assert callable(rdbms_RDBMS.__init__)


def test_rdbms_rdbms_constructor_args():
    sig = inspect.signature(rdbms_RDBMS.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_oid_is_not_abstract():
    assert not inspect.isabstract(rdbms_oID)


def test_rdbms_oid_constructor_exists():
    assert callable(rdbms_oID.__init__)


def test_rdbms_oid_constructor_args():
    sig = inspect.signature(rdbms_oID.__init__)
    params = list(sig.parameters.keys())
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms_oid_has_oID():
    assert hasattr(rdbms_oID, "oID")
    descriptor = None
    for klass in rdbms_oID.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_key2_is_not_abstract():
    assert not inspect.isabstract(rdbms_key2)


def test_rdbms_key2_constructor_exists():
    assert callable(rdbms_key2.__init__)


def test_rdbms_key2_constructor_args():
    sig = inspect.signature(rdbms_key2.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_key_is_not_abstract():
    assert not inspect.isabstract(rdbms_key)


def test_rdbms_key_constructor_exists():
    assert callable(rdbms_key.__init__)


def test_rdbms_key_constructor_args():
    sig = inspect.signature(rdbms_key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms_key_has_name():
    assert hasattr(rdbms_key, "name")
    descriptor = None
    for klass in rdbms_key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_key_has_kind():
    assert hasattr(rdbms_key, "kind")
    descriptor = None
    for klass in rdbms_key.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_key_has_oID():
    assert hasattr(rdbms_key, "oID")
    descriptor = None
    for klass in rdbms_key.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(rdbms_EStringToStringMapEntry)


def test_rdbms_estringtostringmapentry_constructor_exists():
    assert callable(rdbms_EStringToStringMapEntry.__init__)


def test_rdbms_estringtostringmapentry_constructor_args():
    sig = inspect.signature(rdbms_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_foreignKey)


def test_rdbms_foreignkey_constructor_exists():
    assert callable(rdbms_foreignKey.__init__)


def test_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(rdbms_foreignKey.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "oID" in params, "Missing parameter 'oID'"
    assert "refersTo" in params, "Missing parameter 'refersTo'"

def test_rdbms_foreignkey_has_kind():
    assert hasattr(rdbms_foreignKey, "kind")
    descriptor = None
    for klass in rdbms_foreignKey.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_name():
    assert hasattr(rdbms_foreignKey, "name")
    descriptor = None
    for klass in rdbms_foreignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_owner():
    assert hasattr(rdbms_foreignKey, "owner")
    descriptor = None
    for klass in rdbms_foreignKey.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_oID():
    assert hasattr(rdbms_foreignKey, "oID")
    descriptor = None
    for klass in rdbms_foreignKey.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_refersTo():
    assert hasattr(rdbms_foreignKey, "refersTo")
    descriptor = None
    for klass in rdbms_foreignKey.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_documentroot_is_not_abstract():
    assert not inspect.isabstract(rdbms_DocumentRoot)


def test_rdbms_documentroot_constructor_exists():
    assert callable(rdbms_DocumentRoot.__init__)


def test_rdbms_documentroot_constructor_args():
    sig = inspect.signature(rdbms_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_rdbms_documentroot_has_mixed():
    assert hasattr(rdbms_DocumentRoot, "mixed")
    descriptor = None
    for klass in rdbms_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_columns_is_not_abstract():
    assert not inspect.isabstract(rdbms_columns)


def test_rdbms_columns_constructor_exists():
    assert callable(rdbms_columns.__init__)


def test_rdbms_columns_constructor_args():
    sig = inspect.signature(rdbms_columns.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_columns_has_group():
    assert hasattr(rdbms_columns, "group")
    descriptor = None
    for klass in rdbms_columns.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_hasforeignkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms_hasForeignKeys)


def test_rdbms_hasforeignkeys_constructor_exists():
    assert callable(rdbms_hasForeignKeys.__init__)


def test_rdbms_hasforeignkeys_constructor_args():
    sig = inspect.signature(rdbms_hasForeignKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_hasforeignkeys_has_group():
    assert hasattr(rdbms_hasForeignKeys, "group")
    descriptor = None
    for klass in rdbms_hasForeignKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_referencedkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms_referencedKeys)


def test_rdbms_referencedkeys_constructor_exists():
    assert callable(rdbms_referencedKeys.__init__)


def test_rdbms_referencedkeys_constructor_args():
    sig = inspect.signature(rdbms_referencedKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms_referencedkeys_has_group():
    assert hasattr(rdbms_referencedKeys, "group")
    descriptor = None
    for klass in rdbms_referencedKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(rdbms_column)


def test_rdbms_column_constructor_exists():
    assert callable(rdbms_column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(rdbms_column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms_column_has_type():
    assert hasattr(rdbms_column, "type")
    descriptor = None
    for klass in rdbms_column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_name():
    assert hasattr(rdbms_column, "name")
    descriptor = None
    for klass in rdbms_column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_kind():
    assert hasattr(rdbms_column, "kind")
    descriptor = None
    for klass in rdbms_column.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_oID():
    assert hasattr(rdbms_column, "oID")
    descriptor = None
    for klass in rdbms_column.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)


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
rdbms_referencedColumns_strategy = st.builds(
    rdbms_referencedColumns,
    group=
        safe_text
)
rdbms_tables_strategy = st.builds(
    rdbms_tables,
    group=
        safe_text
)
rdbms_table_strategy = st.builds(
    rdbms_table,
    name=
        safe_text,
    oID=
        safe_text,
    kind=
        safe_text
)
rdbms_schemas_strategy = st.builds(
    rdbms_schemas,
    group=
        safe_text
)
rdbms_schema_strategy = st.builds(
    rdbms_schema,
    name=
        safe_text,
    oID=
        safe_text,
    kind=
        safe_text
)
rdbms_foreignKeys_strategy = st.builds(
    rdbms_foreignKeys,
    group=
        safe_text
)
rdbms_RDBMS_strategy = st.builds(
    rdbms_RDBMS,
)
rdbms_oID_strategy = st.builds(
    rdbms_oID,
    oID=
        safe_text
)
rdbms_key2_strategy = st.builds(
    rdbms_key2,
)
rdbms_key_strategy = st.builds(
    rdbms_key,
    name=
        safe_text,
    kind=
        safe_text,
    oID=
        safe_text
)
rdbms_EStringToStringMapEntry_strategy = st.builds(
    rdbms_EStringToStringMapEntry,
)
rdbms_foreignKey_strategy = st.builds(
    rdbms_foreignKey,
    kind=
        safe_text,
    name=
        safe_text,
    owner=
        safe_text,
    oID=
        safe_text,
    refersTo=
        safe_text
)
rdbms_DocumentRoot_strategy = st.builds(
    rdbms_DocumentRoot,
    mixed=
        safe_text
)
rdbms_columns_strategy = st.builds(
    rdbms_columns,
    group=
        safe_text
)
rdbms_hasForeignKeys_strategy = st.builds(
    rdbms_hasForeignKeys,
    group=
        safe_text
)
rdbms_referencedKeys_strategy = st.builds(
    rdbms_referencedKeys,
    group=
        safe_text
)
rdbms_column_strategy = st.builds(
    rdbms_column,
    type=
        safe_text,
    name=
        safe_text,
    kind=
        safe_text,
    oID=
        safe_text
)

@given(instance=rdbms_referencedColumns_strategy)
@settings(max_examples=50)
def test_rdbms_referencedcolumns_instantiation(instance):
    assert isinstance(instance, rdbms_referencedColumns)



@given(instance=rdbms_referencedColumns_strategy)
def test_rdbms_referencedcolumns_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_tables_strategy)
@settings(max_examples=50)
def test_rdbms_tables_instantiation(instance):
    assert isinstance(instance, rdbms_tables)



@given(instance=rdbms_tables_strategy)
def test_rdbms_tables_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, rdbms_table)



@given(instance=rdbms_table_strategy)
def test_rdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_table_strategy)
def test_rdbms_table_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original



@given(instance=rdbms_table_strategy)
def test_rdbms_table_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms_schemas_strategy)
@settings(max_examples=50)
def test_rdbms_schemas_instantiation(instance):
    assert isinstance(instance, rdbms_schemas)



@given(instance=rdbms_schemas_strategy)
def test_rdbms_schemas_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_schema_strategy)
@settings(max_examples=50)
def test_rdbms_schema_instantiation(instance):
    assert isinstance(instance, rdbms_schema)



@given(instance=rdbms_schema_strategy)
def test_rdbms_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_schema_strategy)
def test_rdbms_schema_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original



@given(instance=rdbms_schema_strategy)
def test_rdbms_schema_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms_foreignKeys_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkeys_instantiation(instance):
    assert isinstance(instance, rdbms_foreignKeys)



@given(instance=rdbms_foreignKeys_strategy)
def test_rdbms_foreignkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_RDBMS_strategy)
@settings(max_examples=50)
def test_rdbms_rdbms_instantiation(instance):
    assert isinstance(instance, rdbms_RDBMS)

@given(instance=rdbms_oID_strategy)
@settings(max_examples=50)
def test_rdbms_oid_instantiation(instance):
    assert isinstance(instance, rdbms_oID)



@given(instance=rdbms_oID_strategy)
def test_rdbms_oid_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms_key2_strategy)
@settings(max_examples=50)
def test_rdbms_key2_instantiation(instance):
    assert isinstance(instance, rdbms_key2)

@given(instance=rdbms_key_strategy)
@settings(max_examples=50)
def test_rdbms_key_instantiation(instance):
    assert isinstance(instance, rdbms_key)



@given(instance=rdbms_key_strategy)
def test_rdbms_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_key_strategy)
def test_rdbms_key_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=rdbms_key_strategy)
def test_rdbms_key_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_rdbms_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, rdbms_EStringToStringMapEntry)

@given(instance=rdbms_foreignKey_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms_foreignKey)



@given(instance=rdbms_foreignKey_strategy)
def test_rdbms_foreignkey_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=rdbms_foreignKey_strategy)
def test_rdbms_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_foreignKey_strategy)
def test_rdbms_foreignkey_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=rdbms_foreignKey_strategy)
def test_rdbms_foreignkey_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original



@given(instance=rdbms_foreignKey_strategy)
def test_rdbms_foreignkey_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original

@given(instance=rdbms_DocumentRoot_strategy)
@settings(max_examples=50)
def test_rdbms_documentroot_instantiation(instance):
    assert isinstance(instance, rdbms_DocumentRoot)



@given(instance=rdbms_DocumentRoot_strategy)
def test_rdbms_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=rdbms_columns_strategy)
@settings(max_examples=50)
def test_rdbms_columns_instantiation(instance):
    assert isinstance(instance, rdbms_columns)



@given(instance=rdbms_columns_strategy)
def test_rdbms_columns_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_hasForeignKeys_strategy)
@settings(max_examples=50)
def test_rdbms_hasforeignkeys_instantiation(instance):
    assert isinstance(instance, rdbms_hasForeignKeys)



@given(instance=rdbms_hasForeignKeys_strategy)
def test_rdbms_hasforeignkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_referencedKeys_strategy)
@settings(max_examples=50)
def test_rdbms_referencedkeys_instantiation(instance):
    assert isinstance(instance, rdbms_referencedKeys)



@given(instance=rdbms_referencedKeys_strategy)
def test_rdbms_referencedkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms_column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, rdbms_column)



@given(instance=rdbms_column_strategy)
def test_rdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rdbms_column_strategy)
def test_rdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_column_strategy)
def test_rdbms_column_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=rdbms_column_strategy)
def test_rdbms_column_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original
