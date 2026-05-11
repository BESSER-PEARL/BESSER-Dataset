import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Bits,
    DML::DDL::Bit,
    Characters,
    DML::DDL::Clob,
    DML::DDL::NationalCharVarying,
    DML::DDL::CharacterVarying,
    DML::DDL::NationalCharacter,
    DML::DDL::NClob,
    DML::DDL::NChar,
    DML::DDL::VarChar,
    DML::DDL::NVarChar2,
    DML::DDL::NCharVarying,
    DML::DDL::Char,
    DML::DDL::NationalChar,
    DML::DDL::CharVarying,
    DML::DDL::NationalCharacterVarying,
    DML::DDL::VarChar2,
    DML::DDL::Character,
    Binaries,
    DML::DDL::BFile,
    DML::DDL::Blob,
    DML::DDL::BinaryFloat,
    DML::DDL::BinaryDouble,
    Intervals,
    DML::DDL::DayTime,
    DML::DDL::YearMonth,
    Times,
    DML::DDL::Timestamp,
    DML::DDL::Time,
    DML::DDL::Date,
    Bit,
    DML::DDL::BitVarying,
    DML::DDL::Registry,
    DataDefinition,
    DML::DDL::Database,
    Aproximado,
    DML::DDL::LongRaw,
    DML::DDL::Float,
    DML::DDL::DoublePrecision,
    DML::DDL::Long,
    DML::DDL::Real,
    Exacto,
    DML::DDL::Decimal,
    DML::DDL::SmallInt,
    DML::DDL::Int,
    DML::DDL::Number,
    DML::DDL::Numeric,
    DML::DDL::SmallInteger,
    DML::DDL::Integer,
    Type,
    DML::DDL::Aproximado,
    DML::DDL::Characters,
    DML::DDL::Bits,
    DML::DDL::Times,
    DML::DDL::Binaries,
    DML::DDL::Intervals,
    DML::DDL::Exacto,
    DML::DDL::CommentColumn,
    DML::DDL::CommentTable,
    DML::DDL::Value,
    DML::DDL::DDLDefinition,
    DML::DDL::Type,
    DML::DDL::DataType,
    Statement,
    DML::DDL::DataDefinition,
    DML::DDL::Statement,
    DML::DDL::Column,
    DML::DDL::ValuesCk,
    DML::DDL::Ck,
    DML::DDL::Table,
    DML::DDL::Fk,
    DML::DDL::Pk,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bits_is_not_abstract():
    assert not inspect.isabstract(Bits)


def test_bits_constructor_exists():
    assert callable(Bits.__init__)


def test_bits_constructor_args():
    sig = inspect.signature(Bits.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::bit_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Bit)


def test_dml::ddl::bit_constructor_exists():
    assert callable(DML::DDL::Bit.__init__)


def test_dml::ddl::bit_constructor_args():
    sig = inspect.signature(DML::DDL::Bit.__init__)
    params = list(sig.parameters.keys())



def test_characters_is_not_abstract():
    assert not inspect.isabstract(Characters)


def test_characters_constructor_exists():
    assert callable(Characters.__init__)


def test_characters_constructor_args():
    sig = inspect.signature(Characters.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::clob_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Clob)


def test_dml::ddl::clob_constructor_exists():
    assert callable(DML::DDL::Clob.__init__)


def test_dml::ddl::clob_constructor_args():
    sig = inspect.signature(DML::DDL::Clob.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nationalcharvarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NationalCharVarying)


def test_dml::ddl::nationalcharvarying_constructor_exists():
    assert callable(DML::DDL::NationalCharVarying.__init__)


def test_dml::ddl::nationalcharvarying_constructor_args():
    sig = inspect.signature(DML::DDL::NationalCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::charactervarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::CharacterVarying)


def test_dml::ddl::charactervarying_constructor_exists():
    assert callable(DML::DDL::CharacterVarying.__init__)


def test_dml::ddl::charactervarying_constructor_args():
    sig = inspect.signature(DML::DDL::CharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nationalcharacter_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NationalCharacter)


def test_dml::ddl::nationalcharacter_constructor_exists():
    assert callable(DML::DDL::NationalCharacter.__init__)


def test_dml::ddl::nationalcharacter_constructor_args():
    sig = inspect.signature(DML::DDL::NationalCharacter.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nclob_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NClob)


def test_dml::ddl::nclob_constructor_exists():
    assert callable(DML::DDL::NClob.__init__)


def test_dml::ddl::nclob_constructor_args():
    sig = inspect.signature(DML::DDL::NClob.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nchar_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NChar)


def test_dml::ddl::nchar_constructor_exists():
    assert callable(DML::DDL::NChar.__init__)


def test_dml::ddl::nchar_constructor_args():
    sig = inspect.signature(DML::DDL::NChar.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::varchar_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::VarChar)


def test_dml::ddl::varchar_constructor_exists():
    assert callable(DML::DDL::VarChar.__init__)


def test_dml::ddl::varchar_constructor_args():
    sig = inspect.signature(DML::DDL::VarChar.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nvarchar2_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NVarChar2)


def test_dml::ddl::nvarchar2_constructor_exists():
    assert callable(DML::DDL::NVarChar2.__init__)


def test_dml::ddl::nvarchar2_constructor_args():
    sig = inspect.signature(DML::DDL::NVarChar2.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::ncharvarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NCharVarying)


def test_dml::ddl::ncharvarying_constructor_exists():
    assert callable(DML::DDL::NCharVarying.__init__)


def test_dml::ddl::ncharvarying_constructor_args():
    sig = inspect.signature(DML::DDL::NCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::char_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Char)


def test_dml::ddl::char_constructor_exists():
    assert callable(DML::DDL::Char.__init__)


def test_dml::ddl::char_constructor_args():
    sig = inspect.signature(DML::DDL::Char.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nationalchar_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NationalChar)


def test_dml::ddl::nationalchar_constructor_exists():
    assert callable(DML::DDL::NationalChar.__init__)


def test_dml::ddl::nationalchar_constructor_args():
    sig = inspect.signature(DML::DDL::NationalChar.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::charvarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::CharVarying)


def test_dml::ddl::charvarying_constructor_exists():
    assert callable(DML::DDL::CharVarying.__init__)


