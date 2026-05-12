import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Bits,
    DML_DDL_Bit,
    Characters,
    DML_DDL_VarChar2,
    DML_DDL_NationalCharacter,
    DML_DDL_NationalCharVarying,
    DML_DDL_NChar,
    DML_DDL_CharVarying,
    DML_DDL_Clob,
    DML_DDL_CharacterVarying,
    DML_DDL_NClob,
    DML_DDL_NationalCharacterVarying,
    DML_DDL_Char,
    DML_DDL_NVarChar2,
    DML_DDL_VarChar,
    DML_DDL_NCharVarying,
    DML_DDL_NationalChar,
    DML_DDL_Character,
    Binaries,
    DML_DDL_Blob,
    DML_DDL_BinaryFloat,
    DML_DDL_BFile,
    DML_DDL_BinaryDouble,
    Intervals,
    DML_DDL_DayTime,
    DML_DDL_YearMonth,
    Times,
    DML_DDL_Time,
    DML_DDL_Timestamp,
    DML_DDL_Date,
    Bit,
    DML_DDL_BitVarying,
    DML_DDL_Registry,
    DataDefinition,
    DML_DDL_Database,
    Aproximado,
    DML_DDL_DoublePrecision,
    DML_DDL_LongRaw,
    DML_DDL_Float,
    DML_DDL_Long,
    DML_DDL_Real,
    Exacto,
    DML_DDL_SmallInt,
    DML_DDL_SmallInteger,
    DML_DDL_Decimal,
    DML_DDL_Numeric,
    DML_DDL_Int,
    DML_DDL_Number,
    DML_DDL_Integer,
    Type,
    DML_DDL_Intervals,
    DML_DDL_Aproximado,
    DML_DDL_Characters,
    DML_DDL_Bits,
    DML_DDL_Binaries,
    DML_DDL_Times,
    DML_DDL_Exacto,
    DML_DDL_CommentColumn,
    DML_DDL_CommentTable,
    DML_DDL_Value,
    DML_DDL_DDLDefinition,
    DML_DDL_Type,
    DML_DDL_DataType,
    Statement,
    DML_DDL_DataDefinition,
    DML_DDL_Statement,
    DML_DDL_Column,
    DML_DDL_ValuesCk,
    DML_DDL_Ck,
    DML_DDL_Table,
    DML_DDL_Fk,
    DML_DDL_Pk,
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



def test_dml_ddl_bit_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Bit)


def test_dml_ddl_bit_constructor_exists():
    assert callable(DML_DDL_Bit.__init__)


def test_dml_ddl_bit_constructor_args():
    sig = inspect.signature(DML_DDL_Bit.__init__)
    params = list(sig.parameters.keys())



def test_characters_is_not_abstract():
    assert not inspect.isabstract(Characters)


def test_characters_constructor_exists():
    assert callable(Characters.__init__)


def test_characters_constructor_args():
    sig = inspect.signature(Characters.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_varchar2_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_VarChar2)


def test_dml_ddl_varchar2_constructor_exists():
    assert callable(DML_DDL_VarChar2.__init__)


def test_dml_ddl_varchar2_constructor_args():
    sig = inspect.signature(DML_DDL_VarChar2.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nationalcharacter_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NationalCharacter)


def test_dml_ddl_nationalcharacter_constructor_exists():
    assert callable(DML_DDL_NationalCharacter.__init__)


def test_dml_ddl_nationalcharacter_constructor_args():
    sig = inspect.signature(DML_DDL_NationalCharacter.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nationalcharvarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NationalCharVarying)


def test_dml_ddl_nationalcharvarying_constructor_exists():
    assert callable(DML_DDL_NationalCharVarying.__init__)


def test_dml_ddl_nationalcharvarying_constructor_args():
    sig = inspect.signature(DML_DDL_NationalCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nchar_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NChar)


def test_dml_ddl_nchar_constructor_exists():
    assert callable(DML_DDL_NChar.__init__)


def test_dml_ddl_nchar_constructor_args():
    sig = inspect.signature(DML_DDL_NChar.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_charvarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_CharVarying)


def test_dml_ddl_charvarying_constructor_exists():
    assert callable(DML_DDL_CharVarying.__init__)


def test_dml_ddl_charvarying_constructor_args():
    sig = inspect.signature(DML_DDL_CharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_clob_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Clob)


def test_dml_ddl_clob_constructor_exists():
    assert callable(DML_DDL_Clob.__init__)


def test_dml_ddl_clob_constructor_args():
    sig = inspect.signature(DML_DDL_Clob.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_charactervarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_CharacterVarying)


def test_dml_ddl_charactervarying_constructor_exists():
    assert callable(DML_DDL_CharacterVarying.__init__)


def test_dml_ddl_charactervarying_constructor_args():
    sig = inspect.signature(DML_DDL_CharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nclob_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NClob)


def test_dml_ddl_nclob_constructor_exists():
    assert callable(DML_DDL_NClob.__init__)


def test_dml_ddl_nclob_constructor_args():
    sig = inspect.signature(DML_DDL_NClob.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nationalcharactervarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NationalCharacterVarying)


def test_dml_ddl_nationalcharactervarying_constructor_exists():
    assert callable(DML_DDL_NationalCharacterVarying.__init__)


def test_dml_ddl_nationalcharactervarying_constructor_args():
    sig = inspect.signature(DML_DDL_NationalCharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_char_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Char)


def test_dml_ddl_char_constructor_exists():
    assert callable(DML_DDL_Char.__init__)


def test_dml_ddl_char_constructor_args():
    sig = inspect.signature(DML_DDL_Char.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nvarchar2_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NVarChar2)


def test_dml_ddl_nvarchar2_constructor_exists():
    assert callable(DML_DDL_NVarChar2.__init__)


def test_dml_ddl_nvarchar2_constructor_args():
    sig = inspect.signature(DML_DDL_NVarChar2.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_varchar_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_VarChar)


def test_dml_ddl_varchar_constructor_exists():
    assert callable(DML_DDL_VarChar.__init__)


def test_dml_ddl_varchar_constructor_args():
    sig = inspect.signature(DML_DDL_VarChar.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_ncharvarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NCharVarying)


