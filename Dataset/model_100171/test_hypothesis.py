import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbms::referencedColumns,
    rdbms::RDBMS,
    rdbms::tables,
    rdbms::table,
    rdbms::schemas,
    rdbms::schema,
    rdbms::foreignKeys,
    rdbms::foreignKey,
    rdbms::oID,
    rdbms::key2,
    rdbms::key,
    rdbms::columns,
    rdbms::EStringToStringMapEntry,
    rdbms::DocumentRoot,
    rdbms::hasForeignKeys,
    rdbms::referencedKeys,
    rdbms::column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms::referencedcolumns_is_not_abstract():
    assert not inspect.isabstract(rdbms::referencedColumns)


def test_rdbms::referencedcolumns_constructor_exists():
    assert callable(rdbms::referencedColumns.__init__)


def test_rdbms::referencedcolumns_constructor_args():
    sig = inspect.signature(rdbms::referencedColumns.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::referencedcolumns_has_group():
    assert hasattr(rdbms::referencedColumns, "group")
    descriptor = None
    for klass in rdbms::referencedColumns.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbms_is_not_abstract():
    assert not inspect.isabstract(rdbms::RDBMS)


def test_rdbms::rdbms_constructor_exists():
    assert callable(rdbms::RDBMS.__init__)


def test_rdbms::rdbms_constructor_args():
    sig = inspect.signature(rdbms::RDBMS.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::tables_is_not_abstract():
    assert not inspect.isabstract(rdbms::tables)


def test_rdbms::tables_constructor_exists():
    assert callable(rdbms::tables.__init__)


def test_rdbms::tables_constructor_args():
    sig = inspect.signature(rdbms::tables.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::tables_has_group():
    assert hasattr(rdbms::tables, "group")
    descriptor = None
    for klass in rdbms::tables.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::table_is_not_abstract():
    assert not inspect.isabstract(rdbms::table)


def test_rdbms::table_constructor_exists():
    assert callable(rdbms::table.__init__)


def test_rdbms::table_constructor_args():
    sig = inspect.signature(rdbms::table.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "oID" in params, "Missing parameter 'oID'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::table_has_kind():
    assert hasattr(rdbms::table, "kind")
    descriptor = None
    for klass in rdbms::table.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::table_has_oID():
    assert hasattr(rdbms::table, "oID")
    descriptor = None
    for klass in rdbms::table.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::table_has_name():
    assert hasattr(rdbms::table, "name")
    descriptor = None
    for klass in rdbms::table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::schemas_is_not_abstract():
    assert not inspect.isabstract(rdbms::schemas)


def test_rdbms::schemas_constructor_exists():
    assert callable(rdbms::schemas.__init__)


def test_rdbms::schemas_constructor_args():
    sig = inspect.signature(rdbms::schemas.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::schemas_has_group():
    assert hasattr(rdbms::schemas, "group")
    descriptor = None
    for klass in rdbms::schemas.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::schema_is_not_abstract():
    assert not inspect.isabstract(rdbms::schema)


def test_rdbms::schema_constructor_exists():
    assert callable(rdbms::schema.__init__)


def test_rdbms::schema_constructor_args():
    sig = inspect.signature(rdbms::schema.__init__)
    params = list(sig.parameters.keys())
    assert "oID" in params, "Missing parameter 'oID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_rdbms::schema_has_oID():
    assert hasattr(rdbms::schema, "oID")
    descriptor = None
    for klass in rdbms::schema.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::schema_has_name():
    assert hasattr(rdbms::schema, "name")
    descriptor = None
    for klass in rdbms::schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::schema_has_kind():
    assert hasattr(rdbms::schema, "kind")
    descriptor = None
    for klass in rdbms::schema.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::foreignkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms::foreignKeys)


def test_rdbms::foreignkeys_constructor_exists():
    assert callable(rdbms::foreignKeys.__init__)


def test_rdbms::foreignkeys_constructor_args():
    sig = inspect.signature(rdbms::foreignKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::foreignkeys_has_group():
    assert hasattr(rdbms::foreignKeys, "group")
    descriptor = None
    for klass in rdbms::foreignKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms::foreignKey)


def test_rdbms::foreignkey_constructor_exists():
    assert callable(rdbms::foreignKey.__init__)


def test_rdbms::foreignkey_constructor_args():
    sig = inspect.signature(rdbms::foreignKey.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "refersTo" in params, "Missing parameter 'refersTo'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms::foreignkey_has_kind():
    assert hasattr(rdbms::foreignKey, "kind")
    descriptor = None
    for klass in rdbms::foreignKey.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::foreignkey_has_name():
    assert hasattr(rdbms::foreignKey, "name")
    descriptor = None
    for klass in rdbms::foreignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::foreignkey_has_refersTo():
    assert hasattr(rdbms::foreignKey, "refersTo")
    descriptor = None
    for klass in rdbms::foreignKey.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::foreignkey_has_owner():
    assert hasattr(rdbms::foreignKey, "owner")
    descriptor = None
    for klass in rdbms::foreignKey.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::foreignkey_has_oID():
    assert hasattr(rdbms::foreignKey, "oID")
    descriptor = None
    for klass in rdbms::foreignKey.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::oid_is_not_abstract():
    assert not inspect.isabstract(rdbms::oID)


def test_rdbms::oid_constructor_exists():
    assert callable(rdbms::oID.__init__)


def test_rdbms::oid_constructor_args():
    sig = inspect.signature(rdbms::oID.__init__)
    params = list(sig.parameters.keys())
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms::oid_has_oID():
    assert hasattr(rdbms::oID, "oID")
    descriptor = None
    for klass in rdbms::oID.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::key2_is_not_abstract():
    assert not inspect.isabstract(rdbms::key2)


def test_rdbms::key2_constructor_exists():
    assert callable(rdbms::key2.__init__)


def test_rdbms::key2_constructor_args():
    sig = inspect.signature(rdbms::key2.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::key_is_not_abstract():
    assert not inspect.isabstract(rdbms::key)


def test_rdbms::key_constructor_exists():
    assert callable(rdbms::key.__init__)


def test_rdbms::key_constructor_args():
    sig = inspect.signature(rdbms::key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "oID" in params, "Missing parameter 'oID'"

def test_rdbms::key_has_name():
    assert hasattr(rdbms::key, "name")
    descriptor = None
    for klass in rdbms::key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::key_has_kind():
    assert hasattr(rdbms::key, "kind")
    descriptor = None
    for klass in rdbms::key.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::key_has_oID():
    assert hasattr(rdbms::key, "oID")
    descriptor = None
    for klass in rdbms::key.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::columns_is_not_abstract():
    assert not inspect.isabstract(rdbms::columns)


def test_rdbms::columns_constructor_exists():
    assert callable(rdbms::columns.__init__)


def test_rdbms::columns_constructor_args():
    sig = inspect.signature(rdbms::columns.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::columns_has_group():
    assert hasattr(rdbms::columns, "group")
    descriptor = None
    for klass in rdbms::columns.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(rdbms::EStringToStringMapEntry)


def test_rdbms::estringtostringmapentry_constructor_exists():
    assert callable(rdbms::EStringToStringMapEntry.__init__)


def test_rdbms::estringtostringmapentry_constructor_args():
    sig = inspect.signature(rdbms::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::documentroot_is_not_abstract():
    assert not inspect.isabstract(rdbms::DocumentRoot)


def test_rdbms::documentroot_constructor_exists():
    assert callable(rdbms::DocumentRoot.__init__)


def test_rdbms::documentroot_constructor_args():
    sig = inspect.signature(rdbms::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_rdbms::documentroot_has_mixed():
    assert hasattr(rdbms::DocumentRoot, "mixed")
    descriptor = None
    for klass in rdbms::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::hasforeignkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms::hasForeignKeys)


def test_rdbms::hasforeignkeys_constructor_exists():
    assert callable(rdbms::hasForeignKeys.__init__)


def test_rdbms::hasforeignkeys_constructor_args():
    sig = inspect.signature(rdbms::hasForeignKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::hasforeignkeys_has_group():
    assert hasattr(rdbms::hasForeignKeys, "group")
    descriptor = None
    for klass in rdbms::hasForeignKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::referencedkeys_is_not_abstract():
    assert not inspect.isabstract(rdbms::referencedKeys)


def test_rdbms::referencedkeys_constructor_exists():
    assert callable(rdbms::referencedKeys.__init__)


def test_rdbms::referencedkeys_constructor_args():
    sig = inspect.signature(rdbms::referencedKeys.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_rdbms::referencedkeys_has_group():
    assert hasattr(rdbms::referencedKeys, "group")
    descriptor = None
    for klass in rdbms::referencedKeys.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::column_is_not_abstract():
    assert not inspect.isabstract(rdbms::column)


def test_rdbms::column_constructor_exists():
    assert callable(rdbms::column.__init__)


def test_rdbms::column_constructor_args():
    sig = inspect.signature(rdbms::column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "oID" in params, "Missing parameter 'oID'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::column_has_type():
    assert hasattr(rdbms::column, "type")
    descriptor = None
    for klass in rdbms::column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_kind():
    assert hasattr(rdbms::column, "kind")
    descriptor = None
    for klass in rdbms::column.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_oID():
    assert hasattr(rdbms::column, "oID")
    descriptor = None
    for klass in rdbms::column.__mro__:
        if "oID" in klass.__dict__:
            descriptor = klass.__dict__["oID"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_name():
    assert hasattr(rdbms::column, "name")
    descriptor = None
    for klass in rdbms::column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
rdbms::referencedColumns_strategy = st.builds(
    rdbms::referencedColumns,
    group=
        safe_text
)
rdbms::RDBMS_strategy = st.builds(
    rdbms::RDBMS,
)
rdbms::tables_strategy = st.builds(
    rdbms::tables,
    group=
        safe_text
)
rdbms::table_strategy = st.builds(
    rdbms::table,
    kind=
        safe_text,
    oID=
        safe_text,
    name=
        safe_text
)
rdbms::schemas_strategy = st.builds(
    rdbms::schemas,
    group=
        safe_text
)
rdbms::schema_strategy = st.builds(
    rdbms::schema,
    oID=
        safe_text,
    name=
        safe_text,
    kind=
        safe_text
)
rdbms::foreignKeys_strategy = st.builds(
    rdbms::foreignKeys,
    group=
        safe_text
)
rdbms::foreignKey_strategy = st.builds(
    rdbms::foreignKey,
    kind=
        safe_text,
    name=
        safe_text,
    refersTo=
        safe_text,
    owner=
        safe_text,
    oID=
        safe_text
)
rdbms::oID_strategy = st.builds(
    rdbms::oID,
    oID=
        safe_text
)
rdbms::key2_strategy = st.builds(
    rdbms::key2,
)
rdbms::key_strategy = st.builds(
    rdbms::key,
    name=
        safe_text,
    kind=
        safe_text,
    oID=
        safe_text
)
rdbms::columns_strategy = st.builds(
    rdbms::columns,
    group=
        safe_text
)
rdbms::EStringToStringMapEntry_strategy = st.builds(
    rdbms::EStringToStringMapEntry,
)
rdbms::DocumentRoot_strategy = st.builds(
    rdbms::DocumentRoot,
    mixed=
        safe_text
)
rdbms::hasForeignKeys_strategy = st.builds(
    rdbms::hasForeignKeys,
    group=
        safe_text
)
rdbms::referencedKeys_strategy = st.builds(
    rdbms::referencedKeys,
    group=
        safe_text
)
rdbms::column_strategy = st.builds(
    rdbms::column,
    type=
        safe_text,
    kind=
        safe_text,
    oID=
        safe_text,
    name=
        safe_text
)

@given(instance=rdbms::referencedColumns_strategy)
@settings(max_examples=50)
def test_rdbms::referencedcolumns_instantiation(instance):
    assert isinstance(instance, rdbms::referencedColumns)

@given(instance=rdbms::referencedColumns_strategy)
def test_rdbms::referencedcolumns_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::referencedColumns_strategy)
def test_rdbms::referencedcolumns_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::RDBMS_strategy)
@settings(max_examples=50)
def test_rdbms::rdbms_instantiation(instance):
    assert isinstance(instance, rdbms::RDBMS)

@given(instance=rdbms::tables_strategy)
@settings(max_examples=50)
def test_rdbms::tables_instantiation(instance):
    assert isinstance(instance, rdbms::tables)

@given(instance=rdbms::tables_strategy)
def test_rdbms::tables_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::tables_strategy)
def test_rdbms::tables_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::table_strategy)
@settings(max_examples=50)
def test_rdbms::table_instantiation(instance):
    assert isinstance(instance, rdbms::table)

@given(instance=rdbms::table_strategy)
def test_rdbms::table_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::table_strategy)
def test_rdbms::table_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::table_strategy)
def test_rdbms::table_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::table_strategy)
def test_rdbms::table_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::table_strategy)
def test_rdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::table_strategy)
def test_rdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::schemas_strategy)
@settings(max_examples=50)
def test_rdbms::schemas_instantiation(instance):
    assert isinstance(instance, rdbms::schemas)

@given(instance=rdbms::schemas_strategy)
def test_rdbms::schemas_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::schemas_strategy)
def test_rdbms::schemas_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::schema_strategy)
@settings(max_examples=50)
def test_rdbms::schema_instantiation(instance):
    assert isinstance(instance, rdbms::schema)

@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::schema_strategy)
def test_rdbms::schema_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::foreignKeys_strategy)
@settings(max_examples=50)
def test_rdbms::foreignkeys_instantiation(instance):
    assert isinstance(instance, rdbms::foreignKeys)

