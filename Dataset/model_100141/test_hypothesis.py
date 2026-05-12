import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SqlDateTime,
    ddlDsl::SqlInterval,
    ddlDsl::SqlTimeStamp,
    ddlDsl::SqlDate,
    LongRaw,
    ddlDsl::Raw,
    ddlDsl::Long,
    SqlDataType,
    ddlDsl::SqlDateTime,
    ddlDsl::RowIdType,
    ddlDsl::SqlBoolean,
    ddlDsl::LongRaw,
    ddlDsl::LargeObjectType,
    ddlDsl::SqlNumber,
    ddlDsl::SqlCharacter,
    ddlDsl::TableProperty,
    Create,
    ddlDsl::CreateIndex,
    Constraint,
    ddlDsl::PrimaryKeyConstraint,
    ddlDsl::UniqueKeyConstraint,
    ddlDsl::ForeignKeyConstraint,
    ddlDsl::NullableConstraint,
    ddlDsl::ReferenceClause,
    ddlDsl::SqlDataType,
    TableProperty,
    ddlDsl::Column,
    ddlDsl::DdlStatement,
    ddlDsl::Ddl,
    Comment,
    ddlDsl::ColumnComment,
    ddlDsl::TableComment,
    AlterTableAction,
    ddlDsl::AddTableConstraint,
    ddlDsl::DropTableConstraint,
    ddlDsl::Constraint,
    ddlDsl::AlterTableAction,
    ddlDsl::CreateTable,
    DdlStatement,
    ddlDsl::Create,
    ddlDsl::Drop,
    ddlDsl::Comment,
    ddlDsl::Alter,
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



def test_ddldsl::sqlinterval_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlInterval)


def test_ddldsl::sqlinterval_constructor_exists():
    assert callable(ddlDsl::SqlInterval.__init__)


def test_ddldsl::sqlinterval_constructor_args():
    sig = inspect.signature(ddlDsl::SqlInterval.__init__)
    params = list(sig.parameters.keys())
    assert "secondsPrecision" in params, "Missing parameter 'secondsPrecision'"
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddldsl::sqlinterval_has_secondsPrecision():
    assert hasattr(ddlDsl::SqlInterval, "secondsPrecision")
    descriptor = None
    for klass in ddlDsl::SqlInterval.__mro__:
        if "secondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["secondsPrecision"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlinterval_has_year():
    assert hasattr(ddlDsl::SqlInterval, "year")
    descriptor = None
    for klass in ddlDsl::SqlInterval.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlinterval_has_day():
    assert hasattr(ddlDsl::SqlInterval, "day")
    descriptor = None
    for klass in ddlDsl::SqlInterval.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlinterval_has_precision():
    assert hasattr(ddlDsl::SqlInterval, "precision")
    descriptor = None
    for klass in ddlDsl::SqlInterval.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::sqltimestamp_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlTimeStamp)


def test_ddldsl::sqltimestamp_constructor_exists():
    assert callable(ddlDsl::SqlTimeStamp.__init__)


def test_ddldsl::sqltimestamp_constructor_args():
    sig = inspect.signature(ddlDsl::SqlTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddldsl::sqltimestamp_has_precision():
    assert hasattr(ddlDsl::SqlTimeStamp, "precision")
    descriptor = None
    for klass in ddlDsl::SqlTimeStamp.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::sqldate_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlDate)


def test_ddldsl::sqldate_constructor_exists():
    assert callable(ddlDsl::SqlDate.__init__)


def test_ddldsl::sqldate_constructor_args():
    sig = inspect.signature(ddlDsl::SqlDate.__init__)
    params = list(sig.parameters.keys())



def test_longraw_is_not_abstract():
    assert not inspect.isabstract(LongRaw)


def test_longraw_constructor_exists():
    assert callable(LongRaw.__init__)


def test_longraw_constructor_args():
    sig = inspect.signature(LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::raw_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Raw)


def test_ddldsl::raw_constructor_exists():
    assert callable(ddlDsl::Raw.__init__)


def test_ddldsl::raw_constructor_args():
    sig = inspect.signature(ddlDsl::Raw.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl::raw_has_size():
    assert hasattr(ddlDsl::Raw, "size")
    descriptor = None
    for klass in ddlDsl::Raw.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::long_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Long)


def test_ddldsl::long_constructor_exists():
    assert callable(ddlDsl::Long.__init__)