def test_dml::ddl::charvarying_constructor_args():
    sig = inspect.signature(DML::DDL::CharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::nationalcharactervarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::NationalCharacterVarying)


def test_dml::ddl::nationalcharactervarying_constructor_exists():
    assert callable(DML::DDL::NationalCharacterVarying.__init__)


def test_dml::ddl::nationalcharactervarying_constructor_args():
    sig = inspect.signature(DML::DDL::NationalCharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::varchar2_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::VarChar2)


def test_dml::ddl::varchar2_constructor_exists():
    assert callable(DML::DDL::VarChar2.__init__)


def test_dml::ddl::varchar2_constructor_args():
    sig = inspect.signature(DML::DDL::VarChar2.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::character_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Character)


def test_dml::ddl::character_constructor_exists():
    assert callable(DML::DDL::Character.__init__)


def test_dml::ddl::character_constructor_args():
    sig = inspect.signature(DML::DDL::Character.__init__)
    params = list(sig.parameters.keys())



def test_binaries_is_not_abstract():
    assert not inspect.isabstract(Binaries)


def test_binaries_constructor_exists():
    assert callable(Binaries.__init__)


def test_binaries_constructor_args():
    sig = inspect.signature(Binaries.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::bfile_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::BFile)


def test_dml::ddl::bfile_constructor_exists():
    assert callable(DML::DDL::BFile.__init__)


def test_dml::ddl::bfile_constructor_args():
    sig = inspect.signature(DML::DDL::BFile.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::blob_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Blob)


def test_dml::ddl::blob_constructor_exists():
    assert callable(DML::DDL::Blob.__init__)


def test_dml::ddl::blob_constructor_args():
    sig = inspect.signature(DML::DDL::Blob.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::binaryfloat_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::BinaryFloat)


def test_dml::ddl::binaryfloat_constructor_exists():
    assert callable(DML::DDL::BinaryFloat.__init__)


def test_dml::ddl::binaryfloat_constructor_args():
    sig = inspect.signature(DML::DDL::BinaryFloat.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::binarydouble_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::BinaryDouble)


def test_dml::ddl::binarydouble_constructor_exists():
    assert callable(DML::DDL::BinaryDouble.__init__)


def test_dml::ddl::binarydouble_constructor_args():
    sig = inspect.signature(DML::DDL::BinaryDouble.__init__)
    params = list(sig.parameters.keys())



def test_intervals_is_not_abstract():
    assert not inspect.isabstract(Intervals)


def test_intervals_constructor_exists():
    assert callable(Intervals.__init__)


def test_intervals_constructor_args():
    sig = inspect.signature(Intervals.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::daytime_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::DayTime)


def test_dml::ddl::daytime_constructor_exists():
    assert callable(DML::DDL::DayTime.__init__)


def test_dml::ddl::daytime_constructor_args():
    sig = inspect.signature(DML::DDL::DayTime.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::yearmonth_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::YearMonth)


def test_dml::ddl::yearmonth_constructor_exists():
    assert callable(DML::DDL::YearMonth.__init__)


def test_dml::ddl::yearmonth_constructor_args():
    sig = inspect.signature(DML::DDL::YearMonth.__init__)
    params = list(sig.parameters.keys())



def test_times_is_not_abstract():
    assert not inspect.isabstract(Times)


def test_times_constructor_exists():
    assert callable(Times.__init__)


def test_times_constructor_args():
    sig = inspect.signature(Times.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::timestamp_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Timestamp)


def test_dml::ddl::timestamp_constructor_exists():
    assert callable(DML::DDL::Timestamp.__init__)


def test_dml::ddl::timestamp_constructor_args():
    sig = inspect.signature(DML::DDL::Timestamp.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::time_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Time)


def test_dml::ddl::time_constructor_exists():
    assert callable(DML::DDL::Time.__init__)


def test_dml::ddl::time_constructor_args():
    sig = inspect.signature(DML::DDL::Time.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::date_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Date)


def test_dml::ddl::date_constructor_exists():
    assert callable(DML::DDL::Date.__init__)


def test_dml::ddl::date_constructor_args():
    sig = inspect.signature(DML::DDL::Date.__init__)
    params = list(sig.parameters.keys())



def test_bit_is_not_abstract():
    assert not inspect.isabstract(Bit)


def test_bit_constructor_exists():
    assert callable(Bit.__init__)


def test_bit_constructor_args():
    sig = inspect.signature(Bit.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::bitvarying_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::BitVarying)


def test_dml::ddl::bitvarying_constructor_exists():
    assert callable(DML::DDL::BitVarying.__init__)


def test_dml::ddl::bitvarying_constructor_args():
    sig = inspect.signature(DML::DDL::BitVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::registry_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Registry)


def test_dml::ddl::registry_constructor_exists():
    assert callable(DML::DDL::Registry.__init__)


def test_dml::ddl::registry_constructor_args():
    sig = inspect.signature(DML::DDL::Registry.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::database_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Database)


def test_dml::ddl::database_constructor_exists():
    assert callable(DML::DDL::Database.__init__)


