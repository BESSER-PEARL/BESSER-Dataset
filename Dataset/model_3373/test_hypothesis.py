import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    DDL::DataDefinition,
    DDL::Statement,
    Binaries,
    DDL::BFile,
    DDL::BinaryFloat,
    DDL::Blob,
    DDL::BinaryDouble,
    Intervals,
    DDL::DayTime,
    DDL::YearMonth,
    Times,
    DDL::Time,
    DDL::Timestamp,
    DDL::Date,
    Bit,
    DDL::BitVarying,
    Bits,
    DDL::Bit,
    Characters,
    DDL::VarChar,
    DDL::NCharVarying,
    DDL::NChar,
    DDL::NationalChar,
    DDL::NationalCharacterVarying,
    DDL::Text,
    DDL::NClob,
    DDL::NVarChar2,
    DDL::CharVarying,
    DDL::Char,
    DDL::VarChar2,
    DDL::Clob,
    DDL::CharacterVarying,
    DDL::NationalCharacter,
    DDL::NationalCharVarying,
    DDL::Character,
    Aproximado,
    DDL::Long,
    DDL::DoublePrecision,
    DDL::LongRaw,
    DDL::Float,
    DDL::Real,
    Exacto,
    DDL::SmallInteger,
    DDL::Int,
    DDL::SmallInt,
    DDL::Number,
    DDL::Numeric,
    DDL::Decimal,
    DDL::Integer,
    Type,
    DDL::Aproximado,
    DDL::Binaries,
    DDL::Intervals,
    DDL::Times,
    DDL::Bits,
    DDL::Characters,
    DDL::Exacto,
    DataDefinition,
    DDL::CommentTable,
    DDL::CommentColumn,
    DDL::Database,
    DDL::Column,
    DDL::ValuesCk,
    DDL::Ck,
    DDL::Table,
    DDL::Fk,
    DDL::Pk,
    DDL::DDLDefinition,
    DDL::Type,
    DDL::DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ddl::datadefinition_is_not_abstract():
    assert not inspect.isabstract(DDL::DataDefinition)


def test_ddl::datadefinition_constructor_exists():
    assert callable(DDL::DataDefinition.__init__)