@given(instance=rdbms::foreignKeys_strategy)
def test_rdbms::foreignkeys_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::foreignKeys_strategy)
def test_rdbms::foreignkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::foreignKey_strategy)
@settings(max_examples=50)
def test_rdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms::foreignKey)

@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_refersTo_type(instance):
    assert isinstance(instance.refersTo, str)


@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original

@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::foreignKey_strategy)
def test_rdbms::foreignkey_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::oID_strategy)
@settings(max_examples=50)
def test_rdbms::oid_instantiation(instance):
    assert isinstance(instance, rdbms::oID)

@given(instance=rdbms::oID_strategy)
def test_rdbms::oid_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::oID_strategy)
def test_rdbms::oid_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::key2_strategy)
@settings(max_examples=50)
def test_rdbms::key2_instantiation(instance):
    assert isinstance(instance, rdbms::key2)

@given(instance=rdbms::key_strategy)
@settings(max_examples=50)
def test_rdbms::key_instantiation(instance):
    assert isinstance(instance, rdbms::key)

@given(instance=rdbms::key_strategy)
def test_rdbms::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::key_strategy)
def test_rdbms::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::key_strategy)
def test_rdbms::key_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::key_strategy)
def test_rdbms::key_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::key_strategy)
def test_rdbms::key_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::key_strategy)
def test_rdbms::key_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::columns_strategy)
@settings(max_examples=50)
def test_rdbms::columns_instantiation(instance):
    assert isinstance(instance, rdbms::columns)

