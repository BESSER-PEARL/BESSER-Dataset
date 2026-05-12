import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SqlDateTime,
    ddlDsl_SqlTimeStamp,
    ddlDsl_SqlInterval,
    ddlDsl_SqlDate,
    SqlDataType,
    ddlDsl_LongRaw,
    ddlDsl_SqlNumber,
    ddlDsl_LargeObjectType,
    ddlDsl_SqlDateTime,
    ddlDsl_RowIdType,
    ddlDsl_SqlBoolean,
    ddlDsl_SqlCharacter,
    Constraint,
    ddlDsl_UniqueKeyConstraint,
    ddlDsl_ForeignKeyConstraint,
    ddlDsl_PrimaryKeyConstraint,
    ddlDsl_NullableConstraint,
    ddlDsl_ReferenceClause,
    LongRaw,
    ddlDsl_Raw,
    ddlDsl_Long,
    TableProperty,
    ddlDsl_TableProperty,
    Create,
    ddlDsl_CreateIndex,
    ddlDsl_Column,
    Comment,
    ddlDsl_ColumnComment,
    ddlDsl_TableComment,
    AlterTableAction,
    ddlDsl_AddTableConstraint,
    ddlDsl_DropTableConstraint,
    ddlDsl_Constraint,
    ddlDsl_AlterTableAction,
    ddlDsl_CreateTable,
    DdlStatement,
    ddlDsl_Comment,
    ddlDsl_Create,
    ddlDsl_Drop,
    ddlDsl_Alter,
    ddlDsl_SqlDataType,
    ddlDsl_DdlStatement,
    ddlDsl_Ddl,
    SortDirectionEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqldatetime_is_not_abstract():
    assert not inspect.isabstract(SqlDateTime)


def test_sqldatetime_constructor_exists():
    assert callable(SqlDateTime.__init__)


def test_sqldatetime_constructor_args():
    sig = inspect.signature(SqlDateTime.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_sqltimestamp_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlTimeStamp)


def test_ddldsl_sqltimestamp_constructor_exists():
    assert callable(ddlDsl_SqlTimeStamp.__init__)


def test_ddldsl_sqltimestamp_constructor_args():
    sig = inspect.signature(ddlDsl_SqlTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddldsl_sqltimestamp_has_precision():
    assert hasattr(ddlDsl_SqlTimeStamp, "precision")
    descriptor = None
    for klass in ddlDsl_SqlTimeStamp.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_sqlinterval_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlInterval)


def test_ddldsl_sqlinterval_constructor_exists():
    assert callable(ddlDsl_SqlInterval.__init__)


def test_ddldsl_sqlinterval_constructor_args():
    sig = inspect.signature(ddlDsl_SqlInterval.__init__)
    params = list(sig.parameters.keys())
    assert "secondsPrecision" in params, "Missing parameter 'secondsPrecision'"
    assert "day" in params, "Missing parameter 'day'"
    assert "year" in params, "Missing parameter 'year'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddldsl_sqlinterval_has_secondsPrecision():
    assert hasattr(ddlDsl_SqlInterval, "secondsPrecision")
    descriptor = None
    for klass in ddlDsl_SqlInterval.__mro__:
        if "secondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["secondsPrecision"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlinterval_has_day():
    assert hasattr(ddlDsl_SqlInterval, "day")
    descriptor = None
    for klass in ddlDsl_SqlInterval.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlinterval_has_year():
    assert hasattr(ddlDsl_SqlInterval, "year")
    descriptor = None
    for klass in ddlDsl_SqlInterval.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlinterval_has_precision():
    assert hasattr(ddlDsl_SqlInterval, "precision")
    descriptor = None
    for klass in ddlDsl_SqlInterval.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_sqldate_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlDate)


def test_ddldsl_sqldate_constructor_exists():
    assert callable(ddlDsl_SqlDate.__init__)


def test_ddldsl_sqldate_constructor_args():
    sig = inspect.signature(ddlDsl_SqlDate.__init__)
    params = list(sig.parameters.keys())



def test_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SqlDataType)


def test_sqldatatype_constructor_exists():
    assert callable(SqlDataType.__init__)