def test_ddl::datadefinition_constructor_args():
    sig = inspect.signature(DDL::DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::statement_is_not_abstract():
    assert not inspect.isabstract(DDL::Statement)


def test_ddl::statement_constructor_exists():
    assert callable(DDL::Statement.__init__)


def test_ddl::statement_constructor_args():
    sig = inspect.signature(DDL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_binaries_is_not_abstract():
    assert not inspect.isabstract(Binaries)


def test_binaries_constructor_exists():
    assert callable(Binaries.__init__)


def test_binaries_constructor_args():
    sig = inspect.signature(Binaries.__init__)
    params = list(sig.parameters.keys())



def test_ddl::bfile_is_not_abstract():
    assert not inspect.isabstract(DDL::BFile)


def test_ddl::bfile_constructor_exists():
    assert callable(DDL::BFile.__init__)


def test_ddl::bfile_constructor_args():
    sig = inspect.signature(DDL::BFile.__init__)
    params = list(sig.parameters.keys())



def test_ddl::binaryfloat_is_not_abstract():
    assert not inspect.isabstract(DDL::BinaryFloat)


def test_ddl::binaryfloat_constructor_exists():
    assert callable(DDL::BinaryFloat.__init__)


def test_ddl::binaryfloat_constructor_args():
    sig = inspect.signature(DDL::BinaryFloat.__init__)
    params = list(sig.parameters.keys())



def test_ddl::blob_is_not_abstract():
    assert not inspect.isabstract(DDL::Blob)


def test_ddl::blob_constructor_exists():
    assert callable(DDL::Blob.__init__)


def test_ddl::blob_constructor_args():
    sig = inspect.signature(DDL::Blob.__init__)
    params = list(sig.parameters.keys())



def test_ddl::binarydouble_is_not_abstract():
    assert not inspect.isabstract(DDL::BinaryDouble)


def test_ddl::binarydouble_constructor_exists():
    assert callable(DDL::BinaryDouble.__init__)


def test_ddl::binarydouble_constructor_args():
    sig = inspect.signature(DDL::BinaryDouble.__init__)
    params = list(sig.parameters.keys())



def test_intervals_is_not_abstract():
    assert not inspect.isabstract(Intervals)


def test_intervals_constructor_exists():
    assert callable(Intervals.__init__)


def test_intervals_constructor_args():
    sig = inspect.signature(Intervals.__init__)
    params = list(sig.parameters.keys())



def test_ddl::daytime_is_not_abstract():
    assert not inspect.isabstract(DDL::DayTime)


def test_ddl::daytime_constructor_exists():
    assert callable(DDL::DayTime.__init__)


def test_ddl::daytime_constructor_args():
    sig = inspect.signature(DDL::DayTime.__init__)
    params = list(sig.parameters.keys())



def test_ddl::yearmonth_is_not_abstract():
    assert not inspect.isabstract(DDL::YearMonth)


def test_ddl::yearmonth_constructor_exists():
    assert callable(DDL::YearMonth.__init__)


def test_ddl::yearmonth_constructor_args():
    sig = inspect.signature(DDL::YearMonth.__init__)
    params = list(sig.parameters.keys())



def test_times_is_not_abstract():
    assert not inspect.isabstract(Times)


def test_times_constructor_exists():
    assert callable(Times.__init__)


def test_times_constructor_args():
    sig = inspect.signature(Times.__init__)
    params = list(sig.parameters.keys())



def test_ddl::time_is_not_abstract():
    assert not inspect.isabstract(DDL::Time)


def test_ddl::time_constructor_exists():
    assert callable(DDL::Time.__init__)


def test_ddl::time_constructor_args():
    sig = inspect.signature(DDL::Time.__init__)
    params = list(sig.parameters.keys())



def test_ddl::timestamp_is_not_abstract():
    assert not inspect.isabstract(DDL::Timestamp)


def test_ddl::timestamp_constructor_exists():
    assert callable(DDL::Timestamp.__init__)


def test_ddl::timestamp_constructor_args():
    sig = inspect.signature(DDL::Timestamp.__init__)
    params = list(sig.parameters.keys())



def test_ddl::date_is_not_abstract():
    assert not inspect.isabstract(DDL::Date)


def test_ddl::date_constructor_exists():
    assert callable(DDL::Date.__init__)


def test_ddl::date_constructor_args():
    sig = inspect.signature(DDL::Date.__init__)
    params = list(sig.parameters.keys())



def test_bit_is_not_abstract():
    assert not inspect.isabstract(Bit)


def test_bit_constructor_exists():
    assert callable(Bit.__init__)


def test_bit_constructor_args():
    sig = inspect.signature(Bit.__init__)
    params = list(sig.parameters.keys())



def test_ddl::bitvarying_is_not_abstract():
    assert not inspect.isabstract(DDL::BitVarying)


def test_ddl::bitvarying_constructor_exists():
    assert callable(DDL::BitVarying.__init__)


def test_ddl::bitvarying_constructor_args():
    sig = inspect.signature(DDL::BitVarying.__init__)
    params = list(sig.parameters.keys())



def test_bits_is_not_abstract():
    assert not inspect.isabstract(Bits)


def test_bits_constructor_exists():
    assert callable(Bits.__init__)


def test_bits_constructor_args():
    sig = inspect.signature(Bits.__init__)
    params = list(sig.parameters.keys())



def test_ddl::bit_is_not_abstract():
    assert not inspect.isabstract(DDL::Bit)


def test_ddl::bit_constructor_exists():
    assert callable(DDL::Bit.__init__)


def test_ddl::bit_constructor_args():
    sig = inspect.signature(DDL::Bit.__init__)
    params = list(sig.parameters.keys())



def test_characters_is_not_abstract():
    assert not inspect.isabstract(Characters)


def test_characters_constructor_exists():
    assert callable(Characters.__init__)


def test_characters_constructor_args():
    sig = inspect.signature(Characters.__init__)
    params = list(sig.parameters.keys())



def test_ddl::varchar_is_not_abstract():
    assert not inspect.isabstract(DDL::VarChar)


def test_ddl::varchar_constructor_exists():
    assert callable(DDL::VarChar.__init__)


def test_ddl::varchar_constructor_args():
    sig = inspect.signature(DDL::VarChar.__init__)
    params = list(sig.parameters.keys())



def test_ddl::ncharvarying_is_not_abstract():
    assert not inspect.isabstract(DDL::NCharVarying)


def test_ddl::ncharvarying_constructor_exists():
    assert callable(DDL::NCharVarying.__init__)


def test_ddl::ncharvarying_constructor_args():
    sig = inspect.signature(DDL::NCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nchar_is_not_abstract():
    assert not inspect.isabstract(DDL::NChar)


def test_ddl::nchar_constructor_exists():
    assert callable(DDL::NChar.__init__)


def test_ddl::nchar_constructor_args():
    sig = inspect.signature(DDL::NChar.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nationalchar_is_not_abstract():
    assert not inspect.isabstract(DDL::NationalChar)


def test_ddl::nationalchar_constructor_exists():
    assert callable(DDL::NationalChar.__init__)


def test_ddl::nationalchar_constructor_args():
    sig = inspect.signature(DDL::NationalChar.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nationalcharactervarying_is_not_abstract():
    assert not inspect.isabstract(DDL::NationalCharacterVarying)


def test_ddl::nationalcharactervarying_constructor_exists():
    assert callable(DDL::NationalCharacterVarying.__init__)


def test_ddl::nationalcharactervarying_constructor_args():
    sig = inspect.signature(DDL::NationalCharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl::text_is_not_abstract():
    assert not inspect.isabstract(DDL::Text)


def test_ddl::text_constructor_exists():
    assert callable(DDL::Text.__init__)


def test_ddl::text_constructor_args():
    sig = inspect.signature(DDL::Text.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nclob_is_not_abstract():
    assert not inspect.isabstract(DDL::NClob)


def test_ddl::nclob_constructor_exists():
    assert callable(DDL::NClob.__init__)


def test_ddl::nclob_constructor_args():
    sig = inspect.signature(DDL::NClob.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nvarchar2_is_not_abstract():
    assert not inspect.isabstract(DDL::NVarChar2)


def test_ddl::nvarchar2_constructor_exists():
    assert callable(DDL::NVarChar2.__init__)


def test_ddl::nvarchar2_constructor_args():
    sig = inspect.signature(DDL::NVarChar2.__init__)
    params = list(sig.parameters.keys())



def test_ddl::charvarying_is_not_abstract():
    assert not inspect.isabstract(DDL::CharVarying)


def test_ddl::charvarying_constructor_exists():
    assert callable(DDL::CharVarying.__init__)


def test_ddl::charvarying_constructor_args():
    sig = inspect.signature(DDL::CharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl::char_is_not_abstract():
    assert not inspect.isabstract(DDL::Char)


def test_ddl::char_constructor_exists():
    assert callable(DDL::Char.__init__)


def test_ddl::char_constructor_args():
    sig = inspect.signature(DDL::Char.__init__)
    params = list(sig.parameters.keys())



def test_ddl::varchar2_is_not_abstract():
    assert not inspect.isabstract(DDL::VarChar2)


def test_ddl::varchar2_constructor_exists():
    assert callable(DDL::VarChar2.__init__)


def test_ddl::varchar2_constructor_args():
    sig = inspect.signature(DDL::VarChar2.__init__)
    params = list(sig.parameters.keys())



def test_ddl::clob_is_not_abstract():
    assert not inspect.isabstract(DDL::Clob)


def test_ddl::clob_constructor_exists():
    assert callable(DDL::Clob.__init__)


def test_ddl::clob_constructor_args():
    sig = inspect.signature(DDL::Clob.__init__)
    params = list(sig.parameters.keys())



def test_ddl::charactervarying_is_not_abstract():
    assert not inspect.isabstract(DDL::CharacterVarying)


def test_ddl::charactervarying_constructor_exists():
    assert callable(DDL::CharacterVarying.__init__)


def test_ddl::charactervarying_constructor_args():
    sig = inspect.signature(DDL::CharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nationalcharacter_is_not_abstract():
    assert not inspect.isabstract(DDL::NationalCharacter)


def test_ddl::nationalcharacter_constructor_exists():
    assert callable(DDL::NationalCharacter.__init__)


def test_ddl::nationalcharacter_constructor_args():
    sig = inspect.signature(DDL::NationalCharacter.__init__)
    params = list(sig.parameters.keys())



def test_ddl::nationalcharvarying_is_not_abstract():
    assert not inspect.isabstract(DDL::NationalCharVarying)


def test_ddl::nationalcharvarying_constructor_exists():
    assert callable(DDL::NationalCharVarying.__init__)


def test_ddl::nationalcharvarying_constructor_args():
    sig = inspect.signature(DDL::NationalCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl::character_is_not_abstract():
    assert not inspect.isabstract(DDL::Character)


def test_ddl::character_constructor_exists():
    assert callable(DDL::Character.__init__)


def test_ddl::character_constructor_args():
    sig = inspect.signature(DDL::Character.__init__)
    params = list(sig.parameters.keys())



def test_aproximado_is_not_abstract():
    assert not inspect.isabstract(Aproximado)


def test_aproximado_constructor_exists():
    assert callable(Aproximado.__init__)


def test_aproximado_constructor_args():
    sig = inspect.signature(Aproximado.__init__)
    params = list(sig.parameters.keys())



def test_ddl::long_is_not_abstract():
    assert not inspect.isabstract(DDL::Long)


def test_ddl::long_constructor_exists():
    assert callable(DDL::Long.__init__)


def test_ddl::long_constructor_args():
    sig = inspect.signature(DDL::Long.__init__)
    params = list(sig.parameters.keys())



def test_ddl::doubleprecision_is_not_abstract():
    assert not inspect.isabstract(DDL::DoublePrecision)


def test_ddl::doubleprecision_constructor_exists():
    assert callable(DDL::DoublePrecision.__init__)


def test_ddl::doubleprecision_constructor_args():
    sig = inspect.signature(DDL::DoublePrecision.__init__)
    params = list(sig.parameters.keys())



def test_ddl::longraw_is_not_abstract():
    assert not inspect.isabstract(DDL::LongRaw)


def test_ddl::longraw_constructor_exists():
    assert callable(DDL::LongRaw.__init__)


def test_ddl::longraw_constructor_args():
    sig = inspect.signature(DDL::LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_ddl::float_is_not_abstract():
    assert not inspect.isabstract(DDL::Float)


def test_ddl::float_constructor_exists():
    assert callable(DDL::Float.__init__)


def test_ddl::float_constructor_args():
    sig = inspect.signature(DDL::Float.__init__)
    params = list(sig.parameters.keys())



def test_ddl::real_is_not_abstract():
    assert not inspect.isabstract(DDL::Real)


def test_ddl::real_constructor_exists():
    assert callable(DDL::Real.__init__)


def test_ddl::real_constructor_args():
    sig = inspect.signature(DDL::Real.__init__)
    params = list(sig.parameters.keys())



def test_exacto_is_not_abstract():
    assert not inspect.isabstract(Exacto)


def test_exacto_constructor_exists():
    assert callable(Exacto.__init__)


def test_exacto_constructor_args():
    sig = inspect.signature(Exacto.__init__)
    params = list(sig.parameters.keys())



def test_ddl::smallinteger_is_not_abstract():
    assert not inspect.isabstract(DDL::SmallInteger)


def test_ddl::smallinteger_constructor_exists():
    assert callable(DDL::SmallInteger.__init__)


def test_ddl::smallinteger_constructor_args():
    sig = inspect.signature(DDL::SmallInteger.__init__)
    params = list(sig.parameters.keys())



def test_ddl::int_is_not_abstract():
    assert not inspect.isabstract(DDL::Int)


def test_ddl::int_constructor_exists():
    assert callable(DDL::Int.__init__)


def test_ddl::int_constructor_args():
    sig = inspect.signature(DDL::Int.__init__)
    params = list(sig.parameters.keys())



def test_ddl::smallint_is_not_abstract():
    assert not inspect.isabstract(DDL::SmallInt)


def test_ddl::smallint_constructor_exists():
    assert callable(DDL::SmallInt.__init__)


def test_ddl::smallint_constructor_args():
    sig = inspect.signature(DDL::SmallInt.__init__)
    params = list(sig.parameters.keys())



def test_ddl::number_is_not_abstract():
    assert not inspect.isabstract(DDL::Number)


def test_ddl::number_constructor_exists():
    assert callable(DDL::Number.__init__)


def test_ddl::number_constructor_args():
    sig = inspect.signature(DDL::Number.__init__)
    params = list(sig.parameters.keys())



def test_ddl::numeric_is_not_abstract():
    assert not inspect.isabstract(DDL::Numeric)


def test_ddl::numeric_constructor_exists():
    assert callable(DDL::Numeric.__init__)


def test_ddl::numeric_constructor_args():
    sig = inspect.signature(DDL::Numeric.__init__)
    params = list(sig.parameters.keys())



def test_ddl::decimal_is_not_abstract():
    assert not inspect.isabstract(DDL::Decimal)


def test_ddl::decimal_constructor_exists():
    assert callable(DDL::Decimal.__init__)


def test_ddl::decimal_constructor_args():
    sig = inspect.signature(DDL::Decimal.__init__)
    params = list(sig.parameters.keys())



def test_ddl::integer_is_not_abstract():
    assert not inspect.isabstract(DDL::Integer)


def test_ddl::integer_constructor_exists():
    assert callable(DDL::Integer.__init__)


def test_ddl::integer_constructor_args():
    sig = inspect.signature(DDL::Integer.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ddl::aproximado_is_not_abstract():
    assert not inspect.isabstract(DDL::Aproximado)


def test_ddl::aproximado_constructor_exists():
    assert callable(DDL::Aproximado.__init__)


def test_ddl::aproximado_constructor_args():
    sig = inspect.signature(DDL::Aproximado.__init__)
    params = list(sig.parameters.keys())



def test_ddl::binaries_is_not_abstract():
    assert not inspect.isabstract(DDL::Binaries)


def test_ddl::binaries_constructor_exists():
    assert callable(DDL::Binaries.__init__)


def test_ddl::binaries_constructor_args():
    sig = inspect.signature(DDL::Binaries.__init__)
    params = list(sig.parameters.keys())



def test_ddl::intervals_is_not_abstract():
    assert not inspect.isabstract(DDL::Intervals)


def test_ddl::intervals_constructor_exists():
    assert callable(DDL::Intervals.__init__)


def test_ddl::intervals_constructor_args():
    sig = inspect.signature(DDL::Intervals.__init__)
    params = list(sig.parameters.keys())



def test_ddl::times_is_not_abstract():
    assert not inspect.isabstract(DDL::Times)


def test_ddl::times_constructor_exists():
    assert callable(DDL::Times.__init__)


def test_ddl::times_constructor_args():
    sig = inspect.signature(DDL::Times.__init__)
    params = list(sig.parameters.keys())



def test_ddl::bits_is_not_abstract():
    assert not inspect.isabstract(DDL::Bits)


def test_ddl::bits_constructor_exists():
    assert callable(DDL::Bits.__init__)


def test_ddl::bits_constructor_args():
    sig = inspect.signature(DDL::Bits.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_ddl::bits_has_n():
    assert hasattr(DDL::Bits, "n")
    descriptor = None
    for klass in DDL::Bits.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_ddl::characters_is_not_abstract():
    assert not inspect.isabstract(DDL::Characters)


def test_ddl::characters_constructor_exists():
    assert callable(DDL::Characters.__init__)


def test_ddl::characters_constructor_args():
    sig = inspect.signature(DDL::Characters.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_ddl::characters_has_n():
    assert hasattr(DDL::Characters, "n")
    descriptor = None
    for klass in DDL::Characters.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_ddl::exacto_is_not_abstract():
    assert not inspect.isabstract(DDL::Exacto)


def test_ddl::exacto_constructor_exists():
    assert callable(DDL::Exacto.__init__)


def test_ddl::exacto_constructor_args():
    sig = inspect.signature(DDL::Exacto.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::commenttable_is_not_abstract():
    assert not inspect.isabstract(DDL::CommentTable)


def test_ddl::commenttable_constructor_exists():
    assert callable(DDL::CommentTable.__init__)


def test_ddl::commenttable_constructor_args():
    sig = inspect.signature(DDL::CommentTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "tableComment" in params, "Missing parameter 'tableComment'"

def test_ddl::commenttable_has_tableName():
    assert hasattr(DDL::CommentTable, "tableName")
    descriptor = None
    for klass in DDL::CommentTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::commenttable_has_tableComment():
    assert hasattr(DDL::CommentTable, "tableComment")
    descriptor = None
    for klass in DDL::CommentTable.__mro__:
        if "tableComment" in klass.__dict__:
            descriptor = klass.__dict__["tableComment"]
            break
    assert isinstance(descriptor, property)



def test_ddl::commentcolumn_is_not_abstract():
    assert not inspect.isabstract(DDL::CommentColumn)


def test_ddl::commentcolumn_constructor_exists():
    assert callable(DDL::CommentColumn.__init__)


def test_ddl::commentcolumn_constructor_args():
    sig = inspect.signature(DDL::CommentColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "columnComment" in params, "Missing parameter 'columnComment'"

def test_ddl::commentcolumn_has_columnName():
    assert hasattr(DDL::CommentColumn, "columnName")
    descriptor = None
    for klass in DDL::CommentColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::commentcolumn_has_tableName():
    assert hasattr(DDL::CommentColumn, "tableName")
    descriptor = None
    for klass in DDL::CommentColumn.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::commentcolumn_has_columnComment():
    assert hasattr(DDL::CommentColumn, "columnComment")
    descriptor = None
    for klass in DDL::CommentColumn.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)



def test_ddl::database_is_not_abstract():
    assert not inspect.isabstract(DDL::Database)


def test_ddl::database_constructor_exists():
    assert callable(DDL::Database.__init__)


def test_ddl::database_constructor_args():
    sig = inspect.signature(DDL::Database.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_ddl::database_has_databaseName():
    assert hasattr(DDL::Database, "databaseName")
    descriptor = None
    for klass in DDL::Database.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::column_is_not_abstract():
    assert not inspect.isabstract(DDL::Column)


def test_ddl::column_constructor_exists():
    assert callable(DDL::Column.__init__)


def test_ddl::column_constructor_args():
    sig = inspect.signature(DDL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "commentColumn" in params, "Missing parameter 'commentColumn'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "columnNull" in params, "Missing parameter 'columnNull'"

def test_ddl::column_has_commentColumn():
    assert hasattr(DDL::Column, "commentColumn")
    descriptor = None
    for klass in DDL::Column.__mro__:
        if "commentColumn" in klass.__dict__:
            descriptor = klass.__dict__["commentColumn"]
            break
    assert isinstance(descriptor, property)

def test_ddl::column_has_columnName():
    assert hasattr(DDL::Column, "columnName")
    descriptor = None
    for klass in DDL::Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::column_has_precision():
    assert hasattr(DDL::Column, "precision")
    descriptor = None
    for klass in DDL::Column.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_ddl::column_has_scale():
    assert hasattr(DDL::Column, "scale")
    descriptor = None
    for klass in DDL::Column.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ddl::column_has_columnNull():
    assert hasattr(DDL::Column, "columnNull")
    descriptor = None
    for klass in DDL::Column.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
            break
    assert isinstance(descriptor, property)



def test_ddl::valuesck_is_not_abstract():
    assert not inspect.isabstract(DDL::ValuesCk)


def test_ddl::valuesck_constructor_exists():
    assert callable(DDL::ValuesCk.__init__)


def test_ddl::valuesck_constructor_args():
    sig = inspect.signature(DDL::ValuesCk.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "value" in params, "Missing parameter 'value'"
    assert "logConjuntion" in params, "Missing parameter 'logConjuntion'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl::valuesck_has_comparator():
    assert hasattr(DDL::ValuesCk, "comparator")
    descriptor = None
    for klass in DDL::ValuesCk.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_ddl::valuesck_has_value():
    assert hasattr(DDL::ValuesCk, "value")
    descriptor = None
    for klass in DDL::ValuesCk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ddl::valuesck_has_logConjuntion():
    assert hasattr(DDL::ValuesCk, "logConjuntion")
    descriptor = None
    for klass in DDL::ValuesCk.__mro__:
        if "logConjuntion" in klass.__dict__:
            descriptor = klass.__dict__["logConjuntion"]
            break
    assert isinstance(descriptor, property)

def test_ddl::valuesck_has_columnName():
    assert hasattr(DDL::ValuesCk, "columnName")
    descriptor = None
    for klass in DDL::ValuesCk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::ck_is_not_abstract():
    assert not inspect.isabstract(DDL::Ck)


def test_ddl::ck_constructor_exists():
    assert callable(DDL::Ck.__init__)


def test_ddl::ck_constructor_args():
    sig = inspect.signature(DDL::Ck.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nameCk" in params, "Missing parameter 'nameCk'"

def test_ddl::ck_has_status():
    assert hasattr(DDL::Ck, "status")
    descriptor = None
    for klass in DDL::Ck.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_ddl::ck_has_nameCk():
    assert hasattr(DDL::Ck, "nameCk")
    descriptor = None
    for klass in DDL::Ck.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)



def test_ddl::table_is_not_abstract():
    assert not inspect.isabstract(DDL::Table)


def test_ddl::table_constructor_exists():
    assert callable(DDL::Table.__init__)


def test_ddl::table_constructor_args():
    sig = inspect.signature(DDL::Table.__init__)
    params = list(sig.parameters.keys())
    assert "commentTable" in params, "Missing parameter 'commentTable'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_ddl::table_has_commentTable():
    assert hasattr(DDL::Table, "commentTable")
    descriptor = None
    for klass in DDL::Table.__mro__:
        if "commentTable" in klass.__dict__:
            descriptor = klass.__dict__["commentTable"]
            break
    assert isinstance(descriptor, property)

def test_ddl::table_has_tableName():
    assert hasattr(DDL::Table, "tableName")
    descriptor = None
    for klass in DDL::Table.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::fk_is_not_abstract():
    assert not inspect.isabstract(DDL::Fk)


def test_ddl::fk_constructor_exists():
    assert callable(DDL::Fk.__init__)


def test_ddl::fk_constructor_args():
    sig = inspect.signature(DDL::Fk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "nameFk" in params, "Missing parameter 'nameFk'"
    assert "status" in params, "Missing parameter 'status'"
    assert "columnReference" in params, "Missing parameter 'columnReference'"

def test_ddl::fk_has_columnName():
    assert hasattr(DDL::Fk, "columnName")
    descriptor = None
    for klass in DDL::Fk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::fk_has_nameFk():
    assert hasattr(DDL::Fk, "nameFk")
    descriptor = None
    for klass in DDL::Fk.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)

def test_ddl::fk_has_status():
    assert hasattr(DDL::Fk, "status")
    descriptor = None
    for klass in DDL::Fk.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_ddl::fk_has_columnReference():
    assert hasattr(DDL::Fk, "columnReference")
    descriptor = None
    for klass in DDL::Fk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)



def test_ddl::pk_is_not_abstract():
    assert not inspect.isabstract(DDL::Pk)


def test_ddl::pk_constructor_exists():
    assert callable(DDL::Pk.__init__)


def test_ddl::pk_constructor_args():
    sig = inspect.signature(DDL::Pk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "namePk" in params, "Missing parameter 'namePk'"

def test_ddl::pk_has_columnName():
    assert hasattr(DDL::Pk, "columnName")
    descriptor = None
    for klass in DDL::Pk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::pk_has_namePk():
    assert hasattr(DDL::Pk, "namePk")
    descriptor = None
    for klass in DDL::Pk.__mro__:
        if "namePk" in klass.__dict__:
            descriptor = klass.__dict__["namePk"]
            break
    assert isinstance(descriptor, property)



def test_ddl::ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DDL::DDLDefinition)


def test_ddl::ddldefinition_constructor_exists():
    assert callable(DDL::DDLDefinition.__init__)


def test_ddl::ddldefinition_constructor_args():
    sig = inspect.signature(DDL::DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::type_is_not_abstract():
    assert not inspect.isabstract(DDL::Type)


def test_ddl::type_constructor_exists():
    assert callable(DDL::Type.__init__)


def test_ddl::type_constructor_args():
    sig = inspect.signature(DDL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddl::type_has_name():
    assert hasattr(DDL::Type, "name")
    descriptor = None
    for klass in DDL::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddl::datatype_is_not_abstract():
    assert not inspect.isabstract(DDL::DataType)


def test_ddl::datatype_constructor_exists():
    assert callable(DDL::DataType.__init__)


def test_ddl::datatype_constructor_args():
    sig = inspect.signature(DDL::DataType.__init__)
    params = list(sig.parameters.keys())


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
Statement_strategy = st.builds(
    Statement,
)
DDL::DataDefinition_strategy = st.builds(
    DDL::DataDefinition,
)
DDL::Statement_strategy = st.builds(
    DDL::Statement,
)
Binaries_strategy = st.builds(
    Binaries,
)
DDL::BFile_strategy = st.builds(
    DDL::BFile,
)
DDL::BinaryFloat_strategy = st.builds(
    DDL::BinaryFloat,
)
DDL::Blob_strategy = st.builds(
    DDL::Blob,
)
DDL::BinaryDouble_strategy = st.builds(
    DDL::BinaryDouble,
)
Intervals_strategy = st.builds(
    Intervals,
)
DDL::DayTime_strategy = st.builds(
    DDL::DayTime,
)
DDL::YearMonth_strategy = st.builds(
    DDL::YearMonth,
)
Times_strategy = st.builds(
    Times,
)
DDL::Time_strategy = st.builds(
    DDL::Time,
)
DDL::Timestamp_strategy = st.builds(
    DDL::Timestamp,
)
DDL::Date_strategy = st.builds(
    DDL::Date,
)
Bit_strategy = st.builds(
    Bit,
)
DDL::BitVarying_strategy = st.builds(
    DDL::BitVarying,
)
Bits_strategy = st.builds(
    Bits,
)
DDL::Bit_strategy = st.builds(
    DDL::Bit,
)
Characters_strategy = st.builds(
    Characters,
)
DDL::VarChar_strategy = st.builds(
    DDL::VarChar,
)
DDL::NCharVarying_strategy = st.builds(
    DDL::NCharVarying,
)
DDL::NChar_strategy = st.builds(
    DDL::NChar,
)
DDL::NationalChar_strategy = st.builds(
    DDL::NationalChar,
)
DDL::NationalCharacterVarying_strategy = st.builds(
    DDL::NationalCharacterVarying,
)
DDL::Text_strategy = st.builds(
    DDL::Text,
)
DDL::NClob_strategy = st.builds(
    DDL::NClob,
)
DDL::NVarChar2_strategy = st.builds(
    DDL::NVarChar2,
)
DDL::CharVarying_strategy = st.builds(
    DDL::CharVarying,
)
DDL::Char_strategy = st.builds(
    DDL::Char,
)
DDL::VarChar2_strategy = st.builds(
    DDL::VarChar2,
)
DDL::Clob_strategy = st.builds(
    DDL::Clob,
)
DDL::CharacterVarying_strategy = st.builds(
    DDL::CharacterVarying,
)
DDL::NationalCharacter_strategy = st.builds(
    DDL::NationalCharacter,
)
DDL::NationalCharVarying_strategy = st.builds(
    DDL::NationalCharVarying,
)
DDL::Character_strategy = st.builds(
    DDL::Character,
)
Aproximado_strategy = st.builds(
    Aproximado,
)
DDL::Long_strategy = st.builds(
    DDL::Long,
)
DDL::DoublePrecision_strategy = st.builds(
    DDL::DoublePrecision,
)
DDL::LongRaw_strategy = st.builds(
    DDL::LongRaw,
)
DDL::Float_strategy = st.builds(
    DDL::Float,
)
DDL::Real_strategy = st.builds(
    DDL::Real,
)
Exacto_strategy = st.builds(
    Exacto,
)
DDL::SmallInteger_strategy = st.builds(
    DDL::SmallInteger,
)
DDL::Int_strategy = st.builds(
    DDL::Int,
)
DDL::SmallInt_strategy = st.builds(
    DDL::SmallInt,
)
DDL::Number_strategy = st.builds(
    DDL::Number,
)
DDL::Numeric_strategy = st.builds(
    DDL::Numeric,
)
DDL::Decimal_strategy = st.builds(
    DDL::Decimal,
)
DDL::Integer_strategy = st.builds(
    DDL::Integer,
)
Type_strategy = st.builds(
    Type,
)
DDL::Aproximado_strategy = st.builds(
    DDL::Aproximado,
)
DDL::Binaries_strategy = st.builds(
    DDL::Binaries,
)
DDL::Intervals_strategy = st.builds(
    DDL::Intervals,
)
DDL::Times_strategy = st.builds(
    DDL::Times,
)
DDL::Bits_strategy = st.builds(
    DDL::Bits,
    n=
        safe_text
)
DDL::Characters_strategy = st.builds(
    DDL::Characters,
    n=
        safe_text
)
DDL::Exacto_strategy = st.builds(
    DDL::Exacto,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
DDL::CommentTable_strategy = st.builds(
    DDL::CommentTable,
    tableName=
        safe_text,
    tableComment=
        safe_text
)
DDL::CommentColumn_strategy = st.builds(
    DDL::CommentColumn,
    columnName=
        safe_text,
    tableName=
        safe_text,
    columnComment=
        safe_text
)
DDL::Database_strategy = st.builds(
    DDL::Database,
    databaseName=
        safe_text
)
DDL::Column_strategy = st.builds(
    DDL::Column,
    commentColumn=
        safe_text,
    columnName=
        safe_text,
    precision=
        st.integers(),
    scale=
        st.integers(),
    columnNull=
        st.booleans()
)
DDL::ValuesCk_strategy = st.builds(
    DDL::ValuesCk,
    comparator=
        safe_text,
    value=
        safe_text,
    logConjuntion=
        safe_text,
    columnName=
        safe_text
)
DDL::Ck_strategy = st.builds(
    DDL::Ck,
    status=
        safe_text,
    nameCk=
        safe_text
)
DDL::Table_strategy = st.builds(
    DDL::Table,
    commentTable=
        safe_text,
    tableName=
        safe_text
)
DDL::Fk_strategy = st.builds(
    DDL::Fk,
    columnName=
        safe_text,
    nameFk=
        safe_text,
    status=
        safe_text,
    columnReference=
        safe_text
)
DDL::Pk_strategy = st.builds(
    DDL::Pk,
    columnName=
        safe_text,
    namePk=
        safe_text
)
DDL::DDLDefinition_strategy = st.builds(
    DDL::DDLDefinition,
)
DDL::Type_strategy = st.builds(
    DDL::Type,
    name=
        safe_text
)
DDL::DataType_strategy = st.builds(
    DDL::DataType,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DDL::DataDefinition_strategy)
@settings(max_examples=50)
def test_ddl::datadefinition_instantiation(instance):
    assert isinstance(instance, DDL::DataDefinition)

@given(instance=DDL::Statement_strategy)
@settings(max_examples=50)
def test_ddl::statement_instantiation(instance):
    assert isinstance(instance, DDL::Statement)

@given(instance=Binaries_strategy)
@settings(max_examples=50)
def test_binaries_instantiation(instance):
    assert isinstance(instance, Binaries)

@given(instance=DDL::BFile_strategy)
@settings(max_examples=50)
def test_ddl::bfile_instantiation(instance):
    assert isinstance(instance, DDL::BFile)

@given(instance=DDL::BinaryFloat_strategy)
@settings(max_examples=50)
def test_ddl::binaryfloat_instantiation(instance):
    assert isinstance(instance, DDL::BinaryFloat)

@given(instance=DDL::Blob_strategy)
@settings(max_examples=50)
def test_ddl::blob_instantiation(instance):
    assert isinstance(instance, DDL::Blob)

@given(instance=DDL::BinaryDouble_strategy)
@settings(max_examples=50)
def test_ddl::binarydouble_instantiation(instance):
    assert isinstance(instance, DDL::BinaryDouble)

@given(instance=Intervals_strategy)
@settings(max_examples=50)
def test_intervals_instantiation(instance):
    assert isinstance(instance, Intervals)

@given(instance=DDL::DayTime_strategy)
@settings(max_examples=50)
def test_ddl::daytime_instantiation(instance):
    assert isinstance(instance, DDL::DayTime)

@given(instance=DDL::YearMonth_strategy)
@settings(max_examples=50)
def test_ddl::yearmonth_instantiation(instance):
    assert isinstance(instance, DDL::YearMonth)

@given(instance=Times_strategy)
@settings(max_examples=50)
def test_times_instantiation(instance):
    assert isinstance(instance, Times)

@given(instance=DDL::Time_strategy)
@settings(max_examples=50)
def test_ddl::time_instantiation(instance):
    assert isinstance(instance, DDL::Time)

@given(instance=DDL::Timestamp_strategy)
@settings(max_examples=50)
def test_ddl::timestamp_instantiation(instance):
    assert isinstance(instance, DDL::Timestamp)

@given(instance=DDL::Date_strategy)
@settings(max_examples=50)
def test_ddl::date_instantiation(instance):
    assert isinstance(instance, DDL::Date)

@given(instance=Bit_strategy)
@settings(max_examples=50)
def test_bit_instantiation(instance):
    assert isinstance(instance, Bit)

@given(instance=DDL::BitVarying_strategy)
@settings(max_examples=50)
def test_ddl::bitvarying_instantiation(instance):
    assert isinstance(instance, DDL::BitVarying)

@given(instance=Bits_strategy)
@settings(max_examples=50)
def test_bits_instantiation(instance):
    assert isinstance(instance, Bits)

@given(instance=DDL::Bit_strategy)
@settings(max_examples=50)
def test_ddl::bit_instantiation(instance):
    assert isinstance(instance, DDL::Bit)

@given(instance=Characters_strategy)
@settings(max_examples=50)
def test_characters_instantiation(instance):
    assert isinstance(instance, Characters)

@given(instance=DDL::VarChar_strategy)
@settings(max_examples=50)
def test_ddl::varchar_instantiation(instance):
    assert isinstance(instance, DDL::VarChar)

@given(instance=DDL::NCharVarying_strategy)
@settings(max_examples=50)
def test_ddl::ncharvarying_instantiation(instance):
    assert isinstance(instance, DDL::NCharVarying)

@given(instance=DDL::NChar_strategy)
@settings(max_examples=50)
def test_ddl::nchar_instantiation(instance):
    assert isinstance(instance, DDL::NChar)

@given(instance=DDL::NationalChar_strategy)
@settings(max_examples=50)
def test_ddl::nationalchar_instantiation(instance):
    assert isinstance(instance, DDL::NationalChar)

@given(instance=DDL::NationalCharacterVarying_strategy)
@settings(max_examples=50)
def test_ddl::nationalcharactervarying_instantiation(instance):
    assert isinstance(instance, DDL::NationalCharacterVarying)

@given(instance=DDL::Text_strategy)
@settings(max_examples=50)
def test_ddl::text_instantiation(instance):
    assert isinstance(instance, DDL::Text)

@given(instance=DDL::NClob_strategy)
@settings(max_examples=50)
def test_ddl::nclob_instantiation(instance):
    assert isinstance(instance, DDL::NClob)

@given(instance=DDL::NVarChar2_strategy)
@settings(max_examples=50)
def test_ddl::nvarchar2_instantiation(instance):
    assert isinstance(instance, DDL::NVarChar2)

@given(instance=DDL::CharVarying_strategy)
@settings(max_examples=50)
def test_ddl::charvarying_instantiation(instance):
    assert isinstance(instance, DDL::CharVarying)

@given(instance=DDL::Char_strategy)
@settings(max_examples=50)
def test_ddl::char_instantiation(instance):
    assert isinstance(instance, DDL::Char)

@given(instance=DDL::VarChar2_strategy)
@settings(max_examples=50)
def test_ddl::varchar2_instantiation(instance):
    assert isinstance(instance, DDL::VarChar2)

@given(instance=DDL::Clob_strategy)
@settings(max_examples=50)
def test_ddl::clob_instantiation(instance):
    assert isinstance(instance, DDL::Clob)

@given(instance=DDL::CharacterVarying_strategy)
@settings(max_examples=50)
def test_ddl::charactervarying_instantiation(instance):
    assert isinstance(instance, DDL::CharacterVarying)

@given(instance=DDL::NationalCharacter_strategy)
@settings(max_examples=50)
def test_ddl::nationalcharacter_instantiation(instance):
    assert isinstance(instance, DDL::NationalCharacter)

@given(instance=DDL::NationalCharVarying_strategy)
@settings(max_examples=50)
def test_ddl::nationalcharvarying_instantiation(instance):
    assert isinstance(instance, DDL::NationalCharVarying)

@given(instance=DDL::Character_strategy)
@settings(max_examples=50)
def test_ddl::character_instantiation(instance):
    assert isinstance(instance, DDL::Character)

@given(instance=Aproximado_strategy)
@settings(max_examples=50)
def test_aproximado_instantiation(instance):
    assert isinstance(instance, Aproximado)

@given(instance=DDL::Long_strategy)
@settings(max_examples=50)
def test_ddl::long_instantiation(instance):
    assert isinstance(instance, DDL::Long)

@given(instance=DDL::DoublePrecision_strategy)
@settings(max_examples=50)
def test_ddl::doubleprecision_instantiation(instance):
    assert isinstance(instance, DDL::DoublePrecision)

@given(instance=DDL::LongRaw_strategy)
@settings(max_examples=50)
def test_ddl::longraw_instantiation(instance):
    assert isinstance(instance, DDL::LongRaw)

@given(instance=DDL::Float_strategy)
@settings(max_examples=50)
def test_ddl::float_instantiation(instance):
    assert isinstance(instance, DDL::Float)

@given(instance=DDL::Real_strategy)
@settings(max_examples=50)
def test_ddl::real_instantiation(instance):
    assert isinstance(instance, DDL::Real)

@given(instance=Exacto_strategy)
@settings(max_examples=50)
def test_exacto_instantiation(instance):
    assert isinstance(instance, Exacto)

@given(instance=DDL::SmallInteger_strategy)
@settings(max_examples=50)
def test_ddl::smallinteger_instantiation(instance):
    assert isinstance(instance, DDL::SmallInteger)

@given(instance=DDL::Int_strategy)
@settings(max_examples=50)
def test_ddl::int_instantiation(instance):
    assert isinstance(instance, DDL::Int)

@given(instance=DDL::SmallInt_strategy)
@settings(max_examples=50)
def test_ddl::smallint_instantiation(instance):
    assert isinstance(instance, DDL::SmallInt)

@given(instance=DDL::Number_strategy)
@settings(max_examples=50)
def test_ddl::number_instantiation(instance):
    assert isinstance(instance, DDL::Number)

@given(instance=DDL::Numeric_strategy)
@settings(max_examples=50)
def test_ddl::numeric_instantiation(instance):
    assert isinstance(instance, DDL::Numeric)

@given(instance=DDL::Decimal_strategy)
@settings(max_examples=50)
def test_ddl::decimal_instantiation(instance):
    assert isinstance(instance, DDL::Decimal)

@given(instance=DDL::Integer_strategy)
@settings(max_examples=50)
def test_ddl::integer_instantiation(instance):
    assert isinstance(instance, DDL::Integer)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DDL::Aproximado_strategy)
@settings(max_examples=50)
def test_ddl::aproximado_instantiation(instance):
    assert isinstance(instance, DDL::Aproximado)

@given(instance=DDL::Binaries_strategy)
@settings(max_examples=50)
def test_ddl::binaries_instantiation(instance):
    assert isinstance(instance, DDL::Binaries)

@given(instance=DDL::Intervals_strategy)
@settings(max_examples=50)
def test_ddl::intervals_instantiation(instance):
    assert isinstance(instance, DDL::Intervals)

@given(instance=DDL::Times_strategy)
@settings(max_examples=50)
def test_ddl::times_instantiation(instance):
    assert isinstance(instance, DDL::Times)

@given(instance=DDL::Bits_strategy)
@settings(max_examples=50)
def test_ddl::bits_instantiation(instance):
    assert isinstance(instance, DDL::Bits)

@given(instance=DDL::Bits_strategy)
def test_ddl::bits_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=DDL::Bits_strategy)
def test_ddl::bits_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DDL::Characters_strategy)
@settings(max_examples=50)
def test_ddl::characters_instantiation(instance):
    assert isinstance(instance, DDL::Characters)

@given(instance=DDL::Characters_strategy)
def test_ddl::characters_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=DDL::Characters_strategy)
def test_ddl::characters_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DDL::Exacto_strategy)
@settings(max_examples=50)
def test_ddl::exacto_instantiation(instance):
    assert isinstance(instance, DDL::Exacto)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=DDL::CommentTable_strategy)
@settings(max_examples=50)
def test_ddl::commenttable_instantiation(instance):
    assert isinstance(instance, DDL::CommentTable)

@given(instance=DDL::CommentTable_strategy)
def test_ddl::commenttable_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::CommentTable_strategy)
def test_ddl::commenttable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::CommentTable_strategy)
def test_ddl::commenttable_tableComment_type(instance):
    assert isinstance(instance.tableComment, str)


@given(instance=DDL::CommentTable_strategy)
def test_ddl::commenttable_tableComment_setter(instance):
    original = instance.tableComment
    instance.tableComment = original
    assert instance.tableComment == original

@given(instance=DDL::CommentColumn_strategy)
@settings(max_examples=50)
def test_ddl::commentcolumn_instantiation(instance):
    assert isinstance(instance, DDL::CommentColumn)

@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_columnComment_type(instance):
    assert isinstance(instance.columnComment, str)


@given(instance=DDL::CommentColumn_strategy)
def test_ddl::commentcolumn_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original

@given(instance=DDL::Database_strategy)
@settings(max_examples=50)
def test_ddl::database_instantiation(instance):
    assert isinstance(instance, DDL::Database)

@given(instance=DDL::Database_strategy)
def test_ddl::database_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=DDL::Database_strategy)
def test_ddl::database_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=DDL::Column_strategy)
@settings(max_examples=50)
def test_ddl::column_instantiation(instance):
    assert isinstance(instance, DDL::Column)

@given(instance=DDL::Column_strategy)
def test_ddl::column_commentColumn_type(instance):
    assert isinstance(instance.commentColumn, str)


@given(instance=DDL::Column_strategy)
def test_ddl::column_commentColumn_setter(instance):
    original = instance.commentColumn
    instance.commentColumn = original
    assert instance.commentColumn == original

@given(instance=DDL::Column_strategy)
def test_ddl::column_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::Column_strategy)
def test_ddl::column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::Column_strategy)
def test_ddl::column_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=DDL::Column_strategy)
def test_ddl::column_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=DDL::Column_strategy)
def test_ddl::column_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=DDL::Column_strategy)
def test_ddl::column_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=DDL::Column_strategy)
def test_ddl::column_columnNull_type(instance):
    assert isinstance(instance.columnNull, bool)


@given(instance=DDL::Column_strategy)
def test_ddl::column_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original

@given(instance=DDL::ValuesCk_strategy)
@settings(max_examples=50)
def test_ddl::valuesck_instantiation(instance):
    assert isinstance(instance, DDL::ValuesCk)

@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_logConjuntion_type(instance):
    assert isinstance(instance.logConjuntion, str)


@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_logConjuntion_setter(instance):
    original = instance.logConjuntion
    instance.logConjuntion = original
    assert instance.logConjuntion == original

@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::ValuesCk_strategy)
def test_ddl::valuesck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::Ck_strategy)
@settings(max_examples=50)
def test_ddl::ck_instantiation(instance):
    assert isinstance(instance, DDL::Ck)

@given(instance=DDL::Ck_strategy)
def test_ddl::ck_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=DDL::Ck_strategy)
def test_ddl::ck_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=DDL::Ck_strategy)
def test_ddl::ck_nameCk_type(instance):
    assert isinstance(instance.nameCk, str)


@given(instance=DDL::Ck_strategy)
def test_ddl::ck_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original

@given(instance=DDL::Table_strategy)
@settings(max_examples=50)
def test_ddl::table_instantiation(instance):
    assert isinstance(instance, DDL::Table)

@given(instance=DDL::Table_strategy)
def test_ddl::table_commentTable_type(instance):
    assert isinstance(instance.commentTable, str)


@given(instance=DDL::Table_strategy)
def test_ddl::table_commentTable_setter(instance):
    original = instance.commentTable
    instance.commentTable = original
    assert instance.commentTable == original

@given(instance=DDL::Table_strategy)
def test_ddl::table_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::Table_strategy)
def test_ddl::table_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::Fk_strategy)
@settings(max_examples=50)
def test_ddl::fk_instantiation(instance):
    assert isinstance(instance, DDL::Fk)