def test_dml_ddl_ncharvarying_constructor_exists():
    assert callable(DML_DDL_NCharVarying.__init__)


def test_dml_ddl_ncharvarying_constructor_args():
    sig = inspect.signature(DML_DDL_NCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_nationalchar_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_NationalChar)


def test_dml_ddl_nationalchar_constructor_exists():
    assert callable(DML_DDL_NationalChar.__init__)


def test_dml_ddl_nationalchar_constructor_args():
    sig = inspect.signature(DML_DDL_NationalChar.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_character_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Character)


def test_dml_ddl_character_constructor_exists():
    assert callable(DML_DDL_Character.__init__)


def test_dml_ddl_character_constructor_args():
    sig = inspect.signature(DML_DDL_Character.__init__)
    params = list(sig.parameters.keys())



def test_binaries_is_not_abstract():
    assert not inspect.isabstract(Binaries)


def test_binaries_constructor_exists():
    assert callable(Binaries.__init__)


def test_binaries_constructor_args():
    sig = inspect.signature(Binaries.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_blob_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Blob)


def test_dml_ddl_blob_constructor_exists():
    assert callable(DML_DDL_Blob.__init__)


def test_dml_ddl_blob_constructor_args():
    sig = inspect.signature(DML_DDL_Blob.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_binaryfloat_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_BinaryFloat)


def test_dml_ddl_binaryfloat_constructor_exists():
    assert callable(DML_DDL_BinaryFloat.__init__)


def test_dml_ddl_binaryfloat_constructor_args():
    sig = inspect.signature(DML_DDL_BinaryFloat.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_bfile_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_BFile)


def test_dml_ddl_bfile_constructor_exists():
    assert callable(DML_DDL_BFile.__init__)


def test_dml_ddl_bfile_constructor_args():
    sig = inspect.signature(DML_DDL_BFile.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_binarydouble_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_BinaryDouble)


def test_dml_ddl_binarydouble_constructor_exists():
    assert callable(DML_DDL_BinaryDouble.__init__)


def test_dml_ddl_binarydouble_constructor_args():
    sig = inspect.signature(DML_DDL_BinaryDouble.__init__)
    params = list(sig.parameters.keys())



def test_intervals_is_not_abstract():
    assert not inspect.isabstract(Intervals)


def test_intervals_constructor_exists():
    assert callable(Intervals.__init__)


def test_intervals_constructor_args():
    sig = inspect.signature(Intervals.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_daytime_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_DayTime)


def test_dml_ddl_daytime_constructor_exists():
    assert callable(DML_DDL_DayTime.__init__)


def test_dml_ddl_daytime_constructor_args():
    sig = inspect.signature(DML_DDL_DayTime.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_yearmonth_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_YearMonth)


def test_dml_ddl_yearmonth_constructor_exists():
    assert callable(DML_DDL_YearMonth.__init__)


def test_dml_ddl_yearmonth_constructor_args():
    sig = inspect.signature(DML_DDL_YearMonth.__init__)
    params = list(sig.parameters.keys())



def test_times_is_not_abstract():
    assert not inspect.isabstract(Times)


def test_times_constructor_exists():
    assert callable(Times.__init__)


def test_times_constructor_args():
    sig = inspect.signature(Times.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_time_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Time)


def test_dml_ddl_time_constructor_exists():
    assert callable(DML_DDL_Time.__init__)


def test_dml_ddl_time_constructor_args():
    sig = inspect.signature(DML_DDL_Time.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_timestamp_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Timestamp)


def test_dml_ddl_timestamp_constructor_exists():
    assert callable(DML_DDL_Timestamp.__init__)


def test_dml_ddl_timestamp_constructor_args():
    sig = inspect.signature(DML_DDL_Timestamp.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_date_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Date)


def test_dml_ddl_date_constructor_exists():
    assert callable(DML_DDL_Date.__init__)


def test_dml_ddl_date_constructor_args():
    sig = inspect.signature(DML_DDL_Date.__init__)
    params = list(sig.parameters.keys())



def test_bit_is_not_abstract():
    assert not inspect.isabstract(Bit)


def test_bit_constructor_exists():
    assert callable(Bit.__init__)


def test_bit_constructor_args():
    sig = inspect.signature(Bit.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_bitvarying_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_BitVarying)


def test_dml_ddl_bitvarying_constructor_exists():
    assert callable(DML_DDL_BitVarying.__init__)


def test_dml_ddl_bitvarying_constructor_args():
    sig = inspect.signature(DML_DDL_BitVarying.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_registry_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Registry)


def test_dml_ddl_registry_constructor_exists():
    assert callable(DML_DDL_Registry.__init__)


def test_dml_ddl_registry_constructor_args():
    sig = inspect.signature(DML_DDL_Registry.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_database_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Database)


def test_dml_ddl_database_constructor_exists():
    assert callable(DML_DDL_Database.__init__)


def test_dml_ddl_database_constructor_args():
    sig = inspect.signature(DML_DDL_Database.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_dml_ddl_database_has_databaseName():
    assert hasattr(DML_DDL_Database, "databaseName")
    descriptor = None
    for klass in DML_DDL_Database.__mro__:
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



def test_dml_ddl_doubleprecision_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_DoublePrecision)


def test_dml_ddl_doubleprecision_constructor_exists():
    assert callable(DML_DDL_DoublePrecision.__init__)


def test_dml_ddl_doubleprecision_constructor_args():
    sig = inspect.signature(DML_DDL_DoublePrecision.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_longraw_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_LongRaw)


def test_dml_ddl_longraw_constructor_exists():
    assert callable(DML_DDL_LongRaw.__init__)


def test_dml_ddl_longraw_constructor_args():
    sig = inspect.signature(DML_DDL_LongRaw.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_float_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Float)


def test_dml_ddl_float_constructor_exists():
    assert callable(DML_DDL_Float.__init__)


def test_dml_ddl_float_constructor_args():
    sig = inspect.signature(DML_DDL_Float.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_long_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Long)


def test_dml_ddl_long_constructor_exists():
    assert callable(DML_DDL_Long.__init__)


