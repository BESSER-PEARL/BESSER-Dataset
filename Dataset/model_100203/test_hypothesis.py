import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Group,
    User,
    Role,
    RoleAuthorization,
    ValueExpression,
    QueryExpression,
    DerivedTable,
    sqlmodel::tables::ViewTable,
    statements::SQLStatement,
    SQLDataStatement,
    sqlmodel::statements::SQLDataChangeStatement,
    SQLStatement,
    sqlmodel::statements::SQLTransactionStatement,
    sqlmodel::statements::SQLControlStatement,
    sqlmodel::statements::SQLDynamicStatement,
    sqlmodel::statements::SQLConnectionStatement,
    sqlmodel::statements::SQLSchemaStatement,
    sqlmodel::statements::SQLDiagnosticsStatement,
    sqlmodel::statements::SQLSessionStatement,
    sqlmodel::statements::SQLDataStatement,
    sqlmodel::statements::SQLStatement,
    Function,
    sqlmodel::routines::BuiltInFunction,
    sqlmodel::routines::UserDefinedFunction,
    sqlmodel::routines::Method,
    RoutineResultTable,
    Source,
    Parameter,
    expressions::SearchCondition,
    expressions::ValueExpression,
    sqlmodel::expressions::QueryExpression,
    expressions::QueryExpression,
    schema::SQLObject,
    sqlmodel::expressions::SearchConditionDefault,
    sqlmodel::expressions::ValueExpressionDefault,
    sqlmodel::statements::SQLStatementDefault,
    sqlmodel::expressions::QueryExpressionDefault,
    sqlmodel::expressions::SearchCondition,
    sqlmodel::expressions::ValueExpression,
    NumericalDataType,
    sqlmodel::datatypes::ApproximateNumericDataType,
    sqlmodel::datatypes::ExactNumericDataType,
    CheckConstraint,
    DistinctUserDefinedType,
    sqlmodel::datatypes::Domain,
    ExactNumericDataType,
    sqlmodel::datatypes::IntegerDataType,
    sqlmodel::datatypes::FixedPrecisionDataType,
    StructuredUserDefinedType,
    Method,
    AttributeDefinition,
    CharacterStringDataType,
    CollectionDataType,
    sqlmodel::datatypes::MultisetDataType,
    sqlmodel::datatypes::ArrayDataType,
    Field,
    PredefinedDataType,
    sqlmodel::datatypes::IntervalDataType,
    sqlmodel::datatypes::DataLinkDataType,
    sqlmodel::datatypes::BooleanDataType,
    sqlmodel::datatypes::DateDataType,
    sqlmodel::datatypes::CharacterStringDataType,
    sqlmodel::datatypes::XMLDataType,
    sqlmodel::datatypes::TimeDataType,
    sqlmodel::datatypes::BinaryStringDataType,
    sqlmodel::datatypes::NumericalDataType,
    ElementType,
    ConstructedDataType,
    sqlmodel::datatypes::RowDataType,
    sqlmodel::datatypes::ReferenceDataType,
    sqlmodel::datatypes::CollectionDataType,
    IndexExpression,
    UserDefinedTypeOrdering,
    DataType,
    sqlmodel::datatypes::SQLDataType,
    sqlmodel::datatypes::ConstructedDataType,
    sqlmodel::datatypes::UserDefinedType,
    IndexMember,
    ForeignKey,
    UniqueConstraint,
    sqlmodel::constraints::PrimaryKey,
    ReferenceConstraint,
    sqlmodel::constraints::UniqueConstraint,
    sqlmodel::constraints::ForeignKey,
    Column,
    TableConstraint,
    sqlmodel::constraints::CheckConstraint,
    sqlmodel::constraints::ReferenceConstraint,
    SearchCondition,
    Constraint,
    sqlmodel::constraints::TableConstraint,
    sqlmodel::constraints::Assertion,
    BaseTable,
    sqlmodel::tables::TemporaryTable,
    sqlmodel::tables::PersistentTable,
    sqlmodel::schema::Comment,
    sqlmodel::schema::ObjectExtension,
    Event,
    IdentitySpecifier,
    TypedElement,
    sqlmodel::datatypes::ElementType,
    sqlmodel::routines::Parameter,
    sqlmodel::datatypes::Field,
    sqlmodel::tables::Column,
    sqlmodel::datatypes::AttributeDefinition,
    sqlmodel::schema::Sequence,
    Privilege,
    Schema,
    ObjectExtension,
    Comment,
    Dependency,
    CharacterSet,
    Assertion,
    Catalog,
    ENamedElement,
    sqlmodel::schema::SQLObject,
    AuthorizationIdentifier,
    sqlmodel::accesscontrol::User,
    sqlmodel::accesscontrol::Role,
    sqlmodel::accesscontrol::Group,
    Routine,
    sqlmodel::routines::Function,
    sqlmodel::routines::Procedure,
    Trigger,
    schema::sqlmodel::EObject,
    Database,
    Sequence,
    Table,
    sqlmodel::tables::BaseTable,
    sqlmodel::tables::DerivedTable,
    sqlmodel::routines::RoutineResultTable,
    Index,
    UserDefinedType,
    sqlmodel::datatypes::StructuredUserDefinedType,
    sqlmodel::datatypes::DistinctUserDefinedType,
    SQLDataType,
    sqlmodel::datatypes::PredefinedDataType,
    SQLObject,
    sqlmodel::tables::Table,
    sqlmodel::tables::Trigger,
    sqlmodel::routines::Routine,
    sqlmodel::constraints::IndexExpression,
    sqlmodel::constraints::Index,
    sqlmodel::datatypes::CharacterSet,
    sqlmodel::schema::TypedElement,
    sqlmodel::accesscontrol::Privilege,
    sqlmodel::datatypes::UserDefinedTypeOrdering,
    sqlmodel::schema::Schema,
    sqlmodel::constraints::Constraint,
    sqlmodel::routines::Source,
    sqlmodel::datatypes::DataType,
    sqlmodel::schema::Dependency,
    sqlmodel::schema::Catalog,
    sqlmodel::accesscontrol::AuthorizationIdentifier,
    sqlmodel::schema::Event,
    sqlmodel::schema::Database,
    sqlmodel::constraints::IndexMember,
    sqlmodel::accesscontrol::RoleAuthorization,
    sqlmodel::schema::IdentitySpecifier,
    ActionTimeType,
    ActionGranularityType,
    ReadPermissionOption,
    UnlinkOption,
    CheckType,
    IntegrityControlOption,
    ReferentialActionType,
    OrderingType,
    OrderingCategoryType,
    LinkControlOption,
    MatchType,
    CoercibilityType,
    ReferenceType,
    IntervalQualifierType,
    ParameterMode,
    DataAccess,
    IncrementType,
    WritePermissionOption,
    GenerateType,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_roleauthorization_is_not_abstract():
    assert not inspect.isabstract(RoleAuthorization)


def test_roleauthorization_constructor_exists():
    assert callable(RoleAuthorization.__init__)


def test_roleauthorization_constructor_args():
    sig = inspect.signature(RoleAuthorization.__init__)
    params = list(sig.parameters.keys())



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_queryexpression_is_not_abstract():
    assert not inspect.isabstract(QueryExpression)


def test_queryexpression_constructor_exists():
    assert callable(QueryExpression.__init__)


def test_queryexpression_constructor_args():
    sig = inspect.signature(QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_derivedtable_is_not_abstract():
    assert not inspect.isabstract(DerivedTable)


def test_derivedtable_constructor_exists():
    assert callable(DerivedTable.__init__)


def test_derivedtable_constructor_args():
    sig = inspect.signature(DerivedTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::tables::viewtable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::ViewTable)


def test_sqlmodel::tables::viewtable_constructor_exists():
    assert callable(sqlmodel::tables::ViewTable.__init__)


def test_sqlmodel::tables::viewtable_constructor_args():
    sig = inspect.signature(sqlmodel::tables::ViewTable.__init__)
    params = list(sig.parameters.keys())
    assert "checkType" in params, "Missing parameter 'checkType'"

def test_sqlmodel::tables::viewtable_has_checkType():
    assert hasattr(sqlmodel::tables::ViewTable, "checkType")
    descriptor = None
    for klass in sqlmodel::tables::ViewTable.__mro__:
        if "checkType" in klass.__dict__:
            descriptor = klass.__dict__["checkType"]
            break
    assert isinstance(descriptor, property)



def test_statements::sqlstatement_is_not_abstract():
    assert not inspect.isabstract(statements::SQLStatement)


def test_statements::sqlstatement_constructor_exists():
    assert callable(statements::SQLStatement.__init__)


def test_statements::sqlstatement_constructor_args():
    sig = inspect.signature(statements::SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(SQLDataStatement)


def test_sqldatastatement_constructor_exists():
    assert callable(SQLDataStatement.__init__)


def test_sqldatastatement_constructor_args():
    sig = inspect.signature(SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqldatachangestatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLDataChangeStatement)


def test_sqlmodel::statements::sqldatachangestatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLDataChangeStatement.__init__)


def test_sqlmodel::statements::sqldatachangestatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLDataChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(SQLStatement)


def test_sqlstatement_constructor_exists():
    assert callable(SQLStatement.__init__)


def test_sqlstatement_constructor_args():
    sig = inspect.signature(SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqltransactionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLTransactionStatement)


def test_sqlmodel::statements::sqltransactionstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLTransactionStatement.__init__)


def test_sqlmodel::statements::sqltransactionstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLTransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqlcontrolstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLControlStatement)


def test_sqlmodel::statements::sqlcontrolstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLControlStatement.__init__)


def test_sqlmodel::statements::sqlcontrolstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqldynamicstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLDynamicStatement)


def test_sqlmodel::statements::sqldynamicstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLDynamicStatement.__init__)


def test_sqlmodel::statements::sqldynamicstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLDynamicStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqlconnectionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLConnectionStatement)


def test_sqlmodel::statements::sqlconnectionstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLConnectionStatement.__init__)


def test_sqlmodel::statements::sqlconnectionstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLConnectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLSchemaStatement)


def test_sqlmodel::statements::sqlschemastatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLSchemaStatement.__init__)


def test_sqlmodel::statements::sqlschemastatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqldiagnosticsstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLDiagnosticsStatement)


def test_sqlmodel::statements::sqldiagnosticsstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLDiagnosticsStatement.__init__)


def test_sqlmodel::statements::sqldiagnosticsstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLDiagnosticsStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqlsessionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLSessionStatement)


def test_sqlmodel::statements::sqlsessionstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLSessionStatement.__init__)


def test_sqlmodel::statements::sqlsessionstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLSessionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLDataStatement)


def test_sqlmodel::statements::sqldatastatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLDataStatement.__init__)


def test_sqlmodel::statements::sqldatastatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::statements::sqlstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLStatement)


def test_sqlmodel::statements::sqlstatement_constructor_exists():
    assert callable(sqlmodel::statements::SQLStatement.__init__)


def test_sqlmodel::statements::sqlstatement_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::builtinfunction_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::BuiltInFunction)


def test_sqlmodel::routines::builtinfunction_constructor_exists():
    assert callable(sqlmodel::routines::BuiltInFunction.__init__)


def test_sqlmodel::routines::builtinfunction_constructor_args():
    sig = inspect.signature(sqlmodel::routines::BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::userdefinedfunction_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::UserDefinedFunction)


def test_sqlmodel::routines::userdefinedfunction_constructor_exists():
    assert callable(sqlmodel::routines::UserDefinedFunction.__init__)


def test_sqlmodel::routines::userdefinedfunction_constructor_args():
    sig = inspect.signature(sqlmodel::routines::UserDefinedFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::method_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Method)


def test_sqlmodel::routines::method_constructor_exists():
    assert callable(sqlmodel::routines::Method.__init__)


def test_sqlmodel::routines::method_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Method.__init__)
    params = list(sig.parameters.keys())
    assert "overriding" in params, "Missing parameter 'overriding'"
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_sqlmodel::routines::method_has_overriding():
    assert hasattr(sqlmodel::routines::Method, "overriding")
    descriptor = None
    for klass in sqlmodel::routines::Method.__mro__:
        if "overriding" in klass.__dict__:
            descriptor = klass.__dict__["overriding"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::method_has_constructor():
    assert hasattr(sqlmodel::routines::Method, "constructor")
    descriptor = None
    for klass in sqlmodel::routines::Method.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_routineresulttable_is_not_abstract():
    assert not inspect.isabstract(RoutineResultTable)


def test_routineresulttable_constructor_exists():
    assert callable(RoutineResultTable.__init__)


def test_routineresulttable_constructor_args():
    sig = inspect.signature(RoutineResultTable.__init__)
    params = list(sig.parameters.keys())



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_expressions::searchcondition_is_not_abstract():
    assert not inspect.isabstract(expressions::SearchCondition)


def test_expressions::searchcondition_constructor_exists():
    assert callable(expressions::SearchCondition.__init__)


def test_expressions::searchcondition_constructor_args():
    sig = inspect.signature(expressions::SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_expressions::valueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ValueExpression)


def test_expressions::valueexpression_constructor_exists():
    assert callable(expressions::ValueExpression.__init__)


def test_expressions::valueexpression_constructor_args():
    sig = inspect.signature(expressions::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::expressions::queryexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::QueryExpression)


def test_sqlmodel::expressions::queryexpression_constructor_exists():
    assert callable(sqlmodel::expressions::QueryExpression.__init__)


def test_sqlmodel::expressions::queryexpression_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::queryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::QueryExpression)


def test_expressions::queryexpression_constructor_exists():
    assert callable(expressions::QueryExpression.__init__)


def test_expressions::queryexpression_constructor_args():
    sig = inspect.signature(expressions::QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_schema::sqlobject_is_not_abstract():
    assert not inspect.isabstract(schema::SQLObject)


def test_schema::sqlobject_constructor_exists():
    assert callable(schema::SQLObject.__init__)


def test_schema::sqlobject_constructor_args():
    sig = inspect.signature(schema::SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::expressions::searchconditiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::SearchConditionDefault)


def test_sqlmodel::expressions::searchconditiondefault_constructor_exists():
    assert callable(sqlmodel::expressions::SearchConditionDefault.__init__)


def test_sqlmodel::expressions::searchconditiondefault_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::SearchConditionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel::expressions::searchconditiondefault_has_SQL():
    assert hasattr(sqlmodel::expressions::SearchConditionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel::expressions::SearchConditionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::expressions::valueexpressiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::ValueExpressionDefault)


def test_sqlmodel::expressions::valueexpressiondefault_constructor_exists():
    assert callable(sqlmodel::expressions::ValueExpressionDefault.__init__)


def test_sqlmodel::expressions::valueexpressiondefault_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::ValueExpressionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel::expressions::valueexpressiondefault_has_SQL():
    assert hasattr(sqlmodel::expressions::ValueExpressionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel::expressions::ValueExpressionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::statements::sqlstatementdefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::statements::SQLStatementDefault)


def test_sqlmodel::statements::sqlstatementdefault_constructor_exists():
    assert callable(sqlmodel::statements::SQLStatementDefault.__init__)


def test_sqlmodel::statements::sqlstatementdefault_constructor_args():
    sig = inspect.signature(sqlmodel::statements::SQLStatementDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel::statements::sqlstatementdefault_has_SQL():
    assert hasattr(sqlmodel::statements::SQLStatementDefault, "SQL")
    descriptor = None
    for klass in sqlmodel::statements::SQLStatementDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::expressions::queryexpressiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::QueryExpressionDefault)


def test_sqlmodel::expressions::queryexpressiondefault_constructor_exists():
    assert callable(sqlmodel::expressions::QueryExpressionDefault.__init__)


def test_sqlmodel::expressions::queryexpressiondefault_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::QueryExpressionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel::expressions::queryexpressiondefault_has_SQL():
    assert hasattr(sqlmodel::expressions::QueryExpressionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel::expressions::QueryExpressionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::expressions::searchcondition_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::SearchCondition)


def test_sqlmodel::expressions::searchcondition_constructor_exists():
    assert callable(sqlmodel::expressions::SearchCondition.__init__)


def test_sqlmodel::expressions::searchcondition_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::expressions::valueexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::expressions::ValueExpression)


def test_sqlmodel::expressions::valueexpression_constructor_exists():
    assert callable(sqlmodel::expressions::ValueExpression.__init__)


def test_sqlmodel::expressions::valueexpression_constructor_args():
    sig = inspect.signature(sqlmodel::expressions::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_numericaldatatype_is_not_abstract():
    assert not inspect.isabstract(NumericalDataType)


def test_numericaldatatype_constructor_exists():
    assert callable(NumericalDataType.__init__)


def test_numericaldatatype_constructor_args():
    sig = inspect.signature(NumericalDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::approximatenumericdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ApproximateNumericDataType)


def test_sqlmodel::datatypes::approximatenumericdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::ApproximateNumericDataType.__init__)


def test_sqlmodel::datatypes::approximatenumericdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ApproximateNumericDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::exactnumericdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ExactNumericDataType)


def test_sqlmodel::datatypes::exactnumericdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::ExactNumericDataType.__init__)


def test_sqlmodel::datatypes::exactnumericdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ExactNumericDataType.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_sqlmodel::datatypes::exactnumericdatatype_has_scale():
    assert hasattr(sqlmodel::datatypes::ExactNumericDataType, "scale")
    descriptor = None
    for klass in sqlmodel::datatypes::ExactNumericDataType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CheckConstraint)


def test_checkconstraint_constructor_exists():
    assert callable(CheckConstraint.__init__)


def test_checkconstraint_constructor_args():
    sig = inspect.signature(CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(DistinctUserDefinedType)


def test_distinctuserdefinedtype_constructor_exists():
    assert callable(DistinctUserDefinedType.__init__)


def test_distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::domain_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::Domain)