def test_dml::ddl::database_constructor_args():
    sig = inspect.signature(DML::DDL::Database.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_dml::ddl::database_has_databaseName():
    assert hasattr(DML::DDL::Database, "databaseName")
    descriptor = None
    for klass in DML::DDL::Database.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_aproximado_is_not_abstract():
    assert not inspect.isabstract(Aproximado)


def test_aproximado_constructor_exists():
    assert callable(Aproximado.__init__)


def test_aproximado_constructor_args():
    sig = inspect.signature(Aproximado.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::longraw_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::LongRaw)


def test_dml::ddl::longraw_constructor_exists():
    assert callable(DML::DDL::LongRaw.__init__)


def test_dml::ddl::longraw_constructor_args():
    sig = inspect.signature(DML::DDL::LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::float_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Float)


def test_dml::ddl::float_constructor_exists():
    assert callable(DML::DDL::Float.__init__)


def test_dml::ddl::float_constructor_args():
    sig = inspect.signature(DML::DDL::Float.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::doubleprecision_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::DoublePrecision)


def test_dml::ddl::doubleprecision_constructor_exists():
    assert callable(DML::DDL::DoublePrecision.__init__)


def test_dml::ddl::doubleprecision_constructor_args():
    sig = inspect.signature(DML::DDL::DoublePrecision.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::long_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Long)


def test_dml::ddl::long_constructor_exists():
    assert callable(DML::DDL::Long.__init__)


def test_dml::ddl::long_constructor_args():
    sig = inspect.signature(DML::DDL::Long.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::real_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Real)


def test_dml::ddl::real_constructor_exists():
    assert callable(DML::DDL::Real.__init__)


def test_dml::ddl::real_constructor_args():
    sig = inspect.signature(DML::DDL::Real.__init__)
    params = list(sig.parameters.keys())



def test_exacto_is_not_abstract():
    assert not inspect.isabstract(Exacto)


def test_exacto_constructor_exists():
    assert callable(Exacto.__init__)


def test_exacto_constructor_args():
    sig = inspect.signature(Exacto.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::decimal_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Decimal)


def test_dml::ddl::decimal_constructor_exists():
    assert callable(DML::DDL::Decimal.__init__)


def test_dml::ddl::decimal_constructor_args():
    sig = inspect.signature(DML::DDL::Decimal.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::smallint_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::SmallInt)


def test_dml::ddl::smallint_constructor_exists():
    assert callable(DML::DDL::SmallInt.__init__)


def test_dml::ddl::smallint_constructor_args():
    sig = inspect.signature(DML::DDL::SmallInt.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::int_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Int)


def test_dml::ddl::int_constructor_exists():
    assert callable(DML::DDL::Int.__init__)


def test_dml::ddl::int_constructor_args():
    sig = inspect.signature(DML::DDL::Int.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::number_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Number)


def test_dml::ddl::number_constructor_exists():
    assert callable(DML::DDL::Number.__init__)


def test_dml::ddl::number_constructor_args():
    sig = inspect.signature(DML::DDL::Number.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::numeric_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Numeric)


def test_dml::ddl::numeric_constructor_exists():
    assert callable(DML::DDL::Numeric.__init__)


def test_dml::ddl::numeric_constructor_args():
    sig = inspect.signature(DML::DDL::Numeric.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::smallinteger_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::SmallInteger)


def test_dml::ddl::smallinteger_constructor_exists():
    assert callable(DML::DDL::SmallInteger.__init__)


def test_dml::ddl::smallinteger_constructor_args():
    sig = inspect.signature(DML::DDL::SmallInteger.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::integer_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Integer)


def test_dml::ddl::integer_constructor_exists():
    assert callable(DML::DDL::Integer.__init__)


def test_dml::ddl::integer_constructor_args():
    sig = inspect.signature(DML::DDL::Integer.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::aproximado_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Aproximado)


def test_dml::ddl::aproximado_constructor_exists():
    assert callable(DML::DDL::Aproximado.__init__)


def test_dml::ddl::aproximado_constructor_args():
    sig = inspect.signature(DML::DDL::Aproximado.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::characters_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Characters)


def test_dml::ddl::characters_constructor_exists():
    assert callable(DML::DDL::Characters.__init__)


def test_dml::ddl::characters_constructor_args():
    sig = inspect.signature(DML::DDL::Characters.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_dml::ddl::characters_has_n():
    assert hasattr(DML::DDL::Characters, "n")
    descriptor = None
    for klass in DML::DDL::Characters.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::bits_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Bits)


def test_dml::ddl::bits_constructor_exists():
    assert callable(DML::DDL::Bits.__init__)


def test_dml::ddl::bits_constructor_args():
    sig = inspect.signature(DML::DDL::Bits.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_dml::ddl::bits_has_n():
    assert hasattr(DML::DDL::Bits, "n")
    descriptor = None
    for klass in DML::DDL::Bits.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::times_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Times)


def test_dml::ddl::times_constructor_exists():
    assert callable(DML::DDL::Times.__init__)


def test_dml::ddl::times_constructor_args():
    sig = inspect.signature(DML::DDL::Times.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::binaries_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Binaries)


def test_dml::ddl::binaries_constructor_exists():
    assert callable(DML::DDL::Binaries.__init__)


def test_dml::ddl::binaries_constructor_args():
    sig = inspect.signature(DML::DDL::Binaries.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::intervals_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Intervals)


def test_dml::ddl::intervals_constructor_exists():
    assert callable(DML::DDL::Intervals.__init__)


def test_dml::ddl::intervals_constructor_args():
    sig = inspect.signature(DML::DDL::Intervals.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::exacto_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Exacto)


def test_dml::ddl::exacto_constructor_exists():
    assert callable(DML::DDL::Exacto.__init__)


def test_dml::ddl::exacto_constructor_args():
    sig = inspect.signature(DML::DDL::Exacto.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::commentcolumn_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::CommentColumn)


def test_dml::ddl::commentcolumn_constructor_exists():
    assert callable(DML::DDL::CommentColumn.__init__)


def test_dml::ddl::commentcolumn_constructor_args():
    sig = inspect.signature(DML::DDL::CommentColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnComment" in params, "Missing parameter 'columnComment'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dml::ddl::commentcolumn_has_columnComment():
    assert hasattr(DML::DDL::CommentColumn, "columnComment")
    descriptor = None
    for klass in DML::DDL::CommentColumn.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::commentcolumn_has_columnName():
    assert hasattr(DML::DDL::CommentColumn, "columnName")
    descriptor = None
    for klass in DML::DDL::CommentColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::commentcolumn_has_tableName():
    assert hasattr(DML::DDL::CommentColumn, "tableName")
    descriptor = None
    for klass in DML::DDL::CommentColumn.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::commenttable_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::CommentTable)


def test_dml::ddl::commenttable_constructor_exists():
    assert callable(DML::DDL::CommentTable.__init__)


def test_dml::ddl::commenttable_constructor_args():
    sig = inspect.signature(DML::DDL::CommentTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableComment" in params, "Missing parameter 'tableComment'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dml::ddl::commenttable_has_tableComment():
    assert hasattr(DML::DDL::CommentTable, "tableComment")
    descriptor = None
    for klass in DML::DDL::CommentTable.__mro__:
        if "tableComment" in klass.__dict__:
            descriptor = klass.__dict__["tableComment"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::commenttable_has_tableName():
    assert hasattr(DML::DDL::CommentTable, "tableName")
    descriptor = None
    for klass in DML::DDL::CommentTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::value_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Value)


def test_dml::ddl::value_constructor_exists():
    assert callable(DML::DDL::Value.__init__)


def test_dml::ddl::value_constructor_args():
    sig = inspect.signature(DML::DDL::Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dml::ddl::value_has_value():
    assert hasattr(DML::DDL::Value, "value")
    descriptor = None
    for klass in DML::DDL::Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::DDLDefinition)


def test_dml::ddl::ddldefinition_constructor_exists():
    assert callable(DML::DDL::DDLDefinition.__init__)


def test_dml::ddl::ddldefinition_constructor_args():
    sig = inspect.signature(DML::DDL::DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::type_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Type)


def test_dml::ddl::type_constructor_exists():
    assert callable(DML::DDL::Type.__init__)


def test_dml::ddl::type_constructor_args():
    sig = inspect.signature(DML::DDL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dml::ddl::type_has_name():
    assert hasattr(DML::DDL::Type, "name")
    descriptor = None
    for klass in DML::DDL::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::datatype_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::DataType)


def test_dml::ddl::datatype_constructor_exists():
    assert callable(DML::DDL::DataType.__init__)


def test_dml::ddl::datatype_constructor_args():
    sig = inspect.signature(DML::DDL::DataType.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::datadefinition_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::DataDefinition)


def test_dml::ddl::datadefinition_constructor_exists():
    assert callable(DML::DDL::DataDefinition.__init__)


def test_dml::ddl::datadefinition_constructor_args():
    sig = inspect.signature(DML::DDL::DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::statement_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Statement)


def test_dml::ddl::statement_constructor_exists():
    assert callable(DML::DDL::Statement.__init__)


def test_dml::ddl::statement_constructor_args():
    sig = inspect.signature(DML::DDL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dml::ddl::column_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Column)


def test_dml::ddl::column_constructor_exists():
    assert callable(DML::DDL::Column.__init__)


def test_dml::ddl::column_constructor_args():
    sig = inspect.signature(DML::DDL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "commentColumn" in params, "Missing parameter 'commentColumn'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "columnNull" in params, "Missing parameter 'columnNull'"

def test_dml::ddl::column_has_commentColumn():
    assert hasattr(DML::DDL::Column, "commentColumn")
    descriptor = None
    for klass in DML::DDL::Column.__mro__:
        if "commentColumn" in klass.__dict__:
            descriptor = klass.__dict__["commentColumn"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::column_has_columnName():
    assert hasattr(DML::DDL::Column, "columnName")
    descriptor = None
    for klass in DML::DDL::Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::column_has_columnNull():
    assert hasattr(DML::DDL::Column, "columnNull")
    descriptor = None
    for klass in DML::DDL::Column.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::valuesck_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::ValuesCk)


def test_dml::ddl::valuesck_constructor_exists():
    assert callable(DML::DDL::ValuesCk.__init__)


def test_dml::ddl::valuesck_constructor_args():
    sig = inspect.signature(DML::DDL::ValuesCk.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "logConjuntion" in params, "Missing parameter 'logConjuntion'"
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dml::ddl::valuesck_has_value():
    assert hasattr(DML::DDL::ValuesCk, "value")
    descriptor = None
    for klass in DML::DDL::ValuesCk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::valuesck_has_logConjuntion():
    assert hasattr(DML::DDL::ValuesCk, "logConjuntion")
    descriptor = None
    for klass in DML::DDL::ValuesCk.__mro__:
        if "logConjuntion" in klass.__dict__:
            descriptor = klass.__dict__["logConjuntion"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::valuesck_has_comparator():
    assert hasattr(DML::DDL::ValuesCk, "comparator")
    descriptor = None
    for klass in DML::DDL::ValuesCk.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::valuesck_has_columnName():
    assert hasattr(DML::DDL::ValuesCk, "columnName")
    descriptor = None
    for klass in DML::DDL::ValuesCk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::ck_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Ck)


def test_dml::ddl::ck_constructor_exists():
    assert callable(DML::DDL::Ck.__init__)


def test_dml::ddl::ck_constructor_args():
    sig = inspect.signature(DML::DDL::Ck.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nameCk" in params, "Missing parameter 'nameCk'"

def test_dml::ddl::ck_has_status():
    assert hasattr(DML::DDL::Ck, "status")
    descriptor = None
    for klass in DML::DDL::Ck.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::ck_has_nameCk():
    assert hasattr(DML::DDL::Ck, "nameCk")
    descriptor = None
    for klass in DML::DDL::Ck.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::table_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Table)


def test_dml::ddl::table_constructor_exists():
    assert callable(DML::DDL::Table.__init__)


def test_dml::ddl::table_constructor_args():
    sig = inspect.signature(DML::DDL::Table.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "commentTable" in params, "Missing parameter 'commentTable'"

def test_dml::ddl::table_has_tableName():
    assert hasattr(DML::DDL::Table, "tableName")
    descriptor = None
    for klass in DML::DDL::Table.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::table_has_commentTable():
    assert hasattr(DML::DDL::Table, "commentTable")
    descriptor = None
    for klass in DML::DDL::Table.__mro__:
        if "commentTable" in klass.__dict__:
            descriptor = klass.__dict__["commentTable"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::fk_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Fk)


def test_dml::ddl::fk_constructor_exists():
    assert callable(DML::DDL::Fk.__init__)


def test_dml::ddl::fk_constructor_args():
    sig = inspect.signature(DML::DDL::Fk.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nameFk" in params, "Missing parameter 'nameFk'"
    assert "columnReference" in params, "Missing parameter 'columnReference'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "type" in params, "Missing parameter 'type'"

def test_dml::ddl::fk_has_status():
    assert hasattr(DML::DDL::Fk, "status")
    descriptor = None
    for klass in DML::DDL::Fk.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::fk_has_nameFk():
    assert hasattr(DML::DDL::Fk, "nameFk")
    descriptor = None
    for klass in DML::DDL::Fk.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::fk_has_columnReference():
    assert hasattr(DML::DDL::Fk, "columnReference")
    descriptor = None
    for klass in DML::DDL::Fk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::fk_has_columnName():
    assert hasattr(DML::DDL::Fk, "columnName")
    descriptor = None
    for klass in DML::DDL::Fk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::fk_has_type():
    assert hasattr(DML::DDL::Fk, "type")
    descriptor = None
    for klass in DML::DDL::Fk.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dml::ddl::pk_is_not_abstract():
    assert not inspect.isabstract(DML::DDL::Pk)


def test_dml::ddl::pk_constructor_exists():
    assert callable(DML::DDL::Pk.__init__)


def test_dml::ddl::pk_constructor_args():
    sig = inspect.signature(DML::DDL::Pk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "namePk" in params, "Missing parameter 'namePk'"

def test_dml::ddl::pk_has_columnName():
    assert hasattr(DML::DDL::Pk, "columnName")
    descriptor = None
    for klass in DML::DDL::Pk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml::ddl::pk_has_namePk():
    assert hasattr(DML::DDL::Pk, "namePk")
    descriptor = None
    for klass in DML::DDL::Pk.__mro__:
        if "namePk" in klass.__dict__:
            descriptor = klass.__dict__["namePk"]
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
Bits_strategy = st.builds(
    Bits,
)
DML::DDL::Bit_strategy = st.builds(
    DML::DDL::Bit,
)
Characters_strategy = st.builds(
    Characters,
)
DML::DDL::Clob_strategy = st.builds(
    DML::DDL::Clob,
)
DML::DDL::NationalCharVarying_strategy = st.builds(
    DML::DDL::NationalCharVarying,
)
DML::DDL::CharacterVarying_strategy = st.builds(
    DML::DDL::CharacterVarying,
)
DML::DDL::NationalCharacter_strategy = st.builds(
    DML::DDL::NationalCharacter,
)
DML::DDL::NClob_strategy = st.builds(
    DML::DDL::NClob,
)
DML::DDL::NChar_strategy = st.builds(
    DML::DDL::NChar,
)
DML::DDL::VarChar_strategy = st.builds(
    DML::DDL::VarChar,
)
DML::DDL::NVarChar2_strategy = st.builds(
    DML::DDL::NVarChar2,
)
DML::DDL::NCharVarying_strategy = st.builds(
    DML::DDL::NCharVarying,
)
DML::DDL::Char_strategy = st.builds(
    DML::DDL::Char,
)
DML::DDL::NationalChar_strategy = st.builds(
    DML::DDL::NationalChar,
)
DML::DDL::CharVarying_strategy = st.builds(
    DML::DDL::CharVarying,
)
DML::DDL::NationalCharacterVarying_strategy = st.builds(
    DML::DDL::NationalCharacterVarying,
)
DML::DDL::VarChar2_strategy = st.builds(
    DML::DDL::VarChar2,
)
DML::DDL::Character_strategy = st.builds(
    DML::DDL::Character,
)
Binaries_strategy = st.builds(
    Binaries,
)
DML::DDL::BFile_strategy = st.builds(
    DML::DDL::BFile,
)
DML::DDL::Blob_strategy = st.builds(
    DML::DDL::Blob,
)
DML::DDL::BinaryFloat_strategy = st.builds(
    DML::DDL::BinaryFloat,
)
DML::DDL::BinaryDouble_strategy = st.builds(
    DML::DDL::BinaryDouble,
)
Intervals_strategy = st.builds(
    Intervals,
)
DML::DDL::DayTime_strategy = st.builds(
    DML::DDL::DayTime,
)
DML::DDL::YearMonth_strategy = st.builds(
    DML::DDL::YearMonth,
)
Times_strategy = st.builds(
    Times,
)
DML::DDL::Timestamp_strategy = st.builds(
    DML::DDL::Timestamp,
)
DML::DDL::Time_strategy = st.builds(
    DML::DDL::Time,
)
DML::DDL::Date_strategy = st.builds(
    DML::DDL::Date,
)
Bit_strategy = st.builds(
    Bit,
)
DML::DDL::BitVarying_strategy = st.builds(
    DML::DDL::BitVarying,
)
DML::DDL::Registry_strategy = st.builds(
    DML::DDL::Registry,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
DML::DDL::Database_strategy = st.builds(
    DML::DDL::Database,
    databaseName=
        safe_text
)
Aproximado_strategy = st.builds(
    Aproximado,
)
DML::DDL::LongRaw_strategy = st.builds(
    DML::DDL::LongRaw,
)
DML::DDL::Float_strategy = st.builds(
    DML::DDL::Float,
)
DML::DDL::DoublePrecision_strategy = st.builds(
    DML::DDL::DoublePrecision,
)
DML::DDL::Long_strategy = st.builds(
    DML::DDL::Long,
)
DML::DDL::Real_strategy = st.builds(
    DML::DDL::Real,
)
Exacto_strategy = st.builds(
    Exacto,
)
DML::DDL::Decimal_strategy = st.builds(
    DML::DDL::Decimal,
)
DML::DDL::SmallInt_strategy = st.builds(
    DML::DDL::SmallInt,
)
DML::DDL::Int_strategy = st.builds(
    DML::DDL::Int,
)
DML::DDL::Number_strategy = st.builds(
    DML::DDL::Number,
)
DML::DDL::Numeric_strategy = st.builds(
    DML::DDL::Numeric,
)
DML::DDL::SmallInteger_strategy = st.builds(
    DML::DDL::SmallInteger,
)
DML::DDL::Integer_strategy = st.builds(
    DML::DDL::Integer,
)
Type_strategy = st.builds(
    Type,
)
DML::DDL::Aproximado_strategy = st.builds(
    DML::DDL::Aproximado,
)
DML::DDL::Characters_strategy = st.builds(
    DML::DDL::Characters,
    n=
        safe_text
)
DML::DDL::Bits_strategy = st.builds(
    DML::DDL::Bits,
    n=
        safe_text
)
DML::DDL::Times_strategy = st.builds(
    DML::DDL::Times,
)
DML::DDL::Binaries_strategy = st.builds(
    DML::DDL::Binaries,
)
DML::DDL::Intervals_strategy = st.builds(
    DML::DDL::Intervals,
)
DML::DDL::Exacto_strategy = st.builds(
    DML::DDL::Exacto,
)
DML::DDL::CommentColumn_strategy = st.builds(
    DML::DDL::CommentColumn,
    columnComment=
        safe_text,
    columnName=
        safe_text,
    tableName=
        safe_text
)
DML::DDL::CommentTable_strategy = st.builds(
    DML::DDL::CommentTable,
    tableComment=
        safe_text,
    tableName=
        safe_text
)
DML::DDL::Value_strategy = st.builds(
    DML::DDL::Value,
    value=
        safe_text
)
DML::DDL::DDLDefinition_strategy = st.builds(
    DML::DDL::DDLDefinition,
)
DML::DDL::Type_strategy = st.builds(
    DML::DDL::Type,
    name=
        safe_text
)
DML::DDL::DataType_strategy = st.builds(
    DML::DDL::DataType,
)
Statement_strategy = st.builds(
    Statement,
)
DML::DDL::DataDefinition_strategy = st.builds(
    DML::DDL::DataDefinition,
)
DML::DDL::Statement_strategy = st.builds(
    DML::DDL::Statement,
)
DML::DDL::Column_strategy = st.builds(
    DML::DDL::Column,
    commentColumn=
        safe_text,
    columnName=
        safe_text,
    columnNull=
        st.booleans()
)
DML::DDL::ValuesCk_strategy = st.builds(
    DML::DDL::ValuesCk,
    value=
        safe_text,
    logConjuntion=
        safe_text,
    comparator=
        safe_text,
    columnName=
        safe_text
)
DML::DDL::Ck_strategy = st.builds(
    DML::DDL::Ck,
    status=
        safe_text,
    nameCk=
        safe_text
)
DML::DDL::Table_strategy = st.builds(
    DML::DDL::Table,
    tableName=
        safe_text,
    commentTable=
        safe_text
)
DML::DDL::Fk_strategy = st.builds(
    DML::DDL::Fk,
    status=
        safe_text,
    nameFk=
        safe_text,
    columnReference=
        safe_text,
    columnName=
        safe_text,
    type=
        safe_text
)
DML::DDL::Pk_strategy = st.builds(
    DML::DDL::Pk,
    columnName=
        safe_text,
    namePk=
        safe_text
)

@given(instance=Bits_strategy)
@settings(max_examples=50)
def test_bits_instantiation(instance):
    assert isinstance(instance, Bits)

@given(instance=DML::DDL::Bit_strategy)
@settings(max_examples=50)
def test_dml::ddl::bit_instantiation(instance):
    assert isinstance(instance, DML::DDL::Bit)

@given(instance=Characters_strategy)
@settings(max_examples=50)
def test_characters_instantiation(instance):
    assert isinstance(instance, Characters)

@given(instance=DML::DDL::Clob_strategy)
@settings(max_examples=50)
def test_dml::ddl::clob_instantiation(instance):
    assert isinstance(instance, DML::DDL::Clob)

@given(instance=DML::DDL::NationalCharVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::nationalcharvarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::NationalCharVarying)

@given(instance=DML::DDL::CharacterVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::charactervarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::CharacterVarying)

@given(instance=DML::DDL::NationalCharacter_strategy)
@settings(max_examples=50)
def test_dml::ddl::nationalcharacter_instantiation(instance):
    assert isinstance(instance, DML::DDL::NationalCharacter)

@given(instance=DML::DDL::NClob_strategy)
@settings(max_examples=50)
def test_dml::ddl::nclob_instantiation(instance):
    assert isinstance(instance, DML::DDL::NClob)

@given(instance=DML::DDL::NChar_strategy)
@settings(max_examples=50)
def test_dml::ddl::nchar_instantiation(instance):
    assert isinstance(instance, DML::DDL::NChar)

@given(instance=DML::DDL::VarChar_strategy)
@settings(max_examples=50)
def test_dml::ddl::varchar_instantiation(instance):
    assert isinstance(instance, DML::DDL::VarChar)

@given(instance=DML::DDL::NVarChar2_strategy)
@settings(max_examples=50)
def test_dml::ddl::nvarchar2_instantiation(instance):
    assert isinstance(instance, DML::DDL::NVarChar2)

@given(instance=DML::DDL::NCharVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::ncharvarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::NCharVarying)

@given(instance=DML::DDL::Char_strategy)
@settings(max_examples=50)
def test_dml::ddl::char_instantiation(instance):
    assert isinstance(instance, DML::DDL::Char)

@given(instance=DML::DDL::NationalChar_strategy)
@settings(max_examples=50)
def test_dml::ddl::nationalchar_instantiation(instance):
    assert isinstance(instance, DML::DDL::NationalChar)

@given(instance=DML::DDL::CharVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::charvarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::CharVarying)

@given(instance=DML::DDL::NationalCharacterVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::nationalcharactervarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::NationalCharacterVarying)

@given(instance=DML::DDL::VarChar2_strategy)
@settings(max_examples=50)
def test_dml::ddl::varchar2_instantiation(instance):
    assert isinstance(instance, DML::DDL::VarChar2)

@given(instance=DML::DDL::Character_strategy)
@settings(max_examples=50)
def test_dml::ddl::character_instantiation(instance):
    assert isinstance(instance, DML::DDL::Character)

@given(instance=Binaries_strategy)
@settings(max_examples=50)
def test_binaries_instantiation(instance):
    assert isinstance(instance, Binaries)

@given(instance=DML::DDL::BFile_strategy)
@settings(max_examples=50)
def test_dml::ddl::bfile_instantiation(instance):
    assert isinstance(instance, DML::DDL::BFile)

@given(instance=DML::DDL::Blob_strategy)
@settings(max_examples=50)
def test_dml::ddl::blob_instantiation(instance):
    assert isinstance(instance, DML::DDL::Blob)

@given(instance=DML::DDL::BinaryFloat_strategy)
@settings(max_examples=50)
def test_dml::ddl::binaryfloat_instantiation(instance):
    assert isinstance(instance, DML::DDL::BinaryFloat)

@given(instance=DML::DDL::BinaryDouble_strategy)
@settings(max_examples=50)
def test_dml::ddl::binarydouble_instantiation(instance):
    assert isinstance(instance, DML::DDL::BinaryDouble)

@given(instance=Intervals_strategy)
@settings(max_examples=50)
def test_intervals_instantiation(instance):
    assert isinstance(instance, Intervals)

@given(instance=DML::DDL::DayTime_strategy)
@settings(max_examples=50)
def test_dml::ddl::daytime_instantiation(instance):
    assert isinstance(instance, DML::DDL::DayTime)

@given(instance=DML::DDL::YearMonth_strategy)
@settings(max_examples=50)
def test_dml::ddl::yearmonth_instantiation(instance):
    assert isinstance(instance, DML::DDL::YearMonth)

@given(instance=Times_strategy)
@settings(max_examples=50)
def test_times_instantiation(instance):
    assert isinstance(instance, Times)

@given(instance=DML::DDL::Timestamp_strategy)
@settings(max_examples=50)
def test_dml::ddl::timestamp_instantiation(instance):
    assert isinstance(instance, DML::DDL::Timestamp)

@given(instance=DML::DDL::Time_strategy)
@settings(max_examples=50)
def test_dml::ddl::time_instantiation(instance):
    assert isinstance(instance, DML::DDL::Time)

@given(instance=DML::DDL::Date_strategy)
@settings(max_examples=50)
def test_dml::ddl::date_instantiation(instance):
    assert isinstance(instance, DML::DDL::Date)

@given(instance=Bit_strategy)
@settings(max_examples=50)
def test_bit_instantiation(instance):
    assert isinstance(instance, Bit)

@given(instance=DML::DDL::BitVarying_strategy)
@settings(max_examples=50)
def test_dml::ddl::bitvarying_instantiation(instance):
    assert isinstance(instance, DML::DDL::BitVarying)

@given(instance=DML::DDL::Registry_strategy)
@settings(max_examples=50)
def test_dml::ddl::registry_instantiation(instance):
    assert isinstance(instance, DML::DDL::Registry)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=DML::DDL::Database_strategy)
@settings(max_examples=50)
def test_dml::ddl::database_instantiation(instance):
    assert isinstance(instance, DML::DDL::Database)

@given(instance=DML::DDL::Database_strategy)
def test_dml::ddl::database_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=DML::DDL::Database_strategy)
def test_dml::ddl::database_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=Aproximado_strategy)
@settings(max_examples=50)
def test_aproximado_instantiation(instance):
    assert isinstance(instance, Aproximado)

@given(instance=DML::DDL::LongRaw_strategy)
@settings(max_examples=50)
def test_dml::ddl::longraw_instantiation(instance):
    assert isinstance(instance, DML::DDL::LongRaw)

@given(instance=DML::DDL::Float_strategy)
@settings(max_examples=50)
def test_dml::ddl::float_instantiation(instance):
    assert isinstance(instance, DML::DDL::Float)

@given(instance=DML::DDL::DoublePrecision_strategy)
@settings(max_examples=50)
def test_dml::ddl::doubleprecision_instantiation(instance):
    assert isinstance(instance, DML::DDL::DoublePrecision)

@given(instance=DML::DDL::Long_strategy)
@settings(max_examples=50)
def test_dml::ddl::long_instantiation(instance):
    assert isinstance(instance, DML::DDL::Long)

@given(instance=DML::DDL::Real_strategy)
@settings(max_examples=50)
def test_dml::ddl::real_instantiation(instance):
    assert isinstance(instance, DML::DDL::Real)

@given(instance=Exacto_strategy)
@settings(max_examples=50)
def test_exacto_instantiation(instance):
    assert isinstance(instance, Exacto)

@given(instance=DML::DDL::Decimal_strategy)
@settings(max_examples=50)
def test_dml::ddl::decimal_instantiation(instance):
    assert isinstance(instance, DML::DDL::Decimal)

@given(instance=DML::DDL::SmallInt_strategy)
@settings(max_examples=50)
def test_dml::ddl::smallint_instantiation(instance):
    assert isinstance(instance, DML::DDL::SmallInt)

@given(instance=DML::DDL::Int_strategy)
@settings(max_examples=50)
def test_dml::ddl::int_instantiation(instance):
    assert isinstance(instance, DML::DDL::Int)

@given(instance=DML::DDL::Number_strategy)
@settings(max_examples=50)
def test_dml::ddl::number_instantiation(instance):
    assert isinstance(instance, DML::DDL::Number)

@given(instance=DML::DDL::Numeric_strategy)
@settings(max_examples=50)
def test_dml::ddl::numeric_instantiation(instance):
    assert isinstance(instance, DML::DDL::Numeric)

@given(instance=DML::DDL::SmallInteger_strategy)
@settings(max_examples=50)
def test_dml::ddl::smallinteger_instantiation(instance):
    assert isinstance(instance, DML::DDL::SmallInteger)

@given(instance=DML::DDL::Integer_strategy)
@settings(max_examples=50)
def test_dml::ddl::integer_instantiation(instance):
    assert isinstance(instance, DML::DDL::Integer)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DML::DDL::Aproximado_strategy)
@settings(max_examples=50)
def test_dml::ddl::aproximado_instantiation(instance):
    assert isinstance(instance, DML::DDL::Aproximado)

@given(instance=DML::DDL::Characters_strategy)
@settings(max_examples=50)
def test_dml::ddl::characters_instantiation(instance):
    assert isinstance(instance, DML::DDL::Characters)

@given(instance=DML::DDL::Characters_strategy)
def test_dml::ddl::characters_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=DML::DDL::Characters_strategy)
def test_dml::ddl::characters_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DML::DDL::Bits_strategy)
@settings(max_examples=50)
def test_dml::ddl::bits_instantiation(instance):
    assert isinstance(instance, DML::DDL::Bits)

@given(instance=DML::DDL::Bits_strategy)
def test_dml::ddl::bits_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=DML::DDL::Bits_strategy)
def test_dml::ddl::bits_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DML::DDL::Times_strategy)
@settings(max_examples=50)
def test_dml::ddl::times_instantiation(instance):
    assert isinstance(instance, DML::DDL::Times)

