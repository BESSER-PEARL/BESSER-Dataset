import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TableConstraint,
    sql::schema::TableColumnsConstraint,
    schema::TableColumnsConstraint,
    DatetimeValueFunction,
    SQLSchemaStatement,
    sql::schema::SQLSchemaDefinitionStatement,
    DirectSQLStatement,
    sql::schema::SQLSchemaStatement,
    schema::ReferentialConstraint,
    sql::schema::ReferentialTableConstraint,
    schema::ColumnConstraint,
    sql::schema::ReferentialColumnConstraint,
    schema::UniqueConstraint,
    sql::schema::UniqueTableConstraint,
    sql::schema::UniqueColumnConstraint,
    sql::schema::TableReference,
    TableReference,
    sql::schema::ReferentialConstraint,
    sql::schema::UniqueConstraint,
    schema::TableElement,
    ColumnConstraint,
    sql::schema::NotNullColumnConstraint,
    DefaultOption,
    sql::schema::ImplicitlyTypedValueSpecificationDefaultOption,
    sql::schema::LiteralDefaultOption,
    sql::schema::DatetimeValueFunctionDefaultOption,
    TableElementList,
    sql::schema::TableElement,
    TableElement,
    sql::schema::Column,
    TableContentsSource,
    sql::schema::TableElementList,
    EObject,
    sql::schema::TableConstraint,
    schema::SQLSchemaDefinitionStatement,
    sql::schema::TableDefinition,
    sql::schema::ColumnConstraint,
    Column,
    sql::schema::DefaultOption,
    TableDefinition,
    sql::schema::TableContentsSource,
    DatetimeType,
    sql::datatype::TimestampType,
    sql::datatype::TimeType,
    sql::datatype::DateType,
    sql::datatype::LargeObjectLength,
    NumericType,
    sql::datatype::ApproximateNumericType,
    sql::datatype::ExactNumericType,
    ImplicitlyTypedValueSpecification,
    sql::expression::NullSpecification,
    sql::expression::ImplicitlyTypedValueSpecification,
    sql::function::DatetimeValueFunction,
    LargeObjectLength,
    PredefinedType,
    sql::datatype::BooleanType,
    sql::datatype::BinaryLargeObjectStringType,
    sql::datatype::DatetimeType,
    sql::datatype::NumericType,
    sql::datatype::NationalCharacterStringType,
    sql::datatype::CharacterStringType,
    DataType,
    sql::datatype::PredefinedType,
    sql::datatype::DataType,
    DatetimeLiteral,
    sql::literal::DateLiteral,
    GeneralLiteral,
    sql::literal::DatetimeLiteral,
    sql::literal::BooleanLiteral,
    sql::literal::NationalCharacterStringLiteral,
    SchemaQualifiedName,
    NationalCharacterStringLiteral,
    sql::literal::CharacterStringLiteral,
    Literal,
    sql::literal::GeneralLiteral,
    sql::literal::Literal,
    sql::common::SchemaQualifiedName,
    sql::common::Statement,
    Comment,
    sql::common::BracketedComment,
    sql::common::SimpleComment,
    Separator,
    sql::common::Comment,
    sql::literal::NumericLiteral,
    NumericLiteral,
    sql::literal::ApproximateNumericLiteral,
    sql::literal::ExactNumericLiteral,
    sql::literal::TimestampLiteral,
    sql::literal::TimeLiteral,
    sql::Dummy,
    Statement,
    sql::common::DirectSQLStatement,
    sql::common::Separator,
    sql::common::SQLScript,
    NationalCharacterStringTypeKind,
    UniqueSpecificationKind,
    Multiplier,
    DatetimeValueFunctionKind,
    CharLengthUnits,
    BinaryLargeObjectStringTypeKind,
    TableScope,
    ExactNumericTypeKind,
    CharacterStringTypeKind,
    ApproximateNumericTypeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableColumnsConstraint)


def test_sql::schema::tablecolumnsconstraint_constructor_exists():
    assert callable(sql::schema::TableColumnsConstraint.__init__)


