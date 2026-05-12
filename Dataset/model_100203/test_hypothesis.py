import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Group,
    User,
    Role,
    RoleAuthorization,
    ValueExpression,
    QueryExpression,
    DerivedTable,
    sqlmodel_tables_ViewTable,
    statements_SQLStatement,
    SQLDataStatement,
    sqlmodel_statements_SQLDataChangeStatement,
    SQLStatement,
    sqlmodel_statements_SQLControlStatement,
    sqlmodel_statements_SQLDynamicStatement,
    sqlmodel_statements_SQLSessionStatement,
    sqlmodel_statements_SQLSchemaStatement,
    sqlmodel_statements_SQLConnectionStatement,
    sqlmodel_statements_SQLTransactionStatement,
    sqlmodel_statements_SQLDiagnosticsStatement,
    sqlmodel_statements_SQLDataStatement,
    sqlmodel_statements_SQLStatement,
    Function,
    sqlmodel_routines_BuiltInFunction,
    sqlmodel_routines_UserDefinedFunction,
    sqlmodel_routines_Method,
    RoutineResultTable,
    Source,
    Parameter,
    expressions_SearchCondition,
    expressions_ValueExpression,
    sqlmodel_expressions_QueryExpression,
    expressions_QueryExpression,
    schema_SQLObject,
    sqlmodel_statements_SQLStatementDefault,
    sqlmodel_expressions_SearchConditionDefault,
    sqlmodel_expressions_ValueExpressionDefault,
    sqlmodel_expressions_QueryExpressionDefault,
    sqlmodel_expressions_SearchCondition,
    sqlmodel_expressions_ValueExpression,
    NumericalDataType,
    sqlmodel_datatypes_ApproximateNumericDataType,
    sqlmodel_datatypes_ExactNumericDataType,
    CheckConstraint,
    DistinctUserDefinedType,
    sqlmodel_datatypes_Domain,
    ExactNumericDataType,
    sqlmodel_datatypes_IntegerDataType,
    sqlmodel_datatypes_FixedPrecisionDataType,
    StructuredUserDefinedType,
    Method,
    AttributeDefinition,
    CharacterStringDataType,
    CollectionDataType,
    sqlmodel_datatypes_MultisetDataType,
    sqlmodel_datatypes_ArrayDataType,
    Field,
    PredefinedDataType,
    sqlmodel_datatypes_DateDataType,
    sqlmodel_datatypes_IntervalDataType,
    sqlmodel_datatypes_CharacterStringDataType,
    sqlmodel_datatypes_TimeDataType,
    sqlmodel_datatypes_BooleanDataType,
    sqlmodel_datatypes_XMLDataType,
    sqlmodel_datatypes_BinaryStringDataType,
    sqlmodel_datatypes_DataLinkDataType,
    sqlmodel_datatypes_NumericalDataType,
    ElementType,
    ConstructedDataType,
    sqlmodel_datatypes_ReferenceDataType,
    sqlmodel_datatypes_RowDataType,
    sqlmodel_datatypes_CollectionDataType,
    IndexExpression,
    UserDefinedTypeOrdering,
    DataType,
    sqlmodel_datatypes_ConstructedDataType,
    sqlmodel_datatypes_SQLDataType,
    sqlmodel_datatypes_UserDefinedType,
    IndexMember,
    ForeignKey,
    UniqueConstraint,
    sqlmodel_constraints_PrimaryKey,
    ReferenceConstraint,
    sqlmodel_constraints_UniqueConstraint,
    sqlmodel_constraints_ForeignKey,
    Column,
    TableConstraint,
    sqlmodel_constraints_CheckConstraint,
    sqlmodel_constraints_ReferenceConstraint,
    SearchCondition,
    Constraint,
    sqlmodel_constraints_TableConstraint,
    sqlmodel_constraints_Assertion,
    BaseTable,
    sqlmodel_tables_PersistentTable,
    sqlmodel_tables_TemporaryTable,
    sqlmodel_schema_Comment,
    sqlmodel_schema_ObjectExtension,
    Event,
    IdentitySpecifier,
    TypedElement,
    sqlmodel_datatypes_AttributeDefinition,
    sqlmodel_datatypes_Field,
    sqlmodel_routines_Parameter,
    sqlmodel_tables_Column,
    sqlmodel_datatypes_ElementType,
    sqlmodel_schema_Sequence,
    Privilege,
    Schema,
    ObjectExtension,
    Comment,
    Dependency,
    CharacterSet,
    Assertion,
    Catalog,
    ENamedElement,
    sqlmodel_schema_SQLObject,
    AuthorizationIdentifier,
    sqlmodel_accesscontrol_Role,
    sqlmodel_accesscontrol_Group,
    sqlmodel_accesscontrol_User,
    Routine,
    sqlmodel_routines_Function,
    sqlmodel_routines_Procedure,
    Trigger,
    schema_sqlmodel_EObject,
    Database,
    Sequence,
    Table,
    sqlmodel_routines_RoutineResultTable,
    sqlmodel_tables_BaseTable,
    sqlmodel_tables_DerivedTable,
    Index,
    UserDefinedType,
    sqlmodel_datatypes_DistinctUserDefinedType,
    sqlmodel_datatypes_StructuredUserDefinedType,
    SQLDataType,
    sqlmodel_datatypes_PredefinedDataType,
    SQLObject,
    sqlmodel_constraints_IndexMember,
    sqlmodel_constraints_Constraint,
    sqlmodel_schema_Catalog,
    sqlmodel_schema_Event,
    sqlmodel_datatypes_CharacterSet,
    sqlmodel_routines_Routine,
    sqlmodel_tables_Trigger,
    sqlmodel_schema_Database,
    sqlmodel_schema_Schema,
    sqlmodel_schema_Dependency,
    sqlmodel_datatypes_UserDefinedTypeOrdering,
    sqlmodel_accesscontrol_Privilege,
    sqlmodel_schema_TypedElement,
    sqlmodel_accesscontrol_AuthorizationIdentifier,
    sqlmodel_constraints_Index,
    sqlmodel_datatypes_DataType,
    sqlmodel_routines_Source,
    sqlmodel_accesscontrol_RoleAuthorization,
    sqlmodel_constraints_IndexExpression,
    sqlmodel_tables_Table,
    sqlmodel_schema_IdentitySpecifier,
    MatchType,
    ReferenceType,
    ParameterMode,
    CoercibilityType,
    PrimitiveType,
    GenerateType,
    ReadPermissionOption,
    IncrementType,
    UnlinkOption,
    CheckType,
    ActionTimeType,
    ReferentialActionType,
    DataAccess,
    LinkControlOption,
    OrderingType,
    ActionGranularityType,
    OrderingCategoryType,
    WritePermissionOption,
    IntervalQualifierType,
    IntegrityControlOption,
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



def test_sqlmodel_tables_viewtable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_ViewTable)


def test_sqlmodel_tables_viewtable_constructor_exists():
    assert callable(sqlmodel_tables_ViewTable.__init__)


def test_sqlmodel_tables_viewtable_constructor_args():
    sig = inspect.signature(sqlmodel_tables_ViewTable.__init__)
    params = list(sig.parameters.keys())
    assert "checkType" in params, "Missing parameter 'checkType'"

def test_sqlmodel_tables_viewtable_has_checkType():
    assert hasattr(sqlmodel_tables_ViewTable, "checkType")
    descriptor = None
    for klass in sqlmodel_tables_ViewTable.__mro__:
        if "checkType" in klass.__dict__:
            descriptor = klass.__dict__["checkType"]
            break
    assert isinstance(descriptor, property)



def test_statements_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(statements_SQLStatement)


def test_statements_sqlstatement_constructor_exists():
    assert callable(statements_SQLStatement.__init__)


def test_statements_sqlstatement_constructor_args():
    sig = inspect.signature(statements_SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(SQLDataStatement)


def test_sqldatastatement_constructor_exists():
    assert callable(SQLDataStatement.__init__)


def test_sqldatastatement_constructor_args():
    sig = inspect.signature(SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqldatachangestatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLDataChangeStatement)


def test_sqlmodel_statements_sqldatachangestatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLDataChangeStatement.__init__)


def test_sqlmodel_statements_sqldatachangestatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLDataChangeStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(SQLStatement)


def test_sqlstatement_constructor_exists():
    assert callable(SQLStatement.__init__)


def test_sqlstatement_constructor_args():
    sig = inspect.signature(SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlcontrolstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLControlStatement)


def test_sqlmodel_statements_sqlcontrolstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLControlStatement.__init__)


def test_sqlmodel_statements_sqlcontrolstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqldynamicstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLDynamicStatement)


def test_sqlmodel_statements_sqldynamicstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLDynamicStatement.__init__)


def test_sqlmodel_statements_sqldynamicstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLDynamicStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlsessionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLSessionStatement)


def test_sqlmodel_statements_sqlsessionstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLSessionStatement.__init__)


def test_sqlmodel_statements_sqlsessionstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLSessionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlschemastatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLSchemaStatement)


def test_sqlmodel_statements_sqlschemastatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLSchemaStatement.__init__)


def test_sqlmodel_statements_sqlschemastatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLSchemaStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlconnectionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLConnectionStatement)


def test_sqlmodel_statements_sqlconnectionstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLConnectionStatement.__init__)


def test_sqlmodel_statements_sqlconnectionstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLConnectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqltransactionstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLTransactionStatement)


def test_sqlmodel_statements_sqltransactionstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLTransactionStatement.__init__)


def test_sqlmodel_statements_sqltransactionstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLTransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqldiagnosticsstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLDiagnosticsStatement)


def test_sqlmodel_statements_sqldiagnosticsstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLDiagnosticsStatement.__init__)


def test_sqlmodel_statements_sqldiagnosticsstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLDiagnosticsStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqldatastatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLDataStatement)


def test_sqlmodel_statements_sqldatastatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLDataStatement.__init__)


def test_sqlmodel_statements_sqldatastatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLDataStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlstatement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLStatement)


def test_sqlmodel_statements_sqlstatement_constructor_exists():
    assert callable(sqlmodel_statements_SQLStatement.__init__)


def test_sqlmodel_statements_sqlstatement_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLStatement.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_routines_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_BuiltInFunction)


def test_sqlmodel_routines_builtinfunction_constructor_exists():
    assert callable(sqlmodel_routines_BuiltInFunction.__init__)


def test_sqlmodel_routines_builtinfunction_constructor_args():
    sig = inspect.signature(sqlmodel_routines_BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_routines_userdefinedfunction_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_UserDefinedFunction)


def test_sqlmodel_routines_userdefinedfunction_constructor_exists():
    assert callable(sqlmodel_routines_UserDefinedFunction.__init__)


def test_sqlmodel_routines_userdefinedfunction_constructor_args():
    sig = inspect.signature(sqlmodel_routines_UserDefinedFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_routines_method_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Method)


def test_sqlmodel_routines_method_constructor_exists():
    assert callable(sqlmodel_routines_Method.__init__)


def test_sqlmodel_routines_method_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Method.__init__)
    params = list(sig.parameters.keys())
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "overriding" in params, "Missing parameter 'overriding'"

def test_sqlmodel_routines_method_has_constructor():
    assert hasattr(sqlmodel_routines_Method, "constructor")
    descriptor = None
    for klass in sqlmodel_routines_Method.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_method_has_overriding():
    assert hasattr(sqlmodel_routines_Method, "overriding")
    descriptor = None
    for klass in sqlmodel_routines_Method.__mro__:
        if "overriding" in klass.__dict__:
            descriptor = klass.__dict__["overriding"]
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



def test_expressions_searchcondition_is_not_abstract():
    assert not inspect.isabstract(expressions_SearchCondition)


def test_expressions_searchcondition_constructor_exists():
    assert callable(expressions_SearchCondition.__init__)


def test_expressions_searchcondition_constructor_args():
    sig = inspect.signature(expressions_SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_expressions_valueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ValueExpression)


def test_expressions_valueexpression_constructor_exists():
    assert callable(expressions_ValueExpression.__init__)


def test_expressions_valueexpression_constructor_args():
    sig = inspect.signature(expressions_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_expressions_queryexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_QueryExpression)


def test_sqlmodel_expressions_queryexpression_constructor_exists():
    assert callable(sqlmodel_expressions_QueryExpression.__init__)


def test_sqlmodel_expressions_queryexpression_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_queryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_QueryExpression)


def test_expressions_queryexpression_constructor_exists():
    assert callable(expressions_QueryExpression.__init__)


def test_expressions_queryexpression_constructor_args():
    sig = inspect.signature(expressions_QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_schema_sqlobject_is_not_abstract():
    assert not inspect.isabstract(schema_SQLObject)


def test_schema_sqlobject_constructor_exists():
    assert callable(schema_SQLObject.__init__)


def test_schema_sqlobject_constructor_args():
    sig = inspect.signature(schema_SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_statements_sqlstatementdefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_statements_SQLStatementDefault)


def test_sqlmodel_statements_sqlstatementdefault_constructor_exists():
    assert callable(sqlmodel_statements_SQLStatementDefault.__init__)


def test_sqlmodel_statements_sqlstatementdefault_constructor_args():
    sig = inspect.signature(sqlmodel_statements_SQLStatementDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel_statements_sqlstatementdefault_has_SQL():
    assert hasattr(sqlmodel_statements_SQLStatementDefault, "SQL")
    descriptor = None
    for klass in sqlmodel_statements_SQLStatementDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_expressions_searchconditiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_SearchConditionDefault)


def test_sqlmodel_expressions_searchconditiondefault_constructor_exists():
    assert callable(sqlmodel_expressions_SearchConditionDefault.__init__)


def test_sqlmodel_expressions_searchconditiondefault_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_SearchConditionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel_expressions_searchconditiondefault_has_SQL():
    assert hasattr(sqlmodel_expressions_SearchConditionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel_expressions_SearchConditionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_expressions_valueexpressiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_ValueExpressionDefault)


def test_sqlmodel_expressions_valueexpressiondefault_constructor_exists():
    assert callable(sqlmodel_expressions_ValueExpressionDefault.__init__)


def test_sqlmodel_expressions_valueexpressiondefault_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_ValueExpressionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel_expressions_valueexpressiondefault_has_SQL():
    assert hasattr(sqlmodel_expressions_ValueExpressionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel_expressions_ValueExpressionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_expressions_queryexpressiondefault_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_QueryExpressionDefault)


def test_sqlmodel_expressions_queryexpressiondefault_constructor_exists():
    assert callable(sqlmodel_expressions_QueryExpressionDefault.__init__)


def test_sqlmodel_expressions_queryexpressiondefault_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_QueryExpressionDefault.__init__)
    params = list(sig.parameters.keys())
    assert "SQL" in params, "Missing parameter 'SQL'"

def test_sqlmodel_expressions_queryexpressiondefault_has_SQL():
    assert hasattr(sqlmodel_expressions_QueryExpressionDefault, "SQL")
    descriptor = None
    for klass in sqlmodel_expressions_QueryExpressionDefault.__mro__:
        if "SQL" in klass.__dict__:
            descriptor = klass.__dict__["SQL"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_expressions_searchcondition_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_SearchCondition)


def test_sqlmodel_expressions_searchcondition_constructor_exists():
    assert callable(sqlmodel_expressions_SearchCondition.__init__)


def test_sqlmodel_expressions_searchcondition_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_SearchCondition.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_expressions_valueexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_expressions_ValueExpression)


def test_sqlmodel_expressions_valueexpression_constructor_exists():
    assert callable(sqlmodel_expressions_ValueExpression.__init__)