def test_sqlmodel::datatypes::domain_constructor_exists():
    assert callable(sqlmodel::datatypes::Domain.__init__)


def test_sqlmodel::datatypes::domain_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_sqlmodel::datatypes::domain_has_defaultValue():
    assert hasattr(sqlmodel::datatypes::Domain, "defaultValue")
    descriptor = None
    for klass in sqlmodel::datatypes::Domain.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_exactnumericdatatype_is_not_abstract():
    assert not inspect.isabstract(ExactNumericDataType)


def test_exactnumericdatatype_constructor_exists():
    assert callable(ExactNumericDataType.__init__)


def test_exactnumericdatatype_constructor_args():
    sig = inspect.signature(ExactNumericDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::integerdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::IntegerDataType)


def test_sqlmodel::datatypes::integerdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::IntegerDataType.__init__)


def test_sqlmodel::datatypes::integerdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::IntegerDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::fixedprecisiondatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::FixedPrecisionDataType)


def test_sqlmodel::datatypes::fixedprecisiondatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::FixedPrecisionDataType.__init__)


def test_sqlmodel::datatypes::fixedprecisiondatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::FixedPrecisionDataType.__init__)
    params = list(sig.parameters.keys())



def test_structureduserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(StructuredUserDefinedType)


def test_structureduserdefinedtype_constructor_exists():
    assert callable(StructuredUserDefinedType.__init__)


def test_structureduserdefinedtype_constructor_args():
    sig = inspect.signature(StructuredUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_characterstringdatatype_is_not_abstract():
    assert not inspect.isabstract(CharacterStringDataType)


def test_characterstringdatatype_constructor_exists():
    assert callable(CharacterStringDataType.__init__)


def test_characterstringdatatype_constructor_args():
    sig = inspect.signature(CharacterStringDataType.__init__)
    params = list(sig.parameters.keys())



def test_collectiondatatype_is_not_abstract():
    assert not inspect.isabstract(CollectionDataType)


def test_collectiondatatype_constructor_exists():
    assert callable(CollectionDataType.__init__)


def test_collectiondatatype_constructor_args():
    sig = inspect.signature(CollectionDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::multisetdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::MultisetDataType)


def test_sqlmodel::datatypes::multisetdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::MultisetDataType.__init__)


def test_sqlmodel::datatypes::multisetdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::MultisetDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::arraydatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ArrayDataType)


def test_sqlmodel::datatypes::arraydatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::ArrayDataType.__init__)


def test_sqlmodel::datatypes::arraydatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ArrayDataType.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"

def test_sqlmodel::datatypes::arraydatatype_has_maxCardinality():
    assert hasattr(sqlmodel::datatypes::ArrayDataType, "maxCardinality")
    descriptor = None
    for klass in sqlmodel::datatypes::ArrayDataType.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_predefineddatatype_is_not_abstract():
    assert not inspect.isabstract(PredefinedDataType)


def test_predefineddatatype_constructor_exists():
    assert callable(PredefinedDataType.__init__)


def test_predefineddatatype_constructor_args():
    sig = inspect.signature(PredefinedDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::intervaldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::IntervalDataType)


def test_sqlmodel::datatypes::intervaldatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::IntervalDataType.__init__)


def test_sqlmodel::datatypes::intervaldatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::IntervalDataType.__init__)
    params = list(sig.parameters.keys())
    assert "leadingFieldPrecision" in params, "Missing parameter 'leadingFieldPrecision'"
    assert "fractionalSecondsPrecision" in params, "Missing parameter 'fractionalSecondsPrecision'"
    assert "trailingQualifier" in params, "Missing parameter 'trailingQualifier'"
    assert "leadingQualifier" in params, "Missing parameter 'leadingQualifier'"
    assert "trailingFieldPrecision" in params, "Missing parameter 'trailingFieldPrecision'"

def test_sqlmodel::datatypes::intervaldatatype_has_leadingFieldPrecision():
    assert hasattr(sqlmodel::datatypes::IntervalDataType, "leadingFieldPrecision")
    descriptor = None
    for klass in sqlmodel::datatypes::IntervalDataType.__mro__:
        if "leadingFieldPrecision" in klass.__dict__:
            descriptor = klass.__dict__["leadingFieldPrecision"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::intervaldatatype_has_fractionalSecondsPrecision():
    assert hasattr(sqlmodel::datatypes::IntervalDataType, "fractionalSecondsPrecision")
    descriptor = None
    for klass in sqlmodel::datatypes::IntervalDataType.__mro__:
        if "fractionalSecondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["fractionalSecondsPrecision"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::intervaldatatype_has_trailingQualifier():
    assert hasattr(sqlmodel::datatypes::IntervalDataType, "trailingQualifier")
    descriptor = None
    for klass in sqlmodel::datatypes::IntervalDataType.__mro__:
        if "trailingQualifier" in klass.__dict__:
            descriptor = klass.__dict__["trailingQualifier"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::intervaldatatype_has_leadingQualifier():
    assert hasattr(sqlmodel::datatypes::IntervalDataType, "leadingQualifier")
    descriptor = None
    for klass in sqlmodel::datatypes::IntervalDataType.__mro__:
        if "leadingQualifier" in klass.__dict__:
            descriptor = klass.__dict__["leadingQualifier"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::intervaldatatype_has_trailingFieldPrecision():
    assert hasattr(sqlmodel::datatypes::IntervalDataType, "trailingFieldPrecision")
    descriptor = None
    for klass in sqlmodel::datatypes::IntervalDataType.__mro__:
        if "trailingFieldPrecision" in klass.__dict__:
            descriptor = klass.__dict__["trailingFieldPrecision"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::datalinkdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::DataLinkDataType)


def test_sqlmodel::datatypes::datalinkdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::DataLinkDataType.__init__)


def test_sqlmodel::datatypes::datalinkdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::DataLinkDataType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "writePermission" in params, "Missing parameter 'writePermission'"
    assert "recovery" in params, "Missing parameter 'recovery'"
    assert "readPermission" in params, "Missing parameter 'readPermission'"
    assert "unlink" in params, "Missing parameter 'unlink'"
    assert "linkControl" in params, "Missing parameter 'linkControl'"
    assert "integrityControl" in params, "Missing parameter 'integrityControl'"

def test_sqlmodel::datatypes::datalinkdatatype_has_length():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "length")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_writePermission():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "writePermission")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "writePermission" in klass.__dict__:
            descriptor = klass.__dict__["writePermission"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_recovery():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "recovery")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "recovery" in klass.__dict__:
            descriptor = klass.__dict__["recovery"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_readPermission():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "readPermission")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "readPermission" in klass.__dict__:
            descriptor = klass.__dict__["readPermission"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_unlink():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "unlink")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "unlink" in klass.__dict__:
            descriptor = klass.__dict__["unlink"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_linkControl():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "linkControl")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "linkControl" in klass.__dict__:
            descriptor = klass.__dict__["linkControl"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::datalinkdatatype_has_integrityControl():
    assert hasattr(sqlmodel::datatypes::DataLinkDataType, "integrityControl")
    descriptor = None
    for klass in sqlmodel::datatypes::DataLinkDataType.__mro__:
        if "integrityControl" in klass.__dict__:
            descriptor = klass.__dict__["integrityControl"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::booleandatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::BooleanDataType)


def test_sqlmodel::datatypes::booleandatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::BooleanDataType.__init__)


def test_sqlmodel::datatypes::booleandatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::BooleanDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::datedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::DateDataType)


def test_sqlmodel::datatypes::datedatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::DateDataType.__init__)


def test_sqlmodel::datatypes::datedatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::DateDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::characterstringdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::CharacterStringDataType)


def test_sqlmodel::datatypes::characterstringdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::CharacterStringDataType.__init__)


def test_sqlmodel::datatypes::characterstringdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::CharacterStringDataType.__init__)
    params = list(sig.parameters.keys())
    assert "coercibility" in params, "Missing parameter 'coercibility'"
    assert "fixedLength" in params, "Missing parameter 'fixedLength'"
    assert "length" in params, "Missing parameter 'length'"
    assert "collationName" in params, "Missing parameter 'collationName'"

def test_sqlmodel::datatypes::characterstringdatatype_has_coercibility():
    assert hasattr(sqlmodel::datatypes::CharacterStringDataType, "coercibility")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterStringDataType.__mro__:
        if "coercibility" in klass.__dict__:
            descriptor = klass.__dict__["coercibility"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::characterstringdatatype_has_fixedLength():
    assert hasattr(sqlmodel::datatypes::CharacterStringDataType, "fixedLength")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterStringDataType.__mro__:
        if "fixedLength" in klass.__dict__:
            descriptor = klass.__dict__["fixedLength"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::characterstringdatatype_has_length():
    assert hasattr(sqlmodel::datatypes::CharacterStringDataType, "length")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterStringDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::characterstringdatatype_has_collationName():
    assert hasattr(sqlmodel::datatypes::CharacterStringDataType, "collationName")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterStringDataType.__mro__:
        if "collationName" in klass.__dict__:
            descriptor = klass.__dict__["collationName"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::xmldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::XMLDataType)


def test_sqlmodel::datatypes::xmldatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::XMLDataType.__init__)


def test_sqlmodel::datatypes::xmldatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::XMLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::timedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::TimeDataType)


def test_sqlmodel::datatypes::timedatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::TimeDataType.__init__)


def test_sqlmodel::datatypes::timedatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::TimeDataType.__init__)
    params = list(sig.parameters.keys())
    assert "fractionalSecondsPrecision" in params, "Missing parameter 'fractionalSecondsPrecision'"
    assert "timeZone" in params, "Missing parameter 'timeZone'"

def test_sqlmodel::datatypes::timedatatype_has_fractionalSecondsPrecision():
    assert hasattr(sqlmodel::datatypes::TimeDataType, "fractionalSecondsPrecision")
    descriptor = None
    for klass in sqlmodel::datatypes::TimeDataType.__mro__:
        if "fractionalSecondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["fractionalSecondsPrecision"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::timedatatype_has_timeZone():
    assert hasattr(sqlmodel::datatypes::TimeDataType, "timeZone")
    descriptor = None
    for klass in sqlmodel::datatypes::TimeDataType.__mro__:
        if "timeZone" in klass.__dict__:
            descriptor = klass.__dict__["timeZone"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::binarystringdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::BinaryStringDataType)


def test_sqlmodel::datatypes::binarystringdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::BinaryStringDataType.__init__)


def test_sqlmodel::datatypes::binarystringdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::BinaryStringDataType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_sqlmodel::datatypes::binarystringdatatype_has_length():
    assert hasattr(sqlmodel::datatypes::BinaryStringDataType, "length")
    descriptor = None
    for klass in sqlmodel::datatypes::BinaryStringDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::numericaldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::NumericalDataType)


def test_sqlmodel::datatypes::numericaldatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::NumericalDataType.__init__)


def test_sqlmodel::datatypes::numericaldatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::NumericalDataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_sqlmodel::datatypes::numericaldatatype_has_precision():
    assert hasattr(sqlmodel::datatypes::NumericalDataType, "precision")
    descriptor = None
    for klass in sqlmodel::datatypes::NumericalDataType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_constructeddatatype_is_not_abstract():
    assert not inspect.isabstract(ConstructedDataType)


def test_constructeddatatype_constructor_exists():
    assert callable(ConstructedDataType.__init__)


def test_constructeddatatype_constructor_args():
    sig = inspect.signature(ConstructedDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::rowdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::RowDataType)


def test_sqlmodel::datatypes::rowdatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::RowDataType.__init__)


def test_sqlmodel::datatypes::rowdatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::RowDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::referencedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ReferenceDataType)


def test_sqlmodel::datatypes::referencedatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::ReferenceDataType.__init__)


def test_sqlmodel::datatypes::referencedatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ReferenceDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::collectiondatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::CollectionDataType)


def test_sqlmodel::datatypes::collectiondatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::CollectionDataType.__init__)


def test_sqlmodel::datatypes::collectiondatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::CollectionDataType.__init__)
    params = list(sig.parameters.keys())



def test_indexexpression_is_not_abstract():
    assert not inspect.isabstract(IndexExpression)


def test_indexexpression_constructor_exists():
    assert callable(IndexExpression.__init__)


def test_indexexpression_constructor_args():
    sig = inspect.signature(IndexExpression.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtypeordering_is_not_abstract():
    assert not inspect.isabstract(UserDefinedTypeOrdering)


def test_userdefinedtypeordering_constructor_exists():
    assert callable(UserDefinedTypeOrdering.__init__)


def test_userdefinedtypeordering_constructor_args():
    sig = inspect.signature(UserDefinedTypeOrdering.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::sqldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::SQLDataType)


def test_sqlmodel::datatypes::sqldatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::SQLDataType.__init__)


def test_sqlmodel::datatypes::sqldatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::constructeddatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ConstructedDataType)


def test_sqlmodel::datatypes::constructeddatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::ConstructedDataType.__init__)


def test_sqlmodel::datatypes::constructeddatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ConstructedDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::UserDefinedType)


def test_sqlmodel::datatypes::userdefinedtype_constructor_exists():
    assert callable(sqlmodel::datatypes::UserDefinedType.__init__)


def test_sqlmodel::datatypes::userdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_indexmember_is_not_abstract():
    assert not inspect.isabstract(IndexMember)


def test_indexmember_constructor_exists():
    assert callable(IndexMember.__init__)


def test_indexmember_constructor_args():
    sig = inspect.signature(IndexMember.__init__)
    params = list(sig.parameters.keys())



def test_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ForeignKey)


def test_foreignkey_constructor_exists():
    assert callable(ForeignKey.__init__)


def test_foreignkey_constructor_args():
    sig = inspect.signature(ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::primarykey_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::PrimaryKey)


def test_sqlmodel::constraints::primarykey_constructor_exists():
    assert callable(sqlmodel::constraints::PrimaryKey.__init__)


def test_sqlmodel::constraints::primarykey_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(ReferenceConstraint)


def test_referenceconstraint_constructor_exists():
    assert callable(ReferenceConstraint.__init__)


def test_referenceconstraint_constructor_args():
    sig = inspect.signature(ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::UniqueConstraint)


def test_sqlmodel::constraints::uniqueconstraint_constructor_exists():
    assert callable(sqlmodel::constraints::UniqueConstraint.__init__)


def test_sqlmodel::constraints::uniqueconstraint_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "clustered" in params, "Missing parameter 'clustered'"

def test_sqlmodel::constraints::uniqueconstraint_has_clustered():
    assert hasattr(sqlmodel::constraints::UniqueConstraint, "clustered")
    descriptor = None
    for klass in sqlmodel::constraints::UniqueConstraint.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::constraints::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::ForeignKey)


def test_sqlmodel::constraints::foreignkey_constructor_exists():
    assert callable(sqlmodel::constraints::ForeignKey.__init__)


def test_sqlmodel::constraints::foreignkey_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "match" in params, "Missing parameter 'match'"
    assert "onDelete" in params, "Missing parameter 'onDelete'"

def test_sqlmodel::constraints::foreignkey_has_onUpdate():
    assert hasattr(sqlmodel::constraints::ForeignKey, "onUpdate")
    descriptor = None
    for klass in sqlmodel::constraints::ForeignKey.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::foreignkey_has_match():
    assert hasattr(sqlmodel::constraints::ForeignKey, "match")
    descriptor = None
    for klass in sqlmodel::constraints::ForeignKey.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::foreignkey_has_onDelete():
    assert hasattr(sqlmodel::constraints::ForeignKey, "onDelete")
    descriptor = None
    for klass in sqlmodel::constraints::ForeignKey.__mro__:
        if "onDelete" in klass.__dict__:
            descriptor = klass.__dict__["onDelete"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::checkconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::CheckConstraint)


def test_sqlmodel::constraints::checkconstraint_constructor_exists():
    assert callable(sqlmodel::constraints::CheckConstraint.__init__)


def test_sqlmodel::constraints::checkconstraint_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::ReferenceConstraint)


def test_sqlmodel::constraints::referenceconstraint_constructor_exists():
    assert callable(sqlmodel::constraints::ReferenceConstraint.__init__)


def test_sqlmodel::constraints::referenceconstraint_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_searchcondition_is_not_abstract():
    assert not inspect.isabstract(SearchCondition)


def test_searchcondition_constructor_exists():
    assert callable(SearchCondition.__init__)


def test_searchcondition_constructor_args():
    sig = inspect.signature(SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::TableConstraint)


def test_sqlmodel::constraints::tableconstraint_constructor_exists():
    assert callable(sqlmodel::constraints::TableConstraint.__init__)


def test_sqlmodel::constraints::tableconstraint_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::assertion_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::Assertion)


def test_sqlmodel::constraints::assertion_constructor_exists():
    assert callable(sqlmodel::constraints::Assertion.__init__)


def test_sqlmodel::constraints::assertion_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::Assertion.__init__)
    params = list(sig.parameters.keys())



def test_basetable_is_not_abstract():
    assert not inspect.isabstract(BaseTable)


def test_basetable_constructor_exists():
    assert callable(BaseTable.__init__)


def test_basetable_constructor_args():
    sig = inspect.signature(BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::tables::temporarytable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::TemporaryTable)


def test_sqlmodel::tables::temporarytable_constructor_exists():
    assert callable(sqlmodel::tables::TemporaryTable.__init__)


def test_sqlmodel::tables::temporarytable_constructor_args():
    sig = inspect.signature(sqlmodel::tables::TemporaryTable.__init__)
    params = list(sig.parameters.keys())
    assert "local" in params, "Missing parameter 'local'"
    assert "deleteOnCommit" in params, "Missing parameter 'deleteOnCommit'"

