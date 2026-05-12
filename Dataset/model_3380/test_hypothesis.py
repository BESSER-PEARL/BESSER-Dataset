import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ExactNumericType,
    DDL_Decimal,
    DDL_Integer,
    DDL_Dec,
    DDL_Numeric,
    NumericType,
    DDL_ExactNumericType,
    BitStringType,
    DDL_BitVarying,
    DDL_Bit,
    DatetimeType,
    DDL_Time,
    DDL_TimeStamp,
    DDL_Date,
    ApproximateNumericType,
    DDL_Real,
    DDL_DoublePrecision,
    DDL_Float,
    DDL_ApproximateNumericType,
    DDL_Small,
    DDL_Int,
    DDL_ValuesCheck,
    DDL_Type,
    NationalCharacterStringType,
    DDL_NationalCharacterVarying,
    DDL_NCharVarying,
    DDL_NationalChar,
    DDL_NChar,
    DDL_NationalCharVarying,
    DDL_NationalCharacter,
    CharacterStringType,
    DDL_CharVarying,
    DDL_Varchar,
    DDL_CharacterVarying,
    DDL_Char,
    DDL_Character,
    Type,
    DDL_DatetimeType,
    DDL_Interval,
    DDL_BitStringType,
    DDL_NationalCharacterStringType,
    DDL_NumericType,
    DDL_CharacterStringType,
    NamedElement,
    Statement,
    DDL_Table,
    DDL_Database,
    DDL_NamedElement,
    DDL_Statement,
    DDL_DDLDefinition,
    DDL_Check,
    DDL_Fk,
    DDL_Ck,
    DDL_Pk,
    DDL_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exactnumerictype_is_not_abstract():
    assert not inspect.isabstract(ExactNumericType)


def test_exactnumerictype_constructor_exists():
    assert callable(ExactNumericType.__init__)