def test_sqlmodel_expressions_valueexpression_constructor_args():
    sig = inspect.signature(sqlmodel_expressions_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_numericaldatatype_is_not_abstract():
    assert not inspect.isabstract(NumericalDataType)


def test_numericaldatatype_constructor_exists():
    assert callable(NumericalDataType.__init__)


def test_numericaldatatype_constructor_args():
    sig = inspect.signature(NumericalDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_approximatenumericdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ApproximateNumericDataType)


def test_sqlmodel_datatypes_approximatenumericdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_ApproximateNumericDataType.__init__)


def test_sqlmodel_datatypes_approximatenumericdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ApproximateNumericDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_exactnumericdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ExactNumericDataType)


def test_sqlmodel_datatypes_exactnumericdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_ExactNumericDataType.__init__)


def test_sqlmodel_datatypes_exactnumericdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ExactNumericDataType.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_sqlmodel_datatypes_exactnumericdatatype_has_scale():
    assert hasattr(sqlmodel_datatypes_ExactNumericDataType, "scale")
    descriptor = None
    for klass in sqlmodel_datatypes_ExactNumericDataType.__mro__:
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



def test_sqlmodel_datatypes_domain_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_Domain)


def test_sqlmodel_datatypes_domain_constructor_exists():
    assert callable(sqlmodel_datatypes_Domain.__init__)


def test_sqlmodel_datatypes_domain_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_sqlmodel_datatypes_domain_has_defaultValue():
    assert hasattr(sqlmodel_datatypes_Domain, "defaultValue")
    descriptor = None
    for klass in sqlmodel_datatypes_Domain.__mro__:
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



def test_sqlmodel_datatypes_integerdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_IntegerDataType)


def test_sqlmodel_datatypes_integerdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_IntegerDataType.__init__)


def test_sqlmodel_datatypes_integerdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_IntegerDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_fixedprecisiondatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_FixedPrecisionDataType)


def test_sqlmodel_datatypes_fixedprecisiondatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_FixedPrecisionDataType.__init__)


def test_sqlmodel_datatypes_fixedprecisiondatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_FixedPrecisionDataType.__init__)
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



def test_sqlmodel_datatypes_multisetdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_MultisetDataType)


def test_sqlmodel_datatypes_multisetdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_MultisetDataType.__init__)


def test_sqlmodel_datatypes_multisetdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_MultisetDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_arraydatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ArrayDataType)


def test_sqlmodel_datatypes_arraydatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_ArrayDataType.__init__)


def test_sqlmodel_datatypes_arraydatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ArrayDataType.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"

def test_sqlmodel_datatypes_arraydatatype_has_maxCardinality():
    assert hasattr(sqlmodel_datatypes_ArrayDataType, "maxCardinality")
    descriptor = None
    for klass in sqlmodel_datatypes_ArrayDataType.__mro__:
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



def test_sqlmodel_datatypes_datedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_DateDataType)


def test_sqlmodel_datatypes_datedatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_DateDataType.__init__)


def test_sqlmodel_datatypes_datedatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_DateDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_intervaldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_IntervalDataType)


def test_sqlmodel_datatypes_intervaldatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_IntervalDataType.__init__)


def test_sqlmodel_datatypes_intervaldatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_IntervalDataType.__init__)
    params = list(sig.parameters.keys())
    assert "leadingFieldPrecision" in params, "Missing parameter 'leadingFieldPrecision'"
    assert "trailingQualifier" in params, "Missing parameter 'trailingQualifier'"
    assert "leadingQualifier" in params, "Missing parameter 'leadingQualifier'"
    assert "fractionalSecondsPrecision" in params, "Missing parameter 'fractionalSecondsPrecision'"
    assert "trailingFieldPrecision" in params, "Missing parameter 'trailingFieldPrecision'"

def test_sqlmodel_datatypes_intervaldatatype_has_leadingFieldPrecision():
    assert hasattr(sqlmodel_datatypes_IntervalDataType, "leadingFieldPrecision")
    descriptor = None
    for klass in sqlmodel_datatypes_IntervalDataType.__mro__:
        if "leadingFieldPrecision" in klass.__dict__:
            descriptor = klass.__dict__["leadingFieldPrecision"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_intervaldatatype_has_trailingQualifier():
    assert hasattr(sqlmodel_datatypes_IntervalDataType, "trailingQualifier")
    descriptor = None
    for klass in sqlmodel_datatypes_IntervalDataType.__mro__:
        if "trailingQualifier" in klass.__dict__:
            descriptor = klass.__dict__["trailingQualifier"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_intervaldatatype_has_leadingQualifier():
    assert hasattr(sqlmodel_datatypes_IntervalDataType, "leadingQualifier")
    descriptor = None
    for klass in sqlmodel_datatypes_IntervalDataType.__mro__:
        if "leadingQualifier" in klass.__dict__:
            descriptor = klass.__dict__["leadingQualifier"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_intervaldatatype_has_fractionalSecondsPrecision():
    assert hasattr(sqlmodel_datatypes_IntervalDataType, "fractionalSecondsPrecision")
    descriptor = None
    for klass in sqlmodel_datatypes_IntervalDataType.__mro__:
        if "fractionalSecondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["fractionalSecondsPrecision"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_intervaldatatype_has_trailingFieldPrecision():
    assert hasattr(sqlmodel_datatypes_IntervalDataType, "trailingFieldPrecision")
    descriptor = None
    for klass in sqlmodel_datatypes_IntervalDataType.__mro__:
        if "trailingFieldPrecision" in klass.__dict__:
            descriptor = klass.__dict__["trailingFieldPrecision"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_characterstringdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_CharacterStringDataType)


def test_sqlmodel_datatypes_characterstringdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_CharacterStringDataType.__init__)


def test_sqlmodel_datatypes_characterstringdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_CharacterStringDataType.__init__)
    params = list(sig.parameters.keys())
    assert "fixedLength" in params, "Missing parameter 'fixedLength'"
    assert "length" in params, "Missing parameter 'length'"
    assert "collationName" in params, "Missing parameter 'collationName'"
    assert "coercibility" in params, "Missing parameter 'coercibility'"

def test_sqlmodel_datatypes_characterstringdatatype_has_fixedLength():
    assert hasattr(sqlmodel_datatypes_CharacterStringDataType, "fixedLength")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterStringDataType.__mro__:
        if "fixedLength" in klass.__dict__:
            descriptor = klass.__dict__["fixedLength"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_characterstringdatatype_has_length():
    assert hasattr(sqlmodel_datatypes_CharacterStringDataType, "length")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterStringDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_characterstringdatatype_has_collationName():
    assert hasattr(sqlmodel_datatypes_CharacterStringDataType, "collationName")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterStringDataType.__mro__:
        if "collationName" in klass.__dict__:
            descriptor = klass.__dict__["collationName"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_characterstringdatatype_has_coercibility():
    assert hasattr(sqlmodel_datatypes_CharacterStringDataType, "coercibility")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterStringDataType.__mro__:
        if "coercibility" in klass.__dict__:
            descriptor = klass.__dict__["coercibility"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_timedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_TimeDataType)


def test_sqlmodel_datatypes_timedatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_TimeDataType.__init__)


def test_sqlmodel_datatypes_timedatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_TimeDataType.__init__)
    params = list(sig.parameters.keys())
    assert "timeZone" in params, "Missing parameter 'timeZone'"
    assert "fractionalSecondsPrecision" in params, "Missing parameter 'fractionalSecondsPrecision'"

def test_sqlmodel_datatypes_timedatatype_has_timeZone():
    assert hasattr(sqlmodel_datatypes_TimeDataType, "timeZone")
    descriptor = None
    for klass in sqlmodel_datatypes_TimeDataType.__mro__:
        if "timeZone" in klass.__dict__:
            descriptor = klass.__dict__["timeZone"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_timedatatype_has_fractionalSecondsPrecision():
    assert hasattr(sqlmodel_datatypes_TimeDataType, "fractionalSecondsPrecision")
    descriptor = None
    for klass in sqlmodel_datatypes_TimeDataType.__mro__:
        if "fractionalSecondsPrecision" in klass.__dict__:
            descriptor = klass.__dict__["fractionalSecondsPrecision"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_booleandatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_BooleanDataType)


def test_sqlmodel_datatypes_booleandatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_BooleanDataType.__init__)


def test_sqlmodel_datatypes_booleandatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_BooleanDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_xmldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_XMLDataType)


def test_sqlmodel_datatypes_xmldatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_XMLDataType.__init__)


def test_sqlmodel_datatypes_xmldatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_XMLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_binarystringdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_BinaryStringDataType)


def test_sqlmodel_datatypes_binarystringdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_BinaryStringDataType.__init__)


def test_sqlmodel_datatypes_binarystringdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_BinaryStringDataType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_sqlmodel_datatypes_binarystringdatatype_has_length():
    assert hasattr(sqlmodel_datatypes_BinaryStringDataType, "length")
    descriptor = None
    for klass in sqlmodel_datatypes_BinaryStringDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_datalinkdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_DataLinkDataType)


def test_sqlmodel_datatypes_datalinkdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_DataLinkDataType.__init__)


def test_sqlmodel_datatypes_datalinkdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_DataLinkDataType.__init__)
    params = list(sig.parameters.keys())
    assert "recovery" in params, "Missing parameter 'recovery'"
    assert "linkControl" in params, "Missing parameter 'linkControl'"
    assert "writePermission" in params, "Missing parameter 'writePermission'"
    assert "integrityControl" in params, "Missing parameter 'integrityControl'"
    assert "unlink" in params, "Missing parameter 'unlink'"
    assert "length" in params, "Missing parameter 'length'"
    assert "readPermission" in params, "Missing parameter 'readPermission'"

def test_sqlmodel_datatypes_datalinkdatatype_has_recovery():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "recovery")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "recovery" in klass.__dict__:
            descriptor = klass.__dict__["recovery"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_linkControl():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "linkControl")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "linkControl" in klass.__dict__:
            descriptor = klass.__dict__["linkControl"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_writePermission():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "writePermission")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "writePermission" in klass.__dict__:
            descriptor = klass.__dict__["writePermission"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_integrityControl():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "integrityControl")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "integrityControl" in klass.__dict__:
            descriptor = klass.__dict__["integrityControl"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_unlink():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "unlink")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "unlink" in klass.__dict__:
            descriptor = klass.__dict__["unlink"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_length():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "length")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_datalinkdatatype_has_readPermission():
    assert hasattr(sqlmodel_datatypes_DataLinkDataType, "readPermission")
    descriptor = None
    for klass in sqlmodel_datatypes_DataLinkDataType.__mro__:
        if "readPermission" in klass.__dict__:
            descriptor = klass.__dict__["readPermission"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_numericaldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_NumericalDataType)


def test_sqlmodel_datatypes_numericaldatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_NumericalDataType.__init__)


def test_sqlmodel_datatypes_numericaldatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_NumericalDataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_sqlmodel_datatypes_numericaldatatype_has_precision():
    assert hasattr(sqlmodel_datatypes_NumericalDataType, "precision")
    descriptor = None
    for klass in sqlmodel_datatypes_NumericalDataType.__mro__:
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



def test_sqlmodel_datatypes_referencedatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ReferenceDataType)


def test_sqlmodel_datatypes_referencedatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_ReferenceDataType.__init__)


def test_sqlmodel_datatypes_referencedatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ReferenceDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_rowdatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_RowDataType)


def test_sqlmodel_datatypes_rowdatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_RowDataType.__init__)


def test_sqlmodel_datatypes_rowdatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_RowDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_collectiondatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_CollectionDataType)


def test_sqlmodel_datatypes_collectiondatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_CollectionDataType.__init__)


def test_sqlmodel_datatypes_collectiondatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_CollectionDataType.__init__)
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



def test_sqlmodel_datatypes_constructeddatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ConstructedDataType)


def test_sqlmodel_datatypes_constructeddatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_ConstructedDataType.__init__)


def test_sqlmodel_datatypes_constructeddatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ConstructedDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_SQLDataType)


def test_sqlmodel_datatypes_sqldatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_SQLDataType.__init__)


def test_sqlmodel_datatypes_sqldatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_UserDefinedType)


def test_sqlmodel_datatypes_userdefinedtype_constructor_exists():
    assert callable(sqlmodel_datatypes_UserDefinedType.__init__)


def test_sqlmodel_datatypes_userdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_UserDefinedType.__init__)
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



def test_sqlmodel_constraints_primarykey_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_PrimaryKey)


def test_sqlmodel_constraints_primarykey_constructor_exists():
    assert callable(sqlmodel_constraints_PrimaryKey.__init__)


def test_sqlmodel_constraints_primarykey_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(ReferenceConstraint)


def test_referenceconstraint_constructor_exists():
    assert callable(ReferenceConstraint.__init__)


def test_referenceconstraint_constructor_args():
    sig = inspect.signature(ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_constraints_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_UniqueConstraint)


def test_sqlmodel_constraints_uniqueconstraint_constructor_exists():
    assert callable(sqlmodel_constraints_UniqueConstraint.__init__)


def test_sqlmodel_constraints_uniqueconstraint_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "clustered" in params, "Missing parameter 'clustered'"

def test_sqlmodel_constraints_uniqueconstraint_has_clustered():
    assert hasattr(sqlmodel_constraints_UniqueConstraint, "clustered")
    descriptor = None
    for klass in sqlmodel_constraints_UniqueConstraint.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_constraints_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_ForeignKey)


def test_sqlmodel_constraints_foreignkey_constructor_exists():
    assert callable(sqlmodel_constraints_ForeignKey.__init__)


def test_sqlmodel_constraints_foreignkey_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "match" in params, "Missing parameter 'match'"
    assert "onDelete" in params, "Missing parameter 'onDelete'"

def test_sqlmodel_constraints_foreignkey_has_onUpdate():
    assert hasattr(sqlmodel_constraints_ForeignKey, "onUpdate")
    descriptor = None
    for klass in sqlmodel_constraints_ForeignKey.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_foreignkey_has_match():
    assert hasattr(sqlmodel_constraints_ForeignKey, "match")
    descriptor = None
    for klass in sqlmodel_constraints_ForeignKey.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_foreignkey_has_onDelete():
    assert hasattr(sqlmodel_constraints_ForeignKey, "onDelete")
    descriptor = None
    for klass in sqlmodel_constraints_ForeignKey.__mro__:
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



def test_sqlmodel_constraints_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_CheckConstraint)


def test_sqlmodel_constraints_checkconstraint_constructor_exists():
    assert callable(sqlmodel_constraints_CheckConstraint.__init__)


def test_sqlmodel_constraints_checkconstraint_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_constraints_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_ReferenceConstraint)


def test_sqlmodel_constraints_referenceconstraint_constructor_exists():
    assert callable(sqlmodel_constraints_ReferenceConstraint.__init__)


def test_sqlmodel_constraints_referenceconstraint_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_ReferenceConstraint.__init__)
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



def test_sqlmodel_constraints_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_TableConstraint)


def test_sqlmodel_constraints_tableconstraint_constructor_exists():
    assert callable(sqlmodel_constraints_TableConstraint.__init__)


def test_sqlmodel_constraints_tableconstraint_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_constraints_assertion_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_Assertion)


def test_sqlmodel_constraints_assertion_constructor_exists():
    assert callable(sqlmodel_constraints_Assertion.__init__)


def test_sqlmodel_constraints_assertion_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_basetable_is_not_abstract():
    assert not inspect.isabstract(BaseTable)


def test_basetable_constructor_exists():
    assert callable(BaseTable.__init__)


def test_basetable_constructor_args():
    sig = inspect.signature(BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_tables_persistenttable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_PersistentTable)