def test_dml_ddl_long_constructor_args():
    sig = inspect.signature(DML_DDL_Long.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_real_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Real)


def test_dml_ddl_real_constructor_exists():
    assert callable(DML_DDL_Real.__init__)


def test_dml_ddl_real_constructor_args():
    sig = inspect.signature(DML_DDL_Real.__init__)
    params = list(sig.parameters.keys())



def test_exacto_is_not_abstract():
    assert not inspect.isabstract(Exacto)


def test_exacto_constructor_exists():
    assert callable(Exacto.__init__)


def test_exacto_constructor_args():
    sig = inspect.signature(Exacto.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_smallint_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_SmallInt)


def test_dml_ddl_smallint_constructor_exists():
    assert callable(DML_DDL_SmallInt.__init__)


def test_dml_ddl_smallint_constructor_args():
    sig = inspect.signature(DML_DDL_SmallInt.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_smallinteger_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_SmallInteger)


def test_dml_ddl_smallinteger_constructor_exists():
    assert callable(DML_DDL_SmallInteger.__init__)


def test_dml_ddl_smallinteger_constructor_args():
    sig = inspect.signature(DML_DDL_SmallInteger.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_decimal_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Decimal)


def test_dml_ddl_decimal_constructor_exists():
    assert callable(DML_DDL_Decimal.__init__)


def test_dml_ddl_decimal_constructor_args():
    sig = inspect.signature(DML_DDL_Decimal.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_numeric_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Numeric)


def test_dml_ddl_numeric_constructor_exists():
    assert callable(DML_DDL_Numeric.__init__)


def test_dml_ddl_numeric_constructor_args():
    sig = inspect.signature(DML_DDL_Numeric.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_int_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Int)


def test_dml_ddl_int_constructor_exists():
    assert callable(DML_DDL_Int.__init__)


def test_dml_ddl_int_constructor_args():
    sig = inspect.signature(DML_DDL_Int.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_number_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Number)


def test_dml_ddl_number_constructor_exists():
    assert callable(DML_DDL_Number.__init__)


def test_dml_ddl_number_constructor_args():
    sig = inspect.signature(DML_DDL_Number.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_integer_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Integer)


def test_dml_ddl_integer_constructor_exists():
    assert callable(DML_DDL_Integer.__init__)


def test_dml_ddl_integer_constructor_args():
    sig = inspect.signature(DML_DDL_Integer.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_intervals_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Intervals)


def test_dml_ddl_intervals_constructor_exists():
    assert callable(DML_DDL_Intervals.__init__)


def test_dml_ddl_intervals_constructor_args():
    sig = inspect.signature(DML_DDL_Intervals.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_aproximado_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Aproximado)


def test_dml_ddl_aproximado_constructor_exists():
    assert callable(DML_DDL_Aproximado.__init__)


def test_dml_ddl_aproximado_constructor_args():
    sig = inspect.signature(DML_DDL_Aproximado.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_characters_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Characters)


def test_dml_ddl_characters_constructor_exists():
    assert callable(DML_DDL_Characters.__init__)


def test_dml_ddl_characters_constructor_args():
    sig = inspect.signature(DML_DDL_Characters.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_dml_ddl_characters_has_n():
    assert hasattr(DML_DDL_Characters, "n")
    descriptor = None
    for klass in DML_DDL_Characters.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_bits_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Bits)


def test_dml_ddl_bits_constructor_exists():
    assert callable(DML_DDL_Bits.__init__)


def test_dml_ddl_bits_constructor_args():
    sig = inspect.signature(DML_DDL_Bits.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_dml_ddl_bits_has_n():
    assert hasattr(DML_DDL_Bits, "n")
    descriptor = None
    for klass in DML_DDL_Bits.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_binaries_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Binaries)


def test_dml_ddl_binaries_constructor_exists():
    assert callable(DML_DDL_Binaries.__init__)


def test_dml_ddl_binaries_constructor_args():
    sig = inspect.signature(DML_DDL_Binaries.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_times_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Times)


def test_dml_ddl_times_constructor_exists():
    assert callable(DML_DDL_Times.__init__)


def test_dml_ddl_times_constructor_args():
    sig = inspect.signature(DML_DDL_Times.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_exacto_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Exacto)


def test_dml_ddl_exacto_constructor_exists():
    assert callable(DML_DDL_Exacto.__init__)


def test_dml_ddl_exacto_constructor_args():
    sig = inspect.signature(DML_DDL_Exacto.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_commentcolumn_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_CommentColumn)


def test_dml_ddl_commentcolumn_constructor_exists():
    assert callable(DML_DDL_CommentColumn.__init__)


def test_dml_ddl_commentcolumn_constructor_args():
    sig = inspect.signature(DML_DDL_CommentColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "columnComment" in params, "Missing parameter 'columnComment'"

def test_dml_ddl_commentcolumn_has_columnName():
    assert hasattr(DML_DDL_CommentColumn, "columnName")
    descriptor = None
    for klass in DML_DDL_CommentColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_commentcolumn_has_tableName():
    assert hasattr(DML_DDL_CommentColumn, "tableName")
    descriptor = None
    for klass in DML_DDL_CommentColumn.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_commentcolumn_has_columnComment():
    assert hasattr(DML_DDL_CommentColumn, "columnComment")
    descriptor = None
    for klass in DML_DDL_CommentColumn.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_commenttable_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_CommentTable)


def test_dml_ddl_commenttable_constructor_exists():
    assert callable(DML_DDL_CommentTable.__init__)