def test_ddldsl::long_constructor_args():
    sig = inspect.signature(ddlDsl::Long.__init__)
    params = list(sig.parameters.keys())
    assert "raw" in params, "Missing parameter 'raw'"

def test_ddldsl::long_has_raw():
    assert hasattr(ddlDsl::Long, "raw")
    descriptor = None
    for klass in ddlDsl::Long.__mro__:
        if "raw" in klass.__dict__:
            descriptor = klass.__dict__["raw"]
            break
    assert isinstance(descriptor, property)



def test_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SqlDataType)


def test_sqldatatype_constructor_exists():
    assert callable(SqlDataType.__init__)


def test_sqldatatype_constructor_args():
    sig = inspect.signature(SqlDataType.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::sqldatetime_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlDateTime)


def test_ddldsl::sqldatetime_constructor_exists():
    assert callable(ddlDsl::SqlDateTime.__init__)


def test_ddldsl::sqldatetime_constructor_args():
    sig = inspect.signature(ddlDsl::SqlDateTime.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::rowidtype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::RowIdType)


def test_ddldsl::rowidtype_constructor_exists():
    assert callable(ddlDsl::RowIdType.__init__)


def test_ddldsl::rowidtype_constructor_args():
    sig = inspect.signature(ddlDsl::RowIdType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl::rowidtype_has_size():
    assert hasattr(ddlDsl::RowIdType, "size")
    descriptor = None
    for klass in ddlDsl::RowIdType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::sqlboolean_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlBoolean)


def test_ddldsl::sqlboolean_constructor_exists():
    assert callable(ddlDsl::SqlBoolean.__init__)


def test_ddldsl::sqlboolean_constructor_args():
    sig = inspect.signature(ddlDsl::SqlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::longraw_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::LongRaw)


def test_ddldsl::longraw_constructor_exists():
    assert callable(ddlDsl::LongRaw.__init__)


def test_ddldsl::longraw_constructor_args():
    sig = inspect.signature(ddlDsl::LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::largeobjecttype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::LargeObjectType)


def test_ddldsl::largeobjecttype_constructor_exists():
    assert callable(ddlDsl::LargeObjectType.__init__)


def test_ddldsl::largeobjecttype_constructor_args():
    sig = inspect.signature(ddlDsl::LargeObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_ddldsl::largeobjecttype_has_size():
    assert hasattr(ddlDsl::LargeObjectType, "size")
    descriptor = None
    for klass in ddlDsl::LargeObjectType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::sqlnumber_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlNumber)


def test_ddldsl::sqlnumber_constructor_exists():
    assert callable(ddlDsl::SqlNumber.__init__)