def test_sqldatatype_constructor_args():
    sig = inspect.signature(SqlDataType.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_longraw_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_LongRaw)


def test_ddldsl_longraw_constructor_exists():
    assert callable(ddlDsl_LongRaw.__init__)


def test_ddldsl_longraw_constructor_args():
    sig = inspect.signature(ddlDsl_LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_sqlnumber_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlNumber)


def test_ddldsl_sqlnumber_constructor_exists():
    assert callable(ddlDsl_SqlNumber.__init__)


def test_ddldsl_sqlnumber_constructor_args():
    sig = inspect.signature(ddlDsl_SqlNumber.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "hasPrecision" in params, "Missing parameter 'hasPrecision'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_ddldsl_sqlnumber_has_precision():
    assert hasattr(ddlDsl_SqlNumber, "precision")
    descriptor = None
    for klass in ddlDsl_SqlNumber.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlnumber_has_hasPrecision():
    assert hasattr(ddlDsl_SqlNumber, "hasPrecision")
    descriptor = None
    for klass in ddlDsl_SqlNumber.__mro__:
        if "hasPrecision" in klass.__dict__:
            descriptor = klass.__dict__["hasPrecision"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlnumber_has_scale():
    assert hasattr(ddlDsl_SqlNumber, "scale")
    descriptor = None
    for klass in ddlDsl_SqlNumber.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_largeobjecttype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_LargeObjectType)


def test_ddldsl_largeobjecttype_constructor_exists():
    assert callable(ddlDsl_LargeObjectType.__init__)


def test_ddldsl_largeobjecttype_constructor_args():
    sig = inspect.signature(ddlDsl_LargeObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl_largeobjecttype_has_size():
    assert hasattr(ddlDsl_LargeObjectType, "size")
    descriptor = None
    for klass in ddlDsl_LargeObjectType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_sqldatetime_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlDateTime)


def test_ddldsl_sqldatetime_constructor_exists():
    assert callable(ddlDsl_SqlDateTime.__init__)


def test_ddldsl_sqldatetime_constructor_args():
    sig = inspect.signature(ddlDsl_SqlDateTime.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_rowidtype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_RowIdType)


def test_ddldsl_rowidtype_constructor_exists():
    assert callable(ddlDsl_RowIdType.__init__)


def test_ddldsl_rowidtype_constructor_args():
    sig = inspect.signature(ddlDsl_RowIdType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl_rowidtype_has_size():
    assert hasattr(ddlDsl_RowIdType, "size")
    descriptor = None
    for klass in ddlDsl_RowIdType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_sqlboolean_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlBoolean)


def test_ddldsl_sqlboolean_constructor_exists():
    assert callable(ddlDsl_SqlBoolean.__init__)


def test_ddldsl_sqlboolean_constructor_args():
    sig = inspect.signature(ddlDsl_SqlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_sqlcharacter_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlCharacter)


def test_ddldsl_sqlcharacter_constructor_exists():
    assert callable(ddlDsl_SqlCharacter.__init__)


def test_ddldsl_sqlcharacter_constructor_args():
    sig = inspect.signature(ddlDsl_SqlCharacter.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "national" in params, "Missing parameter 'national'"

def test_ddldsl_sqlcharacter_has_size():
    assert hasattr(ddlDsl_SqlCharacter, "size")
    descriptor = None
    for klass in ddlDsl_SqlCharacter.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_sqlcharacter_has_national():
    assert hasattr(ddlDsl_SqlCharacter, "national")
    descriptor = None
    for klass in ddlDsl_SqlCharacter.__mro__:
        if "national" in klass.__dict__:
            descriptor = klass.__dict__["national"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_uniquekeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_UniqueKeyConstraint)


def test_ddldsl_uniquekeyconstraint_constructor_exists():
    assert callable(ddlDsl_UniqueKeyConstraint.__init__)


def test_ddldsl_uniquekeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_UniqueKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_foreignkeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_ForeignKeyConstraint)


def test_ddldsl_foreignkeyconstraint_constructor_exists():
    assert callable(ddlDsl_ForeignKeyConstraint.__init__)


def test_ddldsl_foreignkeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_ForeignKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_primarykeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_PrimaryKeyConstraint)