def test_dml_ddl_commenttable_constructor_args():
    sig = inspect.signature(DML_DDL_CommentTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "tableComment" in params, "Missing parameter 'tableComment'"

def test_dml_ddl_commenttable_has_tableName():
    assert hasattr(DML_DDL_CommentTable, "tableName")
    descriptor = None
    for klass in DML_DDL_CommentTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_commenttable_has_tableComment():
    assert hasattr(DML_DDL_CommentTable, "tableComment")
    descriptor = None
    for klass in DML_DDL_CommentTable.__mro__:
        if "tableComment" in klass.__dict__:
            descriptor = klass.__dict__["tableComment"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_value_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Value)


def test_dml_ddl_value_constructor_exists():
    assert callable(DML_DDL_Value.__init__)


def test_dml_ddl_value_constructor_args():
    sig = inspect.signature(DML_DDL_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dml_ddl_value_has_value():
    assert hasattr(DML_DDL_Value, "value")
    descriptor = None
    for klass in DML_DDL_Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_DDLDefinition)


def test_dml_ddl_ddldefinition_constructor_exists():
    assert callable(DML_DDL_DDLDefinition.__init__)


def test_dml_ddl_ddldefinition_constructor_args():
    sig = inspect.signature(DML_DDL_DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_type_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Type)


def test_dml_ddl_type_constructor_exists():
    assert callable(DML_DDL_Type.__init__)


def test_dml_ddl_type_constructor_args():
    sig = inspect.signature(DML_DDL_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dml_ddl_type_has_name():
    assert hasattr(DML_DDL_Type, "name")
    descriptor = None
    for klass in DML_DDL_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_datatype_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_DataType)


def test_dml_ddl_datatype_constructor_exists():
    assert callable(DML_DDL_DataType.__init__)


def test_dml_ddl_datatype_constructor_args():
    sig = inspect.signature(DML_DDL_DataType.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_DataDefinition)


def test_dml_ddl_datadefinition_constructor_exists():
    assert callable(DML_DDL_DataDefinition.__init__)


def test_dml_ddl_datadefinition_constructor_args():
    sig = inspect.signature(DML_DDL_DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_statement_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Statement)


def test_dml_ddl_statement_constructor_exists():
    assert callable(DML_DDL_Statement.__init__)


def test_dml_ddl_statement_constructor_args():
    sig = inspect.signature(DML_DDL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dml_ddl_column_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Column)


def test_dml_ddl_column_constructor_exists():
    assert callable(DML_DDL_Column.__init__)


def test_dml_ddl_column_constructor_args():
    sig = inspect.signature(DML_DDL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnNull" in params, "Missing parameter 'columnNull'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "commentColumn" in params, "Missing parameter 'commentColumn'"

def test_dml_ddl_column_has_columnNull():
    assert hasattr(DML_DDL_Column, "columnNull")
    descriptor = None
    for klass in DML_DDL_Column.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_column_has_columnName():
    assert hasattr(DML_DDL_Column, "columnName")
    descriptor = None
    for klass in DML_DDL_Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_column_has_commentColumn():
    assert hasattr(DML_DDL_Column, "commentColumn")
    descriptor = None
    for klass in DML_DDL_Column.__mro__:
        if "commentColumn" in klass.__dict__:
            descriptor = klass.__dict__["commentColumn"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_valuesck_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_ValuesCk)


def test_dml_ddl_valuesck_constructor_exists():
    assert callable(DML_DDL_ValuesCk.__init__)


def test_dml_ddl_valuesck_constructor_args():
    sig = inspect.signature(DML_DDL_ValuesCk.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "logConjuntion" in params, "Missing parameter 'logConjuntion'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "value" in params, "Missing parameter 'value'"

def test_dml_ddl_valuesck_has_comparator():
    assert hasattr(DML_DDL_ValuesCk, "comparator")
    descriptor = None
    for klass in DML_DDL_ValuesCk.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_valuesck_has_logConjuntion():
    assert hasattr(DML_DDL_ValuesCk, "logConjuntion")
    descriptor = None
    for klass in DML_DDL_ValuesCk.__mro__:
        if "logConjuntion" in klass.__dict__:
            descriptor = klass.__dict__["logConjuntion"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_valuesck_has_columnName():
    assert hasattr(DML_DDL_ValuesCk, "columnName")
    descriptor = None
    for klass in DML_DDL_ValuesCk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_valuesck_has_value():
    assert hasattr(DML_DDL_ValuesCk, "value")
    descriptor = None
    for klass in DML_DDL_ValuesCk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_ck_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Ck)


def test_dml_ddl_ck_constructor_exists():
    assert callable(DML_DDL_Ck.__init__)


def test_dml_ddl_ck_constructor_args():
    sig = inspect.signature(DML_DDL_Ck.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nameCk" in params, "Missing parameter 'nameCk'"

def test_dml_ddl_ck_has_status():
    assert hasattr(DML_DDL_Ck, "status")
    descriptor = None
    for klass in DML_DDL_Ck.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_ck_has_nameCk():
    assert hasattr(DML_DDL_Ck, "nameCk")
    descriptor = None
    for klass in DML_DDL_Ck.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_table_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Table)


def test_dml_ddl_table_constructor_exists():
    assert callable(DML_DDL_Table.__init__)


def test_dml_ddl_table_constructor_args():
    sig = inspect.signature(DML_DDL_Table.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "commentTable" in params, "Missing parameter 'commentTable'"

def test_dml_ddl_table_has_tableName():
    assert hasattr(DML_DDL_Table, "tableName")
    descriptor = None
    for klass in DML_DDL_Table.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_table_has_commentTable():
    assert hasattr(DML_DDL_Table, "commentTable")
    descriptor = None
    for klass in DML_DDL_Table.__mro__:
        if "commentTable" in klass.__dict__:
            descriptor = klass.__dict__["commentTable"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_fk_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Fk)


def test_dml_ddl_fk_constructor_exists():
    assert callable(DML_DDL_Fk.__init__)


def test_dml_ddl_fk_constructor_args():
    sig = inspect.signature(DML_DDL_Fk.__init__)
    params = list(sig.parameters.keys())
    assert "nameFk" in params, "Missing parameter 'nameFk'"
    assert "status" in params, "Missing parameter 'status'"
    assert "columnReference" in params, "Missing parameter 'columnReference'"
    assert "type" in params, "Missing parameter 'type'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dml_ddl_fk_has_nameFk():
    assert hasattr(DML_DDL_Fk, "nameFk")
    descriptor = None
    for klass in DML_DDL_Fk.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_fk_has_status():
    assert hasattr(DML_DDL_Fk, "status")
    descriptor = None
    for klass in DML_DDL_Fk.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_fk_has_columnReference():
    assert hasattr(DML_DDL_Fk, "columnReference")
    descriptor = None
    for klass in DML_DDL_Fk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_fk_has_type():
    assert hasattr(DML_DDL_Fk, "type")
    descriptor = None
    for klass in DML_DDL_Fk.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_fk_has_columnName():
    assert hasattr(DML_DDL_Fk, "columnName")
    descriptor = None
    for klass in DML_DDL_Fk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dml_ddl_pk_is_not_abstract():
    assert not inspect.isabstract(DML_DDL_Pk)


def test_dml_ddl_pk_constructor_exists():
    assert callable(DML_DDL_Pk.__init__)


def test_dml_ddl_pk_constructor_args():
    sig = inspect.signature(DML_DDL_Pk.__init__)
    params = list(sig.parameters.keys())
    assert "namePk" in params, "Missing parameter 'namePk'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dml_ddl_pk_has_namePk():
    assert hasattr(DML_DDL_Pk, "namePk")
    descriptor = None
    for klass in DML_DDL_Pk.__mro__:
        if "namePk" in klass.__dict__:
            descriptor = klass.__dict__["namePk"]
            break
    assert isinstance(descriptor, property)

def test_dml_ddl_pk_has_columnName():
    assert hasattr(DML_DDL_Pk, "columnName")
    descriptor = None
    for klass in DML_DDL_Pk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
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
DML_DDL_Bit_strategy = st.builds(
    DML_DDL_Bit,
)
Characters_strategy = st.builds(
    Characters,
)
DML_DDL_VarChar2_strategy = st.builds(
    DML_DDL_VarChar2,
)
DML_DDL_NationalCharacter_strategy = st.builds(
    DML_DDL_NationalCharacter,
)
DML_DDL_NationalCharVarying_strategy = st.builds(
    DML_DDL_NationalCharVarying,
)
DML_DDL_NChar_strategy = st.builds(
    DML_DDL_NChar,
)
DML_DDL_CharVarying_strategy = st.builds(
    DML_DDL_CharVarying,
)
DML_DDL_Clob_strategy = st.builds(
    DML_DDL_Clob,
)
DML_DDL_CharacterVarying_strategy = st.builds(
    DML_DDL_CharacterVarying,
)
DML_DDL_NClob_strategy = st.builds(
    DML_DDL_NClob,
)
DML_DDL_NationalCharacterVarying_strategy = st.builds(
    DML_DDL_NationalCharacterVarying,
)
DML_DDL_Char_strategy = st.builds(
    DML_DDL_Char,
)
DML_DDL_NVarChar2_strategy = st.builds(
    DML_DDL_NVarChar2,
)
DML_DDL_VarChar_strategy = st.builds(
    DML_DDL_VarChar,
)
DML_DDL_NCharVarying_strategy = st.builds(
    DML_DDL_NCharVarying,
)
DML_DDL_NationalChar_strategy = st.builds(
    DML_DDL_NationalChar,
)
DML_DDL_Character_strategy = st.builds(
    DML_DDL_Character,
)
Binaries_strategy = st.builds(
    Binaries,
)
DML_DDL_Blob_strategy = st.builds(
    DML_DDL_Blob,
)
DML_DDL_BinaryFloat_strategy = st.builds(
    DML_DDL_BinaryFloat,
)
DML_DDL_BFile_strategy = st.builds(
    DML_DDL_BFile,
)
DML_DDL_BinaryDouble_strategy = st.builds(
    DML_DDL_BinaryDouble,
)
Intervals_strategy = st.builds(
    Intervals,
)
DML_DDL_DayTime_strategy = st.builds(
    DML_DDL_DayTime,
)
DML_DDL_YearMonth_strategy = st.builds(
    DML_DDL_YearMonth,
)
Times_strategy = st.builds(
    Times,
)
DML_DDL_Time_strategy = st.builds(
    DML_DDL_Time,
)
DML_DDL_Timestamp_strategy = st.builds(
    DML_DDL_Timestamp,
)
DML_DDL_Date_strategy = st.builds(
    DML_DDL_Date,
)
Bit_strategy = st.builds(
    Bit,
)
DML_DDL_BitVarying_strategy = st.builds(
    DML_DDL_BitVarying,
)
DML_DDL_Registry_strategy = st.builds(
    DML_DDL_Registry,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
DML_DDL_Database_strategy = st.builds(
    DML_DDL_Database,
    databaseName=
        safe_text
)
Aproximado_strategy = st.builds(
    Aproximado,
)
DML_DDL_DoublePrecision_strategy = st.builds(
    DML_DDL_DoublePrecision,
)
DML_DDL_LongRaw_strategy = st.builds(
    DML_DDL_LongRaw,
)
DML_DDL_Float_strategy = st.builds(
    DML_DDL_Float,
)
DML_DDL_Long_strategy = st.builds(
    DML_DDL_Long,
)
DML_DDL_Real_strategy = st.builds(
    DML_DDL_Real,
)
Exacto_strategy = st.builds(
    Exacto,
)
DML_DDL_SmallInt_strategy = st.builds(
    DML_DDL_SmallInt,
)
DML_DDL_SmallInteger_strategy = st.builds(
    DML_DDL_SmallInteger,
)
DML_DDL_Decimal_strategy = st.builds(
    DML_DDL_Decimal,
)
DML_DDL_Numeric_strategy = st.builds(
    DML_DDL_Numeric,
)
DML_DDL_Int_strategy = st.builds(
    DML_DDL_Int,
)
DML_DDL_Number_strategy = st.builds(
    DML_DDL_Number,
)
DML_DDL_Integer_strategy = st.builds(
    DML_DDL_Integer,
)
Type_strategy = st.builds(
    Type,
)
DML_DDL_Intervals_strategy = st.builds(
    DML_DDL_Intervals,
)
DML_DDL_Aproximado_strategy = st.builds(
    DML_DDL_Aproximado,
)
DML_DDL_Characters_strategy = st.builds(
    DML_DDL_Characters,
    n=
        safe_text
)
DML_DDL_Bits_strategy = st.builds(
    DML_DDL_Bits,
    n=
        safe_text
)
DML_DDL_Binaries_strategy = st.builds(
    DML_DDL_Binaries,
)
DML_DDL_Times_strategy = st.builds(
    DML_DDL_Times,
)
DML_DDL_Exacto_strategy = st.builds(
    DML_DDL_Exacto,
)
DML_DDL_CommentColumn_strategy = st.builds(
    DML_DDL_CommentColumn,
    columnName=
        safe_text,
    tableName=
        safe_text,
    columnComment=
        safe_text
)
DML_DDL_CommentTable_strategy = st.builds(
    DML_DDL_CommentTable,
    tableName=
        safe_text,
    tableComment=
        safe_text
)
DML_DDL_Value_strategy = st.builds(
    DML_DDL_Value,
    value=
        safe_text
)
DML_DDL_DDLDefinition_strategy = st.builds(
    DML_DDL_DDLDefinition,
)
DML_DDL_Type_strategy = st.builds(
    DML_DDL_Type,
    name=
        safe_text
)
DML_DDL_DataType_strategy = st.builds(
    DML_DDL_DataType,
)
Statement_strategy = st.builds(
    Statement,
)
DML_DDL_DataDefinition_strategy = st.builds(
    DML_DDL_DataDefinition,
)
DML_DDL_Statement_strategy = st.builds(
    DML_DDL_Statement,
)
DML_DDL_Column_strategy = st.builds(
    DML_DDL_Column,
    columnNull=
        st.booleans(),
    columnName=
        safe_text,
    commentColumn=
        safe_text
)
DML_DDL_ValuesCk_strategy = st.builds(
    DML_DDL_ValuesCk,
    comparator=
        safe_text,
    logConjuntion=
        safe_text,
    columnName=
        safe_text,
    value=
        safe_text
)
DML_DDL_Ck_strategy = st.builds(
    DML_DDL_Ck,
    status=
        safe_text,
    nameCk=
        safe_text
)
DML_DDL_Table_strategy = st.builds(
    DML_DDL_Table,
    tableName=
        safe_text,
    commentTable=
        safe_text
)
DML_DDL_Fk_strategy = st.builds(
    DML_DDL_Fk,
    nameFk=
        safe_text,
    status=
        safe_text,
    columnReference=
        safe_text,
    type=
        safe_text,
    columnName=
        safe_text
)
DML_DDL_Pk_strategy = st.builds(
    DML_DDL_Pk,
    namePk=
        safe_text,
    columnName=
        safe_text
)

@given(instance=Bits_strategy)
@settings(max_examples=50)
def test_bits_instantiation(instance):
    assert isinstance(instance, Bits)

@given(instance=DML_DDL_Bit_strategy)
@settings(max_examples=50)
def test_dml_ddl_bit_instantiation(instance):
    assert isinstance(instance, DML_DDL_Bit)

@given(instance=Characters_strategy)
@settings(max_examples=50)
def test_characters_instantiation(instance):
    assert isinstance(instance, Characters)

@given(instance=DML_DDL_VarChar2_strategy)
@settings(max_examples=50)
def test_dml_ddl_varchar2_instantiation(instance):
    assert isinstance(instance, DML_DDL_VarChar2)

@given(instance=DML_DDL_NationalCharacter_strategy)
@settings(max_examples=50)
def test_dml_ddl_nationalcharacter_instantiation(instance):
    assert isinstance(instance, DML_DDL_NationalCharacter)

@given(instance=DML_DDL_NationalCharVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_nationalcharvarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_NationalCharVarying)

@given(instance=DML_DDL_NChar_strategy)
@settings(max_examples=50)
def test_dml_ddl_nchar_instantiation(instance):
    assert isinstance(instance, DML_DDL_NChar)

@given(instance=DML_DDL_CharVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_charvarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_CharVarying)

@given(instance=DML_DDL_Clob_strategy)
@settings(max_examples=50)
def test_dml_ddl_clob_instantiation(instance):
    assert isinstance(instance, DML_DDL_Clob)

@given(instance=DML_DDL_CharacterVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_charactervarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_CharacterVarying)

@given(instance=DML_DDL_NClob_strategy)
@settings(max_examples=50)
def test_dml_ddl_nclob_instantiation(instance):
    assert isinstance(instance, DML_DDL_NClob)

@given(instance=DML_DDL_NationalCharacterVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_nationalcharactervarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_NationalCharacterVarying)

@given(instance=DML_DDL_Char_strategy)
@settings(max_examples=50)
def test_dml_ddl_char_instantiation(instance):
    assert isinstance(instance, DML_DDL_Char)

@given(instance=DML_DDL_NVarChar2_strategy)
@settings(max_examples=50)
def test_dml_ddl_nvarchar2_instantiation(instance):
    assert isinstance(instance, DML_DDL_NVarChar2)

@given(instance=DML_DDL_VarChar_strategy)
@settings(max_examples=50)
def test_dml_ddl_varchar_instantiation(instance):
    assert isinstance(instance, DML_DDL_VarChar)

@given(instance=DML_DDL_NCharVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_ncharvarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_NCharVarying)

@given(instance=DML_DDL_NationalChar_strategy)
@settings(max_examples=50)
def test_dml_ddl_nationalchar_instantiation(instance):
    assert isinstance(instance, DML_DDL_NationalChar)

@given(instance=DML_DDL_Character_strategy)
@settings(max_examples=50)
def test_dml_ddl_character_instantiation(instance):
    assert isinstance(instance, DML_DDL_Character)

@given(instance=Binaries_strategy)
@settings(max_examples=50)
def test_binaries_instantiation(instance):
    assert isinstance(instance, Binaries)

@given(instance=DML_DDL_Blob_strategy)
@settings(max_examples=50)
def test_dml_ddl_blob_instantiation(instance):
    assert isinstance(instance, DML_DDL_Blob)

@given(instance=DML_DDL_BinaryFloat_strategy)
@settings(max_examples=50)
def test_dml_ddl_binaryfloat_instantiation(instance):
    assert isinstance(instance, DML_DDL_BinaryFloat)

@given(instance=DML_DDL_BFile_strategy)
@settings(max_examples=50)
def test_dml_ddl_bfile_instantiation(instance):
    assert isinstance(instance, DML_DDL_BFile)

@given(instance=DML_DDL_BinaryDouble_strategy)
@settings(max_examples=50)
def test_dml_ddl_binarydouble_instantiation(instance):
    assert isinstance(instance, DML_DDL_BinaryDouble)

@given(instance=Intervals_strategy)
@settings(max_examples=50)
def test_intervals_instantiation(instance):
    assert isinstance(instance, Intervals)

@given(instance=DML_DDL_DayTime_strategy)
@settings(max_examples=50)
def test_dml_ddl_daytime_instantiation(instance):
    assert isinstance(instance, DML_DDL_DayTime)

@given(instance=DML_DDL_YearMonth_strategy)
@settings(max_examples=50)
def test_dml_ddl_yearmonth_instantiation(instance):
    assert isinstance(instance, DML_DDL_YearMonth)

@given(instance=Times_strategy)
@settings(max_examples=50)
def test_times_instantiation(instance):
    assert isinstance(instance, Times)

@given(instance=DML_DDL_Time_strategy)
@settings(max_examples=50)
def test_dml_ddl_time_instantiation(instance):
    assert isinstance(instance, DML_DDL_Time)

@given(instance=DML_DDL_Timestamp_strategy)
@settings(max_examples=50)
def test_dml_ddl_timestamp_instantiation(instance):
    assert isinstance(instance, DML_DDL_Timestamp)

@given(instance=DML_DDL_Date_strategy)
@settings(max_examples=50)
def test_dml_ddl_date_instantiation(instance):
    assert isinstance(instance, DML_DDL_Date)

@given(instance=Bit_strategy)
@settings(max_examples=50)
def test_bit_instantiation(instance):
    assert isinstance(instance, Bit)

@given(instance=DML_DDL_BitVarying_strategy)
@settings(max_examples=50)
def test_dml_ddl_bitvarying_instantiation(instance):
    assert isinstance(instance, DML_DDL_BitVarying)

@given(instance=DML_DDL_Registry_strategy)
@settings(max_examples=50)
def test_dml_ddl_registry_instantiation(instance):
    assert isinstance(instance, DML_DDL_Registry)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=DML_DDL_Database_strategy)
@settings(max_examples=50)
def test_dml_ddl_database_instantiation(instance):
    assert isinstance(instance, DML_DDL_Database)



@given(instance=DML_DDL_Database_strategy)
def test_dml_ddl_database_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=Aproximado_strategy)
@settings(max_examples=50)
def test_aproximado_instantiation(instance):
    assert isinstance(instance, Aproximado)

@given(instance=DML_DDL_DoublePrecision_strategy)
@settings(max_examples=50)
def test_dml_ddl_doubleprecision_instantiation(instance):
    assert isinstance(instance, DML_DDL_DoublePrecision)

@given(instance=DML_DDL_LongRaw_strategy)
@settings(max_examples=50)
def test_dml_ddl_longraw_instantiation(instance):
    assert isinstance(instance, DML_DDL_LongRaw)

@given(instance=DML_DDL_Float_strategy)
@settings(max_examples=50)
def test_dml_ddl_float_instantiation(instance):
    assert isinstance(instance, DML_DDL_Float)

@given(instance=DML_DDL_Long_strategy)
@settings(max_examples=50)
def test_dml_ddl_long_instantiation(instance):
    assert isinstance(instance, DML_DDL_Long)

@given(instance=DML_DDL_Real_strategy)
@settings(max_examples=50)
def test_dml_ddl_real_instantiation(instance):
    assert isinstance(instance, DML_DDL_Real)

@given(instance=Exacto_strategy)
@settings(max_examples=50)
def test_exacto_instantiation(instance):
    assert isinstance(instance, Exacto)

@given(instance=DML_DDL_SmallInt_strategy)
@settings(max_examples=50)
def test_dml_ddl_smallint_instantiation(instance):
    assert isinstance(instance, DML_DDL_SmallInt)

@given(instance=DML_DDL_SmallInteger_strategy)
@settings(max_examples=50)
def test_dml_ddl_smallinteger_instantiation(instance):
    assert isinstance(instance, DML_DDL_SmallInteger)

@given(instance=DML_DDL_Decimal_strategy)
@settings(max_examples=50)
def test_dml_ddl_decimal_instantiation(instance):
    assert isinstance(instance, DML_DDL_Decimal)

@given(instance=DML_DDL_Numeric_strategy)
@settings(max_examples=50)
def test_dml_ddl_numeric_instantiation(instance):
    assert isinstance(instance, DML_DDL_Numeric)

@given(instance=DML_DDL_Int_strategy)
@settings(max_examples=50)
def test_dml_ddl_int_instantiation(instance):
    assert isinstance(instance, DML_DDL_Int)

@given(instance=DML_DDL_Number_strategy)
@settings(max_examples=50)
def test_dml_ddl_number_instantiation(instance):
    assert isinstance(instance, DML_DDL_Number)

@given(instance=DML_DDL_Integer_strategy)
@settings(max_examples=50)
def test_dml_ddl_integer_instantiation(instance):
    assert isinstance(instance, DML_DDL_Integer)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DML_DDL_Intervals_strategy)
@settings(max_examples=50)
def test_dml_ddl_intervals_instantiation(instance):
    assert isinstance(instance, DML_DDL_Intervals)

@given(instance=DML_DDL_Aproximado_strategy)
@settings(max_examples=50)
def test_dml_ddl_aproximado_instantiation(instance):
    assert isinstance(instance, DML_DDL_Aproximado)

@given(instance=DML_DDL_Characters_strategy)
@settings(max_examples=50)
def test_dml_ddl_characters_instantiation(instance):
    assert isinstance(instance, DML_DDL_Characters)



@given(instance=DML_DDL_Characters_strategy)
def test_dml_ddl_characters_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DML_DDL_Bits_strategy)
@settings(max_examples=50)
def test_dml_ddl_bits_instantiation(instance):
    assert isinstance(instance, DML_DDL_Bits)



@given(instance=DML_DDL_Bits_strategy)
def test_dml_ddl_bits_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DML_DDL_Binaries_strategy)
@settings(max_examples=50)
def test_dml_ddl_binaries_instantiation(instance):
    assert isinstance(instance, DML_DDL_Binaries)