def test_ddldsl::sqlnumber_constructor_args():
    sig = inspect.signature(ddlDsl::SqlNumber.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "hasPrecision" in params, "Missing parameter 'hasPrecision'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddldsl::sqlnumber_has_scale():
    assert hasattr(ddlDsl::SqlNumber, "scale")
    descriptor = None
    for klass in ddlDsl::SqlNumber.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlnumber_has_hasPrecision():
    assert hasattr(ddlDsl::SqlNumber, "hasPrecision")
    descriptor = None
    for klass in ddlDsl::SqlNumber.__mro__:
        if "hasPrecision" in klass.__dict__:
            descriptor = klass.__dict__["hasPrecision"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlnumber_has_precision():
    assert hasattr(ddlDsl::SqlNumber, "precision")
    descriptor = None
    for klass in ddlDsl::SqlNumber.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::sqlcharacter_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlCharacter)


def test_ddldsl::sqlcharacter_constructor_exists():
    assert callable(ddlDsl::SqlCharacter.__init__)


def test_ddldsl::sqlcharacter_constructor_args():
    sig = inspect.signature(ddlDsl::SqlCharacter.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "national" in params, "Missing parameter 'national'"

def test_ddldsl::sqlcharacter_has_size():
    assert hasattr(ddlDsl::SqlCharacter, "size")
    descriptor = None
    for klass in ddlDsl::SqlCharacter.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::sqlcharacter_has_national():
    assert hasattr(ddlDsl::SqlCharacter, "national")
    descriptor = None
    for klass in ddlDsl::SqlCharacter.__mro__:
        if "national" in klass.__dict__:
            descriptor = klass.__dict__["national"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::tableproperty_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::TableProperty)


def test_ddldsl::tableproperty_constructor_exists():
    assert callable(ddlDsl::TableProperty.__init__)


def test_ddldsl::tableproperty_constructor_args():
    sig = inspect.signature(ddlDsl::TableProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl::tableproperty_has_name():
    assert hasattr(ddlDsl::TableProperty, "name")
    descriptor = None
    for klass in ddlDsl::TableProperty.__mro__:
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



def test_ddldsl::createindex_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::CreateIndex)


def test_ddldsl::createindex_constructor_exists():
    assert callable(ddlDsl::CreateIndex.__init__)


def test_ddldsl::createindex_constructor_args():
    sig = inspect.signature(ddlDsl::CreateIndex.__init__)
    params = list(sig.parameters.keys())
    assert "sortOrders" in params, "Missing parameter 'sortOrders'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_ddldsl::createindex_has_sortOrders():
    assert hasattr(ddlDsl::CreateIndex, "sortOrders")
    descriptor = None
    for klass in ddlDsl::CreateIndex.__mro__:
        if "sortOrders" in klass.__dict__:
            descriptor = klass.__dict__["sortOrders"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::createindex_has_unique():
    assert hasattr(ddlDsl::CreateIndex, "unique")
    descriptor = None
    for klass in ddlDsl::CreateIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::primarykeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::PrimaryKeyConstraint)


def test_ddldsl::primarykeyconstraint_constructor_exists():
    assert callable(ddlDsl::PrimaryKeyConstraint.__init__)


def test_ddldsl::primarykeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::PrimaryKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::uniquekeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::UniqueKeyConstraint)


def test_ddldsl::uniquekeyconstraint_constructor_exists():
    assert callable(ddlDsl::UniqueKeyConstraint.__init__)


def test_ddldsl::uniquekeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::UniqueKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::foreignkeyconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::ForeignKeyConstraint)


def test_ddldsl::foreignkeyconstraint_constructor_exists():
    assert callable(ddlDsl::ForeignKeyConstraint.__init__)


def test_ddldsl::foreignkeyconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::ForeignKeyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::nullableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::NullableConstraint)


def test_ddldsl::nullableconstraint_constructor_exists():
    assert callable(ddlDsl::NullableConstraint.__init__)


def test_ddldsl::nullableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::NullableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_ddldsl::nullableconstraint_has_not_():
    assert hasattr(ddlDsl::NullableConstraint, "not_")
    descriptor = None
    for klass in ddlDsl::NullableConstraint.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::referenceclause_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::ReferenceClause)


def test_ddldsl::referenceclause_constructor_exists():
    assert callable(ddlDsl::ReferenceClause.__init__)


def test_ddldsl::referenceclause_constructor_args():
    sig = inspect.signature(ddlDsl::ReferenceClause.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::sqldatatype_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::SqlDataType)


def test_ddldsl::sqldatatype_constructor_exists():
    assert callable(ddlDsl::SqlDataType.__init__)


def test_ddldsl::sqldatatype_constructor_args():
    sig = inspect.signature(ddlDsl::SqlDataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl::sqldatatype_has_name():
    assert hasattr(ddlDsl::SqlDataType, "name")
    descriptor = None
    for klass in ddlDsl::SqlDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tableproperty_is_not_abstract():
    assert not inspect.isabstract(TableProperty)


def test_tableproperty_constructor_exists():
    assert callable(TableProperty.__init__)


def test_tableproperty_constructor_args():
    sig = inspect.signature(TableProperty.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::column_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Column)


def test_ddldsl::column_constructor_exists():
    assert callable(ddlDsl::Column.__init__)


def test_ddldsl::column_constructor_args():
    sig = inspect.signature(ddlDsl::Column.__init__)
    params = list(sig.parameters.keys())
    assert "sorted" in params, "Missing parameter 'sorted'"
    assert "default" in params, "Missing parameter 'default'"

def test_ddldsl::column_has_sorted():
    assert hasattr(ddlDsl::Column, "sorted")
    descriptor = None
    for klass in ddlDsl::Column.__mro__:
        if "sorted" in klass.__dict__:
            descriptor = klass.__dict__["sorted"]
            break
    assert isinstance(descriptor, property)

def test_ddldsl::column_has_default():
    assert hasattr(ddlDsl::Column, "default")
    descriptor = None
    for klass in ddlDsl::Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::ddlstatement_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::DdlStatement)