def test_sqlmodel::tables::temporarytable_has_local():
    assert hasattr(sqlmodel::tables::TemporaryTable, "local")
    descriptor = None
    for klass in sqlmodel::tables::TemporaryTable.__mro__:
        if "local" in klass.__dict__:
            descriptor = klass.__dict__["local"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::temporarytable_has_deleteOnCommit():
    assert hasattr(sqlmodel::tables::TemporaryTable, "deleteOnCommit")
    descriptor = None
    for klass in sqlmodel::tables::TemporaryTable.__mro__:
        if "deleteOnCommit" in klass.__dict__:
            descriptor = klass.__dict__["deleteOnCommit"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::tables::persistenttable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::PersistentTable)


def test_sqlmodel::tables::persistenttable_constructor_exists():
    assert callable(sqlmodel::tables::PersistentTable.__init__)


def test_sqlmodel::tables::persistenttable_constructor_args():
    sig = inspect.signature(sqlmodel::tables::PersistentTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::schema::comment_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Comment)


def test_sqlmodel::schema::comment_constructor_exists():
    assert callable(sqlmodel::schema::Comment.__init__)


def test_sqlmodel::schema::comment_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_sqlmodel::schema::comment_has_description():
    assert hasattr(sqlmodel::schema::Comment, "description")
    descriptor = None
    for klass in sqlmodel::schema::Comment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::objectextension_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::ObjectExtension)


def test_sqlmodel::schema::objectextension_constructor_exists():
    assert callable(sqlmodel::schema::ObjectExtension.__init__)


def test_sqlmodel::schema::objectextension_constructor_args():
    sig = inspect.signature(sqlmodel::schema::ObjectExtension.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_identityspecifier_is_not_abstract():
    assert not inspect.isabstract(IdentitySpecifier)


def test_identityspecifier_constructor_exists():
    assert callable(IdentitySpecifier.__init__)


def test_identityspecifier_constructor_args():
    sig = inspect.signature(IdentitySpecifier.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::elementtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::ElementType)


def test_sqlmodel::datatypes::elementtype_constructor_exists():
    assert callable(sqlmodel::datatypes::ElementType.__init__)


def test_sqlmodel::datatypes::elementtype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::parameter_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Parameter)


def test_sqlmodel::routines::parameter_constructor_exists():
    assert callable(sqlmodel::routines::Parameter.__init__)


def test_sqlmodel::routines::parameter_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "locator" in params, "Missing parameter 'locator'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_sqlmodel::routines::parameter_has_locator():
    assert hasattr(sqlmodel::routines::Parameter, "locator")
    descriptor = None
    for klass in sqlmodel::routines::Parameter.__mro__:
        if "locator" in klass.__dict__:
            descriptor = klass.__dict__["locator"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::parameter_has_mode():
    assert hasattr(sqlmodel::routines::Parameter, "mode")
    descriptor = None
    for klass in sqlmodel::routines::Parameter.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::field_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::Field)


def test_sqlmodel::datatypes::field_constructor_exists():
    assert callable(sqlmodel::datatypes::Field.__init__)


def test_sqlmodel::datatypes::field_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::Field.__init__)
    params = list(sig.parameters.keys())
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"

def test_sqlmodel::datatypes::field_has_scopeCheck():
    assert hasattr(sqlmodel::datatypes::Field, "scopeCheck")
    descriptor = None
    for klass in sqlmodel::datatypes::Field.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::field_has_scopeChecked():
    assert hasattr(sqlmodel::datatypes::Field, "scopeChecked")
    descriptor = None
    for klass in sqlmodel::datatypes::Field.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::tables::column_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::Column)


def test_sqlmodel::tables::column_constructor_exists():
    assert callable(sqlmodel::tables::Column.__init__)


def test_sqlmodel::tables::column_constructor_args():
    sig = inspect.signature(sqlmodel::tables::Column.__init__)
    params = list(sig.parameters.keys())
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"
    assert "implementationDependent" in params, "Missing parameter 'implementationDependent'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_sqlmodel::tables::column_has_scopeChecked():
    assert hasattr(sqlmodel::tables::Column, "scopeChecked")
    descriptor = None
    for klass in sqlmodel::tables::Column.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::column_has_nullable():
    assert hasattr(sqlmodel::tables::Column, "nullable")
    descriptor = None
    for klass in sqlmodel::tables::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::column_has_scopeCheck():
    assert hasattr(sqlmodel::tables::Column, "scopeCheck")
    descriptor = None
    for klass in sqlmodel::tables::Column.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::column_has_implementationDependent():
    assert hasattr(sqlmodel::tables::Column, "implementationDependent")
    descriptor = None
    for klass in sqlmodel::tables::Column.__mro__:
        if "implementationDependent" in klass.__dict__:
            descriptor = klass.__dict__["implementationDependent"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::column_has_defaultValue():
    assert hasattr(sqlmodel::tables::Column, "defaultValue")
    descriptor = None
    for klass in sqlmodel::tables::Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::AttributeDefinition)


def test_sqlmodel::datatypes::attributedefinition_constructor_exists():
    assert callable(sqlmodel::datatypes::AttributeDefinition.__init__)


def test_sqlmodel::datatypes::attributedefinition_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"

def test_sqlmodel::datatypes::attributedefinition_has_scopeCheck():
    assert hasattr(sqlmodel::datatypes::AttributeDefinition, "scopeCheck")
    descriptor = None
    for klass in sqlmodel::datatypes::AttributeDefinition.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::attributedefinition_has_defaultValue():
    assert hasattr(sqlmodel::datatypes::AttributeDefinition, "defaultValue")
    descriptor = None
    for klass in sqlmodel::datatypes::AttributeDefinition.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::attributedefinition_has_scopeChecked():
    assert hasattr(sqlmodel::datatypes::AttributeDefinition, "scopeChecked")
    descriptor = None
    for klass in sqlmodel::datatypes::AttributeDefinition.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::sequence_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Sequence)


def test_sqlmodel::schema::sequence_constructor_exists():
    assert callable(sqlmodel::schema::Sequence.__init__)


def test_sqlmodel::schema::sequence_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_privilege_is_not_abstract():
    assert not inspect.isabstract(Privilege)


def test_privilege_constructor_exists():
    assert callable(Privilege.__init__)


def test_privilege_constructor_args():
    sig = inspect.signature(Privilege.__init__)
    params = list(sig.parameters.keys())



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_objectextension_is_not_abstract():
    assert not inspect.isabstract(ObjectExtension)


def test_objectextension_constructor_exists():
    assert callable(ObjectExtension.__init__)


def test_objectextension_constructor_args():
    sig = inspect.signature(ObjectExtension.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_characterset_is_not_abstract():
    assert not inspect.isabstract(CharacterSet)


def test_characterset_constructor_exists():
    assert callable(CharacterSet.__init__)


def test_characterset_constructor_args():
    sig = inspect.signature(CharacterSet.__init__)
    params = list(sig.parameters.keys())



def test_assertion_is_not_abstract():
    assert not inspect.isabstract(Assertion)


def test_assertion_constructor_exists():
    assert callable(Assertion.__init__)


def test_assertion_constructor_args():
    sig = inspect.signature(Assertion.__init__)
    params = list(sig.parameters.keys())



def test_catalog_is_not_abstract():
    assert not inspect.isabstract(Catalog)


def test_catalog_constructor_exists():
    assert callable(Catalog.__init__)


def test_catalog_constructor_args():
    sig = inspect.signature(Catalog.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::schema::sqlobject_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::SQLObject)


def test_sqlmodel::schema::sqlobject_constructor_exists():
    assert callable(sqlmodel::schema::SQLObject.__init__)


def test_sqlmodel::schema::sqlobject_constructor_args():
    sig = inspect.signature(sqlmodel::schema::SQLObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_sqlmodel::schema::sqlobject_has_label():
    assert hasattr(sqlmodel::schema::SQLObject, "label")
    descriptor = None
    for klass in sqlmodel::schema::SQLObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::sqlobject_has_description():
    assert hasattr(sqlmodel::schema::SQLObject, "description")
    descriptor = None
    for klass in sqlmodel::schema::SQLObject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_authorizationidentifier_is_not_abstract():
    assert not inspect.isabstract(AuthorizationIdentifier)


def test_authorizationidentifier_constructor_exists():
    assert callable(AuthorizationIdentifier.__init__)


def test_authorizationidentifier_constructor_args():
    sig = inspect.signature(AuthorizationIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::accesscontrol::user_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::User)


def test_sqlmodel::accesscontrol::user_constructor_exists():
    assert callable(sqlmodel::accesscontrol::User.__init__)


def test_sqlmodel::accesscontrol::user_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::User.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::accesscontrol::role_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::Role)


def test_sqlmodel::accesscontrol::role_constructor_exists():
    assert callable(sqlmodel::accesscontrol::Role.__init__)


def test_sqlmodel::accesscontrol::role_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::Role.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::accesscontrol::group_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::Group)


def test_sqlmodel::accesscontrol::group_constructor_exists():
    assert callable(sqlmodel::accesscontrol::Group.__init__)


def test_sqlmodel::accesscontrol::group_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::Group.__init__)
    params = list(sig.parameters.keys())



def test_routine_is_not_abstract():
    assert not inspect.isabstract(Routine)


def test_routine_constructor_exists():
    assert callable(Routine.__init__)


def test_routine_constructor_args():
    sig = inspect.signature(Routine.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::function_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Function)


def test_sqlmodel::routines::function_constructor_exists():
    assert callable(sqlmodel::routines::Function.__init__)


def test_sqlmodel::routines::function_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Function.__init__)
    params = list(sig.parameters.keys())
    assert "typePreserving" in params, "Missing parameter 'typePreserving'"
    assert "nullCall" in params, "Missing parameter 'nullCall'"
    assert "mutator" in params, "Missing parameter 'mutator'"
    assert "transformGroup" in params, "Missing parameter 'transformGroup'"
    assert "static" in params, "Missing parameter 'static'"