def test_sql::schema::tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(sql::schema::TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema::tablecolumnsconstraint_is_not_abstract():
    assert not inspect.isabstract(schema::TableColumnsConstraint)


def test_schema::tablecolumnsconstraint_constructor_exists():
    assert callable(schema::TableColumnsConstraint.__init__)


def test_schema::tablecolumnsconstraint_constructor_args():
    sig = inspect.signature(schema::TableColumnsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(DatetimeValueFunction)


def test_datetimevaluefunction_constructor_exists():
    assert callable(DatetimeValueFunction.__init__)


def test_datetimevaluefunction_constructor_args():
    sig = inspect.signature(DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(SQLSchemaStatement)


def test_sqlschemastatement_constructor_exists():
    assert callable(SQLSchemaStatement.__init__)


def test_sqlschemastatement_constructor_args():
    sig = inspect.signature(SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(sql::schema::SQLSchemaDefinitionStatement)


def test_sql::schema::sqlschemadefinitionstatement_constructor_exists():
    assert callable(sql::schema::SQLSchemaDefinitionStatement.__init__)


def test_sql::schema::sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(sql::schema::SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(DirectSQLStatement)


def test_directsqlstatement_constructor_exists():
    assert callable(DirectSQLStatement.__init__)


def test_directsqlstatement_constructor_args():
    sig = inspect.signature(DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(sql::schema::SQLSchemaStatement)


def test_sql::schema::sqlschemastatement_constructor_exists():
    assert callable(sql::schema::SQLSchemaStatement.__init__)


def test_sql::schema::sqlschemastatement_constructor_args():
    sig = inspect.signature(sql::schema::SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_schema::referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(schema::ReferentialConstraint)


def test_schema::referentialconstraint_constructor_exists():
    assert callable(schema::ReferentialConstraint.__init__)


def test_schema::referentialconstraint_constructor_args():
    sig = inspect.signature(schema::ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::referentialtableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::ReferentialTableConstraint)


def test_sql::schema::referentialtableconstraint_constructor_exists():
    assert callable(sql::schema::ReferentialTableConstraint.__init__)


def test_sql::schema::referentialtableconstraint_constructor_args():
    sig = inspect.signature(sql::schema::ReferentialTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema::columnconstraint_is_not_abstract():
    assert not inspect.isabstract(schema::ColumnConstraint)


def test_schema::columnconstraint_constructor_exists():
    assert callable(schema::ColumnConstraint.__init__)


def test_schema::columnconstraint_constructor_args():
    sig = inspect.signature(schema::ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::referentialcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::ReferentialColumnConstraint)


def test_sql::schema::referentialcolumnconstraint_constructor_exists():
    assert callable(sql::schema::ReferentialColumnConstraint.__init__)


def test_sql::schema::referentialcolumnconstraint_constructor_args():
    sig = inspect.signature(sql::schema::ReferentialColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(schema::UniqueConstraint)


def test_schema::uniqueconstraint_constructor_exists():
    assert callable(schema::UniqueConstraint.__init__)


def test_schema::uniqueconstraint_constructor_args():
    sig = inspect.signature(schema::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::UniqueTableConstraint)


def test_sql::schema::uniquetableconstraint_constructor_exists():
    assert callable(sql::schema::UniqueTableConstraint.__init__)


def test_sql::schema::uniquetableconstraint_constructor_args():
    sig = inspect.signature(sql::schema::UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::uniquecolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::UniqueColumnConstraint)


def test_sql::schema::uniquecolumnconstraint_constructor_exists():
    assert callable(sql::schema::UniqueColumnConstraint.__init__)


def test_sql::schema::uniquecolumnconstraint_constructor_args():
    sig = inspect.signature(sql::schema::UniqueColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tablereference_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableReference)


def test_sql::schema::tablereference_constructor_exists():
    assert callable(sql::schema::TableReference.__init__)


def test_sql::schema::tablereference_constructor_args():
    sig = inspect.signature(sql::schema::TableReference.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "catalogName" in params, "Missing parameter 'catalogName'"

def test_sql::schema::tablereference_has_schemaName():
    assert hasattr(sql::schema::TableReference, "schemaName")
    descriptor = None
    for klass in sql::schema::TableReference.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_sql::schema::tablereference_has_catalogName():
    assert hasattr(sql::schema::TableReference, "catalogName")
    descriptor = None
    for klass in sql::schema::TableReference.__mro__:
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



def test_sql::schema::referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::ReferentialConstraint)


def test_sql::schema::referentialconstraint_constructor_exists():
    assert callable(sql::schema::ReferentialConstraint.__init__)


def test_sql::schema::referentialconstraint_constructor_args():
    sig = inspect.signature(sql::schema::ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::UniqueConstraint)


def test_sql::schema::uniqueconstraint_constructor_exists():
    assert callable(sql::schema::UniqueConstraint.__init__)


def test_sql::schema::uniqueconstraint_constructor_args():
    sig = inspect.signature(sql::schema::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql::schema::uniqueconstraint_has_kind():
    assert hasattr(sql::schema::UniqueConstraint, "kind")
    descriptor = None
    for klass in sql::schema::UniqueConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_schema::tableelement_is_not_abstract():
    assert not inspect.isabstract(schema::TableElement)


def test_schema::tableelement_constructor_exists():
    assert callable(schema::TableElement.__init__)


def test_schema::tableelement_constructor_args():
    sig = inspect.signature(schema::TableElement.__init__)
    params = list(sig.parameters.keys())



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::notnullcolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::NotNullColumnConstraint)


def test_sql::schema::notnullcolumnconstraint_constructor_exists():
    assert callable(sql::schema::NotNullColumnConstraint.__init__)


def test_sql::schema::notnullcolumnconstraint_constructor_args():
    sig = inspect.signature(sql::schema::NotNullColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_defaultoption_is_not_abstract():
    assert not inspect.isabstract(DefaultOption)


def test_defaultoption_constructor_exists():
    assert callable(DefaultOption.__init__)


def test_defaultoption_constructor_args():
    sig = inspect.signature(DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::implicitlytypedvaluespecificationdefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql::schema::ImplicitlyTypedValueSpecificationDefaultOption)


def test_sql::schema::implicitlytypedvaluespecificationdefaultoption_constructor_exists():
    assert callable(sql::schema::ImplicitlyTypedValueSpecificationDefaultOption.__init__)


def test_sql::schema::implicitlytypedvaluespecificationdefaultoption_constructor_args():
    sig = inspect.signature(sql::schema::ImplicitlyTypedValueSpecificationDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::literaldefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql::schema::LiteralDefaultOption)


def test_sql::schema::literaldefaultoption_constructor_exists():
    assert callable(sql::schema::LiteralDefaultOption.__init__)


def test_sql::schema::literaldefaultoption_constructor_args():
    sig = inspect.signature(sql::schema::LiteralDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::datetimevaluefunctiondefaultoption_is_not_abstract():
    assert not inspect.isabstract(sql::schema::DatetimeValueFunctionDefaultOption)


def test_sql::schema::datetimevaluefunctiondefaultoption_constructor_exists():
    assert callable(sql::schema::DatetimeValueFunctionDefaultOption.__init__)


def test_sql::schema::datetimevaluefunctiondefaultoption_constructor_args():
    sig = inspect.signature(sql::schema::DatetimeValueFunctionDefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_tableelementlist_is_not_abstract():
    assert not inspect.isabstract(TableElementList)


def test_tableelementlist_constructor_exists():
    assert callable(TableElementList.__init__)


def test_tableelementlist_constructor_args():
    sig = inspect.signature(TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tableelement_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableElement)


def test_sql::schema::tableelement_constructor_exists():
    assert callable(sql::schema::TableElement.__init__)


def test_sql::schema::tableelement_constructor_args():
    sig = inspect.signature(sql::schema::TableElement.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::column_is_not_abstract():
    assert not inspect.isabstract(sql::schema::Column)


def test_sql::schema::column_constructor_exists():
    assert callable(sql::schema::Column.__init__)


def test_sql::schema::column_constructor_args():
    sig = inspect.signature(sql::schema::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::schema::column_has_name():
    assert hasattr(sql::schema::Column, "name")
    descriptor = None
    for klass in sql::schema::Column.__mro__:
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



def test_sql::schema::tableelementlist_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableElementList)


def test_sql::schema::tableelementlist_constructor_exists():
    assert callable(sql::schema::TableElementList.__init__)


def test_sql::schema::tableelementlist_constructor_args():
    sig = inspect.signature(sql::schema::TableElementList.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableConstraint)


def test_sql::schema::tableconstraint_constructor_exists():
    assert callable(sql::schema::TableConstraint.__init__)


def test_sql::schema::tableconstraint_constructor_args():
    sig = inspect.signature(sql::schema::TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_schema::sqlschemadefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(schema::SQLSchemaDefinitionStatement)


def test_schema::sqlschemadefinitionstatement_constructor_exists():
    assert callable(schema::SQLSchemaDefinitionStatement.__init__)


def test_schema::sqlschemadefinitionstatement_constructor_args():
    sig = inspect.signature(schema::SQLSchemaDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tabledefinition_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableDefinition)


def test_sql::schema::tabledefinition_constructor_exists():
    assert callable(sql::schema::TableDefinition.__init__)


def test_sql::schema::tabledefinition_constructor_args():
    sig = inspect.signature(sql::schema::TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "label" in params, "Missing parameter 'label'"

def test_sql::schema::tabledefinition_has_scope():
    assert hasattr(sql::schema::TableDefinition, "scope")
    descriptor = None
    for klass in sql::schema::TableDefinition.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_sql::schema::tabledefinition_has_label():
    assert hasattr(sql::schema::TableDefinition, "label")
    descriptor = None
    for klass in sql::schema::TableDefinition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_sql::schema::columnconstraint_is_not_abstract():
    assert not inspect.isabstract(sql::schema::ColumnConstraint)


def test_sql::schema::columnconstraint_constructor_exists():
    assert callable(sql::schema::ColumnConstraint.__init__)


def test_sql::schema::columnconstraint_constructor_args():
    sig = inspect.signature(sql::schema::ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::defaultoption_is_not_abstract():
    assert not inspect.isabstract(sql::schema::DefaultOption)


def test_sql::schema::defaultoption_constructor_exists():
    assert callable(sql::schema::DefaultOption.__init__)


def test_sql::schema::defaultoption_constructor_args():
    sig = inspect.signature(sql::schema::DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(TableDefinition)


def test_tabledefinition_constructor_exists():
    assert callable(TableDefinition.__init__)


def test_tabledefinition_constructor_args():
    sig = inspect.signature(TableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema::tablecontentssource_is_not_abstract():
    assert not inspect.isabstract(sql::schema::TableContentsSource)


def test_sql::schema::tablecontentssource_constructor_exists():
    assert callable(sql::schema::TableContentsSource.__init__)


def test_sql::schema::tablecontentssource_constructor_args():
    sig = inspect.signature(sql::schema::TableContentsSource.__init__)
    params = list(sig.parameters.keys())



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatetimeType)


def test_datetimetype_constructor_exists():
    assert callable(DatetimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::timestamptype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::TimestampType)


def test_sql::datatype::timestamptype_constructor_exists():
    assert callable(sql::datatype::TimestampType.__init__)


def test_sql::datatype::timestamptype_constructor_args():
    sig = inspect.signature(sql::datatype::TimestampType.__init__)
    params = list(sig.parameters.keys())
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_sql::datatype::timestamptype_has_withTimeZone():
    assert hasattr(sql::datatype::TimestampType, "withTimeZone")
    descriptor = None
    for klass in sql::datatype::TimestampType.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::timestamptype_has_precision():
    assert hasattr(sql::datatype::TimestampType, "precision")
    descriptor = None
    for klass in sql::datatype::TimestampType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_sql::datatype::timetype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::TimeType)


def test_sql::datatype::timetype_constructor_exists():
    assert callable(sql::datatype::TimeType.__init__)


def test_sql::datatype::timetype_constructor_args():
    sig = inspect.signature(sql::datatype::TimeType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "withTimeZone" in params, "Missing parameter 'withTimeZone'"

def test_sql::datatype::timetype_has_precision():
    assert hasattr(sql::datatype::TimeType, "precision")
    descriptor = None
    for klass in sql::datatype::TimeType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::timetype_has_withTimeZone():
    assert hasattr(sql::datatype::TimeType, "withTimeZone")
    descriptor = None
    for klass in sql::datatype::TimeType.__mro__:
        if "withTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["withTimeZone"]
            break
    assert isinstance(descriptor, property)



def test_sql::datatype::datetype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::DateType)


def test_sql::datatype::datetype_constructor_exists():
    assert callable(sql::datatype::DateType.__init__)


def test_sql::datatype::datetype_constructor_args():
    sig = inspect.signature(sql::datatype::DateType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::LargeObjectLength)


def test_sql::datatype::largeobjectlength_constructor_exists():
    assert callable(sql::datatype::LargeObjectLength.__init__)


def test_sql::datatype::largeobjectlength_constructor_args():
    sig = inspect.signature(sql::datatype::LargeObjectLength.__init__)
    params = list(sig.parameters.keys())
    assert "multiplier" in params, "Missing parameter 'multiplier'"
    assert "value" in params, "Missing parameter 'value'"
    assert "units" in params, "Missing parameter 'units'"

def test_sql::datatype::largeobjectlength_has_multiplier():
    assert hasattr(sql::datatype::LargeObjectLength, "multiplier")
    descriptor = None
    for klass in sql::datatype::LargeObjectLength.__mro__:
        if "multiplier" in klass.__dict__:
            descriptor = klass.__dict__["multiplier"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::largeobjectlength_has_value():
    assert hasattr(sql::datatype::LargeObjectLength, "value")
    descriptor = None
    for klass in sql::datatype::LargeObjectLength.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::largeobjectlength_has_units():
    assert hasattr(sql::datatype::LargeObjectLength, "units")
    descriptor = None
    for klass in sql::datatype::LargeObjectLength.__mro__:
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



def test_sql::datatype::approximatenumerictype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::ApproximateNumericType)


def test_sql::datatype::approximatenumerictype_constructor_exists():
    assert callable(sql::datatype::ApproximateNumericType.__init__)


def test_sql::datatype::approximatenumerictype_constructor_args():
    sig = inspect.signature(sql::datatype::ApproximateNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_sql::datatype::approximatenumerictype_has_kind():
    assert hasattr(sql::datatype::ApproximateNumericType, "kind")
    descriptor = None
    for klass in sql::datatype::ApproximateNumericType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::approximatenumerictype_has_precision():
    assert hasattr(sql::datatype::ApproximateNumericType, "precision")
    descriptor = None
    for klass in sql::datatype::ApproximateNumericType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_sql::datatype::exactnumerictype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::ExactNumericType)


def test_sql::datatype::exactnumerictype_constructor_exists():
    assert callable(sql::datatype::ExactNumericType.__init__)


def test_sql::datatype::exactnumerictype_constructor_args():
    sig = inspect.signature(sql::datatype::ExactNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql::datatype::exactnumerictype_has_precision():
    assert hasattr(sql::datatype::ExactNumericType, "precision")
    descriptor = None
    for klass in sql::datatype::ExactNumericType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::exactnumerictype_has_scale():
    assert hasattr(sql::datatype::ExactNumericType, "scale")
    descriptor = None
    for klass in sql::datatype::ExactNumericType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::exactnumerictype_has_kind():
    assert hasattr(sql::datatype::ExactNumericType, "kind")
    descriptor = None
    for klass in sql::datatype::ExactNumericType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(ImplicitlyTypedValueSpecification)


def test_implicitlytypedvaluespecification_constructor_exists():
    assert callable(ImplicitlyTypedValueSpecification.__init__)


def test_implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::nullspecification_is_not_abstract():
    assert not inspect.isabstract(sql::expression::NullSpecification)


def test_sql::expression::nullspecification_constructor_exists():
    assert callable(sql::expression::NullSpecification.__init__)


def test_sql::expression::nullspecification_constructor_args():
    sig = inspect.signature(sql::expression::NullSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::implicitlytypedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(sql::expression::ImplicitlyTypedValueSpecification)


def test_sql::expression::implicitlytypedvaluespecification_constructor_exists():
    assert callable(sql::expression::ImplicitlyTypedValueSpecification.__init__)


def test_sql::expression::implicitlytypedvaluespecification_constructor_args():
    sig = inspect.signature(sql::expression::ImplicitlyTypedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_sql::function::datetimevaluefunction_is_not_abstract():
    assert not inspect.isabstract(sql::function::DatetimeValueFunction)


def test_sql::function::datetimevaluefunction_constructor_exists():
    assert callable(sql::function::DatetimeValueFunction.__init__)


def test_sql::function::datetimevaluefunction_constructor_args():
    sig = inspect.signature(sql::function::DatetimeValueFunction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_sql::function::datetimevaluefunction_has_kind():
    assert hasattr(sql::function::DatetimeValueFunction, "kind")
    descriptor = None
    for klass in sql::function::DatetimeValueFunction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sql::function::datetimevaluefunction_has_precision():
    assert hasattr(sql::function::DatetimeValueFunction, "precision")
    descriptor = None
    for klass in sql::function::DatetimeValueFunction.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_largeobjectlength_is_not_abstract():
    assert not inspect.isabstract(LargeObjectLength)


def test_largeobjectlength_constructor_exists():
    assert callable(LargeObjectLength.__init__)


def test_largeobjectlength_constructor_args():
    sig = inspect.signature(LargeObjectLength.__init__)
    params = list(sig.parameters.keys())



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::booleantype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::BooleanType)


def test_sql::datatype::booleantype_constructor_exists():
    assert callable(sql::datatype::BooleanType.__init__)


def test_sql::datatype::booleantype_constructor_args():
    sig = inspect.signature(sql::datatype::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::binarylargeobjectstringtype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::BinaryLargeObjectStringType)


def test_sql::datatype::binarylargeobjectstringtype_constructor_exists():
    assert callable(sql::datatype::BinaryLargeObjectStringType.__init__)


def test_sql::datatype::binarylargeobjectstringtype_constructor_args():
    sig = inspect.signature(sql::datatype::BinaryLargeObjectStringType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql::datatype::binarylargeobjectstringtype_has_kind():
    assert hasattr(sql::datatype::BinaryLargeObjectStringType, "kind")
    descriptor = None
    for klass in sql::datatype::BinaryLargeObjectStringType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sql::datatype::datetimetype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::DatetimeType)


def test_sql::datatype::datetimetype_constructor_exists():
    assert callable(sql::datatype::DatetimeType.__init__)


def test_sql::datatype::datetimetype_constructor_args():
    sig = inspect.signature(sql::datatype::DatetimeType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::numerictype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::NumericType)


def test_sql::datatype::numerictype_constructor_exists():
    assert callable(sql::datatype::NumericType.__init__)


def test_sql::datatype::numerictype_constructor_args():
    sig = inspect.signature(sql::datatype::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::nationalcharacterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::NationalCharacterStringType)


def test_sql::datatype::nationalcharacterstringtype_constructor_exists():
    assert callable(sql::datatype::NationalCharacterStringType.__init__)


def test_sql::datatype::nationalcharacterstringtype_constructor_args():
    sig = inspect.signature(sql::datatype::NationalCharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql::datatype::nationalcharacterstringtype_has_length():
    assert hasattr(sql::datatype::NationalCharacterStringType, "length")
    descriptor = None
    for klass in sql::datatype::NationalCharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::nationalcharacterstringtype_has_kind():
    assert hasattr(sql::datatype::NationalCharacterStringType, "kind")
    descriptor = None
    for klass in sql::datatype::NationalCharacterStringType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sql::datatype::characterstringtype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::CharacterStringType)


def test_sql::datatype::characterstringtype_constructor_exists():
    assert callable(sql::datatype::CharacterStringType.__init__)


def test_sql::datatype::characterstringtype_constructor_args():
    sig = inspect.signature(sql::datatype::CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_sql::datatype::characterstringtype_has_length():
    assert hasattr(sql::datatype::CharacterStringType, "length")
    descriptor = None
    for klass in sql::datatype::CharacterStringType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sql::datatype::characterstringtype_has_kind():
    assert hasattr(sql::datatype::CharacterStringType, "kind")
    descriptor = None
    for klass in sql::datatype::CharacterStringType.__mro__:
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



def test_sql::datatype::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::PredefinedType)


def test_sql::datatype::predefinedtype_constructor_exists():
    assert callable(sql::datatype::PredefinedType.__init__)


def test_sql::datatype::predefinedtype_constructor_args():
    sig = inspect.signature(sql::datatype::PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql::datatype::datatype_is_not_abstract():
    assert not inspect.isabstract(sql::datatype::DataType)


def test_sql::datatype::datatype_constructor_exists():
    assert callable(sql::datatype::DataType.__init__)


def test_sql::datatype::datatype_constructor_args():
    sig = inspect.signature(sql::datatype::DataType.__init__)
    params = list(sig.parameters.keys())



def test_datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(DatetimeLiteral)


def test_datetimeliteral_constructor_exists():
    assert callable(DatetimeLiteral.__init__)


def test_datetimeliteral_constructor_args():
    sig = inspect.signature(DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::dateliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::DateLiteral)


def test_sql::literal::dateliteral_constructor_exists():
    assert callable(sql::literal::DateLiteral.__init__)


def test_sql::literal::dateliteral_constructor_args():
    sig = inspect.signature(sql::literal::DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::dateliteral_has_value():
    assert hasattr(sql::literal::DateLiteral, "value")
    descriptor = None
    for klass in sql::literal::DateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_generalliteral_is_not_abstract():
    assert not inspect.isabstract(GeneralLiteral)


def test_generalliteral_constructor_exists():
    assert callable(GeneralLiteral.__init__)


def test_generalliteral_constructor_args():
    sig = inspect.signature(GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::datetimeliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::DatetimeLiteral)


def test_sql::literal::datetimeliteral_constructor_exists():
    assert callable(sql::literal::DatetimeLiteral.__init__)


def test_sql::literal::datetimeliteral_constructor_args():
    sig = inspect.signature(sql::literal::DatetimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::BooleanLiteral)


def test_sql::literal::booleanliteral_constructor_exists():
    assert callable(sql::literal::BooleanLiteral.__init__)


def test_sql::literal::booleanliteral_constructor_args():
    sig = inspect.signature(sql::literal::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::booleanliteral_has_value():
    assert hasattr(sql::literal::BooleanLiteral, "value")
    descriptor = None
    for klass in sql::literal::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::literal::nationalcharacterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::NationalCharacterStringLiteral)


def test_sql::literal::nationalcharacterstringliteral_constructor_exists():
    assert callable(sql::literal::NationalCharacterStringLiteral.__init__)


def test_sql::literal::nationalcharacterstringliteral_constructor_args():
    sig = inspect.signature(sql::literal::NationalCharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_sql::literal::nationalcharacterstringliteral_has_values():
    assert hasattr(sql::literal::NationalCharacterStringLiteral, "values")
    descriptor = None
    for klass in sql::literal::NationalCharacterStringLiteral.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
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



def test_sql::literal::characterstringliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::CharacterStringLiteral)


def test_sql::literal::characterstringliteral_constructor_exists():
    assert callable(sql::literal::CharacterStringLiteral.__init__)


def test_sql::literal::characterstringliteral_constructor_args():
    sig = inspect.signature(sql::literal::CharacterStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::generalliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::GeneralLiteral)


def test_sql::literal::generalliteral_constructor_exists():
    assert callable(sql::literal::GeneralLiteral.__init__)


def test_sql::literal::generalliteral_constructor_args():
    sig = inspect.signature(sql::literal::GeneralLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::literal_is_not_abstract():
    assert not inspect.isabstract(sql::literal::Literal)


def test_sql::literal::literal_constructor_exists():
    assert callable(sql::literal::Literal.__init__)


def test_sql::literal::literal_constructor_args():
    sig = inspect.signature(sql::literal::Literal.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::schemaqualifiedname_is_not_abstract():
    assert not inspect.isabstract(sql::common::SchemaQualifiedName)


def test_sql::common::schemaqualifiedname_constructor_exists():
    assert callable(sql::common::SchemaQualifiedName.__init__)


def test_sql::common::schemaqualifiedname_constructor_args():
    sig = inspect.signature(sql::common::SchemaQualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "catalogName" in params, "Missing parameter 'catalogName'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql::common::schemaqualifiedname_has_catalogName():
    assert hasattr(sql::common::SchemaQualifiedName, "catalogName")
    descriptor = None
    for klass in sql::common::SchemaQualifiedName.__mro__:
        if "catalogName" in klass.__dict__:
            descriptor = klass.__dict__["catalogName"]
            break
    assert isinstance(descriptor, property)

def test_sql::common::schemaqualifiedname_has_schemaName():
    assert hasattr(sql::common::SchemaQualifiedName, "schemaName")
    descriptor = None
    for klass in sql::common::SchemaQualifiedName.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_sql::common::schemaqualifiedname_has_name():
    assert hasattr(sql::common::SchemaQualifiedName, "name")
    descriptor = None
    for klass in sql::common::SchemaQualifiedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::common::statement_is_not_abstract():
    assert not inspect.isabstract(sql::common::Statement)


def test_sql::common::statement_constructor_exists():
    assert callable(sql::common::Statement.__init__)


def test_sql::common::statement_constructor_args():
    sig = inspect.signature(sql::common::Statement.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::bracketedcomment_is_not_abstract():
    assert not inspect.isabstract(sql::common::BracketedComment)


def test_sql::common::bracketedcomment_constructor_exists():
    assert callable(sql::common::BracketedComment.__init__)


def test_sql::common::bracketedcomment_constructor_args():
    sig = inspect.signature(sql::common::BracketedComment.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::simplecomment_is_not_abstract():
    assert not inspect.isabstract(sql::common::SimpleComment)


def test_sql::common::simplecomment_constructor_exists():
    assert callable(sql::common::SimpleComment.__init__)


def test_sql::common::simplecomment_constructor_args():
    sig = inspect.signature(sql::common::SimpleComment.__init__)
    params = list(sig.parameters.keys())



def test_separator_is_not_abstract():
    assert not inspect.isabstract(Separator)


def test_separator_constructor_exists():
    assert callable(Separator.__init__)


def test_separator_constructor_args():
    sig = inspect.signature(Separator.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::comment_is_not_abstract():
    assert not inspect.isabstract(sql::common::Comment)


def test_sql::common::comment_constructor_exists():
    assert callable(sql::common::Comment.__init__)


def test_sql::common::comment_constructor_args():
    sig = inspect.signature(sql::common::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::common::comment_has_value():
    assert hasattr(sql::common::Comment, "value")
    descriptor = None
    for klass in sql::common::Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::literal::numericliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::NumericLiteral)


def test_sql::literal::numericliteral_constructor_exists():
    assert callable(sql::literal::NumericLiteral.__init__)


def test_sql::literal::numericliteral_constructor_args():
    sig = inspect.signature(sql::literal::NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sql::literal::approximatenumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::ApproximateNumericLiteral)


def test_sql::literal::approximatenumericliteral_constructor_exists():
    assert callable(sql::literal::ApproximateNumericLiteral.__init__)


def test_sql::literal::approximatenumericliteral_constructor_args():
    sig = inspect.signature(sql::literal::ApproximateNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::approximatenumericliteral_has_value():
    assert hasattr(sql::literal::ApproximateNumericLiteral, "value")
    descriptor = None
    for klass in sql::literal::ApproximateNumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::literal::exactnumericliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::ExactNumericLiteral)


def test_sql::literal::exactnumericliteral_constructor_exists():
    assert callable(sql::literal::ExactNumericLiteral.__init__)


def test_sql::literal::exactnumericliteral_constructor_args():
    sig = inspect.signature(sql::literal::ExactNumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::exactnumericliteral_has_value():
    assert hasattr(sql::literal::ExactNumericLiteral, "value")
    descriptor = None
    for klass in sql::literal::ExactNumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::literal::timestampliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::TimestampLiteral)


def test_sql::literal::timestampliteral_constructor_exists():
    assert callable(sql::literal::TimestampLiteral.__init__)


def test_sql::literal::timestampliteral_constructor_args():
    sig = inspect.signature(sql::literal::TimestampLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::timestampliteral_has_value():
    assert hasattr(sql::literal::TimestampLiteral, "value")
    descriptor = None
    for klass in sql::literal::TimestampLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::literal::timeliteral_is_not_abstract():
    assert not inspect.isabstract(sql::literal::TimeLiteral)


def test_sql::literal::timeliteral_constructor_exists():
    assert callable(sql::literal::TimeLiteral.__init__)


def test_sql::literal::timeliteral_constructor_args():
    sig = inspect.signature(sql::literal::TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::literal::timeliteral_has_value():
    assert hasattr(sql::literal::TimeLiteral, "value")
    descriptor = None
    for klass in sql::literal::TimeLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::dummy_is_not_abstract():
    assert not inspect.isabstract(sql::Dummy)


def test_sql::dummy_constructor_exists():
    assert callable(sql::Dummy.__init__)


def test_sql::dummy_constructor_args():
    sig = inspect.signature(sql::Dummy.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::directsqlstatement_is_not_abstract():
    assert not inspect.isabstract(sql::common::DirectSQLStatement)


def test_sql::common::directsqlstatement_constructor_exists():
    assert callable(sql::common::DirectSQLStatement.__init__)


def test_sql::common::directsqlstatement_constructor_args():
    sig = inspect.signature(sql::common::DirectSQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::separator_is_not_abstract():
    assert not inspect.isabstract(sql::common::Separator)


def test_sql::common::separator_constructor_exists():
    assert callable(sql::common::Separator.__init__)


def test_sql::common::separator_constructor_args():
    sig = inspect.signature(sql::common::Separator.__init__)
    params = list(sig.parameters.keys())



def test_sql::common::sqlscript_is_not_abstract():
    assert not inspect.isabstract(sql::common::SQLScript)


def test_sql::common::sqlscript_constructor_exists():
    assert callable(sql::common::SQLScript.__init__)


def test_sql::common::sqlscript_constructor_args():
    sig = inspect.signature(sql::common::SQLScript.__init__)
    params = list(sig.parameters.keys())

def test_nationalcharacterstringtypekind_exists():
    # Check that the Enumeration exists
    assert NationalCharacterStringTypeKind is not None

def test_nationalcharacterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NationalCharacterStringTypeKind]
    expected_literals = [
        "NCHAR",
        "NATIONAL_CHARACTER",
        "NATIONAL_CHARACTER_VARYING",
        "NCHAR_VARYING",
        "NATIONAL_CHAR_VARYING",
        "NATIONAL_CHAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NationalCharacterStringTypeKind"

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

def test_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "K",
        "G",
        "M",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_datetimevaluefunctionkind_exists():
    # Check that the Enumeration exists
    assert DatetimeValueFunctionKind is not None

def test_datetimevaluefunctionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeValueFunctionKind]
    expected_literals = [
        "CURRENT_TIME",
        "LOCALTIME",
        "CURRENT_TIMESTAMP",
        "LOCALTIMESTAMP",
        "CURRENT_DATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeValueFunctionKind"

def test_charlengthunits_exists():
    # Check that the Enumeration exists
    assert CharLengthUnits is not None

def test_charlengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharLengthUnits]
    expected_literals = [
        "CODE_UNITS",
        "CHARACTERS",
        "OCTETS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharLengthUnits"

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

def test_tablescope_exists():
    # Check that the Enumeration exists
    assert TableScope is not None

def test_tablescope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableScope]
    expected_literals = [
        "PERSISTENT",
        "GLOBAL_TEMPORARY",
        "LOCAL_TEMPORARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableScope"

def test_exactnumerictypekind_exists():
    # Check that the Enumeration exists
    assert ExactNumericTypeKind is not None

def test_exactnumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExactNumericTypeKind]
    expected_literals = [
        "INT",
        "SMALLINT",
        "INTEGER",
        "NUMERIC",
        "BIGINT",
        "DEC",
        "DECIMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExactNumericTypeKind"

def test_characterstringtypekind_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypeKind is not None

def test_characterstringtypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypeKind]
    expected_literals = [
        "CHARACTER_VARYING",
        "CHARACTER",
        "VARCHAR",
        "CHAR",
        "CHAR_VARYING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypeKind"

def test_approximatenumerictypekind_exists():
    # Check that the Enumeration exists
    assert ApproximateNumericTypeKind is not None

def test_approximatenumerictypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ApproximateNumericTypeKind]
    expected_literals = [
        "REAL",
        "FLOAT",
        "DOUBLE_PRECISION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ApproximateNumericTypeKind"


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
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sql::schema::TableColumnsConstraint_strategy = st.builds(
    sql::schema::TableColumnsConstraint,
)
schema::TableColumnsConstraint_strategy = st.builds(
    schema::TableColumnsConstraint,
)
DatetimeValueFunction_strategy = st.builds(
    DatetimeValueFunction,
)
SQLSchemaStatement_strategy = st.builds(
    SQLSchemaStatement,
)
sql::schema::SQLSchemaDefinitionStatement_strategy = st.builds(
    sql::schema::SQLSchemaDefinitionStatement,
)
DirectSQLStatement_strategy = st.builds(
    DirectSQLStatement,
)
sql::schema::SQLSchemaStatement_strategy = st.builds(
    sql::schema::SQLSchemaStatement,
)
schema::ReferentialConstraint_strategy = st.builds(
    schema::ReferentialConstraint,
)
sql::schema::ReferentialTableConstraint_strategy = st.builds(
    sql::schema::ReferentialTableConstraint,
)
schema::ColumnConstraint_strategy = st.builds(
    schema::ColumnConstraint,
)
sql::schema::ReferentialColumnConstraint_strategy = st.builds(
    sql::schema::ReferentialColumnConstraint,
)
schema::UniqueConstraint_strategy = st.builds(
    schema::UniqueConstraint,
)
sql::schema::UniqueTableConstraint_strategy = st.builds(
    sql::schema::UniqueTableConstraint,
)
sql::schema::UniqueColumnConstraint_strategy = st.builds(
    sql::schema::UniqueColumnConstraint,
)
sql::schema::TableReference_strategy = st.builds(
    sql::schema::TableReference,
    schemaName=
        safe_text,
    catalogName=
        safe_text
)
TableReference_strategy = st.builds(
    TableReference,
)
sql::schema::ReferentialConstraint_strategy = st.builds(
    sql::schema::ReferentialConstraint,
)
sql::schema::UniqueConstraint_strategy = st.builds(
    sql::schema::UniqueConstraint,
    kind=
        safe_text
)
schema::TableElement_strategy = st.builds(
    schema::TableElement,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
sql::schema::NotNullColumnConstraint_strategy = st.builds(
    sql::schema::NotNullColumnConstraint,
)
DefaultOption_strategy = st.builds(
    DefaultOption,
)
sql::schema::ImplicitlyTypedValueSpecificationDefaultOption_strategy = st.builds(
    sql::schema::ImplicitlyTypedValueSpecificationDefaultOption,
)
sql::schema::LiteralDefaultOption_strategy = st.builds(
    sql::schema::LiteralDefaultOption,
)
sql::schema::DatetimeValueFunctionDefaultOption_strategy = st.builds(
    sql::schema::DatetimeValueFunctionDefaultOption,
)
TableElementList_strategy = st.builds(
    TableElementList,
)
sql::schema::TableElement_strategy = st.builds(
    sql::schema::TableElement,
)
TableElement_strategy = st.builds(
    TableElement,
)
sql::schema::Column_strategy = st.builds(
    sql::schema::Column,
    name=
        safe_text
)
TableContentsSource_strategy = st.builds(
    TableContentsSource,
)
sql::schema::TableElementList_strategy = st.builds(
    sql::schema::TableElementList,
)
EObject_strategy = st.builds(
    EObject,
)
sql::schema::TableConstraint_strategy = st.builds(
    sql::schema::TableConstraint,
)
schema::SQLSchemaDefinitionStatement_strategy = st.builds(
    schema::SQLSchemaDefinitionStatement,
)
sql::schema::TableDefinition_strategy = st.builds(
    sql::schema::TableDefinition,
    scope=
        safe_text,
    label=
        safe_text
)
sql::schema::ColumnConstraint_strategy = st.builds(
    sql::schema::ColumnConstraint,
)
Column_strategy = st.builds(
    Column,
)
sql::schema::DefaultOption_strategy = st.builds(
    sql::schema::DefaultOption,
)
TableDefinition_strategy = st.builds(
    TableDefinition,
)
sql::schema::TableContentsSource_strategy = st.builds(
    sql::schema::TableContentsSource,
)
DatetimeType_strategy = st.builds(
    DatetimeType,
)
sql::datatype::TimestampType_strategy = st.builds(
    sql::datatype::TimestampType,
    withTimeZone=
        safe_text,
    precision=
        safe_text
)
sql::datatype::TimeType_strategy = st.builds(
    sql::datatype::TimeType,
    precision=
        safe_text,
    withTimeZone=
        safe_text
)
sql::datatype::DateType_strategy = st.builds(
    sql::datatype::DateType,
)
sql::datatype::LargeObjectLength_strategy = st.builds(
    sql::datatype::LargeObjectLength,
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
sql::datatype::ApproximateNumericType_strategy = st.builds(
    sql::datatype::ApproximateNumericType,
    kind=
        safe_text,
    precision=
        safe_text
)
sql::datatype::ExactNumericType_strategy = st.builds(
    sql::datatype::ExactNumericType,
    precision=
        safe_text,
    scale=
        safe_text,
    kind=
        safe_text
)
ImplicitlyTypedValueSpecification_strategy = st.builds(
    ImplicitlyTypedValueSpecification,
)
sql::expression::NullSpecification_strategy = st.builds(
    sql::expression::NullSpecification,
)
sql::expression::ImplicitlyTypedValueSpecification_strategy = st.builds(
    sql::expression::ImplicitlyTypedValueSpecification,
)
sql::function::DatetimeValueFunction_strategy = st.builds(
    sql::function::DatetimeValueFunction,
    kind=
        safe_text,
    precision=
        safe_text
)
LargeObjectLength_strategy = st.builds(
    LargeObjectLength,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
sql::datatype::BooleanType_strategy = st.builds(
    sql::datatype::BooleanType,
)
sql::datatype::BinaryLargeObjectStringType_strategy = st.builds(
    sql::datatype::BinaryLargeObjectStringType,
    kind=
        safe_text
)
sql::datatype::DatetimeType_strategy = st.builds(
    sql::datatype::DatetimeType,
)
sql::datatype::NumericType_strategy = st.builds(
    sql::datatype::NumericType,
)
sql::datatype::NationalCharacterStringType_strategy = st.builds(
    sql::datatype::NationalCharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
sql::datatype::CharacterStringType_strategy = st.builds(
    sql::datatype::CharacterStringType,
    length=
        safe_text,
    kind=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
sql::datatype::PredefinedType_strategy = st.builds(
    sql::datatype::PredefinedType,
)
sql::datatype::DataType_strategy = st.builds(
    sql::datatype::DataType,
)
DatetimeLiteral_strategy = st.builds(
    DatetimeLiteral,
)
sql::literal::DateLiteral_strategy = st.builds(
    sql::literal::DateLiteral,
    value=
        safe_text
)
GeneralLiteral_strategy = st.builds(
    GeneralLiteral,
)
sql::literal::DatetimeLiteral_strategy = st.builds(
    sql::literal::DatetimeLiteral,
)
sql::literal::BooleanLiteral_strategy = st.builds(
    sql::literal::BooleanLiteral,
    value=
        safe_text
)
sql::literal::NationalCharacterStringLiteral_strategy = st.builds(
    sql::literal::NationalCharacterStringLiteral,
    values=
        safe_text
)
SchemaQualifiedName_strategy = st.builds(
    SchemaQualifiedName,
)
NationalCharacterStringLiteral_strategy = st.builds(
    NationalCharacterStringLiteral,
)
sql::literal::CharacterStringLiteral_strategy = st.builds(
    sql::literal::CharacterStringLiteral,
)
Literal_strategy = st.builds(
    Literal,
)
sql::literal::GeneralLiteral_strategy = st.builds(
    sql::literal::GeneralLiteral,
)
sql::literal::Literal_strategy = st.builds(
    sql::literal::Literal,
)
sql::common::SchemaQualifiedName_strategy = st.builds(
    sql::common::SchemaQualifiedName,
    catalogName=
        safe_text,
    schemaName=
        safe_text,
    name=
        safe_text
)
sql::common::Statement_strategy = st.builds(
    sql::common::Statement,
)
Comment_strategy = st.builds(
    Comment,
)
sql::common::BracketedComment_strategy = st.builds(
    sql::common::BracketedComment,
)
sql::common::SimpleComment_strategy = st.builds(
    sql::common::SimpleComment,
)
Separator_strategy = st.builds(
    Separator,
)
sql::common::Comment_strategy = st.builds(
    sql::common::Comment,
    value=
        safe_text
)
sql::literal::NumericLiteral_strategy = st.builds(
    sql::literal::NumericLiteral,
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
sql::literal::ApproximateNumericLiteral_strategy = st.builds(
    sql::literal::ApproximateNumericLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sql::literal::ExactNumericLiteral_strategy = st.builds(
    sql::literal::ExactNumericLiteral,
    value=
        safe_text
)
sql::literal::TimestampLiteral_strategy = st.builds(
    sql::literal::TimestampLiteral,
    value=
        safe_text
)
sql::literal::TimeLiteral_strategy = st.builds(
    sql::literal::TimeLiteral,
    value=
        safe_text
)
sql::Dummy_strategy = st.builds(
    sql::Dummy,
)
Statement_strategy = st.builds(
    Statement,
)
sql::common::DirectSQLStatement_strategy = st.builds(
    sql::common::DirectSQLStatement,
)
sql::common::Separator_strategy = st.builds(
    sql::common::Separator,
)
sql::common::SQLScript_strategy = st.builds(
    sql::common::SQLScript,
)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sql::schema::TableColumnsConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::tablecolumnsconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::TableColumnsConstraint)

@given(instance=schema::TableColumnsConstraint_strategy)
@settings(max_examples=50)
def test_schema::tablecolumnsconstraint_instantiation(instance):
    assert isinstance(instance, schema::TableColumnsConstraint)

@given(instance=DatetimeValueFunction_strategy)
@settings(max_examples=50)
def test_datetimevaluefunction_instantiation(instance):
    assert isinstance(instance, DatetimeValueFunction)

@given(instance=SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sqlschemastatement_instantiation(instance):
    assert isinstance(instance, SQLSchemaStatement)

@given(instance=sql::schema::SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=50)
def test_sql::schema::sqlschemadefinitionstatement_instantiation(instance):
    assert isinstance(instance, sql::schema::SQLSchemaDefinitionStatement)

@given(instance=DirectSQLStatement_strategy)
@settings(max_examples=50)
def test_directsqlstatement_instantiation(instance):
    assert isinstance(instance, DirectSQLStatement)

@given(instance=sql::schema::SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sql::schema::sqlschemastatement_instantiation(instance):
    assert isinstance(instance, sql::schema::SQLSchemaStatement)

@given(instance=schema::ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_schema::referentialconstraint_instantiation(instance):
    assert isinstance(instance, schema::ReferentialConstraint)

@given(instance=sql::schema::ReferentialTableConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::referentialtableconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::ReferentialTableConstraint)

@given(instance=schema::ColumnConstraint_strategy)
@settings(max_examples=50)
def test_schema::columnconstraint_instantiation(instance):
    assert isinstance(instance, schema::ColumnConstraint)

@given(instance=sql::schema::ReferentialColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::referentialcolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::ReferentialColumnConstraint)

@given(instance=schema::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_schema::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, schema::UniqueConstraint)

@given(instance=sql::schema::UniqueTableConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::uniquetableconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::UniqueTableConstraint)

@given(instance=sql::schema::UniqueColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::uniquecolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::UniqueColumnConstraint)

@given(instance=sql::schema::TableReference_strategy)
@settings(max_examples=50)
def test_sql::schema::tablereference_instantiation(instance):
    assert isinstance(instance, sql::schema::TableReference)

@given(instance=sql::schema::TableReference_strategy)
def test_sql::schema::tablereference_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=sql::schema::TableReference_strategy)
def test_sql::schema::tablereference_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=sql::schema::TableReference_strategy)
def test_sql::schema::tablereference_catalogName_type(instance):
    assert isinstance(instance.catalogName, str)


@given(instance=sql::schema::TableReference_strategy)
def test_sql::schema::tablereference_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original

@given(instance=TableReference_strategy)
@settings(max_examples=50)
def test_tablereference_instantiation(instance):
    assert isinstance(instance, TableReference)

@given(instance=sql::schema::ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::referentialconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::ReferentialConstraint)

@given(instance=sql::schema::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::UniqueConstraint)

@given(instance=sql::schema::UniqueConstraint_strategy)
def test_sql::schema::uniqueconstraint_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::schema::UniqueConstraint_strategy)
def test_sql::schema::uniqueconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=schema::TableElement_strategy)
@settings(max_examples=50)
def test_schema::tableelement_instantiation(instance):
    assert isinstance(instance, schema::TableElement)

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=sql::schema::NotNullColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::notnullcolumnconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::NotNullColumnConstraint)

@given(instance=DefaultOption_strategy)
@settings(max_examples=50)
def test_defaultoption_instantiation(instance):
    assert isinstance(instance, DefaultOption)

@given(instance=sql::schema::ImplicitlyTypedValueSpecificationDefaultOption_strategy)
@settings(max_examples=50)
def test_sql::schema::implicitlytypedvaluespecificationdefaultoption_instantiation(instance):
    assert isinstance(instance, sql::schema::ImplicitlyTypedValueSpecificationDefaultOption)

@given(instance=sql::schema::LiteralDefaultOption_strategy)
@settings(max_examples=50)
def test_sql::schema::literaldefaultoption_instantiation(instance):
    assert isinstance(instance, sql::schema::LiteralDefaultOption)

@given(instance=sql::schema::DatetimeValueFunctionDefaultOption_strategy)
@settings(max_examples=50)
def test_sql::schema::datetimevaluefunctiondefaultoption_instantiation(instance):
    assert isinstance(instance, sql::schema::DatetimeValueFunctionDefaultOption)

@given(instance=TableElementList_strategy)
@settings(max_examples=50)
def test_tableelementlist_instantiation(instance):
    assert isinstance(instance, TableElementList)

@given(instance=sql::schema::TableElement_strategy)
@settings(max_examples=50)
def test_sql::schema::tableelement_instantiation(instance):
    assert isinstance(instance, sql::schema::TableElement)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=sql::schema::Column_strategy)
@settings(max_examples=50)
def test_sql::schema::column_instantiation(instance):
    assert isinstance(instance, sql::schema::Column)

@given(instance=sql::schema::Column_strategy)
def test_sql::schema::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::schema::Column_strategy)
def test_sql::schema::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TableContentsSource_strategy)
@settings(max_examples=50)
def test_tablecontentssource_instantiation(instance):
    assert isinstance(instance, TableContentsSource)

@given(instance=sql::schema::TableElementList_strategy)
@settings(max_examples=50)
def test_sql::schema::tableelementlist_instantiation(instance):
    assert isinstance(instance, sql::schema::TableElementList)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=sql::schema::TableConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::tableconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::TableConstraint)

@given(instance=schema::SQLSchemaDefinitionStatement_strategy)
@settings(max_examples=50)
def test_schema::sqlschemadefinitionstatement_instantiation(instance):
    assert isinstance(instance, schema::SQLSchemaDefinitionStatement)

@given(instance=sql::schema::TableDefinition_strategy)
@settings(max_examples=50)
def test_sql::schema::tabledefinition_instantiation(instance):
    assert isinstance(instance, sql::schema::TableDefinition)

@given(instance=sql::schema::TableDefinition_strategy)
def test_sql::schema::tabledefinition_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=sql::schema::TableDefinition_strategy)
def test_sql::schema::tabledefinition_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=sql::schema::TableDefinition_strategy)
def test_sql::schema::tabledefinition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=sql::schema::TableDefinition_strategy)
def test_sql::schema::tabledefinition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=sql::schema::ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql::schema::columnconstraint_instantiation(instance):
    assert isinstance(instance, sql::schema::ColumnConstraint)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=sql::schema::DefaultOption_strategy)
@settings(max_examples=50)
def test_sql::schema::defaultoption_instantiation(instance):
    assert isinstance(instance, sql::schema::DefaultOption)

@given(instance=TableDefinition_strategy)
@settings(max_examples=50)
def test_tabledefinition_instantiation(instance):
    assert isinstance(instance, TableDefinition)

@given(instance=sql::schema::TableContentsSource_strategy)
@settings(max_examples=50)
def test_sql::schema::tablecontentssource_instantiation(instance):
    assert isinstance(instance, sql::schema::TableContentsSource)

@given(instance=DatetimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DatetimeType)

@given(instance=sql::datatype::TimestampType_strategy)
@settings(max_examples=50)
def test_sql::datatype::timestamptype_instantiation(instance):
    assert isinstance(instance, sql::datatype::TimestampType)

@given(instance=sql::datatype::TimestampType_strategy)
def test_sql::datatype::timestamptype_withTimeZone_type(instance):
    assert isinstance(instance.withTimeZone, str)


@given(instance=sql::datatype::TimestampType_strategy)
def test_sql::datatype::timestamptype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original

@given(instance=sql::datatype::TimestampType_strategy)
def test_sql::datatype::timestamptype_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=sql::datatype::TimestampType_strategy)
def test_sql::datatype::timestamptype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sql::datatype::TimeType_strategy)
@settings(max_examples=50)
def test_sql::datatype::timetype_instantiation(instance):
    assert isinstance(instance, sql::datatype::TimeType)

@given(instance=sql::datatype::TimeType_strategy)
def test_sql::datatype::timetype_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=sql::datatype::TimeType_strategy)
def test_sql::datatype::timetype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sql::datatype::TimeType_strategy)
def test_sql::datatype::timetype_withTimeZone_type(instance):
    assert isinstance(instance.withTimeZone, str)


@given(instance=sql::datatype::TimeType_strategy)
def test_sql::datatype::timetype_withTimeZone_setter(instance):
    original = instance.withTimeZone
    instance.withTimeZone = original
    assert instance.withTimeZone == original

@given(instance=sql::datatype::DateType_strategy)
@settings(max_examples=50)
def test_sql::datatype::datetype_instantiation(instance):
    assert isinstance(instance, sql::datatype::DateType)

@given(instance=sql::datatype::LargeObjectLength_strategy)
@settings(max_examples=50)
def test_sql::datatype::largeobjectlength_instantiation(instance):
    assert isinstance(instance, sql::datatype::LargeObjectLength)

@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_multiplier_type(instance):
    assert isinstance(instance.multiplier, str)


@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_multiplier_setter(instance):
    original = instance.multiplier
    instance.multiplier = original
    assert instance.multiplier == original

@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=sql::datatype::LargeObjectLength_strategy)
def test_sql::datatype::largeobjectlength_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=sql::datatype::ApproximateNumericType_strategy)
@settings(max_examples=50)
def test_sql::datatype::approximatenumerictype_instantiation(instance):
    assert isinstance(instance, sql::datatype::ApproximateNumericType)

@given(instance=sql::datatype::ApproximateNumericType_strategy)
def test_sql::datatype::approximatenumerictype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::datatype::ApproximateNumericType_strategy)
def test_sql::datatype::approximatenumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql::datatype::ApproximateNumericType_strategy)
def test_sql::datatype::approximatenumerictype_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=sql::datatype::ApproximateNumericType_strategy)
def test_sql::datatype::approximatenumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sql::datatype::ExactNumericType_strategy)
@settings(max_examples=50)
def test_sql::datatype::exactnumerictype_instantiation(instance):
    assert isinstance(instance, sql::datatype::ExactNumericType)

@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::datatype::ExactNumericType_strategy)
def test_sql::datatype::exactnumerictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=50)
def test_implicitlytypedvaluespecification_instantiation(instance):
    assert isinstance(instance, ImplicitlyTypedValueSpecification)

@given(instance=sql::expression::NullSpecification_strategy)
@settings(max_examples=50)
def test_sql::expression::nullspecification_instantiation(instance):
    assert isinstance(instance, sql::expression::NullSpecification)

@given(instance=sql::expression::ImplicitlyTypedValueSpecification_strategy)
@settings(max_examples=50)
def test_sql::expression::implicitlytypedvaluespecification_instantiation(instance):
    assert isinstance(instance, sql::expression::ImplicitlyTypedValueSpecification)

@given(instance=sql::function::DatetimeValueFunction_strategy)
@settings(max_examples=50)
def test_sql::function::datetimevaluefunction_instantiation(instance):
    assert isinstance(instance, sql::function::DatetimeValueFunction)

@given(instance=sql::function::DatetimeValueFunction_strategy)
def test_sql::function::datetimevaluefunction_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::function::DatetimeValueFunction_strategy)
def test_sql::function::datetimevaluefunction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql::function::DatetimeValueFunction_strategy)
def test_sql::function::datetimevaluefunction_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=sql::function::DatetimeValueFunction_strategy)
def test_sql::function::datetimevaluefunction_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=LargeObjectLength_strategy)
@settings(max_examples=50)
def test_largeobjectlength_instantiation(instance):
    assert isinstance(instance, LargeObjectLength)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=sql::datatype::BooleanType_strategy)
@settings(max_examples=50)
def test_sql::datatype::booleantype_instantiation(instance):
    assert isinstance(instance, sql::datatype::BooleanType)

@given(instance=sql::datatype::BinaryLargeObjectStringType_strategy)
@settings(max_examples=50)
def test_sql::datatype::binarylargeobjectstringtype_instantiation(instance):
    assert isinstance(instance, sql::datatype::BinaryLargeObjectStringType)

@given(instance=sql::datatype::BinaryLargeObjectStringType_strategy)
def test_sql::datatype::binarylargeobjectstringtype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::datatype::BinaryLargeObjectStringType_strategy)
def test_sql::datatype::binarylargeobjectstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql::datatype::DatetimeType_strategy)
@settings(max_examples=50)
def test_sql::datatype::datetimetype_instantiation(instance):
    assert isinstance(instance, sql::datatype::DatetimeType)

@given(instance=sql::datatype::NumericType_strategy)
@settings(max_examples=50)
def test_sql::datatype::numerictype_instantiation(instance):
    assert isinstance(instance, sql::datatype::NumericType)

@given(instance=sql::datatype::NationalCharacterStringType_strategy)
@settings(max_examples=50)
def test_sql::datatype::nationalcharacterstringtype_instantiation(instance):
    assert isinstance(instance, sql::datatype::NationalCharacterStringType)

@given(instance=sql::datatype::NationalCharacterStringType_strategy)
def test_sql::datatype::nationalcharacterstringtype_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=sql::datatype::NationalCharacterStringType_strategy)
def test_sql::datatype::nationalcharacterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=sql::datatype::NationalCharacterStringType_strategy)
def test_sql::datatype::nationalcharacterstringtype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::datatype::NationalCharacterStringType_strategy)
def test_sql::datatype::nationalcharacterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sql::datatype::CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql::datatype::characterstringtype_instantiation(instance):
    assert isinstance(instance, sql::datatype::CharacterStringType)

@given(instance=sql::datatype::CharacterStringType_strategy)
def test_sql::datatype::characterstringtype_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=sql::datatype::CharacterStringType_strategy)
def test_sql::datatype::characterstringtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=sql::datatype::CharacterStringType_strategy)
def test_sql::datatype::characterstringtype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sql::datatype::CharacterStringType_strategy)
def test_sql::datatype::characterstringtype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sql::datatype::PredefinedType_strategy)
@settings(max_examples=50)
def test_sql::datatype::predefinedtype_instantiation(instance):
    assert isinstance(instance, sql::datatype::PredefinedType)

@given(instance=sql::datatype::DataType_strategy)
@settings(max_examples=50)
def test_sql::datatype::datatype_instantiation(instance):
    assert isinstance(instance, sql::datatype::DataType)

@given(instance=DatetimeLiteral_strategy)
@settings(max_examples=50)
def test_datetimeliteral_instantiation(instance):
    assert isinstance(instance, DatetimeLiteral)

@given(instance=sql::literal::DateLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::dateliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::DateLiteral)

@given(instance=sql::literal::DateLiteral_strategy)
def test_sql::literal::dateliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::literal::DateLiteral_strategy)
def test_sql::literal::dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GeneralLiteral_strategy)
@settings(max_examples=50)
def test_generalliteral_instantiation(instance):
    assert isinstance(instance, GeneralLiteral)