def test_ddldsl_primarykeyconstraint_constructor_exists():
    assert callable(ddlDsl_PrimaryKeyConstraint.__init__)


def test_ddldsl_primarykeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_PrimaryKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_nullableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_NullableConstraint)


def test_ddldsl_nullableconstraint_constructor_exists():
    assert callable(ddlDsl_NullableConstraint.__init__)


def test_ddldsl_nullableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_NullableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_ddldsl_nullableconstraint_has_not_():
    assert hasattr(ddlDsl_NullableConstraint, "not_")
    descriptor = None
    for klass in ddlDsl_NullableConstraint.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_referenceclause_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_ReferenceClause)


def test_ddldsl_referenceclause_constructor_exists():
    assert callable(ddlDsl_ReferenceClause.__init__)


def test_ddldsl_referenceclause_constructor_args():
    sig = inspect.signature(ddlDsl_ReferenceClause.__init__)
    params = list(sig.parameters.keys())



def test_longraw_is_not_abstract():
    assert not inspect.isabstract(LongRaw)


def test_longraw_constructor_exists():
    assert callable(LongRaw.__init__)


def test_longraw_constructor_args():
    sig = inspect.signature(LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_raw_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Raw)


def test_ddldsl_raw_constructor_exists():
    assert callable(ddlDsl_Raw.__init__)


def test_ddldsl_raw_constructor_args():
    sig = inspect.signature(ddlDsl_Raw.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl_raw_has_size():
    assert hasattr(ddlDsl_Raw, "size")
    descriptor = None
    for klass in ddlDsl_Raw.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_long_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Long)


def test_ddldsl_long_constructor_exists():
    assert callable(ddlDsl_Long.__init__)


def test_ddldsl_long_constructor_args():
    sig = inspect.signature(ddlDsl_Long.__init__)
    params = list(sig.parameters.keys())
    assert "raw" in params, "Missing parameter 'raw'"

def test_ddldsl_long_has_raw():
    assert hasattr(ddlDsl_Long, "raw")
    descriptor = None
    for klass in ddlDsl_Long.__mro__:
        if "raw" in klass.__dict__:
            descriptor = klass.__dict__["raw"]
            break
    assert isinstance(descriptor, property)



def test_tableproperty_is_not_abstract():
    assert not inspect.isabstract(TableProperty)


def test_tableproperty_constructor_exists():
    assert callable(TableProperty.__init__)


def test_tableproperty_constructor_args():
    sig = inspect.signature(TableProperty.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_tableproperty_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_TableProperty)


def test_ddldsl_tableproperty_constructor_exists():
    assert callable(ddlDsl_TableProperty.__init__)