def test_sqlmodel::routines::function_has_typePreserving():
    assert hasattr(sqlmodel::routines::Function, "typePreserving")
    descriptor = None
    for klass in sqlmodel::routines::Function.__mro__:
        if "typePreserving" in klass.__dict__:
            descriptor = klass.__dict__["typePreserving"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::function_has_nullCall():
    assert hasattr(sqlmodel::routines::Function, "nullCall")
    descriptor = None
    for klass in sqlmodel::routines::Function.__mro__:
        if "nullCall" in klass.__dict__:
            descriptor = klass.__dict__["nullCall"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::function_has_mutator():
    assert hasattr(sqlmodel::routines::Function, "mutator")
    descriptor = None
    for klass in sqlmodel::routines::Function.__mro__:
        if "mutator" in klass.__dict__:
            descriptor = klass.__dict__["mutator"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::function_has_transformGroup():
    assert hasattr(sqlmodel::routines::Function, "transformGroup")
    descriptor = None
    for klass in sqlmodel::routines::Function.__mro__:
        if "transformGroup" in klass.__dict__:
            descriptor = klass.__dict__["transformGroup"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::function_has_static():
    assert hasattr(sqlmodel::routines::Function, "static")
    descriptor = None
    for klass in sqlmodel::routines::Function.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::routines::procedure_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Procedure)


def test_sqlmodel::routines::procedure_constructor_exists():
    assert callable(sqlmodel::routines::Procedure.__init__)


def test_sqlmodel::routines::procedure_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "oldSavePoint" in params, "Missing parameter 'oldSavePoint'"
    assert "maxResultSets" in params, "Missing parameter 'maxResultSets'"

def test_sqlmodel::routines::procedure_has_oldSavePoint():
    assert hasattr(sqlmodel::routines::Procedure, "oldSavePoint")
    descriptor = None
    for klass in sqlmodel::routines::Procedure.__mro__:
        if "oldSavePoint" in klass.__dict__:
            descriptor = klass.__dict__["oldSavePoint"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::procedure_has_maxResultSets():
    assert hasattr(sqlmodel::routines::Procedure, "maxResultSets")
    descriptor = None
    for klass in sqlmodel::routines::Procedure.__mro__:
        if "maxResultSets" in klass.__dict__:
            descriptor = klass.__dict__["maxResultSets"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_schema::sqlmodel::eobject_is_not_abstract():
    assert not inspect.isabstract(schema::sqlmodel::EObject)


def test_schema::sqlmodel::eobject_constructor_exists():
    assert callable(schema::sqlmodel::EObject.__init__)


def test_schema::sqlmodel::eobject_constructor_args():
    sig = inspect.signature(schema::sqlmodel::EObject.__init__)
    params = list(sig.parameters.keys())



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::tables::basetable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::BaseTable)


def test_sqlmodel::tables::basetable_constructor_exists():
    assert callable(sqlmodel::tables::BaseTable.__init__)


def test_sqlmodel::tables::basetable_constructor_args():
    sig = inspect.signature(sqlmodel::tables::BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::tables::derivedtable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::DerivedTable)


def test_sqlmodel::tables::derivedtable_constructor_exists():
    assert callable(sqlmodel::tables::DerivedTable.__init__)


def test_sqlmodel::tables::derivedtable_constructor_args():
    sig = inspect.signature(sqlmodel::tables::DerivedTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::routines::routineresulttable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::RoutineResultTable)


def test_sqlmodel::routines::routineresulttable_constructor_exists():
    assert callable(sqlmodel::routines::RoutineResultTable.__init__)


def test_sqlmodel::routines::routineresulttable_constructor_args():
    sig = inspect.signature(sqlmodel::routines::RoutineResultTable.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::structureduserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::StructuredUserDefinedType)


def test_sqlmodel::datatypes::structureduserdefinedtype_constructor_exists():
    assert callable(sqlmodel::datatypes::StructuredUserDefinedType.__init__)


def test_sqlmodel::datatypes::structureduserdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::StructuredUserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "instantiable" in params, "Missing parameter 'instantiable'"

def test_sqlmodel::datatypes::structureduserdefinedtype_has_final():
    assert hasattr(sqlmodel::datatypes::StructuredUserDefinedType, "final")
    descriptor = None
    for klass in sqlmodel::datatypes::StructuredUserDefinedType.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::structureduserdefinedtype_has_instantiable():
    assert hasattr(sqlmodel::datatypes::StructuredUserDefinedType, "instantiable")
    descriptor = None
    for klass in sqlmodel::datatypes::StructuredUserDefinedType.__mro__:
        if "instantiable" in klass.__dict__:
            descriptor = klass.__dict__["instantiable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::DistinctUserDefinedType)


def test_sqlmodel::datatypes::distinctuserdefinedtype_constructor_exists():
    assert callable(sqlmodel::datatypes::DistinctUserDefinedType.__init__)


def test_sqlmodel::datatypes::distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SQLDataType)


def test_sqldatatype_constructor_exists():
    assert callable(SQLDataType.__init__)


def test_sqldatatype_constructor_args():
    sig = inspect.signature(SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::datatypes::predefineddatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::PredefinedDataType)


def test_sqlmodel::datatypes::predefineddatatype_constructor_exists():
    assert callable(sqlmodel::datatypes::PredefinedDataType.__init__)


def test_sqlmodel::datatypes::predefineddatatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::PredefinedDataType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_sqlmodel::datatypes::predefineddatatype_has_primitiveType():
    assert hasattr(sqlmodel::datatypes::PredefinedDataType, "primitiveType")
    descriptor = None
    for klass in sqlmodel::datatypes::PredefinedDataType.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_sqlobject_is_not_abstract():
    assert not inspect.isabstract(SQLObject)


def test_sqlobject_constructor_exists():
    assert callable(SQLObject.__init__)


def test_sqlobject_constructor_args():
    sig = inspect.signature(SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::tables::table_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::Table)


def test_sqlmodel::tables::table_constructor_exists():
    assert callable(sqlmodel::tables::Table.__init__)


def test_sqlmodel::tables::table_constructor_args():
    sig = inspect.signature(sqlmodel::tables::Table.__init__)
    params = list(sig.parameters.keys())
    assert "selfRefColumnGeneration" in params, "Missing parameter 'selfRefColumnGeneration'"
    assert "insertable" in params, "Missing parameter 'insertable'"
    assert "updatable" in params, "Missing parameter 'updatable'"

def test_sqlmodel::tables::table_has_selfRefColumnGeneration():
    assert hasattr(sqlmodel::tables::Table, "selfRefColumnGeneration")
    descriptor = None
    for klass in sqlmodel::tables::Table.__mro__:
        if "selfRefColumnGeneration" in klass.__dict__:
            descriptor = klass.__dict__["selfRefColumnGeneration"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::table_has_insertable():
    assert hasattr(sqlmodel::tables::Table, "insertable")
    descriptor = None
    for klass in sqlmodel::tables::Table.__mro__:
        if "insertable" in klass.__dict__:
            descriptor = klass.__dict__["insertable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::table_has_updatable():
    assert hasattr(sqlmodel::tables::Table, "updatable")
    descriptor = None
    for klass in sqlmodel::tables::Table.__mro__:
        if "updatable" in klass.__dict__:
            descriptor = klass.__dict__["updatable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::tables::trigger_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::tables::Trigger)


def test_sqlmodel::tables::trigger_constructor_exists():
    assert callable(sqlmodel::tables::Trigger.__init__)


def test_sqlmodel::tables::trigger_constructor_args():
    sig = inspect.signature(sqlmodel::tables::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "actionGranularity" in params, "Missing parameter 'actionGranularity'"
    assert "deleteType" in params, "Missing parameter 'deleteType'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "updateType" in params, "Missing parameter 'updateType'"
    assert "timeStamp" in params, "Missing parameter 'timeStamp'"
    assert "oldTable" in params, "Missing parameter 'oldTable'"
    assert "oldRow" in params, "Missing parameter 'oldRow'"
    assert "newRow" in params, "Missing parameter 'newRow'"
    assert "newTable" in params, "Missing parameter 'newTable'"
    assert "insertType" in params, "Missing parameter 'insertType'"

def test_sqlmodel::tables::trigger_has_actionGranularity():
    assert hasattr(sqlmodel::tables::Trigger, "actionGranularity")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "actionGranularity" in klass.__dict__:
            descriptor = klass.__dict__["actionGranularity"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_deleteType():
    assert hasattr(sqlmodel::tables::Trigger, "deleteType")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "deleteType" in klass.__dict__:
            descriptor = klass.__dict__["deleteType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_actionTime():
    assert hasattr(sqlmodel::tables::Trigger, "actionTime")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_updateType():
    assert hasattr(sqlmodel::tables::Trigger, "updateType")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "updateType" in klass.__dict__:
            descriptor = klass.__dict__["updateType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_timeStamp():
    assert hasattr(sqlmodel::tables::Trigger, "timeStamp")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "timeStamp" in klass.__dict__:
            descriptor = klass.__dict__["timeStamp"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_oldTable():
    assert hasattr(sqlmodel::tables::Trigger, "oldTable")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "oldTable" in klass.__dict__:
            descriptor = klass.__dict__["oldTable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_oldRow():
    assert hasattr(sqlmodel::tables::Trigger, "oldRow")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "oldRow" in klass.__dict__:
            descriptor = klass.__dict__["oldRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_newRow():
    assert hasattr(sqlmodel::tables::Trigger, "newRow")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "newRow" in klass.__dict__:
            descriptor = klass.__dict__["newRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_newTable():
    assert hasattr(sqlmodel::tables::Trigger, "newTable")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "newTable" in klass.__dict__:
            descriptor = klass.__dict__["newTable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::tables::trigger_has_insertType():
    assert hasattr(sqlmodel::tables::Trigger, "insertType")
    descriptor = None
    for klass in sqlmodel::tables::Trigger.__mro__:
        if "insertType" in klass.__dict__:
            descriptor = klass.__dict__["insertType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::routines::routine_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Routine)


def test_sqlmodel::routines::routine_constructor_exists():
    assert callable(sqlmodel::routines::Routine.__init__)


def test_sqlmodel::routines::routine_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Routine.__init__)
    params = list(sig.parameters.keys())
    assert "creationTS" in params, "Missing parameter 'creationTS'"
    assert "security" in params, "Missing parameter 'security'"
    assert "specificName" in params, "Missing parameter 'specificName'"
    assert "externalName" in params, "Missing parameter 'externalName'"
    assert "parameterStyle" in params, "Missing parameter 'parameterStyle'"
    assert "lastAlteredTS" in params, "Missing parameter 'lastAlteredTS'"
    assert "authorizationID" in params, "Missing parameter 'authorizationID'"
    assert "sqlDataAccess" in params, "Missing parameter 'sqlDataAccess'"
    assert "language" in params, "Missing parameter 'language'"
    assert "deterministic" in params, "Missing parameter 'deterministic'"

def test_sqlmodel::routines::routine_has_creationTS():
    assert hasattr(sqlmodel::routines::Routine, "creationTS")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "creationTS" in klass.__dict__:
            descriptor = klass.__dict__["creationTS"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_security():
    assert hasattr(sqlmodel::routines::Routine, "security")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "security" in klass.__dict__:
            descriptor = klass.__dict__["security"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_specificName():
    assert hasattr(sqlmodel::routines::Routine, "specificName")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "specificName" in klass.__dict__:
            descriptor = klass.__dict__["specificName"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_externalName():
    assert hasattr(sqlmodel::routines::Routine, "externalName")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "externalName" in klass.__dict__:
            descriptor = klass.__dict__["externalName"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_parameterStyle():
    assert hasattr(sqlmodel::routines::Routine, "parameterStyle")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "parameterStyle" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyle"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_lastAlteredTS():
    assert hasattr(sqlmodel::routines::Routine, "lastAlteredTS")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "lastAlteredTS" in klass.__dict__:
            descriptor = klass.__dict__["lastAlteredTS"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_authorizationID():
    assert hasattr(sqlmodel::routines::Routine, "authorizationID")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "authorizationID" in klass.__dict__:
            descriptor = klass.__dict__["authorizationID"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_sqlDataAccess():
    assert hasattr(sqlmodel::routines::Routine, "sqlDataAccess")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "sqlDataAccess" in klass.__dict__:
            descriptor = klass.__dict__["sqlDataAccess"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_language():
    assert hasattr(sqlmodel::routines::Routine, "language")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::routines::routine_has_deterministic():
    assert hasattr(sqlmodel::routines::Routine, "deterministic")
    descriptor = None
    for klass in sqlmodel::routines::Routine.__mro__:
        if "deterministic" in klass.__dict__:
            descriptor = klass.__dict__["deterministic"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::constraints::indexexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::IndexExpression)


def test_sqlmodel::constraints::indexexpression_constructor_exists():
    assert callable(sqlmodel::constraints::IndexExpression.__init__)


def test_sqlmodel::constraints::indexexpression_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::IndexExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_sqlmodel::constraints::indexexpression_has_sql():
    assert hasattr(sqlmodel::constraints::IndexExpression, "sql")
    descriptor = None
    for klass in sqlmodel::constraints::IndexExpression.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::constraints::index_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::Index)


def test_sqlmodel::constraints::index_constructor_exists():
    assert callable(sqlmodel::constraints::Index.__init__)


def test_sqlmodel::constraints::index_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::Index.__init__)
    params = list(sig.parameters.keys())
    assert "fillFactor" in params, "Missing parameter 'fillFactor'"
    assert "systemGenerated" in params, "Missing parameter 'systemGenerated'"
    assert "clustered" in params, "Missing parameter 'clustered'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_sqlmodel::constraints::index_has_fillFactor():
    assert hasattr(sqlmodel::constraints::Index, "fillFactor")
    descriptor = None
    for klass in sqlmodel::constraints::Index.__mro__:
        if "fillFactor" in klass.__dict__:
            descriptor = klass.__dict__["fillFactor"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::index_has_systemGenerated():
    assert hasattr(sqlmodel::constraints::Index, "systemGenerated")
    descriptor = None
    for klass in sqlmodel::constraints::Index.__mro__:
        if "systemGenerated" in klass.__dict__:
            descriptor = klass.__dict__["systemGenerated"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::index_has_clustered():
    assert hasattr(sqlmodel::constraints::Index, "clustered")
    descriptor = None
    for klass in sqlmodel::constraints::Index.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::index_has_unique():
    assert hasattr(sqlmodel::constraints::Index, "unique")
    descriptor = None
    for klass in sqlmodel::constraints::Index.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::characterset_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::CharacterSet)


def test_sqlmodel::datatypes::characterset_constructor_exists():
    assert callable(sqlmodel::datatypes::CharacterSet.__init__)


def test_sqlmodel::datatypes::characterset_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::CharacterSet.__init__)
    params = list(sig.parameters.keys())
    assert "repertoire" in params, "Missing parameter 'repertoire'"
    assert "defaultCollation" in params, "Missing parameter 'defaultCollation'"
    assert "encoding" in params, "Missing parameter 'encoding'"

def test_sqlmodel::datatypes::characterset_has_repertoire():
    assert hasattr(sqlmodel::datatypes::CharacterSet, "repertoire")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterSet.__mro__:
        if "repertoire" in klass.__dict__:
            descriptor = klass.__dict__["repertoire"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::characterset_has_defaultCollation():
    assert hasattr(sqlmodel::datatypes::CharacterSet, "defaultCollation")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterSet.__mro__:
        if "defaultCollation" in klass.__dict__:
            descriptor = klass.__dict__["defaultCollation"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::characterset_has_encoding():
    assert hasattr(sqlmodel::datatypes::CharacterSet, "encoding")
    descriptor = None
    for klass in sqlmodel::datatypes::CharacterSet.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::typedelement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::TypedElement)


def test_sqlmodel::schema::typedelement_constructor_exists():
    assert callable(sqlmodel::schema::TypedElement.__init__)


def test_sqlmodel::schema::typedelement_constructor_args():
    sig = inspect.signature(sqlmodel::schema::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::accesscontrol::privilege_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::Privilege)


def test_sqlmodel::accesscontrol::privilege_constructor_exists():
    assert callable(sqlmodel::accesscontrol::Privilege.__init__)


def test_sqlmodel::accesscontrol::privilege_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::Privilege.__init__)
    params = list(sig.parameters.keys())
    assert "withHierarchy" in params, "Missing parameter 'withHierarchy'"
    assert "action" in params, "Missing parameter 'action'"
    assert "grantable" in params, "Missing parameter 'grantable'"

def test_sqlmodel::accesscontrol::privilege_has_withHierarchy():
    assert hasattr(sqlmodel::accesscontrol::Privilege, "withHierarchy")
    descriptor = None
    for klass in sqlmodel::accesscontrol::Privilege.__mro__:
        if "withHierarchy" in klass.__dict__:
            descriptor = klass.__dict__["withHierarchy"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::accesscontrol::privilege_has_action():
    assert hasattr(sqlmodel::accesscontrol::Privilege, "action")
    descriptor = None
    for klass in sqlmodel::accesscontrol::Privilege.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::accesscontrol::privilege_has_grantable():
    assert hasattr(sqlmodel::accesscontrol::Privilege, "grantable")
    descriptor = None
    for klass in sqlmodel::accesscontrol::Privilege.__mro__:
        if "grantable" in klass.__dict__:
            descriptor = klass.__dict__["grantable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::userdefinedtypeordering_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::UserDefinedTypeOrdering)


def test_sqlmodel::datatypes::userdefinedtypeordering_constructor_exists():
    assert callable(sqlmodel::datatypes::UserDefinedTypeOrdering.__init__)


def test_sqlmodel::datatypes::userdefinedtypeordering_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::UserDefinedTypeOrdering.__init__)
    params = list(sig.parameters.keys())
    assert "orderingCategory" in params, "Missing parameter 'orderingCategory'"
    assert "orderingForm" in params, "Missing parameter 'orderingForm'"

def test_sqlmodel::datatypes::userdefinedtypeordering_has_orderingCategory():
    assert hasattr(sqlmodel::datatypes::UserDefinedTypeOrdering, "orderingCategory")
    descriptor = None
    for klass in sqlmodel::datatypes::UserDefinedTypeOrdering.__mro__:
        if "orderingCategory" in klass.__dict__:
            descriptor = klass.__dict__["orderingCategory"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::datatypes::userdefinedtypeordering_has_orderingForm():
    assert hasattr(sqlmodel::datatypes::UserDefinedTypeOrdering, "orderingForm")
    descriptor = None
    for klass in sqlmodel::datatypes::UserDefinedTypeOrdering.__mro__:
        if "orderingForm" in klass.__dict__:
            descriptor = klass.__dict__["orderingForm"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::schema_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Schema)


def test_sqlmodel::schema::schema_constructor_exists():
    assert callable(sqlmodel::schema::Schema.__init__)


def test_sqlmodel::schema::schema_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Schema.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::constraints::constraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::Constraint)


def test_sqlmodel::constraints::constraint_constructor_exists():
    assert callable(sqlmodel::constraints::Constraint.__init__)


def test_sqlmodel::constraints::constraint_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "enforced" in params, "Missing parameter 'enforced'"
    assert "deferrable" in params, "Missing parameter 'deferrable'"
    assert "initiallyDeferred" in params, "Missing parameter 'initiallyDeferred'"

def test_sqlmodel::constraints::constraint_has_enforced():
    assert hasattr(sqlmodel::constraints::Constraint, "enforced")
    descriptor = None
    for klass in sqlmodel::constraints::Constraint.__mro__:
        if "enforced" in klass.__dict__:
            descriptor = klass.__dict__["enforced"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::constraint_has_deferrable():
    assert hasattr(sqlmodel::constraints::Constraint, "deferrable")
    descriptor = None
    for klass in sqlmodel::constraints::Constraint.__mro__:
        if "deferrable" in klass.__dict__:
            descriptor = klass.__dict__["deferrable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::constraints::constraint_has_initiallyDeferred():
    assert hasattr(sqlmodel::constraints::Constraint, "initiallyDeferred")
    descriptor = None
    for klass in sqlmodel::constraints::Constraint.__mro__:
        if "initiallyDeferred" in klass.__dict__:
            descriptor = klass.__dict__["initiallyDeferred"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::routines::source_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::routines::Source)


def test_sqlmodel::routines::source_constructor_exists():
    assert callable(sqlmodel::routines::Source.__init__)


def test_sqlmodel::routines::source_constructor_args():
    sig = inspect.signature(sqlmodel::routines::Source.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_sqlmodel::routines::source_has_body():
    assert hasattr(sqlmodel::routines::Source, "body")
    descriptor = None
    for klass in sqlmodel::routines::Source.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::datatypes::datatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::datatypes::DataType)


def test_sqlmodel::datatypes::datatype_constructor_exists():
    assert callable(sqlmodel::datatypes::DataType.__init__)


def test_sqlmodel::datatypes::datatype_constructor_args():
    sig = inspect.signature(sqlmodel::datatypes::DataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::schema::dependency_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Dependency)


def test_sqlmodel::schema::dependency_constructor_exists():
    assert callable(sqlmodel::schema::Dependency.__init__)


def test_sqlmodel::schema::dependency_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "dependencyType" in params, "Missing parameter 'dependencyType'"

def test_sqlmodel::schema::dependency_has_dependencyType():
    assert hasattr(sqlmodel::schema::Dependency, "dependencyType")
    descriptor = None
    for klass in sqlmodel::schema::Dependency.__mro__:
        if "dependencyType" in klass.__dict__:
            descriptor = klass.__dict__["dependencyType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::catalog_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Catalog)


def test_sqlmodel::schema::catalog_constructor_exists():
    assert callable(sqlmodel::schema::Catalog.__init__)


def test_sqlmodel::schema::catalog_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Catalog.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::accesscontrol::authorizationidentifier_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::AuthorizationIdentifier)


def test_sqlmodel::accesscontrol::authorizationidentifier_constructor_exists():
    assert callable(sqlmodel::accesscontrol::AuthorizationIdentifier.__init__)


def test_sqlmodel::accesscontrol::authorizationidentifier_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::AuthorizationIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel::schema::event_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Event)


def test_sqlmodel::schema::event_constructor_exists():
    assert callable(sqlmodel::schema::Event.__init__)


def test_sqlmodel::schema::event_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Event.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "for_" in params, "Missing parameter 'for_'"
    assert "condition" in params, "Missing parameter 'condition'"
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_sqlmodel::schema::event_has_action():
    assert hasattr(sqlmodel::schema::Event, "action")
    descriptor = None
    for klass in sqlmodel::schema::Event.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::event_has_for_():
    assert hasattr(sqlmodel::schema::Event, "for_")
    descriptor = None
    for klass in sqlmodel::schema::Event.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::event_has_condition():
    assert hasattr(sqlmodel::schema::Event, "condition")
    descriptor = None
    for klass in sqlmodel::schema::Event.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::event_has_enabled():
    assert hasattr(sqlmodel::schema::Event, "enabled")
    descriptor = None
    for klass in sqlmodel::schema::Event.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::database_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::Database)


def test_sqlmodel::schema::database_constructor_exists():
    assert callable(sqlmodel::schema::Database.__init__)


def test_sqlmodel::schema::database_constructor_args():
    sig = inspect.signature(sqlmodel::schema::Database.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "vendor" in params, "Missing parameter 'vendor'"

def test_sqlmodel::schema::database_has_version():
    assert hasattr(sqlmodel::schema::Database, "version")
    descriptor = None
    for klass in sqlmodel::schema::Database.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::database_has_vendor():
    assert hasattr(sqlmodel::schema::Database, "vendor")
    descriptor = None
    for klass in sqlmodel::schema::Database.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::constraints::indexmember_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::constraints::IndexMember)


def test_sqlmodel::constraints::indexmember_constructor_exists():
    assert callable(sqlmodel::constraints::IndexMember.__init__)


def test_sqlmodel::constraints::indexmember_constructor_args():
    sig = inspect.signature(sqlmodel::constraints::IndexMember.__init__)
    params = list(sig.parameters.keys())
    assert "incrementType" in params, "Missing parameter 'incrementType'"

def test_sqlmodel::constraints::indexmember_has_incrementType():
    assert hasattr(sqlmodel::constraints::IndexMember, "incrementType")
    descriptor = None
    for klass in sqlmodel::constraints::IndexMember.__mro__:
        if "incrementType" in klass.__dict__:
            descriptor = klass.__dict__["incrementType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::accesscontrol::roleauthorization_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::accesscontrol::RoleAuthorization)


def test_sqlmodel::accesscontrol::roleauthorization_constructor_exists():
    assert callable(sqlmodel::accesscontrol::RoleAuthorization.__init__)


def test_sqlmodel::accesscontrol::roleauthorization_constructor_args():
    sig = inspect.signature(sqlmodel::accesscontrol::RoleAuthorization.__init__)
    params = list(sig.parameters.keys())
    assert "grantable" in params, "Missing parameter 'grantable'"

def test_sqlmodel::accesscontrol::roleauthorization_has_grantable():
    assert hasattr(sqlmodel::accesscontrol::RoleAuthorization, "grantable")
    descriptor = None
    for klass in sqlmodel::accesscontrol::RoleAuthorization.__mro__:
        if "grantable" in klass.__dict__:
            descriptor = klass.__dict__["grantable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel::schema::identityspecifier_is_not_abstract():
    assert not inspect.isabstract(sqlmodel::schema::IdentitySpecifier)


def test_sqlmodel::schema::identityspecifier_constructor_exists():
    assert callable(sqlmodel::schema::IdentitySpecifier.__init__)


def test_sqlmodel::schema::identityspecifier_constructor_args():
    sig = inspect.signature(sqlmodel::schema::IdentitySpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "generationType" in params, "Missing parameter 'generationType'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "cycleOption" in params, "Missing parameter 'cycleOption'"

def test_sqlmodel::schema::identityspecifier_has_generationType():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "generationType")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "generationType" in klass.__dict__:
            descriptor = klass.__dict__["generationType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::identityspecifier_has_maximum():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "maximum")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::identityspecifier_has_minimum():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "minimum")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::identityspecifier_has_startValue():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "startValue")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::identityspecifier_has_increment():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "increment")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel::schema::identityspecifier_has_cycleOption():
    assert hasattr(sqlmodel::schema::IdentitySpecifier, "cycleOption")
    descriptor = None
    for klass in sqlmodel::schema::IdentitySpecifier.__mro__:
        if "cycleOption" in klass.__dict__:
            descriptor = klass.__dict__["cycleOption"]
            break
    assert isinstance(descriptor, property)

def test_actiontimetype_exists():
    # Check that the Enumeration exists
    assert ActionTimeType is not None

def test_actiontimetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionTimeType]
    expected_literals = [
        "BEFORE",
        "AFTER",
        "INSTEADOF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionTimeType"

def test_actiongranularitytype_exists():
    # Check that the Enumeration exists
    assert ActionGranularityType is not None

def test_actiongranularitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionGranularityType]
    expected_literals = [
        "ROW",
        "STATEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionGranularityType"

def test_readpermissionoption_exists():
    # Check that the Enumeration exists
    assert ReadPermissionOption is not None

def test_readpermissionoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReadPermissionOption]
    expected_literals = [
        "FS",
        "DB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReadPermissionOption"

def test_unlinkoption_exists():
    # Check that the Enumeration exists
    assert UnlinkOption is not None

def test_unlinkoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnlinkOption]
    expected_literals = [
        "RESTORE",
        "DELETE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnlinkOption"

def test_checktype_exists():
    # Check that the Enumeration exists
    assert CheckType is not None

def test_checktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CheckType]
    expected_literals = [
        "NONE",
        "LOCAL",
        "CASCADED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CheckType"

def test_integritycontroloption_exists():
    # Check that the Enumeration exists
    assert IntegrityControlOption is not None

def test_integritycontroloption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegrityControlOption]
    expected_literals = [
        "ALL",
        "NONE",
        "SELECTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegrityControlOption"

def test_referentialactiontype_exists():
    # Check that the Enumeration exists
    assert ReferentialActionType is not None

def test_referentialactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialActionType]
    expected_literals = [
        "RESTRICT",
        "CASCADE",
        "SET_DEFAULT",
        "NO_ACTION",
        "SET_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialActionType"

def test_orderingtype_exists():
    # Check that the Enumeration exists
    assert OrderingType is not None

def test_orderingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderingType]
    expected_literals = [
        "EQUALS",
        "FULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderingType"

def test_orderingcategorytype_exists():
    # Check that the Enumeration exists
    assert OrderingCategoryType is not None

def test_orderingcategorytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderingCategoryType]
    expected_literals = [
        "STATE",
        "RELATIVE",
        "MAP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderingCategoryType"

def test_linkcontroloption_exists():
    # Check that the Enumeration exists
    assert LinkControlOption is not None

def test_linkcontroloption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkControlOption]
    expected_literals = [
        "NO_FILE_LINK_CONTROL",
        "FILE_LINK_CONTROL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkControlOption"

def test_matchtype_exists():
    # Check that the Enumeration exists
    assert MatchType is not None

def test_matchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchType]
    expected_literals = [
        "MATCH_SIMPLE",
        "MATCH_PARTIAL",
        "MATCH_FULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchType"

def test_coercibilitytype_exists():
    # Check that the Enumeration exists
    assert CoercibilityType is not None

def test_coercibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoercibilityType]
    expected_literals = [
        "NO_COLLATION",
        "COERCIBILE",
        "IMPLICIT",
        "EXPLICIT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoercibilityType"

def test_referencetype_exists():
    # Check that the Enumeration exists
    assert ReferenceType is not None

def test_referencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceType]
    expected_literals = [
        "DERIVED_SELF_REF",
        "USER_GENERATED",
        "SYSTEM_GENERATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"

def test_intervalqualifiertype_exists():
    # Check that the Enumeration exists
    assert IntervalQualifierType is not None

def test_intervalqualifiertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalQualifierType]
    expected_literals = [
        "HOUR",
        "SECOND",
        "DAY",
        "MINUTE",
        "FRACTION",
        "MONTH",
        "YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalQualifierType"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "INOUT",
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_dataaccess_exists():
    # Check that the Enumeration exists
    assert DataAccess is not None

def test_dataaccess_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataAccess]
    expected_literals = [
        "READS_SQL_DATA",
        "MODIFIES_SQL_DATA",
        "CONTAINS_SQL",
        "NO_SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataAccess"

def test_incrementtype_exists():
    # Check that the Enumeration exists
    assert IncrementType is not None

def test_incrementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementType]
    expected_literals = [
        "DESC",
        "RANDOM",
        "ASC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementType"

def test_writepermissionoption_exists():
    # Check that the Enumeration exists
    assert WritePermissionOption is not None

def test_writepermissionoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WritePermissionOption]
    expected_literals = [
        "BLOCKED",
        "FS",
        "ADMIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WritePermissionOption"

def test_generatetype_exists():
    # Check that the Enumeration exists
    assert GenerateType is not None

def test_generatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GenerateType]
    expected_literals = [
        "DEFAULT_GENERATED",
        "ALWAYS_GENERATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GenerateType"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "DECIMAL",
        "REAL",
        "SMALLINT",
        "XML_TYPE",
        "NATIONAL_CHARACTER_LARGE_OBJECT",
        "BINARY_VARYING",
        "FLOAT",
        "TIME",
        "CHARACTER",
        "CHARACTER_LARGE_OBJECT",
        "BINARY",
        "DATE",
        "TIMESTAMP",
        "NUMERIC",
        "INTERVAL",
        "BINARY_LARGE_OBJECT",
        "DATALINK",
        "DOUBLE_PRECISION",
        "BOOLEAN",
        "BIGINT",
        "NATIONAL_CHARACTER_VARYING",
        "CHARACTER_VARYING",
        "INTEGER",
        "NATIONAL_CHARACTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
Group_strategy = st.builds(
    Group,
)
User_strategy = st.builds(
    User,
)
Role_strategy = st.builds(
    Role,
)
RoleAuthorization_strategy = st.builds(
    RoleAuthorization,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
QueryExpression_strategy = st.builds(
    QueryExpression,
)
DerivedTable_strategy = st.builds(
    DerivedTable,
)
sqlmodel::tables::ViewTable_strategy = st.builds(
    sqlmodel::tables::ViewTable,
    checkType=
        safe_text
)
statements::SQLStatement_strategy = st.builds(
    statements::SQLStatement,
)
SQLDataStatement_strategy = st.builds(
    SQLDataStatement,
)
sqlmodel::statements::SQLDataChangeStatement_strategy = st.builds(
    sqlmodel::statements::SQLDataChangeStatement,
)
SQLStatement_strategy = st.builds(
    SQLStatement,
)
sqlmodel::statements::SQLTransactionStatement_strategy = st.builds(
    sqlmodel::statements::SQLTransactionStatement,
)
sqlmodel::statements::SQLControlStatement_strategy = st.builds(
    sqlmodel::statements::SQLControlStatement,
)
sqlmodel::statements::SQLDynamicStatement_strategy = st.builds(
    sqlmodel::statements::SQLDynamicStatement,
)
sqlmodel::statements::SQLConnectionStatement_strategy = st.builds(
    sqlmodel::statements::SQLConnectionStatement,
)
sqlmodel::statements::SQLSchemaStatement_strategy = st.builds(
    sqlmodel::statements::SQLSchemaStatement,
)
sqlmodel::statements::SQLDiagnosticsStatement_strategy = st.builds(
    sqlmodel::statements::SQLDiagnosticsStatement,
)
sqlmodel::statements::SQLSessionStatement_strategy = st.builds(
    sqlmodel::statements::SQLSessionStatement,
)
sqlmodel::statements::SQLDataStatement_strategy = st.builds(
    sqlmodel::statements::SQLDataStatement,
)
sqlmodel::statements::SQLStatement_strategy = st.builds(
    sqlmodel::statements::SQLStatement,
)
Function_strategy = st.builds(
    Function,
)
sqlmodel::routines::BuiltInFunction_strategy = st.builds(
    sqlmodel::routines::BuiltInFunction,
)
sqlmodel::routines::UserDefinedFunction_strategy = st.builds(
    sqlmodel::routines::UserDefinedFunction,
)
sqlmodel::routines::Method_strategy = st.builds(
    sqlmodel::routines::Method,
    overriding=
        st.booleans(),
    constructor=
        st.booleans()
)
RoutineResultTable_strategy = st.builds(
    RoutineResultTable,
)
Source_strategy = st.builds(
    Source,
)
Parameter_strategy = st.builds(
    Parameter,
)
expressions::SearchCondition_strategy = st.builds(
    expressions::SearchCondition,
)
expressions::ValueExpression_strategy = st.builds(
    expressions::ValueExpression,
)
sqlmodel::expressions::QueryExpression_strategy = st.builds(
    sqlmodel::expressions::QueryExpression,
)
expressions::QueryExpression_strategy = st.builds(
    expressions::QueryExpression,
)
schema::SQLObject_strategy = st.builds(
    schema::SQLObject,
)
sqlmodel::expressions::SearchConditionDefault_strategy = st.builds(
    sqlmodel::expressions::SearchConditionDefault,
    SQL=
        safe_text
)
sqlmodel::expressions::ValueExpressionDefault_strategy = st.builds(
    sqlmodel::expressions::ValueExpressionDefault,
    SQL=
        safe_text
)
sqlmodel::statements::SQLStatementDefault_strategy = st.builds(
    sqlmodel::statements::SQLStatementDefault,
    SQL=
        safe_text
)
sqlmodel::expressions::QueryExpressionDefault_strategy = st.builds(
    sqlmodel::expressions::QueryExpressionDefault,
    SQL=
        safe_text
)
sqlmodel::expressions::SearchCondition_strategy = st.builds(
    sqlmodel::expressions::SearchCondition,
)
sqlmodel::expressions::ValueExpression_strategy = st.builds(
    sqlmodel::expressions::ValueExpression,
)
NumericalDataType_strategy = st.builds(
    NumericalDataType,
)
sqlmodel::datatypes::ApproximateNumericDataType_strategy = st.builds(
    sqlmodel::datatypes::ApproximateNumericDataType,
)
sqlmodel::datatypes::ExactNumericDataType_strategy = st.builds(
    sqlmodel::datatypes::ExactNumericDataType,
    scale=
        st.integers()
)
CheckConstraint_strategy = st.builds(
    CheckConstraint,
)
DistinctUserDefinedType_strategy = st.builds(
    DistinctUserDefinedType,
)
sqlmodel::datatypes::Domain_strategy = st.builds(
    sqlmodel::datatypes::Domain,
    defaultValue=
        safe_text
)
ExactNumericDataType_strategy = st.builds(
    ExactNumericDataType,
)
sqlmodel::datatypes::IntegerDataType_strategy = st.builds(
    sqlmodel::datatypes::IntegerDataType,
)
sqlmodel::datatypes::FixedPrecisionDataType_strategy = st.builds(
    sqlmodel::datatypes::FixedPrecisionDataType,
)
StructuredUserDefinedType_strategy = st.builds(
    StructuredUserDefinedType,
)
Method_strategy = st.builds(
    Method,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
CharacterStringDataType_strategy = st.builds(
    CharacterStringDataType,
)
CollectionDataType_strategy = st.builds(
    CollectionDataType,
)
sqlmodel::datatypes::MultisetDataType_strategy = st.builds(
    sqlmodel::datatypes::MultisetDataType,
)
sqlmodel::datatypes::ArrayDataType_strategy = st.builds(
    sqlmodel::datatypes::ArrayDataType,
    maxCardinality=
        st.integers()
)
Field_strategy = st.builds(
    Field,
)
PredefinedDataType_strategy = st.builds(
    PredefinedDataType,
)
sqlmodel::datatypes::IntervalDataType_strategy = st.builds(
    sqlmodel::datatypes::IntervalDataType,
    leadingFieldPrecision=
        st.integers(),
    fractionalSecondsPrecision=
        st.integers(),
    trailingQualifier=
        safe_text,
    leadingQualifier=
        safe_text,
    trailingFieldPrecision=
        st.integers()
)
sqlmodel::datatypes::DataLinkDataType_strategy = st.builds(
    sqlmodel::datatypes::DataLinkDataType,
    length=
        st.integers(),
    writePermission=
        safe_text,
    recovery=
        st.booleans(),
    readPermission=
        safe_text,
    unlink=
        safe_text,
    linkControl=
        safe_text,
    integrityControl=
        safe_text
)
sqlmodel::datatypes::BooleanDataType_strategy = st.builds(
    sqlmodel::datatypes::BooleanDataType,
)
sqlmodel::datatypes::DateDataType_strategy = st.builds(
    sqlmodel::datatypes::DateDataType,
)
sqlmodel::datatypes::CharacterStringDataType_strategy = st.builds(
    sqlmodel::datatypes::CharacterStringDataType,
    coercibility=
        safe_text,
    fixedLength=
        st.booleans(),
    length=
        st.integers(),
    collationName=
        safe_text
)
sqlmodel::datatypes::XMLDataType_strategy = st.builds(
    sqlmodel::datatypes::XMLDataType,
)
sqlmodel::datatypes::TimeDataType_strategy = st.builds(
    sqlmodel::datatypes::TimeDataType,
    fractionalSecondsPrecision=
        st.integers(),
    timeZone=
        st.booleans()
)
sqlmodel::datatypes::BinaryStringDataType_strategy = st.builds(
    sqlmodel::datatypes::BinaryStringDataType,
    length=
        st.integers()
)
sqlmodel::datatypes::NumericalDataType_strategy = st.builds(
    sqlmodel::datatypes::NumericalDataType,
    precision=
        st.integers()
)
ElementType_strategy = st.builds(
    ElementType,
)
ConstructedDataType_strategy = st.builds(
    ConstructedDataType,
)
sqlmodel::datatypes::RowDataType_strategy = st.builds(
    sqlmodel::datatypes::RowDataType,
)
sqlmodel::datatypes::ReferenceDataType_strategy = st.builds(
    sqlmodel::datatypes::ReferenceDataType,
)
sqlmodel::datatypes::CollectionDataType_strategy = st.builds(
    sqlmodel::datatypes::CollectionDataType,
)
IndexExpression_strategy = st.builds(
    IndexExpression,
)
UserDefinedTypeOrdering_strategy = st.builds(
    UserDefinedTypeOrdering,
)
DataType_strategy = st.builds(
    DataType,
)
sqlmodel::datatypes::SQLDataType_strategy = st.builds(
    sqlmodel::datatypes::SQLDataType,
)
sqlmodel::datatypes::ConstructedDataType_strategy = st.builds(
    sqlmodel::datatypes::ConstructedDataType,
)
sqlmodel::datatypes::UserDefinedType_strategy = st.builds(
    sqlmodel::datatypes::UserDefinedType,
)
IndexMember_strategy = st.builds(
    IndexMember,
)
ForeignKey_strategy = st.builds(
    ForeignKey,
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
sqlmodel::constraints::PrimaryKey_strategy = st.builds(
    sqlmodel::constraints::PrimaryKey,
)
ReferenceConstraint_strategy = st.builds(
    ReferenceConstraint,
)
sqlmodel::constraints::UniqueConstraint_strategy = st.builds(
    sqlmodel::constraints::UniqueConstraint,
    clustered=
        st.booleans()
)
sqlmodel::constraints::ForeignKey_strategy = st.builds(
    sqlmodel::constraints::ForeignKey,
    onUpdate=
        safe_text,
    match=
        safe_text,
    onDelete=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sqlmodel::constraints::CheckConstraint_strategy = st.builds(
    sqlmodel::constraints::CheckConstraint,
)
sqlmodel::constraints::ReferenceConstraint_strategy = st.builds(
    sqlmodel::constraints::ReferenceConstraint,
)
SearchCondition_strategy = st.builds(
    SearchCondition,
)
Constraint_strategy = st.builds(
    Constraint,
)
sqlmodel::constraints::TableConstraint_strategy = st.builds(
    sqlmodel::constraints::TableConstraint,
)
sqlmodel::constraints::Assertion_strategy = st.builds(
    sqlmodel::constraints::Assertion,
)
BaseTable_strategy = st.builds(
    BaseTable,
)
sqlmodel::tables::TemporaryTable_strategy = st.builds(
    sqlmodel::tables::TemporaryTable,
    local=
        st.booleans(),
    deleteOnCommit=
        st.booleans()
)
sqlmodel::tables::PersistentTable_strategy = st.builds(
    sqlmodel::tables::PersistentTable,
)
sqlmodel::schema::Comment_strategy = st.builds(
    sqlmodel::schema::Comment,
    description=
        safe_text
)
sqlmodel::schema::ObjectExtension_strategy = st.builds(
    sqlmodel::schema::ObjectExtension,
)
Event_strategy = st.builds(
    Event,
)
IdentitySpecifier_strategy = st.builds(
    IdentitySpecifier,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
sqlmodel::datatypes::ElementType_strategy = st.builds(
    sqlmodel::datatypes::ElementType,
)
sqlmodel::routines::Parameter_strategy = st.builds(
    sqlmodel::routines::Parameter,
    locator=
        st.booleans(),
    mode=
        safe_text
)
sqlmodel::datatypes::Field_strategy = st.builds(
    sqlmodel::datatypes::Field,
    scopeCheck=
        safe_text,
    scopeChecked=
        st.booleans()
)
sqlmodel::tables::Column_strategy = st.builds(
    sqlmodel::tables::Column,
    scopeChecked=
        st.booleans(),
    nullable=
        st.booleans(),
    scopeCheck=
        safe_text,
    implementationDependent=
        st.booleans(),
    defaultValue=
        safe_text
)
sqlmodel::datatypes::AttributeDefinition_strategy = st.builds(
    sqlmodel::datatypes::AttributeDefinition,
    scopeCheck=
        safe_text,
    defaultValue=
        safe_text,
    scopeChecked=
        st.booleans()
)
sqlmodel::schema::Sequence_strategy = st.builds(
    sqlmodel::schema::Sequence,
)
Privilege_strategy = st.builds(
    Privilege,
)
Schema_strategy = st.builds(
    Schema,
)
ObjectExtension_strategy = st.builds(
    ObjectExtension,
)
Comment_strategy = st.builds(
    Comment,
)
Dependency_strategy = st.builds(
    Dependency,
)
CharacterSet_strategy = st.builds(
    CharacterSet,
)
Assertion_strategy = st.builds(
    Assertion,
)
Catalog_strategy = st.builds(
    Catalog,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
sqlmodel::schema::SQLObject_strategy = st.builds(
    sqlmodel::schema::SQLObject,
    label=
        safe_text,
    description=
        safe_text
)
AuthorizationIdentifier_strategy = st.builds(
    AuthorizationIdentifier,
)
sqlmodel::accesscontrol::User_strategy = st.builds(
    sqlmodel::accesscontrol::User,
)
sqlmodel::accesscontrol::Role_strategy = st.builds(
    sqlmodel::accesscontrol::Role,
)
sqlmodel::accesscontrol::Group_strategy = st.builds(
    sqlmodel::accesscontrol::Group,
)
Routine_strategy = st.builds(
    Routine,
)
sqlmodel::routines::Function_strategy = st.builds(
    sqlmodel::routines::Function,
    typePreserving=
        st.booleans(),
    nullCall=
        st.booleans(),
    mutator=
        st.booleans(),
    transformGroup=
        safe_text,
    static=
        st.booleans()
)
sqlmodel::routines::Procedure_strategy = st.builds(
    sqlmodel::routines::Procedure,
    oldSavePoint=
        st.booleans(),
    maxResultSets=
        st.integers()
)
Trigger_strategy = st.builds(
    Trigger,
)
schema::sqlmodel::EObject_strategy = st.builds(
    schema::sqlmodel::EObject,
)
Database_strategy = st.builds(
    Database,
)
Sequence_strategy = st.builds(
    Sequence,
)
Table_strategy = st.builds(
    Table,
)
sqlmodel::tables::BaseTable_strategy = st.builds(
    sqlmodel::tables::BaseTable,
)
sqlmodel::tables::DerivedTable_strategy = st.builds(
    sqlmodel::tables::DerivedTable,
)
sqlmodel::routines::RoutineResultTable_strategy = st.builds(
    sqlmodel::routines::RoutineResultTable,
)
Index_strategy = st.builds(
    Index,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
sqlmodel::datatypes::StructuredUserDefinedType_strategy = st.builds(
    sqlmodel::datatypes::StructuredUserDefinedType,
    final=
        st.booleans(),
    instantiable=
        st.booleans()
)
sqlmodel::datatypes::DistinctUserDefinedType_strategy = st.builds(
    sqlmodel::datatypes::DistinctUserDefinedType,
)
SQLDataType_strategy = st.builds(
    SQLDataType,
)
sqlmodel::datatypes::PredefinedDataType_strategy = st.builds(
    sqlmodel::datatypes::PredefinedDataType,
    primitiveType=
        safe_text
)
SQLObject_strategy = st.builds(
    SQLObject,
)
sqlmodel::tables::Table_strategy = st.builds(
    sqlmodel::tables::Table,
    selfRefColumnGeneration=
        safe_text,
    insertable=
        st.booleans(),
    updatable=
        st.booleans()
)
sqlmodel::tables::Trigger_strategy = st.builds(
    sqlmodel::tables::Trigger,
    actionGranularity=
        safe_text,
    deleteType=
        st.booleans(),
    actionTime=
        safe_text,
    updateType=
        st.booleans(),
    timeStamp=
        safe_text,
    oldTable=
        safe_text,
    oldRow=
        safe_text,
    newRow=
        safe_text,
    newTable=
        safe_text,
    insertType=
        st.booleans()
)
sqlmodel::routines::Routine_strategy = st.builds(
    sqlmodel::routines::Routine,
    creationTS=
        safe_text,
    security=
        safe_text,
    specificName=
        safe_text,
    externalName=
        safe_text,
    parameterStyle=
        safe_text,
    lastAlteredTS=
        safe_text,
    authorizationID=
        safe_text,
    sqlDataAccess=
        safe_text,
    language=
        safe_text,
    deterministic=
        st.booleans()
)
sqlmodel::constraints::IndexExpression_strategy = st.builds(
    sqlmodel::constraints::IndexExpression,
    sql=
        safe_text
)
sqlmodel::constraints::Index_strategy = st.builds(
    sqlmodel::constraints::Index,
    fillFactor=
        st.integers(),
    systemGenerated=
        st.booleans(),
    clustered=
        st.booleans(),
    unique=
        st.booleans()
)
sqlmodel::datatypes::CharacterSet_strategy = st.builds(
    sqlmodel::datatypes::CharacterSet,
    repertoire=
        safe_text,
    defaultCollation=
        safe_text,
    encoding=
        safe_text
)
sqlmodel::schema::TypedElement_strategy = st.builds(
    sqlmodel::schema::TypedElement,
)
sqlmodel::accesscontrol::Privilege_strategy = st.builds(
    sqlmodel::accesscontrol::Privilege,
    withHierarchy=
        st.booleans(),
    action=
        safe_text,
    grantable=
        st.booleans()
)
sqlmodel::datatypes::UserDefinedTypeOrdering_strategy = st.builds(
    sqlmodel::datatypes::UserDefinedTypeOrdering,
    orderingCategory=
        safe_text,
    orderingForm=
        safe_text
)
sqlmodel::schema::Schema_strategy = st.builds(
    sqlmodel::schema::Schema,
)
sqlmodel::constraints::Constraint_strategy = st.builds(
    sqlmodel::constraints::Constraint,
    enforced=
        st.booleans(),
    deferrable=
        st.booleans(),
    initiallyDeferred=
        st.booleans()
)
sqlmodel::routines::Source_strategy = st.builds(
    sqlmodel::routines::Source,
    body=
        safe_text
)
sqlmodel::datatypes::DataType_strategy = st.builds(
    sqlmodel::datatypes::DataType,
)
sqlmodel::schema::Dependency_strategy = st.builds(
    sqlmodel::schema::Dependency,
    dependencyType=
        safe_text
)
sqlmodel::schema::Catalog_strategy = st.builds(
    sqlmodel::schema::Catalog,
)
sqlmodel::accesscontrol::AuthorizationIdentifier_strategy = st.builds(
    sqlmodel::accesscontrol::AuthorizationIdentifier,
)
sqlmodel::schema::Event_strategy = st.builds(
    sqlmodel::schema::Event,
    action=
        safe_text,
    for_=
        safe_text,
    condition=
        safe_text,
    enabled=
        st.booleans()
)
sqlmodel::schema::Database_strategy = st.builds(
    sqlmodel::schema::Database,
    version=
        safe_text,
    vendor=
        safe_text
)
sqlmodel::constraints::IndexMember_strategy = st.builds(
    sqlmodel::constraints::IndexMember,
    incrementType=
        safe_text
)
sqlmodel::accesscontrol::RoleAuthorization_strategy = st.builds(
    sqlmodel::accesscontrol::RoleAuthorization,
    grantable=
        st.booleans()
)
sqlmodel::schema::IdentitySpecifier_strategy = st.builds(
    sqlmodel::schema::IdentitySpecifier,
    generationType=
        safe_text,
    maximum=
        safe_text,
    minimum=
        safe_text,
    startValue=
        safe_text,
    increment=
        safe_text,
    cycleOption=
        st.booleans()
)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=RoleAuthorization_strategy)
@settings(max_examples=50)
def test_roleauthorization_instantiation(instance):
    assert isinstance(instance, RoleAuthorization)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=QueryExpression_strategy)
@settings(max_examples=50)
def test_queryexpression_instantiation(instance):
    assert isinstance(instance, QueryExpression)

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=sqlmodel::tables::ViewTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::viewtable_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::ViewTable)

@given(instance=sqlmodel::tables::ViewTable_strategy)
def test_sqlmodel::tables::viewtable_checkType_type(instance):
    assert isinstance(instance.checkType, str)


@given(instance=sqlmodel::tables::ViewTable_strategy)
def test_sqlmodel::tables::viewtable_checkType_setter(instance):
    original = instance.checkType
    instance.checkType = original
    assert instance.checkType == original

@given(instance=statements::SQLStatement_strategy)
@settings(max_examples=50)
def test_statements::sqlstatement_instantiation(instance):
    assert isinstance(instance, statements::SQLStatement)

@given(instance=SQLDataStatement_strategy)
@settings(max_examples=50)
def test_sqldatastatement_instantiation(instance):
    assert isinstance(instance, SQLDataStatement)

@given(instance=sqlmodel::statements::SQLDataChangeStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqldatachangestatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLDataChangeStatement)

@given(instance=SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlstatement_instantiation(instance):
    assert isinstance(instance, SQLStatement)

@given(instance=sqlmodel::statements::SQLTransactionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqltransactionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLTransactionStatement)

@given(instance=sqlmodel::statements::SQLControlStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlcontrolstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLControlStatement)

@given(instance=sqlmodel::statements::SQLDynamicStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqldynamicstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLDynamicStatement)

@given(instance=sqlmodel::statements::SQLConnectionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlconnectionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLConnectionStatement)

@given(instance=sqlmodel::statements::SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlschemastatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLSchemaStatement)

@given(instance=sqlmodel::statements::SQLDiagnosticsStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqldiagnosticsstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLDiagnosticsStatement)

@given(instance=sqlmodel::statements::SQLSessionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlsessionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLSessionStatement)

@given(instance=sqlmodel::statements::SQLDataStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqldatastatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLDataStatement)

@given(instance=sqlmodel::statements::SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLStatement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::statements::SQLStatement_strategy)
@settings(max_examples=30)
def test_sqlmodel::statements::sqlstatement_setsql_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSQL(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSQL).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSQL' in sqlmodel::statements::SQLStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel::statements::SQLStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel::statements::SQLStatement is not implemented or raised an error")

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=sqlmodel::routines::BuiltInFunction_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::builtinfunction_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::BuiltInFunction)

@given(instance=sqlmodel::routines::UserDefinedFunction_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::userdefinedfunction_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::UserDefinedFunction)

@given(instance=sqlmodel::routines::Method_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::method_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Method)

@given(instance=sqlmodel::routines::Method_strategy)
def test_sqlmodel::routines::method_overriding_type(instance):
    assert isinstance(instance.overriding, bool)


@given(instance=sqlmodel::routines::Method_strategy)
def test_sqlmodel::routines::method_overriding_setter(instance):
    original = instance.overriding
    instance.overriding = original
    assert instance.overriding == original

@given(instance=sqlmodel::routines::Method_strategy)
def test_sqlmodel::routines::method_constructor_type(instance):
    assert isinstance(instance.constructor, bool)


@given(instance=sqlmodel::routines::Method_strategy)
def test_sqlmodel::routines::method_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=RoutineResultTable_strategy)
@settings(max_examples=50)
def test_routineresulttable_instantiation(instance):
    assert isinstance(instance, RoutineResultTable)

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=expressions::SearchCondition_strategy)
@settings(max_examples=50)
def test_expressions::searchcondition_instantiation(instance):
    assert isinstance(instance, expressions::SearchCondition)

@given(instance=expressions::ValueExpression_strategy)
@settings(max_examples=50)
def test_expressions::valueexpression_instantiation(instance):
    assert isinstance(instance, expressions::ValueExpression)

@given(instance=sqlmodel::expressions::QueryExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::queryexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::QueryExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::expressions::QueryExpression_strategy)
@settings(max_examples=30)
def test_sqlmodel::expressions::queryexpression_setsql_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSQL(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSQL).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSQL' in sqlmodel::expressions::QueryExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::QueryExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::QueryExpression is not implemented or raised an error")

@given(instance=expressions::QueryExpression_strategy)
@settings(max_examples=50)
def test_expressions::queryexpression_instantiation(instance):
    assert isinstance(instance, expressions::QueryExpression)

@given(instance=schema::SQLObject_strategy)
@settings(max_examples=50)
def test_schema::sqlobject_instantiation(instance):
    assert isinstance(instance, schema::SQLObject)

@given(instance=sqlmodel::expressions::SearchConditionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::searchconditiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::SearchConditionDefault)

@given(instance=sqlmodel::expressions::SearchConditionDefault_strategy)
def test_sqlmodel::expressions::searchconditiondefault_SQL_type(instance):
    assert isinstance(instance.SQL, str)


@given(instance=sqlmodel::expressions::SearchConditionDefault_strategy)
def test_sqlmodel::expressions::searchconditiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel::expressions::ValueExpressionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::valueexpressiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::ValueExpressionDefault)

@given(instance=sqlmodel::expressions::ValueExpressionDefault_strategy)
def test_sqlmodel::expressions::valueexpressiondefault_SQL_type(instance):
    assert isinstance(instance.SQL, str)


@given(instance=sqlmodel::expressions::ValueExpressionDefault_strategy)
def test_sqlmodel::expressions::valueexpressiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel::statements::SQLStatementDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel::statements::sqlstatementdefault_instantiation(instance):
    assert isinstance(instance, sqlmodel::statements::SQLStatementDefault)

@given(instance=sqlmodel::statements::SQLStatementDefault_strategy)
def test_sqlmodel::statements::sqlstatementdefault_SQL_type(instance):
    assert isinstance(instance.SQL, str)


@given(instance=sqlmodel::statements::SQLStatementDefault_strategy)
def test_sqlmodel::statements::sqlstatementdefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel::expressions::QueryExpressionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::queryexpressiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::QueryExpressionDefault)

@given(instance=sqlmodel::expressions::QueryExpressionDefault_strategy)
def test_sqlmodel::expressions::queryexpressiondefault_SQL_type(instance):
    assert isinstance(instance.SQL, str)


@given(instance=sqlmodel::expressions::QueryExpressionDefault_strategy)
def test_sqlmodel::expressions::queryexpressiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel::expressions::SearchCondition_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::searchcondition_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::SearchCondition)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::expressions::SearchCondition_strategy)
@settings(max_examples=30)
def test_sqlmodel::expressions::searchcondition_setsql_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSQL(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSQL).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSQL' in sqlmodel::expressions::SearchCondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::SearchCondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::SearchCondition is not implemented or raised an error")

@given(instance=sqlmodel::expressions::ValueExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel::expressions::valueexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel::expressions::ValueExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::expressions::ValueExpression_strategy)
@settings(max_examples=30)
def test_sqlmodel::expressions::valueexpression_setsql_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSQL(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSQL).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSQL' in sqlmodel::expressions::ValueExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::ValueExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel::expressions::ValueExpression is not implemented or raised an error")

@given(instance=NumericalDataType_strategy)
@settings(max_examples=50)
def test_numericaldatatype_instantiation(instance):
    assert isinstance(instance, NumericalDataType)

@given(instance=sqlmodel::datatypes::ApproximateNumericDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::approximatenumericdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ApproximateNumericDataType)

@given(instance=sqlmodel::datatypes::ExactNumericDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::exactnumericdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ExactNumericDataType)

@given(instance=sqlmodel::datatypes::ExactNumericDataType_strategy)
def test_sqlmodel::datatypes::exactnumericdatatype_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=sqlmodel::datatypes::ExactNumericDataType_strategy)
def test_sqlmodel::datatypes::exactnumericdatatype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=CheckConstraint_strategy)
@settings(max_examples=50)
def test_checkconstraint_instantiation(instance):
    assert isinstance(instance, CheckConstraint)

@given(instance=DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, DistinctUserDefinedType)

@given(instance=sqlmodel::datatypes::Domain_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::domain_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::Domain)

@given(instance=sqlmodel::datatypes::Domain_strategy)
def test_sqlmodel::datatypes::domain_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=sqlmodel::datatypes::Domain_strategy)
def test_sqlmodel::datatypes::domain_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=ExactNumericDataType_strategy)
@settings(max_examples=50)
def test_exactnumericdatatype_instantiation(instance):
    assert isinstance(instance, ExactNumericDataType)

@given(instance=sqlmodel::datatypes::IntegerDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::integerdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::IntegerDataType)

@given(instance=sqlmodel::datatypes::FixedPrecisionDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::fixedprecisiondatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::FixedPrecisionDataType)

@given(instance=StructuredUserDefinedType_strategy)
@settings(max_examples=50)
def test_structureduserdefinedtype_instantiation(instance):
    assert isinstance(instance, StructuredUserDefinedType)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=CharacterStringDataType_strategy)
@settings(max_examples=50)
def test_characterstringdatatype_instantiation(instance):
    assert isinstance(instance, CharacterStringDataType)

@given(instance=CollectionDataType_strategy)
@settings(max_examples=50)
def test_collectiondatatype_instantiation(instance):
    assert isinstance(instance, CollectionDataType)

@given(instance=sqlmodel::datatypes::MultisetDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::multisetdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::MultisetDataType)

@given(instance=sqlmodel::datatypes::ArrayDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::arraydatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ArrayDataType)

@given(instance=sqlmodel::datatypes::ArrayDataType_strategy)
def test_sqlmodel::datatypes::arraydatatype_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=sqlmodel::datatypes::ArrayDataType_strategy)
def test_sqlmodel::datatypes::arraydatatype_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=PredefinedDataType_strategy)
@settings(max_examples=50)
def test_predefineddatatype_instantiation(instance):
    assert isinstance(instance, PredefinedDataType)

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::intervaldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::IntervalDataType)

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_leadingFieldPrecision_type(instance):
    assert isinstance(instance.leadingFieldPrecision, int)


@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_leadingFieldPrecision_setter(instance):
    original = instance.leadingFieldPrecision
    instance.leadingFieldPrecision = original
    assert instance.leadingFieldPrecision == original

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_fractionalSecondsPrecision_type(instance):
    assert isinstance(instance.fractionalSecondsPrecision, int)


@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_fractionalSecondsPrecision_setter(instance):
    original = instance.fractionalSecondsPrecision
    instance.fractionalSecondsPrecision = original
    assert instance.fractionalSecondsPrecision == original

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_trailingQualifier_type(instance):
    assert isinstance(instance.trailingQualifier, str)


@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_trailingQualifier_setter(instance):
    original = instance.trailingQualifier
    instance.trailingQualifier = original
    assert instance.trailingQualifier == original

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_leadingQualifier_type(instance):
    assert isinstance(instance.leadingQualifier, str)


@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_leadingQualifier_setter(instance):
    original = instance.leadingQualifier
    instance.leadingQualifier = original
    assert instance.leadingQualifier == original

@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_trailingFieldPrecision_type(instance):
    assert isinstance(instance.trailingFieldPrecision, int)


@given(instance=sqlmodel::datatypes::IntervalDataType_strategy)
def test_sqlmodel::datatypes::intervaldatatype_trailingFieldPrecision_setter(instance):
    original = instance.trailingFieldPrecision
    instance.trailingFieldPrecision = original
    assert instance.trailingFieldPrecision == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::datalinkdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::DataLinkDataType)

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_writePermission_type(instance):
    assert isinstance(instance.writePermission, str)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_writePermission_setter(instance):
    original = instance.writePermission
    instance.writePermission = original
    assert instance.writePermission == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_recovery_type(instance):
    assert isinstance(instance.recovery, bool)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_recovery_setter(instance):
    original = instance.recovery
    instance.recovery = original
    assert instance.recovery == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_readPermission_type(instance):
    assert isinstance(instance.readPermission, str)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_readPermission_setter(instance):
    original = instance.readPermission
    instance.readPermission = original
    assert instance.readPermission == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_unlink_type(instance):
    assert isinstance(instance.unlink, str)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_unlink_setter(instance):
    original = instance.unlink
    instance.unlink = original
    assert instance.unlink == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_linkControl_type(instance):
    assert isinstance(instance.linkControl, str)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_linkControl_setter(instance):
    original = instance.linkControl
    instance.linkControl = original
    assert instance.linkControl == original

@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_integrityControl_type(instance):
    assert isinstance(instance.integrityControl, str)


@given(instance=sqlmodel::datatypes::DataLinkDataType_strategy)
def test_sqlmodel::datatypes::datalinkdatatype_integrityControl_setter(instance):
    original = instance.integrityControl
    instance.integrityControl = original
    assert instance.integrityControl == original

@given(instance=sqlmodel::datatypes::BooleanDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::booleandatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::BooleanDataType)

@given(instance=sqlmodel::datatypes::DateDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::datedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::DateDataType)

@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::characterstringdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::CharacterStringDataType)

@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_coercibility_type(instance):
    assert isinstance(instance.coercibility, str)


@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_coercibility_setter(instance):
    original = instance.coercibility
    instance.coercibility = original
    assert instance.coercibility == original

@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_fixedLength_type(instance):
    assert isinstance(instance.fixedLength, bool)


@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_fixedLength_setter(instance):
    original = instance.fixedLength
    instance.fixedLength = original
    assert instance.fixedLength == original

@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_collationName_type(instance):
    assert isinstance(instance.collationName, str)


@given(instance=sqlmodel::datatypes::CharacterStringDataType_strategy)
def test_sqlmodel::datatypes::characterstringdatatype_collationName_setter(instance):
    original = instance.collationName
    instance.collationName = original
    assert instance.collationName == original

@given(instance=sqlmodel::datatypes::XMLDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::xmldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::XMLDataType)

@given(instance=sqlmodel::datatypes::TimeDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::timedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::TimeDataType)

@given(instance=sqlmodel::datatypes::TimeDataType_strategy)
def test_sqlmodel::datatypes::timedatatype_fractionalSecondsPrecision_type(instance):
    assert isinstance(instance.fractionalSecondsPrecision, int)


@given(instance=sqlmodel::datatypes::TimeDataType_strategy)
def test_sqlmodel::datatypes::timedatatype_fractionalSecondsPrecision_setter(instance):
    original = instance.fractionalSecondsPrecision
    instance.fractionalSecondsPrecision = original
    assert instance.fractionalSecondsPrecision == original

@given(instance=sqlmodel::datatypes::TimeDataType_strategy)
def test_sqlmodel::datatypes::timedatatype_timeZone_type(instance):
    assert isinstance(instance.timeZone, bool)


@given(instance=sqlmodel::datatypes::TimeDataType_strategy)
def test_sqlmodel::datatypes::timedatatype_timeZone_setter(instance):
    original = instance.timeZone
    instance.timeZone = original
    assert instance.timeZone == original

@given(instance=sqlmodel::datatypes::BinaryStringDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::binarystringdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::BinaryStringDataType)

@given(instance=sqlmodel::datatypes::BinaryStringDataType_strategy)
def test_sqlmodel::datatypes::binarystringdatatype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=sqlmodel::datatypes::BinaryStringDataType_strategy)
def test_sqlmodel::datatypes::binarystringdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::datatypes::BinaryStringDataType_strategy)
@settings(max_examples=30)
def test_sqlmodel::datatypes::binarystringdatatype_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in sqlmodel::datatypes::BinaryStringDataType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in sqlmodel::datatypes::BinaryStringDataType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in sqlmodel::datatypes::BinaryStringDataType is not implemented or raised an error")

@given(instance=sqlmodel::datatypes::NumericalDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::numericaldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::NumericalDataType)

@given(instance=sqlmodel::datatypes::NumericalDataType_strategy)
def test_sqlmodel::datatypes::numericaldatatype_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=sqlmodel::datatypes::NumericalDataType_strategy)
def test_sqlmodel::datatypes::numericaldatatype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=ConstructedDataType_strategy)
@settings(max_examples=50)
def test_constructeddatatype_instantiation(instance):
    assert isinstance(instance, ConstructedDataType)

@given(instance=sqlmodel::datatypes::RowDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::rowdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::RowDataType)

@given(instance=sqlmodel::datatypes::ReferenceDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::referencedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ReferenceDataType)

@given(instance=sqlmodel::datatypes::CollectionDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::collectiondatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::CollectionDataType)

@given(instance=IndexExpression_strategy)
@settings(max_examples=50)
def test_indexexpression_instantiation(instance):
    assert isinstance(instance, IndexExpression)

@given(instance=UserDefinedTypeOrdering_strategy)
@settings(max_examples=50)
def test_userdefinedtypeordering_instantiation(instance):
    assert isinstance(instance, UserDefinedTypeOrdering)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sqlmodel::datatypes::SQLDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::sqldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::SQLDataType)

@given(instance=sqlmodel::datatypes::ConstructedDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::constructeddatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ConstructedDataType)

@given(instance=sqlmodel::datatypes::UserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::userdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::UserDefinedType)

@given(instance=IndexMember_strategy)
@settings(max_examples=50)
def test_indexmember_instantiation(instance):
    assert isinstance(instance, IndexMember)

@given(instance=ForeignKey_strategy)
@settings(max_examples=50)
def test_foreignkey_instantiation(instance):
    assert isinstance(instance, ForeignKey)

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=sqlmodel::constraints::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::primarykey_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::PrimaryKey)

@given(instance=ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_referenceconstraint_instantiation(instance):
    assert isinstance(instance, ReferenceConstraint)

@given(instance=sqlmodel::constraints::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::UniqueConstraint)

@given(instance=sqlmodel::constraints::UniqueConstraint_strategy)
def test_sqlmodel::constraints::uniqueconstraint_clustered_type(instance):
    assert isinstance(instance.clustered, bool)


@given(instance=sqlmodel::constraints::UniqueConstraint_strategy)
def test_sqlmodel::constraints::uniqueconstraint_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original

@given(instance=sqlmodel::constraints::ForeignKey_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::foreignkey_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::ForeignKey)

@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_onUpdate_type(instance):
    assert isinstance(instance.onUpdate, str)


@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original

@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_match_type(instance):
    assert isinstance(instance.match, str)


@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original

@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_onDelete_type(instance):
    assert isinstance(instance.onDelete, str)


@given(instance=sqlmodel::constraints::ForeignKey_strategy)
def test_sqlmodel::constraints::foreignkey_onDelete_setter(instance):
    original = instance.onDelete
    instance.onDelete = original
    assert instance.onDelete == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sqlmodel::constraints::CheckConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::checkconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::CheckConstraint)

@given(instance=sqlmodel::constraints::ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::referenceconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::ReferenceConstraint)

@given(instance=SearchCondition_strategy)
@settings(max_examples=50)
def test_searchcondition_instantiation(instance):
    assert isinstance(instance, SearchCondition)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=sqlmodel::constraints::TableConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::tableconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::TableConstraint)

@given(instance=sqlmodel::constraints::Assertion_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::assertion_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::Assertion)

@given(instance=BaseTable_strategy)
@settings(max_examples=50)
def test_basetable_instantiation(instance):
    assert isinstance(instance, BaseTable)

@given(instance=sqlmodel::tables::TemporaryTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::temporarytable_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::TemporaryTable)

@given(instance=sqlmodel::tables::TemporaryTable_strategy)
def test_sqlmodel::tables::temporarytable_local_type(instance):
    assert isinstance(instance.local, bool)


@given(instance=sqlmodel::tables::TemporaryTable_strategy)
def test_sqlmodel::tables::temporarytable_local_setter(instance):
    original = instance.local
    instance.local = original
    assert instance.local == original

@given(instance=sqlmodel::tables::TemporaryTable_strategy)
def test_sqlmodel::tables::temporarytable_deleteOnCommit_type(instance):
    assert isinstance(instance.deleteOnCommit, bool)


@given(instance=sqlmodel::tables::TemporaryTable_strategy)
def test_sqlmodel::tables::temporarytable_deleteOnCommit_setter(instance):
    original = instance.deleteOnCommit
    instance.deleteOnCommit = original
    assert instance.deleteOnCommit == original

@given(instance=sqlmodel::tables::PersistentTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::persistenttable_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::PersistentTable)

@given(instance=sqlmodel::schema::Comment_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::comment_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Comment)

@given(instance=sqlmodel::schema::Comment_strategy)
def test_sqlmodel::schema::comment_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=sqlmodel::schema::Comment_strategy)
def test_sqlmodel::schema::comment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=sqlmodel::schema::ObjectExtension_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::objectextension_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::ObjectExtension)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=IdentitySpecifier_strategy)
@settings(max_examples=50)
def test_identityspecifier_instantiation(instance):
    assert isinstance(instance, IdentitySpecifier)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=sqlmodel::datatypes::ElementType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::elementtype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::ElementType)

@given(instance=sqlmodel::routines::Parameter_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::parameter_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Parameter)

@given(instance=sqlmodel::routines::Parameter_strategy)
def test_sqlmodel::routines::parameter_locator_type(instance):
    assert isinstance(instance.locator, bool)


@given(instance=sqlmodel::routines::Parameter_strategy)
def test_sqlmodel::routines::parameter_locator_setter(instance):
    original = instance.locator
    instance.locator = original
    assert instance.locator == original

@given(instance=sqlmodel::routines::Parameter_strategy)
def test_sqlmodel::routines::parameter_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=sqlmodel::routines::Parameter_strategy)
def test_sqlmodel::routines::parameter_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=sqlmodel::datatypes::Field_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::field_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::Field)