@given(instance=sql::literal::DatetimeLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::datetimeliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::DatetimeLiteral)

@given(instance=sql::literal::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::booleanliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::BooleanLiteral)

@given(instance=sql::literal::BooleanLiteral_strategy)
def test_sql::literal::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::literal::BooleanLiteral_strategy)
def test_sql::literal::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::literal::NationalCharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::nationalcharacterstringliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::NationalCharacterStringLiteral)

@given(instance=sql::literal::NationalCharacterStringLiteral_strategy)
def test_sql::literal::nationalcharacterstringliteral_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=sql::literal::NationalCharacterStringLiteral_strategy)
def test_sql::literal::nationalcharacterstringliteral_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=SchemaQualifiedName_strategy)
@settings(max_examples=50)
def test_schemaqualifiedname_instantiation(instance):
    assert isinstance(instance, SchemaQualifiedName)

@given(instance=NationalCharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_nationalcharacterstringliteral_instantiation(instance):
    assert isinstance(instance, NationalCharacterStringLiteral)

@given(instance=sql::literal::CharacterStringLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::characterstringliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::CharacterStringLiteral)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=sql::literal::GeneralLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::generalliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::GeneralLiteral)

@given(instance=sql::literal::Literal_strategy)
@settings(max_examples=50)
def test_sql::literal::literal_instantiation(instance):
    assert isinstance(instance, sql::literal::Literal)