def test_ddldsl_tableproperty_constructor_args():
    sig = inspect.signature(ddlDsl_TableProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl_tableproperty_has_name():
    assert hasattr(ddlDsl_TableProperty, "name")
    descriptor = None
    for klass in ddlDsl_TableProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_create_is_not_abstract():
    assert not inspect.isabstract(Create)


def test_create_constructor_exists():
    assert callable(Create.__init__)


def test_create_constructor_args():
    sig = inspect.signature(Create.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_createindex_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_CreateIndex)


def test_ddldsl_createindex_constructor_exists():
    assert callable(ddlDsl_CreateIndex.__init__)


def test_ddldsl_createindex_constructor_args():
    sig = inspect.signature(ddlDsl_CreateIndex.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "sortOrders" in params, "Missing parameter 'sortOrders'"

def test_ddldsl_createindex_has_unique():
    assert hasattr(ddlDsl_CreateIndex, "unique")
    descriptor = None
    for klass in ddlDsl_CreateIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_createindex_has_sortOrders():
    assert hasattr(ddlDsl_CreateIndex, "sortOrders")
    descriptor = None
    for klass in ddlDsl_CreateIndex.__mro__:
        if "sortOrders" in klass.__dict__:
            descriptor = klass.__dict__["sortOrders"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_column_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Column)


def test_ddldsl_column_constructor_exists():
    assert callable(ddlDsl_Column.__init__)


def test_ddldsl_column_constructor_args():
    sig = inspect.signature(ddlDsl_Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "sorted" in params, "Missing parameter 'sorted'"

def test_ddldsl_column_has_default():
    assert hasattr(ddlDsl_Column, "default")
    descriptor = None
    for klass in ddlDsl_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl_column_has_sorted():
    assert hasattr(ddlDsl_Column, "sorted")
    descriptor = None
    for klass in ddlDsl_Column.__mro__:
        if "sorted" in klass.__dict__:
            descriptor = klass.__dict__["sorted"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_columncomment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_ColumnComment)


def test_ddldsl_columncomment_constructor_exists():
    assert callable(ddlDsl_ColumnComment.__init__)


def test_ddldsl_columncomment_constructor_args():
    sig = inspect.signature(ddlDsl_ColumnComment.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_tablecomment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_TableComment)


def test_ddldsl_tablecomment_constructor_exists():
    assert callable(ddlDsl_TableComment.__init__)


def test_ddldsl_tablecomment_constructor_args():
    sig = inspect.signature(ddlDsl_TableComment.__init__)
    params = list(sig.parameters.keys())



def test_altertableaction_is_not_abstract():
    assert not inspect.isabstract(AlterTableAction)


def test_altertableaction_constructor_exists():
    assert callable(AlterTableAction.__init__)


def test_altertableaction_constructor_args():
    sig = inspect.signature(AlterTableAction.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_addtableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_AddTableConstraint)


def test_ddldsl_addtableconstraint_constructor_exists():
    assert callable(ddlDsl_AddTableConstraint.__init__)


def test_ddldsl_addtableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_AddTableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl_addtableconstraint_has_name():
    assert hasattr(ddlDsl_AddTableConstraint, "name")
    descriptor = None
    for klass in ddlDsl_AddTableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_droptableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_DropTableConstraint)


def test_ddldsl_droptableconstraint_constructor_exists():
    assert callable(ddlDsl_DropTableConstraint.__init__)


def test_ddldsl_droptableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl_DropTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_constraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Constraint)


def test_ddldsl_constraint_constructor_exists():
    assert callable(ddlDsl_Constraint.__init__)


def test_ddldsl_constraint_constructor_args():
    sig = inspect.signature(ddlDsl_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_altertableaction_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_AlterTableAction)


def test_ddldsl_altertableaction_constructor_exists():
    assert callable(ddlDsl_AlterTableAction.__init__)


def test_ddldsl_altertableaction_constructor_args():
    sig = inspect.signature(ddlDsl_AlterTableAction.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_createtable_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_CreateTable)


def test_ddldsl_createtable_constructor_exists():
    assert callable(ddlDsl_CreateTable.__init__)


def test_ddldsl_createtable_constructor_args():
    sig = inspect.signature(ddlDsl_CreateTable.__init__)
    params = list(sig.parameters.keys())



def test_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(DdlStatement)


def test_ddlstatement_constructor_exists():
    assert callable(DdlStatement.__init__)


def test_ddlstatement_constructor_args():
    sig = inspect.signature(DdlStatement.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_comment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Comment)


def test_ddldsl_comment_constructor_exists():
    assert callable(ddlDsl_Comment.__init__)


def test_ddldsl_comment_constructor_args():
    sig = inspect.signature(ddlDsl_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_ddldsl_comment_has_comment():
    assert hasattr(ddlDsl_Comment, "comment")
    descriptor = None
    for klass in ddlDsl_Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_create_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Create)


def test_ddldsl_create_constructor_exists():
    assert callable(ddlDsl_Create.__init__)


def test_ddldsl_create_constructor_args():
    sig = inspect.signature(ddlDsl_Create.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl_create_has_name():
    assert hasattr(ddlDsl_Create, "name")
    descriptor = None
    for klass in ddlDsl_Create.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_drop_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Drop)


def test_ddldsl_drop_constructor_exists():
    assert callable(ddlDsl_Drop.__init__)


def test_ddldsl_drop_constructor_args():
    sig = inspect.signature(ddlDsl_Drop.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"

def test_ddldsl_drop_has_object():
    assert hasattr(ddlDsl_Drop, "object")
    descriptor = None
    for klass in ddlDsl_Drop.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_alter_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Alter)


def test_ddldsl_alter_constructor_exists():
    assert callable(ddlDsl_Alter.__init__)


def test_ddldsl_alter_constructor_args():
    sig = inspect.signature(ddlDsl_Alter.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_SqlDataType)


def test_ddldsl_sqldatatype_constructor_exists():
    assert callable(ddlDsl_SqlDataType.__init__)


def test_ddldsl_sqldatatype_constructor_args():
    sig = inspect.signature(ddlDsl_SqlDataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl_sqldatatype_has_name():
    assert hasattr(ddlDsl_SqlDataType, "name")
    descriptor = None
    for klass in ddlDsl_SqlDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_DdlStatement)


def test_ddldsl_ddlstatement_constructor_exists():
    assert callable(ddlDsl_DdlStatement.__init__)


def test_ddldsl_ddlstatement_constructor_args():
    sig = inspect.signature(ddlDsl_DdlStatement.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl_ddl_is_not_abstract():
    assert not inspect.isabstract(ddlDsl_Ddl)


def test_ddldsl_ddl_constructor_exists():
    assert callable(ddlDsl_Ddl.__init__)


def test_ddldsl_ddl_constructor_args():
    sig = inspect.signature(ddlDsl_Ddl.__init__)
    params = list(sig.parameters.keys())

def test_sortdirectionenum_exists():
    # Check that the Enumeration exists
    assert SortDirectionEnum is not None

def test_sortdirectionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortDirectionEnum]
    expected_literals = [
        "DESC",
        "ASC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortDirectionEnum"


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
SqlDateTime_strategy = st.builds(
    SqlDateTime,
)
ddlDsl_SqlTimeStamp_strategy = st.builds(
    ddlDsl_SqlTimeStamp,
    precision=
        st.integers()
)
ddlDsl_SqlInterval_strategy = st.builds(
    ddlDsl_SqlInterval,
    secondsPrecision=
        st.integers(),
    day=
        st.booleans(),
    year=
        st.booleans(),
    precision=
        st.integers()
)
ddlDsl_SqlDate_strategy = st.builds(
    ddlDsl_SqlDate,
)
SqlDataType_strategy = st.builds(
    SqlDataType,
)
ddlDsl_LongRaw_strategy = st.builds(
    ddlDsl_LongRaw,
)
ddlDsl_SqlNumber_strategy = st.builds(
    ddlDsl_SqlNumber,
    precision=
        st.integers(),
    hasPrecision=
        st.booleans(),
    scale=
        st.integers()
)
ddlDsl_LargeObjectType_strategy = st.builds(
    ddlDsl_LargeObjectType,
    size=
        st.integers()
)
ddlDsl_SqlDateTime_strategy = st.builds(
    ddlDsl_SqlDateTime,
)
ddlDsl_RowIdType_strategy = st.builds(
    ddlDsl_RowIdType,
    size=
        st.integers()
)
ddlDsl_SqlBoolean_strategy = st.builds(
    ddlDsl_SqlBoolean,
)
ddlDsl_SqlCharacter_strategy = st.builds(
    ddlDsl_SqlCharacter,
    size=
        st.integers(),
    national=
        st.booleans()
)
Constraint_strategy = st.builds(
    Constraint,
)
ddlDsl_UniqueKeyConstraint_strategy = st.builds(
    ddlDsl_UniqueKeyConstraint,
)
ddlDsl_ForeignKeyConstraint_strategy = st.builds(
    ddlDsl_ForeignKeyConstraint,
)
ddlDsl_PrimaryKeyConstraint_strategy = st.builds(
    ddlDsl_PrimaryKeyConstraint,
)
ddlDsl_NullableConstraint_strategy = st.builds(
    ddlDsl_NullableConstraint,
    not_=
        st.booleans()
)
ddlDsl_ReferenceClause_strategy = st.builds(
    ddlDsl_ReferenceClause,
)
LongRaw_strategy = st.builds(
    LongRaw,
)
ddlDsl_Raw_strategy = st.builds(
    ddlDsl_Raw,
    size=
        st.integers()
)
ddlDsl_Long_strategy = st.builds(
    ddlDsl_Long,
    raw=
        st.booleans()
)
TableProperty_strategy = st.builds(
    TableProperty,
)
ddlDsl_TableProperty_strategy = st.builds(
    ddlDsl_TableProperty,
    name=
        safe_text
)
Create_strategy = st.builds(
    Create,
)
ddlDsl_CreateIndex_strategy = st.builds(
    ddlDsl_CreateIndex,
    unique=
        st.booleans(),
    sortOrders=
        safe_text
)
ddlDsl_Column_strategy = st.builds(
    ddlDsl_Column,
    default=
        safe_text,
    sorted=
        st.booleans()
)
Comment_strategy = st.builds(
    Comment,
)
ddlDsl_ColumnComment_strategy = st.builds(
    ddlDsl_ColumnComment,
)
ddlDsl_TableComment_strategy = st.builds(
    ddlDsl_TableComment,
)
AlterTableAction_strategy = st.builds(
    AlterTableAction,
)
ddlDsl_AddTableConstraint_strategy = st.builds(
    ddlDsl_AddTableConstraint,
    name=
        safe_text
)
ddlDsl_DropTableConstraint_strategy = st.builds(
    ddlDsl_DropTableConstraint,
)
ddlDsl_Constraint_strategy = st.builds(
    ddlDsl_Constraint,
)
ddlDsl_AlterTableAction_strategy = st.builds(
    ddlDsl_AlterTableAction,
)
ddlDsl_CreateTable_strategy = st.builds(
    ddlDsl_CreateTable,
)
DdlStatement_strategy = st.builds(
    DdlStatement,
)
ddlDsl_Comment_strategy = st.builds(
    ddlDsl_Comment,
    comment=
        safe_text
)
ddlDsl_Create_strategy = st.builds(
    ddlDsl_Create,
    name=
        safe_text
)
ddlDsl_Drop_strategy = st.builds(
    ddlDsl_Drop,
    object=
        safe_text
)
ddlDsl_Alter_strategy = st.builds(
    ddlDsl_Alter,
)
ddlDsl_SqlDataType_strategy = st.builds(
    ddlDsl_SqlDataType,
    name=
        safe_text
)
ddlDsl_DdlStatement_strategy = st.builds(
    ddlDsl_DdlStatement,
)
ddlDsl_Ddl_strategy = st.builds(
    ddlDsl_Ddl,
)

@given(instance=SqlDateTime_strategy)
@settings(max_examples=50)
def test_sqldatetime_instantiation(instance):
    assert isinstance(instance, SqlDateTime)

@given(instance=ddlDsl_SqlTimeStamp_strategy)
@settings(max_examples=50)
def test_ddldsl_sqltimestamp_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlTimeStamp)



@given(instance=ddlDsl_SqlTimeStamp_strategy)
def test_ddldsl_sqltimestamp_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ddlDsl_SqlInterval_strategy)
@settings(max_examples=50)
def test_ddldsl_sqlinterval_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlInterval)