@given(instance=DML_DDL_Times_strategy)
@settings(max_examples=50)
def test_dml_ddl_times_instantiation(instance):
    assert isinstance(instance, DML_DDL_Times)

@given(instance=DML_DDL_Exacto_strategy)
@settings(max_examples=50)
def test_dml_ddl_exacto_instantiation(instance):
    assert isinstance(instance, DML_DDL_Exacto)

@given(instance=DML_DDL_CommentColumn_strategy)
@settings(max_examples=50)
def test_dml_ddl_commentcolumn_instantiation(instance):
    assert isinstance(instance, DML_DDL_CommentColumn)



@given(instance=DML_DDL_CommentColumn_strategy)
def test_dml_ddl_commentcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DML_DDL_CommentColumn_strategy)
def test_dml_ddl_commentcolumn_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=DML_DDL_CommentColumn_strategy)
def test_dml_ddl_commentcolumn_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original

@given(instance=DML_DDL_CommentTable_strategy)
@settings(max_examples=50)
def test_dml_ddl_commenttable_instantiation(instance):
    assert isinstance(instance, DML_DDL_CommentTable)



@given(instance=DML_DDL_CommentTable_strategy)
def test_dml_ddl_commenttable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=DML_DDL_CommentTable_strategy)
def test_dml_ddl_commenttable_tableComment_setter(instance):
    original = instance.tableComment
    instance.tableComment = original
    assert instance.tableComment == original