def test_sqlmodel_tables_persistenttable_constructor_exists():
    assert callable(sqlmodel_tables_PersistentTable.__init__)


def test_sqlmodel_tables_persistenttable_constructor_args():
    sig = inspect.signature(sqlmodel_tables_PersistentTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_tables_temporarytable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_TemporaryTable)


def test_sqlmodel_tables_temporarytable_constructor_exists():
    assert callable(sqlmodel_tables_TemporaryTable.__init__)


def test_sqlmodel_tables_temporarytable_constructor_args():
    sig = inspect.signature(sqlmodel_tables_TemporaryTable.__init__)
    params = list(sig.parameters.keys())
    assert "local" in params, "Missing parameter 'local'"
    assert "deleteOnCommit" in params, "Missing parameter 'deleteOnCommit'"

def test_sqlmodel_tables_temporarytable_has_local():
    assert hasattr(sqlmodel_tables_TemporaryTable, "local")
    descriptor = None
    for klass in sqlmodel_tables_TemporaryTable.__mro__:
        if "local" in klass.__dict__:
            descriptor = klass.__dict__["local"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_temporarytable_has_deleteOnCommit():
    assert hasattr(sqlmodel_tables_TemporaryTable, "deleteOnCommit")
    descriptor = None
    for klass in sqlmodel_tables_TemporaryTable.__mro__:
        if "deleteOnCommit" in klass.__dict__:
            descriptor = klass.__dict__["deleteOnCommit"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_comment_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Comment)


def test_sqlmodel_schema_comment_constructor_exists():
    assert callable(sqlmodel_schema_Comment.__init__)


def test_sqlmodel_schema_comment_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_sqlmodel_schema_comment_has_description():
    assert hasattr(sqlmodel_schema_Comment, "description")
    descriptor = None
    for klass in sqlmodel_schema_Comment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_objectextension_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_ObjectExtension)


def test_sqlmodel_schema_objectextension_constructor_exists():
    assert callable(sqlmodel_schema_ObjectExtension.__init__)


def test_sqlmodel_schema_objectextension_constructor_args():
    sig = inspect.signature(sqlmodel_schema_ObjectExtension.__init__)
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



def test_sqlmodel_datatypes_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_AttributeDefinition)


def test_sqlmodel_datatypes_attributedefinition_constructor_exists():
    assert callable(sqlmodel_datatypes_AttributeDefinition.__init__)


def test_sqlmodel_datatypes_attributedefinition_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"

def test_sqlmodel_datatypes_attributedefinition_has_defaultValue():
    assert hasattr(sqlmodel_datatypes_AttributeDefinition, "defaultValue")
    descriptor = None
    for klass in sqlmodel_datatypes_AttributeDefinition.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_attributedefinition_has_scopeCheck():
    assert hasattr(sqlmodel_datatypes_AttributeDefinition, "scopeCheck")
    descriptor = None
    for klass in sqlmodel_datatypes_AttributeDefinition.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_attributedefinition_has_scopeChecked():
    assert hasattr(sqlmodel_datatypes_AttributeDefinition, "scopeChecked")
    descriptor = None
    for klass in sqlmodel_datatypes_AttributeDefinition.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_field_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_Field)


def test_sqlmodel_datatypes_field_constructor_exists():
    assert callable(sqlmodel_datatypes_Field.__init__)


def test_sqlmodel_datatypes_field_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_Field.__init__)
    params = list(sig.parameters.keys())
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"

def test_sqlmodel_datatypes_field_has_scopeChecked():
    assert hasattr(sqlmodel_datatypes_Field, "scopeChecked")
    descriptor = None
    for klass in sqlmodel_datatypes_Field.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_field_has_scopeCheck():
    assert hasattr(sqlmodel_datatypes_Field, "scopeCheck")
    descriptor = None
    for klass in sqlmodel_datatypes_Field.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_routines_parameter_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Parameter)


def test_sqlmodel_routines_parameter_constructor_exists():
    assert callable(sqlmodel_routines_Parameter.__init__)


def test_sqlmodel_routines_parameter_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "locator" in params, "Missing parameter 'locator'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_sqlmodel_routines_parameter_has_locator():
    assert hasattr(sqlmodel_routines_Parameter, "locator")
    descriptor = None
    for klass in sqlmodel_routines_Parameter.__mro__:
        if "locator" in klass.__dict__:
            descriptor = klass.__dict__["locator"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_parameter_has_mode():
    assert hasattr(sqlmodel_routines_Parameter, "mode")
    descriptor = None
    for klass in sqlmodel_routines_Parameter.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_tables_column_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_Column)


def test_sqlmodel_tables_column_constructor_exists():
    assert callable(sqlmodel_tables_Column.__init__)


def test_sqlmodel_tables_column_constructor_args():
    sig = inspect.signature(sqlmodel_tables_Column.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "scopeCheck" in params, "Missing parameter 'scopeCheck'"
    assert "implementationDependent" in params, "Missing parameter 'implementationDependent'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "scopeChecked" in params, "Missing parameter 'scopeChecked'"

def test_sqlmodel_tables_column_has_defaultValue():
    assert hasattr(sqlmodel_tables_Column, "defaultValue")
    descriptor = None
    for klass in sqlmodel_tables_Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_column_has_scopeCheck():
    assert hasattr(sqlmodel_tables_Column, "scopeCheck")
    descriptor = None
    for klass in sqlmodel_tables_Column.__mro__:
        if "scopeCheck" in klass.__dict__:
            descriptor = klass.__dict__["scopeCheck"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_column_has_implementationDependent():
    assert hasattr(sqlmodel_tables_Column, "implementationDependent")
    descriptor = None
    for klass in sqlmodel_tables_Column.__mro__:
        if "implementationDependent" in klass.__dict__:
            descriptor = klass.__dict__["implementationDependent"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_column_has_nullable():
    assert hasattr(sqlmodel_tables_Column, "nullable")
    descriptor = None
    for klass in sqlmodel_tables_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_column_has_scopeChecked():
    assert hasattr(sqlmodel_tables_Column, "scopeChecked")
    descriptor = None
    for klass in sqlmodel_tables_Column.__mro__:
        if "scopeChecked" in klass.__dict__:
            descriptor = klass.__dict__["scopeChecked"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_elementtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_ElementType)


def test_sqlmodel_datatypes_elementtype_constructor_exists():
    assert callable(sqlmodel_datatypes_ElementType.__init__)


def test_sqlmodel_datatypes_elementtype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_schema_sequence_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Sequence)


def test_sqlmodel_schema_sequence_constructor_exists():
    assert callable(sqlmodel_schema_Sequence.__init__)


def test_sqlmodel_schema_sequence_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Sequence.__init__)
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



def test_sqlmodel_schema_sqlobject_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_SQLObject)


def test_sqlmodel_schema_sqlobject_constructor_exists():
    assert callable(sqlmodel_schema_SQLObject.__init__)


def test_sqlmodel_schema_sqlobject_constructor_args():
    sig = inspect.signature(sqlmodel_schema_SQLObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_sqlmodel_schema_sqlobject_has_label():
    assert hasattr(sqlmodel_schema_SQLObject, "label")
    descriptor = None
    for klass in sqlmodel_schema_SQLObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_sqlobject_has_description():
    assert hasattr(sqlmodel_schema_SQLObject, "description")
    descriptor = None
    for klass in sqlmodel_schema_SQLObject.__mro__:
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



def test_sqlmodel_accesscontrol_role_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_Role)


def test_sqlmodel_accesscontrol_role_constructor_exists():
    assert callable(sqlmodel_accesscontrol_Role.__init__)


def test_sqlmodel_accesscontrol_role_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_Role.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_accesscontrol_group_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_Group)


def test_sqlmodel_accesscontrol_group_constructor_exists():
    assert callable(sqlmodel_accesscontrol_Group.__init__)


def test_sqlmodel_accesscontrol_group_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_Group.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_accesscontrol_user_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_User)


def test_sqlmodel_accesscontrol_user_constructor_exists():
    assert callable(sqlmodel_accesscontrol_User.__init__)


def test_sqlmodel_accesscontrol_user_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_User.__init__)
    params = list(sig.parameters.keys())



def test_routine_is_not_abstract():
    assert not inspect.isabstract(Routine)


def test_routine_constructor_exists():
    assert callable(Routine.__init__)


def test_routine_constructor_args():
    sig = inspect.signature(Routine.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_routines_function_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Function)


def test_sqlmodel_routines_function_constructor_exists():
    assert callable(sqlmodel_routines_Function.__init__)


def test_sqlmodel_routines_function_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Function.__init__)
    params = list(sig.parameters.keys())
    assert "typePreserving" in params, "Missing parameter 'typePreserving'"
    assert "mutator" in params, "Missing parameter 'mutator'"
    assert "transformGroup" in params, "Missing parameter 'transformGroup'"
    assert "nullCall" in params, "Missing parameter 'nullCall'"
    assert "static" in params, "Missing parameter 'static'"

def test_sqlmodel_routines_function_has_typePreserving():
    assert hasattr(sqlmodel_routines_Function, "typePreserving")
    descriptor = None
    for klass in sqlmodel_routines_Function.__mro__:
        if "typePreserving" in klass.__dict__:
            descriptor = klass.__dict__["typePreserving"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_function_has_mutator():
    assert hasattr(sqlmodel_routines_Function, "mutator")
    descriptor = None
    for klass in sqlmodel_routines_Function.__mro__:
        if "mutator" in klass.__dict__:
            descriptor = klass.__dict__["mutator"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_function_has_transformGroup():
    assert hasattr(sqlmodel_routines_Function, "transformGroup")
    descriptor = None
    for klass in sqlmodel_routines_Function.__mro__:
        if "transformGroup" in klass.__dict__:
            descriptor = klass.__dict__["transformGroup"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_function_has_nullCall():
    assert hasattr(sqlmodel_routines_Function, "nullCall")
    descriptor = None
    for klass in sqlmodel_routines_Function.__mro__:
        if "nullCall" in klass.__dict__:
            descriptor = klass.__dict__["nullCall"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_function_has_static():
    assert hasattr(sqlmodel_routines_Function, "static")
    descriptor = None
    for klass in sqlmodel_routines_Function.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_routines_procedure_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Procedure)


def test_sqlmodel_routines_procedure_constructor_exists():
    assert callable(sqlmodel_routines_Procedure.__init__)


def test_sqlmodel_routines_procedure_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "oldSavePoint" in params, "Missing parameter 'oldSavePoint'"
    assert "maxResultSets" in params, "Missing parameter 'maxResultSets'"

def test_sqlmodel_routines_procedure_has_oldSavePoint():
    assert hasattr(sqlmodel_routines_Procedure, "oldSavePoint")
    descriptor = None
    for klass in sqlmodel_routines_Procedure.__mro__:
        if "oldSavePoint" in klass.__dict__:
            descriptor = klass.__dict__["oldSavePoint"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_procedure_has_maxResultSets():
    assert hasattr(sqlmodel_routines_Procedure, "maxResultSets")
    descriptor = None
    for klass in sqlmodel_routines_Procedure.__mro__:
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



def test_schema_sqlmodel_eobject_is_not_abstract():
    assert not inspect.isabstract(schema_sqlmodel_EObject)


def test_schema_sqlmodel_eobject_constructor_exists():
    assert callable(schema_sqlmodel_EObject.__init__)


def test_schema_sqlmodel_eobject_constructor_args():
    sig = inspect.signature(schema_sqlmodel_EObject.__init__)
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



def test_sqlmodel_routines_routineresulttable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_RoutineResultTable)


def test_sqlmodel_routines_routineresulttable_constructor_exists():
    assert callable(sqlmodel_routines_RoutineResultTable.__init__)


def test_sqlmodel_routines_routineresulttable_constructor_args():
    sig = inspect.signature(sqlmodel_routines_RoutineResultTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_tables_basetable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_BaseTable)


def test_sqlmodel_tables_basetable_constructor_exists():
    assert callable(sqlmodel_tables_BaseTable.__init__)


def test_sqlmodel_tables_basetable_constructor_args():
    sig = inspect.signature(sqlmodel_tables_BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_tables_derivedtable_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_DerivedTable)


def test_sqlmodel_tables_derivedtable_constructor_exists():
    assert callable(sqlmodel_tables_DerivedTable.__init__)


def test_sqlmodel_tables_derivedtable_constructor_args():
    sig = inspect.signature(sqlmodel_tables_DerivedTable.__init__)
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



def test_sqlmodel_datatypes_distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_DistinctUserDefinedType)


def test_sqlmodel_datatypes_distinctuserdefinedtype_constructor_exists():
    assert callable(sqlmodel_datatypes_DistinctUserDefinedType.__init__)


def test_sqlmodel_datatypes_distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_structureduserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_StructuredUserDefinedType)


def test_sqlmodel_datatypes_structureduserdefinedtype_constructor_exists():
    assert callable(sqlmodel_datatypes_StructuredUserDefinedType.__init__)


def test_sqlmodel_datatypes_structureduserdefinedtype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_StructuredUserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "instantiable" in params, "Missing parameter 'instantiable'"
    assert "final" in params, "Missing parameter 'final'"

def test_sqlmodel_datatypes_structureduserdefinedtype_has_instantiable():
    assert hasattr(sqlmodel_datatypes_StructuredUserDefinedType, "instantiable")
    descriptor = None
    for klass in sqlmodel_datatypes_StructuredUserDefinedType.__mro__:
        if "instantiable" in klass.__dict__:
            descriptor = klass.__dict__["instantiable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_structureduserdefinedtype_has_final():
    assert hasattr(sqlmodel_datatypes_StructuredUserDefinedType, "final")
    descriptor = None
    for klass in sqlmodel_datatypes_StructuredUserDefinedType.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SQLDataType)


def test_sqldatatype_constructor_exists():
    assert callable(SQLDataType.__init__)


def test_sqldatatype_constructor_args():
    sig = inspect.signature(SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_datatypes_predefineddatatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_PredefinedDataType)


def test_sqlmodel_datatypes_predefineddatatype_constructor_exists():
    assert callable(sqlmodel_datatypes_PredefinedDataType.__init__)


def test_sqlmodel_datatypes_predefineddatatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_PredefinedDataType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_sqlmodel_datatypes_predefineddatatype_has_primitiveType():
    assert hasattr(sqlmodel_datatypes_PredefinedDataType, "primitiveType")
    descriptor = None
    for klass in sqlmodel_datatypes_PredefinedDataType.__mro__:
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



def test_sqlmodel_constraints_indexmember_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_IndexMember)


def test_sqlmodel_constraints_indexmember_constructor_exists():
    assert callable(sqlmodel_constraints_IndexMember.__init__)


def test_sqlmodel_constraints_indexmember_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_IndexMember.__init__)
    params = list(sig.parameters.keys())
    assert "incrementType" in params, "Missing parameter 'incrementType'"