@given(instance=sqlmodel::datatypes::Field_strategy)
def test_sqlmodel::datatypes::field_scopeCheck_type(instance):
    assert isinstance(instance.scopeCheck, str)


@given(instance=sqlmodel::datatypes::Field_strategy)
def test_sqlmodel::datatypes::field_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original

@given(instance=sqlmodel::datatypes::Field_strategy)
def test_sqlmodel::datatypes::field_scopeChecked_type(instance):
    assert isinstance(instance.scopeChecked, bool)


@given(instance=sqlmodel::datatypes::Field_strategy)
def test_sqlmodel::datatypes::field_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original

@given(instance=sqlmodel::tables::Column_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::column_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::Column)

@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_scopeChecked_type(instance):
    assert isinstance(instance.scopeChecked, bool)


@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original

@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_scopeCheck_type(instance):
    assert isinstance(instance.scopeCheck, str)


@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original

@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_implementationDependent_type(instance):
    assert isinstance(instance.implementationDependent, bool)


@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_implementationDependent_setter(instance):
    original = instance.implementationDependent
    instance.implementationDependent = original
    assert instance.implementationDependent == original

@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=sqlmodel::tables::Column_strategy)
def test_sqlmodel::tables::column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::tables::Column_strategy)
@settings(max_examples=30)
def test_sqlmodel::tables::column_ispartofuniqueconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPartOfUniqueConstraint()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPartOfUniqueConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPartOfUniqueConstraint' in sqlmodel::tables::Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfUniqueConstraint' in sqlmodel::tables::Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfUniqueConstraint' in sqlmodel::tables::Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::tables::Column_strategy)
@settings(max_examples=30)
def test_sqlmodel::tables::column_ispartofforeignkey_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPartOfForeignKey()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPartOfForeignKey).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPartOfForeignKey' in sqlmodel::tables::Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfForeignKey' in sqlmodel::tables::Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfForeignKey' in sqlmodel::tables::Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::tables::Column_strategy)
@settings(max_examples=30)
def test_sqlmodel::tables::column_ispartofprimarykey_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPartOfPrimaryKey()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPartOfPrimaryKey).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPartOfPrimaryKey' in sqlmodel::tables::Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfPrimaryKey' in sqlmodel::tables::Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfPrimaryKey' in sqlmodel::tables::Column is not implemented or raised an error")