@given(instance=DML_DDL_Value_strategy)
@settings(max_examples=50)
def test_dml_ddl_value_instantiation(instance):
    assert isinstance(instance, DML_DDL_Value)



@given(instance=DML_DDL_Value_strategy)
def test_dml_ddl_value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML_DDL_DDLDefinition_strategy)
@settings(max_examples=50)
def test_dml_ddl_ddldefinition_instantiation(instance):
    assert isinstance(instance, DML_DDL_DDLDefinition)

@given(instance=DML_DDL_Type_strategy)
@settings(max_examples=50)
def test_dml_ddl_type_instantiation(instance):
    assert isinstance(instance, DML_DDL_Type)



@given(instance=DML_DDL_Type_strategy)
def test_dml_ddl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DML_DDL_DataType_strategy)
@settings(max_examples=50)
def test_dml_ddl_datatype_instantiation(instance):
    assert isinstance(instance, DML_DDL_DataType)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DML_DDL_DataDefinition_strategy)
@settings(max_examples=50)
def test_dml_ddl_datadefinition_instantiation(instance):
    assert isinstance(instance, DML_DDL_DataDefinition)

@given(instance=DML_DDL_Statement_strategy)
@settings(max_examples=50)
def test_dml_ddl_statement_instantiation(instance):
    assert isinstance(instance, DML_DDL_Statement)