def test_ddldsl::ddlstatement_constructor_exists():
    assert callable(ddlDsl::DdlStatement.__init__)


def test_ddldsl::ddlstatement_constructor_args():
    sig = inspect.signature(ddlDsl::DdlStatement.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::ddl_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Ddl)


def test_ddldsl::ddl_constructor_exists():
    assert callable(ddlDsl::Ddl.__init__)


def test_ddldsl::ddl_constructor_args():
    sig = inspect.signature(ddlDsl::Ddl.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::columncomment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::ColumnComment)


def test_ddldsl::columncomment_constructor_exists():
    assert callable(ddlDsl::ColumnComment.__init__)


def test_ddldsl::columncomment_constructor_args():
    sig = inspect.signature(ddlDsl::ColumnComment.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::tablecomment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::TableComment)


def test_ddldsl::tablecomment_constructor_exists():
    assert callable(ddlDsl::TableComment.__init__)


def test_ddldsl::tablecomment_constructor_args():
    sig = inspect.signature(ddlDsl::TableComment.__init__)
    params = list(sig.parameters.keys())



def test_altertableaction_is_not_abstract():
    assert not inspect.isabstract(AlterTableAction)


def test_altertableaction_constructor_exists():
    assert callable(AlterTableAction.__init__)


def test_altertableaction_constructor_args():
    sig = inspect.signature(AlterTableAction.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::addtableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::AddTableConstraint)


def test_ddldsl::addtableconstraint_constructor_exists():
    assert callable(ddlDsl::AddTableConstraint.__init__)


def test_ddldsl::addtableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::AddTableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl::addtableconstraint_has_name():
    assert hasattr(ddlDsl::AddTableConstraint, "name")
    descriptor = None
    for klass in ddlDsl::AddTableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::droptableconstraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::DropTableConstraint)


def test_ddldsl::droptableconstraint_constructor_exists():
    assert callable(ddlDsl::DropTableConstraint.__init__)


def test_ddldsl::droptableconstraint_constructor_args():
    sig = inspect.signature(ddlDsl::DropTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::constraint_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Constraint)


def test_ddldsl::constraint_constructor_exists():
    assert callable(ddlDsl::Constraint.__init__)


def test_ddldsl::constraint_constructor_args():
    sig = inspect.signature(ddlDsl::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::altertableaction_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::AlterTableAction)


def test_ddldsl::altertableaction_constructor_exists():
    assert callable(ddlDsl::AlterTableAction.__init__)


def test_ddldsl::altertableaction_constructor_args():
    sig = inspect.signature(ddlDsl::AlterTableAction.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::createtable_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::CreateTable)


def test_ddldsl::createtable_constructor_exists():
    assert callable(ddlDsl::CreateTable.__init__)


def test_ddldsl::createtable_constructor_args():
    sig = inspect.signature(ddlDsl::CreateTable.__init__)
    params = list(sig.parameters.keys())



def test_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(DdlStatement)


def test_ddlstatement_constructor_exists():
    assert callable(DdlStatement.__init__)


def test_ddlstatement_constructor_args():
    sig = inspect.signature(DdlStatement.__init__)
    params = list(sig.parameters.keys())



def test_ddldsl::create_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Create)


def test_ddldsl::create_constructor_exists():
    assert callable(ddlDsl::Create.__init__)


def test_ddldsl::create_constructor_args():
    sig = inspect.signature(ddlDsl::Create.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddldsl::create_has_name():
    assert hasattr(ddlDsl::Create, "name")
    descriptor = None
    for klass in ddlDsl::Create.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::drop_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Drop)


def test_ddldsl::drop_constructor_exists():
    assert callable(ddlDsl::Drop.__init__)


def test_ddldsl::drop_constructor_args():
    sig = inspect.signature(ddlDsl::Drop.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"

def test_ddldsl::drop_has_object():
    assert hasattr(ddlDsl::Drop, "object")
    descriptor = None
    for klass in ddlDsl::Drop.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::comment_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Comment)


def test_ddldsl::comment_constructor_exists():
    assert callable(ddlDsl::Comment.__init__)