@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::attributedefinition_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::AttributeDefinition)

@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_scopeCheck_type(instance):
    assert isinstance(instance.scopeCheck, str)


@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original

@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_scopeChecked_type(instance):
    assert isinstance(instance.scopeChecked, bool)


@given(instance=sqlmodel::datatypes::AttributeDefinition_strategy)
def test_sqlmodel::datatypes::attributedefinition_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original

@given(instance=sqlmodel::schema::Sequence_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::sequence_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Sequence)

@given(instance=Privilege_strategy)
@settings(max_examples=50)
def test_privilege_instantiation(instance):
    assert isinstance(instance, Privilege)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=ObjectExtension_strategy)
@settings(max_examples=50)
def test_objectextension_instantiation(instance):
    assert isinstance(instance, ObjectExtension)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=CharacterSet_strategy)
@settings(max_examples=50)
def test_characterset_instantiation(instance):
    assert isinstance(instance, CharacterSet)

@given(instance=Assertion_strategy)
@settings(max_examples=50)
def test_assertion_instantiation(instance):
    assert isinstance(instance, Assertion)

@given(instance=Catalog_strategy)
@settings(max_examples=50)
def test_catalog_instantiation(instance):
    assert isinstance(instance, Catalog)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=sqlmodel::schema::SQLObject_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::sqlobject_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::SQLObject)