@given(instance=DML_DDL_Column_strategy)
@settings(max_examples=50)
def test_dml_ddl_column_instantiation(instance):
    assert isinstance(instance, DML_DDL_Column)



@given(instance=DML_DDL_Column_strategy)
def test_dml_ddl_column_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original



@given(instance=DML_DDL_Column_strategy)
def test_dml_ddl_column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DML_DDL_Column_strategy)
def test_dml_ddl_column_commentColumn_setter(instance):
    original = instance.commentColumn
    instance.commentColumn = original
    assert instance.commentColumn == original

@given(instance=DML_DDL_ValuesCk_strategy)
@settings(max_examples=50)
def test_dml_ddl_valuesck_instantiation(instance):
    assert isinstance(instance, DML_DDL_ValuesCk)



@given(instance=DML_DDL_ValuesCk_strategy)
def test_dml_ddl_valuesck_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original



@given(instance=DML_DDL_ValuesCk_strategy)
def test_dml_ddl_valuesck_logConjuntion_setter(instance):
    original = instance.logConjuntion
    instance.logConjuntion = original
    assert instance.logConjuntion == original



@given(instance=DML_DDL_ValuesCk_strategy)
def test_dml_ddl_valuesck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DML_DDL_ValuesCk_strategy)
def test_dml_ddl_valuesck_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DML_DDL_Ck_strategy)
@settings(max_examples=50)
def test_dml_ddl_ck_instantiation(instance):
    assert isinstance(instance, DML_DDL_Ck)