def test_exactnumerictype_constructor_args():
    sig = inspect.signature(ExactNumericType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_decimal_is_not_abstract():
    assert not inspect.isabstract(DDL_Decimal)


def test_ddl_decimal_constructor_exists():
    assert callable(DDL_Decimal.__init__)


def test_ddl_decimal_constructor_args():
    sig = inspect.signature(DDL_Decimal.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_ddl_decimal_has_precision():
    assert hasattr(DDL_Decimal, "precision")
    descriptor = None
    for klass in DDL_Decimal.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_ddl_decimal_has_scale():
    assert hasattr(DDL_Decimal, "scale")
    descriptor = None
    for klass in DDL_Decimal.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_ddl_integer_is_not_abstract():
    assert not inspect.isabstract(DDL_Integer)


def test_ddl_integer_constructor_exists():
    assert callable(DDL_Integer.__init__)


def test_ddl_integer_constructor_args():
    sig = inspect.signature(DDL_Integer.__init__)
    params = list(sig.parameters.keys())



def test_ddl_dec_is_not_abstract():
    assert not inspect.isabstract(DDL_Dec)


def test_ddl_dec_constructor_exists():
    assert callable(DDL_Dec.__init__)


def test_ddl_dec_constructor_args():
    sig = inspect.signature(DDL_Dec.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddl_dec_has_scale():
    assert hasattr(DDL_Dec, "scale")
    descriptor = None
    for klass in DDL_Dec.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_ddl_dec_has_precision():
    assert hasattr(DDL_Dec, "precision")
    descriptor = None
    for klass in DDL_Dec.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddl_numeric_is_not_abstract():
    assert not inspect.isabstract(DDL_Numeric)


def test_ddl_numeric_constructor_exists():
    assert callable(DDL_Numeric.__init__)


def test_ddl_numeric_constructor_args():
    sig = inspect.signature(DDL_Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_ddl_numeric_has_precision():
    assert hasattr(DDL_Numeric, "precision")
    descriptor = None
    for klass in DDL_Numeric.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_ddl_numeric_has_scale():
    assert hasattr(DDL_Numeric, "scale")
    descriptor = None
    for klass in DDL_Numeric.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_exactnumerictype_is_not_abstract():
    assert not inspect.isabstract(DDL_ExactNumericType)


def test_ddl_exactnumerictype_constructor_exists():
    assert callable(DDL_ExactNumericType.__init__)


def test_ddl_exactnumerictype_constructor_args():
    sig = inspect.signature(DDL_ExactNumericType.__init__)
    params = list(sig.parameters.keys())



def test_bitstringtype_is_not_abstract():
    assert not inspect.isabstract(BitStringType)


def test_bitstringtype_constructor_exists():
    assert callable(BitStringType.__init__)


def test_bitstringtype_constructor_args():
    sig = inspect.signature(BitStringType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_bitvarying_is_not_abstract():
    assert not inspect.isabstract(DDL_BitVarying)


def test_ddl_bitvarying_constructor_exists():
    assert callable(DDL_BitVarying.__init__)


def test_ddl_bitvarying_constructor_args():
    sig = inspect.signature(DDL_BitVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_bit_is_not_abstract():
    assert not inspect.isabstract(DDL_Bit)


def test_ddl_bit_constructor_exists():
    assert callable(DDL_Bit.__init__)


def test_ddl_bit_constructor_args():
    sig = inspect.signature(DDL_Bit.__init__)
    params = list(sig.parameters.keys())



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatetimeType)


def test_datetimetype_constructor_exists():
    assert callable(DatetimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_time_is_not_abstract():
    assert not inspect.isabstract(DDL_Time)


def test_ddl_time_constructor_exists():
    assert callable(DDL_Time.__init__)


def test_ddl_time_constructor_args():
    sig = inspect.signature(DDL_Time.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"

def test_ddl_time_has_precision():
    assert hasattr(DDL_Time, "precision")
    descriptor = None
    for klass in DDL_Time.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_ddl_time_has_withTimeZone():
    assert hasattr(DDL_Time, "withTimeZone")
    descriptor = None
    for klass in DDL_Time.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)



def test_ddl_timestamp_is_not_abstract():
    assert not inspect.isabstract(DDL_TimeStamp)


def test_ddl_timestamp_constructor_exists():
    assert callable(DDL_TimeStamp.__init__)


def test_ddl_timestamp_constructor_args():
    sig = inspect.signature(DDL_TimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddl_timestamp_has_withTimeZone():
    assert hasattr(DDL_TimeStamp, "withTimeZone")
    descriptor = None
    for klass in DDL_TimeStamp.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_ddl_timestamp_has_precision():
    assert hasattr(DDL_TimeStamp, "precision")
    descriptor = None
    for klass in DDL_TimeStamp.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddl_date_is_not_abstract():
    assert not inspect.isabstract(DDL_Date)


def test_ddl_date_constructor_exists():
    assert callable(DDL_Date.__init__)


def test_ddl_date_constructor_args():
    sig = inspect.signature(DDL_Date.__init__)
    params = list(sig.parameters.keys())



def test_approximatenumerictype_is_not_abstract():
    assert not inspect.isabstract(ApproximateNumericType)


def test_approximatenumerictype_constructor_exists():
    assert callable(ApproximateNumericType.__init__)


def test_approximatenumerictype_constructor_args():
    sig = inspect.signature(ApproximateNumericType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_real_is_not_abstract():
    assert not inspect.isabstract(DDL_Real)


def test_ddl_real_constructor_exists():
    assert callable(DDL_Real.__init__)


def test_ddl_real_constructor_args():
    sig = inspect.signature(DDL_Real.__init__)
    params = list(sig.parameters.keys())



def test_ddl_doubleprecision_is_not_abstract():
    assert not inspect.isabstract(DDL_DoublePrecision)


def test_ddl_doubleprecision_constructor_exists():
    assert callable(DDL_DoublePrecision.__init__)


def test_ddl_doubleprecision_constructor_args():
    sig = inspect.signature(DDL_DoublePrecision.__init__)
    params = list(sig.parameters.keys())



def test_ddl_float_is_not_abstract():
    assert not inspect.isabstract(DDL_Float)


def test_ddl_float_constructor_exists():
    assert callable(DDL_Float.__init__)


def test_ddl_float_constructor_args():
    sig = inspect.signature(DDL_Float.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_ddl_float_has_precision():
    assert hasattr(DDL_Float, "precision")
    descriptor = None
    for klass in DDL_Float.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_ddl_approximatenumerictype_is_not_abstract():
    assert not inspect.isabstract(DDL_ApproximateNumericType)


def test_ddl_approximatenumerictype_constructor_exists():
    assert callable(DDL_ApproximateNumericType.__init__)


def test_ddl_approximatenumerictype_constructor_args():
    sig = inspect.signature(DDL_ApproximateNumericType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_small_is_not_abstract():
    assert not inspect.isabstract(DDL_Small)


def test_ddl_small_constructor_exists():
    assert callable(DDL_Small.__init__)


def test_ddl_small_constructor_args():
    sig = inspect.signature(DDL_Small.__init__)
    params = list(sig.parameters.keys())



def test_ddl_int_is_not_abstract():
    assert not inspect.isabstract(DDL_Int)


def test_ddl_int_constructor_exists():
    assert callable(DDL_Int.__init__)


def test_ddl_int_constructor_args():
    sig = inspect.signature(DDL_Int.__init__)
    params = list(sig.parameters.keys())



def test_ddl_valuescheck_is_not_abstract():
    assert not inspect.isabstract(DDL_ValuesCheck)


def test_ddl_valuescheck_constructor_exists():
    assert callable(DDL_ValuesCheck.__init__)


def test_ddl_valuescheck_constructor_args():
    sig = inspect.signature(DDL_ValuesCheck.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "logConjuntion" in params, "Missing parameter 'logConjuntion'"
    assert "value" in params, "Missing parameter 'value'"

def test_ddl_valuescheck_has_columnName():
    assert hasattr(DDL_ValuesCheck, "columnName")
    descriptor = None
    for klass in DDL_ValuesCheck.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_valuescheck_has_comparator():
    assert hasattr(DDL_ValuesCheck, "comparator")
    descriptor = None
    for klass in DDL_ValuesCheck.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_ddl_valuescheck_has_logConjuntion():
    assert hasattr(DDL_ValuesCheck, "logConjuntion")
    descriptor = None
    for klass in DDL_ValuesCheck.__mro__:
        if "logConjuntion" in klass.__dict__:
            descriptor = klass.__dict__["logConjuntion"]
            break
    assert isinstance(descriptor, property)

def test_ddl_valuescheck_has_value():
    assert hasattr(DDL_ValuesCheck, "value")
    descriptor = None
    for klass in DDL_ValuesCheck.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddl_type_is_not_abstract():
    assert not inspect.isabstract(DDL_Type)


def test_ddl_type_constructor_exists():
    assert callable(DDL_Type.__init__)


def test_ddl_type_constructor_args():
    sig = inspect.signature(DDL_Type.__init__)
    params = list(sig.parameters.keys())



def test_nationalcharacterstringtype_is_not_abstract():
    assert not inspect.isabstract(NationalCharacterStringType)


def test_nationalcharacterstringtype_constructor_exists():
    assert callable(NationalCharacterStringType.__init__)


def test_nationalcharacterstringtype_constructor_args():
    sig = inspect.signature(NationalCharacterStringType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_nationalcharactervarying_is_not_abstract():
    assert not inspect.isabstract(DDL_NationalCharacterVarying)


def test_ddl_nationalcharactervarying_constructor_exists():
    assert callable(DDL_NationalCharacterVarying.__init__)


def test_ddl_nationalcharactervarying_constructor_args():
    sig = inspect.signature(DDL_NationalCharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_ncharvarying_is_not_abstract():
    assert not inspect.isabstract(DDL_NCharVarying)


def test_ddl_ncharvarying_constructor_exists():
    assert callable(DDL_NCharVarying.__init__)


def test_ddl_ncharvarying_constructor_args():
    sig = inspect.signature(DDL_NCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_nationalchar_is_not_abstract():
    assert not inspect.isabstract(DDL_NationalChar)


def test_ddl_nationalchar_constructor_exists():
    assert callable(DDL_NationalChar.__init__)


def test_ddl_nationalchar_constructor_args():
    sig = inspect.signature(DDL_NationalChar.__init__)
    params = list(sig.parameters.keys())



def test_ddl_nchar_is_not_abstract():
    assert not inspect.isabstract(DDL_NChar)


def test_ddl_nchar_constructor_exists():
    assert callable(DDL_NChar.__init__)


def test_ddl_nchar_constructor_args():
    sig = inspect.signature(DDL_NChar.__init__)
    params = list(sig.parameters.keys())



def test_ddl_nationalcharvarying_is_not_abstract():
    assert not inspect.isabstract(DDL_NationalCharVarying)


def test_ddl_nationalcharvarying_constructor_exists():
    assert callable(DDL_NationalCharVarying.__init__)


def test_ddl_nationalcharvarying_constructor_args():
    sig = inspect.signature(DDL_NationalCharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_nationalcharacter_is_not_abstract():
    assert not inspect.isabstract(DDL_NationalCharacter)


def test_ddl_nationalcharacter_constructor_exists():
    assert callable(DDL_NationalCharacter.__init__)


def test_ddl_nationalcharacter_constructor_args():
    sig = inspect.signature(DDL_NationalCharacter.__init__)
    params = list(sig.parameters.keys())



def test_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(CharacterStringType)


def test_characterstringtype_constructor_exists():
    assert callable(CharacterStringType.__init__)


def test_characterstringtype_constructor_args():
    sig = inspect.signature(CharacterStringType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_charvarying_is_not_abstract():
    assert not inspect.isabstract(DDL_CharVarying)


def test_ddl_charvarying_constructor_exists():
    assert callable(DDL_CharVarying.__init__)


def test_ddl_charvarying_constructor_args():
    sig = inspect.signature(DDL_CharVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_varchar_is_not_abstract():
    assert not inspect.isabstract(DDL_Varchar)


def test_ddl_varchar_constructor_exists():
    assert callable(DDL_Varchar.__init__)


def test_ddl_varchar_constructor_args():
    sig = inspect.signature(DDL_Varchar.__init__)
    params = list(sig.parameters.keys())



def test_ddl_charactervarying_is_not_abstract():
    assert not inspect.isabstract(DDL_CharacterVarying)


def test_ddl_charactervarying_constructor_exists():
    assert callable(DDL_CharacterVarying.__init__)


def test_ddl_charactervarying_constructor_args():
    sig = inspect.signature(DDL_CharacterVarying.__init__)
    params = list(sig.parameters.keys())



def test_ddl_char_is_not_abstract():
    assert not inspect.isabstract(DDL_Char)


def test_ddl_char_constructor_exists():
    assert callable(DDL_Char.__init__)


def test_ddl_char_constructor_args():
    sig = inspect.signature(DDL_Char.__init__)
    params = list(sig.parameters.keys())



def test_ddl_character_is_not_abstract():
    assert not inspect.isabstract(DDL_Character)


def test_ddl_character_constructor_exists():
    assert callable(DDL_Character.__init__)


def test_ddl_character_constructor_args():
    sig = inspect.signature(DDL_Character.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ddl_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DDL_DatetimeType)


def test_ddl_datetimetype_constructor_exists():
    assert callable(DDL_DatetimeType.__init__)


def test_ddl_datetimetype_constructor_args():
    sig = inspect.signature(DDL_DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_interval_is_not_abstract():
    assert not inspect.isabstract(DDL_Interval)


def test_ddl_interval_constructor_exists():
    assert callable(DDL_Interval.__init__)


def test_ddl_interval_constructor_args():
    sig = inspect.signature(DDL_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "precision1" in params, "Missing parameter 'precision1'"
    assert "field2" in params, "Missing parameter 'field2'"
    assert "precision2" in params, "Missing parameter 'precision2'"
    assert "field1" in params, "Missing parameter 'field1'"

def test_ddl_interval_has_precision1():
    assert hasattr(DDL_Interval, "precision1")
    descriptor = None
    for klass in DDL_Interval.__mro__:
        if "precision1" in klass.__dict__:
            descriptor = klass.__dict__["precision1"]
            break
    assert isinstance(descriptor, property)

def test_ddl_interval_has_field2():
    assert hasattr(DDL_Interval, "field2")
    descriptor = None
    for klass in DDL_Interval.__mro__:
        if "field2" in klass.__dict__:
            descriptor = klass.__dict__["field2"]
            break
    assert isinstance(descriptor, property)

def test_ddl_interval_has_precision2():
    assert hasattr(DDL_Interval, "precision2")
    descriptor = None
    for klass in DDL_Interval.__mro__:
        if "precision2" in klass.__dict__:
            descriptor = klass.__dict__["precision2"]
            break
    assert isinstance(descriptor, property)

def test_ddl_interval_has_field1():
    assert hasattr(DDL_Interval, "field1")
    descriptor = None
    for klass in DDL_Interval.__mro__:
        if "field1" in klass.__dict__:
            descriptor = klass.__dict__["field1"]
            break
    assert isinstance(descriptor, property)



def test_ddl_bitstringtype_is_not_abstract():
    assert not inspect.isabstract(DDL_BitStringType)


def test_ddl_bitstringtype_constructor_exists():
    assert callable(DDL_BitStringType.__init__)


def test_ddl_bitstringtype_constructor_args():
    sig = inspect.signature(DDL_BitStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_ddl_bitstringtype_has_length():
    assert hasattr(DDL_BitStringType, "length")
    descriptor = None
    for klass in DDL_BitStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_ddl_nationalcharacterstringtype_is_not_abstract():
    assert not inspect.isabstract(DDL_NationalCharacterStringType)


def test_ddl_nationalcharacterstringtype_constructor_exists():
    assert callable(DDL_NationalCharacterStringType.__init__)


def test_ddl_nationalcharacterstringtype_constructor_args():
    sig = inspect.signature(DDL_NationalCharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_ddl_nationalcharacterstringtype_has_length():
    assert hasattr(DDL_NationalCharacterStringType, "length")
    descriptor = None
    for klass in DDL_NationalCharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_ddl_numerictype_is_not_abstract():
    assert not inspect.isabstract(DDL_NumericType)


def test_ddl_numerictype_constructor_exists():
    assert callable(DDL_NumericType.__init__)


def test_ddl_numerictype_constructor_args():
    sig = inspect.signature(DDL_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ddl_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(DDL_CharacterStringType)


def test_ddl_characterstringtype_constructor_exists():
    assert callable(DDL_CharacterStringType.__init__)


def test_ddl_characterstringtype_constructor_args():
    sig = inspect.signature(DDL_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_ddl_characterstringtype_has_length():
    assert hasattr(DDL_CharacterStringType, "length")
    descriptor = None
    for klass in DDL_CharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ddl_table_is_not_abstract():
    assert not inspect.isabstract(DDL_Table)


def test_ddl_table_constructor_exists():
    assert callable(DDL_Table.__init__)


def test_ddl_table_constructor_args():
    sig = inspect.signature(DDL_Table.__init__)
    params = list(sig.parameters.keys())



def test_ddl_database_is_not_abstract():
    assert not inspect.isabstract(DDL_Database)


def test_ddl_database_constructor_exists():
    assert callable(DDL_Database.__init__)


def test_ddl_database_constructor_args():
    sig = inspect.signature(DDL_Database.__init__)
    params = list(sig.parameters.keys())



def test_ddl_namedelement_is_not_abstract():
    assert not inspect.isabstract(DDL_NamedElement)


def test_ddl_namedelement_constructor_exists():
    assert callable(DDL_NamedElement.__init__)


def test_ddl_namedelement_constructor_args():
    sig = inspect.signature(DDL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddl_namedelement_has_name():
    assert hasattr(DDL_NamedElement, "name")
    descriptor = None
    for klass in DDL_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddl_statement_is_not_abstract():
    assert not inspect.isabstract(DDL_Statement)


def test_ddl_statement_constructor_exists():
    assert callable(DDL_Statement.__init__)


def test_ddl_statement_constructor_args():
    sig = inspect.signature(DDL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_ddl_ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DDL_DDLDefinition)


def test_ddl_ddldefinition_constructor_exists():
    assert callable(DDL_DDLDefinition.__init__)


def test_ddl_ddldefinition_constructor_args():
    sig = inspect.signature(DDL_DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl_check_is_not_abstract():
    assert not inspect.isabstract(DDL_Check)


def test_ddl_check_constructor_exists():
    assert callable(DDL_Check.__init__)


def test_ddl_check_constructor_args():
    sig = inspect.signature(DDL_Check.__init__)
    params = list(sig.parameters.keys())



def test_ddl_fk_is_not_abstract():
    assert not inspect.isabstract(DDL_Fk)


def test_ddl_fk_constructor_exists():
    assert callable(DDL_Fk.__init__)


def test_ddl_fk_constructor_args():
    sig = inspect.signature(DDL_Fk.__init__)
    params = list(sig.parameters.keys())
    assert "columnReference" in params, "Missing parameter 'columnReference'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl_fk_has_columnReference():
    assert hasattr(DDL_Fk, "columnReference")
    descriptor = None
    for klass in DDL_Fk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)

def test_ddl_fk_has_columnName():
    assert hasattr(DDL_Fk, "columnName")
    descriptor = None
    for klass in DDL_Fk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_ck_is_not_abstract():
    assert not inspect.isabstract(DDL_Ck)


def test_ddl_ck_constructor_exists():
    assert callable(DDL_Ck.__init__)


def test_ddl_ck_constructor_args():
    sig = inspect.signature(DDL_Ck.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl_ck_has_columnName():
    assert hasattr(DDL_Ck, "columnName")
    descriptor = None
    for klass in DDL_Ck.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_pk_is_not_abstract():
    assert not inspect.isabstract(DDL_Pk)


def test_ddl_pk_constructor_exists():
    assert callable(DDL_Pk.__init__)


def test_ddl_pk_constructor_args():
    sig = inspect.signature(DDL_Pk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl_pk_has_columnName():
    assert hasattr(DDL_Pk, "columnName")
    descriptor = None
    for klass in DDL_Pk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_column_is_not_abstract():
    assert not inspect.isabstract(DDL_Column)


def test_ddl_column_constructor_exists():
    assert callable(DDL_Column.__init__)


def test_ddl_column_constructor_args():
    sig = inspect.signature(DDL_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnNull" in params, "Missing parameter 'columnNull'"

def test_ddl_column_has_columnNull():
    assert hasattr(DDL_Column, "columnNull")
    descriptor = None
    for klass in DDL_Column.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
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
ExactNumericType_strategy = st.builds(
    ExactNumericType,
)
DDL_Decimal_strategy = st.builds(
    DDL_Decimal,
    precision=
        st.integers(),
    scale=
        st.integers()
)
DDL_Integer_strategy = st.builds(
    DDL_Integer,
)
DDL_Dec_strategy = st.builds(
    DDL_Dec,
    scale=
        st.integers(),
    precision=
        st.integers()
)
DDL_Numeric_strategy = st.builds(
    DDL_Numeric,
    precision=
        st.integers(),
    scale=
        st.integers()
)
NumericType_strategy = st.builds(
    NumericType,
)
DDL_ExactNumericType_strategy = st.builds(
    DDL_ExactNumericType,
)
BitStringType_strategy = st.builds(
    BitStringType,
)
DDL_BitVarying_strategy = st.builds(
    DDL_BitVarying,
)
DDL_Bit_strategy = st.builds(
    DDL_Bit,
)
DatetimeType_strategy = st.builds(
    DatetimeType,
)
DDL_Time_strategy = st.builds(
    DDL_Time,
    precision=
        st.integers(),
    withTimeZone=
        st.booleans()
)
DDL_TimeStamp_strategy = st.builds(
    DDL_TimeStamp,
    withTimeZone=
        st.booleans(),
    precision=
        st.integers()
)
DDL_Date_strategy = st.builds(
    DDL_Date,
)
ApproximateNumericType_strategy = st.builds(
    ApproximateNumericType,
)
DDL_Real_strategy = st.builds(
    DDL_Real,
)
DDL_DoublePrecision_strategy = st.builds(
    DDL_DoublePrecision,
)
DDL_Float_strategy = st.builds(
    DDL_Float,
    precision=
        st.integers()
)
DDL_ApproximateNumericType_strategy = st.builds(
    DDL_ApproximateNumericType,
)
DDL_Small_strategy = st.builds(
    DDL_Small,
)
DDL_Int_strategy = st.builds(
    DDL_Int,
)
DDL_ValuesCheck_strategy = st.builds(
    DDL_ValuesCheck,
    columnName=
        safe_text,
    comparator=
        safe_text,
    logConjuntion=
        safe_text,
    value=
        safe_text
)
DDL_Type_strategy = st.builds(
    DDL_Type,
)
NationalCharacterStringType_strategy = st.builds(
    NationalCharacterStringType,
)
DDL_NationalCharacterVarying_strategy = st.builds(
    DDL_NationalCharacterVarying,
)
DDL_NCharVarying_strategy = st.builds(
    DDL_NCharVarying,
)
DDL_NationalChar_strategy = st.builds(
    DDL_NationalChar,
)
DDL_NChar_strategy = st.builds(
    DDL_NChar,
)
DDL_NationalCharVarying_strategy = st.builds(
    DDL_NationalCharVarying,
)
DDL_NationalCharacter_strategy = st.builds(
    DDL_NationalCharacter,
)
CharacterStringType_strategy = st.builds(
    CharacterStringType,
)
DDL_CharVarying_strategy = st.builds(
    DDL_CharVarying,
)
DDL_Varchar_strategy = st.builds(
    DDL_Varchar,
)
DDL_CharacterVarying_strategy = st.builds(
    DDL_CharacterVarying,
)
DDL_Char_strategy = st.builds(
    DDL_Char,
)
DDL_Character_strategy = st.builds(
    DDL_Character,
)
Type_strategy = st.builds(
    Type,
)
DDL_DatetimeType_strategy = st.builds(
    DDL_DatetimeType,
)
DDL_Interval_strategy = st.builds(
    DDL_Interval,
    precision1=
        st.integers(),
    field2=
        safe_text,
    precision2=
        st.integers(),
    field1=
        safe_text
)
DDL_BitStringType_strategy = st.builds(
    DDL_BitStringType,
    length=
        st.integers()
)
DDL_NationalCharacterStringType_strategy = st.builds(
    DDL_NationalCharacterStringType,
    length=
        st.integers()
)
DDL_NumericType_strategy = st.builds(
    DDL_NumericType,
)
DDL_CharacterStringType_strategy = st.builds(
    DDL_CharacterStringType,
    length=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Statement_strategy = st.builds(
    Statement,
)
DDL_Table_strategy = st.builds(
    DDL_Table,
)
DDL_Database_strategy = st.builds(
    DDL_Database,
)
DDL_NamedElement_strategy = st.builds(
    DDL_NamedElement,
    name=
        safe_text
)
DDL_Statement_strategy = st.builds(
    DDL_Statement,
)
DDL_DDLDefinition_strategy = st.builds(
    DDL_DDLDefinition,
)
DDL_Check_strategy = st.builds(
    DDL_Check,
)
DDL_Fk_strategy = st.builds(
    DDL_Fk,
    columnReference=
        safe_text,
    columnName=
        safe_text
)
DDL_Ck_strategy = st.builds(
    DDL_Ck,
    columnName=
        safe_text
)
DDL_Pk_strategy = st.builds(
    DDL_Pk,
    columnName=
        safe_text
)
DDL_Column_strategy = st.builds(
    DDL_Column,
    columnNull=
        st.booleans()
)

@given(instance=ExactNumericType_strategy)
@settings(max_examples=50)
def test_exactnumerictype_instantiation(instance):
    assert isinstance(instance, ExactNumericType)

@given(instance=DDL_Decimal_strategy)
@settings(max_examples=50)
def test_ddl_decimal_instantiation(instance):
    assert isinstance(instance, DDL_Decimal)



@given(instance=DDL_Decimal_strategy)
def test_ddl_decimal_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=DDL_Decimal_strategy)
def test_ddl_decimal_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=DDL_Integer_strategy)
@settings(max_examples=50)
def test_ddl_integer_instantiation(instance):
    assert isinstance(instance, DDL_Integer)

@given(instance=DDL_Dec_strategy)
@settings(max_examples=50)
def test_ddl_dec_instantiation(instance):
    assert isinstance(instance, DDL_Dec)



@given(instance=DDL_Dec_strategy)
def test_ddl_dec_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=DDL_Dec_strategy)
def test_ddl_dec_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=DDL_Numeric_strategy)
@settings(max_examples=50)
def test_ddl_numeric_instantiation(instance):
    assert isinstance(instance, DDL_Numeric)



@given(instance=DDL_Numeric_strategy)
def test_ddl_numeric_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=DDL_Numeric_strategy)
def test_ddl_numeric_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=DDL_ExactNumericType_strategy)
@settings(max_examples=50)
def test_ddl_exactnumerictype_instantiation(instance):
    assert isinstance(instance, DDL_ExactNumericType)

@given(instance=BitStringType_strategy)
@settings(max_examples=50)
def test_bitstringtype_instantiation(instance):
    assert isinstance(instance, BitStringType)

@given(instance=DDL_BitVarying_strategy)
@settings(max_examples=50)
def test_ddl_bitvarying_instantiation(instance):
    assert isinstance(instance, DDL_BitVarying)

@given(instance=DDL_Bit_strategy)
@settings(max_examples=50)
def test_ddl_bit_instantiation(instance):
    assert isinstance(instance, DDL_Bit)

@given(instance=DatetimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DatetimeType)

@given(instance=DDL_Time_strategy)
@settings(max_examples=50)
def test_ddl_time_instantiation(instance):
    assert isinstance(instance, DDL_Time)



@given(instance=DDL_Time_strategy)
def test_ddl_time_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=DDL_Time_strategy)
def test_ddl_time_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original

@given(instance=DDL_TimeStamp_strategy)
@settings(max_examples=50)
def test_ddl_timestamp_instantiation(instance):
    assert isinstance(instance, DDL_TimeStamp)



@given(instance=DDL_TimeStamp_strategy)
def test_ddl_timestamp_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original



@given(instance=DDL_TimeStamp_strategy)
def test_ddl_timestamp_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=DDL_Date_strategy)
@settings(max_examples=50)
def test_ddl_date_instantiation(instance):
    assert isinstance(instance, DDL_Date)

@given(instance=ApproximateNumericType_strategy)
@settings(max_examples=50)
def test_approximatenumerictype_instantiation(instance):
    assert isinstance(instance, ApproximateNumericType)

@given(instance=DDL_Real_strategy)
@settings(max_examples=50)
def test_ddl_real_instantiation(instance):
    assert isinstance(instance, DDL_Real)

@given(instance=DDL_DoublePrecision_strategy)
@settings(max_examples=50)
def test_ddl_doubleprecision_instantiation(instance):
    assert isinstance(instance, DDL_DoublePrecision)

@given(instance=DDL_Float_strategy)
@settings(max_examples=50)
def test_ddl_float_instantiation(instance):
    assert isinstance(instance, DDL_Float)



@given(instance=DDL_Float_strategy)
def test_ddl_float_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=DDL_ApproximateNumericType_strategy)
@settings(max_examples=50)
def test_ddl_approximatenumerictype_instantiation(instance):
    assert isinstance(instance, DDL_ApproximateNumericType)

@given(instance=DDL_Small_strategy)
@settings(max_examples=50)
def test_ddl_small_instantiation(instance):
    assert isinstance(instance, DDL_Small)

@given(instance=DDL_Int_strategy)
@settings(max_examples=50)
def test_ddl_int_instantiation(instance):
    assert isinstance(instance, DDL_Int)

@given(instance=DDL_ValuesCheck_strategy)
@settings(max_examples=50)
def test_ddl_valuescheck_instantiation(instance):
    assert isinstance(instance, DDL_ValuesCheck)



@given(instance=DDL_ValuesCheck_strategy)
def test_ddl_valuescheck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DDL_ValuesCheck_strategy)
def test_ddl_valuescheck_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original



@given(instance=DDL_ValuesCheck_strategy)
def test_ddl_valuescheck_logConjuntion_setter(instance):
    original = instance.logConjuntion
    instance.logConjuntion = original
    assert instance.logConjuntion == original



@given(instance=DDL_ValuesCheck_strategy)
def test_ddl_valuescheck_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DDL_Type_strategy)
@settings(max_examples=50)
def test_ddl_type_instantiation(instance):
    assert isinstance(instance, DDL_Type)

@given(instance=NationalCharacterStringType_strategy)
@settings(max_examples=50)
def test_nationalcharacterstringtype_instantiation(instance):
    assert isinstance(instance, NationalCharacterStringType)

@given(instance=DDL_NationalCharacterVarying_strategy)
@settings(max_examples=50)
def test_ddl_nationalcharactervarying_instantiation(instance):
    assert isinstance(instance, DDL_NationalCharacterVarying)

@given(instance=DDL_NCharVarying_strategy)
@settings(max_examples=50)
def test_ddl_ncharvarying_instantiation(instance):
    assert isinstance(instance, DDL_NCharVarying)

@given(instance=DDL_NationalChar_strategy)
@settings(max_examples=50)
def test_ddl_nationalchar_instantiation(instance):
    assert isinstance(instance, DDL_NationalChar)

@given(instance=DDL_NChar_strategy)
@settings(max_examples=50)
def test_ddl_nchar_instantiation(instance):
    assert isinstance(instance, DDL_NChar)

@given(instance=DDL_NationalCharVarying_strategy)
@settings(max_examples=50)
def test_ddl_nationalcharvarying_instantiation(instance):
    assert isinstance(instance, DDL_NationalCharVarying)

@given(instance=DDL_NationalCharacter_strategy)
@settings(max_examples=50)
def test_ddl_nationalcharacter_instantiation(instance):
    assert isinstance(instance, DDL_NationalCharacter)

@given(instance=CharacterStringType_strategy)
@settings(max_examples=50)
def test_characterstringtype_instantiation(instance):
    assert isinstance(instance, CharacterStringType)

@given(instance=DDL_CharVarying_strategy)
@settings(max_examples=50)
def test_ddl_charvarying_instantiation(instance):
    assert isinstance(instance, DDL_CharVarying)

@given(instance=DDL_Varchar_strategy)
@settings(max_examples=50)
def test_ddl_varchar_instantiation(instance):
    assert isinstance(instance, DDL_Varchar)

@given(instance=DDL_CharacterVarying_strategy)
@settings(max_examples=50)
def test_ddl_charactervarying_instantiation(instance):
    assert isinstance(instance, DDL_CharacterVarying)

@given(instance=DDL_Char_strategy)
@settings(max_examples=50)
def test_ddl_char_instantiation(instance):
    assert isinstance(instance, DDL_Char)

@given(instance=DDL_Character_strategy)
@settings(max_examples=50)
def test_ddl_character_instantiation(instance):
    assert isinstance(instance, DDL_Character)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DDL_DatetimeType_strategy)
@settings(max_examples=50)
def test_ddl_datetimetype_instantiation(instance):
    assert isinstance(instance, DDL_DatetimeType)

@given(instance=DDL_Interval_strategy)
@settings(max_examples=50)
def test_ddl_interval_instantiation(instance):
    assert isinstance(instance, DDL_Interval)



@given(instance=DDL_Interval_strategy)
def test_ddl_interval_precision1_setter(instance):
    original = instance.precision1
    instance.precision1 = original
    assert instance.precision1 == original



@given(instance=DDL_Interval_strategy)
def test_ddl_interval_field2_setter(instance):
    original = instance.field2
    instance.field2 = original
    assert instance.field2 == original



@given(instance=DDL_Interval_strategy)
def test_ddl_interval_precision2_setter(instance):
    original = instance.precision2
    instance.precision2 = original
    assert instance.precision2 == original



@given(instance=DDL_Interval_strategy)
def test_ddl_interval_field1_setter(instance):
    original = instance.field1
    instance.field1 = original
    assert instance.field1 == original

@given(instance=DDL_BitStringType_strategy)
@settings(max_examples=50)
def test_ddl_bitstringtype_instantiation(instance):
    assert isinstance(instance, DDL_BitStringType)



@given(instance=DDL_BitStringType_strategy)
def test_ddl_bitstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=DDL_NationalCharacterStringType_strategy)
@settings(max_examples=50)
def test_ddl_nationalcharacterstringtype_instantiation(instance):
    assert isinstance(instance, DDL_NationalCharacterStringType)



@given(instance=DDL_NationalCharacterStringType_strategy)
def test_ddl_nationalcharacterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=DDL_NumericType_strategy)
@settings(max_examples=50)
def test_ddl_numerictype_instantiation(instance):
    assert isinstance(instance, DDL_NumericType)

@given(instance=DDL_CharacterStringType_strategy)
@settings(max_examples=50)
def test_ddl_characterstringtype_instantiation(instance):
    assert isinstance(instance, DDL_CharacterStringType)



@given(instance=DDL_CharacterStringType_strategy)
def test_ddl_characterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DDL_Table_strategy)
@settings(max_examples=50)
def test_ddl_table_instantiation(instance):
    assert isinstance(instance, DDL_Table)

@given(instance=DDL_Database_strategy)
@settings(max_examples=50)
def test_ddl_database_instantiation(instance):
    assert isinstance(instance, DDL_Database)

@given(instance=DDL_NamedElement_strategy)
@settings(max_examples=50)
def test_ddl_namedelement_instantiation(instance):
    assert isinstance(instance, DDL_NamedElement)



@given(instance=DDL_NamedElement_strategy)
def test_ddl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DDL_Statement_strategy)
@settings(max_examples=50)
def test_ddl_statement_instantiation(instance):
    assert isinstance(instance, DDL_Statement)

@given(instance=DDL_DDLDefinition_strategy)
@settings(max_examples=50)
def test_ddl_ddldefinition_instantiation(instance):
    assert isinstance(instance, DDL_DDLDefinition)

@given(instance=DDL_Check_strategy)
@settings(max_examples=50)
def test_ddl_check_instantiation(instance):
    assert isinstance(instance, DDL_Check)

@given(instance=DDL_Fk_strategy)
@settings(max_examples=50)
def test_ddl_fk_instantiation(instance):
    assert isinstance(instance, DDL_Fk)



@given(instance=DDL_Fk_strategy)
def test_ddl_fk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original



@given(instance=DDL_Fk_strategy)
def test_ddl_fk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL_Ck_strategy)
@settings(max_examples=50)
def test_ddl_ck_instantiation(instance):
    assert isinstance(instance, DDL_Ck)



@given(instance=DDL_Ck_strategy)
def test_ddl_ck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL_Pk_strategy)
@settings(max_examples=50)
def test_ddl_pk_instantiation(instance):
    assert isinstance(instance, DDL_Pk)



@given(instance=DDL_Pk_strategy)
def test_ddl_pk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL_Column_strategy)
@settings(max_examples=50)
def test_ddl_column_instantiation(instance):
    assert isinstance(instance, DDL_Column)



@given(instance=DDL_Column_strategy)
def test_ddl_column_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original
