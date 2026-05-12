import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PredefinedType,
    sql_datatype_BooleanType,
    sql_datatype_DatetimeType,
    sql_datatype_BinaryLargeObjectStringType,
    sql_datatype_CharacterStringType,
    DataType,
    sql_datatype_PredefinedType,
    sql_datatype_DataType,
    sql_datatype_NationalCharacterStringType,
    DatetimeLiteral,
    sql_literal_TimestampLiteral,
    sql_literal_TimeLiteral,
    sql_literal_DateLiteral,
    NumericLiteral,
    sql_literal_ApproximateNumericLiteral,
    sql_literal_ExactNumericLiteral,
    SchemaQualifiedName,
    NationalCharacterStringLiteral,
    sql_literal_CharacterStringLiteral,
    Literal,
    sql_literal_NumericLiteral,
    sql_literal_GeneralLiteral,
    sql_literal_Literal,
    GeneralLiteral,
    sql_literal_DatetimeLiteral,
    sql_literal_BooleanLiteral,
    sql_literal_NationalCharacterStringLiteral,
    Comment,
    sql_common_BracketedComment,
    sql_common_SimpleComment,
    Separator,
    sql_common_Comment,
    sql_common_SchemaQualifiedName,
    sql_common_Statement,
    sql_Dummy,
    Statement,
    sql_common_Separator,
    sql_common_DirectSQLStatement,
    sql_common_SQLScript,
    sql_schema_TableReference,
    TableReference,
    sql_schema_ReferentialConstraint,
    sql_schema_UniqueConstraint,
    TableConstraint,
    sql_schema_TableColumnsConstraint,
    DatetimeValueFunction,
    schema_TableColumnsConstraint,
    DirectSQLStatement,
    sql_schema_SQLSchemaStatement,
    schema_ReferentialConstraint,
    sql_schema_ReferentialTableConstraint,
    schema_ColumnConstraint,
    sql_schema_ReferentialColumnConstraint,
    schema_UniqueConstraint,
    sql_schema_UniqueTableConstraint,
    sql_schema_UniqueColumnConstraint,
    SQLSchemaStatement,
    sql_schema_SQLSchemaDefinitionStatement,
    Column,
    sql_schema_DefaultOption,
    TableDefinition,
    sql_schema_TableContentsSource,
    schema_TableElement,
    DefaultOption,
    sql_schema_LiteralDefaultOption,
    sql_schema_DatetimeValueFunctionDefaultOption,
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
    ColumnConstraint,
    sql_schema_NotNullColumnConstraint,
    TableElement,
    sql_schema_Column,
    TableContentsSource,
    sql_schema_TableElementList,
    TableElementList,
    sql_schema_TableElement,
    ImplicitlyTypedValueSpecification,
    sql_expression_NullSpecification,
    sql_expression_ImplicitlyTypedValueSpecification,
    EObject,
    sql_schema_TableConstraint,
    sql_schema_ColumnConstraint,
    schema_SQLSchemaDefinitionStatement,
    sql_schema_TableDefinition,
    DatetimeType,
    sql_datatype_TimeType,
    sql_datatype_TimestampType,
    sql_datatype_DateType,
    sql_function_DatetimeValueFunction,
    sql_datatype_LargeObjectLength,
    NumericType,
    sql_datatype_ApproximateNumericType,
    sql_datatype_ExactNumericType,
    sql_datatype_NumericType,
    LargeObjectLength,
    ApproximateNumericTypeKind,
    CharacterStringTypeKind,
    BinaryLargeObjectStringTypeKind,
    CharLengthUnits,
    Multiplier,
    UniqueSpecificationKind,
    TableScope,
    DatetimeValueFunctionKind,
    NationalCharacterStringTypeKind,
    ExactNumericTypeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_booleantype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_BooleanType)


def test_sql_datatype_booleantype_constructor_exists():
    assert callable(sql_datatype_BooleanType.__init__)


def test_sql_datatype_booleantype_constructor_args():
    sig = inspect.signature(sql_datatype_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_datetimetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DatetimeType)


def test_sql_datatype_datetimetype_constructor_exists():
    assert callable(sql_datatype_DatetimeType.__init__)


def test_sql_datatype_datetimetype_constructor_args():
    sig = inspect.signature(sql_datatype_DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_binarylargeobjectstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_BinaryLargeObjectStringType)


def test_sql_datatype_binarylargeobjectstringtype_constructor_exists():
    assert callable(sql_datatype_BinaryLargeObjectStringType.__init__)


def test_sql_datatype_binarylargeobjectstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_BinaryLargeObjectStringType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_datatype_binarylargeobjectstringtype_has_kind():
    assert hasattr(sql_datatype_BinaryLargeObjectStringType, "kind")
    descriptor = None
    for klass in sql_datatype_BinaryLargeObjectStringType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_CharacterStringType)


def test_sql_datatype_characterstringtype_constructor_exists():
    assert callable(sql_datatype_CharacterStringType.__init__)


def test_sql_datatype_characterstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_datatype_characterstringtype_has_length():
    assert hasattr(sql_datatype_CharacterStringType, "length")
    descriptor = None
    for klass in sql_datatype_CharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_characterstringtype_has_kind():
    assert hasattr(sql_datatype_CharacterStringType, "kind")
    descriptor = None
    for klass in sql_datatype_CharacterStringType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_PredefinedType)


def test_sql_datatype_predefinedtype_constructor_exists():
    assert callable(sql_datatype_PredefinedType.__init__)


def test_sql_datatype_predefinedtype_constructor_args():
    sig = inspect.signature(sql_datatype_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DataType)


def test_sql_datatype_datatype_constructor_exists():
    assert callable(sql_datatype_DataType.__init__)


def test_sql_datatype_datatype_constructor_args():
    sig = inspect.signature(sql_datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_nationalcharacterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_NationalCharacterStringType)


def test_sql_datatype_nationalcharacterstringtype_constructor_exists():
    assert callable(sql_datatype_NationalCharacterStringType.__init__)