@given(instance=ddlDsl_SqlInterval_strategy)
def test_ddldsl_sqlinterval_secondsPrecision_setter(instance):
    original = instance.secondsPrecision
    instance.secondsPrecision = original
    assert instance.secondsPrecision == original



@given(instance=ddlDsl_SqlInterval_strategy)
def test_ddldsl_sqlinterval_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=ddlDsl_SqlInterval_strategy)
def test_ddldsl_sqlinterval_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=ddlDsl_SqlInterval_strategy)
def test_ddldsl_sqlinterval_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ddlDsl_SqlDate_strategy)
@settings(max_examples=50)
def test_ddldsl_sqldate_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlDate)

@given(instance=SqlDataType_strategy)
@settings(max_examples=50)
def test_sqldatatype_instantiation(instance):
    assert isinstance(instance, SqlDataType)

@given(instance=ddlDsl_LongRaw_strategy)
@settings(max_examples=50)
def test_ddldsl_longraw_instantiation(instance):
    assert isinstance(instance, ddlDsl_LongRaw)

@given(instance=ddlDsl_SqlNumber_strategy)
@settings(max_examples=50)
def test_ddldsl_sqlnumber_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlNumber)



@given(instance=ddlDsl_SqlNumber_strategy)
def test_ddldsl_sqlnumber_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=ddlDsl_SqlNumber_strategy)
def test_ddldsl_sqlnumber_hasPrecision_setter(instance):
    original = instance.hasPrecision
    instance.hasPrecision = original
    assert instance.hasPrecision == original