@given(instance=sql::common::SchemaQualifiedName_strategy)
@settings(max_examples=50)
def test_sql::common::schemaqualifiedname_instantiation(instance):
    assert isinstance(instance, sql::common::SchemaQualifiedName)

@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_catalogName_type(instance):
    assert isinstance(instance.catalogName, str)


@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_catalogName_setter(instance):
    original = instance.catalogName
    instance.catalogName = original
    assert instance.catalogName == original

@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::common::SchemaQualifiedName_strategy)
def test_sql::common::schemaqualifiedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::common::Statement_strategy)
@settings(max_examples=50)
def test_sql::common::statement_instantiation(instance):
    assert isinstance(instance, sql::common::Statement)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=sql::common::BracketedComment_strategy)
@settings(max_examples=50)
def test_sql::common::bracketedcomment_instantiation(instance):
    assert isinstance(instance, sql::common::BracketedComment)

@given(instance=sql::common::SimpleComment_strategy)
@settings(max_examples=50)
def test_sql::common::simplecomment_instantiation(instance):
    assert isinstance(instance, sql::common::SimpleComment)

@given(instance=Separator_strategy)
@settings(max_examples=50)
def test_separator_instantiation(instance):
    assert isinstance(instance, Separator)

@given(instance=sql::common::Comment_strategy)
@settings(max_examples=50)
def test_sql::common::comment_instantiation(instance):
    assert isinstance(instance, sql::common::Comment)