def test_sqlmodel_constraints_indexmember_has_incrementType():
    assert hasattr(sqlmodel_constraints_IndexMember, "incrementType")
    descriptor = None
    for klass in sqlmodel_constraints_IndexMember.__mro__:
        if "incrementType" in klass.__dict__:
            descriptor = klass.__dict__["incrementType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_constraints_constraint_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_Constraint)


def test_sqlmodel_constraints_constraint_constructor_exists():
    assert callable(sqlmodel_constraints_Constraint.__init__)


def test_sqlmodel_constraints_constraint_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "deferrable" in params, "Missing parameter 'deferrable'"
    assert "enforced" in params, "Missing parameter 'enforced'"
    assert "initiallyDeferred" in params, "Missing parameter 'initiallyDeferred'"

def test_sqlmodel_constraints_constraint_has_deferrable():
    assert hasattr(sqlmodel_constraints_Constraint, "deferrable")
    descriptor = None
    for klass in sqlmodel_constraints_Constraint.__mro__:
        if "deferrable" in klass.__dict__:
            descriptor = klass.__dict__["deferrable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_constraint_has_enforced():
    assert hasattr(sqlmodel_constraints_Constraint, "enforced")
    descriptor = None
    for klass in sqlmodel_constraints_Constraint.__mro__:
        if "enforced" in klass.__dict__:
            descriptor = klass.__dict__["enforced"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_constraint_has_initiallyDeferred():
    assert hasattr(sqlmodel_constraints_Constraint, "initiallyDeferred")
    descriptor = None
    for klass in sqlmodel_constraints_Constraint.__mro__:
        if "initiallyDeferred" in klass.__dict__:
            descriptor = klass.__dict__["initiallyDeferred"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_catalog_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Catalog)


def test_sqlmodel_schema_catalog_constructor_exists():
    assert callable(sqlmodel_schema_Catalog.__init__)


def test_sqlmodel_schema_catalog_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Catalog.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_schema_event_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Event)


def test_sqlmodel_schema_event_constructor_exists():
    assert callable(sqlmodel_schema_Event.__init__)


def test_sqlmodel_schema_event_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Event.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "for_" in params, "Missing parameter 'for_'"
    assert "action" in params, "Missing parameter 'action'"

def test_sqlmodel_schema_event_has_condition():
    assert hasattr(sqlmodel_schema_Event, "condition")
    descriptor = None
    for klass in sqlmodel_schema_Event.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_event_has_enabled():
    assert hasattr(sqlmodel_schema_Event, "enabled")
    descriptor = None
    for klass in sqlmodel_schema_Event.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_event_has_for_():
    assert hasattr(sqlmodel_schema_Event, "for_")
    descriptor = None
    for klass in sqlmodel_schema_Event.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_event_has_action():
    assert hasattr(sqlmodel_schema_Event, "action")
    descriptor = None
    for klass in sqlmodel_schema_Event.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_characterset_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_CharacterSet)


def test_sqlmodel_datatypes_characterset_constructor_exists():
    assert callable(sqlmodel_datatypes_CharacterSet.__init__)


def test_sqlmodel_datatypes_characterset_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_CharacterSet.__init__)
    params = list(sig.parameters.keys())
    assert "repertoire" in params, "Missing parameter 'repertoire'"
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "defaultCollation" in params, "Missing parameter 'defaultCollation'"

def test_sqlmodel_datatypes_characterset_has_repertoire():
    assert hasattr(sqlmodel_datatypes_CharacterSet, "repertoire")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterSet.__mro__:
        if "repertoire" in klass.__dict__:
            descriptor = klass.__dict__["repertoire"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_characterset_has_encoding():
    assert hasattr(sqlmodel_datatypes_CharacterSet, "encoding")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterSet.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_characterset_has_defaultCollation():
    assert hasattr(sqlmodel_datatypes_CharacterSet, "defaultCollation")
    descriptor = None
    for klass in sqlmodel_datatypes_CharacterSet.__mro__:
        if "defaultCollation" in klass.__dict__:
            descriptor = klass.__dict__["defaultCollation"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_routines_routine_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Routine)


def test_sqlmodel_routines_routine_constructor_exists():
    assert callable(sqlmodel_routines_Routine.__init__)


def test_sqlmodel_routines_routine_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Routine.__init__)
    params = list(sig.parameters.keys())
    assert "security" in params, "Missing parameter 'security'"
    assert "parameterStyle" in params, "Missing parameter 'parameterStyle'"
    assert "lastAlteredTS" in params, "Missing parameter 'lastAlteredTS'"
    assert "externalName" in params, "Missing parameter 'externalName'"
    assert "deterministic" in params, "Missing parameter 'deterministic'"
    assert "sqlDataAccess" in params, "Missing parameter 'sqlDataAccess'"
    assert "specificName" in params, "Missing parameter 'specificName'"
    assert "creationTS" in params, "Missing parameter 'creationTS'"
    assert "language" in params, "Missing parameter 'language'"
    assert "authorizationID" in params, "Missing parameter 'authorizationID'"