def test_ddldsl::comment_constructor_args():
    sig = inspect.signature(ddlDsl::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_ddldsl::comment_has_comment():
    assert hasattr(ddlDsl::Comment, "comment")
    descriptor = None
    for klass in ddlDsl::Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_ddldsl::alter_is_not_abstract():
    assert not inspect.isabstract(ddlDsl::Alter)


def test_ddldsl::alter_constructor_exists():
    assert callable(ddlDsl::Alter.__init__)


def test_ddldsl::alter_constructor_args():
    sig = inspect.signature(ddlDsl::Alter.__init__)
    params = list(sig.parameters.keys())

def test_sortdirectionenum_exists():
    # Check that the Enumeration exists
    assert SortDirectionEnum is not None

def test_sortdirectionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortDirectionEnum]
    expected_literals = [
        "ASC",
        "DESC",
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
ddlDsl::SqlInterval_strategy = st.builds(
    ddlDsl::SqlInterval,
    secondsPrecision=
        st.integers(),
    year=
        st.booleans(),
    day=
        st.booleans(),
    precision=
        st.integers()
)
ddlDsl::SqlTimeStamp_strategy = st.builds(
    ddlDsl::SqlTimeStamp,
    precision=
        st.integers()
)
ddlDsl::SqlDate_strategy = st.builds(
    ddlDsl::SqlDate,
)
LongRaw_strategy = st.builds(
    LongRaw,
)
ddlDsl::Raw_strategy = st.builds(
    ddlDsl::Raw,
    size=
        st.integers()
)
ddlDsl::Long_strategy = st.builds(
    ddlDsl::Long,
    raw=
        st.booleans()
)
SqlDataType_strategy = st.builds(
    SqlDataType,
)
ddlDsl::SqlDateTime_strategy = st.builds(
    ddlDsl::SqlDateTime,
)
ddlDsl::RowIdType_strategy = st.builds(
    ddlDsl::RowIdType,
    size=
        st.integers()
)
ddlDsl::SqlBoolean_strategy = st.builds(
    ddlDsl::SqlBoolean,
)
ddlDsl::LongRaw_strategy = st.builds(
    ddlDsl::LongRaw,
)
ddlDsl::LargeObjectType_strategy = st.builds(
    ddlDsl::LargeObjectType,
    size=
        st.integers()
)
ddlDsl::SqlNumber_strategy = st.builds(
    ddlDsl::SqlNumber,
    scale=
        st.integers(),
    hasPrecision=
        st.booleans(),
    precision=
        st.integers()
)
ddlDsl::SqlCharacter_strategy = st.builds(
    ddlDsl::SqlCharacter,
    size=
        st.integers(),
    national=
        st.booleans()
)
ddlDsl::TableProperty_strategy = st.builds(
    ddlDsl::TableProperty,
    name=
        safe_text
)
Create_strategy = st.builds(
    Create,
)
ddlDsl::CreateIndex_strategy = st.builds(
    ddlDsl::CreateIndex,
    sortOrders=
        safe_text,
    unique=
        st.booleans()
)
Constraint_strategy = st.builds(
    Constraint,
)
ddlDsl::PrimaryKeyConstraint_strategy = st.builds(
    ddlDsl::PrimaryKeyConstraint,
)
ddlDsl::UniqueKeyConstraint_strategy = st.builds(
    ddlDsl::UniqueKeyConstraint,
)
ddlDsl::ForeignKeyConstraint_strategy = st.builds(
    ddlDsl::ForeignKeyConstraint,
)
ddlDsl::NullableConstraint_strategy = st.builds(
    ddlDsl::NullableConstraint,
    not_=
        st.booleans()
)
ddlDsl::ReferenceClause_strategy = st.builds(
    ddlDsl::ReferenceClause,
)
ddlDsl::SqlDataType_strategy = st.builds(
    ddlDsl::SqlDataType,
    name=
        safe_text
)
TableProperty_strategy = st.builds(
    TableProperty,
)
ddlDsl::Column_strategy = st.builds(
    ddlDsl::Column,
    sorted=
        st.booleans(),
    default=
        safe_text
)
ddlDsl::DdlStatement_strategy = st.builds(
    ddlDsl::DdlStatement,
)
ddlDsl::Ddl_strategy = st.builds(
    ddlDsl::Ddl,
)
Comment_strategy = st.builds(
    Comment,
)
ddlDsl::ColumnComment_strategy = st.builds(
    ddlDsl::ColumnComment,
)
ddlDsl::TableComment_strategy = st.builds(
    ddlDsl::TableComment,
)
AlterTableAction_strategy = st.builds(
    AlterTableAction,
)
ddlDsl::AddTableConstraint_strategy = st.builds(
    ddlDsl::AddTableConstraint,
    name=
        safe_text
)
ddlDsl::DropTableConstraint_strategy = st.builds(
    ddlDsl::DropTableConstraint,
)
ddlDsl::Constraint_strategy = st.builds(
    ddlDsl::Constraint,
)
ddlDsl::AlterTableAction_strategy = st.builds(
    ddlDsl::AlterTableAction,
)
ddlDsl::CreateTable_strategy = st.builds(
    ddlDsl::CreateTable,
)
DdlStatement_strategy = st.builds(
    DdlStatement,
)
ddlDsl::Create_strategy = st.builds(
    ddlDsl::Create,
    name=
        safe_text
)
ddlDsl::Drop_strategy = st.builds(
    ddlDsl::Drop,
    object=
        safe_text
)
ddlDsl::Comment_strategy = st.builds(
    ddlDsl::Comment,
    comment=
        safe_text
)
ddlDsl::Alter_strategy = st.builds(
    ddlDsl::Alter,
)

@given(instance=SqlDateTime_strategy)
@settings(max_examples=50)
def test_sqldatetime_instantiation(instance):
    assert isinstance(instance, SqlDateTime)

@given(instance=ddlDsl::SqlInterval_strategy)
@settings(max_examples=50)
def test_ddldsl::sqlinterval_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlInterval)

