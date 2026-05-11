import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdb::ERDInfo,
    Table,
    rdb::View,
    rdb::UserComment,
    rdb::Column,
    rdb::Relation,
    rdb::Table,
    ERDInfo,
    rdb::DB,
    RelationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdb::erdinfo_is_not_abstract():
    assert not inspect.isabstract(rdb::ERDInfo)


def test_rdb::erdinfo_constructor_exists():
    assert callable(rdb::ERDInfo.__init__)


def test_rdb::erdinfo_constructor_args():
    sig = inspect.signature(rdb::ERDInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "autoLayout" in params, "Missing parameter 'autoLayout'"

def test_rdb::erdinfo_has_version():
    assert hasattr(rdb::ERDInfo, "version")
    descriptor = None
    for klass in rdb::ERDInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_rdb::erdinfo_has_autoLayout():
    assert hasattr(rdb::ERDInfo, "autoLayout")
    descriptor = None
    for klass in rdb::ERDInfo.__mro__:
        if "autoLayout" in klass.__dict__:
            descriptor = klass.__dict__["autoLayout"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_rdb::view_is_not_abstract():
    assert not inspect.isabstract(rdb::View)


def test_rdb::view_constructor_exists():
    assert callable(rdb::View.__init__)


def test_rdb::view_constructor_args():
    sig = inspect.signature(rdb::View.__init__)
    params = list(sig.parameters.keys())



def test_rdb::usercomment_is_not_abstract():
    assert not inspect.isabstract(rdb::UserComment)


def test_rdb::usercomment_constructor_exists():
    assert callable(rdb::UserComment.__init__)


def test_rdb::usercomment_constructor_args():
    sig = inspect.signature(rdb::UserComment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_rdb::usercomment_has_comment():
    assert hasattr(rdb::UserComment, "comment")
    descriptor = None
    for klass in rdb::UserComment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_rdb::column_is_not_abstract():
    assert not inspect.isabstract(rdb::Column)


def test_rdb::column_constructor_exists():
    assert callable(rdb::Column.__init__)


def test_rdb::column_constructor_args():
    sig = inspect.signature(rdb::Column.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"
    assert "extra" in params, "Missing parameter 'extra'"
    assert "type" in params, "Missing parameter 'type'"
    assert "null" in params, "Missing parameter 'null'"
    assert "key" in params, "Missing parameter 'key'"
    assert "default" in params, "Missing parameter 'default'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "logicalField" in params, "Missing parameter 'logicalField'"

def test_rdb::column_has_field():
    assert hasattr(rdb::Column, "field")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_extra():
    assert hasattr(rdb::Column, "extra")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_type():
    assert hasattr(rdb::Column, "type")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_null():
    assert hasattr(rdb::Column, "null")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_key():
    assert hasattr(rdb::Column, "key")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_default():
    assert hasattr(rdb::Column, "default")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_comment():
    assert hasattr(rdb::Column, "comment")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_logicalField():
    assert hasattr(rdb::Column, "logicalField")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "logicalField" in klass.__dict__:
            descriptor = klass.__dict__["logicalField"]
            break
    assert isinstance(descriptor, property)



def test_rdb::relation_is_not_abstract():
    assert not inspect.isabstract(rdb::Relation)


def test_rdb::relation_constructor_exists():
    assert callable(rdb::Relation.__init__)


def test_rdb::relation_constructor_args():
    sig = inspect.signature(rdb::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "source_kind" in params, "Missing parameter 'source_kind'"
    assert "referenced_column_name" in params, "Missing parameter 'referenced_column_name'"
    assert "bendpoint" in params, "Missing parameter 'bendpoint'"
    assert "target_kind" in params, "Missing parameter 'target_kind'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "constraint_name" in params, "Missing parameter 'constraint_name'"
    assert "column_name" in params, "Missing parameter 'column_name'"

def test_rdb::relation_has_source_kind():
    assert hasattr(rdb::Relation, "source_kind")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "source_kind" in klass.__dict__:
            descriptor = klass.__dict__["source_kind"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_referenced_column_name():
    assert hasattr(rdb::Relation, "referenced_column_name")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "referenced_column_name" in klass.__dict__:
            descriptor = klass.__dict__["referenced_column_name"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_bendpoint():
    assert hasattr(rdb::Relation, "bendpoint")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "bendpoint" in klass.__dict__:
            descriptor = klass.__dict__["bendpoint"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_target_kind():
    assert hasattr(rdb::Relation, "target_kind")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "target_kind" in klass.__dict__:
            descriptor = klass.__dict__["target_kind"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_comment():
    assert hasattr(rdb::Relation, "comment")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_constraint_name():
    assert hasattr(rdb::Relation, "constraint_name")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "constraint_name" in klass.__dict__:
            descriptor = klass.__dict__["constraint_name"]
            break
    assert isinstance(descriptor, property)

def test_rdb::relation_has_column_name():
    assert hasattr(rdb::Relation, "column_name")
    descriptor = None
    for klass in rdb::Relation.__mro__:
        if "column_name" in klass.__dict__:
            descriptor = klass.__dict__["column_name"]
            break
    assert isinstance(descriptor, property)



def test_rdb::table_is_not_abstract():
    assert not inspect.isabstract(rdb::Table)


def test_rdb::table_constructor_exists():
    assert callable(rdb::Table.__init__)


def test_rdb::table_constructor_args():
    sig = inspect.signature(rdb::Table.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "constraints" in params, "Missing parameter 'constraints'"
    assert "logicalName" in params, "Missing parameter 'logicalName'"

def test_rdb::table_has_comment():
    assert hasattr(rdb::Table, "comment")
    descriptor = None
    for klass in rdb::Table.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb::table_has_name():
    assert hasattr(rdb::Table, "name")
    descriptor = None
    for klass in rdb::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdb::table_has_constraints():
    assert hasattr(rdb::Table, "constraints")
    descriptor = None
    for klass in rdb::Table.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)

def test_rdb::table_has_logicalName():
    assert hasattr(rdb::Table, "logicalName")
    descriptor = None
    for klass in rdb::Table.__mro__:
        if "logicalName" in klass.__dict__:
            descriptor = klass.__dict__["logicalName"]
            break
    assert isinstance(descriptor, property)



def test_erdinfo_is_not_abstract():
    assert not inspect.isabstract(ERDInfo)


def test_erdinfo_constructor_exists():
    assert callable(ERDInfo.__init__)


def test_erdinfo_constructor_args():
    sig = inspect.signature(ERDInfo.__init__)
    params = list(sig.parameters.keys())



def test_rdb::db_is_not_abstract():
    assert not inspect.isabstract(rdb::DB)


def test_rdb::db_constructor_exists():
    assert callable(rdb::DB.__init__)


def test_rdb::db_constructor_args():
    sig = inspect.signature(rdb::DB.__init__)
    params = list(sig.parameters.keys())
    assert "sid" in params, "Missing parameter 'sid'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "dbType" in params, "Missing parameter 'dbType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "url" in params, "Missing parameter 'url'"
    assert "key" in params, "Missing parameter 'key'"

def test_rdb::db_has_sid():
    assert hasattr(rdb::DB, "sid")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "sid" in klass.__dict__:
            descriptor = klass.__dict__["sid"]
            break
    assert isinstance(descriptor, property)

def test_rdb::db_has_comment():
    assert hasattr(rdb::DB, "comment")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb::db_has_dbType():
    assert hasattr(rdb::DB, "dbType")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "dbType" in klass.__dict__:
            descriptor = klass.__dict__["dbType"]
            break
    assert isinstance(descriptor, property)

def test_rdb::db_has_id():
    assert hasattr(rdb::DB, "id")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rdb::db_has_url():
    assert hasattr(rdb::DB, "url")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_rdb::db_has_key():
    assert hasattr(rdb::DB, "key")
    descriptor = None
    for klass in rdb::DB.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_relationkind_exists():
    # Check that the Enumeration exists
    assert RelationKind is not None

def test_relationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationKind]
    expected_literals = [
        "ZERO_OR_MANY",
        "ONLY_ONE",
        "ZERO_OR_ONE",
        "ONE_OR_MANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationKind"


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
rdb::ERDInfo_strategy = st.builds(
    rdb::ERDInfo,
    version=
        safe_text,
    autoLayout=
        st.booleans()
)
Table_strategy = st.builds(
    Table,
)
rdb::View_strategy = st.builds(
    rdb::View,
)
rdb::UserComment_strategy = st.builds(
    rdb::UserComment,
    comment=
        safe_text
)
rdb::Column_strategy = st.builds(
    rdb::Column,
    field=
        safe_text,
    extra=
        safe_text,
    type=
        safe_text,
    null=
        safe_text,
    key=
        safe_text,
    default=
        safe_text,
    comment=
        safe_text,
    logicalField=
        safe_text
)
rdb::Relation_strategy = st.builds(
    rdb::Relation,
    source_kind=
        safe_text,
    referenced_column_name=
        safe_text,
    bendpoint=
        safe_text,
    target_kind=
        safe_text,
    comment=
        safe_text,
    constraint_name=
        safe_text,
    column_name=
        safe_text
)
rdb::Table_strategy = st.builds(
    rdb::Table,
    comment=
        safe_text,
    name=
        safe_text,
    constraints=
        safe_text,
    logicalName=
        safe_text
)
ERDInfo_strategy = st.builds(
    ERDInfo,
)
rdb::DB_strategy = st.builds(
    rdb::DB,
    sid=
        safe_text,
    comment=
        safe_text,
    dbType=
        safe_text,
    id=
        safe_text,
    url=
        safe_text,
    key=
        safe_text
)

@given(instance=rdb::ERDInfo_strategy)
@settings(max_examples=50)
def test_rdb::erdinfo_instantiation(instance):
    assert isinstance(instance, rdb::ERDInfo)

@given(instance=rdb::ERDInfo_strategy)
def test_rdb::erdinfo_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=rdb::ERDInfo_strategy)
def test_rdb::erdinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=rdb::ERDInfo_strategy)
def test_rdb::erdinfo_autoLayout_type(instance):
    assert isinstance(instance.autoLayout, bool)


@given(instance=rdb::ERDInfo_strategy)
def test_rdb::erdinfo_autoLayout_setter(instance):
    original = instance.autoLayout
    instance.autoLayout = original
    assert instance.autoLayout == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=rdb::View_strategy)
@settings(max_examples=50)
def test_rdb::view_instantiation(instance):
    assert isinstance(instance, rdb::View)

@given(instance=rdb::UserComment_strategy)
@settings(max_examples=50)
def test_rdb::usercomment_instantiation(instance):
    assert isinstance(instance, rdb::UserComment)

@given(instance=rdb::UserComment_strategy)
def test_rdb::usercomment_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rdb::UserComment_strategy)
def test_rdb::usercomment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb::Column_strategy)
@settings(max_examples=50)
def test_rdb::column_instantiation(instance):
    assert isinstance(instance, rdb::Column)

@given(instance=rdb::Column_strategy)
def test_rdb::column_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_extra_type(instance):
    assert isinstance(instance.extra, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_logicalField_type(instance):
    assert isinstance(instance.logicalField, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_logicalField_setter(instance):
    original = instance.logicalField
    instance.logicalField = original
    assert instance.logicalField == original

@given(instance=rdb::Relation_strategy)
@settings(max_examples=50)
def test_rdb::relation_instantiation(instance):
    assert isinstance(instance, rdb::Relation)

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_source_kind_type(instance):
    assert isinstance(instance.source_kind, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_source_kind_setter(instance):
    original = instance.source_kind
    instance.source_kind = original
    assert instance.source_kind == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_referenced_column_name_type(instance):
    assert isinstance(instance.referenced_column_name, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_referenced_column_name_setter(instance):
    original = instance.referenced_column_name
    instance.referenced_column_name = original
    assert instance.referenced_column_name == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_bendpoint_type(instance):
    assert isinstance(instance.bendpoint, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_bendpoint_setter(instance):
    original = instance.bendpoint
    instance.bendpoint = original
    assert instance.bendpoint == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_target_kind_type(instance):
    assert isinstance(instance.target_kind, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_target_kind_setter(instance):
    original = instance.target_kind
    instance.target_kind = original
    assert instance.target_kind == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_constraint_name_type(instance):
    assert isinstance(instance.constraint_name, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_constraint_name_setter(instance):
    original = instance.constraint_name
    instance.constraint_name = original
    assert instance.constraint_name == original

@given(instance=rdb::Relation_strategy)
def test_rdb::relation_column_name_type(instance):
    assert isinstance(instance.column_name, str)


@given(instance=rdb::Relation_strategy)
def test_rdb::relation_column_name_setter(instance):
    original = instance.column_name
    instance.column_name = original
    assert instance.column_name == original

@given(instance=rdb::Table_strategy)
@settings(max_examples=50)
def test_rdb::table_instantiation(instance):
    assert isinstance(instance, rdb::Table)

@given(instance=rdb::Table_strategy)
def test_rdb::table_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rdb::Table_strategy)
def test_rdb::table_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb::Table_strategy)
def test_rdb::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdb::Table_strategy)
def test_rdb::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdb::Table_strategy)
def test_rdb::table_constraints_type(instance):
    assert isinstance(instance.constraints, str)


@given(instance=rdb::Table_strategy)
def test_rdb::table_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original

@given(instance=rdb::Table_strategy)
def test_rdb::table_logicalName_type(instance):
    assert isinstance(instance.logicalName, str)


@given(instance=rdb::Table_strategy)
def test_rdb::table_logicalName_setter(instance):
    original = instance.logicalName
    instance.logicalName = original
    assert instance.logicalName == original

@given(instance=ERDInfo_strategy)
@settings(max_examples=50)
def test_erdinfo_instantiation(instance):
    assert isinstance(instance, ERDInfo)

@given(instance=rdb::DB_strategy)
@settings(max_examples=50)
def test_rdb::db_instantiation(instance):
    assert isinstance(instance, rdb::DB)

@given(instance=rdb::DB_strategy)
def test_rdb::db_sid_type(instance):
    assert isinstance(instance.sid, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_sid_setter(instance):
    original = instance.sid
    instance.sid = original
    assert instance.sid == original

@given(instance=rdb::DB_strategy)
def test_rdb::db_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb::DB_strategy)
def test_rdb::db_dbType_type(instance):
    assert isinstance(instance.dbType, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_dbType_setter(instance):
    original = instance.dbType
    instance.dbType = original
    assert instance.dbType == original

@given(instance=rdb::DB_strategy)
def test_rdb::db_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=rdb::DB_strategy)
def test_rdb::db_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=rdb::DB_strategy)
def test_rdb::db_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=rdb::DB_strategy)
def test_rdb::db_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original