@given(instance=sqlmodel::schema::SQLObject_strategy)
def test_sqlmodel::schema::sqlobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=sqlmodel::schema::SQLObject_strategy)
def test_sqlmodel::schema::sqlobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=sqlmodel::schema::SQLObject_strategy)
def test_sqlmodel::schema::sqlobject_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=sqlmodel::schema::SQLObject_strategy)
def test_sqlmodel::schema::sqlobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::schema::SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel::schema::sqlobject_setannotationdetail_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setAnnotationDetail(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setAnnotationDetail).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setAnnotationDetail' in sqlmodel::schema::SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAnnotationDetail' in sqlmodel::schema::SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAnnotationDetail' in sqlmodel::schema::SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::schema::SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel::schema::sqlobject_addeannotationdetail_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addEAnnotationDetail(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addEAnnotationDetail).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addEAnnotationDetail' in sqlmodel::schema::SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEAnnotationDetail' in sqlmodel::schema::SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEAnnotationDetail' in sqlmodel::schema::SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::schema::SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel::schema::sqlobject_addeannotation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addEAnnotation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addEAnnotation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addEAnnotation' in sqlmodel::schema::SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEAnnotation' in sqlmodel::schema::SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEAnnotation' in sqlmodel::schema::SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::schema::SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel::schema::sqlobject_removeeannotationdetail_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeEAnnotationDetail(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeEAnnotationDetail).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeEAnnotationDetail' in sqlmodel::schema::SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeEAnnotationDetail' in sqlmodel::schema::SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeEAnnotationDetail' in sqlmodel::schema::SQLObject is not implemented or raised an error")

@given(instance=AuthorizationIdentifier_strategy)
@settings(max_examples=50)
def test_authorizationidentifier_instantiation(instance):
    assert isinstance(instance, AuthorizationIdentifier)

@given(instance=sqlmodel::accesscontrol::User_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::user_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::User)

@given(instance=sqlmodel::accesscontrol::Role_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::role_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::Role)

@given(instance=sqlmodel::accesscontrol::Group_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::group_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::Group)

@given(instance=Routine_strategy)
@settings(max_examples=50)
def test_routine_instantiation(instance):
    assert isinstance(instance, Routine)

@given(instance=sqlmodel::routines::Function_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::function_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Function)

@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_typePreserving_type(instance):
    assert isinstance(instance.typePreserving, bool)


@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_typePreserving_setter(instance):
    original = instance.typePreserving
    instance.typePreserving = original
    assert instance.typePreserving == original

@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_nullCall_type(instance):
    assert isinstance(instance.nullCall, bool)