@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_secondsPrecision_type(instance):
    assert isinstance(instance.secondsPrecision, int)


@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_secondsPrecision_setter(instance):
    original = instance.secondsPrecision
    instance.secondsPrecision = original
    assert instance.secondsPrecision == original

@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_year_type(instance):
    assert isinstance(instance.year, bool)


@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_day_type(instance):
    assert isinstance(instance.day, bool)


@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=ddlDsl::SqlInterval_strategy)
def test_ddldsl::sqlinterval_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ddlDsl::SqlTimeStamp_strategy)
@settings(max_examples=50)
def test_ddldsl::sqltimestamp_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlTimeStamp)

@given(instance=ddlDsl::SqlTimeStamp_strategy)
def test_ddldsl::sqltimestamp_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=ddlDsl::SqlTimeStamp_strategy)
def test_ddldsl::sqltimestamp_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ddlDsl::SqlDate_strategy)
@settings(max_examples=50)
def test_ddldsl::sqldate_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlDate)

@given(instance=LongRaw_strategy)
@settings(max_examples=50)
def test_longraw_instantiation(instance):
    assert isinstance(instance, LongRaw)

@given(instance=ddlDsl::Raw_strategy)
@settings(max_examples=50)
def test_ddldsl::raw_instantiation(instance):
    assert isinstance(instance, ddlDsl::Raw)

@given(instance=ddlDsl::Raw_strategy)
def test_ddldsl::raw_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=ddlDsl::Raw_strategy)
def test_ddldsl::raw_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl::Long_strategy)
@settings(max_examples=50)
def test_ddldsl::long_instantiation(instance):
    assert isinstance(instance, ddlDsl::Long)

@given(instance=ddlDsl::Long_strategy)
def test_ddldsl::long_raw_type(instance):
    assert isinstance(instance.raw, bool)


@given(instance=ddlDsl::Long_strategy)
def test_ddldsl::long_raw_setter(instance):
    original = instance.raw
    instance.raw = original
    assert instance.raw == original

@given(instance=SqlDataType_strategy)
@settings(max_examples=50)
def test_sqldatatype_instantiation(instance):
    assert isinstance(instance, SqlDataType)

@given(instance=ddlDsl::SqlDateTime_strategy)
@settings(max_examples=50)
def test_ddldsl::sqldatetime_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlDateTime)

@given(instance=ddlDsl::RowIdType_strategy)
@settings(max_examples=50)
def test_ddldsl::rowidtype_instantiation(instance):
    assert isinstance(instance, ddlDsl::RowIdType)

@given(instance=ddlDsl::RowIdType_strategy)
def test_ddldsl::rowidtype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=ddlDsl::RowIdType_strategy)
def test_ddldsl::rowidtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl::SqlBoolean_strategy)
@settings(max_examples=50)
def test_ddldsl::sqlboolean_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlBoolean)