@given(instance=DML::DDL::Binaries_strategy)
@settings(max_examples=50)
def test_dml::ddl::binaries_instantiation(instance):
    assert isinstance(instance, DML::DDL::Binaries)

@given(instance=DML::DDL::Intervals_strategy)
@settings(max_examples=50)
def test_dml::ddl::intervals_instantiation(instance):
    assert isinstance(instance, DML::DDL::Intervals)

@given(instance=DML::DDL::Exacto_strategy)
@settings(max_examples=50)
def test_dml::ddl::exacto_instantiation(instance):
    assert isinstance(instance, DML::DDL::Exacto)

@given(instance=DML::DDL::CommentColumn_strategy)
@settings(max_examples=50)
def test_dml::ddl::commentcolumn_instantiation(instance):
    assert isinstance(instance, DML::DDL::CommentColumn)

@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_columnComment_type(instance):
    assert isinstance(instance.columnComment, str)


@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original

@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DML::DDL::CommentColumn_strategy)
def test_dml::ddl::commentcolumn_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DML::DDL::CommentTable_strategy)
@settings(max_examples=50)
def test_dml::ddl::commenttable_instantiation(instance):
    assert isinstance(instance, DML::DDL::CommentTable)

@given(instance=DML::DDL::CommentTable_strategy)
def test_dml::ddl::commenttable_tableComment_type(instance):
    assert isinstance(instance.tableComment, str)


