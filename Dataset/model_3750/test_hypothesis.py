import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdb_ERDInfo,
    Table,
    rdb_View,
    ERDInfo,
    rdb_DB,
    rdb_Column,
    rdb_Style,
    rdb_UserComment,
    rdb_Relation,
    rdb_Table,
    RelationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdb_erdinfo_is_not_abstract():
    assert not inspect.isabstract(rdb_ERDInfo)


def test_rdb_erdinfo_constructor_exists():
    assert callable(rdb_ERDInfo.__init__)


def test_rdb_erdinfo_constructor_args():
    sig = inspect.signature(rdb_ERDInfo.__init__)
    params = list(sig.parameters.keys())
    assert "autoLayout" in params, "Missing parameter 'autoLayout'"
    assert "version" in params, "Missing parameter 'version'"

def test_rdb_erdinfo_has_autoLayout():
    assert hasattr(rdb_ERDInfo, "autoLayout")
    descriptor = None
    for klass in rdb_ERDInfo.__mro__:
        if "autoLayout" in klass.__dict__:
            descriptor = klass.__dict__["autoLayout"]
            break
    assert isinstance(descriptor, property)

def test_rdb_erdinfo_has_version():
    assert hasattr(rdb_ERDInfo, "version")
    descriptor = None
    for klass in rdb_ERDInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_rdb_view_is_not_abstract():
    assert not inspect.isabstract(rdb_View)


def test_rdb_view_constructor_exists():
    assert callable(rdb_View.__init__)


def test_rdb_view_constructor_args():
    sig = inspect.signature(rdb_View.__init__)
    params = list(sig.parameters.keys())



def test_erdinfo_is_not_abstract():
    assert not inspect.isabstract(ERDInfo)


def test_erdinfo_constructor_exists():
    assert callable(ERDInfo.__init__)


def test_erdinfo_constructor_args():
    sig = inspect.signature(ERDInfo.__init__)
    params = list(sig.parameters.keys())



def test_rdb_db_is_not_abstract():
    assert not inspect.isabstract(rdb_DB)


def test_rdb_db_constructor_exists():
    assert callable(rdb_DB.__init__)