@given(instance=DDL::Fk_strategy)
def test_ddl::fk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::Fk_strategy)
def test_ddl::fk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::Fk_strategy)
def test_ddl::fk_nameFk_type(instance):
    assert isinstance(instance.nameFk, str)


@given(instance=DDL::Fk_strategy)
def test_ddl::fk_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original

@given(instance=DDL::Fk_strategy)
def test_ddl::fk_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=DDL::Fk_strategy)
def test_ddl::fk_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=DDL::Fk_strategy)
def test_ddl::fk_columnReference_type(instance):
    assert isinstance(instance.columnReference, str)


@given(instance=DDL::Fk_strategy)
def test_ddl::fk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original

@given(instance=DDL::Pk_strategy)
@settings(max_examples=50)
def test_ddl::pk_instantiation(instance):
    assert isinstance(instance, DDL::Pk)

@given(instance=DDL::Pk_strategy)
def test_ddl::pk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::Pk_strategy)
def test_ddl::pk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::Pk_strategy)
def test_ddl::pk_namePk_type(instance):
    assert isinstance(instance.namePk, str)


@given(instance=DDL::Pk_strategy)
def test_ddl::pk_namePk_setter(instance):
    original = instance.namePk
    instance.namePk = original
    assert instance.namePk == original

@given(instance=DDL::DDLDefinition_strategy)
@settings(max_examples=50)
def test_ddl::ddldefinition_instantiation(instance):
    assert isinstance(instance, DDL::DDLDefinition)

@given(instance=DDL::Type_strategy)
@settings(max_examples=50)
def test_ddl::type_instantiation(instance):
    assert isinstance(instance, DDL::Type)

@given(instance=DDL::Type_strategy)
def test_ddl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DDL::Type_strategy)
def test_ddl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DDL::DataType_strategy)
@settings(max_examples=50)
def test_ddl::datatype_instantiation(instance):
    assert isinstance(instance, DDL::DataType)