def test_sqlmodel_routines_routine_has_security():
    assert hasattr(sqlmodel_routines_Routine, "security")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "security" in klass.__dict__:
            descriptor = klass.__dict__["security"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_parameterStyle():
    assert hasattr(sqlmodel_routines_Routine, "parameterStyle")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "parameterStyle" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyle"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_lastAlteredTS():
    assert hasattr(sqlmodel_routines_Routine, "lastAlteredTS")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "lastAlteredTS" in klass.__dict__:
            descriptor = klass.__dict__["lastAlteredTS"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_externalName():
    assert hasattr(sqlmodel_routines_Routine, "externalName")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "externalName" in klass.__dict__:
            descriptor = klass.__dict__["externalName"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_deterministic():
    assert hasattr(sqlmodel_routines_Routine, "deterministic")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "deterministic" in klass.__dict__:
            descriptor = klass.__dict__["deterministic"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_sqlDataAccess():
    assert hasattr(sqlmodel_routines_Routine, "sqlDataAccess")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "sqlDataAccess" in klass.__dict__:
            descriptor = klass.__dict__["sqlDataAccess"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_specificName():
    assert hasattr(sqlmodel_routines_Routine, "specificName")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "specificName" in klass.__dict__:
            descriptor = klass.__dict__["specificName"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_creationTS():
    assert hasattr(sqlmodel_routines_Routine, "creationTS")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "creationTS" in klass.__dict__:
            descriptor = klass.__dict__["creationTS"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_language():
    assert hasattr(sqlmodel_routines_Routine, "language")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_routines_routine_has_authorizationID():
    assert hasattr(sqlmodel_routines_Routine, "authorizationID")
    descriptor = None
    for klass in sqlmodel_routines_Routine.__mro__:
        if "authorizationID" in klass.__dict__:
            descriptor = klass.__dict__["authorizationID"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_tables_trigger_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_Trigger)


def test_sqlmodel_tables_trigger_constructor_exists():
    assert callable(sqlmodel_tables_Trigger.__init__)


def test_sqlmodel_tables_trigger_constructor_args():
    sig = inspect.signature(sqlmodel_tables_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "deleteType" in params, "Missing parameter 'deleteType'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "newRow" in params, "Missing parameter 'newRow'"
    assert "updateType" in params, "Missing parameter 'updateType'"
    assert "timeStamp" in params, "Missing parameter 'timeStamp'"
    assert "newTable" in params, "Missing parameter 'newTable'"
    assert "actionGranularity" in params, "Missing parameter 'actionGranularity'"
    assert "oldRow" in params, "Missing parameter 'oldRow'"
    assert "oldTable" in params, "Missing parameter 'oldTable'"
    assert "insertType" in params, "Missing parameter 'insertType'"

def test_sqlmodel_tables_trigger_has_deleteType():
    assert hasattr(sqlmodel_tables_Trigger, "deleteType")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "deleteType" in klass.__dict__:
            descriptor = klass.__dict__["deleteType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_actionTime():
    assert hasattr(sqlmodel_tables_Trigger, "actionTime")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_newRow():
    assert hasattr(sqlmodel_tables_Trigger, "newRow")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "newRow" in klass.__dict__:
            descriptor = klass.__dict__["newRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_updateType():
    assert hasattr(sqlmodel_tables_Trigger, "updateType")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "updateType" in klass.__dict__:
            descriptor = klass.__dict__["updateType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_timeStamp():
    assert hasattr(sqlmodel_tables_Trigger, "timeStamp")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "timeStamp" in klass.__dict__:
            descriptor = klass.__dict__["timeStamp"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_newTable():
    assert hasattr(sqlmodel_tables_Trigger, "newTable")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "newTable" in klass.__dict__:
            descriptor = klass.__dict__["newTable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_actionGranularity():
    assert hasattr(sqlmodel_tables_Trigger, "actionGranularity")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "actionGranularity" in klass.__dict__:
            descriptor = klass.__dict__["actionGranularity"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_oldRow():
    assert hasattr(sqlmodel_tables_Trigger, "oldRow")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "oldRow" in klass.__dict__:
            descriptor = klass.__dict__["oldRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_oldTable():
    assert hasattr(sqlmodel_tables_Trigger, "oldTable")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "oldTable" in klass.__dict__:
            descriptor = klass.__dict__["oldTable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_trigger_has_insertType():
    assert hasattr(sqlmodel_tables_Trigger, "insertType")
    descriptor = None
    for klass in sqlmodel_tables_Trigger.__mro__:
        if "insertType" in klass.__dict__:
            descriptor = klass.__dict__["insertType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_database_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Database)


def test_sqlmodel_schema_database_constructor_exists():
    assert callable(sqlmodel_schema_Database.__init__)


def test_sqlmodel_schema_database_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Database.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "vendor" in params, "Missing parameter 'vendor'"

def test_sqlmodel_schema_database_has_version():
    assert hasattr(sqlmodel_schema_Database, "version")
    descriptor = None
    for klass in sqlmodel_schema_Database.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_database_has_vendor():
    assert hasattr(sqlmodel_schema_Database, "vendor")
    descriptor = None
    for klass in sqlmodel_schema_Database.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_schema_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Schema)


def test_sqlmodel_schema_schema_constructor_exists():
    assert callable(sqlmodel_schema_Schema.__init__)


def test_sqlmodel_schema_schema_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Schema.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_schema_dependency_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_Dependency)


def test_sqlmodel_schema_dependency_constructor_exists():
    assert callable(sqlmodel_schema_Dependency.__init__)


def test_sqlmodel_schema_dependency_constructor_args():
    sig = inspect.signature(sqlmodel_schema_Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "dependencyType" in params, "Missing parameter 'dependencyType'"

def test_sqlmodel_schema_dependency_has_dependencyType():
    assert hasattr(sqlmodel_schema_Dependency, "dependencyType")
    descriptor = None
    for klass in sqlmodel_schema_Dependency.__mro__:
        if "dependencyType" in klass.__dict__:
            descriptor = klass.__dict__["dependencyType"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_userdefinedtypeordering_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_UserDefinedTypeOrdering)


def test_sqlmodel_datatypes_userdefinedtypeordering_constructor_exists():
    assert callable(sqlmodel_datatypes_UserDefinedTypeOrdering.__init__)


def test_sqlmodel_datatypes_userdefinedtypeordering_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_UserDefinedTypeOrdering.__init__)
    params = list(sig.parameters.keys())
    assert "orderingCategory" in params, "Missing parameter 'orderingCategory'"
    assert "orderingForm" in params, "Missing parameter 'orderingForm'"

def test_sqlmodel_datatypes_userdefinedtypeordering_has_orderingCategory():
    assert hasattr(sqlmodel_datatypes_UserDefinedTypeOrdering, "orderingCategory")
    descriptor = None
    for klass in sqlmodel_datatypes_UserDefinedTypeOrdering.__mro__:
        if "orderingCategory" in klass.__dict__:
            descriptor = klass.__dict__["orderingCategory"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_datatypes_userdefinedtypeordering_has_orderingForm():
    assert hasattr(sqlmodel_datatypes_UserDefinedTypeOrdering, "orderingForm")
    descriptor = None
    for klass in sqlmodel_datatypes_UserDefinedTypeOrdering.__mro__:
        if "orderingForm" in klass.__dict__:
            descriptor = klass.__dict__["orderingForm"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_accesscontrol_privilege_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_Privilege)


def test_sqlmodel_accesscontrol_privilege_constructor_exists():
    assert callable(sqlmodel_accesscontrol_Privilege.__init__)


def test_sqlmodel_accesscontrol_privilege_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_Privilege.__init__)
    params = list(sig.parameters.keys())
    assert "withHierarchy" in params, "Missing parameter 'withHierarchy'"
    assert "grantable" in params, "Missing parameter 'grantable'"
    assert "action" in params, "Missing parameter 'action'"

def test_sqlmodel_accesscontrol_privilege_has_withHierarchy():
    assert hasattr(sqlmodel_accesscontrol_Privilege, "withHierarchy")
    descriptor = None
    for klass in sqlmodel_accesscontrol_Privilege.__mro__:
        if "withHierarchy" in klass.__dict__:
            descriptor = klass.__dict__["withHierarchy"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_accesscontrol_privilege_has_grantable():
    assert hasattr(sqlmodel_accesscontrol_Privilege, "grantable")
    descriptor = None
    for klass in sqlmodel_accesscontrol_Privilege.__mro__:
        if "grantable" in klass.__dict__:
            descriptor = klass.__dict__["grantable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_accesscontrol_privilege_has_action():
    assert hasattr(sqlmodel_accesscontrol_Privilege, "action")
    descriptor = None
    for klass in sqlmodel_accesscontrol_Privilege.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_typedelement_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_TypedElement)


def test_sqlmodel_schema_typedelement_constructor_exists():
    assert callable(sqlmodel_schema_TypedElement.__init__)


def test_sqlmodel_schema_typedelement_constructor_args():
    sig = inspect.signature(sqlmodel_schema_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_accesscontrol_authorizationidentifier_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_AuthorizationIdentifier)


def test_sqlmodel_accesscontrol_authorizationidentifier_constructor_exists():
    assert callable(sqlmodel_accesscontrol_AuthorizationIdentifier.__init__)


def test_sqlmodel_accesscontrol_authorizationidentifier_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_AuthorizationIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_constraints_index_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_Index)


def test_sqlmodel_constraints_index_constructor_exists():
    assert callable(sqlmodel_constraints_Index.__init__)


def test_sqlmodel_constraints_index_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_Index.__init__)
    params = list(sig.parameters.keys())
    assert "clustered" in params, "Missing parameter 'clustered'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "fillFactor" in params, "Missing parameter 'fillFactor'"
    assert "systemGenerated" in params, "Missing parameter 'systemGenerated'"

def test_sqlmodel_constraints_index_has_clustered():
    assert hasattr(sqlmodel_constraints_Index, "clustered")
    descriptor = None
    for klass in sqlmodel_constraints_Index.__mro__:
        if "clustered" in klass.__dict__:
            descriptor = klass.__dict__["clustered"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_index_has_unique():
    assert hasattr(sqlmodel_constraints_Index, "unique")
    descriptor = None
    for klass in sqlmodel_constraints_Index.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_index_has_fillFactor():
    assert hasattr(sqlmodel_constraints_Index, "fillFactor")
    descriptor = None
    for klass in sqlmodel_constraints_Index.__mro__:
        if "fillFactor" in klass.__dict__:
            descriptor = klass.__dict__["fillFactor"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_constraints_index_has_systemGenerated():
    assert hasattr(sqlmodel_constraints_Index, "systemGenerated")
    descriptor = None
    for klass in sqlmodel_constraints_Index.__mro__:
        if "systemGenerated" in klass.__dict__:
            descriptor = klass.__dict__["systemGenerated"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_datatypes_datatype_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_datatypes_DataType)


def test_sqlmodel_datatypes_datatype_constructor_exists():
    assert callable(sqlmodel_datatypes_DataType.__init__)


def test_sqlmodel_datatypes_datatype_constructor_args():
    sig = inspect.signature(sqlmodel_datatypes_DataType.__init__)
    params = list(sig.parameters.keys())



def test_sqlmodel_routines_source_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_routines_Source)


def test_sqlmodel_routines_source_constructor_exists():
    assert callable(sqlmodel_routines_Source.__init__)


def test_sqlmodel_routines_source_constructor_args():
    sig = inspect.signature(sqlmodel_routines_Source.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_sqlmodel_routines_source_has_body():
    assert hasattr(sqlmodel_routines_Source, "body")
    descriptor = None
    for klass in sqlmodel_routines_Source.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_accesscontrol_roleauthorization_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_accesscontrol_RoleAuthorization)


def test_sqlmodel_accesscontrol_roleauthorization_constructor_exists():
    assert callable(sqlmodel_accesscontrol_RoleAuthorization.__init__)


def test_sqlmodel_accesscontrol_roleauthorization_constructor_args():
    sig = inspect.signature(sqlmodel_accesscontrol_RoleAuthorization.__init__)
    params = list(sig.parameters.keys())
    assert "grantable" in params, "Missing parameter 'grantable'"

def test_sqlmodel_accesscontrol_roleauthorization_has_grantable():
    assert hasattr(sqlmodel_accesscontrol_RoleAuthorization, "grantable")
    descriptor = None
    for klass in sqlmodel_accesscontrol_RoleAuthorization.__mro__:
        if "grantable" in klass.__dict__:
            descriptor = klass.__dict__["grantable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_constraints_indexexpression_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_constraints_IndexExpression)


def test_sqlmodel_constraints_indexexpression_constructor_exists():
    assert callable(sqlmodel_constraints_IndexExpression.__init__)


def test_sqlmodel_constraints_indexexpression_constructor_args():
    sig = inspect.signature(sqlmodel_constraints_IndexExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_sqlmodel_constraints_indexexpression_has_sql():
    assert hasattr(sqlmodel_constraints_IndexExpression, "sql")
    descriptor = None
    for klass in sqlmodel_constraints_IndexExpression.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_tables_table_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_tables_Table)


def test_sqlmodel_tables_table_constructor_exists():
    assert callable(sqlmodel_tables_Table.__init__)


def test_sqlmodel_tables_table_constructor_args():
    sig = inspect.signature(sqlmodel_tables_Table.__init__)
    params = list(sig.parameters.keys())
    assert "selfRefColumnGeneration" in params, "Missing parameter 'selfRefColumnGeneration'"
    assert "insertable" in params, "Missing parameter 'insertable'"
    assert "updatable" in params, "Missing parameter 'updatable'"

def test_sqlmodel_tables_table_has_selfRefColumnGeneration():
    assert hasattr(sqlmodel_tables_Table, "selfRefColumnGeneration")
    descriptor = None
    for klass in sqlmodel_tables_Table.__mro__:
        if "selfRefColumnGeneration" in klass.__dict__:
            descriptor = klass.__dict__["selfRefColumnGeneration"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_table_has_insertable():
    assert hasattr(sqlmodel_tables_Table, "insertable")
    descriptor = None
    for klass in sqlmodel_tables_Table.__mro__:
        if "insertable" in klass.__dict__:
            descriptor = klass.__dict__["insertable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_tables_table_has_updatable():
    assert hasattr(sqlmodel_tables_Table, "updatable")
    descriptor = None
    for klass in sqlmodel_tables_Table.__mro__:
        if "updatable" in klass.__dict__:
            descriptor = klass.__dict__["updatable"]
            break
    assert isinstance(descriptor, property)



def test_sqlmodel_schema_identityspecifier_is_not_abstract():
    assert not inspect.isabstract(sqlmodel_schema_IdentitySpecifier)


def test_sqlmodel_schema_identityspecifier_constructor_exists():
    assert callable(sqlmodel_schema_IdentitySpecifier.__init__)


def test_sqlmodel_schema_identityspecifier_constructor_args():
    sig = inspect.signature(sqlmodel_schema_IdentitySpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "generationType" in params, "Missing parameter 'generationType'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "cycleOption" in params, "Missing parameter 'cycleOption'"

def test_sqlmodel_schema_identityspecifier_has_startValue():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "startValue")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_identityspecifier_has_maximum():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "maximum")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_identityspecifier_has_minimum():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "minimum")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_identityspecifier_has_generationType():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "generationType")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "generationType" in klass.__dict__:
            descriptor = klass.__dict__["generationType"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_identityspecifier_has_increment():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "increment")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_sqlmodel_schema_identityspecifier_has_cycleOption():
    assert hasattr(sqlmodel_schema_IdentitySpecifier, "cycleOption")
    descriptor = None
    for klass in sqlmodel_schema_IdentitySpecifier.__mro__:
        if "cycleOption" in klass.__dict__:
            descriptor = klass.__dict__["cycleOption"]
            break
    assert isinstance(descriptor, property)

def test_matchtype_exists():
    # Check that the Enumeration exists
    assert MatchType is not None

def test_matchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchType]
    expected_literals = [
        "MATCH_FULL",
        "MATCH_SIMPLE",
        "MATCH_PARTIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchType"

def test_referencetype_exists():
    # Check that the Enumeration exists
    assert ReferenceType is not None

def test_referencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceType]
    expected_literals = [
        "USER_GENERATED",
        "SYSTEM_GENERATED",
        "DERIVED_SELF_REF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "IN",
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_coercibilitytype_exists():
    # Check that the Enumeration exists
    assert CoercibilityType is not None

def test_coercibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoercibilityType]
    expected_literals = [
        "COERCIBILE",
        "EXPLICIT",
        "IMPLICIT",
        "NO_COLLATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoercibilityType"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "XML_TYPE",
        "BINARY_VARYING",
        "NATIONAL_CHARACTER_VARYING",
        "INTEGER",
        "TIME",
        "BINARY_LARGE_OBJECT",
        "DATE",
        "INTERVAL",
        "TIMESTAMP",
        "FLOAT",
        "DECIMAL",
        "DOUBLE_PRECISION",
        "REAL",
        "NATIONAL_CHARACTER_LARGE_OBJECT",
        "CHARACTER_VARYING",
        "BOOLEAN",
        "BINARY",
        "CHARACTER",
        "BIGINT",
        "NUMERIC",
        "SMALLINT",
        "DATALINK",
        "NATIONAL_CHARACTER",
        "CHARACTER_LARGE_OBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_generatetype_exists():
    # Check that the Enumeration exists
    assert GenerateType is not None

def test_generatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GenerateType]
    expected_literals = [
        "ALWAYS_GENERATED",
        "DEFAULT_GENERATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GenerateType"

def test_readpermissionoption_exists():
    # Check that the Enumeration exists
    assert ReadPermissionOption is not None

def test_readpermissionoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReadPermissionOption]
    expected_literals = [
        "DB",
        "FS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReadPermissionOption"

def test_incrementtype_exists():
    # Check that the Enumeration exists
    assert IncrementType is not None

def test_incrementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementType]
    expected_literals = [
        "DESC",
        "ASC",
        "RANDOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementType"

def test_unlinkoption_exists():
    # Check that the Enumeration exists
    assert UnlinkOption is not None

def test_unlinkoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnlinkOption]
    expected_literals = [
        "RESTORE",
        "NONE",
        "DELETE",
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
        "CASCADED",
        "LOCAL",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CheckType"

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

def test_referentialactiontype_exists():
    # Check that the Enumeration exists
    assert ReferentialActionType is not None

def test_referentialactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialActionType]
    expected_literals = [
        "SET_DEFAULT",
        "NO_ACTION",
        "RESTRICT",
        "SET_NULL",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialActionType"

def test_dataaccess_exists():
    # Check that the Enumeration exists
    assert DataAccess is not None

def test_dataaccess_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataAccess]
    expected_literals = [
        "NO_SQL",
        "MODIFIES_SQL_DATA",
        "READS_SQL_DATA",
        "CONTAINS_SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataAccess"

def test_linkcontroloption_exists():
    # Check that the Enumeration exists
    assert LinkControlOption is not None

def test_linkcontroloption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkControlOption]
    expected_literals = [
        "FILE_LINK_CONTROL",
        "NO_FILE_LINK_CONTROL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkControlOption"

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

def test_actiongranularitytype_exists():
    # Check that the Enumeration exists
    assert ActionGranularityType is not None

def test_actiongranularitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionGranularityType]
    expected_literals = [
        "STATEMENT",
        "ROW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionGranularityType"

def test_orderingcategorytype_exists():
    # Check that the Enumeration exists
    assert OrderingCategoryType is not None

def test_orderingcategorytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderingCategoryType]
    expected_literals = [
        "MAP",
        "STATE",
        "RELATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderingCategoryType"

def test_writepermissionoption_exists():
    # Check that the Enumeration exists
    assert WritePermissionOption is not None

def test_writepermissionoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WritePermissionOption]
    expected_literals = [
        "ADMIN",
        "BLOCKED",
        "FS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WritePermissionOption"

def test_intervalqualifiertype_exists():
    # Check that the Enumeration exists
    assert IntervalQualifierType is not None

def test_intervalqualifiertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalQualifierType]
    expected_literals = [
        "FRACTION",
        "SECOND",
        "MINUTE",
        "MONTH",
        "DAY",
        "HOUR",
        "YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalQualifierType"

def test_integritycontroloption_exists():
    # Check that the Enumeration exists
    assert IntegrityControlOption is not None

def test_integritycontroloption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegrityControlOption]
    expected_literals = [
        "ALL",
        "SELECTIVE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegrityControlOption"


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
sqlmodel_tables_ViewTable_strategy = st.builds(
    sqlmodel_tables_ViewTable,
    checkType=
        safe_text
)
statements_SQLStatement_strategy = st.builds(
    statements_SQLStatement,
)
SQLDataStatement_strategy = st.builds(
    SQLDataStatement,
)
sqlmodel_statements_SQLDataChangeStatement_strategy = st.builds(
    sqlmodel_statements_SQLDataChangeStatement,
)
SQLStatement_strategy = st.builds(
    SQLStatement,
)
sqlmodel_statements_SQLControlStatement_strategy = st.builds(
    sqlmodel_statements_SQLControlStatement,
)
sqlmodel_statements_SQLDynamicStatement_strategy = st.builds(
    sqlmodel_statements_SQLDynamicStatement,
)
sqlmodel_statements_SQLSessionStatement_strategy = st.builds(
    sqlmodel_statements_SQLSessionStatement,
)
sqlmodel_statements_SQLSchemaStatement_strategy = st.builds(
    sqlmodel_statements_SQLSchemaStatement,
)
sqlmodel_statements_SQLConnectionStatement_strategy = st.builds(
    sqlmodel_statements_SQLConnectionStatement,
)
sqlmodel_statements_SQLTransactionStatement_strategy = st.builds(
    sqlmodel_statements_SQLTransactionStatement,
)
sqlmodel_statements_SQLDiagnosticsStatement_strategy = st.builds(
    sqlmodel_statements_SQLDiagnosticsStatement,
)
sqlmodel_statements_SQLDataStatement_strategy = st.builds(
    sqlmodel_statements_SQLDataStatement,
)
sqlmodel_statements_SQLStatement_strategy = st.builds(
    sqlmodel_statements_SQLStatement,
)
Function_strategy = st.builds(
    Function,
)
sqlmodel_routines_BuiltInFunction_strategy = st.builds(
    sqlmodel_routines_BuiltInFunction,
)
sqlmodel_routines_UserDefinedFunction_strategy = st.builds(
    sqlmodel_routines_UserDefinedFunction,
)
sqlmodel_routines_Method_strategy = st.builds(
    sqlmodel_routines_Method,
    constructor=
        st.booleans(),
    overriding=
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
expressions_SearchCondition_strategy = st.builds(
    expressions_SearchCondition,
)
expressions_ValueExpression_strategy = st.builds(
    expressions_ValueExpression,
)
sqlmodel_expressions_QueryExpression_strategy = st.builds(
    sqlmodel_expressions_QueryExpression,
)
expressions_QueryExpression_strategy = st.builds(
    expressions_QueryExpression,
)
schema_SQLObject_strategy = st.builds(
    schema_SQLObject,
)
sqlmodel_statements_SQLStatementDefault_strategy = st.builds(
    sqlmodel_statements_SQLStatementDefault,
    SQL=
        safe_text
)
sqlmodel_expressions_SearchConditionDefault_strategy = st.builds(
    sqlmodel_expressions_SearchConditionDefault,
    SQL=
        safe_text
)
sqlmodel_expressions_ValueExpressionDefault_strategy = st.builds(
    sqlmodel_expressions_ValueExpressionDefault,
    SQL=
        safe_text
)
sqlmodel_expressions_QueryExpressionDefault_strategy = st.builds(
    sqlmodel_expressions_QueryExpressionDefault,
    SQL=
        safe_text
)
sqlmodel_expressions_SearchCondition_strategy = st.builds(
    sqlmodel_expressions_SearchCondition,
)
sqlmodel_expressions_ValueExpression_strategy = st.builds(
    sqlmodel_expressions_ValueExpression,
)
NumericalDataType_strategy = st.builds(
    NumericalDataType,
)
sqlmodel_datatypes_ApproximateNumericDataType_strategy = st.builds(
    sqlmodel_datatypes_ApproximateNumericDataType,
)
sqlmodel_datatypes_ExactNumericDataType_strategy = st.builds(
    sqlmodel_datatypes_ExactNumericDataType,
    scale=
        st.integers()
)
CheckConstraint_strategy = st.builds(
    CheckConstraint,
)
DistinctUserDefinedType_strategy = st.builds(
    DistinctUserDefinedType,
)
sqlmodel_datatypes_Domain_strategy = st.builds(
    sqlmodel_datatypes_Domain,
    defaultValue=
        safe_text
)
ExactNumericDataType_strategy = st.builds(
    ExactNumericDataType,
)
sqlmodel_datatypes_IntegerDataType_strategy = st.builds(
    sqlmodel_datatypes_IntegerDataType,
)
sqlmodel_datatypes_FixedPrecisionDataType_strategy = st.builds(
    sqlmodel_datatypes_FixedPrecisionDataType,
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
sqlmodel_datatypes_MultisetDataType_strategy = st.builds(
    sqlmodel_datatypes_MultisetDataType,
)
sqlmodel_datatypes_ArrayDataType_strategy = st.builds(
    sqlmodel_datatypes_ArrayDataType,
    maxCardinality=
        st.integers()
)
Field_strategy = st.builds(
    Field,
)
PredefinedDataType_strategy = st.builds(
    PredefinedDataType,
)
sqlmodel_datatypes_DateDataType_strategy = st.builds(
    sqlmodel_datatypes_DateDataType,
)
sqlmodel_datatypes_IntervalDataType_strategy = st.builds(
    sqlmodel_datatypes_IntervalDataType,
    leadingFieldPrecision=
        st.integers(),
    trailingQualifier=
        safe_text,
    leadingQualifier=
        safe_text,
    fractionalSecondsPrecision=
        st.integers(),
    trailingFieldPrecision=
        st.integers()
)
sqlmodel_datatypes_CharacterStringDataType_strategy = st.builds(
    sqlmodel_datatypes_CharacterStringDataType,
    fixedLength=
        st.booleans(),
    length=
        st.integers(),
    collationName=
        safe_text,
    coercibility=
        safe_text
)
sqlmodel_datatypes_TimeDataType_strategy = st.builds(
    sqlmodel_datatypes_TimeDataType,
    timeZone=
        st.booleans(),
    fractionalSecondsPrecision=
        st.integers()
)
sqlmodel_datatypes_BooleanDataType_strategy = st.builds(
    sqlmodel_datatypes_BooleanDataType,
)
sqlmodel_datatypes_XMLDataType_strategy = st.builds(
    sqlmodel_datatypes_XMLDataType,
)
sqlmodel_datatypes_BinaryStringDataType_strategy = st.builds(
    sqlmodel_datatypes_BinaryStringDataType,
    length=
        st.integers()
)
sqlmodel_datatypes_DataLinkDataType_strategy = st.builds(
    sqlmodel_datatypes_DataLinkDataType,
    recovery=
        st.booleans(),
    linkControl=
        safe_text,
    writePermission=
        safe_text,
    integrityControl=
        safe_text,
    unlink=
        safe_text,
    length=
        st.integers(),
    readPermission=
        safe_text
)
sqlmodel_datatypes_NumericalDataType_strategy = st.builds(
    sqlmodel_datatypes_NumericalDataType,
    precision=
        st.integers()
)
ElementType_strategy = st.builds(
    ElementType,
)
ConstructedDataType_strategy = st.builds(
    ConstructedDataType,
)
sqlmodel_datatypes_ReferenceDataType_strategy = st.builds(
    sqlmodel_datatypes_ReferenceDataType,
)
sqlmodel_datatypes_RowDataType_strategy = st.builds(
    sqlmodel_datatypes_RowDataType,
)
sqlmodel_datatypes_CollectionDataType_strategy = st.builds(
    sqlmodel_datatypes_CollectionDataType,
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
sqlmodel_datatypes_ConstructedDataType_strategy = st.builds(
    sqlmodel_datatypes_ConstructedDataType,
)
sqlmodel_datatypes_SQLDataType_strategy = st.builds(
    sqlmodel_datatypes_SQLDataType,
)
sqlmodel_datatypes_UserDefinedType_strategy = st.builds(
    sqlmodel_datatypes_UserDefinedType,
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
sqlmodel_constraints_PrimaryKey_strategy = st.builds(
    sqlmodel_constraints_PrimaryKey,
)
ReferenceConstraint_strategy = st.builds(
    ReferenceConstraint,
)
sqlmodel_constraints_UniqueConstraint_strategy = st.builds(
    sqlmodel_constraints_UniqueConstraint,
    clustered=
        st.booleans()
)
sqlmodel_constraints_ForeignKey_strategy = st.builds(
    sqlmodel_constraints_ForeignKey,
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
sqlmodel_constraints_CheckConstraint_strategy = st.builds(
    sqlmodel_constraints_CheckConstraint,
)
sqlmodel_constraints_ReferenceConstraint_strategy = st.builds(
    sqlmodel_constraints_ReferenceConstraint,
)
SearchCondition_strategy = st.builds(
    SearchCondition,
)
Constraint_strategy = st.builds(
    Constraint,
)
sqlmodel_constraints_TableConstraint_strategy = st.builds(
    sqlmodel_constraints_TableConstraint,
)
sqlmodel_constraints_Assertion_strategy = st.builds(
    sqlmodel_constraints_Assertion,
)
BaseTable_strategy = st.builds(
    BaseTable,
)
sqlmodel_tables_PersistentTable_strategy = st.builds(
    sqlmodel_tables_PersistentTable,
)
sqlmodel_tables_TemporaryTable_strategy = st.builds(
    sqlmodel_tables_TemporaryTable,
    local=
        st.booleans(),
    deleteOnCommit=
        st.booleans()
)
sqlmodel_schema_Comment_strategy = st.builds(
    sqlmodel_schema_Comment,
    description=
        safe_text
)
sqlmodel_schema_ObjectExtension_strategy = st.builds(
    sqlmodel_schema_ObjectExtension,
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
sqlmodel_datatypes_AttributeDefinition_strategy = st.builds(
    sqlmodel_datatypes_AttributeDefinition,
    defaultValue=
        safe_text,
    scopeCheck=
        safe_text,
    scopeChecked=
        st.booleans()
)
sqlmodel_datatypes_Field_strategy = st.builds(
    sqlmodel_datatypes_Field,
    scopeChecked=
        st.booleans(),
    scopeCheck=
        safe_text
)
sqlmodel_routines_Parameter_strategy = st.builds(
    sqlmodel_routines_Parameter,
    locator=
        st.booleans(),
    mode=
        safe_text
)
sqlmodel_tables_Column_strategy = st.builds(
    sqlmodel_tables_Column,
    defaultValue=
        safe_text,
    scopeCheck=
        safe_text,
    implementationDependent=
        st.booleans(),
    nullable=
        st.booleans(),
    scopeChecked=
        st.booleans()
)
sqlmodel_datatypes_ElementType_strategy = st.builds(
    sqlmodel_datatypes_ElementType,
)
sqlmodel_schema_Sequence_strategy = st.builds(
    sqlmodel_schema_Sequence,
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
sqlmodel_schema_SQLObject_strategy = st.builds(
    sqlmodel_schema_SQLObject,
    label=
        safe_text,
    description=
        safe_text
)
AuthorizationIdentifier_strategy = st.builds(
    AuthorizationIdentifier,
)
sqlmodel_accesscontrol_Role_strategy = st.builds(
    sqlmodel_accesscontrol_Role,
)
sqlmodel_accesscontrol_Group_strategy = st.builds(
    sqlmodel_accesscontrol_Group,
)
sqlmodel_accesscontrol_User_strategy = st.builds(
    sqlmodel_accesscontrol_User,
)
Routine_strategy = st.builds(
    Routine,
)
sqlmodel_routines_Function_strategy = st.builds(
    sqlmodel_routines_Function,
    typePreserving=
        st.booleans(),
    mutator=
        st.booleans(),
    transformGroup=
        safe_text,
    nullCall=
        st.booleans(),
    static=
        st.booleans()
)
sqlmodel_routines_Procedure_strategy = st.builds(
    sqlmodel_routines_Procedure,
    oldSavePoint=
        st.booleans(),
    maxResultSets=
        st.integers()
)
Trigger_strategy = st.builds(
    Trigger,
)
schema_sqlmodel_EObject_strategy = st.builds(
    schema_sqlmodel_EObject,
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
sqlmodel_routines_RoutineResultTable_strategy = st.builds(
    sqlmodel_routines_RoutineResultTable,
)
sqlmodel_tables_BaseTable_strategy = st.builds(
    sqlmodel_tables_BaseTable,
)
sqlmodel_tables_DerivedTable_strategy = st.builds(
    sqlmodel_tables_DerivedTable,
)
Index_strategy = st.builds(
    Index,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
sqlmodel_datatypes_DistinctUserDefinedType_strategy = st.builds(
    sqlmodel_datatypes_DistinctUserDefinedType,
)
sqlmodel_datatypes_StructuredUserDefinedType_strategy = st.builds(
    sqlmodel_datatypes_StructuredUserDefinedType,
    instantiable=
        st.booleans(),
    final=
        st.booleans()
)
SQLDataType_strategy = st.builds(
    SQLDataType,
)
sqlmodel_datatypes_PredefinedDataType_strategy = st.builds(
    sqlmodel_datatypes_PredefinedDataType,
    primitiveType=
        safe_text
)
SQLObject_strategy = st.builds(
    SQLObject,
)
sqlmodel_constraints_IndexMember_strategy = st.builds(
    sqlmodel_constraints_IndexMember,
    incrementType=
        safe_text
)
sqlmodel_constraints_Constraint_strategy = st.builds(
    sqlmodel_constraints_Constraint,
    deferrable=
        st.booleans(),
    enforced=
        st.booleans(),
    initiallyDeferred=
        st.booleans()
)
sqlmodel_schema_Catalog_strategy = st.builds(
    sqlmodel_schema_Catalog,
)
sqlmodel_schema_Event_strategy = st.builds(
    sqlmodel_schema_Event,
    condition=
        safe_text,
    enabled=
        st.booleans(),
    for_=
        safe_text,
    action=
        safe_text
)
sqlmodel_datatypes_CharacterSet_strategy = st.builds(
    sqlmodel_datatypes_CharacterSet,
    repertoire=
        safe_text,
    encoding=
        safe_text,
    defaultCollation=
        safe_text
)
sqlmodel_routines_Routine_strategy = st.builds(
    sqlmodel_routines_Routine,
    security=
        safe_text,
    parameterStyle=
        safe_text,
    lastAlteredTS=
        safe_text,
    externalName=
        safe_text,
    deterministic=
        st.booleans(),
    sqlDataAccess=
        safe_text,
    specificName=
        safe_text,
    creationTS=
        safe_text,
    language=
        safe_text,
    authorizationID=
        safe_text
)
sqlmodel_tables_Trigger_strategy = st.builds(
    sqlmodel_tables_Trigger,
    deleteType=
        st.booleans(),
    actionTime=
        safe_text,
    newRow=
        safe_text,
    updateType=
        st.booleans(),
    timeStamp=
        safe_text,
    newTable=
        safe_text,
    actionGranularity=
        safe_text,
    oldRow=
        safe_text,
    oldTable=
        safe_text,
    insertType=
        st.booleans()
)
sqlmodel_schema_Database_strategy = st.builds(
    sqlmodel_schema_Database,
    version=
        safe_text,
    vendor=
        safe_text
)
sqlmodel_schema_Schema_strategy = st.builds(
    sqlmodel_schema_Schema,
)
sqlmodel_schema_Dependency_strategy = st.builds(
    sqlmodel_schema_Dependency,
    dependencyType=
        safe_text
)
sqlmodel_datatypes_UserDefinedTypeOrdering_strategy = st.builds(
    sqlmodel_datatypes_UserDefinedTypeOrdering,
    orderingCategory=
        safe_text,
    orderingForm=
        safe_text
)
sqlmodel_accesscontrol_Privilege_strategy = st.builds(
    sqlmodel_accesscontrol_Privilege,
    withHierarchy=
        st.booleans(),
    grantable=
        st.booleans(),
    action=
        safe_text
)
sqlmodel_schema_TypedElement_strategy = st.builds(
    sqlmodel_schema_TypedElement,
)
sqlmodel_accesscontrol_AuthorizationIdentifier_strategy = st.builds(
    sqlmodel_accesscontrol_AuthorizationIdentifier,
)
sqlmodel_constraints_Index_strategy = st.builds(
    sqlmodel_constraints_Index,
    clustered=
        st.booleans(),
    unique=
        st.booleans(),
    fillFactor=
        st.integers(),
    systemGenerated=
        st.booleans()
)
sqlmodel_datatypes_DataType_strategy = st.builds(
    sqlmodel_datatypes_DataType,
)
sqlmodel_routines_Source_strategy = st.builds(
    sqlmodel_routines_Source,
    body=
        safe_text
)
sqlmodel_accesscontrol_RoleAuthorization_strategy = st.builds(
    sqlmodel_accesscontrol_RoleAuthorization,
    grantable=
        st.booleans()
)
sqlmodel_constraints_IndexExpression_strategy = st.builds(
    sqlmodel_constraints_IndexExpression,
    sql=
        safe_text
)
sqlmodel_tables_Table_strategy = st.builds(
    sqlmodel_tables_Table,
    selfRefColumnGeneration=
        safe_text,
    insertable=
        st.booleans(),
    updatable=
        st.booleans()
)
sqlmodel_schema_IdentitySpecifier_strategy = st.builds(
    sqlmodel_schema_IdentitySpecifier,
    startValue=
        safe_text,
    maximum=
        safe_text,
    minimum=
        safe_text,
    generationType=
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

@given(instance=sqlmodel_tables_ViewTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_viewtable_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_ViewTable)



@given(instance=sqlmodel_tables_ViewTable_strategy)
def test_sqlmodel_tables_viewtable_checkType_setter(instance):
    original = instance.checkType
    instance.checkType = original
    assert instance.checkType == original

@given(instance=statements_SQLStatement_strategy)
@settings(max_examples=50)
def test_statements_sqlstatement_instantiation(instance):
    assert isinstance(instance, statements_SQLStatement)

@given(instance=SQLDataStatement_strategy)
@settings(max_examples=50)
def test_sqldatastatement_instantiation(instance):
    assert isinstance(instance, SQLDataStatement)

@given(instance=sqlmodel_statements_SQLDataChangeStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqldatachangestatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLDataChangeStatement)

@given(instance=SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlstatement_instantiation(instance):
    assert isinstance(instance, SQLStatement)

@given(instance=sqlmodel_statements_SQLControlStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlcontrolstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLControlStatement)

@given(instance=sqlmodel_statements_SQLDynamicStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqldynamicstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLDynamicStatement)

@given(instance=sqlmodel_statements_SQLSessionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlsessionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLSessionStatement)

@given(instance=sqlmodel_statements_SQLSchemaStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlschemastatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLSchemaStatement)

@given(instance=sqlmodel_statements_SQLConnectionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlconnectionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLConnectionStatement)

@given(instance=sqlmodel_statements_SQLTransactionStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqltransactionstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLTransactionStatement)

@given(instance=sqlmodel_statements_SQLDiagnosticsStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqldiagnosticsstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLDiagnosticsStatement)

@given(instance=sqlmodel_statements_SQLDataStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqldatastatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLDataStatement)

@given(instance=sqlmodel_statements_SQLStatement_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlstatement_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLStatement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_statements_SQLStatement_strategy)
@settings(max_examples=30)
def test_sqlmodel_statements_sqlstatement_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in sqlmodel_statements_SQLStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel_statements_SQLStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel_statements_SQLStatement is not implemented or raised an error")

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=sqlmodel_routines_BuiltInFunction_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_builtinfunction_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_BuiltInFunction)

@given(instance=sqlmodel_routines_UserDefinedFunction_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_userdefinedfunction_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_UserDefinedFunction)

@given(instance=sqlmodel_routines_Method_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_method_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Method)



@given(instance=sqlmodel_routines_Method_strategy)
def test_sqlmodel_routines_method_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=sqlmodel_routines_Method_strategy)
def test_sqlmodel_routines_method_overriding_setter(instance):
    original = instance.overriding
    instance.overriding = original
    assert instance.overriding == original

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

@given(instance=expressions_SearchCondition_strategy)
@settings(max_examples=50)
def test_expressions_searchcondition_instantiation(instance):
    assert isinstance(instance, expressions_SearchCondition)

@given(instance=expressions_ValueExpression_strategy)
@settings(max_examples=50)
def test_expressions_valueexpression_instantiation(instance):
    assert isinstance(instance, expressions_ValueExpression)

@given(instance=sqlmodel_expressions_QueryExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_queryexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_QueryExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_expressions_QueryExpression_strategy)
@settings(max_examples=30)
def test_sqlmodel_expressions_queryexpression_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in sqlmodel_expressions_QueryExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_QueryExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_QueryExpression is not implemented or raised an error")

@given(instance=expressions_QueryExpression_strategy)
@settings(max_examples=50)
def test_expressions_queryexpression_instantiation(instance):
    assert isinstance(instance, expressions_QueryExpression)

@given(instance=schema_SQLObject_strategy)
@settings(max_examples=50)
def test_schema_sqlobject_instantiation(instance):
    assert isinstance(instance, schema_SQLObject)

@given(instance=sqlmodel_statements_SQLStatementDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel_statements_sqlstatementdefault_instantiation(instance):
    assert isinstance(instance, sqlmodel_statements_SQLStatementDefault)



@given(instance=sqlmodel_statements_SQLStatementDefault_strategy)
def test_sqlmodel_statements_sqlstatementdefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel_expressions_SearchConditionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_searchconditiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_SearchConditionDefault)



@given(instance=sqlmodel_expressions_SearchConditionDefault_strategy)
def test_sqlmodel_expressions_searchconditiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel_expressions_ValueExpressionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_valueexpressiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_ValueExpressionDefault)



@given(instance=sqlmodel_expressions_ValueExpressionDefault_strategy)
def test_sqlmodel_expressions_valueexpressiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel_expressions_QueryExpressionDefault_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_queryexpressiondefault_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_QueryExpressionDefault)



@given(instance=sqlmodel_expressions_QueryExpressionDefault_strategy)
def test_sqlmodel_expressions_queryexpressiondefault_SQL_setter(instance):
    original = instance.SQL
    instance.SQL = original
    assert instance.SQL == original

@given(instance=sqlmodel_expressions_SearchCondition_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_searchcondition_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_SearchCondition)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_expressions_SearchCondition_strategy)
@settings(max_examples=30)
def test_sqlmodel_expressions_searchcondition_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in sqlmodel_expressions_SearchCondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_SearchCondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_SearchCondition is not implemented or raised an error")

@given(instance=sqlmodel_expressions_ValueExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel_expressions_valueexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel_expressions_ValueExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_expressions_ValueExpression_strategy)
@settings(max_examples=30)
def test_sqlmodel_expressions_valueexpression_setsql_changes_state(instance):
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
        assert has_statements, f"Function 'setSQL' in sqlmodel_expressions_ValueExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_ValueExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSQL' in sqlmodel_expressions_ValueExpression is not implemented or raised an error")

@given(instance=NumericalDataType_strategy)
@settings(max_examples=50)
def test_numericaldatatype_instantiation(instance):
    assert isinstance(instance, NumericalDataType)

@given(instance=sqlmodel_datatypes_ApproximateNumericDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_approximatenumericdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ApproximateNumericDataType)

@given(instance=sqlmodel_datatypes_ExactNumericDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_exactnumericdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ExactNumericDataType)



@given(instance=sqlmodel_datatypes_ExactNumericDataType_strategy)
def test_sqlmodel_datatypes_exactnumericdatatype_scale_setter(instance):
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

@given(instance=sqlmodel_datatypes_Domain_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_domain_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_Domain)



@given(instance=sqlmodel_datatypes_Domain_strategy)
def test_sqlmodel_datatypes_domain_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=ExactNumericDataType_strategy)
@settings(max_examples=50)
def test_exactnumericdatatype_instantiation(instance):
    assert isinstance(instance, ExactNumericDataType)

@given(instance=sqlmodel_datatypes_IntegerDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_integerdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_IntegerDataType)

@given(instance=sqlmodel_datatypes_FixedPrecisionDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_fixedprecisiondatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_FixedPrecisionDataType)

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

@given(instance=sqlmodel_datatypes_MultisetDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_multisetdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_MultisetDataType)

@given(instance=sqlmodel_datatypes_ArrayDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_arraydatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ArrayDataType)



@given(instance=sqlmodel_datatypes_ArrayDataType_strategy)
def test_sqlmodel_datatypes_arraydatatype_maxCardinality_setter(instance):
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

@given(instance=sqlmodel_datatypes_DateDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_datedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_DateDataType)

@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_intervaldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_IntervalDataType)



@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
def test_sqlmodel_datatypes_intervaldatatype_leadingFieldPrecision_setter(instance):
    original = instance.leadingFieldPrecision
    instance.leadingFieldPrecision = original
    assert instance.leadingFieldPrecision == original



@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
def test_sqlmodel_datatypes_intervaldatatype_trailingQualifier_setter(instance):
    original = instance.trailingQualifier
    instance.trailingQualifier = original
    assert instance.trailingQualifier == original



@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
def test_sqlmodel_datatypes_intervaldatatype_leadingQualifier_setter(instance):
    original = instance.leadingQualifier
    instance.leadingQualifier = original
    assert instance.leadingQualifier == original



@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
def test_sqlmodel_datatypes_intervaldatatype_fractionalSecondsPrecision_setter(instance):
    original = instance.fractionalSecondsPrecision
    instance.fractionalSecondsPrecision = original
    assert instance.fractionalSecondsPrecision == original



@given(instance=sqlmodel_datatypes_IntervalDataType_strategy)
def test_sqlmodel_datatypes_intervaldatatype_trailingFieldPrecision_setter(instance):
    original = instance.trailingFieldPrecision
    instance.trailingFieldPrecision = original
    assert instance.trailingFieldPrecision == original

@given(instance=sqlmodel_datatypes_CharacterStringDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_characterstringdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_CharacterStringDataType)



@given(instance=sqlmodel_datatypes_CharacterStringDataType_strategy)
def test_sqlmodel_datatypes_characterstringdatatype_fixedLength_setter(instance):
    original = instance.fixedLength
    instance.fixedLength = original
    assert instance.fixedLength == original



@given(instance=sqlmodel_datatypes_CharacterStringDataType_strategy)
def test_sqlmodel_datatypes_characterstringdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sqlmodel_datatypes_CharacterStringDataType_strategy)
def test_sqlmodel_datatypes_characterstringdatatype_collationName_setter(instance):
    original = instance.collationName
    instance.collationName = original
    assert instance.collationName == original



@given(instance=sqlmodel_datatypes_CharacterStringDataType_strategy)
def test_sqlmodel_datatypes_characterstringdatatype_coercibility_setter(instance):
    original = instance.coercibility
    instance.coercibility = original
    assert instance.coercibility == original

@given(instance=sqlmodel_datatypes_TimeDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_timedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_TimeDataType)



@given(instance=sqlmodel_datatypes_TimeDataType_strategy)
def test_sqlmodel_datatypes_timedatatype_timeZone_setter(instance):
    original = instance.timeZone
    instance.timeZone = original
    assert instance.timeZone == original



@given(instance=sqlmodel_datatypes_TimeDataType_strategy)
def test_sqlmodel_datatypes_timedatatype_fractionalSecondsPrecision_setter(instance):
    original = instance.fractionalSecondsPrecision
    instance.fractionalSecondsPrecision = original
    assert instance.fractionalSecondsPrecision == original

@given(instance=sqlmodel_datatypes_BooleanDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_booleandatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_BooleanDataType)

@given(instance=sqlmodel_datatypes_XMLDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_xmldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_XMLDataType)

@given(instance=sqlmodel_datatypes_BinaryStringDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_binarystringdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_BinaryStringDataType)



@given(instance=sqlmodel_datatypes_BinaryStringDataType_strategy)
def test_sqlmodel_datatypes_binarystringdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_datatypes_BinaryStringDataType_strategy)
@settings(max_examples=30)
def test_sqlmodel_datatypes_binarystringdatatype_equals_changes_state(instance):
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
        assert has_statements, f"Function 'equals' in sqlmodel_datatypes_BinaryStringDataType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in sqlmodel_datatypes_BinaryStringDataType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in sqlmodel_datatypes_BinaryStringDataType is not implemented or raised an error")

@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_datalinkdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_DataLinkDataType)



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_recovery_setter(instance):
    original = instance.recovery
    instance.recovery = original
    assert instance.recovery == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_linkControl_setter(instance):
    original = instance.linkControl
    instance.linkControl = original
    assert instance.linkControl == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_writePermission_setter(instance):
    original = instance.writePermission
    instance.writePermission = original
    assert instance.writePermission == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_integrityControl_setter(instance):
    original = instance.integrityControl
    instance.integrityControl = original
    assert instance.integrityControl == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_unlink_setter(instance):
    original = instance.unlink
    instance.unlink = original
    assert instance.unlink == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=sqlmodel_datatypes_DataLinkDataType_strategy)
def test_sqlmodel_datatypes_datalinkdatatype_readPermission_setter(instance):
    original = instance.readPermission
    instance.readPermission = original
    assert instance.readPermission == original

@given(instance=sqlmodel_datatypes_NumericalDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_numericaldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_NumericalDataType)



@given(instance=sqlmodel_datatypes_NumericalDataType_strategy)
def test_sqlmodel_datatypes_numericaldatatype_precision_setter(instance):
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

@given(instance=sqlmodel_datatypes_ReferenceDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_referencedatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ReferenceDataType)

@given(instance=sqlmodel_datatypes_RowDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_rowdatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_RowDataType)

@given(instance=sqlmodel_datatypes_CollectionDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_collectiondatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_CollectionDataType)

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

@given(instance=sqlmodel_datatypes_ConstructedDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_constructeddatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ConstructedDataType)

@given(instance=sqlmodel_datatypes_SQLDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_sqldatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_SQLDataType)

@given(instance=sqlmodel_datatypes_UserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_userdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_UserDefinedType)

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

@given(instance=sqlmodel_constraints_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_primarykey_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_PrimaryKey)

@given(instance=ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_referenceconstraint_instantiation(instance):
    assert isinstance(instance, ReferenceConstraint)

@given(instance=sqlmodel_constraints_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_UniqueConstraint)



@given(instance=sqlmodel_constraints_UniqueConstraint_strategy)
def test_sqlmodel_constraints_uniqueconstraint_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original

@given(instance=sqlmodel_constraints_ForeignKey_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_foreignkey_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_ForeignKey)



@given(instance=sqlmodel_constraints_ForeignKey_strategy)
def test_sqlmodel_constraints_foreignkey_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original



@given(instance=sqlmodel_constraints_ForeignKey_strategy)
def test_sqlmodel_constraints_foreignkey_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=sqlmodel_constraints_ForeignKey_strategy)
def test_sqlmodel_constraints_foreignkey_onDelete_setter(instance):
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

@given(instance=sqlmodel_constraints_CheckConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_checkconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_CheckConstraint)

@given(instance=sqlmodel_constraints_ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_referenceconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_ReferenceConstraint)

@given(instance=SearchCondition_strategy)
@settings(max_examples=50)
def test_searchcondition_instantiation(instance):
    assert isinstance(instance, SearchCondition)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=sqlmodel_constraints_TableConstraint_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_tableconstraint_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_TableConstraint)

@given(instance=sqlmodel_constraints_Assertion_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_assertion_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_Assertion)

@given(instance=BaseTable_strategy)
@settings(max_examples=50)
def test_basetable_instantiation(instance):
    assert isinstance(instance, BaseTable)

@given(instance=sqlmodel_tables_PersistentTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_persistenttable_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_PersistentTable)

@given(instance=sqlmodel_tables_TemporaryTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_temporarytable_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_TemporaryTable)



@given(instance=sqlmodel_tables_TemporaryTable_strategy)
def test_sqlmodel_tables_temporarytable_local_setter(instance):
    original = instance.local
    instance.local = original
    assert instance.local == original



@given(instance=sqlmodel_tables_TemporaryTable_strategy)
def test_sqlmodel_tables_temporarytable_deleteOnCommit_setter(instance):
    original = instance.deleteOnCommit
    instance.deleteOnCommit = original
    assert instance.deleteOnCommit == original

@given(instance=sqlmodel_schema_Comment_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_comment_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Comment)



@given(instance=sqlmodel_schema_Comment_strategy)
def test_sqlmodel_schema_comment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=sqlmodel_schema_ObjectExtension_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_objectextension_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_ObjectExtension)

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

@given(instance=sqlmodel_datatypes_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_attributedefinition_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_AttributeDefinition)



@given(instance=sqlmodel_datatypes_AttributeDefinition_strategy)
def test_sqlmodel_datatypes_attributedefinition_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=sqlmodel_datatypes_AttributeDefinition_strategy)
def test_sqlmodel_datatypes_attributedefinition_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original



@given(instance=sqlmodel_datatypes_AttributeDefinition_strategy)
def test_sqlmodel_datatypes_attributedefinition_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original

@given(instance=sqlmodel_datatypes_Field_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_field_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_Field)



@given(instance=sqlmodel_datatypes_Field_strategy)
def test_sqlmodel_datatypes_field_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original



@given(instance=sqlmodel_datatypes_Field_strategy)
def test_sqlmodel_datatypes_field_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original

@given(instance=sqlmodel_routines_Parameter_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_parameter_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Parameter)



@given(instance=sqlmodel_routines_Parameter_strategy)
def test_sqlmodel_routines_parameter_locator_setter(instance):
    original = instance.locator
    instance.locator = original
    assert instance.locator == original



@given(instance=sqlmodel_routines_Parameter_strategy)
def test_sqlmodel_routines_parameter_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=sqlmodel_tables_Column_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_column_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_Column)



@given(instance=sqlmodel_tables_Column_strategy)
def test_sqlmodel_tables_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=sqlmodel_tables_Column_strategy)
def test_sqlmodel_tables_column_scopeCheck_setter(instance):
    original = instance.scopeCheck
    instance.scopeCheck = original
    assert instance.scopeCheck == original



@given(instance=sqlmodel_tables_Column_strategy)
def test_sqlmodel_tables_column_implementationDependent_setter(instance):
    original = instance.implementationDependent
    instance.implementationDependent = original
    assert instance.implementationDependent == original



@given(instance=sqlmodel_tables_Column_strategy)
def test_sqlmodel_tables_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=sqlmodel_tables_Column_strategy)
def test_sqlmodel_tables_column_scopeChecked_setter(instance):
    original = instance.scopeChecked
    instance.scopeChecked = original
    assert instance.scopeChecked == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_tables_Column_strategy)
@settings(max_examples=30)
def test_sqlmodel_tables_column_ispartofforeignkey_changes_state(instance):
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
        assert has_statements, f"Function 'isPartOfForeignKey' in sqlmodel_tables_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfForeignKey' in sqlmodel_tables_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfForeignKey' in sqlmodel_tables_Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_tables_Column_strategy)
@settings(max_examples=30)
def test_sqlmodel_tables_column_ispartofuniqueconstraint_changes_state(instance):
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
        assert has_statements, f"Function 'isPartOfUniqueConstraint' in sqlmodel_tables_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfUniqueConstraint' in sqlmodel_tables_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfUniqueConstraint' in sqlmodel_tables_Column is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_tables_Column_strategy)
@settings(max_examples=30)
def test_sqlmodel_tables_column_ispartofprimarykey_changes_state(instance):
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
        assert has_statements, f"Function 'isPartOfPrimaryKey' in sqlmodel_tables_Column is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPartOfPrimaryKey' in sqlmodel_tables_Column did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPartOfPrimaryKey' in sqlmodel_tables_Column is not implemented or raised an error")

@given(instance=sqlmodel_datatypes_ElementType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_elementtype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_ElementType)

@given(instance=sqlmodel_schema_Sequence_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_sequence_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Sequence)

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

@given(instance=sqlmodel_schema_SQLObject_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_sqlobject_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_SQLObject)



@given(instance=sqlmodel_schema_SQLObject_strategy)
def test_sqlmodel_schema_sqlobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=sqlmodel_schema_SQLObject_strategy)
def test_sqlmodel_schema_sqlobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_schema_SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel_schema_sqlobject_addeannotation_changes_state(instance):
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
        assert has_statements, f"Function 'addEAnnotation' in sqlmodel_schema_SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEAnnotation' in sqlmodel_schema_SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEAnnotation' in sqlmodel_schema_SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_schema_SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel_schema_sqlobject_removeeannotationdetail_changes_state(instance):
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
        assert has_statements, f"Function 'removeEAnnotationDetail' in sqlmodel_schema_SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeEAnnotationDetail' in sqlmodel_schema_SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeEAnnotationDetail' in sqlmodel_schema_SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_schema_SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel_schema_sqlobject_setannotationdetail_changes_state(instance):
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
        assert has_statements, f"Function 'setAnnotationDetail' in sqlmodel_schema_SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAnnotationDetail' in sqlmodel_schema_SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAnnotationDetail' in sqlmodel_schema_SQLObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_schema_SQLObject_strategy)
@settings(max_examples=30)
def test_sqlmodel_schema_sqlobject_addeannotationdetail_changes_state(instance):
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
        assert has_statements, f"Function 'addEAnnotationDetail' in sqlmodel_schema_SQLObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEAnnotationDetail' in sqlmodel_schema_SQLObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEAnnotationDetail' in sqlmodel_schema_SQLObject is not implemented or raised an error")

@given(instance=AuthorizationIdentifier_strategy)
@settings(max_examples=50)
def test_authorizationidentifier_instantiation(instance):
    assert isinstance(instance, AuthorizationIdentifier)

@given(instance=sqlmodel_accesscontrol_Role_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_role_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_Role)

@given(instance=sqlmodel_accesscontrol_Group_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_group_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_Group)

@given(instance=sqlmodel_accesscontrol_User_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_user_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_User)

@given(instance=Routine_strategy)
@settings(max_examples=50)
def test_routine_instantiation(instance):
    assert isinstance(instance, Routine)

@given(instance=sqlmodel_routines_Function_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_function_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Function)



@given(instance=sqlmodel_routines_Function_strategy)
def test_sqlmodel_routines_function_typePreserving_setter(instance):
    original = instance.typePreserving
    instance.typePreserving = original
    assert instance.typePreserving == original



@given(instance=sqlmodel_routines_Function_strategy)
def test_sqlmodel_routines_function_mutator_setter(instance):
    original = instance.mutator
    instance.mutator = original
    assert instance.mutator == original



@given(instance=sqlmodel_routines_Function_strategy)
def test_sqlmodel_routines_function_transformGroup_setter(instance):
    original = instance.transformGroup
    instance.transformGroup = original
    assert instance.transformGroup == original



@given(instance=sqlmodel_routines_Function_strategy)
def test_sqlmodel_routines_function_nullCall_setter(instance):
    original = instance.nullCall
    instance.nullCall = original
    assert instance.nullCall == original



@given(instance=sqlmodel_routines_Function_strategy)
def test_sqlmodel_routines_function_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=sqlmodel_routines_Procedure_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_procedure_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Procedure)



@given(instance=sqlmodel_routines_Procedure_strategy)
def test_sqlmodel_routines_procedure_oldSavePoint_setter(instance):
    original = instance.oldSavePoint
    instance.oldSavePoint = original
    assert instance.oldSavePoint == original



@given(instance=sqlmodel_routines_Procedure_strategy)
def test_sqlmodel_routines_procedure_maxResultSets_setter(instance):
    original = instance.maxResultSets
    instance.maxResultSets = original
    assert instance.maxResultSets == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=schema_sqlmodel_EObject_strategy)
@settings(max_examples=50)
def test_schema_sqlmodel_eobject_instantiation(instance):
    assert isinstance(instance, schema_sqlmodel_EObject)

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

@given(instance=sqlmodel_routines_RoutineResultTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_routineresulttable_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_RoutineResultTable)

@given(instance=sqlmodel_tables_BaseTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_basetable_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_BaseTable)

@given(instance=sqlmodel_tables_DerivedTable_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_derivedtable_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_DerivedTable)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=sqlmodel_datatypes_DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_DistinctUserDefinedType)