def test_rdb_db_constructor_args():
    sig = inspect.signature(rdb_DB.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "sid" in params, "Missing parameter 'sid'"
    assert "url" in params, "Missing parameter 'url'"
    assert "dbType" in params, "Missing parameter 'dbType'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "key" in params, "Missing parameter 'key'"

def test_rdb_db_has_id():
    assert hasattr(rdb_DB, "id")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rdb_db_has_sid():
    assert hasattr(rdb_DB, "sid")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "sid" in klass.__dict__:
            descriptor = klass.__dict__["sid"]
            break
    assert isinstance(descriptor, property)

def test_rdb_db_has_url():
    assert hasattr(rdb_DB, "url")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_rdb_db_has_dbType():
    assert hasattr(rdb_DB, "dbType")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "dbType" in klass.__dict__:
            descriptor = klass.__dict__["dbType"]
            break
    assert isinstance(descriptor, property)

def test_rdb_db_has_comment():
    assert hasattr(rdb_DB, "comment")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb_db_has_key():
    assert hasattr(rdb_DB, "key")
    descriptor = None
    for klass in rdb_DB.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_rdb_column_is_not_abstract():
    assert not inspect.isabstract(rdb_Column)


def test_rdb_column_constructor_exists():
    assert callable(rdb_Column.__init__)


def test_rdb_column_constructor_args():
    sig = inspect.signature(rdb_Column.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"
    assert "logicalField" in params, "Missing parameter 'logicalField'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "default" in params, "Missing parameter 'default'"
    assert "extra" in params, "Missing parameter 'extra'"
    assert "null" in params, "Missing parameter 'null'"
    assert "key" in params, "Missing parameter 'key'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdb_column_has_field():
    assert hasattr(rdb_Column, "field")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_logicalField():
    assert hasattr(rdb_Column, "logicalField")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "logicalField" in klass.__dict__:
            descriptor = klass.__dict__["logicalField"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_comment():
    assert hasattr(rdb_Column, "comment")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_default():
    assert hasattr(rdb_Column, "default")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_extra():
    assert hasattr(rdb_Column, "extra")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_null():
    assert hasattr(rdb_Column, "null")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_key():
    assert hasattr(rdb_Column, "key")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_type():
    assert hasattr(rdb_Column, "type")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdb_style_is_not_abstract():
    assert not inspect.isabstract(rdb_Style)


def test_rdb_style_constructor_exists():
    assert callable(rdb_Style.__init__)


def test_rdb_style_constructor_args():
    sig = inspect.signature(rdb_Style.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "columnType" in params, "Missing parameter 'columnType'"
    assert "columnPrimaryKey" in params, "Missing parameter 'columnPrimaryKey'"
    assert "columnComment" in params, "Missing parameter 'columnComment'"
    assert "columnNullCheck" in params, "Missing parameter 'columnNullCheck'"
    assert "tableTitle" in params, "Missing parameter 'tableTitle'"
    assert "grid" in params, "Missing parameter 'grid'"

def test_rdb_style_has_scale():
    assert hasattr(rdb_Style, "scale")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_columnName():
    assert hasattr(rdb_Style, "columnName")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_columnType():
    assert hasattr(rdb_Style, "columnType")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "columnType" in klass.__dict__:
            descriptor = klass.__dict__["columnType"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_columnPrimaryKey():
    assert hasattr(rdb_Style, "columnPrimaryKey")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "columnPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["columnPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_columnComment():
    assert hasattr(rdb_Style, "columnComment")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_columnNullCheck():
    assert hasattr(rdb_Style, "columnNullCheck")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "columnNullCheck" in klass.__dict__:
            descriptor = klass.__dict__["columnNullCheck"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_tableTitle():
    assert hasattr(rdb_Style, "tableTitle")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "tableTitle" in klass.__dict__:
            descriptor = klass.__dict__["tableTitle"]
            break
    assert isinstance(descriptor, property)

def test_rdb_style_has_grid():
    assert hasattr(rdb_Style, "grid")
    descriptor = None
    for klass in rdb_Style.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)



def test_rdb_usercomment_is_not_abstract():
    assert not inspect.isabstract(rdb_UserComment)


def test_rdb_usercomment_constructor_exists():
    assert callable(rdb_UserComment.__init__)


def test_rdb_usercomment_constructor_args():
    sig = inspect.signature(rdb_UserComment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_rdb_usercomment_has_comment():
    assert hasattr(rdb_UserComment, "comment")
    descriptor = None
    for klass in rdb_UserComment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_rdb_relation_is_not_abstract():
    assert not inspect.isabstract(rdb_Relation)


def test_rdb_relation_constructor_exists():
    assert callable(rdb_Relation.__init__)


def test_rdb_relation_constructor_args():
    sig = inspect.signature(rdb_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "column_name" in params, "Missing parameter 'column_name'"
    assert "referenced_column_name" in params, "Missing parameter 'referenced_column_name'"
    assert "target_kind" in params, "Missing parameter 'target_kind'"
    assert "constraint_name" in params, "Missing parameter 'constraint_name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "bendpoint" in params, "Missing parameter 'bendpoint'"
    assert "source_kind" in params, "Missing parameter 'source_kind'"

def test_rdb_relation_has_column_name():
    assert hasattr(rdb_Relation, "column_name")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "column_name" in klass.__dict__:
            descriptor = klass.__dict__["column_name"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_referenced_column_name():
    assert hasattr(rdb_Relation, "referenced_column_name")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "referenced_column_name" in klass.__dict__:
            descriptor = klass.__dict__["referenced_column_name"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_target_kind():
    assert hasattr(rdb_Relation, "target_kind")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "target_kind" in klass.__dict__:
            descriptor = klass.__dict__["target_kind"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_constraint_name():
    assert hasattr(rdb_Relation, "constraint_name")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "constraint_name" in klass.__dict__:
            descriptor = klass.__dict__["constraint_name"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_type():
    assert hasattr(rdb_Relation, "type")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_comment():
    assert hasattr(rdb_Relation, "comment")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_bendpoint():
    assert hasattr(rdb_Relation, "bendpoint")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "bendpoint" in klass.__dict__:
            descriptor = klass.__dict__["bendpoint"]
            break
    assert isinstance(descriptor, property)

def test_rdb_relation_has_source_kind():
    assert hasattr(rdb_Relation, "source_kind")
    descriptor = None
    for klass in rdb_Relation.__mro__:
        if "source_kind" in klass.__dict__:
            descriptor = klass.__dict__["source_kind"]
            break
    assert isinstance(descriptor, property)



def test_rdb_table_is_not_abstract():
    assert not inspect.isabstract(rdb_Table)


def test_rdb_table_constructor_exists():
    assert callable(rdb_Table.__init__)


def test_rdb_table_constructor_args():
    sig = inspect.signature(rdb_Table.__init__)
    params = list(sig.parameters.keys())
    assert "constraints" in params, "Missing parameter 'constraints'"
    assert "name" in params, "Missing parameter 'name'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "logicalName" in params, "Missing parameter 'logicalName'"

def test_rdb_table_has_constraints():
    assert hasattr(rdb_Table, "constraints")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)

def test_rdb_table_has_name():
    assert hasattr(rdb_Table, "name")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdb_table_has_schema():
    assert hasattr(rdb_Table, "schema")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_rdb_table_has_comment():
    assert hasattr(rdb_Table, "comment")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rdb_table_has_logicalName():
    assert hasattr(rdb_Table, "logicalName")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "logicalName" in klass.__dict__:
            descriptor = klass.__dict__["logicalName"]
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
        "ZERO_OR_ONE",
        "ONLY_ONE",
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
rdb_ERDInfo_strategy = st.builds(
    rdb_ERDInfo,
    autoLayout=
        st.booleans(),
    version=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
rdb_View_strategy = st.builds(
    rdb_View,
)
ERDInfo_strategy = st.builds(
    ERDInfo,
)
rdb_DB_strategy = st.builds(
    rdb_DB,
    id=
        safe_text,
    sid=
        safe_text,
    url=
        safe_text,
    dbType=
        safe_text,
    comment=
        safe_text,
    key=
        safe_text
)
rdb_Column_strategy = st.builds(
    rdb_Column,
    field=
        safe_text,
    logicalField=
        safe_text,
    comment=
        safe_text,
    default=
        safe_text,
    extra=
        safe_text,
    null=
        safe_text,
    key=
        safe_text,
    type=
        safe_text
)
rdb_Style_strategy = st.builds(
    rdb_Style,
    scale=
        safe_text,
    columnName=
        safe_text,
    columnType=
        safe_text,
    columnPrimaryKey=
        safe_text,
    columnComment=
        safe_text,
    columnNullCheck=
        safe_text,
    tableTitle=
        safe_text,
    grid=
        safe_text
)
rdb_UserComment_strategy = st.builds(
    rdb_UserComment,
    comment=
        safe_text
)
rdb_Relation_strategy = st.builds(
    rdb_Relation,
    column_name=
        safe_text,
    referenced_column_name=
        safe_text,
    target_kind=
        safe_text,
    constraint_name=
        safe_text,
    type=
        safe_text,
    comment=
        safe_text,
    bendpoint=
        safe_text,
    source_kind=
        safe_text
)
rdb_Table_strategy = st.builds(
    rdb_Table,
    constraints=
        safe_text,
    name=
        safe_text,
    schema=
        safe_text,
    comment=
        safe_text,
    logicalName=
        safe_text
)

@given(instance=rdb_ERDInfo_strategy)
@settings(max_examples=50)
def test_rdb_erdinfo_instantiation(instance):
    assert isinstance(instance, rdb_ERDInfo)



@given(instance=rdb_ERDInfo_strategy)
def test_rdb_erdinfo_autoLayout_setter(instance):
    original = instance.autoLayout
    instance.autoLayout = original
    assert instance.autoLayout == original



@given(instance=rdb_ERDInfo_strategy)
def test_rdb_erdinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=rdb_View_strategy)
@settings(max_examples=50)
def test_rdb_view_instantiation(instance):
    assert isinstance(instance, rdb_View)

@given(instance=ERDInfo_strategy)
@settings(max_examples=50)
def test_erdinfo_instantiation(instance):
    assert isinstance(instance, ERDInfo)

@given(instance=rdb_DB_strategy)
@settings(max_examples=50)
def test_rdb_db_instantiation(instance):
    assert isinstance(instance, rdb_DB)



@given(instance=rdb_DB_strategy)
def test_rdb_db_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=rdb_DB_strategy)
def test_rdb_db_sid_setter(instance):
    original = instance.sid
    instance.sid = original
    assert instance.sid == original



@given(instance=rdb_DB_strategy)
def test_rdb_db_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=rdb_DB_strategy)
def test_rdb_db_dbType_setter(instance):
    original = instance.dbType
    instance.dbType = original
    assert instance.dbType == original



@given(instance=rdb_DB_strategy)
def test_rdb_db_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rdb_DB_strategy)
def test_rdb_db_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=rdb_Column_strategy)
@settings(max_examples=50)
def test_rdb_column_instantiation(instance):
    assert isinstance(instance, rdb_Column)



@given(instance=rdb_Column_strategy)
def test_rdb_column_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_logicalField_setter(instance):
    original = instance.logicalField
    instance.logicalField = original
    assert instance.logicalField == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdb_Style_strategy)
@settings(max_examples=50)
def test_rdb_style_instantiation(instance):
    assert isinstance(instance, rdb_Style)



@given(instance=rdb_Style_strategy)
def test_rdb_style_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_columnType_setter(instance):
    original = instance.columnType
    instance.columnType = original
    assert instance.columnType == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_columnPrimaryKey_setter(instance):
    original = instance.columnPrimaryKey
    instance.columnPrimaryKey = original
    assert instance.columnPrimaryKey == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_columnNullCheck_setter(instance):
    original = instance.columnNullCheck
    instance.columnNullCheck = original
    assert instance.columnNullCheck == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_tableTitle_setter(instance):
    original = instance.tableTitle
    instance.tableTitle = original
    assert instance.tableTitle == original



@given(instance=rdb_Style_strategy)
def test_rdb_style_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original

@given(instance=rdb_UserComment_strategy)
@settings(max_examples=50)
def test_rdb_usercomment_instantiation(instance):
    assert isinstance(instance, rdb_UserComment)



@given(instance=rdb_UserComment_strategy)
def test_rdb_usercomment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rdb_Relation_strategy)
@settings(max_examples=50)
def test_rdb_relation_instantiation(instance):
    assert isinstance(instance, rdb_Relation)



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_column_name_setter(instance):
    original = instance.column_name
    instance.column_name = original
    assert instance.column_name == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_referenced_column_name_setter(instance):
    original = instance.referenced_column_name
    instance.referenced_column_name = original
    assert instance.referenced_column_name == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_target_kind_setter(instance):
    original = instance.target_kind
    instance.target_kind = original
    assert instance.target_kind == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_constraint_name_setter(instance):
    original = instance.constraint_name
    instance.constraint_name = original
    assert instance.constraint_name == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_bendpoint_setter(instance):
    original = instance.bendpoint
    instance.bendpoint = original
    assert instance.bendpoint == original



@given(instance=rdb_Relation_strategy)
def test_rdb_relation_source_kind_setter(instance):
    original = instance.source_kind
    instance.source_kind = original
    assert instance.source_kind == original

@given(instance=rdb_Table_strategy)
@settings(max_examples=50)
def test_rdb_table_instantiation(instance):
    assert isinstance(instance, rdb_Table)



@given(instance=rdb_Table_strategy)
def test_rdb_table_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original



@given(instance=rdb_Table_strategy)
def test_rdb_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdb_Table_strategy)
def test_rdb_table_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=rdb_Table_strategy)
def test_rdb_table_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rdb_Table_strategy)
def test_rdb_table_logicalName_setter(instance):
    original = instance.logicalName
    instance.logicalName = original
    assert instance.logicalName == original