@given(instance=ddlDsl_SqlNumber_strategy)
def test_ddldsl_sqlnumber_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ddlDsl_LargeObjectType_strategy)
@settings(max_examples=50)
def test_ddldsl_largeobjecttype_instantiation(instance):
    assert isinstance(instance, ddlDsl_LargeObjectType)



@given(instance=ddlDsl_LargeObjectType_strategy)
def test_ddldsl_largeobjecttype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl_SqlDateTime_strategy)
@settings(max_examples=50)
def test_ddldsl_sqldatetime_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlDateTime)

@given(instance=ddlDsl_RowIdType_strategy)
@settings(max_examples=50)
def test_ddldsl_rowidtype_instantiation(instance):
    assert isinstance(instance, ddlDsl_RowIdType)



@given(instance=ddlDsl_RowIdType_strategy)
def test_ddldsl_rowidtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl_SqlBoolean_strategy)
@settings(max_examples=50)
def test_ddldsl_sqlboolean_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlBoolean)

@given(instance=ddlDsl_SqlCharacter_strategy)
@settings(max_examples=50)
def test_ddldsl_sqlcharacter_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlCharacter)



@given(instance=ddlDsl_SqlCharacter_strategy)
def test_ddldsl_sqlcharacter_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ddlDsl_SqlCharacter_strategy)
def test_ddldsl_sqlcharacter_national_setter(instance):
    original = instance.national
    instance.national = original
    assert instance.national == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=ddlDsl_UniqueKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_uniquekeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_UniqueKeyConstraint)