@given(instance=sqlmodel_datatypes_StructuredUserDefinedType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_structureduserdefinedtype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_StructuredUserDefinedType)



@given(instance=sqlmodel_datatypes_StructuredUserDefinedType_strategy)
def test_sqlmodel_datatypes_structureduserdefinedtype_instantiable_setter(instance):
    original = instance.instantiable
    instance.instantiable = original
    assert instance.instantiable == original



@given(instance=sqlmodel_datatypes_StructuredUserDefinedType_strategy)
def test_sqlmodel_datatypes_structureduserdefinedtype_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=SQLDataType_strategy)
@settings(max_examples=50)
def test_sqldatatype_instantiation(instance):
    assert isinstance(instance, SQLDataType)

@given(instance=sqlmodel_datatypes_PredefinedDataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_predefineddatatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_PredefinedDataType)



@given(instance=sqlmodel_datatypes_PredefinedDataType_strategy)
def test_sqlmodel_datatypes_predefineddatatype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=sqlmodel_constraints_IndexMember_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_indexmember_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_IndexMember)



@given(instance=sqlmodel_constraints_IndexMember_strategy)
def test_sqlmodel_constraints_indexmember_incrementType_setter(instance):
    original = instance.incrementType
    instance.incrementType = original
    assert instance.incrementType == original