@given(instance=sql::common::Comment_strategy)
def test_sql::common::comment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::common::Comment_strategy)
def test_sql::common::comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::literal::NumericLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::numericliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::NumericLiteral)

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=sql::literal::ApproximateNumericLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::approximatenumericliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::ApproximateNumericLiteral)

@given(instance=sql::literal::ApproximateNumericLiteral_strategy)
def test_sql::literal::approximatenumericliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=sql::literal::ApproximateNumericLiteral_strategy)
def test_sql::literal::approximatenumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::literal::ExactNumericLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::exactnumericliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::ExactNumericLiteral)

@given(instance=sql::literal::ExactNumericLiteral_strategy)
def test_sql::literal::exactnumericliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::literal::ExactNumericLiteral_strategy)
def test_sql::literal::exactnumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::literal::TimestampLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::timestampliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::TimestampLiteral)

@given(instance=sql::literal::TimestampLiteral_strategy)
def test_sql::literal::timestampliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::literal::TimestampLiteral_strategy)
def test_sql::literal::timestampliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::literal::TimeLiteral_strategy)
@settings(max_examples=50)
def test_sql::literal::timeliteral_instantiation(instance):
    assert isinstance(instance, sql::literal::TimeLiteral)

@given(instance=sql::literal::TimeLiteral_strategy)
def test_sql::literal::timeliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::literal::TimeLiteral_strategy)
def test_sql::literal::timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::Dummy_strategy)
@settings(max_examples=50)
def test_sql::dummy_instantiation(instance):
    assert isinstance(instance, sql::Dummy)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sql::common::DirectSQLStatement_strategy)
@settings(max_examples=50)
def test_sql::common::directsqlstatement_instantiation(instance):
    assert isinstance(instance, sql::common::DirectSQLStatement)

@given(instance=sql::common::Separator_strategy)
@settings(max_examples=50)
def test_sql::common::separator_instantiation(instance):
    assert isinstance(instance, sql::common::Separator)

@given(instance=sql::common::SQLScript_strategy)
@settings(max_examples=50)
def test_sql::common::sqlscript_instantiation(instance):
    assert isinstance(instance, sql::common::SQLScript)