@given(instance=ddlDsl::LongRaw_strategy)
@settings(max_examples=50)
def test_ddldsl::longraw_instantiation(instance):
    assert isinstance(instance, ddlDsl::LongRaw)

@given(instance=ddlDsl::LargeObjectType_strategy)
@settings(max_examples=50)
def test_ddldsl::largeobjecttype_instantiation(instance):
    assert isinstance(instance, ddlDsl::LargeObjectType)

@given(instance=ddlDsl::LargeObjectType_strategy)
def test_ddldsl::largeobjecttype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=ddlDsl::LargeObjectType_strategy)
def test_ddldsl::largeobjecttype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl::SqlNumber_strategy)
@settings(max_examples=50)
def test_ddldsl::sqlnumber_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlNumber)

@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_hasPrecision_type(instance):
    assert isinstance(instance.hasPrecision, bool)


@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_hasPrecision_setter(instance):
    original = instance.hasPrecision
    instance.hasPrecision = original
    assert instance.hasPrecision == original

@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=ddlDsl::SqlNumber_strategy)
def test_ddldsl::sqlnumber_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ddlDsl::SqlCharacter_strategy)
@settings(max_examples=50)
def test_ddldsl::sqlcharacter_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlCharacter)

@given(instance=ddlDsl::SqlCharacter_strategy)
def test_ddldsl::sqlcharacter_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=ddlDsl::SqlCharacter_strategy)
def test_ddldsl::sqlcharacter_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ddlDsl::SqlCharacter_strategy)
def test_ddldsl::sqlcharacter_national_type(instance):
    assert isinstance(instance.national, bool)


@given(instance=ddlDsl::SqlCharacter_strategy)
def test_ddldsl::sqlcharacter_national_setter(instance):
    original = instance.national
    instance.national = original
    assert instance.national == original

@given(instance=ddlDsl::TableProperty_strategy)
@settings(max_examples=50)
def test_ddldsl::tableproperty_instantiation(instance):
    assert isinstance(instance, ddlDsl::TableProperty)

@given(instance=ddlDsl::TableProperty_strategy)
def test_ddldsl::tableproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddlDsl::TableProperty_strategy)
def test_ddldsl::tableproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Create_strategy)
@settings(max_examples=50)
def test_create_instantiation(instance):
    assert isinstance(instance, Create)

@given(instance=ddlDsl::CreateIndex_strategy)
@settings(max_examples=50)
def test_ddldsl::createindex_instantiation(instance):
    assert isinstance(instance, ddlDsl::CreateIndex)

@given(instance=ddlDsl::CreateIndex_strategy)
def test_ddldsl::createindex_sortOrders_type(instance):
    assert isinstance(instance.sortOrders, str)


@given(instance=ddlDsl::CreateIndex_strategy)
def test_ddldsl::createindex_sortOrders_setter(instance):
    original = instance.sortOrders
    instance.sortOrders = original
    assert instance.sortOrders == original

@given(instance=ddlDsl::CreateIndex_strategy)
def test_ddldsl::createindex_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=ddlDsl::CreateIndex_strategy)
def test_ddldsl::createindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=ddlDsl::PrimaryKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::primarykeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::PrimaryKeyConstraint)

@given(instance=ddlDsl::UniqueKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::uniquekeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::UniqueKeyConstraint)

@given(instance=ddlDsl::ForeignKeyConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::foreignkeyconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::ForeignKeyConstraint)

@given(instance=ddlDsl::NullableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::nullableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::NullableConstraint)

@given(instance=ddlDsl::NullableConstraint_strategy)
def test_ddldsl::nullableconstraint_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=ddlDsl::NullableConstraint_strategy)
def test_ddldsl::nullableconstraint_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=ddlDsl::ReferenceClause_strategy)
@settings(max_examples=50)
def test_ddldsl::referenceclause_instantiation(instance):
    assert isinstance(instance, ddlDsl::ReferenceClause)

@given(instance=ddlDsl::SqlDataType_strategy)
@settings(max_examples=50)
def test_ddldsl::sqldatatype_instantiation(instance):
    assert isinstance(instance, ddlDsl::SqlDataType)