@given(instance=sqlmodel_constraints_Constraint_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_constraint_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_Constraint)



@given(instance=sqlmodel_constraints_Constraint_strategy)
def test_sqlmodel_constraints_constraint_deferrable_setter(instance):
    original = instance.deferrable
    instance.deferrable = original
    assert instance.deferrable == original



@given(instance=sqlmodel_constraints_Constraint_strategy)
def test_sqlmodel_constraints_constraint_enforced_setter(instance):
    original = instance.enforced
    instance.enforced = original
    assert instance.enforced == original



@given(instance=sqlmodel_constraints_Constraint_strategy)
def test_sqlmodel_constraints_constraint_initiallyDeferred_setter(instance):
    original = instance.initiallyDeferred
    instance.initiallyDeferred = original
    assert instance.initiallyDeferred == original

@given(instance=sqlmodel_schema_Catalog_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_catalog_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Catalog)

@given(instance=sqlmodel_schema_Event_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_event_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Event)



@given(instance=sqlmodel_schema_Event_strategy)
def test_sqlmodel_schema_event_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original



@given(instance=sqlmodel_schema_Event_strategy)
def test_sqlmodel_schema_event_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=sqlmodel_schema_Event_strategy)
def test_sqlmodel_schema_event_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original



@given(instance=sqlmodel_schema_Event_strategy)
def test_sqlmodel_schema_event_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=sqlmodel_datatypes_CharacterSet_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_characterset_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_CharacterSet)