@given(instance=rdbms::columns_strategy)
def test_rdbms::columns_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::columns_strategy)
def test_rdbms::columns_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_rdbms::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, rdbms::EStringToStringMapEntry)

@given(instance=rdbms::DocumentRoot_strategy)
@settings(max_examples=50)
def test_rdbms::documentroot_instantiation(instance):
    assert isinstance(instance, rdbms::DocumentRoot)

@given(instance=rdbms::DocumentRoot_strategy)
def test_rdbms::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=rdbms::DocumentRoot_strategy)
def test_rdbms::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=rdbms::hasForeignKeys_strategy)
@settings(max_examples=50)
def test_rdbms::hasforeignkeys_instantiation(instance):
    assert isinstance(instance, rdbms::hasForeignKeys)

@given(instance=rdbms::hasForeignKeys_strategy)
def test_rdbms::hasforeignkeys_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::hasForeignKeys_strategy)
def test_rdbms::hasforeignkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::referencedKeys_strategy)
@settings(max_examples=50)
def test_rdbms::referencedkeys_instantiation(instance):
    assert isinstance(instance, rdbms::referencedKeys)

@given(instance=rdbms::referencedKeys_strategy)
def test_rdbms::referencedkeys_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=rdbms::referencedKeys_strategy)
def test_rdbms::referencedkeys_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=rdbms::column_strategy)
@settings(max_examples=50)
def test_rdbms::column_instantiation(instance):
    assert isinstance(instance, rdbms::column)

@given(instance=rdbms::column_strategy)
def test_rdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdbms::column_strategy)
def test_rdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbms::column_strategy)
def test_rdbms::column_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbms::column_strategy)
def test_rdbms::column_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=rdbms::column_strategy)
def test_rdbms::column_oID_type(instance):
    assert isinstance(instance.oID, str)


@given(instance=rdbms::column_strategy)
def test_rdbms::column_oID_setter(instance):
    original = instance.oID
    instance.oID = original
    assert instance.oID == original

@given(instance=rdbms::column_strategy)
def test_rdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::column_strategy)
def test_rdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