@given(instance=ddlDsl::SqlDataType_strategy)
def test_ddldsl::sqldatatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddlDsl::SqlDataType_strategy)
def test_ddldsl::sqldatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TableProperty_strategy)
@settings(max_examples=50)
def test_tableproperty_instantiation(instance):
    assert isinstance(instance, TableProperty)

@given(instance=ddlDsl::Column_strategy)
@settings(max_examples=50)
def test_ddldsl::column_instantiation(instance):
    assert isinstance(instance, ddlDsl::Column)

@given(instance=ddlDsl::Column_strategy)
def test_ddldsl::column_sorted_type(instance):
    assert isinstance(instance.sorted, bool)


@given(instance=ddlDsl::Column_strategy)
def test_ddldsl::column_sorted_setter(instance):
    original = instance.sorted
    instance.sorted = original
    assert instance.sorted == original

@given(instance=ddlDsl::Column_strategy)
def test_ddldsl::column_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=ddlDsl::Column_strategy)
def test_ddldsl::column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ddlDsl::DdlStatement_strategy)
@settings(max_examples=50)
def test_ddldsl::ddlstatement_instantiation(instance):
    assert isinstance(instance, ddlDsl::DdlStatement)

@given(instance=ddlDsl::Ddl_strategy)
@settings(max_examples=50)
def test_ddldsl::ddl_instantiation(instance):
    assert isinstance(instance, ddlDsl::Ddl)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ddlDsl::ColumnComment_strategy)
@settings(max_examples=50)
def test_ddldsl::columncomment_instantiation(instance):
    assert isinstance(instance, ddlDsl::ColumnComment)

@given(instance=ddlDsl::TableComment_strategy)
@settings(max_examples=50)
def test_ddldsl::tablecomment_instantiation(instance):
    assert isinstance(instance, ddlDsl::TableComment)

@given(instance=AlterTableAction_strategy)
@settings(max_examples=50)
def test_altertableaction_instantiation(instance):
    assert isinstance(instance, AlterTableAction)

@given(instance=ddlDsl::AddTableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::addtableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::AddTableConstraint)

@given(instance=ddlDsl::AddTableConstraint_strategy)
def test_ddldsl::addtableconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddlDsl::AddTableConstraint_strategy)
def test_ddldsl::addtableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddlDsl::DropTableConstraint_strategy)
@settings(max_examples=50)
def test_ddldsl::droptableconstraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::DropTableConstraint)

@given(instance=ddlDsl::Constraint_strategy)
@settings(max_examples=50)
def test_ddldsl::constraint_instantiation(instance):
    assert isinstance(instance, ddlDsl::Constraint)

@given(instance=ddlDsl::AlterTableAction_strategy)
@settings(max_examples=50)
def test_ddldsl::altertableaction_instantiation(instance):
    assert isinstance(instance, ddlDsl::AlterTableAction)

@given(instance=ddlDsl::CreateTable_strategy)
@settings(max_examples=50)
def test_ddldsl::createtable_instantiation(instance):
    assert isinstance(instance, ddlDsl::CreateTable)

@given(instance=DdlStatement_strategy)
@settings(max_examples=50)
def test_ddlstatement_instantiation(instance):
    assert isinstance(instance, DdlStatement)

@given(instance=ddlDsl::Create_strategy)
@settings(max_examples=50)
def test_ddldsl::create_instantiation(instance):
    assert isinstance(instance, ddlDsl::Create)

@given(instance=ddlDsl::Create_strategy)
def test_ddldsl::create_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddlDsl::Create_strategy)
def test_ddldsl::create_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddlDsl::Drop_strategy)
@settings(max_examples=50)
def test_ddldsl::drop_instantiation(instance):
    assert isinstance(instance, ddlDsl::Drop)

@given(instance=ddlDsl::Drop_strategy)
def test_ddldsl::drop_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=ddlDsl::Drop_strategy)
def test_ddldsl::drop_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=ddlDsl::Comment_strategy)
@settings(max_examples=50)
def test_ddldsl::comment_instantiation(instance):
    assert isinstance(instance, ddlDsl::Comment)

@given(instance=ddlDsl::Comment_strategy)
def test_ddldsl::comment_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ddlDsl::Comment_strategy)
def test_ddldsl::comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ddlDsl::Alter_strategy)
@settings(max_examples=50)
def test_ddldsl::alter_instantiation(instance):
    assert isinstance(instance, ddlDsl::Alter)