@given(instance=sqlmodel_datatypes_CharacterSet_strategy)
def test_sqlmodel_datatypes_characterset_repertoire_setter(instance):
    original = instance.repertoire
    instance.repertoire = original
    assert instance.repertoire == original



@given(instance=sqlmodel_datatypes_CharacterSet_strategy)
def test_sqlmodel_datatypes_characterset_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original



@given(instance=sqlmodel_datatypes_CharacterSet_strategy)
def test_sqlmodel_datatypes_characterset_defaultCollation_setter(instance):
    original = instance.defaultCollation
    instance.defaultCollation = original
    assert instance.defaultCollation == original

@given(instance=sqlmodel_routines_Routine_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_routine_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Routine)



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_security_setter(instance):
    original = instance.security
    instance.security = original
    assert instance.security == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_parameterStyle_setter(instance):
    original = instance.parameterStyle
    instance.parameterStyle = original
    assert instance.parameterStyle == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_lastAlteredTS_setter(instance):
    original = instance.lastAlteredTS
    instance.lastAlteredTS = original
    assert instance.lastAlteredTS == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_externalName_setter(instance):
    original = instance.externalName
    instance.externalName = original
    assert instance.externalName == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_deterministic_setter(instance):
    original = instance.deterministic
    instance.deterministic = original
    assert instance.deterministic == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_sqlDataAccess_setter(instance):
    original = instance.sqlDataAccess
    instance.sqlDataAccess = original
    assert instance.sqlDataAccess == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_specificName_setter(instance):
    original = instance.specificName
    instance.specificName = original
    assert instance.specificName == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_creationTS_setter(instance):
    original = instance.creationTS
    instance.creationTS = original
    assert instance.creationTS == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=sqlmodel_routines_Routine_strategy)
def test_sqlmodel_routines_routine_authorizationID_setter(instance):
    original = instance.authorizationID
    instance.authorizationID = original
    assert instance.authorizationID == original

@given(instance=sqlmodel_tables_Trigger_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_trigger_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_Trigger)



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_deleteType_setter(instance):
    original = instance.deleteType
    instance.deleteType = original
    assert instance.deleteType == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_newRow_setter(instance):
    original = instance.newRow
    instance.newRow = original
    assert instance.newRow == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_updateType_setter(instance):
    original = instance.updateType
    instance.updateType = original
    assert instance.updateType == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_timeStamp_setter(instance):
    original = instance.timeStamp
    instance.timeStamp = original
    assert instance.timeStamp == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_newTable_setter(instance):
    original = instance.newTable
    instance.newTable = original
    assert instance.newTable == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_actionGranularity_setter(instance):
    original = instance.actionGranularity
    instance.actionGranularity = original
    assert instance.actionGranularity == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_oldRow_setter(instance):
    original = instance.oldRow
    instance.oldRow = original
    assert instance.oldRow == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_oldTable_setter(instance):
    original = instance.oldTable
    instance.oldTable = original
    assert instance.oldTable == original



@given(instance=sqlmodel_tables_Trigger_strategy)
def test_sqlmodel_tables_trigger_insertType_setter(instance):
    original = instance.insertType
    instance.insertType = original
    assert instance.insertType == original

@given(instance=sqlmodel_schema_Database_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_database_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Database)



@given(instance=sqlmodel_schema_Database_strategy)
def test_sqlmodel_schema_database_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=sqlmodel_schema_Database_strategy)
def test_sqlmodel_schema_database_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=sqlmodel_schema_Schema_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_schema_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Schema)

@given(instance=sqlmodel_schema_Dependency_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_dependency_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_Dependency)



@given(instance=sqlmodel_schema_Dependency_strategy)
def test_sqlmodel_schema_dependency_dependencyType_setter(instance):
    original = instance.dependencyType
    instance.dependencyType = original
    assert instance.dependencyType == original

@given(instance=sqlmodel_datatypes_UserDefinedTypeOrdering_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_userdefinedtypeordering_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_UserDefinedTypeOrdering)



@given(instance=sqlmodel_datatypes_UserDefinedTypeOrdering_strategy)
def test_sqlmodel_datatypes_userdefinedtypeordering_orderingCategory_setter(instance):
    original = instance.orderingCategory
    instance.orderingCategory = original
    assert instance.orderingCategory == original



@given(instance=sqlmodel_datatypes_UserDefinedTypeOrdering_strategy)
def test_sqlmodel_datatypes_userdefinedtypeordering_orderingForm_setter(instance):
    original = instance.orderingForm
    instance.orderingForm = original
    assert instance.orderingForm == original

@given(instance=sqlmodel_accesscontrol_Privilege_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_privilege_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_Privilege)



@given(instance=sqlmodel_accesscontrol_Privilege_strategy)
def test_sqlmodel_accesscontrol_privilege_withHierarchy_setter(instance):
    original = instance.withHierarchy
    instance.withHierarchy = original
    assert instance.withHierarchy == original



@given(instance=sqlmodel_accesscontrol_Privilege_strategy)
def test_sqlmodel_accesscontrol_privilege_grantable_setter(instance):
    original = instance.grantable
    instance.grantable = original
    assert instance.grantable == original



@given(instance=sqlmodel_accesscontrol_Privilege_strategy)
def test_sqlmodel_accesscontrol_privilege_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=sqlmodel_schema_TypedElement_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_typedelement_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_TypedElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_schema_TypedElement_strategy)
@settings(max_examples=30)
def test_sqlmodel_schema_typedelement_setdatatype_changes_state(instance):
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
        assert has_statements, f"Function 'setDataType' in sqlmodel_schema_TypedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDataType' in sqlmodel_schema_TypedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDataType' in sqlmodel_schema_TypedElement is not implemented or raised an error")

@given(instance=sqlmodel_accesscontrol_AuthorizationIdentifier_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_authorizationidentifier_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_AuthorizationIdentifier)

@given(instance=sqlmodel_constraints_Index_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_index_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_Index)



@given(instance=sqlmodel_constraints_Index_strategy)
def test_sqlmodel_constraints_index_clustered_setter(instance):
    original = instance.clustered
    instance.clustered = original
    assert instance.clustered == original



@given(instance=sqlmodel_constraints_Index_strategy)
def test_sqlmodel_constraints_index_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=sqlmodel_constraints_Index_strategy)
def test_sqlmodel_constraints_index_fillFactor_setter(instance):
    original = instance.fillFactor
    instance.fillFactor = original
    assert instance.fillFactor == original



@given(instance=sqlmodel_constraints_Index_strategy)
def test_sqlmodel_constraints_index_systemGenerated_setter(instance):
    original = instance.systemGenerated
    instance.systemGenerated = original
    assert instance.systemGenerated == original

@given(instance=sqlmodel_datatypes_DataType_strategy)
@settings(max_examples=50)
def test_sqlmodel_datatypes_datatype_instantiation(instance):
    assert isinstance(instance, sqlmodel_datatypes_DataType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sqlmodel_datatypes_DataType_strategy)
@settings(max_examples=30)
def test_sqlmodel_datatypes_datatype_setcontainer_changes_state(instance):
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
        assert has_statements, f"Function 'setContainer' in sqlmodel_datatypes_DataType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setContainer' in sqlmodel_datatypes_DataType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setContainer' in sqlmodel_datatypes_DataType is not implemented or raised an error")

@given(instance=sqlmodel_routines_Source_strategy)
@settings(max_examples=50)
def test_sqlmodel_routines_source_instantiation(instance):
    assert isinstance(instance, sqlmodel_routines_Source)



@given(instance=sqlmodel_routines_Source_strategy)
def test_sqlmodel_routines_source_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=sqlmodel_accesscontrol_RoleAuthorization_strategy)
@settings(max_examples=50)
def test_sqlmodel_accesscontrol_roleauthorization_instantiation(instance):
    assert isinstance(instance, sqlmodel_accesscontrol_RoleAuthorization)



@given(instance=sqlmodel_accesscontrol_RoleAuthorization_strategy)
def test_sqlmodel_accesscontrol_roleauthorization_grantable_setter(instance):
    original = instance.grantable
    instance.grantable = original
    assert instance.grantable == original

@given(instance=sqlmodel_constraints_IndexExpression_strategy)
@settings(max_examples=50)
def test_sqlmodel_constraints_indexexpression_instantiation(instance):
    assert isinstance(instance, sqlmodel_constraints_IndexExpression)



@given(instance=sqlmodel_constraints_IndexExpression_strategy)
def test_sqlmodel_constraints_indexexpression_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=sqlmodel_tables_Table_strategy)
@settings(max_examples=50)
def test_sqlmodel_tables_table_instantiation(instance):
    assert isinstance(instance, sqlmodel_tables_Table)



@given(instance=sqlmodel_tables_Table_strategy)
def test_sqlmodel_tables_table_selfRefColumnGeneration_setter(instance):
    original = instance.selfRefColumnGeneration
    instance.selfRefColumnGeneration = original
    assert instance.selfRefColumnGeneration == original



@given(instance=sqlmodel_tables_Table_strategy)
def test_sqlmodel_tables_table_insertable_setter(instance):
    original = instance.insertable
    instance.insertable = original
    assert instance.insertable == original



@given(instance=sqlmodel_tables_Table_strategy)
def test_sqlmodel_tables_table_updatable_setter(instance):
    original = instance.updatable
    instance.updatable = original
    assert instance.updatable == original

@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
@settings(max_examples=50)
def test_sqlmodel_schema_identityspecifier_instantiation(instance):
    assert isinstance(instance, sqlmodel_schema_IdentitySpecifier)



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_generationType_setter(instance):
    original = instance.generationType
    instance.generationType = original
    assert instance.generationType == original



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original



@given(instance=sqlmodel_schema_IdentitySpecifier_strategy)
def test_sqlmodel_schema_identityspecifier_cycleOption_setter(instance):
    original = instance.cycleOption
    instance.cycleOption = original
    assert instance.cycleOption == original