@given(instance=ddlDsl_ForeignKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_foreignkeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_ForeignKeyConstraint)

@given(instance=ddlDsl_PrimaryKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_primarykeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_PrimaryKeyConstraint)

@given(instance=ddlDsl_NullableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_nullableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_NullableConstraint)



@given(instance=ddlDsl_NullableConstraint_strategy)
def test_ddldsl_nullableconstraint_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=ddlDsl_ReferenceClause_strategy)
@settings(max_examples=50)
def test_ddldsl_referenceclause_instantiation(instance):
    assert isinstance(instance, ddlDsl_ReferenceClause)

@given(instance=LongRaw_strategy)
@settings(max_examples=50)
def test_longraw_instantiation(instance):
    assert isinstance(instance, LongRaw)

@given(instance=ddlDsl_Raw_strategy)
@settings(max_examples=50)
def test_ddldsl_raw_instantiation(instance):
    assert isinstance(instance, ddlDsl_Raw)



@given(instance=ddlDsl_Raw_strategy)
def test_ddldsl_raw_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl_Long_strategy)
@settings(max_examples=50)
def test_ddldsl_long_instantiation(instance):
    assert isinstance(instance, ddlDsl_Long)



@given(instance=ddlDsl_Long_strategy)
def test_ddldsl_long_raw_setter(instance):
    original = instance.raw
    instance.raw = original
    assert instance.raw == original

@given(instance=TableProperty_strategy)
@settings(max_examples=50)
def test_tableproperty_instantiation(instance):
    assert isinstance(instance, TableProperty)

@given(instance=ddlDsl_TableProperty_strategy)
@settings(max_examples=50)
def test_ddldsl_tableproperty_instantiation(instance):
    assert isinstance(instance, ddlDsl_TableProperty)



@given(instance=ddlDsl_TableProperty_strategy)
def test_ddldsl_tableproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Create_strategy)
@settings(max_examples=50)
def test_create_instantiation(instance):
    assert isinstance(instance, Create)

@given(instance=ddlDsl_CreateIndex_strategy)
@settings(max_examples=50)
def test_ddldsl_createindex_instantiation(instance):
    assert isinstance(instance, ddlDsl_CreateIndex)