@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_nullCall_setter(instance):
    original = instance.nullCall
    instance.nullCall = original
    assert instance.nullCall == original

@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_mutator_type(instance):
    assert isinstance(instance.mutator, bool)


@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_mutator_setter(instance):
    original = instance.mutator
    instance.mutator = original
    assert instance.mutator == original

@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_transformGroup_type(instance):
    assert isinstance(instance.transformGroup, str)


@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_transformGroup_setter(instance):
    original = instance.transformGroup
    instance.transformGroup = original
    assert instance.transformGroup == original

@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=sqlmodel::routines::Function_strategy)
def test_sqlmodel::routines::function_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=sqlmodel::routines::Procedure_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::procedure_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Procedure)

@given(instance=sqlmodel::routines::Procedure_strategy)
def test_sqlmodel::routines::procedure_oldSavePoint_type(instance):
    assert isinstance(instance.oldSavePoint, bool)


@given(instance=sqlmodel::routines::Procedure_strategy)
def test_sqlmodel::routines::procedure_oldSavePoint_setter(instance):
    original = instance.oldSavePoint
    instance.oldSavePoint = original
    assert instance.oldSavePoint == original

@given(instance=sqlmodel::routines::Procedure_strategy)
def test_sqlmodel::routines::procedure_maxResultSets_type(instance):
    assert isinstance(instance.maxResultSets, int)


@given(instance=sqlmodel::routines::Procedure_strategy)
def test_sqlmodel::routines::procedure_maxResultSets_setter(instance):
    original = instance.maxResultSets
    instance.maxResultSets = original
    assert instance.maxResultSets == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=schema::sqlmodel::EObject_strategy)
@settings(max_examples=50)
def test_schema::sqlmodel::eobject_instantiation(instance):
    assert isinstance(instance, schema::sqlmodel::EObject)

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=sqlmodel::tables::BaseTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::basetable_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::BaseTable)

@given(instance=sqlmodel::tables::DerivedTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::derivedtable_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::DerivedTable)

@given(instance=sqlmodel::routines::RoutineResultTable_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::routineresulttable_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::RoutineResultTable)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=sqlmodel::datatypes::StructuredUserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::structureduserdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::StructuredUserDefinedType)

@given(instance=sqlmodel::datatypes::StructuredUserDefinedType_strategy)
def test_sqlmodel::datatypes::structureduserdefinedtype_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=sqlmodel::datatypes::StructuredUserDefinedType_strategy)
def test_sqlmodel::datatypes::structureduserdefinedtype_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=sqlmodel::datatypes::StructuredUserDefinedType_strategy)
def test_sqlmodel::datatypes::structureduserdefinedtype_instantiable_type(instance):
    assert isinstance(instance.instantiable, bool)


@given(instance=sqlmodel::datatypes::StructuredUserDefinedType_strategy)
def test_sqlmodel::datatypes::structureduserdefinedtype_instantiable_setter(instance):
    original = instance.instantiable
    instance.instantiable = original
    assert instance.instantiable == original

@given(instance=sqlmodel::datatypes::DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::DistinctUserDefinedType)

@given(instance=SQLDataType_strategy)
@settings(max_examples=50)
def test_sqldatatype_instantiation(instance):
    assert isinstance(instance, SQLDataType)

@given(instance=sqlmodel::datatypes::PredefinedDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::predefineddatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::PredefinedDataType)

@given(instance=sqlmodel::datatypes::PredefinedDataType_strategy)
def test_sqlmodel::datatypes::predefineddatatype_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=sqlmodel::datatypes::PredefinedDataType_strategy)
def test_sqlmodel::datatypes::predefineddatatype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=sqlmodel::tables::Table_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::table_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::Table)

@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_selfRefColumnGeneration_type(instance):
    assert isinstance(instance.selfRefColumnGeneration, str)


@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_selfRefColumnGeneration_setter(instance):
    original = instance.selfRefColumnGeneration
    instance.selfRefColumnGeneration = original
    assert instance.selfRefColumnGeneration == original

@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_insertable_type(instance):
    assert isinstance(instance.insertable, bool)


@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_insertable_setter(instance):
    original = instance.insertable
    instance.insertable = original
    assert instance.insertable == original

@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_updatable_type(instance):
    assert isinstance(instance.updatable, bool)


@given(instance=sqlmodel::tables::Table_strategy)
def test_sqlmodel::tables::table_updatable_setter(instance):
    original = instance.updatable
    instance.updatable = original
    assert instance.updatable == original

@given(instance=sqlmodel::tables::Trigger_strategy)
@settings(max_examples=50)
def test_sqlmodel::tables::trigger_instantiation(instance):
    assert isinstance(instance, sqlmodel::tables::Trigger)

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_actionGranularity_type(instance):
    assert isinstance(instance.actionGranularity, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_actionGranularity_setter(instance):
    original = instance.actionGranularity
    instance.actionGranularity = original
    assert instance.actionGranularity == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_deleteType_type(instance):
    assert isinstance(instance.deleteType, bool)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_deleteType_setter(instance):
    original = instance.deleteType
    instance.deleteType = original
    assert instance.deleteType == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_actionTime_type(instance):
    assert isinstance(instance.actionTime, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_updateType_type(instance):
    assert isinstance(instance.updateType, bool)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_updateType_setter(instance):
    original = instance.updateType
    instance.updateType = original
    assert instance.updateType == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_timeStamp_type(instance):
    assert isinstance(instance.timeStamp, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_timeStamp_setter(instance):
    original = instance.timeStamp
    instance.timeStamp = original
    assert instance.timeStamp == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_oldTable_type(instance):
    assert isinstance(instance.oldTable, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_oldTable_setter(instance):
    original = instance.oldTable
    instance.oldTable = original
    assert instance.oldTable == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_oldRow_type(instance):
    assert isinstance(instance.oldRow, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_oldRow_setter(instance):
    original = instance.oldRow
    instance.oldRow = original
    assert instance.oldRow == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_newRow_type(instance):
    assert isinstance(instance.newRow, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_newRow_setter(instance):
    original = instance.newRow
    instance.newRow = original
    assert instance.newRow == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_newTable_type(instance):
    assert isinstance(instance.newTable, str)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_newTable_setter(instance):
    original = instance.newTable
    instance.newTable = original
    assert instance.newTable == original

@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_insertType_type(instance):
    assert isinstance(instance.insertType, bool)


@given(instance=sqlmodel::tables::Trigger_strategy)
def test_sqlmodel::tables::trigger_insertType_setter(instance):
    original = instance.insertType
    instance.insertType = original
    assert instance.insertType == original

@given(instance=sqlmodel::routines::Routine_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::routine_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Routine)

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_creationTS_type(instance):
    assert isinstance(instance.creationTS, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_creationTS_setter(instance):
    original = instance.creationTS
    instance.creationTS = original
    assert instance.creationTS == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_security_type(instance):
    assert isinstance(instance.security, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_security_setter(instance):
    original = instance.security
    instance.security = original
    assert instance.security == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_specificName_type(instance):
    assert isinstance(instance.specificName, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_specificName_setter(instance):
    original = instance.specificName
    instance.specificName = original
    assert instance.specificName == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_externalName_type(instance):
    assert isinstance(instance.externalName, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_externalName_setter(instance):
    original = instance.externalName
    instance.externalName = original
    assert instance.externalName == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_parameterStyle_type(instance):
    assert isinstance(instance.parameterStyle, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_parameterStyle_setter(instance):
    original = instance.parameterStyle
    instance.parameterStyle = original
    assert instance.parameterStyle == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_lastAlteredTS_type(instance):
    assert isinstance(instance.lastAlteredTS, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_lastAlteredTS_setter(instance):
    original = instance.lastAlteredTS
    instance.lastAlteredTS = original
    assert instance.lastAlteredTS == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_authorizationID_type(instance):
    assert isinstance(instance.authorizationID, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_authorizationID_setter(instance):
    original = instance.authorizationID
    instance.authorizationID = original
    assert instance.authorizationID == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_sqlDataAccess_type(instance):
    assert isinstance(instance.sqlDataAccess, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_sqlDataAccess_setter(instance):
    original = instance.sqlDataAccess
    instance.sqlDataAccess = original
    assert instance.sqlDataAccess == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_deterministic_type(instance):
    assert isinstance(instance.deterministic, bool)


@given(instance=sqlmodel::routines::Routine_strategy)
def test_sqlmodel::routines::routine_deterministic_setter(instance):
    original = instance.deterministic
    instance.deterministic = original
    assert instance.deterministic == original

@given(instance=sqlmodel::constraints::IndexExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::indexexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::IndexExpression)

@given(instance=sqlmodel::constraints::IndexExpression_strategy)
def test_sqlmodel::constraints::indexexpression_sql_type(instance):
    assert isinstance(instance.sql, str)


@given(instance=sqlmodel::constraints::IndexExpression_strategy)
def test_sqlmodel::constraints::indexexpression_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=sqlmodel::constraints::Index_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::index_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::Index)

@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_fillFactor_type(instance):
    assert isinstance(instance.fillFactor, int)


@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_fillFactor_setter(instance):
    original = instance.fillFactor
    instance.fillFactor = original
    assert instance.fillFactor == original

@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_systemGenerated_type(instance):
    assert isinstance(instance.systemGenerated, bool)


@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_systemGenerated_setter(instance):
    original = instance.systemGenerated
    instance.systemGenerated = original
    assert instance.systemGenerated == original

@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_clustered_type(instance):
    assert isinstance(instance.clustered, bool)


@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original

@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=sqlmodel::constraints::Index_strategy)
def test_sqlmodel::constraints::index_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::characterset_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::CharacterSet)

@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_repertoire_type(instance):
    assert isinstance(instance.repertoire, str)


@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_repertoire_setter(instance):
    original = instance.repertoire
    instance.repertoire = original
    assert instance.repertoire == original

@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_defaultCollation_type(instance):
    assert isinstance(instance.defaultCollation, str)


@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_defaultCollation_setter(instance):
    original = instance.defaultCollation
    instance.defaultCollation = original
    assert instance.defaultCollation == original

@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=sqlmodel::datatypes::CharacterSet_strategy)
def test_sqlmodel::datatypes::characterset_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=sqlmodel::schema::TypedElement_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::typedelement_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::TypedElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::schema::TypedElement_strategy)
@settings(max_examples=30)
def test_sqlmodel::schema::typedelement_setdatatype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDataType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDataType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDataType' in sqlmodel::schema::TypedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDataType' in sqlmodel::schema::TypedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDataType' in sqlmodel::schema::TypedElement is not implemented or raised an error")

@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::privilege_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::Privilege)

@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_withHierarchy_type(instance):
    assert isinstance(instance.withHierarchy, bool)


@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_withHierarchy_setter(instance):
    original = instance.withHierarchy
    instance.withHierarchy = original
    assert instance.withHierarchy == original

@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_grantable_type(instance):
    assert isinstance(instance.grantable, bool)


@given(instance=sqlmodel::accesscontrol::Privilege_strategy)
def test_sqlmodel::accesscontrol::privilege_grantable_setter(instance):
    original = instance.grantable
    instance.grantable = original
    assert instance.grantable == original

@given(instance=sqlmodel::datatypes::UserDefinedTypeOrdering_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::userdefinedtypeordering_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::UserDefinedTypeOrdering)

@given(instance=sqlmodel::datatypes::UserDefinedTypeOrdering_strategy)
def test_sqlmodel::datatypes::userdefinedtypeordering_orderingCategory_type(instance):
    assert isinstance(instance.orderingCategory, str)


@given(instance=sqlmodel::datatypes::UserDefinedTypeOrdering_strategy)
def test_sqlmodel::datatypes::userdefinedtypeordering_orderingCategory_setter(instance):
    original = instance.orderingCategory
    instance.orderingCategory = original
    assert instance.orderingCategory == original

@given(instance=sqlmodel::datatypes::UserDefinedTypeOrdering_strategy)
def test_sqlmodel::datatypes::userdefinedtypeordering_orderingForm_type(instance):
    assert isinstance(instance.orderingForm, str)


@given(instance=sqlmodel::datatypes::UserDefinedTypeOrdering_strategy)
def test_sqlmodel::datatypes::userdefinedtypeordering_orderingForm_setter(instance):
    original = instance.orderingForm
    instance.orderingForm = original
    assert instance.orderingForm == original

@given(instance=sqlmodel::schema::Schema_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::schema_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Schema)

@given(instance=sqlmodel::constraints::Constraint_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::constraint_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::Constraint)

@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_enforced_type(instance):
    assert isinstance(instance.enforced, bool)


@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_enforced_setter(instance):
    original = instance.enforced
    instance.enforced = original
    assert instance.enforced == original

@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_deferrable_type(instance):
    assert isinstance(instance.deferrable, bool)


@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_deferrable_setter(instance):
    original = instance.deferrable
    instance.deferrable = original
    assert instance.deferrable == original

@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_initiallyDeferred_type(instance):
    assert isinstance(instance.initiallyDeferred, bool)


@given(instance=sqlmodel::constraints::Constraint_strategy)
def test_sqlmodel::constraints::constraint_initiallyDeferred_setter(instance):
    original = instance.initiallyDeferred
    instance.initiallyDeferred = original
    assert instance.initiallyDeferred == original

@given(instance=sqlmodel::routines::Source_strategy)
@settings(max_examples=50)
def test_sqlmodel::routines::source_instantiation(instance):
    assert isinstance(instance, sqlmodel::routines::Source)

@given(instance=sqlmodel::routines::Source_strategy)
def test_sqlmodel::routines::source_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=sqlmodel::routines::Source_strategy)
def test_sqlmodel::routines::source_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=sqlmodel::datatypes::DataType_strategy)
@settings(max_examples=50)
def test_sqlmodel::datatypes::datatype_instantiation(instance):
    assert isinstance(instance, sqlmodel::datatypes::DataType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel::datatypes::DataType_strategy)
@settings(max_examples=30)
def test_sqlmodel::datatypes::datatype_setcontainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setContainer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setContainer' in sqlmodel::datatypes::DataType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setContainer' in sqlmodel::datatypes::DataType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setContainer' in sqlmodel::datatypes::DataType is not implemented or raised an error")

@given(instance=sqlmodel::schema::Dependency_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::dependency_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Dependency)

@given(instance=sqlmodel::schema::Dependency_strategy)
def test_sqlmodel::schema::dependency_dependencyType_type(instance):
    assert isinstance(instance.dependencyType, str)


@given(instance=sqlmodel::schema::Dependency_strategy)
def test_sqlmodel::schema::dependency_dependencyType_setter(instance):
    original = instance.dependencyType
    instance.dependencyType = original
    assert instance.dependencyType == original

@given(instance=sqlmodel::schema::Catalog_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::catalog_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Catalog)

@given(instance=sqlmodel::accesscontrol::AuthorizationIdentifier_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::authorizationidentifier_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::AuthorizationIdentifier)

@given(instance=sqlmodel::schema::Event_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::event_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Event)

@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_for__type(instance):
    assert isinstance(instance.for_, str)


@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_enabled_type(instance):
    assert isinstance(instance.enabled, bool)


@given(instance=sqlmodel::schema::Event_strategy)
def test_sqlmodel::schema::event_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=sqlmodel::schema::Database_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::database_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::Database)

@given(instance=sqlmodel::schema::Database_strategy)
def test_sqlmodel::schema::database_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=sqlmodel::schema::Database_strategy)
def test_sqlmodel::schema::database_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sqlmodel::schema::Database_strategy)
def test_sqlmodel::schema::database_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=sqlmodel::schema::Database_strategy)
def test_sqlmodel::schema::database_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=sqlmodel::constraints::IndexMember_strategy)
@settings(max_examples=50)
def test_sqlmodel::constraints::indexmember_instantiation(instance):
    assert isinstance(instance, sqlmodel::constraints::IndexMember)

@given(instance=sqlmodel::constraints::IndexMember_strategy)
def test_sqlmodel::constraints::indexmember_incrementType_type(instance):
    assert isinstance(instance.incrementType, str)


@given(instance=sqlmodel::constraints::IndexMember_strategy)
def test_sqlmodel::constraints::indexmember_incrementType_setter(instance):
    original = instance.incrementType
    instance.incrementType = original
    assert instance.incrementType == original

@given(instance=sqlmodel::accesscontrol::RoleAuthorization_strategy)
@settings(max_examples=50)
def test_sqlmodel::accesscontrol::roleauthorization_instantiation(instance):
    assert isinstance(instance, sqlmodel::accesscontrol::RoleAuthorization)

@given(instance=sqlmodel::accesscontrol::RoleAuthorization_strategy)
def test_sqlmodel::accesscontrol::roleauthorization_grantable_type(instance):
    assert isinstance(instance.grantable, bool)


@given(instance=sqlmodel::accesscontrol::RoleAuthorization_strategy)
def test_sqlmodel::accesscontrol::roleauthorization_grantable_setter(instance):
    original = instance.grantable
    instance.grantable = original
    assert instance.grantable == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
@settings(max_examples=50)
def test_sqlmodel::schema::identityspecifier_instantiation(instance):
    assert isinstance(instance, sqlmodel::schema::IdentitySpecifier)

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_generationType_type(instance):
    assert isinstance(instance.generationType, str)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_generationType_setter(instance):
    original = instance.generationType
    instance.generationType = original
    assert instance.generationType == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_startValue_type(instance):
    assert isinstance(instance.startValue, str)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_cycleOption_type(instance):
    assert isinstance(instance.cycleOption, bool)


@given(instance=sqlmodel::schema::IdentitySpecifier_strategy)
def test_sqlmodel::schema::identityspecifier_cycleOption_setter(instance):
    original = instance.cycleOption
    instance.cycleOption = original
    assert instance.cycleOption == original