def test_sql_datatype_nationalcharacterstringtype_constructor_args():
    sig = inspect.signature(sql_datatype_NationalCharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_datatype_nationalcharacterstringtype_has_length():
    assert hasattr(sql_datatype_NationalCharacterStringType, "length")
    descriptor = None
    for klass in sql_datatype_NationalCharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_nationalcharacterstringtype_has_kind():
    assert hasattr(sql_datatype_NationalCharacterStringType, "kind")
    descriptor = None
    for klass in sql_datatype_NationalCharacterStringType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(DatetimeLiteral)


def test_datetimeliteral_constructor_exists():
    assert callable(DatetimeLiteral.__init__)


def test_datetimeliteral_constructor_args():
    sig = inspect.signature(DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_timestampliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_TimestampLiteral)


def test_sql_literal_timestampliteral_constructor_exists():
    assert callable(sql_literal_TimestampLiteral.__init__)


def test_sql_literal_timestampliteral_constructor_args():
    sig = inspect.signature(sql_literal_TimestampLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_timestampliteral_has_value():
    assert hasattr(sql_literal_TimestampLiteral, "value")
    descriptor = None
    for klass in sql_literal_TimestampLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_literal_timeliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_TimeLiteral)


def test_sql_literal_timeliteral_constructor_exists():
    assert callable(sql_literal_TimeLiteral.__init__)


def test_sql_literal_timeliteral_constructor_args():
    sig = inspect.signature(sql_literal_TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_timeliteral_has_value():
    assert hasattr(sql_literal_TimeLiteral, "value")
    descriptor = None
    for klass in sql_literal_TimeLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_literal_dateliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_DateLiteral)


def test_sql_literal_dateliteral_constructor_exists():
    assert callable(sql_literal_DateLiteral.__init__)


def test_sql_literal_dateliteral_constructor_args():
    sig = inspect.signature(sql_literal_DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_dateliteral_has_value():
    assert hasattr(sql_literal_DateLiteral, "value")
    descriptor = None
    for klass in sql_literal_DateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_approximatenumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_ApproximateNumericLiteral)


def test_sql_literal_approximatenumericliteral_constructor_exists():
    assert callable(sql_literal_ApproximateNumericLiteral.__init__)


def test_sql_literal_approximatenumericliteral_constructor_args():
    sig = inspect.signature(sql_literal_ApproximateNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_approximatenumericliteral_has_value():
    assert hasattr(sql_literal_ApproximateNumericLiteral, "value")
    descriptor = None
    for klass in sql_literal_ApproximateNumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_literal_exactnumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_ExactNumericLiteral)


def test_sql_literal_exactnumericliteral_constructor_exists():
    assert callable(sql_literal_ExactNumericLiteral.__init__)


def test_sql_literal_exactnumericliteral_constructor_args():
    sig = inspect.signature(sql_literal_ExactNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_exactnumericliteral_has_value():
    assert hasattr(sql_literal_ExactNumericLiteral, "value")
    descriptor = None
    for klass in sql_literal_ExactNumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_schemaqualifiedname_is_not_abstract():
    assert not inspect.isabstract(SchemaQualifiedName)


def test_schemaqualifiedname_constructor_exists():
    assert callable(SchemaQualifiedName.__init__)


def test_schemaqualifiedname_constructor_args():
    sig = inspect.signature(SchemaQualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_nationalcharacterstringliteral_is_not_abstract():
    assert not inspect.isabstract(NationalCharacterStringLiteral)


def test_nationalcharacterstringliteral_constructor_exists():
    assert callable(NationalCharacterStringLiteral.__init__)


def test_nationalcharacterstringliteral_constructor_args():
    sig = inspect.signature(NationalCharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_characterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_CharacterStringLiteral)


def test_sql_literal_characterstringliteral_constructor_exists():
    assert callable(sql_literal_CharacterStringLiteral.__init__)


def test_sql_literal_characterstringliteral_constructor_args():
    sig = inspect.signature(sql_literal_CharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_numericliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_NumericLiteral)


def test_sql_literal_numericliteral_constructor_exists():
    assert callable(sql_literal_NumericLiteral.__init__)


def test_sql_literal_numericliteral_constructor_args():
    sig = inspect.signature(sql_literal_NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_generalliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_GeneralLiteral)


def test_sql_literal_generalliteral_constructor_exists():
    assert callable(sql_literal_GeneralLiteral.__init__)


def test_sql_literal_generalliteral_constructor_args():
    sig = inspect.signature(sql_literal_GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_literal_is_not_abstract():
    assert not inspect.isabstract(sql_literal_Literal)


def test_sql_literal_literal_constructor_exists():
    assert callable(sql_literal_Literal.__init__)


def test_sql_literal_literal_constructor_args():
    sig = inspect.signature(sql_literal_Literal.__init__)
    params = list(sig.parameters.keys())



def test_generalliteral_is_not_abstract():
    assert not inspect.isabstract(GeneralLiteral)


def test_generalliteral_constructor_exists():
    assert callable(GeneralLiteral.__init__)


def test_generalliteral_constructor_args():
    sig = inspect.signature(GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_DatetimeLiteral)


def test_sql_literal_datetimeliteral_constructor_exists():
    assert callable(sql_literal_DatetimeLiteral.__init__)


def test_sql_literal_datetimeliteral_constructor_args():
    sig = inspect.signature(sql_literal_DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql_literal_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_BooleanLiteral)


def test_sql_literal_booleanliteral_constructor_exists():
    assert callable(sql_literal_BooleanLiteral.__init__)


def test_sql_literal_booleanliteral_constructor_args():
    sig = inspect.signature(sql_literal_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_literal_booleanliteral_has_value():
    assert hasattr(sql_literal_BooleanLiteral, "value")
    descriptor = None
    for klass in sql_literal_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_literal_nationalcharacterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql_literal_NationalCharacterStringLiteral)


def test_sql_literal_nationalcharacterstringliteral_constructor_exists():
    assert callable(sql_literal_NationalCharacterStringLiteral.__init__)


def test_sql_literal_nationalcharacterstringliteral_constructor_args():
    sig = inspect.signature(sql_literal_NationalCharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_sql_literal_nationalcharacterstringliteral_has_values():
    assert hasattr(sql_literal_NationalCharacterStringLiteral, "values")
    descriptor = None
    for klass in sql_literal_NationalCharacterStringLiteral.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_bracketedcomment_is_not_abstract():
    assert not inspect.isabstract(sql_common_BracketedComment)


def test_sql_common_bracketedcomment_constructor_exists():
    assert callable(sql_common_BracketedComment.__init__)


def test_sql_common_bracketedcomment_constructor_args():
    sig = inspect.signature(sql_common_BracketedComment.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_simplecomment_is_not_abstract():
    assert not inspect.isabstract(sql_common_SimpleComment)


def test_sql_common_simplecomment_constructor_exists():
    assert callable(sql_common_SimpleComment.__init__)


def test_sql_common_simplecomment_constructor_args():
    sig = inspect.signature(sql_common_SimpleComment.__init__)
    params = list(sig.parameters.keys())



def test_separator_is_not_abstract():
    assert not inspect.isabstract(Separator)


def test_separator_constructor_exists():
    assert callable(Separator.__init__)


def test_separator_constructor_args():
    sig = inspect.signature(Separator.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_comment_is_not_abstract():
    assert not inspect.isabstract(sql_common_Comment)


def test_sql_common_comment_constructor_exists():
    assert callable(sql_common_Comment.__init__)


def test_sql_common_comment_constructor_args():
    sig = inspect.signature(sql_common_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_common_comment_has_value():
    assert hasattr(sql_common_Comment, "value")
    descriptor = None
    for klass in sql_common_Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_common_schemaqualifiedname_is_not_abstract():
    assert not inspect.isabstract(sql_common_SchemaQualifiedName)


def test_sql_common_schemaqualifiedname_constructor_exists():
    assert callable(sql_common_SchemaQualifiedName.__init__)


def test_sql_common_schemaqualifiedname_constructor_args():
    sig = inspect.signature(sql_common_SchemaQualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "catalogName" in params, "Missing parameter 'catalogName'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql_common_schemaqualifiedname_has_schemaName():
    assert hasattr(sql_common_SchemaQualifiedName, "schemaName")
    descriptor = None
    for klass in sql_common_SchemaQualifiedName.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_sql_common_schemaqualifiedname_has_catalogName():
    assert hasattr(sql_common_SchemaQualifiedName, "catalogName")
    descriptor = None
    for klass in sql_common_SchemaQualifiedName.__mro__:
        if "catalogName" in klass.__dict__:
            descriptor = klass.__dict__["catalogName"]
            break
    assert isinstance(descriptor, property)

def test_sql_common_schemaqualifiedname_has_name():
    assert hasattr(sql_common_SchemaQualifiedName, "name")
    descriptor = None
    for klass in sql_common_SchemaQualifiedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_common_statement_is_not_abstract():
    assert not inspect.isabstract(sql_common_Statement)


def test_sql_common_statement_constructor_exists():
    assert callable(sql_common_Statement.__init__)


def test_sql_common_statement_constructor_args():
    sig = inspect.signature(sql_common_Statement.__init__)
    params = list(sig.parameters.keys())



def test_sql_dummy_is_not_abstract():
    assert not inspect.isabstract(sql_Dummy)


def test_sql_dummy_constructor_exists():
    assert callable(sql_Dummy.__init__)


def test_sql_dummy_constructor_args():
    sig = inspect.signature(sql_Dummy.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_separator_is_not_abstract():
    assert not inspect.isabstract(sql_common_Separator)


def test_sql_common_separator_constructor_exists():
    assert callable(sql_common_Separator.__init__)


def test_sql_common_separator_constructor_args():
    sig = inspect.signature(sql_common_Separator.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(sql_common_DirectSQLStatement)


def test_sql_common_directsqlstatement_constructor_exists():
    assert callable(sql_common_DirectSQLStatement.__init__)


def test_sql_common_directsqlstatement_constructor_args():
    sig = inspect.signature(sql_common_DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql_common_sqlscript_is_not_abstract():
    assert not inspect.isabstract(sql_common_SQLScript)


def test_sql_common_sqlscript_constructor_exists():
    assert callable(sql_common_SQLScript.__init__)


def test_sql_common_sqlscript_constructor_args():
    sig = inspect.signature(sql_common_SQLScript.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tablereference_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableReference)


def test_sql_schema_tablereference_constructor_exists():
    assert callable(sql_schema_TableReference.__init__)


def test_sql_schema_tablereference_constructor_args():
    sig = inspect.signature(sql_schema_TableReference.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "catalogName" in params, "Missing parameter 'catalogName'"

def test_sql_schema_tablereference_has_schemaName():
    assert hasattr(sql_schema_TableReference, "schemaName")
    descriptor = None
    for klass in sql_schema_TableReference.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_sql_schema_tablereference_has_catalogName():
    assert hasattr(sql_schema_TableReference, "catalogName")
    descriptor = None
    for klass in sql_schema_TableReference.__mro__:
        if "catalogName" in klass.__dict__:
            descriptor = klass.__dict__["catalogName"]
            break
    assert isinstance(descriptor, property)



def test_tablereference_is_not_abstract():
    assert not inspect.isabstract(TableReference)


def test_tablereference_constructor_exists():
    assert callable(TableReference.__init__)


def test_tablereference_constructor_args():
    sig = inspect.signature(TableReference.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialConstraint)


def test_sql_schema_referentialconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialConstraint.__init__)


def test_sql_schema_referentialconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueConstraint)


def test_sql_schema_uniqueconstraint_constructor_exists():
    assert callable(sql_schema_UniqueConstraint.__init__)


def test_sql_schema_uniqueconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_schema_uniqueconstraint_has_kind():
    assert hasattr(sql_schema_UniqueConstraint, "kind")
    descriptor = None
    for klass in sql_schema_UniqueConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableColumnsConstraint)


def test_sql_schema_tablecolumnsconstraint_constructor_exists():
    assert callable(sql_schema_TableColumnsConstraint.__init__)


def test_sql_schema_tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(sql_schema_TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(DatetimeValueFunction)


def test_datetimevaluefunction_constructor_exists():
    assert callable(DatetimeValueFunction.__init__)


def test_datetimevaluefunction_constructor_args():
    sig = inspect.signature(DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_schema_tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_TableColumnsConstraint)


def test_schema_tablecolumnsconstraint_constructor_exists():
    assert callable(schema_TableColumnsConstraint.__init__)


def test_schema_tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(schema_TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(DirectSQLStatement)


def test_directsqlstatement_constructor_exists():
    assert callable(DirectSQLStatement.__init__)


def test_directsqlstatement_constructor_args():
    sig = inspect.signature(DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_SQLSchemaStatement)


def test_sql_schema_sqlschemastatement_constructor_exists():
    assert callable(sql_schema_SQLSchemaStatement.__init__)


def test_sql_schema_sqlschemastatement_constructor_args():
    sig = inspect.signature(sql_schema_SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_schema_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_ReferentialConstraint)


def test_schema_referentialconstraint_constructor_exists():
    assert callable(schema_ReferentialConstraint.__init__)


def test_schema_referentialconstraint_constructor_args():
    sig = inspect.signature(schema_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_referentialtableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialTableConstraint)


def test_sql_schema_referentialtableconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialTableConstraint.__init__)


def test_sql_schema_referentialtableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_ColumnConstraint)


def test_schema_columnconstraint_constructor_exists():
    assert callable(schema_ColumnConstraint.__init__)


def test_schema_columnconstraint_constructor_args():
    sig = inspect.signature(schema_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_referentialcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ReferentialColumnConstraint)


def test_sql_schema_referentialcolumnconstraint_constructor_exists():
    assert callable(sql_schema_ReferentialColumnConstraint.__init__)


def test_sql_schema_referentialcolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ReferentialColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(schema_UniqueConstraint)


def test_schema_uniqueconstraint_constructor_exists():
    assert callable(schema_UniqueConstraint.__init__)


def test_schema_uniqueconstraint_constructor_args():
    sig = inspect.signature(schema_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueTableConstraint)


def test_sql_schema_uniquetableconstraint_constructor_exists():
    assert callable(sql_schema_UniqueTableConstraint.__init__)


def test_sql_schema_uniquetableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_uniquecolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_UniqueColumnConstraint)


def test_sql_schema_uniquecolumnconstraint_constructor_exists():
    assert callable(sql_schema_UniqueColumnConstraint.__init__)


def test_sql_schema_uniquecolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_UniqueColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(SQLSchemaStatement)


def test_sqlschemastatement_constructor_exists():
    assert callable(SQLSchemaStatement.__init__)


def test_sqlschemastatement_constructor_args():
    sig = inspect.signature(SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_SQLSchemaDefinitionStatement)


def test_sql_schema_sqlschemadefinitionstatement_constructor_exists():
    assert callable(sql_schema_SQLSchemaDefinitionStatement.__init__)


def test_sql_schema_sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(sql_schema_SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_defaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_DefaultOption)


def test_sql_schema_defaultoption_constructor_exists():
    assert callable(sql_schema_DefaultOption.__init__)


def test_sql_schema_defaultoption_constructor_args():
    sig = inspect.signature(sql_schema_DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(TableDefinition)


def test_tabledefinition_constructor_exists():
    assert callable(TableDefinition.__init__)


def test_tabledefinition_constructor_args():
    sig = inspect.signature(TableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tablecontentssource_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableContentsSource)


def test_sql_schema_tablecontentssource_constructor_exists():
    assert callable(sql_schema_TableContentsSource.__init__)


def test_sql_schema_tablecontentssource_constructor_args():
    sig = inspect.signature(sql_schema_TableContentsSource.__init__)
    params = list(sig.parameters.keys())



def test_schema_tableelement_is_not_abstract():
    assert not inspect.isabstract(schema_TableElement)


def test_schema_tableelement_constructor_exists():
    assert callable(schema_TableElement.__init__)


def test_schema_tableelement_constructor_args():
    sig = inspect.signature(schema_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultoption_is_not_abstract():
    assert not inspect.isabstract(DefaultOption)


def test_defaultoption_constructor_exists():
    assert callable(DefaultOption.__init__)


def test_defaultoption_constructor_args():
    sig = inspect.signature(DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_literaldefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_LiteralDefaultOption)


def test_sql_schema_literaldefaultoption_constructor_exists():
    assert callable(sql_schema_LiteralDefaultOption.__init__)


def test_sql_schema_literaldefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_LiteralDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_datetimevaluefunctiondefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_DatetimeValueFunctionDefaultOption)


def test_sql_schema_datetimevaluefunctiondefaultoption_constructor_exists():
    assert callable(sql_schema_DatetimeValueFunctionDefaultOption.__init__)


def test_sql_schema_datetimevaluefunctiondefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_DatetimeValueFunctionDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_implicitlytypedvaluespecificationdefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)


def test_sql_schema_implicitlytypedvaluespecificationdefaultoption_constructor_exists():
    assert callable(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption.__init__)


def test_sql_schema_implicitlytypedvaluespecificationdefaultoption_constructor_args():
    sig = inspect.signature(sql_schema_ImplicitlyTypedValueSpecificationDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_notnullcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_NotNullColumnConstraint)


def test_sql_schema_notnullcolumnconstraint_constructor_exists():
    assert callable(sql_schema_NotNullColumnConstraint.__init__)


def test_sql_schema_notnullcolumnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_NotNullColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_column_is_not_abstract():
    assert not inspect.isabstract(sql_schema_Column)


def test_sql_schema_column_constructor_exists():
    assert callable(sql_schema_Column.__init__)


def test_sql_schema_column_constructor_args():
    sig = inspect.signature(sql_schema_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_schema_column_has_name():
    assert hasattr(sql_schema_Column, "name")
    descriptor = None
    for klass in sql_schema_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tablecontentssource_is_not_abstract():
    assert not inspect.isabstract(TableContentsSource)


def test_tablecontentssource_constructor_exists():
    assert callable(TableContentsSource.__init__)


def test_tablecontentssource_constructor_args():
    sig = inspect.signature(TableContentsSource.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tableelementlist_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableElementList)


def test_sql_schema_tableelementlist_constructor_exists():
    assert callable(sql_schema_TableElementList.__init__)


def test_sql_schema_tableelementlist_constructor_args():
    sig = inspect.signature(sql_schema_TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_tableelementlist_is_not_abstract():
    assert not inspect.isabstract(TableElementList)


def test_tableelementlist_constructor_exists():
    assert callable(TableElementList.__init__)


def test_tableelementlist_constructor_args():
    sig = inspect.signature(TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tableelement_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableElement)


def test_sql_schema_tableelement_constructor_exists():
    assert callable(sql_schema_TableElement.__init__)


def test_sql_schema_tableelement_constructor_args():
    sig = inspect.signature(sql_schema_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(ImplicitlyTypedValueSpecification)


def test_implicitlytypedvaluespecification_constructor_exists():
    assert callable(ImplicitlyTypedValueSpecification.__init__)


def test_implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_nullspecification_is_not_abstract():
    assert not inspect.isabstract(sql_expression_NullSpecification)


def test_sql_expression_nullspecification_constructor_exists():
    assert callable(sql_expression_NullSpecification.__init__)


def test_sql_expression_nullspecification_constructor_args():
    sig = inspect.signature(sql_expression_NullSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ImplicitlyTypedValueSpecification)


def test_sql_expression_implicitlytypedvaluespecification_constructor_exists():
    assert callable(sql_expression_ImplicitlyTypedValueSpecification.__init__)


def test_sql_expression_implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(sql_expression_ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableConstraint)


def test_sql_schema_tableconstraint_constructor_exists():
    assert callable(sql_schema_TableConstraint.__init__)


def test_sql_schema_tableconstraint_constructor_args():
    sig = inspect.signature(sql_schema_TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql_schema_ColumnConstraint)


def test_sql_schema_columnconstraint_constructor_exists():
    assert callable(sql_schema_ColumnConstraint.__init__)


def test_sql_schema_columnconstraint_constructor_args():
    sig = inspect.signature(sql_schema_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema_sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(schema_SQLSchemaDefinitionStatement)


def test_schema_sqlschemadefinitionstatement_constructor_exists():
    assert callable(schema_SQLSchemaDefinitionStatement.__init__)


def test_schema_sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(schema_SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(sql_schema_TableDefinition)


def test_sql_schema_tabledefinition_constructor_exists():
    assert callable(sql_schema_TableDefinition.__init__)


def test_sql_schema_tabledefinition_constructor_args():
    sig = inspect.signature(sql_schema_TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "label" in params, "Missing parameter 'label'"

def test_sql_schema_tabledefinition_has_scope():
    assert hasattr(sql_schema_TableDefinition, "scope")
    descriptor = None
    for klass in sql_schema_TableDefinition.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_sql_schema_tabledefinition_has_label():
    assert hasattr(sql_schema_TableDefinition, "label")
    descriptor = None
    for klass in sql_schema_TableDefinition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatetimeType)


def test_datetimetype_constructor_exists():
    assert callable(DatetimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_timetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_TimeType)


def test_sql_datatype_timetype_constructor_exists():
    assert callable(sql_datatype_TimeType.__init__)


def test_sql_datatype_timetype_constructor_args():
    sig = inspect.signature(sql_datatype_TimeType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"

def test_sql_datatype_timetype_has_precision():
    assert hasattr(sql_datatype_TimeType, "precision")
    descriptor = None
    for klass in sql_datatype_TimeType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_timetype_has_withTimeZone():
    assert hasattr(sql_datatype_TimeType, "withTimeZone")
    descriptor = None
    for klass in sql_datatype_TimeType.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_timestamptype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_TimestampType)


def test_sql_datatype_timestamptype_constructor_exists():
    assert callable(sql_datatype_TimestampType.__init__)


def test_sql_datatype_timestamptype_constructor_args():
    sig = inspect.signature(sql_datatype_TimestampType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"

def test_sql_datatype_timestamptype_has_precision():
    assert hasattr(sql_datatype_TimestampType, "precision")
    descriptor = None
    for klass in sql_datatype_TimestampType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_timestamptype_has_withTimeZone():
    assert hasattr(sql_datatype_TimestampType, "withTimeZone")
    descriptor = None
    for klass in sql_datatype_TimestampType.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_datetype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_DateType)


def test_sql_datatype_datetype_constructor_exists():
    assert callable(sql_datatype_DateType.__init__)


def test_sql_datatype_datetype_constructor_args():
    sig = inspect.signature(sql_datatype_DateType.__init__)
    params = list(sig.parameters.keys())



def test_sql_function_datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(sql_function_DatetimeValueFunction)


def test_sql_function_datetimevaluefunction_constructor_exists():
    assert callable(sql_function_DatetimeValueFunction.__init__)


def test_sql_function_datetimevaluefunction_constructor_args():
    sig = inspect.signature(sql_function_DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_function_datetimevaluefunction_has_precision():
    assert hasattr(sql_function_DatetimeValueFunction, "precision")
    descriptor = None
    for klass in sql_function_DatetimeValueFunction.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql_function_datetimevaluefunction_has_kind():
    assert hasattr(sql_function_DatetimeValueFunction, "kind")
    descriptor = None
    for klass in sql_function_DatetimeValueFunction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_LargeObjectLength)


def test_sql_datatype_largeobjectlength_constructor_exists():
    assert callable(sql_datatype_LargeObjectLength.__init__)


def test_sql_datatype_largeobjectlength_constructor_args():
    sig = inspect.signature(sql_datatype_LargeObjectLength.__init__)
    params = list(sig.parameters.keys())
    assert "multiplier" in params, "Missing parameter 'multiplier'"
    assert "value" in params, "Missing parameter 'value'"
    assert "units" in params, "Missing parameter 'units'"

def test_sql_datatype_largeobjectlength_has_multiplier():
    assert hasattr(sql_datatype_LargeObjectLength, "multiplier")
    descriptor = None
    for klass in sql_datatype_LargeObjectLength.__mro__:
        if "multiplier" in klass.__dict__:
            descriptor = klass.__dict__["multiplier"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_largeobjectlength_has_value():
    assert hasattr(sql_datatype_LargeObjectLength, "value")
    descriptor = None
    for klass in sql_datatype_LargeObjectLength.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_largeobjectlength_has_units():
    assert hasattr(sql_datatype_LargeObjectLength, "units")
    descriptor = None
    for klass in sql_datatype_LargeObjectLength.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_sql_datatype_approximatenumerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_ApproximateNumericType)


def test_sql_datatype_approximatenumerictype_constructor_exists():
    assert callable(sql_datatype_ApproximateNumericType.__init__)


def test_sql_datatype_approximatenumerictype_constructor_args():
    sig = inspect.signature(sql_datatype_ApproximateNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_sql_datatype_approximatenumerictype_has_kind():
    assert hasattr(sql_datatype_ApproximateNumericType, "kind")
    descriptor = None
    for klass in sql_datatype_ApproximateNumericType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_approximatenumerictype_has_precision():
    assert hasattr(sql_datatype_ApproximateNumericType, "precision")
    descriptor = None
    for klass in sql_datatype_ApproximateNumericType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_exactnumerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_ExactNumericType)


def test_sql_datatype_exactnumerictype_constructor_exists():
    assert callable(sql_datatype_ExactNumericType.__init__)


def test_sql_datatype_exactnumerictype_constructor_args():
    sig = inspect.signature(sql_datatype_ExactNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql_datatype_exactnumerictype_has_scale():
    assert hasattr(sql_datatype_ExactNumericType, "scale")
    descriptor = None
    for klass in sql_datatype_ExactNumericType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_exactnumerictype_has_precision():
    assert hasattr(sql_datatype_ExactNumericType, "precision")
    descriptor = None
    for klass in sql_datatype_ExactNumericType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql_datatype_exactnumerictype_has_kind():
    assert hasattr(sql_datatype_ExactNumericType, "kind")
    descriptor = None
    for klass in sql_datatype_ExactNumericType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sql_datatype_numerictype_is_not_abstract():
    assert not inspect.isabstract(sql_datatype_NumericType)


def test_sql_datatype_numerictype_constructor_exists():
    assert callable(sql_datatype_NumericType.__init__)


def test_sql_datatype_numerictype_constructor_args():
    sig = inspect.signature(sql_datatype_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(LargeObjectLength)


def test_largeobjectlength_constructor_exists():
    assert callable(LargeObjectLength.__init__)


def test_largeobjectlength_constructor_args():
    sig = inspect.signature(LargeObjectLength.__init__)
    params = list(sig.parameters.keys())

def test_approximatenumerictypekind_exists():
    # Check that the Enumeration exists
    assert ApproximateNumericTypeKind is not None

def test_approximatenumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ApproximateNumericTypeKind]
    expected_literals = [
        "FLOAT",
        "REAL",
        "DOUBLE_PRECISION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ApproximateNumericTypeKind"

def test_characterstringtypekind_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypeKind is not None

def test_characterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypeKind]
    expected_literals = [
        "VARCHAR",
        "CHAR_VARYING",
        "CHAR",
        "CHARACTER_VARYING",
        "CHARACTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypeKind"

def test_binarylargeobjectstringtypekind_exists():
    # Check that the Enumeration exists
    assert BinaryLargeObjectStringTypeKind is not None

def test_binarylargeobjectstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryLargeObjectStringTypeKind]
    expected_literals = [
        "BLOB",
        "BINARY_LARGE_OBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryLargeObjectStringTypeKind"

def test_charlengthunits_exists():
    # Check that the Enumeration exists
    assert CharLengthUnits is not None

def test_charlengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharLengthUnits]
    expected_literals = [
        "OCTETS",
        "CHARACTERS",
        "CODE_UNITS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharLengthUnits"

def test_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "M",
        "G",
        "K",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_uniquespecificationkind_exists():
    # Check that the Enumeration exists
    assert UniqueSpecificationKind is not None

def test_uniquespecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UniqueSpecificationKind]
    expected_literals = [
        "UNIQUE",
        "PRIMARY_KEY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UniqueSpecificationKind"

def test_tablescope_exists():
    # Check that the Enumeration exists
    assert TableScope is not None

def test_tablescope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableScope]
    expected_literals = [
        "PERSISTENT",
        "LOCAL_TEMPORARY",
        "GLOBAL_TEMPORARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableScope"

def test_datetimevaluefunctionkind_exists():
    # Check that the Enumeration exists
    assert DatetimeValueFunctionKind is not None

def test_datetimevaluefunctionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeValueFunctionKind]
    expected_literals = [
        "CURRENT_TIMESTAMP",
        "CURRENT_DATE",
        "LOCALTIME",
        "CURRENT_TIME",
        "LOCALTIMESTAMP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeValueFunctionKind"

def test_nationalcharacterstringtypekind_exists():
    # Check that the Enumeration exists
    assert NationalCharacterStringTypeKind is not None

def test_nationalcharacterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NationalCharacterStringTypeKind]
    expected_literals = [
        "NATIONAL_CHARACTER",
        "NATIONAL_CHAR_VARYING",
        "NCHAR_VARYING",
        "NATIONAL_CHARACTER_VARYING",
        "NATIONAL_CHAR",
        "NCHAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NationalCharacterStringTypeKind"

def test_exactnumerictypekind_exists():
    # Check that the Enumeration exists
    assert ExactNumericTypeKind is not None

def test_exactnumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExactNumericTypeKind]
    expected_literals = [
        "BIGINT",
        "SMALLINT",
        "DECIMAL",
        "INTEGER",
        "NUMERIC",
        "INT",
        "DEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExactNumericTypeKind"


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
PredefinedType_strategy = st.builds(
    PredefinedType,
)
sql_datatype_BooleanType_strategy = st.builds(
    sql_datatype_BooleanType,
)
sql_datatype_DatetimeType_strategy = st.builds(
    sql_datatype_DatetimeType,
)
sql_datatype_BinaryLargeObjectStringType_strategy = st.builds(
    sql_datatype_BinaryLargeObjectStringType,
    kind=
        safe_text
)
sql_datatype_CharacterStringType_strategy = st.builds(
    sql_datatype_CharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
sql_datatype_PredefinedType_strategy = st.builds(
    sql_datatype_PredefinedType,
)
sql_datatype_DataType_strategy = st.builds(
    sql_datatype_DataType,
)
sql_datatype_NationalCharacterStringType_strategy = st.builds(
    sql_datatype_NationalCharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
DatetimeLiteral_strategy = st.builds(
    DatetimeLiteral,
)
sql_literal_TimestampLiteral_strategy = st.builds(
    sql_literal_TimestampLiteral,
    value=
        safe_text
)
sql_literal_TimeLiteral_strategy = st.builds(
    sql_literal_TimeLiteral,
    value=
        safe_text
)
sql_literal_DateLiteral_strategy = st.builds(
    sql_literal_DateLiteral,
    value=
        safe_text
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
sql_literal_ApproximateNumericLiteral_strategy = st.builds(
    sql_literal_ApproximateNumericLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sql_literal_ExactNumericLiteral_strategy = st.builds(
    sql_literal_ExactNumericLiteral,
    value=
        safe_text
)
SchemaQualifiedName_strategy = st.builds(
    SchemaQualifiedName,
)
NationalCharacterStringLiteral_strategy = st.builds(
    NationalCharacterStringLiteral,
)
sql_literal_CharacterStringLiteral_strategy = st.builds(
    sql_literal_CharacterStringLiteral,
)
Literal_strategy = st.builds(
    Literal,
)
sql_literal_NumericLiteral_strategy = st.builds(
    sql_literal_NumericLiteral,
)
sql_literal_GeneralLiteral_strategy = st.builds(
    sql_literal_GeneralLiteral,
)
sql_literal_Literal_strategy = st.builds(
    sql_literal_Literal,
)
GeneralLiteral_strategy = st.builds(
    GeneralLiteral,
)
sql_literal_DatetimeLiteral_strategy = st.builds(
    sql_literal_DatetimeLiteral,
)
sql_literal_BooleanLiteral_strategy = st.builds(
    sql_literal_BooleanLiteral,
    value=
        safe_text
)
sql_literal_NationalCharacterStringLiteral_strategy = st.builds(
    sql_literal_NationalCharacterStringLiteral,
    values=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
sql_common_BracketedComment_strategy = st.builds(
    sql_common_BracketedComment,
)
sql_common_SimpleComment_strategy = st.builds(
    sql_common_SimpleComment,
)
Separator_strategy = st.builds(
    Separator,
)
sql_common_Comment_strategy = st.builds(
    sql_common_Comment,
    value=
        safe_text
)
sql_common_SchemaQualifiedName_strategy = st.builds(
    sql_common_SchemaQualifiedName,
    schemaName=
        safe_text,
    catalogName=
        safe_text,
    name=
        safe_text
)
sql_common_Statement_strategy = st.builds(
    sql_common_Statement,
)
sql_Dummy_strategy = st.builds(
    sql_Dummy,
)
Statement_strategy = st.builds(
    Statement,
)
sql_common_Separator_strategy = st.builds(
    sql_common_Separator,
)
sql_common_DirectSQLStatement_strategy = st.builds(
    sql_common_DirectSQLStatement,
)
sql_common_SQLScript_strategy = st.builds(
    sql_common_SQLScript,
)
sql_schema_TableReference_strategy = st.builds(
    sql_schema_TableReference,
    schemaName=
        safe_text,
    catalogName=
        safe_text
)
TableReference_strategy = st.builds(
    TableReference,
)
sql_schema_ReferentialConstraint_strategy = st.builds(
    sql_schema_ReferentialConstraint,
)
sql_schema_UniqueConstraint_strategy = st.builds(
    sql_schema_UniqueConstraint,
    kind=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sql_schema_TableColumnsConstraint_strategy = st.builds(
    sql_schema_TableColumnsConstraint,
)
DatetimeValueFunction_strategy = st.builds(
    DatetimeValueFunction,
)
schema_TableColumnsConstraint_strategy = st.builds(
    schema_TableColumnsConstraint,
)
DirectSQLStatement_strategy = st.builds(
    DirectSQLStatement,
)
sql_schema_SQLSchemaStatement_strategy = st.builds(
    sql_schema_SQLSchemaStatement,
)
schema_ReferentialConstraint_strategy = st.builds(
    schema_ReferentialConstraint,
)
sql_schema_ReferentialTableConstraint_strategy = st.builds(
    sql_schema_ReferentialTableConstraint,
)
schema_ColumnConstraint_strategy = st.builds(
    schema_ColumnConstraint,
)
sql_schema_ReferentialColumnConstraint_strategy = st.builds(
    sql_schema_ReferentialColumnConstraint,
)
schema_UniqueConstraint_strategy = st.builds(
    schema_UniqueConstraint,
)
sql_schema_UniqueTableConstraint_strategy = st.builds(
    sql_schema_UniqueTableConstraint,
)
sql_schema_UniqueColumnConstraint_strategy = st.builds(
    sql_schema_UniqueColumnConstraint,
)
SQLSchemaStatement_strategy = st.builds(
    SQLSchemaStatement,
)
sql_schema_SQLSchemaDefinitionStatement_strategy = st.builds(
    sql_schema_SQLSchemaDefinitionStatement,
)
Column_strategy = st.builds(
    Column,
)
sql_schema_DefaultOption_strategy = st.builds(
    sql_schema_DefaultOption,
)
TableDefinition_strategy = st.builds(
    TableDefinition,
)
sql_schema_TableContentsSource_strategy = st.builds(
    sql_schema_TableContentsSource,
)
schema_TableElement_strategy = st.builds(
    schema_TableElement,
)
DefaultOption_strategy = st.builds(
    DefaultOption,
)
sql_schema_LiteralDefaultOption_strategy = st.builds(
    sql_schema_LiteralDefaultOption,
)
sql_schema_DatetimeValueFunctionDefaultOption_strategy = st.builds(
    sql_schema_DatetimeValueFunctionDefaultOption,
)
sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_strategy = st.builds(
    sql_schema_ImplicitlyTypedValueSpecificationDefaultOption,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
sql_schema_NotNullColumnConstraint_strategy = st.builds(
    sql_schema_NotNullColumnConstraint,
)
TableElement_strategy = st.builds(
    TableElement,
)
sql_schema_Column_strategy = st.builds(
    sql_schema_Column,
    name=
        safe_text
)
TableContentsSource_strategy = st.builds(
    TableContentsSource,
)
sql_schema_TableElementList_strategy = st.builds(
    sql_schema_TableElementList,
)
TableElementList_strategy = st.builds(
    TableElementList,
)
sql_schema_TableElement_strategy = st.builds(
    sql_schema_TableElement,
)
ImplicitlyTypedValueSpecification_strategy = st.builds(
    ImplicitlyTypedValueSpecification,
)
sql_expression_NullSpecification_strategy = st.builds(
    sql_expression_NullSpecification,
)
sql_expression_ImplicitlyTypedValueSpecification_strategy = st.builds(
    sql_expression_ImplicitlyTypedValueSpecification,
)
EObject_strategy = st.builds(
    EObject,
)
sql_schema_TableConstraint_strategy = st.builds(
    sql_schema_TableConstraint,
)
sql_schema_ColumnConstraint_strategy = st.builds(
    sql_schema_ColumnConstraint,
)
schema_SQLSchemaDefinitionStatement_strategy = st.builds(
    schema_SQLSchemaDefinitionStatement,
)
sql_schema_TableDefinition_strategy = st.builds(
    sql_schema_TableDefinition,
    scope=
        safe_text,
    label=
        safe_text
)
DatetimeType_strategy = st.builds(
    DatetimeType,
)
sql_datatype_TimeType_strategy = st.builds(
    sql_datatype_TimeType,
    precision=
        safe_text,
    withTimeZone=
        safe_text
)
sql_datatype_TimestampType_strategy = st.builds(
    sql_datatype_TimestampType,
    precision=
        safe_text,
    withTimeZone=
        safe_text
)
sql_datatype_DateType_strategy = st.builds(
    sql_datatype_DateType,
)
sql_function_DatetimeValueFunction_strategy = st.builds(
    sql_function_DatetimeValueFunction,
    precision=
        safe_text,
    kind=
        safe_text
)
sql_datatype_LargeObjectLength_strategy = st.builds(
    sql_datatype_LargeObjectLength,
    multiplier=
        safe_text,
    value=
        safe_text,
    units=
        safe_text
)
NumericType_strategy = st.builds(
    NumericType,
)
sql_datatype_ApproximateNumericType_strategy = st.builds(
    sql_datatype_ApproximateNumericType,
    kind=
        safe_text,
    precision=
        safe_text
)
sql_datatype_ExactNumericType_strategy = st.builds(
    sql_datatype_ExactNumericType,
    scale=
        safe_text,
    precision=
        safe_text,
    kind=
        safe_text
)
sql_datatype_NumericType_strategy = st.builds(
    sql_datatype_NumericType,
)
LargeObjectLength_strategy = st.builds(
    LargeObjectLength,
)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=sql_datatype_BooleanType_strategy)
@settings(max_examples=50)
def test_sql_datatype_booleantype_instantiation(instance):
    assert isinstance(instance, sql_datatype_BooleanType)

@given(instance=sql_datatype_DatetimeType_strategy)
@settings(max_examples=50)
def test_sql_datatype_datetimetype_instantiation(instance):
    assert isinstance(instance, sql_datatype_DatetimeType)

@given(instance=sql_datatype_BinaryLargeObjectStringType_strategy)
@settings(max_examples=50)
def test_sql_datatype_binarylargeobjectstringtype_instantiation(instance):
    assert isinstance(instance, sql_datatype_BinaryLargeObjectStringType)



@given(instance=sql_datatype_BinaryLargeObjectStringType_strategy)
def test_sql_datatype_binarylargeobjectstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql_datatype_CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql_datatype_characterstringtype_instantiation(instance):
    assert isinstance(instance, sql_datatype_CharacterStringType)



@given(instance=sql_datatype_CharacterStringType_strategy)
def test_sql_datatype_characterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sql_datatype_CharacterStringType_strategy)
def test_sql_datatype_characterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sql_datatype_PredefinedType_strategy)
@settings(max_examples=50)
def test_sql_datatype_predefinedtype_instantiation(instance):
    assert isinstance(instance, sql_datatype_PredefinedType)

@given(instance=sql_datatype_DataType_strategy)
@settings(max_examples=50)
def test_sql_datatype_datatype_instantiation(instance):
    assert isinstance(instance, sql_datatype_DataType)

@given(instance=sql_datatype_NationalCharacterStringType_strategy)
@settings(max_examples=50)
def test_sql_datatype_nationalcharacterstringtype_instantiation(instance):
    assert isinstance(instance, sql_datatype_NationalCharacterStringType)



@given(instance=sql_datatype_NationalCharacterStringType_strategy)
def test_sql_datatype_nationalcharacterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sql_datatype_NationalCharacterStringType_strategy)
def test_sql_datatype_nationalcharacterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=DatetimeLiteral_strategy)
@settings(max_examples=50)
def test_datetimeliteral_instantiation(instance):
    assert isinstance(instance, DatetimeLiteral)

@given(instance=sql_literal_TimestampLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_timestampliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_TimestampLiteral)



@given(instance=sql_literal_TimestampLiteral_strategy)
def test_sql_literal_timestampliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_literal_TimeLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_timeliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_TimeLiteral)



@given(instance=sql_literal_TimeLiteral_strategy)
def test_sql_literal_timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_literal_DateLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_dateliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_DateLiteral)



@given(instance=sql_literal_DateLiteral_strategy)
def test_sql_literal_dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=sql_literal_ApproximateNumericLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_approximatenumericliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_ApproximateNumericLiteral)



@given(instance=sql_literal_ApproximateNumericLiteral_strategy)
def test_sql_literal_approximatenumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_literal_ExactNumericLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_exactnumericliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_ExactNumericLiteral)



@given(instance=sql_literal_ExactNumericLiteral_strategy)
def test_sql_literal_exactnumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SchemaQualifiedName_strategy)
@settings(max_examples=50)
def test_schemaqualifiedname_instantiation(instance):
    assert isinstance(instance, SchemaQualifiedName)

@given(instance=NationalCharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_nationalcharacterstringliteral_instantiation(instance):
    assert isinstance(instance, NationalCharacterStringLiteral)

@given(instance=sql_literal_CharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_characterstringliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_CharacterStringLiteral)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=sql_literal_NumericLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_numericliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_NumericLiteral)

@given(instance=sql_literal_GeneralLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_generalliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_GeneralLiteral)

@given(instance=sql_literal_Literal_strategy)
@settings(max_examples=50)
def test_sql_literal_literal_instantiation(instance):
    assert isinstance(instance, sql_literal_Literal)

@given(instance=GeneralLiteral_strategy)
@settings(max_examples=50)
def test_generalliteral_instantiation(instance):
    assert isinstance(instance, GeneralLiteral)

@given(instance=sql_literal_DatetimeLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_datetimeliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_DatetimeLiteral)

@given(instance=sql_literal_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_booleanliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_BooleanLiteral)



@given(instance=sql_literal_BooleanLiteral_strategy)
def test_sql_literal_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_literal_NationalCharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_sql_literal_nationalcharacterstringliteral_instantiation(instance):
    assert isinstance(instance, sql_literal_NationalCharacterStringLiteral)



@given(instance=sql_literal_NationalCharacterStringLiteral_strategy)
def test_sql_literal_nationalcharacterstringliteral_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=sql_common_BracketedComment_strategy)
@settings(max_examples=50)
def test_sql_common_bracketedcomment_instantiation(instance):
    assert isinstance(instance, sql_common_BracketedComment)

@given(instance=sql_common_SimpleComment_strategy)
@settings(max_examples=50)
def test_sql_common_simplecomment_instantiation(instance):
    assert isinstance(instance, sql_common_SimpleComment)

@given(instance=Separator_strategy)
@settings(max_examples=50)
def test_separator_instantiation(instance):
    assert isinstance(instance, Separator)

@given(instance=sql_common_Comment_strategy)
@settings(max_examples=50)
def test_sql_common_comment_instantiation(instance):
    assert isinstance(instance, sql_common_Comment)



@given(instance=sql_common_Comment_strategy)
def test_sql_common_comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_common_SchemaQualifiedName_strategy)
@settings(max_examples=50)
def test_sql_common_schemaqualifiedname_instantiation(instance):
    assert isinstance(instance, sql_common_SchemaQualifiedName)



@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_sql_common_schemaqualifiedname_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_sql_common_schemaqualifiedname_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original



@given(instance=sql_common_SchemaQualifiedName_strategy)
def test_sql_common_schemaqualifiedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql_common_Statement_strategy)
@settings(max_examples=50)
def test_sql_common_statement_instantiation(instance):
    assert isinstance(instance, sql_common_Statement)

@given(instance=sql_Dummy_strategy)
@settings(max_examples=50)
def test_sql_dummy_instantiation(instance):
    assert isinstance(instance, sql_Dummy)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sql_common_Separator_strategy)
@settings(max_examples=50)
def test_sql_common_separator_instantiation(instance):
    assert isinstance(instance, sql_common_Separator)

@given(instance=sql_common_DirectSQLStatement_strategy)
@settings(max_examples=50)
def test_sql_common_directsqlstatement_instantiation(instance):
    assert isinstance(instance, sql_common_DirectSQLStatement)

@given(instance=sql_common_SQLScript_strategy)
@settings(max_examples=50)
def test_sql_common_sqlscript_instantiation(instance):
    assert isinstance(instance, sql_common_SQLScript)

@given(instance=sql_schema_TableReference_strategy)
@settings(max_examples=50)
def test_sql_schema_tablereference_instantiation(instance):
    assert isinstance(instance, sql_schema_TableReference)



@given(instance=sql_schema_TableReference_strategy)
def test_sql_schema_tablereference_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=sql_schema_TableReference_strategy)
def test_sql_schema_tablereference_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original

@given(instance=TableReference_strategy)
@settings(max_examples=50)
def test_tablereference_instantiation(instance):
    assert isinstance(instance, TableReference)

@given(instance=sql_schema_ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_referentialconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialConstraint)

@given(instance=sql_schema_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueConstraint)



@given(instance=sql_schema_UniqueConstraint_strategy)
def test_sql_schema_uniqueconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sql_schema_TableColumnsConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_tablecolumnsconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_TableColumnsConstraint)

@given(instance=DatetimeValueFunction_strategy)
@settings(max_examples=50)
def test_datetimevaluefunction_instantiation(instance):
    assert isinstance(instance, DatetimeValueFunction)

@given(instance=schema_TableColumnsConstraint_strategy)
@settings(max_examples=50)
def test_schema_tablecolumnsconstraint_instantiation(instance):
    assert isinstance(instance, schema_TableColumnsConstraint)

@given(instance=DirectSQLStatement_strategy)
@settings(max_examples=50)
def test_directsqlstatement_instantiation(instance):
    assert isinstance(instance, DirectSQLStatement)

@given(instance=sql_schema_SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sql_schema_sqlschemastatement_instantiation(instance):
    assert isinstance(instance, sql_schema_SQLSchemaStatement)

@given(instance=schema_ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_schema_referentialconstraint_instantiation(instance):
    assert isinstance(instance, schema_ReferentialConstraint)

@given(instance=sql_schema_ReferentialTableConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_referentialtableconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialTableConstraint)

@given(instance=schema_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_schema_columnconstraint_instantiation(instance):
    assert isinstance(instance, schema_ColumnConstraint)

@given(instance=sql_schema_ReferentialColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_referentialcolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ReferentialColumnConstraint)

@given(instance=schema_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_schema_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, schema_UniqueConstraint)

@given(instance=sql_schema_UniqueTableConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_uniquetableconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueTableConstraint)

@given(instance=sql_schema_UniqueColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_uniquecolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_UniqueColumnConstraint)

@given(instance=SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sqlschemastatement_instantiation(instance):
    assert isinstance(instance, SQLSchemaStatement)

@given(instance=sql_schema_SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=50)
def test_sql_schema_sqlschemadefinitionstatement_instantiation(instance):
    assert isinstance(instance, sql_schema_SQLSchemaDefinitionStatement)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=sql_schema_DefaultOption_strategy)
@settings(max_examples=50)
def test_sql_schema_defaultoption_instantiation(instance):
    assert isinstance(instance, sql_schema_DefaultOption)

@given(instance=TableDefinition_strategy)
@settings(max_examples=50)
def test_tabledefinition_instantiation(instance):
    assert isinstance(instance, TableDefinition)

@given(instance=sql_schema_TableContentsSource_strategy)
@settings(max_examples=50)
def test_sql_schema_tablecontentssource_instantiation(instance):
    assert isinstance(instance, sql_schema_TableContentsSource)

@given(instance=schema_TableElement_strategy)
@settings(max_examples=50)
def test_schema_tableelement_instantiation(instance):
    assert isinstance(instance, schema_TableElement)

@given(instance=DefaultOption_strategy)
@settings(max_examples=50)
def test_defaultoption_instantiation(instance):
    assert isinstance(instance, DefaultOption)

@given(instance=sql_schema_LiteralDefaultOption_strategy)
@settings(max_examples=50)
def test_sql_schema_literaldefaultoption_instantiation(instance):
    assert isinstance(instance, sql_schema_LiteralDefaultOption)

@given(instance=sql_schema_DatetimeValueFunctionDefaultOption_strategy)
@settings(max_examples=50)
def test_sql_schema_datetimevaluefunctiondefaultoption_instantiation(instance):
    assert isinstance(instance, sql_schema_DatetimeValueFunctionDefaultOption)

@given(instance=sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_strategy)
@settings(max_examples=50)
def test_sql_schema_implicitlytypedvaluespecificationdefaultoption_instantiation(instance):
    assert isinstance(instance, sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=sql_schema_NotNullColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_notnullcolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_NotNullColumnConstraint)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=sql_schema_Column_strategy)
@settings(max_examples=50)
def test_sql_schema_column_instantiation(instance):
    assert isinstance(instance, sql_schema_Column)



@given(instance=sql_schema_Column_strategy)
def test_sql_schema_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TableContentsSource_strategy)
@settings(max_examples=50)
def test_tablecontentssource_instantiation(instance):
    assert isinstance(instance, TableContentsSource)

@given(instance=sql_schema_TableElementList_strategy)
@settings(max_examples=50)
def test_sql_schema_tableelementlist_instantiation(instance):
    assert isinstance(instance, sql_schema_TableElementList)

@given(instance=TableElementList_strategy)
@settings(max_examples=50)
def test_tableelementlist_instantiation(instance):
    assert isinstance(instance, TableElementList)

@given(instance=sql_schema_TableElement_strategy)
@settings(max_examples=50)
def test_sql_schema_tableelement_instantiation(instance):
    assert isinstance(instance, sql_schema_TableElement)

@given(instance=ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=50)
def test_implicitlytypedvaluespecification_instantiation(instance):
    assert isinstance(instance, ImplicitlyTypedValueSpecification)

@given(instance=sql_expression_NullSpecification_strategy)
@settings(max_examples=50)
def test_sql_expression_nullspecification_instantiation(instance):
    assert isinstance(instance, sql_expression_NullSpecification)

@given(instance=sql_expression_ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=50)
def test_sql_expression_implicitlytypedvaluespecification_instantiation(instance):
    assert isinstance(instance, sql_expression_ImplicitlyTypedValueSpecification)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=sql_schema_TableConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_tableconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_TableConstraint)

@given(instance=sql_schema_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql_schema_columnconstraint_instantiation(instance):
    assert isinstance(instance, sql_schema_ColumnConstraint)

@given(instance=schema_SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=50)
def test_schema_sqlschemadefinitionstatement_instantiation(instance):
    assert isinstance(instance, schema_SQLSchemaDefinitionStatement)

@given(instance=sql_schema_TableDefinition_strategy)
@settings(max_examples=50)
def test_sql_schema_tabledefinition_instantiation(instance):
    assert isinstance(instance, sql_schema_TableDefinition)



@given(instance=sql_schema_TableDefinition_strategy)
def test_sql_schema_tabledefinition_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=sql_schema_TableDefinition_strategy)
def test_sql_schema_tabledefinition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=DatetimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DatetimeType)

@given(instance=sql_datatype_TimeType_strategy)
@settings(max_examples=50)
def test_sql_datatype_timetype_instantiation(instance):
    assert isinstance(instance, sql_datatype_TimeType)



@given(instance=sql_datatype_TimeType_strategy)
def test_sql_datatype_timetype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_TimeType_strategy)
def test_sql_datatype_timetype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original

@given(instance=sql_datatype_TimestampType_strategy)
@settings(max_examples=50)
def test_sql_datatype_timestamptype_instantiation(instance):
    assert isinstance(instance, sql_datatype_TimestampType)



@given(instance=sql_datatype_TimestampType_strategy)
def test_sql_datatype_timestamptype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_TimestampType_strategy)
def test_sql_datatype_timestamptype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original

@given(instance=sql_datatype_DateType_strategy)
@settings(max_examples=50)
def test_sql_datatype_datetype_instantiation(instance):
    assert isinstance(instance, sql_datatype_DateType)

@given(instance=sql_function_DatetimeValueFunction_strategy)
@settings(max_examples=50)
def test_sql_function_datetimevaluefunction_instantiation(instance):
    assert isinstance(instance, sql_function_DatetimeValueFunction)



@given(instance=sql_function_DatetimeValueFunction_strategy)
def test_sql_function_datetimevaluefunction_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_function_DatetimeValueFunction_strategy)
def test_sql_function_datetimevaluefunction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql_datatype_LargeObjectLength_strategy)
@settings(max_examples=50)
def test_sql_datatype_largeobjectlength_instantiation(instance):
    assert isinstance(instance, sql_datatype_LargeObjectLength)



@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_sql_datatype_largeobjectlength_multiplier_setter(instance):
    original = instance.multiplier
    instance.multiplier = original
    assert instance.multiplier == original



@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_sql_datatype_largeobjectlength_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=sql_datatype_LargeObjectLength_strategy)
def test_sql_datatype_largeobjectlength_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=sql_datatype_ApproximateNumericType_strategy)
@settings(max_examples=50)
def test_sql_datatype_approximatenumerictype_instantiation(instance):
    assert isinstance(instance, sql_datatype_ApproximateNumericType)



@given(instance=sql_datatype_ApproximateNumericType_strategy)
def test_sql_datatype_approximatenumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=sql_datatype_ApproximateNumericType_strategy)
def test_sql_datatype_approximatenumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sql_datatype_ExactNumericType_strategy)
@settings(max_examples=50)
def test_sql_datatype_exactnumerictype_instantiation(instance):
    assert isinstance(instance, sql_datatype_ExactNumericType)



@given(instance=sql_datatype_ExactNumericType_strategy)
def test_sql_datatype_exactnumerictype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=sql_datatype_ExactNumericType_strategy)
def test_sql_datatype_exactnumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=sql_datatype_ExactNumericType_strategy)
def test_sql_datatype_exactnumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql_datatype_NumericType_strategy)
@settings(max_examples=50)
def test_sql_datatype_numerictype_instantiation(instance):
    assert isinstance(instance, sql_datatype_NumericType)

@given(instance=LargeObjectLength_strategy)
@settings(max_examples=50)
def test_largeobjectlength_instantiation(instance):
    assert isinstance(instance, LargeObjectLength)