@given(instance=ddlDsl_CreateIndex_strategy)
def test_ddldsl_createindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=ddlDsl_CreateIndex_strategy)
def test_ddldsl_createindex_sortOrders_setter(instance):
    original = instance.sortOrders
    instance.sortOrders = original
    assert instance.sortOrders == original

@given(instance=ddlDsl_Column_strategy)
@settings(max_examples=50)
def test_ddldsl_column_instantiation(instance):
    assert isinstance(instance, ddlDsl_Column)



@given(instance=ddlDsl_Column_strategy)
def test_ddldsl_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=ddlDsl_Column_strategy)
def test_ddldsl_column_sorted_setter(instance):
    original = instance.sorted
    instance.sorted = original
    assert instance.sorted == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ddlDsl_ColumnComment_strategy)
@settings(max_examples=50)
def test_ddldsl_columncomment_instantiation(instance):
    assert isinstance(instance, ddlDsl_ColumnComment)

@given(instance=ddlDsl_TableComment_strategy)
@settings(max_examples=50)
def test_ddldsl_tablecomment_instantiation(instance):
    assert isinstance(instance, ddlDsl_TableComment)

@given(instance=AlterTableAction_strategy)
@settings(max_examples=50)
def test_altertableaction_instantiation(instance):
    assert isinstance(instance, AlterTableAction)

@given(instance=ddlDsl_AddTableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_addtableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_AddTableConstraint)



@given(instance=ddlDsl_AddTableConstraint_strategy)
def test_ddldsl_addtableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddlDsl_DropTableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl_droptableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_DropTableConstraint)

@given(instance=ddlDsl_Constraint_strategy)
@settings(max_examples=50)
def test_ddldsl_constraint_instantiation(instance):
    assert isinstance(instance, ddlDsl_Constraint)

@given(instance=ddlDsl_AlterTableAction_strategy)
@settings(max_examples=50)
def test_ddldsl_altertableaction_instantiation(instance):
    assert isinstance(instance, ddlDsl_AlterTableAction)

@given(instance=ddlDsl_CreateTable_strategy)
@settings(max_examples=50)
def test_ddldsl_createtable_instantiation(instance):
    assert isinstance(instance, ddlDsl_CreateTable)

@given(instance=DdlStatement_strategy)
@settings(max_examples=50)
def test_ddlstatement_instantiation(instance):
    assert isinstance(instance, DdlStatement)

@given(instance=ddlDsl_Comment_strategy)
@settings(max_examples=50)
def test_ddldsl_comment_instantiation(instance):
    assert isinstance(instance, ddlDsl_Comment)



@given(instance=ddlDsl_Comment_strategy)
def test_ddldsl_comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ddlDsl_Create_strategy)
@settings(max_examples=50)
def test_ddldsl_create_instantiation(instance):
    assert isinstance(instance, ddlDsl_Create)



@given(instance=ddlDsl_Create_strategy)
def test_ddldsl_create_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddlDsl_Drop_strategy)
@settings(max_examples=50)
def test_ddldsl_drop_instantiation(instance):
    assert isinstance(instance, ddlDsl_Drop)



@given(instance=ddlDsl_Drop_strategy)
def test_ddldsl_drop_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=ddlDsl_Alter_strategy)
@settings(max_examples=50)
def test_ddldsl_alter_instantiation(instance):
    assert isinstance(instance, ddlDsl_Alter)

@given(instance=ddlDsl_SqlDataType_strategy)
@settings(max_examples=50)
def test_ddldsl_sqldatatype_instantiation(instance):
    assert isinstance(instance, ddlDsl_SqlDataType)



@given(instance=ddlDsl_SqlDataType_strategy)
def test_ddldsl_sqldatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddlDsl_DdlStatement_strategy)
@settings(max_examples=50)
def test_ddldsl_ddlstatement_instantiation(instance):
    assert isinstance(instance, ddlDsl_DdlStatement)

@given(instance=ddlDsl_Ddl_strategy)
@settings(max_examples=50)
def test_ddldsl_ddl_instantiation(instance):
    assert isinstance(instance, ddlDsl_Ddl)