@given(instance=DML_DDL_Ck_strategy)
def test_dml_ddl_ck_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=DML_DDL_Ck_strategy)
def test_dml_ddl_ck_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original

@given(instance=DML_DDL_Table_strategy)
@settings(max_examples=50)
def test_dml_ddl_table_instantiation(instance):
    assert isinstance(instance, DML_DDL_Table)



@given(instance=DML_DDL_Table_strategy)
def test_dml_ddl_table_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=DML_DDL_Table_strategy)
def test_dml_ddl_table_commentTable_setter(instance):
    original = instance.commentTable
    instance.commentTable = original
    assert instance.commentTable == original

@given(instance=DML_DDL_Fk_strategy)
@settings(max_examples=50)
def test_dml_ddl_fk_instantiation(instance):
    assert isinstance(instance, DML_DDL_Fk)



@given(instance=DML_DDL_Fk_strategy)
def test_dml_ddl_fk_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original



@given(instance=DML_DDL_Fk_strategy)
def test_dml_ddl_fk_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=DML_DDL_Fk_strategy)
def test_dml_ddl_fk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original



@given(instance=DML_DDL_Fk_strategy)
def test_dml_ddl_fk_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=DML_DDL_Fk_strategy)
def test_dml_ddl_fk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DML_DDL_Pk_strategy)
@settings(max_examples=50)
def test_dml_ddl_pk_instantiation(instance):
    assert isinstance(instance, DML_DDL_Pk)



@given(instance=DML_DDL_Pk_strategy)
def test_dml_ddl_pk_namePk_setter(instance):
    original = instance.namePk
    instance.namePk = original
    assert instance.namePk == original



@given(instance=DML_DDL_Pk_strategy)
def test_dml_ddl_pk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original