@given(instance=DML::DDL::CommentTable_strategy)
def test_dml::ddl::commenttable_tableComment_setter(instance):
    original = instance.tableComment
    instance.tableComment = original
    assert instance.tableComment == original

@given(instance=DML::DDL::CommentTable_strategy)
def test_dml::ddl::commenttable_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DML::DDL::CommentTable_strategy)
def test_dml::ddl::commenttable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DML::DDL::Value_strategy)
@settings(max_examples=50)
def test_dml::ddl::value_instantiation(instance):
    assert isinstance(instance, DML::DDL::Value)

@given(instance=DML::DDL::Value_strategy)
def test_dml::ddl::value_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DML::DDL::Value_strategy)
def test_dml::ddl::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML::DDL::DDLDefinition_strategy)
@settings(max_examples=50)
def test_dml::ddl::ddldefinition_instantiation(instance):
    assert isinstance(instance, DML::DDL::DDLDefinition)

@given(instance=DML::DDL::Type_strategy)
@settings(max_examples=50)
def test_dml::ddl::type_instantiation(instance):
    assert isinstance(instance, DML::DDL::Type)

@given(instance=DML::DDL::Type_strategy)
def test_dml::ddl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DML::DDL::Type_strategy)
def test_dml::ddl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DML::DDL::DataType_strategy)
@settings(max_examples=50)
def test_dml::ddl::datatype_instantiation(instance):
    assert isinstance(instance, DML::DDL::DataType)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DML::DDL::DataDefinition_strategy)
@settings(max_examples=50)
def test_dml::ddl::datadefinition_instantiation(instance):
    assert isinstance(instance, DML::DDL::DataDefinition)

@given(instance=DML::DDL::Statement_strategy)
@settings(max_examples=50)
def test_dml::ddl::statement_instantiation(instance):
    assert isinstance(instance, DML::DDL::Statement)

@given(instance=DML::DDL::Column_strategy)
@settings(max_examples=50)
def test_dml::ddl::column_instantiation(instance):
    assert isinstance(instance, DML::DDL::Column)

@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_commentColumn_type(instance):
    assert isinstance(instance.commentColumn, str)


@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_commentColumn_setter(instance):
    original = instance.commentColumn
    instance.commentColumn = original
    assert instance.commentColumn == original

@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_columnNull_type(instance):
    assert isinstance(instance.columnNull, bool)


@given(instance=DML::DDL::Column_strategy)
def test_dml::ddl::column_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original

@given(instance=DML::DDL::ValuesCk_strategy)
@settings(max_examples=50)
def test_dml::ddl::valuesck_instantiation(instance):
    assert isinstance(instance, DML::DDL::ValuesCk)

@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_logConjuntion_type(instance):
    assert isinstance(instance.logConjuntion, str)


@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_logConjuntion_setter(instance):
    original = instance.logConjuntion
    instance.logConjuntion = original
    assert instance.logConjuntion == original

@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::DDL::ValuesCk_strategy)
def test_dml::ddl::valuesck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::DDL::Ck_strategy)
@settings(max_examples=50)
def test_dml::ddl::ck_instantiation(instance):
    assert isinstance(instance, DML::DDL::Ck)

@given(instance=DML::DDL::Ck_strategy)
def test_dml::ddl::ck_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=DML::DDL::Ck_strategy)
def test_dml::ddl::ck_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=DML::DDL::Ck_strategy)
def test_dml::ddl::ck_nameCk_type(instance):
    assert isinstance(instance.nameCk, str)


@given(instance=DML::DDL::Ck_strategy)
def test_dml::ddl::ck_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original

@given(instance=DML::DDL::Table_strategy)
@settings(max_examples=50)
def test_dml::ddl::table_instantiation(instance):
    assert isinstance(instance, DML::DDL::Table)

@given(instance=DML::DDL::Table_strategy)
def test_dml::ddl::table_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DML::DDL::Table_strategy)
def test_dml::ddl::table_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DML::DDL::Table_strategy)
def test_dml::ddl::table_commentTable_type(instance):
    assert isinstance(instance.commentTable, str)


@given(instance=DML::DDL::Table_strategy)
def test_dml::ddl::table_commentTable_setter(instance):
    original = instance.commentTable
    instance.commentTable = original
    assert instance.commentTable == original

@given(instance=DML::DDL::Fk_strategy)
@settings(max_examples=50)
def test_dml::ddl::fk_instantiation(instance):
    assert isinstance(instance, DML::DDL::Fk)

@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_nameFk_type(instance):
    assert isinstance(instance.nameFk, str)


@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original

@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_columnReference_type(instance):
    assert isinstance(instance.columnReference, str)


@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original

@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=DML::DDL::Fk_strategy)
def test_dml::ddl::fk_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DML::DDL::Pk_strategy)
@settings(max_examples=50)
def test_dml::ddl::pk_instantiation(instance):
    assert isinstance(instance, DML::DDL::Pk)

@given(instance=DML::DDL::Pk_strategy)
def test_dml::ddl::pk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DML::DDL::Pk_strategy)
def test_dml::ddl::pk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML::DDL::Pk_strategy)
def test_dml::ddl::pk_namePk_type(instance):
    assert isinstance(instance.namePk, str)


@given(instance=DML::DDL::Pk_strategy)
def test_dml::ddl::pk_namePk_setter(instance):
    original = instance.namePk
    instance.namePk = original
    assert instance.namePk == original
